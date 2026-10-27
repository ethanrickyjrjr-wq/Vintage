[![Hugging Face's logo](https://huggingface.co/front/assets/huggingface_logo-noborder.svg) Hugging Face](https://huggingface.co/)
  * [ Models](https://huggingface.co/models)
  * [ Datasets](https://huggingface.co/datasets)
  * [ Spaces](https://huggingface.co/spaces)
  * [ Buckets](https://huggingface.co/storage)
  * [ Docs](https://huggingface.co/docs)
  * [ Enterprise](https://huggingface.co/enterprise)
  * [Pricing](https://huggingface.co/pricing)
  *     * Website
      * [ Tasks](https://huggingface.co/tasks)
      * [ HuggingChat](https://huggingface.co/chat)
      * [ Collections](https://huggingface.co/collections)
      * [ Languages](https://huggingface.co/languages)
      * [ Organizations](https://huggingface.co/organizations)
    * Community
      * [ Blog](https://huggingface.co/blog)
      * [ Posts](https://huggingface.co/posts)
      * [ Daily Papers](https://huggingface.co/papers)
      * [ Hardware](https://huggingface.co/hardware)
      * [ Learn](https://huggingface.co/learn)
      * [ Discord](https://huggingface.co/join/discord)
      * [ Forum](https://discuss.huggingface.co/)
      * [ GitHub](https://github.com/huggingface)
    * Solutions
      * [ Team & Enterprise](https://huggingface.co/enterprise)
      * [ Hugging Face PRO](https://huggingface.co/pro)
      * [ Enterprise Support](https://huggingface.co/support)
      * [ Inference Providers](https://huggingface.co/inference/models)
      * [ Inference Endpoints](https://huggingface.co/inference-endpoints)
      * [ Storage Buckets](https://huggingface.co/storage)
  * * * *
  * [Log In](https://huggingface.co/login)
  * [Sign Up](https://huggingface.co/join)


# 
[ ![](https://cdn-avatars.huggingface.co/v1/production/uploads/65659985cfbe8a857070d950/1HTn-HmGDwK53SSJ5dEYt.png) ](https://huggingface.co/briaai)
[briaai](https://huggingface.co/briaai)
/
[RMBG-2.0](https://huggingface.co/briaai/RMBG-2.0)
Like 1.58k
Follow
![](https://cdn-avatars.huggingface.co/v1/production/uploads/65659985cfbe8a857070d950/1HTn-HmGDwK53SSJ5dEYt.png) BRIA AI 16.1k
[ Image Segmentation ](https://huggingface.co/models?pipeline_tag=image-segmentation)[ Transformers ](https://huggingface.co/models?library=transformers)[ PyTorch ](https://huggingface.co/models?library=pytorch)[ ONNX ](https://huggingface.co/models?library=onnx)[ Safetensors ](https://huggingface.co/models?library=safetensors)[ Transformers.js ](https://huggingface.co/models?library=transformers.js)[ remove background ](https://huggingface.co/models?other=remove+background)[ background ](https://huggingface.co/models?other=background)[ background-removal ](https://huggingface.co/models?other=background-removal)[ Pytorch ](https://huggingface.co/models?other=Pytorch)[ vision ](https://huggingface.co/models?other=vision)[ legal liability ](https://huggingface.co/models?other=legal+liability)[ custom_code ](https://huggingface.co/models?other=custom_code)
License: bria-rmbg-2.0
[ Model card ](https://huggingface.co/briaai/RMBG-2.0)[ Files Files and versions xet ](https://huggingface.co/briaai/RMBG-2.0/tree/main)[ Community 51 ](https://huggingface.co/briaai/RMBG-2.0/discussions)
Deploy
Copy to bucket
Use this model
### Instructions to use briaai/RMBG-2.0 with libraries, inference providers, notebooks, and local apps. Follow these links to get started.
  * Libraries
  * [ Transformers](https://huggingface.co/briaai/RMBG-2.0?library=transformers)
How to use briaai/RMBG-2.0 with Transformers:

```
# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("image-segmentation", model="briaai/RMBG-2.0", trust_remote_code=True)
```

```
# pip install -U transformers accelerate
# Load model directly
from transformers import AutoModelForImageSegmentation
model = AutoModelForImageSegmentation.from_pretrained("briaai/RMBG-2.0", trust_remote_code=True, device_map="auto")
```

  * [ Transformers.js](https://huggingface.co/briaai/RMBG-2.0?library=transformers.js)
How to use briaai/RMBG-2.0 with Transformers.js:

```
// npm i @huggingface/transformers
import { pipeline } from '@huggingface/transformers';

// Allocate pipeline
const pipe = await pipeline('image-segmentation', 'briaai/RMBG-2.0');
```

  * Inference
  * Inference Providers
  * Notebooks
  * [ Google Colab](https://huggingface.co/briaai/RMBG-2.0/colab)
  * [ Kaggle](https://huggingface.co/briaai/RMBG-2.0/kaggle)


##  Fill in this form to immediatly access the model for non commercial use
Bria AI Model weights are open source for non commercial use only, per the provided [license](https://creativecommons.org/licenses/by-nc/4.0/deed.en).
[Log in](https://huggingface.co/login?next=%2Fbriaai%2FRMBG-2.0) or [Sign Up](https://huggingface.co/join?next=%2Fbriaai%2FRMBG-2.0) to review the conditions and access this model content.
  * [BRIA Background Removal v2.0 Model Card](https://huggingface.co/briaai/RMBG-2.0#bria-background-removal-v20-model-card "BRIA Background Removal v2.0 Model Card")
    * [Model Details](https://huggingface.co/briaai/RMBG-2.0#model-details "Model Details")
    * [Training data](https://huggingface.co/briaai/RMBG-2.0#training-data "Training data")
      * [Distribution of images:](https://huggingface.co/briaai/RMBG-2.0#distribution-of-images "Distribution of images:")
    * [Qualitative Evaluation](https://huggingface.co/briaai/RMBG-2.0#qualitative-evaluation "Qualitative Evaluation")
      * [Architecture](https://huggingface.co/briaai/RMBG-2.0#architecture "Architecture")
      * [Usage](https://huggingface.co/briaai/RMBG-2.0#usage "Usage")


#  [ ](https://huggingface.co/briaai/RMBG-2.0#bria-background-removal-v20-model-card) BRIA Background Removal v2.0 Model Card 
![BRIA Logo](https://bria-public.s3.us-east-1.amazonaws.com/Bria-logo.svg)
[ ![Hugging Face](https://huggingface.co/front/assets/huggingface_logo-noborder.svg) ✨ Discover **FIBO** on Hugging Face ](https://huggingface.co/briaai/FIBO)
💜 [**Bria AI**](https://go.bria.ai/46gzn20) | 🤗 [Hugging Face](https://huggingface.co/briaai/) | 📑 [Blog](https://blog.bria.ai/)   
🖥️ [Demo](https://huggingface.co/spaces/briaai/BRIA-RMBG-2.0) | [Github](https://github.com/Bria-AI/RMBG-2.0)
RMBG v2.0 is our new state-of-the-art background removal model significantly improves RMBG v1.4. The model is designed to effectively separate foreground from background in a range of categories and image types. This model has been trained on a carefully selected dataset, which includes: general stock images, e-commerce, gaming, and advertising content, making it suitable for commercial use cases powering enterprise content creation at scale. The accuracy, efficiency, and versatility currently rival leading source-available models. It is ideal where content safety, legally licensed datasets, and bias mitigation are paramount. 
**[→ Try the API Sandbox (no signup required)](https://catalog.bria.ai/image-editing/remove-background/sandbox)**
Developed by BRIA AI, RMBG v2.0 is available as a source-available model for non-commercial use.
###  [ ](https://huggingface.co/briaai/RMBG-2.0#get-access) Get Access 
Bria RMBG2.0 is availabe everywhere you build, either as source-code and weights, ComfyUI nodes or API endpoints.
#####  [ ](https://huggingface.co/briaai/RMBG-2.0)
###  [ ](https://huggingface.co/briaai/RMBG-2.0#model-description) Model Description 
**For production / commercial deployment** , use the Bria API — same RMBG-2.0 quality, fully licensed, zero infrastructure:  
| Use  | Self-Hosted (HF Weights)  | Bria API  |  
| --- | --- | --- |  
| Quality  | ✅ RMBG-2.0  | ✅ RMBG-2.0  |  
| Commercial License  | ❌ Requires agreement  | ✅ Included  |  
| GPU Infrastructure  | ❌ You manage  | ✅ Managed  |  
| Legally Licensed Data  | ✅ Yes  | ✅ Yes  |  
| Setup Time  | Hours  | Minutes  |  
**[→ Try the API Sandbox](https://catalog.bria.ai/image-editing/remove-background/sandbox)** — test it live, no signup required.
##  [ ](https://huggingface.co/briaai/RMBG-2.0#model-details) Model Details 
  * **Developed by:** [BRIA AI](https://bria.ai/)
  * **Model type:** Background Removal 
  * **License:** [Creative Commons Attribution–Non-Commercial (CC BY-NC 4.0)](https://creativecommons.org/licenses/by-nc/4.0/deed.en)
    * The model is released under a CC BY-NC 4.0 license for non-commercial use.
    * Commercial use is subject to a commercial agreement with BRIA. Available [here](https://platform.bria.ai/licensing/pricing?model=rmbg-2.0)


**API Endpoint** : [Sandbox](https://catalog.bria.ai/image-editing/remove-background/sandbox)
  * **ComfyUI** : [Use it in workflows](https://github.com/Bria-AI/ComfyUI-BRIA-API)
  * **GitHub** : [github.com/Bria-AI/RMBG-2.0](https://github.com/Bria-AI/RMBG-2.0)


**Purchase:** To purchase a Self-Hosted (HF Weights) commercial license [Click Here](https://share-eu1.hsforms.com/2sj9FVZTGSFmFRibDLhr_ZAf4e04).
For more information, please visit our [website](https://catalog.bria.ai/image-editing/remove-background/sandbox).
Join our [Discord community](https://discord.gg/Nxe9YW9zHS) for more information, tutorials, tools, and to connect with other users!
[CLICK HERE FOR A DEMO](https://huggingface.co/spaces/briaai/BRIA-RMBG-2.0)
[fal.ai](https://fal.ai/models/fal-ai/bria/background/remove), [Replicate](https://replicate.com/bria/remove-background)
[![examples](https://huggingface.co/briaai/RMBG-2.0/media/main/t4.png)](https://huggingface.co/briaai/RMBG-2.0/blob/main/t4.png)
  * **Model Description:** BRIA RMBG-2.0 is a dichotomous image segmentation model trained exclusively on a professional-grade dataset. The model output includes a single-channel 8-bit grayscale alpha matte, where each pixel value indicates the opacity level of the corresponding pixel in the original image. This non-binary output approach offers developers the flexibility to define custom thresholds for foreground-background separation, catering to varied use cases requirements and enhancing integration into complex pipelines.
  * **BRIA:** Resources for more information: [BRIA AI](https://bria.ai/)


##  [ ](https://huggingface.co/briaai/RMBG-2.0#training-data) Training data 
Bria-RMBG model was trained with over 15,000 high-quality, high-resolution, manually labeled (pixel-wise accuracy), fully licensed images. Our benchmark included balanced gender, balanced ethnicity, and people with different types of disabilities. For clarity, we provide our data distribution according to different categories, demonstrating our model’s versatility.
###  [ ](https://huggingface.co/briaai/RMBG-2.0#distribution-of-images) Distribution of images:   
| Category  | Distribution  |  
| --- | --- |  
| Objects only  | 45.11%  |  
| People with objects/animals  | 25.24%  |  
| People only  | 17.35%  |  
| people/objects/animals with text  | 8.52%  |  
| Text only  | 2.52%  |  
| Animals only  | 1.89%  |  
| Category  | Distribution  |  
| --- | --- |  
| Photorealistic  | 87.70%  |  
| Non-Photorealistic  | 12.30%  |  
| Category  | Distribution  |  
| --- | --- |  
| Non Solid Background  | 52.05%  |  
| Solid Background  | 47.95%  |  
| Category  | Distribution  |  
| --- | --- |  
| Single main foreground object  | 51.42%  |  
| Multiple objects in the foreground  | 48.58%  |  
##  [ ](https://huggingface.co/briaai/RMBG-2.0#qualitative-evaluation) Qualitative Evaluation 
Open source models comparison [![diagram](https://huggingface.co/briaai/RMBG-2.0/media/main/diagram1.png)](https://huggingface.co/briaai/RMBG-2.0/blob/main/diagram1.png) [![examples](https://huggingface.co/briaai/RMBG-2.0/media/main/collage5.png)](https://huggingface.co/briaai/RMBG-2.0/blob/main/collage5.png)
###  [ ](https://huggingface.co/briaai/RMBG-2.0#architecture) Architecture 
RMBG-2.0 is developed on the [BiRefNet](https://github.com/ZhengPeng7/BiRefNet) architecture enhanced with our proprietary dataset and training scheme. This training data significantly improves the model’s accuracy and effectiveness for background-removal task.  
If you use this model in your research, please cite:

```
@article{BiRefNet,
  title={Bilateral Reference for High-Resolution Dichotomous Image Segmentation},
  author={Zheng, Peng and Gao, Dehong and Fan, Deng-Ping and Liu, Li and Laaksonen, Jorma and Ouyang, Wanli and Sebe, Nicu},
  journal={CAAI Artificial Intelligence Research},
  year={2024}
}

```

####  [ ](https://huggingface.co/briaai/RMBG-2.0#requirements) Requirements 

```
torch
torchvision
pillow
kornia
transformers

```

###  [ ](https://huggingface.co/briaai/RMBG-2.0#usage) Usage 

```
from PIL import Image
import torch
from torchvision import transforms
from transformers import AutoModelForImageSegmentation

device = 'cuda' if torch.cuda.is_available() else 'cpu'
model = AutoModelForImageSegmentation.from_pretrained('briaai/RMBG-2.0', trust_remote_code=True).eval().to(device)

# Data settings
image_size = (1024, 1024)
transform_image = transforms.Compose([
    transforms.Resize(image_size),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

image = Image.open(input_image_path)
input_images = transform_image(image).unsqueeze(0).to(device)

# Prediction
with torch.no_grad():
    preds = model(input_images)[-1].sigmoid().cpu()
pred = preds[0].squeeze()
pred_pil = transforms.ToPILImage()(pred)
mask = pred_pil.resize(image.size)
image.putalpha(mask)

image.save("no_bg_image.png")

```


Downloads last month
    370,376
Safetensors[](https://huggingface.co/docs/safetensors)
Model size
0.2B params
Tensor type
I64 
·
F32 
·
Files info
Inference Providers [NEW](https://huggingface.co/docs/inference-providers)
fal
[ Image Segmentation ](https://huggingface.co/tasks/image-segmentation "Learn more about image-segmentation")
Drag image file here or click to browse from your device
Browse for image
View Code Snippets
Maximize
##  Model tree for briaai/RMBG-2.0 [](https://huggingface.co/docs/hub/model-cards#specifying-a-base-model)
Adapters
[1 model](https://huggingface.co/models?other=base_model:adapter:briaai/RMBG-2.0)
Finetunes
[2 models](https://huggingface.co/models?other=base_model:finetune:briaai/RMBG-2.0)
Quantizations
[5 models](https://huggingface.co/models?other=base_model:quantized:briaai/RMBG-2.0)
##  Spaces using briaai/RMBG-2.0 100
[ ![](https://cdn-avatars.huggingface.co/v1/production/uploads/65659985cfbe8a857070d950/1HTn-HmGDwK53SSJ5dEYt.png) briaai/BRIA-RMBG-2.0 ](https://huggingface.co/spaces/briaai/BRIA-RMBG-2.0)[🎭 linoyts/minimax-h3-character-swap ](https://huggingface.co/spaces/linoyts/minimax-h3-character-swap)[🧊 broyang/3dai ](https://huggingface.co/spaces/broyang/3dai)[🏆 LiXiang12/RMBG2.0-gradio ](https://huggingface.co/spaces/LiXiang12/RMBG2.0-gradio)[🏆 ifire/Pixal3D ](https://huggingface.co/spaces/ifire/Pixal3D)[🐨 iatiah/RMBG2.0 ](https://huggingface.co/spaces/iatiah/RMBG2.0)[🧊 luh0502/NeAR ](https://huggingface.co/spaces/luh0502/NeAR)[🎨 oindrila13saha/sigma-gen-demo ](https://huggingface.co/spaces/oindrila13saha/sigma-gen-demo) + 95 Spaces + 92 Spaces
##  Collection including briaai/RMBG-2.0
#### [RMBG Collection Background Removal models • 6 items • Updated Jun 14 • 3 ](https://huggingface.co/collections/briaai/rmbg)
System theme
Company
[TOS](https://huggingface.co/terms-of-service) [Privacy](https://huggingface.co/privacy) [About](https://huggingface.co/huggingface) [Careers](https://apply.workable.com/huggingface/) [](https://huggingface.co/)
Website
[Models](https://huggingface.co/models) [Datasets](https://huggingface.co/datasets) [Spaces](https://huggingface.co/spaces) [Pricing](https://huggingface.co/pricing) [Docs](https://huggingface.co/docs)
You have to accept the conditions to access the files info
Inference providers allow you to run inference using different serverless providers.

