# Lane 02: AI listing writers and Etsy/eBay SEO tools

Date 2026-11-07. Author: research subagent. Question: Which AI writers and keyword/SEO tools produce better titles, tags and descriptions for Etsy, eBay and Shopify listings of one-of-one vintage pieces, and what do they cost? Legend: V = vendor page read today (2026-11-07); U = unverified (snippet, third-party page, or the vendor page would not load).

Method note: pages were read with headless Chromium through the session proxy. etsy.com (Seller Handbook, legal pages) returns HTTP 403 to the fetcher; help.etsy.com does not, so every Etsy rule below comes from help.etsy.com. eBay's US Seller Center pages 404 or wall; eBay Help and the UK Seller Centre load. The chatgpt.com and photoroom.com pricing pages render their dollar figures outside the text layer; ChatGPT prices were taken from OpenAI's own announcement page instead, Photoroom prices stay U. WebSearch budget ran out mid-sweep; the last third of the sweep used direct URLs only.

## 0. Bottom line

- The best free keyword source for Etsy is Etsy itself. Marketplace Insights gives 15 keyword searches a week free (unlimited with Etsy Plus, $10 USD per month). Stats shows the real search terms that brought shoppers to the shop. The Search Visibility page carries Etsy's own optional AI title tool (English shops only). All V.
- The best free vocabulary source for vintage is eBay Product research (the old Terapeak), free in Seller Hub for all sellers, three years of sold data. Sold titles tell you what buyers call a thing. V.
- Of the third-party Etsy SEO tools, two have real free tiers: eRank Free (5 keyword lookups a day, 1 AI Listing Helper use a day) and Alura Free (5 searches a day, about 20 AI listing optimizations as a one-time starter balance). EverBee Hobby is free but caps keyword research at 10 keywords. Marmalead ($19/mo) and Sale Samurai ($19.99/mo) have no free tier. Koalanda is the cheapest unlimited plan at $5.99/mo billed yearly ($71.88). All V.
- For writing the listing itself, the cheapest purpose-built option is already in the stack: Crosslist's AI add-on is +$4.99/month on any plan and turns a photo into a draft listing at 1 credit per item. Gold is still $39.99 per month, unchanged since 2026-10-26. V.
- General chatbots are free and good enough for a stopgap prompt: ChatGPT Free, Claude Free, Gemini Free. Paid tiers for a solo seller: ChatGPT Go $8 USD/month or Plus $20 USD/month; Claude Pro $20 monthly or $17 on annual; Google AI Plus $4.99/month or AI Pro $19.99/month. The shop's planned Claude Haiku drafting (Haiku 5.5 API input $0.10 / MTok) replaces these once the dashboard exists. V.
- Etsy rules that shape every listing: up to 13 tags of 20 characters; vintage means at least 20 years old; titles should name the item first and run under 15 words (the handbook text is U via a third-party quote, the help-center tool page is V). AI-created items must disclose AI in the description; no Etsy page read today restricts AI-written listing text for a physical vintage item. V except where noted.
- Skip: Copy.ai ($29/mo, team GTM tool), Describely ($0.75 per product, catalog tool for Shopify/WooCommerce), Nifty ($35.99/mo and up, Poshmark-automation centric), Keywords Everywhere (Google volume, no Etsy or eBay), Marmalead and Sale Samurai until a free tool runs out. Reeva AI could not be found as a reseller product (reeva.ai is an industrial engineering-data company); U, dropped.

## 1. Comparison table

