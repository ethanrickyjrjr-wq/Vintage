
```
# Posts & Scheduling

Posts are the core content type in Buffer. Here's how they work, from creation through delivery.

## What is a post?

A post is a piece of content scheduled or published through Buffer. Every post belongs to a specific [channel](https://developers.buffer.com/guides/data-model.md#channel) (a connected social media profile) and goes through a lifecycle from creation to delivery.

Key fields on a post:

- **`id`** - unique identifier
- **`text`** - the post content
- **`channelId`** - which channel this post belongs to
- **`dueAt`** - when the post is scheduled to publish
- **`status`** - current lifecycle state (scheduled, sent, etc.)
- **`assets`** - attached images or media

## Scheduling types

When creating a post, you choose how it should be scheduled:

### `addToQueue`

We'll add the post to the next available time slot from your posting schedule. This is the simplest option.

```graphql
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

### `customScheduled`

You specify an exact date and time using the `dueAt` field in ISO 8601 format (UTC):

```graphql
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

## Post status lifecycle

A post moves through the following states:

- **Scheduled** the post is in the queue, waiting for its `dueAt` time
- **Sent** the post was successfully published to the social platform
- **Error** the post could not be published (e.g., the channel was disconnected)

## Creating posts

Use the `createPost` mutation. Required fields:

- **`text`** - the post content
- **`channelId`** - the target channel
- **`schedulingType`** - how to schedule (`automatic`)

Always include both `PostActionSuccess` and `MutationError` in your response:

```graphql
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

See [Create a Text Post](https://developers.buffer.com/examples/create-text-post.md) and [Create an Image Post](https://developers.buffer.com/examples/create-image-post.md) for complete examples.

### Channel-specific configuration

Beyond the shared fields above, the API supports channel-specific configuration through the `metadata` field on `createPost`. Each network has its own metadata input, so you can do things like create a [thread](https://developers.buffer.com/examples/create-threaded-post.md) on X (Twitter), Bluesky, Threads, or Mastodon, add a first comment on LinkedIn, Facebook, or Instagram, set the post type (post, story, reel) on Instagram, or attach a board to a Pinterest pin. You only need to provide the metadata for the network the channel belongs to. To learn more about the available configurations for each network, see the [PostInputMetaData](https://developers.buffer.com/types/PostInputMetaData.md) reference.

A few options are configured on the assets themselves rather than in the network `metadata`. For example, Instagram user tags are positioned per image via `image.metadata.userTags` - see [Create an Instagram Post with User Tags](https://developers.buffer.com/examples/create-instagram-post-with-user-tags.md) for a complete example.

## Retrieving posts

Query posts for a specific organization, filtered by channel and status:

```graphql
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

Posts are returned using [cursor-based pagination](https://developers.buffer.com/guides/pagination.md). Use `first` and `after` to page through results.

See [Get Posts for Channels](https://developers.buffer.com/examples/get-posts-for-channels.md) and [Get Paginated Posts](https://developers.buffer.com/examples/get-paginated-posts.md) for more examples.

## Metrics

Once a post is sent, the network reports performance data — reactions, impressions, reach, and so on. Buffer normalizes those values across networks and exposes them on `Post.metrics`. Reading metrics is available for personal workflows and automations only, using a personal API key.

See [Post Metrics](https://developers.buffer.com/guides/post-metrics.md) for the full guide and [Get Post Metrics](https://developers.buffer.com/examples/get-post-metrics.md) for a single-post query.

## Supported platforms

The API can create posts for the following platforms:

- Instagram
- Threads
- LinkedIn
- X (Twitter)
- Facebook
- Google Business Profiles
- Mastodon
- YouTube
- Pinterest
- Bluesky

The `service` field on a [Channel](https://developers.buffer.com/guides/data-model.md#channel) tells you which platform it's connected to.

## Next steps

- [Create a Text Post](https://developers.buffer.com/examples/create-text-post.md): basic post creation example
- [Create an Image Post](https://developers.buffer.com/examples/create-image-post.md): attach images to posts
- [Ideas](https://developers.buffer.com/guides/ideas.md): save content for later
- [Pagination](https://developers.buffer.com/guides/pagination.md): iterate through all your posts

```


