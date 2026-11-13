Source: https://huggingface.co/zai-org/CogVideoX1.5-5B-I2V (fetched 2026-11-13 with crawl4ai)

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
[ ![](https://cdn-avatars.huggingface.co/v1/production/uploads/62dc173789b4cf157d36ebee/i_pxzM2ZDo3Ub-BEgIkE9.png) ](https://huggingface.co/zai-org)
[zai-org](https://huggingface.co/zai-org)
/
[CogVideoX1.5-5B-I2V](https://huggingface.co/zai-org/CogVideoX1.5-5B-I2V)
Like 127
Follow
![](https://cdn-avatars.huggingface.co/v1/production/uploads/62dc173789b4cf157d36ebee/i_pxzM2ZDo3Ub-BEgIkE9.png) Z.ai 23.4k
[ Image-to-Video ](https://huggingface.co/models?pipeline_tag=image-to-video)[ Diffusers ](https://huggingface.co/models?library=diffusers)[ Safetensors ](https://huggingface.co/models?library=safetensors)[ English ](https://huggingface.co/models?language=en)[ CogVideoXImageToVideoPipeline ](https://huggingface.co/models?other=diffusers%3ACogVideoXImageToVideoPipeline)[ video-generation ](https://huggingface.co/models?other=video-generation)[ thudm ](https://huggingface.co/models?other=thudm)
arxiv: 2408.06072
License: other
[ Model card ](https://huggingface.co/zai-org/CogVideoX1.5-5B-I2V)[ Files Files and versions xet ](https://huggingface.co/zai-org/CogVideoX1.5-5B-I2V/tree/main)[ Community 17 ](https://huggingface.co/zai-org/CogVideoX1.5-5B-I2V/discussions)
Deploy
Copy to bucket
Use this model
### Instructions to use zai-org/CogVideoX1.5-5B-I2V with libraries, inference providers, notebooks, and local apps. Follow these links to get started.
  * Libraries
  * [ Diffusers](https://huggingface.co/zai-org/CogVideoX1.5-5B-I2V?library=diffusers)
How to use zai-org/CogVideoX1.5-5B-I2V with Diffusers:

```
pip install -U diffusers transformers accelerate
```

```
import torch
from diffusers import DiffusionPipeline
from diffusers.utils import load_image, export_to_video

# switch to "mps" for apple devices
pipe = DiffusionPipeline.from_pretrained("zai-org/CogVideoX1.5-5B-I2V", dtype=torch.bfloat16, device_map="cuda")
pipe.to("cuda")

prompt = "A man with short gray hair plays a red electric guitar."
image = load_image(
    "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/diffusers/guitar-man.png"
)

output = pipe(image=image, prompt=prompt).frames[0]
export_to_video(output, "output.mp4")
```

  * Notebooks
  * [ Google Colab](https://huggingface.co/zai-org/CogVideoX1.5-5B-I2V/colab)
  * [ Kaggle](https://huggingface.co/zai-org/CogVideoX1.5-5B-I2V/kaggle)


  * [CogVideoX1.5-5B-I2V](https://huggingface.co/zai-org/CogVideoX1.5-5B-I2V#cogvideox15-5b-i2v "CogVideoX1.5-5B-I2V")
    * [Model Introduction](https://huggingface.co/zai-org/CogVideoX1.5-5B-I2V#model-introduction "Model Introduction")
    * [Getting Started Quickly 🤗](https://huggingface.co/zai-org/CogVideoX1.5-5B-I2V#getting-started-quickly-%F0%9F%A4%97 "Getting Started Quickly 🤗")
    * [Quantized Inference](https://huggingface.co/zai-org/CogVideoX1.5-5B-I2V#quantized-inference "Quantized Inference")
    * [Further Exploration](https://huggingface.co/zai-org/CogVideoX1.5-5B-I2V#further-exploration "Further Exploration")
    * [Model License](https://huggingface.co/zai-org/CogVideoX1.5-5B-I2V#model-license "Model License")
    * [Citation](https://huggingface.co/zai-org/CogVideoX1.5-5B-I2V#citation "Citation")


#  [ ](https://huggingface.co/zai-org/CogVideoX1.5-5B-I2V#cogvideox15-5b-i2v) CogVideoX1.5-5B-I2V 
![](https://github.com/THUDM/CogVideo/raw/main/resources/logo.svg)
[📄 中文阅读](https://huggingface.co/THUDM/CogVideoX1.5-5B-I2V/blob/main/README_zh.md) | [🤗 Huggingface Space](https://huggingface.co/spaces/THUDM/CogVideoX-5B-Space) | [🌐 Github ](https://github.com/THUDM/CogVideo) | [📜 arxiv ](https://arxiv.org/pdf/2408.06072)
📍 Visit [ Qingying ](https://chatglm.cn/video?fr=osm_cogvideox) and the [ API Platform ](https://open.bigmodel.cn/?utm_campaign=open&_channel_track_key=OWTVNma9) to experience the commercial video generation model 
##  [ ](https://huggingface.co/zai-org/CogVideoX1.5-5B-I2V#model-introduction) Model Introduction 
CogVideoX is an open-source video generation model similar to [QingYing](https://chatglm.cn/video?fr=osm_cogvideo). Below is a table listing information on the video generation models available in this generation:  
| Model Name  | CogVideoX1.5-5B  | CogVideoX1.5-5B-I2V (Current Repository)  |  
| --- | --- | --- |  
| Video Resolution  | 1360 * 768  |  Min(W, H) = 768   
768 ≤ Max(W, H) ≤ 1360   
Max(W, H) % 16 = 0   |  
| Inference Precision  |  **BF16 (recommended)** , FP16, FP32, FP8*, INT8, not supported INT4  |  
| Single GPU Inference Memory Consumption  | **BF16: 9GB minimum***  |  
| Multi-GPU Inference Memory Consumption  |  **BF16: 24GB* using diffusers**  
 |  
| Inference Speed  
(Step = 50, FP/BF16)  | Single A100: ~1000 seconds (5-second video)  
Single H100: ~550 seconds (5-second video)  |  
| Prompt Language  | English*  |  
| Max Prompt Length  | 224 Tokens  |  
| Video Length  | 5 or 10 seconds  |  
| Frame Rate  | 16 frames/second  |  
**Data Explanation**
  * Testing with the `diffusers` library enabled all optimizations included in the library. This scheme has not been tested on non-NVIDIA A100/H100 devices. It should generally work with all NVIDIA Ampere architecture or higher devices. Disabling optimizations can triple VRAM usage but increase speed by 3-4 times. You can selectively disable certain optimizations, including:



```
pipe.enable_sequential_cpu_offload()
pipe.vae.enable_slicing()
pipe.vae.enable_tiling()

```

  * In multi-GPU inference, `enable_sequential_cpu_offload()` optimization needs to be disabled.
  * Using an INT8 model reduces inference speed, meeting the requirements of lower VRAM GPUs while retaining minimal video quality degradation, at the cost of significant speed reduction.
  * [PytorchAO](https://github.com/pytorch/ao) and [Optimum-quanto](https://github.com/huggingface/optimum-quanto/) can be used to quantize the text encoder, Transformer, and VAE modules, reducing CogVideoX’s memory requirements, making it feasible to run the model on smaller VRAM GPUs. TorchAO quantization is fully compatible with `torch.compile`, significantly improving inference speed. `FP8` precision is required for NVIDIA H100 and above, which requires source installation of `torch`, `torchao`, `diffusers`, and `accelerate`. Using `CUDA 12.4` is recommended.
  * Inference speed testing also used the above VRAM optimizations, and without optimizations, speed increases by about 10%. Only `diffusers` versions of models support quantization.
  * Models support English input only; other languages should be translated into English during prompt crafting with a larger model.


**Note**
  * Use [SAT](https://github.com/THUDM/SwissArmyTransformer) for inference and fine-tuning SAT version models. Check our GitHub for more details.


##  [ ](https://huggingface.co/zai-org/CogVideoX1.5-5B-I2V#getting-started-quickly-%F0%9F%A4%97) Getting Started Quickly 🤗 
This model supports deployment using the Hugging Face diffusers library. You can follow the steps below to get started.
**We recommend that you visit our[GitHub](https://github.com/THUDM/CogVideo) to check out prompt optimization and conversion to get a better experience.**
  1. Install the required dependencies



```
# diffusers (from source)
# transformers>=4.46.2
# accelerate>=1.1.1
# imageio-ffmpeg>=0.5.1
pip install git+https://github.com/huggingface/diffusers
pip install --upgrade transformers accelerate diffusers imageio-ffmpeg

```

  1. Run the code



```
import torch
from diffusers import CogVideoXImageToVideoPipeline
from diffusers.utils import export_to_video, load_image

prompt = "A little girl is riding a bicycle at high speed. Focused, detailed, realistic."
image = load_image(image="input.jpg")
pipe = CogVideoXImageToVideoPipeline.from_pretrained(
    "THUDM/CogVideoX1.5-5B-I2V",
    torch_dtype=torch.bfloat16
)

pipe.enable_sequential_cpu_offload()
pipe.vae.enable_tiling()
pipe.vae.enable_slicing()

video = pipe(
    prompt=prompt,
    image=image,
    num_videos_per_prompt=1,
    num_inference_steps=50,
    num_frames=81,
    guidance_scale=6,
    generator=torch.Generator(device="cuda").manual_seed(42),
).frames[0]

export_to_video(video, "output.mp4", fps=8)

```

##  [ ](https://huggingface.co/zai-org/CogVideoX1.5-5B-I2V#quantized-inference) Quantized Inference 
[PytorchAO](https://github.com/pytorch/ao) and [Optimum-quanto](https://github.com/huggingface/optimum-quanto/) can be used to quantize the text encoder, transformer, and VAE modules to reduce CogVideoX's memory requirements. This allows the model to run on free T4 Colab or GPUs with lower VRAM! Also, note that TorchAO quantization is fully compatible with `torch.compile`, which can significantly accelerate inference.

```
# To get started, PytorchAO needs to be installed from the GitHub source and PyTorch Nightly.
# Source and nightly installation is only required until the next release.

import torch
from diffusers import AutoencoderKLCogVideoX, CogVideoXTransformer3DModel, CogVideoXImageToVideoPipeline
from diffusers.utils import export_to_video, load_image
from transformers import T5EncoderModel
from torchao.quantization import quantize_, int8_weight_only

quantization = int8_weight_only

text_encoder = T5EncoderModel.from_pretrained("THUDM/CogVideoX1.5-5B-I2V", subfolder="text_encoder",
                                              torch_dtype=torch.bfloat16)
quantize_(text_encoder, quantization())

transformer = CogVideoXTransformer3DModel.from_pretrained("THUDM/CogVideoX1.5-5B-I2V", subfolder="transformer",
                                                          torch_dtype=torch.bfloat16)
quantize_(transformer, quantization())

vae = AutoencoderKLCogVideoX.from_pretrained("THUDM/CogVideoX1.5-5B-I2V", subfolder="vae", torch_dtype=torch.bfloat16)
quantize_(vae, quantization())

# Create pipeline and run inference
pipe = CogVideoXImageToVideoPipeline.from_pretrained(
    "THUDM/CogVideoX1.5-5B-I2V",
    text_encoder=text_encoder,
    transformer=transformer,
    vae=vae,
    torch_dtype=torch.bfloat16,
)

pipe.enable_model_cpu_offload()
pipe.vae.enable_tiling()
pipe.vae.enable_slicing()

prompt = "A little girl is riding a bicycle at high speed. Focused, detailed, realistic."
image = load_image(image="input.jpg")
video = pipe(
    prompt=prompt,
    image=image,
    num_videos_per_prompt=1,
    num_inference_steps=50,
    num_frames=81,
    guidance_scale=6,
    generator=torch.Generator(device="cuda").manual_seed(42),
).frames[0]

export_to_video(video, "output.mp4", fps=8)

```

Additionally, these models can be serialized and stored using PytorchAO in quantized data types to save disk space. You can find examples and benchmarks at the following links:
  * [torchao](https://gist.github.com/a-r-r-o-w/4d9732d17412888c885480c6521a9897)
  * [quanto](https://gist.github.com/a-r-r-o-w/31be62828b00a9292821b85c1017effa)


##  [ ](https://huggingface.co/zai-org/CogVideoX1.5-5B-I2V#further-exploration) Further Exploration 
Feel free to enter our [GitHub](https://github.com/THUDM/CogVideo), where you'll find:
  1. More detailed technical explanations and code.
  2. Optimized prompt examples and conversions.
  3. Detailed code for model inference and fine-tuning.
  4. Project update logs and more interactive opportunities.
  5. CogVideoX toolchain to help you better use the model.
  6. INT8 model inference code.


##  [ ](https://huggingface.co/zai-org/CogVideoX1.5-5B-I2V#model-license) Model License 
This model is released under the [CogVideoX LICENSE](https://huggingface.co/zai-org/CogVideoX1.5-5B-I2V/tree/main/LICENSE).
##  [ ](https://huggingface.co/zai-org/CogVideoX1.5-5B-I2V#citation) Citation 

```
@article{yang2024cogvideox,
  title={CogVideoX: Text-to-Video Diffusion Models with An Expert Transformer},
  author={Yang, Zhuoyi and Teng, Jiayan and Zheng, Wendi and Ding, Ming and Huang, Shiyu and Xu, Jiazheng and Yang, Yuanming and Hong, Wenyi and Zhang, Xiaohan and Feng, Guanyu and others},
  journal={arXiv preprint arXiv:2408.06072},
  year={2024}
}

```


Downloads last month
    620
Safetensors[](https://huggingface.co/docs/safetensors)
Model size
6B params
Tensor type
BF16 
·
Files info
Inference Providers [NEW](https://huggingface.co/docs/inference-providers)
[ Image-to-Video ](https://huggingface.co/tasks/image-to-video "Learn more about image-to-video")
This model isn't deployed by any Inference Provider. [🙋 1 Ask for provider support](https://huggingface.co/spaces/huggingface/InferenceSupport/discussions/4451)
##  Model tree for zai-org/CogVideoX1.5-5B-I2V [](https://huggingface.co/docs/hub/model-cards#specifying-a-base-model)
Quantizations
[1 model](https://huggingface.co/models?other=base_model:quantized:zai-org/CogVideoX1.5-5B-I2V)
##  Spaces using zai-org/CogVideoX1.5-5B-I2V 8
[🥇 Video-Reason/VBVR-Bench-Leaderboard ](https://huggingface.co/spaces/Video-Reason/VBVR-Bench-Leaderboard)[💻 pm6six/Image_to_video ](https://huggingface.co/spaces/pm6six/Image_to_video)[⚡ Zynara/Nolimit ](https://huggingface.co/spaces/Zynara/Nolimit)[💻 guardiancc/Image_to_video ](https://huggingface.co/spaces/guardiancc/Image_to_video)[💻 heather8516/Image_to_video ](https://huggingface.co/spaces/heather8516/Image_to_video)[💻 JahDaGanj/Image_to_video ](https://huggingface.co/spaces/JahDaGanj/Image_to_video)[💻 damg32/Image_to_video ](https://huggingface.co/spaces/damg32/Image_to_video)[🐨 patrickluan11/Motinon-AI ](https://huggingface.co/spaces/patrickluan11/Motinon-AI) + 3 Spaces
##  Collection including zai-org/CogVideoX1.5-5B-I2V
#### [CogVideo Collection 10 items • Updated Jun 30, 2025 • 66 ](https://huggingface.co/collections/zai-org/cogvideo)
##  Paper for zai-org/CogVideoX1.5-5B-I2V
#### [CogVideoX: Text-to-Video Diffusion Models with An Expert Transformer Paper • 2408.06072 • Published Aug 12, 2024 • 38 ](https://huggingface.co/papers/2408.06072)
System theme
Company
[TOS](https://huggingface.co/terms-of-service) [Privacy](https://huggingface.co/privacy) [About](https://huggingface.co/huggingface) [Careers](https://apply.workable.com/huggingface/) [](https://huggingface.co/)
Website
[Models](https://huggingface.co/models) [Datasets](https://huggingface.co/datasets) [Spaces](https://huggingface.co/spaces) [Pricing](https://huggingface.co/pricing) [Docs](https://huggingface.co/docs)
Inference providers allow you to run inference using different serverless providers.

