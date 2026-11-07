# Lane 05: Identification and authentication tools for Holliewood and Vine

Date 2026-11-07. Author: research subagent (lane 05-identification).
Question: Which tools identify a vintage piece (maker, era, pattern, material) and check authenticity, and what do they cost?
Legend: V = vendor page read today (2026-11-07) with the fetch script; U = unverified (search snippet, third-party tracker, memory, or the page would not load).
Scope note: sold-price comps and sourcing are other lanes. This lane covers "what is it, who made it, when, and is it real".
Method note: the WebSearch budget for the whole workflow ran out partway through this lane, so the second half of the sweep used direct vendor URLs only. About 90 URL reads were attempted; roughly 55 returned a readable vendor page. Bot walls hit: worthpoint.com, replacements.com, etsy.com, marks4antiques.com, 925-1000.com, beckett.com, vitra.com, openai.com and help.openai.com. Unreachable through the proxy: glassencyclopedia.com, eppersonauthentication.com, help.worthpoint.com.

## 0. Bottom line

- The best identification tool for Hollie's stock is free and already on her phone: Google Lens inside the Google app (iPhone) and in Chrome on the Windows PC. It handles lamps, art, glass patterns and furniture silhouettes well enough for a first guess. Everything after that is checking the guess.
- Marks are the proof layer, and the good marks references are free: Kovels' marks identification guides (free pages, no login), thepotteries.org (Staffordshire marks, over 2000 makers), porcelainmarksandmore.com (German porcelain), silvercollection.it (hallmarks by country, including USA sterling) and 20thcenturyglass.com (glass encyclopaedia and database). Kovels itself warns that "marks are often forged and changed".
- For the 80s and 90s fashion, the Vintage Fashion Guild Label Resource (free, 1349 label entries) plus the FTC RN database (free, government) date and attribute a garment in a few minutes.
- WorthPoint is the only paid marks database worth a look (150,000 marks, autographs, patterns and symbols per its own landing page), but its pricing pages are bot-walled; a third-party App Store tracker last saw MARKS Premium at $19.99 monthly in March 2026 (U). Start the free trial only when a specific unidentified mark is blocking a listing.
- The AI "antique identifier" apps in the App Store are weekly-billed, sit in the Entertainment category, have between zero and two ratings each, and one thrift-scanner review reads "Lens is better and faster". Skip them. Use Claude or Gemini free tiers to brainstorm hypotheses instead, and treat the output as a lead, not proof: both vendors say in writing that their assistants make mistakes.
- Authentication proper is item-specific and paid. The Elvis photo signed by Scotty Moore and D.J. Fontana goes to PSA/DNA: single-signer autograph authentication is tiered from $10 to $500 by signer, two signatures add roughly $10 to $25 at the low tiers, the Premium Letter upgrade is $15 for items priced under $50, and turnaround is about 30 business days. The exact tier for those two signers needs the interactive lookup on PSA's page (U).
- Luxury-fashion authenticators (Real Authentication from $30 an item, LegitGrails "as low as $11 each" with bulk credits, Entrupy from $139 a month) only pay off for a designer handbag or sneaker. Hollie's 80s and 90s fashion is not that stock. Real Authentication's $20 "Identification" and $10 "Age" add-ons are the one interesting option if a designer piece shows up.
- Etsy's 20-year vintage rule could not be read today (every Etsy page returned 403 or 405). The rule is well known and was quoted by the search engine from Etsy's House Rules ("20+ years old"), but it is marked U here. eBay has no official vintage age definition that could be found; community posts say eBay does not enforce one (U).

## 1. Comparison table

