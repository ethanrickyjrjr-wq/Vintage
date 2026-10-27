# Hollywood and Vine: project brief for NotebookLM

Written 2026-10-27 from the project's own files and fresh research. Upload this as one source; it is self-contained.
Confidence tags used throughout: **VERIFIED** (read from a primary page or our own data this session), **COMP** (price evidence from listings), **JUDGMENT** (our estimate, no comp), **BLOG** (reseller-industry articles, directional only), **NEEDS REVIEW** (open or conflicting).

---

## 1. The one-paragraph version

**Hollywood and Vine** is a vintage resale shop owned by Ricky Cooper. It started as a physical room: burgundy walls, racks of 70s to 90s clothes, lamps, art, a pink "do it for the plot" neon sign, a chalkboard that says "come on in, get lost", disco balls, Marilyn and Elvis on the walls, and a cowhide over a rust mid-century sofa. The job now is to put that room online: list the inventory on **Etsy and Shopify** (and eBay through a crosslister), with a custom storefront as the brand home. On 2026-10-26 we catalogued the first batch of stock, priced it from market comps, built a sample storefront, and designed (but have not built) an operations dashboard that tracks sales, profit, inventory and buy opportunities from a phone.

The brand is maximalist 70s to 90s glam with a little punk. It is not farmhouse and not minimalist.

---

## 2. What we are trying to do

**Goal:** turn a room full of curated vintage into a profitable online business that feels like walking into that room, and run it with as little admin as possible.

**What we want to accomplish, in order:**

1. **List what we already own.** About 39 catalogue entries (some are bundles) across lighting, decor, art, memorabilia, magazines and clothing. The "needs photo" items are the bottleneck; Ricky is re-shooting them.
2. **Price correctly.** Use sold prices, not asking prices, and catch the few items whose price could swing 4x on one fact (a maker stamp, a signature certificate, a label).
3. **Be a brand, not a bin.** A storefront with a point of view: dimensional lettering, objects in the foreground, framed displays, a disco-ball signature. Disco balls are a signature gift or handout for buyers (confirmed by Ricky); we do not promise one with every order.
4. **Run the back office from a phone.** One installable app that answers: What sold? What do I own? What should I go buy? What needs me right now? Plus listing from the phone: photos and one line in, Claude drafts the Etsy listing, Ricky taps Publish, and a crosslister fans it out to eBay and Shopify.
5. **Buy smarter.** Watch eBay for pieces that fit what Ricky wants at a price cap, and alert the phone. Never auto-buy.

**Evaluation lens for every decision:** is it better for building, coding, customer utilization, brand, or growth?

**Principles that shape the work:** verify vendor facts against live docs before building on them; surface disagreement between sources as "X verified, Y needs review"; cite the source homepage for any data; the owner decides structure changes.

---

## 3. What we know (current state, as of 2026-10-27)

### 3.1 Source material
- 10 listing photos (iPhone, up to 4284x5712) and a 24-second walkthrough video (compressed to 568x320, not listing quality). Originals live in Ricky's Google Drive.
- Two photos (the cubist painting and the ink face) were shot at an angle with glare; they need a square-on re-shoot, no flash.

### 3.2 Inventory (39 catalogue entries)
Grouped the way the shop thinks about them:

| Group | What is in it | Count |
|---|---|---|
| **A. Lighting, decor, art, memorabilia** | Stiffel-style brass and cream urn lamp; two-tier frosted sea-glass chandelier; cubist acrylic painting; framed ink-and-wash face; Elvis 8x10 signed by Scotty Moore and D.J. Fontana; pair of silver mannequin busts; 8mm film projector; pink stemware (about 12 pieces); black and gold cocktail shaker; cut crystal decanter; gold bust lamp; ceramic leopard; black armchair with star cushion; retro turntable; brass hurricane lamps; cowhide throw; white ribbed sculptural chair; paint-splattered dress form; upcycled sneaker-leather collar art | 19 |
| **B. Clothing and accessories** | Blush faux-leather trench; paisley jacket; 1950s to 60s feather cocktail hat; leather chain harness belt; gray fringed western boots; 90s neon windbreaker; gold chain necklaces; navy shirt dress; red lace dress; neon track jacket plus paisley leggings; colorblock blouse and red embroidered jacket; four pairs of shoes | 12 |
| **C. Print** | Playboy (Jan 1997 Marilyn issue, Apr 1991, Dec 1989, Jan 1970), Penthouse Sep 1977, "Midnight Playmates" special, a college-football magazine, a Chanel coffee-table book | 8 |

