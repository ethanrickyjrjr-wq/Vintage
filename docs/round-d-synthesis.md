# Round D: how the shop gets found, keeps people and ships safely (synthesis)

2026-10-29. Seven Sonnet lanes from `docs/research-brief-round-d.md`. Full evidence, quotes and URLs are in `research/round-d/d1..d7-*.md`, with raw crawls in `research/round-d/raw/`. This page is the decision layer. It is research, not legal or tax advice.

**How the reports were saved.** The harness refuses report-file writes from subagents. Each lane returned its report as text, and this session saved it verbatim with a one-line header.

**What I re-checked myself.** I grepped the agents' raw captures for the exact quotes below. Everything else is agent-reported from live pages: treat it as "verified by agent" and re-check it before relying on it.
- Shipsurance's "neon items" exclusion and its descriptive-packaging exclusion.
- Etsy Purchase Protection: "up to $250", "first instance per calendar year".
- USPS DMM 609 4.3: "without evidence of damage to the mailing container".
- Etsy calculated shipping: "smallest and cheapest package".
- Kit Free: "10,000 email subscribers", sequences paid. Shopify Email: "10,000 manual or automated emails". Klaviyo: "500 emails/month".
- FCC 26-67: effective "November 25, 2026".
- Fla. Stat. 501.059: "checking a box indicating consent". Fla. Stat. 501.616: "after 8 p.m.".
- 16 CFR 465: "expressing a particular sentiment", "generalized solicitations".
- Google Business Profile: "online-only businesses" ineligible, "travels to customers where they are", "selectively solicit positive reviews".
- Judge.me Etsy Sync skips "sold-out" listings. Etsy Star Seller: "90 days after your first sale". Fla. Stat. 540.08: "express written or oral consent".
- Google merchant listings: the merchant "has to be the seller of the product". Pinterest Product Pins: buyers must "buy the product directly from your site". Merchant Center: refurbished "comes with a warranty".
- DR-15DSS 2026: Lee .5% to Dec 31, 2028; Collier none; Charlotte 1% ending Dec 31, 2026.
- Vintage Market Days: "January 29 - 31, 2027". Pine Ridge: "$160.00". River District Art Walk: "$50".
- eBay Best Offer study (NBER w24306): first offers average 61% of list, bargained sales 73%. Chairish: "more than 50%" of transactions through offers. 16 CFR 233.1: "reasonably substantial period of time". Etsy: an accepted offer does not reserve the item.
- Pinterest merchant guidelines, under "We don't allow the following products to be product Pins": "Pre-owned products", with a Shopping Ads carve-out. Also "Resale or consignment marketplaces are only eligible for Ads distribution".
- TikTok Shop: pre-owned apparel, jewelry and watches "are invite-only categories". "Only eligible sellers may offer Antique Collectibles".
- Meta commerce policy: the only used-goods ban is "cosmetics that have been used". Services can't be sold except through appointments. Buffer free: "10 scheduled posts per channel".

**Three corrections to the agents.**
- **Pinterest Product Pins.** d5 recommends Product Pins from the Shopify listings. Pinterest's merchant guidelines don't allow pre-owned products as Product Pins (d1, re-checked). Organic Pinterest for this shop means plain Pins and Article Pins that link to pages.
- **Shipsurance and stained glass.** d2 says both Shipsurance policies exclude stained glass. The Etsy terms list "windows, plate glass, float glass"; only the Shopify terms add "stained glass". Neon is excluded on both. Verified: neon, float glass. Needs review: stained glass on Etsy-bought cover.
- **The Worker.** d3 says the Worker already has an `/api/hire` route. It doesn't. The only route is `/api/room-preview`, so a subscribe route would be the second.

## A fact from the code that gates several lanes

Items open as `#item-<id>` hash routes inside a dialog (`site/catalog.js`), and `storefront.html` carries no JSON-LD.
- Google indexes the page, not the fragment, so the sold archive, product structured data, Merchant Center and Pinterest pins all need **one real URL per piece**.
- `build.mjs` can generate those static pages from `demo-products.js`. Another session has uncommitted edits to `build.mjs`, so this is a Codex task after that lands.

## Top findings by lane

