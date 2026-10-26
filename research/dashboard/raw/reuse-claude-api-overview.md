[Claude Platform Docs](https://platform.claude.com/docs/en/home)
  * [Messages](https://platform.claude.com/docs/en/intro)
  * [Managed Agents](https://platform.claude.com/docs/en/managed-agents/overview)
  * [Admin](https://platform.claude.com/docs/en/manage-claude/admin-api)
  * Resources
    * [Best practices](https://platform.claude.com/docs/en/about-claude/use-case-guides/overview)
    * [Models & pricing](https://platform.claude.com/docs/en/models/overview)
    * [SDKs, CLI, and libraries](https://platform.claude.com/docs/en/cli-sdks-libraries/overview)
    * [Claude API skill](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/claude-api-skill)
    * [Release notes](https://platform.claude.com/docs/en/release-notes/overview)


[API reference](https://platform.claude.com/docs/en/api/overview)
English
[Console](https://platform.claude.com/)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Foverview)

Search`Ctrl``K`
Include beta APIs
Using the API
[Features overview](https://platform.claude.com/docs/en/api/overview)[Beta headers](https://platform.claude.com/docs/en/api/beta-headers)[Errors](https://platform.claude.com/docs/en/api/errors)
[Messages](https://platform.claude.com/docs/en/api/http/beta/messages)[ Create a Message ](https://platform.claude.com/docs/en/api/http/beta/messages/create)[ Count tokens in a Message ](https://platform.claude.com/docs/en/api/http/beta/messages/count_tokens)
Batches
Managed Agents
Agents
Environments
Sessions
Deployments
Deployment Runs
Vaults
Memory Stores
Dreams
[Files](https://platform.claude.com/docs/en/api/http/beta/files)[ Upload File ](https://platform.claude.com/docs/en/api/http/beta/files/upload)[ List Files ](https://platform.claude.com/docs/en/api/http/beta/files/list)[ Download File ](https://platform.claude.com/docs/en/api/http/beta/files/download)[ Get File Metadata ](https://platform.claude.com/docs/en/api/http/beta/files/retrieve_metadata)[ Delete File ](https://platform.claude.com/docs/en/api/http/beta/files/delete)
[Models](https://platform.claude.com/docs/en/api/http/beta/models)[ List Models ](https://platform.claude.com/docs/en/api/http/beta/models/list)[ Get a Model ](https://platform.claude.com/docs/en/api/http/beta/models/retrieve)
[Organization](https://platform.claude.com/docs/en/api/http/beta/organization)[ Get Current Organization ](https://platform.claude.com/docs/en/api/http/beta/organization/retrieve)
API Keys
External Keys
Federation
Invites
Service Accounts
Users
Workspaces
Rate Limits
Compliance Settings
Usage Report
Cost Report
MCP Tunnels
Analytics
Spend Limits
RBAC Groups
RBAC Roles
Plugins
Plugin Marketplaces
Telemetry Destinations
Webhooks
Claude Tag
[Skills](https://platform.claude.com/docs/en/api/http/beta/skills)[ Create Skill ](https://platform.claude.com/docs/en/api/http/beta/skills/create)[ List Skills ](https://platform.claude.com/docs/en/api/http/beta/skills/list)[ Get Skill ](https://platform.claude.com/docs/en/api/http/beta/skills/retrieve)[ Delete Skill ](https://platform.claude.com/docs/en/api/http/beta/skills/delete)
Versions
[User Profiles](https://platform.claude.com/docs/en/api/http/beta/user_profiles)[ Create User Profile ](https://platform.claude.com/docs/en/api/http/beta/user_profiles/create)[ List User Profiles ](https://platform.claude.com/docs/en/api/http/beta/user_profiles/list)[ Get User Profile ](https://platform.claude.com/docs/en/api/http/beta/user_profiles/retrieve)[ Update User Profile ](https://platform.claude.com/docs/en/api/http/beta/user_profiles/update)[ Delete User Profile ](https://platform.claude.com/docs/en/api/http/beta/user_profiles/delete)[ Create Enrollment URL ](https://platform.claude.com/docs/en/api/http/beta/user_profiles/create_enrollment_url)
Action URLs
[Tunnels ](https://platform.claude.com/docs/en/api/http/beta/tunnels)[ Create Tunnel ](https://platform.claude.com/docs/en/api/http/beta/tunnels/create)[ Get Tunnel ](https://platform.claude.com/docs/en/api/http/beta/tunnels/retrieve)[ List Tunnels ](https://platform.claude.com/docs/en/api/http/beta/tunnels/list)[ Archive Tunnel ](https://platform.claude.com/docs/en/api/http/beta/tunnels/archive)[ Reveal Tunnel Token ](https://platform.claude.com/docs/en/api/http/beta/tunnels/reveal_token)[ Rotate Tunnel Token ](https://platform.claude.com/docs/en/api/http/beta/tunnels/rotate_token)
Certificates
[Compliance API](https://platform.claude.com/docs/en/api/http/compliance)
Activities
Organizations
Groups
Apps
[Completions](https://platform.claude.com/docs/en/api/http/completions)[ Create a Text Completion Deprecated ](https://platform.claude.com/docs/en/api/http/completions/create)
OpenTelemetry
[Spans](https://platform.claude.com/docs/en/api/opentelemetry/spans)
Support & configuration
[Rate limits](https://platform.claude.com/docs/en/api/rate-limits)[Service tiers](https://platform.claude.com/docs/en/api/service-tiers)[AWS IAM actions](https://platform.claude.com/docs/en/api/claude-platform-on-aws-iam-actions)[Google Cloud IAM permissions](https://platform.claude.com/docs/en/api/claude-models-on-google-cloud-anthropic-managed-iam-permissions)[Versions](https://platform.claude.com/docs/en/api/versioning)[Migrating to API version 2026-10-21](https://platform.claude.com/docs/en/api/migration-2026-10-21)[IP addresses](https://platform.claude.com/docs/en/api/ip-addresses)[Supported regions](https://platform.claude.com/docs/en/api/supported-regions)
Claude Code
[Trigger a routine](https://platform.claude.com/docs/en/api/claude-code/routines-fire)
[Console](https://platform.claude.com/)
API referenceUsing the API
# API overview
Copy page

Understand the Claude API's available endpoints, authentication headers, client SDKs, pagination, rate limits, and cloud platform access options.
Copy page

The Claude API is a RESTful API at `https://api.anthropic.com` that provides programmatic access to Claude models and Claude Managed Agents.

**New to Claude?** For direct model access, start with [Get started](https://platform.claude.com/docs/en/get-started) and [Working with Messages](https://platform.claude.com/docs/en/build-with-claude/working-with-messages). For managed agent infrastructure, see the [Claude Managed Agents quickstart](https://platform.claude.com/docs/en/managed-agents/quickstart).
## Prerequisites
To use the Claude API, you need:
  * A [Claude Console account](https://platform.claude.com/)
  * An [API key](https://platform.claude.com/settings/keys) from the Console, or a configured [Workload Identity Federation](https://platform.claude.com/docs/en/manage-claude/workload-identity-federation) rule


For step-by-step setup instructions, see [Get started](https://platform.claude.com/docs/en/get-started).
## Available APIs
The Claude API includes the following APIs:
  * **[Messages API](https://platform.claude.com/docs/en/api/messages/create):** Send messages to Claude for conversational interactions (`POST /v1/messages`)
  * **[Message Batches API](https://platform.claude.com/docs/en/api/messages/batches/create):** Process large volumes of Messages requests asynchronously with a 50 percent cost reduction (`POST /v1/messages/batches`)
  * **[Token Counting API](https://platform.claude.com/docs/en/api/messages/count_tokens):** Count tokens in a message before sending to manage costs and rate limits (`POST /v1/messages/count_tokens`)
  * **[Models API](https://platform.claude.com/docs/en/api/models/list):** List available Claude models and their details (`GET /v1/models`)
  * **[Files API](https://platform.claude.com/docs/en/api/files/upload):** Upload and manage files for use across multiple API calls (`POST /v1/files`, `GET /v1/files`)
  * **[Skills API](https://platform.claude.com/docs/en/api/skills/create):** Create and manage custom agent skills (`POST /v1/skills`, `GET /v1/skills`)


The following APIs are in beta:
  * **[Agents API](https://platform.claude.com/docs/en/managed-agents/agent-setup):** Define reusable, versioned agent configurations for Claude Managed Agents (`POST /v1/agents`, `GET /v1/agents`)
  * **[Sessions API](https://platform.claude.com/docs/en/managed-agents/sessions):** Run stateful agent sessions in managed cloud sandboxes (`POST /v1/sessions`, `GET /v1/sessions/{id}/events/stream`)
  * **[Environments API](https://platform.claude.com/docs/en/managed-agents/environments):** Configure sandbox templates for agent sessions (`POST /v1/environments`, `GET /v1/environments`)


For the complete API reference with all endpoints, parameters, and response schemas, explore the API reference pages listed in the navigation. To access beta features, see [Beta headers](https://platform.claude.com/docs/en/api/beta-headers).
## Authentication
For details on each authentication method and when to use it, see [Authentication](https://platform.claude.com/docs/en/manage-claude/authentication). Requests to the Claude API include these headers:  
| Header  | Value  | Required  |  
| --- | --- | --- |  
| `Authorization`  |  `Bearer <token>`, where `<token>` is your API key or a short-lived access token obtained from `POST /v1/oauth/token` through [Workload Identity Federation](https://platform.claude.com/docs/en/manage-claude/workload-identity-federation)  | Yes, unless `x-api-key` is set  |  
| `x-api-key`  | Your API key from Console. Legacy fallback for `Authorization`, still supported  | No  |  
| `anthropic-workspace-id`  | ID of the [workspace](https://platform.claude.com/docs/en/manage-claude/workspaces) the request runs in (for example, `wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ`). See [Select a workspace](https://platform.claude.com/docs/en/manage-claude/authentication#select-a-workspace).  | Required with an API key that isn't scoped to a workspace. Optional for other API keys. A key created for a single workspace runs in that workspace when you omit the header. Not used with Workload Identity Federation tokens, which select a workspace at token exchange.  |  
| `anthropic-version`  | API version (for example, `2026-10-21`)  | Yes  |  
| `content-type`  | `application/json`  | Yes  |  
If you are using the [Client SDKs](https://platform.claude.com/docs/en/api/overview#client-sdks), the SDK sends the authentication, version, and content-type headers automatically; you pass `anthropic-workspace-id` yourself when your key needs it. For API versioning details, see [API versions](https://platform.claude.com/docs/en/api/versioning).
When accessing Claude through a [cloud platform](https://platform.claude.com/docs/en/api/overview#claude-api-vs-cloud-platforms), authentication is integrated with the cloud provider's IAM system. See the platform-specific documentation for supported credential types, required headers, and authentication options.
### Getting API keys
The API is made available through the web [Console](https://platform.claude.com/). In the Console, you can use [playground](https://platform.claude.com/playground) (`platform.claude.com/playground`) to try out the API in the browser and then generate API keys on the [API keys](https://platform.claude.com/settings/keys) page (`platform.claude.com/settings/keys`). To learn how, see [Get your Claude API key](https://platform.claude.com/docs/en/get-api-key). You choose each key's type (see [Key types](https://platform.claude.com/docs/en/manage-claude/authentication#key-types)) and its [expiration](https://platform.claude.com/docs/en/manage-claude/authentication#key-expiration) when you create it. Use [workspaces](https://platform.claude.com/settings/workspaces) in the Console to separate environments and [control spend](https://platform.claude.com/docs/en/api/rate-limits) by use case.
## Client SDKs
Anthropic provides official SDKs that simplify API integration by handling authentication, request formatting, error handling, and more.
**Benefits:**
  * Automatic header management (authentication, `anthropic-version`, `content-type`)
  * Type-safe request and response handling
  * Built-in retry logic and error handling
  * Streaming support
  * Request timeouts and connection management


For a list of client SDKs, see [SDKs, CLI, and libraries](https://platform.claude.com/docs/en/cli-sdks-libraries/overview).
## Claude API versus cloud platforms
Claude is available through the direct Claude API and through cloud platforms. Choose based on your infrastructure, feature availability, compliance requirements, and pricing preferences.
### Claude API
  * **Direct access** to the latest models and features
  * **Anthropic billing and support**
  * **Best for:** New integrations, full feature access, direct relationship with Anthropic


### Cloud platform APIs
Access Claude through AWS, Google Cloud, or Microsoft Azure:
  * **Integrated** with cloud provider billing and IAM
  * **Feature availability varies by platform:** Anthropic-operated platforms include [Claude Platform on AWS](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws), [Claude Models on Google Cloud (Anthropic managed)](https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/anthropic-managed), and [Microsoft Foundry](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry); partner-operated platforms include Amazon Bedrock and Claude Models on Google Cloud (Google managed). See each platform's page for feature availability and timing.
  * **Best for:** Existing cloud commitments, specific compliance requirements, consolidated cloud billing

  
| Platform  | Provider  | Documentation  |  
| --- | --- | --- |  
| Claude Models on Google Cloud (Google managed)  | Google Cloud  | [Claude Models on Google Cloud (Google managed)](https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/google-managed)  |  
| Amazon Bedrock  | AWS  | [Claude in Amazon Bedrock](https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock)  |  
| Claude Platform on AWS  | AWS (Anthropic-operated)  | [Claude Platform on AWS](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws)  |  
| Claude Models on Google Cloud (Anthropic managed)  | Google Cloud (Anthropic-operated)  | [Claude Models on Google Cloud (Anthropic managed)](https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/anthropic-managed)  |  
| Microsoft Foundry  | Microsoft Azure (Anthropic-operated)  | [Claude in Microsoft Foundry](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry)  |  

Claude Managed Agents is available through the direct Claude API, [Claude Platform on AWS](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws), and [Claude Models on Google Cloud (Anthropic managed)](https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/anthropic-managed). For feature availability across platforms, see the [Features overview](https://platform.claude.com/docs/en/build-with-claude/overview).
## Request and response format
### Request size limits  
| Endpoint  | Maximum request size  |  
| --- | --- |  
| Messages, Token Counting  | 32 MB  |  
| Message Batches API (see [Batch processing](https://platform.claude.com/docs/en/build-with-claude/batch-processing))  | 256 MB  |  
| [Files API](https://platform.claude.com/docs/en/build-with-claude/files)  | 500 MB  |  
| Sessions, Agents, Environments  | 32 MB  |  
If you exceed these limits, you'll receive a 413 `request_too_large` error.

Partner-operated platforms have their own request size limits: Bedrock limits requests to 20 MB, and Claude Models on Google Cloud (Google managed) limits requests to 30 MB. Claude Platform on AWS uses the same limits as the direct Claude API. Consult your platform's documentation for current values.
### Response headers
The Claude API includes the following headers in its responses:  
| Header  | Description  |  
| --- | --- |  
| `request-id`  | A globally unique identifier for the request, such as `req_018EeWyXxfu5pfWkrYcMdjWG`. Include it when you contact support about a specific request. See [Request ID](https://platform.claude.com/docs/en/api/errors#request-id).  |  
| `anthropic-organization-id`  | The ID of the organization that the API key or access token used in the request belongs to.  |  
| `anthropic-workspace-id`  | The `wrkspc_`-prefixed ID of the [workspace](https://platform.claude.com/docs/en/manage-claude/workspaces) that the API key or access token resolved to, such as `wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ`, including when that is your organization's Default Workspace. Absent when the credential doesn't resolve to a workspace (for example, on Admin API requests) or the request fails before authentication completes. See [Identify the workspace behind an API response](https://platform.claude.com/docs/en/manage-claude/workspaces#identify-the-workspace-behind-an-api-response).  |  
For the rate limit headers, see [Response headers](https://platform.claude.com/docs/en/api/rate-limits#response-headers) in Rate limits. For examples that read a response header by name with each SDK, see [Identify the workspace behind an API response](https://platform.claude.com/docs/en/manage-claude/workspaces#identify-the-workspace-behind-an-api-response).

Claude Platform on AWS adds an AWS request ID (`x-amzn-requestid`) alongside the standard `request-id` header. See [Request IDs](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws#request-ids) for the dual-ID handling pattern.
## Pagination
List endpoints return results in pages. Most newer list endpoints use the `page` and `next_page` cursor scheme described in this section. Some use a different scheme; see the note at the end of this section. Use the `limit` query parameter to control the page size and the `page` query parameter to fetch an adjacent page. Each response includes a `data` array alongside cursor fields for navigating between pages.  
| Name  | Location  | Description  |  
| --- | --- | --- |  
| `limit`  | Query parameter  | Maximum number of items to return per page.  |  
| `page`  | Query parameter  | Opaque cursor from a previous response. Pass a `next_page` or `prev_page` value here to fetch the adjacent page.  |  
| `order`  | Query parameter  | Sort direction for the results (`asc` or `desc`), on list endpoints that support sorting. A `page` cursor is only valid with the `order` it was created with.  |  
| `next_page`  | Response field  | Cursor for the next page, or `null` if there are no more results.  |  
| `prev_page`  | Response field  | Cursor for the previous page on endpoints that support backward pagination (currently `GET /v1/sessions`), or `null` if you are on the first page. Other list endpoints omit the field.  |  
To go back a page, pass `prev_page` as the `page` parameter. `prev_page` is `null` when you're on the first page. Not all list endpoints support `prev_page`. Only `GET /v1/sessions` returns `prev_page`; on list endpoints that do not support backward pagination, the field is absent from the response rather than `null`. For a request walkthrough, see [Listing sessions](https://platform.claude.com/docs/en/managed-agents/session-operations#listing-sessions).
The SDK provides an auto-paginating iterator that follows `next_page` for you. For example, `for session in client.beta.sessions.list()` walks through every session. SDK auto-pagination is forward-only; to go back a page, read `prev_page` from the response and pass it back as the `page` parameter yourself. See [SDKs, CLI, and libraries](https://platform.claude.com/docs/en/cli-sdks-libraries/overview) for details.

Some list endpoints use a different cursor scheme. The Message Batches API (see [Batch processing](https://platform.claude.com/docs/en/build-with-claude/batch-processing)), the [Models API](https://platform.claude.com/docs/en/api/models/list), and several [Admin API](https://platform.claude.com/docs/en/manage-claude/admin-api) endpoints take `after_id` and `before_id` query parameters instead of `page`. Their responses return `has_more`, `first_id`, and `last_id` instead of `next_page`. See the reference page for each endpoint for its exact pagination fields.
## Rate limits and availability
### Rate limits
The API enforces rate limits and spend limits to prevent misuse and manage capacity. Limits are organized into usage tiers; your organization is placed on a tier automatically and can move to a higher tier over time. Each tier has:
  * **Spend limits:** Maximum monthly cost for API usage
  * **Rate limits:** Maximum number of requests per minute (RPM) and tokens per minute (TPM)


You can view your rate limits under [Rate limits in the Claude Console](https://platform.claude.com/usage/limits) and your spend limits on the Console's [Billing](https://platform.claude.com/settings/billing) page. For higher rate limits or a higher monthly spend cap, use **Request tier increase** on the **Rate limits** page.
For detailed information about limits, tiers, and the token bucket algorithm used for rate limiting, see [Rate limits](https://platform.claude.com/docs/en/api/rate-limits).
### Availability
The Claude API is available in [many countries and regions](https://platform.claude.com/docs/en/api/supported-regions) worldwide. Check the supported regions page to confirm availability in your location.
## Next steps

[Messages API reference](https://platform.claude.com/docs/en/api/messages/create)
Complete API specification for direct model interactions

[Claude Managed Agents reference](https://platform.claude.com/docs/en/managed-agents/sessions)
Agents, Sessions, and Environments endpoints

[Client SDKs](https://platform.claude.com/docs/en/cli-sdks-libraries/overview)
Python, TypeScript, C#, Go, Java, PHP, and Ruby

[Rate limits](https://platform.claude.com/docs/en/api/rate-limits)
Usage tiers, requesting higher limits, and the token bucket algorithm
Was this page helpful?

  * [Prerequisites](https://platform.claude.com/docs/en/api/overview#prerequisites)
  * [Available APIs](https://platform.claude.com/docs/en/api/overview#available-apis)
  * [Authentication](https://platform.claude.com/docs/en/api/overview#authentication)
  * [Getting API keys](https://platform.claude.com/docs/en/api/overview#getting-api-keys)
  * [Client SDKs](https://platform.claude.com/docs/en/api/overview#client-sdks)
  * [Claude API versus cloud platforms](https://platform.claude.com/docs/en/api/overview#claude-api-vs-cloud-platforms)
  * [Claude API](https://platform.claude.com/docs/en/api/overview#claude-api)
  * [Cloud platform APIs](https://platform.claude.com/docs/en/api/overview#cloud-platform-apis)
  * [Request and response format](https://platform.claude.com/docs/en/api/overview#request-and-response-format)
  * [Request size limits](https://platform.claude.com/docs/en/api/overview#request-size-limits)
  * [Response headers](https://platform.claude.com/docs/en/api/overview#response-headers)
  * [Pagination](https://platform.claude.com/docs/en/api/overview#pagination)
  * [Rate limits and availability](https://platform.claude.com/docs/en/api/overview#rate-limits-and-availability)
  * [Rate limits](https://platform.claude.com/docs/en/api/overview#rate-limits)
  * [Availability](https://platform.claude.com/docs/en/api/overview#availability)
  * [Next steps](https://platform.claude.com/docs/en/api/overview#next-steps)


[Claude Platform Docs](https://platform.claude.com/docs/en/home)
[](https://x.com/claudeai)[](https://www.threads.com/@claudeai)[](https://www.linkedin.com/showcase/claude)[](https://www.youtube.com/@anthropic-ai)[](https://instagram.com/claudeai)

### Solutions
  * [AI agents](https://claude.com/solutions/agents)
  * [Code modernization](https://claude.com/solutions/code-modernization)
  * [Coding](https://claude.com/solutions/coding)
  * [Customer support](https://claude.com/solutions/customer-support)
  * [Financial services](https://claude.com/solutions/financial-services)
  * [Government](https://claude.com/solutions/government)
  * [Higher education](https://claude.com/solutions/education)
  * [K-12 teachers](https://claude.com/solutions/teachers)
  * [Life sciences](https://claude.com/solutions/life-sciences)


### Partners
  * [Claude on AWS](https://claude.com/partners/amazon-bedrock)
  * [Claude on Google Cloud](https://claude.com/partners/google-cloud-vertex-ai)


### Learn
  * [Blog](https://claude.com/blog)
  * [Courses](https://claude.com/resources/courses)
  * [Use cases](https://claude.com/resources/use-cases)
  * [Connectors](https://claude.com/partners/mcp)
  * [Customer stories](https://claude.com/customers)
  * [Engineering at Anthropic](https://www.anthropic.com/engineering)
  * [Events](https://www.anthropic.com/events)
  * [Powered by Claude](https://claude.com/partners/powered-by-claude)
  * [Service partners](https://claude.com/partners/services)
  * [Startups program](https://claude.com/programs/startups)


### Company
  * [Anthropic](https://www.anthropic.com/company)
  * [Careers](https://www.anthropic.com/careers)
  * [Economic Futures](https://www.anthropic.com/economic-futures)
  * [Research](https://www.anthropic.com/research)
  * [News](https://www.anthropic.com/news)
  * [Responsible Scaling Policy](https://www.anthropic.com/news/announcing-our-updated-responsible-scaling-policy)
  * [Security and compliance](https://trust.anthropic.com)
  * [Transparency](https://www.anthropic.com/transparency)


### Learn
  * [Blog](https://claude.com/blog)
  * [Courses](https://claude.com/resources/courses)
  * [Use cases](https://claude.com/resources/use-cases)
  * [Connectors](https://claude.com/partners/mcp)
  * [Customer stories](https://claude.com/customers)
  * [Engineering at Anthropic](https://www.anthropic.com/engineering)
  * [Events](https://www.anthropic.com/events)
  * [Powered by Claude](https://claude.com/partners/powered-by-claude)
  * [Service partners](https://claude.com/partners/services)
  * [Startups program](https://claude.com/programs/startups)


### Help and security
  * [Availability](https://www.anthropic.com/supported-countries)
  * [Status](https://status.claude.com/)
  * [Support](https://support.claude.com/)
  * [Discord](https://www.anthropic.com/discord)


### Terms and policies
  * [Privacy policy](https://www.anthropic.com/legal/privacy)
  * [Responsible disclosure policy](https://www.anthropic.com/responsible-disclosure-policy)
  * [Terms of service: Commercial](https://www.anthropic.com/legal/commercial-terms)
  * [Terms of service: Consumer](https://www.anthropic.com/legal/consumer-terms)
  * [Usage policy](https://www.anthropic.com/legal/aup)


Ask Docs

