# Web type scale and spacing: gap research for Holliewood and Vine

Date: 2026-10-29. Lane C of the 2026-10-29 type-and-spacing research (Sonnet subagent). The
subagent's Write tool was refused, so the parent session saved its returned report here verbatim.
About 45 fetched or computed files, with source URLs, are in `raw/`, plus `raw/scripts/`.

Scope: the 7 gaps in the brief. Not repeated: 45-75ch measure, 4/8/12/16/24/32/48/64/96 grid, role tokens, internal <= external, 44px targets and 16px inputs, dashboard 12px floor.

Tags: **[V]** fetched or run this session (raw file in `raw/`, URL in the index at the bottom). **[RUN]** computed here from the repo's own woff2 files or Utopia's published formula (`raw/computed-*.md`, scripts in `raw/scripts/`). **[U]** memory or inference.

## Summary
- **Ten font sizes instead of 40:** Utopia steps -1 to 5 (360 to 1500px viewport, base 16 to 18, ratio 1.2 to 1.25), a hero pair of 52 to 130px, and labels at 12px with an 11px floor.
- **Body 16px minimum.**
- **Labels:** 0.08em tracking, range 0.06 to 0.12.
- **`opsz: auto` does not protect Bodoni Moda.** Measured on the shipped woff2: the hairline is about 0.2 CSS px at every size. Use no Bodoni under 20px, `font-optical-sizing: none` for 20 to 31px, and auto from 32px up.
- **Display tracking:** -0.01 to -0.02em (Apple New York serif), versus the hero's -0.055em.
- **Fallback `@font-face` blocks:** the values are computed.
- **Flagged for review:** the hero fails WCAG 1.4.4 at 300% zoom.

## Bottom line

1. **Ten font sizes, not 40.** Seven fluid steps (Utopia method, 360 to 1500px viewport, base 16 to 18px, ratio 1.2 to 1.25), one hand-set hero pair (52 to 130px), two fixed label sizes (12px, 11px floor). One ratio cannot span 12px labels to a 130px Didone hero (10.8x), so the hero is its own clamp.
2. **Body to 16px (1rem) minimum, 18px on desktop.** 15px is the bottom edge of Butterick's web range (15 to 25px) and under Apple's 17pt default and Material's 16sp body. DM Sans at auto optical size has x-height 0.502em vs Arial 0.519 [RUN on shipped file], so 15px DM Sans (7.5px x-height) reads like Arial at 14.5px. X verified, Y needs review: Capsize says 0.504 (= opsz 14); the file's default instance (opsz 9) is 0.526, which would be larger than Arial. The claim holds only while optical sizing is on (the default).
3. **Label floor 11px (0.6875rem) absolute, 12px for anything a buyer must read; tracking 0.08em, allowed 0.06 to 0.12.** Current 6 to 10px labels are below every floor found (Apple iOS 11pt, Material label-small 11sp, NN/g 8pt = 10.7px). WCAG sets no px minimum. The site's 0.14em exceeds Butterick's 0.05 to 0.12em, and Space Mono already has wide fixed advances.
4. **`opsz: auto` is not enough for Bodoni Moda on burgundy.** Measured on the shipped woff2: hairline is about **0.2 CSS px at every font size from 11px to 130px**. The axis changes proportions and contrast ratio, not hairline px. Rule: no Bodoni under 20px, none for price/size/condition, `font-optical-sizing: none` (opsz 11) for 20 to 31px, auto from 32px.
5. **Display tracking -0.01 to -0.02em, leading 1.1.** Apple's New York (an optical-size serif) is -0.014em at 34 to 52pt and -0.016em at 70pt and up. The hero's -0.055em is 3.4x that. X verified, Y needs review (a Didone display choice; check "oo", "ll" by eye).
6. **Product card order: era/maker label, Bodoni title, price (only 600 weight, brightest), size/condition line.** Baymard and NN/g agree on distinct styling per element and price emphasis; boutique logic disagrees in one place (section 6).
7. **Font loading: add metric-matched fallbacks.** Three `@font-face` blocks, about 15 lines, zero dependencies. Bodoni Moda is 14.2% wider than Times New Roman, so an unmatched swap reflows the hero. Also preload DM Sans (only Bodoni is preloaded). Skip Capsize and fontaine as dependencies: they are bundler transforms and `site/build.mjs` is custom.
8. **Fluid type vs WCAG 1.4.4 needs a test.** Computed at a 1500px screen: body grows 1.85x at 200% zoom and 2.71x at 300%; a 52 to 130px hero grows only 1.42x at 300%. Today's hero is no better (1.38x at 200%, desktop rule only). `atmosphere.css:284` (`font-size: 9vw`, 768 to 1150px) and `:360` (`12.4vw`, <=370px) are bare-`vw` text sizes, the exact pattern WCAG failure F94 names.

---

## Proposed token block

