# 02 Cutout tooling and pipeline for Hollywood and Vine (researched 2026-10-27)

Tags: **VERIFIED** = read on the vendor/repo/licence page this session (URL + close paraphrase). **UNVERIFIED** = memory, blog, snippet, or not fetched. Raw crawls: `research/cutouts/raw/02-*.md`. Cutting is done with a MASK (original pixels kept), not a generative edit.

## Bottom line

1. **Use rembg 2.0.86 (MIT) pinned to `-m birefnet-general -dc` (BiRefNet weights are MIT), with Sharp 0.35.5 for resize/trim/WebP.** Local, free, no per-image cost, original pixels kept.
2. **TRAP: bare `rembg i in out` runs bria-rmbg (RMBG-2.0), the rembg default. Its weights are CC BY-NC 4.0, and commercial use needs a BRIA agreement.** Every command must pass `-m`. Skip BRIA RMBG-1.4/2.0 entirely (a shop is commercial use).
3. **Do not build on remove.bg: its standalone site and credits end 1 Dec 2026 (5 weeks from today), API pricing moved to Leonardo.ai.** Google Product Studio is disqualified (its UI outputs white not transparent; transparency only in `v1alpha` Merchant API; its page also carries a caveat about "light fixtures" and "walled art", scope of which is unclear). Gemini image editing is generative (redraw risk), SynthID-watermarked, no documented alpha output.
4. **Photoroom API is the verified paid hosted fallback**: $0.02/image on its marketing page, docs say it does not alter product pixels. Free Photoroom accounts are personal/non-commercial and sandbox output is watermarked.
5. **Glass has no verified good automatic answer.** Chandelier, pink stemware, decanter: shoot on a seamless backdrop and DO NOT cut; show them on a "display card" tile in the backdrop colour. Fringe, feathers, chains: BiRefNet general + `-dc`; test BiRefNet_HR-matting (MIT, 2048 px, "matting with transparency") as the soft-alpha challenger.
6. **Hardware**: Windows desktop has an RTX 4060 Ti 16 GB, i7-14700KF, 32 GB RAM (observed locally with nvidia-smi/CIM, not a vendor claim). CPU alone is fine for 40 items. Fedora is out for rembg (needs Python >=3.11,<3.14; the Fedora box runs 3.14 per CLAUDE.md) unless a container is used.
7. **Use a NEW venv**, not `C:\Users\ethan\crawl4ai-venv` (that is the machine-wide crawl4ai install).
8. **Deliver JPEG, not HEIC**: Sharp's prebuilt format list does not include HEIC. Etsy Seller Handbook pages were walled (4-byte responses): Etsy guidance is UNVERIFIED.
9. **Pilot first** (section 7): chandelier, pink glasses, fringed boots, with a mechanical "pixels unchanged" check plus by-eye criteria on white, black and burgundy.

## 1. Tool comparison (licence and price from vendor pages)

### (a) Apple built-in

| Option | What it does | Version | Output | Cost/licence |
|---|---|---|---|---|
| iPhone Photos "Copy"/"Copy Subject" | VERIFIED https://support.apple.com/guide/iphone/lift-a-subject-from-the-photo-background-iphfe4809658/ios : touch and hold the subject, an outline appears, then Copy, Add Sticker or Share | VERIFIED https://support.apple.com/en-us/102460 : iOS 16 and later, iPhone XS, XR and later | Output file format NOT stated by either page: UNVERIFIED (do not assume PNG). 102460 also says "Subjects cannot be pasted onto another photo." | Built in; no price or output-licence text on the pages |
| Mac Preview "Remove Background" | VERIFIED https://support.apple.com/guide/preview/remove-a-background-or-extract-an-image-prvw15636/mac : button in Markup toolbar; "If you're asked whether you want to convert the document to a PNG file" | Page lists macOS 11 to 27 | PNG (conversion prompt) | Built in; needs a Mac. Nothing says Ricky has one |
| Mac Finder Quick Action | VERIFIED https://support.apple.com/guide/mac-help/perform-quick-actions-in-the-finder-on-mac-mchl97ff9142/mac : More > Remove Background; More > Convert Image turns .heic into .jpeg/.png | macOS | Not stated | Built in; needs a Mac |
| Shortcuts "Remove Background" action | UNVERIFIED: no Apple page found; the only pages reached were a 1.2 KB third-party stub (shortcutactions.com) and a search hit (matthewcassinelli.com, not fetched) | | | |

Verdict: one-at-a-time, no batch, no mask control, no statement that pixels are untouched. Fine for a quick look, not for the catalog pipeline.

