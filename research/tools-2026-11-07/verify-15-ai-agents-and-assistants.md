# Verification of lane 15: AI assistants and browser agents (adversarial price and claim check)

Date 2026-11-07. Author: research subagent (checker). Question: Do the prices, free tiers, platform claims and availability claims in `15-ai-agents-and-assistants.md` hold up against the vendors' own pages today? Legend: V = page read today; U = unverified (snippet, memory, or the page would not load).

Method. Every page was read today through the headless Chromium fetch script via the session proxy (curl fallback). WebFetch was not used. No subagents. GitHub's API (`gh`) refused both MCP repos (HTTP 403, repository not attached to this session), so the GitHub web pages and commit histories were read instead. Verdicts: confirmed = the exact figure or claim is on the page read; refuted = the page says something different (correction given); unreadable = the page did not load after one alternative.

Count: 26 checks across 16 tools (8 PICKS plus the highest-fit TOOLS). 31 URLs fetched, 2 failed (one bot wall, one 404).

## 1. Checks

| # | Tool | Claim checked | Verdict | Evidence quote | URL | Correction |
|---|------|---------------|---------|----------------|-----|------------|
| 1 | Claude in Chrome | Included on all paid Claude plans, $0 extra | confirmed (V) | "Available on all paid plans. Not on a paid plan? Upgrade now" | https://claude.com/claude-in-chrome | none |
| 2 | Claude in Chrome | Paid plans only (Pro, Max, Ultra, Team, Enterprise); Chrome extension; launchable from Cowork and Claude Code | confirmed (V) | "available on paid plans (Pro, Max, Ultra, Team, and Enterprise), in the Chrome side panel, Claude Cowork, and Claude Code" | https://support.claude.com/en/articles/12012173-get-started-with-claude-in-chrome | Pricing table also shows Claude in Chrome "No" on Free, "Yes" on Pro, Max, Ultra. Product page says "Claude Cowork is now just Claude", so the Cowork name is being retired. |
| 3 | Claude plans | Free $0; Pro $17/mo annual ($200 up front) or $20 monthly; Max $100/mo; Ultra $200/mo | confirmed (V) | "$17 Per month with annual subscription discount ($200 billed up front). $20 if billed monthly." Max "$100 Per month". Ultra "$200 Per month". | https://claude.com/pricing | none |
| 4 | Claude Free tier | Limited usage every 5 hours and weekly; Sonnet and Haiku; web search; connectors; up to 5 projects | confirmed (V) | "Limited usage every 5 hours and every week*"; Projects row "Up to 5"; Sonnet "Yes"; Haiku "Yes"; Web search "Yes"; Connectors "Yes" | https://claude.com/pricing | none. Fable on Free is "No" (usage credits only). |
| 5 | Claude Code | Included in all paid plans; not on Free | confirmed (V) | "Claude Code is included in all paid plans." Table: Claude Code "No" on Free. | https://claude.com/pricing | none |
| 6 | Claude connectors | Connectors "Yes" on Free through Ultra; Shopify, Canva, Notion, Gmail, Google Drive, Squarespace, Supabase listed | confirmed (V) | Shopify: "Build, manage, and analyze your Shopify store"; Squarespace: "run your Squarespace store's orders, products and customers, all from Claude" | https://claude.com/connectors (redirects to https://claude.com/marketplace/connectors-plugins) | URL redirects to the marketplace page. Connectors row on pricing page reads Yes for all four plans. |
| 7 | Windows voice typing (Win+H) | Free, nothing to install, Windows 10 and 11 | confirmed (V) | "Press Windows key+H on a hardware keyboard."; "you'll need to be connected to the internet, have a working microphone" | https://support.microsoft.com/en-us/windows/use-voice-typing-to-talk-instead-of-type-on-your-pc-fec94565-c4bd-329d-e59a-af033fa5689f (redirects to https://support.microsoft.com/en-us/accessibility/windows/use-voice-typing-to-talk-instead-of-type-on-your-pc) | First agent omitted that voice typing needs an internet connection. Page tabs: Windows 11 and Windows 10. |
| 8 | iPhone Dictation | Free, iOS, nothing to install | confirmed (V) | "Dictation is processed on your iPhone in many languages, and no internet connection is required." | https://support.apple.com/guide/iphone/dictate-text-iph2c0651d2/ios | none. Guide covers iOS 12 through iOS 27. |
| 9 | Gemini (Free) | $0/ month with a Google Account; limits refresh every 5 hours up to a weekly cap | confirmed (V) | "$0/ month with a Google Account"; "Your limit refreshes every 5 hours until you reach your weekly limit." | https://gemini.google/subscriptions/ | none |
| 10 | Gemini paid tiers | Plus $4.99/ month; Pro $19.99/ month; Ultra $99.99/ month (5x) or $199.99 / month (20x) | confirmed (V) | "$4.99/ month"; "$19.99/ month"; "$99.99/ month: 5x higher usage limits vs. AI Pro"; "$199.99 / month: 20x higher usage limits vs. AI Pro" | https://gemini.google/subscriptions/ | none |
| 11 | Gemini in Chrome (auto browse) | Bundled in Google AI Pro at $19.99; US preview for Pro and Ultra; summaries free | confirmed (V) | "Rolling out first in preview to Google AI Pro and Ultra subscribers in the U.S."; AI Pro card: "Access Chrome auto browse to help complete tasks for you" | https://gemini.google/overview/gemini-in-chrome/ and https://gemini.google/subscriptions/ | none. Still a US preview today. |
| 12 | Shopify Sidekick | Built into every store, no extra charge above the store plan | confirmed (V, via alternative page) | "BUILT INTO EVERY STORE"; pricing table row "Sidekick, AI assistant for commerce" on every plan | https://www.shopify.com/sidekick and https://www.shopify.com/pricing | The help page https://help.shopify.com/en/manual/ai-powered-tools/sidekick returned HTTP 403 today. The FAQ "Does using Sidekick cost money?" is on the product page but its answer did not render. |
| 13 | Shopify Basic plan | $29 USD/mo yearly or $39 USD/mo monthly; trial 3 days free then $1/month for 3 months | confirmed (V) | "Pay monthly $39 USD/mo"; "Pay yearly $29 USD/mo"; "Try 3 days free, then $1/month for 3 months." | https://www.shopify.com/pricing | none |
| 14 | Shopify Sidekick | Writes copy, cleans phone photos, edits orders, builds Flow automations, review before apply, voice mode | unreadable for voice mode, edits orders and Flow (help page 403); photos, copy, automation and review confirmed (V) | "Upgrade your phone photos to studio shots."; "Hook shoppers with irresistible product copy."; "Workflow Automation"; "show you the recommendation to review" | https://www.shopify.com/sidekick | The product page does not mention voice mode, order editing or Flow by name. Those three claims rest on the help page, which was walled today. |
| 15 | Shopify AI Toolkit (Claude Code plugin) | Free; Claude Code, Codex, Cursor, VS Code; authenticated store-management tasks | confirmed (V) for platforms and store tasks | "A supported AI tool: Claude Code, Codex, Antigravity CLI, Cursor, Hermes (plugin only), OpenClaw (plugin only), Pi (plugin only), or Visual Studio Code."; "Shopify CLI's authenticated store context, with you choosing when to execute them" | https://shopify.dev/docs/apps/build/ai-toolkit | The page states no price at all; "free" is inferred from the absence of any fee and the open install command `claude plugin install shopify-ai-toolkit@claude-plugins-official`. |
| 16 | Wispr Flow | Free $0/mo; Pro $12/user/mo; Growth $18/user/mo; limited words per week; Mac, Windows, iOS, Android | confirmed (V) | "Free on Mac, Windows, iPhone and Android."; "$0/mo"; "$12/user/mo"; "$18/user/mo"; "Limited words per week" | https://wisprflow.ai/pricing | The "annual 20% discount" the first agent recorded is not visible in today's page text (the Monthly/Annual toggle amounts did not render). Prices shown are the monthly toggle. |
| 17 | Superwhisper | Pro $8.49/month on the yearly toggle; free tier forever after 3,000-word Pro trial; Mac, Windows, iOS, Android | confirmed (V) | "you can try the Pro features for 3,000 words for free, after that the free tier features are available to you forever"; Pro "$ 8 49 /month"; "Available on Mac, Windows, iOS and Android" | https://superwhisper.com/ | Monthly and Lifetime amounts again did not render (toggle). |
| 18 | aserper/etsy-mcp | Free, MIT, 37 tools, OAuth PKCE, pushed 2026-11-07 | refuted (V) on the date; MIT, 37 tools and PKCE confirmed | "Commits on Apr 2, 2026" (the only date group, 21 commits); "37 tools"; "MIT license"; "On first use, call the authenticate tool. This opens your browser to Etsy's OAuth consent page using PKCE." | https://github.com/aserper/etsy-mcp and https://github.com/aserper/etsy-mcp/commits/main | Latest commit is Apr 2, 2026, not 2026-11-07. All 21 commits landed that day. 12 stars, 7 forks, 1 branch, 0 tags, single author (aserper). Seven months without a commit. |
| 19 | YosefHayim/ebay-mcp | 194 stars, 828 commits, MIT, updated 2026-11-06, sandbox and production | refuted (V) on the date; stars, commits, MIT, sandbox confirmed | "Star194"; "828 Commits"; "MIT license"; "Sandbox and production"; "switch environments with a single variable"; "Commits on Oct 29, 2026" | https://github.com/YosefHayim/ebay-mcp and https://github.com/YosefHayim/ebay-mcp/commits/main | Latest commit is Oct 29, 2026 (first agent's 2026-11-06 is probably GitHub's `updated_at`, which moves on stars and issues too). README now says "379 tools" and carries a disclaimer: "Unofficial, third-party project"; "You are responsible for complying with eBay's API License Agreement". |
| 20 | Etsy Open API v3 Seller App | Free; automated near-instant approval; your shop only; commercial use not permitted | confirmed (V) for the three table rows; price not stated | "Approval Automated, near-instant for eligible sellers"; "Shop access Your shop only"; "Commercial use Not permitted" | https://developers.etsy.com/documentation/ | No fee is stated anywhere on the page, so "free" is inferred, not quoted. New today: the page says "The OpenAPI Dev MCP server connects AI coding assistants directly to the Etsy Open API" (an official Etsy dev MCP exists). |
| 21 | eBay User Agreement | Bans LLM-driven bots and buy-for-me agents without eBay's express permission | confirmed (V) | "other automated means (including, without limitation buy-for-me agents, LLM-driven bots, or any end-to-end flow that attempts to place orders without human review)"; "except with the prior express permission of eBay" | https://www.ebay.com/help/policies/member-behaviour-policies/user-agreement?id=4259 | none |
| 22 | ChatGPT plans | Pro $100, $200 or $500 per month; Plus and Go unknown | refuted (V) on "Plus unknown": Plus is $20/month; Pro confirmed; Go still unknown | "Pro 500, a new $500/month plan"; tier cards "$100" "$200" "$500"; Plus: "Price: $20/month (billed monthly)."; Go: "Subscription prices can be found in the ChatGPT pricing page." | https://help.openai.com/en/articles/9793128-what-is-chatgpt-pro (redirects to .../9793128-about-chatgpt-pro-tiers); https://help.openai.com/en/articles/6950777-what-is-chatgpt-plus; https://help.openai.com/en/articles/11989085-what-is-chatgpt-go; https://openai.com/chatgpt/pricing/ (redirects to https://chatgpt.com/pricing/) | ChatGPT Plus is $20/month (billed monthly) per the help center. The pricing page still renders Go and Plus with "/ month" and no amount. Go stays U. |
| 23 | ChatGPT agent mode / Operator | Retired | confirmed (V) | "ChatGPT agent is no longer available. Use ChatGPT Work for longer, multi-step tasks and finished deliverables." | https://help.openai.com/en/articles/11752874-chatgpt-agent | none |
| 24 | ChatGPT Atlas | Retired; was macOS only | confirmed (V) | "ChatGPT Atlas has been retired and no longer receives updates." | https://help.openai.com/en/articles/20001371-chatgpt-atlas-retirement | "macOS only" is consistent (uninstall steps are for Mac only) but not stated in those words. Article updated 16 days ago. |
| 25 | ChatGPT Work cloud browser | Paid plans only, excluding Free and Go; web and mobile | confirmed (V) | "Cloud browser is available in ChatGPT Work on paid ChatGPT plans in supported regions, excluding Free and Go."; "start a task on web or mobile" | https://help.openai.com/en/articles/20001280-using-cloud-browser-in-chatgpt | none |
| 26 | Perplexity Comet | Price unknown; Mac, Windows, iOS, Android | platforms confirmed (V); price unreadable (U) | "Available for Mac, Windows, iOS, and Android"; FAQ heading "Is Comet free?" with no rendered answer | https://www.perplexity.ai/comet; https://www.perplexity.ai/help-center/en/articles/11172798-getting-started-with-comet | Two help-center articles read today say nothing about price. The guessed article 11480364 was a 404. Price stays U. |

