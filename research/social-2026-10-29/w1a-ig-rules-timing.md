<!-- Saved verbatim by the parent session from agent w1a's final message, 2026-10-29 (the agent's heredoc write failed on a bash parse error). Raw captures: research/social-2026-10-29/raw/w1a-*, transcripts raw/w1a-clipfeed-1..4-*.txt -->

REPORT WRITE FAILED: my one heredoc attempt to research/social-2026-10-29/w1a-ig-rules-timing.md died with a bash parse error ("unexpected EOF while looking for matching '"), so no file was created and I did not retry. Parent: save the report below verbatim as `research/social-2026-10-29/w1a-ig-rules-timing.md`. Raw captures are in `research/social-2026-10-29/raw/w1a-*` (pages, plus `w1a-clipfeed-1..4-*.txt` transcripts).

# w1a: Instagram's own rules, ranking and timing (Holliewood & Vine)

Accessed 2026-10-29 unless noted. Budget used: 19 of 20 searches; about 75 crawls (over the ~40 guide because pages were fetched in parallel and about 10 captures were thin, dead or the wrong page; those were deleted); 5 of 5 clipfeed attempts (4 transcripts, 1 failed on an image carousel).

Tags: `verified` = read on the live page this session. `vendor` = tool-vendor claim (marketing). `study (n, window)` = stated sample. `press` = trade press quoting Instagram. `unverified` = snippet or memory. `inferred` = my reading.

## TL;DR

1. **No universal best time exists.** Instagram's FAQ: "When your audience is awake and most active. Use your insights" `verified`. Five 2026 vendor studies give five different answers (Tue-Wed midday, Thu 9 am, 8 pm, 5 am, Eastern Saturday 11 am). Instagram also says posts with many reactions in the first 30 minutes are NOT ranked higher `verified`.
2. **Ranking, from Mosseri's mouth (video posted 2025-01-21):** for both followers (connected) and non-followers (unconnected) the top signals are average watch time, likes per reach, sends per reach; "time is the most important for both"; sends weigh a bit more for non-followers `verified (transcript)`. Instagram's per-surface lists date from 2023 (Search: 2021). **No 2026 change to ranking signals found.**
3. **Five gates to be shown to non-followers** (Mosseri, 2025-01-23): no watermarks, add audio (esp. photos/carousels), video 3 minutes or less, original, good Account Status `verified (transcript)`. Originality rules extended to photos and carousels 2026-04-30 `verified`.
4. **Hashtags: the Help Center now says up to 5 per post** `verified`. Instagram says fewer, targeted tags do better `press` (2025-12-18). Mosseri has said tags do not raise reach `press`. Keywords belong in caption, handle, Name and bio (Search rule, 2021) `verified`.
5. **Cadence:** Instagram says creators with the greatest net follower growth post "10 or more reels per month" (FAQ, undated) `verified`; Mosseri: pick a sustainable pace `verified (transcript)`; Buffer: 3-5 feed posts a week `study (2.1M posts, 102K accounts, published 2025-08-13)`. The d1 skeleton has only about 7-9 reels in 4 weeks, which is short.
6. **A 0-follower account fails two gates:** Trial Reels need 200+ followers (professional account); Insights "times followers are most active" needs 100+ followers `verified`. Month-one tests must use per-post metrics.
7. **A Facebook Page is not required for API publishing** (Unified Login, Instagram Login) `verified`. This conflicts with PLAN.md wave 3 ("link Facebook Page" before "scheduler"); flagged, not changed. In-app scheduling: any public account, 25 posts a day, 30 days ahead; no collab posts or product tags on scheduled posts `verified`.
8. **Music:** Meta's licensed library is "intended for personal, non-commercial use" and "certain business accounts" lack it; Sound Collection (14,000+ tracks) is commercial-safe; boosted reels cannot use licensed music `verified`. Meta publishes **no Business vs Creator matrix**. Use the room's own audio plus Sound Collection.
9. **Constraint risks (section 7):** giveaway promotion and engagement bait are non-recommendable `verified`; whether "reply LINK" counts is not stated; location tags vs "no showroom language"; Name/bio must say "style", never "interior design".
10. **AI:** the "AI-generated profile" label (2026-08-31) covers AI-generated *people* only; ordinary AI tools need no label `verified`. Real-photo policy is unaffected, with one export-metadata caution.

---

## 1. Ranking, per surface

