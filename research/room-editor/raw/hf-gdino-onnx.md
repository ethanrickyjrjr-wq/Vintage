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
[grounding-dino-tiny-ONNX](https://huggingface.co/onnx-community/grounding-dino-tiny-ONNX)
Like 7
Follow
![](https://cdn-avatars.huggingface.co/v1/production/uploads/61b253b7ac5ecaae3d1efe0c/BpiYJ-m5mXPXfjkzEt6yZ.png) ONNX Community 2.29k
[ Zero-Shot Object Detection ](https://huggingface.co/models?pipeline_tag=zero-shot-object-detection)[ Transformers.js ](https://huggingface.co/models?library=transformers.js)[ ONNX ](https://huggingface.co/models?library=onnx)[ grounding-dino ](https://huggingface.co/models?other=grounding-dino)
License: apache-2.0
[ Model card ](https://huggingface.co/onnx-community/grounding-dino-tiny-ONNX)[ Files Files and versions xet ](https://huggingface.co/onnx-community/grounding-dino-tiny-ONNX/tree/main)[ Community 4 ](https://huggingface.co/onnx-community/grounding-dino-tiny-ONNX/discussions)
Deploy
Copy to bucket
Use this model
### Instructions to use onnx-community/grounding-dino-tiny-ONNX with libraries, inference providers, notebooks, and local apps. Follow these links to get started.
  * Libraries
  * [ Transformers.js](https://huggingface.co/onnx-community/grounding-dino-tiny-ONNX?library=transformers.js)
How to use onnx-community/grounding-dino-tiny-ONNX with Transformers.js:

```
// npm i @huggingface/transformers
import { pipeline } from '@huggingface/transformers';

// Allocate pipeline
const pipe = await pipeline('zero-shot-object-detection', 'onnx-community/grounding-dino-tiny-ONNX');
```



  * [Usage (Transformers.js)](https://huggingface.co/onnx-community/grounding-dino-tiny-ONNX#usage-transformersjs "Usage \(Transformers.js\)")


<https://huggingface.co/IDEA-Research/grounding-dino-tiny> with ONNX weights to be compatible with Transformers.js.
##  [ ](https://huggingface.co/onnx-community/grounding-dino-tiny-ONNX#usage-transformersjs) Usage (Transformers.js) 
If you haven't already, you can install the [Transformers.js](https://huggingface.co/docs/transformers.js) JavaScript library from [NPM](https://www.npmjs.com/package/@huggingface/transformers) using:

```
npm i @huggingface/transformers

```

**Example:** Zero-shot object detection with `onnx-community/grounding-dino-tiny-ONNX` using the `pipeline` API.

```
import { pipeline } from "@huggingface/transformers";

const detector = await pipeline("zero-shot-object-detection", "onnx-community/grounding-dino-tiny-ONNX");

const url = "http://images.cocodataset.org/val2017/000000039769.jpg";
const candidate_labels = ["a cat."];
const output = await detector(url, candidate_labels, {
  threshold: 0.3,
});

```

See example output

```
[
  { score: 0.45316222310066223, label: "a cat", box: { xmin: 343, ymin: 23, xmax: 637, ymax: 372 } },
  { score: 0.36190420389175415, label: "a cat", box: { xmin: 12, ymin: 52, xmax: 317, ymax: 472 } },
]

```

**Example:** Zero-shot object detection with `onnx-community/grounding-dino-tiny-ONNX` using the `AutoModel` API.

```
import { AutoModelForZeroShotObjectDetection, AutoProcessor, load_image } from "@huggingface/transformers";

// Load model and processor
const model_id = "onnx-community/grounding-dino-tiny-ONNX";
const processor = await AutoProcessor.from_pretrained(model_id);
const model = await AutoModelForZeroShotObjectDetection.from_pretrained(model_id, { dtype: "fp32" });

// Prepare image and text inputs
const image = await load_image("http://images.cocodataset.org/val2017/000000039769.jpg");
const text = "a cat."; // NB: text query needs to be lowercased + end with a dot

// Preprocess image and text
const inputs = await processor(image, text);

// Run model
const outputs = await model(inputs);

// Post-process outputs
const results = processor.post_process_grounded_object_detection(
  outputs,
  inputs.input_ids,
  {
    box_threshold: 0.3,
    text_threshold: 0.3,
    target_sizes: [image.size.reverse()],
  },
);
console.log(results);

```

See example output

```
[
  {
    scores: [ 0.45316222310066223, 0.36190420389175415 ],
    boxes: [
      [ 343.7238121032715, 23.02229404449463, 637.0737648010254, 372.6510000228882 ],
      [ 12.311229705810547, 52.27128982543945, 317.4389839172363, 472.60459899902344 ]
    ],
    labels: [ 'a cat', 'a cat' ]
  }
]

```

* * * 

Downloads last month
    3,918
Inference Providers [NEW](https://huggingface.co/docs/inference-providers)
[ Zero-Shot Object Detection ](https://huggingface.co/tasks/zero-shot-object-detection "Learn more about zero-shot-object-detection")
This model isn't deployed by any Inference Provider. [🙋 Ask for provider support](https://huggingface.co/spaces/huggingface/InferenceSupport/discussions/new?title=onnx-community/grounding-dino-tiny-ONNX&description=React%20to%20this%20comment%20with%20an%20emoji%20to%20vote%20for%20%5Bonnx-community%2Fgrounding-dino-tiny-ONNX%5D\(%2Fonnx-community%2Fgrounding-dino-tiny-ONNX\)%20to%20be%20supported%20by%20Inference%20Providers.%0A%0A\(optional\)%20Which%20providers%20are%20you%20interested%20in%3F%20\(Novita%2C%20Hyperbolic%2C%20Together%E2%80%A6\)%0A)
System theme
Company
[TOS](https://huggingface.co/terms-of-service) [Privacy](https://huggingface.co/privacy) [About](https://huggingface.co/huggingface) [Careers](https://apply.workable.com/huggingface/) [](https://huggingface.co/)
Website
[Models](https://huggingface.co/models) [Datasets](https://huggingface.co/datasets) [Spaces](https://huggingface.co/spaces) [Pricing](https://huggingface.co/pricing) [Docs](https://huggingface.co/docs)
Inference providers allow you to run inference using different serverless providers.

