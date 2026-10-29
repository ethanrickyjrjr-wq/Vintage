[![Meta](https://static.xx.fbcdn.net/rsrc.php/y9/r/tL_v571NdZ0.svg)](https://developers.facebook.com/)
Build with us
[Docs](https://developers.facebook.com/docs/)
[Blog](https://developers.facebook.com/blog/)
Resources
Developer centers
[Login](https://business.facebook.com/business/loginpage/?next=https%3A%2F%2Fdevelopers.facebook.com%2Fdocumentation%2Fthreads%2Fposts)
Threads
Threads
[Threads API](https://developers.facebook.com/documentation/threads)
[Overview](https://developers.facebook.com/documentation/threads/overview)
[Get Started](https://developers.facebook.com/documentation/threads/posts)
[Get Started](https://developers.facebook.com/documentation/threads/get-started)
[Create an app](https://developers.facebook.com/documentation/threads/get-started/create-an-app)
[Get Access Tokens](https://developers.facebook.com/documentation/threads/get-started/get-access-tokens-and-permissions)
[Long-Lived Tokens](https://developers.facebook.com/documentation/threads/get-started/long-lived-tokens)
[App Access Tokens](https://developers.facebook.com/documentation/threads/get-started/app-access-tokens)
[Create Posts](https://developers.facebook.com/documentation/threads/posts)
[Create Posts](https://developers.facebook.com/documentation/threads/create-posts)
[Posts](https://developers.facebook.com/documentation/threads/posts)
[Create Replies](https://developers.facebook.com/documentation/threads/retrieve-and-manage-replies/create-replies)
[Reposts](https://developers.facebook.com/documentation/threads/posts/reposts)
[Quote Posts](https://developers.facebook.com/documentation/threads/posts/quote-posts)
[Ghost Posts](https://developers.facebook.com/documentation/threads/create-posts/ghost-posts)
[Polls](https://developers.facebook.com/documentation/threads/create-posts/polls)
[Spoilers](https://developers.facebook.com/documentation/threads/create-posts/spoilers)
[Text Attachments](https://developers.facebook.com/documentation/threads/create-posts/text-attachments)
[Share to Instagram Stories](https://developers.facebook.com/documentation/threads/create-posts/share-to-ig-stories)
[Location Tagging](https://developers.facebook.com/documentation/threads/create-posts/location-tagging)
[Geo-Gated Content](https://developers.facebook.com/documentation/threads/posts/geo-gating)
[Accessibility](https://developers.facebook.com/documentation/threads/posts/accessibility)
[Retrieve and Discover Posts](https://developers.facebook.com/documentation/threads/posts)
[Retrieve and Discover Posts](https://developers.facebook.com/documentation/threads/retrieve-and-discover-posts)
[Retrieve User Posts](https://developers.facebook.com/documentation/threads/retrieve-and-discover-posts/retrieve-posts)
[Mentions](https://developers.facebook.com/documentation/threads/threads-mentions)
[Keyword Search](https://developers.facebook.com/documentation/threads/keyword-search)
[Retrieve and Manage Replies](https://developers.facebook.com/documentation/threads/posts)
[Retrieve and Manage Replies](https://developers.facebook.com/documentation/threads/retrieve-and-manage-replies)
[Retrieve Replies](https://developers.facebook.com/documentation/threads/retrieve-and-manage-replies/retrieve-replies)
[Replies and Conversions](https://developers.facebook.com/documentation/threads/retrieve-and-manage-replies/replies-and-conversations)
[Reply Management](https://developers.facebook.com/documentation/threads/reply-management)
[Delete Posts](https://developers.facebook.com/documentation/threads/posts/delete-posts)
[Profiles](https://developers.facebook.com/documentation/threads/threads-profiles)
[Insights](https://developers.facebook.com/documentation/threads/insights)
[Webhooks](https://developers.facebook.com/documentation/threads/webhooks)
[oEmbed](https://developers.facebook.com/documentation/threads/tools-and-resources/embed-a-threads-post)
[Web Intents](https://developers.facebook.com/documentation/threads/threads-web-intents)
[Troubleshooting](https://developers.facebook.com/documentation/threads/posts)
[Troubleshooting](https://developers.facebook.com/documentation/threads/troubleshooting)
[Debug Access Token](https://developers.facebook.com/documentation/threads/troubleshooting/debug-access-token)
[Reference](https://developers.facebook.com/documentation/threads/posts)
[Reference](https://developers.facebook.com/documentation/threads/reference)
[Publishing](https://developers.facebook.com/documentation/threads/reference/publishing)
[Media Retrieval](https://developers.facebook.com/documentation/threads/reference/media-retrieval)
[Reply Management](https://developers.facebook.com/documentation/threads/reference/reply-management)
[User](https://developers.facebook.com/documentation/threads/reference/user)
[Locations](https://developers.facebook.com/documentation/threads/reference/locations)
[Location Search](https://developers.facebook.com/documentation/threads/reference/location-search)
[Insights](https://developers.facebook.com/documentation/threads/reference/insights)
[oEmbed](https://developers.facebook.com/documentation/threads/reference/oembed)
[Debug](https://developers.facebook.com/documentation/threads/reference/debug)
[Tools and Resources](https://developers.facebook.com/documentation/threads/posts)
[Tools and Resources](https://developers.facebook.com/documentation/threads/tools-and-resources)
[Postman Collection](https://developers.facebook.com/documentation/threads/tools-and-resources/postman-collection)
[Changelog](https://developers.facebook.com/documentation/threads/changelog)
* * *
Resources
[Changelog](https://developers.facebook.com/documentation/threads/changelog/)
[Docs](https://developers.facebook.com/docs)
[Overview](https://developers.facebook.com/documentation/threads)
Threads Posts
# Threads Posts
Updated: Oct 13, 2026
Copy for LLM
[View as Markdown](https://developers.facebook.com/documentation/threads/posts.md)
You can use the Threads API to publish image, video, text, or carousel posts.
This document covers:
  * [Single Thread Posts](https://developers.facebook.com/documentation/threads/posts#single-thread-posts)
  * [Carousel Posts](https://developers.facebook.com/documentation/threads/posts#carousel-posts)
  * [Topic Tags, Links, and GIFs](https://developers.facebook.com/documentation/threads/posts#topic-tags--links--and-gifs)
  * [Media Specifications](https://developers.facebook.com/documentation/threads/posts#media-specifications)


## Permissions
Publishing posts requires the following permissions:
  * `threads_basic` — Required for making any calls to all Threads API endpoints.
  * `threads_content_publish` — Required for Threads publishing endpoints only.


If your app has not been approved for advanced access for the `threads_content_publish` permission, you can only post on behalf of [Threads testers](https://developers.facebook.com/documentation/threads/get-started#threads-testers) on your app. After your app is published and approved, you can post on behalf of any Threads user who grants your app the permission.
## Single thread posts
Publishing a single image, video, or text post is a two-step process:
  1. Create a media container with text only or with an image or video hosted on your public server with optional text using the `POST /{threads-user-id}/threads` endpoint.
  2. Publish the media container using the `POST /{threads-user-id}/threads_publish` endpoint.


### Limitations
  * Text posts are limited to 500 characters.
  * Emojis are counted as the [number of UTF-8 bytes⁠](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2Fgrapheme-splitter&h=AUCVHuPfC5UTMDwyAm9oP5AEnTtDyz4SNpiBMgU1ynkKIXDV-vPAvojLwg_AekqsivpH5ffAclIBziFBHyk_yzVJ3Ucxy5CrX2n8cSLjbx4aQ_N1Csyxqw7ox7xFJqtqRtt_2LkwKx7U4w).


### Step 1: Create a Threads media container
Use the `POST /{threads-user-id}/threads` endpoint to create a Threads media container.
#### Parameters  
|  Name   |  Description   |  
| --- | --- |  
|  `is_carousel_item` Boolean   |  **Required.**  
Indicates that images and/or videos will appear in a carousel. **Values:** `true`, `false` (_default_ for single thread posts)  |  
|  `media_type` string   |  **Required.**  
Indicates the current media type. **Values:** `TEXT`, `IMAGE`, `VIDEO` **Note:** `CAROUSEL` is not available for single thread posts.  |  
|  `image_url` URL   |  **Optional. Required for`media_type=IMAGE`.**  
The URL path to the image. **Note:** Threads retrieves your image from the URL provided, so it must be on a public server.  |  
|  `video_url` URL   |  **Optional. Required for`media_type=VIDEO`.**  
The URL path to the video. **Note:** Threads retrieves your video from the URL provided, so it must be on a public server.  |  
|  `text` string   |  **Optional. Required for`media_type=TEXT`.**  
The text associated with the post. If any URLs are included, the first URL in the `text` field will be used as the link preview for the post. **Note:** For the post character limit, emojis are counted as the [number of UTF-8 bytes⁠](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2Fgrapheme-splitter&h=AUCVHuPfC5UTMDwyAm9oP5AEnTtDyz4SNpiBMgU1ynkKIXDV-vPAvojLwg_AekqsivpH5ffAclIBziFBHyk_yzVJ3Ucxy5CrX2n8cSLjbx4aQ_N1Csyxqw7ox7xFJqtqRtt_2LkwKx7U4w).  |  
Refer to the [`POST /{threads-user-id}/threads` endpoint reference](https://developers.facebook.com/documentation/threads/reference/publishing#post---threads-user-id--threads) for additional supported parameters.
#### Example request

```


```
curl -i -X POST \
  -d "media_type=IMAGE" \
  -d "image_url=<IMAGE_URL>" \
  -d "text=<TEXT>" \
  -d "access_token=<ACCESS_TOKEN>" \
"https://graph.threads.com/v1.0/<THREADS_USER_ID>/threads"
```


```

#### Example response

```


```
{
  "id": "<THREADS_MEDIA_CONTAINER_ID>"
}
```


```

### Step 2: Publish the Threads media container
Use the `POST /{threads-user-id}/threads_publish` endpoint to publish the media container ID returned in the previous step.
It is recommended to wait on average 30 seconds before publishing a Threads media container to give our server enough time to fully process the upload. See the [media container status endpoint](https://developers.facebook.com/documentation/threads/troubleshooting#publishing-does-not-return-a-media-id) for more details.
#### Parameters  
|  Name   |  Description   |  
| --- | --- |  
|  `creation_id` int   |  **Required.**  
The Threads media container ID.  |  
#### Example request

```


```
curl -i -X POST \
  -d "creation_id=<MEDIA_CONTAINER_ID>" \
  -d "access_token=<ACCESS_TOKEN>" \
"https://graph.threads.com/v1.0/<THREADS_USER_ID>/threads_publish"
```


```

#### Example response

```


```
{
  "id": "<THREADS_MEDIA_ID>"
}
```


```

## Carousel posts
You may publish up to 20 images, videos, or a mix of the two in a carousel post. Publishing carousels is a three-step process:
  1. Create the individual media containers for each image and video that should appear in the carousel using the `POST /{threads-user-id}/threads` endpoint.
  2. Create a single carousel container to contain the media containers using the `POST /{threads-user-id}/threads` endpoint.
  3. Publish the carousel container using the `POST /{threads-user-id}/threads_publish` endpoint.


**Note:** Carousel posts count as a single post against a profile’s [rate limit](https://developers.facebook.com/documentation/threads/overview#rate-limiting).
### Limitations
  * Carousels are limited to 20 images, videos, or a mix of the two.
  * Carousels require a minimum of two children.


### Step 1: Create a media container
Use the `POST /{threads-user-id}/threads` endpoint to create a media container for each of the images and/or videos that will appear in the carousel.
#### Parameters  
|  Name   |  Description   |  
| --- | --- |  
|  `is_carousel_item` Boolean   |  **Required.**  
Indicates that images and/or videos will appear in a carousel when set to `true`. **Values:** `true`, `false`  |  
|  `media_type` string   |  **Required.**  
Indicates the current media type. **Values:** `IMAGE`, `VIDEO` **Note:** `CAROUSEL` is not available for single thread posts.  |  
|  `image_url` URL   |  **Optional. Required for`media_type=IMAGE`.**  
The URL path to the image. **Note:** Threads retrieves your image from the URL provided, so it must be on a public server.  |  
|  `video_url` URL   |  **Optional. Required for`media_type=VIDEO`.**  
The URL path to the video. **Note:** Threads retrieves your video from the URL provided, so it must be on a public server.  |  
|  `text` string   |  **Optional.**  
The text associated with the post. If any URLs are included, the first URL in the `text` field will be used as the link preview for the post. **Note:** For the post character limit, emojis are counted as the [number of UTF-8 bytes⁠](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2Fgrapheme-splitter&h=AUCVHuPfC5UTMDwyAm9oP5AEnTtDyz4SNpiBMgU1ynkKIXDV-vPAvojLwg_AekqsivpH5ffAclIBziFBHyk_yzVJ3Ucxy5CrX2n8cSLjbx4aQ_N1Csyxqw7ox7xFJqtqRtt_2LkwKx7U4w).  |  
Refer to the [`POST /{threads-user-id}/threads` endpoint reference](https://developers.facebook.com/documentation/threads/reference/publishing#post---threads-user-id--threads) for additional supported parameters.
#### Example request

```


```
curl -i -X POST \
  -d "image_url=<IMAGE_URL>" \
  -d "is_carousel_item=true" \
  -d "access_token=<ACCESS_TOKEN>" \
"https://graph.threads.com/v1.0/<THREADS_USER_ID>/threads"
```


```

#### Example response

```


```
{
  "id": "<THREADS_MEDIA_CONTAINER_ID>"
}
```


```

If the operation is successful, the API will return a media container ID, which can be used when creating the carousel container.
Repeat this process for each image and/or video that will appear in the carousel.
### Step 2: Create a carousel container
Use the `POST /{threads-user-id}/threads` endpoint to create a carousel container.
#### Parameters  
|  Name   |  Description   |  
| --- | --- |  
|  `media_type` string   |  **Required.**  
Indicates the current media type. **Value:** `CAROUSEL`  |  
|  `children` list<int>  |  **Required.**  
A comma-separated list of the media container IDs of the images and/or videos that should appear in the published carousel. **Note:** Carousels must have at least 2 and no more than 20 total images, videos, or a mix of the two.  |  
|  `text` string   |  **Optional.**  
The text associated with the post.  |  
Refer to the [`POST /{threads-user-id}/threads` endpoint reference](https://developers.facebook.com/documentation/threads/reference/publishing#post---threads-user-id--threads) for additional supported parameters.
#### Example request

```


```
curl -i -X POST \
  -d "media_type=CAROUSEL" \
  -d "children=<MEDIA_ID_1>,<MEDIA_ID_2>,<MEDIA_ID_3>,..." \
  -d "access_token=<ACCESS_TOKEN>" \
"https://graph.threads.com/v1.0/<THREADS_USER_ID>/threads"
```


```

#### Example response

```


```
{
  "id": "<THREADS_CAROUSEL_CONTAINER_ID>"
}
```


```

### Step 3: Publish the carousel container
Use the `POST /{threads-user-id}/threads_publish` endpoint to publish a carousel post.
**Note:** Profiles are limited to 250 published posts within a 24-hour period. Publishing a carousel counts as a single post.
#### Parameters  
|  Name   |  Description   |  
| --- | --- |  
|  `creation_id` int   |  **Required.**  
The Threads carousel container ID.  |  
#### Example request

```


```
curl -i -X POST \
  -d "creation_id=<MEDIA_CONTAINER_ID>" \
  -d "access_token=<ACCESS_TOKEN>" \
"https://graph.threads.com/v1.0/<THREADS_USER_ID>/threads_publish"
```


```

#### Example response

```


```
{
  "id": "<THREADS_MEDIA_ID>"
}
```


```

If the operation is successful, the API will return the carousel album’s Threads media ID.
## Topic tags, links, and GIFs
Topics and links appear in posts in such a way as to encourage engagement.
### Topic tags
Topics make posts more social by allowing central topics of discussion. You can include a topic in a post either by using the `topic_tag` parameter or by including a tag within the text of a post.
#### Using the `topic_tag` parameter
**Note:** Topic tags must be at least 1 character and no more than 50 characters long. The following characters are not allowed:
  * Periods (.)
  * Ampersands (&)


##### Example request

```


```
curl -i -X POST \
  -d "media_type=TEXT" \
  -d "text=<Text>" \
  -d "access_token=<ACCESS_TOKEN>" \
  -d "topic_tag=<TAG>" \
"https://graph.threads.com/v1.0/<THREADS_USER_ID>/threads"
```


```

#### Using an in-text topic tag
This method is not preferred but is kept for backward compatibility.
A topic can also be attached to a post by including it in-line within the text of the post. Only one topic tag is allowed per post, so the first valid tag included in a post of any type (text-only, image, video, carousel) via the API is treated as the tag for that post.
Information to keep in mind when adding a topic to a post using an in-text tag:
  * Valid tags start with a hash sign (#).
  * The text is also configured in the app without the hash sign.
  * Topic must be at least 1 character and no more than 50 characters long.
  * Whole numbers that are preceded by a hash sign (i.e., #1) will not be converted into a tag. This is because it is assumed that # is signifying a number sign in this scenario.
  * The following characters are not allowed when using in-text tags with the Threads API, so any in-text tag that starts with a hash sign will end just before these characters:
  * Spaces, Tabs, New Line Characters
  * Periods (.)
  * Ampersands (&)
  * At Signs (@)
  * Exclamation Marks (!)
  * Question Marks (?)
  * Commas (,)
  * Semi-Colons (;)
  * Colons (:)


### Links
To attach a link to your post, use the `link_attachment` parameter when creating a media container. If no `link_attachment` parameter is provided, then the first link made in a text-only post via the API is configured as the link attachment, which displays as a preview card, to make it easier to engage with and click on.
#### Limitations
  * This feature is only available for text-only posts. It will not work with image, video, or carousel posts.
  * The number of links is restricted to 5 or fewer.


Starting December 22, 2025, Threads posts containing more than 5 links will fail to post during the media creation step (`POST /{threads-user-id}/threads`) with the error code: `THREADS_API__LINK_LIMIT_EXCEEDED`.
How links are counted:
  * All unique URLs found in the text field are counted as links.
  * If the `link_attachment` field contains a URL that is different from all URLs in the text field, it is counted as an additional link.
  * If the `link_attachment` URL is the same as any URL in the text field, it is only counted once, rather than twice.


Examples:
  * If the `text` field contains only www.facebook.com, and the `link_attachment` is also www.facebook.com, this counts as 1 link.
  * If the `text` field contains www.instagram.com and www.threads.com, and the `link_attachment` is www.facebook.com, this counts as 3 links.
  * If the `text` field contains www.example.com, www.example.com, and www.test.com, and the `link_attachment` is www.test.com, this counts as 2 links (www.example.com and www.test.com are each counted once).


If you receive this error, reduce the number of unique links in your post to 5 or fewer.
#### Publishing
Links can be attached when making an API call to the `POST /{threads-user-id}/threads` endpoint to [create a media container](https://developers.facebook.com/documentation/threads/posts#step-1--create-a-threads-media-container).  
|  Name   |  Description   |  
| --- | --- |  
|  `link_attachment` URL   |  **Optional.**  
The URL that should be attached to a Threads post and displayed as a link preview. This must be a valid, publicly accessible URL. **Note:** Can only be used for `media_type=TEXT` posts.  |  
##### Example request

```


```
curl -i -X POST \
  -d "media_type=TEXT" \
  -d "text=<TEXT>" \
  -d "access_token=<ACCESS_TOKEN>" \
  -d "link_attachment=<URL> \
"https://graph.threads.com/v1.0/<THREADS_USER_ID>/threads"
```


```

##### Example response

```


```
{
  "id": "<THREADS_MEDIA_CONTAINER_ID>"
}
```


```

The request above creates a Threads media container that, once [published](https://developers.facebook.com/documentation/threads/posts#step-2--publish-a-threads-media-container), will attach a link preview to your media.
#### Media Retrieval
The value for the `link_attachment` URL can be retrieved by making a request to the `GET /threads` or `GET /{threads_media_id}` endpoint to [retrieve media object(s)](https://developers.facebook.com/documentation/threads/retrieve-and-discover-posts/retrieve-posts).  
|  Name   |  Description   |  
| --- | --- |  
|  `link_attachment_url` URL   | The URL attached to a Threads post.  |  
##### Example request

```


```
curl -s -X GET \
"https://graph.threads.com/v1.0/<THREADS_MEDIA_ID>?fields=id,link_attachment_url&access_token=<ACCESS_TOKEN>"
```


```

##### Example response

```


```
{
   "id": "<THREADS_MEDIA_ID>",
   "link_attachment_url": "<LINK_ATTACHMENT_URL>",
}
```


```

### GIFs
GIFs make posts more engaging by allowing users to express reactions, emotions, or ideas visually.
#### Limitations
  * This feature is only available for text-only posts. It will not work on image, video, or carousel posts.
  * [GIPHY⁠](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.giphy.com%2Fdocs%2Fapi&h=AUCVHuPfC5UTMDwyAm9oP5AEnTtDyz4SNpiBMgU1ynkKIXDV-vPAvojLwg_AekqsivpH5ffAclIBziFBHyk_yzVJ3Ucxy5CrX2n8cSLjbx4aQ_N1Csyxqw7ox7xFJqtqRtt_2LkwKx7U4w) is currently the only available GIF provider.


#### Publishing
GIFS can be attached when making an API call to the `POST /{threads-user-id}/threads` endpoint to [create a media container](https://developers.facebook.com/documentation/threads/posts#step-1--create-a-threads-media-container).  
|  Name   |  Description   |  
| --- | --- |  
|  `gif_attachment` object   |  **Optional.**  
The ID and GIF provider for the GIF to attach to the post. **Fields:** `gif_id`, `provider`  |  
##### Example request

```


```
curl -i -X POST \
  -d "media_type=TEXT" \
  -d "text=<Text> \
  -d "access_token=<ACCESS_TOKEN>" \
  -d "gif_attachment={"gif_id":"<GIF_ID>","provider":"GIPHY"}" \
"https://graph.threads.com/v1.0/<THREADS_USER_ID>/threads"
```


```

**Note:** The value of the `id` field you receive from the GIF provider’s API response should be used as the `<GIF_ID>` in the API call.
##### Example response

```


```
{
 "id": "<THREADS_MEDIA_ID>"
}
```


```

The request above creates a Threads media container that, once [published](https://developers.facebook.com/documentation/threads/posts#step-2--publish-a-threads-media-container), will attach a GIF to your media.
## Media Specifications
### Image Specifications
  * **Format:** JPEG and PNG image types are the officially supported formats for image posts.
  * **File Size:** 8 MB maximum.
  * **Aspect Ratio Limit:** 10:1
  * **Minimum Width:** 320 (will be scaled up to the minimum if necessary)
  * **Maximum Width:** 1440 (will be scaled down to the maximum if necessary)
  * **Height:** Varies (depending on width and aspect ratio)
  * **Color Space:** sRGB. Images using other color spaces will have their color spaces converted to sRGB.


### Video Specifications
  * **Container:** MOV or MP4 (MPEG-4 Part 14), no edit lists, moov atom at the front of the file.
  * **Audio Codec:** AAC, 48khz sample rate maximum, 1 or 2 channels (mono or stereo).
  * **Video Codec:** HEVC or H264, progressive scan, closed GOP, 4:2:0 chroma subsampling.
  * **Frame Rate:** 23-60 FPS
  * **Picture Size:**
    * Maximum Columns (horizontal pixels): 1920
    * Required aspect ratio is between 0.01:1 and 10:1 but we recommend 9:16 to avoid cropping or blank space.
  * **Video Bitrate:** VBR, 100 Mbps maximum.
  * **Audio Bitrate:** 128 kbps.
  * **Duration:** 300 seconds (5 minutes) maximum, minimum longer than 0 seconds.
  * **File Size:** 1 GB maximum.


## Learn more
  * [Reposts](https://developers.facebook.com/documentation/threads/posts/reposts)
  * [Quote Posts](https://developers.facebook.com/documentation/threads/posts/quote-posts)
  * [Polls](https://developers.facebook.com/documentation/threads/create-posts/polls)
  * [Spoilers](https://developers.facebook.com/documentation/threads/create-posts/spoilers)
  * [Text Attachments](https://developers.facebook.com/documentation/threads/create-posts/text-attachments)


* * *
* * *
![Meta](https://static.xx.fbcdn.net/rsrc.php/y9/r/tL_v571NdZ0.svg)
[![Facebook](https://scontent-mia5-1.xx.fbcdn.net/v/t39.2365-6/425860105_925920989121941_6933048753023841367_n.svg?_nc_cat=1&ccb=1-7&_nc_sid=aa6a2f&_nc_ohc=ae5txUzRuuYQ7kNvwHC0XyY&_nc_oc=Adr8veNI20SUSJDzX_Z51cCxhhYGaGpxFPX9xQA1lJxzRob8b9OD_uclUGANsIP-EEM&_nc_zt=14&_nc_ht=scontent-mia5-1.xx&_nc_gid=7VV_Fp867VTdY96LNdDsvg&_nc_ss=7b289&oh=00_AQTt0HRaklfuo6DOJnqHWQpPKYlJnqhc7q1QKRi_bpzPFg&oe=6AE954A2)](https://www.facebook.com/MetaforDevelopers)[![Instagram](https://scontent-mia3-3.xx.fbcdn.net/v/t39.2365-6/425804778_757649995874129_6917476492193301523_n.svg?_nc_cat=108&ccb=1-7&_nc_sid=aa6a2f&_nc_ohc=3TM3ED2Lx2gQ7kNvwEVEV2E&_nc_oc=AdqW-kwhO6AEf3rBtpDNMuvYufNQLZzX2ingBmNiAR20r_r30wikMwhIGY92cy-K9LA&_nc_zt=14&_nc_ht=scontent-mia3-3.xx&_nc_gid=7VV_Fp867VTdY96LNdDsvg&_nc_ss=7b289&oh=00_AQTfIgCEbaxtlCp2b8plbZIm4x8-Jg5BAjKz6S75jcsB8g&oe=6AE93EB8)](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.instagram.com%2Fmetafordevelopers%2F&h=AUCVHuPfC5UTMDwyAm9oP5AEnTtDyz4SNpiBMgU1ynkKIXDV-vPAvojLwg_AekqsivpH5ffAclIBziFBHyk_yzVJ3Ucxy5CrX2n8cSLjbx4aQ_N1Csyxqw7ox7xFJqtqRtt_2LkwKx7U4w)[![X](https://scontent-mia5-1.xx.fbcdn.net/v/t39.2365-6/426747931_385023204117867_5811151062540225287_n.svg?_nc_cat=1&ccb=1-7&_nc_sid=aa6a2f&_nc_ohc=Xe5MMfN34ssQ7kNvwEwfjeY&_nc_oc=AdoITz2Q-FwhJ-VIlzRxMM2rEzmshnHlWUMCRiHu8360qbjf8GocpVE7wsFXCZtCgSk&_nc_zt=14&_nc_ht=scontent-mia5-1.xx&_nc_gid=7VV_Fp867VTdY96LNdDsvg&_nc_ss=7b289&oh=00_AQREDn8Y52AwmLWgBW3xlper9v-rNcjXaOOj8Vbg2R8V5w&oe=6AE95D2A)](https://l.facebook.com/l.php?u=https%3A%2F%2Ftwitter.com%2Fmetafordevs&h=AUCVHuPfC5UTMDwyAm9oP5AEnTtDyz4SNpiBMgU1ynkKIXDV-vPAvojLwg_AekqsivpH5ffAclIBziFBHyk_yzVJ3Ucxy5CrX2n8cSLjbx4aQ_N1Csyxqw7ox7xFJqtqRtt_2LkwKx7U4w)[![LinkedIn](https://scontent-mia3-2.xx.fbcdn.net/v/t39.2365-6/467689750_1684384502343829_7561568713040200172_n.svg?_nc_cat=103&ccb=1-7&_nc_sid=aa6a2f&_nc_ohc=ysnjNBowAQUQ7kNvwH52CpT&_nc_oc=AdqCd0G3oGEQOTelp2T5pGHqvpwBNnezdIT_cgGyxnsg3XcizKgjt92ykj1EXXcWhSQ&_nc_zt=14&_nc_ht=scontent-mia3-2.xx&_nc_gid=7VV_Fp867VTdY96LNdDsvg&_nc_ss=7b289&oh=00_AQR1ftIGajO5Km8UI_BBz8TTj7-pFanZ6bW-p6qLU3x6Tg&oe=6AE96CBE)](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.linkedin.com%2Fshowcase%2Fmeta-for-developers%2F&h=AUCVHuPfC5UTMDwyAm9oP5AEnTtDyz4SNpiBMgU1ynkKIXDV-vPAvojLwg_AekqsivpH5ffAclIBziFBHyk_yzVJ3Ucxy5CrX2n8cSLjbx4aQ_N1Csyxqw7ox7xFJqtqRtt_2LkwKx7U4w)[![YouTube](https://scontent-mia5-1.xx.fbcdn.net/v/t39.2365-6/425519002_724756916408357_7491658959807896355_n.svg?_nc_cat=1&ccb=1-7&_nc_sid=aa6a2f&_nc_ohc=oG_Saoc72KsQ7kNvwHhe09m&_nc_oc=Adqmadw82MDErKrFaafimlzWlMGUhE9M8yfZfOVvk_tiCrAL3qez5SY61T_-JhrHbjU&_nc_zt=14&_nc_ht=scontent-mia5-1.xx&_nc_gid=7VV_Fp867VTdY96LNdDsvg&_nc_ss=7b289&oh=00_AQQpYKPyT1mIJunbWgF6sBU1uXWmWow-Hn7Sntm7WuAvJw&oe=6AE957DF)](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.youtube.com%2FMetaDevelopers%2F&h=AUCVHuPfC5UTMDwyAm9oP5AEnTtDyz4SNpiBMgU1ynkKIXDV-vPAvojLwg_AekqsivpH5ffAclIBziFBHyk_yzVJ3Ucxy5CrX2n8cSLjbx4aQ_N1Csyxqw7ox7xFJqtqRtt_2LkwKx7U4w)
Build with Meta
Build with Meta
[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F&h=AUCVHuPfC5UTMDwyAm9oP5AEnTtDyz4SNpiBMgU1ynkKIXDV-vPAvojLwg_AekqsivpH5ffAclIBziFBHyk_yzVJ3Ucxy5CrX2n8cSLjbx4aQ_N1Csyxqw7ox7xFJqtqRtt_2LkwKx7U4w)
[Meta Horizon ](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F&h=AUCVHuPfC5UTMDwyAm9oP5AEnTtDyz4SNpiBMgU1ynkKIXDV-vPAvojLwg_AekqsivpH5ffAclIBziFBHyk_yzVJ3Ucxy5CrX2n8cSLjbx4aQ_N1Csyxqw7ox7xFJqtqRtt_2LkwKx7U4w)
[Social technologies](https://developers.facebook.com/social-technologies/)
[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F&h=AUCVHuPfC5UTMDwyAm9oP5AEnTtDyz4SNpiBMgU1ynkKIXDV-vPAvojLwg_AekqsivpH5ffAclIBziFBHyk_yzVJ3Ucxy5CrX2n8cSLjbx4aQ_N1Csyxqw7ox7xFJqtqRtt_2LkwKx7U4w)
* * *
News
News
[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F&h=AUCVHuPfC5UTMDwyAm9oP5AEnTtDyz4SNpiBMgU1ynkKIXDV-vPAvojLwg_AekqsivpH5ffAclIBziFBHyk_yzVJ3Ucxy5CrX2n8cSLjbx4aQ_N1Csyxqw7ox7xFJqtqRtt_2LkwKx7U4w)
[Blog](https://developers.facebook.com/blog/)
[Success stories](https://developers.facebook.com/success-stories/)
* * *
Support
Support
[Developer Support](https://developers.facebook.com/support/)
[Bug tool](https://developers.facebook.com/support/bugs/)
[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F&h=AUCVHuPfC5UTMDwyAm9oP5AEnTtDyz4SNpiBMgU1ynkKIXDV-vPAvojLwg_AekqsivpH5ffAclIBziFBHyk_yzVJ3Ucxy5CrX2n8cSLjbx4aQ_N1Csyxqw7ox7xFJqtqRtt_2LkwKx7U4w)
[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)
[Report an incident](https://developers.facebook.com/incident/report/)
* * *
About us
About us
[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AUCVHuPfC5UTMDwyAm9oP5AEnTtDyz4SNpiBMgU1ynkKIXDV-vPAvojLwg_AekqsivpH5ffAclIBziFBHyk_yzVJ3Ucxy5CrX2n8cSLjbx4aQ_N1Csyxqw7ox7xFJqtqRtt_2LkwKx7U4w)
[Careers](https://www.facebook.com/careers)
* * *
Terms and policies
Terms and policies
[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)
[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)
[Developer policies](https://developers.facebook.com/devpolicy/)
[Privacy policy](https://www.facebook.com/about/privacy)
[Cookies](https://www.facebook.com/help/cookies)
* * *
English (US)

