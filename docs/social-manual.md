# Holliewood and Vine: the social media manual

**Status (2026-10-29).** Written from 19 research lanes (`research/social-2026-10-29/`, 8 strategy, 7 automation, 4 live re-checks). Every price and link below was read on the vendor's own page on 2026-10-29 unless it says otherwise; **re-check the price on the signup page before paying.** The content banks (hooks, calendar, cover templates, shoot plan, timing test) are in `docs/social-manual-appendices.md`. The build spec for the automated version is `docs/codex-handoff-social-autopilot.md`.

**On camera (2026-10-30):** what Hollie films and how she talks are in `docs/video-direction.md`; the shoot is `docs/video-shoot-in-depth.md`, with a two-page card in `docs/video-shoot-quick.md`. Voice or on-camera is the default for decision 4 (Hollie's comfort still open).

Tags: `verified` (read on the live page), `vendor claim`, `inferred` (my reading), `need review` (sources disagree or one page was walled).

---

## 0. The short version

1. **Start free and native this week.** Business Instagram account, Instagram's own Edits app, one 90-minute shoot, the room and Hollie's hands. No scheduler, no bots, no spend. Nothing automatic can run yet anyway: no accounts, no real stock, no checkout.
2. **Add Buffer Free in week 2.** It gives 3 channels, 10 queued posts each, and an API **and an MCP server on the free plan**, so Claude can draft and queue posts for Hollie to approve in Buffer. This is the cheapest real autonomy (`verified`: Buffer pricing and MCP pages; Claude driving it is `inferred`, untested).
3. **Build the full pipeline later, in this order of payoff:** Claude-drafted captions, code-rendered covers, a JSON edit list rendered by ffmpeg, a metrics sheet, then own-API publishing. Replies stay by hand until the Meta question in section 9 is settled.
4. **Instagram first, then Pinterest, YouTube Shorts and a Facebook Page. TikTok in month 3** (make the account now to hold the handle). How to grow is section 3A. Skip Whatnot, Poshmark, Depop, Lemon8 and Facebook Groups.
5. **No best time to post exists.** Five 2026 studies give five answers. Run the four-week test in Appendix E and use Hollie's own numbers.
6. **Nothing links to a product until real stock exists.** November is a setup month, not a posting month for products. Room and brand posts can start the day the accounts exist.

### Three tiers

| | **A. Free and native** | **B. One scheduler (recommended middle)** | **C. Full Claude + Codex pipeline** |
|---|---|---|---|
| Software cost | $0 | Buffer $0 (3 channels) or $20 a month (4 channels, billed yearly; $24 billed monthly), plus optional extras below | About $0 to $30 a month (section 6), plus a build |
| One-time | Optional starter gear $78.97 | Gear kit $178.94 optional | Same gear |
| Edits | Instagram Edits on the phone | Edits, or a Claude-written edit list rendered by ffmpeg (tested on the Fedora box; the Windows run is untested) | Edit list rendered automatically on a runner |
| Covers | Canva Free or Edits | Code-rendered cover (Playwright, 1.7 s per cover on the Fedora box) | Same, automatic |
| Posting | Hollie posts in the app (in-app scheduling: 25 a day, 30 days ahead) | Posts queue in Buffer; Hollie approves | Own API on a timer, with Buffer for TikTok and Pinterest |
| Replies | Hollie, by hand | Hollie, by hand; optional ManyChat or InstantDM | Drafts into an approval queue; keyword rule |
| Hollie's time per post | 10 to 15 min (`inferred`) | 6 to 10 min (`inferred`) | 1 to 3 min (`inferred`) |
| Build effort | None | 3 to 4 hours (Buffer, `inferred` by w2c) | Claude 28 to 35 hours, Codex about 3, Ricky about 4 |
| Needs a legal entity? | No | No | No for posting; **likely yes** for automatic comment replies (section 9) |

---

## 1. Decisions I need from you

**Blocking (answer first):**

1. **Is `@holliewoodandvine` yours?** Instagram's pages are walled to my tools, so nobody has checked. Search the handle in the app. If it is taken, pick one name and claim it on every platform before posting anything.
   **Confirmed by Ricky 2026-11-08:** `@holliewoodandvine` is the shop's Instagram account.
2. **Is there, or will there be, a registered business entity?** It does not gate posting. It gates taking a Meta app Live (Business Verification, up to 14 business days; desk read 2026-10-12, not re-read) and so probably automatic comment replies on your own app, and a TikTok developer app. Without one, use third-party tools that hold Meta's approved app.
3. **Does Hollie approve every post, or only the exceptions?** Default I used: approve everything for the first 60 days, then exceptions only (prices, claims, faces, complaints, anything touching the rules). Approving by exception reverses the dashboard handoff's "no auto-publish" rule, so it needs your word.
4. **Hands only, voiceover, or Hollie on camera?** Default is hands-first. Evidence on faces is thin (`vendor claim`: vidIQ, n=500; a 2014 Instagram study); a mirror shot can show her by accident, and the shoot plan is built to avoid that.

**Soon:**

5. **The link rule (section 3) and one disclosure line.** A compliant automated DM carries an "automated message" line. Does that still count as "the link and nothing else"?
6. **"10% off each room after the first" is live on `site/hire.html:121` and in `docs/fabulous-from-online-design.md:87`.** It conflicts with your no-discounts rule. Keep or cut? I changed nothing.
7. **Drop day and time.** I used Wednesday 7 pm ET as a placeholder; it is a guess, not evidence.
8. **Is the iPhone 17 Pro the shop phone, and does Hollie shoot?** The walkthrough video's metadata says iPhone 17 Pro (iOS 26.5.1). That is a file, not proof.
9. **Gear spend:** $78.97 or $178.94, or none.

**Later:** may Claude install user-local tools on the Fedora box; is a small separate repo for the pipeline acceptable (a structure change); a $10-a-month Anthropic API key limit; the Screen Test calls recorded or published (call recording needs everyone's consent; Fla. Stat. 934.03(2)(d), flagged by w1g, not legal advice); prop or event rental, a market booth, Chairish; Apify (about $2 to $5) for measured competitor engagement, which I did not spend.

---

## 2. The rules every post follows

These are yours. Research pushed on three of them; each is flagged, none changed.

- No claims by DM or comment; the only call to action is the listing page. No bidding or claim-to-bid lives (Florida regulated-auction status unchecked). No discounts, no codes, "Absolutely no offers."
- No showroom language: never "visit", "in store", "our doors", "stop by", and no business-pin location tag. A city or region tag only, and Instagram names the location tag as a Feed signal (`verified`), so this is your call.
- Hollie is she/her. "Style," never "interior design." The mirror ball is "sometimes," never promised, and never framed as a giveaway: Instagram lists contest and giveaway promotion as not recommendable (`verified`, w1a).
- Real photos of real items only. AI for captions, cuts and layout around real photos is fine; no AI product imagery, no AI B-roll, no AI avatars. The editorial cutouts contain generated pixels and must not be used on a cover that sells a specific piece (w1e).
- Sold pieces say **Gone** and stay visible.
- No product-link post until real stock exists (the site's listings are samples with illustrative prices).

---

## 3. The link rule (the one conflict wave 1 found)

A URL typed in a public Instagram comment is **not tappable** (`vendor claim`, two tools; Meta's own page not read). So "reply LINK with the link" does not work as written. What does (w2d, recommended):

1. **Link in bio plus a piece number on every post.** The listing page answers the number. This always works and needs nothing.
2. **"Comment LINK" as an optional extra:** a public reply ("sent, check your DMs") plus a private reply or DM carrying only the listing URL. Needs a tool (below) or your own Live app. Limits: one private reply per comment, within 7 days, 750 an hour; it lands in Requests unless the commenter follows (`verified`, w2d). Whether "comment LINK" counts as engagement bait on Instagram is unstated (`need review`); check Account Status weekly.
3. **A link sticker on Stories**, added by Hollie on drop days. A human tap, always.
4. **Never gate the link behind a follow or a comment.** Meta's Spam standard bans like or share gating of exclusive content (`verified`, w2d).

---

## 3A. How to grow

Ranked by how well the evidence holds. Every line is from Instagram's own statements or a lane-verified source; none is a promise.

1. **Make reels people send.** Sends per reach is one of Instagram's three top signals, and slightly more important than likes for non-followers; watch time is the most important for both (Mosseri, 2025-01-21, transcript read). A reel that makes someone text it to a friend ("this lamp") beats one that earns a like.
2. **Clear the five gates to reach non-followers:** no watermarks, add audio (especially on carousels), 3 minutes or less, original, good account status (Mosseri, 2025-01-23). Photos and carousels fall under the originality rules from 2026-04-30. Your own photos and video count as original.
3. **Post enough, and keep one lane.** 10 or more reels a month (Instagram FAQ), 3 to 5 feed posts a week (Buffer study), and mix in carousels. Instagram says staying on a theme your audience already responds to earns similar distribution: lamps, pink glass, the burgundy room.
4. **Put the keywords where Search reads them:** the Name field, bio and captions (not comments), plus 3 to 5 niche hashtags (up to 5 allowed). Hashtags describe a post; they do not raise reach.
5. **Reply to comments within 7 days** (Instagram FAQ).
6. **Trial Reels once you reach 200 followers** on a professional account: they go only to non-followers first, so you can test hooks before your followers see them.
7. **Collab posts with adjacent accounts** (vintage dealers, stylists, designers) are an approved collaboration tool for originality (`verified`), but they cannot be scheduled, so post them live. Eligibility details were not read; the advice to pick adjacent, not competing, accounts is `inferred`.
8. **A Broadcast channel as the drop list** (text, video, voice, polls; no claims in it). Eligibility was not read; using it as the "tell me when the drop opens" list is `inferred`.
9. **Pinterest is the long-lead search channel** (plain Pins to real pages, live 4 to 6 weeks before a season); **Shorts mirror** the same cuts.
10. **A signup-only hunt list** (w1f, ranked first for your rules): collect emails or Broadcast followers for "find me a piece" requests before stock exists, with no listing link until it does.

**What no source gives:** a time to the first 1,000 followers or to steady sales. The nearest case is 7,100 followers in about 12 months (Halifax, 2019 to 2020), and the growth stories are mostly 2018 to 2021 winners. Anchor on nothing; use the four-week test in Appendix E and Instagram Insights.

---

## 4. Step by step

Each step: what, where, cost, time, who. Prices as read 2026-10-29.

### Phase 0: this week, no cost

1. Decide the four blockers above. Pick one name and spelling: **Holliewood and Vine** or **Holliewood & Vine**, used identically everywhere.
2. Check the handle in the Instagram app. Do the same for TikTok, Pinterest, YouTube.
3. Pick Hollie's drop day (placeholder only).

### Phase 1: accounts (about 1 hour, all free)

Do them in this order. Nothing here needs a legal entity or an ID check, as the pages state it.

| # | Account | Create it | Prerequisite, as stated | Notes |
|---|---|---|---|---|
| 1 | **Instagram, then Business** | https://www.instagram.com, then Profile > More > Settings and activity > For professionals > Account type and tools > Switch to professional account > Business ([Meta help](https://www.facebook.com/help/instagram/502981923235522)) | Age 13+. A private account becomes public | Facebook Page link is optional (skip it). Business is Meta's wording for retailers and service providers |
| 2 | **Facebook Page** | https://www.facebook.com > Pages > Create ([help](https://www.facebook.com/help/104002523024878)) | Any Facebook account | Not needed to post to Instagram through the API (w1a, w3d). Needed when you start Facebook posting; cross-posting from Instagram uses it |
| 3 | **Meta Business Suite** | https://business.facebook.com/latest | Facebook login | Free scheduling for Facebook and Instagram |
| 4 | **Pinterest Business** | https://www.pinterest.com, desktop only ([help](https://help.pinterest.com/en/business/article/get-a-business-account)) | An email not already used on Pinterest | Business needed to schedule Pins |
| 5 | **YouTube channel, then verify** | https://www.youtube.com, then https://www.youtube.com/verify ([help](https://support.google.com/youtube/answer/171664)) | Phone number for the verification code | Verification unlocks Shorts custom thumbnails (Studio on a computer only) |
| 6 | **TikTok, then Business** | https://www.tiktok.com | Phone, email or third-party login | **Create the account now to hold the handle; post from month 3.** Business gives the Commercial Music Library; scheduling is 10 days ahead on desktop (TikTok's old undated blog; 30 days is a snippet, `need review`) |
| 7 | **Threads** (optional mirror) | https://www.threads.com | Sign in with Instagram or Facebook | Cut-down mirror only |

**Not yet:** a Meta developer account and app (Tier C only; needs a phone and email code, https://developers.facebook.com/async/registration); Etsy and Shopify (separate project).

### Phase 2: set up the Instagram profile (30 minutes)

- **Name field and bio carry the search keywords.** Instagram Search matches handle, Name, bio, captions, hashtags and places; keywords in the caption count, in comments they do not (`verified`, 2021 Instagram post). A starting Name: "Holliewood & Vine | Vintage lamps & decor" (`inferred`). Never "interior design."
- **Link in bio:** the site's link-in-bio page (Codex builds it; see the handoff). Handle and link limits were not verified; do not count on a specific number.
- **Hashtags: up to 5 per post** (Help Center, `verified`); 3 to 5 niche tags, none generic.
- **Check Settings > Account status** weekly. It shows recommendation eligibility.
- **Audio:** open Audio in the Reels camera on the real account and see what appears. Meta's licensed library is "personal, non-commercial" and some business accounts lack it; the Sound Collection (14,000+ tracks) is commercial-safe (`verified`, w1a, w3c). The four Kevin MacLeod tracks already chosen in `docs/music-and-lights-notes.md` need a visible credit.

### Phase 3: the first shoot (90 minutes, one phone)

Full settings table, reflection rules and the 34-clip shot list: Appendix D. The essentials:

- **iPhone settings:** Settings > Camera > Formats > Most Compatible; 1080p at 30 fps (4K30 for hero clips you may crop); Auto FPS off; Lock White Balance on; HDR Video off; lock exposure on a mid-tone wall and dim the neon (`verified` settings, chosen values `inferred`).
- **Mirrors, glass and the mirror ball:** shoot off-axis, farther back, with black foam board where the reflection falls. This is what keeps Hollie and the phone out of frame.
- **One shoot makes the four weeks:** about 34 clips cover the Instagram posts, TikTok re-cuts and Pin stills (`inferred`; nobody has timed it).
- **Gear:** Kit A **$78.97** (desk mount $29.99, flexible tripod $25.99, bi-colour light $22.99) or Kit B **$178.94** on sale, $188.94 at list (adds overhead stand $44.99, 180 cm light stand $34.99, two RGB61 lights at $24.99 sale, $29.99 list). All six prices re-read 2026-10-29; the DS034 showed 3 in stock; free shipping banner over $50 (Florida shipping not tested). Links are in section 7. **Skip:** ring lights, softboxes, polarizers, any gimbal before month two. I dropped the gimbal: the $149 DJI price never existed on a DJI page.

### Phase 4: edit and post (the first four weeks)

- **Edit in Instagram Edits** (free; "4K, no watermark"; auto captions; iOS 16.3+; in-app purchases exist but their prices were not read). **Do not use CapCut's library music**: its Sounds are non-commercial only (`verified`, CapCut licence updated 2026-01-22). Export clean: no watermark, no letterbox, never re-upload a clip.
- **Cadence:** Instagram's FAQ says the greatest follower growth goes to accounts posting **10 or more reels a month**; Buffer's 2.1-million-post study says **3 to 5 feed posts a week** (`verified`/`study`, vendor). The old 4-week skeleton had 7 to 9 reels, so add 2 to 3 reels cut from the same footage. Carousels matter: a 21.6-million-post vendor dataset has carousels leading views at every follower tier (`vendor claim`, w1c). Add audio to every carousel (Instagram says so, `verified`).
- **Hooks:** 11 of 15 sampled reels put a text hook on screen by about 1 second, median 7 words; 9 of 15 had no speech (n=15, `inferred` pattern). 30 hooks, 12 series formats, caption formulas and 10 call-to-action lines that obey section 2 are in Appendix A.
- **Ranking, from Instagram itself:** watch time, likes per reach and sends per reach, with watch time most important for both followers and non-followers (Mosseri, 2025-01-21, transcript read). Five gates to be shown to non-followers: no watermarks, add audio, 3 minutes or less, original, good account status. Early reactions do **not** boost a post (`verified`).
- **When to post:** run the four-week test in Appendix E (16 posts, four slots, four formats). At zero followers it mostly measures noise, so treat it as a screen to retest. Trial Reels need 200 followers; Insights' "times your followers are active" needs 100.
- **Collab posts and product tags cannot be scheduled** (`verified`): post those live.

### Phase 5: covers

One 1080x1920 master with the key content inside x 90 to 990, y 420 to 1500; that survives the 3:4 grid crop and the 4:5 feed crop (crop numbers are `vendor claim`). Pinterest gets its own 1000x1500 file. Six templates with coordinates, type scale and contrast table: Appendix C. Two fixes before anyone builds it: template 1's top label sits at y 330, outside that safe square, and a blind `object-fit: cover` crop can keep the switch or a hanger in a lamp shot, so each listing needs a focal box. **Decisions:** the Gone stamp in site pink `#e5a6b4` (7.18:1 on burgundy) or sampled neon `#e33fa6` (3.8:1, large stamps only); Hollie's face yes or no; a lighter-ground Pin to A/B (one vendor set claims dark loses 38% of saves).

Click evidence is thin everywhere: no controlled Instagram or TikTok cover study exists in what I found. At this volume, rotate templates and trust only gaps of about 2x.

### Phase 6: the other platforms (about 1.75 to 2 extra hours a week for three)

| Rank | Platform | What to do | Gate |
|---|---|---|---|
| 1 | **Pinterest** | Plain Pins that link to real pages; keyworded boards; schedule up to 30 days ahead, 10 queued | Product Pins are not allowed for pre-owned goods (`verified`), and a real URL per piece does not exist yet. No Pins to sample listings. Seasonal Pins need to be live 4 to 6 weeks early (Pinterest's own rule) |
| 2 | **YouTube Shorts** | Same vertical cuts; custom 9:16 thumbnail in Studio on a computer | Verified channel. Shorts cannot be A/B tested. The best verified vintage-lamp numbers are here (Crazy Lamp Lady, 309K subscribers; one 72-second Short at 23,394 views), but from a reseller audience |
| 3 | **Facebook Page** | Native cross-post of what you post; no links in captions performs best (Meta's guidance) | A Page. Avoid third-party watermarks |
| 4 | **TikTok** | Month 3 | Business account for music. No lane for these goods in TikTok Shop; content only. Own-app posting is private-only (below) |
| Skip | Whatnot (auctions, lawyer), Poshmark, Depop, Lemon8, Facebook Groups (claims by comment), Marketplace except shipped checkout, Nextdoor except for Hire Hollie | | |

### Phase 7: add the scheduler (week 2)

**Buffer.** Sign up free: https://login.buffer.com/signup?product=buffer&plan=free&cycle=year.

- Free: 3 channels, 10 scheduled posts per channel, API (1 key) and MCP on the free plan. Essentials: **$5 per channel a month billed yearly, $6 billed monthly**; four channels is $20 or $24 (`inferred` from the per-channel rate). Team: $10 or $12 per channel.
- Reels yes (3 seconds to 15 minutes), carousels in the app, alt text on static images. **No custom cover upload**: only a frame pick. Workaround from Buffer's own help: bake the cover into the first frame. Own-API posting does support covers.
- Music on Posts and Stories, stickers, product tags and Story links fall back to a phone reminder, not an auto-post. Native approval workflow is Team only; the MCP leaves posts as drafts, so "you are always the last step."
- Channel pick on Free: Instagram, Pinterest, and one of TikTok or YouTube; Facebook can ride native cross-posting.

**Alternatives, compared honestly:**

| Option | Price (4 channels, 2026-10-29) | API / MCP | Why or why not |
|---|---|---|---|
| **Buffer** | $0 (3 ch) or $20 yearly / $24 monthly | API and MCP on every plan | Best fit for Claude and Codex |
| Postiz Cloud | $29 monthly, $23 yearly (5 channels, 7-day trial) | API, CLI, MCP on every plan | Strong open-source scheduler with a hosted tier. Self-hosting (9 containers) still needs your own Meta and TikTok apps and has open Instagram connect issues. Telemetry not assessed |
| Metricool Starter | "From $20" yearly, $25 monthly; rises with brands | MCP yes; API only on Advanced from $53 | Free tier is 20 posts a month (about 48 needed) |
| Publer | Free 3 accounts; paid per account (about $16 yearly for four, `inferred`) | API and MCP **Business only** | Needs the top plan for any Claude hookup |
| Zernio (formerly Late) | $12 for four accounts (usage-based) | API is the product | Newer; whether it runs on its own approved apps was not verified |
| Later, Hootsuite, Planoly | Trials or $14 and up | Not read | Skipped |

TikTok rule (w2c): unaudited apps post `SELF_ONLY`, and TikTok's guidelines name "a utility tool to help upload contents to the account(s) you or your team manages" as not acceptable. So public TikTok posting goes **through a scheduler that holds the approved app**, not your own app. **Untested:** whether Buffer Free actually publishes a public TikTok from a Business account is smoke test SA-1 in the handoff; Buffer's own posts guide omits TikTok while its MCP page includes it. Until SA-1 passes, post TikTok by hand in TikTok Studio.

### Phase 8: replies

**Month 1: by hand.** 30 comments a week is a few minutes. Use the reply wording in Appendix A (the "is this available?" and "price?" replies).

**Tools, when you want comment-to-DM:**

| Tool | Price | Verdict |
|---|---|---|
| **InstantDM Legend Pro** | $9.99 a month billed yearly (about $12 monthly, snippet). Free: 5 post automations, 500 DMs | Cheapest working option. API only on Trendsetter ($24.99 yearly) |
| **ManyChat Essential** | $14 a month billed yearly ($17 monthly, snippet). Free: 25 contacts, too few | Mature; API only on Advanced ($139) |
| CommentSold CommentChat | Bundled in Starter **$149 a month plus 6% of sales** | Worst fit: a live-selling and auction platform |

Both cheap tools hold Meta's approved app, so you need no entity of your own (their entity requirements were not checked). **None offers a draft-approval queue**, so "Hollie approves every reply" means your own pipeline or doing it by hand. Instagram's own Meta Business Agent (free since June 2026) advertises "Close sales" and breaks API sends when it owns a thread: do not turn it on. Unofficial libraries (instagrapi, instagram-private-api) risk a ban on your one brand account: no.

### Phase 9: automation (Tier C)

Build order by payoff (`inferred`, from w2g and w2e): 1. Claude drafts captions from a clip and one line (Haiku, banned-words lint). 2. Cover render. 3. The edit list and ffmpeg render. 4. The metrics sheet. 5. Own-API Instagram and Facebook publishing. 6. Reply drafts into an approval queue. The full spec, schema, smoke tests and corrections: `docs/codex-handoff-social-autopilot.md`.

### Phase 10: the weekly rhythm

| Day | What | Time |
|---|---|---|
| Shoot day (every 4 weeks) | 90-minute batch, share clips to the ingest folder | 90 min |
| Weekly | Approve the queued week (5 feed posts, 3 Pins, 3 Shorts); fix anything flagged | 30 to 45 min |
| Drop day | Add Story link sticker; reply to comments | 15 min |
| Monthly | Read Insights, Account status, the test sheet; refresh the calendar | 30 min |

---

## 5. What other vintage and designer accounts do

d1 already studied 12 vintage accounts (`research/round-d/d1-social-video.md`). The new lanes found:

- **Revenue split is unknown.** No survey divides vintage revenue between Instagram, marketplaces and an own site. The one dealer figure is Dobbin St. Co-Op: Instagram over 50% of revenue (Curbed, Feb 2021, a pandemic year, one shop). Growth stories are mostly 2018 to 2021 winner profiles; none gives time to the first 1K or to steady sales. Treat them as examples, not benchmarks.
- **Models that fit your rules, ranked (w1f):** a signup-only "hunt list" with no listing link until stock exists; a Vintage Market Days booth; Chairish if offers can be turned off (its Trade program's "up to 50% off" conflicts with no-discounts). Examples with evidence: an $85 lamp-wiring workshop sold out at a Philadelphia vintage shop (one case); a flipper reports 80% of income from YouTube and sponsors (one anecdote); antique-mall booths run a median $275 a month plus 7 to 15% at 21 of 35 malls (vendor with an app); four South Florida rental houses already exist. Prop and event rental needs your ruling on "no rentals in v1."
- **Designers and stylists (w1g):** every service seller I could read routes inquiries to its own site, not Instagram DMs; referrals lead and Instagram is portfolio and warm-up; two of three small designers have more Pinterest followers than Instagram. Your written Hire Hollie prices sit inside public bands, with two review items: Casting Call at $95 is under the $150 sourcing floor at two competitors, and nobody publishes a rush fee.
- **Funnel stack for Hire Hollie:** Cal.com Free + Stripe + Tally Free is $0 a month in subscriptions, but **each paid booking costs Stripe's 2.9% + 30 cents** (`verified`), and Cal.com and Tally keep their own branding on Free. Step up: Dubsado $35 or $55 a month, $335 or $525 a year; HoneyBook $29 a month billed yearly. Worth it past about four projects a month (`inferred`).
- **Google Business Profile** needs a service area (up to 20, about two hours of driving), so it fits only if Hollie really visits homes.
- **Show proof without clients:** her own corner, mood boards, the free Screen Test as content. Use a staged call until a lawyer reads the recording and likeness rules.

---

## 6. What the full pipeline costs, month by month

At the reference load: one brand, 5 Instagram and Facebook posts a week, 3 TikTok videos, 3 Pins, about 30 comments a week.

| Piece | Cost | Source and caveat |
|---|---|---|
| Claude drafting, Haiku 5.5 | About $0.27 a month ($2.69 at 10x) | $0.10 in / $0.50 out per million tokens, **only up to 100K-token prompts**; $0.50 / $2.50 above (`verified`). Sonnet 5.5 is $2 / $10. Set a limit at https://platform.claude.com/settings/billing |
| Media runner (GitHub Actions, private repo) | About $1.44 of the **$12 a month GitHub Free includes** | $0.006 a minute, about 240 minutes; the 2,000-minute figure is arithmetic. The runner has no ffmpeg preinstalled, so it installs it |
| Control plane (Supabase) | Free, or Pro from $25 | Free projects pause after 7 days of low activity; Edge Functions get 2 s CPU; Free storage is 50 MB a file. Whether a cron counts as activity is `need review`, so Pro is the safe choice |
| Notifications | ntfy free; Pushover $4.99 one-time per platform | Pushover has no action buttons; ntfy has `http` buttons (iOS support stated on its docs) |
| Scheduler for TikTok and Pinterest | Buffer $0 to $24 | Section 4, phase 7 |
| Own Meta app | $0 | Needs Business Verification only to go Live |
| Vercel | $0 if renders stay off it | Hobby is non-commercial; Pro $20 |
| **Approximate total** | **$0 to about $50 a month** | Plus the build hours in section 0 |

**Claude and Codex plans (for building):** Claude Pro $17 a month billed yearly ($20 monthly), Max from $100; ChatGPT Plus $20 with Codex, Pro from $100. Cloud scheduled tasks run hourly at most and draw on the subscription. `claude --bare -p` refuses subscription login; non-bare `claude -p` with a setup token is the documented subscription route. Anthropic's terms ask product builders to use API keys, so an unattended shop pipeline should use an API key with a limit (`need review` whether it counts as ordinary individual use). Max API credits do not cover Claude Code.

---

## 7. Every signup and price in one place

All read 2026-10-29. "Yr" is billed yearly; "mo" is billed monthly.

| What | Link | Price |
|---|---|---|
| Instagram Edits (iPhone) | https://apps.apple.com/us/app/edits-video-editor/id6738967378 | Free; in-app purchases, items not read |
| Buffer | https://login.buffer.com/signup?product=buffer&plan=free&cycle=year | Free; Essentials $5 yr / $6 mo per channel; Team $10 / $12 |
| Postiz Cloud | https://platform.postiz.com/auth | $29 mo, $23 yr; 7-day trial |
| Metricool | https://app.metricool.com/register | Free; Starter from $20 yr / $25 mo; Advanced from $53 yr / $67 mo |
| Publer | https://app.publer.com/users/sign_up | Free; Professional $4 yr / $5 mo; Business $8 / $10 (per-account basis is `inferred`, the slider was not captured) |
| Zernio | https://zernio.com/signup | 1 to 2 accounts free, 3 to 10 at $6 each |
| InstantDM | https://app.instantdm.com/signup | Free; Legend Pro $9.99 yr |
| ManyChat | https://app.manychat.com/signup/facebookAuth?channel=instagram | Free; Essential $14 yr |
| Canva | https://www.canva.com/pricing/ | Free; Pro $144 yr ($12 a month) or $18 mo |
| Anthropic API console | https://platform.claude.com/ | Haiku 5.5 $0.10 / $0.50, Sonnet 5.5 $2 / $10, Opus 5.5 $4 / $20, Fable 5.1 $10 / $50 per million tokens |
| Claude | https://claude.com/pricing | Pro $17 yr / $20 mo; Max from $100 |
| Codex / ChatGPT | https://developers.openai.com/codex/pricing | Plus $20; Pro from $100; Go $8 |
| Supabase | https://supabase.com/pricing | Free; Pro from $25 |
| GitHub Actions | https://docs.github.com/en/billing/concepts/product-billing/github-actions | Free includes $12 a month for private repos |
| Cloudflare R2 | https://developers.cloudflare.com/r2/pricing/ | 10 GB, 1M and 10M operations free; then $0.015 per GB-month |
| Vercel | https://vercel.com/pricing | Hobby $0 (non-commercial); Pro $20 |
| ntfy | https://ntfy.sh/ | Free; Supporter $5 yr / $6 mo |
| Pushover | https://pushover.net/pricing | $4.99 one-time per platform |
| PhotoSync (iPhone) | https://apps.apple.com/us/app/photosync-transfer-photos/id415850124 | Premium $6.49 yr / $0.99 mo; lifetime $24.99 (SKU `need review`) |
| rclone | https://rclone.org/ | Free |
| Cal.com | https://cal.com/pricing | Free; Teams $12 per user yr |
| Stripe | https://stripe.com/pricing | 2.9% + 30 cents per card payment |
| Tally | https://tally.so/pricing | Free; Pro about $24 yr / $29 mo (`inferred`) |
| Dubsado | https://www.dubsado.com/pricing | $35 / $55 mo; $335 / $525 yr |
| HoneyBook | https://www.honeybook.com/pricing | $29 / $49 / $109 yr |
| Neewer gear | [DS034](https://www.neewer.com/products/neewer-basics-ds034-camera-desk-mount-stand-with-c-clamp-phone-holder-66610105), [TP34](https://www.neewer.com/products/neewer-tp34-flexible-phone-tripod-66610307), [NL-36AI](https://www.neewer.com/products/neewer-nl-36ai-camera-soft-light-66600903), [DS026](https://www.neewer.com/products/neewer-ds026-overhead-phone-tripod-stand-66609390), [ST180B](https://www.neewer.com/products/neewer-basics-st180b-180cm-photography-light-stand-66609099), [RGB61](https://www.neewer.com/products/neewer-rgb61-cri-97-rgb-video-light-360-full-color-led-camera-light-with-3-cold-shoe-66600609) | $29.99, $25.99, $22.99, $44.99, $34.99, $24.99 sale ($29.99 list) |
| Meta developer account (Tier C) | https://developers.facebook.com/async/registration | Free |

---

## 8. The calendar, in three lines

Full table with gates is Appendix B. **November is a setup month**: Pinterest asks for seasonal Pins 4 to 6 weeks early, so a new account opened in November misses Christmas. **Valentine's is the first moment you can hit on time** (Pins live Dec 20 to Jan 3). Verified dates: USPS lower-48 send-by dates Ground Advantage Dec 17, Priority Dec 18, Express Dec 19; Design Miami Dec 1 to 6, Art Basel Miami Beach Dec 4 to 6; Palm Beach Show Feb 11 to 16, 2027; Salone del Mobile Apr 13 to 18; High Point Market Apr 10 to 14 and Oct 23 to 27. Search demand for lamps is winter-high and spring-low (Jan to Feb beat Apr to Jun in each of four years, by 12 to 32%); disco ball peaks in December (US weekly Google Trends, small-number data). Pinterest Predicts 2026 names "Neo Deco," which fits the room (`vendor claim`); the 2027 edition is expected around Dec 9, 2026.

---

## 9. Open conflicts and tests

**The Meta entity question (w2d vs w2c, arbitrated by w3d).** Meta's own pages contradict each other.

| Operation (your own account) | Without a legal entity |
|---|---|
| Publish Reels, carousels, Stories | **Yes.** Standard Access, App Review "not required" (`verified`). Test posts in Development mode are visible to role users only |
| Reply to, hide, delete a comment | Yes at Standard Access, but each needs a comment ID |
| Read customers' comments by polling | **Unclear.** No page says non-role commenters' text is withheld or returned |
| Webhooks for customers' comments | **Leaning no.** Setup page: the app must be Live, Advanced Access, and Business Verification "required for production access"; the create-app page requires a Business-Verified business "before you can publish your app" |
| Private reply or DM | **Unclear.** Three Meta pages disagree on Standard Access |
| Counter-quote (Business Verification page) | "If your app will only be used by app users who have a role on the app itself you do not need to complete verification ... all features are always active." |

One hour settles it: a throwaway Meta app, a tester account and one non-tester commenting account (nine steps, `research/social-2026-10-29/w3d-meta-arbiter.md`). **The desk wiki line "our own pages need no review" is true for posting and contested for comment webhooks until the one-hour test; the wiki page will say that, not "wrong".**

**Other tests worth an afternoon:**

1. One real export from your own pipeline and from Edits posted to a throwaway account, to see whether Instagram adds an "AI info" label (Meta's own page says it cannot yet detect other companies' video AI signals, dated 2024, may be stale). Generative fill or upscalers that stamp provenance metadata could label real photos.
2. Share one fresh phone clip through Drive, pull it with rclone, and check its resolution. The only clip seen through Drive was 568x320 and nobody knows whether Drive or the download shrank it. If it fails, PhotoSync to SFTP is the fallback.
3. Open Audio on the real Business account to see whether the licensed library appears.
4. One test upload to settle YouTube: the live page (updated 2026-10-15) says unverified projects are not private-locked and uploads cost 1 unit; older mirrors say otherwise.
5. Create one draft through Buffer's MCP from Claude.

**Other open items:** whether "comment LINK" is engagement bait on Instagram; whether the Instagram API limit is 50 or 100 posts a day (plan for 50); how much the Postiz telemetry matters (HyperFrames collects telemetry by default; `hyperframes telemetry disable` turns it off); the BtbN ffmpeg daily tag `autobuild-2026-10-28-19-47` is pruned around 2026-11-11, so pin the month-end tag (`autobuild-2026-09-30-13-08`, SHA-256 digest in w3b) or mirror the tarball by checksum.

**Local tools that already work on the Fedora box without sudo:** a pinned static ffmpeg decodes iPhone H.264 and HEVC (two lanes tested it independently; 4K to 1080p with a burned caption in 9.1 s; a 10.5-second edit-list render in 20 to 31 s, 6 s at `veryfast`); output carries no GPS, Apple, C2PA or XMP tags in our own code path; an HTML cover renders to 1080x1920 and 1000x1500 in 1.7 s. The Fedora box was off the network from 2026-09-26 to 2026-09-29, so treat it as best-effort. Windows ffmpeg and a GitHub runner are the fallbacks.

---

## 10. Things I would change in the repo (none done)

1. `site/hire.html:121` and `docs/fabulous-from-online-design.md:87`: the 10% multi-room line (decision 6).
2. Cover template 1's top label (y 330) and the per-listing focal box (Appendix C).
3. The desk wiki page `Chief Of Staff/wiki/social-comment-ai.md`: "our own pages need no review" holds for posting; for comment webhooks it is contested until the throwaway-app test.
4. The 4-week skeleton in `research/round-d/d1-social-video.md`: add 2 to 3 reels and carousels (cadence).
5. If approval mode B is chosen, `docs/dashboard-handoff.md`'s "no auto-publish" rule.
6. Pages the posts point to: piece-number pages (`/p/<n>`), a link-in-bio page, a sold archive (Codex builds these; handoff).

---

## 11. X verified, Y need review

- Instagram scheduling: 25 posts a day, 30 days ahead, any public account (Help Center, verified) vs 75 days, professional only (a 2022 snippet).
- Hashtags: up to 5 (Help Center, verified) vs 30 (older snippet of the same article).
- Instagram API publish limit: 50 (endpoint reference) vs 100 (guide).
- Posting time: five studies disagree by up to 16 hours; Instagram says audience-awake time matters and early reactions do not boost.
- TikTok scheduling: 10 days (TikTok's old blog, undated) vs 30 (snippet).
- Buffer carousels: up to 10 images (marketing page) vs 20 (help article). Buffer "Custom video covers" (pricing page) vs "can't upload a separate image" (help): probably the frame picker.
- Pinterest bottom margin: 790 px organic and 440 px ads, both verified, need review.
- Satori: README says WOFF2 and Grid work; the Vercel OG docs say no. Unresolved.
- CapCut yearly: $89.99 (App Store) vs $179.99 (capcut.com, "reference only").
- Tally Pro $24 vs $29 is probably yearly vs monthly (`inferred`).
- The Meta webhook, polling and private-reply questions in section 9.
- "Sends weigh 3 to 5x likes" and "watch time 35%, saves 25%, DM shares 20%" have no primary source: discard.

## 12. Source index

Lane reports in `research/social-2026-10-29/`: w1a Instagram rules and timing; w1b other platforms; w1c hooks (n=15 reels); w1d audience and calendar; w1e covers; w1f dealers; w1g designers; w1h capture and ingest; w2a editing; w2b cover automation; w2c publishing APIs; w2d replies; w2e GitHub scan; w2f Hugging Face scan; w2g runtime; w3a to w3d live re-checks. Raw captures are in `raw/`. Earlier work: `research/round-d/d1-social-video.md`, `docs/round-d-synthesis.md`, `Chief Of Staff/wiki/social-comment-ai.md`.

**What this research could not reach:** Instagram and TikTok profile pages, the Instagram terms page, Meta's Business Verification help pages, and any measured engagement for the accounts studied (the only engagement numbers are 19 reels read through `clipfeed`). Measured data would need Apify (a few dollars), which I did not spend.
