# Mask-only catalog pilot

Run from the repository root in PowerShell. This is local image tooling, not a site runtime dependency. It never changes source photos, catalog records, the hero, or hosting settings. `site/pilot-cutouts.html` is deliberately absent from the static build's allowlist.

## Environment

```powershell
uv venv --python 3.12 .venv/cutout
uv pip install --python .venv/cutout/Scripts/python.exe -r tools/cutout/requirements.txt
$env:U2NET_HOME = (Join-Path (Get-Location) '.venv/models/rembg')
.venv/cutout/Scripts/rembg.exe d birefnet-general
```

`d` takes a positional model. All segmentation explicitly selects `birefnet-general`, including the Python API's `new_session`; **never invoke the default model**. The general ONNX checksum is enforced by rembg. The MIT model cards and pinned revisions are recorded in `docs/cutout-pilot-results.md`.

The four-image challenger requires PyTorch. Its model predicts alpha only. Reviewed model code is loaded from the pinned local snapshot, using safetensors and `local_files_only=True`; its network-oriented `handler.py` is not executed. The `eval` calls in the model select architecture classes from its internal configuration. Backbone pretraining is disabled in the downloaded config, so the legacy `torch.load` backbone path is not taken.

```powershell
hf download ZhengPeng7/BiRefNet_HR-matting --revision 5d6b6f8adcb5b417c871b1d84ceaae9871355b7f --local-dir .venv/models/BiRefNet_HR-matting
uv pip install --python .venv/cutout/Scripts/python.exe torch==2.5.1 torchvision==0.20.1 --index-url https://download.pytorch.org/whl/cpu
uv pip install --python .venv/cutout/Scripts/python.exe -r tools/cutout/requirements-matting.txt
```

On this machine the Hugging Face Xet transfer stalled. The fallback was the same revision's official `/resolve/<revision>/model.safetensors` HTTPS download. Expected SHA256: `a5a4de698739ea5e0e8bbab28e1b293dde95092b87a442d566cbc585c53cef55`. CPU PyTorch 2.5.1 and torchvision 0.20.1 were verified with rembg's NumPy 2.5.4 requirement; the older model requirements' `numpy<2` pin cannot be shared with current rembg.

## Reproduce

```powershell
.venv/cutout/Scripts/python.exe tools/cutout/pipeline.py prepare
.venv/cutout/Scripts/python.exe -u tools/cutout/pipeline.py general
.venv/cutout/Scripts/python.exe -u tools/cutout/pipeline.py matting
.venv/cutout/Scripts/python.exe tools/cutout/pipeline.py export
.venv/cutout/Scripts/python.exe tools/cutout/pipeline.py sheets
node site/build.mjs
.venv/cutout/Scripts/python.exe -m http.server 4182 --bind 127.0.0.1 --directory site
```

Open `http://127.0.0.1:4182/pilot-cutouts.html`. Optional query parameters: `style=all|white|cream|burgundy|shelf`, `theme=day|evening`, `wall=theme|cream|burgundy`. Port 4182 is separate from the existing storefront preview.

Each pipeline stage accepts `--ids A1 A2 ...`. Run stages sequentially: they update the same manifest. `items.json` holds crop coordinates (fractions of the oriented source), alpha-only background exclusions, perspective corners, fit, anchor, and review scale. Glass and obscured objects can explicitly use `mode: keep`. All incomplete objects remain labelled layout tests.

Keep the entire photographed mannequin/display support with anything placed on it. `displaySupport: true` rejects input crops; `includePolygons` restores omitted support areas using alpha alone. B6 includes the full head, neck and base. A22/B10 retain the full photographed display and visible chair. B7 retains its original so all chair parts stay visible. WebP and JSON writes are atomic, and every pipeline process must finish before build/staging.

- `prepare`: byte-identical originals and hashes in ignored `media/<id>/orig.jpg`; sRGB, oriented, at-most-2048-pixel working sources under ignored `artifacts/pilot/work/`. Archives are the available preview originals, not claimed full-resolution camera masters.
- `general`: one CPU session; A is the same prediction/decontamination code path as `rembg i -m birefnet-general -dc`; A0 is the non-decontaminated control with the same alpha. Session-load time is separate from per-image inference and colour-processing time.
- `matting`: the four test subjects at a 2048×2048 model input, CPU fp32. A larger model input does not create more source detail.
- `export`: source RGB plus the selected alpha, alpha-only bbox, transparent 4:5 contain. 960×1200 and 480×600 WebP, quality 82 (lowered only to meet 200 KB), alpha_quality 100. RGB under alpha 0 is cleared. Perspective-only art is sampled from the original; existing glare and occlusion remain.
- `sheets`: A/B/C on white, black and burgundy, with adjacent native 1:1 crops; `test-<id>.jpg`, `mask-contact-sheet.jpg` and `trial-results.json` under ignored `artifacts/pilot/`.

The pixels-kept check runs **before** trimming, resizing and lossy encoding: at least 99% of alpha≥250 pixels must differ by at most 3/255. An empty opaque set fails. Mask-only recomposition is exactly 100%; decontaminated and naive arms are measured independently. WebP decoding loss is recorded separately in `encoding_comparison` and must not be described as a failed mask or as a pixel-identical final file.

No channel exports are produced in this pilot. Current available source subjects are below 1500 pixels; upscaling to 2048 would not fix that. `media/` contains no alpha files. A future approved rollout must obtain suitable originals and emit flattened, undecorated sRGB JPEGs with the source original retained.

Capture the page at 1440, 390 and 320 CSS pixels in both themes for each style, into `artifacts/pilot/`. Results and remaining photo limitations are in `docs/cutout-pilot-results.md`. Commit only named pilot paths; never stage `media/`, `.venv/`, artifacts, or another session's work. Publishing and catalog rollout wait for the owner's style choice.

After browser QA has written `browser-captures.json` (including section rectangles) and `browser-checks.json`, run `pipeline.py pagesheets` to assemble the four combined style sheets and `styles-overview.jpg`, and append the browser evidence to the committed audit. The local-only pilot loads all study images eagerly so full-page screenshots include every item. Production catalog loading is unchanged.