| Tool | What it does | Price (verbatim quote) | Free tier | Platform | Fit for Hollie | V/U | Source URL |
|---|---|---|---|---|---|---|---|
| Etsy Marketplace Insights | Real Etsy search counts and listing counts per keyword, last 30 days; related terms; trends | "Sellers can explore up to 15 keyword searches per week for free." Etsy Plus: "$10 USD per month" | Yes, 15 searches/week | Etsy, desktop and mobile web only | High. Free, first-party data | V | https://help.etsy.com/hc/en-us/articles/35122361353239 ; https://help.etsy.com/hc/en-us/articles/360001589928-What-is-Etsy-Plus |
| Etsy Stats search terms | Shows the search terms shoppers used to reach your listings | "Choose Etsy search under How shoppers found you to see what search terms people used" | Yes, included | Etsy web and Seller app | High once listings have traffic | V | https://help.etsy.com/hc/articles/115015774268 |
| Etsy AI title tool (Search Visibility page) | Optional AI suggestions for listing titles, bulk accept or edit | "You may have access to an optional tool on the search visibility page that provides title recommendations." | Yes, included | Etsy web (Shop Manager); English shops only | Medium-high. Free; hidden if titles already comply | V | https://help.etsy.com/hc/en-us/articles/25869947521175-How-to-Use-the-Etsy-Search-Visibility-Page |
| eRank | Etsy keyword volume, tag audits, competitor tracking, AI Listing Helper (OpenAI) for title, description and tags with tag stats | Free "$0/mo"; Basic "$5.99/mo"; Pro "$9.99/mo"; Expert "$29.99/mo" (monthly toggle) | Yes: "5 keyword lookups/day, 1 shop, 50 listings, 5 listing audits/day, 1 AI Listing Helper use/day" | Web, Chrome extension; Etsy API app | High. Free tier fits a few listings a day | V | https://erank.com/plans ; https://help.erank.com/blog/listing-helper-saves-you-time/ |
| Alura | Etsy keyword and product research, AI listing optimization, follow-ups, Pinterest pins | Basic "$11.99/mo" or "$7.99/mo" yearly ("$95.88 billed yearly"); Growth "$29.99/mo" or "$14.99/mo" yearly ("$179.99 billed yearly"); Professional "$69.99/mo" or "$29.99/mo" yearly ("$359.88 billed yearly") | Yes: "5 daily keyword & product searches", "AI listing optimization (about 20)", "1,000 starter AI credits" | Web, Chrome extension, API and MCP | High for a trial. Starter AI credits are one-time | V | https://www.alura.io/pricing ; https://www.alura.io/vs/koalanda |
| Koalanda | Etsy keyword tool, product and competitor research, SEO tools; no AI writer seen | "$11.99 / month Billed monthly"; "$9.99 / month Billed every 3 months as $29.97 USD"; "$5.99 / month Billed every year as $71.88 USD" | Yes: "$0.00 / month", "Limited searches" | Web; Etsy API app | Medium. Cheapest unlimited keyword data | V | https://koalanda.pro/pricing |
| EverBee | Etsy product analytics (sales, revenue), keyword research with Keyword Score, Tag Analyzer, AI Actions | Hobby "$0 / month Free forever"; Growth "$24.99 / month" ("$299 per year" annual); Business "$69 / month Billed annually at $828" | Yes, but "Keyword Research: 10 keywords" | Web, Chrome extension, MCP | Medium-low. Built for finding products to make, not one-offs | V | https://www.everbee.io/pricing |
| Marmalead | Etsy keyword search volume and engagement, seasonality, letter grades, "AI Description Critique", "AI Generated FAQs" | "$19 USD paid monthly"; "$53 USD paid quarterly"; "$190 USD paid annually"; Lifetime "$300 USD paid ONCE" | No | Web; Etsy API app | Medium. No free tier; lifetime is the only interesting price | V | https://marmalead.com/pricing/ |
| Sale Samurai | Etsy search volume, keyword and competitor tools, Chrome extension | "$19.99 Monthly"; "$16.65/mo Billed as $199.90 yearly" | No. "3-day free trial" | Web, Chrome extension | Low-medium. No free tier | V | https://salesamurai.io/pricing/ |
| ListifyAI | Writes an Etsy title, description and 13 tags from a product photo; listing score | Free "$0" "3 listings / month"; Starter "$9 /month" "15 listings / day"; Pro "$29 /month"; Agency "$79 /month" | Yes, 3 listings a month | Web | Medium. Cheap photo-to-listing; small vendor, quality unverified | V | https://www.listifyai.net/pricing |
| Listadum | Etsy listing manager, templates, scheduler, tag finder, listing score; AI on paid plans | Title: "Plans from $15/mo, Free Forever Plan"; Free "$0", "No AI credits included" | Yes, listing manager only | Web | Medium. Free manager is useful; AI costs | V | https://www.listadum.com/pricing |
| eBay Product research (Terapeak) | Three years of eBay sold data: sales trends, average sold price, sell-through, sold titles | "All sellers can now take advantage of insights... directly from the Seller Hub Research tab and the mobile apps." | Yes, free for all sellers; Sourcing insights needs a Basic Store | eBay Seller Hub web, eBay apps | High. Best sold-title vocabulary for vintage | V | https://www.ebay.com/help/selling/selling-tools/terapeak-research?id=4853 |
| eBay AI-generated descriptions | One-tap AI item description inside the listing flow | Free, part of listing. UK notice: "AI-powered item descriptions are now available to all UK sellers listing in the majority of categories on the eBay app." | Yes | eBay app (iOS, Android); desktop rollout promised in 2023 | Medium. Review every line; seller is responsible for accuracy | V (UK page, 2023); US page 404 | https://www.ebay.co.uk/sellercentre/news/2023-september/ai-enabled-description |
| eBay AI bulk listing (photo to listing) | Upload many photos; AI groups and drafts listings; desktop only | Free | Yes | eBay web (desktop) | Medium. Still rolling out; trading-card misses reported | U (third-party report) | https://www.valueaddedresource.net/ebay-winter-2026-seller-check-in/ |
| Shopify Sidekick / Shopify Magic | Writes product descriptions and other store text inside Shopify admin; suggests category | Included with a Shopify plan. Basic "$29 USD/mo" paid yearly, "$39 USD/mo" paid monthly; "Try 3 days free, then $1/month for 3 months." | Included; "Many of these features are available at no additional cost, but availability can vary by plan, device, and language." | Shopify admin web and Shopify app | Medium. Only once the Shopify store exists | V | https://help.shopify.com/en/manual/ai-powered-tools ; https://www.shopify.com/pricing |
| ChatGPT | General assistant; drafts titles, tags and descriptions from a prompt and a photo | "ChatGPT Go at $8 USD/month"; "ChatGPT Plus at $20 USD/month"; "ChatGPT Pro at $200 USD/month" (OpenAI announcement, Jan 16 2026) | Yes: "The free version of ChatGPT is available to everyone." | Web, iOS, Android, Windows and Mac apps | High as a free stopgap; Go "may include ads" | V | https://openai.com/index/introducing-chatgpt-go/ ; https://chatgpt.com/pricing |
| Claude | General assistant; same job. Haiku API is the shop's planned drafting engine | Free "$0"; Pro "$17 Per month with annual subscription discount ($200 billed up front). $20 if billed monthly."; Max "$100 Per month"; Ultra "$200 Per month". API: Haiku 5.5 "$0.10 / MTok for prompts up to 100,000 tokens" | Yes | Web, desktop, iOS, Android; API | High as a free stopgap; API already planned | V | https://claude.com/pricing ; https://platform.claude.com/docs/en/about-claude/pricing |
| Gemini | General assistant; same job | Free "$0/ month"; Google AI Plus "$4.99/ month"; Google AI Pro "$19.99/ month"; Google AI Ultra "$99.99/ month" or "$199.99 / month" | Yes | Web, iOS, Android, Gmail and Docs | Medium. Cheapest paid tier of the three at $4.99 | V | https://gemini.google/subscriptions/ |
| Crosslist AI add-on | Photo to full listing draft, AI photo edits, AI pricing suggestion, on top of the crosslister | Plans "$29.99" / "$34.99" / "$39.99" / "$44.99" per month (monthly toggle); add-on "+$4.99/month" with 200 / 500 / 1000 / 2000 credits; "Consumes 1 credit per request" for listing creation | No free tier; "3-day money-back guarantee" or 20 listings | Web, mobile app; US, UK, CA, AU only | High. Cheapest purpose-built writer in the stack; Gold unchanged at $39.99 | V | https://crosslist.com/pricing |
| Vendoo AI Listing Enhancement | Crosslister with AI listing enhancement from the Growth tier | Starter "$12.49", Growth "$24.99", Pro "$49.99", all "Per month, billed yearly"; monthly-billed prices not in page text | 14-day trial, no free plan | Web, iOS, Android | Medium. Another lane owns the crosslister decision | V | https://www.vendoo.co/pricing |
| Nifty | Crosslisting plus "AI-powered listing generation", smart credits, Poshmark/eBay automation | Crosslisting Plus "$35.99*/ month" with "500 smart credits per month"; Automation "$35.99*/ month"; Bundle Plus "$62.99*/ month"; "+ $18 / month for larger closets" | "7-day free trial" | Web (PWA) | Low. Pricier; Poshmark-automation centric | V | https://nifty.ai/pricing |
| Copy.ai | Chat with OpenAI, Anthropic and Gemini models; GTM workflows | Chat "$29/mo Billed monthly", "5 Seat" | None shown | Web | Low. Team sales tool; no free plan on the page | V | https://www.copy.ai/prices |
| Describely | Bulk product descriptions, data enrichment, content audit for catalogs | "$0.75 Per product for up to 500 products"; "your first 5 products are free" | 5 products | Web; Shopify, WooCommerce, Wix, Squarespace, CSV | Low-medium. Catalog tool; no Etsy or eBay | V | https://describely.ai/pricing |
| Photoroom (description generator) | Free web tool writes a product description from details you type; plan prices hide behind JS | Pro / Max / Ultra "Per month, billed yearly" with "8,000/month", "25,000/month", "75,000/month" AI credits; dollar figures not readable | Free generator page; app has a free tier | Web, iOS, Android, Shopify | Low for text. Photo tools are another lane. No "Instant Listing" page found | U (prices); V (generator exists) | https://www.photoroom.com/tools/product-description-generator ; https://www.photoroom.com/pricing |
| Keywords Everywhere | Google, YouTube, Amazon, Pinterest keyword volume in the browser; credits | "$84 billed annually" for "100,000 credits/year"; top-ups "$80 200,000 credits"; "1 Credit = 1 Keyword"; "Credits expire after one year" | Free widgets without volume | Chrome and Firefox extension | Low. No Etsy or eBay on its site list; only helps Shopify page SEO | V | https://keywordseverywhere.com/pricing.html ; https://keywordseverywhere.com/credits.html |
| Google Trends | Seasonality of search terms, free | Free, no pricing page | Yes | Web | Medium. Timing for seasonal vintage (barware before holidays) | V | https://trends.google.com/trends/ |
| Pinterest Trends | Two years of search, save and shopping trends by region; predictions | Free with a business account | Yes | Web (business account) | Medium. Decor vocabulary and timing | V (help page); trends.pinterest.com itself did not render | https://help.pinterest.com/en/business/article/pinterest-trends |
| Reeva AI | Seed could not be resolved. reeva.ai is "Engineering intelligence for industrial enterprises"; reeva.co returned HTTP 402 | unknown | unknown | unknown | Dropped | U | https://www.reeva.ai/ |

