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
# Buffer API
Copy Page
Ask AI assistant Chat with the docs AI assistant Copy page Copy this page as Markdown View as Markdown Open this page as plain Markdown Open in Claude Ask Claude about this page Open in ChatGPT Ask ChatGPT about this page Open in Perplexity Ask Perplexity about this page
Connect Buffer to your agents, automation tools, or build something entirely new.
## Account
### Queries 1
QUERY account : [Account](https://developers.buffer.com/reference.html#type/Account)!
Retrieves the authenticated user's account information
Example Response

```
{
  "data": {
    "account": {
      "id": "...",
      "email": "...",
      "backupEmail": "...",
      "avatar": "..."
    }
  }
}
```

### Outputs 1
OUTPUT [Account](https://developers.buffer.com/reference.html#type/Account)
Account is a representation of a Buffer user.
Fields 10
id : ID!
Unique identifier for the account
email : String!
Primary email address for the account
backupEmail : String
Backup email address for account recovery
avatar : String!
URL to the account's avatar image
createdAt : [DateTime](https://developers.buffer.com/reference.html#type/DateTime)
Date the account was created in the Core DB. For older customers, it's possible a Publish account existed in the Publish DB for this customer before this date
organizations (filter: [OrganizationFilterInput](https://developers.buffer.com/reference.html#type/OrganizationFilterInput)) : [[Organization](https://developers.buffer.com/reference.html#type/Organization)!]!
timezone : String
The account-level timezone - this is used as a default input for streaks, posting plans, and new channel channel connections.
name : String
The account name, different from the organization name
preferences : [Preferences](https://developers.buffer.com/reference.html#type/Preferences)
The accounts preferences
connectedApps : [[ConnectedApp](https://developers.buffer.com/reference.html#type/ConnectedApp)!]
The connected apps for the account
### Types 2
TYPE [ConnectedApp](https://developers.buffer.com/reference.html#type/ConnectedApp)
Connected App
Fields 8
category : [ConnectedAppCategory](https://developers.buffer.com/reference.html#type/ConnectedAppCategory)
The category of the connected app, when known.
clientId : ID!
The id of the connectedApp.
description : String!
A brief description of the connected app.
name : String!
The name of the connected app.
scopes : [String!]!
The access scopes granted to this connection for Buffer's public API resources. Empty when the connection holds none.
userId : ID!
The id of the user that has granted access to the app.
website : String!
The website URL of the connected app.
createdAt : [DateTime](https://developers.buffer.com/reference.html#type/DateTime)!
The date and time when the connected app was created.
TYPE [Preferences](https://developers.buffer.com/reference.html#type/Preferences)
Account preferences
Fields 3
timeFormat : String
startOfWeek : String
defaultScheduleOption : [ScheduleOption](https://developers.buffer.com/reference.html#type/ScheduleOption)!
### Enums 2
ENUM [ConnectedAppCategory](https://developers.buffer.com/reference.html#type/ConnectedAppCategory)
The category of a connected app.
ENUM [ScheduleOption](https://developers.buffer.com/reference.html#type/ScheduleOption)
### Scalars 2
SCALAR [AccountId](https://developers.buffer.com/reference.html#type/AccountId)
The `AccountId` scalar represents the ID of a Buffer Account
SCALAR [DateTime](https://developers.buffer.com/reference.html#type/DateTime)
The `DateTime` scalar represents a date and time following the ISO 8601 standard.
## Channels
### Queries 2
QUERY channel (input: [ChannelInput](https://developers.buffer.com/reference.html#type/ChannelInput)!) : [Channel](https://developers.buffer.com/reference.html#type/Channel)!
Fetches a single channel using the provided ID
Arguments  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| input Required  |  [ChannelInput](https://developers.buffer.com/reference.html#type/ChannelInput)!  |  Query's input.   |  
Example Response

```
{
  "data": {
    "channel": {
      "id": "...",
      "allowedActions": [
        "approvePosts"
      ],
      "avatar": "...",
      "descriptor": "..."
    }
  }
}
```

QUERY channels (input: [ChannelsInput](https://developers.buffer.com/reference.html#type/ChannelsInput)!) : [[Channel](https://developers.buffer.com/reference.html#type/Channel)!]!
Fetch all channels for the organization taking into account the current's user permissions
Arguments  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| input Required  |  [ChannelsInput](https://developers.buffer.com/reference.html#type/ChannelsInput)!  |  Query's input.   |  
Example Response

```
{
  "data": {
    "channels": [
      {
        "id": "...",
        "allowedActions": [
          "approvePosts"
        ],
        "avatar": "...",
        "descriptor": "..."
      }
    ]
  }
}
```

### Outputs 1
OUTPUT [Channel](https://developers.buffer.com/reference.html#type/Channel)
Channel entity
Fields 27
id : [ChannelId](https://developers.buffer.com/reference.html#type/ChannelId)!
The ID of the channel
allowedActions : [[ChannelAction](https://developers.buffer.com/reference.html#type/ChannelAction)!]!
The allowed actions for the current user
avatar : String!
The avatar URL of the channel
descriptor : String!
Formatted name of the channel service and type: e.g. 'Twitter Profile' or 'Facebook Page'
displayName : String
The display name of the channel - nullable (reason?)
externalLink : String
The channel's URL on the social network (e.g. instagram.com/username or facebook.com/page) Returns null if the channel is not supported
hasActiveMemberDevice : Boolean!
Whether at least one member of the orginization who have access to this channel also has a user device registered for push notifications
isDisconnected : Boolean!
Indicates if the channel is properly connected to Buffer
isLocked : Boolean!
Indicates if the channel is locked - Locked channels can't be used for posting. A channel can be locked when the organization downgrades and reduces the channel quantity of their plan.
isNew : Boolean!
Indicates if the channel was recently created (in less than 10 seconds). This is used to determine the redirect modal after channel authorization
isQueuePaused : Boolean!
Indicates is the queue is paused for the channel. A paused queue means schedules posts won't be published.
linkShortening : [ChannelLinkShortening](https://developers.buffer.com/reference.html#type/ChannelLinkShortening)!
Link Shortening settings for the channel
metadata : [ChannelMetadata](https://developers.buffer.com/reference.html#type/ChannelMetadata)
Metadata or settings depending on the service type - such as the server URL for Mastodon or Location data for Facebook/GPB
name : String!
The name of the channel - the handle name, username, etc.
organizationId : [OrganizationId](https://developers.buffer.com/reference.html#type/OrganizationId)!
The organization ID of the channel
postingGoal : [PostingGoal](https://developers.buffer.com/reference.html#type/PostingGoal)
The posting goal for the channel
postingSchedule : [[ScheduleV2](https://developers.buffer.com/reference.html#type/ScheduleV2)!]!
Provides the posting slots for each day of the week
products : [[Product](https://developers.buffer.com/reference.html#type/Product)!]
Products that support a given channel
scopes : [String]!
Scopes requested for a given channel - empty array if we don't have them tracked
service : [Service](https://developers.buffer.com/reference.html#type/Service)!
Represents the social network
serviceId : String!
Represents the external ID of the channel on social network API
showTrendingTopicSuggestions : Boolean!
Indicates if trending topic suggestions should be shown in the composer. When false, users can still access trends via the trending icon button. Defaults to true for backward compatibility.
timezone : String!
The timezone of the channel - Default if not set is Europe/London
type : [ChannelType](https://developers.buffer.com/reference.html#type/ChannelType)!
The type of the channel - Page, Profile, Business, Group, Account, etc.
weeklyPostingLimit : [WeeklyPostingLimit](https://developers.buffer.com/reference.html#type/WeeklyPostingLimit)
Weekly posting limit for the channel
createdAt : [DateTime](https://developers.buffer.com/reference.html#type/DateTime)!
The creation date of the channel
updatedAt : [DateTime](https://developers.buffer.com/reference.html#type/DateTime)!
The last time the channel was updated
### Types 37
TYPE [BlueskyMetadata](https://developers.buffer.com/reference.html#type/BlueskyMetadata)
Bluesky metadata
Fields 1
serverUrl : String!
The instance of bluesky of the channel
TYPE [ChannelConfiguration](https://developers.buffer.com/reference.html#type/ChannelConfiguration) ⚠️ Experimental
Everything for one connected channel: its engagement capabilities, its full `content` config, and per-feature authorization. Each channel carries its own complete config — there is no service-level default to merge against.
Fields 6
authorizationStatus : [[FeatureAuthorizationStatus](https://developers.buffer.com/reference.html#type/FeatureAuthorizationStatus)!]!
Authorization status per feature for this channel. A feature is a capability a channel can expose — e.g. posting, commenting, mentions, insights (see the `Feature` enum).
channelId : [ChannelId](https://developers.buffer.com/reference.html#type/ChannelId)!
The connected channel this config describes.
channelType : [ChannelType](https://developers.buffer.com/reference.html#type/ChannelType)!
The channel's type within the service (e.g. profile, page, business).
content : [[ContentConfiguration](https://developers.buffer.com/reference.html#type/ContentConfiguration)!]!
Content config — one entry per content type, or a single entry grouping several types that share identical rules (post / story / reel / comment reply).
engagement : [[EngagementTypeConfiguration](https://developers.buffer.com/reference.html#type/EngagementTypeConfiguration)!]!
Engagement capabilities — one entry per engagement type. Empty when engagement isn't supported on the channel.
service : [Service](https://developers.buffer.com/reference.html#type/Service)!
The channel's social service (e.g. twitter, instagram).
TYPE [ChannelLinkShortening](https://developers.buffer.com/reference.html#type/ChannelLinkShortening)
Settings for link shortening
Fields 2
config : [LinkShorteningConfig](https://developers.buffer.com/reference.html#type/LinkShorteningConfig)
Configuration of link shortening integration. Null if disabled.
isEnabled : Boolean!
If link shortening is enabled for the channel
TYPE [ChannelRefreshRequired](https://developers.buffer.com/reference.html#type/ChannelRefreshRequired) ⚠️ Experimental
Error returned when the channel needs a refresh
Fields 2
channelIds : [[ChannelId](https://developers.buffer.com/reference.html#type/ChannelId)!]!
ChannelIds that need refreshing
message : String!
Error message
TYPE [ContentConfiguration](https://developers.buffer.com/reference.html#type/ContentConfiguration) ⚠️ Experimental
Config for one or more content types that share the same properties and rules. Grouping several `configurationContentTypes` in one entry avoids duplicating an identical config (e.g. story + reel).
Fields 3
configurationContentTypes : [[ConfigurationContentType](https://developers.buffer.com/reference.html#type/ConfigurationContentType)!]!
The content type(s) this config applies to (grouped when rules are identical).
rules : [[ValidationRule](https://developers.buffer.com/reference.html#type/ValidationRule)!]!
Validation rules that decide whether a draft is valid.
supportedProperties : [[ContentProperty](https://developers.buffer.com/reference.html#type/ContentProperty)!]!
The properties these content types support; absence means unsupported.
TYPE [EngagementSupportedReaction](https://developers.buffer.com/reference.html#type/EngagementSupportedReaction) ⚠️ Experimental
A supported reaction. `reactionType` is the opaque identity echoed back on the react mutation; `visual` carries everything needed to render it.
Fields 2
reactionType : [ReactionType](https://developers.buffer.com/reference.html#type/ReactionType)!
The kind of reaction a user can apply (e.g. like, love, celebrate). This is the identifier the client sends back to the react mutation when the user picks this reaction; treat it as an opaque value rather than parsing it.
visual : [ReactionVisual](https://developers.buffer.com/reference.html#type/ReactionVisual)!
How to render this reaction (built-in icon or network image).
TYPE [EngagementTypeConfiguration](https://developers.buffer.com/reference.html#type/EngagementTypeConfiguration) ⚠️ Experimental
Per-engagement-type configuration. One entry per kind; `engagementType` discriminates. Adding a kind is additive — a new `EngagementType` value, not a new type.
Fields 7
engagementType : [EngagementType](https://developers.buffer.com/reference.html#type/EngagementType)!
The kind of engagement this entry configures (comment / mention / directMessage).
media : [MediaConfiguration](https://developers.buffer.com/reference.html#type/MediaConfiguration)!
Media configuration. Always present; `supportsMedia: false` = the platform doesn't deliver attached media to Buffer, so none can be shown.
metadata : [EngagementMetadata](https://developers.buffer.com/reference.html#type/EngagementMetadata)
Optional network-specific engagement metadata (e.g. Google Business). null when none applies.
reactions : [ReactionsConfiguration](https://developers.buffer.com/reference.html#type/ReactionsConfiguration)!
Reactions. Always present; empty `supportedReactions` with `supportsAnyEmoji: false` = reacting via Buffer isn't supported.
replying : [ReplyingConfiguration](https://developers.buffer.com/reference.html#type/ReplyingConfiguration)!
Reply configuration. Always present; `supportsReplying: false` = replying via Buffer not supported.
supportedAiFeatures : [[AiFeature](https://developers.buffer.com/reference.html#type/AiFeature)!]!
AI features supported for this engagement type. Empty when none.
syncData : [SyncDataConfiguration](https://developers.buffer.com/reference.html#type/SyncDataConfiguration)!
Sync configuration — realTime/polling mechanism plus optional forced-sync detail.
TYPE [FacebookMetadata](https://developers.buffer.com/reference.html#type/FacebookMetadata)
Facebook metadata
Fields 1
locationData : [LocationData](https://developers.buffer.com/reference.html#type/LocationData)
Metadata about the location of the business associated with the channel. Only available for Facebook and GPB
TYPE [FeatureAuthorizationStatus](https://developers.buffer.com/reference.html#type/FeatureAuthorizationStatus) ⚠️ Experimental
Pairs a feature with the channel's authorization status for it (token/scope level). One entry per authorization-gated feature the channel exposes.
Fields 3
feature : [Feature](https://developers.buffer.com/reference.html#type/Feature)!
The feature this status describes — a capability a channel can expose, e.g. posting, commenting, mentions, insights, reacting to engagements (see the `Feature` enum).
reason : String
Why the feature is in its current `status`, when a specific cause is known (e.g. the connected platform user lacks rights on the account that owns webhook subscriptions). Informative text for display/support — not a stable machine key, so clients must not parse or switch on it. Null when the status needs no explanation (`ok`) or no specific cause was identified.
status : [AuthorizationStatus](https://developers.buffer.com/reference.html#type/AuthorizationStatus)!
Whether the channel is currently authorized to use `feature`: `ok` (usable), `needsRefresh` (token refresh required), `notEnoughData` (missing scopes / webhook metadata), `needsUpgrade` (client below the minimum version — applies only to the mobile apps), or `notEnoughRights` (the connected platform user's role is insufficient — reconnecting cannot fix it). See the `AuthorizationStatus` enum.
TYPE [ForcedSyncConfiguration](https://developers.buffer.com/reference.html#type/ForcedSyncConfiguration) ⚠️ Experimental
Forced-sync detail. Present only when the kind's sync mechanism supports a forced (manual) sync.
Fields 2
forcedSyncRateLimit : [ForcedSyncRateLimit](https://developers.buffer.com/reference.html#type/ForcedSyncRateLimit)
Rate limit for forced syncs. `null` when forced sync is unthrottled. Reuses the `ForcedSyncRateLimit` type defined by the comment schema.
pollInterval : Int!
How often, in seconds, the channel is automatically polled for new items.
TYPE [ForcedSyncRateLimit](https://developers.buffer.com/reference.html#type/ForcedSyncRateLimit) ⚠️ Experimental
Rate limit configuration for forced sync operations.
Fields 2
allowedAttempts : Int!
Number of allowed forced backfill attempts within the period.
period : Int!
Rate limit period in seconds for forced backfill operations.
TYPE [GoogleBusinessEngagementMetadata](https://developers.buffer.com/reference.html#type/GoogleBusinessEngagementMetadata) ⚠️ Experimental
Google Business-specific engagement metadata. Distinct from the channel-level `GoogleBusinessMetadata` (which carries location data) — this is the engagement surface's rating/note metadata.
Fields 2
hasUserRating : Boolean!
Whether engagements on this channel carry a user star rating.
permanentNote : String!
A permanent note surfaced to the user about this channel's engagements. Empty when there is nothing to tell the user.
TYPE [GoogleBusinessMetadata](https://developers.buffer.com/reference.html#type/GoogleBusinessMetadata)
Google Business metadata
Fields 1
locationData : [LocationData](https://developers.buffer.com/reference.html#type/LocationData)
Metadata about the location of the business associated with the channel. Only available for Facebook and GPB
TYPE [IconVisual](https://developers.buffer.com/reference.html#type/IconVisual) ⚠️ Experimental
Render from the built-in client icon set.
Fields 1
icon : [ReactionIcon](https://developers.buffer.com/reference.html#type/ReactionIcon)!
The built-in icon to render.
TYPE [IdeaMedia](https://developers.buffer.com/reference.html#type/IdeaMedia)
Media attached to an idea
Fields 7
id : ID!
Unique identifier for the media in Buffer's upload system
alt : String
Alternative text description for accessibility
size : Int
File size in bytes
source : [IdeaMediaSource](https://developers.buffer.com/reference.html#type/IdeaMediaSource)
Source platform information for the media
thumbnailUrl : String
URL to a smaller version of the media for preview purposes
type : [MediaType](https://developers.buffer.com/reference.html#type/MediaType)!
Type of media (e.g., image, video, gif)
url : String!
Direct URL to access the media file
TYPE [IdeaMediaSource](https://developers.buffer.com/reference.html#type/IdeaMediaSource)
Media source for the idea, e.g. Unsplash, Gifphy, etc.
Fields 4
id : String
Unique identifier from the source platform
author : String
Name of the content creator/author
authorUrl : String
URL to the author's profile on the source platform
name : String!
Name of the media source platform (e.g., 'Unsplash', 'Giphy')
TYPE [ImageVisual](https://developers.buffer.com/reference.html#type/ImageVisual) ⚠️ Experimental
Render a network-supplied image (e.g. LinkedIn-branded reactions).
Fields 1
url : String!
URL of the network-supplied reaction image.
TYPE [LinkedInMetadata](https://developers.buffer.com/reference.html#type/LinkedInMetadata)
LinkedIn metadata
Fields 1
shouldShowLinkedinAnalyticsRefreshBanner : Boolean!
Property parsed from scopes indicating whether the client should show the LinkedIn analytics refresh banner
TYPE [LinkShorteningConfig](https://developers.buffer.com/reference.html#type/LinkShorteningConfig)
Link Shortening Configuration
Fields 2
domain : String!
Domain of the link shortener - eg buff.ly, dub.co, or the user's custom domain.
name : String!
Human readable string to describe the link shortening service.
TYPE [LocationData](https://developers.buffer.com/reference.html#type/LocationData)
Location data about the channel
Fields 3
googleAccountId : String
Google Account Id of the business
location : String
Location of the business associated with the channel
mapsLink : String
Link to the map
TYPE [MastodonMetadata](https://developers.buffer.com/reference.html#type/MastodonMetadata)
Mastodon metadata
Fields 2
maxCharacters : Int!
Maximum character limit allowed for this channel's server instance
serverUrl : String!
The instance of mastodon of the channel
TYPE [MediaConfiguration](https://developers.buffer.com/reference.html#type/MediaConfiguration) ⚠️ Experimental
Media configuration for an engagement type — whether media attached to an engagement reaches Buffer and can therefore be shown to the user.
Fields 3
additionalInformation : String
User-facing explanation of what the client can do about the missing media, worded for the platform (e.g. "Instagram doesn't send media with mentions to Buffer. Open the mention natively to see the full content."). Display text only — not a stable machine key, so clients must not parse or switch on it. Null when `supportsMedia` is true.
disclaimer : String
User-facing explanation of why media isn't shown. Display text only — not a stable machine key, so clients must not parse or switch on it. Null when `supportsMedia` is true.
supportsMedia : Boolean!
Whether media attached to this engagement type is delivered by the platform and can be shown.
TYPE [PinterestBoard](https://developers.buffer.com/reference.html#type/PinterestBoard)
A Pinterest board
Fields 6
id : String!
The ID of the board
avatar : String
The board avatar
description : String
The board description
name : String!
The board name
serviceId : String!
The ID of the service
url : String!
The board URL
TYPE [PinterestMetadata](https://developers.buffer.com/reference.html#type/PinterestMetadata)
Pinterest metadata
Fields 1
boards : [[PinterestBoard](https://developers.buffer.com/reference.html#type/PinterestBoard)!]!
The list of boards the user has on Pinterest
TYPE [PostChannelNotFoundError](https://developers.buffer.com/reference.html#type/PostChannelNotFoundError) ⚠️ Experimental
The channel targeted by a single post in the promoteContentItemDraftToPosts input list was not found or is not accessible.
Fields 2
channelId : [ChannelId](https://developers.buffer.com/reference.html#type/ChannelId)!
Channel targeted by the failing post.
message : String!
Error message.
TYPE [ReactionsConfiguration](https://developers.buffer.com/reference.html#type/ReactionsConfiguration) ⚠️ Experimental
Reactions configuration. `restingIcon` is always populated; `supportedReactions` empty = reacting via Buffer isn't supported (unless `supportsAnyEmoji`), one = single-button liking, multiple = a reaction set.
Fields 4
requiresAuthorization : Boolean!
Whether reacting needs an OAuth scope beyond the ones a base connection grants. When true, check the channel's `engagementReaction` entry in `authorizationStatus` before offering the reaction — the channel may need a reconnect to grant it. On the service-level catalog this is channel-agnostic and may overstate the requirement, since it can vary with a channel's login flow; the per-channel configuration resolves it exactly.
restingIcon : [ReactionIcon](https://developers.buffer.com/reference.html#type/ReactionIcon)!
The resting-state icon — the pre-reaction icon.
supportedReactions : [[EngagementSupportedReaction](https://developers.buffer.com/reference.html#type/EngagementSupportedReaction)!]!
The reactions the user can apply. Empty when reacting via Buffer isn't supported, or when `supportsAnyEmoji` is true.
supportsAnyEmoji : Boolean!
Whether the user can react with any single emoji (e.g. direct messages). When true, offer an emoji picker and send the chosen emoji to the network's emoji reaction mutation; `supportedReactions` is empty.
TYPE [ReplyingConfiguration](https://developers.buffer.com/reference.html#type/ReplyingConfiguration) ⚠️ Experimental
Reply configuration for an engagement type. A rich object (not a bare boolean) so reply metadata can be added later.
Fields 3
prefixReplyWithMention : Boolean!
Whether replies should be prefixed with the author's @mention.
supportsReplying : Boolean!
Whether replying to this engagement type via Buffer is supported.
supportsReplyTo : Boolean!
Whether a reply can quote a specific message.
TYPE [ScheduleV2](https://developers.buffer.com/reference.html#type/ScheduleV2)
Posting schedule for a specific day of the week
Fields 3
day : [DayOfWeek](https://developers.buffer.com/reference.html#type/DayOfWeek)!
The day of the week: mon, tue, wed, thu, fri, sat, sun
paused : Boolean!
Indicates if this day is paused in the posting schedule.
times : [String!]!
The times the channel is scheduled to post on the day: HH:MM
TYPE [SyncDataConfiguration](https://developers.buffer.com/reference.html#type/SyncDataConfiguration) ⚠️ Experimental
Sync configuration for an engagement type — the realTime/polling `syncDataMechanism` plus optional forced-sync detail.
Fields 2
forcedSyncConfiguration : [ForcedSyncConfiguration](https://developers.buffer.com/reference.html#type/ForcedSyncConfiguration)
Forced-sync detail. A forced sync is a user-triggered (manual) refresh that fetches new items on demand instead of waiting for the next scheduled poll or push. `null` when this kind's sync mechanism has no forced-sync support.
syncDataMechanism : [SyncDataMechanism](https://developers.buffer.com/reference.html#type/SyncDataMechanism)!
How this engagement type syncs on this channel: `realTime` (push) or `polling` (pull).
TYPE [TiktokMetadata](https://developers.buffer.com/reference.html#type/TiktokMetadata)
Tiktok metadata
Fields 1
defaultToReminders : Boolean!
Indicates if we should default to reminder for Tiktok
TYPE [TwitterMetadata](https://developers.buffer.com/reference.html#type/TwitterMetadata)
Twitter metadata
Fields 1
subscriptionType : String
Indicates the type of subscription the user has on Twitter
TYPE [WhatsAppMetadata](https://developers.buffer.com/reference.html#type/WhatsAppMetadata)
The WhatsApp phone's connection details, without credentials or synchronization request IDs.
Fields 4
businessPortfolioId : String!
The Meta business portfolio that owns the WhatsApp Business Account.
lastSubscribedAt : [DateTime](https://developers.buffer.com/reference.html#type/DateTime)
When Buffer last confirmed the WABA subscription. Null before confirmation.
phoneNumberId : String!
Meta's ID for the business phone.
wabaId : String!
The WhatsApp Business Account that owns the phone.
TYPE [YoutubeMetadata](https://developers.buffer.com/reference.html#type/YoutubeMetadata)
Youtube metadata
Fields 1
defaultToReminders : Boolean!
Indicates if we should default to reminder for Youtube
TYPE [ValidationRule](https://developers.buffer.com/reference.html#type/ValidationRule) ⚠️ Experimental
A validation rule constraining how a content property may be used. Each concrete rule carries only the fields it needs; new constraint kinds are additive (a new type implementing this interface). Clients switch on `__typename`.
Fields 1
property : [ContentProperty](https://developers.buffer.com/reference.html#type/ContentProperty)!
The content property this rule constrains.
TYPE [ChannelMetadata](https://developers.buffer.com/reference.html#type/ChannelMetadata)
Metadata or settings about the channel depending on the service type
TYPE [EngagementMetadata](https://developers.buffer.com/reference.html#type/EngagementMetadata) ⚠️ Experimental
Network-specific engagement metadata. Single-member union for now; grows additively as more networks contribute their own shape.
TYPE [ReactionVisual](https://developers.buffer.com/reference.html#type/ReactionVisual) ⚠️ Experimental
How to render a reaction. The client switches on `__typename` purely as a render strategy (built-in icon vs network image) — never on the network or the reaction identity.
### Inputs 5
INPUT [ChannelInput](https://developers.buffer.com/reference.html#type/ChannelInput)
Input for the channel query
Fields 1
id : [ChannelId](https://developers.buffer.com/reference.html#type/ChannelId)!
The ID of the channel to be retrieved
INPUT [ChannelsFiltersInput](https://developers.buffer.com/reference.html#type/ChannelsFiltersInput)
Filter to pass when fetching channels.
Fields 2
isLocked : Boolean
If not defined, it returns all channels Else, if true, it only returns locked channels if false, it only returns not locked channels
product : [Product](https://developers.buffer.com/reference.html#type/Product)
If not passed, it return all channels Else, it filters the channels based on what the product supports.
INPUT [ChannelsInput](https://developers.buffer.com/reference.html#type/ChannelsInput)
Input to pass when fetching channels.
Fields 2
filter : [ChannelsFiltersInput](https://developers.buffer.com/reference.html#type/ChannelsFiltersInput)
A list of option filters - passing null means we don't want to filter
organizationId : [OrganizationId](https://developers.buffer.com/reference.html#type/OrganizationId)!
The Organization id to fetch channels for
INPUT [IdeaMediaInput](https://developers.buffer.com/reference.html#type/IdeaMediaInput)
Fields 6
url : String!
The URL of the media
alt : String
Alternative text for the media
thumbnailUrl : String
Thumbnail URL for the media
type : [MediaType](https://developers.buffer.com/reference.html#type/MediaType)!
The type of media (image, gif, video, link, document, unsupported). Note: 'video' is not supported via public API
size : Int
The size of the media in bytes
source : [IdeaMediaSourceInput](https://developers.buffer.com/reference.html#type/IdeaMediaSourceInput)
Source information for the media
INPUT [IdeaMediaSourceInput](https://developers.buffer.com/reference.html#type/IdeaMediaSourceInput)
Input type for the source information of media attached to an idea
Fields 5
name : String!
id : String
trigger : String
author : String
for unsplash only
authorUrl : String
### Enums 16
ENUM [AiFeature](https://developers.buffer.com/reference.html#type/AiFeature) ⚠️ Experimental
AI features supported for an engagement type. Grows additively.
ENUM [AuthorizationStatus](https://developers.buffer.com/reference.html#type/AuthorizationStatus) ⚠️ Experimental
Represents the authorization evaluation result for a feature.
ENUM [ChannelAction](https://developers.buffer.com/reference.html#type/ChannelAction)
List of possible actions that can be performed on a Channel
ENUM [ChannelType](https://developers.buffer.com/reference.html#type/ChannelType)
Channel is a representation of a social media account or page that can be connected to Buffer.
ENUM [ConfigurationContentType](https://developers.buffer.com/reference.html#type/ConfigurationContentType) ⚠️ Experimental
The kinds of content a channel can compose. Grows additively.
ENUM [ContentProperty](https://developers.buffer.com/reference.html#type/ContentProperty) ⚠️ Experimental
A property a content type can carry. Support is expressed by inclusion in `supportedProperties` — there are no exclusion lists. Grows additively.
ENUM [DayOfWeek](https://developers.buffer.com/reference.html#type/DayOfWeek)
Day of the week.
ENUM [EngagementType](https://developers.buffer.com/reference.html#type/EngagementType) ⚠️ Experimental
Discriminator used in inputs/filters to scope a query to specific types.
ENUM [Feature](https://developers.buffer.com/reference.html#type/Feature) ⚠️ Experimental
A capability a channel can expose, spanning every domain. The shared key for per-channel `authorizationStatus`. Grows additively.
ENUM [MediaFormat](https://developers.buffer.com/reference.html#type/MediaFormat) ⚠️ Experimental
Media formats a `FormatRule` can allow-list. Grows additively.
ENUM [MediaType](https://developers.buffer.com/reference.html#type/MediaType)
The type of media attached to a post
ENUM [Product](https://developers.buffer.com/reference.html#type/Product)
Buffer products, buffer is used as all products
ENUM [ReactionIcon](https://developers.buffer.com/reference.html#type/ReactionIcon) ⚠️ Experimental
Standard reaction icon set used by `IconVisual`. Grows additively.
ENUM [ReactionType](https://developers.buffer.com/reference.html#type/ReactionType) ⚠️ Experimental
Types of reactions that can be applied to a comment.
ENUM [Service](https://developers.buffer.com/reference.html#type/Service)
The list of services that can be authorized.
ENUM [SyncDataMechanism](https://developers.buffer.com/reference.html#type/SyncDataMechanism) ⚠️ Experimental
How items of an engagement type are pulled / pushed. `realTime` covers push (webhook / firehose); `polling` is pull.
### Scalars 1
SCALAR [ChannelId](https://developers.buffer.com/reference.html#type/ChannelId)
The `ChannelId` scalar represents the ID of a Buffer Channel
## Tags
### Queries 2
QUERY tag (input: [TagByIdInput](https://developers.buffer.com/reference.html#type/TagByIdInput)!) : [Tag](https://developers.buffer.com/reference.html#type/Tag) ⚠️ Experimental
Fetch a single tag by id.
Resolves to null with a NOT_FOUND error when no tag has that id, and with an UNAUTHORIZED error when the tag belongs to an organization the caller cannot read. Both are reported in the errors array.
This API is an early preview and can change without a deprecation period.
Arguments  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| input Required  |  [TagByIdInput](https://developers.buffer.com/reference.html#type/TagByIdInput)!  |  Identifies the tag to fetch.   |  
Example Response

```
{
  "data": {
    "tag": {
      "id": "...",
      "color": "...",
      "colorName": "blue",
      "isLocked": true
    }
  }
}
```

QUERY tagsV2 (after: String, first: Int, input: [TagsInput](https://developers.buffer.com/reference.html#type/TagsInput)!) : [TagsConnection](https://developers.buffer.com/reference.html#type/TagsConnection)! ⚠️ Experimental
Fetch a page of the organization's tags, sorted by name in ascending order. Uses standard cursor pagination: pass the previous page's `pageInfo.endCursor` as `after` to fetch the next page. Requesting more than 100 tags in a single page is rejected.
This API is an early preview and can change without a deprecation period.
Arguments  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| after Optional  | String  |  The cursor after which to return results. Cursors are opaque: treat them as a black box and reset to null when the input changes, since a cursor from a different result set produces undefined behavior.   |  
| first Optional  | Int  |  The number of tags to return, up to 100.   |  
| input Required  |  [TagsInput](https://developers.buffer.com/reference.html#type/TagsInput)!  |  Identifies the organization whose tags to list, and how to filter them.   |  
Example Response

```
{
  "data": {
    "tagsV2": {
      "edges": [
        {
          "cursor": "...",
          "node": {}
        }
      ],
      "pageInfo": {
        "endCursor": "...",
        "hasNextPage": true,
        "hasPreviousPage": true,
        "startCursor": "..."
      },
      "totalCount": 0
    }
  }
}
```

### Mutations 3
MUTATION createTag (input: [CreateTagInput](https://developers.buffer.com/reference.html#type/CreateTagInput)!) : [CreateTagPayload](https://developers.buffer.com/reference.html#type/CreateTagPayload)! ⚠️ Experimental
Create a tag for an organization.
The name must be unique within the organization; a duplicate is refused with `DuplicateError`. Creation is refused with `LimitReachedError` once the organization already holds as many tags as its plan allows.
This API is an early preview and can change without a deprecation period.
Arguments  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| input Required  |  [CreateTagInput](https://developers.buffer.com/reference.html#type/CreateTagInput)!  |  Identifies the organization to create the tag in, and the name and color to give the tag.   |  
Example Response

```
{
  "data": {
    "createTag": {}
  }
}
```

MUTATION deleteTag (input: [DeleteTagInput](https://developers.buffer.com/reference.html#type/DeleteTagInput)!) : [DeleteTagPayload](https://developers.buffer.com/reference.html#type/DeleteTagPayload)! ⚠️ Experimental
Delete a tag.
The tag is removed from every post, idea and content item carrying it; those items are otherwise untouched. A locked tag can be deleted, and deleting an unlocked tag frees a slot for the oldest locked one. See `Tag.isLocked`.
This API is an early preview and can change without a deprecation period.
Arguments  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| input Required  |  [DeleteTagInput](https://developers.buffer.com/reference.html#type/DeleteTagInput)!  |  Identifies the tag to delete.   |  
Example Response

```
{
  "data": {
    "deleteTag": {}
  }
}
```

MUTATION updateTag (input: [UpdateTagInput](https://developers.buffer.com/reference.html#type/UpdateTagInput)!) : [UpdateTagPayload](https://developers.buffer.com/reference.html#type/UpdateTagPayload)! ⚠️ Experimental
Update a tag's name and color.
Both values are replaced, so send the current value for the one you are not changing. The new name must still be unique within the organization; a duplicate is refused with `DuplicateError`.
A locked tag cannot be edited and the update is refused. See `Tag.isLocked`.
This API is an early preview and can change without a deprecation period.
Arguments  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| input Required  |  [UpdateTagInput](https://developers.buffer.com/reference.html#type/UpdateTagInput)!  |  Identifies the tag to update, and the name and color to set on it.   |  
Example Response

```
{
  "data": {
    "updateTag": {}
  }
}
```

### Outputs 2
OUTPUT [Tag](https://developers.buffer.com/reference.html#type/Tag)
A label an organization applies to posts and ideas so they can be grouped and filtered together. Tags belong to the organization and are shared by everyone in it, rather than being per channel or per person.
Fields 5
id : [TagId](https://developers.buffer.com/reference.html#type/TagId)!
The tag's unique identifier.
color : String!
The tag's color as a hex triplet, for example `#F523F1`. Use `colorName` where you need a stable identifier rather than a literal color.
colorName : [TagColorName](https://developers.buffer.com/reference.html#type/TagColorName)
Stable Buffer palette identifier derived from `color`. Clients should map this value to platform- and theme-specific presentation, falling back to `color` when this field is null or unsupported. Returns null for custom or unrecognized colors.
isLocked : Boolean!
Whether the tag is locked. A tag locks when the organization holds more tags than its plan allows, typically after a downgrade. Buffer locks the excess rather than deleting it, so nothing is lost if the organization upgrades again. A locked tag **cannot be edited** — `updateTag` rejects it. It can still be read, deleted, and applied to posts through the API. Buffer's own apps also hide locked tags when picking a tag for a post; that is a client convention, not something the API enforces. Locking is recalculated when the organization's plan changes, and deleting an unlocked tag frees a slot for the oldest locked one.
name : String!
The tag's display name, for example `Summer sales`.
OUTPUT [TagsConnection](https://developers.buffer.com/reference.html#type/TagsConnection) ⚠️ Experimental
A page of an organization's tags.
Fields 3
edges : [[TagEdge](https://developers.buffer.com/reference.html#type/TagEdge)!]!
The list of tag edges.
pageInfo : [PaginationPageInfo](https://developers.buffer.com/reference.html#type/PaginationPageInfo)!
Pagination information for the connection.
totalCount : Int!
The total number of tags matching the request, across every page.
### Types 2
TYPE [TagActionSuccess](https://developers.buffer.com/reference.html#type/TagActionSuccess) ⚠️ Experimental
Returned when a tag was created or updated successfully.
Fields 1
tag : [Tag](https://developers.buffer.com/reference.html#type/Tag)!
The tag as persisted, read back after the write.
TYPE [TagEdge](https://developers.buffer.com/reference.html#type/TagEdge) ⚠️ Experimental
An edge in a tag connection.
Fields 2
cursor : String!
A cursor for pagination.
node : [Tag](https://developers.buffer.com/reference.html#type/Tag)!
The tag at the end of the edge.
### Inputs 7
INPUT [TagByIdInput](https://developers.buffer.com/reference.html#type/TagByIdInput) ⚠️ Experimental
Input for fetching a single tag by id.
Fields 1
id : [TagId](https://developers.buffer.com/reference.html#type/TagId)!
The unique identifier of the tag to fetch.
INPUT [TagComparator](https://developers.buffer.com/reference.html#type/TagComparator)
Comparator for filtering by tags
Fields 2
in : [[TagId](https://developers.buffer.com/reference.html#type/TagId)!]!
Include results that have any of the specified tags (union/OR).
isEmpty : Boolean!
When true, include results that have no tags assigned. Can be combined with 'in' for union filtering. Defaults to false if not specified.
INPUT [TagInput](https://developers.buffer.com/reference.html#type/TagInput)
Input type for tag information used in idea creation
Fields 3
id : ID!
name : String!
color : String!
INPUT [TagsFiltersInput](https://developers.buffer.com/reference.html#type/TagsFiltersInput) ⚠️ Experimental
Filters for listing an organization's tags. Omitted fields do not filter.
Fields 1
isLocked : Boolean
Return only locked tags when true, only unlocked tags when false. Omit to return both. See `Tag.isLocked` for what locking means.
INPUT [TagsInput](https://developers.buffer.com/reference.html#type/TagsInput) ⚠️ Experimental
Input for listing an organization's tags.
Fields 2
filter : [TagsFiltersInput](https://developers.buffer.com/reference.html#type/TagsFiltersInput)
Filters to apply. When omitted, all of the organization's tags are returned.
organizationId : [OrganizationId](https://developers.buffer.com/reference.html#type/OrganizationId)!
Organization to list tags for. The caller must be a member of this organization.
INPUT [TagToCreateInput](https://developers.buffer.com/reference.html#type/TagToCreateInput) ⚠️ Experimental
The name and color to give a new tag.
Fields 2
color : String!
The tag's color as a hex triplet: `#` followed by exactly six hex digits, for example `#F523F1`. Shorthand such as `#F51` is rejected. Buffer maps recognized palette colors onto `Tag.colorName`.
name : String!
The tag's display name, for example `Summer sales`. Between 1 and 100 characters, and unique within the organization. Names are compared exactly, so `Summer sales` and `summer sales` can coexist.
INPUT [TagToUpdateInput](https://developers.buffer.com/reference.html#type/TagToUpdateInput) ⚠️ Experimental
The name and color to set on an existing tag. Both are replaced, so send the current value for the one you are not changing.
Fields 2
color : String!
The tag's color as a hex triplet: `#` followed by exactly six hex digits, for example `#F523F1`. Shorthand such as `#F51` is rejected. Buffer maps recognized palette colors onto `Tag.colorName`.
name : String!
The tag's display name, for example `Summer sales`. Between 1 and 100 characters, and unique within the organization. Names are compared exactly, so `Summer sales` and `summer sales` can coexist.
### Enums 1
ENUM [TagColorName](https://developers.buffer.com/reference.html#type/TagColorName)
Stable Buffer identifiers for the supported tag color palette. Clients map these values to platform- and theme-specific presentation. Values ending in `Light` are lighter palette variants, not UI theme modes.
### Scalars 1
SCALAR [TagId](https://developers.buffer.com/reference.html#type/TagId)
The `TagId` scalar represents the ID of a Buffer Tag
## Posts
### Queries 11
QUERY aggregatedPostMetrics (input: [AggregatedPostMetricsInput](https://developers.buffer.com/reference.html#type/AggregatedPostMetricsInput)!) : [AggregatedPostMetrics](https://developers.buffer.com/reference.html#type/AggregatedPostMetrics)!
Aggregate normalized post metrics across a filtered post set. Useful for yearly summaries, channel-level rollups, and BI exports without paginating through thousands of posts.
For per-post metrics, use `posts(input)` or `post(input)` with a `metrics { … }` selection — this query is purely for aggregation.
The result always contains a baseline trio of entries: `postCount` (number of matched posts in the window), `reactions`, and `comments`. Posts on networks that don't track reactions or comments contribute 0 to those totals.
Beyond the baseline, additional metric types are returned only when every channel in the filter set supports them. A single-network filter surfaces that network's richer metrics (e.g. impressions, reach, engagementRate on LinkedIn); a mixed-network filter trims the extras to those common to every network in the set.
Arguments  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| input Required  |  [AggregatedPostMetricsInput](https://developers.buffer.com/reference.html#type/AggregatedPostMetricsInput)!  |  Query's input: organization, date range, optional channel and tag filters. Date range is capped to 365 days.   |  
Example Response

```
{
  "data": {
    "aggregatedPostMetrics": {
      "metrics": [
        {
          "description": "...",
          "name": "...",
          "type": "averageTimeWatched",
          "unit": "count"
        }
      ],
      "metricsUpdatedAt": "..."
    }
  }
}
```

QUERY dailyPostingLimits (input: [DailyPostingLimitsInput](https://developers.buffer.com/reference.html#type/DailyPostingLimitsInput)!) : [[DailyPostingLimitStatus](https://developers.buffer.com/reference.html#type/DailyPostingLimitStatus)!]!
Returns posting limit status for the given channels at the intended posting time.
Arguments  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| input Required  |  [DailyPostingLimitsInput](https://developers.buffer.com/reference.html#type/DailyPostingLimitsInput)!  |  Query's input.   |  
Example Response

```
{
  "data": {
    "dailyPostingLimits": [
      {
        "channelId": "...",
        "isAtLimit": true,
        "limit": 0,
        "scheduled": 0
      }
    ]
  }
}
```

QUERY instagramAudio (input: [InstagramAudioInput](https://developers.buffer.com/reference.html#type/InstagramAudioInput)!) : [InstagramAudioPayload](https://developers.buffer.com/reference.html#type/InstagramAudioPayload)! ⚠️ Experimental
Refresh metadata and preview availability for one Instagram audio asset. Requires Facebook Login. Instagram Login channels return ChannelRefreshRequired.
Arguments  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| input Required  |  [InstagramAudioInput](https://developers.buffer.com/reference.html#type/InstagramAudioInput)!  |  Channel and audio asset used to refresh metadata.   |  
Example Response

```
{
  "data": {
    "instagramAudio": {}
  }
}
```

QUERY instagramAudioCatalog (input: [InstagramAudioCatalogInput](https://developers.buffer.com/reference.html#type/InstagramAudioCatalogInput)!) : [InstagramAudioCatalogPayload](https://developers.buffer.com/reference.html#type/InstagramAudioCatalogPayload)! ⚠️ Experimental
Return trending music and original sounds in a single request. Requires Facebook Login. Instagram Login channels return ChannelRefreshRequired.
Arguments  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| input Required  |  [InstagramAudioCatalogInput](https://developers.buffer.com/reference.html#type/InstagramAudioCatalogInput)!  |  Channel to load trending audio for. No catalog selection is needed.   |  
Example Response

```
{
  "data": {
    "instagramAudioCatalog": {}
  }
}
```

QUERY post (input: [PostInput](https://developers.buffer.com/reference.html#type/PostInput)!) : [Post](https://developers.buffer.com/reference.html#type/Post)!
Fetches a post by PostID for the given organization: first and last can be set for forward pagination using Relay convention
Arguments  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| input Required  |  [PostInput](https://developers.buffer.com/reference.html#type/PostInput)!  |  Query's input.   |  
Example Response

```
{
  "data": {
    "post": {
      "id": "...",
      "allowedActions": [
        "addPostNote"
      ],
      "assets": [
        {
          "id": "...",
          "mimeType": "...",
          "source": "...",
          "thumbnail": "..."
        }
      ],
      "author": {
        "id": "...",
        "avatar": "...",
        "email": "...",
        "isDeleted": true
      }
    }
  }
}
```

QUERY posts (after: String, first: Int, input: [PostsInput](https://developers.buffer.com/reference.html#type/PostsInput)!) : [PostsResults](https://developers.buffer.com/reference.html#type/PostsResults)!
Fetches posts for the given organization: first and last can be set for forward pagination using Relay convention
Arguments  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| after Optional  | String  |  The cursor of the post to start fetching from   |  
| first Optional  | Int  |  The number of posts to return   |  
| input Required  |  [PostsInput](https://developers.buffer.com/reference.html#type/PostsInput)!  |  Query's input.   |  
Example Response

```
{
  "data": {
    "posts": {
      "edges": [
        {
          "cursor": "...",
          "node": {}
        }
      ],
      "pageInfo": {
        "endCursor": "...",
        "hasNextPage": true,
        "hasPreviousPage": true,
        "startCursor": "..."
      }
    }
  }
}
```

QUERY postTemplate (input: [PostTemplateInput](https://developers.buffer.com/reference.html#type/PostTemplateInput)!) : [PostTemplate](https://developers.buffer.com/reference.html#type/PostTemplate) 🧪 Preview
Fetch a single post template by ID. Returns null if not found.
Arguments  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| input Required  |  [PostTemplateInput](https://developers.buffer.com/reference.html#type/PostTemplateInput)!  |  Input for fetching a single post template.   |  
Example Response

```
{
  "data": {
    "postTemplate": {
      "id": "...",
      "body": "...",
      "description": "...",
      "emoji": "..."
    }
  }
}
```

QUERY postTemplates (after: String, first: Int, input: [PostTemplatesInput](https://developers.buffer.com/reference.html#type/PostTemplatesInput)!) : [PostTemplatesConnection](https://developers.buffer.com/reference.html#type/PostTemplatesConnection)! 🧪 Preview
Fetch the templates visible to the current actor for the template library: public templates, plus internal templates from the supplied `organizationId`, plus private templates owned by the actor's account. The visibility scope is always pinned to the actor and the supplied organization — the input filter can only narrow within that scope, never widen it.
Arguments  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| after Optional  | String  |  The cursor after which to return results.   |  
| first Optional  | Int  |  The number of templates to return.   |  
| input Required  |  [PostTemplatesInput](https://developers.buffer.com/reference.html#type/PostTemplatesInput)!  |  Input containing the organization scope and optional filters.   |  
Example Response

```
{
  "data": {
    "postTemplates": {
      "edges": [
        {
          "cursor": "...",
          "node": {}
        }
      ],
      "pageInfo": {
        "endCursor": "...",
        "hasNextPage": true,
        "hasPreviousPage": true,
        "startCursor": "..."
      },
      "totalCount": 0
    }
  }
}
```

QUERY searchInstagramAudio (input: [SearchInstagramAudioInput](https://developers.buffer.com/reference.html#type/SearchInstagramAudioInput)!) : [SearchInstagramAudioPayload](https://developers.buffer.com/reference.html#type/SearchInstagramAudioPayload)! ⚠️ Experimental
Search Instagram audio for one channel. Requires Facebook Login. Instagram Login channels return ChannelRefreshRequired.
Arguments  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| input Required  |  [SearchInstagramAudioInput](https://developers.buffer.com/reference.html#type/SearchInstagramAudioInput)!  |  Channel, catalog type, and search text.   |  
Example Response

```
{
  "data": {
    "searchInstagramAudio": {}
  }
}
```

QUERY searchInstagramAudioCatalog (input: [SearchInstagramAudioCatalogInput](https://developers.buffer.com/reference.html#type/SearchInstagramAudioCatalogInput)!) : [InstagramAudioCatalogPayload](https://developers.buffer.com/reference.html#type/InstagramAudioCatalogPayload)! ⚠️ Experimental
Search music and original sounds in a single request. Requires Facebook Login. Instagram Login channels return ChannelRefreshRequired.
Arguments  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| input Required  |  [SearchInstagramAudioCatalogInput](https://developers.buffer.com/reference.html#type/SearchInstagramAudioCatalogInput)!  |  Channel and nonblank search text. No catalog selection is needed.   |  
Example Response

```
{
  "data": {
    "searchInstagramAudioCatalog": {}
  }
}
```

QUERY trendingInstagramAudio (input: [TrendingInstagramAudioInput](https://developers.buffer.com/reference.html#type/TrendingInstagramAudioInput)!) : [SearchInstagramAudioPayload](https://developers.buffer.com/reference.html#type/SearchInstagramAudioPayload)! ⚠️ Experimental
Return Meta trending Instagram audio for one channel. Requires Facebook Login. Instagram Login channels return ChannelRefreshRequired.
Arguments  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| input Required  |  [TrendingInstagramAudioInput](https://developers.buffer.com/reference.html#type/TrendingInstagramAudioInput)!  |  Channel and catalog type for Meta trending audio.   |  
Example Response

```
{
  "data": {
    "trendingInstagramAudio": {}
  }
}
```

### Mutations 13
MUTATION addPostToContentItem (input: [AddPostToContentItemInput](https://developers.buffer.com/reference.html#type/AddPostToContentItemInput)!) : [AddPostToContentItemPayload](https://developers.buffer.com/reference.html#type/AddPostToContentItemPayload)! ⚠️ Experimental
Add a post that already exists to a content item. The mutation creates no post. To add a new post, call createPost first.
Arguments  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| input Required  |  [AddPostToContentItemInput](https://developers.buffer.com/reference.html#type/AddPostToContentItemInput)!  |  Input for addPostToContentItem.   |  
Example Response

```
{
  "data": {
    "addPostToContentItem": {}
  }
}
```

MUTATION createPost (input: [CreatePostInput](https://developers.buffer.com/reference.html#type/CreatePostInput)!) : [PostActionPayload](https://developers.buffer.com/reference.html#type/PostActionPayload)!
Create post for channel
Arguments  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| input Required  |  [CreatePostInput](https://developers.buffer.com/reference.html#type/CreatePostInput)!  |  The mutation's input   |  
Example Response

```
{
  "data": {
    "createPost": {}
  }
}
```

MUTATION createPostTemplate (input: [CreatePostTemplateInput](https://developers.buffer.com/reference.html#type/CreatePostTemplateInput)!) : [CreatePostTemplatePayload](https://developers.buffer.com/reference.html#type/CreatePostTemplatePayload)! 🧪 Preview
Create a post template visible only to the caller (`private`) or to the caller's organization (`internal`).
Arguments  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| input Required  |  [CreatePostTemplateInput](https://developers.buffer.com/reference.html#type/CreatePostTemplateInput)!  |  Input for creating a post template.   |  
Example Response

```
{
  "data": {
    "createPostTemplate": {}
  }
}
```

MUTATION deletePost (input: [DeletePostInput](https://developers.buffer.com/reference.html#type/DeletePostInput)!) : [DeletePostPayload](https://developers.buffer.com/reference.html#type/DeletePostPayload)!
Delete a post by id.
Arguments  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| input Required  |  [DeletePostInput](https://developers.buffer.com/reference.html#type/DeletePostInput)!  |  Input for the deletePost mutation.   |  
Example Response

```
{
  "data": {
    "deletePost": {}
  }
}
```

MUTATION deletePostTemplate (input: [DeletePostTemplateInput](https://developers.buffer.com/reference.html#type/DeletePostTemplateInput)!) : [DeletePostTemplatePayload](https://developers.buffer.com/reference.html#type/DeletePostTemplatePayload)! 🧪 Preview
Delete a post template owned by the caller (or an internal template in the caller's organization, if the caller is an org admin/owner).
Arguments  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| input Required  |  [DeletePostTemplateInput](https://developers.buffer.com/reference.html#type/DeletePostTemplateInput)!  |  Input for deleting a post template.   |  
Example Response

```
{
  "data": {
    "deletePostTemplate": {}
  }
}
```

MUTATION editPost (input: [EditPostInput](https://developers.buffer.com/reference.html#type/EditPostInput)!) : [PostActionPayload](https://developers.buffer.com/reference.html#type/PostActionPayload)!
Edit post for channel
Arguments  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| input Required  |  [EditPostInput](https://developers.buffer.com/reference.html#type/EditPostInput)!  |  The mutation's input   |  
Example Response

```
{
  "data": {
    "editPost": {}
  }
}
```

MUTATION movePostInQueue (input: [MovePostInQueueInput](https://developers.buffer.com/reference.html#type/MovePostInQueueInput)!) : [MovePostInQueuePayload](https://developers.buffer.com/reference.html#type/MovePostInQueuePayload)! ⚠️ Experimental
Move a queued post to the top or bottom of its channel's queue. Unlike editPost, this is a scheduling-only operation that never re-validates the post's content.
Arguments  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| input Required  |  [MovePostInQueueInput](https://developers.buffer.com/reference.html#type/MovePostInQueueInput)!  |  The mutation's input   |  
Example Response

```
{
  "data": {
    "movePostInQueue": {}
  }
}
```

MUTATION promoteContentItemDraftToPosts (input: [PromoteContentItemDraftToPostsInput](https://developers.buffer.com/reference.html#type/PromoteContentItemDraftToPostsInput)!) : [PromoteContentItemDraftToPostsPayload](https://developers.buffer.com/reference.html#type/PromoteContentItemDraftToPostsPayload)! ⚠️ Experimental
Promote a channel-less draft into channel-specific posts. One-way: once promoted, the content item can no longer be edited as a draft. If any post fails validation, none are created. A failure can also be reported when a post could not be fully processed after the promotion already took effect; re-fetch the content item to check its state before retrying.
This API is an early preview and can change without a deprecation period.
Arguments  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| input Required  |  [PromoteContentItemDraftToPostsInput](https://developers.buffer.com/reference.html#type/PromoteContentItemDraftToPostsInput)!  |  Input for promoteContentItemDraftToPosts.   |  
Example Response

```
{
  "data": {
    "promoteContentItemDraftToPosts": {}
  }
}
```

MUTATION removePostFromContentItem (input: [RemovePostFromContentItemInput](https://developers.buffer.com/reference.html#type/RemovePostFromContentItemInput)!) : [RemovePostFromContentItemPayload](https://developers.buffer.com/reference.html#type/RemovePostFromContentItemPayload)! ⚠️ Experimental
Remove a post from a content item. The post survives on its own channel and keeps its schedule, text, status, and tags. Only the link to the content item goes away. To delete a post, call deletePost.
A second call with a post that belongs to no content item changes nothing, and the mutation reports success.
Arguments  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| input Required  |  [RemovePostFromContentItemInput](https://developers.buffer.com/reference.html#type/RemovePostFromContentItemInput)!  |  Input for removePostFromContentItem.   |  
Example Response

```
{
  "data": {
    "removePostFromContentItem": {}
  }
}
```

MUTATION updateContentItem (input: [UpdateContentItemInput](https://developers.buffer.com/reference.html#type/UpdateContentItemInput)!) : [UpdateContentItemPayload](https://developers.buffer.com/reference.html#type/UpdateContentItemPayload)! ⚠️ Experimental
Update a content item's title or target date. Fields that are omitted keep their current value.
This API is an early preview and can change without a deprecation period.
Arguments  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| input Required  |  [UpdateContentItemInput](https://developers.buffer.com/reference.html#type/UpdateContentItemInput)!  |  Input for updateContentItem.   |  
Example Response

```
{
  "data": {
    "updateContentItem": {}
  }
}
```

MUTATION updateContentItemDraft (input: [UpdateContentItemDraftInput](https://developers.buffer.com/reference.html#type/UpdateContentItemDraftInput)!) : [UpdateContentItemDraftPayload](https://developers.buffer.com/reference.html#type/UpdateContentItemDraftPayload)! ⚠️ Experimental
Replace a channel-less draft's content in full, and optionally set the content item's target date in the same write. The draft needs text or at least one asset. Only valid while the content item is still a draft.
This API is an early preview and can change without a deprecation period.
Arguments  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| input Required  |  [UpdateContentItemDraftInput](https://developers.buffer.com/reference.html#type/UpdateContentItemDraftInput)!  |  Input for updateContentItemDraft.   |  
Example Response

```
{
  "data": {
    "updateContentItemDraft": {}
  }
}
```

MUTATION updatePostTemplate (input: [UpdatePostTemplateInput](https://developers.buffer.com/reference.html#type/UpdatePostTemplateInput)!) : [UpdatePostTemplatePayload](https://developers.buffer.com/reference.html#type/UpdatePostTemplatePayload)! 🧪 Preview
Update a post template owned by the caller (or an internal template in the caller's organization, if the caller is an org admin/owner).
Arguments  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| input Required  |  [UpdatePostTemplateInput](https://developers.buffer.com/reference.html#type/UpdatePostTemplateInput)!  |  Input for updating a post template.   |  
Example Response

```
{
  "data": {
    "updatePostTemplate": {}
  }
}
```

MUTATION updateSnippet (input: [UpdateSnippetInput](https://developers.buffer.com/reference.html#type/UpdateSnippetInput)!) : [UpdateSnippetPayload](https://developers.buffer.com/reference.html#type/UpdateSnippetPayload)! ⚠️ Experimental
Replaces the name and text of a snippet.
Arguments  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| input Required  |  [UpdateSnippetInput](https://developers.buffer.com/reference.html#type/UpdateSnippetInput)!  |  Input for updateSnippet.   |  
Example Response

```
{
  "data": {
    "updateSnippet": {}
  }
}
```

### Outputs 25
OUTPUT [AggregatedPostMetrics](https://developers.buffer.com/reference.html#type/AggregatedPostMetrics)
Aggregated post metrics across a filtered post set. Each entry in `metrics` mirrors the shape of a `Post.metrics` entry; the total number of matched posts is carried as a regular `PostMetric` entry with `type: postCount`.
Fields 2
metrics : [[PostMetric](https://developers.buffer.com/reference.html#type/PostMetric)!]!
Normalized metric aggregates across the matched posts. Always includes a baseline trio (`postCount`, `reactions`, `comments`) — posts on networks that don't track reactions or comments contribute 0 to those totals. Beyond the baseline, additional metric types are included only when every channel in the filter set supports them.
metricsUpdatedAt : [DateTime](https://developers.buffer.com/reference.html#type/DateTime)
The latest `metricsUpdatedAt` across the matched posts, indicating the freshness of the aggregate. Metrics are refreshed daily, so values can be up to ~24h behind the source network. Null when no posts matched the filter.
OUTPUT [ContentItem](https://developers.buffer.com/reference.html#type/ContentItem) ⚠️ Experimental
A piece of content in Buffer. It starts as a channel-less draft and can later become a set of channel-specific posts, or it can be created with its posts directly. This API is an early preview and can change without a deprecation period.
Fields 10
id : [ContentItemId](https://developers.buffer.com/reference.html#type/ContentItemId)!
Unique identifier for this content item.
accountId : [AccountId](https://developers.buffer.com/reference.html#type/AccountId)!
Account that owns this content item.
allowedActions : [[ContentItemAction](https://developers.buffer.com/reference.html#type/ContentItemAction)!]!
Actions the calling actor can take on this content item. A client reads this set instead of deriving the authorization rules itself.
author : [Author](https://developers.buffer.com/reference.html#type/Author)
The person who created this content item. Null when that person's account no longer exists.
body : [ContentItemBody](https://developers.buffer.com/reference.html#type/ContentItemBody)!
The current content of this item: either a channel-less draft or the channel-specific posts created from it.
organizationId : [OrganizationId](https://developers.buffer.com/reference.html#type/OrganizationId)!
Organization that owns this content item.
tags : [[Tag](https://developers.buffer.com/reference.html#type/Tag)!]!
Tags applied to this content item, in the order they were set. A tag applies to the item as a whole, so it survives the move from a channel-less draft to channel-specific posts.
targetDate : [DateTime](https://developers.buffer.com/reference.html#type/DateTime)
Optional date indicating when this piece of content should go out. This is a planning aid only and does not schedule any posts.
title : String
Optional title describing what this piece of content is about.
createdAt : [DateTime](https://developers.buffer.com/reference.html#type/DateTime)!
When this content item was created.
OUTPUT [DailyPostingLimitStatus](https://developers.buffer.com/reference.html#type/DailyPostingLimitStatus)
Posting limit status at an intended posting time. For X, counts describe the busiest rolling 24-hour window affected by adding a post at that time, including later scheduled posts. Other networks use the channel's local calendar day. Counts include existing posts only, excluding the proposed post.
Fields 5
channelId : [ChannelId](https://developers.buffer.com/reference.html#type/ChannelId)!
The channel ID this status refers to.
isAtLimit : Boolean!
Whether adding a post at the requested time would exceed the posting limit.
limit : Int
The network daily posting limit. Null means unlimited.
scheduled : Int!
Number of existing scheduled posts in the evaluated window.
sent : Int!
Number of existing sent posts in the evaluated window.
OUTPUT [Post](https://developers.buffer.com/reference.html#type/Post)
Post entity
Fields 28
id : [PostId](https://developers.buffer.com/reference.html#type/PostId)!
The ID of the post
allowedActions : [[PostAction](https://developers.buffer.com/reference.html#type/PostAction)!]!
Indicates what actions the current account can perform on the post
assets : [[Asset](https://developers.buffer.com/reference.html#type/Asset)!]!
assets
author : [Author](https://developers.buffer.com/reference.html#type/Author)
Represents the user who created the post
channel : [Channel](https://developers.buffer.com/reference.html#type/Channel)!
channel
channelId : [ChannelId](https://developers.buffer.com/reference.html#type/ChannelId)!
channel ID (faster than resolving the channnel.id)
channelService : [Service](https://developers.buffer.com/reference.html#type/Service)!
channel service (faster than resolving the channnel.service)
contentItemId : [ContentItemId](https://developers.buffer.com/reference.html#type/ContentItemId)
The content item this post belongs to. Null when the post belongs to no content item.
dueAt : [DateTime](https://developers.buffer.com/reference.html#type/DateTime)
Date when the post is scheduled to be published
error : [PostPublishingError](https://developers.buffer.com/reference.html#type/PostPublishingError)
error
externalLink : String
The external URL of the post at the destination service
ideaId : [IdeaId](https://developers.buffer.com/reference.html#type/IdeaId)
Is set when the Post is generated from an Idea
isCustomScheduled : Boolean!
Indicates whether time to publish was manually selected by the user
metadata : [PostMetadata](https://developers.buffer.com/reference.html#type/PostMetadata)
Metadata of the post which differs based on the social network/service @see post.metadata.graphql
metrics : [[PostMetric](https://developers.buffer.com/reference.html#type/PostMetric)!]
Metrics for the sent post. If post is not yet sent, this field will be null
metricsUpdatedAt : [DateTime](https://developers.buffer.com/reference.html#type/DateTime)
Timestamp of when `metrics` were last refreshed from the network. Null until the daily ingestion job has processed the post. Buffer pulls fresh metrics once per day, so this can lag the network value by ~24h.
notes : [[Note](https://developers.buffer.com/reference.html#type/Note)!]!
notes
notificationStatus : [NotificationStatus](https://developers.buffer.com/reference.html#type/NotificationStatus)
notificationStatus: notified or markedAsPublished
schedulingType : [SchedulingType](https://developers.buffer.com/reference.html#type/SchedulingType)
How the post publishes: `notification` for a reminder that asks someone to publish it by hand, `automatic` for one the publishing workers send.
sentAt : [DateTime](https://developers.buffer.com/reference.html#type/DateTime)
Date when the post is published
sharedNow : Boolean!
Indicates whether the post was shared via publish now action
shareMode : [ShareMode](https://developers.buffer.com/reference.html#type/ShareMode)!
Indicates the share mode of the post (e.g., addToQueue, shareNext, shareNow, customScheduled)
status : [PostStatus](https://developers.buffer.com/reference.html#type/PostStatus)!
status
tags : [[Tag](https://developers.buffer.com/reference.html#type/Tag)!]!
tags - sorted by name in ascending order
text : String!
Text content of the Post
via : [PostVia](https://developers.buffer.com/reference.html#type/PostVia)!
Indicates if the post is created from Buffer or the API
createdAt : [DateTime](https://developers.buffer.com/reference.html#type/DateTime)!
Date when the post was created
updatedAt : [DateTime](https://developers.buffer.com/reference.html#type/DateTime)!
Date when the post was updated
OUTPUT [PostsResults](https://developers.buffer.com/reference.html#type/PostsResults)
Results for the posts query.
Fields 2
edges : [[PostsEdge](https://developers.buffer.com/reference.html#type/PostsEdge)!]
The list of posts that match the query.
pageInfo : [PaginationPageInfo](https://developers.buffer.com/reference.html#type/PaginationPageInfo)!
Information to aid in pagination.
OUTPUT [PostTemplate](https://developers.buffer.com/reference.html#type/PostTemplate)
A post template used for content inspiration.
Fields 9
id : [PostTemplateId](https://developers.buffer.com/reference.html#type/PostTemplateId)!
The unique identifier for the template.
body : String!
The main content body of the template, may contain {{placeholders}}.
description : String!
A short user-facing description of the template.
emoji : String!
The emoji associated with the template.
organizationId : [OrganizationId](https://developers.buffer.com/reference.html#type/OrganizationId)!
The organization that owns this template.
title : String!
The title of the template.
visibility : [PostTemplateVisibility](https://developers.buffer.com/reference.html#type/PostTemplateVisibility)!
The visibility level of the template. `public` is returned for Buffer-managed templates.
createdAt : [DateTime](https://developers.buffer.com/reference.html#type/DateTime)!
The date and time the template was created.
updatedAt : [DateTime](https://developers.buffer.com/reference.html#type/DateTime)!
The date and time the template was last updated.
OUTPUT [PostTemplatesConnection](https://developers.buffer.com/reference.html#type/PostTemplatesConnection) 🧪 Preview
A paginated connection of post templates.
Fields 3
edges : [[PostTemplateEdge](https://developers.buffer.com/reference.html#type/PostTemplateEdge)!]!
The list of post template edges.
pageInfo : [PaginationPageInfo](https://developers.buffer.com/reference.html#type/PaginationPageInfo)!
Pagination information for the connection.
totalCount : Int!
The total number of templates matching the filters.
OUTPUT [AddPostToContentItemPayload](https://developers.buffer.com/reference.html#type/AddPostToContentItemPayload) ⚠️ Experimental
All possible responses for addPostToContentItem.
OUTPUT [CreatePostTemplatePayload](https://developers.buffer.com/reference.html#type/CreatePostTemplatePayload) 🧪 Preview
Result of an end user creating a post template.
OUTPUT [CreateTagPayload](https://developers.buffer.com/reference.html#type/CreateTagPayload) ⚠️ Experimental
The result of `createTag`: the tag that was created, or the reason it was refused. **Members on the way out.** `RestProxyError`, `NotFoundError`, `UnauthorizedError` and `UnexpectedError` are being removed from this union. No new operation should select them by name. `RestProxyError` is never returned. The other three describe situations a caller cannot correct — the tag not existing, the caller not being permitted, an unexpected fault — and will be reported in the response's top-level `errors` array instead of here. Select `... on MutationError { message }` rather than naming concrete error types. Every error member implements that interface, so the selection keeps working across the change.
OUTPUT [DeletePostPayload](https://developers.buffer.com/reference.html#type/DeletePostPayload)
All possible response types for the deletePost mutation.
OUTPUT [DeletePostTemplatePayload](https://developers.buffer.com/reference.html#type/DeletePostTemplatePayload) 🧪 Preview
Result of an end user deleting a post template.
OUTPUT [DeleteTagPayload](https://developers.buffer.com/reference.html#type/DeleteTagPayload) ⚠️ Experimental
The result of `deleteTag`: the id of the deleted tag, or the reason the delete was refused. **Members on the way out.** `RestProxyError`, `NotFoundError`, `UnauthorizedError` and `UnexpectedError` are being removed from this union. No new operation should select them by name. `RestProxyError` is never returned. The other three describe situations a caller cannot correct — the tag not existing, the caller not being permitted, an unexpected fault — and will be reported in the response's top-level `errors` array instead of here. Select `... on MutationError { message }` rather than naming concrete error types. Every error member implements that interface, so the selection keeps working across the change.
OUTPUT [InstagramAudioCatalogPayload](https://developers.buffer.com/reference.html#type/InstagramAudioCatalogPayload) ⚠️ Experimental
Combined Instagram audio results or a request to refresh the channel.
OUTPUT [InstagramAudioPayload](https://developers.buffer.com/reference.html#type/InstagramAudioPayload) ⚠️ Experimental
Payload returned when refreshing Instagram audio metadata
OUTPUT [MovePostInQueuePayload](https://developers.buffer.com/reference.html#type/MovePostInQueuePayload) ⚠️ Experimental
All possible response types that can be returned by movePostInQueue mutation.
OUTPUT [PostActionPayload](https://developers.buffer.com/reference.html#type/PostActionPayload)
Create post's request response payload.
OUTPUT [PromoteContentItemDraftToPostsPayload](https://developers.buffer.com/reference.html#type/PromoteContentItemDraftToPostsPayload) ⚠️ Experimental
All possible responses for promoteContentItemDraftToPosts.
OUTPUT [RemovePostFromContentItemPayload](https://developers.buffer.com/reference.html#type/RemovePostFromContentItemPayload) ⚠️ Experimental
All possible responses for removePostFromContentItem.
OUTPUT [SearchInstagramAudioPayload](https://developers.buffer.com/reference.html#type/SearchInstagramAudioPayload) ⚠️ Experimental
Payload returned when searching Instagram audio
OUTPUT [UpdateContentItemDraftPayload](https://developers.buffer.com/reference.html#type/UpdateContentItemDraftPayload) ⚠️ Experimental
All possible responses for updateContentItemDraft.
OUTPUT [UpdateContentItemPayload](https://developers.buffer.com/reference.html#type/UpdateContentItemPayload) ⚠️ Experimental
All possible responses for updateContentItem.
OUTPUT [UpdatePostTemplatePayload](https://developers.buffer.com/reference.html#type/UpdatePostTemplatePayload) 🧪 Preview
Result of an end user updating a post template.
OUTPUT [UpdateSnippetPayload](https://developers.buffer.com/reference.html#type/UpdateSnippetPayload) ⚠️ Experimental
All possible responses for updateSnippet. VoidMutationError reports an empty or too long name or text.
OUTPUT [UpdateTagPayload](https://developers.buffer.com/reference.html#type/UpdateTagPayload) ⚠️ Experimental
The result of `updateTag`: the tag as it now stands, or the reason the edit was refused. **Members on the way out.** `RestProxyError`, `NotFoundError`, `UnauthorizedError` and `UnexpectedError` are being removed from this union. No new operation should select them by name. `RestProxyError` is never returned. The other three describe situations a caller cannot correct — the tag not existing, the caller not being permitted, an unexpected fault — and will be reported in the response's top-level `errors` array instead of here. Select `... on MutationError { message }` rather than naming concrete error types. Every error member implements that interface, so the selection keeps working across the change.
### Types 76
TYPE [AddPostToContentItemSuccess](https://developers.buffer.com/reference.html#type/AddPostToContentItemSuccess) ⚠️ Experimental
Successful addPostToContentItem response.
Fields 2
contentItem : [ContentItem](https://developers.buffer.com/reference.html#type/ContentItem)!
The content item after the mutation added the post.
post : [Post](https://developers.buffer.com/reference.html#type/Post)!
The post after the mutation added it. Its contentItemId names this content item.
TYPE [Annotation](https://developers.buffer.com/reference.html#type/Annotation)
Annotation representing all the entities in the text
Fields 5
content : String!
The content of the annotation. Annotations can sometimes be different from the actual text content. E.g., Mastodon mentions have 'text: @buffer', but includes the server name in the content, 'content: @buffer@threads.net'
indices : [Int!]!
The indices of the annotation in the text
text : String!
The text representation of the annotation, eg '@buffer'
type : [AnnotationType](https://developers.buffer.com/reference.html#type/AnnotationType)!
The type of the annotation
url : String!
The URL the annotation points to. Empty string when the annotation has no link.
TYPE [Author](https://developers.buffer.com/reference.html#type/Author)
Represent the author of a post or note.
Fields 6
id : [AccountId](https://developers.buffer.com/reference.html#type/AccountId)!
The unique identifier of the author.
avatar : String!
The avatar URL of the author.
email : String!
The email address of the author.
isDeleted : Boolean!
Indicates whether the author is a deleted.
name : String
The name of the author. Null if the user has not yet set a name.
urn : String
The Buffer account URN for this author, in the form `urn:buffer:account:`. Null when the author is deleted or the account ID is missing or invalid. A URN identifies an account. It does not prove that the account exists, that the caller has access, or that the account can be mentioned.
TYPE [BlueskyPostMetadata](https://developers.buffer.com/reference.html#type/BlueskyPostMetadata)
Bluesky post metadata
Fields 5
annotations : [[Annotation](https://developers.buffer.com/reference.html#type/Annotation)!]!
Annotations representing entities in the text
linkAttachment : [LinkAttachment](https://developers.buffer.com/reference.html#type/LinkAttachment)
Link attachment
thread : [[ThreadedPost](https://developers.buffer.com/reference.html#type/ThreadedPost)!]!
The list of threaded posts (not paginated)
threadCount : Int!
The number of threaded posts
type : [PostType](https://developers.buffer.com/reference.html#type/PostType)!
The channel-specific type of the post, eg, post, story, reel for Instagram
TYPE [ContentItemStateError](https://developers.buffer.com/reference.html#type/ContentItemStateError) ⚠️ Experimental
updateContentItemDraft and promoteContentItemDraftToPosts need a channel-less draft. They report this error when the item already holds channel-specific posts. Another request can put the item in that state while this one runs.
Fields 1
message : String!
Error message.
TYPE [CreatePostTemplateSuccess](https://developers.buffer.com/reference.html#type/CreatePostTemplateSuccess) 🧪 Preview
Successful result of an end user creating a post template.
Fields 1
postTemplate : [PostTemplate](https://developers.buffer.com/reference.html#type/PostTemplate)!
The newly created post template.
TYPE [DeletePostSuccess](https://developers.buffer.com/reference.html#type/DeletePostSuccess)
deletePost success response returns the post id that was deleted.
Fields 1
id : [PostId](https://developers.buffer.com/reference.html#type/PostId)!
Post id that was delete.
TYPE [DeleteTagActionSuccess](https://developers.buffer.com/reference.html#type/DeleteTagActionSuccess) ⚠️ Experimental
Returned when a tag was deleted successfully.
Fields 1
id : [TagId](https://developers.buffer.com/reference.html#type/TagId)!
The id of the tag that was deleted.
TYPE [DraftContent](https://developers.buffer.com/reference.html#type/DraftContent) ⚠️ Experimental
A content draft that is not attached to any channel yet. Because no channel is selected, no network-specific rules apply, including media type restrictions.
Fields 4
id : [DraftContentId](https://developers.buffer.com/reference.html#type/DraftContentId)!
Unique identifier for this draft.
aiAssisted : Boolean!
True when the draft content was written with the help of AI.
assets : [[Asset](https://developers.buffer.com/reference.html#type/Asset)!]!
Images, videos, or documents attached to the draft, in display order.
text : String!
The written content of the draft. Empty when the draft holds only assets.
TYPE [DuplicateError](https://developers.buffer.com/reference.html#type/DuplicateError)
Error returned when a unique constraint is violated
Fields 1
message : String!
Error message
TYPE [EmptySuccess](https://developers.buffer.com/reference.html#type/EmptySuccess)
Empty mutation success response used when client doesn't need any data back or simply needs to respond to a success or error.
Fields 1
_empty : String!
The value is always an empty string '' Note: GraphQL doesn't allow types with no fields, so we have to add this field
TYPE [FacebookPostMetadata](https://developers.buffer.com/reference.html#type/FacebookPostMetadata)
Facebook post metadata
Fields 5
annotations : [[Annotation](https://developers.buffer.com/reference.html#type/Annotation)!]!
Annotations representing entities in the text
firstComment : String
Facebook post's first comment
linkAttachment : [LinkAttachment](https://developers.buffer.com/reference.html#type/LinkAttachment)
Link attachment
title : String
Title of Facebook reel
type : [PostType](https://developers.buffer.com/reference.html#type/PostType)!
The channel-specific type of the post, eg, post, story, reel for Instagram
TYPE [GoogleBusinessEventMetaData](https://developers.buffer.com/reference.html#type/GoogleBusinessEventMetaData)
Metadata for a GBP post that is an event
Fields 8
button : [GoogleBusinessPostActionType](https://developers.buffer.com/reference.html#type/GoogleBusinessPostActionType)!
Action button
endDate : [DateTime](https://developers.buffer.com/reference.html#type/DateTime)!
End date of the event
endTime : String
End time of the event
isFullDayEvent : Boolean!
Indicate whether the event has a start or end time.
link : String
Link to the action
startDate : [DateTime](https://developers.buffer.com/reference.html#type/DateTime)!
Start date of the event
startTime : String
Start time of the event
title : String!
Title of the event
TYPE [GoogleBusinessOfferMetaData](https://developers.buffer.com/reference.html#type/GoogleBusinessOfferMetaData)
Metadata for a GBP post that is an offer
Fields 6
code : String
Coupon code for the offer
endDate : [DateTime](https://developers.buffer.com/reference.html#type/DateTime)!
End date of the offer
link : String
Link to the offer
startDate : [DateTime](https://developers.buffer.com/reference.html#type/DateTime)!
Start date of the offer
terms : String
Terms and Conditions
title : String!
Title of the offer
TYPE [GoogleBusinessPostMetadata](https://developers.buffer.com/reference.html#type/GoogleBusinessPostMetadata)
Google Business Profile post metadata @deprecated: pending proposal for specific GBP post types: update, offer and event metadata types
Fields 4
annotations : [[Annotation](https://developers.buffer.com/reference.html#type/Annotation)!]!
Annotations representing entities in the text
details : [GoogleBusinessPostDetails](https://developers.buffer.com/reference.html#type/GoogleBusinessPostDetails)
Details of the metadata
title : String
Title if available in the given GBP post type: event and offer
type : [PostType](https://developers.buffer.com/reference.html#type/PostType)!
The channel-specific type of the post, eg, post, story, reel for Instagram
TYPE [GoogleBusinessWhatsNewMetaData](https://developers.buffer.com/reference.html#type/GoogleBusinessWhatsNewMetaData)
Metadata for a GBP post of type Whats new
Fields 2
button : [GoogleBusinessPostActionType](https://developers.buffer.com/reference.html#type/GoogleBusinessPostActionType)!
Action button
link : String
Link to the action
TYPE [InstagramAudio](https://developers.buffer.com/reference.html#type/InstagramAudio) ⚠️ Experimental
An Instagram music track or original sound that can be attached to a Reel.
Fields 8
id : String!
Meta audio asset ID
coverArtworkUrl : [URL](https://developers.buffer.com/reference.html#type/URL)
Temporary artwork URL from Meta. May be null.
creatorUsername : String
Creator username for original sounds
displayArtist : String
Artist name for licensed music
duration : Int!
Duration of the audio in milliseconds
previewUrl : [URL](https://developers.buffer.com/reference.html#type/URL)
Temporary preview URL from Meta. May be null.
title : String!
Display title for the audio
type : [InstagramAudioType](https://developers.buffer.com/reference.html#type/InstagramAudioType)!
Whether this asset is licensed music or an original sound
TYPE [InstagramAudioCatalogSuccess](https://developers.buffer.com/reference.html#type/InstagramAudioCatalogSuccess) ⚠️ Experimental
Combined music and original sound results, with duplicate audio IDs removed.
Fields 2
audio : [[InstagramAudio](https://developers.buffer.com/reference.html#type/InstagramAudio)!]!
Available tracks, with duplicate audio IDs removed. Meta's order within each catalog is preserved. Browsing returns music first, then original sounds. Search returns original sounds first, then music, to better reflect the search text: creators write original sound titles, so they usually contain the words people search for, while music results often don't match the query.
failedAudioTypes : [[InstagramAudioType](https://developers.buffer.com/reference.html#type/InstagramAudioType)!]!
Catalogs that failed to load. Results from successful catalogs are still returned, including an empty list if that catalog has no available tracks. If both catalogs fail, the query returns an error instead.
TYPE [InstagramAudioSuccess](https://developers.buffer.com/reference.html#type/InstagramAudioSuccess) ⚠️ Experimental
Refreshed metadata for one Instagram audio asset.
Fields 1
audio : [InstagramAudio](https://developers.buffer.com/reference.html#type/InstagramAudio)!
Refreshed audio metadata.
TYPE [InstagramGeolocation](https://developers.buffer.com/reference.html#type/InstagramGeolocation)
Instagram Geolocation
Fields 2
id : String
The id of this location
text : String
The name of this location
TYPE [InstagramMetadata](https://developers.buffer.com/reference.html#type/InstagramMetadata)
Instagram metadata
Fields 1
defaultToReminders : Boolean!
Indicates if we should default to reminder for Instagram
TYPE [InstagramPostMetadata](https://developers.buffer.com/reference.html#type/InstagramPostMetadata)
Instagram post metadata
Fields 8
annotations : [[Annotation](https://developers.buffer.com/reference.html#type/Annotation)!]!
Annotations representing entities in the text
firstComment : String
Instagram post's first comment
geolocation : [InstagramGeolocation](https://developers.buffer.com/reference.html#type/InstagramGeolocation)
Geolocation of the post
isAiGenerated : Boolean!
Whether the post discloses AI-generated content
link : String
Shop Grid link for the post
shouldShareToFeed : Boolean!
Indicates whether post should be shared to feed
stickerFields : [InstagramStickerFields](https://developers.buffer.com/reference.html#type/InstagramStickerFields)
Sticker fields for reminder-based publishing
type : [PostType](https://developers.buffer.com/reference.html#type/PostType)!
The channel-specific type of the post, eg, post, story, reel for Instagram
TYPE [InstagramStickerFields](https://developers.buffer.com/reference.html#type/InstagramStickerFields)
Instagram fields for reminder-based publishing. Upon the reminder for publishing, the user is prompted to copy and paste these fields into the Instagram app to complete the post.
Fields 5
music : String
Placeholder text for the post's music
other : String
Additional field for any other post content
products : String
Placeholder text for the post's linked products
text : String
Text for the Story or Reel
topics : String
Placeholder text for the post's topics (Reels only)
TYPE [InvalidInputError](https://developers.buffer.com/reference.html#type/InvalidInputError)
Error returned when the input is invalid
Fields 1
message : String!
Error message
TYPE [LinkAttachment](https://developers.buffer.com/reference.html#type/LinkAttachment)
Link attachment
Fields 6
expandedUrl : String
Full URL that the link asset has been built from
text : String!
Description for the scraped link
thumbnail : String
Selected thumbnail for this link preview
thumbnails : [String!]!
Thumbnails of media available in the link
title : String!
Title for the link attachment
url : String!
URL that the link asset has been built from
TYPE [LinkedInPostMetadata](https://developers.buffer.com/reference.html#type/LinkedInPostMetadata)
LinkedIn post metadata
Fields 4
annotations : [[Annotation](https://developers.buffer.com/reference.html#type/Annotation)!]!
Annotations representing entities in the text
firstComment : String
LinkedIn post's first comment
linkAttachment : [LinkAttachment](https://developers.buffer.com/reference.html#type/LinkAttachment)
Link attachment
type : [PostType](https://developers.buffer.com/reference.html#type/PostType)!
The channel-specific type of the post, eg, post, story, reel for Instagram
TYPE [MastodonPostMetadata](https://developers.buffer.com/reference.html#type/MastodonPostMetadata)
Mastodon post metadata
Fields 5
annotations : [[Annotation](https://developers.buffer.com/reference.html#type/Annotation)!]!
Annotations representing entities in the text
spoilerText : String
Spoiler text hiding the root text of this post
thread : [[ThreadedPost](https://developers.buffer.com/reference.html#type/ThreadedPost)!]!
The list of threaded posts (not paginated)
threadCount : Int!
The number of threaded posts
type : [PostType](https://developers.buffer.com/reference.html#type/PostType)!
The channel-specific type of the post, eg, post, story, reel for Instagram
TYPE [Note](https://developers.buffer.com/reference.html#type/Note)
Note entity
Fields 7
id : [NoteId](https://developers.buffer.com/reference.html#type/NoteId)!
The unique identifier of the note.
allowedActions : [[NoteAction](https://developers.buffer.com/reference.html#type/NoteAction)!]!
The allowed actions a user can perform on the note.
author : [Author](https://developers.buffer.com/reference.html#type/Author)!
The author of the note - null if the user is deleted or left the organization.
text : String!
The content of the note.
type : [NoteType](https://developers.buffer.com/reference.html#type/NoteType)!
The type of the note.
createdAt : [DateTime](https://developers.buffer.com/reference.html#type/DateTime)!
The date and time when the note was created.
updatedAt : [DateTime](https://developers.buffer.com/reference.html#type/DateTime)
The date and time when the note was last edited.
TYPE [NotFoundError](https://developers.buffer.com/reference.html#type/NotFoundError)
Error returned when the resource is not found
Fields 1
message : String!
Error message
TYPE [PinterestPostMetadata](https://developers.buffer.com/reference.html#type/PinterestPostMetadata)
Pinterest post metadata
Fields 5
annotations : [[Annotation](https://developers.buffer.com/reference.html#type/Annotation)!]!
Annotations representing entities in the text
board : [PinterestBoard](https://developers.buffer.com/reference.html#type/PinterestBoard)
The board the Pin is saved to
title : String
The title of the Pin
type : [PostType](https://developers.buffer.com/reference.html#type/PostType)!
The channel-specific type of the post, eg, post, story, reel for Instagram
url : String
The Pin destination link
TYPE [PostActionSuccess](https://developers.buffer.com/reference.html#type/PostActionSuccess)
Success response returns the full up-to-date post from after the action was performed.
Fields 1
post : [Post](https://developers.buffer.com/reference.html#type/Post)!
Post on which the action was successfully performed.
TYPE [PostContent](https://developers.buffer.com/reference.html#type/PostContent) ⚠️ Experimental
The fixed set of channel-specific posts created from a content item. Each post targets a single channel and follows that channel's network rules.
Fields 1
posts : [[Post](https://developers.buffer.com/reference.html#type/Post)!]!
The posts created for this content item, one per channel. Individual posts are edited through their own mutations.
TYPE [PostingGoal](https://developers.buffer.com/reference.html#type/PostingGoal)
Represents a posting goal for a channel, including target, progress, and status information.
Fields 6
goal : Int!
The target number of posts for this goal.
periodEnd : [DateTime](https://developers.buffer.com/reference.html#type/DateTime)!
The end date of the period for this posting goal.
periodStart : [DateTime](https://developers.buffer.com/reference.html#type/DateTime)!
The start date of the period for this posting goal.
scheduledCount : Int!
The number of posts that are scheduled to be sent for this goal.
sentCount : Int!
The number of posts that have been sent (published or ingested) for this goal.
status : [PostingGoalStatus](https://developers.buffer.com/reference.html#type/PostingGoalStatus)!
The current status of the posting goal.
TYPE [PostInvalidInputError](https://developers.buffer.com/reference.html#type/PostInvalidInputError) ⚠️ Experimental
Invalid input for a single post in the promoteContentItemDraftToPosts input list.
Fields 2
channelId : [ChannelId](https://developers.buffer.com/reference.html#type/ChannelId)!
Channel targeted by the failing post.
message : String!
Error message.
TYPE [PostLimitReachedError](https://developers.buffer.com/reference.html#type/PostLimitReachedError) ⚠️ Experimental
Limit reached for a single post in the promoteContentItemDraftToPosts input list.
Fields 2
channelId : [ChannelId](https://developers.buffer.com/reference.html#type/ChannelId)!
Channel targeted by the failing post.
message : String!
Error message.
TYPE [PostMetric](https://developers.buffer.com/reference.html#type/PostMetric)
A single metric for a post (or an entry in an aggregated metrics response).
Fields 5
description : String!
A human-readable description of what the metric represents.
name : String!
The human-readable name of the metric (e.g. "Reactions", "Eng. Rate").
type : [PostMetricType](https://developers.buffer.com/reference.html#type/PostMetricType)!
The type of metric. Cross-network metrics use unified naming (`reactions`, `comments`, etc.); network-specific metrics retain their network's vocabulary (`saves`, `quotes`, etc.). See `PostMetricType` for the full catalog including deprecated values.
unit : [PostMetricUnit](https://developers.buffer.com/reference.html#type/PostMetricUnit)!
The unit (count vs percentage) of `value`.
value : Float!
The metric value. Defaults to 0 when the network did not report the metric.
TYPE [PostNotDeletableError](https://developers.buffer.com/reference.html#type/PostNotDeletableError) ⚠️ Experimental
A post in this content item cannot be deleted, so the item cannot be deleted either. Either the post is publishing or has already published, and posts in those states can no longer be deleted, or this account is not allowed to delete posts on that channel.
Fields 2
channelId : [ChannelId](https://developers.buffer.com/reference.html#type/ChannelId)!
Channel targeted by the post that cannot be deleted.
message : String!
Error message.
TYPE [PostPublishingError](https://developers.buffer.com/reference.html#type/PostPublishingError)
Post publishing error
Fields 3
message : String!
Error message to display
rawError : String
The original error from the publishing service (internal use only)
supportUrl : String
Link to a help center article to help resolve the error
TYPE [PostsEdge](https://developers.buffer.com/reference.html#type/PostsEdge)
Represent a node in the pagination result using the Connect Relay convention.
Fields 2
cursor : String!
Opaque cursor to be used in pagination to fetch from current node.
node : [Post](https://developers.buffer.com/reference.html#type/Post)!
Represents the current post in the list.
TYPE [PostTemplateEdge](https://developers.buffer.com/reference.html#type/PostTemplateEdge) 🧪 Preview
An edge in a post template connection.
Fields 2
cursor : String!
A cursor for pagination.
node : [PostTemplate](https://developers.buffer.com/reference.html#type/PostTemplate)!
The post template node at the end of the edge.
TYPE [PromoteContentItemDraftToPostsFailure](https://developers.buffer.com/reference.html#type/PromoteContentItemDraftToPostsFailure) ⚠️ Experimental
promoteContentItemDraftToPosts failure. Every recoverable error is reported together so the caller can surface them all at once — for example, every post that failed validation across every targeted channel. A failure does not always mean nothing changed: post-processing errors are reported after the promotion has taken effect.
Fields 2
errors : [[PromoteContentItemDraftToPostsError](https://developers.buffer.com/reference.html#type/PromoteContentItemDraftToPostsError)!]!
The recoverable errors behind this failure.
message : String!
Summary error message.
TYPE [PromoteContentItemDraftToPostsSuccess](https://developers.buffer.com/reference.html#type/PromoteContentItemDraftToPostsSuccess) ⚠️ Experimental
Successful promoteContentItemDraftToPosts response.
Fields 1
contentItem : [ContentItem](https://developers.buffer.com/reference.html#type/ContentItem)!
The promoted content item.
TYPE [PublishingTag](https://developers.buffer.com/reference.html#type/PublishingTag)
Tag snapshot associated with content
Fields 4
id : ID!
color : String!
Hex color for tag e.g #F523F1
colorName : [TagColorName](https://developers.buffer.com/reference.html#type/TagColorName)
Stable Buffer palette identifier derived from `color`. Clients should map this value to platform- and theme-specific presentation, falling back to `color` when this field is null or unsupported. Returns null for custom or unrecognized colors.
name : String!
TYPE [RemovePostFromContentItemSuccess](https://developers.buffer.com/reference.html#type/RemovePostFromContentItemSuccess) ⚠️ Experimental
Successful removePostFromContentItem response.
Fields 2
contentItem : [ContentItem](https://developers.buffer.com/reference.html#type/ContentItem)!
The content item after the post left it.
post : [Post](https://developers.buffer.com/reference.html#type/Post)!
The post after the mutation removed it. It belongs to no content item.
TYPE [RestProxyError](https://developers.buffer.com/reference.html#type/RestProxyError)
An error passed through from Buffer's legacy REST API. **On the way out.** This type exists only because some mutations still forward to that API. It is never returned by the tag mutations, and will be removed from their payloads. The post mutations can still return it, so keep handling it there for now. Do not select it in new operations. Select `... on MutationError { message }` instead, which every error type implements and which keeps working when this one goes away.
Fields 3
code : Int
Error code from the REST API response - https://buffer.com/developers/api/errors
link : String
Link to our Help center from the REST API response
message : String!
An error message from the REST API response that we proxied here
TYPE [RetweetMetadata](https://developers.buffer.com/reference.html#type/RetweetMetadata)
Information about the initial Tweet that was retweeted
Fields 6
id : String!
Retweet ID
text : String!
Text of the original tweet
thumbnails : [String!]!
Thumbnails to media available in the link
url : String!
Link to original tweet
user : [RetweetUserMetadata](https://developers.buffer.com/reference.html#type/RetweetUserMetadata)!
User who created the original tweet
createdAt : [DateTime](https://developers.buffer.com/reference.html#type/DateTime)!
Date when the original tweet was created
TYPE [RetweetUserMetadata](https://developers.buffer.com/reference.html#type/RetweetUserMetadata)
Information about the initial author of the Tweet that was retweeted
Fields 3
avatar : String!
Avatar of the user who created the original Tweet
name : String!
Name of the user who created the original Tweet
username : String!
Username of the user who created the original Tweet
TYPE [SearchInstagramAudioSuccess](https://developers.buffer.com/reference.html#type/SearchInstagramAudioSuccess) ⚠️ Experimental
Success response for searching Instagram audio
Fields 1
audio : [[InstagramAudio](https://developers.buffer.com/reference.html#type/InstagramAudio)!]!
Matching or trending audio assets
TYPE [Snippet](https://developers.buffer.com/reference.html#type/Snippet) ⚠️ Experimental
A named set of hashtags that a team member saves once and inserts into posts.
Fields 3
id : [SnippetId](https://developers.buffer.com/reference.html#type/SnippetId)!
Unique identifier of the snippet.
name : String!
Display name of the snippet.
text : String!
The hashtags, as the text that is inserted into a post.
TYPE [SubstackPostMetadata](https://developers.buffer.com/reference.html#type/SubstackPostMetadata)
Substack post metadata
Fields 3
annotations : [[Annotation](https://developers.buffer.com/reference.html#type/Annotation)!]!
Annotations representing entities in the text
linkAttachment : [LinkAttachment](https://developers.buffer.com/reference.html#type/LinkAttachment)
Link attachment
type : [PostType](https://developers.buffer.com/reference.html#type/PostType)!
The channel-specific type of the post, eg, post, story, reel for Instagram
TYPE [ThreadedPost](https://developers.buffer.com/reference.html#type/ThreadedPost)
A post authored by the user which is posted to a thread. This is commonly used for long-format twitter and meta threads posts to allow authored content to span multiple threads. Threads are represented as a list of replies, each replying to the previous one.
Fields 4
assets : [[Asset](https://developers.buffer.com/reference.html#type/Asset)!]!
Media assets of the threaded post
linkAttachment : [LinkAttachment](https://developers.buffer.com/reference.html#type/LinkAttachment)
Use metadata.{service}.linkAttachment on the thread item instead. This field will be removed on December 15, 2026.
metadata : [ThreadItemMetadata](https://developers.buffer.com/reference.html#type/ThreadItemMetadata)
Service-specific fields for this threaded post
text : String!
The text body content of the threaded post
TYPE [ThreadItemBlueskyMetadata](https://developers.buffer.com/reference.html#type/ThreadItemBlueskyMetadata)
Bluesky fields on a single item of a thread
Fields 1
linkAttachment : [LinkAttachment](https://developers.buffer.com/reference.html#type/LinkAttachment)
Link attachment
TYPE [ThreadItemMetadata](https://developers.buffer.com/reference.html#type/ThreadItemMetadata)
Service-specific fields on a single item of a thread. The populated key matches the post's service.
Fields 2
bluesky : [ThreadItemBlueskyMetadata](https://developers.buffer.com/reference.html#type/ThreadItemBlueskyMetadata)
Bluesky fields for this thread item
threads : [ThreadItemThreadsMetadata](https://developers.buffer.com/reference.html#type/ThreadItemThreadsMetadata)
Threads fields for this thread item
TYPE [ThreadItemThreadsMetadata](https://developers.buffer.com/reference.html#type/ThreadItemThreadsMetadata)
Threads fields on a single item of a thread
Fields 1
linkAttachment : [LinkAttachment](https://developers.buffer.com/reference.html#type/LinkAttachment)
Link attachment
TYPE [ThreadsPostMetadata](https://developers.buffer.com/reference.html#type/ThreadsPostMetadata)
Threads post metadata
Fields 8
annotations : [[Annotation](https://developers.buffer.com/reference.html#type/Annotation)!]!
Annotations representing entities in the text
linkAttachment : [LinkAttachment](https://developers.buffer.com/reference.html#type/LinkAttachment)
Link attachment
locationId : String
LocationId associated with the post
locationName : String
Location name associated with the post
thread : [[ThreadedPost](https://developers.buffer.com/reference.html#type/ThreadedPost)!]!
The list of threaded posts (not paginated)
threadCount : Int!
The number of threaded posts
topic : String
Topic associated with the post
type : [PostType](https://developers.buffer.com/reference.html#type/PostType)!
The channel-specific type of the post, eg, post, story, reel for Instagram
TYPE [TiktokPostMetadata](https://developers.buffer.com/reference.html#type/TiktokPostMetadata)
Tiktok post metadata
Fields 4
annotations : [[Annotation](https://developers.buffer.com/reference.html#type/Annotation)!]!
Annotations representing entities in the text
isAiGenerated : Boolean!
Whether the post discloses AI-generated content (TikTok video only)
title : String
The title of the TikTok post (for photo posts)
type : [PostType](https://developers.buffer.com/reference.html#type/PostType)!
The channel-specific type of the post, eg, post, story, reel for Instagram
TYPE [TwitterPostMetadata](https://developers.buffer.com/reference.html#type/TwitterPostMetadata)
Twitter post metadata
Fields 6
annotations : [[Annotation](https://developers.buffer.com/reference.html#type/Annotation)!]!
Annotations representing entities in the text
isAiGenerated : Boolean!
Whether the post discloses AI-generated content
retweet : [RetweetMetadata](https://developers.buffer.com/reference.html#type/RetweetMetadata)
The details of the tweet being retweeted
thread : [[ThreadedPost](https://developers.buffer.com/reference.html#type/ThreadedPost)!]!
The list of threaded posts (not paginated)
threadCount : Int!
The number of threaded posts
type : [PostType](https://developers.buffer.com/reference.html#type/PostType)!
The channel-specific type of the post, eg, post, story, reel for Instagram
TYPE [UpdateContentItemDraftFailure](https://developers.buffer.com/reference.html#type/UpdateContentItemDraftFailure) ⚠️ Experimental
updateContentItemDraft failure.
Fields 2
errors : [[UpdateContentItemDraftError](https://developers.buffer.com/reference.html#type/UpdateContentItemDraftError)!]!
The recoverable errors behind this failure.
message : String!
Summary error message.
TYPE [UpdateContentItemDraftSuccess](https://developers.buffer.com/reference.html#type/UpdateContentItemDraftSuccess) ⚠️ Experimental
Successful updateContentItemDraft response.
Fields 1
contentItem : [ContentItem](https://developers.buffer.com/reference.html#type/ContentItem)!
The updated content item.
TYPE [UpdateContentItemFailure](https://developers.buffer.com/reference.html#type/UpdateContentItemFailure) ⚠️ Experimental
updateContentItem failure. When any part of the input is invalid, nothing is changed.
Fields 2
errors : [[InvalidInputError](https://developers.buffer.com/reference.html#type/InvalidInputError)!]!
The recoverable errors behind this failure.
message : String!
Summary error message.
TYPE [UpdateContentItemSuccess](https://developers.buffer.com/reference.html#type/UpdateContentItemSuccess) ⚠️ Experimental
Successful updateContentItem response.
Fields 1
contentItem : [ContentItem](https://developers.buffer.com/reference.html#type/ContentItem)!
The content item after the update.
TYPE [UpdatePostTemplateSuccess](https://developers.buffer.com/reference.html#type/UpdatePostTemplateSuccess) 🧪 Preview
Successful result of an end user updating a post template.
Fields 1
postTemplate : [PostTemplate](https://developers.buffer.com/reference.html#type/PostTemplate)!
The updated post template.
TYPE [UpdateSnippetSuccess](https://developers.buffer.com/reference.html#type/UpdateSnippetSuccess) ⚠️ Experimental
Success response of the updateSnippet mutation.
Fields 1
snippet : [Snippet](https://developers.buffer.com/reference.html#type/Snippet)!
The snippet after the update.
TYPE [UserTag](https://developers.buffer.com/reference.html#type/UserTag)
User tag in the image
Fields 3
handle : String!
The handle (username) of the tagged account, without the leading @.
x : Float!
Horizontal position of the tag as a normalized decimal float between 0.0 and 1.0 - the fraction of the image width from the left edge (0.5 is the horizontal center).
y : Float!
Vertical position of the tag as a normalized decimal float between 0.0 and 1.0 - the fraction of the image height from the top edge (0.5 is the vertical center).
TYPE [VoidMutationError](https://developers.buffer.com/reference.html#type/VoidMutationError)
Error implementation that allows clients to resolve the MutationError on mutations that do not currently have typed errors. This allows clients to automatically handle errors that may be added to a mutation in future. Do not directly throw this error, use a custom typed error instead
Fields 1
message : String!
Error message
TYPE [WeeklyPostingLimit](https://developers.buffer.com/reference.html#type/WeeklyPostingLimit)
Weekly posting limit for a channel
Fields 3
limit : Int!
The weekly posting limit for the channel
scheduled : Int!
The number of posts the channel has scheduled for this week
sent : Int!
The number of posts the channel has sent this week
TYPE [YoutubeCategory](https://developers.buffer.com/reference.html#type/YoutubeCategory)
Fields 2
categoryId : String!
title : String!
TYPE [YoutubePostMetadata](https://developers.buffer.com/reference.html#type/YoutubePostMetadata)
Youtube post metadata
Fields 10
annotations : [[Annotation](https://developers.buffer.com/reference.html#type/Annotation)!]!
Annotations representing entities in the text
category : [YoutubeCategory](https://developers.buffer.com/reference.html#type/YoutubeCategory)
Post category
embeddable : Boolean!
Indicates whether the video allows embedding
isAiGenerated : Boolean!
Whether the post discloses AI-generated content
license : [YoutubeLicense](https://developers.buffer.com/reference.html#type/YoutubeLicense)
Video license
madeForKids : Boolean!
Indicates whether the video is suitable for kids
notifySubscribers : Boolean!
Indicates whether to notify subscribers on publish video
privacy : [YoutubePrivacy](https://developers.buffer.com/reference.html#type/YoutubePrivacy)
Privacy setting for post
title : String
Title of the Youtube post
type : [PostType](https://developers.buffer.com/reference.html#type/PostType)!
The channel-specific type of the post, eg, post, story, reel for Youtube
TYPE [Asset](https://developers.buffer.com/reference.html#type/Asset)
Asset interface with common fields
Fields 5
id : ID
The ID of the asset in the database
mimeType : String!
The MIME type of the asset
source : String!
URL to the file source
thumbnail : String!
URL to the static thumbnail of the asset
type : [AssetType](https://developers.buffer.com/reference.html#type/AssetType)!
The type of the asset
TYPE [CommonPostMetadata](https://developers.buffer.com/reference.html#type/CommonPostMetadata)
Common properties for all post metadata types
Fields 2
annotations : [[Annotation](https://developers.buffer.com/reference.html#type/Annotation)!]!
Annotations representing entities in the text
type : [PostType](https://developers.buffer.com/reference.html#type/PostType)!
The channel-specific type of the post, eg, post, story, reel for Instagram
TYPE [ThreadedPostMetadata](https://developers.buffer.com/reference.html#type/ThreadedPostMetadata)
Common properties for all posts that support threaded replies. See ThreadedPost for more details.
Fields 2
thread : [[ThreadedPost](https://developers.buffer.com/reference.html#type/ThreadedPost)!]!
The list of threaded posts (not paginated)
threadCount : Int!
The number of threaded posts
TYPE [ContentItemBody](https://developers.buffer.com/reference.html#type/ContentItemBody) ⚠️ Experimental
A content item's content: its channel-less draft while it is a draft, or its channel-specific posts once it holds posts. The body shows one or the other, never both, although a content item keeps its draft after it becomes posts.
TYPE [GoogleBusinessPostDetails](https://developers.buffer.com/reference.html#type/GoogleBusinessPostDetails)
GoogleBusiness Metadata details
TYPE [PostMetadata](https://developers.buffer.com/reference.html#type/PostMetadata)
Post metadata union type. Contains all possible types of post metadata.
TYPE [PromoteContentItemDraftToPostsError](https://developers.buffer.com/reference.html#type/PromoteContentItemDraftToPostsError) ⚠️ Experimental
A recoverable error that prevented a content item draft from being promoted. Post errors identify the specific channel they apply to; the others apply to the request as a whole.
TYPE [UpdateContentItemDraftError](https://developers.buffer.com/reference.html#type/UpdateContentItemDraftError) ⚠️ Experimental
A recoverable error that prevented a content item draft from being updated.
### Inputs 68
INPUT [AddPostToContentItemInput](https://developers.buffer.com/reference.html#type/AddPostToContentItemInput) ⚠️ Experimental
Input for addPostToContentItem.
Fields 2
id : [ContentItemId](https://developers.buffer.com/reference.html#type/ContentItemId)!
The content item to add the post to.
postId : [PostId](https://developers.buffer.com/reference.html#type/PostId)!
The post to add. The post must already exist. The post and the content item must belong to the same organization.
INPUT [AggregatedPostMetricsInput](https://developers.buffer.com/reference.html#type/AggregatedPostMetricsInput)
Input for the `aggregatedPostMetrics` query.
Fields 5
channelIds : [[ChannelId](https://developers.buffer.com/reference.html#type/ChannelId)!]
Optional list of channel IDs to filter by. When omitted (null), the aggregate spans every channel in the organization the actor has insights access to. When set to an empty array, no channels match and the result is empty.
endDateTime : [DateTime](https://developers.buffer.com/reference.html#type/DateTime)!
End of the aggregation window. Consumers typically pass UTC midnight of the last calendar day in the window (the backend treats the range as inclusive of that day), for example `2026-01-31T00:00:00Z`. Date range is capped to 365 days.
organizationId : [OrganizationId](https://developers.buffer.com/reference.html#type/OrganizationId)!
The organization ID
startDateTime : [DateTime](https://developers.buffer.com/reference.html#type/DateTime)!
Start of the aggregation window. Consumers typically pass UTC midnight of the first calendar day in the window, for example `2026-01-01T00:00:00Z`.
tags : [TagComparator](https://developers.buffer.com/reference.html#type/TagComparator)
Filter to posts with specific tags. When omitted, all posts are included regardless of tags.
INPUT [AnnotationInputFacebook](https://developers.buffer.com/reference.html#type/AnnotationInputFacebook)
Annotation representing all the entities in the text
Fields 4
content : String!
The content of the annotation, e.g. '107509875938399'
indices : [Int!]!
The indices of the annotation in the text, e.g. [6, 9] (from 6 to 9 characters in the text)
text : String!
The text representation of the annotation, eg 'Buffer'
url : String!
The URL the annotation points to, e.g. https://www.facebook.com/107509875938399
INPUT [AnnotationInputLinkedIn](https://developers.buffer.com/reference.html#type/AnnotationInputLinkedIn)
Annotation representing all the entities in the text
Fields 7
id : String!
The id of the annotation, e.g. 1521226
entity : String!
The entity of the annotation, e.g. urn:li:organization:1521226
length : Int!
The length of the annotation, e.g. 6
link : String!
The link of the annotation, e.g. https://www.linkedin.com/company/bufferapp
localizedName : String!
The localized name of the annotation, e.g. Buffer
start : Int!
The start of the annotation, e.g. 5
vanityName : String!
The vanity name of the annotation, e.g. bufferapp
INPUT [AssetInput](https://developers.buffer.com/reference.html#type/AssetInput)
A single entity's asset. Exactly one variant must be provided.
Fields 4
document : [DocumentAssetInput](https://developers.buffer.com/reference.html#type/DocumentAssetInput)
Document asset
image : [ImageAssetInput](https://developers.buffer.com/reference.html#type/ImageAssetInput)
Image asset
link : [LinkAssetInput](https://developers.buffer.com/reference.html#type/LinkAssetInput)
Use metadata.{service}.linkAttachment instead. This field will be removed on December 15, 2026.
video : [VideoAssetInput](https://developers.buffer.com/reference.html#type/VideoAssetInput)
Video asset
INPUT [BlueskyPostMetadataInput](https://developers.buffer.com/reference.html#type/BlueskyPostMetadataInput)
Bluesky post metadata
Fields 2
linkAttachment : [LinkAttachmentInput](https://developers.buffer.com/reference.html#type/LinkAttachmentInput)
Link attachment. Mutually exclusive with a non-empty `assets` array — input providing both is rejected.
thread : [[ThreadedPostInput](https://developers.buffer.com/reference.html#type/ThreadedPostInput)!]
The ordered list of posts that make up the thread (not paginated). This array is the source of truth for what gets published: every post in the thread, including the root post, must be provided here. Posts are published in order, each replying to the previous one. The first item is the root post and should match the top-level `text` on the post input.
INPUT [CreatePostInput](https://developers.buffer.com/reference.html#type/CreatePostInput)
Create post's request input. Note: `metadata.{service}.linkAttachment` is mutually exclusive with a non-empty `assets` array. Input providing both is rejected.
Fields 14
aiAssisted : Boolean
If this post was created with the help of AI
assets : [[AssetInput](https://developers.buffer.com/reference.html#type/AssetInput)!]!
Ordered list of assets on this post.
channelId : [ChannelId](https://developers.buffer.com/reference.html#type/ChannelId)!
Channel's Id for which we want to create the post
draftId : [DraftId](https://developers.buffer.com/reference.html#type/DraftId)
Is set when the Post is generated from a Draft
dueAt : [DateTime](https://developers.buffer.com/reference.html#type/DateTime)
Date when the post is scheduled to be published
ideaId : [IdeaId](https://developers.buffer.com/reference.html#type/IdeaId)
Is set when the Post is generated from an Idea
metadata : [PostInputMetaData](https://developers.buffer.com/reference.html#type/PostInputMetaData)
Metadata of the post which differs based on the social network/service
mode : [ShareMode](https://developers.buffer.com/reference.html#type/ShareMode)!
How the post is being scheduled.
needsApproval : Boolean!
Submit the post for approval instead of scheduling it. A post submitted for approval is always a draft, so this conflicts with turning `saveToDraft` off. Only valid when your posting policy on the target channel requires approval.
saveToDraft : Boolean
If true, saves the post as a draft instead of scheduling it. When saving as draft: - Post status will be 'draft' instead of 'buffer' - Posting limits are not checked - The post will not be published until explicitly scheduled
schedulingType : [SchedulingType](https://developers.buffer.com/reference.html#type/SchedulingType)!
Scheduling type to indicate notification publishing or automatic publishing
source : String
source where the composer was initiated from, used for tracking.
tagIds : [[TagId](https://developers.buffer.com/reference.html#type/TagId)!]
List of tag IDs
text : String
Text content of the Post. Note: for threaded posts, this needs to match the first item in the `thread` array.
INPUT [CreatePostTemplateInput](https://developers.buffer.com/reference.html#type/CreatePostTemplateInput)
Input for an end user creating a post template. Buffer-curated taxonomy fields are server-defaulted; setting them is only available to official Buffer clients.
Fields 6
body : String!
The main content body of the template, may contain {{placeholders}}.
description : String
A short user-facing description of the template. Nullable for backwards-compat at the GraphQL boundary — the resolver rejects null/empty values with a clear input error so the underlying storage contract (non-empty string) is still honored.
emoji : String
The emoji associated with the template.
organizationId : [OrganizationId](https://developers.buffer.com/reference.html#type/OrganizationId)!
Organization the template belongs to. The caller must be a member of this organization. For `internal` visibility this is the team scope; for `private` it's recorded on the template but does not affect visibility.
title : String!
The title of the template.
visibility : [PostTemplateVisibility](https://developers.buffer.com/reference.html#type/PostTemplateVisibility)
Defaults to `private` if omitted. `public` is rejected — it is only available to official Buffer clients.
INPUT [CreateTagInput](https://developers.buffer.com/reference.html#type/CreateTagInput) ⚠️ Experimental
Input for creating a tag.
Fields 2
organizationId : [OrganizationId](https://developers.buffer.com/reference.html#type/OrganizationId)!
Organization to create the tag in. The caller must be an administrator of this organization.
tag : [TagToCreateInput](https://developers.buffer.com/reference.html#type/TagToCreateInput)!
The name and color to give the new tag.
INPUT [DailyPostingLimitsInput](https://developers.buffer.com/reference.html#type/DailyPostingLimitsInput)
Input for the dailyPostingLimits query.
Fields 2
channelIds : [[ChannelId](https://developers.buffer.com/reference.html#type/ChannelId)!]!
List of channel IDs to check limits for. All channels must belong to the same organization.
date : [DateTime](https://developers.buffer.com/reference.html#type/DateTime)
The intended posting time. Defaults to now if not provided. For X, the exact time determines the affected rolling 24-hour windows. For other networks, the date selects the channel's local calendar day.
INPUT [DateTimeComparator](https://developers.buffer.com/reference.html#type/DateTimeComparator)
Comparator for filtering by date
Fields 2
end : [DateTime](https://developers.buffer.com/reference.html#type/DateTime)
Include results with dates equal to or before the specified date
start : [DateTime](https://developers.buffer.com/reference.html#type/DateTime)
Include results with dates equal to or after the specified date
INPUT [DeletePostInput](https://developers.buffer.com/reference.html#type/DeletePostInput)
deletePost mutation deletes a post by id.
Fields 1
id : [PostId](https://developers.buffer.com/reference.html#type/PostId)!
Post id to delete.
INPUT [DeletePostTemplateInput](https://developers.buffer.com/reference.html#type/DeletePostTemplateInput) 🧪 Preview
Input for an end user deleting a post template.
Fields 1
id : [PostTemplateId](https://developers.buffer.com/reference.html#type/PostTemplateId)!
The ID of the template to delete.
INPUT [DeleteTagInput](https://developers.buffer.com/reference.html#type/DeleteTagInput) ⚠️ Experimental
Input for deleting a tag.
Fields 1
id : [TagId](https://developers.buffer.com/reference.html#type/TagId)!
The tag to delete. Its organization is taken from the tag itself, and the caller must be an administrator of that organization.
INPUT [DocumentAssetInput](https://developers.buffer.com/reference.html#type/DocumentAssetInput)
Document asset
Fields 3
thumbnailUrl : String!
Document thumbnail URL
title : String!
Document title
url : String!
Document URL
INPUT [DraftContentInput](https://developers.buffer.com/reference.html#type/DraftContentInput) ⚠️ Experimental
A channel-less draft to save on a content item.
Fields 3
aiAssisted : Boolean!
Set to true when the draft content was written with the help of AI.
assets : [[AssetInput](https://developers.buffer.com/reference.html#type/AssetInput)!]!
Images, videos, or documents to attach to the draft, in display order.
text : String!
The written content of the draft. Can be empty when the draft holds at least one asset.
INPUT [EditPostInput](https://developers.buffer.com/reference.html#type/EditPostInput)
Edit post's request input. Note: `metadata.{service}.linkAttachment` is mutually exclusive with a non-empty `assets` array. Input providing both is rejected.
Fields 14
id : [PostId](https://developers.buffer.com/reference.html#type/PostId)!
ID of the post to edit
aiAssisted : Boolean
If this post was edited with the help of AI
approvalChange : [PostApprovalChange](https://developers.buffer.com/reference.html#type/PostApprovalChange)
Change the post's approval state alongside this edit. Leave unset to keep the post's current approval state. Only valid when your posting policy on the post's channel requires approval, and only on your own drafts. Asking for the state the post is already in does nothing.
assets : [[AssetInput](https://developers.buffer.com/reference.html#type/AssetInput)!]
Ordered list of assets on this post. Omit to preserve the existing list, pass an empty array to clear it
draftId : [DraftId](https://developers.buffer.com/reference.html#type/DraftId)
Is set when the Post is generated from a Draft
dueAt : [DateTime](https://developers.buffer.com/reference.html#type/DateTime)
Date when the post is scheduled to be published
ideaId : [IdeaId](https://developers.buffer.com/reference.html#type/IdeaId)
Is set when the Post is generated from an Idea
metadata : [PostInputMetaData](https://developers.buffer.com/reference.html#type/PostInputMetaData)
Metadata of the post which differs based on the social network/service
mode : [ShareMode](https://developers.buffer.com/reference.html#type/ShareMode)
How the post is being scheduled. Omit the field or pass null to make no scheduling change — null does not clear or reset the schedule: a scheduled post keeps its current share mode, queue slot, and any custom time, and the edit applies only the other provided fields. Pass a non-null ShareMode to apply that mode.
saveToDraft : Boolean
If true, saves the post as a draft instead of keeping it scheduled. When saving as draft: - Post status will be 'draft' instead of 'buffer' - The post will not be published until explicitly scheduled
schedulingType : [SchedulingType](https://developers.buffer.com/reference.html#type/SchedulingType)
Scheduling type to indicate notification publishing or automatic publishing. Omit it, or send null, to leave the post publishing the way it already does.
source : String
source where the composer was initiated from, used for tracking.
tagIds : [[TagId](https://developers.buffer.com/reference.html#type/TagId)!]
tags
text : String
Text content of the Post. Omit the field to keep the current text; pass an empty string or null to clear it. Note: for threaded posts, this needs to match the first item in the `thread` array.
INPUT [FacebookPostMetadataInput](https://developers.buffer.com/reference.html#type/FacebookPostMetadataInput)
Facebook post metadata
Fields 4
annotations : [[AnnotationInputFacebook](https://developers.buffer.com/reference.html#type/AnnotationInputFacebook)!]
Annotations representing entities in the text
firstComment : String
Facebook post's first comment
linkAttachment : [LinkAttachmentInput](https://developers.buffer.com/reference.html#type/LinkAttachmentInput)
Link attachment. Mutually exclusive with a non-empty `assets` array — input providing both is rejected.
type : [PostTypeFacebook](https://developers.buffer.com/reference.html#type/PostTypeFacebook)!
The channel-specific type of the post, eg, post, story, reel for Facebook
INPUT [GoogleBusinessEventMetaDataInput](https://developers.buffer.com/reference.html#type/GoogleBusinessEventMetaDataInput)
Metadata for a GBP post that is an event
Fields 6
button : [GoogleBusinessPostActionType](https://developers.buffer.com/reference.html#type/GoogleBusinessPostActionType)
Action button. Optional: a post with no button, or `none`, publishes without a call-to-action. On edit, omitting it preserves the existing value.
endDate : [DateTime](https://developers.buffer.com/reference.html#type/DateTime)
End date of the event. Required on create; optional on edit (omitted preserves existing value).
isFullDayEvent : Boolean!
Indicate whether the event has a start or end time.
link : String
Link to the action
startDate : [DateTime](https://developers.buffer.com/reference.html#type/DateTime)
Start date of the event. Required on create; optional on edit (omitted preserves existing value).
title : String
Title of the event. Required on create; optional on edit (omitted preserves existing value).
INPUT [GoogleBusinessOfferMetaDataInput](https://developers.buffer.com/reference.html#type/GoogleBusinessOfferMetaDataInput)
Metadata for a GBP post that is an offer
Fields 6
code : String
Coupon code for the offer
endDate : [DateTime](https://developers.buffer.com/reference.html#type/DateTime)
End date of the offer. Required on create; optional on edit (omitted preserves existing value).
link : String
Link to the offer
startDate : [DateTime](https://developers.buffer.com/reference.html#type/DateTime)
Start date of the offer. Required on create; optional on edit (omitted preserves existing value).
terms : String
Terms and Conditions
title : String
Title of the offer. Required on create; optional on edit (omitted preserves existing value).
INPUT [GoogleBusinessPostMetadataInput](https://developers.buffer.com/reference.html#type/GoogleBusinessPostMetadataInput)
Google Business Profile post metadata @deprecated: pending proposal for specific GBP post types: update, offer and event metadata types
Fields 5
detailsEvent : [GoogleBusinessEventMetaDataInput](https://developers.buffer.com/reference.html#type/GoogleBusinessEventMetaDataInput)
Details of the Event metadata
detailsOffer : [GoogleBusinessOfferMetaDataInput](https://developers.buffer.com/reference.html#type/GoogleBusinessOfferMetaDataInput)
Details of the Offer metadata
detailsWhatsNew : [GoogleBusinessWhatsNewMetaDataInput](https://developers.buffer.com/reference.html#type/GoogleBusinessWhatsNewMetaDataInput)
Details of the Whats new metadata
title : String
Title if available in the given GBP post type: event and offer
type : [PostTypeGoogleBusiness](https://developers.buffer.com/reference.html#type/PostTypeGoogleBusiness)!
The channel-specific type of the post, eg, post, offer, event for Google Business Profile
INPUT [GoogleBusinessWhatsNewMetaDataInput](https://developers.buffer.com/reference.html#type/GoogleBusinessWhatsNewMetaDataInput)
Metadata for a GBP post of type Whats new
Fields 2
button : [GoogleBusinessPostActionType](https://developers.buffer.com/reference.html#type/GoogleBusinessPostActionType)
Action button. Optional: a post with no button, or `none`, publishes without a call-to-action. On edit, omitting it preserves the existing value.
link : String
Link to the action
INPUT [ImageAssetInput](https://developers.buffer.com/reference.html#type/ImageAssetInput)
Image asset
Fields 3
metadata : [ImageMetadataInput](https://developers.buffer.com/reference.html#type/ImageMetadataInput)
Image specific metadata
thumbnailUrl : String
URL to the static thumbnail of the asset
url : String!
URL to the file source
INPUT [ImageDimensionsInput](https://developers.buffer.com/reference.html#type/ImageDimensionsInput)
Image dimensions
Fields 2
height : Int!
Image height in pixels
width : Int!
Image width in pixels
INPUT [ImageMetadataInput](https://developers.buffer.com/reference.html#type/ImageMetadataInput)
Image metadata
Fields 4
altText : String!
Alternative text for accessibility
animatedThumbnail : String
Animated thumbnail URL
dimensions : [ImageDimensionsInput](https://developers.buffer.com/reference.html#type/ImageDimensionsInput)
Ignored — the API resolves image dimensions itself.
userTags : [[UserTagInput](https://developers.buffer.com/reference.html#type/UserTagInput)!]
Accounts to tag at specific points on the image. Each tag's x/y position uses normalized 0.0-1.0 coordinates - see UserTagInput.
INPUT [InstagramAudioCatalogInput](https://developers.buffer.com/reference.html#type/InstagramAudioCatalogInput) ⚠️ Experimental
Input for browsing trending music and original sounds.
Fields 1
channelId : [ChannelId](https://developers.buffer.com/reference.html#type/ChannelId)!
Instagram channel used to authorize the catalog request.
INPUT [InstagramAudioInput](https://developers.buffer.com/reference.html#type/InstagramAudioInput) ⚠️ Experimental
Input for refreshing a single Instagram audio asset
Fields 2
audioId : String!
Meta audio asset ID
channelId : [ChannelId](https://developers.buffer.com/reference.html#type/ChannelId)!
Instagram channel used to authorize the refresh
INPUT [InstagramGeolocationInput](https://developers.buffer.com/reference.html#type/InstagramGeolocationInput)
Instagram Geolocation
Fields 2
id : String
The id of this location
text : String
The name of this location
INPUT [InstagramPostMetadataInput](https://developers.buffer.com/reference.html#type/InstagramPostMetadataInput)
Instagram post metadata
Fields 7
firstComment : String
Instagram post's first comment
geolocation : [InstagramGeolocationInput](https://developers.buffer.com/reference.html#type/InstagramGeolocationInput)
Geolocation of the post
isAiGenerated : Boolean
Whether the post discloses AI-generated content
link : String
Shop Grid link for the post
shouldShareToFeed : Boolean!
Indicates whether post should be shared to feed
stickerFields : [InstagramStickerFieldsInput](https://developers.buffer.com/reference.html#type/InstagramStickerFieldsInput)
Sticker fields for reminder-based publishing
type : [PostType](https://developers.buffer.com/reference.html#type/PostType)!
The channel-specific type of the post, eg, post, story, reel for Instagram
INPUT [InstagramStickerFieldsInput](https://developers.buffer.com/reference.html#type/InstagramStickerFieldsInput)
Instagram fields for reminder-based publishing. Upon the reminder for publishing, the user is prompted to copy and paste these fields into the Instagram app to complete the post.
Fields 5
music : String
Placeholder text for the post's music
other : String
Additional field for any other post content
products : String
Placeholder text for the post's linked products
text : String
Text for the Story or Reel
topics : String
Placeholder text for the post's topics (Reels only)
INPUT [LinkAssetInput](https://developers.buffer.com/reference.html#type/LinkAssetInput)
Link attached to the post
Fields 4
description : String
Description of the link
thumbnailUrl : String
Thumbnail URL of the link
title : String
Title of the link
url : String!
URL to the link
INPUT [LinkAttachmentInput](https://developers.buffer.com/reference.html#type/LinkAttachmentInput)
Link attachment
Fields 4
description : String
Description shown on the link card
thumbnail : [LinkAttachmentThumbnailInput](https://developers.buffer.com/reference.html#type/LinkAttachmentThumbnailInput)
Thumbnail shown on the link card
title : String
Title shown on the link card
url : String!
URL that the link asset has been built from
INPUT [LinkAttachmentThumbnailInput](https://developers.buffer.com/reference.html#type/LinkAttachmentThumbnailInput)
Thumbnail of a link attachment
Fields 1
url : String!
URL of the thumbnail image
INPUT [LinkedInPostMetadataInput](https://developers.buffer.com/reference.html#type/LinkedInPostMetadataInput)
LinkedIn post metadata
Fields 3
annotations : [[AnnotationInputLinkedIn](https://developers.buffer.com/reference.html#type/AnnotationInputLinkedIn)!]
Annotations representing entities in the text
firstComment : String
LinkedIn post's first comment
linkAttachment : [LinkAttachmentInput](https://developers.buffer.com/reference.html#type/LinkAttachmentInput)
Link attachment. Mutually exclusive with a non-empty `assets` array — input providing both is rejected.
INPUT [MastodonPostMetadataInput](https://developers.buffer.com/reference.html#type/MastodonPostMetadataInput)
Mastodon post metadata
Fields 2
spoilerText : String
Spoiler text hiding the root text of this post
thread : [[ThreadedPostInput](https://developers.buffer.com/reference.html#type/ThreadedPostInput)!]
The ordered list of posts that make up the thread (not paginated). This array is the source of truth for what gets published: every post in the thread, including the root post, must be provided here. Posts are published in order, each replying to the previous one. The first item is the root post and should match the top-level `text` on the post input.
INPUT [MovePostInQueueInput](https://developers.buffer.com/reference.html#type/MovePostInQueueInput) ⚠️ Experimental
movePostInQueue mutation moves a queued post to the top or bottom of its channel's queue.
Fields 2
id : [PostId](https://developers.buffer.com/reference.html#type/PostId)!
ID of the post to move.
position : [QueuePosition](https://developers.buffer.com/reference.html#type/QueuePosition)!
Target position within the channel's queue.
INPUT [PinterestPostMetadataInput](https://developers.buffer.com/reference.html#type/PinterestPostMetadataInput)
Pinterest post metadata
Fields 3
boardServiceId : String
The board ID of the Pin, can be obtained when fetching the channel details with the following query: ``` query GetChannelWithSubprofiles { channel(input: { id: "[CHANNEL_ID_HERE]" }) { metadata { ... on PinterestMetadata { boards { serviceId } } } } } ``` Required on create; optional on edit (omitted preserves existing board).
title : String
The title of the Pin
url : String
The Pin destination link
INPUT [PostInput](https://developers.buffer.com/reference.html#type/PostInput)
Input for the post query
Fields 1
id : [PostId](https://developers.buffer.com/reference.html#type/PostId)!
The ID of the post to be retrieved
INPUT [PostInputMetaData](https://developers.buffer.com/reference.html#type/PostInputMetaData)
Metadata of the post which differs based on the social network/service
Fields 12
bluesky : [BlueskyPostMetadataInput](https://developers.buffer.com/reference.html#type/BlueskyPostMetadataInput)
Metadata for Bluesky post
facebook : [FacebookPostMetadataInput](https://developers.buffer.com/reference.html#type/FacebookPostMetadataInput)
Metadata for Facebook post
google : [GoogleBusinessPostMetadataInput](https://developers.buffer.com/reference.html#type/GoogleBusinessPostMetadataInput)
Metadata for Google Business Profile post
instagram : [InstagramPostMetadataInput](https://developers.buffer.com/reference.html#type/InstagramPostMetadataInput)
Metadata for Instagram post
linkedin : [LinkedInPostMetadataInput](https://developers.buffer.com/reference.html#type/LinkedInPostMetadataInput)
Metadata for LinkedIn post
mastodon : [MastodonPostMetadataInput](https://developers.buffer.com/reference.html#type/MastodonPostMetadataInput)
Metadata for Mastodon post
pinterest : [PinterestPostMetadataInput](https://developers.buffer.com/reference.html#type/PinterestPostMetadataInput)
Metadata for Pinterest post
substack : [SubstackPostMetadataInput](https://developers.buffer.com/reference.html#type/SubstackPostMetadataInput)
Metadata for Substack post
threads : [ThreadsPostMetadataInput](https://developers.buffer.com/reference.html#type/ThreadsPostMetadataInput)
Metadata for Threads post
tiktok : [TikTokPostMetadataInput](https://developers.buffer.com/reference.html#type/TikTokPostMetadataInput)
Metadata for TikTok post
twitter : [TwitterPostMetadataInput](https://developers.buffer.com/reference.html#type/TwitterPostMetadataInput)
Metadata for Twitter post
youtube : [YoutubePostMetadataInput](https://developers.buffer.com/reference.html#type/YoutubePostMetadataInput)
Metadata for Youtube post
INPUT [PostsFiltersInput](https://developers.buffer.com/reference.html#type/PostsFiltersInput)
Filter to apply to the posts query
Fields 10
channelIds : [[ChannelId](https://developers.buffer.com/reference.html#type/ChannelId)!]
When set, it will filter posts by channel
dueAt : [DateTimeComparator](https://developers.buffer.com/reference.html#type/DateTimeComparator)
When set, it will filter posts by their scheduled posting date
dueAtPresence : [DateTimePresence](https://developers.buffer.com/reference.html#type/DateTimePresence)
When set, it will filter posts by whether their scheduled posting date exists. `absent` cannot be combined with `dueAt`, because absent dates cannot also match a date range.
endDate : [DateTime](https://developers.buffer.com/reference.html#type/DateTime)
When set, it will return posts with createdAt or dueAt date before endDate
postTypes : [[PostType](https://developers.buffer.com/reference.html#type/PostType)!]
When set, it will filter posts by format. `post` is a fallback bucket rather than one stored format: it matches every post the other formats do not claim, which is what `Post.metadata.type` reports for the same post. `carousel` and `thread` are rejected, because no stored value resolves to them.
startDate : [DateTime](https://developers.buffer.com/reference.html#type/DateTime)
When set, it will return posts with createdAt or dueAt date after startDate
status : [[PostStatus](https://developers.buffer.com/reference.html#type/PostStatus)!]
When set, it will filter posts by status
tagIds : [[TagId](https://developers.buffer.com/reference.html#type/TagId)!]
When set, it will filter posts by tag
tags : [TagComparator](https://developers.buffer.com/reference.html#type/TagComparator)
Filter posts by tags. Supports specific tags, untagged posts, or union of both.
createdAt : [DateTimeComparator](https://developers.buffer.com/reference.html#type/DateTimeComparator)
When set, it will filter posts by the date they were created
INPUT [PostsInput](https://developers.buffer.com/reference.html#type/PostsInput)
Input for the posts query
Fields 3
filter : [PostsFiltersInput](https://developers.buffer.com/reference.html#type/PostsFiltersInput)
The filters to apply to the posts query
organizationId : [OrganizationId](https://developers.buffer.com/reference.html#type/OrganizationId)!
The Organization id to fetch posts for
sort : [[PostSortInput](https://developers.buffer.com/reference.html#type/PostSortInput)!]
The sort to apply to the posts results
INPUT [PostSortInput](https://developers.buffer.com/reference.html#type/PostSortInput)
Sort order of post results. List multiple to create tie-breaking order.
Fields 2
direction : [SortDirection](https://developers.buffer.com/reference.html#type/SortDirection)!
The direction to sort by.
field : [PostSortableKey](https://developers.buffer.com/reference.html#type/PostSortableKey)!
The field to sort by.
INPUT [PostTemplateInput](https://developers.buffer.com/reference.html#type/PostTemplateInput) 🧪 Preview
Input for fetching a single post template by ID.
Fields 1
id : [PostTemplateId](https://developers.buffer.com/reference.html#type/PostTemplateId)!
The unique identifier of the template to fetch.
INPUT [PostTemplatesFilterInput](https://developers.buffer.com/reference.html#type/PostTemplatesFilterInput)
Filters for the template library. Visibility narrows the actor-scoped result set; it can never widen it.
Fields 1
visibility : [PostTemplateVisibility](https://developers.buffer.com/reference.html#type/PostTemplateVisibility)
Narrow the result to a single visibility scope. Omit to receive the union of: public templates, internal templates from the supplied organization, and private templates from the actor's account.
INPUT [PostTemplatesInput](https://developers.buffer.com/reference.html#type/PostTemplatesInput) 🧪 Preview
Input for fetching templates accessible to the current actor for the template library. A caller can never reach templates outside their own scope — the server pins `private` to the actor's account and `internal` to the supplied `organizationId` regardless of input.
Fields 2
filter : [PostTemplatesFilterInput](https://developers.buffer.com/reference.html#type/PostTemplatesFilterInput)
Optional filters to narrow the template list.
organizationId : [OrganizationId](https://developers.buffer.com/reference.html#type/OrganizationId)!
Organization to scope `internal`-visibility templates to. The caller must be a member of this organization.
INPUT [PromoteContentItemDraftToPostsInput](https://developers.buffer.com/reference.html#type/PromoteContentItemDraftToPostsInput) ⚠️ Experimental
Input for promoteContentItemDraftToPosts.
Fields 3
id : [ContentItemId](https://developers.buffer.com/reference.html#type/ContentItemId)!
The content item to promote.
posts : [[CreatePostInput](https://developers.buffer.com/reference.html#type/CreatePostInput)!]!
The channel-specific posts to create, one per channel. Provide at least one post, and at most one post per channel.
tagIds : [[TagId](https://developers.buffer.com/reference.html#type/TagId)!]
Tags to apply to this content item. Omit to keep the current tags. An empty list or null removes them all.
INPUT [RemovePostFromContentItemInput](https://developers.buffer.com/reference.html#type/RemovePostFromContentItemInput) ⚠️ Experimental
Input for removePostFromContentItem.
Fields 2
id : [ContentItemId](https://developers.buffer.com/reference.html#type/ContentItemId)!
The content item to remove the post from.
postId : [PostId](https://developers.buffer.com/reference.html#type/PostId)!
The post to remove from a content item.
INPUT [RetweetMetadataInput](https://developers.buffer.com/reference.html#type/RetweetMetadataInput)
Information about the initial Tweet that was retweeted
Fields 2
id : String!
Retweet ID
comment : String
Optional user comment shown above the embedded retweet
INPUT [SearchInstagramAudioCatalogInput](https://developers.buffer.com/reference.html#type/SearchInstagramAudioCatalogInput) ⚠️ Experimental
Input for searching both Instagram audio catalogs.
Fields 2
channelId : [ChannelId](https://developers.buffer.com/reference.html#type/ChannelId)!
Instagram channel used to authorize the search.
query : String!
Search text. Must not be blank.
INPUT [SearchInstagramAudioInput](https://developers.buffer.com/reference.html#type/SearchInstagramAudioInput) ⚠️ Experimental
Input for searching Instagram audio for one channel.
Fields 3
audioType : [InstagramAudioType](https://developers.buffer.com/reference.html#type/InstagramAudioType)!
Music or original sound catalog
channelId : [ChannelId](https://developers.buffer.com/reference.html#type/ChannelId)!
Instagram channel to search audio for
query : String!
Search text. Required. Use trendingInstagramAudio for trending results.
INPUT [SubstackPostMetadataInput](https://developers.buffer.com/reference.html#type/SubstackPostMetadataInput)
Substack post metadata
Fields 1
linkAttachment : [LinkAttachmentInput](https://developers.buffer.com/reference.html#type/LinkAttachmentInput)
Link attachment. Mutually exclusive with a non-empty `assets` array — input providing both is rejected.
INPUT [ThreadedPostInput](https://developers.buffer.com/reference.html#type/ThreadedPostInput)
A post authored by the user which is posted to a thread. This is commonly used for long-format twitter and meta threads posts to allow authored content to span multiple threads. Threads are represented as a list of replies, each replying to the previous one. The first item in the list is the root post of the thread and should match the top-level `text` on the post input; the remaining items are replies.
Fields 3
assets : [[AssetInput](https://developers.buffer.com/reference.html#type/AssetInput)!]!
Ordered list of assets on this threaded post
metadata : [ThreadItemMetadataInput](https://developers.buffer.com/reference.html#type/ThreadItemMetadataInput)
Service-specific fields for this threaded post
text : String
The text body content of the threaded post
INPUT [ThreadItemBlueskyMetadataInput](https://developers.buffer.com/reference.html#type/ThreadItemBlueskyMetadataInput)
Bluesky fields on a single item of a thread
Fields 1
linkAttachment : [LinkAttachmentInput](https://developers.buffer.com/reference.html#type/LinkAttachmentInput)
Link attachment. Mutually exclusive with a non-empty `assets` array — input providing both is rejected.
INPUT [ThreadItemMetadataInput](https://developers.buffer.com/reference.html#type/ThreadItemMetadataInput)
Service-specific fields on a single item of a thread. The key must match the channel's service; input under any other key is rejected.
Fields 2
bluesky : [ThreadItemBlueskyMetadataInput](https://developers.buffer.com/reference.html#type/ThreadItemBlueskyMetadataInput)
Bluesky fields for this thread item
threads : [ThreadItemThreadsMetadataInput](https://developers.buffer.com/reference.html#type/ThreadItemThreadsMetadataInput)
Threads fields for this thread item
INPUT [ThreadItemThreadsMetadataInput](https://developers.buffer.com/reference.html#type/ThreadItemThreadsMetadataInput)
Threads fields on a single item of a thread
Fields 1
linkAttachment : [LinkAttachmentInput](https://developers.buffer.com/reference.html#type/LinkAttachmentInput)
Link attachment. Mutually exclusive with a non-empty `assets` array — input providing both is rejected.
INPUT [ThreadsPostMetadataInput](https://developers.buffer.com/reference.html#type/ThreadsPostMetadataInput)
Threads post metadata
Fields 6
linkAttachment : [LinkAttachmentInput](https://developers.buffer.com/reference.html#type/LinkAttachmentInput)
Link attachment. Mutually exclusive with a non-empty `assets` array — input providing both is rejected.
locationId : String
LocationId associated with the post
locationName : String
Location name associated with the post
thread : [[ThreadedPostInput](https://developers.buffer.com/reference.html#type/ThreadedPostInput)!]
The ordered list of posts that make up the thread (not paginated). This array is the source of truth for what gets published: every post in the thread, including the root post, must be provided here. Posts are published in order, each replying to the previous one. The first item is the root post and should match the top-level `text` on the post input.
topic : String
Topic associated with the post
type : [PostType](https://developers.buffer.com/reference.html#type/PostType)
The type of the post
INPUT [TikTokPostMetadataInput](https://developers.buffer.com/reference.html#type/TikTokPostMetadataInput)
TikTok post metadata
Fields 2
isAiGenerated : Boolean
Whether the post discloses AI-generated content (TikTok video only)
title : String
The title of the TikTok post (for photo posts)
INPUT [TrendingInstagramAudioInput](https://developers.buffer.com/reference.html#type/TrendingInstagramAudioInput) ⚠️ Experimental
Input for trending Instagram audio for one channel.
Fields 2
audioType : [InstagramAudioType](https://developers.buffer.com/reference.html#type/InstagramAudioType)!
Music or original sound catalog
channelId : [ChannelId](https://developers.buffer.com/reference.html#type/ChannelId)!
Instagram channel to load trending audio for
INPUT [TwitterPostMetadataInput](https://developers.buffer.com/reference.html#type/TwitterPostMetadataInput)
Twitter post metadata
Fields 3
isAiGenerated : Boolean
Whether the post discloses AI-generated content (original tweets only, never retweets)
retweet : [RetweetMetadataInput](https://developers.buffer.com/reference.html#type/RetweetMetadataInput)
The details of the tweet being retweeted
thread : [[ThreadedPostInput](https://developers.buffer.com/reference.html#type/ThreadedPostInput)!]
The ordered list of posts that make up the thread (not paginated). This array is the source of truth for what gets published: every post in the thread, including the root post, must be provided here. Posts are published in order, each replying to the previous one. The first item is the root post and should match the top-level `text` on the post input.
INPUT [UpdateContentItemDraftInput](https://developers.buffer.com/reference.html#type/UpdateContentItemDraftInput) ⚠️ Experimental
Input for updateContentItemDraft.
Fields 4
id : [ContentItemId](https://developers.buffer.com/reference.html#type/ContentItemId)!
The content item whose channel-less draft is replaced.
draft : [DraftContentInput](https://developers.buffer.com/reference.html#type/DraftContentInput)!
The new draft content. Replaces the current draft in full.
tagIds : [[TagId](https://developers.buffer.com/reference.html#type/TagId)!]
Tags to apply to this content item. Omit to keep the current tags. An empty list or null removes them all.
targetDate : [DateTime](https://developers.buffer.com/reference.html#type/DateTime)
Date indicating when this piece of content should go out. This is a planning aid only and does not schedule any posts. Omit to preserve the existing target date. Null clears it.
INPUT [UpdateContentItemInput](https://developers.buffer.com/reference.html#type/UpdateContentItemInput) ⚠️ Experimental
Input for updateContentItem. Only the fields provided are changed. Omitted fields keep their current value.
Fields 3
id : [ContentItemId](https://developers.buffer.com/reference.html#type/ContentItemId)!
The content item to update.
targetDate : [DateTime](https://developers.buffer.com/reference.html#type/DateTime)
Omit to preserve the existing target date. Null clears it.
title : String
Omit to preserve the existing title. Null clears it.
INPUT [UpdatePostTemplateInput](https://developers.buffer.com/reference.html#type/UpdatePostTemplateInput)
Input for an end user updating a post template. Buffer-curated taxonomy fields are ignored; setting them is only available to official Buffer clients.
Fields 6
id : [PostTemplateId](https://developers.buffer.com/reference.html#type/PostTemplateId)!
The ID of the template to update.
body : String
The main content body of the template, may contain {{placeholders}}.
description : String
A short user-facing description of the template.
emoji : String
The emoji associated with the template.
title : String
The title of the template.
visibility : [PostTemplateVisibility](https://developers.buffer.com/reference.html#type/PostTemplateVisibility)
`public` is rejected — it is only available to official Buffer clients.
INPUT [UpdateSnippetInput](https://developers.buffer.com/reference.html#type/UpdateSnippetInput) ⚠️ Experimental
Input for the updateSnippet mutation. Both name and text are replaced.
Fields 4
id : [SnippetId](https://developers.buffer.com/reference.html#type/SnippetId)!
The snippet to update.
name : String!
The new display name of the snippet.
organizationId : [OrganizationId](https://developers.buffer.com/reference.html#type/OrganizationId)!
The organization that owns the snippet.
text : String!
The new hashtags, as the text that is inserted into a post.
INPUT [UpdateTagInput](https://developers.buffer.com/reference.html#type/UpdateTagInput) ⚠️ Experimental
Input for updating a tag.
Fields 2
id : [TagId](https://developers.buffer.com/reference.html#type/TagId)!
The tag to update. Its organization is taken from the tag itself, and the caller must be an administrator of that organization.
tag : [TagToUpdateInput](https://developers.buffer.com/reference.html#type/TagToUpdateInput)!
The name and color to set on the tag.
INPUT [UserTagInput](https://developers.buffer.com/reference.html#type/UserTagInput)
User tag in the image
Fields 3
handle : String!
The handle (username) of the account to tag, without the leading @.
x : Float!
Horizontal position of the tag as a normalized decimal float between 0.0 and 1.0 - the fraction of the image width from the left edge (0.5 is the horizontal center). Pass a number, not a string, and do not use pixel coordinates; to convert, divide the pixel X by the image width.
y : Float!
Vertical position of the tag as a normalized decimal float between 0.0 and 1.0 - the fraction of the image height from the top edge (0.5 is the vertical center). Pass a number, not a string, and do not use pixel coordinates; to convert, divide the pixel Y by the image height.
INPUT [VideoAssetInput](https://developers.buffer.com/reference.html#type/VideoAssetInput)
Video asset
Fields 3
metadata : [VideoMetadataInput](https://developers.buffer.com/reference.html#type/VideoMetadataInput)
Video specific metadata
thumbnailUrl : String
Do not use: social networks do not accept custom video thumbnail images, and the API rejects video assets that set this field. To choose the video thumbnail, set `metadata.thumbnailOffset` to select a frame from the video (supported for Instagram, TikTok, and Pinterest only).
url : String!
URL to the file source
INPUT [VideoMetadataInput](https://developers.buffer.com/reference.html#type/VideoMetadataInput)
Video metadata
Fields 2
thumbnailOffset : Int
Offset of the thumbnail chosen for the video, in ms
title : String
Video title
INPUT [YoutubePostMetadataInput](https://developers.buffer.com/reference.html#type/YoutubePostMetadataInput)
Youtube post metadata
Fields 8
categoryId : String
Youtube Category ID, one ID of this list: ID: 1 -> Film & Animation ID: 2 -> Autos & Vehicles ID: 10 -> Music ID: 15 -> Pets & Animals ID: 17 -> Sports ID: 19 -> Travel & Events ID: 20 -> Gaming ID: 22 -> People & Blogs ID: 23 -> Comedy ID: 24 -> Entertainment ID: 25 -> News & Politics ID: 26 -> Howto & Style ID: 27 -> Education ID: 28 -> Science & Technology ID: 29 -> Nonprofits & Activism Required on create; optional on edit (omitted preserves existing value).
embeddable : Boolean
Indicates whether the video allows embedding (default: true)
isAiGenerated : Boolean
Whether the post discloses AI-generated content
license : [YoutubeLicense](https://developers.buffer.com/reference.html#type/YoutubeLicense)
Video license (default: youtube)
madeForKids : Boolean
Indicates whether the video is suitable for kids (default: false)
notifySubscribers : Boolean
Indicates whether to notify subscribers on publish video (default: true)
privacy : [YoutubePrivacy](https://developers.buffer.com/reference.html#type/YoutubePrivacy)
Privacy setting for post (default: public)
title : String
Title of the Youtube post. Required on create; optional on edit (omitted preserves existing value).
### Enums 27
ENUM [AnnotationType](https://developers.buffer.com/reference.html#type/AnnotationType)
List of possible types for an annotation
ENUM [AssetType](https://developers.buffer.com/reference.html#type/AssetType)
Asset types
ENUM [ContentItemAction](https://developers.buffer.com/reference.html#type/ContentItemAction) ⚠️ Experimental
Actions the calling actor can take on a `ContentItem`. The server computes this set from the same rules the content item mutations enforce. A client reads it to drive UI affordances instead of deriving the rules itself. The set carries an action only when a client can offer it on this one item. An action whose answer is the same for every item in a response drives no affordance, so it stays out. Read access is one of those: the API returns only a content item the actor may read.
ENUM [DateTimePresence](https://developers.buffer.com/reference.html#type/DateTimePresence)
Presence filter for nullable date fields. When filtering the same field, absent dates cannot also match a date comparator range.
ENUM [GoogleBusinessPostActionType](https://developers.buffer.com/reference.html#type/GoogleBusinessPostActionType)
List of possible types for GBP cta
ENUM [InstagramAudioType](https://developers.buffer.com/reference.html#type/InstagramAudioType) ⚠️ Experimental
Instagram audio catalog type from Meta's Audio API.
ENUM [NoteAction](https://developers.buffer.com/reference.html#type/NoteAction)
List of possible actions that can be performed on a note
ENUM [NoteType](https://developers.buffer.com/reference.html#type/NoteType)
The type of a note.
ENUM [NotificationStatus](https://developers.buffer.com/reference.html#type/NotificationStatus)
List of possible statuses for a notification
ENUM [PostAction](https://developers.buffer.com/reference.html#type/PostAction)
List of possible actions that can be performed on a Post
ENUM [PostApprovalChange](https://developers.buffer.com/reference.html#type/PostApprovalChange)
A change to a post's approval state, for a post that is already a draft.
ENUM [PostingGoalStatus](https://developers.buffer.com/reference.html#type/PostingGoalStatus)
PostingGoalStatus is used to track the status of a posting goal.
ENUM [PostMetricType](https://developers.buffer.com/reference.html#type/PostMetricType)
List of possible metrics available for a Post. Values fall into three groups: - **Cross-network normalized** (reactions, comments, shares, reposts, reach, impressions, views, clicks, engagementRate): Used wherever a concept maps cleanly across networks. Per-network adapters normalize their native names (e.g., Instagram `likes` → `reactions`, Twitter `retweets` → `reposts`). - **Network-specific** (saves, follows, quotes, viewers, totalTimeWatched, averageTimeWatched, likes, freeSubscriptions, paidSubscriptions): Real metrics that don't have a cross-network equivalent. `likes` is intentionally distinct from `reactions` on Facebook — Facebook's Graph API surfaces them separately. `freeSubscriptions` and `paidSubscriptions` are Substack's per-Note subscription attribution; no other network reports it. - **Aggregation-only** (postCount): Meaningful only on aggregate endpoints; never emitted per-post. Deprecated values are pre-normalization legacy or tied to features being removed. They're kept in the enum for backwards compatibility until clients migrate.
ENUM [PostMetricUnit](https://developers.buffer.com/reference.html#type/PostMetricUnit)
The unit representing the value of a PostMetric.
ENUM [PostSortableKey](https://developers.buffer.com/reference.html#type/PostSortableKey)
Key of collection to use for sorting
ENUM [PostStatus](https://developers.buffer.com/reference.html#type/PostStatus)
List of possible statuses for a Post
ENUM [PostTemplateVisibility](https://developers.buffer.com/reference.html#type/PostTemplateVisibility) 🧪 Preview
The visibility level of a post template. `public` is reserved for Buffer-curated templates; setting it is only available to official Buffer clients.
ENUM [PostType](https://developers.buffer.com/reference.html#type/PostType)
List of possible types for a Post. Some services may have different types (e.g., Instagram has story, reel, post but Twitter has only post)
ENUM [PostTypeFacebook](https://developers.buffer.com/reference.html#type/PostTypeFacebook)
List of specific post types available for Facebook
ENUM [PostTypeGoogleBusiness](https://developers.buffer.com/reference.html#type/PostTypeGoogleBusiness)
List of specific post types available for Google Business profiles
ENUM [PostVia](https://developers.buffer.com/reference.html#type/PostVia)
List of possible ways to create a Post
ENUM [QueuePosition](https://developers.buffer.com/reference.html#type/QueuePosition) ⚠️ Experimental
Target position within a channel's queue that a post can be moved to.
ENUM [SchedulingType](https://developers.buffer.com/reference.html#type/SchedulingType)
Indicates whether the post was scheduled for notification publishing or automatic publishing
ENUM [ShareMode](https://developers.buffer.com/reference.html#type/ShareMode)
How the post is being scheduled.
ENUM [SortDirection](https://developers.buffer.com/reference.html#type/SortDirection)
Direction to sort the results by.
ENUM [YoutubeLicense](https://developers.buffer.com/reference.html#type/YoutubeLicense)
List of license types
ENUM [YoutubePrivacy](https://developers.buffer.com/reference.html#type/YoutubePrivacy)
List of privacy types
### Scalars 8
SCALAR [ContentItemId](https://developers.buffer.com/reference.html#type/ContentItemId) ⚠️ Experimental
A unique identifier for a content item.
SCALAR [DraftContentId](https://developers.buffer.com/reference.html#type/DraftContentId) ⚠️ Experimental
A unique identifier for a channel-less draft's content.
SCALAR [DraftId](https://developers.buffer.com/reference.html#type/DraftId)
The `DraftId` scalar represents the ID of a Buffer Draft
SCALAR [NoteId](https://developers.buffer.com/reference.html#type/NoteId)
The `NoteId` scalar represents the ID of a Buffer Note
SCALAR [PostId](https://developers.buffer.com/reference.html#type/PostId)
The `PostId` scalar represents the ID of a Buffer Post
SCALAR [PostTemplateId](https://developers.buffer.com/reference.html#type/PostTemplateId)
The `PostTemplateId` scalar represents the ID of a Post Template.
SCALAR [SnippetId](https://developers.buffer.com/reference.html#type/SnippetId)
The `SnippetId` scalar represents the ID of a Snippet.
SCALAR [URL](https://developers.buffer.com/reference.html#type/URL)
The `URL` scalar represents a valid URL
## Ideas
### Queries 2
QUERY ideaGroups (input: [IdeaGroupsInput](https://developers.buffer.com/reference.html#type/IdeaGroupsInput)!) : [[IdeaGroup](https://developers.buffer.com/reference.html#type/IdeaGroup)!]!
Retrieves idea groups based on the provided input parameters.
Arguments  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| input Required  |  [IdeaGroupsInput](https://developers.buffer.com/reference.html#type/IdeaGroupsInput)!  |  Input for retrieving idea groups.   |  
Example Response

```
{
  "data": {
    "ideaGroups": [
      {
        "id": "...",
        "isLocked": true,
        "name": "..."
      }
    ]
  }
}
```

QUERY ideas (after: String, first: Int, input: [IdeasInput](https://developers.buffer.com/reference.html#type/IdeasInput)!) : [IdeasConnection](https://developers.buffer.com/reference.html#type/IdeasConnection)!
Fetch a paginated list of ideas with optional filtering
Arguments  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| after Optional  | String  |  Cursor for pagination, marks where to start fetching from   |  
| first Optional  | Int  |  Maximum number of items to return   |  
| input Required  |  [IdeasInput](https://developers.buffer.com/reference.html#type/IdeasInput)!  |  Filtering criteria for the ideas list   |  
Example Response

```
{
  "data": {
    "ideas": {
      "edges": [
        {
          "cursor": "...",
          "node": {}
        }
      ],
      "pageInfo": {
        "endCursor": "...",
        "hasNextPage": true,
        "hasPreviousPage": true,
        "startCursor": "..."
      }
    }
  }
}
```

### Mutations 1
MUTATION createIdea (input: [CreateIdeaInput](https://developers.buffer.com/reference.html#type/CreateIdeaInput)!) : [CreateIdeaPayload](https://developers.buffer.com/reference.html#type/CreateIdeaPayload)!
Create a new idea with the given content and metadata
Arguments  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| input Required  |  [CreateIdeaInput](https://developers.buffer.com/reference.html#type/CreateIdeaInput)!  |  Input to create an idea   |  
Example Response

```
{
  "data": {
    "createIdea": {}
  }
}
```

### Outputs 3
OUTPUT [IdeaGroup](https://developers.buffer.com/reference.html#type/IdeaGroup)
Idea groups are used to organize ideas in the board
Fields 3
id : ID!
Unique identifier for the idea group.
isLocked : Boolean!
Whether the idea group is locked.
name : String!
The name of the idea group.
OUTPUT [IdeasConnection](https://developers.buffer.com/reference.html#type/IdeasConnection)
Relay connection for paginated ideas.
Fields 2
edges : [[IdeaEdge](https://developers.buffer.com/reference.html#type/IdeaEdge)!]!
List of idea edges containing the ideas and their cursors
pageInfo : [PaginationPageInfo](https://developers.buffer.com/reference.html#type/PaginationPageInfo)!
Pagination metadata including hasNextPage and endCursor
OUTPUT [CreateIdeaPayload](https://developers.buffer.com/reference.html#type/CreateIdeaPayload)
createIdea response (including errors)
### Types 8
TYPE [Idea](https://developers.buffer.com/reference.html#type/Idea)
Ideas are the main entity in the create space
Fields 7
id : ID!
Unique identifier for the idea
content : [IdeaContent](https://developers.buffer.com/reference.html#type/IdeaContent)!
The actual content and metadata of the idea
groupId : ID
ID of the group this idea belongs to (if any)
organizationId : ID!
ID of the organization that owns this idea
position : Float
Numerical position for ordering within a group
createdAt : Int!
Unix timestamp of when the idea was created
updatedAt : Int!
Unix timestamp of when the idea was last modified
TYPE [IdeaContent](https://developers.buffer.com/reference.html#type/IdeaContent)
Content of an idea
Fields 7
aiAssisted : Boolean!
Indicates whether AI tools were used in creating this idea
date : [DateTime](https://developers.buffer.com/reference.html#type/DateTime)
DateTime set by user associated with the idea - this often reflects a target publish date.
media : [[IdeaMedia](https://developers.buffer.com/reference.html#type/IdeaMedia)!]
List of media items attached to the idea
services : [[Service](https://developers.buffer.com/reference.html#type/Service)!]!
Services tagged by the user - this is typically used to annotate ideas with their target services
tags : [[PublishingTag](https://developers.buffer.com/reference.html#type/PublishingTag)!]!
Tags used to categorize and organize the idea
text : String
Main body text or description of the idea
title : String
Title or headline of the idea
TYPE [IdeaEdge](https://developers.buffer.com/reference.html#type/IdeaEdge)
Pagination type for Ideas
Fields 2
cursor : String!
Opaque cursor for pagination, used to fetch subsequent pages
node : [Idea](https://developers.buffer.com/reference.html#type/Idea)!
The idea object
TYPE [IdeaResponse](https://developers.buffer.com/reference.html#type/IdeaResponse)
createIdea response type
Fields 2
idea : [Idea](https://developers.buffer.com/reference.html#type/Idea)
The affected idea
refreshIdeas : Boolean!
If true, the client should refresh the ideas list because other ideas might have been moved
TYPE [LimitReachedError](https://developers.buffer.com/reference.html#type/LimitReachedError)
Error returned when the limit is reached
Fields 1
message : String!
Error message
TYPE [PaginationPageInfo](https://developers.buffer.com/reference.html#type/PaginationPageInfo)
Information to aid in pagination.
Fields 4
endCursor : String
The last cursor in the list. It can be used to fetch the next page.
hasNextPage : Boolean!
When set to true, it means there is a next page available.
hasPreviousPage : Boolean!
When set to true, it means there is a previous page available. Will always return false for now as we only support forward pagination.
startCursor : String
The first cursor in the list. It can be used to fetch the previous page.
TYPE [UnauthorizedError](https://developers.buffer.com/reference.html#type/UnauthorizedError)
Error returned when the user is not authorized to perform the action
Fields 1
message : String!
Error message
TYPE [UnexpectedError](https://developers.buffer.com/reference.html#type/UnexpectedError)
Error returned when unexpected error occurs
Fields 1
message : String!
Error message
### Inputs 6
INPUT [CreateIdeaInput](https://developers.buffer.com/reference.html#type/CreateIdeaInput)
createIdea input type
Fields 5
content : [IdeaContentInput](https://developers.buffer.com/reference.html#type/IdeaContentInput)!
Content and metadata for the new idea
cta : String
Call-to-action identifier for analytics tracking
group : [IdeaGroupInput](https://developers.buffer.com/reference.html#type/IdeaGroupInput)
Group placement (null for unassigned group)
organizationId : ID!
Organization ID that will own the idea
templateId : String
Template ID used to create the idea
INPUT [IdeaContentInput](https://developers.buffer.com/reference.html#type/IdeaContentInput)
content input for creating/updating an idea
Fields 7
aiAssisted : Boolean
Whether AI tools were used in creation
date : [DateTime](https://developers.buffer.com/reference.html#type/DateTime)
Target date for the idea, often used for planning publish schedules
media : [[IdeaMediaInput](https://developers.buffer.com/reference.html#type/IdeaMediaInput)!]
List of media items to attach
services : [[Service](https://developers.buffer.com/reference.html#type/Service)!]
Services associated with the idea for targeting specific platforms
tags : [[TagInput](https://developers.buffer.com/reference.html#type/TagInput)!]
Tags to categorize the idea
text : String
Main body text or description
title : String
Title or headline of the idea
INPUT [IdeaGroupInput](https://developers.buffer.com/reference.html#type/IdeaGroupInput)
idea group input for create/update
Fields 2
groupId : ID
Target group ID (null for unassigned group)
placeAfterId : ID
ID of idea to place after (null for top position)
INPUT [IdeaGroupsInput](https://developers.buffer.com/reference.html#type/IdeaGroupsInput)
Input type for retrieving idea groups by organization ID.
Fields 1
organizationId : ID!
Unique identifier for the organization.
INPUT [IdeasGroupFilter](https://developers.buffer.com/reference.html#type/IdeasGroupFilter)
Selects which ideas to return by group membership. Exactly one field must be provided (enforced by @oneOf). To return ideas from all groups, omit `groupFilter` on IdeasInput rather than setting a field here.
Fields 2
groups : [ID!]
Return only ideas that belong to these specific groups (union/OR).
membership : [IdeaGroupMembership](https://developers.buffer.com/reference.html#type/IdeaGroupMembership)
Return ideas by a group-membership bucket rather than by specific group IDs.
INPUT [IdeasInput](https://developers.buffer.com/reference.html#type/IdeasInput)
Filtering criteria for the ideas list.
Fields 3
groupFilter : [IdeasGroupFilter](https://developers.buffer.com/reference.html#type/IdeasGroupFilter)
Filter ideas by group membership. Omit this field entirely to return ideas across all groups.
organizationId : [OrganizationId](https://developers.buffer.com/reference.html#type/OrganizationId)!
The organization to fetch ideas from.
tagsFilter : [TagComparator](https://developers.buffer.com/reference.html#type/TagComparator)
Filter ideas by tags using TagComparator.
### Enums 1
ENUM [IdeaGroupMembership](https://developers.buffer.com/reference.html#type/IdeaGroupMembership)
Named buckets for filtering ideas by their group membership.
### Scalars 1
SCALAR [IdeaId](https://developers.buffer.com/reference.html#type/IdeaId)
The `IdeaId` scalar represents the ID of a Buffer Idea
## Organizations
### Types 3
TYPE [MemberConnection](https://developers.buffer.com/reference.html#type/MemberConnection)
Represents the members connection edge. Later, we can add the list of members with the page info to follow our connection edge pattern.
Fields 1
totalCount : Int!
The total count of team members counting the org owner and team members from the Publish DB.
TYPE [Organization](https://developers.buffer.com/reference.html#type/Organization)
Organization is a representation of a Buffer Organization.
Fields 7
id : [OrganizationId](https://developers.buffer.com/reference.html#type/OrganizationId)!
The ID of the organization.
channelCount : Int!
The total number of channels connected to the organization.
limits : [OrganizationLimits](https://developers.buffer.com/reference.html#type/OrganizationLimits)!
The limits of the organization. Can be used to check if the organization has reached the limit of channels, members, etc.
members : [MemberConnection](https://developers.buffer.com/reference.html#type/MemberConnection)!
The members of the organization. Can be used to check the total number of members in the organization. In the future, it might contain more information about the members.
name : String!
The name of the organization.
ownerEmail : String!
The owner email of the organization.
shouldEnforce2FASetup : Boolean!
Whether the requesting actor should be sent through 2FA setup before they can use this organization. Derived: true only when the org has `settings.enforce2FA` ON and the actor has no 2FA configured on their own account. This is the single source of truth for the forced-2FA gate; app-shell and publish-frontend redirect to the setup flow when it's true. Exposed to the API gateway so any stitched consumer reads the same value.
TYPE [OrganizationLimits](https://developers.buffer.com/reference.html#type/OrganizationLimits)
Resource limits for an organization including channels, members, and content limits
Fields 11
channels : Int!
The maximum number of channels allowed for the organization.
generateContent : Int!
The maximum number of content generations allowed for the organization.
ideaGroups : Int!
The maximum number of idea groups allowed for the organization.
ideas : Int!
The maximum number of ideas allowed for the organization.
members : Int!
The maximum number of members allowed for the organization.
postTemplates : Int!
The maximum number of post templates allowed for the organization.
savedReplies : Int!
The maximum number of saved replies allowed for the organization.
scheduledPosts : Int!
The maximum number of scheduled posts allowed for the organization.
scheduledStoriesPerChannel : Int!
The maximum number of scheduled stories allowed per channel.
scheduledThreadsPerChannel : Int!
The maximum number of scheduled threads allowed per channel.
tags : Int!
The maximum number of tags allowed for the organization.
### Inputs 1
INPUT [OrganizationFilterInput](https://developers.buffer.com/reference.html#type/OrganizationFilterInput)
Allow retrieving a specific Organization
Fields 1
organizationId : String!
### Scalars 1
SCALAR [OrganizationId](https://developers.buffer.com/reference.html#type/OrganizationId)
The `OrganizationId` scalar represents the ID of a Buffer Organization
## Other
### Queries 4
QUERY configuration (input: [ConfigurationInput](https://developers.buffer.com/reference.html#type/ConfigurationInput)!) : [Configuration](https://developers.buffer.com/reference.html#type/Configuration)! ⚠️ Experimental
Global, per-organization configuration: the connected `channels` the actor can view (with per-feature authorization) plus the service-level capability catalog (`services`). One round trip for every capability domain; clients select only what they need.
Arguments  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| input Required  |  [ConfigurationInput](https://developers.buffer.com/reference.html#type/ConfigurationInput)!  |  Input for the configuration query.   |  
Example Response

```
{
  "data": {
    "configuration": {
      "channels": [
        {
          "authorizationStatus": [
            {}
          ],
          "channelId": "...",
          "channelType": "account",
          "content": [
            {}
          ]
        }
      ],
      "services": [
        {
          "channelType": "account",
          "content": [
            {}
          ],
          "engagement": [
            {}
          ],
          "service": "bluesky"
        }
      ]
    }
  }
}
```

QUERY contentItem (input: [ContentItemInput](https://developers.buffer.com/reference.html#type/ContentItemInput)!) : [ContentItem](https://developers.buffer.com/reference.html#type/ContentItem)! ⚠️ Experimental
Fetch a single content item by id. Errors if no content item with that id exists.
This API is an early preview and can change without a deprecation period.
Arguments  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| input Required  |  [ContentItemInput](https://developers.buffer.com/reference.html#type/ContentItemInput)!  |  Input for fetching a single content item.   |  
Example Response

```
{
  "data": {
    "contentItem": {
      "id": "...",
      "accountId": "...",
      "allowedActions": [
        "deleteContentItem"
      ],
      "author": {
        "id": "...",
        "avatar": "...",
        "email": "...",
        "isDeleted": true
      }
    }
  }
}
```

QUERY contentItems (after: String, first: Int, input: [ContentItemsInput](https://developers.buffer.com/reference.html#type/ContentItemsInput)!) : [ContentItemsConnection](https://developers.buffer.com/reference.html#type/ContentItemsConnection)! ⚠️ Experimental
Fetch an organization's content items in the requested order, newest first by default. Uses standard cursor pagination: pass the previous page's `pageInfo.endCursor` as `after` to fetch the next page. Requesting more than 100 items in a single page is rejected.
This API is an early preview and can change without a deprecation period.
Arguments  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| after Optional  | String  |  The cursor after which to return results. Cursors are opaque: treat them as a black box and reset to null when the input changes, since a cursor from a different result set produces undefined behavior.   |  
| first Optional  | Int  |  The number of content items to return, up to 100.   |  
| input Required  |  [ContentItemsInput](https://developers.buffer.com/reference.html#type/ContentItemsInput)!  |  Input for listing content items.   |  
Example Response

```
{
  "data": {
    "contentItems": {
      "edges": [
        {
          "cursor": "...",
          "node": {}
        }
      ],
      "pageInfo": {
        "endCursor": "...",
        "hasNextPage": true,
        "hasPreviousPage": true,
        "startCursor": "..."
      },
      "totalCount": 0
    }
  }
}
```

QUERY snippets (after: String, first: Int, input: [SnippetsInput](https://developers.buffer.com/reference.html#type/SnippetsInput)!) : [SnippetsConnection](https://developers.buffer.com/reference.html#type/SnippetsConnection)! ⚠️ Experimental
Returns the snippets of an organization, sorted by name. Uses standard cursor pagination: pass the previous page's `pageInfo.endCursor` as `after` to fetch the next page. Requesting more than 100 snippets in a single page is rejected. A cursor whose snippet was deleted reports a BAD_USER_INPUT error. Fetch again from the first page.
Arguments  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| after Optional  | String  |  The cursor after which to return results. Cursors are opaque: treat them as a black box.   |  
| first Optional  | Int  |  The number of snippets to return, from 1 to 100. Defaults to 10.   |  
| input Required  |  [SnippetsInput](https://developers.buffer.com/reference.html#type/SnippetsInput)!  |  The query input.   |  
Example Response

```
{
  "data": {
    "snippets": {
      "edges": [
        {
          "cursor": "...",
          "node": {}
        }
      ],
      "pageInfo": {
        "endCursor": "...",
        "hasNextPage": true,
        "hasPreviousPage": true,
        "startCursor": "..."
      }
    }
  }
}
```

### Mutations 5
MUTATION createContentItem (input: [CreateContentItemInput](https://developers.buffer.com/reference.html#type/CreateContentItemInput)!) : [CreateContentItemPayload](https://developers.buffer.com/reference.html#type/CreateContentItemPayload)! ⚠️ Experimental
Create a content item together with all of its channel-specific post variants in a single operation. Validation is all-or-nothing: if any variant fails validation, no content item and no variants are created. Variants that fail while being processed after creation are reported per channel in the failure payload; the content item and its variants are still created in that case.
This API is an early preview and can change without a deprecation period.
Arguments  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| input Required  |  [CreateContentItemInput](https://developers.buffer.com/reference.html#type/CreateContentItemInput)!  |  Input for createContentItem.   |  
Example Response

```
{
  "data": {
    "createContentItem": {}
  }
}
```

MUTATION createContentItemDraft (input: [CreateContentItemDraftInput](https://developers.buffer.com/reference.html#type/CreateContentItemDraftInput)!) : [CreateContentItemDraftPayload](https://developers.buffer.com/reference.html#type/CreateContentItemDraftPayload)! ⚠️ Experimental
Create a content item holding a channel-less draft, before any channels are selected. No network-specific validation applies to the draft content. The draft needs text or at least one asset.
This API is an early preview and can change without a deprecation period.
Arguments  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| input Required  |  [CreateContentItemDraftInput](https://developers.buffer.com/reference.html#type/CreateContentItemDraftInput)!  |  Input for createContentItemDraft.   |  
Example Response

```
{
  "data": {
    "createContentItemDraft": {}
  }
}
```

MUTATION createSnippet (input: [CreateSnippetInput](https://developers.buffer.com/reference.html#type/CreateSnippetInput)!) : [CreateSnippetPayload](https://developers.buffer.com/reference.html#type/CreateSnippetPayload)! ⚠️ Experimental
Creates a snippet in an organization.
Arguments  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| input Required  |  [CreateSnippetInput](https://developers.buffer.com/reference.html#type/CreateSnippetInput)!  |  Input for createSnippet.   |  
Example Response

```
{
  "data": {
    "createSnippet": {}
  }
}
```

MUTATION deleteContentItem (input: [DeleteContentItemInput](https://developers.buffer.com/reference.html#type/DeleteContentItemInput)!) : [DeleteContentItemPayload](https://developers.buffer.com/reference.html#type/DeleteContentItemPayload)! ⚠️ Experimental
Delete a content item: the item itself and any posts created from it. Deletion is all-or-nothing. Every post must be deletable on its own, or nothing is deleted and every blocked post is reported at once. A post can only be deleted while it is a draft, awaiting approval, scheduled, or failed, so an item cannot be deleted while any of its posts is publishing or already published. An item still holding a channel-less draft has no posts, so nothing blocks it. An error can also be reported when a post could not be fully processed after the deletion already took effect; re-fetch before retrying.
Deleting a content item also deletes the team notes on the item and on its posts. The notes are removed shortly after the item is deleted.
This API is an early preview and can change without a deprecation period.
Arguments  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| input Required  |  [DeleteContentItemInput](https://developers.buffer.com/reference.html#type/DeleteContentItemInput)!  |  Input for deleteContentItem.   |  
Example Response

```
{
  "data": {
    "deleteContentItem": {}
  }
}
```

MUTATION deleteSnippet (input: [DeleteSnippetInput](https://developers.buffer.com/reference.html#type/DeleteSnippetInput)!) : [DeleteSnippetPayload](https://developers.buffer.com/reference.html#type/DeleteSnippetPayload)! ⚠️ Experimental
Deletes a snippet.
Arguments  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| input Required  |  [DeleteSnippetInput](https://developers.buffer.com/reference.html#type/DeleteSnippetInput)!  |  Input for deleteSnippet.   |  
Example Response

```
{
  "data": {
    "deleteSnippet": {}
  }
}
```

### Outputs 8
OUTPUT [Configuration](https://developers.buffer.com/reference.html#type/Configuration) ⚠️ Experimental
Organization configuration. `channels` carries the per-connected-channel config the actor can view (including per-`Feature` `authorizationStatus`); `services` carries the service-level capability catalog — the engagement and content config for every supported `service` + `channelType`, independent of which channels are connected (e.g. for composing before a channel is connected); `collaborationRoleAbilities` carries the Roles ability catalog. `@public` is set per field rather than on the type, so a field is external only when tagged. A new field is internal until it carries its own `@public`.
Fields 2
channels : [[ChannelConfiguration](https://developers.buffer.com/reference.html#type/ChannelConfiguration)!]!
Per-connected-channel config for every channel the actor can view.
services : [[ServiceConfiguration](https://developers.buffer.com/reference.html#type/ServiceConfiguration)!]!
Service-level capability catalog for every supported service + channel type.
OUTPUT [ContentItemsConnection](https://developers.buffer.com/reference.html#type/ContentItemsConnection) ⚠️ Experimental
A paginated connection of content items.
Fields 3
edges : [[ContentItemEdge](https://developers.buffer.com/reference.html#type/ContentItemEdge)!]!
The list of content item edges.
pageInfo : [PaginationPageInfo](https://developers.buffer.com/reference.html#type/PaginationPageInfo)!
Pagination information for the connection.
totalCount : Int!
The total number of content items matching the request.
OUTPUT [SnippetsConnection](https://developers.buffer.com/reference.html#type/SnippetsConnection) ⚠️ Experimental
A paginated connection of snippets, sorted by name.
Fields 2
edges : [[SnippetEdge](https://developers.buffer.com/reference.html#type/SnippetEdge)!]!
The list of snippet edges.
pageInfo : [PaginationPageInfo](https://developers.buffer.com/reference.html#type/PaginationPageInfo)!
Pagination information for the connection.
OUTPUT [CreateContentItemDraftPayload](https://developers.buffer.com/reference.html#type/CreateContentItemDraftPayload) ⚠️ Experimental
All possible responses for createContentItemDraft.
OUTPUT [CreateContentItemPayload](https://developers.buffer.com/reference.html#type/CreateContentItemPayload) ⚠️ Experimental
All possible responses for createContentItem.
OUTPUT [CreateSnippetPayload](https://developers.buffer.com/reference.html#type/CreateSnippetPayload) ⚠️ Experimental
All possible responses for createSnippet. VoidMutationError reports an empty or too long name or text.
OUTPUT [DeleteContentItemPayload](https://developers.buffer.com/reference.html#type/DeleteContentItemPayload) ⚠️ Experimental
All possible responses for deleteContentItem.
OUTPUT [DeleteSnippetPayload](https://developers.buffer.com/reference.html#type/DeleteSnippetPayload) ⚠️ Experimental
All possible responses for deleteSnippet.
### Types 30
TYPE [ContentItemEdge](https://developers.buffer.com/reference.html#type/ContentItemEdge) ⚠️ Experimental
An edge in a content item connection.
Fields 2
cursor : String!
A cursor for pagination.
node : [ContentItem](https://developers.buffer.com/reference.html#type/ContentItem)!
The content item node at the end of the edge.
TYPE [CountRule](https://developers.buffer.com/reference.html#type/CountRule) ⚠️ Experimental
Bounds how many of a property are allowed. `min` null/absent = no lower bound (optional); `min: 1` = required. `max` null = unlimited. At least one of `min` or `max` is always present — a rule that bounds neither is never emitted.
Fields 3
max : Int
Maximum allowed count. Null = unlimited.
min : Int
Minimum allowed count. Null = no lower bound (optional).
property : [ContentProperty](https://developers.buffer.com/reference.html#type/ContentProperty)!
The content property this rule constrains.
TYPE [CreateContentItemDraftFailure](https://developers.buffer.com/reference.html#type/CreateContentItemDraftFailure) ⚠️ Experimental
createContentItemDraft failure. When any part of the input is invalid, nothing is created.
Fields 2
errors : [[InvalidInputError](https://developers.buffer.com/reference.html#type/InvalidInputError)!]!
The recoverable errors behind this failure.
message : String!
Summary error message.
TYPE [CreateContentItemDraftSuccess](https://developers.buffer.com/reference.html#type/CreateContentItemDraftSuccess) ⚠️ Experimental
Successful createContentItemDraft response.
Fields 1
contentItem : [ContentItem](https://developers.buffer.com/reference.html#type/ContentItem)!
The content item first created for this request, including its current state.
TYPE [CreateContentItemFailure](https://developers.buffer.com/reference.html#type/CreateContentItemFailure) ⚠️ Experimental
createContentItem failure. Every recoverable error is reported together so the caller can surface them all at once. When the input fails validation, no content item and no variants are created. When one or more variants fail while being processed after creation, the content item and all of its variants already exist; the per-channel errors identify the variants that need attention.
Fields 2
errors : [[CreateContentItemError](https://developers.buffer.com/reference.html#type/CreateContentItemError)!]!
The recoverable errors behind this failure.
message : String!
Summary error message.
TYPE [CreateContentItemSuccess](https://developers.buffer.com/reference.html#type/CreateContentItemSuccess) ⚠️ Experimental
Successful createContentItem response.
Fields 1
content : [ContentItem](https://developers.buffer.com/reference.html#type/ContentItem)!
The content item created by this mutation.
TYPE [CreateContentItemVariantInvalidInputError](https://developers.buffer.com/reference.html#type/CreateContentItemVariantInvalidInputError) ⚠️ Experimental
Invalid input for a single post variant in the createContentItem input list.
Fields 2
channelId : [ChannelId](https://developers.buffer.com/reference.html#type/ChannelId)!
Channel targeted by the failing variant.
message : String!
Error message.
TYPE [CreateContentItemVariantLimitReachedError](https://developers.buffer.com/reference.html#type/CreateContentItemVariantLimitReachedError) ⚠️ Experimental
Limit reached for a single post variant in the createContentItem input list.
Fields 2
channelId : [ChannelId](https://developers.buffer.com/reference.html#type/ChannelId)!
Channel targeted by the failing variant.
message : String!
Error message.
TYPE [CreateContentItemVariantNotFoundError](https://developers.buffer.com/reference.html#type/CreateContentItemVariantNotFoundError) ⚠️ Experimental
The channel targeted by a single post variant in the createContentItem input list was not found or is not accessible.
Fields 2
channelId : [ChannelId](https://developers.buffer.com/reference.html#type/ChannelId)!
Channel targeted by the failing variant.
message : String!
Error message.
TYPE [CreateSnippetSuccess](https://developers.buffer.com/reference.html#type/CreateSnippetSuccess) ⚠️ Experimental
Success response of the createSnippet mutation.
Fields 1
snippet : [Snippet](https://developers.buffer.com/reference.html#type/Snippet)!
The snippet that was created.
TYPE [DeleteContentItemFailure](https://developers.buffer.com/reference.html#type/DeleteContentItemFailure) ⚠️ Experimental
deleteContentItem failure. When any post cannot be deleted, nothing is deleted: the content item and all of its posts remain unchanged. Every blocked post is reported together so the caller can surface them all at once.
Fields 2
errors : [[PostNotDeletableError](https://developers.buffer.com/reference.html#type/PostNotDeletableError)!]!
The recoverable errors behind this failure.
message : String!
Summary error message.
TYPE [DeleteSnippetSuccess](https://developers.buffer.com/reference.html#type/DeleteSnippetSuccess) ⚠️ Experimental
Success response of the deleteSnippet mutation.
Fields 1
id : [SnippetId](https://developers.buffer.com/reference.html#type/SnippetId)!
The id of the deleted snippet.
TYPE [DocumentAsset](https://developers.buffer.com/reference.html#type/DocumentAsset)
Document asset
Fields 6
id : ID
The ID of the asset in the database
document : [DocumentMetadata](https://developers.buffer.com/reference.html#type/DocumentMetadata)!
Document specific metadata
mimeType : String!
The MIME type of the asset
source : String!
URL to the file source
thumbnail : String!
URL to the static thumbnail of the asset
type : [AssetType](https://developers.buffer.com/reference.html#type/AssetType)!
The type of the asset
TYPE [DocumentMetadata](https://developers.buffer.com/reference.html#type/DocumentMetadata)
Document metadata
Fields 4
filesize : Int
Document fileSize in bytes
numPages : Int!
Number of pages in the document
thumbnails : [String!]!
URLs to the static thumbnails of the document pages
title : String
Document title
TYPE [DurationRule](https://developers.buffer.com/reference.html#type/DurationRule) ⚠️ Experimental
Caps the duration of a time-based media property.
Fields 2
maxDurationSeconds : Int!
Maximum allowed duration in seconds.
property : [ContentProperty](https://developers.buffer.com/reference.html#type/ContentProperty)!
The content property this rule constrains.
TYPE [ExclusiveRule](https://developers.buffer.com/reference.html#type/ExclusiveRule) ⚠️ Experimental
`property` cannot be combined with any of `conflictsWith`.
Fields 2
conflictsWith : [[ContentProperty](https://developers.buffer.com/reference.html#type/ContentProperty)!]!
Properties that `property` cannot be combined with.
property : [ContentProperty](https://developers.buffer.com/reference.html#type/ContentProperty)!
The content property this rule constrains.
TYPE [FileSizeRule](https://developers.buffer.com/reference.html#type/FileSizeRule) ⚠️ Experimental
Caps the byte size of a media property.
Fields 2
maxMegabytes : Int!
Maximum allowed size in megabytes (MB).
property : [ContentProperty](https://developers.buffer.com/reference.html#type/ContentProperty)!
The content property this rule constrains.
TYPE [FormatRule](https://developers.buffer.com/reference.html#type/FormatRule) ⚠️ Experimental
Restricts a media property to specific formats (allow-list).
Fields 2
allowedFormats : [[MediaFormat](https://developers.buffer.com/reference.html#type/MediaFormat)!]!
The formats `property` is allowed to use.
property : [ContentProperty](https://developers.buffer.com/reference.html#type/ContentProperty)!
The content property this rule constrains.
TYPE [ImageAsset](https://developers.buffer.com/reference.html#type/ImageAsset)
Image asset
Fields 6
id : ID
The ID of the asset in the database
image : [ImageMetadata](https://developers.buffer.com/reference.html#type/ImageMetadata)!
Image specific metadata
mimeType : String!
The MIME type of the asset
source : String!
URL to the file source
thumbnail : String!
URL to the static thumbnail of the asset
type : [AssetType](https://developers.buffer.com/reference.html#type/AssetType)!
The type of the asset
TYPE [ImageMetadata](https://developers.buffer.com/reference.html#type/ImageMetadata)
Image metadata
Fields 6
altText : String!
Alternative text for accessibility
animatedThumbnail : String
Animated thumbnail URL
height : Int!
Image height in pixels
isAnimated : Boolean!
Is the image animated?
userTags : [[UserTag](https://developers.buffer.com/reference.html#type/UserTag)!]
User tags in the image
width : Int!
Image width in pixels
TYPE [LengthRule](https://developers.buffer.com/reference.html#type/LengthRule) ⚠️ Experimental
Caps the character length of a text-like property (e.g. 280 for X post text).
Fields 2
maxLength : Int!
Maximum allowed character length.
property : [ContentProperty](https://developers.buffer.com/reference.html#type/ContentProperty)!
The content property this rule constrains.
TYPE [RequiresRule](https://developers.buffer.com/reference.html#type/RequiresRule) ⚠️ Experimental
`property` requires all of `requires` to also be present.
Fields 2
property : [ContentProperty](https://developers.buffer.com/reference.html#type/ContentProperty)!
The content property this rule constrains.
requires : [[ContentProperty](https://developers.buffer.com/reference.html#type/ContentProperty)!]!
Properties that must also be present when `property` is used.
TYPE [ServiceConfiguration](https://developers.buffer.com/reference.html#type/ServiceConfiguration) ⚠️ Experimental
Service-level configuration for one supported `service` + `channelType`: its engagement capabilities and `content`. The channel-agnostic baseline — today the same fields as `ChannelConfiguration` minus `channelId` and the per-channel `authorizationStatus`. This overlap is incidental, not a contract: it is a distinct type so the service-level catalog can evolve independently of the per-channel config (either side may add fields the other doesn't share).
Fields 4
channelType : [ChannelType](https://developers.buffer.com/reference.html#type/ChannelType)!
The channel type within the service (e.g. profile, page, business).
content : [[ContentConfiguration](https://developers.buffer.com/reference.html#type/ContentConfiguration)!]!
Content config — one entry per content type, or a single entry grouping several types that share identical rules. Empty when none is exposed.
engagement : [[EngagementTypeConfiguration](https://developers.buffer.com/reference.html#type/EngagementTypeConfiguration)!]!
Engagement capabilities — one entry per engagement type. Empty when engagement isn't supported for this service + channel type.
service : [Service](https://developers.buffer.com/reference.html#type/Service)!
The social service this config describes (e.g. twitter, instagram).
TYPE [SnippetEdge](https://developers.buffer.com/reference.html#type/SnippetEdge) ⚠️ Experimental
An edge in a snippets connection.
Fields 2
cursor : String!
A cursor for pagination.
node : [Snippet](https://developers.buffer.com/reference.html#type/Snippet)!
The snippet at the end of the edge.
TYPE [VideoAsset](https://developers.buffer.com/reference.html#type/VideoAsset)
Video asset
Fields 6
id : ID
The ID of the asset in the database
mimeType : String!
The MIME type of the asset
source : String!
URL to the file source
thumbnail : String!
URL to the static thumbnail of the asset
type : [AssetType](https://developers.buffer.com/reference.html#type/AssetType)!
The type of the asset
video : [VideoMetadata](https://developers.buffer.com/reference.html#type/VideoMetadata)!
Video specific metadata
TYPE [VideoMetadata](https://developers.buffer.com/reference.html#type/VideoMetadata)
Video metadata
Fields 14
audioCodec : String
Audio codec
containerFormat : String
Video container format
durationMs : Int!
Video duration in seconds
fileSize : Int
Video fileSize in bytes
frameRate : Int
Video framerate
height : Int!
Video height in pixels
isTranscodingRequired : Boolean!
Whether the video needs to be transcoded before it can be broadcasted
isVideoProcessing : Boolean!
Whether the video is currently being processed (transcoding in progress)
rotationDegree : Int
Rotation degree
thumbnailOffset : Int
Offset of the thumbnail chosen for the video, in ms
title : String
Video title
videoBitRate : Int
Video bitrate in kbps
videoCodec : String
Video codec
width : Int!
Video width in pixels
TYPE [MutationError](https://developers.buffer.com/reference.html#type/MutationError)
Base Mutation Error type
Fields 1
message : String!
Error message
TYPE [MutationSuccess](https://developers.buffer.com/reference.html#type/MutationSuccess)
Base Mutation Success type Used when we have a success response with no data, we return this type with empty string
Fields 1
_empty : String!
The value is alwaus an empty string '' Note: GraphQL doesn't allow types with no fields, so we have to add this field
TYPE [ScrapedLink](https://developers.buffer.com/reference.html#type/ScrapedLink)
Link data for link preview
Fields 3
text : String!
Description for the scraped link
thumbnails : [String!]!
Thumbnails of media available in the link
url : String!
URL that the link asset has been built from
TYPE [CreateContentItemError](https://developers.buffer.com/reference.html#type/CreateContentItemError) ⚠️ Experimental
A recoverable error that prevented a content item from being created. Variant errors identify the specific channel they apply to; the others apply to the request as a whole.
### Inputs 12
INPUT [ConfigurationInput](https://developers.buffer.com/reference.html#type/ConfigurationInput) ⚠️ Experimental
Input for the configuration query.
Fields 1
organizationId : [OrganizationId](https://developers.buffer.com/reference.html#type/OrganizationId)!
The organization to return configuration for.
INPUT [ContentItemInput](https://developers.buffer.com/reference.html#type/ContentItemInput) ⚠️ Experimental
Input for fetching a single content item by id.
Fields 1
id : [ContentItemId](https://developers.buffer.com/reference.html#type/ContentItemId)!
The unique identifier of the content item to fetch.
INPUT [ContentItemsFilter](https://developers.buffer.com/reference.html#type/ContentItemsFilter) ⚠️ Experimental
Filters for listing content items. Omitted fields do not filter.
Fields 3
contentStatus : [ContentItemStatus](https://developers.buffer.com/reference.html#type/ContentItemStatus)
Only return content items with this content status. When omitted, content items in every status are returned.
tags : [TagComparator](https://developers.buffer.com/reference.html#type/TagComparator)
Only return content items carrying one of these tags, or, with `isEmpty`, content items with no tags at all. Matches the tags applied to the content item itself, not tags applied later to an individual post.
targetDate : [ContentItemsTargetDateFilter](https://developers.buffer.com/reference.html#type/ContentItemsTargetDateFilter)
Only return content items matching this target date filter.
INPUT [ContentItemsInput](https://developers.buffer.com/reference.html#type/ContentItemsInput) ⚠️ Experimental
Input for listing an organization's content items.
Fields 3
filter : [ContentItemsFilter](https://developers.buffer.com/reference.html#type/ContentItemsFilter)
Filters to apply. When omitted, all of the organization's content items are returned.
organizationId : [OrganizationId](https://developers.buffer.com/reference.html#type/OrganizationId)!
Organization to list content items for. The caller must be a member of this organization.
sort : [[ContentItemsSortInput](https://developers.buffer.com/reference.html#type/ContentItemsSortInput)!]
Sorting to apply, each entry breaking ties in the one before it. Defaults to newest first. A pagination cursor is only valid for the sort that produced it, so reset `after` to null whenever the sort changes.
INPUT [ContentItemsSortInput](https://developers.buffer.com/reference.html#type/ContentItemsSortInput) ⚠️ Experimental
One sorting criterion for the content items query. List several to break ties.
Fields 2
direction : [SortDirection](https://developers.buffer.com/reference.html#type/SortDirection)!
The direction to sort by.
field : [ContentItemSortableKey](https://developers.buffer.com/reference.html#type/ContentItemSortableKey)!
The field to sort by.
INPUT [ContentItemsTargetDateFilter](https://developers.buffer.com/reference.html#type/ContentItemsTargetDateFilter) ⚠️ Experimental
Filter for a content item's target date. Provide exactly one field (enforced by @oneOf).
Fields 2
presence : [DateTimePresence](https://developers.buffer.com/reference.html#type/DateTimePresence)
Only return content items by whether a target date is set: `present` returns only dated items, `absent` only undated ones.
range : [DateTimeComparator](https://developers.buffer.com/reference.html#type/DateTimeComparator)
Only return content items whose target date falls within this range. A range with no bounds returns every content item that has a target date.
INPUT [CreateContentItemDraftInput](https://developers.buffer.com/reference.html#type/CreateContentItemDraftInput) ⚠️ Experimental
Input for createContentItemDraft.
Fields 6
correlationId : [Uuid](https://developers.buffer.com/reference.html#type/Uuid)
Client-generated UUID that makes draft creation idempotent. A retry with the same UUID in the same organization returns the first content item in its current state.
draft : [DraftContentInput](https://developers.buffer.com/reference.html#type/DraftContentInput)!
The channel-less draft content to start with.
organizationId : [OrganizationId](https://developers.buffer.com/reference.html#type/OrganizationId)!
Organization that will own the content item.
tagIds : [[TagId](https://developers.buffer.com/reference.html#type/TagId)!]
Tags to apply to this content item. Omit to create it with no tags.
targetDate : [DateTime](https://developers.buffer.com/reference.html#type/DateTime)
Optional date indicating when this piece of content should go out. This is a planning aid only and does not schedule any posts.
title : String
Optional title describing what this piece of content is about.
INPUT [CreateContentItemInput](https://developers.buffer.com/reference.html#type/CreateContentItemInput) ⚠️ Experimental
Input for createContentItem.
Fields 5
organizationId : [OrganizationId](https://developers.buffer.com/reference.html#type/OrganizationId)!
Organization that owns the content item and all variants created in it.
posts : [[CreatePostInput](https://developers.buffer.com/reference.html#type/CreatePostInput)!]!
The channel-specific post variants to create, one per channel. Provide at least one variant, and at most one variant per channel.
tagIds : [[TagId](https://developers.buffer.com/reference.html#type/TagId)!]
Tags to apply to this content item. Omit to create it with no tags.
targetDate : [DateTime](https://developers.buffer.com/reference.html#type/DateTime)
Optional date indicating when this piece of content should go out. This is a planning aid only and does not schedule any posts.
title : String
Optional title describing what this piece of content is about.
INPUT [CreateSnippetInput](https://developers.buffer.com/reference.html#type/CreateSnippetInput) ⚠️ Experimental
Input for the createSnippet mutation.
Fields 3
name : String!
Display name of the snippet.
organizationId : [OrganizationId](https://developers.buffer.com/reference.html#type/OrganizationId)!
The organization that owns the snippet.
text : String!
The hashtags, as the text that is inserted into a post.
INPUT [DeleteContentItemInput](https://developers.buffer.com/reference.html#type/DeleteContentItemInput) ⚠️ Experimental
Input for deleteContentItem.
Fields 1
id : [ContentItemId](https://developers.buffer.com/reference.html#type/ContentItemId)!
The content item to delete.
INPUT [DeleteSnippetInput](https://developers.buffer.com/reference.html#type/DeleteSnippetInput) ⚠️ Experimental
Input for the deleteSnippet mutation.
Fields 2
id : [SnippetId](https://developers.buffer.com/reference.html#type/SnippetId)!
The snippet to delete.
organizationId : [OrganizationId](https://developers.buffer.com/reference.html#type/OrganizationId)!
The organization that owns the snippet.
INPUT [SnippetsInput](https://developers.buffer.com/reference.html#type/SnippetsInput) ⚠️ Experimental
Input for the snippets query.
Fields 1
organizationId : [OrganizationId](https://developers.buffer.com/reference.html#type/OrganizationId)!
The organization whose snippets to return.
### Enums 2
ENUM [ContentItemSortableKey](https://developers.buffer.com/reference.html#type/ContentItemSortableKey) ⚠️ Experimental
Field to sort content items by.
ENUM [ContentItemStatus](https://developers.buffer.com/reference.html#type/ContentItemStatus) ⚠️ Experimental
The status of a content item's body.
### Scalars 3
SCALAR [Email](https://developers.buffer.com/reference.html#type/Email)
The `Email` scalar represents a valid, normalized email address. Input is trimmed and lowercased before validation.
SCALAR [InvitationId](https://developers.buffer.com/reference.html#type/InvitationId)
The `InvitationId` scalar represents the ID of a pending team invitation
SCALAR [Uuid](https://developers.buffer.com/reference.html#type/Uuid)
The `Uuid` scalar represents an RFC 4122 v4 UUID, e.g. `550e8400-e29b-41d4-a716-446655440000`.
## Directives 1
@oneOf
Indicates exactly one field must be supplied and this field must not be `null`.
**Locations:** `INPUT_OBJECT`
TYPE
# Account
Account is a representation of a Buffer user.
## Fields 10
id : ID!
Unique identifier for the account
email : String!
Primary email address for the account
backupEmail : String
Backup email address for account recovery
avatar : String!
URL to the account's avatar image
createdAt : [DateTime](https://developers.buffer.com/reference.html#type/DateTime)
Date the account was created in the Core DB. For older customers, it's possible a Publish account existed in the Publish DB for this customer before this date
organizations (filter: [OrganizationFilterInput](https://developers.buffer.com/reference.html#type/OrganizationFilterInput)) : [[Organization](https://developers.buffer.com/reference.html#type/Organization)!]!
No description provided.
Arguments  
| Name  | Type  | Description  |  
| --- | --- | --- |  
| filter Optional  | [OrganizationFilterInput](https://developers.buffer.com/reference.html#type/OrganizationFilterInput)  |  No description  |  
timezone : String
The account-level timezone - this is used as a default input for streaks, posting plans, and new channel channel connections.
name : String
The account name, different from the organization name
preferences : [Preferences](https://developers.buffer.com/reference.html#type/Preferences)
The accounts preferences
connectedApps : [[ConnectedApp](https://developers.buffer.com/reference.html#type/ConnectedApp)!]
The connected apps for the account
TYPE ⚠️ Experimental
# AddPostToContentItemSuccess
Successful addPostToContentItem response.
## Fields 2
contentItem : [ContentItem](https://developers.buffer.com/reference.html#type/ContentItem)!
The content item after the mutation added the post.
post : [Post](https://developers.buffer.com/reference.html#type/Post)!
The post after the mutation added it. Its contentItemId names this content item.
TYPE
# AggregatedPostMetrics
Aggregated post metrics across a filtered post set. Each entry in `metrics` mirrors the shape of a `Post.metrics` entry; the total number of matched posts is carried as a regular `PostMetric` entry with `type: postCount`.
## Fields 2
metrics : [[PostMetric](https://developers.buffer.com/reference.html#type/PostMetric)!]!
Normalized metric aggregates across the matched posts. Always includes a baseline trio (`postCount`, `reactions`, `comments`) — posts on networks that don't track reactions or comments contribute 0 to those totals. Beyond the baseline, additional metric types are included only when every channel in the filter set supports them.
metricsUpdatedAt : [DateTime](https://developers.buffer.com/reference.html#type/DateTime)
The latest `metricsUpdatedAt` across the matched posts, indicating the freshness of the aggregate. Metrics are refreshed daily, so values can be up to ~24h behind the source network. Null when no posts matched the filter.
TYPE
# Annotation
Annotation representing all the entities in the text
## Fields 5
content : String!
The content of the annotation. Annotations can sometimes be different from the actual text content. E.g., Mastodon mentions have 'text: @buffer', but includes the server name in the content, 'content: @buffer@threads.net'
indices : [Int!]!
The indices of the annotation in the text
text : String!
The text representation of the annotation, eg '@buffer'
type : [AnnotationType](https://developers.buffer.com/reference.html#type/AnnotationType)!
The type of the annotation
url : String!
The URL the annotation points to. Empty string when the annotation has no link.
TYPE
# Author
Represent the author of a post or note.
## Fields 6
id : [AccountId](https://developers.buffer.com/reference.html#type/AccountId)!
The unique identifier of the author.
avatar : String!
The avatar URL of the author.
email : String!
The email address of the author.
isDeleted : Boolean!
Indicates whether the author is a deleted.
name : String
The name of the author. Null if the user has not yet set a name.
urn : String
The Buffer account URN for this author, in the form `urn:buffer:account:<account-id>`. Null when the author is deleted or the account ID is missing or invalid. A URN identifies an account. It does not prove that the account exists, that the caller has access, or that the account can be mentioned.
TYPE
# BlueskyMetadata
Bluesky metadata
## Fields 1
serverUrl : String!
The instance of bluesky of the channel
TYPE
# BlueskyPostMetadata
Bluesky post metadata
Implements: [CommonPostMetadata](https://developers.buffer.com/reference.html#type/CommonPostMetadata)[ThreadedPostMetadata](https://developers.buffer.com/reference.html#type/ThreadedPostMetadata)
## Fields 5
annotations : [[Annotation](https://developers.buffer.com/reference.html#type/Annotation)!]!
Annotations representing entities in the text
linkAttachment : [LinkAttachment](https://developers.buffer.com/reference.html#type/LinkAttachment)
Link attachment
thread : [[ThreadedPost](https://developers.buffer.com/reference.html#type/ThreadedPost)!]!
The list of threaded posts (not paginated)
threadCount : Int!
The number of threaded posts
type : [PostType](https://developers.buffer.com/reference.html#type/PostType)!
The channel-specific type of the post, eg, post, story, reel for Instagram
TYPE
# Channel
Channel entity
## Fields 27
id : [ChannelId](https://developers.buffer.com/reference.html#type/ChannelId)!
The ID of the channel
allowedActions : [[ChannelAction](https://developers.buffer.com/reference.html#type/ChannelAction)!]!
The allowed actions for the current user
avatar : String!
The avatar URL of the channel
descriptor : String!
Formatted name of the channel service and type: e.g. 'Twitter Profile' or 'Facebook Page'
displayName : String
The display name of the channel - nullable (reason?)
externalLink : String
The channel's URL on the social network (e.g. instagram.com/username or facebook.com/page) Returns null if the channel is not supported
hasActiveMemberDevice : Boolean!
Whether at least one member of the orginization who have access to this channel also has a user device registered for push notifications
isDisconnected : Boolean!
Indicates if the channel is properly connected to Buffer
isLocked : Boolean!
Indicates if the channel is locked - Locked channels can't be used for posting. A channel can be locked when the organization downgrades and reduces the channel quantity of their plan.
isNew : Boolean!
Indicates if the channel was recently created (in less than 10 seconds). This is used to determine the redirect modal after channel authorization
isQueuePaused : Boolean!
Indicates is the queue is paused for the channel. A paused queue means schedules posts won't be published.
linkShortening : [ChannelLinkShortening](https://developers.buffer.com/reference.html#type/ChannelLinkShortening)!
Link Shortening settings for the channel
metadata : [ChannelMetadata](https://developers.buffer.com/reference.html#type/ChannelMetadata)
Metadata or settings depending on the service type - such as the server URL for Mastodon or Location data for Facebook/GPB
name : String!
The name of the channel - the handle name, username, etc.
organizationId : [OrganizationId](https://developers.buffer.com/reference.html#type/OrganizationId)!
The organization ID of the channel
postingGoal : [PostingGoal](https://developers.buffer.com/reference.html#type/PostingGoal)
The posting goal for the channel
postingSchedule : [[ScheduleV2](https://developers.buffer.com/reference.html#type/ScheduleV2)!]!
Provides the posting slots for each day of the week
products : [[Product](https://developers.buffer.com/reference.html#type/Product)!]
Products that support a given channel
scopes : [String]!
Scopes requested for a given channel - empty array if we don't have them tracked
service : [Service](https://developers.buffer.com/reference.html#type/Service)!
Represents the social network
serviceId : String!
Represents the external ID of the channel on social network API
showTrendingTopicSuggestions : Boolean!
Indicates if trending topic suggestions should be shown in the composer. When false, users can still access trends via the trending icon button. Defaults to true for backward compatibility.
timezone : String!
The timezone of the channel - Default if not set is Europe/London
type : [ChannelType](https://developers.buffer.com/reference.html#type/ChannelType)!
The type of the channel - Page, Profile, Business, Group, Account, etc.
weeklyPostingLimit : [WeeklyPostingLimit](https://developers.buffer.com/reference.html#type/WeeklyPostingLimit)
Deprecated
Weekly posting limit for the channel
**Deprecation reason:** This field is not used anymore
createdAt : [DateTime](https://developers.buffer.com/reference.html#type/DateTime)!
The creation date of the channel
updatedAt : [DateTime](https://developers.buffer.com/reference.html#type/DateTime)!
The last time the channel was updated
TYPE ⚠️ Experimental
# ChannelConfiguration
Everything for one connected channel: its engagement capabilities, its full `content` config, and per-feature authorization. Each channel carries its own complete config — there is no service-level default to merge against.
## Fields 6
authorizationStatus : [[FeatureAuthorizationStatus](https://developers.buffer.com/reference.html#type/FeatureAuthorizationStatus)!]!
Authorization status per feature for this channel. A feature is a capability a channel can expose — e.g. posting, commenting, mentions, insights (see the `Feature` enum).
channelId : [ChannelId](https://developers.buffer.com/reference.html#type/ChannelId)!
The connected channel this config describes.
channelType : [ChannelType](https://developers.buffer.com/reference.html#type/ChannelType)!
The channel's type within the service (e.g. profile, page, business).
content : [[ContentConfiguration](https://developers.buffer.com/reference.html#type/ContentConfiguration)!]!
Content config — one entry per content type, or a single entry grouping several types that share identical rules (post / story / reel / comment reply).
engagement : [[EngagementTypeConfiguration](https://developers.buffer.com/reference.html#type/EngagementTypeConfiguration)!]!
Engagement capabilities — one entry per engagement type. Empty when engagement isn't supported on the channel.
service : [Service](https://developers.buffer.com/reference.html#type/Service)!
The channel's social service (e.g. twitter, instagram).
TYPE
# ChannelLinkShortening
Settings for link shortening
## Fields 2
config : [LinkShorteningConfig](https://developers.buffer.com/reference.html#type/LinkShorteningConfig)
Configuration of link shortening integration. Null if disabled.
isEnabled : Boolean!
If link shortening is enabled for the channel
TYPE ⚠️ Experimental
# ChannelRefreshRequired
Error returned when the channel needs a refresh
Implements: [MutationError](https://developers.buffer.com/reference.html#type/MutationError)
## Fields 2
channelIds : [[ChannelId](https://developers.buffer.com/reference.html#type/ChannelId)!]!
ChannelIds that need refreshing
message : String!
Error message
TYPE ⚠️ Experimental
# Configuration
Organization configuration. `channels` carries the per-connected-channel config the actor can view (including per-`Feature` `authorizationStatus`); `services` carries the service-level capability catalog — the engagement and content config for every supported `service` + `channelType`, independent of which channels are connected (e.g. for composing before a channel is connected); `collaborationRoleAbilities` carries the Roles ability catalog.
`@public` is set per field rather than on the type, so a field is external only when tagged. A new field is internal until it carries its own `@public`.
## Fields 2
channels : [[ChannelConfiguration](https://developers.buffer.com/reference.html#type/ChannelConfiguration)!]!
Per-connected-channel config for every channel the actor can view.
services : [[ServiceConfiguration](https://developers.buffer.com/reference.html#type/ServiceConfiguration)!]!
Service-level capability catalog for every supported service + channel type.
TYPE
# ConnectedApp
Connected App
## Fields 8
category : [ConnectedAppCategory](https://developers.buffer.com/reference.html#type/ConnectedAppCategory)
The category of the connected app, when known.
clientId : ID!
The id of the connectedApp.
description : String!
A brief description of the connected app.
name : String!
The name of the connected app.
scopes : [String!]!
The access scopes granted to this connection for Buffer's public API resources. Empty when the connection holds none.
userId : ID!
The id of the user that has granted access to the app.
website : String!
The website URL of the connected app.
createdAt : [DateTime](https://developers.buffer.com/reference.html#type/DateTime)!
The date and time when the connected app was created.
TYPE ⚠️ Experimental
# ContentConfiguration
Config for one or more content types that share the same properties and rules. Grouping several `configurationContentTypes` in one entry avoids duplicating an identical config (e.g. story + reel).
## Fields 3
configurationContentTypes : [[ConfigurationContentType](https://developers.buffer.com/reference.html#type/ConfigurationContentType)!]!
The content type(s) this config applies to (grouped when rules are identical).
rules : [[ValidationRule](https://developers.buffer.com/reference.html#type/ValidationRule)!]!
Validation rules that decide whether a draft is valid.
supportedProperties : [[ContentProperty](https://developers.buffer.com/reference.html#type/ContentProperty)!]!
The properties these content types support; absence means unsupported.
TYPE ⚠️ Experimental
# ContentItem
A piece of content in Buffer. It starts as a channel-less draft and can later become a set of channel-specific posts, or it can be created with its posts directly.
This API is an early preview and can change without a deprecation period.
## Fields 10
id : [ContentItemId](https://developers.buffer.com/reference.html#type/ContentItemId)!
Unique identifier for this content item.
accountId : [AccountId](https://developers.buffer.com/reference.html#type/AccountId)!
Account that owns this content item.
allowedActions : [[ContentItemAction](https://developers.buffer.com/reference.html#type/ContentItemAction)!]!
Actions the calling actor can take on this content item. A client reads this set instead of deriving the authorization rules itself.
author : [Author](https://developers.buffer.com/reference.html#type/Author)
The person who created this content item. Null when that person's account no longer exists.
body : [ContentItemBody](https://developers.buffer.com/reference.html#type/ContentItemBody)!
The current content of this item: either a channel-less draft or the channel-specific posts created from it.
organizationId : [OrganizationId](https://developers.buffer.com/reference.html#type/OrganizationId)!
Organization that owns this content item.
tags : [[Tag](https://developers.buffer.com/reference.html#type/Tag)!]!
Tags applied to this content item, in the order they were set. A tag applies to the item as a whole, so it survives the move from a channel-less draft to channel-specific posts.
targetDate : [DateTime](https://developers.buffer.com/reference.html#type/DateTime)
Optional date indicating when this piece of content should go out. This is a planning aid only and does not schedule any posts.
title : String
Optional title describing what this piece of content is about.
createdAt : [DateTime](https://developers.buffer.com/reference.html#type/DateTime)!
When this content item was created.
TYPE ⚠️ Experimental
# ContentItemEdge
An edge in a content item connection.
## Fields 2
cursor : String!
A cursor for pagination.
node : [ContentItem](https://developers.buffer.com/reference.html#type/ContentItem)!
The content item node at the end of the edge.
TYPE ⚠️ Experimental
# ContentItemsConnection
A paginated connection of content items.
## Fields 3
edges : [[ContentItemEdge](https://developers.buffer.com/reference.html#type/ContentItemEdge)!]!
The list of content item edges.
pageInfo : [PaginationPageInfo](https://developers.buffer.com/reference.html#type/PaginationPageInfo)!
Pagination information for the connection.
totalCount : Int!
The total number of content items matching the request.
TYPE ⚠️ Experimental
# ContentItemStateError
updateContentItemDraft and promoteContentItemDraftToPosts need a channel-less draft. They report this error when the item already holds channel-specific posts. Another request can put the item in that state while this one runs.
Implements: [MutationError](https://developers.buffer.com/reference.html#type/MutationError)
## Fields 1
message : String!
Error message.
TYPE ⚠️ Experimental
# CountRule
Bounds how many of a property are allowed. `min` null/absent = no lower bound (optional); `min: 1` = required. `max` null = unlimited. At least one of `min` or `max` is always present — a rule that bounds neither is never emitted.
Implements: [ValidationRule](https://developers.buffer.com/reference.html#type/ValidationRule)
## Fields 3
max : Int
Maximum allowed count. Null = unlimited.
min : Int
Minimum allowed count. Null = no lower bound (optional).
property : [ContentProperty](https://developers.buffer.com/reference.html#type/ContentProperty)!
The content property this rule constrains.
TYPE ⚠️ Experimental
# CreateContentItemDraftFailure
createContentItemDraft failure. When any part of the input is invalid, nothing is created.
Implements: [MutationError](https://developers.buffer.com/reference.html#type/MutationError)
## Fields 2
errors : [[InvalidInputError](https://developers.buffer.com/reference.html#type/InvalidInputError)!]!
The recoverable errors behind this failure.
message : String!
Summary error message.
TYPE ⚠️ Experimental
# CreateContentItemDraftSuccess
Successful createContentItemDraft response.
## Fields 1
contentItem : [ContentItem](https://developers.buffer.com/reference.html#type/ContentItem)!
The content item first created for this request, including its current state.
TYPE ⚠️ Experimental
# CreateContentItemFailure
createContentItem failure. Every recoverable error is reported together so the caller can surface them all at once. When the input fails validation, no content item and no variants are created. When one or more variants fail while being processed after creation, the content item and all of its variants already exist; the per-channel errors identify the variants that need attention.
Implements: [MutationError](https://developers.buffer.com/reference.html#type/MutationError)
## Fields 2
errors : [[CreateContentItemError](https://developers.buffer.com/reference.html#type/CreateContentItemError)!]!
The recoverable errors behind this failure.
message : String!
Summary error message.
TYPE ⚠️ Experimental
# CreateContentItemSuccess
Successful createContentItem response.
## Fields 1
content : [ContentItem](https://developers.buffer.com/reference.html#type/ContentItem)!
The content item created by this mutation.
TYPE ⚠️ Experimental
# CreateContentItemVariantInvalidInputError
Invalid input for a single post variant in the createContentItem input list.
Implements: [MutationError](https://developers.buffer.com/reference.html#type/MutationError)
## Fields 2
channelId : [ChannelId](https://developers.buffer.com/reference.html#type/ChannelId)!
Channel targeted by the failing variant.
message : String!
Error message.
TYPE ⚠️ Experimental
# CreateContentItemVariantLimitReachedError
Limit reached for a single post variant in the createContentItem input list.
Implements: [MutationError](https://developers.buffer.com/reference.html#type/MutationError)
## Fields 2
channelId : [ChannelId](https://developers.buffer.com/reference.html#type/ChannelId)!
Channel targeted by the failing variant.
message : String!
Error message.
TYPE ⚠️ Experimental
# CreateContentItemVariantNotFoundError
The channel targeted by a single post variant in the createContentItem input list was not found or is not accessible.
Implements: [MutationError](https://developers.buffer.com/reference.html#type/MutationError)
## Fields 2
channelId : [ChannelId](https://developers.buffer.com/reference.html#type/ChannelId)!
Channel targeted by the failing variant.
message : String!
Error message.
TYPE 🧪 Preview
# CreatePostTemplateSuccess
Successful result of an end user creating a post template.
## Fields 1
postTemplate : [PostTemplate](https://developers.buffer.com/reference.html#type/PostTemplate)!
The newly created post template.
TYPE ⚠️ Experimental
# CreateSnippetSuccess
Success response of the createSnippet mutation.
## Fields 1
snippet : [Snippet](https://developers.buffer.com/reference.html#type/Snippet)!
The snippet that was created.
TYPE
# DailyPostingLimitStatus
Posting limit status at an intended posting time. For X, counts describe the busiest rolling 24-hour window affected by adding a post at that time, including later scheduled posts. Other networks use the channel's local calendar day. Counts include existing posts only, excluding the proposed post.
## Fields 5
channelId : [ChannelId](https://developers.buffer.com/reference.html#type/ChannelId)!
The channel ID this status refers to.
isAtLimit : Boolean!
Whether adding a post at the requested time would exceed the posting limit.
limit : Int
The network daily posting limit. Null means unlimited.
scheduled : Int!
Number of existing scheduled posts in the evaluated window.
sent : Int!
Number of existing sent posts in the evaluated window.
TYPE ⚠️ Experimental
# DeleteContentItemFailure
deleteContentItem failure. When any post cannot be deleted, nothing is deleted: the content item and all of its posts remain unchanged. Every blocked post is reported together so the caller can surface them all at once.
Implements: [MutationError](https://developers.buffer.com/reference.html#type/MutationError)
## Fields 2
errors : [[PostNotDeletableError](https://developers.buffer.com/reference.html#type/PostNotDeletableError)!]!
The recoverable errors behind this failure.
message : String!
Summary error message.
TYPE
# DeletePostSuccess
deletePost success response returns the post id that was deleted.
## Fields 1
id : [PostId](https://developers.buffer.com/reference.html#type/PostId)!
Post id that was delete.
TYPE ⚠️ Experimental
# DeleteSnippetSuccess
Success response of the deleteSnippet mutation.
## Fields 1
id : [SnippetId](https://developers.buffer.com/reference.html#type/SnippetId)!
The id of the deleted snippet.
TYPE ⚠️ Experimental
# DeleteTagActionSuccess
Returned when a tag was deleted successfully.
## Fields 1
id : [TagId](https://developers.buffer.com/reference.html#type/TagId)!
The id of the tag that was deleted.
TYPE
# DocumentAsset
Document asset
Implements: [Asset](https://developers.buffer.com/reference.html#type/Asset)
## Fields 6
id : ID
The ID of the asset in the database
document : [DocumentMetadata](https://developers.buffer.com/reference.html#type/DocumentMetadata)!
Document specific metadata
mimeType : String!
The MIME type of the asset
source : String!
URL to the file source
thumbnail : String!
URL to the static thumbnail of the asset
type : [AssetType](https://developers.buffer.com/reference.html#type/AssetType)!
The type of the asset
TYPE
# DocumentMetadata
Document metadata
## Fields 4
filesize : Int
Document fileSize in bytes
numPages : Int!
Number of pages in the document
thumbnails : [String!]!
URLs to the static thumbnails of the document pages
title : String
Document title
TYPE ⚠️ Experimental
# DraftContent
A content draft that is not attached to any channel yet. Because no channel is selected, no network-specific rules apply, including media type restrictions.
## Fields 4
id : [DraftContentId](https://developers.buffer.com/reference.html#type/DraftContentId)!
Unique identifier for this draft.
aiAssisted : Boolean!
True when the draft content was written with the help of AI.
assets : [[Asset](https://developers.buffer.com/reference.html#type/Asset)!]!
Images, videos, or documents attached to the draft, in display order.
text : String!
The written content of the draft. Empty when the draft holds only assets.
TYPE
# DuplicateError
Error returned when a unique constraint is violated
Implements: [MutationError](https://developers.buffer.com/reference.html#type/MutationError)
## Fields 1
message : String!
Error message
TYPE ⚠️ Experimental
# DurationRule
Caps the duration of a time-based media property.
Implements: [ValidationRule](https://developers.buffer.com/reference.html#type/ValidationRule)
## Fields 2
maxDurationSeconds : Int!
Maximum allowed duration in seconds.
property : [ContentProperty](https://developers.buffer.com/reference.html#type/ContentProperty)!
The content property this rule constrains.
TYPE
# EmptySuccess
Empty mutation success response used when client doesn't need any data back or simply needs to respond to a success or error.
Implements: [MutationSuccess](https://developers.buffer.com/reference.html#type/MutationSuccess)
## Fields 1
_empty : String!
The value is always an empty string '' Note: GraphQL doesn't allow types with no fields, so we have to add this field
TYPE ⚠️ Experimental
# EngagementSupportedReaction
A supported reaction. `reactionType` is the opaque identity echoed back on the react mutation; `visual` carries everything needed to render it.
## Fields 2
reactionType : [ReactionType](https://developers.buffer.com/reference.html#type/ReactionType)!
The kind of reaction a user can apply (e.g. like, love, celebrate). This is the identifier the client sends back to the react mutation when the user picks this reaction; treat it as an opaque value rather than parsing it.
visual : [ReactionVisual](https://developers.buffer.com/reference.html#type/ReactionVisual)!
How to render this reaction (built-in icon or network image).
TYPE ⚠️ Experimental
# EngagementTypeConfiguration
Per-engagement-type configuration. One entry per kind; `engagementType` discriminates. Adding a kind is additive — a new `EngagementType` value, not a new type.
## Fields 7
engagementType : [EngagementType](https://developers.buffer.com/reference.html#type/EngagementType)!
The kind of engagement this entry configures (comment / mention / directMessage).
media : [MediaConfiguration](https://developers.buffer.com/reference.html#type/MediaConfiguration)!
Media configuration. Always present; `supportsMedia: false` = the platform doesn't deliver attached media to Buffer, so none can be shown.
metadata : [EngagementMetadata](https://developers.buffer.com/reference.html#type/EngagementMetadata)
Optional network-specific engagement metadata (e.g. Google Business). null when none applies.
reactions : [ReactionsConfiguration](https://developers.buffer.com/reference.html#type/ReactionsConfiguration)!
Reactions. Always present; empty `supportedReactions` with `supportsAnyEmoji: false` = reacting via Buffer isn't supported.
replying : [ReplyingConfiguration](https://developers.buffer.com/reference.html#type/ReplyingConfiguration)!
Reply configuration. Always present; `supportsReplying: false` = replying via Buffer not supported.
supportedAiFeatures : [[AiFeature](https://developers.buffer.com/reference.html#type/AiFeature)!]!
AI features supported for this engagement type. Empty when none.
syncData : [SyncDataConfiguration](https://developers.buffer.com/reference.html#type/SyncDataConfiguration)!
Sync configuration — realTime/polling mechanism plus optional forced-sync detail.
TYPE ⚠️ Experimental
# ExclusiveRule
`property` cannot be combined with any of `conflictsWith`.
Implements: [ValidationRule](https://developers.buffer.com/reference.html#type/ValidationRule)
## Fields 2
conflictsWith : [[ContentProperty](https://developers.buffer.com/reference.html#type/ContentProperty)!]!
Properties that `property` cannot be combined with.
property : [ContentProperty](https://developers.buffer.com/reference.html#type/ContentProperty)!
The content property this rule constrains.
TYPE
# FacebookMetadata
Facebook metadata
## Fields 1
locationData : [LocationData](https://developers.buffer.com/reference.html#type/LocationData)
Metadata about the location of the business associated with the channel. Only available for Facebook and GPB
TYPE
# FacebookPostMetadata
Facebook post metadata
Implements: [CommonPostMetadata](https://developers.buffer.com/reference.html#type/CommonPostMetadata)
## Fields 5
annotations : [[Annotation](https://developers.buffer.com/reference.html#type/Annotation)!]!
Annotations representing entities in the text
firstComment : String
Facebook post's first comment
linkAttachment : [LinkAttachment](https://developers.buffer.com/reference.html#type/LinkAttachment)
Link attachment
title : String
Title of Facebook reel
type : [PostType](https://developers.buffer.com/reference.html#type/PostType)!
The channel-specific type of the post, eg, post, story, reel for Instagram
TYPE ⚠️ Experimental
# FeatureAuthorizationStatus
Pairs a feature with the channel's authorization status for it (token/scope level). One entry per authorization-gated feature the channel exposes.
## Fields 3
feature : [Feature](https://developers.buffer.com/reference.html#type/Feature)!
The feature this status describes — a capability a channel can expose, e.g. posting, commenting, mentions, insights, reacting to engagements (see the `Feature` enum).
reason : String
Why the feature is in its current `status`, when a specific cause is known (e.g. the connected platform user lacks rights on the account that owns webhook subscriptions). Informative text for display/support — not a stable machine key, so clients must not parse or switch on it. Null when the status needs no explanation (`ok`) or no specific cause was identified.
status : [AuthorizationStatus](https://developers.buffer.com/reference.html#type/AuthorizationStatus)!
Whether the channel is currently authorized to use `feature`: `ok` (usable), `needsRefresh` (token refresh required), `notEnoughData` (missing scopes / webhook metadata), `needsUpgrade` (client below the minimum version — applies only to the mobile apps), or `notEnoughRights` (the connected platform user's role is insufficient — reconnecting cannot fix it). See the `AuthorizationStatus` enum.
TYPE ⚠️ Experimental
# FileSizeRule
Caps the byte size of a media property.
Implements: [ValidationRule](https://developers.buffer.com/reference.html#type/ValidationRule)
## Fields 2
maxMegabytes : Int!
Maximum allowed size in megabytes (MB).
property : [ContentProperty](https://developers.buffer.com/reference.html#type/ContentProperty)!
The content property this rule constrains.
TYPE ⚠️ Experimental
# ForcedSyncConfiguration
Forced-sync detail. Present only when the kind's sync mechanism supports a forced (manual) sync.
## Fields 2
forcedSyncRateLimit : [ForcedSyncRateLimit](https://developers.buffer.com/reference.html#type/ForcedSyncRateLimit)
Rate limit for forced syncs. `null` when forced sync is unthrottled. Reuses the `ForcedSyncRateLimit` type defined by the comment schema.
pollInterval : Int!
How often, in seconds, the channel is automatically polled for new items.
TYPE ⚠️ Experimental
# ForcedSyncRateLimit
Rate limit configuration for forced sync operations.
## Fields 2
allowedAttempts : Int!
Number of allowed forced backfill attempts within the period.
period : Int!
Rate limit period in seconds for forced backfill operations.
TYPE ⚠️ Experimental
# FormatRule
Restricts a media property to specific formats (allow-list).
Implements: [ValidationRule](https://developers.buffer.com/reference.html#type/ValidationRule)
## Fields 2
allowedFormats : [[MediaFormat](https://developers.buffer.com/reference.html#type/MediaFormat)!]!
The formats `property` is allowed to use.
property : [ContentProperty](https://developers.buffer.com/reference.html#type/ContentProperty)!
The content property this rule constrains.
TYPE ⚠️ Experimental
# GoogleBusinessEngagementMetadata
Google Business-specific engagement metadata. Distinct from the channel-level `GoogleBusinessMetadata` (which carries location data) — this is the engagement surface's rating/note metadata.
## Fields 2
hasUserRating : Boolean!
Whether engagements on this channel carry a user star rating.
permanentNote : String!
A permanent note surfaced to the user about this channel's engagements. Empty when there is nothing to tell the user.
TYPE
# GoogleBusinessEventMetaData
Metadata for a GBP post that is an event
## Fields 8
button : [GoogleBusinessPostActionType](https://developers.buffer.com/reference.html#type/GoogleBusinessPostActionType)!
Action button
endDate : [DateTime](https://developers.buffer.com/reference.html#type/DateTime)!
End date of the event
endTime : String
Deprecated
End time of the event
**Deprecation reason:** get time from the endDate
isFullDayEvent : Boolean!
Indicate whether the event has a start or end time.
link : String
Link to the action
startDate : [DateTime](https://developers.buffer.com/reference.html#type/DateTime)!
Start date of the event
startTime : String
Deprecated
Start time of the event
**Deprecation reason:** get time from the startDate
title : String!
Title of the event
TYPE
# GoogleBusinessMetadata
Google Business metadata
## Fields 1
locationData : [LocationData](https://developers.buffer.com/reference.html#type/LocationData)
Metadata about the location of the business associated with the channel. Only available for Facebook and GPB
TYPE
# GoogleBusinessOfferMetaData
Metadata for a GBP post that is an offer
## Fields 6
code : String
Coupon code for the offer
endDate : [DateTime](https://developers.buffer.com/reference.html#type/DateTime)!
End date of the offer
link : String
Link to the offer
startDate : [DateTime](https://developers.buffer.com/reference.html#type/DateTime)!
Start date of the offer
terms : String
Terms and Conditions
title : String!
Title of the offer
TYPE
# GoogleBusinessPostMetadata
Google Business Profile post metadata @deprecated: pending proposal for specific GBP post types: update, offer and event metadata types
Implements: [CommonPostMetadata](https://developers.buffer.com/reference.html#type/CommonPostMetadata)
## Fields 4
annotations : [[Annotation](https://developers.buffer.com/reference.html#type/Annotation)!]!
Annotations representing entities in the text
details : [GoogleBusinessPostDetails](https://developers.buffer.com/reference.html#type/GoogleBusinessPostDetails)
Details of the metadata
title : String
Title if available in the given GBP post type: event and offer
type : [PostType](https://developers.buffer.com/reference.html#type/PostType)!
The channel-specific type of the post, eg, post, story, reel for Instagram
TYPE
# GoogleBusinessWhatsNewMetaData
Metadata for a GBP post of type Whats new
## Fields 2
button : [GoogleBusinessPostActionType](https://developers.buffer.com/reference.html#type/GoogleBusinessPostActionType)!
Action button
link : String
Link to the action
TYPE ⚠️ Experimental
# IconVisual
Render from the built-in client icon set.
## Fields 1
icon : [ReactionIcon](https://developers.buffer.com/reference.html#type/ReactionIcon)!
The built-in icon to render.
TYPE
# Idea
Ideas are the main entity in the create space
## Fields 7
id : ID!
Unique identifier for the idea
content : [IdeaContent](https://developers.buffer.com/reference.html#type/IdeaContent)!
The actual content and metadata of the idea
groupId : ID
ID of the group this idea belongs to (if any)
organizationId : ID!
ID of the organization that owns this idea
position : Float
Numerical position for ordering within a group
createdAt : Int!
Unix timestamp of when the idea was created
updatedAt : Int!
Unix timestamp of when the idea was last modified
TYPE
# IdeaContent
Content of an idea
## Fields 7
aiAssisted : Boolean!
Indicates whether AI tools were used in creating this idea
date : [DateTime](https://developers.buffer.com/reference.html#type/DateTime)
DateTime set by user associated with the idea - this often reflects a target publish date.
media : [[IdeaMedia](https://developers.buffer.com/reference.html#type/IdeaMedia)!]
List of media items attached to the idea
services : [[Service](https://developers.buffer.com/reference.html#type/Service)!]!
Services tagged by the user - this is typically used to annotate ideas with their target services
tags : [[PublishingTag](https://developers.buffer.com/reference.html#type/PublishingTag)!]!
Tags used to categorize and organize the idea
text : String
Main body text or description of the idea
title : String
Title or headline of the idea
TYPE
# IdeaEdge
Pagination type for Ideas
## Fields 2
cursor : String!
Opaque cursor for pagination, used to fetch subsequent pages
node : [Idea](https://developers.buffer.com/reference.html#type/Idea)!
The idea object
TYPE
# IdeaGroup
Idea groups are used to organize ideas in the board
## Fields 3
id : ID!
Unique identifier for the idea group.
isLocked : Boolean!
Whether the idea group is locked.
name : String!
The name of the idea group.
TYPE
# IdeaMedia
Media attached to an idea
## Fields 7
id : ID!
Unique identifier for the media in Buffer's upload system
alt : String
Alternative text description for accessibility
size : Int
File size in bytes
source : [IdeaMediaSource](https://developers.buffer.com/reference.html#type/IdeaMediaSource)
Source platform information for the media
thumbnailUrl : String
URL to a smaller version of the media for preview purposes
type : [MediaType](https://developers.buffer.com/reference.html#type/MediaType)!
Type of media (e.g., image, video, gif)
url : String!
Direct URL to access the media file
TYPE
# IdeaMediaSource
Media source for the idea, e.g. Unsplash, Gifphy, etc.
## Fields 4
id : String
Unique identifier from the source platform
author : String
Name of the content creator/author
authorUrl : String
URL to the author's profile on the source platform
name : String!
Name of the media source platform (e.g., 'Unsplash', 'Giphy')
TYPE
# IdeaResponse
createIdea response type
## Fields 2
idea : [Idea](https://developers.buffer.com/reference.html#type/Idea)
The affected idea
refreshIdeas : Boolean!
If true, the client should refresh the ideas list because other ideas might have been moved
TYPE
# IdeasConnection
Relay connection for paginated ideas.
## Fields 2
edges : [[IdeaEdge](https://developers.buffer.com/reference.html#type/IdeaEdge)!]!
List of idea edges containing the ideas and their cursors
pageInfo : [PaginationPageInfo](https://developers.buffer.com/reference.html#type/PaginationPageInfo)!
Pagination metadata including hasNextPage and endCursor
TYPE
# ImageAsset
Image asset
Implements: [Asset](https://developers.buffer.com/reference.html#type/Asset)
## Fields 6
id : ID
The ID of the asset in the database
image : [ImageMetadata](https://developers.buffer.com/reference.html#type/ImageMetadata)!
Image specific metadata
mimeType : String!
The MIME type of the asset
source : String!
URL to the file source
thumbnail : String!
URL to the static thumbnail of the asset
type : [AssetType](https://developers.buffer.com/reference.html#type/AssetType)!
The type of the asset
TYPE
# ImageMetadata
Image metadata
## Fields 6
altText : String!
Alternative text for accessibility
animatedThumbnail : String
Animated thumbnail URL
height : Int!
Image height in pixels
isAnimated : Boolean!
Is the image animated?
userTags : [[UserTag](https://developers.buffer.com/reference.html#type/UserTag)!]
User tags in the image
width : Int!
Image width in pixels
TYPE ⚠️ Experimental
# ImageVisual
Render a network-supplied image (e.g. LinkedIn-branded reactions).
## Fields 1
url : String!
URL of the network-supplied reaction image.
TYPE ⚠️ Experimental
# InstagramAudio
An Instagram music track or original sound that can be attached to a Reel.
## Fields 8
id : String!
Meta audio asset ID
coverArtworkUrl : [URL](https://developers.buffer.com/reference.html#type/URL)
Temporary artwork URL from Meta. May be null.
creatorUsername : String
Creator username for original sounds
displayArtist : String
Artist name for licensed music
duration : Int!
Duration of the audio in milliseconds
previewUrl : [URL](https://developers.buffer.com/reference.html#type/URL)
Temporary preview URL from Meta. May be null.
title : String!
Display title for the audio
type : [InstagramAudioType](https://developers.buffer.com/reference.html#type/InstagramAudioType)!
Whether this asset is licensed music or an original sound
TYPE ⚠️ Experimental
# InstagramAudioCatalogSuccess
Combined music and original sound results, with duplicate audio IDs removed.
## Fields 2
audio : [[InstagramAudio](https://developers.buffer.com/reference.html#type/InstagramAudio)!]!
Available tracks, with duplicate audio IDs removed. Meta's order within each catalog is preserved.
Browsing returns music first, then original sounds. Search returns original sounds first, then music, to better reflect the search text: creators write original sound titles, so they usually contain the words people search for, while music results often don't match the query.
failedAudioTypes : [[InstagramAudioType](https://developers.buffer.com/reference.html#type/InstagramAudioType)!]!
Catalogs that failed to load. Results from successful catalogs are still returned, including an empty list if that catalog has no available tracks. If both catalogs fail, the query returns an error instead.
TYPE ⚠️ Experimental
# InstagramAudioSuccess
Refreshed metadata for one Instagram audio asset.
## Fields 1
audio : [InstagramAudio](https://developers.buffer.com/reference.html#type/InstagramAudio)!
Refreshed audio metadata.
TYPE
# InstagramGeolocation
Instagram Geolocation
## Fields 2
id : String
The id of this location
text : String
The name of this location
TYPE
# InstagramMetadata
Instagram metadata
## Fields 1
defaultToReminders : Boolean!
Indicates if we should default to reminder for Instagram
TYPE
# InstagramPostMetadata
Instagram post metadata
Implements: [CommonPostMetadata](https://developers.buffer.com/reference.html#type/CommonPostMetadata)
## Fields 8
annotations : [[Annotation](https://developers.buffer.com/reference.html#type/Annotation)!]!
Annotations representing entities in the text
firstComment : String
Instagram post's first comment
geolocation : [InstagramGeolocation](https://developers.buffer.com/reference.html#type/InstagramGeolocation)
Geolocation of the post
isAiGenerated : Boolean!
Whether the post discloses AI-generated content
link : String
Shop Grid link for the post
shouldShareToFeed : Boolean!
Indicates whether post should be shared to feed
stickerFields : [InstagramStickerFields](https://developers.buffer.com/reference.html#type/InstagramStickerFields)
Sticker fields for reminder-based publishing
type : [PostType](https://developers.buffer.com/reference.html#type/PostType)!
The channel-specific type of the post, eg, post, story, reel for Instagram
TYPE
# InstagramStickerFields
Instagram fields for reminder-based publishing. Upon the reminder for publishing, the user is prompted to copy and paste these fields into the Instagram app to complete the post.
## Fields 5
music : String
Placeholder text for the post's music
other : String
Additional field for any other post content
products : String
Placeholder text for the post's linked products
text : String
Text for the Story or Reel
topics : String
Placeholder text for the post's topics (Reels only)
TYPE
# InvalidInputError
Error returned when the input is invalid
Implements: [MutationError](https://developers.buffer.com/reference.html#type/MutationError)
## Fields 1
message : String!
Error message
TYPE ⚠️ Experimental
# LengthRule
Caps the character length of a text-like property (e.g. 280 for X post text).
Implements: [ValidationRule](https://developers.buffer.com/reference.html#type/ValidationRule)
## Fields 2
maxLength : Int!
Maximum allowed character length.
property : [ContentProperty](https://developers.buffer.com/reference.html#type/ContentProperty)!
The content property this rule constrains.
TYPE
# LimitReachedError
Error returned when the limit is reached
Implements: [MutationError](https://developers.buffer.com/reference.html#type/MutationError)
## Fields 1
message : String!
Error message
TYPE
# LinkAttachment
Link attachment
Implements: [ScrapedLink](https://developers.buffer.com/reference.html#type/ScrapedLink)
## Fields 6
expandedUrl : String
Full URL that the link asset has been built from
text : String!
Description for the scraped link
thumbnail : String
Selected thumbnail for this link preview
thumbnails : [String!]!
Thumbnails of media available in the link
title : String!
Title for the link attachment
url : String!
URL that the link asset has been built from
TYPE
# LinkedInMetadata
LinkedIn metadata
## Fields 1
shouldShowLinkedinAnalyticsRefreshBanner : Boolean!
Property parsed from scopes indicating whether the client should show the LinkedIn analytics refresh banner
TYPE
# LinkedInPostMetadata
LinkedIn post metadata
Implements: [CommonPostMetadata](https://developers.buffer.com/reference.html#type/CommonPostMetadata)
## Fields 4
annotations : [[Annotation](https://developers.buffer.com/reference.html#type/Annotation)!]!
Annotations representing entities in the text
firstComment : String
LinkedIn post's first comment
linkAttachment : [LinkAttachment](https://developers.buffer.com/reference.html#type/LinkAttachment)
Link attachment
type : [PostType](https://developers.buffer.com/reference.html#type/PostType)!
The channel-specific type of the post, eg, post, story, reel for Instagram
TYPE
# LinkShorteningConfig
Link Shortening Configuration
## Fields 2
domain : String!
Domain of the link shortener - eg buff.ly, dub.co, or the user's custom domain.
name : String!
Human readable string to describe the link shortening service.
TYPE
# LocationData
Location data about the channel
## Fields 3
googleAccountId : String
Google Account Id of the business
location : String
Location of the business associated with the channel
mapsLink : String
Link to the map
TYPE
# MastodonMetadata
Mastodon metadata
## Fields 2
maxCharacters : Int!
Maximum character limit allowed for this channel's server instance
serverUrl : String!
The instance of mastodon of the channel
TYPE
# MastodonPostMetadata
Mastodon post metadata
Implements: [CommonPostMetadata](https://developers.buffer.com/reference.html#type/CommonPostMetadata)[ThreadedPostMetadata](https://developers.buffer.com/reference.html#type/ThreadedPostMetadata)
## Fields 5
annotations : [[Annotation](https://developers.buffer.com/reference.html#type/Annotation)!]!
Annotations representing entities in the text
spoilerText : String
Spoiler text hiding the root text of this post
thread : [[ThreadedPost](https://developers.buffer.com/reference.html#type/ThreadedPost)!]!
The list of threaded posts (not paginated)
threadCount : Int!
The number of threaded posts
type : [PostType](https://developers.buffer.com/reference.html#type/PostType)!
The channel-specific type of the post, eg, post, story, reel for Instagram
TYPE ⚠️ Experimental
# MediaConfiguration
Media configuration for an engagement type — whether media attached to an engagement reaches Buffer and can therefore be shown to the user.
## Fields 3
additionalInformation : String
User-facing explanation of what the client can do about the missing media, worded for the platform (e.g. "Instagram doesn't send media with mentions to Buffer. Open the mention natively to see the full content."). Display text only — not a stable machine key, so clients must not parse or switch on it. Null when `supportsMedia` is true.
disclaimer : String
User-facing explanation of why media isn't shown. Display text only — not a stable machine key, so clients must not parse or switch on it. Null when `supportsMedia` is true.
supportsMedia : Boolean!
Whether media attached to this engagement type is delivered by the platform and can be shown.
TYPE
# MemberConnection
Represents the members connection edge. Later, we can add the list of members with the page info to follow our connection edge pattern.
## Fields 1
totalCount : Int!
The total count of team members counting the org owner and team members from the Publish DB.
TYPE
# Note
Note entity
## Fields 7
id : [NoteId](https://developers.buffer.com/reference.html#type/NoteId)!
The unique identifier of the note.
allowedActions : [[NoteAction](https://developers.buffer.com/reference.html#type/NoteAction)!]!
The allowed actions a user can perform on the note.
author : [Author](https://developers.buffer.com/reference.html#type/Author)!
The author of the note - null if the user is deleted or left the organization.
text : String!
The content of the note.
type : [NoteType](https://developers.buffer.com/reference.html#type/NoteType)!
The type of the note.
createdAt : [DateTime](https://developers.buffer.com/reference.html#type/DateTime)!
The date and time when the note was created.
updatedAt : [DateTime](https://developers.buffer.com/reference.html#type/DateTime)
The date and time when the note was last edited.
TYPE
# NotFoundError
Error returned when the resource is not found
Implements: [MutationError](https://developers.buffer.com/reference.html#type/MutationError)
## Fields 1
message : String!
Error message
TYPE
# Organization
Organization is a representation of a Buffer Organization.
## Fields 7
id : [OrganizationId](https://developers.buffer.com/reference.html#type/OrganizationId)!
The ID of the organization.
channelCount : Int!
The total number of channels connected to the organization.
limits : [OrganizationLimits](https://developers.buffer.com/reference.html#type/OrganizationLimits)!
The limits of the organization. Can be used to check if the organization has reached the limit of channels, members, etc.
members : [MemberConnection](https://developers.buffer.com/reference.html#type/MemberConnection)!
The members of the organization. Can be used to check the total number of members in the organization. In the future, it might contain more information about the members.
name : String!
The name of the organization.
ownerEmail : String!
The owner email of the organization.
shouldEnforce2FASetup : Boolean!
Whether the requesting actor should be sent through 2FA setup before they can use this organization. Derived: true only when the org has `settings.enforce2FA` ON and the actor has no 2FA configured on their own account.
This is the single source of truth for the forced-2FA gate; app-shell and publish-frontend redirect to the setup flow when it's true. Exposed to the API gateway so any stitched consumer reads the same value.
TYPE
# OrganizationLimits
Resource limits for an organization including channels, members, and content limits
## Fields 11
channels : Int!
The maximum number of channels allowed for the organization.
generateContent : Int!
The maximum number of content generations allowed for the organization.
ideaGroups : Int!
The maximum number of idea groups allowed for the organization.
ideas : Int!
The maximum number of ideas allowed for the organization.
members : Int!
The maximum number of members allowed for the organization.
postTemplates : Int!
The maximum number of post templates allowed for the organization.
savedReplies : Int!
The maximum number of saved replies allowed for the organization.
scheduledPosts : Int!
The maximum number of scheduled posts allowed for the organization.
scheduledStoriesPerChannel : Int!
The maximum number of scheduled stories allowed per channel.
scheduledThreadsPerChannel : Int!
The maximum number of scheduled threads allowed per channel.
tags : Int!
The maximum number of tags allowed for the organization.
TYPE
# PaginationPageInfo
Information to aid in pagination.
## Fields 4
endCursor : String
The last cursor in the list. It can be used to fetch the next page.
hasNextPage : Boolean!
When set to true, it means there is a next page available.
hasPreviousPage : Boolean!
When set to true, it means there is a previous page available. Will always return false for now as we only support forward pagination.
startCursor : String
The first cursor in the list. It can be used to fetch the previous page.
TYPE
# PinterestBoard
A Pinterest board
## Fields 6
id : String!
The ID of the board
avatar : String
The board avatar
description : String
The board description
name : String!
The board name
serviceId : String!
The ID of the service
url : String!
The board URL
TYPE
# PinterestMetadata
Pinterest metadata
## Fields 1
boards : [[PinterestBoard](https://developers.buffer.com/reference.html#type/PinterestBoard)!]!
The list of boards the user has on Pinterest
TYPE
# PinterestPostMetadata
Pinterest post metadata
Implements: [CommonPostMetadata](https://developers.buffer.com/reference.html#type/CommonPostMetadata)
## Fields 5
annotations : [[Annotation](https://developers.buffer.com/reference.html#type/Annotation)!]!
Annotations representing entities in the text
board : [PinterestBoard](https://developers.buffer.com/reference.html#type/PinterestBoard)
The board the Pin is saved to
title : String
The title of the Pin
type : [PostType](https://developers.buffer.com/reference.html#type/PostType)!
The channel-specific type of the post, eg, post, story, reel for Instagram
url : String
The Pin destination link
TYPE
# Post
Post entity
## Fields 28
id : [PostId](https://developers.buffer.com/reference.html#type/PostId)!
The ID of the post
allowedActions : [[PostAction](https://developers.buffer.com/reference.html#type/PostAction)!]!
Indicates what actions the current account can perform on the post
assets : [[Asset](https://developers.buffer.com/reference.html#type/Asset)!]!
assets
author : [Author](https://developers.buffer.com/reference.html#type/Author)
Represents the user who created the post
channel : [Channel](https://developers.buffer.com/reference.html#type/Channel)!
channel
channelId : [ChannelId](https://developers.buffer.com/reference.html#type/ChannelId)!
channel ID (faster than resolving the channnel.id)
channelService : [Service](https://developers.buffer.com/reference.html#type/Service)!
channel service (faster than resolving the channnel.service)
contentItemId : [ContentItemId](https://developers.buffer.com/reference.html#type/ContentItemId) ⚠️ Experimental
The content item this post belongs to. Null when the post belongs to no content item.
dueAt : [DateTime](https://developers.buffer.com/reference.html#type/DateTime)
Date when the post is scheduled to be published
error : [PostPublishingError](https://developers.buffer.com/reference.html#type/PostPublishingError)
error
externalLink : String
The external URL of the post at the destination service
ideaId : [IdeaId](https://developers.buffer.com/reference.html#type/IdeaId)
Is set when the Post is generated from an Idea
isCustomScheduled : Boolean!
Indicates whether time to publish was manually selected by the user
metadata : [PostMetadata](https://developers.buffer.com/reference.html#type/PostMetadata)
Metadata of the post which differs based on the social network/service @see post.metadata.graphql
metrics : [[PostMetric](https://developers.buffer.com/reference.html#type/PostMetric)!]
Metrics for the sent post. If post is not yet sent, this field will be null
metricsUpdatedAt : [DateTime](https://developers.buffer.com/reference.html#type/DateTime)
Timestamp of when `metrics` were last refreshed from the network. Null until the daily ingestion job has processed the post. Buffer pulls fresh metrics once per day, so this can lag the network value by ~24h.
notes : [[Note](https://developers.buffer.com/reference.html#type/Note)!]!
notes
notificationStatus : [NotificationStatus](https://developers.buffer.com/reference.html#type/NotificationStatus)
notificationStatus: notified or markedAsPublished
schedulingType : [SchedulingType](https://developers.buffer.com/reference.html#type/SchedulingType)
How the post publishes: `notification` for a reminder that asks someone to publish it by hand, `automatic` for one the publishing workers send.
sentAt : [DateTime](https://developers.buffer.com/reference.html#type/DateTime)
Date when the post is published
sharedNow : Boolean!
Indicates whether the post was shared via publish now action
shareMode : [ShareMode](https://developers.buffer.com/reference.html#type/ShareMode)!
Indicates the share mode of the post (e.g., addToQueue, shareNext, shareNow, customScheduled)
status : [PostStatus](https://developers.buffer.com/reference.html#type/PostStatus)!
status
tags : [[Tag](https://developers.buffer.com/reference.html#type/Tag)!]!
tags - sorted by name in ascending order
text : String!
Text content of the Post
via : [PostVia](https://developers.buffer.com/reference.html#type/PostVia)!
Indicates if the post is created from Buffer or the API
createdAt : [DateTime](https://developers.buffer.com/reference.html#type/DateTime)!
Date when the post was created
updatedAt : [DateTime](https://developers.buffer.com/reference.html#type/DateTime)!
Date when the post was updated
TYPE
# PostActionSuccess
Success response returns the full up-to-date post from after the action was performed.
## Fields 1
post : [Post](https://developers.buffer.com/reference.html#type/Post)!
Post on which the action was successfully performed.
TYPE ⚠️ Experimental
# PostChannelNotFoundError
The channel targeted by a single post in the promoteContentItemDraftToPosts input list was not found or is not accessible.
Implements: [MutationError](https://developers.buffer.com/reference.html#type/MutationError)
## Fields 2
channelId : [ChannelId](https://developers.buffer.com/reference.html#type/ChannelId)!
Channel targeted by the failing post.
message : String!
Error message.
TYPE ⚠️ Experimental
# PostContent
The fixed set of channel-specific posts created from a content item. Each post targets a single channel and follows that channel's network rules.
## Fields 1
posts : [[Post](https://developers.buffer.com/reference.html#type/Post)!]!
The posts created for this content item, one per channel. Individual posts are edited through their own mutations.
TYPE
# PostingGoal
Represents a posting goal for a channel, including target, progress, and status information.
## Fields 6
goal : Int!
The target number of posts for this goal.
periodEnd : [DateTime](https://developers.buffer.com/reference.html#type/DateTime)!
The end date of the period for this posting goal.
periodStart : [DateTime](https://developers.buffer.com/reference.html#type/DateTime)!
The start date of the period for this posting goal.
scheduledCount : Int!
The number of posts that are scheduled to be sent for this goal.
sentCount : Int!
The number of posts that have been sent (published or ingested) for this goal.
status : [PostingGoalStatus](https://developers.buffer.com/reference.html#type/PostingGoalStatus)!
The current status of the posting goal.
TYPE ⚠️ Experimental
# PostInvalidInputError
Invalid input for a single post in the promoteContentItemDraftToPosts input list.
Implements: [MutationError](https://developers.buffer.com/reference.html#type/MutationError)
## Fields 2
channelId : [ChannelId](https://developers.buffer.com/reference.html#type/ChannelId)!
Channel targeted by the failing post.
message : String!
Error message.
TYPE ⚠️ Experimental
# PostLimitReachedError
Limit reached for a single post in the promoteContentItemDraftToPosts input list.
Implements: [MutationError](https://developers.buffer.com/reference.html#type/MutationError)
## Fields 2
channelId : [ChannelId](https://developers.buffer.com/reference.html#type/ChannelId)!
Channel targeted by the failing post.
message : String!
Error message.
TYPE
# PostMetric
A single metric for a post (or an entry in an aggregated metrics response).
## Fields 5
description : String!
A human-readable description of what the metric represents.
name : String!
The human-readable name of the metric (e.g. "Reactions", "Eng. Rate").
type : [PostMetricType](https://developers.buffer.com/reference.html#type/PostMetricType)!
The type of metric. Cross-network metrics use unified naming (`reactions`, `comments`, etc.); network-specific metrics retain their network's vocabulary (`saves`, `quotes`, etc.). See `PostMetricType` for the full catalog including deprecated values.
unit : [PostMetricUnit](https://developers.buffer.com/reference.html#type/PostMetricUnit)!
The unit (count vs percentage) of `value`.
value : Float!
The metric value. Defaults to 0 when the network did not report the metric.
TYPE ⚠️ Experimental
# PostNotDeletableError
A post in this content item cannot be deleted, so the item cannot be deleted either. Either the post is publishing or has already published, and posts in those states can no longer be deleted, or this account is not allowed to delete posts on that channel.
Implements: [MutationError](https://developers.buffer.com/reference.html#type/MutationError)
## Fields 2
channelId : [ChannelId](https://developers.buffer.com/reference.html#type/ChannelId)!
Channel targeted by the post that cannot be deleted.
message : String!
Error message.
TYPE
# PostPublishingError
Post publishing error
## Fields 3
message : String!
Error message to display
rawError : String
The original error from the publishing service (internal use only)
supportUrl : String
Link to a help center article to help resolve the error
TYPE
# PostsEdge
Represent a node in the pagination result using the Connect Relay convention.
## Fields 2
cursor : String!
Opaque cursor to be used in pagination to fetch from current node.
node : [Post](https://developers.buffer.com/reference.html#type/Post)!
Represents the current post in the list.
TYPE
# PostsResults
Results for the posts query.
## Fields 2
edges : [[PostsEdge](https://developers.buffer.com/reference.html#type/PostsEdge)!]
The list of posts that match the query.
pageInfo : [PaginationPageInfo](https://developers.buffer.com/reference.html#type/PaginationPageInfo)!
Information to aid in pagination.
TYPE
# PostTemplate
A post template used for content inspiration.
## Fields 9
id : [PostTemplateId](https://developers.buffer.com/reference.html#type/PostTemplateId)! 🧪 Preview
The unique identifier for the template.
body : String! 🧪 Preview
The main content body of the template, may contain {{placeholders}}.
description : String! 🧪 Preview
A short user-facing description of the template.
emoji : String! 🧪 Preview
The emoji associated with the template.
organizationId : [OrganizationId](https://developers.buffer.com/reference.html#type/OrganizationId)! 🧪 Preview
The organization that owns this template.
title : String! 🧪 Preview
The title of the template.
visibility : [PostTemplateVisibility](https://developers.buffer.com/reference.html#type/PostTemplateVisibility)! 🧪 Preview
The visibility level of the template. `public` is returned for Buffer-managed templates.
createdAt : [DateTime](https://developers.buffer.com/reference.html#type/DateTime)! 🧪 Preview
The date and time the template was created.
updatedAt : [DateTime](https://developers.buffer.com/reference.html#type/DateTime)! 🧪 Preview
The date and time the template was last updated.
TYPE 🧪 Preview
# PostTemplateEdge
An edge in a post template connection.
## Fields 2
cursor : String!
A cursor for pagination.
node : [PostTemplate](https://developers.buffer.com/reference.html#type/PostTemplate)!
The post template node at the end of the edge.
TYPE 🧪 Preview
# PostTemplatesConnection
A paginated connection of post templates.
## Fields 3
edges : [[PostTemplateEdge](https://developers.buffer.com/reference.html#type/PostTemplateEdge)!]!
The list of post template edges.
pageInfo : [PaginationPageInfo](https://developers.buffer.com/reference.html#type/PaginationPageInfo)!
Pagination information for the connection.
totalCount : Int!
The total number of templates matching the filters.
TYPE
# Preferences
Account preferences
## Fields 3
timeFormat : String
No description provided.
startOfWeek : String
No description provided.
defaultScheduleOption : [ScheduleOption](https://developers.buffer.com/reference.html#type/ScheduleOption)!
No description provided.
TYPE ⚠️ Experimental
# PromoteContentItemDraftToPostsFailure
promoteContentItemDraftToPosts failure. Every recoverable error is reported together so the caller can surface them all at once — for example, every post that failed validation across every targeted channel. A failure does not always mean nothing changed: post-processing errors are reported after the promotion has taken effect.
Implements: [MutationError](https://developers.buffer.com/reference.html#type/MutationError)
## Fields 2
errors : [[PromoteContentItemDraftToPostsError](https://developers.buffer.com/reference.html#type/PromoteContentItemDraftToPostsError)!]!
The recoverable errors behind this failure.
message : String!
Summary error message.
TYPE ⚠️ Experimental
# PromoteContentItemDraftToPostsSuccess
Successful promoteContentItemDraftToPosts response.
## Fields 1
contentItem : [ContentItem](https://developers.buffer.com/reference.html#type/ContentItem)!
The promoted content item.
TYPE
# PublishingTag
Tag snapshot associated with content
## Fields 4
id : ID!
No description provided.
color : String!
Hex color for tag e.g #F523F1
colorName : [TagColorName](https://developers.buffer.com/reference.html#type/TagColorName)
Stable Buffer palette identifier derived from `color`. Clients should map this value to platform- and theme-specific presentation, falling back to `color` when this field is null or unsupported. Returns null for custom or unrecognized colors.
name : String!
No description provided.
TYPE ⚠️ Experimental
# ReactionsConfiguration
Reactions configuration. `restingIcon` is always populated; `supportedReactions` empty = reacting via Buffer isn't supported (unless `supportsAnyEmoji`), one = single-button liking, multiple = a reaction set.
## Fields 4
requiresAuthorization : Boolean!
Whether reacting needs an OAuth scope beyond the ones a base connection grants. When true, check the channel's `engagementReaction` entry in `authorizationStatus` before offering the reaction — the channel may need a reconnect to grant it. On the service-level catalog this is channel-agnostic and may overstate the requirement, since it can vary with a channel's login flow; the per-channel configuration resolves it exactly.
restingIcon : [ReactionIcon](https://developers.buffer.com/reference.html#type/ReactionIcon)!
The resting-state icon — the pre-reaction icon.
supportedReactions : [[EngagementSupportedReaction](https://developers.buffer.com/reference.html#type/EngagementSupportedReaction)!]!
The reactions the user can apply. Empty when reacting via Buffer isn't supported, or when `supportsAnyEmoji` is true.
supportsAnyEmoji : Boolean!
Whether the user can react with any single emoji (e.g. direct messages). When true, offer an emoji picker and send the chosen emoji to the network's emoji reaction mutation; `supportedReactions` is empty.
TYPE ⚠️ Experimental
# RemovePostFromContentItemSuccess
Successful removePostFromContentItem response.
## Fields 2
contentItem : [ContentItem](https://developers.buffer.com/reference.html#type/ContentItem)!
The content item after the post left it.
post : [Post](https://developers.buffer.com/reference.html#type/Post)!
The post after the mutation removed it. It belongs to no content item.
TYPE ⚠️ Experimental
# ReplyingConfiguration
Reply configuration for an engagement type. A rich object (not a bare boolean) so reply metadata can be added later.
## Fields 3
prefixReplyWithMention : Boolean!
Whether replies should be prefixed with the author's @mention.
supportsReplying : Boolean!
Whether replying to this engagement type via Buffer is supported.
supportsReplyTo : Boolean!
Whether a reply can quote a specific message.
TYPE ⚠️ Experimental
# RequiresRule
`property` requires all of `requires` to also be present.
Implements: [ValidationRule](https://developers.buffer.com/reference.html#type/ValidationRule)
## Fields 2
property : [ContentProperty](https://developers.buffer.com/reference.html#type/ContentProperty)!
The content property this rule constrains.
requires : [[ContentProperty](https://developers.buffer.com/reference.html#type/ContentProperty)!]!
Properties that must also be present when `property` is used.
TYPE
# RestProxyError
An error passed through from Buffer's legacy REST API.
**On the way out.** This type exists only because some mutations still forward to that API. It is never returned by the tag mutations, and will be removed from their payloads. The post mutations can still return it, so keep handling it there for now.
Do not select it in new operations. Select `... on MutationError { message }` instead, which every error type implements and which keeps working when this one goes away.
Implements: [MutationError](https://developers.buffer.com/reference.html#type/MutationError)
## Fields 3
code : Int
Deprecated
Error code from the REST API response - <https://buffer.com/developers/api/errors>
**Deprecation reason:** Being retired along with Buffer's legacy REST API. Select `... on MutationError { message }` to handle errors generically, or the specific recoverable error members of the payload.
link : String
Deprecated
Link to our Help center from the REST API response
**Deprecation reason:** Being retired along with Buffer's legacy REST API. Select `... on MutationError { message }` to handle errors generically, or the specific recoverable error members of the payload.
message : String!
An error message from the REST API response that we proxied here
TYPE
# RetweetMetadata
Information about the initial Tweet that was retweeted
Implements: [ScrapedLink](https://developers.buffer.com/reference.html#type/ScrapedLink)
## Fields 6
id : String!
Retweet ID
text : String!
Text of the original tweet
thumbnails : [String!]!
Thumbnails to media available in the link
url : String!
Link to original tweet
user : [RetweetUserMetadata](https://developers.buffer.com/reference.html#type/RetweetUserMetadata)!
User who created the original tweet
createdAt : [DateTime](https://developers.buffer.com/reference.html#type/DateTime)!
Date when the original tweet was created
TYPE
# RetweetUserMetadata
Information about the initial author of the Tweet that was retweeted
## Fields 3
avatar : String!
Avatar of the user who created the original Tweet
name : String!
Name of the user who created the original Tweet
username : String!
Username of the user who created the original Tweet
TYPE
# ScheduleV2
Posting schedule for a specific day of the week
## Fields 3
day : [DayOfWeek](https://developers.buffer.com/reference.html#type/DayOfWeek)!
The day of the week: mon, tue, wed, thu, fri, sat, sun
paused : Boolean!
Indicates if this day is paused in the posting schedule.
times : [String!]!
The times the channel is scheduled to post on the day: HH:MM
TYPE ⚠️ Experimental
# SearchInstagramAudioSuccess
Success response for searching Instagram audio
## Fields 1
audio : [[InstagramAudio](https://developers.buffer.com/reference.html#type/InstagramAudio)!]!
Matching or trending audio assets
TYPE ⚠️ Experimental
# ServiceConfiguration
Service-level configuration for one supported `service` + `channelType`: its engagement capabilities and `content`. The channel-agnostic baseline — today the same fields as `ChannelConfiguration` minus `channelId` and the per-channel `authorizationStatus`. This overlap is incidental, not a contract: it is a distinct type so the service-level catalog can evolve independently of the per-channel config (either side may add fields the other doesn't share).
## Fields 4
channelType : [ChannelType](https://developers.buffer.com/reference.html#type/ChannelType)!
The channel type within the service (e.g. profile, page, business).
content : [[ContentConfiguration](https://developers.buffer.com/reference.html#type/ContentConfiguration)!]!
Content config — one entry per content type, or a single entry grouping several types that share identical rules. Empty when none is exposed.
engagement : [[EngagementTypeConfiguration](https://developers.buffer.com/reference.html#type/EngagementTypeConfiguration)!]!
Engagement capabilities — one entry per engagement type. Empty when engagement isn't supported for this service + channel type.
service : [Service](https://developers.buffer.com/reference.html#type/Service)!
The social service this config describes (e.g. twitter, instagram).
TYPE ⚠️ Experimental
# Snippet
A named set of hashtags that a team member saves once and inserts into posts.
## Fields 3
id : [SnippetId](https://developers.buffer.com/reference.html#type/SnippetId)!
Unique identifier of the snippet.
name : String!
Display name of the snippet.
text : String!
The hashtags, as the text that is inserted into a post.
TYPE ⚠️ Experimental
# SnippetEdge
An edge in a snippets connection.
## Fields 2
cursor : String!
A cursor for pagination.
node : [Snippet](https://developers.buffer.com/reference.html#type/Snippet)!
The snippet at the end of the edge.
TYPE ⚠️ Experimental
# SnippetsConnection
A paginated connection of snippets, sorted by name.
## Fields 2
edges : [[SnippetEdge](https://developers.buffer.com/reference.html#type/SnippetEdge)!]!
The list of snippet edges.
pageInfo : [PaginationPageInfo](https://developers.buffer.com/reference.html#type/PaginationPageInfo)!
Pagination information for the connection.
TYPE
# SubstackPostMetadata
Substack post metadata
Implements: [CommonPostMetadata](https://developers.buffer.com/reference.html#type/CommonPostMetadata)
## Fields 3
annotations : [[Annotation](https://developers.buffer.com/reference.html#type/Annotation)!]!
Annotations representing entities in the text
linkAttachment : [LinkAttachment](https://developers.buffer.com/reference.html#type/LinkAttachment)
Link attachment
type : [PostType](https://developers.buffer.com/reference.html#type/PostType)!
The channel-specific type of the post, eg, post, story, reel for Instagram
TYPE ⚠️ Experimental
# SyncDataConfiguration
Sync configuration for an engagement type — the realTime/polling `syncDataMechanism` plus optional forced-sync detail.
## Fields 2
forcedSyncConfiguration : [ForcedSyncConfiguration](https://developers.buffer.com/reference.html#type/ForcedSyncConfiguration)
Forced-sync detail. A forced sync is a user-triggered (manual) refresh that fetches new items on demand instead of waiting for the next scheduled poll or push. `null` when this kind's sync mechanism has no forced-sync support.
syncDataMechanism : [SyncDataMechanism](https://developers.buffer.com/reference.html#type/SyncDataMechanism)!
How this engagement type syncs on this channel: `realTime` (push) or `polling` (pull).
TYPE
# Tag
A label an organization applies to posts and ideas so they can be grouped and filtered together. Tags belong to the organization and are shared by everyone in it, rather than being per channel or per person.
## Fields 5
id : [TagId](https://developers.buffer.com/reference.html#type/TagId)!
The tag's unique identifier.
color : String!
The tag's color as a hex triplet, for example `#F523F1`. Use `colorName` where you need a stable identifier rather than a literal color.
colorName : [TagColorName](https://developers.buffer.com/reference.html#type/TagColorName)
Stable Buffer palette identifier derived from `color`. Clients should map this value to platform- and theme-specific presentation, falling back to `color` when this field is null or unsupported. Returns null for custom or unrecognized colors.
isLocked : Boolean!
Whether the tag is locked.
A tag locks when the organization holds more tags than its plan allows, typically after a downgrade. Buffer locks the excess rather than deleting it, so nothing is lost if the organization upgrades again.
A locked tag **cannot be edited** — `updateTag` rejects it. It can still be read, deleted, and applied to posts through the API. Buffer's own apps also hide locked tags when picking a tag for a post; that is a client convention, not something the API enforces.
Locking is recalculated when the organization's plan changes, and deleting an unlocked tag frees a slot for the oldest locked one.
name : String!
The tag's display name, for example `Summer sales`.
TYPE ⚠️ Experimental
# TagActionSuccess
Returned when a tag was created or updated successfully.
## Fields 1
tag : [Tag](https://developers.buffer.com/reference.html#type/Tag)!
The tag as persisted, read back after the write.
TYPE ⚠️ Experimental
# TagEdge
An edge in a tag connection.
## Fields 2
cursor : String!
A cursor for pagination.
node : [Tag](https://developers.buffer.com/reference.html#type/Tag)!
The tag at the end of the edge.
TYPE ⚠️ Experimental
# TagsConnection
A page of an organization's tags.
## Fields 3
edges : [[TagEdge](https://developers.buffer.com/reference.html#type/TagEdge)!]!
The list of tag edges.
pageInfo : [PaginationPageInfo](https://developers.buffer.com/reference.html#type/PaginationPageInfo)!
Pagination information for the connection.
totalCount : Int!
The total number of tags matching the request, across every page.
TYPE
# ThreadedPost
A post authored by the user which is posted to a thread. This is commonly used for long-format twitter and meta threads posts to allow authored content to span multiple threads. Threads are represented as a list of replies, each replying to the previous one.
## Fields 4
assets : [[Asset](https://developers.buffer.com/reference.html#type/Asset)!]!
Media assets of the threaded post
linkAttachment : [LinkAttachment](https://developers.buffer.com/reference.html#type/LinkAttachment)
Deprecated
Use metadata.{service}.linkAttachment on the thread item instead. This field will be removed on December 15, 2026.
**Deprecation reason:** Use metadata.{service}.linkAttachment on the thread item instead. This field will be removed on December 15, 2026.
metadata : [ThreadItemMetadata](https://developers.buffer.com/reference.html#type/ThreadItemMetadata)
Service-specific fields for this threaded post
text : String!
The text body content of the threaded post
TYPE
# ThreadItemBlueskyMetadata
Bluesky fields on a single item of a thread
## Fields 1
linkAttachment : [LinkAttachment](https://developers.buffer.com/reference.html#type/LinkAttachment)
Link attachment
TYPE
# ThreadItemMetadata
Service-specific fields on a single item of a thread. The populated key matches the post's service.
## Fields 2
bluesky : [ThreadItemBlueskyMetadata](https://developers.buffer.com/reference.html#type/ThreadItemBlueskyMetadata)
Bluesky fields for this thread item
threads : [ThreadItemThreadsMetadata](https://developers.buffer.com/reference.html#type/ThreadItemThreadsMetadata)
Threads fields for this thread item
TYPE
# ThreadItemThreadsMetadata
Threads fields on a single item of a thread
## Fields 1
linkAttachment : [LinkAttachment](https://developers.buffer.com/reference.html#type/LinkAttachment)
Link attachment
TYPE
# ThreadsPostMetadata
Threads post metadata
Implements: [CommonPostMetadata](https://developers.buffer.com/reference.html#type/CommonPostMetadata)[ThreadedPostMetadata](https://developers.buffer.com/reference.html#type/ThreadedPostMetadata)
## Fields 8
annotations : [[Annotation](https://developers.buffer.com/reference.html#type/Annotation)!]!
Annotations representing entities in the text
linkAttachment : [LinkAttachment](https://developers.buffer.com/reference.html#type/LinkAttachment)
Link attachment
locationId : String
LocationId associated with the post
locationName : String
Location name associated with the post
thread : [[ThreadedPost](https://developers.buffer.com/reference.html#type/ThreadedPost)!]!
The list of threaded posts (not paginated)
threadCount : Int!
The number of threaded posts
topic : String
Topic associated with the post
type : [PostType](https://developers.buffer.com/reference.html#type/PostType)!
The channel-specific type of the post, eg, post, story, reel for Instagram
TYPE
# TiktokMetadata
Tiktok metadata
## Fields 1
defaultToReminders : Boolean!
Indicates if we should default to reminder for Tiktok
TYPE
# TiktokPostMetadata
Tiktok post metadata
Implements: [CommonPostMetadata](https://developers.buffer.com/reference.html#type/CommonPostMetadata)
## Fields 4
annotations : [[Annotation](https://developers.buffer.com/reference.html#type/Annotation)!]!
Annotations representing entities in the text
isAiGenerated : Boolean!
Whether the post discloses AI-generated content (TikTok video only)
title : String
The title of the TikTok post (for photo posts)
type : [PostType](https://developers.buffer.com/reference.html#type/PostType)!
The channel-specific type of the post, eg, post, story, reel for Instagram
TYPE
# TwitterMetadata
Twitter metadata
## Fields 1
subscriptionType : String
Indicates the type of subscription the user has on Twitter
TYPE
# TwitterPostMetadata
Twitter post metadata
Implements: [CommonPostMetadata](https://developers.buffer.com/reference.html#type/CommonPostMetadata)[ThreadedPostMetadata](https://developers.buffer.com/reference.html#type/ThreadedPostMetadata)
## Fields 6
annotations : [[Annotation](https://developers.buffer.com/reference.html#type/Annotation)!]!
Annotations representing entities in the text
isAiGenerated : Boolean!
Whether the post discloses AI-generated content
retweet : [RetweetMetadata](https://developers.buffer.com/reference.html#type/RetweetMetadata)
The details of the tweet being retweeted
thread : [[ThreadedPost](https://developers.buffer.com/reference.html#type/ThreadedPost)!]!
The list of threaded posts (not paginated)
threadCount : Int!
The number of threaded posts
type : [PostType](https://developers.buffer.com/reference.html#type/PostType)!
The channel-specific type of the post, eg, post, story, reel for Instagram
TYPE
# UnauthorizedError
Error returned when the user is not authorized to perform the action
Implements: [MutationError](https://developers.buffer.com/reference.html#type/MutationError)
## Fields 1
message : String!
Error message
TYPE
# UnexpectedError
Error returned when unexpected error occurs
Implements: [MutationError](https://developers.buffer.com/reference.html#type/MutationError)
## Fields 1
message : String!
Error message
TYPE ⚠️ Experimental
# UpdateContentItemDraftFailure
updateContentItemDraft failure.
Implements: [MutationError](https://developers.buffer.com/reference.html#type/MutationError)
## Fields 2
errors : [[UpdateContentItemDraftError](https://developers.buffer.com/reference.html#type/UpdateContentItemDraftError)!]!
The recoverable errors behind this failure.
message : String!
Summary error message.
TYPE ⚠️ Experimental
# UpdateContentItemDraftSuccess
Successful updateContentItemDraft response.
## Fields 1
contentItem : [ContentItem](https://developers.buffer.com/reference.html#type/ContentItem)!
The updated content item.
TYPE ⚠️ Experimental
# UpdateContentItemFailure
updateContentItem failure. When any part of the input is invalid, nothing is changed.
Implements: [MutationError](https://developers.buffer.com/reference.html#type/MutationError)
## Fields 2
errors : [[InvalidInputError](https://developers.buffer.com/reference.html#type/InvalidInputError)!]!
The recoverable errors behind this failure.
message : String!
Summary error message.
TYPE ⚠️ Experimental
# UpdateContentItemSuccess
Successful updateContentItem response.
## Fields 1
contentItem : [ContentItem](https://developers.buffer.com/reference.html#type/ContentItem)!
The content item after the update.
TYPE 🧪 Preview
# UpdatePostTemplateSuccess
Successful result of an end user updating a post template.
## Fields 1
postTemplate : [PostTemplate](https://developers.buffer.com/reference.html#type/PostTemplate)!
The updated post template.
TYPE ⚠️ Experimental
# UpdateSnippetSuccess
Success response of the updateSnippet mutation.
## Fields 1
snippet : [Snippet](https://developers.buffer.com/reference.html#type/Snippet)!
The snippet after the update.
TYPE
# UserTag
User tag in the image
## Fields 3
handle : String!
The handle (username) of the tagged account, without the leading @.
x : Float!
Horizontal position of the tag as a normalized decimal float between 0.0 and 1.0 - the fraction of the image width from the left edge (0.5 is the horizontal center).
y : Float!
Vertical position of the tag as a normalized decimal float between 0.0 and 1.0 - the fraction of the image height from the top edge (0.5 is the vertical center).
TYPE
# VideoAsset
Video asset
Implements: [Asset](https://developers.buffer.com/reference.html#type/Asset)
## Fields 6
id : ID
The ID of the asset in the database
mimeType : String!
The MIME type of the asset
source : String!
URL to the file source
thumbnail : String!
URL to the static thumbnail of the asset
type : [AssetType](https://developers.buffer.com/reference.html#type/AssetType)!
The type of the asset
video : [VideoMetadata](https://developers.buffer.com/reference.html#type/VideoMetadata)!
Video specific metadata
TYPE
# VideoMetadata
Video metadata
## Fields 14
audioCodec : String
Audio codec
containerFormat : String
Video container format
durationMs : Int!
Video duration in seconds
fileSize : Int
Video fileSize in bytes
frameRate : Int
Video framerate
height : Int!
Video height in pixels
isTranscodingRequired : Boolean!
Whether the video needs to be transcoded before it can be broadcasted
isVideoProcessing : Boolean!
Whether the video is currently being processed (transcoding in progress)
rotationDegree : Int
Rotation degree
thumbnailOffset : Int
Offset of the thumbnail chosen for the video, in ms
title : String
Video title
videoBitRate : Int
Video bitrate in kbps
videoCodec : String
Video codec
width : Int!
Video width in pixels
TYPE
# VoidMutationError
Error implementation that allows clients to resolve the MutationError on mutations that do not currently have typed errors. This allows clients to automatically handle errors that may be added to a mutation in future.
Do not directly throw this error, use a custom typed error instead
Implements: [MutationError](https://developers.buffer.com/reference.html#type/MutationError)
## Fields 1
message : String!
Error message
TYPE
# WeeklyPostingLimit
Weekly posting limit for a channel
## Fields 3
limit : Int!
The weekly posting limit for the channel
scheduled : Int!
The number of posts the channel has scheduled for this week
sent : Int!
The number of posts the channel has sent this week
TYPE
# WhatsAppMetadata
The WhatsApp phone's connection details, without credentials or synchronization request IDs.
## Fields 4
businessPortfolioId : String!
The Meta business portfolio that owns the WhatsApp Business Account.
lastSubscribedAt : [DateTime](https://developers.buffer.com/reference.html#type/DateTime)
When Buffer last confirmed the WABA subscription. Null before confirmation.
phoneNumberId : String!
Meta's ID for the business phone.
wabaId : String!
The WhatsApp Business Account that owns the phone.
TYPE
# YoutubeCategory
## Fields 2
categoryId : String!
No description provided.
title : String!
No description provided.
TYPE
# YoutubeMetadata
Youtube metadata
## Fields 1
defaultToReminders : Boolean!
Indicates if we should default to reminder for Youtube
TYPE
# YoutubePostMetadata
Youtube post metadata
Implements: [CommonPostMetadata](https://developers.buffer.com/reference.html#type/CommonPostMetadata)
## Fields 10
annotations : [[Annotation](https://developers.buffer.com/reference.html#type/Annotation)!]!
Annotations representing entities in the text
category : [YoutubeCategory](https://developers.buffer.com/reference.html#type/YoutubeCategory)
Post category
embeddable : Boolean!
Indicates whether the video allows embedding
isAiGenerated : Boolean!
Whether the post discloses AI-generated content
license : [YoutubeLicense](https://developers.buffer.com/reference.html#type/YoutubeLicense)
Video license
madeForKids : Boolean!
Indicates whether the video is suitable for kids
notifySubscribers : Boolean!
Indicates whether to notify subscribers on publish video
privacy : [YoutubePrivacy](https://developers.buffer.com/reference.html#type/YoutubePrivacy)
Privacy setting for post
title : String
Title of the Youtube post
type : [PostType](https://developers.buffer.com/reference.html#type/PostType)!
The channel-specific type of the post, eg, post, story, reel for Youtube
INPUT ⚠️ Experimental
# AddPostToContentItemInput
Input for addPostToContentItem.
## Fields 2
id : [ContentItemId](https://developers.buffer.com/reference.html#type/ContentItemId)!
The content item to add the post to.
postId : [PostId](https://developers.buffer.com/reference.html#type/PostId)!
The post to add. The post must already exist. The post and the content item must belong to the same organization.
INPUT
# AggregatedPostMetricsInput
Input for the `aggregatedPostMetrics` query.
## Fields 5
channelIds : [[ChannelId](https://developers.buffer.com/reference.html#type/ChannelId)!]
Optional list of channel IDs to filter by. When omitted (null), the aggregate spans every channel in the organization the actor has insights access to. When set to an empty array, no channels match and the result is empty.
endDateTime : [DateTime](https://developers.buffer.com/reference.html#type/DateTime)!
End of the aggregation window. Consumers typically pass UTC midnight of the last calendar day in the window (the backend treats the range as inclusive of that day), for example `2026-01-31T00:00:00Z`. Date range is capped to 365 days.
organizationId : [OrganizationId](https://developers.buffer.com/reference.html#type/OrganizationId)!
The organization ID
startDateTime : [DateTime](https://developers.buffer.com/reference.html#type/DateTime)!
Start of the aggregation window. Consumers typically pass UTC midnight of the first calendar day in the window, for example `2026-01-01T00:00:00Z`.
tags : [TagComparator](https://developers.buffer.com/reference.html#type/TagComparator)
Filter to posts with specific tags. When omitted, all posts are included regardless of tags.
INPUT
# AnnotationInputFacebook
Annotation representing all the entities in the text
## Fields 4
content : String!
The content of the annotation, e.g. '107509875938399'
indices : [Int!]!
The indices of the annotation in the text, e.g. [6, 9] (from 6 to 9 characters in the text)
text : String!
The text representation of the annotation, eg 'Buffer'
url : String!
The URL the annotation points to, e.g. <https://www.facebook.com/107509875938399>
INPUT
# AnnotationInputLinkedIn
Annotation representing all the entities in the text
## Fields 7
id : String!
The id of the annotation, e.g. 1521226
entity : String!
The entity of the annotation, e.g. urn:li:organization:1521226
length : Int!
The length of the annotation, e.g. 6
link : String!
The link of the annotation, e.g. <https://www.linkedin.com/company/bufferapp>
localizedName : String!
The localized name of the annotation, e.g. Buffer
start : Int!
The start of the annotation, e.g. 5
vanityName : String!
The vanity name of the annotation, e.g. bufferapp
INPUT
# AssetInput
A single entity's asset. Exactly one variant must be provided.
## Fields 4
document : [DocumentAssetInput](https://developers.buffer.com/reference.html#type/DocumentAssetInput)
Document asset
image : [ImageAssetInput](https://developers.buffer.com/reference.html#type/ImageAssetInput)
Image asset
link : [LinkAssetInput](https://developers.buffer.com/reference.html#type/LinkAssetInput)
Use metadata.{service}.linkAttachment instead. This field will be removed on December 15, 2026.
video : [VideoAssetInput](https://developers.buffer.com/reference.html#type/VideoAssetInput)
Video asset
INPUT
# BlueskyPostMetadataInput
Bluesky post metadata
## Fields 2
linkAttachment : [LinkAttachmentInput](https://developers.buffer.com/reference.html#type/LinkAttachmentInput)
Link attachment. Mutually exclusive with a non-empty `assets` array — input providing both is rejected.
thread : [[ThreadedPostInput](https://developers.buffer.com/reference.html#type/ThreadedPostInput)!]
The ordered list of posts that make up the thread (not paginated). This array is the source of truth for what gets published: every post in the thread, including the root post, must be provided here. Posts are published in order, each replying to the previous one. The first item is the root post and should match the top-level `text` on the post input.
INPUT
# ChannelInput
Input for the channel query
## Fields 1
id : [ChannelId](https://developers.buffer.com/reference.html#type/ChannelId)!
The ID of the channel to be retrieved
INPUT
# ChannelsFiltersInput
Filter to pass when fetching channels.
## Fields 2
isLocked : Boolean
If not defined, it returns all channels Else, if true, it only returns locked channels if false, it only returns not locked channels
product : [Product](https://developers.buffer.com/reference.html#type/Product)
If not passed, it return all channels Else, it filters the channels based on what the product supports.
INPUT
# ChannelsInput
Input to pass when fetching channels.
## Fields 2
filter : [ChannelsFiltersInput](https://developers.buffer.com/reference.html#type/ChannelsFiltersInput)
A list of option filters - passing null means we don't want to filter
organizationId : [OrganizationId](https://developers.buffer.com/reference.html#type/OrganizationId)!
The Organization id to fetch channels for
INPUT ⚠️ Experimental
# ConfigurationInput
Input for the configuration query.
## Fields 1
organizationId : [OrganizationId](https://developers.buffer.com/reference.html#type/OrganizationId)!
The organization to return configuration for.
INPUT ⚠️ Experimental
# ContentItemInput
Input for fetching a single content item by id.
## Fields 1
id : [ContentItemId](https://developers.buffer.com/reference.html#type/ContentItemId)!
The unique identifier of the content item to fetch.
INPUT ⚠️ Experimental
# ContentItemsFilter
Filters for listing content items. Omitted fields do not filter.
## Fields 3
contentStatus : [ContentItemStatus](https://developers.buffer.com/reference.html#type/ContentItemStatus)
Only return content items with this content status. When omitted, content items in every status are returned.
tags : [TagComparator](https://developers.buffer.com/reference.html#type/TagComparator)
Only return content items carrying one of these tags, or, with `isEmpty`, content items with no tags at all. Matches the tags applied to the content item itself, not tags applied later to an individual post.
targetDate : [ContentItemsTargetDateFilter](https://developers.buffer.com/reference.html#type/ContentItemsTargetDateFilter)
Only return content items matching this target date filter.
INPUT ⚠️ Experimental
# ContentItemsInput
Input for listing an organization's content items.
## Fields 3
filter : [ContentItemsFilter](https://developers.buffer.com/reference.html#type/ContentItemsFilter)
Filters to apply. When omitted, all of the organization's content items are returned.
organizationId : [OrganizationId](https://developers.buffer.com/reference.html#type/OrganizationId)!
Organization to list content items for. The caller must be a member of this organization.
sort : [[ContentItemsSortInput](https://developers.buffer.com/reference.html#type/ContentItemsSortInput)!]
Sorting to apply, each entry breaking ties in the one before it. Defaults to newest first. A pagination cursor is only valid for the sort that produced it, so reset `after` to null whenever the sort changes.
INPUT ⚠️ Experimental
# ContentItemsSortInput
One sorting criterion for the content items query. List several to break ties.
## Fields 2
direction : [SortDirection](https://developers.buffer.com/reference.html#type/SortDirection)!
The direction to sort by.
field : [ContentItemSortableKey](https://developers.buffer.com/reference.html#type/ContentItemSortableKey)!
The field to sort by.
INPUT ⚠️ Experimental
# ContentItemsTargetDateFilter
Filter for a content item's target date. Provide exactly one field (enforced by @oneOf).
## Fields 2
presence : [DateTimePresence](https://developers.buffer.com/reference.html#type/DateTimePresence)
Only return content items by whether a target date is set: `present` returns only dated items, `absent` only undated ones.
range : [DateTimeComparator](https://developers.buffer.com/reference.html#type/DateTimeComparator)
Only return content items whose target date falls within this range. A range with no bounds returns every content item that has a target date.
INPUT ⚠️ Experimental
# CreateContentItemDraftInput
Input for createContentItemDraft.
## Fields 6
correlationId : [Uuid](https://developers.buffer.com/reference.html#type/Uuid)
Client-generated UUID that makes draft creation idempotent. A retry with the same UUID in the same organization returns the first content item in its current state.
draft : [DraftContentInput](https://developers.buffer.com/reference.html#type/DraftContentInput)!
The channel-less draft content to start with.
organizationId : [OrganizationId](https://developers.buffer.com/reference.html#type/OrganizationId)!
Organization that will own the content item.
tagIds : [[TagId](https://developers.buffer.com/reference.html#type/TagId)!]
Tags to apply to this content item. Omit to create it with no tags.
targetDate : [DateTime](https://developers.buffer.com/reference.html#type/DateTime)
Optional date indicating when this piece of content should go out. This is a planning aid only and does not schedule any posts.
title : String
Optional title describing what this piece of content is about.
INPUT ⚠️ Experimental
# CreateContentItemInput
Input for createContentItem.
## Fields 5
organizationId : [OrganizationId](https://developers.buffer.com/reference.html#type/OrganizationId)!
Organization that owns the content item and all variants created in it.
posts : [[CreatePostInput](https://developers.buffer.com/reference.html#type/CreatePostInput)!]!
The channel-specific post variants to create, one per channel. Provide at least one variant, and at most one variant per channel.
tagIds : [[TagId](https://developers.buffer.com/reference.html#type/TagId)!]
Tags to apply to this content item. Omit to create it with no tags.
targetDate : [DateTime](https://developers.buffer.com/reference.html#type/DateTime)
Optional date indicating when this piece of content should go out. This is a planning aid only and does not schedule any posts.
title : String
Optional title describing what this piece of content is about.
INPUT
# CreateIdeaInput
createIdea input type
## Fields 5
content : [IdeaContentInput](https://developers.buffer.com/reference.html#type/IdeaContentInput)!
Content and metadata for the new idea
cta : String
Call-to-action identifier for analytics tracking
group : [IdeaGroupInput](https://developers.buffer.com/reference.html#type/IdeaGroupInput)
Group placement (null for unassigned group)
organizationId : ID!
Organization ID that will own the idea
templateId : String
Template ID used to create the idea
INPUT
# CreatePostInput
Create post's request input.
Note: `metadata.{service}.linkAttachment` is mutually exclusive with a non-empty `assets` array. Input providing both is rejected.
## Fields 14
aiAssisted : Boolean
If this post was created with the help of AI
assets : [[AssetInput](https://developers.buffer.com/reference.html#type/AssetInput)!]!
Ordered list of assets on this post.
channelId : [ChannelId](https://developers.buffer.com/reference.html#type/ChannelId)!
Channel's Id for which we want to create the post
draftId : [DraftId](https://developers.buffer.com/reference.html#type/DraftId)
Is set when the Post is generated from a Draft
dueAt : [DateTime](https://developers.buffer.com/reference.html#type/DateTime)
Date when the post is scheduled to be published
ideaId : [IdeaId](https://developers.buffer.com/reference.html#type/IdeaId)
Is set when the Post is generated from an Idea
metadata : [PostInputMetaData](https://developers.buffer.com/reference.html#type/PostInputMetaData)
Metadata of the post which differs based on the social network/service
mode : [ShareMode](https://developers.buffer.com/reference.html#type/ShareMode)!
How the post is being scheduled.
needsApproval : Boolean!
Submit the post for approval instead of scheduling it. A post submitted for approval is always a draft, so this conflicts with turning `saveToDraft` off.
Only valid when your posting policy on the target channel requires approval.
saveToDraft : Boolean
If true, saves the post as a draft instead of scheduling it. When saving as draft:
  * Post status will be 'draft' instead of 'buffer'
  * Posting limits are not checked
  * The post will not be published until explicitly scheduled


schedulingType : [SchedulingType](https://developers.buffer.com/reference.html#type/SchedulingType)!
Scheduling type to indicate notification publishing or automatic publishing
source : String
source where the composer was initiated from, used for tracking.
tagIds : [[TagId](https://developers.buffer.com/reference.html#type/TagId)!]
List of tag IDs
text : String
Text content of the Post.
Note: for threaded posts, this needs to match the first item in the `thread` array.
INPUT
# CreatePostTemplateInput
Input for an end user creating a post template. Buffer-curated taxonomy fields are server-defaulted; setting them is only available to official Buffer clients.
## Fields 6
body : String! 🧪 Preview
The main content body of the template, may contain {{placeholders}}.
description : String 🧪 Preview
A short user-facing description of the template. Nullable for backwards-compat at the GraphQL boundary — the resolver rejects null/empty values with a clear input error so the underlying storage contract (non-empty string) is still honored.
emoji : String 🧪 Preview
The emoji associated with the template.
organizationId : [OrganizationId](https://developers.buffer.com/reference.html#type/OrganizationId)! 🧪 Preview
Organization the template belongs to. The caller must be a member of this organization. For `internal` visibility this is the team scope; for `private` it's recorded on the template but does not affect visibility.
title : String! 🧪 Preview
The title of the template.
visibility : [PostTemplateVisibility](https://developers.buffer.com/reference.html#type/PostTemplateVisibility) 🧪 Preview
Defaults to `private` if omitted. `public` is rejected — it is only available to official Buffer clients.
INPUT ⚠️ Experimental
# CreateSnippetInput
Input for the createSnippet mutation.
## Fields 3
name : String!
Display name of the snippet.
organizationId : [OrganizationId](https://developers.buffer.com/reference.html#type/OrganizationId)!
The organization that owns the snippet.
text : String!
The hashtags, as the text that is inserted into a post.
INPUT ⚠️ Experimental
# CreateTagInput
Input for creating a tag.
## Fields 2
organizationId : [OrganizationId](https://developers.buffer.com/reference.html#type/OrganizationId)!
Organization to create the tag in. The caller must be an administrator of this organization.
tag : [TagToCreateInput](https://developers.buffer.com/reference.html#type/TagToCreateInput)!
The name and color to give the new tag.
INPUT
# DailyPostingLimitsInput
Input for the dailyPostingLimits query.
## Fields 2
channelIds : [[ChannelId](https://developers.buffer.com/reference.html#type/ChannelId)!]!
List of channel IDs to check limits for. All channels must belong to the same organization.
date : [DateTime](https://developers.buffer.com/reference.html#type/DateTime)
The intended posting time. Defaults to now if not provided. For X, the exact time determines the affected rolling 24-hour windows. For other networks, the date selects the channel's local calendar day.
INPUT
# DateTimeComparator
Comparator for filtering by date
## Fields 2
end : [DateTime](https://developers.buffer.com/reference.html#type/DateTime)
Include results with dates equal to or before the specified date
start : [DateTime](https://developers.buffer.com/reference.html#type/DateTime)
Include results with dates equal to or after the specified date
INPUT ⚠️ Experimental
# DeleteContentItemInput
Input for deleteContentItem.
## Fields 1
id : [ContentItemId](https://developers.buffer.com/reference.html#type/ContentItemId)!
The content item to delete.
INPUT
# DeletePostInput
deletePost mutation deletes a post by id.
## Fields 1
id : [PostId](https://developers.buffer.com/reference.html#type/PostId)!
Post id to delete.
INPUT 🧪 Preview
# DeletePostTemplateInput
Input for an end user deleting a post template.
## Fields 1
id : [PostTemplateId](https://developers.buffer.com/reference.html#type/PostTemplateId)!
The ID of the template to delete.
INPUT ⚠️ Experimental
# DeleteSnippetInput
Input for the deleteSnippet mutation.
## Fields 2
id : [SnippetId](https://developers.buffer.com/reference.html#type/SnippetId)!
The snippet to delete.
organizationId : [OrganizationId](https://developers.buffer.com/reference.html#type/OrganizationId)!
The organization that owns the snippet.
INPUT ⚠️ Experimental
# DeleteTagInput
Input for deleting a tag.
## Fields 1
id : [TagId](https://developers.buffer.com/reference.html#type/TagId)!
The tag to delete. Its organization is taken from the tag itself, and the caller must be an administrator of that organization.
INPUT
# DocumentAssetInput
Document asset
## Fields 3
thumbnailUrl : String!
Document thumbnail URL
title : String!
Document title
url : String!
Document URL
INPUT ⚠️ Experimental
# DraftContentInput
A channel-less draft to save on a content item.
## Fields 3
aiAssisted : Boolean!
Set to true when the draft content was written with the help of AI.
assets : [[AssetInput](https://developers.buffer.com/reference.html#type/AssetInput)!]!
Images, videos, or documents to attach to the draft, in display order.
text : String!
The written content of the draft. Can be empty when the draft holds at least one asset.
INPUT
# EditPostInput
Edit post's request input.
Note: `metadata.{service}.linkAttachment` is mutually exclusive with a non-empty `assets` array. Input providing both is rejected.
## Fields 14
id : [PostId](https://developers.buffer.com/reference.html#type/PostId)!
ID of the post to edit
aiAssisted : Boolean
If this post was edited with the help of AI
approvalChange : [PostApprovalChange](https://developers.buffer.com/reference.html#type/PostApprovalChange)
Change the post's approval state alongside this edit. Leave unset to keep the post's current approval state.
Only valid when your posting policy on the post's channel requires approval, and only on your own drafts. Asking for the state the post is already in does nothing.
assets : [[AssetInput](https://developers.buffer.com/reference.html#type/AssetInput)!]
Ordered list of assets on this post. Omit to preserve the existing list, pass an empty array to clear it
draftId : [DraftId](https://developers.buffer.com/reference.html#type/DraftId)
Is set when the Post is generated from a Draft
dueAt : [DateTime](https://developers.buffer.com/reference.html#type/DateTime)
Date when the post is scheduled to be published
ideaId : [IdeaId](https://developers.buffer.com/reference.html#type/IdeaId)
Is set when the Post is generated from an Idea
metadata : [PostInputMetaData](https://developers.buffer.com/reference.html#type/PostInputMetaData)
Metadata of the post which differs based on the social network/service
mode : [ShareMode](https://developers.buffer.com/reference.html#type/ShareMode)
How the post is being scheduled. Omit the field or pass null to make no scheduling change — null does not clear or reset the schedule: a scheduled post keeps its current share mode, queue slot, and any custom time, and the edit applies only the other provided fields. Pass a non-null ShareMode to apply that mode.
saveToDraft : Boolean
If true, saves the post as a draft instead of keeping it scheduled. When saving as draft:
  * Post status will be 'draft' instead of 'buffer'
  * The post will not be published until explicitly scheduled


schedulingType : [SchedulingType](https://developers.buffer.com/reference.html#type/SchedulingType)
Scheduling type to indicate notification publishing or automatic publishing.
Omit it, or send null, to leave the post publishing the way it already does.
source : String
source where the composer was initiated from, used for tracking.
tagIds : [[TagId](https://developers.buffer.com/reference.html#type/TagId)!]
tags
text : String
Text content of the Post. Omit the field to keep the current text; pass an empty string or null to clear it.
Note: for threaded posts, this needs to match the first item in the `thread` array.
INPUT
# FacebookPostMetadataInput
Facebook post metadata
## Fields 4
annotations : [[AnnotationInputFacebook](https://developers.buffer.com/reference.html#type/AnnotationInputFacebook)!]
Annotations representing entities in the text
firstComment : String
Facebook post's first comment
linkAttachment : [LinkAttachmentInput](https://developers.buffer.com/reference.html#type/LinkAttachmentInput)
Link attachment. Mutually exclusive with a non-empty `assets` array — input providing both is rejected.
type : [PostTypeFacebook](https://developers.buffer.com/reference.html#type/PostTypeFacebook)!
The channel-specific type of the post, eg, post, story, reel for Facebook
INPUT
# GoogleBusinessEventMetaDataInput
Metadata for a GBP post that is an event
## Fields 6
button : [GoogleBusinessPostActionType](https://developers.buffer.com/reference.html#type/GoogleBusinessPostActionType)
Action button. Optional: a post with no button, or `none`, publishes without a call-to-action. On edit, omitting it preserves the existing value.
endDate : [DateTime](https://developers.buffer.com/reference.html#type/DateTime)
End date of the event. Required on create; optional on edit (omitted preserves existing value).
isFullDayEvent : Boolean!
Indicate whether the event has a start or end time.
link : String
Link to the action
startDate : [DateTime](https://developers.buffer.com/reference.html#type/DateTime)
Start date of the event. Required on create; optional on edit (omitted preserves existing value).
title : String
Title of the event. Required on create; optional on edit (omitted preserves existing value).
INPUT
# GoogleBusinessOfferMetaDataInput
Metadata for a GBP post that is an offer
## Fields 6
code : String
Coupon code for the offer
endDate : [DateTime](https://developers.buffer.com/reference.html#type/DateTime)
End date of the offer. Required on create; optional on edit (omitted preserves existing value).
link : String
Link to the offer
startDate : [DateTime](https://developers.buffer.com/reference.html#type/DateTime)
Start date of the offer. Required on create; optional on edit (omitted preserves existing value).
terms : String
Terms and Conditions
title : String
Title of the offer. Required on create; optional on edit (omitted preserves existing value).
INPUT
# GoogleBusinessPostMetadataInput
Google Business Profile post metadata @deprecated: pending proposal for specific GBP post types: update, offer and event metadata types
## Fields 5
detailsEvent : [GoogleBusinessEventMetaDataInput](https://developers.buffer.com/reference.html#type/GoogleBusinessEventMetaDataInput)
Details of the Event metadata
detailsOffer : [GoogleBusinessOfferMetaDataInput](https://developers.buffer.com/reference.html#type/GoogleBusinessOfferMetaDataInput)
Details of the Offer metadata
detailsWhatsNew : [GoogleBusinessWhatsNewMetaDataInput](https://developers.buffer.com/reference.html#type/GoogleBusinessWhatsNewMetaDataInput)
Details of the Whats new metadata
title : String
Title if available in the given GBP post type: event and offer
type : [PostTypeGoogleBusiness](https://developers.buffer.com/reference.html#type/PostTypeGoogleBusiness)!
The channel-specific type of the post, eg, post, offer, event for Google Business Profile
INPUT
# GoogleBusinessWhatsNewMetaDataInput
Metadata for a GBP post of type Whats new
## Fields 2
button : [GoogleBusinessPostActionType](https://developers.buffer.com/reference.html#type/GoogleBusinessPostActionType)
Action button. Optional: a post with no button, or `none`, publishes without a call-to-action. On edit, omitting it preserves the existing value.
link : String
Link to the action
INPUT
# IdeaContentInput
content input for creating/updating an idea
## Fields 7
aiAssisted : Boolean
Whether AI tools were used in creation
date : [DateTime](https://developers.buffer.com/reference.html#type/DateTime)
Target date for the idea, often used for planning publish schedules
media : [[IdeaMediaInput](https://developers.buffer.com/reference.html#type/IdeaMediaInput)!]
List of media items to attach
services : [[Service](https://developers.buffer.com/reference.html#type/Service)!]
Services associated with the idea for targeting specific platforms
tags : [[TagInput](https://developers.buffer.com/reference.html#type/TagInput)!]
Tags to categorize the idea
text : String
Main body text or description
title : String
Title or headline of the idea
INPUT
# IdeaGroupInput
idea group input for create/update
## Fields 2
groupId : ID
Target group ID (null for unassigned group)
placeAfterId : ID
ID of idea to place after (null for top position)
INPUT
# IdeaGroupsInput
Input type for retrieving idea groups by organization ID.
## Fields 1
organizationId : ID!
Unique identifier for the organization.
INPUT
# IdeaMediaInput
## Fields 6
url : String!
The URL of the media
alt : String
Alternative text for the media
thumbnailUrl : String
Thumbnail URL for the media
type : [MediaType](https://developers.buffer.com/reference.html#type/MediaType)!
The type of media (image, gif, video, link, document, unsupported). Note: 'video' is not supported via public API
size : Int
The size of the media in bytes
source : [IdeaMediaSourceInput](https://developers.buffer.com/reference.html#type/IdeaMediaSourceInput)
Source information for the media
INPUT
# IdeaMediaSourceInput
Input type for the source information of media attached to an idea
## Fields 5
name : String!
No description provided.
id : String
No description provided.
trigger : String
No description provided.
author : String
for unsplash only
authorUrl : String
No description provided.
INPUT
# IdeasGroupFilter
Selects which ideas to return by group membership. Exactly one field must be provided (enforced by @oneOf). To return ideas from all groups, omit `groupFilter` on IdeasInput rather than setting a field here.
## Fields 2
groups : [ID!]
Return only ideas that belong to these specific groups (union/OR).
membership : [IdeaGroupMembership](https://developers.buffer.com/reference.html#type/IdeaGroupMembership)
Return ideas by a group-membership bucket rather than by specific group IDs.
INPUT
# IdeasInput
Filtering criteria for the ideas list.
## Fields 3
groupFilter : [IdeasGroupFilter](https://developers.buffer.com/reference.html#type/IdeasGroupFilter)
Filter ideas by group membership. Omit this field entirely to return ideas across all groups.
organizationId : [OrganizationId](https://developers.buffer.com/reference.html#type/OrganizationId)!
The organization to fetch ideas from.
tagsFilter : [TagComparator](https://developers.buffer.com/reference.html#type/TagComparator)
Filter ideas by tags using TagComparator.
INPUT
# ImageAssetInput
Image asset
## Fields 3
metadata : [ImageMetadataInput](https://developers.buffer.com/reference.html#type/ImageMetadataInput)
Image specific metadata
thumbnailUrl : String
URL to the static thumbnail of the asset
url : String!
URL to the file source
INPUT
# ImageDimensionsInput
Image dimensions
## Fields 2
height : Int!
Image height in pixels
width : Int!
Image width in pixels
INPUT
# ImageMetadataInput
Image metadata
## Fields 4
altText : String!
Alternative text for accessibility
animatedThumbnail : String
Animated thumbnail URL
dimensions : [ImageDimensionsInput](https://developers.buffer.com/reference.html#type/ImageDimensionsInput)
Ignored — the API resolves image dimensions itself.
userTags : [[UserTagInput](https://developers.buffer.com/reference.html#type/UserTagInput)!]
Accounts to tag at specific points on the image. Each tag's x/y position uses normalized 0.0-1.0 coordinates - see UserTagInput.
INPUT ⚠️ Experimental
# InstagramAudioCatalogInput
Input for browsing trending music and original sounds.
## Fields 1
channelId : [ChannelId](https://developers.buffer.com/reference.html#type/ChannelId)!
Instagram channel used to authorize the catalog request.
INPUT ⚠️ Experimental
# InstagramAudioInput
Input for refreshing a single Instagram audio asset
## Fields 2
audioId : String!
Meta audio asset ID
channelId : [ChannelId](https://developers.buffer.com/reference.html#type/ChannelId)!
Instagram channel used to authorize the refresh
INPUT
# InstagramGeolocationInput
Instagram Geolocation
## Fields 2
id : String
The id of this location
text : String
The name of this location
INPUT
# InstagramPostMetadataInput
Instagram post metadata
## Fields 7
firstComment : String
Instagram post's first comment
geolocation : [InstagramGeolocationInput](https://developers.buffer.com/reference.html#type/InstagramGeolocationInput)
Geolocation of the post
isAiGenerated : Boolean
Whether the post discloses AI-generated content
link : String
Shop Grid link for the post
shouldShareToFeed : Boolean!
Indicates whether post should be shared to feed
stickerFields : [InstagramStickerFieldsInput](https://developers.buffer.com/reference.html#type/InstagramStickerFieldsInput)
Sticker fields for reminder-based publishing
type : [PostType](https://developers.buffer.com/reference.html#type/PostType)!
The channel-specific type of the post, eg, post, story, reel for Instagram
INPUT
# InstagramStickerFieldsInput
Instagram fields for reminder-based publishing. Upon the reminder for publishing, the user is prompted to copy and paste these fields into the Instagram app to complete the post.
## Fields 5
music : String
Placeholder text for the post's music
other : String
Additional field for any other post content
products : String
Placeholder text for the post's linked products
text : String
Text for the Story or Reel
topics : String
Placeholder text for the post's topics (Reels only)
INPUT
# LinkAssetInput
Link attached to the post
## Fields 4
description : String
Description of the link
thumbnailUrl : String
Thumbnail URL of the link
title : String
Title of the link
url : String!
URL to the link
INPUT
# LinkAttachmentInput
Link attachment
## Fields 4
description : String
Description shown on the link card
thumbnail : [LinkAttachmentThumbnailInput](https://developers.buffer.com/reference.html#type/LinkAttachmentThumbnailInput)
Thumbnail shown on the link card
title : String
Title shown on the link card
url : String!
URL that the link asset has been built from
INPUT
# LinkAttachmentThumbnailInput
Thumbnail of a link attachment
## Fields 1
url : String!
URL of the thumbnail image
INPUT
# LinkedInPostMetadataInput
LinkedIn post metadata
## Fields 3
annotations : [[AnnotationInputLinkedIn](https://developers.buffer.com/reference.html#type/AnnotationInputLinkedIn)!]
Annotations representing entities in the text
firstComment : String
LinkedIn post's first comment
linkAttachment : [LinkAttachmentInput](https://developers.buffer.com/reference.html#type/LinkAttachmentInput)
Link attachment. Mutually exclusive with a non-empty `assets` array — input providing both is rejected.
INPUT
# MastodonPostMetadataInput
Mastodon post metadata
## Fields 2
spoilerText : String
Spoiler text hiding the root text of this post
thread : [[ThreadedPostInput](https://developers.buffer.com/reference.html#type/ThreadedPostInput)!]
The ordered list of posts that make up the thread (not paginated). This array is the source of truth for what gets published: every post in the thread, including the root post, must be provided here. Posts are published in order, each replying to the previous one. The first item is the root post and should match the top-level `text` on the post input.
INPUT ⚠️ Experimental
# MovePostInQueueInput
movePostInQueue mutation moves a queued post to the top or bottom of its channel's queue.
## Fields 2
id : [PostId](https://developers.buffer.com/reference.html#type/PostId)!
ID of the post to move.
position : [QueuePosition](https://developers.buffer.com/reference.html#type/QueuePosition)!
Target position within the channel's queue.
INPUT
# OrganizationFilterInput
Allow retrieving a specific Organization
## Fields 1
organizationId : String!
No description provided.
INPUT
# PinterestPostMetadataInput
Pinterest post metadata
## Fields 3
boardServiceId : String
The board ID of the Pin, can be obtained when fetching the channel details with the following query:
Copy Copied! 
```
query GetChannelWithSubprofiles {
  channel(input: { id: "[CHANNEL_ID_HERE]" }) {
    metadata {
      ... on PinterestMetadata {
        boards {
          serviceId
        }
      }
    }
  }
}
```

Required on create; optional on edit (omitted preserves existing board).
title : String
The title of the Pin
url : String
The Pin destination link
INPUT
# PostInput
Input for the post query
## Fields 1
id : [PostId](https://developers.buffer.com/reference.html#type/PostId)!
The ID of the post to be retrieved
INPUT
# PostInputMetaData
Metadata of the post which differs based on the social network/service
## Fields 12
bluesky : [BlueskyPostMetadataInput](https://developers.buffer.com/reference.html#type/BlueskyPostMetadataInput)
Metadata for Bluesky post
facebook : [FacebookPostMetadataInput](https://developers.buffer.com/reference.html#type/FacebookPostMetadataInput)
Metadata for Facebook post
google : [GoogleBusinessPostMetadataInput](https://developers.buffer.com/reference.html#type/GoogleBusinessPostMetadataInput)
Metadata for Google Business Profile post
instagram : [InstagramPostMetadataInput](https://developers.buffer.com/reference.html#type/InstagramPostMetadataInput)
Metadata for Instagram post
linkedin : [LinkedInPostMetadataInput](https://developers.buffer.com/reference.html#type/LinkedInPostMetadataInput)
Metadata for LinkedIn post
mastodon : [MastodonPostMetadataInput](https://developers.buffer.com/reference.html#type/MastodonPostMetadataInput)
Metadata for Mastodon post
pinterest : [PinterestPostMetadataInput](https://developers.buffer.com/reference.html#type/PinterestPostMetadataInput)
Metadata for Pinterest post
substack : [SubstackPostMetadataInput](https://developers.buffer.com/reference.html#type/SubstackPostMetadataInput)
Metadata for Substack post
threads : [ThreadsPostMetadataInput](https://developers.buffer.com/reference.html#type/ThreadsPostMetadataInput)
Metadata for Threads post
tiktok : [TikTokPostMetadataInput](https://developers.buffer.com/reference.html#type/TikTokPostMetadataInput)
Metadata for TikTok post
twitter : [TwitterPostMetadataInput](https://developers.buffer.com/reference.html#type/TwitterPostMetadataInput)
Metadata for Twitter post
youtube : [YoutubePostMetadataInput](https://developers.buffer.com/reference.html#type/YoutubePostMetadataInput)
Metadata for Youtube post
INPUT
# PostsFiltersInput
Filter to apply to the posts query
## Fields 10
channelIds : [[ChannelId](https://developers.buffer.com/reference.html#type/ChannelId)!]
When set, it will filter posts by channel
dueAt : [DateTimeComparator](https://developers.buffer.com/reference.html#type/DateTimeComparator)
When set, it will filter posts by their scheduled posting date
dueAtPresence : [DateTimePresence](https://developers.buffer.com/reference.html#type/DateTimePresence)
When set, it will filter posts by whether their scheduled posting date exists. `absent` cannot be combined with `dueAt`, because absent dates cannot also match a date range.
endDate : [DateTime](https://developers.buffer.com/reference.html#type/DateTime)
When set, it will return posts with createdAt or dueAt date before endDate
postTypes : [[PostType](https://developers.buffer.com/reference.html#type/PostType)!] ⚠️ Experimental
When set, it will filter posts by format.
`post` is a fallback bucket rather than one stored format: it matches every post the other formats do not claim, which is what `Post.metadata.type` reports for the same post. `carousel` and `thread` are rejected, because no stored value resolves to them.
startDate : [DateTime](https://developers.buffer.com/reference.html#type/DateTime)
When set, it will return posts with createdAt or dueAt date after startDate
status : [[PostStatus](https://developers.buffer.com/reference.html#type/PostStatus)!]
When set, it will filter posts by status
tagIds : [[TagId](https://developers.buffer.com/reference.html#type/TagId)!]
When set, it will filter posts by tag
tags : [TagComparator](https://developers.buffer.com/reference.html#type/TagComparator)
Filter posts by tags. Supports specific tags, untagged posts, or union of both.
createdAt : [DateTimeComparator](https://developers.buffer.com/reference.html#type/DateTimeComparator)
When set, it will filter posts by the date they were created
INPUT
# PostsInput
Input for the posts query
## Fields 3
filter : [PostsFiltersInput](https://developers.buffer.com/reference.html#type/PostsFiltersInput)
The filters to apply to the posts query
organizationId : [OrganizationId](https://developers.buffer.com/reference.html#type/OrganizationId)!
The Organization id to fetch posts for
sort : [[PostSortInput](https://developers.buffer.com/reference.html#type/PostSortInput)!]
The sort to apply to the posts results
INPUT
# PostSortInput
Sort order of post results. List multiple to create tie-breaking order.
## Fields 2
direction : [SortDirection](https://developers.buffer.com/reference.html#type/SortDirection)!
The direction to sort by.
field : [PostSortableKey](https://developers.buffer.com/reference.html#type/PostSortableKey)!
The field to sort by.
INPUT 🧪 Preview
# PostTemplateInput
Input for fetching a single post template by ID.
## Fields 1
id : [PostTemplateId](https://developers.buffer.com/reference.html#type/PostTemplateId)!
The unique identifier of the template to fetch.
INPUT
# PostTemplatesFilterInput
Filters for the template library. Visibility narrows the actor-scoped result set; it can never widen it.
## Fields 1
visibility : [PostTemplateVisibility](https://developers.buffer.com/reference.html#type/PostTemplateVisibility) 🧪 Preview
Narrow the result to a single visibility scope. Omit to receive the union of: public templates, internal templates from the supplied organization, and private templates from the actor's account.
INPUT 🧪 Preview
# PostTemplatesInput
Input for fetching templates accessible to the current actor for the template library. A caller can never reach templates outside their own scope — the server pins `private` to the actor's account and `internal` to the supplied `organizationId` regardless of input.
## Fields 2
filter : [PostTemplatesFilterInput](https://developers.buffer.com/reference.html#type/PostTemplatesFilterInput)
Optional filters to narrow the template list.
organizationId : [OrganizationId](https://developers.buffer.com/reference.html#type/OrganizationId)!
Organization to scope `internal`-visibility templates to. The caller must be a member of this organization.
INPUT ⚠️ Experimental
# PromoteContentItemDraftToPostsInput
Input for promoteContentItemDraftToPosts.
## Fields 3
id : [ContentItemId](https://developers.buffer.com/reference.html#type/ContentItemId)!
The content item to promote.
posts : [[CreatePostInput](https://developers.buffer.com/reference.html#type/CreatePostInput)!]!
The channel-specific posts to create, one per channel. Provide at least one post, and at most one post per channel.
tagIds : [[TagId](https://developers.buffer.com/reference.html#type/TagId)!]
Tags to apply to this content item. Omit to keep the current tags. An empty list or null removes them all.
INPUT ⚠️ Experimental
# RemovePostFromContentItemInput
Input for removePostFromContentItem.
## Fields 2
id : [ContentItemId](https://developers.buffer.com/reference.html#type/ContentItemId)!
The content item to remove the post from.
postId : [PostId](https://developers.buffer.com/reference.html#type/PostId)!
The post to remove from a content item.
INPUT
# RetweetMetadataInput
Information about the initial Tweet that was retweeted
## Fields 2
id : String!
Retweet ID
comment : String
Optional user comment shown above the embedded retweet
INPUT ⚠️ Experimental
# SearchInstagramAudioCatalogInput
Input for searching both Instagram audio catalogs.
## Fields 2
channelId : [ChannelId](https://developers.buffer.com/reference.html#type/ChannelId)!
Instagram channel used to authorize the search.
query : String!
Search text. Must not be blank.
INPUT ⚠️ Experimental
# SearchInstagramAudioInput
Input for searching Instagram audio for one channel.
## Fields 3
audioType : [InstagramAudioType](https://developers.buffer.com/reference.html#type/InstagramAudioType)!
Music or original sound catalog
channelId : [ChannelId](https://developers.buffer.com/reference.html#type/ChannelId)!
Instagram channel to search audio for
query : String!
Search text. Required. Use trendingInstagramAudio for trending results.
INPUT ⚠️ Experimental
# SnippetsInput
Input for the snippets query.
## Fields 1
organizationId : [OrganizationId](https://developers.buffer.com/reference.html#type/OrganizationId)!
The organization whose snippets to return.
INPUT
# SubstackPostMetadataInput
Substack post metadata
## Fields 1
linkAttachment : [LinkAttachmentInput](https://developers.buffer.com/reference.html#type/LinkAttachmentInput)
Link attachment. Mutually exclusive with a non-empty `assets` array — input providing both is rejected.
INPUT ⚠️ Experimental
# TagByIdInput
Input for fetching a single tag by id.
## Fields 1
id : [TagId](https://developers.buffer.com/reference.html#type/TagId)!
The unique identifier of the tag to fetch.
INPUT
# TagComparator
Comparator for filtering by tags
## Fields 2
in : [[TagId](https://developers.buffer.com/reference.html#type/TagId)!]!
Include results that have any of the specified tags (union/OR).
isEmpty : Boolean!
When true, include results that have no tags assigned. Can be combined with 'in' for union filtering. Defaults to false if not specified.
INPUT
# TagInput
Input type for tag information used in idea creation
## Fields 3
id : ID!
No description provided.
name : String!
No description provided.
color : String!
No description provided.
INPUT ⚠️ Experimental
# TagsFiltersInput
Filters for listing an organization's tags. Omitted fields do not filter.
## Fields 1
isLocked : Boolean
Return only locked tags when true, only unlocked tags when false. Omit to return both. See `Tag.isLocked` for what locking means.
INPUT ⚠️ Experimental
# TagsInput
Input for listing an organization's tags.
## Fields 2
filter : [TagsFiltersInput](https://developers.buffer.com/reference.html#type/TagsFiltersInput)
Filters to apply. When omitted, all of the organization's tags are returned.
organizationId : [OrganizationId](https://developers.buffer.com/reference.html#type/OrganizationId)!
Organization to list tags for. The caller must be a member of this organization.
INPUT ⚠️ Experimental
# TagToCreateInput
The name and color to give a new tag.
## Fields 2
color : String!
The tag's color as a hex triplet: `#` followed by exactly six hex digits, for example `#F523F1`. Shorthand such as `#F51` is rejected. Buffer maps recognized palette colors onto `Tag.colorName`.
name : String!
The tag's display name, for example `Summer sales`. Between 1 and 100 characters, and unique within the organization. Names are compared exactly, so `Summer sales` and `summer sales` can coexist.
INPUT ⚠️ Experimental
# TagToUpdateInput
The name and color to set on an existing tag. Both are replaced, so send the current value for the one you are not changing.
## Fields 2
color : String!
The tag's color as a hex triplet: `#` followed by exactly six hex digits, for example `#F523F1`. Shorthand such as `#F51` is rejected. Buffer maps recognized palette colors onto `Tag.colorName`.
name : String!
The tag's display name, for example `Summer sales`. Between 1 and 100 characters, and unique within the organization. Names are compared exactly, so `Summer sales` and `summer sales` can coexist.
INPUT
# ThreadedPostInput
A post authored by the user which is posted to a thread. This is commonly used for long-format twitter and meta threads posts to allow authored content to span multiple threads. Threads are represented as a list of replies, each replying to the previous one. The first item in the list is the root post of the thread and should match the top-level `text` on the post input; the remaining items are replies.
## Fields 3
assets : [[AssetInput](https://developers.buffer.com/reference.html#type/AssetInput)!]!
Ordered list of assets on this threaded post
metadata : [ThreadItemMetadataInput](https://developers.buffer.com/reference.html#type/ThreadItemMetadataInput)
Service-specific fields for this threaded post
text : String
The text body content of the threaded post
INPUT
# ThreadItemBlueskyMetadataInput
Bluesky fields on a single item of a thread
## Fields 1
linkAttachment : [LinkAttachmentInput](https://developers.buffer.com/reference.html#type/LinkAttachmentInput)
Link attachment. Mutually exclusive with a non-empty `assets` array — input providing both is rejected.
INPUT
# ThreadItemMetadataInput
Service-specific fields on a single item of a thread. The key must match the channel's service; input under any other key is rejected.
## Fields 2
bluesky : [ThreadItemBlueskyMetadataInput](https://developers.buffer.com/reference.html#type/ThreadItemBlueskyMetadataInput)
Bluesky fields for this thread item
threads : [ThreadItemThreadsMetadataInput](https://developers.buffer.com/reference.html#type/ThreadItemThreadsMetadataInput)
Threads fields for this thread item
INPUT
# ThreadItemThreadsMetadataInput
Threads fields on a single item of a thread
## Fields 1
linkAttachment : [LinkAttachmentInput](https://developers.buffer.com/reference.html#type/LinkAttachmentInput)
Link attachment. Mutually exclusive with a non-empty `assets` array — input providing both is rejected.
INPUT
# ThreadsPostMetadataInput
Threads post metadata
## Fields 6
linkAttachment : [LinkAttachmentInput](https://developers.buffer.com/reference.html#type/LinkAttachmentInput)
Link attachment. Mutually exclusive with a non-empty `assets` array — input providing both is rejected.
locationId : String
LocationId associated with the post
locationName : String
Location name associated with the post
thread : [[ThreadedPostInput](https://developers.buffer.com/reference.html#type/ThreadedPostInput)!]
The ordered list of posts that make up the thread (not paginated). This array is the source of truth for what gets published: every post in the thread, including the root post, must be provided here. Posts are published in order, each replying to the previous one. The first item is the root post and should match the top-level `text` on the post input.
topic : String
Topic associated with the post
type : [PostType](https://developers.buffer.com/reference.html#type/PostType)
The type of the post
INPUT
# TikTokPostMetadataInput
TikTok post metadata
## Fields 2
isAiGenerated : Boolean
Whether the post discloses AI-generated content (TikTok video only)
title : String
The title of the TikTok post (for photo posts)
INPUT ⚠️ Experimental
# TrendingInstagramAudioInput
Input for trending Instagram audio for one channel.
## Fields 2
audioType : [InstagramAudioType](https://developers.buffer.com/reference.html#type/InstagramAudioType)!
Music or original sound catalog
channelId : [ChannelId](https://developers.buffer.com/reference.html#type/ChannelId)!
Instagram channel to load trending audio for
INPUT
# TwitterPostMetadataInput
Twitter post metadata
## Fields 3
isAiGenerated : Boolean
Whether the post discloses AI-generated content (original tweets only, never retweets)
retweet : [RetweetMetadataInput](https://developers.buffer.com/reference.html#type/RetweetMetadataInput)
The details of the tweet being retweeted
thread : [[ThreadedPostInput](https://developers.buffer.com/reference.html#type/ThreadedPostInput)!]
The ordered list of posts that make up the thread (not paginated). This array is the source of truth for what gets published: every post in the thread, including the root post, must be provided here. Posts are published in order, each replying to the previous one. The first item is the root post and should match the top-level `text` on the post input.
INPUT ⚠️ Experimental
# UpdateContentItemDraftInput
Input for updateContentItemDraft.
## Fields 4
id : [ContentItemId](https://developers.buffer.com/reference.html#type/ContentItemId)!
The content item whose channel-less draft is replaced.
draft : [DraftContentInput](https://developers.buffer.com/reference.html#type/DraftContentInput)!
The new draft content. Replaces the current draft in full.
tagIds : [[TagId](https://developers.buffer.com/reference.html#type/TagId)!]
Tags to apply to this content item. Omit to keep the current tags. An empty list or null removes them all.
targetDate : [DateTime](https://developers.buffer.com/reference.html#type/DateTime)
Date indicating when this piece of content should go out. This is a planning aid only and does not schedule any posts. Omit to preserve the existing target date. Null clears it.
INPUT ⚠️ Experimental
# UpdateContentItemInput
Input for updateContentItem. Only the fields provided are changed. Omitted fields keep their current value.
## Fields 3
id : [ContentItemId](https://developers.buffer.com/reference.html#type/ContentItemId)!
The content item to update.
targetDate : [DateTime](https://developers.buffer.com/reference.html#type/DateTime)
Omit to preserve the existing target date. Null clears it.
title : String
Omit to preserve the existing title. Null clears it.
INPUT
# UpdatePostTemplateInput
Input for an end user updating a post template. Buffer-curated taxonomy fields are ignored; setting them is only available to official Buffer clients.
## Fields 6
id : [PostTemplateId](https://developers.buffer.com/reference.html#type/PostTemplateId)! 🧪 Preview
The ID of the template to update.
body : String 🧪 Preview
The main content body of the template, may contain {{placeholders}}.
description : String 🧪 Preview
A short user-facing description of the template.
emoji : String 🧪 Preview
The emoji associated with the template.
title : String 🧪 Preview
The title of the template.
visibility : [PostTemplateVisibility](https://developers.buffer.com/reference.html#type/PostTemplateVisibility) 🧪 Preview
`public` is rejected — it is only available to official Buffer clients.
INPUT ⚠️ Experimental
# UpdateSnippetInput
Input for the updateSnippet mutation. Both name and text are replaced.
## Fields 4
id : [SnippetId](https://developers.buffer.com/reference.html#type/SnippetId)!
The snippet to update.
name : String!
The new display name of the snippet.
organizationId : [OrganizationId](https://developers.buffer.com/reference.html#type/OrganizationId)!
The organization that owns the snippet.
text : String!
The new hashtags, as the text that is inserted into a post.
INPUT ⚠️ Experimental
# UpdateTagInput
Input for updating a tag.
## Fields 2
id : [TagId](https://developers.buffer.com/reference.html#type/TagId)!
The tag to update. Its organization is taken from the tag itself, and the caller must be an administrator of that organization.
tag : [TagToUpdateInput](https://developers.buffer.com/reference.html#type/TagToUpdateInput)!
The name and color to set on the tag.
INPUT
# UserTagInput
User tag in the image
## Fields 3
handle : String!
The handle (username) of the account to tag, without the leading @.
x : Float!
Horizontal position of the tag as a normalized decimal float between 0.0 and 1.0 - the fraction of the image width from the left edge (0.5 is the horizontal center). Pass a number, not a string, and do not use pixel coordinates; to convert, divide the pixel X by the image width.
y : Float!
Vertical position of the tag as a normalized decimal float between 0.0 and 1.0 - the fraction of the image height from the top edge (0.5 is the vertical center). Pass a number, not a string, and do not use pixel coordinates; to convert, divide the pixel Y by the image height.
INPUT
# VideoAssetInput
Video asset
## Fields 3
metadata : [VideoMetadataInput](https://developers.buffer.com/reference.html#type/VideoMetadataInput)
Video specific metadata
thumbnailUrl : String
Do not use: social networks do not accept custom video thumbnail images, and the API rejects video assets that set this field. To choose the video thumbnail, set `metadata.thumbnailOffset` to select a frame from the video (supported for Instagram, TikTok, and Pinterest only).
url : String!
URL to the file source
INPUT
# VideoMetadataInput
Video metadata
## Fields 2
thumbnailOffset : Int
Offset of the thumbnail chosen for the video, in ms
title : String
Video title
INPUT
# YoutubePostMetadataInput
Youtube post metadata
## Fields 8
categoryId : String
Youtube Category ID, one ID of this list: ID: 1 -> Film & Animation ID: 2 -> Autos & Vehicles ID: 10 -> Music ID: 15 -> Pets & Animals ID: 17 -> Sports ID: 19 -> Travel & Events ID: 20 -> Gaming ID: 22 -> People & Blogs ID: 23 -> Comedy ID: 24 -> Entertainment ID: 25 -> News & Politics ID: 26 -> Howto & Style ID: 27 -> Education ID: 28 -> Science & Technology ID: 29 -> Nonprofits & Activism
Required on create; optional on edit (omitted preserves existing value).
embeddable : Boolean
Indicates whether the video allows embedding (default: true)
isAiGenerated : Boolean
Whether the post discloses AI-generated content
license : [YoutubeLicense](https://developers.buffer.com/reference.html#type/YoutubeLicense)
Video license (default: youtube)
madeForKids : Boolean
Indicates whether the video is suitable for kids (default: false)
notifySubscribers : Boolean
Indicates whether to notify subscribers on publish video (default: true)
privacy : [YoutubePrivacy](https://developers.buffer.com/reference.html#type/YoutubePrivacy)
Privacy setting for post (default: public)
title : String
Title of the Youtube post. Required on create; optional on edit (omitted preserves existing value).
ENUM ⚠️ Experimental
# AiFeature
AI features supported for an engagement type. Grows additively.
## Values 2
insights 
suggestions 
ENUM
# AnnotationType
List of possible types for an annotation
## Values 11
annotation 
bold 
bulletedListItem 
cashtag 
hashtag 
heading 
italic 
mention 
orderedListItem 
strikethrough 
url 
ENUM
# AssetType
Asset types
## Values 3
document 
image 
video 
ENUM ⚠️ Experimental
# AuthorizationStatus
Represents the authorization evaluation result for a feature.
## Values 5
needsRefresh  Authorization exists but requires token refresh 
needsUpgrade  The client version is below the minimum required to access this feature. The client should prompt the user to upgrade. 
notEnoughData  Insufficient data to determine authorization state. Typically indicates missing scopes or webhook metadata. 
notEnoughRights  The connected platform user's role/permissions are insufficient for this feature, so reconnecting with the same user cannot fix it. Clients should prompt the user to contact an administrator of the platform account (or have one connect the channel) instead of offering a reconnect. 
ok  Authorization is valid and the feature can be used. 
ENUM
# ChannelAction
List of possible actions that can be performed on a Channel
## Values 23
approvePosts 
backfillChannel 
exportInsights 
interactWithTakeaways 
manageCapabilities 
manageChannelSettings 
manageComments 
manageDms 
manageIntegrations 
managePostingSchedule 
manageUpdates 
publishStartPage 
readUpdates 
reconnectChannel 
removeChannel 
scheduleUpdates 
viewCapabilities 
viewChannel 
viewComments 
viewDms 
viewInsights 
viewPublish 
viewUpdates  Deprecated: Renamed to `viewPublish`. Still emitted for backward-compat with clients that gate on `viewUpdates`; use `viewPublish` to gate the Publish UI or `readUpdates` to gate reading post data. Will be removed once no client reads it.
ENUM
# ChannelType
Channel is a representation of a social media account or page that can be connected to Buffer.
## Values 6
account 
business 
channel 
group 
page 
profile 
ENUM ⚠️ Experimental
# ConfigurationContentType
The kinds of content a channel can compose. Grows additively.
## Values 4
comment 
post 
reel 
story 
ENUM
# ConnectedAppCategory
The category of a connected app.
## Values 1
mcp  An MCP client connection. 
ENUM ⚠️ Experimental
# ContentItemAction
Actions the calling actor can take on a `ContentItem`. The server computes this set from the same rules the content item mutations enforce. A client reads it to drive UI affordances instead of deriving the rules itself.
The set carries an action only when a client can offer it on this one item. An action whose answer is the same for every item in a response drives no affordance, so it stays out. Read access is one of those: the API returns only a content item the actor may read.
## Values 2
deleteContentItem  The actor can delete this content item. An item that holds channel-specific posts gets a second check. The mutation checks each post, so a delete can still fail. 
updateContentItem  The actor can change this content item's title and target date. The actor can also change the tags and the draft text while the item holds a channel-less draft. 
ENUM ⚠️ Experimental
# ContentItemSortableKey
Field to sort content items by.
## Values 2
targetDate  Sort by the content item's target date, the date it is planned for. Content items with no target date sort first in ascending order. 
createdAt  Sort by the date the content item was created. 
ENUM ⚠️ Experimental
# ContentItemStatus
The status of a content item's body.
## Values 2
draftContent  The content item holds a channel-less draft. 
postContent  The content item holds channel-specific posts. 
ENUM ⚠️ Experimental
# ContentProperty
A property a content type can carry. Support is expressed by inclusion in `supportedProperties` — there are no exclusion lists. Grows additively.
## Values 11
board 
document 
firstComment 
gif 
image 
imageAltText 
linkAttachment 
retweetAttachment 
text 
thread 
video 
ENUM
# DateTimePresence
Presence filter for nullable date fields. When filtering the same field, absent dates cannot also match a date comparator range.
## Values 2
absent  Include results where the date field is missing or null 
present  Include results where the date field exists and is not null 
ENUM
# DayOfWeek
Day of the week.
## Values 7
fri 
mon 
sat 
sun 
thu 
tue 
wed 
ENUM ⚠️ Experimental
# EngagementType
Discriminator used in inputs/filters to scope a query to specific types.
## Values 3
comment  Fetch comments (direct replies to Buffer-managed posts). 
directMessage  Direct messages (private conversations between the account and another user). 
mention  Fetch mentions (references to the account across the network). 
ENUM ⚠️ Experimental
# Feature
A capability a channel can expose, spanning every domain. The shared key for per-channel `authorizationStatus`. Grows additively.
## Values 6
comment 
directMessage 
engagementReaction 
insights 
mention 
posting 
ENUM
# GoogleBusinessPostActionType
List of possible types for GBP cta
## Values 7
book 
call 
learn_more 
none 
order 
shop 
signup 
ENUM
# IdeaGroupMembership
Named buckets for filtering ideas by their group membership.
## Values 2
grouped  Only ideas that are assigned to a group. 
ungrouped  Only ideas that are not assigned to any group. 
ENUM ⚠️ Experimental
# InstagramAudioType
Instagram audio catalog type from Meta's Audio API.
## Values 2
music  Licensed music from Meta's audio catalog. 
originalSound  Audio created by an Instagram account. 
ENUM ⚠️ Experimental
# MediaFormat
Media formats a `FormatRule` can allow-list. Grows additively.
## Values 7
gif 
jpeg 
mov 
mp4 
pdf 
png 
webm 
ENUM
# MediaType
The type of media attached to a post
## Values 6
image 
gif 
video 
link 
document 
unsupported 
ENUM
# NoteAction
List of possible actions that can be performed on a note
## Values 3
deleteNote  The user can delete the note. 
reactToNote  The user can add or remove their emoji reactions on the note. 
updateNote  The user can update the note. 
ENUM
# NoteType
The type of a note.
## Values 3
aiGenerated  A note that was generated by our AI system. 
bufferGenerated  A note that was generated by our internal system. Can be used for approval flows notifications or other automated processes. 
userGenerated  A note that was manually written by a user. 
ENUM
# NotificationStatus
List of possible statuses for a notification
## Values 2
markedAsPublished 
notified 
ENUM
# PostAction
List of possible actions that can be performed on a Post
## Values 22
addPostNote 
addPostToQueue 
approvePost 
cancelPostRecurrence 
copyPostLink 
createPostRecurrence 
deletePost 
duplicatePost 
editPostRecurrence 
movePostToDraft 
publishPostNext 
publishPostNow 
rejectPost 
removePostScheduledTime 
requestPostApproval 
revertPostApprovalRequest 
sharePostLink 
updatePost 
updatePostSchedule 
updatePostTags 
updateShopGridLink 
viewPost 
ENUM
# PostApprovalChange
A change to a post's approval state, for a post that is already a draft.
## Values 2
request  Submit the draft for approval. 
revert  Withdraw a pending approval request, returning the post to a plain draft. 
ENUM
# PostingGoalStatus
PostingGoalStatus is used to track the status of a posting goal.
## Values 3
AtRisk 
Hit 
OnTrack 
ENUM
# PostMetricType
List of possible metrics available for a Post.
Values fall into three groups:
  * **Cross-network normalized** (reactions, comments, shares, reposts, reach, impressions, views, clicks, engagementRate): Used wherever a concept maps cleanly across networks. Per-network adapters normalize their native names (e.g., Instagram `likes` → `reactions`, Twitter `retweets` → `reposts`).
  * **Network-specific** (saves, follows, quotes, viewers, totalTimeWatched, averageTimeWatched, likes, freeSubscriptions, paidSubscriptions): Real metrics that don't have a cross-network equivalent. `likes` is intentionally distinct from `reactions` on Facebook — Facebook's Graph API surfaces them separately. `freeSubscriptions` and `paidSubscriptions` are Substack's per-Note subscription attribution; no other network reports it.
  * **Aggregation-only** (postCount): Meaningful only on aggregate endpoints; never emitted per-post.


Deprecated values are pre-normalization legacy or tied to features being removed. They're kept in the enum for backwards compatibility until clients migrate.
## Values 26
averageTimeWatched  Average time watched, in seconds, for video-style posts (TikTok, Instagram Reels). 
clicks  How many times people clicked on your post. 
comments  The count of comments and replies on your post. Unified across networks (Threads `replies` maps here). 
engagementRate  The percentage of people who interacted with your post compared to how many saw it. Unit: percentage. 
favorites  Deprecated: not emitted by any per-network definition. Use `reactions` instead — Twitter and Mastodon favorites normalize into `reactions`. Will be removed on 2026-12-01. Deprecated: Not emitted by any per-network definition; use `reactions` instead. Will be removed on 2026-12-01.
follows  The number of new followers gained from this post (Instagram). 
freeSubscriptions ⚠️ Experimental The number of free subscriptions Substack attributes to this Note. 
impressions  How many times your post was shown on screen. May include multiple views by the same person — useful for spotting how often the content gets surfaced. 
likes  The Like-reaction subcount on Facebook. Distinct from `reactions` (which is the total of all reaction types — Like, Love, Care, Haha, Wow, Sad, Angry); Facebook's Graph API reports them separately and we mirror that. 
link_clicks  Deprecated: StartPage link-clicks metric. StartPage is being deprecated as a product. Will be removed on 2026-12-01. Deprecated: StartPage is being deprecated as a product. Will be removed on 2026-12-01.
other  Deprecated catch-all from pre-normalization. Never emitted. Will be removed on 2026-12-01. Deprecated: Catch-all from pre-normalization; never emitted. Will be removed on 2026-12-01.
paidSubscriptions ⚠️ Experimental The number of paid subscriptions Substack attributes to this Note. 
postCount  The count of posts included in an aggregated response. Only meaningful on aggregate endpoints — never emitted per-post. 
quotes  How many times your post was quoted (Threads). 
reach  The number of unique people who saw your post. 
reactions  How many people reacted to your post. Unified across networks: Instagram/Twitter `likes`, Mastodon `favorites`, etc. all map to this value. 
reblogs  Deprecated: not emitted by any per-network definition. Use `reposts` instead — Mastodon reblogs normalize into `reposts`. Will be removed on 2026-12-01. Deprecated: Not emitted by any per-network definition; use `reposts` instead. Will be removed on 2026-12-01.
repins  Deprecated: not emitted by any per-network definition. Pre-normalization legacy from the Pinterest era. Will be removed on 2026-12-01. Deprecated: Not emitted by any per-network definition. Will be removed on 2026-12-01.
replies  Deprecated: not emitted by any per-network definition. Use `comments` instead — replies are normalized into `comments` on the networks that distinguish them (Threads). Will be removed on 2026-12-01. Deprecated: Not emitted by any per-network definition; use `comments` instead. Will be removed on 2026-12-01.
reposts  How many times your post was reposted by others. Twitter `retweets`, Mastodon `reblogs`, Threads `reposts` all normalize to this value. 
retweets  Deprecated: not emitted by any per-network definition. Use `reposts` instead — Twitter retweets normalize into `reposts`. Will be removed on 2026-12-01. Deprecated: Not emitted by any per-network definition; use `reposts` instead. Will be removed on 2026-12-01.
saves  How many times people saved your post (Instagram, Pinterest). A strong signal that the content is worth revisiting. 
shares  How many times your post was shared or forwarded by others. 
totalTimeWatched  Total time watched, in minutes, for video-style posts (LinkedIn, TikTok, Instagram Reels). 
viewers  Unique viewer count for video-style posts (LinkedIn). 
views  How many times your post was viewed. Used for video-style posts and on networks that report views distinctly from impressions. 
ENUM
# PostMetricUnit
The unit representing the value of a PostMetric.
## Values 2
count  An integer count (e.g. number of reactions, impressions, reach). 
percentage  A percentage value between 0 and 100 (e.g. engagement rate). 
ENUM
# PostSortableKey
Key of collection to use for sorting
## Values 2
dueAt  Sort by the post's dueAt field. Due at is the date when the post is scheduled to be published. 
createdAt  Sort by the post's createdAt field. Created at is the date when the post was created. 
ENUM
# PostStatus
List of possible statuses for a Post
## Values 6
draft 
error 
needs_approval 
scheduled 
sending 
sent 
ENUM 🧪 Preview
# PostTemplateVisibility
The visibility level of a post template. `public` is reserved for Buffer-curated templates; setting it is only available to official Buffer clients.
## Values 3
internal  All members of the template's organization can access this template. 
private  Only the creator can access this template. 
public  Anyone across all organizations can access this template. Reserved for Buffer-curated templates — `createPostTemplate` and `updatePostTemplate` reject this value; setting it is only available to official Buffer clients. It appears in read results. 
ENUM
# PostType
List of possible types for a Post. Some services may have different types (e.g., Instagram has story, reel, post but Twitter has only post)
## Values 10
carousel 
event 
ghost_post 
offer 
post 
reel 
short 
story 
thread 
whats_new 
ENUM
# PostTypeFacebook
List of specific post types available for Facebook
## Values 3
post 
reel 
story 
ENUM
# PostTypeGoogleBusiness
List of specific post types available for Google Business profiles
## Values 3
event 
offer 
whats_new 
ENUM
# PostVia
List of possible ways to create a Post
## Values 3
api 
buffer 
network 
ENUM
# Product
Buffer products, buffer is used as all products
## Values 6
analyze 
buffer 
comments 
engage 
publish 
startPage 
ENUM ⚠️ Experimental
# QueuePosition
Target position within a channel's queue that a post can be moved to.
## Values 2
bottom  Move the post to the bottom of the queue, taking the last slot. 
top  Move the post to the top of the queue, taking the next available slot. 
ENUM ⚠️ Experimental
# ReactionIcon
Standard reaction icon set used by `IconVisual`. Grows additively.
## Values 4
heart 
smilingFace  🙂 (U+1F642). 
star 
thumbsUp 
ENUM ⚠️ Experimental
# ReactionType
Types of reactions that can be applied to a comment.
## Values 7
celebrate  A celebrate reaction. Supported only for LinkedIn comments. 
external  An external reaction on the comment, using an external link. 
funny  A funny reaction. Supported only for LinkedIn comments. 
insightful  An insightful reaction. Supported only for LinkedIn comments. 
like  A like reaction on the comment. 
love  A love reaction. Supported only for LinkedIn comments. 
support  A support reaction. Supported only for LinkedIn comments. 
ENUM
# ScheduleOption
## Values 4
Queue 
Prioritize 
FixedTime 
Now 
ENUM
# SchedulingType
Indicates whether the post was scheduled for notification publishing or automatic publishing
## Values 2
automatic  Buffer's publishing workers send the post, with nobody having to act 
notification  Buffer reminds someone to publish the post by hand 
ENUM
# Service
The list of services that can be authorized.
## Values 14
bluesky 
facebook 
googlebusiness 
instagram 
linkedin 
mastodon 
pinterest 
startPage 
substack 
threads 
tiktok 
twitter 
whatsapp 
youtube 
ENUM
# ShareMode
How the post is being scheduled.
## Values 4
addToQueue 
customScheduled 
shareNext 
shareNow 
ENUM
# SortDirection
Direction to sort the results by.
## Values 2
asc  Sort records in ascending order. 
desc  Sort records in descending order. 
ENUM ⚠️ Experimental
# SyncDataMechanism
How items of an engagement type are pulled / pushed. `realTime` covers push (webhook / firehose); `polling` is pull.
## Values 2
polling 
realTime 
ENUM
# TagColorName
Stable Buffer identifiers for the supported tag color palette. Clients map these values to platform- and theme-specific presentation. Values ending in `Light` are lighter palette variants, not UI theme modes.
## Values 18
blue  The standard blue palette color. 
blueLight  The lighter blue palette color. 
gray  The standard gray palette color. 
grayLight  The lighter gray palette color. 
green  The standard green palette color. 
greenLight  The lighter green palette color. 
orange  The standard orange palette color. 
orangeLight  The lighter orange palette color. 
pink  The standard pink palette color. 
pinkLight  The lighter pink palette color. 
purple  The standard purple palette color. 
purpleLight  The lighter purple palette color. 
red  The standard red palette color. 
redLight  The lighter red palette color. 
teal  The standard teal palette color. 
tealLight  The lighter teal palette color. 
yellow  The standard yellow palette color. 
yellowLight  The lighter yellow palette color. 
ENUM
# YoutubeLicense
List of license types
## Values 2
creativeCommon 
youtube 
ENUM
# YoutubePrivacy
List of privacy types
## Values 3
private 
public 
unlisted 
INTERFACE
# Asset
Asset interface with common fields
## Fields 5
id : ID
The ID of the asset in the database
mimeType : String!
The MIME type of the asset
source : String!
URL to the file source
thumbnail : String!
URL to the static thumbnail of the asset
type : [AssetType](https://developers.buffer.com/reference.html#type/AssetType)!
The type of the asset
INTERFACE
# CommonPostMetadata
Common properties for all post metadata types
## Fields 2
annotations : [[Annotation](https://developers.buffer.com/reference.html#type/Annotation)!]!
Annotations representing entities in the text
type : [PostType](https://developers.buffer.com/reference.html#type/PostType)!
The channel-specific type of the post, eg, post, story, reel for Instagram
INTERFACE
# MutationError
Base Mutation Error type
## Fields 1
message : String!
Error message
INTERFACE
# MutationSuccess
Base Mutation Success type Used when we have a success response with no data, we return this type with empty string
## Fields 1
_empty : String!
The value is alwaus an empty string '' Note: GraphQL doesn't allow types with no fields, so we have to add this field
INTERFACE
# ScrapedLink
Link data for link preview
## Fields 3
text : String!
Description for the scraped link
thumbnails : [String!]!
Thumbnails of media available in the link
url : String!
URL that the link asset has been built from
INTERFACE
# ThreadedPostMetadata
Common properties for all posts that support threaded replies. See ThreadedPost for more details.
## Fields 2
thread : [[ThreadedPost](https://developers.buffer.com/reference.html#type/ThreadedPost)!]!
The list of threaded posts (not paginated)
threadCount : Int!
The number of threaded posts
INTERFACE ⚠️ Experimental
# ValidationRule
A validation rule constraining how a content property may be used. Each concrete rule carries only the fields it needs; new constraint kinds are additive (a new type implementing this interface). Clients switch on `__typename`.
## Fields 1
property : [ContentProperty](https://developers.buffer.com/reference.html#type/ContentProperty)!
The content property this rule constrains.
UNION ⚠️ Experimental
# AddPostToContentItemPayload
All possible responses for addPostToContentItem.
## Possible Types 2
[AddPostToContentItemSuccess](https://developers.buffer.com/reference.html#type/AddPostToContentItemSuccess)[VoidMutationError](https://developers.buffer.com/reference.html#type/VoidMutationError)
UNION
# ChannelMetadata
Metadata or settings about the channel depending on the service type
## Possible Types 11
[InstagramMetadata](https://developers.buffer.com/reference.html#type/InstagramMetadata)[TiktokMetadata](https://developers.buffer.com/reference.html#type/TiktokMetadata)[YoutubeMetadata](https://developers.buffer.com/reference.html#type/YoutubeMetadata)[PinterestMetadata](https://developers.buffer.com/reference.html#type/PinterestMetadata)[MastodonMetadata](https://developers.buffer.com/reference.html#type/MastodonMetadata)[BlueskyMetadata](https://developers.buffer.com/reference.html#type/BlueskyMetadata)[GoogleBusinessMetadata](https://developers.buffer.com/reference.html#type/GoogleBusinessMetadata)[FacebookMetadata](https://developers.buffer.com/reference.html#type/FacebookMetadata)[TwitterMetadata](https://developers.buffer.com/reference.html#type/TwitterMetadata)[LinkedInMetadata](https://developers.buffer.com/reference.html#type/LinkedInMetadata)[WhatsAppMetadata](https://developers.buffer.com/reference.html#type/WhatsAppMetadata)
UNION ⚠️ Experimental
# ContentItemBody
A content item's content: its channel-less draft while it is a draft, or its channel-specific posts once it holds posts. The body shows one or the other, never both, although a content item keeps its draft after it becomes posts.
## Possible Types 2
[DraftContent](https://developers.buffer.com/reference.html#type/DraftContent)[PostContent](https://developers.buffer.com/reference.html#type/PostContent)
UNION ⚠️ Experimental
# CreateContentItemDraftPayload
All possible responses for createContentItemDraft.
## Possible Types 2
[CreateContentItemDraftSuccess](https://developers.buffer.com/reference.html#type/CreateContentItemDraftSuccess)[CreateContentItemDraftFailure](https://developers.buffer.com/reference.html#type/CreateContentItemDraftFailure)
UNION ⚠️ Experimental
# CreateContentItemError
A recoverable error that prevented a content item from being created. Variant errors identify the specific channel they apply to; the others apply to the request as a whole.
## Possible Types 6
[InvalidInputError](https://developers.buffer.com/reference.html#type/InvalidInputError)[NotFoundError](https://developers.buffer.com/reference.html#type/NotFoundError)[LimitReachedError](https://developers.buffer.com/reference.html#type/LimitReachedError)[CreateContentItemVariantInvalidInputError](https://developers.buffer.com/reference.html#type/CreateContentItemVariantInvalidInputError)[CreateContentItemVariantLimitReachedError](https://developers.buffer.com/reference.html#type/CreateContentItemVariantLimitReachedError)[CreateContentItemVariantNotFoundError](https://developers.buffer.com/reference.html#type/CreateContentItemVariantNotFoundError)
UNION ⚠️ Experimental
# CreateContentItemPayload
All possible responses for createContentItem.
## Possible Types 2
[CreateContentItemSuccess](https://developers.buffer.com/reference.html#type/CreateContentItemSuccess)[CreateContentItemFailure](https://developers.buffer.com/reference.html#type/CreateContentItemFailure)
UNION
# CreateIdeaPayload
createIdea response (including errors)
## Possible Types 6
[Idea](https://developers.buffer.com/reference.html#type/Idea)[IdeaResponse](https://developers.buffer.com/reference.html#type/IdeaResponse)[InvalidInputError](https://developers.buffer.com/reference.html#type/InvalidInputError)[UnauthorizedError](https://developers.buffer.com/reference.html#type/UnauthorizedError)[UnexpectedError](https://developers.buffer.com/reference.html#type/UnexpectedError)[LimitReachedError](https://developers.buffer.com/reference.html#type/LimitReachedError)
UNION 🧪 Preview
# CreatePostTemplatePayload
Result of an end user creating a post template.
## Possible Types 2
[CreatePostTemplateSuccess](https://developers.buffer.com/reference.html#type/CreatePostTemplateSuccess)[VoidMutationError](https://developers.buffer.com/reference.html#type/VoidMutationError)
UNION ⚠️ Experimental
# CreateSnippetPayload
All possible responses for createSnippet. VoidMutationError reports an empty or too long name or text.
## Possible Types 2
[CreateSnippetSuccess](https://developers.buffer.com/reference.html#type/CreateSnippetSuccess)[VoidMutationError](https://developers.buffer.com/reference.html#type/VoidMutationError)
UNION ⚠️ Experimental
# CreateTagPayload
The result of `createTag`: the tag that was created, or the reason it was refused.
**Members on the way out.** `RestProxyError`, `NotFoundError`, `UnauthorizedError` and `UnexpectedError` are being removed from this union. No new operation should select them by name.
`RestProxyError` is never returned. The other three describe situations a caller cannot correct — the tag not existing, the caller not being permitted, an unexpected fault — and will be reported in the response's top-level `errors` array instead of here.
Select `... on MutationError { message }` rather than naming concrete error types. Every error member implements that interface, so the selection keeps working across the change.
## Possible Types 8
[TagActionSuccess](https://developers.buffer.com/reference.html#type/TagActionSuccess)[InvalidInputError](https://developers.buffer.com/reference.html#type/InvalidInputError)[DuplicateError](https://developers.buffer.com/reference.html#type/DuplicateError)[LimitReachedError](https://developers.buffer.com/reference.html#type/LimitReachedError)[NotFoundError](https://developers.buffer.com/reference.html#type/NotFoundError)[UnauthorizedError](https://developers.buffer.com/reference.html#type/UnauthorizedError)[UnexpectedError](https://developers.buffer.com/reference.html#type/UnexpectedError)[RestProxyError](https://developers.buffer.com/reference.html#type/RestProxyError)
UNION ⚠️ Experimental
# DeleteContentItemPayload
All possible responses for deleteContentItem.
## Possible Types 2
[EmptySuccess](https://developers.buffer.com/reference.html#type/EmptySuccess)[DeleteContentItemFailure](https://developers.buffer.com/reference.html#type/DeleteContentItemFailure)
UNION
# DeletePostPayload
All possible response types for the deletePost mutation.
## Possible Types 2
[DeletePostSuccess](https://developers.buffer.com/reference.html#type/DeletePostSuccess)[VoidMutationError](https://developers.buffer.com/reference.html#type/VoidMutationError)
UNION 🧪 Preview
# DeletePostTemplatePayload
Result of an end user deleting a post template.
## Possible Types 2
[EmptySuccess](https://developers.buffer.com/reference.html#type/EmptySuccess)[VoidMutationError](https://developers.buffer.com/reference.html#type/VoidMutationError)
UNION ⚠️ Experimental
# DeleteSnippetPayload
All possible responses for deleteSnippet.
## Possible Types 2
[DeleteSnippetSuccess](https://developers.buffer.com/reference.html#type/DeleteSnippetSuccess)[VoidMutationError](https://developers.buffer.com/reference.html#type/VoidMutationError)
UNION ⚠️ Experimental
# DeleteTagPayload
The result of `deleteTag`: the id of the deleted tag, or the reason the delete was refused.
**Members on the way out.** `RestProxyError`, `NotFoundError`, `UnauthorizedError` and `UnexpectedError` are being removed from this union. No new operation should select them by name.
`RestProxyError` is never returned. The other three describe situations a caller cannot correct — the tag not existing, the caller not being permitted, an unexpected fault — and will be reported in the response's top-level `errors` array instead of here.
Select `... on MutationError { message }` rather than naming concrete error types. Every error member implements that interface, so the selection keeps working across the change.
## Possible Types 6
[DeleteTagActionSuccess](https://developers.buffer.com/reference.html#type/DeleteTagActionSuccess)[InvalidInputError](https://developers.buffer.com/reference.html#type/InvalidInputError)[NotFoundError](https://developers.buffer.com/reference.html#type/NotFoundError)[UnauthorizedError](https://developers.buffer.com/reference.html#type/UnauthorizedError)[UnexpectedError](https://developers.buffer.com/reference.html#type/UnexpectedError)[RestProxyError](https://developers.buffer.com/reference.html#type/RestProxyError)
UNION ⚠️ Experimental
# EngagementMetadata
Network-specific engagement metadata. Single-member union for now; grows additively as more networks contribute their own shape.
## Possible Types 1
[GoogleBusinessEngagementMetadata](https://developers.buffer.com/reference.html#type/GoogleBusinessEngagementMetadata)
UNION
# GoogleBusinessPostDetails
GoogleBusiness Metadata details
## Possible Types 3
[GoogleBusinessWhatsNewMetaData](https://developers.buffer.com/reference.html#type/GoogleBusinessWhatsNewMetaData)[GoogleBusinessOfferMetaData](https://developers.buffer.com/reference.html#type/GoogleBusinessOfferMetaData)[GoogleBusinessEventMetaData](https://developers.buffer.com/reference.html#type/GoogleBusinessEventMetaData)
UNION ⚠️ Experimental
# InstagramAudioCatalogPayload
Combined Instagram audio results or a request to refresh the channel.
## Possible Types 2
[InstagramAudioCatalogSuccess](https://developers.buffer.com/reference.html#type/InstagramAudioCatalogSuccess)[ChannelRefreshRequired](https://developers.buffer.com/reference.html#type/ChannelRefreshRequired)
UNION ⚠️ Experimental
# InstagramAudioPayload
Payload returned when refreshing Instagram audio metadata
## Possible Types 2
[InstagramAudioSuccess](https://developers.buffer.com/reference.html#type/InstagramAudioSuccess)[ChannelRefreshRequired](https://developers.buffer.com/reference.html#type/ChannelRefreshRequired)
UNION ⚠️ Experimental
# MovePostInQueuePayload
All possible response types that can be returned by movePostInQueue mutation.
## Possible Types 2
[PostActionSuccess](https://developers.buffer.com/reference.html#type/PostActionSuccess)[VoidMutationError](https://developers.buffer.com/reference.html#type/VoidMutationError)
UNION
# PostActionPayload
Create post's request response payload.
## Possible Types 7
[PostActionSuccess](https://developers.buffer.com/reference.html#type/PostActionSuccess)[NotFoundError](https://developers.buffer.com/reference.html#type/NotFoundError)[UnauthorizedError](https://developers.buffer.com/reference.html#type/UnauthorizedError)[UnexpectedError](https://developers.buffer.com/reference.html#type/UnexpectedError)[RestProxyError](https://developers.buffer.com/reference.html#type/RestProxyError)[LimitReachedError](https://developers.buffer.com/reference.html#type/LimitReachedError)[InvalidInputError](https://developers.buffer.com/reference.html#type/InvalidInputError)
UNION
# PostMetadata
Post metadata union type. Contains all possible types of post metadata.
## Possible Types 12
[InstagramPostMetadata](https://developers.buffer.com/reference.html#type/InstagramPostMetadata)[FacebookPostMetadata](https://developers.buffer.com/reference.html#type/FacebookPostMetadata)[LinkedInPostMetadata](https://developers.buffer.com/reference.html#type/LinkedInPostMetadata)[TwitterPostMetadata](https://developers.buffer.com/reference.html#type/TwitterPostMetadata)[PinterestPostMetadata](https://developers.buffer.com/reference.html#type/PinterestPostMetadata)[GoogleBusinessPostMetadata](https://developers.buffer.com/reference.html#type/GoogleBusinessPostMetadata)[YoutubePostMetadata](https://developers.buffer.com/reference.html#type/YoutubePostMetadata)[MastodonPostMetadata](https://developers.buffer.com/reference.html#type/MastodonPostMetadata)[TiktokPostMetadata](https://developers.buffer.com/reference.html#type/TiktokPostMetadata)[ThreadsPostMetadata](https://developers.buffer.com/reference.html#type/ThreadsPostMetadata)[BlueskyPostMetadata](https://developers.buffer.com/reference.html#type/BlueskyPostMetadata)[SubstackPostMetadata](https://developers.buffer.com/reference.html#type/SubstackPostMetadata)
UNION ⚠️ Experimental
# PromoteContentItemDraftToPostsError
A recoverable error that prevented a content item draft from being promoted. Post errors identify the specific channel they apply to; the others apply to the request as a whole.
## Possible Types 5
[ContentItemStateError](https://developers.buffer.com/reference.html#type/ContentItemStateError)[InvalidInputError](https://developers.buffer.com/reference.html#type/InvalidInputError)[PostChannelNotFoundError](https://developers.buffer.com/reference.html#type/PostChannelNotFoundError)[PostInvalidInputError](https://developers.buffer.com/reference.html#type/PostInvalidInputError)[PostLimitReachedError](https://developers.buffer.com/reference.html#type/PostLimitReachedError)
UNION ⚠️ Experimental
# PromoteContentItemDraftToPostsPayload
All possible responses for promoteContentItemDraftToPosts.
## Possible Types 2
[PromoteContentItemDraftToPostsSuccess](https://developers.buffer.com/reference.html#type/PromoteContentItemDraftToPostsSuccess)[PromoteContentItemDraftToPostsFailure](https://developers.buffer.com/reference.html#type/PromoteContentItemDraftToPostsFailure)
UNION ⚠️ Experimental
# ReactionVisual
How to render a reaction. The client switches on `__typename` purely as a render strategy (built-in icon vs network image) — never on the network or the reaction identity.
## Possible Types 2
[IconVisual](https://developers.buffer.com/reference.html#type/IconVisual)[ImageVisual](https://developers.buffer.com/reference.html#type/ImageVisual)
UNION ⚠️ Experimental
# RemovePostFromContentItemPayload
All possible responses for removePostFromContentItem.
## Possible Types 2
[RemovePostFromContentItemSuccess](https://developers.buffer.com/reference.html#type/RemovePostFromContentItemSuccess)[VoidMutationError](https://developers.buffer.com/reference.html#type/VoidMutationError)
UNION ⚠️ Experimental
# SearchInstagramAudioPayload
Payload returned when searching Instagram audio
## Possible Types 2
[SearchInstagramAudioSuccess](https://developers.buffer.com/reference.html#type/SearchInstagramAudioSuccess)[ChannelRefreshRequired](https://developers.buffer.com/reference.html#type/ChannelRefreshRequired)
UNION ⚠️ Experimental
# UpdateContentItemDraftError
A recoverable error that prevented a content item draft from being updated.
## Possible Types 2
[InvalidInputError](https://developers.buffer.com/reference.html#type/InvalidInputError)[ContentItemStateError](https://developers.buffer.com/reference.html#type/ContentItemStateError)
UNION ⚠️ Experimental
# UpdateContentItemDraftPayload
All possible responses for updateContentItemDraft.
## Possible Types 2
[UpdateContentItemDraftSuccess](https://developers.buffer.com/reference.html#type/UpdateContentItemDraftSuccess)[UpdateContentItemDraftFailure](https://developers.buffer.com/reference.html#type/UpdateContentItemDraftFailure)
UNION ⚠️ Experimental
# UpdateContentItemPayload
All possible responses for updateContentItem.
## Possible Types 2
[UpdateContentItemSuccess](https://developers.buffer.com/reference.html#type/UpdateContentItemSuccess)[UpdateContentItemFailure](https://developers.buffer.com/reference.html#type/UpdateContentItemFailure)
UNION 🧪 Preview
# UpdatePostTemplatePayload
Result of an end user updating a post template.
## Possible Types 2
[UpdatePostTemplateSuccess](https://developers.buffer.com/reference.html#type/UpdatePostTemplateSuccess)[VoidMutationError](https://developers.buffer.com/reference.html#type/VoidMutationError)
UNION ⚠️ Experimental
# UpdateSnippetPayload
All possible responses for updateSnippet. VoidMutationError reports an empty or too long name or text.
## Possible Types 2
[UpdateSnippetSuccess](https://developers.buffer.com/reference.html#type/UpdateSnippetSuccess)[VoidMutationError](https://developers.buffer.com/reference.html#type/VoidMutationError)
UNION ⚠️ Experimental
# UpdateTagPayload
The result of `updateTag`: the tag as it now stands, or the reason the edit was refused.
**Members on the way out.** `RestProxyError`, `NotFoundError`, `UnauthorizedError` and `UnexpectedError` are being removed from this union. No new operation should select them by name.
`RestProxyError` is never returned. The other three describe situations a caller cannot correct — the tag not existing, the caller not being permitted, an unexpected fault — and will be reported in the response's top-level `errors` array instead of here.
Select `... on MutationError { message }` rather than naming concrete error types. Every error member implements that interface, so the selection keeps working across the change.
## Possible Types 7
[TagActionSuccess](https://developers.buffer.com/reference.html#type/TagActionSuccess)[InvalidInputError](https://developers.buffer.com/reference.html#type/InvalidInputError)[DuplicateError](https://developers.buffer.com/reference.html#type/DuplicateError)[NotFoundError](https://developers.buffer.com/reference.html#type/NotFoundError)[UnauthorizedError](https://developers.buffer.com/reference.html#type/UnauthorizedError)[UnexpectedError](https://developers.buffer.com/reference.html#type/UnexpectedError)[RestProxyError](https://developers.buffer.com/reference.html#type/RestProxyError)
SCALAR
# AccountId
The `AccountId` scalar represents the ID of a Buffer Account
Identifies: [Account](https://developers.buffer.com/reference.html#type/Account)
SCALAR
# ChannelId
The `ChannelId` scalar represents the ID of a Buffer Channel
Identifies: [Channel](https://developers.buffer.com/reference.html#type/Channel)
SCALAR ⚠️ Experimental
# ContentItemId
A unique identifier for a content item.
Identifies: [ContentItem](https://developers.buffer.com/reference.html#type/ContentItem)
SCALAR
# DateTime
The `DateTime` scalar represents a date and time following the ISO 8601 standard.
SCALAR ⚠️ Experimental
# DraftContentId
A unique identifier for a channel-less draft's content.
Identifies: [DraftContent](https://developers.buffer.com/reference.html#type/DraftContent)
SCALAR
# DraftId
The `DraftId` scalar represents the ID of a Buffer Draft
SCALAR
# Email
The `Email` scalar represents a valid, normalized email address. Input is trimmed and lowercased before validation.
SCALAR
# IdeaId
The `IdeaId` scalar represents the ID of a Buffer Idea
Identifies: [Idea](https://developers.buffer.com/reference.html#type/Idea)
SCALAR
# InvitationId
The `InvitationId` scalar represents the ID of a pending team invitation
SCALAR
# NoteId
The `NoteId` scalar represents the ID of a Buffer Note
Identifies: [Note](https://developers.buffer.com/reference.html#type/Note)
SCALAR
# OrganizationId
The `OrganizationId` scalar represents the ID of a Buffer Organization
Identifies: [Organization](https://developers.buffer.com/reference.html#type/Organization)
SCALAR
# PostId
The `PostId` scalar represents the ID of a Buffer Post
Identifies: [Post](https://developers.buffer.com/reference.html#type/Post)
SCALAR
# PostTemplateId
The `PostTemplateId` scalar represents the ID of a Post Template.
Identifies: [PostTemplate](https://developers.buffer.com/reference.html#type/PostTemplate)
SCALAR
# SnippetId
The `SnippetId` scalar represents the ID of a Snippet.
Identifies: [Snippet](https://developers.buffer.com/reference.html#type/Snippet)
SCALAR
# TagId
The `TagId` scalar represents the ID of a Buffer Tag
Identifies: [Tag](https://developers.buffer.com/reference.html#type/Tag)
SCALAR
# URL
The `URL` scalar represents a valid URL
SCALAR
# Uuid
The `Uuid` scalar represents an RFC 4122 v4 UUID, e.g. `550e8400-e29b-41d4-a716-446655440000`.
Reference
[Account](https://developers.buffer.com/reference.html#account)
[QUERYaccount](https://developers.buffer.com/reference.html#field-account)[OUTPUTAccount](https://developers.buffer.com/reference.html#type/Account)[TYPEConnectedApp](https://developers.buffer.com/reference.html#type/ConnectedApp)[TYPEPreferences](https://developers.buffer.com/reference.html#type/Preferences)[ENUMConnectedAppCategory](https://developers.buffer.com/reference.html#type/ConnectedAppCategory)[ENUMScheduleOption](https://developers.buffer.com/reference.html#type/ScheduleOption)[SCALARAccountId](https://developers.buffer.com/reference.html#type/AccountId)[SCALARDateTime](https://developers.buffer.com/reference.html#type/DateTime)
[Channels](https://developers.buffer.com/reference.html#channels)
[QUERYchannel](https://developers.buffer.com/reference.html#field-channel)[QUERYchannels](https://developers.buffer.com/reference.html#field-channels)[TYPEBlueskyMetadata](https://developers.buffer.com/reference.html#type/BlueskyMetadata)[OUTPUTChannel](https://developers.buffer.com/reference.html#type/Channel)[TYPEChannelConfiguration](https://developers.buffer.com/reference.html#type/ChannelConfiguration)[TYPEChannelLinkShortening](https://developers.buffer.com/reference.html#type/ChannelLinkShortening)[TYPEChannelRefreshRequired](https://developers.buffer.com/reference.html#type/ChannelRefreshRequired)[TYPEContentConfiguration](https://developers.buffer.com/reference.html#type/ContentConfiguration)[TYPEEngagementSupportedReaction](https://developers.buffer.com/reference.html#type/EngagementSupportedReaction)[TYPEEngagementTypeConfiguration](https://developers.buffer.com/reference.html#type/EngagementTypeConfiguration)[TYPEFacebookMetadata](https://developers.buffer.com/reference.html#type/FacebookMetadata)[TYPEFeatureAuthorizationStatus](https://developers.buffer.com/reference.html#type/FeatureAuthorizationStatus)[TYPEForcedSyncConfiguration](https://developers.buffer.com/reference.html#type/ForcedSyncConfiguration)[TYPEForcedSyncRateLimit](https://developers.buffer.com/reference.html#type/ForcedSyncRateLimit)[TYPEGoogleBusinessEngagementMetadata](https://developers.buffer.com/reference.html#type/GoogleBusinessEngagementMetadata)[TYPEGoogleBusinessMetadata](https://developers.buffer.com/reference.html#type/GoogleBusinessMetadata)[TYPEIconVisual](https://developers.buffer.com/reference.html#type/IconVisual)[TYPEIdeaMedia](https://developers.buffer.com/reference.html#type/IdeaMedia)[TYPEIdeaMediaSource](https://developers.buffer.com/reference.html#type/IdeaMediaSource)[TYPEImageVisual](https://developers.buffer.com/reference.html#type/ImageVisual)[TYPELinkedInMetadata](https://developers.buffer.com/reference.html#type/LinkedInMetadata)[TYPELinkShorteningConfig](https://developers.buffer.com/reference.html#type/LinkShorteningConfig)[TYPELocationData](https://developers.buffer.com/reference.html#type/LocationData)[TYPEMastodonMetadata](https://developers.buffer.com/reference.html#type/MastodonMetadata)[TYPEMediaConfiguration](https://developers.buffer.com/reference.html#type/MediaConfiguration)[TYPEPinterestBoard](https://developers.buffer.com/reference.html#type/PinterestBoard)[TYPEPinterestMetadata](https://developers.buffer.com/reference.html#type/PinterestMetadata)[TYPEPostChannelNotFoundError](https://developers.buffer.com/reference.html#type/PostChannelNotFoundError)[TYPEReactionsConfiguration](https://developers.buffer.com/reference.html#type/ReactionsConfiguration)[TYPEReplyingConfiguration](https://developers.buffer.com/reference.html#type/ReplyingConfiguration)[TYPEScheduleV2](https://developers.buffer.com/reference.html#type/ScheduleV2)[TYPESyncDataConfiguration](https://developers.buffer.com/reference.html#type/SyncDataConfiguration)[TYPETiktokMetadata](https://developers.buffer.com/reference.html#type/TiktokMetadata)[TYPETwitterMetadata](https://developers.buffer.com/reference.html#type/TwitterMetadata)[TYPEWhatsAppMetadata](https://developers.buffer.com/reference.html#type/WhatsAppMetadata)[TYPEYoutubeMetadata](https://developers.buffer.com/reference.html#type/YoutubeMetadata)[INPUTChannelInput](https://developers.buffer.com/reference.html#type/ChannelInput)[INPUTChannelsFiltersInput](https://developers.buffer.com/reference.html#type/ChannelsFiltersInput)[INPUTChannelsInput](https://developers.buffer.com/reference.html#type/ChannelsInput)[INPUTIdeaMediaInput](https://developers.buffer.com/reference.html#type/IdeaMediaInput)[INPUTIdeaMediaSourceInput](https://developers.buffer.com/reference.html#type/IdeaMediaSourceInput)[TYPEValidationRule](https://developers.buffer.com/reference.html#type/ValidationRule)[TYPEChannelMetadata](https://developers.buffer.com/reference.html#type/ChannelMetadata)[TYPEEngagementMetadata](https://developers.buffer.com/reference.html#type/EngagementMetadata)[TYPEReactionVisual](https://developers.buffer.com/reference.html#type/ReactionVisual)[ENUMAiFeature](https://developers.buffer.com/reference.html#type/AiFeature)[ENUMAuthorizationStatus](https://developers.buffer.com/reference.html#type/AuthorizationStatus)[ENUMChannelAction](https://developers.buffer.com/reference.html#type/ChannelAction)[ENUMChannelType](https://developers.buffer.com/reference.html#type/ChannelType)[ENUMConfigurationContentType](https://developers.buffer.com/reference.html#type/ConfigurationContentType)[ENUMContentProperty](https://developers.buffer.com/reference.html#type/ContentProperty)[ENUMDayOfWeek](https://developers.buffer.com/reference.html#type/DayOfWeek)[ENUMEngagementType](https://developers.buffer.com/reference.html#type/EngagementType)[ENUMFeature](https://developers.buffer.com/reference.html#type/Feature)[ENUMMediaFormat](https://developers.buffer.com/reference.html#type/MediaFormat)[ENUMMediaType](https://developers.buffer.com/reference.html#type/MediaType)[ENUMProduct](https://developers.buffer.com/reference.html#type/Product)[ENUMReactionIcon](https://developers.buffer.com/reference.html#type/ReactionIcon)[ENUMReactionType](https://developers.buffer.com/reference.html#type/ReactionType)[ENUMService](https://developers.buffer.com/reference.html#type/Service)[ENUMSyncDataMechanism](https://developers.buffer.com/reference.html#type/SyncDataMechanism)[SCALARChannelId](https://developers.buffer.com/reference.html#type/ChannelId)
[Tags](https://developers.buffer.com/reference.html#tags)
[QUERYtag](https://developers.buffer.com/reference.html#field-tag)[QUERYtagsV2](https://developers.buffer.com/reference.html#field-tagsV2)[MUTATIONcreateTag](https://developers.buffer.com/reference.html#field-createTag)[MUTATIONdeleteTag](https://developers.buffer.com/reference.html#field-deleteTag)[MUTATIONupdateTag](https://developers.buffer.com/reference.html#field-updateTag)[OUTPUTTag](https://developers.buffer.com/reference.html#type/Tag)[TYPETagActionSuccess](https://developers.buffer.com/reference.html#type/TagActionSuccess)[TYPETagEdge](https://developers.buffer.com/reference.html#type/TagEdge)[OUTPUTTagsConnection](https://developers.buffer.com/reference.html#type/TagsConnection)[INPUTTagByIdInput](https://developers.buffer.com/reference.html#type/TagByIdInput)[INPUTTagComparator](https://developers.buffer.com/reference.html#type/TagComparator)[INPUTTagInput](https://developers.buffer.com/reference.html#type/TagInput)[INPUTTagsFiltersInput](https://developers.buffer.com/reference.html#type/TagsFiltersInput)[INPUTTagsInput](https://developers.buffer.com/reference.html#type/TagsInput)[INPUTTagToCreateInput](https://developers.buffer.com/reference.html#type/TagToCreateInput)[INPUTTagToUpdateInput](https://developers.buffer.com/reference.html#type/TagToUpdateInput)[ENUMTagColorName](https://developers.buffer.com/reference.html#type/TagColorName)[SCALARTagId](https://developers.buffer.com/reference.html#type/TagId)
[Posts](https://developers.buffer.com/reference.html#posts)
[QUERYaggregatedPostMetrics](https://developers.buffer.com/reference.html#field-aggregatedPostMetrics)[QUERYdailyPostingLimits](https://developers.buffer.com/reference.html#field-dailyPostingLimits)[QUERYinstagramAudio](https://developers.buffer.com/reference.html#field-instagramAudio)[QUERYinstagramAudioCatalog](https://developers.buffer.com/reference.html#field-instagramAudioCatalog)[QUERYpost](https://developers.buffer.com/reference.html#field-post)[QUERYposts](https://developers.buffer.com/reference.html#field-posts)[QUERYpostTemplate](https://developers.buffer.com/reference.html#field-postTemplate)[QUERYpostTemplates](https://developers.buffer.com/reference.html#field-postTemplates)[QUERYsearchInstagramAudio](https://developers.buffer.com/reference.html#field-searchInstagramAudio)[QUERYsearchInstagramAudioCatalog](https://developers.buffer.com/reference.html#field-searchInstagramAudioCatalog)[QUERYtrendingInstagramAudio](https://developers.buffer.com/reference.html#field-trendingInstagramAudio)[MUTATIONaddPostToContentItem](https://developers.buffer.com/reference.html#field-addPostToContentItem)[MUTATIONcreatePost](https://developers.buffer.com/reference.html#field-createPost)[MUTATIONcreatePostTemplate](https://developers.buffer.com/reference.html#field-createPostTemplate)[MUTATIONdeletePost](https://developers.buffer.com/reference.html#field-deletePost)[MUTATIONdeletePostTemplate](https://developers.buffer.com/reference.html#field-deletePostTemplate)[MUTATIONeditPost](https://developers.buffer.com/reference.html#field-editPost)[MUTATIONmovePostInQueue](https://developers.buffer.com/reference.html#field-movePostInQueue)[MUTATIONpromoteContentItemDraftToPosts](https://developers.buffer.com/reference.html#field-promoteContentItemDraftToPosts)[MUTATIONremovePostFromContentItem](https://developers.buffer.com/reference.html#field-removePostFromContentItem)[MUTATIONupdateContentItem](https://developers.buffer.com/reference.html#field-updateContentItem)[MUTATIONupdateContentItemDraft](https://developers.buffer.com/reference.html#field-updateContentItemDraft)[MUTATIONupdatePostTemplate](https://developers.buffer.com/reference.html#field-updatePostTemplate)[MUTATIONupdateSnippet](https://developers.buffer.com/reference.html#field-updateSnippet)[TYPEAddPostToContentItemSuccess](https://developers.buffer.com/reference.html#type/AddPostToContentItemSuccess)[OUTPUTAggregatedPostMetrics](https://developers.buffer.com/reference.html#type/AggregatedPostMetrics)[TYPEAnnotation](https://developers.buffer.com/reference.html#type/Annotation)[TYPEAuthor](https://developers.buffer.com/reference.html#type/Author)[TYPEBlueskyPostMetadata](https://developers.buffer.com/reference.html#type/BlueskyPostMetadata)[OUTPUTContentItem](https://developers.buffer.com/reference.html#type/ContentItem)[TYPEContentItemStateError](https://developers.buffer.com/reference.html#type/ContentItemStateError)[TYPECreatePostTemplateSuccess](https://developers.buffer.com/reference.html#type/CreatePostTemplateSuccess)[OUTPUTDailyPostingLimitStatus](https://developers.buffer.com/reference.html#type/DailyPostingLimitStatus)[TYPEDeletePostSuccess](https://developers.buffer.com/reference.html#type/DeletePostSuccess)[TYPEDeleteTagActionSuccess](https://developers.buffer.com/reference.html#type/DeleteTagActionSuccess)[TYPEDraftContent](https://developers.buffer.com/reference.html#type/DraftContent)[TYPEDuplicateError](https://developers.buffer.com/reference.html#type/DuplicateError)[TYPEEmptySuccess](https://developers.buffer.com/reference.html#type/EmptySuccess)[TYPEFacebookPostMetadata](https://developers.buffer.com/reference.html#type/FacebookPostMetadata)[TYPEGoogleBusinessEventMetaData](https://developers.buffer.com/reference.html#type/GoogleBusinessEventMetaData)[TYPEGoogleBusinessOfferMetaData](https://developers.buffer.com/reference.html#type/GoogleBusinessOfferMetaData)[TYPEGoogleBusinessPostMetadata](https://developers.buffer.com/reference.html#type/GoogleBusinessPostMetadata)[TYPEGoogleBusinessWhatsNewMetaData](https://developers.buffer.com/reference.html#type/GoogleBusinessWhatsNewMetaData)[TYPEInstagramAudio](https://developers.buffer.com/reference.html#type/InstagramAudio)[TYPEInstagramAudioCatalogSuccess](https://developers.buffer.com/reference.html#type/InstagramAudioCatalogSuccess)[TYPEInstagramAudioSuccess](https://developers.buffer.com/reference.html#type/InstagramAudioSuccess)[TYPEInstagramGeolocation](https://developers.buffer.com/reference.html#type/InstagramGeolocation)[TYPEInstagramMetadata](https://developers.buffer.com/reference.html#type/InstagramMetadata)[TYPEInstagramPostMetadata](https://developers.buffer.com/reference.html#type/InstagramPostMetadata)[TYPEInstagramStickerFields](https://developers.buffer.com/reference.html#type/InstagramStickerFields)[TYPEInvalidInputError](https://developers.buffer.com/reference.html#type/InvalidInputError)[TYPELinkAttachment](https://developers.buffer.com/reference.html#type/LinkAttachment)[TYPELinkedInPostMetadata](https://developers.buffer.com/reference.html#type/LinkedInPostMetadata)[TYPEMastodonPostMetadata](https://developers.buffer.com/reference.html#type/MastodonPostMetadata)[TYPENote](https://developers.buffer.com/reference.html#type/Note)[TYPENotFoundError](https://developers.buffer.com/reference.html#type/NotFoundError)[TYPEPinterestPostMetadata](https://developers.buffer.com/reference.html#type/PinterestPostMetadata)[OUTPUTPost](https://developers.buffer.com/reference.html#type/Post)[TYPEPostActionSuccess](https://developers.buffer.com/reference.html#type/PostActionSuccess)[TYPEPostContent](https://developers.buffer.com/reference.html#type/PostContent)[TYPEPostingGoal](https://developers.buffer.com/reference.html#type/PostingGoal)[TYPEPostInvalidInputError](https://developers.buffer.com/reference.html#type/PostInvalidInputError)[TYPEPostLimitReachedError](https://developers.buffer.com/reference.html#type/PostLimitReachedError)[TYPEPostMetric](https://developers.buffer.com/reference.html#type/PostMetric)[TYPEPostNotDeletableError](https://developers.buffer.com/reference.html#type/PostNotDeletableError)[TYPEPostPublishingError](https://developers.buffer.com/reference.html#type/PostPublishingError)[TYPEPostsEdge](https://developers.buffer.com/reference.html#type/PostsEdge)[OUTPUTPostsResults](https://developers.buffer.com/reference.html#type/PostsResults)[OUTPUTPostTemplate](https://developers.buffer.com/reference.html#type/PostTemplate)[TYPEPostTemplateEdge](https://developers.buffer.com/reference.html#type/PostTemplateEdge)[OUTPUTPostTemplatesConnection](https://developers.buffer.com/reference.html#type/PostTemplatesConnection)[TYPEPromoteContentItemDraftToPostsFailure](https://developers.buffer.com/reference.html#type/PromoteContentItemDraftToPostsFailure)[TYPEPromoteContentItemDraftToPostsSuccess](https://developers.buffer.com/reference.html#type/PromoteContentItemDraftToPostsSuccess)[TYPEPublishingTag](https://developers.buffer.com/reference.html#type/PublishingTag)[TYPERemovePostFromContentItemSuccess](https://developers.buffer.com/reference.html#type/RemovePostFromContentItemSuccess)[TYPERestProxyError](https://developers.buffer.com/reference.html#type/RestProxyError)[TYPERetweetMetadata](https://developers.buffer.com/reference.html#type/RetweetMetadata)[TYPERetweetUserMetadata](https://developers.buffer.com/reference.html#type/RetweetUserMetadata)[TYPESearchInstagramAudioSuccess](https://developers.buffer.com/reference.html#type/SearchInstagramAudioSuccess)[TYPESnippet](https://developers.buffer.com/reference.html#type/Snippet)[TYPESubstackPostMetadata](https://developers.buffer.com/reference.html#type/SubstackPostMetadata)[TYPEThreadedPost](https://developers.buffer.com/reference.html#type/ThreadedPost)[TYPEThreadItemBlueskyMetadata](https://developers.buffer.com/reference.html#type/ThreadItemBlueskyMetadata)[TYPEThreadItemMetadata](https://developers.buffer.com/reference.html#type/ThreadItemMetadata)[TYPEThreadItemThreadsMetadata](https://developers.buffer.com/reference.html#type/ThreadItemThreadsMetadata)[TYPEThreadsPostMetadata](https://developers.buffer.com/reference.html#type/ThreadsPostMetadata)[TYPETiktokPostMetadata](https://developers.buffer.com/reference.html#type/TiktokPostMetadata)[TYPETwitterPostMetadata](https://developers.buffer.com/reference.html#type/TwitterPostMetadata)[TYPEUpdateContentItemDraftFailure](https://developers.buffer.com/reference.html#type/UpdateContentItemDraftFailure)[TYPEUpdateContentItemDraftSuccess](https://developers.buffer.com/reference.html#type/UpdateContentItemDraftSuccess)[TYPEUpdateContentItemFailure](https://developers.buffer.com/reference.html#type/UpdateContentItemFailure)[TYPEUpdateContentItemSuccess](https://developers.buffer.com/reference.html#type/UpdateContentItemSuccess)[TYPEUpdatePostTemplateSuccess](https://developers.buffer.com/reference.html#type/UpdatePostTemplateSuccess)[TYPEUpdateSnippetSuccess](https://developers.buffer.com/reference.html#type/UpdateSnippetSuccess)[TYPEUserTag](https://developers.buffer.com/reference.html#type/UserTag)[TYPEVoidMutationError](https://developers.buffer.com/reference.html#type/VoidMutationError)[TYPEWeeklyPostingLimit](https://developers.buffer.com/reference.html#type/WeeklyPostingLimit)[TYPEYoutubeCategory](https://developers.buffer.com/reference.html#type/YoutubeCategory)[TYPEYoutubePostMetadata](https://developers.buffer.com/reference.html#type/YoutubePostMetadata)[INPUTAddPostToContentItemInput](https://developers.buffer.com/reference.html#type/AddPostToContentItemInput)[INPUTAggregatedPostMetricsInput](https://developers.buffer.com/reference.html#type/AggregatedPostMetricsInput)[INPUTAnnotationInputFacebook](https://developers.buffer.com/reference.html#type/AnnotationInputFacebook)[INPUTAnnotationInputLinkedIn](https://developers.buffer.com/reference.html#type/AnnotationInputLinkedIn)[INPUTAssetInput](https://developers.buffer.com/reference.html#type/AssetInput)[INPUTBlueskyPostMetadataInput](https://developers.buffer.com/reference.html#type/BlueskyPostMetadataInput)[INPUTCreatePostInput](https://developers.buffer.com/reference.html#type/CreatePostInput)[INPUTCreatePostTemplateInput](https://developers.buffer.com/reference.html#type/CreatePostTemplateInput)[INPUTCreateTagInput](https://developers.buffer.com/reference.html#type/CreateTagInput)[INPUTDailyPostingLimitsInput](https://developers.buffer.com/reference.html#type/DailyPostingLimitsInput)[INPUTDateTimeComparator](https://developers.buffer.com/reference.html#type/DateTimeComparator)[INPUTDeletePostInput](https://developers.buffer.com/reference.html#type/DeletePostInput)[INPUTDeletePostTemplateInput](https://developers.buffer.com/reference.html#type/DeletePostTemplateInput)[INPUTDeleteTagInput](https://developers.buffer.com/reference.html#type/DeleteTagInput)[INPUTDocumentAssetInput](https://developers.buffer.com/reference.html#type/DocumentAssetInput)[INPUTDraftContentInput](https://developers.buffer.com/reference.html#type/DraftContentInput)[INPUTEditPostInput](https://developers.buffer.com/reference.html#type/EditPostInput)[INPUTFacebookPostMetadataInput](https://developers.buffer.com/reference.html#type/FacebookPostMetadataInput)[INPUTGoogleBusinessEventMetaDataInput](https://developers.buffer.com/reference.html#type/GoogleBusinessEventMetaDataInput)[INPUTGoogleBusinessOfferMetaDataInput](https://developers.buffer.com/reference.html#type/GoogleBusinessOfferMetaDataInput)[INPUTGoogleBusinessPostMetadataInput](https://developers.buffer.com/reference.html#type/GoogleBusinessPostMetadataInput)[INPUTGoogleBusinessWhatsNewMetaDataInput](https://developers.buffer.com/reference.html#type/GoogleBusinessWhatsNewMetaDataInput)[INPUTImageAssetInput](https://developers.buffer.com/reference.html#type/ImageAssetInput)[INPUTImageDimensionsInput](https://developers.buffer.com/reference.html#type/ImageDimensionsInput)[INPUTImageMetadataInput](https://developers.buffer.com/reference.html#type/ImageMetadataInput)[INPUTInstagramAudioCatalogInput](https://developers.buffer.com/reference.html#type/InstagramAudioCatalogInput)[INPUTInstagramAudioInput](https://developers.buffer.com/reference.html#type/InstagramAudioInput)[INPUTInstagramGeolocationInput](https://developers.buffer.com/reference.html#type/InstagramGeolocationInput)[INPUTInstagramPostMetadataInput](https://developers.buffer.com/reference.html#type/InstagramPostMetadataInput)[INPUTInstagramStickerFieldsInput](https://developers.buffer.com/reference.html#type/InstagramStickerFieldsInput)[INPUTLinkAssetInput](https://developers.buffer.com/reference.html#type/LinkAssetInput)[INPUTLinkAttachmentInput](https://developers.buffer.com/reference.html#type/LinkAttachmentInput)[INPUTLinkAttachmentThumbnailInput](https://developers.buffer.com/reference.html#type/LinkAttachmentThumbnailInput)[INPUTLinkedInPostMetadataInput](https://developers.buffer.com/reference.html#type/LinkedInPostMetadataInput)[INPUTMastodonPostMetadataInput](https://developers.buffer.com/reference.html#type/MastodonPostMetadataInput)[INPUTMovePostInQueueInput](https://developers.buffer.com/reference.html#type/MovePostInQueueInput)[INPUTPinterestPostMetadataInput](https://developers.buffer.com/reference.html#type/PinterestPostMetadataInput)[INPUTPostInput](https://developers.buffer.com/reference.html#type/PostInput)[INPUTPostInputMetaData](https://developers.buffer.com/reference.html#type/PostInputMetaData)[INPUTPostsFiltersInput](https://developers.buffer.com/reference.html#type/PostsFiltersInput)[INPUTPostsInput](https://developers.buffer.com/reference.html#type/PostsInput)[INPUTPostSortInput](https://developers.buffer.com/reference.html#type/PostSortInput)[INPUTPostTemplateInput](https://developers.buffer.com/reference.html#type/PostTemplateInput)[INPUTPostTemplatesFilterInput](https://developers.buffer.com/reference.html#type/PostTemplatesFilterInput)[INPUTPostTemplatesInput](https://developers.buffer.com/reference.html#type/PostTemplatesInput)[INPUTPromoteContentItemDraftToPostsInput](https://developers.buffer.com/reference.html#type/PromoteContentItemDraftToPostsInput)[INPUTRemovePostFromContentItemInput](https://developers.buffer.com/reference.html#type/RemovePostFromContentItemInput)[INPUTRetweetMetadataInput](https://developers.buffer.com/reference.html#type/RetweetMetadataInput)[INPUTSearchInstagramAudioCatalogInput](https://developers.buffer.com/reference.html#type/SearchInstagramAudioCatalogInput)[INPUTSearchInstagramAudioInput](https://developers.buffer.com/reference.html#type/SearchInstagramAudioInput)[INPUTSubstackPostMetadataInput](https://developers.buffer.com/reference.html#type/SubstackPostMetadataInput)[INPUTThreadedPostInput](https://developers.buffer.com/reference.html#type/ThreadedPostInput)[INPUTThreadItemBlueskyMetadataInput](https://developers.buffer.com/reference.html#type/ThreadItemBlueskyMetadataInput)[INPUTThreadItemMetadataInput](https://developers.buffer.com/reference.html#type/ThreadItemMetadataInput)[INPUTThreadItemThreadsMetadataInput](https://developers.buffer.com/reference.html#type/ThreadItemThreadsMetadataInput)[INPUTThreadsPostMetadataInput](https://developers.buffer.com/reference.html#type/ThreadsPostMetadataInput)[INPUTTikTokPostMetadataInput](https://developers.buffer.com/reference.html#type/TikTokPostMetadataInput)[INPUTTrendingInstagramAudioInput](https://developers.buffer.com/reference.html#type/TrendingInstagramAudioInput)[INPUTTwitterPostMetadataInput](https://developers.buffer.com/reference.html#type/TwitterPostMetadataInput)[INPUTUpdateContentItemDraftInput](https://developers.buffer.com/reference.html#type/UpdateContentItemDraftInput)[INPUTUpdateContentItemInput](https://developers.buffer.com/reference.html#type/UpdateContentItemInput)[INPUTUpdatePostTemplateInput](https://developers.buffer.com/reference.html#type/UpdatePostTemplateInput)[INPUTUpdateSnippetInput](https://developers.buffer.com/reference.html#type/UpdateSnippetInput)[INPUTUpdateTagInput](https://developers.buffer.com/reference.html#type/UpdateTagInput)[INPUTUserTagInput](https://developers.buffer.com/reference.html#type/UserTagInput)[INPUTVideoAssetInput](https://developers.buffer.com/reference.html#type/VideoAssetInput)[INPUTVideoMetadataInput](https://developers.buffer.com/reference.html#type/VideoMetadataInput)[INPUTYoutubePostMetadataInput](https://developers.buffer.com/reference.html#type/YoutubePostMetadataInput)[TYPEAsset](https://developers.buffer.com/reference.html#type/Asset)[TYPECommonPostMetadata](https://developers.buffer.com/reference.html#type/CommonPostMetadata)[TYPEThreadedPostMetadata](https://developers.buffer.com/reference.html#type/ThreadedPostMetadata)[OUTPUTAddPostToContentItemPayload](https://developers.buffer.com/reference.html#type/AddPostToContentItemPayload)[TYPEContentItemBody](https://developers.buffer.com/reference.html#type/ContentItemBody)[OUTPUTCreatePostTemplatePayload](https://developers.buffer.com/reference.html#type/CreatePostTemplatePayload)[OUTPUTCreateTagPayload](https://developers.buffer.com/reference.html#type/CreateTagPayload)[OUTPUTDeletePostPayload](https://developers.buffer.com/reference.html#type/DeletePostPayload)[OUTPUTDeletePostTemplatePayload](https://developers.buffer.com/reference.html#type/DeletePostTemplatePayload)[OUTPUTDeleteTagPayload](https://developers.buffer.com/reference.html#type/DeleteTagPayload)[TYPEGoogleBusinessPostDetails](https://developers.buffer.com/reference.html#type/GoogleBusinessPostDetails)[OUTPUTInstagramAudioCatalogPayload](https://developers.buffer.com/reference.html#type/InstagramAudioCatalogPayload)[OUTPUTInstagramAudioPayload](https://developers.buffer.com/reference.html#type/InstagramAudioPayload)[OUTPUTMovePostInQueuePayload](https://developers.buffer.com/reference.html#type/MovePostInQueuePayload)[OUTPUTPostActionPayload](https://developers.buffer.com/reference.html#type/PostActionPayload)[TYPEPostMetadata](https://developers.buffer.com/reference.html#type/PostMetadata)[TYPEPromoteContentItemDraftToPostsError](https://developers.buffer.com/reference.html#type/PromoteContentItemDraftToPostsError)[OUTPUTPromoteContentItemDraftToPostsPayload](https://developers.buffer.com/reference.html#type/PromoteContentItemDraftToPostsPayload)[OUTPUTRemovePostFromContentItemPayload](https://developers.buffer.com/reference.html#type/RemovePostFromContentItemPayload)[OUTPUTSearchInstagramAudioPayload](https://developers.buffer.com/reference.html#type/SearchInstagramAudioPayload)[TYPEUpdateContentItemDraftError](https://developers.buffer.com/reference.html#type/UpdateContentItemDraftError)[OUTPUTUpdateContentItemDraftPayload](https://developers.buffer.com/reference.html#type/UpdateContentItemDraftPayload)[OUTPUTUpdateContentItemPayload](https://developers.buffer.com/reference.html#type/UpdateContentItemPayload)[OUTPUTUpdatePostTemplatePayload](https://developers.buffer.com/reference.html#type/UpdatePostTemplatePayload)[OUTPUTUpdateSnippetPayload](https://developers.buffer.com/reference.html#type/UpdateSnippetPayload)[OUTPUTUpdateTagPayload](https://developers.buffer.com/reference.html#type/UpdateTagPayload)[ENUMAnnotationType](https://developers.buffer.com/reference.html#type/AnnotationType)[ENUMAssetType](https://developers.buffer.com/reference.html#type/AssetType)[ENUMContentItemAction](https://developers.buffer.com/reference.html#type/ContentItemAction)[ENUMDateTimePresence](https://developers.buffer.com/reference.html#type/DateTimePresence)[ENUMGoogleBusinessPostActionType](https://developers.buffer.com/reference.html#type/GoogleBusinessPostActionType)[ENUMInstagramAudioType](https://developers.buffer.com/reference.html#type/InstagramAudioType)[ENUMNoteAction](https://developers.buffer.com/reference.html#type/NoteAction)[ENUMNoteType](https://developers.buffer.com/reference.html#type/NoteType)[ENUMNotificationStatus](https://developers.buffer.com/reference.html#type/NotificationStatus)[ENUMPostAction](https://developers.buffer.com/reference.html#type/PostAction)[ENUMPostApprovalChange](https://developers.buffer.com/reference.html#type/PostApprovalChange)[ENUMPostingGoalStatus](https://developers.buffer.com/reference.html#type/PostingGoalStatus)[ENUMPostMetricType](https://developers.buffer.com/reference.html#type/PostMetricType)[ENUMPostMetricUnit](https://developers.buffer.com/reference.html#type/PostMetricUnit)[ENUMPostSortableKey](https://developers.buffer.com/reference.html#type/PostSortableKey)[ENUMPostStatus](https://developers.buffer.com/reference.html#type/PostStatus)[ENUMPostTemplateVisibility](https://developers.buffer.com/reference.html#type/PostTemplateVisibility)[ENUMPostType](https://developers.buffer.com/reference.html#type/PostType)[ENUMPostTypeFacebook](https://developers.buffer.com/reference.html#type/PostTypeFacebook)[ENUMPostTypeGoogleBusiness](https://developers.buffer.com/reference.html#type/PostTypeGoogleBusiness)[ENUMPostVia](https://developers.buffer.com/reference.html#type/PostVia)[ENUMQueuePosition](https://developers.buffer.com/reference.html#type/QueuePosition)[ENUMSchedulingType](https://developers.buffer.com/reference.html#type/SchedulingType)[ENUMShareMode](https://developers.buffer.com/reference.html#type/ShareMode)[ENUMSortDirection](https://developers.buffer.com/reference.html#type/SortDirection)[ENUMYoutubeLicense](https://developers.buffer.com/reference.html#type/YoutubeLicense)[ENUMYoutubePrivacy](https://developers.buffer.com/reference.html#type/YoutubePrivacy)[SCALARContentItemId](https://developers.buffer.com/reference.html#type/ContentItemId)[SCALARDraftContentId](https://developers.buffer.com/reference.html#type/DraftContentId)[SCALARDraftId](https://developers.buffer.com/reference.html#type/DraftId)[SCALARNoteId](https://developers.buffer.com/reference.html#type/NoteId)[SCALARPostId](https://developers.buffer.com/reference.html#type/PostId)[SCALARPostTemplateId](https://developers.buffer.com/reference.html#type/PostTemplateId)[SCALARSnippetId](https://developers.buffer.com/reference.html#type/SnippetId)[SCALARURL](https://developers.buffer.com/reference.html#type/URL)
[Ideas](https://developers.buffer.com/reference.html#ideas)
[QUERYideaGroups](https://developers.buffer.com/reference.html#field-ideaGroups)[QUERYideas](https://developers.buffer.com/reference.html#field-ideas)[MUTATIONcreateIdea](https://developers.buffer.com/reference.html#field-createIdea)[TYPEIdea](https://developers.buffer.com/reference.html#type/Idea)[TYPEIdeaContent](https://developers.buffer.com/reference.html#type/IdeaContent)[TYPEIdeaEdge](https://developers.buffer.com/reference.html#type/IdeaEdge)[OUTPUTIdeaGroup](https://developers.buffer.com/reference.html#type/IdeaGroup)[TYPEIdeaResponse](https://developers.buffer.com/reference.html#type/IdeaResponse)[OUTPUTIdeasConnection](https://developers.buffer.com/reference.html#type/IdeasConnection)[TYPELimitReachedError](https://developers.buffer.com/reference.html#type/LimitReachedError)[TYPEPaginationPageInfo](https://developers.buffer.com/reference.html#type/PaginationPageInfo)[TYPEUnauthorizedError](https://developers.buffer.com/reference.html#type/UnauthorizedError)[TYPEUnexpectedError](https://developers.buffer.com/reference.html#type/UnexpectedError)[INPUTCreateIdeaInput](https://developers.buffer.com/reference.html#type/CreateIdeaInput)[INPUTIdeaContentInput](https://developers.buffer.com/reference.html#type/IdeaContentInput)[INPUTIdeaGroupInput](https://developers.buffer.com/reference.html#type/IdeaGroupInput)[INPUTIdeaGroupsInput](https://developers.buffer.com/reference.html#type/IdeaGroupsInput)[INPUTIdeasGroupFilter](https://developers.buffer.com/reference.html#type/IdeasGroupFilter)[INPUTIdeasInput](https://developers.buffer.com/reference.html#type/IdeasInput)[OUTPUTCreateIdeaPayload](https://developers.buffer.com/reference.html#type/CreateIdeaPayload)[ENUMIdeaGroupMembership](https://developers.buffer.com/reference.html#type/IdeaGroupMembership)[SCALARIdeaId](https://developers.buffer.com/reference.html#type/IdeaId)
[Organizations](https://developers.buffer.com/reference.html#organizations)
[TYPEMemberConnection](https://developers.buffer.com/reference.html#type/MemberConnection)[TYPEOrganization](https://developers.buffer.com/reference.html#type/Organization)[TYPEOrganizationLimits](https://developers.buffer.com/reference.html#type/OrganizationLimits)[INPUTOrganizationFilterInput](https://developers.buffer.com/reference.html#type/OrganizationFilterInput)[SCALAROrganizationId](https://developers.buffer.com/reference.html#type/OrganizationId)
[Other](https://developers.buffer.com/reference.html#other)
[QUERYconfiguration](https://developers.buffer.com/reference.html#field-configuration)[QUERYcontentItem](https://developers.buffer.com/reference.html#field-contentItem)[QUERYcontentItems](https://developers.buffer.com/reference.html#field-contentItems)[QUERYsnippets](https://developers.buffer.com/reference.html#field-snippets)[MUTATIONcreateContentItem](https://developers.buffer.com/reference.html#field-createContentItem)[MUTATIONcreateContentItemDraft](https://developers.buffer.com/reference.html#field-createContentItemDraft)[MUTATIONcreateSnippet](https://developers.buffer.com/reference.html#field-createSnippet)[MUTATIONdeleteContentItem](https://developers.buffer.com/reference.html#field-deleteContentItem)[MUTATIONdeleteSnippet](https://developers.buffer.com/reference.html#field-deleteSnippet)[OUTPUTConfiguration](https://developers.buffer.com/reference.html#type/Configuration)[TYPEContentItemEdge](https://developers.buffer.com/reference.html#type/ContentItemEdge)[OUTPUTContentItemsConnection](https://developers.buffer.com/reference.html#type/ContentItemsConnection)[TYPECountRule](https://developers.buffer.com/reference.html#type/CountRule)[TYPECreateContentItemDraftFailure](https://developers.buffer.com/reference.html#type/CreateContentItemDraftFailure)[TYPECreateContentItemDraftSuccess](https://developers.buffer.com/reference.html#type/CreateContentItemDraftSuccess)[TYPECreateContentItemFailure](https://developers.buffer.com/reference.html#type/CreateContentItemFailure)[TYPECreateContentItemSuccess](https://developers.buffer.com/reference.html#type/CreateContentItemSuccess)[TYPECreateContentItemVariantInvalidInputError](https://developers.buffer.com/reference.html#type/CreateContentItemVariantInvalidInputError)[TYPECreateContentItemVariantLimitReachedError](https://developers.buffer.com/reference.html#type/CreateContentItemVariantLimitReachedError)[TYPECreateContentItemVariantNotFoundError](https://developers.buffer.com/reference.html#type/CreateContentItemVariantNotFoundError)[TYPECreateSnippetSuccess](https://developers.buffer.com/reference.html#type/CreateSnippetSuccess)[TYPEDeleteContentItemFailure](https://developers.buffer.com/reference.html#type/DeleteContentItemFailure)[TYPEDeleteSnippetSuccess](https://developers.buffer.com/reference.html#type/DeleteSnippetSuccess)[TYPEDocumentAsset](https://developers.buffer.com/reference.html#type/DocumentAsset)[TYPEDocumentMetadata](https://developers.buffer.com/reference.html#type/DocumentMetadata)[TYPEDurationRule](https://developers.buffer.com/reference.html#type/DurationRule)[TYPEExclusiveRule](https://developers.buffer.com/reference.html#type/ExclusiveRule)[TYPEFileSizeRule](https://developers.buffer.com/reference.html#type/FileSizeRule)[TYPEFormatRule](https://developers.buffer.com/reference.html#type/FormatRule)[TYPEImageAsset](https://developers.buffer.com/reference.html#type/ImageAsset)[TYPEImageMetadata](https://developers.buffer.com/reference.html#type/ImageMetadata)[TYPELengthRule](https://developers.buffer.com/reference.html#type/LengthRule)[TYPERequiresRule](https://developers.buffer.com/reference.html#type/RequiresRule)[TYPEServiceConfiguration](https://developers.buffer.com/reference.html#type/ServiceConfiguration)[TYPESnippetEdge](https://developers.buffer.com/reference.html#type/SnippetEdge)[OUTPUTSnippetsConnection](https://developers.buffer.com/reference.html#type/SnippetsConnection)[TYPEVideoAsset](https://developers.buffer.com/reference.html#type/VideoAsset)[TYPEVideoMetadata](https://developers.buffer.com/reference.html#type/VideoMetadata)[INPUTConfigurationInput](https://developers.buffer.com/reference.html#type/ConfigurationInput)[INPUTContentItemInput](https://developers.buffer.com/reference.html#type/ContentItemInput)[INPUTContentItemsFilter](https://developers.buffer.com/reference.html#type/ContentItemsFilter)[INPUTContentItemsInput](https://developers.buffer.com/reference.html#type/ContentItemsInput)[INPUTContentItemsSortInput](https://developers.buffer.com/reference.html#type/ContentItemsSortInput)[INPUTContentItemsTargetDateFilter](https://developers.buffer.com/reference.html#type/ContentItemsTargetDateFilter)[INPUTCreateContentItemDraftInput](https://developers.buffer.com/reference.html#type/CreateContentItemDraftInput)[INPUTCreateContentItemInput](https://developers.buffer.com/reference.html#type/CreateContentItemInput)[INPUTCreateSnippetInput](https://developers.buffer.com/reference.html#type/CreateSnippetInput)[INPUTDeleteContentItemInput](https://developers.buffer.com/reference.html#type/DeleteContentItemInput)[INPUTDeleteSnippetInput](https://developers.buffer.com/reference.html#type/DeleteSnippetInput)[INPUTSnippetsInput](https://developers.buffer.com/reference.html#type/SnippetsInput)[TYPEMutationError](https://developers.buffer.com/reference.html#type/MutationError)[TYPEMutationSuccess](https://developers.buffer.com/reference.html#type/MutationSuccess)[TYPEScrapedLink](https://developers.buffer.com/reference.html#type/ScrapedLink)[OUTPUTCreateContentItemDraftPayload](https://developers.buffer.com/reference.html#type/CreateContentItemDraftPayload)[TYPECreateContentItemError](https://developers.buffer.com/reference.html#type/CreateContentItemError)[OUTPUTCreateContentItemPayload](https://developers.buffer.com/reference.html#type/CreateContentItemPayload)[OUTPUTCreateSnippetPayload](https://developers.buffer.com/reference.html#type/CreateSnippetPayload)[OUTPUTDeleteContentItemPayload](https://developers.buffer.com/reference.html#type/DeleteContentItemPayload)[OUTPUTDeleteSnippetPayload](https://developers.buffer.com/reference.html#type/DeleteSnippetPayload)[ENUMContentItemSortableKey](https://developers.buffer.com/reference.html#type/ContentItemSortableKey)[ENUMContentItemStatus](https://developers.buffer.com/reference.html#type/ContentItemStatus)[SCALAREmail](https://developers.buffer.com/reference.html#type/Email)[SCALARInvitationId](https://developers.buffer.com/reference.html#type/InvitationId)[SCALARUuid](https://developers.buffer.com/reference.html#type/Uuid)
`Esc`
`↑``↓` Navigate `Enter` Open `Esc` Close

