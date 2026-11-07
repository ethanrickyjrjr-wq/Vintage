# Lane 07-enhance: post-processing after the cut-out

Status (2026-11-07): Fetched and saved under raw/07-enhance/: GitHub pages and release pages for Real-ESRGAN, Upscayl, waifu2x-ncnn-vulkan, SwinIR, chaiNNer, ImageMagick, XnConvert, realsr-ncnn-vulkan, QualityScaler, catalog-image-upscaler, plus pypi.org JSON for realesrgan and rawpy. Blocked (proxy 403 on CONNECT, tested twice or once): www.ebay.com, irfanview.com, xnview.com, topazlabs.com, helpx.adobe.com, pixelcut.ai, imagemagick.org, wikipedia, support.apple.com, community.ebay.com, expertphotography.com, alanranger.com, dev.to, realesrgan.org, and the eBay-size blogs (img.vision, pixotter, nightjar). Not run: Hugging Face MCP (not needed for this lane). Anything marked UNVERIFIED is from memory or reasoning, not a source.

## Findings

1. Real-ESRGAN is BSD-3-Clause, latest GitHub release is v0.3.0, PyPI realesrgan 0.3.0 uploaded 2022-09-20. VERIFIED_FETCHED. Sources: https://github.com/xinntao/Real-ESRGAN , https://pypi.org/pypi/realesrgan/json (raw: github.com_xinntao_Real-ESRGAN.md, f7.md). The Windows portable ncnn build listed is realesrgan-ncnn-vulkan-20220424-windows.zip (https://github.com/xinntao/Real-ESRGAN/releases , VERIFIED_FETCHED). So the project's last tagged release is about four years old. The package runs on PyTorch (CUDA on the 4060 Ti is UNVERIFIED for this repo, but chaiNNer's page below confirms CUDA for PyTorch models generally).

2. Upscayl: AGPL-3.0, latest release v2.15.0 "New Year Update", assets stamped 2024-12-25. VERIFIED_FETCHED. https://github.com/upscayl/upscayl and /releases. It uses Real-ESRGAN with Vulkan. Exact quote on GPU: "Yes, unfortunately. NCNN Vulkan requires a Vulkan-compatible GPU. Upscayl won't work with **most** iGPUs or CPUs." Another line: "Upscayl uses AI models to enhance your images by guessing what the details could be." That second sentence is the core trust problem for clothing: the model invents texture. Windows build exists (release notes mention Windows users; installer asset names not captured). It is a GUI with batch folder mode (batch mode UNVERIFIED from memory).

3. waifu2x-ncnn-vulkan: MIT, latest release 20250915 (a 20250802 pre-release before it). VERIFIED_FETCHED. https://github.com/nihui/waifu2x-ncnn-vulkan/releases . Vulkan GPU. Quote from the release notes: "It was only tested on Linux platform. So, please check if it works on Windows." A later note says "fix palette png loading in windows", so Windows builds exist. waifu2x is trained for anime art and its fit for photographic fabric is UNVERIFIED and doubtful.

4. realsr-ncnn-vulkan (RealSR, photo oriented, same author) exists, page fetched: https://github.com/nihui/realsr-ncnn-vulkan , VERIFIED_FETCHED for existence only (raw f13.md). Licence and date not captured.

5. SwinIR is Apache-2.0, official repo, 66 commits, research code (PyTorch, needs Python setup). VERIFIED_FETCHED. https://github.com/JingyunLiang/SwinIR . No Windows installer; not worth it for this job.

6. chaiNNer: GPL-3.0, latest "Alpha v0.26.1" (changelog mentions Windows file-watch fix). VERIFIED_FETCHED. https://github.com/chaiNNer-org/chaiNNer and /releases. Node-graph batch tool that runs ESRGAN-family and other models. Quotes: "Nvidia GPUs: Full support via PyTorch (CUDA), ONNX, and TensorRT." and "Windows versions 8.1 and below are also not supported." The v0.26.0 notes say "This is the last release (minus any patches for necessary bug fixes) with the Python backend", so the app is mid-rewrite. Release date not captured. chaiNNer can do the whole post chain (load folder, resize, levels, sharpen, save) in one graph, which is its real value here, with or without an upscaler.

