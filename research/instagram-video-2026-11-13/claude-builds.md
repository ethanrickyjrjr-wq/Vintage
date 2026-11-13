2026-11-13 | lane: claude-builds (what Claude can build itself, no paid generative-video model; posting automation; Hermes fit; cost)

# Claude-built "Just listed" reels

Bottom line: a templated Just Listed reel from 3 to 6 Photoroom stills is a solved problem with plain ffmpeg. It rendered in about 2 seconds here, costs nothing, and is deterministic. Claude's job is the words (hook, on-screen text, caption, alt text, hashtags). Posting can be a Telegram-approved manual step now, and the Graph API can be wired later once Ricky creates the Meta app (not done here).

Rules used: every external claim below is from a page crawled today with crawl4ai, quoted with its URL and raw file in `raw/`. Items I could not fetch are in "Could not verify".

## 1. Programmatic video

### Instagram / Meta Reels specs (fetched today)
Source: https://developers.facebook.com/docs/video-api/guides/reels-publishing (raw: `raw/claude-builds-meta-reels-publishing.md`). Caveat: this is Meta's Facebook Page Reels guide ("You can only publish Reels to Facebook Pages"), not the Instagram-account guide. The Instagram content-publishing page I fetched gives no video-spec table. Treat these as the best published spec and the PoC as conforming to them.
- "File Type | .mp4 (recommended)"; "Aspect Ratio | 9 x 16"; "Resolution | 1080 x 1920 pixels (recommended). Minimum is 540 x 960 pixels"; "Frame Rate | 24 to 60 frames per second"; "Duration | 3 to 90 seconds."
- Video settings: "Chroma subsampling 4:2:0", "Closed GOP (2-5 seconds)", "Compression – H.264, H.265 (VP9, AV1 are also supported)", "Fixed frame rate", "Progressive scan".
- Audio: "Audio bitrate – 128kbs+", "Channels – Stereo", "Codec – AAC Low Complexity", "Sample rate – 48kHz".
- Error text: "Reels duration must be between 3 and 90 seconds." / "Reels frame rate must be between 24 and 60 frames per second."

My PoC settings match all of these: 1080x1920, 30 fps fixed, H.264 High yuv420p, GOP 60 frames (2 s), AAC-LC stereo 48 kHz 128k, mp4 with faststart, 11.4 s.