## 2. Notes per tool

### Etsy built-ins (Marketplace Insights, Stats, Search Visibility, Etsy Plus). V
- Marketplace Insights: "At this time, Marketplace Insights is only available on the desktop and mobile web versions of Etsy." Not in the Seller app. "The results of your 15 free searches remain available to you for 7 days." Etsy says it will not edit listings for you; it feeds "The AI-powered title suggestion tool". Etsy also warns the terms shown "reflect what buyers are searching for - even if something is not allowed on Etsy."
- Etsy Plus: "$10 USD per month", includes "15 credits for creating or renewing listings", "$5 USD in Etsy Ads credit", and "Unlock unlimited Marketplace Insights searches". Credits do not roll over. For a shop listing a few one-offs a week, 15 free searches is likely enough; Plus pays back only if the 15 listing credits ($3 at $0.20 each) and $5 ads are used.
- AI title tool: "At this time, title recommendations are only available to shops with their language set to English. If your titles already adhere to our guidance, the tool will not be visible." Etsy advises "Before you make any updates, download a CSV of your listings" to keep old keywords for tags.
- Etsy title guidance (U, quoted by Value Added Resource from the Seller Handbook, Aug 2025): "Clearly state the item for sale, like 'mug' or 'dress'"; "Consider using less than 15 words"; "Move subjective words, like 'perfect' or 'beautiful,' to the description"; "Only include holidays, special occasions, or recipient types if they're essential". The handbook article itself (etsy.com) returned 403 twice.
- Tags: "You can use up to 13 tags per listing. Each tag can contain up to 20 characters. Tags can only include spaces, letters, numbers." Apostrophe and hyphen allowed inside words, not at the start.
- Vintage: "vintage items that are at least 20 years old" (What Can I Sell on Etsy). Reselling article: "Reselling is not allowed on Etsy except for the following items... Vintage items: Breathe new life into unique, handpicked items that are over 20 years old." For 2026 that means made in 2006 or earlier, so most 80s and 90s fashion qualifies; late-2000s pieces do not.
- AI: "Etsy allows sellers to use artificial intelligence (AI) tools to create certain items... Sellers must disclose within their listing description if an item is created with the use of AI." Not allowed: "Bot-generated content", "AI-generated functional instructions", "AI prompt bundles". This governs AI-made products. No help.etsy.com page read today bars AI-drafted titles or descriptions for a physical vintage item; the Creativity Standards legal page (etsy.com) would not load, so treat that as a gap, not a clearance.
- "How Etsy AI Assistants Work" is about Etsy's buyer-facing support, gifting and wedding chat assistants, not seller tools.

