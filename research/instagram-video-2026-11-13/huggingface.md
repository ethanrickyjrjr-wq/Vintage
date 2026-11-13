2026-11-13 · lane `huggingface` · open models and hosting on Hugging Face for Instagram listing videos (Holliewood and Vine)

Method: model cards and docs fetched today with crawl4ai into `raw/huggingface-*.md` (17 files; `huggingface-misc-merged.md` joins ten small pages, each under a `########` header). Discovery used the Hugging Face MCP search (Lightricks and Wan-AI listings). Anything not quoted from those files is marked "unverified". I did not create Spaces, run jobs or spend money.

## 0. Local context (from the repo, not the web)
- PC: RTX 4060 Ti with 16 GB VRAM, about 6.3 GB system RAM free at that check (`docs/mustache-moonwalk.md`, "This PC has an RTX 4060 Ti with 16 GB VRAM ... only about 6.3 GB system RAM was free").
- What worked: a local Wan-Animate render "used NF4 / six steps / seed 57 and completed inference in 302 seconds on the RTX 4060 Ti", output 384 square, 24 fps, 4.5 s. Note this is video-to-video motion transfer, not still-to-video.
- What broke: the `techfreakworm/LTX2.3-Studio` Space "returned **Generation failed**"; a ZeroGPU request failed with "The requested GPU duration (382s) is larger than the maximum allowed"; the first Wan-Animate-2 Space output "failed visual review".
- Rules honoured here: Photoroom does cut-outs; no ghost mannequin or AI try-on by default.

## 1. Image-to-video from one product still
Quotes are from the model cards.