**d1 social and short video.**
- Niche accounts sell on a fixed weekly drop slot stated in the bio, a teaser the day before, and claims by comment or DM. The repo has already ruled out DM-to-buy because of the double-sell risk, so the only call to action is the listing page: reply "LINK" with the link.
- The answer to "is this still available?" is the page: "It's very difficult for us to hold an item as it could sell at any time" (Palm Beach Regency). Palm Beach Regency is a Florida shop in the same Hollywood Regency lane.
- **TikTok Shop has no lane** for 1960s–80s lamps and glass. Pre-owned there means authenticated luxury, and antiques must be pre-1930. Use TikTok for content only.
- **Instagram and Facebook Shops:** used goods are allowed, but Shops now use website checkout. The site's "checkout coming soon" blocks them. Hire Hollie can't be a catalog item.
- Check Meta's animal-parts rule against the cowhide and feather pieces before any catalog upload.
- Free schedulers fit a weekly batch: Buffer, Publer, Metricool, or Pinterest's own 30-day queue.
- Deliverable: a four-week, hands-only content plan from the real room, the neon and the mirror ball (section "4-week content skeleton" of d1).

**d2 shipping and the unboxing.**
- The packing standard doubles as the claims defense. USPS refuses damage claims where articles were "not properly wrapped" or where the container shows no damage.
- Shipsurance won't pay loss or theft claims when the packaging "alludes to" the contents. So the outside of the box stays plain, and all branding goes inside.
- Etsy calculated shipping undercharges double boxes: it is USPS-only, uses the item's size before boxing, picks the smallest box, and has no handling-fee field. Use fixed shipping classes on Etsy, and flat rates plus a handling fee on Shopify later.
- Etsy Purchase Protection stops at $250 and covers only the first damage claim each calendar year. Insure anything over $250.
- Tightest claim clock: Shipsurance concealed damage, 15 days from delivery.

**d3 email and SMS.**
- Send caps decide the tool, not contact caps. A weekly drop sends to the whole list about five times a month.
  - Klaviyo and Mailchimp free tiers (500 sends a month) cap out near 100 subscribers.
  - Brevo (300 a day) can't send the hour-early alert to more than 300 people.
- **Now: Kit Free.** 10,000 subscribers, unlimited broadcasts, a hosted landing page, tags. No automations, so the welcome email is a manual send.
- **With Shopify: Shopify Email,** 10,000 free sends a month.
- Email law (CAN-SPAM) is opt-out. It needs a postal address (a PO box counts) and a working unsubscribe.
- Texts need prior express written consent, at $500 per violation federally and in Florida. **No SMS until a lawyer reads the consent wording.**
- New FCC rule from Nov 25, 2026: a STOP reply ends all marketing texts from that sender.

**d4 reviews and proof.**
- Product reviews die with a one-of-one listing, and Judge.me's Etsy Sync skips sold-out listings. Proof has to live at shop level: Etsy shop reviews and Judge.me store reviews.
- The FTC rule's safe harbor is inviting every buyer, in the same words, to post an honest review.
- Google and Shopify go further than the FTC: no incentives at all, and no reviews from family. The plan follows the strictest source.
- Most small vintage shops show no stars. Proof comes from tenure, sold counts, curation and authentication.
- A recognizable person in a buyer's photo needs consent under Fla. 540.08.

**d5 search and content.**
- Buy-intent searches go to marketplaces. "Identify / markings" searches go to guides and Facebook threads. That is the opening: maker-and-marks guides shot from the shop's own pieces.
- Sold pages stay up at HTTP 200, marked SOLD, with `OutOfStock` and the real price kept.
- Every piece is `UsedCondition`. Never `Refurbished`: Google defines it as warranty-backed restoration.
- Google merchant listings need checkout on the site. Until then, the site gets product-snippet markup. Pinterest doesn't allow pre-owned Product Pins at all (d1), so pins are plain or Article Pins.
- Brand collision: searching "Holliewood & Vine vintage" returns Poshmark and Etsy "Hollywood" pages. An Instagram handle `@holliewoodandvine` and a Facebook page also exist; ownership is unknown.

