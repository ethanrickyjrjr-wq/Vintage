# Verify 04: Comps and pricing research tools (adversarial price and claim check)

Date: 2026-11-07. Author: research subagent (verifier for lane 04-pricing-comps).
Question: Do the prices, free tiers, platform claims and availability claims recorded by the first agent for lane 04 hold up against the vendors' own pages today?
Legend: V = vendor page read today (2026-11-07); U = unverified (page would not load, or only a non-vendor source).
Verdicts: confirmed = the exact figure or claim appears on the page read today; refuted = the page says something different (correction given); unreadable = page and one alternative would not load.

Method: every page fetched with headless Chromium through the session proxy (curl fallback). WebSearch quota was exhausted for the session before this lane ran, so no new URLs were searched; alternatives came from vendor footers, help links and app-store links on pages that did load. Prices quoted as the vendor writes them. No new tools were added.

## 0. Bottom line

- 17 confirmed, 2 refuted, 4 unreadable, out of 23 checks on 17 tools.
- The free backbone holds: eBay Product Research is free to all sellers with 3 years of sold data, Poshmark shows sold prices without login, Chairish's Hide Sold Out filter exists, EBTH's archive is searchable on a free (card-validated) account, Google Lens is free on iPhone and desktop browsers.
- Refuted 1: Invaluable's free tier is not "limits unknown". A free account shows 12 months of past prices; Premium shows 5 years; Professional 15+ years. Subscription prices still unread (page walled).
- Refuted 2: Kovels price guide price is not unknown. It is sold as "Kovels All Access" at $59.99 per year (price guide, articles, newsletter archive); All Access + Print is 79.99 per year. The $24.95 figure is a separate Antique Trader magazine digital subscription that does not list the price guide.
- WorthPoint: the vendor site walled every URL again. Apple's own App Store listing carries the in-app prices: Price Guide Monthly $26.99, Price Guide Annual $249.99, plus MARKS bundles. App rating 2.1 from 117 ratings. The first agent's figures stand; the source is Apple's listing, not a third-party snapshot.
- LiveAuctioneers: the first agent's URL (/pages/price-results/) returns a 404 body. The free-account claim remains unverified. Heritage and Mercari sold search walled the fetcher.
- Etsy SEO tools (eRank, EverBee, Marmalead, Alura) and the reseller tools (Flipwise, Vendoo) match the recorded prices, with one nuance: EverBee's $24.99 and $69 per month are the annual-billing rates; monthly billing is higher ($468 per year implied for Growth).
- eBay Basic Store is $27.95 per month on monthly renewal or $21.95 per month on yearly renewal; eBay charges either option monthly. Only Sourcing Insights needs it; Product Research does not.

## 1. Check table

