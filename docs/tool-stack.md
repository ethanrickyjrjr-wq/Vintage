# Holliewood and Vine: tool stack

**Date:** 2026-11-07. **Status:** research synthesis; nothing built or bought.

Sixteen Sonnet lanes ran on 2026-11-07, one per step of the process. Each lane left three files in `research/tools-2026-11-07/`: a lane report (`NN-name.md`), a verify file (`verify-NN-name.md`) that re-read the lane's picks on the vendor pages the same day and overrides the lane where they disagree, and a gaps file (`gaps-NN-name.md`) for tools the lane missed and tools that are defunct or renamed. Sixteen digests in `research/tools-2026-11-07/digests/` fold the three together. This page is the decision layer. Every price is quoted as the vendor writes it, with its billing period, and carries its source file and URL. **V** means an agent read the vendor page on 2026-11-07. **U** means the page would not load or the figure is not in any page text. Where the verify file refuted a lane figure, the verify figure is used and the correction is named. crawl4ai was not reachable from the cloud session, so pages were read with WebFetch. Several gaps agents ran after the shared WebSearch budget ran out and worked from direct vendor URLs, so their coverage of new entrants is thinner. Source shorthand in the tables: `lane 01` is `01-listing-crosslisting.md`; `verify-01` and `gaps-01` are its verify and gaps files; full names are under Sources.

Prior decisions this page inherits: Crosslist Gold to trial for crosslisting (`docs/dashboard-design.md` section 10), rembg pinned to `-m birefnet-general` with flattened JPEGs for every channel (`docs/cutout-catalog-handoff.md` sections 1 and 5), Buffer Free, Canva Free and Instagram Edits (`docs/social-manual.md` section 7), Claude Haiku listing drafts in the planned dashboard, Supabase and Pushover (`docs/dashboard-design.md` section 9), Kit Free for email before Shopify and fixed Etsy shipping classes (`docs/round-d-synthesis.md`). They stand unless the Contradictions section says otherwise.

## Read this first

- The stack in one breath. List from the Etsy Seller app and the eBay app. Haiku drafts the Etsy listing in the planned dashboard. rembg BiRefNet cuts out and ImageMagick flattens. Pirate Ship and Etsy labels ship. Airtable Free and Zoho Books Free keep the books. EstateSales.net, Trove and CTBids find stock. Buffer Free, Canva Free and Instagram Edits post. Cal.com Free and Tally book Hire Hollie. A crosslister fans Etsy out to eBay and Shopify.
- The free stack costs $0 a month. The only money is platform fees: Etsy "$0.20 per listing", "6.5% of the total order amount" and "3% + 0.25 USD"; eBay "13.6%" plus "$0.30" or "$0.40" per order, with the first 250 listings a month free (V, verify-14).
- The paid stack on the standing decisions is Shopify Basic "$29 USD/mo" paid yearly plus Crosslist Gold "$39.99 per month": $68.99 before anything else, so it does not fit a $50 line. The everything stack is about $350 a month plus about $382 once.
- Time saver 1: eBay Product Research, "free to all sellers", "the last 3 years of eBay sales data" (V, verify-04). It removes every paid comps subscription for the first year.
- Time saver 2: Etsy's own messaging. Auto-replies, quick replies and the writing assistant are free, and auto-replies count toward Star Seller (V, verify-11).
- Time saver 3: native alerts. EstateSales.net email, Trove's eBay push "usually within 60 seconds", CTBids bidding with local pickup. The sourcing feed is free and nothing is scraped (V, verify-06, gaps-06, verify-07).
- Contradiction: Crosslist Gold is not a free trial. "20 free listings with our 3-day money-back guarantee", a card is required, and annual refunds carry "a small $9.99 processing fee" (V, verify-01, verify-13). Five cheaper tools cover all three channels with sale detection on the entry plan. Ricky decides; the evidence is in Contradictions.
- Soft contradiction: Flippd and Inventory Now keep the cost ledger in their own cloud, while the plan makes Supabase the home. Decide one home before paying either.
- rembg's README now makes bria-rmbg "The default", and that licence "requires a paid agreement for commercial use" (V, verify-03). Every call must pass `-m birefnet-general`. Etsy renders transparent PNG areas black, so every cutout is flattened. Both were already decided; both are now confirmed on the vendor pages.
- remove.bg closes "from 1 December 2026 at 9:00am CET" (V, verify-03). Windows 11 Photos and Paint remove backgrounds locally for free.
- Claude in Chrome and Claude Cowork are "Available on all paid plans" (V, verify-15). eBay bans "LLM-driven bots" without permission (V, verify-15). Browser agent on Etsy only, Ricky watching; eBay through the API.
- Etsy Share & Save refunds "6.5% back" from October 20 to January 4, then "4% off the eligible order total" (V, verify-08). Turn it on day one. Decide Offsite Ads before the first sale.

## Install today

Free only. Ordered by payoff. One line each.

**Windows PC**

1. Bitwarden Free, "Unlimited devices, unlimited passwords"; every marketplace and API key from day one. $0. lane 13.
2. PowerToys: Image Resizer with 2000px and 1600px presets added by hand, Text Extractor, Advanced Paste. $0. lane 13, verify-03.
3. Windows 11 Photos and Paint: background removal "locally on your device". Built in. $0. verify-03, gaps-03.
4. rembg in its own venv, every call `-m birefnet-general`, plus ImageMagick to flatten onto white. $0, MIT. verify-03.
5. Upscayl, to reach Etsy's 2000 pixels. $0. verify-03.
6. Caesium Image Compressor, whole shoots under Etsy's 1 MB warning. $0. gaps-03.
7. Affinity by Canva, "free for individuals (seriously)". $0. verify-03.
8. eRank Chrome extension with a free account, "5 keyword lookups/day". $0. lane 13.
9. Google Lens in Chrome plus the Search by Image extension. $0. gaps-13.
10. LanguageTool or Harper, one of them. $0. lane 13, gaps-13.
11. Espanso text expander, once ten listings of boilerplate exist. $0. lane 11.
12. iCloud for Windows with iCloud Photos on, plus the free HEIF Image Extension. $0 to 5 GB. lane 13, gaps-13.
13. LocalSend for same-day photo batches. $0. lane 13.
14. Pirate Ship account, "No monthly fees". $0. verify-10.
15. DaVinci Resolve, LosslessCut, HandBrake, Subtitle Edit, OBS Studio. $0. lane 12, gaps-12.
16. changedetection.io self-hosted on the Fedora box for estate-sale calendars, notifying Pushover through Apprise. $0. lane 06.

**iPhone**

1. Etsy Seller app. "Free". lane 14.
2. eBay app, "Create a listing in a snap with the help of AI". Free. lane 01.
3. Trove - Smart Alerts for eBay, "Free to use", "Up to 15 saved searches". gaps-06.
4. EstateSales.net app and Estate Sale Finder from EstateSales.org. Free. lane 06, gaps-06.
5. Snapseed, "no subscriptions, purchases, ads, or watermarks". verify-03.
6. Microsoft Designer, "free with a Microsoft account". gaps-03.
7. Google app for Lens. Free. lane 05.
8. TripLog, Basic "Free forever" automatic mileage. verify-09.
9. ShipSaving, Starter "Free/ month", the FedEx backup with a phone app. gaps-10.
10. Text Replacement in Settings for canned replies. Built in. gaps-11.
11. LocalSend and Bitwarden. Free. lane 13.
12. Already decided and still free: Instagram Edits, Buffer, Canva. `docs/social-manual.md` section 7.

## 1. Source

### Online alerts

| Tool | Does | Price | Free tier | Platform | Verdict | Source |
|---|---|---|---|---|---|---|
| Trove - Smart Alerts for eBay | Push on new eBay listings, "usually within 60 seconds" | "Free to use", "No fees. No subscriptions. No limitations." | Whole app; "Up to 15 saved searches" | iOS; Android U | Use now, first eBay alert app | V · gaps-06 · https://apps.apple.com/us/app/trove-smart-alerts-for-ebay/id1536471650 |
| eBay saved searches | Native email alert; no interval stated | Free | Whole feature | Web, app | Use now as the slow backstop | V · verify-06 · https://www.ebay.com/help/buying/search-tips/saved-searches?id=4051 |
| EstateSales.net | Daily email by lead day, sale type, radius; Treasure Tracker keywords | "Free E-mail notifications" | Whole feature | Web, iOS, Android | Use now; ZIP 33901 and 34102, 50 miles | V · verify-06 · https://www.estatesales.net/help/frequently-asked-questions |
| EstateSales.org and gsalr | Second aggregator, 5 to 100 miles, weekday picker, "Online Auction Items"; gsalr yard-sale digest | Free; gsalr "Go Ad Free for $4.99" | Whole feature | Web; Estate Sale Finder iOS app | Use now; sign up in the homepage modal, /subscribe is a 404 | V · verify-06 · https://estatesales.org/ |
| Proxibid, LiveAuctioneers, Invaluable, HiBid | Auction aggregator alerts; Proxibid "default frequency of once a week" | Free | Yes | Web, apps | Use now; set Proxibid to daily; HiBid and Invaluable alert settings U | V · verify-06 · https://discover.proxibid.com/comparison-shopping-hard-help |
| Craigslist search alerts | "automated email when new postings match" | Free | Yes | Web, app | Use now on the fort myers and sarasota sites | V · verify-06 · https://www.craigslist.org/about/help/account/features/searches |
| changedetection.io | Self-hosted page monitor; Pushover through Apprise | Hosted "$8.99 / Month"; self-hosted free, Apache-2.0 | Self-hosted | Fedora box | Use now on estate-sale calendars and auction-house pages only | V · verify-06 · https://github.com/dgtlmoon/changedetection.io |
| Sift; Dibs | Chrome extensions re-running Facebook Marketplace searches in Hollie's own browser | Sift Pro "$6.99 a month or $49 a year"; Dibs Pro "$12/month" | Sift "free to use"; Dibs "3 saved searches, checked every 15 minutes" | Chrome | Only if Ricky accepts the Meta-terms risk; a ban lands on the selling account | V · gaps-06 · https://siftmarketplace.com/pricing |
| Botifex, Swoopa, DealHunter, Marketplace Monitor, Pacto | Proxy scrapers of Facebook, OfferUp, eBay | Botifex "Basic $19.99/mo"; Swoopa "$47/mo"; DealHunter "$7.99 / month" | Thin | Web | Skip; scraping against Meta and eBay terms | V · gaps-06 · https://botifex.com/pricing |

Decision. Use now: EstateSales.net and EstateSales.org accounts, Trove, eBay saved searches, Proxibid and LiveAuctioneers follows, Craigslist alerts on two city sites, changedetection.io on the Fedora box. Pay when it earns it: Dealerts or BayWatch in-app purchases when Trove's 15 searches run out, prices read in-app first (gaps-06); Wachete "STARTER $ 5.40 / month billed monthly" if self-hosting is off and daily checks miss sales (gaps-06). Skip every proxy scraper. The dashboard's sourcing feed holds alert emails and what Hollie types, not scraped listings; EstateSales.net's terms forbid harvesting (verify-07). IFTTT's Craigslist service is a 404, so that glue idea is dead (verify-06).

