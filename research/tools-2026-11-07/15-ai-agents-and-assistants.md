# Lane 15: AI assistants and browser agents for a one-person reseller

Date 2026-11-07. Author: research subagent. Question: Which AI assistants and browser agents (2026) can do reseller work for one person (draft listings from photos, fill listing forms in the browser, research comps, write buyer replies, summarize auctions), and which of these do Etsy, eBay, Shopify, Facebook and Chairish terms allow? Legend: V = page read today; U = unverified (snippet, memory, or the page would not load).

Method note. WebFetch was broken, so every page was read through a headless Chromium fetch script via the session proxy, with curl fallback. The shared WebSearch budget ran out partway through, so the sweep stayed on vendor URLs that could be addressed directly plus GitHub's own repo search (via the `gh` CLI, GitHub API). No roundups were used for prices. No subagents.

## 0. Bottom line

- Ricky already pays for a Claude plan to run Claude Code, and Claude in Chrome is included on every paid plan ("Available on all paid plans"). It reads the open page, clicks, types and fills forms. That is the browser agent to use first, at no extra cost. (V)
- The browser agent is not allowed everywhere. eBay's User Agreement now names "LLM-driven bots" and "buy-for-me agents" among the automated means banned without eBay's express permission. Facebook bans automated access or collection without prior permission. Chairish bans processes that run while you are not logged in and any crawling or scraping. So: use Claude in Chrome for Etsy drafting and research with Ricky watching, but let eBay listings go through eBay's API (an MCP server or Crosslist), not a browser agent. (V)
- Etsy's own legal pages (API terms, terms of use) were bot-walled today (HTTP 403). What did load: Etsy's developer docs offer a "Seller App" path, "Automated, near-instant for eligible sellers", "Your shop only", "Commercial use: Not permitted". That is the sanctioned way for Ricky's own tools to touch his own shop. Etsy's stance on AI filling the seller UI is unverified. (V for docs, U for stance)
- OpenAI's consumer agent landscape changed. The help center says "ChatGPT agent is no longer available" and "ChatGPT Atlas has been retired and no longer receives updates." The replacement is ChatGPT Work with a cloud browser, "excluding Free and Go." ChatGPT Plus and Go monthly prices did not render on the pricing page (amounts come from a separate price API), so they are U. Pro is $100, $200 or $500 a month. (V)
- Google's agent is cheapest among the paid browsers: Gemini in Chrome "auto browse" is bundled with Google AI Pro at "$19.99/ month" and is "Rolling out first in preview to Google AI Pro and Ultra subscribers in the U.S." Gemini Free ($0) still reads photos and drafts text. (V)
- Shopify's own agent, Sidekick, is "BUILT INTO EVERY STORE" at no extra cost above the store plan (Basic "$39 USD/mo" monthly or "$29 USD/mo" yearly). It writes product copy, edits phone photos "to studio shots", and "presents changes for your review before applying them." Claude also has an official Shopify connector and a Shopify AI Toolkit plugin for Claude Code. Shopify's old Storefront MCP was removed in favor of UCP. (V)
- Dictation for listings is free on both of Ricky's devices: Windows voice typing (Win+H, Azure speech, online) and iPhone Dictation (on-device, no internet needed). Wispr Flow Free adds AI cleanup on Mac, Windows, iOS and Android with "Limited words per week"; Pro is "$12/user/mo". Superwhisper Pro shows "$8.49/month" on the yearly toggle. (V)
- Community MCP servers exist for both marketplaces and use the official APIs. eBay: YosefHayim/ebay-mcp, 194 stars, MIT, 828 commits, updated 2026-11-06. Etsy: aserper/etsy-mcp, 12 stars, MIT, 37 tools, pushed 2026-11-07. Both need Ricky's own developer keys, which are still the Step 0 blocker. (V)

## 1. Comparison table

