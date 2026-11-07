# 02 Models: open-source background removal and matting for vintage clothing

Status (2026-11-07): Fetched and saved under raw/02-models/: GitHub pages and raw READMEs for BiRefNet, transparent-background, BEN2, SAM2, DIS, rembg and Bria RMBG-2.0; LICENSE files for rembg, BiRefNet, BEN2, SAM2, DIS, transparent-background; Hugging Face hub details for all 11 requested repos (hf-hub-details.md) and card excerpts (hf-cards-excerpts.md). Blocked: huggingface.co, www.ebay.com and www.reddit.com web hosts (curl 403 on 2026-11-07, tested once each); the RMBG-2.0 card itself via hf_fs (gated, access denied). No GPU here, so nothing was run; speed numbers are the authors' own. No head-to-head benchmark on lace, fringe, glass or sheer fabric was found, so every ranking below is a judgement from model design and training data, and Ricky's own sample photos must decide it.

## Findings

### Licences (the commercial-use question matters because the shop sells things)
- BiRefNet, all seven variants: hub field "License: mit" on each of BiRefNet, _HR, -matting, _HR-matting, _dynamic, _lite, -portrait. MCP_DATA, hf-hub-details.md. GitHub LICENSE is MIT as well (raw_githubusercontent_com_ZhengPeng7_BiRefNet_main_LICENSE.md, VERIFIED_FETCHED). Commercial use is fine.
- BEN2 (open Base weights): hub field "License: mit"; GitHub LICENSE "MIT License / Copyright (c) 2025 Prama LLC". MCP_DATA plus VERIFIED_FETCHED. The card says "Our Base model is open source" and "For access to our commercial model email us at sales@backgrounderase.com", so the better hair/4K model is not the free one.
- RMBG-2.0: hub field "License: other", Status gated (MCP_DATA). GitHub README, VERIFIED_FETCHED (gh-bria-rmbg2.md): "License: Creative Commons Attribution–Non-Commercial (CC BY-NC 4.0)" and "Commercial use is subject to a commercial agreement with BRIA." rembg's README agrees: "RMBG-2.0 is released under a BRIA license ... that requires a paid agreement for commercial use." A web search snippet notes the HF YAML points to a Bria custom licence rather than the CC deed (SEARCH_SNIPPET). Verdict: do not use RMBG-2.0 for the shop. This matters because rembg's DEFAULT model is bria-rmbg, so a bare `rembg i` silently uses a non-commercial model. Always pass `-m birefnet-...`.
- RMBG-1.4: hub "License: other", license_name bria-rmbg-1.4; card: "RMBG v1.4 is available as a source-available model for non-commercial use." Same verdict. VERIFIED via hf_fs (MCP_DATA).
- transparent-background (InSPyReNet): README badge and LICENSE "MIT License / Copyright (c) 2022 Taehun Kim". VERIFIED_FETCHED.
- SAM 2: README "The SAM 2 model checkpoints, SAM 2 demo code (front-end and back-end), and SAM 2 training code are licensed under Apache 2.0". VERIFIED_FETCHED.
- DIS / IS-Net: README "Our code and evaluation metric use Apache License 2.0." VERIFIED_FETCHED. Caveat in same README: the released weights were trained on DIS5K V1.0, "which includes very few animal, human, cars, etc. So it may not work well on these targets."
- rembg itself: LICENSE "MIT License / Copyright (c) 2020 Daniel Gatis". VERIFIED_FETCHED. Individual model weights carry their own licence.
- skytnt/anime-seg: hub "License: apache-2.0" (MCP_DATA). Trained for anime characters; irrelevant to clothing, skip.

