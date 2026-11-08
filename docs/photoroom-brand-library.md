# Photoroom Brand Library for Holliewood & Vine

Written 2026-11-08. Ricky asked to "set up all of this" at
https://app.photoroom.com/brand-library/assets. The Claude Chrome extension was not connected that
session, so the Photoroom side is not done; everything below is ready to upload in one sitting.
Every Photoroom fact here was read from Photoroom's own pages on 2026-11-08 (files in `research/`,
named `help.photoroom.com_*` and `www.photoroom.com_pricing-*`).

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
| Instagram | `@holliewoodandvine` is the planned handle. Nobody has confirmed it is ours (`social-manual.md`, item 1). Leave blank until Ricky claims it. |

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
6. **Brand info**: name, description, website. Instagram only once the handle is confirmed.
7. Screenshot the finished library into `assets/brand/` and note the date here.

With the Claude Chrome extension connected (claude.ai/chrome, signed in as the same account),
Claude can do steps 2 to 6 from this file.
