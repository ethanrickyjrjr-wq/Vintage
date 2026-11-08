# Holliewood and Vine: tool stack

**Date:** 2026-11-07. **Status:** research synthesis; nothing built or bought.

Sixteen Sonnet lanes ran on 2026-11-07, one per step of the process. Each left three files in `research/tools-2026-11-07/`: a lane report (`NN-name.md`), a verify file (`verify-NN-name.md`) that re-read the lane's picks on the vendor pages the same day and overrides the lane where they disagree, and a gaps file (`gaps-NN-name.md`) for missed, defunct and renamed tools. Sixteen digests in `research/tools-2026-11-07/digests/` fold them together. This page is the decision layer. Prices are quoted as the vendor writes them, with the billing period, and each carries its source file and URL. **V**: an agent read the vendor page on 2026-11-07. **U**: the page would not load or the figure is not in any page text. Where verify refuted a lane figure, the verify figure is used and the correction named. crawl4ai was not reachable from the cloud session, so pages were read with WebFetch; several gaps agents ran after the shared WebSearch budget ran out and worked from direct vendor URLs, so their coverage is thinner. Shorthand: `lane 01` is `01-listing-crosslisting.md`; `verify-01` and `gaps-01` are its verify and gaps files. Full names are under Sources.

Prior decisions inherited: Crosslist Gold to trial (`docs/dashboard-design.md` section 10); rembg pinned to `-m birefnet-general -dc`, flattened JPEGs to every channel (`docs/cutout-catalog-handoff.md`); Buffer Free, Canva Free, Instagram Edits (`docs/social-manual.md` section 7); Claude Haiku listing drafts, Supabase, Pushover (`docs/dashboard-design.md` section 9); Kit Free before Shopify and fixed Etsy shipping classes (`docs/round-d-synthesis.md`). They stand unless the Contradictions section says otherwise.

## Read this first