### Southwest Florida venues

| Venue | Does | Price or fee | Free tool | Hours or cadence | Verdict | Source |
|---|---|---|---|---|---|---|
| CTBids (Caring Transitions of Cape Coral) | Online estate auctions, local pickup | "Bidding Starts at $1"; Premier "$99/year" | Free account; "Real time updates and notifications" | Four live Cape Coral auctions on 2026-11-07 | Use now, free; Premier pay when it earns it | V · verify-07 · https://ctbids.com/estate-sales/Cape-Coral-FL |
| HiBid with Gulf Coast Auction House, Bonita Springs | Local house; estates, decor, vintage | "18% Buyer's Premium \| 3% Discount for Cash Payments" | Watch list, email list | Preview Fri 10 to 6, Sat 12 to 3 | Use now; budget premium plus tax | V · verify-07 · https://gulfcoastauctionhouse.hibid.com/ |
| KCM Galleries, Cape Coral | Online framed-art auctions "Every Sunday and Wednesday" | Premium set per auction; the lane's "no buyer's premium" was a listing title, refuted by verify | Free to register | Twice weekly | Use now for framed art; read each auction's terms | V · verify-07 · https://www.kcmgalleries.com/buy-art/how-to-bid/ |
| Goodwill SWFL and ShopGoodwill | Thrift chain plus online auctions with Tice St pickup | VIP Perks free; "Members earn 5% back" | Free; "Saved Searches" online | Sundays "50% discount on most color-tagged items"; leftovers "$1.99 the following Sunday & Monday" | Use now | V · verify-07 · https://goodwillswfl.org/shop/ |
| Habitat ReStores (North Fort Myers, Bonita Springs, East Naples); Hope Chest (four stores) | Furniture, lighting, decor; upscale resale | n/a | Rewards app; Collier inventory email; Hope Chest newsletter | ReStore "Monday-Saturday \| 10am - 5pm"; East Naples "Mon-Sat: 9 a.m. - 6:30 p.m."; Hope Chest Mon to Fri 9 to 5, Sat 9 to 4 | Use now; McGregor ReStore is "PERMANENTLY CLOSED" | V · verify-07 · https://www.habitat4humanity.org/locations/ |
| Fleamasters, Flamingo Island, Ortiz flea markets | Mixed new and used; collectables | Entry fee not stated; Ortiz "Free parking." | None | Fleamasters "Friday - Sunday: 9am-5pm"; Flamingo Island "Fri, Sat & Sun 8am-4pm"; Ortiz "Saturday 8AM-4PM Sunday 6AM-4PM" | Use now; Ortiz Sunday 6 AM is the picker hour (verify corrected the lane's Fri to Sun) | V · verify-07 · https://www.ortizfleamarket.com/ |
| Allegro (Fort Myers), Can't Take It With You, Dovetails (Naples), Sharon Hardison (Punta Gorda), Freedom Auction Company (Sarasota) | Estate-sale companies; Freedom runs a "MID-CENTURY MODERN DESIGN DECEMBER 11TH, 2026" sale | Premiums not shown or per platform | Free text or email lists | By sale | Use now; join every list | V · gaps-07, lane 07 · https://linktr.ee/allegroestatesalesfl |
| StorageTreasures; Lockerfox | Storage unit auctions | StorageTreasures "$0.00 / Month", "ProBidder $10.00 / Month"; Lockerfox "15% of the winning bid subject to a $10.00 minimum" | StorageTreasures free | Naples "Total Auctions: 21" on 2026-11-07 | One-off gamble on StorageTreasures; skip Lockerfox | V · verify-07 · https://www.storagetreasures.com/pro-membership-upgrade |
| MaxSold | Online downsizing auctions | "the buyer's premium is 18%" | U | SWFL activity U; site 403 | Skip until a Lee or Collier sale appears | V premium, U activity · gaps-07 · https://support.maxsold.com/hc/en-us/search?query=buyer%27s+premium |

Decision. The desk route to whole-house contents is CTBids and HiBid with local pickup. Floor stock is Goodwill color tags on Sunday, the three ReStores and Hope Chest. Early November was thin in Collier and the action was Cape Coral online auctions; re-check in January (verify-07). Pay when it earns it: CTBids Premier "$99/year" when she wins several lots a month and pickup slots sell out; its WorthPoint benefit is a "90 Day All-Access Subscription", not a year (verify-06). Skip Lockerfox and storage units as a routine. EBTH ships from Ohio and AuctionNinja has no SWFL sellers (lane 07).

## 2. Identify

| Tool | Does | Price | Free tier | Platform | Verdict | Source |
|---|---|---|---|---|---|---|
| Google Lens; Bing Visual Search | Reverse image search for maker and pattern leads | Free | Whole product | iPhone, Chrome; Bing on PC | Use now; Lens is the first guess, marks are the proof | V · verify-05 · https://search.google/ways-to-search/lens/ |
| Claude, Gemini, Copilot free tiers | Photo to maker, era and style hypotheses | Claude Free "$0"; Gemini "$0/ month"; Copilot free app | Yes | Web, phone, Windows | Use now for vocabulary only; never cite as attribution | V · verify-05 · https://claude.com/pricing |
| Kovels marks guides; Kovels All Access | Free marks articles; paid price guide and marks dictionary | "Kovels All Access Online $59.99 per year" (verify corrected the lane's "not found"; lane 04's $24.95 was the Antique Trader magazine) | Guide pages, Kovels Komments newsletter | Web | Free pages now; All Access pay when it earns it | V · verify-05 · https://www.kovels.com/subscriptions/ |
| Marks bookmark folder: thepotteries.org, porcelainmarksandmore.com, silvercollection.it, 20thcenturyglass.com, The Marks Project | Pottery, porcelain, silver, glass and studio ceramic marks | Free | Whole sites | Web | Use now | V · verify-05, gaps-05 · https://www.themarksproject.org/ |
| VFG Label Resource; FTC RN database | Vintage clothing labels; company behind an RN number | Free | Whole sites | Web | Use now for every garment | V · verify-05 · https://rn.ftc.gov/ |
| Antiquers.com; Collectors Weekly Show & Tell | Human identification forums | Free | Yes | Web | Use now for the pieces nothing else names | V · gaps-05 · https://www.antiquers.com/ |
| Appraisily; Mearto; ValueMyStuff | Free photo ID and paid working value; specialist appraisals | "Identification is free. Unlock a working value ... for $9."; Mearto "1 Appraisal $25"; ValueMyStuff "1 credit $ 28" | Appraisily identification | Web | Appraisily free ID now; $9, $25 or $28 for one piece whose price depends on the maker | V · gaps-05 · https://appraisily.com/ |
| FindArtInfo; Art Signature Dictionary | Artist signature databases | FindArtInfo "$4.95 for 24 hours or $17.95 a month"; ASD "7 days free, then $12/month" | FindArtInfo free account | Web | Free account now; $4.95 day pass for all signed pieces in one sitting | V · gaps-05 · https://findartinfo.com/pricing |
| WorthPoint MARKS Premium | "more than 150,000 makers' marks" | Apple listing: "MARKS Premium Monthly $19.99", "Annual $99.99"; web pricing page 403 | Trial only | Web, iOS (2.1 rating) | Pay when it earns it, after the web price is confirmed | V Apple, U web · verify-05 · https://apps.apple.com/us/app/worthpoint/id1472512649 |
| PSA/DNA | Autograph authentication | "2 Signatures" tier "$20" to "$500"; Premium Letter "an additional $15" under $50; Original Photograph "$999 or less $50" | None | Mail-in | Pay when it earns it: the Elvis photo carries two signatures, so the 2 Signatures column applies | V · verify-05 · https://www.psacard.com/pricing/autographs |
| AI identifier apps (Antiquer, Antiqly, ThriftCheck and others) | AI photo ID | Weekly billing "$4.99" to "$9.99 per week"; Antiqly "$39.99 per year", no trial | Antiquer "2 identifications per day" | iOS, Chrome | Skip; Lens is free and reviews say faster | V · verify-05, gaps-05 · https://apps.apple.com/us/app/antique-identifier-antiquer/id6764046845 |

Decision. Lens plus a marks bookmark folder is the whole identification stack for $0. A Haiku draft must not assert a maker or era that no mark, label or appraiser confirmed; Anthropic's own page says Claude "can occasionally produce responses that are incorrect or misleading" (verify-05). Pay only per piece: Appraisily $9, Mearto $25, FindArtInfo $4.95, PSA/DNA for the Elvis photo with a JSA Florida phone quote as the price check (lane 05). TinEye is "free for non-commercial use" only and a shop is commercial, so skip it (lane 13).

## 3. Price

| Tool | Does | Price | Free tier | Platform | Verdict | Source |
|---|---|---|---|---|---|---|
| eBay Product Research (Terapeak) | Sold prices, sell-through, "the last 3 years of eBay sales data" | "free to all sellers" | Full tool | Seller Hub, eBay app | Use now; the backbone | V · verify-04 · https://www.ebay.com/help/selling/selling-tools/terapeak-research?id=4853 |
| Poshmark Sold filter; Mercari sold search | Sold prices for lamps, small decor, fashion | Free; Poshmark needs no login | Yes | Web, apps | Use now; Mercari was 403, confirm in the app | Poshmark V, Mercari U · verify-04 · https://poshmark.com/search?query=stiffel%20lamp&availability=sold_out |
| Chairish; 1stDibs | Asking prices, "Hide Sold Out" filter, listing language | Free to browse | Yes | Web | Use now for ceilings; asking, not sold | V · verify-04 · https://www.chairish.com/maker/stiffel |
| EBTH archive | Realized estate-sale prices, "Active and Archived Items" | Free account, card required | Yes | Web, apps | Use now | V · verify-04 · https://www.ebth.com/faq |
| Invaluable Price Archive | Realized auction prices | Free account "up to 12 months of past auction prices"; Premium "last five years" (verify refuted the lane's "limits unknown") | 12 months | Web, apps | Use now; sign up before paying anyone | V tiers, U paid prices · verify-04 · https://www.invaluable.com/inv/help/faq/search-price-archive/ |
| Artsy Price Database; Bidsquare; HiBid closed auctions | Fine-art results "for free", "no search limits"; Florida houses' past catalogs | Free | Yes | Web | Use now; hammer-price visibility logged out is U | V · gaps-04 · https://www.artsy.net/price-database |
| Lot-Art Price Database | "75M+" results from "5,000+" houses since January 2016 | "Day Pass $9.90 one-time"; "Explorer $13.90/month"; "Prices shown are in USD billed monthly" | Free account, basic search | Web | Pay when it earns it: the Day Pass the first time a lamp or signed piece looks worth over about $300 | V · gaps-04 · https://www.lot-art.com/user-guide |
| WorthPoint Price Guide | eBay and auction sold prices, "nearly 2 decades" | Apple listing: "Price Guide Monthly $26.99", "Price Guide Annual $249.99"; vendor site 403 | Locked | Web, iOS | Pay when it earns it: a piece older than eBay's 3 years or fewer than five comps; buy monthly, cancel | V Apple, U web · verify-04 · https://apps.apple.com/us/app/worthpoint/id1472512649 |
| Artnet Price Database | Auction results, "items estimated at $500 and above" | Decorative Art "$34 /30 days*" | None | Web | Pay only in a month with a signed piece near $500 | V · verify-04 · https://www.artnet.com/price-database/ |
| WatchCount | eBay sold search and most-watched | "unknown"; search works without login | Free web | Web | By hand on the phone; never in the dashboard, terms ban AI access | V · gaps-04 · https://www.watchcount.com/ |
| Etsy estimators: eRank, EverBee, Alura, Marmalead, Sale Samurai, EHunt, Koalanda | Keyword data and sales estimates; no sold prices | See section 5 | Varies | Web | Skip for pricing | V · verify-04 · https://erank.com/plans |

Decision. Etsy exposes no sold prices, so pricing runs on eBay Product Research, EBTH, Invaluable's free 12 months, Chairish for the ceiling and Google Shopping for the new-equivalent ceiling. Pay per need: Lot-Art Day Pass $9.90, WorthPoint $26.99 for one month when a backlog needs older records, Artnet only for a $500-plus signed piece. For the dashboard: eBay bans scraping and WatchCount's terms ban "any automated agent, AI assistant, bot"; the only sanctioned feed is the Marketplace Insights API, whose docs sit behind a developer sign-in (U, gaps-04). The comps panel stays live links, as `docs/dashboard-design.md` section 10 already says. Dead or renamed: Algopix, Checkaflip, Prices4Antiques, ShelfTrend; EtsyHunt is now EHunt (gaps-04).

## 4. Shoot and edit photos

| Tool | Does | Price | Free tier | Platform | Verdict | Source |
|---|---|---|---|---|---|---|
| Windows 11 Photos; Paint | Remove or replace background, Generative Erase; Paint one-click "Background Removal" | Built in | Everything; "done locally on your device" | Windows 11 | Use now | V · verify-03, gaps-03 · https://support.microsoft.com/en-us/windows/apps/photos/edit-photos-and-videos-in-windows |
| Snapseed | Smart Masking, Healing, Batch Editing, RAW | "Free"; "no subscriptions, purchases, ads, or watermarks" | Everything | iOS 17+ | Use now; the phone retoucher | V · verify-03 · https://apps.apple.com/us/app/snapseed-photo-editor-camera/id439438619 |
| Apple Photos lift subject; Clean Up | Cutout for social; object removal | Built in | Clean Up needs "iPhone 15 Pro, iPhone 15 Pro Max, or iPhone 16 model or later" | iPhone | Social only; no save-as-PNG, so not listing grade | V · gaps-03 · https://support.apple.com/guide/iphone/clean-up-extend-and-reframe-photos-xy0grrlxue5w/27/ios/27 |
| Microsoft Designer | "Remove background", "Generative erase" | "available for free with a Microsoft account" | Free with account | iOS, web, Windows | Use now on the phone; disclose AI backgrounds on Etsy | V · gaps-03 · https://apps.apple.com/us/app/microsoft-designer/id6448308247 |
| rembg (BiRefNet) | Local cutout CLI and server | Free, "MIT license" | Everything | Windows Python, Docker | Use now, decided; always `-m birefnet-general`; "bria-rmbg ... The default" needs "a paid agreement for commercial use" | V · verify-03 · https://github.com/danielgatis/rembg |
| withoutBG | Open-weights cutout model, web demo, API | Open model "Apache-2.0"; API "100 credits 100 €10" | Local unlimited; web "5 free images a day" | Python, Docker, web | Use now as the second local engine | V · gaps-03 · https://withoutbg.com/ |
| Upscayl; PowerToys Image Resizer; Caesium; Squoosh; ImageMagick | Upscale to 2000px; bulk resize; batch compress; one-off compress; flatten PNG onto white | Free, open source | Everything | Windows, web | Use now; add the 2000px and 1600px presets yourself | V · verify-03, gaps-03 · https://upscayl.org/ |
| Affinity by Canva | Full photo and vector editor | "Affinity is free for individuals (seriously)" | Everything but "Access to Affinity with AI" | Windows, Mac, iPad | Use now for real retouching | V · verify-03 · https://www.affinity.studio/ |
| Canva | Background Remover, Magic Resize; takes in remove.bg from December | Free "US$ 0 /year for one person"; Pro "US$ 144 /year for one person" | Feature page: "Remove your photo's background for free"; quota U. Verify refuted the lane's "listed under Pro" | Web, Windows, iOS | Use now; Canva Free stands | V price, U quota · verify-03 · https://www.canva.com/features/background-remover/ |
| PicWish | Background remover, white background, bulk listing images | "Pro $4.99 /mo Billed Annually" ("billed $59.99/yr") | "Free ... Limited" | Web, iOS, Android, Windows | Pay at 20 or more listings a month from the phone; read the commercial terms first | V annual, U monthly · gaps-03 · https://picwish.com/pricing |
| Pixelcut; Photoroom | Phone cutouts, AI backgrounds, batch | Pixelcut "Pro $10 $8 per month, billed yearly"; Photoroom "Pro (monthly) 12.99 USD", "Pro (yearly) 89.99 USD" (JSON-LD only) | Limited | iOS, Android, web | Pay only if PicWish fails on edges; Pixelcut states "Commercial license" | V · verify-03 · https://www.pixelcut.ai/pricing |
| Pixian.AI; Path | Pay-per-image cutouts; hand-drawn clipping paths | Pixian "250 $5.00" credits, about $0.01 per 12 MP photo; Path "Clipping path FROM $0.39 PER IMAGE" | Pixian 0.25 MP web; Path "2 free edits" | Web | Pay per hero shot for crystal and chandeliers no local engine cuts | V · gaps-03, lane 03 · https://pixian.ai/pricing |
| remove.bg; Topaz Photo; Gigapixel; Luminar | Cutouts; paid upscalers and editors | remove.bg closes "from 1 December 2026 at 9:00am CET"; Topaz "$199/yr"; Gigapixel "$149/yr"; Luminar "$99.00" with "*365 days access to AI tools" | n/a | n/a | Skip | V · verify-03, lane 03 · https://www.topazlabs.com/pricing |

Decision. The free stack covers the job on both devices. Pipeline: shoot, rembg with `-m birefnet-general`, withoutBG as second engine, ImageMagick flattens every PNG before Etsy, PowerToys resizes to 2000px for Etsy and 1600px for eBay, Caesium brings the folder under 1 MB. Etsy's rules, V on lane 03: "transparent .png files are not supported ... will appear black"; "at least one unedited photo of the actual item against a real background"; 2000 pixels or more; over 1 MB "may not finish uploading"; note edits in the description, so the Haiku template needs a disclosure line whenever a background was replaced. Glass does not get cut, as the cutout handoff already says; Pixian or Path are the paid fallback per hero shot. Pay when it earns it: PicWish Pro at 20 or more listings a month. Skip every paid upscaler; Upscayl is free.

## 5. Write the listing

| Tool | Does | Price | Free tier | Platform | Verdict | Source |
|---|---|---|---|---|---|---|
| Etsy Marketplace Insights, Stats, Search Visibility | Real Etsy keyword volume; terms that brought shoppers; "title recommendations" | "Sellers can explore up to 15 keyword searches per week for free."; Etsy Plus "$10 USD per month" for unlimited | 15 a week | Etsy web | Use now; replaces a paid keyword tool at this scale | V · verify-02 · https://help.etsy.com/hc/en-us/articles/35122361353239 |
| eRank | Etsy keywords, tag audits, AI Listing Helper | Free "$0/mo"; Basic "$5.99/mo"; Pro "$9.99/mo" | "5 keyword lookups/day, 1 shop, 50 listings, 5 listing audits/day, 1 AI Listing Helper use/day" | Web, Chrome | Use now; Basic when 5 a day runs out | V · verify-02 · https://erank.com/plans |
| EHunt (was EtsyHunt); Alura | Etsy keyword search; AI listing optimization | EHunt Basic "$7.99 /month $95.88 billed" annual; Alura Basic "$11.99/mo" monthly or "$7.99/mo" yearly | EHunt "Keyword search 5 times/day"; Alura "5 daily keyword & product searches", "AI listing optimization (about 20)" | Web, Chrome | Use free now as second opinions | V annual, U monthly · gaps-02, verify-02 · https://ehunt.ai/pricing |
| Koalanda | Unlimited Etsy keyword searches, no AI | "$5.99 / month Billed every year as $71.88 USD"; "$11.99 / month Billed monthly" | "Limited searches" | Web | Pay when it earns it: cheapest unlimited keyword data | V · verify-02 · https://koalanda.pro/pricing |
| eBay Product research; 3Dsellers free eBay Title Builder; Keyword Tool Dominator | Sold-title vocabulary; title builder with live eBay keyword scores; eBay autocomplete | Free; free; "$9 USD One payment · 30 Days access" | Yes; yes; "2 searches per day per keyword source" | Web | The first two for every eBay title; KTD $9 once when a batch is ready | V · verify-02, gaps-02 · https://www.3dsellers.com/free-tools/ebay-title-builder |
| Free chatbots: ChatGPT, Claude, Gemini, Copilot | Draft title, 13 tags, description from a prompt and photo | Free tiers; Claude Pro "$17 Per month with annual subscription discount ... $20 if billed monthly" | Yes | Web, phone, Windows | Use now as the stopgap with one saved prompt | V · verify-02 · https://claude.com/pricing |
| Claude Haiku 5.5 API | The planned drafting engine in the dashboard | "$0.10 / MTok for prompts up to 100,000 tokens", then "$0.50 / MTok" | n/a | API | Use when the dashboard ships; decided | V · verify-02 · https://platform.claude.com/docs/en/about-claude/pricing |
| eBay app AI; Shopify Sidekick | Photo to listing in the eBay app; description writer in Shopify admin | Free in listing; Sidekick included, "availability can vary by plan, device, and language" | Yes | eBay app; Shopify admin | Free second opinion; review every line | V · verify-01, verify-02 · https://help.shopify.com/en/manual/ai-powered-tools |
| Crosslist AI add-on; Lysterly; Vela | Purpose-built listing writers | Crosslist "+$4.99/month", "1000 AI credits per month" on Gold; Lysterly "$19.99/mo ... Up to 30 Monthly Generations"; Vela "$29.95 / Per shop Per month" | None | Web | Pay only if chatbot drafts keep needing rewrites before the dashboard; skip Vela | V · verify-02, gaps-02 · https://crosslist.com/pricing |
| Marmalead; Sale Samurai; EverBee | Etsy keyword and product analytics | Marmalead "$19 USD paid monthly"; Sale Samurai "$19.99 Monthly"; EverBee Growth "$24.99 per month, billed annually at $299", monthly U | None; none; "10 keywords" | Web | Skip; no free tier, or built for products to copy | V · verify-02 · https://marmalead.com/pricing/ |
| SEOWILL (was SEOAnt) | Shopify SEO audits and AI content | "Pro Plan $29.99 / month or $287.90/year" | "AI Content Optimization - 30 credits", "On-page SEO Audit - 20 pages" | Shopify app | Use free once the store exists | V · gaps-02 · https://apps.shopify.com/seo-master |

Decision. Keywords come from first-party data first: Etsy Marketplace Insights and Stats, eBay Product research. eRank Free and EHunt Free add volume numbers. Drafts come from one free chatbot with a saved prompt until the Haiku dashboard ships: title under 15 words, item first, 13 tags of 20 characters or fewer, measurements and condition, a disclosure line for edited photos, no maker claim without a mark. Haiku stays the controlled path; the native writers are free but uncontrolled, and the Crosslist AI add-on would duplicate it. Pay when it earns it: eRank Basic "$5.99/mo" or Koalanda yearly when the free lookups run out; Etsy Plus "$10 USD per month" when 15 searches a week is a real limit. Reeva is dropped: reeva.ai is an industrial engineering company and no reseller product was found at any domain (lane 01, gaps-01, gaps-02). Nifty the reseller tool lives at nifty.ai, not nifty.app, and has no Shopify (verify-01).

## 6. List and crosslist

| Tool | Does | Price | Free tier | Platform | Verdict | Source |
|---|---|---|---|---|---|---|
| Etsy built-in: Seller app, bulk edit, copy listing | Phone listing; bulk edit tags, prices, shipping profiles; "You can't bulk upload new listings, but you can copy listings" | Free | Yes | Web, iOS, Android | Use now | V · verify-01 · https://help.etsy.com/hc/en-us/articles/360000337307 |
| eBay built-in: app AI listing, Seller Hub "Multiple listings from photos" | "Create a listing in a snap with the help of AI" | Free | Yes | App; Seller Hub | Use now; only the UK page was read, confirm in a US account | V UK · verify-01 · https://www.ebay.co.uk/sellercentre/news/2025-january/ai-bulk-listings |
| Crosslist (standing decision) | One form to 11+ marketplaces incl. all three; "API-first"; autodelist on Gold and Diamond only | "Gold $39.99 per month"; yearly tab "$32.99 per month billed yearly"; AI "+$4.99/month"; Diamond "$44.99 per month" | None. "20 free listings with our 3-day money-back guarantee", "whichever comes first"; card required; annual refunds carry "a small $9.99 processing fee" | Web, iOS, Android, extension (v3.12.7, Nov 6 2026) | Trial means paying $39.99 up front and testing inside 3 days or 20 listings | V · verify-01, verify-13 · https://crosslist.com/pricing |
| Secnd | Crosslist to eBay, Etsy, Shopify, Depop; "Inventory sync + automatic delisting" | "Free $0 CAD/mo Free forever"; "Starter $29 CAD/mo Billed monthly" | "Unlimited cross-posting", "AI listings, 5 / month", auto-delist | Web, iPhone (17 ratings) | Use now, free, on two cheap items; confirm eBay is connectable | V · gaps-01 · https://www.secnd.ca/pricing |
| Swiftlisted | eBay and Shopify by API; Etsy via a Chrome extension on a PC that must be on; sold scan every 30 min | "Starter $6 USD/mo $72 USD billed yearly"; monthly U | "Free trial $0 for 30 days ... No credit card"; no free plan | Web, Chrome, iPhone (0 ratings) | Run the 30-day trial against Secnd; pay if it wins | V yearly, U monthly · gaps-01 · https://www.swiftlisted.ai/pricing |
| VendorSnap | Phone lister: eBay and Etsy by official API; no Shopify | Pro "$6.67/month Billed yearly at $79.99" | Free plan; "7-day free trial" for Pro | iPhone, Android (48 ratings) | Use free now for phone listing to Etsy and eBay | V yearly · gaps-01 · https://vendorsnap.app/ |
| Vendoo | 11 marketplaces incl. all three; sale detection on Starter | "STARTER $12.49 Per month, billed yearly"; "$14.99 Per month, billed monthly" (verify: the monthly figure is on the page) | "Try Vendoo Free for 14 Days"; card requirement U | Web, iOS, Android | Pay when it earns it: first paid trial; auto-delist covers "Poshmark, eBay, Mercari, Depop, Whatnot, and Etsy", not Shopify | V · verify-01 · https://www.vendoo.co/pricing |
| FLUF Connect; Voolist | "70+ marketplaces", "Sales checked every 90 min"; 11 platforms, auto-delist on every plan | FLUF "Starter $9 /month"; Voolist "Starter $19.99 / month Billed monthly" | FLUF "Start 7 days for $1"; Voolist "14-day money-back guarantee" | Web, app | Pay when it earns it if Vendoo disappoints, or if Shopify auto-delist matters | V · verify-01 · https://www.voolist.com/pricing |
| Closo | Free crosslist to eBay, Shopify, Poshmark, Mercari, Depop, Vinted; no Etsy | "Free $0 forever"; "Member $99 / year" | "No caps on listings." | Web | Only for the eBay plus Shopify pair | V · verify-01 · https://closo.co/pages/pricing |
| PrimeLister; List Perfectly; Nifty; Posh Sidekick; SellerAider; OneShop | Other crosslisters | PrimeLister "$49.99 Per Month" (verify filled the lane's "unknown"); List Perfectly "Simple $29 Monthly", Auto Delist "Pro Plus $99+"; Nifty "Crosslisting Plus ($35.99/month)" | Various trials | Web | Skip: dearest, or no Shopify, or auto-delist at $99 | V · verify-01 · https://www.primelister.com/pricing/cross-listing |
| 3Dsellers hosted MCP | eBay, Etsy, Shopify writes from a chat, "no eBay developer account" | "Essential $19 $16 /Mo Billed Annually", 100 Listings; "AI Lite $9/mo" | "Try All Features for 7 Days Free" | Web, remote MCP | Fallback only if the crosslister trial disappoints; Etsy and Shopify on Essential U | V · gaps-15 · https://www.3dsellers.com/pricing |
| Shopify stock sync: QuickSync, Shuttle, shopUpz, Sellbrite, Trunk | Etsy to Shopify stock, product and order sync once the store exists | QuickSync "Lite Plan $19 / month"; Shuttle "Essential $12 / month", "Growth $19 / month" real-time; shopUpz "UNLIMITED $18 / month"; Sellbrite "Pro 100 $19 / month"; Trunk "From $35/month" | QuickSync "Free: $0, 100-variant stock sync for eligible shops"; Shuttle "10 product transfers per month"; Sellbrite "Up to 30 Orders Monthly 2-hr Inventory Quantity Sync" | Shopify apps | Free tiers when the store exists; pay only after a crosslister misses a sale | V · gaps-01, verify-16 · https://apps.shopify.com/shuttle-transfer-from-etsy |
| Shopify Marketplace Connect | Shopify to eBay, Amazon, Walmart, Target Plus; "New connections to Etsy can't be made at this time" | "Free to install"; "First 50 marketplace-synced orders/mo free, 1% fee per additional synced-order, capped at $99/month" | 50 orders | Shopify app | A free eBay leg later; not an Etsy replacement | V · gaps-14 · https://apps.shopify.com/marketplace-connect |
| API routes after Step 0 keys: Etsy Open API v3 Seller App; eBay official MCP; YosefHayim/ebay-mcp; aserper/etsy-mcp | Sanctioned automation | Etsy "Approval Automated, near-instant", no fee stated; eBay MCP "Only GET requests are supported"; both community MCPs free, MIT | Yes | Claude Code | Etsy key is Step 0; eBay official MCP for comps; etsy-mcp dormant since Apr 2, 2026, read before running | V · verify-15, gaps-15 · https://github.com/eBay/npm-public-api-mcp |

Decision. Listing stays Etsy-first from the phone, as Phase 1 says. Until Ricky decides the crosslister, the free tests cost nothing and answer the real question, sale-to-delist latency on a quantity-1 item: Secnd Free and the Swiftlisted 30-day trial on the same two cheap items, VendorSnap free for phone listing to Etsy and eBay. The standing decision is Crosslist Gold, and the research argues against paying first; that goes to Ricky in Contradictions. Terms: eBay bans "any robot, spider, scraper ... or other automated means" without permission (verify-01), so prefer API posting; Crosslist says "API-first", and Voolist, Nifty, SellerAider and Secnd print Etsy API notices, but no file confirms how Crosslist reaches eBay (verify-11). Facebook Marketplace is always extension-driven; keep it manual. Zipsale is "made to be used in the UK" and inkFrog redirects to Wix (verify-01).

## 7. Ship

| Tool | Does | Price | Free tier | Platform | Verdict | Source |
|---|---|---|---|---|---|---|
| Pirate Ship with InsureShield | USPS and UPS labels; imports Etsy, eBay, Shopify orders | "No monthly fees"; "we're paid by the carriers, not by you!"; InsureShield "$1.00 for every $100 of declared value" | All free, "No credit card required" | Web | Use now as primary; InsureShield on non-Etsy items over $100 | V · verify-10 · https://www.pirateship.com/integrations/etsy |
| Etsy labels with Shipsurance | Labels inside the order; "helps you qualify for Etsy Purchase Protection" | "no additional membership fees"; Shipsurance "$0.80 per $100 of order value" domestic, "$1.35 per $100" international | Pay postage | Web, Seller app | Use now for every Etsy order; insure over $250 | V · verify-10 · https://help.etsy.com/hc/en-us/articles/360001988847-Insurance-and-Claims-for-Shipping-Labels |
| eBay Labels; eBay International Shipping; ShipCover | USPS, FedEx, UPS labels, QR code at the counter; eBay handles the international leg | "no subscription fees"; EIS "no extra charge"; ShipCover rates did not render | Pay postage | Seller Hub, app | Use now for eBay orders; leave EIS on; skip ShipCover until rates are readable | V fees, U ShipCover · verify-10, verify-14 · https://www.ebay.com/sellercenter/shipping/ebay-international-shipping |
| ShipSaving | USPS, UPS, FedEx, DHL Express labels; QR codes; iPhone app | Starter "Free/ month"; Pro "$15/ month(starting at)" | "Up to 50 labels/month", "No credit card required" | Web, iOS | Use now as the FedEx and DHL backup; Etsy connection seen only in a review | V · gaps-10 · https://www.shipsaving.com/en/pricing |
| ShipSaver (Shipsurance) | Pay-as-you-go insurance on any label | USPS "$0.01 – $50.00 $0.65", "Each additional $100 $1.00"; UPS and FedEx "Per $100 of declared value $0.75" | "No monthly fees (pay-as-you-go)" | Web | Use now for eBay and Shopify orders over $100; undercuts InsureShield on UPS | V · gaps-10 · https://www.shipsaver.com/insurance-calculator/ |
| USPS free Priority Mail boxes; Label Broker; Addresses 3.0 | Free boxes; QR-code label printed at the Post Office; free address validation API | "Priority Mail® Shoe Box $0.00"; Label Broker free; APIs "free of charge" | Free | Post Office, API | Use now; Label Broker until the printer arrives; Addresses 3.0 replaces Smarty in the dashboard | V · verify-10, gaps-10 · https://developers.usps.com/addressesv3 |
| Munbyn RW403B printer; IPS03 scale | 4x6 thermal labels; 440 lb scale | "$79.99" sale against struck "$159.99"; IPS03 "$39.99" against "$49.99" | n/a | USB, Bluetooth; phone support U | Buy once while the sale holds | V price, U phone · verify-10 · https://munbyn.com/search?q=RW403B |
| GoShare; Roadie | On-demand truck or van; same-day oversized delivery | No published price, "free estimate in the app"; Roadie no public price | n/a | Apps | GoShare now for local chairs and large art; Fort Myers, Cape Coral and Naples listed. Lugg has no Lee or Collier service (verify corrected the lane's city count) | V · verify-10, gaps-10 · https://goshare.co/florida/ |
| Shopify Shipping on Basic | Labels in admin, "Up to 87% off" | Basic "$29 USD/mo" yearly, "$39 USD/mo" monthly; the "$200 USD of shipping insurance" needs Grow "$79" plus Shopify Payments | 3-day trial | Shopify | Included at store launch; do not upgrade to Grow for the insurance | V · verify-10 · https://www.shopify.com/pricing |
| The UPS Store Pack & Ship; TSI; Freightquote and FreightCenter | Packing with guarantee; single-item furniture and art freight; LTL quotes | "prices may vary. Contact your neighborhood location"; TSI quote only; freight quotes "no signup required" | Free quotes | In store, web | Pay per high-value chandelier or out-of-state chair; quote before listing | V, prices U · verify-10, gaps-10 · https://www.theupsstore.com/pack-ship/artwork |
| Chairish-Managed Shipping | UPS parcel or In-Home delivery arranged and insured by Chairish; buyer pays | "start at $11" parcel, "start at $149" In-Home | Buyer pays | Chairish | A channel decision: best furniture route if Chairish is used | V · lane 10 · https://support.chairish.com/hc/en-us/articles/44167972846097-Available-Shipping-Methods-for-Sellers |
| Shippo; ShipStation; Stamps.com; Veeqo; XPS Ship | Multi-carrier label tools | Shippo Pro "$17/mo" annual only; ShipStation Starter "$14.99 /month"; Stamps.com Basic "$14.99 /month", "Print up to 10 shipping labels" | Shippo 30 labels; Veeqo "Free" but no Etsy | Web | Skip; ShipSaving gives 50 free labels and FedEx | V · verify-10, gaps-10 · https://goshippo.com/pricing |

Decision. Pirate Ship is the primary label tool, Etsy labels for Etsy orders because they feed Star Seller and Purchase Protection, eBay Labels for eBay orders. Insurance by channel: Shipsurance inside Etsy, ShipSaver for eBay and Shopify, InsureShield only where ShipSaver is dearer. Buy the Munbyn printer and scale once; until then USPS Label Broker prints at the counter. Large pieces go GoShare locally and TSI or Freightquote out of state, quoted before the listing goes up. Fixed Etsy shipping classes stand, with two January tasks: Etsy's USPS page says "a temporary 8% rate increase ... expected to last through January 17, 2027", and "USPS charges an additional $4 fee" for "Cylindrical rolls" (verify-10), so rolled prints need their own class or a buffer. Etsy prioritizes US listings with domestic shipping under $6 in search (verify-14): set the smallest class under $6 or free. Skip Stamps.com, Shippo, Veeqo and XPS Ship.

## 8. Market and extra channels

| Tool | Does | Price | Free tier | Platform | Verdict | Source |
|---|---|---|---|---|---|---|
| Etsy Share & Save | Fee refund on sales from Hollie's own `yourshopname.etsy.com` link | "instant refund of 4% off the eligible order total"; "From October 20 to January 4 ... 6.5% back" | Free, opt-in | Etsy | Use now; links in Messages or descriptions do not count | V · verify-08 · https://help.etsy.com/hc/en-us/articles/16981332744087 |
| Etsy Offsite Ads; Etsy Ads | Ads on Google and social, fee on attributed sales; pay-per-click in Etsy search | Offsite "15% fee", "will never exceed $100 USD" per order, opt-out under $10,000; Ads "maximum daily budget of $25" to start, "15 day waiting period" | No upfront cost | Etsy | Decide Offsite Ads before the first sale; Etsy Ads only as $1 to $3 a day tests | V · verify-08, verify-14 · https://help.etsy.com/hc/articles/360000338367 |
| eBay Promoted Listings General | Paid only when a promoted item sells | "ad rate between 2% - 100%"; needs Above Standard | No upfront cost | eBay | Pay when it earns it: fixed 3% to 5% on slow pieces, never dynamic without a cap; skip Promoted Offsite | V · verify-14 · https://www.ebay.com/help/selling/ebay-advertising/promoted-listings/general-campaign-strategy?id=4164 |
| Email: Shopify Messaging; Kit Free (prior); Brevo; Klaviyo, Omnisend, Mailchimp | Campaigns and automations | Shopify "first 10,000 emails each month are free", then "$1/1000"; Brevo "Free forever", "up to 300 emails per day"; Klaviyo "$20 /month"; Omnisend list $16/mo (verify: "$11.20/mo" needs 3 months upfront); Mailchimp Essentials "$13 /month" | Klaviyo, Omnisend, Mailchimp stop at 250 contacts | Web, Shopify | Kit Free before Shopify stands from Round D; lane 08 could not read Kit's page. Shopify Messaging at launch. Skip the 250-contact tiers; Brevo's 300 a day cannot send a drop alert to a list over 300 | V · verify-08, gaps-08 · https://apps.shopify.com/shopify-messaging |
| Shopify channels at launch: Shop, Google & YouTube, Microsoft Channel, Pinterest, Facebook & Instagram by Meta, Judge.me | Free listings and reviews | All "Free to install"; Judge.me "Free $0 per month", "Awesome $15 per month" is "the most you can ever pay us" | Yes | Shopify | Use at launch; Meta "is no longer a marketplace tax facilitator" since August 26, 2025, set tax first; Microsoft Channel rates "2.8" from "338" | V · verify-08, gaps-08 · https://judge.me/pricing |
| Linktree; QRCode Monkey; Canva QR | Link page; static QR for inserts and the disco-ball tag | Linktree Starter "$7 Billed annually, or $9 monthly"; QR "100% free ... all commercial purposes" | Linktree Free | Web | Use free now; skip paid tiers | V · verify-08 · https://www.qrcode-monkey.com/ |
| Chairish | Curated marketplace; approves items, arranges shipping, pays via PayPal | "1 - 9 active listings Free membership ... 40% Flat Commission"; "10+ active listings ... 30% Flat Commission"; Premium "$49 / Month" at 25% | Free to list | Web, iPhone and iPad app | Use now for furniture, lighting and art over about $300 once 10 can be live | V · verify-08 · https://www.chairish.com/pages/consign-with-us |
| Mercari; Whatnot; Palmstreet | General marketplace; live selling; plant and decor live app | Mercari "10% of the item price + buyer-paid shipping"; Whatnot "≤8% ... + ... 2.9% on total order value + $0.30"; Palmstreet "Selling Fee: 6.9%" plus "2.9% + $0.3" | Free to list | Apps | Mercari now for pieces under $200; one live show when 20 to 40 small pieces are in stock | V · verify-08, gaps-08 · https://www.mercari.com/us/help_center/article/169/ |
| Local: Craigslist by-dealer; Nextdoor Business Page; Yelp; Google Business Profile; Vintage Market Days | Local pickup posts; free pages; juried market "January 29 - 31, 2027 Lee Civic Center" | Craigslist "$5" per by-dealer post; pages free; booth fee behind the vendor login | Free profile | Web | Free pages now; GBP as a service-area profile for Hire Hollie only; VMD vendor profile now, "home decor is accepted ... but in limited quantities" | V, fee U · gaps-08 · https://www.vintagemarketdays.com/market/south-gulf-coast-florida/ |
| Buffer Free (prior) | Scheduler | Verify: "Connect up to 3 channels", "10 scheduled posts per channel"; paid "$5 /month" is "$60 billed yearly", monthly U | Free | Web, apps | Stands | V · verify-08 · https://buffer.com/pricing |

Decision. The cheapest buyer acquisition is inside Etsy: Share & Save in every bio, pin and email from day one. Offsite Ads is Ricky's call before the first sale: leave on for 60 days and read attribution, or opt out while under $10,000 if video traffic is the plan. Pinterest business account today; the Shopify channels on launch day in this order: Shop, Google & YouTube, Pinterest, Microsoft, Meta after tax settings, Judge.me Free. Round D's Pinterest correction stands: pre-owned products are not allowed as Product Pins, so pins are plain or Article Pins. Chairish is the furniture route at 30% from 10 listings, with Chairish-managed shipping. Pay when it earns it: an Etsy Ads two-week test on the five best-photographed listings, kept only at 5x spend; eBay Promoted General once Above Standard; Judge.me Awesome "$15 per month" when reviews should show in Google Shopping; Chairish Premium "$49 / Month" above $1,000 a month there. Skip Klaviyo, Omnisend and Mailchimp. Linkpop is gone (gaps-08). Facebook Marketplace stays a manual local-pickup channel; its fee pages would not load (U).

## 9. Messages and bookings

| Tool | Does | Price | Free tier | Platform | Verdict | Source |
|---|---|---|---|---|---|---|
| Etsy Messages: auto-replies, quick replies, writing assistant | Temporary auto-replies "from an hour to a maximum of five days", weekly auto-replies, US-only writing assistant; auto-replies count toward Star Seller | Included | Yes | Etsy.com for auto-replies; Seller app for quick replies | Use now | V · verify-11 · https://help.etsy.com/hc/en-us/articles/115015654988-How-to-Send-Messages-to-Buyers |
| Shopify Inbox, Flow, Email, pickup in store | Chat; automations; email; pickup | "Pricing Free"; Flow "free app available on the Basic, Grow, Advanced, and Plus plans"; Send HTTP Request needs Grow | Yes with a plan | Shopify | Use at launch; Flow on Basic cannot call Pushover or Supabase | V · verify-11 · https://help.shopify.com/en/manual/shopify-flow |
| Cal.com | Booking page with payments | Teams "$12per user/month" yearly, branding removal only | "Free forever": "1 user", "Accept Stripe & PayPal payments", "no usage limits" | Web, app | Use now; one Stripe-paid consult type, one free Screen Test type | V · verify-11 · https://cal.com/pricing |
| zcal; TidyCal; YouCanBookMe; Calendly | Backups | zcal Pro "$7 per user / month", "Fee on payments 3%" on free; TidyCal "Lifetime $29 once", "1% platform fee"; YouCanBookMe "Free $ 0 / month", "30 bookings per month"; Calendly Standard Plus "$18 /seat/mo" | First three take payments on free; Calendly Free does not | Web | Skip for now; Calendly cannot take the deposit | V · gaps-11, verify-11 · https://zcal.co/pricing |
| Appointo; Cowlendar (Shopify) | Bookings as Shopify products | Appointo Pro "$14 / month or $151/year"; Cowlendar Starter "$13.99 / month" | Appointo "Unlimited Bookings" with Appointo branding; Cowlendar "5 bookings/mo" | Shopify | Appointo Pro pay when it earns it; skip Cowlendar | V · verify-11, gaps-11 · https://apps.shopify.com/appointo-appointments-and-bookings |
| Tally | Forms with payments | Pro "$24 per month" | "unlimited forms and submissions, completely free", "Collect payments" | Web | Use now for Hire Hollie intake | V · gaps-11 · https://tally.so/pricing |
| Linktree; Carrd | Link page; one-page site on an own domain | Carrd "Pro Standard $19 / year" | Linktree Free; Carrd "up to three sites" with branding | Web | Linktree Free now; Carrd $19 / year when the bio page should sit on Hollie's domain | V · gaps-11 · https://carrd.co/ |
| Espanso; Text Blaze; iPhone Text Replacement | Canned replies | Espanso free, GPL-3; Text Blaze Pro "$2.99 USD per month, billed yearly" | Espanso all; Text Blaze "Limited snippets"; iOS built in | Windows; Chrome; iPhone | Use now, the same reply library on PC and phone | V · verify-11, gaps-11 · https://espanso.org/ |
| Instagram FAQ automated responses; ManyChat; Beacons | DM automation | ManyChat page 403, "Start Free" on Play; Beacons "9% seller fees" on Free | Instagram built in | Apps | Instagram FAQs now; ManyChat only when "link please" comments outrun manual replies and the price is read; never sell through Beacons | V feature, U price · gaps-11, verify-11 · https://help.instagram.com/search/?query=saved%20replies |
| Zapier; n8n; Activepieces; IFTTT; Make | Workflow glue | Zapier "Free forever $0 /month", "100 tasks per month", Professional "Starting from $19.99 /month"; n8n Cloud Starter "$20 /mo, billed annually" (verify corrected 20€); Activepieces "$0 Free forever", "1,000 credits a month"; Make 403 | n8n self-hosted Community "free ... indefinitely" | Web; Fedora box | n8n Community or Activepieces only if the dashboard needs glue Supabase does not cover; skip Zapier, "Etsy has not yet built an integration on Zapier" | V, Make U · verify-11, gaps-11 · https://docs.n8n.io/n8n-community-license |
| Google Voice; Pushover | Shop phone number; push alerts | Google Voice personal calls "free"; Pushover "$4.99 USD one-time purchase on each platform" | Yes; "10,000 messages per month for free" | Web, phone | Use now; never script texts | V · lane 11, verify-11 · https://support.google.com/voice/answer/115061 |
| Help desks: Tidio, Crisp, Help Scout, Chatwoot, Zoho Desk, HubSpot | Shared inbox | Tidio Starter "$24.17 /mo."; Help Scout "$25 per user/mo" | Free tiers exist | Web | Skip; one person does not need a ticket queue | V · lane 11, gaps-11 · https://www.tidio.com/pricing/ |

Decision. Etsy's own messaging is the whole customer-service layer for the Etsy side: a weekly auto-reply for away hours, 8 to 12 quick replies, the writing assistant on. The same reply library lives in Espanso on the PC and Text Replacement on the iPhone. Hire Hollie books through Cal.com Free and intakes through Tally, both taking payment on free, which matches the Fabulous From Online rule of payment before any visit. Haiku stays for listing drafts, not buyer replies. Pushover stands; alerts from Shopify events need the Shopify API, n8n or Activepieces, because Flow on Basic has no Send HTTP Request (verify-11). Skip Calendly, Gorgias, Freshdesk, Chatfuel and every browser bot on eBay or Facebook.

## 10. Books and tax

| Tool | Does | Price | Free tier | Platform | Verdict | Source |
|---|---|---|---|---|---|---|
| Airtable | Item ledger with photos; Ricky has it | Team "$20USD per seat/month" annual | "1,000 records per base", "1 GB of attachments per base" | Web, apps | Use now; stopgap until Supabase | V · verify-09 · https://airtable.com/pricing |
| Zoho Books | Books: autoscans, mileage, reconciliation, P&L | "STANDARD $20 $15 Price/Org/Month Billed Annually" for bank feeds (verify correction: Free has none) | "FREE $0 ... Receipt and Document Autoscans ... Mileage tracking ... Bank reconciliation ... 1 User + 1 Accountant" | Web, apps | Use now; import statements by hand | V · verify-09 · https://www.zoho.com/us/books/pricing/ |
| TripLog | Automatic mileage | Premium "$4.99 Per month Paid annually" | Basic "Unlimited automatic GPS mileage tracking ... Free forever" | iOS, Android | Use now | V · verify-09 · https://www.triplog.net/pricing |
| FreeTaxUSA | Federal Schedule C filing | "Federal Tax Returns Free", "State Tax Returns $15.99" | Free federal; no Florida return | Web | Use at filing time | V · verify-09 · https://www.freetaxusa.com/pricing/ |
| Shopify Tax | Sales tax on the own store | After "$100,000 USD" lifetime sales, "0.35%" per order, max "$0.99 USD" | Free to the threshold for stores created on or after May 13, 2026 | Shopify | Use at launch, after Florida DR-1 registration | V · verify-09 · https://help.shopify.com/en/manual/taxes/shopify-tax/pricing |
| Avery Design & Print Online; NIIMBOT D110; Brother QL-800 | SKU and QR labels | Avery free; NIIMBOT "Regular price $29.99 USD Sale price $20.90 USD"; Brother "$124.99" | Avery all | Web; phone; USB | Avery now on the existing printer; NIIMBOT when tags must print at the rack; skip Brother | V · gaps-09, verify-09 · https://www.avery.com/software/design-and-print/ |
| Flippd | Phone-first reseller ledger: cost per item, fees, net profit, Schedule C; one-way eBay sync | Pro "$8.33/mo billed annually ($99.99/yr), or $9.99/month" | "free for up to 20 inventory items, plus 25 expenses and 30 mileage entries a month" | iPhone, Android, web | Use free on 20 pieces to test; see Contradictions before paying | V · gaps-09 · https://getflippd.com/pricing |
| Seller Ledger | Books for online sellers; imports Etsy, eBay, Shopify | "Up to 250 transactions per month $10 /month $100 /year" | "30-day free trial No credit card required" | Web | Pay when orders flow; monthly plans look back only 90 days | V · verify-09 · https://sellerledger.com/pricing/ |
| Inventory Now; My Reseller Genie | Item tracker with Shopify, eBay, Etsy connections; reseller books with marketplace sync | Inventory Now Personal "$10 BILLED $120 YEARLY"; MRG "Ultimate $22.99 per month" is the only tier with sync | Inventory Now "Free for your first ten items." | Apps; MRG web only | Pay only if three-channel stock sync from the phone is wanted; Etsy connection shipped "Nov 2, 2026" | V · gaps-09, verify-09 · https://www.inventorynow.com/ |
| QuickBooks Free and Solopreneur; Wave; ZipBooks; Found | General small-business books | QuickBooks Solopreneur "$20 $10/mo 50% off for 3 months*"; Wave "PRO Plan $190USD/year"; Found Plus "$35/mo" | QuickBooks "Connect 1 bank", "2 invoices per month"; Wave Starter $0 with hand entry | Web | Skip: capped, bank import paid, or a bank switch | V · verify-09, gaps-09 · https://quickbooks.intuit.com/pricing/ |
| Everlance; MileIQ; Hurdlr; Zoho Expense | Mileage and expenses | Everlance "Starter $89.99 Per year or $10.99 per month"; MileIQ "Unlimited $11.66 PER MONTH BILLED ANNUALLY" | MileIQ "40 FREE DRIVES EVERY MONTH"; Everlance 30 trips | Apps | Skip; TripLog is unlimited and free | V · verify-09 · https://mileiq.com/pricing |
| Sortly; BoxHero; Flipwise; Keeper | Photo inventory; eBay-only books; pro-signed filing | Sortly "Advanced $24 USD/mo.* Billed at $288/yr."; Flipwise "$19.99 /mo"; Keeper "Standard $199 /yr" | Sortly "100 Unique Items"; Flipwise "Up to 24 listings" | Web, apps | Skip Sortly and Flipwise; Keeper only if Hollie wants a tax pro | V · verify-09 · https://www.sortly.com/pricing/ |

Decision. Day one is $0: Airtable Free as the item ledger with cost-basis columns, Zoho Books Free with statements imported by hand, TripLog Basic for sourcing miles, Avery labels on the existing printer, FreeTaxUSA at filing time. Seller Ledger "$10 /month" is the first paid books tool, started the month of the first sale. Tax facts that hold (verify-09): 1099-K only above $20,000 in more than 200 transactions, all income reportable regardless; Florida 6% plus Lee 0.5% through December 31, 2028, Collier none; Etsy and eBay remit as marketplace facilitators and those sales are excluded from the shop's own return; the Shopify store needs DOR registration on form DR-1 first, then Shopify Tax; Lee County's business tax receipt is "$50" for an October to March start, prorated after, expiring September 30; no DOR page states a registration fee (U). Which county the room is in is unconfirmed and decides the surtax and the receipt.

## 11. Desktop utilities and video

| Tool | Does | Price | Free tier | Platform | Verdict | Source |
|---|---|---|---|---|---|---|
| DaVinci Resolve 21; Clipchamp; CapCut Desktop | Full editor; 1080p cuts "Watermark-free"; vertical templates and video Remove BG | Free; DaVinci Studio "Was $295 Now $236" one-time; CapCut Pro "USD 19.99 /month", toggle unlabelled, "Displayed pricing is for reference only" | All | Windows | Use now; no CapCut library music until Ricky reads its terms (every terms page failed) | V · verify-12 · https://www.blackmagicdesign.com/products/davinciresolve |
| LosslessCut; HandBrake; Subtitle Edit; Buzz; OBS Studio; Snipping Tool; CuePrompter; Audacity | Trim without re-encode; compress; offline Whisper captions; recording and live; screen video with Win+Shift+R; teleprompter; audio | Free, open source | All | Windows, browser | Use now | V · gaps-12, verify-12 · https://www.nikse.dk/subtitleedit |
| Music: Meta Sound Collection; Incompetech; YouTube Audio Library; Bensound; Epidemic Sound | Licensed music | Bensound "All Access $9 /month (Billed $119 annually)"; Epidemic Pro "$16.99 Per month, billed $203.88 yearly" for "commercial use online" (verify: the lane named the wrong tier) | Meta "Free to use in any videos you create and share on Facebook and Instagram" only; Incompetech CC BY 4.0 with credit | Web | Meta for Reels, Incompetech with a credit line elsewhere; Bensound when credit lines become a chore; skip Epidemic | V · gaps-12, verify-12 · https://www.facebook.com/sound/collection/ |
| Veed; Kittl; Opus Clip; Descript; ElevenLabs | Auto subtitles; vintage lettering; AI clipper; text-based editor; AI voice | Veed Creator "$12 per user / month billed yearly"; Kittl Pro "$14 /mo, billed annually"; Opus Clip Starter "$15 USD/mo"; ElevenLabs Free "does not include a commercial license" | Kittl "$0 /mo, free forever" with "Full commercial license"; Opus free watermarks | Web | Kittl Free now; Veed when a captioned video goes out daily; skip the clippers and AI voices, Hollie's own voice is the brand | V · verify-12, gaps-12 · https://www.kittl.com/pricing |
| Bitwarden | Password manager | Premium "$1.65 per month" "Billed annually at $19.80" | "Unlimited devices, unlimited passwords" | Everywhere | Use now; Premium when TOTP codes in the vault are wanted; 1Password has no free tier | V · verify-13 · https://bitwarden.com/pricing/ |
| LanguageTool; Harper; Grammarly | Grammar checkers | LanguageTool Premium Annual "$69.90 /year"; Grammarly Pro "$12 USD", period U | LanguageTool free, no account; Harper "$0", runs locally | Chrome, Edge, Windows | One of the first two; skip Grammarly | V · verify-13, gaps-13 · https://writewithharper.com/ |
| PowerToys; Snipping Tool OCR; Win+V; Ditto; ShareX; Win+H voice typing | Resize, OCR, rename, clipboard, scrolling capture, dictation | Free | All; Win+V holds 25 entries and clears on restart except pinned (verify) | Windows | Use now; Ditto only when the 25-entry cap bites | V · verify-13, gaps-13 · https://learn.microsoft.com/en-us/windows/powertoys/install |
| iCloud for Windows and iCloud+; HEIF and HEVC extensions; LocalSend | Full-resolution iPhone photos in File Explorer; open HEIC; play HEVC; local Wi-Fi transfer | iCloud+ "200 GB" "$2.99" "billed monthly"; HEIF "Free"; HEVC "$0.99" one-time | iCloud "5 GB"; LocalSend "100% free and open source" | Windows 11, iPhone | Use now; $2.99 a month when 5 GB fills, which is fast | V · verify-13, gaps-13 · https://support.apple.com/en-us/108047 |
| Wispr Flow; Superwhisper; Aqua Voice | AI dictation that cleans up speech | Wispr Pro "$12/user/mo"; Superwhisper Pro "$8.49/month" yearly | Wispr "$0/mo", "Limited words per week" | Mac, Windows, iPhone | Wispr Free for a week; Pro when the weekly cap stops a listing session; skip the others | V · verify-15 · https://wisprflow.ai/pricing |
| Claude in Chrome; Claude Cowork | Browser agent: "clicks, types, and fills forms"; Cowork browser on Windows beta | "Available on all paid plans."; Cowork "Works with a paid plan." | No, paid plans; Ricky already pays | Chrome; Windows desktop | Use now on Etsy only, Ricky watching, "safety check on each action" on; never on eBay, Facebook or Chairish; never scheduled | V · verify-15, gaps-15 · https://claude.com/claude-in-chrome |
| Gemini in Chrome auto browse; ChatGPT Work cloud browser; Perplexity Comet; Opera Neon; Nanobrowser | Other browser agents | Google AI Pro "$19.99/ month", US preview; ChatGPT Plus "$20/month (billed monthly)", cloud browser "excluding Free and Go"; Comet price U; Neon "$19.90/month"; Nanobrowser free, Apache-2.0 | Varies | Chrome, web | Skip; ChatGPT agent and Atlas are retired; the cloud browser runs unattended, which marketplace terms forbid | V, Comet U · verify-15 · https://help.openai.com/en/articles/20001280-using-cloud-browser-in-chatgpt |

Decision. A fully free Windows stack covers editing, captions, recording and design: DaVinci Resolve, Clipchamp, CapCut without its music, LosslessCut first on every iPhone clip, HandBrake under TikTok's 500 MB, Subtitle Edit for offline captions, OBS for live selling, Affinity and Canva Free for graphics, Kittl Free for retro lettering. Music licences matter more than tool prices: Meta Sound Collection only on Facebook and Instagram, Incompetech with a credit line everywhere else, nothing from CapCut's library until its terms are read. AI video generators are out: a one-of-one listing must show the real object, and Sora was "discontinued on April 26, 2026" (verify-12). Utilities: Bitwarden, PowerToys, one grammar checker, iCloud for Windows for full-resolution originals, LocalSend for same-day batches. Dictation is free on both devices; iPhone Dictation needs no signal, which matters in a thrift store. The browser agent is Claude in Chrome on Etsy only, with Ricky watching; browser sessions and Claude Code draw from "the same pool" (verify-15), and drafts through the API key are unaffected. Pay when it earns it: DaVinci Studio one-time, Veed Creator, Kittl Pro, Bensound, iCloud+.

## Cost ladders

### The $0 stack

| Stage | Tools | Monthly |
|---|---|---|
| Source | EstateSales.net, EstateSales.org, Trove, eBay saved searches, Proxibid, LiveAuctioneers, Craigslist alerts, CTBids, HiBid, Goodwill VIP Perks, changedetection.io self-hosted | $0 |
| Identify | Google Lens, Bing Visual Search, Kovels guide pages, marks bookmark folder, VFG, FTC RN, Antiquers, Appraisily free ID, FindArtInfo free account | $0 |
| Price | eBay Product Research, Poshmark Sold, Chairish, EBTH, Invaluable free, Artsy, Bidsquare, HiBid, Google Shopping | $0 |
| Photos | Windows 11 Photos and Paint, Snapseed, Microsoft Designer, rembg BiRefNet, withoutBG, Upscayl, PowerToys, Caesium, ImageMagick, Affinity, Canva Free | $0 |
| Write | Etsy Marketplace Insights and Stats, eRank Free, EHunt Free, Alura Free, 3Dsellers Title Builder, one free chatbot | $0 |
| List | Etsy Seller app, eBay app, Secnd Free, VendorSnap Free, Swiftlisted 30-day trial | $0 |
| Ship | Pirate Ship, Etsy labels, eBay Labels, ShipSaving Starter, USPS boxes and Label Broker, GoShare quotes | $0 plus postage and insurance per shipment |
| Market | Share & Save, Pinterest business account, Linktree Free, QRCode Monkey, Nextdoor, Yelp, Mercari, Vintage Market Days profile, Buffer Free, Canva Free, Instagram Edits, Kit Free | $0 |
| Messages | Etsy Messages, Cal.com Free, Tally, Espanso, iPhone Text Replacement, Instagram FAQs, Google Voice | $0 |
| Books | Airtable Free, Zoho Books Free, TripLog Basic, Avery, FreeTaxUSA, Flippd free to 20 items | $0 |
| Desktop and video | DaVinci Resolve, Clipchamp, LosslessCut, HandBrake, Subtitle Edit, OBS, Bitwarden Free, LanguageTool, iCloud 5 GB, LocalSend, Wispr Flow Free, Claude in Chrome on the existing plan | $0 |
| **Total** | Platform fees only: Etsy "$0.20 per listing", "6.5%", "3% + 0.25 USD"; eBay "13.6%" plus "$0.30" or "$0.40" per order (verify-14) | **$0 a month** |

### The about-$50 stack

| Line | Price as written | Monthly | Source |
|---|---|---|---|
| Shopify Basic | "Pay yearly $29 USD/mo" | $29.00 | verify-14 |
| Vendoo Starter | "$12.49 Per month, billed yearly" | $12.49 | verify-01 |
| Seller Ledger | "$10 /month", from the first sale | $10.00 | verify-09 |
| iCloud+ 200 GB | "$2.99" "billed monthly" | $2.99 | lane 13 |
| Pushover | "$4.99 USD one-time purchase on each platform" | once | verify-11 |
| **Total** | | **$54.48 a month, plus $4.99 once** | |

The standing decisions do not fit this line. Crosslist Gold "$39.99 per month" in place of Vendoo makes $81.98. Swiftlisted Starter "$6 USD/mo $72 USD billed yearly" in place of Vendoo makes $47.99, with Etsy posted through a Chrome extension on a PC that stays on. Holding Shopify until the storefront takes checkout brings the line to between $25.48 and $52.98, depending on the crosslister.

### The everything stack

Every "pay when it earns it" line switched on at once. Yearly prices are divided by twelve.

| Line | Price as written | Monthly | Source |
|---|---|---|---|
| Shopify Basic | "Pay yearly $29 USD/mo" | 29.00 | verify-14 |
| Crosslist Gold with AI | "$39.99 per month" plus "+$4.99/month" | 44.98 | verify-01 |
| Supabase Pro | $25, repo figure from `docs/dashboard-design.md` section 9, not re-read on 2026-11-07 | 25.00 | prior |
| Seller Ledger | "$10 /month" | 10.00 | verify-09 |
| Flippd Pro | "$9.99/month" | 9.99 | gaps-09 |
| iCloud+ 200 GB | "$2.99" | 2.99 | lane 13 |
| eRank Basic | "$5.99/mo" | 5.99 | verify-02 |
| Etsy Plus | "$10 USD per month" | 10.00 | verify-14 |
| WorthPoint Price Guide | "Price Guide Monthly $26.99", Apple listing | 26.99 | verify-04 |
| Lot-Art Explorer | "$13.90/month" | 13.90 | gaps-04 |
| PicWish Pro | "$4.99 /mo Billed Annually" | 4.99 | gaps-03 |
| eBay Basic Store | "$21.95" on yearly renewal | 21.95 | verify-14 |
| Judge.me Awesome | "$15 per month" | 15.00 | verify-08 |
| Shuttle Growth | "$19 / month" | 19.00 | verify-16 |
| Offerly Pro | "$20 / month" | 20.00 | verify-16 |
| Appointo Pro | "$14 / month" | 14.00 | verify-11 |
| Veed Creator | "$12 per user / month billed yearly" | 12.00 | verify-12 |
| Wispr Flow Pro | "$12/user/mo" | 12.00 | verify-15 |
| Kittl Pro | "$14 /mo, billed annually" | 14.00 | gaps-12 |
| Bensound All Access | "$9 /month (Billed $119 annually)" | 9.00 | gaps-12 |
| Sift Pro | "$6.99 a month" | 6.99 | gaps-06 |
| Wachete Starter | "$ 5.40 / month billed monthly" | 5.40 | gaps-06 |
| Bitwarden Premium | "$1.65 per month" "Billed annually at $19.80" | 1.65 | verify-13 |
| CTBids Premier | "$99/year" | 8.25 | verify-07 |
| Kovels All Access Online | "$59.99 per year" | 5.00 | verify-05 |
| Carrd Pro Standard | "$19 / year" | 1.58 | gaps-11 |
| **Monthly total** | | **$349.65** | |
| One-time: Pushover "$4.99", Munbyn RW403B "$79.99", IPS03 scale "$39.99", NIIMBOT D110 "$20.90" sale, DaVinci Resolve Studio "Now $236" | | **$381.87 once** | verify-11, verify-10, gaps-09, verify-12 |

## Contradictions with earlier decisions

Strongest first.

1. **Crosslist Gold to trial.** The trial is not free: "20 free listings with our 3-day money-back guarantee", "whichever comes first", a card is required, and annual refunds carry "a small $9.99 processing fee" (V, verify-01, verify-13). Autodelisting is Gold and Diamond only, Gold with the AI add-on is $44.98, and five tools cover Etsy, eBay and Shopify with sale detection on the entry plan for less: Secnd "Free $0 CAD/mo" with "automatic delisting" (gaps-01), Swiftlisted "$6 USD/mo $72 USD billed yearly" (gaps-01), FLUF "Starter $9 /month" (verify-01), Vendoo "$12.49 Per month, billed yearly" without Shopify auto-delist (verify-01), Voolist "$19.99 / month Billed monthly" with auto-delist on every plan (verify-01). Softening facts: Gold is "$32.99 per month billed yearly", the extension is maintained (v3.12.7, Nov 6 2026), and `docs/dashboard-design.md` already ruled out Vendoo for the Shopify gap and FLUF for its 90-minute polling. Ricky decides.
2. **Supabase as the one home for inventory and cost basis.** Flippd Pro "$9.99/month" and Inventory Now "$10 BILLED $120 YEARLY" keep cost of goods, fees and net profit per item in their own cloud, with Schedule C reports and marketplace connections (V, gaps-09). Paying either makes a second permanent ledger beside the dashboard; Airtable Free was picked as a stopgap for that reason. Decide one home before paying.
3. **Pushover and Supabase fed from Shopify.** Shopify Flow is free on Basic, but Send HTTP Request needs Grow at "$79" yearly (V, verify-11, verify-14). Flow cannot call Pushover or Supabase from Basic, so alerts from Shopify events need the Shopify API, a webhook of our own, n8n or Activepieces. A build constraint, not a change of tool.
4. **Kit Free for email before Shopify.** Lane 08 could not read Kit's fee page and offered Brevo Free, "up to 300 emails per day", as the pre-Shopify tool (V, gaps-08). Round D already rejected Brevo because 300 a day cannot send a drop alert to a list over 300, and chose Kit Free on 2026-10-29. Kit stands.
5. **Claude Haiku listing drafts.** Not refuted, but partly duplicated: the eBay app writes listings from photos, Shopify Sidekick writes descriptions, and every crosslister bundles a writer, Crosslist at "+$4.99/month" (V, verify-01, verify-02). Etsy has no AI writer, so the Haiku draft keeps its job. Two amendments: a disclosure line whenever a background was replaced, because Etsy asks sellers to note edits (V, lane 03), and no maker or era in a draft without a mark, label or appraiser (verify-05).
6. **rembg BiRefNet.** Two confirmations. The README now makes bria-rmbg "The default" and its licence "requires a paid agreement for commercial use" (V, verify-03); the cutout handoff already pins `-m birefnet-general -dc`. Etsy renders transparent PNG areas black (V, lane 03); the handoff already sends flattened JPEGs to every channel. Refinements from gaps-03: MIT "BiRefNet_HR" weights, and withoutBG "Apache-2.0" as a second engine.
7. **Canva Free.** The lane said background removal was "listed under Pro" at "US$ 144 /year for one person"; verify found no such line, and Canva's feature page says "Remove your photo's background for free" (V, verify-03). Canva Free stands; the free quota is U.
8. **Buffer Free and Instagram Edits.** Buffer Free confirmed: "Connect up to 3 channels", "10 scheduled posts per channel" (V, verify-08); the paid "$5 /month" is "$60 billed yearly" and the monthly price did not render. Nothing touches Instagram Edits.
9. **Fixed Etsy shipping classes.** Supported by "99 custom shipping profiles" on Shopify (verify-16) and Etsy's rejection of furniture for calculated shipping (gaps-14). Three facts to fold in: the USPS "temporary 8% rate increase ... through January 17, 2027", the "$4 fee" for "Cylindrical rolls" (verify-10), and Etsy's search preference for domestic shipping under $6 (verify-14). Re-check the classes in January 2027.
10. **Shopify as hub: no.** Confirmed: Marketplace Connect says "New connections to Etsy can't be made at this time" (V, gaps-14). The free Shopify-to-eBay leg is still worth a test once the store exists, against whatever crosslister Ricky picks.

## What the research could not read

- WorthPoint, worthpoint.com/pricing, 403 on every fetch. Assumed Apple's in-app list: "Price Guide Monthly $26.99", "MARKS Premium Monthly $19.99". Confirm on the web before buying.
- Flyp, flyp.com, 403. Assumed unavailable; a reported "$9/month" with a "100-day free trial" and Etsy support is unverified.
- Mavin, 130point, Replacements.com, 925-1000.com, Barnebys, Heritage, Audiogon, LiveAuctioneers price results (dead URL), Wright past auctions: bot walls or 404s. Assumed free to browse; none relied on.
- Etsy legal and handbook pages: etsy.com/legal/api, creativity standards, the title-guidance article, the shop set-up fee screen, all 403. Assumed no clause bars third-party listing tools, title guidance "less than 15 words", and a one-time set-up fee of unknown amount.
- eBay help pages behind captcha: image specs, International Shipping caps, ShipCover rates, the US Seller Hub "Multiple listings from photos". Image specs rest on the lane's read; EIS caps and ShipCover rates are U; the bulk tool was read on the UK page only.
- Shopify Sidekick help page, 403. Assumed the description writer is on Basic; the marketing page says "BUILT INTO EVERY STORE".
- Make.com and ManyChat pricing, 403. Assumed free tiers exist; prices unknown; neither is in a ladder.
- Poshmark fee policy, Facebook Marketplace fees, TikTok Shop fees, Ruby Lane fees, Whatnot's US tier table, EBTH commission: unread. None of these channels is in the plan.
- Monthly-billing toggles that did not render: Swiftlisted, VendorSnap, EverBee, EHunt, Photoroom, Pixelcut, PicWish, Shippo, CapCut, Veed, Epidemic Sound, Buffer paid per channel, Grammarly, Superwhisper. Yearly figures are used as written; monthly is U.
- Canva free background-remover quota, Google Photos Magic Editor quotas, Text Blaze free snippet count: U.
- CapCut terms of service, 404, 500 and 502. Assumed library music is not cleared for a shop; none used.
- MaxSold, 403. The 18% premium came from its help desk; Lee or Collier activity unknown.
- HiBid and Invaluable alert settings, ShopGoodwill saved-search email, Facebook Marketplace saved-search alerts: unread. Assumed alerts exist and are set by hand.
- Florida DOR registration fee and Collier County receipt fee: no page states them.
- Judge.me Forever Free Etsy sync: the listing says "Sync with Shop App, Etsy, Amazon"; whether it shows Hollie's shop reviews is untested. If not, Reputon "$6.99 / month".
- Secnd's eBay connection, Vendoo's trial card requirement, QuickSync's free-tier eligibility, Phone Link iPhone photo support: U.
- Device facts: Clean Up and Apple Visual Intelligence need a qualifying iPhone; NVIDIA Broadcast needs an RTX 2060 or newer. Ricky checks Settings and dxdiag.

## Questions for Ricky

1. Crosslister. Pay Crosslist Gold "$39.99 per month" up front and test inside 3 days or 20 listings, or run Secnd Free, the Swiftlisted 30-day trial and Vendoo's 14 days first and pay the winner?
2. Ledger home. Airtable Free now and Supabase when the dashboard ships, or Flippd Pro "$9.99/month" as a permanent phone ledger?
3. Shopify timing. Open Basic at "$29 USD/mo" yearly now, or hold it until the storefront takes checkout? This decides the about-$50 line.
4. Offsite Ads. Leave on for 60 days and read attribution, or opt out while under $10,000?
5. Facebook Marketplace alerts. Accept the Meta-terms risk of Sift or Dibs in Hollie's own browser, or keep Marketplace a phone habit?
6. Chairish. List furniture, lighting and art over about $300 there at "30% Flat Commission" from 10 listings, with Chairish-managed shipping, or keep every piece on the three channels?
7. Hardware. Buy Munbyn RW403B "$79.99" and IPS03 "$39.99" now while the sale holds, or use USPS Label Broker until the first sales?
8. Which county is the room in? Lee means 0.5% surtax and a "$50" October to March receipt; Collier means no surtax and an unread fee.

## Sources

All in `research/tools-2026-11-07/`. Digests: `digests/01-listing-crosslisting.md` through `digests/16-shopify-apps-vintage.md`.

- 01: `01-listing-crosslisting.md`, `verify-01-listing-crosslisting.md`, `gaps-01-listing-crosslisting.md`
- 02: `02-ai-writers-and-seo.md`, `verify-02-ai-writers-and-seo.md`, `gaps-02-ai-writers-and-seo.md`
- 03: `03-photos.md`, `verify-03-photos.md`, `gaps-03-photos.md`
- 04: `04-pricing-comps.md`, `verify-04-pricing-comps.md`, `gaps-04-pricing-comps.md`
- 05: `05-identification.md`, `verify-05-identification.md`, `gaps-05-identification.md`
- 06: `06-sourcing-online.md`, `verify-06-sourcing-online.md`, `gaps-06-sourcing-online.md`
- 07: `07-sourcing-local-swfl.md`, `verify-07-sourcing-local-swfl.md`, `gaps-07-sourcing-local-swfl.md`
- 08: `08-marketing-channels.md`, `verify-08-marketing-channels.md`, `gaps-08-marketing-channels.md`
- 09: `09-inventory-books-tax.md`, `verify-09-inventory-books-tax.md`, `gaps-09-inventory-books-tax.md`
- 10: `10-shipping-tools.md`, `verify-10-shipping-tools.md`, `gaps-10-shipping-tools.md`
- 11: `11-customer-service-automation.md`, `verify-11-customer-service-automation.md`, `gaps-11-customer-service-automation.md`
- 12: `12-video-desktop.md`, `verify-12-video-desktop.md`, `gaps-12-video-desktop.md`
- 13: `13-extensions-desktop-utilities.md`, `verify-13-extensions-desktop-utilities.md`, `gaps-13-extensions-desktop-utilities.md`
- 14: `14-platform-native-free.md`, `verify-14-platform-native-free.md`, `gaps-14-platform-native-free.md`
- 15: `15-ai-agents-and-assistants.md`, `verify-15-ai-agents-and-assistants.md`, `gaps-15-ai-agents-and-assistants.md`
- 16: `16-shopify-apps-vintage.md`, `verify-16-shopify-apps-vintage.md`, `gaps-16-shopify-apps-vintage.md`

Prior decisions: `docs/dashboard-design.md` sections 2, 9 and 10; `docs/round-d-synthesis.md`; `docs/social-manual.md` sections 6 and 7; `docs/cutout-catalog-handoff.md` sections 1 and 5.
