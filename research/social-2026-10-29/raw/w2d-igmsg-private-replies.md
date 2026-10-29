[![Meta](https://static.xx.fbcdn.net/rsrc.php/y9/r/tL_v571NdZ0.svg)](https://developers.facebook.com/)
Build with us
[Docs](https://developers.facebook.com/docs/)
[Blog](https://developers.facebook.com/blog/)
Resources
Developer centers
[Login](https://business.facebook.com/business/loginpage/?next=https%3A%2F%2Fdevelopers.facebook.com%2Fdocumentation%2Fbusiness-messaging%2Finstagram-messaging%2Ffeatures%2Fprivate-replies)
Instagram Messaging
Instagram Messaging
Business Messaging
Instagram Messaging
[Instagram Messaging](https://developers.facebook.com/documentation/business-messaging/instagram-messaging)
[Overview](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/overview)
[Getting Started](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/get-started)
[Sample Experience](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/sample-experience)
[Messages](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/features/private-replies)
[Send a Message](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/features/send-message)
[Generic Template](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/generic-template)
[Button Template](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/button-template)
[Product Template](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/features/product-template)
[Quick Replies](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/features/quick-replies)
[Sender Actions](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/features/sender-actions)
[Attachment Upload API](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/features/attachment-upload)
[Conversation Features](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/features/private-replies)
[Conversation Routing](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/features/private-replies)
[Conversation Routing](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/features/conversation-routing)
[Conversation Routing APIs](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/features/conversation-routing/apis)
[Human Agent Escalation](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/features/human-agent-escalation)
[Ice Breakers](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/features/ice-breakers)
[ig.me links](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/features/ig-me-links)
[Persistent Menu](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/features/persistent-menu)
[Private Replies](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/features/private-replies)
[Story Mention](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/features/story-mention)
[Moderate Conversations API](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/features/moderate-conversations)
[User Profile API](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/features/user-profile)
[Webhooks](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/webhooks)
[App Review](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/features/private-replies)
[App Review](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/app-review)
[Apps For Other Businesses](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/app-review/apps-for-other-businesses)
[Apps For Your Own Business](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/app-review/apps-for-your-own-business)
[Webhook Debugger](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/webhooks/debugging)
* * *
Resources
[Changelog](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/changelog/)
[Docs](https://developers.facebook.com/docs)
[Overview](https://developers.facebook.com/documentation/business-messaging/whatsapp/overview)
Private replies - Instagram Messaging
# Private replies - Instagram Messaging
Updated: Jul 2, 2026
Copy for LLM
[View as Markdown](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/features/private-replies.md)
This document shows you how to programmatically add Private Replies to your messaging experience.
## How it works
Private Replies allows your app user to send a single message to an Instagram user who commented on the app user’s Instagram professional account post, ads post, reel, or live story.
When your webhook server receives a `comments` or `live_comments` event notification, you can use the comment ID to send a private reply directly to the Instagram user who published the comment. This reply will be delivered to the Instagram user’s **Inbox** folder, if the Instagram user follows the Instagram professional account, or to the Instagram user’s **Request** folder, if the Instagram user does not follow the account.
Private replies can be sent within 7 days of when the comment was created, except for Instagram Live, for which a private reply can only be sent during the live broadcast. The message will contain a link to the post that the Instagram user commented on.
![Two Instagram phone screens: a post with comments, and a Private Reply message sent to the commenter's Inbox](https://scontent-mia5-2.xx.fbcdn.net/v/t39.2365-6/118520113_305452657552386_5531150750029687976_n.jpg?_nc_cat=100&ccb=1-7&_nc_sid=e280be&_nc_ohc=1PExl1U2KCsQ7kNvwHGPRKe&_nc_oc=AdrAfa0YjWu4JSbTUY9RPCaCbRYn7c2QOip8Y7EtOPHvvzV1Sf9mVNDH6PCjnDAI78Y&_nc_zt=14&_nc_ht=scontent-mia5-2.xx&_nc_gid=Dwbb6_0RMHur3AszC5PXMw&_nc_ss=7b289&oh=00_AQRYNyGslPSdCh6NKaBDO8Pi1QEmqnboFUjP6ebDJiJtzA&oe=6AFDDA0A)
### Webhooks
  * When hosting an Instagram Live story, make sure your server can handle the increased load of notifications triggered by [`live_comments` webhooks events, via the Instagram API,](https://developers.facebook.com/docs/instagram-api/guides/webhooks) and that your system can differentiate between `live_comments` and `comments` notifications. 
  * Instagram Graph API `comments` webhooks notifications for ads posts will include the ID and title for the ad. You may need to update your webhooks server to handle these new fields. 
The `ad_id` and `ad_title` will be returned in the media object when an Instagram user comments on a boosted Instagram post or Instagram ads post. Commenting on a boosted or ads post may result in duplicate webhook notifications.


### Limitations
  * Only one message can be sent to the Instagram user who commented.
  * The message must be sent within 7 days from when the comment was created for comments on a post, ads post, or reel.
  * Due to the transient nature of Instagram Live Stories, private replies on Instagram Live Story comments can only be sent during the live broadcast. As soon as the live broadcast has ended, private replies can no longer be sent.
  * Only when the Instagram user responds to the private message can you continue the conversation within the 24-hour messaging window.
  * Standard Access apps can only access data for people who have a role on the app.


### Before you start
This guide assumes you have read the [Messenger Platform Overview](https://developers.facebook.com/documentation/business-messaging/messenger-platform/overview) and the [Instagram Messaging Overview](https://developers.facebook.com/docs/messenger-platform/instagram/overview) and implemented the needed components.
You will need:
  * The ID for the Facebook Page linked to your Instagram professional account
  * The ID for the comment made by the person to whom you are sending the private reply. The ID can be obtained from the Instagram `comments` webhooks, for posts, ads posts, and reels, and Instagram `live_comments` webhooks for live stories (recommended to avoid rate limiting) or an API call to the `/page/feed` endpoint
  * The `instagram_manage_comments` and `pages_messaging` permissions, obtained via Facebook Login
  * A Page access token requested by an Instagram user who can perform the `MESSAGING` task on the Facebook Page linked to your Instagram professional account
  * The Human Agent feature
  * Advanced Access


## Send a private reply
To send a private reply to an Instagram user who commented on your post, reel, or live story, send a `POST` request to the `/<PAGE_ID>/messages` endpoint where the `recipient` parameter contains the comment ID and the `message` parameter contains the text you wish to send.
_Formatted for readability._
Select language
cURL Android SDK Objective-C Java SDK
* * *

```
curl -i -X POST "https://graph.facebook.com/<PAGE_ID>/messages
  ?recipient: { comment_id: <COMMENT_ID> }
  &message: { "text": "Thanks for reaching out, how can I help?" }
  &access_token=<PAGE_ACCESS_TOKEN>"

```

On success, your app will receive the following response:

```


```
{
  "recipient_id": "526...",   // The Instagram-scoped ID
  "message_id": "aWdfZ..."    // The message ID for your private reply
}
```


```

## See also
  * [Access Levels](https://developers.facebook.com/documentation/business-messaging/messenger-platform/overview#advanced---standard-access) – Learn about the access levels and data available for each. 
  * [Instagram Live Media and Comments](https://developers.facebook.com/docs/instagram-api/reference/ig-user/live_media) – Visit the Instagram Graph API Reference for more information about live media. 
  * [Instagram Media and Comments](https://developers.facebook.com/docs/instagram-api/reference/ig-media) – Visit the Instagram Graph API Reference for more information about Instagram media. 
  * [Rate limits for Instagram Messaging API](https://developers.facebook.com/documentation/business-messaging/messenger-platform/overview#rate-limiting) – Learn more about the rate limits that affect Instagram Messaging. 
  * [Tasks on Facebook Pages](https://developers.facebook.com/docs/pages/overview/permissions-features#tasks) – Learn about the tasks people can perform on the Page. 
  * [Webhooks for Messenger Platform](https://developers.facebook.com/documentation/business-messaging/messenger-platform/webhooks) – Learn about the webhooks available for Instagram Messaging 


### Developer Support
  * Use the [Meta Status tool⁠](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F&h=AUC_PaYMW2zjKuwNSvMOziH2XpthENaFtseD1KlEnm9_UPxrcr-ZpncjhrKAZNu-GOPtLkbJoQIEfw8gPYNzmdZkry8_l2-ir5ob-4snwCEyJu7N6n73eMD63OC7UtytZUSMcYhrnPlAlQ) to check for the status and outages of Meta business products.
  * Use the [Meta Developer Support tool](https://developers.facebook.com/support) to report bugs and view reported bugs, get help with Ads or Business Manager, and more.


* * *
* * *
![Meta](https://static.xx.fbcdn.net/rsrc.php/y9/r/tL_v571NdZ0.svg)
[![Facebook](https://scontent-mia5-1.xx.fbcdn.net/v/t39.2365-6/425860105_925920989121941_6933048753023841367_n.svg?_nc_cat=1&ccb=1-7&_nc_sid=aa6a2f&_nc_ohc=ae5txUzRuuYQ7kNvwHC0XyY&_nc_oc=Adr8veNI20SUSJDzX_Z51cCxhhYGaGpxFPX9xQA1lJxzRob8b9OD_uclUGANsIP-EEM&_nc_zt=14&_nc_ht=scontent-mia5-1.xx&_nc_gid=Dwbb6_0RMHur3AszC5PXMw&_nc_ss=7b289&oh=00_AQRGNNslE7aa2G-MqL-LKNkcSHRX3kWhRcPQI_LINiI4LA&oe=6AE954A2)](https://www.facebook.com/MetaforDevelopers)[![Instagram](https://scontent-mia5-1.xx.fbcdn.net/v/t39.2365-6/425804778_757649995874129_6917476492193301523_n.svg?_nc_cat=1&ccb=1-7&_nc_sid=aa6a2f&_nc_ohc=3TM3ED2Lx2gQ7kNvwEVEV2E&_nc_oc=AdqW-kwhO6AEf3rBtpDNMuvYufNQLZzX2ingBmNiAR20r_r30wikMwhIGY92cy-K9LA&_nc_zt=14&_nc_ht=scontent-mia5-1.xx&_nc_gid=Dwbb6_0RMHur3AszC5PXMw&_nc_ss=7b289&oh=00_AQQ2IId4v8XDJ1gkci6sNnLszsWJpeUcSNZTbJhCFDDCNA&oe=6AE93EB8)](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.instagram.com%2Fmetafordevelopers%2F&h=AUC_PaYMW2zjKuwNSvMOziH2XpthENaFtseD1KlEnm9_UPxrcr-ZpncjhrKAZNu-GOPtLkbJoQIEfw8gPYNzmdZkry8_l2-ir5ob-4snwCEyJu7N6n73eMD63OC7UtytZUSMcYhrnPlAlQ)[![X](https://scontent-mia5-1.xx.fbcdn.net/v/t39.2365-6/426747931_385023204117867_5811151062540225287_n.svg?_nc_cat=1&ccb=1-7&_nc_sid=aa6a2f&_nc_ohc=Xe5MMfN34ssQ7kNvwEwfjeY&_nc_oc=AdoITz2Q-FwhJ-VIlzRxMM2rEzmshnHlWUMCRiHu8360qbjf8GocpVE7wsFXCZtCgSk&_nc_zt=14&_nc_ht=scontent-mia5-1.xx&_nc_gid=Dwbb6_0RMHur3AszC5PXMw&_nc_ss=7b289&oh=00_AQSeaXVJpAPwZ_6wwh4LwBg-fzaeZz9K5BGPij77JB4ycA&oe=6AE95D2A)](https://l.facebook.com/l.php?u=https%3A%2F%2Ftwitter.com%2Fmetafordevs&h=AUC_PaYMW2zjKuwNSvMOziH2XpthENaFtseD1KlEnm9_UPxrcr-ZpncjhrKAZNu-GOPtLkbJoQIEfw8gPYNzmdZkry8_l2-ir5ob-4snwCEyJu7N6n73eMD63OC7UtytZUSMcYhrnPlAlQ)[![LinkedIn](https://scontent-mia3-2.xx.fbcdn.net/v/t39.2365-6/467689750_1684384502343829_7561568713040200172_n.svg?_nc_cat=103&ccb=1-7&_nc_sid=aa6a2f&_nc_ohc=ysnjNBowAQUQ7kNvwH52CpT&_nc_oc=AdqCd0G3oGEQOTelp2T5pGHqvpwBNnezdIT_cgGyxnsg3XcizKgjt92ykj1EXXcWhSQ&_nc_zt=14&_nc_ht=scontent-mia3-2.xx&_nc_gid=Dwbb6_0RMHur3AszC5PXMw&_nc_ss=7b289&oh=00_AQQs03KMl0IC08Cy8x219_JgTgFV70F5kdXGNQeVzVsZwQ&oe=6AE96CBE)](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.linkedin.com%2Fshowcase%2Fmeta-for-developers%2F&h=AUC_PaYMW2zjKuwNSvMOziH2XpthENaFtseD1KlEnm9_UPxrcr-ZpncjhrKAZNu-GOPtLkbJoQIEfw8gPYNzmdZkry8_l2-ir5ob-4snwCEyJu7N6n73eMD63OC7UtytZUSMcYhrnPlAlQ)[![YouTube](https://scontent-mia5-1.xx.fbcdn.net/v/t39.2365-6/425519002_724756916408357_7491658959807896355_n.svg?_nc_cat=1&ccb=1-7&_nc_sid=aa6a2f&_nc_ohc=oG_Saoc72KsQ7kNvwHhe09m&_nc_oc=Adqmadw82MDErKrFaafimlzWlMGUhE9M8yfZfOVvk_tiCrAL3qez5SY61T_-JhrHbjU&_nc_zt=14&_nc_ht=scontent-mia5-1.xx&_nc_gid=Dwbb6_0RMHur3AszC5PXMw&_nc_ss=7b289&oh=00_AQRtZXf1qdPJtRdb0CZtmB8EZHSklBWbRx3H3-qjrzovRA&oe=6AE957DF)](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.youtube.com%2FMetaDevelopers%2F&h=AUC_PaYMW2zjKuwNSvMOziH2XpthENaFtseD1KlEnm9_UPxrcr-ZpncjhrKAZNu-GOPtLkbJoQIEfw8gPYNzmdZkry8_l2-ir5ob-4snwCEyJu7N6n73eMD63OC7UtytZUSMcYhrnPlAlQ)
Build with Meta
Build with Meta
[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F&h=AUC_PaYMW2zjKuwNSvMOziH2XpthENaFtseD1KlEnm9_UPxrcr-ZpncjhrKAZNu-GOPtLkbJoQIEfw8gPYNzmdZkry8_l2-ir5ob-4snwCEyJu7N6n73eMD63OC7UtytZUSMcYhrnPlAlQ)
[Meta Horizon ](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F&h=AUC_PaYMW2zjKuwNSvMOziH2XpthENaFtseD1KlEnm9_UPxrcr-ZpncjhrKAZNu-GOPtLkbJoQIEfw8gPYNzmdZkry8_l2-ir5ob-4snwCEyJu7N6n73eMD63OC7UtytZUSMcYhrnPlAlQ)
[Social technologies](https://developers.facebook.com/social-technologies/)
[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F&h=AUC_PaYMW2zjKuwNSvMOziH2XpthENaFtseD1KlEnm9_UPxrcr-ZpncjhrKAZNu-GOPtLkbJoQIEfw8gPYNzmdZkry8_l2-ir5ob-4snwCEyJu7N6n73eMD63OC7UtytZUSMcYhrnPlAlQ)
* * *
News
News
[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F&h=AUC_PaYMW2zjKuwNSvMOziH2XpthENaFtseD1KlEnm9_UPxrcr-ZpncjhrKAZNu-GOPtLkbJoQIEfw8gPYNzmdZkry8_l2-ir5ob-4snwCEyJu7N6n73eMD63OC7UtytZUSMcYhrnPlAlQ)
[Blog](https://developers.facebook.com/blog/)
[Success stories](https://developers.facebook.com/success-stories/)
* * *
Support
Support
[Developer Support](https://developers.facebook.com/support/)
[Bug tool](https://developers.facebook.com/support/bugs/)
[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F&h=AUC_PaYMW2zjKuwNSvMOziH2XpthENaFtseD1KlEnm9_UPxrcr-ZpncjhrKAZNu-GOPtLkbJoQIEfw8gPYNzmdZkry8_l2-ir5ob-4snwCEyJu7N6n73eMD63OC7UtytZUSMcYhrnPlAlQ)
[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)
[Report an incident](https://developers.facebook.com/incident/report/)
* * *
About us
About us
[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AUC_PaYMW2zjKuwNSvMOziH2XpthENaFtseD1KlEnm9_UPxrcr-ZpncjhrKAZNu-GOPtLkbJoQIEfw8gPYNzmdZkry8_l2-ir5ob-4snwCEyJu7N6n73eMD63OC7UtytZUSMcYhrnPlAlQ)
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

