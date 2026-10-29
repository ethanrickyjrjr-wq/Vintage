# Vintage typography for Holliewood and Vine

Date: 2026-10-29. Lane A of the 2026-10-29 type-and-spacing research (Sonnet subagent). The
subagent's Write tool was refused, so the parent session saved its returned report here verbatim.
Raw evidence (about 354 KB) is in `raw/`, with each text file's source URL at the top.

Scope: research only. Tags: **[V]** = read or measured this session (source named). **[U]** = memory or inference. "X verified, Y needs review" where sources disagree.

## Summary
- Keep Bodoni Moda. The shipped files already hold wght 400-900. Widening fonts.css to `400 900` costs 0 B (Google serves identical 46,260 B and 53,756 B files for 400..500 and 400..900). Nothing on the page asks for Bodoni above 500 today (0 elements, computed-style audit), so name a placement: the "Disco night" tile at 800.
- ONE SWAP: Space Mono -> Courier Prime, +2,120 B. Space Mono's README says it is a display face; Courier Prime was "designed specifically for screenplays", and the Hire copy is already film talk (Screen Test, Logline, Casting Call, Cameo). It is not drop-in: caps are 17% shorter at equal px, so add `size-adjust: 120%` (MDN: Baseline widely available). I tested that on the live page: no overflow at 1440/390/320; one eyebrow wraps at 320.
- Keep DM Sans. Jost is the better period sans and 36 KB lighter, but body would need about 16.4 px. Runner-up.
- Accent face: optional, zero is legitimate. If a new neon line of 48 px or more is wanted above #hire-contact, Sacramento a-z subset, +6,172 B. No candidate matches the real sign's casual upright hand. Bodoni italic plus glow is the 0 B fallback.
- Net +8,292 B. Optional DM Sans opsz trim is -25,792 B (needs visual check).
- Special Elite and Yellowtail are Apache 2.0, not OFL.

## Bottom line
1. **Keep Bodoni Moda and the burgundy system.** Shipped Bodoni files hold wght 400-900 and opsz 6-96. Widening `font-weight: 400 500` to `400 900` costs 0 B: Google serves byte-identical 46,260 B (normal) and 53,756 B (italic) for the 400..500 and 400..900 requests [V, raw/gfonts-latin-woff2-sizes.txt]. But no element computes above weight 500 today (0 of 651) [V, raw/audit-storefront-computed-styles.txt], so the unlock does nothing until a rule uses it. One named placement: the "Disco night" occasion title at 800, mixed case (render G/H) [V].
2. **The one swap: Space Mono -> Courier Prime (+2,120 B).** Space Mono's README: "designed ... explicitly for use in headline and display typography" [V], yet it runs at 8-11 px here. Courier Prime: "designed specifically for screenplays" [V], and the Hire section already says Screen Test, The Logline, Casting Call, The Cameo (storefront.html lines 421-434) [V]. Not drop-in: caps are 17% shorter at equal px, so add `size-adjust: 120%`.
3. **Keep DM Sans.** Jost is the better period sans (1920s German lineage, same designer as Bodoni Moda, same 0.460 em x-height) and 36,148 B lighter than the shipped DM Sans, but body would need about 16.4 px site-wide. Only one swap is allowed, so it is the runner-up.
4. **Accent face: optional; zero is a legitimate answer.** The site has no neon text element and the real sign is already in the room photo. Bodoni italic plus text-shadow glow gives a decent lit script at 0 B (render) [V]. If Ricky wants a true tube-neon line, Sacramento is the only candidate that reads as tubing: 6,172 B (a-z subset), serving one new line of 48 px or more, nothing else.
5. **No listed accent matches the real sign.** It is a casual, upright, hand-lettered monoline in a cloud-shaped outline [V, photo IMG_6610]. Sacramento is thinner and more slanted. An SVG trace of the real sign would be the only exact match (0 font bytes) [U], needs Ricky's eye.
6. **Net bytes:** swap +2,120 and accent +6,172 = +8,292 B. The optional DM Sans opsz trim (side note, needs visual check) is -25,792 B, making the net -17,500 B.
7. **References agree on direction.** Two of three LA vintage clothiers run Jost (Resurrection, The Way We Wore); Timeless Vixen runs Bodoni Moda plus Playfair and Old Standard TT. All three set headings in tracked uppercase [V, declared CSS].

