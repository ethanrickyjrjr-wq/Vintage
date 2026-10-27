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
[ ![](https://cdn-avatars.huggingface.co/v1/production/uploads/1583646260758-5e64858c87403103f9f1055d.png) ](https://huggingface.co/microsoft)
[microsoft](https://huggingface.co/microsoft)
/
[Florence-2-base](https://huggingface.co/microsoft/Florence-2-base)
Like 432
Follow
![](https://cdn-avatars.huggingface.co/v1/production/uploads/1583646260758-5e64858c87403103f9f1055d.png) Microsoft 22.8k
[ Image-Text-to-Text ](https://huggingface.co/models?pipeline_tag=image-text-to-text)[ Transformers ](https://huggingface.co/models?library=transformers)[ PyTorch ](https://huggingface.co/models?library=pytorch)[ Safetensors ](https://huggingface.co/models?library=safetensors)[ florence2 ](https://huggingface.co/models?other=florence2)[ vision ](https://huggingface.co/models?other=vision)[ custom_code ](https://huggingface.co/models?other=custom_code)
arxiv: 2311.06242
License: mit
[ Model card ](https://huggingface.co/microsoft/Florence-2-base)[ Files Files and versions xet ](https://huggingface.co/microsoft/Florence-2-base/tree/main)[ Community 36 ](https://huggingface.co/microsoft/Florence-2-base/discussions)
Deploy
Copy to bucket
Use this model
### Instructions to use microsoft/Florence-2-base with libraries, inference providers, notebooks, and local apps. Follow these links to get started.
  * Libraries
  * [ Transformers](https://huggingface.co/microsoft/Florence-2-base?library=transformers)
How to use microsoft/Florence-2-base with Transformers:

```
# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("image-text-to-text", model="microsoft/Florence-2-base", trust_remote_code=True)
```

```
# pip install -U transformers accelerate
# Load model directly
from transformers import AutoProcessor, AutoModelForMultimodalLM

processor = AutoProcessor.from_pretrained("microsoft/Florence-2-base", trust_remote_code=True)
model = AutoModelForMultimodalLM.from_pretrained("microsoft/Florence-2-base", trust_remote_code=True, device_map="auto")
```

  * Notebooks
  * [ Google Colab](https://huggingface.co/microsoft/Florence-2-base/colab)
  * [ Kaggle](https://huggingface.co/microsoft/Florence-2-base/kaggle)
  * Local Apps [Settings](https://huggingface.co/settings/local-apps "Set up your favorite local applications")
  * [ vLLM ](https://huggingface.co/microsoft/Florence-2-base?local-app=vllm)
How to use microsoft/Florence-2-base with vLLM:
##### Install from pip and serve model

```
# Install vLLM from pip:
pip install vllm
# Start the vLLM server:
vllm serve "microsoft/Florence-2-base"
# Call the server using curl (OpenAI-compatible API):
curl -X POST "http://localhost:8000/v1/completions" \
	-H "Content-Type: application/json" \
	--data '{
		"model": "microsoft/Florence-2-base",
		"prompt": "Once upon a time,",
		"max_tokens": 512,
		"temperature": 0.5
	}'
```

##### Use Docker

```
docker model run hf.co/microsoft/Florence-2-base
```

  * [ SGLang ](https://huggingface.co/microsoft/Florence-2-base?local-app=sglang)
How to use microsoft/Florence-2-base with SGLang:
##### Install from pip and serve model

```
# Install SGLang from pip:
pip install sglang
# Start the SGLang server:
python3 -m sglang.launch_server \
    --model-path "microsoft/Florence-2-base" \
    --host 0.0.0.0 \
    --port 30000
# Call the server using curl (OpenAI-compatible API):
curl -X POST "http://localhost:30000/v1/completions" \
	-H "Content-Type: application/json" \
	--data '{
		"model": "microsoft/Florence-2-base",
		"prompt": "Once upon a time,",
		"max_tokens": 512,
		"temperature": 0.5
	}'
```

##### Use Docker images

```
docker run --gpus all \
    --shm-size 32g \
    -p 30000:30000 \
    -v ~/.cache/huggingface:/root/.cache/huggingface \
    --env "HF_TOKEN=<secret>" \
    --ipc=host \
    lmsysorg/sglang:latest \
    python3 -m sglang.launch_server \
        --model-path "microsoft/Florence-2-base" \
        --host 0.0.0.0 \
        --port 30000
# Call the server using curl (OpenAI-compatible API):
curl -X POST "http://localhost:30000/v1/completions" \
	-H "Content-Type: application/json" \
	--data '{
		"model": "microsoft/Florence-2-base",
		"prompt": "Once upon a time,",
		"max_tokens": 512,
		"temperature": 0.5
	}'
```

  * [ Docker Model Runner ](https://huggingface.co/microsoft/Florence-2-base?local-app=docker-model-runner)
How to use microsoft/Florence-2-base with Docker Model Runner:

```
docker model run hf.co/microsoft/Florence-2-base
```

  * [Browse Quantizations](https://huggingface.co/models?other=base_model:quantized:microsoft/Florence-2-base) to use this model in  llama.cpp,  Ollama,  LM Studio, or any compatible app.


  * [Florence-2: Advancing a Unified Representation for a Variety of Vision Tasks](https://huggingface.co/microsoft/Florence-2-base#florence-2-advancing-a-unified-representation-for-a-variety-of-vision-tasks "Florence-2: Advancing a Unified Representation for a Variety of Vision Tasks")
    * [Model Summary](https://huggingface.co/microsoft/Florence-2-base#model-summary "Model Summary")
    * [How to Get Started with the Model](https://huggingface.co/microsoft/Florence-2-base#how-to-get-started-with-the-model "How to Get Started with the Model")
    * [Tasks](https://huggingface.co/microsoft/Florence-2-base#tasks "Tasks")
      * [Caption](https://huggingface.co/microsoft/Florence-2-base#caption "Caption")
      * [Detailed Caption](https://huggingface.co/microsoft/Florence-2-base#detailed-caption "Detailed Caption")
      * [More Detailed Caption](https://huggingface.co/microsoft/Florence-2-base#more-detailed-caption "More Detailed Caption")
      * [Caption to Phrase Grounding](https://huggingface.co/microsoft/Florence-2-base#caption-to-phrase-grounding "Caption to Phrase Grounding")
      * [Object Detection](https://huggingface.co/microsoft/Florence-2-base#object-detection "Object Detection")
      * [Dense Region Caption](https://huggingface.co/microsoft/Florence-2-base#dense-region-caption "Dense Region Caption")
      * [Region proposal](https://huggingface.co/microsoft/Florence-2-base#region-proposal "Region proposal")
      * [OCR](https://huggingface.co/microsoft/Florence-2-base#ocr "OCR")
      * [OCR with Region](https://huggingface.co/microsoft/Florence-2-base#ocr-with-region "OCR with Region")
  * [Benchmarks](https://huggingface.co/microsoft/Florence-2-base#benchmarks "Benchmarks")
    * [Florence-2 Zero-shot performance](https://huggingface.co/microsoft/Florence-2-base#florence-2-zero-shot-performance "Florence-2 Zero-shot performance")
    * [Florence-2 finetuned performance](https://huggingface.co/microsoft/Florence-2-base#florence-2-finetuned-performance "Florence-2 finetuned performance")
    * [BibTex and citation info](https://huggingface.co/microsoft/Florence-2-base#bibtex-and-citation-info "BibTex and citation info")


#  [ ](https://huggingface.co/microsoft/Florence-2-base#florence-2-advancing-a-unified-representation-for-a-variety-of-vision-tasks) Florence-2: Advancing a Unified Representation for a Variety of Vision Tasks 
##  [ ](https://huggingface.co/microsoft/Florence-2-base#model-summary) Model Summary 
This Hub repository contains a HuggingFace's `transformers` implementation of Florence-2 model from Microsoft.
Florence-2 is an advanced vision foundation model that uses a prompt-based approach to handle a wide range of vision and vision-language tasks. Florence-2 can interpret simple text prompts to perform tasks like captioning, object detection, and segmentation. It leverages our FLD-5B dataset, containing 5.4 billion annotations across 126 million images, to master multi-task learning. The model's sequence-to-sequence architecture enables it to excel in both zero-shot and fine-tuned settings, proving to be a competitive vision foundation model. 
Resources and Technical Documentation:
  * [Florence-2 technical report](https://arxiv.org/abs/2311.06242). 
  * [Jupyter Notebook for inference and visualization of Florence-2-large model](https://huggingface.co/microsoft/Florence-2-large/blob/main/sample_inference.ipynb)

  
| Model  | Model size  | Model Description  |  
| --- | --- | --- |  
| Florence-2-base[[HF]](https://huggingface.co/microsoft/Florence-2-base)  | 0.23B  | Pretrained model with FLD-5B  |  
| Florence-2-large[[HF]](https://huggingface.co/microsoft/Florence-2-large)  | 0.77B  | Pretrained model with FLD-5B  |  
| Florence-2-base-ft[[HF]](https://huggingface.co/microsoft/Florence-2-base-ft)  | 0.23B  | Finetuned model on a colletion of downstream tasks  |  
| Florence-2-large-ft[[HF]](https://huggingface.co/microsoft/Florence-2-large-ft)  | 0.77B  | Finetuned model on a colletion of downstream tasks  |  
##  [ ](https://huggingface.co/microsoft/Florence-2-base#how-to-get-started-with-the-model) How to Get Started with the Model 
Use the code below to get started with the model. All models are trained with float16. 

```
import requests

from PIL import Image
from transformers import AutoProcessor, AutoModelForCausalLM 

device = "cuda:0" if torch.cuda.is_available() else "cpu"
torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32

model = AutoModelForCausalLM.from_pretrained("microsoft/Florence-2-base", torch_dtype=torch_dtype, trust_remote_code=True).to(device)
processor = AutoProcessor.from_pretrained("microsoft/Florence-2-base", trust_remote_code=True)

prompt = "<OD>"

url = "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/tasks/car.jpg?download=true"
image = Image.open(requests.get(url, stream=True).raw)

inputs = processor(text=prompt, images=image, return_tensors="pt").to(device, torch_dtype)

generated_ids = model.generate(
    input_ids=inputs["input_ids"],
    pixel_values=inputs["pixel_values"],
    max_new_tokens=1024,
    do_sample=False,
    num_beams=3,
)
generated_text = processor.batch_decode(generated_ids, skip_special_tokens=False)[0]

parsed_answer = processor.post_process_generation(generated_text, task="<OD>", image_size=(image.width, image.height))

print(parsed_answer)

```

##  [ ](https://huggingface.co/microsoft/Florence-2-base#tasks) Tasks 
This model is capable of performing different tasks through changing the prompts.
First, let's define a function to run a prompt.
Click to expand 

```
import requests

from PIL import Image
from transformers import AutoProcessor, AutoModelForCausalLM 

device = "cuda:0" if torch.cuda.is_available() else "cpu"
torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32

model = AutoModelForCausalLM.from_pretrained("microsoft/Florence-2-base", torch_dtype=torch_dtype, trust_remote_code=True).to(device)
processor = AutoProcessor.from_pretrained("microsoft/Florence-2-base", trust_remote_code=True)

url = "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/tasks/car.jpg?download=true"
image = Image.open(requests.get(url, stream=True).raw)

def run_example(task_prompt, text_input=None):
    if text_input is None:
        prompt = task_prompt
    else:
        prompt = task_prompt + text_input
    inputs = processor(text=prompt, images=image, return_tensors="pt").to(device, torch_dtype)
    generated_ids = model.generate(
      input_ids=inputs["input_ids"],
      pixel_values=inputs["pixel_values"],
      max_new_tokens=1024,
      num_beams=3
    )
    generated_text = processor.batch_decode(generated_ids, skip_special_tokens=False)[0]

    parsed_answer = processor.post_process_generation(generated_text, task=task_prompt, image_size=(image.width, image.height))

    print(parsed_answer)

```

Here are the tasks `Florence-2` could perform:
Click to expand 
###  [ ](https://huggingface.co/microsoft/Florence-2-base#caption) Caption 

```
prompt = "<CAPTION>"
run_example(prompt)

```

###  [ ](https://huggingface.co/microsoft/Florence-2-base#detailed-caption) Detailed Caption 

```
prompt = "<DETAILED_CAPTION>"
run_example(prompt)

```

###  [ ](https://huggingface.co/microsoft/Florence-2-base#more-detailed-caption) More Detailed Caption 

```
prompt = "<MORE_DETAILED_CAPTION>"
run_example(prompt)

```

###  [ ](https://huggingface.co/microsoft/Florence-2-base#caption-to-phrase-grounding) Caption to Phrase Grounding 
caption to phrase grounding task requires additional text input, i.e. caption. 
Caption to phrase grounding results format: {'<CAPTION_TO_PHRASE_GROUNDING>': {'bboxes': [[x1, y1, x2, y2], ...], 'labels': ['', '', ...]}}

```
task_prompt = "<CAPTION_TO_PHRASE_GROUNDING>"
results = run_example(task_prompt, text_input="A green car parked in front of a yellow building.")

```

###  [ ](https://huggingface.co/microsoft/Florence-2-base#object-detection) Object Detection 
OD results format: {'<OD>': {'bboxes': [[x1, y1, x2, y2], ...], 'labels': ['label1', 'label2', ...]} }

```
prompt = "<OD>"
run_example(prompt)

```

###  [ ](https://huggingface.co/microsoft/Florence-2-base#dense-region-caption) Dense Region Caption 
Dense region caption results format: {'<DENSE_REGION_CAPTION>' : {'bboxes': [[x1, y1, x2, y2], ...], 'labels': ['label1', 'label2', ...]} }

```
prompt = "<DENSE_REGION_CAPTION>"
run_example(prompt)

```

###  [ ](https://huggingface.co/microsoft/Florence-2-base#region-proposal) Region proposal 
Dense region caption results format: {'<REGION_PROPOSAL>': {'bboxes': [[x1, y1, x2, y2], ...], 'labels': ['', '', ...]}}

```
prompt = "<REGION_PROPOSAL>"
run_example(prompt)

```

###  [ ](https://huggingface.co/microsoft/Florence-2-base#ocr) OCR 

```
prompt = "<OCR>"
run_example(prompt)

```

###  [ ](https://huggingface.co/microsoft/Florence-2-base#ocr-with-region) OCR with Region 
OCR with region output format: {'<OCR_WITH_REGION>': {'quad_boxes': [[x1, y1, x2, y2, x3, y3, x4, y4], ...], 'labels': ['text1', ...]}}

```
prompt = "<OCR_WITH_REGION>"
run_example(prompt)

```

for More detailed examples, please refer to [notebook](https://huggingface.co/microsoft/Florence-2-large/blob/main/sample_inference.ipynb)
#  [ ](https://huggingface.co/microsoft/Florence-2-base#benchmarks) Benchmarks 
##  [ ](https://huggingface.co/microsoft/Florence-2-base#florence-2-zero-shot-performance) Florence-2 Zero-shot performance 
The following table presents the zero-shot performance of generalist vision foundation models on image captioning and object detection evaluation tasks. These models have not been exposed to the training data of the evaluation tasks during their training phase.   
| Method  | #params  | COCO Cap. test CIDEr  | NoCaps val CIDEr  | TextCaps val CIDEr  | COCO Det. val2017 mAP  |  
| --- | --- | --- | --- | --- | --- |  
| Flamingo  | 80B  | 84.3  | -  | -  | -  |  
| Florence-2-base  | 0.23B  | 133.0  | 118.7  | 70.1  | 34.7  |  
| Florence-2-large  | 0.77B  | 135.6  | 120.8  | 72.8  | 37.5  |  
The following table continues the comparison with performance on other vision-language evaluation tasks.   
| Method  | Flickr30k test R@1  | Refcoco val Accuracy  | Refcoco test-A Accuracy  | Refcoco test-B Accuracy  | Refcoco+ val Accuracy  | Refcoco+ test-A Accuracy  | Refcoco+ test-B Accuracy  | Refcocog val Accuracy  | Refcocog test Accuracy  | Refcoco RES val mIoU  |  
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |  
| Kosmos-2  | 78.7  | 52.3  | 57.4  | 47.3  | 45.5  | 50.7  | 42.2  | 60.6  | 61.7  | -  |  
| Florence-2-base  | 83.6  | 53.9  | 58.4  | 49.7  | 51.5  | 56.4  | 47.9  | 66.3  | 65.1  | 34.6  |  
| Florence-2-large  | 84.4  | 56.3  | 61.6  | 51.4  | 53.6  | 57.9  | 49.9  | 68.0  | 67.0  | 35.8  |  
##  [ ](https://huggingface.co/microsoft/Florence-2-base#florence-2-finetuned-performance) Florence-2 finetuned performance 
We finetune Florence-2 models with a collection of downstream tasks, resulting two generalist models _Florence-2-base-ft_ and _Florence-2-large-ft_ that can conduct a wide range of downstream tasks. 
The table below compares the performance of specialist and generalist models on various captioning and Visual Question Answering (VQA) tasks. Specialist models are fine-tuned specifically for each task, whereas generalist models are fine-tuned in a task-agnostic manner across all tasks. The symbol "▲" indicates the usage of external OCR as input.   
| Method  | # Params  | COCO Caption Karpathy test CIDEr  | NoCaps val CIDEr  | TextCaps val CIDEr  | VQAv2 test-dev Acc  | TextVQA test-dev Acc  | VizWiz VQA test-dev Acc  |  
| --- | --- | --- | --- | --- | --- | --- | --- |  
| **Specialist Models**  |   |   |   |   |   |   |   |  
| CoCa  | 2.1B  | 143.6  | 122.4  | -  | 82.3  | -  | -  |  
| BLIP-2  | 7.8B  | 144.5  | 121.6  | -  | 82.2  | -  | -  |  
| GIT2  | 5.1B  | 145.0  | 126.9  | 148.6  | 81.7  | 67.3  | 71.0  |  
| Flamingo  | 80B  | 138.1  | -  | -  | 82.0  | 54.1  | 65.7  |  
| PaLI  | 17B  | 149.1  | 127.0  | 160.0▲  | 84.3  | 58.8 / 73.1▲  | 71.6 / 74.4▲  |  
| PaLI-X  | 55B  | 149.2  | 126.3  | 147.0 / 163.7▲  | 86.0  | 71.4 / 80.8▲  | 70.9 / 74.6▲  |  
| **Generalist Models**  |   |   |   |   |   |   |   |  
| Unified-IO  | 2.9B  | -  | 100.0  | -  | 77.9  | -  | 57.4  |  
| Florence-2-base-ft  | 0.23B  | 140.0  | 116.7  | 143.9  | 79.7  | 63.6  | 63.6  |  
| Florence-2-large-ft  | 0.77B  | 143.3  | 124.9  | 151.1  | 81.7  | 73.5  | 72.6  |  
| Method  | # Params  | COCO Det. val2017 mAP  | Flickr30k test R@1  | RefCOCO val Accuracy  | RefCOCO test-A Accuracy  | RefCOCO test-B Accuracy  | RefCOCO+ val Accuracy  | RefCOCO+ test-A Accuracy  | RefCOCO+ test-B Accuracy  | RefCOCOg val Accuracy  | RefCOCOg test Accuracy  | RefCOCO RES val mIoU  |  
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |  
| **Specialist Models**  |   |   |   |   |   |   |   |   |   |   |   |   |  
| SeqTR  | -  | -  | -  | 83.7  | 86.5  | 81.2  | 71.5  | 76.3  | 64.9  | 74.9  | 74.2  | -  |  
| PolyFormer  | -  | -  | -  | 90.4  | 92.9  | 87.2  | 85.0  | 89.8  | 78.0  | 85.8  | 85.9  | 76.9  |  
| UNINEXT  | 0.74B  | 60.6  | -  | 92.6  | 94.3  | 91.5  | 85.2  | 89.6  | 79.8  | 88.7  | 89.4  | -  |  
| Ferret  | 13B  | -  | -  | 89.5  | 92.4  | 84.4  | 82.8  | 88.1  | 75.2  | 85.8  | 86.3  | -  |  
| **Generalist Models**  |   |   |   |   |   |   |   |   |   |   |   |   |  
| UniTAB  | -  | -  | -  | 88.6  | 91.1  | 83.8  | 81.0  | 85.4  | 71.6  | 84.6  | 84.7  | -  |  
| Florence-2-base-ft  | 0.23B  | 41.4  | 84.0  | 92.6  | 94.8  | 91.5  | 86.8  | 91.7  | 82.2  | 89.8  | 82.2  | 78.0  |  
| Florence-2-large-ft  | 0.77B  | 43.4  | 85.2  | 93.4  | 95.3  | 92.0  | 88.3  | 92.9  | 83.6  | 91.2  | 91.7  | 80.5  |  
##  [ ](https://huggingface.co/microsoft/Florence-2-base#bibtex-and-citation-info) BibTex and citation info 

```
@article{xiao2023florence,
  title={Florence-2: Advancing a unified representation for a variety of vision tasks},
  author={Xiao, Bin and Wu, Haiping and Xu, Weijian and Dai, Xiyang and Hu, Houdong and Lu, Yumao and Zeng, Michael and Liu, Ce and Yuan, Lu},
  journal={arXiv preprint arXiv:2311.06242},
  year={2023}
}

```


Downloads last month
    3,193,117
Safetensors[](https://huggingface.co/docs/safetensors)
Model size
0.2B params
Tensor type
F16 
·
Files info
Inference Providers [NEW](https://huggingface.co/docs/inference-providers)
[ Image-Text-to-Text ](https://huggingface.co/tasks/image-text-to-text "Learn more about image-text-to-text")
This model isn't deployed by any Inference Provider. [🙋 5 Ask for provider support](https://huggingface.co/spaces/huggingface/InferenceSupport/discussions/2916)
##  Model tree for microsoft/Florence-2-base [](https://huggingface.co/docs/hub/model-cards#specifying-a-base-model)
Adapters
[7 models](https://huggingface.co/models?other=base_model:adapter:microsoft/Florence-2-base)
Finetunes
[21 models](https://huggingface.co/models?other=base_model:finetune:microsoft/Florence-2-base)
Quantizations
[](https://huggingface.co/models?apps=llama.cpp&other=base_model:quantized:microsoft/Florence-2-base "Use with llama.cpp")[](https://huggingface.co/models?apps=llama-app&other=base_model:quantized:microsoft/Florence-2-base "Use with Llama")[](https://huggingface.co/models?apps=lmstudio&other=base_model:quantized:microsoft/Florence-2-base "Use with LM Studio")[](https://huggingface.co/models?apps=jan&other=base_model:quantized:microsoft/Florence-2-base "Use with Jan")
[6 models](https://huggingface.co/models?other=base_model:quantized:microsoft/Florence-2-base)
##  Spaces using microsoft/Florence-2-base 100
[ ![](https://cdn-avatars.huggingface.co/v1/production/uploads/1583646260758-5e64858c87403103f9f1055d.png) microsoft/OmniParser-v2 ](https://huggingface.co/spaces/microsoft/OmniParser-v2)[ ![](https://cdn-avatars.huggingface.co/v1/production/uploads/1583646260758-5e64858c87403103f9f1055d.png) microsoft/OmniParser ](https://huggingface.co/spaces/microsoft/OmniParser)[ ![](https://cdn-avatars.huggingface.co/v1/production/uploads/1583646260758-5e64858c87403103f9f1055d.png) microsoft/Magma-UI ](https://huggingface.co/spaces/microsoft/Magma-UI)[🟩 embedl/hfviewer ](https://huggingface.co/spaces/embedl/hfviewer)[🥐 AlekseyCalvin/SLM_Bistro ](https://huggingface.co/spaces/AlekseyCalvin/SLM_Bistro)[😻 ovi054/image-to-prompt ](https://huggingface.co/spaces/ovi054/image-to-prompt)[📷 raf2e34t/photo-to-info ](https://huggingface.co/spaces/raf2e34t/photo-to-info)[📉 gokaygokay/Florence-2 ](https://huggingface.co/spaces/gokaygokay/Florence-2) + 95 Spaces + 92 Spaces
##  Collection including microsoft/Florence-2-base
#### [Florence Collection 5 items • Updated Mar 2 • 174 ](https://huggingface.co/collections/microsoft/florence)
##  Paper for microsoft/Florence-2-base
#### [Florence-2: Advancing a Unified Representation for a Variety of Vision Tasks Paper • 2311.06242 • Published Nov 10, 2023 • 98 ](https://huggingface.co/papers/2311.06242)
System theme
Company
[TOS](https://huggingface.co/terms-of-service) [Privacy](https://huggingface.co/privacy) [About](https://huggingface.co/huggingface) [Careers](https://apply.workable.com/huggingface/) [](https://huggingface.co/)
Website
[Models](https://huggingface.co/models) [Datasets](https://huggingface.co/datasets) [Spaces](https://huggingface.co/spaces) [Pricing](https://huggingface.co/pricing) [Docs](https://huggingface.co/docs)

