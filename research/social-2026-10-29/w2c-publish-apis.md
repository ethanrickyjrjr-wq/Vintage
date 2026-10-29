# w2c: publish stage, three paths per platform (Holliewood & Vine)

Lane w2c-publish-apis. Accessed 2026-10-29. Raw captures: `research/social-2026-10-29/raw/w2c-*.md` (41 kept). Budget used: crawls 45 of 45 (4 dead captures deleted), WebSearch 16 of 20 (WebSearch tool, standard mode), gh 5 of 10, no tests run, no logins, no signups.

Tags: **[V]** verified on the live page this session. **[VC]** vendor claim. **[SN]** unverified search snippet. **[I]** inferred. Meta dev docs are API v26.0.

Reference load (BRIEF2): 5 IG/FB posts a week, 3 TikTok videos a week, 3 Pins a week. Per month that is about 22 IG, 22 FB (via IG cross-post), 13 TikTok, 13 Pins. Pricing assumes 4 channels: IG, FB Page, TikTok, Pinterest. YouTube Shorts is an optional 5th.

---

## TL;DR

1. **The own-API path works for Instagram, Facebook, Pinterest, YouTube and Threads on Ricky's own accounts without a legal entity, and is dead for public TikTok.** TikTok's guidelines list "a utility tool to help upload contents to the account(s) you or your team manages" as **not acceptable**; unaudited clients post `SELF_ONLY` only, to private accounts, 5 users per 24 h. [V] T2
2. **Instagram own-API recipe:** Instagram Login, a **Business-type** Meta app kept in **Development mode**, the account added under roles, Standard Access, no App Review, no Facebook Page, no business portfolio. [V] M4 M6 M7. Going **Live** needs a Business-Verified business (legal entity). [V] M6
3. **Instagram API has no schedule field.** Containers expire after 24 h, so a cron must create and publish at post time. [V] M1. Facebook Pages **do** schedule server-side (`scheduled_publish_time`, 10 min to 30 days). [V] M8. YouTube schedules with `status.publishAt`. [V] Y1
4. **Instagram limit: 50 per 24 h on the endpoint reference ("currently 50"); the guide says 100.** Plan for 50 and read `content_publishing_limit` live. 400 containers per 24 h. The reference load is about 1 a day, so this changes nothing. [V] M3 M1
5. **Buffer is the strongest paid-or-free scheduler for Claude/Codex:** API and an MCP server on **every plan including Free** (1 key); Free = 3 channels, 10 scheduled posts each. Essentials is $5 per channel per month billed yearly. [V] B1 B2. Its API shows `metadata.thumbnailOffset` (a frame), not a custom cover image. [V] B3
6. **YouTube contradicts the old rule.** The live `videos.insert` page (updated 2026-10-15) says unverified projects are **not** restricted to private and puts uploads in their own bucket: 100 calls a day, 1 unit each. Search snippets and the google.cn mirror still carry the 2020 private-lock and 1,600 units. [V live vs SN stale] Y1 Y2. The real YouTube gate is the OAuth consent screen: "Testing" status expires refresh tokens in 7 days. [SN]
7. **Pinterest own-API works for one user:** Trial access makes Pins visible only to the creator; Standard access needs a demo video of the OAuth flow, and Pinterest says a sole user still must supply it. [V] P1
8. **Self-hosted Postiz/Mixpost escape no gate.** Postiz self-host needs your own Meta app (public apps need business verification) and your own TikTok app. Postiz **Cloud** ($29/mo) is path 2. Mixpost Lite publishes only to Facebook Pages, Mastodon, X. [V] PZ MX
9. **Cheapest drivable unified API:** Zernio (formerly Late; getlate.dev redirects) about $12/mo at 4 accounts [V pricing page; rebrand SN]. SocialClaw (already wired as `ecc:social-publisher`) is $29/mo at 6 accounts. Ayrshare Premium is $149/mo. [V]
10. **Recommendation:** start Tier B on Buffer Free (day one, $0, 3 channels, FB rides the IG cross-post), build own IG/FB API (Tier C) when the cover pipeline needs `cover_url`, keep TikTok on a scheduler or native. Every "public TikTok auto-publish" claim by a scheduler is a **vendor claim** needing a logged-out smoke test.

---

## 1. Per-platform decision matrix (three paths)

