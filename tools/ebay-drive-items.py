"""One Drive folder per eBay item, and a check that every item has one.

Rule (Ricky, 2026-11-08): every item for eBay gets its own folder under
G:\\My Drive\\Holliewood eBay\\Items\\<NN slug>\\ holding its Photoroom photos and a
listing.txt (title, description, item specifics, notes) ready to paste into the eBay app.
A new item is set up when that folder exists with a front photo and the listing text.

Usage:
  python -I tools/ebay-drive-items.py assets/ebay-2026-11-08            # lay out + check
  python -I tools/ebay-drive-items.py assets/ebay-2026-11-08 --check    # report only
  a third argument overrides the Drive Items folder.
Exit 1 if any item is not set up.
"""
import re
import shutil
import sys
from pathlib import Path

args = [a for a in sys.argv[1:] if not a.startswith('--')]
check = '--check' in sys.argv
batch = Path(args[0])
dest = Path(args[1] if len(args) > 1 else r'G:/My Drive/Holliewood eBay/Items')

# Non-clothing items: listing number -> photo slug. Clothes carry their number in the file name.
# 38 and 39 (jewelry box, and the lot inside it) share one photo until the lot is shot on its own.
OTHER = {21: 'art-louvre-dogs', 22: 'canvas-darling-be-daring', 23: 'cap-its-only-sex', 24: 'cap-us-army',
         25: 'flowers-dried', 26: 'frame-banana-figure', 27: 'frame-fashion-photo', 28: 'frame-feather-red',
         29: 'frame-porsche-356', 30: 'frame-porsche-911', 31: 'frame-shisa-lion', 32: 'frame-train-shadowbox',
         33: 'frame-trust-me-dance', 34: 'frame-wagon-wheel', 35: 'frame-wavy-gold-dress', 36: 'gold-ornate-landscape',
         37: 'handbag-dooney-bourke', 38: 'jewelry-case-open', 39: 'jewelry-case-open', 40: 'loafers-navy',
         41: 'loafers-tan', 42: 'mug-pipe-mozone', 43: 'oval-floral', 44: 'plaque-church-ceramic',
         45: 'vest-black-halter', 46: 'wallart-crystal-glass'}
VIEW = re.compile(r'-(front|back|tag|detail|side|sole|flaw)[\w-]*\.jpg$')

# listing sections "# N. Title" up to the next "# "
text = (batch / 'listings-copy.md').read_text(encoding='utf-8')
sections = {int(m[1]): (m[2].strip(), m[3].strip())
            for m in re.finditer(r'^# (\d+)\. (.+?)\n(.*?)(?=^# |\Z)', text, re.M | re.S)}

photos = {}
for p in sorted((batch / 'ebay').glob('*.jpg')):
    photos.setdefault(int(p.name[:2]), []).append(p)
others = sorted((batch / 'other-items').glob('*.jpg'))
for n, slug in OTHER.items():
    photos[n] = [p for p in others if p.name.startswith(slug + '-')]

if not check:
    dest.mkdir(parents=True, exist_ok=True)
    (dest / 'README.txt').write_text(
        'One folder per item: its white-background photos plus listing.txt to paste into the eBay app.\n'
        'Every new item gets a folder here before it is listed. Built by tools/ebay-drive-items.py in the Vintage repo.\n',
        encoding='utf-8')

bad = 0
print(f'{"item":>4}  {"folder":<40} {"photos":>6}  front  copy  status')
for n in sorted(set(sections) | set(photos)):
    pics = photos.get(n, [])
    title, body = sections.get(n, ('', ''))
    if not pics and 'merged into' in (title + body).lower():
        print(f'{n:>4}  {"-":<40} {0:>6}  -      -     merged into another item')
        continue
    slugs = {VIEW.sub('', p.name) for p in pics}
    slug = OTHER.get(n) or (slugs.pop()[3:] if len(slugs) == 1 else '')
    front = any('-front' in p.name for p in pics)
    status = []
    if not pics: status.append('no photos')
    elif not front: status.append('no front photo')
    if not body: status.append('no listing copy')
    if len(slugs) > 1: status.append(f'mixed names {sorted(slugs)}')
    folder = dest / f'{n:02d} {slug or re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")}'
    if not check and (pics or body):
        folder.mkdir(exist_ok=True)
        for p in pics:
            t = folder / p.name
            if not t.exists() or t.stat().st_size != p.stat().st_size:
                shutil.copy2(p, t)
        if body:
            plain = re.sub(r'^## ', '', body, flags=re.M)
            (folder / 'listing.txt').write_text(f'{n}. {title}\n\n{plain}\n', encoding='utf-8')
        # eBay posting sheet from tools/ebay-ready.py: policies, category, footer, blanks to fill.
        for sheet in (batch / 'ready').glob(f'{n:02d}-*.txt'):
            shutil.copy2(sheet, folder / 'ebay-ready.txt')
    ok = not status
    bad += not ok
    print(f'{n:>4}  {folder.name:<40} {len(pics):>6}  {"yes" if front else "no ":<5}  {"yes" if body else "no ":<4}  {"ok" if ok else "; ".join(status)}')
print(f'\n{len(set(sections) | set(photos)) - bad} set up, {bad} not; folders under {dest}')
sys.exit(1 if bad else 0)
