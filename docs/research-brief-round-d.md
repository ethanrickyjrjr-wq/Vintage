# Research brief, round d: the gaps (for an Opus session to send out a group of Sonnets)

Written 2026-10-29 by Claude. Ricky: "write the other research for opus to send out a group of sonnets".

Three earlier rounds covered:
- **(a)** how the site looks and works, and platform setup
- **(b)** consignment and buying
- **(c)** the Fabulous From Online service

None looked at how the shop gets found, keeps people, and ships safely. This round does, in seven lanes.

**What comes out:**
- seven reports in `research/round-d/`
- one synthesis at `docs/round-d-synthesis.md`
- new ideas that survive, added to the idea room for Hollie (`docs/codex-handoff-idea-room.md`)

## How to run it (the Opus session)

1. **Read first:**
   - `CLAUDE.md`
   - `docs/site-ideas-and-consignment-synthesis.md`
   - `docs/fabulous-from-online-design.md`
   - `docs/codex-handoff-idea-room.md`

   They hold what is decided and what's already an idea. Don't send agents after those.
2. **Spawn.** Spawn the seven lanes below in ONE message, in parallel:
   - Agent tool, `subagent_type: "general-purpose"`, `model: "sonnet"`, background.
   - Each prompt is the **shared preamble** followed by that lane's brief. Paste both verbatim; the agents see nothing else.
   - Cut a lane if Ricky says so, but don't merge lanes. Narrow briefs come back better.
3. **While they run.** Don't redo their work. Do the local reads the synthesis needs:
   - the current homepage and the idea pages
   - `site/build.mjs`
   - `site/room-worker.mjs`
4. **Vendor First on you.** Before the synthesis names a vendor price, a statute or a platform policy as **verified**, re-check it yourself in the agent's raw capture of the live page, or crawl it again. Everything else stays "agent-reported".
5. **Write `docs/round-d-synthesis.md`.** It is the decision layer, about 2 pages:
   - the top findings per lane
   - "X verified, Y need review" wherever sources disagree
   - a ranked list of new ideas, each marked keep / maybe / cut with a one-line reason
6. **Ideas that survive.** Append them to `docs/codex-handoff-idea-room.md` as new `idea-*.html` pages in its section 5. Use the same shell, a one-line "Why" with sources, and a mock description, then bump the page count in its test. Codex builds them; you don't.
7. **Commit and push.** Run a secrets grep (raw captures can contain cookies; redact `set-cookie` values). Use pathspec `git add` for `research/round-d/` and the two docs, then `git pull --rebase` and push. Other sessions commit to this tree, so never `git add -A`.
8. **Report to Ricky:**
   - the five strongest new ideas
   - anything that changes an earlier decision
   - anything that needs a lawyer, an accountant or an account he has to create

## Shared preamble (paste at the top of every agent prompt)

```
CONTEXT
You are one of seven Sonnet research agents for Holliewood and Vine (also "Holliewood & Vine"). The spelling is
Hollie, with ie; never write "Hollywood" for the shop. Hollie (she/her) is the stylist and the eye behind it.
- A vintage resale shop going online: Etsy, Shopify, and a hand-built site on ChatGPT Sites (static pages plus a
  small Worker with a D1 database; no accounts or keys exist yet for Etsy, Shopify or email tools).
- Stock: one-of-one vintage home pieces (brass lamps, pink and cut glass, mirrors, art, chairs, rugs) and some
  vintage fashion. Look: burgundy walls, Hollywood Regency, chrome, a pink "do it for the plot" neon, disco balls
  (a mirror ball is sometimes a gift in the box, never promised with every order).
- Voice: short, witty, a little vain ("Collector of good things. Excellent taste. Absolutely no offers.").
- There is a service, "Fabulous From Online": people hire Hollie to find a piece or style a corner, a room or a home,
  by video call, photos or email.
- Assumption: based in Southwest Florida (Lee and Collier counties). No public showroom.
- Already decided or already an idea (do NOT re-research): weekly drop, sold archive, wish list, vibe navigation,
  room looks, condition grades, lamp spec block, the box card, live selling monthly at most, Crosslist for
  cross-posting, Florida ch. 538 secondhand rules, ch. 481 interior design wording.

TOOLS (Windows machine; use the Bash tool, POSIX syntax only; run from /c/Users/ethan/dev/Vintage)
- Search: tools/search.sh "query"   prints url | title | engine
- Crawl:  tools/crawl.sh "<url>" research/round-d/raw/dN-<short-name>.md   (always a unique path)
  crawl.sh already handles env -u MSYS_NO_PATHCONV, < /dev/null and -bc. Under 1 KB is a bot wall, not a
  page: note it and move on, do not try Patchright. WebFetch / WebSearch are acceptable fallbacks; say which.
- Vendor rule: every vendor price, limit or policy comes from the vendor's LIVE page this session, quoted with
  URL and access date. Training memory is not evidence. Laws come from primary text (flsenate.gov, ecfr.gov).
- Aim for 15-25 real pages. Quality over count.

OUTPUT
Write exactly one file: /c/Users/ethan/dev/Vintage/research/round-d/dN-<slug>.md, raw captures in
research/round-d/raw/dN-*. Match the format of research/fabulous-from-online/c2-vintage-sourcing.md (read its
first 60 lines):
- "# dN: <topic>", "Agent dN, accessed <date>.", a method line
- TL;DR, 5-8 numbered findings
- per source: URL, raw filename, verbatim evidence in quotes, each claim tagged `verified` (read live this
  session), `inferred` or `unverified`, and a "Steal this:" line
- "X verified, Y need review" wherever sources disagree
- a recommendation for Holliewood & Vine, in two parts: what to do now (no accounts needed) and what needs an
  account, a fee or a lawyer
- an "Ideas for Hollie" list: 5-10 concrete ideas, each one line, each tagged with the source that inspired it
No fabricated examples, customers or numbers. Do NOT run git. Do NOT edit anything under site/ or docs/.
Final reply: the file path plus your TL;DR, under 250 words.
```

