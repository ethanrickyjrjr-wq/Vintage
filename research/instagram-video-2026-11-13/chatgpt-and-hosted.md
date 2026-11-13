2026-11-13 | Lane: chatgpt-and-hosted | Holliewood and Vine, Instagram video for new listings
Raw crawls (crawl4ai, fetched 2026-11-13): `research/instagram-video-2026-11-13/raw/lane-chatgpt-and-hosted-*.md`. Nothing signed up, signed in or bought.

## Headline
1. **Sora is gone.** ChatGPT has no first-party video generator I could find. "The Sora web and app experiences were discontinued on April 26, 2026. The Sora API was discontinued on September 24, 2026." (https://openai.com/sora/ redirected to https://help.openai.com/en/articles/20001152 "What to know about the Sora discontinuation", updated 7 days ago). So "what can ChatGPT create" for this job = images, text, plans, not video clips.
2. ChatGPT's useful lane is **stills and words**: price/title cards, cover frames, captions, scripts. Not animating a real garment.
3. For clips from a product still, **Runway, Luma, Pika, CapCut/Seedance, Gemini Omni, Kling, Canva** all offer image-to-video (details below). I found **no independent test** of text/pattern warping for any of them (see "could not verify").

## 1. ChatGPT, Nov 2026

**Image model.** OpenAI's own page: "April 21, 2026 ... Introducing ChatGPT Images 2.0 ... This post introduced ChatGPT Images 2.0. For the latest image experience: Learn about ChatGPT Images 2.5" (https://openai.com/index/introducing-chatgpt-images-2-5/ is the linked page; it returned a bot wall, so 2.5 details are unread from OpenAI). API model card: `GPT-Image-2`, snapshot `gpt-image-2-2026-04-21`, "state-of-the-art image generation model for fast, high-quality image generation and editing. It supports flexible image sizes and high-fidelity image inputs" (https://platform.openai.com/docs/models/gpt-image-2).
Newer names are third-party only: PhotoWorkout (hands-on test run Nov 7): "the company released Images 2.6 on November 4, promising faster generation, more consistent edits, animated GIFs and SVG export" (https://www.photoworkout.com/?p=223762). Artlist (updated Nov 8): 2.6 Flare/Sunburst, aspect ratios "16:9, 9:16, 1:1 ...", "Up to 16 reference images in one edit", 2.6 GIF is 400px, 2 to 12 frames (https://help.artlist.io/hc/en-us/articles/39018863931165-GPT-Image-2-Family). Whether ChatGPT itself shows "2.6" is unverified.

**Edit an uploaded photo: yes.** chatgpt.com/images accepts ".avif, .bmp, .gif, .heic, .heif, .jpeg, .jpg, .png, .webp" uploads (https://chatgpt.com/images/). But PhotoWorkout's real-photo test is a warning for listings: "The handwritten note ... came back as Fresh Hall, Seeding Sampaign ... The model was told not to change anything else, and it rewrote the text anyway ... the binder clip changed shape." Faces/relighting held well. So edits can silently change small details of a real item.

**Text rendering (price cards): strong.** PhotoWorkout: "Text rendering was flawless: a 29-string camera settings cheat sheet came back with zero errors, from both 2.6 and 2.5." Artlist: text "the model's standout strength". Good for price/measurement cards made from scratch (always proofread).

**Video / animate a photo in ChatGPT.** None found. PhotoWorkout: "Asked to animate a real photo, ChatGPT instead pasted AI-drawn leaves over the untouched original with code." The GIF feature (cartoons drawn frame by frame) is not Reels-grade.

**Provenance.** PhotoWorkout citing the system card: "images carry C2PA provenance metadata plus Google DeepMind's SynthID invisible watermark." (Unusual pairing; treat as reported, not confirmed from OpenAI.) Sora's watermark/cameo rules are moot, product discontinued.

**Plans (first-party page lost the prices in the crawl).** https://openai.com/chatgpt/pricing/ lists tiers Free / Go / Plus / Pro / Business / Enterprise. Image lines: Free "Limited image creation"; Go "More image creation"; Plus "More complex and accurate image creation"; Pro "Unlimited and faster image creation". The comparison table has "Image generation with Thinking": No for Free and Go, Yes for Plus and Pro. Dollar amounts are blank in the crawl. Web search snippets (unverified, third-party): Plus $20/mo, Go about $8/mo (one outlier $5.50, "may include ads" is confirmed on the page), Pro tiers $100/$200 (maybe $500), Business about $25/user.

**Agent that posts to Instagram.** Not found. Pro lists "Dot, your always-on agent" and plugins/connected apps exist (https://help.openai.com/en/articles/20001256, example app "such as Slack"). No Instagram connector confirmed. Also: new custom GPT creation is closed on personal plans (https://help.openai.com/en/articles/8554407).

**Commercial rights.** OpenAI Terms of Use: "you (a) retain your ownership rights in Input and (b) own the Output. We hereby assign to you all our right, title, and interest, if any, in and to Output." Also "output may not be unique and other users may receive similar output", and you may not "Represent that Output was human-generated when it was not." (https://openai.com/policies/terms-of-use/). Consumer data may train models unless you opt out.

## 2. Hosted alternatives (all fetched today)

| Tool | Image-to-video | Cost | Length | Watermark / commercial |
|---|---|---|---|---|
| **Runway** (https://runwayml.com/pricing) | Yes (credits per model) | Free 125 one-time credits; Standard $12/mo yearly ($15 monthly), 625 credits = "52s of Gen-4.5"; Pro $28 yearly/$35, 2,250 credits; Max $76/$95. Gen-4.5 60 credits per 5s; Kling 4.0 89 credits/5s (25% off to Nov 30); Seedance 2.0 Pro 160 credits/4s | 5s units | Standard lists "No watermarks"; free tier watermark not stated on page; commercial terms unread |
| **Luma** (https://lumalabs.ai/pricing) | Yes ("Text-to-Video Image-to-Video", Ray3.2) | Plus $30/mo, 10,000 credits, lists "Commercial use"; Pro $90; Ultra $300. 720p 100 credits/5s, 1080p 400 credits/5s | 5s or 10s | Free tier not shown |
| **Pika** (https://pika.art/pricing) | Yes (many models, incl. "GPT Image 2.6" for stills) | Starter $10/mo 600 credits; Creator $35; Fancy $95 | not stated | Free: "No watermark", but "Not included: Commercial license"; Starter and up: "Commercial license" |
| **CapCut** (https://www.capcut.com/pricing) | Seedance 2.5 / 2.0 Mini (image-input not confirmed on this page) | Pro $19.99/mo, 1200 credits; Seedance 2.5 "from $0.12/sec (first month)"; Ultra $79 | per-second billing | not stated |
| **Gemini Omni (replaces Veo in the Gemini app)** (https://gemini.google/overview/video-generation/) | Yes: "Turn photos into a video (up to 5)", "Create 10 second videos" | AI Plus $4.99/mo, AI Pro $19.99/mo, Ultra $99.99 or $199.99 (https://gemini.google/subscriptions/); Flow credits 200 / 1,000 / 10,000 or 25,000. Pro page says "limited trial of Veo 3.1 Lite"; Omni by plan unclear | 10s | "all videos generated in the Gemini app are embedded with SynthID" (invisible). Commercial terms unread |
| **Canva** (https://www.canva.com/pricing/, https://www.canva.com/features/ai-video-generator/) | "Image to Video" is a Premium AI tool; clip generator "powered by Google's Veo-3" is text prompt, "16:9 video for up to eight seconds" | Pro US$144/yr; Business US$250/yr; Free has "Limited access" | 8s, 16:9 only per page (not 9:16) | "Pro, Business ... users can use ... a limited number of cinematic video clips per month"; "you may not have exclusive rights" to AI output |
| **Kling** (https://klingai.com/) | Kling 4.0 exists; pricing page blocked; Runway sells it at 89 credits/5s | unverified direct | unverified | unverified |
| **Higgsfield** (https://higgsfield.ai/pricing) | page rendered empty | unverified | unverified | unverified |

## 3. Keeping the real item unchanged
No tool page I fetched documents a "first frame lock" or "product consistency" guarantee that I could quote. Best-supported facts:
- Gemini Omni lets you give up to 5 photos as references (above). Artlist says GPT-Image-2.6 takes up to 16 references, but that is stills.
- The only e-commerce advice found (web search summary, vendor blogs, unverified): animate the approved product image, tell the model to preserve logo/stitching/sole/colors and "No new objects or text". Same search: "I found no independent, controlled test that compares logo and text warping across Kling, Runway, Veo, and Luma". One source said Pika, Luma and Firefly did better at text-to-video than image-to-video (single source).
- The only quoted evidence of an AI tool altering a real item is the GPT-Image edit above (rewritten handwriting, reshaped clip). Assume any generative step can change labels, prints, hardware and weave.

## Could not verify
- ChatGPT dollar prices from OpenAI (blank in crawl); Images 2.5/2.6 on OpenAI's site; help.openai.com usage-limits and release-notes pages (bot wall).
- Any ChatGPT video or Instagram-posting agent (searched, none).
- Kling and Higgsfield pricing; watermark on free tiers for Runway, Luma, Canva, CapCut; max length for Pika; commercial terms for Runway, Kling, Gemini.
- Whether Omni is included in Plus/Pro or only Ultra; Gemini API video prices (repo file `research/ai.google.dev_gemini_api_docs_pricing-20261030T123651Z.md` has no Veo/Omni per-second table in its first lines; not read fully).
- Any independent text/pattern-warp comparison.

## Recommendation (ranked)
1. **ChatGPT (Plus or even Free/Go): stills and copy only.** Price/measurement cards, title frames, caption and hashtag drafts, shot-list scripts. Cheap; Terms give Hollie the output. Do not let it "touch up" the garment photo (documented detail drift); never use for the product itself.
2. **Primary video method for listings: real footage plus Photoroom stills, edited in CapCut or Canva (non-generative).** Keeps the item true, which matters for returns and eBay buyers. (Editing features themselves not tested this lane.)
3. **If one paid generator is wanted: Runway Standard ($12/mo yearly)** for mood/brand clips and image-to-video: lists all models, "No watermarks", 5 parallel gens, small credit use, 52s of Gen-4.5 a month. Runner-up: Pika Starter $10 (commercial license explicit) or Gemini AI Pro $19.99 if she wants the Google Omni photo-reference route (up to 5 photos) plus the rest of Google. Test with 3 real items first and compare labels, prints, buttons frame by frame before paying a year.
4. **Avoid:** paying for ChatGPT Pro for video (no video exists); Canva's AI clip generator for product listings (text-prompt, 16:9, non-exclusive rights); any AI clip showing a listed garment as if it were the actual item; Sora (discontinued); trusting vendor blogs on "consistency".
