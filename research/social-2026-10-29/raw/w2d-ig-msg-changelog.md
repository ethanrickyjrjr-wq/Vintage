[![Meta](https://static.xx.fbcdn.net/rsrc.php/y9/r/tL_v571NdZ0.svg)](https://developers.facebook.com/)
Build with us
[Docs](https://developers.facebook.com/docs/)
[Blog](https://developers.facebook.com/blog/)
Resources
Developer centers
[Login](https://business.facebook.com/business/loginpage/?next=https%3A%2F%2Fdevelopers.facebook.com%2Fdocumentation%2Fbusiness-messaging%2Finstagram-messaging%2Fchangelog)
Instagram Messaging
Instagram Messaging
[Instagram Messaging](https://developers.facebook.com/documentation/business-messaging/instagram-messaging)
[Overview](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/overview)
[Getting Started](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/get-started)
[Sample Experience](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/sample-experience)
[Messages](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/changelog)
[Send a Message](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/features/send-message)
[Generic Template](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/generic-template)
[Button Template](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/button-template)
[Product Template](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/features/product-template)
[Quick Replies](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/features/quick-replies)
[Sender Actions](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/features/sender-actions)
[Attachment Upload API](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/features/attachment-upload)
[Conversation Features](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/changelog)
[Conversation Routing](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/changelog)
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
[App Review](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/changelog)
[App Review](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/app-review)
[Apps For Other Businesses](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/app-review/apps-for-other-businesses)
[Apps For Your Own Business](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/app-review/apps-for-your-own-business)
[Webhook Debugger](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/webhooks/debugging)
* * *
Resources
[Changelog](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/changelog/)
[Docs](https://developers.facebook.com/documentation)
Changelog
Changelog
Updated: October 28, 2026
[Get notified](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/changelog/rss/)
* * *
Changelog (42)
Search Changelog
October 28, 2026
_Instagram Messaging API, Webhooks_
Updated the [Instagram webhook reference](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/webhooks#handoff-reasons) to document `message.handoff_reason` for Meta Business Agent handoffs. When enabled, this optional string accompanies `message.admin_text` and identifies `purchase_intent`, `payment_received`, `human_requested`, or `other`. Use it to route handoff notifications without parsing localized text, and continue to handle notifications without the field.
The reference includes a table of example trigger conditions, including missing information, unsupported requests, business takeover, and response failures that map to `other`.
* * *
October 18, 2026
_Instagram Messaging API_
Updated [Conversation Routing for Instagram](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/features/conversation-routing) to clarify how your app can take control of a conversation owned by Meta Business AI. **Take control of conversations with your Business AI** is off by default and is independent of **Take control of conversations**. When the setting is off, untagged Send API requests fail with error code `100` and error subcode `2534037`. Wait for a `messaging_handovers` webhook event containing `pass_thread_control` before responding.
* * *
September 28, 2026
_Instagram Messaging API, Messenger Platform_
Updated the [Messenger Platform messaging policy](https://developers.facebook.com/documentation/business-messaging/messenger-platform/policy) and [Instagram Platform Overview](https://developers.facebook.com/documentation/instagram-platform/overview) to document that the standard messaging window may extend up to 7 days for conversations that start from Click-to-Messenger or Click-to-Direct ads. The up to 7-day period starts when the person sends their first message after clicking the ad. Conversations started through other entry points remain within a 24-hour window.
* * *
May 6, 2026
[Sending multiple images](https://developers.facebook.com/docs/instagram-platform/instagram-api-with-instagram-login/messaging-api/) is now out of beta and available to all accounts via [Facebook Graph API](https://developers.facebook.com/docs/messenger-platform/instagram/features/send-message/) for Instagram accounts linked with a Facebook page OR the [Instagram API](https://developers.facebook.com/docs/instagram-platform/instagram-api-with-instagram-login/messaging-api/) for Instagram-only accounts.
* * *
April 27, 2026
The legacy `share` attachment type is being removed from Instagram post share webhook payloads. As announced on [October 30, 2025](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/changelog#october-30-2025), the `share` attachment has been deprecated in favor of the `ig_post` attachment type, which includes full metadata (media ID, URL, and title). This change is being rolled out gradually: webhooks will return only the `ig_post` attachment once rollout reaches your app. If your integration still relies on the `share` attachment type for Instagram posts, update it to use `ig_post` instead or contact our developer support team through [Meta Developer Support Portal](https://developers.facebook.com/support/) to request exclusion of your app(s) from this change.
* * *
March 13, 2026
The Instagram Direct Send API now supports sending the images with attachment IDs (in addition to image URLs) which resolves the problem of timeouts when uploading multiple large high-quality images from slow servers. You can use the attachment API to upload the images one at a time and reuse the attachment IDs to send the same image to multiple users. See the updated documentation for [Facebook Graph API](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/features/send-message) for Instagram accounts linked with a Facebook page OR the [Instagram API](https://developers.facebook.com/docs/instagram-platform/instagram-api-with-instagram-login/messaging-api) for Intagram-only accounts.
* * *
December 19, 2025
### Instagram PDF Attachments
You can now upload and send PDF file attachment in Instagram Direct using [Facebook Graph API](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/features/send-message) for Instagram accounts linked with a Facebook page OR the [Instagram API](https://developers.facebook.com/docs/instagram-platform/instagram-api-with-instagram-login/messaging-api) for Instagram-only accounts.
### Instagram Message Replies API
You can now send a reply to a specific message in Instagram Direct using the [Facebook Graph API](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/features/send-message#send-a-reply-to-a-message) for Instagram accounts linked with a Facebook page
`reply_to` object will also be available in the [Conversations API](https://developers.facebook.com/documentation/business-messaging/messenger-platform/conversations). It will be non-null when the message is a reply and will indicate if it is a self reply. This boolean flag will also be added to the reply_to object returned in the message object in Message and Echo webhooks.
* * *
December 2, 2025
Businesses can now use the [Messenger](https://developers.facebook.com/documentation/business-messaging/messenger-platform/send-messages/sender-actions) and [Instagram Send API](https://developers.facebook.com/docs/instagram-platform/instagram-api-with-instagram-login/messaging-api#react-or-unreact-to-a-message) to react with a reaction emoji to a message in their inbox, edit an existing reaction on a message and remove a reaction (unreact) from a message that was previously reacted to.
* * *
November 3, 2025
You can now send a collection of images in Instagram Direct using either the [Facebook Graph API](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/features/send-message) for Instagram accounts linked with a Facebook page OR the [Instagram API](https://developers.facebook.com/docs/instagram-platform/instagram-api-with-instagram-login/messaging-api) for Intagram-only accounts.
November 3, 2025: Multi-image sending is a Beta feature that will be rolled out incrementally over a few weeks . While the feature is rolled out, some Instagram accounts may get an error response [`2534068`](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/features/send-message#send-images) to indicate that the feature is not yet available for that account.
* * *
October 30, 2025
Starting November 3, 2025, the webhook payload for Instagram post shares will include two attachments: the existing `share` attachment and a new `ig_post` attachment. The payload now provides additional metadata, including media ID, URL, and title (caption).
If this change is not compatible with your app and you need more time to make updates, please contact our developer support team via the [Meta Developer Support Portal](https://developers.facebook.com/support/) to request exclusion of your app(s) from this change until you make the necessary updates to support the new attachment type.
The old `share` attachment type will continue to be supported for Instagram posts until **February 1, 2026** , after which it will be removed. Partners and integrators are encouraged to migrate to the new `ig_post` attachment type as soon as possible. See [here](https://developers.facebook.com/docs/instagram-platform/webhooks/new) for before and after payload sample.
* * *
October 23, 2025
Meta no longer supports the Handover Protocol for Instagram. All businesses have been migrated to [Conversation Routing](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/features/conversation-routing). Conversation Routing is backwards compatible with most Handover Protocol APIs and functionalities, and is expected to function without interruption.
* * *
October 21, 2025
[Instagram Moderate Conversations API](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/features/moderate-conversations) is now available. This new API will allow businesses to block users, unblock users, and move conversations to the spam folder in Meta Business Suite Inbox for the Instagram platform. Previously, these actions could only be completed on the Instagram app or Meta Business Suite.
* * *
October 13, 2025
The [Conversations API](https://developers.facebook.com/documentation/business-messaging/messenger-platform/conversations#conversation-ownership-filtering) now supports an `is_owner` field for both Messenger and Instagram. This field indicates if the app making the request is the current thread owner of the conversation or not, and is only returned when [Conversation Routing](https://developers.facebook.com/documentation/business-messaging/messenger-platform/conversation-routing) is enabled.
Benefits:
  1. Filter and respond only to conversations your app owns.
  2. Avoid unnecessary ticket creation and reduce costs.
  3. Streamline recovery after downtime by focusing on relevant threads.


* * *
September 23, 2025
Businesses can now display typing indicators and mark_seen indicators in a conversation to let message recipients know that the business has seen and are processing their message, using [Sender Actions](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/features/sender-actions).
* * *
September 16, 2025
[Custom thread control window](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/features/conversation-routing?locale=en_US#extended-thread-control-window) for Click To Instagram Ads is now available. When a conversation starts from an ad, the app controls the thread for 24 hours from the last user message, extendable up to 30 days by setting `receiving_app_control_expiration`. Invalid values or Conversation Control actions reset the window to 1 day.
* * *
September 10, 2025
Introducing the new `message_edit` webhook subscription in Instagram supporting both use cases of both Business Login for Instagram and Facebook Login for Business. Sample `message_edit` webhook can be found [here](https://developers.facebook.com/docs/instagram-platform/webhooks/examples?locale=en_US#message-edit).
* * *
February 24, 2025
### Messenger and Instagram
`messaging_referrals` webhook now contains flow ID. The webhook event contains a `flow_id` field when an ad referral originates from an ad with a [Welcome Message flow](https://developers.facebook.com/documentation/business-messaging/messenger-platform/ads/ads-welcome-message-flows). This is available in the ad referral object of the `messages`, `messaging_postbacks`, `messaging_referrals` webhooks. See more details about the webhook [here](https://developers.facebook.com/documentation/business-messaging/messenger-platform/reference/webhook-events/messaging_referrals).
* * *
October 8, 2024
### Messenger `response_feedback` webhook
The new `response_feedback` webhook event notifies you when a user provides feedback on a message you send, by clicking on one of the “thumbs up”/”thumbs down”/”Good response”/”Bad response” buttons. See more details about the webhook [here](https://developers.facebook.com/documentation/business-messaging/messenger-platform/reference/webhook-events/response_feedback).
### Send API Rate Limits
Your app can now make 300 (up from 100) calls per second per Instagram professional account for messages that contain text, links, reactions, and stickers. [Learn more.](https://developers.facebook.com/documentation/business-messaging/messenger-platform/overview#rate-limiting)
* * *
June 23, 2024
### Launch of the new Instagram API with Instagram Login
[Components of this new Instagram API:](https://developers.facebook.com/docs/instagram/platform/instagram-api/overview)
  * A Facebook Page will no longer be required
  * The host URL for API calls is `graph.instagram.com`
  * New permissions for this API: 
    * `instagram_business_basic`
    * `instagram_business_content_publishing`
    * `instagram_business_manage_comments`
    * `instagram_business_manage_messages`
  * New apps will add the new **Instagram** product when creating a Meta app
  * Existing apps can add the new **Instagram** product in the App Dashboard


[Visit our migration guide to learn if this new Instagram API with Instagram Login is right for you](https://developers.facebook.com/docs/instagram/platform/instagram-api/migration-guide).
Monitor the [Instagram Platform Changelog](https://developers.facebook.com/docs/instagram-api/changelog) for changes including bug fixes and new features
* * *
June 11, 2024
### Messenger Messages Webhook
`ig_reel` will now be a supported attachment type for the messages webhook. IG reel attachments will have type `ig_reel` and the attachment payload will include the title, url, and video id for the reel.
### Instagram Messages Webhook
`ig_reel` and `reel` will now be supported attachment types in a messages webhook. IG reel attachments will have type `ig_reel`, and the attachment payload will include the title, url, and video id for the reel. FB reel attachments will have type `reel`, and the attachment payload will include the title, url, and video id for the reel.
### Messenger Conversation Routing: app-level thread control configs
Businesses using Messenger Conversation Routing can now configure the thread control takeover capability on the individual app level. The original takeover config that’s coupled with the default app is now deprecated with all values migrated. Learn more [here](https://developers.facebook.com/documentation/business-messaging/messenger-platform/conversation-routing?locale=en_US#tc-takeover-configs).
### Instagram Comment Webhooks
_Applies to all versions_
In addition to the `ad_id` and `ad_title`, the `original_media_id` will be returned in the `media` object of the `comments` field’s `value` object when a person comments on a [boosted Instagram post or Instagram ads post⁠](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F1067656009937668&h=AUCJmPOC0M_PZZvmz2TVZF_HPNHmcCJb62xGoJbIZuR4sJggG58YXRqDMGmcss3kwUbi6Su1s87iC08uOxos15BXhxbd9cQ6GxXAzyUlWZ9ZhzVHyGQAMTJGN0TOkSu6hu4cfGg7RwW7vg). For more information, refer to [Set Up Webhooks for Instagram](https://developers.facebook.com/docs/instagram-api/guides/webhooks).
* * *
March 12, 2024
### Welcome Message Flows
Welcome Message flows can now be configured for messaging ads using the marketing API. Learn more about Click to Messenger ads [here](https://developers.facebook.com/documentation/ads-commerce/marketing-api/ad-creative/messaging-ads/click-to-messenger) and Click to Instagram ads [here](https://developers.facebook.com/documentation/ads-commerce/marketing-api/ad-creative/messaging-ads/click-to-instagram).
* * *
October 17, 2023
### Conversation Routing for Instagram
Conversation Routing is now available for Instagram. Conversation Routing allows Meta to route conversations between your business and customers, or prospective customers, to the app that you have specified to respond in the conversation. This routing allows your business to create rich conversations with people and to minimize API calls to Meta’s servers.
### Custom Labels and Personas APIs
The Custom Labels API and Personas API access has been restored to businesses that operate in Europe, and for people in Europe and Japan who connect with businesses globally.
### Updates to welcome message flows for Ads that Click to Messenger and Instagram Direct
Businesses and agencies can now easily connect their Click to Messenger and Click to Instagram Direct ads to a welcome message created in a partner app without having to use a JSON code snippet. The welcome message will appear as a dropdown in ads manager when creating the Click to Messenger and Click to Instagram Direct ad. [Learn more about it here.](https://developers.facebook.com/documentation/business-messaging/messenger-platform/ads/ads-welcome-message-flows)
* * *
September 12, 2023
### Conversation Routing
As a business, you may use multiple third-party messaging providers for different conversations with your customers, like lead generation, marketing offers about your products, or customer support questions. Conversation routing lets you define which partners control customer conversations at a particular time, so that customers get the information they need. You can create and manage message routing rules in your Page settings.
### Button Template for Instagram
The button template sends a text message with up to three attached buttons. This template is useful for offering the message recipient options to choose from, such as predetermined responses to a question, or actions to take. Supported button types are `postback` and `web_url`.
* * *
June 20, 2023
### Instagram Messaging with the Messenger Platform
Instagram Messaging is now available for any Instagram Professional account for a business or a Creator.
* * *
June 15, 2023
### Ads that Click to Messenger
#### Call Prompt
You can now add a call prompt to allow customers or people interested in your business to call your business.
#### Click to Subscribe
You can now create ads that include a click to subscribe flow that allow you to ask customers or people interested in your business to opt in to receiving marketing messages.
### Multi App Routing
Multi App Routing is now available for Instagram Direct and Messenger.
* * *
February 21, 2023
Recurring Notifications for Messenger Platform 
#### Titles for Opt In Request
The `title` property for [recurring notification opt in requests](https://developers.facebook.com/docs/messenger-platform/send-messages/recurring-notifications#request-permission-to-send-recurring-notifications) is **no longer required**. If `title` is not set, the value defaults to “Updates and promotions”. This change applies to opt in requests sent from a Facebook Page or Instagram Professional accounts.
* * *
February 2, 2023
Recurring Notifications for Messenger Platform 
#### Message Frequency for Opt In Requests
The `notification_messages_frequency` property for [recurring notification opt in requests](https://developers.facebook.com/docs/messenger-platform/send-messages/recurring-notifications) is **deprecated** and will no longer be returned in `GET` requests or webhook notifications. However, notification message tokens created before Feb. 2, 2023 for weekly or monthly recurring notifications will be supported and the `notification_message_frequency` will be returned in webhook notifications.
#### Followup Messages for Opt Ins
You can now send up to three [followup messages](https://developers.facebook.com/docs/messenger-platform/send-messages/recurring-notifications#opt-in-followup-messages) to a person who has opted in to receiving recurring notifications. All three followup messages must be sent within 2 minutes of the first followup message.
#### Notification Message Tokens
The [`GET /PAGE-ID/notification_message_tokens` endpoint](https://developers.facebook.com/docs/messenger-platform/send-messages/recurring-notifications#get-a-list-of-tokens) is now available for Instagram Messaging.
The [`next_eligible_time` property](https://developers.facebook.com/docs/messenger-platform/send-messages/recurring-notifications#get-a-list-of-tokens) for Notification Message Token endpoints is now available. This field returns the time at which you are able to send the next recurring notification using that notification message token.
Messenger API for Instagram 
You can now send GIFs in [messages sent](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/features/send-message) from an Instagram Professional account using the Messenger API for Instagram.
The [Attachment Upload API](https://developers.facebook.com/docs/messenger-platform/instagram/features/upload-attachment) now supports uploading media for messages sent from an Instagram Professional account.
Referral information for ads that click to an Instagram conversation (CTD) is now returned in [messages webhook notifications](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/webhooks#messages).
* * *
November 9, 2022
#### Business Login for Instagram
[Business Login for Instagram](https://developers.facebook.com/docs/instagram/business-login-for-instagram) makes it easier for you to onboard Instagram users who still need to configure their account for API access through modal pop ups and fewer steps. 
#### Improvements between Click to Messenger, Lead Gen ads and Messenger Platform
We’ve made following up on Lead Gen ads that Click to Messenger easier through:
  * A new [Referral Webhook for Click to Messenger, Lead Gen ads](https://developers.facebook.com/documentation/business-messaging/messenger-platform/discovery/lead-generation-ads-in-messenger#webhooks) that include the lead information.
  * Improvements to the [Handover Protocol](https://developers.facebook.com/docs/messenger-platform/handover-protocol/messenger-lead-ads-hop). Advertisers can now select which app they want to route completed leads. Additionally, for apps that haven’t yet implemented these app notifications, an [optional summary message](https://developers.facebook.com/documentation/business-messaging/messenger-platform/discovery/lead-generation-ads-in-messenger#connnectapp) can be enabled, to send lead information to that app in the form of a regular message.
  * Since referral or summary events are triggered while the standard messaging window is open, apps can use this to follow-up with leads directly in Messenger, upsell them to [Recurring Notifications](https://developers.facebook.com/docs/messenger-platform/send-messages/recurring-notifications) or have them book an appointment or call the business directly.


#### Messaging Events API
Messaging Events API supports the [`lead_submitted` event](https://developers.facebook.com/documentation/ads-commerce/conversions-api/business-messaging#lead_submitted). Businesses can use this event to report lead submissions from Click to Messenger ads. This new messaging event is released as an Open Beta. Reporting in Ads Manager will come soon.
#### Persistent Menu
[Persistent Menu](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/features/persistent-menu) is now available for Instagram Messaging.
#### Private Replies
Instagram Messaging now supports [Private Replies](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/features/private-replies) for comments on Instagram Live Stories and ads posts. You may need to update your webhooks server to handle these new fields.
#### Recurring Notifications
You can now get a list of all valid Notification Message Tokens using the [`GET /PAGE-ID/notification_message_tokens` endpoint](https://developers.facebook.com/docs/messenger-platform/send-messages/recurring-notifications#get-a-list-of-tokens).
* * *
August 16, 2022
#### Private Replies
[Private Reply](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/features/private-replies) is now available for comments on Instagram Reels.
#### Instagram Messaging
You can now send Instagram messages with audio and videos that have been uploaded to a Meta server or sent from your server.
* * *
May 25, 2022
[User Profile API](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/features/user-profile) supports retrieval of the customer’s Instagram username field on Graph API v14.0 and later.
* * *
May 19, 2022
**Recurring Notifications for Messenger API**  
[Recurring Notifications](https://developers.facebook.com/docs/messenger-platform/send-messages/recurring-notifications) is a major update to the Messenger API to allow businesses to send proactive, automated messages that drive re-engagement. Recurring Notifications help businesses deliver personalized, customer centric messages at every stage of the customer journey.
**Recurring Notifications for Messenger API for Instagram**  
We’re announcing Recurring Notifications for Messenger API for Instagram as a beta. Developers can sign up for our [beta interest list⁠](https://www.facebook.com/help/contact/528956182103351) before July.
**Instagram Send API rate limit increase**  
We have increased the rate limit for the Send API to 100 API calls per second for each Instagram Professional Account.
**ig.me referral parameter**  
Businesses can add [ig.me links](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/features/ig-me-links) on websites, emails, and product packaging to easily enable users to start a conversation with a business on Instagram. We are adding the ability for brands to add a **referral parameter** to these ig.me links to create personalized messaging experiences.
**Instagram API New Onboarding Flow**  
We are announcing a [new onboarding flow for the Instagram API](https://developers.facebook.com/docs/instagram/business-login-for-instagram) as a beta. Developers can sign up for our beta interest list before June 29.
* * *
March 15, 2022
We have launched the [Persistent Menu for Messenger API support for Instagram](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/features/persistent-menu). This enables users to discover and interact with a Page’s main features.
* * *
November 11, 2021
Messenger API for Instagram is now available for Instagram Creators account type with less than 500K followers. Please see details in the [developer documentation](https://developers.facebook.com/docs/messenger-platform/instagram/rollout).
* * *
November 9, 2021
  * We have updated [Private Reply](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/features/private-replies) on Instagram to support comments on Instagram Live videos. Please refer to the [developer documentation](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/features/private-replies) for details on implementation.


* * *
October 20, 2021
  * IG comments [webhook](https://developers.facebook.com/docs/graph-api/webhooks/reference/instagram#comments) and [API](https://developers.facebook.com/docs/instagram-api/reference/ig-comment) are updated with additional fields. Please refer to the developer documentation for more details on new fields.
  * Starting support for [IG.me link](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/features/ig-me-links), a shortened URL service that directs users to messaging experience on Instagram. Developers can use the link format `https://ig.me/m/{ig_profile_handle}` on website, email, and more. Please refer to the [developer documentation](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/features/ig-me-links) for more details.
  * We have made updates to the [Ice Breaker](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/features/ice-breakers) on Instagram to support multiple versions in different languages. Developers can now set up Ice Breakers in different languages and serve the right version to users based on user locale. Please refer to the [developer documentation](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/features/ice-breakers) for more details.


* * *
September 14, 2021
  * Handover Protocol Improvements 
    * We are making improvements to [Handover Protocol](https://developers.facebook.com/docs/messenger-platform/handover-protocol) which helps developers and businesses launch messaging experiences (i.e. apps) quickly, makes it easy to pass control of conversation between apps and ensures a great user experience by disallowing apps from interjecting ongoing conversations. Key improvements include [Exclusive mode](https://developers.facebook.com/docs/messenger-platform/handover-protocol#how-it-works), [Idle mode](https://developers.facebook.com/docs/messenger-platform/handover-protocol#how-it-works), [New APIs for finer control over thread ownership](https://developers.facebook.com/docs/messenger-platform/handover-protocol/conversation-control) and [removing the requirement to assign primary or secondary roles for apps](https://developers.facebook.com/docs/messenger-platform/handover-protocol#how-it-works)
    * Note that developers and businesses who currently use Handover Protocol need to implement the changes to their current Handover Protocol implementation by March 1st, 2022. Please refer to the [migration guide](https://developers.facebook.com/docs/messenger-platform/handover-protocol-v2#migration-guide) and [breaking changes](https://developers.facebook.com/docs/messenger-platform/handover-protocol-v2#breaking-changes) sections for more details.
  * Custom Labels API - We are making exciting updates to the [Custom Labels API](https://developers.facebook.com/documentation/business-messaging/messenger-platform/identity/custom-labels) that would allow businesses to create, update and delete labels and sync the labels between the Facebook Page Inbox and any other tool the business might be using to communicate with their customers. 
    1. In order to use the Custom Labels API after October 1st, 2021 businesses need to accept our new _Page Contact Terms._ These terms describe Meta’s data practices for the Custom Labels created by the business. We will be rolling out the Page Contact Terms acceptance requirement to Facebook Pages on a rolling basis starting October 1st.
    2. Graph API `v12.0`+ Custom Labels API `name` field will be replaced with `page_label_name`. This change will take effect on all older Graph API versions starting Dec 14, 2021. Developer should leverage `page_label_name` across various CRUD (Create, Retrieve, Update, Delete) API calls and webhooks.
  * [Messenger API Updates for Europe and Japan](https://developers.facebook.com/documentation/business-messaging/messenger-platform/europe-japan-updates) - We have restored [Customer Feedback Template](https://developers.facebook.com/documentation/business-messaging/messenger-platform/send-messages/templates/customer-feedback-template) in the Messenger API that wasn’t available to businesses in Europe, and for people in Europe and Japan who connect with businesses globally. Details [here](https://developers.facebook.com/documentation/business-messaging/messenger-platform/europe-japan-updates).
  * Messenger API for Instagram updates 
    * [Reaction Webhook](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/webhooks) - We have updated emoji reactions to return a new unicode format and support multiple emoji reactions. Please refer to the [developer documentation](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/webhooks) and migrate to the new version before December 14, 2021 in order to continue supporting emoji reactions.
  * [User Profile API](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/features/user-profile) - We have updated User Profile API to include additional fields that are publicly available on the Instagram app. Please refer to the [developer documentation](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/features/user-profile) for details.
  * IGID Deprecation - [Conversation API](https://developers.facebook.com/documentation/business-messaging/messenger-platform/conversations) will no longer return `IGID` field and fully rely on `IGSID` field. See [developer documentation](https://developers.facebook.com/documentation/business-messaging/messenger-platform/conversations) for details in order to migrate before December 14, 2021.
  * [Facebook Chat Plugin Customization API](https://developers.facebook.com/documentation/business-messaging/messenger-platform/discovery) - We are launching Chat Plugin customization settings through API. With this new release, developers will be able to edit features including the position, color, greetings, guest mode settings, etc. that are currently only available using our first-party tools today.
  * [Message Echo webhook](https://developers.facebook.com/documentation/business-messaging/messenger-platform/reference/webhook-events/message-echoes) will now include the app id for Facebook Page Inbox as part of Graph API `v12.0` - When a business responds to a Messenger conversation from Facebook Page Inbox, other apps connected to the Page can listen to the Message Echo webhook. These apps will receive an echo webhook with the Facebook Page inbox app id (`263902037430900`).


* * *
August 16, 2021
  * [Messenger API for Instagram](https://developers.facebook.com/docs/messenger-platform/instagram)- Messenger API for Instagram opened up to all developers in June, with an opportunity to build for IG business accounts with follower counts between 10k-100k. Now, developers can add Instagram messaging into their apps and build Instagram messaging experiences for all businesses on Instagram. The use of Messenger API for Instagram must comply with the [Developer Policies](https://developers.facebook.com/devpolicy#messengerplatform), particularly the policies listed under ‘Messenger and Instagram Messaging APIs’, as well as the [technical documentation](https://developers.facebook.com/docs/messenger-platform/instagram).


* * *
August 6, 2021
  * [Private Replies](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/features/private-replies) on Instagram Messaging API no longer need to be sent using the Human Agent Message Tag. Private Reply API calls with the [Human Agent Tag](https://developers.facebook.com/documentation/business-messaging/messenger-platform/reference/send-api) will stop working after Sept 13, 2021.


* * *
July 7, 2021
  * [Messenger API for Instagram](https://developers.facebook.com/docs/messenger-platform/instagram) - Messenger API for Instagram opened up to all developers in June, with an opportunity to build for IG business accounts with follower counts between 10k-100k. We are expanding the rollout to IG business accounts with follower counts between 1K-10K. Now, developers can add Instagram messaging into their apps and build Instagram messaging experiences for even more businesses. The use of Messenger API for Instagram must comply with the [Developer Policies](https://developers.facebook.com/devpolicy#messengerplatform), particularly the policies listed under ‘Messenger and Instagram Messaging APIs’, as well as the [technical documentation](https://developers.facebook.com/docs/messenger-platform/instagram).


* * *
June 22, 2021
  * [Generic Templates](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/generic-template), which allows you to send a structured message that includes an image, text and buttons, is now available for Instagram


* * *
June 8, 2021
The following changes apply to v11.0+
  * **Adding`<mid>` to `messaging_postback` events for Messenger and Messenger API for Instagram for Graph API V11.0+** - We are adding the Message Id (`<mid>`) field as part of the `messaging_postback` payload to help reduce engineering overheads for our partners who have had to rely on the [Conversations API](https://developers.facebook.com/docs/graph-api/reference/v10.0/conversation) to fetch conversation history and then compare it with the webhook events. See more details [here](https://developers.facebook.com/documentation/business-messaging/messenger-platform/reference/webhook-events/messaging_postbacks).
  * **[Airline Templates are deprecated](https://developers.facebook.com/docs/messenger-platform/send-messages/template/airline)**  _-_ Airline Templates will no longer be supported starting Graph API v11. Deprecation for the prior versions of the Graph API will occur 6 months after the announcement of this change on Dec 6, 2021. We recommend airlines send [Boarding Pass](https://developers.facebook.com/docs/messenger-platform/reference/templates/airline-boarding-pass) and [Check-in](https://developers.facebook.com/docs/messenger-platform/reference/templates/airline-checkin) templates as images which are consistent with how they typically send these notifications in other channels.


* * *
June 2, 2021
  * [Messenger API for Instagram](https://developers.facebook.com/docs/messenger-platform/instagram) - We have opened up the Messenger API for Instagram to all developers who are making it possible for brands to offer messaging experiences on Instagram at scale. Now, developers can add Instagram messaging into their apps and build experiences for Instagram messaging. Developers can help businesses use different applications to leverage existing workflows, drive more meaningful conversations, increase customer satisfaction, and grow sales. Learn more [here](https://developers.facebook.com/docs/messenger-platform/instagram). The use of Messenger API for Instagram must comply with the [Developer Policies](https://developers.facebook.com/devpolicy#messengerplatform), particularly the policies listed under ‘Messenger and Instagram Messaging APIs’, as well as the [technical documentation](https://developers.facebook.com/docs/messenger-platform/instagram).
  * [Human Agent message tag](https://developers.facebook.com/documentation/business-messaging/messenger-platform/reference/send-api) now available to all developers - This tag allows businesses to respond to user messages on Messenger and Instagram manually outside the 24-hour standard messaging window up to 7days. This tag is helpful especially for use cases such as weekend closures or for inquiries that need more than 24 hours to resolve. Developers should apply for the Human Agent tag permission via the App dashboard even if your app has been previously approved for Human Agent message tag. Navigate to the “Permissions and Features” section of the app dashboard and apply for the “Human Agent” permission. Learn more [here](https://developers.facebook.com/documentation/business-messaging/messenger-platform/reference/send-api).
  * [Customer Feedback Template](https://developers.facebook.com/documentation/business-messaging/messenger-platform/send-messages/templates/customer-feedback-template)  _is now available as Beta_ - We are launching a native template within Messenger that supports common survey formats such as CSAT (Customer Satisfaction), NPS (Net Promoter Score), CES (Customer Effort Score) and free form text. The native template is easier to integrate because it’s built on Send API, eliminates the need to build custom survey solutions using Webview and makes it easy for developers to aggregate scores across channels that use similar survey formats. Learn more [here](https://developers.facebook.com/documentation/business-messaging/messenger-platform/send-messages/templates/customer-feedback-template).


* * *
* * *
![Meta](https://static.xx.fbcdn.net/rsrc.php/y9/r/tL_v571NdZ0.svg)
[![Facebook](https://scontent-mia5-1.xx.fbcdn.net/v/t39.2365-6/425860105_925920989121941_6933048753023841367_n.svg?_nc_cat=1&ccb=1-7&_nc_sid=aa6a2f&_nc_ohc=ae5txUzRuuYQ7kNvwHC0XyY&_nc_oc=Adr8veNI20SUSJDzX_Z51cCxhhYGaGpxFPX9xQA1lJxzRob8b9OD_uclUGANsIP-EEM&_nc_zt=14&_nc_ht=scontent-mia5-1.xx&_nc_gid=fUIBUOY8DnW7y4TQucZizg&_nc_ss=7b289&oh=00_AQS1_gA8GgpaA154bsIU8cXf0IN0wIkTuxsiwhqpvPhK2A&oe=6AE954A2)](https://www.facebook.com/MetaforDevelopers)[![Instagram](https://scontent-mia5-1.xx.fbcdn.net/v/t39.2365-6/425804778_757649995874129_6917476492193301523_n.svg?_nc_cat=1&ccb=1-7&_nc_sid=aa6a2f&_nc_ohc=3TM3ED2Lx2gQ7kNvwEVEV2E&_nc_oc=AdqW-kwhO6AEf3rBtpDNMuvYufNQLZzX2ingBmNiAR20r_r30wikMwhIGY92cy-K9LA&_nc_zt=14&_nc_ht=scontent-mia5-1.xx&_nc_gid=fUIBUOY8DnW7y4TQucZizg&_nc_ss=7b289&oh=00_AQQKNSwd-H2K5cFhBVgUsuqoMbW600-MqXRD7I-eFh1CRw&oe=6AE93EB8)](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.instagram.com%2Fmetafordevelopers%2F&h=AUCJmPOC0M_PZZvmz2TVZF_HPNHmcCJb62xGoJbIZuR4sJggG58YXRqDMGmcss3kwUbi6Su1s87iC08uOxos15BXhxbd9cQ6GxXAzyUlWZ9ZhzVHyGQAMTJGN0TOkSu6hu4cfGg7RwW7vg)[![X](https://scontent-mia5-1.xx.fbcdn.net/v/t39.2365-6/426747931_385023204117867_5811151062540225287_n.svg?_nc_cat=1&ccb=1-7&_nc_sid=aa6a2f&_nc_ohc=Xe5MMfN34ssQ7kNvwEwfjeY&_nc_oc=AdoITz2Q-FwhJ-VIlzRxMM2rEzmshnHlWUMCRiHu8360qbjf8GocpVE7wsFXCZtCgSk&_nc_zt=14&_nc_ht=scontent-mia5-1.xx&_nc_gid=fUIBUOY8DnW7y4TQucZizg&_nc_ss=7b289&oh=00_AQRnpvJmq6d5FLiaznkSOOaTk7ObZEb6uIvHwhfgXMjbGA&oe=6AE95D2A)](https://l.facebook.com/l.php?u=https%3A%2F%2Ftwitter.com%2Fmetafordevs&h=AUCJmPOC0M_PZZvmz2TVZF_HPNHmcCJb62xGoJbIZuR4sJggG58YXRqDMGmcss3kwUbi6Su1s87iC08uOxos15BXhxbd9cQ6GxXAzyUlWZ9ZhzVHyGQAMTJGN0TOkSu6hu4cfGg7RwW7vg)[![LinkedIn](https://scontent-mia3-2.xx.fbcdn.net/v/t39.2365-6/467689750_1684384502343829_7561568713040200172_n.svg?_nc_cat=103&ccb=1-7&_nc_sid=aa6a2f&_nc_ohc=ysnjNBowAQUQ7kNvwH52CpT&_nc_oc=AdqCd0G3oGEQOTelp2T5pGHqvpwBNnezdIT_cgGyxnsg3XcizKgjt92ykj1EXXcWhSQ&_nc_zt=14&_nc_ht=scontent-mia3-2.xx&_nc_gid=fUIBUOY8DnW7y4TQucZizg&_nc_ss=7b289&oh=00_AQQRKREG9jG6skG7OieFaUxsgvpg9pDcrpCKMGfNHI8yhw&oe=6AE96CBE)](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.linkedin.com%2Fshowcase%2Fmeta-for-developers%2F&h=AUCJmPOC0M_PZZvmz2TVZF_HPNHmcCJb62xGoJbIZuR4sJggG58YXRqDMGmcss3kwUbi6Su1s87iC08uOxos15BXhxbd9cQ6GxXAzyUlWZ9ZhzVHyGQAMTJGN0TOkSu6hu4cfGg7RwW7vg)[![YouTube](https://scontent-mia5-1.xx.fbcdn.net/v/t39.2365-6/425519002_724756916408357_7491658959807896355_n.svg?_nc_cat=1&ccb=1-7&_nc_sid=aa6a2f&_nc_ohc=oG_Saoc72KsQ7kNvwHhe09m&_nc_oc=Adqmadw82MDErKrFaafimlzWlMGUhE9M8yfZfOVvk_tiCrAL3qez5SY61T_-JhrHbjU&_nc_zt=14&_nc_ht=scontent-mia5-1.xx&_nc_gid=fUIBUOY8DnW7y4TQucZizg&_nc_ss=7b289&oh=00_AQTW8oVLogT7PjcsTo6pBtYRDNEDju3fKuAkySwaiLNPVg&oe=6AE957DF)](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.youtube.com%2FMetaDevelopers%2F&h=AUCJmPOC0M_PZZvmz2TVZF_HPNHmcCJb62xGoJbIZuR4sJggG58YXRqDMGmcss3kwUbi6Su1s87iC08uOxos15BXhxbd9cQ6GxXAzyUlWZ9ZhzVHyGQAMTJGN0TOkSu6hu4cfGg7RwW7vg)
Build with Meta
Build with Meta
[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F&h=AUCJmPOC0M_PZZvmz2TVZF_HPNHmcCJb62xGoJbIZuR4sJggG58YXRqDMGmcss3kwUbi6Su1s87iC08uOxos15BXhxbd9cQ6GxXAzyUlWZ9ZhzVHyGQAMTJGN0TOkSu6hu4cfGg7RwW7vg)
[Meta Horizon ](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F&h=AUCJmPOC0M_PZZvmz2TVZF_HPNHmcCJb62xGoJbIZuR4sJggG58YXRqDMGmcss3kwUbi6Su1s87iC08uOxos15BXhxbd9cQ6GxXAzyUlWZ9ZhzVHyGQAMTJGN0TOkSu6hu4cfGg7RwW7vg)
[Social technologies](https://developers.facebook.com/social-technologies/)
[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F&h=AUCJmPOC0M_PZZvmz2TVZF_HPNHmcCJb62xGoJbIZuR4sJggG58YXRqDMGmcss3kwUbi6Su1s87iC08uOxos15BXhxbd9cQ6GxXAzyUlWZ9ZhzVHyGQAMTJGN0TOkSu6hu4cfGg7RwW7vg)
* * *
News
News
[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F&h=AUCJmPOC0M_PZZvmz2TVZF_HPNHmcCJb62xGoJbIZuR4sJggG58YXRqDMGmcss3kwUbi6Su1s87iC08uOxos15BXhxbd9cQ6GxXAzyUlWZ9ZhzVHyGQAMTJGN0TOkSu6hu4cfGg7RwW7vg)
[Blog](https://developers.facebook.com/blog/)
[Success stories](https://developers.facebook.com/success-stories/)
* * *
Support
Support
[Developer Support](https://developers.facebook.com/support/)
[Bug tool](https://developers.facebook.com/support/bugs/)
[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F&h=AUCJmPOC0M_PZZvmz2TVZF_HPNHmcCJb62xGoJbIZuR4sJggG58YXRqDMGmcss3kwUbi6Su1s87iC08uOxos15BXhxbd9cQ6GxXAzyUlWZ9ZhzVHyGQAMTJGN0TOkSu6hu4cfGg7RwW7vg)
[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)
[Report an incident](https://developers.facebook.com/incident/report/)
* * *
About us
About us
[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AUCJmPOC0M_PZZvmz2TVZF_HPNHmcCJb62xGoJbIZuR4sJggG58YXRqDMGmcss3kwUbi6Su1s87iC08uOxos15BXhxbd9cQ6GxXAzyUlWZ9ZhzVHyGQAMTJGN0TOkSu6hu4cfGg7RwW7vg)
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

