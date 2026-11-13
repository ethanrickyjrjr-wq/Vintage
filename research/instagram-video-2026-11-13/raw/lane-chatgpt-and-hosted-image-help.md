Source: https://help.openai.com/en/articles/8554407-how-can-i-generate-images-with-chatgpt (fetched 2026-11-13 with crawl4ai)

[![OpenAI](https://help.openai.com/logo.png)](https://help.openai.com/en)
  1. [All Collections](https://help.openai.com/en)
  2. [ChatGPT](https://help.openai.com/en/collections/3742473-chatgpt)
  3. [GPTs](https://help.openai.com/en/collections/8475420-gpts)
  4. GPTs in ChatGPT


# GPTs in ChatGPT
Learn what GPTs are in ChatGPT, what they can include, who can use and build them, and how they interact with privacy, workspaces, and the GPT Store.
Updated: 10 days ago
We’re planning to retire custom GPTs and help creators move their workflows to [plugins](https://help.openai.com/articles/20001256). Plugins bring reusable instructions, reference files, and connected apps together.  
  
For affected Enterprise workspaces, new GPT creation ended on October 26, 2026. FedRAMP workspaces are excluded from this creation cutoff and can still create GPTs. Existing unmigrated GPTs remain usable and editable until their applicable retirement date. After migration, the original GPT becomes read-only. Standard retirement is scheduled for December 11, 2026. FedRAMP workspaces and workspaces with a qualifying, approved deferral have a retirement date of February 11, 2027.  
  
The transition includes all ChatGPT plans, but creation restrictions and migration access depend on the account or workspace. Follow the notice for yours. For dates, migration steps, and what to expect on other plans, see: [Custom GPT retirement and migration FAQ](https://help.openai.com/articles/20001519).
# Overview
GPTs (also called custom GPTs) are versions of ChatGPT configured for a specific purpose. A GPT can combine specific instructions, knowledge, and selected capabilities to create a more tailored experience in ChatGPT.
## Availability
GPTs are available to all ChatGPT users, but users must be signed in to start a conversation. Public GPT pages may be visible without signing in, but users are prompted to sign in before chatting.  
  
Once signed in, users can interact with any GPT they have access to, including GPTs that are public, shared with them directly, or available through workspace settings.  
  
  
**New GPT creation and publishing are not available on personal ChatGPT accounts, including Free, Go, Plus, and Pro.**
Existing GPTs remain available to use. Editing an existing GPT continues to require an eligible subscription and any applicable account or workspace permissions.
In Business, Enterprise, and Edu workspaces, GPT creation, editing, and publishing depend on product availability, workspace settings, and permissions.
New GPT creation ended on October 26, 2026 for affected Enterprise workspaces, with the exception of FedRAMP workspaces. Existing unmigrated GPTs remain usable and editable until their applicable retirement date. After migration, the original GPT becomes read-only. For dates and migration guidance, see: [Custom GPT retirement and migration FAQ](https://help.openai.com/articles/20001519).
# What a GPT can include
A GPT can include several configuration elements that shape how it behaves and what it can do.
  * **Instructions:** Define the GPT’s behavior, tone, goals, and boundaries.
  * **Conversation starters:** Provide example prompts to help users get started.
  * **Knowledge:** Uploaded files the GPT can use as reference when answering questions.
  * **Capabilities:** Selected tools or features, such as web search or image generation.
  * **Apps:** Ways a GPT can connect to outside services through user-connected tools.
  * **Actions:** Ways a GPT can connect to external APIs you define.


A GPT can use either apps or actions, but not both at the same time.
# Getting started
## Using a GPT
Users can access a GPT in several ways.
  * Open **Explore GPTs** in ChatGPT to browse available GPTs.
  * Use a direct link to a GPT.
  * Open a GPT that has been shared with them in their workspace.


After opening a GPT, users can review its description or conversation starters to understand what it is designed to do, then send a message to begin chatting. The GPT will respond based on its configured instructions, knowledge, and enabled capabilities.
## Creating a GPT in a managed workspace
If new GPT creation is available in your workspace and you have the required permissions, you can create a GPT:
  * Open the GPTs area in ChatGPT
  * Select **Create**.
  * GPTs can be built conversationally or configured directly in the editor.
  * After configuring a GPT, test it in preview and save changes.


**New GPT creation is not available on personal ChatGPT accounts, including Free, Go, Plus, and Pro.**
For step-by-step instructions on building, editing, testing, and updating a GPT, see: [Creating and editing GPTs](https://help.openai.com/articles/8554397).
For new reusable workflows after the creation cutoff, use Plugin Creator. For setup, see: [Plugins in ChatGPT](https://help.openai.com/articles/20001256).
## Sharing and publishing
GPT sharing options depend on your account, plan, and workspace settings. Personal ChatGPT accounts, including Free, Go, Plus, and Pro, cannot publish new GPTs.
In Business, Enterprise, and Edu workspaces, GPT sharing and publishing options continue to depend on workspace settings and permissions. Available options may include sharing with specific people, sharing within a workspace, sharing by link, or publishing to the GPT Store when permitted.
For step-by-step guidance on sharing options, public publishing requirements, Builder Profiles, and GPT Store publishing, see: [Sharing and publishing GPTs](https://help.openai.com/articles/8798878).
## Workspace controls (Enterprise and Edu)
GPT access and sharing may be limited by workspace settings and permissions. Admins or owners may control which GPTs users can access, what options appear in the GPT editor, and which sharing methods are available. For detailed information, see: [Managing GPT access in Enterprise and Edu workspaces](https://help.openai.com/articles/8555535).
## Troubleshooting and reporting issues
For information on common issues, how to troubleshoot them, and how to report content or other issues, see: [Troubleshooting GPTs](https://help.openai.com/articles/11325361).
# Privacy and data use
## Model training
Whether conversations with a GPT may be used to improve OpenAI’s models depends on the plan you are using.  
  
For Business, Enterprise, and Edu plans, data is not used for training by default.  
  
For consumer plans, including Free, Plus, Go, and Pro, data may be used for training depending on whether you have opted out. To opt out or learn more, see: [Data Controls FAQ](https://help.openai.com/articles/7730893).
## Conversation access
GPT builders **cannot view** individual conversations that users have with their GPTs.
## External APIs and apps
GPTs can be integrated with apps and external APIs. When you interact with a GPT that uses apps or external APIs, relevant parts of your input may be sent to the third-party service. Depending on the GPT's setup and the type of action, ChatGPT may ask you to approve the request before information is sent or the action runs. OpenAI does not audit or control how those services use or store your data. Only use GPTs with APIs or apps that you trust.
# FAQ
## Can I embed my GPT on my website?
GPTs are designed to work in ChatGPT. They are not a way to embed ChatGPT in an external website or application. To build an assistant into a product, use the API.
## What’s the difference between GPTs and assistants built with the API?
GPTs are no-code assistants built and used inside ChatGPT. Assistants built with the API are developer-built integrations that use OpenAI models inside a website or service outside of ChatGPT.
## Can I use a GPT from a regular ChatGPT conversation?
Yes. On ChatGPT web, you can type @ in a conversation to bring in a GPT without starting a new chat. Your next message will go to that GPT, and the conversation keeps its current context. This @-mention flow isn’t available in the iOS or Android apps. On mobile, open the GPT from the GPTs menu or sidebar instead.
## Do GPTs use memory or custom instructions?
GPTs do not use saved memory, custom instructions, or previous conversations. Each conversation starts fresh.
## What happens to my existing GPTs if I change or cancel my subscription?
You can continue using GPTs you previously created. Editing an existing GPT still depends on your subscription and permissions, so changing to a plan that does not support editing may prevent you from making changes.
New GPT creation is unavailable on personal ChatGPT accounts, regardless of subscription.
## Why don’t I see the same model options as before?
Models can be updated or retired over time. If a model is no longer available, GPTs are automatically switched to a similar current model.
## Was this article helpful?
Submit
![OpenAI logo](https://help.openai.com/favicon.png)[ChatGPT](https://chatgpt.com)[API](https://platform.openai.com/docs/)[Service Status](https://status.openai.com)Cookie Preferences

