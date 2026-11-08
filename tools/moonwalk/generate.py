"""Retry the saved free motion-transfer attempt, then export a candidate GIF."""

import argparse
from datetime import datetime, timezone
from pathlib import Path
import shutil
import subprocess
import sys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--size", type=int, default=416)
    parser.add_argument("--steps", type=int, default=6)
    parser.add_argument("--seed", type=int, default=57)
    args = parser.parse_args()
    if args.size < 256 or args.size % 16:
        parser.error("--size must be at least 256 and a multiple of 16")
    if args.steps < 1:
        parser.error("--steps must be positive")

    from gradio_client import Client, handle_file
    from huggingface_hub import get_token

    assets = Path(__file__).resolve().parents[2] / "assets" / "moonwalk"
    token = get_token()
    if not token:
        parser.error("Log in with hf auth login before using free ZeroGPU inference")
    ffmpeg = shutil.which("ffmpeg")
    if not ffmpeg:
        parser.error("ffmpeg is required to make the candidate GIF")

    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    output = assets / "candidates" / stamp
    output.mkdir(parents=True)
    client = Client(
        "hugging-apps/wan2-2-animate",
        token=token,
        download_files=str(output / "download"),
        verbose=False,
    )
    print("Requesting free motion transfer; a quota error will stop this run.", flush=True)
    try:
        result = client.predict(
            handle_file(str(assets / "mannequin_full_body_start.png")),
            handle_file(str(assets / "moonwalk-driver-side.mp4")),
            (assets / "prompt.txt").read_text(encoding="utf-8"),
            4.5,
            args.size,
            args.size,
            args.steps,
            args.seed,
            "The central dancer moonwalks backward in profile, with alternating "
            "raised heels and backward sliding flat feet. Transfer his footwork "
            "and subtle arm sway, keep the reference character face visible.",
            api_name="/animate",
        )
    except Exception as error:
        print(f"Generation failed: {error}", file=sys.stderr)
        return 1

    video = output / "candidate.mp4"
    gif = output / "candidate.gif"
    shutil.copyfile(result, video)
    shutil.copyfile(assets / "CREDITS.txt", output / "CREDITS.txt")
    subprocess.run(
        [
            ffmpeg, "-hide_banner", "-loglevel", "error", "-y", "-i", str(video),
            "-filter_complex",
            "[0:v]fps=15,scale=480:-1:flags=lanczos,split[a][b];"
            "[a]palettegen=max_colors=256:stats_mode=diff[p];"
            "[b][p]paletteuse=dither=sierra2_4a",
            "-an", "-loop", "0", str(gif),
        ],
        check=True,
    )
    print(video)
    print(gif)
    print("Candidate only: inspect mustache, hat, shoes, footwork and loop seam.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
