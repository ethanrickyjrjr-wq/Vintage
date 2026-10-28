"""Cut real item photos into site cutouts and marketplace JPEGs; mask only, never redrawn.

Setup once, from the repo root (Windows):
    uv venv .venv/cutout --python 3.12
    uv pip install --python .venv/cutout/Scripts/python.exe "rembg[cpu]==2.0.86" "pillow-heif==1.8.1"

Run (the first run downloads the model, about 1 GB, to ~/.u2net or ~/.rembg):
    .venv/cutout/Scripts/python.exe tools/cutout/cutout.py PHOTOS_FOLDER [OUTPUT_FOLDER]

For every JPEG/HEIC/PNG/WebP in PHOTOS_FOLDER it writes, under OUTPUT_FOLDER
(default PHOTOS_FOLDER/cutouts):
    site/NAME.png      transparent, trimmed, 2048 px max: our storefront only
    listing/NAME.jpg   2048x2048 on white, item fills 85%: Etsy, eBay, Shopify
Marketplaces never get the PNG (Etsy renders transparent pixels black). Keep the
untouched original as well: Etsy wants one unedited photo per listing.
Glass (chandelier, stemware, decanter): do not cut; list the original sweep shot.

Each line of the report gives "pixels kept": the share of solid item pixels
identical to the photo. Below 99% means something was altered; check by eye.
Sources: rembg https://github.com/danielgatis/rembg (PyPI 2.0.86, 2026-10-28),
BiRefNet https://github.com/ZhengPeng7/BiRefNet (MIT weights).
"""

import io
import sys
import time
from pathlib import Path

import numpy as np
from PIL import Image, ImageCms, ImageOps
from pillow_heif import register_heif_opener
from rembg import new_session, remove

# Always name the model: rembg's default (bria-rmbg) is licensed non-commercial only.
MODEL = 'birefnet-general'
EXTS = {'.jpg', '.jpeg', '.png', '.webp', '.heic', '.heif'}
WORK_EDGE = 4096  # caps 48 MP phone shots; the model itself runs at 1024
SITE_EDGE = 2048
LISTING = 2048
FILL = 0.85  # Google recommends the item fill 75-90% of the main image
SPECK = 8  # alpha below this is dust, not item


def load(path):
    img = ImageOps.exif_transpose(Image.open(path))  # HEIC is already upright
    icc = img.info.get('icc_profile')
    if icc:  # iPhones shoot Display P3; the web and marketplaces assume sRGB
        img = ImageCms.profileToProfile(
            img.convert('RGB'), ImageCms.ImageCmsProfile(io.BytesIO(icc)),
            ImageCms.createProfile('sRGB'), outputMode='RGB')
    img = img.convert('RGB')
    img.thumbnail((WORK_EDGE, WORK_EDGE), Image.Resampling.LANCZOS)
    return img


def cut(session, photo):
    """Return the RGBA cutout, share of solid pixels unchanged, share of item that is solid."""
    rgba = np.array(remove(photo, session=session, decontaminate=True))
    alpha = rgba[..., 3]
    alpha[alpha < SPECK] = 0
    rgba[alpha == 0, :3] = 0  # no leftover room colour hiding under transparent pixels
    solid = alpha >= 250
    diff = np.abs(rgba[..., :3].astype(int) - np.asarray(photo).astype(int)).max(-1)
    kept = float((diff[solid] <= 3).mean()) if solid.any() else 0.0
    return Image.fromarray(rgba), kept, solid.sum() / max((alpha > 0).sum(), 1)


def listing(item):
    scale = FILL * LISTING / max(item.size)
    item = item.resize((round(item.width * scale), round(item.height * scale)),
                       Image.Resampling.LANCZOS)
    canvas = Image.new('RGB', (LISTING, LISTING), 'white')
    canvas.paste(item, ((LISTING - item.width) // 2, (LISTING - item.height) // 2), item)
    return canvas, scale


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    src = Path(sys.argv[1])
    out = Path(sys.argv[2]) if len(sys.argv) > 2 else src / 'cutouts'
    photos = sorted(p for p in src.iterdir() if p.suffix.lower() in EXTS)
    if not photos:
        sys.exit(f'No photos found in {src}')
    for folder in ('site', 'listing'):
        (out / folder).mkdir(parents=True, exist_ok=True)
    register_heif_opener()
    session = new_session(MODEL)
    for path in photos:
        start = time.time()
        rgba, kept, solid = cut(session, load(path))
        box = rgba.getchannel('A').getbbox()
        if not box:
            print(f'{path.name}: no item found, reshoot on the white sweep')
            continue
        # ponytail: one bbox over everything kept; a stray speck far away widens it. Crop by hand if seen.
        item = rgba.crop(box)
        site = item.copy()
        site.thumbnail((SITE_EDGE, SITE_EDGE), Image.Resampling.LANCZOS)
        site.save(out / 'site' / f'{path.stem}.png', optimize=True)
        jpg, scale = listing(item)
        jpg.save(out / 'listing' / f'{path.stem}.jpg', quality=90)
        notes = []
        if kept < 0.99:
            notes.append('PIXELS CHANGED, check by eye')
        if solid < 0.5:
            notes.append('mostly see-through (glass?), list the original instead')
        if scale > 1.25:
            notes.append('item small in frame, shoot closer')
        print(f'{path.name}: {time.time() - start:.1f}s  pixels kept {kept:.1%}  '
              f'solid {solid:.0%}  {"; ".join(notes) or "OK"}')
    print(f'Done: {out}')


if __name__ == '__main__':
    main()
