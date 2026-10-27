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


Transformers.js documentation
Using quantized models (dtypes)
# Transformers.js
🏡 View all docs AWS Trainium & Inferentia Accelerate Argilla AutoTrain Bitsandbytes CLI Chat UI Dataset viewer Datasets Deploying on AWS Diffusers Distilabel Evaluate Google Cloud Google TPUs Gradio Hub Hub Python Library Huggingface.js Inference Endpoints (dedicated) Inference Providers Kernels LeRobot Leaderboards Lighteval Microsoft Azure OpenEnv Optimum PEFT Reachy Mini Safetensors Sentence Transformers TRL Tasks Text Embeddings Inference Text Generation Inference Tokenizers Trackio Transformers Transformers.js Xet smolagents timm
Search documentation
`Ctrl+K`
main v3.8.1 v3.0.0 v2.17.2 EN
[ ](https://github.com/huggingface/transformers.js)
[🤗 Transformers.js](https://huggingface.co/docs/transformers.js/index)
Get started
[Installation](https://huggingface.co/docs/transformers.js/installation)[The pipeline API](https://huggingface.co/docs/transformers.js/pipelines)[Custom usage](https://huggingface.co/docs/transformers.js/custom_usage)
Tutorials
[Building a Vanilla JS Application](https://huggingface.co/docs/transformers.js/tutorials/vanilla-js)[Building a React Application](https://huggingface.co/docs/transformers.js/tutorials/react)[Building a Next.js Application](https://huggingface.co/docs/transformers.js/tutorials/next)[Building a Browser Extension](https://huggingface.co/docs/transformers.js/tutorials/browser-extension)[Building an Electron Application](https://huggingface.co/docs/transformers.js/tutorials/electron)[Server-side Inference in Node.js](https://huggingface.co/docs/transformers.js/tutorials/node)[Building a Next.js AI Chatbot with Vercel AI SDK](https://huggingface.co/docs/transformers.js/tutorials/next-ai-sdk)
Developer Guides
[Running models on WebGPU](https://huggingface.co/docs/transformers.js/guides/webgpu)[Using quantized models (dtypes)](https://huggingface.co/docs/transformers.js/guides/dtypes)[Accessing Private/Gated Models](https://huggingface.co/docs/transformers.js/guides/private)[Server-side Audio Processing](https://huggingface.co/docs/transformers.js/guides/node-audio-processing)
Integrations
[Vercel AI SDK](https://huggingface.co/docs/transformers.js/integrations/vercel-ai-sdk)
API Reference
[Index](https://huggingface.co/docs/transformers.js/api/transformers)[Pipelines](https://huggingface.co/docs/transformers.js/api/pipelines)[Models](https://huggingface.co/docs/transformers.js/api/models)[Tokenizers](https://huggingface.co/docs/transformers.js/api/tokenizers)[Processors](https://huggingface.co/docs/transformers.js/api/processors)[Configs](https://huggingface.co/docs/transformers.js/api/configs)[Environment variables](https://huggingface.co/docs/transformers.js/api/env)
Backends
Generation
Utilities
You are viewing main version, which requires installation from source. If you'd like regular npm install, checkout the latest stable version ([v3.8.1](https://huggingface.co/docs/transformers.js/v3.8.1/guides/dtypes)).
![Hugging Face's logo](https://huggingface.co/front/assets/huggingface_logo-noborder.svg)
Join the Hugging Face community
and get access to the augmented documentation experience
Collaborate on models, datasets and Spaces
Faster examples with accelerated inference
Switch between documentation themes
[Sign Up](https://huggingface.co/join)
to get started
Copy page
#  [](https://huggingface.co/docs/transformers.js/guides/dtypes#using-quantized-models-dtypes) Using quantized models (dtypes)
Before Transformers.js v3, we used the `quantized` option to specify whether to use a quantized (q8) or full-precision (fp32) variant of the model by setting `quantized` to `true` or `false`, respectively. Now, we’ve added the ability to select from a much larger list with the `dtype` parameter.
The list of available quantizations depends on the model, but some common ones are: full-precision (`"fp32"`), half-precision (`"fp16"`), 8-bit (`"q8"`, `"int8"`, `"uint8"`), and 4-bit (`"q4"`, `"bnb4"`, `"q4f16"`).
![Available dtypes for mixedbread-ai/mxbai-embed-xsmall-v1](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/transformersjs-v3/dtypes-dark.jpg) [(e.g., mixedbread-ai/mxbai-embed-xsmall-v1)](https://huggingface.co/mixedbread-ai/mxbai-embed-xsmall-v1/tree/main/onnx)
##  [](https://huggingface.co/docs/transformers.js/guides/dtypes#basic-usage) Basic usage
**Example:** Run Qwen2.5-0.5B-Instruct in 4-bit quantization
Copied

```
import { pipeline } from "@huggingface/transformers";

// Create a text generation pipeline
const generator = await pipeline(
  "text-generation",
  "onnx-community/Qwen2.5-0.5B-Instruct",
  { dtype: "q4", device: "webgpu" },
);

// Define the list of messages
const messages = [
  { role: "system", content: "You are a helpful assistant." },
  { role: "user", content: "Tell me a funny joke." },
];

// Generate a response
const output = await generator(messages, { max_new_tokens: 128 });
console.log(output[0].generated_text.at(-1).content);
```

##  [](https://huggingface.co/docs/transformers.js/guides/dtypes#detecting-available-dtypes) Detecting available dtypes
Not sure which quantizations a model offers? Use `ModelRegistry.get_available_dtypes()` to probe the repository and find out:
Copied

```
import { ModelRegistry } from "@huggingface/transformers";

const dtypes = await ModelRegistry.get_available_dtypes(
  "onnx-community/all-MiniLM-L6-v2-ONNX",
);
console.log(dtypes); // e.g., [ 'fp32', 'fp16', 'int8', 'uint8', 'q8', 'q4' ]
```

This checks which ONNX files exist on the Hugging Face Hub for each dtype. For multi-session models (e.g., encoder-decoder), a dtype is only listed if **all** required session files are present.
You can use this to build UIs that let users pick a quantization level, or to automatically select the smallest available dtype:
Copied

```
const dtypes = await ModelRegistry.get_available_dtypes(
  "onnx-community/Qwen3-0.6B-ONNX",
);

// Pick the smallest available quantization, falling back to fp32
const preferred = ["q4", "q8", "fp16", "fp32"];
const dtype = preferred.find((d) => dtypes.includes(d)) ?? "fp32";

const generator = await pipeline(
  "text-generation",
  "onnx-community/Qwen3-0.6B-ONNX",
  { dtype },
);
```

##  [](https://huggingface.co/docs/transformers.js/guides/dtypes#per-module-dtypes) Per-module dtypes
Some encoder-decoder models, like Whisper or Florence-2, are extremely sensitive to quantization settings: especially of the encoder. For this reason, we added the ability to select per-module dtypes, which can be done by providing a mapping from module name to dtype.
**Example:** Run Florence-2 on WebGPU
Copied

```
import { Florence2ForConditionalGeneration } from "@huggingface/transformers";

const model = await Florence2ForConditionalGeneration.from_pretrained(
  "onnx-community/Florence-2-base-ft",
  {
    dtype: {
      embed_tokens: "fp16",
      vision_encoder: "fp16",
      encoder_model: "q4",
      decoder_model_merged: "q4",
    },
    device: "webgpu",
  },
);
```

![Florence-2 running on WebGPU](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/transformersjs-v3/florence-2-webgpu.gif)
See full code example
Copied

```
import {
  Florence2ForConditionalGeneration,
  AutoProcessor,
  AutoTokenizer,
  RawImage,
} from "@huggingface/transformers";

// Load model, processor, and tokenizer
const model_id = "onnx-community/Florence-2-base-ft";
const model = await Florence2ForConditionalGeneration.from_pretrained(
  model_id,
  {
    dtype: {
      embed_tokens: "fp16",
      vision_encoder: "fp16",
      encoder_model: "q4",
      decoder_model_merged: "q4",
    },
    device: "webgpu",
  },
);
const processor = await AutoProcessor.from_pretrained(model_id);
const tokenizer = await AutoTokenizer.from_pretrained(model_id);

// Load image and prepare vision inputs
const url =
  "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/tasks/car.jpg";
const image = await RawImage.fromURL(url);
const vision_inputs = await processor(image);

// Specify task and prepare text inputs
const task = "<MORE_DETAILED_CAPTION>";
const prompts = processor.construct_prompts(task);
const text_inputs = tokenizer(prompts);

// Generate text
const generated_ids = await model.generate({
  ...text_inputs,
  ...vision_inputs,
  max_new_tokens: 100,
});

// Decode generated text
const generated_text = tokenizer.batch_decode(generated_ids, {
  skip_special_tokens: false,
})[0];

// Post-process the generated text
const result = processor.post_process_generation(
  generated_text,
  task,
  image.size,
);
console.log(result);
// { '<MORE_DETAILED_CAPTION>': 'A green car is parked in front of a tan building. The building has a brown door and two brown windows. The car is a two door and the door is closed. The green car has black tires.' }
```

[ Update on GitHub](https://github.com/huggingface/transformers.js/blob/main/packages/transformers/docs/source/guides/dtypes.md)
[←Running models on WebGPU](https://huggingface.co/docs/transformers.js/guides/webgpu) [Accessing Private/Gated Models→](https://huggingface.co/docs/transformers.js/guides/private)
[Using quantized models (dtypes)](https://huggingface.co/docs/transformers.js/guides/dtypes#using-quantized-models-dtypes)[Basic usage](https://huggingface.co/docs/transformers.js/guides/dtypes#basic-usage)[Detecting available dtypes](https://huggingface.co/docs/transformers.js/guides/dtypes#detecting-available-dtypes)[Per-module dtypes](https://huggingface.co/docs/transformers.js/guides/dtypes#per-module-dtypes)