### Tool comparison for "3 to 6 stills + title + price + link in bio"
| Tool | Verdict |
|---|---|
| **ffmpeg (zoompan, xfade, drawtext)** | Best fit. One file, no Node, no browser, 2 s render, runs on the PC, Fedora box or this cloud box. Limits: text layout is manual (pixel coordinates), no easing curves beyond expressions, drawtext has no text wrapping. Fine for a fixed template. |
| **Remotion** (React to video) | Better for rich motion and live-edited templates, but adds Node, Chromium and a React project. License, fetched today (https://www.remotion.dev/docs/license/pricing): "Remotion is completely free to use for any individual or small company - no catch." and "For individuals and companies of up to 3 people ... Free License ... Unlimited commercial use". "For bigger companies, we charge a license fee." Holliewood and Vine qualifies on the 3-person rule as I read it; the eligibility check is at https://www.remotion.dev/docs/license/faq (not fetched, see below). Use only if ffmpeg's look proves too plain. |
| **HTML/CSS/canvas + Playwright recording** | The `site/` already has this look (Bodoni, burgundy, neon). Recording means capturing frames and encoding with ffmpeg anyway; slower, timing is flaky. Only worth it to reuse site components. Not tested. |
| **MoviePy** | Python wrapper that calls ffmpeg; nice API, slower, extra dependency, nothing ffmpeg cannot do for this template. Not tested. |

Pick: ffmpeg driven by a small Python script (JSON in, mp4 out). Remotion is the upgrade path, not the start.

### Environment check
`ffmpeg 6.1.1` at /usr/bin/ffmpeg with libx264, aac, drawtext, zoompan, xfade. (Playwright's ffmpeg-1011 was not needed.)

## 2. PoC result

Files: `poc/make_poc.py` (generator), `poc/just-listed-poc.mp4` (2.87 MB), `poc/frame-1.2.png`, `poc/frame-4.5.png`, `poc/frame-8.0.png`.

Command: `python3 research/instagram-video-2026-11-13/poc/make_poc.py` (about 2.4 s wall). Inside: three `-loop 1` JPEG inputs (item 06 Starlo dress: front, back, tag from `assets/ebay-2026-11-08/ebay/`), the cream wordmark PNG from `assets/brand/`, `anullsrc` silent stereo; filter graph = burgundy `#451c2b` background, photo on a white framed panel with `zoompan` 1.0 to 1.10 over 2.6 s, `drawtext` in Bodoni Moda (title), Space Mono (subtitle, label, end card) from `assets/brand/fonts/`, neon `#ff2f92` label, cream price chip, five scenes joined with `xfade=fade` 0.4 s; encode `libx264 -profile:v high -pix_fmt yuv420p -r 30 -crf 20 -g 60 -bf 2 -movflags +faststart`, `aac 128k 48000 stereo`.

First attempt rendered only 2.7 s: single-image inputs need `-loop 1 -t` or zoompan emits one frame per image. Fixed in the script.

ffprobe (after fix):
```
video: codec_name=h264 profile=High width=1080 height=1920 pix_fmt=yuv420p avg_frame_rate=30/1
audio: codec_name=aac profile=LC sample_rate=48000 channels=2
format: duration=11.400000 size=2868668 format_name=mov,mp4,...
frames counted: 342 (= 11.4 s x 30)
```
Frames (viewed with Read):
- 1.2 s title card: cream "Holliewood & Vine" wordmark, neon Space Mono "JUST LISTED", cream "red moire pleated midi" on flat burgundy. Clean, but the lower half of the frame is empty.
- 4.5 s back photo: Bodoni title "Vintage 80s Starlo", subtitle, white panel with the dress on white, cream "$48" chip bottom right, neon "back" label. Layout is correct and legible; the Photoroom back image is a 1600x1600 square so the dress sits small inside the panel (needs a tighter crop or per-image zoom focus).
- 8.0 s tag close-up: full-bleed tag photo in the panel, Starlo label sharp, text all readable, price chip overlaps the photo corner (acceptable, could move).
Quirks: "$48" is a placeholder, no approved price exists; the neon labels render in Space Mono Bold; PoC audio is silent (music/voice must be added, see below). No typography problems found. It is a competent template, not yet polished: no hook line, no motion on text, no sell-through cue.

## 3. Claude for words (inputs: listing text; output: JSON)

Voice rules come from `docs/video-direction.md` section 4 ("How to talk"): six beats (hook under 2 s and also on screen, one fact, a taste line, proof, "One honest flaw", close), picker lines such as "I have a thing for [x], and this might be the best one I've found." and "Okay. This one.", closes "Full photos and honest condition: link in bio, piece [No.]." and "Gone." for sold; "Leave out: Visit, in store, stop by, our doors, a business location pin." The caption step should load those lines as a fixed system prompt and be given the listing title, measurements, condition notes, flaw and price, and told to invent no facts (era, maker and measurement must come from the listing text; anything else flagged "?").

One call returns: `hook` (on-screen, 6 words max), `slide_texts[]` (one per still, 4 words max), `price_line`, `close_line`, `caption` (Hollie voice, ends "Link in bio, piece No. 06."), `alt_text` (a plain description, max about 100 words), `hashtags[]` (5 to 8), `flaw_line`. A schema-validated structured output (`output_config.format`) keeps it machine-readable. Honest-flaw rule: if the listing has no flaw text, the field is empty and the draft flags it rather than inventing one.

One platform fact from the Meta page fetched today: alt text via API is image-only: "we introduced the new `alt_text` field for image posts ... Reels and stories are not supported." (https://developers.facebook.com/documentation/instagram-platform/content-publishing, raw `raw/claude-builds-graph-igLogin-publishing.md`; the other raw file is the same page). So reel alt text goes into the caption/Telegram message for hand entry.

## 4. Posting automation

Fetched today from the Instagram Platform content-publishing page (https://developers.facebook.com/documentation/instagram-platform/content-publishing):
- Scope: "publish single images, videos, reels (single media posts), or posts containing multiple images and videos (carousel posts) on Instagram professional accounts". So a personal or non-professional account cannot be automated.
- Rate limit (2026 text): "Instagram accounts are limited to 100 API-published posts within a 24-hour moving period. Carousels count as a single post." Check via `GET /<IG_ID>/content_publishing_limit`. (Far above what a shop needs.)
- Media must be public: "We cURL media used in publishing attempts, so the media must be hosted on a publicly accessible server at the time of the attempt." Reel container: "include the `media_type=REELS` parameter along with the path to the video using the `video_url` parameter."
- Flow: create container (`POST /<IG_ID>/media`), wait for it, `POST /<IG_ID>/media_publish`.
- Three variants in the doc's table: Facebook Login (host `graph.facebook.com`, token "Facebook Page access token", permissions `instagram_basic`, `instagram_content_publish`, `pages_read_engagement`), Unified Login, and **Instagram Login** (host `graph.instagram.com`, "Business Login for Instagram", "Instagram User access token", permissions `instagram_business_basic`, `instagram_business_content_publish`). The Instagram Login column lists no Page token, so a Page link is not a stated requirement for that route; but the page states Page Publishing Authorization applies to "An Instagram professional account connected to a Page that requires" it. Whether Ricky's account would need a Page link in practice: unverified.
- Resumable upload: "`upload_type=resumable` ... Only for apps that have implemented Facebook Login for Business." Host `rupload.facebook.com`. On the Instagram Login route you therefore host the mp4 at a public URL (for example a temporary signed link).
- Optional: `is_ai_generated=true` self-disclosure parameter exists (available on both login types). Trial reels (`trial_params`, `graduation_strategy` `MANUAL` or `SS_PERFORMANCE`) exist: "Trial reels are reels that are only shared to non-followers." Interesting for new-listing reach tests; not evaluated.
- Access levels: "Advanced Access / Standard Access" are both listed. What app review a single-account owner needs: not found in the fetched text, unverified.

Versus Meta Business Suite by hand: I could not fetch Meta's scheduling help page today (see below), so I make no claim about its limits. The practical comparison: API = no manual upload but needs a Meta developer app, tokens, a public host and token refresh (long-lived token upkeep); manual = Ricky uploads the mp4 and pastes the caption in the Instagram app or Business Suite, 2 minutes per reel, zero setup. Recommendation: start manual (Telegram delivers the mp4 + caption + alt text), build the API step only after 10 or so reels prove the format.

## 5. Fit with Hermes/Telegram (builds on `docs/hermes-telegram-automation.md`)

That doc ranks: 1 cut-outs back to the phone, 2 `/list` from the phone (`hv-lister` skill), 6 "New Finds" channel, 7 caption drafts. This lane extends them, not around them:
```
phone photos + one line -> Photoroom stills (already the rule) -> /list drafts eBay copy (idea 2)
-> Ricky taps Publish on eBay (his step, unchanged)
-> /reel <HV-NN> : hv-reel skill reads the listing row + the item's Drive folder
   -> Claude caption JSON (this doc, section 3) -> make_reel.py renders mp4
   -> hermes send: mp4 + caption + alt text + hashtags to Ricky's Telegram, inline "Approve / Redo"
-> Approve: manual post now (Ricky), API publish later
-> optional: same mp4 reused for the New Finds channel (idea 6)
```
Gates kept from the Hermes doc: block-send hook fails closed; pin the cron/skill model; Ricky approves before anything public. Nothing posts without his tap.

## 6. Claude API cost for the caption step

Prices below are from the claude-api skill's cached model table (cached 2026-11-03, not crawled today; skill is the source the lane brief told me to use). Assumed per reel: about 1,500 input tokens (voice prompt + listing) and 500 output tokens, no caching.
| Model | $/1M in / out | per reel |
|---|---|---|
| `claude-haiku-5-5` | $0.10 / $0.50 | about $0.0004 |
| `claude-sonnet-5-5` | $2 / $10 | about $0.008 |
| `claude-opus-5-5` | $4 / $20 | about $0.016 |
| `claude-fable-5-2` | $8 / $40 | about $0.032 (plus thinking tokens: always-on, billed as output; set `output_config.effort` low to medium) |
At 20 listings that is under 2 cents (Haiku) to under 70 cents (Fable 5.2). Cost is not a factor; choose by voice quality. Haiku 5.5 note from the skill: prices apply "for prompts up to 100K tokens". Fable 5.2 notes: omit `thinking`, no forced `tool_choice`, handle `stop_reason: "refusal"`, 30-day retention required. Prompts written for older models can be too prescriptive.

## Could not verify
- Meta Business Suite scheduling limits and steps: the URL I tried (business.facebook.com/business/help/1061359524584322) returned "That page doesn't exist". Not searched further.
- Instagram's own help page for Reels upload specs (help.instagram.com/1038071743007909): bot wall / 90-byte result. Specs above are Meta's Facebook-Page Reels page only.
- Remotion license FAQ and the "company license" employee threshold beyond "up to 3 people" on the pricing page; I did not fetch /docs/license/faq.
- Whether an Instagram Login app needs Meta app review/Advanced Access for posting to one's own account, and whether a Facebook Page link is practically required: not stated in fetched text.
- Playwright-recorded HTML and MoviePy: not tested.
- Third-party spec claims from WebSearch snippets (for example "5 to 90 seconds for Reels tab eligibility", "15 minutes"): unverified, not used.
- Model prices: from the skill's cache dated 2026-11-03, not re-crawled.
- Instagram app behaviors (music licensing for business accounts, caption length, hashtag count): not researched here.

## Build list for Fable 5.2 (`claude-fable-5-2`)

1. **make_reel.py (the template renderer)**
   - Inputs: `reel.json` (item number, title, subtitle, price, up to 6 stills in order, hook, per-slide texts, close line); the Photoroom stills; brand fonts and wordmark.
   - Output: `out/HV-NN-reel.mp4` (1080x1920, 30 fps, H.264/AAC, 8 to 15 s, under 20 MB) plus a cover PNG.
   - Files: `tools/reels/make_reel.py` (grow from `research/instagram-video-2026-11-13/poc/make_poc.py`: N scenes, auto-fit text with Pillow measuring, per-image crop/zoom focus, hook scene, end card), `tools/reels/reel.example.json`, `tools/reels/README.md`.
   - Test: render the item 06 PoC and two other items (a framed print and a pair of loafers); ffprobe must show 1080x1920, 24 to 60 fps, 3 to 90 s, yuv420p, AAC 48 kHz stereo; a script asserts this and fails otherwise; extract 3 frames and check text is inside the safe area (about 250 px top and 340 px bottom margins for Reels UI overlay, unverified, check Instagram's current safe zone).
   - Needs Ricky: nothing, except the real price and approval of the look.

2. **caption_pack.py (Claude writes the words)**
   - Inputs: listing row (title, description, measurements, flaw, price) from the eBay draft data in `tools/ebay-drafts/` or `listing.txt` in the Drive item folder; Hollie voice prompt built from `docs/video-direction.md` section 4.
   - Output: `HV-NN.reel.json` (hook, slide_texts, caption, alt_text, hashtags, flaw_line) via schema-validated structured output; flags guesses with "?".
   - Files: `tools/reels/caption_pack.py`, `tools/reels/voice-prompt.md`, `tools/reels/schema.json`.
   - Test: 5 real listings; checks pass: no banned words (visit, in store, stop by), hook 6 words or fewer, no facts absent from the listing, alt text present, "Link in bio" close present; Hollie reads 5 outputs and marks each keep or rewrite (the real voice test).
   - Needs Ricky: an Anthropic API key (already planned for the dashboard handoff section 0) in `.env.local`; Hollie's voice sign-off; an effort/model choice.

3. **hv-reel Hermes skill and Telegram approval**
   - Inputs: `/reel HV-NN` typed in Telegram.
   - Output: mp4, caption, alt text and hashtags sent to Ricky's Telegram with Approve/Redo; approved state logged to a sheet row.
   - Files: Hermes skill folder (`hv-reel`, following the layout in `docs/hermes-telegram-automation.md` idea 2), `tools/reels/run_reel.sh`, entry in the Hermes fixes list (pin the model).
   - Test: send `/reel HV-06` from the phone; get the video within 2 minutes; the fail-closed send hook still blocks anything not addressed to Ricky.
   - Needs Ricky: the PC awake and on the network; confirmation Hermes can send video files to Telegram (not checked here).

4. **Batch and cover-frame tools**
   - Inputs: a folder of Drive item folders (`G:\My Drive\Holliewood eBay\Items\<NN slug>`).
   - Output: `reel-queue/` with an mp4 + caption + cover PNG per item that has 3 or more Photoroom stills and a `listing.txt`; a `queue.csv` with status (draft, approved, posted).
   - Files: `tools/reels/batch.py`, `tools/reels/queue.csv` schema.
   - Test: run on the 20 clothing items (`HWV-01` to `HWV-20` drafts) without any public action; count that every item either renders or lists the missing input.
   - Needs Ricky: the real prices and measurements (the drafts are missing them); nothing is posted.

5. **Optional later: Graph API publisher (draft code only until credentials exist)**
   - Inputs: approved mp4 + caption from the queue, a public URL for the mp4, an Instagram User access token.
   - Output: container id, publish id and permalink recorded in `queue.csv`; checks `content_publishing_limit` first.
   - Files: `tools/reels/ig_publish.py` (stdlib or `requests`; `--dry-run` prints the exact requests; never runs without `--confirm`), `docs/instagram-api-setup.md` (step card for Ricky).
   - Test: `--dry-run` produces the requests matching the docs quoted above; the real test is one trial reel (`trial_params` MANUAL) published after Ricky approves.
   - Needs Ricky: a professional Instagram account (confirm @holliewoodandvine type), a Meta developer app with the Instagram Login product, token generation, a decision on whether a Facebook Page link is wanted, and the first live post approval. Claude does not create the app or tokens.

6. **Reel variants and measurement (after 10 reels)**
   - Inputs: the queue plus Instagram Insights numbers Ricky or Hollie copy into the sheet.
   - Output: a weekly line "which hook and length held people", feeding the talking-versus-silent test in `docs/video-direction.md`.
   - Files: `tools/reels/variants.py` (A/B hooks, 9 s vs 15 s cuts from the same JSON), `docs/reel-results.md`.
   - Test: two variants of the same item render and differ only in hook and length.
   - Needs Ricky or Hollie: posting both and entering the numbers by hand.
