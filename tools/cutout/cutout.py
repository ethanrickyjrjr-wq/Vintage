"""Cut real item photos into marketplace JPEGs and site cutouts; mask only, never redrawn.

Setup once, from the repo root (Windows, PowerShell or Git Bash):
    uv venv .venv/cutout --python 3.12
    uv pip install --python .venv/cutout/Scripts/python.exe "rembg[gpu,cli]==2.0.87" "pillow-heif==1.8.1" opencv-python-headless scipy
    (no NVIDIA card, or the GPU check in docs/ebay-photo-studio-handoff.md fails: install "rembg[cpu,cli]==2.0.87" instead)
    .venv/cutout/Scripts/rembg d birefnet-general          # the model, about 1 GB, downloaded once

Run:
    .venv/cutout/Scripts/python.exe tools/cutout/cutout.py PHOTOS_FOLDER [OUTPUT_FOLDER] [options]
    --watch      keep running and process each photo as it lands (iCloud, AirDrop, USB). Stop with
                 Ctrl+C or by creating a file named stop.txt in PHOTOS_FOLDER.
    --shadow     soft contact shadow under the item, for objects standing on a surface (lamps, shoes,
                 hats, bags). --shadow drop gives a faint drop shadow behind a hanging or framed item
                 instead. Leave both off for clothes on a form. The site PNG never has one.
    --rect       fill the outline of frames, mirrors, boxes and books (see below) for every photo.
    --straighten square up a frame, mirror or box shot at a slight angle: the four corners of the
                 outline are found and the item is warped to a true rectangle (real pixels resampled,
                 nothing invented). Rectangle photos only; proportions are estimated from the photo,
                 so compare with the plain output before trusting it on a listing.
    --reframe    for framed art: rebuild the frame from its own bar. The widest bar's colour profile
                 (its median across the bar, measured away from the corners, so glare and the model's
                 nicks drop out) is laid around the mat and picture with mitred corners. The mat and
                 the picture stay exactly as photographed. Implies --straighten. Only for an undamaged
                 frame: a chipped or worn frame must be shown, not rebuilt.
    --model M    rembg model name, default birefnet-general. Never bria-rmbg (non-commercial licence).
    --force      redo photos whose outputs already exist.

The simplest route, and the one to use for anything the model gets wrong: cut the item out ON THE
PHONE (press and hold the item in Photos, Copy Subject, or Files > Quick Actions > Remove Background)
and drop the transparent PNG in the folder. The script sees the transparency, skips the model, and
only does what the phone cannot: pure white, the square, 1600 px, the naming and the manifest. No
model is loaded when every photo in the run is already cut.

The file name decides the treatment. Name photos item-view: A13-front.jpg, A13-back.heic, A13-label.jpg.
    front, back, side, hero, or any other word       cut out, pure white background
    label, tag, flaw, detail, close, closeup, inside,
    measure, stitch, fabric, hem, button, zipper      kept exactly as shot, only resized: buyers must see
                                                      the real thing in close-ups
    frame, framed, art, mirror, painting, poster,
    box, book, sign, tray, record, album              cut out, then the rectangle repair (same as --rect)
    (not print or canvas: a floral print dress and a canvas tote are clothes)

Rectangle repair: a dark frame on a dark wall loses notches to the model. The repair fills the
object's convex hull with the photo's own pixels, so nothing is redrawn. Never for clothes: a
hull would fill between sleeve and body.

Outputs under OUTPUT_FOLDER (default PHOTOS_FOLDER/cutouts):
    ebay/NAME.jpg      1600x1600 on white, item fills 85%: upload this to eBay (the crosslister
                       carries it to Etsy and Shopify)
    listing/NAME.jpg   2048x2048 on white: the archive master, Shopify's preferred square
    site/NAME.png      transparent, trimmed, 2048 px max: our storefront only (Etsy renders
                       transparent pixels black, so marketplaces never get the PNG)
    manifest.csv       one row per photo: mode, model, provider, seconds, pixels kept, warnings
Keep the untouched original as well: Etsy wants one unedited photo per listing.
Glass (chandelier, stemware, decanter): do not cut; list the original sweep shot.

Each report line gives "pixels kept": the share of solid item pixels identical to the photo.
Below 99% means something was altered; check by eye.
Sources: rembg https://github.com/danielgatis/rembg (MIT; PyPI 2.0.87, 2026-11-06),
BiRefNet https://github.com/ZhengPeng7/BiRefNet (MIT weights). Decisions and tests:
docs/ebay-photo-studio.md, research/ebay-photo-studio-2026-11-07/.
"""

