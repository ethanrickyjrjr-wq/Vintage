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
[Console](https://platform.claude.com/)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fmodels%2Fhaiku-5-5%2Foverview)
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
[Models & pricing](https://platform.claude.com/docs/en/models/overview)Models
![](https://platform.claude.com/images/dashboard-discovery/bird.svg?dpl=0a82b0fca8e491f3681e1bfdb6f80293938b929b-dc8ad335)
# Claude Haiku 5.5Latest
For high-volume, latency-sensitive tasks such as classification, extraction, and routing
Copy page

claude-haiku-5-5[Try in playground](https://platform.claude.com/playground?model=claude-haiku-5-5)
Copy page

[Announcement(opens in new tab)](https://www.anthropic.com/claude-haiku-5-5)[What’s new](https://platform.claude.com/docs/en/models/haiku-5-5/whats-new-haiku-5-5)[Migration guide](https://platform.claude.com/docs/en/models/haiku-5-5/migration-guide) Context window
     1Mtokens Max output
     128Ktokens Input pricing
     From $0.10/ MTok Output pricing
     From $0.50/ MTok
## Overview
Claude Haiku 5.5 is built for high-volume, latency-sensitive work such as classification, routing, extraction, and subagent tasks. It supports adaptive thinking with the effort parameter, a 1M token context window, and up to 128k output tokens. It uses the same newer tokenizer as Claude 4.7 and later models, so the same text counts as approximately 30 percent more tokens than on Claude Haiku 4.5. Its thinking blocks work only in the account that produced them, or in an account linked to it.
For code changes, see the [migration guide](https://platform.claude.com/docs/en/models/haiku-5-5/migration-guide). For model IDs, pricing, and limits, see the [Claude Haiku 5.5 overview](https://platform.claude.com/docs/en/models/haiku-5-5/overview). For prompting guidance, see [Prompting Claude Haiku 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-haiku-5-5).
[What's new in Claude Haiku 5.5](https://platform.claude.com/docs/en/models/haiku-5-5/whats-new-haiku-5-5)
## How it compares  
| Model  | Context  | Max output  | Price / MTok  | Latency  | Thinking  | Default effort  | Knowledge cutoff  |  
| --- | --- | --- | --- | --- | --- | --- | --- |  
| [Claude Fable 5.1](https://platform.claude.com/docs/en/models/fable-5-1/overview)  | 1M  | 128K  | $10 / $50  | Slower  | Adaptive (always on)  | `high`  | Jun 2026  |  
| [Claude Opus 5.5](https://platform.claude.com/docs/en/models/opus-5-5/overview)  | 1M  | 128K  | $4 / $20  | Moderate  | Adaptive (always on)  | `medium`  | Jun 2026  |  
| [Claude Sonnet 5.5](https://platform.claude.com/docs/en/models/sonnet-5-5/overview)  | 1M  | 128K  | $2 / $10  | Fast  | Adaptive  | `high`  | Jun 2026  |  
| Claude Haiku 5.5This model  | 1M  | 128K  | From $0.10 / $0.50  | Fastest  | Adaptive  | `medium`  | Jun 2026  |  
## Specifications
### Model IDs Claude API
    claude-haiku-5-5 [Amazon Bedrock](https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock)
    anthropic.claude-haiku-5-5 [Claude Models on Google Cloud (Google managed)](https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/google-managed)
    claude-haiku-5-5 [Microsoft Foundry](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry)
    claude-haiku-5-5 [Claude Platform on AWS](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws)
    claude-haiku-5-5 [Claude Models on Google Cloud (Anthropic managed)](https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/anthropic-managed)
    claude-haiku-5-5
### Pricing Input
    $0.10 / MTok for prompts up to 100,000 tokens$0.50 / MTok for prompts over 100,000 tokens Output
    $0.50 / MTok for prompts up to 100,000 tokens$2.50 / MTok for prompts over 100,000 tokens [5m cache write](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)
    $0.125 / MTok for prompts up to 100,000 tokens$0.625 / MTok for prompts over 100,000 tokens [1h cache write](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)
    $0.20 / MTok for prompts up to 100,000 tokens$1 / MTok for prompts over 100,000 tokens [Cache read](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)
    $0.01 / MTok for prompts up to 100,000 tokens$0.05 / MTok for prompts over 100,000 tokens [Batch API](https://platform.claude.com/docs/en/build-with-claude/batch-processing)
    50% discount on input and output
[Full price list](https://platform.claude.com/docs/en/about-claude/pricing)
### Capabilities [Context window](https://platform.claude.com/docs/en/build-with-claude/context-windows)
    1M tokens Max output
    128K tokens [Max output (Batch API, beta)](https://platform.claude.com/docs/en/build-with-claude/batch-processing#extended-output-beta)
    300K tokens [Thinking](https://platform.claude.com/docs/en/build-with-claude/thinking)
    Adaptive [Default effort](https://platform.claude.com/docs/en/build-with-claude/effort)
    `medium` Comparative latency
    Fastest Input → output
    Text and images → text Reliable knowledge cutoff
    Jun 2026 Training data cutoff
    Jun 2026
### Availability [Status](https://platform.claude.com/docs/en/about-claude/model-deprecations)
    Active (latest) Released
    October 7, 2026 Retirement
    Not sooner than October 7, 2027 Platforms
    Claude API[Amazon Bedrock](https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock)[Claude Models on Google Cloud (Google managed)](https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/google-managed)[Microsoft Foundry](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry)[Claude Platform on AWS](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws)[Claude Models on Google Cloud (Anthropic managed)](https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/anthropic-managed)
## Good to know
  * Adaptive thinking is on by default. Control thinking depth with the [effort parameter](https://platform.claude.com/docs/en/build-with-claude/effort).
  * Omit `temperature`, `top_p`, and `top_k`.
  * On the [Message Batches API](https://platform.claude.com/docs/en/build-with-claude/batch-processing#extended-output-beta), Claude Haiku 5.5 supports up to 300k output tokens with the `output-300k-2026-03-24` beta header.
  * The minimum cacheable prompt length is 512 tokens. See [Prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching#cache-limitations).
  * Query limits and capabilities programmatically with the [Models API](https://platform.claude.com/docs/en/api/models/list).


## Resources

[Prompting Claude Haiku 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-haiku-5-5)
Behavioral differences and prompting patterns specific to Claude Haiku 5.5.

[Reduce latency](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-latency)
Choose a model and effort level, shape prompts, and stream output for faster responses.

[Adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/thinking)
Claude Haiku 5.5 determines when and how much to think. Steer depth with `effort`.

[Context windows](https://platform.claude.com/docs/en/build-with-claude/context-windows)
How the context window is counted and managed.
## Reference

[System prompt](https://platform.claude.com/docs/en/release-notes/system-prompts/claude-haiku-5-5)
The system prompt Claude Haiku 5.5 uses on claude.ai and the Claude apps.

[System card](https://www.anthropic.com/document/claude-haiku-5-5-system-card)
Safety evaluations and deployment decisions for Claude Haiku 5.5.
[Pricing](https://platform.claude.com/docs/en/about-claude/pricing)
Full price list, including batch discounts and prompt caching rates.
[Model IDs and versioning](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions)
How model IDs, aliases, and pinned snapshots work.

[Model deprecations](https://platform.claude.com/docs/en/about-claude/model-deprecations)
Lifecycle status and retirement commitments for every Claude model.
Was this page helpful?

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