### eRank. V
- Free is genuinely free: "There is no limited timeline - it's free for as long as you would like to be a member." No card needed.
- AI Listing Helper: "Enter a short description of your item and sit back, letting Listing Helper provide you with options for your title, description, and even keyword tags. It provides you with three suggestions for title and descriptions, and also includes the keyword stats for tag suggestions." It "uses the same OpenAI as ChatGPT, is not a Search Engine Optimization (SEO) expert". eRank's own advice: edit titles so "the beginning of your title reflects what the product is" because "only the first five or six words of your title are visible".
- Free plan allows 1 Listing Helper use a day; Basic ($5.99/mo) lifts keyword lookups to 100 a day. Footer: "This app uses the Etsy API but is not endorsed or certified by Etsy."
- Annual toggle exists; annual prices were not captured (monthly view read).

### Alura. V
- Monthly figures come from Alura's own comparison page (alura.io/vs/koalanda), which also states "Alura links a second shop only on Professional". The pricing page shows yearly totals only in the text layer.
- Free: "Research databases include a sample of 1 million products and 25,000 shops. Includes 1,000 starter AI credits." Basic: "AI listing optimization (about 40/mo)" and "AI credits (2,000/mo)". "7-day money-back guarantee" on paid plans.
- Alura's AI listing optimization is the closest thing in this set to a one-click rewrite with keyword data attached. The free tier's starter credits are a trial, not a monthly allowance.

