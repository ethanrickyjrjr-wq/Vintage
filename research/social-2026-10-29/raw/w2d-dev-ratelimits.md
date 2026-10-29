
```
# Instagram Platform overview



The Instagram Platform is a collection of APIs that allows your app to access data for Instagram professional accounts, including business and creator accounts. You can build an app that serves only an account you own or manage, or an app that serves app users' Instagram professional accounts.

There are three Instagram API setups:

- [Instagram API with Unified Login](https://developers.facebook.com/documentation/instagram-platform/instagram-api-with-unified-login) is recommended for new integrations. App users can connect their Instagram professional account by logging in with either Instagram or Facebook, without a Facebook Page.
- [Instagram API with Instagram Login](https://developers.facebook.com/documentation/instagram-platform/instagram-api-with-instagram-login) serves Instagram professional accounts without requiring a linked Facebook Page.
- [Instagram API with Facebook Login](https://developers.facebook.com/documentation/instagram-platform/instagram-api-with-facebook-login) serves Instagram professional accounts linked to a Facebook Page.

Depending on the configuration and features you use, app users can have conversations with end users, moderate comments, send private replies, publish content, publish ads, and get insights.

## Which API setup is right for my app? {#which-api-is-right-for-my-app}

| Component | [Unified Login](https://developers.facebook.com/documentation/instagram-platform/instagram-api-with-unified-login) | [Instagram Login](https://developers.facebook.com/documentation/instagram-platform/instagram-api-with-instagram-login) | [Facebook Login](https://developers.facebook.com/documentation/instagram-platform/instagram-api-with-facebook-login) |
|---|---|---|---|
| **Recommended use** | New integrations | Existing Instagram Login integrations | Existing Page-linked integrations |
| **App user login** | Instagram or Facebook credentials | Instagram credentials | Facebook credentials |
| **Authorization** | [Facebook Login for Business](https://developers.facebook.com/documentation/facebook-login/facebook-login-for-business) | [Business Login for Instagram](https://developers.facebook.com/documentation/instagram-platform/instagram-api-with-instagram-login/business-login) | [Facebook Login for Business](https://developers.facebook.com/documentation/facebook-login/facebook-login-for-business) |
| **Access token** | Business Integration System User Access Token | Instagram User access token | Facebook User or Page access token |
| **API host** | `graph.facebook.com` | `graph.instagram.com` | `graph.facebook.com` |
| **Primary request object** | Instagram professional account ID | Instagram professional account ID or `/me` | Facebook Page ID or `/me` |
| **Facebook Page** | Not required | Not required | Required |
| **Business portfolio** | Required | Not required by the login flow | Depends on the Facebook Login for Business configuration |
| **Permissions** | Uses the `instagram_*` permission family and other [Facebook Login for Business permissions](https://developers.facebook.com/documentation/instagram-platform/instagram-api-with-unified-login/permissions) | Uses the `instagram_business_*` permission family | Uses the `instagram_*` permission family and applicable Page permissions |
| **Comment moderation** | Supported | Supported | Supported |
| **Content publishing** | Supported | Supported | Supported |
| **Hashtag search** | Supported | Not supported | Supported |
| [**Insights**](https://developers.facebook.com/documentation/instagram-platform/insights) | Supported | Supported | Supported |
| **Mentions** | Supported | Supported | Supported |
| **Messaging** | Supported | Supported | [Supported through Messenger Platform](https://developers.facebook.com/documentation/business-messaging/instagram-messaging) |
| [**Product tagging**](https://developers.facebook.com/documentation/instagram-platform/instagram-api-with-facebook-login/product-tagging) | Supported | Not supported | Supported |
| [**Partnership ads**](https://developers.facebook.com/documentation/ads-commerce/marketing-api/ad-creative/partnership-ads) | Supported | Not supported | Supported |

## Access levels

There are two access levels available to your app: **Standard Access** and **Advanced Access**.

**Standard Access**

Standard Access is the default access level for all apps and limits the data your app can get. It is intended for apps that will only be used by people who have roles on them, during app development, or for testing your app. If your app only serves your Instagram professional account or an account you manage, Standard Access is all your app needs.

**Advanced Access**

Advanced Access is the access level required if your app serves Instagram professional accounts that you don't own or manage and can be used by app users who do not have a role on your app or a role on a business portfolio that has claimed your app. This access level requires App Review and Business Verification.

**Note:** Because of the limited scope of Standard Access, some features might not work properly until your app has been granted Advanced Access. This might limit the functionality of any test apps you use.

Learn more about
[Advanced and Standard Access.](https://developers.facebook.com/docs/graph-api/overview/access-levels)

## App Review

Meta App Review enables Meta to verify that your app uses our products and APIs in an approved manner. Your app must complete Meta App Review to be granted Advanced Access. Learn more about
[Meta App Review.](https://developers.facebook.com/documentation/resp-plat-initiatives/individual-processes/app-review)

#### Private apps

If reviewers are unable to test your app because it is behind a private intranet, has no user interface, or has not implemented Facebook Login for Business, you can request approval only for the following permissions:

* `instagram_basic`
* `instagram_manage_comments`

## App users

To use the APIs, your app users must have an [Instagram professional account](https://business.instagram.com/getting-started). An Instagram professional account can represent a business or creator. The Instagram API with Unified Login and the Instagram API with Instagram Login can serve app users who don't have a Facebook Page. Facebook Login serves app users whose Instagram professional account is linked to a Facebook Page. For a Page-linked setup, your app user must also be able to perform admin-equivalent tasks on the linked Facebook Page.

Your app will also interact with Instagram users who interact with your app users' Instagram professional accounts. These interactions can happen through comments and reactions on your app users' Instagram comments, posts, reels, and stories, ads, and Instagram Direct.

## Authentication and authorization

Endpoint authorization is handled through [permissions and features.](#features-and-permissions) Before your app can use an endpoint to access an app user's Instagram professional account data, you must first request all permissions required by those endpoints from the app user.

You can request permissions through the Instagram API with Unified Login, Business Login for Instagram, or Facebook Login for Business. With the Instagram API with Unified Login, app users log in with Instagram or Facebook. Business Login for Instagram uses Instagram credentials, and Facebook Login for Business uses Facebook credentials. See [Authentication and access tokens](https://developers.facebook.com/documentation/instagram-platform/instagram-api-with-unified-login/authentication) for the Instagram API with Unified Login.

For Business Login for Instagram and the Page-linked Facebook Login setup, an app user starts the login flow from your **embed URL**. Meta opens an authorization window where the app user grants your app the requested permissions. Meta then redirects the app user to your app's redirect URI and sends your app an **Authorization Code**. This code is valid for **one hour**.

Next, exchange the authorization code for a **short-lived access token**, an ID for your app user, and a list of permissions granted by your app user. This access token is valid for **one hour**. Access tokens follow the OAuth 2.0 protocol, are app-scoped, and are required for most API calls. Apps using Business Login for Instagram receive Instagram User access tokens, and apps using Facebook Login for Business receive Facebook User access tokens.

Before the short-lived access token expires, your app exchange it for a **long-lived access token**. This access token is valid for **60 days** and can be refreshed before they expire.

Once permissions have been granted and your app receives an access token, your app can query the endpoints to access the user's data. Note that a permission only allows access to data created by the app user who granted the permission. There are a few endpoints that allow apps to access data not created by the app user, but the accessible data is limited and public.

If your app serves only your Instagram professional accounts, or accounts you manage, you do not need to implement a login flow. However, you will need to configure the business login settings in the App Dashboard to obtain an Instagram app ID and an Instagram app secret, as well as obtain long-lived access tokens to use in your API calls.

#### Features and permissions

The API uses the following permissions and features, which are based on login type:

| Instagram login | Facebook login |
| --- | --- |
| - `instagram_business_basic`<br>- `instagram_business_content_publish`<br>- `instagram_business_manage_comments`<br>- `instagram_business_manage_messages`<br>- Human Agent | - `instagram_basic`<br>- `instagram_content_publish`<br>- `instagram_manage_comments`<br>- `instagram_manage_insights`<br>- `instagram_manage_messages`<br>- `pages_show_list`<br>- `pages_read_engagement`<br>- Human Agent<br>- Instagram Public Content Access |

The **Human Agent** feature allows your app to have a human agent respond to user messages using the **human_agent** tag within 7 days of a user's message. The allowed usage for this feature is to provide human agent support in cases where a user’s issue cannot be resolved in the standard messaging window. Examples include when the business is closed for the weekend, or if the issue requires more than 24 hours to resolve.

The **Instagram Public Content Access** feature allows your app to access Instagram Graph API's Hashtag Search endpoints.


The allowed usages for this feature is to discover content associated with your hashtag campaigns, understand public sentiment around your brand or identify contest, competition and sweepstakes entrants. It can also be used to provide customer support and better understand and manage your audience.

See our [API Reference](https://developers.facebook.com/documentation/instagram-platform/reference) to determine which permission and features your app will need to request from app users.

## Base URLs

For apps using Business Login for Instagram, where your app users log in with their Instagram credentials, all endpoints are accessed via the **`graph.instagram.com`** host.

For apps using Facebook Login for Business, where your app users' Instagram professional account is linked to a Facebook Page and your app users log in with their Facebook credentials, all endpoints are accessed via the **`graph.facebook.com`** host.

## [Business verification](https://developers.facebook.com/documentation/development/release/business-verification)

You must complete Business Verification if your app requires Advanced Access; if your app will be used by app users who do not have a Role on the app itself, or a Role in a Business that has claimed the app.

## Comment moderation

An Instagram user comments on your app user's Instagram professional account's media. Your app can use the API to get comments, reply to comments, delete comments, hide/unhide comments, and disable/enable comments on Instagram media owned by your app user's Instagram professional account. The API can also identify media where the Instagram professional account has been @mentioned by other Instagram users.

## Content publishing

Your app can use the API to publish single images, videos, reels (single media posts), or posts containing multiple images and videos (carousel posts) on behalf of your app user's Instagram professional accounts.

#### Content Delivery Network URLs

Instagram Platform leverages Content Delivery Network (CDN) URLs which allow you to retrieve rich media content shared by Instagram users. The CDN URL is privacy-aware and will not return the media when the content has been deleted or has expired.

### Collaborators

_Facebook Login for Business only._

The [Instagram Collaborator Tags](https://www.facebook.com/help/instagram/291200585956732) allows Instagram users to co-author content, such as publish media with other accounts (collaborators).

With a few exceptions, data on or about co-authored media can only be accessed through the API by the user who published the media; collaborators are unable to access this data via the API. The only exceptions are when searching for top performing media or recently published media that has been tagged with a specific hashtag.

## [Develop with Meta](https://developers.facebook.com/documentation/development)

Before you can integrate a Meta Technologies API into your app, you must [register as a Meta developer](https://developers.facebook.com/documentation/development/register) and then create an app in the Meta App Dashboard that represents your app.

When creating an app, you will add the following products depending on login type:

|  | Business Login for Instagram | Facebook Login for Business |
| --- | --- | --- |
| **Products Required<br>** | * **Instagram** > Instagram API setup with Instagram login | • **Facebook Login for Business**<br>• **Messenger**, including Instagram settings for sending and receiving messages<br>• **Instagram** > Instagram API setup with Facebook login<br> |

### App IDs

App IDs are required during authentication and can be found in the app's Meta App Dashboard. Apps that use Facebook Login for Business will use the Meta app ID displayed at the top of the Meta App Dashboard for your app. Apps that use Business Login for Instagram will use the Instagram app ID displayed on the **Instagram > API setup with Instagram login** section of the dashboard.

## [Facebook Pages](https://help.instagram.com/570895513091465)

If your app implements Facebook Login for Business, your app users' Instagram professional accounts must be connected to a Facebook Page.

[Tasks](https://developers.facebook.com/documentation/facebook-login/guides/access-tokens#page-tasks)

Your app users must be able to perform **tasks** on the Facebook Page linked to their Instagram professional account so that they can grant your app permissions related to those tasks. The following table maps the name of the task in our UIs, such as Facebook Page Settings or Meta Business Suite, with task names returned in [`GET /me/accounts`](https://developers.facebook.com/docs/graph-api/reference/user/accounts#Reading) endpoint requests, and the permission the user can grant if they can perform that task.

| Task name in UIs | Task name in API | Grantable Permissions |
| --- | --- | --- |
| Ads | `PROFILE_PLUS_ADVERTISE` | `instagram_basic` |
| Content | `PROFILE_PLUS_CREATE_CONTENT` | `instagram_basic`<br>`instagram_content_publish` |
| Full control | `PROFILE_PLUS_FULL_CONTROL` | `instagram_basic`<br>`instagram_content_publish` |
| Insights | `PROFILE_PLUS_ANALYZE` | `instagram_basic`<br>`instagram_manage_insights` |
| Messages | `PROFILE_PLUS_MESSAGING` | `instagram_basic`  <br>`instagram_manage_messages` |
| Community Activity | `PROFILE_PLUS_MODERATE` | `instagram_basic`  <br>`instagram_manage_comments` |

See our [Instagram API Reference](https://developers.facebook.com/documentation/instagram-platform/reference) to see which permissions each endpoint requires.

## Scoped User IDs

Instagram-scoped User IDs

When an Instagram user comments on a post, reel, or story, or sends a message to an Instagram professional account, an Instagram-scoped User ID is created that represents that person on that app. This ID is specific to the person and the Instagram account they are interacting with. This allows your app users, businesses and creators, to map interactions for the same person across multiple apps.

Page-scoped User IDs

When an Instagram user comments on a post, reel, or story, or sends a message to an Instagram professional account, an Page-scoped User ID is created that represents that person on that app. This ID is specific to the person and the Instagram account they are interacting with. This allows your app users, businesses and creators, to map interactions for the same person across multiple apps.

## `/me` endpoint

The `/me` endpoint is a special endpoint that translates to the object ID of the account, Facebook Page or Instagram professional account, whose access token is currently being used to make the API calls. This special endpoint can also represent any ID, comments, conversations, media, posts, reels, and stories owned by your app user's Instagram professional account.

## Messaging

An Instagram user sends a message to your app user's Instagram professional account while logged in to Instagram. The message is delivered to your app user's Instagram inbox and a webhook notification is sent to your server. Your app can use the API to respond during the standard messaging window. The duration of the standard messaging window depends on the user action that opens it. For most user actions, it lasts 24 hours. When the user action is a person sending their first message after clicking a Click-to-Direct ad, the window may last up to 7 days from that message. If more time is needed to allow a human agent to respond, you can use the human agent tag to send a response during the separate 7-day Human Agent window.

If your app uses Facebook Login for Business, your app will use the [Messenger Platform's Instagram Messaging API](https://developers.facebook.com/documentation/business-messaging/instagram-messaging) to send and receive messages.

Instagram Inbox

An Instagram professional account has a messaging inbox that allows you to control notifications and organize messages. By default notifications are off. You can turn notifications on in the Inbox Settings. The inbox is organized into different categories, **Primary**, **General**, and **Requests**. By default, all new conversations from followers will appear in the Primary folder.
Conversations that existed before you implemented Instagram Messaging will be in the folders you have placed them within.
Messages that you receive from people who are not followers of your account are in Requests folder. You can choose to accept or deny these requests, and request messages aren't marked as **Seen** until you accept them. Once a request is accepted you can move the conversation to the Primary or General folder. All message requests that you answer using a third-party app will be moved to the General folder.

Inbox Limitations

* If you reply to a message using a third-party app, the conversation will be moved to the **General** folder regardless of your Setting configuration
* Inbox folders are not supported and messages delivered by the Messenger Platform do not include folder information that is shown in the Instagram from Meta app inbox folder
* Webhooks notifications or messages delivered via the API will not be considered as **Read** in the Instagram app inbox. Only after a reply is sent will a message be considered **Read**.

### Automated Experiences {#automated-experiences}

You can provide an escalation path for automated messaging experiences using one of the following:

- **A Single App** – You can create a custom inbox to receive or reply to messages from a person. This custom inbox is powered by the same messaging app that also provides the automated experience

- **Multiple Apps** – [Handover Protocol](https://developers.facebook.com/docs/messenger-platform/handover-protocol) allows you pass the conversation from one app or inbox to another. For example, one app would handle the conversation with an automated experience and, when needed, would pass the conversation to another app to continue the conversation with a human agent.

#### Informing Users About Your Automated Experience

When required by applicable law, automated chat experiences must disclose that a person is interacting with an automated service:

* at the beginning of any conversation or message thread,
* after a significant lapse of time, or
* when a chat moves from human interaction to automated experience.

Automated chat experiences that serve the following groups should pay special attention to this requirement:

* California market or California users
* German market or German users

Disclosures may include but are not limited to: “I’m the [Page Name] bot,”“You are interacting with an automated experience,” “You are talking to a bot,” or “I am an automated chatbot.”

Even where not legally required, we recommend informing users when they’re interacting with an automated chat as best practice, as this helps manage user expectations about their interaction with your messaging experience.

Visit our
[Developer Policies](https://developers.facebook.com/devpolicy/#messengerplatform)
for more information.

## Policies

To gain and retain access to the Meta social graph you must adhere to the following:

- [Automated chats on Instagram](https://help.instagram.com/655277382759165)

- [Meta Platform Terms](https://developers.facebook.com/terms/)

- [Developer Policies](https://developers.facebook.com/devpolicy)

- [Community Standards](https://transparency.meta.com/policies/community-standards/)

- [Responsible Platform Initiatives](https://developers.facebook.com/documentation/resp-plat-initiatives)

## Rate Limiting {#rate-limiting}

All endpoints are subject to
[Instagram Business Use Case rate limiting](https://developers.facebook.com/docs/graph-api/overview/rate-limiting#instagram-graph-api)
except for
[Business Discovery](https://developers.facebook.com/documentation/instagram-platform/instagram-api-with-facebook-login/business-discovery)
and
[Hashtag Search](https://developers.facebook.com/documentation/instagram-platform/instagram-api-with-facebook-login/hashtag-search)
endpoints, which are subject to
[Platform Rate limiting.](https://developers.facebook.com/docs/graph-api/overview/rate-limiting#platform-rate-limits)

Calls to the Instagram Platform endpoints, excluding messaging, are counted against the calling app's call count. An app's call count is unique for each app and app user pair, and is the number of calls the app has made in a rolling 24 hour window. It is calculated as follows:

`Calls within 24 hours = 4800 * Number of Impressions`

The Number of Impressions is the number of times any content from the app user's Instagram professional account has entered a person's screen within the last 24 hours.

#### Notes

- Business Discovery and Hashtag Search API are subject to  [Platform Rate Limits](https://developers.facebook.com/docs/graph-api/overview/rate-limiting#platform-rate-limits).

### Messaging Rate Limits

Calls to the Instagram messaging endpoints are counted against the number of calls your app can make per Instagram professional account and the API used.

#### Conversations API

* Your app can make 2 calls per second per Instagram professional account.

#### Private Replies API

* Your app can make 100 calls per second per Instagram professional account for private replies to Instagram Live comments
* Your app can make 750 calls per hour per Instagram professional account for private replies to comments on Instagram posts and reels

#### Send API

* Your app can make 100 calls per second per Instagram professional account for messages that contain text, links, reactions, and stickers
* Your app can make 10 calls per second per Instagram professional account for messages that contain audio or video content

## Webhooks

We strongly recommend using webhooks to receive notifications about your app users' media objects or messages. Using webhooks will reduce the number of needed API calls made by your app and hence, reducing the risk of being rate limited.

## Next steps

Now that you are familiar with the components of this API, set up your [webhooks server and subscribe to events](https://developers.facebook.com/documentation/instagram-platform/webhooks).

## See also

Learn more about [Meta's Graph API](https://developers.facebook.com/docs/graph-api) and the [Messenger Platform](https://developers.facebook.com/documentation/business-messaging/messenger-platform).


```


