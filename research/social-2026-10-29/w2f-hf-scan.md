# w2f: Hugging Face scan for the social pipeline (wave 2, 2026-10-29)

Lane w2f-hf-scan. All facts accessed 2026-10-29. Tags: `verified` (read on the Hub API, model card or vendor doc this session), `measured` (my own run, logs in `research/social-2026-10-29/raw/w2f-ollama-test/`), `inferred`, `unverified`. Hub data came through the Hugging Face MCP connector (authenticated as user `Stanicky`, so an HF account already exists; its plan is unknown). Hub URL pattern: `https://huggingface.co/<owner>/<name>`.

## TL;DR

- **At the reference load, HF is a source of free weights, not a service to buy.** About 22 IG/FB posts, 13 TikToks, 13 Pins and 130 comments a month is roughly 150 to 300 images and 35 short clips. Local CPU does it for $0; a month on HF Jobs would be under $1 (`inferred`).
- **Two stages are already solved and need no new find:** ASR is faster-whisper small on the Fedora box (clipfeed, MIT weights `verified`), and cutouts are BiRefNet via rembg (MIT; decided 2026-10-27 in `.site-publication/account-repo-sync/research/cutouts/02-cutout-tools-pipeline.md`, and `.venv/cutout` already holds rembg 2.0.86 + onnxruntime).
- **License trap confirmed live:** `briaai/RMBG-2.0` (and 1.4) is CC BY-NC 4.0, "commercial use is subject to a commercial agreement with BRIA" (`verified`). A shop is commercial use. Also `facebook/musicgen-*` is CC-BY-NC-4.0 (`verified`), `cafeai/cafe_aesthetic` is AGPL-3.0 (`verified`), and `Qwen/Qwen2.5-VL-3B-Instruct` ships under `qwen-research` (named in its card; terms not read, treat as non-commercial until read).
- **The box can already read a still.** `qwen3.5:4b` on Fedora has `vision` capability (`verified` via `ollama show`) and wrote a usable alt-text caption in 25 to 33 s per image (`measured`). It is a draft tool, not a decider: it invented "suede", ran over my 125-character limit, and used the words "boutique" and "interior design" (both banned by the shop's rules).
- **Best-frame voting by a 4B model is position-biased.** Shown 4 frames, it picked "Frame 1" in both the original and the reversed order (`measured`). Scored one frame at a time it ranked plausibly (13 to 19 s per frame, n=4, one sample). Its "blurry" flag was right on a visibly out-of-focus boot photo and wrong on a glassware photo that is not blurry by eye; a 20-line Laplacian-variance check scored them 26.5 vs 722.6, illustrative only because they are different scenes (`measured`).
- **Hosted (`verified`, section 3):** PRO $9/mo with $2 credits; ZeroGPU 5 min/day free, 40 PRO; Jobs per minute from $0.01/h CPU to $0.40/h T4; Inference Providers at provider rates, no markup.
- **TTS and music:** nothing worth using. Kokoro-82M (Apache-2.0) and Chatterbox (MIT, voice cloning) have permissive licenses (`verified`), but an AI voice for a she/her persona is a disclosure and impersonation risk (`inferred`) and conflicts with "real objects, real hands". Music models are non-commercial (MusicGen) or generative (ACE-Step); use Instagram's Sound Collection per w1a, or silence plus text.
- **Comment intent and spam:** none needed. Reply policy is a keyword (`LINK`) plus drafts; a regex does the keyword, Claude drafts the rest. No HF dataset fits Instagram comments (largest hit had 22 downloads, `verified` on the Hub search; the conclusion is `inferred`).

Stages: `ingest > edit > caption > cover > publish > reply > analytics`. Nothing here touches Instagram, TikTok or Meta, so ban risk is nil except w1a's AI-info metadata caution (hosted generative editors may add C2PA tags; local mask tools do not, `inferred`; test first).

## 1. The throwaway test (Fedora, Ollama, real shop photos)

Setup: Ollama 0.34.0 in podman container `ollama-agents` (host port 127.0.0.1:11435), CPU only, i7-8565U. Models present: `qwen3.5:4b` (4.7B, Q4_K_M, capabilities completion/vision/tools/thinking, Apache-2.0, `verified`) and `hf.co/openbmb/MiniCPM5-2B-GGUF:Q4_K_M` (2.52B, **no vision capability**, `verified`, so it cannot read frames).

Exact commands (images only from the repo's `assets/`, public sample-site material):

```
ffmpeg -loglevel error -y -i assets/crops/IMG_6610_glass.jpg -vf "scale='min(768,iw)':-2" /tmp/w2f/IMG_6610_glass.jpg   # same for IMG_6612_boots.jpg, frames b02/b05/b08/b12
scp /tmp/w2f/* fedora:~/social-lab/w2f/
python3 vtest.py qwen3.5:4b alt|tag|vote|voterev|score     # POST http://127.0.0.1:11435/api/chat, stream:false, think:false, temperature 0.2, num_ctx 4096, num_predict 60-250
```

Script and all logs: `research/social-2026-10-29/raw/w2f-ollama-test/` (`vtest.py`, `alt.log`, `tag.log`, `vote.log`, `voterev.log`, `score.log`, `lapvar.py`). Fedora `~/social-lab/w2f` deleted afterwards and the model unloaded (`ollama stop`).

| Test | Wall time | Output (`measured`) | Good enough? |
|---|---|---|---|
| Alt text, pink-glass shelf (325 prompt tok) | 24.7 s (6.6 s was cold model load; 13.4 s image read; 4.6 s to write 35 tok, ~7.6 tok/s) | "A gold-framed shelf displays clear and amber-colored glassware with intricate designs, including floral patterns and etched details, set against a dark background with colorful fabric accents." | Draft only. About 195 characters against my "under 125" instruction; "floral" is wrong (the dark glass is etched with birds/reeds). |
| Alt text, boots (493 tok) | 33.3 s | "A pair of grey suede ankle boots with buckles and laces, photographed on a wooden floor." | Best result (88 characters). "Suede" is a material guess; the floor looks like wood-look flooring. Material, age, condition must come from Ricky's one line, never the model. |
| JSON tags + quality flags, boots | 37.4 s | `blurry: true, sharp_enough_for_listing: false` | Correct (the photo is out of focus). |
| JSON tags + quality flags, glassware | 32.3 s | listed 5 items, said `blurry: true, sharp_enough: false` | **Wrong on blur** (not blurry by eye). `sharp_enough_for_listing: false` is debatable: it is a 1400x622 px crop that may not be listing-grade. Laplacian 722.6 is illustrative only (different scene). |
| 4-frame "best Reel cover" vote | 54.3 s (800 tok) | "Frame 1 ... patterned chair" | Reversed order (47.9 s): again "Frame 1" (now the coat). **Position-biased; unusable as a decider.** |
| One frame at a time, score 1 to 10, JSON | 12.8 to 19.4 s per frame (234 tok) | chair 4.5, mannequins+lamp 3, clothing racks 3, coat+rug 6.5 | Plausible against my own read of the contact sheet (b05, b08 cluttered). n=4, one sample each, not repeatable proof. Its text said "clothing boutique interior" and "interior design showcase": banned wording, needs a lint. |

Non-model baseline (`measured`, repo's `.venv/cutout` Python, read-only, no install): variance of the Laplacian on 768 px width. Boots 26.5, glassware 722.6, walkthrough frames 10.9 to 23.9. Illustrative, not proof: variance depends on scene content (a shelf of glass edges scores high at any focus), so only a **within-clip** comparison means anything. Inside the walkthrough clip the four test frames order b02 23.9 > b12 20.4 > b05 14.2 > b08 10.9.

Cost implication (`inferred` from the timings): 300 images x ~30 s is about 2.5 hours of Fedora CPU a month, $0.

## 2. Options per stage

Columns: license from the model card or Hub API (`verified`); size; where it runs; Claude/Codex drivable; verdict. "CPU speed not stated" means the card states none and I did not measure it.

### ingest / edit: scene detection and clip scoring
| Option | License, size, date | Runs / drivable | Verdict |
|---|---|---|---|
| ffmpeg `select='gt(scene,x)'` or PySceneDetect (GitHub, not HF) | n/a | Windows PC and Fedora; CLI, both drive it | **use** (outside HF scope; GitHub lane w2e per BRIEF2). Wins when: any video, cheap first cut |
| Laplacian-variance blur gate (numpy/OpenCV, no model) | n/a, 20 lines | any; script | **use** as a within-clip sharpness ranker (`measured` above). Wins when: ranking frames of one clip |
| `qwen3.5:4b` single-frame score, already on box | Apache-2.0, 4.7B | Fedora CPU, 13 to 19 s/frame; curl or ssh | **use** as a pre-filter that drops clutter, never as the final pick. Wins when: a free offline gate is wanted |
| `google/siglip2-base-patch16-224` zero-shot scoring vs prompts like "one object, centered" | Apache-2.0, 1.66M downloads, 2025-02-21 | CPU plausible, speed not stated, needs torch install (not tried) | **study**. Wins when: clutter needs a text-defined test |
| `HuggingFaceTB/SmolVLM2-500M-Video-Instruct` (video-capable) | Apache-2.0, 507.5M params, 8.8M downloads | GGUF at `ggml-org/SmolVLM2-500M-Video-Instruct-GGUF` needs a llama.cpp build; Fedora has no compiler; not tried | **study**. Wins when: clip-level highlights are needed |
| Space `HuggingFaceTB/SmolVLM2-HighlightGenerator` (listed on the SmolVLM2 card; judged by name only, not opened) | Apache-2.0 model behind it | hosted demo; not tried | **study**. Wins when: a highlight-reel cut is wanted |
| Multi-image "pick the best frame" prompts to any small VLM | n/a | n/a | **avoid** (position-bias result above). Wins when: never at this model size |

### caption: ASR
| Option | License, size, date | Runs / drivable | Verdict |
|---|---|---|---|
| `Systran/faster-whisper-small` (CTranslate2) | MIT, 23.6M downloads, 2023-11-23 | Fedora CPU int8, already in clipfeed; a 2:10 reel transcribed "in under a minute" (desk wiki 2026-09-24, not re-run by me) | **use**. Wins when: default, box already has it |
| `distil-whisper/distil-large-v3.5`, `Systran/faster-distil-whisper-large-v3` | MIT; English only; 2026-04-13 | CPU speed not stated | **study**. Wins when: small mishears product words |
| `nvidia/parakeet-tdt-0.6b-v3` | CC-BY-4.0 (attribution), 627.1M params, 25 European languages, 2026-08-05 | NeMo/transformers/gguf tags; Python 3.14 on Fedora untested | **study**. Wins when: non-English clips appear |
| whisper.cpp ggml (`ggerganov/whisper.cpp`) | MIT | needs a compiler Fedora lacks; wiki already chose faster-whisper 2026-09-15 | **avoid**. Wins when: a compiler appears on the box |
| Hosted `openai/whisper-large-v3-turbo` (MIT) via hf-inference/deepinfra | live on the card | price not read | **study**. Wins when: the Fedora box is down |

Note (`inferred`): hands-first filming has little speech, so ASR matters only for burned-in captions when someone talks. ASR mishears brand and product words (wiki: "Wispr Flow" heard as "Whisper Flow"), so proofread any transcript that names a maker, age or price.

### caption: vision-language models (alt text, tags, "describe this real photo")
| Option | License, size, date | Runs / drivable | Verdict |
|---|---|---|---|
| `qwen3.5:4b` (Ollama, on box now) | Apache-2.0, 4.7B | `measured`: 25 to 37 s per still on Fedora CPU; curl, both drive | **use** for drafts and pre-filtering. Wins when: model is already loaded, free |
| `Qwen/Qwen3-VL-2B-Instruct` | Apache-2.0, 2.1B, 219.5M downloads, 2025-10-23 | smaller and faster than the 4B in principle; not tried | **study**. Wins when: 4B proves too slow |
| `HuggingFaceTB/SmolVLM2-2.2B-Instruct`, `SmolVLM-256M/500M` | Apache-2.0, 0.26B to 2.2B | CPU via GGUF/ONNX, speed not stated, not tried | **study**. Wins when: RAM or speed is tight |
| `microsoft/Florence-2-large` (and base) | MIT, 776.7M params, custom_code, 24.1M downloads, 2025-08 | terse captions, OCR, boxes; `trust_remote_code`; not tried | **study**. Wins when: OCR or tags beat prose |
| `vikhyatk/moondream2` | Apache-2.0, 1.93B, custom_code, 40.8M downloads, updated 2026-09-23 | CPU, speed not stated, not tried | **study** (`moondream/moondream3-preview` is `license: other`, not read: avoid until read). Wins when: short captions are wanted |
| `openbmb/MiniCPM-V-4_5` | Apache-2.0, 8.7B | too big for a 15 GB CPU box at usable speed (`inferred`) | **avoid** here. Wins when: a GPU is added |
| `LiquidAI/LFM2-VL-1.6B` | `lfm1.0` custom license, not read | n/a | **avoid** until read. Wins when: license is read and fits |
| `Qwen/Qwen2.5-VL-3B-Instruct` | `qwen-research` license (named in card; LICENSE file exists, not read) | n/a | **avoid** (treat as non-commercial). Wins when: never for a shop |
| `MiniCPM5-2B` already on box | no vision capability | cannot read frames | **avoid** for this stage. Wins when: text-only drafting |

Guardrail found in the test: model text reaches for "boutique", "interior design", and material guesses. Whatever a VLM drafts must pass a banned-word lint (interior design, boutique, store, shop floor, visit, showroom, brand, age, "vintage 19xx", condition claims) and may only state colour, shape, count and what is visibly in frame. Material, maker, age and condition come from Ricky's one line.

### cover: background removal
| Option | License, size | Runs / drivable | Verdict |
|---|---|---|---|
| `ZhengPeng7/BiRefNet` via `rembg i -m birefnet-general -dc` | MIT, 821.5K downloads | Windows PC (`.venv/cutout`) and CPU; CLI | **use** (decided 2026-10-27; the repo pilot owes real CPU seconds). Wins when: any non-glass object |
| `ZhengPeng7/BiRefNet_lite`, `_HR`, `_HR-matting` | MIT | lite is faster; HR-matting is the soft-alpha challenger for fringe | **use/study** per the cutout doc (glass stays uncut; seamless backdrop). Wins when: speed or fringe matters |
| `briaai/RMBG-2.0`, `RMBG-1.4` (rembg's default model) | CC BY-NC 4.0, commercial agreement required, gated | n/a | **avoid** (never run `rembg` without `-m`). Wins when: a Bria agreement is bought |
| Hosted Space `not-lain/background-removal` (reads as BiRefNet in `app.py`, Space license MIT) | MIT Space on ZeroGPU | listed in the HF MCP `dynamic_space` tool, so Claude can call it; Codex via script only (MCP support unverified) | **study** (uploads the photo to a public Space; fine for sample-site photos, not for unreleased stock). Wins when: no local setup, a one-off cut |

### cover: best-frame / aesthetic scoring, upscaling
| Option | License | Verdict |
|---|---|---|
| Laplacian variance + human pick from a contact sheet (Claude reads it) | n/a | **use** (cheap; within-clip only; illustrative, not proof). Wins when: choosing among burst frames |
| `shunk031/aesthetics-predictor-v2-sac-logos-ava1-l14-linearMSE` (304.9M, custom_code) | no license tag on the Hub card | **study** (read the upstream license first). Wins when: a numeric aesthetic score is wanted |
| `apple/MobileCLIP-S2-OpenCLIP` | `apple-amlr` / `apple-ascl`; terms page 404 from my fetch | **avoid** until read. Wins when: terms permit commercial use |
| `cafeai/cafe_aesthetic` | AGPL-3.0, trained for anime dataset curation | **avoid**. Wins when: never (AGPL, anime-trained) |
| Automated aesthetic picker as a decider | | **none good enough**; keep the human or a template rule. Wins when: n/a |
| `caidas/swin2SR-classical-sr-x2-64` (Apache-2.0), Real-ESRGAN x4plus (Qualcomm export, BSD-3-Clause) | permissive | **avoid for listing photos**: super-resolution invents texture, which conflicts with "real objects only"; acceptable only for a background tile of a cover. Wins when: a cover background is low-res |
| InstantIR / Photo-Mate Spaces (generative restoration) | | **avoid** (generative). Wins when: never under real-photos-only |

### edit: voiceover and music (list only; skip generative product imagery)
| Option | License, size | Verdict and flag |
|---|---|---|
| `hexgrad/Kokoro-82M` | Apache-2.0, 82M, 10.9M downloads | **study**; avoid as Hollie's voice (a synthetic she/her voice for a persona; Meta's treatment of AI audio not verified). Wins when: a neutral non-persona voice is wanted |
| `ResembleAI/chatterbox` | MIT, voice cloning | **avoid** (cloning a voice = impersonation risk). Wins when: Hollie's own consented clone, her call |
| `facebook/musicgen-small/medium/large` | CC-BY-NC-4.0 | **avoid** (non-commercial). Wins when: never in a shop |
| `ACE-Step/Ace-Step1.5` | MIT per card, updated 2026-02-03 | **avoid**: generative music, training-data rights unread, GPU-class model (`inferred`). Wins when: rights are read and a GPU exists |
| Instagram Sound Collection / silence + on-screen text | per w1a: commercial-safe | **use** (w1a finding, not re-verified here). Wins when: any Reel needs sound |

### analytics: comment intent and spam
| Option | License | Verdict |
|---|---|---|
| Regex for `LINK` + Claude drafts everything else (no HF) | n/a | **use** (matches the reply policy shape). Wins when: volume stays near 30 a week |
| `MoritzLaurer/deberta-v3-large-zeroshot-v2.0` (zero-shot; card says runs on CPU and GPU) | MIT, 118K downloads | **study**. Wins when: hundreds of comments a week |
| `SamLowe/roberta-base-go_emotions` | MIT, 5.0M downloads | **study** for a complaint/anger flag. Wins when: tone triage is wanted |
| `mrm8488/bert-tiny-finetuned-sms-spam-detection` | no license field; trained on SMS, 0.98 val accuracy there | **avoid** (wrong domain). Wins when: never on IG comments |
| HF datasets: `PolyAI/banking77` (banking intents), four Instagram-comment sets with 2 to 22 downloads | | **none good enough** for comment intent. Wins when: n/a |

## 3. Hosted options, verified prices (all from vendor pages, 2026-10-29)

| Product | Price and limits | Source | Fit |
|---|---|---|---|
| PRO account | $9/mo; $2 monthly compute credits; 8x ZeroGPU quota; host ZeroGPU, Gradio, Docker Spaces | https://huggingface.co/pricing | not needed at this load |
| Inference Providers | free users: no credits, must buy; PRO $2/mo; pay-as-you-go at provider rates, "no additional fees"; `hf-inference` is mostly small CPU models (as of July 2025) | https://huggingface.co/docs/inference-providers/pricing | VLM per-provider prices not read |
| ZeroGPU | quota/day: free 5 min, PRO 40 min, Enterprise 60 min; overage $1 per 10 min; Gradio SDK only; RTX Pro 6000 Blackwell | https://huggingface.co/docs/hub/spaces-zerogpu | fine for an occasional BiRefNet batch; not an API to depend on |
| Spaces | CPU Basic free (2 vCPU, 16 GB, sleeps after 48 h idle); CPU Upgrade $0.03/h ($22/mo always-on); T4 small $0.40/h ($288/mo) | https://huggingface.co/docs/hub/spaces-gpus | a Space is a web demo; wrong tool for a batch pipeline |
| Jobs | per-minute billing; CPU Basic $0.01/h, CPU Upgrade $0.03/h, T4 small $0.40/h; default timeout 30 min; any user with positive credit balance | https://huggingface.co/docs/hub/jobs-pricing | **best hosted fit**: run `hf jobs run` for a cutout batch, pay cents |
| Inference Endpoints | CPU 1 vCPU/2 GB from $0.03/h ($24/mo) | https://huggingface.co/pricing | always-on; scale-to-zero not verified |

**Month at the BRIEF2 reference load** (`inferred`): local Fedora and PC $0; a hosted month at 3 hours CPU Upgrade plus 10 minutes of T4 is about $0.16; PRO $9 buys only credits and quota the load does not use. Raw captures: `raw/w2f-hf-pricing.md`, `-providers-pricing.md`, `-zerogpu.md`, `-jobs.md`, `-spaces-gpus.md`.

## 4. Recommendation for Holliewood & Vine

| Tier | What | Human still does |
|---|---|---|
| (a) free and native | Local only: faster-whisper small for captions, rembg + BiRefNet for cutouts, Laplacian sharpness gate, Claude reading a contact sheet to pick the cover. No HF account spend. | Picks the cover, approves alt text, supplies material/age/condition in the one line. |
| (b) one paid tool | None justified. If Ricky wants one hosted thing: top up HF credits for **Jobs** ($0.01 to $0.40/h, per minute) for cutout batches. Skip PRO ($9). | Same as (a). |
| (c) full Claude + Codex | Claude Code on the PC calls the Fedora Ollama REST for a clutter/blur pre-filter and draft alt text, then a banned-word lint, then Claude drafts the caption from the frames; Codex wires scripts. `qwen3.5:4b` is a free offline gate that saves the subscription window, not a replacement for Claude's reading. | Mode A: taps Publish. Mode B: only alt text that passes lint, cutouts, and `LINK` replies run unattended; prices, claims, provenance, any person, complaints and anything touching the fixed constraints stay human. |

Approval-mode notes: in B a VLM may never write material, age, brand, condition or price; transcripts that name makers need a proofread; cover choice should be a template rule or human, not a model vote.

## 5. Decision matrix

| Option | Stage | Cost/mo at reference load | Setup hours | Claude/Codex drivable | Ban/ToS risk | Approval fit |
|---|---|---|---|---|---|---|
| faster-whisper small (installed) | caption | $0 | 0 to 1 | yes (ssh/CLI) | none | A and B (proofread) |
| rembg + BiRefNet MIT | cover | $0 | 2 to 3 | yes (CLI) | none; BRIA trap | A and B (not glass) |
| `qwen3.5:4b` Ollama pre-filter | caption/edit | $0 (~3 h CPU) | 2 | yes (curl) | none; text needs lint | A; B for gate only |
| Laplacian sharpness gate | edit/cover | $0 | 1 | yes | none | A and B |
| HF Jobs batch | cover | under $1 | 3 to 4 | yes (`hf` CLI) | none | A and B |
| HF PRO + ZeroGPU/`dynamic_space` | cover | $9 | 1 | Claude via MCP; Codex unverified | none; photo goes to a public Space | A |
| SigLIP 2 frame scoring | edit | $0 | 4 to 6, untested | yes | none | A |
| Kokoro / Chatterbox / MusicGen / ACE-Step | edit | $0 compute | n/a | yes | AI-audio/label and NC-license risk | not recommended |

**Build effort** (Claude Code + Codex): about 6 to 10 hours: Ollama gate + lint 2 to 3, BiRefNet pilot 2, Laplacian gate 1, caption burn-in from faster-whisper SRT 1 to 2. Ricky by hand: cover pick, alt text approval, the one-line facts, and any account/credit top-up.

## 6. X verified, Y need review

- Qwen2.5-VL-3B: Hub metadata shows no license, card header says `qwen-research` (verified); whether that bars commercial use is need review (LICENSE not read).
- Free-account hosting: the ZeroGPU doc says free accounts can host up to 2 ZeroGPU Spaces (verified); the Spaces hardware doc says creating a new compute (Gradio/Docker) Space needs a paid plan (verified); the pricing page lists hosting under PRO. Need review before anyone relies on a free hosted demo.
- ACE-Step 1.5 card says MIT; training-data rights not checked. Moondream 3, LFM2-VL and MobileCLIP licenses are named but their terms were not read (the Apple LICENSE URL returned 404).
- Qwen3.5's "blurry" flag on the glassware crop is wrong by eye and disagrees with the Laplacian number (mine, n=2, different scenes).
- No finding changes a fixed constraint; the VLM wording clash ("boutique", "interior design") is a lint requirement, not a change to the rules.

## 7. Questions only Ricky can answer

1. Is a free offline pre-filter worth keeping, or should every frame go to Claude directly (subscription window vs 25 to 35 s of Fedora CPU each)?
2. Does any synthetic voice ever front the brand? (Recommended no.)
3. Are unreleased stock photos allowed to be uploaded to a public HF Space, or local-only?
4. What plan is the existing HF account `Stanicky` on?

## 8. Gaps and a disclosure

- Not run: SmolVLM2, Florence-2, Moondream, SigLIP on CPU (no torch install on Fedora; llama.cpp build impossible without a compiler). BiRefNet CPU seconds still unmeasured (prior doc cites one 6 s anecdote). Per-provider VLM prices not read. Whether Instagram labels AI audio not checked. I did not invoke any hosted Space.
- **Disclosure:** at about 13:51 local I ran `pkill -f crawl4ai` in Git Bash to stop my own crawl loop, which had in fact already finished. If another wave-2 lane lost a crawl4ai call around then, that was me; re-run it.
- Zero-byte wall captures deleted. Fedora `~/social-lab/w2f` removed; `w2a` and `w2b` left untouched.