| Tool | Claim checked | Verdict | Evidence quote | URL | Correction |
|---|---|---|---|---|---|
| eBay Product Research | Free to all sellers; lives in Seller Hub Research tab | confirmed (V) | "The best part: it's free to all sellers. Find it under the Research tab in Seller Hub." | https://www.ebay.com/sellercenter/growth/ebay-research-tools | none |
| eBay Product Research | 3 years of sold data; available in the mobile apps | confirmed (V) | "access to the last 3 years of eBay sales data" and "directly from the Seller Hub Research tab and the mobile apps" | https://www.ebay.com/help/selling/selling-tools/terapeak-research?id=4853 | none |
| eBay Product Research | Sourcing Insights needs a Basic Store at $27.95 monthly / $21.95 yearly | confirmed (V) | "Basic $27.95 $21.95" (Monthly renewal / Yearly renewal); "For either option, we charge the subscription fee on a monthly basis." | https://www.ebay.com/help/selling/fees-credits-invoices/store-selling-fees?id=4809 | Clarify: $21.95 is per month on a yearly commitment, not a yearly lump sum. Sourcing Insights "is available to sellers with a Basic or above Store subscription" (sellercenter page). |
| Poshmark Sold filter | Free; sold prices visible without login | confirmed (V) | Page shows "Log in / Sign up" (not logged in) and listings such as "SOLD Vintage Cream Stiffel Linen Lamp Shade, Accordion Pleats $45" | https://poshmark.com/search?query=stiffel%20lamp&availability=sold_out | none |
| Chairish | Free to browse; Hide Sold Out filter under Availability | confirmed (V) | "Availability / Hide Sold Out / Ready to Ship"; "463 items" | https://www.chairish.com/collection/stiffel (redirects to https://www.chairish.com/maker/stiffel) | URL correction: /collection/stiffel redirects to /maker/stiffel. Use the maker URL. |
| 1stDibs | Free to browse; no sold filter | confirmed (V) | "Show 151 Results"; filter list is "PRICE / Any price / Under $1,000 / Under $2,000 / Under $3,000 / $3,000 and up"; no sold or availability filter in the list | https://www.1stdibs.com/creators/stiffel/furniture/ | none |
| EBTH | Free account; credit card required at sign-up; archive of past lots searchable | confirmed (V) | "WHY DO I HAVE TO INPUT CREDIT CARD INFORMATION TO SIGN UP?" ... "By validating card information, we protect our bidders and sellers"; "You can search for both Active and Archived Items." | https://www.ebth.com/faq | none |
| EBTH | Platform: web, iOS | confirmed (V), incomplete | App Store: "Free", "iPhone, iPad, Apple TV", "25K RATINGS", "Requires iOS 13.0 or later." Footer of ebth.com also links https://play.google.com/store/apps/details?id=com.ebth.ebth_webview | https://apps.apple.com/us/app/ebth/id974740086 | Add Android: a Google Play app is linked from the EBTH footer. |
| Google Lens | Free; web (Chrome, Firefox, Safari, Edge), Android, iPhone | confirmed (V) | "You can do a visual search with Lens on most browsers like: Chrome Firefox Safari Edge"; tabs "Computer / Android phone & tablet / iPhone & iPad" | https://support.google.com/websearch/answer/1325808 | none. The page never says "free"; it shows no price and no sign-up. |
| Invaluable Price Archive | Free account exists; limits unknown | refuted (V) | "With a free Invaluable account, you will have access to up to 12 months of past auction prices." "our Premium subscription provides access to the last five years in the archive, and the Professional provides access to the last 15+ years." | https://www.invaluable.com/inv/help/faq/search-price-archive/ (answers are collapsed on the page; read from the page HTML) | Free tier limit is 12 months of past prices. Paid: Premium 5 years, Professional 15+ years, unlimited searches, Christie's and Sotheby's catalogs. Prices of the paid tiers still unknown: /subscriptions/ and /price-archive/ would not load. |
| LiveAuctioneers Price Results | Free with account (reported); page at /pages/price-results/ | unreadable (U) | The URL returns the site shell with "404 Sorry! We can't find what you're looking for." Support site redirected to "LiveAuctioneers Admin" (hc/en-gb) with no relevant article. /price-guide/ and /price-result/ failed. | https://www.liveauctioneers.com/pages/price-results/ | The first agent's URL is dead. Free-account claim stays unverified. Manual browser check still required. |
| WorthPoint Price Guide | About $26.99 per month; $249.99 per year; vendor pricing page blocked; 2.1-star app | confirmed (V, via Apple listing) | "Price Guide Monthly $26.99", "Price Guide Annual $249.99", "Price Guide + MARKS Monthly $37.99", "Price Guide + MARKS Annual $399.99", "MARKS Premium Monthly $19.99", "MARKS Premium Annual $99.99"; "Free · In-App Purchases"; "2.1" "117 RATINGS"; "Requires iOS 16.0 or later." iTunes lookup: version 6.3.4, released 2026-09-28, averageUserRating 2.08 | https://apps.apple.com/us/app/worthpoint/id1472512649 and https://itunes.apple.com/lookup?id=1472512649 | Source correction: the prices are on Apple's own listing (in-app purchase list), not a third-party snapshot. worthpoint.com/pricing, /subscribe, /pricing-plans and the home page all failed today; Google Play failed. App Store prices can differ from web prices; still confirm on worthpoint.com in a browser before buying. |
| Artnet Price Database Decorative Art | $34 / 30 days; $350 / year; unlimited searches; lots under $500 excluded | confirmed (V) | "PRICE DATABASE DECORATIVE ART ... Number of searches unlimited unlimited ... $34 /30 days* ... $350 /year*"; "both databases only include items estimated at $500 and above." | https://www.artnet.com/price-database/ | none |
| Artnet Price Database Fine Art and Design | One-Day Pass $32.50 / day (5 searches); Individual Rollover $42.50 / 30 days (10 searches) | confirmed (V) | "Number of searches 5 10** 150 450"; "$32.50 /day"; "$42.50 /30 days*"; "$450 /year*"; "$1,175 /year*"; "Each additional Individual Rollover search is $3.50." | https://www.artnet.com/price-database/ | Omitted, not wrong: Expert $450 / year (150 searches) and Appraiser $1,175 / year (450 searches). |
| eRank | Free $0/mo; Basic $5.99/mo; Pro $9.99/mo; Expert $29.99/mo; free = 5 keyword lookups/day, 1 shop, 50 listings | confirmed (V) | "Free $0/mo 5 keyword lookups/day 1 shop, 50 listings"; "$5.99/mo ... 100 keyword lookups/day"; "$9.99/mo ... 200 keyword lookups/day"; "$29.99/mo ... 500 keyword lookups/day"; "without submitting any credit card or payment information" | https://erank.com/pricing (redirects to https://erank.com/plans) | none. Figures read with the Monthly toggle. |
| EverBee | HOBBY $0; GROWTH $24.99 / month ($299 per year); BUSINESS $69 / month billed annually at $828 | confirmed (V), with nuance | "HOBBY $ 0 / month Free forever"; "GROWTH $ 24.99 / month That comes to $468 $299 per year"; "BUSINESS $ 69 / month Billed annually at $828 - save $360"; free: "Product Analytics: views, reviews, favorites Keyword Research: 10 keywords" | https://www.everbee.io/pricing | The $24.99 and $69 per-month figures are the Annual toggle (default, "Annual Save 36%"). Monthly billing is higher: "$468" struck through implies $39 per month for Growth. Record them as annual-billing rates. |
| Marmalead | $19/mo paid monthly; $190 USD paid annually; $300 USD paid ONCE lifetime; no free tier | confirmed (V) | "$19/mo $19 USD paid monthly"; "$16/mo $190 USD paid annually"; "$5/mo $300 USD paid ONCE"; no "free" or "trial" text on the page | https://marmalead.com/pricing (serves /pricing/) | Omitted, not wrong: quarterly "$18/mo $53 USD paid quarterly". |
| Alura | Free $0 / month; Basic $95.88 billed yearly; Growth $179.99 billed yearly; Professional $359.88 billed yearly; free = 5 daily searches, Chrome extension, API & MCP access, 100 API credits per month | confirmed (V) | "$95.88 billed yearly, save 33%"; "$179.99 billed yearly, save 50%"; "$359.88 billed yearly, save 57%"; "Free plan includes: 5 daily keyword & product searches ... Alura Chrome Extension"; "API & MCP access Included"; "API credits 100 per month" | https://www.alura.io/pricing | none. Page defaults to the Annually toggle; monthly-billing prices were not captured. "Every paid plan has a 7-day money-back guarantee." |
| Kovels Price Guide | Price guide price unknown; magazine Digital Only 1 year (12 issues) $24.95 | refuted (V) | Kovels offers page: "Kovels All Access ... $59.99 per year ... Kovels Price Guide with over 1 million items, rigorously maintained"; "Kovels All Access + Print 79.99 per year". Antique Trader page: "Digital Only 1 year (12 issues) for just $24.95" (also Print $29.95, Print + Digital $34.95) | https://www.kovels.com/subscriptions/ (redirects to https://subscribe.kovels.com/loading.do?omedasite=AQT_LandOffer); https://www.kovels.com/subscribe (redirects to my.antiquetrader.com) | The price guide is sold inside Kovels All Access at $59.99 per year. The $24.95 digital magazine is a separate product; its page does not list price-guide access. Price guide page itself: "Over 1 million prices for antiques and collectibles". |
| Flipwise | Free up to 24 listings (new members only); $19.99 /mo for 100–499 listings | confirmed (V) | "Free Up to 24 listings (new members only)"; "$19.99 /mo 100–499 listings"; "We charge based on the size of your store. (Total active listings + sold over the last 30 days.)"; "7-DAY MONEY-BACK GUARANTEE" | https://flipwise.app/ | none. Price is a slider; the 25–99 listing tier was not visible in static text. |
| Vendoo | STARTER $12.49, GROWTH $24.99, PRO $49.99 per month billed yearly; 14-day trial | confirmed (V) | "STARTER $12.49 Per month, billed yearly"; "GROWTH $24.99 Per month, billed yearly"; "PRO $49.99 Per month, billed yearly"; "Try Vendoo Free for 14 Days." | https://vendoo.co/pricing | none. Monthly-billing prices (Pay Monthly toggle) not captured. |
| Mercari sold search | Free sold-item search on the web | unreadable (U) | Search URL: browser HTTP 403. Help center loaded ("How Can We Help? Mercari Support") but lists no sold-search article. | https://www.mercari.com/search/?keyword=stiffel%20lamp&status=sold_out ; https://www.mercari.com/us/help_center/ | Still unverified. Check in the Mercari app on the iPhone instead. |
| Heritage Auctions archive | Price and free tier unknown | unreadable (U) | Both ha.com URLs failed to load (archive page and home). | https://www.ha.com/c/ref/auction-archives.zx ; https://www.ha.com/ | Still unknown. Low fit anyway (coins, cards, fine art). |

