"""Turn a batch's listings-copy.md into eBay posting sheets, one per item, plus a status board.

Each sheet says which Seller Hub template and business policies to pick, a category to search for,
the title (with its length), the description with the shop footer appended, the item specifics,
and every blank that still has to be filled before publishing. Nothing here touches eBay.

Usage:
  python -I tools/ebay-ready.py assets/ebay-2026-11-08
Writes <batch>/ready/NN-slug.txt and <batch>/ready/STATUS.md. Safe to rerun.
"""
import re
import sys
from pathlib import Path

batch = Path(sys.argv[1])
repo = Path(__file__).resolve().parent.parent
footer = (repo / 'assets/ebay-shop-kit/listing-footer.txt').read_text(encoding='utf-8').strip()
out = batch / 'ready'
out.mkdir(exist_ok=True)

# Policy names as created on the account, 2026-11-09 (docs/ebay-setup.md).
RET = 'HWV | Returns | 30 days | Buyer pays'
PAY = 'HWV | eBay checkout | Immediate payment'
PARCEL = 'HWV | Parcel | Calculated | 2 business days'
PICKUP = 'HWV | Parcel + pickup | Calculated | 2 business days'
TPL = {'clothing': ('HWV | Clothing | 2 day | 30 day', PARCEL),
       'accessories': ('HWV | Accessories | 2 day | 30 day', PARCEL),
       'decor': ('HWV | Decor | 2 day | 30 day', PICKUP)}

# Item -> (template kind, category to type into eBay's category search). The search phrase is a
# suggestion; eBay's category picker decides the final path.
KIND = {**{n: 'clothing' for n in range(1, 21)}, 45: 'clothing',
        23: 'accessories', 24: 'accessories', 37: 'accessories', 38: 'accessories', 39: 'accessories',
        40: 'accessories', 41: 'accessories'}
CAT = {1: "women's dresses", 2: "women's dresses", 3: "women's dresses", 4: "women's shorts", 5: "women's tops blouses",
       6: "women's dresses", 7: "women's jeans", 8: "women's tops blouses", 10: "women's dresses",
       11: "women's activewear jackets", 12: "women's dresses", 13: "women's tops blouses", 14: "women's dresses",
       15: "women's pants", 16: "men's coats jackets", 17: "women's dresses", 18: "women's jumpsuits",
       19: "men's casual button-down shirts", 20: "women's skirts", 21: 'wall art', 22: 'wall art',
       23: "men's hats", 24: "men's hats", 25: 'artificial flowers garlands', 26: 'art prints',
       27: 'art photographs', 28: 'folk art', 29: 'automobilia photographs', 30: 'automobilia photographs',
       31: 'art prints', 32: 'wall plaques', 33: 'art prints', 34: 'wall art', 35: 'picture frames',
       36: 'art paintings', 37: "women's bags handbags", 38: 'jewelry boxes', 39: 'costume jewelry lots',
       40: "men's casual shoes loafers", 41: "men's dress shoes loafers", 42: 'mugs', 43: 'picture frames',
       44: 'wall plaques', 45: "men's vests"}

# Clothing ballparks live in the workbook's Listings sheet; mirror them here so the sheet is self-contained.
CLOTHING_BALLPARK = {1: '$32 to $48', 2: '$14 to $24', 3: '$65 to $120', 4: '$16 to $28', 5: '$12 to $20'}

text = (batch / 'listings-copy.md').read_text(encoding='utf-8')
sections = {int(m[1]): (m[2].strip(), m[3])
            for m in re.finditer(r'^# (\d+)\. (.+?)\n(.*?)(?=^# |\Z)', text, re.M | re.S)}


def part(body, name):
    m = re.search(rf'^## {name}\n(.*?)(?=^## |\Z)', body, re.M | re.S)
    return m[1].strip() if m else ''


try:
    import openpyxl
    wb = openpyxl.load_workbook(batch / 'fill-in-2026-11-08.xlsx', read_only=True)
    for row in list(wb['Listings'].iter_rows(values_only=True))[1:]:
        if row and isinstance(row[0], int) and row[5]:
            CLOTHING_BALLPARK[row[0]] = str(row[5])
