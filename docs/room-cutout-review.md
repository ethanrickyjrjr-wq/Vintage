# Room editor asset review — 2026-10-27

The five proposed new items cannot yet become honest whole-item layers from
the supplied photographs. This is a visual source review, not a segmentation
benchmark: no missing portion was generated, filled, or reconstructed.

| Item | Source inspected | Why unavailable | Re-shoot needed |
| --- | --- | --- | --- |
| A5 Elvis frame | `site/assets/crops/IMG_6616_elvis.webp` and full `IMG_6616.webp` | Bottom edge is outside the photograph; another frame covers the lower-left part. Rectification cannot recover either area. | Whole frame, square-on, unobstructed. |
| A22 dress form | Full `site/assets/photos/IMG_6607.webp` | Legs extend beyond the bottom of the photo. A coat, belts and a foreground woven object cover substantial parts of the form. | Full form and base, with accessories and foreground objects removed. |
| A8 silver busts, pair | `IMG_6610_shelf_top.webp`, full `IMG_6610.webp` and the 3840-pixel export | Shelf bars cross the left bust; projector, jewelry and other objects cover portions of both busts. | Both complete busts together, with nothing in front of them. |
| A9 projector | Same shelf crop and larger export | The left bust, foreground heart and shelf lip obscure parts of the body/base. A mask can isolate visible fragments but cannot recover the complete item. | Complete projector including reels, body and base; keep cords visible. |
| A10 pink stemware | `IMG_6610_glass.webp` and full room photo | Shelf support and overlapping glasses obscure parts; burgundy background remains visible through the bowls. No glass matte was tested or approved. | Glasses separated on a seamless pale backdrop, all rims, stems and feet visible; photograph may remain the display asset. |

Do not mark these five as draggable or substitute generated catalog objects.
The seven video-still items remain unavailable for the same quality reason
already documented in the handoff: A13, A14, A15, A16, A17, A19 and A20.

## Artwork textures delivered

`tools/cutout/prepare-room-art.py` applies an inverse perspective transform to
the A3/A4 quadrilaterals already used by `site/room-products.js`. It uses the
existing 2048 × 2731 source exports, not generative editing. Each output fills
its complete rectangle, with no cell padding, baked shadow, or surrounding
shop wall. The output aspect ratio is estimated from photographed edge
lengths; it is not a verified physical measurement.

| File | Dimensions | Width / height | Size |
| --- | --- | --- | --- |
| `site/assets/cutouts/A3.webp` | 772 × 1200 | 0.643333 | 162,606 bytes |
| `site/assets/cutouts/A3--480.webp` | 480 × 746 | 0.643432 | 72,510 bytes |
| `site/assets/cutouts/A4.webp` | 764 × 1200 | 0.636667 | 44,382 bytes |
| `site/assets/cutouts/A4--480.webp` | 480 × 754 | 0.636605 | 22,614 bytes |

All pixels are opaque and content bounds are the full image dimensions.
Photographed glare on A4 and the small dark obstruction at A3's lower-right
edge remain visible. These are styling-preview textures, not condition proofs
or channel-ready listing photos. The untouched catalog photos remain first
in item details; square-on re-shoots are still needed for clean listing images.

The lossless audit PNGs in ignored `artifacts/cutouts/` match the deterministic
source warp exactly (100% pixel equality before encoding). Perspective
resampling changes pixel locations; the shipped WebP uses quality 82 and
therefore adds normal lossy compression. No claim of bitwise identity to the
unwarped original or the lossy export is made. Source hashes, bounds and the
operation are recorded in `site/assets/cutouts/room-art-provenance.json`.
No paid tool, remote image service, or channel export was used.

## Vendor checks

Read live with the project's crawl4ai installation on 2026-10-27; captured
pages remain in ignored `artifacts/cutouts/`:

- [Pillow perspective transforms](https://pillow.readthedocs.io/en/stable/reference/ImageTransform.html): documented eight-coefficient output-to-input mapping.
- [Pillow transform resampling](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.transform): bicubic is supported.
- [Pillow WebP output](https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#webp): verified `quality`, `alpha_quality`, `method`, and `exact` options.
- [rembg](https://github.com/danielgatis/rembg) and [BiRefNet weights](https://huggingface.co/ZhengPeng7/BiRefNet): MIT code/model were checked before preparing the proposed masking environment. No model was run because source occlusion already prevents complete honest cutouts. BRIA weights were not used.

Runtime used for artwork export: the pre-existing Pillow 12.3.0 and NumPy
2.4.6 environment. The dedicated ignored `.venv/cutout` preparation was stopped
once source review ruled out the proposed masking work; it is not required to
build or run the storefront.
