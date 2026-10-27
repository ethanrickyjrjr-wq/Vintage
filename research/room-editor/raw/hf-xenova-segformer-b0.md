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
[ ![](https://cdn-avatars.huggingface.co/v1/production/uploads/61b253b7ac5ecaae3d1efe0c/hwiQ0uvz3t-L5a-NtBIO6.png) ](https://huggingface.co/Xenova)
[Xenova](https://huggingface.co/Xenova)
/
[segformer-b0-finetuned-ade-512-512](https://huggingface.co/Xenova/segformer-b0-finetuned-ade-512-512)
Like 3
[ Image Segmentation ](https://huggingface.co/models?pipeline_tag=image-segmentation)[ Transformers.js ](https://huggingface.co/models?library=transformers.js)[ ONNX ](https://huggingface.co/models?library=onnx)[ segformer ](https://huggingface.co/models?other=segformer)
[ Model card ](https://huggingface.co/Xenova/segformer-b0-finetuned-ade-512-512)[ Files Files and versions xet ](https://huggingface.co/Xenova/segformer-b0-finetuned-ade-512-512/tree/main)[ Community 1 ](https://huggingface.co/Xenova/segformer-b0-finetuned-ade-512-512/discussions)
Deploy
Copy to bucket
Use this model
### Instructions to use Xenova/segformer-b0-finetuned-ade-512-512 with libraries, inference providers, notebooks, and local apps. Follow these links to get started.
  * Libraries
  * [ Transformers.js](https://huggingface.co/Xenova/segformer-b0-finetuned-ade-512-512?library=transformers.js)
How to use Xenova/segformer-b0-finetuned-ade-512-512 with Transformers.js:

```
// npm i @huggingface/transformers
import { pipeline } from '@huggingface/transformers';

// Allocate pipeline
const pipe = await pipeline('image-segmentation', 'Xenova/segformer-b0-finetuned-ade-512-512');
```



  * [Usage (Transformers.js)](https://huggingface.co/Xenova/segformer-b0-finetuned-ade-512-512#usage-transformersjs "Usage \(Transformers.js\)")


<https://huggingface.co/nvidia/segformer-b0-finetuned-ade-512-512> with ONNX weights to be compatible with Transformers.js.
##  [ ](https://huggingface.co/Xenova/segformer-b0-finetuned-ade-512-512#usage-transformersjs) Usage (Transformers.js) 
If you haven't already, you can install the [Transformers.js](https://huggingface.co/docs/transformers.js) JavaScript library from [NPM](https://www.npmjs.com/package/@huggingface/transformers) using:

```
npm i @huggingface/transformers

```

**Example:** Image segmentation with `Xenova/segformer-b0-finetuned-ade-512-512`.

```
import { pipeline } from '@huggingface/transformers';

// Create an image segmentation pipeline
const segmenter = await pipeline('image-segmentation', 'Xenova/segformer-b0-finetuned-ade-512-512');

// Segment an image
const url = 'https://huggingface.co/datasets/Xenova/transformers.js-docs/resolve/main/house.jpg';
const output = await segmenter(url);
console.log(output)
// [
//   {
//     score: null,
//     label: 'wall',
//     mask: RawImage { ... }
//   },
//   {
//     score: null,
//     label: 'building',
//     mask: RawImage { ... }
//   },
//   ...
// ]

```

You can visualize the outputs with:

```
for (const l of output) {
  l.mask.save(`${l.label}.png`);
}

```

* * *
Note: Having a separate repo for ONNX weights is intended to be a temporary solution until WebML gains more traction. If you would like to make your models web-ready, we recommend converting to ONNX using [🤗 Optimum](https://huggingface.co/docs/optimum/index) and structuring your repo like this one (with ONNX weights located in a subfolder named `onnx`). 

Downloads last month
    176,407
Inference Providers [NEW](https://huggingface.co/docs/inference-providers)
[ Image Segmentation ](https://huggingface.co/tasks/image-segmentation "Learn more about image-segmentation")
This model isn't deployed by any Inference Provider. [🙋 Ask for provider support](https://huggingface.co/spaces/huggingface/InferenceSupport/discussions/new?title=Xenova/segformer-b0-finetuned-ade-512-512&description=React%20to%20this%20comment%20with%20an%20emoji%20to%20vote%20for%20%5BXenova%2Fsegformer-b0-finetuned-ade-512-512%5D\(%2FXenova%2Fsegformer-b0-finetuned-ade-512-512\)%20to%20be%20supported%20by%20Inference%20Providers.%0A%0A\(optional\)%20Which%20providers%20are%20you%20interested%20in%3F%20\(Novita%2C%20Hyperbolic%2C%20Together%E2%80%A6\)%0A)
##  Model tree for Xenova/segformer-b0-finetuned-ade-512-512 [](https://huggingface.co/docs/hub/model-cards#specifying-a-base-model)
Base model
[nvidia/segformer-b0-finetuned-ade-512-512](https://huggingface.co/nvidia/segformer-b0-finetuned-ade-512-512)
Quantized
([2](https://huggingface.co/models?other=base_model:quantized:nvidia/segformer-b0-finetuned-ade-512-512))
this model
##  Spaces using Xenova/segformer-b0-finetuned-ade-512-512 5
[🐢 Dazny/alo-sabagh-ai ](https://huggingface.co/spaces/Dazny/alo-sabagh-ai)[👀 homeglazer/homeglazer-room-ai ](https://huggingface.co/spaces/homeglazer/homeglazer-room-ai)[🎨 htgudi/painting-3d-deepdive ](https://huggingface.co/spaces/htgudi/painting-3d-deepdive)[🖼️ Jacobzz11/robust-image-segmentation ](https://huggingface.co/spaces/Jacobzz11/robust-image-segmentation)[🛰️ liu-rs-vision/RS-CV-Demo ](https://huggingface.co/spaces/liu-rs-vision/RS-CV-Demo)
System theme
Company
[TOS](https://huggingface.co/terms-of-service) [Privacy](https://huggingface.co/privacy) [About](https://huggingface.co/huggingface) [Careers](https://apply.workable.com/huggingface/) [](https://huggingface.co/)
Website
[Models](https://huggingface.co/models) [Datasets](https://huggingface.co/datasets) [Spaces](https://huggingface.co/spaces) [Pricing](https://huggingface.co/pricing) [Docs](https://huggingface.co/docs)
Inference providers allow you to run inference using different serverless providers.

