# CSS typography and spacing audit (read-only)

Audited 2026-10-29. Lane D of the 2026-10-29 type-and-spacing research (Sonnet subagent). The
subagent's Write tool was refused, so the parent session saved its returned report here verbatim. The
ephemeral scripts and the frozen CSS copy stayed in the session scratchpad and are not in the repo.

## Summary
- Your counts hold within a few rules. The working tree moved during the audit (another writer), so I froze a copy and cite it.
- 115 font-size declarations are under 12px, counting `font:` shorthand that a `font-size` grep misses. 77 are live; 38 are dead (overridden, `display:none`, or no markup). At 390px, 25% of visible characters render under 12px; at 1440px, 18%.
- Faux-bold: none renders today on any page. All 11 candidates set weight 400 through the `font:` shorthand. I found two faux-italics instead: DM Sans in `p.owner-aside` and `<cite>`.
- Spacing: 177 of 757 tokens move more than 2px under a strict snap. 20px is the most-used value (64 tokens) and has no anchor in the scale.
- px letter-spacing: 5 instances, all Bodoni. `.collection-mark` is -0.169em, against -0.125em designed.
- Measure: `.hire-disclosure p` (90ch), the fine-print list (85ch) and `.music-credit` (to 189ch) are too wide. The hire grids drop to 18-19ch columns at 820px and 1100px.
- Quick wins are ranked in section 7.

**Snapshot.** Another writer was editing `account-preview.css`, `storefront.html` and `homepage.css` while I worked. I froze a copy at HEAD `3800032` plus the staged index, and every `file:line` refers to that copy. If lines drifted, search by selector. Short SHA-1 of the frozen CSS: storefront `9559d21f`, atmosphere `499f5a71`, room-preview `0782a17a`, homepage `3586add1`, sample-shop `121fa2c6`, account-preview `fda23484`, category-colors `c61efac5`, showroom `fa3cb7fb`, demo `c0b30da7`.

**Method.**
1. A tokenizer parsed all nine CSS files into 1,311 rules and 3,536 declarations, with file, line and `@media`.
2. Chromium (DevTools) loaded the frozen page at 360, 390, 820, 1100, 1440 and 1700px. I opened the product, bag, tour and Account dialogs so lazily built markup existed.
3. I then read `getComputedStyle` for every element and for every rule setting `font-size` or `letter-spacing`.

Family, uppercase, live and overridden are therefore measured, not guessed. **[U]** = static analysis could not settle it.

## 0. Which CSS is live where

| Page | Stylesheets | Notes |
|---|---|---|
| `index.html` | none | 1-line redirect. `build.mjs` copies `storefront.html` to `dist/index.html`, so **storefront.html is the homepage**. |
| `storefront.html` | `assets/fonts/fonts.css`, `storefront.css`, `atmosphere.css`, `room-preview.css`, `homepage.css`, `sample-shop.css`, `account-preview.css`, `category-colors.css` (this order) | Later files win ties. Most tiny sizes are declared 2-5 times across these. |
| `showroom.html` | `fonts.css`, `storefront.css`, `atmosphere.css`, `showroom.css`, `category-colors.css` | Side page. Only `showroom.css` (84 lines) is exclusive. |
| `demo-photos.html`, `demo-showroom.html` | `fonts.css` + inline `<style>` | Side pages, not in the build. |
| `demo.css` | nobody | Its header says "Loaded only by the local /demo route; excluded from the publishable build". |

## 1. Your counts, confirmed

| Claim | Found (frozen copy, all 9 files) |
|---|---|
| More than 40 distinct font-sizes | 49 distinct px values + 31 fluid/non-px (`clamp`, `vw`, `em`) = 80 expressions in 455 declarations. |
| 68x 12px, 44x 11px, 25x 10px, 17x 9px, 13x 8px, 3x 7px | `font-size` property only: 72, 43, 27, 18, 14, 3. Counting `font:` shorthand (38 carry a px size): 75, 48, 32, 18, 14, 3. |
| 18 distinct line-heights | 19 via `line-height`; **22** with shorthand (extra 1.16, 1.25, 1.35). |
| letter-spacing mixes em and px | 51 declarations, 31 distinct values. **5 are px**: -11, -7, -2, plus -1.5 and -1 on `.wordmark`. |
| 70 distinct px in padding, margin, gap | 66 non-negative (65 above 0) + 4 negative (-2, -8, -10, -40) = 70. 1,078 tokens, 245 of them `0`. |
| Body 15px / 1.6 | `storefront.css:34-42` (size at :39, line-height at :40). |

## 2. Tiny text (under 12px)

**115 declarations under 12px** in the 7 homepage sheets: 0px x1, 6px x1, 7px x3, 8px x14, 9px x18, 10px x32, 11px x46. **77 are live** (render at some width, when a dialog or overlay opens, or only on showroom.html). **38 are dead.**