## 0. Vendor-First disclosure
- **Google Fonts specimen pages could not be read.** All 15 `fonts.google.com/specimen/<Family>` crawls returned an identical 1,672-byte JS shell (identical md5). That is above the 1 KB wall heuristic but still a wall. I deleted those files.
- **What verified each font instead:** (1) google/fonts `METADATA.pb` (license, designer, axes, weights): `raw/meta-*.pb`, URL pattern https://raw.githubusercontent.com/google/fonts/main/<ofl|apache>/<name>/METADATA.pb. (2) https://fonts.google.com/metadata/fonts, the JSON behind the specimen pages: `raw/gfonts-metadata-trimmed.json`. (3) `DESCRIPTION.en_us.html` from the same repo: `raw/desc-*.html`; Space Mono has none (404), so `googlefonts/spacemono` README: `raw/desc-spacemono-readme.md`. (4) Google Fonts CSS2 API woff2 `/* latin */` files, sized with `wc -c`: `raw/gfonts-latin-woff2-sizes.txt`. The site's shipped files match those sizes exactly (46,260 / 53,756 / 62,724 / 16,520 B), so they are the same Latin subsets [V].
- **Licenses.** OFL [V]: Courier Prime, Sacramento, Jost, Bodoni Moda, DM Sans, Space Mono, Cutive Mono, Josefin Sans, Monoton, Yesteryear, Pinyon Script, Italiana, Limelight, Poiret One. **APACHE2, not OFL [V]: Special Elite and Yellowtail** (`apache/` dir in google/fonts). Neither is recommended.
- **Source disagreements:** `date_added`: DM Sans .pb 2019-06-12 vs JSON 2019-06-11; Space Mono .pb 2016-06-20 vs JSON 2016-06-15. Irrelevant to the decision.

## 1. Traditions and where each goes
Design-intent quotes marked [V] are the foundry/Google descriptions in `raw/desc-*`. What each tradition "looks like" is [U].

| Tradition | Anchor | Where on this site | New font? |
|---|---|---|---|
| Old-Hollywood marquee / title card | Yesteryear is "loosely based on the title screen from the 1942 film The Palm Beach Story" [V]; Limelight is Art Deco "often used to suggest the 1920's ... theatre ... hollywood filmmaking" [V]. Heavy Didone fat-face is the Bodoni side [U]. | Bodoni 700-900 on occasion tiles; Bodoni italic for credit lines ("Hollie dresses the set."). Render G/H: wght 900/800 reads as a title card [V]. | No |
| Hollywood Regency salon | High-contrast Didone with italics [U] | Product names, section H2s; wordmark locked | No |
| Art Deco | Jost "inspired by 1920s German sans-serifs" [V]; Josefin Sans "geometric sans serif designs from the 1920s", x-height "half way from baseline to cap height" [V], so display only | Tracked uppercase on tiles already uses Bodoni 500 at about .05em ("Cocktail hour") [V] | No |
| 70s disco | Tight bold geometric caps (Avant Garde-style) [U] | "The party" tile: DM Sans 700 uppercase -.04em [V]; Jost 700 is a near-twin (render E/F) [V]. Monoton is "a contemporary take on metalpress fonts like Prisma (1931) ... above 30 points" [V]: caps-only, striped, wraps; rejected | No |
| Neon script | Sacramento: "monoline, semi-connected script inspired by hand-lettering ... brochure work of the 1950's and 1960's" [V] | One new display line (section 2) | Conditional |
| Boutique hang-tags | Typed tag: number, era, price [U] | Item meta line; render M reads as a tag, DM Sans (O) reads as UI [V] | Courier Prime |
| Typewriter labels | Courier Prime: "new take on IBM's Courier ... designed in 1956 by Howard Kettler ... specifically for screenplays" [V] | `--mono` consumers: 15 visible elements at 1440 px [V audit] | Courier Prime (swap) |

## 2. Does the current trio fit?
Current state [V] (headless Chromium, computed styles of site/storefront.html): DM Sans 334 elements at 400, 105 at 500, 17 at 600, 8 at 700; Bodoni 95 at 400, 5 at 500, 17 italic; Space Mono 15 elements at 8, 9, 10, 11, 13, 20 px.

### Bodoni Moda: keep, unlock range
Axes [V]: opsz 6-96, wght 400-900, normal + italic, OFL, Owen Earl. Do not drop `opsz`: a wght-only file is 25,884 B vs 46,260 B, and the 86-130 px entrance headlines depend on it (not rendered side by side, [U]). Zero Bodoni elements compute above 500, so no faux bold is being applied today [V].

### Body: DM Sans vs Jost vs Josefin Sans
| | x-height | cap | x/cap | woff2 latin | Note |
|---|---|---|---|---|---|
| Bodoni Moda | 0.460 em | 0.750 | 0.613 | 46,260 B | [V] fontTools |
| DM Sans shipped (opsz 9-40) | 0.526 at opsz 9 | 0.700 | 0.751 | 62,724 B | "intended for use at smaller text sizes", started from Poppins [V] |
| DM Sans wght-only | 0.504 | 0.700 | 0.720 | 36,932 B | opsz axis costs 25,792 B |
| Jost 400-700 | 0.460 | 0.700 | 0.657 | 26,576 B | same designer and x-height as Bodoni [V] |
| Josefin Sans 400-700 | 0.378 | 0.702 | 0.538 | 28,528 B | "for use at larger sizes" [V]; reject for body |

