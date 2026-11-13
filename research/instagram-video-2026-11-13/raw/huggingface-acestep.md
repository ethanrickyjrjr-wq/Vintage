Source: https://huggingface.co/ACE-Step/ACE-Step-v1-3.5B (fetched 2026-11-13 with crawl4ai)

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
[ ![](https://cdn-avatars.huggingface.co/v1/production/uploads/6209bb6ede1c3ff3ec37620c/xk4TNYgu3UPz74tAgzTrA.jpeg) ](https://huggingface.co/ACE-Step)
[ACE-Step](https://huggingface.co/ACE-Step)
/
[ACE-Step-v1-3.5B](https://huggingface.co/ACE-Step/ACE-Step-v1-3.5B)
Like 757
Follow
![](https://cdn-avatars.huggingface.co/v1/production/uploads/6209bb6ede1c3ff3ec37620c/xk4TNYgu3UPz74tAgzTrA.jpeg) ACE-Step 1.36k
[ Text-to-Audio ](https://huggingface.co/models?pipeline_tag=text-to-audio)[ Diffusers ](https://huggingface.co/models?library=diffusers)[ Safetensors ](https://huggingface.co/models?library=safetensors)[ ACE-Step ](https://huggingface.co/models?library=acestep)
17 languages
[ music ](https://huggingface.co/models?other=music)[ text2music ](https://huggingface.co/models?other=text2music)
License: apache-2.0
[ Model card ](https://huggingface.co/ACE-Step/ACE-Step-v1-3.5B)[ Files Files and versions xet ](https://huggingface.co/ACE-Step/ACE-Step-v1-3.5B/tree/main)[ Community 19 ](https://huggingface.co/ACE-Step/ACE-Step-v1-3.5B/discussions)
Deploy
Copy to bucket
Use this model
### Instructions to use ACE-Step/ACE-Step-v1-3.5B with libraries, inference providers, notebooks, and local apps. Follow these links to get started.
  * Libraries
  * [ Diffusers](https://huggingface.co/ACE-Step/ACE-Step-v1-3.5B?library=diffusers)
How to use ACE-Step/ACE-Step-v1-3.5B with Diffusers:

```
pip install -U diffusers transformers accelerate
```

```
import torch
from diffusers import DiffusionPipeline

# switch to "mps" for apple devices
pipe = DiffusionPipeline.from_pretrained("ACE-Step/ACE-Step-v1-3.5B", dtype=torch.bfloat16, device_map="cuda")

prompt = "Astronaut in a jungle, cold color palette, muted colors, detailed, 8k"
image = pipe(prompt).images[0]
```

  * [ ACE-Step](https://huggingface.co/ACE-Step/ACE-Step-v1-3.5B?library=acestep)
How to use ACE-Step/ACE-Step-v1-3.5B with ACE-Step:

```
# No code snippets available yet for this library.

# To use this model, check the repository files and the library's documentation.

# Want to help? PRs adding snippets are welcome at:
# https://github.com/huggingface/huggingface.js
```

  * Notebooks
  * [ Google Colab](https://huggingface.co/ACE-Step/ACE-Step-v1-3.5B/colab)
  * [ Kaggle](https://huggingface.co/ACE-Step/ACE-Step-v1-3.5B/kaggle)


  * [ACE-Step: A Step Towards Music Generation Foundation Model](https://huggingface.co/ACE-Step/ACE-Step-v1-3.5B#ace-step-a-step-towards-music-generation-foundation-model "ACE-Step: A Step Towards Music Generation Foundation Model")
    * [Model Description](https://huggingface.co/ACE-Step/ACE-Step-v1-3.5B#model-description "Model Description")
    * [Uses](https://huggingface.co/ACE-Step/ACE-Step-v1-3.5B#uses "Uses")
      * [Direct Use](https://huggingface.co/ACE-Step/ACE-Step-v1-3.5B#direct-use "Direct Use")
      * [Downstream Use](https://huggingface.co/ACE-Step/ACE-Step-v1-3.5B#downstream-use "Downstream Use")
      * [Out-of-Scope Use](https://huggingface.co/ACE-Step/ACE-Step-v1-3.5B#out-of-scope-use "Out-of-Scope Use")
    * [How to Get Started](https://huggingface.co/ACE-Step/ACE-Step-v1-3.5B#how-to-get-started "How to Get Started")
    * [Hardware Performance](https://huggingface.co/ACE-Step/ACE-Step-v1-3.5B#hardware-performance "Hardware Performance")
    * [Limitations](https://huggingface.co/ACE-Step/ACE-Step-v1-3.5B#limitations "Limitations")
    * [Ethical Considerations](https://huggingface.co/ACE-Step/ACE-Step-v1-3.5B#ethical-considerations "Ethical Considerations")
    * [Model Details](https://huggingface.co/ACE-Step/ACE-Step-v1-3.5B#model-details "Model Details")
    * [Citation](https://huggingface.co/ACE-Step/ACE-Step-v1-3.5B#citation "Citation")
    * [Acknowledgements](https://huggingface.co/ACE-Step/ACE-Step-v1-3.5B#acknowledgements "Acknowledgements")


#  [ ](https://huggingface.co/ACE-Step/ACE-Step-v1-3.5B#ace-step-a-step-towards-music-generation-foundation-model) ACE-Step: A Step Towards Music Generation Foundation Model 
[![ACE-Step Framework](https://github.com/ACE-Step/ACE-Step/raw/main/assets/ACE-Step_framework.png)](https://github.com/ACE-Step/ACE-Step/raw/main/assets/ACE-Step_framework.png)
##  [ ](https://huggingface.co/ACE-Step/ACE-Step-v1-3.5B#model-description) Model Description 
ACE-Step is a novel open-source foundation model for music generation that overcomes key limitations of existing approaches through a holistic architectural design. It integrates diffusion-based generation with Sana's Deep Compression AutoEncoder (DCAE) and a lightweight linear transformer, achieving state-of-the-art performance in generation speed, musical coherence, and controllability.
**Key Features:**
  * 15× faster than LLM-based baselines (20s for 4-minute music on A100)
  * Superior musical coherence across melody, harmony, and rhythm
  * full-song generation, duration control and accepts natural language descriptions


##  [ ](https://huggingface.co/ACE-Step/ACE-Step-v1-3.5B#uses) Uses 
###  [ ](https://huggingface.co/ACE-Step/ACE-Step-v1-3.5B#direct-use) Direct Use 
ACE-Step can be used for:
  * Generating original music from text descriptions
  * Music remixing and style transfer
  * edit song lyrics


###  [ ](https://huggingface.co/ACE-Step/ACE-Step-v1-3.5B#downstream-use) Downstream Use 
The model serves as a foundation for:
  * Voice cloning applications
  * Specialized music generation (rap, jazz, etc.)
  * Music production tools
  * Creative AI assistants


###  [ ](https://huggingface.co/ACE-Step/ACE-Step-v1-3.5B#out-of-scope-use) Out-of-Scope Use 
The model should not be used for:
  * Generating copyrighted content without permission
  * Creating harmful or offensive content
  * Misrepresenting AI-generated music as human-created


##  [ ](https://huggingface.co/ACE-Step/ACE-Step-v1-3.5B#how-to-get-started) How to Get Started 
see: <https://github.com/ace-step/ACE-Step>
##  [ ](https://huggingface.co/ACE-Step/ACE-Step-v1-3.5B#hardware-performance) Hardware Performance   
| Device  | 27 Steps  | 60 Steps  |  
| --- | --- | --- |  
| NVIDIA A100  | 27.27x  | 12.27x  |  
| RTX 4090  | 34.48x  | 15.63x  |  
| RTX 3090  | 12.76x  | 6.48x  |  
| M2 Max  | 2.27x  | 1.03x  |  
_RTF (Real-Time Factor) shown - higher values indicate faster generation_
##  [ ](https://huggingface.co/ACE-Step/ACE-Step-v1-3.5B#limitations) Limitations 
  * Performance varies by language (top 10 languages perform best)
  * Longer generations (>5 minutes) may lose structural coherence
  * Rare instruments may not render perfectly
  * Output Inconsistency: Highly sensitive to random seeds and input duration, leading to varied "gacha-style" results.
  * Style-specific Weaknesses: Underperforms on certain genres (e.g. Chinese rap/zh_rap) Limited style adherence and musicality ceiling
  * Continuity Artifacts: Unnatural transitions in repainting/extend operations
  * Vocal Quality: Coarse vocal synthesis lacking nuance
  * Control Granularity: Needs finer-grained musical parameter control


##  [ ](https://huggingface.co/ACE-Step/ACE-Step-v1-3.5B#ethical-considerations) Ethical Considerations 
Users should:
  * Verify originality of generated works
  * Disclose AI involvement
  * Respect cultural elements and copyrights
  * Avoid harmful content generation


##  [ ](https://huggingface.co/ACE-Step/ACE-Step-v1-3.5B#model-details) Model Details 
**Developed by:** ACE Studio and StepFun  
**Model type:** Diffusion-based music generation with transformer conditioning  
**License:** Apache 2.0  
**Resources:**
  * [Project Page](https://ace-step.github.io/)
  * [Demo Space](https://huggingface.co/spaces/ACE-Step/ACE-Step)
  * [GitHub Repository](https://github.com/ACE-Step/ACE-Step)


##  [ ](https://huggingface.co/ACE-Step/ACE-Step-v1-3.5B#citation) Citation 

```
@misc{gong2025acestep,
  title={ACE-Step: A Step Towards Music Generation Foundation Model},
  author={Junmin Gong, Wenxiao Zhao, Sen Wang, Shengyuan Xu, Jing Guo}, 
  howpublished={\url{https://github.com/ace-step/ACE-Step}},
  year={2025},
  note={GitHub repository}
}

```

##  [ ](https://huggingface.co/ACE-Step/ACE-Step-v1-3.5B#acknowledgements) Acknowledgements 
This project is co-led by ACE Studio and StepFun. 

Downloads last month
    -
Inference Providers [NEW](https://huggingface.co/docs/inference-providers)
Text-to-Audio
This model isn't deployed by any Inference Provider. [🙋 22 Ask for provider support](https://huggingface.co/spaces/huggingface/InferenceSupport/discussions/1645)
##  Model tree for ACE-Step/ACE-Step-v1-3.5B [](https://huggingface.co/docs/hub/model-cards#specifying-a-base-model)
Adapters
[12 models](https://huggingface.co/models?other=base_model:adapter:ACE-Step/ACE-Step-v1-3.5B)
Finetunes
[3 models](https://huggingface.co/models?other=base_model:finetune:ACE-Step/ACE-Step-v1-3.5B)
Merges
[1 model](https://huggingface.co/models?other=base_model:merge:ACE-Step/ACE-Step-v1-3.5B)
Quantizations
[3 models](https://huggingface.co/models?other=base_model:quantized:ACE-Step/ACE-Step-v1-3.5B)
##  Spaces using ACE-Step/ACE-Step-v1-3.5B 47
[ ![](https://cdn-avatars.huggingface.co/v1/production/uploads/6209bb6ede1c3ff3ec37620c/xk4TNYgu3UPz74tAgzTrA.jpeg) ACE-Step/ACE-Step ](https://huggingface.co/spaces/ACE-Step/ACE-Step)[🎛️ Reubencf/Kiku-Engine ](https://huggingface.co/spaces/Reubencf/Kiku-Engine)[📚 eduagarcia/multilingual-tokenizer-leaderboard ](https://huggingface.co/spaces/eduagarcia/multilingual-tokenizer-leaderboard)[🎵 LububMusicAi/ACE-Step-Custom ](https://huggingface.co/spaces/LububMusicAi/ACE-Step-Custom)[🎤 Reubencf/Score-Studio ](https://huggingface.co/spaces/Reubencf/Score-Studio)[🎵 Gamahea/ACE-Step-Custom ](https://huggingface.co/spaces/Gamahea/ACE-Step-Custom)[🎤 Reubencf/Kiku-AI ](https://huggingface.co/spaces/Reubencf/Kiku-AI)[🎵 adowu/ACE-Step-Training ](https://huggingface.co/spaces/adowu/ACE-Step-Training) + 42 Spaces + 39 Spaces
System theme
Company
[TOS](https://huggingface.co/terms-of-service) [Privacy](https://huggingface.co/privacy) [About](https://huggingface.co/huggingface) [Careers](https://apply.workable.com/huggingface/) [](https://huggingface.co/)
Website
[Models](https://huggingface.co/models) [Datasets](https://huggingface.co/datasets) [Spaces](https://huggingface.co/spaces) [Pricing](https://huggingface.co/pricing) [Docs](https://huggingface.co/docs)
Inference providers allow you to run inference using different serverless providers.

