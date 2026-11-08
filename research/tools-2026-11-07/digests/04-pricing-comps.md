# 04-pricing-comps: Pricing comps tools for Holliewood and Vine

Question: which tools show what vintage pieces actually sold for (eBay, Etsy, auction houses, design marketplaces), help set a price, and what do they cost? V = vendor page read 2026-11-07; U = unreadable or non-vendor source.

## Bottom line

- The free backbone held up. eBay Product Research is "free to all sellers" with "the last 3 years of eBay sales data", in Seller Hub and the eBay mobile apps. Poshmark's Sold filter shows sold prices with no login. Chairish has a "Hide Sold Out" filter. EBTH's archive is searchable on a free, card-validated account. Google Lens is free. All V.
- The verify file corrected two lane figures. Invaluable's free account gives "up to 12 months of past auction prices" (Premium 5 years, Professional 15+ years), so sign up there before paying anyone. The Kovels price guide is sold as "Kovels All Access" at $59.99 per year; the lane's $24.95 was a separate Antique Trader digital magazine.
- WorthPoint's prices come from Apple's own App Store in-app list, not a third-party snapshot: "Price Guide Monthly $26.99", "Price Guide Annual $249.99". The vendor site walled every URL, so confirm on worthpoint.com before buying. The app is rated 2.1 from 117 ratings; use the website.
- Best gaps finds. Lot-Art's Price Database (75M+ auction results from 5,000+ houses since January 2016) sells a "Day Pass $9.90 one-time" and "Explorer $13.90/month", which covers most post-2016 auction comps without WorthPoint. Bidsquare's free past-results page carries Florida houses (Sarasota Estate Auction, Coral Gables Auction). Artsy's Price Database is free with "no search limits" for signed art where Artnet charges "$34 /30 days". Appraisily undercuts Mearto: free identification, "$9" for a working value, "Standard $59" for a signed report.
- Etsy exposes no sold prices. eRank, EverBee, Alura, Marmalead, Sale Samurai, EHunt and Koalanda sell estimates and keyword data. Skip them for pricing; they belong to the SEO lane. Nuance from verify: EverBee's $24.99 and $69 per month are annual-billing rates, and monthly billing is higher.
- Dashboard constraint. eBay bans scraping, and WatchCount's terms ban "any automated agent, AI assistant, bot, crawler, or scraper". The only eBay-sanctioned comps feed is the Marketplace Insights API, whose docs sit behind a developer sign-in (U). Human-only browser tools stay on the phone.
- Dead or renamed: Algopix (HTTP 502), Checkaflip (HTTP 525), Prices4Antiques (HTTP 502), ShelfTrend, Collectors.com, Antiques Navigator. Reeva and Nifty were not found. EtsyHunt is now EHunt. Mavin and 130point bot-walled the fetcher; check by hand.

## Table

