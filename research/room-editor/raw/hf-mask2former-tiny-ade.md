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
[ ![](https://cdn-avatars.huggingface.co/v1/production/uploads/1592839207516-noauth.png) ](https://huggingface.co/facebook)
[facebook](https://huggingface.co/facebook)
/
[mask2former-swin-tiny-ade-semantic](https://huggingface.co/facebook/mask2former-swin-tiny-ade-semantic)
Like 8
Follow
![](https://cdn-avatars.huggingface.co/v1/production/uploads/1592839207516-noauth.png) AI at Meta 15.7k
[ Image Segmentation ](https://huggingface.co/models?pipeline_tag=image-segmentation)[ Transformers ](https://huggingface.co/models?library=transformers)[ PyTorch ](https://huggingface.co/models?library=pytorch)
coco
[ mask2former ](https://huggingface.co/models?other=mask2former)[ vision ](https://huggingface.co/models?other=vision)
arxiv: 2112.01527
arxiv: 2107.06278
License: other
[ Model card ](https://huggingface.co/facebook/mask2former-swin-tiny-ade-semantic)[ Files Files and versions xet ](https://huggingface.co/facebook/mask2former-swin-tiny-ade-semantic/tree/main)[ Community 2 ](https://huggingface.co/facebook/mask2former-swin-tiny-ade-semantic/discussions)
Deploy
Copy to bucket
Use this model
### Instructions to use facebook/mask2former-swin-tiny-ade-semantic with libraries, inference providers, notebooks, and local apps. Follow these links to get started.
  * Libraries
  * [ Transformers](https://huggingface.co/facebook/mask2former-swin-tiny-ade-semantic?library=transformers)
How to use facebook/mask2former-swin-tiny-ade-semantic with Transformers:

```
# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("image-segmentation", model="facebook/mask2former-swin-tiny-ade-semantic")
```

```
# pip install -U transformers accelerate
# Load model directly
from transformers import AutoImageProcessor, Mask2FormerForUniversalSegmentation

processor = AutoImageProcessor.from_pretrained("facebook/mask2former-swin-tiny-ade-semantic")
model = Mask2FormerForUniversalSegmentation.from_pretrained("facebook/mask2former-swin-tiny-ade-semantic", device_map="auto")
```

  * Inference
  * Inference Providers
  * Notebooks
  * [ Google Colab](https://huggingface.co/facebook/mask2former-swin-tiny-ade-semantic/colab)
  * [ Kaggle](https://huggingface.co/facebook/mask2former-swin-tiny-ade-semantic/kaggle)


  * [Mask2Former](https://huggingface.co/facebook/mask2former-swin-tiny-ade-semantic#mask2former "Mask2Former")
    * [Model description](https://huggingface.co/facebook/mask2former-swin-tiny-ade-semantic#model-description "Model description")
    * [Intended uses & limitations](https://huggingface.co/facebook/mask2former-swin-tiny-ade-semantic#intended-uses--limitations "Intended uses &amp; limitations")
      * [How to use](https://huggingface.co/facebook/mask2former-swin-tiny-ade-semantic#how-to-use "How to use")


#  [ ](https://huggingface.co/facebook/mask2former-swin-tiny-ade-semantic#mask2former) Mask2Former 
Mask2Former model trained on ADE20k semantic segmentation (tiny-sized version, Swin backbone). It was introduced in the paper [Masked-attention Mask Transformer for Universal Image Segmentation ](https://arxiv.org/abs/2112.01527) and first released in [this repository](https://github.com/facebookresearch/Mask2Former/). 
Disclaimer: The team releasing Mask2Former did not write a model card for this model so this model card has been written by the Hugging Face team.
##  [ ](https://huggingface.co/facebook/mask2former-swin-tiny-ade-semantic#model-description) Model description 
Mask2Former addresses instance, semantic and panoptic segmentation with the same paradigm: by predicting a set of masks and corresponding labels. Hence, all 3 tasks are treated as if they were instance segmentation. Mask2Former outperforms the previous SOTA, [MaskFormer](https://arxiv.org/abs/2107.06278) both in terms of performance an efficiency by (i) replacing the pixel decoder with a more advanced multi-scale deformable attention Transformer, (ii) adopting a Transformer decoder with masked attention to boost performance without without introducing additional computation and (iii) improving training efficiency by calculating the loss on subsampled points instead of whole masks.
[![model image](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/mask2former_architecture.png)](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/mask2former_architecture.png)
##  [ ](https://huggingface.co/facebook/mask2former-swin-tiny-ade-semantic#intended-uses--limitations) Intended uses & limitations 
You can use this particular checkpoint for panoptic segmentation. See the [model hub](https://huggingface.co/models?search=mask2former) to look for other fine-tuned versions on a task that interests you.
###  [ ](https://huggingface.co/facebook/mask2former-swin-tiny-ade-semantic#how-to-use) How to use 
Here is how to use this model:

```
import requests
import torch
from PIL import Image
from transformers import AutoImageProcessor, Mask2FormerForUniversalSegmentation


# load Mask2Former fine-tuned on ADE20k semantic segmentation
processor = AutoImageProcessor.from_pretrained("facebook/mask2former-swin-tiny-ade-semantic")
model = Mask2FormerForUniversalSegmentation.from_pretrained("facebook/mask2former-swin-tiny-ade-semantic")

url = "http://images.cocodataset.org/val2017/000000039769.jpg"
image = Image.open(requests.get(url, stream=True).raw)
inputs = processor(images=image, return_tensors="pt")

with torch.no_grad():
    outputs = model(**inputs)

# model predicts class_queries_logits of shape `(batch_size, num_queries)`
# and masks_queries_logits of shape `(batch_size, num_queries, height, width)`
class_queries_logits = outputs.class_queries_logits
masks_queries_logits = outputs.masks_queries_logits

# you can pass them to processor for postprocessing
predicted_semantic_map = processor.post_process_semantic_segmentation(outputs, target_sizes=[image.size[::-1]])[0]
# we refer to the demo notebooks for visualization (see "Resources" section in the Mask2Former docs)

```

For more code examples, we refer to the [documentation](https://huggingface.co/docs/transformers/master/en/model_doc/mask2former). 

Downloads last month
    8,293
Inference Providers [NEW](https://huggingface.co/docs/inference-providers)
HF Inference API
[ Image Segmentation ](https://huggingface.co/tasks/image-segmentation "Learn more about image-segmentation")
Examples
Drag image file here or click to browse from your device
Browse for image
View Code Snippets
Maximize
##  Model tree for facebook/mask2former-swin-tiny-ade-semantic [](https://huggingface.co/docs/hub/model-cards#specifying-a-base-model)
Adapters
[1 model](https://huggingface.co/models?other=base_model:adapter:facebook/mask2former-swin-tiny-ade-semantic)
Finetunes
[2 models](https://huggingface.co/models?other=base_model:finetune:facebook/mask2former-swin-tiny-ade-semantic)
##  Spaces using facebook/mask2former-swin-tiny-ade-semantic 13
[🚀 shivalikasingh/mask2former-demo ](https://huggingface.co/spaces/shivalikasingh/mask2former-demo)[⚡ roundb/Conhecimento ](https://huggingface.co/spaces/roundb/Conhecimento)[🛣️ DaryaEL/cityvision-poc ](https://huggingface.co/spaces/DaryaEL/cityvision-poc)[🚀 sanjayw/mask2former-demo ](https://huggingface.co/spaces/sanjayw/mask2former-demo)[🖼️ SeyedAli/Image-Segmentation ](https://huggingface.co/spaces/SeyedAli/Image-Segmentation)[🚀 hugging-fellows/mask2former-demo ](https://huggingface.co/spaces/hugging-fellows/mask2former-demo)[🏢 justdeveloper2/facebook-mask2former-swin-tiny-ade-semantic ](https://huggingface.co/spaces/justdeveloper2/facebook-mask2former-swin-tiny-ade-semantic)[🚀 wendys-llc/mask2former-demo ](https://huggingface.co/spaces/wendys-llc/mask2former-demo) + 8 Spaces + 5 Spaces
##  Papers for facebook/mask2former-swin-tiny-ade-semantic
#### [Masked-attention Mask Transformer for Universal Image Segmentation Paper • 2112.01527 • Published Dec 2, 2021 • 1 ](https://huggingface.co/papers/2112.01527)#### [Per-Pixel Classification is Not All You Need for Semantic Segmentation Paper • 2107.06278 • Published Jul 13, 2021 ](https://huggingface.co/papers/2107.06278)
System theme
Company
[TOS](https://huggingface.co/terms-of-service) [Privacy](https://huggingface.co/privacy) [About](https://huggingface.co/huggingface) [Careers](https://apply.workable.com/huggingface/) [](https://huggingface.co/)
Website
[Models](https://huggingface.co/models) [Datasets](https://huggingface.co/datasets) [Spaces](https://huggingface.co/spaces) [Pricing](https://huggingface.co/pricing) [Docs](https://huggingface.co/docs)

