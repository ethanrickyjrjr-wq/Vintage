# Cut-out product grids for a one-of-one vintage catalog (research, 2026-10-27)

Tags: **[V]** = read this session (URL plus the exact class, attribute, line or pixel check). **[U]** = memory, inference or heuristic. **[N/O]** = not observable in the markup I got.
Markdown extraction shows no rendered spacing or colour. `crawl4ai --help` has no screenshot flag; `-o all` returns the full page HTML as JSON, and that is what I read [V]. Raw HTML for each shop is in `research/cutouts/raw/03-*.html` (grep-able).

## Bottom line

1. Only Rething (vintage lighting, closest match) ships true transparent PNG cut-outs in its grid: 10 of 10 first images have transparent regions [V]. Layout: 4 columns desktop, 2 on phones, 4:5 frame, a photo revealed on hover, a "Sold out" badge kept in the grid.
2. DWR keeps transparent PNG masters and flattens them to a #f8f8f8 square at the CDN (`trim=auto`, `pad=40`) [V]. Most others (SSENSE, Areaware, WGACA, Georges, Sunbeam) are flattened studio shots in fixed frames. File extension proves nothing: Sunbeam serves `.png` files that have no alpha channel [V].
3. Six of the seven grids that exposed a phone layout use 2 columns (Rething, Georges, Sunbeam, Lost & Loved, DWR, SSENSE) [V]; Areaware's classes imply 1 (my reading, [U]). Baymard and NN/g pages fetched give no mobile column number: not found in sources fetched this session.
4. NN/g (2022): consistency of "background, orientation, context, lighting, scale" makes a grid "easily scannable and comparable". Baymard: cut-out-only images make size hard to judge (42% of users try); give 3+ thumbnails per item. So cutouts are right only with a size line and a second honest photo.
5. For one-of-one stock, sold pieces stay visible with a text badge (Rething, Georges, Lost & Loved) or move to a "Recently Sold / Past Treasures" collection (Lost & Loved). Chairish offers a "Hide Sold Out" filter [V].
6. Our site has two page colours (cream #f6efdf in `storefront.css`, burgundy #422831 in `atmosphere.css`) [V]. Only alpha cut-outs sit correctly on both; flat grey-studio JPGs would show as pale rectangles on burgundy.
7. Recommendation: pilot "Shelf rows on the page colour": bottom-aligned alpha cutouts, a hand-set scale knob, contact shadow, a ledge line per row, dimension line plus a SOLD/second-photo state. 4 columns by 3 rows desktop, 2 on phones.
8. Readiness: of your 12 test items only 4 have a "ready" chip (A1, A2, B6, B7). A11 and A12 are not in `catalog-data.js` at all. See section 6.

## 1. Live shops (collection pages, fetched 2026-10-27)

Sample sizes: Rething 10 images; every other image/transparency claim is 1 image unless stated.

| Shop | Cols desktop to phone | Frame | Image type | Tile bg | Caption on card | Sold state | 2nd image |
|---|---|---|---|---|---|---|---|
| Rething /collections/lighting | 4 to 2 | 4:5 | PNG alpha 10/10; 2nd is a JPG photo | N/O | title, price | "Sold out" badge bottom-left, stays in grid | hover swap, `alt=""` |
| DWR /lighting-table-lamps | 3 to 2 | 1:1 | master PNG alpha; tile flattened JPEG | #f8f8f8 | brand, name, price | N/O | `data-rolloverimg` |
| SSENSE /women/bags | 4 (xl), 3 (sm), 5 (xxxl) to 2 | 2:3 | JPG padded white, bottom-anchored | white | brand, name, price | N/O | N/O |
| Areaware /collections/all-products | 4 (lg), 1 on phone [inferred] | 1:1 | "Silo" JPG, #f7f7f7 | tile bg class only | title, price, variant dots | N/O | hover swap to `Silo-03` |
| Chairish /collection/table-lamps | N/O | 1:1 fit | dealer photos (alpha not checked) | N/O | title, price, W x D x L, "In 1 cart" | "Hide Sold Out" filter | N/O |
| What Goes Around /en-us/bags | N/O (AJAX) | 2:3 | white JPG/WebP, corners 255 | white | brand, name, price | N/O | hover swap |
| Gantri /shop/table-lights | N/O | 1:1 | tinted photos, not cutouts | warm photo | name, "$248, 9.5" tall" | N/O | N/O |
| Sunbeam /collections/bar-accessories | 4 to 2 | ~3:4 | photos in `.png`, no alpha | N/O | title, vendor, price, "ONE OF A KIND" chip | none among 32 cards | N/O |
| Georges /collections/archive | 4 to 2 | 3:4 | photos | #eae7e1 | title with size, price | black "SOLD" chip, price kept | zoom only |
| Lost & Loved /collections/recently-sold | 3 to 2 | 3:4 | photos | N/O | title, price | `grid-view-item--sold-out` | N/O |

### Evidence per shop (exact markup)

**Rething** (https://www.rething.uk/collections/lighting) [V]
- Grid: `<ul id="product-grid" class="grid product-grid grid--2-col-tablet-down grid--4-col-desktop">`; `--grid-desktop-vertical-spacing: 40px`.
- Frame: `<div class="card__inner color-scheme-1 gradient ratio" style="--ratio-percent: 125.0%">` (= 4:5). First `<img>` `width="237" height="296"`, `sizes="(min-width: 1200px) 267px, (min-width: 990px) calc((100vw - 130px) / 4), (min-width: 750px) calc((100vw - 120px) / 3), calc((100vw - 35px) / 2)"`.
- X verified, Y needs review: the class says 2 columns "tablet down", but `sizes` implies 3 columns at 750-989px.
- Cut-out proof: downloaded 10 served PNGs (`IMG_1595.png` etc., 533x666): all RGBA, subject bounding box 19-65% of canvas width, 38-60% of height (alpha > 16), corner pixel (0,0,0,0). The second `<img>` is a JPEG photograph (`photo_2025-03-06_15.02.07.jpg`, corner (60,114,152)). So: cut-out PNG first, in-room photo second.
- Centring, not baseline: top gap roughly equals bottom gap in most files (26.7/26.7, 21.9/21.9, 30.9/30.9); bottom gap ranges 19-31%. Scale varies (subject height 38-60%). Observation, not a stated rule.
- Wrapper `<div class="media media--transparent media--hover-effect">`; the hover CSS was not captured [N/O]. Second image `alt=""`; first image `alt="Habitat Fitz Glass Table Lamp – Mid-Century, White"`.
- Sold: `<span class="badge badge--bottom-left color-scheme-3">Sold out</span>` inside `card__badge bottom left`.
- Maker and era live in titles, e.g. alt "Vintage Mid-Century Modern Raak Fuga Table Lamp – 1960s Design by Maija Liisa Komulainen". Product page: "Condition: Excellent / Material: Glass / Dimensions: Height: 27 cm / Diameter: 10 cm (approx.)" (https://www.rething.uk/products/habitat-fitz-glass-table-lamp-mid-century-white).

**DWR** (https://www.dwr.com/lighting-table-lamps) [V]
- Grid: `row product-grid product-row product-row-3up no-gutters`, cells `col-6 col-sm-4` (2 phone, 3 from sm). Frame `product-image-wrapper ratio ratio-1x1 has-hover-img`.
- Tile URL: `...DWR_2530654_100599751_burugundy_f.png?trim=auto&trim-sd=2&blend-mode=darken&blend=f8f8f8&bg=f8f8f8&auto=format&fit=fill&w=400&h=400&pad=40`. Fetched: JPEG 400x400, corners (248,248,248). The same file without params: PNG 400x400, 96% fully transparent, corner alpha 0.
- Meaning (imgix-style parameters, semantics [U]; the two fetched files confirm the result): transparent master, auto-trimmed, padded 40px on 400 (10% per side), flattened onto #f8f8f8. Each item is scaled to fill the square, so real relative size is lost.
- Hover: `data-rolloverimg="...W-DWR_2530654_100214445_opal_v1_001.png?..."` (a lifestyle shot). Caption: `brand-label` (Louis Poulsen), name link, price range. Data layer has `"in_stock":false` on one item; visual sold state N/O.

**SSENSE** (https://www.ssense.com/en-us/women/bags) [V]
- Grid: `grid grid-cols-2 xxxl:grid-cols-5 gap-x-2 gap-y-4 sm:grid-cols-3 lg:gap-y-[20px] xl:grid-cols-4`.
- Tile: `<div class="relative mb-[10px] aspect-[2/3]"><img class="mb-[10px] object-contain object-bottom" ... src="https://img.ssensemedia.com/image/upload/b_white,c_lpad,g_south,ar_2:3/f_auto,c_limit,w_1920,q_85/262421F046000_1.jpg">`. Fetched at w_600: JPEG 600x900, corners (255,255,255). So items are anchored to the bottom edge of an identical white 2:3 frame. (The meaning of the `c_lpad,g_south` tokens is a Cloudinary-style reading [U]; `object-bottom` is in the markup [V].)
- Caption: brand in caps 11px, name 11px, price. JSON-LD `"availability":"https://schema.org/InStock"`.

**Areaware** (https://www.areaware.com/collections/all-products) [V]
- `<ul class="collection-list grid grid-cols-2 lg:grid-cols-12 gap-gutter bg-border">`, cells `col-span-2 lg:col-span-3` (4 per row at lg; 1 per row on phone is my reading of Tailwind classes [U]). Hairline lines come from `bg-border` showing through `gap-gutter`.
- Image: `padding-top:100%` wrapper, `object-contain`, file `KYCBSRO-CacheBox-Small-RedOrange-025FA-Silo-01.jpg`; fetched JPEG 540x540, corners (247,247,247). Hover: `.product-item-hover ... group-hover:opacity-100 ... bg-contain` with `...Silo-03...` (a different angle).
- Caption: title, price, variant dots; designer name only in analytics JSON.

**Chairish** (https://www.chairish.com/collection/table-lamps) [V]
- Image URL `...?aspect=fit&width=320&height=320` (fit inside a square, i.e. letterboxed [U]). `<img alt="Balloon Lamp by Yves Christin for Bilumen, 1970s For Sale">`.
- Card text: `<strong class="product-attr-value">11.02ʺW × 10.24ʺD × 14.17ʺL</strong>`, `urgency-badge-value` "In 1 cart", title with maker and era, price. Data: `"quantity": 1`, `"is_on_hold": false`, `"product_state_display": "Listed for Purchase"` (48 of 48). Filter facet `"label": "Hide Sold Out"` (`misc_availability`, value `HS`).
- Product page fields: Dimensions, Period, Condition, "Condition Notes: Very Good — This vintage item has no defects, but it may show slight traces of use."

**WGACA** (https://www.whatgoesaroundnyc.com/en-us/bags) [V for tile; grid N/O]
- Grid tiles are injected by AJAX (`<!-- Tile HTML injected via JS -->`). I fetched one tile (`.../Tile-Show?pid=Q9BIYX3PKB004...`): `width="400" height="600"`, container `image-container show-secondary-image`, a second `<img class="tile-image product-tile-image-secondary">`. Fetched primary: 400x600, corners (255,255,255).
- Caption: `<span class="brand">Christian Dior</span> <span class="name">Black Calfskin Saddle Bag NM</span>` plus price. Condition is only in the data layer: `"item_condition":"Excellent"`, `"quantity":1`, `"stock_status":"In Stock"` (not on the card).

**Gantri** (https://gantri.com/shop/table-lights) [V]: `data-aspect-ratio="1:1"`, image `ar_1:1,c_lfill,h_400,w_400`, 800x800 WebP, corners (200,192,181) and (179,170,155) (warm photo backdrop, not a cutout). Caption "Cantilever Table Light" then "$248, 9.5″ tall" (height in the caption). A view toggle `aria-label="Single column view"` exists; column CSS is CSS-in-JS [N/O].

**Sunbeam** (https://sunbeamvintage.com/collections/bar-accessories) [V]
- `<ul class="grid grid--uniform grid--view-items">`, cells `grid__item--collection-template small--one-half medium-up--one-quarter`. Image `width="896" height="1200"`, `data-aspectratio="0.7466..."`, wrapper `padding-top:133.9%`.
- X verified, Y needs review: file `Sunbeam_Vintage_10.14.26-143a_...png` suggests a cutout, but pixels are RGB with no alpha (corner (112,96,75)); it is a photo.
- Chip: inline-styled white box `ONE OF A KIND` on 30 of 32 cards. Caption: title (aria-hidden), vendor "Vintage", price. Link has `<span class="visually-hidden">` with the product title.

**Georges Vintage** (https://georgesvintage.com/collections/archive) [V]
- CSS in page: `.gvc-grid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:36px 14px}`, mobile `repeat(2,minmax(0,1fr));gap:26px 9px`; `.gvc-media{background:#eae7e1;aspect-ratio:3/4}`; `.gvc-media img{object-fit:cover}`; `.gvc-card:hover img{transform:scale(1.035)}`; `sizes="(max-width: 749px) 50vw, 25vw"`.
- `.gvc-sold{position:absolute;top:10px;left:10px;background:#202020;color:white;...}` with text `SOLD`; price still shown. `.gvc-card:focus-visible{outline:2px solid #202020;outline-offset:3px}`; `.gvc-toolbar label{min-height:44px}`.
- Header: "Each item is a genuine one-of-one piece, handpicked and individually graded for condition." Note "Archive" here means a higher-end tier, not sold items.

**Lost & Loved** (https://lostandloved.co.uk/collections/recently-sold) [V]
- `<title>Recently Sold – Lost and loved`; 24 cards with `grid-view-item grid-view-item--sold-out`, cells `small--one-half medium-up--one-third`, `data-aspectratio="0.75"`. Price slot shows `Sold out` and the original price (£15.00) in the sale slot. The homepage links the same collection as "Past Treasures" (`research/lostandloved-home-20261026-luna5.md`).
- Visible `<img>` has `alt=""`; the real text is only in `<noscript>` and in a `visually-hidden` span inside the link.

### Dropped (and why)
- 1stDibs: challenge page (`embedded-challenge-page`). Mr Porter: 403 Access Denied. Anthropologie: 403 bot page. The RealReal: PerimeterX captcha. Muuto: 302 with 39 bytes.
- HAY (https://www.hay.com/products/lighting/table): grid is a client-side template (`<img src="{{result.ImageUrl}}" alt="{{result.Name}}">`) [N/O]. Our Place: only nav images in static HTML.
- Kaufmann Mercantile: the domain now serves an online-casino page ("Online Casinos Real Money", "Responsible Gambling"). Not a shop; do not cite.
- Per-category tinted tiles: not found on any fetched shop (uniform tile colour only). That idea is ours, [U].

## 2. Does a consistent image style matter? (quotes)

NN/g, "6 Tips for Product Photos on Listing Pages", Kate Moran, February 27, 2022 (https://www.nngroup.com/articles/product-photos-listing-pages/) [V]:
- "Especially for small inventories, sites should have consistent images for all products shown on routing pages. This does not mean that all images need to be identical, but they should be consistent in terms of style. When images are consistent, they are easily scannable and comparable."
- Factors listed: "Background (e.g., white, outdoors, studio) / Orientation and direction / Context / Lighting / Scale (e.g., closeup, full length)".
- "Consistent photos don't have to be identical or boring — they just have to feel like they're all in the same style."
- Stuart Weitzman example, participant: "When I look at heels on this site, I can immediately tell the heel height."
- On hover alternates: "slightly delay the animation" to avoid flicker. Alternate views by "click, hover, or swipe".

NN/g, "UX Guidelines for Ecommerce Homepages, Category Pages, and Product Listing Pages", August 12, 2018 (https://www.nngroup.com/articles/ecommerce-homepages-listing-pages/) [V]: minimum differentiating info includes "Photos large enough to identify a known item and show differences between items"; extras include "Alternate product images available via hover or by clicking through a carousel".

Baymard, "Product Listing Page (PLP) UX", Carl MacDonald, Aug 20, 2026 (https://baymard.com/blog/product-listing-page-plp-ux) [V]:
- "For many product types (particularly apparel, furniture, and home decor), the thumbnail is a primary tool users rely on to decide whether to explore or ignore an item. If a visual is missing, misleading, or lacks sufficient information, users frequently overlook suitable products."
- "grid view for visually driven products, list view for spec-heavy products". "Consistent image thumbnails provide a view of the product at a glance" (a bullet under a Newegg example, not a measured percentage).

Baymard, "Always Provide 3 or More Product Thumbnails...", Published Nov 5, 2024 (https://baymard.com/research-articles/secondary-hover-information) and 2025 benchmark (https://baymard.com/research-articles/current-state-product-list-and-filtering, "80% Don't") [V]:
- "1 additional thumbnail won't be enough for most users — 2 additional thumbnails should be considered a minimum, while 3+ will provide users with even more information."
- Lists "Cut Out", "In Scale", "Feature Callout" and "Lifestyle" image types. Raymour & Flanigan participant "was only able to see the couches in the product list as 'Cut Out' thumbnails, even though she liked to see 'Lifestyle' images in the product list too". At Lamps Plus: "Once she found a 'Feature Callout' image in the product page image gallery, she realized the texture of the shade didn't meet her expectations".

Baymard, "All Products Need at Least One 'In Scale' Image", Published May 30, 2017 (https://baymard.com/blog/in-scale-product-images) [V]:
- "When only traditional 'Cut Out' images — just showing the product on a white background — are offered, users have a very difficult time getting an accurate impression of the product's overall size."
- "42% of users will attempt to gauge the overall scale and size of a product from its product images."

Baymard, "2 Key Design Principles for Product Listing Information" (https://baymard.com/research-articles/list-item-design-ecommerce) [V]: "it's critical to make sure the same attributes are included consistently across similar list items in the same product list" (64% of sites fail). This applies to caption fields: show the same fields on every tile.

Not found: any mobile column count from Baymard or NN/g in the pages fetched. Two Baymard `/guidelines/` pages returned the same 20,317-byte gated shell and are not evidence. Markup convergence above (2 columns on phones in 6 of 7 shops that expose it) is the only data I have.

## 3. One-of-one specifics

**Sold items in the grid**
| Treatment | Shop | Evidence |
|---|---|---|
| Stay, text badge, price kept | Georges | `.gvc-sold` "SOLD" chip top-left |
| Stay, badge bottom-left | Rething | `badge badge--bottom-left` "Sold out" |
| Dedicated archive collection | Lost & Loved | "Past Treasures" (`/collections/recently-sold`), 24 cards `--sold-out`, "Sold out" plus original price |
| User filter | Chairish | facet "Hide Sold Out" |
| Not shown / N/O | Sunbeam | none among 32 cards; sold-out CSS exists |
Greyed-out-only treatments: none found, and they would fail colour-only signalling [U]. Every shop that marks sold uses text.

**Caption fields observed**: maker and era go in the title (Chairish "Balloon Lamp by Yves Christin for Bilumen, 1970s"; Rething alt "...1960s Design by Maija Liisa Komulainen"). Size in the title (Georges "– Size 50 (L)"). Dimensions on the card: Chairish `W × D × L`, Gantri "9.5″ tall". Condition lives on the product page (Rething "Condition: Excellent", Chairish "Condition Notes") or in the data layer (WGACA "Excellent"), not on the card, so the card needs only maker/era in the title plus one size line.

**Keeping cutouts honest**
- Vestiaire seller guide (https://faq.vestiairecollective.com/hc/en-us/articles/209239625-Seller-Creating-the-Perfect-Listing) [V]: "Include a minimum of 2 well-lit, quality photographs taken against a plain background. Take clear photographs of any defects." "Be upfront about any small defects such as scratches or stains and include photographs of any problem areas." "If you can't decide between two quality ratings, choose the lower one."
- Rething pairs a cut-out with an in-context photo (above); Baymard asks for 3+ thumbnails (cut-out, in scale, detail).
- A cutout hides wear at the edges and removes context. Always one detail or flaw photo, a plain condition line, and a size line. The Etsy seller-handbook page I tried returned 4 bytes (walled), so no Etsy quote.

## 4. Design patterns and layout options

Verified CSS facts: `drop-shadow()` makes "a blurred, offset version of the input image's alpha mask" and "conforms to the shape (alpha channel)", unlike `box-shadow` (MDN https://developer.mozilla.org/en-US/docs/Web/CSS/filter-function/drop-shadow; lines 248-249 of `research/cutouts/raw/02-mdn-dropshadow.md`, another agent's capture of the same page) [V]. So on a flattened JPG it shadows the rectangle. MDN: `mix-blend-mode` "sets how an element's content should blend with its backdrop" (https://developer.mozilla.org/en-US/docs/Web/CSS/mix-blend-mode; I read the page but did not keep the file) [V].
Heuristics [U]: `multiply` makes white pixels take the backdrop colour but also darkens every other pixel by it, so it only rescues white-background JPGs on LIGHT pages, not on burgundy. Contact shadow (small flat ellipse under the base) says "sits on a surface"; floating shadow (blurred, offset) says "hovers". Mixing both reads as messy. Hanging items (chandelier) get no ground shadow.
Site already uses `repeat(4, minmax(0, 1fr))` (storefront.css lines 464, 759) and `aspect-ratio: 4 / 5` (lines 477-491, 779) [V], so Option A below matches existing tokens.

Observed baseline/scale strategies [V]: SSENSE bottom-anchors in an identical 2:3 frame; Rething centres with variable scale (38-60% of canvas height); DWR and Chairish normalise every item to fill a square (DWR trims and pads 10%; Chairish `aspect=fit`). Baymard's In Scale finding says normalising removes size cues, so a size line is mandatory.

**Option A, Shelf rows on the page colour (recommended pilot)**
- Look: no card boxes. Each row of 4 objects stands on a thin ledge line; items share a bottom baseline; each has a small contact shadow; captions sit under the ledge on the same burgundy as the hero.
- CSS ideas: `display:grid; grid-template-columns:repeat(4,minmax(0,1fr))` (phone `repeat(2,...)`); tile `aspect-ratio:4/5; display:flex; align-items:flex-end`; `img{max-height:calc(var(--s,1)*88%); max-width:86%; object-fit:contain; object-position:center bottom}`; contact shadow as `::after` with `radial-gradient` ellipse in `--burgundy-deep` (#321520); ledge as a 1-2px pseudo-element line (pink or champagne, with `box-shadow` glow). `--s` is a hand-set 0.6-1 scale knob per item (not cm-true).
- Pros: objects look in the room like the hero; same background as the page; baseline gives the strongest scan rhythm; works on cream with a warm shadow.
- Cons: needs alpha cutouts for everything; chandelier and wall art break the baseline (hang from a top rail, hang art above); a hand-set `--s` can lie about size, so keep the size line.

**Option B, Tinted tiles per category (Rething / DWR style)**
- Look: 4:5 tiles, a per-category tint, item centred with about 10% padding, floating soft shadow, caption below.
- CSS ideas: `aspect-ratio:4/5; background:var(--tint); display:grid; place-items:center; padding:10%`; `img{width:100%;height:100%;object-fit:contain; filter:drop-shadow(0 10px 14px rgba(0,0,0,.35))}`; `auto-fill, minmax(min(100%,180px),1fr)` for flexible columns.
- Pros: forgiving for odd shapes; easy to add the second image on hover; works with JPG studio shots as a fallback.
- Cons: tiles read as product cards, not as a room; tints must be checked against caption contrast; no real-world scale; tinted-per-category is not seen on any live shop [U].

**Option C, Floating objects on the page colour, no ledge**
- Look: like the hero lamp. Cutouts centred in transparent 4:5 cells, `filter:drop-shadow`.
- Pros: least CSS; same colour as the page.
- Cons: scale and baseline chaos (a shaker next to a trench); shadows float with no ground; hardest to scan (NN/g's "scale" and "orientation" factors).

**Option D, Scale-true shelf**
- Look: Option A, but height = `calc(var(--h-cm) * var(--cm-px))` clamped (`clamp()`), so a lamp is taller than coupes.
- Pros: honest size at a glance (answers Baymard's In Scale); looks like a real shelf.
- Cons: needs `height_cm` for every item; small items shrink (shaker, coupes); wide objects (leopard) need a width cap; trench and painting are too large; harder on 2 phone columns. Better as a v2 on top of A.

**Option E, Mixed wall and shelf**
- Look: objects stand on a ledge; flat art and framed pieces hang in a "wall" row of fixed-size frames; clothes hang from a rail.
- Pros: most editorial; fits flat art honestly (no fake cut-out).
- Cons: breaks NN/g's single-style rule unless frame size and row rhythm stay identical; most design work; not a 12-slot grid test.

## 5. Accessibility

Thresholds quoted from MDN's WCAG guides (https://developer.mozilla.org/en-US/docs/Web/Accessibility/Guides/Understanding_WCAG/Perceivable/Color_contrast and .../Operable); the W3C pages returned a Cloudflare "Just a moment..." page [V]: text "at least 4.5:1"; large text "at least 3:1" (18pt, or 14pt bold); 2.5.8 target size min "at least 24px wide by 24px tall"; 2.5.5 (AAA) "at least 44 CSS pixels"; 2.4.7 visible focus; 2.4.13 (AAA) focus indicator at least a 2px perimeter and 3:1 change.

Contrast, computed this session with the WCAG relative-luminance formula (hexes from `site/storefront.css` and `atmosphere.css` [V]; golds are placeholders, no gold token exists in the site CSS):
| Pair | Ratio | Use |
|---|---|---|
| cream #f6efdf on burgundy #451c2b | 12.61:1 | captions OK |
| cream on #422831 / on wall #652b40 | 11.61 / 9.29:1 | OK |
| muted #d1bdb8 on #422831 / on #652b40 | 7.40 / 5.92:1 | secondary text OK |
| pink #e5a6b4 on #422831 / on #451c2b | 6.61 / 7.18:1 | links, focus ring OK |
| #74645e on cream | 4.92:1 | OK |
| rust #b75834 on cream | 4.11:1 | fails 4.5 for normal text; large text only |
| line #79545e on #422831 | 2.05:1 | decorative ledge only; not for a focus ring (needs 3:1) |
| placeholder gold #c9a14a on #451c2b / on cream | 5.97 / 2.11:1 | fine on burgundy, decorative only on cream |
| placeholder champagne #e8d5a3 on #451c2b | 9.96:1 | OK |

- Alt text, one-offs: say what it is and one visible feature, add maker or era only if known: "Brass and cream urn lamp with a pineapple finial and linen drum shade" (A1). Do not write "cutout" or "photo of". Observed: Sunbeam writes descriptive alt ("Vintage white ceramic ashtray with small hand-painted Gavin figurine and blue handwritten text..."); Rething sets the second image `alt=""`; Chairish appends "For Sale"; Lost & Loved's visible `<img>` has `alt=""` with the name only in a `visually-hidden` span.
- Name each card link once: title, price, and status as text ("Sold"). Do not rely on grey or a ribbon colour alone.
- Whole card as one link (Georges `a.gvc-card`, Sunbeam `full-width-link`, Areaware `a.increase-target`, Rething heading link `full-unstyled-link`) [V]. On a 360px phone, 2 columns with 16px gutters and a 12px gap is about 158px wide per tile (my arithmetic), far above 24px and 44px.
- Focus: Georges uses `outline:2px solid #202020;outline-offset:3px` [V]. On burgundy use pink or cream, 2px or more, offset 3px, ring visible against both tile and page.
- Hover-only second images fail on touch. Baymard's Pottery Barn participant: "I'm swiping to the right to see if it will show me other pictures, and it doesn't!" Use dots or swipe on phones; keep hover transitions short and respect `prefers-reduced-motion` [U].
- Captions on a solid field below the cutout, never over a busy image.

## 6. Recommendation: pilot Option A

**What the pilot shows** (12 items, 4 columns by 3 rows desktop, 2 columns by 6 rows on phones):
- Each row on a shared baseline with a ledge line; caption = title (maker and era if known), one size line ("27 cm tall", from measurement), price, same fields on every tile (Baymard).
- One tile in a SOLD state (render one item as sold in the pilot only, clearly demo data): text badge plus price kept.
- One item with 3 images (cut-out, in-room, detail or flaw) to test dots on phones and hover on desktop.
- A switch between cream and burgundy page colour, to prove the alpha cutouts on both.
- A "scale knob" `--s` per item, to see if hand-set scale reads right before building cm-true scale.

**Readiness of your test set** (from `site/catalog-data.js` chips and `research/inventory/2026-10-26-catalog.md`):
| Slot | Item | Chip / state | Stress test | Ready? |
|---|---|---|---|---|
| R1 | A1 brass lamp | ready | tall and narrow; baseline | yes |
| R1 | A2 chandelier | ready | hangs, no baseline | yes |
| R1 | A10 pink coupes | reshoot | glass edges, smallest scale | no |
| R1 | A14 leopard | still (video frame) | wide object; source is 568x320 video export | no |
| R2 | A12 decanter | not in catalog data; "needs own shot" | glass | no |
| R2 | A11 cocktail shaker | not in catalog data; "needs own shot" | small, metal | no |
| R2 | A3 cubist painting | reshoot (angled) | flat art in a frame tile | no |
| R2 | A4 framed ink face | reshoot (angled) | framed, portrait | no |
| R3 | B6 feather hat | ready | wispy alpha edges | yes |
| R3 | B7 harness belt | ready | thin, long, chain | yes |
| R3 | B9 fringed boots | reshoot (crop) | pair on baseline, fringe edges | no |
| R3 | B1 trench | reshoot (crop) | large end of scale | no |

- 4 of 12 are ready. Other "ready" catalog items: A22 dress form and A23 sneaker-leather collar. If you want real cutouts before building, swap A22 and A23 in for two reshoot items, or cut the other 8 from existing crops as layout-only placeholders marked "layout test".
- Glass, feathers and fringe are the hardest alpha edges [U]; keep them in the set. Cutout tooling is covered by the other agents' `research/cutouts/raw/02-*` files, not here.
- Shoot-list for the reshoot: each piece straight-on, evenly lit, bottom edge visible, ruler or tape in a second frame; then a detail or flaw shot.

## Method and reproducibility
- Pages: `env -u MSYS_NO_PATHCONV crawl4ai "<url>" -o all -bc < /dev/null > out.json`, then read `.html` from the JSON. Tile fragment for WGACA fetched from the page's own `data-tile-url`.
- Image checks: downloaded the exact served image URLs quoted above (curl, or Python urllib), opened with Pillow, `convert("RGBA")`, bounding box of alpha > 16, corner pixels, and the fraction of alpha 0. Python with Pillow lives in `C:\Users\ethan\crawl4ai-venv`. Repeatable on any URL above.
- Raw captures: `research/cutouts/raw/03-*.html` (kept) and a few walled pages as `03-*.all.json`. I deleted the 6-byte JSON, the empty `.err` logs, and two empty W3C captures and duplicated large JSON; the MDN pages for `drop-shadow` and `mix-blend-mode` were captured but not kept (the first is also in `02-mdn-dropshadow.md`).

## Sources
- Rething https://www.rething.uk/ · Design Within Reach https://www.dwr.com/ · SSENSE https://www.ssense.com/ · Areaware https://www.areaware.com/ · Chairish https://www.chairish.com/ · What Goes Around Comes Around https://www.whatgoesaroundnyc.com/ · Gantri https://gantri.com/ · Sunbeam Vintage https://sunbeamvintage.com/ · George's Vintage https://georgesvintage.com/ · Lost & Loved https://lostandloved.co.uk/
- Nielsen Norman Group https://www.nngroup.com/ · Baymard Institute https://baymard.com/ · Vestiaire Collective https://faq.vestiairecollective.com/ · MDN https://developer.mozilla.org/ (WCAG summaries, CSS) · W3C WCAG https://www.w3.org/WAI/ (walled)
- Local: `site/storefront.css`, `site/atmosphere.css`, `site/catalog-data.js`, `research/inventory/2026-10-26-catalog.md`, `research/lostandloved-home-20261026-luna5.md`.