- **Keep DM Sans for body.** At 15 px Jost is visibly smaller (render A vs B); matching takes about 16.4 px (render C).
- **Deciding constraint:** bytes favor Jost (-36,148 B vs shipped DM Sans); fit and cost favor the mono swap (film copy already exists; one `@font-face` descriptor vs resizing all body text). One swap only, so Jost is the runner-up. Resurrection and The Way We Wore both run Jost [V], which also means it reads as the common vintage-retail default.
- Side note, not a family change, **needs visual check:** DM Sans without `opsz` (36,932 B) saves 25,792 B but loses optical sizing at 38 px ("The party") and 10-11 px.

### Labels: Space Mono vs typewriter faces
- Space Mono README [V]: "original monospace display typeface ... developed explicitly for use in headline and display typography ... geometric slab core with novel over-rationalized forms." Retro-futurist, not typewritten [U].
- Courier Prime: x-height 0.451 em, cap 0.580 em (Space Mono 0.496 / 0.700) [V], so caps are 17% shorter at equal px (render J vs I) [V]. Advance 0.600 em vs 0.612 em [V].
- Fix: `size-adjust: 120%` on the `@font-face`. MDN: "All metrics associated with this font are scaled by the given percentage ... glyph advances, baseline tables"; Baseline widely available [V, raw/mdn-size-adjust.md]. At 120% caps match Space Mono and lines run +17.5% wider (27.34 em vs 23.26 em for "HOLLIEWOOD & VINE FABULOUS FROM ONLINE") [V, raw/font-advance-widths.txt].
- **Tested without editing site/:** injected `--mono: Courier Prime` with `size-adjust: 120%` into the live page [V]. No horizontal overflow at 1440, 390 or 320 (scrollWidth unchanged). Changes: `p.eyebrow` "A little room for possibility." wraps from one line to two at 320 px (16.5 to 33 px tall); `span.owner-ticket` "NOT FOR SALE" is 1.8 px taller at 390 and 320 and 11.5 px wider. Only the 15 visible mono elements at load were measured; hidden dialogs were not.
- Tracking: render K at about 12.5 px effective with about .1em reads well; current .14em is too loose for a wide-set face [U].
- Rejected: Cutive Mono (x-height 0.378 em, hairlines dissolve on burgundy, render L) [V]; Special Elite (53,296 B, distressed, Apache) [V].
- Flag for the spacing agent: 8 px and 9 px mono labels are below a readable floor in any face; `size-adjust` does not fix that.

### Accent face: only if a new display line exists
Rendered with one pink glow next to a crop of the real sign (raw/render-neon-candidates.jpg) [V]:

| Font | Latin woff2 | Phrase-only subset | Verdict |
|---|---|---|---|
| Sacramento | 23,708 B | 2,988 B | Only true monoline tube look; thinner and more slanted than the real sign; x/cap 0.412, unusable below about 28 px |
| Yesteryear | 23,008 B | 3,076 B | Best Hollywood provenance, but heavy brush script: diner chrome, not tube |
| Monoton | 16,492 B | 1,572 B | Caps-only, striped, wraps |
| Pinyon Script | 39,044 B | n/a | Formal copperplate; clashes with a casual sign |
| Limelight / Italiana / Poiret One | 23,080 / 10,100 / 7,824 B | n/a | Deco display; Bodoni 800-900 already covers marquee |
| Bodoni italic + glow | 0 B | n/a | Surprisingly good; reads lit marquee, not tube |

- **Pick, conditional: Sacramento**, subset to a-z, "H" and `. , ! '` = **6,172 B** (Google API `text=` parameter) [V]. Not the 2,988 B phrase-only subset: it falls back silently when copy changes.
- **Exactly where:** one new display line of at least 48 px (36 px mobile) directly above `#hire-contact`, text "do it for the plot", glow, no animation. That element does not exist today; the motto appears only as small text in the "Something else" card (storefront.html line 463) [V].
- **Not for the sign-off.** The shipped `.disco-signoff` (Bodoni italic 23 px) read better than Sacramento at 36 px, which wraps and thins (render, last panel) [V].
- Glow recipe as rendered, without pure white (white is reserved for product frames): `color:#ffe3ee; text-shadow:0 0 4px #ffd1e6, 0 0 10px #ff4fa3, 0 0 22px #ff2d8f, 0 0 44px #ff2d8f, 0 0 70px #d6007a`.
- If no new line is wanted, ship no accent face.

