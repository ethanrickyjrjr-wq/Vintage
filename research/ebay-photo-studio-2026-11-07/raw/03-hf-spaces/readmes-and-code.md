hf:// file reads (MCP_DATA, 2026-11-07)
not-lain/background-removal README: sdk gradio 5.35.0, license: mit, pinned: true. app.py (5028 bytes): loads "ZhengPeng7/BiRefNet", resizes to 1024x1024, @spaces.GPU (ZeroGPU), puts the mask in as alpha: image.putalpha(mask). Three tabs: Image Upload, URL Input, File Output ("Output PNG File", api_name png). Its own text: "In case you are using an MCP, it is recommended you use the one from https://huggingface.co/spaces/hf-applications/background-removal". Output is a transparent PNG. Mask is resampled to original size, so output keeps input resolution (processing at 1024).
hf-applications/background-removal app.py: same BiRefNet code, mcp_server=True, tool background_removal_fn, input is a public image URL string.
ZhengPeng7/BiRefNet_demo README: license: mit, sdk gradio 5.35.0, models BiRefNet, BiRefNet_HR, BiRefNet_HR-matting, BiRefNet-matting, BiRefNet-portrait, BiRefNet_lite.
ZhengPeng7/BiRefNet model card: "license: mit".
Upsampler/birefnet-background-removal README: license mit, "get a clean transparent PNG".
ECCV2022/dis-background-removal README: license apache-2.0, models doevent/dis.
Kwai-Kolors/Kolors-Virtual-Try-On README: license apache-2.0 (Space), sdk gradio 4.43.0, disable_embedding true. Model repo Kwai-Kolors/Kolors-Virtual-Try-On not found as a model.
WeShopAI/WeShopAI-Virtual-Try-On README: "license: other", hf_oauth: true (needs HF login).
Miragic-AI/Miragic-Virtual-Try-On README: no license field.
Xenova/remove-background-web README: sdk static, models briaai/RMBG-1.4, "In-browser background removal".
briaai/RMBG-1.4 README: "license: other", "RMBG v1.4 is available as a source-available model for non-commercial use". briaai/RMBG-2.0 is gated, access denied to this account.
amrhisham123/clawset-ghost-mannequin README: "Ghost mannequin effect powered by rembg + clothing segmentation + Stable Diffusion inpainting." No license field. app.py uses rembg isnet-general-use, mattmdjaga/segformer_b2_clothes, stable-diffusion-v1-5/stable-diffusion-inpainting at 512x512 inpaint size, background color (250,250,248) (off-white, not pure 255). API-style (base64 in), "Clawset Ghost Mannequin API".
meowmeows1/wardrobe-ghost-mannequin README: docker, license mit, "Ghost Mannequin API" only.
mattmdjaga/segformer_b2_clothes model card: "license: other".