| Tool | Does | Price (vendor wording, billing period) | Free tier | Platform | Verdict for Hollie | V or U | Source file and URL |
|---|---|---|---|---|---|---|---|
| eBay Product Research (ex-Terapeak) | Sold prices, average sale price, sold price range, sell-through; "last 3 years of eBay sales data" | "free to all sellers". Sourcing Insights only needs a Basic Store: "Basic $27.95" monthly renewal or "$21.95" per month on yearly renewal; eBay charges either monthly | Full tool free with a seller account | Web (Seller Hub Research tab), eBay mobile apps | Use now; the backbone | V | lane, verify; https://www.ebay.com/help/selling/selling-tools/terapeak-research?id=4853 |
| eBay sold filter and selling-flow price guidance | Buyer-side search filtered to sold listings; eBay suggests a price while listing | free | Free | Web, iOS, Android | Use now as a second view; guidance is weak on one-of-one | U (sold search page errored; FAQ confirms the filter) / V (guidance) | lane; https://www.ebay.com/sellercenter/ebay-for-business/great-price-badge |
| WorthPoint Price Guide (plus MARKS) | Archive of eBay and auction sold prices, "nearly 2 decades" | Apple in-app list: "Price Guide Monthly $26.99", "Price Guide Annual $249.99", "Price Guide + MARKS Monthly $37.99", "Price Guide + MARKS Annual $399.99". Vendor site HTTP 403 | App "Free · In-App Purchases"; prices locked | Web, iOS, iPad | Pay when it earns it (pre-3-year eBay records) | V (Apple listing) / U (vendor site) | verify; https://apps.apple.com/us/app/worthpoint/id1472512649 |
| Google Lens | Reverse image search for maker and pattern leads | free (no price, no sign-up) | Free | Web (Chrome, Firefox, Safari, Edge), Android, iPhone | Use now for identification | V | lane, verify; https://support.google.com/websearch/answer/1325808 |
| Poshmark and Mercari sold search | Search filtered to sold items with sold price | free | Free; Poshmark needs no login | Web, iOS, Android | Use now for lamps, shades, small decor, fashion | Poshmark V / Mercari U (HTTP 403) | lane, verify; https://poshmark.com/search?query=stiffel%20lamp&availability=sold_out |
| Chairish | Design marketplace asking prices, strike-through originals, "Hide Sold Out" filter | free to browse | Free | Web (iOS app per footer, not read) | Use now for ceilings and listing language; asking, not sold | V | verify (URL corrected to maker page); https://www.chairish.com/maker/stiffel |
| 1stDibs | Trade-tier asking prices on maker pages; no sold filter | free to browse | Free | Web | Use now as ceiling only | V | lane, verify; https://www.1stdibs.com/creators/stiffel/furniture/ |
| EBTH | Estate-sale auctions; "search for both Active and Archived Items" | free account; credit card required at sign-up | Free account | Web, iOS, Android (Google Play linked in footer) | Use now; realized prices on Hollie's exact mix | V | lane, verify; https://www.ebth.com/faq |
| LiveAuctioneers Price Results | Realized prices from many houses | reported free with account; lane URL is a 404 | Free account (U) | Web, iOS, Android | Use now if the free account shows prices; check by hand | U | lane, verify; https://www.liveauctioneers.com/pages/price-results/ (dead) |
| Invaluable Price Archive | Realized auction prices | Free account: "up to 12 months of past auction prices"; Premium "last five years"; Professional "last 15+ years"; paid prices unread | Free account, 12 months | Web, iOS, Android | Use now (free account) | V (tiers) / U (paid prices) | verify; https://www.invaluable.com/inv/help/faq/search-price-archive/ |
| Barnebys and Heritage archives | Aggregated auction results; HA lots | unknown; HTTP 403 on both | unknown | Web | Skip for now; Heritage is coins, cards, fine art | U | lane, verify; https://www.barnebys.com/realized-prices ; https://www.ha.com/c/ref/auction-archives.zx |
| Lot-Art Price Database | 5,000+ auction houses; 75M+ sold results since January 2016; image search; Design, Classic Furniture, Glassware, Tableware | "Starter $4.50/month" (no Price Database); "Explorer $13.90/month ... plus Price Database access"; "Collector $37.90/month"; "Day Pass $9.90 one-time"; "Prices shown are in USD billed monthly"; yearly plans 30% off | Free account: lot listings and basic search; Price Database needs Explorer, Collector or Day Pass | Web | Pay when it earns it | V (user guide; plan grid did not render) | gaps; https://www.lot-art.com/user-guide |
| Artsy Price Database | Fine-art auction results, "Auction records from 300,000 artists" | "for free"; "no search limits, no subscriptions" | Free | Web, iOS, Android | Use now for signed art and prints | V | gaps; https://www.artsy.net/price-database |
| Bidsquare Past Auction Results | Past catalogs from US houses incl. Sarasota Estate Auction, Coral Gables Auction; "Lamps, Lighting & Candlesticks", "Mid Century Modern" | free to browse | Free | Web | Use now; hammer-price visibility logged out unconfirmed | V (page) / U (price visibility) | gaps; https://www.bidsquare.com/auctions/past |
| HiBid and AuctionZip | Estate-auction platform with closed auctions and radius search; auction directory with a Florida page and "Featured Prices Realized" | free to browse | Free | Web | Use now for local comps and sourcing | V (pages) / U (lot-level sold prices) | gaps; https://hibid.com/ ; https://www.auctionzip.com/ |
| Wright (Rago Wright) | Design house network; Modern Design, Art Deco & Art Nouveau Lighting, American + European Glass; "Complimentary Evaluations of Property" | free to browse; past-auction URLs 404 | Free | Web | Use now once the PAST tab loads in a browser | V (home) / U (results) | gaps; https://www.wright20.com/ |
| Christie's and Sotheby's results | Past sale results, filters by category | free | Free | Web; Sotheby's app | Skip under about $1,000; ceiling only | V | gaps; https://www.christies.com/en/results ; https://www.sothebys.com/en/results |
| WatchCount | eBay sold-item search plus most-watched listings, rich filters | "unknown" (Pricing link 404); search works without login | Free web search | Web | Use now by hand on the phone; never in the dashboard (terms ban AI access) | V | gaps; https://www.watchcount.com/ |
| Mavin and 130point | Free eBay sold-price front ends (reputation only) | unknown | unknown | Web | Check by hand; if they load, phone home screen | U (bot wall; HTTP 403) | gaps; https://mavin.io/ ; https://130point.com/ |
| HiFi Shark and Audiogon Bluebook | Used hi-fi listings "from 400+ Sources" with a Sold/Expired tab; US transaction history by condition behind login | HiFi Shark free (/premium 404); Audiogon "unknown" (pricing page HTTP 403) | HiFi Shark free; Audiogon unknown | Web; HiFi Shark companion app | Use now for the turntable; Audiogon check by hand | HiFi Shark V / Audiogon price U | gaps; https://www.hifishark.com/search?q=technics+sl-1200 ; https://www.audiogon.com/bluebook |
| Kovels Price Guide | Guide values incl. "Lamps & Lighting", "Glass & Bottles" | "Kovels All Access ... $59.99 per year"; "Kovels All Access + Print 79.99 per year" ($24.95 is the separate Antique Trader digital magazine) | Newsletter only | Web | Skip unless eBay and Invaluable run dry on a category | V | verify; https://www.kovels.com/subscriptions/ |
| Google Shopping and Replacements.com | New-retail asking prices; china, crystal and glass pattern catalog with Replacements' asking prices | free | Free | Web | Use now for the new-equivalent ceiling; Replacements check by hand | Google Shopping V / Replacements U (HTTP 403) | gaps, lane; https://www.google.com/shopping?udm=28 ; https://www.replacements.com/ |
| Artnet Price Database | Fine and decorative art auction results; "only include items estimated at $500 and above" | Decorative Art "$34 /30 days*", "$350 /year*"; Fine Art One-Day Pass "$32.50 /day" (5 searches), Individual Rollover "$42.50 /30 days*" (10 searches), Expert "$450 /year*", Appraiser "$1,175 /year*" | None | Web | Pay when it earns it | V | lane, verify; https://www.artnet.com/price-database/ |
| PSA Auction Prices Realized and Price Guide | "over 5 million auction results"; autograph categories; PSA-certified items only | free | Free | Web | Use now only for PSA-certified signed pieces | V | lane; https://www.psacard.com/auctionprices |
| Appraisily | Signed appraisal PDF; free Instant Screener identification | "Standard $59 · Insurance $99 · Donation from $399"; "Unlock a working value ... for $9" | Free identification | Web | Pay when it earns it | V | gaps; https://appraisily.com/ |
| Mearto and ValueMyStuff | Paid online appraisals by specialists | Mearto "1 Appraisal $25", "3 Appraisals $70", "5 Appraisals $90", "10 Appraisals $170"; ValueMyStuff "1 credit $28", "3 credits $70", "5 credits $99", "24H EXPRESS 2 credits" | None | Web; VMS app | Pay when it earns it, as a second opinion | V | lane; https://www.mearto.com/pricing ; https://www.valuemystuff.com/us/pricing |
| eRank, EverBee, Alura (Etsy estimators with free tiers) | Etsy keyword, shop and sales estimates; no sold prices | eRank "Free $0/mo", "Basic $5.99/mo", "Pro $9.99/mo", "Expert $29.99/mo". EverBee "HOBBY $0", "GROWTH $24.99 / month" ($299 per year, annual rate), "BUSINESS $69 / month Billed annually at $828". Alura "Free $0 / month", Basic "$95.88 billed yearly", Growth "$179.99 billed yearly", Professional "$359.88 billed yearly" | eRank 5 keyword lookups/day, 1 shop, 50 listings; EverBee 10 keywords; Alura 5 daily searches, API & MCP access | Web, Chrome extension | Skip for pricing; SEO lane | V | lane, verify; https://erank.com/plans ; https://www.everbee.io/pricing ; https://www.alura.io/pricing |
| Marmalead and Sale Samurai (paid-only Etsy estimators) | Etsy keyword tools; "priced to win" check | Marmalead "$19 USD paid monthly", "$190 USD paid annually", "$300 USD paid ONCE"; Sale Samurai "$19.99 Monthly", "$16.65/mo Billed as $199.90 yearly" | None (Sale Samurai "3-day free trial") | Web, Chrome extension | Skip | V | lane, verify; https://marmalead.com/pricing ; https://salesamurai.io/pricing/ |
| eBay Marketplace Insights API | eBay's own sold-item data API | unknown; docs redirect to developer sign-in | unknown | API | Dashboard only; the sanctioned comps feed | U | gaps; https://developer.ebay.com/api-docs/buy/marketplace-insights/overview.html |
| Chrome sold-comp extensions (Comp Splitter, eBay Sold and Completed US & UK, ex FlipScout) | Sold-comp shortcuts and averages in the browser | Comp Splitter and eBay Sold and Completed free; ex FlipScout "Free tier gives 3 lookups/day forever", "Pro $14.99/mo", "Lifetime ($89)" | Free | Chrome extension | Skip; 15 to 458 users, grey zone with eBay terms, duplicates Seller Hub | V | lane; https://flipscout-app.pages.dev/how-to-check-ebay-sold-prices |