### Koalanda. V
- Cheapest unlimited data. "All features included, Unlimited searches, Unlimited keyword lists, 5 connected shops" from $5.99/mo billed yearly. No AI writer on the pricing page. Free tier text: "Limited features included, Limited searches".

### EverBee. V
- Hobby free tier: "Keyword Research: 10 keywords", "Favorites: 5 keywords, 5 shops". Growth adds "AI Actions: 100 actions per month" and "Tag Analyzer". EverBee's AI Actions page reads "Iterate on your designs with AI Actions", so it leans toward product design, not listing copy. Product analytics (estimated sales per listing) is for copying what sells, which does not apply to one-of-one stock.

### Marmalead. V
- No free tier. "AI Description Critique" and "AI Generated FAQs" are the AI pieces. Lifetime "$300 USD paid ONCE" is the only way it beats $19/mo. Vendor claims "260,503 other Etsy Shops".

### Sale Samurai. V
- "Start with a 3-day free trial", "No credit card required", then $19.99 monthly or $199.90 yearly. No free plan.

### ListifyAI and Listadum. V
- ListifyAI: "gives you the keyword research and the finished listing - an SEO title, description and all 13 tags, written from your product photo." Free "3 listings / month". Starter $9/month. The vendor is small and the claims are its own; no independent reviews were read.
- Listadum: free plan is a listing manager with "No AI credits included". Paid from $15/mo per the page title; tiers were not captured line by line.

### eBay. V and U
- Product research (Terapeak): "Product research gives you access to the last 3 years of eBay sales data for millions of items, including: Sales trends, Average sales price, Sold price range... Sell through rate". Free to all Seller Hub users. "Sourcing insights is available at no extra cost to business sellers with a Basic Store subscription or above."
- AI descriptions: the US Seller Center URL for this feature 404s. The UK Seller Centre page (2023) is the official description: "You can use the suggested description as-is, or easily customise it to add more detail, adjust for accuracy, or fit your business' unique voice." FAQ heading: "What if my listing is inaccurate because of the automatically-generated information?" (answer collapsed). Treat the output as a draft; the seller carries the accuracy risk.
- AI bulk listing (U, Value Added Resource, Nov 2026): "the bulk photo-upload experience remains desktop-only and does not support listings with variations"; "sellers responsible for reviewing and correcting the results before publishing"; "broader US rollout expected over the coming months and into early 2027". Also "increasing the maximum number of photos per listing from 12 to 24".
- eBay policy on AI text: no eBay policy page read today. Search snippets (U) say eBay's 2026 user agreement bans third-party AI shopping agents and that sellers remain responsible for listing content. Scraping eBay is banned; every third-party tool here that touches eBay does so through the eBay API ("This application uses the eBay API").

### Shopify Sidekick / Magic. V
- shopify.com/magic now redirects to shopify.com/sidekick. Help: "Sidekick writes text for the following: Blog posts, Online store pages, Product descriptions, Shopify Messaging emails, Content in the theme editor." Also "Get a suggested product category and category metafields based on your product details." Caution from Shopify: "AI outputs can contain errors, so review anything a tool creates or changes."
- Cost: "Many of these features are available at no additional cost, but availability can vary by plan, device, and language." The Sidekick FAQ "Does using Sidekick cost money?" is collapsed on the marketing page; the pricing page lists "Sidekick, AI assistant for commerce" under AI features for the plans. Basic plan "$29 USD/mo" yearly, "$39 USD/mo" monthly.
- Shopify also lets you connect ChatGPT, Claude or Gemini to the store: "From within those tools, you can ask questions and manage store data such as products, orders, and customers."

