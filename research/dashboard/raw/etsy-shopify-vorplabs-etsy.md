[Skip to content](https://vorplabs.com/agent-tools/etsy-api#main-content)
[Vorp Labs](https://vorplabs.com/)
[How it works](https://vorplabs.com/#how-it-works)[Research](https://vorplabs.com/research)[About](https://vorplabs.com/about)[Start a project](https://vorplabs.com/contact)
Agent tool field guide
# Etsy agent access: the documentation MCP, the three access tiers, and the commercial-use gate
As of October 7, 2026, Etsy offers a REST API (Open API v3) with three access tiers serving different audiences. A Seller App gives individual sellers automated, near-instant access to manage their own shop only. A Personal App, requiring deeper review, allows developers to build tools beyond their own shop at limited scale. Commercial Access, which requires an approved Personal App first and a separate manual commercial review, permits serving multiple sellers via OAuth consent. Etsy also offers an OpenAPI Dev MCP server that connects AI coding assistants to endpoint details, request and response schemas, authentication requirements, and OAuth scopes, with no API key required. This MCP is a documentation and schema server, not a data-access interface. Actual API calls still require proper authentication through OAuth 2.0 with PKCE. Screen-scraping is prohibited, and Commercial Access apps that use the transactions_r scope must request access to the buyer_email field separately. Etsy's API Terms of Use, last updated August 18, 2026, also prohibit automated systems that access or scrape Etsy data and using the API for AI model training unless Etsy authorizes it in writing.
Current recommendation
Start by identifying which access tier your use case requires. If you are building for your own Etsy shop only, a Seller App gives near-instant automated access. If you need to serve other sellers, plan for the two-step path: first an approved Personal App, then a separate Commercial Access application. Do not treat the documentation MCP server as data access; it exposes schemas and endpoint reference, not shop, listing, or buyer data. Plan for OAuth 2.0 with PKCE for any data-accessing integration, and note that access tokens expire in one hour with refresh tokens valid for 90 days. If a Commercial Access workflow needs buyer email, request access to the buyer_email field separately.
VendorEtsyTypeAPIAvailabilityGenerally availableReviewed2026-10-07
Quick facts
API
Etsy Open API v3, a REST API for inventory management, sales orders, and shop management.
Seller App
Own-shop only. Automated, near-instant approval for active sellers in good standing who do not already have an active app. Commercial use not permitted.
Personal App
Beyond own shop at limited scale. Deeper review process. Commercial use limited to approved use case.
Commercial Access
Multi-seller via OAuth consent. Requires an approved Personal App first, then a separate manual commercial review.
MCP server
An OpenAPI Dev MCP server for documentation and schema exploration, announced April 15, 2026. No API key required. Does not provide data access.
Rate limits
Per-API-key queries-per-second and queries-per-day limits on a rolling 24-hour window; each app's current limits appear in the Developer Portal, and exceeding them returns HTTP 429 with a retry-after header.
Authentication
OAuth 2.0 Authorization Code Grant with PKCE mandatory on every flow. Access tokens expire in 1 hour; refresh tokens valid for 90 days.
Evidence level: Official Etsy developer documentation for the access tiers, the documentation MCP server, authentication, and rate limits, plus Etsy's API Terms of Use and Etsy's Open API announcements; first verified July 27, 2026 and re-verified October 7, 2026. The MCP server's tool list was also checked directly against the live server. Last reviewed 2026-10-07.
Review record Status
    Generally available Access
    Etsy offers a REST API (Open API v3) with three access tiers: Seller App (own-shop only, automated approval), Personal App (broader scope, deeper review), and Commercial Access (multi-seller, manual review requiring an approved Personal App first). Etsy also offers an OpenAPI Dev MCP server for documentation and schema exploration that needs no API key, but this MCP does not provide data access. Platforms
    Web Regions
    Global Review cadence
    Review when Etsy publishes an MCP server for data access (not just documentation), changes the Seller App, Personal App, or Commercial Access tier requirements, or updates API Terms of Use.
Evidence record Three access tiers
    Etsy documents three tiers: Seller App (own-shop, automated approval, no commercial use), Personal App (broader scope, deeper review, limited commercial use), and Commercial Access (multi-seller via OAuth, requires approved Personal App first, manual review).     Official announcement · checked 2026-10-07 · [Etsy Open API v3 developer documentation](https://developers.etsy.com/documentation/) Documentation MCP server
    Etsy offers an OpenAPI Dev MCP server that connects AI coding assistants to Etsy Open API documentation, providing endpoint details, request and response schemas, authentication requirements, and OAuth scopes. No API key is required. It works with Claude, Cursor, VS Code, and other MCP-compatible tools.     Official announcement · checked 2026-10-07 · [Etsy Open API v3 developer documentation](https://developers.etsy.com/documentation/) MCP is documentation-only
    The MCP server exposes API documentation and schemas, not live shop or listing data. Actual API calls still require proper authentication through OAuth 2.0.     Official announcement · checked 2026-10-07 · [Etsy Open API v3 developer documentation](https://developers.etsy.com/documentation/) Authentication requirements
    Every request requires an x-api-key header containing the app's keystring and shared secret separated by a colon. OAuth-authenticated endpoints additionally require OAuth 2.0 Authorization Code Grant with PKCE mandatory. Access tokens expire in 1 hour, refresh tokens in 90 days. Scope changes require re-authorization.     Official announcement · checked 2026-10-07 · [Etsy API authentication documentation](https://developers.etsy.com/documentation/essentials/authentication/) Screen-scraping prohibition
    The commercial access review criteria state that apps must not sidestep the API to retrieve or post Etsy data. A required trademark disclaimer must appear prominently on commercial applications.     Official announcement · checked 2026-10-07 · [Etsy Open API v3 developer documentation](https://developers.etsy.com/documentation/) Buyer email access gate
    Commercial Access apps that use the transactions_r permission scope (written as transaction_r in Etsy's review criteria) must request access to the buyer_email field separately. This is a distinct approval beyond the scope grant itself.     Official announcement · checked 2026-10-07 · [Etsy Open API v3 developer documentation](https://developers.etsy.com/documentation/) MCP launch date
    Etsy announced the OpenAPI Dev MCP Server on April 15, 2026, in the announcements channel of its Open API developer discussions forum.     Official announcement · checked 2026-10-07 · [Etsy Open API announcement: Dev MCP Server release](https://github.com/etsy/open-api/discussions/1582) Seller API Access launch
    Etsy announced Seller API Access, the automated own-shop tier, on July 13, 2026, and stated that a Personal Key remains the prerequisite for Commercial Access.     Official announcement · checked 2026-10-07 · [Etsy Open API announcement: Seller API Access](https://github.com/etsy/open-api/discussions/1647) MCP tool inventory
    Etsy's MCP documentation lists seven tools (learn_etsy_api, search_etsy_api, list_endpoints, get_endpoint, get_schema, list_guides, and get_guide) and states that the server does not call the Etsy API directly. A tools/list request to the server on October 7, 2026 returned those seven plus an eighth, submit_feedback.     Hands-on verification · checked 2026-10-07 · [Etsy Dev MCP Server documentation](https://developers.etsy.com/documentation/mcp_server/devmcpserver/) MCP session analytics
    When checked on October 7, 2026, the server's tool definitions asked the connected assistant to send a short task description and a session correlation ID with each call for Etsy's analytics, and to call a submit_feedback tool once at the end of every session. The definitions say these fields must not contain personal data or secrets. Etsy's MCP documentation page does not describe this.     Hands-on verification · checked 2026-10-07 · [Etsy Dev MCP Server tools/list check](https://mcp.api.etsycloud.com/mcp) Rate limits
    Etsy applies queries-per-second and queries-per-day limits at the API key level, with the daily limit calculated over a rolling 24-hour window. Exceeding either limit returns HTTP 429 with a retry-after header. Each app's current limits appear in the Developer Portal.     Official announcement · checked 2026-10-07 · [Etsy API rate limits documentation](https://developers.etsy.com/documentation/essentials/rate-limits/) API Terms on automated access
    Etsy's API Terms of Use, last updated August 18, 2026, prohibit using automated systems or browser extensions to access, analyze, or scrape the Etsy Site, the Etsy API, or Etsy data, and prohibit using the API to request Etsy content for machine learning or AI model training, unless Etsy authorizes it in writing. The terms do not mention AI agents by name. This is not legal advice.     Official announcement · checked 2026-10-07 · [Etsy API Terms of Use](https://www.etsy.com/legal/api/) Adoption evidence needed
    Commercial Access approval timelines, which Etsy says vary by proposed use case, and whether Etsy plans to ship a data-access MCP beyond the documentation server.     Evaluation question · reviewed 2026-10-07 · [AI workflow release-readiness review](https://vorplabs.com/workflows/ai-governance/ai-workflow-release-readiness)
Confirmed by Etsy
## What the official sources establish.
  * Etsy documents three access tiers with genuinely different eligibility, review processes, and scope boundaries.
  * A Seller App is restricted to the registered shop only; commercial use is not permitted at this tier.
  * Commercial Access requires a prior approved Personal App, a separate commercial review, and compliance with trademark, branding, and screen-scraping rules.
  * The OpenAPI Dev MCP server connects AI coding assistants to API documentation and schemas, with no API key required.
  * OAuth 2.0 with PKCE is mandatory for all authenticated API access, with tokens expiring in 1 hour.
  * Commercial Access apps that use the transactions_r scope must request buyer_email field access separately.


Not publicly documented
## Operational details not covered by public sources.
  * Whether Etsy plans to ship a data-access MCP server beyond the current documentation and schema server.
  * Typical Commercial Access review timelines or the criteria that distinguish approved from rejected applications.
  * Default rate-limit values for each access tier. Etsy documents per-API-key queries-per-second and queries-per-day limits, and says each app's current limits appear in the Developer Portal, but it does not publish default values by tier.
  * Whether Etsy treats an AI agent working through an approved app as an automated system under the API Terms of Use; the terms do not mention AI agents by name.


Permission questions
## Questions to answer before an agent accesses Etsy shop or buyer data.
  * Which access tier does this use case actually require: own-shop Seller App, broader Personal App, or multi-seller Commercial Access?
  * If the workflow serves multiple sellers, has Commercial Access been approved, or is the integration running on a Personal App beyond its documented scope?
  * Does a Commercial Access workflow need buyer email, and has the separate buyer_email field approval been obtained?
  * Where are OAuth tokens stored, and what happens when the 1-hour access token expires mid-workflow?
  * Does the agent write to listings, orders, or shop settings, and who reviews those mutations before they reach production?


Evaluation plan
## Test the action boundary, not only the happy path.
Etsy's access model has three tiers with genuinely different boundaries: a Seller App that cannot touch other shops, a Personal App with review and scale limits, and Commercial Access that requires a prior approved Personal App and a separate manual review. The MCP server is documentation-only and does not grant data access. An evaluation should establish which tier the use case requires and whether Commercial Access review has been completed.
Test 1
Confirm which access tier your use case requires before starting development; building on a Seller App and later discovering you need Commercial Access adds a review gate mid-project.
Test 2
Verify the documentation MCP server is documentation-only by attempting a data query through it and confirming it does not return live shop data.
Test 3
Implement OAuth 2.0 with PKCE and test the full token lifecycle: initial grant, 1-hour expiry, refresh, and re-authorization on scope change.
Test 4
Test the buyer-email approval process separately if your workflow requires transaction data with buyer contact information.
Test 5
If building for Commercial Access, implement the required trademark disclaimer and verify screen-scraping prohibition compliance before the commercial review.
Test 6
Test failure modes: expired tokens, revoked consent, rate limits, and scope mismatches, and confirm the agent surfaces errors rather than retrying silently.
Do not assume
## Keep the demo narrower than the product claim.
  * The MCP server is not a data-access tool; it exposes documentation and schemas only.
  * A Seller App approval does not extend to serving other sellers; that requires the two-step Commercial Access path.
  * No API key required for the MCP does not mean no authentication required for the API; these are separate things.
  * The April 15, 2026 MCP launch covers the documentation server only; it does not indicate a data-access MCP.
  * Automated Seller App approval does not mean the API Terms of Use permit every use case; review the terms independently.


Re-review when
## New documentation or hands-on evidence changes the answer.
  * Etsy ships an MCP server that provides data access, not just documentation.
  * The Seller App, Personal App, or Commercial Access tier requirements change.
  * Etsy publishes rate limits, AI-specific terms, or restrictions on automated listing management.
  * Etsy changes the Dev MCP Server's tool list or the analytics and feedback instructions in its tool definitions.
  * The API Terms of Use change in ways that affect agent or automated access.


Stay current
## Get the weekly Vorp Change Brief.
A concise weekly briefing on the material changes in AI policy, models, tools, security, and operations, published on Substack.
[Subscribe on Substack](https://vorplabs.substack.com/subscribe)
Subscription happens on Substack. Vorp Labs does not collect your newsletter address on this site.
Update history
2026-10-07
Re-verified against Etsy's developer documentation, its API Terms of Use (last updated August 18, 2026), and its Open API announcements. Added the MCP server's April 15, 2026 launch announcement and tool list, the July 13, 2026 Seller API Access launch, the documented rate-limit mechanism, and the API Terms' automated-access and AI-training clauses, and corrected the buyer email requirement to apply to Commercial Access apps.
2026-07-27
Initial field guide published from Etsy's developer documentation for the three access tiers, the documentation MCP server, and the authentication reference. The MCP server launch date could not be verified.
Related reviews
[Compare agent access models](https://vorplabs.com/agent-tools/access-models)[Credential and safety boundaries](https://vorplabs.com/agent-tools/agent-credential-security)[AI workflow release-readiness review](https://vorplabs.com/workflows/ai-governance/ai-workflow-release-readiness)[MCP server intake checklist](https://vorplabs.com/blog/mcp-server-intake-checklist)[Strava MCP field guide](https://vorplabs.com/agent-tools/strava-mcp)
Primary sources
[Etsy Open API v3 developer documentation](https://developers.etsy.com/documentation/)
Etsy · Official announcement
Reference for the three access tiers (Seller App, Personal App, Commercial Access), the OpenAPI Dev MCP server, screen-scraping prohibition, trademark disclaimer, and buyer email approval requirement.
[Etsy API authentication documentation](https://developers.etsy.com/documentation/essentials/authentication/)
Etsy · Official announcement
Reference for the x-api-key header (keystring and shared secret), OAuth 2.0 with PKCE, token lifetimes (1-hour access, 90-day refresh), and available scopes.
[Etsy Dev MCP Server documentation](https://developers.etsy.com/documentation/mcp_server/devmcpserver/)
Etsy · Hands-on verification
Server URL, the documented tool list, coverage of the Open API v3 spec, and the statement that the server does not call the Etsy API directly. The live tool list was also requested from the server on October 7, 2026.
[Etsy Dev MCP Server tools/list check](https://mcp.api.etsycloud.com/mcp)
Etsy · Hands-on verification
Vorp Labs sent initialize and tools/list requests to the public MCP endpoint on October 7, 2026 and called no tools. The tool definitions returned are a single observation and may change.
[Etsy Open API announcement: Dev MCP Server release](https://github.com/etsy/open-api/discussions/1582)
Etsy · Official announcement
April 15, 2026 launch announcement for the OpenAPI Dev MCP Server, posted by the Open API support account in the discussions forum linked from Etsy's developer documentation.
[Etsy Open API announcement: Seller API Access](https://github.com/etsy/open-api/discussions/1647)
Etsy · Official announcement
July 13, 2026 launch of the Seller API Access tier with automated approval; states that a Personal Key remains the prerequisite for Commercial Access.
[Etsy API rate limits documentation](https://developers.etsy.com/documentation/essentials/rate-limits/)
Etsy · Official announcement
Per-API-key queries-per-second and queries-per-day limits, the rolling 24-hour window, 429 handling, and how to request higher limits.
[Etsy API Terms of Use](https://www.etsy.com/legal/api/)
Etsy · Official announcement
Last updated August 18, 2026. Automated-access, AI-training, order-messaging, and data-display rules, and per-app rate limits set in the Developer Portal. Read in a browser on October 7, 2026.
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



