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
[Qwen-Image-Edit-2511](https://huggingface.co/Qwen/Qwen-Image-Edit-2511)
Like 1.51k
Follow
![](https://cdn-avatars.huggingface.co/v1/production/uploads/6215ca5692c0ecfba9186921/hrRM50-6XcdWgg2AKpENG.jpeg) Qwen 113k
[ Image-to-Image ](https://huggingface.co/models?pipeline_tag=image-to-image)[ Diffusers ](https://huggingface.co/models?library=diffusers)[ Safetensors ](https://huggingface.co/models?library=safetensors)[ English ](https://huggingface.co/models?language=en)[ Chinese ](https://huggingface.co/models?language=zh)[ QwenImageEditPlusPipeline ](https://huggingface.co/models?other=diffusers%3AQwenImageEditPlusPipeline)
arxiv: 2508.02324
License: apache-2.0
[ Model card ](https://huggingface.co/Qwen/Qwen-Image-Edit-2511)[ Files Files and versions xet ](https://huggingface.co/Qwen/Qwen-Image-Edit-2511/tree/main)[ Community 35 ](https://huggingface.co/Qwen/Qwen-Image-Edit-2511/discussions)
Deploy
Copy to bucket
Use this model
### Instructions to use Qwen/Qwen-Image-Edit-2511 with libraries, inference providers, notebooks, and local apps. Follow these links to get started.
  * Libraries
  * [ Diffusers](https://huggingface.co/Qwen/Qwen-Image-Edit-2511?library=diffusers)
How to use Qwen/Qwen-Image-Edit-2511 with Diffusers:

```
pip install -U diffusers transformers accelerate
```

```
import torch
from diffusers import DiffusionPipeline
from diffusers.utils import load_image

# switch to "mps" for apple devices
pipe = DiffusionPipeline.from_pretrained("Qwen/Qwen-Image-Edit-2511", dtype=torch.bfloat16, device_map="cuda")

prompt = "Turn this cat into a dog"
input_image = load_image("https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/diffusers/cat.png")

image = pipe(image=input_image, prompt=prompt).images[0]
```

  * Inference
  * Inference Providers
  * Notebooks
  * [ Google Colab](https://huggingface.co/Qwen/Qwen-Image-Edit-2511/colab)
  * [ Kaggle](https://huggingface.co/Qwen/Qwen-Image-Edit-2511/kaggle)


  * [Introduction](https://huggingface.co/Qwen/Qwen-Image-Edit-2511#introduction "Introduction")
    * [Quick Start](https://huggingface.co/Qwen/Qwen-Image-Edit-2511#quick-start "Quick Start")
    * [Showcase](https://huggingface.co/Qwen/Qwen-Image-Edit-2511#showcase "Showcase")
    * [License Agreement](https://huggingface.co/Qwen/Qwen-Image-Edit-2511#license-agreement "License Agreement")
    * [Citation](https://huggingface.co/Qwen/Qwen-Image-Edit-2511#citation "Citation")


![](https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-Image/qwen_image_edit_logo.png)
💜 [**Qwen Chat**](https://chat.qwen.ai/) | 🤗 [Hugging Face](https://huggingface.co/Qwen/Qwen-Image-Edit-2511) | 🤖 [ModelScope](https://modelscope.cn/models/Qwen/Qwen-Image-Edit-2511) | 📑 [Tech Report](https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-Image/Qwen_Image.pdf) | 📑 [Blog](https://qwenlm.github.io/blog/qwen-image-edit-2511/)   
🖥️ [Demo](https://huggingface.co/spaces/Qwen/Qwen-Image-Edit-2511) | 💬 [WeChat (微信)](https://github.com/QwenLM/Qwen-Image/blob/main/assets/wechat.png) | 🫨 [Discord](https://discord.gg/CV4E9rpNSD) | [Github](https://github.com/QwenLM/Qwen-Image)
![](https://qianwen-res.oss-accelerate-overseas.aliyuncs.com/Qwen-Image/edit2511/edit2511big.JPG#center)
#  [ ](https://huggingface.co/Qwen/Qwen-Image-Edit-2511#introduction) Introduction 
We are excited to introduce Qwen-Image-Edit-2511, an enhanced version over Qwen-Image-Edit-2509, featuring multiple improvements—including notably better consistency. To try out the latest model, please visit [Qwen Chat](https://chat.qwen.ai/?inputFeature=image_edit) and select the Image Editing feature.
Key enhancements in Qwen-Image-Edit-2511 include: mitigate image drift, improved character consistency，integrated LoRA capabilities， enhanced industrial design generation, and strengthened geometric reasoning ability.
##  [ ](https://huggingface.co/Qwen/Qwen-Image-Edit-2511#quick-start) Quick Start 
Install the latest version of diffusers

```
pip install git+https://github.com/huggingface/diffusers

```

The following contains a code snippet illustrating how to use `Qwen-Image-Edit-2511`:

```
import os
import torch
from PIL import Image
from diffusers import QwenImageEditPlusPipeline

pipeline = QwenImageEditPlusPipeline.from_pretrained("Qwen/Qwen-Image-Edit-2511", torch_dtype=torch.bfloat16)
print("pipeline loaded")

pipeline.to('cuda')
pipeline.set_progress_bar_config(disable=None)
image1 = Image.open("input1.png")
image2 = Image.open("input2.png")
prompt = "The magician bear is on the left, the alchemist bear is on the right, facing each other in the central park square."
inputs = {
    "image": [image1, image2],
    "prompt": prompt,
    "generator": torch.manual_seed(0),
    "true_cfg_scale": 4.0,
    "negative_prompt": " ",
    "num_inference_steps": 40,
    "guidance_scale": 1.0,
    "num_images_per_prompt": 1,
}
with torch.inference_mode():
    output = pipeline(**inputs)
    output_image = output.images[0]
    output_image.save("output_image_edit_2511.png")
    print("image saved at", os.path.abspath("output_image_edit_2511.png"))

```

##  [ ](https://huggingface.co/Qwen/Qwen-Image-Edit-2511#showcase) Showcase 
**Qwen-Image-Edit-2511 Enhances Character Consistency** In Qwen-Image-Edit-2511, character consistency has been significantly improved. The model can perform imaginative edits based on an input portrait while preserving the identity and visual characteristics of the subject.
[![](https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-Image/edit2511/%E5%B9%BB%E7%81%AF%E7%89%871.JPG#center)](https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-Image/edit2511/%E5%B9%BB%E7%81%AF%E7%89%871.JPG#center) [![](https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-Image/edit2511/%E5%B9%BB%E7%81%AF%E7%89%872.JPG#center)](https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-Image/edit2511/%E5%B9%BB%E7%81%AF%E7%89%872.JPG#center) [![](https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-Image/edit2511/%E5%B9%BB%E7%81%AF%E7%89%873.JPG#center)](https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-Image/edit2511/%E5%B9%BB%E7%81%AF%E7%89%873.JPG#center) [![](https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-Image/edit2511/%E5%B9%BB%E7%81%AF%E7%89%874.JPG#center)](https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-Image/edit2511/%E5%B9%BB%E7%81%AF%E7%89%874.JPG#center)
**Improved Multi-Person Consistency** While Qwen-Image-Edit-2509 already improved consistency for single-subject editing, Qwen-Image-Edit-2511 further enhances consistency in multi-person group photos—enabling high-fidelity fusion of two separate person images into a coherent group shot: [![](https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-Image/edit2511/%E5%B9%BB%E7%81%AF%E7%89%875.JPG#center)](https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-Image/edit2511/%E5%B9%BB%E7%81%AF%E7%89%875.JPG#center) [![](https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-Image/edit2511/%E5%B9%BB%E7%81%AF%E7%89%876.JPG#center)](https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-Image/edit2511/%E5%B9%BB%E7%81%AF%E7%89%876.JPG#center)
**Built-in Support for Community-Created LoRAs** Since Qwen-Image-Edit’s release, the community has developed many creative and high-quality LoRAs—greatly expanding its expressive potential. Qwen-Image-Edit-2511 integrates selected popular LoRAs directly into the base model, unlocking their effects without extra tuning.
For example, Lighting Enhancement LoRA Realistic lighting control is now achievable out-of-the-box: [![](https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-Image/edit2511/%E5%B9%BB%E7%81%AF%E7%89%877.JPG#center)](https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-Image/edit2511/%E5%B9%BB%E7%81%AF%E7%89%877.JPG#center)
[![](https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-Image/edit2511/%E5%B9%BB%E7%81%AF%E7%89%878.JPG#center)](https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-Image/edit2511/%E5%B9%BB%E7%81%AF%E7%89%878.JPG#center)
Another example, generating new viewpoints can now be done directly with the base model:
[![](https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-Image/edit2511/%E5%B9%BB%E7%81%AF%E7%89%879.JPG#center)](https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-Image/edit2511/%E5%B9%BB%E7%81%AF%E7%89%879.JPG#center)
[![](https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-Image/edit2511/%E5%B9%BB%E7%81%AF%E7%89%8710.JPG#center)](https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-Image/edit2511/%E5%B9%BB%E7%81%AF%E7%89%8710.JPG#center)
**Industrial Design Applications**
We’ve paid special attention to practical engineering scenarios—for instance, batch industrial product design:
[![](https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-Image/edit2511/%E5%B9%BB%E7%81%AF%E7%89%8711.JPG#center)](https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-Image/edit2511/%E5%B9%BB%E7%81%AF%E7%89%8711.JPG#center)
[![](https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-Image/edit2511/%E5%B9%BB%E7%81%AF%E7%89%8712.JPG#center)](https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-Image/edit2511/%E5%B9%BB%E7%81%AF%E7%89%8712.JPG#center)
…and material replacement for industrial components: [![](https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-Image/edit2511/%E5%B9%BB%E7%81%AF%E7%89%8713.JPG#center)](https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-Image/edit2511/%E5%B9%BB%E7%81%AF%E7%89%8713.JPG#center)
[![](https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-Image/edit2511/%E5%B9%BB%E7%81%AF%E7%89%8714.JPG#center)](https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-Image/edit2511/%E5%B9%BB%E7%81%AF%E7%89%8714.JPG#center)
**Enhanced Geometric Reasoning** Qwen-Image-Edit-2511 introduces stronger geometric reasoning capability—e.g., directly generating auxiliary construction lines for design or annotation purposes:
[![](https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-Image/edit2511/%E5%B9%BB%E7%81%AF%E7%89%8715.JPG#center)](https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-Image/edit2511/%E5%B9%BB%E7%81%AF%E7%89%8715.JPG#center)
[![](https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-Image/edit2511/%E5%B9%BB%E7%81%AF%E7%89%8716.JPG#center)](https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-Image/edit2511/%E5%B9%BB%E7%81%AF%E7%89%8716.JPG#center)
That wraps up the major updates in Qwen-Image-Edit-2511. Enjoy exploring the new capabilities! 🎉
##  [ ](https://huggingface.co/Qwen/Qwen-Image-Edit-2511#license-agreement) License Agreement 
Qwen-Image is licensed under Apache 2.0. 
##  [ ](https://huggingface.co/Qwen/Qwen-Image-Edit-2511#citation) Citation 
We kindly encourage citation of our work if you find it useful.

```
@misc{wu2025qwenimagetechnicalreport,
      title={Qwen-Image Technical Report}, 
      author={Chenfei Wu and Jiahao Li and Jingren Zhou and Junyang Lin and Kaiyuan Gao and Kun Yan and Sheng-ming Yin and Shuai Bai and Xiao Xu and Yilei Chen and Yuxiang Chen and Zecheng Tang and Zekai Zhang and Zhengyi Wang and An Yang and Bowen Yu and Chen Cheng and Dayiheng Liu and Deqing Li and Hang Zhang and Hao Meng and Hu Wei and Jingyuan Ni and Kai Chen and Kuan Cao and Liang Peng and Lin Qu and Minggang Wu and Peng Wang and Shuting Yu and Tingkun Wen and Wensen Feng and Xiaoxiao Xu and Yi Wang and Yichang Zhang and Yongqiang Zhu and Yujia Wu and Yuxuan Cai and Zenan Liu},
      year={2025},
      eprint={2508.02324},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      url={https://arxiv.org/abs/2508.02324}, 
}

```


Downloads last month
    199,715
Safetensors[](https://huggingface.co/docs/safetensors)
Model size
20B params
Tensor type
BF16 
·
Files info
Inference Providers [NEW](https://huggingface.co/docs/inference-providers)
fal
  * 

[ Image-to-Image ](https://huggingface.co/tasks/image-to-image "Learn more about image-to-image")
Drag image file here or click to browse from your device
Browse for image
(Optional) Text-guidance if the model has support for it Generate
View Code Snippets
Maximize
##  Model tree for Qwen/Qwen-Image-Edit-2511 [](https://huggingface.co/docs/hub/model-cards#specifying-a-base-model)
Adapters
[195 models](https://huggingface.co/models?other=base_model:adapter:Qwen/Qwen-Image-Edit-2511)
Finetunes
[98 models](https://huggingface.co/models?other=base_model:finetune:Qwen/Qwen-Image-Edit-2511)
Quantizations
[32 models](https://huggingface.co/models?other=base_model:quantized:Qwen/Qwen-Image-Edit-2511)
##  Spaces using Qwen/Qwen-Image-Edit-2511 100
[ ![](https://cdn-avatars.huggingface.co/v1/production/uploads/6215ca5692c0ecfba9186921/hrRM50-6XcdWgg2AKpENG.jpeg) Qwen/Qwen-Image-Edit-2511 ](https://huggingface.co/spaces/Qwen/Qwen-Image-Edit-2511)[✨️ AST-1320/Qwen-2511-Plus-Flux.2-klein ](https://huggingface.co/spaces/AST-1320/Qwen-2511-Plus-Flux.2-klein)[🎨 kogutt999/Pro-Realism-Edit-Studio ](https://huggingface.co/spaces/kogutt999/Pro-Realism-Edit-Studio)[⚡ aet256/Qwen-Image-Edit-Rapid-AIO-Loras-Experimental ](https://huggingface.co/spaces/aet256/Qwen-Image-Edit-Rapid-AIO-Loras-Experimental)[🖼 RioShiina/ImageGen ](https://huggingface.co/spaces/RioShiina/ImageGen)[🕺 Yellowbox2026/Qwen-Image-Edit-2511-AnyPose ](https://huggingface.co/spaces/Yellowbox2026/Qwen-Image-Edit-2511-AnyPose)[🎃 prithivMLmods/Qwen-Image-Edit-2511-LoRAs-Fast ](https://huggingface.co/spaces/prithivMLmods/Qwen-Image-Edit-2511-LoRAs-Fast)[🖼 Gramlin/ImageGennew ](https://huggingface.co/spaces/Gramlin/ImageGennew) + 95 Spaces + 92 Spaces
##  Collection including Qwen/Qwen-Image-Edit-2511
#### [Qwen-Image Collection 14 items • Updated Dec 31, 2025 • 124 ](https://huggingface.co/collections/Qwen/qwen-image)
##  Paper for Qwen/Qwen-Image-Edit-2511
#### [Qwen-Image Technical Report Paper • 2508.02324 • Published Aug 4, 2025 • 277 ](https://huggingface.co/papers/2508.02324)
System theme
Company
[TOS](https://huggingface.co/terms-of-service) [Privacy](https://huggingface.co/privacy) [About](https://huggingface.co/huggingface) [Careers](https://apply.workable.com/huggingface/) [](https://huggingface.co/)
Website
[Models](https://huggingface.co/models) [Datasets](https://huggingface.co/datasets) [Spaces](https://huggingface.co/spaces) [Pricing](https://huggingface.co/pricing) [Docs](https://huggingface.co/docs)
Inference providers allow you to run inference using different serverless providers.

