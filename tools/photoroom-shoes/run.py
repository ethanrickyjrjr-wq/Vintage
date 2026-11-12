#!/usr/bin/env python3
"""Run the shoe photos through the Photoroom Image Editing API (v2/edit).

usage: python tools/photoroom-shoes/run.py <dir with IMG_NNNN.heic/.jpg> [--only cutout|keep] [--force]
needs: pip install pillow pillow-heif requests ; PHOTOROOM_API_KEY in the environment
       (on the cloud box the proxy can inject the key, then any non-empty value works)

Reads shots-2026-11-12.csv next to this file. 'cutout' rows go to Photoroom
(removeBackground, background.color from the row, padding 0.1, soft AI shadow,
1600x1600 JPEG). 'keep' rows (labels, tape shots) are only rotated upright and
resized to 1600 px on the long side, never cut. Output:
assets/ebay-2026-11-12/shoes/<pair>/<pair>-NN-<slug>.jpg plus manifest.csv.
API docs read 2026-11-12: docs.photoroom.com/image-editing-api-plus-plan
($0.10 a call; a re-run is billed again, so finished files are skipped unless --force).
"""
import csv, io, os, sys, time
from pathlib import Path
import requests, pillow_heif
from PIL import Image, ImageOps

pillow_heif.register_heif_opener()
HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
OUT = REPO / "assets/ebay-2026-11-12/shoes"
API = "https://image-api.photoroom.com/v2/edit"


def find(src, img):
    for ext in (".heic", ".HEIC", ".jpg", ".JPG", ".jpeg", ".png"):
        p = Path(src) / f"IMG_{img}{ext}"
        if p.exists():
            return p
    raise SystemExit(f"missing IMG_{img} in {src}")


def upright_jpeg(path, long_side):
    im = ImageOps.exif_transpose(Image.open(path)).convert("RGB")
    im.thumbnail((long_side, long_side), Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, "JPEG", quality=92)
    return buf.getvalue()


def main():
    args = sys.argv[1:]
    if not args:
        raise SystemExit(__doc__)
    src, only, force = args[0], None, "--force" in args
    if "--only" in args:
        only = args[args.index("--only") + 1]
    key = os.environ.get("PHOTOROOM_API_KEY", "")
    rows = list(csv.DictReader(open(HERE / "shots-2026-11-12.csv")))
    counters, log = {}, []
    for r in rows:
        counters[r["pair"]] = counters.get(r["pair"], 0) + 1
        name = f"{r['pair']}-{counters[r['pair']]:02d}-{r['slug']}.jpg"
        dest = OUT / r["pair"] / name
        log.append({**r, "file": f"{r['pair']}/{name}"})
        if only and r["mode"] != only:
            continue
        if dest.exists() and not force:
            continue
        dest.parent.mkdir(parents=True, exist_ok=True)
        if r["mode"] == "keep":
            dest.write_bytes(upright_jpeg(find(src, r["img"]), 1600))
            print("keep  ", dest.relative_to(REPO))
            continue
        if not key:
            raise SystemExit("PHOTOROOM_API_KEY is not set")
        data = {
            "removeBackground": "true",
            "background.color": r["background"],
            "padding": "0.1",
            "shadow.mode": "ai.soft",
            "outputSize": "1600x1600",
            "export.format": "jpeg",
        }
        body = upright_jpeg(find(src, r["img"]), 3000)
        for attempt in range(4):
            resp = requests.post(API, headers={"x-api-key": key}, data=data,
                                 files={"imageFile": (f"IMG_{r['img']}.jpg", body, "image/jpeg")}, timeout=180)
            if resp.status_code == 200:
                break
            print(f"  {r['img']}: HTTP {resp.status_code} {resp.text[:200]}")
            if resp.status_code in (401, 402, 403):
                raise SystemExit("key refused; stopping before more calls")
            time.sleep(2 ** attempt * 3)
        else:
            raise SystemExit(f"gave up on {r['img']}")
        dest.write_bytes(resp.content)
        print("photoroom", dest.relative_to(REPO), r["background"])
    with open(OUT / "manifest.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["file", "img", "pair", "slug", "mode", "background", "note"])
        w.writeheader()
        w.writerows(log)


if __name__ == "__main__":
    main()
