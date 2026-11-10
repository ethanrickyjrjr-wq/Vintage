"""Build eBay draft payloads (title, description HTML, item specifics) from each
clothing item's listing.txt. Estimates in [about ..] are dropped, other bracket
notes become ____ blanks, and the unverified smoke-free claim is removed."""
import html, json, re, sys
from pathlib import Path

ITEMS = Path(r"G:\My Drive\Holliewood eBay\Items")
FOOTER = Path(r"C:\Users\ethan\dev\Vintage\assets\ebay-shop-kit\listing-footer.html")
OUT = Path(__file__).with_name("drafts.json")

TITLES = {  # hand-shortened to eBay's 80-character limit
    "01": "Vintage 90s Liz Claiborne Blue Black Leopard Double Breasted Midi Shirt Dress 8",
    "02": "Future Collective Pink Cream Mixed Floral Lace Trim Tie Strap Slip Midi Dress S",
    "03": "Ronny Kobo Rose Pink Jacquard Plunge V Neck Long Sleeve Ruched Maxi Dress XS",
    "04": "Brooks Brothers Advantage Chino White Flat Front Walking Shorts Women's Size 10",
    "05": "The Limited Kelly Green Button Front Blouse Roll Tab Long Sleeve Chest Pocket S",
    "06": "Vintage 80s Starlo Fashions Red Black Abstract Moire Pleated Blouson Midi Dress",
    "07": "Free People We The Free Light Wash High Rise Wide Leg Jeans Flap Pockets Size 29",
    "08": "Free People Mixed Print Floral Paisley Button Front Blouse Balloon Sleeve Size S",
    "10": "Vintage Lew Magram Black Jersey Faux Wrap Maxi Dress White Satin Collar Cuffs 8",
    "11": "adidas Sample Gray Satin Nylon Full Zip Track Bomber Jacket Ribbed Cuffs S",
    "12": "Vintage 70s Connie Rizza Orange Floral Jersey Lace Up Collar Long Sleeve Dress",
    "13": "Vintage Jones New York Ivory Cream Flap Pocket Button Front Blouse Long Sleeve 8",
    "14": "Ghost London Cream Olive Geometric Plunge V Neck Puff Sleeve Midi Dress XXS",
    "15": "White Coral Sea Print High Waist Slim Straight Trousers Gold Buttons Side Stripe",
    "16": "Denim & Flower Ricky Singh Men's Cream Varsity Bomber Jacket Striped Rib Trim L",
    "17": "Vintage 80s Neiman Marcus Navy 100% Silk Shirt Dress Ivory Collar Cuffs 12",
    "18": "Zara Cream Oatmeal Short Sleeve Utility Boilersuit Jumpsuit Button Front Size S",
    "19": "Columbia PFG Men's Pale Yellow Vented Short Sleeve Fishing Shirt Button Front L",
    "20": "Vintage Bonnie & Norma Paisley Elastic Waist Midi Skirt Rust Teal Gold Size 12",
    "45": "Men's Black Backless Halter Tuxedo Vest Blue Paisley Jacquard Front Adjustable",
}
SPLIT = {"Color", "Features", "Occasion", "Pattern"}  # multi-value aspects; others keep the first part
RENAME = {"Country of Manufacture": "Country of Origin", "Line": "Product Line",
          "Type / Style": "Style"}
SKIP = {"Condition", "Rise", "Inseam"} | set()


def section(text, start, end):
    m = re.search(rf"^{start}\n(.*?)(?=^{end}\n|\Z)", text, re.S | re.M)
    return m.group(1).strip() if m else ""


def clean_line(s):
    s = re.sub(r"\s*\[about[^\]]*\]", "", s)          # photo estimates never ship
    s = re.sub(r"\[[^\]]*\]", "____", s)              # other notes become blanks
    s = s.replace(", smoke-free.", ".").replace(" smoke-free.", "")
    return s


def desc_html(body):
    out, items = [], []
    for raw in body.splitlines():
        line = clean_line(raw.strip())
        if line.startswith("- "):
            items.append(f"<li>{html.escape(line[2:])}</li>")
            continue
        if items:
            out.append("<ul>" + "".join(items) + "</ul>")
            items = []
        if line:
            out.append(f"<p>{html.escape(line)}</p>")
    if items:
        out.append("<ul>" + "".join(items) + "</ul>")
    footer = "\n".join(l for l in FOOTER.read_text(encoding="utf-8").splitlines()
                       if not l.lstrip().startswith("<!--"))
    return '<div style="font-family:Arial,Helvetica,sans-serif;font-size:16px;line-height:1.6;">' \
        + "".join(out) + "</div>" + footer


def attributes(specs, dept):
    a = {}
    for raw in specs.splitlines():
        m = re.match(r"^- ([^:]+):\s*(.*)$", raw.strip())
        if not m:
            continue
        key, val = m.group(1).strip(), m.group(2).strip()
        if key in SKIP or "[" in val or "____" in val or not val:
            continue
        val = re.sub(r"\s*\([^)]*\)", "", val)
        if key == "Size":
            parts = [p.strip() for p in val.split(",")]
            a["Size"] = [parts[0]]
            if len(parts) > 1:
                a["Size Type"] = [parts[1]]
            continue
        if key == "Vintage":
            a["Vintage"] = ["Yes" if val.lower().startswith("yes") else "No"]
            continue
        if key == "Sleeve Length / Type":
            length, _, kind = val.partition(",")
            a["Sleeve Length"] = [length.strip() + " Sleeve"]
            if kind.strip():
                a["Sleeve Type"] = [kind.strip() + " Sleeve"]
            continue
        if key == "Material":
            val = re.sub(r"^100%\s*", "", val)
        key = RENAME.get(key, key)
        vals = [v.strip() for v in val.split(",")]
        if key not in SPLIT:
            vals = vals[:1]
        if key == "Sleeve Length" and "Sleeve" not in vals[0] and vals[0] != "Sleeveless":
            vals = [vals[0] + " Sleeve"]
        a.setdefault(key, [])
        a[key] += [v for v in vals if v and v not in a[key]]
    if "Size" in a and "Size Type" not in a and dept == "Women":
        a["Size Type"] = ["Regular"]
    return a


def build():
    drafts = []
    for d in sorted(ITEMS.iterdir()):
        num = d.name[:2]
        if num not in TITLES:
            continue
        text = (d / "listing.txt").read_text(encoding="utf-8")
        specs = section(text, "Item specifics", "Before you publish")
        dept = (re.search(r"^- Department:\s*(\w+)", specs, re.M) or [None, ""])[1]
        drafts.append({
            "num": num, "folder": d.name, "sku": f"HWV-{num}",
            "title": TITLES[num],
            "description": desc_html(section(text, "Description", "Item specifics")),
            "attributes": attributes(specs, dept),
            "photos": sorted(p.name for p in d.glob("*.jpg")),
        })
    return drafts


if __name__ == "__main__":
    drafts = build()
    for x in drafts:
        assert len(x["title"]) <= 80, (x["num"], len(x["title"]))
        assert "[about" not in x["description"] and "smoke-free" not in x["description"], x["num"]
        assert not any("[" in v or "____" in v for vs in x["attributes"].values() for v in vs), x["num"]
    assert len(drafts) == 20, len(drafts)
    OUT.write_text(json.dumps(drafts, ensure_ascii=False, indent=1), encoding="utf-8")
    for x in drafts:
        print(x["num"], len(x["title"]), len(x["description"]), len(x["photos"]), json.dumps(x["attributes"], ensure_ascii=False))
