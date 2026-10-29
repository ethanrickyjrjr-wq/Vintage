[ Skip to main content ](https://developers.google.com/youtube/data/determine_quota_cost#main-content)
[ ![YouTube](https://developers.google.com/static/site-assets/logo-youtube.svg) ](https://developers.google.com/youtube)
  * [ YouTube ](https://developers.google.com/youtube)
  * [ Data API ](https://developers.google.com/youtube/data)


`/`
  * English
  * Deutsch
  * Español
  * Español – América Latina
  * Français
  * Indonesia
  * Italiano
  * Polski
  * Português – Brasil
  * Tiếng Việt
  * Türkçe
  * Русский
  * עברית
  * العربيّة
  * فارسی
  * हिंदी
  * বাংলা
  * ภาษาไทย
  * 中文 – 简体
  * 中文 – 繁體
  * 日本語
  * 한국어

Sign in
[ Home ](https://developers.google.com/youtube/data) [ Guides ](https://developers.google.com/youtube/data/getting-started) [ Reference ](https://developers.google.com/youtube/data/reference/rest) [ Samples ](https://developers.google.com/youtube/data/code_samples)
[ ![YouTube](https://developers.google.com/static/site-assets/logo-youtube.svg) ](https://developers.google.com/youtube)
  * [ YouTube ](https://developers.google.com/youtube)
  * [ Data API ](https://developers.google.com/youtube/data)


  * [ Home  ](https://developers.google.com/youtube/data)
  * [ Guides  ](https://developers.google.com/youtube/data/getting-started)
  * [ Reference  ](https://developers.google.com/youtube/data/reference/rest)
  * [ Samples  ](https://developers.google.com/youtube/data/code_samples)


  * [Overview](https://developers.google.com/youtube/data/getting-started)
  * [Client Libraries](https://developers.google.com/youtube/data/libraries)
  * Authorize Requests
    * [Overview](https://developers.google.com/youtube/data/guides/authentication)
    * [Get Auth Credentials](https://developers.google.com/youtube/registering_an_application)
    * [Server-side Web Apps](https://developers.google.com/youtube/data/guides/auth/server-side-web-apps)
    * [Client-side Web Apps](https://developers.google.com/youtube/data/guides/auth/client-side-web-apps)
    * [Installed Apps](https://developers.google.com/youtube/data/guides/auth/installed-apps)
    * [Devices](https://developers.google.com/youtube/data/guides/auth/devices)
  * Quickstarts
    * [Android](https://developers.google.com/youtube/data/quickstart/android)
    * [Apps Script](https://developers.google.com/youtube/data/quickstart/apps-script)
    * [Go](https://developers.google.com/youtube/data/quickstart/go)
    * [iOS](https://developers.google.com/youtube/data/quickstart/ios)
    * [Java](https://developers.google.com/youtube/data/quickstart/java)
    * [JavaScript](https://developers.google.com/youtube/data/quickstart/js)
    * [Node.js](https://developers.google.com/youtube/data/quickstart/nodejs)
    * [PHP](https://developers.google.com/youtube/data/quickstart/php)
    * [Python](https://developers.google.com/youtube/data/quickstart/python)
    * [Ruby](https://developers.google.com/youtube/data/quickstart/ruby)
  * Guides and Tutorials
    * [Quota costs for API requests](https://developers.google.com/youtube/data/determine_quota_cost)
    * [Quota and Compliance Audits](https://developers.google.com/youtube/data/guides/quota_and_compliance_audits)
    * [Upload a Video](https://developers.google.com/youtube/data/guides/uploading_a_video)
    * [Send Resumable Uploads](https://developers.google.com/youtube/data/guides/using_resumable_upload_protocol)
    * [Find MadeForKids video status](https://developers.google.com/youtube/data/guides/made_for_kids_status)
    * [Subscribe to Push Notifications](https://developers.google.com/youtube/data/guides/push_notifications)
    * [Work with Channel IDs](https://developers.google.com/youtube/data/guides/working_with_channel_ids)
    * [Move from ClientLogin to OAuth](https://developers.google.com/youtube/data/guides/moving_to_oauth)
  * [Sample Requests](https://developers.google.com/youtube/data/sample_requests)
  * Implementation Guide
    * [Overview](https://developers.google.com/youtube/data/guides/implementation)
    * [Activities](https://developers.google.com/youtube/data/guides/implementation/activities)
    * [Captions](https://developers.google.com/youtube/data/guides/implementation/captions)
    * [Channels](https://developers.google.com/youtube/data/guides/implementation/channels)
    * [Comments](https://developers.google.com/youtube/data/guides/implementation/comments)
    * [Pagination](https://developers.google.com/youtube/data/guides/implementation/pagination)
    * [Partial responses](https://developers.google.com/youtube/data/guides/implementation/partial)
    * [Playlists](https://developers.google.com/youtube/data/guides/implementation/playlists)
    * [Ratings](https://developers.google.com/youtube/data/guides/implementation/ratings)
    * [Search requests](https://developers.google.com/youtube/data/guides/implementation/search)
    * [Subscriptions](https://developers.google.com/youtube/data/guides/implementation/subscriptions)
    * [Videos](https://developers.google.com/youtube/data/guides/implementation/videos)
  * Tools
    * [APIs Explorer](https://developers.google.com/apis-explorer/#p/youtube/v3/)


  * [ Home ](https://developers.google.com/)
  * [ Products ](https://developers.google.com/products)
  * [ YouTube ](https://developers.google.com/youtube)
  * [ Data API ](https://developers.google.com/youtube/data)
  * [ Guides ](https://developers.google.com/youtube/data/getting-started)


#  Quota Calculator Stay organized with collections  Save and categorize content based on your preferences. 
The following table shows the quota cost for calling each API method. All API requests, including invalid requests, incur a quota cost of at least one point.
Projects that enable the YouTube Data API have a default quota allocation of 100 `search.list` calls, 100 `videos.insert` calls, and 10,000 units per day combined for all other endpoints. You can see your quota usage on [Quotas ](https://console.cloud.google.com/iam-admin/quotas) page in the Google Cloud console. Daily quotas reset at midnight Pacific Time (PT).
The following points are worth calling out as they both affect your quota usage:
  * The `search.list` and `videos.insert` methods have their own quota buckets. Each of these methods has a default daily limit of 100 per day. The quota cost is 1 per call.
  * If your application calls a method, such as `search.list`, that returns multiple pages of results, each request to retrieve an additional page of results incurs the estimated quota cost.
  * [YouTube Live Streaming API](https://developers.google.com/youtube/data/live) methods are, technically, part of the YouTube Data API, and calls to those methods also incur quota costs. As such, API methods for live streaming are also listed in the table. 

  
| Quota costs  |  
| --- |  
| resource  | method  | cost  |  
| 
### activities
 | list  | 1  |  
| 
### captions
 | list  | 50  |  
|   | insert  | 400  |  
|   | update  | 450  |  
|   | delete  | 50  |  
| 
### channelBanners
 | insert  | 50  |  
| 
### channels
 | list  | 1  |  
|   | update  | 50  |  
| 
### channelSections
 | list  | 1  |  
|   | insert  | 50  |  
|   | update  | 50  |  
|   | delete  | 50  |  
| 
### comments
 | list  | 1  |  
|   | insert  | 50  |  
|   | update  | 50  |  
|   | setModerationStatus  | 50  |  
|   | delete  | 50  |  
| 
### commentThreads
 | list  | 1  |  
|   | insert  | 50  |  
|   | update  | 50  |  
| 
### guideCategories
 | list  | 1  |  
| 
### i18nLanguages
 | list  | 1  |  
| 
### i18nRegions
 | list  | 1  |  
| 
### liveBroadcasts
 | bind  | 1  |  
|   | delete  | 1  |  
|   | insert  | 1  |  
|   | insertCuepoint  | 1  |  
|   | list  | 1  |  
|   | transition  | 1  |  
|   | update  | 1  |  
| 
### liveChatBans
 | delete  | 200  |  
|   | insert  | 200  |  
| 
### liveChatMessages
 | delete  | 20  |  
|   | insert  | 20  |  
|   | list  | 5  |  
|   | streamList  | 5  |  
|   | transition  | 20  |  
| 
### liveChatModerators
 | delete  | 200  |  
|   | insert  | 200  |  
|   | list  | 50  |  
| 
### liveStreams
 | delete  | 1  |  
|   | insert  | 1  |  
|   | list  | 1  |  
|   | update  | 1  |  
| 
### members
 | list  | 1  |  
| 
### membershipsLevels
 | list  | 1  |  
| 
### playlistItems
 | list  | 1  |  
|   | insert  | 50  |  
|   | update  | 50  |  
|   | delete  | 50  |  
| 
### playlists
 | list  | 1  |  
|   | insert  | 50  |  
|   | update  | 50  |  
|   | delete  | 50  |  
| 
### search
 | list  | 100 quota per day. Each call costs 1 quota.  |  
| 
### subscriptions
 | list  | 1  |  
|   | insert  | 50  |  
|   | delete  | 50  |  
| 
### superChatEvents
 | list  | 1  |  
| 
### thumbnails
 | set  | 50  |  
| 
### videoAbuseReportReasons
 | list  | 1  |  
| 
### videoCategories
 | list  | 1  |  
| 
### videos
 | list  | 1  |  
|   | insert  | 100 quota per day. Each call costs 1 quota.  |  
|   | update  | 50  |  
|   | rate  | 50  |  
|   | getRating  | 1  |  
|   | reportAbuse  | 50  |  
|   | delete  | 50  |  
| 
### watermarks
 | set  | 50  |  
|   | unset  | 50  |  
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-15 UTC.
[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
  * [ ![Blog](https://developers.google.com/static/site-assets/logo-youtube.svg) Blog  ](https://blog.youtube)
The latest news on the YouTube blog
  * [ ![Issue Tracker](https://developers.google.com/static/site-assets/developers_64dp.png) Issue Tracker  ](https://issuetracker.google.com/issues/new?component=186600&template=874803)
Something wrong? Send us a bug report!
  * [ ![YouTube Researcher Program](https://developers.google.com/static/site-assets/logo-youtube.svg) YouTube Researcher Program  ](https://research.youtube/)
For researchers interested in using data from YouTube's global API


  * ### Tools
    * [ Google APIs Explorer ](https://developers.google.com/apis-explorer/#p/)
    * [ YouTube Player Demo ](https://developers.google.com/youtube/youtube_player_demo)
    * [ Configure a Subscribe Button ](https://developers.google.com/youtube/youtube_subscribe_button)
  * ### Issue Tracker
    * [ File a bug ](https://issuetracker.google.com/issues/new?component=186600&template=874803)
    * [ Request a feature ](https://issuetracker.google.com/issues/new?component=186600&template=874803)
    * [ See open issues ](https://issuetracker.google.com/issues?q=componentid:186600)
  * ### Product Info
    * [ Terms of Service ](https://developers.google.com/youtube/terms/api-services-terms-of-service)
    * [ Developer Policies ](https://developers.google.com/youtube/terms/developer-policies)
    * [ Required Minimum Functionality ](https://developers.google.com/youtube/terms/required-minimum-functionality)
    * [ Branding Guidelines ](https://developers.google.com/youtube/terms/branding-guidelines)


[ ![Google Developers](https://www.gstatic.com/devrel-devsite/prod/vc1b996b07630b7fba08b3b2fd258fb35e39e5d8dfeab71af65465d9a2fbe5870/developers/images/lockup-google-for-developers.svg) ](https://developers.google.com/)
  * [ Android ](https://developer.android.com)
  * [ Chrome ](https://developer.chrome.com/home)
  * [ Firebase ](https://firebase.google.com)
  * [ Google Cloud Platform ](https://cloud.google.com)
  * [ Google AI ](https://ai.google.dev/)
  * [ All products ](https://developers.google.com/products)


  * [ Terms ](https://developers.google.com/terms/site-terms)
  * [ Privacy ](https://policies.google.com/privacy)
  * [ Manage cookies ](https://developers.google.com/youtube/data/determine_quota_cost)


  * English
  * Deutsch
  * Español
  * Español – América Latina
  * Français
  * Indonesia
  * Italiano
  * Polski
  * Português – Brasil
  * Tiếng Việt
  * Türkçe
  * Русский
  * עברית
  * العربيّة
  * فارسی
  * हिंदी
  * বাংলা
  * ภาษาไทย
  * 中文 – 简体
  * 中文 – 繁體
  * 日本語
  * 한국어



