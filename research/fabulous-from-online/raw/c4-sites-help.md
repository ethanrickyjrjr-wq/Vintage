[![OpenAI](https://help.openai.com/logo.png)](https://help.openai.com/en)
LanguageEnglish
[Login](https://help.openai.com/auth/login?redirectTo=%2Fauth%2Flogin-success%3FreturnTo%3D%252Fen%252Farticles%252F20001339-creating-and-using-chatgpt-sites)
  1. [All Collections](https://help.openai.com/en)
  2. [ChatGPT Sites](https://help.openai.com/en/collections/20001370-chatgpt-sites)
  3. Creating and using ChatGPT Sites


# Creating and using ChatGPT Sites
Create, edit, publish, share, and manage Sites in ChatGPT.
Updated: yesterday
# Overview
ChatGPT Sites lets you create, preview, publish, and share interactive websites and lightweight apps. You can create Sites on ChatGPT web and in the ChatGPT desktop app.
You can build issue dashboards, document finders, and other Sites that use visitors’ connected apps. Each visitor uses their own connected accounts and existing permissions.  
  
To use Sites, ask ChatGPT to build a website and describe what you want it to do. You can also use **@Sites** in your prompt.
## Availability
ChatGPT Sites is available to ChatGPT Plus and Pro accounts, as well as Business and Enterprise workspaces. Workspace settings and role permissions determine who can use Sites. In Enterprise workspaces, public publishing is off by default and must be enabled by an admin.  
  
If you don’t see Sites in a managed workspace, ask your workspace admin to check your access.
For workspace access and publishing controls, see: [_Managing ChatGPT Sites for your workspace_](https://help.openai.com/articles/20001338).
## Usage and limits
### Building and editing
Building or editing a Site counts toward your Codex usage. Usage for running and hosting Sites, including traffic and storage, is separate.
### Enterprise hosting
Charges for running and hosting Sites are currently waived for Enterprise workspaces. Building or editing a Site still counts toward Codex usage. Usage and storage limits still apply.
### Shared limits
If you use ChatGPT Plus or Pro, there’s no fixed limit on the number of Sites you can create. Usage and storage limits still apply across your Sites.
If you reach a shared limit, you may be unable to create a new Site, even if it won’t use storage. Check the limit message in Sites.
### Storage limits
Each Site’s database can store up to 10 GB. File storage has no fixed storage limit per Site.
For Codex usage and plan details, see: [_Using Codex with your ChatGPT plan_](https://help.openai.com/articles/11369540).
# Create a Site
Describe what you want to build, then review and refine a private preview before publishing.
## Create a Site on web or the ChatGPT desktop app
  1. On web, select **Work**. In the desktop app, select **ChatGPT** and then **Work** , or select **Codex**.
  2. In the chat window, describe the website you want ChatGPT to build. Include the word “website” in your prompt, or mention **@Sites**.
  3. Add the content, files, data, links, and constraints ChatGPT should use.
  4. Review the preview ChatGPT generates.
  5. Ask ChatGPT for changes until the Site looks and works the way you want.
  6. Deploy your Site to generate its URL. New Sites are private by default. Workspace admins may also have access.
  7. Open the Site and review its content and full URL. When you’re ready, choose who can access it in **Share** , then save your changes.


When you first deploy your Site, ChatGPT provides a default URL that can include a name for the Site and your username or workspace name. For personal accounts, Sites uses a randomly generated identifier by default instead of your username when creating a new default URL.
If you choose to [_make your profile public_](https://help.openai.com/articles/20001539) or change your username, Sites may use your username in the URL.
Publishing to others makes the current version of your Site available at that URL to the audience you’ve selected. 
Deploying changes to an existing Site updates its live version. To review changes without updating the live Site, save a version first and deploy only after you have reviewed it.
## Choose what to build
Examples include:
  * Turning a presentation into an interactive pitch.
  * Turning a data export you have permission to use into a business performance dashboard.
  * Turning team resources into a customer support app or employee learning hub.


Use content you have permission to share, and choose an audience that matches the content.
### Try a resource-hub prompt
“Use @Sites to build a searchable resource hub from the materials I provide. Add filters and a short description of when to use each resource. Use only supplied materials, ask me about missing details, and show a clear message when nothing matches. Keep links to the original resources. Save a version for review before publishing.”
For more on creating a Site, including prompts, versions, access, and best practices, see: [ChatGPT Sites developer guide](https://developers.openai.com/codex/sites).
## Build a Site with connected apps
Use connected apps to build a tool for a recurring task, such as tracking assigned issues or finding project documents.
Before you begin, confirm that connected-app access is available in your workspace and that you’ve connected the apps you want to use. Your workspace admin can review **Allow site visitors to use this plugin** for each required plugin.
  1. Describe the tool you want to build, the connected apps it should use, and the information it should show. If you’re unsure which apps to use, ask ChatGPT which available apps could help.
  2. Review the preview with your data. ChatGPT uses your available connections while building and previewing the Site. Ask for changes until the Site is ready to share.
  3. Publish the Site privately for your workspace, then share the link with a teammate.
  4. Ask your teammate to sign in, review the requested access, and choose their own connected account. Test that the Site shows the information they expect before sharing it more widely within the workspace.


Examples include: “Build a Site using my connected issue tracker that shows issues assigned to me, grouped by priority. Add project filters and links to the original issues.”
Each visitor uses their own connected accounts and existing permissions. Review the requested app access before you authorize it.
## Connect a Site to a service on your private network through a tunnel
Tunnels are rolling out to eligible workspaces. They let a Site connect to a service on your company’s private network, such as an internal inventory API, without making the service public.
Your IT team runs OpenAI’s tunnel client, a small program that passes requests and responses between the Site and the service.
Connect only to services your organization allows the Site to use, and limit access to the actions it needs. The service’s own authentication and access controls still apply.
For tunnel setup, permissions, and troubleshooting, see: [_Connecting ChatGPT Sites to private services with tunnels_](https://help.openai.com/articles/20001606).
## Use a custom domain
Where custom domains are available, Site owners can connect a domain they control to a Site, including a workspace Site. Sites does not register a domain for you. You must already own the domain and be able to change its DNS records.  
  
To connect a custom domain:
  1. Open the Site's settings and select **Add domain**.
  2. Enter the apex domain or subdomain you want to use.
  3. Copy the DNS records and values Sites provides, and add them through your domain provider.
  4. Wait a few minutes, then refresh the domain status in Sites.


You can also ask ChatGPT to help point the domain at your Site. If browsing or computer use is enabled, ChatGPT can help you navigate the domain provider after you sign in.
### A custom domain stays pending
These checks apply when custom-domain controls are available in your Site’s settings. If a Site you own works at its chatgpt.site address but its custom domain stays pending and returns a 404, compare the DNS records with the current instructions in Sites, including the verification TXT record. Allow time for any DNS changes to take effect, then refresh the domain status.
If the required DNS records are correct and have taken effect but the domain is still pending, try removing only that custom domain from the Site’s settings and adding the same hostname again. Check the new DNS instructions: the verification value may have changed. Update only the required records. Once any DNS changes have taken effect, refresh the status and test the custom domain again.
## Use a Site to host a plugin
A Site can host an MCP server that gives ChatGPT tools to use through a plugin. This lets you use the Site’s workflow from a ChatGPT conversation.
Ask ChatGPT or Codex to add an MCP server to a new or existing Site. Explain what information its tools should read and whether they should be able to make changes.
Review access to the Site, the plugin, and the connected service. Their permissions still apply.
For plugin hosting, see: [Hosting a plugin with ChatGPT Sites](https://help.openai.com/articles/20001547).
For plugin creation and installation, see: [Plugins in ChatGPT and Codex](https://help.openai.com/articles/20001256).
# Edit a Site
## On web or on the desktop app
  1. Open the chat where the Site was created, or select **Sites** in the sidebar, locate the Site, and select the edit icon.
  2. The chat opens with a reference to the Site.
  3. Describe the change you want, such as changing copy, layout, data, styles, links, forms, or interactive behavior.
  4. Review the updated preview.
  5. Ask ChatGPT for any follow-up changes.
  6. Publish the updated version only after you have reviewed it.


## Edit from your published Site
When the editing controls are available, you can start an edit from your published Site in a desktop browser. You must be signed in as the Site owner or an editor.
  1. Open the published Site.
  2. Select **Edit site**.
  3. Describe the changes you want in **Describe your edits**.
  4. Select **Send edits** to continue in ChatGPT with the Site and your instructions.
  5. Review the updated preview, then publish the changes when they’re ready.


Sending instructions from the Site starts the editing workflow. It does not immediately change the published Site.
## Review versions and saved data
Publishing can change the Site’s database before the new version goes live. If publishing fails, some database changes may already have been saved. Check the database before trying again.
Restoring an earlier version restores the code, not your database or uploaded files. Review any database migrations before publishing.
## Update secrets and environment variables
On Sites that use regional hosting, changes to existing secret values can affect the live Site without publishing again. Adding or removing keys from the Site’s configuration still requires publishing.
Other Sites apply saved environment-variable changes when you publish.
# Edit a Site with collaborators
A Site owner can give an active member of the same ChatGPT workspace **Can edit** access. An editor can update and save the shared Site. After the owner publishes the Site for the first time, an editor can publish later versions to the same Site URL.
## Give someone edit access
  1. Open the Site and select **Share**.
  2. Under **Who has access** , add or select an active member of the same workspace.
  3. Change their access to **Can edit**.


The editor can open **Sites** and select **Shared with you** to find the Site. They can then open the Site, make changes, review the updated preview, and save a version. After the owner completes the first publish, the editor can publish later versions.
From the Site’s settings, the owner manages access, the Site name and URL, and settings such as secrets and custom domains.
Give edit access only to trusted collaborators. Editors can inspect the live database and publish code that uses the Site’s secrets and storage. After the owner’s first publish, they can publish updates without a separate owner-approval step.
## Change or remove edit access
  1. Open the Site and select **Share**.
  2. Under **Who has access** , find the editor.
  3. Change their access to **Can view** , or remove them.


Changing or removing edit access stops the person from editing the Site. Whether they can still view it depends on the Site’s remaining audience settings.  
  
If **Can edit** or **Shared with you** is missing, co-editing may not be available for your account yet. Ask your workspace owner or admin to check that Sites is enabled for your account.
## Transfer Site ownership
The Site owner can transfer ownership to another active member of the same workspace and remain an editor. Workspace owners and admins can also transfer ownership.
## Change a Site’s URL
When you change a Site’s URL, the previous URL redirects to the new one as long as the workspace keeps the same address. This does not cover changes to the workspace address or a custom domain.
### Change the account name in personal Site addresses
Updating your ChatGPT username can also update the account name in all your personal Site addresses.
  1. Open **Settings** in ChatGPT.
  2. Select **Account**.
  3. Select **Username** , then enter and save your new username.


Choose a username you’re comfortable including in a Site address, and review your Site addresses before sharing them.
# Review, share, and publish a Site
After creating a Site, open its preview and use the sharing controls available to your account. A new Site is limited to its owner and workspace admins until access is changed. Available access options depend on your plan and workspace settings.
## Check your Site’s address before making it public
  1. On ChatGPT web, open **Sites**.
  2. Find the Site and open its more options menu (•••).
  3. Select **Open site** and review the full address in your browser.


Opening a private Site to check its address doesn’t make it public. Review the audience in **Share** before changing access.
## Share a Site on web or the ChatGPT desktop app
  1. Review the Site preview and check that it does not include information or content you do not want to share. You can also open **Sites** from the sidebar and locate the Site you want to share.
  2. Select **Share**.
  3. Under **Who has access** , choose one of the available options:


  * Owner and workspace admins
  * Selected active users or groups, and named external viewers (see section below).
  * Anyone in the workspace, where supported
  * Anyone on the internet, only when public publishing is enabled


  1. Available sharing options and sign-in requirements depend on your account and workspace. Review the selected audience before publishing.
  2. If you choose Anyone on the Internet, the Site will be publicly accessible. Carefully review your Site before proceeding.
  3. Select **Save**.
  4. After the site is live, use **Visit** to open it or **Copy link** to share the URL.


### If you cannot find workspace members
If your Enterprise workspace uses role-based permissions and you cannot find workspace members in a Site’s sharing dialog, ask your workspace owner or admin to check **View workspace members and groups** in **Workspace settings > Permissions & roles** for your assigned role. If your organization allows that access, the admin can enable it. Refresh ChatGPT, then try sharing again.
## Share with someone outside your workspace
A Site owner can invite someone outside the workspace to view a Site. The viewer must sign in with the ChatGPT account that received access. The invitation doesn’t let them edit the Site or make it public.
  1. Open the Site and select **Share**.
  2. Use the available people or email control to enter the email address for the person you want to invite.
  3. Review the recipient and their view-only access, then save the sharing change.
  4. Confirm that the person appears in the Site's access list. Ask them to open the Site while signed in with the account that received access.


In Enterprise workspaces, you need permission to invite external viewers. If you can’t enter an external email address or an invitation is rejected, ask your workspace owner or admin to check your permission. Availability can also depend on the rollout and where you use Sites.
For administrator checks, see: [Managing ChatGPT Sites for your workspace](https://help.openai.com/articles/20001338).
To remove an external viewer:
  1. Remove the person in the Site’s sharing controls.
  2. Check whether another audience setting still gives them access, such as public or workspace-wide access.
  3. Test that the Site is accessible only to the intended audience.


External viewers can’t edit or publish the Site. Sharing a Site doesn’t give them access to other workspace content or change the permissions required by services the Site uses.
# Schedule updates to a Site
When Site automations are available, you can create a cloud schedule for recurring work on a published Site. To link a schedule, you must own both the Site and the schedule.
  1. Open your Site’s **Automations**.
  2. Select **Create schedule**.
  3. Review the task instructions and timing.
  4. Confirm the schedule.


You can add more than one schedule to a Site. Site schedules run in the cloud, including schedules created on desktop.
ChatGPT may also suggest **Set up scheduled task** while you’re working on a Site. Review the instructions and timing before confirming. A suggestion does not create a schedule on its own.
## Manage a Site’s schedules
Open the Site’s **Automations** to find its linked schedules. Open a schedule in **Scheduled** to edit it, pause it, or resume it.
A scheduled task can’t use app access that a visitor approved while using the Site. Before you schedule a task, check that it can access the database or other supported data connection it needs when it runs in the cloud.
# Take down a Site
## On web or on the ChatGPT desktop app
  1. Open **Sites** from the sidebar.
  2. Use **Share settings** to restrict access to selected people or just yourself.
  3. If you want to permanently delete the Site, select **Delete site** and follow the instructions in the prompt.
  4. Confirm that the Site is no longer available to the previous audience.


Note: Deleting a site permanently removes it, and you cannot restore deleted sites. To confirm deletion, type the Site slug in the dialog, then select **Permanently delete**.
# Understand sign-in on Sites
The Site’s sharing settings control who can open it. If you add a sign-in feature inside the Site, that feature has its own controls. Before publishing, test the Site as an intended visitor and confirm that access matches your audience.
To limit sharing, invite supported users or groups through the Site’s sharing controls. Invited visitors must sign in with the account that received access.
Anyone can open a public Site without signing in to ChatGPT. The Site may still have its own sign-in feature.
Before you share or publish a Site, review its content, access setting, forms, sign-in behavior, files, links, and interactive features. Remove or change anything that should not be available to the intended audience.
If your Site uses Sign in with ChatGPT, explain what visitor information the Site receives and how it uses that information. You are responsible for complying with applicable privacy and data-protection laws.
## Use your connected apps in a Site
In supported workspaces, a Site can use each visitor’s own connected apps. For example, a shared dashboard can show information from your account, using your existing app permissions.
Before you approve access, check that:
  * The Site is private to your workspace.
  * You belong to that workspace.
  * Your admins allow connected-app access for Sites.


Being invited to view a Site, including as an external viewer, doesn’t by itself give you connected-app access.
When the Site requests access:
  1. Sign in with the ChatGPT account you want to use.
  2. Review which data and actions the Site requests.
  3. Choose the connected account and access you want to allow, then return to the Site.


The Site can use the data and actions you approve, within your existing app permissions. If **Read and write** is offered, approve it only if you want the Site to make changes in that app.
Sharing the Site doesn’t let other visitors use your connected accounts. Your approval also doesn’t give background scheduled tasks access to your connected apps.
You can continue without approving app access, but features that need it won’t work.
If the Site can’t use an app:
  * Check that you’re using the correct account and have connected the app.
  * Ask your workspace admin to check **Allow site visitors to use this plugin** for the app’s plugin.
  * If your workspace belongs to a tenant, ask a tenant admin whether connected-app access for Sites needs to be enabled.


For administrator checks, see: [_Managing ChatGPT Sites for your workspace_](https://help.openai.com/articles/20001338).
# What to check before you share or publish
Before you share or publish a ChatGPT Site, check that it does not include confidential or sensitive data, or third-party content unless you have the right to share it.  
  
Make sure:
  * The Site behaves the way you expect when opened by another user.
  * The access setting matches your intended audience.
  * If you plan to publish publicly, check that your workspace admin allows it.
  * You have reviewed any content, generated text or images, links, uploaded files, forms, and interactive behavior the Site includes.


Review any features that let visitors provide personal information or other content, such as open-text fields, message boards, or sign-in functionality. Consider whether you want these features in your Site and whether you want to collect, share, or publish that information.
For more information about your obligations when collecting and processing personal data from others through a public Site, see: [_Complying with data protection laws for ChatGPT Sites_](https://help.openai.com/articles/20001340).
Test the features your Site includes:
  * If your Site has required fields, try leaving them blank or entering invalid information. Check that the Site explains what needs correcting.
  * Try searches or filters with no matches. Check that the Site shows a clear message when nothing matches.
  * Check that resource links are current and that a colleague can open the original files using their own account.
  * If your Site is designed to save records, submit a sample entry and reload to check that it remains. Use another authorized account to check that it can view only the intended records.


# Limits and unsupported uses
Sites is designed for web experiences that can be hosted through the supported Sites runtime. Available capabilities depend on your account and workspace.
Supported capabilities depend on the Sites runtime and the features available to your account. Some frameworks, private networks, databases, background services, and hosting patterns may not be supported.
A tunnel provides a connection to a private service. The service’s own access controls still determine what the Site can do.
For tunnel setup and permissions, see: [_Connecting ChatGPT Sites to private services with tunnels_](https://help.openai.com/articles/20001606).
Sites must not process sensitive data such as Protected Health Information or payment-card data (unless solely through a third-party payment processor); target children under 13 or the applicable age of digital consent; distribute malware; enable phishing; impersonate people or organizations; or otherwise violate the OpenAI Usage Policies or ChatGPT Sites Terms.
If you want to sell goods or services or collect payments through your ChatGPT Site, you can do so by using a third-party payment processor. Please note that you are responsible for connecting, configuring, and maintaining any third-party payment processors you choose to use on your ChatGPT Site, and we are not responsible for payments processed through those providers. You are also responsible for any e-commerce activities and transactions with your users, including fulfillment, delivery, refunds, customer support, and any claims or warranties relating to what you sell, as well as for calculating, collecting, and remitting any related taxes and fees.
# FAQ
## Is Sites hosting included with ChatGPT Plus and Pro?
Yes. Sites hosting is currently included with ChatGPT Plus and Pro. There is no fixed limit on the number of Sites you can create. Building or editing a Site counts toward your Codex usage.
## Are Enterprise workspaces charged for Sites hosting?
Charges for running and hosting Sites are currently waived for Enterprise workspaces. Building or editing a Site still counts toward Codex usage. Usage and storage limits still apply.
## How will Enterprise Sites hosting be billed when charges apply?
When hosting charges apply, your workspace’s agreement determines whether Sites usage is billed in credits or dollars. Contact your OpenAI account team to confirm your workspace’s terms.
## Why can’t I use ChatGPT Sites?
Confirm that Sites is available for your plan and that you are signed in to the correct account or workspace. Sites is not available on Free or Go. In Enterprise, ask an admin whether Sites is enabled for your role.
Use **Work** on ChatGPT web, or **Work** or **Codex** in the ChatGPT desktop app. Sites is not available in the ChatGPT Classic app. Make sure you’re using the latest [ChatGPT desktop app](https://chatgpt.com/download/).
## I’m in an Enterprise workspace. Why can’t I publish a ChatGPT Site I created to the public?
In Enterprise workspaces, public publishing is off by default. An admin must enable public publishing and grant the appropriate role access before members can publish publicly.
## Why can’t I access a ChatGPT Site?
A Site must be shared with you, available to your workspace, or published publicly before you can access it. You may need to sign in to the account or workspace that has access, when prompted.
## Why was my site taken down?
OpenAI may remove or restrict a Site if there is a risk that it violates OpenAI policies or platform safety requirements. If you believe your Site was removed in error, please submit an appeal using the link in the email notification you received. This helps us route your request correctly and review it more efficiently.  
  
If you can’t access that email, you can submit an appeal through our intake [form](https://openai.com/form/appeal/).  
  
Your organization may also restrict access to Sites. Contact your workspace owner or admin to check whether a workspace policy or review is affecting access.
## How do I report or request takedown of a ChatGPT Site?
If you believe a Site violates OpenAI policies, report it using the [content reporting form](https://help.openai.com/articles/10245791). Include the full Site URL and enough detail to identify the issue.
## What information does a Site use?
Depending on how you create and publish a Site, Sites can include information from ChatGPT prompts, instructions, conversation context, uploaded or referenced files, site code, generated artifacts, hosted URLs, access settings, storage, metadata, logs, and operational data needed to host, secure, debug, or enforce policy on the Site.
## Does OpenAI use information from ChatGPT Sites to train its models?
The following information applies to your conversations with ChatGPT, including conversations where you create, design, or edit a Site or ask ChatGPT to retrieve information from one.
For ChatGPT Business and Enterprise/Edu customers: OpenAI does not use these conversations or the Site information included in them to train its models by default.
For ChatGPT Free, Go, Plus, and Pro users: OpenAI may use your conversations with ChatGPT to train our models if your “Improve the model for everyone” setting is on, which includes conversations where you use ChatGPT to create, design, edit, or manage a Site. For example, if you ask ChatGPT to edit a published Site or retrieve information from it, ChatGPT may bring relevant information from the Site into your conversation to help complete your request. You should only ask ChatGPT to use information that you have permission to provide. For more information about how your data is stored and used, see: [Data Controls FAQ](https://help.openai.com/articles/7730893).
## What should I check if a Site fails to save or publish?
Identify where the problem occurs: opening a preview, saving a version, publishing, or opening the published Site. Saving a version and publishing are separate steps.
In a workspace, ask your admin to check that Sites is enabled for your role and that you have permission for the intended audience. Public publishing requires separate permission.
If the problem continues, [contact OpenAI Support](https://help.openai.com/articles/6614161). Include the Site URL if available, the exact error or approval message, the step that failed, your account or workspace, the app or browser version, and the time of the error with its time zone.
## Was this article helpful?
Submit
  * [Overview](https://help.openai.com/en/articles/20001339-creating-and-using-chatgpt-sites#overview)
  * [Availability](https://help.openai.com/en/articles/20001339-creating-and-using-chatgpt-sites#availability)
  * [Usage and limits](https://help.openai.com/en/articles/20001339-creating-and-using-chatgpt-sites#usage-and-limits)
  * [Building and editing](https://help.openai.com/en/articles/20001339-creating-and-using-chatgpt-sites#building-and-editing)
  * [Enterprise hosting](https://help.openai.com/en/articles/20001339-creating-and-using-chatgpt-sites#enterprise-hosting)
  * [Shared limits](https://help.openai.com/en/articles/20001339-creating-and-using-chatgpt-sites#shared-limits)
  * [Storage limits](https://help.openai.com/en/articles/20001339-creating-and-using-chatgpt-sites#storage-limits)
  * [Create a Site](https://help.openai.com/en/articles/20001339-creating-and-using-chatgpt-sites#create-a-site)
  * [Create a Site on web or the ChatGPT desktop app](https://help.openai.com/en/articles/20001339-creating-and-using-chatgpt-sites#create-a-site-on-web-or-the-chatgpt-desktop-app)
  * [Choose what to build](https://help.openai.com/en/articles/20001339-creating-and-using-chatgpt-sites#choose-what-to-build)
  * [Try a resource-hub prompt](https://help.openai.com/en/articles/20001339-creating-and-using-chatgpt-sites#try-a-resource-hub-prompt)
  * [Build a Site with connected apps](https://help.openai.com/en/articles/20001339-creating-and-using-chatgpt-sites#build-a-site-with-connected-apps)
  * [Connect a Site to a service on your private network through a tunnel](https://help.openai.com/en/articles/20001339-creating-and-using-chatgpt-sites#connect-a-site-to-a-service-on-your-private-network-through-a-tunnel)
  * [Use a custom domain](https://help.openai.com/en/articles/20001339-creating-and-using-chatgpt-sites#use-a-custom-domain)
  * [A custom domain stays pending](https://help.openai.com/en/articles/20001339-creating-and-using-chatgpt-sites#a-custom-domain-stays-pending)
  * [Use a Site to host a plugin](https://help.openai.com/en/articles/20001339-creating-and-using-chatgpt-sites#use-a-site-to-host-a-plugin)
  * [Edit a Site](https://help.openai.com/en/articles/20001339-creating-and-using-chatgpt-sites#edit-a-site)
  * [On web or on the desktop app](https://help.openai.com/en/articles/20001339-creating-and-using-chatgpt-sites#on-web-or-on-the-desktop-app)
  * [Edit from your published Site](https://help.openai.com/en/articles/20001339-creating-and-using-chatgpt-sites#edit-from-your-published-site)
  * [Review versions and saved data](https://help.openai.com/en/articles/20001339-creating-and-using-chatgpt-sites#review-versions-and-saved-data)
  * [Update secrets and environment variables](https://help.openai.com/en/articles/20001339-creating-and-using-chatgpt-sites#update-secrets-and-environment-variables)
  * [Edit a Site with collaborators](https://help.openai.com/en/articles/20001339-creating-and-using-chatgpt-sites#edit-a-site-with-collaborators)
  * [Give someone edit access](https://help.openai.com/en/articles/20001339-creating-and-using-chatgpt-sites#give-someone-edit-access)
  * [Change or remove edit access](https://help.openai.com/en/articles/20001339-creating-and-using-chatgpt-sites#change-or-remove-edit-access)
  * [Transfer Site ownership](https://help.openai.com/en/articles/20001339-creating-and-using-chatgpt-sites#transfer-site-ownership)
  * [Change a Site’s URL](https://help.openai.com/en/articles/20001339-creating-and-using-chatgpt-sites#change-a-sites-url)
  * [Change the account name in personal Site addresses](https://help.openai.com/en/articles/20001339-creating-and-using-chatgpt-sites#change-the-account-name-in-personal-site-addresses)
  * [Review, share, and publish a Site](https://help.openai.com/en/articles/20001339-creating-and-using-chatgpt-sites#review-share-and-publish-a-site)
  * [Check your Site’s address before making it public](https://help.openai.com/en/articles/20001339-creating-and-using-chatgpt-sites#check-your-sites-address-before-making-it-public)
  * [Share a Site on web or the ChatGPT desktop app](https://help.openai.com/en/articles/20001339-creating-and-using-chatgpt-sites#share-a-site-on-web-or-the-chatgpt-desktop-app)
  * [If you cannot find workspace members](https://help.openai.com/en/articles/20001339-creating-and-using-chatgpt-sites#if-you-cannot-find-workspace-members)
  * [Share with someone outside your workspace](https://help.openai.com/en/articles/20001339-creating-and-using-chatgpt-sites#share-with-someone-outside-your-workspace)
  * [Schedule updates to a Site](https://help.openai.com/en/articles/20001339-creating-and-using-chatgpt-sites#schedule-updates-to-a-site)
  * [Manage a Site’s schedules](https://help.openai.com/en/articles/20001339-creating-and-using-chatgpt-sites#manage-a-sites-schedules)
  * [Take down a Site](https://help.openai.com/en/articles/20001339-creating-and-using-chatgpt-sites#take-down-a-site)
  * [On web or on the ChatGPT desktop app](https://help.openai.com/en/articles/20001339-creating-and-using-chatgpt-sites#on-web-or-on-the-chatgpt-desktop-app)
  * [Understand sign-in on Sites](https://help.openai.com/en/articles/20001339-creating-and-using-chatgpt-sites#understand-sign-in-on-sites)
  * [Use your connected apps in a Site](https://help.openai.com/en/articles/20001339-creating-and-using-chatgpt-sites#use-your-connected-apps-in-a-site)
  * [What to check before you share or publish](https://help.openai.com/en/articles/20001339-creating-and-using-chatgpt-sites#what-to-check-before-you-share-or-publish)
  * [Limits and unsupported uses](https://help.openai.com/en/articles/20001339-creating-and-using-chatgpt-sites#limits-and-unsupported-uses)
  * [FAQ](https://help.openai.com/en/articles/20001339-creating-and-using-chatgpt-sites#faq)
  * [Is Sites hosting included with ChatGPT Plus and Pro?](https://help.openai.com/en/articles/20001339-creating-and-using-chatgpt-sites#is-sites-hosting-included-with-chatgpt-plus-and-pro)
  * [Are Enterprise workspaces charged for Sites hosting?](https://help.openai.com/en/articles/20001339-creating-and-using-chatgpt-sites#are-enterprise-workspaces-charged-for-sites-hosting)
  * [How will Enterprise Sites hosting be billed when charges apply?](https://help.openai.com/en/articles/20001339-creating-and-using-chatgpt-sites#how-will-enterprise-sites-hosting-be-billed-when-charges-apply)
  * [Why can’t I use ChatGPT Sites?](https://help.openai.com/en/articles/20001339-creating-and-using-chatgpt-sites#why-cant-i-use-chatgpt-sites)
  * [I’m in an Enterprise workspace. Why can’t I publish a ChatGPT Site I created to the public?](https://help.openai.com/en/articles/20001339-creating-and-using-chatgpt-sites#im-in-an-enterprise-workspace-why-cant-i-publish-a-chatgpt-site-i-created-to-the-public)
  * [Why can’t I access a ChatGPT Site?](https://help.openai.com/en/articles/20001339-creating-and-using-chatgpt-sites#why-cant-i-access-a-chatgpt-site)
  * [Why was my site taken down?](https://help.openai.com/en/articles/20001339-creating-and-using-chatgpt-sites#why-was-my-site-taken-down)
  * [How do I report or request takedown of a ChatGPT Site?](https://help.openai.com/en/articles/20001339-creating-and-using-chatgpt-sites#how-do-i-report-or-request-takedown-of-a-chatgpt-site)
  * [What information does a Site use?](https://help.openai.com/en/articles/20001339-creating-and-using-chatgpt-sites#what-information-does-a-site-use)
  * [Does OpenAI use information from ChatGPT Sites to train its models?](https://help.openai.com/en/articles/20001339-creating-and-using-chatgpt-sites#does-openai-use-information-from-chatgpt-sites-to-train-its-models)
  * [What should I check if a Site fails to save or publish?](https://help.openai.com/en/articles/20001339-creating-and-using-chatgpt-sites#what-should-i-check-if-a-site-fails-to-save-or-publish)


![OpenAI logo](https://help.openai.com/favicon.png)[ChatGPT](https://chatgpt.com)[API](https://platform.openai.com/docs/)[Service Status](https://status.openai.com)Cookie Preferences