import argparse
import csv
import io
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
from PIL import Image, ImageCms, ImageFilter, ImageOps
from pillow_heif import register_heif_opener
from rembg import new_session, remove

# Always name the model: rembg's default (bria-rmbg) is licensed non-commercial only.
DEFAULT_MODEL = 'birefnet-general'
EXTS = {'.jpg', '.jpeg', '.png', '.webp', '.heic', '.heif'}
WORK_EDGE = 4096  # caps 48 MP phone shots; the model itself runs at 1024
SITE_EDGE = 2048
MASTER = 2048  # listing/ square, Shopify's preferred size
EBAY = 1600  # ebay/ square, eBay's recommended size (500 minimum, 12 MB cap)
FILL = 0.85  # Google recommends the item fill 75-90% of the main image
SPECK = 8  # alpha below this is dust, not item
RECT_WORDS = {'frame', 'framed', 'art', 'artwork', 'mirror', 'painting', 'poster',
              'box', 'book', 'sign', 'tray', 'record', 'album'}  # not 'print' or 'canvas': fabrics and totes
KEEP_WORDS = {'label', 'tag', 'flaw', 'detail', 'close', 'closeup', 'inside', 'measure',
              'measurements', 'stitch', 'stitching', 'fabric', 'hem', 'button', 'zipper', 'mark',
              'signature', 'stamp'}
SHADOW_OPACITY = 0.25
MANIFEST_COLS = ['file', 'mode', 'model', 'provider', 'seconds', 'pixels_kept', 'solid', 'rect_filled',
                 'scale', 'notes', 'ebay', 'listing', 'site', 'processed_utc']


def words(path):
    return set(''.join(c if c.isalnum() else ' ' for c in path.stem.lower()).split())


def mode_for(path, rect_all):
    w = words(path)
    if w & KEEP_WORDS:
        return 'keep'
    if already_cut(path):  # the phone did the cutting; frame words do not matter any more
        return 'precut'
    if rect_all or w & RECT_WORDS:
        return 'rect'
    return 'cut'


def load(path, keep_alpha=False):
    img = ImageOps.exif_transpose(Image.open(path))  # HEIC is already upright
    alpha = img.getchannel('A') if keep_alpha and 'A' in img.getbands() else None
    icc = img.info.get('icc_profile')
    if icc:  # iPhones shoot Display P3; the web and marketplaces assume sRGB
        img = ImageCms.profileToProfile(
            img.convert('RGB'), ImageCms.ImageCmsProfile(io.BytesIO(icc)),
            ImageCms.createProfile('sRGB'), outputMode='RGB')
    img = img.convert('RGB')
    if alpha is not None:
        img.putalpha(alpha)
    img.thumbnail((WORK_EDGE, WORK_EDGE), Image.Resampling.LANCZOS)
    return img


def already_cut(path):
    """True for a transparent PNG from the phone (or any editor): real transparency, not just an alpha band."""
    try:
        img = Image.open(path)
    except Exception:  # noqa: BLE001
        return False
    if 'A' not in img.getbands() and not (img.mode == 'P' and 'transparency' in img.info):
        return False
    a = np.asarray(img.convert('RGBA').getchannel('A'))
    clear = (a < SPECK).mean()
    # a frame or box cut on the phone fills its own box, so only the corners are clear: any real
    # transparency counts, as long as the whole image is not empty
    return 0.0 < clear < 0.98


def provider_name():
    """Name the fastest provider onnxruntime offers. On Windows the pip-installed CUDA and cuDNN DLLs
    (onnxruntime-gpu[cuda,cudnn]) are only found after preload_dlls(); rembg itself never calls it."""
    try:
        import onnxruntime as ort
        if hasattr(ort, 'preload_dlls'):
            try:
                ort.preload_dlls()
            except Exception:  # noqa: BLE001
                pass
        avail = ort.get_available_providers()
    except Exception:  # noqa: BLE001
        return 'unknown'
    for p in ('CUDAExecutionProvider', 'DmlExecutionProvider', 'ROCMExecutionProvider'):
        if p in avail:
            return p
    return 'CPUExecutionProvider'


