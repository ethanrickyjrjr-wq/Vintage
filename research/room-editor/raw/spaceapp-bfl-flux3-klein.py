import glob
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
_wheel = glob.glob(os.path.join(HERE, "diffusers-*.whl"))
if _wheel:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--no-deps", "--no-cache-dir", _wheel[0]])

import spaces
import time
from spaces.config import Config as SPACES_CONFIG
import base64
import html
import io
import json
import random
import re
import tempfile
from pathlib import Path
from urllib.parse import unquote

import gradio as gr
import numpy as np
import safetensors.torch
import torch
from gradio.workflow_api import _active_blocks
from gradio_client import utils as client_utils
from openai import OpenAI
from huggingface_hub import HfApi, InferenceClient, hf_hub_download, snapshot_download
from PIL import Image, ImageDraw, ImageFont
from transformers import AutoProcessor, Qwen3VLForConditionalGeneration

from diffusers import AutoencoderKLFlux2, Flux3Transformer2DModel
from diffusers.modular_pipelines import Flux3AutoBlocks, Flux3DistilledAutoBlocks
from vae_convert import convert_flux2_vae_checkpoint_to_diffusers

dtype = torch.bfloat16
token = os.environ.get("HF_TOKEN")

MAX_SEED = np.iinfo(np.int32).max
MAX_IMAGE_SIZE = 4096
MAX_REF_PIXELS = 1024 * 1024
MAX_STEPS = 50

hf_client = InferenceClient(api_key=os.environ.get("INFERENCE_TOKEN") or token)
pup_client = OpenAI(base_url=os.environ["PUP_URL"].rstrip("/") + "/v1", api_key=os.environ["PUP_TOKEN"], timeout=60)
PUP_MODEL = "black-forest-labs/flux-3-image-klein-pup"
VLM_MODEL = "Qwen/Qwen3-VL-235B-A22B-Instruct"

# The system prompts of the FLUX 3 Image Klein prompt upsampler (black-forest-labs/flux-3-image-klein-pup), sent to the
# upsampler itself on its Inference Endpoint (pup_client). Same prompts and the same instruction scaffold as the reference code.
PUP_REPO = "black-forest-labs/flux-3-image-klein-pup"
UPSAMPLER_PROMPTS = json.loads(Path(hf_hub_download(PUP_REPO, "system_prompts.json", token=token)).read_text())
I2I_SCAFFOLD = ("Reference images follow in order (the first image, the second image, ...).\n"
                "User request: {instruction}\n"
                "Output the caption.")

def first_available(*repos):
    api = HfApi(token=token)
    for repo in repos:
        try:
            api.model_info(repo)
            return repo
        except Exception:
            continue
    raise RuntimeError(f"None of {repos} is accessible with the configured HF_TOKEN")


BASE_REPO = first_available("black-forest-labs/flux-3-image-klein-base", "black-forest-labs/flux-3-image-small")
DISTILLED_REPO = first_available("black-forest-labs/flux-3-image-klein", "black-forest-labs/flux-3-image-small-sd")
print(f"Base: {BASE_REPO} | Distilled: {DISTILLED_REPO}")

print("Loading text encoder...")
text_encoder = Qwen3VLForConditionalGeneration.from_pretrained(
    BASE_REPO, subfolder="text_encoder", dtype=dtype, token=token
)
processor = AutoProcessor.from_pretrained(BASE_REPO, subfolder="text_encoder", token=token)

print("Loading VAE...")
vae = AutoencoderKLFlux2()
_ae = safetensors.torch.load_file(hf_hub_download(BASE_REPO, "ae.safetensors", token=token))
vae.load_state_dict(convert_flux2_vae_checkpoint_to_diffusers(_ae, vae.config), strict=True)
vae.to(torch.float32).eval()
# Decode in 2048 px tiles when a side is over 2048 px: a 4K decode in one piece runs out of memory on ZeroGPU.
vae.use_tiling = True
vae.tile_sample_min_size = 2048
vae.tile_latent_min_size = 2048 // (2 ** (len(vae.config.block_out_channels) - 1))
del _ae


def load_transformer(repo, config_dir):
    transformer = Flux3Transformer2DModel.from_single_file(
        f"https://huggingface.co/{repo}/blob/main/model.safetensors",
        config=os.path.join(HERE, "configs", config_dir),
        subfolder="transformer",
        torch_dtype=dtype,
        token=token,
    )
    for name in Flux3Transformer2DModel._keep_in_fp32_modules:
        for module_name, module in transformer.named_modules():
            if module_name.split(".")[-1] == name:
                module.to(torch.float32)
    return transformer


print("Loading Base transformer...")
transformer_base = load_transformer(BASE_REPO, "base")
print("Loading Distilled transformer...")
transformer_distilled = load_transformer(DISTILLED_REPO, "distilled")

pipe_regular = Flux3AutoBlocks().init_pipeline()
pipe_regular.update_components(
    text_encoder=text_encoder, tokenizer=processor, vae=vae, transformer=transformer_base
)
pipe_regular.to("cuda")

pipe_distilled = Flux3DistilledAutoBlocks().init_pipeline()
pipe_distilled.update_components(
    text_encoder=text_encoder, tokenizer=processor, vae=vae, transformer=transformer_distilled
)
pipe_distilled.to("cuda")


AOTI_REPOS = {
    "base": "diffusers-internal-dev/f3-small-img-aoti-sm120",
    "distilled": "diffusers-internal-dev/f3-small-image-distilled-aoti-sm120",
}
aoti_token = os.environ.get("AOTI_TOKEN") or token


def with_eager_fallback(compiled, eager, label):
    warned = []

    def forward(*args, **kwargs):
        try:
            return compiled(*args, **kwargs)
        except Exception as e:
            if not warned:
                warned.append(True)
                print(f"AOTI {label} fell back to eager: {e!r}")
            return eager(*args, **kwargs)

    return forward


def load_aoti(transformer, repo, label):
    from spaces.zero.torch.aoti import aoti_load_from_package_dir

    config = json.loads(Path(hf_hub_download(repo, "config.json", token=aoti_token)).read_text())
    if config.get("torch") != torch.__version__:
        raise RuntimeError(f"built for torch {config.get('torch')}, runtime has {torch.__version__}")
    package_dir = Path(snapshot_download(repo, allow_patterns="package/*", token=aoti_token)) / "package"

    def blocks(name):
        stack = transformer.get_submodule(name)
        return list(stack) if isinstance(stack, torch.nn.ModuleList) else [stack]

    names = list(config["stacks"])
    for name in names:
        for block in blocks(name):
            block.attn.norm_q.to(torch.bfloat16)
            block.attn.norm_k.to(torch.bfloat16)
    eager = {name: [block.forward for block in blocks(name)] for name in names}
    aoti_load_from_package_dir(transformer, package_dir)
    for name in names:
        for block, eager_forward in zip(blocks(name), eager[name]):
            block.forward = with_eager_fallback(block.forward, eager_forward, f"{label}/{name}")
    print(f"AOTI {label}: {len(names)} stacks from {repo}")


AOTI_LOADED = {}
for label, transformer in [("base", transformer_base), ("distilled", transformer_distilled)] if os.environ.get("AOTI", "1") != "0" else []:
    try:
        load_aoti(transformer, AOTI_REPOS[label], label)
        AOTI_LOADED[label] = True
    except Exception as e:
        AOTI_LOADED[label] = False
        print(f"AOTI {label} unavailable, running eager: {e!r}")
print(f"AOTI loaded: {AOTI_LOADED}")

DISTILLED = "Distilled (16 steps)"
BASE = "Base (50 steps)"

pipes = {
    DISTILLED: pipe_distilled,
    BASE: pipe_regular,
}

STEP_SECONDS_AT_4K = 0.5

DEFAULT_STEPS = {
    DISTILLED: 16,
    BASE: 50,
}

DEFAULT_CFG = {
    DISTILLED: 1.0,
    BASE: 4.0,
}


def image_to_data_uri(img):
    buffered = io.BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
    return f"data:image/png;base64,{img_str}"


def upsample_prompt_logic(prompt, image_list):
    """The caption the model receives, from the upsampler's prompts: t2i on the request alone, i2i with the references."""
    try:
        if image_list and len(image_list) > 0:
            user_content = [{"type": "image_url", "image_url": {"url": image_to_data_uri(img)}} for img in image_list]
            user_content.append({"type": "text", "text": I2I_SCAFFOLD.format(instruction=prompt)})
            messages = [
                {"role": "system", "content": UPSAMPLER_PROMPTS["i2i"]},
                {"role": "user", "content": user_content},
            ]
        else:
            messages = [
                {"role": "system", "content": UPSAMPLER_PROMPTS["t2i"]},
                {"role": "user", "content": prompt},
            ]

        completion = pup_client.chat.completions.create(model=PUP_MODEL, messages=messages, max_tokens=1024, temperature=0.0,
            extra_body={"chat_template_kwargs": {"enable_thinking": False}})
        caption = (completion.choices[0].message.content or "").strip()
        return caption or prompt
    except Exception as e:
        print(f"Upsampling failed: {e}")
        raise gr.Error("Prompt upsampler unavailable, please retry")


def fit_reference(img, max_pixels=MAX_REF_PIXELS):
    img = img.convert("RGB")
    pixels = img.width * img.height
    if pixels <= max_pixels:
        return img
    scale = (max_pixels / pixels) ** 0.5
    return img.resize((max(16, round(img.width * scale)), max(16, round(img.height * scale))), Image.LANCZOS)


RESOLUTIONS = {
    "1K": 1024,
    "2K": 2048,
    "4K": 4096,
}
# Distilled 4K runs on a full ZeroGPU GPU (xlarge, ~135 s). Base at 2K/4K is not offered in the UI.
MODE_RESOLUTIONS = {
    DISTILLED: ["1K", "2K", "4K"],
    BASE: ["1K"],
}
DEFAULT_RESOLUTION = {
    DISTILLED: "2K",
    BASE: "1K",
}


def update_dimensions_from_image(image_list, resolution="1K"):
    """
    Match width/height to the first uploaded image: the selected resolution's pixel count at its aspect ratio, multiples of 16.
    """
    if image_list is None or len(image_list) == 0:
        return dimensions_for_aspect(1.0, resolution)

    img = image_list[0][0] if isinstance(image_list[0], (tuple, list)) else image_list[0]
    return dimensions_for_aspect(img.width / img.height, resolution)


def dimensions_for_aspect(aspect_ratio, resolution="1K"):
    side = RESOLUTIONS.get(resolution, 1024)
    new_height = (side * side / aspect_ratio) ** 0.5
    new_width = new_height * aspect_ratio

    scale = min(1.0, MAX_IMAGE_SIZE / max(new_width, new_height))
    new_width = max(256, min(MAX_IMAGE_SIZE, round(new_width * scale / 16) * 16))
    new_height = max(256, min(MAX_IMAGE_SIZE, round(new_height * scale / 16) * 16))

    return new_width, new_height