**Wan 2.2 TI2V-5B** (https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B): "License: apache-2.0". "supports both text-to-video and image-to-video generation at 720P resolution with 24fps and can runs on single consumer-grade GPU such as the 4090". Command note: "This command can run on a GPU with at least 24GB VRAM (e.g, RTX 4090 GPU)" using `--offload_model True --convert_model_dtype --t5_cpu`. 720P is "1280*704". So the card's own number is 24 GB with offload; on a 16 GB card it needs quantisation or more offload, which the card does not claim (unverified). The license section says "We claim no rights over the your generated contents".
**Wan 2.2 I2V-A14B** (https://huggingface.co/Wan-AI/Wan2.2-I2V-A14B): Apache-2.0, 480P and 720P; "This command can run on a GPU with at least 80GB VRAM." Not for the 4060 Ti without heavy quantisation (unverified); fine on a rented A100 80 GB.
**LTX-2.5** (https://huggingface.co/Lightricks/LTX-2.5-Diffusers, newest family, files updated 22 Oct 2026): "an open world model with open weights, built for local execution and fine-tuning", generates "synchronized, high-fidelity video and audio from text, image, and video inputs". 22B class (LoRA cards say "LTX-2.5-22B"). Download: "72 GB rather than 110 GB" for the distilled path, so a 16 GB card needs fp8/GGUF-style quantisation plus offload; the LTX-2 readme only says "In cases of GPU memory constraints, consider `--quantization fp8-cast --offload {cpu, disk}`" (https://github.com/Lightricks/LTX-2, in `raw/huggingface-ltx25-diffusers.md` and the earlier README crawl). No VRAM figure was published on pages I read: unverified. The Diffusers repo is gated ("You need to agree to share your Hugging Face information to access this model"; the agreement text says users "consent to receive offers and updates including targeted and personalized advertisements"). Also "LTX-2.5 support is not in a `diffusers` release yet, so install from main".
- LTX license (https://huggingface.co/Lightricks/LTX-2.5-Diffusers): "Under $10M annual revenue: Commercial and production use at no cost under the LTX-2.x Community License. Transfer of fine-tunes may require a paid license". Over $10M needs a paid agreement. The LTX-2 license file (`raw/huggingface-ltx2-license.md`): "Entities with annual revenues of at least $10,000,000 ... are required to obtain a paid commercial license". A small shop is under that line: commercial OK, with the gate click-through.
**LTX-2.5 Cinemagraph LoRA** (https://huggingface.co/Lightricks/LTX-2.5-22b-LoRA-Cinemagraph): "Transforms still images into smooth, looping cinemagraphs with selective motion while keeping the rest of the scene frozen." Prompting: "Emphasize 'locked-off static camera' and 'seamless natural loop'"; "Best results at 512×704 pixels, 25 frames (the training resolution)" (about 1 second). Out of scope: "Scenes with camera movement, character/body movement". Its examples are scenes (neon, water, clouds), not garments; garment fidelity untested (unverified). License tag "ltx-2.x-community-license".
**HunyuanVideo-I2V** (https://huggingface.co/tencent/HunyuanVideo-I2V): "The minimum GPU memory required is 60GB for 720p." License `tencent-hunyuan-community`; the license text says it "DOES NOT APPLY IN THE EUROPEAN UNION, UNITED KINGDOM AND SOUTH KOREA" (in the merged file). Skip: too big, territory-limited.
**CogVideoX1.5-5B-I2V** (https://huggingface.co/zai-org/CogVideoX1.5-5B-I2V): "BF16: 9GB minimum*" with diffusers optimisations (offload; INT8 "at the cost of significant speed reduction"), 5 or 10 s at 16 frames/second, "Single A100: ~1000 seconds (5-second video)" at 50 steps. License "other": "Users who wish to use the models for commercial purposes must register and obtain a basic commercial license" (merged file). Fits 16 GB but slow, 16 fps, registration needed. Older family; try only as fallback.
**Stable Video Diffusion 1.1** (merged file): 25 frames at 1024x576; community license "preserves free access ... for people or organizations generating annual revenue of less than US $1,000,000". Old; low value.

## 2. Subtle camera move / keep the product unchanged
- No model card I fetched promises fabric, label or flaw preservation. Diffusion image-to-video re-draws every pixel, so any such claim is unverified and the key risk stands. Only Cinemagraph states "keeping the rest of the scene frozen", and only for static-camera non-garment scenes.
- LTX-2.5 lists `IC-LoRA-Layout-To-Render` with a `camera-control` tag, `Slow-Motion-Control` and a Pixel-Spatial-Upscaler in the hub search (https://huggingface.co/Lightricks/LTX-2.5-22b-IC-LoRA-Layout-To-Render); I did not fetch those cards (unverified).
- Stable Virtual Camera (https://huggingface.co/stabilityai/stable-virtual-camera) is "Free for research and non-commercial use": not usable here.
- My reading, not a fetched fact: the safe way to get a camera move that keeps the garment exact is not a generative model. A Ken Burns zoom, pan or parallax done in ffmpeg or a video editor on the real Photoroom photo changes no pixels of the cloth. Generative image-to-video is only worth a test on non-garment hero shots (a frame, lamp, neon) and must be compared side by side with the photo before posting.

## 3. Virtual try-on
- IDM-VTON (https://huggingface.co/yisol/IDM-VTON): License `cc-by-nc-sa-4.0`, non-commercial.
- CatVTON (https://huggingface.co/zhengchong/CatVTON): "bf16 ... 1024x768 only requires about 8G VRAM"; but "All the materials, including code, checkpoints, and demo, are made available under the Creative Commons BY-NC-SA 4.0 license ... for non-commercial purposes".
- Verdict: both are non-commercial, so they cannot be used for shop promotion at all, and they also break the standing no-AI-try-on rule. Skip. If Ricky ever wants labelled "styling idea" images, a commercially licensed vendor would be needed; I did not find one on Hugging Face (unverified).

## 4. Upscaling and frame interpolation
- RIFE (https://github.com/hzwer/ECCV2022-RIFE, in the merged file): "MIT license". Useful to smooth a 12-16 fps generation to 30 fps or give a slow-motion glide to a Ken Burns clip; usable commercially. VRAM not stated on the page I read (unverified, but known as a light model).
- Real-ESRGAN page on HF (ai-forever/Real-ESRGAN) fetched but no licence line was extracted; unverified. LTX offers its own x2 spatial and temporal upscalers inside the LTX-2 family ("An x2 spatial upscaler", "An x2 temporal upscaler for the ltx-2 latents ... for higher FPS", LTX-2 card).
- Note Photoroom stays the cut-out tool; none of this touches cut-outs.

## 5. Speech
- Kokoro-82M (https://huggingface.co/hexgrad/Kokoro-82M): "License: apache-2.0". "an open-weight TTS model with 82 million parameters." "Kokoro has been deployed in numerous projects and commercial APIs. We welcome the deployment of the model in real use cases." Small enough for the CPU Fedora box or the PC. Commercial OK.
- XTTS-v2 (https://huggingface.co/coqui/XTTS-v2): "licensed under Coqui Public Model License" (CPML, a non-commercial license; I did not read the license text, so treat as not OK, unverified detail). Skip.
- F5-TTS (https://huggingface.co/SWivid/F5-TTS): "License: cc-by-nc-4.0". Non-commercial. Skip.
- Whisper large-v3-turbo (https://huggingface.co/openai/whisper-large-v3-turbo): "License: mit". Fine for captions and burned-in subtitles. Card warns it is "prone to generating repetitive texts", so proofread.
- Cloning a voice of Hollie is a separate decision (consent, disclosure); not researched here.

## 6. Music
- MusicGen (https://huggingface.co/facebook/musicgen-small): "Code is released under MIT, model weights are released under CC-BY-NC 4.0." Non-commercial. Skip.
- Stable Audio Open 1.0 (merged file): license `stable-audio-community`; "For commercial use, please refer to https://stability.ai/license". Conditional, unverified terms; skip.
- MMAudio (merged file): "licensed under CC BY-NC 4.0 and can be used for non-commercial purposes only." Skip.
- ACE-Step v1 3.5B (https://huggingface.co/ACE-Step/ACE-Step-v1-3.5B): "License: apache-2.0". "novel open-source foundation model for music generation". Speed table lists "RTX 4090 | 34.48x" real-time; "Longer generations (>5 minutes) may lose structural coherence". 4060 Ti speed and VRAM not read (unverified). Commercial OK per tag, though who owns training-data rights was not examined.
- Important separate point (not from HF): whatever music is used, Instagram's own library rules belong to another lane; generated music avoids copyright claims but check how it is labelled.

## 7. Hosting without the PC
- PRO plan (https://huggingface.co/pricing): "$9 /month"; includes "$2 of included inference credits monthly", "8× ZeroGPU quota and highest queue priority".
- ZeroGPU (https://huggingface.co/docs/hub/spaces-zerogpu): "ZeroGPU Spaces are available to use for free to all users". Daily quota table: "Unauthenticated 2 minutes; Free account 5 minutes; PRO account 40 minutes (extensible)". Hardware "NVIDIA RTX Pro 6000 Blackwell", `large` = 48 GB, `xlarge` 96 GB. Each Space sets its own max duration, which is what broke the Wan-Animate-2 request earlier. Public community Spaces: your product photos go to a third-party Space (privacy; also the Space's own terms apply); no SLA, may break.
- Inference Providers (https://huggingface.co/docs/inference-providers/pricing): "pay-as-you-go pricing ... no markup from Hugging Face"; "PRO Users $2.00" monthly credits; "Free Users: None". Whether a given video model is served by a provider and its per-clip price: unverified (I did not fetch the provider model list).
- HF Jobs (https://huggingface.co/docs/hub/jobs-pricing): "Jobs are billed per minute based on the hardware used. For example, 10 billable minutes on `a10g-small` costs approximately $0.17". Hourly prices: L4 24 GB $0.80, L40S 48 GB $1.80, A100 large 80 GB $2.50, RTX PRO 6000 96 GB $2.75 (https://huggingface.co/pricing). So an A100 80 GB hour is $2.50, enough for Wan2.2 A14B (80 GB requirement) at roughly cents per clip if a clip takes a few minutes (clip time unverified).
- Tradeoff: the PC is free per clip but slow (302 s for 4.5 s at 384 px on Wan-Animate NF4). A rented L40S or A100 is cheap per clip but needs a script and a token; only worth it if the generative route proves useful on the test photos.

## Could not verify
- Real VRAM for LTX-2.5 on 16 GB, and for Wan2.2 TI2V-5B below 24 GB.
- Any garment-fidelity result for any model (none published on the cards).
- Clip times on the 4060 Ti for I2V (only the Wan-Animate moonwalk number exists).
- Real-ESRGAN license, XTTS CPML terms text, Stable Audio commercial terms, provider-served video models and prices.
- HF Space availability today (not tested; no jobs run).

## Table
| Model | Use | VRAM | License | Commercial OK? | Verdict |
|---|---|---|---|---|---|
| Wan2.2 TI2V-5B | I2V, 720p 24 fps | card: 24 GB w/ offload; 16 GB unverified | Apache-2.0 | Yes | Try (non-garment shots only) |
| Wan2.2 I2V-A14B | I2V 480/720p | card: 80 GB | Apache-2.0 | Yes | Try on rented A100 only |
| LTX-2.5 (+ Cinemagraph LoRA) | I2V + audio, loops | unverified; 72 GB download, needs fp8+offload | LTX-2.x Community (free under $10M revenue) | Yes, gated | Try |
| HunyuanVideo-I2V | I2V | 60 GB | Tencent community, excludes EU/UK/KR | Territory-limited | Skip |
| CogVideoX1.5-5B-I2V | I2V 5-10 s, 16 fps | 9 GB min (slow) | CogVideoX license, register for commercial | Yes after registering | Skip (fallback) |
| Stable Virtual Camera | camera move | n/a | Stability non-commercial | No | Skip |
| IDM-VTON / CatVTON | try-on | CatVTON ~8 GB | CC-BY-NC-SA 4.0 | No | Skip |
| RIFE | interpolation | light, unverified | MIT | Yes | Use |
| Kokoro-82M | voiceover TTS | tiny (82M params) | Apache-2.0 | Yes | Use |
| XTTS-v2 | TTS/clone | unverified | Coqui CPML | No (non-commercial) | Skip |
| F5-TTS | TTS/clone | unverified | CC-BY-NC-4.0 | No | Skip |
| Whisper large-v3-turbo | captions | unverified | MIT | Yes | Use |
| MusicGen | music | unverified | CC-BY-NC-4.0 weights | No | Skip |
| MMAudio | video-to-audio | unverified | CC-BY-NC-4.0 | No | Skip |
| Stable Audio Open | music/SFX | unverified | Stability community | Conditional | Skip |
| ACE-Step v1 3.5B | music | unverified | Apache-2.0 | Yes | Try |
| HF PRO / ZeroGPU / Jobs | hosting | up to 96 GB | $9/mo; Jobs from $0.40/h | n/a | Try only for tests |

## Recommended minimal stack
1. Hero motion: ffmpeg Ken Burns / parallax on the real Photoroom image (no pixels invented), plus RIFE only if smoothing is needed. This is the safe default for clothes.
2. Optional experiment, not default: Wan2.2 TI2V-5B or LTX-2.5 Cinemagraph on non-garment pieces, compared side by side with the photo before use; run on a rented GPU via HF Jobs rather than force it onto 16 GB.
3. Voiceover: Kokoro-82M (Apache-2.0) on CPU. Captions: Whisper large-v3-turbo (MIT), proofread by hand.
4. Music: ACE-Step (Apache-2.0) only if a library track is not wanted; skip MusicGen/MMAudio (non-commercial).
5. No try-on models. Do not buy PRO ($9/mo) until a model proves useful; free ZeroGPU (5 min/day) is enough to test.
