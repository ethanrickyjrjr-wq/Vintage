[![Hugging Face's logo](https://huggingface.co/front/assets/huggingface_logo-noborder.svg) Hugging Face](https://huggingface.co/)
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
[flux-3-image-klein](https://huggingface.co/black-forest-labs/flux-3-image-klein)
Like 735
Follow
![](https://cdn-avatars.huggingface.co/v1/production/uploads/633f7a8f4be90e06da248e0f/m5YoF33abJ09vcwFxt1Mj.png) Black Forest Labs 43.5k
[ Image-to-Image ](https://huggingface.co/models?pipeline_tag=image-to-image)[ Diffusers ](https://huggingface.co/models?library=diffusers)[ Safetensors ](https://huggingface.co/models?library=safetensors)[ English ](https://huggingface.co/models?language=en)[ image-generation ](https://huggingface.co/models?other=image-generation)[ image-editing ](https://huggingface.co/models?other=image-editing)[ flux ](https://huggingface.co/models?other=flux)[ flux-3 ](https://huggingface.co/models?other=flux-3)[ black-forest-labs ](https://huggingface.co/models?other=black-forest-labs)
License: flux-kommunity-license
[ Model card ](https://huggingface.co/black-forest-labs/flux-3-image-klein)[ Files Files and versions xet ](https://huggingface.co/black-forest-labs/flux-3-image-klein/tree/main)[ Community 12 ](https://huggingface.co/black-forest-labs/flux-3-image-klein/discussions)
Deploy
Copy to bucket
Use this model
### Instructions to use black-forest-labs/flux-3-image-klein with libraries, inference providers, notebooks, and local apps. Follow these links to get started.
  * Libraries
  * [ Diffusers](https://huggingface.co/black-forest-labs/flux-3-image-klein?library=diffusers)
How to use black-forest-labs/flux-3-image-klein with Diffusers:

```
pip install -U diffusers transformers accelerate
```

```
import torch
from diffusers import DiffusionPipeline
from diffusers.utils import load_image

# switch to "mps" for apple devices
pipe = DiffusionPipeline.from_pretrained("black-forest-labs/flux-3-image-klein", dtype=torch.bfloat16, device_map="cuda")

prompt = "Turn this cat into a dog"
input_image = load_image("https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/diffusers/cat.png")

image = pipe(image=input_image, prompt=prompt).images[0]
```

  * Notebooks
  * [ Google Colab](https://huggingface.co/black-forest-labs/flux-3-image-klein/colab)
  * [ Kaggle](https://huggingface.co/black-forest-labs/flux-3-image-klein/kaggle)


##  You need to agree to share your Hugging Face information to access this model
This repository is publicly accessible, but you have to accept the conditions to access its files and content.
[Log in](https://huggingface.co/login?next=%2Fblack-forest-labs%2Fflux-3-image-klein) or [Sign Up](https://huggingface.co/join?next=%2Fblack-forest-labs%2Fflux-3-image-klein) to review the conditions and access this model content.
  * [FLUX 3 Image Klein](https://huggingface.co/black-forest-labs/flux-3-image-klein#flux-3-image-klein "FLUX 3 Image Klein")
    * [Key Features](https://huggingface.co/black-forest-labs/flux-3-image-klein#key-features "Key Features")
    * [Download](https://huggingface.co/black-forest-labs/flux-3-image-klein#download "Download")
    * [Using with reference code](https://huggingface.co/black-forest-labs/flux-3-image-klein#using-with-reference-code "Using with reference code")
    * [Using with Diffusers](https://huggingface.co/black-forest-labs/flux-3-image-klein#using-with-diffusers "Using with Diffusers")
      * [Prompt upsampling](https://huggingface.co/black-forest-labs/flux-3-image-klein#prompt-upsampling "Prompt upsampling")
    * [Prompting](https://huggingface.co/black-forest-labs/flux-3-image-klein#prompting "Prompting")
    * [Limitations](https://huggingface.co/black-forest-labs/flux-3-image-klein#limitations "Limitations")
    * [Hardware](https://huggingface.co/black-forest-labs/flux-3-image-klein#hardware "Hardware")
    * [Out-of-scope use](https://huggingface.co/black-forest-labs/flux-3-image-klein#out-of-scope-use "Out-of-scope use")
    * [Responsible AI Development](https://huggingface.co/black-forest-labs/flux-3-image-klein#responsible-ai-development "Responsible AI Development")
    * [License](https://huggingface.co/black-forest-labs/flux-3-image-klein#license "License")
    * [Trademarks and IP](https://huggingface.co/black-forest-labs/flux-3-image-klein#trademarks-and-ip "Trademarks and IP")
    * [Citation](https://huggingface.co/black-forest-labs/flux-3-image-klein#citation "Citation")


#  [ ](https://huggingface.co/black-forest-labs/flux-3-image-klein#flux-3-image-klein) FLUX 3 Image Klein 
[![Launch gallery](https://huggingface.co/black-forest-labs/flux-3-image-klein/media/main/launch-gallery.jpg)](https://huggingface.co/black-forest-labs/flux-3-image-klein/blob/main/launch-gallery.jpg)
[![Teaser](https://huggingface.co/black-forest-labs/flux-3-image-klein/media/main/teaser.jpg)](https://huggingface.co/black-forest-labs/flux-3-image-klein/blob/main/teaser.jpg)
FLUX 3 Image Klein is a 5.6B open weights model for text-to-image generation and image editing. It takes a prompt and up to 10 reference images and returns one image. Text-to-image, single-reference edits and multi-reference compositions run through the same model, with Qwen3-VL-4B-Instruct as the text encoder.
The 5.6B parameter label refers to the image transformer; the text encoder is separate.
This repository holds the distilled checkpoint for generation and image editing. For fine-tuning, LoRA training and research, use [FLUX 3 Image Klein Base](https://huggingface.co/black-forest-labs/flux-3-image-klein-base).
Inference code, prompt upsampling and the bounding box format: [black-forest-labs/flux-3-image-klein](https://github.com/black-forest-labs/flux-3-image-klein) on GitHub.
**Do not use the model without a prompt upsampler.** FLUX 3 Image Klein takes full scene captions, for text-to-image, editing and layout with boxes alike; a short prompt sent as typed gives generic output. Use ours, [flux-3-image-klein-pup](https://huggingface.co/black-forest-labs/flux-3-image-klein-pup), which the reference code loads by default, or any LLM you prefer with a system prompt that expands the request into one full scene caption ([`system_prompts.json`](https://huggingface.co/black-forest-labs/flux-3-image-klein-pup/blob/main/system_prompts.json) has ours). Diffusers runs neither on its own; see [Prompt upsampling](https://huggingface.co/black-forest-labs/flux-3-image-klein#prompt-upsampling).
This repository includes the BF16 transformer and [FP8](https://huggingface.co/black-forest-labs/flux-3-image-klein/tree/main/variants/fp8r) and [NVFP4](https://huggingface.co/black-forest-labs/flux-3-image-klein/tree/main/variants/nvfp4) variants, together with the Qwen3-VL-4B-Instruct text encoder and image autoencoder.  
| Checkpoint  | Format  | Steps  | Guidance  | Built for  |  
| --- | --- | --- | --- | --- |  
| [Klein Base](https://huggingface.co/black-forest-labs/flux-3-image-klein-base)  | undistilled, bfloat16  | 50  | 3.5  | fine-tuning, LoRA training, research  |  
| [Klein](https://huggingface.co/black-forest-labs/flux-3-image-klein)  | distilled, bfloat16  | 16  | none  | generation and editing, self-hosting; the checkpoint behind the BFL API  |  
##  [ ](https://huggingface.co/black-forest-labs/flux-3-image-klein#key-features) Key Features 
  1. Text-to-image, single-reference editing and multi-reference generation in one model.
  2. Bounding boxes in the prompt. Place elements with boxes on a 0 to 1000 grid, then recolor, move, replace or remove them through the prompt. Boxes guide placement and scale; they do not constrain pixels to a hard mask.
  3. Text rendering within generated images.
  4. Released under the [FLUX Kommunity License](https://huggingface.co/black-forest-labs/flux-3-image-klein/blob/main/LICENSE.md). The license permits non-commercial use and provides a commercial-output exception for Qualifying Users, subject to its terms. See [License](https://huggingface.co/black-forest-labs/flux-3-image-klein#license) below.


##  [ ](https://huggingface.co/black-forest-labs/flux-3-image-klein#download) Download 
Download the root BF16 distilled package, including its text encoder and image autoencoder, without downloading the quantized variants:

```
from huggingface_hub import snapshot_download

snapshot_download(
    repo_id="black-forest-labs/flux-3-image-klein",
    local_dir="weights/flux-3-image-klein",
    allow_patterns=[
        "model.safetensors", "config.json", "manifest.json",
        "ae.safetensors", "text_encoder/*",
        "README.md", "LICENSE.md", "NOTICE.md",
    ],
)

```

To download a quantized distilled transformer instead, replace the three root transformer patterns (`model.safetensors`, `config.json`, and `manifest.json`) with `variants/fp8r/*` or `variants/nvfp4/*`. Keep `ae.safetensors` and `text_encoder/*` for the other components.
These files contain the model package, not a complete inference application. Use an inference implementation that supports flow-map sampling and this checkpoint format. Quantized packages need a loader that supports their format; their file size is not a measure of total GPU memory use.
##  [ ](https://huggingface.co/black-forest-labs/flux-3-image-klein#using-with-reference-code) Using with reference code 
The distilled checkpoint is served on the [BFL API](https://bfl.ai) as FLUX 3 Image Klein. The reference inference code is [black-forest-labs/flux-3-image-klein](https://github.com/black-forest-labs/flux-3-image-klein).
From the reference implementation checkout, install the package and download the two components the CLI loads besides this checkpoint. The CLI reads its weights from `weights/` (set `WEIGHTS_DIR` for another root), where the download above puts this repository.

```
pip install -e .

# safety classifier, always loaded
hf download Falconsai/nsfw_image_detection --local-dir weights/nsfw-classifier
# prompt upsampler (18.8 GB), on by default; --no-pup sends the prompt as typed, for captions written by another LLM
hf download black-forest-labs/flux-3-image-klein-pup --local-dir weights/pup

# text-to-image
python scripts/cli.py 'A chunky knitted diorama: three white cable-knit icebergs with tiny pale blue houses, a cream banner embroidered "KNITTED ICEBERG VILLAGE", a giant magenta knitted whale tail bursting from a yarn sea' \
  --model distilled --out knitted.png

# image editing; repeat --image for multiple references
python scripts/cli.py 'the same scene at night under a knitted full moon, embroidered stars above the peaks' \
  --model distilled --image knitted.png --out knitted_night.png

```

##  [ ](https://huggingface.co/black-forest-labs/flux-3-image-klein#using-with-diffusers) Using with Diffusers 
FLUX 3 Image Klein uses a modular pipeline. Pass `prompt` for text-to-image generation, or pass `image` with a prompt for editing; `image` can be one image or a list of reference images. The model takes full scene captions, not short prompts: a request sent as typed gives generic output. Every request below goes through the [prompt upsampler](https://huggingface.co/black-forest-labs/flux-3-image-klein#prompt-upsampling) first, a separate 9B model ([black-forest-labs/flux-3-image-klein-pup](https://huggingface.co/black-forest-labs/flux-3-image-klein-pup)) that the pipeline does not run on its own. Load it beside the pipeline, then generate:

```
pip install git+https://github.com/huggingface/diffusers.git

```


```
import json

import torch
from diffusers import ModularPipeline
from huggingface_hub import hf_hub_download
from transformers import AutoProcessor, Qwen3_5ForConditionalGeneration

pipe = ModularPipeline.from_pretrained("black-forest-labs/flux-3-image-klein")
pipe.load_components(dtype=torch.bfloat16)
pipe.to("cuda")

pup_id = "black-forest-labs/flux-3-image-klein-pup"
processor = AutoProcessor.from_pretrained(pup_id)
upsampler = Qwen3_5ForConditionalGeneration.from_pretrained(pup_id, dtype=torch.bfloat16, device_map="auto").eval()
system_prompts = json.load(open(hf_hub_download(pup_id, "system_prompts.json")))


def upsample(prompt, images=()):
    if images:
        text = (
            "Reference images follow in order (the first image, the second image, ...).\n"
            f"User request: {prompt}\nOutput the caption."
        )
        content = [{"type": "image", "image": image} for image in images] + [{"type": "text", "text": text}]
        messages = [{"role": "system", "content": system_prompts["i2i"]}, {"role": "user", "content": content}]
    else:
        messages = [{"role": "system", "content": system_prompts["t2i"]}, {"role": "user", "content": prompt}]
    inputs = processor.apply_chat_template(
        messages, add_generation_prompt=True, tokenize=True, return_dict=True, return_tensors="pt", enable_thinking=False
    ).to(upsampler.device)
    with torch.no_grad():
        output = upsampler.generate(**inputs, max_new_tokens=3584, do_sample=False)
    return processor.decode(output[0, inputs["input_ids"].shape[1]:], skip_special_tokens=True).strip()


caption = upsample('A chunky knitted diorama: three white cable-knit icebergs with tiny pale blue houses, a cream banner embroidered "KNITTED ICEBERG VILLAGE", a giant magenta knitted whale tail bursting from a yarn sea')
image = pipe(prompt=caption, generator=torch.Generator().manual_seed(1), output="images")[0]
image.save("knitted.png")

night = pipe(
    prompt=upsample("the same scene at night under a knitted full moon, embroidered stars above the peaks", [image]),
    image=image,
    generator=torch.Generator().manual_seed(1),
    output="images",
)[0]
night.save("knitted_night.png")

```

###  [ ](https://huggingface.co/black-forest-labs/flux-3-image-klein#prompt-upsampling) Prompt upsampling 
The prompt upsampler turns a short request, together with the reference images when editing, into the full scene caption the model takes: medium and style, scene, lighting and camera, each subject with its colors, materials and position in the frame. The reference CLI runs it by default. `upsample` above runs it with Transformers: `system_prompts["t2i"]` for text-to-image, `system_prompts["i2i"]` with the references first in the user message for an edit, greedy decoding, thinking off. Its [model card](https://huggingface.co/black-forest-labs/flux-3-image-klein-pup) has the decoding settings and the layout form (`t2i_bbox`, `i2i_bbox`), which takes a list of boxes and writes the box table after the caption.
Any other LLM can take its place: give it `system_prompts["t2i"]` (or `"i2i"` with the references) as the system prompt, the request as the user message, and pass the caption it returns as `prompt`.
##  [ ](https://huggingface.co/black-forest-labs/flux-3-image-klein#prompting) Prompting 
The caption controls composition; reference images anchor content, they do not lock structure.
  * Always run a [prompt upsampler](https://huggingface.co/black-forest-labs/flux-3-image-klein#prompt-upsampling), ours or your own LLM: the model takes full scene captions (framing, subject, background, lighting), and a short prompt sent as typed gives generic output. A one-line edit instruction ("make it blue") reframes the shot.
  * For edits, the [prompt upsampler](https://huggingface.co/black-forest-labs/flux-3-image-klein#prompt-upsampling) writes the caption from the instruction and the references: a complete caption of the reference with the edit folded in. For style, describe the attributes (palette, stroke, texture) rather than naming an artwork.
  * For layout, append a JSON list of elements to the caption. Each box is `[top, left, bottom, right]` on a 0 to 1000 grid; tag the element in the caption with `<id>`:



```
Minimalist graphic illustration featuring a black silhouette of a person <silhouette_1> centered against a solid, vibrant chartreuse background <background_1>. The figure is captured in a dynamic, mid-stride running pose, facing toward the left side of the frame. [{"id": "background_1", "bbox": [0, 0, 1000, 1000], "desc": "A flat field of neon yellow-green with a subtle paper texture and fine, organic grain."}, {"id": "silhouette_1", "bbox": [150, 150, 850, 850], "desc": "A black silhouette of a person in motion, made of dense stippled ink."}]

```

For edits by box, refer to the n-th reference as `<ref_image_n>` and give each element `from`, `src_bbox` and `tgt_bbox`; a `null` target removes it. The full format with worked examples: [Bounding boxes](https://docs.bfl.ai/flux_3/flux3_image_bounding_boxes).
##  [ ](https://huggingface.co/black-forest-labs/flux-3-image-klein#limitations) Limitations 
  * This model is not intended or able to provide factual information.
  * While the model can output text, text rendered may be inaccurate or subject to distortion.
  * As a statistical model, this checkpoint may represent or amplify biases observed in the training data.
  * The model may fail to generate output that matches the prompts.
  * Prompt following is heavily influenced by the prompting style. Short prompts produce generic output.
  * Boxes set placement and scale, not a hard mask: an element can extend past its box, and small requested elements may not appear. Edits can change content outside the requested region.


##  [ ](https://huggingface.co/black-forest-labs/flux-3-image-klein#hardware) Hardware 
Peak GPU memory with the [reference code](https://github.com/black-forest-labs/flux-3-image-klein), B200, 1024x1024, prompt upsampler off: 31 GB in BF16, 26 GB in FP8, 25 GB in NVFP4. The prompt upsampler adds about 28 GB on an 80 GB GPU.
##  [ ](https://huggingface.co/black-forest-labs/flux-3-image-klein#out-of-scope-use) Out-of-scope use 
See Section 4 of the [FLUX Kommunity License](https://huggingface.co/black-forest-labs/flux-3-image-klein/blob/main/LICENSE.md) for the full restrictions. They include military purposes; surveillance, including related research and development; biometric processing; unlawful, unsafe, fraudulent, defamatory, or abusive activity; generating unlawful content, including child sexual abuse material or non-consensual intimate images; violating third-party rights, including rights of publicity or digital replica rights; and using the model, its Derivatives, or its Outputs to improve another AI model that performs a function similar to a FLUX Model or Derivative.
The license also covers export controls and sanctions. Its commercial-use exception is not blanket permission for commercial fine-tuning or distribution. Consult the full license for the terms that apply to each use.
Nothing contained in this model card should be interpreted as or deemed a restriction or modification to the license the model is released under.
##  [ ](https://huggingface.co/black-forest-labs/flux-3-image-klein#responsible-ai-development) Responsible AI Development 
Black Forest Labs is committed to responsible model development and deployment. Prior to releasing FLUX 3 Image Klein, we evaluated and mitigated a number of risks, including child sexual abuse material (CSAM) and nonconsensual intimate imagery (NCII). For detailed information about our mitigations, evaluation processes, content provenance features, and policies, please see our post: [Capable, Open, and Safe: Combating AI Misuse](https://bfl.ai/blog/capable-open-and-safe-combating-ai-misuse). To report safety concerns, contact safety@blackforestlabs.ai.
##  [ ](https://huggingface.co/black-forest-labs/flux-3-image-klein#license) License 
This model is released under the [FLUX Kommunity License v.1.0](https://huggingface.co/black-forest-labs/flux-3-image-klein/blob/main/LICENSE.md): non-commercial use, plus commercial output generation by Qualifying Users with less than US$5M in gross annualized revenue, including affiliates, subject to the license terms. For other uses, see [commercial licensing](https://bfl.ai/licensing).
The Qwen3-VL-4B-Instruct text encoder is under [Apache-2.0](https://huggingface.co/black-forest-labs/flux-3-image-klein/tree/main/text_encoder/LICENSE).
##  [ ](https://huggingface.co/black-forest-labs/flux-3-image-klein#trademarks-and-ip) Trademarks and IP 
Use of Black Forest Labs and FLUX trademarks requires prior written permission, except for required attribution or necessary descriptive references. Use must not cause confusion or imply sponsorship or endorsement. Third-party trademarks remain subject to their owners' policies.
##  [ ](https://huggingface.co/black-forest-labs/flux-3-image-klein#citation) Citation 
If you use FLUX 3 Image in your work, please cite:

```
@misc{bfl2026flux3image,
  author       = {{Black Forest Labs}},
  title        = {{FLUX} 3 Image Klein},
  year         = {2026},
  url          = {https://bfl.ai/blog/flux-3-image-klein},
}

```


Downloads last month
    123,271
Safetensors[](https://huggingface.co/docs/safetensors)
Model size
6B params
Tensor type
BF16 
·
Files info
Inference Providers [NEW](https://huggingface.co/docs/inference-providers)
[ Image-to-Image ](https://huggingface.co/tasks/image-to-image "Learn more about image-to-image")
This model isn't deployed by any Inference Provider. [🙋 3 Ask for provider support](https://huggingface.co/spaces/huggingface/InferenceSupport/discussions/13022)
##  Model tree for black-forest-labs/flux-3-image-klein [](https://huggingface.co/docs/hub/model-cards#specifying-a-base-model)
Adapters
[9 models](https://huggingface.co/models?other=base_model:adapter:black-forest-labs/flux-3-image-klein)
Finetunes
[12 models](https://huggingface.co/models?other=base_model:finetune:black-forest-labs/flux-3-image-klein)
Merges
[1 model](https://huggingface.co/models?other=base_model:merge:black-forest-labs/flux-3-image-klein)
Quantizations
[34 models](https://huggingface.co/models?other=base_model:quantized:black-forest-labs/flux-3-image-klein)
##  Spaces using black-forest-labs/flux-3-image-klein 40
[ ![](https://cdn-avatars.huggingface.co/v1/production/uploads/633f7a8f4be90e06da248e0f/m5YoF33abJ09vcwFxt1Mj.png) black-forest-labs/flux-3-image-klein ](https://huggingface.co/spaces/black-forest-labs/flux-3-image-klein)[🖼 RioShiina/ImageGen ](https://huggingface.co/spaces/RioShiina/ImageGen)[🎨 amisima/Flux-3-Image ](https://huggingface.co/spaces/amisima/Flux-3-Image)[🖼 Gramlin/ImageGennew ](https://huggingface.co/spaces/Gramlin/ImageGennew)[🎃 Diskfo/flux-3-image-klein ](https://huggingface.co/spaces/Diskfo/flux-3-image-klein)[🎃 prithivMLmods/flux-3-image-klein-loras-fast ](https://huggingface.co/spaces/prithivMLmods/flux-3-image-klein-loras-fast)[📈 BIGJUTT/model-pulse ](https://huggingface.co/spaces/BIGJUTT/model-pulse)[🖼 Or1290/LP12 ](https://huggingface.co/spaces/Or1290/LP12) + 35 Spaces + 32 Spaces
##  Collection including black-forest-labs/flux-3-image-klein
#### [FLUX 3 Image Klein Collection 5 items • Updated 10 days ago • 49 ](https://huggingface.co/collections/black-forest-labs/flux-3-image-klein)
System theme
Company
[TOS](https://huggingface.co/terms-of-service) [Privacy](https://huggingface.co/privacy) [About](https://huggingface.co/huggingface) [Careers](https://apply.workable.com/huggingface/) [](https://huggingface.co/)
Website
[Models](https://huggingface.co/models) [Datasets](https://huggingface.co/datasets) [Spaces](https://huggingface.co/spaces) [Pricing](https://huggingface.co/pricing) [Docs](https://huggingface.co/docs)
You have to accept the conditions to access the files info
Inference providers allow you to run inference using different serverless providers.

