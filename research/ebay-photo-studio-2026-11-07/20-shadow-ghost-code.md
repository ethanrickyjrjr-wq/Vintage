# Lane 20: shadow and ghost mannequin code

Status (2026-11-07): FETCHED with tools/crawl-cloud.sh --browser and raw.githubusercontent.com: whitebg repo page, tree, README, LICENSE, engine.py, gui.py; GhostMannequinEngine repo page, README, ghost_auto.py, requirements.txt. HF MCP read of facebook/sam3.1. BLOCKED: docs.photoroom.com (curl: "CONNECT tunnel failed, response 403", code 000, tested once). GhostMannequinEngine has no LICENSE or LICENSE.md file (raw URLs returned 404). Saved under raw/20-shadow-ghost-code/ (w-* = whitebg, g-* = ghost engine, hf-sam3.1.md). Sketch below was run once with Pillow 12.3.0 and numpy 2.5.3 on a synthetic disc and behaved as described.

## Part A: whitebg

1. Licence (VERIFIED_FETCHED, raw/.../w-LICENSE): "MIT License ... Copyright (c) 2026 whitebg contributors". The repo page also shows "MIT license". 0 stars, 11 commits, so a young solo project. Safe to copy ideas and short snippets with the notice; we only need the idea.

2. Shadow (VERIFIED_FETCHED, w-src-engine.py lines 244-267, compose_on_white). Exact recipe: defaults shadow_opacity=0.28, shadow_blur=0.02, shadow_offset=0.015. blur radius = max(1.0, max(w,h) * 0.02) as a Pillow GaussianBlur radius applied to the item's own alpha channel (the whole silhouette, not a footprint). Opacity: each blurred alpha value multiplied by 0.28. Colour is pure black (RGBA (0,0,0,0) layer with the blurred alpha as its alpha). Offset: dy = round(h * 0.015), dx = round(w * 0.015 * 0.6), so down and slightly right. Shifted layer is alpha-composited on a white canvas, then the item is pasted on top with its own alpha. Only the CLI flag --shadow exists (no tunable flags for the numbers). validate() rejects --shadow with --transparent: the shadow is white-background only. Which matches our rule that the transparent site PNG stays shadowless.

3. Crop and pad (VERIFIED_FETCHED, lines 197-243). trim_to_subject: alpha thresholded at 12 (v>12 becomes 255), getbbox, crop, then pad = round(max(w,h) * margin) on every side onto a transparent canvas; default --margin 0.06. make_square: side = max(w,h), pad = round(side * inner_margin) (default 0.04), centre on a transparent square. fit_size: longest side to --size (default 1200), downscale only unless --upscale, LANCZOS. pad_to_exact fills to exactly N by N. Note the blur radius is 2 percent of the final canvas, and the margins (6 percent plus 4 percent) are what keep the blurred shadow from being clipped at the canvas edge.

4. Decontamination (VERIFIED_FETCHED, lines 147-191). Newer rembg: passed through as decontaminate=True. Older rembg: _decontaminate_cutout uses pymatting.estimate_foreground_ml(rgb/255, alpha/255), then restacks with alpha. Comment: with alpha_matting on, rembg ignores decontamination. Default is on (--no-decontaminate turns it off). requirements.txt lists PyMatting>=1.1.12, rembg>=2.0.60,<3, onnxruntime>=1.17, tkinterdnd2.

5. Defaults and GUI (VERIFIED_FETCHED, README and engine.py). Default model birefnet-general-lite ("birefnet-general-lite ... 224MB ... Stable on fine structures, recommended default ... MIT, commercial use OK"), output 1200x1200 white JPG at quality 95. README: "A soft drop shadow to avoid the 'sticker' look | --shadow". The GUI (gui.py, Tkinter, drag and drop) has no shadow control: the only "shadow" hits in gui.py are drawing code for card borders (SHADOW_1/SHADOW_2). So the GUI offers nothing to learn from for our shadow; the CLI engine is the whole story.

6. Important finding: tools/cutout/cutout.py ALREADY HAS a --shadow option (MEASURED_HERE, reading the file): square_on_white(item, size, shadow=False) squashes the item's alpha into a sliver 12 percent of item height, centres it on the item's bottom edge, blurs it (radius max(4, 2.5 percent of item height)) and pastes black at SHADOW_OPACITY = 0.25. It is applied to the master (2048) and eBay (1600) JPGs only; the site PNG is saved before shadowing, so the site PNG is already shadowless. So the question is not whether to add a shadow but whether whitebg's whole-silhouette drop shadow is a better look than the existing footprint sliver. Both are cheap.

## Which shadow suits eBay