| Platform | Path 1: native | Path 2: third-party under its approved app | Path 3: own API app | Verdict |
|---|---|---|---|---|
| **Instagram** (Reels, carousels, Stories, covers, alt text) | In-app scheduling: any public account, 25 a day, 30 days ahead; **no collab posts or product tags on scheduled posts**; free [V w1a] | Buffer: auto-publish posts (carousel to 20), Reels (incl. Trial Reels, collaborators up to 3, first comment, music), Stories (up to 10 items, no text/links/stickers). Stickers, Story links, post music, product tags force "Notify Me" (you tap in IG) [V B4] | Instagram Login, Business-type app, Dev mode. $0. Needs own cron + public media URL. Full parameter set in section 2 | Path 3 for covers/alt text/collabs; Path 2 (Buffer) to start; Path 1 as fallback |
| **Facebook Page** | IG-to-FB cross-post toggle (stories, posts, reels) [V w1b]; Business Suite scheduling window **not stated** by Meta page (blogs: 29 to 30 days, some say 75) [SN] | Any scheduler; Buffer charges per channel [V] | Page access token + `pages_manage_posts` (+ `publish_video` for video); `published=false` + `scheduled_publish_time` 10 min to 30 days [V M8]. Server-side scheduling, no cron | Path 1 (cross-post) is free and enough; Path 3 only if FB-specific copy is wanted |
| **TikTok** | TikTok Studio desktop: 15 min to 10 days ahead, Business Account [V d1/w1b]; no trending sounds for business accounts (Commercial Music Library only) [V w1b] | Buffer "straight to TikTok" auto-publish; Business-account requirement **conflicts** across Buffer pages [SN]; trending sounds cannot be added via API [SN]. Upload-Post, Blotato, Postiz Cloud, Zernio, SocialClaw, Ayrshare claim TikTok through their own app [VC] | **Blocked for public posting**: unaudited = `SELF_ONLY`, private account, 5 users/24 h; intended-use rule names our exact case "not acceptable"; app review: "Apps must not be for private or personal use"; apps in development/testing not approved; sandbox has no public Content Posting [V T1 T2 T4 T6 T3] | Path 1 or 2 only. Inbox/draft upload (`video.upload`, you finish in TikTok app) still needs an approved app: gap |
| **Pinterest** | Business account; 30 days ahead, 10 queued [V d1] | Buffer, Later, Publer, Metricool, Zernio, Postiz list Pinterest [V pricing pages]; Pins need a real URL per piece [V w1b] | Business account, request Trial (email decision), then Standard via OAuth demo video [V P1 P2]. Scheduling parameter not read: assume cron [I] | Path 1 first (1 h/wk); Path 3 viable later at $0 |
| **YouTube Shorts** | Studio: date, time, zone; private until then [V w1b]; Shorts custom thumbnail needs Studio on a computer [V w1e] | Buffer, Later, Publer, Zernio, SocialClaw, Upload-Post list YouTube [V] | `videos.insert` scope `youtube.upload`, 100 calls/day, `status.publishAt`; consent screen must be In production (7-day token expiry in Testing) [V Y1, SN] | Path 1 now; Path 3 optional, 4 h build |
| **Threads** | App scheduling up to 75 days [SN w1b] | Buffer, Later, Metricool, Postiz list Threads [V] | `threads_content_publish`; without Advanced Access you can post for your own **Threads testers** only, which covers Ricky. Carousels 2 to 20. No schedule field read: cron [V M9, I] | Skip until Pinterest and Shorts run |

### 1.1 Instagram API fields that decide between paths [V M1 M2 M3]

| Need | Own API | Buffer API | Native app |
|---|---|---|---|
| Custom Reel cover image | `cover_url` (JPEG, 9:16, 8 MB; wins over `thumb_offset`) | only `metadata.thumbnailOffset` (frame, ms) shown on its video example | yes, manual |
| Frame as cover | `thumb_offset` (ms) | `thumbnailOffset` on Instagram, TikTok, Pinterest | yes |
| Alt text | `alt_text`, 1000 chars, **images and carousel images only; not Reels or Stories** | `metadata.altText` per image (required whenever image metadata is set) | yes |
| Carousel | up to 20, JPEG only for images, first image sets crop | up to 20 images+video mixed [V B4] | yes |
| Collab posts | `collaborators` up to 3 (feed image, Reels, carousels; **not Stories**) | up to 3 on posts and Reels [V B4] | **not on scheduled posts** |
| Trial Reels | `trial_params.graduation_strategy` = `MANUAL` or `SS_PERFORMANCE` | Trial Reel toggle [V B4] | yes (200+ followers, w1a) |
| Stories | image/video Story containers; **no link/poll/location stickers** | auto only without text/links/stickers; else Notify Me | in-app only |
| Music | `audio_name` renames **original audio only** | music on Reels automatic; on posts/Stories Notify Me | yes |
| Location | `location_id` (a Page ID with location data) | yes | yes |
| AI label | `is_ai_generated` (not on carousel children) | not read | n/a |