def update_steps_from_mode(mode_choice, aspect, image_list):
    """
    Update inference steps, guidance scale and the resolution menu based on the selected mode.
    """
    res = DEFAULT_RESOLUTION[mode_choice]
    width, height = set_aspect(aspect, image_list, res)
    return (
        gr.update(value=DEFAULT_STEPS[mode_choice]),
        gr.update(value=DEFAULT_CFG[mode_choice], interactive=mode_choice == BASE),
        gr.Radio(choices=MODE_RESOLUTIONS[mode_choice], value=res),
        width,
        height,
    )


def get_duration(
    prompt,
    input_images=None,
    mode_choice=DISTILLED,
    seed=42,
    randomize_seed=False,
    width=1024,
    height=1024,
    num_inference_steps=16,
    guidance_scale=4.0,
    prompt_upsampling=False,
    progress=None,
):
    tokens = int(width) * int(height) / 256 + 512
    for item in input_images or []:
        img = item[0] if isinstance(item, (tuple, list)) else item
        if isinstance(img, str):
            img = Image.open(img)
        tokens += min(img.width * img.height, MAX_REF_PIXELS) / 256
    passes = 2 if mode_choice == BASE else 1
    step_seconds = STEP_SECONDS_AT_4K * (tokens / 4608) ** 1.5
    estimate = 15 + int(num_inference_steps) * passes * step_seconds
    return int(min(max(estimate, 20), 300))


XL_STEP_SECONDS_AT_4K = 8.4


def get_duration_xl(
    prompt,
    input_images=None,
    mode_choice=DISTILLED,
    seed=42,
    randomize_seed=False,
    width=1024,
    height=1024,
    num_inference_steps=16,
    guidance_scale=4.0,
    prompt_upsampling=False,
    progress=None,
):
    """GPU seconds for a full RTX Pro 6000 (ZeroGPU xlarge, no duration factor; costs 2x quota)."""
    tokens = int(width) * int(height) / 256 + 512
    for item in input_images or []:
        img = item[0] if isinstance(item, (tuple, list)) else item
        if isinstance(img, str):
            img = Image.open(img)
        tokens += min(img.width * img.height, MAX_REF_PIXELS) / 256
    passes = 2 if mode_choice == BASE else 1
    step_seconds = XL_STEP_SECONDS_AT_4K * (tokens / 66048) ** 1.5
    estimate = 20 + 1.3 * int(num_inference_steps) * passes * step_seconds
    return int(min(max(estimate, 30), 300))


def _infer_gpu_body(
    prompt: str,
    input_images=None,
    mode_choice: str = DISTILLED,
    seed: int = 42,
    randomize_seed: bool = False,
    width: int = 1024,
    height: int = 1024,
    num_inference_steps: int = 16,
    guidance_scale: float = 4.0,
    prompt_upsampling: bool = False,
    progress=gr.Progress(track_tqdm=True),
):
    """GPU half of infer(): generates from a caption that is already final."""
    if isinstance(seed, str):
        seed = int(seed)
    if isinstance(randomize_seed, str):
        randomize_seed = randomize_seed.lower() == "true"
    if isinstance(width, str):
        width = int(width)
    if isinstance(height, str):
        height = int(height)
    if isinstance(num_inference_steps, str):
        num_inference_steps = int(num_inference_steps)
    if isinstance(guidance_scale, str):
        guidance_scale = float(guidance_scale)
    if isinstance(prompt_upsampling, str):
        prompt_upsampling = prompt_upsampling.lower() == "true"

    if randomize_seed:
        seed = random.randint(0, MAX_SEED)

    width = round(width / 16) * 16
    height = round(height / 16) * 16
    num_inference_steps = max(1, min(int(num_inference_steps), MAX_STEPS))

    pipe = pipes[mode_choice]

    image_list = None
    if input_images is not None and len(input_images) > 0:
        image_list = [fit_reference(item[0] if isinstance(item, (tuple, list)) else item) for item in input_images]

    # The caption arrives already upsampled; infer() runs the upsampler before the GPU is allocated.
    final_prompt = prompt

    if progress is not None:
        progress(0.2, desc=f"Generating image with {mode_choice}...")

    if mode_choice == BASE:
        pipe.guider = pipe.guider.new(guidance_scale=guidance_scale)

    pipe_kwargs = {
        "prompt": final_prompt,
        "height": height,
        "width": width,
        "num_inference_steps": num_inference_steps,
        "generator": torch.Generator().manual_seed(seed),
        "output": "images",
    }
    if image_list is not None:
        pipe_kwargs["image"] = image_list

    _t0 = time.time()
    image = pipe(**pipe_kwargs)[0]
    try:
        mem = f" peak_gb={torch.cuda.max_memory_allocated() / 2**30:.1f} total_gb={torch.cuda.mem_get_info()[1] / 2**30:.0f}"
    except Exception:
        mem = ""
    print(f"[timing] mode={mode_choice} {width}x{height} steps={num_inference_steps} gen_s={time.time() - _t0:.1f}{mem}", flush=True)

    return image, seed, final_prompt


# Two decorated entry points around one body: spaces.GPU caches by function, so each size needs its own function.
@spaces.GPU(duration=get_duration)
def _infer_gpu(prompt, input_images=None, mode_choice=DISTILLED, seed=42, randomize_seed=False, width=1024,
               height=1024, num_inference_steps=16, guidance_scale=4.0, prompt_upsampling=False,
               progress=gr.Progress(track_tqdm=True)):
    return _infer_gpu_body(prompt, input_images, mode_choice, seed, randomize_seed, width, height,
                           num_inference_steps, guidance_scale, prompt_upsampling, progress=progress)


@spaces.GPU(duration=get_duration_xl, size="xlarge")
def _infer_gpu_xl(prompt, input_images=None, mode_choice=DISTILLED, seed=42, randomize_seed=False, width=1024,
                  height=1024, num_inference_steps=16, guidance_scale=4.0, prompt_upsampling=False,
                  progress=gr.Progress(track_tqdm=True)):
    return _infer_gpu_body(prompt, input_images, mode_choice, seed, randomize_seed, width, height,
                           num_inference_steps, guidance_scale, prompt_upsampling, progress=progress)


def infer(
    prompt: str,
    input_images=None,
    mode_choice: str = DISTILLED,
    seed: int = 42,
    randomize_seed: bool = False,
    width: int = 1024,
    height: int = 1024,
    num_inference_steps: int = 16,
    guidance_scale: float = 4.0,
    prompt_upsampling: bool = False,
    progress=gr.Progress(track_tqdm=True),
):
    """
    Generate or edit images with FLUX 3 Image Klein, the 5.6B open weights image model from Black Forest Labs.

    Text-to-image, editing with up to 10 reference images, and layout control with bounding boxes, through one model.
    Use the distilled mode for 16-step generation without guidance, or base mode for 50-step generation with
    classifier-free guidance.

    Args:
        prompt (str): What to generate. With input images, the edit instruction; refer to them as the first image, the second image, ... Optional layout: append a JSON list of boxes, [{"id", "bbox": [top, left, bottom, right] on a 0-1000 grid, "desc"}], and cite each box as <id> in the prompt; for edits a box is {"id", "from": "ref_image_0", "src_bbox", "tgt_bbox", "desc"}.
        input_images: Optional list of input reference images. Provide image URLs.
        mode_choice (str): Model mode - "Distilled (16 steps)" for fast generation or "Base (50 steps)".
        seed (str): Random seed for reproducible generation. Use "0" with randomize_seed=True for random results.
        randomize_seed (str): Set to "true" to use a random seed, "false" to use the specified seed.
        width (str): Output image width in pixels (256-4096, multiple of 16).
        height (str): Output image height in pixels (256-4096, multiple of 16).
        num_inference_steps (str): Number of denoising steps. Use "16" for distilled mode (trained for 4-16), "50" for base mode.
        guidance_scale (str): Classifier-free guidance scale, only used by base mode ("4.0" recommended).
        prompt_upsampling (str): Ignored. The FLUX 3 Image Klein prompt upsampler always runs, except on prompts that end in a box table.

    Returns:
        tuple: the generated PIL Image, the seed used, and the prompt the model saw.
    """
    if isinstance(prompt_upsampling, str):
        prompt_upsampling = prompt_upsampling.lower() == "true"
    raw_estimate = get_duration(prompt, input_images, mode_choice, seed, randomize_seed, width, height,
                                num_inference_steps, guidance_scale)
    gpu_call = _infer_gpu
    if SPACES_CONFIG.zero_gpu and raw_estimate >= 300:
        xl_estimate = get_duration_xl(prompt, input_images, mode_choice, seed, randomize_seed, width, height,
                                      num_inference_steps, guidance_scale)
        if xl_estimate >= 300:
            raise gr.Error("This size needs more GPU time than the Space allows. Use Distilled up to 4K, or Base at 1K.")
        gpu_call = _infer_gpu_xl
        print(f"[route] xlarge, requesting {xl_estimate}s", flush=True)
    final_prompt = prompt
    # A prompt that already ends in a box table (the layout examples) goes to the model as it is.
    # The upsampler is a network call, so it runs here, outside @spaces.GPU, and spends no ZeroGPU quota.
    # PUP always runs (Maanav 2026-10-17); prompt_upsampling stays in the signature for API compatibility and is ignored.
    if not prompt_boxes(prompt):
        if progress is not None:
            progress(0.1, desc="Upsampling prompt...")
        image_list = None
        if input_images is not None and len(input_images) > 0:
            image_list = [fit_reference(item[0] if isinstance(item, (tuple, list)) else item) for item in input_images]
        final_prompt = upsample_prompt_logic(prompt, image_list)
        print(f"Original Prompt: {prompt}")
        print(f"Upsampled Prompt: {final_prompt}")
    return gpu_call(
        final_prompt, input_images, mode_choice, seed, randomize_seed, width, height,
        num_inference_steps, guidance_scale, False, progress=progress,
    )


def local_path(value):
    if isinstance(value, str):
        return value
    if path := value.get("path"):
        return path
    url = value.get("url") or ""
    return unquote(url.split("/gradio_api/file=", 1)[-1])


