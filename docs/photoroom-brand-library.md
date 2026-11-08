# Photoroom Brand Library for Holliewood & Vine

Set up in Photoroom on 2026-11-08 (Space "Holliewood & Vine", Pro plan) by Claude through the Chrome
extension, from the kit below: three logos, one seven-color palette named "Holliewood & Vine", eight font
styles (Bodoni Moda Regular, Medium, Italic; DM Sans Regular, Medium, Bold; Space Mono Regular, Bold; all
from Photoroom's built-in list, so the TTFs were not needed) and Brand info with name, description, website
and brand style. Instagram `@holliewoodandvine` was added after Ricky confirmed the handle. The Brand style field had a stray
"jones new york" in it and was replaced. Proof: `assets/brand/photoroom-brand-library-2026-11-08.jpg`.
Every Photoroom fact here was read from Photoroom's own pages on 2026-11-08 (files in `research/`,
named `help.photoroom.com_*` and `www.photoroom.com_pricing-*`).

**Brand info quirk (2026-11-08):** the Brand info form comes back empty after a reload even though
Save worked. Verified by watching the request: Save sends a PATCH to
`api.photoroom.com/v1/brand-kits/<id>/` and the 200 response carries `brandName`, `brandDescription`,
`brandWebsiteUrl`, `brandInstagramHandle` (`holliewoodandvine`) and `brandMoreInfo` with our values. So
the data is on Photoroom's side; the page just does not read it back into the form. Do not retype it
on sight of empty fields; if a future session needs proof, hook `fetch` and press Save once more.
Re-checked 2026-11-08 07:52 UTC after Ricky saw the tab empty: logos (3), palette (7) and fonts (8) are
all present; only Brand info reads back blank. The page fills the form from a client-side store loaded
once at start-up, and no later tab switch, remount or focus refetches it, so a Save is never shown back
on the same visit or the next. Each Save still returns 200 with every field. If the values must be
re-entered, set them through the DOM (React setter plus an input event) and click Save through the DOM;
screen coordinates drift with the window size and a missed click looks like a save.

## What Photoroom's Brand Library takes (verified)

Source: help article 10208814 "What is a Brand Library?", and the Web App articles 17731485 (import
from website), 17731971 (logos), 17741971 (fonts), 17744222 (colors).

- One Brand Library per Space. Sections: Brand info (name, description, website, brand style),
  Logos, Colors (palettes), Fonts, Models (AI Fashion Models), Backgrounds, Cutouts.
- **Plan gate:** the pricing page's feature table lists Brand Library as Included on Pro, Max and
  Ultra. It is not a Free feature, and the terms license Free Accounts for personal, non-commercial
  use only (see `ebay-photo-studio.md`).
- **Import from website** (Web App only) pulls logos, a color palette, Google fonts, brand info and
  an Instagram handle from a URL. If the banner is missing, open any design, choose Brand Library in
  the editor and use the "Import your brand" box at the top, or use a private window.
- **Logos:** Logos > Add > choose the file. Photoroom also builds a palette from the logo's colors.
- **Colors:** Colors > + Add > Create your own > rename the palette (... menu) > + per color.
- **Fonts:** Fonts > Add + > search the built-in list (many but not all Google fonts) or Upload
  your font. Uploads must be **OTF, TTF or WOFF** (WOFF2 is not listed). Each style uploads
  separately, and the Regular / Italic / Bold switches must be on or nothing is added.

## The kit

### Brand info

| Field | Value |
|---|---|
| Name | Holliewood & Vine |
| Description | Vintage with a past. Lighting, furniture, fashion, rugs and beautiful oddities from Southwest Florida, sold online and styled by Hollie. |
| Website | https://hollywood-and-vine-vintage.allstatecoop.chatgpt.site/ |
| Instagram | `@holliewoodandvine`, confirmed by Ricky 2026-11-08 and entered in Photoroom the same day. |

The description is a draft from the site's meta description; Hollie can rewrite it in the app.

### Logos (`assets/brand/`, rendered from the live site's Bodoni Moda woff2 with headless Chrome)

| File | Use |
|---|---|
| `holliewood-and-vine-wordmark-cream.png` | 1605 by 235, transparent. On burgundy or dark photos. |
| `holliewood-and-vine-wordmark-burgundy.png` | 1605 by 235, transparent. On white listing shots and cream. |
| `holliewood-and-vine-mark-1024.png` | 1024 square, the site favicon: cream H with a pink plus on burgundy. Avatar and watermark. |

The wordmark is the site's header wordmark: Bodoni Moda 400, "& Vine" italic, letter-spacing scaled
from the site's -1.5 px at 28 px.

### Colors (one palette, name it "Holliewood & Vine")

| Name | Hex | Where it comes from |
|---|---|---|
| Burgundy | `#451c2b` | `--burgundy`, the walls and the page background |
| Burgundy deep | `#321520` | `--burgundy-deep` |
| Cream | `#f6efdf` | `--cream`, text on burgundy |
| Neon pink | `#ff2f92` | `--neon`, the "do it for the plot" sign |
| Rose | `#e5a6b4` | the favicon's plus sign |
| Muted | `#74645e` | `--muted`, secondary text on cream |
| Listing white | `#ffffff` | eBay product backgrounds; photo framing only, never the page |

### Fonts

| Family | Role | Files if Photoroom's list lacks it (`assets/brand/fonts/`, SIL OFL, from google/fonts) |
|---|---|---|
| Bodoni Moda | display and wordmark; italic for "& Vine" | `BodoniModa[opsz,wght].ttf`, `BodoniModa-Italic[opsz,wght].ttf` |
| DM Sans | body | `DMSans[opsz,wght].ttf`, `DMSans-Italic[opsz,wght].ttf` |
| Space Mono | labels and prices | `SpaceMono-Regular.ttf`, `-Bold`, `-Italic`, `-BoldItalic` |

Search Photoroom's built-in list first; all three are Google fonts. Upload the TTFs only if a search
finds nothing. The Bodoni Moda and DM Sans files are variable fonts; if Photoroom rejects them,
Google Fonts' download zip has static instances.

### Backgrounds and cutouts (optional, later)

- A pure white background saved for eBay batches (help article 17887674).
- The burgundy wall and the neon sign as backgrounds for social crops, from `assets/photos/`.
- The three logos saved as cutouts once they exist as layers.

## Doing it (about ten minutes once signed in)

1. Open https://app.photoroom.com, pick the Space, open **Brand Library**. If the page shows a
   Free plan, stop: the library needs Pro or above.
2. Try **Import from website** with the site URL. Review the Profile it detects. Add it, then
   prune the palette it guessed down to the table above.
3. **Logos > Add**: upload the three PNGs.
4. **Colors > + Add > Create your own**, rename to "Holliewood & Vine", add the seven hexes.
   Delete the auto palettes Photoroom made from the logos if they clutter the list.
5. **Fonts > Add +**: search Bodoni Moda, DM Sans, Space Mono; switch on Regular and Italic (and
   Bold for Space Mono). Upload the TTFs only for a family the search cannot find.
6. **Brand info**: name, description, website. Instagram handle `holliewoodandvine` (no @).
7. Screenshot the finished library into `assets/brand/` and note the date here.

With the Claude Chrome extension connected (claude.ai/chrome, signed in as the same account),
Claude can do steps 2 to 6 from this file.