## The seven lanes

### d1: social and short video (`d1-social-video.md`)

How do one-of-one vintage home and fashion shops sell on Instagram, TikTok, Pinterest and Facebook?
- **Accounts.** Study 8–12 real accounts in the niche (vintage home, Hollywood Regency, glassware, vintage fashion), with handles and URLs. Note:
  - post formats (styling reels, "claim it" posts, drop teasers, before-and-after rooms, packing videos)
  - posting rhythm
  - link-in-bio setup
  - how they handle "is this still available?"
- **Platform rules from the live pages:**
  - TikTok Shop and Instagram/Facebook Shops: eligibility and rules for vintage or pre-owned goods
  - Pinterest as a search engine for decor
- **Free schedulers:** live free-tier limits.
- **Deliverable:** a 4-week content skeleton in the shop's voice, using the real room, the neon, Hollie's hands and the mirror ball. Each week has a theme. Each post gets one line and the page it links to.

### d2: packing, shipping and the unboxing (`d2-shipping-unboxing.md`)

How do small shops ship glass, lamps, mirrors and framed art without breakage or lost claims?
- **Carrier rules** from the live UPS, USPS and FedEx pages: packaging guidelines, double-boxing, insurance limits, what a damage claim requires (photos, the original box).
- **Lamps:** bulb, harp and shade packed apart; finials.
- **Costs:** materials and suppliers; free sources such as liquor-store dividers.
- **Pricing shipping:** flat vs calculated on Etsy and Shopify, from their live help pages.
- **The extras in the box:** the cost of the mirror-ball gift and the insert card.
- **Unboxing as content.**
- **Deliverable:**
  - a packing standard per item type (glass, lamp, mirror, art, fashion)
  - a shipping-price rule
  - a claims checklist

### d3: email and SMS (`d3-email-sms.md`)

How should a one-of-one shop collect and use emails and texts?
- **Tools.** Live free-tier limits for Shopify Email, Klaviyo, Kit, Mailchimp, Brevo and Beehiiv: contact caps, sends, forms, whether a form works on a static site by link or embed.
- **Flows that fit one-of-ones:**
  - welcome
  - drop alert, sent an hour early to the list
  - wish-list match
  - "it's gone, here's its cousin"
  - after a purchase: care and "find me another"
- **Law, from primary text:**
  - CAN-SPAM (16 CFR 316)
  - for texts, the TCPA and Florida's Telephone Solicitation Act (Fla. Stat. 501.059, including its 2021 and 2023 amendments): consent, quiet hours, opt-out wording
- **Deliverable:**
  - the three flows written in the shop's voice: subject line plus three lines each
  - a recommended tool now (no Shopify yet) and later (with Shopify)

### d4: reviews and social proof for a new one-of-one shop (`d4-reviews-proof.md`)