Rules from this table for the manual: (a) **w1e's designed covers can ship only through the own API (`cover_url`) or by burning the cover into the video's first frame and pointing the offset at it** (flag to w2b); (b) collab drops need the API, a scheduler, or live posting; (c) a Story link sticker is a human tap on every path (flag to w2d); (d) omit `location_id` (conflicts with "no showroom language"); (e) never set `is_ai_generated` on real photos; (f) the API needs media on a **public HTTPS URL** at publish time, and Buffer does too ("asset url must point to a publicly accessible file") [V B3], so a public bucket is required on every API path (cost and hosting: hand to w2g); (g) images must be JPEG; Reels MP4/MOV, H.264/HEVC, AAC, 23 to 60 fps, 3 s to 15 min, 300 MB, up to 1920 px wide; Story video 3 to 60 s.

### 1.2 Gates by path

| Gate | Native | Scheduler (their app) | Own app |
|---|---|---|---|
| Legal entity | no | no | IG/FB/Threads/Pinterest/YouTube: **no** while in Dev mode/Trial/Testing; Meta Live mode: yes (Business Verification) [V M6]; TikTok: moot (intended-use rule) |
| App review / audit | no | held by vendor [VC] | IG own-account Standard Access: none [V M7, SN Meta App Review page]; Pinterest: Trial review + Standard demo [V]; TikTok: audit, would be rejected [V]; YouTube: audit form for quota/restriction, status unclear [SN] |
| Business portfolio | no | no | Unified Login: required; **Instagram Login: not required** [V M7] |
| Facebook Page | no | FB posting only | IG: not needed; FB posting: needed |
| Token upkeep | none | vendor | IG: 60-day token, refresh only when at least 24 h old and unexpired, **a lapse is unrecoverable** [V M5]; Pinterest ~30-day access/365-day refresh sample [SN P-scopes]; Google 7-day in Testing [SN]; TikTok user token up to one year [V T3] |

---

## 2. Schedulers and unified APIs: price at the reference load, API, MCP

All prices read on the vendor page 2026-10-29 unless tagged. "Drivable" = Claude Code/Codex can run it by REST, CLI or MCP (Codex speaks MCP and shell [I]).