```css
:root {
  /* ---------- FLUID SIZES (rem, so browser text-size settings work) ----------
     Utopia method, viewports 360 -> 1500px (1500 = the site's layout cap:
     atmosphere.css:56 `width: min(1500px, 100%)` and storefront.html sizes attr),
     base 16 -> 18px, ratio 1.2 -> 1.25.
     Formula: slope=(max-min)/(maxVW-minVW); clamp(min, intercept + slope*100vw, max). */
  --step--1: clamp(0.8333rem, 0.8123rem + 0.0936vw, 0.9000rem); /* 13.3 -> 14.4px  meta, size/condition  */
  --step-0:  clamp(1.0000rem, 0.9605rem + 0.1754vw, 1.1250rem); /* 16   -> 18px    body                  */
  --step-1:  clamp(1.2000rem, 1.1349rem + 0.2895vw, 1.4062rem); /* 19.2 -> 22.5px  price                 */
  --step-2:  clamp(1.4400rem, 1.3396rem + 0.4461vw, 1.7578rem); /* 23   -> 28.1px  card title            */
  --step-3:  clamp(1.7280rem, 1.5798rem + 0.6586vw, 2.1973rem); /* 27.7 -> 35.2px  spare (h3 / lead)     */
  --step-4:  clamp(2.0736rem, 1.8611rem + 0.9445vw, 2.7466rem); /* 33.2 -> 44px    h2 section title      */
  --step-5:  clamp(2.4883rem, 2.1899rem + 1.3262vw, 3.4332rem); /* 39.8 -> 54.9px  h1                    */
  --step-hero: clamp(3.2500rem, 1.7105rem + 6.8421vw, 8.1250rem); /* 52 -> 130px, hand-set pair. 52px leaves
                     ~4% margin: "Bad influence." (italic, 6.25em) fits 320px at 54px with -0.02em tracking */
  --label: 0.75rem;         /* 12px  default label                              */
  --label-floor: 0.6875rem; /* 11px  absolute minimum, decorative tags only      */

  /* ---------- FAMILIES: metric-matched fallbacks listed first ---------- */
  --font-display: 'Bodoni Moda', 'Bodoni Moda Fallback', 'Bodoni 72', Didot, 'Times New Roman', serif;
  --font-body:    'DM Sans', 'DM Sans Fallback', system-ui, sans-serif;
  --font-mono:    'Space Mono', 'Space Mono Fallback', ui-monospace, monospace;

  /* ---------- ROLES: weight size/leading family travel together; tracking beside ---------- */
  --t-hero:  500 var(--step-hero)/1.1  var(--font-display);  --t-hero-track:  -0.02em;
  --t-h1:    500 var(--step-5)/1.1     var(--font-display);  --t-h1-track:    -0.015em;
  --t-h2:    500 var(--step-4)/1.15    var(--font-display);  --t-h2-track:    -0.01em;
  --t-title: 500 var(--step-2)/1.2     var(--font-display);  --t-title-track: -0.01em;  /* + font-optical-sizing:none */
  --t-price: 600 var(--step-1)/1.2     var(--font-body);     --t-price-track: 0;        /* + tabular-nums */
  --t-body:  400 var(--step-0)/1.5     var(--font-body);     --t-body-track:  0;
  --t-meta:  400 var(--step--1)/1.45   var(--font-body);     --t-meta-track:  0;
  --t-label: 400 var(--label)/1.3      var(--font-mono);     --t-label-track: 0.08em;   /* + uppercase */

  /* ---------- SPACING: the covered grid, named by px; two fluid tokens ---------- */
  --sp-4: 0.25rem; --sp-8: 0.5rem; --sp-12: 0.75rem; --sp-16: 1rem; --sp-24: 1.5rem;
  --sp-32: 2rem;   --sp-48: 3rem;  --sp-64: 4rem;    --sp-96: 6rem;
  --gutter:  clamp(1rem, 0.6842rem + 1.4035vw, 2rem);   /* 16 -> 32px, page side padding */
  --section: clamp(3rem, 2.0526rem + 4.2105vw, 6rem);   /* 48 -> 96px, between big sections */
}

/* USAGE. The `font` shorthand RESETS font-optical-sizing, font-variant-numeric,
   font-variation-settings, font-kerning and font-feature-settings to initial [V css-fonts-4 §font shorthand],
   so those declarations MUST come AFTER `font:`, and a child rule that sets `font:` undoes them.
   .hero       { font: var(--t-hero); letter-spacing: var(--t-hero-track); }
   .label      { font: var(--t-label); letter-spacing: var(--t-label-track); text-transform: uppercase; }
   .price      { font: var(--t-price); font-variant-numeric: tabular-nums; }
   .card-title { font: var(--t-title); letter-spacing: var(--t-title-track); font-optical-sizing: none; } */

/* ---------- FALLBACK FACES (section 7) ---------- */
@font-face { font-family: 'DM Sans Fallback';     src: local('Arial'), local('Liberation Sans');
  size-adjust: 104.53%; ascent-override: 94.90%;  descent-override: 29.66%; line-gap-override: 0%; }
@font-face { font-family: 'Bodoni Moda Fallback'; src: local('Times New Roman'), local('Liberation Serif');
  size-adjust: 114.22%; ascent-override: 98.50%;  descent-override: 35.02%; line-gap-override: 0%; }
@font-face { font-family: 'Space Mono Fallback';  src: local('Courier New'), local('Liberation Mono');
  size-adjust: 101.98%; ascent-override: 109.82%; descent-override: 35.40%; line-gap-override: 0%; }
```

