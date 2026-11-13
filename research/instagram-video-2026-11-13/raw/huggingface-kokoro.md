Source: https://huggingface.co/hexgrad/Kokoro-82M (fetched 2026-11-13 with crawl4ai)

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
[ ![](https://cdn-avatars.huggingface.co/v1/production/uploads/6629552c96f529a39bac7c89/EaoEz4WH2VoE5twl2oJie.png) ](https://huggingface.co/hexgrad)
[hexgrad](https://huggingface.co/hexgrad)
/
[Kokoro-82M](https://huggingface.co/hexgrad/Kokoro-82M)
Like 7.41k
[ Text-to-Speech ](https://huggingface.co/models?pipeline_tag=text-to-speech)[ English ](https://huggingface.co/models?language=en)
doi:10.57967/hf/4329
arxiv: 2306.07691
arxiv: 2203.02395
License: apache-2.0
[ Model card ](https://huggingface.co/hexgrad/Kokoro-82M)[ Files Files and versions xet ](https://huggingface.co/hexgrad/Kokoro-82M/tree/main)
Deploy
Copy to bucket
Use this model
### Instructions to use hexgrad/Kokoro-82M with libraries, inference providers, notebooks, and local apps. Follow these links to get started.
  * Inference
  * Inference Providers
  * Notebooks
  * [ Google Colab](https://huggingface.co/hexgrad/Kokoro-82M/colab)
  * [ Kaggle](https://huggingface.co/hexgrad/Kokoro-82M/kaggle)


  * [Releases](https://huggingface.co/hexgrad/Kokoro-82M#releases "Releases")
  * [Usage](https://huggingface.co/hexgrad/Kokoro-82M#usage "Usage")
  * [Model Facts](https://huggingface.co/hexgrad/Kokoro-82M#model-facts "Model Facts")
  * [Training Details](https://huggingface.co/hexgrad/Kokoro-82M#training-details "Training Details")
  * [Creative Commons Attribution](https://huggingface.co/hexgrad/Kokoro-82M#creative-commons-attribution "Creative Commons Attribution")
  * [Acknowledgements](https://huggingface.co/hexgrad/Kokoro-82M#acknowledgements "Acknowledgements")


**Kokoro** is an open-weight TTS model with 82 million parameters. Despite its lightweight architecture, it delivers comparable quality to larger models while being significantly faster and more cost-efficient. With Apache-licensed weights, Kokoro can be deployed anywhere from production environments to personal projects.
🐈 **GitHub** : <https://github.com/hexgrad/kokoro>
🚀 **Demo** : <https://hf.co/spaces/hexgrad/Kokoro-TTS>
> As of April 2025, the market rate of Kokoro served over API is **under $1 per million characters of text input** , or under $0.06 per hour of audio output. (On average, 1000 characters of input is about 1 minute of output.) Sources: [ArtificialAnalysis/Replicate at 65 cents per M chars](https://artificialanalysis.ai/text-to-speech/model-family/kokoro#price) and [DeepInfra at 80 cents per M chars](https://deepinfra.com/hexgrad/Kokoro-82M).
> This is an Apache-licensed model, and Kokoro has been deployed in numerous projects and commercial APIs. We welcome the deployment of the model in real use cases.
> Fake websites like kokorottsai_com (snapshot: <https://archive.ph/nRRnk>) and kokorotts_net (snapshot: <https://archive.ph/60opa>) are likely scams masquerading under the banner of a popular model.
> Any website containing "kokoro" in its root domain (e.g. kokorottsai_com, kokorotts_net) is **NOT owned by and NOT affiliated with this model page or its author** , and attempts to imply otherwise are red flags.
  * [Releases](https://huggingface.co/hexgrad/Kokoro-82M#releases)
  * [Usage](https://huggingface.co/hexgrad/Kokoro-82M#usage)
  * [EVAL.md](https://huggingface.co/hexgrad/Kokoro-82M/blob/main/EVAL.md) ↗️
  * [SAMPLES.md](https://huggingface.co/hexgrad/Kokoro-82M/blob/main/SAMPLES.md) ↗️
  * [VOICES.md](https://huggingface.co/hexgrad/Kokoro-82M/blob/main/VOICES.md) ↗️
  * [Model Facts](https://huggingface.co/hexgrad/Kokoro-82M#model-facts)
  * [Training Details](https://huggingface.co/hexgrad/Kokoro-82M#training-details)
  * [Creative Commons Attribution](https://huggingface.co/hexgrad/Kokoro-82M#creative-commons-attribution)
  * [Acknowledgements](https://huggingface.co/hexgrad/Kokoro-82M#acknowledgements)


###  [ ](https://huggingface.co/hexgrad/Kokoro-82M#releases) Releases   
| Model  | Published  | Training Data  | Langs & Voices  | SHA256  |  
| --- | --- | --- | --- | --- |  
| **v1.0**  | **2025 Jan 27**  | **Few hundred hrs**  | [**8 & 54**](https://huggingface.co/hexgrad/Kokoro-82M/blob/main/VOICES.md)  | `496dba11`  |  
| [v0.19](https://huggingface.co/hexgrad/kLegacy/tree/main/v0.19)  | 2024 Dec 25  | <100 hrs  | 1 & 10  | `3b0c392f`  |  
| Training Costs  | v0.19  | v1.0  | **Total**  |  
| --- | --- | --- | --- |  
| in A100 80GB GPU hours  | 500  | 500  | **1000**  |  
| average hourly rate  | $0.80/h  | $1.20/h  | **$1/h**  |  
| in USD  | $400  | $600  | **$1000**  |  
###  [ ](https://huggingface.co/hexgrad/Kokoro-82M#usage) Usage 
You can run this basic cell on [Google Colab](https://colab.research.google.com/). [Listen to samples](https://huggingface.co/hexgrad/Kokoro-82M/blob/main/SAMPLES.md). For more languages and details, see [Advanced Usage](https://github.com/hexgrad/kokoro?tab=readme-ov-file#advanced-usage).

```
!pip install -q kokoro>=0.9.2 soundfile
!apt-get -qq -y install espeak-ng > /dev/null 2>&1
from kokoro import KPipeline
from IPython.display import display, Audio
import soundfile as sf
import torch
pipeline = KPipeline(lang_code='a')
text = '''
[Kokoro](/kˈOkəɹO/) is an open-weight TTS model with 82 million parameters. Despite its lightweight architecture, it delivers comparable quality to larger models while being significantly faster and more cost-efficient. With Apache-licensed weights, [Kokoro](/kˈOkəɹO/) can be deployed anywhere from production environments to personal projects.
'''
generator = pipeline(text, voice='af_heart')
for i, (gs, ps, audio) in enumerate(generator):
    print(i, gs, ps)
    display(Audio(data=audio, rate=24000, autoplay=i==0))
    sf.write(f'{i}.wav', audio, 24000)

```

Under the hood, `kokoro` uses [`misaki`](https://pypi.org/project/misaki/), a G2P library at <https://github.com/hexgrad/misaki>
###  [ ](https://huggingface.co/hexgrad/Kokoro-82M#model-facts) Model Facts 
**Architecture:**
  * StyleTTS 2: <https://arxiv.org/abs/2306.07691>
  * ISTFTNet: <https://arxiv.org/abs/2203.02395>
  * Decoder only: no diffusion, no encoder release


**Architected by:** Li et al @ <https://github.com/yl4579/StyleTTS2>
**Trained by** : `@rzvzn` on Discord
**Languages:** Multiple
**Model SHA256 Hash:** `496dba118d1a58f5f3db2efc88dbdc216e0483fc89fe6e47ee1f2c53f18ad1e4`
###  [ ](https://huggingface.co/hexgrad/Kokoro-82M#training-details) Training Details 
**Data:** Kokoro was trained exclusively on **permissive/non-copyrighted audio data** and IPA phoneme labels. Examples of permissive/non-copyrighted audio include:
  * Public domain audio
  * Audio licensed under Apache, MIT, etc
  * Synthetic audio[1] generated by closed[2] TTS models from large providers  
[1] <https://copyright.gov/ai/ai_policy_guidance.pdf>  
[2] No synthetic audio from open TTS models or "custom voice clones"


**Total Dataset Size:** A few hundred hours of audio
**Total Training Cost:** About $1000 for 1000 hours of A100 80GB vRAM
###  [ ](https://huggingface.co/hexgrad/Kokoro-82M#creative-commons-attribution) Creative Commons Attribution 
The following CC BY audio was part of the dataset used to train Kokoro v1.0.  
| Audio Data  | Duration Used  | License  | Added to Training Set After  |  
| --- | --- | --- | --- |  
|  [Koniwa](https://github.com/koniwa/koniwa) `tnc`  | <1h  | [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/deed.ja)  | v0.19 / 22 Nov 2024  |  
| [SIWIS](https://datashare.ed.ac.uk/handle/10283/2353)  | <11h  | [CC BY 4.0](https://datashare.ed.ac.uk/bitstream/handle/10283/2353/license_text)  | v0.19 / 22 Nov 2024  |  
###  [ ](https://huggingface.co/hexgrad/Kokoro-82M#acknowledgements) Acknowledgements 
  * 🛠️ [@yl4579](https://huggingface.co/yl4579) for architecting StyleTTS 2.
  * 🏆 [@Pendrokar](https://huggingface.co/Pendrokar) for adding Kokoro as a contender in the TTS Spaces Arena.
  * 📊 Thank you to everyone who contributed synthetic training data.
  * ❤️ Special thanks to all compute sponsors.
  * 👾 Discord server: <https://discord.gg/QuGxSWBfQy>
  * 🪽 Kokoro is a Japanese word that translates to "heart" or "spirit". It is also the name of an [AI in the Terminator franchise](https://terminator.fandom.com/wiki/Kokoro).

![kokoro](https://static0.gamerantimages.com/wordpress/wp-content/uploads/2024/08/terminator-zero-41-1.jpg) 

Downloads last month
    12,580,963
Inference Providers [NEW](https://huggingface.co/docs/inference-providers)
DeepInfra
  * 

[ Text-to-Speech ](https://huggingface.co/tasks/text-to-speech "Learn more about text-to-speech")
Generate
View Code Snippets
Maximize
##  Model tree for hexgrad/Kokoro-82M [](https://huggingface.co/docs/hub/model-cards#specifying-a-base-model)
Base model
[yl4579/StyleTTS2-LJSpeech](https://huggingface.co/yl4579/StyleTTS2-LJSpeech)
Finetuned
([71](https://huggingface.co/models?other=base_model:finetune:yl4579/StyleTTS2-LJSpeech))
this model
Adapters
[12 models](https://huggingface.co/models?other=base_model:adapter:hexgrad/Kokoro-82M)
Finetunes
[74 models](https://huggingface.co/models?other=base_model:finetune:hexgrad/Kokoro-82M)
Quantizations
[121 models](https://huggingface.co/models?other=base_model:quantized:hexgrad/Kokoro-82M)
##  Spaces using hexgrad/Kokoro-82M 100
[ ![](https://cdn-avatars.huggingface.co/v1/production/uploads/6629552c96f529a39bac7c89/EaoEz4WH2VoE5twl2oJie.png) hexgrad/Kokoro-TTS ](https://huggingface.co/spaces/hexgrad/Kokoro-TTS)[🗣️ hf-audio/open_tts_leaderboard ](https://huggingface.co/spaces/hf-audio/open_tts_leaderboard)[📈 emanforhelp/model-pulse ](https://huggingface.co/spaces/emanforhelp/model-pulse)[🤗🏆 Pendrokar/TTS-Spaces-Arena ](https://huggingface.co/spaces/Pendrokar/TTS-Spaces-Arena)[🎴 remsky/Kokoro-TTS-Zero ](https://huggingface.co/spaces/remsky/Kokoro-TTS-Zero)[🟩 embedl/hfviewer ](https://huggingface.co/spaces/embedl/hfviewer)[🐦 sahilmahendrakar/paradee ](https://huggingface.co/spaces/sahilmahendrakar/paradee)[🗣️ Sammy-Mohan/kannada-tts ](https://huggingface.co/spaces/Sammy-Mohan/kannada-tts) + 95 Spaces + 92 Spaces
##  Papers for hexgrad/Kokoro-82M
#### [StyleTTS 2: Towards Human-Level Text-to-Speech through Style Diffusion and Adversarial Training with Large Speech Language Models Paper • 2306.07691 • Published Jun 13, 2023 • 19 ](https://huggingface.co/papers/2306.07691)#### [iSTFTNet: Fast and Lightweight Mel-Spectrogram Vocoder Incorporating Inverse Short-Time Fourier Transform Paper • 2203.02395 • Published Mar 4, 2022 • 2 ](https://huggingface.co/papers/2203.02395)
System theme
Company
[TOS](https://huggingface.co/terms-of-service) [Privacy](https://huggingface.co/privacy) [About](https://huggingface.co/huggingface) [Careers](https://apply.workable.com/huggingface/) [](https://huggingface.co/)
Website
[Models](https://huggingface.co/models) [Datasets](https://huggingface.co/datasets) [Spaces](https://huggingface.co/spaces) [Pricing](https://huggingface.co/pricing) [Docs](https://huggingface.co/docs)

