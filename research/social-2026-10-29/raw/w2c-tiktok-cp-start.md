[![TikTok for Developers](https://sf16-sg.tiktokcdn.com/obj/eden-sg/wv_k4aa/ljhwZthlaukjlkulzlp/doc_station/tt4d_logo_dark.ac59d2631b2b.svg)](https://developers.tiktok.com/)
Products[Docs](https://developers.tiktok.com/docs)[Support](https://developers.tiktok.com/portal/support?origin_site=doc-station)[Blog](https://developers.tiktok.com/blogs)
Get started
# Developer Docs
Share to TikTok/.../Get Started - Direct Post
ENSearch⌘ K
Share to TikTok
  * [Overview](https://developers.tiktok.com/docs/en/content-publishing-landing)
  * [Share Kit](https://developers.tiktok.com/docs/en/share-kit-ios-quickstart-v2)
  * [Content Posting API](https://developers.tiktok.com/docs/en/content-posting-api-get-started)
    * [Get Started - Direct Post](https://developers.tiktok.com/docs/en/content-posting-api-get-started)
    * [Get Started - Upload](https://developers.tiktok.com/docs/en/content-posting-api-get-started-upload-content)
    * [Media Transfer Guide](https://developers.tiktok.com/docs/en/content-posting-api-media-transfer-guide)
    * [API Reference](https://developers.tiktok.com/docs/en/content-posting-api-reference-direct-post)
  * [Green Screen Kit](https://developers.tiktok.com/docs/en/green-screen-kit)


[Share to TikTok](https://developers.tiktok.com/docs/en/content-publishing-landing)/[Content Posting API](https://developers.tiktok.com/docs/en/content-posting-api-get-started)/Get Started - Direct PostShare to TikTok/Content Posting API/Get Started - Direct PostLast updated August 4, 2026
  * [Prerequisites](https://developers.tiktok.com/docs/en/content-posting-api-get-started#prerequisites)
  * [Post directly to TikTok](https://developers.tiktok.com/docs/en/content-posting-api-get-started#post_directly_to_tiktok)
    * [Query Creator Info](https://developers.tiktok.com/docs/en/content-posting-api-get-started#query_creator_info)
    * [Post a video](https://developers.tiktok.com/docs/en/content-posting-api-get-started#post_a_video)
      * [Example](https://developers.tiktok.com/docs/en/content-posting-api-get-started#example)
    * [Post photos](https://developers.tiktok.com/docs/en/content-posting-api-get-started#post_photos)
      * [Example](https://developers.tiktok.com/docs/en/content-posting-api-get-started#example_2)


On this page
# Get Started - Direct Post
  

**Tip** : You can enable [email notifications](https://developers.tiktok.com/settings/#notification-setting) to get our latest product updates.
**New:** Content Posting API now supports [posting photos](https://developers.tiktok.com/docs/en/content-posting-api-reference-photo-post)!
This guide demonstrates how to use the Content Posting API to post content directly to TikTok. 
##  [#](https://developers.tiktok.com/docs/en/content-posting-api-get-started#prerequisites)Prerequisites
To successfully complete this tutorial, you will need the following:
  1. A valid video if you want to post videos:
     * Ensure you have a video file in one of the [supported formats](https://developers.tiktok.com/docs/en/content-posting-api-media-transfer-guide#video_restrictions), such as MP4 + H.264, stored on your local machine.
     * Alternatively, you can provide the URL of a video from your verified domain or URL prefix. Learn how to [verify your domain or URL prefix](https://developers.tiktok.com/docs/en/content-posting-api-media-transfer-guide#pull_from_url).
     * Learn more about [video restrictions](https://developers.tiktok.com/docs/en/content-posting-api-media-transfer-guide#video_restrictions).
  2. A valid photo if you want to post photos:
     * You must provide a URL of a photo from your verified domain or URL prefix. Learn how to [verify your domain or URL prefix](https://developers.tiktok.com/docs/en/content-posting-api-media-transfer-guide#pull_from_url).
     * Learn more about [photo restrictions.](https://developers.tiktok.com/docs/en/content-posting-api-media-transfer-guide#image_restrictions)
  3. A [registered app](https://developers.tiktok.com/docs/en/getting-started-create-an-app) on the TikTok for Developers website.
  4. Add the Content Posting API product to your app as shown below.


![](https://sf16-sg.tiktokcdn.com/obj/tiktok-open-platform-sg/ttop_doc_images/f7e446de7adf4a97a8e606d1db9f0003)
  1. To enable the direct posting of content on authorized users' profiles, you need to enable the Direct Post configuration for the Content Posting API in your app, as shown below.


![](https://sf16-sg.tiktokcdn.com/obj/tiktok-open-platform-sg/ttop_doc_images/78cba97728b274ecdaeefa5e30c34946)
  1. Get approval and authorization of the `video.publish` scope. Learn more about [scopes](https://developers.tiktok.com/docs/en/scopes-overview).
    1. Your app must be approved for the `video.publish` scope.
    2. The target TikTok user must have authorized your app for the `video.publish` scope.
  2. The access token and open ID of the TikTok user who authorized your app. Learn how to [obtain the access token and open ID](https://developers.tiktok.com/docs/en/login-kit-manage-user-access-tokens).


**Note:** All content posted by unaudited clients will be restricted to private viewing mode. Once you have successfully tested your integration, to lift the restrictions on content visibility, your API client must [undergo an audit](https://developers.tiktok.com/application/content-posting-api) to verify compliance with our [Terms of Service](https://www.tiktok.com/legal/tik-tok-developer-terms-of-service?lang=en).
##  [#](https://developers.tiktok.com/docs/en/content-posting-api-get-started#post_directly_to_tiktok)Post directly to TikTok
This section demonstrates how to successfully post a video or photo to a creator's TikTok account. 
###  [#](https://developers.tiktok.com/docs/en/content-posting-api-get-started#query_creator_info)Query Creator Info
To initiate a direct post to a creator's account, you must first use the Query Creator Info endpoint to get the target creator's latest information. For more information about why creator information is necessary, refer to these [UX guidelines](https://developers.tiktok.com/docs/en/content-sharing-guidelines).
Request:

```
curl --location --request POST 'https://open.tiktokapis.com/v2/post/publish/creator_info/query/' \
--header 'Authorization: Bearer act.example12345Example12345Example' \
--header 'Content-Type: application/json; charset=UTF-8'
```

Response:

```
200 OK

{
   "data":{
      "creator_avatar_url": "https://lf16-tt4d.tiktokcdn.com/obj/tiktok-open-platform/8d5740ac3844be417beeacd0df75aef1",
      "creator_username": "tiktok",
      "creator_nickname": "TikTok Official",
      "privacy_level_options": ["PUBLIC_TO_EVERYONE", "MUTUAL_FOLLOW_FRIENDS", "SELF_ONLY"] 
      "comment_disabled": false,
      "duet_disabled": false,
      "stitch_disabled": true,
      "max_video_post_duration_sec": 300
   },
    "error": {
         "code": "ok",
         "message": "",
         "log_id": "202210112248442CB9319E1FB30C1073F3"
     }
```

###  [#](https://developers.tiktok.com/docs/en/content-posting-api-get-started#post_a_video)Post a video
To initiate video upload on TikTok's server, you must invoke the [Direct Post Video](https://developers.tiktok.com/docs/en/content-posting-api-reference-direct-post) endpoint. You have the following two options:
  * If you have the video file locally, set the source parameter to `FILE_UPLOAD` in your request.
  * If the video is hosted on a URL, set the source parameter to `PULL_FROM_URL`.


####  [#](https://developers.tiktok.com/docs/en/content-posting-api-get-started#example)Example
Example using `source=FILE_UPLOAD`:
Request:

```
curl --location 'https://open.tiktokapis.com/v2/post/publish/video/init/' \
--header 'Authorization: Bearer act.example12345Example12345Example' \
--header 'Content-Type: application/json; charset=UTF-8' \
--data-raw '{
  "post_info": {
    "title": "this will be a funny #cat video on your @tiktok #fyp",
    "privacy_level": "MUTUAL_FOLLOW_FRIENDS",
    "disable_duet": false,
    "disable_comment": true,
    "disable_stitch": false,
    "video_cover_timestamp_ms": 1000
  },
  "source_info": {
      "source": "FILE_UPLOAD",
      "video_size": 50000123,
      "chunk_size":  10000000,
      "total_chunk_count": 5
  }
}'
```

Response:

```
200 OK

{
    "data": {
        "publish_id": "v_pub_file~v2-1.123456789",
        "upload_url": "https://open-upload.tiktokapis.com/video/?upload_id=67890&upload_token=Xza123"    
    },
    "error": {
         "code": "ok",
         "message": "",
         "log_id": "202210112248442CB9319E1FB30C1073F3"
     }
}
```

  

Example using `source=PULL_FROM_URL`:
Request:

```
curl --location 'https://open.tiktokapis.com/v2/post/publish/video/init/' \
--header 'Authorization: Bearer act.example12345Example12345Example' \
--header 'Content-Type: application/json; charset=UTF-8' \
--data-raw '{
  "post_info": {
    "title": "this will be a funny #cat video on your @tiktok #fyp",
    "privacy_level": "MUTUAL_FOLLOW_FRIENDS",
    "disable_duet": false,
    "disable_comment": true,
    "disable_stitch": false,
    "video_cover_timestamp_ms": 1000
  },
  "source_info": {
      "source": "PULL_FROM_URL",
      "video_url": "https://example.verified.domain.com/example_video.mp4"
  }
}'
```

Response:

```
200 OK

{
    "data": {
        "publish_id": "v_pub_url~v2.123456789"  
    },
    "error": {
         "code": "ok",
         "message": "",
         "log_id": "202210112248442CB9319E1FB30C1073F4"
     }
}
```

If you are using `source=FILE_UPLOAD`
  1. Extract the `upload_url` and `publish_id` from the response data.
  2. [Send the video ](https://developers.tiktok.com/docs/en/content-posting-api-reference-direct-post)from your local filesystem to the extracted `upload_url` using a PUT request. The video processing will occur asynchronously once the upload is complete.



```
curl --location --request PUT 'https://open-upload.tiktokapis.com/upload/?upload_id=67890&upload_token=Xza123' \
--header 'Content-Range: bytes 0-30567099/30567100' \
--header 'Content-Type: video/mp4' \
--data '@/path/to/file/example.mp4'
```

With the `publish_id` returned earlier, check for status updates using the [Get Post Status ](https://developers.tiktok.com/docs/en/content-posting-api-reference-get-video-status)endpoint.

```
curl --location 'https://open.tiktokapis.com/v2/post/publish/status/fetch/' \
--header 'Authorization: Bearer act.example12345Example12345Example' \
--header 'Content-Type: application/json; charset=UTF-8' \
--data '{
    "publish_id": "v_pub_url~v2.123456789"
}'
```

###  [#](https://developers.tiktok.com/docs/en/content-posting-api-get-started#post_photos)Post photos
To initiate photo upload on TikTok's server, you must invoke the [Content Posting API endpoint.](https://developers.tiktok.com/docs/en/content-posting-api-reference-photo-post)
Note:
There are differences between the photo post endpoint and the existing video post endpoint.
  * Use /v2/post/publish/content/init/ to upload photos instead of /v2/post/publish/inbox/video/init/
  * The `post_mode` and `media_type` is required in request.body


####  [#](https://developers.tiktok.com/docs/en/content-posting-api-get-started#example_2)Example
Request:

```
curl --location 'https://open.tiktokapis.com/v2/post/publish/content/init/' \
--header 'Authorization: Bearer act.example12345Example12345Example' \
--header 'Content-Type: application/json' \
--data-raw '{
    "post_info": {
        "title": "funny cat",
        "description": "this will be a #funny photo on your @tiktok #fyp",
        "disable_comment": true,
        "privacy_level": "PUBLIC_TO_EVERYONE",
        "auto_add_music": true
    },
    "source_info": {
        "source": "PULL_FROM_URL",
        "photo_cover_index": 1,
        "photo_images": [
            "https://tiktokcdn.com/obj/example-image-01.webp",
            "https://tiktokcdn.com/obj/example-image-02.webp"
        ]
    },
    "post_mode": "DIRECT_POST",
    "media_type": "PHOTO"
}'
```

Response:

```
200 OK

{
    "data": {
        "publish_id": "p_pub_url~v2.123456789"
    },
    "error": {
         "code": "ok",
         "message": "",
         "log_id": "202210112248442CB9319E1FB30C1073F3"
     }
}
```

  

On this page
  * [Prerequisites](https://developers.tiktok.com/docs/en/content-posting-api-get-started#prerequisites)
  * [Post directly to TikTok](https://developers.tiktok.com/docs/en/content-posting-api-get-started#post_directly_to_tiktok)
    * [Query Creator Info](https://developers.tiktok.com/docs/en/content-posting-api-get-started#query_creator_info)
    * [Post a video](https://developers.tiktok.com/docs/en/content-posting-api-get-started#post_a_video)
      * [Example](https://developers.tiktok.com/docs/en/content-posting-api-get-started#example)
    * [Post photos](https://developers.tiktok.com/docs/en/content-posting-api-get-started#post_photos)
      * [Example](https://developers.tiktok.com/docs/en/content-posting-api-get-started#example_2)


Prerequisites
[![TikTok for Developers](https://sf16-sg.tiktokcdn.com/obj/eden-sg/wv_k4aa/ljhwZthlaukjlkulzlp/doc_station/tt4d_logo_dark.ac59d2631b2b.svg)](https://developers.tiktok.com/)
Products
  * [Share Kit](https://developers.tiktok.com/products/share-kit)
  * [Login Kit](https://developers.tiktok.com/products/login-kit)
  * [Content Posting API](https://developers.tiktok.com/products/content-posting-api)
  * [Research API](https://developers.tiktok.com/products/research-api)
  * [Display API](https://developers.tiktok.com/docs/en/display-api-get-started)


  * [Embed Videos](https://developers.tiktok.com/docs/en/embed-videos)
  * [Data Portability API](https://developers.tiktok.com/products/data-portability-api)
  * [Green Screen Kit](https://developers.tiktok.com/products/share-kit#green-screen)
  * [Commercial Content API](https://developers.tiktok.com/products/commercial-content-api)


Other platforms
  * [TikTok Embeds](https://www.tiktok.com/embed "TikTok Embeds")
  * [TikTok for Business](https://www.tiktok.com/business "TikTok for Business")
  * [Advertise on TikTok](https://www.tiktok.com/business/&attr_source=tt_official_site&attr_medium=tt_official_site_guidance "Advertise on TikTok")
  * [TikTok Creative Center](https://ads.tiktok.com/business/creativecenter/ "TikTok Creative Center")
  * [TikTok.com](https://www.tiktok.com "TikTok")
  * [Policy Center](https://developers.tiktok.com/policy/en "Policy Center")


Company
  * [About TikTok](https://www.tiktok.com/about "About TikTok")
  * [Newsroom](https://newsroom.tiktok.com "TikTok Newsroom")
  * [Contact](https://www.tiktok.com/about/contact "Contact TikTok")
  * [Careers](https://careers.tiktok.com "TikTok Careers page")
  * [ByteDance](https://www.bytedance.com "About ByteDance")
  * [Transparency Center](https://www.tiktok.com/transparency "TikTok")


© 2026 TikTok[Terms of Service](https://www.tiktok.com/legal/page/global/tik-tok-developer-terms-of-service/en)[Privacy Policy](https://www.tiktok.com/legal/page/global/partner-privacy-policy/en)[Resources & Legal](https://developers.tiktok.com/docs/en/content-posting-api-get-started#site-footer)