Dropped: Algopix (HTTP 502, Amazon and dropship), ZIK Analytics (dropship-first, "$1 trial"), Checkaflip (HTTP 525, dead), Prices4Antiques (HTTP 502, dead), ShelfTrend (now a newsletter), Collectors.com (corporate page), Antiques Navigator (changed beyond use), Reeva and Nifty (reseller apps not found at any domain), Hammer Price (collector-car app), EHunt ex EtsyHunt and Koalanda (Etsy estimators, no sold prices; EHunt nav is dropshipping-oriented), JustAnswer ("$65 /month per category", recurring), Flipwise (eBay bookkeeping, "not a cross-listing tool", not comps), Vendoo (crosslister; Crosslist Gold chosen), JSA (no price guide), Collectors Weekly (reading plus eBay affiliate asking prices), Artprice and AskART (Artsy covers free art results; AskART Cloudflare-walled), AuctionNinja (Northeast-heavy), Goldin (memorabilia ceiling only), MaxSold (HTTP 403, reputation only).

## Picks

Use now (free):
- eBay Product Research (Seller Hub on the PC, Research tab in the eBay app).
- Poshmark Sold filter; Mercari sold search once confirmed in the app.
- Chairish maker pages with Hide Sold Out off, and 1stDibs, for ceilings and listing language.
- EBTH free account (card required) for archived estate-sale prices.
- Invaluable free account for 12 months of realized auction prices.
- Google Lens for identification; Google Shopping for the new-equivalent ceiling.
- Bidsquare /auctions/past and HiBid for Florida estate houses.
- Artsy Price Database for any signed painting or print.
- WatchCount by hand on the phone. HiFi Shark for the turntable.