Measured on the homepage by characters of visible text: at **390px, 25% (3,014 of 11,942 characters, 212 of 643 text nodes) are under 12px**. At 1440px, 18% (2,139 of 12,058). At 390px the sizes are 11px (1,815 characters), 9px (637), 10px (453), 8px (74), 7px (35).

Reading the tables:
- **@media** is the enclosing query as written: `<=767` is `max-width:767px`, no brackets means none.
- **family** is the computed first family of a real matched element, not the rule's own `font-family`.
- **UC** means `text-transform: uppercase` on that element.
- "phones" means live at 360 and 390.
- Rows are sorted by size. Rows with the same selector and size are merged.

### 2a. Live (73 merged rows)

| px | selector | file:line [@media] | family | UC | status | UI |
|--:|---|---|---|---|---|---|
| 7 | `.owner-copy .eyebrow` | storefront:1770 [<=767] | Space Mono | UC | phones | kicker above owner copy "The only thing you can't take home." |
| 8 | `.site-header .saved-count` | account-preview:103 [<=767] | Space Mono | - | phones | saved-count badge on the phone header heart |
| 8 | `.saved-nav .saved-count` | storefront:1486 [<=767] | Space Mono | - | phones | same badge (duplicate rule) |
| 8 | `.room-working .eyebrow` | room-preview:85 [<=767] | Space Mono | UC | transient | kicker in the room-editor loading overlay |
| 8 | `.collection-context .saved-count` | storefront:746 | Space Mono | - | all | count badge on "Saved finds" above the grid |
| 8 | `.status` | storefront:815; :1718 [<=767] | Space Mono (dialog chip) | UC | in product dialog | category chip in the product dialog ("Sample collection") |
| 8 | `.owner-copy .eyebrow` | storefront:985 | Space Mono | UC | >=820 | same owner kicker |
| 8 | `.footer-bottom`, `.footer-bottom button` | storefront:1837, :1846 [<=767] | DM Sans | - | phones | footer legal line and the "Daytime colors" toggle |
| 8, 9, 11 | `.product-price small` | storefront:1742 [<=767], :889; homepage:57 | [U] | [U] | JS-conditional [U] | "guide price" note; emitted only for non-sample prices (none today) |
| 9 | `.account-nav small` | account-preview:3 | DM Sans | - | all | small tag in header Account buttons |
| 9 | `.account-heading .eyebrow` | account-preview:113 [<=767] | DM Sans 500 | UC | in Account dialog | dialog kicker |
| 9 | `.salon-tour small` | atmosphere:313 [<=767] | DM Sans | - | phones | caption on the hero tour tile |
| 9 | `.design-detail > span` | atmosphere:336 [<=767] | DM Sans | - | phones | pink-stemware hotspot caption |
| 9 | `.product-meta .status` | homepage:132; sample-shop:105 [both <=767] | DM Sans 500 | UC | phones | category chip on all 52 product cards |
| 9 | `.room-working .eyebrow` | room-preview:76 | Space Mono | UC | transient | loading overlay kicker |
| 9 | `.footer-bottom`, `.footer-bottom button` | storefront:1138, :1142 | DM Sans | - | >=820 | footer legal line and toggle |
| 9 | `.detail-category` | storefront:1202 | Space Mono | UC | in product dialog | "Lighting / A1" line atop the dialog |
| 9, 11 | `.reveal-cover` | storefront:1755 [<=767], :915 | [U] | [U] | JS-conditional [U] | "View cover (18+)" button for hidden items |
| 9 | `.owner-ticket` | storefront:1782 [<=767] | Space Mono | - | phones | "NOT FOR SALE" ticket |
| 10 | `.account-preview-label` | account-preview:7 | DM Sans | - | all | "Coming soon" tag in header and menu buttons |
| 10 | `.room-project-bar > div > span` | account-preview:18 | DM Sans | - | all | room-project subtitle |
| 10 | `.account-heading .eyebrow` | account-preview:24 | DM Sans 500 | UC | in Account dialog | dialog kicker |
| 10 | `.account-tabs button span` | account-preview:33 | Space Mono | - | in Account dialog | count chip on tabs |
| 10 | `.account-room-card .account-caption` | account-preview:74 | DM Sans | - | in Account dialog | "Example project · AI-generated room" |
| 10 | `.account-room-save .eyebrow` | account-preview:78 | Space Mono | UC | in Account dialog | dialog kicker |
| 10 | `.salon-copy .eyebrow` | atmosphere:68; homepage:100 [<=767] | DM Sans 500 | UC | phones | hero kicker on phones |
| 10 | `.salon-tour small` | atmosphere:203 | DM Sans | - | >=820 | hero tour tile caption |
| 10 | `.design-room figcaption` | atmosphere:334 [<=767] | DM Sans | - | phones | design photo caption |
| 10 | `.room-example small` | room-preview:21 | DM Sans | - | all | "AI-generated example room" |
| 10 | `.room-secondary span` | room-preview:46 | Space Mono | - | all | count chip in room-editor controls |
| 10 | `.room-tray button` | room-preview:53 | [U] | [U] | JS-conditional [U] | buttons on picks in the room tray |
| 10 | `.room-privacy` | room-preview:68 | DM Sans | - | all | "Your photo stays in this tab" |
| 10 | `.product-meta .status` | sample-shop:27 | DM Sans 500 | UC | >=820 | product card chip on desktop |
| 10 | `.bag-count` | sample-shop:38 | Space Mono | - | all | count badge on the header Bag button |
| 10 | `.saved-count` | storefront:203 | Space Mono | - | >=820 | header heart-count badge |
| 10 | `.eyebrow` (base) | storefront:251 | Space Mono per :250; hero and Account kickers override to DM Sans 500 | UC | all | base for the 8 kickers |
| 10 | `.owner-price span` | storefront:1015 | Space Mono | - | all | "Firm." beside $10,000,000 |
| 10 | `.detail-price small`, `.detail-notes` | storefront:1233, :1250 | DM Sans | - | in product dialog | "Sample price · USD" and the "About this find" block |
| 11 | `.account-dialog .account-fine-print` | account-preview:56 | DM Sans | - | in Account dialog | sign-in fine print |
| 11 | `.account-preview-note`; `.account-footer .account-text-link` | account-preview:115; :131 [<=767] | DM Sans | - | in Account dialog | "Just a preview" strip; "Back to the shop" |
| 11 | `.site-header .header-actions > button` | account-preview:136 [<=380] | DM Sans | - | 360 only | header Account and Bag buttons |
| 11 | `.object-caption` | atmosphere:128 | DM Sans | - | >=820 | "Quite the conversation starter." |
| 11 | `.disco-motion-toggle` | atmosphere:157 | DM Sans | - | all | "Start the disco" button |
| 11 | `.design-detail > span` | atmosphere:233 | DM Sans | - | >=820 | pink-stemware hotspot caption |
| 11 | `.music-credit` | atmosphere:271 | DM Sans | - | all | footer music credit |
| 11 | `.salon-tour` | atmosphere:312 [<=767] | DM Sans | - | phones | hero tour tile text |
| 11 | `.piece-category` | category-colors:70 | Space Mono | UC | showroom.html only | category line on the 3D showroom |
| 11 | `.salon-copy .eyebrow` | homepage:18 | DM Sans 500 | UC | >=768 | hero kicker on desktop |
| 11 | `.category-filters button span` | homepage:48 | DM Sans | - | all | count pill in filter chips |
| 11 | `.hire-scope` | homepage:173 | Space Mono | UC | all | "One find" label on each tier card |
| 11 | `.room-upload small` | room-preview:17 | DM Sans | - | all | "JPG, PNG or WebP · up to 15 MB" |
| 11 | `.room-label` | room-preview:34 | DM Sans 600 | - | all | "01 / Make your picks" step labels |
| 11 | `.room-selected-product span, a` | room-preview:41 | DM Sans | - | all | "$245 sample price" |
| 11 | `.room-tray span`; `.room-unplaced li` | room-preview:52; :62 | [U] | [U] | JS-conditional [U] | tray labels; "could not place" reasons |
| 11 | `.room-layer-actions button` | room-preview:60 | DM Sans | - | transient | "Flip" and layer buttons |
| 11 | `.room-help` | room-preview:64 | DM Sans | - | all | help lines (5 of them) |
| 11 | `#room-working-label` | room-preview:85 [<=767] | DM Sans | - | transient | loading overlay text |
| 11 | `.sample-notice` | sample-shop:95 [<=767] | DM Sans | - | phones | "A sample of our future shop..." banner |
| 11 | `.category-filters button` | sample-shop:97 [<=767]; storefront:659 | DM Sans | - | phones | filter chips |
| 11 | `.product-add` | sample-shop:106 [<=767] | DM Sans | - | phones | "Add to bag +" on all 52 cards |
| 11 | `.owner-ticket` | storefront:979 | Space Mono | - | >=820 | "NOT FOR SALE" ticket |
| 11 | `.detail-notes h3` | storefront:1257 | DM Sans 700 | - | in product dialog | "About this find" subhead |
| 11 | `.button` | storefront:1530 [<=767] | DM Sans 600 | - | phones | every CTA button on phones |
| 11 | `.section-intro p` | storefront:1576 [<=767] | DM Sans | - | phones | intro paragraph under section titles |
| 11 | `.footer-top p` | storefront:1826 [<=767] | DM Sans | - | phones | footer tagline |