## 2. What the first agent got wrong or left out

1. aserper/etsy-mcp "pushed 2026-11-07" is wrong. The commit history shows one date group, "Commits on Apr 2, 2026", for all 21 commits. The project is young and dormant: 12 stars, 7 forks, one author, no commits in seven months. Read it before running it, and expect to patch it yourself.
2. YosefHayim/ebay-mcp "updated 2026-11-06" is not supported by the commit history. The latest commit group is Oct 29, 2026. Stars (194), commits (828), MIT and sandbox-plus-production all hold. The README now advertises 379 tools and carries an "Unofficial, third-party project" disclaimer that puts eBay API License Agreement compliance on the user.
3. ChatGPT Plus was recorded as unknown. The help center states "$20/month (billed monthly)". Go is still not priced on any page that loaded.
4. Windows voice typing was called "nothing to install", which holds, but the page also says "you'll need to be connected to the internet". iPhone Dictation, by contrast, "no internet connection is required". That matters for dictating notes in a thrift store with poor signal.
5. Shopify Sidekick's "voice mode", "edits orders" and "builds Flow automations" came from the help page, which was bot-walled (HTTP 403) today. The product page confirms photo cleanup, product copy, "Workflow Automation" and review-before-apply, but does not name voice mode, order editing or Flow. Treat those three as U until the help page loads.
6. Wispr Flow's "annual 20% discount" is not in today's page text. The monthly figures ($0, $12, $18) are confirmed.
7. Two source URLs redirect: claude.com/connectors goes to claude.com/marketplace/connectors-plugins, and the Microsoft voice typing page moved under /accessibility/windows/. Both still load.
8. "Free" for the Etsy Seller App and the Shopify AI Toolkit is inferred from the absence of any fee, not quoted. No page states a price either way.
9. Perplexity Comet's price remains unreadable after two help-center alternatives. Platforms (Mac, Windows, iOS, Android) are confirmed.
10. New fact the first agent missed: Etsy's developer docs now mention an official "OpenAPI Dev MCP server" for AI coding assistants. It is a docs and schema helper, not a listing tool, but it is Etsy's own.

