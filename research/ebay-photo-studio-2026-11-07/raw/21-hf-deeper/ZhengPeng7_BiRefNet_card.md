hf://models/ZhengPeng7/BiRefNet/README.md (MCP_DATA 2026-11-07). Header trimmed.
Files: .gitattributes 1519; .gitignore 1908; BiRefNet_config.py 298; README.md 9965; birefnet.py 91896; config.json 405; handler.py 4762; model.safetensors 444473596; requirements.txt 149. No .onnx.
license: mit
Load: from transformers import AutoModelForImageSegmentation; birefnet = AutoModelForImageSegmentation.from_pretrained('ZhengPeng7/BiRefNet', trust_remote_code=True)
Inference: same as HR-matting card but image_size = (1024, 1024), transforms.Resize(image_size), birefnet.half(), birefnet(input_images)[-1].sigmoid().cpu().
The card text contains no refine_foreground; it appears only in handler.py (see ZhengPeng7_BiRefNet_HR-matting_handler.py.md).
