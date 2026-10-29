# Vintage visual vocabulary for Holliewood and Vine (2026-10-29)

Lane B of the 2026-10-29 type-and-spacing research (Sonnet subagent). The subagent's Write tool was
refused, so the parent session saved its returned report here verbatim. Raw sources are in `raw/`,
with the source URL on line 1. `sketches/sketch-test.html` and `sketch-test-render.png` are Chrome
renders of every CSS sketch below, using the shipped fonts.

Tags: **[V]** = read or measured this session. **[U]** = memory or inference.

## Summary

Ranked picks: (1) catalogue lot numbers, (2) gallery-style label, (3) film title card and credits, (4) swing price tag, (5) receipt slip for the bag. All are type plus one or two CSS shapes, with no new assets.

- **DM Sans in the shipped subset has no `tnum`/`pnum`/`lnum`/`onum`, and its digits are proportional** [V, fontTools]. The existing `tabular-nums` on `.product-price`, `.bag-item p`, `.bag-total strong` and `.hire-price` renders in DM Sans and does nothing. Bodoni Moda has `tnum`/`pnum`. Space Mono digits are uniform.
- No shipped font has `lnum`, `onum`, `smcp` or №/★/✦, so write "No." in text and build ornaments in CSS.
- Sample listings carry only id/cat/title/sub/source/price. A tombstone with maker, date or dimensions would invent facts, so the label shows true fields only, and the "Sample photo source" link becomes the credit line.
- Lot numbers must come from data, not `counter()`. `.product-id` is already rendered and hidden by `atmosphere.css`, and sample ids collide with inventory ids.
- Avoid grain/foxing (the `--layer-grain` token was never implemented), neon text, animated marquee, matchbooks, and ticket notches on all 15 occasion cards.
- No live vintage shop using swing tags, tickets, matchbooks or marquee was found.

## 1. Site ground truth [V, read this session]

- **Contrast, computed:**
  - Cream `#f6efdf` on paper `#422831` is 11.61, on paper-deep `#4d303b` 10.18, on wall `#652b40` 9.29.
  - Muted `#d1bdb8` on paper-deep is 6.48.
  - Pink `#e5a6b4` on paper is 6.61, on paper-deep 5.80.
  - Brass `#d5b16b` on paper-deep is 5.73.
  - Gilt `#b69553` on paper-deep is 4.11 (fails 4.5 for text). `--relief #ae9680` is 4.15 (fails).
  - `--line #79545e` is 1.80 (decoration only).
  - Ink `#451c2b` on manila `#e6d3ab` is 9.81, on brass `#d5b16b` 7.10. Ink `#351527` on ticket coral `#dc735e` is 5.17.
- **Existing motifs:**
  - `.eyebrow` is mono uppercase 10px/.14em.
  - `.status` category label is 8px base and 11px desktop, but **9px at <=767px** in `homepage.css`.
  - `.product-id` is 8px mono and is **rendered, then hidden** by `.product-id{display:none}` in `atmosphere.css`.
  - `.object-caption` is 11px. `.owner-copy .eyebrow` is 8px.
  - `.owner-ticket` is a rotated pink "NOT FOR SALE".
  - `.hero-stamp` is **dead CSS**: no markup in any html/js/mjs outside `dist`.
  - Also present: `.gilt-frame`, `.salon-ledge`, extruded text-shadow lettering, 15 coloured "invitation" cards in `.hire-occasions`, a WebGL disco ball, and a page-sized screen-blended light layer.
- **Not present:** neon CSS (the neon is only in the room photo), marquee, any ornament rule, grain. `--layer-grain:6` was introduced in commit `bda6327` and never referenced, so grain was never tried and removed.
- **Fonts (fontTools on the shipped woff2 files):**

| Font | Features | Digits |
|---|---|---|
| Bodoni Moda | ccmp, frac, liga, locl, **pnum, tnum** | proportional by default; `tnum` glyphs exist |
| DM Sans | calt, ccmp, dnom, frac, liga, locl, numr | proportional (342 to 656 of 1000); **no tnum/pnum/lnum/onum** |
| Space Mono | ccmp, dnom, frac, numr | uniform 612/1000 |

  Bodoni Moda has wght 400-900 and opsz 6-96 in the file, but `fonts.css` declares `font-weight:400 500`. None of the three has U+2116 (№), U+2605 or U+2726.