**d6 local Southwest Florida.**
- Google Business Profile is only for a business that "travels to customers where they are". d4 confirms that online-only shops are ineligible. So a profile exists only through the in-person Cameo.
- The one real vintage audience is Vintage Market Days, Jan 29–31, 2027, at the Lee Civic Center. The booth fee is unpublished: email sgulfcoastfl@vintagemarketdays.com.
- River District Art Walk ($50) and Pine Ridge ($160 non-refundable, outdoor tent) are cheap tests with eligibility catches.
- Lee 2025: January–March is 33.9% of visitor spending. Local delivery tax: Lee 6.5%, Collier 6%.

**d7 pricing over time.**
- Offers anchor buyers low. On eBay, first offers average 61% of list, and bargained sales land at 73%. Chairish runs more than half its sales through offers.
- Published markdown ladders end near 30% off by day 90 (10/20/30% at 30/60/90 days).
- "Was / now" is a legal claim (16 CFR 233.1). Write "Listed at $X on [date]. Now $Y."
- $245 versus $250 doesn't matter. Crossing a hundred does.
- **The Fabulous From Online prices pay about $38, $49 and $61 an hour** at d7's estimated 2.5, 6 and 12 hours. The benchmark is $75 to $100. The Casting Call is effectively a deposit, not a labor fee.

## X verified, Y need review

- Shipsurance stained glass: see the correction above. Whether a framed mirror counts as "float glass" needs a written answer from Shipsurance.
- Google Business Profile services with prices: the live page says they can carry "descriptions and prices"; a search summary said no. Needs a test on the real account (d6).
- Nextdoor free posts: "unlimited" on the current page, "twice per month" on a blog updated in 2023 (d6).
- Etsy shop score: one Etsy page says a recency-weighted average, another says the last 12 months (d4).
- Sold-page value: `OutOfStock` is in Google's, Pinterest's and Merchant Center's lists; `SoldOut` is Google-only. Only Search Console on the live site will show whether SOLD pages get flagged as soft 404s (d5).
- Quiet hours for texts: federal 8 a.m.–9 p.m., Florida 501.616 8 a.m.–8 p.m. Whether Florida's applies to subscribers who consented needs a lawyer. Follow the stricter one (d3).
- CAN-SPAM ad label: the FTC summary says always, the statute exempts recipients who consented. Keep a light label (d3).

## Decisions for Ricky

1. **Fabulous From Online pricing.** You approved $95 / $295 / $750. d7 puts the real hourly yield well under the shop's own $100 benchmark. Options:
   - keep the prices as launch pricing, but print the hours: "about 2 / 6 / 12 hours of Hollie; more at $100 an hour, never without your yes"
   - raise the prices
   - leave it as is
   Nothing is changed in the build.
2. **Offers.** The owner line says "Absolutely no offers." d7's ladder adds "offers open at day 30". My pick: keep no-offers as the brand, and let the markdown ladder be the quiet discount. One voice, no haggling anchor.
3. **Will the site take payment?** This sharpens decision 2 of the earlier synthesis. Without checkout on the site:
- the site gets product-snippet markup only
- Google free listings come from Shopify
- Instagram and Facebook Shops stay closed (d1)
4. **One spelling everywhere.** Google's name rule wants the name used "consistently". Pick "Holliewood and Vine" or "Holliewood & Vine" for Google, Etsy, Nextdoor and the site.
5. **Are `@holliewoodandvine` on Instagram and the matching Facebook page yours?** If not, claim a handle now.
6. **Google Business Profile** only if Hollie really will visit homes (the Cameo). Video calls alone don't qualify.

## New ideas, ranked