Judgement (not a measurement): the existing footprint sliver reads as an object resting on a surface, right for lamps, vases and boxed things. The whitebg whole-silhouette drop shadow, offset down and right, reads as a floating sticker with a halo, which fits flat garments, framed art, and anything photographed hanging or on a form (nothing is touching a floor). For a hanging or form-mounted garment, a floor sliver under the hem looks wrong. Suggest two modes: --shadow contact (current) and --shadow drop (new). eBay itself does not forbid a soft natural shadow, but I did not fetch eBay policy (host blocked), so UNVERIFIED; keep opacity in the 15 to 25 percent range Ricky asked for so the background stays reading as white. A pure 255 white background is retained at the corners (checked in the sketch run: pixel (0,0) stayed 255,255,255).

## Sketch: drop shadow mode for cutout.py (not applied)

Pillow plus numpy only, no new dependency. Works on the already-placed item on the final canvas so the shadow never clips against the item's own crop. The site PNG path is untouched: never call this on `site`.

```python
SHADOW_OPACITY = 0.20     # inside the 15-25 percent request
DROP_BLUR, DROP_DY, DROP_DX = 0.02, 0.015, 0.009   # fractions of canvas size (whitebg: 0.02, 0.015, 0.015*0.6)

def drop_shadow_mask(alpha_canvas, opacity=SHADOW_OPACITY):
    """alpha_canvas: L image, item alpha already placed on the final canvas. Returns L paste mask for black."""
    w, h = alpha_canvas.size
    blur = max(1.0, max(w, h) * DROP_BLUR)
    a = np.asarray(alpha_canvas.filter(ImageFilter.GaussianBlur(blur)), dtype=np.float32) * opacity
    dx, dy = round(w * DROP_DX), round(h * DROP_DY)
    out = np.zeros_like(a)
    out[dy:, dx:] = a[:h - dy, :w - dx]          # shift down and slightly right, no wraparound
    return Image.fromarray(out.astype(np.uint8), 'L')

def square_on_white(item, size, shadow=None):     # shadow in (None, 'contact', 'drop')
    scale = FILL * size / max(item.size)
    item = item.resize((round(item.width * scale), round(item.height * scale)), Image.Resampling.LANCZOS)
    canvas = Image.new('RGB', (size, size), 'white')
    x, y = (size - item.width) // 2, (size - item.height) // 2
    if shadow == 'drop':
        a = Image.new('L', (size, size), 0)
        a.paste(item.getchannel('A'), (x, y))
        canvas.paste(Image.new('RGB', (size, size), 'black'), (0, 0), drop_shadow_mask(a))
    elif shadow == 'contact':
        ...existing sliver code...
    canvas.paste(item, (x, y), item)
    return canvas, scale
```
CLI: `--shadow {contact,drop}` with bare `--shadow` meaning contact (nargs='?', const='contact') to keep today's behaviour. Rules to keep: shadow only in listing/ and ebay/ JPGs; the site/ PNG is saved from `item` before this call, as now. Edge case: FILL = 0.85 leaves 7.5 percent margin per side, which clears a 2 percent blur plus 1.5 percent offset, so no clipping. Note the sketch's black layer is a single colour; the multiplied alpha makes it grey on white. Also matte-edge point: the existing cut() already zeroes RGB under transparent pixels, which avoids dark fringes when the item is pasted over the shadow.

## Part B: GhostMannequinEngine

1. Source and licence (VERIFIED_FETCHED, g-page.md, g-README.md). https://github.com/ccsaltik-photography/GhostMannequinEngine. 0 stars, 0 forks, three files only: README.md, ghost_auto.py, requirements.txt. No LICENSE file (raw .../main/LICENSE and LICENSE.md both 404). No licence means all rights reserved by default (general legal position, UNVERIFIED here); we could read it but not safely reuse it.

2. What it needs (VERIFIED_FETCHED). README: "Requires PyTorch, OpenCV, NumPy, SciPy, and SAM 3.1 weights in `weights/sam3.1/`". Code loads "weights/sam3.1/sam3.1_multiplex.pt" via `from sam3.model_builder import build_sam3_image_model` and `Sam3Processor`. The HF repo facebook/sam3.1 is "Status: Gated", license "other" (MCP_DATA, raw/.../hf-sam3.1.md). So the weights need an HF account and an accepted access request; Ricky's HF account would have to be granted. Whether the file name sam3.1_multiplex.pt matches that repo's files I did not check (UNVERIFIED). requirements.txt also pulls PyQt6, colour-science, watchdog and "Apple Silicon MPS" torch, a dependency bundle far larger than the work done.

3. Input type (VERIFIED_FETCHED). Two inputs: `--hanger` (garment on a hanger) and `--flat` (same garment laid flat with the back collar shown). Not form shots. The SAM text prompts are literally "clothes hanger" and "inside of jacket" (jackets, not general garments). The mask step finds the hanger plus the inside lining, so on a dress form it would be looking for a hanger that is not there.