- **Cost context:** every extra `filter` or `mask` in view adds repaint work, because the disco layer already repaints at 30 fps. Use them on one-off elements, not on 52 cards.

## 2. Evidence

**Museum label conventions [V]**
- **MGNSW "Exhibition Labelling" (2026):**
  - Order is Artist/maker, Title, Date, Medium/materials, Dimensions, Provenance or collection, Description, kept consistent.
  - 70-80 words per artwork label.
  - Sans text of at least 18 pt for print.
  - Raw file: `mgnsw-exhibition-labelling.md`.
- **NCMA "Label Writing 101":**
  - A "tombstone" is artist, title, date, medium, credit line.
  - "Create a format and stick to it."
  - Raw file: `ncma-label-writing-101.md`.
- **Smithsonian Guidelines for Accessible Exhibition Design** (PDF, text extracted locally):
  - Sans or simple serif, with "easily legible numbers (e.g. distinguishable 5, 6, and 8)".
  - "Do not set text in all caps ... limited to items such as titles and decorative heads."
  - Avoid italic for essential information.
  - Minimum x-height 4.5 mm.
  - "Lighter type weight and greater letter spacing is required when type is reversed out of the background."
  - "Print only on a solid background."
  - Raw file: `smithsonian-accessible-exhibition-design-excerpts.md`.
- **MGNSW verified, NCMA verified, they disagree.** MGNSW lists dimensions and provenance; NCMA's tombstone has a credit line and no dimensions.
- **Needs review for commerce.** Buyers need dimensions (Moore Vintage lists them), so use the MGNSW order and treat the credit line as our photo-source link.
- **Size floor:** the 18 pt and 4.5 mm figures are for printed labels at a distance and do not convert to CSS px. Use the site's own 11px `.status` precedent plus WCAG.

**WCAG** (WebFetch; the crawl returned 4 bytes): 1.4.3 needs 4.5:1 text and 3:1 large (18 pt, or 14 pt bold), and decoration is exempt. 1.4.12 requires no loss of content at 0.12em letter spacing, 0.16 word spacing, 1.5 line height. 2.3.1 forbids more than three flashes per second.

**Shops**
- **Wright (wright20.com)** [V]:
  - Lot card text reads `100 Vladimir Kagan Custom sofa $8,000–10,000 ...` (lot, maker, title, estimate), with sort by "lot (100–376)".
  - Its CSS is `.lot_no{color:#999; font-family:var(--font-family-serif); font-size:3.2rem; letter-spacing:.1rem}`, a large low-contrast tracked serif numeral.
  - The shared auction CSS uses `lining-nums` in 9 rules, `oldstyle-nums` in 3 (a sibling house sets lot numbers oldstyle), and `tabular-nums` once.
  - Evidence file: `wright20-lot-css-evidence.md`.
- **Moore Vintage Archive (moorevintage.com)** [V, re-crawled today]:
  - Title with the date in parentheses: "Frank Gehry for Vitra Wiggle Side Chair (1972, reissued by Vitra in 1992)".
  - Then a spec block: Material / Made in America / Dimensions: 13.75"W x 24"D x 34.25"H / Condition Report. That is the tombstone convention in a real vintage shop.
- **TIAS (tias.com)** [V, dated 2026-10-26 file]:
  - Dealer stock numbers in titles, e.g. "...Raised Gold Trim # 27971 Debsellstoyou $895.00".
  - Today's homepage had rotated them off, so I cited the dated file `research/pages.adateintimecollectibles.com_11804_PictPage_3924275877.-20261026T182342Z.md`, not a live read.
- **Not found:** no live vintage-shop example of swing tags, ADMIT ONE tickets, matchbooks or marquee bulbs. Wasteland was JS-only, and the Beyond Retro, Rokit, Pamono, Lassco and Retrouvius crawls showed nothing readable as design, so I discarded them.

**Hollywood Regency** [V]: Wikipedia names "bold use of color and contrast ... metallic and glass accents", mirrors, animal prints, and "The sunburst wall mirror and clock ... is a regular feature". **Sunburst verified, Greek key needs review:** the page text I read does not mention Greek key, so treat it as [U].

