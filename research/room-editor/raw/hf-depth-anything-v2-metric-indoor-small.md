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
[ ![](https://www.gravatar.com/avatar/f4f72407f9653fd54129eee82ed335fa?d=retro&size=100) ](https://huggingface.co/depth-anything)
[depth-anything](https://huggingface.co/depth-anything)
/
[Depth-Anything-V2-Metric-Indoor-Small-hf](https://huggingface.co/depth-anything/Depth-Anything-V2-Metric-Indoor-Small-hf)
Like 12
Follow
![](https://www.gravatar.com/avatar/f4f72407f9653fd54129eee82ed335fa?d=retro&size=100) Depth Aything 616
[ Depth Estimation ](https://huggingface.co/models?pipeline_tag=depth-estimation)[ Transformers ](https://huggingface.co/models?library=transformers)[ Safetensors ](https://huggingface.co/models?library=safetensors)[ depth_anything ](https://huggingface.co/models?other=depth_anything)[ depth ](https://huggingface.co/models?other=depth)[ absolute depth ](https://huggingface.co/models?other=absolute+depth)
arxiv: 2406.09414
arxiv: 2401.10891
[ Model card ](https://huggingface.co/depth-anything/Depth-Anything-V2-Metric-Indoor-Small-hf)[ Files Files and versions xet ](https://huggingface.co/depth-anything/Depth-Anything-V2-Metric-Indoor-Small-hf/tree/main)[ Community 4 ](https://huggingface.co/depth-anything/Depth-Anything-V2-Metric-Indoor-Small-hf/discussions)
Deploy
Copy to bucket
Use this model
### Instructions to use depth-anything/Depth-Anything-V2-Metric-Indoor-Small-hf with libraries, inference providers, notebooks, and local apps. Follow these links to get started.
  * Libraries
  * [ Transformers](https://huggingface.co/depth-anything/Depth-Anything-V2-Metric-Indoor-Small-hf?library=transformers)
How to use depth-anything/Depth-Anything-V2-Metric-Indoor-Small-hf with Transformers:

```
# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("depth-estimation", model="depth-anything/Depth-Anything-V2-Metric-Indoor-Small-hf")
```

```
# pip install -U transformers accelerate
# Load model directly
from transformers import AutoImageProcessor, AutoModelForDepthEstimation

processor = AutoImageProcessor.from_pretrained("depth-anything/Depth-Anything-V2-Metric-Indoor-Small-hf")
model = AutoModelForDepthEstimation.from_pretrained("depth-anything/Depth-Anything-V2-Metric-Indoor-Small-hf", device_map="auto")
```

  * Notebooks
  * [ Google Colab](https://huggingface.co/depth-anything/Depth-Anything-V2-Metric-Indoor-Small-hf/colab)
  * [ Kaggle](https://huggingface.co/depth-anything/Depth-Anything-V2-Metric-Indoor-Small-hf/kaggle)


  * [Depth Anything V2 (Fine-tuned for Metric Depth Estimation) - Transformers Version](https://huggingface.co/depth-anything/Depth-Anything-V2-Metric-Indoor-Small-hf#depth-anything-v2-fine-tuned-for-metric-depth-estimation---transformers-version "Depth Anything V2 \(Fine-tuned for Metric Depth Estimation\) - Transformers Version")
    * [Model description](https://huggingface.co/depth-anything/Depth-Anything-V2-Metric-Indoor-Small-hf#model-description "Model description")
    * [Intended uses & limitations](https://huggingface.co/depth-anything/Depth-Anything-V2-Metric-Indoor-Small-hf#intended-uses--limitations "Intended uses &amp; limitations")
      * [Requirements](https://huggingface.co/depth-anything/Depth-Anything-V2-Metric-Indoor-Small-hf#requirements "Requirements")
      * [How to use](https://huggingface.co/depth-anything/Depth-Anything-V2-Metric-Indoor-Small-hf#how-to-use "How to use")
    * [Citation](https://huggingface.co/depth-anything/Depth-Anything-V2-Metric-Indoor-Small-hf#citation "Citation")


#  [ ](https://huggingface.co/depth-anything/Depth-Anything-V2-Metric-Indoor-Small-hf#depth-anything-v2-fine-tuned-for-metric-depth-estimation---transformers-version) Depth Anything V2 (Fine-tuned for Metric Depth Estimation) - Transformers Version 
This model represents a fine-tuned version of [Depth Anything V2](https://huggingface.co/depth-anything/Depth-Anything-V2-Large-hf) for indoor metric depth estimation using the synthetic Hypersim datasets.
The model checkpoint is compatible with the transformers library.
Depth Anything V2 was introduced in [the paper of the same name](https://arxiv.org/abs/2406.09414) by Lihe Yang et al. It uses the same architecture as the original Depth Anything release but employs synthetic data and a larger capacity teacher model to achieve much finer and robust depth predictions. This fine-tuned version for metric depth estimation was first released in [this repository](https://github.com/DepthAnything/Depth-Anything-V2).
**Six metric depth models** of three scales for indoor and outdoor scenes, respectively, were released and are available:  
| Base Model  | Params  | Indoor (Hypersim)  | Outdoor (Virtual KITTI 2)  |  
| --- | --- | --- | --- |  
| Depth-Anything-V2-Small  | 24.8M  | [Model Card](https://huggingface.co/depth-anything/Depth-Anything-V2-Metric-Indoor-Small-hf)  | [Model Card](https://huggingface.co/depth-anything/Depth-Anything-V2-Metric-Outdoor-Small-hf)  |  
| Depth-Anything-V2-Base  | 97.5M  | [Model Card](https://huggingface.co/depth-anything/Depth-Anything-V2-Metric-Indoor-Base-hf)  | [Model Card](https://huggingface.co/depth-anything/Depth-Anything-V2-Metric-Outdoor-Base-hf)  |  
| Depth-Anything-V2-Large  | 335.3M  | [Model Card](https://huggingface.co/depth-anything/Depth-Anything-V2-Metric-Indoor-Large-hf)  | [Model Card](https://huggingface.co/depth-anything/Depth-Anything-V2-Metric-Outdoor-Large-hf)  |  
##  [ ](https://huggingface.co/depth-anything/Depth-Anything-V2-Metric-Indoor-Small-hf#model-description) Model description 
Depth Anything V2 leverages the [DPT](https://huggingface.co/docs/transformers/model_doc/dpt) architecture with a [DINOv2](https://huggingface.co/docs/transformers/model_doc/dinov2) backbone.
The model is trained on ~600K synthetic labeled images and ~62 million real unlabeled images, obtaining state-of-the-art results for both relative and absolute depth estimation.
![drawing](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/model_doc/depth_anything_overview.jpg)
Depth Anything overview. Taken from the [original paper](https://arxiv.org/abs/2401.10891).
##  [ ](https://huggingface.co/depth-anything/Depth-Anything-V2-Metric-Indoor-Small-hf#intended-uses--limitations) Intended uses & limitations 
You can use the raw model for tasks like zero-shot depth estimation. See the [model hub](https://huggingface.co/models?search=depth-anything) to look for other versions on a task that interests you.
###  [ ](https://huggingface.co/depth-anything/Depth-Anything-V2-Metric-Indoor-Small-hf#requirements) Requirements 
`transformers>=4.45.0`
Alternatively, use `transformers` latest version installed from the source:

```
pip install git+https://github.com/huggingface/transformers

```

###  [ ](https://huggingface.co/depth-anything/Depth-Anything-V2-Metric-Indoor-Small-hf#how-to-use) How to use 
Here is how to use this model to perform zero-shot depth estimation:

```
from transformers import pipeline
from PIL import Image
import requests

# load pipe
pipe = pipeline(task="depth-estimation", model="depth-anything/Depth-Anything-V2-Metric-Indoor-Small-hf")

# load image
url = 'http://images.cocodataset.org/val2017/000000039769.jpg'
image = Image.open(requests.get(url, stream=True).raw)

# inference
depth = pipe(image)["depth"]

```

Alternatively, you can use the model and processor classes:

```
from transformers import AutoImageProcessor, AutoModelForDepthEstimation
import torch
import numpy as np
from PIL import Image
import requests

url = "http://images.cocodataset.org/val2017/000000039769.jpg"
image = Image.open(requests.get(url, stream=True).raw)

image_processor = AutoImageProcessor.from_pretrained("depth-anything/Depth-Anything-V2-Metric-Indoor-Small-hf")
model = AutoModelForDepthEstimation.from_pretrained("depth-anything/Depth-Anything-V2-Metric-Indoor-Small-hf")

# prepare image for the model
inputs = image_processor(images=image, return_tensors="pt")

with torch.no_grad():
    outputs = model(**inputs)
    predicted_depth = outputs.predicted_depth

# interpolate to original size
prediction = torch.nn.functional.interpolate(
    predicted_depth.unsqueeze(1),
    size=image.size[::-1],
    mode="bicubic",
    align_corners=False,
)

```

For more code examples, please refer to the [documentation](https://huggingface.co/transformers/main/model_doc/depth_anything.html).
##  [ ](https://huggingface.co/depth-anything/Depth-Anything-V2-Metric-Indoor-Small-hf#citation) Citation 

```
@article{depth_anything_v2,
  title={Depth Anything V2},
  author={Yang, Lihe and Kang, Bingyi and Huang, Zilong and Zhao, Zhen and Xu, Xiaogang and Feng, Jiashi and Zhao, Hengshuang},
  journal={arXiv:2406.09414},
  year={2024}
}

@inproceedings{depth_anything_v1,
  title={Depth Anything: Unleashing the Power of Large-Scale Unlabeled Data}, 
  author={Yang, Lihe and Kang, Bingyi and Huang, Zilong and Xu, Xiaogang and Feng, Jiashi and Zhao, Hengshuang},
  booktitle={CVPR},
  year={2024}
}

```


Downloads last month
    32,384
Safetensors[](https://huggingface.co/docs/safetensors)
Model size
24.8M params
Tensor type
F32 
·
Files info
Inference Providers [NEW](https://huggingface.co/docs/inference-providers)
[ Depth Estimation ](https://huggingface.co/tasks/depth-estimation "Learn more about depth-estimation")
This model isn't deployed by any Inference Provider. [🙋 Ask for provider support](https://huggingface.co/spaces/huggingface/InferenceSupport/discussions/new?title=depth-anything/Depth-Anything-V2-Metric-Indoor-Small-hf&description=React%20to%20this%20comment%20with%20an%20emoji%20to%20vote%20for%20%5Bdepth-anything%2FDepth-Anything-V2-Metric-Indoor-Small-hf%5D\(%2Fdepth-anything%2FDepth-Anything-V2-Metric-Indoor-Small-hf\)%20to%20be%20supported%20by%20Inference%20Providers.%0A%0A\(optional\)%20Which%20providers%20are%20you%20interested%20in%3F%20\(Novita%2C%20Hyperbolic%2C%20Together%E2%80%A6\)%0A)
##  Model tree for depth-anything/Depth-Anything-V2-Metric-Indoor-Small-hf [](https://huggingface.co/docs/hub/model-cards#specifying-a-base-model)
Finetunes
[1 model](https://huggingface.co/models?other=base_model:finetune:depth-anything/Depth-Anything-V2-Metric-Indoor-Small-hf)
##  Spaces using depth-anything/Depth-Anything-V2-Metric-Indoor-Small-hf 9
[🧊 mattiagatti/image2mesh ](https://huggingface.co/spaces/mattiagatti/image2mesh)[🔊 Joemulberry/image-to-reverb ](https://huggingface.co/spaces/Joemulberry/image-to-reverb)[🐠 zeidImigine/Depth-Anything-V2-Metric ](https://huggingface.co/spaces/zeidImigine/Depth-Anything-V2-Metric)[🚀 eho69/cylinder ](https://huggingface.co/spaces/eho69/cylinder)[🚀 Doomshroom/ohio12 ](https://huggingface.co/spaces/Doomshroom/ohio12)[🌐 SiddhuG01/PanoGS ](https://huggingface.co/spaces/SiddhuG01/PanoGS)[🛰️ netha01/sanjaya-engine ](https://huggingface.co/spaces/netha01/sanjaya-engine)[🦯 michaelmccamy/obstacle-alert-api ](https://huggingface.co/spaces/michaelmccamy/obstacle-alert-api) + 4 Spaces + 1 Spaces
##  Papers for depth-anything/Depth-Anything-V2-Metric-Indoor-Small-hf
#### [Depth Anything V2 Paper • 2406.09414 • Published Jun 13, 2024 • 105 ](https://huggingface.co/papers/2406.09414)#### [Depth Anything: Unleashing the Power of Large-Scale Unlabeled Data Paper • 2401.10891 • Published Jan 19, 2024 • 64 ](https://huggingface.co/papers/2401.10891)
System theme
Company
[TOS](https://huggingface.co/terms-of-service) [Privacy](https://huggingface.co/privacy) [About](https://huggingface.co/huggingface) [Careers](https://apply.workable.com/huggingface/) [](https://huggingface.co/)
Website
[Models](https://huggingface.co/models) [Datasets](https://huggingface.co/datasets) [Spaces](https://huggingface.co/spaces) [Pricing](https://huggingface.co/pricing) [Docs](https://huggingface.co/docs)
Inference providers allow you to run inference using different serverless providers.