## 2. What the first agent got wrong

1. Invaluable: "limits unknown" was wrong. The FAQ states a free account gives 12 months of past auction prices; Premium 5 years; Professional 15+ years. Paid prices remain unread.
2. Kovels: "unknown for the price guide" was wrong. Kovels All Access is $59.99 per year and includes the Price Guide. The $24.95 figure is the Antique Trader digital magazine, a different product.
3. LiveAuctioneers: the cited URL https://www.liveauctioneers.com/pages/price-results/ is a 404. Do not reuse it. The free-account claim is still unverified.
4. Chairish: https://www.chairish.com/collection/stiffel redirects to https://www.chairish.com/maker/stiffel. Use maker URLs.
5. EBTH: the platform list missed Android. EBTH's footer links a Google Play app as well as the iOS app.
6. EverBee: $24.99 and $69 per month are annual-billing rates (Annual toggle is the default). Monthly billing is higher (Growth implied at $39 per month from the struck-through $468 per year).
7. WorthPoint: the price source was labelled a "third-party iOS snapshot". The figures are on Apple's own App Store listing for the WorthPoint app (in-app purchase list). Figures confirmed: Price Guide Monthly $26.99, Annual $249.99. Vendor site still walled.
8. eBay Basic Store: "$27.95 monthly / $21.95 yearly" reads as a yearly lump sum. eBay charges both options monthly; $21.95 is the per-month rate with yearly renewal.
9. Minor omissions, not errors: Marmalead quarterly $53; Artnet Expert $450 / year and Appraiser $1,175 / year; WorthPoint MARKS bundles ($19.99 and $37.99 monthly, $99.99 and $399.99 annual).

