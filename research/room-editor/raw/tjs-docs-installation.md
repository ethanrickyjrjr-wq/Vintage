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
Installation
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
You are viewing main version, which requires installation from source. If you'd like regular npm install, checkout the latest stable version ([v3.8.1](https://huggingface.co/docs/transformers.js/v3.8.1/installation)).
![Hugging Face's logo](https://huggingface.co/front/assets/huggingface_logo-noborder.svg)
Join the Hugging Face community
and get access to the augmented documentation experience
Collaborate on models, datasets and Spaces
Faster examples with accelerated inference
Switch between documentation themes
[Sign Up](https://huggingface.co/join)
to get started
Copy page
#  [](https://huggingface.co/docs/transformers.js/installation#installation) Installation
To install via [NPM](https://www.npmjs.com/package/@huggingface/transformers), run:
Copied

```
npm i @huggingface/transformers
```

Alternatively, you can use it in vanilla JS, without any bundler, by using a CDN or static hosting. For example, using [ES Modules](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules), you can import the library with:
Copied

```
<script type="module">
    import { pipeline } from 'https://cdn.jsdelivr.net/npm/@huggingface/transformers@4.3.2';
</script>
```

[ Update on GitHub](https://github.com/huggingface/transformers.js/blob/main/packages/transformers/docs/source/installation.md)
[←🤗 Transformers.js](https://huggingface.co/docs/transformers.js/index) [The pipeline API→](https://huggingface.co/docs/transformers.js/pipelines)
[Installation](https://huggingface.co/docs/transformers.js/installation#installation)

