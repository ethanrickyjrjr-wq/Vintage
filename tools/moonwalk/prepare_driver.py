"""Prepare a wide, 4.5-second motion driver with the mannequin's visible head.

This edits continuous driving video, not pose stills or the final animation.
It keeps RichKaz's actual footwork, keys the head position, composites the character
head, widens the shot and slows playback. No optical-flow frames are synthesized.
"""

import json
from pathlib import Path
import subprocess
import tempfile

import cv2
import numpy as np


def main():
    assets = Path(__file__).resolve().parents[2] / "assets" / "moonwalk"
    capture = cv2.VideoCapture(str(assets / "moonwalk-driver-side.mp4"))
    frames = []
    while True:
        ok, frame = capture.read()
        if not ok:
            break
        frames.append(frame)
    capture.release()
    if not frames:
        raise RuntimeError("Cannot decode the driving clip")

    keys = np.array([
        [0, 291, 123], [12, 242, 140], [24, 235, 94], [36, 257, 102],
        [48, 235, 100], [60, 204, 96], [72, 225, 111], [85, 234, 109],
    ], dtype=np.float32)
    anchors = np.column_stack([
        np.interp(np.arange(len(frames)), keys[:, 0], keys[:, axis]) for axis in (1, 2)
    ]).astype(np.float32)
    anchors = cv2.GaussianBlur(anchors[:, None, :], (1, 7), 1.3)[:, 0, :]

    reference = cv2.imread(str(assets / "mannequin_full_body_wide.png"))
    polygon = np.array([
        [580, 240], [650, 237], [677, 248], [688, 278], [695, 310],
        [687, 338], [672, 360], [655, 380], [644, 398], [626, 400],
        [615, 382], [591, 371], [569, 351], [554, 333], [552, 317],
        [561, 300], [570, 272],
    ], dtype=np.int32)
    mask = np.zeros(reference.shape[:2], dtype=np.uint8)
    cv2.fillPoly(mask, [polygon], 255)
    mask = cv2.GaussianBlur(mask, (5, 5), 0.8)
    head = reference[230:408, 548:708]
    alpha = mask[230:408, 548:708].astype(np.float32) / 255
    head_anchor = np.array([83., 167.])
    scale = 0.44

    with tempfile.TemporaryDirectory() as temporary:
        raw = Path(temporary) / "driver.mp4"
        writer = cv2.VideoWriter(str(raw), cv2.VideoWriter_fourcc(*"mp4v"), 24, (480, 480))
        for frame, anchor in zip(frames, anchors):
            offset = anchor - head_anchor * scale
            transform = np.array([[scale, 0, offset[0]], [0, scale, offset[1]]], np.float32)
            layer = cv2.warpAffine(head, transform, (480, 480))
            opacity = cv2.warpAffine(alpha, transform, (480, 480))[:, :, None]
            composite = (layer * opacity + frame * (1 - opacity)).astype(np.uint8)
            wide = cv2.warpAffine(composite, np.array([[0.8, 0, 48], [0, 0.8, 48]], np.float32),
                                  (480, 480), borderValue=(40, 5, 40))
            writer.write(wide)
        writer.release()
        output = assets / "moonwalk-driver-facing.mp4"
        subprocess.run([
            "ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", str(raw),
            "-vf", f"setpts={108 / len(frames):.10f}*PTS,fps=24", "-frames:v", "108",
            "-c:v", "libx264", "-crf", "17", "-pix_fmt", "yuv420p", "-an", str(output),
        ], check=True)
    (assets / "driver-facing-tracking.json").write_text(json.dumps({
        "input": "moonwalk-driver-side.mp4", "input_frames": len(frames),
        "output_frames": 108, "fps": 24, "head_reference": "mannequin_full_body_wide.png",
        "neck_anchors": anchors.round(2).tolist(),
        "edits": "tracked head composite, 80 percent framing, slowed to 4.5 seconds; no synthesized frames",
    }, indent=2), encoding="utf-8")
    print(output)


if __name__ == "__main__":
    main()
