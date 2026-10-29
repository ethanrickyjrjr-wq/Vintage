# w2d: reply stage, comment-to-DM and the link conflict (Holliewood & Vine)

Lane w2d-reply-dm, accessed 2026-10-29. Raw captures: `research/social-2026-10-29/raw/w2d-*.md` (28 pages). Budget used: 11 of 20 searches, about 35 crawls, 3 `gh` calls. No signups, no logins, no tests run (nothing here needed the Fedora box). Tags: `verified` = read on the live page this session; `vendor claim`; `unverified (search snippet)`; `inferred`.

## TL;DR

1. **Correction to the brief, the wiki and w1a: "our own pages need no review" does not hold for comment webhooks.** Meta's webhook setup page says the app must be Live, `comments` notifications need **Advanced Access**, and Business Verification is "required for production access" (a legal entity). Reading, replying to, hiding and deleting comments does work at Standard Access on our own account. `verified` (https://developers.facebook.com/documentation/instagram-platform/webhooks/setup and .../comment-moderation). Whether a private reply works at Standard Access is contradicted across three Meta pages (section 2).
2. **Fallback that avoids the gate: poll `GET /<media>/comments`** on recent posts. Standard Access, far under the rate limit, no public HTTPS endpoint. Whether it returns non-role commenters' text in a dev-mode app is `unverified`; one throwaway test decides it (section 7).
3. **Private reply facts:** one message per comment, within 7 days, delivered to Requests unless the commenter follows us, 750 per hour per account, follow-ups only if the person replies and only within 24 hours. `verified`.
4. **Link conflict, recommendation:** link in bio plus piece number on every post (primary, zero platform risk); "comment LINK" as an optional convenience that triggers a public reply plus a private-reply DM carrying only the listing URL; Story link sticker by hand on drop days. A bare URL in a public comment is not the plan.
5. **Engagement-gating risk is real but defusable.** Meta's Spam standard bans "like/share-gating" of "specific, exclusive content". The link is never exclusive if link-in-bio always works. Never write "comment to get/unlock". Never gate on a follow. `verified` (text), `inferred` (application).
6. **At launch a third-party tool beats our own app:** it holds the approved Meta app, so Ricky needs no entity. At the reference load (about 130 comments a month) InstantDM Legend Pro is $9.99 a month billed yearly and ManyChat Essential is $14 billed yearly. `vendor claim`, prices `verified` on the vendors' pages.
7. **No tool offers a draft-approval queue** on the pages read. Approve-everything (mode A) therefore points to our own pipeline or to Hollie replying by hand.
8. **Our own LLM cost is cents.** `claude-haiku-5-5` is $0.10 in and $0.50 out per million tokens; 130 classifications a month is about $0.08; drafting the non-LINK replies with `claude-sonnet-5-5` adds about $0.80. `verified` prices, `inferred` token counts.
9. **Meta Business Agent (free on Instagram since June 2026, paid later) is not recommended:** it advertises "Close sales", and if it owns a thread our API sends fail (error 2534037). `verified`.
10. **Unofficial Instagram libraries: not recommended** (ToS and ban risk to the one brand account).

## 1. Link conflict: three routes against the shop's rules

Shop rules: the only call to action is the listing page; no claims by DM or comment; no DM selling; "Gone" never "sold"; the mirror ball is never a promotion. Evidence that a public URL is not tappable: InstantDM blog (Aug 2026, vendor, sells DM automation), Social Media Today (pinned comments cannot hold links, 2025, press). No Instagram help page stating it was reachable. `vendor claim`.

