# w1e-covers-thumbnails: covers and thumbnails that get clicked, as a build spec

Lane w1e, written 2026-10-29. All pages accessed 2026-10-29. Raw captures: `research/social-2026-10-29/raw/w1e-*.md`. Tags: `verified` (read on the live page this session), `vendor claim`, `study (n=, date)`, `unverified (snippet or search-tool summary)`, `inferred`. Sources are coded S1-S29 in the list at the end. Not read: Instagram, TikTok and Meta help pages (walled; WebFetch returned only "Help Center"), so no Instagram or TikTok cover spec is `verified`.

## TL;DR

1. **Evidence on cover design is thin.** No controlled study of Instagram or TikTok covers was found. YouTube and Pinterest have official A/B routes; Instagram has none for covers. Rotate templates and judge only large gaps. `inferred`
2. **Design one 1080x1920 master with a 1080x1080 "hard-safe square" at y 420-1500.** It survives the Instagram 3:4 grid crop (y 240-1680, S9/S10, `vendor claim`), the 4:5 feed crop (y 285-1635, S9, `vendor claim`) and TikTok's grid crop if that is square (S26, `unverified`). `inferred` from those sources.
3. **YouTube Shorts take a custom thumbnail, uploaded in Studio on a computer by a verified account**, 9:16, 2160x3840 recommended. `verified` S1. Shorts cannot be A/B tested. `verified` S2.
4. **Faces are the best-evidenced click lever** (vidIQ n=500, 69% of breakouts, vendor; Bakhshi n~1.1M, +38% likes, 2014 academic). This conflicts with hands-first. Surfaced, not applied.
5. **Pinterest: own 2:3 file at 1000x1500** (`verified` S4/S5). Too much overlay text lowers saves (Pinterest-shared study, fashion, undated, S14). A 5-8 word overlay raising clicks 2.1x is a vendor claim (S15).
6. **Pinterest's own data favors real-life settings over plain backgrounds** (+30% clicks, +170% checkout, S14). That pushes against isolated cutouts, so each template gets a room-context variant.
7. **A vendor dataset says dark Pin backgrounds get 38% fewer saves than light ones** (S15, n=148k, LLM-labelled). It conflicts with the burgundy brand. Needs a Pin A/B, not a rebrand.
8. **Colors:** cream on burgundy 12.61:1, pink `#e5a6b4` on burgundy 7.18:1 (computed). Pink on white is 2.01:1, so never pink text on the white frame.
9. **Mosseri called the polished grid "dead"** (S17, secondary coverage). Cohesion is a weaker lever than it was; real photos of real pieces fit that.
10. **Templates 1 (Drop day) and 2 (Here/Gone) stay unposted until real stock exists.**

## 1. Platform specs (2026)

| Surface | Spec | Source and tag |
|---|---|---|
| IG Reel cover | 1080x1920 (9:16). Profile grid shows 3:4 (1013x1350 rendered, 240 px lost top and bottom). Reels feed shows 4:5 (1080x1350). Grid moved from squares in Jan 2025. | Planoly S9, Hopper S10: `vendor claim`. Meta help page S28 via search-tool summary: Reels 1.91:1 to 9:16, min 30 fps, min 720p: `unverified` |
| IG cover edit | Hopper: no edit after posting. Planoly: "Adjust Preview" (three dots) repositions the grid thumbnail. | `vendor claim`, conflict, see section 9 |
| IG photo / carousel | 3:4 now accepted natively "exactly as you shot it"; 1:1 and 4:5 still work. 4:5 is cropped to 3:4 in the grid. | SMT S11 quoting Instagram, 2025-05-28: `vendor claim` (trade press quoting Instagram) |
| IG Stories / Reels safe zone | Keep 14% top, 35% bottom, 6% sides free of text and logos (y 269-1248, x 65-1015 on 1080x1920). Stated for Reels **ads**; image ad spec is 1440x2560, JPG/PNG. | Meta S8: `verified` for ads. For organic: `inferred` |
| IG carousel first slide | The first slide is the cover in the grid. Mosseri: a non-swiped carousel is re-served, often starting at slide 2, so slide 2 needs cover quality. | S25 blog relaying Mosseri: `unverified` |
| TikTok cover | The upload page lets you "edit the cover image" (`verified` S23, undated blog). Third-party: 1080x1920, JPG/PNG; grid crop either square (1080x1080) or other; the first caption line may print over the bottom. | S26: `unverified (snippet)`. Grid crop unresolved |
| Pinterest Pin | 2:3, 1000x1500; taller than 2:3 "might get cut off"; PNG/JPEG; 20 MB web; title 100 chars; description 800 chars, not shown in feed. Full-bleed 9:16 (1080x1920) safe zone: top 270, left 65, right 195, bottom 790 (organic) or 440 (ads). | S4, S5: `verified` |
| Pinterest text | "Not all Pins need text"; use it "thoughtfully", "headlines or hooks". Ad text overlay: no more than 10 words. | S6, S5: `verified` |
| YouTube Short | Custom thumbnail: Studio, computer only, verified account. 9:16 recommended, 2160x3840, min height 640 px, JPG/PNG, 50 MB desktop. A 16:9 custom on a vertical video is replaced by an auto 4:5 on Home, Explore, Subscriptions. A Short is up to 3 min and square or taller. | S1, S2: `verified` |
| Facebook Reels | No official cover spec read. API docs: 9:16, cover matches video ratio, 10 MB. | Ayrshare S27: `vendor claim`; grid crop unknown |