### ChatGPT, Claude, Gemini. V
- ChatGPT pricing page: "We offer monthly plans for Go, Plus and Business". Go: "This plan may include ads." Privacy row: "Content is used to train our models - Opt-out available" on consumer plans. Prices from OpenAI's Jan 16 2026 post: Go $8, Plus $20, Pro $200 USD/month.
- Claude: Free "Limited usage every 5 hours and every week". Pro includes Haiku, Sonnet, Opus. "Model training: Opt-out" on all consumer plans. API Haiku 5.5: "$0.10 / MTok for prompts up to 100,000 tokens" (a batch row shows "$0.05 / MTok"). Other columns of that table were not reliably parsed from the text layer. The shop's Haiku drafting plan stands as decided; this is a price re-check only.
- Gemini: Google AI Plus "$4.99/ month" is the cheapest paid assistant tier found. Pro "$19.99/ month" bundles 5 TB storage and Gemini in Gmail and Docs.
- All three are web plus iOS and Android, so they work from Ricky's Windows PC and iPhone. None knows Etsy search volume; pair them with Marketplace Insights or eRank for the tag list.

### Crosslist AI add-on. V
- "+$4.99/month" on every tier. "Create listings with AI: Upload a photo and let AI create or complete your entire listing in a few seconds. Consumes 1 credit per request." Gold gives "1000 AI credits per month". "AI-powered pricing: Use AI to suggest the right price based on real-time market insights. Included in AI generation." "AI customization: Customize how AI creates your listings to match your preferences. Does not consume credits."
- Gold "$39.99 per month" with "15 images per listing", "CSV import and export", "Autodelisting". Same price as recorded 2026-10-26. Refund: "3-day money-back guarantee on your first purchase, as long as you've created fewer than 20 listings". "we do not support users residing in the European Union."

### Vendoo. V
- AI Listing Enhancement sits in Growth ("$24.99 Per month, billed yearly") with "300 background removals powered by PhotoRoom". Monthly-billed prices are behind a toggle and not in the text. Crosslisting mechanics belong to another lane; noted here only because the AI writer is tier-gated.

### Nifty. V
- "AI-powered listing generation: Create professional listings instantly with AI" in Crosslisting Plus at $35.99/month with "500 smart credits per month For Photoroom and other AI-powered features". Automation plans share, follow and relist on Poshmark and "Free CAPTCHA solving" is a feature, which signals browser automation against a marketplace without an API; terms-of-service risk, U (Poshmark terms not read). Pricing is above the $50 ceiling once bundled.

### Copy.ai. V
- Page shows one self-serve plan: Chat "$29/mo Billed monthly", "5 Seat", "Unlimited Words in Chat", "Access to OpenAI, Anthropic, and Gemini models". Everything else is enterprise GTM. Footer copyright 2025. No free plan on the page.

### Describely. V
- "Pay as you go $0.75 Per product for up to 500 products"; "Is there a free version? Yes... your first 5 products are free. After that it's pay-as-you-go at $0.75 per product, with no subscription". Integrations are Shopify, WooCommerce, Akeneo, Wix, Squarespace, CSV. Built for catalogs with repeat SKUs; there is a Home Decor industry page. For 52 one-off pieces that is about $39 once, but it does not know Etsy tags or eBay item specifics.

### Photoroom. U for prices, V for the generator
- The description generator page: "Create a ready-to-use product description based on the information you provided, then review and edit it before publishing" and "review the generated description before publishing to make sure nothing has been altered, exaggerated, or invented." No page named "Instant Listing" was found. Plan prices (Pro, Max, Ultra) did not render in the text layer; the App Store and Google Play listings show "In-App Purchases" without a price list. A 2026 App Store review mentions "$10 a month... for the pro version" (U). Photo tooling is another lane.

### Keywords Everywhere. V
- "Every plan includes all Keywords Everywhere features; they differ in credits". Bronze "$84 billed annually", "100,000 credits/year". Credits burn fast on Google pages: one search can cost "1 + 20 + 8 = 29 credits". Site list on the pages read: Google, YouTube, Amazon, Google Search Console, Pinterest metrics. No Etsy or eBay. Useful only for Shopify page titles aimed at Google.

### Google Trends and Pinterest Trends. V
- Google Trends loaded and is free. Pinterest Trends: "displays a historic view (up to the last two years) of the top search, save, and shopping trends across different regions and countries"; some features "are in testing right now, and are only available for certain regions". trends.pinterest.com itself returned zero text to the fetcher (likely needs a logged-in business account).

## 3. Recommendation for Hollie

Judged for one person listing one-of-one vintage pieces, a few at a time, from a Windows PC and an iPhone.