| Route | How it works | Platform rules and limits | Fits "no claims, no DM selling" | Cost | Own API without review | Wins when |
|---|---|---|---|---|---|---|
| A. Link in bio plus "piece No. [n]" | Caption says "Link in bio, piece 14"; listing page answers by number | None. Needs a real URL or lookup per piece (round-d gating fact). Link-in-bio rules not verified (w1a gap) | Fully | $0 | n/a, no API | Every post. It is the canonical route |
| B. Public reply plus private-reply DM with the URL | Comment "LINK" triggers a public reply ("sent, check message requests") and one DM with the page URL | One private reply per comment, within 7 days, Requests folder for non-followers, 750/hour (`verified`); DMs may carry links and promotional text inside the window, text up to 1,000 bytes (`verified`); the Spam "gating" clause applies if the link is exclusive (`verified` text) | Yes if the DM is fixed text: URL, no price talk, no hold. Any reply from the person goes to a human or a canned "pieces can't be held" | $0 by hand; $0-$29 tool; about $1 own | Unresolved (section 2) | Comments arrive and Hollie wants fewer taps for buyers |
| C. Story link sticker | Hollie adds the Link sticker in the app; story lasts 24 h | Instagram's 2021 announcement: all creators and businesses, excluding new accounts and repeat violators (`unverified` for current rules; https://about.instagram.com/blog/announcements/expanding-sharing-links-in-stories-to-everyone). The Stories publish API documents `media_type=STORIES` and no sticker field (`verified`, w1a capture) | Yes, it is a link to the page | $0 | No sticker via API (`inferred` from docs); human step | Drop day |
| D. Bare URL in public comment | Typed into the reply | Plain text, not tappable (`vendor claim`) | Yes | $0 | Yes | Not recommended as the only route |

**Recommendation.** Every CTA offers A first: "Link in bio, piece No. 14. Or comment LINK and Hollie will message it." That keeps B a convenience, not a gate. B starts by hand (Hollie, free). Automate B only after real stock exists and comments are real. C by hand on drop days.

**Engagement-bait question (open in w1a).** Meta's engagement-bait guideline is Facebook-scoped and exempts "a specific call to action" (https://transparency.meta.com/en-gb/features/approach-to-ranking/content-distribution-guidelines/engagement-bait, `verified`). The Spam standard bans requiring public engagement "to gain access to specific, exclusive content" and "claiming that users are required to engage" before seeing promised content (https://transparency.meta.com/policies/community-standards/spam/, `verified`; Facebook standards, Instagram's own wording not read). A link that is always also in the bio is not exclusive, so B is defensible; this is `inferred`, and Account Status after 30 days is the check. Giveaways in exchange for engagement are banned in the same page: never tie the mirror ball to commenting.

**Where this changes a fixed constraint.** The brief says reply "LINK" with the link, nothing else. A compliant B adds a public reply and, per Meta's policy page, a "you are talking to an automated service" disclosure line where law requires it (California and Germany named; recommended elsewhere; https://developers.facebook.com/documentation/business-messaging/messenger-platform/policy, `verified`). Ricky decides whether one disclosure line breaks "nothing else". Not applied silently.

## 2. Meta's own APIs for Instagram (accessed 2026-10-29, `verified` unless tagged)

| Capability | What Meta says | Source |
|---|---|---|
| Comment webhooks | Subscribe to `comments` / `live_comments`. App must be Live. Advanced Access required for `comments`. Business Verification "required for production access". Public account only. Endpoint must handle duplicates and return fast | .../webhooks/setup, .../webhooks |
| Read comments | `GET /<IG_MEDIA_ID>/comments`; Meta "strongly recommends webhooks to prevent rate limiting" | .../comment-moderation |
| Reply, hide, delete, disable comments | `POST /<COMMENT_ID>/replies`; `POST /<COMMENT_ID>` hide/unhide; `DELETE`; `POST /<MEDIA_ID>` toggles comments. Standard Access suffices for accounts "you own or manage and have added to your app" | .../comment-moderation |
| Private reply | `POST /<IG_ID>/messages` with `recipient.comment_id`. One message, 7 days, Live only during broadcast, goes to Inbox (follower) or Requests (non-follower), contains a link to the post, follow-ups only after the person replies and within 24 h | .../private-replies; .../instagram-messaging/features/private-replies |
| Messaging window | 24 h after the user's message (7 days for Click-to-Direct ad starts). Human Agent tag: 7 days for human replies. One-time notification, News and Sponsored messages not available on the Instagram API. Promotional content allowed inside the window | .../messenger-platform/policy |
| Message content | Text (UTF-8, 1,000 bytes max), links, images (8 MB), templates, quick replies, ice breakers | .../messaging-api |
| Rate limits | Non-messaging calls: 4,800 x impressions per 24 h per app-user pair. Private replies to posts and reels: 750 calls per hour per account. Text and link messages: 100 per second | .../instagram-platform/overview |
| Access levels | Standard Access "if your app only serves your Instagram professional account ... is all your app needs". Development mode: only role users. Live mode: only permissions approved through App Review | .../overview; .../app-modes |
| Own-business App Review track | Exists (`instagram_manage_messages`, optional Human Agent), verification details "optional" (page updated 2026-06-30). Does not say Business Verification is waived | .../app-review/apps-for-your-own-business |
| Meta Business AI interplay | Oct 18 2026 changelog: if Meta Business AI owns the thread and "Take control of conversations with your Business AI" is off (default), untagged Send API calls fail with code 100 / subcode 2534037 | .../instagram-messaging/changelog |

