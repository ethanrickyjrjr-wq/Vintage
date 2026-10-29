[![Meta](https://static.xx.fbcdn.net/rsrc.php/y9/r/tL_v571NdZ0.svg)](https://developers.facebook.com/)
Build with us
[Docs](https://developers.facebook.com/docs/)
[Blog](https://developers.facebook.com/blog/)
Resources
Developer centers
[Login](https://business.facebook.com/business/loginpage/?next=https%3A%2F%2Fdevelopers.facebook.com%2Fdocumentation%2Fbusiness-messaging%2Finstagram-messaging%2Fapp-review%2Fapps-for-your-own-business)
Instagram Messaging
Instagram Messaging
Business Messaging
Instagram Messaging
[Instagram Messaging](https://developers.facebook.com/documentation/business-messaging/instagram-messaging)
[Overview](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/overview)
[Getting Started](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/get-started)
[Sample Experience](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/sample-experience)
[Messages](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/app-review/apps-for-your-own-business)
[Send a Message](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/features/send-message)
[Generic Template](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/generic-template)
[Button Template](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/button-template)
[Product Template](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/features/product-template)
[Quick Replies](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/features/quick-replies)
[Sender Actions](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/features/sender-actions)
[Attachment Upload API](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/features/attachment-upload)
[Conversation Features](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/app-review/apps-for-your-own-business)
[Conversation Routing](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/app-review/apps-for-your-own-business)
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
[App Review](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/app-review/apps-for-your-own-business)
[App Review](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/app-review)
[Apps For Other Businesses](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/app-review/apps-for-other-businesses)
[Apps For Your Own Business](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/app-review/apps-for-your-own-business)
[Webhook Debugger](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/webhooks/debugging)
* * *
Resources
[Changelog](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/changelog/)
[Docs](https://developers.facebook.com/docs)
[Overview](https://developers.facebook.com/documentation/business-messaging/whatsapp/overview)
Apps For Your Own Business
# Apps For Your Own Business
Updated: Jun 30, 2026
Copy for LLM
[View as Markdown](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/app-review/apps-for-your-own-business.md)
If your app is an automated experience or a custom inbox solution that can only process messages sent to your own Instagram Professional account, follow these guidelines when completing App Review. If your app will be used to process messages on behalf of other businesses, follow [this guide](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/app-review/apps-for-other-businesses) instead.
If you are unfamiliar with App Review, refer to our [App Review for Instagram Messaging Apps](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/app-review) document before proceeding.
## Screen recording
Create a [screen recording](https://developers.facebook.com/videos/2021/developing-for-success-how-to-produce-a-screencast-for-app-review/) showing us how to test your app. You will upload this video in later steps and our reviewers will refer to it when testing your app.
Show the following:
  * How to initiate a conversation with your app 
  * How your app processes a message 
  * How your app processes [quick replies](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/features/quick-replies), [ice breakers](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/features/ice-breakers), or [generic templates](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/generic-template), if you have implemented them 
  * How your app processes [rich media](https://developers.facebook.com/documentation/business-messaging/messenger-platform/overview#content-design-network-urls)
  * How your app processes messages the sender unsent 


Make sure that the app you are recording is the same app that you are submitting for review, otherwise your submission will be rejected.
## Verification details
Providing verification details is optional. If you do want to provide this information, use the guidance below.
![Screenshot of the App Verification Details window](https://scontent-mia5-1.xx.fbcdn.net/v/t39.2365-6/258779682_672778047037720_5895450097279284281_n.png?_nc_cat=101&ccb=1-7&_nc_sid=e280be&_nc_ohc=frZdbeljzd4Q7kNvwEvyJfz&_nc_oc=AdrxVCJJVMfDd7gtg34kDY0lIZ3kAF4TixIPhA2zjOPXu69y-E5HIeEZAoAeklMHxgE&_nc_zt=14&_nc_ht=scontent-mia5-1.xx&_nc_gid=nJaeE3Ln6SAkQB2BECT6wQ&_nc_ss=7b289&oh=00_AQT960yh2F5tOfQDL6FAjnkKaKgRc4gSGbxPQNWLq9oSSw&oe=6AFDB884)
### Platform settings
Set the platform to **Website** (click the **Add Platform** button if you haven’t set a platform yet) and use your business’s website URL.
### Credentials
Leave this section blank.
## `instagram_manage_messages`
![App Review form for requesting the instagram_manage_messages permission with description and screen recording fields](https://scontent-mia3-1.xx.fbcdn.net/v/t39.2365-6/641668262_1445181454007171_7295215445309758039_n.png?_nc_cat=110&ccb=1-7&_nc_sid=e280be&_nc_ohc=0Cj_cJQPIVwQ7kNvwGwkktF&_nc_oc=AdrGKk0h03efuCTAwldloC2G1DZqBsAmBxpKQoTPM6a6k61Xx8f9rTFxAyouK6pXywk&_nc_zt=14&_nc_ht=scontent-mia3-1.xx&_nc_gid=nJaeE3Ln6SAkQB2BECT6wQ&_nc_ss=7b289&oh=00_AQRxP3fHgs6T3XUIes_9bpa2lQ7tWZXmTAtNllTec3Ezag&oe=6AFDB7F7)
### Description
  * Tell us if your app is an automated experience, a custom inbox solution, or both. 
  * Tell us how to initiate a conversation with your app. 
  * If your app is an automated experience, provide a set of commands we can test. Include commands that can trigger [quick replies](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/features/quick-replies), [ice breakers](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/features/ice-breakers), or [generic templates](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/generic-template), if you have implemented them. 


### Instagram account
Enter your Instagram profile handle.
### Primary experience
Choose an option that best describes what we can build using your app.
  * **Automated** — Choose this option if we can use your app to build an automated experience that automatically processes messages in real-time.
  * **Live Agent** — Choose this option if we can only use your app to build a custom inbox solution that agents can use to manually process (read, reply, delete, and so on) direct messages.


### Screen recording
Upload the [screen recording](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/app-review/apps-for-your-own-business#screen-recording) you recorded earlier.
## business_management
When requesting the `business_management` permission, call out the following in your app review submission:
  1. This permission is a dependency for the `pages_messaging` and `pages_show_list` permissions.
  2. For Instagram Messaging, call out that this permission is a dependency for the `instagram_manage_messages` permission.
  3. In the app review screencast, clearly show the Page admin navigating the Facebook Login flow, picking the pages or Instagram handles and providing the necessary permissions to the app.


In your app, make sure to inform the Page admin that they need to explicitly provide permissions to the app to manage their business assets. You will need to add the `business_management` permission as part of the [Facebook Login for Business](https://developers.facebook.com/documentation/facebook-login/facebook-login-for-business) flow.
## Human agent
The Human Agent feature is optional. Only request this feature if you have a custom inbox solution to process [human agent escalations](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/features/human-agent-escalation) and your agents need up to 7 days to respond to escalations using [message tags](https://developers.facebook.com/documentation/business-messaging/messenger-platform/reference/send-api).
![Screenshot of the App Verification Details window](https://scontent-mia3-3.xx.fbcdn.net/v/t39.2365-6/259362305_259059542917474_1848277544194004737_n.png?_nc_cat=108&ccb=1-7&_nc_sid=e280be&_nc_ohc=MXwcUg9h-YMQ7kNvwFKplFj&_nc_oc=AdqhwjpJPIOhT1sEQgwuh_FIalCePzEwGTzyK8ZwJM0H5nmUZVfBN-HoFrr8qY2SQLc&_nc_zt=14&_nc_ht=scontent-mia3-3.xx&_nc_gid=nJaeE3Ln6SAkQB2BECT6wQ&_nc_ss=7b289&oh=00_AQR-8zZBpr0bXMDxfOP9CTfwMtaI5Yh-_c-WsXgbrmUd7A&oe=6AFDCFF1)
### Description
Explain why it can take someone up to 7 days to reply to a direct message instead of 24 hours.
### Screen recording
If you are requesting this feature along with the `instagram_manages_messages` permission in the same App Review submission, upload the [screen recording](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/app-review/apps-for-your-own-business#screen-recording) you recorded earlier. Otherwise, capture a new screen recording that shows a human agent responding to a message.
* * *
* * *
![Meta](https://static.xx.fbcdn.net/rsrc.php/y9/r/tL_v571NdZ0.svg)
[![Facebook](https://scontent-mia5-1.xx.fbcdn.net/v/t39.2365-6/425860105_925920989121941_6933048753023841367_n.svg?_nc_cat=1&ccb=1-7&_nc_sid=aa6a2f&_nc_ohc=ae5txUzRuuYQ7kNvwHC0XyY&_nc_oc=Adr8veNI20SUSJDzX_Z51cCxhhYGaGpxFPX9xQA1lJxzRob8b9OD_uclUGANsIP-EEM&_nc_zt=14&_nc_ht=scontent-mia5-1.xx&_nc_gid=nJaeE3Ln6SAkQB2BECT6wQ&_nc_ss=7b289&oh=00_AQRcBD-ewJYnhNg1bdfXGqL8n1fXo3yaVHBemHdLrf-7rg&oe=6AE954A2)](https://www.facebook.com/MetaforDevelopers)[![Instagram](https://scontent-mia5-1.xx.fbcdn.net/v/t39.2365-6/425804778_757649995874129_6917476492193301523_n.svg?_nc_cat=1&ccb=1-7&_nc_sid=aa6a2f&_nc_ohc=3TM3ED2Lx2gQ7kNvwEVEV2E&_nc_oc=AdqW-kwhO6AEf3rBtpDNMuvYufNQLZzX2ingBmNiAR20r_r30wikMwhIGY92cy-K9LA&_nc_zt=14&_nc_ht=scontent-mia5-1.xx&_nc_gid=nJaeE3Ln6SAkQB2BECT6wQ&_nc_ss=7b289&oh=00_AQQhI2d1jGy6aF4STlmexiF5zdwjuR80rCxmVMIVNCdpbQ&oe=6AE93EB8)](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.instagram.com%2Fmetafordevelopers%2F&h=AUCXoT5PpJORr5cor-dUwXHDnIV9uwIqcwWvTILxSzLkXm18d6zGlKoVTWKjxsE87ZP3FeUduVeHDGOyDTDhvBPLvMrRoghR9DtrPtvD30omO_FsvycFNC4tUWru8dpPtnOTZrqD84pMNA)[![X](https://scontent-mia5-1.xx.fbcdn.net/v/t39.2365-6/426747931_385023204117867_5811151062540225287_n.svg?_nc_cat=1&ccb=1-7&_nc_sid=aa6a2f&_nc_ohc=Xe5MMfN34ssQ7kNvwEwfjeY&_nc_oc=AdoITz2Q-FwhJ-VIlzRxMM2rEzmshnHlWUMCRiHu8360qbjf8GocpVE7wsFXCZtCgSk&_nc_zt=14&_nc_ht=scontent-mia5-1.xx&_nc_gid=nJaeE3Ln6SAkQB2BECT6wQ&_nc_ss=7b289&oh=00_AQTXATWcxQ0t8Om5ehWfH7HDqv_KbRt9y1BItE62ngKDXA&oe=6AE95D2A)](https://l.facebook.com/l.php?u=https%3A%2F%2Ftwitter.com%2Fmetafordevs&h=AUCXoT5PpJORr5cor-dUwXHDnIV9uwIqcwWvTILxSzLkXm18d6zGlKoVTWKjxsE87ZP3FeUduVeHDGOyDTDhvBPLvMrRoghR9DtrPtvD30omO_FsvycFNC4tUWru8dpPtnOTZrqD84pMNA)[![LinkedIn](https://scontent-mia3-2.xx.fbcdn.net/v/t39.2365-6/467689750_1684384502343829_7561568713040200172_n.svg?_nc_cat=103&ccb=1-7&_nc_sid=aa6a2f&_nc_ohc=ysnjNBowAQUQ7kNvwH52CpT&_nc_oc=AdqCd0G3oGEQOTelp2T5pGHqvpwBNnezdIT_cgGyxnsg3XcizKgjt92ykj1EXXcWhSQ&_nc_zt=14&_nc_ht=scontent-mia3-2.xx&_nc_gid=nJaeE3Ln6SAkQB2BECT6wQ&_nc_ss=7b289&oh=00_AQTsW_B2BHarhlQ5L-iwj4owKhyRHrE-fxqyFdyY3blqDw&oe=6AE96CBE)](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.linkedin.com%2Fshowcase%2Fmeta-for-developers%2F&h=AUCXoT5PpJORr5cor-dUwXHDnIV9uwIqcwWvTILxSzLkXm18d6zGlKoVTWKjxsE87ZP3FeUduVeHDGOyDTDhvBPLvMrRoghR9DtrPtvD30omO_FsvycFNC4tUWru8dpPtnOTZrqD84pMNA)[![YouTube](https://scontent-mia5-1.xx.fbcdn.net/v/t39.2365-6/425519002_724756916408357_7491658959807896355_n.svg?_nc_cat=1&ccb=1-7&_nc_sid=aa6a2f&_nc_ohc=oG_Saoc72KsQ7kNvwHhe09m&_nc_oc=Adqmadw82MDErKrFaafimlzWlMGUhE9M8yfZfOVvk_tiCrAL3qez5SY61T_-JhrHbjU&_nc_zt=14&_nc_ht=scontent-mia5-1.xx&_nc_gid=nJaeE3Ln6SAkQB2BECT6wQ&_nc_ss=7b289&oh=00_AQTQG-b-0NhRbYBD4EI-Tq6YQHCtQGJ9oucsW1Zub1ngGA&oe=6AE957DF)](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.youtube.com%2FMetaDevelopers%2F&h=AUCXoT5PpJORr5cor-dUwXHDnIV9uwIqcwWvTILxSzLkXm18d6zGlKoVTWKjxsE87ZP3FeUduVeHDGOyDTDhvBPLvMrRoghR9DtrPtvD30omO_FsvycFNC4tUWru8dpPtnOTZrqD84pMNA)
Build with Meta
Build with Meta
[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F&h=AUCXoT5PpJORr5cor-dUwXHDnIV9uwIqcwWvTILxSzLkXm18d6zGlKoVTWKjxsE87ZP3FeUduVeHDGOyDTDhvBPLvMrRoghR9DtrPtvD30omO_FsvycFNC4tUWru8dpPtnOTZrqD84pMNA)
[Meta Horizon ](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F&h=AUCXoT5PpJORr5cor-dUwXHDnIV9uwIqcwWvTILxSzLkXm18d6zGlKoVTWKjxsE87ZP3FeUduVeHDGOyDTDhvBPLvMrRoghR9DtrPtvD30omO_FsvycFNC4tUWru8dpPtnOTZrqD84pMNA)
[Social technologies](https://developers.facebook.com/social-technologies/)
[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F&h=AUCXoT5PpJORr5cor-dUwXHDnIV9uwIqcwWvTILxSzLkXm18d6zGlKoVTWKjxsE87ZP3FeUduVeHDGOyDTDhvBPLvMrRoghR9DtrPtvD30omO_FsvycFNC4tUWru8dpPtnOTZrqD84pMNA)
* * *
News
News
[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F&h=AUCXoT5PpJORr5cor-dUwXHDnIV9uwIqcwWvTILxSzLkXm18d6zGlKoVTWKjxsE87ZP3FeUduVeHDGOyDTDhvBPLvMrRoghR9DtrPtvD30omO_FsvycFNC4tUWru8dpPtnOTZrqD84pMNA)
[Blog](https://developers.facebook.com/blog/)
[Success stories](https://developers.facebook.com/success-stories/)
* * *
Support
Support
[Developer Support](https://developers.facebook.com/support/)
[Bug tool](https://developers.facebook.com/support/bugs/)
[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F&h=AUCXoT5PpJORr5cor-dUwXHDnIV9uwIqcwWvTILxSzLkXm18d6zGlKoVTWKjxsE87ZP3FeUduVeHDGOyDTDhvBPLvMrRoghR9DtrPtvD30omO_FsvycFNC4tUWru8dpPtnOTZrqD84pMNA)
[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)
[Report an incident](https://developers.facebook.com/incident/report/)
* * *
About us
About us
[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AUCXoT5PpJORr5cor-dUwXHDnIV9uwIqcwWvTILxSzLkXm18d6zGlKoVTWKjxsE87ZP3FeUduVeHDGOyDTDhvBPLvMrRoghR9DtrPtvD30omO_FsvycFNC4tUWru8dpPtnOTZrqD84pMNA)
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

