# Gaps check, lane 15: AI assistants and browser agents a one-person reseller could use

Date 2026-11-07. Author: research subagent (completeness critic for lane 15). Question: Which AI assistants, browser agents and MCP routes that can do reseller work (draft listings from photos, fill listing forms, research comps, write buyer replies) are missing from the lane 15 list, and is anything on that list defunct, acquired or renamed? Legend: V = vendor page read today; U = unverified (page would not load, price did not render, or snippet only).

Method note. The shared WebSearch budget was already spent when this agent started, so no search engine was used. Every page below was addressed directly by URL and read through the session's headless Chromium fetch script (curl fallback). GitHub star counts, licences and last-push dates come from GitHub's own search API (api.github.com/search/repositories) today; GitHub's per-repo endpoint was not enabled for this session and no access was requested. One GitHub-hosted curated list (FLUF-io/awesome-reseller-tools) was read as a lead only; no roundups were used for prices. No subagents. Tools already on the lane 15 list were not re-verified.

## 0. Bottom line

- The biggest omission is Anthropic's own Claude Cowork. It is included in the plan Ricky already pays for ("Works with a paid plan"), runs on "Claude Desktop for macOS, Windows, and Linux (beta)", and has a built-in browser that can "open sites, read pages, click, type, and fill forms." It is the same agent as Claude in Chrome, with scheduling and file access added. The scheduling part ("runs unattended") is exactly what eBay, Meta and Chairish terms forbid, so keep it to Etsy drafting with Ricky watching. (V)
- eBay now publishes an official MCP server under its own GitHub org (eBay/npm-public-api-mcp, Apache-2.0, 46 stars, pushed 2026-10-27). It is read-only by design: "REST APIs: Only GET requests are supported (read operations only)". That makes it the safest comps-research route on eBay and a better first install than the community servers already listed, but it cannot create listings. (V)
- Two free, open-source photo-to-listing routes exist that the lane list lacks: Listing Writer (hahm-ebay-lister, 45 stars, "photos in, posted listings out", bring your own Anthropic and eBay developer keys, licence switched to FSL-1.1-MIT "free to use, not to resell") and seerxo for Etsy (MIT, CLI plus MCP plus Claude Code skill). Both need Step 0 developer keys. (V)
- 3Dsellers runs a hosted MCP server for "eBay, Amazon, Walmart, Etsy, Shopify and TikTok Shop" with "no eBay developer account", 120+ tools, Claude Code plugin. Entry plan "Essential $19" a month monthly ($16 billed annually), 100 listings, 7-day free trial. It overlaps the Crosslist Gold trial already decided, so it is a fallback, not a new decision. (V)
- The free, open-source browser agents are Nanobrowser (Chrome and Edge extension, Apache-2.0, 14.3k stars, bring your own API key), Browser Use (MIT, 120k stars, cloud at "$0.02 per browser hour") and Stagehand (MIT, 26k stars). OpenClaw (MIT, 394k stars, Windows 10/11, "No subscription. No hosted tier.") is the big 2026 self-hosted assistant. All of them carry the same marketplace-terms limits as Claude in Chrome and none adds anything reseller-specific. (V)
- Paid AI browsers not on the list: Dia (free browser, AI at "$10/month", owned by Atlassian since September 2025, paid plans "starting with new Mac users", Windows "Not yet"), Fellou (Windows and Mac, "Free $0 /month" for about 4 tasks, "Plus $19.0 /month"; it advertises solving CAPTCHAs, which marketplaces ban) and Brave Leo (free summaries, Premium "$14.99 /month"). Low fit. (V)
- MCP aggregators: Zapier MCP works on the Free plan ("100 tasks per month") and reaches eBay (orders) and Shopify, but "Etsy has not yet built an integration on Zapier." Pipedream's eBay MCP page says "We don't have any tools available for this app yet" and has no Etsy server. Composio has a Shopify toolkit and no Etsy toolkit (404). None replaces the Etsy Seller App route. (V)
- Defunct or renamed: Copilot Pro's Microsoft Store URL now redirects to Microsoft 365 Premium ("$19.99/month"); The Browser Company (Dia, Arc) was acquired by Atlassian; Mistral's pricing page no longer uses the name Le Chat (the assistant is sold as "Vibe"). Nothing on the lane 15 list itself is dead beyond what the first agent already marked (ChatGPT agent, Operator, Atlas). Manus, Genspark and Perplexity Computer prices could not be read today (U).

## 1. Comparison table (missing tools)