Fixtures seen but probably not for sale: neon sign, gold étagère, chalkboard, posters, clapperboard, dartboard, mirror, rug. A running joke: the owner's mirror selfie is "priced at $10,000,000, not for sale".

### 3.3 Pricing (COMP and JUDGMENT)
Method: Sonnet subagents crawled comps; eBay sold pages require sign-in, so sold prices were read through Ricky's signed-in Chrome. Poshmark sold prices crawl fine. Etsy and eBay search pages block our crawler, so many comps are **asking** prices, which run higher than sold prices.

**Total list value of everything except fixtures: about $3,190 at target prices.**

| Group | Approx. target total | Share of value | Typical item |
|---|---|---|---|
| A. Decor, lighting, art | about $2,505 (19 items) | about 79% | $28 to $275 |
| B. Clothing | about $590 (12 entries) | about 18% | $14 to $58 |
| C. Print | about $91 (8 items) | about 3% | $4 to $20 |

**Takeaway for strategy: roughly four-fifths of the value sits in 19 objects. Magazines are add-ons, not a business.** Clothing is cheap per piece, so it only works as volume.

Items where **one fact moves the price a lot** (check these before listing):

| Item | Base target | Swing | The deciding fact |
|---|---|---|---|
| White ribbed sculptural chair | $275 | up to about $700 to $1,150 | Possibly a Frank Gehry "Wiggle Side Chair" (Easy Edges 1972, Vitra reissue 1992; 34.25 in tall matches). Look for a Vitra or Easy Edges label. A white one is probably painted or a copy, which cuts collector value about 40%. |
| Elvis photo signed by Moore and Fontana | $140 | about $60 to $300 | Not Elvis's signature. Third-party authentication (JSA-certified dual-signed asks run $290 to $573; unauthenticated about $180). PSA/DNA two-signature fee runs $20 to $125 by signer tier, about 30 business days. |
| Stiffel-style brass urn lamp | $95 | about $45 to $325 | A STIFFEL stamp or label under the base. Stamped singles ask about $300 to $500; unmarked is judged at 40 to 60% of that. |
| Ceramic leopard | $125 | $45 to $345 | Maker mark. Ronzan, Bitossi, Fanciullacci, Zaccagnini and Lenci are the premium tier; "Italy" only is mid. |
| Cubist acrylic painting | $275 | $150 to $450 | Hand-painted original versus factory decor canvas; check the back for labels. eBay sold comps for similar cubist acrylics: $127 to $550 (a signed Brazilian artist at $550). |
| Gold bust lamp | $110 | to $200+ | Resin reproduction versus genuine chalkware. |

