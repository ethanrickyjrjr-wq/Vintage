"""Private, in-memory room previews. No paid inference provider is used."""
import os
os.environ.setdefault("GRADIO_ANALYTICS_ENABLED", "False")
import spaces  # Must precede torch and diffusers for ZeroGPU.
import base64
import io
import math
import time
import warnings
import gradio as gr
import torch
from diffusers import Flux2KleinPipeline
from PIL import Image, ImageOps

Image.MAX_IMAGE_PIXELS = 12_000_000
warnings.simplefilter("error", Image.DecompressionBombWarning)
print("Loading FLUX.2 Klein 4B on ZeroGPU.")
pipe = Flux2KleinPipeline.from_pretrained(
    "black-forest-labs/FLUX.2-klein-4B", torch_dtype=torch.bfloat16,
).to("cuda")
print("Room renderer model loaded.")


def decode_image(value: dict) -> Image.Image:
    """Decode a bounded image from server-owned request JSON."""
    if not isinstance(value, dict) or value.get("mimeType") not in {"image/jpeg", "image/png", "image/webp"}:
        raise gr.Error("Unsupported photo format.")
    data = value.get("data", "")
    if not isinstance(data, str) or len(data) > 4_000_000:
        raise gr.Error("Photo is too large.")
    image = Image.open(io.BytesIO(base64.b64decode(data, validate=True)))
    image.load()
    image = ImageOps.exif_transpose(image).convert("RGB")
    if min(image.size) < 100:
        raise gr.Error("Photo is too small.")
    image.thumbnail((1280, 1280))
    return image


@spaces.GPU(duration=15)
def render_room(payload: dict) -> dict:
    """Edit one room using its photo, one catalog reference, and a target close-up.

    Returns a base64 styling preview and measured runtime. Images are never saved.
    """
    started = time.perf_counter()
    if not isinstance(payload, dict):
        raise gr.Error("Expected a room-preview request.")
    room = decode_image(payload.get("room"))
    product = decode_image(payload.get("reference"))
    outline = payload.get("outline")
    if isinstance(outline, list) and len(outline) == 4:
        # Rectify the artwork from its original photograph so the model sees
        # the actual piece without the surrounding shop wall. Original files
        # remain unchanged; this reference exists only during inference.
        points = [(float(x) * product.width, float(y) * product.height) for x, y in outline]
        if any(not 0 <= x <= product.width or not 0 <= y <= product.height for x, y in points):
            raise gr.Error("Invalid reference outline.")
        top_left, top_right, bottom_right, bottom_left = points
        target_width = round((math.dist(top_left, top_right) + math.dist(bottom_left, bottom_right)) / 2)
        target_height = round((math.dist(top_left, bottom_left) + math.dist(top_right, bottom_right)) / 2)
        product = product.transform((target_width, target_height), Image.Transform.QUAD,
                                    (*top_left, *bottom_left, *bottom_right, *top_right), Image.Resampling.BICUBIC)
    prompt = payload.get("prompt", "")
    if not isinstance(prompt, str) or not 20 <= len(prompt) <= 5000:
        raise gr.Error("Invalid styling instructions.")
    images = [room, product]
    box = payload.get("box")
    point = payload.get("point")
    if payload.get("mode") == "replace" and isinstance(box, dict):
        target = room.crop((int(box["x"] * room.width), int(box["y"] * room.height),
                            int((box["x"] + box["width"]) * room.width),
                            int((box["y"] + box["height"]) * room.height)))
        images.append(target)
        prompt += " Image 3 is a close-up of the EXISTING object to replace in image 1. Remove that existing object from image 1 and put the product from image 2 in its place, sized to fit. Keep the full room viewpoint of image 1."
    elif payload.get("mode") == "place" and isinstance(point, dict):
        x, y = int(point["x"] * room.width), int(point["y"] * room.height)
        radius = max(50, int(room.width * float(payload.get("size", .25)) / 2))
        target = room.crop((max(0, x - radius), max(0, y - radius), min(room.width, x + radius), min(room.height, y + radius)))
        images.append(target)
        prompt += " Image 3 is a close-up of the selected location in image 1. Center the product from image 2 at this location, keeping the full room viewpoint of image 1."
    scale = min(1.0, 1024 / max(room.size))
    width = max(256, round(room.width * scale / 16) * 16)
    height = max(256, round(room.height * scale / 16) * 16)
    with torch.inference_mode():
        result = pipe(
            prompt=prompt, image=images, width=width, height=height,
            num_inference_steps=4, guidance_scale=1.0,
            generator=torch.Generator(device="cuda").manual_seed(42),
        ).images[0]
    buffer = io.BytesIO()
    result.save(buffer, format="WEBP", quality=94)
    seconds = round(time.perf_counter() - started, 2)
    print(f"Room preview completed in {seconds}s.")
    return {"image": "data:image/webp;base64," + base64.b64encode(buffer.getvalue()).decode("ascii"), "seconds": seconds}


with gr.Blocks(title="Hollywood and Vine Room Renderer") as demo:
    gr.Markdown("# Hollywood & Vine room renderer\nPrivate service for the storefront. Photos are processed in memory.")
    request = gr.JSON(label="Room request")
    result = gr.JSON(label="Styling preview")
    run = gr.Button("Render room")
    run.click(render_room, inputs=request, outputs=result, api_name="render_room", concurrency_limit=1)

demo.queue(max_size=5).launch(mcp_server=True, enable_monitoring=False, show_error=False)