7. ImageMagick: open source, 25,049 commits, ships Install-windows.txt, command-line batch tool. VERIFIED_FETCHED. https://github.com/ImageMagick/ImageMagick . Licence file exists (name not captured; ImageMagick's own licence is Apache-like, UNVERIFIED). Best fit for a scripted, no-GUI batch: resize to 1600, auto-level, unsharp, strip metadata, JPEG quality.

8. XnConvert (XnSoft) GitHub page fetched (raw f9.md); xnview.com is blocked so the Windows free-for-private-use licence is UNVERIFIED. Batch GUI with resize, auto levels, sharpen is UNVERIFIED from memory. Note: if Ricky sells commercially, check the licence terms before relying on the free tier.

9. QualityScaler (Djdefrag) is a Windows GUI AI upscaler using DirectX 12 (topic tags on the page: amd, anime, directx-12, compression-artifact-reduction). VERIFIED_FETCHED for existence and topics. https://github.com/Djdefrag/QualityScaler . Not needed.

10. Upscaling guidance from search: "Real-ESRGAN can't restore detail the original lacks", "high scaling may also amplify artifacts if the input is noisy or compressed", "AI upscaling can distort small lettering". SEARCH_SNIPPET (summary of realesrgan.org and wavespeed.ai pages, both pages unfetchable). Supplier-photo guides pitch upscaling for tiny 500 px sources, which is the opposite of Ricky's case.

11. eBay size: sources agree the floor is 500 px and the recommendation is 1600 px on the long side, but disagree whether zoom triggers at 800 or 1600. SEARCH_SNIPPET only; eBay's own page is blocked. Safe move is 1600 px or larger on the long side either way. An iPhone 12 MP photo is roughly 4032 x 3024 (UNVERIFIED from memory), so it is about 2.5 times the needed size and gets downscaled, not upscaled.

12. Colour and trust: an eBay Community thread says "if the color is off or the item does not look true to its' physical appearance, then you need new pictures", and that a phone shot of white clothing came out yellow about 10% of the time. SEARCH_SNIPPET (page blocked). A Shopify blog titled "how to color correct product images in adobe lightroom and minimize returns" exists (URL below, blocked). I found no source quantifying returns from over-processing, so any return-rate number would be invented. The reasoning that over-edited colour and fake texture cause "not as described" returns is UNVERIFIED but is the standard seller worry.

13. Grey card: the neutral card lets software set the white point for the whole image. SEARCH_SNIPPET (Wikipedia quote, page blocked). Lightroom batch method: set white balance on the card shot, then Copy Settings with only White Balance ticked and paste to the rest of the same session. SEARCH_SNIPPET (Adobe community thread). Lightroom needs a subscription (SEARCH_SNIPPET).

14. iPhone: tap and hold on the product until AE/AF lock appears, so exposure and focus stop hunting. SEARCH_SNIPPET (alanranger.com, blocked). The stock Camera app has no grey-card custom white balance in these results; a third-party app such as ProCamera offers manual WB lock (it was paid in 2015, price now unknown). ProRAW or RAW needs a capable app and settings (UNVERIFIED).

15. Perspective and lens correction: nothing fetched. From memory (UNVERIFIED): shoot from chest height, phone level and parallel to the mannequin, 2x lens or 3 to 6 feet back to avoid wide-angle stretch; Lightroom and Photoshop have Upright and Lens Correction; ImageMagick has -distort Perspective; darktable and RawTherapee are free with keystone tools. Verify these before building anything on them.

16. Vendor tools (Topaz Photo AI, Pixelcut upscale, Photoshop Image Processor and Actions, Lightroom presets, Affinity batch, IrfanView batch): all blocked this run. No price, version, or feature claim made. URLs listed below.

