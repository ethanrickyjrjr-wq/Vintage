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
[Console](https://platform.claude.com/)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fversioning)
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
[API reference](https://platform.claude.com/docs/en/api/overview)Support & configuration
# Versions
Copy page

When making API requests, you must send an `anthropic-version` request header. For example, `anthropic-version: 2026-10-21`. If you are using the [client SDKs](https://platform.claude.com/docs/en/cli-sdks-libraries/overview), this is handled for you automatically.
Copy page

For any given API version, Anthropic preserves:
  * Existing input parameters
  * Existing output parameters


However, Anthropic may do the following:
  * Add additional optional inputs
  * Add additional values to the output
  * Change conditions for specific error types
  * Add new variants to enum-like output values (for example, streaming event types)


Generally, if you are using the API as documented in this reference, Anthropic will not break your usage.
## Version history
Anthropic recommends using the latest API version whenever possible.
  * `2026-10-21`
    * [Migrating to API version 2026-10-21](https://platform.claude.com/docs/en/api/migration-2026-10-21) shows how to upgrade.
    * Available on the Claude API, [Claude Platform on AWS](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws), [Claude Models on Google Cloud (Anthropic managed)](https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/anthropic-managed), [Microsoft Foundry](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry), and [Claude Models on Google Cloud (Google managed)](https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/google-managed). On [Amazon Bedrock](https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock), it's available for Claude 4.7 and later models. For other models on Bedrock, see the [migration guide for API version 2026-10-21](https://platform.claude.com/docs/en/api/migration-2026-10-21#upgrade).
    * Messages API:
      * A request that places a `document` block directly in an `assistant` message returns a 400 error.
      * Sending a `text` block with a non-empty `citations` array in a `user` message, directly or inside a `search_result` block, returns a 400 error.
      * The `temperature`, `top_p`, and `top_k` request parameters are removed. A request that sends any of them returns a 400 error on every model.
    * Admin API:
      * [RBAC groups](https://platform.claude.com/docs/en/api/beta/organization/rbac_groups/list) no longer return `roles`. Use `role_ids` instead.
      * [RBAC group members](https://platform.claude.com/docs/en/api/beta/organization/rbac_groups/members/list), and the response to removing one, no longer return `group_id`. Use `rbac_group_id` instead.
      * [RBAC roles](https://platform.claude.com/docs/en/api/beta/organization/rbac_roles/list) no longer return `name`. Use `display_name` instead.
      * [Organization](https://platform.claude.com/docs/en/api/organization/rate_limits/list) and [workspace](https://platform.claude.com/docs/en/api/organization/workspaces/rate_limits/list) rate-limit entries no longer return `group_type`. Use `group.type` instead.
      * [API keys](https://platform.claude.com/docs/en/api/organization/api_keys/list) no longer return `workspace_id`. Use `scope.workspace_id` instead, which gives the workspace's real ID even for the Default Workspace (an all-workspaces key has no `workspace_id` in `scope`).
    * Claude Enterprise Analytics API:
      * The per-user [usage](https://platform.claude.com/docs/en/api/beta/organization/analytics/user_usage_report/list) and [cost](https://platform.claude.com/docs/en/api/beta/organization/analytics/user_cost_report/list) reports no longer have `actor.email`. Use `actor.email_address` instead.
      * The [activity summaries](https://platform.claude.com/docs/en/api/beta/organization/analytics/summaries/list) response no longer has `summaries`. Use `data` instead.


  * `2023-06-01`
    * New format for [streaming](https://platform.claude.com/docs/en/build-with-claude/streaming) server-sent events (SSE):
      * Completions are incremental. For example, `" Hello"`, `" my"`, `" name"`, `" is"`, `" Claude." ` instead of `" Hello"`, `" Hello my"`, `" Hello my name"`, `" Hello my name is"`, `" Hello my name is Claude."`.
      * All events are [named events](https://developer.mozilla.org/en-US/Web/API/Server-sent%5Fevents/Using%5Fserver-sent%5Fevents#named%5Fevents), rather than [data-only events](https://developer.mozilla.org/en-US/Web/API/Server-sent%5Fevents/Using%5Fserver-sent%5Fevents#data-only%5Fmessages).
      * Removed unnecessary `data: [DONE]` event.
    * Removed legacy `exception` and `truncated` values in responses.
  * `2023-01-01`: Initial release.


Was this page helpful?

  * [Version history](https://platform.claude.com/docs/en/api/versioning#version-history)


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

