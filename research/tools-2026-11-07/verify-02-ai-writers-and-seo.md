# Verify lane 02: AI listing writers and Etsy/eBay SEO tools

Date 2026-11-07. Author: research subagent (adversarial price and claim checker). Question: Do the prices, free tiers, platform claims and availability claims in `02-ai-writers-and-seo.md` match the vendors' own pages today? Legend: V = page read today; U = unverified.

Method: every page below was read today with headless Chromium through the session proxy (fetch.sh), with a raw curl of the HTML where the visible text layer hid a dollar figure (Alura, EverBee, Vendoo, eRank, chatgpt.com). No Reddit, no roundups. 24 checks across 23 pages. No shutdown, acquisition or sunset notice appeared on any page read.

## 0. Bottom line

- Nothing in the first agent's PICKS was refuted. Every dollar figure checked matches the vendor's page today.
- Four claims needed a correction or a caveat, none of them price errors: Vendoo's monthly-billed prices are on the page after all ($14.99 / $29.99 / $59.99); EverBee's $24.99 is the annual-billing rate only; the Etsy Search Visibility page never uses the word "AI" (the Marketplace Insights FAQ does); the eBay Product research page never uses the word "free".
- Alura's and EverBee's per-month figures sit outside the visible text (JSON-LD and FAQ markup), so a text-only reader would miss them. The figures recorded by the first agent are right.
- chatgpt.com/pricing shows no dollar figures in its text layer or raw HTML. OpenAI's announcement page carries them: Go $8, Plus $20, Pro $200 USD/month, and says ads will be tested in Free and Go in the US.
- Crosslist Gold is still $39.99 per month and the AI add-on is still +$4.99/month with 1000 credits on Gold, 1 credit per listing request.

## 1. Checks