4. How the inside-neck shot is warped (VERIFIED_FETCHED, lines 183-250). Step 1 compute_torso_global_translation: shoulder-line top profile (median row difference, dy) and chest-band centre of mass (dx) from gray < 225 masks, then a plain affine shift of the flat shot. Step 2 SAM builds a column-wise "waterfall" mask (everything above the lowest masked pixel in each column), hole-filled, polygon-simplified, dilated 2 px, feathered. Step 3 a 16-point thin plate spline (scipy RBFInterpolator, kernel thin_plate_spline) on a 25 px grid, upsampled bicubically, applied with cv2.remap: three collar-seam handles (left, centre, right at cx-170, cx, cx+170) are pulled by measured dy, with counter-balance handles 450 px lower at -0.2 times that pull so the brand label does not distort. Then everything above the fabric start in the middle 600 columns is painted flat (246,246,246). Step 4 a QC step; its seam error is a hard-coded 0.00 ("TPS directly locks the seam so 0.00px"), so the "QC bot" does not truly measure the seam (VERIFIED_FETCHED line 293).

5. Hard-coded to one photo (VERIFIED_FETCHED, lines 328-332). Crop is fixed: y 800 to 2200, x 1600 to 2800; handle offsets 170 and 450 px, fabric threshold 130, background 246. README says masters of 6720x4480. Code comments are Turkish. These are numbers from one shoot, not parameters. Anything else would need those rewritten.

6. 4060 Ti: device selection is `"mps" if torch.backends.mps.is_available() else "cpu"` (VERIFIED_FETCHED line 80). No CUDA branch. SAM 3 on a 16 GB 4060 Ti is very likely fine (UNVERIFIED, no size read), but the code would run on CPU unless one line is changed. A one-line edit, but combined with the above it is a rewrite.

7. Photoroom ghost mannequin API doc: BLOCKED (docs.photoroom.com 403 CONNECT, once). Only lane 04's SEARCH_SNIPPET stands: parameter "ghostMannequin.mode" = "ai.auto". Not re-verified here. Pricing conflicting in snippets (lane 04).

## Is ghost mannequin worth building for pre-owned vintage

Honest answer: no, not now. Reasons:
- Lane 04 found visible forms are the norm for used and vintage clothing sellers. Visible form tells buyers fit and drape, and a dress form is part of the Holliewood and Vine look (my summary of lane 04, not re-fetched).
- The only open code we found is a prototype built for jacket hanger shots at a fixed crop, no licence, gated weights, MPS/CPU only, fake QC number. Making it work on form shots means writing the form-removal side ourselves.
- Ghost mannequin needs a second inside-back shot per garment with locked camera and light: double the shooting for one-off pieces. Time spent per garment likely exceeds the benefit on a single-item listing. (UNVERIFIED judgement.)
- Diffusion ghost tools (FLUX.2 klein LoRA from lane 04) regenerate fabric and can invent collars, prints, seams. For used items that is a condition and honesty risk, since the listing must show the real piece.
- Worth keeping: the TPS idea (handle points, counter-balance, fabric-start clean-up) is sound and about 60 lines of scipy and cv2 if ever wanted.

## Recommendations
1. Do not adopt GhostMannequinEngine. Do not build ghost mannequin in v1. Ship forms-visible shots as the default look; handle anything else as a manual Photoshop or GIMP composite on rare high-value pieces.
2. Add the drop shadow mode (sketch above) to cutout.py as `--shadow drop` next to the existing contact sliver; test both on one garment on a form and one lamp, pick by eye. Keep opacity 0.20 and the site PNG shadowless.
3. Borrow nothing else from whitebg: cutout.py already trims, pads, squares and zeroes RGB under transparent pixels. If edge fringes appear on dark items, try pymatting estimate_foreground_ml as whitebg does (PyMatting adds one dependency; effect not tested here). If a later lane tests rembg's decontaminate, compare.
4. If ghosting is ever wanted, test Photoroom ghostMannequin on one garment first (needs an API key; docs not reachable here), and mark such photos honestly in the listing.

## Open questions
- Does the eBay Image Policy permit soft shadows on a white background? eBay host blocked; needs a fetch from Ricky's PC.
- Does facebook/sam3.1 contain a file named sam3.1_multiplex.pt, and how fast does Ricky get gated access?
- Photoroom ghost mannequin API: current parameters, price per image, and quality on a dress form, not verified.
- Which shadow looks better on actual eBay thumbnails: contact sliver or whole-silhouette drop? Needs a visual side by side on Ricky's items.