Everything else checked (eBay Product Research free and 3 years, Poshmark, 1stDibs, EBTH card requirement, Google Lens, Artnet, eRank, Marmalead, Alura, Flipwise, Vendoo) matched the vendor page today.

## 3. Notes for Hollie

- Free stack is intact: eBay Product Research (Seller Hub on the PC, eBay app on the iPhone), Poshmark sold filter, Chairish maker pages with Hide Sold Out off, EBTH archive on a free card-validated account, Invaluable free account for the last 12 months of realized prices, Google Lens for identification.
- Invaluable free account is better than recorded: 12 months of realized auction prices, no payment. Sign up before paying anyone.
- WorthPoint stays a pay-once-then-cancel option at $26.99 for a month (Apple in-app price). Prefer the website at the same login; the app is rated 2.1. Vendor site prices could differ from Apple's; check in a browser.
- Kovels All Access ($59.99 per year) is the only way to the Kovels price guide. Guide values are not live comps; skip unless eBay and Invaluable both run dry on a category.
- Artnet Decorative Art $34 for 30 days only for a signed piece that already looks like $500 plus.
- LiveAuctioneers, Heritage and Mercari sold search need a manual browser or app check; none loaded here.

## 4. Gaps and pages that would not load

- worthpoint.com: /pricing, /subscribe, /pricing-plans and the home page all failed (browser and curl). Google Play listing failed. wp.force.com/FAQ/s/ loaded empty via curl.
- invaluable.com: /subscriptions/ and /price-archive/ failed. Paid tier prices unknown.
- liveauctioneers.com: /pages/price-results/ is a 404; /price-guide/ and /price-result/ failed; the support site redirected to an admin help center with nothing relevant.
- mercari.com search: HTTP 403. Help center loaded but has no sold-search article.
- ha.com: archive page and home failed.
- ebay.com/sellercenter/ebay-stores/subscription-plans: curl fallback returned only the title; the help page on Store fees covered the figures.
- kovels.com/price-guide.html: 404 (wrong guess); the real page is /antique-collectible-price-guide.
- Monthly-billing prices for EverBee, Alura and Vendoo were not captured because each page defaults to the annual toggle and the fetcher reads the default state.
- WebSearch quota was exhausted before this lane ran; no URLs beyond the first agent's list and on-page links were discovered.

