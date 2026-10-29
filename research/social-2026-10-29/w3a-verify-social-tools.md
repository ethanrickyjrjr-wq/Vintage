# w3a: live re-read of finalist social tools (accessed 2026-10-29)

Method: every row below was read on the vendor's own page today unless tagged otherwise. Raw captures: `research/social-2026-10-29/raw/w3a-*.md`. Load assumed: ONE brand, 4 channels (Instagram, Facebook, TikTok, Pinterest), about 11 publishes a week (about 48 a month), about 30 comments a week. Tags: `verified`, `inferred`, `snippet` (search snippet, unread page).

## 1. Schedulers (price per month; "yr" = billed annually, "mo" = billed monthly)

| Tool / plan | Price (4 channels where it scales) | Limits that matter | API / MCP | Sign up | Source |
|---|---|---|---|---|---|
| Buffer Free | $0 | 3 channels max (one short of 4); 10 scheduled posts per channel; 100 ideas; 1 user; Insights 30 days; community inbox; AI replies 5 suggestions/week; 1 saved reply; no first comment; no hashtag manager | API: 1 key, 1,000 req/channel/mo up to 3,000, 150 per 15 min, 600 per 24 h. MCP: yes, "free on every plan". Limits shared by API and MCP. `verified` | https://login.buffer.com/signup?product=buffer&plan=free&cycle=year | https://buffer.com/pricing.md ; https://buffer.com/mcp ; https://developers.buffer.com/guides/api-limits.html |
| Buffer Essentials | $6 mo / $5 yr per channel (1-10 channels). 4 channels = $24 mo / $20 yr (`inferred` from per-channel rate; page's own examples: 3 ch $18/$15, 5 ch $30/$25) | Unlimited scheduled posts (fair-use cap 5,000/channel); first comment; hashtag manager; unlimited AI replies; 14-day trial; you pay for the 3 free channels too | 3 keys, 3,000 req/channel/mo up to 30,000; 450 per 15 min; 1,800 per 24 h. MCP yes | same as above | same |
| Buffer Team | $12 mo / $10 yr per channel | Adds approval workflows, unlimited users | 5 keys, 10,000 req/channel/mo | same | same |
| Postiz Cloud Standard | $29 mo / $23 yr (FAQ: "$23, $31, $39, $79 on annual billing") | 5 channels; unlimited posts; 7-day free trial on every plan; Team $39 (10 ch), Pro $49, Ultimate $99 | API, CLI, MCP, webhooks on every plan `verified` | https://platform.postiz.com/auth | https://postiz.com/pricing |
| Metricool Free | $0 | 1 brand; 20 posts/month (about 48 needed: too small); 30 days analytics | "Metricool MCP" listed in the Free feature list; API (Zapier, Make) is Advanced only | https://app.metricool.com/register | https://metricool.com/pricing/ |
| Metricool Starter | "From $20/mo" yr, "from $25/mo" mo. Up to 5 brands $20 yr; up to 10 brands $36 yr. EUR: from 16 yr / 20 mo | Unlimited publishing (fair use); LinkedIn; unlimited analytics history. Not a flat price | MCP yes; no API | same | same |
| Metricool Advanced | From $53 yr / $67 mo (up to 15 brands) | Approval system; Data Studio | "Metricool API (Zapier, Make)" | same | same |
| Publer Free | $0 | 3 social accounts (no X); 10 scheduled posts per account; 25 drafts; 24-hour post history | None | https://app.publer.com/users/sign_up | https://publer.com/plans |
| Publer Professional | $5 mo / $4 yr | Unlimited scheduling; first comments; 7-day trial. Price is per social account (`inferred` from "for every 9 accounts the 10th is free"; slider value not captured) so 4 accounts = about $20 mo / $16 yr `inferred` | None | same | same |
| Publer Business | $10 mo / $8 yr (same per-account basis; 4 accounts about $40 / $32 `inferred`) | Analytics, best times, 14-day trial | "Access to Publer API & MCP" (Business only; blog confirms Free and Professional must upgrade) | same | https://publer.com/plans ; https://publer.com/blog/publer-mcp/ |
| Zernio (formerly Late) | Usage-based, card on file, monthly: accounts 1-2 free, 3-10 $6 each, 11-100 $3. 4 accounts = $12 | "Every feature included, no plans"; unlimited posts, first comment, queue, comments; DMs first 10,000 sent/month free | API is the product; MCP only seen in a customer testimonial, not on the pricing page | https://zernio.com/signup | https://zernio.com/pricing ; rename: https://zernio.com/rebrand (verified) |

## 2. Comment and DM automation

| Tool / plan | Price | Limits at ~30 comments/week | API | Sign up | Source |
|---|---|---|---|---|---|
| ManyChat Free | $0 | 25 active contacts/month (too small: 30 comments a week is likely 100+ people a month); 2 channels; 4 live triggers; "Powered by Manychat" branding | none | https://app.manychat.com/signup/facebookAuth?channel=instagram (Facebook login) | https://manychat.com/pricing |
| ManyChat Essential | $14/mo billed yearly ($168 up front, 18% off). Monthly billing $17 (`snippet`; consistent with 18% off, not shown in my capture) | 250 contacts; unlimited automations; no branding; 14-day trial; overage $0.10 per extra contact mo | API access is on Advanced only ($139/mo yr) per help article | same | https://manychat.com/pricing ; https://help.manychat.com/hc/en-us/articles/25800347122716 |
| InstantDM Free | $0 forever | 500 DM automations/month; up to 5 post automations; 3 custom trigger words; AI comment replies; 1 Instagram account | none | https://app.instantdm.com/signup | https://instantdm.com/pricing |
| InstantDM Legend Pro | $9.99/mo billed yearly. Monthly about $12 (`snippet`, vendor's own blog) | Unlimited, up to 800/hour; Instagram + Facebook; post scheduling with AutoDM; 7-day trial, no card | Trendsetter ($24.99/mo yr): "API, webhooks, and MCP" | same | same |
| CommentSold CommentChat | No standalone price. Bundled in Starter $149/mo + 6% of sales (Starter with AI $249 + 6%; Small Business $499 + 5%; Large Business $999 + 4%). 15-day trial | Instagram and Facebook now; TikTok "coming soon". Product is a live-selling and auction platform: conflicts with the shop's no-bidding rule and the sales cut makes it the worst fit | Open API on higher tiers | https://try.commentsold.com/landing/commentsold-start-15-day-free-trial/ | https://try.commentsold.com/get-started/pricing/ ; https://try.commentsold.com/features/commentchat-landing-page/ |

Vendor bias: InstantDM's competitor prices are `vendor claim`.

## 3. Editing and design

| Tool | Price | Notes | Link | Source |
|---|---|---|---|---|
| Instagram Edits | Free; App Store says "In-App Purchases" but lists none | 4K export, no watermark, clips up to 10 min (listing text). `verified` | https://apps.apple.com/us/app/edits-an-instagram-app/id6738967378 | same |
| CapCut (iOS) | Free + in-app purchases: Standard Monthly $9.99, Pro Monthly $19.99, Monthly $7.99 and $19.99, Yearly $89.99 (listing mixes names; which entry maps to which tier not stated) | `verified` price list, tier mapping unclear | https://apps.apple.com/us/app/capcut-photo-video-editor/id1500855883 | same |
| Canva Free | $0 | 1 Brand Kit (3 colors), 5 GB, up to 20 AI uses | https://www.canva.com/pricing/ | same |
| Canva Pro | $144/year (= $12/mo billed yearly); $18/mo billed monthly (canva.com learn page, read in full) | 5 Brand Kits, social content scheduling, premium templates, 100 GB, 10x AI; free trial offered (length not read) | same | https://www.canva.com/pricing/ ; https://www.canva.com/learn/canva-pro-vs-canva-enterprise/ |

## 4. Buffer's own docs: API/MCP on Free, and Instagram capabilities

- **API and MCP on Free: confirmed.** Pricing page lists API access on Free (1 key, 1,000 requests per channel per month up to 3,000). `buffer.com/mcp`: "MCP access is included on every plan, including Free." Remote server `https://mcp.buffer.com/mcp`, OAuth for Claude, ChatGPT, Cursor, Raycast, Perplexity, Notion, Zapier, n8n. Codex is not in that list; the dev docs' quick start does name Codex for the API. `verified`
- **Drafts and approval.** `create_post` takes `schedulingType` automatic or notification, and `saveToDraft`. MCP page: posts land as drafts or scheduled posts, "you're always the last step." Native approval workflows are Team only. `verified`
- **Reels: yes.** `metadata.instagram.type` accepts post, story, reel; single videos always publish as Reels; Reel length 3 s to 15 min; Free plan can schedule Reels. https://support.buffer.com/articles/scheduling-instagram-posts-reels-stories-and-notifications-3XA98S9Q5p ; https://buffer.com/instagram `verified`
- **Carousels: yes in the app**, up to 20 images and videos mixed (help article). Creating one through the API (several image assets) is not stated in what I read. `verified` app / `unverified` API
- **Alt text: yes for static images** (single and carousel), 1,000 characters on Instagram, API field `ImageMetadataInput.altText`. Not stated for Reels or Stories. https://support.buffer.com/articles/adding-alt-text-to-your-images-Oqn4WJGS1j ; https://developers.buffer.com/reference.html `verified`
- **Custom cover upload: NOT supported.** Help article: "You can't upload a separate image as a custom cover through Buffer, because Instagram's API doesn't support it." Only a frame pick ("Edit Thumbnail"). API: video `thumbnailUrl` is rejected; use `metadata.thumbnailOffset` in ms, Instagram, TikTok and Pinterest only. Workaround per Buffer: bake the cover into the first frame, or schedule with Notify Me and add the cover in the Instagram app (Edit Thumbnail is unavailable for notification posts). `verified`
- **Falls back to a phone reminder** (not auto-post) for music on Posts/Stories, stickers, product tags, topics, Story links, or personal accounts. Reels with music are allowed automatically. `verified`
- Pinterest via API needs `metadata.pinterest.boardServiceId` (from `get_channel`). `verified`

## 5. Corrections (page disagrees with the earlier report)

1. **Metricool Starter is not "$20 flat".** It is "from $20/mo" billed yearly ($25 monthly) and the price rises with brands (10 brands $36 yr). Metricool API is Advanced only (from $53 yr).
2. **CommentChat has no price of its own.** It sits inside CommentSold Starter at $149/mo plus 6% of sales.
3. **Buffer monthly price:** report gave only $5 yearly. Monthly is $6 per channel (Team $12).
4. **Buffer carousel size:** Buffer's Instagram marketing page says "up to 10 images"; its help article says 20. Need review.
5. **ManyChat API** is not on Essential; Advanced only.
6. **Buffer cover wording:** pricing page lists "Custom video covers" as an Essentials/Team feature while help says no custom cover upload exists. Likely the frame picker; not stated. Need review.
7. **Buffer API platform list** (posts guide) omits TikTok, but the MCP `create_post` text and `thumbnailOffset` doc include TikTok. MCP doc verified, guide list likely stale.
8. Confirmed with no change: Buffer Free (3 channels, 10 per channel, API and MCP), Postiz ($29, 5 channels, 7-day trial; yearly $23), Publer Free (3 accounts, 10 scheduled; API and MCP Business only), Zernio ($12 at 4 accounts), ManyChat Essential ($14 yr; Free 25 contacts), InstantDM (Legend Pro $9.99 yr; Free 5 post automations), Canva Pro $144/yr (monthly $18).

## 6. Could not verify

- Publer: the per-account multiplier. Prices rendered only after a delayed render and the account slider's value was not captured; 4-account totals are `inferred`.
- ManyChat monthly $17 and InstantDM monthly about $12: the Monthly toggle did not render in captures; figures are search snippets (a toggle-click retry returned zero bytes and was deleted).
- Zernio: MCP availability, free-tier rate limits, and whether TikTok or Instagram publishing runs on Zernio's approved apps or needs Ricky's own (and so a registered entity). Docs: https://docs.zernio.com/
- Postiz Cloud: same app-approval question; the FAQ's "app approval" fee is about self-hosting.
- Whether Metricool counts one post to two networks as one or two against the 20/month cap.
- Edits in-app purchase contents; CapCut tier-to-price mapping; Canva trial length.
- Buffer: API-created carousels; alt text on Reels; which feature the "Custom video covers" row gates.
- Any legal-entity requirement for ManyChat/InstantDM accounts (both advertise Meta partner status).