Sources: Mosseri, "Instagram Ranking Explained", **2023-05-31**, https://about.instagram.com/blog/announcements/instagram-ranking-explained `verified`; "Breaking Down How Instagram Search Works", **2021-08-25**, https://about.instagram.com/blog/announcements/break-down-how-instagram-search-works `verified`; Creators FAQ (undated), https://creators.instagram.com/faq?locale=en_US `verified`; videos in section 6.

| Surface | Predictions / signals Instagram lists | Statement date | Use for H&V |
|---|---|---|---|
| Feed | Time spent, comment, like, share, profile tap. Signals: your activity, post info (popularity, **when posted, location tag**), poster info, interaction history | 2023 | Location tag is a named signal (flag in section 2) |
| Reels | Reshare, watch all the way, like, audio-page visit; 2025: watch time, likes per reach, sends per reach | 2023, 2025-01-21 | Hook, watch-through, "send this to someone who loves lamps" |
| Explore | Likes, saves, shares; post popularity matters "much more" than in Feed | 2023 | Saves-worthy carousels (how to read a lamp) |
| Stories | Tap, reply, move on; viewing history, closeness | 2023 | Followers only; drop-day nudges |
| Search | "The text you enter... is by far the most important signal"; matched to usernames, bios, captions, hashtags, places; keywords in **caption not comments** | 2021 | Handle, Name, bio, caption keywords |

