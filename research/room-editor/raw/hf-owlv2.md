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
[ ![](https://cdn-avatars.huggingface.co/v1/production/uploads/5dd96eb166059660ed1ee413/WtA3YYitedOr9n02eHfJe.png) ](https://huggingface.co/google)
[google](https://huggingface.co/google)
/
[owlv2-base-patch16-ensemble](https://huggingface.co/google/owlv2-base-patch16-ensemble)
Like 148
Follow
![](https://cdn-avatars.huggingface.co/v1/production/uploads/5dd96eb166059660ed1ee413/WtA3YYitedOr9n02eHfJe.png) Google 71.9k
[ Zero-Shot Object Detection ](https://huggingface.co/models?pipeline_tag=zero-shot-object-detection)[ Transformers ](https://huggingface.co/models?library=transformers)[ PyTorch ](https://huggingface.co/models?library=pytorch)[ Safetensors ](https://huggingface.co/models?library=safetensors)[ owlv2 ](https://huggingface.co/models?other=owlv2)[ vision ](https://huggingface.co/models?other=vision)
arxiv: 2306.09683
License: apache-2.0
[ Model card ](https://huggingface.co/google/owlv2-base-patch16-ensemble)[ Files Files and versions xet ](https://huggingface.co/google/owlv2-base-patch16-ensemble/tree/main)[ Community 8 ](https://huggingface.co/google/owlv2-base-patch16-ensemble/discussions)
Deploy
Copy to bucket
Use this model
### Instructions to use google/owlv2-base-patch16-ensemble with libraries, inference providers, notebooks, and local apps. Follow these links to get started.
  * Libraries
  * [ Transformers](https://huggingface.co/google/owlv2-base-patch16-ensemble?library=transformers)
How to use google/owlv2-base-patch16-ensemble with Transformers:

```
# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("zero-shot-object-detection", model="google/owlv2-base-patch16-ensemble")
```

```
# pip install -U transformers accelerate
# Load model directly
from transformers import AutoProcessor, AutoModelForZeroShotObjectDetection

processor = AutoProcessor.from_pretrained("google/owlv2-base-patch16-ensemble")
model = AutoModelForZeroShotObjectDetection.from_pretrained("google/owlv2-base-patch16-ensemble", device_map="auto")
```

  * Notebooks
  * [ Google Colab](https://huggingface.co/google/owlv2-base-patch16-ensemble/colab)
  * [ Kaggle](https://huggingface.co/google/owlv2-base-patch16-ensemble/kaggle)


  * [Model Card: OWLv2](https://huggingface.co/google/owlv2-base-patch16-ensemble#model-card-owlv2 "Model Card: OWLv2")
    * [Model Details](https://huggingface.co/google/owlv2-base-patch16-ensemble#model-details "Model Details")
      * [Model Date](https://huggingface.co/google/owlv2-base-patch16-ensemble#model-date "Model Date")
      * [Model Type](https://huggingface.co/google/owlv2-base-patch16-ensemble#model-type "Model Type")
      * [Documents](https://huggingface.co/google/owlv2-base-patch16-ensemble#documents "Documents")
      * [Use with Transformers](https://huggingface.co/google/owlv2-base-patch16-ensemble#use-with-transformers "Use with Transformers")
    * [Model Use](https://huggingface.co/google/owlv2-base-patch16-ensemble#model-use "Model Use")
      * [Intended Use](https://huggingface.co/google/owlv2-base-patch16-ensemble#intended-use "Intended Use")
    * [Data](https://huggingface.co/google/owlv2-base-patch16-ensemble#data "Data")
      * [BibTeX entry and citation info](https://huggingface.co/google/owlv2-base-patch16-ensemble#bibtex-entry-and-citation-info "BibTeX entry and citation info")


#  [ ](https://huggingface.co/google/owlv2-base-patch16-ensemble#model-card-owlv2) Model Card: OWLv2 
##  [ ](https://huggingface.co/google/owlv2-base-patch16-ensemble#model-details) Model Details 
The OWLv2 model (short for Open-World Localization) was proposed in [Scaling Open-Vocabulary Object Detection](https://arxiv.org/abs/2306.09683) by Matthias Minderer, Alexey Gritsenko, Neil Houlsby. OWLv2, like OWL-ViT, is a zero-shot text-conditioned object detection model that can be used to query an image with one or multiple text queries. 
The model uses CLIP as its multi-modal backbone, with a ViT-like Transformer to get visual features and a causal language model to get the text features. To use CLIP for detection, OWL-ViT removes the final token pooling layer of the vision model and attaches a lightweight classification and box head to each transformer output token. Open-vocabulary classification is enabled by replacing the fixed classification layer weights with the class-name embeddings obtained from the text model. The authors first train CLIP from scratch and fine-tune it end-to-end with the classification and box heads on standard detection datasets using a bipartite matching loss. One or multiple text queries per image can be used to perform zero-shot text-conditioned object detection. 
###  [ ](https://huggingface.co/google/owlv2-base-patch16-ensemble#model-date) Model Date 
June 2023
###  [ ](https://huggingface.co/google/owlv2-base-patch16-ensemble#model-type) Model Type 
The model uses a CLIP backbone with a ViT-B/16 Transformer architecture as an image encoder and uses a masked self-attention Transformer as a text encoder. These encoders are trained to maximize the similarity of (image, text) pairs via a contrastive loss. The CLIP backbone is trained from scratch and fine-tuned together with the box and class prediction heads with an object detection objective.
###  [ ](https://huggingface.co/google/owlv2-base-patch16-ensemble#documents) Documents 
  * [OWLv2 Paper](https://arxiv.org/abs/2306.09683)


###  [ ](https://huggingface.co/google/owlv2-base-patch16-ensemble#use-with-transformers) Use with Transformers 

```
import requests
from PIL import Image
import torch

from transformers import Owlv2Processor, Owlv2ForObjectDetection

processor = Owlv2Processor.from_pretrained("google/owlv2-base-patch16-ensemble")
model = Owlv2ForObjectDetection.from_pretrained("google/owlv2-base-patch16-ensemble")

url = "http://images.cocodataset.org/val2017/000000039769.jpg"
image = Image.open(requests.get(url, stream=True).raw)
texts = [["a photo of a cat", "a photo of a dog"]]
inputs = processor(text=texts, images=image, return_tensors="pt")

with torch.no_grad():
  outputs = model(**inputs)

# Target image sizes (height, width) to rescale box predictions [batch_size, 2]
target_sizes = torch.Tensor([image.size[::-1]])
# Convert outputs (bounding boxes and class logits) to Pascal VOC Format (xmin, ymin, xmax, ymax)
results = processor.post_process_object_detection(outputs=outputs, target_sizes=target_sizes, threshold=0.1)
i = 0  # Retrieve predictions for the first image for the corresponding text queries
text = texts[i]
boxes, scores, labels = results[i]["boxes"], results[i]["scores"], results[i]["labels"]
for box, score, label in zip(boxes, scores, labels):
    box = [round(i, 2) for i in box.tolist()]
    print(f"Detected {text[label]} with confidence {round(score.item(), 3)} at location {box}")

```

##  [ ](https://huggingface.co/google/owlv2-base-patch16-ensemble#model-use) Model Use 
###  [ ](https://huggingface.co/google/owlv2-base-patch16-ensemble#intended-use) Intended Use 
The model is intended as a research output for research communities. We hope that this model will enable researchers to better understand and explore zero-shot, text-conditioned object detection. We also hope it can be used for interdisciplinary studies of the potential impact of such models, especially in areas that commonly require identifying objects whose label is unavailable during training.
####  [ ](https://huggingface.co/google/owlv2-base-patch16-ensemble#primary-intended-uses) Primary intended uses 
The primary intended users of these models are AI researchers.
We primarily imagine the model will be used by researchers to better understand robustness, generalization, and other capabilities, biases, and constraints of computer vision models.
##  [ ](https://huggingface.co/google/owlv2-base-patch16-ensemble#data) Data 
The CLIP backbone of the model was trained on publicly available image-caption data. This was done through a combination of crawling a handful of websites and using commonly-used pre-existing image datasets such as [YFCC100M](http://projects.dfki.uni-kl.de/yfcc100m/). A large portion of the data comes from our crawling of the internet. This means that the data is more representative of people and societies most connected to the internet. The prediction heads of OWL-ViT, along with the CLIP backbone, are fine-tuned on publicly available object detection datasets such as [COCO](https://cocodataset.org/#home) and [OpenImages](https://storage.googleapis.com/openimages/web/index.html).
(to be updated for v2)
###  [ ](https://huggingface.co/google/owlv2-base-patch16-ensemble#bibtex-entry-and-citation-info) BibTeX entry and citation info 

```
@misc{minderer2023scaling,
      title={Scaling Open-Vocabulary Object Detection}, 
      author={Matthias Minderer and Alexey Gritsenko and Neil Houlsby},
      year={2023},
      eprint={2306.09683},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}

```


Downloads last month
    1,578,253
Safetensors[](https://huggingface.co/docs/safetensors)
Model size
0.2B params
Tensor type
F32 
·
Files info
Inference Providers [NEW](https://huggingface.co/docs/inference-providers)
[ Zero-Shot Object Detection ](https://huggingface.co/tasks/zero-shot-object-detection "Learn more about zero-shot-object-detection")
This model isn't deployed by any Inference Provider. [🙋 Ask for provider support](https://huggingface.co/spaces/huggingface/InferenceSupport/discussions/new?title=google/owlv2-base-patch16-ensemble&description=React%20to%20this%20comment%20with%20an%20emoji%20to%20vote%20for%20%5Bgoogle%2Fowlv2-base-patch16-ensemble%5D\(%2Fgoogle%2Fowlv2-base-patch16-ensemble\)%20to%20be%20supported%20by%20Inference%20Providers.%0A%0A\(optional\)%20Which%20providers%20are%20you%20interested%20in%3F%20\(Novita%2C%20Hyperbolic%2C%20Together%E2%80%A6\)%0A)
##  Model tree for google/owlv2-base-patch16-ensemble [](https://huggingface.co/docs/hub/model-cards#specifying-a-base-model)
Finetunes
[2 models](https://huggingface.co/models?other=base_model:finetune:google/owlv2-base-patch16-ensemble)
Quantizations
[2 models](https://huggingface.co/models?other=base_model:quantized:google/owlv2-base-patch16-ensemble)
##  Spaces using google/owlv2-base-patch16-ensemble 86
[😻 merve/OWLSAM ](https://huggingface.co/spaces/merve/OWLSAM)[👀 merve/owlv2 ](https://huggingface.co/spaces/merve/owlv2)[⚡ merve/owl-tracking ](https://huggingface.co/spaces/merve/owl-tracking)[🦖🦉 merve/GroundingDINO_OWL ](https://huggingface.co/spaces/merve/GroundingDINO_OWL)[🔥 fancyfeast/joycaption-watermark-detection ](https://huggingface.co/spaces/fancyfeast/joycaption-watermark-detection)[📈 emanforhelp/model-pulse ](https://huggingface.co/spaces/emanforhelp/model-pulse)[👀 vvmnnnkv/owlv2-visual-prompt ](https://huggingface.co/spaces/vvmnnnkv/owlv2-visual-prompt)[🤖 manavgoel4/reachy_desk_assistant ](https://huggingface.co/spaces/manavgoel4/reachy_desk_assistant) + 81 Spaces + 78 Spaces
##  Paper for google/owlv2-base-patch16-ensemble
#### [Scaling Open-Vocabulary Object Detection Paper • 2306.09683 • Published Jun 16, 2023 • 16 ](https://huggingface.co/papers/2306.09683)
System theme
Company
[TOS](https://huggingface.co/terms-of-service) [Privacy](https://huggingface.co/privacy) [About](https://huggingface.co/huggingface) [Careers](https://apply.workable.com/huggingface/) [](https://huggingface.co/)
Website
[Models](https://huggingface.co/models) [Datasets](https://huggingface.co/datasets) [Spaces](https://huggingface.co/spaces) [Pricing](https://huggingface.co/pricing) [Docs](https://huggingface.co/docs)