### (b) Google

| Option | Verified facts | Verdict |
|---|---|---|
| Merchant Center Product Studio "Remove background" | VERIFIED https://support.google.com/merchants/answer/13708167 : "suite of free, AI-powered tools"; "Remove background ... Only your product will remain on a white background"; available to all Merchant Center users except RU and FR; the same page says "This feature doesn't support images with hands, walled art, and light fixtures" and is "experimental". That sentence sits in the general paragraph about the experimental generative features, not under "Remove background", so its scope for background removal is unclear | Caveat touches our lamps, chandelier, framed art, but the reject does not depend on it: the UI result is white, not transparent, and transparency exists only in `v1alpha`. Reject |
| Merchant API `removeProductImageBackground` | VERIFIED https://developers.google.com/merchant/api/samples/remove-product-image-background : package `productstudio.v1alpha`; code comment "Don't set this field if you want the image to have a RGBA 4-channel transparent image as the background" | Transparent output exists only via an alpha-version API (unstable); no statement that pixels are preserved. Reject for a 40-item shop |
| Gemini API image editing ("Nano Banana") | VERIFIED https://ai.google.dev/gemini-api/docs/image-generation : "All generated images include a SynthID watermark"; searching the page for "transparen/alpha" finds nothing, so transparent output is undocumented. VERIFIED https://ai.google.dev/gemini-api/docs/pricing : per output image, Nano Banana 2.1 about $0.0336 per 1K image (Standard) and $0.0168 (Batch); Gemini 3.1 Flash Image $0.067 per 1K; Nano Banana Pro $0.134 per 1K/2K | Generative: can redraw the item. This is the same class as the current `docs/storefront-art-direction.md` prompts. Not for catalog |
| Google Photos, Imagen | Not fetched. UNVERIFIED | Not evaluated |

### (c) Hosted tools

| Tool | Price | Commercial use | Resolution/format | Verdict |
|---|---|---|---|---|
| Photoroom Remove Background API | VERIFIED https://www.photoroom.com/api/remove-background : "for $0.02 per image"; accepts "PNG, JPEG, WEBP or HEIC". The pricing page https://www.photoroom.com/api/pricing rendered NO dollar amounts in our crawl (tiers Basic/Plus/Enterprise, "1,000 free images using our sandbox mode"): plan minimums UNVERIFIED. VERIFIED docs.photoroom.com/getting-started/pricing : billed per image; errors do not consume images; sandbox mode is free but "will produce a result with a watermark" | VERIFIED https://www.photoroom.com/legal/terms-and-conditions : "We grant Free Accounts a ... license ... for your own personal, non commercial purposes". Paid subscription = business use. Whether API use has separate terms is UNVERIFIED (check https://photoroom.discourse.group/tos before buying) | Max size UNVERIFIED. Params `format, channels, bg_color, size, crop` (quickstart) | **Best hosted fallback.** VERIFIED quickstart: "will only remove the background and will not make any change to the actual pixels of the original image" (Green Screen Despill is the exception) |
| remove.bg | VERIFIED https://www.remove.bg/pricing : $3 for 3 credits PAYG, $9/month for 40 credits; banner: "background removal is moving to Canva. The standalone website will no longer be available from 1 December 2026"; "Credits expire December 1, 2026"; "Go to Leonardo.ai for API Pricing" | Not checked | Max resolution: moot, service ends | **Reject** |
| Adobe Express / Firefly | VERIFIED https://helpx.adobe.com/express/web/image-creation-and-editing/edit-images/remove-background.html : transparent export needs Background > "No fill" then "Transparent PNG"; warns the tool "may also remove fine details or low-contrast areas. Review the cutout". VERIFIED https://www.adobe.com/express/feature/image/remove-background : headline "for free", upload "JPEG (JPG), PNG, or WEBP and up to 50MB" | Free-plan limits and commercial terms NOT stated on fetched pages: UNVERIFIED | | Manual, one image at a time. Good for rescuing a single failed cutout by hand |

### (d) Open-source models and wrappers

