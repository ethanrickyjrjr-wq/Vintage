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
[Examples](https://developers.buffer.com/examples/index.html)Create Video Post
# Create Video Post
[ Try in Explorer ](https://developers.buffer.com/explorer.html?query=mutation%20CreatePost%20%7B%0A%20%20createPost\(%0A%20%20%20%20input%3A%20%7B%0A%20%20%20%20%20%20text%3A%20%22Hello%20there%2C%20this%20is%20another%20one!%22%0A%20%20%20%20%20%20channelId%3A%20%22some_channel_id%22%0A%20%20%20%20%20%20schedulingType%3A%20automatic%0A%20%20%20%20%20%20mode%3A%20addToQueue%0A%20%20%20%20%20%20assets%3A%20%5B%0A%20%20%20%20%20%20%20%20%7B%0A%20%20%20%20%20%20%20%20%20%20video%3A%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20url%3A%20%22https%3A%2F%2Fexample.com%2Fvideo.mp4%22%0A%20%20%20%20%20%20%20%20%20%20%20%20metadata%3A%20%7B%20thumbnailOffset%3A%202000%20%7D%0A%20%20%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%5D%0A%20%20%20%20%7D%0A%20%20\)%20%7B%0A%20%20%20%20...%20on%20PostActionSuccess%20%7B%0A%20%20%20%20%20%20post%20%7B%0A%20%20%20%20%20%20%20%20id%0A%20%20%20%20%20%20%20%20text%0A%20%20%20%20%20%20%20%20assets%20%7B%0A%20%20%20%20%20%20%20%20%20%20source%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%7D%0A%20%20%20%20%7D%0A%20%20%20%20...%20on%20MutationError%20%7B%0A%20%20%20%20%20%20message%0A%20%20%20%20%7D%0A%20%20%7D%0A%7D)
Copy Page
Ask AI assistant Chat with the docs AI assistant Copy page Copy this page as Markdown View as Markdown Open this page as plain Markdown Open in Claude Ask Claude about this page Open in ChatGPT Ask ChatGPT about this page Open in Perplexity Ask Perplexity about this page
Creating a post with a video works in the same way as creating a text post, with the addition of a `video` entry in the `assets` array. `assets` is an ordered list where each entry specifies exactly one of `image`, `video`, or `document` - pass a `video` entry with the URL you want to attach. 
To set the video thumbnail, choose which frame to use with `metadata.thumbnailOffset` - a millisecond offset into the video - on Instagram, TikTok, or Pinterest.
> The asset `url` must point to a publicly accessible file. See [Hosting Media](https://developers.buffer.com/guides/hosting-media.html) for suggested hosts and how to verify a URL works.
GraphQLcURLNode.jsPythonPHP
Copy Copied! 
```
mutation CreatePost {
  createPost(
    input: {
      text: "Hello there, this is another one!"
      channelId: "some_channel_id"
      schedulingType: automatic
      mode: addToQueue
      assets: [
        {
          video: {
            url: "https://example.com/video.mp4"
            metadata: { thumbnailOffset: 2000 }
          }
        }
      ]
    }
  ) {
    ... on PostActionSuccess {
      post {
        id
        text
        assets {
          source
        }
      }
    }
    ... on MutationError {
      message
    }
  }
}
```

Copy Copied! 
```
curl -X POST 'https://api.buffer.com' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer YOUR_API_KEY' \
  -d '{"query": "mutation CreatePost {\n  createPost(\n    input: {\n      text: \"Hello there, this is another one!\"\n      channelId: \"some_channel_id\"\n      schedulingType: automatic\n      mode: addToQueue\n      assets: [\n        {\n          video: {\n            url: \"https://example.com/video.mp4\"\n            metadata: { thumbnailOffset: 2000 }\n          }\n        }\n      ]\n    }\n  ) {\n    ... on PostActionSuccess {\n      post {\n        id\n        text\n        assets {\n          source\n        }\n      }\n    }\n    ... on MutationError {\n      message\n    }\n  }\n}"}'
```

Copy Copied! 
```
async function createPost() {
  const response = await fetch('https://api.buffer.com', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer YOUR_API_KEY',
    },
    body: JSON.stringify({
      query: `
      mutation CreatePost {
        createPost(
          input: {
            text: "Hello there, this is another one!"
            channelId: "some_channel_id"
            schedulingType: automatic
            mode: addToQueue
            assets: [
              {
                video: {
                  url: "https://example.com/video.mp4"
                  metadata: { thumbnailOffset: 2000 }
                }
              }
            ]
          }
        ) {
          ... on PostActionSuccess {
            post {
              id
              text
              assets {
                source
              }
            }
          }
          ... on MutationError {
            message
          }
        }
      }
      `,
    }),
  });

  const data = await response.json();
  console.log(JSON.stringify(data, null, 2));
}

createPost();
```

Copy Copied! 
```
import requests

query = """
mutation CreatePost {
  createPost(
    input: {
      text: "Hello there, this is another one!"
      channelId: "some_channel_id"
      schedulingType: automatic
      mode: addToQueue
      assets: [
        {
          video: {
            url: "https://example.com/video.mp4"
            metadata: { thumbnailOffset: 2000 }
          }
        }
      ]
    }
  ) {
    ... on PostActionSuccess {
      post {
        id
        text
        assets {
          source
        }
      }
    }
    ... on MutationError {
      message
    }
  }
}
"""

response = requests.post(
    "https://api.buffer.com",
    headers={
        "Content-Type": "application/json",
        "Authorization": "Bearer YOUR_API_KEY",
    },
    json={
        "query": query,
    },
)

data = response.json()
print(data)
```

Copy Copied! 
```
<?php

$query = '
mutation CreatePost {
  createPost(
    input: {
      text: "Hello there, this is another one!"
      channelId: "some_channel_id"
      schedulingType: automatic
      mode: addToQueue
      assets: [
        {
          video: {
            url: "https://example.com/video.mp4"
            metadata: { thumbnailOffset: 2000 }
          }
        }
      ]
    }
  ) {
    ... on PostActionSuccess {
      post {
        id
        text
        assets {
          source
        }
      }
    }
    ... on MutationError {
      message
    }
  }
}
';

$payload = [
    'query' => $query,
];

$ch = curl_init('https://api.buffer.com');
curl_setopt_array($ch, [
    CURLOPT_POST => true,
    CURLOPT_HTTPHEADER => [
        'Content-Type: application/json',
        'Authorization: Bearer YOUR_API_KEY',
    ],
    CURLOPT_POSTFIELDS => json_encode($payload),
    CURLOPT_RETURNTRANSFER => true,
]);

$response = curl_exec($ch);
curl_close($ch);

$data = json_decode($response, true);
print_r($data);
```

`Esc`
`↑``↓` Navigate `Enter` Open `Esc` Close

