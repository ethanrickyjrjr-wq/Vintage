hf://models/yisol/IDM-VTON (MCP_DATA, read 2026-11-07 via hf_fs cat and hub_repo_details)
- license cc-by-nc-sa-4.0; downloads 1.6M, likes 747, updated 22 Apr 2024; base SDXL inpainting
- "The codes and checkpoints in this repository are under the [CC BY-NC-SA 4.0 license]"
hf://models/zhengchong/CatVTON
- license cc-by-nc-sa-4.0; downloads 65.4K; likes 87; updated 1 Jan 2025
- "Simplified Inference (< 8G VRAM for 1024X768 resolution)"; "When using `bf16` precision, generating results with a resolution of `1024x768` only requires about `8G` VRAM."
- "Problems under Windows OS, please refer to issue#8." ComfyUI workflow released.
- Mask-free version zhengchong/CatVTON-MaskFree (14 likes, no licence tag shown by hub_repo_details)
hf://models/levihsu/OOTDiffusion
- license cc-by-nc-sa-4.0; likes 341; updated 17 Apr 2024
- "We've only tested our code and models on Linux (Ubuntu 22.04)"; "checkpoints trained on VITON-HD (half-body) and Dress Code (full-body)"
hf://models/franciszzj/Leffa
- license mit; likes 343; updated 11 Sep 2025; paper CVPR 2025
- "prior methods often distort fine-grained textural details from the reference image ... Leffa ... significantly reducing fine-grained detail distortion"
- "Inference defaults to float16, generating an image in 6 seconds (on A100)." ComfyUI node by StartHua.
- "We use SCHP and DensePose to generate masks and densepose in our Demo."
hf://models/BoyuanJiang/FitDiT
- license cc-by-nc-sa-4.0; gated: "You agree that this model will only be used for non-commercial purposes."
- "This model can only be used **for non-commercial use**. For commercial use, please visit Tencent Cloud"
- bf16 no offload / fp16 / --offload / --aggressive_offload options (no VRAM number given); ComfyUI version exists; env onnxruntime-gpu==1.20.1
hf://spaces/Kwai-Kolors/Kolors-Virtual-Try-On
- space, 10217 likes, updated 1 Apr 2026, README licence apache-2.0. Files: app.py, README.md, requirements.txt, assets only (no weights).
- app.py posts base64 images to url = "http://" + os.environ['tryon_url'] with token/cookie env secrets: the Space is a thin client to a private Kuaishou server. Not runnable locally.
hf://models/Kwai-Kolors/Kolors (text-to-image base): "Kolors are fully open-sourced for academic research. For commercial use, please fill out this questionnaire ... sent it to kwai-kolors@kuaishou.com for registration."
hf://models/fal/flux-klein-9b-virtual-tryon-lora: apache-2.0 LoRA, 159 likes, created 24 Feb 2026. "3 input images (person, top, bottom) -> 1 output"; inputs table: "1st Person / Mannequin"; clothing types listed: T-shirts, hoodies, jackets, jeans, skirts, pants, shorts. Base black-forest-labs/FLUX.2-klein-9B is gated, license:other.
hf://models/xocialize/tryon-FLUX.2-klein-4B-lora: apache-2.0, base FLUX.2-klein-4B (hub: license:apache-2.0, 3.6M downloads). Needs clothing-agnostic masked person, top, bottom. "all-dark outfits are the weakest case". Trained on 273 tuples.
hf://models/ovi054/virtual-tryon-kontext-lora: apache-2.0 LoRA on FLUX.1-Kontext-dev (license:other, gated). Trigger "wear it"; input is model photo with garment overlaid.
hf://models/FoxBaze/Try_On_Qwen_Edit_Lora_Alpha: apache-2.0 LoRA on Qwen/Qwen-Image-Edit (apache-2.0, 20.4B params). "Struggles with 5 or more garments"; ComfyUI workflow; 832x1248 recommended.
hub search "try-on" by lastModified: nothing notable beyond the above; newest items are tiny or empty repos (duke182/tryon-garment-detector, Genlook/tryon-safety-classifier). Search "mannequin garment ghost": no results.