One-line rationale per token:

| Token | Why | Source |
|---|---|---|
| 360 to 1500 viewports | 360 is Utopia's default min; 1500 is the site's own container cap, so type stops growing where layout does | [V] utopia-home nav params `c=360,18,1.2,1240,20,1.25`; [V] repo atmosphere.css:56 |
| ratio 1.2 to 1.25, base 16 to 18 | Utopia's default ratio pair, base moved from 18/20 to 16/18 to match Material body-large 16sp and Apple 17pt | [V] utopia-home, material-android-typography, apple-hig-typography |
| min and max in `rem` | `vw`-only text fails WCAG 1.4.4 (F94); the rem term keeps text-size settings working | [V] wcag-f94, utopia-blog-clamp |
| `--step-hero` as its own pair | Utopia ships a separate single-pair Clamp tool; a ratio scale would need 10+ steps | [V] utopia-blog-clamp, utopia-blog-fluid-type |
| label 12px, floor 11px | Apple 11pt min (12 on visionOS/watchOS), Material label-small 11sp; NN/g's 8pt (10.7px) is the loosest | [V] apple-hig-typography, material-android-typography, nng-low-contrast |
| tracking 0.08em on labels | Butterick 0.05 to 0.12em for caps, "particularly important at small sizes"; Tailwind `widest` 0.1em; mono already spaced | [V] butterick-letterspacing, tailwind-letter-spacing |
| -0.01 to -0.02em display | Apple New York: -0.010em at 20pt, -0.014em at 34 to 52pt, -0.016em at 70pt and up | [V] apple-hig-typography (New York table) |
| leading 1.1 / 1.15 / 1.2 | Apple Large Title 34/41 and Title 1 28/34 = 1.21; repo email playbook 1.1 for 28px+; Bodoni `normal` = 1.525 | [V] apple-hig-typography; [V] email-build-playbook §1.3; [RUN] hhea (2250+800)/2000 |
| body leading 1.5 | Butterick optimum 1.2 to 1.45 (170% "too loose"); 1.5 equals the WCAG 1.4.12 override, so overrides change nothing | [V] butterick-line-spacing, w3c-1-4-12 |
| `font-optical-sizing: none` on card titles | gives the font's default opsz 11, about 2x the auto hairline at 24px | [RUN] section 4; [V] css-fonts-4 |
| fallback overrides | `size-adjust = avgWidth(web)/avgWidth(fallback)`; `ascent = metric/(UPM x size-adjust)` | [V] chrome-font-fallbacks; inputs [V] capsize-metrics-4.4.0 |

---

## 1. Fluid type scales with `clamp()` (Utopia)

**Method [V].** Define a small-screen scale and a large-screen scale and let the browser interpolate by viewport width, so "H2 is always step 4" at any width (utopia-blog-fluid-type). The precomputed form is `clamp(min rem, intercept rem + slope vw, max rem)` with `slope = (max-min)/(maxVW-minVW)` and `intercept = -minVW x slope + min` (utopia-blog-clamp). Utopia itself warns clamp can interfere with a user's text-zoom preference and says to test thoroughly (same page).

**Parameters chosen [U choice, math RUN].** Viewports 360 to 1500. Ratio pair 1.2 to 1.25 (Utopia default pair), gentle on phones with a little more air on desktop. Hero outside the scale: a 12px label to 130px hero is a 10.8x span, 10+ steps at 1.25.

**Steps [RUN]** (`raw/computed-utopia-clamp.md`):

| Step | min to max px | clamp() | at 768 / 1024 |
|---|---|---|---|
| -1 | 13.3 to 14.4 | `clamp(0.8333rem, 0.8123rem + 0.0936vw, 0.9000rem)` | 13.7 / 14.0 |
| 0 | 16 to 18 | `clamp(1.0000rem, 0.9605rem + 0.1754vw, 1.1250rem)` | 16.7 / 17.2 |
| 1 | 19.2 to 22.5 | `clamp(1.2000rem, 1.1349rem + 0.2895vw, 1.4062rem)` | 20.4 / 21.1 |
| 2 | 23.0 to 28.1 | `clamp(1.4400rem, 1.3396rem + 0.4461vw, 1.7578rem)` | 24.9 / 26.0 |
| 3 | 27.7 to 35.2 | `clamp(1.7280rem, 1.5798rem + 0.6586vw, 2.1973rem)` | 30.3 / 32.0 |
| 4 | 33.2 to 44.0 | `clamp(2.0736rem, 1.8611rem + 0.9445vw, 2.7466rem)` | 37.0 / 39.4 |
| 5 | 39.8 to 54.9 | `clamp(2.4883rem, 2.1899rem + 1.3262vw, 3.4332rem)` | 45.2 / 48.6 |
| hero | 52 to 130 | `clamp(3.2500rem, 1.7105rem + 6.8421vw, 8.1250rem)` | 79.9 / 97.4 |

