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
[Qwen-Image-Edit-2509-Fusion](https://huggingface.co/dx8152/Qwen-Image-Edit-2509-Fusion)
Like 255
[ Image-to-Image ](https://huggingface.co/models?pipeline_tag=image-to-image)[ Diffusers ](https://huggingface.co/models?library=diffusers)[ lora ](https://huggingface.co/models?other=lora)
License: apache-2.0
[ Model card ](https://huggingface.co/dx8152/Qwen-Image-Edit-2509-Fusion)[ Files Files and versions xet ](https://huggingface.co/dx8152/Qwen-Image-Edit-2509-Fusion/tree/main)[ Community 9 ](https://huggingface.co/dx8152/Qwen-Image-Edit-2509-Fusion/discussions)
Deploy
Copy to bucket
Use this model
### Instructions to use dx8152/Qwen-Image-Edit-2509-Fusion with libraries, inference providers, notebooks, and local apps. Follow these links to get started.
  * Libraries
  * [ Diffusers](https://huggingface.co/dx8152/Qwen-Image-Edit-2509-Fusion?library=diffusers)
How to use dx8152/Qwen-Image-Edit-2509-Fusion with Diffusers:

```
pip install -U diffusers transformers accelerate
```

```
import torch
from diffusers import DiffusionPipeline
from diffusers.utils import load_image

# switch to "mps" for apple devices
pipe = DiffusionPipeline.from_pretrained("Qwen/Qwen-Image-Edit-2509", dtype=torch.bfloat16, device_map="cuda")
pipe.load_lora_weights("dx8152/Qwen-Image-Edit-2509-Fusion")

prompt = "Turn this cat into a dog"
input_image = load_image("https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/diffusers/cat.png")

image = pipe(image=input_image, prompt=prompt).images[0]
```

  * Inference
  * Inference Providers
  * Notebooks
  * [ Google Colab](https://huggingface.co/dx8152/Qwen-Image-Edit-2509-Fusion/colab)
  * [ Kaggle](https://huggingface.co/dx8152/Qwen-Image-Edit-2509-Fusion/kaggle)
  * Local Apps [Settings](https://huggingface.co/settings/local-apps "Set up your favorite local applications")
  * [ Draw Things ](https://drawthings.ai/import/diffusers/pipeline.load_lora_weights?repo_id=dx8152/Qwen-Image-Edit-2509-Fusion)


Hi everyone overseas! ModelScope has launched its training service abroad.
My LoRa training is all done using ModelScope. Thanks to the ModelScope team for providing the training infrastructure. Give it a try!
<https://www.modelscope.cn/aigc/modelTraining>
* * *
Welcome everyone to use Lora of Qwen-Edit-2509 of Image Fusion, its performance is amazing！
Online running link： <https://www.runninghub.ai/post/1983425100517187586?inviteCode=rh-v1331>
The trigger words are: 溶图,纠正产品透视角度和光影并使产品融入背景
Instructions: Download the lora file to the models/loras folder. 
You also need this lora and use them together: <https://huggingface.co/lightx2v/Qwen-Image-Lightning/tree/main>
This is the effect used by Lora: 
YouTube：<https://youtu.be/0ObRTPbOPi0>
Blibili：<https://www.bilibili.com/video/BV15vWpzwEKJ/>
For communication/cooperation, you can join the discord group to communicate： <https://discord.gg/yVAVa43mWk>
If these resources are helpful to you, or if you use them for business purposes, please buy me a coffee. Thank you for supporting original content! PayPal: Daniel8152
[![未标题-1](https://cdn-uploads.huggingface.co/production/uploads/64461e86ab86b035add67e41/f7NFToLOA9kQ3ChzOyGpn.gif)](https://cdn-uploads.huggingface.co/production/uploads/64461e86ab86b035add67e41/f7NFToLOA9kQ3ChzOyGpn.gif) [![2](https://cdn-uploads.huggingface.co/production/uploads/64461e86ab86b035add67e41/PYB_whFoXiv4V4NIJOV9d.gif)](https://cdn-uploads.huggingface.co/production/uploads/64461e86ab86b035add67e41/PYB_whFoXiv4V4NIJOV9d.gif) [![5](https://cdn-uploads.huggingface.co/production/uploads/64461e86ab86b035add67e41/_xgWIWmZ_2w-XKbIVjntd.gif)](https://cdn-uploads.huggingface.co/production/uploads/64461e86ab86b035add67e41/_xgWIWmZ_2w-XKbIVjntd.gif) [![4](https://cdn-uploads.huggingface.co/production/uploads/64461e86ab86b035add67e41/AGJIIHizpbcE-_G12XcvL.gif)](https://cdn-uploads.huggingface.co/production/uploads/64461e86ab86b035add67e41/AGJIIHizpbcE-_G12XcvL.gif) [![3](https://cdn-uploads.huggingface.co/production/uploads/64461e86ab86b035add67e41/UvVO3VJreINwQqFXO-gSE.gif)](https://cdn-uploads.huggingface.co/production/uploads/64461e86ab86b035add67e41/UvVO3VJreINwQqFXO-gSE.gif) 

Downloads last month
    2,083
Inference Providers [NEW](https://huggingface.co/docs/inference-providers)
WaveSpeed
[ Image-to-Image ](https://huggingface.co/tasks/image-to-image "Learn more about image-to-image")
Drag image file here or click to browse from your device
Browse for image
(Optional) Text-guidance if the model has support for it Generate
View Code Snippets
Maximize
##  Model tree for dx8152/Qwen-Image-Edit-2509-Fusion [](https://huggingface.co/docs/hub/model-cards#specifying-a-base-model)
Base model
[Qwen/Qwen-Image-Edit-2509](https://huggingface.co/Qwen/Qwen-Image-Edit-2509)
Adapter
([86](https://huggingface.co/models?other=base_model:adapter:Qwen/Qwen-Image-Edit-2509))
this model
##  Spaces using dx8152/Qwen-Image-Edit-2509-Fusion 14
[🌖 prithivMLmods/Qwen-Image-Edit-2509-LoRAs-Fast-Fusion ](https://huggingface.co/spaces/prithivMLmods/Qwen-Image-Edit-2509-LoRAs-Fast-Fusion)[📸 linoyts/Qwen-Image-Edit-Fusion ](https://huggingface.co/spaces/linoyts/Qwen-Image-Edit-Fusion)[⭐ MySafeCode/Qwen-Image-Edit-2509-LoRAs-Fast-Fusion ](https://huggingface.co/spaces/MySafeCode/Qwen-Image-Edit-2509-LoRAs-Fast-Fusion)[📸 Omid40ail/4846 ](https://huggingface.co/spaces/Omid40ail/4846)[🌅 adowu/Qwen-Image-Edit-2509-LoRAs-Fast-Fusion_2 ](https://huggingface.co/spaces/adowu/Qwen-Image-Edit-2509-LoRAs-Fast-Fusion_2)[⭐ MrJasper1987/Multiimage ](https://huggingface.co/spaces/MrJasper1987/Multiimage)[📸 alejandrarr/Qwen-Image-Edit-Fusion ](https://huggingface.co/spaces/alejandrarr/Qwen-Image-Edit-Fusion)[⭐ alejandrarr/Qwen-Image-Edit-2509-LoRAs-Fast-Fusion ](https://huggingface.co/spaces/alejandrarr/Qwen-Image-Edit-2509-LoRAs-Fast-Fusion) + 9 Spaces + 6 Spaces
System theme
Company
[TOS](https://huggingface.co/terms-of-service) [Privacy](https://huggingface.co/privacy) [About](https://huggingface.co/huggingface) [Careers](https://apply.workable.com/huggingface/) [](https://huggingface.co/)
Website
[Models](https://huggingface.co/models) [Datasets](https://huggingface.co/datasets) [Spaces](https://huggingface.co/spaces) [Pricing](https://huggingface.co/pricing) [Docs](https://huggingface.co/docs)
Inference providers allow you to run inference using different serverless providers.
##  Run 15,000+ Models Instantly
Inference Providers let you run inference on thousands of models served by our partners using a simple, unified, OpenAI-compatible serverless API ([Learn more](https://huggingface.co/docs/inference-providers)).
dx8152/Qwen-Image-Edit-2509-Fusion is supported by the following Inference Providers:
WaveSpeed
View API Code Dismiss

