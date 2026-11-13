# Instagram video for new listings (2026-11-13)

Status: research and decisions only. Nothing was posted, no account was touched, nothing was bought. Built from seven Sonnet lanes in `research/instagram-video-2026-11-13/` (every external claim there is quoted from a page fetched that day with crawl4ai; raw pages in `raw/`). The parent re-checked the claims most likely to be wrong against those raw pages: Sora's shutdown dates, Photoroom video not on Pro, the 100-posts-a-day API limit, Trial Reels in the API, Planoly's private-reply rule, Remotion's licence and Wan's VRAM. All matched. Decisions marked "Ricky" are his to make.

## The answer in five lines

1. **Every new listing gets one short reel made from the real Photoroom stills** (pan, zoom, text, price, "link in bio"), plus a same-day Story with a link sticker. Reels reach strangers; Stories and the bio link close the sale.
2. **Claude builds the reels itself with ffmpeg.** A working 11 s, 1080x1920 proof exists (`research/instagram-video-2026-11-13/poc/just-listed-poc.mp4`, item 06, renders in about 2 s, free). No paid video tool is needed for listings.
3. **No AI-generated motion on garments.** No model or vendor promises to keep the fabric, labels and flaws unchanged. Under our 30-day returns, the seller pays for description errors, so an altered garment in a promo is a real cost. AI motion is allowed only for mood/brand clips and, after a side-by-side check, maybe decor.
4. **ChatGPT makes stills and words, not video.** Sora was shut down (web and app April 26, 2026; API September 24, 2026).
5. **Fable 5.2 builds the pipeline** in the order below: renderer, captions in Hollie's voice, Telegram approval, batch queue, then (only with Ricky's credentials) auto-posting.

## What Instagram rewards (lane `reels-mechanics`)

