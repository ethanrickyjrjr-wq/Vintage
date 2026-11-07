# eBay photo studio research (2026-11-07)

Asked by Ricky: how to make eBay-grade photos of vintage clothes on nice vintage mannequins with the background whited out, as automatically as possible, researched everywhere (Hugging Face, GitHub, eBay, Reddit) and set up for the Windows PC. Two Sonnet sweeps ran from a cloud session on 2026-11-07. Synthesis and decisions: `docs/ebay-photo-studio.md`. The PC card: `docs/ebay-photo-studio-handoff.md`.

**Network note.** The cloud session's proxy refused www.ebay.com, community.ebay.com, reddit, huggingface.co (the website; the Hugging Face connector worked), youtube, amazon and every vendor site. GitHub, raw.githubusercontent.com, GitHub release downloads and PyPI worked. So the tool lanes are verified from source; the discovery lanes are search-snippet level and list their pages in `fetch-later.md` (153 URLs) for crawl4ai on the PC. Pages were fetched with `tools/crawl-cloud.sh`; each raw file has its source URL on line 1.

## Lanes

| File | Lane | Evidence |
|---|---|---|
| `01-rembg.md` | rembg CLI, flags, models, licences, GPU notes, 2.0.87 vs 2.0.86 | fetched |
| `02-models.md` | BiRefNet variants, BEN2, InSPyReNet, SAM2, IS-Net, RMBG; licences; which for fabric and glass | fetched plus Hub data |
| `03-hf-spaces.md` | browser route: Hugging Face Spaces for background removal, the RMBG-1.4 trap, try-on Spaces | Hub data; invoke disabled |
| `04-ghost-mannequin.md` | the invisible-mannequin method, open source and AI tools, whether vintage sellers use it | GitHub fetched, rest snippets |
| `05-ai-tryon.md` | virtual try-on models, licences, why not for listings | Hub data, GitHub, snippets |
| `06-pipeline.md` | folder-in folder-out spec, rembg p -w source read, reference repos, Windows GUIs | fetched |
| `07-enhance.md` | upscalers, sharpening, colour workflow | GitHub fetched, snippets |
| `08-prior-work.md` | what this repo had already verified and decided, and what the old script lacked | repo files |
| `09-disc-reddit.md` | Reddit seller wisdom: nothing reachable, substitute sources | snippets only |
| `10-disc-youtube.md` | about 60 tutorial URLs, grouped | snippets only |
| `11-disc-mannequins.md` | forms to buy, pinning kit, three tiers | snippets only |
| `12-disc-lighting.md` | lights, backdrop, paper, tripod, three tiers | snippets only |
| `13-disc-ebay-ai.md` | eBay's own photo tools and rules, re-read from the 2026-10-30 pages | 2026-10-30 pages plus snippets |
| `14-disc-hosted.md` | Photoroom, Pixelcut, remove.bg, Canva, Claid, Pixian and others | snippets, two carried quotes |
| `15-disc-competitors.md` | how top vintage shops shoot; house style for Hollie | snippets only |
| `16-disc-ebay-community.md` | eBay community threads on forms, white, the in-app remover | snippets only |
| `17-disc-phone-builtin.md` | iPhone and Windows built-in removers, a phone step card | snippets, two GitHub pages |
| `18-gpu-windows.md` | the pinned GPU install for the RTX 4060 Ti and the CPU route | fetched |
| `19-bench.md` | three models on nine photos, judged by eye, with sheets in `test-results/` | measured here |
| `20-shadow-ghost-code.md` | whitebg's shadow code (MIT), GhostMannequinEngine read in full | fetched |
| `21-hf-deeper.md` | BiRefNet HR-matting, dynamic, lite-2K, BEN2 cards; the transformers route; ONNX options | Hub data |

## Claim check (sweep B, two independent refuters per claim)