| Tool | What it does | Price (verbatim quote) | Free tier | Platform | Fit for Hollie | V/U | Source URL |
|---|---|---|---|---|---|---|---|
| Claude Cowork (with built-in browser) | Agentic Claude for files and web: "open sites, read pages, click, type, and fill forms"; scheduled tasks; same agent as Claude in Chrome | "Works with a paid plan. Rolling out on web, mobile." Built-in browser: "Available in the Cowork desktop app on Pro, Max, Ultra, and Team plans." | No (paid Claude plans only) | Windows, macOS, Linux (beta) desktop app; web; iOS and Android; Chrome side panel | High. Already included in Ricky's plan. Use for Etsy drafting and comps with review; do not schedule unattended runs on eBay, Facebook or Chairish | V | https://claude.com/product/cowork and https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork |
| eBay API MCP Server (eBay/npm-public-api-mcp, official) | Lets Claude Desktop, Claude Code and Cursor call eBay REST and GraphQL APIs in plain language; OAuth handled | Free, Apache-2.0. "REST APIs: Only GET requests are supported (read operations only)" | Yes (open source; eBay API calls free within eBay developer limits) | Node.js 22+, Claude Desktop, Claude Code, Cursor, Cline (local MCP) | High for comps research and order lookups, the official and terms-safe route; cannot create listings. Needs eBay developer keys (Step 0). 46 stars, pushed 2026-10-27 | V | https://github.com/eBay/npm-public-api-mcp |
| 3Dsellers MCP Server (hosted) | Hosted MCP: "manage listings, products, inventory, orders and buyer messages from a chat. 120+ tools." Channels: eBay, Amazon, Walmart, Etsy, Shopify, TikTok Shop | "Essential $19 $16 /Mo Billed Annually ... 100 Listings"; "Growth $39.90 $29.90 /Mo Billed Annually ... 500 Listings"; AI add-on "AI Lite $9/mo - 2,000 AI actions" | "Try All Features for 7 Days Free", "No credit card required" | Web app plus remote MCP for Claude, ChatGPT, Claude Code, Cursor, VS Code, Gemini CLI | Medium. Writes to eBay, Etsy and Shopify through APIs with "no eBay developer account", approval before data-changing tools. Overlaps Crosslist Gold; eBay-first product; 100-listing cap fits Hollie's stock | V | https://github.com/3dsellers/ebay-mcp-server and https://www.3dsellers.com/pricing |
| Listing Writer (ashnicholes-droid/hahm-ebay-lister) | "Dump in a pile of item photos" and it sorts items, writes title, description, item specifics, price, then "Posts straight to eBay" | Free, open source. Licence commit: "switch from MIT to FSL-1.1-MIT (free to use, not to resell". You pay Anthropic per use ("pennies per item") | Yes | Self-hosted web app on Vercel (free tier); "works on your computer and your phone" | Medium. Exactly the photo-to-listing job, through eBay's API, so terms-safe. eBay only. Needs an Anthropic key, eBay developer keyset and a Vercel deploy. 45 stars, single maintainer | V | https://github.com/ashnicholes-droid/hahm-ebay-lister |
| Nanobrowser | "Open-source AI agent for the web" in the Chrome or Edge side panel; "it clicks, types and reads pages"; bring your own model key | "No subscription needed. Free. Open source, Apache-2.0" | Yes (you pay the model provider) | Chrome and Edge extension | Medium-low. Free stand-in for Claude in Chrome if Ricky ever drops the paid plan; "Ask mode" confirms before submitting. Same marketplace-terms limits. 14.3k stars | V | https://nanobrowser.ai/ |
| Zapier MCP | Lets Claude call Zapier actions in 9,000+ apps; eBay: "New Order ... Triggers when a new order is made", Create a Shipping Fulfillment, Find an Order | "Free Free forever $0 /month ... (100 tasks per month)"; "Professional Starting from $19.99 /month"; MCP draws from the same tasks | Yes, 100 tasks a month | Web; MCP for Claude, ChatGPT, Cursor | Low-medium. "Etsy has not yet built an integration on Zapier." eBay side is orders only, no listing creation. Fine later for Shopify order alerts | V | https://zapier.com/mcp, https://zapier.com/pricing, https://zapier.com/apps/etsy/integrations, https://zapier.com/apps/ebay/integrations |
| Secondhand MCP (jlsookiki/secondhand-mcp) | MCP that searches Facebook Marketplace, eBay, Depop and Poshmark for comps and sourcing, with photos and seller info | "Price: free, forever" (local); Cloud: "free tier, then $4.99" | Yes | Local MCP for Claude Desktop, Claude Code, Cursor (needs Chrome for Depop and Poshmark); Cloud works from ChatGPT and phone | Medium for comps and local sourcing. eBay part uses the "Official Browse API" (needs keys). Facebook part runs with "No" auth via logged-out pages, which Meta's terms treat as automated collection; use at Ricky's risk or skip that marketplace. MIT, 99 stars | V | https://github.com/jlsookiki/secondhand-mcp |
| Dia browser (The Browser Company, now Atlassian) | Chat-with-your-tabs browser: Morning Brief, "find, summarize, draft, or build"; connects to Slack, Notion, GSuite | Free browser; "Better Answers ($10/month)"; "Better Days ($100/month)" | Yes, browser with no AI; 14-day trial of Better Days | macOS and Windows; paid plans "starting with new Mac users", Windows "Not yet" | Low. Not a form-filling agent; Ricky's Windows PC cannot even buy the AI plan yet | V | https://www.diabrowser.com/plans and https://www.atlassian.com/blog/company-news/atlassian-acquires-the-browser-company |
| Fellou | "Agentic Browser" that plans then acts across sites; Deep Search; scheduled tasks; computer use | "Free $0 /month ... 1000 Sparks (New User Bonus) - Approximately 4 Tasks"; "Plus $19.0 /month"; "Pro $39.9 /month"; "Ultra $199.9 /month" | Yes, about 4 tasks total, 2 scheduled tasks | Windows and Mac (Apple Silicon and Intel) | Low. FAQ boasts it can "handle logins, authentication, and even CAPTCHA challenges", which is the behaviour eBay and Meta ban. Free tier too small to matter | V | https://fellou.ai/pricing and https://fellou.ai/download |
| Brave Leo | AI sidebar in the Brave browser: summarize pages, draft, analyze PDFs; "No account or login is required" | "Brave Leo is free to use." Premium: "$14.99 /month" monthly or "$12.50 /month. $149.99 /year" | Yes | Brave browser on desktop, Android, iOS ("available exclusively in the Brave browser") | Low. Free page summaries for comps reading; no agent actions; Claude already covers it | V | https://brave.com/leo/ and https://account.brave.com/?intent=checkout&product=leo |
| Apple Visual Intelligence (Apple Intelligence) | Camera and screenshot based object search on iPhone: "Search and take action with Visual Intelligence, now on even more devices" | Free with a compatible device | Yes | iPhone (compatibility list on the page starts at iPhone 17 class and lists iPhone 16; Ricky's model unverified) | Medium. Zero-cost first-pass ID of a lamp or glass pattern at an estate sale, before asking Claude or Gemini | V | https://www.apple.com/apple-intelligence/ |
| OpenClaw | Self-hosted personal AI assistant: "Organizes your inbox, sends emails, manages your calendar" from WhatsApp, Telegram or any chat app; skills and browser automation | "No subscription. No hosted tier. No token." MIT. You bring model keys or a ChatGPT/Claude login | Yes | macOS 15+, Windows 10/11 (x64, ARM64), Linux desktop apps; one-line npm install | Low-medium. Largest open-source agent of 2026 (394k stars), but a solo seller gets the same from Claude Code and Cowork with less setup and security exposure | V | https://openclaw.ai/ and https://github.com/openclaw/openclaw |
| Browser Use (open source plus cloud) | Python library for browser agents plus cloud browsers and hosted agent API | "$0.02 per browser hour"; home-IP proxy "$5 / GB"; "License MIT"; "Start with $1 free." | Yes (open-source harness; $1 cloud credit) | Python; cloud API; "Your Chrome Free" | Low for Hollie. Developer tool; stealth browsers and CAPTCHA solving are aimed at scraping, the thing eBay forbids. 120k stars | V | https://browser-use.com/pricing |
| Skyvern | AI browser-workflow platform (open source AGPL-3.0 plus cloud) | "Hobby 30,000 credits/month ... $29/month"; "Pro ... $149/month"; "Every self-serve plan starts with a 14-day free trial" | Trial only (plus self-host) | Web app and API; self-host | Low. Built for enterprise portal work and CAPTCHA solving. 23.4k stars | V | https://www.skyvern.com/pricing |
| Stagehand (Browserbase) | "The SDK for browser agents" (TypeScript, Python, Go), MIT, 26k stars; Browserbase hosts the browsers | Browserbase "Free Plan $0/mo ... 3 concurrent browsers 1 browser hour"; "Developer Plan $20/mo" | Yes, tiny | Code SDK; cloud browsers | Low. Developer SDK; nothing reseller-specific | V | https://www.stagehand.dev/ and https://www.browserbase.com/pricing |
| n8n | Workflow automation with "AI Agent node", "MCP Server Trigger" and "MCP Client"; Shopify node built in; Etsy only via community node | Cloud "Starter ... 20€ /mo, billed annually 2.5k workflow executions"; "Community Edition A standard, self-hosted version of n8n is available on GitHub." | Yes, self-hosted Community Edition | Web (cloud) or self-host (Docker, Windows via Docker) | Low-medium. Free if self-hosted on the Fedora box; Etsy support is a 3-star community node (mesutkisi11/n8n-nodes-etsy). Only worth it after the dashboard exists | V | https://n8n.io/pricing/ |
| Composio | Tool and auth layer for agents, 1,500+ toolkits incl. Shopify MCP; no Etsy toolkit (404) | "Hobby $0 No credit card required 100,000 tool calls / mo"; "Pro $29 / mo" | Yes | Web dashboard; MCP and SDK for Claude Code, Cursor | Low. Shopify only among Hollie's channels; the official Claude Shopify connector already does that | V | https://composio.dev/pricing and https://composio.dev/toolkits/shopify |
| Pipedream Connect / MCP | Hosted MCP servers for 3,000+ apps; eBay and Shopify servers exist, no Etsy | "Free $0 ... Everything you need to build and test" (development only); "Startup ... $99 per month" | Yes, development only; "Production environment: Not included" on Free | Web; remote MCP URL for ChatGPT, Claude | Low. eBay server: "We don't have any tools available for this app yet." Etsy: "MCP Server Not Found." Production costs $99 a month | V | https://pipedream.com/pricing, https://mcp.pipedream.com/app/ebay, https://mcp.pipedream.com/app/shopify, https://mcp.pipedream.com/app/etsy |
| Mistral Vibe (the assistant formerly sold as Le Chat) | Chat assistant with photo upload, web search, connectors, task scheduling | "Free ... Limited messages and web searches."; "Pro ... $14.99 /mo Excluding taxes" | Yes | Web, iOS and Android, CLI | Low. A third free second-opinion on photo ID after Gemini and ChatGPT; nothing extra | V | https://mistral.ai/pricing/ |
| Grok (xAI) | Chat with "Vision understanding", live web and X search, voice | "Free to try on the web and in the apps. Upgrade to SuperGrok for higher limits"; SuperGrok amount not on the page | Yes | Web, iOS, Android | Low. Free vision second opinion; price of SuperGrok unverified (grok.com walled) | V (platform), U (paid price) | https://x.ai/grok |
| Aqua Voice | AI dictation for Windows, Mac, iOS, Android, with MCP and CLI hooks for Claude Code | "Free Try voice typing. $0 to start ... 1,000 Words"; Pro and Max amounts did not render | Yes, 1,000 words | macOS, Windows, iOS, Android | Low-medium. Another Wispr Flow alternative; try only if Flow's weekly cap bites | V (free tier), U (paid price) | https://aquavoice.com/pricing |
| seerxo (Etsy listing generator) | "AI-assisted Etsy listing generation and audit, CLI, MCP server and Claude Code skill"; title, 13 tags, attributes within Etsy rules | Free, MIT (web app "Try it free"; paid web tier not shown) | Yes | npm CLI, Claude Desktop MCP, Claude Code skill, web | Low-medium. Handmade-leaning examples, but the tag and title rule checks apply to vintage listings too. 29 stars | V | https://github.com/semihbugrasezer/seerxo |
| eBay Seller Hub "Photo upload" AI listing | eBay's own tool: "Our AI-powered tool transforms product images into detailed listing drafts in seconds." | Free inside Seller Hub | Yes | eBay web (Seller Hub) | Medium. The only photo-to-listing route eBay itself sanctions, but "Best for items that tend to be standardized, such as trading cards", so expect weak drafts for one-of-one decor | V | https://www.ebay.com/sellercenter/listings/listing-tools |
| facebook-marketplace-mcp (jdcodes1) | MCP that searches Marketplace by replaying Facebook's internal GraphQL "using your existing Facebook session cookies from Chrome" | Free; no licence file listed | Yes | macOS only ("cookie extraction uses Keychain"), Node 20+ | Skip. Breaches Meta's automated-access terms and does not run on Windows. 497 stars shows demand, not permission | V | https://github.com/jdcodes1/facebook-marketplace-mcp |
| Manus | General agent with browser, slides, "My Browser" | Prices did not render (two attempts) | Unknown | Web, mobile app, desktop app | Unknown | U | https://manus.im/pricing |
| Genspark | "AI Workspace 6.0", products include "Genspark Claw" and an AI dictation tool | Pricing page failed to load; home page has no prices | Unknown | Web, downloads | Unknown | U | https://www.genspark.ai/ |
| Perplexity Computer | Perplexity's agent product | Page returned no text (bot wall) | Unknown | Unknown | Unknown | U | https://www.perplexity.ai/computer |

## 2. Notes per tool

### Claude Cowork
- Product page (V): "Claude Cowork is now part of Claude. Just ask for what you need." "Download for Windows" and "Windows (arm64)" buttons present. "Schedule a task for any cadence, and it runs unattended." Built-in browser: "Separate from your own browser, logins, and tabs. Sign in once for every session, or import cookies to stay signed in to your browser (Chrome, Edge, and Firefox on macOS; Firefox on Windows and Linux)." Cookie import on Windows is Firefox only.
- Support article (V): "Claude Cowork is available on paid plans (Pro, Max, Ultra, Team, and Enterprise)". "Claude Desktop for macOS, Windows, and Linux (beta): Available on all paid plans." "Cowork has unique risks due to its agentic nature and internet access." "Scheduled tasks run in the cloud, with no device online."
- Terms fit: unattended cloud runs against eBay, Facebook Marketplace or Chairish breach those sites' terms as quoted in the lane 15 report, and Anthropic's Usage Policy makes the user responsible for agent actions. Etsy drafting with Ricky watching is the use.

### eBay API MCP Server (official)
- README (V): "This MCP server enables Claude Desktop, Cursor, Cline, and other AI tools to discover and call eBay marketplace APIs directly." "Simplified setup with automatic token management: Just provide Client ID and Client Secret". Limitations: "Sandbox Environment Not Supported"; "REST APIs: Only GET requests are supported (read operations only)"; "GraphQL API: Only Query operations are supported". Install: npx -y @ebay/npm-public-api-mcp; a claude mcp add command is given.
- GitHub API today: Apache-2.0, 46 stars, pushed 2026-10-27, not archived. Published by the eBay org, so it is the sanctioned automation route. Listing creation still needs the community servers (YosefHayim/ebay-mcp, already listed) or 3Dsellers.

### 3Dsellers MCP Server
- README (V): "The hosted eBay MCP server for ecommerce sellers." "120+ tools. Nothing to install, no code and no eBay developer account." "approval before any tool that changes data, a log of every call, and one-click revoke." "Sign in with OAuth". Server URL https://api.3dsellers.com/mcp. Repo is docs only (MIT), 1 star, pushed 2026-11-01; the service itself is closed.
- Pricing (V): Essential "$19" monthly, "$16 /Mo Billed Annually", "100 Listings", "1 eBay account", "Limited support (72h)". Growth "$39.90" / "$29.90 /Mo Billed Annually", "500 Listings". Professional "$79" / "$59 /Mo Billed Annually", "2,000 Listings", "Multichannel catalog". Integrations row lists Shopify, WooCommerce, Amazon (Beta), Walmart (Beta), Etsy, Facebook, TikTok. "Free 7-day trial No credit card required". AI actions are an add-on from "$9/mo".
- Gotcha: whether Etsy and Shopify publishing are available on the $19 Essential plan or only with the Professional "Multichannel catalog" is not stated in the text read; ask before paying. Facebook channel is listed but Meta's API only allows Shops, not Marketplace listings, so do not assume Marketplace posting.

### Listing Writer (hahm-ebay-lister)
- README (V): "Runs as your own private website on Vercel; works on your computer and your phone." "It's bring-your-own-keys: you plug in your own Anthropic (AI) key and your own eBay developer keys". Needs "App ID, Cert ID, and a RuName". "Only needed for posting; sorting and writing work without it." Export "as CSV / JSON".
- Licence (V, commit message on the repo page): "license: switch from MIT to FSL-1.1-MIT (free to use, not to resell". Fine for Ricky's own shop; GitHub shows NOASSERTION for the SPDX. 45 stars, pushed 2026-10-31, one maintainer.
- Fit: eBay only, and the price suggestions are AI guesses, not sold comps. Still the closest free match to "photos in, listing out" via the API route eBay allows.

### Nanobrowser
- Page (V): "It runs as a Chrome and Edge extension in the browser's side panel and works in your real, signed-in browser". Models: "Anthropic, OpenAI, Google Gemini, OpenRouter, xAI Grok, DeepSeek, Mistral ... or a model on your own computer." "Your keys and chats are stored in your browser." "In Ask mode, the default, it asks before it submits, sends, deletes or uploads anything ... It may not spot every such step, so keep an eye on it." GitHub API: Apache-2.0, 14,260 stars, pushed 2026-10-24.
- Terms: same as Claude in Chrome. A signed-in browser agent on eBay or Facebook Marketplace is still an "automated means" under their terms.

### Zapier MCP
- MCP page (V): "Zapier MCP lets Claude, ChatGPT, Cursor, and any other AI client take real action in the apps that run your business". Pricing page (V): Free "$0 /month ... (100 tasks per month)"; "Professional Starting from $19.99 /month"; "Zap workflows, AI steps, code, MCP, and SDK all draw from the same task allocation". Yearly toggle "Save 33%".
- Etsy (V): "Etsy has not yet built an integration on Zapier." Workarounds offered are webhooks and code, which means the Etsy Seller App key anyway.
- eBay (V): triggers and actions shown are "New Order", "API Request (Beta)", "Create a Shipping Fulfillment", "Find an Order". No listing creation. "Zapier checks for new data every 15 min on the Free plan".

### Secondhand MCP
- README (V): "Search Facebook Marketplace, eBay, Depop, and Poshmark for used and secondhand items". Table: Facebook Marketplace "No" auth, "Location-based search"; eBay "Yes (API keys)", "Official Browse API"; Depop and Poshmark "Requires Chrome installed". "Price: free, forever" local; Cloud "free tier, then $4.99" (period not stated). Latest commit message: "Facebook: route around the gated search API via the logged-out page". MIT, 99 stars, pushed 2026-10-05.
- Terms: Meta's Terms (quoted in the lane report) ban automated collection "regardless of whether such automated access or collection is undertaken while logged-in". The eBay part is the official API and fine.

### Dia and The Browser Company
- Plans page (V): "Free Plan: A clean, calm, effortlessly organized browser with no AI features." "Better Answers ($10/month)". "Better Days ($100/month) ... 20x more asks". "Every new Dia user gets a 14-day free trial with access to the Dia Better Days plan." "Paid plans begin rolling out to most new Mac users on August 17." "I'm on Windows, does this apply to me? Not yet." Extra usage "in $20 credits".
- Home page (V): "Download Dia for free. Available for macOS and Windows." Footer: "DESIGNED AND BUILT BY THE BROWSER COMPANY OF NEW YORK".
- Atlassian blog, September 4, 2025 (V): "We've entered into an agreement to acquire The Browser Company of New York, the team behind the incredible Dia and Arc browsers." Direction: "make Dia the browser ... Optimized for the SaaS apps where you spend your day." No listing-form agent is described.

### Fellou
- Pricing (V): Free "$0 /month", "1000 Sparks (New User Bonus) - Approximately 4 Tasks", "2 Scheduled Tasks". Plus "$19.0 /month" (annual "$192 ($16/Monthly)"), Pro "$39.9 /month" (annual "$384 ($32/Monthly)"), Ultra "$199.9 /month". "Actual consumption varies significantly based on workflow complexity."
- Download (V): Mac OS Apple and Intel builds; "Windows Download the CE version".
- Home FAQ (V): "It is designed to handle logins, authentication, and even CAPTCHA challenges. Advanced AI can solve CAPTCHAs with high accuracy by simulating human behavior." Also "automates deep research ... including logged-in accounts on platforms like Reddit". That is scraping by another name and would breach eBay's and Meta's terms if pointed at them.

### Brave Leo
- Leo page (V): "Brave Leo is free to use. Or it's available as a premium experience, with access to more models and even faster responses." "No account or login is required." "Bring your own models".
- Checkout page (V): "7-day free trial. Annual payment Save ~17% $12.50 /month. $149.99 /year. Monthly payment $14.99 /month." "Leo AI is available exclusively in the Brave browser."

### Apple Visual Intelligence
- Apple page (V): "Search and take action with Visual Intelligence, now on even more devices". "Apple Intelligence is compatible with these devices." followed by a list that begins with iPhone 18 Pro Max, iPhone 17 Pro, iPhone Air, iPhone 17 and includes iPhone 16 further down. Siri AI "is available in beta in iOS 27". Whether Ricky's iPhone is on the list is unknown (U). Free with the device; nothing to install.

### OpenClaw
- Site (V): "OPEN SOURCE. RUNS ON YOUR MACHINE. NOBODY'S BUSINESS MODEL." "No subscription. No hosted tier. No token. Stewarded by an independent 501(c)(3)." Desktop apps: "macOS 15+", "Windows 10/11 x64 or ARM64 v2026.9.8-1", Linux. Testimonials on the page include "you can sign in to openclaw with your chatgpt account now and use your subscription there" (attributed to @sama) and a Microsoft Build quote; treat as marketing.
- GitHub API (V): MIT, 394,144 stars, 82.8k forks, pushed 2026-11-07. The repo lists a SECURITY.md and a "Security and quality" tab with 722 items; a self-hosted agent that reads your inbox is a real attack surface for a one-person shop.

### Browser Use, Skyvern, Stagehand and Browserbase
- Browser Use (V): "Pay as you go. No subscription." Browsers "$0.02 per browser hour", home-IP proxy "$5 / GB", "CAPTCHA solving Included", harness "$0 open source ... License MIT". "Start with $1 free. One per person." GitHub: 120,262 stars, MIT, pushed today.
- Skyvern (V): "Hobby ... $29/month", "Pro ... $149/month", "Estimated actions ~1,200/month" on Hobby, "Basic CAPTCHA solver". GitHub: AGPL-3.0, 23,361 stars. AGPL matters only if Ricky ever redistributes a modified server.
- Stagehand (V): "Stagehand is the SDK for browser agents", "26k stars", MIT per GitHub API (25,979 stars). Browserbase (V): "Free Plan $0/mo", "Developer Plan $20/mo", "Startup Plan $99/mo"; "Captcha Solving: No" on Free.
- All three sell stealth browsing and CAPTCHA solving, which is the toolkit marketplaces write their anti-bot clauses against. Not for Hollie.

### n8n, Composio, Pipedream
- n8n (V): "Pricing is based on monthly workflow executions"; Starter "20€ /mo, billed annually"; Pro "50€ /mo, billed annually"; "Community Edition: A standard, self-hosted version of n8n is available on GitHub." Agents and MCP included on all cloud plans. Etsy: no built-in node; community node mesutkisi11/n8n-nodes-etsy (MIT, 3 stars, pushed 2026-07-29) covers "listings, orders, inventory and a polling trigger for new orders".
- Composio (V): "Hobby $0 ... 100,000 tool calls / mo", "hard-capped, needs no credit card". "Pro $29 / mo". Shopify toolkit page exists; the Etsy toolkit URL returns 404.
- Pipedream (V): "Free $0 ... Everything you need to build and test"; "Production environment: Not included" on Free; "Startup $99 per month". eBay MCP page: "We don't have any tools available for this app yet." Shopify MCP page exists. Etsy: "MCP Server Not Found".

### Mistral Vibe, Grok, Aqua Voice
- Mistral (V): plan names Free, Pro "$14.99 /mo Excluding taxes", Team "$24.99 /user/mo". Interfaces listed: "Vibe on web, Vibe CLI, Vibe for IDE, Vibe on mobile (iOS and Android)". The string "Le Chat" does not appear on the pricing page. Students "$5.99 / month".
- Grok (V): "Available on Web, iOS and Android". "Free to try on the web and in the apps. Upgrade to SuperGrok for higher limits and multi-agent reasoning." Page footer: "SpaceX Super Intelligence LLC". SuperGrok price not on the page; grok.com served a wall (U).
- Aqua Voice (V): "Free: Try voice typing. $0 to start. 1,000 Words"; Pro "Unlimited dictation"; Max "Realtime Mode, Voice Commands". Platforms footer: "macOS Windows iOS Android". Use cases list "Claude Code" and "Codex". Paid amounts did not render (U).

### eBay Seller Hub Photo upload
- Seller Center (V): "Photo upload: Best for items that tend to be standardized, such as trading cards. Our AI-powered tool transforms product images into detailed listing drafts in seconds. Simply bulk upload photos of what you want to list". Also "Advanced listing tool ... Just describe your item and we'll start your listing based on similar items." Free inside Seller Hub. The marketing name "magical listing" is not on this page.

### Defunct, acquired or renamed (evidence)
- Copilot Pro (seed item): https://www.microsoft.com/en-us/store/b/copilotpro now redirects to the Microsoft 365 Premium product page: "$199.99/year ... Buy now $19.99/month Try free for 1 month". The lane list's Microsoft row already prices M365 Premium; add that Copilot Pro as a product is gone. (V)
- The Browser Company (Dia, Arc): acquired by Atlassian, agreement announced September 4, 2025 ("the team behind the incredible Dia and Arc browsers"). Dia keeps its name. (V)
- Mistral Le Chat: the pricing page sells the assistant as "Vibe" on web, CLI, IDE and mobile; "Le Chat" is absent from the page text. Rename inferred from absence, so treat as likely, not certain. (V page, U on the rename itself)
- Genspark "Super Agent": the home page now says "Genspark AI Workspace 6.0" and lists "Genspark Claw"; pricing page would not load. Name change not confirmed. (U)
- Shopify Dev MCP to AI Toolkit, Shopify Magic into Sidekick, ChatGPT agent, Operator and Atlas retired: already recorded by the first agent; nothing further found.
- Nothing else on the lane 15 list is defunct as far as today's pages show. Claude Cowork and chat are merging ("Claude Cowork and chat are one Claude"), which may change the Claude in Chrome row's wording later.

## 3. Recommendation for Hollie

Top picks, free first:
1. Open Claude Cowork on the Windows PC today (it is in the plan Ricky already pays for) and use its built-in browser or Claude in Chrome for Etsy listing drafts, buyer-reply drafts and comps reading, always with Ricky watching. Do not create scheduled or unattended tasks that touch eBay, Facebook Marketplace or Chairish.
2. When Step 0 produces eBay developer keys, install eBay's own MCP server first (npx -y @ebay/npm-public-api-mcp, read-only) for sold-comps research in Claude Code. Keep YosefHayim/ebay-mcp (already listed) for listing writes.
3. Try Apple Visual Intelligence on the iPhone at estate sales if the phone supports it. Zero cost, zero install.

Pay only once it earns it:
- 3Dsellers Essential ($19 a month, 7-day trial) only if the Crosslist Gold trial disappoints and Ricky wants chat-driven listing to eBay, Etsy and Shopify without developer keys. Confirm Etsy and Shopify publishing on the Essential tier first.
- Zapier Free (100 tasks) is enough later for Shopify order alerts; Etsy is not supported there, so it does not replace the Etsy Seller App route.

Skip and why:
- Fellou, Browser Use cloud, Skyvern, Browserbase: they advertise CAPTCHA solving and stealth, which is what eBay's and Meta's terms are written against, and they add nothing for a 50-item vintage shop.
- Dia ($10 a month, Mac first, Windows not yet), Brave Leo Premium ($14.99 a month), Mistral Pro ($14.99 a month), SuperGrok: all duplicate what Claude already does for Ricky.
- OpenClaw and n8n self-hosting: real projects, but each is a second agent stack to secure and maintain. Revisit only if the dashboard build wants a scheduler on the Fedora box.
- facebook-marketplace-mcp (cookie replay, macOS only) and the Facebook half of Secondhand MCP: breach Meta's automated-access terms. Marketplace stays manual.
- Listing Writer and seerxo: good free code to borrow ideas from (photo batching, SKU bins, 13-tag rules), but running a Vercel app beside the planned Supabase dashboard is a second system. Fold the ideas into the dashboard handoff instead.

## 4. Gaps and pages that would not load

- WebSearch budget was exhausted before this agent started; discovery relied on known vendor URLs and GitHub's search API. Tools that only appear in 2026 roundups could have been missed.
- Manus pricing (https://manus.im/pricing): page shell loaded twice, no prices rendered. U.
- Genspark pricing (https://www.genspark.ai/pricing): failed to load; home page has no prices. U.
- Perplexity Computer (https://www.perplexity.ai/computer): zero text, bot wall. U.
- grok.com: wall; SuperGrok price not found on x.ai/grok. U.
- Make.com pricing: HTTP 403. Not included.
- Flyp (flyp.com, www.flyp.com): bot wall both ways. Not included (crosslisting is lane 01 anyway).
- Aqua Voice paid prices and 3Dsellers per-tier channel limits did not appear in rendered text. U on those details.
- Mistral rename to Vibe inferred from the absence of "Le Chat" on the pricing page; no announcement page read.
- GitHub per-repo API endpoint not enabled for this session; star counts come from the search endpoint, which can lag slightly.
- Etsy legal pages and 1stDibs terms remain unread (bot-walled for the first agent; not retried here).
- FLUF-io/awesome-reseller-tools (GitHub list) names FLUF Connect ("AI listing creation", 55+ marketplaces) and Storminder ("AI Assistant inventory, listing, pricing, and item identification tools"); both are crosslisting or inventory tools for lane 01 or 09, not fetched here.

## 5. Sources (every URL fetched today, 2026-11-07)

https://claude.com/cowork (redirects to https://claude.com/product/cowork)
https://support.claude.com/en/articles/13345190-getting-started-with-cowork (redirects to https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork)
https://www.diabrowser.com/
https://www.diabrowser.com/pricing (redirects to https://www.diabrowser.com/plans)
https://www.diabrowser.com/about (404)
https://thebrowser.company/ (curl only, 307 chars)
https://www.atlassian.com/blog/announcements/atlassian-acquires-the-browser-company (redirects to https://www.atlassian.com/blog/company-news/atlassian-acquires-the-browser-company)
https://fellou.ai/
https://fellou.ai/pricing
https://fellou.ai/download
https://brave.com/leo/
https://account.brave.com/?intent=checkout&product=leo
https://browser-use.com/pricing
https://www.skyvern.com/pricing
https://www.stagehand.dev/
https://www.browserbase.com/pricing
https://nanobrowser.ai/
https://openclaw.ai/
https://github.com/openclaw/openclaw
https://manus.im/pricing (prices did not render, two attempts)
https://www.genspark.ai/pricing (FETCH FAILED)
https://www.genspark.ai/
https://www.perplexity.ai/computer (empty, bot wall)
https://zapier.com/mcp
https://zapier.com/pricing
https://zapier.com/apps/etsy/integrations
https://zapier.com/apps/ebay/integrations
https://n8n.io/pricing/
https://composio.dev/pricing
https://composio.dev/toolkits/shopify
https://composio.dev/toolkits/etsy (404)
https://pipedream.com/pricing
https://pipedream.com/apps/etsy (404)
https://mcp.pipedream.com/app/etsy (MCP Server Not Found)
https://mcp.pipedream.com/app/ebay
https://mcp.pipedream.com/app/shopify
https://www.make.com/en/pricing (HTTP 403)
https://www.flyp.com/ (bot wall)
https://flyp.com/ (bot wall)
https://mistral.ai/pricing (redirects to https://mistral.ai/pricing/)
https://x.ai/grok
https://grok.com/ (bot wall)
https://www.apple.com/apple-intelligence/
https://www.microsoft.com/en-us/store/b/copilotpro (redirects to https://www.microsoft.com/en-us/microsoft-365/p/microsoft-365-premium/cfq7ttc11z3q)
https://www.ebay.com/sellercenter/listings/listing-tools
https://withaqua.com/pricing (redirects to https://aquavoice.com/pricing)
https://github.com/eBay/npm-public-api-mcp
https://github.com/3dsellers/ebay-mcp-server
https://www.3dsellers.com/pricing
https://github.com/ashnicholes-droid/hahm-ebay-lister
https://github.com/semihbugrasezer/seerxo
https://github.com/jlsookiki/secondhand-mcp
https://github.com/jdcodes1/facebook-marketplace-mcp
https://raw.githubusercontent.com/FLUF-io/awesome-reseller-tools/main/README.md
https://api.github.com/search/repositories (queries: repo:browser-use/browser-use, repo:Skyvern-AI/skyvern, repo:nanobrowser/nanobrowser, repo:browserbase/stagehand, repo:openclaw/openclaw, repo:GeLi2001/shopify-mcp, mcp org:eBay, mcp org:etsy, mcp org:Shopify, etsy mcp, ebay mcp, shopify mcp server, etsy listing ai, ebay listing ai, reseller ai agent, poshmark mcp, facebook marketplace mcp, chairish, crosslist)
