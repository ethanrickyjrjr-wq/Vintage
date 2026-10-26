[Skip to content](https://vorplabs.com/agent-tools/ebay-buy-api#main-content)
[Vorp Labs](https://vorplabs.com/)
[How it works](https://vorplabs.com/#how-it-works)[Research](https://vorplabs.com/research)[About](https://vorplabs.com/about)[Start a project](https://vorplabs.com/contact)
Agent tool field guide
# eBay agent access: the sandbox-to-production gap, the partner requirement, and the Application Growth Check
As of October 7, 2026, eBay offers Buy APIs that are publicly documented and accessible in sandbox to anyone with an eBay developer account, with the exception of checkout methods (guest checkout and member checkout) which require separate approval even for sandbox use. Production access is a different matter: many of the Buy APIs are limited-release, and production use is intended for eBay partners only. Developers must apply through the eBay Partner Network, and acceptance is based on the proposed business model and a formal agreement to abide by eBay's policies and requirements. There is no guarantee that an application will be approved for production use. Production access requires multiple contracts (eBay User Agreement, API License Agreement, eBay Partner Network Agreement, and possibly business-model-specific contracts and mutual non-disclosure agreements), technical review, and compliance with the Application Growth Check. The API License Agreement grants a non-exclusive, non-transferable, non-sublicensable license to use eBay's developer tools solely for facilitating use of eBay Services. eBay may suspend access, reduce API calls, or terminate the agreement at its sole discretion if it believes the tools are being used in any way that undermines eBay's business interests. Restricted APIs, defined as those providing market trends, pricing strategies, sales volumes, user behavior, or AI-generated content, require special access granted to select developers. Separately, the eBay User Agreement prohibits using automated means, including buy-for-me agents, LLM-driven bots, or any end-to-end flow that attempts to place orders without human review, to access eBay's services without eBay's prior express permission. eBay's open-source GitHub organization publishes a local MCP server that is limited to read (GET) requests in production; it is not listed on developer.ebay.com, it runs on the developer's own application keys, and eBay's Buy API call-limits page states that Buy APIs require an additional license.
Current recommendation
Do not invest heavily in application development before obtaining production approval. eBay's own documentation advises completing the production application process and obtaining approval before investing significantly in development and testing. Apply through the eBay Partner Network, understand the contractual requirements (which may include mutual non-disclosure agreements), and plan for the Application Growth Check. Do not treat sandbox success as evidence that production access will be granted. If your use case involves checkout, request that approval separately as it requires a distinct review. Be aware that Restricted APIs (market trends, pricing, sales volumes, AI-generated content) require special access beyond standard production approval.
VendoreBayTypeAPIAvailabilityGenerally availableReviewed2026-10-07
Quick facts
Sandbox access
Open to anyone with an eBay developer account, except checkout methods which require separate approval.
Production access
Limited-release, restricted to eBay partners. Must apply through the eBay Partner Network. Approval is not guaranteed.
Application Growth Check
Every application that interacts with an eBay API must comply with eBay's Compatible Application Growth Check requirements, which may be updated. A Growth Check request is required to raise API call limits or to use restricted APIs in production.
Checkout approval
Guest checkout (Checkout with eBay widget) and eBay member checkout (Order API) each require separate approval for both sandbox and production use.
Official MCP
eBay's open-source GitHub organization publishes a local MCP server (npm package @ebay/npm-public-api-mcp, version 1.1.0 released 2026-08-14). Its README says it supports only read (GET) requests in production and does not support sandbox. It is not listed on developer.ebay.com and runs on your own eBay application keys; eBay states separately that Buy APIs require an additional license.
Buy-for-me agents
Prohibited by the eBay User Agreement without eBay's prior express permission, along with LLM-driven bots and order flows that skip human review.
Restricted APIs
APIs providing market trends, pricing strategies, sales volumes, user behavior, or AI-generated content require special access granted to select developers.
Evidence level: eBay's Buy APIs Requirements page and API License Agreement were read directly in a browser on July 27, 2026 and re-read on October 7, 2026. The Requirements page confirms limited-release status, partner-only production access, and the separate checkout approval. The License Agreement confirms the Application Growth Check requirement, the Restricted APIs definition, and eBay's discretionary suspension rights. The eBay User Agreement, the Application Growth Check page, and the README of eBay's open-source MCP server were read on October 7, 2026. Last reviewed 2026-10-07.
Review record Status
    Generally available Access
    eBay's Buy APIs are publicly documented and anyone with a developer account can use them in sandbox, except for checkout methods which require separate approval. However, production use is limited-release and restricted to eBay partners: developers must apply through the eBay Partner Network, sign additional contracts, and pass the Application Growth Check. Approval is not guaranteed. The API License Agreement grants a non-exclusive, non-transferable license solely for facilitating use of eBay Services, and eBay may suspend access at its sole discretion if it believes the developer tools are being used in any way that undermines eBay's business interests. Platforms
    Web Regions
    Global Review cadence
    Review when eBay changes the Buy API production access requirements, opens self-service production access, changes the Application Growth Check, updates the API License Agreement, or publishes any MCP server or CLI.
Evidence record Limited-release production access
    The Buy APIs Requirements page states: Many of the Buy APIs are a (Limited Release). The use of eBay's Buy APIs in production is intended for eBay partners only. You must apply for production access through the eBay Partner Network.     Hands-on verification · checked 2026-10-07 · [eBay Buy APIs Requirements](https://developer.ebay.com/api-docs/buy/buy-requirements.html) No guarantee of approval
    eBay states: There is no guarantee that your application for production use of the APIs will be approved. Acceptance is based on the proposed business model and a formal agreement to abide by policies and requirements.     Hands-on verification · checked 2026-10-07 · [eBay Buy APIs Requirements](https://developer.ebay.com/api-docs/buy/buy-requirements.html) Sandbox open except checkout
    Anyone with an eBay developer account can use the Buy APIs in sandbox, with the exception of methods in the guest_checkout_session and checkout_session resources. Developers requiring checkout access must contact Developer Technical Support or their Business Unit contact.     Hands-on verification · checked 2026-10-07 · [eBay Buy APIs Requirements](https://developer.ebay.com/api-docs/buy/buy-requirements.html) Contractual requirements
    Production access requires an eBay member account, eBay Developers Program account, and additional contracts specific to the Buy APIs and business model. These include the eBay User Agreement, API License Agreement, eBay Partner Network Agreement, and possibly mutual non-disclosure agreements.     Hands-on verification · checked 2026-10-07 · [eBay Buy APIs Requirements](https://developer.ebay.com/api-docs/buy/buy-requirements.html) Application Growth Check
    The API License Agreement states that applications that interact with an eBay API must comply with eBay's Compatible Application Growth Check requirements, which are incorporated by reference and may be updated.     Hands-on verification · checked 2026-10-07 · [eBay API License Agreement](https://developer.ebay.com/join/api-license-agreement) When a Growth Check is required
    eBay's Application Growth Check page states that requesting a Growth Check is required to increase an application's API call limits or to use restricted APIs in production.     Hands-on verification · checked 2026-10-07 · [eBay Application Growth Check](https://developer.ebay.com/grow/application-growth-check) Buy API license
    eBay's Buy API call-limits page lists default call limits and states that Buy APIs require an additional license.     Hands-on verification · checked 2026-10-07 · [eBay Buy API call limits](https://developer.ebay.com/develop/api/buy/api_call_limits) Authorized use boundary
    The API License Agreement grants a non-exclusive, non-transferable, non-sublicensable license solely for facilitating use of eBay Services. eBay may suspend access, reduce API calls, or terminate the agreement if it believes the tools are used in any way that undermines eBay's business interests.     Hands-on verification · checked 2026-10-07 · [eBay API License Agreement](https://developer.ebay.com/join/api-license-agreement) Restricted APIs definition
    The API License Agreement defines Restricted APIs as any eBay APIs that provide information about market trends, pricing strategies, sales volumes, user behavior, or provide generated content including content using artificial intelligence. Access is specially granted to select developers.     Hands-on verification · checked 2026-10-07 · [eBay API License Agreement](https://developer.ebay.com/join/api-license-agreement) Partner Network response time
    The Buy APIs Requirements page states that the eBay Partner Network responds to a production application, approving or declining it, within 10 business days; the following compliance review and contract signing have no stated timeline.     Hands-on verification · checked 2026-10-07 · [eBay Buy APIs Requirements](https://developer.ebay.com/api-docs/buy/buy-requirements.html) Invest-after-approval advice
    eBay advises developers to complete the production application process and obtain approval before investing significantly in application development and testing.     Hands-on verification · checked 2026-10-07 · [eBay Buy APIs Requirements](https://developer.ebay.com/api-docs/buy/buy-requirements.html) User Agreement automated-access ban
    The eBay User Agreement, effective June 28, 2026 for existing users, prohibits using any robot, scraper, or other automated means, including buy-for-me agents, LLM-driven bots, or any end-to-end flow that attempts to place orders without human review, to access eBay's services for any purpose, except with eBay's prior express permission.     Hands-on verification · checked 2026-10-07 · [eBay User Agreement](https://www.ebay.com/help/policies/member-behaviour-policies/user-agreement?id=4259) Open-source MCP server
    eBay's GitHub organization publishes @ebay/npm-public-api-mcp, first released on npm on 2026-02-18, with version 1.1.0 released 2026-08-14. The README describes it as designed for safe, read-only access to production eBay data, supports only GET requests, and says the release does not officially support the eBay sandbox. The server is not listed on developer.ebay.com.     Hands-on verification · checked 2026-10-07 · [eBay API MCP Server (GitHub)](https://github.com/eBay/npm-public-api-mcp) Adoption evidence needed
    The end-to-end time from application to production access, the proportion of applications that receive approval, and whether any self-service production path exists for lower-risk use cases.     Evaluation question · reviewed 2026-10-07 · [AI workflow release-readiness review](https://vorplabs.com/workflows/ai-governance/ai-workflow-release-readiness)
Confirmed by eBay
## What the official sources establish.
  * Many Buy APIs are limited-release and production use is intended for eBay partners only.
  * There is no guarantee that a production application will be approved; acceptance is based on the proposed business model.
  * Sandbox access is open to all developers except for checkout methods, which require separate approval.
  * Production access requires multiple contracts, including business-model-specific agreements and possibly mutual non-disclosure agreements.
  * eBay advises completing the production application process before investing significantly in development.
  * The Application Growth Check applies to every application that interacts with an eBay API and may be updated.
  * The eBay User Agreement prohibits buy-for-me agents, LLM-driven bots, and order flows without human review unless eBay gives prior express permission.


Not publicly documented
## Operational details not covered by public sources.
  * The end-to-end time from application to production access and the proportion of applications approved. eBay states only that the eBay Partner Network responds to the business-model application within 10 business days.
  * Whether any self-service production path exists for lower-risk use cases that do not involve checkout.
  * Whether eBay supports its open-source MCP server as a product: the server is published on eBay's GitHub organization but is not listed on developer.ebay.com, and no official CLI is documented.
  * Whether eBay plans to open broader self-service production access or whether the partner-only model is permanent.
  * Specific criteria that distinguish approved from rejected production applications beyond the stated business-model review.


Permission questions
## Questions to answer before building an agent that searches, bids, or buys on eBay.
  * Have you applied through the eBay Partner Network and received production approval, or are you building on sandbox access alone?
  * Does your use case involve checkout (guest or member), and have you obtained the separate approval required for those methods?
  * Does your application touch any Restricted APIs (market trends, pricing, sales volumes, user behavior, AI-generated content), and have you received the special access required?
  * Have you reviewed the Application Growth Check requirements and confirmed your application complies with the current version?
  * If eBay denies production access, what is your fallback, and does it comply with the eBay User Agreement's restrictions on automated access, which name buy-for-me agents and LLM-driven bots?


Evaluation plan
## Test the action boundary, not only the happy path.
eBay's developer documentation is extensive and the sandbox is genuinely open, which creates a misleading impression of production readiness. The critical distinction is that sandbox experimentation is not production authority to transact. Production access requires eBay Partner Network membership, additional contracts, technical review, and in some cases mutual non-disclosure agreements. An agent that works in sandbox may never receive production approval.
Test 1
Apply through the eBay Partner Network before investing in development; eBay's own documentation advises this sequence.
Test 2
Test the full Buy API surface in sandbox, but do not treat sandbox success as evidence of production readiness.
Test 3
Request checkout approval separately if your use case involves guest checkout or member checkout, as these have distinct review processes.
Test 4
Review the Application Growth Check requirements and the API License Agreement's Restricted APIs definition before scoping your integration.
Test 5
Map your use case against the authorized-use boundary in the API License Agreement: the license is solely for facilitating use of eBay Services, not for competitive analysis, market intelligence, or AI training on eBay content.
Test 6
Plan for the contractual requirements: eBay Partner Network Agreement, API License Agreement, and potentially business-model-specific contracts and mutual non-disclosure agreements.
Do not assume
## Keep the demo narrower than the product claim.
  * Sandbox access is not production access; checkout methods are restricted even in sandbox, and production requires partner approval.
  * Publicly documented APIs do not mean self-service production access; eBay states production is for partners only.
  * The Application Growth Check is not a one-time gate; requirements may be updated and compliance is ongoing.
  * Restricted APIs (market trends, pricing, AI-generated content) require special access beyond standard production approval.
  * eBay's discretionary suspension rights mean that even approved production access can be revoked if eBay believes the tools undermine its business interests.
  * Community eBay API wrappers and MCP packages do not carry eBay's production authorization, and eBay's own open-source MCP server runs on your application keys and is limited to read requests.


Re-review when
## New documentation or hands-on evidence changes the answer.
  * eBay opens self-service production access for Buy APIs without requiring eBay Partner Network membership.
  * The Application Growth Check requirements change.
  * eBay lists its MCP server on developer.ebay.com, adds sandbox, write, or checkout support to it, or publishes a CLI or agent-specific developer surface.
  * eBay changes the User Agreement's automated-access or buy-for-me agent terms.
  * The API License Agreement's Restricted APIs definition or authorized-use boundary changes.
  * eBay changes the checkout approval process or opens checkout to sandbox without separate review.


Stay current
## Get the weekly Vorp Change Brief.
A concise weekly briefing on the material changes in AI policy, models, tools, security, and operations, published on Substack.
[Subscribe on Substack](https://vorplabs.substack.com/subscribe)
Subscription happens on Substack. Vorp Labs does not collect your newsletter address on this site.
Update history
2026-10-07
Re-verified the Buy APIs Requirements page and API License Agreement; the partner-only production model, checkout approval, and License terms are unchanged. Corrected the MCP entry: eBay's open-source GitHub organization publishes a read-only local MCP server (version 1.1.0 released 2026-08-14). Added the User Agreement's prohibition on buy-for-me agents without eBay's permission.
2026-07-27
Initial field guide published. Buy APIs Requirements page and API License Agreement both read directly via browser session July 27, 2026. Confirmed limited-release production access, partner-only requirement, Application Growth Check, and eBay's discretionary suspension rights.
Related reviews
[Compare agent access models](https://vorplabs.com/agent-tools/access-models)[Credential and safety boundaries](https://vorplabs.com/agent-tools/agent-credential-security)[AI workflow release-readiness review](https://vorplabs.com/workflows/ai-governance/ai-workflow-release-readiness)[MCP server intake checklist](https://vorplabs.com/blog/mcp-server-intake-checklist)[Walmart Marketplace API field guide](https://vorplabs.com/agent-tools/walmart-marketplace-api)
Primary sources
[eBay Buy APIs Requirements](https://developer.ebay.com/api-docs/buy/buy-requirements.html)
eBay · Hands-on verification
Read directly via browser session July 27, 2026, and re-read October 7, 2026. Confirmed many Buy APIs are limited-release, production is for eBay partners only via the eBay Partner Network, sandbox is open except for checkout methods, and approval is not guaranteed. eBay advises obtaining production approval before investing in development.
[eBay API License Agreement](https://developer.ebay.com/join/api-license-agreement)
eBay · Hands-on verification
Read directly via browser session July 27, 2026, and re-read October 7, 2026. Confirmed the non-exclusive, non-transferable license, Application Growth Check requirement, Restricted APIs definition (market trends, pricing, sales volumes, user behavior, AI-generated content), and eBay's right to suspend access at its sole discretion.
[eBay User Agreement](https://www.ebay.com/help/policies/member-behaviour-policies/user-agreement?id=4259)
eBay · Hands-on verification
Read directly via browser session October 7, 2026. Effective June 28, 2026 for existing users. Prohibits buy-for-me agents, LLM-driven bots, and end-to-end order flows without human review unless eBay gives prior express permission.
[eBay Application Growth Check](https://developer.ebay.com/grow/application-growth-check)
eBay · Hands-on verification
Read directly via browser session October 7, 2026. States that requesting a Growth Check is required to raise API call limits or to use restricted APIs in production.
[eBay Buy API call limits](https://developer.ebay.com/develop/api/buy/api_call_limits)
eBay · Hands-on verification
Read directly via browser session October 7, 2026. Lists default Buy API call limits and states that Buy APIs require an additional license.
[eBay API MCP Server (GitHub)](https://github.com/eBay/npm-public-api-mcp)
eBay · Hands-on verification
README and npm metadata read October 7, 2026. Published by eBay's open-source GitHub organization; version 1.1.0 released 2026-08-14; read-only (GET) in production; sandbox not supported; not listed on developer.ebay.com.
## Site footer
Vorp Labs
We take on operations, data, and software work, and you only pay if it works.
© 2026 Vorp Labs.
### Company
  * [About](https://vorplabs.com/about)
  * [Programs](https://vorplabs.com/programs)
  * [Start a project](https://vorplabs.com/contact)
  * [GitHub (research data)](https://github.com/vorplabs)


### Research
  * [Research library](https://vorplabs.com/research)
  * [Coding agents](https://vorplabs.com/coding-agents)
  * [Agent tools](https://vorplabs.com/agent-tools)
  * [Models](https://vorplabs.com/models)
  * [Regulatory updates](https://vorplabs.com/ai-regulatory-updates)


### Recall
  * [About Recall](https://vorplabs.com/recall)
  * [Where transcripts go](https://vorplabs.com/recall#data-path)
  * [Sign in](https://app.vorplabs.com)
  * [Request beta access](https://vorplabs.com/contact?program=recall-design-partner)


### Legal
  * [Privacy](https://vorplabs.com/privacy)
  * [Terms](https://vorplabs.com/terms)
  * [Editorial standards](https://vorplabs.com/editorial-standards)


Site directory+
### Product and services
  * [Captured Recall search](https://vorplabs.com/recall#proof)
  * [Programs](https://vorplabs.com/programs)
  * [AI Coding Cost Audit](https://vorplabs.com/ai-coding-cost-audit)
  * [Agent workbench setup](https://vorplabs.com/agent-memory-systems)
  * [Workflow review](https://vorplabs.com/workflows/review)
  * [Workflow playbooks](https://vorplabs.com/workflows)
  * [Compliance](https://vorplabs.com/workflows/compliance)
  * [AI governance](https://vorplabs.com/workflows/ai-governance)
  * [Knowledge](https://vorplabs.com/workflows/knowledge)
  * [Accounting](https://vorplabs.com/workflows/accounting)
  * [Founding partners](https://vorplabs.com/partners)


### Regulation
  * [AI regulatory updates](https://vorplabs.com/ai-regulatory-updates)
  * [United States AI regulation](https://vorplabs.com/ai-regulatory-updates/united-states)
  * [California AI regulation](https://vorplabs.com/ai-regulatory-updates/united-states/california)
  * [Deepfake laws](https://vorplabs.com/ai-regulatory-updates/deepfake-laws)
  * [August 2026 US policy delta](https://vorplabs.com/ai-regulatory-updates/reports/2026-08-us-ai-policy-delta)


Regulatory pages are reference, not legal advice.
### Models and agents
  * [Model field guides](https://vorplabs.com/models)
  * [Model retirement calendar](https://vorplabs.com/models/model-retirement-calendar)
  * [OpenRouter routing policy](https://vorplabs.com/models/openrouter-routing-policy)
  * [Amazon Bedrock retirements](https://vorplabs.com/models/amazon-bedrock-model-retirements)
  * [Coding-agent field guides](https://vorplabs.com/coding-agents)
  * [Agent tool field guides](https://vorplabs.com/agent-tools)
  * [AI incident tracking](https://vorplabs.com/ai-incident-tracking)


### Datasets and methods
  * [Token-efficiency benchmarks](https://vorplabs.com/benchmarks/coding-agent-token-efficiency)
  * [E-invoicing mandates](https://vorplabs.com/e-invoicing-mandates)
  * [Security framework changes](https://vorplabs.com/security-framework-changes)
  * [Research library and data catalog](https://vorplabs.com/research)
  * [Research methods](https://vorplabs.com/methods)


### More research
  * [Compare](https://vorplabs.com/compare)
  * [Benchmarks](https://vorplabs.com/benchmarks)
  * [Application vendors](https://vorplabs.com/applications)
  * [Model release reviews](https://vorplabs.com/models/releases)
  * [Field notes](https://vorplabs.com/blog)
  * [AI threat monitoring](https://vorplabs.com/ai-threat-monitoring)


### Datasets and feeds
  * [Facts](https://vorplabs.com/facts)
  * [llms.txt](https://vorplabs.com/llms.txt)
  * [llms-full.txt](https://vorplabs.com/llms-full.txt)
  * [Sitemap](https://vorplabs.com/sitemap.xml)
  * [RSS feed](https://vorplabs.com/feed.xml)
  * [Regulatory RSS](https://vorplabs.com/ai-regulatory-updates/feed.xml)


### Elsewhere
  * [Hugging Face](https://huggingface.co/vorplabs)