def flux3_klein(
    prompt: str,
    image=None,
    mode: str = DISTILLED,
    num_inference_steps: int = 0,
    seed: int = -1,
    width: int = 1024,
    height: int = 1024,
):
    mode = mode if mode in pipes else DISTILLED
    refs = [(Image.open(local_path(image)), None)] if image else None
    steps = int(num_inference_steps or 0) or DEFAULT_STEPS[mode]
    seed = int(seed if seed is not None else -1)
    if refs and not (width and height):
        width, height = update_dimensions_from_image(refs)
    result, _, _ = infer(
        prompt,
        refs,
        mode,
        max(seed, 0),
        seed < 0,
        int(width or 1024),
        int(height or 1024),
        steps,
        DEFAULT_CFG[mode],
        True,  # PUP on for the Workflow view and /image
        progress=None,
    )
    path = tempfile.NamedTemporaryFile(suffix=".png", delete=False).name
    result.save(path)
    return {"path": path, "url": f"/gradio_api/file={client_utils.encode_file_path(path)}", "is_file": True}


ASPECT_RATIOS = {
    "1:1": 1.0,
    "4:3": 4 / 3,
    "3:4": 3 / 4,
    "3:2": 3 / 2,
    "2:3": 2 / 3,
    "16:9": 16 / 9,
    "9:16": 9 / 16,
}


AUTO = "Auto"


def set_aspect(aspect, image_list, resolution):
    if aspect == AUTO and image_list:
        return update_dimensions_from_image(image_list, resolution)
    if aspect not in ASPECT_RATIOS:
        return gr.update(), gr.update()
    return dimensions_for_aspect(ASPECT_RATIOS[aspect], resolution)


def sync_references(image_list, aspect, prompt, resolution):
    """Output size follows the first reference; the references accordion opens whenever there are images."""
    if image_list:
        width, height = update_dimensions_from_image(image_list, resolution)
        return width, height, gr.Radio(choices=[AUTO, *ASPECT_RATIOS], value=AUTO), gr.Accordion(open=True)
    if aspect == AUTO or aspect not in ASPECT_RATIOS:
        width, height = dimensions_for_aspect(1.0, resolution)
        return width, height, gr.Radio(choices=list(ASPECT_RATIOS), value="1:1"), gr.update()
    return gr.update(), gr.update(), gr.Radio(choices=list(ASPECT_RATIOS), value=aspect), gr.update()


def use_as_reference(result_image, image_list):
    if result_image is None:
        raise gr.Error("Generate an image first.")
    images = [item[0] if isinstance(item, (tuple, list)) else item for item in (image_list or [])]
    images.append(result_image)
    return images, gr.Accordion(open=True)


def describe_result(seed, mode_choice, width, height):
    return f"<div class='f3-meta'><span>{mode_choice}</span><span>{int(width)} × {int(height)}</span><span>seed {int(seed)}</span></div>"


def split_prompt_table(prompt):
    """A prompt split into its text and the box table at its end (JSON rows on a 0-1000 grid); no table gives []."""
    prompt = (prompt or "").rstrip()
    for i in range(len(prompt) - 1, -1, -1):
        if prompt[i] != "[":
            continue
        try:
            rows = json.loads(prompt[i:])
        except json.JSONDecodeError:
            continue
        return prompt[:i].rstrip(), rows if isinstance(rows, list) else []
    return prompt, []


def prompt_boxes(prompt):
    """The box table at the end of a prompt, as (id, [top, left, bottom, right]) pairs."""
    boxes = []
    for row in split_prompt_table(prompt)[1]:
        box = row.get("tgt_bbox") or row.get("bbox") if isinstance(row, dict) else None
        if isinstance(box, list) and len(box) == 4 and max(box) > 1 and (box[2] - box[0]) * (box[3] - box[1]) < 900_000:
            boxes.append((str(row.get("id", "")), box))  # whole-frame rows (the background) are not drawn
    return boxes