### BiRefNet family (the main candidate)
- Zoo, VERIFIED_FETCHED (rawreadme-BiRefNet.md). Standard model (swin_v1_large, 220.7M params) runs at 1024x1024. Lite is swin_v1_tiny, 44.4M params, DIS-VD scores 0.882/0.830 vs 0.911/0.875 for large. Quote: "the standard BiRefNet can run in `17 FPS` with `resolution==1024x1024` with `3.45GB GPU memory` on a single `RTX 4090`." Table: 4090 57.7 ms FP16, 95.8 ms FP32; inference memory 4.8 GB FP32, 3.5 GB FP16. A 4060 Ti 16 GB has far more VRAM than needed at 1024; the 2048 HR models use more (author gives no HR figure; UNVERIFIED estimate: roughly 4x pixels, test it).
- BiRefNet_HR: card, "This BiRefNet was trained with images in `2048x2048` for higher resolution inference." Its own table shows it scores wF .894 at 2048 but only .840 at 1024 (the base model scores .877 at 1024). So feed HR at 2048 or not at all. Use for large phone photos where fringe or lace detail is lost when downscaled to 1024.
- BiRefNet_HR-matting: "trained with images in `2048x2048` for higher resolution image matting with transparency." Best candidate for soft edges. Its table shows HR-matting and plain BiRefNet-matting are nearly equal on AM-2k (.997/.996 wF); HR gains show more on real high-res photos than on this metric.
- BiRefNet-matting: "official weights of BiRefNet for general matting". Trained on P3M-10k, TR-humans, AM-2k, AIM-500, Human-2k, Distinctions-646, HIM2K, PPM-100: people, animals, objects, hair. Trimap-free (README: "general trimap-free matting use").
- BiRefNet_dynamic: "trained on arbitrary shapes (256x256 ~ 2304x2304) and shows great robustness on inputs with any shape." Card claims it beats general and HR on its validation sets. Good default for mixed portrait/landscape phone photos with no resize guessing.
- BiRefNet_lite: 44.4M params; the CPU / small-GPU fallback. rembg wraps its ONNX as birefnet-general-lite.
- BiRefNet-portrait: trained on P3M-10k and TR-humans (people). A mannequin is a human-shaped object, so it may do well on torsos but it never saw fabric fringe; test, do not assume.
- Windows route, VERIFIED_FETCHED: (1) `pip install rembg[gpu,cli]` and `rembg i -m birefnet-general ...` (rembg README); (2) transformers: `AutoModelForImageSegmentation.from_pretrained('ZhengPeng7/BiRefNet', trust_remote_code=True)` (card pattern, shown for lite); (3) ComfyUI nodes, README lists Comfy-Org official integration plus lldacing/ComfyUI_BiRefNet_ll and others; (4) ONNX files in GitHub release v1; README warns ONNX costs "~90% more time" (SwinL, ~165 ms on A100) and "Pay attention to the compatibility among `onnxruntime-gpu, CUDA, and CUDNN`". Native PyTorch FP16 is faster than ONNX; rembg uses ONNX, so the transformers route is faster on the 4060 Ti but rembg is simpler.
- What rembg wraps, VERIFIED_FETCHED (rembg README model list): birefnet-general (BiRefNet-general-epoch_244.onnx), birefnet-general-fp16 ("Roughly 30% faster on CUDA with near-identical masks; it does not reduce VRAM"), birefnet-general-lite, birefnet-portrait, birefnet-dis, birefnet-hrsod, birefnet-cod, birefnet-massive, bria-rmbg ("The default"), isnet-general-use, isnet-anime, u2net family, silueta, sam, u2net_cloth_seg. NOT wrapped: BiRefNet_HR, HR-matting, matting, dynamic (no such names in the list), BEN2, InSPyReNet. So rembg cannot reach the best BiRefNet variants; use transformers/ComfyUI for HR-matting and dynamic.
- Edge post-processing in rembg, VERIFIED_FETCHED: `-dc` decontaminate colours (cheap, "leave on for a whole batch"), `-a` alpha matting (slow, can fail to converge), `-vm` ViTMatte ("recovers more of the wispy strands ... cannot fail to converge"; small ~110 MB, base ~380 MB). rembg's own advice: for portraits "`birefnet-portrait` with `-dc` is a good starting point, and `-vm` when the hair detail matters". For batch work "prefer `-dc` over `-a`". Note `-ppm` makes the mask binary and kills soft edges; never use for fringe or lace.
- BiRefNet's own refine_foreground (foreground colour estimation): "accelerate refine_foreground by 8 times (~80ms now on 5090)". This is the same halo-removal idea as rembg -dc; use it in the transformers route.

