# Verify 05: Identification and authentication tools (adversarial price and claim check)

Date: 2026-11-07. Author: research subagent (verifier for lane 05-identification).
Question: Do the prices, free tiers, platform claims and availability claims the first agent recorded for lane 05 hold up against the vendors' own pages today?
Legend: V = vendor page read today (2026-11-07); U = unverified (page would not load, or only a non-vendor source).
Verdicts: confirmed = the exact figure or claim appears on the page read today; refuted = the page says something different (correction given); unreadable = the page and one alternative would not load.

Method: every page fetched with headless Chromium through the session proxy (curl fallback), 2026-11-07. WebSearch was not used; every URL came from the first agent's list, from vendor footers and redirects, or from the lane 04 verifier's notes. Prices are quoted as the vendor writes them. No new tools were added.

## 0. Bottom line

- 26 checks on 21 tools: 21 confirmed, 2 refuted, 3 unreadable.
- The free backbone holds. Google Lens, Bing Visual Search, Kovels' marks guide pages, thepotteries.org, porcelainmarksandmore.com, silvercollection.it, 20thcenturyglass.com, the VFG Label Resource, the FTC RN database and Collectors Weekly Show & Tell all loaded today and all are free to read.
- Refuted 1: Kovels' membership price is not "not found". kovels.com/subscriptions/ redirects to the vendor's offers page: "Kovels All Access Online $59.99 per year" and "Kovels All Access + Print 79.99 per year". The marks guide pages and the Kovels Komments newsletter stay free.
- Refuted 2 (source, not figure): WorthPoint "MARKS Premium Monthly $19.99" is on Apple's own App Store listing for the WorthPoint app, not only a third-party tracker. Also there: MARKS Premium Annual $99.99, Price Guide Monthly $26.99, Price Guide + MARKS Monthly $37.99. worthpoint.com/pricing still returns 403. App rating 2.1 from 117 ratings and the login lockout complaints are real.
- PSA/DNA figures are exact: single-signed $10 to $500, 2 signatures from $20, Premium Letter upgrade $15 under $50, expedited $75 for 10 business days, about 30 business days standard. Nuance the first agent missed: the Elvis photo carries two signatures, so the "2 Signatures" column applies (from $20), and any item declared at $1,000 or more pays an extra $40 and up.
- Claude, Gemini and Entrupy prices match the vendor pages to the cent. ChatGPT's pricing page still shows no dollar figures; OpenAI's help center gives Plus at "$20/month (billed monthly)".
- Unreadable: Replacements.com (403 on both URLs), Etsy's /legal/creativity (403; the help center loads but did not surface the 20-year rule), JSA's fee page (Angular route error, falls back to the home page; the FL phone number confirms a Florida office).
- Licence gotcha: TinEye's FAQ says "TinEye is free for non-commercial use." A resale shop is commercial use. Fit was already low; now it is also outside the free terms.

## 1. Check table

