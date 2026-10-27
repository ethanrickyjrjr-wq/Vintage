# Catalog cutout pilot

Scope: handoff Phases 0–2 only. Local review; no publication and no catalog rollout. Work is isolated on `codex/cutout-pilot` in `../Vintage-cutout-pilot`, preserving the original checkout's uncommitted disco and room work.

## Setup (2026-10-27)

- Python 3.12.13, a new `.venv/cutout` environment. No packages installed into the crawl4ai environment.
- `rembg[cpu,cli]==2.0.86`, Pillow 12.3.0. Pillow replaces Sharp to keep one image-processing script. Pillow 13 conflicts with the CLI's Gradio requirement; 12.3 supports the required WebP options.
- General model is explicitly `birefnet-general`; never the rembg default. Confirmed `rembg i -m birefnet-general -dc` in installed CLI help. Download command is `rembg d birefnet-general` (positional model, no `-m` option on `d`).
- Live licence checks: [BiRefNet](https://huggingface.co/ZhengPeng7/BiRefNet), MIT, revision `e2bf8e4460fc8fa32bba5ea4d94b3233d367b0e4`; [HR-matting](https://huggingface.co/ZhengPeng7/BiRefNet_HR-matting), MIT, revision `5d6b6f8adcb5b417c871b1d84ceaae9871355b7f`. General ONNX is distributed by rembg with expected MD5 `7a35a0141cbbc80de11d9c9a28f52697`.
- [Pillow WebP options](https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#webp) verified against installed `WebPImagePlugin.py`: quality, alpha_quality, method, exact. Exports use quality 82, alpha_quality 100, method 6, exact true after clearing RGB under zero alpha.
- The Firecrawl CLI is not installed; vendor pages were checked with web browsing and the installed `hf` CLI.
- No generative image tool is used. Models predict alpha only; final product RGB comes from the oriented, sRGB, downsized source. Trials also measure rembg's decontaminated output independently.
- `media/` and `.venv/` are ignored. Originals are archived byte for byte with hashes; the source files are untouched. Masks and test renders live under ignored `artifacts/pilot/`.

## Source limitations

The urn lamp's shade is clipped at the top. The dress form, harness and jacket overlap other inventory; the Elvis frame is obscured. These limitations stay visible. Sizes are unmeasured, so all cards say **Size coming**. Research price targets are labelled guide prices. The SOLD badge is explicitly demo data.

Owner direction: **retain complete photographed display supports**. B6 includes the entire mannequin head, neck and base with the feather hat. A22 and B10 use the full scene source and retain the supporting forms, clothing and visible chair; alpha-only support masks recover chair areas omitted by the model. B7 keeps the original photograph because the automatic mask omits chair parts. Source camera framing is preserved, with no additional crop through a support and no reconstruction. This rule is also recorded in the handoff and enforced by the input-crop guard in the pipeline.

The archived photo JPEGs are 1050×1400, and the crop sources are at most 1400 pixels along their long side. Some site WebPs are larger derivatives, not higher-resolution originals. None qualifies for a 1500-pixel source-subject channel export; no channel JPEGs are manufactured by upscaling.

## Actual collection colours

Browser-computed values in the isolated storefront, verified in both themes: `#collection` is transparent, and its inherited page background is **#422831 by day** and **#291d24 in evening**. `atmosphere.css`, loaded after `storefront.css`, overrides the base cream/plum tokens. This corrects the handoff's section 1 interpretation. The pilot loads both unchanged stylesheets in the same order, and offers separate cream (#f6efdf) and burgundy (#451c2b) wall controls. No hero CSS is edited.

## Phase 1: four-item comparison

All arms use the same oriented sRGB source crop. A uses rembg's general prediction and `-dc` code path; B uses HR-matting at 2048×2048, CPU fp32; C retains the source without segmentation (zero model inference time; I/O excluded). General session loading took 9.15 s, HR loading 6.17 s, separately from the image timings below.

| Item | A: general + decontamination | B: HR-matting | Pilot decision |
|---|---|---|---|
| A1 urn lamp | 15.05 s. **FAIL as-is:** the adjacent Elvis frame is also selected; lamp outline is usable. | 115.46 s. **FAIL:** stray hanger, softened foot and adjacent frame. | General alpha plus an alpha-only exclusion of the neighbouring frame. **Layout only:** original shade and foot remain incomplete. |
| A2 chandelier | 17.48 s. **FAIL glass:** improved gaps, but opaque-looking shards. | 118.56 s. **FAIL glass:** uneven translucency and background haze, especially on white. | **Keep original.** Seamless-backdrop re-shoot. |
| A10 pink glass | 11.38 s. **FAIL glass:** old wall visible inside opaque-looking bowls. | 118.27 s. **FAIL:** most glasses vanish; unrelated clothing survives. | **Keep original.** Re-shoot with defined glass edges. |
| B9 fringed boots | 11.35 s. **PASS for layout:** boots, toes, soles and existing fringe remain; source is soft. | 120.81 s. **FAIL:** shafts and most fringe disappear; toe regions remain. | General alpha for layout; re-shoot for sharp listing photographs. |

The mechanical test passes for every raw A trial (99.79%–100% of alpha≥250 pixels within 3/255), all A0 controls, and all four B trials. **This alone does not prove a correct mask:** B's opaque coverage is only 2.18% for the boots and 6.70% for the glasses. Visual review rejects them despite unchanged RGB. No generative model is involved.

Final mask studies reapply the selected alpha to the original prepared RGB: **100% opaque RGB retention before trimming, resizing and lossy WebP**. Exported alpha is verified bit for bit after WebP decoding. Lossy RGB encoding differences are recorded separately, without applying the mask-integrity pass/fail threshold to compression.

Eight transparent studies ship as pilot assets: six masks (A1, A22, B6, B9, B1, B10) and two perspective crops (A3, A4). A2, A10, B7 and A5 retain the original photograph. The complete hat display is retained; A22/B10 retain their full photographed display groups, including the chair. The harness photograph preserves its whole chair; the Elvis frame remains obscured by another picture. Glare, wear, occlusion, cords and labels are not retouched away.

All eight studies have 960×1200 and 480×600 variants, quality 82, alpha quality 100; largest file 118,492 bytes, below 200 KB. The third lamp image is explicitly a detail crop of its existing original, not another angle. Channel export is deferred and there are no transparent files under `media/`.

Inspect the committed [audit](../tools/cutout/pilot-audit.json) for source hashes, dimensions, flags, versions, timings, coverage and export checks. Local generated evidence (ignored): `artifacts/pilot/pass-fail.jpg` (one-page table), `test-A1.jpg`, `test-A2.jpg`, `test-A10.jpg`, `test-B9.jpg`, `mask-contact-sheet.jpg`; native 1:1 hard-area crops appear to the right of every tile on white, black and burgundy. The original archives and full manifest are under `media/`.

## Phase 2: local tile pilot

Browser screenshots and final validation are in progress. Catalog rollout and publication remain stopped for the owner's style choice.
