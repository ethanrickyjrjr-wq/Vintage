Source: https://huggingface.co/coqui/XTTS-v2 (fetched 2026-11-13 with crawl4ai)

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
[ ![](https://cdn-avatars.huggingface.co/v1/production/uploads/1648459271425-61dbf25b99eac69222659467.png) ](https://huggingface.co/coqui)
[coqui](https://huggingface.co/coqui)
/
[XTTS-v2](https://huggingface.co/coqui/XTTS-v2)
Like 3.96k
Follow
![](https://cdn-avatars.huggingface.co/v1/production/uploads/1648459271425-61dbf25b99eac69222659467.png) Coqui.ai 1.13k
[ Text-to-Speech ](https://huggingface.co/models?pipeline_tag=text-to-speech)[ coqui ](https://huggingface.co/models?other=coqui)
License: coqui-public-model-license
[ Model card ](https://huggingface.co/coqui/XTTS-v2)[ Files Files and versions xet ](https://huggingface.co/coqui/XTTS-v2/tree/main)[ Community 151 ](https://huggingface.co/coqui/XTTS-v2/discussions)
Copy to bucket
**Configuration Parsing Warning:** Invalid JSON for config file config.json
  * [ⓍTTS](https://huggingface.co/coqui/XTTS-v2#%E2%93%A7tts "ⓍTTS")
    * [Features](https://huggingface.co/coqui/XTTS-v2#features "Features")
    * [Updates over XTTS-v1](https://huggingface.co/coqui/XTTS-v2#updates-over-xtts-v1 "Updates over XTTS-v1")
    * [Languages](https://huggingface.co/coqui/XTTS-v2#languages "Languages")
    * [Code](https://huggingface.co/coqui/XTTS-v2#code "Code")
    * [Demo Spaces](https://huggingface.co/coqui/XTTS-v2#demo-spaces "Demo Spaces")
    * [License](https://huggingface.co/coqui/XTTS-v2#license "License")
    * [Contact](https://huggingface.co/coqui/XTTS-v2#contact "Contact")


#  [ ](https://huggingface.co/coqui/XTTS-v2#%E2%93%A7tts) ⓍTTS 
ⓍTTS is a Voice generation model that lets you clone voices into different languages by using just a quick 6-second audio clip. There is no need for an excessive amount of training data that spans countless hours.
This is the same or similar model to what powers [Coqui Studio](https://coqui.ai/) and [Coqui API](https://docs.coqui.ai/docs).
###  [ ](https://huggingface.co/coqui/XTTS-v2#features) Features 
  * Supports 17 languages. 
  * Voice cloning with just a 6-second audio clip.
  * Emotion and style transfer by cloning. 
  * Cross-language voice cloning.
  * Multi-lingual speech generation.
  * 24khz sampling rate.


###  [ ](https://huggingface.co/coqui/XTTS-v2#updates-over-xtts-v1) Updates over XTTS-v1 
  * 2 new languages; Hungarian and Korean
  * Architectural improvements for speaker conditioning.
  * Enables the use of multiple speaker references and interpolation between speakers.
  * Stability improvements.
  * Better prosody and audio quality across the board.


###  [ ](https://huggingface.co/coqui/XTTS-v2#languages) Languages 
XTTS-v2 supports 17 languages: **English (en), Spanish (es), French (fr), German (de), Italian (it), Portuguese (pt), Polish (pl), Turkish (tr), Russian (ru), Dutch (nl), Czech (cs), Arabic (ar), Chinese (zh-cn), Japanese (ja), Hungarian (hu), Korean (ko) Hindi (hi)**.
Stay tuned as we continue to add support for more languages. If you have any language requests, feel free to reach out!
###  [ ](https://huggingface.co/coqui/XTTS-v2#code) Code 
The [code-base](https://github.com/coqui-ai/TTS) supports inference and [fine-tuning](https://tts.readthedocs.io/en/latest/models/xtts.html#training).
###  [ ](https://huggingface.co/coqui/XTTS-v2#demo-spaces) Demo Spaces 
  * [XTTS Space](https://huggingface.co/spaces/coqui/xtts) : You can see how model performs on supported languages, and try with your own reference or microphone input
  * [XTTS Voice Chat with Mistral or Zephyr](https://huggingface.co/spaces/coqui/voice-chat-with-mistral) : You can experience streaming voice chat with Mistral 7B Instruct or Zephyr 7B Beta

  
|   |   |  
| --- | --- |  
| 🐸💬 **CoquiTTS**  | [coqui/TTS on Github](https://github.com/coqui-ai/TTS)  |  
| 💼 **Documentation**  | [ReadTheDocs](https://tts.readthedocs.io/en/latest/)  |  
| 👩‍💻 **Questions**  | [GitHub Discussions](https://github.com/coqui-ai/TTS/discussions)  |  
| 🗯 **Community**  | [Discord](https://discord.gg/5eXr5seRrv)  |  
###  [ ](https://huggingface.co/coqui/XTTS-v2#license) License 
This model is licensed under [Coqui Public Model License](https://coqui.ai/cpml). There's a lot that goes into a license for generative models, and you can read more of [the origin story of CPML here](https://coqui.ai/blog/tts/cpml).
###  [ ](https://huggingface.co/coqui/XTTS-v2#contact) Contact 
Come and join in our 🐸Community. We're active on [Discord](https://discord.gg/fBC58unbKE) and [Twitter](https://twitter.com/coqui_ai). You can also mail us at info@coqui.ai.
Using 🐸TTS API:

```
from TTS.api import TTS
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=True)

# generate speech by cloning a voice using default settings
tts.tts_to_file(text="It took me quite a long time to develop a voice, and now that I have it I'm not going to be silent.",
                file_path="output.wav",
                speaker_wav="/path/to/target/speaker.wav",
                language="en")

```

Using 🐸TTS Command line:

```
 tts --model_name tts_models/multilingual/multi-dataset/xtts_v2 \
     --text "Bugün okula gitmek istemiyorum." \
     --speaker_wav /path/to/target/speaker.wav \
     --language_idx tr \
     --use_cuda true

```

Using the model directly:

```
from TTS.tts.configs.xtts_config import XttsConfig
from TTS.tts.models.xtts import Xtts

config = XttsConfig()
config.load_json("/path/to/xtts/config.json")
model = Xtts.init_from_config(config)
model.load_checkpoint(config, checkpoint_dir="/path/to/xtts/", eval=True)
model.cuda()

outputs = model.synthesize(
    "It took me quite a long time to develop a voice and now that I have it I am not going to be silent.",
    config,
    speaker_wav="/data/TTS-public/_refclips/3.wav",
    gpt_cond_len=3,
    language="en",
)

```


Downloads last month
    5,492,387
Inference Providers [NEW](https://huggingface.co/docs/inference-providers)
[ Text-to-Speech ](https://huggingface.co/tasks/text-to-speech "Learn more about text-to-speech")
This model isn't deployed by any Inference Provider. [🙋 1 Ask for provider support](https://huggingface.co/spaces/huggingface/InferenceSupport/discussions/199)
##  Model tree for coqui/XTTS-v2 [](https://huggingface.co/docs/hub/model-cards#specifying-a-base-model)
Adapters
[1 model](https://huggingface.co/models?other=base_model:adapter:coqui/XTTS-v2)
Finetunes
[84 models](https://huggingface.co/models?other=base_model:finetune:coqui/XTTS-v2)
Merges
[1 model](https://huggingface.co/models?other=base_model:merge:coqui/XTTS-v2)
Quantizations
[3 models](https://huggingface.co/models?other=base_model:quantized:coqui/XTTS-v2)
##  Spaces using coqui/XTTS-v2 100
[ ![](https://cdn-avatars.huggingface.co/v1/production/uploads/1648459271425-61dbf25b99eac69222659467.png) coqui/xtts ](https://huggingface.co/spaces/coqui/xtts)[ ![](https://cdn-avatars.huggingface.co/v1/production/uploads/1648459271425-61dbf25b99eac69222659467.png) coqui/voice-chat-with-mistral ](https://huggingface.co/spaces/coqui/voice-chat-with-mistral)[📈 emanforhelp/model-pulse ](https://huggingface.co/spaces/emanforhelp/model-pulse)[🤗🏆 Pendrokar/TTS-Spaces-Arena ](https://huggingface.co/spaces/Pendrokar/TTS-Spaces-Arena)[🟩 embedl/hfviewer ](https://huggingface.co/spaces/embedl/hfviewer)[🚀 hasanbasbunar/Voice-Cloning-XTTS-v2 ](https://huggingface.co/spaces/hasanbasbunar/Voice-Cloning-XTTS-v2)[🎙️ Nouira-Oussema/TTS-Tounsi ](https://huggingface.co/spaces/Nouira-Oussema/TTS-Tounsi)[🔊 eustlb/tts-models-on-the-hub ](https://huggingface.co/spaces/eustlb/tts-models-on-the-hub) + 95 Spaces + 92 Spaces
System theme
Company
[TOS](https://huggingface.co/terms-of-service) [Privacy](https://huggingface.co/privacy) [About](https://huggingface.co/huggingface) [Careers](https://apply.workable.com/huggingface/) [](https://huggingface.co/)
Website
[Models](https://huggingface.co/models) [Datasets](https://huggingface.co/datasets) [Spaces](https://huggingface.co/spaces) [Pricing](https://huggingface.co/pricing) [Docs](https://huggingface.co/docs)

