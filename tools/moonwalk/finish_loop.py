"""Composite continuous generated footwork onto a fixed disco room and loop it.

Run with .venv/cutout/Scripts/python.exe. Uses video mattes, not generated poses
or optical-flow frame synthesis. Source motion remains in the candidate MP4.
"""

import argparse
import json
from pathlib import Path
import subprocess
import sys
import tempfile

import cv2
import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools" / "cutout"))
from cutout import open_session, provider_name


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    assets = ROOT / "assets" / "moonwalk"
    capture = cv2.VideoCapture(str(args.input))
    source = []
    while True:
        ok, frame = capture.read()
        if not ok:
            break
        source.append(frame)
    capture.release()
    if len(source) != 108:
        raise ValueError("This finishing edit expects the reviewed 108-frame candidate")

    start, length, overlap, repeats = 46, 52, 4, 2
    frames = source[start:start + length]
    session, provider = open_session("u2netp", provider_name())
    mattes, heads, floors = [], [], []
    for index, frame in enumerate(frames):
        matte = np.asarray(session.predict(Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)))[0], np.float32) / 255
        matte = np.clip((matte - 0.1) / 0.8, 0, 1)
        b, g, r = cv2.split(frame.astype(np.float32))
        skin = ((r > g * 1.07) & (g > b * 1.02) & (r > 85) & (g > 60)).astype(np.uint8)
        skin[:35] = 0
        skin[106:] = 0
        skin[:, :85] = 0
        skin[:, 230:] = 0
        sy, sx = np.where(skin)
        if len(sy) < 8:
            raise ValueError(f"Cannot locate mannequin face at source frame {start + index}")
        hx, hy = float(np.median(sx)), float(np.median(sy))
        # The disco ball can touch the hat in the source and join the salient mask.
        # Constrain the head area to the face/cap rather than retaining that ball.
        head_limit = np.zeros((384, 384), np.uint8)
        cv2.ellipse(head_limit, (round(hx), round(hy - 7)), (24, 34), 0, 0, 360, 255, -1)
        head_limit[round(hy + 24):] = 255
        head_limit = cv2.GaussianBlur(head_limit, (5, 5), .8).astype(np.float32) / 255
        matte *= head_limit
        count, labels, stats, _ = cv2.connectedComponentsWithStats((matte > 0.2).astype(np.uint8))
        if count < 2:
            raise ValueError(f"No character matte at source frame {start + index}")
        body = 1 + np.argmax(stats[1:, cv2.CC_STAT_AREA])
        keep = cv2.dilate((labels == body).astype(np.uint8), np.ones((3, 3), np.uint8))
        matte *= keep
        ys, xs = np.where(matte > 0.75)
        top, bottom = int(ys.min()), int(ys.max())
        heads.append((hx, hy))
        floors.append(float(bottom))
        mattes.append(matte)
        if index % 12 == 0:
            print(f"Matting continuous video: {index + 1}/{length}", flush=True)
    heads = cv2.GaussianBlur(np.array(heads, np.float32)[:, None, :], (1, 5), .9)[:, 0, :]
    floors = cv2.GaussianBlur(np.array(floors, np.float32)[:, None], (1, 3), .6).ravel()
    layers = []
    for frame, matte, (hx, hy), floor in zip(frames, mattes, heads, floors):
        scale = (330 - 87) / (floor - hy)
        transform = np.array([[scale, 0, 192 - hx * scale], [0, scale, 87 - hy * scale]], np.float32)
        alpha = cv2.warpAffine(matte, transform, (384, 384))
        color = cv2.warpAffine(frame.astype(np.float32) * matte[:, :, None], transform, (384, 384))
        layers.append(np.concatenate([color, alpha[:, :, None]], axis=2))

    # Dissolve only matching character layers; the room remains fixed throughout.
    transition = []
    for index in range(overlap):
        amount = index / (overlap - 1)
        transition.append(layers[-overlap + index] * (1 - amount) + layers[index] * amount)
    cycle = transition + layers[overlap:-overlap]
    background = cv2.resize(cv2.imread(str(assets / "disco-background.png")), (384, 384)).astype(np.float32)
    rendered = []
    for layer in cycle:
        color, alpha = layer[:, :, :3], layer[:, :, 3:]
        plate = background.copy()
        reflection_color = color[276:330][::-1]
        reflection_alpha = alpha[276:330][::-1]
        fade = (.16 * (1 - np.arange(54) / 54) ** 2)[:, None, None]
        reflection_color = cv2.GaussianBlur(reflection_color, (5, 5), 1.2)
        reflection_alpha = cv2.GaussianBlur(reflection_alpha, (5, 5), 1.2)[:, :, None]
        plate[330:384] = reflection_color * fade + plate[330:384] * (1 - reflection_alpha * fade)
        rendered.append(np.clip(color + plate * (1 - alpha), 0, 255).astype(np.uint8))

    video = assets / "mustache-moonwalk-final.mp4"
    gif = assets / "mustache-moonwalk-final.gif"
    with tempfile.TemporaryDirectory() as temporary:
        raw = Path(temporary) / "loop.mp4"
        writer = cv2.VideoWriter(str(raw), cv2.VideoWriter_fourcc(*"mp4v"), 24, (384, 384))
        for frame in rendered * repeats:
            writer.write(frame)
        writer.release()
        subprocess.run([
            "ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", str(raw),
            "-c:v", "libx264", "-crf", "16", "-pix_fmt", "yuv420p", "-movflags", "+faststart",
            "-metadata", "title=Mustache Moonwalk", "-metadata", "comment=RichKaz motion reference, CC BY 3.0; see CREDITS.txt",
            "-an", str(video),
        ], check=True)
    subprocess.run([
        "ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", str(video),
        "-filter_complex", "[0:v]fps=15,scale=480:-1:flags=lanczos,split[a][b];"
        "[a]palettegen=max_colors=256:stats_mode=diff[p];[b][p]paletteuse=dither=sierra2_4a",
        "-an", "-loop", "0", str(gif),
    ], check=True)
    (assets / "loop-finishing.json").write_text(json.dumps({
        "source": str(args.input).replace("\\", "/"), "source_frames": [start, start + length - 1],
        "mask_model": "u2netp", "provider": provider, "background": "disco-background.png",
        "overlap_frames": overlap, "cycle_frames": len(cycle), "repeats": repeats,
        "fps": 24, "frames": len(cycle) * repeats, "seconds": len(cycle) * repeats / 24,
        "edits": "character matte, fixed backdrop, head/foot framing normalization, soft reflection, four-frame character dissolve",
        "motion": "continuous model-generated frames; no pose grid, reversed playback or optical-flow frame interpolation",
    }, indent=2), encoding="utf-8")
    print(video)
    print(gif)


if __name__ == "__main__":
    main()