### 3.4 Discrepancies (rule: "X verified, Y needs review")
- **Verified:** the master price table and the five category reports agree on the structure of the catalogue and on the fashion, print and magazine ranges.
- **NEEDS REVIEW: A1 lamp basis.** The master table says the $95 target is based on "eBay sold", but the saved sold-comps file contains no Stiffel or pineapple-lamp lines. The category report instead says $325 stamped and $175 unmarked (judgment). Treat $95 as unverified until a Stiffel sold search is pulled through the signed-in browser.
- **NEEDS REVIEW: A2 chandelier.** Master table says "no comps, judgment, $125". The sold file does show two *French sea-green glass* chandeliers at $605 and $799, but those are 6 to 10 light dining-room pendants, a larger and different format. Not a direct comp, but it argues $125 may be low.
- **NEEDS REVIEW: master table versus category reports.** Where eBay sold data was found, the master table is lower than the category reports (Elvis $140 vs $180; Playboy 1997 $14 vs $18; Penthouse 1977 $14 vs $22; feather hat $48 vs $58). The master table is the later, sold-based number; the category reports lean on asking prices.
- **NEEDS REVIEW: Chanel book.** Title unconfirmed; priced as a guess at *Chanel: Collections and Creations* (Bott, 2007). Do not list blind.
- **NEEDS REVIEW: Playboy 1970 issue.** Identified by visual match to a thumbnail only.
- **NEEDS REVIEW: mature-content rule.** Etsy is believed to require mature-content flagging for adult magazines; the policy text was not re-read. Etsy policy pages blocked our crawler on 2026-10-27, so that, and the exact rule for calling something "vintage" (commonly cited as 20 or more years old), should be confirmed in a signed-in browser before the first listing.
- **NEEDS REVIEW: fee percentages in blogs versus our model.** Our dashboard fee model reproduces eBay's own worked examples (most categories 13.6% plus $0.40 per order; Books and Magazines 15.3%; Jewelry 15%). Resale blogs quote around 13% to 13.25% for eBay, 20% for Poshmark on sales of $15 or more, 10% for Mercari, and an August 2026 change taking Depop's US seller commission to 0 (about 3.3% plus $0.45 processing). Use our model for eBay; treat the blog numbers for other platforms as directional.

---

## 4. The storefront (built, sample version)

- Handmade in native HTML/CSS and hosted as a public site (the owner asked for public access on 2026-10-26); the page source lives in the repo (`site/`).
- **Design direction (2026-10-26):** the original room is a reference for taste and composition, not a claim that a physical store is operating. The site should feel like entering that world.
- Entrance: wall molding and framed art in the background, raised lettering in the middle, transparent lamp and chandelier cutouts in front. A hanging disco ball toggles a field of sparkles; both disco balls turn on a small WebGL mirror sphere; soft rectangular light reflections drift across the page every 14 seconds or so; there is an original music toggle.
- Categories ("Pick your obsession"): four equal portrait tiles. Search, sorting, saved finds, guide prices, authentication notes and mature-cover consent are in place.
- Accessibility and performance: reduced-motion users get stationary stars; the effect layers pause offscreen and in hidden tabs; WebGL capped at 30 fps and 640 px; photos fall back when WebGL is missing.
- Visual references researched (boutique and vintage commerce): Chairish, Georges Vintage, Pop Sick Vintage, YOWIE, Coming Soon, Sunbeam Vintage, The Vintage Shop LA, Lost & Loved, Rething.
- Open design ideas (not shipped): "Room edits" (cross-category looks such as brass and glass), "Why we picked it" (short item stories), "New finds" (only when real new stock arrives; no invented schedules or stock counters).
- Music and light research was done to pick royalty-clear sources; the findings sit in the project's research folder (free libraries, CC licences, and synthesis approaches) and are not summarised here.

---

## 5. The operations dashboard (designed, not built)

One installable web app (iPhone Home Screen), five tabs: **Today, Alerts, Watches, Inventory, Sales**, plus an Item detail page.

**What it does:**
- **Sold feed with real profit** across eBay, Etsy and Shopify: gross, fees, shipping, cost basis.
- **Inventory:** every piece, cost, storage location, live status per channel.
- **Buy alerts:** eBay listings matching a watch Ricky writes in plain words plus a price cap, pushed to the phone (Pushover, with ntfy as fallback).
- **Oversell guard:** if a piece sells on one channel and is still live on another 20 minutes later, raise a high-priority alert.
- **List from the phone:** photos plus one line of what the camera cannot see (measurements, flaws, maker marks) go to Claude Haiku, which drafts title, description, condition notes, era and maker guesses with confidence, materials, keywords and tags. It creates an **Etsy draft**; Ricky reviews and taps Publish. A crosslister (Crosslist Gold is the first candidate) imports the Etsy listing and posts it to eBay and Shopify. There is no auto-publish; Claude cannot measure a jacket or see a flaw on the back.

**Stack:** Supabase Pro (Postgres, Edge Functions, cron, Vault, Realtime), React 19 PWA with Tailwind and shadcn, Cloudflare Pages or Vercel, raw `fetch` for each vendor API.

**Cost:** about $26 to $46 a month plus a $4.99 one-time Pushover purchase. Claude listing drafts cost well under $1 a month (about $0.001 per five-photo listing).