**MDN, all fetched this session; raw files `mdn-*.md`**
- **Widely available:**
  - `clip-path` (since Jan 2020).
  - `mask-image` and `mask-composite` (since Dec 2023, so no `-webkit-` prefix needed).
  - `radial-gradient`, `conic-gradient` and `repeating-conic-gradient` (its page cites starbursts).
  - `border-image`, `font-variant-numeric`, `text-shadow`, `filter: drop-shadow()`, `background-repeat` including `space`, `background-blend-mode`, `prefers-reduced-motion`, `letter-spacing`.
- **Behaviours MDN confirms:**
  - `drop-shadow()` uses the input image's alpha mask, so it follows a clipped shape where `box-shadow` does not.
  - `font-variant-caps` synthesizes small caps when the font lacks them.
  - CSS `content` text is not in the accessibility tree, so keep real information in the DOM.
  - `letter-spacing` above zero suppresses optional ligatures.
- **`corner-shape` is limited and experimental.** Don't use it for ticket notches.

## 3. Shared type rules for label-like motifs
- Labels: Space Mono uppercase, 11px floor, tracking .08-.12em, two words at most.
- Values: DM Sans 13-15px, sentence case. Titles: Bodoni roman.
- Numerals: write "No." as text. Use Space Mono digits, or Bodoni with `tabular-nums` (works). Do not rely on DM Sans `tabular-nums`. Do not promise oldstyle figures.
- Label/value grid: `grid-template-columns:max-content 1fr; column-gap:.9em; row-gap:.15em; align-items:baseline`. The baseline line is needed; the first render was visibly off without it.
- Decorative parts live in CSS pseudo-elements or backgrounds. Real information (number, price) stays in DOM text. Anything animated sits inside `@media (prefers-reduced-motion: no-preference)`.

## 4. Motif-by-motif

**Swing price tag. Rank 4, constrained.**
- Fit: the shop literally uses hand tags (catalog copy: "Shop tag reads $60"). Use it on the detail-dialog price and a few featured pieces. On all 52 cards it becomes a tag farm.
- Type: Space Mono 15-17px, ink `#451c2b` on manila `#e6d3ab` (9.81). Manila, not white.
- Build: `clip-path:polygon()`, a `mask-image:radial-gradient()` hole, a wrapper with `filter:drop-shadow()`, and a 1px `::before` string.
- A11y: the price stays text. Sway only on hover and only under no-preference.
- Cost: one clip, one mask and one filter per tag. Fine for 1-4 tags, avoid for 52.

**Museum / gallery label. Rank 2.**
- Fit: card (under the white panel), detail dialog, owner section. It refines `.product-meta`, `.product-title` and the existing source link.
- Type: MGNSW order. Render true rows only: Listing = Sample, Photo = Source ↗ (the credit line). Add Maker, Date, Materials, Dimensions only when real, with dimensions formatted like Moore's `13.75"W × 24"D × 34.25"H`. Keep to about 12 words on cards.
- Build: `<dl>` with `display:grid`. Optional brass nameplate on the detail dialog only: `linear-gradient(#d5b16b,#b69553)` with ink `#451c2b` (7.1 / 5.1).
- A11y: a real `dl` is read as term/definition pairs. The link keeps a 44px target via padding.
- Cost: zero. Don't restyle `.object-caption` under the entrance cutouts.

**Boutique hang tags. Avoid separately.** It is the swing tag in fashion costume and needs brand and size data the samples lack.

**Ticket stub / ADMIT ONE. One use, optional.**
- Fit: the free "Screen Test" CTA only, not the 15 occasion cards (they already read as invitations).
- Type: Space Mono 13px, tracking .14em: "Admit one · Screen Test". Ink on coral is 5.17.
- Build: two `radial-gradient()` masks combined with `mask-composite:intersect`. **Do not set `mask-size` on them**: my first render did and collapsed to a sliver. Perforation line via `repeating-linear-gradient()`.
- A11y: the visible text is the accessible name. Cost: trivial; clutter medium. Choose ticket or title-card framing for that block, not both.