Pay when it earns it:
- Lot-Art "Day Pass $9.90 one-time" the first time a lamp, chandelier or signed piece looks worth more than about $300. "Explorer $13.90/month" only if auction comps are checked weekly.
- WorthPoint "Price Guide Monthly $26.99" when a piece is older than eBay's 3-year window or eBay shows fewer than five sold comps. Buy monthly, cancel when the backlog is priced. Confirm the web price first.
- Artnet Decorative Art "$34 /30 days" only in a month when a signed or attributed piece already looks like $500 plus.
- Appraisily "$9" screener value or "Standard $59", or Mearto "1 Appraisal $25", when comps disagree by hundreds of dollars.

Skip:
- Kovels All Access $59.99 per year: guide values, not live comps, unless eBay and Invaluable both run dry.
- eRank, EverBee, Alura, Marmalead, Sale Samurai, EHunt, Koalanda for pricing: estimates, no sold prices.
- Chrome sold-comp extensions: tiny user counts, eBay terms grey zone, Seller Hub does the same job.
- ZIK, Algopix: dropship and Amazon tooling. JustAnswer: recurring $65 a month. Flipwise and Vendoo: other lanes. Heritage, Christie's, Sotheby's: wrong price band.

## Contradictions with earlier decisions

None found. Two adjacent notes:
- Crosslist Gold (trial): Vendoo appears at "STARTER $12.49 Per month, billed yearly" with a 14-day trial and, on Growth, "AI Listing Enhancement" and "300 background removals powered by PhotoRoom". No file compares it with Crosslist; the lane kept Crosslist. A sighting, not a conflict.
- Claude Haiku drafts: unaffected. But an automated comps feed for the dashboard cannot scrape eBay or WatchCount (terms ban AI access); the only sanctioned feed is the Marketplace Insights API, docs gated (U). That adds a developer sign-up step to the handoff, nothing more.

## Check by hand

- https://www.worthpoint.com/pricing : does the web price match Apple's $26.99 monthly and $249.99 annual, and is there a monthly plan that cancels cleanly.
- https://www.liveauctioneers.com : find Price Results (the /pages/price-results/ URL is dead); does a free bidder account show realized prices.
- https://www.invaluable.com/subscriptions/ : Premium and Professional prices.
- Mercari app on the iPhone: search "stiffel lamp", filter Sold; do sold prices show.
- https://mavin.io/ and https://130point.com/ : do they load and show eBay sold averages free.
- https://www.bidsquare.com/auctions/past : open a closed lot logged out; does the hammer price show.
- https://hibid.com/auctions?status=closed : open a closed lot; does the sold price show.
- https://www.lot-art.com/auction-sale-price-database : confirm Day Pass $9.90 one-time and Explorer $13.90/month on the live plan grid.
- https://www.audiogon.com/bluebook : after a free login, does transaction history show without paying.
- https://www.wright20.com/auctions : PAST tab; do results show prices.
- https://www.barnebys.com/realized-prices and https://www.replacements.com/ : do they load, and is browsing free.

## Sources

- research/tools-2026-11-07/04-pricing-comps.md
- research/tools-2026-11-07/verify-04-pricing-comps.md
- research/tools-2026-11-07/gaps-04-pricing-comps.md
