hf://models/ZhengPeng7/BiRefNet_dynamic/README.md (MCP_DATA 2026-11-07). Header trimmed.
Files: BiRefNet_config.py 298; README.md 11184; birefnet.py 92134; config.json 413; handler.py 5256; model.safetensors 444473596; requirements.txt 149. No .onnx.
license: mit
> An arbitrary shape adaptable BiRefNet for general segmentation.
> This model was trained on arbitrary shapes (256x256 ~ 2304x2304) and shows great robustness on inputs with any shape.
### Performance
> How it looks when compared with BiRefNet-general (fixed 1024x1024 resolution) -- greater than BiRefNet-general and BiRefNet_HR-general on the reserved validation sets (DIS-VD and TE-P3M-500-NP).
> The `dynamic_XXxXX` means this BiRefNet_dynamic model was being tested in various input resolutions for the evaluation.
(Performance given only as images; no numbers in the card text.)
Load line in the card (note: it names the base repo, a copy-paste from the main card): AutoModelForImageSegmentation.from_pretrained('ZhengPeng7/BiRefNet', trust_remote_code=True)
Inference snippet in the card:
    # image_size = (1024, 1024)
    # Since this model was trained on arbitrary shapes (256x256 ~ 2304x2304), the resizing is not necessary.
    transform_image = transforms.Compose([
        # transforms.Resize(image_size),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])
    (rest identical to the HR-matting snippet: .to('cuda').half(), birefnet(input_images)[-1].sigmoid().cpu(), putalpha)
Acknowledgement: Freepik (higher resolution training GPUs), fal (general model GPUs), not-lain (deployment).
