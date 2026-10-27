# Site ideas and consignment: synthesis of ten research reports

2026-10-27. Ten Sonnet agents, two groups of five. Full evidence, quotes and URLs are in `research/site-ideas/a1..a5-*.md` and `research/consignment/b1..b5-*.md`; raw crawls under each `raw/`. This page is the decision layer. Research, not legal or tax advice.

**Verification status.** I re-checked these myself against captured live pages: Florida ch. 538 (flsenate.gov, 2026 text), Chairish's 40% consignor rate, Buffalo Exchange's 25% cash / 50% credit, Etsy's 20-year vintage rule. Everything else below is agent-reported from live pages and not independently re-verified. Treat figures as "verified by agent", and re-check before you rely on one.

## Group A: look, flash, setup

**The lane is open.** Almost no vintage reseller is loud on the web (a1: 15 shop sites tried, one genuinely maximalist; a3: the design galleries contain almost no vintage-resale sites). Holliewood and Vine's disco/WebGL room is already ahead of the field.

**Flash, ranked by wow per effort (a3).** All build on the existing `disco.js` / `atmosphere.css` / `storefront.js`, no new libraries.
1. Drag-to-spin the mirror ball.
2. Light glints steered onto chrome and glass on product cards.
3. Neon and wordmark breathing with the music.
4. Mirror-chip burst on the primary button.
5. Phone-tilt light sweep, requested inside the "Start the disco" tap.
Rule: anything always-on must be static or paused under `prefers-reduced-motion`; motion that starts only after "Start the disco" is conversion-safe. Rejected: arcade game, camera gestures, boot screens, retro-OS desktop, Frutiger Aero, full-page glitch, per-item 3D, fake hit counters.

**Structure worth stealing.**
- Room-scene pages built from the real room photo: named scenes, one wide photo, one sentence, a rail of the real pieces, sold pieces left up tagged "gone" (a2). Nobody in vintage has true pin hotspots yet, which makes that a differentiator, ranked below the cheap wins.
- Objects as navigation (James Veloria, a1): a statue, a dress and a poster are the nav. Steal the structure, not the illustration budget.
- Public sold archive, doubling as a "tell us what you're hunting" form (a1, a2, a4).
- Condition vocabulary plus per-item condition notes (Joy of Cocktails, Show Pony), and a lamp spec block: bulb base, wattage, wiring, drop (The Old Above) (a2).
- First-person item voice, flat measurements, a visible "I have a question" button (Shrimpton, a1). A note card in the package (Kiko, a1).
- Weekly fixed-time drop (a4). Shopify can schedule it on the Online Store only; Etsy shows no scheduler.
- Disco ball: pack it in the box. Do not build cart logic. It stays a buyer gift, not an every-order promise.

**Skip.** DM-to-buy (double-sell risk with one-of-one stock on three channels), appointment showroom (contradicts the "reference room, not a public store" brief), mystery bundles, VIP tiers, 360/3D spin, weekly live selling (monthly event at most).

**Setup facts that change the plan (a5).**
- Etsy "vintage" means 20+ years old. 70s-90s fashion is fine. Y2K and newer pieces, new disco balls, and catalog item C7 (2016-17) cannot be listed on Etsy. Every Etsy vintage listing needs a label or maker's-mark photo ("estate sale" is not proof).
- Which storefront customers land on decides the stack. If it is the hand-built site, a paid Shopify theme ($220-$420) is wasted money; Shopify's Storefront Web Components embed in plain HTML. Open: whether ChatGPT Sites allows external Shopify scripts. Nobody checked.
- Quantity-1 needs no paid app: Shopify collection condition "Inventory stock is greater than 0" hides sold pieces.
- Crosslist Gold ($39.99/mo) stays the only tool whose docs state cloud auto-delist across Etsy, eBay and Shopify, consistent with `docs/dashboard-design.md`. Turn Etsy auto-renew off for one-of-ones until checked.

## Group B: consigning and buying

