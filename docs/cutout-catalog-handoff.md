# Handoff for Codex: cut-out product tiles for the Hollywood and Vine catalog

Written 2026-10-27 by Claude for Codex (Ricky publishes through the Codex app; Claude cannot publish to the site).
Goal: show catalog items as clean cut-outs in rows and columns, like the lamp and chandelier at the top of the homepage, without
misrepresenting any item and without breaking what the sales channels accept.

Read first, in this order:
1. This file.
2. `research/cutouts/02-cutout-tools-pipeline.md` (tool choice, licences, recipes, pilot criteria; every fact tagged VERIFIED or UNVERIFIED).
3. `research/cutouts/01-channel-image-rules.md` (Etsy, eBay, Shopify, Google image rules).
4. `research/cutouts/03-grid-layout-references.md` (layout references; read before Phase 2).
5. `docs/storefront-art-direction.md` (house look, asset provenance, what was already decided).

**Before you start:** run `git status`. On 2026-10-27 the working tree had uncommitted edits in `site/atmosphere.css`, `site/catalog.js`, `site/disco.js`,
`site/disco-music.js`, `site/storefront.html`, `site/README.md`, `docs/storefront-art-direction.md` and `docs/music-and-lights-notes.md` that Claude did NOT make
(another session's disco and music work). `catalog.js` is on this handoff's path. Finish or commit that work first, then `git pull --rebase`; never overwrite or revert it.
Line numbers quoted below may have moved.

House rules that apply: Vendor First (re-check any option name or licence against the live page before you rely on it), Plan Mode First
(post your plan, then build), ponytail (fewest files, no new dependency without a reason), pathspec `git add` only (never `git add -A`),
commit and push every time a phase lands, never put secrets in the repo. Pushing to GitHub does NOT publish the site; Ricky publishes.

---

## 1. Decisions already made (Ricky, 2026-10-27)

1. **Default tile is pure white** (#FFFFFF), framed like a gallery print (thin frame line plus a white mat) so it reads as deliberate, not as
   a generic web shop. The page around it keeps the burgundy, cream and gold type.
2. **The homepage hero stays as it is**: transparent lamp, chandelier and disco ball on the burgundy wall. Do not touch `atmosphere.css`,
   `disco.js`, `assets/editorial/`.
3. **Pilot four styles side by side** on 12 items so Ricky can choose by eye: (a) white tile, the default Ricky chose; (b) cream tile;
   (c) burgundy tile; (d) "shelf": no tile, cut-outs standing on a thin ledge directly on the page colour like the hero (`03` Option A, the
   layout report's recommendation; Ricky has not reviewed it yet). Tile colour must be a CSS variable, not baked into pixels (see section 6).
4. **Mask-based cut-outs only for the catalog.** The three existing hero cut-outs were made with a generative image edit; do not use that
   method for catalog items (it can quietly redraw the object, and marketplaces require the true item). Original pixels stay; only the
   background is removed.
5. **Keep the untouched original for every item.** The detail view and every Etsy listing must include it (Etsy requires one unedited photo).
6. **Transparent files are for our own site only.** Anything that goes to Etsy, eBay, Shopify or Google is a flattened JPEG.
7. **Keep complete display supports (Ricky, 2026-10-27).** The feather cocktail hat must include the entire mannequin head, neck and base. Apply this to anything presented on a mannequin or similar support: retain the whole photographed display rather than cropping the support to isolate the item. Use source pixels and alpha-only support masks where needed; preserve the original camera framing without inventing missing parts.

Correction to something said earlier in the session: the catalog section does not sit on burgundy. In `site/storefront.css` the page uses
`--paper: #f6efdf` (cream) in the default theme and `--paper: #2c2024` (dark plum) in `:root[data-theme="evening"]`. Burgundy
(`--burgundy: #451c2b`) is the entrance. A white tile on cream paper has low contrast, so the pilot must be reviewed in BOTH themes.
X verified, Y needs review: report `03` read `#422831` as a burgundy in `atmosphere.css`, while `storefront.css` defines `--burgundy: #451c2b`.
Read the real computed background of the collection section in each theme (and the shelf-style page colour) before choosing any hex for the pilot.

---

## 2. What exists (verified in the repo, 2026-10-27)

- `site/catalog-data.js`: `HNV_ITEMS`, 35 records (34 browsable plus `OWNER`). Fields: `id, cat, title, sub, img, chip`.
  `chip` is one of `ready, still, reshoot, auth, mature, nfs`. `img` points into `assets/photos/` (2048 px long edge, with `--480` and `--960` variants),
  `assets/crops/` (about 800 to 2000 px, some very tall), or `assets/stills/` (video frames, about 270x411: too small to use).
- `site/catalog.js`: `card(item)` builds `<article class="product-card">` with `.product-visual > .product-image(button) > img` (640x800, 4:5, lazy),
  a save button, an optional mature-cover reveal button, then `.product-info`. `photoSources()` only builds a `srcset` for `assets/photos/IMG_####.webp`.
  The grid is `#product-grid.product-grid`: 4 columns desktop, 2 on phones (`storefront.css` around lines 757 to 830 and the media queries near 1453 and 1727).
  Current `.product-visual` background is `var(--paper-deep)`; hover scales the image 1.045.
- `site/build.mjs` copies a fixed list of root files plus `assets/` recursively into `site/dist/` (gitignored). A new `assets/cutouts/` folder ships automatically;
  a new root `.html` file does NOT ship unless added to the list. That is useful: the pilot page stays local.
- The site publishes through ChatGPT Sites from `site/dist/` (project id in `site/.openai/hosting.json`). Public access must stay public.
- Fonts and colours: Bodoni Moda (display), DM Sans (body), Space Mono; tokens in `:root` of `storefront.css`.
- No `package.json` exists in the repo, and `site/build.mjs` does not import Sharp (the art-direction doc says Sharp was used for the editorial assets, but that setup is not here).
  Add tooling under `tools/cutout/` only.
- Machine facts (observed locally 2026-10-27): the Windows desktop has an RTX 4060 Ti 16 GB, i7-14700KF, 32 GB RAM. Python 3.12.13 exists in `C:\Users\ethan\crawl4ai-venv` (do not install into it).
  Fedora is out for rembg (its Python is 3.14).

## 3. Which items can be cut out today

Derived from `chip` plus the photo notes in `research/inventory/2026-10-26-catalog.md`. Only the item's own pixels can be used; nothing is invented.

| Tier | Items | What it means |
|---|---|---|
| 1. Real photo of the item | A1 urn lamp, A2 chandelier, A22 dress form, A23 collar art, B6 feather hat, B7 harness belt | Cut out now. |
| 2. Crop from a scene photo | A10 pink glasses, A8 busts, A9 projector (A8 and A9 share one shelf crop: split them), B9 boots, B1 trench, B10 windbreaker, B12 navy dress | Real pixels but small (crops are roughly 800 to 2000 px). Fine for a grid tile; too small for 2048 px channel files. If a crop includes a person's face, skip that item. |
| 3. Flat rectangles | A3, A4 (paintings, shot at an angle with glare), A5 (Elvis frame), C1 to C6, C8 (magazines, book) | No segmentation needed: perspective-correct crop to the rectangle. A3 and A4 need a square-on re-shoot before channels. Mature gating on C1 to C6 stays. |
| 4. Video stills only (about 270x411) | A13, A14, A15, A16, A17, A19, A20, B13, B14, B15, B18 | Cannot be cut out at quality. Keep the current photo-coming treatment until Ricky re-shoots. |
| Not in the catalog yet | A11 shaker, A12 decanter, B5 paisley jacket, B11 chain necklaces | No usable photo. Confirm against `catalog-data.js`. |
| Not for sale | OWNER | Never gets a cut-out. |

## 4. Rules from the channels (summary of `01-channel-image-rules.md`; open its VERIFIED quotes before relying on them)

- **Etsy (VERIFIED):** transparent PNGs are not supported and transparent parts appear black; WebP is not a supported type. Every listing must include at least one
  unedited photo of the actual item against a real background. Backgrounds may be changed in the other photos, but editing may not hide flaws. Etsy suggests
  noting in the description when AI edited a photo. Recommended 2000 px or more on both sides. First photo sets the shape of the rest.
- **Google Merchant Center (VERIFIED):** main image must be the exact item, no text, border, logo, watermark or placeholder. 500x500 minimum enforced from 2027-01-31
  (100/250 until then); about 1500 px recommended. White background is not stated as a rule but every example is white. AI-generated images must keep their IPTC provenance tag.
  Product Studio (free) outputs white and says it does not support light fixtures or wall art.
- **eBay (VERIFIED):** no added borders, text or watermarks; no stock photos for used items; white backgrounds generally best; 1:1 or 16:9 looks best; about 1600 px recommended; 12 MB cap.
- **Shopify (VERIFIED):** 2048x2048 square displays best; use one consistent aspect ratio across a collection; JPEG or PNG both safe.
- **Therefore:** per item, export (a) the untouched original, (b) a transparent WebP for our own site only, (c) a flattened white JPEG (2048x2048, 1:1, sRGB, about q85, at most 1 MB) for channels.
  Never put badges, "SOLD", price, borders or condition text into any channel file.
  Unverified: whether the crosslister copies Etsy's first photo to eBay and Shopify. Assume it might, so the first Etsy photo should be the safe one.

## 5. Tool choice and pipeline (summary of `02-cutout-tools-pipeline.md`)

- **Cutter: rembg 2.0.86 (MIT), pinned to `-m birefnet-general -dc`.** BiRefNet weights are MIT (verified on Hugging Face).
  **TRAP: bare `rembg` defaults to `bria-rmbg` (RMBG-2.0), whose weights are CC BY-NC 4.0; commercial use needs a BRIA agreement. Always pass `-m`. Never use `bria-rmbg` or RMBG-1.4.**
  Re-verify the weights licence on the model page at install time.
- Do not use: remove.bg (standalone service ends 2026-12-01), Google Product Studio (white output, light-fixture/wall-art caveat), Gemini image editing
  (generative, SynthID watermark, no documented transparent output), Apple's built-in tool (no batch).
- Paid fallback only if Ricky agrees: Photoroom Remove Background API, about $0.02 per image (marketing page; plan minimums unverified; free accounts are non-commercial).
- New venv (for example `.venv-cutout`, already gitignored as `.venv/`; pick a name that matches), Python 3.12. `pip install "rembg[cpu,cli]==2.0.86"`. CPU is fine for about 40 items; GPU optional.
- Order of operations: orient + downsize to at most 2048 px long edge + convert to sRGB (cut at no more than 2048 px; the model runs near 1024 px anyway) -> cut ->
  zero the RGB where alpha is 0 -> crop to the **alpha-only** bounding box (Sharp `trim` can silently do nothing on matting output because RGB under alpha 0 can keep the old room) ->
  contain into a fixed 4:5 cell with transparent padding -> WebP with alpha.
- Sharp 0.35.5 (Apache-2.0, Node 20.9 or later) is recommended for resize, sRGB conversion and WebP because the options are verified in the report. A single Python script
  with Pillow is acceptable if you verify its WebP options against current docs; either way keep one script, not two. HEIC is not in Sharp's prebuilt formats: convert to JPEG first.
- **Glass does not get cut.** The chandelier, pink stemware and decanter: no verified tool produces a true glass alpha. Shoot on a seamless backdrop and show the photo on a pale tile
  (or run the pilot and let the result decide, section 7).
- **Shadow in CSS, not in pixels** (verified on MDN): `filter: drop-shadow(0 14px 12px rgb(0 0 0 / .35))` follows the alpha shape; add a CSS ellipse under standing items.
  Bake a shadow only into channel JPEGs, and keep it faint.
- Scale rules (starting points, tune by eye, expect about 5 hand tweaks): cell 4:5. Tall items (lamps, dress form) fill about 88% of cell height; wide items (chandelier, art) about 88% of width;
  small items (hat, belt, stemware) 62% to 70%. Standing items share a bottom baseline, hung items share a top line. Put the per-item fit in a small config file (`tools/cutout/items.json`:
  `id, source, mode: cut | flat | keep, fit: tall | wide | small, anchor: bottom | top | center`) so the CSS stays dumb.
- Mechanical proof that the item was not redrawn (script in section 6 of `02`): at least 99% of pixels with alpha 250 or more must be within 3/255 of the resized source. If the item is mostly
  translucent the check proves little; judge glass by eye only.

## 6. Output files and storefront changes

Per item id, e.g. `A1`:

| File | Spec | Where | Ships |
|---|---|---|---|
| Original | untouched camera file | `media/<id>/orig.jpg` (source from Ricky's Drive when available; until then the 2048 px site photo) | no |
| Site cut-out | transparent WebP, 4:5 cell, 960x1200 plus a 480x600 variant, quality about 82, alpha quality 100, at most 200 KB | `site/assets/cutouts/<id>.webp`, `<id>--480.webp` | yes |
| Channel flat | 2048x2048 JPEG, #FFFFFF, sRGB, 1:1, subject 75% to 90% of frame, at most 1 MB | `media/<id>/flat-white.jpg` | no |
| Channel flat for Etsy | same but subject about 60% to 70% so Etsy's square, portrait and landscape crops do not clip it | `media/<id>/flat-etsy.jpg` | no |

Add `media/` to `.gitignore` (large derived files and Ricky's listing exports). Only generate a channel flat when the source has at least 1500 px on the item's long side; otherwise
record "needs re-shoot" in a manifest (`media/manifest.json`: id, source, source px, mode, tool and flags, pixels-kept result, status).

Catalog wiring (smallest change):
- In `catalog-data.js` add an optional field per item: `cutout: "assets/cutouts/A1.webp"`.
- In `catalog.js` `card()`: when `item.cutout` exists, render `<img class="cutout" src=... srcset="...--480.webp 480w, ...webp 960w" sizes=...>` inside the same `.product-visual`;
  otherwise keep the current image. Keep `width`/`height` attributes and `alt` as the item title. Keep the mature-cover reveal for C1 to C6.
- Detail view: keep the **original photo first**. Do not replace it with the cut-out.
- CSS: `.product-visual.is-cutout { background: var(--tile-bg, #fff); }` with `--tile-bg` set by `data-tile="white|cream|burgundy"` on the grid (cream = `var(--cream)`, burgundy = `var(--burgundy)`). `data-tile="shelf"` drops the tile background and frame,
  bottom-aligns each item (`object-position: center bottom`), and draws a ledge line plus a flat contact shadow under standing items (`03` Option A).
  Add the frame line and mat with existing tokens (`--line`, `--burgundy`, gold if one exists; check). `.cutout { width:100%; aspect-ratio:4/5; object-fit:contain; filter: drop-shadow(...) }`.
  Reduce the hover scale on cut-outs (about 1.02) so it does not crop the frame. No new colours except `#fff`.
- The mix of cut-out tiles and plain photos in one grid looks inconsistent. Until the whole catalog is converted, keep the current photo in the same 4:5 tile with the existing chip.

Card content and layout rules (from `03`; cut-outs are only honest with these):
- **Same fields on every tile** (Baymard: 64% of sites fail this): title with maker and era when known, ONE size line from a real measurement (for example "27 cm tall"), price. Condition goes on the detail view, not the card.
  Add `size` (text) to `catalog-data.js`; leave it blank rather than guess. A cut-out-only grid hides scale (Baymard: 42% of users judge size from images), so a size line is mandatory.
- **Second honest image.** Each cut-out tile reveals the original photo (and later an in-scale or flaw shot) on hover on desktop and with dots or swipe on phones; hover-only fails on touch. Keep the transition short and respect `prefers-reduced-motion`.
  Baymard recommends 3 or more thumbnails per item (cut-out, in scale or in the room, detail or flaw).
- **Sold state (one-of-one stock):** keep the tile in the grid with a text badge "SOLD" and the price kept (Rething, Georges, Lost & Loved do this), never colour or grey alone. A "Past treasures" archive can come later. Render one demo SOLD tile in the pilot, clearly marked demo.
- **Baseline and scale:** shelf style anchors items to a shared bottom edge (SSENSE does `object-contain object-bottom`; Rething centres instead). Hung items (chandelier) hang from a top line, flat art hangs above the ledge.
  Use a hand-set per-item scale knob (`--s`, about 0.6 to 1) in the pilot; real-scale (cm-true) heights are a v2.
- **Accessibility numbers computed in `03`:** cream on burgundy 12.6:1 (fine); the site's `--line` colour on burgundy is about 2:1, so it is decorative only and must not be the focus ring; use pink or cream, 2px or more, offset 3px.
  Whole card is one link; the name is announced once with status as text; alt text says what the item is plus one visible feature, never "cutout" or "photo of".

## 7. Phases (stop at each STOP and show Ricky; do not publish anything)

**Phase 0: setup (about 30 minutes).** New venv, rembg pinned, models downloaded (`rembg d`; confirm the arguments), Sharp or Pillow. Record versions in `media/manifest.json`.
Confirm the weights licence of `birefnet-general` on its model page.

**Phase 1: cut-out test.** Run the pilot in `02` section 7: the chandelier (`IMG_6614`), pink glasses (`crops/IMG_6610_glass`), fringed boots (`crops/IMG_6612_boots`), with the urn lamp (`IMG_6616`) as the easy control.
Arms: A `rembg -m birefnet-general -dc`; B BiRefNet_HR-matting at 2048 px (soft alpha); C no cut (glass control). Record seconds per image. Judge each result on white, black and burgundy with 100% crops against the pass/fail table in `02`.
Output: a contact sheet and a one-page pass/fail table. If glass fails (expected), glass categories use "no cut".

**Phase 2: tile pilot (STOP 1: Ricky decides).** Build `site/pilot-cutouts.html` (local only; not added to `build.mjs`) with **12 items**:
A1 urn lamp, A2 chandelier, A22 dress form, A10 pink glasses, B6 feather hat, B7 harness belt, B9 boots, B1 trench, B10 windbreaker, A3 cubist painting, A4 ink face, A5 Elvis frame.
(A3, A4 and A5 are flat rectangles: they show how art sits in a tile.) Only A1, A2, B6 and B7 have a "ready" chip (A22 and A23 are the other ready items and can substitute for reshoot-chip items). The rest are cut from existing
crops purely as layout tests: label them "layout test" on the page. Show them in a 4-column by 3-row desktop grid and a 2-column phone grid (6 rows), in each of the four styles (white, cream, burgundy, shelf), in both themes.
Include: one demo SOLD tile (marked demo), one item with a second and third image (hover on desktop, dots on phone), the size line and per-item scale knob, and a cream/burgundy page-colour switch to prove the transparent files sit right on both.
Capture screenshots at 1440, 390 and 320 CSS px into `artifacts/pilot/` (already gitignored) and one combined contact sheet per style. Give Ricky the local preview URL (serve from `site/` on a free port; use `python -m http.server`, not port 4173) plus the sheets.
Check horizontal overflow, keyboard focus (visible ring on tile and page), `prefers-reduced-motion`, caption contrast in both themes, and no console errors.

**Phase 3: rollout (only after Ricky picks a style).** Convert every tier 1 to 3 item, wire `cutout` into the catalog, regenerate `media/` channel files where the source is large enough, build with `node build.mjs`, commit, push,
and hand Ricky a one-line publish prompt for the Codex app.

## 8. Acceptance checks

- Every cut-out passes the pixels-kept check, or is judged by eye and flagged (glass).
- No generative model touched a catalog image. Manifest lists the tool and flags for each.
- Alt text stays the item title; captions stay readable; tap targets 44 px; focus ring visible on the tile; contrast of caption text checked in both themes.
- No channel file contains text, badge, border or watermark. No transparent file is in `media/`.
- `node build.mjs` passes, `site/dist/` contains `assets/cutouts/`, and the pilot page is NOT in `dist/`.
- Public access setting preserved; the room is still described as the source of the designer's taste, not as an operating store; gift copy unchanged.
- Every cut-out tile has a size line (or is visibly marked "size coming") and a second photo path (original at minimum); a SOLD tile uses text, not colour alone.

## 9. Do not

- Run `rembg` without `-m`, or use any BRIA model.
- Use a generative edit for catalog items, or replace an original photo with a cut-out.
- Send any alpha PNG or WebP to Etsy, eBay, Shopify or Google.
- Hide flaws, remove cords or labels, tidy patina, or change colours.
- Touch the hero, `disco.js`, or `assets/editorial/`.
- Commit large images or `media/` (gitignored), or use `git add -A`.
- Publish. Ricky publishes from the Codex app.

## 10. For Ricky: shoot for cut-outs (verified Shopify and Photoroom guidance; glass tips from studio blogs)

You are re-shooting anyway; this makes every cut-out easy and the Etsy rules happy.
1. Square: frame photos 1:1 (or leave margin so a square crop already fits). Etsy's first photo sets the shape of the rest.
2. Backdrop: seamless white paper by default; charcoal for white, pale, frosted or glass items so edges show. Never a backdrop colour that appears in the item (no pink behind pink glass).
3. Light: a window, every other light off, flash off. Item about 90 degrees to the window. White foam board fills shadows.
4. Tripod; same distance for similar-sized items (tape a mark on the table); main 1x camera, not ultra-wide; shoot straight on at mid-height; item fills about 70% to 80% of the frame with margin on all sides.
5. Keep the item 2 to 3 feet off the backdrop. Chandelier hangs free with nothing behind it. Wipe fingerprints. Diffuse light on brass so the window does not mirror in it.
6. Shoot extra: the untouched hero shot (this is the Etsy "unedited photo"), flaws close up, maker marks and labels, underside, and one with a tape measure.
7. Settings: JPEG ("Most Compatible" format; UNVERIFIED path). Priorities from the pricing work: Elvis frame (front, back, signatures), white chair (label), lamp base stamp, leopard underside, painting back, glasses and decanter.

## 11. Open issues (not verified; do not guess)

- Etsy's legal image-requirements page (exceptions to the "unedited photo" rule), vintage policy and seller handbook were walled (403 or empty). Confirm in a signed-in browser.
- eBay alpha handling, whether all 24 photos are free, and Inventory API image limits.
- Whether the crosslister copies Etsy's first photo to eBay and Shopify.
- CPU time for a 2000 px image with BiRefNet: no source; the pilot records it.
- BiRefNet training-data licences were not audited (weights card says MIT).
- Photoroom: API-specific terms and plan minimums.
- A single decision for the first Etsy photo: Etsy suggests the clearest, most realistic image first; a white-background flat is allowed only because an unedited original exists elsewhere in the listing.
- No Baymard or NN/g mobile column count was found; "2 columns on phones" rests on 6 of 7 shops whose markup exposes it. WCAG thresholds in `03` are quoted from MDN (the W3C pages were walled).
- Per-category tinted tiles were not seen on any fetched shop; that idea is ours. Only Rething ships true transparent cut-outs in a vintage grid (10 of 10 first images); other shops flatten them at the CDN. A file extension of `.png` proves nothing.
- Of 10 shops tried for layout references, 1stDibs, Mr Porter, Anthropologie, The RealReal, Muuto, HAY and Our Place were walled or unusable; Kaufmann Mercantile's domain now serves a casino page and must not be cited.

## 12. Paste into the Codex app

```
Read docs/cutout-catalog-handoff.md and research/cutouts/01, 02 and 03 in the Vintage repo. Plan first, then do Phase 0, Phase 1 and
Phase 2 only. Use mask-based cut-outs (rembg 2.0.86 pinned to -m birefnet-general -dc; never run rembg without -m) and never use a
generative edit on catalog items. Build the local pilot page with 12 items in four styles (white tile, cream tile, burgundy tile,
and shelf-on-page) in both themes, with a size line on every tile, one demo SOLD tile and one multi-photo item. Capture
screenshots and a contact sheet, run the pixels-kept check, and stop for Ricky to choose. Do not publish and do not
touch the homepage hero. Commit and push with pathspec adds, and report what passed and failed.
```
