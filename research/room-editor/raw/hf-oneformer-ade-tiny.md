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
[ ![](https://cdn-avatars.huggingface.co/v1/production/uploads/1650941798672-61e1188afc27c0f5e3641eb3.jpeg) ](https://huggingface.co/shi-labs)
[shi-labs](https://huggingface.co/shi-labs)
/
[oneformer_ade20k_swin_tiny](https://huggingface.co/shi-labs/oneformer_ade20k_swin_tiny)
Like 17
Follow
![](https://cdn-avatars.huggingface.co/v1/production/uploads/1650941798672-61e1188afc27c0f5e3641eb3.jpeg) SHI Labs 100
[ Image Segmentation ](https://huggingface.co/models?pipeline_tag=image-segmentation)[ Transformers ](https://huggingface.co/models?library=transformers)[ PyTorch ](https://huggingface.co/models?library=pytorch)
scene_parse_150
[ oneformer ](https://huggingface.co/models?other=oneformer)[ vision ](https://huggingface.co/models?other=vision)
arxiv: 2211.06220
License: mit
[ Model card ](https://huggingface.co/shi-labs/oneformer_ade20k_swin_tiny)[ Files Files and versions xet ](https://huggingface.co/shi-labs/oneformer_ade20k_swin_tiny/tree/main)[ Community 7 ](https://huggingface.co/shi-labs/oneformer_ade20k_swin_tiny/discussions)
Deploy
Copy to bucket
Use this model
### Instructions to use shi-labs/oneformer_ade20k_swin_tiny with libraries, inference providers, notebooks, and local apps. Follow these links to get started.
  * Libraries
  * [ Transformers](https://huggingface.co/shi-labs/oneformer_ade20k_swin_tiny?library=transformers)
How to use shi-labs/oneformer_ade20k_swin_tiny with Transformers:

```
# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("image-segmentation", model="shi-labs/oneformer_ade20k_swin_tiny")
```

```
# pip install -U transformers accelerate
# Load model directly
from transformers import AutoProcessor, OneFormerForUniversalSegmentation

processor = AutoProcessor.from_pretrained("shi-labs/oneformer_ade20k_swin_tiny")
model = OneFormerForUniversalSegmentation.from_pretrained("shi-labs/oneformer_ade20k_swin_tiny", device_map="auto")
```

  * Inference
  * Inference Providers
  * Notebooks
  * [ Google Colab](https://huggingface.co/shi-labs/oneformer_ade20k_swin_tiny/colab)
  * [ Kaggle](https://huggingface.co/shi-labs/oneformer_ade20k_swin_tiny/kaggle)


  * [OneFormer](https://huggingface.co/shi-labs/oneformer_ade20k_swin_tiny#oneformer "OneFormer")
    * [Model description](https://huggingface.co/shi-labs/oneformer_ade20k_swin_tiny#model-description "Model description")
    * [Intended uses & limitations](https://huggingface.co/shi-labs/oneformer_ade20k_swin_tiny#intended-uses--limitations "Intended uses &amp; limitations")
      * [How to use](https://huggingface.co/shi-labs/oneformer_ade20k_swin_tiny#how-to-use "How to use")
      * [Citation](https://huggingface.co/shi-labs/oneformer_ade20k_swin_tiny#citation "Citation")


#  [ ](https://huggingface.co/shi-labs/oneformer_ade20k_swin_tiny#oneformer) OneFormer 
OneFormer model trained on the ADE20k dataset (tiny-sized version, Swin backbone). It was introduced in the paper [OneFormer: One Transformer to Rule Universal Image Segmentation](https://arxiv.org/abs/2211.06220) by Jain et al. and first released in [this repository](https://github.com/SHI-Labs/OneFormer).
[![model image](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/model_doc/oneformer_teaser.png)](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/model_doc/oneformer_teaser.png)
##  [ ](https://huggingface.co/shi-labs/oneformer_ade20k_swin_tiny#model-description) Model description 
OneFormer is the first multi-task universal image segmentation framework. It needs to be trained only once with a single universal architecture, a single model, and on a single dataset, to outperform existing specialized models across semantic, instance, and panoptic segmentation tasks. OneFormer uses a task token to condition the model on the task in focus, making the architecture task-guided for training, and task-dynamic for inference, all with a single model.
[![model image](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/model_doc/oneformer_architecture.png)](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/model_doc/oneformer_architecture.png)
##  [ ](https://huggingface.co/shi-labs/oneformer_ade20k_swin_tiny#intended-uses--limitations) Intended uses & limitations 
You can use this particular checkpoint for semantic, instance and panoptic segmentation. See the [model hub](https://huggingface.co/models?search=oneformer) to look for other fine-tuned versions on a different dataset.
###  [ ](https://huggingface.co/shi-labs/oneformer_ade20k_swin_tiny#how-to-use) How to use 
Here is how to use this model:

```
from transformers import OneFormerProcessor, OneFormerForUniversalSegmentation
from PIL import Image
import requests
url = "https://huggingface.co/datasets/shi-labs/oneformer_demo/blob/main/ade20k.jpeg"
image = Image.open(requests.get(url, stream=True).raw)

# Loading a single model for all three tasks
processor = OneFormerProcessor.from_pretrained("shi-labs/oneformer_ade20k_swin_tiny")
model = OneFormerForUniversalSegmentation.from_pretrained("shi-labs/oneformer_ade20k_swin_tiny")

# Semantic Segmentation
semantic_inputs = processor(images=image, task_inputs=["semantic"], return_tensors="pt")
semantic_outputs = model(**semantic_inputs)
# pass through image_processor for postprocessing
predicted_semantic_map = processor.post_process_semantic_segmentation(outputs, target_sizes=[image.size[::-1]])[0]

# Instance Segmentation
instance_inputs = processor(images=image, task_inputs=["instance"], return_tensors="pt")
instance_outputs = model(**instance_inputs)
# pass through image_processor for postprocessing
predicted_instance_map = processor.post_process_instance_segmentation(outputs, target_sizes=[image.size[::-1]])[0]["segmentation"]

# Panoptic Segmentation
panoptic_inputs = processor(images=image, task_inputs=["panoptic"], return_tensors="pt")
panoptic_outputs = model(**panoptic_inputs)
# pass through image_processor for postprocessing
predicted_semantic_map = processor.post_process_panoptic_segmentation(outputs, target_sizes=[image.size[::-1]])[0]["segmentation"]

```

For more examples, please refer to the [documentation](https://huggingface.co/docs/transformers/master/en/model_doc/oneformer).
###  [ ](https://huggingface.co/shi-labs/oneformer_ade20k_swin_tiny#citation) Citation 

```
@article{jain2022oneformer,
      title={{OneFormer: One Transformer to Rule Universal Image Segmentation}},
      author={Jitesh Jain and Jiachen Li and MangTik Chiu and Ali Hassani and Nikita Orlov and Humphrey Shi},
      journal={arXiv}, 
      year={2022}
    }

```


Downloads last month
    21,004
Inference Providers [NEW](https://huggingface.co/docs/inference-providers)
HF Inference API
[ Image Segmentation ](https://huggingface.co/tasks/image-segmentation "Learn more about image-segmentation")
Examples
Drag image file here or click to browse from your device
Browse for image
View Code Snippets
Maximize
##  Model tree for shi-labs/oneformer_ade20k_swin_tiny [](https://huggingface.co/docs/hub/model-cards#specifying-a-base-model)
Finetunes
[1 model](https://huggingface.co/models?other=base_model:finetune:shi-labs/oneformer_ade20k_swin_tiny)
##  Dataset used to train shi-labs/oneformer_ade20k_swin_tiny
#### [zhoubolei/scene_parse_150 Updated Jan 18, 2024 • 1.94k • 31 ](https://huggingface.co/datasets/zhoubolei/scene_parse_150)
##  Spaces using shi-labs/oneformer_ade20k_swin_tiny 8
[🧪 tarekziade/mic-fleet-candidates ](https://huggingface.co/spaces/tarekziade/mic-fleet-candidates)[🖼 HighCWu/control-lora-v3 ](https://huggingface.co/spaces/HighCWu/control-lora-v3)[📊 SharafeevRavil/test ](https://huggingface.co/spaces/SharafeevRavil/test)[💻 Laihiujin/shi-labs-oneformer_ade20k_swin_tiny ](https://huggingface.co/spaces/Laihiujin/shi-labs-oneformer_ade20k_swin_tiny)[🔥 AIgang777/shi-labs-oneformer_ade20k_swin_tiny ](https://huggingface.co/spaces/AIgang777/shi-labs-oneformer_ade20k_swin_tiny)[📉 yaokunAI/shi-labs-oneformer_ade20k_swin_tiny ](https://huggingface.co/spaces/yaokunAI/shi-labs-oneformer_ade20k_swin_tiny)[👁 we4rt234/shi-labs-oneformer_ade20k_swin_tiny ](https://huggingface.co/spaces/we4rt234/shi-labs-oneformer_ade20k_swin_tiny)[🖼 Asumuna67/control-lora-v3 ](https://huggingface.co/spaces/Asumuna67/control-lora-v3) + 3 Spaces
##  Collection including shi-labs/oneformer_ade20k_swin_tiny
#### [Visual Understanding Collection Accurate & efficient vision models, ops and systems • 15 items • Updated Dec 19, 2025 • 4 ](https://huggingface.co/collections/shi-labs/visual-understanding)
##  Paper for shi-labs/oneformer_ade20k_swin_tiny
#### [OneFormer: One Transformer to Rule Universal Image Segmentation Paper • 2211.06220 • Published Nov 10, 2022 • 1 ](https://huggingface.co/papers/2211.06220)
System theme
Company
[TOS](https://huggingface.co/terms-of-service) [Privacy](https://huggingface.co/privacy) [About](https://huggingface.co/huggingface) [Careers](https://apply.workable.com/huggingface/) [](https://huggingface.co/)
Website
[Models](https://huggingface.co/models) [Datasets](https://huggingface.co/datasets) [Spaces](https://huggingface.co/spaces) [Pricing](https://huggingface.co/pricing) [Docs](https://huggingface.co/docs)
This is not a dataset id from hf.co/datasets
Inference providers allow you to run inference using different serverless providers.
##  Run 15,000+ Models Instantly
Inference Providers let you run inference on thousands of models served by our partners using a simple, unified, OpenAI-compatible serverless API ([Learn more](https://huggingface.co/docs/inference-providers)).
shi-labs/oneformer_ade20k_swin_tiny is supported by the following Inference Providers:
HF Inference API
View API Code Dismiss