**Must the owner ship it to us? It depends on the model, and the answer isn't simple.**
- Mail-in platforms: owner ships to them, free prepaid label or bag (The RealReal, ThredUp, WGACA, Beacon's Closet). b1.
- Owner keeps it, ships only after it sells: exists only on marketplaces where the owner stays the seller (Chairish seller-managed shipping, Poshmark, Vestiaire Direct). b2, b4.
- No branded shop publishes "owner keeps it, we list it" terms, so that model would be invented, not copied. b4.
- If our own site sells the item, we are merchant of record and, by b4's reading of F.S. 212.05965, a Florida "marketplace provider": we owe the tax, refunds and chargebacks without ever touching the box. The clean alternative is the owner staying the seller on their own Chairish or eBay account while we coach them for a fee.
- Etsy is the high-risk channel for third-party items (drop-shipping ban; Etsy's seller policy pages were walled, so no explicit ban is confirmed).

**Florida gate (assumes the shop is in Florida; confirm).** I read the 2026 statute text (https://www.flsenate.gov/Laws/Statutes/2026/Chapter538/All, raw capture `research/consignment/raw/b3-fl-ch538-2026.md`; Department of Revenue page https://floridarevenue.com/taxes/taxesfees/Pages/secondhand_dealers_recyclers.aspx). As written, the rules below apply unless an exemption fits, and exemptions are listed after them:
- Ch. 538.03: "Acquire" means to obtain by purchase, consignment, or trade. Buying, consigning and trading are all regulated.
- "Secondhand goods" excludes clothing, books, coins, office furniture and pianos (full list in the statute). So fashion is likely out of scope. Lamps, glass, art, decorative objects and fine jewelry are in. Playboys and signed memorabilia are unclear.
- Registration with the Department of Revenue, $6 per location. Report each acquisition to law enforcement within 24 hours. Seller ID, thumbprint and photos (per b3/b5).
- 538.06: you may not sell, alter or dispose of goods for 15 calendar days, or 30 for antique decorative objects, art, jewelry, precious metals and gemstones.
- 538.06(2): a dealer must maintain actual physical possession of secondhand goods throughout a transaction. No agent flagged this. Whether it blocks hold-and-ship depends on the exemptions below, so it is a question for an attorney, not a settled blocker.
- **Exemptions in 538.03(2) that could take an online shop out of ch. 538.** I read them; whether any fits is for the attorney or the Department of Revenue to say. Two agents (b3, b5) did not surface these in their summaries, and b5 listed the online-seller carve-out as unverified.
  - (l) A business registered with the Department of Revenue for sales tax as an antique dealer under ch. 212 that buys from the owner at the owner's residence under a written agreement stating the owner's name, address and phone.
  - (m) A business that contracts with others to offer goods through a website and "maintains a shop, store, or other business premises for this purpose," if eight conditions hold: public viewing at no charge; 2-year records; serial numbers on the records and the listing; listings searchable by state or zip; business names given to law enforcement; premises open to inspection; payment only by check or a licensed money services business to the person who contracted; and either a stolen-article database check 48 hours after contracting or an electronic report to law enforcement within 24 hours. Whether the room counts as "business premises" decides this one.
  - (n) A person offering their own property, or a person or entity offering others' property, through a website "when that person or entity does not have, and is not required to have, a local occupational or business license for this purpose." A shop that holds a local business tax receipt may not qualify. Unresolved.
  Net: an online-only consignment model might be exempt, but only if it fits one of these. Treat the whole Florida question as undecided until a Florida attorney or the Department of Revenue answers it.
- Also (b5): the art statutes (686.502-.503) may make "left at consignor's risk" unenforceable for art. Consignee collects sales tax on the full price (Rule 12A-1.081, read on a mirror only). 1099-K threshold is $20,000 and 200 transactions; 1099-NEC/MISC is $2,000 for tax years after 2025, and the IRS lists "payments for merchandise" as not reportable, which a CPA must confirm.

**Benchmarks.**
- Chairish: 40% flat for a new Consignor (seller nets 60%). Chairish's own pages disagree on the worked $40k example, so treat the tier table as the source.
- Local Naples showrooms (The Find, Posh Plum): 50/50 for 90 days, markdown ladder (10% off from day 31, 20% from day 61), risk of loss on the consignor. Posh Plum does not accept glassware or light fixtures.
- The RealReal clothing keeps: 20% under $100 up to 70% at $5k+. Buffalo Exchange: 25% cash or 50% credit. Crossroads: 25/35/40% cash by band or 45% trade.
- Unsold, slow, or unpaid risk is real: ThredUp 38% unsold and 10-20 weeks to cash; Rebag about 22 business days plus 15 after a sale; Kaiyo collapsed in 2024 and left sellers unpaid.

**Recommendation (b1, b3, b4, b5 converge).**
1. Launch buy-only for soft goods first, because clothing sits outside ch. 538. Use a photo-gated flow modelled on Beacon's Closet (3 photos per piece, 48-hour answer, prepaid mailer only at 5+ accepted) and WGACA's email quote for high-value pieces. Cap the spend: buying turns a no-cash business into a cash-out business, and one-of-one stock has no turns. Never auto-accept on silence (Rebag does). Skip credit bonuses at launch.
2. Hard-goods consignment (lamps, glass, art, furniture): invite-only and in person, after talking to a Florida attorney and the Department of Revenue. Take possession. Copy the showrooms' clauses: 90 days, 50/50, markdown ladder, abandonment date. A web form can only be a pre-screen.
3. Skip Stripe Connect and Shopify multi-vendor apps for now (each consignor needs KYC, you still eat chargebacks, and Shopify Payments terms restrict acting as a payment intermediary). Track consignors in a spreadsheet until volume hurts.

## Discrepancies, "X verified, Y need review"
- Chairish: tier bounds verified; its two $40k examples and plan details disagree across its own pages.
- Rebag: whether a declined revised offer ships back free (old help article says yes, new one silent).
- Vinterior: "100,000 pieces" vs "200,000+" on the same page.
- Bintagged: Copenhagen (own site) vs Spain (2024 article). James Veloria: About page address vs contact block.
- eBay Trading Assistants: FAQ still live on ebay.com.my, but a third party says the program is retired; eBay's "20-40%" consignment rate comes only from that third party.
- Dashboard drift: Crosslist says sales "usually detected within 15 minutes", the dashboard doc says "up to"; LitCommerce says near real-time, the dashboard doc says 15 minutes.
- Rule 12A-1.081 text verified on a mirror only; its citation history differs from the official page.

## Blocked or unverified
AptDeco, Sotheby's Home, Etsy seller/creativity policies, Poshmark terms and fees, Fashionphile terms, Club Vintage, Rejuvenation vintage, Poolsuite. Visuals in group A are inferred from page text and markup; nobody saw a rendered page.

## Decisions for Ricky
1. Is the shop Florida-based, and does it hold (or need) a local business tax receipt? Everything in the legal section assumes Florida, and exemption (n) turns on the license.
2. Which storefront is primary: the hand-built site or a Shopify theme? That decides whether to spend $220-$420 on a theme at all.
3. Soft-goods-first buy flow now, hard-goods consignment later: yes or no?
4. Want screenshots of the top 5 or 6 reference sites (James Veloria, The Kitschy Maximalist, Soho Home Shop the Look, The Old Above, Shrimpton) from your signed-in Chrome to judge the look?
