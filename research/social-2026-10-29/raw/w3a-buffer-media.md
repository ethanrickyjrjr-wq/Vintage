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
Core ConceptsHosting Media
# Hosting Media
Copy Page
Ask AI assistant Chat with the docs AI assistant Copy page Copy this page as Markdown View as Markdown Open this page as plain Markdown Open in Claude Ask Claude about this page Open in ChatGPT Ask ChatGPT about this page Open in Perplexity Ask Perplexity about this page
When you attach an image, video, or document to a post, the Buffer API doesn't accept a file upload - there's no upload endpoint. Instead, you host the file yourself and pass a publicly accessible URL in the `assets` array. The thumbnail on a link attachment works the same way.
## Why media must be hosted[](https://developers.buffer.com/guides/hosting-media.html#why-media-must-be-hosted)
The `url` field on each asset (`image`, `video`, or `document`) must point to a file that is reachable over the public internet without authentication.
This means the URL must work for anyone, not just you. Links that require a viewer to be signed in - for example a Google Drive or Dropbox "share" link - will not work.
Some assets take more than one URL. A document needs both the file and a thumbnail, and a link attachment can carry its own thumbnail. Every URL you pass has to meet the same bar, not just the main one.
> **The URL must stay reachable until the post publishes, not just when you create it.** Buffer fetches the media when the post goes out, which for scheduled or queued posts can be hours or days later. Avoid expiring or signed URLs (such as S3 pre-signed links or Cloudinary signed-delivery URLs) - they often work the moment you call `createPost` but expire before the post publishes, causing it to fail silently. Use a stable, permanent URL.
## Where to host your media[](https://developers.buffer.com/guides/hosting-media.html#where-to-host-your-media)
You can use any host that serves files at a direct, public URL. If you don't already have one, these options have a free tier and work well:
  * [Cloudinary](https://cloudinary.com/) - A media management platform with a generous free tier. After you upload a file you get a direct, publicly accessible URL you can use right away. It also offers optional on-the-fly image and video transformations. Use the delivery URL (e.g. `https://res.cloudinary.com/...`), not the link to the dashboard or media-library page.
  * [Cloudflare R2](https://www.cloudflare.com/developer-platform/products/r2/) - Object storage with a free tier. A good fit if you already use Cloudflare or are comfortable with a slightly more technical setup. Upload your file and enable public access on the bucket (or attach a public custom domain) so the file is reachable without credentials.


## Verifying that a URL works[](https://developers.buffer.com/guides/hosting-media.html#verifying-that-a-url-works)
Before using a URL with the API, open it in a private/incognito browser window:
  * If the file loads directly without asking you to log in, it will work with the API.
  * If you see a login prompt, a preview page, or an error, the URL won't work - host the file somewhere that serves it directly.


Open your media URL in a private browser window before using it. If it asks for a login or errors, the API can't access it either. Note that some hosts, such as WordPress sites or those using Cloudflare bot protection, may block automated requests even when the file loads in your browser.
A good media URL is:
  * Public - loads without authentication
  * Direct - points straight at the file (not a redirect or preview page)
  * HTTPS - served over `https://`
  * Stable - won't expire before the post publishes


## Using the media URL[](https://developers.buffer.com/guides/hosting-media.html#using-the-media-url)
Once your file is hosted, pass its URL in the `assets` array on `createPost` or `editPost`. `assets` is an ordered list where each entry specifies exactly one asset.
Image - pass the publicly hosted image URL. You can optionally pass `thumbnailUrl` as well, which is a second hosted URL and needs to be just as public and stable as the image itself:
Copy Copied! 
```
assets: [
  {
    image: {
      url: "https://your-host.example.com/photo.jpg"
    }
  }
]
```

Video - pass the publicly hosted video URL. To set the video thumbnail, choose which frame to use with `metadata.thumbnailOffset` (a millisecond offset into the video) on Instagram, TikTok, or Pinterest:
Copy Copied! 
```
assets: [
  {
    video: {
      url: "https://your-host.example.com/clip.mp4"
      metadata: { thumbnailOffset: 2000 }
    }
  }
]
```

Document - pass both the file URL and a thumbnail URL, plus a title. All three are required, so a document post means hosting two files, not one:
Copy Copied! 
```
assets: [
  {
    document: {
      url: "https://your-host.example.com/report.pdf"
      thumbnailUrl: "https://your-host.example.com/report-cover.jpg"
      title: "Q3 report"
    }
  }
]
```

A full mutation looks like this:
Copy Copied! 
```
mutation CreatePost {
  createPost(
    input: {
      text: "Check out our latest update!"
      channelId: "some_channel_id"
      schedulingType: automatic
      mode: addToQueue
      assets: [
        {
          image: {
            url: "https://your-host.example.com/photo.jpg"
          }
        }
      ]
    }
  ) {
    ... on PostActionSuccess {
      post { id }
    }
    ... on MutationError {
      message
    }
  }
}
```

For complete walkthroughs, see the [Create an image post](https://developers.buffer.com/examples/create-image-post.html) and [Create a video post](https://developers.buffer.com/examples/create-video-post.html) examples.
## Link attachments[](https://developers.buffer.com/guides/hosting-media.html#link-attachments)
A link card is not an asset. To attach one, use `metadata.{service}.linkAttachment`, which is supported on Bluesky, Facebook, LinkedIn, Substack, and Threads:
Copy Copied! 
```
metadata: {
  linkedin: {
    linkAttachment: {
      url: "https://example.com/announcement"
      title: "Our latest announcement"
      description: "What we shipped this quarter"
      thumbnail: { url: "https://your-host.example.com/card.jpg" }
    }
  }
}
```

Two things to know:
  * The `thumbnail.url` is fetched by Buffer the same way asset URLs are, so it has to meet every point in the list above. The link's own `url` is the page you're linking to and is not fetched as media.
  * `linkAttachment` is mutually exclusive with a non-empty `assets` array. Passing both is rejected, so a post is either a link card or a media post, never both.


## Troubleshooting[](https://developers.buffer.com/guides/hosting-media.html#troubleshooting)
If a media URL can't be fetched, the mutation returns a `MutationError` with a message:
Copy Copied! 
```
{
  "data": {
    "createPost": {
      "message": "Failed to create post: Failed to fetch image dimensions: Not Found"
    }
  }
}
```

If you hit this, check the URL against this list:
  1. Public - open it in an incognito window; it should load with no login.
  2. Direct - it points at the file itself, not a share, preview, or redirect page.
  3. HTTPS - it's served over `https://`.
  4. Still live - it isn't a signed/expiring URL that may lapse before a scheduled post publishes.


If the post has a document or a link attachment, check the thumbnail URL against the same list. A thumbnail that can't be fetched fails the whole mutation.
[ Previous Content Items ](https://developers.buffer.com/guides/content-items.html) [ Next Tags ](https://developers.buffer.com/guides/tags.html)
On this page
[Why media must be hosted](https://developers.buffer.com/guides/hosting-media.html#why-media-must-be-hosted) [Where to host your media](https://developers.buffer.com/guides/hosting-media.html#where-to-host-your-media) [Verifying that a URL works](https://developers.buffer.com/guides/hosting-media.html#verifying-that-a-url-works) [Using the media URL](https://developers.buffer.com/guides/hosting-media.html#using-the-media-url) [Link attachments](https://developers.buffer.com/guides/hosting-media.html#link-attachments) [Troubleshooting](https://developers.buffer.com/guides/hosting-media.html#troubleshooting)
`Esc`
`↑``↓` Navigate `Enter` Open `Esc` Close

