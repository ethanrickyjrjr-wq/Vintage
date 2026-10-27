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

The urn lamp's shade is clipped at the top. The dress form, harness and jacket overlap other inventory; the Elvis frame is obscured. These limitations must stay visible and cannot be repaired by segmentation. Sizes are unmeasured, so all cards say **Size coming**. Research price targets are labelled guide prices. The SOLD badge is explicitly demo data.

The archived photo JPEGs are 1050×1400, and the crop sources are at most 1400 pixels along their long side. Some site WebPs are larger derivatives, not higher-resolution originals. None qualifies for a 1500-pixel source-subject channel export; no channel JPEGs are manufactured by upscaling.

## Actual collection colours

Browser-computed values in the isolated storefront, verified in both themes: `#collection` is transparent, and its inherited page background is **#422831 by day** and **#291d24 in evening**. `atmosphere.css`, loaded after `storefront.css`, overrides the base cream/plum tokens. This corrects the handoff's section 1 interpretation. The pilot loads both unchanged stylesheets in the same order, and offers separate cream (#f6efdf) and burgundy (#451c2b) wall controls. No hero CSS is edited.

Comparison results and browser validation will be recorded after the pilot runs.