| Tool | What it does | Price (verbatim quote) | Free tier | Platform | Fit for Hollie | V/U | Source URL |
|---|---|---|---|---|---|---|---|
| Google Lens | Visual search from camera, photo or screenshot; shop, identify artwork, plants, landmarks | Free. "Use your camera, an image, or a screenshot to search." Google app: "Free · In-App Purchases", 5.3M ratings | Yes, whole product | iOS and Android (Google app), Chrome desktop, Android camera | High: first-pass ID of lamps, art, glass, furniture | V | https://search.google/ways-to-search/lens/ ; https://apps.apple.com/us/app/google/id284815942 |
| Bing Visual Search | Reverse image and object search | Free. "Free Visual Search Tool"; "Windows 11 now allows users to capture screenshots and perform instant image lookups directly from the Snipping Tool." | Yes | Web, Windows 11 Snipping Tool, Edge, Chrome extension | Medium: second opinion on the PC | V | https://explore.microsoft.com/en-us/bing/visual-search/ |
| Apple Visual Look Up | Built-in iPhone Photos identification (art, plants, pets, landmarks) | Free with iOS | Yes | iOS | Medium: convenient but narrow | U: Apple guide URL redirected to the iPhone User Guide front page three times; feature page not read | https://support.apple.com/guide/iphone/welcome/ios |
| TinEye | Reverse image search for exact and altered copies | "TinEye is free for non-commercial use." Paid plans page needs JavaScript and would not render; price unknown | Yes, non-commercial only | Web, browser extension | Low: "it cannot recognize the contents of any image"; finds copies of a photo, not what the object is | V (FAQ), U (plan prices) | https://tineye.com/faq ; https://tineye.com/plans |
| Yandex Images | Reverse image search | Free | Yes | Web | Low to medium: useful for European glass and ceramics; Russian service, data terms not read | V (page exists), U (terms) | https://yandex.com/images/ |
| Pinterest Lens | In-app camera search for similar pins | Free. "Lens lets you discover ideas inspired by anything you point your Pinterest camera at." | Yes | iOS, Android (Pinterest app) | Low: finds look-alikes and styling, not makers | V | https://help.pinterest.com/en/article/pinterest-lens |
| ChatGPT (vision) | Describe a photo, suggest maker, era, style | Free plan: "Unlimited text chats with GPT-6", "Limited messages with uploads". Paid: "Go, Plus, Business, and Enterprise ... priced per user per month"; dollar amounts not present in page text | Yes | Web, Windows, Mac, iOS, Android | Medium: hypotheses only; verify against marks | V (plans), U (prices, caveat page walled) | https://chatgpt.com/pricing/ |
| Claude (vision) | Same | Free "$0". Pro "$17 Per month with annual subscription discount ($200 billed up front). $20 if billed monthly." Max $100/month, Ultra $200/month | Yes | Web, Windows, Mac, iOS, Android | Medium: hypotheses only; already planned for listing drafts | V | https://claude.com/pricing ; caveat: https://support.claude.com/en/articles/8525154-claude-is-providing-incorrect-or-misleading-responses-what-s-going-on |
| Gemini (vision) | Same | Free "$0/ month with a Google Account"; Google AI Plus "$4.99/ month"; Google AI Pro "$19.99/ month"; AI Ultra "$99.99/ month" and "$199.99 / month" | Yes | Web, iOS, Android | Medium: hypotheses only | V | https://gemini.google/subscriptions/ ; caveat: https://support.google.com/gemini/answer/13275745 |
| WorthPoint (Marks Gallery, Price Guide) | Visual database of makers' marks, autographs, patterns and symbols; price guide | Web pricing pages return 403. Landing page: "START YOUR FREE TRIAL NOW". Third-party App Store tracker (2026-03-21): "MARKS Premium Monthly $19.99", "Price Guide Monthly $26.99", "Price Guide + MARKS Monthly $37.99", "MARKS Premium Annual $99.99" | Free trial only | Web, iOS app (117 ratings), Android | Medium to high once volume justifies it; marks database is the draw | U (prices), V (features, trial) | https://pages.worthpoint.com/pages/welcome-landing-fb/ ; https://apps.apple.com/us/app/worthpoint/id1472512649 ; https://apppricinglab.com/iap/apple/1472512649 |
| Kovels marks identification guides | Articles and lists: pottery and porcelain marks, silver hallmarks, English registry marks, Sevres date marks | Free pages. Member database ("Look For Your Mark", "Dictionary of Marks") price not found; /join and /pricing are 404; /subscribe redirects to the magazine | Yes, guide pages and weekly newsletter | Web | High: free, written for exactly this stock | V (guides), U (membership price) | https://www.kovels.com/marks-identification-guide/ ; https://www.kovels.com/membership/ |
| Kovels Antique Trader magazine | Monthly magazine with "Dictionary of Marks" column and sales reports | "Print Only 1 year (12 issues) for just $29.95"; "Digital Only ... $24.95"; "Print + Digital ... $34.95"; auto-renews | No | Print, digital | Low to medium: education, not a lookup tool | V | https://www.kovels.com/subscribe (redirects to my.antiquetrader.com) |
| Replacements.com Pattern Identification | Staff researchers identify china, crystal and flatware patterns from photos | All pages 403 today. Search snippet of the vendor services page: "free Pattern Identification Service" | Yes (per snippet) | Web, email | High for pink depression glass, cut crystal and barware patterns, if the snippet holds | U | https://www.replacements.com/identify.htm ; https://www.replacements.com/services.htm |
| Vintage Fashion Guild Label Resource | Vintage clothing labels with company histories; union label section | "free, public educational project". "1 - 48 of 1349 results" | Yes | Web | High for the 80s and 90s fashion | V | https://vintagefashionguild.org/resources/vintage-label-resource/ ; https://vintagefashionguild.org/resources/item/label/ilgwu/ |
| FTC RN database | Look up the company behind an RN number on a garment label | Free. "Businesses can use a registered identification number (RN) in place of a company name on the required label." | Yes | Web | High for fashion attribution and dating | V | https://rn.ftc.gov/ |
| thepotteries.org marks index | Staffordshire pottery marks, trade names, initials, registry diamonds, Royal Arms | Free. "Identify makers, dates and marks from North Staffordshire"; "list of over 2000" manufacturers | Yes | Web | High for English ceramics and figurines | V | https://www.thepotteries.org/mark/index.htm |
| porcelainmarksandmore.com | German and related porcelain marks and factory histories | Free. "offers a lot of useful information for free (no ads, no pop-ups, no cookies...)". "A few factory entries ... can only be viewed by site members." | Yes, most entries | Web | High for German figurines and porcelain | V | https://www.porcelainmarksandmore.com/ |
| silvercollection.it | Hallmarks (sterling) and silverplate marks by country, incl. USA | Free. "a 1500 pages richly illustrated website". Disclaimer: "we cannot guarantee its accuracy and reliability" | Yes | Web | High for barware, cocktail shakers, decanter collars | V | https://www.silvercollection.it/ |
| 925-1000.com | Online encyclopedia of silver marks | 403 today | Unknown | Web | High if reachable from Ricky's PC (it is a common free reference) | U | https://www.925-1000.com/ |
| 20thcenturyglass.com | Glass encyclopaedia, galleries and searchable glass database (UK dealer) | Free. "Browse our extensive identification guide to antique & collectable vintage glass." | Yes | Web | High for art glass, Murano, Scandinavian; medium for American depression glass | V | https://www.20thcenturyglass.com/ |
| Glass Encyclopedia (glassencyclopedia.com) | Glass ID reference | Host unreachable through the proxy (tunnel failed) | Unknown | Web | Unknown | U | https://www.glassencyclopedia.com/ |
| National Depression Glass Association | Association site, members' glass photos, convention | "American made Depression Glass is glassware generally made in the period 1929-1939." Membership price not captured | Partly | Web | Medium: context and community for the pink depression glass | V | https://www.ndga.net/ |
| Collectors Weekly Show & Tell | Post an item, community identifies and comments | Free. "Share your favorites on Show & Tell. Post an item" | Yes | Web | Medium: slow, but real humans; good for odd lamps and figurines | V | https://www.collectorsweekly.com/stories |
| LiveAuctioneers Price Results | Past auction lots with descriptions (catalogue text is an ID aid) | Page shows "Price Results" and "Log In"; access terms not stated in text read | Account | Web, iOS, Android | Medium: catalogue descriptions teach the vocabulary | V (exists), U (access terms) | https://www.liveauctioneers.com/price-results/ |
| Invaluable Price Archive | Same idea | Home page shows "Price Archive" nav; /price-archive/ is 404; terms not read | Unknown | Web | Medium | V (exists), U (terms) | https://www.invaluable.com/ |
| Eames.com authenticity article | How to check Eames and Herman Miller labels and parts | Free. "Labels are the first port of call when checking Eames authenticity." | Yes | Web | High if an Eames or Herman Miller piece is on hand | V | https://eames.com/en/articles/shellauthenticity |
| Herman Miller (hermanmiller.com) | Maker site | No identification or authenticity page found; Eames Lounge product page has no label guidance in its text | n/a | Web | Low as an ID tool | U (no page) | https://www.hermanmiller.com/products/seating/lounge-seating/eames-lounge-chair-and-ottoman/ |
| Knoll The Archive | Interactive timeline of people, objects, events | Free. "Spanning over a century, explore Knoll's robust history" | Yes | Web (modern browser) | Low to medium: dating a design, not authenticating a piece | V | https://www.knoll.com/the-archive |
| Vitra (Wiggle Side Chair) | Maker page for the Gehry chair | 403 on both URLs tried | n/a | Web | Needed if the shop has a Wiggle; could not be read | U | https://www.vitra.com/en-us/product/wiggle-side-chair |
| Stiffel (stiffel.com) | Maker site, company history | "family-owned business founded in 1932", Linden, New Jersey. No marks guide on the site | Yes | Web | Medium: confirms maker still exists; dating needs a secondary guide | V | https://stiffel.com/ |
| Lighting New York Stiffel markings guide | Retailer article on where Stiffel marks sit | Free. "there isn't a single, comprehensive database for all Stiffel lamp markings" | Yes | Web | Medium: tells you where to look (base underside, socket, paper label) | V (retailer, not maker) | https://lightingnewyork.com/k/lighting/wall-lights/lamps/stiffel-lamp-markings |
| 1stDibs Q&A: Frederick Cooper | Dealer-platform answer on FC marks | Free. "Nearly all pieces ... feature an 'FC' or 'F' marking ... on the bottom of the base, the turn switch or the socket." | Yes | Web | Medium: one quick check for the urn lamp | V (marketplace, not maker) | https://www.1stdibs.com/answers/how-do-you-identify-a-frederick-cooper-lamp/ |
| PSA/DNA autograph authentication | Expert autograph authentication, letters, encapsulation | Single-signed tiers "$10 ... $500" by signer; 2 signatures from "$20"; "Upgrades to full Premium Letters of Authenticity are available for an additional $15" under $50; "Turnaround time is approximately 30 business days"; expedited "$75 10 Business Days" | No | Mail-in with web submission form | High for the Elvis photo signed by Scotty Moore and D.J. Fontana; signer tier needs the interactive lookup | V (tiers), U (these signers' tier) | https://www.psacard.com/pricing/autographs |
| PSA Original Photograph authentication | Confirms a photo is a period original print | "$999 or less $50"; "$1,000 - $2,499 $100"; 30 business days | No | Mail-in | Medium: only if buyers ask whether the Elvis print is period | V | https://www.psacard.com/pricing/autographs |
| JSA (James Spence Authentication) | Autograph authentication, NJ and FL offices | Fee page is a JavaScript app and rendered no fees. Phones on page: "NJ: 9738981300 FL: 9543808670" | No | Mail-in, events | High as a second option; Florida office is a plus; price unknown | U | https://www.spenceloa.com/authentication-fees |
| Beckett Authentication Services | Autograph authentication | Cloudflare block on every URL | No | Mail-in | Medium; price unknown | U | https://www.beckett-authentication.com/ |
| Epperson Authentication (REAL) | Music autograph specialist | Host unreachable | No | Mail-in | Potentially high for Elvis-circle signatures; unknown | U | https://www.eppersonauthentication.com/ |
| Real Authentication | Photo-based luxury authentication with ID, age and valuation add-ons | "$30 BASIC AUTHENTICATION"; "+$10" Certificate of Authenticity; "+$30" 1 hour; "+$20" 12 hour; "+$20" Fair Market Valuation; "+$20" Identification; "+$10" Age; "+$25" mailed Authenticity Card | No | Web (mobile and desktop); Shopify plugin listed in nav | Medium: pay per designer item only | V | https://realauthentication.com/services/ |
| LegitGrails | Photo-based authentication: handbags, clothing, shoes, jewelry, watches, eyewear, toys, trading cards | "as low as $11 each" with credit top-ups; "in as little as 30 minutes"; single-item price not shown without starting an order | No | Web (Shopify store) | Medium-low: designer fashion only | V (quotes), U (per-item list price) | https://legitgrails.com/ |
| Entrupy | AI plus imaging device authentication for luxury goods | "Petit $139/mo 25 authentication tokens included per month ... 1 Token = $5.60"; "Moyen $599/mo"; "Grand $1049/mo" | No | iOS app plus Entrupy hardware | Low: subscription far over budget; luxury categories only | V | https://www.entrupy.com/pricing/ |
| Authenticate First | Fashion authentication | Not fetched (search budget exhausted before this seed) | Unknown | Web | Unknown | U | n/a |
| Marks4Antiques | Paid makers' marks dictionary and price guides | 403 on home and pricing. Search snippet of contact page: "minimum subscription is 30 days", "don't offer free trials" | No | Web | Low: cannot be read; no trial | U | https://marks4antiques.com/ |
| Antique Identifier - Trove (iOS) | AI photo ID with "estimated market value" | "Antique Identifier Trove Pro: $9.99 per week"; "$29.99 per Yearly" | Limited | iOS | Low: "hasn't received enough ratings"; privacy policy on a Google Sites page | V | https://apps.apple.com/us/app/antique-identifier-trove/id6747611925 |
| Antique Identifier - Antiquer (iOS) | AI photo ID | "Weekly: USD 4.99 per week, with a 3-day free trial." "Free users receive 2 identifications per day." 2 ratings | 2 IDs/day | iOS | Low | V | https://apps.apple.com/us/app/antique-identifier-antiquer/id6764046845 |
| Antique Snap: Identifier (iOS) | AI photo ID | Free with in-app purchases; prices not in listing text; category Entertainment; 1 rating | Unknown | iOS, iPad | Low | V | https://apps.apple.com/us/app/antique-snap-identifier/id6763597726 |
| Antique Identifier: Relicanica (iOS) | AI photo ID | Free with in-app purchases; Entertainment; no ratings; policy on Google Sites | Unknown | iOS, iPad | Low | V | https://apps.apple.com/us/app/antique-identifier-relicanica/id6752642652 |
| Antique Identifier: Appraiser (iOS) | AI photo ID | Free with in-app purchases; Entertainment; no ratings | Unknown | iOS | Low | V | https://apps.apple.com/us/app/antique-identifier-appraiser/id6759754170 |
| Antique Identifier AI App (id6736668751) | AI photo ID | 404 in the US App Store today; search snippet: "Monthly Subscription $9.99" | Unknown | iOS | Low | U | https://apps.apple.com/app/id6736668751 |
| ResalePal (iOS) | Photo to resale price across eBay, StockX, Depop, Poshmark, Mercari, Facebook Marketplace, GOAT | "Scan your first item for free - no account required." Pro price not in listing text. 109 ratings, 4.9 | First scan | iOS, iPad | Low to medium: pricing tool, not an identifier (other lane) | V | https://apps.apple.com/us/app/resalepal-resale-scanner/id6762302637 |
| ThriftCheck (iOS) | Photo to resale prices from eBay, Mercari, Poshmark, Etsy; "BUY or SKIP" | "3-day free trial, then $4.99/week auto-renewing" | Trial | iOS | Low: 7 ratings; top review titled "Not accurate" | V | https://apps.apple.com/us/app/thriftcheck-vintage-resale-ai/id6762850899 |
| Thrifted (iOS) | Clothing scan, era and rarity, wardrobe tracker | Free with in-app purchases; price not in listing text; 23 ratings | Unknown | iOS | Low: clothing only | V | https://apps.apple.com/us/app/thrifted-scan-price-clothes/id6757867446 |
| ThriftAI: Profit Identifier (Android) | Photo to resale potential | Free with in-app purchases; 18.5K reviews. Review: "charged the $9.99 monthly fee almost immediately" | Trial | Android | Low: billing complaints; "Lens is better and faster" (review) | V | https://play.google.com/store/apps/details?id=com.fulcra.thriftai&hl=en_US |
| Etsy 20-year vintage rule | Marketplace definition | All Etsy pages 403/405 today. Search snippet of House Rules: vintage is "20+ years old" | n/a | n/a | Governs every "vintage" tag; must be re-verified from Ricky's browser | U | https://www.etsy.com/legal/creativity |
| eBay vintage definition | Marketplace definition | No official page found; community posts say eBay does not enforce an age | n/a | n/a | Use the 20-year convention anyway | U | https://community.ebay.com/t5/Ask-a-Mentor/what-is-vintage/qaq-p/26888472 (not fetched) |

## 2. Notes per tool

### Visual search (free)
- Google Lens (V). The Lens page lists "Shop what you see", "learn more about artwork, murals, and landmarks", "Search as you browse" in Chrome desktop, and a new create mode that restyles photos (ignore that one). The Google app is free on the App Store with 5.3M ratings. No licence issue for commercial use of search results; Lens results are leads, not proof.
- Bing Visual Search (V). Free. Built into Windows 11 Snipping Tool and Edge, and a Chrome extension. Handy on the PC when Lens misses.
- Apple Visual Look Up (U). Apple's guide URL redirected to the iPhone User Guide welcome page on every attempt, so the feature page was not read. It identifies art, plants, pets and landmarks from the Photos app on supported iPhones (memory, U).
- TinEye (V). The FAQ is explicit: "TinEye finds exact and altered copies... it cannot recognize the contents of any image." Useful only to find where a product photo already appears online (for example to see if a listing photo was lifted). "TinEye is free for non-commercial use"; a reseller's use is commercial, so strictly a paid plan applies, and the plans page would not render (U).
- Yandex Images (V exists). Strong for European objects. Terms and data handling not read (U).
- Pinterest Lens (V). Finds similar pins, not makers. Camera inside the Pinterest app.

### Generative AI (free tiers)
- All three vendors say their assistants err. Anthropic: "Claude can occasionally produce responses that are incorrect or misleading... known as 'hallucinating'" (V). Google: "Gemini Apps can make mistakes. When using Gemini Apps, double-check responses" (V). OpenAI's help and blog pages returned 403 today (U). Use them to turn a photo into a vocabulary list ("hollywood regency", "bouillotte", "zanfirico") and candidate makers, then confirm with a mark.
- Prices (V): Claude Free $0, Pro $17 a month on annual ($200 up front) or $20 monthly. Gemini Free $0, Google AI Pro $19.99 a month. ChatGPT Free exists with "Limited messages with uploads"; paid dollar amounts did not appear in the page text (U).
- Terms gotcha: none of these are authentication; never cite an AI answer as attribution in a listing.

### Marks and pattern references
- Kovels (V). Four free guide articles reached today: Sevres marks, Silver Identification Guide, English Registry Marks, Antique Pottery & Porcelain Marks. Kovels' own line: "sometimes it's unreliable because marks are often forged and changed." The member database ("Look For Your Mark", "Readers Q&A on Marks", "Dictionary of Marks") sits behind "JOIN NOW"; /join and /pricing are 404 and /subscribe lands on the Antique Trader magazine order page ($24.95 to $34.95 a year, auto-renewing). Membership price: not found (U). Free weekly newsletter "Kovels Komments" includes marks Q&A.
- WorthPoint (V features, U prices). worthpoint.com/pricing and /plans return 403 to this container, and help.worthpoint.com refused the connection. The marketing landing page says "more than 845 million 'sold for' prices" and "WorthPoint Marks Gallery - a resource of more than 150,000 makers' marks, autographs, patterns, and symbols", with a free trial. The App Store listing confirms the marks search ("Search our visual database of makers' marks, autographs, patterns, and symbols") and "Subscription automatically renews on selected term basis (monthly or annual)". App Store reviews (117 ratings) complain repeatedly about login lockouts and the app forgetting sessions; one says "if you are a reseller you really have no other options that allow you to see old eBay records". Third-party IAP tracker (U, 2026-03-21): MARKS Premium Monthly $19.99, MARKS Premium Annual $99.99, Price Guide Monthly $26.99, Price Guide + MARKS Monthly $37.99, Price Guide Annual $249.99, Price Guide + MARKS Annual $399.99. Re-verify from Ricky's browser before paying.
- Replacements.com (U). Every page returned 403. The search engine quoted the vendor's services page as offering a "free Pattern Identification Service" with "full-time researchers", and the request form at /identify.htm. Reported scale: about 3,000 requests a week (interview, U). For pink depression glass and cut crystal this is the strongest free pattern ID lead in the lane; Ricky should open the page himself.
- thepotteries.org (V). Free. Marks by category (Stafford Knot, beehive), trade names, initials, unidentified marks, dating pottery, design registration diamonds, British Royal Arms.
- porcelainmarksandmore.com (V). Free, German-run, "no ads, no pop-ups, no cookies". Some factory entries are members-only for a fee (amount not read); individual questions still answered free.
- silvercollection.it (V). Free. Hallmarks by country including "USA (sterling)" and silverplate marks. Carries its own disclaimer on accuracy.
- 925-1000.com (U). 403 today. Commonly used free silver marks encyclopedia; try from Ricky's PC.
- 20thcenturyglass.com (V). UK dealer running a free encyclopaedia and a "vast reference database of vintage collectable glass items". Good for Murano, Scandinavian, British art glass; thinner on American depression glass.
- Glass Encyclopedia (U). Host unreachable.
- NDGA (V). Defines American depression glass as "generally made in the period 1929-1939". Members' glass photos and a gift shop; membership price not captured.
- Marks4Antiques (U). 403. Search snippet of its contact page: 30-day minimum, no free trials; its terms disclaim accuracy. Skip unless Ricky wants to compare it with WorthPoint himself.

### Fashion labels
- VFG Label Resource (V). Free, 1349 label entries with histories; ILGWU entry links to a union labels section. Donation requested, no paywall. Fits the 80s and 90s stock exactly.
- FTC RN database (V). Free government lookup. The RN number on a care label maps to the company; the FTC says an RN "is not required", so absence proves nothing.

### Furniture and lighting makers
- Eames.com (V). "Labels are the first port of call"; copying of labels is "extremely rare" but "it is always good to look out for other tells". Herman Miller's own site offered no ID page (U); Knoll's archive is a timeline, not an authentication tool (V); Vitra's Wiggle page is bot-walled (U). If the Gehry Wiggle chair is on hand, Vitra's marking should be checked from Ricky's browser.
- Stiffel (V). Maker site confirms 1932 founding and current production in Linden, NJ; no marks guide. The retailer guide (V) says marks sit on the base underside or socket, stamped or on paper labels, and that no comprehensive Stiffel marks database exists.
- Frederick Cooper (V, 1stDibs Q&A). "FC" or "F" on the base, turn switch or socket. Date codes are unreliable (search snippet, U).
- Chandelier and lighting ID: no dedicated resource reached today (gap).

### Autograph authentication (for the Elvis photo signed by Scotty Moore and D.J. Fontana)
- PSA/DNA (V). Price depends on the signer's tier; the table runs $10, $20, $25, $30, $35, $45, $50, $75, $100, $150, $200, $250, $300, $500 for a single signature, and the two-signature column starts at $20. "To determine the price of your multi-signed item, look up the price for the premier autograph." Items under $50 get a 3x3 certificate; a full Premium Letter is "an additional $15". Declared value of $1,000 or more adds $40 and up. Turnaround "approximately 30 business days"; expedited 10 business days is $75 per order of 1 to 5 items. A separate "Original Photograph Authentication" service ($50 for declared value $999 or less) certifies the print itself as period; "For photos that have live signatures, please use the Original Photo & Autograph Submission Form." The signer lookup (?name=Moore) did not return the tier in page text (U).
- JSA (U). Angular app; fee page rendered only navigation. Florida office phone 954-380-8670 (V).
- Beckett (U). Cloudflare block.
- Epperson/REAL (U). Unreachable. Known as the music specialist; worth a call from Ricky.

### Luxury authentication (designer fashion only)
- Real Authentication (V). $30 base, two or more experts, 24-hour turnaround. Add-ons: Certificate +$10, 1-hour +$30, 12-hour +$20, Fair Market Valuation +$20, Identification (style name, material, size) +$20, Age +$10, mailed Authenticity Card +$25. Certificates carry a QR code; "Written Statements serve as an expert opinion needed by PayPal, eBay and credit card companies". Enterprise pricing above 10 items a day. Has a Shopify plugin in its nav (not read).
- LegitGrails (V). "as low as $11 each" with bulk credits and up to 40% off with an account; "in as little as 30 minutes". Categories include Clothing and Toys & Collectibles. Per-item list price not visible without starting an order (U).
- Entrupy (V). $139 a month minimum, hardware plus app, luxury brand tiers (Hermes to Coach). Not for this shop.
- Authenticate First: not reached (gap).

### AI antique identifier and thrift scanner apps
- Pattern across the App Store listings read today (V): weekly billing ($4.99 to $9.99 a week), Entertainment category, zero to two ratings, privacy policies hosted on Google Sites or WordPress, and marketing like "trained on thousands of verified antiques". None names a data source for its "estimated market value". Trove: $9.99 a week or $29.99 a year. Antiquer: $4.99 a week after a 3-day trial, two free IDs a day.
- Thrift scanners are pricing tools (other lane) but overlap here because they also "identify". ThriftCheck's one visible review: "scan the exact same item twice using the same photos and getting 2 different answers." ThriftAI (Android, 18.5K reviews) has billing complaints and a reviewer saying "Lens is better and faster". ResalePal (109 ratings, 4.9) offers the first scan free without an account; Pro price not in text.

### Marketplace vintage definitions
- Etsy (U). Every Etsy URL returned 403 or 405 today. The search engine quoted Etsy's House Rules: vintage items are "20+ years old" and Etsy "may ask for additional photo documentation or information about vintage items in your shop, such as their source, age, designer, or materials." Keep a dating note per item.
- eBay (U). No official age definition found; community threads say eBay does not police the word.

## 3. Recommendation for Hollie

Install or bookmark today (all free):
1. Google app on the iPhone (Lens) and Lens in Chrome on the PC. First pass on everything.
2. Kovels marks identification guides and the free Kovels Komments newsletter. Second pass on ceramics, silver and registry marks.
3. Bookmark folder "Marks": thepotteries.org/mark, porcelainmarksandmore.com, silvercollection.it, 20thcenturyglass.com. Try 925-1000.com and glassencyclopedia.com from the PC; they were walled or unreachable from this container.
4. VFG Label Resource plus rn.ftc.gov for every garment.
5. Collectors Weekly Show & Tell account, for the pieces nothing else names.
6. Claude or Gemini free tier to turn a photo into search vocabulary. Never quote them as attribution.
7. Replacements.com pattern identification form, opened from Ricky's browser, for the pink depression glass, cut crystal and barware. Confirm it is still free on the page before sending photos.

Pay once, item by item:
- PSA/DNA for the Elvis photo. Budget the signer tier (look up "Moore" and "Fontana" on psacard.com/pricing/autographs), plus $15 for the Premium Letter if the tier is under $50, plus return shipping. Expect about 30 business days. Call JSA's Florida office and Epperson as price checks; neither could be read today.
- Real Authentication at $30 plus $20 Identification and $10 Age only if a real designer piece turns up.

Pay monthly only once it earns it:
- WorthPoint MARKS Premium (about $19.99 a month per the third-party tracker, unverified) after the free trial, and only if unidentified marks are blocking listings weekly. Read the App Store reviews about login lockouts first.

Skip:
- All App Store "antique identifier" apps and thrift scanners for identification. Weekly billing, no ratings, no stated data source.
- Entrupy, LegitGrails and Marks4Antiques. Wrong stock, over budget, or unreadable with no trial.
- TinEye for identification. It finds copies of a photo, not the object.

## 4. Gaps and pages that would not load

- worthpoint.com/pricing and /plans: HTTP 403. help.worthpoint.com: connection refused by the proxy. Prices are third-party and dated March 2026.
- kovels.com membership price: /join and /pricing are 404; /subscribe redirects to the magazine; ?p=3684971 loops redirects.
- replacements.com: 403 on /pattern-identification, /identify.htm, /services.htm, /faq.htm.
- etsy.com and help.etsy.com vintage pages: 403, 405 or wrong article; the 20-year rule is U.
- eBay: no official vintage definition page found.
- marks4antiques.com: 403.
- 925-1000.com: 403. glassencyclopedia.com: tunnel failed (both https and http).
- vitra.com Wiggle Side Chair: 403 on two URLs.
- hermanmiller.com: no identification page found; one guessed URL was 404.
- Apple Visual Look Up: three support URLs redirected to the iPhone User Guide front page; one guessed article number was a 2007 security note, another 404.
- openai.com and help.openai.com: 403; ChatGPT paid prices not in page text.
- spenceloa.com (JSA): JavaScript app, fee page shows no fees. beckett-authentication.com and beckett.com: Cloudflare block. eppersonauthentication.com: unreachable.
- tineye.com/plans: requires JavaScript; browser render failed twice.
- Authenticate First, chandelier and lighting ID resources, Google Play antique identifier listings, LiveAuctioneers and Invaluable access terms, NDGA membership price: not reached before the search budget ran out.
- WebSearch budget for the workflow was exhausted mid-lane; six planned searches (JSA fees, Beckett pricing, Epperson, Vitra Wiggle, Knoll labels, Google Play antique identifiers) did not run.

## 5. Sources (every URL fetched today, including failures)

https://www.worthpoint.com/pricing (403)
https://www.worthpoint.com/plans (403)
https://help.worthpoint.com/ (connection refused)
https://apps.apple.com/us/app/worthpoint-vault/id1448347152 (404)
https://apps.apple.com/us/app/worthpoint/id1472512649
https://pages.worthpoint.com/pages/welcome-landing-fb/
https://apppricinglab.com/iap/apple/1472512649 (third party)
https://www.kovels.com/subscribe (redirects to https://my.antiquetrader.com/pubs/WS/AQT/antique_trader_digital.jsp)
https://www.kovels.com/marks-identification-guide/
https://www.kovels.com/membership/
https://www.kovels.com/join (404)
https://www.kovels.com/pricing/ (404)
https://www.kovels.com/shop/
https://kovels.com/?p=3684971 (redirect loop)
https://www.entrupy.com/pricing/
https://realauthentication.com/pricing/ (404)
https://realauthentication.com/services/
https://realauthentication.com/how-it-works/
https://legitgrails.com/pages/pricing
https://legitgrails.com/
https://legitgrails.com/products/handbags-authentication
https://www.psacard.com/services/autographauthentication
https://www.psacard.com/services/autographauthentication/pricing (empty)
https://www.psacard.com/pricing (empty)
https://www.psacard.com/pricing/autographs
https://www.psacard.com/pricing/autographs?name=Moore
https://www.spenceloa.com/pricing
https://www.spenceloa.com/authentication-fees
https://www.spenceloa.com/fees
https://www.beckett.com/authentication/ (blocked)
https://www.beckett-authentication.com/pricing (blocked)
https://www.beckett-authentication.com/ (Cloudflare block)
https://www.beckett.com/authentication/pricing (Cloudflare block)
https://www.eppersonauthentication.com/ (unreachable)
https://www.replacements.com/pattern-identification (403)
https://www.replacements.com/identify.htm (403)
https://www.replacements.com/services.htm (403)
https://www.replacements.com/faq.htm (403)
https://vintagefashionguild.org/label-resource/ (redirects to https://vintagefashionguild.org/resources/vintage-label-resource/)
https://vintagefashionguild.org/label-resource/ilgwu/ (redirects to https://vintagefashionguild.org/resources/item/label/ilgwu/)
https://vintagefashionguild.org/resources/union-labels/ (404)
https://rn.ftc.gov/
https://tineye.com/plans (JS required, not rendered)
https://tineye.com/
https://tineye.com/faq
https://yandex.com/images/
https://help.pinterest.com/en/article/search-with-pinterest-lens (404)
https://help.pinterest.com/en/article/pinterest-lens
https://www.etsy.com/legal/policy/creativity-standards/ (no text)
https://www.etsy.com/legal/creativity (403)
https://www.etsy.com/help/article/4511 (403)
https://www.etsy.com/new-guidelines (405)
https://help.etsy.com/hc/articles/34707360607511 (does not exist)
https://help.etsy.com/hc/en-us/articles/115015663347 (wrong article: images)
https://help.etsy.com/hc/en-us/articles/360000344908 (wrong article: fees)
https://www.vitra.com/en-us/product/details/wiggle-side-chair (403)
https://www.vitra.com/en-us/product/wiggle-side-chair (403)
https://marks4antiques.com/ (403)
https://marks4antiques.com/pricing (403)
https://lens.google/ (redirects to https://search.google/ways-to-search/lens/)
https://apps.apple.com/us/app/google/id284815942
https://support.apple.com/guide/iphone/use-visual-look-up-iph21c2ecdb3/ios (redirected to guide front page)
https://support.apple.com/guide/iphone/iph21c2ecdb3/ios (redirected)
https://support.apple.com/guide/iphone/use-visual-look-up-iph21c2ecdb3/17.0/ios/17.0 (redirected)
https://support.apple.com/guide/iphone/look-up-information-about-whats-in-a-photo-iph21c2ecdb3/ios (redirected)
https://support.apple.com/en-us/102579 (wrong article)
https://support.apple.com/en-us/121704 (404)
https://www.bing.com/visualsearch (redirects to https://explore.microsoft.com/en-us/bing/visual-search/)
https://openai.com/chatgpt/pricing/ (redirects to https://chatgpt.com/pricing/)
https://help.openai.com/en/articles/8313359-is-chatgpt-safe-for-all-ages (403)
https://openai.com/index/chatgpt/ (403)
https://claude.com/pricing
https://support.claude.com/en/articles/8525154-claude-is-providing-incorrect-or-misleading-responses-what-s-going-on
https://gemini.google/subscriptions/
https://support.google.com/gemini/answer/13594961
https://support.google.com/gemini/answer/13275745
https://gemini.google/faq/ (failed)
https://gemini.google/faq (failed)
https://www.glassencyclopedia.com/ (unreachable)
http://www.glassencyclopedia.com/ (unreachable)
https://www.20thcenturyglass.com/
https://www.925-1000.com/ (403)
https://www.silvercollection.it/
https://www.porcelainmarksandmore.com/
https://www.thepotteries.org/mark/index.htm
https://www.ndga.net/
https://eames.com/en/articles/shellauthenticity
https://www.hermanmiller.com/stories/why-magazine/the-value-of-an-original/ (404)
https://www.hermanmiller.com/products/seating/lounge-seating/eames-lounge-chair-and-ottoman/
https://www.knoll.com/the-archive
https://stiffel.com/
https://lightingnewyork.com/k/lighting/wall-lights/lamps/stiffel-lamp-markings
https://www.1stdibs.com/answers/how-do-you-identify-a-frederick-cooper-lamp/
https://www.collectorsweekly.com/
https://www.collectorsweekly.com/stories
https://www.liveauctioneers.com/price-results/
https://www.invaluable.com/
https://www.invaluable.com/price-archive/ (404)
https://apps.apple.com/us/app/antique-identifier-ai-app/id6736668751 (404)
https://apps.apple.com/app/id6736668751 (404)
https://apps.apple.com/us/app/id6747611925 (Trove; resolves to https://apps.apple.com/us/app/antique-identifier-trove/id6747611925)
https://apps.apple.com/us/app/id6752833084 (404)
https://apps.apple.com/us/app/id6759754170 (resolves to https://apps.apple.com/us/app/antique-identifier-appraiser/id6759754170)
https://apps.apple.com/us/app/-/id6763597726 (resolves to https://apps.apple.com/us/app/antique-snap-identifier/id6763597726)
https://apps.apple.com/us/app/-/id6752642652 (resolves to https://apps.apple.com/us/app/antique-identifier-relicanica/id6752642652)
https://apps.apple.com/us/app/-/id6764046845 (resolves to https://apps.apple.com/us/app/antique-identifier-antiquer/id6764046845)
https://apps.apple.com/us/app/id6762302637 (resolves to https://apps.apple.com/us/app/resalepal-resale-scanner/id6762302637)
https://apps.apple.com/us/app/-/id6762850899 (resolves to https://apps.apple.com/us/app/thriftcheck-vintage-resale-ai/id6762850899)
https://apps.apple.com/us/app/id6757867446 (resolves to https://apps.apple.com/us/app/thrifted-scan-price-clothes/id6757867446)
https://play.google.com/store/apps/details?id=com.fulcra.thriftai&hl=en_US
https://play.google.com/store/apps/details?id=com.ruvixlabs.thriftgenius&hl=en_US (404)

Search-engine snippets used only as leads (U): Etsy House Rules 20-year wording; Replacements.com free Pattern Identification Service; Marks4Antiques contact page terms; eBay community threads on "vintage"; App Store price snippets for apps whose listings did not load.
