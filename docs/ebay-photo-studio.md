# eBay photo studio: what we are doing and why

**Status (2026-11-07):** decisions from the two Sonnet sweeps in `research/ebay-photo-studio-2026-11-07/` (21 lanes, 30 claim checks; the verdicts are in that folder's README) plus tests on Ricky's four example photos in this cloud session. The script is built and tested on CPU here; the Windows install and the first GPU run happen when Ricky is at the PC (`docs/ebay-photo-studio-handoff.md`). Prices for gear are asking prices seen in search results that day, not opened pages, and are marked so. Every eBay rule quoted below comes from eBay pages fetched 2026-10-30 (`research/ebay-clothing-photos-2026-10-30/`).

## 1. The short answer

- **Photo 1 is the real garment on a real, visible form, on pure white.** The white comes from our own script, which only removes the room behind the item and never redraws a pixel. Then the back, one in-room burgundy shot (the Etsy and Shopify cover), label, fabric, closures, every flaw, and a measurements card. Eight to twelve photos per listing, square, 1600 px.
- **Close-ups stay exactly as shot.** Labels, flaws and fabric are the trust shots on vintage; the script leaves them alone and only resizes.
- **No ghost mannequin by default, no AI try-on, no AI-generated scenes.** Nothing we found shows pre-owned vintage sellers using invisible-mannequin shots, the visible vintage form is on-brand, and every AI route either carries a non-commercial licence or can quietly change the garment, which on used goods is a returns and policy risk.
- **The program is right.** rembg with the BiRefNet model (both MIT, free, local, runs on the RTX 4060 Ti) cut the dress off a grey Jeep door cleanly. The one failure, a notch of black frame against a dark pegboard, is fixed by a rectangle repair we added and tested. Six models were compared on that print; the other five were worse.
- **The light is the real limit now, not the software.** The cut-outs are clean; the washed-out navy in Ricky's dress photo came from hard sun. A form, even light and a backdrop a step behind are the next purchase.

## 2. What the tests showed (measured here, 2026-11-07)

Inputs: Ricky's four phone photos (`assets/examples-2026-11-07/`) and the October room photos. Outputs and sheets: `research/ebay-photo-studio-2026-11-07/test-results/`.

| Photo | Result | Report line |
|---|---|---|
| Navy silk dress, front, hanging on a Jeep door in sun | Clean cut, hanger kept, collar and pink button intact | 18.4 s, 99.9% of pixels untouched, 98% solid |
| Same dress, back | Clean cut | 18.6 s, 99.9%, 98% |
| Framed shisa print on a dark pegboard, plain cut | Frame lost a notch at the top and a sliver on the right; glass reflections stay | 21.9 s, 100%, 92% |
| Same print with the rectangle repair | Frame complete, filled with the photo's own pixels | 22.9 s, 3.1% of the outline reclaimed |
| Dressed form in the burgundy room | Form and jacket came off the wall as one object, chains intact | 17.7 s |

Timing is this cloud box: four CPU cores, no graphics card, about 18 to 23 seconds a photo. On the RTX 4060 Ti the same model runs on the GPU; the handoff has the install and the check. The model comparison on the print: `birefnet-general` was the only one of six that kept the whole frame; `birefnet-dis` and `birefnet-massive` dropped the frame, `isnet-general-use` and `u2net` kept only the artwork, and the lite model smeared the right edge. A general morphological "closing" did not fix the notch; the convex-hull repair did.

The bench (lane 19, three models on nine photos, every sheet judged by eye): `birefnet-general` never failed. The lite model is 35 to 40 percent faster and matches general on clean garment shots but loses thin frame bars and shelf contents. `isnet-general-use` failed on seven of nine, including washing the Neiman Marcus label to white. So the default stays general; lite is only for a laptop and clean garments.

Two things to change on the shoot side, seen in the photos: take the price tag off before shooting (it stayed in the cut, as the chandelier's tag did in October), and shoot labels in shade so the fabric is not blown out.

## 3. The rules we are inside

eBay, quoted from eBay's own pages (fetched 2026-10-30):

- "You can add up to 24 pictures." The first is the search thumbnail: "Make it your best shot, with your item centered and fully visible."
- "Images should have a minimum resolution of 500 x 500 pixels but we recommend images that are about 1600 x 1600." The picture policy words the floor differently: "at least one photo that is 500 pixels on the longest side". "photos in a 1:1 or 16:9 aspect ratio look best". "maximum 12MB each" (per file). Accepted: "JPEG, PNG, GIF, TIFF, BMP, WEBP, HEIC, or AVIF".
- "White backgrounds are generally best, but for shiny or reflective items like a piece of jewelry, a darker background may work better." eBay's clothing page: "Use a white or light-colored background for darker clothes, and a black or dark background for lighter clothes."
- Not allowed: "Photos that don't accurately represent the item", "Stock photos for used, damaged, or defective items", "Photos with added borders", "Photos with added text, artwork or marketing material", "Watermarks of any type, including those used for ownership attributions". "You can't use a catalog or stock photo if you're listing an item as used."
- eBay's own listing tool has a Background button that will "automatically replace the background with a solid white color"; the app adds AI scenes and says "Try to only use this option for a few photos". A white cut-out of our own photo is therefore the same thing eBay offers, not a stock photo.
- Flaws: "show clear, closeup images of them". Pre-owned clothing grades are Excellent, Good and Fair, and "every imperfection must be shown and described".

Etsy and Shopify (from `research/cutouts/01-channel-image-rules.md`, fetched 2026-10-27): Etsy's help page says "If a file contains transparency, the transparent parts of the image will appear black on Etsy" and wants "at least one unedited photo of the actual item against a real background"; 2000 px recommended, up to 20 photos. Shopify: "For square product images, a size of 2048 x 2048 px usually displays best". eBay's handling of transparency is unverified, so the safe rule is flat JPEG everywhere: the script writes a 1600 square for eBay, a 2048 square master for Shopify, and keeps the transparent PNG for our own site only. eBay's current page on AI-edited photos could not be opened from here; the picture policy we hold says nothing about AI and everything about accuracy.

## 4. The tools

**Use:**

- **rembg 2.0.87** (MIT, PyPI 2026-11-06; Python 3.12 is the safe pick, since its README caps at 3.14 and onnxruntime's wheels decide) running the **BiRefNet general** model. The weights are MIT on the GitHub LICENSE and on the Hugging Face cards of every variant we would use (one untagged research checkpoint aside), and MIT permits selling and sublicensing. This is `tools/cutout/cutout.py`. Always with the model named: rembg's default model is Bria's RMBG-2.0, and its README says "RMBG-2.0 is released under a BRIA license that requires a paid agreement for commercial use"; the script refuses it.
- **The rectangle repair** for frames, mirrors, boxes and books (automatic from the file name, or `--rect`).
- **Hugging Face Spaces as the no-install backup:** `not-lain/background-removal` (BiRefNet, MIT, 2,984 likes) gives a transparent PNG to flatten onto white at home; `ZhengPeng7/BiRefNet_demo` offers the HR and matting variants for lace and fringe. Avoid `Xenova/remove-background-web`: it runs RMBG-1.4, which its card calls "source-available ... for non-commercial use".
- **Later, for lace, fringe, feathers and fur:** BiRefNet HR-matting at 2048 px through the `transformers` route on the GPU (lane 21 has the snippet). rembg cannot load that variant by name.

**Do not use:**

- Bria RMBG-1.4 and RMBG-2.0 (non-commercial), and any tool built on them.
- remove.bg: "The standalone website will no longer be available from 1 December 2026" (fetched 2026-10-27).
- AI virtual try-on (IDM-VTON, CatVTON, OOTDiffusion, FitDiT): CC BY-NC or gated non-commercial licences, and the papers themselves admit texture distortion. Kolors' demo is a thin client to a private server. If a styling image is ever wanted, it goes last in the gallery, captioned as AI and not the item, or off eBay entirely.
- Upscalers on 12 MP phone photos headed for 1600 px: nothing to gain, and Upscayl describes itself as "guessing what the details could be". Downscale well, sharpen once lightly, done.
- eBay's in-app remover and AI scenes for clothing: seller reports (snippet-level) of tint, lost tools and forced backgrounds; use its White button only as a benchmark.

**Paid fallback, only if Ricky agrees:** Photoroom's API at "$0.02 per image" (the page saved 2026-10-27 says so and lists PNG, JPEG, WEBP or HEIC; one of two checkers could not re-find it, so re-check on the PC), on a paid plan because the free account is for personal, non-commercial use. Its single-photo ghost mannequin mode exists but regenerates pixels, so it would need a side-by-side check against the real garment before any listing uses it.

**Phone-only stopgap (unverified on device):** iPhone Photos lift-subject and the Files Quick Action "Remove Background" produce transparent PNGs; nothing built in fills white, so the PC pipeline stays the real route. Skip third-party shortcuts that upload photos to someone's server.

## 5. The shoot

**The form.** One adjustable, pinnable dress form with an adjustable pole for the daily work, plus the cream linen vintage-look form as the room piece that also appears in shots. For sizes 6 to 10, buy the smaller form and pad up with batting rather than a larger one and pin down. The form should be darker or cream, not bright white, so it separates from the backdrop. Pinning kit: binder clips at the back, tissue in shoulders and sleeves, transparent tape, pins, a black cloth under sheers. The paint-splattered form in the catalogue is a decor piece, not the working form. Which forms are still on hand after the move is an open question for Ricky.

Prices seen in search results on 2026-11-07, pages not opened: Dritz My Double about $155; an Etsy white linen form on a wooden base $125; Roxy linen forms $136 to $188; used Acme adjustable forms $50 to $250; Mannequin Mall French forms $183 to $305; an antique linen spindle-base form $375. No full-size pinnable form under $60 was confirmed.

**The light and backdrop.** The sources agree on one setup: two soft lights at 45 degrees, no flash, the form five or six feet in front of the backdrop so its shadow does not climb the paper, the paper curved down to the floor, and a third light on the backdrop only if the white reads grey. Same bulbs in every light, 5500 to 5700 K, CRI 90 or better. Pale garments go on a pale grey or dark backdrop per eBay's own clothing page, and the script whitens it. Cheapest tier (snippet prices): two Neewer 24-inch softbox kits $80 to $120, a 10 by 7 foot backdrop stand $30 to $46, a Savage 53-inch pure white paper roll $45, a phone tripod with remote $7 to $20, about $165 to $230 all in. Whether a 53-inch roll is wide enough for coats and the feather hat, and whether the smaller room has six feet of depth, are open.

**The shot list, in order.** Front on the form, white. In the burgundy room (unedited, the Etsy and Shopify cover). Back. A flat or hanging view where the drape on the form misleads. Label and maker tag. Fabric close-up. Closures and hardware. Every flaw, same light. Measurements card with the tape visible (pit to pit, shoulder, length, waist, sleeve), numbers also in the description. Eight to twelve photos. Flat lay only for denim, tees, scarves and accessories.

**Naming on the phone or PC before the script runs:** `B12-front.heic`, `B12-back.heic`, `B12-label.heic`, `B12-flaw1.heic`. The second word decides the treatment (section 7).

## 6. Ghost mannequin: when, if ever

Ghost (invisible) mannequin means two shots per garment, front on the form plus the inside of the neck shot separately, then a composite in Photoshop or GIMP, 20 to 45 minutes a piece by hand (vendor figures, snippet-level). The automation field is thin: one GitHub project with no licence and no stars that needs SAM 3.1 weights and expects hanger shots, two zero-like Spaces, and a FLUX LoRA that regenerates the garment. The honest reading of the seller threads we could see is that pre-owned sellers use a visible form or a flat lay, and buyers of vintage want to see fit and flaws.

Decision: visible form by default. Ghost only clean, structured, flawless pieces (blazers, coats, tailored shirts) and always alongside a visible-form or flat shot. Never on fragile, stretched or stained pieces, and never with a generative method unless the result is compared against the real garment. If Ricky wants to try it, the cheapest test is Photoroom's single-photo mode on one blazer against a manual two-shot composite of the same blazer.

## 7. Automation: what the script now does

`tools/cutout/cutout.py` (tested here on CPU; the handoff has the Windows install):

- Reads JPEG, PNG, WebP and iPhone HEIC, rotates by EXIF, converts Display P3 to sRGB.
- Decides the treatment from the file name. `front`, `back`, `side` or anything else: cut out onto white. `label`, `tag`, `flaw`, `detail`, `close`, `inside`, `measure`, `fabric`, `hem`, `button`, `zipper`: kept exactly as shot, resized only. `frame`, `framed`, `art`, `mirror`, `painting`, `poster`, `box`, `book`, `sign`, `tray`, `record`, `album`: cut, then the rectangle repair. Not `print` or `canvas`: a floral print dress and a canvas tote are clothes.
- Writes `ebay/NAME.jpg` (1600 square, item at 85%), `listing/NAME.jpg` (2048 square master), `site/NAME.png` (transparent, our site only), and a `manifest.csv` row with the model, the processor, seconds, the share of pixels untouched, and warnings.
- `--shadow` adds a soft contact shadow under objects standing on a surface (lamps, shoes, hats, bags); `--shadow drop` gives a faint drop shadow behind a hanging or framed item (whitebg's recipe, MIT). Off for clothes on a form; the PNG never has one.
- `--watch` keeps running and processes each photo two seconds after it stops growing in the folder, so it can run while Ricky shoots and the phone syncs. `stop.txt` in the folder or Ctrl+C ends it. Photos already done are skipped unless `--force`.
- Warns when fewer than 99% of the item's pixels match the photo, when the item is mostly see-through (glass: list the original), and when the item is small in the frame.
- Refuses the Bria model.

Not built, on purpose: ghost mannequin, any generative fill, upscaling. Glass is still "list the original sweep shot".

## 8. Open questions for Ricky, and what is still unverified

Questions only Ricky can answer:

- Which forms are on hand now, and does any have a removable neck or arms?
- iPhone model and iOS version (decides the phone stopgap), and whether photos arrive as HEIC or JPEG.
- The room's depth: can the form stand five or six feet from the backdrop?
- Shoot into one folder with named files, or one subfolder per item?

Unverified because the cloud session could not open those sites (every one listed in `research/ebay-photo-studio-2026-11-07/fetch-later.md`, 153 URLs, with a one-line crawl4ai loop for the PC): all gear prices; eBay's current wording on AI-edited photos and whether a Seller Center page recommends a form or mannequin; Reddit seller threads (none could be reached at all, search does not index them from here); YouTube tutorials and transcripts; Photoroom, Pixelcut and Canva pricing pages; Apple and Microsoft support pages for the phone steps. The Windows GPU recipe, the model bench on all the photos and the claim-by-claim check are sweep B (lanes 18 to 21 and the verification table in this folder's README).

## 9. Where things are

- Lane reports: `research/ebay-photo-studio-2026-11-07/01-rembg.md` through `21-hf-deeper.md`, raw pages under `raw/`, tests under `test-results/`, the blocked-URL list in `fetch-later.md`.
- The script: `tools/cutout/cutout.py`. The cloud page fetcher used by the lanes: `tools/crawl-cloud.sh`.
- The setup card for the PC: `docs/ebay-photo-studio-handoff.md`.
- Earlier decisions this builds on: `docs/cutout-catalog-handoff.md` (the October cutout stack), `docs/photo-checklist.html` (the shoot checklist), `research/ebay-clothing-photos-2026-10-30/` (the eBay pages).