Free first, sign up today:
1. Etsy's own tools. Open Shop Manager > Stats > Marketplace Insights on the desktop and spend the 15 free searches a week on the words buyers actually type ("depression glass pink", "brass table lamp", "hollywood regency"). Once listings get traffic, read Stats > How shoppers found you > Etsy search. Check the Search Visibility page for the title tool; it only appears for English shops whose titles miss Etsy's guidance.
2. eRank Free (erank.com, Chrome extension). 5 keyword lookups and 1 AI Listing Helper run a day. Use the Listing Helper for a first draft of title, description and 13 tags, then edit so the first words name the object.
3. eBay Product research in Seller Hub (free). Search the item type, filter Sold, and copy the vocabulary from sold titles. This is the best free source for how vintage is named and priced.
4. A free chatbot (ChatGPT Free, Claude Free or Gemini Free) with one saved prompt: "Etsy title under 15 words, item first, then 13 tags of 20 characters or fewer, then an honest description with measurements and condition." This is the stopgap until the Haiku dashboard drafts listings.
5. Google Trends and Pinterest Trends for timing (barware before the holidays, patio and rattan in spring). Both free.

Pay only once it earns it:
- Crosslist AI add-on, +$4.99/month on the Gold plan already being trialed. Photo in, draft listing out, 1 credit per item. Turn it on when the Crosslist trial proves out; it is the cheapest purpose-built writer here.
- eRank Basic $5.99/mo if 5 lookups a day runs out, or Koalanda $5.99/mo billed yearly ($71.88) for unlimited keyword searches.
- Alura Free is a good second opinion for a month; Basic at $11.99/mo (or $7.99 yearly) only if its AI listing optimization clearly beats eRank's.
- Etsy Plus $10 USD/month only when 15 Marketplace Insights searches a week is a real limit; its 15 listing credits and $5 ads credit soften the price.

Skip and why:
- Marmalead ($19/mo) and Sale Samurai ($19.99/mo): no free tier; the free tools above cover the same keyword job.
- EverBee: its edge is sales estimates for products to copy; one-of-one stock does not benefit.
- Copy.ai ($29/mo, 5 seats): a sales-team tool.
- Describely ($0.75 per product): catalog tool for Shopify and WooCommerce, no Etsy tags or eBay specifics.
- Nifty ($35.99/mo and up): Poshmark-automation centric and over budget.
- Keywords Everywhere: Google volume only, credits expire, no Etsy or eBay.
- Reeva AI: no reseller product found under that name.
- Vendoo: the crosslister decision is Crosslist; its AI writer is tier-gated at $24.99/mo billed yearly.

Rules to bake into every draft, from pages read today: 13 tags, 20 characters each; name the object in the first words; keep titles under 15 words (Etsy guidance, U via third party); "vintage" only for pieces 20+ years old (made 2006 or earlier in 2026); disclose AI in the description only if the item itself was made with AI; on eBay the seller is responsible for the accuracy of any AI-written description.

## 4. Gaps and pages that would not load

- etsy.com Seller Handbook articles 1399426136697 (title guidance and AI tool) and 1402347260856 (How Etsy Uses AI): HTTP 403 twice. Title guidance is therefore U, quoted via valueaddedresource.net.
- etsy.com/legal/creativity-standards and etsy.com/help/article/4511: failed / 403. The exact Creativity Standards wording on AI text is unread.
- ebay.com/sellercenter/listing-and-marketing/ai-powered-descriptions: 404. US seller news pages for Sept and Oct 2026 returned no readable text. eBay Help pages load.
- chatgpt.com/pricing: loads but dollar figures are not in the text layer; prices taken from openai.com's Jan 16 2026 announcement. help.openai.com: 403.
- photoroom.com/pricing: loads but dollar figures are not in the text layer; App Store and Google Play listings show "In-App Purchases" without amounts.
- trends.pinterest.com: zero text (login wall). business.pinterest.com/pinterest-trends/: 404. Help page used instead.
- reeva.ai is a different company; reeva.co: HTTP 402. Reeva AI as a reseller tool: not found.
- Alura pricing page shows yearly totals only in text; monthly prices taken from Alura's own vs page.
- Vendoo monthly-billed prices and eRank annual prices sit behind toggles and were not captured.
- Claude API pricing table: only the Haiku 5.5 input price was parsed with confidence.
- help.etsy.com site search and JSON API returned no links to curl; the sitemap route worked.
- WebSearch budget for the turn ran out after about 14 searches, so late-sweep leads (Insight Agent, EtsyHunt, Lysterly, EtsyGenerator, Frooition, 3Dsellers) were not opened.
- No independent user reviews were read for any tool; all "complaints" in this report are limited to vendor pages and the Value Added Resource articles.

## 5. Sources (every URL fetched today)

