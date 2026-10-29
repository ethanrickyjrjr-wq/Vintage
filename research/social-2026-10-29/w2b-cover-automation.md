# w2b-cover-automation: how to automate covers and the best-frame pick (stage `cover`)

Lane w2b, written and tested 2026-10-29. All pages accessed 2026-10-29. Raw captures: `research/social-2026-10-29/raw/w2b-*.md`. Test files and outputs: `research/social-2026-10-29/raw/w2b-test/` and the one required PNG `research/social-2026-10-29/raw/w2b-test-cover.png`.

Tags: `verified` (read on the live vendor page via crawl4ai this session), `WebFetch summary` (live page read, but summarised by a small model; numbers not re-read), `vendor claim`, `tested` (my own run this session, hardware named), `unverified (snippet)`, `inferred`. Hours are `inferred` estimates.

## TL;DR

1. **Winner for type and layout control: one HTML template rendered by Playwright/Chromium.** `tested` on the Fedora box: two PNGs (1080x1920 reel cover and 1000x1500 Pin) from one `cover.html` in 1.7 s wall, $0, no sudo, Chromium already cached there. Bodoni Moda 700 with `opsz` pinned to 12 keeps its hairlines; text is crisp at 1:1.
2. **Satori and @vercel/og are the stack-native second place, not the first.** Satori renders a variable font as its default instance (README `verified`; my render showed the lighter, wider default cut), so Bodoni Moda 700 must be pre-instanced to a static TTF with fonttools (0.87 s, `tested`). Satori exposes no layout readback (grep of README, `verified`), so the safe-zone gate for approve-by-exception would live elsewhere.
3. **A blurred box-shadow nearly broke the Edge budget.** The same cover cost 1.7-2.3 s in resvg with the 60 px shadow and 0.29-0.37 s without it (`tested`). Supabase Edge Functions allow 2 s CPU per request (`verified`). Real Edge Runtime timing is unmeasured.
4. **Vercel Hobby is "personal, non-commercial use only"** (`verified`, fair-use page). A render endpoint for a shop on Vercel needs Pro, $20/mo (WebFetch summary).
5. **Template SaaS all fit about 60 renders a month** (Placid Basic $19/mo, Bannerbear Automate $49/mo, Creatomate Essential $45/mo annual-billed, APITemplate Starter $35/mo monthly). None is verified to pin `opsz`; spend the free trial credits on this lane's test cover before paying anyone.
6. **Canva autofill is open to Pro now**: "available when your app acts on behalf of a user on Canva Pro ... Teams, or Enterprise" (`verified`, canva.dev). That corrects the "Enterprise only" idea. It still means building an OAuth integration, and autofill only fills named fields.
7. **Best frame: two stages.** A cheap filter (ffmpeg `blurdetect` plus a Pillow Laplacian, 48 frames in 0.22 s, `tested`) removes blur. It does not know what a good cover is. A vision model or a human then picks from a top-6 contact sheet.
8. **A vision pick costs under a cent.** Image cost is `ceil(w/28) x ceil(h/28)` tokens (`verified`); 12 frames at 540x960 is about 8,400 tokens: about $0.0008 on Haiku 5.5 ($0.10/MTok in) or about $0.017 on Sonnet 5.5 ($2/MTok in), arithmetic `inferred`.
9. **Fonts are clear for graphics**: the three OFL.txt files declare no Reserved Font Name (0 hits, `tested` grep), and artwork made with OFL fonts is not bound by the OFL (FAQ 1.1.1, 1.13, `verified`).
10. **Two w1e spec points surfaced, not fixed** (section 7): template 1's top label sits outside the hard-safe square, and the vertical stack is tight.

## 1. The throwaway test (exact commands, times, verdict)

Where: Fedora box, `~/social-lab/w2b/` (plus `~/social-lab/w2b-deno/`, outside the lane folder only because a parent `package.json` made Deno switch to node_modules mode). CPU: i7-8565U, 8 threads. Everything user-local, no sudo. Both directories are deleted at the end of this lane (npm and Deno caches remain in `~/.npm` and `~/.cache/deno`).