## 3. New references (not in the luna reports)
Method: `curl` of homepage HTML plus up to 8 linked stylesheets (crawl4ai markdown strips CSS). Values are **declared in CSS/theme variables, not rendered**. Raw rule dumps: raw/ref-*.md. Tracking converted to em.

| Shop | Type as declared | Case / tracking |
|---|---|---|
| Timeless Vixen, https://timelessvixen.com/ (Beverly Hills couture per its meta description) | Body Old Standard TT 18 px/1.6; h1-h6 and logo Playfair Display 400; nav and top bar Bodoni Moda 400; Libre Franklin also declared | h1-h6 uppercase 3 px (about .09-.14 em at 34-22 px); top bar Bodoni 13 px uppercase 3 px (about .23 em); nav 16 px uppercase 0 |
| Resurrection Vintage, https://resurrectionvintage.com/ | Jost 500 for headings and text; base 15 px (`--text-base: .9375rem`) | Headings uppercase .15 em (one component overrides to 0); buttons uppercase .18 em; badges .625 rem uppercase |
| The Way We Wore, https://thewaywewore.com/ (LA) | Headings Fraunces 600; body, nav, subheading Jost 400/500 | Headings uppercase .1 em; nav .15 em; logo uppercase .12 em; buttons 14 px uppercase .125 em; body tracking declared .1 em with a .75 size multiplier, effective size needs review |
| Obsolete, https://www.obsoleteinc.com/ (LA antiques, counter-example) | rift-soft (Adobe Fonts) on 19 rules; Trade Gothic Next faces declared | Not read; homepage was a 17 KB shell |

Inference [U from V data]: tracked uppercase headings at about .1-.15 em are the vintage-retail default; Bodoni Moda is used by a real vintage couture shop, so the display face is on-pattern; Jost is the common vintage-retail sans (a point for it, and a reason it would look generic). Scanned, not selected: Angeles Vintage, Furnish Me Vintage, Dear Golden, Vinterior, Shrimpton Couture, Dorothy Draper & Co., Pamono (`raw/ref-others-scanned.md`). WGACA returned 403; Decades, Unique Vintage, Rellik, Trashy Diva did not respond.

## 4. Recommendation table
| Role | Font | Where on site | Why | Bytes (woff2 Latin) | Source URL |
|---|---|---|---|---|---|
| Display (keep, unlock range) | Bodoni Moda, wght 400-900, opsz 6-96, OFL | `fonts.css` declare `400 900`; first use "Disco night" occasion title at 800, mixed case | Title-card fat-face look from a file already shipped | +0 (46,260 + 53,756 shipped) | https://fonts.google.com/specimen/Bodoni+Moda (specimen unreadable; verified via https://raw.githubusercontent.com/google/fonts/main/ofl/bodonimoda/METADATA.pb) |
| Body (keep) | DM Sans, opsz 9-40, wght 100-1000, OFL | Body 15 px, "The party" tile | Legible small; Jost needs about 16.4 px | 0 (62,724 shipped) | https://raw.githubusercontent.com/google/fonts/main/ofl/dmsans/METADATA.pb |
| Labels (the one swap) | Courier Prime 400, static, OFL, Alan Dague-Greene | Replace `--mono`/Space Mono; add `size-adjust: 120%`; tracking about .1 em; labels, hang-tag meta, scope lines | Typewriter/screenplay voice matching the film copy already on the page | +2,120 (18,640 vs 16,520) | https://raw.githubusercontent.com/google/fonts/main/ofl/courierprime/METADATA.pb |
| Accent (the one add, conditional) | Sacramento 400, a-z + H + `. , ! '` subset, OFL, Astigmatic | One new neon line, 48 px or larger, above `#hire-contact`; nowhere else | Only monoline tube-style script; skip if no new line (Bodoni italic + glow is the 0 B fallback) | +6,172 | https://raw.githubusercontent.com/google/fonts/main/ofl/sacramento/METADATA.pb |
| Side note, needs visual check | DM Sans without `opsz` | Not counted as swap or add | -25,792 B, changes rendering at 38 px and 10-11 px | -25,792 | raw/gfonts-latin-woff2-sizes.txt |

Net with swap + accent: **+8,292 B**. With the DM Sans trim: **-17,500 B**.

## Raw index (all in research/type-and-spacing-2026-10-29/a-vintage-type/raw/)
meta-*.pb, desc-*, gfonts-metadata-trimmed.json, gfonts-latin-woff2-sizes.txt, font-metrics-fonttools.txt, font-advance-widths.txt, mdn-size-adjust.md, audit-storefront-computed-styles.txt, ref-*.md, render-* (headless Chromium renders A-P and neon rows; the neon render includes a crop of the shop's own photo). Throwaway scripts and font copies are only in the scratchpad.
