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
[ ![](https://cdn-avatars.huggingface.co/v1/production/uploads/61b253b7ac5ecaae3d1efe0c/BpiYJ-m5mXPXfjkzEt6yZ.png) ](https://huggingface.co/onnx-community)
[onnx-community](https://huggingface.co/onnx-community)
/
[Florence-2-base-ft](https://huggingface.co/onnx-community/Florence-2-base-ft)
Like 44
Follow
![](https://cdn-avatars.huggingface.co/v1/production/uploads/61b253b7ac5ecaae3d1efe0c/BpiYJ-m5mXPXfjkzEt6yZ.png) ONNX Community 2.29k
[ Image-Text-to-Text ](https://huggingface.co/models?pipeline_tag=image-text-to-text)[ Transformers.js ](https://huggingface.co/models?library=transformers.js)[ ONNX ](https://huggingface.co/models?library=onnx)[ florence2 ](https://huggingface.co/models?other=florence2)[ vision ](https://huggingface.co/models?other=vision)[ text-generation ](https://huggingface.co/models?other=text-generation)[ text2text-generation ](https://huggingface.co/models?other=text2text-generation)[ image-to-text ](https://huggingface.co/models?other=image-to-text)
License: mit
[ Model card ](https://huggingface.co/onnx-community/Florence-2-base-ft)[ Files Files and versions xet ](https://huggingface.co/onnx-community/Florence-2-base-ft/tree/main)[ Community 11 ](https://huggingface.co/onnx-community/Florence-2-base-ft/discussions)
Deploy
Copy to bucket
Use this model
### Instructions to use onnx-community/Florence-2-base-ft with libraries, inference providers, notebooks, and local apps. Follow these links to get started.
  * Libraries
  * [ Transformers.js](https://huggingface.co/onnx-community/Florence-2-base-ft?library=transformers.js)
How to use onnx-community/Florence-2-base-ft with Transformers.js:

```
// npm i @huggingface/transformers
import { pipeline } from '@huggingface/transformers';

// Allocate pipeline
const pipe = await pipeline('image-text-to-text', 'onnx-community/Florence-2-base-ft');
```



  * [Usage (Transformers.js)](https://huggingface.co/onnx-community/Florence-2-base-ft#usage-transformersjs "Usage \(Transformers.js\)")


<https://huggingface.co/microsoft/Florence-2-base-ft> with ONNX weights to be compatible with Transformers.js.
##  [ ](https://huggingface.co/onnx-community/Florence-2-base-ft#usage-transformersjs) Usage (Transformers.js) 
If you haven't already, you can install the [Transformers.js](https://huggingface.co/docs/transformers.js) JavaScript library from [NPM](https://www.npmjs.com/package/@huggingface/transformers) using:

```
npm i @huggingface/transformers

```

**Example:** Perform image captioning with `onnx-community/Florence-2-base-ft`.

```
import {
    Florence2ForConditionalGeneration,
    AutoProcessor,
    load_image,
} from '@huggingface/transformers';

// Load model, processor, and tokenizer
const model_id = 'onnx-community/Florence-2-base-ft';
const model = await Florence2ForConditionalGeneration.from_pretrained(model_id, { dtype: 'fp32' });
const processor = await AutoProcessor.from_pretrained(model_id);

// Load image and prepare vision inputs
const url = 'https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/tasks/car.jpg';
const image = await load_image(url);

// Specify task and prepare text inputs
const task = '<MORE_DETAILED_CAPTION>';
const prompts = processor.construct_prompts(task);

// Pre-process the image and text inputs
const inputs = await processor(image, prompts);

// Generate text
const generated_ids = await model.generate({
    ...inputs,
    max_new_tokens: 100,
});

// Decode generated text
const generated_text = processor.batch_decode(generated_ids, { skip_special_tokens: false })[0];

// Post-process the generated text
const result = processor.post_process_generation(generated_text, task, image.size);
console.log(result);
// { '<MORE_DETAILED_CAPTION>': 'A green car is parked in front of a tan building. There is a brown door on the building behind the car. There are two windows on the front of the building. ' }

```

We also released an online demo, which you can try yourself: <https://huggingface.co/spaces/Xenova/florence2-webgpu>
* * *
Note: Having a separate repo for ONNX weights is intended to be a temporary solution until WebML gains more traction. If you would like to make your models web-ready, we recommend converting to ONNX using [🤗 Optimum](https://huggingface.co/docs/optimum/index) and structuring your repo like this one (with ONNX weights located in a subfolder named `onnx`). 

Downloads last month
    30,699
Inference Providers [NEW](https://huggingface.co/docs/inference-providers)
[ Image-Text-to-Text ](https://huggingface.co/tasks/image-text-to-text "Learn more about image-text-to-text")
This model isn't deployed by any Inference Provider. [🙋 Ask for provider support](https://huggingface.co/spaces/huggingface/InferenceSupport/discussions/new?title=onnx-community/Florence-2-base-ft&description=React%20to%20this%20comment%20with%20an%20emoji%20to%20vote%20for%20%5Bonnx-community%2FFlorence-2-base-ft%5D\(%2Fonnx-community%2FFlorence-2-base-ft\)%20to%20be%20supported%20by%20Inference%20Providers.%0A%0A\(optional\)%20Which%20providers%20are%20you%20interested%20in%3F%20\(Novita%2C%20Hyperbolic%2C%20Together%E2%80%A6\)%0A)
##  Model tree for onnx-community/Florence-2-base-ft [](https://huggingface.co/docs/hub/model-cards#specifying-a-base-model)
Base model
[microsoft/Florence-2-base-ft](https://huggingface.co/microsoft/Florence-2-base-ft)
Quantized
([9](https://huggingface.co/models?other=base_model:quantized:microsoft/Florence-2-base-ft))
this model
##  Spaces using onnx-community/Florence-2-base-ft 8
[🖼️ Xenova/florence2-webgpu ](https://huggingface.co/spaces/Xenova/florence2-webgpu)[🌐 dwb2023/transformers-js-demos ](https://huggingface.co/spaces/dwb2023/transformers-js-demos)[🖼️ itembox/florence2-webgpu ](https://huggingface.co/spaces/itembox/florence2-webgpu)[🦀 Rtop0726/Images ](https://huggingface.co/spaces/Rtop0726/Images)[👁 dav729/image-caption ](https://huggingface.co/spaces/dav729/image-caption)[🏃 milormik/image-ia ](https://huggingface.co/spaces/milormik/image-ia)[🖼️ jaimenms/image2vienna ](https://huggingface.co/spaces/jaimenms/image2vienna)[🖼️ Yunpeng-26/ai-powered-image-captioning ](https://huggingface.co/spaces/Yunpeng-26/ai-powered-image-captioning) + 3 Spaces
System theme
Company
[TOS](https://huggingface.co/terms-of-service) [Privacy](https://huggingface.co/privacy) [About](https://huggingface.co/huggingface) [Careers](https://apply.workable.com/huggingface/) [](https://huggingface.co/)
Website
[Models](https://huggingface.co/models) [Datasets](https://huggingface.co/datasets) [Spaces](https://huggingface.co/spaces) [Pricing](https://huggingface.co/pricing) [Docs](https://huggingface.co/docs)
Inference providers allow you to run inference using different serverless providers.