- The stack in one breath. The Etsy Seller app and the eBay app list. Haiku drafts the Etsy listing in the planned dashboard. rembg cuts out, ImageMagick flattens. Pirate Ship and Etsy labels ship. Airtable Free and Zoho Books Free keep the books. EstateSales.net, Trove and CTBids find stock. Buffer, Canva and Instagram Edits post. Cal.com and Tally book Hire Hollie. A crosslister fans Etsy out to eBay and Shopify.
- The free stack is $0 a month. The only money is platform fees: Etsy "$0.20 per listing", "6.5% of the total order amount", "3% + 0.25 USD"; eBay "13.6%" plus "$0.30" or "$0.40" per order, 250 free listings a month (V, verify-14, which corrected the lane's flat $0.40).
- The paid stack on the standing decisions is Shopify Basic "$29 USD/mo" yearly plus Crosslist Gold "$39.99 per month": $68.99 before anything else, so it does not fit a $50 line. The everything stack is about $330 a month plus about $382 once.
- Time saver 1: eBay Product Research, "free to all sellers", "the last 3 years of eBay sales data" (V, verify-04). No paid comps subscription in year one.
- Time saver 2: Etsy's own auto-replies, quick replies and writing assistant, free, and auto-replies count toward Star Seller (V, verify-11).
- Time saver 3: native alerts. EstateSales.net email, Trove's eBay push "usually within 60 seconds", CTBids bidding with local pickup. Free, and nothing is scraped (V, verify-06, gaps-06, verify-07).
- Contradiction: Crosslist Gold is not a free trial. "20 free listings with our 3-day money-back guarantee", card required, "a small $9.99 processing fee" on annual refunds (V, verify-01, verify-13). Four cheaper tools cover all three channels with sale detection on the entry plan; Vendoo is a fifth whose auto-delist excludes Shopify. Ricky decides.
- Soft contradiction: Flippd and Inventory Now keep the cost ledger in their own cloud while the plan makes Supabase the home. Decide one home before paying.
- rembg's README now makes bria-rmbg "The default", and that licence "requires a paid agreement for commercial use" (V, verify-03). Every call passes `-m birefnet-general -dc`, as the cutout handoff pins. Etsy renders transparent PNG black, so every cutout is flattened. Both already decided, now confirmed on vendor pages.
- remove.bg closes "from 1 December 2026 at 9:00am CET" (V, verify-03). Windows 11 Photos and Paint remove backgrounds locally, free.
- Claude in Chrome is "Available on all paid plans" and Cowork "Works with a paid plan" (V, verify-15, gaps-15). eBay bans "LLM-driven bots" without permission. Browser agent on Etsy only, Ricky watching; eBay through the API.
- Share & Save refunds "6.5% back" through January 4, then "4% off the eligible order total" (V, verify-08). On from day one. Decide Offsite Ads before the first sale.

## Install today

Free only, ordered by payoff.

**Windows PC**

1. Bitwarden Free, every key from day one. $0. lane 13.
2. PowerToys: Image Resizer with a 2048px preset, Text Extractor, Advanced Paste. $0. lane 13.
3. Windows 11 Photos and Paint background removal, built in. $0. verify-03, gaps-03.
4. rembg in a venv, every call `-m birefnet-general -dc` as the cutout handoff pins, plus ImageMagick to flatten. $0, MIT. verify-03.
5. Upscayl. $0. verify-03.
6. Caesium Image Compressor. $0. gaps-03.
7. Affinity by Canva, "free for individuals (seriously)". $0. verify-03.
8. eRank extension with a free account. $0. lane 13.
9. Google Lens in Chrome plus Search by Image. $0. gaps-13.
10. LanguageTool or Harper, one of them. $0. lane 13.
11. Espanso, once ten listings of boilerplate exist. $0. lane 11.
12. iCloud for Windows plus the free HEIF Image Extension. $0 to 5 GB. lane 13, gaps-13.
13. LocalSend. $0. lane 13.
14. Pirate Ship account, "No monthly fees". $0. verify-10.
15. DaVinci Resolve, LosslessCut, HandBrake, Subtitle Edit, OBS Studio. $0. lane 12, gaps-12.
16. changedetection.io on the Fedora box, Pushover through Apprise. $0. lane 06.

**iPhone**

1. Etsy Seller app. "Free". lane 14.
2. eBay app. Free. lane 01.
3. Trove - Smart Alerts for eBay, "Free to use". gaps-06.
4. EstateSales.net app and Estate Sale Finder. Free. lane 06, gaps-06.
5. Snapseed. "Free". verify-03.
6. Microsoft Designer. Free with a Microsoft account. gaps-03.
7. Google app for Lens. Free. lane 05.
8. TripLog Basic, "Free forever". verify-09.
9. ShipSaving, Starter "Free/ month". gaps-10.
10. Text Replacement in Settings for canned replies. Built in. gaps-11.
11. LocalSend and Bitwarden. Free. lane 13.
12. Already decided and still free: Instagram Edits, Buffer, Canva. `docs/social-manual.md` section 7.

## 1. Source

### Online alerts

| Tool | Does | Price | Free tier | Platform | Verdict | Source |
|---|---|---|---|---|---|---|
| Trove - Smart Alerts for eBay | eBay push alerts "usually within 60 seconds" | "Free to use", "No fees. No subscriptions." | "Up to 15 saved searches" | iOS; Android U | Use now | V · gaps-06 · https://apps.apple.com/us/app/trove-smart-alerts-for-ebay/id1536471650 |
| eBay saved searches | Native email alert, no interval stated | Free | Whole feature | Web, app | Use now, slow backstop | V · verify-06 · https://www.ebay.com/help/buying/search-tips/saved-searches?id=4051 |
| EstateSales.net | Daily email by lead day, type, radius; keyword tracker | "Free E-mail notifications" | Whole feature | Web, iOS, Android | Use now; 33901 and 34102, 50 miles | V · verify-06 · https://www.estatesales.net/help/frequently-asked-questions |
| EstateSales.org, gsalr | Second net, 5 to 100 miles, "Online Auction Items"; yard-sale digest | Free; gsalr "Go Ad Free for $4.99" | Whole feature | Web, iOS app | Use now; homepage modal, /subscribe is a 404 | V · verify-06 · https://estatesales.org/ |
| Proxibid, LiveAuctioneers, Invaluable, HiBid | Auction aggregator alerts | Free; Proxibid "default frequency of once a week" | Yes | Web, apps | Use now; set Proxibid daily; HiBid and Invaluable settings U | V · verify-06 · https://discover.proxibid.com/comparison-shopping-hard-help |
| Craigslist search alerts | "automated email when new postings match" | Free | Yes | Web | Use now, fort myers and sarasota sites | V · verify-06 · https://www.craigslist.org/about/help/account/features/searches |
| changedetection.io | Page monitor, Pushover through Apprise | Hosted "$8.99 / Month"; self-hosted free | Apache-2.0 | Fedora box | Use now on estate-sale and auction-house pages only | V · verify-06 · https://github.com/dgtlmoon/changedetection.io |
| Sift; Dibs | Facebook Marketplace searches in Hollie's own browser | Sift Pro "$6.99 a month or $49 a year"; Dibs Pro "$12/month" | Sift "free to use"; Dibs "3 saved searches" | Chrome | Only if Ricky accepts the Meta-terms risk | V · gaps-06 · https://siftmarketplace.com/pricing |
| Botifex, Swoopa, DealHunter, Pacto | Proxy scrapers | Botifex "Basic $19.99/mo"; Swoopa "$47/mo" | Thin | Web | Skip; against Meta and eBay terms | V · gaps-06 · https://botifex.com/pricing |

Decision. Use now: both estate-sale nets, Trove, eBay saved searches, Proxibid and LiveAuctioneers follows, Craigslist alerts, changedetection.io self-hosted. Pay when it earns it: Dealerts or BayWatch in-app purchases when Trove's 15 searches run out, prices read in-app first; Wachete "STARTER $ 5.40 / month billed monthly" if self-hosting is off (gaps-06). Skip every proxy scraper; a ban lands on the selling account. The dashboard's sourcing feed holds alert emails and what Hollie types, never scraped listings; EstateSales.net's terms forbid harvesting (verify-07). IFTTT's Craigslist service is a 404 (verify-06).

### Southwest Florida venues

| Venue | Does | Fee | Free tool | Hours or cadence | Verdict | Source |
|---|---|---|---|---|---|---|
| CTBids, Caring Transitions of Cape Coral | Online estate auctions, local pickup | "Bidding Starts at $1"; Premier "$99/year" | Account, "Real time updates and notifications" | Four live auctions 2026-11-07 | Use now; Premier later | V · verify-07 · https://ctbids.com/estate-sales/Cape-Coral-FL |
| Gulf Coast Auction House on HiBid, Bonita Springs | Estates, decor, vintage | "18% Buyer's Premium \| 3% Discount for Cash Payments" | Watch list, email list | Preview Fri 10 to 6, Sat 12 to 3 | Use now; budget premium plus tax | V · verify-07 · https://gulfcoastauctionhouse.hibid.com/ |
| KCM Galleries, Cape Coral | Framed-art auctions "Every Sunday and Wednesday" | Premium per auction; the lane's "no buyer's premium" was a listing title, refuted | Register free | Twice weekly | Use now; read each auction's terms | V · verify-07 · https://www.kcmgalleries.com/buy-art/how-to-bid/ |
| Goodwill SWFL, ShopGoodwill | Thrift chain; online auctions with Tice St pickup | VIP Perks free, "5% back" | "Saved Searches" online | Sunday "50% discount on most color-tagged items"; "$1.99 the following Sunday & Monday" | Use now | V · verify-07 · https://goodwillswfl.org/shop/ |
| Habitat ReStores; Hope Chest | Lamps, chairs, decor; upscale resale, four stores | n/a | Rewards app; Collier inventory email; newsletter | ReStore "Monday-Saturday \| 10am - 5pm"; Hope Chest Mon to Fri 9 to 5, Sat 9 to 4 | Use now; McGregor ReStore "PERMANENTLY CLOSED" | V · verify-07 · https://www.habitat4humanity.org/locations/ |
| Fleamasters; Flamingo Island; Ortiz | Flea markets | Entry fee not stated | None | "Friday - Sunday: 9am-5pm"; "Fri, Sat & Sun 8am-4pm"; Ortiz "Saturday 8AM-4PM Sunday 6AM-4PM" (verify corrected the lane) | Use now; Ortiz Sunday 6 AM | V · verify-07 · https://www.ortizfleamarket.com/ |
| Allegro, Can't Take It With You, Dovetails, Sharon Hardison, Freedom Auction Company | Estate-sale companies, Sarasota to Punta Gorda; Freedom's "MID-CENTURY MODERN DESIGN DECEMBER 11TH, 2026" | Premiums per platform | Text or email lists | By sale | Use now; join every list | V · gaps-07 · https://linktr.ee/allegroestatesalesfl |
| StorageTreasures; Lockerfox; MaxSold | Storage auctions; downsizing auctions | StorageTreasures "ProBidder $10.00 / Month"; Lockerfox "15% of the winning bid subject to a $10.00 minimum"; MaxSold "the buyer's premium is 18%" | StorageTreasures "$0.00 / Month" | Naples "Total Auctions: 21" | StorageTreasures as a gamble; skip Lockerfox; MaxSold SWFL activity U | V · verify-07, gaps-07 · https://www.storagetreasures.com/pro-membership-upgrade |

Decision. Whole-house contents come through CTBids and HiBid with local pickup; floor stock from Goodwill color tags on Sunday, the ReStores and Hope Chest. Early November was thin in Collier; re-check in January (verify-07). CTBids Premier "$99/year" only when she wins several lots a month; its WorthPoint benefit is a "90 Day All-Access Subscription", not a year (verify-06). Skip Lockerfox and storage units as a routine, EBTH with its Ohio pickup, and AuctionNinja with no SWFL sellers (lane 07).

## 2. Identify

| Tool | Does | Price | Free tier | Platform | Verdict | Source |
|---|---|---|---|---|---|---|
| Google Lens; Bing Visual Search | Reverse image search | Free | Whole | iPhone, Chrome, PC | Use now; first guess | V · verify-05 · https://search.google/ways-to-search/lens/ |
| Claude, Gemini, Copilot free tiers | Photo to hypotheses | Claude Free "$0"; Gemini "$0/ month" | Yes | Web, phone | Vocabulary only; never cite as attribution | V · verify-05 · https://claude.com/pricing |
| Kovels guides; Kovels All Access | Marks articles; paid price guide and marks dictionary | "Kovels All Access Online $59.99 per year" (verify corrected the lane's "not found"; lane 04's $24.95 was Antique Trader) | Guide pages, newsletter | Web | Free pages now; pay when it earns it | V · verify-05 · https://www.kovels.com/subscriptions/ |
| Marks folder: thepotteries.org, porcelainmarksandmore.com, silvercollection.it, 20thcenturyglass.com, The Marks Project; VFG Label Resource; FTC RN | Pottery, porcelain, silver, glass, studio ceramics; clothing labels and RN numbers | Free | Whole | Web | Use now | V · verify-05, gaps-05 · https://rn.ftc.gov/ |
| Antiquers.com; Collectors Weekly | Human ID forums | Free | Yes | Web | Use now for the pieces nothing else names | V · gaps-05 · https://www.antiquers.com/ |
| Appraisily; Mearto; ValueMyStuff | Free ID and paid value; specialist appraisals | "Unlock a working value ... for $9."; Mearto "1 Appraisal $25"; ValueMyStuff "1 credit $ 28" | Appraisily ID free | Web | Per piece, when the price depends on the maker | V · gaps-05 · https://appraisily.com/ |
| FindArtInfo; Art Signature Dictionary | Signature databases | "$4.95 for 24 hours or $17.95 a month"; ASD "7 days free, then $12/month" | FindArtInfo account | Web | Free account; $4.95 day pass for all signed pieces at once | V · gaps-05 · https://findartinfo.com/pricing |
| WorthPoint MARKS Premium | "more than 150,000 makers' marks" | Apple: "MARKS Premium Monthly $19.99"; web 403 | Trial only | Web, iOS (2.1 rating) | Pay when it earns it, web price confirmed first | V Apple, U web · verify-05 · https://apps.apple.com/us/app/worthpoint/id1472512649 |
| PSA/DNA | Autograph authentication | "2 Signatures" "$20" to "$500"; Premium Letter "an additional $15"; Original Photograph "$999 or less $50" | None | Mail-in | The Elvis photo: two signatures, so the 2 Signatures column | V · verify-05 · https://www.psacard.com/pricing/autographs |
| AI identifier apps: Antiquer, Antiqly, ThriftCheck | AI photo ID | "$4.99" to "$9.99 per week"; Antiqly "$39.99 per year", no trial | Antiquer "2 identifications per day" | iOS, Chrome | Skip; Lens is free and faster | V · verify-05, gaps-05 · https://apps.apple.com/us/app/antique-identifier-antiquer/id6764046845 |

Decision. Lens plus the marks folder is the whole identification stack for $0. A Haiku draft never asserts a maker or era that no mark, label or appraiser confirmed; Anthropic's page says Claude "can occasionally produce responses that are incorrect or misleading" (verify-05). Pay per piece only: Appraisily $9, Mearto $25, FindArtInfo $4.95, PSA/DNA for the Elvis photo with a JSA Florida phone quote as the check (lane 05). TinEye is "free for non-commercial use" only; skip (lane 13).

## 3. Price

| Tool | Does | Price | Free tier | Platform | Verdict | Source |
|---|---|---|---|---|---|---|
| eBay Product Research | Sold prices, sell-through, "the last 3 years of eBay sales data" | "free to all sellers" | Full | Seller Hub, app | Use now; the backbone | V · verify-04 · https://www.ebay.com/help/selling/selling-tools/terapeak-research?id=4853 |
| Poshmark Sold; Mercari sold | Sold prices, small decor and fashion | Free; Poshmark needs no login | Yes | Web, apps | Use now; Mercari 403, confirm in app | V, Mercari U · verify-04 · https://poshmark.com/search?query=stiffel%20lamp&availability=sold_out |
| Chairish; 1stDibs | Asking prices, "Hide Sold Out" filter | Free | Yes | Web | Ceilings and listing language | V · verify-04 · https://www.chairish.com/maker/stiffel |
| EBTH archive; Invaluable | Realized estate and auction prices | Free account, card required; Invaluable free "up to 12 months of past auction prices" (verify refuted "limits unknown") | Yes | Web, apps | Use now; sign up before paying anyone | V · verify-04 · https://www.invaluable.com/inv/help/faq/search-price-archive/ |
| Artsy Price Database; Bidsquare; HiBid closed | Fine-art results "for free", "no search limits"; Florida houses' past catalogs | Free | Yes | Web | Use now; hammer visibility logged out U | V · gaps-04 · https://www.artsy.net/price-database |
| Lot-Art Price Database | "75M+" results from "5,000+" houses since 2016 | "Day Pass $9.90 one-time"; "Explorer $13.90/month", "billed monthly" | Basic search | Web | Day Pass the first time a piece looks worth over about $300 | V · gaps-04 · https://www.lot-art.com/user-guide |
| WorthPoint Price Guide | eBay and auction sold prices, "nearly 2 decades" | Apple: "Price Guide Monthly $26.99", "Annual $249.99"; web 403 | Locked | Web, iOS | One month when a backlog is older than eBay's 3 years; cancel | V Apple, U web · verify-04 · https://apps.apple.com/us/app/worthpoint/id1472512649 |
| Artnet Price Database | "items estimated at $500 and above" | Decorative Art "$34 /30 days*" | None | Web | Only for a $500-plus signed piece | V · verify-04 · https://www.artnet.com/price-database/ |
| WatchCount | eBay sold search | Price "unknown"; search works | Free web | Web | By hand only; terms ban AI access | V · gaps-04 · https://www.watchcount.com/ |

Decision. Etsy exposes no sold prices, and the Etsy estimators in section 5 sell keyword data, not sales, so pricing runs on eBay Product Research, EBTH, Invaluable's free 12 months, Chairish for the ceiling and Google Shopping for the new-equivalent ceiling. Pay per need: Lot-Art Day Pass $9.90, WorthPoint $26.99 for one month, Artnet only for a $500-plus signed piece. The dashboard cannot scrape eBay or WatchCount; the only sanctioned feed is the Marketplace Insights API, docs behind a developer sign-in (U, gaps-04), so the comps panel stays live links, as `docs/dashboard-design.md` section 10 says. Dead: Algopix, Checkaflip, Prices4Antiques, ShelfTrend; EtsyHunt is now EHunt (gaps-04).

## 4. Shoot and edit photos

| Tool | Does | Price | Free tier | Platform | Verdict | Source |
|---|---|---|---|---|---|---|
| Windows 11 Photos; Paint | Remove or replace background, Generative Erase; Paint "Background Removal" | Built in | "done locally on your device" | Windows 11 | Use now | V · verify-03, gaps-03 · https://support.microsoft.com/en-us/windows/apps/photos/edit-photos-and-videos-in-windows |
| Snapseed; Apple Photos lift subject and Clean Up; Microsoft Designer | Phone retouch, cutouts for social, erasers | Free; Designer "free with a Microsoft account" | Snapseed "no subscriptions, purchases, ads, or watermarks"; Clean Up needs "iPhone 15 Pro, iPhone 15 Pro Max, or iPhone 16 model or later" | iPhone | Use now; Apple lift has no save-as-PNG, so not listing grade | V · verify-03, gaps-03 · https://apps.apple.com/us/app/snapseed-photo-editor-camera/id439438619 |
| rembg (BiRefNet) | Local cutout CLI and server | Free, "MIT license" | Everything | Windows Python, Docker | Decided; always `-m birefnet-general`; "bria-rmbg ... The default" needs "a paid agreement for commercial use" | V · verify-03 · https://github.com/danielgatis/rembg |
| withoutBG | Open-weights cutout model, web demo | Model "Apache-2.0"; API "100 credits 100 €10" | Local unlimited; web "5 free images a day" | Python, Docker, web | Second local engine | V · gaps-03 · https://withoutbg.com/ |
| Upscayl; PowerToys Image Resizer; Caesium; Squoosh; ImageMagick | Upscale to 2000px; bulk resize; batch compress; flatten PNG onto white | Free, open source | Everything | Windows, web | Use now; add the 2000px and 1600px presets by hand | V · verify-03, gaps-03 · https://upscayl.org/ |
| Affinity by Canva | Full photo and vector editor | "free for individuals (seriously)" | All but "Access to Affinity with AI" | Windows, Mac, iPad | Use now for real retouching | V · verify-03 · https://www.affinity.studio/ |
| Canva | Background Remover, Magic Resize; absorbs remove.bg in December | Free "US$ 0 /year for one person"; Pro "US$ 144 /year for one person" | "Remove your photo's background for free"; quota U; verify refuted the lane's "listed under Pro" | Web, Windows, iOS | Canva Free stands | V price, U quota · verify-03 · https://www.canva.com/features/background-remover/ |
| PicWish; Pixelcut; Photoroom | Phone cutouts, white backgrounds, batch | PicWish "Pro $4.99 /mo Billed Annually"; Pixelcut "Pro $10 $8 per month, billed yearly"; Photoroom "Pro (yearly) 89.99 USD" (JSON-LD) | Limited | iOS, Android, web | PicWish at 20 or more listings a month, commercial terms read first; the others only if its edges fail | V · gaps-03, verify-03 · https://picwish.com/pricing |
| Pixian.AI; Path | Pay-per-image cutouts; hand-drawn clipping paths | Pixian "250 $5.00" credits; Path "Clipping path FROM $0.39 PER IMAGE" | Pixian 0.25 MP web; Path "2 free edits" | Web | Per hero shot for crystal and chandeliers | V · gaps-03, lane 03 · https://pixian.ai/pricing |
| remove.bg; Topaz; Gigapixel; Luminar | Cutouts; paid upscalers | remove.bg closes "from 1 December 2026 at 9:00am CET"; Topaz "$199/yr"; Gigapixel "$149/yr"; Luminar "$99.00" with "*365 days access to AI tools" | n/a | n/a | Skip | V · verify-03, lane 03 · https://www.topazlabs.com/pricing |

Decision. Pipeline, all free: shoot; rembg with `-m birefnet-general`, withoutBG as second engine; ImageMagick flattens every PNG; PowerToys resizes to 2000px for Etsy and 1600px for eBay; Caesium brings the folder under 1 MB. Etsy's rules, V on lane 03: "transparent .png files are not supported ... will appear black"; "at least one unedited photo of the actual item against a real background"; 2000 pixels or more; over 1 MB "may not finish uploading"; note edits in the description, so the Haiku template carries a disclosure line whenever a background was replaced. Glass is not cut, as the cutout handoff says; Pixian or Path per hero shot. Skip every paid upscaler.

## 5. Write the listing

| Tool | Does | Price | Free tier | Platform | Verdict | Source |
|---|---|---|---|---|---|---|
| Etsy Marketplace Insights, Stats, Search Visibility | Real keyword volume; terms that brought shoppers; "title recommendations" | "up to 15 keyword searches per week for free"; Etsy Plus "$10 USD per month" for unlimited | 15 a week | Etsy web | Use now | V · verify-02 · https://help.etsy.com/hc/en-us/articles/35122361353239 |
| eRank | Keywords, tag audits, AI Listing Helper | Free "$0/mo"; Basic "$5.99/mo"; Pro "$9.99/mo" | "5 keyword lookups/day ... 1 AI Listing Helper use/day" | Web, Chrome | Use now; Basic when 5 a day runs out | V · verify-02 · https://erank.com/plans |
| EHunt (was EtsyHunt); Alura; Koalanda | Keyword search; AI optimization; unlimited searches | EHunt Basic "$7.99 /month $95.88 billed"; Alura Basic "$11.99/mo" monthly, "$7.99/mo" yearly; Koalanda "$5.99 / month Billed every year as $71.88 USD" | EHunt "Keyword search 5 times/day"; Alura "5 daily keyword & product searches"; Koalanda "Limited searches" | Web | Free tiers as second opinions; Koalanda yearly is the cheapest unlimited data | V annual, U monthly · gaps-02, verify-02 · https://ehunt.ai/pricing |
| eBay Product research; 3Dsellers eBay Title Builder; Keyword Tool Dominator | Sold-title vocabulary; title builder with live eBay scores; eBay autocomplete | Free; free; "$9 USD One payment · 30 Days access" | Yes; yes; "2 searches per day" | Web | First two for every eBay title; KTD $9 once per batch | V · verify-02, gaps-02 · https://www.3dsellers.com/free-tools/ebay-title-builder |
| Free chatbots: ChatGPT, Claude, Gemini, Copilot | Title, 13 tags, description from a prompt and photo | Free; Claude Pro "$17 Per month with annual subscription discount ... $20 if billed monthly" | Yes | Web, phone, Windows | The stopgap, one saved prompt | V · verify-02 · https://claude.com/pricing |
| Claude Haiku 5.5 API | The dashboard's drafting engine | "$0.10 / MTok for prompts up to 100,000 tokens", then "$0.50 / MTok" | n/a | API | Decided; when the dashboard ships | V · verify-02 · https://platform.claude.com/docs/en/about-claude/pricing |
| eBay app AI; Shopify Sidekick | Photo to listing; description writer | Free in listing; Sidekick included, "availability can vary by plan, device, and language" | Yes | eBay app; Shopify | Free second opinion; review every line | V · verify-01, verify-02 · https://help.shopify.com/en/manual/ai-powered-tools |
| Crosslist AI add-on; Lysterly; Vela | Purpose-built writers | "+$4.99/month", "1000 AI credits per month" on Gold; Lysterly "$19.99/mo ... Up to 30 Monthly Generations"; Vela "$29.95 / Per shop Per month" | None | Web | Only if chatbot drafts keep needing rewrites before the dashboard; skip Vela | V · verify-02, gaps-02 · https://crosslist.com/pricing |
| Marmalead; Sale Samurai; EverBee | Etsy analytics | "$19 USD paid monthly"; "$19.99 Monthly"; EverBee Growth "$24.99 per month, billed annually at $299", monthly U | None; none; "10 keywords" | Web | Skip | V · verify-02 · https://marmalead.com/pricing/ |
| SEOWILL (was SEOAnt) | Shopify SEO audits, AI content | "Pro Plan $29.99 / month or $287.90/year" | "30 credits", "20 pages" | Shopify app | Free tier once the store exists | V · gaps-02 · https://apps.shopify.com/seo-master |

Decision. Keywords from first-party data first: Marketplace Insights, Etsy Stats, eBay Product research; eRank Free and EHunt Free add volume. Drafts from one free chatbot with a saved prompt until the Haiku dashboard ships: title under 15 words, item first, 13 tags of 20 characters or fewer, measurements and condition, the edit-disclosure line, no maker claim without a mark. Haiku is the controlled path; the native writers are free but uncontrolled, and the Crosslist add-on would duplicate it. Pay when it earns it: eRank Basic "$5.99/mo" or Koalanda yearly; Etsy Plus "$10 USD per month" when 15 searches a week binds. Reeva is dropped: reeva.ai is an industrial engineering company and no reseller product exists at any domain (lane 01, gaps-01, gaps-02). Nifty lives at nifty.ai, not nifty.app, and has no Shopify (verify-01).

## 6. List and crosslist

| Tool | Does | Price | Free tier | Platform | Verdict | Source |
|---|---|---|---|---|---|---|
| Etsy built-in | Seller app listing; bulk edit; "you can copy listings" | Free | Yes | Web, iOS, Android | Use now | V · verify-01 · https://help.etsy.com/hc/en-us/articles/360000337307 |
| eBay built-in | App AI listing; Seller Hub "Multiple listings from photos" | Free | Yes | App; Seller Hub | Use now; UK page only read, confirm in a US account | V UK · verify-01 · https://www.ebay.co.uk/sellercentre/news/2025-january/ai-bulk-listings |
| Crosslist (standing decision) | 11+ marketplaces incl. all three; "API-first"; autodelist Gold and Diamond only | "Gold $39.99 per month"; yearly "$32.99 per month billed yearly"; AI "+$4.99/month"; Diamond "$44.99 per month" | None; "20 free listings with our 3-day money-back guarantee", card required, annual refunds "a small $9.99 processing fee" | Web, apps, extension (v3.12.7, Nov 6 2026) | Trial means $39.99 up front, tested inside 3 days or 20 listings | V · verify-01, verify-13 · https://crosslist.com/pricing |
| Secnd | eBay, Etsy, Shopify, Depop; "Inventory sync + automatic delisting" | "Free $0 CAD/mo Free forever"; "Starter $29 CAD/mo Billed monthly" | "Unlimited cross-posting", "AI listings, 5 / month" | Web, iPhone (17 ratings) | Use now on two cheap items; confirm eBay connects | V · gaps-01 · https://www.secnd.ca/pricing |
| Swiftlisted | eBay and Shopify by API; Etsy via Chrome extension on a PC that stays on | "Starter $6 USD/mo $72 USD billed yearly"; monthly U | "Free trial $0 for 30 days ... No credit card" | Web, Chrome, iPhone (0 ratings) | 30-day trial against Secnd | V yearly · gaps-01 · https://www.swiftlisted.ai/pricing |
| VendorSnap | Phone lister, eBay and Etsy by API; no Shopify | Pro "$6.67/month Billed yearly at $79.99" | Free plan; "7-day free trial" | iPhone, Android (48 ratings) | Use free for phone listing | V yearly · gaps-01 · https://vendorsnap.app/ |
| Vendoo | 11 marketplaces incl. all three; sale detection on Starter | "STARTER $12.49 Per month, billed yearly"; "$14.99 Per month, billed monthly" (verify: on the page) | "Try Vendoo Free for 14 Days"; card U | Web, iOS, Android | First paid trial; auto-delist excludes Shopify | V · verify-01 · https://www.vendoo.co/pricing |
| FLUF; Voolist | "70+ marketplaces", "Sales checked every 90 min"; auto-delist on every plan | FLUF "Starter $9 /month"; Voolist "Starter $19.99 / month Billed monthly" | FLUF "Start 7 days for $1"; Voolist money-back | Web | Pay when it earns it if Vendoo disappoints or Shopify auto-delist matters | V · verify-01 · https://www.voolist.com/pricing |
| Closo; PrimeLister; List Perfectly; Nifty; SellerAider; OneShop; Posh Sidekick | Other crosslisters | Closo "Free $0 forever", no Etsy; PrimeLister "$49.99 Per Month" (verify filled the lane's "unknown"); List Perfectly "Simple $29 Monthly", Auto Delist "Pro Plus $99+"; Nifty "Crosslisting Plus ($35.99/month)" | Various | Web | Skip: no Etsy, dearest, or auto-delist at $99 | V · verify-01 · https://www.primelister.com/pricing/cross-listing |
| 3Dsellers hosted MCP | eBay, Etsy, Shopify writes from a chat, "no eBay developer account" | "Essential $19 $16 /Mo Billed Annually", 100 Listings | "7 Days Free" | Web, remote MCP | Fallback only; Etsy and Shopify on Essential U | V · gaps-15 · https://www.3dsellers.com/pricing |
| Shopify stock sync: QuickSync, Shuttle, shopUpz, Sellbrite, Trunk | Etsy to Shopify stock and order sync once the store exists | Shuttle "Growth $19 / month" real-time; shopUpz "UNLIMITED $18 / month"; Sellbrite "Pro 100 $19 / month"; Trunk "From $35/month" | QuickSync "Free: $0, 100-variant stock sync for eligible shops"; Shuttle "10 product transfers per month"; Sellbrite "Up to 30 Orders Monthly 2-hr Inventory Quantity Sync" | Shopify apps | Free tiers at launch; pay after a missed sale | V · gaps-01, verify-16 · https://apps.shopify.com/shuttle-transfer-from-etsy |
| Shopify Marketplace Connect | Shopify to eBay, Amazon, Walmart; "New connections to Etsy can't be made at this time" | "Free to install"; "First 50 marketplace-synced orders/mo free, 1% fee per additional synced-order, capped at $99/month" | 50 orders | Shopify app | A free eBay leg later, not an Etsy replacement | V · gaps-14 · https://apps.shopify.com/marketplace-connect |
| API routes: Etsy Open API v3 Seller App; eBay official MCP; YosefHayim/ebay-mcp; aserper/etsy-mcp | Sanctioned automation after Step 0 keys | Etsy "Approval Automated, near-instant", no fee stated; eBay MCP "Only GET requests are supported"; community MCPs MIT | Yes | Claude Code | Etsy key is Step 0; eBay MCP for comps; etsy-mcp dormant since Apr 2, 2026 | V · verify-15, gaps-15 · https://github.com/eBay/npm-public-api-mcp |

Decision. Listing stays Etsy-first from the phone, as Phase 1 says. Until Ricky picks the crosslister, the free tests cost nothing and measure the one thing that matters, sale-to-delist latency on a quantity-1 item: Secnd Free and the Swiftlisted trial on the same two cheap items, VendorSnap for phone listing. The standing decision is Crosslist Gold; the research argues against paying first, and that goes to Ricky under Contradictions. eBay bans "any robot, spider, scraper ... or other automated means" without permission (verify-01), so prefer API posting; Crosslist says "API-first", but no file confirms how it reaches eBay (verify-11). Facebook Marketplace is always extension-driven; keep it manual. Zipsale is "made to be used in the UK"; inkFrog redirects to Wix (verify-01).

## 7. Ship

| Tool | Does | Price | Free tier | Platform | Verdict | Source |
|---|---|---|---|---|---|---|
| Pirate Ship with InsureShield | USPS and UPS labels; imports Etsy, eBay, Shopify orders | "No monthly fees"; InsureShield "$1.00 for every $100 of declared value" | All free, "No credit card required" | Web | Primary; InsureShield on non-Etsy items over $100 | V · verify-10 · https://www.pirateship.com/integrations/etsy |
| Etsy labels with Shipsurance | Labels in the order; "helps you qualify for Etsy Purchase Protection" | "no additional membership fees"; Shipsurance "$0.80 per $100 of order value" domestic | Pay postage | Web, Seller app | Every Etsy order; insure over $250 | V · verify-10 · https://help.etsy.com/hc/en-us/articles/360001988847-Insurance-and-Claims-for-Shipping-Labels |
| eBay Labels; eBay International Shipping; ShipCover | USPS, FedEx, UPS labels; eBay handles the international leg | "no subscription fees"; EIS "no extra charge"; ShipCover rates did not render | Pay postage | Seller Hub, app | Every eBay order; EIS on; skip ShipCover until readable | V, ShipCover U · verify-10, verify-14 · https://www.ebay.com/sellercenter/shipping/ebay-international-shipping |
| ShipSaving | USPS, UPS, FedEx, DHL labels; iPhone app | Starter "Free/ month"; Pro "$15/ month(starting at)" | "Up to 50 labels/month" | Web, iOS | FedEx and DHL backup | V · gaps-10 · https://www.shipsaving.com/en/pricing |
| ShipSaver (Shipsurance) | Pay-as-you-go insurance on any label | USPS "$0.65" to $50 then "$1.00" per $100; UPS and FedEx "$0.75" per $100 | "No monthly fees (pay-as-you-go)" | Web | eBay and Shopify orders over $100 | V · gaps-10 · https://www.shipsaver.com/insurance-calculator/ |
| USPS free boxes; Label Broker; Addresses 3.0 | Free Priority Mail boxes; QR label at the counter; free address API | "Priority Mail® Shoe Box $0.00"; APIs "free of charge" | Free | Post Office, API | Label Broker until the printer arrives; Addresses 3.0 replaces Smarty in the dashboard | V · verify-10, gaps-10 · https://developers.usps.com/addressesv3 |
| Munbyn RW403B; IPS03 scale | 4x6 thermal printer; 440 lb scale | "$79.99" against struck "$159.99"; "$39.99" against "$49.99" | n/a | USB, Bluetooth; phone U | Buy once while the sale holds | V · verify-10 · https://munbyn.com/search?q=RW403B |
| GoShare; Roadie; Lugg | Local truck or van | No published prices; Lugg has no Lee or Collier service | n/a | Apps | GoShare now, Fort Myers, Cape Coral, Naples listed; Lugg out | V · verify-10, gaps-10 · https://goshare.co/florida/ |
| Shopify Shipping on Basic | Labels in admin, "Up to 87% off" | Basic "$29 USD/mo" yearly; the "$200 USD of shipping insurance" needs Grow "$79" plus Shopify Payments | 3-day trial | Shopify | Included at launch; no Grow for the insurance | V · verify-10 · https://www.shopify.com/pricing |
| The UPS Store Pack & Ship; TSI; Freightquote; Chairish-Managed Shipping | Guaranteed packing; furniture freight; LTL quotes; Chairish arranges, buyer pays "start at $11" or "start at $149" In-Home | Store prices "may vary"; quotes only | Free quotes | In store, web | Per high-value piece, quoted before listing; Chairish shipping is a channel decision | V, prices U · verify-10, gaps-10, lane 10 · https://www.tsishipping.com/shipping |
| Shippo; ShipStation; Stamps.com; Veeqo; XPS Ship | Multi-carrier tools | Shippo Pro "$17/mo" annual only; ShipStation Starter "$14.99 /month"; Stamps.com Basic "$14.99 /month", "Print up to 10 shipping labels" | Shippo 30 labels; Veeqo free, no Etsy | Web | Skip; ShipSaving beats them free | V · verify-10, gaps-10 · https://goshippo.com/pricing |

Decision. Pirate Ship primary, Etsy labels for Etsy orders because they feed Star Seller and Purchase Protection, eBay Labels for eBay. Insurance by channel: Shipsurance inside Etsy, ShipSaver for eBay and Shopify, InsureShield only where ShipSaver is dearer. Buy the Munbyn printer and scale once; Label Broker until then. Large pieces: GoShare locally, TSI or Freightquote out of state, quoted before listing. Fixed Etsy shipping classes stand with two January tasks: Etsy's USPS page names "a temporary 8% rate increase ... expected to last through January 17, 2027" and "an additional $4 fee" for "Cylindrical rolls" (verify-10), so rolled prints get their own class. Etsy favors domestic shipping under $6 in search (verify-14): the smallest class sits under $6 or free.

## 8. Market and extra channels

| Tool | Does | Price | Free tier | Platform | Verdict | Source |
|---|---|---|---|---|---|---|
| Etsy Share & Save | Fee refund on sales from Hollie's own link | "instant refund of 4% off the eligible order total"; "From October 20 to January 4 ... 6.5% back" | Free, opt-in | Etsy | Use now; Messages and description links do not count | V · verify-08 · https://help.etsy.com/hc/en-us/articles/16981332744087 |
| Etsy Offsite Ads; Etsy Ads | Fee on attributed sales; pay-per-click | Offsite "15% fee", "will never exceed $100 USD", opt-out under $10,000; Ads "maximum daily budget of $25", "15 day waiting period" | No upfront cost | Etsy | Decide Offsite before the first sale; Ads only as $1 to $3 a day tests | V · verify-08, verify-14 · https://help.etsy.com/hc/articles/360000338367 |
| eBay Promoted Listings General | Paid on sale after a click | "ad rate between 2% - 100%"; needs Above Standard | None | eBay | Fixed 3% to 5% on slow pieces; skip Promoted Offsite | V · verify-14 · https://www.ebay.com/help/selling/ebay-advertising/promoted-listings/general-campaign-strategy?id=4164 |
| Email: Shopify Messaging; Kit Free (prior); Brevo; Klaviyo, Omnisend, Mailchimp | Campaigns | Shopify "first 10,000 emails each month are free", then "$1/1000"; Brevo "up to 300 emails per day"; Klaviyo "$20 /month"; Omnisend $16/mo list (verify: "$11.20/mo" needs 3 months upfront); Mailchimp Essentials "$13 /month" | The last three stop at 250 contacts | Web, Shopify | Kit Free stands from Round D (lane 08 could not read Kit); Shopify Messaging at launch; skip the rest | V · verify-08, gaps-08 · https://apps.shopify.com/shopify-messaging |
| Shopify channels: Shop, Google & YouTube, Microsoft Channel, Pinterest, Facebook & Instagram, Judge.me | Free listings and reviews | "Free to install"; Judge.me "Free $0 per month", "Awesome $15 per month" | Yes | Shopify | At launch; Meta "is no longer a marketplace tax facilitator", set tax first | V · verify-08, gaps-08 · https://judge.me/pricing |
| Linktree; QRCode Monkey | Link page; static QR for the disco-ball tag | Linktree Starter "$7 Billed annually, or $9 monthly"; QR "100% free ... all commercial purposes" | Linktree Free | Web | Free now | V · verify-08 · https://www.qrcode-monkey.com/ |
| Chairish | Curated marketplace, arranges shipping, pays via PayPal | "1 - 9 active listings ... 40% Flat Commission"; "10+ active listings ... 30% Flat Commission"; Premium "$49 / Month" | Free to list | Web, iPhone app | Furniture, lighting, art over about $300 once 10 can be live | V · verify-08 · https://www.chairish.com/pages/consign-with-us |
| Mercari; Whatnot; Palmstreet | General marketplace; live selling | Mercari "10% of the item price + buyer-paid shipping"; Whatnot "≤8%" plus "2.9% on total order value + $0.30"; Palmstreet "Selling Fee: 6.9%" plus "2.9% + $0.3" | Free to list | Apps | Mercari now under $200; one live show at 20 to 40 small pieces | V · verify-08, gaps-08 · https://www.mercari.com/us/help_center/article/169/ |
| Local: Craigslist by-dealer; Nextdoor; Yelp; Google Business Profile; Vintage Market Days | Pickup posts; free pages; "January 29 - 31, 2027 Lee Civic Center" | Craigslist "$5" per post; booth fee behind the vendor login | Free pages and profile | Web | Free pages now; GBP for Hire Hollie only; VMD profile now | V, fee U · gaps-08 · https://www.vintagemarketdays.com/market/south-gulf-coast-florida/ |
| Buffer Free (prior) | Scheduler | Paid "$5 /month" is "$60 billed yearly", monthly U | "Connect up to 3 channels", "10 scheduled posts per channel" | Web, apps | Stands | V · verify-08 · https://buffer.com/pricing |

Decision. Share & Save in every bio, pin and email from day one. Offsite Ads is Ricky's call before the first sale. Pinterest business account today; Shopify channels at launch in this order: Shop, Google & YouTube, Pinterest, Microsoft, Meta after tax, Judge.me Free. Round D's correction holds: pre-owned products are not allowed as Product Pins, so pins are plain or Article Pins. Chairish is the furniture route at 30% from 10 listings. Pay when it earns it: an Etsy Ads two-week test kept only at 5x spend; eBay Promoted General once Above Standard; Judge.me Awesome "$15 per month" for Google Shopping stars; Chairish Premium "$49 / Month" above $1,000 a month there. Skip Klaviyo, Omnisend, Mailchimp. Linkpop is gone (gaps-08). Facebook Marketplace stays manual; its fee pages would not load (U).

## 9. Messages and bookings

| Tool | Does | Price | Free tier | Platform | Verdict | Source |
|---|---|---|---|---|---|---|
| Etsy Messages | Auto-replies "from an hour to a maximum of five days", weekly auto-replies, quick replies, US writing assistant; count toward Star Seller | Included | Yes | Etsy.com; app for quick replies | Use now | V · verify-11 · https://help.etsy.com/hc/en-us/articles/115015654988-How-to-Send-Messages-to-Buyers |
| Shopify Inbox, Flow, Email, pickup | Chat; automations; email; pickup | "Pricing Free"; Flow "free app available on the Basic, Grow, Advanced, and Plus plans"; Send HTTP Request needs Grow | With a plan | Shopify | At launch; Flow on Basic cannot call Pushover or Supabase | V · verify-11 · https://help.shopify.com/en/manual/shopify-flow |
| Cal.com | Booking page with payments | Teams "$12per user/month" yearly | "Free forever": "1 user", "Accept Stripe & PayPal payments", "no usage limits" | Web, app | Use now; one paid consult type, one free Screen Test | V · verify-11 · https://cal.com/pricing |
| zcal; TidyCal; YouCanBookMe; Calendly | Backups | zcal "Fee on payments 3%" free; TidyCal "Lifetime $29 once", "1% platform fee"; YouCanBookMe "30 bookings per month"; Calendly Standard Plus "$18 /seat/mo" | First three take payments free; Calendly Free does not | Web | Skip; Calendly cannot take the deposit | V · gaps-11, verify-11 · https://zcal.co/pricing |
| Appointo; Cowlendar | Bookings as Shopify products | Appointo Pro "$14 / month or $151/year"; Cowlendar Starter "$13.99 / month" | Appointo "Unlimited Bookings" with branding; Cowlendar "5 bookings/mo" | Shopify | Appointo Pro pay when it earns it; skip Cowlendar | V · verify-11, gaps-11 · https://apps.shopify.com/appointo-appointments-and-bookings |
| Tally | Forms with payments | Pro "$24 per month" | "unlimited forms and submissions, completely free", "Collect payments" | Web | Hire Hollie intake | V · gaps-11 · https://tally.so/pricing |
| Linktree; Carrd | Link page; one-page site on an own domain | Carrd "Pro Standard $19 / year" | Linktree Free; Carrd "up to three sites" with branding | Web | Linktree now; Carrd when the page should sit on Hollie's domain | V · gaps-11 · https://carrd.co/ |
| Espanso; Text Blaze; iPhone Text Replacement | Canned replies | Text Blaze Pro "$2.99 USD per month, billed yearly" | Espanso GPL-3; Text Blaze "Limited snippets"; iOS built in | Windows; Chrome; iPhone | Use now, one library | V · verify-11, gaps-11 · https://espanso.org/ |
| Instagram FAQ responses; ManyChat; Beacons | DM automation | ManyChat page 403; Beacons "9% seller fees" on Free | Instagram built in | Apps | Instagram FAQs now; ManyChat when comments outrun replies and its price is read; never sell through Beacons | V, ManyChat U · gaps-11, verify-11 · https://help.instagram.com/search/?query=saved%20replies |
| Zapier; n8n; Activepieces; IFTTT; Make | Glue | Zapier "100 tasks per month" free, Professional "Starting from $19.99 /month"; n8n Cloud Starter "$20 /mo, billed annually" (verify corrected 20€); Activepieces "1,000 credits a month" free; Make 403 | n8n Community "free ... indefinitely" | Web; Fedora box | n8n or Activepieces only if the dashboard needs glue; skip Zapier, "Etsy has not yet built an integration on Zapier" | V, Make U · verify-11, gaps-11 · https://docs.n8n.io/n8n-community-license |
| Google Voice; Pushover | Shop number; push | Pushover "$4.99 USD one-time purchase on each platform" | Voice personal calls free; Pushover "10,000 messages per month for free" | Web, phone | Use now; never script texts | V · lane 11, verify-11 · https://support.google.com/voice/answer/115061 |
| Help desks: Tidio, Crisp, Help Scout, Chatwoot, Zoho Desk, HubSpot | Shared inbox | Tidio Starter "$24.17 /mo." | Free tiers exist | Web | Skip; no ticket queue for one person | V · lane 11, gaps-11 · https://www.tidio.com/pricing/ |

Decision. Etsy's own messaging is the customer-service layer: a weekly auto-reply for away hours, 8 to 12 quick replies, the writing assistant on. One reply library in Espanso and iPhone Text Replacement. Hire Hollie books through Cal.com Free and intakes through Tally, both taking payment free, which fits the rule of payment before any visit. Haiku stays for listing drafts, not buyer replies. Pushover stands; Shopify-event alerts need the Shopify API, n8n or Activepieces because Flow on Basic has no Send HTTP Request (verify-11). Skip Calendly, Gorgias, Freshdesk, Chatfuel and every browser bot on eBay or Facebook.

## 10. Books and tax

| Tool | Does | Price | Free tier | Platform | Verdict | Source |
|---|---|---|---|---|---|---|
| Airtable | Item ledger with photos; Ricky has it | Team "$20USD per seat/month" annual | "1,000 records per base", "1 GB of attachments per base" | Web, apps | Use now until Supabase | V · verify-09 · https://airtable.com/pricing |
| Zoho Books | Autoscans, mileage, reconciliation, P&L | "STANDARD $20 $15 Price/Org/Month Billed Annually" for bank feeds (verify: Free has none) | "FREE $0 ... Receipt and Document Autoscans ... 1 User + 1 Accountant" | Web, apps | Use now; import statements by hand | V · verify-09 · https://www.zoho.com/us/books/pricing/ |
| TripLog; FreeTaxUSA | Automatic mileage; federal Schedule C filing | TripLog Premium "$4.99 Per month Paid annually"; FreeTaxUSA "State Tax Returns $15.99" | TripLog Basic "Free forever"; "Federal Tax Returns Free" | iOS, Android; web | Use now; no Florida return | V · verify-09 · https://www.triplog.net/pricing |
| Shopify Tax | Sales tax on the own store | After "$100,000 USD" lifetime sales, "0.35%" per order, max "$0.99 USD" | Free to the threshold, stores created on or after May 13, 2026 | Shopify | At launch, after DR-1 | V · verify-09 · https://help.shopify.com/en/manual/taxes/shopify-tax/pricing |
| Avery Design & Print; NIIMBOT D110; Brother QL-800 | SKU and QR labels | NIIMBOT "Regular price $29.99 USD Sale price $20.90 USD"; Brother "$124.99" | Avery free | Web; phone; USB | Avery now; NIIMBOT for tags at the rack; skip Brother | V · gaps-09, verify-09 · https://www.avery.com/software/design-and-print/ |
| Flippd | Phone ledger: cost, fees, net profit, Schedule C; one-way eBay sync | Pro "$8.33/mo billed annually ($99.99/yr), or $9.99/month" | "free for up to 20 inventory items" | iPhone, Android, web | Test free on 20 pieces; see Contradictions before paying | V · gaps-09 · https://getflippd.com/pricing |
| Seller Ledger | Imports Etsy, eBay, Shopify sales | "Up to 250 transactions per month $10 /month $100 /year" | "30-day free trial No credit card required" | Web | Pay when orders flow; monthly plans look back 90 days | V · verify-09 · https://sellerledger.com/pricing/ |
| Inventory Now; My Reseller Genie | Item tracker with three-channel connections; reseller books | "$10 BILLED $120 YEARLY"; MRG "Ultimate $22.99 per month" is the only tier with sync | Inventory Now "Free for your first ten items." | Apps; MRG web only | Only if phone stock sync is wanted; Etsy connection shipped "Nov 2, 2026" | V · gaps-09, verify-09 · https://www.inventorynow.com/ |
| QuickBooks; Wave; ZipBooks; Found; Everlance; MileIQ; Hurdlr; Sortly; Flipwise; Keeper | General books, mileage, inventory, eBay-only, tax pro | QuickBooks Solopreneur "$20 $10/mo 50% off for 3 months*"; Wave "PRO Plan $190USD/year"; MileIQ "Unlimited $11.66 PER MONTH BILLED ANNUALLY"; Sortly "Advanced $24 USD/mo.*"; Flipwise "$19.99 /mo"; Keeper "Standard $199 /yr" | Capped | Web, apps | Skip: capped, paid bank import, or a free pick covers it; Keeper only for a pro-signed return | V · verify-09, gaps-09 · https://quickbooks.intuit.com/pricing/ |

Decision. Day one is $0: Airtable Free with cost-basis columns, Zoho Books Free with statements imported by hand, TripLog Basic, Avery labels, FreeTaxUSA at filing time. Seller Ledger "$10 /month" is the first paid books tool, from the month of the first sale. Tax facts that hold (verify-09): 1099-K only above $20,000 and 200 transactions, all income reportable regardless; Florida 6% plus Lee 0.5% through December 31, 2028, Collier none; Etsy and eBay remit as facilitators and those sales are excluded from the shop's own return; the Shopify store needs DOR registration on DR-1 first; Lee County's receipt is "$50" for an October to March start, expiring September 30; no DOR page states a registration fee (U). The room's county is unconfirmed and decides surtax and receipt.

## 11. Desktop utilities and video

| Tool | Does | Price | Free tier | Platform | Verdict | Source |
|---|---|---|---|---|---|---|
| DaVinci Resolve 21; Clipchamp; CapCut Desktop | Full editor; 1080p "Watermark-free" cuts; vertical templates, video Remove BG | DaVinci Studio "Was $295 Now $236" once; CapCut Pro "USD 19.99 /month", "Displayed pricing is for reference only" | All | Windows | Use now; no CapCut library music until its terms are read (every terms page failed) | V · verify-12 · https://www.blackmagicdesign.com/products/davinciresolve |
| LosslessCut; HandBrake; Subtitle Edit; Buzz; OBS Studio; Snipping Tool; CuePrompter; Audacity | Trim; compress; offline Whisper captions; recording and live; Win+Shift+R screen video; teleprompter; audio | Free, open source | All | Windows, browser | Use now | V · gaps-12, verify-12 · https://www.nikse.dk/subtitleedit |
| Music: Meta Sound Collection; Incompetech; YouTube Audio Library; Bensound; Epidemic Sound | Licensed music | Bensound "All Access $9 /month (Billed $119 annually)"; Epidemic Pro "$16.99 Per month, billed $203.88 yearly" for "commercial use online" (verify: the lane named the wrong tier) | Meta "Free to use in any videos you create and share on Facebook and Instagram" only; Incompetech CC BY 4.0 with credit | Web | Meta for Reels, Incompetech elsewhere; Bensound when credits become a chore; skip Epidemic | V · gaps-12, verify-12 · https://www.facebook.com/sound/collection/ |
| Veed; Kittl; Opus Clip; Descript; ElevenLabs | Auto subtitles; vintage lettering; AI clipper; text editor; AI voice | Veed Creator "$12 per user / month billed yearly"; Kittl Pro "$14 /mo, billed annually"; Opus Clip Starter "$15 USD/mo"; ElevenLabs Free "does not include a commercial license" | Kittl "$0 /mo, free forever", "Full commercial license"; Opus watermarks | Web | Kittl Free now; Veed when captions go out daily; skip clippers and AI voices | V · verify-12, gaps-12 · https://www.kittl.com/pricing |
| Bitwarden; LanguageTool; Harper; Grammarly | Passwords; grammar | Bitwarden Premium "$1.65 per month" "Billed annually at $19.80"; Grammarly Pro "$12 USD", period U | Bitwarden "Unlimited devices, unlimited passwords"; LanguageTool free, no account; Harper "$0" | Chrome, Edge, Windows | Bitwarden now; one checker; skip Grammarly and 1Password | V · verify-13, gaps-13 · https://bitwarden.com/pricing/ |
| PowerToys; Snipping Tool OCR; Win+V; Ditto; ShareX; Win+H | Resize, OCR, rename, clipboard, capture, dictation | Free | Win+V holds 25 entries, clears on restart except pinned (verify) | Windows | Use now; Ditto when the cap bites | V · verify-13, gaps-13 · https://learn.microsoft.com/en-us/windows/powertoys/install |
| iCloud for Windows and iCloud+; HEIF and HEVC extensions; LocalSend | Full-resolution iPhone photos in Explorer; HEIC; HEVC; local transfer | iCloud+ "200 GB" "$2.99" "billed monthly"; HEIF "Free"; HEVC "$0.99" once | iCloud "5 GB"; LocalSend "100% free and open source" | Windows 11, iPhone | Use now; $2.99 when 5 GB fills | V · verify-13, gaps-13 · https://support.apple.com/en-us/108047 |
| Wispr Flow; Superwhisper; Aqua Voice | AI dictation | Wispr Pro "$12/user/mo"; Superwhisper Pro "$8.49/month" yearly | Wispr "$0/mo", "Limited words per week" | Windows, iPhone | Wispr Free a week; Pro when the cap stops a session; skip the others | V · verify-15 · https://wisprflow.ai/pricing |
| Claude in Chrome; Claude Cowork | Browser agent, "clicks, types, and fills forms" | "Available on all paid plans."; Cowork "Works with a paid plan." | Ricky already pays | Chrome; Windows desktop | Etsy only, Ricky watching, "safety check on each action" on; never eBay, Facebook, Chairish; never scheduled | V · verify-15, gaps-15 · https://claude.com/claude-in-chrome |
| Gemini auto browse; ChatGPT Work cloud browser; Perplexity Comet; Opera Neon; Nanobrowser | Other agents | Google AI Pro "$19.99/ month" US preview; ChatGPT Plus "$20/month (billed monthly)", cloud browser "excluding Free and Go"; Comet U; Neon "$19.90/month"; Nanobrowser free | Varies | Chrome, web | Skip; ChatGPT agent and Atlas retired; the cloud browser runs unattended | V, Comet U · verify-15 · https://help.openai.com/en/articles/20001280-using-cloud-browser-in-chatgpt |

Decision. A free Windows stack covers editing, captions, recording and design: DaVinci, Clipchamp, CapCut without its music, LosslessCut first on every iPhone clip, HandBrake under TikTok's 500 MB, Subtitle Edit, OBS, Affinity, Canva Free, Kittl Free. Music licences matter more than tool prices: Meta Sound Collection only on Facebook and Instagram, Incompetech with a credit line elsewhere. AI video generators are out; the buyer must see the real object, and Sora was "discontinued on April 26, 2026" (verify-12). Dictation is free on both devices; iPhone Dictation needs no signal, which matters in a thrift store. The browser agent is Claude in Chrome on Etsy only; browser sessions and Claude Code draw from "the same pool" (verify-15), API drafts are unaffected. Pay when it earns it: DaVinci Studio once, Veed, Kittl Pro, Bensound, iCloud+.

## Cost ladders

### The $0 stack

| Stage | Tools | Monthly |
|---|---|---|
| Source | EstateSales.net, EstateSales.org, Trove, eBay saved searches, Proxibid, LiveAuctioneers, Craigslist, CTBids, HiBid, Goodwill VIP Perks, changedetection.io | $0 |
| Identify | Lens, Bing Visual Search, Kovels guide pages, marks folder, VFG, FTC RN, Antiquers, Appraisily ID, FindArtInfo account | $0 |
| Price | eBay Product Research, Poshmark Sold, Chairish, EBTH, Invaluable free, Artsy, Bidsquare, Google Shopping | $0 |
| Photos | Windows Photos and Paint, Snapseed, Designer, rembg, withoutBG, Upscayl, PowerToys, Caesium, ImageMagick, Affinity, Canva Free | $0 |
| Write | Marketplace Insights, Etsy Stats, eRank Free, EHunt Free, Alura Free, 3Dsellers Title Builder, one chatbot | $0 |
| List | Etsy Seller app, eBay app, Secnd Free, VendorSnap Free, Swiftlisted trial | $0 |
| Ship | Pirate Ship, Etsy labels, eBay Labels, ShipSaving Starter, USPS boxes, Label Broker | $0 plus postage and insurance |
| Market | Share & Save, Pinterest account, Linktree, QRCode Monkey, Nextdoor, Yelp, Mercari, VMD profile, Buffer Free, Canva Free, Instagram Edits, Kit Free | $0 |
| Messages | Etsy Messages, Cal.com Free, Tally, Espanso, Text Replacement, Instagram FAQs, Google Voice | $0 |
| Books | Airtable Free, Zoho Books Free, TripLog Basic, Avery, FreeTaxUSA, Flippd to 20 items | $0 |
| Desktop and video | DaVinci, Clipchamp, LosslessCut, HandBrake, Subtitle Edit, OBS, Bitwarden Free, LanguageTool, iCloud 5 GB, LocalSend, Wispr Free, Claude in Chrome on the existing plan | $0 |
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

The standing decisions do not fit this line. Crosslist Gold "$39.99 per month" in place of Vendoo makes $81.98. Swiftlisted Starter "$6 USD/mo $72 USD billed yearly" makes $47.99, with Etsy posted through a Chrome extension on a PC that stays on. Holding Shopify until the storefront takes checkout brings the line to between $25.48 and $52.98, depending on the crosslister.

### The everything stack

Every "pay when it earns it" line on at once; yearly prices divided by twelve.

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