| Tool | Stage | Plan used and price | Free tier / caps | API | MCP | Notes |
|---|---|---|---|---|---|---|
| **Buffer** | publish | Free $0; **Essentials $5/mo per channel, $60/yr billed yearly** (4 channels = $20/mo); Team $10 per channel [V buffer.com/pricing] | Free: 3 channels, 10 scheduled posts per channel, 100 ideas | GraphQL `https://api.buffer.com`, key on **all** plans: Free 1 key, 1,000 req/channel/mo up to 3,000; limits 150 per 15 min, 600 per 24 h [V buffer.com/api] | yes, on all plans (limits shared with API) [V] | Drafts supported (`Create Draft Post` example); "Official API partner with Meta, LinkedIn, X" [VC]; Notify-Me push needs Buffer phone app |
| **Metricool** | publish+analytics | Free $0; **Starter $20/mo** (priced per brand, so one flat fee for all channels; billing period not shown in capture); Advanced $53 [V] | Free: 1 brand, **20 posts/mo** (does not fit 70/mo) | REST on Advanced only [V] | **MCP listed on Free**; works with Claude Code, ChatGPT, n8n, Make [V page, SN detail] | Free MCP cannot carry the load; Starter is the floor |
| **Publer** | publish | Free; paid numbers did **not render** in the crawl. Third-party snippets: Professional ~$5/mo (first account) + ~$4 per extra, Business ~$10 + ~$7 per extra [SN] => ~$17 and ~$31 at 4 accounts | Free: 3 accounts, 10 scheduled per account | "Access to Publer API & MCP" listed under **Business** [V] | official MCP described as beta for ambassadors/enterprise [SN]: need review | Cheap per account; API gated to Business |
| **Later** | publish | Starter **$18.75/mo billed yearly**, 1 social set (IG, FB, Threads, Pinterest, TikTok, LinkedIn, YouTube, Snapchat), 30 posts per profile per month; Growth $37.50 [V] | no free plan, 14-day trial | not found on pricing page | not found | Not drivable on what was read |
| **Hootsuite** | publish | Standard "starts at $99"/mo, 10 accounts, 14-day trial [V] | none | not read | "MCP connectors" under Wisdom AI [V mention] | Overpriced for one brand |
| **Planoly** | publish | paid from $14/mo, free 10 uploads/mo [V d1, not re-read] | | not read | not read | |
| **Zernio (was Late, getlate.dev)** | publish API | first 2 accounts free, then **$6 per account/mo** => 4 accounts **$12**, 5 **$18** [V zernio.com/pricing]; rebrand [SN] | Build plan $0 base, unlimited posts | REST, "every feature on every account" [V] | yes, docs.zernio.com/mcp [V link] | Trustpilot reports big post-rebrand price rises for old customers [SN] |
| **SocialClaw** | publish API | Starter 3 accounts/200 posts $15/mo (7-day trial); **Startup 6 accounts/400 posts $29/mo**; Plus 20/1,000 $67 [V getsocialclaw.com/pricing] | | REST, CLI, skill | **MCP, 18 tools** [V] | Backs installed `ecc:social-publisher`; skill pins npm `socialclaw@0.1.12`; covers X, LinkedIn, IG, FB, TikTok, YouTube, Pinterest [V] |
| **Blotato** | publish+AI | **Starter $29/mo**: 20 accounts, API, n8n/Make nodes, up to 900 TikTok posts/mo, 1,000 DM/comment-reply contacts [V]; Creator $97 | 7-day trial **excludes API and MCP** [V] | yes | yes (FB, IG, TikTok, YT pages) [V] | Bundles AI image/video credits |
| **Upload-Post** | publish API | Free 10 uploads/mo, 2 profiles (TikTok **not named** on Free list); **Basic $16/mo billed annually ($192/yr)**, unlimited uploads, 5 profiles [V] | | REST (`api.upload-post.com`), n8n/Make/Zapier guides | agent pages for Claude/ChatGPT [V link] | "Our app is verified... adheres to their reviews and audits" [VC] |
| **Ayrshare** | publish API | Premium **$149/mo** billed monthly, 1 profile; Launch $299 [V] | 28-day trial on Launch only | yes | MCP server [V link] | Priced for SaaS builders |
| **Postiz Cloud** | publish | Standard **$29/mo** (5 channels; $23 annual), Team $39/10 ch [V] | 7-day trial | public API + webhooks | **hosted MCP + CLI on every plan** [V] | Path 2 |
| **Postiz self-host** | publish | $0 license, AGPL-3.0, 40,086 stars, pushed 2026-10-28 [V gh] | | yes | yes | **Path 3 in disguise**: you create your own Meta app (public apps need business verification) and TikTok app [V docs.postiz.com] |
| **Mixpost** | publish | Lite free MIT (3,883 stars, last push 2026-03-16 [V gh]); Pro $299 one-time [V] | | | | Lite posts only to FB Pages, Mastodon, X: no Instagram [V] |
| **Repurpose.io** | auto-repost | Starter **$35/mo monthly** ($349/yr), Pro $79 [V] | 14-day trial | | | Reposts existing videos; not a calendar |
| **Zapier / Make / n8n** | glue | Snippets only: Zapier free 100 tasks (2-step), Pro $19.99/750 tasks; Make free 1,000 ops, Core ~$9; n8n Cloud ~$20 to $24/mo for 2,500 runs, self-host free [SN]. n8n repo license reads NOASSERTION on gh [V], 209K stars | | Zapier "Instagram for Business": Publish Photo(s) incl. carousels, Publish Video as Reel; Make: "Create a photo post", "Create a reel post"; photos need a public URL, Facebook login [SN] | Metricool/Postiz/Blotato plug into them | Triggers poll (delay); Zapier MCP calls cost 2 tasks [SN]. Neither read on vendor pages |