| Item | Code licence | Weights licence | Commercial OK? | CPU-only |
|---|---|---|---|---|
| **rembg** 2.0.86 (released Oct 21, 2026; PyPI https://pypi.org/project/rembg/ ) | MIT (PyPI classifier and README) | Per model, "independent of rembg's MIT license" (README) | Depends on model: see rows below | `pip install "rembg[cpu,cli]"` is the documented CPU install; needs Python >=3.11,<3.14 |
| **BiRefNet** (https://github.com/ZhengPeng7/BiRefNet ) | MIT (GitHub licence panel) | VERIFIED `License: mit` on https://huggingface.co/ZhengPeng7/BiRefNet and .../BiRefNet_HR-matting | Yes per weights card. Licences of the datasets it was trained on were not audited: UNVERIFIED | README: A100 86.8 ms, RTX 4090 95.8 ms at 1024 px (FP32). CPU: one user report of ~6 s/image for BiRefNet_lite ONNX at 1024 px (https://github.com/ZhengPeng7/BiRefNet/issues/259, hardware unstated, issue closed, owner asked the reporter to post their fix). 2000 px CPU time: UNVERIFIED, measure in pilot |
| **BRIA RMBG-2.0** | n/a | VERIFIED https://huggingface.co/briaai/RMBG-2.0 : "CC BY-NC 4.0 ... non-commercial use"; "Commercial use is subject to a commercial agreement with BRIA" | **No** without paid agreement | Not stated |
| **BRIA RMBG-1.4** | n/a | VERIFIED https://huggingface.co/briaai/RMBG-1.4 : licence `bria-rmbg-1.4`, "released under a Creative Commons license for non-commercial use ... Commercial use is subject to a commercial agreement" | **No** without paid agreement | Not stated |
| **U2-Net** | Apache-2.0 (https://github.com/xuebinqin/U-2-Net ) | Not separately stated: UNVERIFIED | Apache-2.0 on repo | rembg: older models (u2net, u2netp, silueta) "produce firmer, blockier edges". CPU time per 2000 px: UNVERIFIED (no source) |
| **SAM 2** (https://github.com/facebookresearch/sam2 ) | Apache-2.0 (+BSD-3 parts) | VERIFIED: "checkpoints, demo code, training code are licensed under Apache 2.0" | Yes | Needs python>=3.10, torch>=2.5.1. Promptable (needs click/box prompts): a manual fallback, not a batch tool. rembg exposes it as `-m sam -x '{"sam_prompt":[...]}'`. CPU speed UNVERIFIED |
| **pymatting** 1.1.16 (https://pypi.org/project/PyMatting/ ) | MIT | n/a (no weights) | Yes | Alpha matting from a TRIMAP; "There currently is no GPU support for alpha estimation" (CPU only) |

**Discrepancy:** BRIA's blog (https://bria.ai/blog/youre-missing-253-shades-of-transparency) says RMBG-2.0 "outputs a complete 8-bit alpha matte" suited to glass. The BiRefNet README says RMBG-2.0 weights "are not aware of transparency due to training in the DIS task setting, which focuses only on predicting binary masks". The BiRefNet README verified, BRIA's blog is vendor marketing, needs review. Moot for us because of the licence.

## 2. Hard cases (glass, gaps, fringe, feathers, chains)

What is VERIFIED about masks vs mattes:
- rembg README: three edge modes (naive, `-dc` decontaminate, `-a` alpha matting, `-vm` ViTMatte). Decontamination: `captured = alpha * foreground + (1 - alpha) * background`; `-dc` "only changes color, never coverage". `-ppm` "thresholds the mask into a fully binary one, which leaves no partially transparent pixels". Newer models (`bria-rmbg`, `birefnet-*`, `isnet-general-use`) "already produce a soft, well-shaped alpha"; try `-dc` first and `-a` only "if the edge shape itself is wrong"; `-a`/`-vm` are slow.
- pymatting README: matting is solved from a trimap (known fg / known bg / unknown band), foreground-colour estimation included.
- BiRefNet README: `BiRefNet-matting` (1024 px, "trimap-free matting"), `BiRefNet_HR-matting` (trained at 2048x2048), HF card says "for higher resolution image matting with transparency". Its inference snippet applies the soft mask to the ORIGINAL image with `image.putalpha(mask)` (pixels kept). Matting training sets listed are human/animal oriented (P3M-10k, AM-2k, Distinctions-646, HIM2K, PPM-100...): our inference, glass is not named, so glass quality is UNVERIFIED.
- Vendor claims (flagged vendor-biased): BRIA blog says binary masks make glass/lace "lose their character"; Photoroom's own comparison (https://www.photoroom.com/blog/image-background-removal-technology-comparison) says a plain mask "does not consider color" so cannot decontaminate. Photoroom ran 45 images and picked itself as best: treat as marketing, not a benchmark.
- Adobe's own help page warns the tool may remove "fine details or low-contrast areas".

| Hard case | Expectation (inference; no verified source tests our objects) | Recommended | Fallback |
|---|---|---|---|
| Two-tier sea-glass chandelier (gaps, frosted shards, wires) | Binary masks fill the gaps or drop shards; soft masks may leave wall-coloured haze | Pilot: BiRefNet_HR-matting vs birefnet-general `-dc` on a re-shot with a clean backdrop far behind | Shoot on seamless backdrop and skip cutting; display card tile in backdrop colour |
| Pink stemware, decanter | Clear/translucent glass: a matte keeps the edge but the inside still contains the old backdrop colour, so it looks wrong on burgundy | Same as above; honest cutout only if edge-defined (dark flags) | Skip cutting; display card |
| Fringed western boots | Fine strands in a thin band | birefnet-general `-dc`; `birefnet-hrsod`/HR-matting if strands vanish; rembg `-vm` only if shape is wrong | Contrasting solid backdrop; hand rescue in Adobe Express |
| Feathered cocktail hat | Same as fringe | Same as boots | Same |
| Chain-and-stud harness belt | Open links get filled | birefnet-general, check link holes; shoot hanging/flat on contrasting backdrop | Skip cutting |
| Brass lamps, ceramic leopard, busts, dress form, art, magazines | Solid, hard edges: the easy case (rembg: "Use the default (naive) when the subject has hard edges") | birefnet-general `-dc` | |
| Trench, jackets | Soft fabric edge, medium | birefnet-general `-dc` | |

**Fallback that needs no model** (the standard glass practice): photograph on a seamless solid backdrop and do not cut. Then the storefront tile shows the photo on a "display card" whose CSS background equals the backdrop colour. Rules: sample the backdrop hex AFTER Sharp's sRGB conversion (Sharp default converts to sRGB and strips ICC: VERIFIED https://sharp.pixelplumbing.com/api-output/ , `keepMetadata` text), otherwise Display P3 vs CSS sRGB leaves a visible seam; keep the backdrop evenly lit (a gradient will show as a box); for glass pick a pale card, not the burgundy wall.

## 3. Shooting guidance (actionable now)

VERIFIED from https://help.shopify.com/en/manual/products/product-media/product-photography and https://www.shopify.com/blog/12206313-the-ultimate-diy-guide-to-beautiful-product-photography :
- Use a room with a window; turn off all other lights ("other light will contaminate the set"); flash off; no harsh direct sun.
- Tripod; "keep your camera and tripod in the same position during your shoot"; "Rotate the product if you want to change angles. If you rotate the product only, then your final images will have the same frame effect."
- Backdrop: seamless sweep (paper) taped on a table curving up a wall; "Opt for pure white, as off-white or cream backgrounds are more challenging to edit to pure white".
- White foam board fills shadows; black foam board at the sides "to create a dark edge on the white product" on white.
- Shoot eye-level (straight on) first, then other angles.
- Web images: aim for no larger than 200 KB each (Shopify help).
VERIFIED from https://www.photoroom.com/blog/ai-product-photography-tips : uniform light free from harsh shadows and reflections; window light with the product at 90 degrees to the window; flat mono-colour backgrounds suit online stores.
Glass (secondary blogs, studio vendors: https://www.prophotostudio.net/blog/learning-center/why-photographing-glass-is-so-hard/ , https://www.mainstreammultimedia.com/blog/how-to-photograph-transparent-objects-in-product-photography ): you light the background, the glass edges define the shape; bright field = white sheet at least 2 to 3 ft behind the glass, lit from behind, black cards just outside frame to give crisp dark edge lines; dark field = black backdrop, white cards at 45 degrees; ISO 100, f/11, tripod; clean off fingerprints and dust; a polarizing filter reduces glare. Treat as practice tips, not verified science.
Etsy Seller Handbook (photography checklist, "How to Photograph Challenging Items"): all fetches returned 4 bytes (walled), so nothing from Etsy is claimed.

Our recommendations (inference, not vendor-verified), for the re-shoot:
1. Two backdrops: white seamless paper (default); a charcoal/black one for white, pale, frosted or glass items so edges contrast. Never a backdrop colour that appears in the item (pink glass: no pink).
2. Keep the item 2 to 3 ft off the backdrop (glass guide) and lift/hang so its shadow lands away from the item edge; chandelier hangs free, no wall behind it.
3. Frame square-on at the item's mid-height, item filling ~70 to 80% of the frame with margin on all four sides; mark the table with tape so camera distance is identical for similar-sized items. Use the main 1x camera, not ultra-wide (distortion).
4. Brass/glossy: diffuse light so the window does not mirror in it. Glass: dark flags (bright field) or white cards (dark field).
5. Export JPEG (UNVERIFIED iPhone path: Settings > Camera > Formats > Most Compatible). Original 4284x5712 is fine; we downsize.
6. One short ruler or tape-measure photo per item for real size; real size goes in the listing, not in the grid scale.

## 4. Post-processing recipe

Pipeline order: **orient+downsize+sRGB (Sharp) -> cut (rembg) -> trim (Sharp) -> contain into a cell with transparent padding (Sharp) -> WebP (Sharp)**. rembg/BiRefNet runs the model at about 1024 px (BiRefNet default input is 1024x1024; HR/matting variants 2048), so cutting a 4284x5712 original wastes time and the mask is upsampled anyway: cut at <=2048 px long edge.

Sharp 0.35.5 (npm, Apache-2.0, Node >=20.9.0: VERIFIED npm page and install page). Option names below are from https://sharp.pixelplumbing.com/api-output/ and /api-resize/ :
- `autoOrient()` = auto-orient from EXIF Orientation, then remove the tag. `resize({width:2048,height:2048,fit:'inside',withoutEnlargement:true})`.
- `trim({threshold, margin, lineArt})`: default `threshold` 10, `margin` 0; "Images with an alpha channel will use the combined bounding box of alpha and non-alpha channels". Use a low threshold (1 to 3) so wispy fringe survives (our tuning, UNVERIFIED). **WARNING: trim looks at RGB as well as alpha.** The BiRefNet_HR-matting snippet does `image.putalpha(mask)`, which leaves the original room's RGB under the transparent pixels, so the RGB bounding box is the whole frame and `trim` can do nothing, silently. What rembg writes under alpha 0 is unchecked (UNVERIFIED). Always clear RGB where alpha is 0 first (step 2b below), or take the bbox from the alpha channel alone.
- `resize({width:W,height:H,fit:'contain',background:{r:0,g:0,b:0,alpha:0}})`: `contain` letterboxes, and the default background is black WITHOUT transparency, so pass alpha 0 explicitly. `extend({top,left,bottom,right,background:{...alpha:0}})` also pads.
- `webp({quality, alphaQuality, effort, smartSubsample, lossless, nearLossless, exact})`: defaults quality 80, alphaQuality 100, effort 4 (0 to 6), lossless false, nearLossless false, smartSubsample false, `exact` false ("preserve the colour data in transparent pixels"). Recommended: `{quality:82, alphaQuality:100, effort:5, smartSubsample:true}`; use `nearLossless` or `lossless` only if edges band. Keep each tile <=200 KB (Shopify's target).
- Colour: default output is sRGB with metadata stripped (iPhone Display P3 gets converted if the JPEG has its ICC profile). Do this BEFORE cutting so rembg sees the same colours the site will show.
- HEIC: Sharp's prebuilt format list (https://sharp.pixelplumbing.com/install/ ) = JPEG, PNG, Ultra HDR, WebP, AVIF, TIFF, GIF, SVG input; HEIC is not listed, so convert to JPEG first. rembg HEIC support is not stated: UNVERIFIED.

Concrete recipe (one item; three separate Sharp passes so nobody has to guess operation order: Sharp fixes some order itself, e.g. `extend` "will always occur after resizing", one `rotate` per pipeline). Only options verified above are used; the numbers are starting points:
```js
import sharp from 'sharp';                                   // npm i sharp@0.35.5
// pass 1: orient + downsize (+ sRGB by default) -> JPEG for the cutter
await sharp('in/IMG_6614.jpg').autoOrient()
  .resize({ width: 2048, height: 2048, fit: 'inside', withoutEnlargement: true })
  .jpeg({ quality: 95 }).toFile('work/IMG_6614.jpg');
// cutter:  rembg i -m birefnet-general -dc work/IMG_6614.jpg cut/IMG_6614.png
```
```python
# step 2b (Python, after the cutter): clear RGB under alpha 0, then crop to an alpha-only bbox
from PIL import Image; import numpy as np
im = Image.open('cut/IMG_6614.png').convert('RGBA'); arr = np.array(im)
arr[arr[..., 3] == 0, :3] = 0                    # matting output may keep the old room under alpha 0
im = Image.fromarray(arr)
box = im.getchannel('A').point(lambda v: 255 if v > 8 else 0).getbbox()   # ignore faint specks
im.crop(box).save('cut2/IMG_6614.png')           # (Sharp trim() on this file is now safe too, threshold 1 to 3)
```
```js
// pass 3: fit into the grid cell with transparent padding, then WebP (own pipeline)
await sharp('cut2/IMG_6614.png')
  .resize({ width: 880, height: 1056, fit: 'contain', background: { r: 0, g: 0, b: 0, alpha: 0 } })
  .extend({ top: 72, bottom: 72, left: 60, right: 60, background: { r: 0, g: 0, b: 0, alpha: 0 } })
  .webp({ quality: 82, alphaQuality: 100, effort: 5, smartSubsample: true })
  .toFile('out/IMG_6614.webp');                  // cell 1000x1200 incl. padding; check size <= 200 KB
```
Sampling check for the pilot: read one pixel where alpha is 0 in `cut/` and in `cut2/`; in `cut2/` its RGB must be 0.

Edge handling:
- Colour fringe: rembg `-dc` (decontaminate; colour only, coverage untouched). Use `-a`/`-vm` only if the shape is wrong (slow).
- Halo remaining after `-dc`: erode alpha 1 px in Python (cv2/scipy, UNVERIFIED), do not blur the alpha in Sharp. Sharp has `blur` (api-operation) and `unflatten` (white to transparent) but neither is a clean fix for a coloured halo.
- Specks: zero alpha below ~8/255 in numpy (our suggestion).

Shadow: **prefer CSS, do not bake it in.** VERIFIED https://developer.mozilla.org/en-US/docs/Web/CSS/filter-function/drop-shadow : "a blurred, offset version of the input image's alpha mask"; unlike `box-shadow` it "conforms to the shape (alpha channel) of the image itself"; `inset` and `spread` are not allowed. Example: `filter: drop-shadow(0 14px 12px rgb(0 0 0 / .35))`. This keeps the image pixel-pure and lets one cutout work on white, black and burgundy tiles. For standing items add a CSS ellipse shadow under the base (radial-gradient pseudo-element, UNVERIFIED but standard). Bake a shadow only for marketplace images that must be flat JPEG.

Scale normalisation (our recipe): after the step 2b alpha-bbox crop, take each cutout's bbox, then place it with `fit:'contain'` into a fixed cell (for example 1000x1200) and cap its filled area per category: tall (lamps, dress form) cell-height 88%; wide (chandelier, art) cell-width 88%; small (hat, belt, stemware) 62 to 70%; anchor standing items on a common baseline (bottom), hung items on a common top. Record real dimensions in the data file. Expect to hand-tune about 5 items.

## 5. Recommended pipeline and install (versions from the pages we fetched)

| Step | Tool | Version | Install (verification) |
|---|---|---|---|
| Venv | Python 3.12.13 exists in the crawl4ai venv (observed `--version`) | any >=3.11,<3.14 | `py -3.12 -m venv C:\Users\ethan\dev\Vintage\.venv-cutout` (UNVERIFIED; do not install into crawl4ai-venv) |
| Cutter | rembg | 2.0.86 (PyPI, released Oct 21, 2026) | `pip install "rembg[cpu,cli]==2.0.86"` (command form VERIFIED on PyPI README; the `==` pin is ours). GPU optional: `pip install "rembg[gpu,cli]"` needs CUDA/cuDNN, README warns it may fail: skip for 40 items |
| Models | birefnet-general (default pick), birefnet-general-lite (faster), `isnet-general-use`, `birefnet-hrsod` | via rembg `-m` | `rembg d` downloads models ahead of time (subcommand listed; arguments UNVERIFIED). Never `-m bria-rmbg`, never omit `-m` |
| Soft-alpha challenger | BiRefNet_HR-matting (HF `ZhengPeng7/BiRefNet_HR-matting`, MIT) | n/a | `pip install -qr https://raw.githubusercontent.com/ZhengPeng7/BiRefNet/main/requirements.txt` (from the HF card, VERIFIED); torch/transformers install UNVERIFIED; load `AutoModelForImageSegmentation.from_pretrained('ZhengPeng7/BiRefNet_HR-matting', trust_remote_code=True)` (HF card). `trust_remote_code=True` runs code from the model repo: review it |
| Image ops | Sharp | 0.35.5 (npm, published about a month ago) | `npm i sharp@0.35.5`. NOTE: there is no `package.json` in this repo and no `sharp` reference in `site/build.mjs`, so the brief's "Sharp already used by the site build" is not visible here (docs say Sharp was used for the editorial assets). Add a package.json under `tools/` |
| Paid fallback | Photoroom Remove Background API | n/a | `curl --request POST --url https://sdk.photoroom.com/v1/segment --header 'x-api-key: KEY' --form image_file=@in.jpg --output out.png` (VERIFIED, docs quickstart). Sandbox keys: prepend `sandbox_` (watermarked) |

Commands (always pinned):
```
rembg i -m birefnet-general -dc work/IMG_6614.jpg cut/IMG_6614.png      # one file
rembg p -m birefnet-general -dc work/ cut/                              # folder (VERIFIED subcommands i, p; flags -m, -dc)
rembg i -m birefnet-general -om work/IMG_6614.jpg mask/IMG_6614.png    # mask only, for inspection (-om VERIFIED)
```
Time: unmeasured on this desktop. GPU references: BiRefNet 95.8 ms at 1024 on an RTX 4090 (README). Even at 60 s/image on CPU, 40 items is 40 minutes. The pilot records real seconds.

Fedora: skip rembg there (Python 3.14 outside rembg's range). If wanted: rembg's Docker CPU image (README: CPU image about 1.6 GB, models not included) under rootless podman, UNVERIFIED on that box.

Cost: open-source path $0. Photoroom: $0.02 x (40 items x about 3 tries) ~ $2.40 of images, plus an unverified plan minimum.

## 6. Mechanical check that proves "mask-based, not redrawn" (put in the pilot)

Where alpha is (nearly) opaque, the cutout RGB must equal the resized source RGB. Run once with `-dc` and once without (decontamination may touch pixels near edges). Interior alpha from a sigmoid matte can sit at 254, so the test uses `>= 250`, not `== 255`:
```python
import numpy as np
from PIL import Image
def pixels_kept(src_path, cut_path):
    cut = Image.open(cut_path).convert("RGBA")
    src = Image.open(src_path).convert("RGB").resize(cut.size, Image.LANCZOS)  # same size as the cut
    a = np.asarray(cut)[..., 3]; opaque = a >= 250
    d = np.abs(np.asarray(cut)[..., :3].astype(int) - np.asarray(src).astype(int)).max(-1)
    return float((d[opaque] <= 3).mean()), float(opaque.mean())   # (share unchanged, share opaque)
```
Pass line (ours, tune after the first run): at least 99% of opaque pixels within 3/255. A generative edit would fail this; rembg/BiRefNet should pass because the soft mask is applied to the original (BiRefNet `putalpha`). If the cut was made on a cropped/trimmed image, compare against the same crop. If the second number (share opaque) is near zero, the check proved nothing: the item is mostly translucent (glass), so judge those by eye only.

## 7. Pilot test plan (three hard cases, human pass/fail)

Material: for each item use (i) the best current photo and (ii) one re-shot on a seamless backdrop as in section 3. Photos: chandelier is `site/assets/photos/IMG_6614`, urn lamp `IMG_6616` (control, easy). Pink glasses and boots: use the current best photos.

Arms (record seconds per image for each):
- A: `rembg -m birefnet-general -dc`
- B: BiRefNet_HR-matting script at 2048 px (soft alpha)
- C: no cut, display card in the backdrop colour (glass control)
- D (optional, needs Ricky's account): Photoroom sandbox on one image to see the paid-tool bar. The sandbox is watermarked; real output costs about $0.02.

View every result: (1) 100% crop of the hard areas, (2) tile size, each on white, black and storefront burgundy (copy the hex from `site/storefront.css`), and blink-compare with the original. Judge each criterion pass/fail.

| Item | PASS needs all of | Auto-FAIL if any |
|---|---|---|
| **Chandelier** | Every glass shard and gold ring present; each gap between shards shows the tile colour (view on white: no burgundy/wall patches); frosted shards still read translucent, not flat white or grey cut-outs; the small silver ball and hanging wires intact; 100% edge not jagged | Missing shards or arms; gaps filled; wall-coloured haze inside the fixture |
| **Pink glasses** | Rim, bowl, stem and foot all there; bowls still read pink and glassy (not black, opaque, or filled with wall colour on white/black); no white or burgundy rim line; foot disc not cut off | Missing stem/foot; bowl fill wrong colour; halo on the burgundy tile |
| **Fringed boots** | Individual fringe strands visible; no coloured halo between strands on white or black; no solid fill between strands; stitching, heel, sole edge and toe intact | Strands fused into a blob or removed; visible background colour fringe |
| **All three** | Mechanical check (section 6) passes; colours match original on blink compare; file is <=200 KB at tile size | Pixels redrawn or shifted |

Decision:
- Arm A or B passes boots and chandelier: use that arm for all non-glass items, per-item review of contact sheet, `-a/-vm` only on failures.
- Chandelier or glasses fail on A and B: those categories use Arm C (display card, no cut) and we stop trying to cut glass.
- Only Arm D passes: Ricky decides whether about $2 to $5 of Photoroom images plus its plan fee is worth it.
- Report: seconds per image on this desktop (CPU vs GPU if tried) so we can plan the 40-item run.

## 8. Open issues and discrepancies

- **BRIA vs BiRefNet README** on whether RMBG-2.0 gives soft alpha: BiRefNet README verified, BRIA blog needs review. Licence makes it moot.
- **"Sharp already in site build"**: not found in this repo (no package.json, no `sharp` match in `site/build.mjs`). Coding agent installs it.
- **Photoroom price**: $0.02/image verified on its marketing page; its pricing page rendered no amounts, so plan/minimum fees are unverified.
- **Photoroom commercial use**: free tier non-commercial verified; API-specific terms not fetched.
- **CPU speed for 2000 px**: no source. One anecdote (6 s at 1024, BiRefNet_lite ONNX). Measure.
- **BiRefNet training-data licences**: weights card says MIT; datasets not audited.
- **Gemini/Imagen/Google Photos** transparent-background capability: not verified; ignored.
- **Adobe, Apple Shortcuts, Etsy**: incomplete as stated above.
- Machine facts (GPU, CPU, RAM, Python 3.12.13) were observed locally on 2026-10-27, not taken from a vendor.

## Sources

Apple: https://support.apple.com/guide/iphone/lift-a-subject-from-the-photo-background-iphfe4809658/ios ; https://support.apple.com/en-us/102460 ; https://support.apple.com/guide/preview/remove-a-background-or-extract-an-image-prvw15636/mac ; https://support.apple.com/guide/mac-help/perform-quick-actions-in-the-finder-on-mac-mchl97ff9142/mac (homepage https://www.apple.com)
Google: https://support.google.com/merchants/answer/13708167 ; https://developers.google.com/merchant/api/samples/remove-product-image-background ; https://ai.google.dev/gemini-api/docs/image-generation ; https://ai.google.dev/gemini-api/docs/pricing (homepage https://www.google.com)
Photoroom: https://www.photoroom.com/api/remove-background ; https://www.photoroom.com/api/pricing ; https://docs.photoroom.com/getting-started/pricing ; https://docs.photoroom.com/remove-background-api-basic-plan/quickstart-guide ; https://docs.photoroom.com/remove-background-api-basic-plan/sandbox-mode ; https://www.photoroom.com/legal/terms-and-conditions ; https://www.photoroom.com/blog/image-background-removal-technology-comparison ; https://www.photoroom.com/blog/ai-product-photography-tips (homepage https://www.photoroom.com)
remove.bg: https://www.remove.bg/pricing ; https://www.remove.bg/faq (homepage https://www.remove.bg)
Adobe: https://helpx.adobe.com/express/web/image-creation-and-editing/edit-images/remove-background.html ; https://www.adobe.com/express/feature/image/remove-background (homepage https://www.adobe.com)
Open source: https://pypi.org/project/rembg/ ; https://github.com/danielgatis/rembg ; https://github.com/ZhengPeng7/BiRefNet ; https://huggingface.co/ZhengPeng7/BiRefNet ; https://huggingface.co/ZhengPeng7/BiRefNet_HR-matting ; https://github.com/ZhengPeng7/BiRefNet/issues/259 ; https://huggingface.co/briaai/RMBG-2.0 ; https://huggingface.co/briaai/RMBG-1.4 ; https://bria.ai/blog/youre-missing-253-shades-of-transparency ; https://github.com/xuebinqin/U-2-Net ; https://github.com/facebookresearch/sam2 ; https://github.com/pymatting/pymatting ; https://pypi.org/project/PyMatting/
Sharp and CSS: https://sharp.pixelplumbing.com/api-output/ ; https://sharp.pixelplumbing.com/api-resize/ ; https://sharp.pixelplumbing.com/api-operation/ ; https://sharp.pixelplumbing.com/install/ ; https://www.npmjs.com/package/sharp ; https://developer.mozilla.org/en-US/docs/Web/CSS/filter-function/drop-shadow
Shooting: https://help.shopify.com/en/manual/products/product-media/product-photography ; https://www.shopify.com/blog/12206313-the-ultimate-diy-guide-to-beautiful-product-photography ; https://www.prophotostudio.net/blog/learning-center/why-photographing-glass-is-so-hard/ (secondary) ; https://www.mainstreammultimedia.com/blog/how-to-photograph-transparent-objects-in-product-photography (secondary). Etsy Seller Handbook (https://www.etsy.com/seller-handbook/category/photography ) walled, not read.
Local observation: `nvidia-smi` (RTX 4060 Ti, 16380 MiB), CIM (i7-14700KF, 20 cores, 31.8 GB), `crawl4ai-venv\Scripts\python.exe --version` = 3.12.13.