- New reels are first shown to a small group of non-followers and widened if they hold attention (creators.instagram.com, April 2024). The strongest signals are shares/sends, watch-through, likes and audio-page visits (Mosseri's ranking post, May 2023, so treat as old but official).
- Instagram shows less of reels that are "low-resolution or watermarked", "muted or contain borders", "majority text", or already posted. Accounts that mostly post unoriginal content (borders, watermarks, speed changes, "just crediting") lose recommendations over a rolling 30 days. So: no CapCut or TikTok exports with their watermark or end card, no reposts, and keep sound on.
- **Trial Reels** go to non-followers only and stay off the grid; graduate them after about 24 to 72 hours if they do well. Official eligibility says "a professional account", with no follower minimum stated; check the toggle in the app. The Graph API can post them too (`trial_params`).
- **Product tags are out.** Meta says some Shops and checkout features "are no longer supported", and tagging needs a Commerce Manager catalog with checkout. No route was found for an eBay-only seller. Use link in bio and Story link stickers.
- The Edits app exports "with no watermark"; phone price unverified.
- **Fix first (Ricky/Hollie):** the bio still says Loveland and studio rental. Change it to Southwest Florida vintage and resale before promoting.

## Formats, ranked (lane `vintage-formats`)

No source gives hard numbers on reels turning into sales for small resellers; reels bring viewers, sales close through Stories, DMs and the link. Sources favour under about 10 s for low-lift stills reels, the hook in the first 2 s, and in-app captions over burned-in paragraphs. Full shot outlines (phone version and photos-only version) are in the lane report.

1. **"Just listed" price-tag reveal** (10 to 20 s): hero, side, back, label, flaw, price, end card. This is the default for every listing and the one the renderer makes first.
2. **"What the label tells you"** detail macro: label and detail photos, an arrow or circle and one fact each.
3. **Weekly drop day:** Story countdown the day before, then a reel of 4 to 6 reveals. Same day and time each week (Ricky/Hollie pick it).
4. **One piece, three ways:** uses the maximalist room; phone footage is better here.
5. **Before and after:** only with a real "before" photo.
6. **Guess the decade or the price:** an engagement post, not every listing.

## Tools: use, try, skip

| Tool | What it can do for us | Verdict |
|---|---|---|
| **Claude + ffmpeg** (this repo) | Templated reels from real stills, captions, alt text, hashtags, queue, Telegram approval, API posting later | **Use.** Free; proof works |
| Remotion | Fancier code-made motion | Later upgrade; licence page: "completely free ... for individuals and companies of up to 3 people" |
| **Photoroom Pro** (already paid) | Cut-outs, shadows, batch, resize to 9:16 stills | **Use** for stills and frames |
| Photoroom video (Video Ad Maker, Product Animator) | 5 to 10 s 9:16 clips from up to 6 photos | Not on Pro ("Not included"); Max or Ultra only, price unread. Skip unless one test on Max wins |
| Photoroom AI Backgrounds / Virtual Model | Regenerated scenes or models | Never the main shot of a used item |
| Photoroom API | $0.02 per cut-out, $0.10 per edit; not included in Pro | Only if the pipeline later needs scripted cut-outs |
| **ChatGPT** | Image editing and clean text on price/measurement cards, titles, captions, scripts | **Use** for words and graphic cards only. It rewrote handwriting and reshaped an object in a third-party test, so never on garment photos. No video (Sora shut down). Prices on OpenAI's page did not render |
| Gemini (Omni in the app, AI Pro $19.99) | Up to 5 photos to a 10 s video; SynthID watermark | Try only for brand/mood clips |
| Runway Standard ($12/mo yearly, "No watermarks") | Image-to-video | The one paid generator worth a test for mood clips; test 3 items first. Not needed for listings |
| Pika, Luma, Kling, Higgsfield, Canva AI clips | Image or text to video | Skip for now (Canva's clips are text-only, 16:9, and it may not give exclusive rights) |
| CapCut | Editor with AI extras | Skip for exports that carry its watermark/end card; Instagram's Edits app or our ffmpeg instead |
| Hugging Face Wan 2.2 / LTX-2.5 (Apache-2.0 / free under $10M) | Open image-to-video | Not on the 4060 Ti (cards say 24 GB+ and 72 GB downloads). Revisit only for decor |
| Hugging Face Kokoro-82M (Apache-2.0), Whisper large-v3-turbo (MIT), RIFE (MIT) | Voiceover, captions, smoother motion | **Try** if voiceover or caption files are wanted |
| IDM-VTON, CatVTON, F5-TTS, XTTS, MusicGen | Try-on, TTS, music | **Skip:** non-commercial licences |
| Meta Sound Collection | Licensed music | **Use** for music on the business account |

## Rules for our videos (lane `rules-and-risk`; research, not legal advice)

1. Show the real piece. No AI change to colour, fit, fabric or flaws. eBay's picture policy requires photos that "accurately represent the item"; the FTC judges words and pictures together.
2. Any flaw in the listing appears in the reel's text or footage too (omissions count).
3. Size, condition and price in the video match the listing exactly.
4. Realistic AI voice or photorealistic AI video gets Instagram's AI label. Real footage and graphics need none.
5. Music from Meta's Sound Collection; no trending commercial tracks on the business account.
6. No "like/share to get the link" gating (Meta Spam policy). Manual "ask me" replies are fine. **Comment-to-DM bots: hold.** Planoly says Meta's official Private Replies API allows one reply per commenter within 7 days, but Meta's own page was not read and the rules lane found no Meta page on it. Re-check before Fable builds any auto-DM.
7. Original, unwatermarked, vertical, sound on.
8. A clone of Hollie's voice only from her own verified recording with her consent (ElevenLabs allows own-voice only).
9. Promo text overlays go on Instagram only, never on eBay listing photos (eBay bars added text, borders and watermarks).

## What Fable 5.2 builds (from lane `claude-builds`)

Each item's inputs, files and tests are spelled out in `research/instagram-video-2026-11-13/claude-builds.md`, "Build list". Order:

1. **`tools/reels/make_reel.py`**, grown from `poc/make_poc.py`: N scenes from `reel.json`, auto-fitting text, per-photo crop and zoom, hook scene, end card, cover PNG. Fix the PoC's two faults: the square back photo leaves the garment small, and the title card's lower half is empty. Test on item 06, a framed print and a pair of shoes; a script asserts the specs Meta publishes for Reels (mp4, 9:16, 1080x1920, 24 to 60 fps, 3 to 90 s, H.264, AAC 48 kHz stereo). Keep text out of the Reels UI zones (top and bottom margins; check Instagram's current safe zone, unverified).
2. **`tools/reels/caption_pack.py`**: Claude writes hook, slide text, caption, alt text, hashtags and the flaw line from the listing, in Hollie's voice (`docs/video-direction.md` section 4), as schema-checked JSON. It never states a fact the listing doesn't contain. Cost is under 4 cents a reel even on Fable 5.2.
3. **Hermes `hv-reel` skill**: `/reel HV-NN` in Telegram returns the mp4, caption and alt text with Approve/Redo. Ricky or Hollie posts by hand. Builds on ideas 2, 6 and 7 in `docs/hermes-telegram-automation.md`.
4. **`tools/reels/batch.py`**: a reel queue for the 20 clothing drafts. Each one renders, or the queue lists what it is missing (most lack price and measurements).
5. **`tools/reels/ig_publish.py`**, dry-run only until Ricky makes the Meta app and token. It checks the 100-posts-a-day limit, and the first live post is a Trial Reel after Ricky approves it.
6. **Variants and results** after 10 reels: two hooks or lengths per item, with Insights numbers entered by hand.

## Ricky's decisions

- Approve the reel look from the PoC (or ask for changes).
- Update the Instagram bio (no Loveland, no rentals).
- Pick a weekly drop day and time.
- Anthropic API key in `.env.local` for the caption step (already planned in the dashboard handoff section 0).
- Real prices and measurements for the drafts, since reels show the price.
- Whether to test one paid generator (Runway Standard $12/mo, or Photoroom Max) for mood clips only.
- Later: Meta developer app and token for auto-posting; confirm @holliewoodandvine is a professional account.

## Could not verify (all lanes)

Instagram's own Reels length cap and safe zones, Meta's music rules for business accounts, whether the AI label lowers reach, Meta's own page on comment-to-DM automation, first-party ChatGPT, Photoroom Max/Ultra, Kling and Higgsfield prices, whether Photoroom's Brand Library applies to its video templates, the 4060 Ti speed of any open video model, and any Florida-specific rule. Reddit threads were behind a login wall.
