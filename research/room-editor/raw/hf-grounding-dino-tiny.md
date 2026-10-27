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
[ ![](https://cdn-avatars.huggingface.co/v1/production/uploads/6438ff69e1acfc375c693ab1/CSi9zEks9X2rRdCXoEeU_.png) ](https://huggingface.co/IDEA-Research)
[IDEA-Research](https://huggingface.co/IDEA-Research)
/
[grounding-dino-tiny](https://huggingface.co/IDEA-Research/grounding-dino-tiny)
Like 126
Follow
![](https://cdn-avatars.huggingface.co/v1/production/uploads/6438ff69e1acfc375c693ab1/CSi9zEks9X2rRdCXoEeU_.png) IDEA-Research 244
[ Zero-Shot Object Detection ](https://huggingface.co/models?pipeline_tag=zero-shot-object-detection)[ Transformers ](https://huggingface.co/models?library=transformers)[ PyTorch ](https://huggingface.co/models?library=pytorch)[ Safetensors ](https://huggingface.co/models?library=safetensors)[ grounding-dino ](https://huggingface.co/models?other=grounding-dino)[ vision ](https://huggingface.co/models?other=vision)
arxiv: 2303.05499
License: apache-2.0
[ Model card ](https://huggingface.co/IDEA-Research/grounding-dino-tiny)[ Files Files and versions xet ](https://huggingface.co/IDEA-Research/grounding-dino-tiny/tree/main)[ Community 7 ](https://huggingface.co/IDEA-Research/grounding-dino-tiny/discussions)
Deploy
Copy to bucket
Use this model
### Instructions to use IDEA-Research/grounding-dino-tiny with libraries, inference providers, notebooks, and local apps. Follow these links to get started.
  * Libraries
  * [ Transformers](https://huggingface.co/IDEA-Research/grounding-dino-tiny?library=transformers)
How to use IDEA-Research/grounding-dino-tiny with Transformers:

```
# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("zero-shot-object-detection", model="IDEA-Research/grounding-dino-tiny")
```

```
# pip install -U transformers accelerate
# Load model directly
from transformers import AutoProcessor, AutoModelForZeroShotObjectDetection

processor = AutoProcessor.from_pretrained("IDEA-Research/grounding-dino-tiny")
model = AutoModelForZeroShotObjectDetection.from_pretrained("IDEA-Research/grounding-dino-tiny", device_map="auto")
```

  * Notebooks
  * [ Google Colab](https://huggingface.co/IDEA-Research/grounding-dino-tiny/colab)
  * [ Kaggle](https://huggingface.co/IDEA-Research/grounding-dino-tiny/kaggle)


  * [Grounding DINO model (tiny variant)](https://huggingface.co/IDEA-Research/grounding-dino-tiny#grounding-dino-model-tiny-variant "Grounding DINO model \(tiny variant\)")
    * [Intended uses & limitations](https://huggingface.co/IDEA-Research/grounding-dino-tiny#intended-uses--limitations "Intended uses &amp; limitations")
      * [How to use](https://huggingface.co/IDEA-Research/grounding-dino-tiny#how-to-use "How to use")
      * [BibTeX entry and citation info](https://huggingface.co/IDEA-Research/grounding-dino-tiny#bibtex-entry-and-citation-info "BibTeX entry and citation info")


#  [ ](https://huggingface.co/IDEA-Research/grounding-dino-tiny#grounding-dino-model-tiny-variant) Grounding DINO model (tiny variant) 
The Grounding DINO model was proposed in [Grounding DINO: Marrying DINO with Grounded Pre-Training for Open-Set Object Detection](https://arxiv.org/abs/2303.05499) by Shilong Liu, Zhaoyang Zeng, Tianhe Ren, Feng Li, Hao Zhang, Jie Yang, Chunyuan Li, Jianwei Yang, Hang Su, Jun Zhu, Lei Zhang. Grounding DINO extends a closed-set object detection model with a text encoder, enabling open-set object detection. The model achieves remarkable results, such as 52.5 AP on COCO zero-shot.
![drawing](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/model_doc/grouding_dino_architecture.png)
Grounding DINO overview. Taken from the [original paper](https://arxiv.org/abs/2303.05499). 
##  [ ](https://huggingface.co/IDEA-Research/grounding-dino-tiny#intended-uses--limitations) Intended uses & limitations 
You can use the raw model for zero-shot object detection (the task of detecting things in an image out-of-the-box without labeled data).
###  [ ](https://huggingface.co/IDEA-Research/grounding-dino-tiny#how-to-use) How to use 
Here's how to use the model for zero-shot object detection:

```
import requests

import torch
from PIL import Image
from transformers import AutoProcessor, AutoModelForZeroShotObjectDetection 

model_id = "IDEA-Research/grounding-dino-tiny"
device = "cuda" if torch.cuda.is_available() else "cpu"

processor = AutoProcessor.from_pretrained(model_id)
model = AutoModelForZeroShotObjectDetection.from_pretrained(model_id).to(device)

image_url = "http://images.cocodataset.org/val2017/000000039769.jpg"
image = Image.open(requests.get(image_url, stream=True).raw)
# Check for cats and remote controls
# VERY important: text queries need to be lowercased + end with a dot
text = "a cat. a remote control."

inputs = processor(images=image, text=text, return_tensors="pt").to(device)
with torch.no_grad():
    outputs = model(**inputs)

results = processor.post_process_grounded_object_detection(
    outputs,
    inputs.input_ids,
    box_threshold=0.4,
    text_threshold=0.3,
    target_sizes=[image.size[::-1]]
)

```

###  [ ](https://huggingface.co/IDEA-Research/grounding-dino-tiny#bibtex-entry-and-citation-info) BibTeX entry and citation info 

```
@misc{liu2023grounding,
      title={Grounding DINO: Marrying DINO with Grounded Pre-Training for Open-Set Object Detection}, 
      author={Shilong Liu and Zhaoyang Zeng and Tianhe Ren and Feng Li and Hao Zhang and Jie Yang and Chunyuan Li and Jianwei Yang and Hang Su and Jun Zhu and Lei Zhang},
      year={2023},
      eprint={2303.05499},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}

```


Downloads last month
    631,443
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
[ Zero-Shot Object Detection ](https://huggingface.co/tasks/zero-shot-object-detection "Learn more about zero-shot-object-detection")
This model isn't deployed by any Inference Provider. [🙋 2 Ask for provider support](https://huggingface.co/spaces/huggingface/InferenceSupport/discussions/9421)
##  Model tree for IDEA-Research/grounding-dino-tiny [](https://huggingface.co/docs/hub/model-cards#specifying-a-base-model)
Finetunes
[7 models](https://huggingface.co/models?other=base_model:finetune:IDEA-Research/grounding-dino-tiny)
Quantizations
[3 models](https://huggingface.co/models?other=base_model:quantized:IDEA-Research/grounding-dino-tiny)
##  Spaces using IDEA-Research/grounding-dino-tiny 100
[🤖 SahilCodevally/codevally-vision-language-action ](https://huggingface.co/spaces/SahilCodevally/codevally-vision-language-action)[⚡ ZENLLC/videodiffusion ](https://huggingface.co/spaces/ZENLLC/videodiffusion)[🦀 HorizonRobotics/3D-Fixer ](https://huggingface.co/spaces/HorizonRobotics/3D-Fixer)[📚 VAST-AI/MIDI-3D ](https://huggingface.co/spaces/VAST-AI/MIDI-3D)[🏃 zheyangqin/VADER ](https://huggingface.co/spaces/zheyangqin/VADER)[💻 merve/vision_papers ](https://huggingface.co/spaces/merve/vision_papers)[⚡ EduardoPacheco/Grounding-Dino-Inference ](https://huggingface.co/spaces/EduardoPacheco/Grounding-Dino-Inference)[🦀 Volkopat/SegmentAnythingxGroundingDINO ](https://huggingface.co/spaces/Volkopat/SegmentAnythingxGroundingDINO) + 95 Spaces + 92 Spaces
##  Paper for IDEA-Research/grounding-dino-tiny
#### [Grounding DINO: Marrying DINO with Grounded Pre-Training for Open-Set Object Detection Paper • 2303.05499 • Published Mar 9, 2023 • 9 ](https://huggingface.co/papers/2303.05499)
System theme
Company
[TOS](https://huggingface.co/terms-of-service) [Privacy](https://huggingface.co/privacy) [About](https://huggingface.co/huggingface) [Careers](https://apply.workable.com/huggingface/) [](https://huggingface.co/)
Website
[Models](https://huggingface.co/models) [Datasets](https://huggingface.co/datasets) [Spaces](https://huggingface.co/spaces) [Pricing](https://huggingface.co/pricing) [Docs](https://huggingface.co/docs)