**Rules worth knowing:**
- eBay licence limits shape the sourcing feature: watch hits are purged when the listing ends, are never more than 6 hours stale, are never used to suggest prices, to train, or to score. "Comps" are live links only.
- No "good deal" badge, no typical-price display, no buyer personal data anywhere.
- Etsy Seller App, eBay account-deletion endpoint, Shopify protected-data rules, signatures on raw webhook bytes, row-level security on every table, and token expiry watchdogs are built into the design.
- Of 19 other candidate sourcing sites, only Etsy has an official buyer-side search API; 12 explicitly ban automated collection; the compliant path for the rest is each site's own saved-search email.

**Status:** research done (ten reports, about 350 raw vendor pages), design and build handoff written. **Blocked on Ricky creating accounts and keys**: eBay developer keyset, Etsy Seller App (needs a live shop), Shopify Dev Dashboard app, Supabase Pro project, domain, Pushover, Resend, Healthchecks.io, a crosslister trial, and an Anthropic API key with a spend cap.

---

## 6. Market overview: what vintage and resale sellers typically buy and sell

*Sources: BLOG-grade reseller guides crawled 2026-10-27 (Flippd, Thriff Resale, Underpriced AI), plus our own comps. These are marketing blogs by reseller-tool companies, so treat percentages as directional and re-check any number before acting. Homepages: getflippd.com, thriffresale.com, underpricedai.com.*

### 6.1 The goods, by category

