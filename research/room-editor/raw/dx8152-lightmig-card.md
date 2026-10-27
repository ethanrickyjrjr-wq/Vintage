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
[ ![](https://cdn-avatars.huggingface.co/v1/production/uploads/64461e86ab86b035add67e41/eDoTkuWIHd4kXplY0ZfiM.jpeg) ](https://huggingface.co/dx8152)
[dx8152](https://huggingface.co/dx8152)
/
[Qwen-Edit-2509-Light-Migration](https://huggingface.co/dx8152/Qwen-Edit-2509-Light-Migration)
Like 168
[ Image-to-Image ](https://huggingface.co/models?pipeline_tag=image-to-image)[ Diffusers ](https://huggingface.co/models?library=diffusers)[ lora ](https://huggingface.co/models?other=lora)
License: apache-2.0
[ Model card ](https://huggingface.co/dx8152/Qwen-Edit-2509-Light-Migration)[ Files Files and versions xet ](https://huggingface.co/dx8152/Qwen-Edit-2509-Light-Migration/tree/main)[ Community 5 ](https://huggingface.co/dx8152/Qwen-Edit-2509-Light-Migration/discussions)
Deploy
Copy to bucket
Use this model
### Instructions to use dx8152/Qwen-Edit-2509-Light-Migration with libraries, inference providers, notebooks, and local apps. Follow these links to get started.
  * Libraries
  * [ Diffusers](https://huggingface.co/dx8152/Qwen-Edit-2509-Light-Migration?library=diffusers)
How to use dx8152/Qwen-Edit-2509-Light-Migration with Diffusers:

```
pip install -U diffusers transformers accelerate
```

```
import torch
from diffusers import DiffusionPipeline
from diffusers.utils import load_image

# switch to "mps" for apple devices
pipe = DiffusionPipeline.from_pretrained("Qwen/Qwen-Image-Edit-2509", dtype=torch.bfloat16, device_map="cuda")
pipe.load_lora_weights("dx8152/Qwen-Edit-2509-Light-Migration")

prompt = "Turn this cat into a dog"
input_image = load_image("https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/diffusers/cat.png")

image = pipe(image=input_image, prompt=prompt).images[0]
```

  * Inference
  * Inference Providers
  * Notebooks
  * [ Google Colab](https://huggingface.co/dx8152/Qwen-Edit-2509-Light-Migration/colab)
  * [ Kaggle](https://huggingface.co/dx8152/Qwen-Edit-2509-Light-Migration/kaggle)
  * Local Apps [Settings](https://huggingface.co/settings/local-apps "Set up your favorite local applications")
  * [ Draw Things ](https://drawthings.ai/import/diffusers/pipeline.load_lora_weights?repo_id=dx8152/Qwen-Edit-2509-Light-Migration)


This model is trained (code-free!) on ModelScope. Thanks to ModelScope team for providing the training infra:
<https://www.modelscope.cn/aigc/modelTraining>
* * *
This time, we're bringing you the groundbreaking LoRA light transfer tool. It's the first to solve the problem of Qwen-Edit-2509's inability to perform secondary lighting on images with existing lighting. 
* * *
Online running link： [www.runninghub.ai/post/1997616377580204033?inviteCode=rh-v1331](http://www.runninghub.ai/post/1997616377580204033?inviteCode=rh-v1331)
This is a user guide:
YouTube：<https://youtu.be/zhB74PiVG_4>
Blibili：<https://www.bilibili.com/video/BV1VumPBSEuU/>
For communication/cooperation, you can join the discord group to communicate： <https://discord.gg/yVAVa43mWk>
* * *
The operation is extremely simple; just input the desired image and the desired lighting and shadow. The results are absolutely fantastic!
Default suggestion word: "参考色调，移除图1原有的光照并参考图2的光照和色调对图1重新照明"
[![1](https://cdn-uploads.huggingface.co/production/uploads/64461e86ab86b035add67e41/joTFyiAUje97_wHHXfVhX.jpeg)](https://cdn-uploads.huggingface.co/production/uploads/64461e86ab86b035add67e41/joTFyiAUje97_wHHXfVhX.jpeg)
[![2](https://cdn-uploads.huggingface.co/production/uploads/64461e86ab86b035add67e41/7xRjxM5-j7iLitAlwC1QK.jpeg)](https://cdn-uploads.huggingface.co/production/uploads/64461e86ab86b035add67e41/7xRjxM5-j7iLitAlwC1QK.jpeg)
[![3](https://cdn-uploads.huggingface.co/production/uploads/64461e86ab86b035add67e41/d9LZQJOjZRUdTpqMwunSD.jpeg)](https://cdn-uploads.huggingface.co/production/uploads/64461e86ab86b035add67e41/d9LZQJOjZRUdTpqMwunSD.jpeg)
[![4](https://cdn-uploads.huggingface.co/production/uploads/64461e86ab86b035add67e41/TCxODfWBmsWjAi-UtRkjv.jpeg)](https://cdn-uploads.huggingface.co/production/uploads/64461e86ab86b035add67e41/TCxODfWBmsWjAi-UtRkjv.jpeg)
* * *
You can use either the Image version of Lightning or the Edit version of Lightning; I feel the Edit version performs better.
[![7](https://cdn-uploads.huggingface.co/production/uploads/64461e86ab86b035add67e41/8ybZ0VupPxdt6fpFR6wjH.jpeg)](https://cdn-uploads.huggingface.co/production/uploads/64461e86ab86b035add67e41/8ybZ0VupPxdt6fpFR6wjH.jpeg) [![7 \(1\)](https://cdn-uploads.huggingface.co/production/uploads/64461e86ab86b035add67e41/dFYhmsYcPy-tf55OcjMIV.jpeg)](https://cdn-uploads.huggingface.co/production/uploads/64461e86ab86b035add67e41/dFYhmsYcPy-tf55OcjMIV.jpeg) [![7 \(2\)](https://cdn-uploads.huggingface.co/production/uploads/64461e86ab86b035add67e41/Sj8s7uPOnHhKzQR5m3GBI.jpeg)](https://cdn-uploads.huggingface.co/production/uploads/64461e86ab86b035add67e41/Sj8s7uPOnHhKzQR5m3GBI.jpeg)
[![4](https://cdn-uploads.huggingface.co/production/uploads/64461e86ab86b035add67e41/f7GROTnfoXU2PI-raqLQu.gif)](https://cdn-uploads.huggingface.co/production/uploads/64461e86ab86b035add67e41/f7GROTnfoXU2PI-raqLQu.gif) [![2](https://cdn-uploads.huggingface.co/production/uploads/64461e86ab86b035add67e41/3gmed3ph0mBWHRHbkSE0-.gif)](https://cdn-uploads.huggingface.co/production/uploads/64461e86ab86b035add67e41/3gmed3ph0mBWHRHbkSE0-.gif) [![1](https://cdn-uploads.huggingface.co/production/uploads/64461e86ab86b035add67e41/0rmLv2-8aNaRn6IqBXE1K.gif)](https://cdn-uploads.huggingface.co/production/uploads/64461e86ab86b035add67e41/0rmLv2-8aNaRn6IqBXE1K.gif) [![3](https://cdn-uploads.huggingface.co/production/uploads/64461e86ab86b035add67e41/HPI9IHifl4Jm9Kt5SkmA6.gif)](https://cdn-uploads.huggingface.co/production/uploads/64461e86ab86b035add67e41/HPI9IHifl4Jm9Kt5SkmA6.gif) 

Downloads last month
    6,089
Inference Providers [NEW](https://huggingface.co/docs/inference-providers)
WaveSpeed
[ Image-to-Image ](https://huggingface.co/tasks/image-to-image "Learn more about image-to-image")
Drag image file here or click to browse from your device
Browse for image
(Optional) Text-guidance if the model has support for it Generate
View Code Snippets
Maximize
##  Model tree for dx8152/Qwen-Edit-2509-Light-Migration [](https://huggingface.co/docs/hub/model-cards#specifying-a-base-model)
Base model
[Qwen/Qwen-Image-Edit-2509](https://huggingface.co/Qwen/Qwen-Image-Edit-2509)
Adapter
([86](https://huggingface.co/models?other=base_model:adapter:Qwen/Qwen-Image-Edit-2509))
this model
Adapters
[1 model](https://huggingface.co/models?other=base_model:adapter:dx8152/Qwen-Edit-2509-Light-Migration)
##  Spaces using dx8152/Qwen-Edit-2509-Light-Migration 100
[🎃 prithivMLmods/Qwen-Image-Edit-2511-LoRAs-Fast ](https://huggingface.co/spaces/prithivMLmods/Qwen-Image-Edit-2511-LoRAs-Fast)[🎃 Zenx566/Qwen-Image-Edit-2511-LoRAs-Fast ](https://huggingface.co/spaces/Zenx566/Qwen-Image-Edit-2511-LoRAs-Fast)[🎃 Shourabhji500/Qwen-Image-Edit-2511-LoRAs-Fast ](https://huggingface.co/spaces/Shourabhji500/Qwen-Image-Edit-2511-LoRAs-Fast)[💡 multimodalart/Qwen-Image-Light-Migration ](https://huggingface.co/spaces/multimodalart/Qwen-Image-Light-Migration)[🎃 NeoLeoLP/Qwen-Image-Edit-2511-LoRAs-Fast ](https://huggingface.co/spaces/NeoLeoLP/Qwen-Image-Edit-2511-LoRAs-Fast)[🎃 STCM/Qwen-Image-Edit-2511-LoRAs-Fast ](https://huggingface.co/spaces/STCM/Qwen-Image-Edit-2511-LoRAs-Fast)[🌖 prithivMLmods/Qwen-Image-Edit-2509-LoRAs-Fast-Fusion ](https://huggingface.co/spaces/prithivMLmods/Qwen-Image-Edit-2509-LoRAs-Fast-Fusion)[🌍 Qdpie/Qdpie-Qwen-Image-Editor ](https://huggingface.co/spaces/Qdpie/Qdpie-Qwen-Image-Editor) + 95 Spaces + 92 Spaces
System theme
Company
[TOS](https://huggingface.co/terms-of-service) [Privacy](https://huggingface.co/privacy) [About](https://huggingface.co/huggingface) [Careers](https://apply.workable.com/huggingface/) [](https://huggingface.co/)
Website
[Models](https://huggingface.co/models) [Datasets](https://huggingface.co/datasets) [Spaces](https://huggingface.co/spaces) [Pricing](https://huggingface.co/pricing) [Docs](https://huggingface.co/docs)
Inference providers allow you to run inference using different serverless providers.