| Tool | Claim checked | Verdict | Evidence quote | URL | Correction |
|---|---|---|---|---|---|
| Google Lens | Free; Google app on iPhone; 5.3M ratings | confirmed (V) | "Free · In‑App Purchases" ... "5.3M RATINGS" ... "Requires iOS 17.0 or later." | https://apps.apple.com/us/app/google/id284815942 | none |
| Google Lens | Lens on desktop via Chrome | confirmed (V) | "With Google Lens in Chrome desktop, easily select, search and ask questions about anything you see on the web" | https://search.google/ways-to-search/lens/ | none |
| Bing Visual Search | Free; web, Windows 11, Edge, extensions | confirmed (V) | Title "Free Visual Search Tool"; "Windows 11 now allows users to capture screenshots and perform instant image lookups directly from the Snipping Tool." | https://explore.microsoft.com/en-us/bing/visual-search/ | none |
| Kovels marks guides | Guide pages free; Kovels Komments weekly newsletter free; warns marks are forged | confirmed (V) | "Sign up for our FREE weekly eNewsletter — Kovels Komments"; "marks are often forged and changed" | https://www.kovels.com/marks-identification-guide/ | none |
| Kovels membership | "membership price not found (join and pricing pages 404)" | refuted (V) | "Kovels All Access Online $59.99 per year"; "Kovels All Access + Print 79.99 per year" | https://www.kovels.com/subscriptions/ (redirects to https://subscribe.kovels.com/loading.do?omedasite=AQT_LandOffer) | Price exists on the vendor's offers page: $59.99 per year online, 79.99 per year with the print magazine. Not needed for the free marks pages. |
| thepotteries.org | Free marks index | confirmed (V) | "This section helps you identify pottery made in the North Staffordshire potteries of Stoke-on-Trent using the marks often found on the base of ceramics." No fee or login text on the page. | https://www.thepotteries.org/mark/index.htm | none |
| porcelainmarksandmore.com | Free; a few factory entries members-only for a fee | confirmed (V) | "offers a lot of useful information for free ... A few factory entries (shown as red text in the appropriate menus) can only be viewed by site members." | https://www.porcelainmarksandmore.com/ | Fee amount still not read (membership page not fetched). |
| silvercollection.it | Free hallmark reference | confirmed (V) | "a 1500 pages richly illustrated website offering all you need to know about antique silver, sterling silver, silverplate"; no fee text | https://www.silvercollection.it/ | none |
| 20thcenturyglass.com | Free glass encyclopaedia | confirmed (V) | "Browse our extensive identification guide to antique & collectable vintage glass." | https://www.20thcenturyglass.com/ | Note: it is also a dealer's shop ("Enter Glass Store"); the encyclopaedia is free. |
| VFG Label Resource | Free; donation requested | confirmed (V) | "a free, public educational project"; "HELP KEEP THESE RESOURCES FREE. CLICK TO DONATE $5 NOW." | https://vintagefashionguild.org/resources/vintage-label-resource/ | none |
| FTC RN database | Free search | confirmed (V) | "SEARCH RN DATABASE"; "Welcome to the new RN System!" | https://rn.ftc.gov/ (redirects to https://rn.ftc.gov/rns) | A login is needed only to apply for or change an RN, not to search. |
| Collectors Weekly Show & Tell | Free to post; humans identify | confirmed (V) | "Share your favorites on Show & Tell / Post an item"; "Unsolved Mysteries / Solved Mysteries"; "Sign in" | https://www.collectorsweekly.com/stories | Posting needs a free account (Sign in link). |
| Replacements.com Pattern Identification | Free pattern ID service | unreadable (U) | "FETCH FAILED ... browser: HTTP 403" on identify.htm and services.htm | https://www.replacements.com/identify.htm ; https://www.replacements.com/services.htm | Still walled. Confirm from Ricky's browser. |
| PSA/DNA | Single-signed tiers $10 to $500; about 30 business days | confirmed (V) | "Turnaround time is approximately 30 business days"; table "Single-Signed" runs "$10" to "$500" | https://www.psacard.com/pricing/autographs | Nuance: the Elvis photo has two signers, so the "2 Signatures" column applies: "$20" to "$500". Declared value "$1,000 - $2,499 $40" surcharge. |
| PSA/DNA | Premium Letter $15 for items under $50 | confirmed (V) | "Upgrades to full Premium Letters of Authenticity are available for an additional $15. Full Premium Letters are automatically issued for items submitted at $50 and above" | https://www.psacard.com/pricing/autographs | none |
| PSA/DNA | Expedited $75 per order, 10 business days; original photograph $50 for $999 or less | confirmed (V) | "$75 10 Business Days 1 - 5 items"; ORIGINAL PHOTOGRAPH AUTHENTICATION "$999 or less $50" | https://www.psacard.com/pricing/autographs | Original Photograph service is a separate order and cannot be expedited. |
| WorthPoint MARKS Premium | "about $19.99 monthly per third-party tracker dated 2026-03-21; vendor pages walled" | confirmed figure, refuted source (V via Apple listing) | "MARKS Premium Monthly $19.99"; "MARKS Premium Annual $99.99"; "Price Guide + MARKS Monthly $37.99"; "Price Guide Monthly $26.99"; "Requires iOS 16.0 or later" | https://apps.apple.com/us/app/worthpoint/id1472512649 | The prices are on Apple's own listing (in-app purchase list), not only a third-party snapshot. worthpoint.com/pricing returned HTTP 403 today. Web prices could differ; check in a browser before paying. |
| WorthPoint Marks Gallery | 150,000 marks; free trial | confirmed (V) | "a resource of more than 150,000 makers' marks, autographs, patterns, and symbols (Marks)"; "START YOUR FREE TRIAL NOW" | https://pages.worthpoint.com/pages/welcome-landing-fb/ | none |
| WorthPoint app | Login lockouts in App Store reviews; 117 ratings | confirmed (V) | "2.1" "117 RATINGS"; review: "Constantly locking you out for too many failed log-in attempts when you tried.......once." | https://apps.apple.com/us/app/worthpoint/id1472512649 | none |
| Claude (vision) | Free $0; Pro $17/mo annual ($200 up front), $20 monthly; Max $100/mo; Ultra $200/mo | confirmed (V) | "$17 Per month with annual subscription discount ($200 billed up front). $20 if billed monthly."; "Max $100 Per month"; "Ultra $200 Per month" | https://claude.com/pricing | none |
| Gemini (vision) | Free $0; AI Plus $4.99; AI Pro $19.99; AI Ultra $99.99 or $199.99 per month | confirmed (V) | "$0/ month with a Google Account"; "$4.99/ month"; "$19.99/ month"; "$99.99/ month: 5x higher usage limits vs. AI Pro"; "$199.99 / month: 20x" | https://gemini.google/subscriptions/ | none |
| ChatGPT (vision) | Free plan with "Unlimited text chats with GPT-6", "Limited messages with uploads"; paid amounts not in page text | confirmed (V) | "Unlimited text chats with GPT-6"; "Limited messages with uploads"; no dollar figure anywhere in the rendered page or 1.26 MB of HTML | https://chatgpt.com/pricing/ | Added from OpenAI's help center: ChatGPT Plus "Price: $20/month (billed monthly)." https://help.openai.com/en/articles/6950777-what-is-chatgpt-plus |
| Real Authentication | $30 basic; +$10 certificate; +$30 1-hour; +$20 12-hour; +$20 valuation; +$20 identification; +$10 age; +$25 mailed card; Shopify plugin | confirmed (V) | "All authentications start at a base price of $30"; "1 HOUR TURNAROUND +$30"; "12 HOUR TURNAROUND +$20"; "FAIR MARKET VALUATION +$20"; "IDENTIFICATION +$20"; "AGE +$10"; "MAILED AUTHENTICITY CARD +$25"; "SHOPIFY PLUGIN" | https://realauthentication.com/services/ | none. Also listed: Hermès fee +$10, extra expert +$10. Luxury fashion only. |
| Entrupy | Petit $139/mo, 25 tokens, 1 Token = $5.60; Moyen $599/mo; Grand $1049/mo; yearly saves 10% | confirmed (V) | "Monthly / Yearly (Save 10%)"; "Petit $139/mo"; "25 authentication tokens included per month"; "1 Token = $5.60"; "Moyen $599/mo"; "Grand $1049/mo" | https://www.entrupy.com/pricing/ | Figures shown on the Monthly toggle. Hardware requirement not stated on this page; "Using your device and the Entrupy app". Far over budget. |
| Etsy 20-year vintage rule | Vintage means at least 20 years old | unreadable (U) | "FETCH FAILED ... HTTP 403" for /legal/creativity; help center search for "vintage 20 years" returned unrelated articles | https://www.etsy.com/legal/creativity ; https://help.etsy.com/hc/en-us/search?query=vintage+20+years | Read from Ricky's browser. |
| JSA (James Spence Authentication) | Fees unknown; Florida office | unreadable for fees (U); Florida office confirmed (V) | Home page shows "FL: 9543808670"; fee route returns "Oops - Error! NG04002: 'authentication-fees'" | https://www.spenceloa.com/authentication-fees ; https://www.spenceloa.com/#/authentication-fees | Fee page is broken for this fetcher on both routes. Call the FL number or read in a browser. |
| Antique Identifier - Trove (iOS) | Pro $9.99 per week; $29.99 per Yearly; no ratings | confirmed (V) | "Antique Identifier Trove Pro: $9.99 per week"; "$29.99 per Yearly (best value)"; "This app hasn't received enough ratings or reviews to display an overview." | https://apps.apple.com/us/app/antique-identifier-trove/id6747611925 | none |
| ThriftCheck (iOS) | 3-day trial then $4.99/week; 7 ratings; inaccuracy complaint | confirmed (V) | "ThriftCheck offers a 3-day free trial, then $4.99/week auto-renewing."; "7 RATINGS"; review titled "Not accurate" | https://apps.apple.com/us/app/thriftcheck-vintage-resale-ai/id6762850899 | none |
| Antique Identifier - Antiquer (iOS) | Weekly USD 4.99 with 3-day trial; free users 2 IDs per day; 2 ratings | confirmed (V) | "Weekly: USD 4.99 per week, with a 3-day free trial."; "Free users receive 2 identifications per day."; "2 RATINGS" | https://apps.apple.com/us/app/antique-identifier-antiquer/id6764046845 | Omission: "Annual: USD 39.99 per year (about USD 0.77 per week)". |
| TinEye | Free for non-commercial use; plans page needs JavaScript | confirmed (V), plans unreadable | "TinEye is free for non-commercial use."; extensions "work with the latest stable builds of Firefox, Chrome, Edge, and Opera"; /plans returned an error page | https://tineye.com/faq ; https://tineye.com/plans | Gotcha: a resale shop is commercial use, so the free tier does not cover Hollie. Paid price still unknown. |

