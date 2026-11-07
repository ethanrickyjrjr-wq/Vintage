# Lane 06 pipeline: folder-in, folder-out photo pipeline

Status (2026-11-07): Fetched and saved under raw/06-pipeline/: PyPI JSON for Pillow, pillow-heif and rembg; rembg README (rendered and raw); rembg/commands/p_command.py source; GitHub pages for rembg, whitebg, rembg-clean, shadow-aware-bg-removal, the Backblaze sample, free-rembg-desktop, bg_remover, vdanielvpl/rmbg, python-batch-background-remover, pillow_heif; pillow-heif README; Pillow ImageOps.py source. Blocked (403 CONNECT): huggingface.co, www.ebay.com, pillow.readthedocs.io, onnxruntime.ai. api.github.com also refused (GitHub API not enabled for the session). "Last commit date" is empty in every rendered GitHub page (it is a relative-time element), so last-commit dates are NOT established; only star counts, commit counts and licences are. No GPU here, nothing was run.

## 1. Verified facts

- VERIFIED_FETCHED. Pillow 13.0.0 on PyPI, requires_python ">=3.11", uploaded 2026-10-16, Windows amd64 wheels for cp311 to cp315. Source: https://pypi.org/pypi/Pillow/json (raw/06-pipeline/pypi-Pillow.json).
- VERIFIED_FETCHED. pillow-heif 1.8.1, requires_python ">=3.10", BSD-3-Clause, uploaded 2026-10-11, win_amd64 wheels cp310 to cp315. Source: https://pypi.org/pypi/pillow-heif/json. Its README: "register_heif_opener()" adds HEIF to Pillow in one line (https://raw.githubusercontent.com/bigcat88/pillow_heif/master/README.md). Same README warns the discontinued sibling pi-heif is affected by a libheif heap overflow: "If you decode untrusted HEIC/HEIF files, migrate to the latest `pillow-heif` release". So use pillow-heif, not pi-heif.
- VERIFIED_FETCHED. rembg 2.0.87, requires_python "<4.0,>=3.11", MIT, uploaded 2026-11-06. Requires "pillow<14.0.0,>=12.3.0" (so Pillow 13.0.0 is fine). The cli extra pulls in "watchdog<7.0.0,>=6.0.0", click, gradio, fastapi, uvicorn. GPU extra is "onnxruntime-gpu<2.0.0,>=1.23.2". Source: https://pypi.org/pypi/rembg/json. Python 3.11 to 3.13 is the safe target on the PC; 3.14 and 3.15 are listed in classifiers but onnxruntime support decides (README: "Python version support is determined by onnxruntime's compatibility").
- VERIFIED_FETCHED. rembg repo: 25.4k stars, 2.5k forks, 565 commits, MIT. https://github.com/danielgatis/rembg
- VERIFIED_FETCHED. Install lines from the README: `pip install "rembg[cpu,cli]"` and `pip install "rembg[gpu,cli]"`. Warning quoted: "NVIDIA GPUs may require `onnxruntime-gpu`, CUDA, and `cudnn-devel`... If `rembg[gpu]` doesn't work and you can't install CUDA or `cudnn-devel`, use `rembg[cpu]` with `onnxruntime` instead." Plan for the 4060 Ti: try [gpu,cli] first, fall back to [cpu,cli] (birefnet-general on CPU is slow but works).
- VERIFIED_FETCHED. Model: "birefnet-general ... A pre-trained model for general use cases." Also "birefnet-general-lite" and "birefnet-general-fp16 ... Roughly 30% faster on CUDA with near-identical masks; it does not reduce VRAM" (needs `pip install "rembg[fp16]"`). Default model when no -m is bria-rmbg ("`bria-rmbg` is the default"), so always pass -m birefnet-general explicitly. NOTE for orchestrator: bria-rmbg weights have their own licence terms; I did not fetch them (UNVERIFIED), another lane should check.
- VERIFIED_FETCHED. Batch: "rembg p path/to/input path/to/output" ("Used for batch processing entire folders") and "**Watch mode (process new/changed files automatically):** rembg p -w path/to/input path/to/output". Edge colour fix flag: "rembg p -dc path/to/input path/to/output" (decontaminate; "It only changes color, never coverage"; "If you are batch-processing and cannot inspect each result, prefer `-dc` over `-a`: it is faster and cannot fail"). `-ppm` makes a hard binary mask (no soft edges). Server: "rembg s --host 0.0.0.0 --port 7000" with a Gradio UI, "--no-ui" to disable it.
- VERIFIED_FETCHED (source read). p_command.py has `-bgc/--bgcolor` taking four ints "Background color (R G B A) to replace the removed background with" (default 0 0 0 0). The README itself never mentions -bgc, so rely on the source. Output is always PNG: `each_output = (output / each_input.name).with_suffix(".png")`. Skip rule: if that output already exists the input is skipped. `-d` deletes the input after processing. Source: https://raw.githubusercontent.com/danielgatis/rembg/main/rembg/commands/p_command.py
- VERIFIED_FETCHED (source read), important behaviour of `-w`: it processes all existing files first, then uses watchdog Observer, non-recursive, handling every event except "deleted", "closed", "closed_no_write", "opened". There is no wait for a file to finish copying, so a half-written phone upload can be read mid-copy (errors are caught and printed, and the file is not retried unless another event fires). Dropping a file named `stop.txt` in the input folder ends the watch loop. It names output after the input name, so it cannot name by item id and view, cannot read HEIC (no pillow-heif registration appears in the file; I grep-checked: absent), does no EXIF rotation, no crop, no white, no manifest. Conclusion: use rembg as a library inside our own script and our own watchdog loop; do not rely on `rembg p -w` as the pipeline.

