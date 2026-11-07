# Lane 03: Hugging Face Spaces, the zero-install browser route

Status (2026-11-07): Searched and read through the Hugging Face MCP (level MCP_DATA). huggingface.co, hf.space, Wikimedia and hearstapps are refused by the proxy from this machine (curl code 000). Live invocation was NOT possible: dynamic_space invoke returned "The invoke operation is disabled because gradio=none is set." So there is no timing, no queue figure and no output sample. Hardware and running/sleeping status were not returned by hub_repo_details (only SDK, likes, updated date, tags). Raw notes: research/ebay-photo-studio-2026-11-07/raw/03-hf-spaces/.

## Findings

1. The best background-remover Space is not-lain/background-removal. MCP_DATA, hf://spaces/not-lain/background-removal. 2984 likes, gradio, updated 20 Apr 2026, README "license: mit". It runs BiRefNet ("ZhengPeng7/BiRefNet") under @spaces.GPU (ZeroGPU), and applies the mask as alpha ("image.putalpha(mask)"), so the output is a transparent PNG, not a white background. Tabs: Image Upload, URL Input, File Output ("Output PNG File").
2. Official BiRefNet demo: ZhengPeng7/BiRefNet_demo, 339 likes, updated 21 Feb 2026, MIT. README lists BiRefNet, BiRefNet_HR, BiRefNet_HR-matting, BiRefNet-matting, BiRefNet-portrait, BiRefNet_lite. HR and matting variants are the ones to try on lace and fringe. MCP_DATA.
3. The BiRefNet model card says "license: mit". MCP_DATA, hf://models/ZhengPeng7/BiRefNet. Fine for selling.
4. Licence trap: Xenova/remove-background-web (774 likes, in-browser, runs in your browser so nothing is uploaded) uses briaai/RMBG-1.4, whose card says "RMBG v1.4 is available as a source-available model for non-commercial use." Shop use is commercial. Avoid it for listings. RMBG-2.0 is gated. MCP_DATA.
5. ECCV2022/dis-background-removal (478 likes) is Apache-2.0, model doevent/dis (older DIS network). Older, weaker than BiRefNet. MCP_DATA.
6. MCP-ready variants hf-applications/background-removal (17 likes) and Upsampler/birefnet-background-removal (8 likes, MIT) run the same BiRefNet code. The not-lain app itself says to use hf-applications for MCP. Tool background_removal_fn, one parameter: a public image URL (view_parameters worked). MCP_DATA.
7. Ghost mannequin: only two Spaces exist and both have 0 likes: amrhisham123/clawset-ghost-mannequin (gradio, Apr 2026) and meowmeows1/wardrobe-ghost-mannequin (docker, Jun 2026, MIT). The first says "Ghost mannequin effect powered by rembg + clothing segmentation + Stable Diffusion inpainting", works at 512x512 inpaint size, with an off-white (250,250,248) background, no licence field, API-style (base64 in). Not a bookmark candidate; a code idea at best. Search "invisible mannequin" returned nothing. MCP_DATA.
8. Virtual try-on: Kwai-Kolors/Kolors-Virtual-Try-On (10217 likes, Space licence Apache-2.0), WeShopAI (560, "license: other", needs HF login), Miragic (558, no licence). These put a garment on a generated person, which changes the item's look; eBay buyers expect the real item. Use for ideas only, not listing photos. MCP_DATA.
9. discover lists exactly one Background Removal Space (not-lain/background-removal) and no clothing/try-on category. Image-edit Spaces exist (FLUX.1-Kontext-Dev, Qwen-Image-Edit LoRAs, Flux.2-Klein, Photo-Mate-i2i) but I could not run them. MCP_DATA.
10. Product photo / garment searches found nothing popular (top is Jaroliya/AI-Product-Photography, 10 likes). tonyassi/clothing-segmentation (60 likes) segments clothing and could drive a ghost-mannequin pipeline locally. SEARCH via MCP, MCP_DATA.
11. Unverified from memory: ZeroGPU Spaces queue for free anonymous users, daily GPU quotas, and image size caps. I did not fetch any HF limits page. UNVERIFIED.

## Recommendations for Ricky

- Bookmark two: not-lain/background-removal (transparent PNG, MIT, BiRefNet) and ZhengPeng7/BiRefNet_demo (try HR/matting for hair, lace, fringe). Use the URL tab or Output PNG File tab, then composite onto pure white 255,255,255 at home (a transparent PNG must be flattened; eBay main photos want a white or clean background).
- Treat Spaces as the no-setup backup for a handful of items. For the whole inventory, the local BiRefNet on the RTX 4060 Ti is faster, private, and not quota limited (same model, MIT).
- Do not use RMBG-1.4 tools for listings (non-commercial).
- Do not rely on try-on or generative Spaces for listing photos; a mannequin shot should show the real garment.
- Ghost mannequin: no usable Space. Lane 04 should cover the local method (two shots, composite).

## Open questions

- Hardware, sleeping or running status, queue times and file size limits for each Space (not returned by the MCP).
- Does BiRefNet leave a fringe on mannequin necks and stands? Need a real test with Ricky's photos.
- Is the HF MCP invoke ever allowed (gradio header)? Needed for a real timing test.

## URLs to fetch once the network opens

- https://huggingface.co/spaces/not-lain/background-removal (live status, hardware, limits; host blocked now)
- https://huggingface.co/spaces/ZhengPeng7/BiRefNet_demo (runtime, hardware)
- https://huggingface.co/docs/hub/spaces-zerogpu (ZeroGPU quotas and queue, to replace finding 11)
- https://huggingface.co/api/spaces/not-lain/background-removal (runtime stage and hardware JSON)
- https://github.com/ZhengPeng7/BiRefNet (local install, model zoo, licences)
