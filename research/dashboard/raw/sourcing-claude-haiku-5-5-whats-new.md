[Claude Platform Docs](https://platform.claude.com/docs/en/home)
  * [Messages](https://platform.claude.com/docs/en/intro)
  * [Managed Agents](https://platform.claude.com/docs/en/managed-agents/overview)
  * [Admin](https://platform.claude.com/docs/en/manage-claude/admin-api)
  * Resources
    * [Best practices](https://platform.claude.com/docs/en/about-claude/use-case-guides/overview)
    * [Models & pricing](https://platform.claude.com/docs/en/models/overview)
    * [SDKs, CLI, and libraries](https://platform.claude.com/docs/en/cli-sdks-libraries/overview)
    * [Claude API skill](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/claude-api-skill)
    * [Release notes](https://platform.claude.com/docs/en/release-notes/overview)


[API reference](https://platform.claude.com/docs/en/api/overview)
English
[Console](https://platform.claude.com/)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fmodels%2Fhaiku-5-5%2Fwhats-new-haiku-5-5)

Search`Ctrl``K`
Models
[Models overview](https://platform.claude.com/docs/en/models/overview)
[Claude Fable 5.1](https://platform.claude.com/docs/en/models/fable-5-1/overview)
[Claude Opus 5.5](https://platform.claude.com/docs/en/models/opus-5-5/overview)
[Claude Sonnet 5.5](https://platform.claude.com/docs/en/models/sonnet-5-5/overview)
[Claude Haiku 5.5](https://platform.claude.com/docs/en/models/haiku-5-5/overview)
[Overview](https://platform.claude.com/docs/en/models/haiku-5-5/overview)[What's new](https://platform.claude.com/docs/en/models/haiku-5-5/whats-new-haiku-5-5)[Migration guide](https://platform.claude.com/docs/en/models/haiku-5-5/migration-guide)
Specialized models
Legacy models
Guides
[Choosing a model](https://platform.claude.com/docs/en/about-claude/models/choosing-a-model)[Optimizing for cost and intelligence](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence)[Upgrade between model versions](https://platform.claude.com/docs/en/about-claude/models/migration-guide)
Lifecycle and reference
[Model IDs and versioning](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions)[Model deprecations](https://platform.claude.com/docs/en/about-claude/model-deprecations)[Model cards](https://platform.claude.com/docs/en/resources/overview)[Pricing](https://platform.claude.com/docs/en/about-claude/pricing)[API credits for subscribers](https://platform.claude.com/docs/en/about-claude/api-credits-for-subscribers)
[System prompts](https://platform.claude.com/docs/en/release-notes/system-prompts/overview)
[Console](https://platform.claude.com/)
[Models & pricing](https://platform.claude.com/docs/en/models/overview)Claude Haiku 5.5
# What's new in Claude Haiku 5.5
Copy page

Overview of new capabilities, breaking changes, and behavior changes in Claude Haiku 5.5, with a link to each feature's guide and to the migration guide for code changes.
Copy page

Claude Haiku 5.5 is built for high-volume, latency-sensitive work such as classification, routing, extraction, and subagent tasks. It supports adaptive thinking with the effort parameter, a 1M token context window, and up to 128k output tokens. It uses the same newer tokenizer as Claude 4.7 and later models, so the same text counts as approximately 30 percent more tokens than on Claude Haiku 4.5. Its thinking blocks work only in the account that produced them, or in an account linked to it.
For code changes, see the [migration guide](https://platform.claude.com/docs/en/models/haiku-5-5/migration-guide). For model IDs, pricing, and limits, see the [Claude Haiku 5.5 overview](https://platform.claude.com/docs/en/models/haiku-5-5/overview). For prompting guidance, see [Prompting Claude Haiku 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-haiku-5-5).
## Summary of changes from Claude Haiku 4.5
Each row names one change, whether it is new, changed, or breaking, and what your code has to do.  
| Change  | Type  | Action needed  |  
| --- | --- | --- |  
| [Adaptive thinking and effort](https://platform.claude.com/docs/en/models/haiku-5-5/whats-new-haiku-5-5#adaptive-thinking-and-effort)  | New  | Optional: set `effort` to trade response quality against speed and cost.  |  
| [Larger context window and output](https://platform.claude.com/docs/en/models/haiku-5-5/whats-new-haiku-5-5#larger-context-window-and-output)  | New  | None. Existing `max_tokens` values stay valid, but thinking tokens count toward them. Long prompts are billed at higher prices; see [Long context pricing](https://platform.claude.com/docs/en/about-claude/pricing#long-context-pricing).  |  
| [Browser use tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/browser-use-tool)  | New  | None. Available on the Claude API and Claude Models on Google Cloud (Google managed).  |  
| [Safety classifiers can decline a request](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback#refusal-response)  | New  | Handle `stop_reason: "refusal"` in your client. Server-side fallback isn't available.  |  
| [Manual extended thinking returns an error](https://platform.claude.com/docs/en/models/haiku-5-5/migration-guide#configure-thinking)  | Breaking  | Replace `budget_tokens` with adaptive thinking.  |  
| [Sampling parameters can return an error](https://platform.claude.com/docs/en/models/haiku-5-5/migration-guide#remove-sampling-parameters)  | Breaking  | Omit `temperature`, `top_p`, and `top_k`.  |  
| [Assistant message prefill returns an error](https://platform.claude.com/docs/en/models/haiku-5-5/migration-guide#replace-assistant-prefill)  | Breaking  | End `messages` with a user turn.  |  
|  [`computer_20250124` returns an error](https://platform.claude.com/docs/en/models/haiku-5-5/migration-guide#computer-use-toolset) on the Claude API, Claude Models on Google Cloud (Google managed), and Amazon Bedrock  | Breaking  | Replace it with `computer_toolset_20260801` on the Claude API and Claude Models on Google Cloud (Google managed), or with `computer_20251124` on Amazon Bedrock.  |  
| [Changing earlier turns invalidates thinking blocks](https://platform.claude.com/docs/en/models/haiku-5-5/migration-guide#keep-earlier-turns-unchanged)  | Breaking  | Keep conversations append-only if you send thinking blocks back.  |  
| [Responses can start with thinking blocks](https://platform.claude.com/docs/en/models/haiku-5-5/whats-new-haiku-5-5#responses-can-begin-with-thinking-blocks)  | Changed  | Select content blocks by `type`, not by position.  |  
| [Thinking text is omitted by default](https://platform.claude.com/docs/en/models/haiku-5-5/migration-guide#configure-thinking)  | Changed  | To receive summarized thinking, set `thinking.display` to `"summarized"`.  |  
| [Same text counts as more tokens](https://platform.claude.com/docs/en/models/haiku-5-5/whats-new-haiku-5-5#same-text-counts-as-more-tokens)  | Changed  | Recount prompts and revisit `max_tokens` and cost estimates.  |  
| [Replaying thinking blocks across accounts](https://platform.claude.com/docs/en/models/haiku-5-5/whats-new-haiku-5-5#replaying-thinking-blocks-across-accounts)  | Changed  | If you replay stored conversations through a different account, replay each through the account that produced it.  |  
| [Earlier thinking blocks stay in context](https://platform.claude.com/docs/en/models/haiku-5-5/whats-new-haiku-5-5#earlier-thinking-blocks-stay-in-context)  | Changed  | Expect more input tokens in multi-turn conversations. To remove older blocks, use [thinking block clearing](https://platform.claude.com/docs/en/build-with-claude/context-editing#thinking-block-clearing).  |  
| [Shorter prompts can be cached](https://platform.claude.com/docs/en/build-with-claude/prompt-caching#cache-limitations)  | Changed  | None. The minimum cacheable prompt length is 512 tokens, down from 4,096 on Claude Haiku 4.5, so a prompt in between that sets `cache_control` is cached on Claude Haiku 5.5.  |  
| [Context awareness tags aren't injected](https://platform.claude.com/docs/en/build-with-claude/context-windows#context-awareness)  | Changed  | To give the model an explicit budget for an agentic loop, use [task budgets](https://platform.claude.com/docs/en/build-with-claude/task-budgets) (beta).  |  
## New capabilities
### Adaptive thinking and effort
With [adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/thinking), Claude Haiku 5.5 determines when and how much to think. Adaptive thinking is on by default. Although you can still turn thinking off with `thinking: {"type": "disabled"}` at `high` effort or below, the better way to trade response quality against speed and cost is to use the [effort parameter](https://platform.claude.com/docs/en/build-with-claude/effort).
### Larger context window and output
Claude Haiku 5.5 has a 1M token [context window](https://platform.claude.com/docs/en/build-with-claude/context-windows) and returns up to 128k output tokens, up from 200k and 64k on Claude Haiku 4.5. Existing `max_tokens` values stay valid, but thinking tokens count toward `max_tokens`, so a small limit can stop after a `thinking` block and before any text. See [Configure thinking](https://platform.claude.com/docs/en/models/haiku-5-5/migration-guide#configure-thinking). Long prompts are billed at higher prices; see [Long context pricing](https://platform.claude.com/docs/en/about-claude/pricing#long-context-pricing).
## Behavior changes
### Responses can start with thinking blocks
Adaptive thinking is on by default, so a response can start with one or more `thinking` blocks even when the request doesn't mention thinking. Code that reads the first content block as the answer needs to select blocks by their `type` field. See [Configure thinking](https://platform.claude.com/docs/en/models/haiku-5-5/migration-guide#configure-thinking) in the migration guide.
### Earlier thinking blocks stay in context
Claude Haiku 5.5 keeps thinking blocks from all earlier assistant turns in context, and they count as input tokens. Claude Haiku 4.5 kept only the latest turn's blocks. Multi-turn conversations therefore carry more input tokens than the tokenizer change alone explains. To remove older blocks, use [thinking block clearing](https://platform.claude.com/docs/en/build-with-claude/context-editing#thinking-block-clearing). See [Thinking block preservation by model](https://platform.claude.com/docs/en/build-with-claude/thinking#thinking-block-preservation-by-model).
### Same text counts as more tokens
Claude Haiku 5.5 uses the same newer tokenizer as Claude 4.7 and later models. As with all models that use this tokenizer, the same input text produces approximately 30 percent more tokens on Claude Haiku 5.5 than on Claude Haiku 4.5. The exact increase depends on the content. The shape of requests and responses doesn't depend on the tokenizer, but anything you measure or budget in tokens changes. See [Recount tokens](https://platform.claude.com/docs/en/models/haiku-5-5/migration-guide#recount-tokens) in the migration guide.
### Replaying thinking blocks across accounts
Thinking blocks from Claude Haiku 5.5 work only in the account that produced them, or in an account linked to it. This matters only if you store conversations and replay them through a different account. See [Replay thinking blocks through the account that produced them](https://platform.claude.com/docs/en/models/haiku-5-5/migration-guide#replay-thinking-blocks-through-the-producing-account).
Was this page helpful?

  * [Summary of changes from Claude Haiku 4.5](https://platform.claude.com/docs/en/models/haiku-5-5/whats-new-haiku-5-5#summary-of-changes-from-claude-haiku-4-5)
  * [New capabilities](https://platform.claude.com/docs/en/models/haiku-5-5/whats-new-haiku-5-5#new-capabilities)
  * [Adaptive thinking and effort](https://platform.claude.com/docs/en/models/haiku-5-5/whats-new-haiku-5-5#adaptive-thinking-and-effort)
  * [Larger context window and output](https://platform.claude.com/docs/en/models/haiku-5-5/whats-new-haiku-5-5#larger-context-window-and-output)
  * [Behavior changes](https://platform.claude.com/docs/en/models/haiku-5-5/whats-new-haiku-5-5#behavior-changes)
  * [Responses can start with thinking blocks](https://platform.claude.com/docs/en/models/haiku-5-5/whats-new-haiku-5-5#responses-can-begin-with-thinking-blocks)
  * [Earlier thinking blocks stay in context](https://platform.claude.com/docs/en/models/haiku-5-5/whats-new-haiku-5-5#earlier-thinking-blocks-stay-in-context)
  * [Same text counts as more tokens](https://platform.claude.com/docs/en/models/haiku-5-5/whats-new-haiku-5-5#same-text-counts-as-more-tokens)
  * [Replaying thinking blocks across accounts](https://platform.claude.com/docs/en/models/haiku-5-5/whats-new-haiku-5-5#replaying-thinking-blocks-across-accounts)


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