## 5. Sources (every URL fetched today, 2026-11-07)

https://www.ebay.com/sellercenter/growth/ebay-research-tools
https://www.ebay.com/help/selling/selling-tools/terapeak-research?id=4853
https://www.ebay.com/help/selling/fees-credits-invoices/store-selling-fees?id=4809
https://www.ebay.com/sellercenter/ebay-stores/subscription-plans
https://poshmark.com/search?query=stiffel%20lamp&availability=sold_out
https://www.chairish.com/collection/stiffel
https://www.chairish.com/maker/stiffel
https://www.1stdibs.com/creators/stiffel/furniture/
https://www.ebth.com/faq
https://www.ebth.com/
https://apps.apple.com/us/app/ebth/id974740086
https://support.google.com/websearch/answer/1325808
https://www.invaluable.com/inv/help/faq/search-price-archive/
https://www.invaluable.com/subscriptions/
https://www.invaluable.com/price-archive/
https://www.liveauctioneers.com/pages/price-results/
https://support.liveauctioneers.com/hc/en-us
https://www.liveauctioneers.com/price-guide/
https://www.liveauctioneers.com/price-result/
https://www.worthpoint.com/pricing
https://www.worthpoint.com/subscribe
https://www.worthpoint.com/pricing-plans
https://www.worthpoint.com/
https://apps.apple.com/us/app/worthpoint/id1472512649
https://itunes.apple.com/lookup?id=1472512649
https://play.google.com/store/apps/details?id=com.worthpoint.app&hl=en_US
https://wp.force.com/FAQ/s/
https://www.artnet.com/price-database/
https://erank.com/pricing
https://erank.com/plans
https://www.everbee.io/pricing
https://marmalead.com/pricing
https://www.alura.io/pricing
https://www.kovels.com/
https://www.kovels.com/subscribe
https://www.kovels.com/price-guide.html
https://www.kovels.com/subscriptions/
https://subscribe.kovels.com/loading.do?omedasite=AQT_LandOffer
https://www.kovels.com/antique-collectible-price-guide
https://flipwise.app/
https://vendoo.co/pricing
https://www.mercari.com/search/?keyword=stiffel%20lamp&status=sold_out
https://www.mercari.com/us/help_center/
https://www.ha.com/c/ref/auction-archives.zx
https://www.ha.com/
