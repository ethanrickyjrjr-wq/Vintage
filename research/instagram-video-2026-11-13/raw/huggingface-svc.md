Source: https://huggingface.co/stabilityai/stable-virtual-camera (fetched 2026-11-13 with crawl4ai)

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
[ ![](https://cdn-avatars.huggingface.co/v1/production/uploads/643feeb67bc3fbde1385cc25/7vmYr2XwVcPtkLzac_jxQ.png) ](https://huggingface.co/stabilityai)
[stabilityai](https://huggingface.co/stabilityai)
/
[stable-virtual-camera](https://huggingface.co/stabilityai/stable-virtual-camera)
Like 244
Follow
![](https://cdn-avatars.huggingface.co/v1/production/uploads/643feeb67bc3fbde1385cc25/7vmYr2XwVcPtkLzac_jxQ.png) Stability AI 40.7k
[ Image-to-Video ](https://huggingface.co/models?pipeline_tag=image-to-video)[ Safetensors ](https://huggingface.co/models?library=safetensors)[ novel-view-synthesis ](https://huggingface.co/models?other=novel-view-synthesis)
arxiv: 2503.14489
License: stabilityai-ai-non-commercial
[ Model card ](https://huggingface.co/stabilityai/stable-virtual-camera)[ Files Files and versions xet ](https://huggingface.co/stabilityai/stable-virtual-camera/tree/main)[ Community 6 ](https://huggingface.co/stabilityai/stable-virtual-camera/discussions)
Copy to bucket
##  You need to agree to share your Hugging Face information to access this model
This repository is publicly accessible, but you have to accept the conditions to access its files and content.
By clicking "Agree", you agree to the [License Agreement](https://huggingface.co/stabilityai/stable-virtual-camera/blob/main/LICENSE) and acknowledge Stability AI's [Privacy Policy](https://stability.ai/privacy-policy).
[Log in](https://huggingface.co/login?next=/stabilityai/stable-virtual-camera) or [Sign Up](https://huggingface.co/join?next=/stabilityai/stable-virtual-camera) to review the conditions and access this model content.
  * [Stable Virtual Camera](https://huggingface.co/stabilityai/stable-virtual-camera#stable-virtual-camera "Stable Virtual Camera")
    * [Updates](https://huggingface.co/stabilityai/stable-virtual-camera#updates "Updates")
    * [Model Description](https://huggingface.co/stabilityai/stable-virtual-camera#model-description "Model Description")
    * [License](https://huggingface.co/stabilityai/stable-virtual-camera#license "License")
    * [Model Sources](https://huggingface.co/stabilityai/stable-virtual-camera#model-sources "Model Sources")
  * [**Project Page**](https://huggingface.co/stabilityai/stable-virtual-camera#project-pagehttpsstable-virtual-cameragithubio "Project Page")
    * [Usage](https://huggingface.co/stabilityai/stable-virtual-camera#usage "Usage")
      * [Intended Uses](https://huggingface.co/stabilityai/stable-virtual-camera#intended-uses "Intended Uses")
      * [Out-of-Scope Uses](https://huggingface.co/stabilityai/stable-virtual-camera#out-of-scope-uses "Out-of-Scope Uses")
      * [Contact](https://huggingface.co/stabilityai/stable-virtual-camera#contact "Contact")


#  [ ](https://huggingface.co/stabilityai/stable-virtual-camera#stable-virtual-camera) Stable Virtual Camera 
#  [ ](https://huggingface.co/stabilityai/stable-virtual-camera#project-page) **[Project Page](https://stable-virtual-camera.github.io/)**
`Stable Virtual Camera` is a 1.3B generalist diffusion model for Novel View Synthesis (NVS), generating 3D consistent novel views of a scene, given any number of input views and target cameras. We encourage you to visit our [website](https://stable-virtual-camera.github.io/) for more visualizations.
###  [ ](https://huggingface.co/stabilityai/stable-virtual-camera#updates) Updates 
  * June 2025: Release `v1.1` checkpoint fixing known issues of foreground objects sometimes being detached from the background in `v1.0`.


###  [ ](https://huggingface.co/stabilityai/stable-virtual-camera#model-description) Model Description 
  * **Developed by** : [Stability AI](https://stability.ai/)
  * **Model type** : Transformer image-to-video model
  * **Model details** : This model was trained to generate 3D consistent novel views of a scene given any number of input views and target cameras. Users can specify the target camera trajectory freely, spanning across a large spatial range. Our model is capable of generating large viewpoint changes and temporally smooth samples. As a result, our samples maintain high consistency without requiring additional NeRF distillation, streamlining the view synthesis pipeline in the wild. Furthermore, we show that our method can generate high-quality videos lasting up to half a minute with seamless loop closure.


###  [ ](https://huggingface.co/stabilityai/stable-virtual-camera#license) License 
  * **Non-Commercial License:** Free for research and non-commercial use by organizations and individuals. Please refer to Stability AI's Non-Commercial License, available [here](https://huggingface.co/stabilityai/stable-virtual-camera/blob/main/LICENSE), for more information.


###  [ ](https://huggingface.co/stabilityai/stable-virtual-camera#model-sources) Model Sources 
  * **Project Page** : <https://stable-virtual-camera.github.io/>
  * **Paper** : <https://arxiv.org/abs/2503.14489>
  * **Blog** : <https://stability.ai/news/introducing-stable-virtual-camera-multi-view-video-generation-with-3d-camera-control>
  * **Code** : <https://github.com/Stability-AI/stable-virtual-camera>
  * **Demo** : <https://huggingface.co/spaces/stabilityai/stable-virtual-camera>
  * **Video** : <https://www.youtube.com/channel/UCLLlVDcS7nNenT_zzO3OPxQ>


##  [ ](https://huggingface.co/stabilityai/stable-virtual-camera#usage) Usage 
For usage instructions, please refer to our [GitHub repository](https://github.com/Stability-AI/stable-virtual-camera).
###  [ ](https://huggingface.co/stabilityai/stable-virtual-camera#intended-uses) Intended Uses 
Intended uses include the following research and non-commercial uses:
  * Generation of artworks and use in design and other artistic processes.
  * Applications in educational or creative tools.
  * Research on reconstruction models, including understanding the limitations of these models.


All uses of the model should be in accordance with our [Acceptable Use Policy](https://stability.ai/use-policy).
###  [ ](https://huggingface.co/stabilityai/stable-virtual-camera#out-of-scope-uses) Out-of-Scope Uses 
The model was not trained to be factual or true representations of people or events. As such, using the model to generate such content is out-of-scope of the abilities of this model.
###  [ ](https://huggingface.co/stabilityai/stable-virtual-camera#contact) Contact 
Please report any issues with the model or contact us:
  * Security issues: security@stability.ai
  * Privacy issues: privacy@stability.ai



Downloads last month
    30,383
Safetensors[](https://huggingface.co/docs/safetensors)
Model size
1B params
Tensor type
F32 
·
Files info
Inference Providers [NEW](https://huggingface.co/docs/inference-providers)
[ Image-to-Video ](https://huggingface.co/tasks/image-to-video "Learn more about image-to-video")
This model isn't deployed by any Inference Provider. [🙋 7 Ask for provider support](https://huggingface.co/spaces/huggingface/InferenceSupport/discussions/14)
##  Model tree for stabilityai/stable-virtual-camera [](https://huggingface.co/docs/hub/model-cards#specifying-a-base-model)
Finetunes
[1 model](https://huggingface.co/models?other=base_model:finetune:stabilityai/stable-virtual-camera)
##  Spaces using stabilityai/stable-virtual-camera 11
[ ![](https://cdn-avatars.huggingface.co/v1/production/uploads/643feeb67bc3fbde1385cc25/7vmYr2XwVcPtkLzac_jxQ.png) stabilityai/stable-virtual-camera ](https://huggingface.co/spaces/stabilityai/stable-virtual-camera)[🚀 ZayarnyukNick/stable-virtual-camera ](https://huggingface.co/spaces/ZayarnyukNick/stable-virtual-camera)[🚀 sengerchen/stable-virtual-camera ](https://huggingface.co/spaces/sengerchen/stable-virtual-camera)[🚀 gukim/seva ](https://huggingface.co/spaces/gukim/seva)[⚡ svjack/stable-virtual-camera ](https://huggingface.co/spaces/svjack/stable-virtual-camera)[⚡ mjohanes/stable-virtual-camera ](https://huggingface.co/spaces/mjohanes/stable-virtual-camera)[🚀 Hiepppp/stable-virtual-camera ](https://huggingface.co/spaces/Hiepppp/stable-virtual-camera)[⚡ chenmy0814/stable-virtual-camera ](https://huggingface.co/spaces/chenmy0814/stable-virtual-camera) + 6 Spaces + 3 Spaces
##  Paper for stabilityai/stable-virtual-camera
#### [Stable Virtual Camera: Generative View Synthesis with Diffusion Models Paper • 2503.14489 • Published Mar 18, 2025 • 3 ](https://huggingface.co/papers/2503.14489)
System theme
Company
[TOS](https://huggingface.co/terms-of-service) [Privacy](https://huggingface.co/privacy) [About](https://huggingface.co/huggingface) [Careers](https://apply.workable.com/huggingface/) [](https://huggingface.co/)
Website
[Models](https://huggingface.co/models) [Datasets](https://huggingface.co/datasets) [Spaces](https://huggingface.co/spaces) [Pricing](https://huggingface.co/pricing) [Docs](https://huggingface.co/docs)

