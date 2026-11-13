Source: https://huggingface.co/Lightricks/LTX-2.5-Diffusers (fetched 2026-11-13 with crawl4ai)

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
[ ![](https://cdn-avatars.huggingface.co/v1/production/uploads/669524bcbcd81f395e8f60f6/0ynfqKEWMh_dn3h4ff1K5.png) ](https://huggingface.co/Lightricks)
[Lightricks](https://huggingface.co/Lightricks)
/
[LTX-2.5-Diffusers](https://huggingface.co/Lightricks/LTX-2.5-Diffusers)
Like 140
Follow
![](https://cdn-avatars.huggingface.co/v1/production/uploads/669524bcbcd81f395e8f60f6/0ynfqKEWMh_dn3h4ff1K5.png) LTX.io 6.73k
[ Text-to-Video ](https://huggingface.co/models?pipeline_tag=text-to-video)[ Diffusers ](https://huggingface.co/models?library=diffusers)[ Safetensors ](https://huggingface.co/models?library=safetensors)
9 languages
[ LTX2Pipeline ](https://huggingface.co/models?other=diffusers%3ALTX2Pipeline)[ image-to-video ](https://huggingface.co/models?other=image-to-video)[ video-to-video ](https://huggingface.co/models?other=video-to-video)[ image-text-to-video ](https://huggingface.co/models?other=image-text-to-video)[ audio-to-video ](https://huggingface.co/models?other=audio-to-video)[ text-to-audio ](https://huggingface.co/models?other=text-to-audio)[ video-to-audio ](https://huggingface.co/models?other=video-to-audio)[ audio-to-audio ](https://huggingface.co/models?other=audio-to-audio)[ text-to-audio-video ](https://huggingface.co/models?other=text-to-audio-video)[ image-to-audio-video ](https://huggingface.co/models?other=image-to-audio-video)[ image-text-to-audio-video ](https://huggingface.co/models?other=image-text-to-audio-video)[ ltx-2 ](https://huggingface.co/models?other=ltx-2)[ ltx-video ](https://huggingface.co/models?other=ltx-video)[ ltxv ](https://huggingface.co/models?other=ltxv)[ lightricks ](https://huggingface.co/models?other=lightricks)[ ltx-2.5 ](https://huggingface.co/models?other=ltx-2.5)
arxiv: 2601.03233
License: ltx-2.x-community-license-agreement
[ Model card ](https://huggingface.co/Lightricks/LTX-2.5-Diffusers)[ Files Files and versions xet ](https://huggingface.co/Lightricks/LTX-2.5-Diffusers/tree/main)[ Community 12 ](https://huggingface.co/Lightricks/LTX-2.5-Diffusers/discussions)
Deploy
Copy to bucket
Use this model
### Instructions to use Lightricks/LTX-2.5-Diffusers with libraries, inference providers, notebooks, and local apps. Follow these links to get started.
  * Libraries
  * [ Diffusers](https://huggingface.co/Lightricks/LTX-2.5-Diffusers?library=diffusers)
How to use Lightricks/LTX-2.5-Diffusers with Diffusers:

```
pip install -U diffusers transformers accelerate
```

```
import torch
from diffusers import DiffusionPipeline

# switch to "mps" for apple devices
pipe = DiffusionPipeline.from_pretrained("Lightricks/LTX-2.5-Diffusers", dtype=torch.bfloat16, device_map="cuda")

prompt = "Astronaut in a jungle, cold color palette, muted colors, detailed, 8k"
image = pipe(prompt).images[0]
```

  * Notebooks
  * [ Google Colab](https://huggingface.co/Lightricks/LTX-2.5-Diffusers/colab)
  * [ Kaggle](https://huggingface.co/Lightricks/LTX-2.5-Diffusers/kaggle)


##  You need to agree to share your Hugging Face information to access this model
By clicking "Agree and Access" you acknowledge the [Privacy Policy](https://static.lightricks.com/legal/Privacy%20Policy%20-%20LTX%20Platform.pdf) and consent to receive offers and updates including targeted and personalized advertisements. You can unsubscribe at any time.
[Log in](https://huggingface.co/login?next=/Lightricks/LTX-2.5-Diffusers) or [Sign Up](https://huggingface.co/join?next=/Lightricks/LTX-2.5-Diffusers) to review the conditions and access this model content.
  * [Diffusers weights for LTX-2.5.](https://huggingface.co/Lightricks/LTX-2.5-Diffusers#diffusers-weights-for-ltx-25httpshuggingfacecolightricksltx-25 "Diffusers weights for LTX-2.5.")
    * [Layout](https://huggingface.co/Lightricks/LTX-2.5-Diffusers#layout "Layout")
    * [Install](https://huggingface.co/Lightricks/LTX-2.5-Diffusers#install "Install")
    * [Downloading only what you need](https://huggingface.co/Lightricks/LTX-2.5-Diffusers#downloading-only-what-you-need "Downloading only what you need")
    * [Quick start — distilled, convolutional decode](https://huggingface.co/Lightricks/LTX-2.5-Diffusers#quick-start--distilled-convolutional-decode "Quick start — distilled, convolutional decode")
    * [Two-stage distilled generation](https://huggingface.co/Lightricks/LTX-2.5-Diffusers#two-stage-distilled-generation "Two-stage distilled generation")
    * [Decode with the diffusion decoder](https://huggingface.co/Lightricks/LTX-2.5-Diffusers#decode-with-the-diffusion-decoder "Decode with the diffusion decoder")
    * [Full / SFT transformer](https://huggingface.co/Lightricks/LTX-2.5-Diffusers#full--sft-transformer "Full / SFT transformer")
    * [🧱 Modular inference](https://huggingface.co/Lightricks/LTX-2.5-Diffusers#%F0%9F%A7%B1-modular-inference "🧱 Modular inference")
      * [Distilled, diffusion decode](https://huggingface.co/Lightricks/LTX-2.5-Diffusers#distilled-diffusion-decode "Distilled, diffusion decode")
      * [Full / SFT transformer, convolutional decode](https://huggingface.co/Lightricks/LTX-2.5-Diffusers#full--sft-transformer-convolutional-decode "Full / SFT transformer, convolutional decode")
    * [Prompting](https://huggingface.co/Lightricks/LTX-2.5-Diffusers#prompting "Prompting")
    * [Notes](https://huggingface.co/Lightricks/LTX-2.5-Diffusers#notes "Notes")


![LTX-2.5 — Video, Audio & World Simulation](https://huggingface.co/Lightricks/LTX-2.5/resolve/main/hf-hero-web.webp)
# LTX-2.5 — Video, Audio & World Simulation
Full control and customization — self-host on your infrastructure.
[Homepage](https://ltx.io) [Docs](https://docs.ltx.io/open-source-model/getting-started/overview) [GitHub](https://github.com/Lightricks/LTX-2) [Research](https://huggingface.co/papers/2601.03233) [API Playground](https://console.ltx.io/playground/) [Discord](https://discord.gg/ltx)
[LTX License](https://github.com/Lightricks/LTX-2/blob/main/LICENSE-2_x)
# LTX-2.5 — Video, Audio & World Simulation
Full control and customization — self-host on your infrastructure.
[Homepage](https://ltx.io) [Docs](https://docs.ltx.io/open-source-model/getting-started/overview) [GitHub](https://github.com/Lightricks/LTX-2) [Research](https://huggingface.co/papers/2601.03233) [API Playground](https://console.ltx.io/playground/) [Discord](https://discord.gg/ltx)
[LTX License](https://github.com/Lightricks/LTX-2/blob/main/LICENSE-2_x)
Under $10M annual revenue
Commercial and production use at no cost under the LTX-2.x Community License. Transfer of fine-tunes may require a paid license, in accordance with the LTX-2.x Community License.
[Read the Documentation](https://docs.ltx.io/open-source-model/getting-started/overview)
Over $10M annual revenue
Paid Commercial Use Agreement for LTX-2.x with full weights, engineering support, LoRAs, and flexible deployment options. To learn about all licensing options, talk to an expert.
[Talk to a Commercial Licensing Expert](https://ltx.io/forms/ltx-contact-sales?kpi=licensing)
Under $10M annual revenue
Commercial and production use at no cost under the LTX-2.x Community License. Transfer of fine-tunes may require a paid license, in accordance with the LTX-2.x Community License.
[Read the Documentation](https://docs.ltx.io/open-source-model/getting-started/overview)
Over $10M annual revenue
Paid Commercial Use Agreement for LTX-2.x with full weights, engineering support, LoRAs, and flexible deployment options. To learn about all licensing options, talk to an expert.
[Talk to a Commercial Licensing Expert](https://ltx.io/forms/ltx-contact-sales?kpi=licensing)
* * *
#  [ ](https://huggingface.co/Lightricks/LTX-2.5-Diffusers#diffusers-weights-for-ltx-25) Diffusers weights for [LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5). 
* * *
**LTX-2.5** is an open world model with open weights, built for local execution and fine-tuning. Its established use is generating synchronized, high-fidelity video and audio from text, image, and video inputs; applicability to emerging domains such as robotics and physical AI is developing.
**Full control and customization** — self-host on your own infrastructure. No per-generation billing, no per-seat lock-in, no forced API dependency. Revenue is measured across the whole entity, including subsidiaries and affiliates under common control. The full, binding terms live in [`LICENSE`](https://github.com/Lightricks/LTX-2/blob/main/LICENSE-2_x).
* * *
##  [ ](https://huggingface.co/Lightricks/LTX-2.5-Diffusers#layout) Layout   
| Path  | Component  |  
| --- | --- |  
| `transformer/`  |  **Distilled** DiT (default in `model_index.json`)  |  
| `transformer_full/`  | Full / SFT DiT  |  
| `vae/`  | Convolutional video VAE (encode + conv decode)  |  
| `diffusion_decoder/`  | Diffusion (DiT) video decoder, decoder-only  |  
| `latent_upsampler/`  | Spatial x2 latent upsampler, for the two-stage distilled recipe  |  
|  `audio_vae/`, `vocoder/`, `connectors/`, `text_encoder/`, `tokenizer/`, `scheduler/`, `duration_head/`  | Shared  |  
Encoding always uses `vae/`, and `LTX2Pipeline` decodes with `vae/` too. The diffusion decoder is a diffusion model in its own right rather than a pipeline component, so it is driven by `LTX2VideoDiffusionDecodePipeline`: run the pipeline with `output_type="latent"`, then decode. Both decoders consume the same latents.
`scheduler/` is configured for the **distilled** transformer (`use_dynamic_shifting: false`, `shift_terminal: null`) so that distilled sigma schedules are used exactly as given. See [Full / SFT transformer](https://huggingface.co/Lightricks/LTX-2.5-Diffusers#full--sft-transformer) for the override the full DiT needs.
##  [ ](https://huggingface.co/Lightricks/LTX-2.5-Diffusers#install) Install 
LTX-2.5 support is not in a `diffusers` release yet, so install from main:

```
pip install git+https://github.com/huggingface/diffusers

```

##  [ ](https://huggingface.co/Lightricks/LTX-2.5-Diffusers#downloading-only-what-you-need) Downloading only what you need 
`from_pretrained` fetches just the components listed in `model_index.json`, so the distilled path never pulls `transformer_full/`. If you snapshot the repo instead, exclude it explicitly — 72 GB rather than 110 GB:

```
hf download Lightricks/LTX-2.5-Diffusers --exclude "transformer_full/*"

```

##  [ ](https://huggingface.co/Lightricks/LTX-2.5-Diffusers#quick-start--distilled-convolutional-decode) Quick start — distilled, convolutional decode 
Distilled inference is driven by an explicit sigma schedule, not a step count, and runs unguided — `guidance_scale=1.0` plus STG and modality guidance zeroed, since the pipeline defaults are the SFT values. Passing `num_inference_steps` instead would hand the model a generic linear schedule and quietly cost quality.

```
import torch
from diffusers import LTX2Pipeline
from diffusers.pipelines.ltx2.utils import DEFAULT_NEGATIVE_PROMPT, DISTILLED_SIGMA_VALUES
from diffusers.utils import encode_video

MODEL_ID = "Lightricks/LTX-2.5-Diffusers"

pipe = LTX2Pipeline.from_pretrained(MODEL_ID, dtype=torch.bfloat16)
pipe.enable_model_cpu_offload()

video, audio = pipe(
    prompt="A cinematic shot of a red fox walking through a snowy forest at dawn, "
           "the camera tracking alongside, snow crunching underfoot.",
    negative_prompt=DEFAULT_NEGATIVE_PROMPT,
    width=960,
    height=544,
    num_frames=121,
    frame_rate=24.0,
    sigmas=DISTILLED_SIGMA_VALUES,
    guidance_scale=1.0,
    audio_guidance_scale=1.0,
    stg_scale=0.0,
    audio_stg_scale=0.0,
    modality_scale=1.0,
    audio_modality_scale=1.0,
    generator=torch.Generator("cuda").manual_seed(42),
    output_type="np",
    return_dict=False,
)

encode_video(
    video[0],
    fps=24,
    output_path="ltx25.mp4",
    audio=audio[0].float().cpu(),
    audio_sample_rate=pipe.vocoder.config.output_sampling_rate,
)

```

Video and audio are generated jointly. Read the audio rate off the vocoder rather than hardcoding it — this checkpoint ships `LTX2VocoderWithBWE`, whose `output_sampling_rate` is 48000.
##  [ ](https://huggingface.co/Lightricks/LTX-2.5-Diffusers#two-stage-distilled-generation) Two-stage distilled generation 
Better quality than the single-stage quick start: half resolution, x2 latent upsample, then a 3-sigma tail at full resolution. One generator across both calls, so stage 2 continues the noise stream.

```
import torch
from diffusers import LTX2LatentUpsamplePipeline, LTX2Pipeline
from diffusers.pipelines.ltx2.latent_upsampler import LTX2LatentUpsamplerModel
from diffusers.pipelines.ltx2.utils import (
    DEFAULT_NEGATIVE_PROMPT,
    DISTILLED_SIGMA_VALUES,
    STAGE_2_DISTILLED_SIGMA_VALUES,
)
from diffusers.utils import encode_video

MODEL_ID = "Lightricks/LTX-2.5-Diffusers"
# Stage 1 resolution; stage 2 runs at 2x this.
HEIGHT, WIDTH, NUM_FRAMES, FRAME_RATE = 544, 960, 121, 24.0

pipe = LTX2Pipeline.from_pretrained(MODEL_ID, dtype=torch.bfloat16)
pipe.enable_model_cpu_offload()
pipe.vae.enable_tiling()  # stage 2 decodes at 2x

latent_upsampler = LTX2LatentUpsamplerModel.from_pretrained(
    MODEL_ID, subfolder="latent_upsampler", dtype=torch.bfloat16
).to("cuda")
upsample_pipe = LTX2LatentUpsamplePipeline(vae=pipe.vae, latent_upsampler=latent_upsampler)

generator = torch.Generator("cuda").manual_seed(42)
shared = dict(
    prompt="A cinematic shot of a red fox walking through a snowy forest at dawn, "
           "the camera tracking alongside, snow crunching underfoot.",
    negative_prompt=DEFAULT_NEGATIVE_PROMPT,
    frame_rate=FRAME_RATE,
    guidance_scale=1.0,
    audio_guidance_scale=1.0,
    stg_scale=0.0,
    audio_stg_scale=0.0,
    modality_scale=1.0,
    audio_modality_scale=1.0,
    generator=generator,
    return_dict=False,
)

stage_1_latents, audio_latents = pipe(
    height=HEIGHT, width=WIDTH, num_frames=NUM_FRAMES,
    sigmas=DISTILLED_SIGMA_VALUES, output_type="latent", **shared,
)

upsampled_latents = upsample_pipe(
    latents=stage_1_latents, output_type="latent", return_dict=False
)[0]

# Stage 2 takes its size from the upsampled latents, so pass no height/width.
video, audio = pipe(
    num_frames=NUM_FRAMES,
    sigmas=STAGE_2_DISTILLED_SIGMA_VALUES,
    latents=upsampled_latents,
    audio_latents=audio_latents,
    noise_scale=STAGE_2_DISTILLED_SIGMA_VALUES[0],
    output_type="np",
    **shared,
)

encode_video(
    video[0],
    fps=int(FRAME_RATE),
    output_path="ltx25_two_stage.mp4",
    audio=audio[0].float().cpu(),
    audio_sample_rate=pipe.vocoder.config.output_sampling_rate,
)

```

To finish this with the diffusion decoder instead, ask stage 2 for `output_type="latent"` and follow the next section — including its by-hand audio decode, since latents skip the vocoder.
##  [ ](https://huggingface.co/Lightricks/LTX-2.5-Diffusers#decode-with-the-diffusion-decoder) Decode with the diffusion decoder 
Ask the pipeline for latents, then decode them. Two things differ from the snippet above: `output_type="latent"` skips the vocoder, so the audio comes back as **latents** and has to be finished by hand; and the decoder needs `pip install kernels`, which fetches the [NATTEN](https://github.com/SHI-Labs/NATTEN) kernel from the Hub (a local `natten` install is not used).

```
import torch
from diffusers import LTX2Pipeline, LTX2VideoDiffusionDecoderModel
from diffusers.models.autoencoders.ltx2_diffusion_decoder import LTX2VideoVaeNeighborhoodNattenProcessor
from diffusers.pipelines.ltx2.pipeline_ltx2_diffusion_decode import LTX2VideoDiffusionDecodePipeline
from diffusers.pipelines.ltx2.utils import DEFAULT_NEGATIVE_PROMPT, DISTILLED_SIGMA_VALUES
from diffusers.utils import encode_video

MODEL_ID = "Lightricks/LTX-2.5-Diffusers"

pipe = LTX2Pipeline.from_pretrained(MODEL_ID, dtype=torch.bfloat16)
pipe.enable_model_cpu_offload()
generator = torch.Generator("cuda").manual_seed(42)

latents, audio_latents = pipe(
    prompt="A cinematic shot of a red fox walking through a snowy forest at dawn, "
           "the camera tracking alongside, snow crunching underfoot.",
    negative_prompt=DEFAULT_NEGATIVE_PROMPT,
    width=960, height=544, num_frames=121, frame_rate=24.0,
    sigmas=DISTILLED_SIGMA_VALUES,
    guidance_scale=1.0,
    audio_guidance_scale=1.0,
    stg_scale=0.0,
    audio_stg_scale=0.0,
    modality_scale=1.0,
    audio_modality_scale=1.0,
    generator=generator,
    output_type="latent",
    return_dict=False,
)

# `output_type="latent"` skips the vocoder, so finish the audio here. These latents are already
# denormalized, which is what `audio_vae.decode` expects.
mel = pipe.audio_vae.decode(audio_latents.to(pipe.audio_vae.dtype), return_dict=False)[0]
audio = pipe.vocoder(mel)

decoder = LTX2VideoDiffusionDecoderModel.from_pretrained(
    MODEL_ID, subfolder="diffusion_decoder", dtype=torch.bfloat16
).to("cuda")

# The default FlexAttention processor is uncompiled, so it materialises the full score matrix and needs
# tens of GB at video resolutions. NATTEN's kernels are what the original implementation uses.
# `set_attention_backend` is not an alternative: no backend other than `flex` accepts the BlockMask.
# Every attention module in the decoder is the same neighborhood attention, so one call swaps them all.
decoder.set_attn_processor(LTX2VideoVaeNeighborhoodNattenProcessor())
# Decode in overlapping tiles so peak memory is bounded by the tile size, not the video size.
decoder.enable_tiling()

decode_pipe = LTX2VideoDiffusionDecodePipeline(diffusion_decoder=decoder, scheduler=pipe.scheduler)

# denormalize=False: `output_type="latent"` already applied the latent statistics, so applying them
# again would rescale every channel by its std a second time. The decoder draws its own noise, so pass
# a generator for reproducible decoding.
video = decode_pipe(
    latents, generator=generator, output_type="np", denormalize=False, return_dict=False
)[0]

encode_video(
    video[0],
    fps=24,
    output_path="ltx25_diffusion_decode.mp4",
    audio=audio[0].float().cpu(),
    audio_sample_rate=pipe.vocoder.config.output_sampling_rate,
)

```

`enable_tiling()` bounds peak memory by the tile size rather than by the size of the video. The cheap early upsampling stages still see the full latent; only the last upsampling stage and the diffusion stage, which dominate decode memory, run per tile, so tiling changes the output only near tile borders. Each tile is denoised separately, so a tiled decode does not reproduce an untiled one exactly. The default tile and overlap sizes match the reference implementation's and can be overridden with the `tile_sample_min_*` / `tile_sample_stride_*` arguments.
##  [ ](https://huggingface.co/Lightricks/LTX-2.5-Diffusers#full--sft-transformer) Full / SFT transformer 
`transformer_full/` is not in `model_index.json`, so load it explicitly, and re-enable the shifting the distilled `scheduler/` turns off. The pipeline's guidance defaults are already the SFT values, so the only other change is dropping the distilled overrides. As a diff against the quick start:

```
 import torch
-from diffusers import LTX2Pipeline
-from diffusers.pipelines.ltx2.utils import DEFAULT_NEGATIVE_PROMPT, DISTILLED_SIGMA_VALUES
+from diffusers import FlowMatchEulerDiscreteScheduler, LTX2Pipeline, LTX2VideoTransformer3DModel
+from diffusers.pipelines.ltx2.utils import DEFAULT_NEGATIVE_PROMPT
 from diffusers.utils import encode_video

 MODEL_ID = "Lightricks/LTX-2.5-Diffusers"

-pipe = LTX2Pipeline.from_pretrained(MODEL_ID, dtype=torch.bfloat16)
+pipe = LTX2Pipeline.from_pretrained(
+    MODEL_ID,
+    transformer=LTX2VideoTransformer3DModel.from_pretrained(
+        MODEL_ID, subfolder="transformer_full", dtype=torch.bfloat16
+    ),
+    dtype=torch.bfloat16,
+)
 pipe.enable_model_cpu_offload()
+pipe.scheduler = FlowMatchEulerDiscreteScheduler.from_config(
+    pipe.scheduler.config, use_dynamic_shifting=True, shift_terminal=0.1
+)

 video, audio = pipe(
     prompt="A cinematic shot of a red fox walking through a snowy forest at dawn, "
            "the camera tracking alongside, snow crunching underfoot.",
     negative_prompt=DEFAULT_NEGATIVE_PROMPT,
     width=960,
     height=544,
     num_frames=121,
     frame_rate=24.0,
-    sigmas=DISTILLED_SIGMA_VALUES,
-    guidance_scale=1.0,
-    audio_guidance_scale=1.0,
-    stg_scale=0.0,
-    audio_stg_scale=0.0,
-    modality_scale=1.0,
-    audio_modality_scale=1.0,
     generator=torch.Generator("cuda").manual_seed(42),
     output_type="np",
     return_dict=False,
 )

```

Passing `transformer=` also keeps `from_pretrained` from fetching the distilled folder.
##  [ ](https://huggingface.co/Lightricks/LTX-2.5-Diffusers#%F0%9F%A7%B1-modular-inference) 🧱 Modular inference 
The same weights also run as a [Modular Diffusers](https://huggingface.co/docs/diffusers/main/en/modular_diffusers/overview) pipeline.
###  [ ](https://huggingface.co/Lightricks/LTX-2.5-Diffusers#distilled-diffusion-decode) Distilled, diffusion decode 

```
import torch
from diffusers import ModularPipeline
from diffusers.models.autoencoders.ltx2_diffusion_decoder import LTX2VideoVaeNeighborhoodNattenProcessor
from diffusers.modular_pipelines import ComponentsManager
from diffusers.modular_pipelines.ltx2.guider import LTX2Guidance
from diffusers.pipelines.ltx2.utils import DEFAULT_NEGATIVE_PROMPT, DISTILLED_SIGMA_VALUES
from diffusers.utils import encode_video, load_image

MODEL_ID = "Lightricks/LTX-2.5-Diffusers"

components = ComponentsManager()
pipe = ModularPipeline.from_pretrained(MODEL_ID, components_manager=components)
pipe.load_components(dtype=torch.bfloat16)

# Distilled recipe: unguided, one forward per step.
pipe.update_components(
    guider=LTX2Guidance(guidance_scale=1.0),
    audio_guider=LTX2Guidance(guidance_scale=1.0),
)

pipe.diffusion_decoder.set_attn_processor(LTX2VideoVaeNeighborhoodNattenProcessor())
pipe.diffusion_decoder.enable_tiling()
components.enable_auto_cpu_offload(memory_reserve_margin="20GB")

image = load_image(
    "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/diffusers/astronaut.jpg"
)

output = pipe(
    image=image,
    prompt="An astronaut hatches from a fragile egg on the surface of the Moon, the shell cracking and "
           "peeling apart in gentle low-gravity motion.",
    negative_prompt=DEFAULT_NEGATIVE_PROMPT,
    width=960,
    height=544,
    num_frames=121,  # omit to let `duration_head` predict the length
    frame_rate=24.0,
    sigmas=DISTILLED_SIGMA_VALUES,
    generator=torch.Generator("cuda").manual_seed(42),
    output_type="np",
    output=["videos", "audio"],
)
video, audio = output["videos"], output["audio"]

encode_video(
    video[0],
    fps=24,
    output_path="ltx25_modular_i2v.mp4",
    audio=audio[0].float().cpu(),
    audio_sample_rate=pipe.vocoder.config.output_sampling_rate,
)

```

The workflow follows the inputs: drop `image` for text-to-video, or pass `conditions=` / `reference_conditions=` for the condition and in-context (IC-LoRA) workflows. Raising `memory_reserve_margin` offloads more aggressively — decode activations need far more than the 3 GB default.
###  [ ](https://huggingface.co/Lightricks/LTX-2.5-Diffusers#full--sft-transformer-convolutional-decode) Full / SFT transformer, convolutional decode 
The two swaps are independent — either works on its own. `subfolder=` takes a per-component dict, so only the transformer moves to `transformer_full/`, and the decode block is replaced before loading so the diffusion decoder is never fetched. Guidance stays at the block defaults, which are already the SFT values.

```
import torch
from diffusers import FlowMatchEulerDiscreteScheduler, ModularPipeline
from diffusers.modular_pipelines import ComponentsManager
from diffusers.modular_pipelines.ltx2.modular_blocks_ltx2 import LTX2AutoDecoderStep
from diffusers.pipelines.ltx2.utils import DEFAULT_NEGATIVE_PROMPT
from diffusers.utils import encode_video

MODEL_ID = "Lightricks/LTX-2.5-Diffusers"

components = ComponentsManager()
pipe = ModularPipeline.from_pretrained(MODEL_ID, components_manager=components)

# Convolutional decode. Assign through `_blocks`: `pipe.blocks` returns a copy, so assigning to that is a
# silent no-op.
pipe._blocks.sub_blocks["decode"] = LTX2AutoDecoderStep()

pipe.load_components(dtype=torch.bfloat16, subfolder={"transformer": "transformer_full"})
pipe.vae.enable_tiling()

# Re-enable the shifting the distilled `scheduler/` turns off. `audio_scheduler` is deep-copied from this
# one, so a single update covers both.
pipe.update_components(
    scheduler=FlowMatchEulerDiscreteScheduler.from_config(
        pipe.scheduler.config, use_dynamic_shifting=True, shift_terminal=0.1
    )
)
components.enable_auto_cpu_offload(memory_reserve_margin="32GB")

output = pipe(
    prompt="A cinematic shot of a red fox walking through a snowy forest at dawn, "
           "the camera tracking alongside, snow crunching underfoot.",
    negative_prompt=DEFAULT_NEGATIVE_PROMPT,
    width=960,
    height=544,
    num_frames=121,
    frame_rate=24.0,
    num_inference_steps=30,
    generator=torch.Generator("cuda").manual_seed(42),
    output_type="np",
    output=["videos", "audio"],
)
video, audio = output["videos"], output["audio"]

encode_video(
    video[0],
    fps=24,
    output_path="ltx25_modular_full.mp4",
    audio=audio[0].float().cpu(),
    audio_sample_rate=pipe.vocoder.config.output_sampling_rate,
)

```

##  [ ](https://huggingface.co/Lightricks/LTX-2.5-Diffusers#prompting) Prompting 
The model was trained on long, single-paragraph audio-visual captions and degrades on short prompts. Describe the shot, the motion, the light and the sound in one paragraph, as the examples above do. Prompt enhancement for 2.5 uses a separate Gemma 4 checkpoint (e.g. `google/gemma-4-E2B-it`), not this repo's fine-tuned text encoder.
##  [ ](https://huggingface.co/Lightricks/LTX-2.5-Diffusers#notes) Notes 
  * Distilled (`transformer/`) is for few-step inference with an explicit `sigmas=` schedule and all guidance disabled; the full DiT (`transformer_full/`) uses step counts and real guidance.
  * The diffusion decoder denoises rather than decoding deterministically, so decoding is only reproducible with a `generator`.
  * `processor` and `prompt_enhancer` appear in `model_index.json` but are not shipped here; they load as `None`.



Downloads last month
    33,105
Safetensors[](https://huggingface.co/docs/safetensors)
Model size
19B params
Tensor type
BF16 
·
Files info
Inference Providers [NEW](https://huggingface.co/docs/inference-providers)
[ Text-to-Video ](https://huggingface.co/tasks/text-to-video "Learn more about text-to-video")
This model isn't deployed by any Inference Provider. [🙋 1 Ask for provider support](https://huggingface.co/spaces/huggingface/InferenceSupport/discussions/12734)
##  Model tree for Lightricks/LTX-2.5-Diffusers [](https://huggingface.co/docs/hub/model-cards#specifying-a-base-model)
Finetunes
[3 models](https://huggingface.co/models?other=base_model:finetune:Lightricks/LTX-2.5-Diffusers)
Quantizations
[2 models](https://huggingface.co/models?other=base_model:quantized:Lightricks/LTX-2.5-Diffusers)
##  Spaces using Lightricks/LTX-2.5-Diffusers 100
[ ![](https://cdn-avatars.huggingface.co/v1/production/uploads/669524bcbcd81f395e8f60f6/0ynfqKEWMh_dn3h4ff1K5.png) Lightricks/LTX-2.5 ](https://huggingface.co/spaces/Lightricks/LTX-2.5)[⚡ fastgpu/vram-and-gpu-cost-calculator ](https://huggingface.co/spaces/fastgpu/vram-and-gpu-cost-calculator)[🎬 Upsampler/ltx-2-5 ](https://huggingface.co/spaces/Upsampler/ltx-2-5)[🤖 RyanL22/RoboTryOn ](https://huggingface.co/spaces/RyanL22/RoboTryOn)[🎞️ hugging-apps/ltx-2-5-alpha-matte ](https://huggingface.co/spaces/hugging-apps/ltx-2-5-alpha-matte)[⚗️ ChopperBlu/ltx-2-5-demo ](https://huggingface.co/spaces/ChopperBlu/ltx-2-5-demo)[🌍 Sobhanm/ltx-video-extender ](https://huggingface.co/spaces/Sobhanm/ltx-video-extender)[🎬 WepeNerd/ltx-ripple-demo ](https://huggingface.co/spaces/WepeNerd/ltx-ripple-demo) + 95 Spaces + 92 Spaces
##  Collection including Lightricks/LTX-2.5-Diffusers
#### [LTX-2.5 Collection LTX-2.5 base models, quantized models and accompanying LoRAs and IC-LoRAs • 5 items • Updated Sep 9 • 80 ](https://huggingface.co/collections/Lightricks/ltx-25)
##  Paper for Lightricks/LTX-2.5-Diffusers
#### [LTX-2: Efficient Joint Audio-Visual Foundation Model Paper • 2601.03233 • Published Jan 6 • 203 ](https://huggingface.co/papers/2601.03233)
System theme
Company
[TOS](https://huggingface.co/terms-of-service) [Privacy](https://huggingface.co/privacy) [About](https://huggingface.co/huggingface) [Careers](https://apply.workable.com/huggingface/) [](https://huggingface.co/)
Website
[Models](https://huggingface.co/models) [Datasets](https://huggingface.co/datasets) [Spaces](https://huggingface.co/spaces) [Pricing](https://huggingface.co/pricing) [Docs](https://huggingface.co/docs)

