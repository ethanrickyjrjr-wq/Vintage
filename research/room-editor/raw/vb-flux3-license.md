[The Independent  
Voice on AI](https://venturebeat.com/)
  * [Orchestration](https://venturebeat.com/category/orchestration)
  * [Infrastructure](https://venturebeat.com/category/infrastructure)
  * [Data](https://venturebeat.com/category/data)
  * [Security](https://venturebeat.com/category/security)
  * [Technology](https://venturebeat.com/category/technology)
More


[Newsletters](https://venturebeat.com/newsletters)
# Black Forest Labs opens FLUX 3 Image Klein weights, with free commercial use limited to smaller businesses
[Carl Franzen](https://venturebeat.com/author/carlfranzen)
8:50 am, PT, October 15, 2026 
![Robot holding Klein bottle](https://venturebeat.com/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fjdtwqhzvc2n1%2F1f3tY0rpH62SuCyKqdYuzi%2Fe09f099f2d602f2b771df72641bb4d7c%2Fminimalist-retromodern-2474973291.jpg%3Fw%3D1000%26q%3D100&w=3840&q=85)
Credit: VentureBeat made with Flux 3 Klein on Github 
German AI video and image company Black Forest Labs is today releasing open weights for [FLUX 3 Image Klein](https://bfl.ai/blog/flux-3-image-klein), a 5.6-billion-parameter image model designed to let developers generate, edit and customize visuals on their own hardware.
The company says Klein retains capabilities from its larger [FLUX 3 Image model announced back in July](https://venturebeat.com/technology/black-forest-labs-launches-flux-3-capable-of-generating-images-and-20-second-video-with-audio-but-in-limited-release-to-start), including:
  * Native 4K output
  * Spatial controls and editing driven by reference images
  * Runs on consumer GPUs and laptops with as little as 8 GB of video memory


The release includes a base version for adaptation, a faster distilled version and FP8, NVFP4 and INT8 versions intended to reduce deployment requirements.
For enterprise buyers, the most consequential detail is the license. Black Forest Labs permits** _free commercial use_** for individuals and businesses whose**annual revenue falls below $5 million.**
Larger organizations need a separate arrangement for commercial self-hosting or can use the company's API, with Klein starting at USD $0.009 for a 1K-resolution image.
That makes Klein an additional option for local AI imagery, but the ability to download its weights does not give every business unrestricted commercial rights.
## **A smaller model for private, customizable image workflows**
Klein supports generation from written instructions, changes to existing images and creation guided by multiple reference images. Black Forest Labs says the model also supports bounding boxes, letting developers specify where an element should appear.
The company positions the base checkpoint as a starting point for fine-tuning. The distilled checkpoint takes fewer generation steps and is aimed at lower latency. The compressed versions use reduced numerical precision to lower memory demands.
Black Forest Labs lists support for ComfyUI, Hugging Face Diffusers, Ostris's AI Toolkit, vLLM-Omni and SGLang Diffusion. It also says developers can fine-tune the model using Nvidia NeMo AutoModel. The company says it trained Klein on Nvidia GB200 GPUs in an NVL72 system and optimized it for Nvidia's accelerated computing platform.
BFL now specifies an 8 GB minimum for local use on GeForce RTX hardware. It has not tied that minimum to a particular model variant, output size or generation time, and the supplied speed charts do not test an 8 GB configuration or 4K output. Buyers can size supported hardware more concretely, but still need those details to estimate performance at the minimum specification.
The practical attraction is control. A company can adapt a model to its own examples and operate it within its infrastructure instead of routing each image request through a hosted service. Potential applications include product photography, repeatable brand assets and internal design tools. Those are use cases for evaluating Klein, rather than reported customer deployments in the launch materials.
The hosted distilled version also includes Black Forest Labs' prompt-processing and targeted-editing pipeline. Consequently, an API benchmark does not by itself establish what an unmodified checkpoint will deliver locally.
## **The commercial license is the dividing line**
The release uses the FLUX Kommunity License. Black Forest Labs says businesses below the $5 million revenue threshold can use Klein commercially without a licensing payment; larger organizations can arrange self-hosted rights or buy API access.
The company's [published Kommunity license for FLUX 3 Action](https://huggingface.co/black-forest-labs/flux-3-action-droid/blob/main/LICENSE.md) defines eligibility using gross annualized revenue combined with affiliates. The same published license also imposes conditions on output review or filtering and on redistribution. That existing text provides context for the license family; the terms accompanying Klein's actual download remain the controlling document for this release.
The distinction matters for a large company's small subsidiary or an experimental team. The budget of an individual project does not determine eligibility under that existing revenue definition.
The company's subsequent [API documentation](https://docs.bfl.ai/quick_start/pricing) lists prices of $0.008 at 768 × 768 pixel resolution, $0.009 at 1K, $0.011 at 1.5K, $0.014 at 2K and $0.036 at 4K. 
Generation and editing carry the same per-image price at each resolution. BFL has not published a standard commercial self-hosting fee. 
An earlier briefing described API pricing as roughly one-quarter of a leading open-weight competitor's price, but did not name the comparator or specify matching output settings.
Free commercial permission also does not eliminate compute, storage, adaptation or maintenance expenses. The business calculation differs between a team using idle local hardware and one building a service with sustained demand.
## **What its benchmark charts show — and what they leave open**
Black Forest Labs says its internal evaluations place Klein ahead of other leading models with downloadable weights for generation, reference-based creation and editing.
The charts provided to VentureBeat compare Klein and its base version with Qwen-Image 2.1, Ideogram 4.5, FLUX.2 [pro], FLUX.2 [klein] 9B and Krea 2. They plot preference ratings against model size and, separately, API latency for one-megapixel output.
In the updated API latency chart, Klein receives higher preference ratings than the displayed alternatives in both text-to-image generation and editing. For one-megapixel output, BFL plots the distilled version at roughly five seconds for generation and seven seconds for editing, versus roughly 11 and 22 seconds for the base checkpoint. These are points read from the company's chart, not independently reproduced measurements.
BFL has also supplied local speed measurements with the hardware, precision and number of sampling steps identified. 
![Flux 3 Klein generation speed graph](https://venturebeat.com/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fjdtwqhzvc2n1%2F2Aid3TDtiEep8v0bANOlHz%2F714f5629ae8ab94eac2c7ccc7b61af60%2Fflux3-klein-grid-distilled__1_.png%3Fw%3D1000%26q%3D100&w=3840&q=75)
Credit: Black Forest Labs
On an RTX 5090 using an INT8 version, its 16-step distilled model takes 4.1 seconds to generate a 1,024 × 1,024-pixel image and 7.2 seconds to edit one. At 2,048 × 2,048 pixels, those times rise to 15 seconds and 43 seconds. 
![Flux 3 Klein 50-step image generation speed and times](https://venturebeat.com/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fjdtwqhzvc2n1%2F4yyDdHvcFRb6gH0i4VQyRO%2F7daefc6378f5fbb6fcb6315ca8771195%2Fflux3-klein-grid-base__1_.png%3Fw%3D1000%26q%3D100&w=3840&q=75)
Credit: Black Forest Labs
The 50-step base model on the same GPU takes 12.5 and 27.4 seconds at 1,024 × 1,024, and 79.8 and 236 seconds at 2,048 × 2,048. 
BFL labels each result as the fastest build for that GPU, measured one image per run.
The consumer-hardware spread is material. 
In the same 16-step test, an RTX 4070 takes 8.9 seconds to generate a 1,024 × 1,024-pixel image and 50.4 seconds at 2,048 × 2,048; editing takes 18.9 seconds and 150 seconds, respectively. 
On a DGX Station, BFL reports 0.59 seconds for 1,024 × 1,024 generation and 2.2 seconds at 2,048 × 2,048. The charts use INT8 for the GeForce cards and NVFP4 for the DGX Station and DGX Spark, so the cross-hardware figures are not a controlled comparison of chips alone. They measure local processing rather than the complete hosted API request.
These are Black Forest Labs' evaluations. The preference charts do not include enough information about prompts, judging, sample sizes or uncertainty to independently establish the size of the quality advantage. 
The charts quantify generation and editing on specified GPUs, but supply no matching competitor runs, energy or cost measurements, or quality assessment of the 16-step version against the 50-step base. They also do not measure 4K output.
The chart compares Krea 2, rather than the Krea 3 release separately briefed to VentureBeat. It likewise does not include OpenAI's current GPT Image 2.5 models or Google's Nano Banana 2.1. It therefore does not support a claim that Klein leads the entire image-model market.
## **Its rivals offer different combinations of access and control**
The closest comparison is [Alibaba's Qwen-Image 2.1](https://huggingface.co/Qwen/Qwen-Image-2.1), which has a seven-billion-parameter visual generator, downloadable weights, generation and editing in one model, native transparency and support for up to ten reference images.
However, Qwen-Image 2.1's [research license](https://huggingface.co/Qwen/Qwen-Image-2.1/blob/main/LICENSE) limits its standard grant to noncommercial research or evaluation. Commercial use requires a separate license. Klein's stated permission for smaller businesses creates a meaningful distinction. Earlier [Qwen-Image-Edit](https://huggingface.co/Qwen/Qwen-Image-Edit) uses Apache 2.0, so buyers should check the exact checkpoint rather than assuming consistent terms across the family.
[Ideogram 4.5](https://ideogram.ai/models/4.5/) offers generation and editing through its application, MCP and API, with native 2K output. Ideogram emphasizes maintaining image fidelity across repeated edits. Klein emphasizes downloadable deployment and customization; the supplied BFL evaluation does not test Ideogram's repeated-edit claim.
[OpenAI's GPT Image 2.5](https://developers.openai.com/api/docs/guides/image-generation) offers Sunburst for editing precision and Flare for faster everyday generation, with conversational editing through the Responses API. [Google's Nano Banana 2.1](https://ai.google.dev/gemini-api/docs/models/gemini-nano-banana-2.1) supports generation and editing at 1K, 2K and 4K, reference-image workflows and grounding through search.
Their documented API workflows provide alternatives for organizations that prefer provider-operated infrastructure. Klein adds a route for businesses that want to manage the model themselves.
A concurrent Krea 3 announcement adds competition on customization and price. In materials supplied to VentureBeat, Krea quotes $0.03 for a 1K image and $0.06 for a 2K image, and describes fine-tuning for particular products, people or styles. Those are Krea's launch claims, rather than results from BFL's comparison chart.  
| **Model or family**  | **Deployment described by its supplier**  | **Commercial-access distinction**  |  
| --- | --- | --- |  
| **FLUX 3 Image Klein**  | **Downloadable base, distilled and compressed weights; BFL API**  | **Free commercial use below BFL's revenue threshold; API costs $0.009 at 1K and $0.014 at 2K; separate self-hosting terms for larger businesses**  |  
| Qwen-Image 2.1  | Downloadable weights and local tooling  | Research license; separate commercial permission required  |  
| Earlier Qwen-Image-Edit  | Downloadable weights and Diffusers integration  | Apache 2.0  |  
| Ideogram 4.5  | App, MCP and API  | Provider-operated access  |  
| Krea 3  | Image editing with model personalization, according to launch materials  | Quoted image prices: $0.03 at 1K; $0.06 at 2K  |  
| GPT Image 2.5 / Nano Banana 2.1  | Hosted APIs for generation and editing  | Usage charges rather than the BFL revenue-based weight-license grant  |  
_Sources: BFL's and Krea's launch materials and the supplier documentation linked above. This compares access models, rather than establishing a common quality ranking._
## **Klein's API prices against rival image models**
Klein's published $0.009 price for a 1K image and $0.014 at 2K are below Krea's quoted $0.03 and $0.06 for those respective resolutions. 
BFL's larger FLUX 3 Image model was listed at $0.048 for a 1K image on the company's API pricing page at launch. These are prices for different models and do not establish equivalent output quality. BFL says Klein generation and editing cost the same at a given output resolution.
[Google lists](https://ai.google.dev/gemini-api/docs/pricing) standard Nano Banana 2.1 image-output charges of $0.0336 at 1K, $0.0504 at 2K and $0.113 at 4K. Those figures exclude input processing, text or thinking output, and any chargeable search queries.
[OpenAI lists](https://developers.openai.com/api/docs/guides/image-generation) GPT Image 2.5 image-output pricing at $30 per million tokens, with additional input charges. The per-image total varies by size and quality, so the token rate is not a flat fee for a finished image.
Klein's published per-image rates are**also below Google's listed image-output charges at 1K, 2K and 4K** , but Google's figures exclude other billable components. 
A total-cost comparison needs matching workloads and a complete accounting of each provider's charges.
## **Image generation and robotics share a foundation, not an identical product**
Black Forest Labs describes Klein as a release from the same FLUX 3 foundation underlying its recent[ FLUX 3 Action robotics model](https://venturebeat.com/infrastructure/black-forest-labs-debuts-flux-3-action-an-open-weights-ai-robotics-model-that-tops-the-leaderboard-at-half-the-size-of-its-competition). The company says shared training across images, video and audio helps the system learn visual structure and physical behavior. Klein's announced functions concern images; the release does not establish that the image checkpoint can directly control robots.
"FLUX 3 allows that community to adapt the same foundation to very different needs, from creative generation to robotics," said Robin Rombach, Black Forest Labs' co-founder and CEO, in the announcement.
The company also says external partner Cinder evaluated both Klein checkpoints for safety before release, following dataset filtering and post-training intended to limit harmful outputs. It reports fewer vulnerabilities than other popular models with open weights, but supplies no numerical comparison or full methodology in the release.
For enterprises, Klein's value will depend on whether local control, adaptation and licensing produce a better fit than a hosted alternative. 
The GPU measurements show why resolution, checkpoint and hardware choice belong in that calculation: moving from 1K to 2K can turn a few seconds into tens of seconds or minutes on a consumer card. BFL's published rates now provide an API cost at each offered resolution, while commercial self-hosting terms for larger organizations still require a separate agreement.
[![Agentic Infrastructure Stack Summit October 28 SF](https://venturebeat.com/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fjdtwqhzvc2n1%2F3PUNpBiDK3adbJGbhcWgkg%2F010d15a58119ec7d20fbc8b448754d1f%2F300x250.jpg&w=640&q=75)](https://venturebeat.com/agentic-infrastructure-stack-summit-oct-28-2026)[![Enterprise Agentic Orchestration Survey](https://venturebeat.com/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fjdtwqhzvc2n1%2F2hEjUQLMshtvpS078ukEeY%2F3526ef3b73334998b0330dd14a4100b3%2Fsurvey_ads-3.jpg&w=1200&q=75)](https://r39crwmcu9m.typeform.com/to/U8KdS0u4#audience_survey_id=xxxxx?utm_source=venturebeat&utm_medium=housead)
## More
[](https://venturebeat.com/)
[](https://www.facebook.com/venturebeat)[](https://www.instagram.com/venturebeat)[](https://x.com/VentureBeat)[](https://www.linkedin.com/company/venturebeat)[](https://www.youtube.com/venturebeat)
  * [Press Releases](https://venturebeat.com/press-releases)
  * [About Us](https://venturebeat.com/about)
  * [Contact Us](https://venturebeat.com/contact-2)
  * [Advertise](https://media.venturebeat.com)
  * [Share a News Tip](https://venturebeat.com/contact-2)
  * [Contribute](https://venturebeat.com/guest-posts)


  * [Cookie Policy](https://venturebeat.com/cookies)
  * [Privacy Policy](https://venturebeat.com/privacy-policy)
  * [Terms of Service](https://venturebeat.com/terms-of-service)
  * [Consent Preferences](https://venturebeat.com/technology/black-forest-labs-opens-flux-3-image-klein-weights-with-free-commercial-use-limited-to-smaller-businesses)
  * [Do Not Sell or Share My Personal Information](https://app.termly.io/notify/f592675e-4484-4dc9-bb50-462a84720662)
  * [Limit the Use Of My Sensitive Personal Information](https://app.termly.io/notify/f592675e-4484-4dc9-bb50-462a84720662)


© 2026 VentureBeat. All rights reserved.

