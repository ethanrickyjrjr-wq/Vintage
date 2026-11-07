# Verify on the PC: lanes 01 (rembg), 02 (models), 03 (HF Spaces), 06 (pipeline), 08 (prior work)

Date 2026-11-07. Sonnet subagent report, saved as returned. Brief: check each snippet-level claim in those five lanes against the pages crawled into `raw/fetched-on-pc/` on the PC, quoting licences exactly; read-only, no network.

---

**Lanes covered:** 01-rembg, 02-models, 03-hf-spaces, 06-pipeline, 08-prior-work. **Index rows:** 30. **Pages read:** 27, of which 3 are unusable (onnxruntime.ai/getting-started is a shell, eBay `listing-pictures` is an error page, r/comfyui is a feed home). **Walled:** 3 (both HF Space pages, Etsy). **Not fetched (cited, not in index):** 16 URLs, among them the BiRefNet_lite-2K and HR-matting cards, RMBG-1.4 card, rembg `bria.py`, eBay picture-policy 4113/4370, Pillow ImageOps, remove.bg FAQ, whitebg `engine.py`.

Handles are the start of the file name under `raw/fetched-on-pc/`: PYPI=pypi.org_pypi_rembg_json, ORT=onnxruntime CUDA ExecutionProvider page, BRN-HF/BRN-GH=ZhengPeng7 Hugging Face/GitHub pages, EXP=export.ebay.com photo_tips, HELP=ebay help id 4148, SC=Seller Center photo_tips, CLO=Seller Center selling_clothes, POL=policy id 4240, WOBG=withoutbg birefnet_general. Table separators in quotes are shown as "/".