Side pages, not in the table: `showroom.css:83` `.showroom-header nav` 11px at <=370; `demo.css:69` 11px at <=767; `demo-photos.html:14` and `demo-showroom.html:15,27,34,38,62` use 11px inline.

Worst live offenders:
- `.owner-copy .eyebrow`: 7px mono uppercase on phones (`storefront.css:1770`).
- `.status` (8px) and `.detail-category` (9px) in the product dialog, the surface read before "Add to bag" (`storefront.css:815`, `:1202`).
- The 9px uppercase chip on all 52 phone cards (`sample-shop.css:105`).

### 2b. Dead or not rendering (36 merged rows)

Listed so nobody "fixes" a size that does nothing. "renders N" is the computed size of the winning rule.

| px | selector | file:line [@media] | status |
|--:|---|---|---|
| 0 | `.menu-toggle` | sample-shop:125 [<=370] | overridden, renders 12px |
| 6, 7, 8 | `.hero-stamp span` | storefront:1555 [<=767], :1403 [<=1150], :412 | no markup |
| 7, 8 | `.product-id` | storefront:1722 [<=767], :851 | `display:none` (`atmosphere.css:249`) |
| 8 | `.salon-copy .eyebrow` | atmosphere:300 [<=767] | overridden, renders 10px |
| 8 | `.hero .eyebrow` | storefront:1510 [<=767] | no markup |
| 9 | `.category-filters button span` | storefront:677 | overridden, renders 11px |
| 9, 10 | `.sort-box select`, `.collection-context`, `.collection-context button`, `.collection-bottom p` | storefront:1695, 1701, 1704, 1751 [<=767]; :715, 726, 736, 925 | overridden, renders 12-13px |
| 10 | `.tour-button small`; `.back-top`; `.tour-copy .tour-footnote`; `.price-notes summary` | storefront:383; :1121, :1829; :1294; :1811 | no markup |
| 10 | `.menu-toggle` | storefront:1493 [<=767] | overridden, renders 12px |
| 10 | `.category-filters button` | storefront:1681 [<=767] | overridden, renders 11px |
| 11 | `.display-shelves .department p`; `.department p` | atmosphere:326; storefront:1605 [<=767] | overridden, renders 12px |
| 11 | `.collection-bottom p` | atmosphere:347 [<=767] | overridden, renders 12px |
| 11 | `.product-meta .status` | homepage:54 | overridden, renders 9-10px |
| 11 | `.room-demo summary > span`; `.room-demo > p` | room-preview:24; :26 | no markup |
| 11 | `.desktop-nav` | sample-shop:85, storefront:1368 | nav is `display:none` from 768 to 1400px (`account-preview.css:89`, `homepage.css:83`) |
| 11 | `.search-box input` | storefront:704 | overridden, renders 14-16px |
| 11 | `.notes-grid p` | storefront:1044, :1805 [<=767] | overridden, renders 12-13px |
| 11 | `.price-notes summary`, `.price-notes > div` | storefront:1062, :1077 | no markup |
| 11 | `.collection-intro p` | storefront:1652 [<=767] | overridden, renders 13px |