except Exception:
    pass

rows = []
for n, (name, body) in sorted(sections.items()):
    if 'merged into' in (name + body).lower():
        continue
    title = part(body, 'Title')
    desc = part(body, 'Description')
    specs = part(body, 'Item specifics')
    notes = part(body, 'Before you publish')
    kind = KIND.get(n, 'decor')
    template, ship = TPL[kind]
    # Blanket smoke-free claims are not verified (docs/ebay-setup.md): drop them; the checklist asks.
    desc = re.sub(r',\s*smoke-free\.', '.', desc)
    ballpark = re.search(r'Ballpark:\s*([^;.\n]+(?:\.\d+)?[^;\n]*)', notes)
    ballpark = ballpark[1].strip().rstrip('.') if ballpark else CLOTHING_BALLPARK.get(n, 'none written')
    notes = '\n'.join(l for l in notes.splitlines() if not l.lstrip('- ').startswith('Ballpark'))
    blanks = desc.count('____') + specs.count('____')
    brackets = re.findall(r'\[([^\]]+)\]', desc)
    todo_cond = any(b.lower().startswith(('describe', 'note', 'condition')) for b in brackets) or '[describe' in desc
    slug = re.sub(r'[^a-z0-9]+', '-', name.lower()).strip('-')[:48]
    over = len(title) > 80
    sheet = f"""ITEM {n:02d}. {name}
eBay posting sheet. Built by tools/ebay-ready.py from listings-copy.md. Nothing below is on eBay yet.

== PICK IN EBAY ==
Start from template:  {template}
Category (search):    {CAT.get(n, '')}{'   (template defaults to Antiques: change it)' if kind == 'clothing' else ''}
Format:               Buy It Now, quantity 1
Shipping policy:      {ship}
Return policy:        {RET}
Payment policy:       {PAY}
Best Offer:           on if the price is over about $30; auto-decline below your floor
Package:              PACKED weight and box size: ____ lb ____ oz, ____ x ____ x ____ in
Price:                ____   (ballpark {ballpark}, unverified: check eBay Sold first)
Photos:               the Photoroom set in Drive, Holliewood eBay/Items/{n:02d} ...

== TITLE ({len(title)}/80{' TOO LONG' if over else ''}) ==
{title}

== DESCRIPTION (paste as is, after filling the blanks) ==
{desc}

{footer}

== ITEM SPECIFICS (eBay's own fields) ==
{specs}

== BEFORE YOU PUBLISH (delete nothing above; these are for you) ==
- Fill every ____ ({blanks} in the copy) from the tape, plus the package line.
- Replace each [bracket] with what you see in daylight, or delete it.
- Smoke-free was taken out. Add it back only if it is true for this piece.
- Set eBay's Condition field to match the condition line.
{notes}
"""
    (out / f'{n:02d}-{slug}.txt').write_text(sheet, encoding='utf-8')
    rows.append((n, name, kind, CAT.get(n, ''), len(title), blanks, len(brackets), ballpark))

with open(out / 'STATUS.md', 'w', encoding='utf-8') as f:
    f.write('# eBay posting status, batch ' + batch.name.replace('ebay-', '') + '\n\n'
            'One sheet per item in this folder. **Ready to post** means: blanks filled, condition written, price set '
            'from eBay Sold, packed weight entered. None is there yet: every item still needs the tape, a daylight '
            'condition check and a price.\n\n'
            '| # | Item | Template | Category search | Title len | Blanks | [ ] notes | Ballpark (unverified) |\n'
            '|---|---|---|---|---|---|---|---|\n')
    for r in rows:
        f.write(f'| {r[0]} | {r[1]} | {r[2]} | {r[3]} | {r[4]} | {r[5]} | {r[6]} | {r[7]} |\n')
print(f'{len(rows)} sheets in {out}')
for r in rows:
    if r[4] > 80:
        print('TITLE TOO LONG:', r[0], r[4])