def open_session(model, provider):
    """Ask for the named provider plus CPU, so TensorRT is never attempted and a CPU fallback is explicit.
    The onnxruntime CPU memory arena is switched off: with it on, the second photo in one process grew
    the arena past the memory limit here (measured 2026-11-07: 9.7 GB peak and killed on photo two;
    arena off, 8.1 GB peak and flat across three photos, about 2 s slower each)."""
    import onnxruntime as ort
    opts = ort.SessionOptions()
    opts.enable_cpu_mem_arena = False
    if provider in ('CUDAExecutionProvider', 'ROCMExecutionProvider', 'DmlExecutionProvider'):
        session = new_session(model, sess_opts=opts, providers=[provider, 'CPUExecutionProvider'])
        running = session.inner_session.get_providers()[0] if hasattr(session, 'inner_session') else provider
        if running != provider:
            print(f'WARNING: {provider} was requested but the session runs on {running}; '
                  'see the GPU check in docs/ebay-photo-studio-handoff.md')
        return session, running
    return new_session(model, sess_opts=opts), 'CPUExecutionProvider'


def cut(session, photo, rect=False):
    """Return the RGBA cutout, share of solid pixels unchanged, share of item that is solid, hull share added."""
    rgba = np.array(remove(photo, session=session, decontaminate=True))
    added = 0.0
    if rect:
        rgba, added = rect_repair(rgba, photo)
    alpha = rgba[..., 3]
    alpha[alpha < SPECK] = 0
    rgba[alpha == 0, :3] = 0  # no leftover room colour hiding under transparent pixels
    solid = alpha >= 250
    diff = np.abs(rgba[..., :3].astype(int) - np.asarray(photo).astype(int)).max(-1)
    kept = float((diff[solid] <= 3).mean()) if solid.any() else 0.0
    return Image.fromarray(rgba), kept, solid.sum() / max((alpha > 0).sum(), 1), added