Cascade drift behind the dead rows. Selectors with many `font-size` declarations spread across files:

| Selector | Declarations | Files |
|---|--:|---|
| `.product-title` | 12 | 4 files |
| `.collection-intro h2` | 10 | 4 files |
| `.wordmark` | 9 | 3 files |
| `.salon h1` | 7 | 2 files |
| `.desktop-nav` | 6 | 4 files, never visible 768-1400px |

The hero `h1` visitors see is `.salon h1` (`homepage.css:19`, 7.8vw gives 112px at 1440). The `.hero h1` rules in `storefront.css` match nothing. About 63 rules in the `.hero*`, `.tour-button`, `.price-notes` and `.back-top` families (`storefront.css:232-430, 346-391, 1050-1095, 1120-1135`, plus media copies) look dead. I DOM-tested only the members that set a tiny size, so the rest is **[U]**.

## 3. Faux-bold (and faux-italic) check

**Nothing renders faux-bold today, on the homepage or the side pages.**

Evidence:
- The runtime scan covered every text element plus every `::before` and `::after`.
- It ran at 6 viewports with the product, bag, tour and Account surfaces opened, giving 394 element groups per width.
- It found **0** elements in Bodoni Moda or Space Mono with computed weight of 600 or more.
- `showroom.html`, `demo-photos.html` and `demo-showroom.html`: also 0.
- There is no global `h1..h6 { font-weight }` reset and no `font-synthesis` rule, so safety rests on each rule's own weight.

Why the naive scan over-reported: all 11 candidates set weight through the **`font:` shorthand** in the same block, which a `font-weight` grep misses.

