Source: https://developers.facebook.com/docs/video-api/guides/reels-publishing (fetched 2026-11-13 with crawl4ai)

[![Meta](https://static.xx.fbcdn.net/rsrc.php/y9/r/tL_v571NdZ0.svg)](https://developers.facebook.com/)
Build with us
[Docs](https://developers.facebook.com/docs/)
[Blog](https://developers.facebook.com/blog/)
Resources
Developer centers
[Login](https://business.facebook.com/business/loginpage/?next=https%3A%2F%2Fdevelopers.facebook.com%2Fdocumentation%2Fvideo-api%2Fguides%2Freels-publishing)
Video API
Video API
Videos
Video API
[Video API](https://developers.facebook.com/documentation/video-api)
[Overview](https://developers.facebook.com/documentation/video-api/overview)
[Get Started](https://developers.facebook.com/documentation/video-api/getting-started)
[A/B Testing](https://developers.facebook.com/documentation/video-api/ab-testing)
[Crossposting](https://developers.facebook.com/documentation/video-api/guides/crossposting)
[Get Videos](https://developers.facebook.com/documentation/video-api/guides/get-videos)
[Get Insights](https://developers.facebook.com/documentation/video-api/guides/insights)
[Get Music Recommendations](https://developers.facebook.com/documentation/video-api/guides/music-recommendations)
[Upload a File or Video](https://developers.facebook.com/documentation/video-api/graph-api/guides/upload)
[Publish a Video](https://developers.facebook.com/documentation/video-api/guides/publishing)
[Publish a Reel](https://developers.facebook.com/documentation/video-api/guides/reels-publishing)
[Rights Manager API](https://developers.facebook.com/documentation/video-api/graph-api/rights-manager-api)
[Publish a Slideshow](https://developers.facebook.com/documentation/video-api/guides/slideshows)
[Stories](https://developers.facebook.com/documentation/video-api/page-stories-api)
[Reference](https://developers.facebook.com/documentation/video-api/guides/reels-publishing)
[Reference](https://developers.facebook.com/documentation/video-api/reference)
[Error Codes](https://developers.facebook.com/documentation/video-api/reference/error-codes)
[Docs](https://developers.facebook.com/docs)
[Overview](https://developers.facebook.com/documentation/video-api)
Reels Publishing API
# Reels Publishing API
Updated: Jul 30, 2026
Copy for LLM
[View as Markdown](https://developers.facebook.com/documentation/video-api/guides/reels-publishing.md)
This document explains how to publish a reel on a Facebook Page. To publish a reel on a Facebook Page, you will:
  1. Initialize an upload session to upload your reel to the Meta servers
  2. Upload your reel
  3. Publish the reel to your Facebook Page


  * Optionally, you can invite a collaborator to publish the reel on their Facebook Page.


#### Sharing Disclosure
When uploading a reel using your app, the app user should be presented with disclosure of and options for control over how their Reels are used on Facebook.
#### Privacy / Who can see this?
An app user should be able to select the audience for their reel. This selection corresponds to the privacy parameter in the publishing step. Publishing to a Page has implicit public scope, and only the ‘Public’ option should be available.
#### Limitations
  * You can only publish Reels to Facebook Pages
  * You can only crosspost Reels to Facebook Pages


#### Rate Limit
Reels API is limited to 30 API-published posts within a 24-hour moving period. This limit is enforced on the `POST /{page_id}/video_reels` endpoint when attempting to publish a reel. Meta recommends that your app also enforces the publishing rate limit, especially if your app allows app users to schedule posts to be published in the future.
_Sharing Disclosure Mockup_
![New Reel sharing disclosure dialog with the Public audience option selected and Cancel and Share Reel buttons](https://scontent-ord5-2.xx.fbcdn.net/v/t39.2365-6/299692207_789876818817443_2233519248934922026_n.png?_nc_cat=111&_nc_map=urlgen_bucketless&ccb=1-7&_nc_sid=e280be&_nc_ohc=8YuZ0-PqGXsQ7kNvwEmfUyt&_nc_oc=Ado7lGULrLWP3qQwc_H3-gXZfPSHyah7V8X02Gg2Jwhf5rnl-yftjhaIy3eVNM34tBY&_nc_zt=14&_nc_ht=scontent-ord5-2.xx&_nc_gid=iGOGXgwUtmLNqYfyfTkVpQ&_nc_ss=7020f&oh=00_AQSbi4zhstY1mbv6oq0UOO_4kyb4nlS3FLjL3GBEPPzjig&oe=6B10A938)
## Before You Start
You will need:
  * A Page access token requested from your app user who can perform the `CREATE_CONTENT` task on the Page
  * The your app user must grant your app the following permissions using Facebook Login: 
    * `pages_show_list`
    * `pages_read_engagement`
    * `pages_manage_posts`
  * A video file that contains your reel


### Video Specifications  
|  Property   |  Specification   |  
| --- | --- |  
| File Type  | .mp4 (recommended)  |  
| Aspect Ratio  | 9 x 16  |  
| Resolution  | 1080 x 1920 pixels (recommended). Minimum is 540 x 960 pixels  |  
| Frame Rate  | 24 to 60 frames per second  |  
| Duration  |  3 to 90 seconds. A reel published as a story on a Facebook Page can not exceed 60 seconds.  |  
| Video Settings  | 
  * Chroma subsampling 4:2:0
  * Closed GOP (2-5 seconds)
  * Compression – H.264, H.265 (VP9, AV1 are also supported)


  * Fixed frame rate
  * Progressive scan

 |  
| Audio Settings  | 
  * Audio bitrate – 128kbs+
  * Channels – Stereo


  * Codec – AAC Low Complexity
  * Sample rate – 48kHz

 |  
## Step 1: Initialize an Upload Session
Before you can publish a video to a Facebook Page, you must first upload it to the Meta social graph. You will need to initialize a video upload session to start the upload process. To start a session, send a `POST` request to the `/page-id/video_reels` endpoint, where **_page-id_** is the ID for your Facebook Page, with the `upload_phase` parameter set to `start`.
Be sure the host is **_`graph.facebook.com`_**.
#### Example Request
_Formatted for readability. Replace***bold** *, ***italics values** *, such as ***page_access_token** *, with your values._

```
curl -X POST "https://graph.facebook.com/v27.0/**_Your_page_id_**/video_reels" \
     -H "Content-Type: application/json" \
     -d '{
           "upload_phase":"start",
           "access_token":"**_Your_page_access_token_**"
         }'
```

On success, your app will receive a video ID and a URL to the video. This video ID will be used in subsequent steps.

```
{
  "video_id": "**_video-id_**",
  "upload_url": "https://rupload.facebook.com/video-upload/**_video-id_**",
}
```

## Step 2: Upload the Video
Most Graph API calls use the graph.facebook.com host however, calls to upload videos for reels use **_`rupload.facebook.com`_**.
The following file sources are supported for uploaded video files:
  * A file located on your computer
  * A file hosted on a public facing server, such as a CDN


### Upload a Local File
To initiate the upload of the video asset, send a `POST` request using application/octet-stream as content type to the `/video-upload/`**_`video-id`_**endpoint where** _video-id_** is the ID from Step 1, `offset` is set to the first byte being upload, generally `0`, and `file_size` set to the size of your file, in bytes.
Be sure the host is **_`rupload.facebook.com`_**.
**Video Reel Upload Quick Reference**
#### Example Request
_Formatted for readability. Replace***bold** *, ***italics values** *, such as ***page_access_token** *, with your values._

```
curl -X POST "https://rupload.facebook.com/video-upload/v27.0/**_video-id_**" \
     -H "Authorization: OAuth **_Your_page_access_token_**" \
     -H "offset: 0" \
     -H "file_size: **_Your_file_size_in_bytes_**" \
     --data-binary "@**_my_video_file.mp4_**"
```

### Upload a Hosted File
To upload a hosted file, send a `POST` request to the `/video-upload/`**_`video-id`_**endpoint where** _video-id_** is the ID returned in Step 1 and `file_url` is set to the URL for your hosted file.
Be sure the host is **_`rupload.facebook.com`_**.
The API will now reject files hosted on sites that restrict access via robots.txt. Developers need to ensure that the hosting site allows the “facebookexternalhit/1.1 (+http://www.facebook.com/externalhit_uatext.php)” user agent to fetch the hosted file.
Files hosted on Meta CDN (e.g.. fbcdn URLs) will get rejected. Instead, developers can use the crossposting feature to publish a video on multiple pages without uploading the video to each page. Refer to our [detailed guidance](https://developers.facebook.com/documentation/video-api/guides/crossposting) on crossposting.
#### Example Request
_Formatted for readability. Replace***bold** *, ***italics values** *, such as ***page_access_token** *, with your values._

```
curl -X POST "https://rupload.facebook.com/video-upload/v27.0/**_video_id_**" \
     -H "Authorization: OAuth **_Your_page_access_token_**" \
     -H "file_url: **_https://some.cdn.url/video.mp4_**"
```

### Example Upload Response
If you upload was successful, your app will receive a JSON object with `success` set to `true`.

```


```
{"success": true}
```


```

### Get the Upload Status
To get the status of a video, send a `GET` request to the `/` `video-id` endpoint where the `video-id` is the ID from initialization step, and with `fields` set to `status`.
Be sure the host is `graph.facebook.com`.
#### Sample Request

```
curl -X GET "https://graph.facebook.com/**_v27.0_**/**_video-id_**?fields=status
&access_token=**_Your_page_access_token_**"
```

On success your app will receive a JSON object with status information that includes the processing, uploading, and publishing phases, and the video status.
**Video Status Quick Reference**
If re-uploading doesn’t work, try again from Step 1.
##### Example Response with a Processing Error

```


```
{
  "status": {
    "video_status": "processing",
    "uploading_phase": {
      "status": "complete",
    },
    "processing_phase": {
      "status": "not_started",
      "error": {
        "message": "Resolution too low. Video must have a minimum resolution of 540p."
      }
    }
    "publishing_phase": {
      "status": "not_started",
    }
  }
}
```


```

##### Example Response for an Interrupted Upload

```


```
{
  "status": {
    "video_status": "processing",
    "uploading_phase": {
      "status": "in_progress",
      "bytes_transfered": 50002
    }
    "processing_phase": {
      "status": "not_started"
    }
    "publishing_phase": {
      "status": "not_started",
    }
  }
}
```


```
  
|  Error Type   |  Error Message   |  Recommended Solution   |  
| --- | --- | --- |  
| OffsetInvalidError  | Request starting offset is invalid  | Set the ‘offset’ parameter to the `bytes_transfered` value returned in the Video endpoint `status` field  |  
| PartialRequestError  | Partial request (did not match length of file)  | Check the file size and try the upload again.  |  
| ProcessingFailedError  | Request processing failed  | Please try uploading again. Make sure the video meets all of the requirements. If the upload does not work, initialize a new upload session.  |  
### Resume an Interrupted Upload
If the video upload is interrupted, it can be resumed.
To resume an upload, send another POST request to the `/video-upload/video-id` endpoint and use the value for `upload_phase.bytes_transfered` as the value for `offset`.
## Step 3: Publish the Reel
To end the upload session and publish your video, send a `POST `request to the `/`**_`page-id`_**`/video_reels`endpoint. You can also include any of the additional fields, like`description` , which can include hashtags, and `title`.
Be sure the host is **_`graph.facebook.com`_**.
**POST Page Video Reels Quick Reference**
#### Example Request
_Formatted for readability. Replace***bold** *, ***italics values** *, such as ***page_access_token** *, with your values._

```
curl -X POST "https://graph.facebook.com/**_v27.0_**/**_page-id_**/video_reels
    ?access_token=**_Your_page_access_token_**&video_id=**_video-id_**&upload_phase=finish
&video_state=PUBLISHED
&description=**_What a beautiful day! #sunnyand72_**"
```

On success your app will receive a JSON object with `success` set to `true`.

```


```
{"success": true}
```


```

### Get a List of Reels
To get a list of all reels published on your Facebook Page, send a `GET` request to `/`**_`page-id`_**`/video_reels`endpoint.
Be sure the host is **_`graph.facebook.com`_**for this API call.
**Note:** When using `since` and `until` in your `GET` request, the date for `until` must be a date after the date for `since`. For example, if `since` is `2023-01-31`, `until` must be after `2023-01-31`. You can use both parameters, or one or the other. Date formats can be any of the following:
  * `today`, `yesterday`
  * Epoch timestamps (1676057525)
  * `yyyy-mm-dd` (2023-1-31)



```
curl -X GET "https://graph.facebook.com/**_v27.0_**/**_page-id_**/video_reels?access_token=**_Your_page_access_token_**"
```

On success your app will receive a JSON object with information about your published reels such as video ID and published time.

```
{
  "data": [
    {
      "updated_time": "**_unix_timestamp_**",
      "id": "**_video-1-id_**"
    },
    {
      "description": "sample_description",
      "updated_time": "**_unix_timestamp_**",
      "id": "**_video-2-id_**"
    },
    ...
  ]
}
```

## Invite a collaborator
Invite a person, a **collaborator** , to publish your reel on their Facebook Page.
To publish a reel on a collaborator’s Facebook Page you will invite the collaborator to publish your reel on their Facebook Page. When they accept the invitation, the reel will immediately be published on their Facebook Page if the reel has been published, or the reel will be published on their Page when you publish the reel on your Page.
You will need:
  * The ID for the collaborator’s Facebook Page (for New Page Experience, use the delegate Page ID)
  * The ID for the Video you want to share with a collaborator


#### Limitations
  * You can only send 10 collaborator invitation per Page per 24 hours
  * You can only publish Reels to other Facebook Pages


### Send an Invitation
To invite a collaborator to publish your reel on their Facebook Page, send a `POST` request to the `/`**_`video-id`_**`/collaborators`endpoint with the`target_id` parameter set to the ID for the collaborator’s Facebook Page.
_Formatted for readability._

```
curl -X POST "https://graph.facebook.com/**_v27.0_**/**_video-id_**/collaborators
  ?target_id=**_collaborators-page-id_**&access_token=**_your-page-access-token_**"
```

On success your app will receive a JSON response with the link to the invitation and your collaborator will receive an invite notification.
#### Example Response

```
{
  "success": true,
  "collaborator_id": "**_collaborators-page-id_**"
  "invitation_link": "**_facebook-url-for-invitation_**"
}
```

### Get Invitation Status
To get the status for an invitation you sent, send a `GET` request to the `/`**_`video-id`_**`/collaborators`endpoint.
#### Example Request
_Formatted for readability._

```
curl -X POST "https://graph.facebook.com/**_v27.0_**/**_video-id_**/collaborators
  ?access_token=**_your-page-or-user--access-token_**"
```

On success your app will receive a JSON response with the invitation status of `Accepted`, `Declined`, or `Pending`.

```
{
  "id": "**_video-id_**"
  "name": "**_collaborators-page-name_**"
  "invite_status": "**_Accepted_**"
  "invitation_link": "**_facebook-url-for-invitation_**"
}
```

## Tag a location
To find a place to tag, you can use the [Pages Search API](https://developers.facebook.com/documentation/pages-api/search-pages). When searching for a place, only pages with valid locations can be used. When searching be sure to include the `location` field to verify this.
To tag the location in your reel, include the parameter `place` and the `id` returned from the Pages Search API in the publish call.
**Example Request**

```


```
curl -X POST "https://graph.facebook.com/v18.0/page-id/video_reels
    ?access_token=Your_page_access_token
    &video_id=video-id
    &upload_phase=finish
    &video_state=PUBLISHED
    &place=123456"
```


```

## Retrieve Copyright Information
At upload, a copyright check is run to see if your upload contains licensed content and lets you act appropriately before publishing. Videos in violation may have restricted access or be subject to monetization impacts. To retrieve the copyright check information on the Reel, you must have `pages_read_engagement` permission on the Page. You will need the ID of the Video and the Page access token. Please note that it may take a couple of minutes for the copyright check to be completed and return information.
### Limitations
  * Works for Reels API uploads
  * Only the owner can view the matches information


### Example
**Example Request**

```


```
curl -i -X GET "https://graph.facebook.com/v18.0/VIDEO_ID?fields=copyright_check_information&access_token=ACCESS_TOKEN"
```


```

**Example Responses**
_In progress:_

```


```
{
  "copyright_check_information": {
        "status": {
            "status": "in_progress",
        },
    }
}
```


```

_Without any matches:_

```


```
{
  "copyright_check_information": {
        "status": {
            "status": "complete",
            "matches_found": false
        },
    }
}
```


```

_With matches:_

```


```
"copyright_check_information": {
        "status": {
            "status": "complete",
            "matches_found": true
        },
        "copyright_matches": [
            {
                "content_title": "Title 1",
                "owner_copyright_policy": {
                    "name": "Owner name 1",
                    "actions": [
                        {
                            "action": "TRACK",
                            "territories": "3",
                            "geos": [
                                "United Arab Emirates",
                                "Afghanistan",
                                "Antigua and Barbuda",
                            ]
                        }
                    ]
                },
                "matched_segments": [
                    {
                        "start_time_in_seconds": 90.5,
                        "duration_in_seconds": 35,
                        "segment_type": "AUDIO"
                    }
                ]
            },
            {
                "content_title": "Title 2",
                "owner_copyright_policy": {
                    "name": "Owner name 2",
                    "actions": [
                        {
                            "action": "BLOCK",
                            "territories": "1",
                            "geos": [
                                "Italy"
                            ]
                        }
                    ]
                },
                "matched_segments": [
                    {
                        "start_time_in_seconds": 90.5,
                        "duration_in_seconds": 35,
                        "segment_type": "AUDIO"
                    }
                ]
            }
        ]
    },
```


```

## Error Codes
Common error codes and possible mitigations.  
|  Error Code   |  Error Message   |  Possible Mitigation   |  
| --- | --- | --- |  
| `100`  | “error”: { “message”: “(#100) Missing parameter: {a list of missing parameters}”, “type”: “OAuthException”, “code”: 100, “fbtrace_id”: “----“ } }  | A required parameter, such as `upload_phase`, is missing from your API call. Visit the endpoint reference to ensure all required parameters are included and be sure to check for typos.  |  
| `1363040`  | The video you tried to upload has an aspect ratio that isn’t supported on Facebook. Aspect ratios for videos need to be between 16x9 and 9x16. Please try uploading a video in a supported aspect ratio.  | Aspect ratios for videos need to be between 16x9 and 9x16.  |  
| `1363127`  | The video you tried to upload has resolution that isn’t supported on Facebook for this product. Please try uploading a video with a supported resolution  | Minimum resolution is 540 x 960 pixels. Recommended resolution is 1080 x 1920 pixels.  |  
| `1363128`  | The video you tried to upload has a duration that isn’t supported on Facebook for this product. Please try uploading a video with a supported duration.  | Reels duration must be between 3 and 90 seconds.  |  
| `1363129`  | The video you tried to upload has an average frame rate that isn’t supported on Facebook for this product. Please try uploading a video with a supported frame rate  | Reels frame rate must be between 24 and 60 frames per second.  |  
## Learn how to customize a reel
Customize your reel to create a richer reels experience for your viewers.
  * [Add a custom cover photo for your reel](https://developers.facebook.com/docs/graph-api/reference/video/thumbnails#Creating)
  * [Add your favorite music to your reel](https://developers.facebook.com/documentation/video-api/guides/music-recommendations#music-for-you)
  * [Get music recommendations from Meta for new music](https://developers.facebook.com/documentation/video-api/guides/music-recommendations#new-music-on-facebook)
  * [Get music recommendations from Meta for popular music on Facebook](https://developers.facebook.com/documentation/video-api/guides/music-recommendations#music-popular-on-facebook)


## See also
  * [Get insights for your reels](https://developers.facebook.com/docs/graph-api/reference/video/video_insights#reels-metrics) to track engagement
  * [Facebook Sharing to Reels From Android](https://developers.facebook.com/documentation/android/sharing-to-reels-facebook)
  * [Facebook Sharing to Reels From iOS](https://developers.facebook.com/documentation/ios/sharing-to-reels-facebook)
  * Check out the [Facebook Reels Publishing API Sample⁠](https://l.facebook.com/l.php?u=https%3A%2F%2Fgithub.com%2Ffbsamples%2Freels_publishing_apis%2Ftree%2Fmain%2Ffb_reels_publishing_api_sample&h=AUCVBhKTc2jcqbHDULgWyTvml--pj0PG0xC8eAUfR8cGRHHYitxohzsxUcJE5Ynp0kY7xY_ptlcRePTd5yvBHD_ICr0P9G1fgVbprTQ4up53-8zkNQuzrZXt2o39EJpjtAzq-iVA_bG6zA) available on Github.
  * Check out the [Facebook Reels collection on the Postman API Platform⁠](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.postman.com%2Fmeta%2Fworkspace%2Ffacebook%2Ffolder%2F23987686-8318a757-f788-40fa-a27b-e3dcfdc2f8d4%3Fctx%3Ddocumentation%26fbclid%3DIwAR23KQZpXD4mdQ-fFdEYU5KkigRM67AtsFPwJMJ-EdZZyuxAmuC-Zd22jV0&h=AUCVBhKTc2jcqbHDULgWyTvml--pj0PG0xC8eAUfR8cGRHHYitxohzsxUcJE5Ynp0kY7xY_ptlcRePTd5yvBHD_ICr0P9G1fgVbprTQ4up53-8zkNQuzrZXt2o39EJpjtAzq-iVA_bG6zA)
  * Check out the [Instagram Reels collection on the Postman API Platform⁠](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.postman.com%2Fmeta%2Fworkspace%2Finstagram%2Ffolder%2F23987686-91b95cb4-a10c-4aad-b15d-b54f2e6900e7%3Fctx%3Ddocumentation%26fbclid%3DIwAR31DFQLv9Uew9bxy-Cx6WqINMpg3sqdV-ipqVc2fBeFMdxVE4lOzDHGp80&h=AUCVBhKTc2jcqbHDULgWyTvml--pj0PG0xC8eAUfR8cGRHHYitxohzsxUcJE5Ynp0kY7xY_ptlcRePTd5yvBHD_ICr0P9G1fgVbprTQ4up53-8zkNQuzrZXt2o39EJpjtAzq-iVA_bG6zA)


ON THIS PAGE
Sharing Disclosure
Privacy / Who can see this?
Limitations
Rate Limit
Before You Start
Video Specifications
Step 1: Initialize an Upload Session
Example Request
Step 2: Upload the Video
Upload a Local File
Example Request
Upload a Hosted File
Example Request
Example Upload Response
Get the Upload Status
Sample Request
Resume an Interrupted Upload
Step 3: Publish the Reel
Example Request
Get a List of Reels
Invite a collaborator
Limitations
Send an Invitation
Example Response
Get Invitation Status
Example Request
Tag a location
Retrieve Copyright Information
Limitations
Example
Error Codes
Learn how to customize a reel
See also
* * *
* * *
![Meta](https://static.xx.fbcdn.net/rsrc.php/y9/r/tL_v571NdZ0.svg)
[![Facebook](https://scontent-ord5-1.xx.fbcdn.net/v/t39.2365-6/425860105_925920989121941_6933048753023841367_n.svg?_nc_cat=1&ccb=1-7&_nc_sid=aa6a2f&_nc_ohc=pXipGCdWXXwQ7kNvwFE88Sg&_nc_oc=Adq79KEtmOO3ibwJs6vur8pGCLkuPNYJW1C102ew7x2f20M_0FsM_r4UAJa0hPEF5HQ&_nc_zt=14&_nc_ht=scontent-ord5-1.xx&_nc_gid=iGOGXgwUtmLNqYfyfTkVpQ&_nc_ss=7020f&oh=00_AQSD33EOBazA-ac7AGMUmBFdF1vaMyrB0OcVRcOAACEANg&oe=6AFC3A22)](https://www.facebook.com/MetaforDevelopers)[![Instagram](https://scontent-ord5-1.xx.fbcdn.net/v/t39.2365-6/425804778_757649995874129_6917476492193301523_n.svg?_nc_cat=1&ccb=1-7&_nc_sid=aa6a2f&_nc_ohc=N2ATnWKr0tgQ7kNvwFZwYV4&_nc_oc=Ado0ArjBfxNm0Jnky5rEvMIxjdUHptZqxYrL-yCgfa2BlL9hqTqBQh5FDgSv1g0kOY0&_nc_zt=14&_nc_ht=scontent-ord5-1.xx&_nc_gid=iGOGXgwUtmLNqYfyfTkVpQ&_nc_ss=7020f&oh=00_AQSvX1cT94G5urUfbAs7GcFuZaLpGkUwtk3XNY0cvTwO5w&oe=6AFC5C78)](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.instagram.com%2Fmetafordevelopers%2F&h=AUCVBhKTc2jcqbHDULgWyTvml--pj0PG0xC8eAUfR8cGRHHYitxohzsxUcJE5Ynp0kY7xY_ptlcRePTd5yvBHD_ICr0P9G1fgVbprTQ4up53-8zkNQuzrZXt2o39EJpjtAzq-iVA_bG6zA)[![X](https://scontent-ord5-1.xx.fbcdn.net/v/t39.2365-6/426747931_385023204117867_5811151062540225287_n.svg?_nc_cat=1&ccb=1-7&_nc_sid=aa6a2f&_nc_ohc=rDq5BDrJPIMQ7kNvwHg5h9-&_nc_oc=AdoWUl6MJZiD0Y4z_LTBLvG39PsDkkcFP7EKuXQxUG7LrCH2f-3IFsYVnlwEydinqhU&_nc_zt=14&_nc_ht=scontent-ord5-1.xx&_nc_gid=iGOGXgwUtmLNqYfyfTkVpQ&_nc_ss=7020f&oh=00_AQRTa0adZygjDtG4pNHGogysrDSKPC6IBDEe3LRiOecC_g&oe=6AFC42AA)](https://l.facebook.com/l.php?u=https%3A%2F%2Ftwitter.com%2Fmetafordevs&h=AUCVBhKTc2jcqbHDULgWyTvml--pj0PG0xC8eAUfR8cGRHHYitxohzsxUcJE5Ynp0kY7xY_ptlcRePTd5yvBHD_ICr0P9G1fgVbprTQ4up53-8zkNQuzrZXt2o39EJpjtAzq-iVA_bG6zA)[![LinkedIn](https://scontent-ord5-2.xx.fbcdn.net/v/t39.2365-6/467689750_1684384502343829_7561568713040200172_n.svg?_nc_cat=103&_nc_map=urlgen_bucketless&ccb=1-7&_nc_sid=aa6a2f&_nc_ohc=6z3DjFAzbcsQ7kNvwE60IU-&_nc_oc=AdrOE8eQKzTG1BXNB7A7SBV2g14arBb8VL-OY0iWY3kt8dckNuWDKEQnosI25I7p3do&_nc_zt=14&_nc_ht=scontent-ord5-2.xx&_nc_gid=iGOGXgwUtmLNqYfyfTkVpQ&_nc_ss=7020f&oh=00_AQTpOW6RilfDz7499O501T4V_mG4cIVWWmHxynBGVu057w&oe=6AFC523E)](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.linkedin.com%2Fshowcase%2Fmeta-for-developers%2F&h=AUCVBhKTc2jcqbHDULgWyTvml--pj0PG0xC8eAUfR8cGRHHYitxohzsxUcJE5Ynp0kY7xY_ptlcRePTd5yvBHD_ICr0P9G1fgVbprTQ4up53-8zkNQuzrZXt2o39EJpjtAzq-iVA_bG6zA)[![YouTube](https://scontent-ord5-1.xx.fbcdn.net/v/t39.2365-6/425519002_724756916408357_7491658959807896355_n.svg?_nc_cat=1&ccb=1-7&_nc_sid=aa6a2f&_nc_ohc=uxhO0L6IDm8Q7kNvwHXuTTl&_nc_oc=AdoGb3RtlYwLM9TQqWSLGtFbIyl-2vHBNfddfGRgoz-K7MnMHSAuRmjvrrmQe6viL2c&_nc_zt=14&_nc_ht=scontent-ord5-1.xx&_nc_gid=iGOGXgwUtmLNqYfyfTkVpQ&_nc_ss=7020f&oh=00_AQTsQioEnjbBX1mbEjtAEFkNv9IVorV0adERvhutlCnUBQ&oe=6AFC3D5F)](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.youtube.com%2FMetaDevelopers%2F&h=AUCVBhKTc2jcqbHDULgWyTvml--pj0PG0xC8eAUfR8cGRHHYitxohzsxUcJE5Ynp0kY7xY_ptlcRePTd5yvBHD_ICr0P9G1fgVbprTQ4up53-8zkNQuzrZXt2o39EJpjtAzq-iVA_bG6zA)
Build with Meta
Build with Meta
[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F&h=AUCVBhKTc2jcqbHDULgWyTvml--pj0PG0xC8eAUfR8cGRHHYitxohzsxUcJE5Ynp0kY7xY_ptlcRePTd5yvBHD_ICr0P9G1fgVbprTQ4up53-8zkNQuzrZXt2o39EJpjtAzq-iVA_bG6zA)
[Meta Horizon ](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F&h=AUCVBhKTc2jcqbHDULgWyTvml--pj0PG0xC8eAUfR8cGRHHYitxohzsxUcJE5Ynp0kY7xY_ptlcRePTd5yvBHD_ICr0P9G1fgVbprTQ4up53-8zkNQuzrZXt2o39EJpjtAzq-iVA_bG6zA)
[Social technologies](https://developers.facebook.com/social-technologies/)
[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F&h=AUCVBhKTc2jcqbHDULgWyTvml--pj0PG0xC8eAUfR8cGRHHYitxohzsxUcJE5Ynp0kY7xY_ptlcRePTd5yvBHD_ICr0P9G1fgVbprTQ4up53-8zkNQuzrZXt2o39EJpjtAzq-iVA_bG6zA)
* * *
News
News
[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F&h=AUCVBhKTc2jcqbHDULgWyTvml--pj0PG0xC8eAUfR8cGRHHYitxohzsxUcJE5Ynp0kY7xY_ptlcRePTd5yvBHD_ICr0P9G1fgVbprTQ4up53-8zkNQuzrZXt2o39EJpjtAzq-iVA_bG6zA)
[Blog](https://developers.facebook.com/blog/)
[Success stories](https://developers.facebook.com/success-stories/)
* * *
Support
Support
[Developer Support](https://developers.facebook.com/support/)
[Bug tool](https://developers.facebook.com/support/bugs/)
[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F&h=AUCVBhKTc2jcqbHDULgWyTvml--pj0PG0xC8eAUfR8cGRHHYitxohzsxUcJE5Ynp0kY7xY_ptlcRePTd5yvBHD_ICr0P9G1fgVbprTQ4up53-8zkNQuzrZXt2o39EJpjtAzq-iVA_bG6zA)
[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)
[Report an incident](https://developers.facebook.com/incident/report/)
* * *
About us
About us
[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AUCVBhKTc2jcqbHDULgWyTvml--pj0PG0xC8eAUfR8cGRHHYitxohzsxUcJE5Ynp0kY7xY_ptlcRePTd5yvBHD_ICr0P9G1fgVbprTQ4up53-8zkNQuzrZXt2o39EJpjtAzq-iVA_bG6zA)
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