How does a shop with no repeat products and no reviews yet earn trust?
- **Shop-level reviews** where products never repeat: Etsy shop reviews, Google Business Profile reviews, Judge.me's free tier, and Shopify's options. Check what's live; Shopify retired its own reviews app.
- **The FTC's 2024 rule on reviews (16 CFR Part 465)**, from primary text: fake reviews, buying reviews, suppressing bad ones, incentives.
- **An "in its new home" photo program:** customers send a photo of the piece in their room. Cover consent and usage-rights wording.
- **Press and feature mentions** as proof.
- **How small vintage shops display proof today:** 5+ examples.
- **Deliverable:**
  - a 90-day plan to get the first 10 genuine reviews within the FTC rule
  - the photo-consent line

### d5: search, Pinterest and content (`d5-search-content.md`)

How do people find vintage home pieces online, and what should the shop's pages do about it?
- **What ranks:** sample real results for 10 target searches, e.g. "vintage brass table lamp", "pink depression glass coupes", "Hollywood Regency decor", "vintage bar cart styling", "Stiffel lamp". Note which page types win: marketplace listings, shop collections, guides.
- **Google's live docs:**
  - Product structured data for one-of-ones (availability values for sold pieces)
  - Merchant Center free listings for used or vintage goods (the condition attribute)
  - what to do with sold pages: keep, redirect or 404
- **Era and maker guide pages** as content.
- **Pinterest Rich Pins.**
- **Deliverable:**
  - the page types the site should add, in order
  - the structured-data fields for a listing and for a sold listing
  - five guide-page titles in the shop's voice

### d6: being local in Southwest Florida (`d6-local-swfl.md`)

How does an online shop with an in-person service show up locally without a storefront?
- **Google Business Profile** as a service-area business with a hidden address, from Google's live guidelines. Can it list "Fabulous From Online" as a service?
- **Nextdoor** business pages.
- **Local markets and pop-ups** in Naples, Fort Myers, Cape Coral and Bonita Springs: names, dates, booth fees, rules.
- **The snowbird calendar** (October–April) and seasonal events.
- **Estate-sale companies and auctions as sourcing.** Note ch. 538 only by pointing to the prior research.
- **Partners:** local interior designers and stagers, and trade programs.
- **Local press:** Gulfshore Life, Naples Daily News and News-Press home sections; how to pitch.
- **County sales-tax surtax** for local delivery in Lee and Collier, from the Florida Department of Revenue's live page.
- **Deliverable:**
  - a local plan for this season
  - the three events worth a booth, with dates and fees

### d7: pricing and selling one-of-ones over time (`d7-pricing-over-time.md`)

How do one-of-one shops set prices, lower them, and take offers?
- **Use, don't redo,** the comps in `research/pricing/`. Read `research/pricing/SUMMARY.md` first.
- **Markdown ladders** for aging stock, with real shop policies.
- **Offer features,** from the live pages: Etsy's, eBay Best Offer, Chairish offers, and what they do to the price buyers expect.
- **Public price-drop days**, e.g. "Sunday price drops".
- **Bundles, holds and layaway.**
- **Free-shipping thresholds** vs heavy, fragile pieces.
- **How vintage shops show prices:** $245 vs $250, "was / now".
- **A time check on the Fabulous From Online prices:** how many hours a Casting Call, a Close-Up and a Leading Role take, from published designers' process descriptions. Does $95 / $295 / $750 pay Hollie a sane hourly rate?
- **Deliverable:**
  - a markdown ladder
  - an offer policy in the shop's voice
  - an hours-per-tier table with the implied hourly rate

## Already covered (agents and the synthesis should not repeat these)

| Folder | Covers |
|---|---|
| `research/site-ideas/` (a1–a5) | Look, flash, merchandising mechanics, platform setup |
| `research/consignment/` (b1–b5) | Consigning, buying outright, Florida ch. 538 |
| `research/fabulous-from-online/` (c1–c6) | E-design pricing, sourcing fees, events and rush, intake and booking, Florida ch. 481/489/501, copy |
| `research/dashboard/` (01–10) | eBay, Etsy and Shopify APIs, Crosslist, sourcing alerts, ops dashboard |
| `research/pricing/` | Item comps for the original inventory |
| `research/3d-capture/`, `research/room-editor/`, `research/disco-visuals/`, `research/music-*` | The 3D showroom, room editor, disco and music |
| `research/type-and-spacing-2026-10-29/`, `research/account-layout-2026-10-29/` | Typography and the account preview (other sessions) |