**Matchbooks. Avoid.** No natural placement, high effort, no precedent found.

**Film title cards and credits. Rank 3.**
- Fit: the Fabulous From Online section, whose copy is already cinema ("You bring the plot. Hollie dresses the set.", "Screen Test", "set"), plus the footer as end credits.
- Type: a "A Holliewood & Vine production" line in mono 11px, tracking .24em. Credit rows with a Bodoni 18px name, a dotted leader, and the price in Space Mono (uniform digits, so right alignment works without any feature). A double rule above and below.
- Build: `border-block:3px double`, plus an `::after` flex leader made of `radial-gradient()` dots.
- A11y: leader dots are background, so nothing extra is read aloud. Cost: zero.

**Marquee bulbs. Avoid animated; at most one static instance.**
- Build: `radial-gradient()` dot plus halo, with `background-repeat:space`. Static looked good in the render.
- Risks: a chase animation brings 2.3.1 risk and competes with the disco layer. If used, make it static, once, and not together with the ticket.

**Art Deco fan / sunburst. One optional ornament.**
- Fit: a sunburst mirror is a regular Hollywood Regency feature [V]. Use one static gilt fan behind the Fabulous headline, or in the dead `.hero-stamp` slot.
- Build: `repeating-conic-gradient(from -90deg at 50% 100%, #d5b16b 0 4deg, #0000 4deg 10deg)` plus `border-radius:200px 200px 0 0`. Rendered cleanly. Decorative; brass is 6.54 on paper.

**Greek-key rule. Optional cheap divider (rank 6).**
- Fit: replace the plain `border-top:1px solid var(--line)` above `.hire` and `.display-shelves`. Greek key is [U] for this style.
- Build: an SVG data-URI as `background-image` with `background-repeat:space no-repeat`. A 14px tile rendered as discrete key spirals, not a continuous meander; a continuous one needs a longer tile, to tune in the browser.
- Decorative; pink is 6.61. Cost about 250 bytes.

**Lot numbers "No. 0042". Rank 1.**
- Fit: card meta line, detail dialog, bag lines.
- Type: "No." plus digits in Space Mono 11px, tracking .1em, muted (6.48 on paper-deep). Wright uses a large low-contrast serif numeral; at 52 small cards a small mono line is quieter.
- Build: unhide `.product-id`. The number is data: a `lot` field assigned at build in stable order, emitted as text. Not `counter()`, not the hash ids, not the ids that collide with inventory ids.
- A11y: real text. Cost: zero. Authenticity per pixel is highest (Wright and TIAS both do it).

**Receipt / sales slip. Rank 5, bag only.**
- Fit: the bag dialog's item lines and subtotal. Checkout is disabled and prices are illustrative, so the slip must keep saying so.
- Type: Space Mono 13px, right-aligned amounts, dotted leaders. This also fixes the dead `tabular-nums`.
- Build: `mask-image:conic-gradient()` with `mask-size:14px 100%` for a torn zig-zag bottom. Paper stays `--paper-deep`, not cream. Remove buttons stay as 44px controls.
- Cost: one mask on one element.

**Neon glow. Avoid as live text.** Bodoni hairlines vanish in the glow, the real neon is already in the room photo, a static glow competes with the screen-blended disco layer, and a flicker risks 2.3.1. If wanted, add a static pink radial halo behind the existing neon photo, with no text and no animation.

**Paper grain / foxing. Avoid.**
- The `--layer-grain` token was never implemented, so there is no precedent to follow.
- Foxing near product photographs reads as damage on the item, which is an honesty problem.
- Smithsonian says "Print only on a solid background."
- It would add another full-page layer over the disco light layer.
- If grain ever ships, it belongs on empty burgundy walls only, never on or near a product panel.

## 5. Top 5 with CSS sketches
Each sketch rendered correctly in Chrome on 2026-10-29, using the shipped fonts. Source: `sketches/sketch-test.html`.

**1. Lot number** (delete `.product-id{display:none}` in `atmosphere.css`; markup `<span class="product-id">No. 0042</span>`)
```css
.product-meta { flex-wrap: wrap; align-items: baseline; gap: 2px 10px; }
.product-id { font: 400 11px/1.5 var(--mono); letter-spacing: .1em; text-transform: uppercase; color: var(--muted); }
.product-meta .status { font-size: 11px; }   /* removes the 9px mobile override in homepage.css */
```