### BEN2
- 94.6M params, ONNX weights on hub, safetensors. Confidence Guided Matting: "a refiner network that targets and processes pixels where the base model exhibits lower confidence levels". Card claims strength in "hair matting, 4K processing" but that is for the commercial full model; "Our Base model is open source." GitHub also ships `BEN2_Base.onnx` plus `onnx_run.py`. Batch warning: "batch size not exceed 3 for consumer GPUs". `refine_foreground=True` adds time and improves edges. Not wrapped by rembg. Windows: `pip install -e "git+https://github.com/PramaLLC/BEN2.git#egg=ben2"` then `BEN_Base.from_pretrained("PramaLLC/BEN2")`. No independent benchmark on clothing found. Worth an A/B on Ricky's samples because it is a second MIT-licensed model with a different architecture (MVANet-based per README text), cheap to try.

### transparent-background (InSPyReNet)
- MIT. CLI and Python `Remover`; modes `base`, `fast`, `base-nightly`; `--resize dynamic` "will produce better results in terms of sharper edges but maybe unstable"; default static. Supports `--jit`. Windows GPU: README gives `pip install --extra-index-url https://download.pytorch.org/whl/cu118 transparent-background` (also CUDA 12.8 line). Output RGBA estimates foreground with pymatting, optional GPU acceleration. Older architecture (2022); BiRefNet generally supersedes it for fine detail, but it is a light, well-behaved batch tool. Not wrapped by rembg. Rank as backup, not primary.

### SAM 2 (manual fallback)
- Apache 2.0. SAM 2.1 checkpoints tiny/small/base_plus/large. Click-or-box prompt segmentation: `SAM2ImagePredictor(build_sam2(cfg, ckpt))` with point or box prompts; also HF `facebook/sam2-hiera-large`. Needs python>=3.10, torch>=2.5.1; README: "If you are installing on Windows, it's strongly recommended to use ... WSL"; CUDA extension build failure "you can ignore it". Binary masks only, hard edges, no alpha. Use for the awkward cases where the automatic model grabs the mannequin stand, the rack or the wrong garment: click the garment, take the mask, then refine edges with BiRefNet-matting or ViTMatte inside the SAM box. rembg wraps a quantized SAM ViT-B (`rembg i -m sam -x '{ "sam_prompt": [...] }'`), which gives a Windows-friendly route without WSL.

### IS-Net (DIS)
- Apache 2.0, the predecessor of BiRefNet in the DIS lineage; rembg wraps `isnet-general-use`. README concedes the academic weights saw few humans. BRIA RMBG-1.4 is IS-Net based. Use only as a fast CPU fallback; BiRefNet-lite beats it per the author's DIS-VD numbers (lite .830 wF vs the paper table in the zoo; no isnet number in README, so no numeric claim).

### Glass and sheer (honest limits)
- No source found demonstrates true see-through alpha on glass or sheer fabric for any of these models. SEARCH_SNIPPET (fuser.studio, ComfyUI guide, lofttools): RMBG-2.0 and rembg "neither ... made it see-through"; "the table and room colours visible through the glass stay inside the cutout"; commercial services "still pull ahead" on "semi-transparent glass". These are blog claims, not tests of ours.
- Practical consequence: segmentation models give a mask, not physically correct transparency. For glass and sheer pieces the dependable route is photographic: shoot on the final white backdrop with light, rather than cutting out. For white-background eBay listings, a glass piece cut out onto white loses its transparency look anyway. UNVERIFIED but standard practice; flag to the lighting lane.

