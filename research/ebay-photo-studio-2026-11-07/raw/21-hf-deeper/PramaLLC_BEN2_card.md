hf://models/PramaLLC/BEN2/README.md (MCP_DATA 2026-11-07). Header trimmed; install/inference text verbatim.
Files: BEN2.py 53513; BEN2_Base.onnx 222932053 (lfs); BEN2_Base.pth 1134584206 (lfs); README.md 5128; config.json 124; inference.py 353; model.safetensors 380577976 (lfs); onnx_run.py 1675; requirements.txt 102; dir BEN2_demo_pictures.
license: mit
## BEN2 access
BEN2 was trained on the DIS5k and our 22K proprietary segmentation dataset. Our enhanced model delivers superior performance in hair matting, 4K processing, object segmentation, and edge refinement. Our Base model is open source. To try the full model through our free web demo or integrate BEN2 into your project with our API:
- backgrounderase.com
## Contact us
- For access to our commercial model email us at sales@backgrounderase.com
## Installation
pip install -e "git+https://github.com/PramaLLC/BEN2.git#egg=ben2"
## Quick start code
from ben2 import BEN_Base
from PIL import Image
import torch
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
file = "./image.png" # input image
model = BEN_Base.from_pretrained("PramaLLC/BEN2")
model.to(device).eval()
image = Image.open(file)
foreground = model.inference(image, refine_foreground=False,) #Refine foreground is an extract postprocessing step that increases inference time but can improve matting edges. The default value is False.
foreground.save("./foreground.png")
Batch: foregrounds = model.inference([image1, image2]) # "We recommend that the batch size not exceed 3 for consumer GPUs"
requirements.txt: numpy>=1.21.0 torch>=1.9.0 einops>=0.6.0 Pillow>=9.0.0 timm>=1.0.10 torchvision>=0.10.0 onnxruntime