## 2. What the first agent got wrong

1. Kovels membership price. Recorded as "not found (join and pricing pages 404)". The vendor's subscriptions URL redirects to an offers page that prices "Kovels All Access Online" at $59.99 per year and "Kovels All Access + Print" at 79.99 per year. The free marks guide pages and the free Kovels Komments newsletter are unchanged, so the pick stands.
2. WorthPoint price source. Labelled "about $19.99 monthly per third-party tracker dated 2026-03-21". The same figure, with the full bundle list, is on Apple's own App Store listing for the WorthPoint app today: MARKS Premium Monthly $19.99, MARKS Premium Annual $99.99, Price Guide Monthly $26.99, Price Guide + MARKS Monthly $37.99. The vendor's pricing page still returns 403, so web prices remain unconfirmed.
3. PSA/DNA tier. The pick says "single-signer tier $10 to $500" for a photo signed by Scotty Moore and D.J. Fontana. Two signers means the "2 Signatures" column: $20 to $500, priced off the premier (higher-priced) signer. Items declared at $1,000 or more pay a surcharge starting at $40. Authenticating the photograph itself is a separate Original Photograph service ($50 for $999 or less) that cannot be expedited.
4. ChatGPT paid price. Recorded as "amounts not in page text". True of chatgpt.com/pricing, but OpenAI's help center states Plus is "$20/month (billed monthly)". Minor gap, not an error.
5. Antiquer. Omitted the annual option: USD 39.99 per year. Weekly figure and free tier were right.
6. TinEye. The free tier was recorded as "Non-commercial use only" without saying that this excludes a shop. A resale business is commercial use. Fit was already low.
7. Replacements.com, Etsy /legal/creativity and the JSA fee page were correctly flagged U. All three still fail from this container today, so those flags were right.

