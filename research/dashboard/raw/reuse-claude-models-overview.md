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
[Console](https://platform.claude.com/)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fmodels%2Foverview)

Search`Ctrl``K`
Models
[Models overview](https://platform.claude.com/docs/en/models/overview)
[Claude Fable 5.1](https://platform.claude.com/docs/en/models/fable-5-1/overview)
[Claude Opus 5.5](https://platform.claude.com/docs/en/models/opus-5-5/overview)
[Claude Sonnet 5.5](https://platform.claude.com/docs/en/models/sonnet-5-5/overview)
[Claude Haiku 5.5](https://platform.claude.com/docs/en/models/haiku-5-5/overview)
Specialized models
Legacy models
Guides
[Choosing a model](https://platform.claude.com/docs/en/about-claude/models/choosing-a-model)[Optimizing for cost and intelligence](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence)[Upgrade between model versions](https://platform.claude.com/docs/en/about-claude/models/migration-guide)
Lifecycle and reference
[Model IDs and versioning](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions)[Model deprecations](https://platform.claude.com/docs/en/about-claude/model-deprecations)[Model cards](https://platform.claude.com/docs/en/resources/overview)[Pricing](https://platform.claude.com/docs/en/about-claude/pricing)[API credits for subscribers](https://platform.claude.com/docs/en/about-claude/api-credits-for-subscribers)
[System prompts](https://platform.claude.com/docs/en/release-notes/system-prompts/overview)
[Console](https://platform.claude.com/)
Models & pricingModels
# Models overview
Copy page

Claude is a family of state-of-the-art large language models developed by Anthropic. Compare the current lineup, find the model ID for every platform, and open each model's page for its full specs and resources.
[Choosing a model](https://platform.claude.com/docs/en/about-claude/models/choosing-a-model)[Pricing](https://platform.claude.com/docs/en/about-claude/pricing)[Migration guide](https://platform.claude.com/docs/en/about-claude/models/migration-guide)
Copy page

## Compare models
If you're unsure which model to use, start with [Claude Opus 5.5](https://platform.claude.com/docs/en/models/opus-5-5/overview) for most workloads. Use [Claude Fable 5.1](https://platform.claude.com/docs/en/models/fable-5-1/overview) for demanding reasoning and long-horizon agentic work, or when your evals on Claude Opus 5.5 at higher effort still fall short. All current models support text and image input, text output, multilingual capabilities, vision, and tool use. Each model's page lists the platforms it's available on.  
| Feature  | ![](https://platform.claude.com/images/dashboard-discovery/head.svg?dpl=0a82b0fca8e491f3681e1bfdb6f80293938b929b-dc8ad335) [Claude Fable 5.1](https://platform.claude.com/docs/en/models/fable-5-1/overview)For demanding reasoning and long-horizon agentic work  | ![](https://platform.claude.com/images/dashboard-discovery/cursor.svg?dpl=0a82b0fca8e491f3681e1bfdb6f80293938b929b-dc8ad335) [Claude Opus 5.5](https://platform.claude.com/docs/en/models/opus-5-5/overview)For long-running agentic coding and knowledge work  | ![](https://platform.claude.com/images/dashboard-discovery/bubble.svg?dpl=0a82b0fca8e491f3681e1bfdb6f80293938b929b-dc8ad335) [Claude Sonnet 5.5](https://platform.claude.com/docs/en/models/sonnet-5-5/overview)The best combination of speed and intelligence  | ![](https://platform.claude.com/images/dashboard-discovery/bird.svg?dpl=0a82b0fca8e491f3681e1bfdb6f80293938b929b-dc8ad335) [Claude Haiku 5.5](https://platform.claude.com/docs/en/models/haiku-5-5/overview)For high-volume, latency-sensitive tasks such as classification, extraction, and routing  |  
| --- | --- | --- | --- | --- |  
| Comparative latency  | Slower  | Moderate  | Fast  | Fastest  |  
| Pricing  | $10 / input MTok$50 / output MTok  | $4 / input MTok$20 / output MTok  | $2 / input MTok$10 / output MTok  | From $0.10 / input MTokFrom $0.50 / output MTok  |  
| Claude API ID  | claude-fable-5-1  | claude-opus-5-5  | claude-sonnet-5-5  | claude-haiku-5-5  |  
| Capabilities  |   |  
| Thinking  | Adaptive (always on)  | Adaptive (always on)  | Adaptive  | Adaptive  |  
| Default effort  | `high`  | `medium`  | `high`  | `medium`  |  
| Context window  | 1M tokens  | 1M tokens  | 1M tokens  | 1M tokens  |  
| Max output  | 128K tokens  | 128K tokens  | 128K tokens  | 128K tokens  |  
| Reliable knowledge cutoff  | Jun 2026  | Jun 2026  | Jun 2026  | Jun 2026  |  
| Additional details  |   |  
| Training data cutoff  | Jun 2026  | Jun 2026  | Jun 2026  | Jun 2026  |  
| Retirement  | Not sooner than September 1, 2027  | Not sooner than September 22, 2027  | Not sooner than September 28, 2027  | Not sooner than October 7, 2027  |  
| Model IDs  |   |  
| Claude API alias  | claude-fable-5-1  | claude-opus-5-5  | claude-sonnet-5-5  | claude-haiku-5-5  |  
| Amazon Bedrock ID  | anthropic.claude-fable-5-1  | anthropic.claude-opus-5-5  | anthropic.claude-sonnet-5-5  | anthropic.claude-haiku-5-5  |  
| Claude Models on Google Cloud (Google managed) ID  | claude-fable-5-1  | claude-opus-5-5  | claude-sonnet-5-5  | claude-haiku-5-5  |  
| Microsoft Foundry ID  | claude-fable-5-1  | claude-opus-5-5  | claude-sonnet-5-5  | claude-haiku-5-5  |  
| Claude Platform on AWS ID  | claude-fable-5-1  | claude-opus-5-5  | claude-sonnet-5-5  | claude-haiku-5-5  |  
| [Claude Models on Google Cloud (Anthropic managed) ID](https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/anthropic-managed)  | claude-fable-5-1  | claude-opus-5-5  | claude-sonnet-5-5  | claude-haiku-5-5  |  
Once you've picked a model, [learn how to make your first API call](https://platform.claude.com/docs/en/get-started). To understand how model IDs, aliases, and snapshots work, see [Model IDs and versioning](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions); for the reliable-knowledge and training-data cutoffs behind each model, see Anthropic's [Transparency Hub](https://www.anthropic.com/transparency).
## Using the Models API
You can query model capabilities and token limits programmatically with the [Models API](https://platform.claude.com/docs/en/api/models/list). The response includes `max_input_tokens`, `max_tokens`, and a `capabilities` object for every available model.
Each model in the response also has a `line` field, which names the model line it belongs to. Claude Opus 4.5 and Claude Opus 4.6 both report `opus`. Use `line` to group models, for example, in a model picker. `line` is `null` when a model belongs to no line. Read `line` instead of inferring it from the model's `id`. Anthropic might add more lines, so don't treat the set of values as fixed.
Each model's `capabilities` object includes `thinking.types.disabled`, which reports whether the model accepts `thinking: {type: "disabled"}`, the setting that [turns thinking off](https://platform.claude.com/docs/en/build-with-claude/thinking#turning-thinking-off). `supported` is `false` when the model rejects `"disabled"` with a 400 error, and `true` on a model that doesn't support thinking. Even when `supported` is `true`, the API can still reject a `"disabled"` request for another reason. One such reason is an [effort](https://platform.claude.com/docs/en/build-with-claude/effort) level that the model doesn't allow with thinking off.
Each model's `capabilities` object also includes `thinking.types.between_tools`, which reports whether the model accepts `thinking: {type: "between_tools"}`, the setting that [turns off up-front thinking](https://platform.claude.com/docs/en/build-with-claude/thinking#turning-thinking-off). `supported` is `false` when the model rejects `"between_tools"` with a 400 error. Even when `supported` is `true`, the API can still reject a `"between_tools"` request for another reason, such as an [effort](https://platform.claude.com/docs/en/build-with-claude/effort) level that the model doesn't allow with `"between_tools"`. For Claude Sonnet 5.5, for example, the Models API reports `thinking.types.between_tools.supported` as `true` and `thinking.types.disabled.supported` as `false`.
Each model's `capabilities` object also includes `server_tools`, which reports whether the model accepts the [web search](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool) and [code execution](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool) tools. It doesn't cover other server tools, such as web fetch. `server_tools.web_search.supported` and `server_tools.code_execution.supported` are `true` when the model accepts at least one version of that tool, not necessarily every version. `server_tools.supported` is `true` when the model accepts at least one of the two tools. Even when a tool is supported, your organization's settings can still cause a request that uses it to fail. For example, an administrator can [disable web search](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool#how-to-use-web-search).
The top-level `code_execution` capability is a different check. It reports whether code that Claude runs in the code execution tool can call the request's other tools, as in [programmatic tool calling](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling). For Claude Haiku 4.5, for example, the Models API reports `server_tools.code_execution.supported` as `true` and `code_execution.supported` as `false`.
## Prompt and output performance
Current Claude models excel in:
  * **Performance:** Top-tier results in reasoning, coding, multilingual tasks, long-context handling, honesty, and image processing. See [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices) for general and model-specific prompting guidance.
  * **Engaging responses:** Claude models are ideal for applications that require rich, human-like interactions. If you prefer more concise responses, adjust your prompts to guide the model toward the output length you want. Refer to the [prompt engineering guides](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering) for details.
  * **Output quality:** When migrating from a previous model generation, you might notice larger improvements in overall performance. If you're on Claude Opus 5 or earlier, see the [Claude Opus 5.5 migration guide](https://platform.claude.com/docs/en/models/opus-5-5/migration-guide).


## Get started with Claude
Whether you're a developer looking to integrate Claude into your applications or a user wanting to experience the power of AI firsthand, the following resources can help.

[Intro to Claude](https://platform.claude.com/docs/en/intro)
Explore Claude's capabilities and development flow.

[Quickstart](https://platform.claude.com/docs/en/get-started)
Learn how to make your first API call in minutes.
[Choosing a model](https://platform.claude.com/docs/en/about-claude/models/choosing-a-model)
Establish criteria and pick the right model for your use case.
[Pricing](https://platform.claude.com/docs/en/about-claude/pricing)
Complete pricing, including batch discounts and prompt caching rates.

[Model deprecations](https://platform.claude.com/docs/en/about-claude/model-deprecations)
Lifecycle status and retirement commitments for every model.

[Claude Console](https://platform.claude.com/)
Craft and test prompts directly in your browser.
Looking to chat with Claude? Visit [claude.ai](https://claude.ai). If you have questions, contact the [support team](https://support.claude.com/) or the [Discord community](https://www.anthropic.com/discord).
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

