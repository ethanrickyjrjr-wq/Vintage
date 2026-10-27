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
[RMBG-1.4](https://huggingface.co/briaai/RMBG-1.4)
Like 2.06k
Follow
![](https://cdn-avatars.huggingface.co/v1/production/uploads/65659985cfbe8a857070d950/1HTn-HmGDwK53SSJ5dEYt.png) BRIA AI 16.1k
[ Image Segmentation ](https://huggingface.co/models?pipeline_tag=image-segmentation)[ Transformers ](https://huggingface.co/models?library=transformers)[ PyTorch ](https://huggingface.co/models?library=pytorch)[ ONNX ](https://huggingface.co/models?library=onnx)[ Safetensors ](https://huggingface.co/models?library=safetensors)[ Transformers.js ](https://huggingface.co/models?library=transformers.js)[ SegformerForSemanticSegmentation ](https://huggingface.co/models?other=SegformerForSemanticSegmentation)[ remove background ](https://huggingface.co/models?other=remove+background)[ background ](https://huggingface.co/models?other=background)[ background-removal ](https://huggingface.co/models?other=background-removal)[ Pytorch ](https://huggingface.co/models?other=Pytorch)[ vision ](https://huggingface.co/models?other=vision)[ legal liability ](https://huggingface.co/models?other=legal+liability)[ custom_code ](https://huggingface.co/models?other=custom_code)
License: bria-rmbg-1.4
[ Model card ](https://huggingface.co/briaai/RMBG-1.4)[ Files Files and versions xet ](https://huggingface.co/briaai/RMBG-1.4/tree/main)[ Community 54 ](https://huggingface.co/briaai/RMBG-1.4/discussions)
Deploy
Copy to bucket
Use this model
### Instructions to use briaai/RMBG-1.4 with libraries, inference providers, notebooks, and local apps. Follow these links to get started.
  * Libraries
  * [ Transformers](https://huggingface.co/briaai/RMBG-1.4?library=transformers)
How to use briaai/RMBG-1.4 with Transformers:

```
# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("image-segmentation", model="briaai/RMBG-1.4", trust_remote_code=True)
```

```
# pip install -U transformers accelerate
# Load model directly
from transformers import AutoModelForImageSegmentation
model = AutoModelForImageSegmentation.from_pretrained("briaai/RMBG-1.4", trust_remote_code=True, device_map="auto")
```

  * [ Transformers.js](https://huggingface.co/briaai/RMBG-1.4?library=transformers.js)
How to use briaai/RMBG-1.4 with Transformers.js:

```
// npm i @huggingface/transformers
import { pipeline } from '@huggingface/transformers';

// Allocate pipeline
const pipe = await pipeline('image-segmentation', 'briaai/RMBG-1.4');
```

  * Notebooks
  * [ Google Colab](https://huggingface.co/briaai/RMBG-1.4/colab)
  * [ Kaggle](https://huggingface.co/briaai/RMBG-1.4/kaggle)


  * [BRIA Background Removal v1.4 Model Card](https://huggingface.co/briaai/RMBG-1.4#bria-background-removal-v14-model-card "BRIA Background Removal v1.4 Model Card")
    * [Training data](https://huggingface.co/briaai/RMBG-1.4#training-data "Training data")
      * [Distribution of images:](https://huggingface.co/briaai/RMBG-1.4#distribution-of-images "Distribution of images:")
    * [Qualitative Evaluation](https://huggingface.co/briaai/RMBG-1.4#qualitative-evaluation "Qualitative Evaluation")
    * [Architecture](https://huggingface.co/briaai/RMBG-1.4#architecture "Architecture")
    * [Installation](https://huggingface.co/briaai/RMBG-1.4#installation "Installation")
    * [Usage](https://huggingface.co/briaai/RMBG-1.4#usage "Usage")


#  [ ](https://huggingface.co/briaai/RMBG-1.4#bria-background-removal-v14-model-card) BRIA Background Removal v1.4 Model Card 
RMBG v1.4 is our state-of-the-art background removal model, designed to effectively separate foreground from background in a range of categories and image types. This model has been trained on a carefully selected dataset, which includes: general stock images, e-commerce, gaming, and advertising content, making it suitable for commercial use cases powering enterprise content creation at scale. The accuracy, efficiency, and versatility currently rival leading source-available models. It is ideal where content safety, legally licensed datasets, and bias mitigation are paramount. 
Developed by BRIA AI, RMBG v1.4 is available as a source-available model for non-commercial use. 
To purchase a commercial license, simply click [Here](https://go.bria.ai/3D5EGp0).
[CLICK HERE FOR A DEMO](https://huggingface.co/spaces/briaai/BRIA-RMBG-1.4)
**NOTE** New RMBG version available! Check out [RMBG-2.0](https://huggingface.co/briaai/RMBG-2.0)
Join our [Discord community](https://discord.gg/Nxe9YW9zHS) for more information, tutorials, tools, and to connect with other users!
[![examples](https://huggingface.co/briaai/RMBG-1.4/resolve/main/t4.png)](https://huggingface.co/briaai/RMBG-1.4/blob/main/t4.png)
###  [ ](https://huggingface.co/briaai/RMBG-1.4#model-description) Model Description 
  * **Developed by:** [BRIA AI](https://bria.ai/)
  * **Model type:** Background Removal 
  * **License:** [bria-rmbg-1.4](https://bria.ai/bria-huggingface-model-license-agreement/)
    * The model is released under a Creative Commons license for non-commercial use.
    * Commercial use is subject to a commercial agreement with BRIA. To purchase a commercial license simply click [Here](https://go.bria.ai/3B4Asxv).
  * **Model Description:** BRIA RMBG 1.4 is a saliency segmentation model trained exclusively on a professional-grade dataset.
  * **BRIA:** Resources for more information: [BRIA AI](https://bria.ai/)


##  [ ](https://huggingface.co/briaai/RMBG-1.4#training-data) Training data 
Bria-RMBG model was trained with over 12,000 high-quality, high-resolution, manually labeled (pixel-wise accuracy), fully licensed images. Our benchmark included balanced gender, balanced ethnicity, and people with different types of disabilities. For clarity, we provide our data distribution according to different categories, demonstrating our model’s versatility.
###  [ ](https://huggingface.co/briaai/RMBG-1.4#distribution-of-images) Distribution of images:   
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
##  [ ](https://huggingface.co/briaai/RMBG-1.4#qualitative-evaluation) Qualitative Evaluation 
[![examples](https://huggingface.co/briaai/RMBG-1.4/resolve/main/results.png)](https://huggingface.co/briaai/RMBG-1.4/blob/main/results.png)
##  [ ](https://huggingface.co/briaai/RMBG-1.4#architecture) Architecture 
RMBG v1.4 is developed on the [IS-Net](https://github.com/xuebinqin/DIS) enhanced with our unique training scheme and proprietary dataset. These modifications significantly improve the model’s accuracy and effectiveness in diverse image-processing scenarios.
##  [ ](https://huggingface.co/briaai/RMBG-1.4#installation) Installation 

```
pip install -qr https://huggingface.co/briaai/RMBG-1.4/resolve/main/requirements.txt

```

##  [ ](https://huggingface.co/briaai/RMBG-1.4#usage) Usage 
Either load the pipeline

```
from transformers import pipeline
image_path = "https://farm5.staticflickr.com/4007/4322154488_997e69e4cf_z.jpg"
pipe = pipeline("image-segmentation", model="briaai/RMBG-1.4", trust_remote_code=True)
pillow_mask = pipe(image_path, return_mask = True) # outputs a pillow mask
pillow_image = pipe(image_path) # applies mask on input and returns a pillow image

```

Or load the model 

```
from PIL import Image
from skimage import io
import torch
import torch.nn.functional as F
from transformers import AutoModelForImageSegmentation
from torchvision.transforms.functional import normalize
model = AutoModelForImageSegmentation.from_pretrained("briaai/RMBG-1.4",trust_remote_code=True)
def preprocess_image(im: np.ndarray, model_input_size: list) -> torch.Tensor:
    if len(im.shape) < 3:
        im = im[:, :, np.newaxis]
    # orig_im_size=im.shape[0:2]
    im_tensor = torch.tensor(im, dtype=torch.float32).permute(2,0,1)
    im_tensor = F.interpolate(torch.unsqueeze(im_tensor,0), size=model_input_size, mode='bilinear')
    image = torch.divide(im_tensor,255.0)
    image = normalize(image,[0.5,0.5,0.5],[1.0,1.0,1.0])
    return image

def postprocess_image(result: torch.Tensor, im_size: list)-> np.ndarray:
    result = torch.squeeze(F.interpolate(result, size=im_size, mode='bilinear') ,0)
    ma = torch.max(result)
    mi = torch.min(result)
    result = (result-mi)/(ma-mi)
    im_array = (result*255).permute(1,2,0).cpu().data.numpy().astype(np.uint8)
    im_array = np.squeeze(im_array)
    return im_array

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
model.to(device)

# prepare input
image_path = "https://farm5.staticflickr.com/4007/4322154488_997e69e4cf_z.jpg"
orig_im = io.imread(image_path)
orig_im_size = orig_im.shape[0:2]
model_input_size = [1024, 1024]
image = preprocess_image(orig_im, model_input_size).to(device)

# inference 
result=model(image)

# post process
result_image = postprocess_image(result[0][0], orig_im_size)

# save result
pil_mask_im = Image.fromarray(result_image)
orig_image = Image.open(image_path)
no_bg_image = orig_image.copy()
no_bg_image.putalpha(pil_mask_im)

```


Downloads last month
    249,052
Safetensors[](https://huggingface.co/docs/safetensors)
Model size
44.1M params
Tensor type
F32 
·
Files info
Inference Providers [NEW](https://huggingface.co/docs/inference-providers)
[ Image Segmentation ](https://huggingface.co/tasks/image-segmentation "Learn more about image-segmentation")
This model isn't deployed by any Inference Provider. [🙋 11 Ask for provider support](https://huggingface.co/spaces/huggingface/InferenceSupport/discussions/2348)
##  Model tree for briaai/RMBG-1.4 [](https://huggingface.co/docs/hub/model-cards#specifying-a-base-model)
Finetunes
[2 models](https://huggingface.co/models?other=base_model:finetune:briaai/RMBG-1.4)
Quantizations
[3 models](https://huggingface.co/models?other=base_model:quantized:briaai/RMBG-1.4)
##  Spaces using briaai/RMBG-1.4 100
[ ![](https://cdn-avatars.huggingface.co/v1/production/uploads/65659985cfbe8a857070d950/1HTn-HmGDwK53SSJ5dEYt.png) briaai/BRIA-RMBG-1.4 ](https://huggingface.co/spaces/briaai/BRIA-RMBG-1.4)[🖼️ Xenova/remove-background-web ](https://huggingface.co/spaces/Xenova/remove-background-web)[📈 lllyasviel/IC-Light ](https://huggingface.co/spaces/lllyasviel/IC-Light)[🎨 HorizonRobotics/EmbodiedGen-Texture-Gen ](https://huggingface.co/spaces/HorizonRobotics/EmbodiedGen-Texture-Gen)[🦑 Ravenok/depth-anything-v2 ](https://huggingface.co/spaces/Ravenok/depth-anything-v2)[🔮 VAST-AI/TripoSG ](https://huggingface.co/spaces/VAST-AI/TripoSG)[🖼️ Xenova/remove-background-webgpu ](https://huggingface.co/spaces/Xenova/remove-background-webgpu)[🎥💨🖋️ linoyts/wan2-1-VACE-fast ](https://huggingface.co/spaces/linoyts/wan2-1-VACE-fast) + 95 Spaces + 92 Spaces
##  Collection including briaai/RMBG-1.4
#### [RMBG Collection Background Removal models • 6 items • Updated Jun 14 • 3 ](https://huggingface.co/collections/briaai/rmbg)
System theme
Company
[TOS](https://huggingface.co/terms-of-service) [Privacy](https://huggingface.co/privacy) [About](https://huggingface.co/huggingface) [Careers](https://apply.workable.com/huggingface/) [](https://huggingface.co/)
Website
[Models](https://huggingface.co/models) [Datasets](https://huggingface.co/datasets) [Spaces](https://huggingface.co/spaces) [Pricing](https://huggingface.co/pricing) [Docs](https://huggingface.co/docs)
Inference providers allow you to run inference using different serverless providers.

