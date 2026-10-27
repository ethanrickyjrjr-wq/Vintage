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
[ ![](https://cdn-avatars.huggingface.co/v1/production/uploads/6215ca5692c0ecfba9186921/hrRM50-6XcdWgg2AKpENG.jpeg) ](https://huggingface.co/Qwen)
[Qwen](https://huggingface.co/Qwen)
/
[Qwen3-VL-4B-Instruct](https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct)
Like 513
Follow
![](https://cdn-avatars.huggingface.co/v1/production/uploads/6215ca5692c0ecfba9186921/hrRM50-6XcdWgg2AKpENG.jpeg) Qwen 113k
[ Image-Text-to-Text ](https://huggingface.co/models?pipeline_tag=image-text-to-text)[ Transformers ](https://huggingface.co/models?library=transformers)[ Safetensors ](https://huggingface.co/models?library=safetensors)[ qwen3_vl ](https://huggingface.co/models?other=qwen3_vl)[ conversational ](https://huggingface.co/models?other=conversational)[ Eval Results ](https://huggingface.co/models?other=eval-results)
arxiv: 4 papers
License: apache-2.0
[ Model card ](https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct)[ Files Files and versions xet ](https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct/tree/main)[ Community 24 ](https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct/discussions)
Deploy
Copy to bucket
Use this model
### Instructions to use Qwen/Qwen3-VL-4B-Instruct with libraries, inference providers, notebooks, and local apps. Follow these links to get started.
  * Libraries
  * [ Transformers](https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct?library=transformers)
How to use Qwen/Qwen3-VL-4B-Instruct with Transformers:

```
# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("image-text-to-text", model="Qwen/Qwen3-VL-4B-Instruct")
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

processor = AutoProcessor.from_pretrained("Qwen/Qwen3-VL-4B-Instruct")
model = AutoModelForMultimodalLM.from_pretrained("Qwen/Qwen3-VL-4B-Instruct", device_map="auto")
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

  * Inference
  * Inference Providers
  * Notebooks
  * [ Google Colab](https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct/colab)
  * [ Kaggle](https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct/kaggle)
  * [ AMD Developer Cloud](https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct/amd)
  * Local Apps [Settings](https://huggingface.co/settings/local-apps "Set up your favorite local applications")
  * [ vLLM ](https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct?local-app=vllm)
How to use Qwen/Qwen3-VL-4B-Instruct with vLLM:
##### Install from pip and serve model

```
# Install vLLM from pip:
pip install vllm
# Start the vLLM server:
vllm serve "Qwen/Qwen3-VL-4B-Instruct"
# Call the server using curl (OpenAI-compatible API):
curl -X POST "http://localhost:8000/v1/chat/completions" \
	-H "Content-Type: application/json" \
	--data '{
		"model": "Qwen/Qwen3-VL-4B-Instruct",
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
docker model run hf.co/Qwen/Qwen3-VL-4B-Instruct
```

  * [ SGLang ](https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct?local-app=sglang)
How to use Qwen/Qwen3-VL-4B-Instruct with SGLang:
##### Install from pip and serve model

```
# Install SGLang from pip:
pip install sglang
# Start the SGLang server:
python3 -m sglang.launch_server \
    --model-path "Qwen/Qwen3-VL-4B-Instruct" \
    --host 0.0.0.0 \
    --port 30000
# Call the server using curl (OpenAI-compatible API):
curl -X POST "http://localhost:30000/v1/chat/completions" \
	-H "Content-Type: application/json" \
	--data '{
		"model": "Qwen/Qwen3-VL-4B-Instruct",
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
        --model-path "Qwen/Qwen3-VL-4B-Instruct" \
        --host 0.0.0.0 \
        --port 30000
# Call the server using curl (OpenAI-compatible API):
curl -X POST "http://localhost:30000/v1/chat/completions" \
	-H "Content-Type: application/json" \
	--data '{
		"model": "Qwen/Qwen3-VL-4B-Instruct",
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

  * [ Docker Model Runner ](https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct?local-app=docker-model-runner)
How to use Qwen/Qwen3-VL-4B-Instruct with Docker Model Runner:

```
docker model run hf.co/Qwen/Qwen3-VL-4B-Instruct
```

  * [Browse Quantizations](https://huggingface.co/models?other=base_model:quantized:Qwen/Qwen3-VL-4B-Instruct) to use this model in  llama.cpp,  Ollama,  LM Studio, or any compatible app.


  * [Qwen3-VL-4B-Instruct](https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct#qwen3-vl-4b-instruct "Qwen3-VL-4B-Instruct")
    * [Model Performance](https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct#model-performance "Model Performance")
    * [Quickstart](https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct#quickstart "Quickstart")
      * [Using 🤗 Transformers to Chat](https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct#using-%F0%9F%A4%97-transformers-to-chat "Using 🤗 Transformers to Chat")
      * [Generation Hyperparameters](https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct#generation-hyperparameters "Generation Hyperparameters")
    * [Citation](https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct#citation "Citation")


[ ![Chat](https://img.shields.io/badge/%F0%9F%92%9C%EF%B8%8F%20Qwen%20Chat%20-536af5) ](https://chat.qwenlm.ai/)
#  [ ](https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct#qwen3-vl-4b-instruct) Qwen3-VL-4B-Instruct 
Meet Qwen3-VL — the most powerful vision-language model in the Qwen series to date.
This generation delivers comprehensive upgrades across the board: superior text understanding & generation, deeper visual perception & reasoning, extended context length, enhanced spatial and video dynamics comprehension, and stronger agent interaction capabilities.
Available in Dense and MoE architectures that scale from edge to cloud, with Instruct and reasoning‑enhanced Thinking editions for flexible, on‑demand deployment.
####  [ ](https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct#key-enhancements) Key Enhancements: 
  * **Visual Agent** : Operates PC/mobile GUIs—recognizes elements, understands functions, invokes tools, completes tasks.
  * **Visual Coding Boost** : Generates Draw.io/HTML/CSS/JS from images/videos.
  * **Advanced Spatial Perception** : Judges object positions, viewpoints, and occlusions; provides stronger 2D grounding and enables 3D grounding for spatial reasoning and embodied AI.
  * **Long Context & Video Understanding**: Native 256K context, expandable to 1M; handles books and hours-long video with full recall and second-level indexing.
  * **Enhanced Multimodal Reasoning** : Excels in STEM/Math—causal analysis and logical, evidence-based answers.
  * **Upgraded Visual Recognition** : Broader, higher-quality pretraining is able to “recognize everything”—celebrities, anime, products, landmarks, flora/fauna, etc.
  * **Expanded OCR** : Supports 32 languages (up from 19); robust in low light, blur, and tilt; better with rare/ancient characters and jargon; improved long-document structure parsing.
  * **Text Understanding on par with pure LLMs** : Seamless text–vision fusion for lossless, unified comprehension.


####  [ ](https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct#model-architecture-updates) Model Architecture Updates: 
![](https://qianwen-res.oss-accelerate.aliyuncs.com/Qwen3-VL/qwen3vl_arc.jpg)
  1. **Interleaved-MRoPE** : Full‑frequency allocation over time, width, and height via robust positional embeddings, enhancing long‑horizon video reasoning.
  2. **DeepStack** : Fuses multi‑level ViT features to capture fine‑grained details and sharpen image–text alignment.
  3. **Text–Timestamp Alignment:** Moves beyond T‑RoPE to precise, timestamp‑grounded event localization for stronger video temporal modeling.


This is the weight repository for Qwen3-VL-4B-Instruct.
* * *
##  [ ](https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct#model-performance) Model Performance 
**Multimodal performance**
[![](https://qianwen-res.oss-accelerate.aliyuncs.com/Qwen3-VL/qwen3vl_4b_8b_vl_instruct.jpg)](https://qianwen-res.oss-accelerate.aliyuncs.com/Qwen3-VL/qwen3vl_4b_8b_vl_instruct.jpg)
**Pure text performance** [![](https://qianwen-res.oss-accelerate.aliyuncs.com/Qwen3-VL/qwen3vl_4b_8b_text_instruct.jpg)](https://qianwen-res.oss-accelerate.aliyuncs.com/Qwen3-VL/qwen3vl_4b_8b_text_instruct.jpg)
##  [ ](https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct#quickstart) Quickstart 
Below, we provide simple examples to show how to use Qwen3-VL with 🤖 ModelScope and 🤗 Transformers.
The code of Qwen3-VL has been in the latest Hugging Face transformers and we advise you to build from source with command:

```
pip install git+https://github.com/huggingface/transformers
# pip install transformers==4.57.0 # currently, V4.57.0 is not released

```

###  [ ](https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct#using-%F0%9F%A4%97-transformers-to-chat) Using 🤗 Transformers to Chat 
Here we show a code snippet to show how to use the chat model with `transformers`:

```
from transformers import Qwen3VLForConditionalGeneration, AutoProcessor

# default: Load the model on the available device(s)
model = Qwen3VLForConditionalGeneration.from_pretrained(
    "Qwen/Qwen3-VL-4B-Instruct", dtype="auto", device_map="auto"
)

# We recommend enabling flash_attention_2 for better acceleration and memory saving, especially in multi-image and video scenarios.
# model = Qwen3VLForConditionalGeneration.from_pretrained(
#     "Qwen/Qwen3-VL-4B-Instruct",
#     dtype=torch.bfloat16,
#     attn_implementation="flash_attention_2",
#     device_map="auto",
# )

processor = AutoProcessor.from_pretrained("Qwen/Qwen3-VL-4B-Instruct")

messages = [
    {
        "role": "user",
        "content": [
            {
                "type": "image",
                "image": "https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-VL/assets/demo.jpeg",
            },
            {"type": "text", "text": "Describe this image."},
        ],
    }
]

# Preparation for inference
inputs = processor.apply_chat_template(
    messages,
    tokenize=True,
    add_generation_prompt=True,
    return_dict=True,
    return_tensors="pt"
)
inputs = inputs.to(model.device)

# Inference: Generation of the output
generated_ids = model.generate(**inputs, max_new_tokens=128)
generated_ids_trimmed = [
    out_ids[len(in_ids) :] for in_ids, out_ids in zip(inputs.input_ids, generated_ids)
]
output_text = processor.batch_decode(
    generated_ids_trimmed, skip_special_tokens=True, clean_up_tokenization_spaces=False
)
print(output_text)

```

###  [ ](https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct#generation-hyperparameters) Generation Hyperparameters 
####  [ ](https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct#vl) VL 

```
export greedy='false'
export top_p=0.8
export top_k=20
export temperature=0.7
export repetition_penalty=1.0
export presence_penalty=1.5
export out_seq_length=16384

```

####  [ ](https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct#text) Text 

```
export greedy='false'
export top_p=1.0
export top_k=40
export repetition_penalty=1.0
export presence_penalty=2.0
export temperature=1.0
export out_seq_length=32768

```

##  [ ](https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct#citation) Citation 
If you find our work helpful, feel free to give us a cite.

```
@misc{qwen3technicalreport,
      title={Qwen3 Technical Report}, 
      author={Qwen Team},
      year={2025},
      eprint={2505.09388},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2505.09388}, 
}

@article{Qwen2.5-VL,
  title={Qwen2.5-VL Technical Report},
  author={Bai, Shuai and Chen, Keqin and Liu, Xuejing and Wang, Jialin and Ge, Wenbin and Song, Sibo and Dang, Kai and Wang, Peng and Wang, Shijie and Tang, Jun and Zhong, Humen and Zhu, Yuanzhi and Yang, Mingkun and Li, Zhaohai and Wan, Jianqiang and Wang, Pengfei and Ding, Wei and Fu, Zheren and Xu, Yiheng and Ye, Jiabo and Zhang, Xi and Xie, Tianbao and Cheng, Zesen and Zhang, Hang and Yang, Zhibo and Xu, Haiyang and Lin, Junyang},
  journal={arXiv preprint arXiv:2502.13923},
  year={2025}
}

@article{Qwen2VL,
  title={Qwen2-VL: Enhancing Vision-Language Model's Perception of the World at Any Resolution},
  author={Wang, Peng and Bai, Shuai and Tan, Sinan and Wang, Shijie and Fan, Zhihao and Bai, Jinze and Chen, Keqin and Liu, Xuejing and Wang, Jialin and Ge, Wenbin and Fan, Yang and Dang, Kai and Du, Mengfei and Ren, Xuancheng and Men, Rui and Liu, Dayiheng and Zhou, Chang and Zhou, Jingren and Lin, Junyang},
  journal={arXiv preprint arXiv:2409.12191},
  year={2024}
}

@article{Qwen-VL,
  title={Qwen-VL: A Versatile Vision-Language Model for Understanding, Localization, Text Reading, and Beyond},
  author={Bai, Jinze and Bai, Shuai and Yang, Shusheng and Wang, Shijie and Tan, Sinan and Wang, Peng and Lin, Junyang and Zhou, Chang and Zhou, Jingren},
  journal={arXiv preprint arXiv:2308.12966},
  year={2023}
}

```


Downloads last month
    4,010,838
Safetensors[](https://huggingface.co/docs/safetensors)
Model size
4B params
Tensor type
BF16 
·
Chat template
Files info
Inference Providers [NEW](https://huggingface.co/docs/inference-providers)
Featherless AI
[ Image-Text-to-Text ](https://huggingface.co/tasks/image-text-to-text "Learn more about image-text-to-text")
Examples
Input a message to start chatting with **Qwen/Qwen3-VL-4B-Instruct**.
Send
View Code Snippets
[ Compare providers](https://huggingface.co/inference/models?model=Qwen%2FQwen3-VL-4B-Instruct)
##  Model tree for Qwen/Qwen3-VL-4B-Instruct [](https://huggingface.co/docs/hub/model-cards#specifying-a-base-model)
Adapters
[230 models](https://huggingface.co/models?other=base_model:adapter:Qwen/Qwen3-VL-4B-Instruct)
Finetunes
[507 models](https://huggingface.co/models?other=base_model:finetune:Qwen/Qwen3-VL-4B-Instruct)
Merges
[2 models](https://huggingface.co/models?other=base_model:merge:Qwen/Qwen3-VL-4B-Instruct)
Quantizations
[](https://huggingface.co/models?apps=llama.cpp&other=base_model:quantized:Qwen/Qwen3-VL-4B-Instruct "Use with llama.cpp")[](https://huggingface.co/models?apps=llama-app&other=base_model:quantized:Qwen/Qwen3-VL-4B-Instruct "Use with Llama")[](https://huggingface.co/models?apps=lmstudio&other=base_model:quantized:Qwen/Qwen3-VL-4B-Instruct "Use with LM Studio")[](https://huggingface.co/models?apps=jan&other=base_model:quantized:Qwen/Qwen3-VL-4B-Instruct "Use with Jan")
[115 models](https://huggingface.co/models?other=base_model:quantized:Qwen/Qwen3-VL-4B-Instruct)
##  Spaces using Qwen/Qwen3-VL-4B-Instruct 89
[🟩 embedl/hfviewer ](https://huggingface.co/spaces/embedl/hfviewer)[👁️ speridlabs/iris-3b ](https://huggingface.co/spaces/speridlabs/iris-3b)[🤖 nvidia/Cosmos3-Action-Viewer ](https://huggingface.co/spaces/nvidia/Cosmos3-Action-Viewer)[⚡ fastgpu/vram-and-gpu-cost-calculator ](https://huggingface.co/spaces/fastgpu/vram-and-gpu-cost-calculator)[🐨 akhaliq/Qwen3-VL-4B-Instruct ](https://huggingface.co/spaces/akhaliq/Qwen3-VL-4B-Instruct)[🛰️ hugging-apps/unispace-gen-edit ](https://huggingface.co/spaces/hugging-apps/unispace-gen-edit)[🎯 hugging-apps/locus-2b-grounding ](https://huggingface.co/spaces/hugging-apps/locus-2b-grounding)[🔥 prithivMLmods/Qwen3-VL-Outpost ](https://huggingface.co/spaces/prithivMLmods/Qwen3-VL-Outpost) + 84 Spaces + 81 Spaces
##  Collection including Qwen/Qwen3-VL-4B-Instruct
#### [Qwen3-VL Collection 37 items • Updated Dec 31, 2025 • 794 ](https://huggingface.co/collections/Qwen/qwen3-vl)
##  Papers for Qwen/Qwen3-VL-4B-Instruct
#### [Qwen3 Technical Report Paper • 2505.09388 • Published May 14, 2025 • 353 ](https://huggingface.co/papers/2505.09388)#### [Qwen2.5-VL Technical Report Paper • 2502.13923 • Published Feb 19, 2025 • 219 ](https://huggingface.co/papers/2502.13923)#### [Qwen2-VL: Enhancing Vision-Language Model's Perception of the World at Any Resolution Paper • 2409.12191 • Published Sep 18, 2024 • 82 ](https://huggingface.co/papers/2409.12191)#### [Qwen-VL: A Frontier Large Vision-Language Model with Versatile Abilities Paper • 2308.12966 • Published Aug 24, 2023 • 13 ](https://huggingface.co/papers/2308.12966)
##  Evaluation results [](https://huggingface.co/docs/hub/eval-results)
  * [VCLab-PolyU/OmniCompass](https://huggingface.co/datasets/VCLab-PolyU/OmniCompass) · OmniCompass VL [View evaluation results ](https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct/discussions/26) [ ![](https://cdn-avatars.huggingface.co/v1/production/uploads/69db8a673114e93a4dbdec28/eJg3LOMGXpPKPa9lrzHtE.jpeg) source](https://omnicompass.netlify.app/#leaderboard) [leaderboard ](https://huggingface.co/datasets/VCLab-PolyU/OmniCompass?eval_result=Qwen/Qwen3-VL-4B-Instruct&leaderboard_task_id=OmniCompass-VL)
[](https://huggingface.co/datasets/VCLab-PolyU/OmniCompass?eval_result=Qwen%2FQwen3-VL-4B-Instruct&leaderboard_task_id=OmniCompass-VL&leaderboard_max_params=6B) 23.3 *
  * [tiiuae/PBench](https://huggingface.co/datasets/tiiuae/PBench) · Average [View evaluation results ](https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct/discussions/22) [leaderboard ](https://huggingface.co/datasets/tiiuae/PBench?eval_result=Qwen/Qwen3-VL-4B-Instruct&leaderboard_task_id=average)
[](https://huggingface.co/datasets/tiiuae/PBench?eval_result=Qwen%2FQwen3-VL-4B-Instruct&leaderboard_task_id=average) 49.2 *


System theme
Company
[TOS](https://huggingface.co/terms-of-service) [Privacy](https://huggingface.co/privacy) [About](https://huggingface.co/huggingface) [Careers](https://apply.workable.com/huggingface/) [](https://huggingface.co/)
Website
[Models](https://huggingface.co/models) [Datasets](https://huggingface.co/datasets) [Spaces](https://huggingface.co/spaces) [Pricing](https://huggingface.co/pricing) [Docs](https://huggingface.co/docs)
View evaluation results shared by the community
Source: OmniCompass official results by VCLab-PolyU
Ranked #1 in the < 6B size range
OmniCompass-VL; Overall CS on a 0-100 scale, higher is better. 32 video frames; paired Text and Text+Image; TG, SG and QA. Imported from the benchmark authors' published results, rounded to one decimal. Evaluation settings and model-specific limits follow the cited source. This submission does not claim HF verified status.
View evaluation results shared by the community
Ranked #3 overall
Detection-only model combined with SAM2 to convert boxes to segmentation masks.
Inference providers allow you to run inference using different serverless providers.

