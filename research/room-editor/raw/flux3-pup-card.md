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
[ ![](https://cdn-avatars.huggingface.co/v1/production/uploads/633f7a8f4be90e06da248e0f/m5YoF33abJ09vcwFxt1Mj.png) ](https://huggingface.co/black-forest-labs)
[black-forest-labs](https://huggingface.co/black-forest-labs)
/
[flux-3-image-klein-pup](https://huggingface.co/black-forest-labs/flux-3-image-klein-pup)
Like 68
Follow
![](https://cdn-avatars.huggingface.co/v1/production/uploads/633f7a8f4be90e06da248e0f/m5YoF33abJ09vcwFxt1Mj.png) Black Forest Labs 43.5k
[ Image-Text-to-Text ](https://huggingface.co/models?pipeline_tag=image-text-to-text)[ Transformers ](https://huggingface.co/models?library=transformers)[ Safetensors ](https://huggingface.co/models?library=safetensors)[ English ](https://huggingface.co/models?language=en)[ qwen3_5 ](https://huggingface.co/models?other=qwen3_5)[ prompt-upsampling ](https://huggingface.co/models?other=prompt-upsampling)[ prompt-rewriting ](https://huggingface.co/models?other=prompt-rewriting)[ text-to-image ](https://huggingface.co/models?other=text-to-image)[ image-editing ](https://huggingface.co/models?other=image-editing)[ flux ](https://huggingface.co/models?other=flux)[ flux-3 ](https://huggingface.co/models?other=flux-3)[ black-forest-labs ](https://huggingface.co/models?other=black-forest-labs)[ conversational ](https://huggingface.co/models?other=conversational)
License: apache-2.0
[ Model card ](https://huggingface.co/black-forest-labs/flux-3-image-klein-pup)[ Files Files and versions xet ](https://huggingface.co/black-forest-labs/flux-3-image-klein-pup/tree/main)[ Community 1 ](https://huggingface.co/black-forest-labs/flux-3-image-klein-pup/discussions)
Deploy
Copy to bucket
Use this model
### Instructions to use black-forest-labs/flux-3-image-klein-pup with libraries, inference providers, notebooks, and local apps. Follow these links to get started.
  * Libraries
  * [ Transformers](https://huggingface.co/black-forest-labs/flux-3-image-klein-pup?library=transformers)
How to use black-forest-labs/flux-3-image-klein-pup with Transformers:

```
# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("image-text-to-text", model="black-forest-labs/flux-3-image-klein-pup")
messages = [
    {
        "role": "user",
        "content": [
            {"type": "image", "url": "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/p-blog/candy.JPG"},
            {"type": "text", "text": "What animal is on the candy?"}
        ]
    },
]
pipe(text=messages)
```

```
# pip install -U transformers accelerate
# Load model directly
from transformers import AutoProcessor, AutoModelForMultimodalLM

processor = AutoProcessor.from_pretrained("black-forest-labs/flux-3-image-klein-pup")
model = AutoModelForMultimodalLM.from_pretrained("black-forest-labs/flux-3-image-klein-pup", device_map="auto")
messages = [
    {
        "role": "user",
        "content": [
            {"type": "image", "url": "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/p-blog/candy.JPG"},
            {"type": "text", "text": "What animal is on the candy?"}
        ]
    },
]
inputs = processor.apply_chat_template(
	messages,
	add_generation_prompt=True,
	tokenize=True,
	return_dict=True,
	return_tensors="pt",
).to(model.device)

outputs = model.generate(**inputs, max_new_tokens=256)
print(processor.decode(outputs[0][inputs["input_ids"].shape[-1]:]))
```

  * Notebooks
  * [ Google Colab](https://huggingface.co/black-forest-labs/flux-3-image-klein-pup/colab)
  * [ Kaggle](https://huggingface.co/black-forest-labs/flux-3-image-klein-pup/kaggle)
  * Local Apps [Settings](https://huggingface.co/settings/local-apps "Set up your favorite local applications")
  * [ vLLM ](https://huggingface.co/black-forest-labs/flux-3-image-klein-pup?local-app=vllm)
How to use black-forest-labs/flux-3-image-klein-pup with vLLM:
##### Install from pip and serve model

```
# Install vLLM from pip:
pip install vllm
# Start the vLLM server:
vllm serve "black-forest-labs/flux-3-image-klein-pup"
# Call the server using curl (OpenAI-compatible API):
curl -X POST "http://localhost:8000/v1/chat/completions" \
	-H "Content-Type: application/json" \
	--data '{
		"model": "black-forest-labs/flux-3-image-klein-pup",
		"messages": [
			{
				"role": "user",
				"content": [
					{
						"type": "text",
						"text": "Describe this image in one sentence."
					},
					{
						"type": "image_url",
						"image_url": {
							"url": "https://cdn.britannica.com/61/93061-050-99147DCE/Statue-of-Liberty-Island-New-York-Bay.jpg"
						}
					}
				]
			}
		]
	}'
```

##### Use Docker

```
docker model run hf.co/black-forest-labs/flux-3-image-klein-pup
```

  * [ SGLang ](https://huggingface.co/black-forest-labs/flux-3-image-klein-pup?local-app=sglang)
How to use black-forest-labs/flux-3-image-klein-pup with SGLang:
##### Install from pip and serve model

```
# Install SGLang from pip:
pip install sglang
# Start the SGLang server:
python3 -m sglang.launch_server \
    --model-path "black-forest-labs/flux-3-image-klein-pup" \
    --host 0.0.0.0 \
    --port 30000
# Call the server using curl (OpenAI-compatible API):
curl -X POST "http://localhost:30000/v1/chat/completions" \
	-H "Content-Type: application/json" \
	--data '{
		"model": "black-forest-labs/flux-3-image-klein-pup",
		"messages": [
			{
				"role": "user",
				"content": [
					{
						"type": "text",
						"text": "Describe this image in one sentence."
					},
					{
						"type": "image_url",
						"image_url": {
							"url": "https://cdn.britannica.com/61/93061-050-99147DCE/Statue-of-Liberty-Island-New-York-Bay.jpg"
						}
					}
				]
			}
		]
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
        --model-path "black-forest-labs/flux-3-image-klein-pup" \
        --host 0.0.0.0 \
        --port 30000
# Call the server using curl (OpenAI-compatible API):
curl -X POST "http://localhost:30000/v1/chat/completions" \
	-H "Content-Type: application/json" \
	--data '{
		"model": "black-forest-labs/flux-3-image-klein-pup",
		"messages": [
			{
				"role": "user",
				"content": [
					{
						"type": "text",
						"text": "Describe this image in one sentence."
					},
					{
						"type": "image_url",
						"image_url": {
							"url": "https://cdn.britannica.com/61/93061-050-99147DCE/Statue-of-Liberty-Island-New-York-Bay.jpg"
						}
					}
				]
			}
		]
	}'
```

  * [ Docker Model Runner ](https://huggingface.co/black-forest-labs/flux-3-image-klein-pup?local-app=docker-model-runner)
How to use black-forest-labs/flux-3-image-klein-pup with Docker Model Runner:

```
docker model run hf.co/black-forest-labs/flux-3-image-klein-pup
```

  * [Browse Quantizations](https://huggingface.co/models?other=base_model:quantized:black-forest-labs/flux-3-image-klein-pup) to use this model in  llama.cpp,  Ollama,  LM Studio, or any compatible app.


  * [FLUX 3 Image Klein Prompt Upsampler](https://huggingface.co/black-forest-labs/flux-3-image-klein-pup#flux-3-image-klein-prompt-upsampler "FLUX 3 Image Klein Prompt Upsampler")
  * [Key Features](https://huggingface.co/black-forest-labs/flux-3-image-klein-pup#key-features "Key Features")
  * [Training](https://huggingface.co/black-forest-labs/flux-3-image-klein-pup#training "Training")
  * [Files](https://huggingface.co/black-forest-labs/flux-3-image-klein-pup#files "Files")
  * [Usage](https://huggingface.co/black-forest-labs/flux-3-image-klein-pup#usage "Usage")
    * [With the FLUX 3 inference code](https://huggingface.co/black-forest-labs/flux-3-image-klein-pup#with-the-flux-3-inference-code "With the FLUX 3 inference code")
    * [With Transformers](https://huggingface.co/black-forest-labs/flux-3-image-klein-pup#with-transformers "With Transformers")
  * [Limitations](https://huggingface.co/black-forest-labs/flux-3-image-klein-pup#limitations "Limitations")
  * [License](https://huggingface.co/black-forest-labs/flux-3-image-klein-pup#license "License")
  * [Trademarks & IP](https://huggingface.co/black-forest-labs/flux-3-image-klein-pup#trademarks--ip "Trademarks &amp; IP")
    * [Citation](https://huggingface.co/black-forest-labs/flux-3-image-klein-pup#citation "Citation")


#  [ ](https://huggingface.co/black-forest-labs/flux-3-image-klein-pup#flux-3-image-klein-prompt-upsampler) FLUX 3 Image Klein Prompt Upsampler 
FLUX 3 Image Klein Prompt Upsampler is a 9B vision-language model that expands a short image request into the detailed prompt [FLUX 3 Image Klein](https://huggingface.co/black-forest-labs/flux-3-image-klein-base) works best with. It takes the request, up to 10 reference images and an optional list of bounding boxes, and returns one prompt. It is a fine-tune of [Qwen3.5-9B](https://huggingface.co/Qwen/Qwen3.5-9B).
FLUX 3 Image Klein is not meant to run without a prompt upsampler in front of it, for text-to-image, editing and layout alike; a short prompt sent to the image model as typed gives generic output. This one is tuned for it, see [Training](https://huggingface.co/black-forest-labs/flux-3-image-klein-pup#training). Any other LLM can do the job with the system prompts in `system_prompts.json`. The inference code in [black-forest-labs/flux-3-image-klein](https://github.com/black-forest-labs/flux-3-image-klein) loads it by default. With Diffusers, run the [Transformers block](https://huggingface.co/black-forest-labs/flux-3-image-klein-pup#with-transformers) below and pass the caption to the pipeline as `prompt`. In ComfyUI, the text-to-image templates on [flux-3-image-klein-comfy](https://huggingface.co/black-forest-labs/flux-3-image-klein-comfy) have an `enable_prompt_upsampler` switch.
**Request**
> A man walking with his dog, afternoon sun
**Prompt**
> Full-color outdoor photograph, eye-level medium-wide shot in late afternoon sunlight, showing a man walking his dog along a neighborhood sidewalk. The low sun shines from the upper right, casting long shadows across the pavement and lighting the man's face and clothing with warm side light. Slightly left of center, a white man in his thirties with fair skin, short brown hair, and light stubble walks toward frame-left at an easy pace. He wears a faded olive overshirt over a plain grey T-shirt, dark blue jeans, and worn brown leather shoes. [...]
220 words in full, with the image it made, in [examples/base/man_dog.json](https://github.com/black-forest-labs/flux-3-image-klein/blob/main/examples/base/man_dog.json).
#  [ ](https://huggingface.co/black-forest-labs/flux-3-image-klein-pup#key-features) Key Features 
  1. One model for text-to-image, editing with reference images and layout with bounding boxes. The system prompt selects the mode.
  2. Prompts with everything the image model needs decided: medium and style, scene, lighting and camera, each subject with its colors, materials and position in the frame. Text to render stays verbatim, in quotes.
  3. For an edit it looks at the references and writes the instruction around what is in them: what changes, what stays, by appearance.
  4. Bounding boxes you pass are kept exactly, as a box table after the prompt; the prompt cites each box by id, so the image model places that element where the box says.
  5. Released under the Apache License 2.0.


#  [ ](https://huggingface.co/black-forest-labs/flux-3-image-klein-pup#training) Training 
A full fine-tune of Qwen3.5-9B with the vision tower frozen, in two stages: supervised training on pairs of short requests and their expanded prompts, then preference tuning on pairs of the model's own prompts, rendered with FLUX 3 Image Klein at the same seed and ranked on the resulting image.
#  [ ](https://huggingface.co/black-forest-labs/flux-3-image-klein-pup#files) Files   
| File  | Content  |  
| --- | --- |  
| `model.safetensors`  | the model, bfloat16, 18.8 GB  |  
| `system_prompts.json`  | the four system prompts: `t2i`, `i2i`, `t2i_bbox`, `i2i_bbox`  |  
|  `config.json`, `generation_config.json`, `tokenizer.json`, `tokenizer_config.json`, `chat_template.jinja`, `processor_config.json`, `preprocessor_config.json`  | Transformers configuration, tokenizer, chat template, image processor  |  
#  [ ](https://huggingface.co/black-forest-labs/flux-3-image-klein-pup#usage) Usage 
##  [ ](https://huggingface.co/black-forest-labs/flux-3-image-klein-pup#with-the-flux-3-inference-code) With the FLUX 3 inference code 

```
hf download black-forest-labs/flux-3-image-klein-pup --local-dir weights/pup
python scripts/cli.py "A man walking with his dog, afternoon sun" --out out.png

```

The upsampler is on by default; `--no-pup` sends the prompt as typed. To upsample without generating: `python -m flux3.pup --prompt "..." --out caption.txt`. Install, references and the box format: [black-forest-labs/flux-3-image-klein](https://github.com/black-forest-labs/flux-3-image-klein).
##  [ ](https://huggingface.co/black-forest-labs/flux-3-image-klein-pup#with-transformers) With Transformers 

```
import json

import torch
from huggingface_hub import hf_hub_download
from transformers import AutoProcessor, Qwen3_5ForConditionalGeneration

model_id = "black-forest-labs/flux-3-image-klein-pup"
processor = AutoProcessor.from_pretrained(model_id)
model = Qwen3_5ForConditionalGeneration.from_pretrained(model_id, dtype=torch.bfloat16, device_map="auto").eval()
prompts = json.load(open(hf_hub_download(model_id, "system_prompts.json")))

messages = [{"role": "system", "content": prompts["t2i"]},
            {"role": "user", "content": "A man walking with his dog, afternoon sun"}]
inputs = processor.apply_chat_template(messages, add_generation_prompt=True, tokenize=True, return_dict=True,
                                       return_tensors="pt", enable_thinking=False).to(model.device)
with torch.no_grad():
    out = model.generate(**inputs, max_new_tokens=3584, do_sample=False)
caption = processor.decode(out[0, inputs["input_ids"].shape[1]:], skip_special_tokens=True).strip()
print(caption)

```

For an edit, use `prompts["i2i"]` and a user message with the reference images first (`{"type": "image", "image": pil_image}` per reference) and then this text, three lines:

```
Reference images follow in order (the first image, the second image, ...).
User request: put a red bandana around the dog's neck
Output the caption.

```

Decoding: greedy, `top_p` 0.95, `top_k` 20, presence penalty 1.5 for text-to-image and 0 for edits. The `*_bbox` prompts take the boxes as JSON after the request and return the prompt with a box table; the exact scaffolds are `flux3/pup.py` and `flux3/bbox.py` in the inference code.
#  [ ](https://huggingface.co/black-forest-labs/flux-3-image-klein-pup#limitations) Limitations 
  * Output is English. The request can be in any language.
  * The prompts are written for FLUX 3 Image Klein; no other image model was part of training.
  * Reference images are resized before the model sees them (at most 1 MP for one reference, less for several), so small details in a reference can be described wrongly.
  * The model does not refuse requests. The inference code wraps it with optional prompt and image checks (`--safety`).


#  [ ](https://huggingface.co/black-forest-labs/flux-3-image-klein-pup#license) License 
This model is released under the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0). It is derived from [Qwen3.5-9B](https://huggingface.co/Qwen/Qwen3.5-9B) by the Qwen team at Alibaba Cloud, released under the Apache License 2.0.
#  [ ](https://huggingface.co/black-forest-labs/flux-3-image-klein-pup#trademarks--ip) Trademarks & IP 
This project may contain trademarks or logos for projects, products, or services. Use of Black Forest Labs and FLUX trademarks or logos in modified versions of this project must not cause confusion or imply sponsorship or endorsement. Any use of third-party trademarks, intellectual property or logos are subject to those third-party's policies.
##  [ ](https://huggingface.co/black-forest-labs/flux-3-image-klein-pup#citation) Citation 
If you use FLUX 3 Image in your work, please cite:

```
@misc{bfl2026flux3image,
  author       = {{Black Forest Labs}},
  title        = {{FLUX} 3 Image Klein},
  year         = {2026},
  url          = {https://bfl.ai/blog/flux-3-image-klein},
}

```


Downloads last month
    52,498
Safetensors[](https://huggingface.co/docs/safetensors)
Model size
9B params
Tensor type
BF16 
·
Chat template
Files info
Inference Providers [NEW](https://huggingface.co/docs/inference-providers)
[ Image-Text-to-Text ](https://huggingface.co/tasks/image-text-to-text "Learn more about image-text-to-text")
This model isn't deployed by any Inference Provider. [🙋 Ask for provider support](https://huggingface.co/spaces/huggingface/InferenceSupport/discussions/new?title=black-forest-labs/flux-3-image-klein-pup&description=React%20to%20this%20comment%20with%20an%20emoji%20to%20vote%20for%20%5Bblack-forest-labs%2Fflux-3-image-klein-pup%5D\(%2Fblack-forest-labs%2Fflux-3-image-klein-pup\)%20to%20be%20supported%20by%20Inference%20Providers.%0A%0A\(optional\)%20Which%20providers%20are%20you%20interested%20in%3F%20\(Novita%2C%20Hyperbolic%2C%20Together%E2%80%A6\)%0A)
##  Model tree for black-forest-labs/flux-3-image-klein-pup [](https://huggingface.co/docs/hub/model-cards#specifying-a-base-model)
Base model
[Qwen/Qwen3.5-9B-Base](https://huggingface.co/Qwen/Qwen3.5-9B-Base)
Finetuned
[Qwen/Qwen3.5-9B](https://huggingface.co/Qwen/Qwen3.5-9B)
Finetuned
([1193](https://huggingface.co/models?other=base_model:finetune:Qwen/Qwen3.5-9B))
this model
Finetunes
[5 models](https://huggingface.co/models?other=base_model:finetune:black-forest-labs/flux-3-image-klein-pup)
Quantizations
[15 models](https://huggingface.co/models?other=base_model:quantized:black-forest-labs/flux-3-image-klein-pup)
##  Spaces using black-forest-labs/flux-3-image-klein-pup 20
[ ![](https://cdn-avatars.huggingface.co/v1/production/uploads/633f7a8f4be90e06da248e0f/m5YoF33abJ09vcwFxt1Mj.png) black-forest-labs/flux-3-image-klein ](https://huggingface.co/spaces/black-forest-labs/flux-3-image-klein)[🖼 RioShiina/ImageGen ](https://huggingface.co/spaces/RioShiina/ImageGen)[🖼 Gramlin/ImageGennew ](https://huggingface.co/spaces/Gramlin/ImageGennew)[🎃 Diskfo/flux-3-image-klein ](https://huggingface.co/spaces/Diskfo/flux-3-image-klein)[🎃 prithivMLmods/flux-3-image-klein-loras-fast ](https://huggingface.co/spaces/prithivMLmods/flux-3-image-klein-loras-fast)[📈 BIGJUTT/model-pulse ](https://huggingface.co/spaces/BIGJUTT/model-pulse)[🖼 Or1290/LP12 ](https://huggingface.co/spaces/Or1290/LP12)[🌿 fffiloni/image-to-fragrance-v2 ](https://huggingface.co/spaces/fffiloni/image-to-fragrance-v2) + 15 Spaces + 12 Spaces
##  Collection including black-forest-labs/flux-3-image-klein-pup
#### [FLUX 3 Image Klein Collection 5 items • Updated 10 days ago • 49 ](https://huggingface.co/collections/black-forest-labs/flux-3-image-klein)
System theme
Company
[TOS](https://huggingface.co/terms-of-service) [Privacy](https://huggingface.co/privacy) [About](https://huggingface.co/huggingface) [Careers](https://apply.workable.com/huggingface/) [](https://huggingface.co/)
Website
[Models](https://huggingface.co/models) [Datasets](https://huggingface.co/datasets) [Spaces](https://huggingface.co/spaces) [Pricing](https://huggingface.co/pricing) [Docs](https://huggingface.co/docs)
Inference providers allow you to run inference using different serverless providers.

