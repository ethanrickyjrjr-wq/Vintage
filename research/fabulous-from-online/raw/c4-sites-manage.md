[![OpenAI](https://help.openai.com/logo.png)](https://help.openai.com/en)
  1. [All Collections](https://help.openai.com/en)
  2. [ChatGPT Sites](https://help.openai.com/en/collections/20001370-chatgpt-sites)
  3. Managing ChatGPT Sites for your workspace


# Managing ChatGPT Sites for your workspace
Manage Site creation, publishing, sharing, and connected-app access for your workspace.
Updated: 14 hours ago
# Overview
ChatGPT Sites lets workspace members create and share hosted Sites from ChatGPT. Workspace owners and admins can help determine who can create Sites, who can publish them, how Sites are shared, and how Sites should be reviewed or removed when needed.
For connected-app features, workspace admins control which supported plugins Sites can use. Each visitor authorizes access through their own connected account, and their existing app permissions still apply.
## Availability
This article is for ChatGPT Business and Enterprise owners and admins. Available controls depend on your plan and workspace configuration.
Sites admin preview is rolling out to eligible Enterprise workspaces. Admins can review access before enabling Sites for members. Workspace settings and role permissions determine who can use Sites. Public publishing is controlled separately.
Connected-app features have their own availability requirements. Workspace and organization settings still apply. Data residency support for Sites does not grant connected-app access.
## Data residency
For workspaces with US or EU data residency, new Sites automatically use the workspace’s existing region for supported storage and hosting. Sites are available in workspaces with data residency in other regions, but that regional residency setting does not currently apply to Sites storage and hosting.
Existing Sites stay in their current location and aren’t automatically migrated. Sites regional hosting is separate from inference residency for model processing. For more information, see: [_Data residency and inference residency for ChatGPT_](https://help.openai.com/articles/9903489).
# Set workspace policies
Before enabling Sites broadly, decide:
  * Who can create Sites.
  * Whether public publishing should be allowed.
  * What content can be published.
  * How your organization will handle support, review, takedown, and compliance questions.


Review your workspace’s data residency requirements and the supported Sites scope before members create Sites. Existing Sites stay in their current location and aren’t automatically migrated.
# Enable or limit Sites
Business workspaces have Sites enabled by default. Enterprise owners and admins can use role-based access controls (RBAC) to decide who can create Sites and who can publish them.
Review members’ current Sites access and public-publishing permissions before enabling Sites more broadly.
If Sites appears in **Admin Preview** , select **Set launch access** or **Edit launch access** to choose access at launch. **Launch access** is separate from current preview access.
To keep Sites off at launch, set the relevant **Launch access** choices to **Off** and save your changes. Reopen the setting to check that **Off** was saved.
Follow your launch notice for the opt-out deadline. If you opted out through an earlier process, contact OpenAI Support to confirm that request.
For help with a launch notice or opt-out request, see: [_Contacting OpenAI Support_](https://help.openai.com/articles/6614161).
Public publishing is off by default in Enterprise workspaces. To let members publish Sites publicly:
  1. Turn on public publishing in **Workspace settings**.
  2. Use RBAC to give the appropriate users or groups permission to create and publish Sites.


If a member can’t use Sites, check that:
  * Sites is enabled for the workspace.
  * The member has an eligible role or belongs to an eligible group.
  * The member is signed in to the correct workspace.


These settings control Site creation and publishing. Connected-app access also depends on workspace settings, each visitor’s approval, and tenant policy where applicable.
# Manage connected-app access
In supported workspaces, a Site can use each visitor’s own connected apps. For example, a shared dashboard can show information from the signed-in visitor’s account.
To use connected apps:
  * The Site must be private to a workspace.
  * The visitor must belong to that workspace.
  * The visitor must approve access through their own connected account.


If a Site requests write access, each visitor must approve it for their own connected account. Their existing app permissions still apply. That approval doesn’t give background scheduled tasks access to their connected apps.
Before allowing a plugin in Sites, review the information it can access and the actions it can perform.
If tenant policy blocks access, a global admin must:
  1. Open the OpenAI Admin Console.
  2. Under **External access** , open **ChatGPT Sites**.
  3. Select **Access** , then set **Connected apps** to **Allowed**.


Workspace owners and admins aren’t automatically global admins. Workspaces without a tenant don’t have this control.
If no explicit connected-app policy has been set for Sites, organization-level access is allowed. Existing saved tenant policies remain in effect.
For tenant access and approval steps, see: [_Managing your tenant in Admin Console_](https://help.openai.com/articles/12289294).
## Allow a plugin in Sites
In the plugin’s **Sites** settings, review **Allow site visitors to use this plugin**.
An admin’s saved choice overrides the default. If no choice is saved:
  * Business: available plugins are allowed by default.
  * Enterprise: available plugins are off by default.


A plugin can be available in ChatGPT but turned off in Sites. Turning it on for Sites doesn’t give members access to the app or connect an account for them. Each visitor must still approve the Site’s requested access.
## Check access for a workspace member
If a Site can’t use a member’s connected app, check the workspace settings first:
  * Connected-app access for Sites is available in the workspace.
  * If the workspace has a tenant, the tenant allows connected-app access for ChatGPT Sites. A global admin can review this under **External access** in the OpenAI Admin Console.
  * **Allow site visitors to use this plugin** is turned on for the app’s plugin.
  * The individual app is enabled for the workspace.


Then check the member’s setup:
  * The Site is private to the workspace, and the member belongs to that workspace.
  * The app is connected to the member’s account, and the member has selected the intended connected account.
  * The member has signed in, reviewed the Site’s requested permissions, and approved access.
  * The member has the required permissions in the connected app.


Tenant approval, where required, covers current and future Sites. Each visitor must still approve access through their own account. Tenant approval doesn’t give every Site access to every member’s data.
Sharing a Site, allowing public publishing, or inviting an external viewer doesn’t approve connected-app access.
For steps to build a Site with connected apps and approve visitor access, see: [_Creating and using ChatGPT Sites_](https://help.openai.com/articles/20001339).
# Manage publishing and access
If your Enterprise workspace uses role-based permissions and a member cannot find coworkers when sharing a Site, go to **Workspace settings > Permissions & roles** and review **View workspace members and groups** for their assigned role. Enable it if appropriate for your organization, then ask the member to refresh ChatGPT and try again. This permission controls member-directory visibility; public publishing and external invitations have separate permissions.
A Site can be shared with:
  * Only its owner and workspace admins.
  * Active members of the workspace.
  * Selected active users or groups, where supported.
  * Anyone on the internet, if public publishing is enabled and the member has permission to publish.


The owner can give an active member of the same workspace **Can edit** access. Editors can save changes and, after the owner’s first publish, publish later versions to the same URL.
Editors can also inspect the live database and publish code that uses the Site’s secrets and storage. Give edit access only to trusted collaborators.
From the Site’s own settings, the owner can:
  * Manage who has access.
  * Change the Site name or URL.
  * Transfer ownership to another active workspace member.
  * Configure owner-only settings, such as secrets and custom domains.


Workspace owners and admins can also transfer ownership to another active member of the same workspace.
The owner can change an editor’s access to **Can view** or remove them. This stops the person from editing. Check the Site’s remaining audience settings to see whether they can still view it.  
  
Where custom domains are enabled for workspace Sites, the Site owner can connect a domain they control. If the controls are missing or an action is denied, confirm the Site owner, workspace availability, and Sites permissions before troubleshooting DNS.  
  
For domain setup, see: [_Creating and using ChatGPT Sites_](https://help.openai.com/articles/20001339).  
  
Public sharing makes a Site available outside the workspace according to the audience selected in the publishing flow.  
  
Available controls vary by plan and workspace configuration. If you cannot find or use a control, contact OpenAI Support.
## Review tunnel permissions
A tunnel lets a Site connect to a service on your company’s private network, such as an internal API.
Before connecting a Site to a tunnel:
  * Confirm that the Site owner and the person connecting the tunnel have Sites access. **Allow members to attach private tunnels** must be enabled for both people.
  * Use a tunnel that’s available to the Site’s workspace. If the Site is already public, make it private before adding a new tunnel.
  * Work with the service owner to confirm what data the Site can access and what actions it can perform.


To make the Site public, **Allow public Sites with private tunnels** must be enabled for both the owner and the person publishing it. The workspace must also allow public publishing. Before publishing, check what visitors will be able to see and do through the Site.
Tunnels don’t change visitors’ connected-app permissions.
For tunnel setup, permissions, and troubleshooting, see: [_Connecting ChatGPT Sites to private services with tunnels_](https://help.openai.com/articles/20001606).
## External viewers
Site owners can invite named people outside the workspace to view a Site.
In Business workspaces, creators can invite external viewers through their existing Sites permissions in Workspace settings.
In Enterprise workspaces, the person sending the invitation needs a separate permission to invite external viewers. Follow the Enterprise steps below to turn it on.
Workspace owners and admins can manage external viewers in **Workspace settings > Sites**.
In Enterprise workspaces:
  1. Go to **Workspace settings > Permissions & roles**.
  2. Select the **role** that should be allowed to invite external viewers or choose workspace defaults.
  3. Under **Early access > Sites**, make sure Sites is enabled for that role, or for the workspace.
  4. Turn on **Allow members to invite external visitors** to sites for the selected role.


An external viewer must sign in with the ChatGPT account invited to the Site. They can view the Site but can’t edit it. The invitation doesn’t add them to your workspace or make the Site public.
Permission to invite external viewers is separate from permission to publish publicly. External viewers also don’t meet the workspace-membership requirement for connected-app features.
Removing an invitation may not remove access the person has through another audience setting. After adding or removing an external viewer:
  * Check the saved access list.
  * Check whether another audience setting still gives the person access.
  * Test how the Site appears to the intended visitors.


If the external invitation option is unavailable or a change does not take effect, confirm the selected workspace, the inviter’s role and permission to invite external viewers, and the app or browser being used. If the issue persists, see: [Contacting OpenAI Support](https://help.openai.com/articles/6614161).
# Review access for plugins hosted on Sites
A new or existing Site can host an MCP server and a plugin. Check whether the recipient can access both the plugin and its host Site. Sharing or installing the plugin alone doesn’t give them access to the Site.
The recipient may also need to authorize an app or approve a requested action. Access to the Site doesn’t replace those approvals.
Check permissions separately for:
  * Publishing the Site publicly.
  * Inviting someone to view the Site.
  * Sharing the plugin.
  * Publishing the plugin to a workspace directory.


For more information on hosting plugins on a Site, including specific administrator permissions you need to enable, read: [Hosting a plugin with ChatGPT Sites](https://help.openai.com/articles/20001547).
For plugin access controls, see: [Admin controls, security, and compliance for plugins and apps](https://help.openai.com/articles/11509118).
# Data, compliance, and residency considerations
Sites can involve prompts, instructions, files, site code, generated artifacts, hosted URLs, storage, and logs needed to operate and secure the Site.
For workspaces with US or EU data residency, new Sites automatically use the workspace’s existing region for supported storage and hosting. Sites are available in workspaces with data residency in other regions, but that regional residency setting does not currently apply to Sites storage and hosting.
Existing Sites stay in their current location and aren’t automatically migrated. Sites regional hosting is separate from inference residency for model processing. For more information, see: [Data residency and inference residency for ChatGPT](https://help.openai.com/articles/9903489).
If a Site’s hosting region is unexpected, check the workspace’s designated region and when the Site was created. Existing Sites stay in their current location and aren’t automatically migrated.
## Recommended workspace policy
  * Give members clear guidelines for creating Sites that comply with your organization’s security, confidentiality, privacy, and other requirements.
  * Define a policy for when public publishing is allowed.
  * Require review before publishing sites that include confidential, sensitive, or third-party content.
  * Decide who can approve public Sites and who can remove them.
  * Document where members should report suspicious, malicious, infringing, or unsafe Sites.
  * Name a person responsible for keeping each Site current and handling access questions. Plan the handoff before that person leaves the team.
  * Review the Site after material changes to its content, connected services, or audience.


# FAQ
## Are Enterprise workspaces charged for Sites hosting and usage?
Charges for running and hosting Sites are currently waived for Enterprise workspaces. Building or editing a Site still counts toward Codex usage. Usage and storage limits still apply.
## Was this article helpful?
Submit
![OpenAI logo](https://help.openai.com/favicon.png)[ChatGPT](https://chatgpt.com)[API](https://platform.openai.com/docs/)[Service Status](https://status.openai.com)Cookie Preferences