## Ranked recommendation

(a) Dressed mannequin shots (solid or textured garments, mannequin or dress form in frame): 
1. BiRefNet_dynamic via transformers (FP16, MIT), or birefnet-general via rembg with `-dc` if simplicity wins. 
2. BiRefNet_HR at exactly 2048 for large phone photos with embroidery or trim. 
3. BEN2 Base as an A/B. 
Important: decide whether the mannequin stays in the picture (a "ghost" or on-form look). If the form should be removed or kept with the garment, models cannot decide: segment the whole object (form + garment), keep the form, or use SAM2 clicks. Dress forms with a pole and base need the base masked out with SAM2 or a crop.

(b) Soft or hairy edges (fur, fringe, feathers, lace, chains): 
1. BiRefNet_HR-matting at 2048 (transformers), then BiRefNet's refine_foreground. 
2. BiRefNet-matting at 1024 (cheaper, near-equal on the card's metric). 
3. rembg `birefnet-general` plus `-vm` ViTMatte (the only way to stay inside rembg). 
Skip `-ppm`. Fine chain links and lace holes will still show background; check each with a dark preview.

(c) Glass and sheer: none are proven. Best open try: BiRefNet_HR-matting, preview on black and on white; if holes or milky regions appear, shoot the item on the white sweep and skip cutout, or use SAM2 for a clean silhouette and accept opaque appearance. Avoid RMBG family (licence and the search-snippet warning).

(d) CPU-only laptop fallback: 
1. birefnet-general-lite through rembg (ONNX, MIT, 44.4M params). Note rembg says the fp16 variant "on CPU it is usually slower", so use the plain lite. 
2. isnet-general-use. 
3. transparent-background `--mode fast`. 
No CPU timings were verified (UNVERIFIED); expect seconds to tens of seconds per photo, to be measured on the real laptop.

## Recommendations for Ricky and the build
1. Install a small test harness on the PC that runs the same 5 to 10 sample photos through birefnet_dynamic, HR-matting, matting, birefnet-general via rembg `-dc`, BEN2 Base and transparent-background, saving each result on white and on black, then pick by eye. That is the only reliable decision per the evidence above.
2. Pin the licence rule in the script: never call rembg without `-m`, because the default is the non-commercial bria-rmbg.
3. Keep SAM2 as a manual "click the garment" tool for hard shots, not part of the automatic batch.
4. Plan white-background finishing after the cutout: composite on pure white (255,255,255) with a soft contact shadow; eBay's own background policy lives in another lane.

## Open questions
- Does Ricky want the mannequin visible in the final image or removed (ghost mannequin)? It changes the model workflow and the shooting plan.
- Real VRAM and seconds per image on the 4060 Ti for HR-matting at 2048 (authors give none).
- BiRefNet_lite-2K (README mentions 2560x1440) was not read; check its hub card.
- The BEN2 architecture claim (MVANet decoding) is from the README batch comment only; the arXiv 2501.06230 paper was not read.
- Is the HR model's ONNX conversion available? The rembg list shows none.

## URLs to fetch once the network opens
- https://huggingface.co/briaai/RMBG-2.0 : the actual licence text and gating terms (hf_fs was denied; web page blocked).
- https://huggingface.co/ZhengPeng7/BiRefNet and /BiRefNet_lite-2K : full usage code blocks, 2K model card.
- https://huggingface.co/PramaLLC/BEN2/blob/main/onnx_run.py : ONNX usage on Windows.
- https://withoutbg.com/models/birefnet-general and /birefnet-portrait : third-party sample results (host not tested).
- https://arxiv.org/abs/2501.06230 and https://arxiv.org/abs/2401.03407 : BEN2 and BiRefNet papers for the architecture and numbers.
- Reddit r/StableDiffusion, r/comfyui, r/ecommerce threads comparing BiRefNet and BEN2 on garments (reddit blocked; needs the other lane's search).
