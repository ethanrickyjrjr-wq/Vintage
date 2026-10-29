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
Core ConceptsPosts & Scheduling
# Posts & Scheduling
Copy Page
Ask AI assistant Chat with the docs AI assistant Copy page Copy this page as Markdown View as Markdown Open this page as plain Markdown Open in Claude Ask Claude about this page Open in ChatGPT Ask ChatGPT about this page Open in Perplexity Ask Perplexity about this page
Posts are the core content type in Buffer. Here's how they work, from creation through delivery.
## What is a post?[](https://developers.buffer.com/guides/posts-and-scheduling.html#what-is-a-post)
A post is a piece of content scheduled or published through Buffer. Every post belongs to a specific [channel](https://developers.buffer.com/guides/data-model.html#channel) (a connected social media profile) and goes through a lifecycle from creation to delivery.
Key fields on a post:
  * **`id`**- unique identifier
  * **`text`**- the post content
  * **`channelId`**- which channel this post belongs to
  * **`dueAt`**- when the post is scheduled to publish
  * **`status`**- current lifecycle state (scheduled, sent, etc.)
  * **`assets`**- attached images or media


## Scheduling types[](https://developers.buffer.com/guides/posts-and-scheduling.html#scheduling-types)
When creating a post, you choose how it should be scheduled:
###  `addToQueue`[](https://developers.buffer.com/guides/posts-and-scheduling.html#addtoqueue)
We'll add the post to the next available time slot from your posting schedule. This is the simplest option.
Copy Copied! 
```
mutation {
  createPost(
    input: {
      text: "Automatically scheduled post"
      channelId: "your_channel_id"
      schedulingType: automatic
      mode: addToQueue
    }
  ) {
    ... on PostActionSuccess {
      post {
        id
        dueAt
      }
    }
    ... on MutationError {
      message
    }
  }
}
```

###  `customScheduled`[](https://developers.buffer.com/guides/posts-and-scheduling.html#customscheduled)
You specify an exact date and time using the `dueAt` field in ISO 8601 format (UTC):
Copy Copied! 
```
mutation {
  createPost(
    input: {
      text: "Scheduled for a specific time"
      channelId: "your_channel_id"
      schedulingType: automatic
      mode: customScheduled
      dueAt: "2026-03-10T15:00:00.000Z"
    }
  ) {
    ... on PostActionSuccess {
      post {
        id
        dueAt
      }
    }
    ... on MutationError {
      message
    }
  }
}
```

## Post status lifecycle[](https://developers.buffer.com/guides/posts-and-scheduling.html#post-status-lifecycle)
A post moves through the following states:
  * **Scheduled** the post is in the queue, waiting for its `dueAt` time
  * **Sent** the post was successfully published to the social platform
  * **Error** the post could not be published (e.g., the channel was disconnected)


## Creating posts[](https://developers.buffer.com/guides/posts-and-scheduling.html#creating-posts)
Use the `createPost` mutation. Required fields:
  * **`text`**- the post content
  * **`channelId`**- the target channel
  * **`schedulingType`**- how to schedule (`automatic`)


Always include both `PostActionSuccess` and `MutationError` in your response:
Copy Copied! 
```
mutation {
  createPost(
    input: {
      text: "Hello from the API"
      channelId: "your_channel_id"
      schedulingType: automatic
      mode: addToQueue
    }
  ) {
    ... on PostActionSuccess {
      post {
        id
        text
        dueAt
        assets {
          id
          mimeType
        }
      }
    }
    ... on MutationError {
      message
    }
  }
}
```

See [Create a Text Post](https://developers.buffer.com/examples/create-text-post.html) and [Create an Image Post](https://developers.buffer.com/examples/create-image-post.html) for complete examples.
### Channel-specific configuration[](https://developers.buffer.com/guides/posts-and-scheduling.html#channel-specific-configuration)
Beyond the shared fields above, the API supports channel-specific configuration through the `metadata` field on `createPost`. Each network has its own metadata input, so you can do things like create a [thread](https://developers.buffer.com/examples/create-threaded-post.html) on X (Twitter), Bluesky, Threads, or Mastodon, add a first comment on LinkedIn, Facebook, or Instagram, set the post type (post, story, reel) on Instagram, or attach a board to a Pinterest pin. You only need to provide the metadata for the network the channel belongs to. To learn more about the available configurations for each network, see the [PostInputMetaData](https://developers.buffer.com/types/PostInputMetaData.html) reference.
A few options are configured on the assets themselves rather than in the network `metadata`. For example, Instagram user tags are positioned per image via `image.metadata.userTags` - see [Create an Instagram Post with User Tags](https://developers.buffer.com/examples/create-instagram-post-with-user-tags.html) for a complete example.
## Retrieving posts[](https://developers.buffer.com/guides/posts-and-scheduling.html#retrieving-posts)
Query posts for a specific organization, filtered by channel and status:
Copy Copied! 
```
query {
  posts(
    first: 20
    input: {
      organizationId: "your_org_id"
      filter: { status: [sent], channelIds: ["your_channel_id"] }
    }
  ) {
    edges {
      node {
        id
        text
        dueAt
        channelId
      }
    }
    pageInfo {
      hasNextPage
      endCursor
    }
  }
}
```

Posts are returned using [cursor-based pagination](https://developers.buffer.com/guides/pagination.html). Use `first` and `after` to page through results.
See [Get Posts for Channels](https://developers.buffer.com/examples/get-posts-for-channels.html) and [Get Paginated Posts](https://developers.buffer.com/examples/get-paginated-posts.html) for more examples.
## Metrics[](https://developers.buffer.com/guides/posts-and-scheduling.html#metrics)
Once a post is sent, the network reports performance data — reactions, impressions, reach, and so on. Buffer normalizes those values across networks and exposes them on `Post.metrics`. Reading metrics is available for personal workflows and automations only, using a personal API key.
See [Post Metrics](https://developers.buffer.com/guides/post-metrics.html) for the full guide and [Get Post Metrics](https://developers.buffer.com/examples/get-post-metrics.html) for a single-post query.
## Supported platforms[](https://developers.buffer.com/guides/posts-and-scheduling.html#supported-platforms)
The API can create posts for the following platforms:
  * Instagram
  * Threads
  * LinkedIn
  * X (Twitter)
  * Facebook
  * Google Business Profiles
  * Mastodon
  * YouTube
  * Pinterest
  * Bluesky


The `service` field on a [Channel](https://developers.buffer.com/guides/data-model.html#channel) tells you which platform it's connected to.
## Next steps[](https://developers.buffer.com/guides/posts-and-scheduling.html#next-steps)
  * [Create a Text Post](https://developers.buffer.com/examples/create-text-post.html): basic post creation example
  * [Create an Image Post](https://developers.buffer.com/examples/create-image-post.html): attach images to posts
  * [Ideas](https://developers.buffer.com/guides/ideas.html): save content for later
  * [Pagination](https://developers.buffer.com/guides/pagination.html): iterate through all your posts


[ Previous Data Model ](https://developers.buffer.com/guides/data-model.html) [ Next Ideas ](https://developers.buffer.com/guides/ideas.html)
On this page
[What is a post?](https://developers.buffer.com/guides/posts-and-scheduling.html#what-is-a-post) [Scheduling types](https://developers.buffer.com/guides/posts-and-scheduling.html#scheduling-types) [addToQueue](https://developers.buffer.com/guides/posts-and-scheduling.html#addtoqueue) [customScheduled](https://developers.buffer.com/guides/posts-and-scheduling.html#customscheduled) [Post status lifecycle](https://developers.buffer.com/guides/posts-and-scheduling.html#post-status-lifecycle) [Creating posts](https://developers.buffer.com/guides/posts-and-scheduling.html#creating-posts) [Channel-specific configuration](https://developers.buffer.com/guides/posts-and-scheduling.html#channel-specific-configuration) [Retrieving posts](https://developers.buffer.com/guides/posts-and-scheduling.html#retrieving-posts) [Metrics](https://developers.buffer.com/guides/posts-and-scheduling.html#metrics) [Supported platforms](https://developers.buffer.com/guides/posts-and-scheduling.html#supported-platforms) [Next steps](https://developers.buffer.com/guides/posts-and-scheduling.html#next-steps)
`Esc`
`↑``↓` Navigate `Enter` Open `Esc` Close