| Claim headed for the decision doc | Verdict | Note |
|---|---|---|
| BiRefNet weights are MIT and fine for commercial use | Corrected | MIT confirmed on the GitHub LICENSE and on 15 of 16 ZhengPeng7 Hub repos; one repo (BiRefNet-DIS5K-TR_TEs) carries no licence tag. "Fine for commercial use" is what MIT permits, not a vendor statement. |
| rembg runs bria-rmbg by default; RMBG-2.0 needs a paid BRIA agreement for commercial use | Confirmed | rembg README: "The default." and "requires a paid agreement for commercial use". |
| eBay: 24 photos, 1600 recommended, 500 minimum, 12 MB | Corrected | 24 and "maximum 12MB each" (per file) exact. The 500 floor is worded two ways: help page "minimum resolution of 500 x 500 pixels"; picture policy "at least one photo that is 500 pixels on the longest side". |
| eBay forbids borders, added text or artwork, watermarks of any type; no stock photos for used items | Confirmed | Picture policy list quoted verbatim. The help page words the graphics rule more softly ("can affect your listing's placement"). |
| eBay web tool makes solid white; the app adds AI scenes | Confirmed | Help page id=4148. |
| rembg 2.0.87 needs Python 3.11 or newer; onnxruntime decides the ceiling | Corrected | PyPI says `<4.0,>=3.11`; the README's requirements block says `<3.14`; onnxruntime wheels today cover 3.11 to 3.14. Use 3.12. |
| pillow-heif 1.8.1 has Windows wheels and opens iPhone HEIC | Corrected | Wheels for cp310 to cp315 win_amd64 confirmed; the README says HEIC, not "iPhone". |
| remove.bg ends 2026-12-01 and moves to Canva | Confirmed | "no longer be available from 1 December 2026 at 9:00am CET"; API users are sent to Leonardo.ai. |
| Photoroom API $0.02 per image, PNG JPEG WEBP HEIC; free accounts non-commercial | Split | One refuter found the saved 2026-10-27 page with "$0.02 per image" and the formats and the T&C wording; the other could not. Treat as verified 2026-10-27, re-check on the PC. |
| rembg README: -dc for batches, not with -a or -ppm | Corrected | README says combining -dc and -a "changes nothing" (redundant, not harmful) and to prefer -dc for batches; -ppm thresholds the mask to binary. |
| rembg p -w behaviour | Corrected | Watchdog, existing files first, same-name PNG, stop.txt confirmed; the first pass is recursive while the watch is not; no HEIC registration found. |
| Etsy renders transparent PNG black, so marketplaces need flat JPEG | Corrected | Etsy quote confirmed; "marketplaces" overreaches, eBay's alpha handling is unverified. Flat JPEG everywhere is still the safe rule. |
| eBay clothing page: dark clothes on light, light clothes on dark | Confirmed | Seller Center selling-clothes page. |
| RMBG-1.4 is non-commercial | Confirmed | Card: "source-available model for non-commercial use", commercial licence purchasable. |
| rembg models live in ~/.rembg/models/<model>/<model>.onnx; REMBG_HOME overrides | Corrected | Default root is ~/.rembg or $XDG_DATA_HOME/rembg; REMBG_HOME sets the root and models land in `$REMBG_HOME/models/<model>/`; SAM uses two files. |

## Tests on Ricky's photos (`test-results/`)

- `before-after.jpg`: dress front, dress back and the framed print, original beside the cut.
- `frame-six-models-three-repairs.jpg` and `frame-test.py`: six rembg models by raw, closing and convex-hull repair on the print. Only birefnet-general kept the frame; the hull repair completed it.
- `shisa-print-rect-repair-v1-scar-top-edge.jpg` and `-v2-top-edge.jpg`: Ricky saw the first repair "more broken than before" at full size. v1 restored only pixels the model called background and left the half-transparent band around the old notch, which bled white as a scar and as bites on the right bar. v2 makes the whole interior of the outline solid from the photo, keeping only the outer 3 px soft. `shisa-print-rect-repair-straightened.jpg` adds the `--straighten` perspective correction. `shisa-print-reframed.jpg` is Ricky's answer to the whole problem: rebuild the frame from its own bar (`--reframe`); the mat and print stay as shot. A mat rebuild was tried and dropped: tiling showed seams and the window detection once cut the signature.
- `bench-*.jpg` and `19-bench.md`: general, lite and isnet on nine photos. General never failed; lite is 35 to 40 percent faster and matches it on clean garments but loses thin frame bars and shelf contents; isnet failed on seven of nine.
- `*-cut-birefnet-general*.jpg`: the listing outputs at 1024 px.
- `memtest.md`: why every multi-photo run died on photo two here (onnxruntime CPU arena growth, 9.7 GB peak) and the fix (arena off, 8.1 GB flat across three photos).

## What to do on the PC

`fetch-later.md` holds the 153 blocked URLs and a one-line crawl4ai loop. After that run, the snippet-level lanes (09 to 17) can be re-verified and the prices in the decision doc replaced with fetched ones.