## Lane 01 rembg
| Claim | URL | Verdict | Evidence |
|---|---|---|---|
| 2.0.87 latest, MIT, Python range | pypi rembg json | CONFIRMED | PYPI: `"requires_python":"<4.0,>=3.11"`, upload `2026-11-06T01:19:57`; README text `python: >=3.11, <3.14` |
| onnxruntime.ai install matrix | getting-started | NOT ON PAGE | "The installation table is visible on desktop only." |
| GPU needs CUDA 12 + cuDNN 9 (from #668) | CUDA EP doc | CORRECTED | ORT: "Starting with version 1.27, GPU packages published to PyPI (onnxruntime-gpu) ... are built with CUDA 13.0 by default." 1.26-1.21 row: CUDA 12.8, cuDNN 9.x. rembg pins `onnxruntime-gpu<2.0.0,>=1.23.2` |
| DLLs without a system CUDA install | CUDA EP doc | CONFIRMED | ORT: "pip install onnxruntime-gpu[cuda,cudnn]"; `onnxruntime.preload_dlls()` since 1.21.0 |
| Mixed onnxruntime + -gpu is a foot-gun | CUDA EP doc | NOT ON PAGE | no mixed-install warning |
| `-dc` cheap, keeps model alpha | PR 843 | CONFIRMED | "keeps the model's alpha and runs only the foreground estimation ... the cost is negligible next to inference." |
| `-vm` weights (lane lists three) and quality | PR 846 | CORRECTED | Four checkpoints; default small-distinctions-646 110 MB, base 380 MB. "Measured on two portraits, all starting from the same bria-rmbg mask"; -dc 0.09s, -a 0.59s, -vm 2.1s; "Fixed 1024×1024, deliberately." |
| BiRefNet preprocessing; HR session? | birefnet_general.py | CONFIRMED / NOT ON PAGE | `(0.485, 0.456, 0.406), (0.229, 0.224, 0.225), (1024, 1024)`. One session file only, so the HR question stays open |
| BRIA licence name "CC BY-NC 4.0" unverified | RMBG-2.0 card | CORRECTED (handoff was right) | "License: Creative Commons Attribution–Non-Commercial (CC BY-NC 4.0)"; hub tag "License: bria-rmbg-2.0" |

## Lane 02 models
| Claim | URL | Verdict | Evidence |
|---|---|---|---|
| RMBG-2.0 non-commercial; HF YAML differs | RMBG-2.0 card | CONFIRMED | "Commercial use is subject to a commercial agreement with BRIA." BRN-GH: RMBG-2.0 "weights are for only non-commercial use" |
| BiRefNet MIT, all seven variants | BRN-HF | CONFIRMED (main card only) | "License: mit". Six variant cards NOT FETCHED |
| BiRefNet_lite-2K is 2560x1440 | BRN-GH | CONFIRMED via README | "takes inputs in a much higher resolution (2560x1440)" |
| Zoo: 17 FPS, 3.45 GB, ONNX slower | BRN-GH | CONFIRMED | "17 FPS ... 3.45GB GPU memory"; ONNX "~90% more time". 44.4M params NOT ON PAGE |
| BEN2 MIT; MVANet; BEN_Base API | BEN2 onnx_run.py, arXiv | licence CONFIRMED; rest NOT ON PAGE / CORRECTED | "License: mit". Abstract: "BEN Base for initial segmentation and BEN Refiner"; no MVANet, no numbers. HF snippet is `from ben2 import AutoModel` |
| BEN2 ONNX on Windows | BEN2 onnx_run.py | CONFIRMED, caveat | loads `./BEN2_Base.onnx`, CUDA/CPU providers, but imports `torch` and `torchvision` |
| Third-party sample results | withoutbg | CONFIRMED (vendor, no garments) | WOBG: "On Bench v0 it ranks #4 of 13 by accuracy (MAE)". MAE: General 0.0169, Lite 0.0301, IS-Net 0.0410, Portrait 0.0509. Categories: People, Plants, Objects |
| Reddit BiRefNet vs BEN2 on garments | r/comfyui | NOT ON PAGE | feed home behind `js_challenge`; no relevant thread |

## Lane 03 HF Spaces
| Claim | URL | Verdict | Evidence |
|---|---|---|---|
| not-lain: BiRefNet, MIT, 2,984 likes, 20 Apr 2026 | api/spaces JSON | CONFIRMED | `"likes":2984`, `"license":"mit"`, `"models":["ZhengPeng7/BiRefNet"]`, `"lastModified":"2026-04-20T14:16:25.000Z"` |
| Hardware and running state unknown | api/spaces JSON | CONFIRMED (new) | `"stage":"RUNNING","hardware":{"current":"zero-a10g"` |
| Tabs: Image Upload, URL Input, File Output | - | NOT ON PAGE | `app.py` listed, not fetched |
| BiRefNet_demo: 339 likes, MIT, HR/matting list | Space page | WALLED | 817 bytes; shell shows only "Like 339", "Running on Zero". BRN-GH: "Online Inference with GUI with adjustable resolutions" |
| not-lain live status and limits | Space page | WALLED | 831 bytes |
| ZeroGPU quotas (item 11) | ZeroGPU docs | CONFIRMED; image caps NOT ON PAGE | "Unauthenticated / 2 minutes / Low"; "Free account / 5 minutes / Medium"; "resets exactly 24 hours after your first GPU usage" |

## Lane 06 pipeline
| Claim | URL | Verdict | Evidence |
|---|---|---|---|
| eBay 7 MB, 800-1,600 px, zoom (snippet) | export.ebay.com | CONFIRMED; zoom NOT ON PAGE | EXP: "try to make it 800-1,600 pixels on the long side. eBay's photo uploader can take images up to 7MB each." HELP says "maximum 12MB each" |
| Accepted: JPEG, PNG, TIFF, BMP, GIF | export.ebay.com | CORRECTED | EXP: "JPEG, PNG, GIF, TIFF, BMP, WEBP, HEIC, or AVIF" |
| eBay picture rules: white, shadow | `/listing-pictures` | NOT ON PAGE | error page: "Something went wrong. We’re sorry." |
| ICC to sRGB via ImageCms | Pillow docs | CONFIRMED | `profileToProfile(im, inputProfile, outputProfile, renderingIntent=Intent.PERCEPTUAL`; `createProfile(colorSpace: 'LAB','XYZ','sRGB')`. `exif_transpose` NOT FETCHED |
| CUDA/cuDNN for onnxruntime-gpu 1.23.x | CUDA EP doc | CONFIRMED | "1.26.x-1.21.x / 12.8 / 9.x ... Default GPU package build before 1.27." |
| whitebg last commit, source to borrow | whitebg tree | date CONFIRMED; source NOT ON PAGE | commit `65fac41`, "Nov 5, 2026"; page is a file list only |
| 16 GB VRAM is enough | BRN-GH | PARTLY | "Inference / 4.8GB / 3.5GB" at 1024; no 2048 figure |

## Lane 08 prior work
| Claim | URL | Verdict | Evidence |
|---|---|---|---|
| 2.0.86 date | PyPI | CONFIRMED; cutout.py header wrong | 2.0.86 `"2026-10-21T21:18:52"` (header says 10-28) |
| remove.bg ends 1 Dec 2026; Leonardo API | remove.bg pricing | CONFIRMED | "no longer be available from 1 December 2026 at 9:00am CET"; "Go to Leonardo.ai for API Pricing". Credit expiry, $3/$9: NOT ON PAGE |
| eBay 24 photos, ~1600, white tool | help 4148 | CONFIRMED | HELP: "up to 24 pictures"; "about 1600 x 1600"; "replace the background with a solid white color" |
| Overhead-lighting contradiction | help + Seller Center | CONFIRMED | HELP: "avoiding using a flash, or overhead lighting"; SC: "Take your photos in an area with bright overhead lighting." |
| Light-on-dark backdrop sentence | selling-clothes | CONFIRMED | CLO: "Use a white or light-colored background for darker clothes, and a black or dark background for lighter clothes." |
| "Take your own images"; AI-image rule | policy 4240 | CONFIRMED / NOT ON PAGE | POL: "You should take your own images and videos and write your own descriptions." No AI clause |
| Photoroom $0.02, ghost parameter, terms | API page | price CONFIRMED; terms NOT ON PAGE | "for $0.02 per image. Send PNG, JPEG, WEBP or HEIC". Lane-04 docs file: "set the parameter `ghostMannequin.mode` to `ai.auto`" (Plus plan) |
| Etsy unedited-photo exceptions | etsy legal | WALLED | 4 bytes, two CRLFs |

## Licence table
| Model or tool | Licence as the page states it | Commercial | File |
|---|---|---|---|
| rembg | `"license":"MIT"`; "Model weights carry their own licenses, independent of rembg's MIT license" | yes | PYPI |
| BiRefNet code | "MIT license" | yes | BRN-GH |
| BiRefNet weights, main card | "License: mit"; WOBG: "open weights under MIT, so commercial use is allowed" | yes | BRN-HF |
| rembg ONNX conversion | none stated; fetched from `github.com/danielgatis/rembg/releases/download/v0.0.0/BiRefNet-general-epoch_244.onnx` | unclear | birefnet_general.py |
| BEN2 | "License: mit" | yes | BEN2 onnx_run.py |
| RMBG-2.0 | "CC BY-NC 4.0"; tag "bria-rmbg-2.0" | no | RMBG_2.0 |
| ViTMatte (`-vm`) | "ViTMatte is MIT licensed" (rembg author; data terms not addressed) | yes | PR 846 |
| not-lain Space | `"license":"mit"` | yes | api JSON |

## What changes in docs/ebay-photo-studio.md
- Section 4: "Python 3.12 is the safe pick, since its README caps at 3.14". Replace: "its README says `python: >=3.11, <3.14`, PyPI allows `<4.0`; Python 3.12 is the safe pick".
- "The weights are MIT on the GitHub LICENSE and on the Hugging Face cards of every variant we would use". Replace: "The BiRefNet repo and main card are MIT (page-checked 2026-11-07); other variant cards are MIT per the Hub API only. rembg downloads its own ONNX conversion from its GitHub release."
- "rembg's default model is Bria's RMBG-2.0, and its README says ..." Verbatim confirmed (also USAGE.md: "This defaults to the `bria-rmbg` model."). Add the card line "License: Creative Commons Attribution–Non-Commercial (CC BY-NC 4.0)".
- "`ZhengPeng7/BiRefNet_demo` offers the HR and matting variants". Page walled. Replace: "is the author's official demo with adjustable resolution (variant list unchecked)". Add to the not-lain line: runs on ZeroGPU; anonymous visitors get 2 GPU minutes a day, a free account 5.
- "rembg cannot load that variant by name." Add: rembg's BiRefNet session resizes to 1024x1024.
- "Bria RMBG-1.4 and RMBG-2.0 (non-commercial)": 2.0 confirmed; the 1.4 card was not opened.
- remove.bg quote: add "(re-fetched 2026-11-07, 'at 9:00am CET')".
- Photoroom "one of two checkers could not re-find it, so re-check on the PC". Replace: "re-found 2026-11-07: '$0.02 per image'; ghost mannequin is a separate Plus-plan call".
- Section 8: "eBay's current wording on AI-edited photos and whether a Seller Center page recommends a form or mannequin". Replace: "Policy 4240 has no AI clause. Seller Center photo-tips and selling-clothes never mention a form or mannequin; export.ebay.com says 'Show the fit by using a model, dress form, or mannequin'."

## Surprises
- onnxruntime-gpu from 1.27 defaults to CUDA 13.0, and `rembg[gpu]` only pins `<2.0.0`. Check which build pip took before following a CUDA 12 recipe.
- rembg's BiRefNet mask is computed at 1024x1024 (session source; WOBG "Input 1024×1024"), and `-vm` is fixed 1024 too. Lace and fringe detail is decided at 1024 px, which favours the HR route.
- ViTMatte's published numbers are portraits from a bria-rmbg mask; `-dc` had the lowest contamination (49.2 against 51.3 for `-vm`).
- WOBG: Lite's error is about 1.8x General's, and Portrait ranks below IS-Net, so skip the portrait model.
- eBay says 7 MB on the export site and 12 MB on the US help page.
- BRN-GH: RMBG-2.0 weights are "not aware of transparency", which supports the glass and sheer limits.