https://erank.com/pricing (redirects to https://erank.com/plans)
https://help.erank.com/?s=AI+listing+helper
https://help.erank.com/blog/listing-helper-saves-you-time/
https://marmalead.com/pricing/
https://www.alura.io/pricing
https://www.alura.io/vs/koalanda
https://www.alura.io/comparison
https://everbee.io/pricing (redirects to https://www.everbee.io/pricing)
https://www.everbee.io/features
https://salesamurai.io/pricing/
https://koalanda.pro/pricing
https://keywordseverywhere.com/credits.html
https://keywordseverywhere.com/pricing.html
https://chatgpt.com/pricing
https://openai.com/chatgpt/pricing/
https://openai.com/index/introducing-chatgpt-go/
https://help.openai.com/en/articles/11989085-what-is-chatgpt-go (403)
https://apps.apple.com/us/app/chatgpt/id6448311069
https://play.google.com/store/apps/details?id=com.openai.chatgpt&hl=en_US
https://claude.com/pricing
https://platform.claude.com/docs/en/about-claude/pricing
https://gemini.google/subscriptions/
https://www.shopify.com/magic (redirects to https://www.shopify.com/sidekick)
https://help.shopify.com/en/manual/shopify-admin/productivity-tools/shopify-magic (redirects to https://help.shopify.com/en/manual/ai-powered-tools)
https://help.shopify.com/en/manual/shopify-admin/productivity-tools/sidekick (redirects to https://help.shopify.com/en/manual/ai-powered-tools/sidekick)
https://www.shopify.com/pricing
https://www.ebay.com/sellercenter/listing-and-marketing/ai-powered-descriptions (404)
https://www.ebay.com/help/selling/selling-tools/terapeak-research?id=4853
https://www.ebay.com/help/selling/listings/creating-managing-listings?id=4105
https://www.ebay.com/sellercenter/listings/create-great-listings
https://www.ebay.com/sellercenter/listings
https://www.ebay.com/sellercenter/news/seller-news-october-2026
https://www.ebay.com/sellercenter/news/seller-news-september-2026
https://www.ebay.co.uk/sellercentre/news/2023-september/ai-enabled-description
https://www.valueaddedresource.net/etsy-guidance-listing-titles-ai/
https://www.valueaddedresource.net/ebay-winter-2026-seller-check-in/
https://www.vendoo.co/pricing
https://www.crosslist.com/pricing (redirects to https://crosslist.com/pricing)
https://www.copy.ai/prices
https://describely.ai/pricing
https://www.nifty.ai/pricing (redirects to https://nifty.ai/pricing)
https://www.reeva.ai/pricing (redirects to https://www.reeva.ai/)
https://reeva.co (402)
https://www.photoroom.com/pricing
https://www.photoroom.com/tools/product-description-generator
https://apps.apple.com/us/app/photoroom-ai-photo-editor/id1455009060
https://play.google.com/store/apps/details?id=com.photoroom.app&hl=en_US
https://trends.google.com/trends/
https://trends.pinterest.com/ (no text)
https://business.pinterest.com/pinterest-trends/ (404)
https://help.pinterest.com/en/business/article/pinterest-trends
https://www.listadum.com/pricing
https://www.listifyai.net/pricing
https://www.etsy.com/seller-handbook/article/1399426136697 (403)
https://www.etsy.com/seller-handbook/article/1402347260856 (403)
https://www.etsy.com/legal/creativity-standards (failed)
https://www.etsy.com/help/article/4511 (403)
https://help.etsy.com/hc/articles/360000336307 (How to Use Tags to Get Found in Search)
https://help.etsy.com/hc/articles/115015774268 (How to Use Etsy Stats for Your Shop)
https://help.etsy.com/hc/en-us/articles/35122361353239 (How Do I Use Etsy's Marketplace Insights Tool?)
https://help.etsy.com/hc/en-us/articles/25869947521175-How-to-Use-the-Etsy-Search-Visibility-Page
https://help.etsy.com/hc/en-us/articles/360024112614-What-Can-I-Sell-on-Etsy
https://help.etsy.com/hc/en-us/articles/23948763872151-Does-Etsy-Allow-Drop-Shipping-or-Reselling
https://help.etsy.com/hc/en-us/articles/360001589928-What-is-Etsy-Plus
https://help.etsy.com/hc/en-us/articles/27283630080151-How-Etsy-AI-Assistants-Work
https://help.etsy.com/hc/en-us/articles/115015628847 (wrong guess; payment processing fees)
https://help.etsy.com/hc/en-us/search?query=... (four site-search pages, titles only)
https://help.etsy.com/api/v2/help_center/en-us/articles/search.json (no response)
https://help.etsy.com/hc/sitemap.xml