**Why 52px for the hero floor [RUN].** Advance widths summed at opsz 96, wght 500, no kerning: "Bad influence." (italic) is 6.246em, "Good taste." is 5.112em. In a 320px content box "Bad influence." fits at 51px (tracking 0) or 54px (-0.02em). The current phone rule `clamp(47px, 12.5vw, 86px)` already respects this.

**The WCAG catch. X verified, Y needs review.**
- Verified [V]: viewport-unit text can fail SC 1.4.4 (F94), and capped or vw-driven sizes may stop text reaching 200% (Roselli, updated 2025-10-20; Firefox caps zoom at 300%, Chrome goes higher). In this repo `atmosphere.css:284` (`9vw`) and `:360` (`12.4vw`) are bare-`vw` hero sizes.
- Computed [RUN]: on-screen text growth vs 100% zoom on a 1500px screen (zoom shrinks the viewport, so the vw term shrinks with it):

| Token | 200% zoom | 300% zoom | 500% zoom |
|---|---|---|---|
| body 16 to 18 | 1.85x | 2.71x | 4.44x |
| step 3 (h3) | 1.72x | 2.44x | 3.93x |
| step 5 (h1) | 1.64x | 2.28x | 3.62x |
| hero 52 to 130 | 1.21x | 1.42x | 2.00x |
| hero 80 to 130 | 1.49x | 1.99x | 3.08x |
| hero 86 to 130 (today's floor, simplified) | 1.55x | 2.11x | 3.31x |

- Reading: body and headings reach 2x by 300% zoom (inside Firefox's cap). The 52px hero does not (1.42x). Algebra: to hit 2x at 300% zoom, min >= 0.62 x max; at Chrome's 500%, min >= 0.40 x max. [U] The "max <= 2.5 x min" heuristic is familiar but I did not fetch a source for it.
- Needs review: whether very large headings are exempt from 1.4.4. Roselli links W3C issue #1671 on exactly this; I saw no resolution. The fix is a design call: wrap the hero on phones and raise the floor to 80px (zoom-safe, but "Bad influence." then needs two lines at 360px).

---

## 2. Body size floor: is 15px acceptable?

| Source | Says | Tag |
|---|---|---|
| WCAG 1.4.4 | No minimum size; only "resize to 200% without loss" | [V] w3c-1-4-4 |
| Apple HIG | iOS default 17pt, min 11pt; visionOS 17/12; watchOS 16/12; "custom font with a thin weight, aim for larger than the recommended sizes" | [V] apple-hig-typography |
| Material 3 | body-large 16sp, body-medium 14sp, body-small 12sp | [V] material-android-typography |
| Butterick | Web body text 15 to 25px; screens are read from farther with fewer pixels per row | [V] butterick-point-size |
| NN/g (2002) | Default "at least 10 point" (13.3px), relative sizes, let users resize | [V] nng-user-control-font-size |
| NN/g (2015) | "Use at least an 8-pt font" (10.7px) | [V] nng-low-contrast |
| Baymard (2026) | Very small default text "breeds mistrust"; testers wondered if illegibility was deliberate (no px figure given) | [V] baymard-mobile-app-trends |

**Verdict.** 15px is legal and inside Butterick's range, but under both platform defaults (Apple 17, Material 16). DM Sans at opsz 16 has x-height 0.502em vs Arial 0.519 [RUN on shipped file; Capsize metrics 4.4.0 for Arial], so it needs about 16.5px to match Arial 16px's 8.3px x-height. Use `1rem` minimum, fluid to 1.125rem, line-height 1.5 (Butterick's optimum tops out at 1.45; the current 1.6 is looser than needed).

X verified, Y needs review: NN/g's 8pt (2015) and 10pt (2002) are 10.7px and 13.3px, older than and below Apple and Material, so they are no basis for 15px. They are also in print points.

---

## 3. Small uppercase tracked labels

**Floor.** 11px (0.6875rem) is the lowest defensible number: Apple iOS min 11pt [V], Material label-small 11sp [V]. 12px (0.75rem) for any label a buyer needs (era, maker, condition, "sold"). Space Mono's cap height is 0.700em [RUN], so 11px caps are 7.7px tall and 12px caps 8.4px, larger than a 12px DM Sans lowercase x-height (about 6.1px at opsz 12) [RUN]. NN/g's summary of the MIT AgeLab study: uppercase beat lowercase for glanceable single words and the effect grows at small sizes, but it does not recommend all-caps for longer passages [V nng-glanceable-fonts]. So short labels only, never a sentence.

**Tracking.** Butterick: add 5 to 12% (0.05 to 0.12em) to all caps and small caps, "not absolute limits" [V butterick-letterspacing]. Tailwind `widest` = 0.1em [V]. The site's 0.14em is above that. Space Mono advances are fixed at 0.612em [V capsize-metrics, RUN], so the low half of the range is enough: **0.08em default, 0.06 to 0.12 allowed.** X verified (Butterick range), Y needs review (his range assumes proportional faces; I found no source for monospace caps).

**WCAG [V].**
- 1.4.4 Resize Text: no size floor, only 200% scaling without loss. Techniques list relative units (C12 percent, C14 em); F94 fails vw-only sizing. Use rem for font-size and em for letter-spacing so both follow the browser setting.
- 1.4.12 Text Spacing: a user may force line-height 1.5, paragraph gap 2em, letter-spacing 0.12em, word-spacing 0.16em with no loss of content. Forced 0.12em adds 0.04em over 0.08em (about +5% label width). Pills, tags and card overlays need `min-height` and padding, not fixed `height` plus `overflow: hidden` plus `nowrap`.
- Contrast (1.4.3) on the repo palette [RUN]: `--text` #f6efdf on `--paper` #422831 = 11.61:1, `--muted` #d1bdb8 = 7.40:1, `--rust` #e5a6b4 = 6.61:1, all pass 4.5:1. On `--wall` #652b40: muted 5.92:1, rust 5.29:1, still pass. `--line` #79545e is 2.05:1: borders only, never text.

---

## 4. Didone optical sizing: Bodoni Moda below about 24px on burgundy

**How browsers map `opsz` [V].** CSS Fonts 4: with `auto`, UAs "are expected to supply a value for the opsz axis which is close to the used value for font-size"; experiments suggest font-size alone works best; UAs must clamp to the font's range and must not synthesise optical sizing. Google Fonts Knowledge: the axis value should match the size in print points, "although browsers instead match it to the CSS px unit". MDN: small sizes get "thicker strokes and larger serifs", large sizes "more contrast between thicker and thinner strokes"; `auto` is default, Baseline since March 2020. `none` means no glyph-shape change, i.e. the font's default instance. For Bodoni Moda that is **opsz 11** [RUN fvar: wght 400/400/900, opsz 6/11/96]. So today 23px text gets opsz 23 and the 130px hero gets opsz 96.

**What `opsz` does to hairlines [RUN].** I instantiated the shipped `bodoni-moda-normal-latin.woff2`, rasterised "o" at 4000px and read the thinnest run. In 1/1000 em:

| opsz | 6 | 11 | 16 | 24 | 36 | 48 | 96 |
|---|---|---|---|---|---|---|---|
| hairline | 36 | 19 | 13 | 9 | 4.5 | 3.5 | 2 |
| stem | 100 | 103 | 104 | 104 | 105 | 105 | 105 |
| stroke contrast | 2.8 | 5.4 | 8 | 11.6 | 23 | 30 | 52 |

Stem is about 0.105em at every opsz; the hairline shrinks as size grows and the product stays nearly constant. Hairline in CSS px:

| font-size | 11 | 14 | 16 | 20 | 24 | 32 | 48 | 96 | 130 |
|---|---|---|---|---|---|---|---|---|---|
| auto (opsz = size) | 0.21 | 0.22 | 0.21 | 0.21 | 0.22 | 0.19 | 0.17 | 0.19 | 0.26 |
| opsz 11 (`font-optical-sizing: none`) | 0.21 | 0.27 | 0.30 | 0.38 | 0.46 | 0.61 | 0.91 | 1.82 | 2.47 |
| opsz 6 forced | 0.40 | 0.50 | 0.58 | 0.72 | 0.86 | 1.15 | 1.73 | 3.46 | 4.68 |

(opsz-11 row = 0.019 x size, from the table above.) Weight does not help: hairline is the same within 0.5/1000 em at wght 400, 500, 600 and 700; only stems thicken (105, 118, 131, 150 at opsz 96). The `@font-face` declares `400 500` only.

**Dark burgundy [RUN, model-dependent].** A 0.2px hairline covers about 20% of a pixel row at 1x. Cream #f6efdf blended into paper #422831 at 20% coverage is #665054, 1.80:1 against the paper; at 50% coverage 4.13:1. This is a linear-blend model; real rasterisers (DirectWrite, CoreText stem darkening, subpixel) differ, so treat it as direction, not spec. 2x and 3x screens double and triple coverage. Apple says use larger sizes with thin custom fonts [V]; NN/g found larger, wider, uppercase text wins for glanceable reading [V]; Baymard says small italic has "too little weight to provide proper contrast" [V baymard-highlighting-text].

**Verdict: opsz is not enough, and a blanket ban is too blunt.**
- **Ban** Bodoni under 20px, and for anything transactional (price, size, condition, buttons). Those are DM Sans or Space Mono.
- **20 to 31px (card titles):** `font-optical-sizing: none`. Doubles the hairline at 24px (0.22 to 0.46px) for a sturdier, lower-contrast cut. The hairline is [RUN]; "looks right" is [U], so check on a real phone.
- **32px and up:** `auto`. Stems and serifs carry recognition; 0.2px hairlines read as elegant, not missing.
- **Italic:** same axes [RUN]; no Bodoni italic under 28px.
- The spec says authors "should not" use `font-variation-settings` for registered axes, but `font-optical-sizing` offers only auto/none [V css-fonts-4]. Google's own page shows `font-variation-settings: 'opsz' 16` to pin a value [V gfk-optical-size-axis]. Prefer `none`; use `"opsz" 6` only for a deliberate small-Bodoni exception.

---

## 5. Tracking and leading

**Tracking, large display serif [V].** Apple's tracking table for New York (their serif with optical sizes), em:

| pt | 12 | 15 | 20 | 24 | 34 | 48 | 70 | 96 | 140 |
|---|---|---|---|---|---|---|---|---|---|
| tracking | +0.006 | 0 | -0.010 | -0.011 | -0.014 | -0.014 | -0.016 | -0.016 | -0.016 |

Even a proper optical-size serif tightens only 1 to 1.6%, and goes positive below 15pt (+0.040em at 6pt) (apple-hig-typography). Butterick: remove letterspacing from lowercase at large sizes [V]. The tokens follow the Apple curve (-0.01 / -0.015 / -0.02em). **Discrepancy: `atmosphere.css:72-75` sets the hero at `letter-spacing: -.055em`, 3.4x Apple's New York at the same size. X verified, Y needs review.** If kept, treat -0.03em as the ceiling and check "Good taste." / "Bad influence." at 1x for touching serifs. The brief's audit also found px letter-spacing as large as -11px; px does not scale with `clamp()`, so use em everywhere.

**Leading, display [V + RUN].**
- Apple iOS Large (default): Large Title 34/41 = 1.21, Title 1 28/34 = 1.21, Title 2 22/28 = 1.27, Title 3 20/25 = 1.25.
- Repo email playbook §1.3: 1.1 for display at 28px and up, 1.55 body, 1.4 caption.
- Butterick: optimum 120 to 145% for text; 110% is "too tight" for text (a body rule, not a display rule).
- Bodoni Moda `line-height: normal` = (2250+800)/2000 = **1.525** [RUN hhea]. At 60 to 130px that is very loose, so set an explicit unitless leading.
- Recommend 1.1 hero and h1 (the site's 1.12 is fine), 1.15 h2, 1.2 for 2-line card titles. Apple's ratios stop at 34pt; the downward trend with size is convention [U]. Below 1.05 risk descender/ascender collisions (the italic "f" in "influence").

---

## 6. Product card typography

**Already in the repo (not redone).** `research/cutouts/raw/03-baymard-listitem.md`: 64% of sites fail to show the same attributes consistently across list items; 40% fail to make list-item info elements "visually distinct", using "font size, capitalization, color variations, and bold or italic styles", even as a single line. Nordstrom's separate top-line brand is the model for a maker/era line. `03-baymard-plp.md` adds "present essential information like price and key product attributes directly on the list page".

**New [V].**
- NN/g *Anatomy of a List Entry* (2016-04-10): prioritise attributes, then "emphasize key attributes by increasing font size and weight or using a unique or dark color"; an entry where name, price and inventory share one style has no information hierarchy (nng-list-entries).
- NN/g *Scanning Patterns… Optimized for the Current Task* (2017-03-19), price-scan task: prices were easy to find because of "price size larger than all the text items in the content area", surrounding whitespace, short numbers, bold font and the same price position in each entry (nng-eyetracking-tasks-scanning).
- NN/g *Cards* (2016-11-06): in cards, price is hard to find because the layout is not predictable; a vertical list is better for price scanning and comparison; use consistent visual treatment for items that will be compared (nng-cards-component). Our grid is cards, so the rule becomes: **price sits in the same corner of every card, same size, same weight.**
- NN/g *Ecommerce listing pages* (2018-08-12): concise names with meaningful characteristics, price on the listing (nng-ecommerce-listing-pages).
- Baymard (2026): very small default text breeds mistrust; text overlaid on images is less readable (baymard-mobile-app-trends). No px figure is given.

**Proposed hierarchy** (all from the token block):

| Line | Role | Size | Weight / colour | Why |
|---|---|---|---|---|
| Maker, era, place | `--t-label` Space Mono caps | 12px, 0.08em | 400, `--muted` | Baymard: separate top line for brand; caps hold at 12px |
| Title | `--t-title` Bodoni | 23 to 28px | 500, `--text` | Brand voice; big enough for hairlines with opsz 11 |
| Price | `--t-price` DM Sans, tabular | 19 to 22.5px | **600, `--text`** | Only 600 weight on the card; fixed corner; NN/g price emphasis |
| Size / condition | `--t-meta` DM Sans | 13.3 to 14.4px | 400, `--muted` (7.4:1) | Functional, must stay >= 13px; not a 10px mono tag |

**X verified, Y needs review.** NN/g: price larger than everything else. A one-of-a-kind vintage shop sells the story before the price, and a 23 to 28px Bodoni title will outweigh a 19 to 22px price in a photo-heavy card. I kept price smaller than title but heavier and brighter. If conversion matters more than mood, raise price to `--step-2`. I found no Baymard or NN/g study testing a Didone title against a sans price, so this is [U].

---

## 7. Font loading and CLS

**Current state [V repo].** `site/assets/fonts/fonts.css`: all four faces `font-display: swap`, self-hosted woff2 (Bodoni normal 46 KB, italic 54 KB, DM Sans 63 KB, Space Mono 17 KB). `storefront.html` preloads both Bodoni files only; DM Sans, the body face, is not preloaded.

**Vendor docs [V].**
- `swap`: extremely small block period, infinite swap period (mdn-font-display). Swapping causes CLS "when a web font and its fallback font take up different amounts of space" (webdev-font-best-practices).
- Fix: `size-adjust`, `ascent-override`, `descent-override`, `line-gap-override` on a local fallback face (chrome-font-fallbacks, webdev-size-adjust, mdn-size-adjust, mdn-ascent-override). Formulas: `size-adjust = avgCharWidth(web)/avgCharWidth(fallback)`; `ascent-override = ascent/(UPM x size-adjust)`, same for descent and line-gap.
- Preload takes resources from other loads, ignores `unicode-range`, and should be limited to the most important fonts; with external stylesheets it is very effective for early discovery (webdev-font-best-practices).

**Tools.** Capsize: `@capsizecss/metrics` 4.4.0 has `bodoniModa`, `dMSans`, `arial`, `timesNewRoman`, `courierNew`, `spaceMono` [V]. Fontaine ("Automatic font fallback based on font metrics", pure CSS output) is a bundler transform (Vite and Astro examples in its README; Nuxt module per Chrome's article) [V]; its README reports CLS 0.24 to 0.054 on its own playground (their number, not ours). Chrome also links a CSV of overrides for every Google Fonts file [V font-fallbacks-dataset-readme].

**Our numbers [RUN].** Inputs [V Capsize 4.4.0]: Bodoni Moda xWidthAvg 928/2000, ascent 2250, descent -800, gap 0; DM Sans 466/1000, 992, -310, 0; Space Mono 612/1000, 1120, -361, 0; Arial 913/2048; Times New Roman 832/2048; Courier New 1229/2048; Georgia 913/2048. Results are the `@font-face` block above. Georgia alternative for Bodoni: size-adjust 104.08%, ascent 108.09%, descent 38.43%.

Checks on the shipped files [RUN]:
- My frequency-weighted widths (a-z plus ~17.5% space): Bodoni 0.4619em, DM Sans at opsz 14 0.4674em, vs Capsize 0.464 and 0.466, within 0.5%.
- Metrics are OS-consistent: both fonts set USE_TYPO_METRICS and hhea equals typo (Bodoni 2250/-800/0, DM Sans 992/-310/0), so one override set works on Mac and Windows (Chrome's per-OS exception does not apply).
- Width drift with optical size: Bodoni at opsz 96 averages 0.4560em vs 0.4619 at opsz 11 (-1.3%), so overrides computed at the default instance stay within ~1.3% at hero size. DM Sans at opsz 40 is 0.4157em (-12%) but body text uses opsz 16 to 18.

**Worth it?** Yes for Bodoni and DM Sans. Bodoni is 14.2% wider than Times New Roman, so any hero or h2 line that wraps in the fallback re-wraps on swap; DM Sans is 4.5% wider than Arial. Cost: 15 lines, no dependency, no build step. Skip fontaine and Capsize as dependencies (`site/build.mjs` is custom). Space Mono is optional (short labels). Also add `<link rel="preload" as="font" ... dm-sans-normal-latin.woff2 crossorigin>`. Limits: `local('Arial')` does not exist on Android; Liberation names are the [U] same-metrics fallback on Linux/ChromeOS, and on Android the stack falls through to `system-ui` unadjusted. I did not run Lighthouse or a throttled layout-shift trace; run one before and after.

---

## Spacing (what this pass adds)

The 4 to 96px grid is [V from prior research]. New here:
- **Snap map for the 70 distinct values:** round each to the nearest of 4/8/12/16/24/32/48/64/96; anything 96 to 130px becomes `--section`.
- **Two fluid tokens** (`--gutter` 16 to 32px, `--section` 48 to 96px) so page rhythm tracks the type. Same Utopia formula and range [RUN]. Inside components, spacing stays fixed.
- **Label and tag padding in em** (for example `0.4em 0.7em`) so 1.4.12 overrides and rem scaling do not clip pills. [U]

## Open items and not fetchable

- **Ricky, hero:** keep the 52px phone floor (fits one line, 1.42x at 300% zoom) or raise to 80px and wrap (zoom-safe).
- **Verify by eye** on a real phone and a 1x Windows monitor: Bodoni 24 to 28px with `font-optical-sizing: none` vs auto; hero at -0.02em vs today's -0.055em.
- **Unfetchable:** Material 3 / 2 sites and the Google Fonts specimen page (JS-rendered, empty). Material sizes came from the Android docs on GitHub (no tracking or leading); Material's `overline` 0.15em is not used. The old Lighthouse font-size audit page does not state its px threshold in the fetched text, so it is not cited. Smashing's "16px" article appeared only in search snippets, so it is not cited.
- **Dates and gating:** NN/g items are 2002 to 2018 and in print points; Baymard's detail pages are Premium-gated beyond the excerpt already in the repo.

## Source index (fetched 2026-10-29; raw copies in `raw/`)

| Short name | URL |
|---|---|
| utopia-blog-clamp / -fluid-type / -home | https://utopia.fyi/blog/clamp/ · /blog/designing-with-fluid-type-scales/ · https://utopia.fyi/ |
| wcag-f94-viewport-units | https://www.w3.org/WAI/WCAG22/Techniques/failures/F94 |
| w3c-1-4-4-resize-text / w3c-1-4-12-text-spacing | https://www.w3.org/WAI/WCAG22/Understanding/resize-text.html · /text-spacing.html |
| roselli-responsive-type-zoom | https://adrianroselli.com/2019/12/responsive-type-and-zoom.html |
| apple-hig-typography | https://developer.apple.com/design/human-interface-guidelines/typography (read via its JSON endpoint) |
| material-android-typography | https://raw.githubusercontent.com/material-components/material-components-android/master/docs/theming/Typography.md |
| butterick-point-size / -letterspacing / -line-spacing | https://practicaltypography.com/point-size.html · /letterspacing.html · /line-spacing.html |
| tailwind-letter-spacing | https://tailwindcss.com/docs/letter-spacing |
| mdn-font-optical-sizing | https://developer.mozilla.org/en-US/docs/Web/CSS/font-optical-sizing |
| gfk-optical-size-axis | https://fonts.google.com/knowledge/glossary/optical_size_axis |
| css-fonts-4-spec | https://www.w3.org/TR/css-fonts-4/ |
| bodoni-moda-github-readme | https://raw.githubusercontent.com/indestructible-type/Bodoni/master/README.md |
| chrome-font-fallbacks | https://developer.chrome.com/blog/font-fallbacks |
| webdev-size-adjust / -font-best-practices / -optimize-cls | https://web.dev/articles/css-size-adjust · /font-best-practices · /optimize-cls |
| mdn-size-adjust / -ascent-override / -font-display / -clamp | https://developer.mozilla.org/en-US/docs/Web/CSS/@font-face/size-adjust · /ascent-override · /font-display · https://developer.mozilla.org/en-US/docs/Web/CSS/clamp |
| capsize-metrics-4.4.0 | https://unpkg.com/@capsizecss/metrics@4.4.0/entireMetricsCollection/<font>/regular/index.cjs |
| capsize-home / fontaine-pkg-readme / font-fallbacks-dataset-readme | https://seek-oss.github.io/capsize/ · https://raw.githubusercontent.com/unjs/fontaine/main/packages/fontaine/README.md · https://raw.githubusercontent.com/khempenius/font-fallbacks-dataset/main/README.md |
| nng-list-entries / -eyetracking-tasks-scanning / -cards-component / -ecommerce-listing-pages | https://www.nngroup.com/articles/list-entries/ · /eyetracking-tasks-efficient-scanning/ · /cards-component/ · /ecommerce-homepages-listing-pages/ |
| nng-glanceable-fonts / -low-contrast / -user-control-font-size / -legibility | https://www.nngroup.com/articles/glanceable-fonts/ · /low-contrast/ · /let-users-control-font-size/ · /legibility-readability-comprehension/ |
| baymard-mobile-app-trends / -highlighting-text | https://baymard.com/blog/mobile-app-ux-trends · https://baymard.com/blog/highlighting-text-online |
| local runs | `raw/computed-fonttools-measurements.md`, `raw/computed-utopia-clamp.md`, `raw/scripts/` |
| repo files read | email-build-playbook §1.3/1.4/1.16; dashboard 07 §4.2-4.3; cutouts 03-baymard-listitem and -plp; site/assets/fonts/fonts.css; site/atmosphere.css |