| Tool | Claim checked | Verdict | Evidence quote | URL | Correction |
|---|---|---|---|---|---|
| Etsy Marketplace Insights | Free, 15 keyword searches a week, results kept 7 days, desktop and mobile web only, unlimited with Etsy Plus | confirmed | "Sellers can explore up to 15 keyword searches per week for free." ... "remain available to you for 7 days" ... "only available on the desktop and mobile web versions of Etsy." | https://help.etsy.com/hc/en-us/articles/35122361353239 | none |
| Etsy Plus | $10 USD per month | confirmed | "The fee for an Etsy Plus subscription is $10 USD per month" | https://help.etsy.com/hc/en-us/articles/360001589928-What-is-Etsy-Plus | none |
| Etsy Search Visibility title tool | Free, included, English-language shops only, hidden when titles already comply | confirmed | "title recommendations are only available to shops with their language set to English. If your titles already adhere to our guidance, the tool will not be visible." | https://help.etsy.com/hc/en-us/articles/25869947521175-How-to-Use-the-Etsy-Search-Visibility-Page | The page never says "AI". The "AI-powered title suggestion tool" wording is on the Marketplace Insights FAQ. |
| Etsy Stats search terms | Free, included, shows the search terms shoppers used, Seller app | confirmed | "Choose Etsy search under How shoppers found you to see what search terms people used to find your listings." Section "Stats on the Etsy Seller App" | https://help.etsy.com/hc/articles/115015774268 | none |
| eRank Free and Basic | Free $0/mo with 5 keyword lookups/day, 1 shop, 50 listings, 5 audits/day, 1 AI Listing Helper use/day; Basic $5.99/mo; Pro $9.99/mo; Expert $29.99/mo; monthly toggle shown; no card | confirmed | "Free $0/mo ... 5 keyword lookups/day ... 1 AI Listing Helper use/day"; "Basic $5.99/mo"; "sign up for our free membership without submitting any credit card" | https://erank.com/plans | Raw HTML adds annual savings tags: "Save $6/yr" (Basic), "Save $25/yr" (Pro), "Save $90/yr" (Expert). The $5.99 is the monthly price. |
| eRank AI Listing Helper | Three titles and descriptions plus tags with keyword stats, OpenAI-based, on every plan with daily limits | confirmed | "It provides you with three suggestions for title and descriptions, and also includes the keyword stats for tag suggestions." "uses the same OpenAI as ChatGPT" | https://help.erank.com/blog/listing-helper-saves-you-time/ | none |
| eBay Product research (Terapeak) | Free for all Seller Hub sellers, 3 years of data, Sourcing insights needs a Basic Store | confirmed | "All sellers can now take advantage of insights ... directly from the Seller Hub Research tab and the mobile apps." "last 3 years of eBay sales data" "Sourcing insights is available at no extra cost to business sellers with a Basic Store subscription or above." | https://www.ebay.com/help/selling/selling-tools/terapeak-research?id=4853 | The page never uses the word "free" for Product research; it states availability to all sellers with Seller Hub and lists no fee. |
| ChatGPT | Go $8, Plus $20, Pro $200 USD/month; Free available to everyone | confirmed | "ChatGPT Go at $8 USD/month*" "ChatGPT Plus at $20 USD/month" "ChatGPT Pro at $200 USD/month" "*US price displayed." | https://openai.com/index/introducing-chatgpt-go/ | chatgpt.com/pricing renders no dollar figures in text or raw HTML (see gaps). Same page: "We plan to begin testing ads in the free tier and ChatGPT Go in the US soon." |
| Claude (consumer) | Free $0; Pro $17/month annual ($200 up front) or $20 monthly; Max $100; Ultra $200; limits every 5 hours and every week | confirmed | "$17 Per month with annual subscription discount ($200 billed up front). $20 if billed monthly." "Max $100 Per month" "Ultra $200 Per month" "Limited usage every 5 hours and every week*" | https://claude.com/pricing | none |
| Claude Haiku 5.5 API | $0.10 / MTok input for prompts up to 100k tokens | confirmed | "Claude Haiku 5.5 ... $0.10 / MTok for prompts up to 100,000 tokens" | https://platform.claude.com/docs/en/about-claude/pricing | Over 100,000 tokens the input price is "$0.50 / MTok". |
| Gemini | Free $0; Google AI Plus $4.99/month; AI Pro $19.99/month; AI Ultra $99.99 or $199.99/month | confirmed | "$0/ month with a Google Account" "Google AI Plus ... $4.99/ month" "Google AI Pro ... $19.99/ month" "$99.99/ month: 5x higher usage limits vs. AI Pro" "$199.99 / month: 20x" | https://gemini.google/subscriptions/ | none |
| Pinterest Trends | Free with a Pinterest business account; web | confirmed | No price or paid tier anywhere on the page. "Some of the features outlined below are in testing right now, and are only available for certain regions." "If you have a Pinterest business account, you can browse the top trends specific to your engaged users" | https://help.pinterest.com/en/business/article/pinterest-trends | A business account is named only for advertiser-specific and own-audience features, not for browsing general trends. Some features are region-limited. |
| Google Trends | Free, web | confirmed | Page loads without sign-in or price: "Explore what the world is searching for right now" | https://trends.google.com/trends/ | none |
| Alura | Free: 5 daily searches, about 20 AI listing optimizations, 1,000 starter credits; Basic $11.99/mo or $7.99/mo billed yearly ($95.88); Growth $179.99 yearly; Professional $359.88 yearly; Chrome extension, API and MCP | confirmed | "5 daily keyword & product searches" "AI listing optimization (about 20)" "Includes 1,000 starter AI credits." "$95.88 billed yearly, save 33%" "$179.99 billed yearly, save 50%" "$359.88 billed yearly, save 57%" "API & MCP access" | https://www.alura.io/pricing | Per-month figures are not in the visible text. The page's JSON-LD carries them: Basic "price":11.99 USD (monthly), $7.99, $14.99, $29.99 for annual-equivalent. "Free includes a one-time starter balance." |
| Crosslist AI add-on | Gold $39.99 per month; AI add-on +$4.99/month, 1000 credits on Gold, 1 credit per listing; no free tier, 3-day money-back or 20 listings; US, UK, CA, AU | confirmed | "Gold $39.99 per month" "Get 1000 AI credits per month" "+$4.99/month" "Upload a photo and let AI create or complete your entire listing ... Consumes 1 credit per request" "Enjoy 3 days of Crosslist or 20 free listings, whichever comes first." "Works in the United States, United Kingdom, Canada, and Australia" | https://crosslist.com/pricing | Bronze $29.99, Silver $34.99, Platinum $44.99 per month also confirmed. Annual plans carry a "$9.99 processing fee" on refunds. |
| Koalanda | $11.99/month monthly; $9.99/month billed every 3 months as $29.97; $5.99/month billed yearly as $71.88; Free $0.00 limited searches, 5 shops; no AI writer | confirmed | "$11.99 / month Billed monthly" "$9.99 / month Billed every 3 months as $29.97 USD" "$5.99 / month Billed every year as $71.88 USD" "Free $0.00 / month ... Limited searches ... 5 connected shops" | https://koalanda.pro/pricing ; https://koalanda.pro/ | Home page describes a "Listing Editor" with SEO suggestions; no AI generation feature is named, so "no AI writer" stands. |
| EverBee | Hobby $0 free forever, 10 keywords; Growth $24.99/month ($299 per year annual); Business $69/month billed annually at $828 | confirmed | "Free forever" "Keyword Research: 10 keywords" "That comes to $468 $299 per year" "Billed annually at $828 - save $360"; raw HTML FAQ: "just $24.99 per month, billed annually at $299" | https://www.everbee.io/pricing | $24.99 is the annual-billing rate only. The monthly-billed figure is not in the text; the struck-out "$468" per year implies $39/month on monthly billing. |
| Marmalead | $19 USD monthly; $53 quarterly; $190 annually; Lifetime $300 once; no free tier | confirmed | "$19 USD paid monthly" "$53 USD paid quarterly" "$190 USD paid annually" "$300 USD paid ONCE" | https://marmalead.com/pricing/ | none; no free tier or trial wording on the page |
| Sale Samurai | $19.99 monthly; $16.65/mo billed as $199.90 yearly; 3-day free trial, no card; Chrome extension | confirmed | "$19.99 Monthly" "$16.65/mo Billed as $199.90 yearly" "No credit card required to sign up." "Free Chrome extension included" | https://salesamurai.io/pricing/ | none |
| ListifyAI | Free $0, 3 listings/month; Starter $9/month, 15 listings/day; Pro $29/month; Agency $79/month; annual 2 months free | confirmed | Title: "Free, Starter $9, Pro $29, Agency $79" "3 listings / month" "$9 /month ... 15 listings / day" "Annual — 2 months free" | https://www.listifyai.net/pricing | none |
| Shopify plan | Basic $29 USD/mo yearly, $39 monthly; 3 days free then $1/month for 3 months | confirmed | "Try 3 days free, then $1/month for 3 months." "Pay monthly $39 USD/mo" "Pay yearly $29 USD/mo" | https://www.shopify.com/pricing | none |
| Shopify Sidekick / AI tools | Included at no additional cost; availability varies by plan, device, language | confirmed | "Many of these features are available at no additional cost, but availability can vary by plan, device, and language." Sidekick writes "Product descriptions" | https://help.shopify.com/en/manual/ai-powered-tools | none |
| Vendoo | Starter $12.49, Growth $24.99, Pro $49.99 per month billed yearly; 14-day trial; AI Listing Enhancement from Growth; iOS and Android | confirmed | "$12.49 Per month, billed yearly" "$24.99 Per month, billed yearly ... AI Listing Enhancement" "$49.99 Per month, billed yearly" "Try Vendoo Free for 14 Days." "Mobile app for iOS and Android" | https://www.vendoo.co/pricing | Monthly-billed prices are on the page (raw HTML, behind the toggle): "$14.99 Per month, billed monthly", $29.99, $59.99. The first agent said they were absent. |
| Listadum | Plans from $15/mo; Free $0, no AI credits | confirmed | "Free Plan $0 ... No AI credits included" "Monthly billing: Starter $15, Growth $30 and Max $150 a month. Yearly billing: Starter $120, Growth $240 and Max $1,200 a year" | https://www.listadum.com/pricing | Prices are per shop. Starter includes "$28.80 included AI credits" on yearly. |