**What the three-way split says:** Buffer, Later, Publer, Metricool, Hootsuite, Planoly, Postiz Cloud, Zernio, SocialClaw, Blotato, Upload-Post, Ayrshare are all path 2 (their app, their audits [VC]). Postiz/Mixpost self-host, n8n or a hand-rolled Deno job on our own Meta app are path 3.

### 2.1 Unofficial APIs (listed because Ricky will see them; **not recommended**)

| Tool | Facts | Risk |
|---|---|---|
| instagrapi (subzeroid) | 7,040 stars, pushed 2026-10-28, license NOASSERTION [V gh] | Reverse-engineered private API: **ToS violation, ban/lock risk to the only brand account** |
| instagram-private-api (dilame) | 6,488 stars, MIT, last push 2024-08-09 [V gh] | Same, plus stale |
| Cookie/session "posters", rotating-IP bots | Upload-Post says it uses none [VC] | Same; do not test |

---

## 3. Recommendation, three tiers

| Tier | What | Cost/mo at reference load | Human must still |
|---|---|---|---|
| **A. Native free** | IG in-app scheduler (30 days, 25/day) + IG-to-FB cross-post + TikTok Studio (desktop) + Pinterest scheduler + YouTube Studio | $0 | Upload and schedule on 4 to 5 surfaces by hand; Claude only drafts captions/files. Approve mode A only |
| **B. One paid scheduler** | **Buffer.** Free tier first: IG + TikTok + Pinterest as the 3 channels, FB via cross-post, schedule in 2-week batches so each queue stays at or under 10. Upgrade to Essentials when you want FB or YouTube as channels or no queue cap | **$0 now; $20 (4 ch) to $25 (5 ch) billed yearly** | Account setup, OAuth, phone for Notify Me. Mode A: pipeline creates **drafts**, Ricky taps. Mode B: pipeline schedules directly; Stories with stickers and anything in the always-human list stay on Notify Me |
| **C. Own API pipeline** | Deno/Supabase cron on our own Meta app (IG, FB), Pinterest app, YouTube app, Threads; TikTok stays on Buffer/native | $0 vendor + public media bucket (w2g) | Create the apps, click OAuth, add Instagram tester role, record the Pinterest demo, publish Google consent screen, monitor token refresh. Mode A: web/Telegram approval before cron fires (w2g) |

**Why Buffer first:** API + MCP free; carries collab, Trial Reels, first comment, Story media; holds the TikTok/Pinterest app approvals we cannot get [VC]. **Loses when:** you need a designed `cover_url`, alt text on Reels is irrelevant anyway, or you want zero third-party token custody. **Hybrid I would build (inferred):** Buffer for TikTok + Pinterest + fallback; own API for IG/FB once the cover pipeline (w2b) exists. **Runner-ups:** Metricool Starter $20 flat if you want one price for any number of channels and analytics in the same tool; Zernio $12 or SocialClaw $29 if you want an API-first backend (SocialClaw already has the installed skill).

**Always human in either mode (BRIEF2):** prices, claims about condition/age/provenance, anything about a person, replies to complaints, anything touching the fixed constraints, Story link stickers, `is_ai_generated` decisions, going Live on Meta.

**Safe for the main account:**

| Path | Safety |
|---|---|
| Native | safest |
| Established scheduler (Buffer, Metricool, Publer, Later) | official OAuth APIs [VC]; risk is token custody, not bans |
| Newer unified APIs (Zernio, SocialClaw, Blotato, Upload-Post, Ayrshare) | official OAuth [VC]; smaller vendors, test on a throwaway account first (Ricky decides) |
| Own API on own account | official API, our token; risk is a lapsed 60-day token or Dev-mode surprises |
| Unofficial libraries | not safe |

---

## 4. Setup steps in dependency order

**Shared first (all tiers):** (1) claim handles and create accounts; (2) switch Instagram to Business (Professional) [w1a]; (3) TikTok to Business Account (needed for desktop scheduling) [V d1]; (4) Pinterest Business account; (5) a Facebook Page only when Facebook posting starts [V M7].

