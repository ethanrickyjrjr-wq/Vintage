Source: https://huggingface.co/facebook/musicgen-small (fetched 2026-11-13 with crawl4ai)

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
[ ![](https://cdn-avatars.huggingface.co/v1/production/uploads/1592839207516-noauth.png) ](https://huggingface.co/facebook)
[facebook](https://huggingface.co/facebook)
/
[musicgen-small](https://huggingface.co/facebook/musicgen-small)
Like 531
Follow
![](https://cdn-avatars.huggingface.co/v1/production/uploads/1592839207516-noauth.png) AI at Meta 16.2k
[ Text-to-Audio ](https://huggingface.co/models?pipeline_tag=text-to-audio)[ Transformers ](https://huggingface.co/models?library=transformers)[ PyTorch ](https://huggingface.co/models?library=pytorch)[ Safetensors ](https://huggingface.co/models?library=safetensors)[ musicgen ](https://huggingface.co/models?other=musicgen)
arxiv: 2306.05284
License: cc-by-nc-4.0
[ Model card ](https://huggingface.co/facebook/musicgen-small)[ Files Files and versions xet ](https://huggingface.co/facebook/musicgen-small/tree/main)[ Community 36 ](https://huggingface.co/facebook/musicgen-small/discussions)
Deploy
Copy to bucket
Use this model
### Instructions to use facebook/musicgen-small with libraries, inference providers, notebooks, and local apps. Follow these links to get started.
  * Libraries
  * [ Transformers](https://huggingface.co/facebook/musicgen-small?library=transformers)
How to use facebook/musicgen-small with Transformers:

```
# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("text-to-audio", model="facebook/musicgen-small")
```

```
# pip install -U transformers accelerate
# Load model directly
from transformers import AutoProcessor, AutoModelForTextToWaveform

processor = AutoProcessor.from_pretrained("facebook/musicgen-small")
model = AutoModelForTextToWaveform.from_pretrained("facebook/musicgen-small", device_map="auto")
```

  * Notebooks
  * [ Google Colab](https://huggingface.co/facebook/musicgen-small/colab)
  * [ Kaggle](https://huggingface.co/facebook/musicgen-small/kaggle)


  * [MusicGen - Small - 300M](https://huggingface.co/facebook/musicgen-small#musicgen---small---300m "MusicGen - Small - 300M")
    * [Example](https://huggingface.co/facebook/musicgen-small#example "Example")
    * [🤗 Transformers Usage](https://huggingface.co/facebook/musicgen-small#%F0%9F%A4%97-transformers-usage "🤗 Transformers Usage")
    * [Audiocraft Usage](https://huggingface.co/facebook/musicgen-small#audiocraft-usage "Audiocraft Usage")
    * [Model details](https://huggingface.co/facebook/musicgen-small#model-details "Model details")
    * [Intended use](https://huggingface.co/facebook/musicgen-small#intended-use "Intended use")
    * [Metrics](https://huggingface.co/facebook/musicgen-small#metrics "Metrics")
    * [Evaluation datasets](https://huggingface.co/facebook/musicgen-small#evaluation-datasets "Evaluation datasets")
    * [Training datasets](https://huggingface.co/facebook/musicgen-small#training-datasets "Training datasets")
    * [Evaluation results](https://huggingface.co/facebook/musicgen-small#evaluation-results "Evaluation results")
    * [Limitations and biases](https://huggingface.co/facebook/musicgen-small#limitations-and-biases "Limitations and biases")


#  [ ](https://huggingface.co/facebook/musicgen-small#musicgen---small---300m) MusicGen - Small - 300M 
MusicGen is a text-to-music model capable of genreating high-quality music samples conditioned on text descriptions or audio prompts. It is a single stage auto-regressive Transformer model trained over a 32kHz EnCodec tokenizer with 4 codebooks sampled at 50 Hz. Unlike existing methods, like MusicLM, MusicGen doesn't require a self-supervised semantic representation, and it generates all 4 codebooks in one pass. By introducing a small delay between the codebooks, we show we can predict them in parallel, thus having only 50 auto-regressive steps per second of audio.
MusicGen was published in [Simple and Controllable Music Generation](https://arxiv.org/abs/2306.05284) by _Jade Copet, Felix Kreuk, Itai Gat, Tal Remez, David Kant, Gabriel Synnaeve, Yossi Adi, Alexandre Défossez_.
Four checkpoints are released:
  * [**small** (this checkpoint)](https://huggingface.co/facebook/musicgen-small)
  * [medium](https://huggingface.co/facebook/musicgen-medium)
  * [large](https://huggingface.co/facebook/musicgen-large)
  * [melody](https://huggingface.co/facebook/musicgen-melody)


##  [ ](https://huggingface.co/facebook/musicgen-small#example) Example 
Try out MusicGen yourself!
  * Audiocraft Colab:

[ ![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg) ](https://colab.research.google.com/drive/1fxGqfg96RBUvGxZ1XXN07s3DthrKUl4-?usp=sharing)
  * Hugging Face Colab:

[ ![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg) ](https://colab.research.google.com/github/sanchit-gandhi/notebooks/blob/main/MusicGen.ipynb)
  * Hugging Face Demo:

[ ![Open in HuggingFace](https://huggingface.co/datasets/huggingface/badges/raw/main/open-in-hf-spaces-sm.svg) ](https://huggingface.co/spaces/facebook/MusicGen)
##  [ ](https://huggingface.co/facebook/musicgen-small#%F0%9F%A4%97-transformers-usage) 🤗 Transformers Usage 
You can run MusicGen locally with the 🤗 Transformers library from version 4.31.0 onwards.
  1. First install the 🤗 [Transformers library](https://github.com/huggingface/transformers) and scipy:



```
pip install --upgrade pip
pip install --upgrade transformers scipy

```

  1. Run inference via the `Text-to-Audio` (TTA) pipeline. You can infer the MusicGen model via the TTA pipeline in just a few lines of code!



```
from transformers import pipeline
import scipy

synthesiser = pipeline("text-to-audio", "facebook/musicgen-small")

music = synthesiser("lo-fi music with a soothing melody", forward_params={"do_sample": True})

scipy.io.wavfile.write("musicgen_out.wav", rate=music["sampling_rate"], data=music["audio"])

```

  1. Run inference via the Transformers modelling code. You can use the processor + generate code to convert text into a mono 32 kHz audio waveform for more fine-grained control.



```
from transformers import AutoProcessor, MusicgenForConditionalGeneration

processor = AutoProcessor.from_pretrained("facebook/musicgen-small")
model = MusicgenForConditionalGeneration.from_pretrained("facebook/musicgen-small")

inputs = processor(
    text=["80s pop track with bassy drums and synth", "90s rock song with loud guitars and heavy drums"],
    padding=True,
    return_tensors="pt",
)

audio_values = model.generate(**inputs, max_new_tokens=256)

```

  1. Listen to the audio samples either in an ipynb notebook:



```
from IPython.display import Audio

sampling_rate = model.config.audio_encoder.sampling_rate
Audio(audio_values[0].numpy(), rate=sampling_rate)

```

Or save them as a `.wav` file using a third-party library, e.g. `scipy`:

```
import scipy

sampling_rate = model.config.audio_encoder.sampling_rate
scipy.io.wavfile.write("musicgen_out.wav", rate=sampling_rate, data=audio_values[0, 0].numpy())

```

For more details on using the MusicGen model for inference using the 🤗 Transformers library, refer to the [MusicGen docs](https://huggingface.co/docs/transformers/model_doc/musicgen).
##  [ ](https://huggingface.co/facebook/musicgen-small#audiocraft-usage) Audiocraft Usage 
You can also run MusicGen locally through the original [Audiocraft library](https://huggingface.co/facebook/musicgen-small/tree/main/\(https://github.com/facebookresearch/audiocraft):
  1. First install the [`audiocraft` library](https://github.com/facebookresearch/audiocraft)



```
pip install git+https://github.com/facebookresearch/audiocraft.git

```

  1. Make sure to have [`ffmpeg`](https://ffmpeg.org/download.html) installed:



```
apt-get install ffmpeg

```

  1. Run the following Python code:



```
from audiocraft.models import MusicGen
from audiocraft.data.audio import audio_write

model = MusicGen.get_pretrained("small")
model.set_generation_params(duration=8)  # generate 8 seconds.

descriptions = ["happy rock", "energetic EDM"]

wav = model.generate(descriptions)  # generates 2 samples.

for idx, one_wav in enumerate(wav):
    # Will save under {idx}.wav, with loudness normalization at -14 db LUFS.
    audio_write(f'{idx}', one_wav.cpu(), model.sample_rate, strategy="loudness")

```

##  [ ](https://huggingface.co/facebook/musicgen-small#model-details) Model details 
**Organization developing the model:** The FAIR team of Meta AI.
**Model date:** MusicGen was trained between April 2023 and May 2023.
**Model version:** This is the version 1 of the model.
**Model type:** MusicGen consists of an EnCodec model for audio tokenization, an auto-regressive language model based on the transformer architecture for music modeling. The model comes in different sizes: 300M, 1.5B and 3.3B parameters ; and two variants: a model trained for text-to-music generation task and a model trained for melody-guided music generation.
**Paper or resources for more information:** More information can be found in the paper [Simple and Controllable Music Generation](https://arxiv.org/abs/2306.05284).
**Citation details:**

```
@misc{copet2023simple,
      title={Simple and Controllable Music Generation}, 
      author={Jade Copet and Felix Kreuk and Itai Gat and Tal Remez and David Kant and Gabriel Synnaeve and Yossi Adi and Alexandre Défossez},
      year={2023},
      eprint={2306.05284},
      archivePrefix={arXiv},
      primaryClass={cs.SD}
}

```

**License:** Code is released under MIT, model weights are released under CC-BY-NC 4.0.
**Where to send questions or comments about the model:** Questions and comments about MusicGen can be sent via the [Github repository](https://github.com/facebookresearch/audiocraft) of the project, or by opening an issue.
##  [ ](https://huggingface.co/facebook/musicgen-small#intended-use) Intended use 
**Primary intended use:** The primary use of MusicGen is research on AI-based music generation, including:
  * Research efforts, such as probing and better understanding the limitations of generative models to further improve the state of science
  * Generation of music guided by text or melody to understand current abilities of generative AI models by machine learning amateurs


**Primary intended users:** The primary intended users of the model are researchers in audio, machine learning and artificial intelligence, as well as amateur seeking to better understand those models.
**Out-of-scope use cases:** The model should not be used on downstream applications without further risk evaluation and mitigation. The model should not be used to intentionally create or disseminate music pieces that create hostile or alienating environments for people. This includes generating music that people would foreseeably find disturbing, distressing, or offensive; or content that propagates historical or current stereotypes.
##  [ ](https://huggingface.co/facebook/musicgen-small#metrics) Metrics 
**Models performance measures:** We used the following objective measure to evaluate the model on a standard music benchmark:
  * Frechet Audio Distance computed on features extracted from a pre-trained audio classifier (VGGish)
  * Kullback-Leibler Divergence on label distributions extracted from a pre-trained audio classifier (PaSST)
  * CLAP Score between audio embedding and text embedding extracted from a pre-trained CLAP model


Additionally, we run qualitative studies with human participants, evaluating the performance of the model with the following axes:
  * Overall quality of the music samples;
  * Text relevance to the provided text input;
  * Adherence to the melody for melody-guided music generation.


More details on performance measures and human studies can be found in the paper.
**Decision thresholds:** Not applicable.
##  [ ](https://huggingface.co/facebook/musicgen-small#evaluation-datasets) Evaluation datasets 
The model was evaluated on the [MusicCaps benchmark](https://www.kaggle.com/datasets/googleai/musiccaps) and on an in-domain held-out evaluation set, with no artist overlap with the training set.
##  [ ](https://huggingface.co/facebook/musicgen-small#training-datasets) Training datasets 
The model was trained on licensed data using the following sources: the [Meta Music Initiative Sound Collection](https://www.fb.com/sound), [Shutterstock music collection](https://www.shutterstock.com/music) and the [Pond5 music collection](https://www.pond5.com/). See the paper for more details about the training set and corresponding preprocessing.
##  [ ](https://huggingface.co/facebook/musicgen-small#evaluation-results) Evaluation results 
Below are the objective metrics obtained on MusicCaps with the released model. Note that for the publicly released models, we had all the datasets go through a state-of-the-art music source separation method, namely using the open source [Hybrid Transformer for Music Source Separation](https://github.com/facebookresearch/demucs) (HT-Demucs), in order to keep only the instrumental part. This explains the difference in objective metrics with the models used in the paper.  
| Model  | Frechet Audio Distance  | KLD  | Text Consistency  | Chroma Cosine Similarity  |  
| --- | --- | --- | --- | --- |  
| **facebook/musicgen-small**  | 4.88  | 1.42  | 0.27  | -  |  
| facebook/musicgen-medium  | 5.14  | 1.38  | 0.28  | -  |  
| facebook/musicgen-large  | 5.48  | 1.37  | 0.28  | -  |  
| facebook/musicgen-melody  | 4.93  | 1.41  | 0.27  | 0.44  |  
More information can be found in the paper [Simple and Controllable Music Generation](https://arxiv.org/abs/2306.05284), in the Results section.
##  [ ](https://huggingface.co/facebook/musicgen-small#limitations-and-biases) Limitations and biases 
**Data:** The data sources used to train the model are created by music professionals and covered by legal agreements with the right holders. The model is trained on 20K hours of data, we believe that scaling the model on larger datasets can further improve the performance of the model.
**Mitigations:** Vocals have been removed from the data source using corresponding tags, and then using a state-of-the-art music source separation method, namely using the open source [Hybrid Transformer for Music Source Separation](https://github.com/facebookresearch/demucs) (HT-Demucs).
**Limitations:**
  * The model is not able to generate realistic vocals.
  * The model has been trained with English descriptions and will not perform as well in other languages.
  * The model does not perform equally well for all music styles and cultures.
  * The model sometimes generates end of songs, collapsing to silence.
  * It is sometimes difficult to assess what types of text descriptions provide the best generations. Prompt engineering may be required to obtain satisfying results.


**Biases:** The source of data is potentially lacking diversity and all music cultures are not equally represented in the dataset. The model may not perform equally well on the wide variety of music genres that exists. The generated samples from the model will reflect the biases from the training data. Further work on this model should include methods for balanced and just representations of cultures, for example, by scaling the training data to be both diverse and inclusive.
**Risks and harms:** Biases and limitations of the model may lead to generation of samples that may be considered as biased, inappropriate or offensive. We believe that providing the code to reproduce the research and train new models will allow to broaden the application to new and more representative data.
**Use cases:** Users must be aware of the biases, limitations and risks of the model. MusicGen is a model developed for artificial intelligence research on controllable music generation. As such, it should not be used for downstream applications without further investigation and mitigation of risks. 

Downloads last month
    160,661
Safetensors[](https://huggingface.co/docs/safetensors)
Model size
0.6B params
Tensor type
F32 
·
Files info
Inference Providers [NEW](https://huggingface.co/docs/inference-providers)
Text-to-Audio
This model isn't deployed by any Inference Provider. [🙋 9 Ask for provider support](https://huggingface.co/spaces/huggingface/InferenceSupport/discussions/731)
##  Model tree for facebook/musicgen-small [](https://huggingface.co/docs/hub/model-cards#specifying-a-base-model)
Adapters
[34 models](https://huggingface.co/models?other=base_model:adapter:facebook/musicgen-small)
Finetunes
[16 models](https://huggingface.co/models?other=base_model:finetune:facebook/musicgen-small)
Quantizations
[8 models](https://huggingface.co/models?other=base_model:quantized:facebook/musicgen-small)
##  Spaces using facebook/musicgen-small 100
[ ![](https://cdn-avatars.huggingface.co/v1/production/uploads/1592839207516-noauth.png) facebook/MusicGen ](https://huggingface.co/spaces/facebook/MusicGen)[ ![](https://cdn-avatars.huggingface.co/v1/production/uploads/1592839207516-noauth.png) facebook/MelodyFlow ](https://huggingface.co/spaces/facebook/MelodyFlow)[🎼 Surn/UnlimitedMusicGen ](https://huggingface.co/spaces/Surn/UnlimitedMusicGen)[🐢 aach456/music-gen-ai ](https://huggingface.co/spaces/aach456/music-gen-ai)[🔥 sanchit-gandhi/musicgen-streaming ](https://huggingface.co/spaces/sanchit-gandhi/musicgen-streaming)[🎵 patgpt4/MusicGen ](https://huggingface.co/spaces/patgpt4/MusicGen)[🎵 sunnyujjawal/AI-Music-Generator ](https://huggingface.co/spaces/sunnyujjawal/AI-Music-Generator)[🏆 SunilGopal/MusicLM ](https://huggingface.co/spaces/SunilGopal/MusicLM) + 95 Spaces + 92 Spaces
##  Paper for facebook/musicgen-small
#### [Simple and Controllable Music Generation Paper • 2306.05284 • Published Jun 8, 2023 • 170 ](https://huggingface.co/papers/2306.05284)
System theme
Company
[TOS](https://huggingface.co/terms-of-service) [Privacy](https://huggingface.co/privacy) [About](https://huggingface.co/huggingface) [Careers](https://apply.workable.com/huggingface/) [](https://huggingface.co/)
Website
[Models](https://huggingface.co/models) [Datasets](https://huggingface.co/datasets) [Spaces](https://huggingface.co/spaces) [Pricing](https://huggingface.co/pricing) [Docs](https://huggingface.co/docs)
Inference providers allow you to run inference using different serverless providers.

