"""Generate the mannequin moonwalk locally on a 16 GB NVIDIA GPU.

Use .venv/moonwalk-local/Scripts/python.exe; see docs/mustache-moonwalk.md.
Model weights stay in the Hugging Face cache, outside Git.
"""

import argparse
from datetime import datetime, timezone
import gc
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import time

import torch
from diffusers import BitsAndBytesConfig, WanAnimate2DistilledModularPipeline
from diffusers.modular_pipelines.wan_animate_2.encoders import get_t5_prompt_embeds
from diffusers.utils import export_to_video, load_image, load_video
from transformers import BitsAndBytesConfig as TextQuantization
from transformers import AutoTokenizer, UMT5EncoderModel

from local_attention import configure


MODEL = "Wan-AI/Wan2.2-Animate-2-14B-Distilled-Diffusers"
ROOT = Path(__file__).resolve().parents[2]
ASSETS = ROOT / "assets" / "moonwalk"
REFERENCE_PROMPT = (
    "The central dancer moonwalks backward in profile, with alternating raised "
    "heels and backward sliding flat feet. Transfer his footwork and subtle arm "
    "sway, keep the reference character face visible."
)


def prompt_embeddings(prompt):
    fingerprint = hashlib.sha256((MODEL + prompt + REFERENCE_PROMPT).encode()).hexdigest()[:16]
    cache = ROOT / ".venv" / "moonwalk-local" / f"prompt-{fingerprint}.pt"
    if cache.exists():
        return torch.load(cache, map_location="cuda", weights_only=True)
    print("Encoding prompts with 4-bit T5.", flush=True)
    encoder = UMT5EncoderModel.from_pretrained(
        MODEL, subfolder="text_encoder", torch_dtype=torch.bfloat16,
        quantization_config=TextQuantization(
            load_in_4bit=True, bnb_4bit_quant_type="nf4",
            bnb_4bit_compute_dtype=torch.bfloat16, bnb_4bit_use_double_quant=True,
        ), device_map={"": "cuda:0"},
    )
    tokenizer = AutoTokenizer.from_pretrained(MODEL, subfolder="tokenizer")
    with torch.no_grad():
        embeds = {
            "prompt_embeds": get_t5_prompt_embeds(encoder, tokenizer, prompt, 512, "cuda"),
            "prompt_ref_embeds": get_t5_prompt_embeds(encoder, tokenizer, REFERENCE_PROMPT, 512, "cuda"),
        }
    torch.save({k: v.cpu() for k, v in embeds.items()}, cache)
    del encoder, tokenizer
    gc.collect()
    torch.cuda.empty_cache()
    return embeds


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--size", type=int, default=384)
    parser.add_argument("--steps", type=int, default=6)
    parser.add_argument("--seed", type=int, default=57)
    parser.add_argument("--segment-frames", type=int, default=49)
    args = parser.parse_args()
    if args.size < 256 or args.size % 16:
        parser.error("--size must be at least 256 and a multiple of 16")
    if args.steps < 1 or args.segment_frames < 5 or args.segment_frames % 4 != 1:
        parser.error("positive steps and segment frames of the form 4n+1 required")
    if not torch.cuda.is_available():
        parser.error("A CUDA GPU is required")
    if not shutil.which("ffmpeg"):
        parser.error("ffmpeg is required")
    configure()
    torch.set_num_threads(4)
    torch.backends.cuda.matmul.allow_tf32 = True
    prompt = (ASSETS / "prompt.txt").read_text(encoding="utf-8")
    embeds = prompt_embeddings(prompt)
    print("Loading 4-bit motion-transfer model; reference cache stays on CPU.", flush=True)
    pipe = WanAnimate2DistilledModularPipeline.from_pretrained(MODEL)
    del pipe.blocks.sub_blocks["text_encoder"]
    pipe.load_components(
        names=["image_encoder", "vae", "scheduler", "transformer"],
        dtype=torch.bfloat16, revision=None,
        quantization_config={"transformer": BitsAndBytesConfig(
            load_in_4bit=True, bnb_4bit_quant_type="nf4",
            bnb_4bit_compute_dtype=torch.bfloat16, bnb_4bit_use_double_quant=True,
        )},
        device_map={"transformer": {"": "cuda:0"}},
    )
    for name in ["image_encoder", "vae", "scheduler", "transformer"]:
        if getattr(pipe, name, None) is None:
            raise RuntimeError(f"Required component did not load: {name}")
    pipe.to("cuda")
    pipe.vae.enable_tiling()
    frames, fps = load_video(str(ASSETS / "moonwalk-driver-side.mp4"), return_fps=True)
    output = ASSETS / "candidates" / datetime.now(timezone.utc).strftime("local-%Y%m%dT%H%M%SZ")
    output.mkdir(parents=True)
    settings = {"model": MODEL, "quantization": "NF4 double quantization",
                "reference_cache": "CPU, original tensor dtype", **vars(args),
                "driver": "moonwalk-driver-side.mp4", "prompt": prompt,
                "prompt_ref": REFERENCE_PROMPT, "status": "candidate, needs visual review"}
    (output / "generation.json").write_text(json.dumps(settings, indent=2), encoding="utf-8")
    shutil.copyfile(ASSETS / "CREDITS.txt", output / "CREDITS.txt")
    print(f"Rendering to {output}", flush=True)
    started = time.monotonic()
    with torch.no_grad():
        videos = pipe(
            image=load_image(str(ASSETS / "mannequin_full_body_start.png")),
            driving_video=frames, driving_video_fps=fps, fps=24,
            height=args.size, width=args.size,
            segment_frame_length=args.segment_frames,
            num_inference_steps=args.steps,
            generator=torch.Generator(device="cuda").manual_seed(args.seed),
            output_type="np", output="videos", **embeds,
        )
    video = output / "candidate.mp4"
    export_to_video(videos[0], str(video), fps=24)
    subprocess.run([
        "ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", str(video),
        "-filter_complex", "[0:v]fps=15,scale=480:-1:flags=lanczos,split[a][b];"
        "[a]palettegen=max_colors=256:stats_mode=diff[p];[b][p]paletteuse=dither=sierra2_4a",
        "-an", "-loop", "0", str(output / "candidate.gif"),
    ], check=True)
    print(f"Render finished in {time.monotonic() - started:.0f} seconds: {video}", flush=True)
    print("Candidate only: inspect face, mustache, outfit, shoes, footwork and loop seam.")


if __name__ == "__main__":
    main()