| Candidate | Weight source | Computed (runtime) |
|---|---|---|
| `.account-heading h2` | `account-preview.css:25` `font: 400 clamp(30px,3.5vw,42px)/1.2 var(--display)` | Bodoni 400 |
| `.account-dialog h3/h4` | `account-preview.css:37` `font: 400 28px/1.25 var(--display)` | Bodoni 400 |
| `.design-copy h2` | `atmosphere.css:235` `font: 400 ...` | Bodoni 400 |
| `.disco-note h2` | `atmosphere.css:258` `font: 400 ...` | Bodoni 400 |
| `.showroom-invitation h2` | `homepage.css:60` `font: 400 ...` | Bodoni 400 |
| `.hire-intro h2` | `homepage.css:158` `font: 400 ...` | Bodoni 400 |
| `.hire h4`, `.hire-disclosure h3` | `homepage.css:170` `font: 400 27px/1.25 var(--display)` | Bodoni 400 |
| `.hire-occasions strong` (15 cards) | base `homepage.css:181`; per-card variants `:200-209` | Bodoni 400/500 (some italic), Space Mono 400, DM Sans 600 and 700 |
| `.bag-dialog h2` | `sample-shop.css:67` `font: 400 46px/1.2 var(--display)` | Bodoni 400 |
| `.showroom-intro h1` (showroom.html) | `showroom.css:8` `font: 400 ...` | Bodoni 400 |
| `.control-group h2` (showroom.html) | `showroom.css:31` `font: 400 25px/1.25 var(--display)` | Bodoni 400 |

None is faux-bold. The DM Sans 600 and 700 cards switch the family to `var(--body)` on purpose (`homepage.css:203`, `:207`), and DM Sans is declared 400-700.

Other headings (`.salon h1`, `.product-title`, `.detail-copy h2`, `.owner-copy h2`, `.detail-price strong`) compute 400 or 500. 500 is inside Bodoni's declared range, so the glyphs are real. `<b>` and `<th>` are not used in the markup. The demo pages use Bodoni 500 inline.

**Latent risks (no current bug):**
- The 11 above stay safe only while the `font:` shorthand keeps its `400`. Splitting it into longhands during a token migration would make every one of them faux-bold. A one-line guard is `font-synthesis-weight: none` on `:root`; do the italic fix below first.
- 16 rules set a display or mono family with no weight: `.wordmark`, `.saved-count`, `.eyebrow`, `.hero-stamp span`, `.hero-handwritten`, `.room-note-detail > span`, `.collection-mark`, `.status`, `.product-id`, `.owner-ticket`, `.owner-price span`, `.footer-wordmark`, `.detail-category`, `.disco-signoff`, `.room-demo summary`, `.browse-nav > span`. All sit on `a`, `span`, `p`, `div` or `summary`, which are not bold by default, so they break only if the element becomes a heading or `strong`.
- The Bodoni descriptor is `400 500`. The file reportedly holds 400-900 (from your brief; I did not open the binary, **[U]**). Widening it to `400 900` is the only way to get a real bold.

### 3b. Faux-italic (found while checking)

`fonts.css` declares **no italic face for DM Sans or Space Mono**. Two live cases, at every width:

| Element | Source | Result |
|---|---|---|
| `p.owner-aside` "The wardrobe is another story." (13px, 12px on phones) | `storefront.css:1018-1020` `font-style: italic` | DM Sans, synthesized slant |
| `<cite>The House in Good Taste</cite>` in `.hire-epigraph footer` (12px) | UA default italic; `storefront.html:514`, `homepage.css:234` | DM Sans, synthesized slant |

Fix: set both in `var(--display)`, which has a real italic, or ship a DM Sans italic.

## 4. Clusters and snapping map

Anchors are your provisional ones: label 12 · small 13-14 · body 16 · lead 18-20 · h4 24 · h3 30 · h2 38-48 · h1 fluid; spacing 4/8/12/16/24/32/48/64/96. Each value snaps to the nearest anchor. Ties are written `a|b`. `!` marks a change over 2px. Counts are declarations (or tokens) across all nine files; "(+n)" is the px change.

### 4a. font-size, px values

| Target | Source values x count (change) | Declarations | Over 2px |
|---|---|--:|---|
| label 12 | 0x1(+12)! 6x1(+6)! 7x3(+5)! 8x14(+4)! 9x18(+3)! 10x32(+2) 11x48(+1) 12x75 | 192 | 0, 6, 7, 8, 9 (37) |
| small 13 / 14 | 13x35, 14x24 | 59 | none |
| body 16 | 15x14(+1) 16x13 17x3(-1) | 30 | none. 15 is the current body size, so inheritors change too. |
| lead 18 / 20 | 18x5 19x6(-1) 20x15 21x7(-1) 22x13(-2; ties 20 and 24) | 46 | none |
| h4 24 | 23x11(+1) 24x11 25x7(-1) 26x3(-2) 27x2(-3)! | 34 | 27 |
| h3 30 | 28x4(+2) 29x2(+1) 30x6 31x4(-1) 32x5(-2) 33x1(-3)! 34x6(-4; ties 38)! | 28 | 33, 34 |
| h2 38-48 band | 35x5(+3)! 36x5(+2) 37x2(+1) snap to 38; in band as is: 38x4 39x2 40x1 42x2 43x1 44x1 45x1 46x1 | 25 | 35 |
| hero (above 48) | 50x2 52x2 53x1 60x1 65x1 66x1 72x1 88x1 | 10 | n/a |

