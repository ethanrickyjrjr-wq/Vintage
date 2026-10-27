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
[ ![](https://cdn-avatars.huggingface.co/v1/production/uploads/65df9200dc3292a8983e5017/Vs5FPVCH-VZBipV3qKTuy.png) ](https://huggingface.co/nvidia)
[nvidia](https://huggingface.co/nvidia)
/
[segformer-b0-finetuned-ade-512-512](https://huggingface.co/nvidia/segformer-b0-finetuned-ade-512-512)
Like 210
Follow
![](https://cdn-avatars.huggingface.co/v1/production/uploads/65df9200dc3292a8983e5017/Vs5FPVCH-VZBipV3qKTuy.png) NVIDIA 73k
[ Image Segmentation ](https://huggingface.co/models?pipeline_tag=image-segmentation)[ Transformers ](https://huggingface.co/models?library=transformers)[ PyTorch ](https://huggingface.co/models?library=pytorch)[ google-tensorflow TensorFlow ](https://huggingface.co/models?library=tf)[ Safetensors ](https://huggingface.co/models?library=safetensors)
scene_parse_150
[ segformer ](https://huggingface.co/models?other=segformer)[ vision ](https://huggingface.co/models?other=vision)
arxiv: 2105.15203
License: other
[ Model card ](https://huggingface.co/nvidia/segformer-b0-finetuned-ade-512-512)[ Files Files and versions xet ](https://huggingface.co/nvidia/segformer-b0-finetuned-ade-512-512/tree/main)[ Community 11 ](https://huggingface.co/nvidia/segformer-b0-finetuned-ade-512-512/discussions)
Deploy
Copy to bucket
Use this model
### Instructions to use nvidia/segformer-b0-finetuned-ade-512-512 with libraries, inference providers, notebooks, and local apps. Follow these links to get started.
  * Libraries
  * [ Transformers](https://huggingface.co/nvidia/segformer-b0-finetuned-ade-512-512?library=transformers)
How to use nvidia/segformer-b0-finetuned-ade-512-512 with Transformers:

```
# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("image-segmentation", model="nvidia/segformer-b0-finetuned-ade-512-512")
```

```
# pip install -U transformers accelerate
# Load model directly
from transformers import AutoImageProcessor, SegformerForSemanticSegmentation

processor = AutoImageProcessor.from_pretrained("nvidia/segformer-b0-finetuned-ade-512-512")
model = SegformerForSemanticSegmentation.from_pretrained("nvidia/segformer-b0-finetuned-ade-512-512", device_map="auto")
```

  * Inference
  * Inference Providers
  * Notebooks
  * [ Google Colab](https://huggingface.co/nvidia/segformer-b0-finetuned-ade-512-512/colab)
  * [ Kaggle](https://huggingface.co/nvidia/segformer-b0-finetuned-ade-512-512/kaggle)


  * [SegFormer (b0-sized) model fine-tuned on ADE20k](https://huggingface.co/nvidia/segformer-b0-finetuned-ade-512-512#segformer-b0-sized-model-fine-tuned-on-ade20k "SegFormer \(b0-sized\) model fine-tuned on ADE20k")
    * [Model description](https://huggingface.co/nvidia/segformer-b0-finetuned-ade-512-512#model-description "Model description")
    * [Intended uses & limitations](https://huggingface.co/nvidia/segformer-b0-finetuned-ade-512-512#intended-uses--limitations "Intended uses &amp; limitations")
      * [How to use](https://huggingface.co/nvidia/segformer-b0-finetuned-ade-512-512#how-to-use "How to use")
      * [License](https://huggingface.co/nvidia/segformer-b0-finetuned-ade-512-512#license "License")
      * [BibTeX entry and citation info](https://huggingface.co/nvidia/segformer-b0-finetuned-ade-512-512#bibtex-entry-and-citation-info "BibTeX entry and citation info")


#  [ ](https://huggingface.co/nvidia/segformer-b0-finetuned-ade-512-512#segformer-b0-sized-model-fine-tuned-on-ade20k) SegFormer (b0-sized) model fine-tuned on ADE20k 
SegFormer model fine-tuned on ADE20k at resolution 512x512. It was introduced in the paper [SegFormer: Simple and Efficient Design for Semantic Segmentation with Transformers](https://arxiv.org/abs/2105.15203) by Xie et al. and first released in [this repository](https://github.com/NVlabs/SegFormer). 
Disclaimer: The team releasing SegFormer did not write a model card for this model so this model card has been written by the Hugging Face team.
##  [ ](https://huggingface.co/nvidia/segformer-b0-finetuned-ade-512-512#model-description) Model description 
SegFormer consists of a hierarchical Transformer encoder and a lightweight all-MLP decode head to achieve great results on semantic segmentation benchmarks such as ADE20K and Cityscapes. The hierarchical Transformer is first pre-trained on ImageNet-1k, after which a decode head is added and fine-tuned altogether on a downstream dataset.
##  [ ](https://huggingface.co/nvidia/segformer-b0-finetuned-ade-512-512#intended-uses--limitations) Intended uses & limitations 
You can use the raw model for semantic segmentation. See the [model hub](https://huggingface.co/models?other=segformer) to look for fine-tuned versions on a task that interests you.
###  [ ](https://huggingface.co/nvidia/segformer-b0-finetuned-ade-512-512#how-to-use) How to use 
Here is how to use this model to classify an image of the COCO 2017 dataset into one of the 1,000 ImageNet classes:

```
from transformers import SegformerImageProcessor, SegformerForSemanticSegmentation
from PIL import Image
import requests

processor = SegformerImageProcessor.from_pretrained("nvidia/segformer-b0-finetuned-ade-512-512")
model = SegformerForSemanticSegmentation.from_pretrained("nvidia/segformer-b0-finetuned-ade-512-512")

url = "http://images.cocodataset.org/val2017/000000039769.jpg"
image = Image.open(requests.get(url, stream=True).raw)

inputs = processor(images=image, return_tensors="pt")
outputs = model(**inputs)
logits = outputs.logits  # shape (batch_size, num_labels, height/4, width/4)

```

For more code examples, we refer to the [documentation](https://huggingface.co/transformers/model_doc/segformer.html).
###  [ ](https://huggingface.co/nvidia/segformer-b0-finetuned-ade-512-512#license) License 
The license for this model can be found [here](https://github.com/NVlabs/SegFormer/blob/master/LICENSE).
###  [ ](https://huggingface.co/nvidia/segformer-b0-finetuned-ade-512-512#bibtex-entry-and-citation-info) BibTeX entry and citation info 

```
@article{DBLP:journals/corr/abs-2105-15203,
  author    = {Enze Xie and
               Wenhai Wang and
               Zhiding Yu and
               Anima Anandkumar and
               Jose M. Alvarez and
               Ping Luo},
  title     = {SegFormer: Simple and Efficient Design for Semantic Segmentation with
               Transformers},
  journal   = {CoRR},
  volume    = {abs/2105.15203},
  year      = {2021},
  url       = {https://arxiv.org/abs/2105.15203},
  eprinttype = {arXiv},
  eprint    = {2105.15203},
  timestamp = {Wed, 02 Jun 2021 11:46:42 +0200},
  biburl    = {https://dblp.org/rec/journals/corr/abs-2105-15203.bib},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}

```


Downloads last month
    286,038
Safetensors[](https://huggingface.co/docs/safetensors)
Model size
3.75M params
Tensor type
F32 
·
Files info
Inference Providers [NEW](https://huggingface.co/docs/inference-providers)
HF Inference API
[ Image Segmentation ](https://huggingface.co/tasks/image-segmentation "Learn more about image-segmentation")
Examples
Drag image file here or click to browse from your device
Browse for image
View Code Snippets
Maximize
##  Model tree for nvidia/segformer-b0-finetuned-ade-512-512 [](https://huggingface.co/docs/hub/model-cards#specifying-a-base-model)
Adapters
[1 model](https://huggingface.co/models?other=base_model:adapter:nvidia/segformer-b0-finetuned-ade-512-512)
Finetunes
[54 models](https://huggingface.co/models?other=base_model:finetune:nvidia/segformer-b0-finetuned-ade-512-512)
Quantizations
[2 models](https://huggingface.co/models?other=base_model:quantized:nvidia/segformer-b0-finetuned-ade-512-512)
##  Dataset used to train nvidia/segformer-b0-finetuned-ade-512-512
#### [zhoubolei/scene_parse_150 Updated Jan 18, 2024 • 1.94k • 31 ](https://huggingface.co/datasets/zhoubolei/scene_parse_150)
##  Spaces using nvidia/segformer-b0-finetuned-ade-512-512 100
[💻 chroneus/stylematte ](https://huggingface.co/spaces/chroneus/stylematte)[🌍 nickkun/Vision_Transformer-Segmentation ](https://huggingface.co/spaces/nickkun/Vision_Transformer-Segmentation)[🛋️ mshayan8401/aeterna ](https://huggingface.co/spaces/mshayan8401/aeterna)[👁 axelhortua/Object-segmentation ](https://huggingface.co/spaces/axelhortua/Object-segmentation)[📊 sofmi/semantic-segmentation-revamped ](https://huggingface.co/spaces/sofmi/semantic-segmentation-revamped)[💻 befozg/stylematte ](https://huggingface.co/spaces/befozg/stylematte)[👀 Ane4ka/422_MTDDP ](https://huggingface.co/spaces/Ane4ka/422_MTDDP)[👀 LeeRuben/rae_2 ](https://huggingface.co/spaces/LeeRuben/rae_2) + 95 Spaces + 92 Spaces
##  Paper for nvidia/segformer-b0-finetuned-ade-512-512
#### [SegFormer: Simple and Efficient Design for Semantic Segmentation with Transformers Paper • 2105.15203 • Published May 31, 2021 • 3 ](https://huggingface.co/papers/2105.15203)
System theme
Company
[TOS](https://huggingface.co/terms-of-service) [Privacy](https://huggingface.co/privacy) [About](https://huggingface.co/huggingface) [Careers](https://apply.workable.com/huggingface/) [](https://huggingface.co/)
Website
[Models](https://huggingface.co/models) [Datasets](https://huggingface.co/datasets) [Spaces](https://huggingface.co/spaces) [Pricing](https://huggingface.co/pricing) [Docs](https://huggingface.co/docs)
This is not a dataset id from hf.co/datasets
Inference providers allow you to run inference using different serverless providers.
##  Run 15,000+ Models Instantly
Inference Providers let you run inference on thousands of models served by our partners using a simple, unified, OpenAI-compatible serverless API ([Learn more](https://huggingface.co/docs/inference-providers)).
nvidia/segformer-b0-finetuned-ade-512-512 is supported by the following Inference Providers:
HF Inference API
View API Code Dismiss