## 2. What the first agent got wrong or left incomplete

No price was wrong. The corrections are all caveats:

1. Vendoo: "monthly-billed prices not in page text" is wrong in substance. The toggle hides them from the text layer, but the HTML carries "$14.99 Per month, billed monthly" (Starter), $29.99 (Growth), $59.99 (Pro).
2. EverBee: "Growth $24.99 / month" is the annual-billing rate only ("$24.99 per month, billed annually at $299"). Monthly billing is not quoted in text; the struck-out $468/year implies $39/month.
3. Etsy Search Visibility: the help page never says "AI". It says "title recommendations". The "AI-powered title suggestion tool" phrase is on the Marketplace Insights FAQ. Fine to keep, but cite both pages.
4. eBay Product research: the page does not say "free". It says all sellers with Seller Hub can use it and names no fee. Only Sourcing insights is described as "at no extra cost" (with a Basic Store).
5. Pinterest Trends: a business account is only named for advertiser-specific and own-audience features; general trend browsing is not gated on the page. Also "Some of the features outlined below are in testing right now, and are only available for certain regions."
6. ChatGPT: the first agent was right that chatgpt.com/pricing hides its figures; the raw HTML hides them too. The announcement page also warns that ads will be tested in Free and Go in the US; keep that in the fit note.
7. Alura: the visible text shows only yearly totals. The monthly figures ($11.99 / $29.99 / $69.99) are in the page's JSON-LD, so they stand, but a future re-check must read the raw HTML.
8. Claude Haiku 5.5: the $0.10 / MTok figure applies "for prompts up to 100,000 tokens"; above that it is $0.50 / MTok. The dashboard's prompts will be far under that, so no fit change.