def rect_repair(rgba, photo):
    """Fill the object's convex hull from the photo. Tested 2026-11-07 on a black frame
    on a dark pegboard: BiRefNet dropped a notch of frame, the hull put it back exactly."""
    import cv2
    from scipy import ndimage
    alpha = rgba[..., 3]
    mask = alpha > 127
    if not mask.any():
        return rgba, 0.0
    lab, n = ndimage.label(mask)
    sizes = ndimage.sum(mask, lab, range(1, n + 1))
    main = ndimage.binary_fill_holes(lab == 1 + int(np.argmax(sizes)))
    cnts, _ = cv2.findContours(main.astype(np.uint8), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    hull = np.zeros(main.shape, np.uint8)
    cv2.fillConvexPoly(hull, cv2.convexHull(max(cnts, key=cv2.contourArea)), 1)
    hull = hull.astype(bool)
    # Everything inside the outline is the object. Make it fully solid from the photo, soft alpha
    # included: a half-transparent band around a notch bleeds white and leaves a scar otherwise.
    # Only the outermost 3 px keep the model's soft edge.
    edge = max(3, int(0.002 * max(main.shape)))
    inner = cv2.erode(hull.astype(np.uint8), np.ones((2 * edge + 1, 2 * edge + 1), np.uint8)).astype(bool)
    missing = hull & (alpha < 128)  # background the model missed inside the outline
    fix = inner & (alpha < 255)
    rgba = rgba.copy()
    rgba[fix, :3] = np.asarray(photo)[fix]  # the real pixels, straight from the photo, never redrawn
    rgba[fix, 3] = 255
    return rgba, float(missing.sum()) / max(hull.sum(), 1)


def straighten(rgba):
    """Perspective-correct a convex four-cornered object to a true rectangle. Returns (rgba, done)."""
    import cv2
    alpha = rgba[..., 3]
    cnts, _ = cv2.findContours((alpha > 127).astype(np.uint8), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if not cnts:
        return rgba, False
    hull = cv2.convexHull(max(cnts, key=cv2.contourArea))
    peri = cv2.arcLength(hull, True)
    quad = None
    for eps in (0.01, 0.02, 0.03, 0.05):
        ap = cv2.approxPolyDP(hull, eps * peri, True)
        if len(ap) == 4:
            quad = ap.reshape(4, 2).astype(np.float32)
            break
    if quad is None:
        return rgba, False
    sums, diffs = quad.sum(1), np.diff(quad, axis=1).ravel()
    tl, br, tr, bl = quad[np.argmin(sums)], quad[np.argmax(sums)], quad[np.argmin(diffs)], quad[np.argmax(diffs)]
    w = int(round(max(np.linalg.norm(tr - tl), np.linalg.norm(br - bl))))
    h = int(round(max(np.linalg.norm(bl - tl), np.linalg.norm(br - tr))))
    if w < 50 or h < 50:
        return rgba, False
    src = np.array([tl, tr, br, bl], np.float32)
    dst = np.array([[0, 0], [w - 1, 0], [w - 1, h - 1], [0, h - 1]], np.float32)
    out = cv2.warpPerspective(rgba, cv2.getPerspectiveTransform(src, dst), (w, h),
                              flags=cv2.INTER_LANCZOS4, borderMode=cv2.BORDER_CONSTANT, borderValue=(0, 0, 0, 0))
    return out, True


def reframe(rgba):
    """Rebuild a picture frame from its own bar around the untouched mat and picture.
    Expects a straightened frame. Returns (rgb_image, done)."""
    from PIL import ImageDraw
    W, H = rgba.size
    arr = np.array(rgba)
    lum = np.array(rgba.convert('L')).astype(int)
    alpha = arr[..., 3]

    def first_light(line, a):
        idx = np.where((line > 110) & (a > 200))[0]
        return int(idx[0]) if len(idx) else None

    rows = range(int(H * 0.25), int(H * 0.75))
    cols = range(int(W * 0.25), int(W * 0.75))
    seen = {}
    for name, vals in (
        ('left', (first_light(lum[y], alpha[y]) for y in rows)),
        ('right', (first_light(lum[y][::-1], alpha[y][::-1]) for y in rows)),
        ('top', (first_light(lum[:, x], alpha[:, x]) for x in cols)),
        ('bottom', (first_light(lum[:, x][::-1], alpha[:, x][::-1]) for x in cols)),
    ):
        vals = [v for v in vals if v is not None]
        if not vals:
            return None, False
        seen[name] = int(np.median(vals))
    w = max(seen.values())  # the bar seen most face-on
    if w < 8 or w > min(W, H) * 0.25:
        return None, False
    pad = int(1.5 * w)
    if w == seen['left']:
        patch = arr[pad:H - pad, 0:w, :3]
    elif w == seen['right']:
        patch = arr[pad:H - pad, W - w:W, :3][:, ::-1]
    elif w == seen['top']:
        patch = np.transpose(arr[0:w, pad:W - pad, :3], (1, 0, 2))
    else:
        patch = np.transpose(arr[H - w:H, pad:W - pad, :3], (1, 0, 2))[:, ::-1]
    profile = np.median(patch, axis=0).astype(np.uint8)  # outer edge to inner edge
    inner = rgba.crop((seen['left'] + 1, seen['top'] + 1, W - seen['right'] - 1, H - seen['bottom'] - 1)).convert('RGB')
    iw, ih = inner.size
    NW, NH = iw + 2 * w, ih + 2 * w
    out = Image.new('RGB', (NW, NH), 'white')
    out.paste(inner, (w, w))
    bar_v = Image.fromarray(np.tile(profile[None, :, :], (NH, 1, 1)))
    bar_h = Image.fromarray(np.tile(profile[:, None, :], (1, NW, 1)))
    pieces = (
        (bar_h, (0, 0), [(0, 0), (NW, 0), (NW - w, w), (w, w)]),
        (bar_h.transpose(Image.FLIP_TOP_BOTTOM), (0, NH - w), [(0, NH), (NW, NH), (NW - w, NH - w), (w, NH - w)]),
        (bar_v, (0, 0), [(0, 0), (w, w), (w, NH - w), (0, NH)]),
        (bar_v.transpose(Image.FLIP_LEFT_RIGHT), (NW - w, 0), [(NW, 0), (NW - w, w), (NW - w, NH - w), (NW, NH)]),
    )
    for img, pos, poly in pieces:
        layer = Image.new('RGB', (NW, NH))
        layer.paste(img, pos)
        mask = Image.new('L', (NW, NH), 0)
        ImageDraw.Draw(mask).polygon(poly, fill=255)
        out.paste(layer, (0, 0), mask)
    return out, True


def square_on_white(item, size, shadow=None):
    """Centre the RGBA item on a white size x size canvas at FILL. shadow: None, 'contact' or 'drop'."""
    scale = FILL * size / max(item.size)
    item = item.resize((round(item.width * scale), round(item.height * scale)), Image.Resampling.LANCZOS)
    canvas = Image.new('RGB', (size, size), 'white')
    x, y = (size - item.width) // 2, (size - item.height) // 2
    layer = None
    if shadow == 'contact':
        # the item's own footprint, squashed to a sliver, centred on the bottom edge, blurred, 25% black
        sh = max(8, int(item.height * 0.12))
        foot = item.getchannel('A').resize((item.width, sh), Image.Resampling.LANCZOS)
        layer = Image.new('L', (size, size), 0)
        layer.paste(foot, (x, y + item.height - sh // 2))
        layer = layer.filter(ImageFilter.GaussianBlur(max(4, int(item.height * 0.025))))
    elif shadow == 'drop':
        # the whole silhouette, blurred and nudged down and right (whitebg's recipe, MIT), 20% black
        dx, dy = round(size * 0.009), round(size * 0.015)
        layer = Image.new('L', (size, size), 0)
        layer.paste(item.getchannel('A'), (x + dx, y + dy))
        layer = layer.filter(ImageFilter.GaussianBlur(max(1.0, size * 0.02)))
    if layer is not None:
        opacity = SHADOW_OPACITY if shadow == 'contact' else 0.20
        layer = layer.point(lambda v: int(v * opacity))
        canvas.paste(Image.new('RGB', (size, size), 'black'), (0, 0), layer)
    canvas.paste(item, (x, y), item)
    return canvas, scale


def fit(photo, edge):
    """Keep mode: the photo as shot, long side at most edge."""
    out = photo.copy()
    out.thumbnail((edge, edge), Image.Resampling.LANCZOS)
    return out


def done_before(out, path):
    return (out / 'ebay' / f'{path.stem}.jpg').exists()


def append_manifest(out, row):
    path = out / 'manifest.csv'
    new = not path.exists()
    with path.open('a', newline='', encoding='utf-8') as fh:
        w = csv.DictWriter(fh, fieldnames=MANIFEST_COLS)
        if new:
            w.writeheader()
        w.writerow(row)


def process(path, out, get_session, args, provider):
    start = time.time()
    mode = mode_for(path, args.rect)
    photo = load(path, keep_alpha=(mode == 'precut'))
    row = dict.fromkeys(MANIFEST_COLS, '')
    row.update(file=path.name, mode=mode, model=args.model if mode in ('cut', 'rect') else '',
               provider=provider if mode in ('cut', 'rect') else '',
               processed_utc=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'))
    notes = []
    if mode == 'keep':
        fit(photo, EBAY).save(out / 'ebay' / f'{path.stem}.jpg', quality=90)
        fit(photo, MASTER).save(out / 'listing' / f'{path.stem}.jpg', quality=90)
        row.update(ebay=f'ebay/{path.stem}.jpg', listing=f'listing/{path.stem}.jpg',
                   notes='kept as shot', seconds=f'{time.time() - start:.1f}')
        append_manifest(out, row)
        print(f'{path.name}: {time.time() - start:.1f}s  kept as shot (close-up), resized only')
        return
    if mode == 'precut':
        rgba = photo
        a = np.asarray(rgba.getchannel('A'))
        kept, solid, added = 1.0, float((a >= 250).sum()) / max((a > SPECK).sum(), 1), 0.0
        notes.append('cut on the phone, framed here')
    else:
        rgba, kept, solid, added = cut(get_session(), photo, rect=(mode == 'rect'))
    box = rgba.getchannel('A').getbbox()
    if not box:
        print(f'{path.name}: no item found, reshoot on the white sweep')
        row.update(notes='no item found', seconds=f'{time.time() - start:.1f}')
        append_manifest(out, row)
        return
    # one bbox over everything kept; a stray speck far away widens it. Crop by hand if seen.
    item = rgba.crop(box)
    if mode == 'rect' and (args.straighten or args.reframe):
        arr, done = straighten(np.array(item))
        if done:
            item = Image.fromarray(arr)
            notes.append('straightened')
            if args.reframe:
                rebuilt, ok = reframe(item)
                if ok:
                    item = rebuilt.convert('RGBA')
                    notes.append('frame rebuilt from its own bar')
                else:
                    notes.append('not reframed (frame bars not found)')
        else:
            notes.append('not straightened (no four corners found)')
    site = item.copy()
    site.thumbnail((SITE_EDGE, SITE_EDGE), Image.Resampling.LANCZOS)
    site.save(out / 'site' / f'{path.stem}.png', optimize=True)
    master, scale = square_on_white(item, MASTER, args.shadow)
    master.save(out / 'listing' / f'{path.stem}.jpg', quality=90)
    ebay, _ = square_on_white(item, EBAY, args.shadow)
    ebay.save(out / 'ebay' / f'{path.stem}.jpg', quality=90)
    if kept < 0.99 and mode != 'precut':
        notes.append('PIXELS CHANGED, check by eye')
    if solid < 0.5:
        notes.append('mostly see-through (glass?), list the original instead')
    if scale > 1.25:
        notes.append('item small in frame, shoot closer')
    if mode == 'rect':
        notes.append(f'rect repair filled {added:.1%}')
    if args.shadow:
        notes.append(f'{args.shadow} shadow')
    secs = time.time() - start
    row.update(seconds=f'{secs:.1f}', pixels_kept=f'{kept:.4f}', solid=f'{solid:.3f}',
               rect_filled=f'{added:.4f}' if mode == 'rect' else '', scale=f'{scale:.3f}',
               notes='; '.join(notes), ebay=f'ebay/{path.stem}.jpg', listing=f'listing/{path.stem}.jpg',
               site=f'site/{path.stem}.png')
    append_manifest(out, row)
    print(f'{path.name}: {secs:.1f}s  pixels kept {kept:.1%}  solid {solid:.0%}  {"; ".join(notes) or "OK"}')


def photos_in(src):
    return sorted(p for p in src.iterdir()
                  if p.suffix.lower() in EXTS and not p.name.startswith('.') and p.is_file())


def stable(path, seen):
    """True once the file size has held still across two polls (a copy that has finished)."""
    try:
        size = path.stat().st_size
    except OSError:
        return False
    last = seen.get(path)
    seen[path] = size
    return last is not None and last == size and size > 0


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('src', type=Path)
    ap.add_argument('out', type=Path, nargs='?')
    ap.add_argument('--watch', action='store_true')
    ap.add_argument('--shadow', nargs='?', const='contact', choices=['contact', 'drop'], default=None)
    ap.add_argument('--rect', action='store_true')
    ap.add_argument('--straighten', action='store_true')
    ap.add_argument('--reframe', action='store_true')
    ap.add_argument('--model', default=DEFAULT_MODEL)
    ap.add_argument('--force', action='store_true')
    args = ap.parse_args()
    if args.model.startswith('bria'):
        sys.exit('bria-rmbg weights are licensed for non-commercial use only; pick a birefnet model')
    src = args.src
    out = args.out or src / 'cutouts'
    if not args.watch and not photos_in(src):
        sys.exit(f'No photos found in {src}')
    for folder in ('site', 'listing', 'ebay'):
        (out / folder).mkdir(parents=True, exist_ok=True)
    register_heif_opener()
    state = {'session': None, 'provider': provider_name()}

    def get_session():  # the model loads only when a photo actually needs cutting
        if state['session'] is None:
            state['session'], state['provider'] = open_session(args.model, state['provider'])
            p = state['provider']
            print(f'model {args.model} on {p}' + ('' if p != 'CPUExecutionProvider' else
                  ' (CPU: about 20 s per photo; the GPU install is in docs/ebay-photo-studio-handoff.md)'))
        return state['session']

    def run(path):
        if done_before(out, path) and not args.force:
            print(f'{path.name}: done before, skipped (use --force to redo)')
            return
        try:
            process(path, out, get_session, args, state['provider'])
        except Exception as exc:  # noqa: BLE001
            print(f'{path.name}: FAILED {exc}')

    for path in photos_in(src):
        run(path)
    if not args.watch:
        print(f'Done: {out}')
        return
    print(f'Watching {src} (create stop.txt there or press Ctrl+C to stop)')
    seen, handled = {}, set(photos_in(src))
    try:
        while not (src / 'stop.txt').exists():
            for path in photos_in(src):
                if path in handled:
                    continue
                if stable(path, seen):
                    run(path)
                    handled.add(path)
            time.sleep(2)
    except KeyboardInterrupt:
        pass
    print(f'Stopped: {out}')


if __name__ == '__main__':
    main()