| Category | What sells | Why it works | Watch-outs | Fit for Hollywood and Vine |
|---|---|---|---|---|
| **Vintage clothing** | Band and tour tees (80s to 90s rock, 90s rap), vintage denim (Levi's 501, Lee, Wrangler), workwear (Carhartt, Dickies, Woolrich), vintage sportswear (Nike, Adidas, Champion, Starter, Polo Sport), outerwear (Patagonia, North Face), Hawaiian shirts, varsity jackets, designer vintage (Chanel, Gucci, YSL, Burberry) | Cheap to acquire (thrifts price by garment type, not brand), light to ship, strong demand, knowledge gap on the rack | Fakes and reprints; trend cycle is fast, hype pieces can lose 20% to 30% in three months; sizing and condition | **Good volume play.** Our rack leans colorblock 80s/90s, leather, hats, western: personality pieces more than label arbitrage. |
| **Lighting** | Mid-century and Hollywood Regency table lamps (Stiffel, Rembrandt), brass, glass chandeliers, sculptural lamps | High ticket per item; decor buyers pay for look | Shipping and breakage; need to confirm wiring and brand stamps; reproductions abound | **Core.** Several of our biggest pieces. |
| **Mid-century and statement furniture** | Eames, Knoll, Herman Miller, Danish teak; sculptural chairs; Gehry, Wiggle | Climbing demand; one find can pay for a month | Authentication; freight shipping; regional demand (California and Northeast strongest) | **Core**, if we can ship or sell local. The Wiggle-chair question is exactly this risk and upside. |
| **Art and decor objects** | Original paintings, prints, ceramics (Bitossi, Heath), Murano glass, brass, animal figurines (leopards), mannequins and busts | Aesthetic-driven; the buyer wants the room | Original versus mass decor canvas; condition (chips on fragile pieces); maker marks | **Core brand.** Our identity lives here. |
| **Barware and glassware** | Depression glass (pink), cut crystal decanters, cocktail shakers, coupes | Gift-able, set-driven; complete sets in good condition sell | Pressed glass versus lead crystal; later pink glass is worth about 40% less; chips | **Good**, ties to the pink-and-gold look. |
| **Leather and accessories** | Vintage Coach (1960s to 80s), Hermès small goods, Gucci, belts, jackets, harnesses | Quality leather ages well | Bonded versus full-grain; hardware quality; authentication | **Selective.** Harness belt and chain pieces fit the punk edge. |
| **Collectibles and memorabilia** | Signed photos, Disneyana, sports and trading cards, vinyl records | Collector demand; high margin on rare pieces | Authenticity and certificates drive price; need provenance | **High upside, high risk.** The Elvis item is exactly this. |
| **Print and media** | Vintage magazines (Playboy, Penthouse), art and fashion books, first editions | Cheap, small, nostalgic | Low unit price (we found $5 to $20 each); sold as lots and "year sets" at $35 to $50; Etsy and eBay mature-content rules | **Add-on only**, bundle or lot them. About 3% of our value. |
| **Electronics, gaming, audio (not our lane)** | Retro consoles and games, pro audio, older iPhones | Strong spreads on thrift buys | Not on-brand; testing needed | **Skip** unless it fits a "room" (a working turntable and 8mm projector do). |
| **Kitchen and cast iron (not our lane)** | Lodge, Griswold, Wagner; KitchenAid stand mixers | Reliable spreads | Not on-brand | **Skip.** |

### 6.2 What the blogs say is hot in 2026 (BLOG, directional)
- Vintage **sportswear** and **workwear** lead: faded, broken-in Carhartt and Dickies out-sell clean pieces; Depop named "Romanticized Sports" a 2026 trend.
- **Y2K** still sells but buyers are more selective; versatile pieces move faster.
- **Denim** has no single winning shape; Levi's 501 and selvedge remain the safe bet.
- **Mid-century modern** furniture "shows no signs of slowing".
- Nostalgia cycles: items 15 to 25 years old are in their sweet spot (as of Flippd's January 2026 article), which in 2026 means roughly 2001 to 2011.
- Experienced flippers focus on 3 to 5 categories (80/20 rule) and always check sold listings before buying anything over $20.

### 6.3 Where sellers buy to resell
Thrift stores and consignment, estate sales, garage sales and flea markets, auctions (ShopGoodwill, LiveAuctioneers, Invaluable, HiBid, EBTH), online marketplaces (eBay, Poshmark, Mercari, Depop, Facebook Marketplace, Craigslist, OfferUp, Whatnot), and design marketplaces for higher-end pieces (Chairish, 1stDibs). GoodwillFinds closed in April 2025.

**Sourcing constraint we found:** automated monitoring is barred by most sites' terms. The compliant, scalable route is each site's own saved-search email alerts (Craigslist, ShopGoodwill Personal Shopper, EstateSales.net Treasure Tracker, Invaluable, Chairish, HiBid, eBay) forwarded to the dashboard, plus eBay's official Browse API for eBay itself.

### 6.4 Where sellers sell
- **eBay:** widest reach, best for higher-value items; fees about 13.6% plus $0.40 per order (our verified model).
- **Etsy:** curated, vintage-friendly, strong for decor, art and fashion; listing fee plus sales fees; vintage conventionally means 20 or more years old (NEEDS REVIEW, see 3.4).
- **Poshmark:** best for clothing; 20% commission on sales of $15 or more (BLOG).
- **Mercari, Depop, Whatnot, Facebook Marketplace:** niche and local fits; Depop favors young vintage and streetwear shoppers (BLOG).
- **Chairish, 1stDibs:** high-end decor and furniture. They show what dealer *asking* prices look like (a Stiffel pair at $1,000, a leopard at $2,356), which is usually well above eBay sold.
- **Own site (Shopify):** brand control; no marketplace discovery.
- **Live selling:** called out by the Thriff Resale article as a growing channel (BLOG).

### 6.5 Pricing and profit rules of thumb
- **Price from sold listings, not asking.** Dealer asking prices on 1stDibs ran far above eBay sold (a seated leopard asked $2,356 against an eBay sold range of $45 to $345).
- Authentication certificates (JSA, PSA/DNA) lift signed items: in the comps we found, JSA-certified dual-signed asks were $290 to $573 against about $180 unauthenticated. The PSA/DNA fee is $20 to $125 for a two-signature item.
- Condition drives fragile goods: one chip on glass or ceramic can cut value sharply.
- Paint-over or a missing label cuts collector value (a repainted designer chair loses about 40%).
- Shipping is a real cost on lamps, projectors and chairs. Price delivered cost in, or offer local pickup.
- Clean, well-photographed items sell for more; condition and presentation beat quantity.

---

## 7. Where we are in the work (next steps)

1. **Ricky re-shoots** the "needs photo" items, square-on, no flash; the Elvis piece first (front, back, signatures close up). Shared in original quality, the video would also give 4K frames for items only seen in it.
2. **Resolve the price swings** (section 3.3) before listing: look under the Stiffel lamp, check the white chair for a Vitra or Easy Edges label, check the leopard for a maker stamp, decide whether to get the Elvis photo authenticated.
3. **Confirm Etsy rules** (vintage age definition, mature-content flag) in a signed-in browser.
4. **Ricky creates the accounts and keys** the dashboard needs (section 5), then a build session runs 14 ordered smoke tests against the live vendor APIs.
5. **Build phase 1:** sold feed, inventory, profit, listing from the phone. Then phase 1b: eBay watches and alerts. Then phase 2 (LLM matching, a compliant comps panel, saved-search email ingestion, web push).
6. **Storefront:** swap in real photos as they come, connect to the real catalogue, keep the public access setting.

**Decisions only Ricky can make:** iPhone or Android; dashboard domain; hosting (Cloudflare Pages, free, or Vercel Pro); which crosslister to trial; how many eBay watches and which categories; Shopify plan; whether the Etsy shop is live; who owns the eBay developer keyset; how much non-eBay sourcing to automate; a CPA conversation about inventory accounting before year end.

---

## 8. Suggested NotebookLM outputs

Use these as starting prompts.

- **Slide deck (investor/partner style, 10 to 12 slides):** the shop story, the room and brand, inventory and value by group, the five price-swing items, the storefront, the dashboard, the market map, the plan.
- **Slide deck (internal, "what to do this week"):** the re-shoot list in priority order, the five checks before listing, accounts Ricky must create.
- **Infographic 1, "Where the money is":** the 79/18/3 value split across decor, clothing and print, with the five swing items called out.
- **Infographic 2, "Vintage resale map":** categories (section 6.1) as a grid with fit-for-us ratings.
- **Infographic 3, "Anatomy of a listing":** photo, one line, Claude draft, Etsy draft, Publish tap, crosslist to eBay and Shopify.
- **Mind map:** center "Hollywood and Vine"; branches Brand, Inventory, Pricing, Storefront, Dashboard, Sourcing, Platforms, Open Risks, Next Steps.
- **Report (briefing doc):** a one-page "state of the business" and a two-page "category strategy: where to specialise" using the 80/20 rule (pick 3 to 5 categories).
- **Study guide / FAQ:** "How do I tell Stiffel from Stiffel-style?", "Is it real Depression glass?", "Original or decor canvas?", "What do I need to list a signed item?", "Which platform for which item?"
- **Audio overview:** ask for a debate-style conversation on "should we specialise in lighting and statement decor, or stay broad?" and "is the dashboard worth building before 50 listings exist?"
- **Timeline:** build phases and the account blockers.
- **Questions to answer with the notebook:** Which 5 items to list first for the fastest cash? Which items need research before pricing? What would a first-month revenue range look like at a 2 to 4 week sell-through? Which sourcing channels best fit lighting and decor? What is the highest-leverage thing to do this week?

---

## 9. Source homepages

- Etsy https://www.etsy.com/ · eBay https://www.ebay.com/ · Shopify https://www.shopify.com/ · Poshmark https://poshmark.com/ · Chairish https://www.chairish.com/ · 1stDibs https://www.1stdibs.com/
- Authentication: PSA/DNA https://www.psacard.com/ · JSA https://www.spenceloa.com/
- Reseller guides (BLOG): https://getflippd.com/ · https://thriffresale.com/ · https://underpricedai.com/
- Dashboard vendors: Supabase https://supabase.com/ · Pushover https://pushover.net/ · Healthchecks https://healthchecks.io/ · Resend https://resend.com/ · Anthropic https://www.anthropic.com/
- Design references: https://www.chairish.com/ · https://georgesvintage.com/ · https://popsickvintage.com/ · https://www.shopyowie.com/ · https://comingsoonnewyork.com/ · https://sunbeamvintage.com/ · https://thevintageshopla.com/ · https://lostandloved.co.uk/ · https://www.rething.uk/