**51 of 424 px declarations move over 2px**, 37 of them the sub-10px labels (the intended fix). 10px to 12px reads as "+2" but is a 20% jump on 32 declarations.

Fluid sizes (31 non-px), by role:

| Role | Declarations | Note |
|---|---|---|
| h1 hero (`.salon h1`) | live `homepage.css:19` clamp(74, 7.8vw, 118); phones `:101` clamp(43, 11.9vw, 78); tablet `:86` 8.8vw. Shadowed: `atmosphere.css:72,284,301,360`. Dead: `.hero h1` `storefront.css:259,1387,1514,1901`. | one hero token; 8 declarations are shadowed or dead |
| h2 section titles | `homepage.css:32` 34-48, `:42` 36-55, `:60` 37-56, `:158` 37-56; `atmosphere.css:235` 39-62, `:258` 45-80; `sample-shop.css:9` 36-52; `account-preview.css:25` 30-42; `storefront.css:545` 30-50, `:608` 40-64; `showroom.css:8` 44-74 | min 36-40, vw 3.5-4.6, max 48-66: collapse to 2 tokens |
| h3 / h4 | `homepage.css:38` 21-27, `:164` 28-34, `:232` 24-32; `room-preview.css:15` 28-39, `:77` 26-35 | one clamp or fixed 24 / 30 |

Fixed display sizes with no fluid twin:
- `.collection-mark`: 88 (`storefront.css:623`), then 72 (`homepage.css:44`), then 65 (`sample-shop.css:12`, wins).
- `.owner-copy h2`: 66, and 52 on phones.
- `.disco-note h2` on phones: 53.
- `.room-upload-mark`: 60.

### 4b. line-height: 22 values to 5 tokens

| Token | Values x count |
|---|---|
| 1 | 1x14 (icons, wordmark, badges; keep) |
| 1.15 | 1.04x2 1.05x2 1.1x3 1.12x4 1.13x1 1.15x8 1.16x2 (22) |
| 1.3 | 1.2x9 1.25x4 1.3x5 1.35x1 (19) |
| 1.5 | 1.4x11 1.45x1 1.5x6 1.55x1 (19) |
| 1.7 | 1.6x7 1.65x3 1.7x5 1.8x6 1.85x3 1.9x4 (28; 1.8-1.9 are the loosest: `atmosphere.css:95,237,260`) |

### 4c. letter-spacing em values: 46 declarations, 18 distinct

| Group | Values x count | Proposed |
|---|---|---|
| tight (display) | -0.055x3, -0.04x7, -0.035x7, -0.03x1, -0.025x4, -0.02x1 | -0.05 (3), -0.04 (14), -0.025 (6). Max shift 0.8px at 80px type. |
| label | 0.015x1, 0.02x1, 0.03x1, 0.04x4, 0.05x3, 0.055x1, 0.06x3, 0.08x3, 0.12x2, 0.14x1, 0.15x1, 0.16x1 | 0.04 / 0.06 / 0.08 / 0.12 / 0.16. Max shift 0.24px at 12px type. |

### 4d. Spacing (padding, margin, gap): 757 tokens above 3px, 245 zeros

