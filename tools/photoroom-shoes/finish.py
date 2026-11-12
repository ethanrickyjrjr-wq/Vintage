#!/usr/bin/env python3
"""Lay cut-out shoe PNGs onto the background each shot needs (white, or light grey for white soles).

usage: python tools/photoroom-shoes/finish.py <folder of transparent PNGs named <pair>-NN-<slug>.png>
Reads the background column of shots-2026-11-12.csv and writes
assets/ebay-2026-11-12/shoes/<pair>/<name>.jpg, 1600x1600, item filling 85%, contact shadow.
The PNGs come from tools/cutout/cutout.py (its site/ folder) or any other cut-out tool.
"""
import csv, sys
from pathlib import Path
from PIL import Image, ImageFilter

HERE = Path(__file__).resolve().parent
OUT = HERE.parent.parent / "assets/ebay-2026-11-12/shoes"
SIZE, FILL, SHADOW = 1600, 0.85, 0.25


def place(item, bg):
    scale = FILL * SIZE / max(item.size)
    item = item.resize((round(item.width * scale), round(item.height * scale)), Image.Resampling.LANCZOS)
    canvas = Image.new("RGB", (SIZE, SIZE), "#" + bg)
    x, y = (SIZE - item.width) // 2, (SIZE - item.height) // 2
    sh = max(8, int(item.height * 0.12))  # same contact shadow as tools/cutout/cutout.py
    foot = item.getchannel("A").resize((item.width, sh), Image.Resampling.LANCZOS)
    layer = Image.new("L", (SIZE, SIZE), 0)
    layer.paste(foot, (x, y + item.height - sh // 2))
    layer = layer.filter(ImageFilter.GaussianBlur(max(4, int(item.height * 0.025))))
    canvas.paste(Image.new("RGB", (SIZE, SIZE), "black"), (0, 0), layer.point(lambda v: int(v * SHADOW)))
    canvas.paste(item, (x, y), item)
    return canvas


def main():
    src = Path(sys.argv[1])
    counters = {}
    for r in csv.DictReader(open(HERE / "shots-2026-11-12.csv")):
        counters[r["pair"]] = counters.get(r["pair"], 0) + 1
        if r["mode"] != "cutout":
            continue
        name = f"{r['pair']}-{counters[r['pair']]:02d}-{r['slug']}"
        png = src / f"{name}.png"
        if not png.exists():
            print("missing", png.name)
            continue
        dest = OUT / r["pair"] / f"{name}.jpg"
        dest.parent.mkdir(parents=True, exist_ok=True)
        place(Image.open(png).convert("RGBA"), r["background"]).save(dest, quality=92)
        print(dest.name, r["background"])


if __name__ == "__main__":
    main()
