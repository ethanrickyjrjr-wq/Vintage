Source: https://huggingface.co/Lightricks/LTX-2 (fetched 2026-11-13 with crawl4ai)

[![Hugging Face's logo](https://huggingface.co/front/assets/huggingface_logo-noborder.svg) Hugging Face](https://huggingface.co/)
Search models, datasets, users... `Ctrl K`
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
[ ![](https://cdn-avatars.huggingface.co/v1/production/uploads/669524bcbcd81f395e8f60f6/0ynfqKEWMh_dn3h4ff1K5.png) ](https://huggingface.co/Lightricks)
[Lightricks](https://huggingface.co/Lightricks)
/
[LTX-2](https://huggingface.co/Lightricks/LTX-2)
Like 1.81k
Follow
![](https://cdn-avatars.huggingface.co/v1/production/uploads/669524bcbcd81f395e8f60f6/0ynfqKEWMh_dn3h4ff1K5.png) LTX.io 6.73k
[ Image-to-Video ](https://huggingface.co/models?pipeline_tag=image-to-video)[ Diffusers ](https://huggingface.co/models?library=diffusers)[ Safetensors ](https://huggingface.co/models?library=safetensors)
9 languages
[ LTX2Pipeline ](https://huggingface.co/models?other=diffusers%3ALTX2Pipeline)[ text-to-video ](https://huggingface.co/models?other=text-to-video)[ video-to-video ](https://huggingface.co/models?other=video-to-video)[ image-text-to-video ](https://huggingface.co/models?other=image-text-to-video)[ audio-to-video ](https://huggingface.co/models?other=audio-to-video)[ text-to-audio ](https://huggingface.co/models?other=text-to-audio)[ video-to-audio ](https://huggingface.co/models?other=video-to-audio)[ audio-to-audio ](https://huggingface.co/models?other=audio-to-audio)[ text-to-audio-video ](https://huggingface.co/models?other=text-to-audio-video)[ image-to-audio-video ](https://huggingface.co/models?other=image-to-audio-video)[ image-text-to-audio-video ](https://huggingface.co/models?other=image-text-to-audio-video)[ ltx-2 ](https://huggingface.co/models?other=ltx-2)[ ltx-video ](https://huggingface.co/models?other=ltx-video)[ ltxv ](https://huggingface.co/models?other=ltxv)[ lightricks ](https://huggingface.co/models?other=lightricks)
arxiv: 2601.03233
License: ltx-2-community-license-agreement
[ Model card ](https://huggingface.co/Lightricks/LTX-2)[ Files Files and versions xet ](https://huggingface.co/Lightricks/LTX-2/tree/main)[ Community 54 ](https://huggingface.co/Lightricks/LTX-2/discussions)
Deploy
Copy to bucket
Use this model
### Instructions to use Lightricks/LTX-2 with libraries, inference providers, notebooks, and local apps. Follow these links to get started.
  * Libraries
  * [ Diffusers](https://huggingface.co/Lightricks/LTX-2?library=diffusers)
How to use Lightricks/LTX-2 with Diffusers:

```
pip install -U diffusers transformers accelerate
```

```
import torch
from diffusers import DiffusionPipeline
from diffusers.utils import load_image, export_to_video

# switch to "mps" for apple devices
pipe = DiffusionPipeline.from_pretrained("Lightricks/LTX-2", dtype=torch.bfloat16, device_map="cuda")
pipe.to("cuda")

prompt = "A man with short gray hair plays a red electric guitar."
image = load_image(
    "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/diffusers/guitar-man.png"
)

output = pipe(image=image, prompt=prompt).frames[0]
export_to_video(output, "output.mp4")
```

  * Inference
  * Inference Providers
  * Notebooks
  * [ Google Colab](https://huggingface.co/Lightricks/LTX-2/colab)
  * [ Kaggle](https://huggingface.co/Lightricks/LTX-2/kaggle)


A newer version of this model is available: [Lightricks/LTX-2.3](https://huggingface.co/Lightricks/LTX-2.3)
  * [LTX-2 Model Card](https://huggingface.co/Lightricks/LTX-2#ltx-2-model-card "LTX-2 Model Card")
  * [Model Checkpoints](https://huggingface.co/Lightricks/LTX-2#model-checkpoints "Model Checkpoints")
    * [Model Details](https://huggingface.co/Lightricks/LTX-2#model-details "Model Details")
  * [Online demo](https://huggingface.co/Lightricks/LTX-2#online-demo "Online demo")
  * [Run locally](https://huggingface.co/Lightricks/LTX-2#run-locally "Run locally")
    * [Direct use license](https://huggingface.co/Lightricks/LTX-2#direct-use-license "Direct use license")
    * [ComfyUI](https://huggingface.co/Lightricks/LTX-2#comfyui "ComfyUI")
    * [PyTorch codebase](https://huggingface.co/Lightricks/LTX-2#pytorch-codebase "PyTorch codebase")
      * [Installation](https://huggingface.co/Lightricks/LTX-2#installation "Installation")
      * [Inference](https://huggingface.co/Lightricks/LTX-2#inference "Inference")
    * [Diffusers 🧨](https://huggingface.co/Lightricks/LTX-2#diffusers-%F0%9F%A7%A8 "Diffusers 🧨")
      * [Use with diffusers](https://huggingface.co/Lightricks/LTX-2#use-with-diffusers "Use with diffusers")
    * [General tips:](https://huggingface.co/Lightricks/LTX-2#general-tips "General tips:")
      * [Limitations](https://huggingface.co/Lightricks/LTX-2#limitations "Limitations")
  * [Train the model](https://huggingface.co/Lightricks/LTX-2#train-the-model "Train the model")
    * [Citation](https://huggingface.co/Lightricks/LTX-2#citation "Citation")


#  [ ](https://huggingface.co/Lightricks/LTX-2#ltx-2-model-card) LTX-2 Model Card 
This model card focuses on the LTX-2 model, as presented in the paper [LTX-2: Efficient Joint Audio-Visual Foundation Model](https://huggingface.co/papers/2601.03233). The codebase is available [here](https://github.com/Lightricks/LTX-2).
LTX-2 is a DiT-based audio-video foundation model designed to generate synchronized video and audio within a single model. It brings together the core building blocks of modern video generation, with open weights and a focus on practical, local execution. 
[![LTX-2 Open Source](https://img.youtube.com/vi/8fWAJXZJbRA/maxresdefault.jpg)](https://www.youtube.com/watch?v=8fWAJXZJbRA)
#  [ ](https://huggingface.co/Lightricks/LTX-2#model-checkpoints) Model Checkpoints   
| Name  | Notes  |  
| --- | --- |  
| ltx-2-19b-dev  | The full model, flexible and trainable in bf16  |  
| ltx-2-19b-dev-fp8  | The full model in fp8 quantization  |  
| ltx-2-19b-dev-fp4  | The full model in nvfp4 quantization  |  
| ltx-2-19b-distilled  | The distilled version of the full model, 8 steps, CFG=1  |  
| ltx-2-19b-distilled-lora-384  | A LoRA version of the distilled model applicable to the full model  |  
| ltx-2-spatial-upscaler-x2-1.0  | An x2 spatial upscaler for the ltx-2 latents, used in multi stage (multiscale) pipelines for higher resolution  |  
| ltx-2-temporal-upscaler-x2-1.0  | An x2 temporal upscaler for the ltx-2 latents, used in multi stage (multiscale) pipelines for higher FPS  |  
##  [ ](https://huggingface.co/Lightricks/LTX-2#model-details) Model Details 
  * **Developed by:** Lightricks
  * **Model type:** Diffusion-based audio-video foundation model
  * **Language(s):** English


#  [ ](https://huggingface.co/Lightricks/LTX-2#online-demo) Online demo 
LTX-2 is accessible right away via the following links:
  * [LTX-Studio text-to-video](https://app.ltx.studio/ltx-2-playground/t2v)
  * [LTX-Studio image-to-video](https://app.ltx.studio/ltx-2-playground/i2v)


#  [ ](https://huggingface.co/Lightricks/LTX-2#run-locally) Run locally 
##  [ ](https://huggingface.co/Lightricks/LTX-2#direct-use-license) Direct use license 
You can use the models - full, distilled, upscalers and any derivatives of the models - for purposes under the [license](https://github.com/Lightricks/LTX-2/blob/main/LICENSE-2).
##  [ ](https://huggingface.co/Lightricks/LTX-2#comfyui) ComfyUI 
We recommend you use the built-in LTXVideo nodes that can be found in the ComfyUI Manager. For manual installation information, please refer to our [documentation site](https://docs.ltx.video/open-source-model/integration-tools/comfy-ui).
##  [ ](https://huggingface.co/Lightricks/LTX-2#pytorch-codebase) PyTorch codebase 
The [LTX-2 codebase](https://github.com/Lightricks/LTX-2) is a monorepo with several packages. From model definition in 'ltx-core' to pipelines in 'ltx-pipelines' and training capabilities in 'ltx-trainer'. The codebase was tested with Python >=3.12, CUDA version >12.7, and supports PyTorch ~= 2.7.
###  [ ](https://huggingface.co/Lightricks/LTX-2#installation) Installation 

```
git clone https://github.com/Lightricks/LTX-2.git
cd LTX-2

# From the repository root
uv sync
source .venv/bin/activate

```

###  [ ](https://huggingface.co/Lightricks/LTX-2#inference) Inference 
To use our model, please follow the instructions in our [ltx-pipelines](https://github.com/Lightricks/LTX-2/blob/main/packages/ltx-pipelines/README.md) package.
##  [ ](https://huggingface.co/Lightricks/LTX-2#diffusers-%F0%9F%A7%A8) Diffusers 🧨 
LTX-2 is supported in the [Diffusers Python library](https://huggingface.co/docs/diffusers/main/en/index) for text & image-to-video generation. Read more on LTX-2 with diffusers [here](https://huggingface.co/docs/diffusers/main/en/api/pipelines/ltx2#diffusers.LTX2Pipeline.__call__.example). 
###  [ ](https://huggingface.co/Lightricks/LTX-2#use-with-diffusers) Use with diffusers 
To achieve production quality generation, it's recommended to use the two-stage generation pipeline. Example for 2-stage inference of text-to-video: 

```
import torch
from diffusers import FlowMatchEulerDiscreteScheduler
from diffusers.pipelines.ltx2 import LTX2Pipeline, LTX2LatentUpsamplePipeline
from diffusers.pipelines.ltx2.latent_upsampler import LTX2LatentUpsamplerModel
from diffusers.pipelines.ltx2.utils import STAGE_2_DISTILLED_SIGMA_VALUES
from diffusers.pipelines.ltx2.export_utils import encode_video

device = "cuda:0"
width = 768
height = 512

pipe = LTX2Pipeline.from_pretrained(
    "Lightricks/LTX-2", torch_dtype=torch.bfloat16
)
pipe.enable_sequential_cpu_offload(device=device)

prompt = "A beautiful sunset over the ocean"
negative_prompt = "shaky, glitchy, low quality, worst quality, deformed, distorted, disfigured, motion smear, motion artifacts, fused fingers, bad anatomy, weird hand, ugly, transition, static."

# Stage 1 default (non-distilled) inference
frame_rate = 24.0
video_latent, audio_latent = pipe(
    prompt=prompt,
    negative_prompt=negative_prompt,
    width=width,
    height=height,
    num_frames=121,
    frame_rate=frame_rate,
    num_inference_steps=40,
    sigmas=None,
    guidance_scale=4.0,
    output_type="latent",
    return_dict=False,
)

latent_upsampler = LTX2LatentUpsamplerModel.from_pretrained(
    "Lightricks/LTX-2",
    subfolder="latent_upsampler",
    torch_dtype=torch.bfloat16,
)
upsample_pipe = LTX2LatentUpsamplePipeline(vae=pipe.vae, latent_upsampler=latent_upsampler)
upsample_pipe.enable_model_cpu_offload(device=device)
upscaled_video_latent = upsample_pipe(
    latents=video_latent,
    output_type="latent",
    return_dict=False,
)[0]

# Load Stage 2 distilled LoRA
pipe.load_lora_weights(
    "Lightricks/LTX-2", adapter_name="stage_2_distilled", weight_name="ltx-2-19b-distilled-lora-384.safetensors"
)
pipe.set_adapters("stage_2_distilled", 1.0)
# VAE tiling is usually necessary to avoid OOM error when VAE decoding
pipe.vae.enable_tiling()
# Change scheduler to use Stage 2 distilled sigmas as is
new_scheduler = FlowMatchEulerDiscreteScheduler.from_config(
    pipe.scheduler.config, use_dynamic_shifting=False, shift_terminal=None
)
pipe.scheduler = new_scheduler
# Stage 2 inference with distilled LoRA and sigmas
video, audio = pipe(
    latents=upscaled_video_latent,
    audio_latents=audio_latent,
    prompt=prompt,
    negative_prompt=negative_prompt,
    num_inference_steps=3,
    noise_scale=STAGE_2_DISTILLED_SIGMA_VALUES[0], # renoise with first sigma value https://github.com/Lightricks/LTX-2/blob/main/packages/ltx-pipelines/src/ltx_pipelines/ti2vid_two_stages.py#L218
    sigmas=STAGE_2_DISTILLED_SIGMA_VALUES,
    guidance_scale=1.0,
    output_type="np",
    return_dict=False,
)

encode_video(
    video[0],
    fps=frame_rate,
    audio=audio[0].float().cpu(),
    audio_sample_rate=pipe.vocoder.config.output_sampling_rate,
    output_path="ltx2_lora_distilled_sample.mp4",
)

```

For more inference examples, including generation with the distilled checkpoint, visit [here](https://huggingface.co/docs/diffusers/main/en/api/pipelines/ltx2#diffusers.LTX2Pipeline.__call__.example). 
##  [ ](https://huggingface.co/Lightricks/LTX-2#general-tips) General tips: 
  * Width & height settings must be divisible by 32. Frame count must be divisible by 8 + 1. 
  * In case the resolution or number of frames are not divisible by 32 or 8 + 1, the input should be padded with -1 and then cropped to the desired resolution and number of frames.
  * For tips on writing effective prompts, please visit our [Prompting guide](https://ltx.video/blog/how-to-prompt-for-ltx-2)


###  [ ](https://huggingface.co/Lightricks/LTX-2#limitations) Limitations 
  * This model is not intended or able to provide factual information.
  * As a statistical model this checkpoint might amplify existing societal biases.
  * The model may fail to generate videos that matches the prompts perfectly.
  * Prompt following is heavily influenced by the prompting-style.
  * The model may generate content that is inappropriate or offensive.
  * When generating audio without speech, the audio may be of lower quality.


#  [ ](https://huggingface.co/Lightricks/LTX-2#train-the-model) Train the model 
The base (dev) model is fully trainable.
It's extremely easy to reproduce the LoRAs and IC-LoRAs we publish with the model by following the instructions on the [LTX-2 Trainer Readme](https://github.com/Lightricks/LTX-2/blob/main/packages/ltx-trainer/README.md).
Training for motion, style or likeness (sound+appearance) can take less than an hour in many settings.
##  [ ](https://huggingface.co/Lightricks/LTX-2#citation) Citation 

```
@article{hacohen2025ltx2,
  title={LTX-2: Efficient Joint Audio-Visual Foundation Model},
  author={HaCohen, Yoav and Brazowski, Benny and Chiprut, Nisan and Bitterman, Yaki and Kvochko, Andrew and Berkowitz, Avishai and Shalem, Daniel and Lifschitz, Daphna and Moshe, Dudu and Porat, Eitan and Richardson, Eitan and Guy Shiran and Itay Chachy and Jonathan Chetboun and Michael Finkelson and Michael Kupchick and Nir Zabari and Nitzan Guetta and Noa Kotler and Ofir Bibi and Ori Gordon and Poriya Panet and Roi Benita and Shahar Armon and Victor Kulikov and Yaron Inger and Yonatan Shiftan and Zeev Melumian and Zeev Farbman},
  journal={arXiv preprint arXiv:2601.03233},
  year={2025}
}

```


Downloads last month
    296,421
Safetensors[](https://huggingface.co/docs/safetensors)
Model size
19B params
Tensor type
F32 
·
BF16 
·
Files info
Inference Providers [NEW](https://huggingface.co/docs/inference-providers)
fal
  * 

[ Image-to-Video ](https://huggingface.co/tasks/image-to-video "Learn more about image-to-video")
Drag image file here or click to browse from your device
Browse for image
(Optional) Text-guidance if the model has support for it Generate
View Code Snippets
Maximize
##  Model tree for Lightricks/LTX-2 [](https://huggingface.co/docs/hub/model-cards#specifying-a-base-model)
Adapters
[58 models](https://huggingface.co/models?other=base_model:adapter:Lightricks/LTX-2)
Finetunes
[68 models](https://huggingface.co/models?other=base_model:finetune:Lightricks/LTX-2)
Quantizations
[10 models](https://huggingface.co/models?other=base_model:quantized:Lightricks/LTX-2)
##  Spaces using Lightricks/LTX-2 100
[ ![](https://cdn-avatars.huggingface.co/v1/production/uploads/669524bcbcd81f395e8f60f6/0ynfqKEWMh_dn3h4ff1K5.png) Lightricks/LTX-2-3 ](https://huggingface.co/spaces/Lightricks/LTX-2-3)[ ![](https://cdn-avatars.huggingface.co/v1/production/uploads/669524bcbcd81f395e8f60f6/0ynfqKEWMh_dn3h4ff1K5.png) Lightricks/ltx-2-distilled ](https://huggingface.co/spaces/Lightricks/ltx-2-distilled)[ ![](https://cdn-avatars.huggingface.co/v1/production/uploads/669524bcbcd81f395e8f60f6/0ynfqKEWMh_dn3h4ff1K5.png) Lightricks/ltx-2 ](https://huggingface.co/spaces/Lightricks/ltx-2)[🎭 ResembleAI/Dramabox ](https://huggingface.co/spaces/ResembleAI/Dramabox)[🎥 linoyts/LTX-2-3-First-Last-Frame ](https://huggingface.co/spaces/linoyts/LTX-2-3-First-Last-Frame)[🎨 hugging-apps/sensenova-sensenova-u1-5-8b-mot ](https://huggingface.co/spaces/hugging-apps/sensenova-sensenova-u1-5-8b-mot)[📹 prithivMLmods/LTX-2-LoRAs-Camera-Control-Dolly ](https://huggingface.co/spaces/prithivMLmods/LTX-2-LoRAs-Camera-Control-Dolly)[🎬 Alissonerdx/ltx-best-face-id ](https://huggingface.co/spaces/Alissonerdx/ltx-best-face-id) + 95 Spaces + 92 Spaces
##  Collection including Lightricks/LTX-2
#### [LTX-2 Collection LTX-2 base models and accompanying LoRAs and IC-LoRAs • 13 items • Updated Sep 9 • 64 ](https://huggingface.co/collections/Lightricks/ltx-2)
##  Paper for Lightricks/LTX-2
#### [LTX-2: Efficient Joint Audio-Visual Foundation Model Paper • 2601.03233 • Published Jan 6 • 203 ](https://huggingface.co/papers/2601.03233)
System theme
Company
[TOS](https://huggingface.co/terms-of-service) [Privacy](https://huggingface.co/privacy) [About](https://huggingface.co/huggingface) [Careers](https://apply.workable.com/huggingface/) [](https://huggingface.co/)
Website
[Models](https://huggingface.co/models) [Datasets](https://huggingface.co/datasets) [Spaces](https://huggingface.co/spaces) [Pricing](https://huggingface.co/pricing) [Docs](https://huggingface.co/docs)
Inference providers allow you to run inference using different serverless providers.
##  Run 15,000+ Models Instantly
Inference Providers let you run inference on thousands of models served by our partners using a simple, unified, OpenAI-compatible serverless API ([Learn more](https://huggingface.co/docs/inference-providers)).
Lightricks/LTX-2 is supported by the following Inference Providers:
WaveSpeed
fal
View API Code Dismiss

