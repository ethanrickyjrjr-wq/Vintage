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
[ ![](https://cdn-avatars.huggingface.co/v1/production/uploads/633f7a8f4be90e06da248e0f/m5YoF33abJ09vcwFxt1Mj.png) ](https://huggingface.co/black-forest-labs)
[black-forest-labs](https://huggingface.co/black-forest-labs)
/
[FLUX.2-klein-base-9B](https://huggingface.co/black-forest-labs/FLUX.2-klein-base-9B)
Like 437
Follow
![](https://cdn-avatars.huggingface.co/v1/production/uploads/633f7a8f4be90e06da248e0f/m5YoF33abJ09vcwFxt1Mj.png) Black Forest Labs 44k
[ Image-to-Image ](https://huggingface.co/models?pipeline_tag=image-to-image)[ Diffusers ](https://huggingface.co/models?library=diffusers)[ Safetensors ](https://huggingface.co/models?library=safetensors)[ Diffusion Single File ](https://huggingface.co/models?library=diffusion-single-file)[ English ](https://huggingface.co/models?language=en)[ Flux2KleinPipeline ](https://huggingface.co/models?other=diffusers%3AFlux2KleinPipeline)[ image-generation ](https://huggingface.co/models?other=image-generation)[ image-editing ](https://huggingface.co/models?other=image-editing)[ flux ](https://huggingface.co/models?other=flux)
License: flux-non-commercial-license
[ Model card ](https://huggingface.co/black-forest-labs/FLUX.2-klein-base-9B)[ Files Files and versions xet ](https://huggingface.co/black-forest-labs/FLUX.2-klein-base-9B/tree/main)[ Community 8 ](https://huggingface.co/black-forest-labs/FLUX.2-klein-base-9B/discussions)
Deploy
Copy to bucket
Use this model
### Instructions to use black-forest-labs/FLUX.2-klein-base-9B with libraries, inference providers, notebooks, and local apps. Follow these links to get started.
  * Libraries
  * [ Diffusers](https://huggingface.co/black-forest-labs/FLUX.2-klein-base-9B?library=diffusers)
How to use black-forest-labs/FLUX.2-klein-base-9B with Diffusers:

```
pip install -U diffusers transformers accelerate
```

```
import torch
from diffusers import DiffusionPipeline
from diffusers.utils import load_image

# switch to "mps" for apple devices
pipe = DiffusionPipeline.from_pretrained("black-forest-labs/FLUX.2-klein-base-9B", dtype=torch.bfloat16, device_map="cuda")

prompt = "Turn this cat into a dog"
input_image = load_image("https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/diffusers/cat.png")

image = pipe(image=input_image, prompt=prompt).images[0]
```

  * [ Diffusion Single File](https://huggingface.co/black-forest-labs/FLUX.2-klein-base-9B?library=diffusion-single-file)
How to use black-forest-labs/FLUX.2-klein-base-9B with Diffusion Single File:

```
# No code snippets available yet for this library.

# To use this model, check the repository files and the library's documentation.

# Want to help? PRs adding snippets are welcome at:
# https://github.com/huggingface/huggingface.js
```

  * Inference
  * Inference Providers
  * Notebooks
  * [ Google Colab](https://huggingface.co/black-forest-labs/FLUX.2-klein-base-9B/colab)
  * [ Kaggle](https://huggingface.co/black-forest-labs/FLUX.2-klein-base-9B/kaggle)


##  You need to agree to share your Hugging Face information to access this model
This repository is publicly accessible, but you have to accept the conditions to access its files and content.
By clicking "Agree", you agree to the [FLUX Non-Commercial License Agreement](https://huggingface.co/black-forest-labs/LICENSE.md) and acknowledge the [Acceptable Use Policy](https://bfl.ai/legal/usage-policy).
[Log in](https://huggingface.co/login?next=%2Fblack-forest-labs%2FFLUX.2-klein-base-9B) or [Sign Up](https://huggingface.co/join?next=%2Fblack-forest-labs%2FFLUX.2-klein-base-9B) to review the conditions and access this model content.
  * [**Key Features**](https://huggingface.co/black-forest-labs/FLUX.2-klein-base-9B#key-features "Key Features")
  * [**Usage**](https://huggingface.co/black-forest-labs/FLUX.2-klein-base-9B#usage "Usage")
    * [**Using with Diffusers 🧨**](https://huggingface.co/black-forest-labs/FLUX.2-klein-base-9B#using-with-diffusers-%F0%9F%A7%A8 "Using with Diffusers 🧨")


[![Teaser](https://huggingface.co/black-forest-labs/FLUX.2-klein-base-9B/media/main/realism.jpg)](https://huggingface.co/black-forest-labs/FLUX.2-klein-base-9B/blob/main/realism.jpg) [![Teaser](https://huggingface.co/black-forest-labs/FLUX.2-klein-base-9B/media/main/editing.jpg)](https://huggingface.co/black-forest-labs/FLUX.2-klein-base-9B/blob/main/editing.jpg) [![Teaser](https://huggingface.co/black-forest-labs/FLUX.2-klein-base-9B/media/main/others.jpg)](https://huggingface.co/black-forest-labs/FLUX.2-klein-base-9B/blob/main/others.jpg)
The FLUX.2 [klein] model family are our fastest image models to date. FLUX.2 [klein] unifies generation and editing in a single compact architecture, **delivering state-of-the-art quality with end-to-end inference in as low as under a second**. Built for applications that require real-time image generation without sacrificing quality, and runs on consumer hardware.
FLUX.2 [klein] 9B Base is a 9 billion parameter rectified flow transformer capable of generating images from text descriptions and supports multi-reference editing capabilities.
It's a full-capacity foundation model. Undistilled, preserving complete training signal for maximum flexibility. Ideal for fine-tuning, LoRA training, research, and custom pipelines where control matters more than speed. Higher output diversity than the distilled models.
For more information, please read our [blog post](https://bfl.ai/blog/flux2-klein-towards-interactive-visual-intelligence).
#  [ ](https://huggingface.co/black-forest-labs/FLUX.2-klein-base-9B#key-features) **Key Features**
  1. Undistilled foundation model for maximum flexibility and control.
  2. Best suited for creative exploration, fine-tuning, LoRA training, research, and custom image generation or editing pipelines.
  3. Trained without step or guidance distillation, making FLUX.2 [klein] 9B Base more efficient and flexible.
  4. Open weights for customization and fine-tuning to drive science, research, and empower artists to iterate with speed.


#  [ ](https://huggingface.co/black-forest-labs/FLUX.2-klein-base-9B#usage) **Usage**
We provide a reference implementation of FLUX.2 [klein] 9B Base, as well as sampling code, in a dedicated [GitHub repository](https://github.com/black-forest-labs/flux2). Developers and creatives looking to build on top of FLUX.2 [klein] 9B Base are encouraged to use this as a starting point.
FLUX.2 [klein] 9B Base is also available in both [ComfyUI](https://github.com/comfyanonymous/ComfyUI) and [Diffusers](https://github.com/huggingface/diffusers).
##  [ ](https://huggingface.co/black-forest-labs/FLUX.2-klein-base-9B#using-with-diffusers-%F0%9F%A7%A8) **Using with Diffusers 🧨**
To use FLUX.2 [klein] 9B Base with the 🧨 Diffusers python library, first install or upgrade diffusers:

```
pip install git+https://github.com/huggingface/diffusers.git

```

Then you can use Flux2KleinPipeline to run the model:

```
import torch
from diffusers import Flux2KleinPipeline

device = "cuda"
dtype = torch.bfloat16

pipe = Flux2KleinPipeline.from_pretrained("black-forest-labs/FLUX.2-klein-base-9B", torch_dtype=dtype)
pipe.enable_model_cpu_offload()  # save some VRAM by offloading the model to CPU

prompt = "A cat holding a sign that says hello world"
image = pipe(
    prompt=prompt,
    height=1024,
    width=1024,
    guidance_scale=4.0,
    num_inference_steps=50,
    generator=torch.Generator(device=device).manual_seed(0)
).images[0]
image.save("flux-klein.png")

```

* * *
Limitations
  * This model is not intended or able to provide factual information.
  * While the model can output text, text rendered may be inaccurate or subject to distortion.
  * As a statistical model, this checkpoint may represent or amplify biases observed in the training data.
  * The model may fail to generate output that matches the prompts.
  * Prompt following is heavily influenced by the prompting style.


Out-of-Scope Use
The model and its derivatives may not be used:
  * In any way that violates applicable law.
  * For the purpose of exploiting, harming or attempting to exploit or harm minors in any way; including but not limited to the solicitation, creation, acquisition, or dissemination of child exploitative content.
  * To generate or disseminate deceptive, fraudulent, misleading or otherwise harmful content.
  * To generate or disseminate personal identifiable information that can be used to harm an individual.
  * To harass, abuse, threaten, stalk, or bully individuals or groups of individuals.
  * To create non-consensual intimate imagery or illegal pornographic content.
  * For fully automated decision making or high risk applications that adversely impact an individual's legal rights or otherwise create or modify a binding, enforceable obligation.


Nothing contained in this Model Card should be interpreted as or deemed a restriction or modification to the license the model is released under.
Hardware
The FLUX.2 [klein] 9B Base model fits in ~29GB VRAM and is accessible on NVIDIA RTX 4090 and above.
* * *
Responsible AI Development
Black Forest Labs is committed to the responsible development and deployment of our models. Prior to releasing the FLUX.2 family of models, we evaluated and mitigated a number of risks in our model checkpoints and hosted services, including the generation of unlawful content, including child sexual abuse material (CSAM) and nonconsensual intimate imagery (NCII). We implemented a series of pre-release mitigations to help prevent misuse by third parties, with additional post-release mitigations to help address residual risks:
  1. Pre-training mitigation. We filtered pre-training data for multiple categories of "not safe for work" (NSFW) and known child sexual abuse material (CSAM) to help prevent a user generating unlawful content in response to text prompts or uploaded images. We have partnered with the <https://www.iwf.org.uk/>, an independent nonprofit organization dedicated to preventing online abuse, to filter known CSAM from the training data.
  2. Post-training mitigation. Subsequently, we undertook multiple rounds of targeted fine-tuning to provide additional mitigation against potential abuse, including both text-to-image (T2I) and image-to-image (I2I) attacks. By inhibiting certain behaviors and suppressing certain concepts in the trained model, these techniques can help to prevent a user generating synthetic CSAM or NCII from a text prompt, or transforming an uploaded image into synthetic CSAM or NCII.
  3. Ongoing evaluation. Throughout this process, we conducted multiple internal and external third-party evaluations of model checkpoints to identify further opportunities for mitigation. External third-party evaluations focused on eliciting CSAM and NCII through adversarial testing with (i) text-only prompts, (ii) a single uploaded reference image with text prompts, and (iii) multiple uploaded reference images with text prompts. Based on this feedback, we conducted further safety fine-tuning to produce our open-weight FLUX.2 [klein] models.
  4. Release decision. After safety fine-tuning and prior to release, we conducted a final third-party evaluation of the proposed release checkpoints, focused on T2I and I2I generation of synthetic CSAM and NCII, including a comparison with other open-weight T2I and I2I models. The final FLUX.2 [klein] checkpoints demonstrated high resilience against violative inputs in complex generation and editing tasks, and demonstrated higher resilience than leading open-weight models across these risk categories. Based on these findings, we approved the release of the open-weight FLUX.2 [klein] 4B models under an Apache 2.0 license and the release of the FLUX.2 [klein] 9B models under a non-commercial license to support third-party research and development.
  5. Inference filters. The repository for the FLUX.2 [klein] models includes filters for NSFW and protected content in inputs and outputs. Filters or manual review must be used with the FLUX.2 [klein] 9B models under the terms of the FLUX Non-Commercial License, and we encourage deployers to implement these mitigations when using the FLUX.2 [klein] 4B models. Where we implement these features on our own hosted services, we may apply multiple filters to intercept text prompts, uploaded images, and output images. We utilize both in-house and third-party filters to mitigate against harmful outputs, such as CSAM and NCII outputs, including filters provided by <https://thehive.ai/> and <https://www.microsoft.com/>.
  6. Content provenance. Content provenance features can help users and platforms better identify, label, and interpret AI-generated content online. The inference code for FLUX.2 [klein] implements an example of pixel-layer watermarking. Additionally, this repository includes links to the <https://c2pa.org/> standard for metadata. The API for FLUX.2 [klein] applies cryptographically-signed C2PA metadata to downloaded output content to indicate that images were produced with our model.
  7. Policies. Acceptable use of our models and access to our API are governed by policies set out in applicable documentation, including FLUX Non-Commercial License (for our non-commercial open-weight users); Developer Terms of Service, Self-Hosted Commercial License Terms, and Usage Policy (for our commercial open-weight model users); and Developer Terms of Service, FLUX API Service Terms, and Usage Policy (for our API users). These prohibit the generation of unlawful content or the use of generated content for unlawful, defamatory, or abusive purposes. Developers and users must consent to these conditions to access the FLUX.2 [klein] 9B models on Hugging Face.
  8. Safety. Black Forest Labs takes model safety seriously. We may monitor use to detect misuse or abuse of our models and services. We provide a dedicated email address (safety@blackforestlabs.ai) to solicit feedback from the community. We maintain a reporting relationship with organizations such as the <https://www.iwf.org.uk/> and the <https://www.missingkids.org/>, and welcome ongoing engagement with authorities, developers, and researchers to share intelligence about emerging risks and develop effective mitigations.


* * *
License
This model falls under the [FLUX Non-Commercial License](https://huggingface.co/black-forest-labs/FLUX.2-klein-base-9B/blob/main/LICENSE.md).
Trademarks & IP
This project may contain trademarks or logos for projects, products, or services. Use of Black Forest Labs and FLUX trademarks or logos in modified versions of this project must not cause confusion or imply sponsorship or endorsement. Any use of third-party trademarks, intellectual property or logos are subject to those third-party's policies. 

Downloads last month
    77,703
Safetensors[](https://huggingface.co/docs/safetensors)
Model size
9B params
Tensor type
BF16 
·
Files info
Inference Providers [NEW](https://huggingface.co/docs/inference-providers)
fal
  *   * 

[ Image-to-Image ](https://huggingface.co/tasks/image-to-image "Learn more about image-to-image")
Drag image file here or click to browse from your device
Browse for image
(Optional) Text-guidance if the model has support for it Generate
View Code Snippets
Maximize
##  Model tree for black-forest-labs/FLUX.2-klein-base-9B [](https://huggingface.co/docs/hub/model-cards#specifying-a-base-model)
Adapters
[96 models](https://huggingface.co/models?other=base_model:adapter:black-forest-labs/FLUX.2-klein-base-9B)
Finetunes
[26 models](https://huggingface.co/models?other=base_model:finetune:black-forest-labs/FLUX.2-klein-base-9B)
Quantizations
[17 models](https://huggingface.co/models?other=base_model:quantized:black-forest-labs/FLUX.2-klein-base-9B)
##  Spaces using black-forest-labs/FLUX.2-klein-base-9B 99
[ ![](https://cdn-avatars.huggingface.co/v1/production/uploads/633f7a8f4be90e06da248e0f/m5YoF33abJ09vcwFxt1Mj.png) black-forest-labs/FLUX.2-klein-9B ](https://huggingface.co/spaces/black-forest-labs/FLUX.2-klein-9B)[🎨 sotinhoss/manga-color-studio ](https://huggingface.co/spaces/sotinhoss/manga-color-studio)[🖼 FoxLoverAI/TurboCustomImageEditing ](https://huggingface.co/spaces/FoxLoverAI/TurboCustomImageEditing)[💻 Lakonik/AsymFLUX.2-klein ](https://huggingface.co/spaces/Lakonik/AsymFLUX.2-klein)[🎁 linoyts/FLUX.2-klein-Move ](https://huggingface.co/spaces/linoyts/FLUX.2-klein-Move)[🦀 cronos3k/CharacterForgePro ](https://huggingface.co/spaces/cronos3k/CharacterForgePro)[💻 Dishku/FLUX.2-klein-9B ](https://huggingface.co/spaces/Dishku/FLUX.2-klein-9B)[👁 sean96t/flux2-try-on ](https://huggingface.co/spaces/sean96t/flux2-try-on) + 94 Spaces + 91 Spaces
##  Collection including black-forest-labs/FLUX.2-klein-base-9B
#### [FLUX.2 Collection Our second generation of FLUX • 21 items • Updated Apr 6 • 292 ](https://huggingface.co/collections/black-forest-labs/flux2)
System theme
Company
[TOS](https://huggingface.co/terms-of-service) [Privacy](https://huggingface.co/privacy) [About](https://huggingface.co/huggingface) [Careers](https://apply.workable.com/huggingface/) [](https://huggingface.co/)
Website
[Models](https://huggingface.co/models) [Datasets](https://huggingface.co/datasets) [Spaces](https://huggingface.co/spaces) [Pricing](https://huggingface.co/pricing) [Docs](https://huggingface.co/docs)
Inference providers allow you to run inference using different serverless providers.
You have to accept the conditions to access the files info