Shutdown or acquisition notices: none on any of the 23 pages read.

## 3. Gaps and pages that would not load

- https://chatgpt.com/pricing/ loads (HTTP 200) but renders no dollar figures in text or raw HTML. Figures taken from the OpenAI announcement instead.
- etsy.com (non-help) and eBay US Seller Center pages were not attempted; every Etsy and eBay claim was checked on help.etsy.com and ebay.com/help, which load.
- Photoroom, Keywords Everywhere, Copy.ai, Describely, Nifty, Reeva AI were not re-checked: low fit, outside the 12 to 16 target.

## 4. Sources (every URL fetched today)

https://help.etsy.com/hc/en-us/articles/35122361353239
https://help.etsy.com/hc/en-us/articles/360001589928-What-is-Etsy-Plus
https://help.etsy.com/hc/en-us/articles/25869947521175-How-to-Use-the-Etsy-Search-Visibility-Page
https://help.etsy.com/hc/articles/115015774268
https://erank.com/plans
https://help.erank.com/blog/listing-helper-saves-you-time/
https://www.ebay.com/help/selling/selling-tools/terapeak-research?id=4853
https://openai.com/index/introducing-chatgpt-go/
https://chatgpt.com/pricing/
https://claude.com/pricing
https://platform.claude.com/docs/en/about-claude/pricing
https://gemini.google/subscriptions/
https://help.pinterest.com/en/business/article/pinterest-trends
https://trends.google.com/trends/
https://www.alura.io/pricing
https://crosslist.com/pricing
https://koalanda.pro/pricing
https://koalanda.pro/
https://www.everbee.io/pricing
https://marmalead.com/pricing/
https://salesamurai.io/pricing/
https://www.listifyai.net/pricing
https://www.shopify.com/pricing
https://help.shopify.com/en/manual/ai-powered-tools
https://www.vendoo.co/pricing
https://www.listadum.com/pricing