**X verified, Y need review (own-account access).**
- Verified: comment read, reply, hide, delete at Standard Access on an owned account. Instagram Login and Unified Login need no Facebook Page.
- Contradiction: the Instagram platform private-replies page lists `instagram_manage_messages` and no access level; the Instagram-Login messaging page says Standard Access "may not work properly until ... Advanced Access"; the Messenger-platform private-replies page lists Advanced Access as a requirement. The app-review page says an app needs review before anyone but role users can use it.
- Plausible reading (`inferred`): in a dev-mode app the account owner (a role user) can call everything, but comments from the public (non-role) may not trigger webhooks or be returned. The wiki line "our own pages need no review" (2026-10-12) is true for moderation calls and unproven for webhooks and private replies.

## 3. Native tools (no API, no review)

| Tool | What it does | Tag and source |
|---|---|---|
| Saved Replies (was Quick Replies) | Business or Creator account; Settings, Business, Saved Replies; shortcut word expands in a DM. Manual only. No official page found | `unverified (search snippet)`; Planoly, Later, Bustle guides, several years old |
| Ice breakers / FAQs | Up to four FAQs shown when a chat opens, business and creator accounts. The API also has ice breakers | `unverified (search snippet)` (help.instagram.com/561062241952036); API mention `verified` in the app-review page |
| Hidden Words | Custom word list hides matching comments and message requests; Settings, Hidden Words | `unverified (search snippet)` (https://help.instagram.com/700284123459336) |
| Meta Business Suite inbox, Facebook Page automated responses | Keyword-triggered and away messages, one inbox for Facebook and Instagram comments and DMs | `unverified (search snippet)`; the official help pages returned 4-byte walls |
| Pinned own comment | Can pin a text comment (CTA text); links cannot be added | `press` (Social Media Today, 2025) |
| Meta Business Agent | AI replies, catalog recommendations, appointment booking, "Close sales", human handoff. Expanded to Instagram June 2026, free to activate, "paid subscription offerings in the coming months", "starting with a select number" on Instagram Pro. Whether it can be told to send a link: not stated. Waitlist: metabusinessai.com/waitlist | `verified` (https://about.fb.com/news/2026/06/meta-business-agent/); AI label "generated by AI" is `unverified (search snippet)` |

Recommendation: do not enable Business Agent. It sells; the shop does not sell by message. It also collides with any API or tool reply path.

## 4. Third-party comment-to-DM tools (prices read 2026-10-29)

Reference load: about 30 comments a week, about 130 a month, perhaps 60-100 unique people (an "active contact" is a person messaged in the month). Annual-billed prices are shown; monthly-billed prices were not read unless stated.

| Tool | Plans at our load | Fit | Meta access and policy | Draft approval | Claude/Codex-drivable |
|---|---|---|---|---|---|
| InstantDM https://instantdm.com/pricing | Free: 500 DM automations a month, 5 post automations, 3 trigger words, 1 account, comment-to-DM with text and link DMs, public replies, AI comment replies, InstantDM branding on DMs. Legend Pro $9.99/mo billed yearly: unlimited, one automation for all posts, no branding, Story and Live triggers. Trendsetter $24.99/mo billed yearly: Flow Editor with an AI agent node on your own Claude key, human takeover, API, webhooks and MCP. No per-contact fees. 7-day trial | Free fails the post cap (about 20 posts a month) unless automations are recreated per post (`inferred`). Legend Pro fits | "Built on Meta's official API", "Meta Business Partner" badge (`vendor claim`; Meta directory not checked). Avoid its follow-before-link gate (follow-gating) | None listed; human takeover pauses AI per contact (Trendsetter) | Trendsetter only (`vendor claim`). A community `sanjaykhanssk/instagram-mcp` repo (MIT, 0 stars, pushed 2026-08-31) is unvetted |
| ManyChat https://manychat.com/pricing | Free: 25 active contacts, 4 live triggers, "Powered by Manychat" branding. Essential $14/mo billed yearly ($168): 250 contacts, no branding. Pro $29/mo billed yearly ($348): 2,500 contacts, AI replies to DMs and comments. Extra contacts $0.082 each (Essential, annual) | Free fails the load. Essential fits | "Official Meta-approved partner" (`vendor claim`); lists Instagram, TikTok, Messenger, Telegram | None listed | External Requests need a paid plan; "Pro and up" per a moderator, May 2026, "Advanced" per Blotato (`unverified (search snippet)`), need review. No ManyChat MCP verified |
| Inro https://www.inro.social/pricing | Free: 100 active contacts a month, 3 campaigns a month. Pro from EUR 12.99/mo billed monthly, 500+ contacts, 14-day trial | Free is marginal; Pro fits | Not read | None listed | Not read |
| Chatfuel https://chatfuel.com/pricing | Business S $18/mo billed yearly ($216) with $20 AI usage; about $0.0093 per AI reply; Instagram, Facebook, TikTok | AI-first, so it answers price and availability on its own. Not our shape | Not read | None listed | Not read |
| CommentSold CommentChat https://try.commentsold.com/features/commentchat-landing-page/ | Bundled in CommentSold plans from $149/mo (Starter), $249, $499, $999; standalone price not read; Instagram and Facebook, TikTok "coming soon" | Overkill. CommentSold is a claim-by-comment live-selling stack, the opposite of the shop's rule | Not read | None listed | Not read |
| Others named by vendor comparisons, not read: ReplyRush ($10/mo with a free tier), LinkDM ($19/mo), SmartReply, CreatorFlow ($24/mo) | | | | | `unverified (search snippet)` |

Self-hosted GitHub examples ("Instagram-Comment-DM-Automation", FastAPI plus Next.js, 0 stars, no license) are Graph API apps that hit the same Meta gates. No value.

## 5. Other platforms (brief)

| Platform | Reply path | Gates and limits | Tag and source |
|---|---|---|---|
| TikTok | Comment management lives on business-api.tiktok.com (Organic Accounts API, webhook `comment.update`). The consumer developer platform has no comment scope. ManyChat and Chatfuel list TikTok channels; CommentChat says "coming soon" | Developer signup needs a company-domain email and a legal entity. The TikTok docs page rendered only "Loading..." this session | `verified` by the desk wiki 2026-10-12; not re-read. TikTok is deferred anyway (w1b) |
| YouTube | `comments.insert` costs 50 quota units; default quota 10,000 units a day; scope `youtube.force-ssl` | 30 replies a week is about 1,500 units a week. An OAuth app in "Testing" status gets refresh tokens that expire in 7 days, so publish the app or re-authorise weekly | `verified` (developers.google.com/youtube/v3/determine_quota_cost; .../docs/comments/insert; .../identity/protocols/oauth2) |
| Pinterest | No comment endpoint. The v5.28.0 OpenAPI spec (github.com/pinterest/api-description, 189 paths) has no path containing "comment" | Replies are manual in the app | `verified` from the spec, 2026-10-29 |
| Facebook Page | Same Graph/Messenger family: private reply within 7 days, Page token, Advanced Access listed on the Messenger private-replies page | Needs a Page | `verified` (policy and private-reply pages) |

## 6. Unofficial Instagram automation: NOT RECOMMENDED

Reverse-engineered libraries and "auto-reply bots" sold online will be recommended to Ricky. Not tested, not recommended: they violate Meta's terms (Instagram terms page not re-read in this lane, `unverified`), and a ban would remove the one brand account.

| Library | Stars | Last push | License |
|---|---|---|---|
| subzeroid/instagrapi | 7,040 | 2026-10-28 | NOASSERTION |
| dilame/instagram-private-api | 6,488 | 2024-08-09 | MIT |

`gh api` output 2026-10-29. Browser-automation bots and scraper actors (Apify "comment scraper" actors exist for Pinterest and Instagram) share the same risk and cost.

## 7. Our own pipeline

**Shape (mode B).** Poll or webhook, then dedupe, then rules, then Haiku classification, then one of four outputs.

```
comments (poll every 10 min on posts from the last 14 days; webhook if approved)
  -> ledger insert, unique on (commenter_id, media_id), BEFORE any send
  -> regex: whole-word "link" (case-insensitive) on its own
       media_id -> piece No. -> stock check (site data: Here / Gone)
       Here: public reply + one private reply, fixed text, URL only
       Gone: public reply from the "Gone" template, no DM
  -> otherwise claude-haiku-5-5 classify:
       link-ish (fuzzy) | availability | price | shipping | compliment | piece question | complaint | abuse/spam | claim attempt ("mine", "hold", "dibs") | other
  -> output: approval-queue draft (default) | hide (high-confidence spam only, logged) | no action
```

**Cost per month at the reference load.** Verified prices: `claude-haiku-5-5` $0.10 in / $0.50 out per MTok (prompts up to 100K); `claude-sonnet-5-5` $2 in / $10 out (https://platform.claude.com/docs/en/about-claude/models/overview and .../pricing, 2026-10-29). Assumed tokens (`inferred`, generous): classify 1,200 in / 1,000 out per comment; draft 2,500 in / 800 out.

| Item | Math | $/mo |
|---|---|---|
| Haiku classification, 130 comments | 0.156 MTok x $0.10 + 0.13 MTok x $0.50 | 0.08 |
| Sonnet drafts, about 60 non-LINK comments | 0.15 MTok x $2 + 0.048 MTok x $10 | 0.78 |
| Hosting | Poller on the Fedora box ($0) or a Supabase/Vercel function on the planned stack (price not read) | 0-few |
| Approval ping | ntfy.sh free, 250 messages a day (`verified` https://docs.ntfy.sh/publish/); Telegram bots free, about 1 message a second per chat (`verified` https://core.telegram.org/bots/faq); email price not read | 0 |
| Total | | about 1 |

Phone approval (`inferred`): the push carries a link to a small approve/edit/reject page (Vercel/Supabase) listing the comment, the draft and the piece's Here/Gone state.

**Failure modes and the fix.**

| Failure | Cause | Fix |
|---|---|---|
| Double replies | Webhook redelivery; boosted or ad posts duplicate notifications (`verified`); poll overlap | Unique ledger on (commenter, media), write before send, no auto-retry of failed sends |
| Spending the single private reply on a Gone piece | Stock changed | Stock check first; Gone gets a public reply only |
| "Is this available?" / price | Nothing safe to improvise | Canned lines from w1c ("The listing page is the only truth ... Prices are fixed") as drafts |
| "Hold it" / "mine" / "sold" | Claim attempt | Draft "Pieces can't be held"; human sees it |
| Abuse and spam | Link-spam, harassment | Hide (reversible) only at high confidence, daily digest; Hidden Words filter as the first layer |
| Reply to the bot's DM | Person answers ("can you hold it?") | Route to human; canned "pieces can't be held; checkout is on the page" |
| Business Agent / another tool owns the thread | Thread control (error 2534037) | Keep one automation owner per account |
| YouTube refresh token dies in 7 days | Testing status | Publish the OAuth app |
| Pre-launch | Sample listings, checkout "coming soon" | No LINK automation until real stock exists; use the pre-launch line ("Hollie is still building the shop. The first real drop is announced here first.") |
| Prompt injection in a comment | Comment text reaches the model | Classifier output is a label only; drafts never auto-send; the only auto-send is the fixed template |

**What must always be human (both modes):** any price or negotiation; condition, age or provenance claims beyond the listing fields; availability beyond the Here/Gone flag; anything about a named person or child; complaints, refunds, safety or electrical questions; every reply once a person answers a DM; collab and press inquiries; low-confidence classifications; any comment containing a link or media.

**Wave-3 deciding test (Ricky creates the throwaway app; free, no entity).**
1. Dev-mode Meta app, Instagram Login, owner as role user. 2. Second Instagram account comments "LINK". 3. Does the `comments` webhook fire? Does `GET /media/comments` return that text? 4. Does `POST /messages` with `comment_id` succeed, and is the URL tappable in the Requests folder? 5. Record error codes.

## 8. Options and recommendation

| Decision | Option | Price | Effort | Risk | Wins when |
|---|---|---|---|---|---|
| Who sends | Hollie by hand (app, Business Suite, Saved Replies) | $0 | 5 min a day at 30 comments a week | Slow | Pre-launch and launch month |
| | Third-party tool, LINK only | $0 to $14 (Legend Pro $9.99, Essential $14) | 1-3 h | Vendor partner status unverified; branding on free tiers | Real comments, Ricky has no entity |
| | Own API pipeline | about $1 | 12-20 h | Meta gate unresolved | The wave-3 test passes, or an entity exists |
| Link route | A, B, C above | | | | Section 1 |

**Tiers.**
- **(a) Free and native:** link in bio plus piece number; Hollie replies by hand; Saved Replies hold the canned lines; Hidden Words for spam; Story link sticker on drop days. Human: everything.
- **(b) One paid tool:** InstantDM Legend Pro ($9.99/mo billed yearly, 7-day trial) or ManyChat Essential ($14/mo billed yearly) for the LINK keyword only; all other comments stay with Hollie. Human: every non-LINK reply, every DM answer, Gone handling, disclosure wording.
- **(c) Claude + Codex pipeline:** section 7. Mode A: nothing sends without a tap (tool support: none; ours only). Mode B: auto only for the LINK template, public "Gone" template and logged spam hides; all else drafted. Human: the list above.

## 9. Decision matrix

| Option | Stage | $/mo at load | Setup h | Claude/Codex-drivable | Ban/ToS risk | Mode fit |
|---|---|---|---|---|---|---|
| Hand + Business Suite + Saved Replies | reply | 0 | 0.5 | No | None | A |
| Link in bio + piece No. | reply/publish | 0 | 0 | n/a | None | A and B |
| Story link sticker | reply | 0 | 0.05 per Story | No (no sticker field documented) | None | A |
| InstantDM Free / Legend Pro | reply | 0 / 9.99 | 1-2 | Trendsetter $24.99 only | Low (official API, vendor claim) | B for LINK; no queue |
| ManyChat Essential / Pro | reply | 14 / 29 | 2-3 | Pro+ External Requests (disputed) | Low | B for LINK; no queue |
| Own API (poll or webhook) | reply | about 1 | 12-20 | Yes | Low if approved route; gate unresolved | A and B (only one with a queue) |
| Meta Business Agent | reply | 0 now, paid later | 0.5 | No | None, but it sells | Not recommended |
| Unofficial libraries | reply | 0 | varies | Yes | High | Not recommended |

**Build effort (Claude Code plus Codex).** Wave-3 test script: about 2 h Claude after Ricky creates the app. Pipeline: poller, ledger, rules, Haiku classifier, template sender, approval page and ping, about 10-16 h Claude Code plus 3-4 h Codex review and page polish. Ricky by hand: create the Meta developer app and authorise the account, supply a second Instagram account for the test, decide the questions below, approve drafts, add Story stickers.

## 10. Questions for Ricky

1. Does a DM carrying the listing URL plus one automated-message line satisfy "reply LINK with the link, nothing else"?
2. Hand-first at launch (tier a), or a tool from day one (tier b)?
3. Will you run the wave-3 throwaway Meta app test (about 1 hour, free)?
4. Is a registered entity coming? It unlocks Business Verification and Advanced Access.
5. Mode A or B for replies?
6. Confirm no Business Agent and no follow-gate on links.

## 11. Gaps

Instagram and Meta help pages for Saved Replies, Hidden Words, Business Suite automated responses and Instagram's comment-link behaviour returned walls or search snippets only. ManyChat's and InstantDM's Meta partner status is vendor claim; Meta's partner directory not checked. Monthly-billed prices for ManyChat and InstantDM not read. No app was built or tested, so every webhook and Standard Access claim about non-role commenters is open. The TikTok docs page did not render. Instagram's own Community Guidelines wording on engagement bait not read (Facebook standards read instead).