## Answer: should an upscaler run on 12 MP phone photos for a 1600 px listing?

No. The source is about 2.5 times larger than the target (item 11, size claim UNVERIFIED), so the correct operation is a high-quality downscale, which itself sharpens perceived detail. An upscaler only earns a place for a rescued photo under about 1000 px (a supplier image, an old scan, a screenshot from video). Even then, Upscayl's own description ("guessing what the details could be") means fabric weave, lace, buttons and print can be invented, which is a returns risk on vintage. If a rescue is ever needed: Upscayl on the 4060 Ti, 2x only, then inspect at 100%.

When sharpening or denoising is justified (reasoning, UNVERIFIED as a rule but consistent with the snippets): apply a light unsharp mask once, after the final downscale, never before; denoise only on dim, high-ISO shots (dark velvet, interiors), and mild. Skip both for a clean daylight shot. The background-removed edges should be checked for halos before sharpening, since sharpening exaggerates fringes.

## Recommendations for Ricky

1. Shoot right so little post is needed: window light or two lamps, same light for the whole batch, phone level, tap-hold for AE/AF lock.
2. Two-line colour workflow for the iPhone: Put a plain grey card or a sheet of plain white printer paper in the first frame of each rack session under the same light, tap-hold on it to lock exposure and focus, then shoot the garments without changing the light. Back at the PC, set white balance from that card frame once and paste it to the whole session (Lightroom Copy Settings, or the auto-levels step in the batch script), then compare one finished photo against the real garment before exporting.
3. Post chain on the PC, no AI upscaler: cut-out, white background, resize to 1600 px long side (or larger, decide after the eBay zoom rule is confirmed), gentle auto-levels or white-point from the card, optional single light unsharp, JPEG at about 85 to 90 quality, strip metadata. Do it in ImageMagick (scriptable, matches the batch script) or chaiNNer if a visual graph is wanted.
4. Include one honest, unprocessed natural-light shot per garment plus a close-up of fabric and flaws; this protects against colour disputes (reasoning).
5. Do not buy Topaz or a Pixelcut plan for this; revisit only if rescue upscaling becomes frequent.

## Open questions

- What is eBay's exact zoom threshold (800 or 1600) and current max file size? Needs eBay's page.
- Do XnConvert and IrfanView free licences allow commercial use? Needs their sites.
- Does Ricky already own Lightroom or Photoshop?
- Which iPhone model, and does he shoot HEIC or JPEG? HEIC needs conversion in the batch.
- Latest chaiNNer, Upscayl installer filenames and release dates (chaiNNer date not captured).

## URLs to fetch once the network opens

- https://www.ebay.com/help/selling/listings/creating-managing-listings/photo-requirements?id=4113 : eBay's own size, zoom, background rules (blocked now: yes)
- https://imagemagick.org/script/command-line-options.php : exact flags for -resize, -unsharp, -auto-level, -distort, -strip (blocked: yes)
- https://www.xnview.com/en/xnconvert/ and https://www.irfanview.com : licence, batch features (blocked: yes)
- https://www.topazlabs.com/topaz-photo-ai : price, version, specs (blocked: yes)
- https://helpx.adobe.com/photoshop/using/processing-batch-files.html and Image Processor docs : batch details (blocked: yes)
- https://www.shopify.com/blog/115603781-how-to-color-correct-product-images-in-adobe-lightroom-and-minimize-returns : colour correction and returns (blocked: yes)
- https://en.wikipedia.org/wiki/Gray_card : grey card definition (blocked: yes)
- https://www.alanranger.com/blog-on-photography/how-to-take-product-photos-with-iphone : iPhone lock steps (blocked: yes)
- https://community.ebay.com/t5/Selling/Help-How-do-I-get-ACTUAL-Color-depicted-in-my-photos/td-p/27847415 : seller colour complaints (blocked: yes)
- https://pixelcut.ai : upscaler pricing (blocked: yes)