**Tier B (Buffer), about 1 to 2 h:**
1. Sign up: https://login.buffer.com/signup (Free).
2. Connect IG, TikTok, Pinterest (3 channels); leave "Enable Notifications by default" off [V B4].
3. Generate a key: https://publish.buffer.com/settings/api (docs https://developers.buffer.com).
4. Add the MCP server to Claude Code/Codex; store the key in the desk `.env`, then project `.env.local`.
5. Host media on a public HTTPS URL; test `createPost` with `schedulingType: automatic`, `mode: customScheduled`, `dueAt` ISO UTC [V B5].
6. Smoke-test (section 6).

**Tier C, Instagram, about 8 to 10 h:**
1. https://developers.facebook.com/apps: create app, use case **Other**, type **Business**; skip connecting a business for now [V M6].
2. Add the **Instagram** product, "API setup with Instagram login"; add the IG account (must be public) under roles/Instagram testers and accept the invite in the Instagram app [V M6, SN].
3. Permissions `instagram_business_basic`, `instagram_business_content_publish` [V M2].
4. App Dashboard, "Generate token": long-lived, 60 days [V M4]. Store in Supabase secrets.
5. Weekly job: `GET https://graph.instagram.com/refresh_access_token?grant_type=ig_refresh_token&access_token=...` (token at least 24 h old, unexpired) plus an alert if it fails [V M5].
6. Publish flow: `POST graph.instagram.com/v26.0/<IG_ID>/media` (`media_type=REELS`, `video_url`, `caption`, `cover_url`, `collaborators`, `share_to_feed`), poll `status_code` once a minute up to 5 minutes, then `POST /media_publish`; check `/content_publishing_limit` first [V M2].
7. Trigger from GitHub Actions cron / Supabase `pg_cron` / Vercel Cron at the post minute (container expires at 24 h) [V M1].
8. Wave-3 smoke test: publish once, open it logged out (see section 5, item 8).

**Tier C, Facebook Page (+3 h):** same app can serve FB (Postiz notes IG and FB share one app [V]); Facebook Login for Business, Page token, `pages_manage_posts`, `publish_video`; set `published=false`, `scheduled_publish_time` [V M8].

**Tier C, Pinterest (+4 h plus review wait):** https://developers.pinterest.com/apps/ : business account, verify email, accept terms, "Connect app" (name needs 3+ Latin letters, cannot contain "Pinterest"), working privacy-policy URL, request Trial; build OAuth; then **Upgrade** with a screen recording of the OAuth flow and one API call; Trial Pins are sandbox/creator-only until then [V P1 P2].

**Tier C, YouTube (+4 h):** Google Cloud project, enable YouTube Data API v3, OAuth consent screen, scope `youtube.upload`, **publish the screen to Production** (Testing expires refresh tokens in 7 days [SN]); upload with `status.publishAt`, `selfDeclaredMadeForKids`, `containsSyntheticMedia=false`; watch quota at https://console.cloud.google.com/iam-admin/quotas [V Y1 Y2]. Do one unlisted test upload to see whether the project is private-locked.

**Tier C, TikTok:** do not build. If ever wanted: https://developers.tiktok.com/signup, register app, add Content Posting API, Direct Post, `video.publish`, verify domain; audit at https://developers.tiktok.com/application/content-posting-api [V T1].

---

## 5. X verified, Y need review

