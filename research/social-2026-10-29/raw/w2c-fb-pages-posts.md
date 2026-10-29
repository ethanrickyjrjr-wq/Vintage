[![Meta](https://static.xx.fbcdn.net/rsrc.php/y9/r/tL_v571NdZ0.svg)](https://developers.facebook.com/)
Build with us
[Docs](https://developers.facebook.com/docs/)
[Blog](https://developers.facebook.com/blog/)
Resources
Developer centers
[Login](https://business.facebook.com/business/loginpage/?next=https%3A%2F%2Fdevelopers.facebook.com%2Fdocumentation%2Fpages-api%2Fposts)
Pages API
Pages API
[Facebook Pages API](https://developers.facebook.com/documentation/pages-api)
[Overview](https://developers.facebook.com/documentation/pages-api/overview)
[Create an app](https://developers.facebook.com/documentation/pages-api/create-an-app)
[Webhooks for Pages](https://developers.facebook.com/documentation/pages-api/webhooks-for-pages)
[Get Started](https://developers.facebook.com/documentation/pages-api/getting-started)
[Manage a Page](https://developers.facebook.com/documentation/pages-api/manage-pages)
[Upcoming Changes](https://developers.facebook.com/documentation/pages-api/pages/upcoming-changes)
[Comments and @Mentions](https://developers.facebook.com/documentation/pages-api/comments-mentions)
[Posts](https://developers.facebook.com/documentation/pages-api/posts)
[Page Integrity API & Webhook](https://developers.facebook.com/documentation/pages-api/integrity-webhook)
[Insights](https://developers.facebook.com/documentation/pages-api/posts)
[Insights](https://developers.facebook.com/documentation/pages-api/platforminsights/page)
[Deprecated Metrics](https://developers.facebook.com/documentation/pages-api/platforminsights/page/deprecated-metrics)
[Search Pages](https://developers.facebook.com/documentation/pages-api/search-pages)
[Error Codes](https://developers.facebook.com/documentation/pages-api/error-codes)
[Changelog](https://developers.facebook.com/documentation/pages-api/changelog)
* * *
Resources
[Changelog](https://developers.facebook.com/documentation/pages-api/changelog/)
[Docs](https://developers.facebook.com/docs)
[Overview](https://developers.facebook.com/documentation/pages-api)
Posts
# Posts
Updated: Apr 17, 2026
Copy for LLM
[View as Markdown](https://developers.facebook.com/documentation/pages-api/posts.md)
This guide explains how to create, publish, and update a post, and reply to a post on your Facebook Page as the Page, and delete a post using the Pages API from Meta.
## Before you start
This guide assumes you have read the [Overview](https://developers.facebook.com/documentation/pages-api/overview)
For a person who can perform tasks on the page, you will need to implement Facebook Login to ask for the following permissions and receive a Page access token:
  * `pages_manage_engagement`
  * `pages_manage_posts`
  * `pages_read_engagement`
  * `pages_read_user_engagement`
  * `publish_video` permission, if you are publishing a video to the Page


Your app user must be able to perform the `CREATE_CONTENT`, `MANAGE`, and `MODERATE` tasks on the Page in the API requests.
If your app users do not own or manage the Page in the API requests, your app will need a User access token and the following features:
  * Page Public Content Access


### Best practices
When testing an API call, you can include the `access_token` parameter set to your access token. However, when making secure calls from your app, use the [access token class.](https://developers.facebook.com/documentation/facebook-login/guides/access-tokens#portabletokens)
## Publish posts
To publish a post to a Page, send a `POST` request to the `/page_id/feed` endpoint, where `page_id` is the ID for your Page, with the following parameters:
  * `message` set to the text for your post
  * `link` set to your URL if you want to post a link
  * `published` set to `true` to publish the post immediately (default) or `false` to publish later 
    * Include `scheduled_publish_time` if set to `false` with the date in one of the following formats: 
      * An integer UNIX timestamp [in seconds] (e.g. `1530432000`)
      * An [ISO 8061⁠](https://l.facebook.com/l.php?u=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FISO_8601&h=AUBlauuyamV0hqDrjpfqJUg-NMzH_cQWHJOuzPb3w_6gwUPmg5XssSDfDgzw_VPM0p189YHaYy4Ofzcz-EbyKQNVP3UDsajL-Zx3joJ1vHDHUkiub40F-_SZPyZC1_fZW3avaae7J1qvLw) timestamp string (e.g. `2018-09-01T10:15:30+01:00`)
      * Any string otherwise parsable by PHP’s [`strtotime()`⁠](https://l.facebook.com/l.php?u=http%3A%2F%2Fphp.net%2Fmanual%2Fen%2Ffunction.strtotime.php&h=AUBlauuyamV0hqDrjpfqJUg-NMzH_cQWHJOuzPb3w_6gwUPmg5XssSDfDgzw_VPM0p189YHaYy4Ofzcz-EbyKQNVP3UDsajL-Zx3joJ1vHDHUkiub40F-_SZPyZC1_fZW3avaae7J1qvLw) (e.g. `+2 weeks`, `tomorrow`)


#### Notes about scheduled posts
  * The publish date must be between 10 minutes and 30 days from the time of the API request.
  * If you are relying on `strtotime()`’s relative date strings you can [read-after-write](https://developers.facebook.com/docs/graph-api/advanced#read-after-write) the `scheduled_publish_time` of the created post to make sure it is what is expected.


#### Example Request
_Formatted for readability. Replace**bold, italics values** , such as **page_id** , with your values._

```
curl -X POST "https://graph.facebook.com/**_v26.0_**/**_page_id_**/feed" \
     -H "Content-Type: application/json" \
     -d '{
           "message":"**_your_message_text_**",
           "link":"**_your_url_**",
           "published":"**_false_**",
           "scheduled_publish_time":"**_unix_time_stamp_of_a_future_date_**",
         }'

```

On success, your app receives the following JSON response with the ID for the post:

```
{
  "id": "**_page_post_id_**"
}

```

### Add audience targeting
To limit who can see a Page post, you can add the `targeting.geo_locations` object or `feed_targeting.geo_locations` parameter in your `POST` request.

```


```
-d '{
      ...
      "targeting": {
        "geo_locations": {
          "countries": [
            "CA"
          ],
          "cities": [
            {
              "key": "296875",
              "name": "Toronto"
            }
          ]
        }
      },
      ...
    }'
```


```

#### Troubleshooting
In some cases using both a country and a region within that country will result in an error: “Some of your locations overlap. Try removing a location.” In these cases target the region or the country depending on the coverage you want.
## Publish Media Posts
You can publish photos and videos to a Page.
### Publish a photo
To publish a photo to a Page, send a `POST` request to the `/page_id/photos` endpoint, where `page_id` is the ID for your Page, with the `url` parameter set to the photo for your post.
#### Example Request
_Formatted for readability. Replace**bold, italics values** , such as **page_id** , with your values._

```
curl -X POST "https://graph.facebook.com/**_v26.0_**/**_page_id_**/photos" \
     -H "Content-Type: application/json" \
     -d '{
           "url":"**_path_to_photo_**",

```

On success, your app receives the following JSON response with the ID for the photo and the ID for the post:

```
{
  "id":"**_photo_id_**",
  "post_id":"**_page_post_id_**"
}

```

### Publish a video
Please visit the [**Video API documentation** to publish a video post to your Page](https://developers.facebook.com/documentation/video-api/guides/publishing). 
## Get Posts
To get a list of Page posts, send a `GET` request to the `/page_id/feed` endpoint.
#### Example Request
_Formatted for readability. Replace**bold, italics values** , such as **page_id** , with your values._

```
curl -i -X GET "https://graph.facebook.com/**_v26.0_**/**_page_id_**/feed"

```

On success, your app receives the following JSON response with an array of objects that include the post ID, the time the post was created, and the content for the post, for each post on your Page:

```


```
{
  "data": [
    {
      "created_time": "2019-01-02T18:31:28+0000",
      "message": "This is my test post on my Page.",
      "id": "page_post_id"
    }
  ],
...
}
```


```

#### Limitations
  * **Live Videos** - If a Page post contains a video that has expired, such as a live broadcast, you can get some post fields but not fields related to the video. The video has its own privacy rules. If the video has expired, you must be the page admin to view its information. 
  * **Message CTA** - Any access token can be used to request publicly shared Page posts as long as your app has been approved for the [Page Public Content Access Feature](https://developers.facebook.com/docs/apps/review/feature#reference-PAGES_ACCESS). However, posts with message CTAs cannot be accessed using another Page's access token since pages cannot message other pages. 


### Page Post URLs
The URL, or permalink, for a Page post is `https://www.facebook.com/`**_`page_post_id`_**.
## Update a Post
To update a Page post, send a `POST` request to the `/page_post_id` endpoint with the parameters you want to update set to the new content.
#### Example Request
_Formatted for readability. Replace**bold, italics values** , such as **page_post_id** , with your values._

```
curl -X POST "https://graph.facebook.com/**_v26.0_**/**_page_post_id_**" \
     -H "Content-Type: application/json" \
     -d '{
           "message":"**_I am updating my Page post_**",
         }'

```

On success, your app receives the following JSON response with `success` set to true:

```


```
{
  "success": true
}
```


```

#### Limitations
An app can only update a Page post if the post was made using that app.
## Delete a Post
To delete a Page post, send a `DELETE` request to the `/page_post_id` endpoint where `page_post_id` is the ID for post you want to delete.
#### Example Request
_Formatted for readability. Replace**bold, italics values** , such as **page_post_id** , with your values._

```
curl -i -X DELETE "https://graph.facebook.com/**_v26.0_**/**_page_post_id_**"

```

On success, your app receives the following JSON response with `success` set to `true`:

```


```
{
  "success": true
}
```


```

## Next Steps
Learn how to [comment on Page posts and @mention](https://developers.facebook.com/docs/pages/comments) a specific person or Page who posted or commented on your Page.
## See Also
#### Video API guides
  * [Video Uploads Guide](https://developers.facebook.com/documentation/video-api/guides/publishing)
  * [Video API Guide](https://developers.facebook.com/docs/graph-api/video)


#### References
  * [Page Reference](https://developers.facebook.com/docs/graph-api/reference/page)
  * [Page Feed Reference](https://developers.facebook.com/docs/graph-api/reference/page/feed)
  * [Page Post Reference](https://developers.facebook.com/docs/graph-api/reference/page-post)
  * [Permissions Reference](https://developers.facebook.com/docs/permissions)
  * [Photo Reference](https://developers.facebook.com/docs/graph-api/reference/photo)
  * [Page Tasks](https://developers.facebook.com/documentation/pages-api/overview#tasks)
  * [Video Reference](https://developers.facebook.com/docs/graph-api/reference/video)


* * *
* * *
![Meta](https://static.xx.fbcdn.net/rsrc.php/y9/r/tL_v571NdZ0.svg)
[![Facebook](https://scontent-mia5-1.xx.fbcdn.net/v/t39.2365-6/425860105_925920989121941_6933048753023841367_n.svg?_nc_cat=1&ccb=1-7&_nc_sid=aa6a2f&_nc_ohc=ae5txUzRuuYQ7kNvwHC0XyY&_nc_oc=Adr8veNI20SUSJDzX_Z51cCxhhYGaGpxFPX9xQA1lJxzRob8b9OD_uclUGANsIP-EEM&_nc_zt=14&_nc_ht=scontent-mia5-1.xx&_nc_gid=yiXpDiMpI7jVw6nTecQIyg&_nc_ss=7b289&oh=00_AQRbxJJ8qDpHoOj2YPeUFVs-KRh-JIrvRk2HvEi4VNOWRg&oe=6AE954A2)](https://www.facebook.com/MetaforDevelopers)[![Instagram](https://scontent-mia3-3.xx.fbcdn.net/v/t39.2365-6/425804778_757649995874129_6917476492193301523_n.svg?_nc_cat=108&ccb=1-7&_nc_sid=aa6a2f&_nc_ohc=3TM3ED2Lx2gQ7kNvwEVEV2E&_nc_oc=AdqW-kwhO6AEf3rBtpDNMuvYufNQLZzX2ingBmNiAR20r_r30wikMwhIGY92cy-K9LA&_nc_zt=14&_nc_ht=scontent-mia3-3.xx&_nc_gid=yiXpDiMpI7jVw6nTecQIyg&_nc_ss=7b289&oh=00_AQRB2TNYIGTRN2agwi5Diuyj0H44wPZyYjMZl7qMFu8CqQ&oe=6AE93EB8)](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.instagram.com%2Fmetafordevelopers%2F&h=AUBlauuyamV0hqDrjpfqJUg-NMzH_cQWHJOuzPb3w_6gwUPmg5XssSDfDgzw_VPM0p189YHaYy4Ofzcz-EbyKQNVP3UDsajL-Zx3joJ1vHDHUkiub40F-_SZPyZC1_fZW3avaae7J1qvLw)[![X](https://scontent-mia5-1.xx.fbcdn.net/v/t39.2365-6/426747931_385023204117867_5811151062540225287_n.svg?_nc_cat=1&ccb=1-7&_nc_sid=aa6a2f&_nc_ohc=Xe5MMfN34ssQ7kNvwEwfjeY&_nc_oc=AdoITz2Q-FwhJ-VIlzRxMM2rEzmshnHlWUMCRiHu8360qbjf8GocpVE7wsFXCZtCgSk&_nc_zt=14&_nc_ht=scontent-mia5-1.xx&_nc_gid=yiXpDiMpI7jVw6nTecQIyg&_nc_ss=7b289&oh=00_AQTO4AJPq_oy32mDIyM7UyBTVy5yG3al3yEik3-nCKefuQ&oe=6AE95D2A)](https://l.facebook.com/l.php?u=https%3A%2F%2Ftwitter.com%2Fmetafordevs&h=AUBlauuyamV0hqDrjpfqJUg-NMzH_cQWHJOuzPb3w_6gwUPmg5XssSDfDgzw_VPM0p189YHaYy4Ofzcz-EbyKQNVP3UDsajL-Zx3joJ1vHDHUkiub40F-_SZPyZC1_fZW3avaae7J1qvLw)[![LinkedIn](https://scontent-mia3-2.xx.fbcdn.net/v/t39.2365-6/467689750_1684384502343829_7561568713040200172_n.svg?_nc_cat=103&ccb=1-7&_nc_sid=aa6a2f&_nc_ohc=ysnjNBowAQUQ7kNvwH52CpT&_nc_oc=AdqCd0G3oGEQOTelp2T5pGHqvpwBNnezdIT_cgGyxnsg3XcizKgjt92ykj1EXXcWhSQ&_nc_zt=14&_nc_ht=scontent-mia3-2.xx&_nc_gid=yiXpDiMpI7jVw6nTecQIyg&_nc_ss=7b289&oh=00_AQRss2s5dQeMsXhf47KNrZ98bHS5BXYJxF6-tFZbslayqw&oe=6AE96CBE)](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.linkedin.com%2Fshowcase%2Fmeta-for-developers%2F&h=AUBlauuyamV0hqDrjpfqJUg-NMzH_cQWHJOuzPb3w_6gwUPmg5XssSDfDgzw_VPM0p189YHaYy4Ofzcz-EbyKQNVP3UDsajL-Zx3joJ1vHDHUkiub40F-_SZPyZC1_fZW3avaae7J1qvLw)[![YouTube](https://scontent-mia5-1.xx.fbcdn.net/v/t39.2365-6/425519002_724756916408357_7491658959807896355_n.svg?_nc_cat=1&ccb=1-7&_nc_sid=aa6a2f&_nc_ohc=oG_Saoc72KsQ7kNvwHhe09m&_nc_oc=Adqmadw82MDErKrFaafimlzWlMGUhE9M8yfZfOVvk_tiCrAL3qez5SY61T_-JhrHbjU&_nc_zt=14&_nc_ht=scontent-mia5-1.xx&_nc_gid=yiXpDiMpI7jVw6nTecQIyg&_nc_ss=7b289&oh=00_AQRE2GZo9St4Q1svDwwSyE0hbqKOYAGXRoYoMJhtrMgMXg&oe=6AE957DF)](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.youtube.com%2FMetaDevelopers%2F&h=AUBlauuyamV0hqDrjpfqJUg-NMzH_cQWHJOuzPb3w_6gwUPmg5XssSDfDgzw_VPM0p189YHaYy4Ofzcz-EbyKQNVP3UDsajL-Zx3joJ1vHDHUkiub40F-_SZPyZC1_fZW3avaae7J1qvLw)
Build with Meta
Build with Meta
[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F&h=AUBlauuyamV0hqDrjpfqJUg-NMzH_cQWHJOuzPb3w_6gwUPmg5XssSDfDgzw_VPM0p189YHaYy4Ofzcz-EbyKQNVP3UDsajL-Zx3joJ1vHDHUkiub40F-_SZPyZC1_fZW3avaae7J1qvLw)
[Meta Horizon ](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F&h=AUBlauuyamV0hqDrjpfqJUg-NMzH_cQWHJOuzPb3w_6gwUPmg5XssSDfDgzw_VPM0p189YHaYy4Ofzcz-EbyKQNVP3UDsajL-Zx3joJ1vHDHUkiub40F-_SZPyZC1_fZW3avaae7J1qvLw)
[Social technologies](https://developers.facebook.com/social-technologies/)
[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F&h=AUBlauuyamV0hqDrjpfqJUg-NMzH_cQWHJOuzPb3w_6gwUPmg5XssSDfDgzw_VPM0p189YHaYy4Ofzcz-EbyKQNVP3UDsajL-Zx3joJ1vHDHUkiub40F-_SZPyZC1_fZW3avaae7J1qvLw)
* * *
News
News
[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F&h=AUBlauuyamV0hqDrjpfqJUg-NMzH_cQWHJOuzPb3w_6gwUPmg5XssSDfDgzw_VPM0p189YHaYy4Ofzcz-EbyKQNVP3UDsajL-Zx3joJ1vHDHUkiub40F-_SZPyZC1_fZW3avaae7J1qvLw)
[Blog](https://developers.facebook.com/blog/)
[Success stories](https://developers.facebook.com/success-stories/)
* * *
Support
Support
[Developer Support](https://developers.facebook.com/support/)
[Bug tool](https://developers.facebook.com/support/bugs/)
[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F&h=AUBlauuyamV0hqDrjpfqJUg-NMzH_cQWHJOuzPb3w_6gwUPmg5XssSDfDgzw_VPM0p189YHaYy4Ofzcz-EbyKQNVP3UDsajL-Zx3joJ1vHDHUkiub40F-_SZPyZC1_fZW3avaae7J1qvLw)
[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)
[Report an incident](https://developers.facebook.com/incident/report/)
* * *
About us
About us
[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AUBlauuyamV0hqDrjpfqJUg-NMzH_cQWHJOuzPb3w_6gwUPmg5XssSDfDgzw_VPM0p189YHaYy4Ofzcz-EbyKQNVP3UDsajL-Zx3joJ1vHDHUkiub40F-_SZPyZC1_fZW3avaae7J1qvLw)
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