**Where covers matter** (`inferred`): autoplay feeds (Reels tab, TikTok For You) show the video, not the cover. Covers decide taps on profile grids, search and Explore grids, Pinterest, YouTube, and shared-link previews. Weight effort there. Where a custom upload is impossible, put the designed card as a one-frame end card so a frame picker can select it. `inferred`

## 2. Click evidence

| Lever | Evidence | Tag | Verdict |
|---|---|---|---|
| Face | 500 breakout YouTube thumbnails, 30 niches, June 2026: face in 69% (75% of top 100, 80% of top 50). No non-breakout comparison, so it is prevalence, not lift. S12 | vendor, study (n=500, 2026-06) | Strong prevalence, weak causality |
| Face (Instagram) | About 1.1M Instagram photos: faces +38% likes, +32% comments after controlling for reach; face count, age and gender did not matter. Photos, not covers; 2014. S13 | study (n~1.1M, 2014, CHI) | Best academic anchor, old |
| Contrast | vidIQ: high contrast in 56% of breakouts, falling to 46% in the top 50, so not a differentiator. Another vendor claims 6.5% vs 4.7% CTR (unverifiable, not used). | vendor, study (n=500) | Table stakes, not a lever |
| Text amount | vidIQ: 140 of 500 had no text; 120 used 1-3 words; median 5 among those with text. Pinterest-shared fashion study: too much overlay text = 42% lower saves, 50% lower checkout (S14). Vendor GenSumo: 5-8 words = 2.1x outbound clicks (S15). | S14: Pinterest-supplied, n>10,000 Promoted Pins from 1,000 advertisers, **date not stated (image path suggests Sept 2016)**. S15: vendor, n=148k pins, 2025-early 2026, LLM-labelled | Short beats long. The two Pinterest sources do not contradict if "too much" is more than about 8 words. `inferred` |
| Object in real setting | Pins in real-life settings: +30% clicks, +170% checkout vs plain background (S14). Person in lifestyle context: +23% close-ups vs product-only (S15). | as above | Push toward room context, away from isolated cutouts |
| Object-forward | vidIQ's top-50 schematics include "object-led: works when the subject is the star". | vendor | Supports white-frame object covers, weakly |
| Background tone | Light/warm 8.4 saves per 1,000 impressions vs dark 6.1 (S15). | vendor, uncontrolled | Test, do not assume |
| Custom vs auto cover (IG) | "Up to 30%" (Oakgen), "20-40% grid tap-through" (Lovart). No method. S29 | vendor claim | Ignore the numbers; use custom covers anyway |
| Numbers, curiosity, before/after, consistent color | Nothing sourced found. Thumbnailr.io's Medium post (Mar 8 2026, vendor, no n) asserts pre-attentive processing in 100-150 ms. Found in the microgh0st cache (`psychology-clicks.md`); the rest of that cache is finance-channel specific and was not opened. | `unverified` | Hypotheses to test |
| Platform guidance | YouTube: "90% of the best-performing videos have custom thumbnails"; rule of thirds, readable font, "not too complex". S3 | `verified` (YouTube's claim) | Official, generic |

Mosseri (year-end Threads post, secondary coverage S17): the curated-grid era "is over"; polished images now spark "suspicion"; people share "unflattering candids". `vendor claim` (press paraphrase). Practical read, `inferred`: real, slightly imperfect photos of real pieces beat a glossy generated look.

## 3. Vintage and decor grids: cohesive or mixed

| Account | What it does | Source and tag |
|---|---|---|
| Good Eye Vintage | Drops of about a dozen pieces, "cohesive collections", mostly neutral hues | Coveteur 2022-01-14, S18 |
| Old Gold Trading Co. (Sydney) | "clean, consistent photography", light caption tone | Bedthreads, undated, S19 |
| CCSS | Posts carry "measurements, condition, period and price" | S19 |
| @sbexchange and others | Two dominant looks: creamy monochrome minimal, or pastel seashell. VSP Consignment: "stick with one or two colour palettes". | Globe and Mail via search summary, c.2021: `unverified (snippet)` |
| d1's 12 accounts | Cohesion comes from a named drop, a repeated legend (Here/Claimed) and a palette, not identical templates | `research/round-d/d1-social-video.md`, `verified` there |

Pattern (`inferred`): the best vintage grids pick one palette lane and one photo setup, then vary the object. **Evidence that cohesive beats mixed is press and opinion, not measured.** With Mosseri's comment, use a hybrid: template covers for drops, Here/Gone and series (about half the grid), real room and hands footage for the rest.

## 4. Cover system for Holliewood and Vine

**Master canvas** 1080x1920. Ground burgundy `#451c2b`, vignette `#321520`. One build, then crop per surface:

| Surface | Canvas | Text zone |
|---|---|---|
| Reel / TikTok / Facebook Reel cover | 1080x1920 | x 90-990, **y 420-1500** (hard-safe square) |
| IG carousel or photo | 1080x1350 (4:5) | x 90-990, y 120-1230 (grid trims about 34 px each side) |
| Story | 1080x1920 | x 90-990, y 300-1240 (Meta ad zone, `inferred` for organic) |
| YouTube Short | 2160x3840 (the master at 2x) | same ratios as master |
| Pinterest | **separate 1000x1500 file**, not cropped from the master | title top y 120-420, frame middle, detail bottom y 1180-1380 (S7: visuals in the middle, text top and bottom) |

**Type scale on the 1080 canvas.** A phone is about 390 CSS px wide (assumption). Full-screen factor 1080/390 = 2.77. Profile-grid tile about 129 CSS px (3 columns, `inferred`), factor 8.4. Pin in a 2-column feed about 185 CSS px, factor 5.4 (`inferred`).

| Role | Face and setting | Master px | Pin px (1000 wide) | Rule |
|---|---|---|---|---|
| Display (grid-readable) | Bodoni Moda 700, `opsz` pinned 12 | 168 (20 CSS px at grid size) | 108 floor, use 150 | 1-3 words, 10 characters per line max |
| Headline (read on open) | Bodoni Moda 700, `opsz` 14 | 120, floor 56 (20 CSS px full-screen) | 112 | 2 lines max |
| Sub | DM Sans 600 | 64 | 72 | floor 44 (16 px body) |
| Label | DM Sans 600 caps, tracking 0.08em | 44, floor 34 (12 px) | floor 65 | decoration only: nothing a buyer needs |
| Series number | Space Mono (Courier Prime pending Hollie's pick) | 56 | 65 | write "NO. 3"; no №, ★ or ✦ glyph exists in the three faces |

Why `opsz` pinned low and weight 700: Bodoni hairlines are about 0.2 CSS px at any size and vanish when shrunk; auto optical sizing at 168 px picks opsz 96, the thinnest cut (`docs/type-and-spacing.md`, lane C). Render each cover at 129 px and 185 px wide before approving. `inferred`

**Colors (house rule)**, contrast computed 2026-10-29 with the WCAG formula:

| Pair | Ratio | Use |
|---|---|---|
| Cream `#f6efdf` on burgundy `#451c2b` / `#321520` | 12.61 / 14.51 | all text on the ground |
| Pink `#e5a6b4` on burgundy / deep | 7.18 / 8.27 | accents, stamps, any size |
| Burgundy on white frame | 14.44 | the only text allowed inside the frame |
| Pink on white / on cream | 2.01 / 1.75 | **never** |
| Hot pink `#e33fa6` on burgundy / deep | 3.80 / 4.37 | large stamps only (66 px+ canvas); sampled from a 320 px video frame, may include clothing. `inferred`; Hollie's call; not a brand token |

Rule: body-size text 4.5:1; large text (24 px CSS, about 66 px full-screen canvas; 18.5 px bold) 3:1 (S20 `verified`). WCAG exempts text inside a picture, so this is a **house rule, not a legal one**. The white frame is for the product photo only, never the full background. Pinterest tints white-background Pins 4% (S4), irrelevant on burgundy.

**Photo rules** (all templates): real photo of the real piece only. Cutouts in `site/assets/editorial/` contain generated pixels (`urn-lamp.webp` had its shade top "completed"; `disco-ball.webp` is fully generated) and are **banned from any selling cover**. The ball image would also imply a promised gift. Check the provenance of `site/assets/cutouts` and `demo` before use; the sample listings are not stock. No price, no discount, no "visit", no claim wording on any cover.

### The six templates (coordinates on the 1080x1920 master)

| # | Template | Layout | Photo | Copy (one line) |
|---|---|---|---|---|
| 1 | **Drop day** | Frame x 237-843, y 430-1240 (3:4 incl. 28 px white mat, shadow 0 24 60 black 45%). Display "Open." baseline y 1400, centered, cream. Label "DROP 07 - THURSDAY" y 330-375 and "HERE, THEN GONE" y 1440-1480, pink. | one hero piece, real photo in frame | "Open. Here. Then gone." |
| 2 | **Here / Gone** | Same frame at y 430-1130. **Here:** cream label chip "HERE" on deep ground y 1180-1240. **Gone:** the same cover re-rendered; stamp "GONE." Bodoni 168, pink with glow (0 0 24 px at 40%), y 1230-1400, **on the burgundy, never over the photo**; sub "Someone has taste." DM Sans 64 cream. Photo stays full color. | same photo | "Gone." Caption begins "Gone." and stays up |
| 3 | **Teaser** | Frame shows a tight real detail of the piece, no name, no price, x 237-843, y 430-1130. Display "Tomorrow." y 1300-1420. Sub "Details after." 64. | real close-up | "Tomorrow: lamps. Details after." |
| 4 | **Spec-card carousel cover** (1080x1350) | Headline Bodoni 700 120 px, 3 lines max, top-left x 90, y 150-520. Frame bottom-right x 480-990, y 600-1230. Label "1 OF 6" y 1260. **Slide 2 gets a full cover treatment** (second-chance rule, `unverified`). | piece with a real detail | "Before you fall in love, read the spec." |
| 5 | **Room reveal** | Full-bleed real room photo, 4:5 safe center. Headline "Same corner. More plot." Bodoni 120 in cream, y 480-780, over a deep-burgundy gradient (never text on a busy photo). Before-inset 300x400 at x 90, y 1100, **cream border, not white** (white is product-only). Hollie's own corner only; say "styled by Hollie", never "interior design". | context photo (Pinterest real-life evidence) | "Same corner. More plot." |
| 6 | **Series cover** | Series name Bodoni 700 120 top, y 440-700. "NO. 3" Space Mono 56, pink rule y 720. Small frame x 560-990, y 800-1400 (right on odd, left on even episodes, for grid rhythm). | one representative piece | "Hollie's Top Three. NO. 3" |

**Context variant (all templates, one each):** swap the isolated frame for the piece in the room, frame as an inset. Addresses S14 and S15. Hollie picks.

**Alt text** (Instagram: Advanced settings > Write alt text; reels on the caption screen; edit later via post menu > Edit > Edit Alt Text, S22, `unverified (search-tool summary)`). Formula: `[object] in [material/colour], on a white frame against a burgundy wall. Cover text: "[exact cover words]". [Here|Gone]`. Use only fields that are real on the listing; never invent era, maker or size. Pinterest: put the same sentence plus search words in the title and description (description is not shown in feed but used for relevance, S4).

**Gates:** templates 1 and 2 unposted until real stock exists and checkout is live; template 5's Hire Hollie link only after the inbox exists. "Gone" stays readable (7.18:1) and visible on the grid.

## 5. Options

**Cover production**

| Option | Price | Effort | Risk | Wins when |
|---|---|---|---|---|
| In-app picker (frame or camera roll) | free | 1 min | off-brand frame, UI over text | speed, a one-off |
| Canva Free | US$0; Brand Kit limited to 3 colors (our system has 4), 5 GB (S21) | 10 min per cover | cannot store the full palette | a quick manual cover |
| Canva Pro | US$144 per year for one person (S21; monthly not read); 5 Brand Kits, social scheduling | 10 min | recurring fee | Hollie wants to design by hand |
| HTML-to-PNG templates built by Claude/Codex from this spec | no fee beyond existing subscriptions (build time only) | wave 2 | build and font-render bugs | many covers per week; this is the wave 2 lane |

**Grid strategy:** all-template (consistent, but "polished" per S17); all-raw (on-trend, no recognition); **hybrid (recommended)**. Wins when: hybrid fits both Mosseri and the brand.

**Subject:** object in white frame (brand-true, second to faces on current evidence); hands-first (the default); Hollie's face (strongest evidence; Ricky's and Hollie's call).

## 6. Testing

| Where | How | Limits | Metrics |
|---|---|---|---|
| YouTube long-form | Studio > A/B Testing: up to 3 titles/thumbnails, desktop only, advanced features on, about 2 weeks. S2 `verified` | **Not for Shorts**, kids, private. Winner by **watch-time share**, not CTR. Likely "Inconclusive" at low impressions. Upload at 1280x720+ or all variants drop to 480p | YouTube names CTR on Home and Suggested in the first 24 hours (above-average impressions) and Subscriptions-feed CTR (S3) |
| Pinterest organic | Two Pins differing in one element, published together to the same or similar boards, S6 `verified` | no stats engine | saves, clicks, impressions |
| Instagram | No cover A/B found (`inferred`). Trial Reels show to non-followers first and reach the grid only once shared with everyone (S24), so they cannot test grid covers; they can test the first frame. | tiny n | profile visits per reach, follows, saves |
| TikTok | none found | | |

**At this volume nothing reaches significance.** Rotate templates on a fixed scorecard (same format, one variable per week, 2-3 posts per variant) and trust only gaps of about 2x, then re-run. `inferred`

## 7. Recommendation

| Tier | What | Human must still |
|---|---|---|
| (a) free, native | Build the six templates by hand in Canva Free or the in-app editor; pick covers per section 4; alt text on every post; YouTube A/B only if a long video exists | choose each cover, approve each post |
| (b) one paid tool | Canva Pro US$144 per year so a 5-kit brand palette and resizing exist (1080x1920, 1080x1350, 1000x1500) | pick photo and one line |
| (c) Claude + Codex | HTML-to-PNG renderer with the section 4 coordinates; photo plus one line in, three covers out (master, 4:5, Pin); Ricky or Hollie taps Publish. Approve-everything: a human reviews each render. Approve-by-exception: auto-send only if contrast and safe-zone checks pass and the photo is a real, listed piece | handle the exceptions |

## 8. Where findings touch a fixed constraint (not applied)

| Constraint | Finding | Handling |
|---|---|---|
| Hands-first default | Faces have the strongest evidence (S12, S13) | Optional face variant per template; Hollie decides |
| White frame, isolated pieces | Real-life settings win on Pinterest (S14, S15) | Context variant per template |
| Burgundy atmosphere | Dark Pin grounds saved less in one vendor set (S15) | Pin A/B only; no rebrand |
| White = product framing only | Room-reveal inset | Cream border instead |
| Real photos only | Editorial cutouts hold generated pixels | Banned on selling covers |

## 9. X verified, Y need review

- Reel cover editable after posting: Hopper says no, Planoly says "Adjust Preview" exists. Likely both (image fixed, grid crop adjustable). `inferred`
- Instagram photo range: older help page 1.91:1 to 4:5, newer 1.91:1 to 3:4 (search-tool summary); SMT says 3:4 supported May 2025.
- Grid change: Jan 2025 (Hopper, Planoly) vs a "late 2025 3:4 grid preview" (search snippet).
- Meta 14/35/6 safe zone `verified` for ads; a checker site gives 895x980 (snippet).
- Pinterest bottom margin: 790 (organic, S4) vs 440 (ads, S5), both `verified`.
- TikTok grid crop: square (some sources) vs other. Unresolved.
- Bakhshi corpus: 1M (abstract) vs 1.1M (press release).
- YouTube A/B page was `/answer/13861714` and now redirects to `/answer/16391400`, retitled "A/B test titles & thumbnails".
- Pinterest text: S14 (less is better) vs S15 (5-8 words doubles clicks). Both weak; compatible.
- Vendor contrast claims disagree (vidIQ: not a differentiator; mer.vin: 6.5% vs 4.7%).

## 10. Questions only Ricky and Hollie can answer

1. Hollie's face on covers, yes or no (evidence favors faces; hands-first is the stated default)?
2. Which hot pink for the "Gone" stamp: keep `#e5a6b4`, or sample the real neon sign?
3. May Pinterest get a lighter-ground variant for an A/B? (S15 says dark loses saves; the brand is burgundy.)
4. Which platform first? Build order follows.
5. Cream-bordered inset in the room-reveal cover, or white?

## 11. Gaps

No official Instagram or TikTok cover spec read (walls). No controlled cover study for Instagram or TikTok. Facebook Reels grid crop unknown. How YouTube crops a true 9:16 custom thumbnail on Home is not stated (`inferred` 4:5). The WWD study is undated. Meta Stories and Facebook Reels ad-spec URLs I guessed returned 404. Instagram's carousel 20-slide limit is unconfirmed. Canva monthly price not read. W3C page via WebFetch only (crawl failed).

## Sources (accessed 2026-10-29)

S1 https://support.google.com/youtube/answer/72431 · S2 https://support.google.com/youtube/answer/16391400 · S3 https://support.google.com/youtube/answer/12340300 · S4 https://help.pinterest.com/en/article/review-pin-specs · S5 https://help.pinterest.com/en/business/article/pinterest-product-specs · S6 https://create.pinterest.com/fundamentals/ · S7 https://business.pinterest.com/creative-best-practices/ · S8 https://www.facebook.com/business/ads-guide/update/image/instagram-reels · S9 https://planoly.com/blog/guide-to-instagrams-new-vertical-grid · S10 https://www.hopperhq.com/blog/instagram-reel-size/ · S11 https://www.socialmediatoday.com/news/instagram-adds-support-phone-camera-aspect-ratio-images/749205/ · S12 https://vidiq.com/research/youtube-thumbnail-study/ · S13 https://www.news.gatech.edu/news/2014/03/20/face-it-instagram-pictures-faces-are-more-popular · S14 https://wwd.com/business-news/media/feature/pinterest-studies-supercharge-fashion-content-10544628 · S15 https://gensumo.pages.dev/research/pinterest-pin-design-report/ · S16 https://community.pinterest.biz/t/designing-pins-text-overlays-dos-donts/661 (Feb 2022, community member: large, bold, brief text; test in a phone feed) · S17 https://www.tomsguide.com/ai/instagram-says-ai-killed-the-curated-feed-now-its-scrambling-to-prove-whats-real · S18 https://coveteur.com/vintage-furniture-shops-instagram · S19 https://bedthreads.com/blogs/journal/best-vintage-furniture-on-instagram · S20 https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html · S21 https://www.canva.com/pricing/ · S22 https://help.instagram.com/503708446705527 · S23 https://ads.tiktok.com/business/en-US/blog/introducing-video-scheduler-now-you-can-plan-tiktoks-in-advance · S24 https://creators.instagram.com/blog/instagram-trial-reels · S25 https://ccstartup.com/blog/2024/10/21/why-instagram-carousels-sometimes-start-on-the-second-slide/ · S26 https://socialrails.com/sizes/tiktok/thumbnail and https://mergeimages.net/ja/blog/tiktok-thumbnail-design-2026 · S27 https://ayrshare.com/docs/media-guidelines/facebook_pages · S28 https://help.instagram.com/1038071743007909 · S29 https://oakgen.ai/blog/instagram-reels-covers-guide , https://www.lovart.ai/es/blog/how-to-chat-generate-reels-lovart · microgh0st: `C:\Users\ethan\microgh0st\.firecrawl\psychology-clicks.md`.
