Source: https://huggingface.co/Lightricks/LTX-2.5-22b-LoRA-Cinemagraph (fetched 2026-11-13 with crawl4ai)

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
[LTX-2.5-22b-LoRA-Cinemagraph](https://huggingface.co/Lightricks/LTX-2.5-22b-LoRA-Cinemagraph)
Like 44
Follow
![](https://cdn-avatars.huggingface.co/v1/production/uploads/669524bcbcd81f395e8f60f6/0ynfqKEWMh_dn3h4ff1K5.png) LTX.io 6.73k
[ Image-to-Video ](https://huggingface.co/models?pipeline_tag=image-to-video)[ Diffusion Single File ](https://huggingface.co/models?library=diffusion-single-file)[ LTX-2 ](https://huggingface.co/models?library=ltx)[ English ](https://huggingface.co/models?language=en)[ cinemagraph ](https://huggingface.co/models?other=cinemagraph)[ i2v ](https://huggingface.co/models?other=i2v)[ lora ](https://huggingface.co/models?other=lora)[ ltx-2.5 ](https://huggingface.co/models?other=ltx-2.5)[ motion-design ](https://huggingface.co/models?other=motion-design)[ selective-motion ](https://huggingface.co/models?other=selective-motion)
License: ltx-2.x-community-license
[ Model card ](https://huggingface.co/Lightricks/LTX-2.5-22b-LoRA-Cinemagraph)[ Files Files and versions xet ](https://huggingface.co/Lightricks/LTX-2.5-22b-LoRA-Cinemagraph/tree/main)[ Community ](https://huggingface.co/Lightricks/LTX-2.5-22b-LoRA-Cinemagraph/discussions)
Deploy
Copy to bucket
Use this model
### Instructions to use Lightricks/LTX-2.5-22b-LoRA-Cinemagraph with libraries, inference providers, notebooks, and local apps. Follow these links to get started.
  * Libraries
  * [ Diffusion Single File](https://huggingface.co/Lightricks/LTX-2.5-22b-LoRA-Cinemagraph?library=diffusion-single-file)
How to use Lightricks/LTX-2.5-22b-LoRA-Cinemagraph with Diffusion Single File:

```
# No code snippets available yet for this library.

# To use this model, check the repository files and the library's documentation.

# Want to help? PRs adding snippets are welcome at:
# https://github.com/huggingface/huggingface.js
```

  * [ LTX-2](https://huggingface.co/Lightricks/LTX-2.5-22b-LoRA-Cinemagraph?library=ltx)
How to use Lightricks/LTX-2.5-22b-LoRA-Cinemagraph with LTX-2:

```
# Install the LTX-2 pipelines
git clone https://github.com/Lightricks/LTX-2.git
cd LTX-2
uv sync --extra natten
```

```
# Download the adapter weights from this repo
# (base components come from Lightricks/LTX-2.5 — see Files and versions)
hf download Lightricks/LTX-2.5-22b-LoRA-Cinemagraph --local-dir models/LTX-2.5-22b-LoRA-Cinemagraph
```

```
# Text/image-to-video with the LoRA on the distilled LTX-2.5 pipeline
uv run python -m ltx_pipelines.distilled \
    --transformer-path path/to/distilled-transformer.safetensors \
    --text-encoder-path path/to/gemma4-12b-with-proj-ltx-2.5-bf16.safetensors \
    --video-vae-path path/to/video-vae.safetensors \
    --audio-vae-path path/to/audio-vae.safetensors \
    --spatial-upsampler-path path/to/spatial-upsampler.safetensors \
    --lora models/LTX-2.5-22b-LoRA-Cinemagraph/<weights>.safetensors 1.0 \
    --prompt "your prompt here" \
    --output-path output.mp4
# For image-to-video, add: --image path/to/image.jpg 0 0.8
```

  * Notebooks
  * [ Google Colab](https://huggingface.co/Lightricks/LTX-2.5-22b-LoRA-Cinemagraph/colab)
  * [ Kaggle](https://huggingface.co/Lightricks/LTX-2.5-22b-LoRA-Cinemagraph/kaggle)


##  You need to agree to share your Hugging Face information to access this model
By clicking "Agree and Access" you acknowledge the [Privacy Policy](https://static.lightricks.com/legal/Privacy%20Policy%20-%20LTX%20Platform.pdf) and consent to receive offers and updates including targeted and personalized advertisements. You can unsubscribe at any time.
[Log in](https://huggingface.co/login?next=/Lightricks/LTX-2.5-22b-LoRA-Cinemagraph) or [Sign Up](https://huggingface.co/join?next=/Lightricks/LTX-2.5-22b-LoRA-Cinemagraph) to review the conditions and access this model content.
  * [Cinemagraph](https://huggingface.co/Lightricks/LTX-2.5-22b-LoRA-Cinemagraph#cinemagraph "Cinemagraph")
    * [Example Outputs](https://huggingface.co/Lightricks/LTX-2.5-22b-LoRA-Cinemagraph#example-outputs "Example Outputs")
    * [Model Files](https://huggingface.co/Lightricks/LTX-2.5-22b-LoRA-Cinemagraph#model-files "Model Files")
    * [Model Details](https://huggingface.co/Lightricks/LTX-2.5-22b-LoRA-Cinemagraph#model-details "Model Details")
    * [Intended Use & Out-of-Scope](https://huggingface.co/Lightricks/LTX-2.5-22b-LoRA-Cinemagraph#intended-use--out-of-scope "Intended Use &amp; Out-of-Scope")
    * [How It Works](https://huggingface.co/Lightricks/LTX-2.5-22b-LoRA-Cinemagraph#how-it-works "How It Works")
    * [Usage](https://huggingface.co/Lightricks/LTX-2.5-22b-LoRA-Cinemagraph#usage "Usage")
      * [🔌 ComfyUI](https://huggingface.co/Lightricks/LTX-2.5-22b-LoRA-Cinemagraph#%F0%9F%94%8C-comfyui "🔌 ComfyUI")
    * [Recommended Settings](https://huggingface.co/Lightricks/LTX-2.5-22b-LoRA-Cinemagraph#recommended-settings "Recommended Settings")
    * [Tips & Troubleshooting](https://huggingface.co/Lightricks/LTX-2.5-22b-LoRA-Cinemagraph#tips--troubleshooting "Tips &amp; Troubleshooting")
    * [Dataset](https://huggingface.co/Lightricks/LTX-2.5-22b-LoRA-Cinemagraph#dataset "Dataset")
    * [Training](https://huggingface.co/Lightricks/LTX-2.5-22b-LoRA-Cinemagraph#training "Training")
    * [References](https://huggingface.co/Lightricks/LTX-2.5-22b-LoRA-Cinemagraph#references "References")
    * [License](https://huggingface.co/Lightricks/LTX-2.5-22b-LoRA-Cinemagraph#license "License")
    * [Acknowledgments](https://huggingface.co/Lightricks/LTX-2.5-22b-LoRA-Cinemagraph#acknowledgments "Acknowledgments")


#  [ ](https://huggingface.co/Lightricks/LTX-2.5-22b-LoRA-Cinemagraph#cinemagraph) Cinemagraph 
Transforms still images into smooth, looping cinemagraphs with selective motion while keeping the rest of the scene frozen.
It is based on the [LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5) foundation model.
##  [ ](https://huggingface.co/Lightricks/LTX-2.5-22b-LoRA-Cinemagraph#example-outputs) Example Outputs  

Prompt 
    CINEMAGRAPH_MOTION, tripod locked-off static camera, zero camera movement, the man, face, hair, clothing, beach, sky, and background remain completely frozen, only the beach reflection inside his sunglasses moves, reflected time-lapse of ocean waves roll and shimmer in the lenses, everything outside the glasses stays still, seamless natural loop 

Prompt 
    CINEMAGRAPH_MOTION, tripod locked-off static camera, zero camera movement, the man and cow remain completely frozen, only the clouds in the sky move in fast time-lapse, clouds drift and roll across the sky, grass and foreground remain still, seamless natural loop. 

Prompt 
    CINEMAGRAPH_MOTION, tripod locked-off static camera, zero camera movement, the woman is frozen, her face, eyes, hair, clothing, seat, and airplane interior remain completely frozen, only the illustrated tear drops move downward along her cheeks like a cutout collage animation, seamless natural loop.
##  [ ](https://huggingface.co/Lightricks/LTX-2.5-22b-LoRA-Cinemagraph#model-files) Model Files 
`ltx-2.5-22b-lora-cinemagraph-0.9.safetensors`
##  [ ](https://huggingface.co/Lightricks/LTX-2.5-22b-LoRA-Cinemagraph#model-details) Model Details 
  * **Base Model:** LTX-2.5-22B Video
  * **Training Type:** LoRA
  * **Modality:** image-to-video


##  [ ](https://huggingface.co/Lightricks/LTX-2.5-22b-LoRA-Cinemagraph#intended-use--out-of-scope) Intended Use & Out-of-Scope 
**Intended use:** Creating cinemagraph videos from still images — producing looping videos with selective motion (water, light, elements) while keeping the rest of the scene static. Ideal for creating animated wallpapers, social media content, and artistic motion pieces.
**Out of scope:** Scenes with camera movement, character/body movement, complex dynamic scenes, videos with multiple moving subjects. The LoRA is optimized for static-camera, single-element-motion scenarios.
##  [ ](https://huggingface.co/Lightricks/LTX-2.5-22b-LoRA-Cinemagraph#how-it-works) How It Works 
This LoRA fine-tunes LTX-2.5 to generate cinemagraph-style videos from still images. It excels at creating smooth, continuous-loop animations where only specific elements move (water flowing, neon lights pulsing, rain falling, reflections shimmering) while the rest of the frame remains completely frozen. The model learns to respect spatial isolation — keeping backgrounds, people, and static objects completely still while animating only the designated element.
The training dataset consisted of "no moving people" scenarios with locked-off cameras, so the LoRA strongly respects composition and avoids unwanted motion outside the intended subject.
##  [ ](https://huggingface.co/Lightricks/LTX-2.5-22b-LoRA-Cinemagraph#usage) Usage 
###  [ ](https://huggingface.co/Lightricks/LTX-2.5-22b-LoRA-Cinemagraph#%F0%9F%94%8C-comfyui) 🔌 ComfyUI 
  1. Copy the LoRA weights into `models/loras`.
  2. Load the **LTX-2.5-22B** base model.
  3. Add `ltx-2.5-22b-lora-cinemagraph-0.9.safetensors` as the LoRA.
  4. Use the [T2V/I2V workflow](https://github.com/Lightricks/ComfyUI-LTXVideo/blob/master/example_workflows/2.5/LTX-2.5_T2V_I2V_Single_Stage_Distilled.json) from the [ComfyUI-LTXVideo repository](https://github.com/Lightricks/ComfyUI-LTXVideo/).
  5. Start with LoRA strength `1.0–1.2` (the sweet spot) and adjust within `0.5–1.5` per generation.
  6. Include the trigger word `CINEMAGRAPH_MOTION` in the positive prompt.


##  [ ](https://huggingface.co/Lightricks/LTX-2.5-22b-LoRA-Cinemagraph#recommended-settings) Recommended Settings 
  * **LoRA strength / weight:** `0.5–1.5` (sweet spot: `1.0–1.2`)
  * **Spatial Guidance (STG):** Use `stg_v` mode, scale `1.0`, targeting block `29` for enhanced motion control and boundary preservation.
  * **Inference steps:** 30 (from training validation)
  * **Guidance scale:** 4.0
  * **Prompting:** See examples below. The model responds well to explicit descriptions of what should move and what should remain still. Emphasize "locked-off static camera" and "seamless natural loop" for best results.


Example positive prompt:

```
CINEMAGRAPH_MOTION, tripod locked-off static camera, zero camera movement, only the neon sign flickers, the starburst, Desert, MOTEL, and NO VACANCY neon tubes subtly pulse and flicker like a real vintage neon sign, everything else stays perfectly still, seamless natural loop

```

Example negative prompt:

```
cars moving, camera movement, pan, tilt, zoom, parallax, whole image moving, background sliding, person moving, flicker on entire image, noisy texture, crawling texture, distorted, blurry, low quality

```

##  [ ](https://huggingface.co/Lightricks/LTX-2.5-22b-LoRA-Cinemagraph#tips--troubleshooting) Tips & Troubleshooting 
  * **Explicit motion boundaries:** Be very specific about what moves and what doesn't. "Only the [element] moves; everything else frozen" works better than vague descriptions.
  * **Avoid camera language:** The LoRA was trained on static-camera footage. Omit phrases like "camera movement," "pan," "zoom," and "parallax."
  * **Seamless loops:** Use "seamless natural loop" or "continuous looping motion" in the prompt to encourage cyclical, repeating movement.
  * **Strength tuning:** The usable range is `0.5–1.5`. `0.5` is conservative; `1.0–1.2` is the sweet spot; pushing toward `1.5` drives selective motion more aggressively. Test within the range for your use case.
  * **Resolution:** Best results at 512×704 pixels, 25 frames (the training resolution).


##  [ ](https://huggingface.co/Lightricks/LTX-2.5-22b-LoRA-Cinemagraph#dataset) Dataset 
**Cinemagraph (No Moving People)** — A carefully curated collection of still images and video references designed for cinemagraph creation. The dataset emphasizes scenes with selective motion elements (flowing water, flickering neon, falling leaves, shimmering light reflections) while keeping characters, backgrounds, and static objects completely frozen. All scenes were shot with locked-off, tripod-mounted static cameras to eliminate parallax and camera drift.
##  [ ](https://huggingface.co/Lightricks/LTX-2.5-22b-LoRA-Cinemagraph#training) Training 
  * **Technique:** LoRA fine-tuning on LTX-2.5-22B using the [LTX-2 Community Trainer](https://github.com/Lightricks/LTX-2/tree/main/packages/ltx-trainer).
  * **Hyperparameters:** learning_rate=0.0001, batch_size=1, gradient_accumulation_steps=1, optimizer=adamw8bit, scheduler=cosine, rank=32, alpha=32, dropout=0.0
  * **Steps:** 1000
  * **Infrastructure:** [LTX-2 Community Trainer](https://github.com/Lightricks/LTX-2/tree/main/packages/ltx-trainer).


##  [ ](https://huggingface.co/Lightricks/LTX-2.5-22b-LoRA-Cinemagraph#references) References 
  * **Code:** [GitHub Repository](https://github.com/Lightricks/LTX-2)
  * **ComfyUI:** [ComfyUI-LTXVideo](https://github.com/Lightricks/ComfyUI-LTXVideo/)


##  [ ](https://huggingface.co/Lightricks/LTX-2.5-22b-LoRA-Cinemagraph#license) License 
See the **[LTX-2.x Community License](https://github.com/Lightricks/LTX-2/blob/main/LICENSE-2_x)** for full terms.
##  [ ](https://huggingface.co/Lightricks/LTX-2.5-22b-LoRA-Cinemagraph#acknowledgments) Acknowledgments 
  * Base model by **[Lightricks](https://ltx.io/)**
  * Training infrastructure: **[LTX-2 Community Trainer](https://github.com/Lightricks/LTX-2/tree/main/packages/ltx-trainer)**



Downloads last month
    5,893
Inference Providers [NEW](https://huggingface.co/docs/inference-providers)
[ Image-to-Video ](https://huggingface.co/tasks/image-to-video "Learn more about image-to-video")
This model isn't deployed by any Inference Provider. [🙋 Ask for provider support](https://huggingface.co/spaces/huggingface/InferenceSupport/discussions/new?title=Lightricks/LTX-2.5-22b-LoRA-Cinemagraph&description=React%20to%20this%20comment%20with%20an%20emoji%20to%20vote%20for%20%5BLightricks%2FLTX-2.5-22b-LoRA-Cinemagraph%5D\(%2FLightricks%2FLTX-2.5-22b-LoRA-Cinemagraph\)%20to%20be%20supported%20by%20Inference%20Providers.%0A%0A\(optional\)%20Which%20providers%20are%20you%20interested%20in%3F%20\(Novita%2C%20Hyperbolic%2C%20Together%E2%80%A6\)%0A)
##  Model tree for Lightricks/LTX-2.5-22b-LoRA-Cinemagraph [](https://huggingface.co/docs/hub/model-cards#specifying-a-base-model)
Base model
[Lightricks/LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5)
Adapter
([44](https://huggingface.co/models?other=base_model:adapter:Lightricks/LTX-2.5))
this model
##  Spaces using Lightricks/LTX-2.5-22b-LoRA-Cinemagraph 3
[🖖 singsenochian/trek-160-cinemagraph-lab ](https://huggingface.co/spaces/singsenochian/trek-160-cinemagraph-lab)[🐢 X-HighVoltage-X/LTX-2.5-Multi-Pipe ](https://huggingface.co/spaces/X-HighVoltage-X/LTX-2.5-Multi-Pipe)[🎞️ abidlabs/ltx-2.5-animate-an-image ](https://huggingface.co/spaces/abidlabs/ltx-2.5-animate-an-image)
##  Collection including Lightricks/LTX-2.5-22b-LoRA-Cinemagraph
#### [LTX-2.5 Creative Lab Collection 15 items • Updated Oct 1 • 37 ](https://huggingface.co/collections/Lightricks/ltx-25-creative-lab)
System theme
Company
[TOS](https://huggingface.co/terms-of-service) [Privacy](https://huggingface.co/privacy) [About](https://huggingface.co/huggingface) [Careers](https://apply.workable.com/huggingface/) [](https://huggingface.co/)
Website
[Models](https://huggingface.co/models) [Datasets](https://huggingface.co/datasets) [Spaces](https://huggingface.co/spaces) [Pricing](https://huggingface.co/pricing) [Docs](https://huggingface.co/docs)

