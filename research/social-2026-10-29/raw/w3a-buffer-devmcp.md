![](https://developers.buffer.com/image/banner-line.svg) ![](https://developers.buffer.com/image/banner-dot.svg) ![](https://developers.buffer.com/image/banner-line.svg) ![](https://developers.buffer.com/image/banner-dot.svg)
![Buffer Commit](https://developers.buffer.com/image/banner-commit-logo.svg)
Join Buffer’s first Build Contest. October 28 - November 13
[Register](https://buffer.com/api/commit?utm_source=buffer&utm_medium=banner&utm_campaign=buffer_commit&utm_content=developer_portal)
[ ![Buffer API](https://developers.buffer.com/logo.svg) ](https://developers.buffer.com/index.html)
Search docs... `⌘K`
[ ](https://discord.gg/9skbzTz6vQ "Discord")
[API Status](https://status.buffer.com/) [Get API Key](https://publish.buffer.com/settings/api)
Guides 
[Introduction](https://developers.buffer.com/guides/introduction.html) [Quick Start](https://developers.buffer.com/guides/getting-started.html) [Authentication](https://developers.buffer.com/guides/authentication.html) [Building Apps](https://developers.buffer.com/guides/building-apps.html) [Your First Post](https://developers.buffer.com/guides/your-first-post.html) [GraphQL for REST Devs](https://developers.buffer.com/guides/graphql-intro.html) [REST API Migration](https://developers.buffer.com/guides/rest-migration.html) [Data Model](https://developers.buffer.com/guides/data-model.html) [Posts & Scheduling](https://developers.buffer.com/guides/posts-and-scheduling.html) [Ideas](https://developers.buffer.com/guides/ideas.html) [Content Items Experimental](https://developers.buffer.com/guides/content-items.html) [Hosting Media](https://developers.buffer.com/guides/hosting-media.html) [Tags Experimental](https://developers.buffer.com/guides/tags.html) [Post Metrics](https://developers.buffer.com/guides/post-metrics.html) [API Standards](https://developers.buffer.com/guides/api-standards.html) [Character Limits](https://developers.buffer.com/guides/character-limits.html) [Error Handling](https://developers.buffer.com/guides/error-handling.html) [Rate Limits](https://developers.buffer.com/guides/api-limits.html) [Pagination](https://developers.buffer.com/guides/pagination.html) [Efficient API Usage](https://developers.buffer.com/guides/efficient-api-usage.html)
Examples 
[Aggregate Post Metrics](https://developers.buffer.com/examples/aggregate-post-metrics.html) [Create Draft Post](https://developers.buffer.com/examples/create-draft-post.html) [Create Idea](https://developers.buffer.com/examples/create-idea.html) [Create Image Post](https://developers.buffer.com/examples/create-image-post.html) [Create Instagram Post With User Tags](https://developers.buffer.com/examples/create-instagram-post-with-user-tags.html) [Create Scheduled Post](https://developers.buffer.com/examples/create-scheduled-post.html) [Create Tag Experimental](https://developers.buffer.com/examples/create-tag.html) [Create Text Post](https://developers.buffer.com/examples/create-text-post.html) [Create Threaded Post](https://developers.buffer.com/examples/create-threaded-post.html) [Create Video Post](https://developers.buffer.com/examples/create-video-post.html) [Delete Tag Experimental](https://developers.buffer.com/examples/delete-tag.html) [Get Channel](https://developers.buffer.com/examples/get-channel.html) [Get Channels](https://developers.buffer.com/examples/get-channels.html) [Get Filtered Channels](https://developers.buffer.com/examples/get-filtered-channels.html) [Get Organizations](https://developers.buffer.com/examples/get-organizations.html) [Get Paginated Posts](https://developers.buffer.com/examples/get-paginated-posts.html) [Get Post Metrics](https://developers.buffer.com/examples/get-post-metrics.html) [Get Posts For Channels](https://developers.buffer.com/examples/get-posts-for-channels.html) [Get Posts With Assets](https://developers.buffer.com/examples/get-posts-with-assets.html) [Get Posts With Metrics](https://developers.buffer.com/examples/get-posts-with-metrics.html) [Get Quarterly Performance Report](https://developers.buffer.com/examples/get-quarterly-performance-report.html) [Get Scheduled Posts](https://developers.buffer.com/examples/get-scheduled-posts.html) [Get Tag Experimental](https://developers.buffer.com/examples/get-tag.html) [Get Tags Experimental](https://developers.buffer.com/examples/get-tags.html) [Update Tag Experimental](https://developers.buffer.com/examples/update-tag.html)
[ CLI](https://developers.buffer.com/guides/cli.html) [ Integrations](https://developers.buffer.com/guides/integrations.html) [ Explorer](https://developers.buffer.com/explorer.html) [ Changelog](https://developers.buffer.com/changelog.html) [ Roadmap](https://developers.buffer.com/roadmap.html) [ Legacy Apps](https://buffer.com/developers/legacy-api)
API Reference
[ Account](https://developers.buffer.com/reference.html#account)[ Organizations](https://developers.buffer.com/reference.html#organizations)[ Channels](https://developers.buffer.com/reference.html#channels)[ Tags](https://developers.buffer.com/reference.html#tags)[ Posts](https://developers.buffer.com/reference.html#posts)[ Ideas](https://developers.buffer.com/reference.html#ideas)[ Other](https://developers.buffer.com/reference.html#other)
[Integrations](https://developers.buffer.com/guides/integrations.html)MCP server
# MCP server
![MCP](https://developers.buffer.com/guides/integrations/mcp.html)
## MCP server
The tools, rate limits and security of Buffer's MCP server
The Model Context Protocol (MCP) is an open standard that lets an AI assistant work with an outside service through a set of tools it can call. Buffer runs a remote MCP server at `https://mcp.buffer.com/mcp`, which enables AI assistants to read your channels, browse your queue and drafts, schedule and edit posts, capture ideas and pull post analytics, all without leaving the conversation.
Most AI tools connect over OAuth, with no API key. Find yours in [Integrations](https://developers.buffer.com/guides/integrations.html). If it isn't listed, see [Other AI tools](https://developers.buffer.com/guides/integrations/other-ai-tools.html).
## Supported tools[](https://developers.buffer.com/guides/integrations/mcp.html#supported-tools)
The Buffer MCP server exposes a large list of tools. Most of them cover a specific job, like listing channels or scheduling a post. Two generic tools let an assistant reach the rest of the GraphQL API when no specific tool fits.
A few conventions apply across the tools:
  * Every ID is a 24-character hex string.
  * Every date and time is an ISO 8601 string with a UTC offset, such as `2026-08-11T17:00:00-05:00`. `get_account` returns the account timezone and its current local time, which is what an assistant should use to turn "tomorrow at 5pm" into a real timestamp.
  * Tools that return lists page with `first` and `after`, returning 20 items by default and up to 100 per page.
  * `create_post`, `edit_post`, `delete_post`, `create_idea` and the template write tools change your data. Most MCP clients ask you to approve those before they run.
  * The write tools hand back the record they saved, and the post tools report each post's `allowedActions`. An assistant is expected to reuse an ID or a post it has already seen in the conversation rather than spending another call to look the same thing up again.
  * Every successful tool response carries the quota that is left: the requests remaining in each window and the seconds until it resets. An error carries its own diagnostics instead, so a `429` reports `Retry-After` rather than a quota. See the rate limits section below.


### Account tools[](https://developers.buffer.com/guides/integrations/mcp.html#account-tools)
#### `get_account`
Returns the signed-in account and the organizations it belongs to: email, name, timezone, the current time in that timezone, and for each organization its ID, name, plan limits and member count.
If you belong to more than one organization, an assistant will name them and ask which one you mean before going further.
Takes no parameters.
**Example prompt:** "Which Buffer organizations do I have access to?"
### Channel tools[](https://developers.buffer.com/guides/integrations/mcp.html#channel-tools)
#### `list_channels`
Lists the social accounts connected to an organization, with each channel's ID, name, display name, service, type, avatar and connection status.  
| Parameter  | Type  | Required  | Description  |  
| --- | --- | --- | --- |  
| `organizationId`  | string  | Yes  | The organization to list channels for  |  
**Example prompt:** "List all my connected Buffer channels."
#### `get_channel`
Returns the detail that `list_channels` leaves out for a single channel: its posting schedule, posting goals, queue status, timezone, link shortening settings, and service-specific data such as Pinterest boards, a Mastodon server URL or Instagram reminder settings.  
| Parameter  | Type  | Required  | Description  |  
| --- | --- | --- | --- |  
| `channelId`  | string  | Yes  | The channel to read  |  
**Example prompt:** "What times does my LinkedIn channel post at?"
### Post tools[](https://developers.buffer.com/guides/integrations/mcp.html#post-tools)
#### `list_posts`
Lists posts in an organization. Returns each post's ID, status, text, scheduled and sent times, channel, tags, assets, `via` and any publishing error.
Each post also carries `allowedActions`, the list of what you can do with it, so an assistant can move straight to an edit or a delete without reading the post again to find out whether it is allowed.  
| Parameter  | Type  | Required  | Description  |  
| --- | --- | --- | --- |  
| `organizationId`  | string  | Yes  | The organization to list posts for  |  
| `channelIds`  | string[]  | No  | Only return posts on these channels  |  
| `status`  | string[]  | No  | Any of `draft`, `needs_approval`, `scheduled`, `sending`, `sent`, `error`  |  
| `tagIds`  | string[]  | No  | Only return posts carrying any of these tags  |  
| `dueAt`  | object  | No  |  `start` and `end` bounds on the scheduled time  |  
| `createdAt`  | object  | No  |  `start` and `end` bounds on the creation time  |  
| `sort`  | object[]  | No  | Sort by `dueAt` or `createdAt`, `asc` or `desc`  |  
| `first`  | integer  | No  | Page size, 20 by default and 100 at most  |  
| `after`  | string  | No  | Pagination cursor  |  
| `includeMetrics`  | boolean  | No  | Also return per-post analytics. Off by default, since it makes the response much larger  |  
**Example prompt:** "Show me all my draft posts in Buffer so I can review what's pending."
#### `get_post`
Reads one post in full: status, content, author, channel, tags, notes, assets and `allowedActions`, the list of what you are allowed to do with it. The `metadata` field carries service-specific data such as Instagram geolocation, a Twitter thread or YouTube privacy settings. A post with the `error` status carries the failure message.  
| Parameter  | Type  | Required  | Description  |  
| --- | --- | --- | --- |  
| `postId`  | string  | Yes  | The post to read  |  
| `includeMetrics`  | boolean  | No  | Also return this post's analytics and the time they were last refreshed  |  
**Example prompt:** "Why did my Instagram post from yesterday fail?"
#### `create_post`
Schedules or publishes a post on one channel. Works for Instagram, Facebook, Twitter, LinkedIn, Pinterest, YouTube, Google Business, Mastodon, TikTok, Threads, Bluesky, Substack and Start Page.
What each service needs as a minimum:
  * Twitter, Mastodon, Threads and Bluesky: text only.
  * Facebook: the post type in `metadata.facebook.type`.
  * Instagram: an image or a video, plus the post type in `metadata.instagram.type`.
  * TikTok: an image or a video.
  * Pinterest: an image, plus the board to pin to in `metadata.pinterest.boardServiceId`, which `get_channel` returns under `metadata.boards[].serviceId`.
  * YouTube: a video, plus a title and category in `metadata.youtube`.
  * Substack: text, an image or a video, or a link in `metadata.substack.linkAttachment`.
  * Google Business: the post type in `metadata.google.type`.


Twitter, Mastodon, Threads and Bluesky also take a thread, through `metadata.<service>.thread`. A threaded post sets both the top-level `text` and that array, the array holds every item in the thread, and the top-level `text` repeats the first item's text. Thread items attach media with the same asset shape as the post itself.
A link preview card is not an asset. It goes in `metadata.<service>.linkAttachment` on Facebook, LinkedIn, Threads and Bluesky, and it cannot be sent alongside a non-empty `assets` array. On Threads and Bluesky an individual thread item can carry one of its own.  
| Parameter  | Type  | Required  | Description  |  
| --- | --- | --- | --- |  
| `channelId`  | string  | Yes  | The channel to post to, taken from `list_channels`  |  
| `schedulingType`  | string  | Yes  |  `automatic` to publish for you, or `notification` to send you a reminder to post manually  |  
| `mode`  | string  | No  |  `addToQueue` (the default), `shareNow`, `shareNext`, or `customScheduled`, which needs `dueAt`  |  
| `text`  | string  | No  | The body of the post  |  
| `dueAt`  | string  | No  | When to publish, required for `customScheduled` and always in the future  |  
| `tagIds`  | string[]  | No  | Tags to file the post under  |  
| `assets`  | object[]  | No  | Media to attach, each one an image, a video, or a document on LinkedIn  |  
| `metadata`  | object  | No  | Service-specific settings, keyed by service  |  
| `saveToDraft`  | boolean  | No  | Save as a draft instead of scheduling it  |  
| `ideaId`  | string  | No  | The idea this post is being created from  |  
| `draftId`  | string  | No  | The draft this post is being created from  |  
It returns the post it saved: content, assets, service settings, tags, `allowedActions`, status and scheduling. An assistant does not need to read the post back to confirm what was stored.
**Example prompt:** "Add a post to my Buffer queue that says 'Excited to share our latest update!' for next Monday."
#### `edit_post`
Changes an existing post. The post that results is validated as a whole, the same way a new one is, so anything you do send has to stand on its own rather than being merged field by field into the stored version.
Omission is how you keep what you are not changing, and it is the safer default. Leave `assets` out and the stored media stays; leave `mode` and `dueAt` out and the post keeps its slot; leave a service setting out and it stays as it is. Resending a value you did not mean to change risks writing a stale copy back over something that moved in the meantime.
What has to be complete is any field you do send, because these replace wholesale rather than merging: the `assets` array, a `metadata.<service>.thread` array, and a service metadata object, which still has to carry its required members, such as an Instagram post's `type` and `shouldShareToFeed`. Dropping one of those from an object you are sending will make the edit fail.
Scheduling follows the same pattern. Leaving `schedulingType` out keeps the post publishing the way it already does, and leaving `mode` and `dueAt` out keeps its current slot. Sending a `mode` reschedules the post even when it matches the one already set, so send one only when you mean to move the post.
An assistant does not need a fresh read to work this out. `create_post` and `edit_post` both return the post they saved, so one that already created or edited the post in this conversation can work from that response, and call `get_post` only when something it needs is missing or may have gone stale.
When you do replace the media, an existing asset's `source` becomes `url` and, on images only, its `thumbnail` becomes `thumbnailUrl`; a video never takes a `thumbnailUrl` and picks its frame through `metadata.thumbnailOffset` instead, on Instagram, TikTok and Pinterest. Service settings such as `firstComment`, `linkAttachment`, an Instagram `geolocation` and LinkedIn `annotations` are kept when you leave them out and cleared when you send `null`.
Editing a threaded post follows the same rule as creating one: send both the top-level `text` and the whole `metadata.<service>.thread` array, not just the item that changed.  
| Parameter  | Type  | Required  | Description  |  
| --- | --- | --- | --- |  
| `postId`  | string  | Yes  | The post to change  |  
| `schedulingType`  | string  | No  |  `automatic` or `notification`  |  
| `mode`  | string  | No  |  `addToQueue`, `shareNow`, `shareNext`, or `customScheduled`  |  
| `text`  | string  | No  | The body of the post  |  
| `dueAt`  | string  | No  | A new publishing time, only valid with `customScheduled`  |  
| `tagIds`  | string[]  | No  | Tags to file the post under  |  
| `assets`  | object[]  | No  | Media to attach. Leave it out to keep the stored media, send an empty array to clear it, or send a new array to replace it  |  
| `metadata`  | object  | No  | Service-specific settings, keyed by service  |  
| `saveToDraft`  | boolean  | No  | Move the post back to a draft  |  
| `ideaId`  | string  | No  | The idea this post is being created from  |  
| `draftId`  | string  | No  | The draft this post is being created from  |  
It returns the post it saved, in the same shape `create_post` does.
**Example prompt:** "Move my Thursday LinkedIn post to Friday at 9am and shorten the opening line."
#### `delete_post`
Deletes a post for good. Not every post can be deleted, so an assistant should check that `deletePost` appears in the post's `allowedActions`. `list_posts` and `get_post` both return that list, so this does not cost an extra lookup.  
| Parameter  | Type  | Required  | Description  |  
| --- | --- | --- | --- |  
| `postId`  | string  | Yes  | The post to delete  |  
**Example prompt:** "Delete the draft I made this morning about the pricing update."
#### `get_aggregated_post_metrics`
Adds up analytics across many posts over a date range and returns the totals and averages, rather than making an assistant pull every post and do the arithmetic itself.
The response always carries post count, reactions and comments. Other metrics, such as reach, impressions and engagement rate, appear only when every channel in the filter supports them. Metrics refresh once a day, so values can lag the social network by up to a day; `metricsUpdatedAt` reports how fresh the aggregate is, and is null when no post matched the filter. The date range can cover at most 365 days.  
| Parameter  | Type  | Required  | Description  |  
| --- | --- | --- | --- |  
| `organizationId`  | string  | Yes  | The organization to aggregate metrics for  |  
| `startDateTime`  | string  | Yes  | Start of the window, inclusive  |  
| `endDateTime`  | string  | Yes  | End of the window, inclusive  |  
| `channelIds`  | string[]  | No  | Channels to include. Leave it out to cover every channel you can see insights for. An empty array filters every channel out and returns an empty result  |  
| `tags`  | object  | No  |  `in` limits the aggregate to posts carrying any of these tags, `isEmpty` also counts untagged posts  |  
**Example prompt:** "How did my LinkedIn posts perform last month?"
### Idea tools[](https://developers.buffer.com/guides/integrations/mcp.html#idea-tools)
#### `list_ideas`
Lists the ideas in an organization. Ideas capture a concept for a future post before it belongs to a channel. Each one returns its title, text, media, tags, target services, target date, board column and timestamps.  
| Parameter  | Type  | Required  | Description  |  
| --- | --- | --- | --- |  
| `organizationId`  | string  | Yes  | The organization to list ideas for  |  
| `tagIds`  | string[]  | No  | Only return ideas carrying any of these tags  |  
| `includeUntagged`  | boolean  | No  | Also return ideas with no tags. Off by default  |  
| `first`  | integer  | No  | Page size, 20 by default and 100 at most  |  
| `after`  | string  | No  | Pagination cursor  |  
**Example prompt:** "What ideas do I have saved that are tagged for the product launch?"
#### `list_idea_groups`
Lists the columns on the ideas board, with each column's ID, name and lock status.  
| Parameter  | Type  | Required  | Description  |  
| --- | --- | --- | --- |  
| `organizationId`  | string  | Yes  | The organization to list idea groups for  |  
**Example prompt:** "What columns does my Buffer ideas board have?"
#### `create_idea`
Saves a new idea. This captures content for later. It does not schedule or publish anything.
Idea media can be an image, a GIF, a link or a document. Video is not supported on ideas through the public API.  
| Parameter  | Type  | Required  | Description  |  
| --- | --- | --- | --- |  
| `organizationId`  | string  | Yes  | The organization to create the idea in  |  
| `content`  | object  | Yes  | The idea itself: `title`, `text`, `media`, `tags`, target `services` and a target `date`, all optional  |  
**Example prompt:** "Save an idea for a post about our new integration, tagged for Instagram and LinkedIn."
### Post template tools[](https://developers.buffer.com/guides/integrations/mcp.html#post-template-tools)
Post templates are reusable starting points for content. A template body can hold `{{placeholders}}` to fill in later. Each template is public, internal or private: public templates are curated by Buffer, internal ones are shared with everyone in your organization, and private ones are yours alone.
#### `list_post_templates`
Lists the templates you can use in an organization. With no filter this returns all three kinds together: the public templates, your organization's internal ones, and your own private ones.  
| Parameter  | Type  | Required  | Description  |  
| --- | --- | --- | --- |  
| `organizationId`  | string  | Yes  | The organization whose templates to list  |  
| `visibility`  | string  | No  | Narrow to `private`, `internal` or `public`  |  
| `first`  | integer  | No  | Page size, 20 by default and 100 at most  |  
| `after`  | string  | No  | Pagination cursor  |  
**Example prompt:** "What post templates can I use?"
#### `get_post_template`
Reads one template: its body, title, description, emoji, visibility and timestamps.  
| Parameter  | Type  | Required  | Description  |  
| --- | --- | --- | --- |  
| `postTemplateId`  | string  | Yes  | The template to read  |  
**Example prompt:** "Show me the full text of my product announcement template."
#### `create_post_template`
Creates a template in an organization. You can set it to private or internal. Public is curated by Buffer and cannot be set here.  
| Parameter  | Type  | Required  | Description  |  
| --- | --- | --- | --- |  
| `organizationId`  | string  | Yes  | The organization the template belongs to  |  
| `title`  | string  | Yes  | The name of the template  |  
| `body`  | string  | Yes  | The content, which may contain `{{placeholders}}`  |  
| `description`  | string  | Yes  | A short description of what the template is for  |  
| `emoji`  | string  | No  | An emoji to show alongside the template  |  
| `visibility`  | string  | No  |  `private`, the default, or `internal`  |  
**Example prompt:** "Turn this post into a template my whole team can reuse."
#### `update_post_template`
Changes a template. Only the fields you send are changed. You can edit templates you own, and internal templates in your organization if you are an admin or owner.  
| Parameter  | Type  | Required  | Description  |  
| --- | --- | --- | --- |  
| `postTemplateId`  | string  | Yes  | The template to change  |  
| `title`  | string  | No  | The name of the template  |  
| `body`  | string  | No  | The content, which may contain `{{placeholders}}`  |  
| `description`  | string  | No  | A short description of what the template is for  |  
| `emoji`  | string  | No  | An emoji to show alongside the template  |  
| `visibility`  | string  | No  |  `private` or `internal`  |  
**Example prompt:** "Add a call to action line to my weekly recap template."
#### `delete_post_template`
Deletes a template for good. You can delete templates you own, and internal templates in your organization if you are an admin or owner.  
| Parameter  | Type  | Required  | Description  |  
| --- | --- | --- | --- |  
| `postTemplateId`  | string  | Yes  | The template to delete  |  
**Example prompt:** "Delete the old holiday sale template."
## Beyond the tools[](https://developers.buffer.com/guides/integrations/mcp.html#beyond-the-tools)
There is one prompt, `review_weekly_posts`, which reviews the posts you have scheduled for the current week and groups them by channel. Clients that support prompts usually list it as a command you can pick.
## Rate limits[](https://developers.buffer.com/guides/integrations/mcp.html#rate-limits)
Requests made through the MCP server count against the same [rate limits](https://developers.buffer.com/guides/api-limits.html) as your API keys: a 15-minute, 24-hour and 30-day window, with quotas that depend on your plan. Your MCP connections and API keys share one set of limits, counted across every request rather than per tool, so one conversation that lists your posts, reads a few of them and then edits one has spent several requests from the same budget.
Every successful tool response carries the quota alongside the result: the requests remaining in each window and the seconds until that window resets. An assistant can read those numbers and pace itself, rather than finding the limit by hitting it.
Past the limit the call fails with `429 Too Many Requests`, and the error the assistant sees carries the `Retry-After` value from the API, in seconds. That is how long to wait before asking for anything else.
Most of what keeps an assistant inside these limits is how you prompt it. Check out the [prompts for AI agents](https://developers.buffer.com/guides/efficient-api-usage.html#prompts-for-ai-agents) section of the Efficient API Usage guide for best practices and example prompts.
## Security considerations[](https://developers.buffer.com/guides/integrations/mcp.html#security-considerations)
Connecting a client to the MCP server gives it the same reach over your content as you have, so it is worth knowing what that covers before you connect one.
  * **The connection covers your whole account.** The assistant acts for you and reaches every organization and channel in your account. There is no per-organization scoping, so you cannot open one workspace to an assistant while holding another back.
  * **Check the server URL.** The only Buffer MCP endpoint is `https://mcp.buffer.com/mcp`. A one-click install from a third-party list is worth opening and reading before you trust it.
  * **Leave the approval prompts on.** `create_post` can publish immediately, and `delete_post` cannot be undone. Most clients ask before they run a tool that writes, and that prompt is your last chance to catch a misread instruction.


## Try It Out[](https://developers.buffer.com/guides/integrations/mcp.html#try-it-out)
Copy any of these example prompts to get started:
List all my connected Buffer channels
Add a post to my Buffer queue that says 'Excited to share our latest update!' for next Monday
Show me all my draft posts in Buffer so I can review what's pending
On this page
[Supported tools](https://developers.buffer.com/guides/integrations/mcp.html#supported-tools) [Account tools](https://developers.buffer.com/guides/integrations/mcp.html#account-tools) [Channel tools](https://developers.buffer.com/guides/integrations/mcp.html#channel-tools) [Post tools](https://developers.buffer.com/guides/integrations/mcp.html#post-tools) [Idea tools](https://developers.buffer.com/guides/integrations/mcp.html#idea-tools) [Post template tools](https://developers.buffer.com/guides/integrations/mcp.html#post-template-tools) [Beyond the tools](https://developers.buffer.com/guides/integrations/mcp.html#beyond-the-tools) [Rate limits](https://developers.buffer.com/guides/integrations/mcp.html#rate-limits) [Security considerations](https://developers.buffer.com/guides/integrations/mcp.html#security-considerations) [Try It Out](https://developers.buffer.com/guides/integrations/mcp.html#try-it-out)
`Esc`
`↑``↓` Navigate `Enter` Open `Esc` Close
×