| Tool | What it does | Price (verbatim quote) | Free tier | Platform | Fit for Hollie | V/U | Source URL |
|---|---|---|---|---|---|---|---|
| Claude (claude.ai) Free / Pro / Max / Ultra | Chat, photo ID, listing drafts, buyer replies, web search, connectors, Claude Code on paid plans | Free "$0"; Pro "$17 Per month with annual subscription discount ($200 billed up front). $20 if billed monthly."; Max "$100 Per month"; Ultra "$200 Per month" | Yes: "Limited usage every 5 hours and every week", Sonnet and Haiku, web search, connectors, up to 5 projects | Web, Windows, Mac, iOS, Android | High. Ricky already has a paid plan for Claude Code; everything here is included | V | https://claude.com/pricing |
| Claude in Chrome | Browser agent: "reads the page you're signed in to, then clicks, types, and fills forms while you decide what happens next" | "Available on all paid plans." No separate charge | No (paid plans only) | Chrome extension (side panel), also from Claude Cowork and Claude Code | High for Etsy drafting and comps with Ricky watching. Do not point it at eBay (see eBay terms) | V | https://claude.com/claude-in-chrome and https://support.claude.com/en/articles/12012173-get-started-with-claude-in-chrome |
| Claude Code | Terminal agent; runs MCP servers (Etsy, eBay, Shopify) and the Shopify AI Toolkit plugin | "Claude Code is included in all paid plans." Team seat "$20" shown on product page | No | Windows, Mac, Linux terminal; web; IDE | High. Already in use | V | https://claude.com/pricing and https://claude.com/product/claude-code |
| Claude connectors (Shopify, Canva, Notion, Gmail, Google Drive, Squarespace, Supabase) | Lets Claude act in those apps directly; Shopify: "Build, manage, and analyze your Shopify store" | Included in plans; "Connectors: Yes" on Free through Ultra | Yes | Web and desktop Claude | High once the Shopify store exists | V | https://claude.com/connectors |
| ChatGPT Free / Go / Plus / Pro | Chat, photo uploads, "ChatGPT Work" agent for multi-step tasks; cloud browser on paid plans | Pro: "$100", "$200", "$500" monthly (help center). Plus and Go: amounts did not render (U). Free "Unlimited text chats with GPT-6", "Limited messages with uploads" | Yes: "Limited messages with uploads", "Limited ChatGPT Work access on desktop" | Web, Windows, Mac, iOS, Android | Medium. Second opinion on photo ID at $0; paying for Plus duplicates Claude | V (Pro, Free features) / U (Plus, Go price) | https://openai.com/chatgpt/pricing/ and https://help.openai.com/en/articles/9793128-what-is-chatgpt-pro |
| ChatGPT agent mode / Operator | Former browser agent | Retired: "ChatGPT agent is no longer available. Use ChatGPT Work for longer, multi-step tasks" | n/a | n/a | Skip | V | https://help.openai.com/en/articles/11752874-chatgpt-agent |
| ChatGPT Work cloud browser | "its own browser on a separate computer in the cloud. It can read web pages, click buttons, enter information into forms" | Included in paid plans; "available in ChatGPT Work on paid ChatGPT plans in supported regions, excluding Free and Go" | No | Web and mobile (runs in OpenAI's cloud) | Medium. Works unattended, which is exactly what marketplace terms dislike; "Some websites use security measures that restrict access from automated browser agents" | V | https://help.openai.com/en/articles/20001280-using-cloud-browser-in-chatgpt |
| ChatGPT Atlas browser | Former AI browser (Mac) | Retired: "ChatGPT Atlas has been retired and no longer receives updates." | n/a | Was macOS only | Skip | V | https://help.openai.com/en/articles/20001371-chatgpt-atlas-retirement |
| Gemini app (Free / Google AI Plus / Pro / Ultra) | Chat, photo ID, drafting; Pro adds Gemini in Chrome auto browse | Free "$0/ month with a Google Account"; Plus "$4.99/ month"; Pro "$19.99/ month"; Ultra "$99.99/ month" (5x) and "$199.99 / month" (20x) | Yes, $0 with Google account; usage "refreshes every 5 hours until you reach your weekly limit" | Web, Android, iOS, Chrome | Medium. Free tier is a good second opinion on photo ID | V | https://gemini.google/subscriptions/ |
| Gemini in Chrome (auto browse) | "tell Gemini what you need and watch it handle the rest on your behalf" | Bundled in Google AI Pro "$19.99/ month" ("Access Chrome auto browse to help complete tasks for you") | Summaries and tab compare yes; auto browse no | Chrome desktop; Android; "On iOS, we built Gemini right into the Chrome app" | Medium. "Rolling out first in preview to Google AI Pro and Ultra subscribers in the U.S." Same ToS limits as any browser agent | V | https://gemini.google/overview/gemini-in-chrome/ |
| Perplexity Comet | AI browser with an assistant that browses, emails, shops | Price not verified: pricing page 404, help center Cloudflare-walled, Comet FAQ answers did not render | Unknown (FAQ asks "Is Comet free?" but answer did not load) | "Available for Mac, Windows, iOS, and Android" | Low until price and terms are verifiable | U (platform V) | https://www.perplexity.ai/comet |
| Microsoft Copilot in Edge (Copilot Mode) and Copilot app | Free summaries, tab comparison, drafting in Edge; paid tiers raise usage | Microsoft 365 Personal "$9.99/month" (or $99.99 a year); Family "$12.99/month" (or $129.99); Premium "$19.99/month" (or $199.99); free tier implied by "Higher usage than free" | Yes, free in Edge and the Copilot app | Windows, Edge, iOS, Android | Low to medium. Good for free comp summaries across tabs; no verified form-filling on the pages read | V | https://www.microsoft.com/en-us/edge/copilot-mode and https://www.microsoft.com/en-us/copilot/solutions/individuals |
| Opera Neon | Agentic browser: "works on your tasks, interprets the web, manages tabs, acts when you command" | "Subscribe to Neon to activate agentic functionalities and top world LLMs." "$19.90/month" | Browser and "Free VPN" yes; agent features need the subscription | Desktop browser (OS list not captured on page) | Low. Costs the same as Gemini Pro with less to show | V | https://www.operaneon.com/ |
| Shopify Sidekick (and Shopify Magic) | Store AI: "edit orders", "create content, such as product descriptions and images", photo editor, writes Flow automations, "presents changes for your review before applying them" | "BUILT INTO EVERY STORE". Store plans: Basic "$39 USD/mo" monthly, "$29 USD/mo" yearly; "Try 3 days free, then $1/month for 3 months." | Included with any store plan | Shopify admin web and the Shopify app (desktop and mobile), voice mode | High. Free with the store Ricky plans anyway | V | https://www.shopify.com/sidekick and https://help.shopify.com/en/manual/ai-powered-tools/sidekick and https://www.shopify.com/pricing |
| Shopify AI Toolkit (was Dev MCP) | Claude Code plugin: docs, schema validation, "Store management: prepare and run supported store-management tasks through Shopify CLI's authenticated store context" | Free. "claude plugin install shopify-ai-toolkit@claude-plugins-official" | Yes | Claude Code, Codex, Cursor, VS Code | High for the storefront build | V | https://shopify.dev/docs/apps/build/ai-toolkit |
| Shopify Storefront MCP | Catalog and cart tools for buyer-side agents | Removed: "The catalog and cart tools on https://{shop}/api/mcp were removed. Use the Universal Commerce Protocol (UCP) instead." | n/a | n/a | Not for Hollie now | V | https://shopify.dev/docs/apps/build/storefront-mcp |
| Etsy Open API v3 Seller App | Sanctioned path for a seller's own tools (and for Etsy MCP servers) | Free. "Approval: Automated, near-instant for eligible sellers"; "Shop access: Your shop only"; "Commercial use: Not permitted" | Yes | Etsy integration (OAuth) | High. The only verified Etsy automation route today | V | https://developers.etsy.com/documentation/ |
| Etsy MCP servers (GitHub) | Claude manages listings, images, inventory via Etsy API. aserper/etsy-mcp: "37 tools for listings, orders, shipping, reviews, inventory, payments" | Free, MIT (aserper). administrativetrick: 20 stars but "3 Commits", initial commit only; georgejeffers 13 stars; aserper 12 stars, pushed 2026-11-07 | Yes | Claude Desktop / Claude Code (local MCP) | Medium. Young, single-maintainer projects; need Ricky's Etsy app key | V | https://github.com/aserper/etsy-mcp and https://github.com/administrativetrick/etsy-mcp-server |
| eBay MCP servers (GitHub) | Claude manages eBay listings, orders, marketing via eBay Sell APIs. YosefHayim/ebay-mcp: "OAuth 2.0 built in", "Sandbox and production" | Free, MIT. 194 stars, 828 commits, updated 2026-11-06. Also jbwashington/ebay-mcp (17 stars, Claude Code plugin with image analysis and pricing research) | Yes | Claude Desktop / Claude Code (local MCP) | Medium-high. API route is the one eBay's terms allow; needs eBay developer keys (Step 0) | V | https://github.com/YosefHayim/ebay-mcp |
| Windows voice typing | Dictate anywhere on the PC with Win+H | Free with Windows 11 | Yes | Windows 10 and 11 | High. Zero install | V | https://support.microsoft.com/en-us/windows/use-voice-typing-to-talk-instead-of-type-on-your-pc-fec94565-c4bd-329d-e59a-af033fa5689f |
| iPhone Dictation | Dictate anywhere you can type; "no internet connection is required" | Free with iOS | Yes | iOS | High. Zero install | V | https://support.apple.com/guide/iphone/dictate-text-iph2c0651d2/ios |
| Wispr Flow | AI dictation that cleans up speech; "Learns your names and jargon" | Free "$0/mo"; Pro "$12/user/mo"; Growth "$18/user/mo" (monthly toggle; "Annual 20% discount") | Yes: "Limited words per week" | "Free on Mac, Windows, iPhone and Android" | Medium. Try Free; Pro only if the weekly cap bites | V | https://wisprflow.ai/pricing |
| Superwhisper | AI dictation, own API keys, offline models on Apple Silicon | Pro "$8.49" "/month" on the "Yearly(2 months free)" toggle; monthly and "Lifetime" amounts did not render | Yes: "try the Pro features for 3,000 words for free, after that the free tier features are available to you forever" | "Available on Mac, Windows, iOS and Android" | Low to medium. Wispr Flow Free covers the same need | V (partial) | https://superwhisper.com/ |

## 2. Notes per tool

### Claude plans, Claude in Chrome, Claude Code, connectors
- Pricing page lists Free $0, Pro $17 per month on annual ($200 up front) or $20 monthly, Max $100 per month, Ultra $200 per month. Feature table: "Claude in Chrome: No / Yes / Yes / Yes" across Free / Pro / Max / Ultra. "Claude Code is included in all paid plans."
- Chrome page: "Claude in Chrome reads the page you're signed in to, then clicks, types, and fills forms while you decide what happens next." Two approval styles: "Let Claude work with a safety check on each action, or approve one site at a time in Permissions Mode." "Purchases, financial actions, and anything you can't undo wait for you." Claude also has a built-in cloud browser now ("nothing to install"); switch in Settings, Capabilities, Preferred browser.
- Support article: "available on paid plans (Pro, Max, Ultra, Team, and Enterprise), in the Chrome side panel, Claude Cowork, and Claude Code. The side panel runs as a Claude Cowork session." Warning: "enhanced with our safety classifiers but is still risky."
- Vision uploads (chat): "File size: 500MB per file", "Number of files: Up to 20 files per chat", "Image dimensions: Up to 8000x8000 pixels". Project files: 30MB per file. The article does not split limits by plan; Free is gated by usage, not file size. Tip from the page: "Use images that are 1000x1000 pixels or larger."
- Connectors directory lists Shopify ("Build, manage, and analyze your Shopify store"), Squarespace, Canva, Notion, Slack, Gmail, Google Drive, Supabase. Connectors are "Yes" on all plans in the pricing table.
- Anthropic Usage Policy (V): prohibits "Engage in actions or behaviors that circumvent the guardrails or terms of other platforms or services" and "Utilize automation in account creation or to engage in spammy behavior." Agentic clause: "Users are responsible for ensuring that agents they build or deploy, including actions those agents take through tools, browsers, or connected systems, comply with this Usage Policy." So using Claude in Chrome against eBay's ban would also breach Anthropic's policy.
- Gotcha: the usage pool is shared. "Your activity across Claude on web, desktop, mobile, and Claude Code all draws from the same pool." Browser sessions eat into Claude Code budget.

### ChatGPT (OpenAI)
- Pricing page text lists plans Free, Go, Plus, Pro but the dollar amounts come from a separate price token and never appeared in the rendered text or HTML. Free: "Unlimited text chats with GPT-6", "Limited messages with uploads", "Limited ChatGPT Work access on desktop". Go: "This plan may include ads." Plus: "Expanded access to ChatGPT Work on desktop, web, and mobile". Pro: "Your choice of 3 usage tiers". Help center (V): Pro 100 "$100", Pro 200 "$200", Pro 500 "$500" monthly.
- Agent mode help article (V, updated 11 days ago): "ChatGPT agent is no longer available. Use ChatGPT Work for longer, multi-step tasks and finished deliverables." The same page still lists stale limits ("Plus: 40 messages/month"); treat those as historical.
- Cloud browser (V): "Cloud browser is available in ChatGPT Work on paid ChatGPT plans in supported regions, excluding Free and Go." It "pauses when it needs your input, sign-in, or confirmation." Sign-in goes through "the secure sign-in form" and "ChatGPT does not store those sign-in credentials." Default site permission is "Always ask". Warning: "Some websites use security measures that restrict access from automated browser agents."
- Atlas (V): retired. The launch post (still online) said agent mode in Atlas was "launching in preview to Plus, Pro and Business users"; moot now.
- OpenAI Usage Policies (V): no clause found about other platforms' terms in the grep (automation, scraping, third party, circumvent). The page bans "circumventing our safeguards" and "automation of high-stakes actions in sensitive areas without human review." Marketplace listing is not in its sensitive-area list.
- Operator help article returned empty; Operator is superseded (U on exact status).

### Gemini and Gemini in Chrome (Google)
- Subscriptions page (V): Free "$0/ month with a Google Account"; Google AI Plus "$4.99/ month" ("2x higher usage access than Free"); Google AI Pro "$19.99/ month" ("4x higher usage access than Free", includes "Gemini in Chrome", "Access Chrome auto browse to help complete tasks for you"); Ultra "$99.99/ month: 5x higher usage limits vs. AI Pro" and "$199.99 / month: 20x". Footnote: "Your limit refreshes every 5 hours until you reach your weekly limit."
- Gemini in Chrome page (V): auto browse "Rolling out first in preview to Google AI Pro and Ultra subscribers in the U.S." Summaries and tab comparison work without the paid tier. "Gemini in Chrome activates only when you choose to use it."
- Age and region: "Google AI plans ... are only available for ages 18+" and "available in more than 140 countries."
- Fit: Gemini Free is the cheapest second camera-ID opinion. Auto browse is the cheapest paid browser agent if Ricky ever drops Claude, but it carries the same marketplace-terms problem.

### Perplexity Comet
- Comet page (V via curl): "Available for Mac, Windows, iOS, and Android". FAQ headings include "Is Comet free?" but the answers did not render. On a second attempt the page served a Cloudflare "Performing security verification" wall. perplexity.ai/pricing returned 404. The help center index loaded but its Comet and Subscription collections returned HTTP 403 "Just a moment...". Price: U. Skip until verifiable.

### Microsoft Copilot (Edge, Windows)
- Edge Copilot Mode (V): "Copilot is built into Edge"; "Copilot can analyze content across many open tabs at once, combining insights to answer questions, compare information". Pages read describe summarize, compare, draft; no verified click-and-fill agent on the consumer page.
- Plans (V): Microsoft 365 Personal "$9.99/month" (or "$99.99" a year), Family "$12.99/month" (or "$129.99"), Premium "$19.99/month" (or "$199.99"). Each lists "Higher usage than free", so a free tier exists in the Copilot app and Edge.
- The copilot/pricing URL rendered navigation only; use the solutions/individuals page.

### Opera Neon
- (V) "Opera Neon is a browser built to act." "Subscribe to Neon to activate agentic functionalities and top world LLMs." "See everything Neon unlocks for $19.90/month here". "Connect them to Neon through MCP or CLI." Free VPN and ad blocking included without subscription. OS support not captured in the page text (U).

### Shopify Sidekick, Magic, AI Toolkit, MCP
- shopify.com/magic now redirects to shopify.com/sidekick; Magic features are folded into Sidekick (V).
- Sidekick page (V): "BUILT INTO EVERY STORE"; "Photo editor: Upgrade your phone photos to studio shots."; "Writer: Hook shoppers with irresistible product copy."; 2026-10-24 note: "Sidekick can now generate images with transparent backgrounds".
- Help center (V): "Sidekick works with your store's data and presents changes for your review before applying them." "Longer tasks continue in the background". "Automate tasks: Sidekick can build Shopify Flow workflows". "You can chat with Sidekick from any page in your Shopify admin on desktop or in the Shopify app, or use voice mode and screen sharing."
- Store cost (V): "Pay monthly $39 USD/mo" / "Pay yearly $29 USD/mo" for Basic; trial "Try 3 days free, then $1/month for 3 months." Marketplace sync: "50 synced marketplace orders per month: Free", then "1% up to $99/mo".
- Shopify AI Toolkit (V, the old Dev MCP URL redirects here): plugin for Claude Code ("claude plugin install shopify-ai-toolkit@claude-plugins-official"), or skills ("npx skills add Shopify/shopify-ai-toolkit"), or "Install with the Dev MCP server". "Store management: prepare and run supported store-management tasks through Shopify CLI's authenticated store context, with you choosing when to execute them."
- Storefront MCP (V): removed, replaced by UCP at "/api/ucp/mcp". Merchants wanting buyer chat are told to "use the Inbox agent in Shopify Inbox."
- Terms: Shopify ships its own agent and an official Claude connector, so AI use in the admin is sanctioned by design. No prohibition was needed or found.

### Etsy
- etsy.com/legal/api and /legal/terms-of-use: HTTP 403 bot wall today. Could not quote the API Terms or the stance on AI filling the seller UI (U).
- developers.etsy.com (V): "Seller Apps are for individual Etsy sellers who want to connect an app to their own shop data. This is the recommended starting point if you are a shop owner building custom tools, automations, reports, or workflows for your shop only." Table: Seller App approval "Automated, near-instant for eligible sellers"; shop access "Your shop only"; commercial use "Not permitted". Eligibility: "Any seller with an active Etsy shop in good standing who doesn't already have an active app." Apps "must comply with Etsy's API Terms of Use" and must display "The term 'Etsy' is a trademark of Etsy, Inc. This application uses the Etsy API but is not endorsed or certified by Etsy, Inc."
- Practical reading: an Etsy MCP server run by Ricky under a Seller App key is the sanctioned route. A browser agent typing into the Etsy listing form while Ricky watches is a human-supervised use of the normal UI; Etsy's position on that is unverified, so keep Ricky in the loop and never run it unattended.

### eBay
- User Agreement (V, 76 KB page loaded): you agree not to "use any robot, spider, scraper, data mining tools, data gathering and extraction tools, or other automated means (including, without limitation buy-for-me agents, LLM-driven bots, or any end-to-end flow that attempts to place orders without human review) to access our Services for any purpose, except with the prior express permission of eBay". This language explicitly covers browser agents like Claude in Chrome, Gemini auto browse and ChatGPT cloud browser.
- Same document: "eBay's automated systems may scan and analyze the contents of every message sent through its messaging platforms". AI-drafted buyer replies pasted by Ricky are fine; bots sending them are not.
- Allowed route: eBay's developer APIs with Ricky's own keys (what the MCP servers and Crosslist use). YosefHayim/ebay-mcp README: "You are responsible for complying with eBay's API License Agreement".

### Facebook Marketplace (Meta)
- Terms of Service (V): "You may not access or collect data from our Products using automated means (without our prior permission) or attempt to access data you do not have permission to access, regardless of whether such automated access or collection is undertaken while logged-in to a Facebook account."
- Automated Data Collection Terms (V, effective October 7, 2024): "You will not engage in Automated Data Collection without first obtaining Meta's express written permission".
- Commerce Policies (V): no automation clause; they govern what may be sold.
- No public Marketplace listing API was found on the pages read; the earlier-research claim that Marketplace has no API stands as U today. Browser agents on Marketplace breach the ToS quote above. Manual posting only.

### Chairish and 1stDibs
- Chairish Terms of Service (V, help center article 44208742405649): users agree not to run "any processes that run or are activated while you are not logged into the Services, or that otherwise interfere with the proper working of the Services" and not to engage in anything that "'crawls,' 'scrapes,' or 'spiders' any page, data, or portion of or relating to the Services or Content (through use of manual or automated means)". chairish.com/terms and four similar paths return 404; the live terms live on support.chairish.com.
- 1stDibs: /about/terms/ and /about/terms-of-use/ serve a JavaScript shell with no text to either headless Chromium or curl. Unreadable today (U). 1stDibs is a vetted dealer platform ("Seller Application" link on the homepage), so it is not a quick channel for Hollie anyway.

### MCP servers on GitHub (GitHub API via gh search repos, 2026-11-07)
- eBay: YosefHayim/ebay-mcp, 194 stars, updated 2026-11-06, MIT, "828 Commits", "Local MCP server that connects AI assistants to eBay seller APIs for listings, orders, and marketing, with OAuth setup." README: "smart fallback from user tokens (10k–50k req/day) to client credentials (1k req/day)", "Sandbox and production — switch environments with a single variable", "Unofficial, third-party project — not affiliated with or endorsed by eBay Inc." jbwashington/ebay-mcp, 17 stars, updated 2026-10-01: "eBay listing automation plugin for Claude Code with AI-powered image analysis, pricing research, and fraud detection". mrnajiboy/ebay-mcp-remote-edition, 5 stars, "325+ tools". CDataSoftware/ebay-mcp-server-by-cdata is read-only and upsells a paid platform.
- Etsy: administrativetrick/etsy-mcp-server, 20 stars, updated 2026-11-04, but the repo page shows "3 Commits" and only "Initial commit: Etsy MCP Server v1.0.0" (search-oriented, thin). georgejeffers/etsy-mcp-server, 13 stars, updated 2026-10-21, "Upload Listings, Edit Listings". aserper/etsy-mcp, 12 stars, pushed 2026-11-07, MIT, "21 Commits", "37 tools for listings, orders, shipping, reviews, inventory, payments", "OAuth 2.0 + PKCE", "10 req/sec limiter to respect Etsy's limits". Several one-star forks claim 50 to 104 tools; not inspected.
- All are hobby projects by single maintainers. Treat as starting code, read before running, and keep keys in `.env.local`.

### Dictation
- Windows voice typing (V): "Press Windows key+H"; "Voice typing uses online speech recognition, which is powered by Azure Speech services"; needs internet and a microphone; automatic punctuation setting available.
- iPhone Dictation (V): "Dictation is processed on your iPhone in many languages, and no internet connection is required." Settings > General > Keyboard > Enable Dictation. iOS 27 with Apple Intelligence improves spelling and punctuation on iPhone 15 Pro or later.
- Wispr Flow (V): Free includes "Speech-to-text in any app, 100+ languages", "Dictation on Mac, Windows, iOS, and Android", "Learns your names and jargon", with "Limited words per week". Pro "$12/user/mo" adds "Unlimited dictations". Growth "$18/user/mo" is admin and SSO. Annual toggle gives "20% discount".
- Superwhisper (V, partial): Free forever after a 3,000-word Pro trial; Pro "$8.49" per month on yearly billing; "Offline models only run really well on Apple Silicon macs"; "Use your own AI API Keys" on Pro.

## 3. Recommendation for Hollie

Top picks, free first:
1. Claude in Chrome, today. Ricky's paid Claude plan already includes it. Install the extension, keep "safety check on each action" on, and use it for: reading a finished Etsy draft back, pulling sold comps from open tabs into a note, drafting buyer replies in Etsy Messages for Ricky to send. Never leave it running unattended, and never use it on eBay or Facebook Marketplace.
2. Windows voice typing (Win+H) and iPhone Dictation. Free, nothing to install. Dictate the one-line item note that the planned Haiku flow turns into a listing.
3. Gemini Free ($0). Use as the second opinion when identifying a maker's mark or a glass pattern from a photo. Do not pay for Google AI Pro just for auto browse; it duplicates Claude in Chrome.
4. Shopify Sidekick, the day the store exists. Included with Basic ($29 a month yearly, $39 monthly). Product copy, phone-photo cleanup, order edits, Flow automations, all with review before apply.
5. Shopify connector in Claude plus the Shopify AI Toolkit plugin in Claude Code (free). The connector for day-to-day store questions, the plugin for the build sessions.
6. Wispr Flow Free. Try it on Windows and iPhone for a week; pay $12 a month only if the weekly word cap stops a listing session.
7. aserper/etsy-mcp (free, MIT) once Ricky creates the Etsy Seller App key (Step 0). It is the sanctioned API route to create and edit listings from Claude.
8. YosefHayim/ebay-mcp (free, MIT, 194 stars) once eBay developer keys exist. This, or Crosslist, is how eBay listings should be created; the User Agreement bans LLM bots in the browser.

What to pay for only once it earns it: Wispr Flow Pro ($12 a month) if dictation becomes the main input; Google AI Pro ($19.99 a month) only if Ricky moves off Claude.

What to skip and why: ChatGPT paid plans (agent mode and Atlas are retired, Plus and Go prices did not even render, cloud browser works unattended which marketplaces dislike, and Claude already covers the same jobs); Perplexity Comet (price and terms unverifiable today, Cloudflare wall); Opera Neon ($19.90 a month for an agent with no reseller-specific advantage); Microsoft Copilot paid tiers (the free Edge sidepane is enough for tab comparisons); any browser agent on eBay, Facebook Marketplace or Chairish (explicit terms quoted above).

Terms summary for the question asked:
- Etsy: API Seller App path is sanctioned; browser-agent stance unverified (legal pages walled). Keep a human in the loop.
- eBay: browser agents and "LLM-driven bots" banned without permission; use the API.
- Shopify: AI in the admin is a product feature; allowed.
- Facebook Marketplace: automated access banned without prior permission; manual only.
- Chairish: unattended processes and scraping banned; manual listing, AI drafting off-site is fine.
- 1stDibs: terms unreadable today.

## 4. Gaps and pages that would not load

- ChatGPT Plus and Go monthly prices: the pricing page renders amounts from a price token not present in the page text or HTML; help articles for Plus and Go returned empty pages. U.
- Perplexity Comet price and free tier: perplexity.ai/pricing 404; help center collections HTTP 403 Cloudflare; Comet FAQ answers did not render; second visit hit a bot wall. U.
- Etsy API Terms of Use and Terms of Use: HTTP 403 at etsy.com/legal/*. Etsy's stance on AI tools filling the seller UI: U.
- 1stDibs terms: JavaScript shell, no text via Chromium or curl. U.
- Facebook Marketplace "no API": not confirmed from a Meta page today. U.
- Microsoft Copilot Mode "Actions" (click and fill in Edge): not found on the pages read. U.
- Opera Neon OS list and Superwhisper monthly and lifetime prices: not in rendered text. U.
- OpenAI Operator help article returned empty; status inferred from the agent article. U.
- GitHub repo licence and commit counts came from public repo pages; star counts and update dates from the GitHub API search. The gh REST repo endpoint was blocked for repos not attached to the session, and add_repo was not used (rule 0).
- WebSearch budget was exhausted mid-task (shared across agents), so no "best agents for resellers 2026" roundup widening was done. The sweep is seed-driven.
- No Reddit, no crawl4ai, no subagents, per rules.

## 5. Sources (every URL fetched today, one per line)

https://claude.com/pricing
https://claude.com/chrome (redirects to https://claude.com/claude-in-chrome)
https://claude.com/claude-in-chrome
https://support.claude.com/en/articles/12012173-get-started-with-claude-in-chrome
https://support.claude.com/en/articles/8241126-what-kinds-of-documents-can-i-upload-to-claude-ai
https://claude.com/connectors
https://claude.com/product/claude-code
https://www.anthropic.com/legal/aup
https://openai.com/chatgpt/pricing/ (redirects to https://chatgpt.com/pricing/; dollar amounts not in text)
https://help.openai.com/en/articles/11752874-chatgpt-agent
https://help.openai.com/en/articles/9793128-what-is-chatgpt-pro (title: About ChatGPT Pro tiers)
https://help.openai.com/en/articles/6950777-what-is-chatgpt-plus (empty)
https://help.openai.com/en/articles/11989085-what-is-chatgpt-go (empty)
https://help.openai.com/en/articles/10421097-operator (empty)
https://help.openai.com/en/articles/8983711-image-inputs-for-chatgpt-faq (empty)
https://help.openai.com/en/collections/3742473-chatgpt
https://help.openai.com/en/articles/20001371-chatgpt-atlas-retirement
https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex
https://help.openai.com/en/articles/20001280-using-cloud-browser-in-chatgpt
https://openai.com/index/introducing-chatgpt-atlas/
https://openai.com/policies/usage-policies/
https://gemini.google/subscriptions/
https://gemini.google/overview/gemini-in-chrome/
https://www.perplexity.ai/comet (curl fallback first; Cloudflare wall on second visit)
https://www.perplexity.ai/pricing (404)
https://www.perplexity.ai/help-center/en/
https://www.perplexity.ai/help-center/en/collections/18799298-comet (403)
https://www.perplexity.ai/help-center/en/collections/18799292-subscription-plans-billing (403)
https://www.perplexity.ai/help-center/en/articles/10352901-what-is-perplexity-pro (no usable text)
https://www.perplexity.ai/hub/faq/comet (redirects to help center index)
https://www.microsoft.com/en-us/microsoft-copilot/pricing (navigation only)
https://www.microsoft.com/en-us/edge/copilot-mode (redirects to https://explore.microsoft.com/en-us/edge/copilot)
https://www.microsoft.com/en-us/microsoft-365/premium
https://www.microsoft.com/en-us/microsoft-copilot/for-individuals (redirects to https://www.microsoft.com/en-us/copilot/solutions/individuals)
https://support.microsoft.com/en-us/windows/use-voice-typing-to-talk-instead-of-type-on-your-pc-fec94565-c4bd-329d-e59a-af033fa5689f
https://support.apple.com/guide/iphone/dictate-text-iph2c0651d2/ios
https://www.operaneon.com/
https://wisprflow.ai/pricing
https://superwhisper.com/
https://www.etsy.com/legal/api (403)
https://www.etsy.com/legal/terms-of-use (empty, walled)
https://developers.etsy.com/documentation/
https://www.ebay.com/help/policies/member-behaviour-policies/user-agreement?id=4259
https://www.shopify.com/sidekick
https://www.shopify.com/magic (redirects to /sidekick)
https://www.shopify.com/pricing
https://help.shopify.com/en/manual/shopify-sidekick (no article; generic help home)
https://help.shopify.com/en/manual/shopify-admin/productivity-tools/sidekick (redirects to https://help.shopify.com/en/manual/ai-powered-tools/sidekick)
https://help.shopify.com/en/manual/ai-powered-tools/sidekick
https://shopify.dev/docs/apps/build/devmcp (redirects to https://shopify.dev/docs/apps/build/ai-toolkit)
https://shopify.dev/docs/apps/build/ai-toolkit
https://shopify.dev/docs/apps/build/storefront-mcp
https://www.facebook.com/terms.php
https://www.facebook.com/policies_center/commerce
https://www.facebook.com/apps/site_scraping_tos_terms.php
https://www.chairish.com/ (footer links only)
https://www.chairish.com/terms (404; also /terms-of-service, /legal/terms, /help/terms, /seller-terms, /terms-of-use all 404)
https://support.chairish.com/hc/en-us/articles/115007071507 (redirects to https://support.chairish.com/hc/en-us/articles/44208742405649-Terms-of-Service)
https://www.1stdibs.com/ (footer links only)
https://www.1stdibs.com/about/terms/ (JS shell, unreadable)
https://www.1stdibs.com/about/terms-of-use/ (JS shell, unreadable)
https://github.com/YosefHayim/ebay-mcp
https://github.com/administrativetrick/etsy-mcp-server
https://github.com/aserper/etsy-mcp
GitHub API via `gh search repos "etsy mcp"` and `gh search repos "ebay mcp"` (stars, updatedAt, descriptions, 2026-11-07)