Everything else in PICKS held: Claude in Chrome on all paid plans, the four Claude plan prices, Gemini Free at $0 and auto browse as a US preview on AI Pro ($19.99/ month) and Ultra, Shopify Basic at $39 USD/mo monthly or $29 USD/mo yearly, Wispr Flow Free at $0/mo, and the eBay User Agreement's "LLM-driven bots" ban.

## 3. Pages that would not load

- https://help.shopify.com/en/manual/ai-powered-tools/sidekick : HTTP 403 (bot wall). Alternative https://www.shopify.com/sidekick loaded.
- https://www.perplexity.ai/help-center/en/articles/11480364-what-is-comet : 404 (guessed URL). Alternatives 11172798 and 11734754 loaded but carry no price.
- GitHub API via `gh api repos/...` for both MCP repos: HTTP 403, "GitHub access to this repository is not enabled for this session". Not pursued further (no add_repo). Web pages used instead.
- https://github.com/aserper/etsy-mcp/commits/main.atom via curl: empty response. Not needed; the HTML commits page carried the date.

## 4. Sources (every URL fetched today)

https://claude.com/claude-in-chrome
https://support.claude.com/en/articles/12012173-get-started-with-claude-in-chrome
https://claude.com/pricing
https://claude.com/connectors (final URL https://claude.com/marketplace/connectors-plugins)
https://support.microsoft.com/en-us/windows/use-voice-typing-to-talk-instead-of-type-on-your-pc-fec94565-c4bd-329d-e59a-af033fa5689f (final URL https://support.microsoft.com/en-us/accessibility/windows/use-voice-typing-to-talk-instead-of-type-on-your-pc)
https://support.apple.com/guide/iphone/dictate-text-iph2c0651d2/ios
https://gemini.google/subscriptions/
https://gemini.google/overview/gemini-in-chrome/
https://help.shopify.com/en/manual/ai-powered-tools/sidekick (HTTP 403)
https://www.shopify.com/pricing
https://www.shopify.com/sidekick
https://shopify.dev/docs/apps/build/ai-toolkit
https://wisprflow.ai/pricing
https://superwhisper.com/
https://github.com/aserper/etsy-mcp
https://github.com/aserper/etsy-mcp/commits/main
https://github.com/YosefHayim/ebay-mcp
https://github.com/YosefHayim/ebay-mcp/commits/main
https://developers.etsy.com/documentation/
https://www.ebay.com/help/policies/member-behaviour-policies/user-agreement?id=4259
https://openai.com/chatgpt/pricing/ (final URL https://chatgpt.com/pricing/)
https://help.openai.com/en/articles/9793128-what-is-chatgpt-pro (final URL https://help.openai.com/en/articles/9793128-about-chatgpt-pro-tiers)
https://help.openai.com/en/articles/6950777-what-is-chatgpt-plus
https://help.openai.com/en/articles/11989085-what-is-chatgpt-go
https://help.openai.com/en/articles/11752874-chatgpt-agent
https://help.openai.com/en/articles/20001371-chatgpt-atlas-retirement
https://help.openai.com/en/articles/20001280-using-cloud-browser-in-chatgpt
https://www.perplexity.ai/comet
https://www.perplexity.ai/help-center/en/articles/11480364-what-is-comet (404)
https://www.perplexity.ai/help-center/en/articles/11172798-getting-started-with-comet
https://www.perplexity.ai/help-center/comet/en/articles/11734754-why-can-t-i-access-сomet
