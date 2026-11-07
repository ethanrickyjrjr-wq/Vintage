hf://models/ZhengPeng7/BiRefNet_HR-matting/README.md (read via Hugging Face MCP hf_fs cat, 2026-11-07, MCP_DATA). Authors/badge header and BibTeX trimmed in this copy; everything load-bearing is verbatim.
Files (hf_fs ls): .gitattributes 1519; BiRefNet_config.py 298; README.md 11522; birefnet.py 92134; config.json 416; handler.py 4765; model.safetensors 444473596 (lfs); requirements.txt 149. No .onnx.
---
library_name: birefnet
tags: background-removal, mask-generation, Dichotomous Image Segmentation, Camouflaged Object Detection, Salient Object Detection, pytorch_model_hub_mixin, model_hub_mixin
repo_url: https://github.com/ZhengPeng7/BiRefNet
pipeline_tag: image-segmentation
license: mit
---
> This BiRefNet was trained with images in `2048x2048` for higher resolution image matting with transparency.
### Performance:
> All tested in FP16 mode.
(table) TE-AM-2k | BiRefNet_HR-matting-epoch_135 | 2048x2048 | maxFm .974 wFmeasure .997 MAE .989(sic column shift) ...
TE-P3M-500-NP | BiRefNet_HR-matting-epoch_135 | 2048x2048 | .980 .996 .989 .002 ...
TE-AM-2k | BiRefNet-matting-epoch_100 | 1024x1024 | .973 .996 .990 .003 ...
TE-P3M-500-NP | BiRefNet-matting-epoch_100 | 1024x1024 | .979 .996 .990 .003 ...
TE-AM-2k | BiRefNet-matting-epoch_100 | 2048x2048 | .971 .996 .990 .003 ...
TE-P3M-500-NP | BiRefNet-matting-epoch_100 | 2048x2048 | .978 .995 .990 .003 ...
(Column headers in the card are misaligned with the cell values; the card gives no VRAM or speed number.)
## How to use
### 0. Install Packages:
pip install -qr https://raw.githubusercontent.com/ZhengPeng7/BiRefNet/main/requirements.txt
### 1. Load BiRefNet: (Use codes + weights from HuggingFace)
from transformers import AutoModelForImageSegmentation
birefnet = AutoModelForImageSegmentation.from_pretrained('ZhengPeng7/BiRefNet_HR-matting', trust_remote_code=True)
#### Use the loaded BiRefNet for inference
from PIL import Image
import matplotlib.pyplot as plt
import torch
from torchvision import transforms
from models.birefnet import BiRefNet
birefnet = ... # -- BiRefNet should be loaded with codes above, either way.
torch.set_float32_matmul_precision(['high', 'highest'][0])
birefnet.to('cuda')
birefnet.eval()
birefnet.half()
def extract_object(birefnet, imagepath):
    # Data settings
    image_size = (2048, 2048)
    transform_image = transforms.Compose([
        transforms.Resize(image_size),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])
    image = Image.open(imagepath)
    input_images = transform_image(image).unsqueeze(0).to('cuda').half()
    # Prediction
    with torch.no_grad():
        preds = birefnet(input_images)[-1].sigmoid().cpu()
    pred = preds[0].squeeze()
    pred_pil = transforms.ToPILImage()(pred)
    mask = pred_pil.resize(image.size)
    image.putalpha(mask)
    return image, mask
Acknowledgement: "Many thanks to @freepik for their generous support on GPU resources for training this model!"