Everything else checked out: Google Lens, Bing Visual Search, the four marks sites, VFG, FTC RN, Collectors Weekly, Claude, Gemini, Real Authentication, Entrupy, Trove and ThriftCheck all match the vendor pages.

## 3. Gaps and pages that would not load

- https://www.replacements.com/identify.htm and /services.htm: HTTP 403 (browser and curl).
- https://www.worthpoint.com/pricing: HTTP 403. Prices taken from Apple's listing instead.
- https://www.etsy.com/legal/creativity: HTTP 403. help.etsy.com loads, but a search for "vintage 20 years" did not surface the policy. The one article ID tried (115015663347) is the listing-images article, not the what-can-I-sell article.
- https://www.spenceloa.com/authentication-fees and the #/ hash route: Angular error NG04002, no fees rendered.
- https://tineye.com/plans: error page. FAQ loaded.
- Not checked today (lower fit, time): Apple Visual Look Up, Yandex, Pinterest Lens, LiveAuctioneers, Invaluable, Marks4Antiques, Beckett, Epperson, LegitGrails, the Eames/Knoll/Vitra/Stiffel/Lighting New York/1stDibs pages, ResalePal, ThriftAI, Glass Encyclopedia, 925-1000.com, NDGA.

## 4. Sources (every URL fetched today)

https://search.google/ways-to-search/lens/
https://apps.apple.com/us/app/google/id284815942
https://www.kovels.com/marks-identification-guide/
https://www.kovels.com/subscribe/ (redirected to https://my.antiquetrader.com/pubs/WS/AQT/antique_trader_digital.jsp)
https://www.kovels.com/subscriptions/ (redirected to https://subscribe.kovels.com/loading.do?omedasite=AQT_LandOffer)
https://www.thepotteries.org/mark/index.htm
https://www.porcelainmarksandmore.com/
https://www.silvercollection.it/
https://www.20thcenturyglass.com/
https://vintagefashionguild.org/resources/vintage-label-resource/
https://rn.ftc.gov/ (redirected to https://rn.ftc.gov/rns)
https://www.collectorsweekly.com/stories
https://www.replacements.com/identify.htm (403)
https://www.replacements.com/services.htm (403)
https://www.psacard.com/pricing/autographs
https://pages.worthpoint.com/pages/welcome-landing-fb/
https://www.worthpoint.com/pricing (403)
https://apps.apple.com/us/app/worthpoint/id1472512649
https://claude.com/pricing
https://gemini.google/subscriptions/
https://chatgpt.com/pricing/
https://help.openai.com/en/articles/6950777-what-is-chatgpt-plus
https://realauthentication.com/services/
https://www.entrupy.com/pricing/
https://www.etsy.com/legal/creativity (403)
https://help.etsy.com/hc/en-us/articles/115015663347 (loaded, wrong article: listing images)
https://help.etsy.com/hc/en-us/search?query=vintage+20+years
https://www.spenceloa.com/authentication-fees (route error)
https://www.spenceloa.com/#/authentication-fees (route error)
https://apps.apple.com/us/app/antique-identifier-trove/id6747611925
https://apps.apple.com/us/app/thriftcheck-vintage-resale-ai/id6762850899
https://apps.apple.com/us/app/antique-identifier-antiquer/id6764046845
https://tineye.com/plans (error page)
https://tineye.com/faq
https://explore.microsoft.com/en-us/bing/visual-search/