1. IG posts per 24 h: **50 verified** (endpoint reference `quota_total`), **100 need review** (guide's rate-limit paragraph). Read the live value.
2. TikTok developer signup: docs say "using your email" and allow an individual developer account, "not recommended for real app integrations" [V T5]; the desk wiki (2026-10-12) says a verified company-domain email and legal entity are required, which probably describes the business-api portal. **Need review.** Does not change the decision (intended-use rule).
3. YouTube: live `.com` page says unverified projects are not private-locked and quota is 100 inserts/day at 1 unit [V Y1 Y2]; search snippets, a google.cn mirror and a 2021 forum answer say private-locked and 1,600 units [SN]. **Live page wins, one test upload confirms.**
4. IG in-app scheduling window: 30 days [V w1a]; snippets say 75 days [SN]. Business Suite window: not stated by Meta; blogs 29 to 30 days. FB API: 10 min to 30 days [V]. Need review.
5. Buffer + TikTok: whether a Business account is required conflicts across Buffer pages [SN]. Need review.
6. Publer MCP: pricing page lists API and MCP under Business [V]; help snippets call the official MCP a beta [SN]. Need review.
7. Metricool: hosted MCP on any plan [V pricing page, SN]; open-source MCP says API (Advanced tier) [SN]. Need review.
8. Dev-mode app: no doc read says whether posts from a Development-mode app are publicly visible [I: they are]; one developer write-up says Meta may refuse an IG account owned by the same business as an app tester [SN]. **Smoke test.** The "App Review: not required" table for a business the developer owns is from a snippet of Meta's App Review page [SN]; the Platform Overview [V] says "If your app only serves your Instagram professional account... Standard Access is all your app needs."
9. Pinterest token lifetimes: 30-day access/365-day refresh sample on the scopes page and a 60-day continuous-refresh newsletter [SN] vs a vendor blog's 1 hour [SN]. Use the values returned by the token call.
10. "AI info" label from C2PA metadata on real photos (w1a): still untested.

---

## 6. Wave-3 smoke tests (cheap, decisive)

| Test | Pass means |
|---|---|
| Buffer Free: one public TikTok through a Business account, view logged out | scheduler path holds a public TikTok app |
| Same for Upload-Post/Zernio only if Buffer fails | |
| IG own-API: one Reel with `cover_url`, `alt_text` image post, view logged out; call `content_publishing_limit` | Dev-mode posts are public; cover works; real limit known |
| Buffer: one Reel via API with `thumbnailOffset`; inspect whether a custom cover is possible in the composer | decides burned-in cover vs own API |
| YouTube: one unlisted upload from an unverified project | confirms private-lock status |
| Pinterest: time from Trial request to approval | schedules the wait |

---

## 7. Decision matrix (BRIEF2 format)

| Option | Stage | $/mo at load | Setup h | Claude/Codex drivable | Ban/ToS risk | Approval-mode fit |
|---|---|---|---|---|---|---|
| Native apps | publish | 0 | 0 | no (GUI) | none | A only |
| **Buffer Free** | publish | 0 | 1 to 2 | **yes (API + MCP)** | low | A (drafts), B (scheduled) |
| Buffer Essentials (4 ch) | publish | 20 (yearly) | 1 to 2 | yes | low | A, B |
| Metricool Starter | publish+analytics | 20 | 1 to 2 | yes (MCP; REST on Advanced $53) | low | A, B |
| Publer Business | publish | ~31 [SN] | 1 to 2 | API+MCP (MCP beta?) | low | A, B |
| Later Starter | publish | 18.75 (yearly) | 1 | not found | low | A |
| Zernio | publish API | 12 | 2 to 3 | yes (API+MCP) | low [VC] | A, B |
| SocialClaw Startup | publish API | 29 | 1 to 2 | yes (CLI, MCP, installed skill) | low [VC] | A, B |
| Blotato Starter | publish+AI | 29 | 2 | yes (API/MCP, not in trial) | low [VC] | A, B |
| Upload-Post Basic | publish API | 16 (yearly) | 2 | yes | low [VC] | A, B |
| Ayrshare Premium | publish API | 149 | 2 | yes | low | A, B |
| Postiz Cloud | publish | 29 | 2 | yes (MCP, CLI, API) | low | A, B |
| Postiz/Mixpost self-host | publish | 0 + hosting | 12 to 20 | yes | same as path 3 | A, B |
| **Own API (IG, FB, YT, Pinterest, Threads)** | publish | 0 + bucket | 20 to 30 | yes (we write it) | low (official) | A, B (we build approval) |
| Own TikTok API | publish | n/a | n/a | n/a | audit rejection | n/a |
| Unofficial libs | publish | 0 | 4+ | yes | **high** | not recommended |

---

## 8. Build effort

| Path | Claude Code + Codex hours | Ricky by hand |
|---|---|---|
| Tier B on Buffer | 3 to 4 h: MCP/API wiring, manifest-to-`createPost` script, draft mode, public-URL step | 1 h: signup, connect 3 channels, key, phone app |
| Tier C IG + FB | 11 to 13 h: Deno publisher, token refresh + alert, cron, container polling, limit check | 1 to 2 h: Meta app, tester role, token, Page |
| Tier C Pinterest | 4 h + review wait | 1 h: app request, demo recording |
| Tier C YouTube | 4 h | 1 h: Cloud project, consent screen to Production |
| Threads | 2 h (skip for now) | 0.5 h |
| TikTok | 0 | 0.25 h per video in TikTok Studio, or via Buffer |

---

## 9. Questions only Ricky can answer; gaps

**Questions**
1. Is it acceptable for Buffer (or another vendor) to hold OAuth tokens for the main account, or should everything Meta-side go through our own app?
2. Is `@holliewoodandvine` Ricky's, and is there a legal entity? (Only needed to take a Meta app Live, not for Dev mode.)
3. Approve-everything or approve-by-exception? Tier B and C support both.
4. Is a public TikTok auto-post worth a scheduler fee, or is TikTok Studio by hand at 3 a week fine?
5. Which scheduler may be tested on a throwaway account before the real one?

**Gaps (not reached)**
- Meta's own Instagram App Review page (no crawl left); Instagram "Live vs Development mode" post visibility.
- Pinterest create-pin reference (crawl returned 403 bytes): scheduling field, video Pin parameters, exact rate limits.
- Later, Planoly and Hootsuite API/MCP; Sendible not evaluated (priced above Buffer by reputation, not read).
- Zapier/Make/n8n pricing on vendor pages; Make/Zapier Instagram module limits on vendor pages.
- Buffer TikTok/Pinterest/YouTube help pages (one crawl failed); Buffer custom-cover support in the composer.
- Threads rate limit; YouTube thumbnail API; TikTok inbox-upload approval; Google audit form location.
- w2d replies are out of scope; note Blotato bills DM/comment contacts and Zernio includes 10,000 DMs a month free [V], worth passing on.

---

## Sources (all accessed 2026-10-29)

Meta: M1 `developers.facebook.com/documentation/instagram-platform/instagram-graph-api/reference/ig-user/media`; M2 `.../instagram-platform/content-publishing` (w1a capture); M3 `.../reference/ig-user/content_publishing_limit`; M4 `.../instagram-api-with-instagram-login/get-started`; M5 `.../instagram-api-with-instagram-login/business-login`; M6 `.../instagram-platform/create-an-instagram-app`; M7 `.../instagram-platform/overview` (w1a); M8 `developers.facebook.com/docs/pages-api/posts`; M9 `developers.facebook.com/docs/threads/posts`.
TikTok: T1 `developers.tiktok.com/doc/content-posting-api-get-started`; T2 `.../content-sharing-guidelines`; T3 `.../getting-started-faq`; T4 `.../app-review-guidelines`; T5 `.../getting-started-create-an-app`; T6 `.../add-a-sandbox`; upload `.../content-posting-api-get-started-upload-content`.
Pinterest: P1 `developers.pinterest.com/docs/key-concepts/access-tiers/`; P2 `.../docs/getting-started/connect-app/`. YouTube: Y1 `developers.google.com/youtube/v3/docs/videos/insert`; Y2 `.../determine_quota_cost`.
Buffer: B1 `buffer.com/pricing`; B2 `buffer.com/api`; B3 `developers.buffer.com` (examples: create-video-post, create-instagram-post-with-user-tags); B4 `support.buffer.com/articles/scheduling-instagram-posts-reels-stories-and-notifications-3XA98S9Q5p`; B5 `developers.buffer.com/guides/posts-and-scheduling.md`.
Pricing: `publer.com/pricing`, `metricool.com/pricing/`, `later.com/pricing/`, `hootsuite.com/plans`, `zernio.com/pricing` (via getlate.dev), `getsocialclaw.com/pricing`, `blotato.com/pricing`, `upload-post.com/#pricing`, `ayrshare.com/pricing/`, `postiz.com/pricing` (PZ docs `docs.postiz.com/self-host/providers/instagram`), `mixpost.app/pricing` (MX), `repurpose.io/pricing`.
Signup: Meta `developers.facebook.com/apps`; TikTok `developers.tiktok.com/signup`; Pinterest `developers.pinterest.com/apps/`; Google `console.cloud.google.com`; Buffer `login.buffer.com/signup`; Metricool `app.metricool.com/register`; Publer `app.publer.com/users/sign_up`; Zernio `zernio.com/signup`; SocialClaw `getsocialclaw.com/sign-up`; Blotato `my.blotato.com/signup`; Upload-Post `app.upload-post.com`; Postiz `platform.postiz.com/auth`; Repurpose `my.repurpose.io/signup`.
gh: postiz-app, mixpost, instagrapi, instagram-private-api, n8n (read via `gh api repos/...`).
