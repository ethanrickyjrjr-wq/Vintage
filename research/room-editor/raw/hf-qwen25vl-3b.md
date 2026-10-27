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
[Qwen2.5-VL-3B-Instruct](https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct)
Like 739
Follow
![](https://cdn-avatars.huggingface.co/v1/production/uploads/6215ca5692c0ecfba9186921/hrRM50-6XcdWgg2AKpENG.jpeg) Qwen 113k
[ Image-Text-to-Text ](https://huggingface.co/models?pipeline_tag=image-text-to-text)[ Transformers ](https://huggingface.co/models?library=transformers)[ Safetensors ](https://huggingface.co/models?library=safetensors)[ English ](https://huggingface.co/models?language=en)[ qwen2_5_vl ](https://huggingface.co/models?other=qwen2_5_vl)[ multimodal ](https://huggingface.co/models?other=multimodal)[ conversational ](https://huggingface.co/models?other=conversational)[ Eval Results ](https://huggingface.co/models?other=eval-results)[ text-generation-inference ](https://huggingface.co/models?other=text-generation-inference)
arxiv: 2309.00071
arxiv: 2409.12191
arxiv: 2308.12966
[ Model card ](https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct)[ Files Files and versions xet ](https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct/tree/main)[ Community 53 ](https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct/discussions)
Deploy
Copy to bucket
Use this model
### Instructions to use Qwen/Qwen2.5-VL-3B-Instruct with libraries, inference providers, notebooks, and local apps. Follow these links to get started.
  * Libraries
  * [ Transformers](https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct?library=transformers)
How to use Qwen/Qwen2.5-VL-3B-Instruct with Transformers:

```
# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("image-text-to-text", model="Qwen/Qwen2.5-VL-3B-Instruct")
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

processor = AutoProcessor.from_pretrained("Qwen/Qwen2.5-VL-3B-Instruct")
model = AutoModelForMultimodalLM.from_pretrained("Qwen/Qwen2.5-VL-3B-Instruct", device_map="auto")
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
  * [ Google Colab](https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct/colab)
  * [ Kaggle](https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct/kaggle)
  * Local Apps [Settings](https://huggingface.co/settings/local-apps "Set up your favorite local applications")
  * [ vLLM ](https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct?local-app=vllm)
How to use Qwen/Qwen2.5-VL-3B-Instruct with vLLM:
##### Install from pip and serve model

```
# Install vLLM from pip:
pip install vllm
# Start the vLLM server:
vllm serve "Qwen/Qwen2.5-VL-3B-Instruct"
# Call the server using curl (OpenAI-compatible API):
curl -X POST "http://localhost:8000/v1/chat/completions" \
	-H "Content-Type: application/json" \
	--data '{
		"model": "Qwen/Qwen2.5-VL-3B-Instruct",
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
docker model run hf.co/Qwen/Qwen2.5-VL-3B-Instruct
```

  * [ SGLang ](https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct?local-app=sglang)
How to use Qwen/Qwen2.5-VL-3B-Instruct with SGLang:
##### Install from pip and serve model

```
# Install SGLang from pip:
pip install sglang
# Start the SGLang server:
python3 -m sglang.launch_server \
    --model-path "Qwen/Qwen2.5-VL-3B-Instruct" \
    --host 0.0.0.0 \
    --port 30000
# Call the server using curl (OpenAI-compatible API):
curl -X POST "http://localhost:30000/v1/chat/completions" \
	-H "Content-Type: application/json" \
	--data '{
		"model": "Qwen/Qwen2.5-VL-3B-Instruct",
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
        --model-path "Qwen/Qwen2.5-VL-3B-Instruct" \
        --host 0.0.0.0 \
        --port 30000
# Call the server using curl (OpenAI-compatible API):
curl -X POST "http://localhost:30000/v1/chat/completions" \
	-H "Content-Type: application/json" \
	--data '{
		"model": "Qwen/Qwen2.5-VL-3B-Instruct",
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

  * [ Docker Model Runner ](https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct?local-app=docker-model-runner)
How to use Qwen/Qwen2.5-VL-3B-Instruct with Docker Model Runner:

```
docker model run hf.co/Qwen/Qwen2.5-VL-3B-Instruct
```

  * [Browse Quantizations](https://huggingface.co/models?other=base_model:quantized:Qwen/Qwen2.5-VL-3B-Instruct) to use this model in  llama.cpp,  Ollama,  LM Studio, or any compatible app.


  * [Qwen2.5-VL-3B-Instruct](https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct#qwen25-vl-3b-instruct "Qwen2.5-VL-3B-Instruct")
    * [Introduction](https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct#introduction "Introduction")
    * [Evaluation](https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct#evaluation "Evaluation")
      * [Image benchmark](https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct#image-benchmark "Image benchmark")
      * [Video benchmark](https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct#video-benchmark "Video benchmark")
      * [Agent benchmark](https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct#agent-benchmark "Agent benchmark")
    * [Requirements](https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct#requirements "Requirements")
    * [Quickstart](https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct#quickstart "Quickstart")
      * [Using 🤗 Transformers to Chat](https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct#using-%F0%9F%A4%97--transformers-to-chat "Using 🤗  Transformers to Chat")
      * [🤖 ModelScope](https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct#%F0%9F%A4%96-modelscope "🤖 ModelScope")
      * [More Usage Tips](https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct#more-usage-tips "More Usage Tips")
      * [Processing Long Texts](https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct#processing-long-texts "Processing Long Texts")
    * [Citation](https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct#citation "Citation")


#  [ ](https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct#qwen25-vl-3b-instruct) Qwen2.5-VL-3B-Instruct 
[ ![Chat](https://img.shields.io/badge/%F0%9F%92%9C%EF%B8%8F%20Qwen%20Chat%20-536af5) ](https://chat.qwenlm.ai/)
##  [ ](https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct#introduction) Introduction 
In the past five months since Qwen2-VL’s release, numerous developers have built new models on the Qwen2-VL vision-language models, providing us with valuable feedback. During this period, we focused on building more useful vision-language models. Today, we are excited to introduce the latest addition to the Qwen family: Qwen2.5-VL.
####  [ ](https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct#key-enhancements) Key Enhancements: 
  * **Understand things visually** : Qwen2.5-VL is not only proficient in recognizing common objects such as flowers, birds, fish, and insects, but it is highly capable of analyzing texts, charts, icons, graphics, and layouts within images.
  * **Being agentic** : Qwen2.5-VL directly plays as a visual agent that can reason and dynamically direct tools, which is capable of computer use and phone use.
  * **Understanding long videos and capturing events** : Qwen2.5-VL can comprehend videos of over 1 hour, and this time it has a new ability of cpaturing event by pinpointing the relevant video segments.
  * **Capable of visual localization in different formats** : Qwen2.5-VL can accurately localize objects in an image by generating bounding boxes or points, and it can provide stable JSON outputs for coordinates and attributes.
  * **Generating structured outputs** : for data like scans of invoices, forms, tables, etc. Qwen2.5-VL supports structured outputs of their contents, benefiting usages in finance, commerce, etc.


####  [ ](https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct#model-architecture-updates) Model Architecture Updates: 
  * **Dynamic Resolution and Frame Rate Training for Video Understanding** :


We extend dynamic resolution to the temporal dimension by adopting dynamic FPS sampling, enabling the model to comprehend videos at various sampling rates. Accordingly, we update mRoPE in the time dimension with IDs and absolute time alignment, enabling the model to learn temporal sequence and speed, and ultimately acquire the ability to pinpoint specific moments.
![](https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen2.5-VL/qwen2.5vl_arc.jpeg)
  * **Streamlined and Efficient Vision Encoder**


We enhance both training and inference speeds by strategically implementing window attention into the ViT. The ViT architecture is further optimized with SwiGLU and RMSNorm, aligning it with the structure of the Qwen2.5 LLM.
We have three models with 3, 7 and 72 billion parameters. This repo contains the instruction-tuned 3B Qwen2.5-VL model. For more information, visit our [Blog](https://qwenlm.github.io/blog/qwen2.5-vl/) and [GitHub](https://github.com/QwenLM/Qwen2.5-VL).
##  [ ](https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct#evaluation) Evaluation 
###  [ ](https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct#image-benchmark) Image benchmark   
| Benchmark  | InternVL2.5-4B  | Qwen2-VL-7B  | Qwen2.5-VL-3B  |  
| --- | --- | --- | --- |  
| MMMUval  | 52.3  | 54.1  | 53.1  |  
| MMMU-Proval  | **32.7**  | 30.5  | 31.6  |  
| AI2Dtest  | 81.4  | **83.0**  | 81.5  |  
| DocVQAtest  | 91.6  | 94.5  | **93.9**  |  
| InfoVQAtest  | 72.1  | 76.5  | **77.1**  |  
| TextVQAval  | 76.8  | **84.3**  | 79.3  |  
| MMBench-V1.1test  | 79.3  | **80.7**  | 77.6  |  
| MMStar  | 58.3  | **60.7**  | 55.9  |  
| MathVistatestmini  | 60.5  | 58.2  | **62.3**  |  
| MathVisionfull  | 20.9  | 16.3  | **21.2**  |  
###  [ ](https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct#video-benchmark) Video benchmark   
| Benchmark  | InternVL2.5-4B  | Qwen2-VL-7B  | Qwen2.5-VL-3B  |  
| --- | --- | --- | --- |  
| MVBench  | 71.6  | 67.0  | 67.0  |  
| VideoMME  | 63.6/62.3  | 69.0/63.3  | 67.6/61.5  |  
| MLVU  | 48.3  | -  | 68.2  |  
| LVBench  | -  | -  | 43.3  |  
| MMBench-Video  | 1.73  | 1.44  | 1.63  |  
| EgoSchema  | -  | -  | 64.8  |  
| PerceptionTest  | -  | -  | 66.9  |  
| TempCompass  | -  | -  | 64.4  |  
| LongVideoBench  | 55.2  | 55.6  | 54.2  |  
| CharadesSTA/mIoU  | -  | -  | 38.8  |  
###  [ ](https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct#agent-benchmark) Agent benchmark   
| Benchmarks  | Qwen2.5-VL-3B  |  
| --- | --- |  
| ScreenSpot  | 55.5  |  
| ScreenSpot Pro  | 23.9  |  
| AITZ_EM  | 76.9  |  
| Android Control High_EM  | 63.7  |  
| Android Control Low_EM  | 22.2  |  
| AndroidWorld_SR  | 90.8  |  
| MobileMiniWob++_SR  | 67.9  |  
##  [ ](https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct#requirements) Requirements 
The code of Qwen2.5-VL has been in the latest Hugging face transformers and we advise you to build from source with command:

```
pip install git+https://github.com/huggingface/transformers accelerate

```

or you might encounter the following error:

```
KeyError: 'qwen2_5_vl'

```

##  [ ](https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct#quickstart) Quickstart 
Below, we provide simple examples to show how to use Qwen2.5-VL with 🤖 ModelScope and 🤗 Transformers.
The code of Qwen2.5-VL has been in the latest Hugging face transformers and we advise you to build from source with command:

```
pip install git+https://github.com/huggingface/transformers accelerate

```

or you might encounter the following error:

```
KeyError: 'qwen2_5_vl'

```

We offer a toolkit to help you handle various types of visual input more conveniently, as if you were using an API. This includes base64, URLs, and interleaved images and videos. You can install it using the following command:

```
# It's highly recommanded to use `[decord]` feature for faster video loading.
pip install qwen-vl-utils[decord]==0.0.8

```

If you are not using Linux, you might not be able to install `decord` from PyPI. In that case, you can use `pip install qwen-vl-utils` which will fall back to using torchvision for video processing. However, you can still [install decord from source](https://github.com/dmlc/decord?tab=readme-ov-file#install-from-source) to get decord used when loading video.
###  [ ](https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct#using-%F0%9F%A4%97--transformers-to-chat) Using 🤗 Transformers to Chat 
Here we show a code snippet to show you how to use the chat model with `transformers` and `qwen_vl_utils`:

```
from transformers import Qwen2_5_VLForConditionalGeneration, AutoTokenizer, AutoProcessor
from qwen_vl_utils import process_vision_info

# default: Load the model on the available device(s)
model = Qwen2_5_VLForConditionalGeneration.from_pretrained(
    "Qwen/Qwen2.5-VL-3B-Instruct", torch_dtype="auto", device_map="auto"
)

# We recommend enabling flash_attention_2 for better acceleration and memory saving, especially in multi-image and video scenarios.
# model = Qwen2_5_VLForConditionalGeneration.from_pretrained(
#     "Qwen/Qwen2.5-VL-3B-Instruct",
#     torch_dtype=torch.bfloat16,
#     attn_implementation="flash_attention_2",
#     device_map="auto",
# )

# default processer
processor = AutoProcessor.from_pretrained("Qwen/Qwen2.5-VL-3B-Instruct")

# The default range for the number of visual tokens per image in the model is 4-16384.
# You can set min_pixels and max_pixels according to your needs, such as a token range of 256-1280, to balance performance and cost.
# min_pixels = 256*28*28
# max_pixels = 1280*28*28
# processor = AutoProcessor.from_pretrained("Qwen/Qwen2.5-VL-3B-Instruct", min_pixels=min_pixels, max_pixels=max_pixels)

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
text = processor.apply_chat_template(
    messages, tokenize=False, add_generation_prompt=True
)
image_inputs, video_inputs = process_vision_info(messages)
inputs = processor(
    text=[text],
    images=image_inputs,
    videos=video_inputs,
    padding=True,
    return_tensors="pt",
)
inputs = inputs.to("cuda")

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

Multi image inference

```
# Messages containing multiple images and a text query
messages = [
    {
        "role": "user",
        "content": [
            {"type": "image", "image": "file:///path/to/image1.jpg"},
            {"type": "image", "image": "file:///path/to/image2.jpg"},
            {"type": "text", "text": "Identify the similarities between these images."},
        ],
    }
]

# Preparation for inference
text = processor.apply_chat_template(
    messages, tokenize=False, add_generation_prompt=True
)
image_inputs, video_inputs = process_vision_info(messages)
inputs = processor(
    text=[text],
    images=image_inputs,
    videos=video_inputs,
    padding=True,
    return_tensors="pt",
)
inputs = inputs.to("cuda")

# Inference
generated_ids = model.generate(**inputs, max_new_tokens=128)
generated_ids_trimmed = [
    out_ids[len(in_ids) :] for in_ids, out_ids in zip(inputs.input_ids, generated_ids)
]
output_text = processor.batch_decode(
    generated_ids_trimmed, skip_special_tokens=True, clean_up_tokenization_spaces=False
)
print(output_text)

```

Video inference

```
# Messages containing a images list as a video and a text query
messages = [
    {
        "role": "user",
        "content": [
            {
                "type": "video",
                "video": [
                    "file:///path/to/frame1.jpg",
                    "file:///path/to/frame2.jpg",
                    "file:///path/to/frame3.jpg",
                    "file:///path/to/frame4.jpg",
                ],
            },
            {"type": "text", "text": "Describe this video."},
        ],
    }
]

# Messages containing a local video path and a text query
messages = [
    {
        "role": "user",
        "content": [
            {
                "type": "video",
                "video": "file:///path/to/video1.mp4",
                "max_pixels": 360 * 420,
                "fps": 1.0,
            },
            {"type": "text", "text": "Describe this video."},
        ],
    }
]

# Messages containing a video url and a text query
messages = [
    {
        "role": "user",
        "content": [
            {
                "type": "video",
                "video": "https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen2-VL/space_woaudio.mp4",
            },
            {"type": "text", "text": "Describe this video."},
        ],
    }
]

#In Qwen 2.5 VL, frame rate information is also input into the model to align with absolute time.
# Preparation for inference
text = processor.apply_chat_template(
    messages, tokenize=False, add_generation_prompt=True
)
image_inputs, video_inputs, video_kwargs = process_vision_info(messages, return_video_kwargs=True)
inputs = processor(
    text=[text],
    images=image_inputs,
    videos=video_inputs,
    fps=fps,
    padding=True,
    return_tensors="pt",
    **video_kwargs,
)
inputs = inputs.to("cuda")

# Inference
generated_ids = model.generate(**inputs, max_new_tokens=128)
generated_ids_trimmed = [
    out_ids[len(in_ids) :] for in_ids, out_ids in zip(inputs.input_ids, generated_ids)
]
output_text = processor.batch_decode(
    generated_ids_trimmed, skip_special_tokens=True, clean_up_tokenization_spaces=False
)
print(output_text)

```

Video URL compatibility largely depends on the third-party library version. The details are in the table below. change the backend by `FORCE_QWENVL_VIDEO_READER=torchvision` or `FORCE_QWENVL_VIDEO_READER=decord` if you prefer not to use the default one.  
| Backend  | HTTP  | HTTPS  |  
| --- | --- | --- |  
| torchvision >= 0.19.0  | ✅  | ✅  |  
| torchvision < 0.19.0  | ❌  | ❌  |  
| decord  | ✅  | ❌  |  
Batch inference

```
# Sample messages for batch inference
messages1 = [
    {
        "role": "user",
        "content": [
            {"type": "image", "image": "file:///path/to/image1.jpg"},
            {"type": "image", "image": "file:///path/to/image2.jpg"},
            {"type": "text", "text": "What are the common elements in these pictures?"},
        ],
    }
]
messages2 = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who are you?"},
]
# Combine messages for batch processing
messages = [messages1, messages2]

# Preparation for batch inference
texts = [
    processor.apply_chat_template(msg, tokenize=False, add_generation_prompt=True)
    for msg in messages
]
image_inputs, video_inputs = process_vision_info(messages)
inputs = processor(
    text=texts,
    images=image_inputs,
    videos=video_inputs,
    padding=True,
    return_tensors="pt",
)
inputs = inputs.to("cuda")

# Batch Inference
generated_ids = model.generate(**inputs, max_new_tokens=128)
generated_ids_trimmed = [
    out_ids[len(in_ids) :] for in_ids, out_ids in zip(inputs.input_ids, generated_ids)
]
output_texts = processor.batch_decode(
    generated_ids_trimmed, skip_special_tokens=True, clean_up_tokenization_spaces=False
)
print(output_texts)

```

###  [ ](https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct#%F0%9F%A4%96-modelscope) 🤖 ModelScope 
We strongly advise users especially those in mainland China to use ModelScope. `snapshot_download` can help you solve issues concerning downloading checkpoints.
###  [ ](https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct#more-usage-tips) More Usage Tips 
For input images, we support local files, base64, and URLs. For videos, we currently only support local files.

```
# You can directly insert a local file path, a URL, or a base64-encoded image into the position where you want in the text.
## Local file path
messages = [
    {
        "role": "user",
        "content": [
            {"type": "image", "image": "file:///path/to/your/image.jpg"},
            {"type": "text", "text": "Describe this image."},
        ],
    }
]
## Image URL
messages = [
    {
        "role": "user",
        "content": [
            {"type": "image", "image": "http://path/to/your/image.jpg"},
            {"type": "text", "text": "Describe this image."},
        ],
    }
]
## Base64 encoded image
messages = [
    {
        "role": "user",
        "content": [
            {"type": "image", "image": "data:image;base64,/9j/..."},
            {"type": "text", "text": "Describe this image."},
        ],
    }
]

```

####  [ ](https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct#image-resolution-for-performance-boost) Image Resolution for performance boost 
The model supports a wide range of resolution inputs. By default, it uses the native resolution for input, but higher resolutions can enhance performance at the cost of more computation. Users can set the minimum and maximum number of pixels to achieve an optimal configuration for their needs, such as a token count range of 256-1280, to balance speed and memory usage.

```
min_pixels = 256 * 28 * 28
max_pixels = 1280 * 28 * 28
processor = AutoProcessor.from_pretrained(
    "Qwen/Qwen2.5-VL-3B-Instruct", min_pixels=min_pixels, max_pixels=max_pixels
)

```

Besides, We provide two methods for fine-grained control over the image size input to the model:
  1. Define min_pixels and max_pixels: Images will be resized to maintain their aspect ratio within the range of min_pixels and max_pixels.
  2. Specify exact dimensions: Directly set `resized_height` and `resized_width`. These values will be rounded to the nearest multiple of 28.



```
# min_pixels and max_pixels
messages = [
    {
        "role": "user",
        "content": [
            {
                "type": "image",
                "image": "file:///path/to/your/image.jpg",
                "resized_height": 280,
                "resized_width": 420,
            },
            {"type": "text", "text": "Describe this image."},
        ],
    }
]
# resized_height and resized_width
messages = [
    {
        "role": "user",
        "content": [
            {
                "type": "image",
                "image": "file:///path/to/your/image.jpg",
                "min_pixels": 50176,
                "max_pixels": 50176,
            },
            {"type": "text", "text": "Describe this image."},
        ],
    }
]

```

###  [ ](https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct#processing-long-texts) Processing Long Texts 
The current `config.json` is set for context length up to 32,768 tokens. To handle extensive inputs exceeding 32,768 tokens, we utilize [YaRN](https://arxiv.org/abs/2309.00071), a technique for enhancing model length extrapolation, ensuring optimal performance on lengthy texts.
For supported frameworks, you could add the following to `config.json` to enable YaRN:

```
{
    ...,
    "type": "yarn",
    "mrope_section": [
        16,
        24,
        24
    ],
    "factor": 4,
    "original_max_position_embeddings": 32768
}

```

However, it should be noted that this method has a significant impact on the performance of temporal and spatial localization tasks, and is therefore not recommended for use.
At the same time, for long video inputs, since MRoPE itself is more economical with ids, the max_position_embeddings can be directly modified to a larger value, such as 64k.
##  [ ](https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct#citation) Citation 
If you find our work helpful, feel free to give us a cite.

```
@misc{qwen2.5-VL,
    title = {Qwen2.5-VL},
    url = {https://qwenlm.github.io/blog/qwen2.5-vl/},
    author = {Qwen Team},
    month = {January},
    year = {2025}
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
    1,642,970
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
Input a message to start chatting with **Qwen/Qwen2.5-VL-3B-Instruct**.
Send
View Code Snippets
[ Compare providers](https://huggingface.co/inference/models?model=Qwen%2FQwen2.5-VL-3B-Instruct)
##  Model tree for Qwen/Qwen2.5-VL-3B-Instruct [](https://huggingface.co/docs/hub/model-cards#specifying-a-base-model)
Adapters
[305 models](https://huggingface.co/models?other=base_model:adapter:Qwen/Qwen2.5-VL-3B-Instruct)
Finetunes
[889 models](https://huggingface.co/models?other=base_model:finetune:Qwen/Qwen2.5-VL-3B-Instruct)
Quantizations
[](https://huggingface.co/models?apps=llama.cpp&other=base_model:quantized:Qwen/Qwen2.5-VL-3B-Instruct "Use with llama.cpp")[](https://huggingface.co/models?apps=llama-app&other=base_model:quantized:Qwen/Qwen2.5-VL-3B-Instruct "Use with Llama")[](https://huggingface.co/models?apps=lmstudio&other=base_model:quantized:Qwen/Qwen2.5-VL-3B-Instruct "Use with LM Studio")[](https://huggingface.co/models?apps=jan&other=base_model:quantized:Qwen/Qwen2.5-VL-3B-Instruct "Use with Jan")
[98 models](https://huggingface.co/models?other=base_model:quantized:Qwen/Qwen2.5-VL-3B-Instruct)
##  Spaces using Qwen/Qwen2.5-VL-3B-Instruct 100
[🟩 embedl/hfviewer ](https://huggingface.co/spaces/embedl/hfviewer)[🎥 NERueda/video_anomaly_detection ](https://huggingface.co/spaces/NERueda/video_anomaly_detection)[🔥 alexnasa/Wan2.2-Animate-ZEROGPU ](https://huggingface.co/spaces/alexnasa/Wan2.2-Animate-ZEROGPU)[⚡ fastgpu/vram-and-gpu-cost-calculator ](https://huggingface.co/spaces/fastgpu/vram-and-gpu-cost-calculator)[⚡ ArrheniusC/Wan2.1 ](https://huggingface.co/spaces/ArrheniusC/Wan2.1)[🚀 gexinh/vlm-probe ](https://huggingface.co/spaces/gexinh/vlm-probe)[📊 Sneha7/FSDP_and_DDP ](https://huggingface.co/spaces/Sneha7/FSDP_and_DDP)[🎥 multimodalart/self-forcing ](https://huggingface.co/spaces/multimodalart/self-forcing) + 95 Spaces + 92 Spaces
##  Collection including Qwen/Qwen2.5-VL-3B-Instruct
#### [Qwen2.5-VL Collection Vision-language model series based on Qwen2.5 • 10 items • Updated Mar 2 • 573 ](https://huggingface.co/collections/Qwen/qwen25-vl)
##  Papers for Qwen/Qwen2.5-VL-3B-Instruct
#### [Qwen2-VL: Enhancing Vision-Language Model's Perception of the World at Any Resolution Paper • 2409.12191 • Published Sep 18, 2024 • 82 ](https://huggingface.co/papers/2409.12191)#### [YaRN: Efficient Context Window Extension of Large Language Models Paper • 2309.00071 • Published Aug 31, 2023 • 88 ](https://huggingface.co/papers/2309.00071)#### [Qwen-VL: A Frontier Large Vision-Language Model with Versatile Abilities Paper • 2308.12966 • Published Aug 24, 2023 • 13 ](https://huggingface.co/papers/2308.12966)
##  Evaluation results [](https://huggingface.co/docs/hub/eval-results)
  * [MMMU/MMMU_Pro](https://huggingface.co/datasets/MMMU/MMMU_Pro) · Mmmu Pro Vision [View evaluation results ](https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct/discussions/50) [leaderboard ](https://huggingface.co/datasets/MMMU/MMMU_Pro?eval_result=Qwen/Qwen2.5-VL-3B-Instruct&leaderboard_task_id=mmmu_pro_vision)
[](https://huggingface.co/datasets/MMMU/MMMU_Pro?eval_result=Qwen%2FQwen2.5-VL-3B-Instruct&leaderboard_task_id=mmmu_pro_vision&leaderboard_max_params=6B) 32.7
  * [likaixin/ScreenSpot-Pro](https://huggingface.co/datasets/likaixin/ScreenSpot-Pro) [leaderboard ](https://huggingface.co/datasets/likaixin/ScreenSpot-Pro?eval_result=Qwen/Qwen2.5-VL-3B-Instruct)
  * Overall [View evaluation results ](https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct/discussions/48) [ ![](https://cdn-avatars.huggingface.co/v1/production/uploads/6141a88b3a0ec78603c9e784/DJsxSmWV39M33JFheLobC.jpeg) source](https://gui-agent.github.io/grounding-leaderboard/)
16.1
  * Android Studio Macos [View evaluation results ](https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct/discussions/48) [ ![](https://cdn-avatars.huggingface.co/v1/production/uploads/6141a88b3a0ec78603c9e784/DJsxSmWV39M33JFheLobC.jpeg) source](https://gui-agent.github.io/grounding-leaderboard/)
2.5
  * Autocad Windows [View evaluation results ](https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct/discussions/48) [ ![](https://cdn-avatars.huggingface.co/v1/production/uploads/6141a88b3a0ec78603c9e784/DJsxSmWV39M33JFheLobC.jpeg) source](https://gui-agent.github.io/grounding-leaderboard/)
[](https://huggingface.co/datasets/likaixin/ScreenSpot-Pro?eval_result=Qwen%2FQwen2.5-VL-3B-Instruct&leaderboard_task_id=autocad_windows&leaderboard_max_params=6B) 2.9
  * +24 more


System theme
Company
[TOS](https://huggingface.co/terms-of-service) [Privacy](https://huggingface.co/privacy) [About](https://huggingface.co/huggingface) [Careers](https://apply.workable.com/huggingface/) [](https://huggingface.co/)
Website
[Models](https://huggingface.co/models) [Datasets](https://huggingface.co/datasets) [Spaces](https://huggingface.co/spaces) [Pricing](https://huggingface.co/pricing) [Docs](https://huggingface.co/docs)
View evaluation results shared by the community
Ranked #1 in the < 6B size range
View evaluation results shared by the community
Source: ScreenSpot-Pro Leaderboard by merve
View evaluation results shared by the community
Source: ScreenSpot-Pro Leaderboard by merve
View evaluation results shared by the community
Source: ScreenSpot-Pro Leaderboard by merve
Ranked #3 in the < 6B size range
Inference providers allow you to run inference using different serverless providers.