| Snap target | Source values x count (change) | Tokens | Over 2px |
|---|---|--:|---|
| keep 0-3 | 0x245 2x5 3x9 | 259 | none |
| 4 | 4x17 5x27(-1) | 44 | none |
| 8 | 7x13(+1) 8x46 9x13(-1) | 72 | none |
| 12 | 11x4(+1) 12x76 13x9(-1) | 89 | none |
| 16 | 15x17(+1) 16x33 17x10(-1) 18x33(-2) 19x2(-3)! | 95 | 19 |
| 24 | 21x1(+3)! 22x26(+2) 23x4(+1) 24x47 25x19(-1) 26x9(-2) 27x3(-3)! | 109 | 21, 27 |
| 32 | 30x21(+2) 31x1 32x15 33x1(-1) 34x2(-2) 35x9(-3)! 36x15(-4)! 38x7(-6)! | 71 | 35, 36, 38 |
| 48 | 42x2(+6)! 43x1(+5)! 44x2(+4)! 45x3(+3)! 46x2(+2) 47x2(+1) 48x7 50x6(-2) 51x1(-3)! 52x2(-4)! 55x11(-7)! | 39 | 42-45, 51, 52, 55 |
| 64 | 58x1(+6)! 60x2(+4)! 64x3 65x4(-1) 66x1(-2) 70x2(-6)! 74x1(-10)! 75x2(-11)! 78x2(-14)! | 18 | 58, 60, 70-78 |
| 96 | 86x1(+10)! 90x6(+6)! 95x1(+1) | 8 | 86, 90 |
| keep above 96 | 100x2 105x1 110x1 115x1 | 5 | none |
| **exact ties** | 6x20 (4 or 8, ±2) · 10x47 (8 or 12, ±2) · 14x39 (12 or 16, ±2) · **20x64 (16 or 24, ±4)!** · 28x12 (24 or 32, ±4)! · 40x16 (32 or 48, ±8)! · 56x6 (48 or 64, ±8)! · 80x3 (64 or 96, ±16)! | 207 | 20, 28, 40, 56, 80 (101) |

177 of 757 tokens (23%) move over 2px under a strict snap. **20px is the most-used non-zero spacing value** (64 tokens, 60 live) and sits between 16 and 24. Adding 20, 40 and probably 56 to the scale removes about 100 of the flagged tokens. Out of scope for the map: negative margins (-2, -8, -10, -40) and the container paddings `max(56px, calc((100vw - 1320px) / 2))` (`storefront.css:244,521,1351`, `homepage.css:8`).

## 5. px letter-spacing on display text

All five are on Bodoni display text. px tracking does not scale when breakpoints change the font-size; em would.

| file:line | selector | @media | px | Computed font-size | em now | Note |
|---|---|---|--:|---|---|---|
| `storefront.css:151` | `.wordmark` | - | -1.5 | 28 base; 24, 23, 22, 20 via `homepage.css:77,93,146`, `sample-shop.css:113,122`, `account-preview.css:97,134` (22 and 24 measured) | -0.054 at 28; **-0.063 at 24; -0.068 at 22** | tightens as the logo shrinks. Use `-.055em`. |
| `storefront.css:1472` | `.wordmark` | <=767 | -1 | 22-24 | -0.042 to -0.045 | looser than desktop; same fix |
| `storefront.css:625` | `.collection-mark` ("HV") | - | **-11** | 88 declared; `homepage.css:44` sets 72; `sample-shop.css:12` sets **65 (wins)** | designed -0.125 at 88; **now -0.169** | monogram overlaps more than designed. Use `-.125em`. |
| `storefront.css:1660` | `.collection-mark` | <=767 | -7 | 50 declared, 65 computed | -0.108 | **dead**: `atmosphere.css:342` hides the mark at <=767 |
| `storefront.css:1108` | `.footer-wordmark` | - | -2 | 43 base; 34 (`storefront.css:1445`); 37 (`:1822`) | -0.047 / -0.059 / -0.054 | use `-.05em` |

## 6. Measure (prose line length)

Computed on live blocks of 75 or more characters, using the resolved font's `0` glyph width as 1ch. Viewports: 5 widths, plus the 4 dialogs at 360 and 1440. That gave 43 blocks.

| Viewport | In 30-75ch | Under 30 | Over 75 | Median |
|---|--:|--:|--:|--:|
| 360 | 20 | 23 | 0 | 29ch |
| 390 | 25 | 18 | 0 | |
| 820 | 31 | 8 | 4 | |
| 1100 | 23 | 11 | 9 | |
| 1440 | 27 | 7 | 9 | 45ch |

**Wider than 75ch and wrapping to 2+ lines** (each has a cap that is too loose):

| Selector | Viewport | ch | Est. lines | Cap |
|---|---|--:|--:|---|
| `.hire-disclosure p` ("Some of what you're shown...") | 1100, 1440 | 90 | 4 | `homepage.css:223` `max-width: 90ch` |
| `.hire-details ul > li` (fine print, 4 long items) | 1100, 1440 | 82.7 | 1-3 | `homepage.css:226` `max-width: 85ch` |
| `.hire-steps li` | wide | up to 78 | n/a | `homepage.css:219` `max-width: 78ch` (not hit at tested widths) |
| `.music-credit` (166 characters, 11px) | 820: 104ch, 1100: 142ch, 1440: 189ch | 104-189 | 2, 2, 1 | `atmosphere.css:271`, no cap |

One-liners over 75ch that do not wrap (informational, no cap): `.sample-notice` (79 characters), `.hire-note` (76), `.hire-cta p` (80), `.account-preview-note` (82).

**Under 30ch and wrapping to 3+ lines:**