| # | Idea | Call | Why |
|---|---|---|---|
| 1 | One page per piece that stays up when sold (200, SOLD, `OutOfStock`, `UsedCondition`, "find me one like it") | **keep** | It unlocks search, Pinterest and the sold archive at once. Today items are hash routes (d5 plus the code) |
| 2 | Plain outer box, "open it on camera" on the card, a 15-second packing reel | **keep** | One habit is the claim evidence, the content and the insurer's condition (d2) |
| 3 | First dibs, an hour early: Kit Free list, signup as a hunt form with tags, box-card QR, never auto-add buyers | **keep** | Free to 10,000 subscribers, and it fits the decided weekly drop (d3) |
| 4 | Proof that isn't stars: a "Rehomed" count, "Checked by Hollie" on lamps, a "Where it landed" photo page with logged consent, the same neutral ask to every buyer | **keep** | A new shop has no reviews. This is what small vintage shops actually show (d4) |
| 5 | Drop Day markdowns: steps at days 30/60/90, a Recently Reduced shelf, "Listed at $X on [date]. Now $Y." | **keep** | Rides the weekly drop, keeps "no offers" true, and stays inside 16 CFR 233 (d7) |
| 6 | Maker-and-marks guides shot from her own stock (Stiffel base, pink glass, cut vs pressed) | **keep** | Identification searches are won by guides, and first-hand photos beat the retailer guide (d5) |
| 7 | Vintage Market Days booth Jan 29–31 as a lead source, with a Screen Test QR card | **keep** | The only true vintage audience locally, and it falls in the January–March peak (d6) |
| 8 | Fixed shipping classes A–D, "ships double-boxed, insured to sale price" on the listing, a lamp parts bag | **keep** | Calculated shipping undercharges double boxes, and the line supports the "matches description" test (d2) |
| 8b | Four weeks of hands-only posts from the real room: a fixed drop slot in the bio, a teaser the day before, a "Here / Gone" legend, captions edited to "Gone.", "LINK" replies only | **keep** | It is how the niche sells, minus DM claims, and needs no new stock to start (d1) |
| 9 | "Found a home, here's its cousin" email sent by hand after each sale | maybe | Nobody has a template, so it's hers to own. It's manual work every sale (d3) |
| 10 | "Send it north": ship to the buyer's northern home after the season | maybe | Real seasonality (Lee January–March). Needs shipping classes first (d6) |
| 11 | 48-hour hold card used everywhere | maybe | Chairish holds expire at 48 hours. Overlaps the decided list-member hold (d7) |
| 12 | Layaway, the Slow Burn: 25% down, six months, $300+ | maybe | Real vintage practice, but a lawyer first (d7) |
| 13 | Free local delivery in Lee and Collier for big pieces | maybe | Only once the Cameo or a van exists (d6, d7) |
| 14 | SMS hour-early alert | cut for now | $500 per text exposure. A lawyer reads the consent first (d3) |
| 15 | Etsy free-shipping guarantee turned on shop-wide | cut | It covers every item at $35 and up, which is the whole shop, heavy glass included (d2, d7) |
| 16 | Offers from day 30 | cut | Conflicts with "Absolutely no offers" and anchors buyers at 61% (d7), unless Ricky decides otherwise |
| 17 | Review incentives of any kind, including the mirror ball after a review | cut | Google and Shopify ban them (d4) |
| 18 | TikTok Shop, Instagram/Facebook Shops, Pinterest Product Pins | cut for now | No TikTok lane for this stock. Meta needs site checkout. Pinterest bars pre-owned Product Pins (d1) |

Ideas 1–8, 8b and 11–12 become idea-room pages or amendments (`docs/codex-handoff-idea-room.md`, section 8).

## Needs a lawyer, an accountant or an account

- **Lawyer (Florida):**
  - SMS consent wording, and whether 501.616 applies to texts to subscribers who consented
  - the buyer-photo release and how it is revoked
  - layaway terms
  - was/now price wording
  - whether a free Screen Test needs disclosing on testimonials
  - whether a live sale with claims or bids is a regulated auction in Florida (d1; the source covers only Colorado and South Carolina)
- **CPA (Florida):** tax on shipping and handling charges, and on gifts in the box.
- **One email:** ask Shipsurance in writing whether framed mirrors, stained-glass shades and neon are covered.
- **Accounts Ricky creates:**
  - Kit (free)
  - a sending domain with SPF/DKIM
  - a PO box for the CAN-SPAM address
  - Etsy and Shopify
  - Google Search Console
  - Instagram Professional, a Facebook Page, a TikTok Business account and a Pinterest business account
  - Nextdoor
  - Google Business Profile, only with the Cameo live
  - a Vintage Market Days vendor profile (free)