| Step | Command (abridged) | Result |
|---|---|---|
| Fonts | `curl -sfL -o fonts/BodoniModa-VF.ttf "https://raw.githubusercontent.com/google/fonts/main/ofl/bodonimoda/BodoniModa%5Bopsz%2Cwght%5D.ttf"`, same for `dmsans/DMSans[opsz,wght].ttf` and `spacemono/SpaceMono-{Regular,Bold}.ttf`, plus each `OFL.txt` | Bodoni Moda axes wght 400-900 (default 400), opsz 6-96 (default 11); DM Sans opsz 9-40 (default 9), wght 100-1000. Both have GPOS kerning. `tested` |
| Python tools | `python3 -m venv .venv && .venv/bin/pip install -q fonttools brotli` | 10.5 s |
| Static instances | `fonttools varLib.instancer fonts/BodoniModa-VF.ttf wght=700 opsz=12 -o fonts/BodoniModa-700-o12.ttf` (and DM Sans `wght=600 opsz=14`) | 0.87 s for both; 58.9 KB and 56.8 KB |
| Node deps | `npm init -y && npm i playwright-core satori @resvg/resvg-js` | 6.5 s; playwright-core 1.64.1, satori 0.63.2, resvg-js 2.6.2 |
| Photo | `site/assets/photos/IMG_6616.webp` (the real urn-lamp photograph, 2048x2731) converted to JPEG with system Pillow 12.1.0 | real photo only, no cutout |
| **HTML to PNG** | `node render.mjs` (playwright-core driving the already cached `chrome-headless-shell`, Chrome for Testing 153.0.8010.12, `--font-render-hinting=none`) | **launch 155 ms; reel 914 ms (cold); Pin 302 ms; `time` real 1.709 s** for both files |
| Satori | `node satori.mjs` | satori() 62-125 ms; resvg 288-370 ms **without** the shadow, 1,695-2,269 ms **with** the 60 px blurred shadow; total 0.35-0.43 s vs 1.8-2.4 s |
| @vercel/og under Deno 2.9.6 | `deno run -A og.tsx` (imports `npm:@vercel/og@^0`, `npm:react@^19`, exactly the Supabase doc example's specifiers) | **text-only cover, no photo, no shadow**: 303 ms first, 183 ms warm; whole command 3.9 s first run (npm fetch), 0.51 s cached. Do not compare with the full-cover timings above |

The template is w1e template 1 (Drop day): ground `#451c2b` with a radial vignette to `#321520`, white frame x 237-843, y 430-1240 with 28 px mat and `0 24px 60px rgba(0,0,0,.45)` shadow, "Open." Bodoni Moda 700 168 px cream, DM Sans 600 44 px caps tracking 0.08em in pink `#e5a6b4`. **It is a test render. Template 1 stays unposted until real stock exists (w1e gate).**

**Is text rendering crisp? Yes, both ways.** Chromium and Satori are both anti-aliased and sharp at 1:1; the thin serifs of Bodoni Moda 700 at opsz 12 survive (zoom crop `raw/w2b-test/zoom-type.png`). After one `boxSizing: 'border-box'` fix, Satori matched Chromium closely: mean absolute luminance difference 2.33 of 255, 12,576 of 2.07M pixels differing by more than 40 (edges and photo resampling). The Satori gotcha: without `boxSizing: 'border-box'` the frame grew by its 56 px of padding and "Open." collided with it. At a 129 px profile-grid tile the 168 px display "Open." is readable and the 44 px labels are not (`raw/w2b-test/grid-thumbs.png`), which confirms w1e's rule that labels are decoration only. `tested`.

**One template file, several formats.** `cover.html` takes `?fmt=reel|pin&head=...&top=...&bot=...&photo=...`, switches a CSS block per format, and the same script wrote both sizes (Pin has its own layout block, as w1e requires, not a crop). The Instagram grid-crop preview is a Pillow crop (y 240-1680 of the master, `vendor claim` from w1e), downsampled to 129 and 185 px. A 2160x3840 YouTube master needs scale 2: Remotion `renderStill` has a `scale` option (`verified`), Playwright `deviceScaleFactor: 2` is `inferred` and not run.

## 2. Options: code-rendered

| Option | Stage | Price | Drivable by Claude/Codex | Setup | Control over type and layout | Stack fit | Wins when |
|---|---|---|---|---|---|---|---|
| **Playwright + Chromium, HTML template** (playwright-core 1.64.1, Apache-2.0, 98.8k stars, pushed 2026-10-29) | cover | $0 | CLI/script, yes | 4-6 h for one layout, 6-8 h for all six (`inferred`) | Highest: real CSS, `font-variation-settings`, `text-wrap`, variable fonts, browser preview, `getBoundingClientRect` for the QA gate | TypeScript; runs on Fedora (tested) or Windows (Chrome exists; Playwright is already in `crawl4ai-venv`, not used). Not a Vercel or Supabase Edge runtime. Supabase's own docs list "Taking Screenshots with Puppeteer" via Browserless.io (nav listing `verified`, page not read) | You want the closest thing to the website's own rendering and a mechanical gate |
| **Satori + resvg-js** (satori 0.63.2, MPL-2.0, 14.1k stars, pushed 2026-10-23; resvg-js 2.6.2, MPL-2.0, 2.0k stars, last push 2026-06-30) | cover | $0 | CLI/script, yes | 6-8 h | Flexbox/Grid subset (README `verified`), variable fonts = default instance only, `font-feature-settings` via HarfBuzz, no layout readback; `debug: true` only draws boxes | Pure JS, no browser, deploys anywhere | You must render inside a serverless function with no browser |
| **@vercel/og 1.0.3** (MPL-2.0; wraps Satori + resvg) | cover | $0 library; **Vercel Pro $20/mo** to host commercially (Hobby is non-commercial, `verified`) | URL endpoint, yes | 6-8 h | Same as Satori; docs say TTF/OTF/WOFF only, no `display: grid`, 500 KB bundle incl. fonts and images (page updated June 16, 2026) | Closest to the stated stack (React, Vercel). Works in Deno via `npm:` specifier (tested) | The covers must be fetchable by URL from the site or a scheduler |
| **Satori inside a Supabase Edge Function** (Supabase doc example `verified`) | cover | Supabase plan price not read | URL endpoint, yes | 6-8 h | As above | Deno-style imports (global rule 6). Limits `verified`: 2 s CPU, 256 MB, 20 MB function size (CLI-bundled) | Everything already lives in Supabase, and shadows are baked or removed |
| **Remotion `renderStill`** (remotion 4.0.539, source-available, GitHub licence NOASSERTION, 68.8k stars, pushed 2026-10-29) | cover (and video, w2a) | **Free for individuals and companies of up to 3 people** (`verified`); the $0.01-per-render "Automators" tier is for products that build video tools (`inferred`: not us) | CLI/API, yes | 6-10 h; not run by me | Chromium underneath, so browser-grade type; React components | React 19 fits; one component set can make stills and video end cards | w2a picks Remotion for video anyway: one design source for both |
| **Pillow / ImageMagick** (Pillow 12.1.0 and `magick` on Fedora) | cover QA | $0 | yes | 1-2 h | Weakest for type: not tested for variable-axis pinning; use a fonttools static instance. Good at crops, thumbnails, contact sheets, composites (all used in the test) | any | Post-processing: grid preview, 129 px legibility check, contrast |

**Font licence (verified).** OFL FAQ 1.1.1: a graphic made with an OFL font does not restrict the artwork; 1.13: embedding does not alter the document's licence. Reserved Font Name: 0 matches of "with Reserved Font Name" in the Bodoni Moda, DM Sans and Space Mono `OFL.txt` (`tested`), so a fonttools instance can keep the family name; keep each `OFL.txt` beside any file you redistribute. Woff2 versions already ship in `site/assets/fonts/` (Bodoni Moda latin variable, DM Sans, Space Mono, Courier Prime); the renderer needs the full TTFs from `google/fonts`, because the site files are latin subsets (`inferred`, not opened).

**Doc conflict (X verified, Y need review).** Satori README: four formats incl. WOFF2, Grid via Taffy. @vercel/og docs (updated June 16, 2026): no WOFF2, grid "will not work". Both read live. Wrapper lag is plausible; test grid and WOFF2 in the actual `@vercel/og` version before relying on either. The site ships woff2 only.

## 3. Options: template SaaS (price at about 60 renders a month)

Load definition (BRIEF2 reference load): 5 IG/FB posts + 3 TikToks + 3 Pins a week is about 47 posts a month. With re-renders and the odd 4:5 or 2x variant, size for **about 60 renders a month**. Credits below are per image render unless stated.

| Tool | Plan and price (period) | Credits vs 60 renders | Drive | Notes | Source and tag |
|---|---|---|---|---|---|
| Canva Pro | US$144 per year (annual-billed; monthly not read), 5 Brand Kits | n/a (manual) | GUI; Connect API autofill: Pro/Teams/Enterprise, 60 requests per minute per user; official AI Connector for Claude exists but tool list not read | Autofill fills named fields in a brand template only; no layout logic; OAuth integration to build | `verified` canva.dev autofill page; price from w1e S21; connector `unverified (snippet)` |
| Placid | Basic $19/mo (500 credits/mo), Pro $39/mo (2,500); page toggle "Monthly / Yearly (save 2 months)", which toggle was captured is **billing period not confirmed** | 60 of 500 | REST, URL API, MCP (page `verified`) | 1 image = 1 credit; previews free and watermarked; unused credits roll over | `verified` placid.app/pricing |
| Bannerbear | Automate $49/mo, 1,000 API credits and 200 AI credits (annual toggle not read); Scale $149/mo | 60 of 1,000; credits multiply by formats and scale (jpg+png at scale 2 = 4) | REST, MCP ("Claude, ChatGPT or Codex" named), Instant URLs | Trial: 30 credits, no card | `verified` bannerbear.com/pricing |
| Creatomate | Essential $45/mo **billed annually** ($540 a year), 2,000 credits; monthly price not read | 60 of 2,000; 1 image = 1 credit | REST; official MCP page exists, `codex mcp add creatomate --url https://api.creatomate.com/mcp` (snippet); image tool in the MCP not confirmed | Trial: 50 credits | price `verified`; MCP `unverified (snippet)` |
| APITemplate.io | Free $0, 50 images/mo (**below the load**); Image+PDF Starter "$29$35/month" for 1,500 (reading: $29 annual-billed, $35 monthly, `inferred`) | 60 of 1,500 | REST, no-code | Drag-drop editor, no HTML/CSS needed | `verified` apitemplate.io/pricing |
| Cloudinary | Free $0, 25 credits/mo; Plus $99/mo ($89 annual-billed), 225 credits; Advanced $249/mo ($224) | credit-to-render ratio not read | REST/SDK; MCP not checked | Text overlay with an uploaded custom font not verified | WebFetch summary, cloudinary.com/pricing |
| Figma | price not read | n/a | Figma remote MCP can write to the canvas (beta, free during beta, needs a Full seat; sources disagree on the plan) | A design and review surface, not a cover renderer | `unverified (snippet)` |

**What SaaS cannot be trusted with yet.** w1e's hairline rule (Bodoni 700, `opsz` pinned at 12) is not something these editors are documented to do. A static instance (section 1) uploaded as a custom font is the workaround; whether each tool accepts it is unread. Run the trial credits on `cover.html`'s design first and judge the zoomed "Open." against `raw/w2b-test/zoom-type.png`.

## 4. Best-frame pick from a video

Test clip: `site/assets/walkthrough.mp4`, 24.2 s, H.264, **320x568** (a preview file, not phone footage). Frames at 2 fps (48) by local ffmpeg 8.1.2 (0.195 s). Scoring: ffmpeg `blurdetect` + `signalstats` in one pass (0.23 s), and a Pillow-only 3x3 Laplacian variance, mean luma and clipped-pixel shares on Fedora (0.22 s for 48 frames, 5 ms each, `tested`; script `raw/w2b-test/score.py`). Contact sheet of best and worst: `raw/w2b-test/frames-top-vs-worst.png`.

| Method | What it does | Result on this clip | Cost and driveability |
|---|---|---|---|
| ffmpeg `thumbnail` | picks the most "typical" frame by histogram | picked about t = 9.0 s, mid-rank on sharpness: not a quality filter | $0, CLI |
| ffmpeg `blurdetect` | blur width per frame (lower = sharper), in ffmpeg 8.1.2 (`-h filter=blurdetect` `verified`) | best t = 18.0 s (5.31); worst 7.3 | $0, CLI, drops into the same pass as `signalstats` |
| Pillow Laplacian variance | sharpness proxy, centre 80% | best t = 18.0 s (160), then 18.5, 5.5, 17.5, 0.0; worst 21.5, 22.0 (blurred wall pans) | $0, CPU, no numpy or OpenCV needed |
| Agreement | Spearman rank (Laplacian vs -blur) | **0.52**: moderate; both pick t = 18.0 s | |
| Exposure gate (mean luma 70-180, under 5% pixels at 250+, under 10% at 5 or less) | rejects dark or clipped | **48 of 48 passed**: no discrimination here. Neon and glass highlights will trip the 250+ check, so tune on real footage | $0 |
| Vision model on a top-6 sheet | judges subject, framing, "would this sell" | not run via API; I read my own sheet and the top row was clearly sharper and better composed than the bottom | Claude Code reads the sheet itself (no extra API spend, `inferred`); API: tokens `ceil(w/28) x ceil(h/28)` (`verified`), Haiku 5.5 $0.10/MTok in and $0.50 out, Sonnet 5.5 $2 and $10 (WebFetch summary of the pricing page, rows also read in the saved text) |
| CLIP aesthetic score (improved-aesthetic-predictor, Apache-2.0, 1.3k stars, last push 2024-07-01) | LAION-trained "looks nice" score | not run | Needs torch plus CLIP ViT-L/14; Fedora Python 3.14 wheels are the same trap the cutout handoff hit (`inferred`). Scores photo beauty, not "sells this lamp" |

**Honest limits.** Laplacian variance rewards texture: it ranked busy racks and the rug first and put bare burgundy wall (a clean negative-space shot) at the bottom, so it drops blur well and picks subject badly. The clip is tiny and the walkthrough is slow pans; phone footage with 4K detail, neon, brass glints and glass will behave differently. So: **stage 1** ffmpeg or Pillow drops frames below a sharpness floor and bad exposure; **stage 2** a vision model, given the listing title and "pick the frame that shows the whole piece, uncluttered, not clipped", chooses from six; **stage 3** a human taps. For a one-piece reveal the better answer is often not a frame at all: shoot a deliberate still, which is also what w1e's "real photo of the real piece" rule favours.

## 5. Photo rules for automated covers (constraints, not options)

- **Selling covers use the original real photograph**, framed (w1e templates 1-4, 6). `site/assets/editorial/` cutouts contain generated pixels (docs: the urn lamp's shade top was "completed", the disco ball is fully generated) and are banned from covers that sell a piece.
- **Mask-only cutouts from `tools/cutout/cutout.py` are real pixels** (rembg pinned to `birefnet-general`, MIT weights; it reports "pixels kept", below 99% means check by eye). They may appear on a cover, with the proof logged. Glass is not cut (handoff section 5): chandelier, stemware, decanter use the original.
- **Blind `object-fit: cover` cropped the lamp photo** so the wall switch, a hanger and the Elvis frame all ended up in the cover (see the test PNG). Real automation needs a per-listing focal box. The cutout tool's alpha bounding box can supply it even when the original is shown; otherwise Claude proposes a crop box from viewing the photo and a human confirms.
- No price, discount, "visit" or claim text on any cover (BRIEF). Templates 1 and 2 stay unposted until real stock exists. The test cover is illustration only.

## 6. Recommendation for Holliewood & Vine

| Tier | What | Human must still |
|---|---|---|
| (a) free, native | In-app cover picker or Canva Free by hand; alt text on every post. The test cover already shows the target look | choose every cover and approve every post |
| (b) one paid tool | **Placid Basic $19/mo** (cheapest API + MCP + editor) or **Canva Pro US$144/yr** if Hollie wants to design by hand. Buy only after the trial renders Bodoni at `opsz` 12 as well as `zoom-type.png` does | pick photo and one line; Hollie adjusts in the editor |
| (c) Claude + Codex | `cover.html` (all six templates as CSS blocks, props JSON) rendered by **Playwright on the Fedora box** (Codex CLI 0.160.1 is already installed there, `npm ls -g` `tested`), Pillow for grid preview and 129 px check, frame pick as above. Hosted-URL variant only if a scheduler needs a link: @vercel/og on Vercel Pro $20/mo, or Supabase Edge with no blur shadows | approve-everything: a human reviews each render. Approve-by-exception: auto-send only when the gate passes |

**Approve-by-exception gate (Playwright only).** In the same run read `getBoundingClientRect` or Range rects of every text and frame element and assert: inside the surface's safe box (x 90-990, y 420-1500 for the hard-safe square; 3:4 crop y 240-1680), no overlaps, minimum font size per w1e, contrast from the CSS colors (w1e's ratios), the photo path points at a listed real item, and no banned words. Everything else, prices, condition, provenance, anything about a person, always goes to a human. Satori offers no readback, so choosing Satori means the gate needs Playwright anyway.

**Mode A vs B per stage.** Render: safe in B. Frame pick: B only if the vision pick agrees with the sharpness top-3, else human. Copy on the cover: human, always. Phone approval: the repo's existing "draft out, Ricky taps Publish" pattern; push or email costs $0 (w2g/w2c own the transport).

## 7. X verified, Y need review

- Canva Autofill: Pro/Teams/Enterprise `verified`; earlier "Enterprise only" idea superseded.
- Satori README (WOFF2, Grid) vs @vercel/og docs (no WOFF2, no grid): both `verified`, conflict unresolved.
- Real Supabase Edge Runtime CPU for a Satori cover: unmeasured (Deno on Fedora is not the Edge Runtime).
- Vercel Pro "$20/mo": WebFetch summary; whether $20 is per seat or base unclear.
- Placid and Creatomate billing toggles; APITemplate "$29$35" reading; Cloudinary credit-to-render ratio.
- **w1e template 1 spec**: the top label at y 330-375 sits outside w1e's own hard-safe square (y 420-1500). It survives the 3:4 grid crop (y 240-1680) and the 4:5 crop (y 285-1635), but a square TikTok crop would cut it. In my render "Open." cap tops start about 15 px under the frame's bottom edge and the "p" descender ends about 20 px above the "HERE, THEN GONE" label. Both are eyeballed from the PNG; I did not edit the spec.
- Tests ran on the Fedora CPU, not the Windows PC and not on Vercel.

## 8. Decision matrix

| Option | Stage | Cost per month at 60 renders | Setup hours (`inferred`) | Claude/Codex drivable | Ban/ToS risk | Approval-mode fit |
|---|---|---|---|---|---|---|
| Native picker / Canva Free | cover | $0 | 0.5 | No (GUI) | none | A only |
| Canva Pro by hand | cover | US$144 a year (about $12/mo, annual-billed) | 1 | GUI only | none | A only |
| Canva Connect autofill | cover | same Pro fee | 10-16 | REST + OAuth | none | A; B needs an extra gate |
| **Playwright HTML on Fedora** | cover, QA | **$0** | **4-6 (one template), 6-8 (six)** | **yes** | none | **A and B** |
| Satori (Node, Fedora) | cover | $0 | 6-8 | yes | none | A; B needs Playwright gate |
| @vercel/og on Vercel | cover | $20 (Pro) | 6-8 | URL endpoint | Hobby is non-commercial | A; B partial |
| Satori in Supabase Edge | cover | plan price not read | 6-8 | URL endpoint | none | A; B partial; 2 s CPU risk |
| Remotion `renderStill` | cover (+video) | $0 under 3 people | 6-10 | yes | licence terms: re-read if the company grows | A and B |
| Placid Basic | cover | $19 | 3-5 | REST, URL, MCP | none | A, B |
| Bannerbear Automate | cover | $49 | 3-5 | REST, MCP | none | A, B |
| Creatomate Essential | cover | $45 (annual-billed) | 3-5 | REST, MCP (image tool unconfirmed) | none | A, B |
| APITemplate.io Starter | cover | $35 monthly ($29 annual-billed, reading) | 3-5 | REST | none | A, B |
| Cloudinary Plus | cover | $99 ($89 annual-billed) | 5+ | REST/SDK | none | A, B |
| ffmpeg + Pillow frame filter | edit to cover | $0 | 1-2 | yes | none | B for filtering |
| Vision pick (Claude Code or Haiku 5.5) | cover | about $0.001-0.02 per pick | 1 | yes | none | A; B with agreement rule |

## 9. Build effort

Claude Code plus Codex: **about 8-12 hours** to wire the recommended path: six template CSS blocks and one props schema (1.5-2 h each pair of formats to calibrate against w1e), `render.mjs` loop with the bounding-box and contrast gate (2 h), Pillow grid-crop and 129/185 px preview (1 h), frame-pick script plus contact sheet (1-2 h), focal-box input per listing (1 h), schedule on Fedora (1 h). Ricky and Hollie still do by hand: shoot or choose the photo and write the one line, set the focal box when Claude's proposal is wrong, approve each cover in mode A, and decide the open points below.

## 10. Questions only Ricky and Hollie can answer

1. Hollie's face on covers? The best click evidence favours faces (w1e); hands-first is the stated default.
2. Hot pink for the "Gone" stamp, `#e5a6b4` or a sampled neon pink?
3. May Pinterest get a lighter-ground variant for an A/B (w1e S15)?
4. Is Vercel Pro $20/mo acceptable, or must renders stay on the Fedora box and Windows PC?
5. May the Fedora box run the render job unattended, given that its Chromium is shared with other projects?

## 11. Gaps

Not tested: Windows rendering, Vercel and the real Supabase Edge Runtime, Remotion, any SaaS render, a vision-model frame pick through the API, CLIP, 2x scale. The clip was 320x568. Canva's monthly Pro price, Creatomate's monthly price, Cloudinary and Vercel plan details beyond the WebFetch summaries, and the Canva AI Connector, Creatomate MCP image tool and Figma seat rules are unconfirmed. Two crawls (Cloudinary and Anthropic pricing) stalled, so those facts came from WebFetch summaries.

## Sources (accessed 2026-10-29)

Satori README https://raw.githubusercontent.com/vercel/satori/main/README.md · @vercel/og https://vercel.com/docs/og-image-generation · Vercel fair use https://vercel.com/docs/limits/fair-use-guidelines · Vercel pricing https://vercel.com/pricing (WebFetch) · Supabase OG example https://supabase.com/docs/guides/functions/examples/og-image · Supabase limits https://supabase.com/docs/guides/functions/limits · Remotion licence https://www.remotion.dev/docs/license/pricing · renderStill https://www.remotion.dev/docs/renderer/render-still · Playwright screenshots https://playwright.dev/docs/screenshots · OFL FAQ https://openfontlicense.org/ofl-faq/ · Fonts https://github.com/google/fonts/tree/main/ofl · Canva autofill https://www.canva.dev/docs/connect/api-reference/autofills/create-design-autofill-job/ · Canva pricing (w1e S21) https://www.canva.com/pricing/ · Placid https://placid.app/pricing · Bannerbear https://www.bannerbear.com/pricing/ · Creatomate https://creatomate.com/pricing · Creatomate MCP https://creatomate.com/docs/fundamentals/getting-started/mcp-integration (snippet) · APITemplate.io https://apitemplate.io/pricing/ · Cloudinary https://cloudinary.com/pricing (WebFetch) · Claude pricing https://platform.claude.com/docs/en/about-claude/pricing (WebFetch) · Claude vision https://platform.claude.com/docs/en/build-with-claude/vision (WebFetch) · Figma write to canvas https://developers.figma.com/docs/figma-mcp-server/write-to-canvas (snippet) · GitHub stats via `gh api` for vercel/satori, yisibl/resvg-js (now thx/resvg-js), remotion-dev/remotion, microsoft/playwright, christophschuhmann/improved-aesthetic-predictor; npm versions via `npm view`.