- **Feed does not favor reels over photos** (FAQ). **No early-reaction boost:** "If posts get a lot of reactions in the first 30 minutes are they ranked higher? No, we can confirm this isn't true!" (https://creators.instagram.com/profile) `verified`.
- **Each surface is ranked on its own engagement:** "Engagement that takes place on each surface matters the most for that specific surface." `verified`
- **How non-followers find you:** every eligible reel goes to a small non-follower sample, then widens "based on its engagement, not just the creator's follower count" (Creators blog 2025-02-26, https://creators.instagram.com/blog/helping-creators-of-all-sizes-break-through) `verified`; rollout began April 2024 (https://creators.instagram.com/recommendations-and-originality) `verified`.
- **Audience matching:** "if you or another creator within your niche have previously posted content that's earned more distribution from the audience you're looking to engage, sharing content around a similar theme could get similar distribution" (FAQ) `verified`. `inferred`: stay in one lane (lamps, pink glass, burgundy room).
- **New/small accounts:** no special boost is stated anywhere I read. Treatment is the equal-chance sampling above plus Trial Reels at 200+ followers. Do not promise a "new account bonus".
- **"Your Algorithm"** (viewers set topics they want more or less of): Reels 2025-12-10, Explore 2026-04-15, all of Instagram in English 2026-06-10 (https://about.instagram.com/blog/announcements/reels-algorithm-control) `verified`. `inferred`: clear topic words in captions and on-screen text matter more.
- Instagram claims: Reels are over 50% of time spent (https://creators.instagram.com/how-to-grow); 75% of US recommendations now come from original posts (2026-04-30) `vendor claim`.

---

## 2. Rules that change what we can do

| Topic | What Instagram says (source, date, tag) | Consequence for H&V |
|---|---|---|
| Originality, aggregators | Reels protections (2024) extended to **photos and carousels 2026-04-30**: accounts that "primarily post unoriginal content... will no longer be shown in places where we recommend content"; eligible again when most recent posts are original over a rolling 30 days (https://creators.instagram.com/blog/rewarding-original-creators-on-instagram) `verified`. "Photos or videos you took" count as original (https://creators.instagram.com/original-content-guidelines) | Own photos and video are fine. Never re-upload a supplier's or another dealer's photos |
| Watermarks, quality | FAQ: "Ditch the watermark! The 3rd party watermark... may be impacting its reach." 2023 page: less visible for low-resolution, watermarked, **muted, bordered, majority-text** reels and reels "already posted on Instagram" `verified` | Export clean masters; no TikTok/CapCut marks; no letterbox borders; never re-upload the same clip |
| Not recommendable | Help page (https://www.facebook.com/help/instagram/313829416281232) `verified`: clickbait or engagement bait, unoriginal repurposed content, "long captions unrelated to the underlying content and coordinated comment networks". FAQ adds content "which promotes a contest or giveaway" `verified` | **Do not frame the mirror ball as a giveaway.** "Reply LINK" may read as engagement bait; not stated either way (`inferred` risk) |
| Account Status | Settings > Account status shows recommendation eligibility and appeals `verified` | Check weekly during the experiment |
| Trial Reels | Launched 2024-12-10. Public account; **professional 200+ followers, personal 1,000+**; make a *new* reel ("may get limited reach if Instagram detects that you've previously shared the same content"); insights in 24 h; auto-share to followers can be set (https://www.facebook.com/help/instagram/1013292530224018, https://creators.instagram.com/blog/instagram-trial-reels) `verified` | Unavailable in month one. After 200 followers, test hooks on non-followers first |
| Collab posts | Listed as an approved collaboration tool for originality (2026-04-30) `verified`; **not compatible with scheduled posts** `verified`. Eligibility not read | Post live, not scheduled |
| Broadcast channels | Text, video, voice, polls; share to Stories, pin to profile (https://creators.instagram.com/create/broadcast-channels) `verified`. Eligibility not read | Best native "tell me when the drop opens" list; no claims in the channel |
| Hashtags | Help Center: "You can use up to **5** tags on a post" (https://www.facebook.com/help/instagram/351460621611097) `verified`. Press 2025-12-18 quoting Instagram: "fewer (up to 5) more targeted hashtags... can improve both your content's performance". FAQ: relevant trending tags can help, irrelevant ones hurt. Mosseri: tags "don't improve visibility" but describe the post `press` | Use 3-5 niche tags (vintage lamp, mid century decor); no generic ones |
| Keywords, SEO | Search matches handle, profile name, bio, captions, hashtags, places; "include relevant keywords and locations in your bio" (2021) `verified`. Google indexing of professional-account public posts from 2025-07-10 `press` (https://metricool.com/instagram-indexing-on-google/); Instagram's own page not read | Name field like "Holliewood & Vine | Vintage lamps & decor" (`inferred`); never "interior design" (Florida ch. 481 rule) |
| Alt text | API field `alt_text` for image posts since 2025-03-24 (https://developers.facebook.com/documentation/instagram-platform/content-publishing.md) `verified`. Ranking use not stated | Pipeline can write alt text |
| Location tags | Named Feed signal; Instagram's profile tip says to add one `verified` | **Conflicts with "no showroom language" if it is a business pin.** City/region tag only; Ricky decides |
| Reel length | Recommended to non-followers: **3 minutes or less** (FAQ; Mosseri). 3-minute reels in the editor, US, early 2025 (https://creators.instagram.com/blog/the-latest-with-instagram) `verified` | Keep reels short (`inferred`: 8-45 s) |
| Carousels, audio, grid | Up to **20** items (developer doc) `verified`. Audio on photos/carousels "may also appear in the Reels tab" `verified`. 3:4 photos supported 2025-05-28 `press`; vertical 3:4 grid (Planoly, updated 2025-10-31) `vendor` | Add audio to every carousel. Cover design is lane w1e |
| Link in bio, handle rules | **Not verified** (gaps) | Do not rely on "5 links" or "30 characters" |
| AI labels | **AI-generated profile** (renamed from AI creator label, 2026-08-31): for profiles featuring an AI-generated *person*; unlabeled ones lose reach; "Creators who simply use AI tools as part of their creative process don't need to add the label" (https://creators.instagram.com/blog/ai-generated-profile-label) `verified`. "AI info" labels appear when industry-standard indicators are detected or the poster discloses (https://transparency.meta.com/governance/tracking-impact/labeling-ai-content/, updated 2025-02-19) `verified`. API has `is_ai_generated` `verified` | `inferred`: generative-fill or upscalers that stamp C2PA metadata could trigger "AI info" on real product photos. Test one export before the pipeline commits to a tool |
| Shoppable reels | "Add products" needs items in a Meta commerce catalog; up to 30 per reel; US rolling out (https://creators.instagram.com/blog/new-ways-to-earn-making-reels-shoppable) `verified` | Same blocker as d1: no real checkout, no catalog |

---

## 3. Music: Business vs Creator

Sources `verified`: https://www.facebook.com/help/instagram/402084904469945 (mirror of help.instagram.com), https://www.facebook.com/government-nonprofits/blog/music-for-videos-on-facebook-and-instagram, https://www.facebook.com/help/instagram/570215404599013, https://www.facebook.com/help/instagram/329208821595430.

- "The music available in our library is intended for personal, non-commercial use." "Certain business accounts and certain types of posts do not have access to the library."
- Sound Collection: "over 14,000 songs and sounds which are entirely royalty free... can be used for commercial purposes like ads"; the blog adds 1,500+ sound effects. Find it under **Audio** in the Reels camera.
- Boosted reels "can't use licensed music". Licensed tracks "can become muted" if rights deals change.
- **Meta does not say which account type gets the licensed library.** Vendor blogs call Creator a "gray area" (`unverified`). Open Audio on the real account before planning around it.

| Audio option | Price | Risk | Wins when |
|---|---|---|---|
| Room's own recorded audio ("Original audio" under H&V) | Free | Low; music playing in the room is third-party music (`inferred`) | Neon click, lamp switch, wrapping |
| Meta Sound Collection | Free | Low; may not match "room mood" | Carousels, mood reels |
| Licensed library | Free | Business accounts may lack it; mute risk; no boosting | Only if the account actually shows it |
| Direct license via Rights Manager allow-list | Not priced | Contract effort | A playlist the shop owns |

---

## 4. Account setup

Sources `verified`: https://www.facebook.com/help/instagram/502981923235522; https://developers.facebook.com/documentation/instagram-platform/overview.md and `.../content-publishing.md`; scheduling https://www.facebook.com/help/instagram/439971288310029; Insights https://www.facebook.com/help/instagram/788388387972460.

| Option | Meta wording | What depends on it | Wins when |
|---|---|---|---|
| **Business** | "best for retailers, local businesses, brands, organizations and service providers" | Insights, ads, API, Trial Reels (200+ followers) | H&V default (`inferred`): it is a retailer |
| Creator | "best for public figures, content producers, artists and influencers" | Same tools; music access unstated | Only if its licensed audio library is proven to open and Business's does not |
| Personal | Default | Scheduling works on any public account; **no API; Trial Reels need 1,000 followers** | Never for the pipeline |

- The category label does not decide the type; switch any time. Switching to personal removes ads and **disconnects the Facebook Page**. A private account becomes public when switched.
- Page in setup is optional ("will make it easier to share Instagram posts on Facebook and use connected experiences such as ads and shopping tools").

| Feature | Needs a Facebook Page? |
|---|---|
| In-app scheduling (25/day, 30 days ahead, public account; no collab/product tags) | No |
| API, Unified Login (recommended for new builds; needs a business portfolio) | **No** |
| API, Instagram Login | **No** |
| API, Facebook Login | Yes |
| Facebook cross-posting, some ads and shopping tools | Yes |
| Own-account API use | Standard Access only, **no App Review**; Advanced Access (other people's accounts) needs App Review plus Business Verification |

- **Flag to parent:** PLAN.md wave 3 puts "link Facebook Page" before "scheduler". For Instagram-only publishing it is no longer a prerequisite; Facebook posting still wants a Page. Unified Login needs a business portfolio (`inferred`: a Meta Business account, not a registered entity, since Business Verification is only for Advanced Access).
- **Developer doc contradicts itself:** 100 API-published posts per 24 h (rate-limit section) vs 50 per 24 h (carousel limitations). Plan for 50.
- Handle rules, link-in-bio limit, Notes: not verified.

---

## 5. Timing and frequency

### 5.1 What Instagram says
- Best time: "When your audience is awake and most active. Use your insights." `verified`
- Cadence: the greatest net follower growth goes to creators posting "10 or more reels per month" on average (FAQ, undated). Reply to comments within 7 days to help reach `verified`.
- Mosseri (2024-12-06): more posting generally means more reach; burnout is real; pick a sustainable pace; define repeatable "patterns" `verified (transcript)`.
- Stories: "not a specific ideal number", but over 4-5 a day was reported to lower reach for now (OnlineMarketing.de/t3n, 2025-05-12, quoting a Mosseri Q&A) `unverified (press)`.

### 5.2 Big-sample studies (vendor marketing; each measures something different)

| Source (published) | Data window | n | Method / outcome | Instagram result | Tag |
|---|---|---|---|---|---|
| Sprout, https://sproutsocial.com/insights/best-times-to-post-on-social-media/ (2026-03-31) | 2025-11-27 to 2026-02-27 | ~2B engagements, ~307K profiles (all networks) | Engagement, local time | Tue 1-7 pm, Wed 12-9 pm; Mon 2-4 pm; Thu 12-2 pm; **weekends worst** | study, vendor |
| Buffer, https://buffer.com/resources/best-time-to-post-social-media/ (2026-03-25) | Not stated | 52M posts all platforms; "nearly 10 million" Instagram | Median engagement/reach (page uses both), local time | **Thu 9 am**; Wed best day; 6 pm secondary; **Friday worst** | study, vendor |
| Hootsuite + Critical Truth, https://blog.hootsuite.com/best-time-to-post-on-instagram/ (page dated 2026-07-14) | Heatmap filenames say Q4 2024; not stated | >1M posts, 118 countries | Engagement | Retail: Mon 7-11 am, Tue 5-7 pm, Thu 9 am, Fri 6-10 am/5-9 pm. **Eastern: Sat 11 am** | study, vendor |
| Later, https://later.com/blog/best-time-to-post-on-instagram/ (2026-04-21) | **2024-01 to 2024-10** | >6M posts | Engagement, "across time zones" | **5 am** overall; Reels Mon 12-6 am | study, vendor |
| Metricool 2026 Instagram Study, https://metricool.com/best-time-to-post-on-instagram/ (2026) | Not stated | 24,364,803 posts, 375,118 accounts | Interactions | Mon-Wed **8-9 pm**, Thu 6 pm, Sat/Sun 6-8 pm; "dead zone" 2-5 am | study, vendor |
| Rival IQ benchmark, https://www.rivaliq.com/blog/social-media-industry-benchmark-report/ (2025-02-25) | Companies selected as of Jan 2023 | 150 random companies per industry, 14 industries | Median engagement rate | No timing. Home Decor: **Reels highest engagement**; Home Decor and Retail Instagram engagement down ~30%; figures are in chart images (not read) | study |
| Buffer frequency, https://buffer.com/resources/how-often-to-post-on-instagram/ (2025-08-13) | Not stated | 2.1M posts, 102K accounts | Within-account z-score and fixed effects (each account vs its own baseline) | **3-5 feed posts a week** more than doubles follower growth vs 1-2; zero posts is below baseline (-0.08 SD); 6-9 and 10+ add more with diminishing returns | study, vendor |
| Sprout frequency, https://sproutsocial.com/insights/how-often-to-post-on-social-media/ (2025-08-27) | Not stated | ~3B messages, 1M profiles | Descriptive average | Average 1-2 posts a day | study |

Socialinsider's best-time page returned a 404 (their benchmarks are lane w1c). Buffer itself wrote (2020-03-11): "The best time to post is when your followers are online and engaging with your posts" `vendor`.

### 5.3 Verdict
**No universal best time.** (1) The five studies disagree by up to 16 hours and on weekends (Sprout "weekends worst", Hootsuite Eastern "Saturday 11 am", Metricool "Sat/Sun 6-8 pm"). (2) They measure different outcomes with different time-zone normalization and windows from 2024 to early 2026. (3) Later's 5 am and Metricool's 2-5 am "dead zone" cannot both hold. (4) Instagram says the awake-audience time matters and denies an early-reaction boost, against Metricool's "speed and volume of early interactions" narrative (X verified, Y need review). (5) Recommendations reach non-followers over days, so clock time should matter less for them (`inferred`).

### 5.4 Hypotheses for a U.S. East Coast home-decor audience (all `inferred`)
| ID | Slot (ET) | Basis |
|---|---|---|
| H1 | Weekday 6:30-8 pm | Metricool evening peak; Buffer 6 pm; Hootsuite retail Tue/Fri evening |
| H2 | Weekday 7:30-9 am | Buffer Thu 9 am; Hootsuite retail Mon/Thu morning |
| H3 | Weekday 12-1 pm | Sprout midday Wed/Thu |
| H4 | Saturday ~11 am | Hootsuite Eastern; weekend decor browsing (`inferred`) |
| H5 | Fixed weekly drop slot | Not a test: DROP DAY is Ricky's call; keep it out of the experiment |

### 5.5 Options
| Timing method | Price | Effort | Risk | Wins when |
|---|---|---|---|---|
| Vendor-published times | Free | None | Contradictory, not your audience | Never as the final answer |
| Scheduler's personal model (Buffer Analyze, Sprout ViralPost, Hootsuite Perch) | Not read in this lane | Low | Needs enough followers and history | After a few hundred followers |
| Insights rotation experiment (5.6) | Free | Medium | Noise at small n | Month one |
| Trial Reels | Free | Low | 200+ followers; tests hooks, not clock time | After 200 followers |

| Cadence | Evidence | Risk | Wins when |
|---|---|---|---|
| 1-2 posts a week | Buffer "minimum"; less stagnates | Slow | Pipeline not built |
| **3-5 feed posts a week, 10+ reels a month** | Buffer sweet spot; Instagram FAQ | The d1 skeleton has ~7-9 reels in 4 weeks (week 1: 3; weeks 2-3: 1 each; week 4: 2); add 2-3 reels cut from existing footage | **Recommended start** |
| 6-9+ a week | Buffer: diminishing returns, "treat with caution" | Burnout; Mosseri warns | Only once autonomous |

### 5.6 Four-week experiment: find Hollie's own slots

**Reality check.** At 0 followers a timing test mostly measures noise. Sixteen posts cannot separate slot from weekday or content, so treat the output as a screen to retest. At 100 followers Insights adds "times they're most active" as a second opinion `verified`. After 200 followers, use Trial Reels for hooks.

**Design (Latin square, 4 slots x 4 formats x 4 weeks):**

| Week | A: Tue 8 am | B: Wed 12:30 pm | C: Thu 7 pm | D: Sat 11 am |
|---|---|---|---|---|
| 1 | Reel 1 (neon) | Reel 2 (lamp click) | Carousel (read a lamp) | Reel 3 (wrapping) |
| 2 | Reel 3 | Reel 1 | Reel 2 | Carousel |
| 3 | Carousel | Reel 3 | Reel 1 | Reel 2 |
| 4 | Reel 2 | Carousel | Reel 3 | Reel 1 |

Each format lands in every slot once. Room and brand content only (no product-link posts until real stock exists).

**Measure per post** (definitions: https://www.facebook.com/help/instagram/202865988324236): Views, Viewers, **average watch time** (watch time / initial views), likes, **shares (sends)**, saves, follows, and the follower vs non-follower split where shown. Primary: average watch time and **sends per viewer**. Secondary: likes per viewer, follows per 1,000 viewers. Read at **24 h and 7 days** (the FAQ's 7-day comment window). A view/skip rate (first 3 seconds) is mentioned in the Feb 2025 Creators post; its presence in the app is unconfirmed.

**Fairness rules (write before posting):**
1. Same caption template, hashtag count (3-5), cover style and call to action across all 16.
2. No boosting, giveaways or collabs; no extra feed posts within 3 hours of a test post; constant Stories count.
3. Same audio rule (room audio or Sound Collection).
4. Skip the Thanksgiving to New Year weeks (`inferred`; the Sprout window shows holiday skew).
5. One sheet: post, format, slot, length, hook, audio, metrics at 24 h and 7 d, Account Status check.
6. **Decision rule:** a slot qualifies only if it ranks top two of four on both primary metrics in at least 3 of 4 weeks. Otherwise record "no detectable difference" and use the slot easiest for Hollie. Retest the top two vs the bottom one for four more weeks.

Pipeline note: the same metrics exist in the Instagram Media Insights API (https://developers.facebook.com/documentation/instagram-platform/reference/instagram-media/insights), so Claude can fill the sheet; interpreting it stays with Hollie.

---

## 6. Clipfeed: Instagram and Mosseri videos

Whisper-small transcripts via the Fedora box, 10+ s apart; dates are yt-dlp post timestamps (UTC); likes as of 2026-10-29. Minor mishearing is possible. All four were posted by Adam Mosseri (@mosseri). A fifth attempt (a "View Rate" carousel, `DFaeuUyxKqZ`) had no video and failed. I found no Mosseri ranking video from 2026.

| # | URL | Posted | Likes | Raw |
|---|---|---|---|---|
| 1 | https://www.instagram.com/p/DFFyRp-pINJ/ | 2025-01-21 | 53,359 | `w1a-clipfeed-1-mosseri-top3.txt` |
| 2 | https://www.instagram.com/reel/DDPU_hfSgnZ | 2024-12-06 | 43,657 | `w1a-clipfeed-2-mosseri-freq.txt` |
| 3 | https://www.instagram.com/p/DFK_lARJBVC/ | 2025-01-23 | 48,222 | `w1a-clipfeed-3-mosseri-DFK.txt` |
| 4 | https://www.instagram.com/p/DA0ua3-yuDg/ | 2024-10-07 | 230,398 | `w1a-clipfeed-4-creators-hook.txt` |

- **#1 ranking (series part 1):** "there are two types of ranking on Instagram. There's one for accounts you follow, we call that connected reach, and there's another for accounts that do not follow you yet... recommendations or unconnected reach. Now for both, the most important signals are the same three... average watch time, likes per reach, and sends per reach... likes are actually slightly more important than sends for connected content, and sends are actually a little bit more important than like for unconnected content, but time is the most important for both." On over-posting: trials "bypass the entire connected ranking system, and just go straight to the unconnected recommendations."
- **#2 frequency:** "the more you post in general, the more reach you're gonna get... if you commit to too much content creation, you're gonna burn out... I have seen creators that are very successful that create only one thing a month and... five reels a day... pick some pace that is sustainable for you... define a few patterns."
- **#3 eligibility (series part 2):** "you need to meet these five criteria. One, no watermarks. Two, make sure you add audio, particularly important for photos and carousels. Three... three minutes long or less. Four, make sure that the content is original... Five, make sure your account is in good status, which you can check by going to profile into account status."
- **#4 hook:** "The first three seconds of a reel are super important... use text when possible because a lot of times people actually have to sound off to start. And two, set expectations."

---

## 7. Recommendation for Holliewood & Vine

| Tier | What | Human must still |
|---|---|---|
| (a) Free, native | Business account; Name/bio/caption keywords; 3-5 targeted hashtags; in-app scheduling; Insights; room audio plus Sound Collection; Instagram's Edits app for clean export without watermark and direct-share priority processing (https://creators.instagram.com/blog/best-camera-settings-instagram-reels, 2026-04-09; Edits price not read); run the Latin square by hand; 10+ reels a month | Film, tap Post (collabs and product tags cannot be scheduled), reply, read the sheet |
| (b) One paid tool | Only for a scheduler's personalized best-time model once followers exist (prices not read here; d1 has the free caps) | Same, plus choosing the tool |
| (c) Claude + Codex | Instagram API via Unified or Instagram Login (no Page; Standard Access on own account; no App Review); the pipeline fills the metrics sheet and drafts captions with the keyword/hashtag rules; Trial Reels API (`trial_params`) after 200 followers | Approve each post (or by exception), reply to people, vet any AI-tool output for an "AI info" label |

**Flags against fixed constraints (not applied silently):**
- Mirror-ball gift vs the non-recommendable "contest or giveaway" category: keep it "sometimes", never a promotion.
- "Reply LINK" call to action vs engagement bait: unresolved.
- Location tag vs "no showroom language": city/region only.
- Name/bio wording vs the ch. 481 "style" rule.
- PLAN.md wave 3 Page-first ordering is outdated for Instagram-only publishing.

## 8. X verified, Y need review
- Scheduling: 25 a day, 30 days ahead, any public account (Help Center, verified) vs 75 days, professional only (2022 snippet).
- Hashtags: 5 (Help Center, verified) vs 30 (older snippet of the same article).
- API publish limit: 100 vs 50 per 24 h in the same Meta doc.
- Best time: five studies disagree; Instagram: early reactions do not boost.
- "Sends weigh 3-5x likes" and "watch time 35% / saves 25% / DM shares 20%": no primary source; discard.
- The 2021/2023 surface lists predate the 2025 three-signal statement; both are Instagram's own.
- Meta Business Help pages (facebook.com/business/help/...) were walled; the same facts came through facebook.com/help/instagram/<id> mirrors.

## 9. Questions only Ricky can answer
1. Business account confirmed? Is `@holliewoodandvine` yours?
2. Keep "reply LINK" as the only CTA despite the unknown engagement-bait line? (Check Account Status after 30 days.)
3. Which location tag may we use (city/region, never a shop pin)?
4. Does the shop own any playlist rights, or only room audio plus Sound Collection?
5. Is Saturday posting (slot D) acceptable to Hollie?
6. Add 2-3 reels to the d1 skeleton to reach 10+ a month?

## 10. Gaps
Handle rules and the link-in-bio limit not verified; Notes; collab-post and broadcast-channel eligibility not read; no Business vs Creator music matrix from Meta; no 2026 Mosseri ranking video or 2026 official signal page; Instagram's own search-indexing page not read; Rival IQ Home Decor figures are in images; Hootsuite, Metricool and Buffer Instagram data windows not stated on the pages read; Socialinsider timing page 404; Edits paid tiers not checked.