| Selector | Viewport: ch | Cause |
|---|---|---|
| `.hire-ways li` and `li p` | **820: 18ch**; 360: 26, 390: 29, 1100: 27 | 3 columns from 768 to 1100 (`homepage.css:166`); collapses only at <=767 (`:238`) |
| `.hire-tiers li` and `li p` | **1100: 19ch**; 1440: 26; phones 26-29 | 4 columns until <=1000 (`homepage.css:167`, `:235`) |
| `.hire-occasions li` | 1100: 24, 1440: 24 | `minmax(min(100%,240px),1fr)` (`homepage.css:178`); short text, acceptable |
| `.hire-epigraph` quote | 360: 21.5, 390: 23.5 | `max-width: 40ch` at 24px type (`homepage.css:232`) |
| `.hire-steps li`, `.hire-details li`, `.hire-disclosure p`, showroom invite | phones 26-30 | normal for a 360-390px phone at 15px; not worth fixing alone |

`label.sort-box` at 11ch is a form label around a select, not prose.

## 7. Quick wins (ranked by visible improvement per line changed)

| # | Change | Where | Lines |
|--:|---|---|--:|
| 1 | Phone cards and controls to 12px: `.product-meta .status` (9px), `.product-add` (11px), `.category-filters button` (11px), `.sample-notice` (11px). Delete the duplicate `homepage.css:132`. All 52 cards show a 9px uppercase chip at 390px. Check chip fit at the 153px card width. | `sample-shop.css:95,97,105,106`; `homepage.css:132` | 5 |
| 2 | Kickers to 12px. One token fixes 8 kickers, including the 7px owner kicker on phones. | `storefront.css:251,985,1770`; `atmosphere.css:68`; `homepage.css:18,100`; `account-preview.css:24,78` | 8 |
| 3 | Body `font-size: 15px` to 16px. Everything inheriting grows 6.7%. Review the hire cards (15px) and the product grid afterwards. | `storefront.css:39` | 1 |
| 4 | Product dialog: `.status` (8px), `.detail-category` (9px), `.detail-price small` (10px), `.detail-notes` (10px), `.detail-notes h3` (11px) to 12px. This is what a buyer reads before "Add to bag". | `storefront.css:815,1202,1233,1250,1257` | 5 |
| 5 | Cap prose and fix the narrow tablet grids. Set `.hire-disclosure p`, `.hire-details ul` and `.hire-steps` to about 65ch. Put `.hire-ways` in one column at <=1000. Move `.hire-tiers` to 2 columns at <=1150. Add a cap to `.music-credit`. | `homepage.css:219,223,226,235,238`; `atmosphere.css:271` | 6 |
| 6 | `h1,h2,h3,h4 { text-wrap: balance } p, li { text-wrap: pretty }`. Only `.hire-occasions strong` uses `balance` today (`homepage.css:181`). | `storefront.css`, after the base reset (about line 60) | 2 |
| 7 | Restore the monogram with `.collection-mark { letter-spacing: -.125em }` and delete the dead -7px rule. Set wordmarks to `-.055em` and the footer wordmark to `-.05em`. | `storefront.css:625,1660,151,1472,1108` | 5 |
| 8 | Remove the two synthesized DM Sans italics (use `var(--display)`), then add `font-synthesis-weight: none` on `:root` as a guard. | `storefront.css:1018-1020`; `homepage.css:234`; `:root` | 3 |
| 9 | Delete dead tiny-size rules and shadowed duplicates, so a size migration has one source per selector. That means the 38 rows in 2b, about 63 `.hero*`, `.tour-button`, `.price-notes` and `.back-top` rules, and the 8 shadowed `.salon h1` / `.hero h1` declarations. No visual change. | `storefront.css:232-430,346-391,1050-1095,1120-1135`; `atmosphere.css:72,284,301,360` | about 300 removed |

## 8. Not settled [U]

- **Engines.** All measurement is Chromium. Safari and Firefox synthesize bold and oblique by their own rules. The Bodoni 400-900 range is from your brief, not verified in the binary.
- **Untested widths.** Rules at `max-width` 560/600/900/1000/1050 were exercised only via the nearest tested width (360, 390, 820, 1100, 1440, 1700).
- **JS-conditional text.** `.reveal-cover`, `.product-price small`, `.room-tray *` and `.room-unplaced li` appear only after user actions or data states I did not trigger. Their sizes come from CSS alone.
- **Dead-family claim.** The roughly 63-rule count is DOM-verified only for the members that set a tiny size.
- **Measure sampling.** It covers 43 blocks of 75+ characters, with dialogs at 2 widths. The `0` glyph understates characters per line by about 10-15% for DM Sans.
- **Working tree churn.** Another writer kept changing the CSS during the audit. Re-look up lines by selector before editing.

Cleanup: I started two read-only static servers (ports 8791 and 8792) for the browser runs and stopped both. The ephemeral scripts and the frozen copy are in the session scratchpad only.