**2. Gallery label**
```css
.product-label { display: grid; grid-template-columns: max-content 1fr; align-items: baseline;
  column-gap: .9em; row-gap: .15em; margin: 0; font: 400 13px/1.45 var(--body); }
.product-label dt { font: 400 11px/1.45 var(--mono); letter-spacing: .1em; text-transform: uppercase; color: var(--muted); }
.product-label dd { margin: 0; }
.product-label a  { color: inherit; text-underline-offset: .25em; }   /* "Source ↗" = credit line */
```

**3. Title card and credits**
```css
.titlecard { font: 400 11px/1.6 var(--mono); letter-spacing: .24em; text-transform: uppercase; text-align: center; color: var(--pink); }
.credits   { list-style: none; padding: 18px 0; border-block: 3px double var(--pink); }
.credit    { display: flex; align-items: baseline; gap: .6em; font: 400 18px/1.9 var(--display); }
.credit > :last-child { order: 2; font: 400 15px var(--mono); }
.credit::after { content: ""; order: 1; flex: 1; height: .8em;
  background: radial-gradient(circle, currentColor 0 .7px, #0000 1.2px) 0 100% / 6px 6px repeat-x; opacity: .55; }
```

**4. Swing price tag**
```css
.tag-wrap { display: inline-block; position: relative; margin-top: 30px; rotate: -4deg; transform-origin: 50% 0;
  filter: drop-shadow(2px 3px 0 #21151f99); }
.tag-wrap::before { content: ""; position: absolute; left: 50%; bottom: 100%; width: 1px; height: 28px; background: var(--muted); }
.price-tag { display: block; padding: 1.5em 1em .6em; background: #e6d3ab; color: #451c2b; font: 400 17px/1 var(--mono);
  clip-path: polygon(0 .9em, .9em 0, calc(100% - .9em) 0, 100% .9em, 100% 100%, 0 100%);
  mask-image: radial-gradient(circle at 50% .7em, #0000 .24em, #000 .26em); }
@media (prefers-reduced-motion: no-preference) { .tag-wrap { transition: rotate .5s; } .tag-wrap:hover { rotate: 3deg; } }
```

**5. Receipt slip**
```css
.bag-receipt { padding: 18px 16px 30px; background: var(--paper-deep); font: 400 13px/1.8 var(--mono);
  mask-image: conic-gradient(from -45deg at bottom, #0000, #000 1deg 89deg, #0000 90deg);
  mask-size: 14px 100%; mask-position: 50%; }
.bag-receipt .row { display: flex; justify-content: space-between; }
```

## 6. Avoid, with reasons
- **Grain/foxing:** the token was never implemented, it reads as item damage, and it adds a full-page layer.
- **Neon text:** Bodoni hairlines wash out, 2.3.1 flicker risk, and the neon is already in the photo.
- **Animated marquee bulbs:** flashing risk, competes with disco, and kitsch.
- **Matchbooks:** no placement, high effort, no precedent.
- **Ticket notches on all 15 occasion cards:** that section is already the loudest on the page.
- **Hang tags as a separate motif, and tags on all 52 cards.**
- **Small caps and oldstyle figures:** synthesized or absent in every shipped font.
- **Glyph ornaments (№, ★, ✦):** missing from all three fonts, so they fall back to a system font.

## 7. Open items before shipping
- Fix the four inert `tabular-nums` sites: `.product-price`, `.bag-item p`, `.bag-total strong`, `.hire-tiers .hire-price`. Switch them to Space Mono or to Bodoni with `tabular-nums`.
- Decide the lot-number rule: stable 0001-0052, assigned at build, not reusing inventory ids.
- Raise the 9px mobile `.status`, and check the 8px `.owner-copy .eyebrow` and `.product-id` once visible.
- Re-test each motif at 0.12em forced letter spacing (WCAG 1.4.12). The sketches are rendered but not stress-tested at that setting.
- Greek-key attribution for Hollywood Regency needs a primary source.
- Safari and Firefox were not tested.