## 2. Pipeline spec (numbered)

Folder layout on the PC: `inbox/` (phone drop, subfolder per item optional), `work/` (transparent cutouts), `out/ebay/`, `out/master/`, `out/site/`, `failed/`, `manifest.csv`, `stop.txt`.

1. Watcher: our script with `watchdog` (already installed by rembg[cli]). On create/move events for .heic .heif .jpg .jpeg .png, wait until size is stable for 2 s (two identical size readings) before reading. On start, process everything already in inbox/ that lacks outputs. A file named `stop.txt` ends the loop (copying rembg's convention). A one-shot mode (`--once`) does the same without watching.
2. Naming: input names come from the phone (IMG_1234.HEIC), so item id and view must be supplied. Recommended: shoot into a subfolder named by item id (inbox/A13/ with files in shot order); view names map by order front, back, side, detail, label, tag (configurable list). Fallback: a `names.csv` or a filename prefix `A13-front.heic` if Ricky renames on the phone. Output: `A13-front.jpg`.
3. Decode: `pillow_heif.register_heif_opener()` then `Image.open`; apply `ImageOps.exif_transpose` (exists in Pillow source, ImageOps.py line 758) before anything else; convert to RGB; if an ICC profile is present convert to sRGB (ImageCms, UNVERIFIED from memory, Pillow docs host was blocked). Drop unrelated EXIF (GPS) on output.
4. Cutout: one `new_session("birefnet-general")` created at start and reused for every image (model load takes tens of seconds, whitebg README says first launch "takes 30 to 60 s"). Call `remove(img, session=session, decontaminate=True)` so colour halos do not show on white. Optional fallback model flag for lace and fur (`-a`, or vitmatte) per item.
5. Mask checks, both on the alpha channel: (a) "pixels changed" warning: fraction of pixels with alpha below 250 relative to the subject bounding box, and fraction of the original that was removed; flag if removed area is below 3 percent (nothing cut) or above 90 percent (subject lost), thresholds are proposals to tune on Ricky's example photos; (b) "see-through" warning: count of partially transparent pixels (alpha 20 to 235) strictly inside the largest connected component's filled region; a high ratio means holes or ghosting in sheer fabric, lace, glass or a mannequin gap, flag for manual review. Both go in the manifest, nothing is silently fixed.
6. Save transparent PNG to `out/site/A13-front.png` (full resolution cutout, cropped to subject plus margin) for the Holliewood and Vine site. Cutout PNG is lossless so keep it as the master.
7. Crop to subject bounding box of alpha > 8, add margin (proposal 6 percent each side, same default as whitebg).
8. Optional soft natural shadow (flag `--shadow`, default per decision below): blurred copy of the alpha, flattened vertically and offset downward, Gaussian blur radius proportional to subject height, opacity about 25 percent, composited on white before the subject. No reflection.
9. Composite on pure white (255,255,255) and pad to a square canvas centred; final fit 1600 x 1600 for eBay (`out/ebay/`), LANCZOS downscale. A second 2048 x 2048 master JPEG goes to `out/master/` (not uploaded to eBay unless Ricky wants).
10. Light sharpen after the resize (UnsharpMask radius 0.8, percent 60, threshold 2, proposal), only on the final size.
11. Save JPEG quality 90, sRGB, `optimize=True`, 4:4:4 or default subsampling; strip transform-unrelated metadata; check the file is under 7 MB (see eBay note below), lower quality in steps of 2 down to 84 if not.
12. Manifest: append row to `manifest.csv` (CSV, UTF-8): source_file, item_id, view, output_ebay, output_master, output_png, width, height, removed_pct, pixels_changed_warning, see_through_warning, model, shadow, processed_at_utc, status. Rewrite atomically (write temp, rename) so Excel opening it does not break the run.
13. Idempotence and failures: skip an input whose outputs and manifest row exist (hash of file bytes recorded); on exception move the input to `failed/` and write a status row; never delete inputs.
14. GPU use: onnxruntime picks CUDA if rembg[gpu] installed; log which provider ran. Process one image at a time; BiRefNet at full size can use several GB VRAM, 16 GB is enough (UNVERIFIED claim, measure on the PC).
15. Launcher: a `run-watch.bat` that activates the venv and runs the script; a `--once` bat for batch runs.

## 3. Reference repos (all fetched from the GitHub web page this run; none was run)

| Repo | Stars | Commits | Licence | What it does | Fit |
|---|---|---|---|---|---|
| danielgatis/rembg https://github.com/danielgatis/rembg | 25.4k | 565 | MIT | The engine. CLI i/p/s/b, library, models incl. birefnet-general | Use as library |
| jimmyXiang123/whitebg https://github.com/jimmyXiang123/whitebg | 0 | 11 | MIT | Closest match: rembg then crop to subject, padding, square, exact NxN, white or transparent, `--shadow`, edge decontamination, EXIF fix, models u2net / birefnet-general-lite (default) / birefnet-general, Tkinter GUI plus CLI, skips existing outputs, multiprocessing, Windows 10/11, Python 3.11+. Defaults: 1200x1200 JPG, 6 percent padding, no shadow. No HEIC or watch mention (grep found neither). | Best to read and borrow from; very new and unproven (0 stars) |
| mess/rembg-clean https://github.com/mess/rembg-clean | 1 | 2 | GPL-3.0 | Batch CLI for product photos with a custom defringing step against white halos; needs GIMP installed for one mode | Idea only; GPL means do not copy code into our scripts if we ever distribute |
| crispinzz/shadow-aware-bg-removal https://github.com/crispinzz/shadow-aware-bg-removal | 1 | 18 | Contradictory: tagline says "MIT", licence section says "All rights reserved ... proprietary; no use or redistribution without written consent" | Keeps the real contact shadow by measuring it; BiRefNet ONNX plus own shadow model; "A 12 MP photo takes about 25 s on a laptop CPU" | Read the idea only; do not use the code |
| backblaze-b2-samples/rembg-product-background-removal https://github.com/backblaze-b2-samples/rembg-product-background-removal | 0 | 7 | MIT | rembg to transparent PNG, Backblaze B2 as ingest and storage | Not useful (cloud storage coupling) |
| Shivam-Singh-Coder/python-batch-background-remover https://github.com/Shivam-Singh-Coder/python-batch-background-remover | 0 | 5 | none stated | rembg plus Pillow folder to transparent PNG | Trivial, skip |

Finding: no repository turned up that is specific to eBay listing photos (SEARCH_SNIPPET, one extended search; the search tool's own wording was "didn't turn up a repo built specifically for eBay listing photos"). Nothing has meaningful community usage except rembg itself. Our own ~200-line script is the right choice; whitebg is a good reference for crop, pad and shadow code.

## 4. Windows GUI alternatives

| Tool | Stars | Licence | How it installs | Notes |
|---|---|---|---|---|
| `rembg s` built-in web UI (README) | part of rembg | MIT | `pip install "rembg[cpu,cli]"` then `rembg s`, open http://localhost:7000 | Gradio UI, one image at a time, no white/crop/pad; good for spot fixes |
| whitebg GUI | 0 | MIT | git clone, venv, `pip install -r requirements.txt`, `python -m whitebg`; PyInstaller portable exe is possible | Drag-drop, thumbnails; "Speed first about 2 to 6 s/image, Quality first about 15 to 20 s/image" (their numbers, on their hardware) |
| Remove-Background-ai/free-rembg-desktop https://github.com/Remove-Background-ai/free-rembg-desktop | 35 | No licence line found on page | Windows installer `RemBG.Desktop.Setup.1.1.0.exe` (79.7 MB) from Releases, SHA256 listed, run as administrator | Bulk drag-drop; tied to the rembg.com service (the README links https://www.rembg.com/en); I did not confirm whether processing is local, so treat as UNVERIFIED local-only. Not the danielgatis library. |
| MIBlue119/bg_remover https://github.com/MIBlue119/bg_remover | 1 | not checked | Python, Tkinter, PyInstaller | Tiny; skip |
| VdanielVPL/RMBG https://github.com/vdanielvpl/rmbg | 5 | GPL-3.0 | Wails app wrapping the rembg CLI | Small; skip |
| Upscayl-style apps | not searched | n/a | n/a | Upscayl is an upscaler, not needed at 1600 px from a phone photo |

I did not find a verified Electron or .NET wrapper around BiRefNet with batch plus white background. Not claimed.

## 5. Decisions recommended

- Shadow: on by default for clothing on forms and for lamps and glass? Recommendation: no shadow for the main (first) eBay image of apparel on a form (cleanest "white background" look, avoids a fake grey smear on the form's base); soft natural shadow ON for objects that would otherwise float (lamps, glass, shoes, hat, art on easel). Make it a per-item flag, default off, and always keep the shadowless PNG. Reason partly from whitebg's own stance, "A soft drop shadow to avoid the 'sticker' look", and defaults of no shadow (VERIFIED_FETCHED). eBay policy on shadows was not verifiable (ebay.com blocked); other lanes cover it.
- Size: make 1600 x 1600 the upload size and keep 2048 as an archive master. Evidence is SEARCH_SNIPPET only: third-party pages say eBay minimum is 500 px long side and zoom works best at about 1600 px; eBay's own export page (https://export.ebay.com/en/manage-listings/photo-tips) says up to 7 MB per image per the search summary. A 2048 px square JPEG at q90 on a detailed garment is often 1 to 2 MB (UNVERIFIED estimate), so 2048 is allowed by size, but the extra pixels bring slow listing loads and no proven benefit. Verify on eBay's own page once the host opens.
- Format: JPEG q90 sRGB for eBay (universal, small); keep PNG only for our own site where transparency matters (the search summary lists JPEG, PNG, TIFF, BMP, GIF as accepted but a transparent PNG sent to eBay would be flattened unpredictably). Never upload the transparent PNG to eBay.
- Model: pass `-m birefnet-general` explicitly (default is bria-rmbg); use `decontaminate=True`; try `birefnet-general-fp16` later for about 30 percent speed on CUDA.
- Do not use `rembg p -w` as the pipeline; use our watcher with a file-stability wait.

## 6. Open questions

- Does Ricky shoot per-item subfolders or can he rename on the iPhone? Determines item id mapping (step 2).
- Python version on the PC (3.11 to 3.13 recommended) and whether `rembg[gpu]` finds CUDA and cuDNN on first try.
- Are mannequin gaps (neck, arms, hollow torso) a problem? Ghost-mannequin and "mannequin visible" styles are lanes 04 and 05; this pipeline just flags see-through areas.
- bria-rmbg licence (default model) and BiRefNet weights licence not fetched.
- Real timing of birefnet-general on the 4060 Ti is unknown; measure on first run.
- eBay's current rules on background colour, shadows, max file size, minimum size (ebay.com blocked).

## 7. URLs to fetch once the network opens

- https://www.ebay.com/help/selling/listings/creating-managing-listings/picture-policy?id=4113 and https://www.ebay.com/help/selling/listings/listing-pictures (eBay picture policy and sizes; confirms min size, 7 MB, white background and shadow rules; ebay.com blocked now). The exact URL paths are from memory, find them via the help search.
- https://export.ebay.com/en/manage-listings/photo-tips (reachable? untested via crawl; search listed it) for the 7 MB and 800 to 1600 px statement.
- https://pillow.readthedocs.io/en/stable/reference/ImageOps.html and /ImageCms.html (blocked) to confirm exif_transpose and the sRGB conversion call.
- https://huggingface.co/briaai/RMBG-1.4 and RMBG-2.0 (blocked; use MCP hf_fs) for the licence of the rembg default model.
- https://onnxruntime.ai/docs/execution-providers/CUDA-ExecutionProvider.html (blocked) for the CUDA and cuDNN version matrix matching onnxruntime-gpu 1.23.x.
- https://github.com/jimmyXiang123/whitebg/blob/main/whitebg (source files, to lift crop, pad, shadow code) and its CHANGELOG, plus a commits page for last-commit dates (GitHub was reachable; I did not read the source files this run).
