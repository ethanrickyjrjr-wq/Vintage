"""Download verified local weights, render a candidate, and save it for review.

Run with the moonwalk-local Python environment. Logs and state stay in .venv.
This worker never buys GPU time or marks a candidate visually approved.
"""

from datetime import datetime, timezone
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys

from huggingface_hub import HfApi, constants, snapshot_download
from filelock import FileLock, Timeout


ROOT = Path(os.environ.get("MOONWALK_ROOT", Path(__file__).resolve().parents[2]))
JOB = ROOT / ".venv" / "moonwalk-local" / "job"
MODEL = "Wan-AI/Wan2.2-Animate-2-14B-Distilled-Diffusers"
PATTERNS = ["transformer/*", "text_encoder/*", "image_encoder/*", "vae/*",
            "scheduler/*", "tokenizer/*", "modular_model_index.json"]


def state(phase, **details):
    JOB.mkdir(parents=True, exist_ok=True)
    payload = {"phase": phase, "updated_utc": datetime.now(timezone.utc).isoformat(), **details}
    (JOB / "status.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(json.dumps(payload), flush=True)


def main():
    info = HfApi().model_info(MODEL, files_metadata=True)
    env = dict(os.environ, MOONWALK_ROOT=str(ROOT), MOONWALK_MODEL_REVISION=info.sha)
    blobs = Path(constants.HF_HUB_CACHE) / ("models--" + MODEL.replace("/", "--")) / "blobs"
    blobs.mkdir(parents=True, exist_ok=True)
    entries = []
    for item in info.siblings:
        if item.lfs and item.rfilename.startswith(("transformer/", "text_encoder/", "image_encoder/", "vae/")):
            entries.extend([
                f"https://huggingface.co/{MODEL}/resolve/{info.sha}/{item.rfilename}",
                f"  dir={blobs}", f"  out={item.lfs.sha256}",
                f"  checksum=sha-256={item.lfs.sha256}",
            ])
    manifest = JOB / "model-downloads.txt"
    manifest.write_text("\n".join(entries) + "\n", encoding="utf-8")
    state("downloading", revision=info.sha, files=len(entries) // 4)
    subprocess.run([
        shutil.which("aria2c") or "aria2c", f"--input-file={manifest}",
        "--max-concurrent-downloads=3", "--max-connection-per-server=16", "--split=16",
        "--min-split-size=1M", "--file-allocation=none", "--continue=true",
        "--auto-file-renaming=false", "--allow-overwrite=true", "--check-integrity=true",
        "--summary-interval=60", "--show-console-readout=false", "--console-log-level=warn",
        "--download-result=hide",
    ], check=True, cwd=ROOT)
    state("preparing_cache", revision=info.sha)
    snapshot_download(MODEL, revision=info.sha, allow_patterns=PATTERNS, max_workers=2)
    state("rendering", revision=info.sha)
    subprocess.run([sys.executable, "-u", str(Path(__file__).with_name("generate_local.py"))],
                   env=env, cwd=ROOT, check=True)
    candidates = ROOT / "assets" / "moonwalk" / "candidates"
    output = max(candidates.glob("local-*"), key=lambda path: path.stat().st_mtime)
    subprocess.run([
        "ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", str(output / "candidate.mp4"),
        "-vf", "fps=2,scale=384:384,tile=3x3", "-frames:v", "1", str(output / "review.jpg"),
    ], check=True)
    # Only this run's generated files may enter the commit; other work can be active here.
    relative = str(output.relative_to(ROOT)).replace("\\", "/")
    for path in output.glob("*.json"):
        if re.search(r"hf_[A-Za-z0-9]{16,}|sk-[A-Za-z0-9]{16,}|-----BEGIN.*PRIVATE KEY", path.read_text()):
            raise RuntimeError("Secret scan rejected generated metadata")
    subprocess.run(["git", "add", "--", relative], cwd=ROOT, check=True)
    subprocess.run(["git", "commit", "--only", "-m", "Save local moonwalk candidate for visual review", "--", relative],
                   cwd=ROOT, check=True)
    pushed = subprocess.run(["git", "push", "origin", "master"], cwd=ROOT, capture_output=True, text=True)
    state("ready_for_visual_review", output=relative, pushed=pushed.returncode == 0,
          push_error=pushed.stderr.strip() if pushed.returncode else None)


if __name__ == "__main__":
    JOB.mkdir(parents=True, exist_ok=True)
    try:
        with FileLock(str(JOB / "worker.lock"), timeout=0):
            main()
    except Timeout:
        sys.exit("A local moonwalk worker is already running.")
    except Exception as error:
        state("failed", error=str(error))
        raise
