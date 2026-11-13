Source: https://huggingface.co/stabilityai/stable-audio-open-1.0 (fetched 2026-11-13 with crawl4ai)

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
[stable-audio-open-1.0](https://huggingface.co/stabilityai/stable-audio-open-1.0)
Like 1.95k
Follow
![](https://cdn-avatars.huggingface.co/v1/production/uploads/643feeb67bc3fbde1385cc25/7vmYr2XwVcPtkLzac_jxQ.png) Stability AI 40.7k
[ Text-to-Audio ](https://huggingface.co/models?pipeline_tag=text-to-audio)[ Stable Audio Tools ](https://huggingface.co/models?library=stable-audio-tools)[ Diffusers ](https://huggingface.co/models?library=diffusers)[ Safetensors ](https://huggingface.co/models?library=safetensors)[ English ](https://huggingface.co/models?language=en)
arxiv: 2407.14358
License: stable-audio-community
[ Model card ](https://huggingface.co/stabilityai/stable-audio-open-1.0)[ Files Files and versions xet ](https://huggingface.co/stabilityai/stable-audio-open-1.0/tree/main)[ Community 65 ](https://huggingface.co/stabilityai/stable-audio-open-1.0/discussions)
Deploy
Copy to bucket
Use this model
### Instructions to use stabilityai/stable-audio-open-1.0 with libraries, inference providers, notebooks, and local apps. Follow these links to get started.
  * Libraries
  * [ Stable Audio Tools](https://huggingface.co/stabilityai/stable-audio-open-1.0?library=stable-audio-tools)
How to use stabilityai/stable-audio-open-1.0 with Stable Audio Tools:

```
import torch
import torchaudio
from einops import rearrange
from stable_audio_tools import get_pretrained_model
from stable_audio_tools.inference.generation import generate_diffusion_cond

device = "cuda" if torch.cuda.is_available() else "cpu"

# Download model
model, model_config = get_pretrained_model("stabilityai/stable-audio-open-1.0")
sample_rate = model_config["sample_rate"]
sample_size = model_config["sample_size"]

model = model.to(device)

# Set up text and timing conditioning
conditioning = [{
	"prompt": "128 BPM tech house drum loop",
}]

# Generate stereo audio
output = generate_diffusion_cond(
	model,
	conditioning=conditioning,
	sample_size=sample_size,
	device=device
)

# Rearrange audio batch to a single sequence
output = rearrange(output, "b d n -> d (b n)")

# Peak normalize, clip, convert to int16, and save to file
output = output.to(torch.float32).div(torch.max(torch.abs(output))).clamp(-1, 1).mul(32767).to(torch.int16).cpu()
torchaudio.save("output.wav", output, sample_rate)
```

  * Notebooks
  * [ Google Colab](https://huggingface.co/stabilityai/stable-audio-open-1.0/colab)
  * [ Kaggle](https://huggingface.co/stabilityai/stable-audio-open-1.0/kaggle)


##  You need to agree to share your Hugging Face information to access this model
This repository is publicly accessible, but you have to accept the conditions to access its files and content.
By clicking "Agree", you agree to the [License Agreement](https://huggingface.co/stabilityai/stable-audio-open-1.0/blob/main/LICENSE.md) and acknowledge Stability AI's [Privacy Policy](https://stability.ai/privacy-policy).
[Log in](https://huggingface.co/login?next=/stabilityai/stable-audio-open-1.0) or [Sign Up](https://huggingface.co/join?next=/stabilityai/stable-audio-open-1.0) to review the conditions and access this model content.
  * [Stable Audio Open 1.0](https://huggingface.co/stabilityai/stable-audio-open-1.0#stable-audio-open-10 "Stable Audio Open 1.0")
    * [Model Description](https://huggingface.co/stabilityai/stable-audio-open-1.0#model-description "Model Description")
    * [Usage](https://huggingface.co/stabilityai/stable-audio-open-1.0#usage "Usage")
      * [Using with `stable-audio-tools`](https://huggingface.co/stabilityai/stable-audio-open-1.0#using-with-stable-audio-tools "Using with <code>stable-audio-tools</code>")
    * [Using with `diffusers`](https://huggingface.co/stabilityai/stable-audio-open-1.0#using-with-diffusers "Using with <code>diffusers</code>")
    * [Model Details](https://huggingface.co/stabilityai/stable-audio-open-1.0#model-details "Model Details")
    * [Training dataset](https://huggingface.co/stabilityai/stable-audio-open-1.0#training-dataset "Training dataset")
      * [Datasets Used](https://huggingface.co/stabilityai/stable-audio-open-1.0#datasets-used "Datasets Used")
      * [Attribution](https://huggingface.co/stabilityai/stable-audio-open-1.0#attribution "Attribution")
      * [Mitigations](https://huggingface.co/stabilityai/stable-audio-open-1.0#mitigations "Mitigations")
    * [Use and Limitations](https://huggingface.co/stabilityai/stable-audio-open-1.0#use-and-limitations "Use and Limitations")
      * [Intended Use](https://huggingface.co/stabilityai/stable-audio-open-1.0#intended-use "Intended Use")
      * [Out-of-Scope Use Cases](https://huggingface.co/stabilityai/stable-audio-open-1.0#out-of-scope-use-cases "Out-of-Scope Use Cases")
      * [Limitations](https://huggingface.co/stabilityai/stable-audio-open-1.0#limitations "Limitations")
      * [Biases](https://huggingface.co/stabilityai/stable-audio-open-1.0#biases "Biases")


#  [ ](https://huggingface.co/stabilityai/stable-audio-open-1.0#stable-audio-open-10) Stable Audio Open 1.0 
[![Stable Audio Open logo](https://huggingface.co/stabilityai/stable-audio-open-1.0/media/main/stable_audio_light.png)](https://huggingface.co/stabilityai/stable-audio-open-1.0/blob/main/stable_audio_light.png)
Please note: For commercial use, please refer to <https://stability.ai/license>
##  [ ](https://huggingface.co/stabilityai/stable-audio-open-1.0#model-description) Model Description 
`Stable Audio Open 1.0` generates variable-length (up to 47s) stereo audio at 44.1kHz from text prompts. It comprises three components: an autoencoder that compresses waveforms into a manageable sequence length, a T5-based text embedding for text conditioning, and a transformer-based diffusion (DiT) model that operates in the latent space of the autoencoder.
##  [ ](https://huggingface.co/stabilityai/stable-audio-open-1.0#usage) Usage 
This model can be used with:
  1. the [`stable-audio-tools`](https://github.com/Stability-AI/stable-audio-tools) library
  2. the [`diffusers`](https://huggingface.co/docs/diffusers/main/en/index) library


###  [ ](https://huggingface.co/stabilityai/stable-audio-open-1.0#using-with-stable-audio-tools) Using with `stable-audio-tools`
This model is made to be used with the [`stable-audio-tools`](https://github.com/Stability-AI/stable-audio-tools) library for inference, for example:

```
import torch
import torchaudio
from einops import rearrange
from stable_audio_tools import get_pretrained_model
from stable_audio_tools.inference.generation import generate_diffusion_cond

device = "cuda" if torch.cuda.is_available() else "cpu"

# Download model
model, model_config = get_pretrained_model("stabilityai/stable-audio-open-1.0")
sample_rate = model_config["sample_rate"]
sample_size = model_config["sample_size"]

model = model.to(device)

# Set up text and timing conditioning
conditioning = [{
    "prompt": "128 BPM tech house drum loop",
    "seconds_start": 0, 
    "seconds_total": 30
}]

# Generate stereo audio
output = generate_diffusion_cond(
    model,
    steps=100,
    cfg_scale=7,
    conditioning=conditioning,
    sample_size=sample_size,
    sigma_min=0.3,
    sigma_max=500,
    sampler_type="dpmpp-3m-sde",
    device=device
)

# Rearrange audio batch to a single sequence
output = rearrange(output, "b d n -> d (b n)")

# Peak normalize, clip, convert to int16, and save to file
output = output.to(torch.float32).div(torch.max(torch.abs(output))).clamp(-1, 1).mul(32767).to(torch.int16).cpu()
torchaudio.save("output.wav", output, sample_rate)

```

##  [ ](https://huggingface.co/stabilityai/stable-audio-open-1.0#using-with-diffusers) Using with `diffusers`
Make sure you upgrade to the latest version of diffusers: `pip install -U diffusers`. And then you can run:

```
import torch
import soundfile as sf
from diffusers import StableAudioPipeline

pipe = StableAudioPipeline.from_pretrained("stabilityai/stable-audio-open-1.0", torch_dtype=torch.float16)
pipe = pipe.to("cuda")

# define the prompts
prompt = "The sound of a hammer hitting a wooden surface."
negative_prompt = "Low quality."

# set the seed for generator
generator = torch.Generator("cuda").manual_seed(0)

# run the generation
audio = pipe(
    prompt,
    negative_prompt=negative_prompt,
    num_inference_steps=200,
    audio_end_in_s=10.0,
    num_waveforms_per_prompt=3,
    generator=generator,
).audios

output = audio[0].T.float().cpu().numpy()
sf.write("hammer.wav", output, pipe.vae.sampling_rate)

```

Refer to the [documentation](https://huggingface.co/docs/diffusers/main/en/index) for more details on optimization and usage.
##  [ ](https://huggingface.co/stabilityai/stable-audio-open-1.0#model-details) Model Details 
  * **Model type** : `Stable Audio Open 1.0` is a latent diffusion model based on a transformer architecture.
  * **Language(s)** : English
  * **License** : [Stability AI Community License](https://huggingface.co/stabilityai/stable-audio-open-1.0/blob/main/LICENSE.md).
  * **Commercial License** : to use this model commercially, please refer to <https://stability.ai/license>
  * **Research Paper** : <https://arxiv.org/abs/2407.14358>


##  [ ](https://huggingface.co/stabilityai/stable-audio-open-1.0#training-dataset) Training dataset 
###  [ ](https://huggingface.co/stabilityai/stable-audio-open-1.0#datasets-used) Datasets Used 
Our dataset consists of 486492 audio recordings, where 472618 are from Freesound and 13874 are from the Free Music Archive (FMA). All audio files are licensed under CC0, CC BY, or CC Sampling+. This data is used to train our autoencoder and DiT. We use a publicly available pre-trained T5 model ([t5-base](https://huggingface.co/google-t5/t5-base)) for text conditioning.
###  [ ](https://huggingface.co/stabilityai/stable-audio-open-1.0#attribution) Attribution 
Attribution for all audio recordings used to train Stable Audio Open 1.0 can be found on our [attribution page](https://info.stability.ai/attributions).
###  [ ](https://huggingface.co/stabilityai/stable-audio-open-1.0#mitigations) Mitigations 
We conducted an in-depth analysis to ensure no unauthorized copyrighted music was present in our training data before we began training.
To that end, we first identified music samples in Freesound using the [PANNs](https://github.com/qiuqiangkong/audioset_tagging_cnn) music classifier based on AudioSet classes. The identified music samples had at least 30 seconds of music that was predicted to belong to a music-related class with a threshold of 0.15 (PANNs output probabilities range from 0 to 1). This threshold was determined by classifying known music examples from FMA and ensuring no false negatives were present. 
The identified music samples were sent to Audible Magic’s identification services, a trusted content detection company, to ensure the absence of copyrighted music. Audible Magic flagged suspected copyrighted music, which we subsequently removed before training on the dataset. The majority of the removed content was field recordings in which copyrighted music was playing in the background. Following this procedure, we were left with 266324 CC0, 194840 CC-BY, and 11454 CC Sampling+ audio recordings.
We also conducted an in-depth analysis to ensure no copyrighted content was present in FMA's subset. In this case, the procedure was slightly different because the FMA subset consists of music signals. We did a metadata search against a large database of copyrighted music (<https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset>) and flagged any potential match. The flagged content was reviewed individually by humans. After this process, we ended up with 8967 CC-BY and 4907 CC0 tracks.
##  [ ](https://huggingface.co/stabilityai/stable-audio-open-1.0#use-and-limitations) Use and Limitations 
###  [ ](https://huggingface.co/stabilityai/stable-audio-open-1.0#intended-use) Intended Use 
The primary use of Stable Audio Open is research and experimentation on AI-based music and audio generation, including:
  * Research efforts to better understand the limitations of generative models and further improve the state of science.
  * Generation of music and audio guided by text to explore current abilities of generative AI models by machine learning practitioners and artists.


###  [ ](https://huggingface.co/stabilityai/stable-audio-open-1.0#out-of-scope-use-cases) Out-of-Scope Use Cases 
The model should not be used on downstream applications without further risk evaluation and mitigation. The model should not be used to intentionally create or disseminate audio or music pieces that create hostile or alienating environments for people.
###  [ ](https://huggingface.co/stabilityai/stable-audio-open-1.0#limitations) Limitations 
  * The model is not able to generate realistic vocals.
  * The model has been trained with English descriptions and will not perform as well in other languages.
  * The model does not perform equally well for all music styles and cultures.
  * The model is better at generating sound effects and field recordings than music.
  * It is sometimes difficult to assess what types of text descriptions provide the best generations. Prompt engineering may be required to obtain satisfying results.


###  [ ](https://huggingface.co/stabilityai/stable-audio-open-1.0#biases) Biases 
The source of data is potentially lacking diversity and all cultures are not equally represented in the dataset. The model may not perform equally well on the wide variety of music genres and sound effects that exist. The generated samples from the model will reflect the biases from the training data. 

Downloads last month
    24,904
Safetensors[](https://huggingface.co/docs/safetensors)
Model size
1B params
Tensor type
F32 
·
Files info
Inference Providers [NEW](https://huggingface.co/docs/inference-providers)
Text-to-Audio
This model isn't deployed by any Inference Provider. [🙋 13 Ask for provider support](https://huggingface.co/spaces/huggingface/InferenceSupport/discussions/27)
##  Model tree for stabilityai/stable-audio-open-1.0 [](https://huggingface.co/docs/hub/model-cards#specifying-a-base-model)
Finetunes
[23 models](https://huggingface.co/models?other=base_model:finetune:stabilityai/stable-audio-open-1.0)
##  Spaces using stabilityai/stable-audio-open-1.0 100
[🐠 fantaxy/Sound-AI-SFX ](https://huggingface.co/spaces/fantaxy/Sound-AI-SFX)[🔥 artificialguybr/Stable-Audio-Open-Zero ](https://huggingface.co/spaces/artificialguybr/Stable-Audio-Open-Zero)[📈 reach-vb/2024-ai-timeline ](https://huggingface.co/spaces/reach-vb/2024-ai-timeline)[🎧 hilamanor/audioEditing ](https://huggingface.co/spaces/hilamanor/audioEditing)[🚀 declare-lab/TangoFlux ](https://huggingface.co/spaces/declare-lab/TangoFlux)[💻 ameerazam08/stableaudio-open-1.0 ](https://huggingface.co/spaces/ameerazam08/stableaudio-open-1.0)[⚡ vml12/wan-video-studio ](https://huggingface.co/spaces/vml12/wan-video-studio)[🎵 MazCodes/fragmenta ](https://huggingface.co/spaces/MazCodes/fragmenta) + 95 Spaces + 92 Spaces
##  Paper for stabilityai/stable-audio-open-1.0
#### [Stable Audio Open Paper • 2407.14358 • Published Jul 19, 2024 • 26 ](https://huggingface.co/papers/2407.14358)
System theme
Company
[TOS](https://huggingface.co/terms-of-service) [Privacy](https://huggingface.co/privacy) [About](https://huggingface.co/huggingface) [Careers](https://apply.workable.com/huggingface/) [](https://huggingface.co/)
Website
[Models](https://huggingface.co/models) [Datasets](https://huggingface.co/datasets) [Spaces](https://huggingface.co/spaces) [Pricing](https://huggingface.co/pricing) [Docs](https://huggingface.co/docs)