def draw_boxes(image, boxes):
    """Red frames with the id in the corner, on a copy of the image."""
    image = image.convert("RGB")
    draw = ImageDraw.Draw(image)
    line = max(2, round(image.width / 400))
    font = ImageFont.load_default(size=max(12, image.width // 60))
    for box_id, (y1, x1, y2, x2) in boxes:
        rect = (x1 / 1000 * image.width, y1 / 1000 * image.height, x2 / 1000 * image.width, y2 / 1000 * image.height)
        draw.rectangle(rect, outline=(239, 64, 53), width=line)
        if box_id:
            left, top, right, bottom = draw.textbbox((rect[0], rect[1]), box_id, font=font)
            pad = line + 2
            draw.rectangle((left, top, right + 2 * pad, bottom + 2 * pad), fill=(239, 64, 53))
            draw.text((rect[0] + pad, rect[1] + pad), box_id, fill="white", font=font)
    return image


def toggle_boxes(show, plain, final_prompt):
    """The output with or without the boxes the model was given."""
    boxes = prompt_boxes(final_prompt)
    if plain is None or not boxes:
        return gr.update()
    return draw_boxes(plain, boxes) if show else plain


def boxes_toggle(final_prompt, image):
    """After a generation: the plain output is kept for the toggle, the checkbox says how many boxes there are."""
    n = len(prompt_boxes(final_prompt))
    return gr.Checkbox(label=f"Show the boxes ({n})" if n else "No boxes in this prompt", interactive=bool(n), value=False), image


examples = [
    ["Studio product photograph shot straight-on and flat, showing a single square 12-inch record sleeve centered against a plain neutral gray surface under even, diffused lighting. The sleeve is printed in black and white with a wide white margin surrounding one grainy monochrome photograph of a frozen lake beneath dense fog. Across the lower half of the photographic panel, the pale ice stretches toward a low horizon, its surface marked by hairline cracks and patches of dull frost; the distant shoreline disappears into layered gray mist, leaving only indistinct dark silhouettes near the upper edge of the image. At the top left within the white margin, small black Helvetica text reads \"STILL WATER\", with the smaller line \"solo piano\" directly beneath it. These are the only words on the sleeve. The photograph fills the central area below the title block, ending well inside broad blank white borders on all four sides. Fine paper fibers, minor ink grain, and a few shallow handling creases give the sleeve a tactile printed finish, while the composition remains parallel to the camera with no perspective distortion."],
    ["Two-ink risograph poster printed in fluorescent orange and blue on warm off-white paper, with coarse halftone grain, uneven ink coverage, and visible color misregistration along the edges of every shape. A swimmer dominates the upper center, captured mid-dive headfirst toward the lower left, body stretched diagonally into a long streamlined pose. The swimmer is constructed from flat geometric shapes: a fluorescent orange head and torso, blue limbs, and a blue cap with an orange face opening. One arm reaches forward while the other follows close behind, and the legs trail together above the waterline. Broad blue wave bands sweep across the middle as angular horizontal forms, interrupted by fluorescent orange circles and sharp splash shapes around the diver. Behind the swimmer, a large fluorescent orange sun sits near the top edge against a blue field, with offset orange contours creating narrow doubled outlines. At the bottom, the word \"LIDO\" spans nearly the full width in oversized uppercase block letters, alternating between fluorescent orange and blue with misregistered edges. The composition contains only the swimmer, abstract water, sun, and the single word \"LIDO\", with no additional lettering, numbers, logos, or symbols."],
    ["Full-color outdoor photograph, straight-on close view of a hand-painted shop fascia in clear morning light. The sign fills the frame as a horizontal band of weathered green wooden planks, with visible grain, chipped edges, narrow gaps between boards, and patches where the faded paint has worn through to grey-brown wood. Centered across the fascia is the large uppercase word \"BAKERY\", formed from individual gold-leaf letters with irregular brushed edges and small variations in the metallic surface. Each letter has a dark brown painted drop shadow offset down and to the right, giving the raised lettering depth against the green wood. Directly beneath it, centered in smaller scale, the text \"est. 1923\" is written in delicate gold-leaf cursive script. Low sunlight enters from the left, catching the raised gold surfaces and casting short shadows along the recessed edges while leaving the right side of the wood in cooler shade. The composition contains only the two lines of lettering on the fascia, with no additional signs, symbols, logos, or text anywhere in the scene."],
    ["Large-format still-life photograph in the register of a Dutch painting, composed vertically on a dark oak table against a deep black background. A single hard window light enters from the left, illuminating the objects with warm highlights and leaving their right sides in dense brown-black shadow. In the upper center, a torn rustic loaf rests off-center on the tabletop, its rough golden-brown crust split open to reveal an irregular pale crumb; several crumbs lie scattered below it. On the left stands a heavy pewter jug with a rounded body, narrow neck, curved handle, and dull silver surface marked by tarnish and small dents. The jug catches a bright vertical reflection along its left rim while its base disappears into shadow. Across the lower center sit exactly three lemons: two whole yellow lemons near the front and one peeled lemon beside them, its exposed flesh curling outward in a broad spiral peel. The remaining whole lemons have dimpled rinds and short shadows cast toward the right. A long old iron knife lies diagonally across the foreground, its blade pointing toward the peeled lemon and its worn wooden handle extending toward the lower right. The dark oak planks show pronounced grain, shallow scratches, and a narrow seam beneath the arrangement. The composition has restrained earth tones, concentrated chiaroscuro, crisp detail on the illuminated food and metal, and broad areas of unbroken darkness above and around the still life."],
    ["Full-color indoor large-format photograph in a vertical 4-by-5 composition, showing the interior of a brutalist concrete church from a low, wide-angle viewpoint. Massive raw concrete walls rise around a cavernous nave, their surfaces marked by formwork seams, pinholes, chipped corners, and broad geometric planes. In the upper center, a narrow rectangular opening cuts through the thick wall as one slot of hard daylight falls diagonally into the otherwise dark sanctuary. The bright beam forms a single pale shaft across the center, revealing suspended dust particles against deep grey-brown shadow. One empty wooden pew stands alone within the light, placed off-center in the lower middle of the frame and facing the unseen altar beyond it. Its long plank seat has a dull brown finish, worn edges, visible grain, and two heavy supports; the backrest is bare, with no person or object resting on it. Behind the pew, the concrete architecture expands into angular buttresses and an overhanging ceiling slab that disappears into darkness. On the left, a recessed wall remains nearly black, while the right side contains a massive cantilevered concrete volume with a rough aggregate texture. At the far end, the daylight slot ends at a small altar-like projection of unadorned concrete, but its details remain lost in shadow. The floor consists of broad poured-concrete slabs with hairline joints and scattered grit. The concentrated beam illuminates only the pew and a thin patch of floor beneath it, leaving the surrounding nave in dense shadow."],
    ["Traditional Japanese woodblock print in the Hiroshige register, rendered entirely in indigo and sumi ink on warm off-white washi paper with visible fibers and uneven carved edges. A broad wooden bridge crosses a rushing river from the lower left toward the center-right, its dark timber planks and low railings reduced to crisp, rhythmic lines. Sudden rain fills the upper half of the composition as dense, fine parallel indigo lines slanting diagonally across the entire scene. Above the bridge, layered blue-grey storm clouds sweep over distant mountains, their flattened silhouettes breaking into pale mist and deep indigo cloud bands. In the foreground, three small travelers stand close together beneath umbrellas on the bridge: one figure in a dark robe holds a round indigo umbrella, another carries a black umbrella, and a third wears a muted grey cloak beneath a smaller umbrella. Their bodies lean forward against the downpour, with hems and sleeves bending in the wind. Below them, white water surges around the bridge supports in curling sumi waves marked by sparse indigo foam crests. On the left bank, reeds and wet grasses rise beside a cluster of dark rocks; on the right, a windswept pine bends over the riverbank. The restrained composition uses broad areas of untouched paper, flat color separations, irregular hand-printed registration, and no lettering, seals, captions, or decorative inscriptions anywhere."],
    ["Studio product photograph of three hand-thrown stoneware vessels arranged on a concrete shelf <shelf_1> against a raw concrete wall <wall_1>. On the left stands a tall, narrow black tenmoku bottle vase <obj_1>; in the center sits a wide, low ash-grey bowl <obj_2>; and on the right rests a small celadon cup <obj_3>. Raking light enters from the right, catching the vessel rims and casting long shadows toward the left. [{\"id\": \"obj_1\", \"bbox\": [180, 120, 780, 260], \"desc\": \"A tall, narrow hand-thrown stoneware bottle vase with a rounded shoulder, slender neck, and flared mouth, finished in glossy black tenmoku glaze with dark brown-black reflections along its right rim and side; subtle throwing rings remain around the body.\"}, {\"id\": \"obj_2\", \"bbox\": [550, 400, 780, 660], \"desc\": \"A wide, low hand-thrown stoneware bowl with an irregular circular lip, broad body, and matte ash-grey glaze; fine horizontal throwing lines circle the exterior, with a darker unglazed foot ring.\"}, {\"id\": \"obj_3\", \"bbox\": [620, 780, 780, 880], \"desc\": \"A small hand-thrown stoneware cup with a compact rounded body, short curved handle, and pale celadon-green glaze; the glaze has muted pooling near the base and a thin exposed clay edge at the rim.\"}, {\"id\": \"wall_1\", \"bbox\": [0, 0, 780, 1000], \"desc\": \"A raw grey concrete wall with visible pores, shallow formwork seams, scattered pinholes, and uneven tonal patches, illuminated more strongly on the right.\"}, {\"id\": \"shelf_1\", \"bbox\": [780, 0, 1000, 1000], \"desc\": \"A thick horizontal concrete shelf with a rough front edge, mottled grey surface, and long directional shadows cast by the three vessels.\"}]"],
    ["Swiss-style offset-print poster on a cream paper field <poster_1>, with the large headline <obj_1> across the top and a coarse halftone photograph of a single snow-covered pine <obj_2> centered below it. Near the bottom, a small location line <obj_3> sits left of center. [{\"id\": \"obj_1\", \"bbox\": [60, 80, 200, 920], \"desc\": \"The word \\\"SILENCE\\\" in uppercase bold black grotesk type, set as one wide horizontal line with tight letter spacing and crisp Swiss poster geometry.\"}, {\"id\": \"obj_2\", \"bbox\": [260, 150, 800, 850], \"desc\": \"A single snow-covered evergreen pine rendered as a coarse black halftone photographic cutout, with dense circular dots, an irregular triangular crown, thick white snow resting across its branches, and a compact dark trunk merging into the printed silhouette; imperfect red-orange offset registration traces one edge.\"}, {\"id\": \"obj_3\", \"bbox\": [880, 80, 930, 550], \"desc\": \"The line \\\"Zürich, 3 December\\\" in small black sans-serif type, set on one baseline with regular letter spacing.\"}, {\"id\": \"poster_1\", \"bbox\": [0, 0, 1000, 1000], \"desc\": \"A flat cream paper field with visible fibrous texture, sparse ink speckling, uneven black registration edges, and restrained red-orange offset-print misregistration around selected graphic boundaries.\"}]"],
]
example_labels = ["💿 Record sleeve, STILL WATER", "🏊 Riso poster, LIDO", "🥖 Gold-leaf fascia, BAKERY", "🍋 Dutch still life", "⛪ Brutalist church", "🌧️ Hiroshige rain", "🏺 Three vessels, placed with boxes", "🪧 SILENCE poster, boxes for word, photo, date"]

examples_images = [
    ["Create a photograph preserving the first image exactly as the canvas: retain the dark black background, the weathered dark wooden tabletop, the same low frontal camera position, the aged silver metal pitcher at frame-left, the rustic torn loaf of bread behind center, the scattered bread crumbs, and the wooden-handled knife lying diagonally across the foreground. Replace only the three lemons and the peeled lemon peel with three pomegranates in the same arrangement and scale. Place one deep burgundy-red pomegranate at the front-left position, one at the central position behind it, and one at the frame-right position, each replacing its corresponding lemon. Make the third pomegranate split open in the central foreground position, exposing densely packed ruby-red seeds and a pale cream membrane, with its two shell halves resting naturally together like the former peeled lemon. Match the original directional light, contact shadows, surface reflections, and perspective. Keep the metal pitcher, bread, crumbs, knife, tabletop texture, and every other element unchanged.", ["ref_still_life.png"]],
    ["Create a vintage screen-printed poster using the first image as the unchanged canvas, preserving the cream paper background, orange outer border, blue rectangular field, orange sun, stylized orange-and-blue diving swimmer, white contour lines, blue wave bands, orange accents, speckled ink texture, and the original vertical composition. Replace only the bottom word \"LIDO\" with \"NACHT\", keeping exactly the same oversized uppercase lettering style: heavy geometric block letters, orange fill, blue inner edging, cream outlines, and the same baseline placement and overall scale. Set \"NACHT\" in one centered line across the lower cream panel, with the N, A, C, H, and T matching the original L, I, D, and O in weight, height, spacing, and hand-printed character. Preserve the orange and blue outlines around each letter, including the blue edging inside the A and H, the cream inset details, and the orange-and-blue color treatment. Keep every other element of the original poster unchanged, including the swimmer’s exact pose, the sun, waves, border, paper texture, and all surrounding negative space.", ["ref_riso_lido.png"]],
    ["Create a photograph preserving the first image exactly as the canvas: retain the straight-on close view of the weathered green wooden signboard, the horizontal plank seams, the dark aged timber trim along the top and bottom, all chipped pale paint, scratches, stains, and the same natural daylight and shadows. Replace only the large upper word \"BAKERY\" with \"BOOKS\", centered in the same position and rendered in the identical oversized uppercase slab-serif lettering, with the same dimensional construction, textured gold-leaf finish, beveled edges, and dark cast shadows falling down and to the right. Replace the smaller lower inscription \"est. 1923\" with \"est. 1961\", preserving the same centered placement, smaller scale, gold-leaf cursive lettering, period after \"est.\", and matching dimensional relief and shadows. Keep every other element unchanged, including the green paint, plank texture, spacing, framing, and surrounding wooden border.", ["ref_shop_sign.png"]],
    ["Create a photograph preserving the first image exactly as the canvas, changing only the coat material and color. Keep the same Black woman with deep brown skin, very short natural black hair, near-frontal head angle, direct gaze, neutral expression, and identical upright pose with both hands tucked into the coat pockets. Replace the long gray wool coat with an oxblood red leather coat of precisely the same cut: the same ankle-length silhouette, broad structured collar, open front, dropped shoulders, roomy sleeves, straight hem, and two large patch pockets in their original positions. Render the leather as deep oxblood red with natural tonal variation, restrained highlights, visible seams, and subtle sheen following the existing light direction. Preserve the black trousers and black leather ankle boots without alteration. Keep the same warm mustard-yellow seamless studio backdrop and floor, the same centered composition, the same camera position, and the same soft directional studio light from frame-left, including the existing highlights on her face and the same long shadow falling toward frame-right. Maintain realistic contact shadows beneath the boots and natural leather shading around the pocket openings, folds, collar, and sleeve bends.", ["ref_fashion_seamless.png"]],
    ["Create a square album-cover graphic using the first image as the exact preservation canvas. Keep the worn off-white paper sleeve, its thin gray edge, the small cast shadow beneath it, the square composition, the distressed corners, creases, scuffs, and all surface wear unchanged. Preserve the broad blank off-white header area and the monochrome photograph exactly as shown: the misty frozen lake, pale ice, scattered white patches, fine scratches, distant dark tree lines on both sides, and the flat gray sky. Change only the two lines of black text in the upper-left header. Replace the title with \"LOW TIDE\" in the same large, bold, uppercase black sans-serif type, aligned in the same position and at the same size. Replace the subtitle directly below it with \"solo cello\" in the same smaller black sans-serif type, retaining the original left alignment and spacing. Leave every other element unchanged, including the photograph, border, paper texture, background, and overall lighting.", ["ref_record_sleeve.png"]],
    ["Add a tall, narrow stained-glass window <obj_1> set into the upper concrete wall <wall_1> on the frame-right side, spanning the specified vertical area from just below the skylight to the projecting concrete ledge. Form it as a slender arched window with a dark lead grid and alternating deep red and deep blue panes, replacing the existing bright opening and casting subdued colored light onto the nearby concrete. Match the scene’s perspective, sharpness, and existing illumination. Keep the wooden bench, concrete architecture, skylight, and all other regions unchanged. [{\"id\": \"obj_1\", \"from\": \"target\", \"src_bbox\": null, \"tgt_bbox\": [100, 620, 600, 780], \"desc\": \"A tall, narrow stained-glass window with a slender arched silhouette, a dark charcoal lead framework, and irregular geometric panes in saturated deep crimson red and deep cobalt blue, set flush into the concrete opening.\"}, {\"id\": \"wall_1\", \"from\": \"ref_image_0\", \"src_bbox\": [0, 665, 704, 1000], \"tgt_bbox\": [0, 665, 704, 1000], \"desc\": \"A massive raw gray concrete wall and projecting architectural volume with visible panel seams, pores, small holes, and a broad cantilevered lower section.\"}]", ["ref_church.png"]],
    ["Add a round yellow sticker <obj_1> in the upper-right corner of the album cover, overlapping the white border, with the word \"NEW\" <En_Text_1> centered on it in bold black uppercase sans-serif lettering. Match the cover’s aged printed texture and lighting, and keep every other region identical to the source, pixel for pixel. [{\"id\": \"obj_1\", \"from\": \"target\", \"src_bbox\": null, \"tgt_bbox\": [40, 800, 160, 940], \"desc\": \"A circular bright yellow adhesive sticker with a subtly matte printed surface, a thin dark edge, and a slight raised rim, sized as a compact corner badge.\"}, {\"id\": \"En_Text_1\", \"from\": \"target\", \"src_bbox\": null, \"tgt_bbox\": [78, 835, 122, 905], \"desc\": \"The text \\\"NEW\\\" in bold black uppercase sans-serif lettering, centered on one line.\"}]", ["ref_record_sleeve.png"]],
    ["Create a photograph preserving the second image exactly as the canvas: retain the dark tabletop still life, the straight-on camera position, the black background, the worn dark wooden plank table, and the same directional light from frame-left. Keep the weathered silver pitcher at frame-left, the broken rustic loaf in the center-right, all three yellow lemons, the curled lemon peel, and the wooden-handled knife in their original positions. Add the orange hardcover book from the first image upright on the table immediately to the left of the loaf, standing beside it without covering the pitcher or any existing object. Preserve the book’s exact orange cover, black spine, proportions, centered black title \"THE WEATHER MACHINE\", thin horizontal rule, and vintage circular weather gauge illustration. Match its scale to the loaf and place its lower edge naturally on the wood, with a grounded contact shadow consistent with the existing light. Keep the book’s front cover facing the camera and fully visible, with the loaf remaining behind and slightly to its right. Integrate the book into the scene with the same subdued highlights, warm reflected wood tones, and deep shadows as the original still life.", ["ref_book_jacket.png", "ref_still_life.png"]],
    ["In <ref_image_0>, move the miniature grey amigurumi knight figure <knight_1> upwards and to the left along the yarn cliff <cliff_1>. Keep the rest of the image completely unchanged, preserving the blurred yarn backdrop <backdrop_1>, the large knitted dragon <dragon_1>, and the fiery orange thread <fire_1>. [{\"id\": \"knight_1\", \"from\": \"ref_image_0\", \"src_bbox\": [500, 150, 850, 350], \"tgt_bbox\": [194, 55, 544, 255], \"desc\": \"A miniature amigurumi knight crocheted from thick grey woolen yarn.\"}, {\"id\": \"backdrop_1\", \"from\": \"ref_image_0\", \"src_bbox\": [0, 0, 1000, 1000], \"tgt_bbox\": [0, 0, 1000, 1000], \"desc\": \"A soft, out-of-focus backdrop of cream and indigo knitted yarn.\"}, {\"id\": \"cliff_1\", \"from\": \"ref_image_0\", \"src_bbox\": [300, 0, 1000, 450], \"tgt_bbox\": [300, 0, 1000, 450], \"desc\": \"A steep cliff of stacked yarn skeins in mustard, terracotta, and indigo.\"}, {\"id\": \"needle_1\", \"from\": \"ref_image_0\", \"src_bbox\": [420, 250, 550, 450], \"tgt_bbox\": [420, 250, 550, 450], \"desc\": \"An oversized polished steel tapestry needle.\"}, {\"id\": \"dragon_1\", \"from\": \"ref_image_0\", \"src_bbox\": [100, 600, 950, 1000], \"tgt_bbox\": [100, 600, 950, 1000], \"desc\": \"A large, fluffy knitted dragon in terracotta and mustard yarn.\"}, {\"id\": \"fire_1\", \"from\": \"ref_image_0\", \"src_bbox\": [350, 400, 650, 650], \"tgt_bbox\": [350, 400, 650, 650], \"desc\": \"Curled puffs of fiery orange angora thread suspended in mid-air.\"}]", ["example_knight.jpg"]],
]
example_images_labels = ["🍋→ Lemons to pomegranates", "🏊 LIDO to NACHT", "🥖 BAKERY to BOOKS", "🧥 Coat to oxblood leather", "💿 STILL WATER to LOW TIDE", "⛪ Stained glass in a box", "💿 NEW sticker in a box", "📙 Book from the first image onto the table of the second", "🧶 Move the knight with boxes"]


# Pre-made outputs for the examples: the images these captions produced (fixed seeds), written as the examples' cache
# so a click shows them without a generation. Any example without a row is generated on first click as before.
EXAMPLE_OUTPUTS = [('outputs/record_sleeve.png', 1), ('outputs/riso_lido.png', 1), ('outputs/shop_sign.png', 2), ('outputs/still_life.png', 1), ('outputs/church.png', 1), ('outputs/hiroshige.png', 1), ('outputs/shelf_layout.png', 1), ('outputs/poster_layout.png', 1)]
EXAMPLE_IMAGE_OUTPUTS = [('outputs/still_life__pomegranate.png', 1), ('outputs/riso_lido__text.png', 1), ('outputs/bakery__text.png', 1), ('outputs/fashion_seamless__red.png', 1), ('outputs/record_sleeve__title.png', 1), ('outputs/church_window.png', 1), ('outputs/sleeve_sticker.png', 1), ('outputs/book_on_table.png', 1)]


def seed_example_cache(block, rows):
    if block.cached_file.exists() or not rows:
        return
    block.cache_logger.setup(block.outputs, block.cached_folder)
    os.makedirs(block.cached_folder, exist_ok=True)
    with open(block.cached_indices_file, "w") as f:
        for i, (png, seed) in enumerate(rows):
            caption = block.examples[i][0]
            values = (Image.open(os.path.join(HERE, png)), seed, caption)
            payload = [c.postprocess(v) for c, v in zip(block.outputs, values)]
            block.cache_logger.flag([p.model_dump() if hasattr(p, "model_dump") else p for p in payload])
            f.write(f"{i}\n")


# ---- Bounding boxes tab ----
# The editor's value is JSON: {"aspect": w/h, "image": data URI or null, "boxes": [{"id", "kind", "src", "tgt", "desc"}]},
# and from Python also "result", the last output shown in the canvas (the browser keeps it and does not send it back),
# boxes as [top, left, bottom, right] on the 0-1000 grid. Without an image every box is a layout row {"id", "bbox", "desc"};
# over an image a box is an edit row: keep (src = tgt), move (src -> tgt), new (no src), remove (no tgt).

BBOX_EDITOR_JS = Path(HERE, "bbox_editor.js").read_text()
BBOX_KINDS = ("keep", "move", "new", "remove")

SYSTEM_PROMPT_LAYOUT = """You plan image layouts for FLUX 3 by Black Forest Labs. Turn the user's idea into a caption and an element table for a {aspect} image (width:height).

- caption: one paragraph describing the whole image: subject, composition, lighting, style. Where an element appears, cite its id in angle brackets, e.g. "a red fox <fox_1> in fresh snow <snow_1>".
- elements: one row per cited id, ids lowercase with a number. "bbox" is [top, left, bottom, right] in integers from 0 to 1000, measured from the top-left corner, sized for the element's real extent in the frame. "desc" says what the element looks like: shape, material, color, texture, light. Include one background row covering [0, 0, 1000, 1000]. Put any text that appears in the image in quotation marks, in both the caption and the desc.
- 3 to 8 elements, unless the idea needs more.

Output only JSON: {{"caption": "...", "elements": [{{"id": "...", "bbox": [0, 0, 0, 0], "desc": "..."}}]}}"""

SYSTEM_PROMPT_DETECT = """You list the elements of an image so it can be edited box by box. Return 4 to 10 elements that together cover the image: the main subjects, notable objects, any text, and the background or setting.

For each element give:
- "id": a short lowercase name with a number, e.g. "dog_1", "sign_1", "background_1"
- "bbox_2d": its bounding box [x1, y1, x2, y2] in coordinates from 0 to 1000 relative to the image
- "desc": one sentence on how it looks: shape, material, color, texture, light; text in quotation marks

Output only a JSON array: [{"id": "...", "bbox_2d": [0, 0, 0, 0], "desc": "..."}]"""


def bbox_state(boxes=(), aspect=1.0, image=None):
    return json.dumps({"aspect": aspect, "image": image, "boxes": list(boxes)})


def read_bbox_state(value):
    try:
        state = json.loads(value or "{}")
    except json.JSONDecodeError:
        state = {}
    state.setdefault("aspect", 1.0)
    state.setdefault("image", None)
    state["boxes"] = [b for b in state.get("boxes") or [] if isinstance(b, dict) and b.get("id")]
    return state


def grid_box(box):
    """A [top, left, bottom, right] box clamped to the 0-1000 grid, or None."""
    if not isinstance(box, (list, tuple)) or len(box) != 4:
        return None
    try:
        y1, x1, y2, x2 = (max(0, min(1000, round(float(v)))) for v in box)
    except (TypeError, ValueError):
        return None
    return [min(y1, y2), min(x1, x2), max(y1, y2), max(x1, x2)] if y1 != y2 and x1 != x2 else None


def editor_box(row):
    """A prompt-table row (layout or edit) as an editor box."""
    if "bbox" in row:
        return {"id": row["id"], "kind": "new", "src": None, "tgt": grid_box(row["bbox"]), "desc": row.get("desc", "")}
    src, tgt = grid_box(row.get("src_bbox")), grid_box(row.get("tgt_bbox"))
    if row.get("from") in (None, "target") or src is None:
        kind = "new"
    elif tgt is None:
        kind = "remove"
    else:
        kind = "keep" if src == tgt else "move"
    return {"id": row["id"], "kind": kind, "src": None if kind == "new" else src, "tgt": tgt, "desc": row.get("desc", "")}


def box_rows(state):
    """The editor's boxes as the JSON rows the model reads."""
    rows = []
    for b in state["boxes"]:
        kind = b.get("kind") if b.get("kind") in BBOX_KINDS else "new"
        src, tgt, desc = grid_box(b.get("src")), grid_box(b.get("tgt")), (b.get("desc") or "").strip()
        if not state["image"]:
            if box := tgt or src:
                rows.append({"id": b["id"], "bbox": box, "desc": desc})
        elif kind == "new" and tgt:
            rows.append({"id": b["id"], "from": None, "src_bbox": None, "tgt_bbox": tgt, "desc": desc})
        elif kind == "remove" and src:
            rows.append({"id": b["id"], "from": "ref_image_0", "src_bbox": src, "tgt_bbox": None, "desc": desc})
        elif src and (tgt or kind == "keep"):
            rows.append({"id": b["id"], "from": "ref_image_0", "src_bbox": src, "tgt_bbox": tgt if kind == "move" else src, "desc": desc})
    return rows


def short_desc(desc, words=6):
    """The head of a description, for naming its box in an instruction: "A large, fluffy knitted dragon in ..." -> "large, fluffy knitted dragon"."""
    text = re.split(r"[.;:]| with | from | made | in | on ", (desc or "").strip(), maxsplit=1)[0]
    text = re.sub(r"^(a|an|the)\s+", "", text.strip(), flags=re.IGNORECASE)
    if text[:1].isupper() and not text[1:2].isupper():
        text = text[0].lower() + text[1:]
    return " ".join(text.split()[:words])


def edit_instruction(rows):
    """An instruction written from the edit rows, for when the prompt box is left empty."""
    def named(row):
        return f"the {short_desc(row['desc'])} <{row['id']}>" if row["desc"] else f"<{row['id']}>"

    changes = []
    for row in rows:
        if row["from"] is None:
            changes.append(f"place {short_desc(row['desc']) or 'a new element'} in <{row['id']}>")
        elif row["tgt_bbox"] is None:
            changes.append(f"remove {named(row)}")
        elif row["src_bbox"] != row["tgt_bbox"]:
            changes.append(f"move {named(row)} to its new position")
    kept = [f"<{row['id']}>" for row in rows if row["from"] and row["src_bbox"] == row["tgt_bbox"]]
    text = f"In <ref_image_0>, {', '.join(changes) if changes else 'keep the scene as it is'}."
    if kept:
        text += f" Keep {', '.join(kept)} exactly unchanged."
    return text


def bbox_prompt(caption, value):
    """The prompt the model gets: the text, a space, the JSON table. Returns (prompt, note about the table)."""
    state = read_bbox_state(value)
    rows = box_rows(state)
    caption = (caption or "").strip()
    if not rows:
        return caption, "Draw at least one box."
    if not caption and state["image"]:
        caption = edit_instruction(rows)
    notes = [f"{len(rows)} box{'es' if len(rows) != 1 else ''}"]
    if missing := [r["id"] for r in rows if f"<{r['id']}>" not in caption]:
        notes.append("not cited in the prompt: " + ", ".join(f"<{i}>" for i in missing))
    if empty := [r["id"] for r in rows if not r["desc"]]:
        notes.append("no description: " + ", ".join(empty))
    return f"{caption} {json.dumps(rows, ensure_ascii=False)}".strip(), " · ".join(notes)


def preview_bbox_prompt(caption, value):
    return f"<p class='f3-hint'>{html.escape(bbox_prompt(caption, value)[1])}</p>"


def import_prompt_table(caption, value):
    """A full prompt pasted into the prompt box: its box table moves into the editor, the text stays."""
    text, rows = split_prompt_table(caption)
    boxes = [editor_box(r) for r in rows if isinstance(r, dict) and r.get("id")]
    boxes = [b for b in boxes if b["tgt"] or b["src"]]
    if not boxes:
        return gr.update(), gr.update()
    state = read_bbox_state(value)
    if not state["image"]:
        for b in boxes:
            b.update(kind="new", tgt=b["tgt"] or b["src"], src=None)
    state["boxes"] = boxes
    gr.Info(f"Moved {len(boxes)} box{'es' if len(boxes) != 1 else ''} from the prompt into the editor.")
    return text, json.dumps(state)


def editor_image(img, size=1024):
    """An image as a data URI small enough to send to the browser with every edit."""
    img = img.convert("RGB")
    img.thumbnail((size, size), Image.LANCZOS)
    buffered = io.BytesIO()
    img.save(buffered, format="JPEG", quality=85)
    return "data:image/jpeg;base64," + base64.b64encode(buffered.getvalue()).decode("utf-8")


def set_bbox_reference(image, value, aspect):
    """Upload or clear the reference: over an image boxes become edit boxes; without one, layout boxes again."""
    state = read_bbox_state(value)
    if image is None:
        for b in state["boxes"]:
            b.update(kind="new", tgt=b.get("tgt") or b.get("src"), src=None)
        state.update(image=None, aspect=ASPECT_RATIOS.get(aspect, 1.0), result=None)
        return json.dumps(state), gr.update(visible=True), gr.update(visible=False), gr.update(visible=True)
    state.update(image=editor_image(image), aspect=image.width / image.height, result=None)
    return json.dumps(state), gr.update(visible=False), gr.update(visible=True), gr.update(visible=False)


def set_bbox_aspect(aspect, value):
    state = read_bbox_state(value)
    if state["image"] or aspect not in ASPECT_RATIOS:
        return gr.update()
    state.update(aspect=ASPECT_RATIOS[aspect], result=None)
    return json.dumps(state)


def vlm_json(messages):
    completion = hf_client.chat.completions.create(model=VLM_MODEL, messages=messages, max_tokens=2048)
    text = completion.choices[0].message.content.strip()
    start, end = min((i for i in (text.find("{"), text.find("[")) if i >= 0), default=-1), max(text.rfind("}"), text.rfind("]"))
    if start < 0 or end < start:
        raise ValueError(f"no JSON in the reply: {text[:200]}")
    return json.loads(text[start : end + 1])


def draft_layout(idea, value, aspect):
    """Caption and boxes for a short idea, planned by the hosted VLM."""
    if not (idea or "").strip():
        raise gr.Error("Write a short idea in the prompt box first.")
    state = read_bbox_state(value)
    try:
        plan = vlm_json([
            {"role": "system", "content": SYSTEM_PROMPT_LAYOUT.format(aspect=aspect if aspect in ASPECT_RATIOS else "1:1")},
            {"role": "user", "content": idea.strip()},
        ])
        boxes = [editor_box(r) for r in plan["elements"] if isinstance(r, dict) and r.get("id") and grid_box(r.get("bbox"))]
    except Exception as e:
        raise gr.Error(f"The layout draft failed: {e}")
    state["boxes"] = boxes
    return plan["caption"].strip(), json.dumps(state)


def detect_elements(image, value):
    """Keep boxes for the main elements of the reference, found by the hosted VLM: the source table for a box edit."""
    if image is None:
        raise gr.Error("Add a reference image first.")
    state = read_bbox_state(value)
    try:
        found = vlm_json([
            {"role": "system", "content": SYSTEM_PROMPT_DETECT},
            {"role": "user", "content": [{"type": "image_url", "image_url": {"url": image_to_data_uri(fit_reference(image))}}, {"type": "text", "text": "List the elements."}]},
        ])
    except Exception as e:
        raise gr.Error(f"Element detection failed: {e}")
    boxes, ids = [], set()
    for row in found if isinstance(found, list) else []:
        x1y1x2y2 = row.get("bbox_2d") if isinstance(row, dict) else None
        box = grid_box([x1y1x2y2[1], x1y1x2y2[0], x1y1x2y2[3], x1y1x2y2[2]]) if isinstance(x1y1x2y2, list) and len(x1y1x2y2) == 4 else None
        box_id = "".join(c if c.isalnum() else "_" for c in str(row.get("id") or "")) if box else ""
        if box_id and box_id not in ids:
            ids.add(box_id)
            boxes.append({"id": box_id, "kind": "keep", "src": box, "tgt": list(box), "desc": str(row.get("desc") or "")})
    if not boxes:
        raise gr.Error("The model found no elements; draw the boxes yourself.")
    state["boxes"] = boxes
    return json.dumps(state)


def bbox_generate(caption, value, image, mode_choice, resolution, seed, randomize_seed, progress=gr.Progress(track_tqdm=True)):
    state = read_bbox_state(value)
    prompt, _ = bbox_prompt(caption, value)
    if not box_rows(state):
        raise gr.Error("Draw at least one box.")
    if not (caption or "").strip() and not state["image"]:
        raise gr.Error("Describe the image in the prompt box and cite each box as <id>, or draft the layout from a short idea.")
    if image is not None and state["image"]:
        refs, (width, height) = [image], update_dimensions_from_image([image], resolution)
    else:
        refs, (width, height) = None, dimensions_for_aspect(state["aspect"], resolution)
    image, seed, final_prompt = infer(
        prompt, refs, mode_choice, seed, randomize_seed, width, height, DEFAULT_STEPS[mode_choice], DEFAULT_CFG[mode_choice], False, progress=progress
    )
    state["result"] = editor_image(image, 1536)
    return (json.dumps(state), seed, final_prompt, describe_result(seed, mode_choice, width, height), image, *result_buttons(image))


def result_buttons(image):
    """Download (the full PNG) and edit buttons for an output, hidden without one."""
    if image is None:
        return gr.update(visible=False), gr.update(visible=False)
    path = tempfile.NamedTemporaryFile(suffix=".png", delete=False).name
    image.save(path)
    return gr.update(value=path, visible=True), gr.update(visible=True)


def edit_bbox_result(image, final_prompt):
    """The last output as the reference, its boxes as keep boxes: the next step of a box-by-box edit."""
    if image is None:
        raise gr.Error("Generate an image first.")
    boxes = []
    for row in split_prompt_table(final_prompt)[1]:
        box = editor_box(row) if isinstance(row, dict) and row.get("id") else None
        if box and box["tgt"]:
            boxes.append({**box, "kind": "keep", "src": list(box["tgt"])})
    state = json.dumps({**read_bbox_state(bbox_state(boxes, image.width / image.height, editor_image(image))), "result": None})
    return image, state, "", gr.update(visible=False), gr.update(visible=True), gr.update(visible=False)


RUNNER_PROMPT = 'Minimalist graphic illustration featuring a black silhouette of a person <silhouette_1> centered against a solid, vibrant chartreuse background <background_1>. The figure is captured in a dynamic, mid-stride running pose, facing toward the left side of the frame. [{"id": "background_1", "bbox": [0, 0, 1000, 1000], "desc": "A flat field of neon yellow-green with a subtle paper texture and fine, organic grain."}, {"id": "silhouette_1", "bbox": [150, 150, 850, 850], "desc": "A black silhouette of a person in motion, made of dense stippled ink. The leading edges are solid; the trailing arm and leg dissolve into coarse square pixels and scattered dots."}]'

# (label, prompt, reference image, pre-made output) for the tab's examples.
BBOX_EXAMPLES = [
    ("🏃 Runner, two boxes", RUNNER_PROMPT, None, None),
    ("🏺 Three vessels", examples[6][0], None, "outputs/shelf_layout.png"),
    ("🪧 SILENCE poster", examples[7][0], None, "outputs/poster_layout.png"),
    ("⛪ Stained glass in a box", examples_images[5][0], "ref_church.png", "outputs/church_window.png"),
    ("💿 NEW sticker", examples_images[6][0], "ref_record_sleeve.png", "outputs/sleeve_sticker.png"),
    ("🧶 Move the knight", examples_images[8][0], "example_knight.jpg", None),
]


def load_bbox_example(index):
    _, prompt, ref, output = BBOX_EXAMPLES[index]
    caption, rows = split_prompt_table(prompt)
    boxes = [editor_box(r) for r in rows if isinstance(r, dict) and r.get("id")]
    image = Image.open(os.path.join(HERE, ref)).convert("RGB") if ref else None
    result = Image.open(os.path.join(HERE, output)).convert("RGB") if output else None
    if image is not None:
        state = read_bbox_state(bbox_state(boxes, image.width / image.height, editor_image(image)))
    else:
        state = read_bbox_state(bbox_state(boxes, result.width / result.height if result else 1.0))
    state["result"] = editor_image(result, 1536) if result else None
    aspect = min(ASPECT_RATIOS, key=lambda k: abs(ASPECT_RATIOS[k] - state["aspect"]))
    return (
        caption,
        json.dumps(state),
        image,
        gr.update(value=aspect, visible=image is None),
        gr.update(visible=image is not None),
        gr.update(visible=image is None),
        result,
        prompt if result else "",
        "<div class='f3-meta'><span>Pre-made output</span></div>" if result else "<div class='f3-meta'></div>",
        *result_buttons(result),
    )


BBOX_HTML = """
<div class="bx">
  <div class="bx-bar"><button class="bx-btn bx-result" type="button" hidden>Hide the result</button><button class="bx-btn bx-boxes" type="button">Hide boxes</button><button class="bx-btn bx-clear" type="button">Clear boxes</button><span class="bx-xy"></span></div>
  <div class="bx-stage"><img class="bx-bg" alt="" /><canvas class="bx-cv" tabindex="0"></canvas><textarea class="bx-note" hidden spellcheck="false" aria-label="description of the box"></textarea></div>
  <p class="bx-hint"></p>
  <div class="bx-rows"></div>
</div>
"""

BBOX_CSS = """
.bx { display: flex; flex-direction: column; gap: 10px; }
.bx-bar { display: flex; align-items: center; gap: 6px; flex-wrap: wrap; }
.bx-hint { margin: 0; font-size: 0.8rem; line-height: 1.4; color: var(--body-text-color-subdued); }
.bx-xy { margin-left: auto; font-family: var(--font-mono); font-size: 0.75rem; white-space: nowrap; color: var(--body-text-color-subdued); }
.bx-btn[hidden] { display: none; }
.bx-btn { display: inline-flex; align-items: center; height: 28px; margin: 0; padding: 0 10px; font: inherit; font-size: 0.8rem; font-weight: 500; line-height: 1; border-radius: 6px; border: 1px solid var(--border-color-primary); background: var(--block-background-fill); color: var(--body-text-color); cursor: pointer; white-space: nowrap; }
.bx-btn:hover { border-color: var(--body-text-color-subdued); }
.bx-stage { position: relative; margin: 0 auto; max-width: 100%; background: #faf8ef; border: 1px solid var(--border-color-primary); border-radius: 8px; overflow: hidden; touch-action: none; user-select: none; }
.bx-bg { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: fill; pointer-events: none; }
.bx-cv { position: absolute; inset: 0; width: 100%; height: 100%; cursor: crosshair; outline: none; }
.bx-note { position: absolute; z-index: 2; box-sizing: border-box; resize: none; font: inherit; font-size: 0.86rem; line-height: 1.35; padding: 6px 8px; border: 2px solid; border-radius: 6px; background: rgba(255, 255, 255, 0.95); color: #1b1f1c; box-shadow: 0 6px 20px rgba(0, 0, 0, 0.18); outline: none; }
.bx-note[hidden] { display: none; }
.bx-rows { display: flex; flex-direction: column; gap: 8px; }
.bx-empty { font-size: 0.85rem; color: var(--body-text-color-subdued); }
.bx-row { border: 1px solid var(--border-color-primary); border-left: 4px solid var(--c); border-radius: 8px; padding: 8px; background: var(--block-background-fill); display: flex; flex-direction: column; gap: 6px; }
.bx-row.is-sel { box-shadow: 0 0 0 2px var(--c); }
.bx-row-head { display: flex; align-items: center; gap: 8px; }
.bx-swatch { width: 10px; height: 10px; border-radius: 3px; background: var(--c); flex: none; }
.bx-id { font-family: var(--font-mono); font-size: 0.85rem; width: 130px; padding: 3px 6px; border: 1px solid var(--border-color-primary); border-radius: 5px; background: var(--input-background-fill); color: var(--body-text-color); }
.bx-kind { font-size: 0.82rem; padding: 3px 6px; border: 1px solid var(--border-color-primary); border-radius: 5px; background: var(--input-background-fill); color: var(--body-text-color); }
.bx-rect { font-family: var(--font-mono); font-size: 0.78rem; width: 172px; padding: 3px 6px; border: 1px solid var(--border-color-primary); border-radius: 5px; background: var(--input-background-fill); color: var(--body-text-color); }
.bx-from { flex: 1; font-size: 0.75rem; color: var(--body-text-color-subdued); overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
.bx-del { border: none; background: none; cursor: pointer; color: var(--body-text-color-subdued); font-size: 0.9rem; padding: 2px 6px; }
.bx-del:hover { color: #ef4035; }
.bx-desc { width: 100%; resize: vertical; font: inherit; font-size: 0.88rem; line-height: 1.4; padding: 6px 8px; border: 1px solid var(--border-color-primary); border-radius: 5px; background: var(--input-background-fill); color: var(--body-text-color); box-sizing: border-box; }
"""


def build_bbox_tab():
    with gr.Row(elem_classes="f3-bbox-examples"):
        example_buttons = [gr.Button(label, size="sm", variant="secondary") for label, *_ in BBOX_EXAMPLES]
    with gr.Row(equal_height=False):
        with gr.Column(scale=6):
            editor = gr.HTML(
                value=bbox_state([editor_box(r) for r in split_prompt_table(RUNNER_PROMPT)[1]]),
                html_template=BBOX_HTML,
                css_template=BBOX_CSS,
                js_on_load=BBOX_EDITOR_JS,
                elem_id="f3-bbox-editor",
            )
        with gr.Column(scale=5):
            with gr.Group():
                caption = gr.Textbox(
                    label="Prompt",
                    elem_id="f3-bb-prompt",
                    lines=4,
                    max_lines=12,
                    value=split_prompt_table(RUNNER_PROMPT)[0],
                    placeholder="Describe the image and cite each box as <id>. With a reference image, say what changes; left empty, the instruction is written from the boxes. A pasted prompt that ends in a box table is split into text and boxes.",
                )
            with gr.Row():
                draft_button = gr.Button("Draft boxes from the prompt", size="sm", variant="secondary")
                detect_button = gr.Button("Detect elements in the image", size="sm", variant="secondary", visible=False)
            with gr.Accordion("Reference image · optional, for box edits", open=False):
                reference = gr.Image(label="Reference", show_label=False, type="pil", height=220, sources=["upload", "clipboard"])
            mode_choice = gr.Radio(label="Model", elem_id="f3-bb-mode", choices=[DISTILLED, BASE], value=DISTILLED)
            aspect = gr.Radio(label="Aspect ratio", elem_id="f3-bb-aspect", choices=list(ASPECT_RATIOS), value="1:1")
            resolution = gr.Radio(label="Resolution", elem_id="f3-bb-resolution", choices=MODE_RESOLUTIONS[DISTILLED], value=DEFAULT_RESOLUTION[DISTILLED])
            with gr.Accordion("Seed", open=False):
                with gr.Row():
                    seed = gr.Slider(label="Seed", minimum=0, maximum=MAX_SEED, step=1, value=0, scale=3)
                    randomize_seed = gr.Checkbox(label="Randomize", value=True, scale=1, min_width=100)
            run_button = gr.Button("Generate with boxes", variant="primary", size="lg", elem_id="f3-bb-run")
            note = gr.HTML(preview_bbox_prompt(caption.value, editor.value))
            meta = gr.HTML("<div class='f3-meta'></div>")
            with gr.Row():
                download_button = gr.DownloadButton("Download PNG", size="sm", variant="secondary", visible=False)
                edit_button = gr.Button("Edit this result box by box", size="sm", variant="secondary", visible=False)
            result = gr.State(None)
            final_prompt = gr.State("")

    for i, button in enumerate(example_buttons):
        button.click(
            fn=lambda i=i: load_bbox_example(i),
            outputs=[caption, editor, reference, aspect, detect_button, draft_button, result, final_prompt, meta, download_button, edit_button],
            api_visibility="private",
        )
    gr.on(
        triggers=[caption.change, editor.change],
        fn=preview_bbox_prompt,
        inputs=[caption, editor],
        outputs=note,
        api_visibility="private",
    )
    gr.on(triggers=[caption.blur, caption.submit], fn=import_prompt_table, inputs=[caption, editor], outputs=[caption, editor], api_visibility="private")
    reference.upload(fn=set_bbox_reference, inputs=[reference, editor, aspect], outputs=[editor, aspect, detect_button, draft_button], api_visibility="private")
    reference.clear(fn=set_bbox_reference, inputs=[reference, editor, aspect], outputs=[editor, aspect, detect_button, draft_button], api_visibility="private")
    aspect.input(fn=set_bbox_aspect, inputs=[aspect, editor], outputs=editor, api_visibility="private")
    draft_button.click(fn=draft_layout, inputs=[caption, editor, aspect], outputs=[caption, editor], api_visibility="private")
    detect_button.click(fn=detect_elements, inputs=[reference, editor], outputs=editor, api_visibility="private")
    edit_button.click(
        fn=edit_bbox_result,
        inputs=[result, final_prompt],
        outputs=[reference, editor, caption, aspect, detect_button, draft_button],
        api_visibility="private",
    )
    mode_choice.change(
        fn=lambda m: gr.Radio(choices=MODE_RESOLUTIONS[m], value=DEFAULT_RESOLUTION[m]),
        inputs=[mode_choice], outputs=[resolution], api_visibility="private",
    )
    gr.on(
        triggers=[run_button.click],
        fn=bbox_generate,
        inputs=[caption, editor, reference, mode_choice, resolution, seed, randomize_seed],
        outputs=[editor, seed, final_prompt, meta, result, download_button, edit_button],
        api_visibility="private",
    )


css = """
#workflow-app .workflow-app-body, #workflow-app-header { display: none !important; }
#workflow-app { padding-top: 0 !important; margin-top: 0 !important; gap: 0 !important; }
#f3-app { max-width: 1280px; margin: 0 auto; padding: 8px 4px 72px; }
.f3-header { display: flex; align-items: flex-end; justify-content: space-between; gap: 16px; flex-wrap: wrap; margin: 0 0 12px; }
.f3-header h1 { font-size: 2rem; font-weight: 600; letter-spacing: -0.02em; margin: 0 0 6px; }
.f3-header p { margin: 0; max-width: 720px; color: var(--body-text-color-subdued); font-size: 0.98rem; line-height: 1.45; }
.f3-links { display: flex; gap: 8px; flex-wrap: wrap; }
.f3-links a, .f3-links a:visited { text-decoration: none !important; font-size: 0.85rem; padding: 6px 12px; border-radius: 6px; border: 1px solid var(--border-color-primary); color: var(--body-text-color); background: var(--block-background-fill); }
.f3-links a:hover { border-color: var(--body-text-color); }
#f3-prompt textarea, #f3-bb-prompt textarea { font-size: 1rem; line-height: 1.5; }
#f3-mode .wrap, #f3-bb-mode .wrap { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; }
#f3-mode .wrap label, #f3-bb-mode .wrap label { justify-content: center; }
#f3-aspect .wrap, #f3-bb-aspect .wrap { display: flex; flex-wrap: wrap; gap: 6px; }
#f3-aspect .wrap label, #f3-bb-aspect .wrap label { flex: 1 1 0; min-width: 52px; justify-content: center; padding: 6px 8px; }
#f3-resolution .wrap, #f3-bb-resolution .wrap { display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px; }
#f3-resolution .wrap label, #f3-bb-resolution .wrap label { justify-content: center; }
#f3-run, #f3-bb-run { font-size: 1.05rem; min-height: 48px; }
#f3-result { min-height: 520px; }
#f3-result img { object-fit: contain; }
.f3-meta { display: flex; gap: 8px; flex-wrap: wrap; justify-content: flex-start; min-height: 28px; }
.f3-meta span { font-size: 0.8rem; padding: 3px 10px; border-radius: 6px; background: var(--block-background-fill); border: 1px solid var(--border-color-primary); color: var(--body-text-color-subdued); }
.f3-hint { font-size: 0.85rem; color: var(--body-text-color-subdued); margin: 0 0 6px; }
#f3-refs .grid-container { grid-template-columns: repeat(auto-fill, minmax(96px, 128px)) !important; grid-auto-rows: 116px !important; justify-content: start; }
#f3-refs .thumbnail-item { width: 100%; height: 116px; aspect-ratio: auto; }
#f3-refs .thumbnail-item img { object-fit: contain; width: 100%; height: 100%; }
.gallery-container img { object-fit: contain; }
.f3-bbox-examples { flex-wrap: wrap; gap: 8px; margin: 4px 0 8px; }
.f3-bbox-examples button { flex: 0 1 auto !important; min-width: 0 !important; }
"""

# Cream page, dark primary button, neutral everything else.
theme = gr.themes.Soft(
    primary_hue="stone",
    neutral_hue="stone",
    font=[gr.themes.GoogleFont("Instrument Sans"), "Arial", "sans-serif"],
    font_mono=[gr.themes.GoogleFont("IBM Plex Mono"), "Consolas", "monospace"],
).set(
    body_background_fill="#f3f1e6",
    block_background_fill="#ffffff",
    button_primary_background_fill="#07130e",
    button_primary_background_fill_hover="#2c3d33",
    button_primary_text_color="#f3f1e6",
    button_primary_border_color="#07130e",
    checkbox_label_background_fill_selected="#07130e",
    checkbox_label_text_color_selected="#f3f1e6",
    slider_color="#07130e",
)

HEADER = """
<div class="f3-header">
  <div>
    <h1>FLUX 3 Image Klein</h1>
    <p>The 5.6B open weights image model from Black Forest Labs: text-to-image, editing with up to 10 reference images, and layout control with bounding boxes, through one model. Distilled runs 16 steps without guidance; Base runs 50 steps with classifier-free guidance.</p>
  </div>
  <div class="f3-links">
    <a href="https://huggingface.co/{distilled_repo}" target="_blank">Distilled weights ↗</a>
    <a href="https://huggingface.co/{base_repo}" target="_blank">Base weights ↗</a>
    <a href="https://github.com/black-forest-labs/flux-3-image-klein" target="_blank">Code ↗</a>
  </div>
</div>
"""


def build_app():
    with gr.Column(elem_id="f3-app"):
        gr.HTML(HEADER.format(base_repo=BASE_REPO, distilled_repo=DISTILLED_REPO))
        with gr.Tabs(selected="bbox") as tabs:
            with gr.Tab("Generate & edit", id="generate"):
                with gr.Row(equal_height=False):
                    with gr.Column(scale=5):
                        with gr.Group():
                            prompt = gr.Textbox(
                                label="Prompt",
                                elem_id="f3-prompt",
                                lines=4,
                                max_lines=12,
                                placeholder="What to generate. With reference images, the instruction: name what changes, e.g. “put a red bandana around the dog's neck” or “print the dog from the second image onto the mug”. Layout: end the prompt with a JSON list of boxes, [top, left, bottom, right] on a 0–1000 grid (see the examples).",
                            )
                        with gr.Accordion("Reference images · optional, up to 10", open=False) as refs_accordion:
                            gr.HTML("<p class='f3-hint'>Edit one image or combine several. Refer to them as the first image, the second image, … in upload order. The output takes the first image's shape.</p>")
                            input_images = gr.Gallery(
                                label="Images",
                                show_label=False,
                                file_types=["image"],
                                elem_id="f3-refs",
                                type="pil",
                                columns=5,
                                rows=1,
                                height=150,
                                object_fit="contain",
                                interactive=True,
                            )
                        mode_choice = gr.Radio(
                            label="Model",
                            elem_id="f3-mode",
                            choices=[DISTILLED, BASE],
                            value=DISTILLED,
                            info="Distilled: 16 steps, no guidance. Base: 50 steps, classifier-free guidance 4.",
                        )
                        aspect = gr.Radio(
                            label="Aspect ratio",
                            elem_id="f3-aspect",
                            choices=list(ASPECT_RATIOS),
                            value="1:1",
                        )
                        resolution = gr.Radio(
                            label="Resolution",
                            elem_id="f3-resolution",
                            choices=MODE_RESOLUTIONS[DISTILLED],
                            value=DEFAULT_RESOLUTION[DISTILLED],
                            info="Pixel count of the output: 1K ≈ 1 MP, 2K ≈ 4 MP, 4K ≈ 16 MP (Distilled only, ~2.5 min). Base runs at 1K on this Space.",
                        )
                        run_button = gr.Button("Generate", variant="primary", size="lg", elem_id="f3-run")
                        with gr.Accordion("Advanced settings", open=False):
                            prompt_upsampling = gr.Checkbox(
                                label="Prompt upsampling",
                                value=True,
                                visible=False,
                                info="Expand a short prompt into the detailed caption the model works best with, using the FLUX 3 Image Klein prompt upsampler. A prompt that ends in a box table is sent as it is.",
                            )
                            with gr.Row():
                                seed = gr.Slider(label="Seed", minimum=0, maximum=MAX_SEED, step=1, value=0, scale=3)
                                randomize_seed = gr.Checkbox(label="Randomize", value=True, scale=1, min_width=100)
                            with gr.Row():
                                width = gr.Slider(label="Width", minimum=256, maximum=MAX_IMAGE_SIZE, step=16, value=2048)
                                height = gr.Slider(label="Height", minimum=256, maximum=MAX_IMAGE_SIZE, step=16, value=2048)
                            with gr.Row():
                                num_inference_steps = gr.Slider(label="Steps", minimum=1, maximum=MAX_STEPS, step=1, value=16)
                                guidance_scale = gr.Slider(
                                    label="Guidance scale",
                                    minimum=0.0,
                                    maximum=10.0,
                                    step=0.1,
                                    value=1.0,
                                    interactive=False,
                                    info="Base model only",
                                )

                    with gr.Column(scale=6):
                        reuse_button = gr.Button("Use as reference", render=False)
                        result = gr.Image(
                            show_label=False,
                            elem_id="f3-result",
                            format="png",
                            type="pil",
                            interactive=False,
                            buttons=[reuse_button, "download", "fullscreen"],
                        )
                        with gr.Row():
                            meta = gr.HTML("<div class='f3-meta'></div>", scale=3)
                            show_boxes = gr.Checkbox(label="No boxes in this prompt", value=False, interactive=False, scale=2)
                        plain = gr.State(None)
                        with gr.Accordion("Prompt the model saw", open=False):
                            final_prompt = gr.Textbox(show_label=False, lines=3, max_lines=12, interactive=False)

                t2i_examples = gr.Examples(
                    examples=examples,
                    example_labels=example_labels,
                    label="Text to image",
                    fn=infer,
                    inputs=[prompt],
                    outputs=[result, seed, final_prompt],
                    cache_examples=True,
                    cache_mode="lazy",
                )
                seed_example_cache(t2i_examples, EXAMPLE_OUTPUTS)
                ref_examples = gr.Examples(
                    examples=examples_images,
                    example_labels=example_images_labels,
                    label="Edit with reference images",
                    fn=infer,
                    inputs=[prompt, input_images],
                    outputs=[result, seed, final_prompt],
                    cache_examples=True,
                    cache_mode="lazy",
                )
                seed_example_cache(ref_examples, EXAMPLE_IMAGE_OUTPUTS)
            with gr.Tab("Bounding boxes", id="bbox"):
                build_bbox_tab()

    input_images.change(fn=sync_references, inputs=[input_images, aspect, prompt, resolution], outputs=[width, height, aspect, refs_accordion], api_visibility="private")
    ref_examples.load_input_event.then(fn=sync_references, inputs=[input_images, aspect, prompt, resolution], outputs=[width, height, aspect, refs_accordion], api_visibility="private")
    aspect.input(fn=set_aspect, inputs=[aspect, input_images, resolution], outputs=[width, height], api_visibility="private")
    resolution.input(fn=set_aspect, inputs=[aspect, input_images, resolution], outputs=[width, height], api_visibility="private")
    mode_choice.change(fn=update_steps_from_mode, inputs=[mode_choice, aspect, input_images], outputs=[num_inference_steps, guidance_scale, resolution, width, height], api_visibility="private")
    reuse_button.click(
        fn=use_as_reference,
        inputs=[result, input_images],
        outputs=[input_images, refs_accordion],
        api_visibility="private",
    )

    show_boxes.input(fn=toggle_boxes, inputs=[show_boxes, plain, final_prompt], outputs=result, api_visibility="private")
    final_prompt.change(fn=boxes_toggle, inputs=[final_prompt, result], outputs=[show_boxes, plain], api_visibility="private")

    gr.on(
        triggers=[run_button.click, prompt.submit],
        fn=infer,
        inputs=[prompt, input_images, mode_choice, seed, randomize_seed, width, height, num_inference_steps, guidance_scale, prompt_upsampling],
        outputs=[result, seed, final_prompt],
        api_name="generate",
    ).then(
        fn=describe_result,
        inputs=[seed, mode_choice, width, height],
        outputs=[meta],
        api_visibility="private",
    )
    return tabs


def pick_tab(request: gr.Request):
    """The Space opens on Bounding boxes; ?tab=generate opens it on Generate & edit."""
    tab = (request.query_params.get("tab") or "").lower() if request else ""
    return gr.Tabs(selected="generate" if tab == "generate" else "bbox")


demo = gr.Workflow(graph=os.path.join(HERE, "workflow.json"), bind=[flux3_klein])
with _active_blocks(demo, demo._api_endpoints.app_root):
    tabs = build_app()
    demo.load(fn=pick_tab, outputs=tabs, api_visibility="private")

demo.launch(theme=theme, css=css, mcp_server=True)
