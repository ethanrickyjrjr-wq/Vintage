Source: https://huggingface.co/ai-forever/Real-ESRGAN (fetched 2026-11-13 with crawl4ai)

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
[ ![](https://cdn-avatars.huggingface.co/v1/production/uploads/5f91b1208a61a359f44e1851/4hQd2Bt8AeSnQsluli5f1.jpeg) ](https://huggingface.co/ai-forever)
[ai-forever](https://huggingface.co/ai-forever)
/
[Real-ESRGAN](https://huggingface.co/ai-forever/Real-ESRGAN)
Like 269
[ Russian ](https://huggingface.co/models?language=ru)[ English ](https://huggingface.co/models?language=en)[ PyTorch ](https://huggingface.co/models?other=PyTorch)
arxiv: 2107.10833
[ Model card ](https://huggingface.co/ai-forever/Real-ESRGAN)[ Files Files and versions xet ](https://huggingface.co/ai-forever/Real-ESRGAN/tree/main)[ Community 8 ](https://huggingface.co/ai-forever/Real-ESRGAN/discussions)
Copy to bucket
  * [Real-ESRGAN](https://huggingface.co/ai-forever/Real-ESRGAN#real-esrgan "Real-ESRGAN")
    * [Usage](https://huggingface.co/ai-forever/Real-ESRGAN#usage "Usage")


#  [ ](https://huggingface.co/ai-forever/Real-ESRGAN#real-esrgan) Real-ESRGAN 
PyTorch implementation of a Real-ESRGAN model trained on custom dataset. This model shows better results on faces compared to the original version. It is also easier to integrate this model into your projects.
Real-ESRGAN is an upgraded ESRGAN trained with pure synthetic data is capable of enhancing details while removing annoying artifacts for common real-world images.
  * [Paper](https://arxiv.org/abs/2107.10833)
  * [Original implementation](https://github.com/xinntao/Real-ESRGAN)
  * [Our github](https://github.com/sberbank-ai/Real-ESRGAN)


##  [ ](https://huggingface.co/ai-forever/Real-ESRGAN#usage) Usage 
Code for using model you can obtain in our [repo](https://github.com/sberbank-ai/Real-ESRGAN).

```
import torch
from PIL import Image
import numpy as np
from RealESRGAN import RealESRGAN

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

model = RealESRGAN(device, scale=4)
model.load_weights('weights/RealESRGAN_x4.pth', download=True)

path_to_image = 'inputs/lr_image.png'
image = Image.open(path_to_image).convert('RGB')

sr_image = model.predict(image)

sr_image.save('results/sr_image.png')

```
Downloads last month
    
-     
Downloads are not tracked for this model. [How to track ](https://huggingface.co/docs/hub/models-download-stats)
Inference Providers [NEW](https://huggingface.co/docs/inference-providers)
This model isn't deployed by any Inference Provider. [🙋 4 Ask for provider support](https://huggingface.co/spaces/huggingface/InferenceSupport/discussions/3492)
##  Model tree for ai-forever/Real-ESRGAN [](https://huggingface.co/docs/hub/model-cards#specifying-a-base-model)
Finetunes
[2 models](https://huggingface.co/models?other=base_model:finetune:ai-forever/Real-ESRGAN)
Quantizations
[1 model](https://huggingface.co/models?other=base_model:quantized:ai-forever/Real-ESRGAN)
##  Spaces using ai-forever/Real-ESRGAN 100
[🚀 gokaygokay/Tile-Upscaler ](https://huggingface.co/spaces/gokaygokay/Tile-Upscaler)[🌍 deepseek-ai/Janus-Pro-7B ](https://huggingface.co/spaces/deepseek-ai/Janus-Pro-7B)[🔥 baldiungu/Sss ](https://huggingface.co/spaces/baldiungu/Sss)[🔥 Lazzy6666/faceswap ](https://huggingface.co/spaces/Lazzy6666/faceswap)[⚡ Delanoir/ESRGAN ](https://huggingface.co/spaces/Delanoir/ESRGAN)[⚡ gokaygokay/PonyRealism ](https://huggingface.co/spaces/gokaygokay/PonyRealism)[🔥📹 Nick088/Real-ESRGAN_Pytorch ](https://huggingface.co/spaces/Nick088/Real-ESRGAN_Pytorch)[😻 gokaygokay/TileUpscalerV2 ](https://huggingface.co/spaces/gokaygokay/TileUpscalerV2) + 95 Spaces + 92 Spaces
##  Paper for ai-forever/Real-ESRGAN
#### [Real-ESRGAN: Training Real-World Blind Super-Resolution with Pure Synthetic Data Paper • 2107.10833 • Published Jul 22, 2021 • 3 ](https://huggingface.co/papers/2107.10833)
System theme
Company
[TOS](https://huggingface.co/terms-of-service) [Privacy](https://huggingface.co/privacy) [About](https://huggingface.co/huggingface) [Careers](https://apply.workable.com/huggingface/) [](https://huggingface.co/)
Website
[Models](https://huggingface.co/models) [Datasets](https://huggingface.co/datasets) [Spaces](https://huggingface.co/spaces) [Pricing](https://huggingface.co/pricing) [Docs](https://huggingface.co/docs)

