[Skip to content](https://developers.pinterest.com/docs/key-concepts/access-tiers/)
## [Developer Platform](https://developers.pinterest.com/)
Docs
API reference
My apps
Search docs & API
[Log in](https://www.pinterest.com/business/login/?next=https://developers.pinterest.com/account-setup/)
[Sign up](https://www.pinterest.com/business/create/?next=https://developers.pinterest.com/account-setup/)
# Understanding our access tiers
Use with AI
The Pinterest API v5 significantly increases the scope of what is possible for you to create as a developer. If approved for API use, your app receives Trial access, which is best for exploring our API features. If you want to offer Pinterest capabilities to your users, we recommend upgrading to Standard access to get the full functionality that our API offers.
There are a few notable differences between Trial and Standard access which are detailed below.  
access tiers table  
| **Activity Type**  | **in Trial Access**  | **in Standard Access**  |  
| --- | --- | --- |  
| Pin Analytics  | Yes  | Yes  |  
| Reading ads  | Yes  | Yes  |  
| Reading audiences  | Yes  | Yes  |  
| Reading boards  | Yes  | Yes  |  
| Reading Pins  | Yes  | Yes  |  
| Reading catalogs  | Yes  | Yes  |  
| Creating ads  | Yes  | Yes  |  
| Creating audiences  | Yes  | Yes  |  
| Creating boards  | Yes (visible only to creator)  | Yes  |  
| Creating Pins  | Yes (visible only to creator)  | Yes  |  
| Creating catalogs  | Yes  | Yes  |  
| Rate limits  | Daily limits based on rate limit category. Please see the section on [Rate Limits](https://developers.pinterest.com/docs/key-concepts/access-tiers/#rate-limits).  | Increased rate limits based on activity. Please see the section on [Rate Limits](https://developers.pinterest.com/docs/key-concepts/access-tiers/#rate-limits).  |  
If you registered your app on or after **September 14, 2026** , you may receive HTTP 403 
`PINNER_DATA_ACCESS_DENIED`
error when you request a board or Pin without Pinterest's authorization for non-business users. Learn more about
[this error message.](https://developers.pinterest.com/docs/changelog/changelog/#pinner-data-access-denial-error)
If you registered your app on or after **September 14, 2026** , you may receive HTTP 403 
`PINNER_DATA_ACCESS_DENIED`
error when you request a board or Pin without Pinterest's authorization for non-business users. Learn more about
[this error message.](https://developers.pinterest.com/docs/changelog/changelog/#pinner-data-access-denial-error)
## Differences between Trial and Standard access
The most notable differences between Trial and Standard access are the overall available rate limits and behavior of Pins and Boards created.
### Rate limits
The rate limits applicable for your app depend on the scope the endpoints you use fall under. As a general rule, Standard access offers higher rate limits than Trial access. If you are wanting to use Pinterest features in your production environment, we recommend upgrading to Standard access.
  * Apps with Trial access are rate limited based on calls per day/per app.
  * Apps with Standard access are rate limited at a more granular level at calls per minute/per user/per app.


Read full details on [rate limits](https://developers.pinterest.com/docs/reference/rate-limits/) and [scopes](https://developers.pinterest.com/docs/getting-started/set-up-authentication-and-authorization/).
### Pins and Boards created with Trial access
We understand that testing our API shouldn't mean you have to impact your existing Pinterest profile. That's why all Pins and Boards created with Trial access are only visible to their creator as Sandbox entities.
Read more on our [API Sandbox](https://developers.pinterest.com/docs/developer-tools/sandbox/) and other supported capabilities.
## Upgrade your app to Standard access
If you've created an app with Trial access and are ready to build a product for more users, you should upgrade to Standard access. To ensure your app gets approved for Standard access make sure to prep the following:
  * Your app must already be approved for Trial access and comply with our [Developer Guidelines](https://policy.pinterest.com/developer-guidelines/).
  * Prepare a video recording of your app completing an action using the Pinterest API. We will review to verify that you are sending users through the [OAuth flow](https://developers.pinterest.com/docs/getting-started/set-up-authentication-and-authorization/) appropriately and not storing any sensitive information.


If you are the only intended user of the Pinterest API, we will still require a video recording of the OAuth flow. We accept screen recordings of calls on your terminal or through tools such as Postman.
If you are the only intended user of the Pinterest API, we will still require a video recording of the OAuth flow. We accept screen recordings of calls on your terminal or through tools such as Postman.
Once you've prepped your materials for Standard access, take the following steps to submit your request:
  1. Go to [My apps](https://developers.pinterest.com/apps/).
  2. Select **Upgrade** on the app card. This button will only be visible for apps eligible for upgrade.
  3. Verify the information you previously submitted about your app. This includes details on your use case and link to your privacy policy.
  4. Upload a video demo of your app.
  5. Submit your request.


Standard upgrade requests are reviewed regularly. You will receive an email notification once a decision has been made on your app.
## Why requests may get denied
All applications must comply with our [Developer Guidelines](https://policy.pinterest.com/developer-guidelines/) and [Developer and API Terms of Service](https://developers.pinterest.com/terms/). Here are some common issues that can make it difficult to verify your application's compliance, causing your request to be denied.
### Trial access denials
  * Privacy policy is inaccurate or not accessible.
    * Make sure the link provided for your privacy policy loads completely, is publicly accessible and is hosted on a domain that is clearly associated with your company or app.
  * App description is incomplete or unclear.
    * To help us understand your app's purpose, please provide as much detail as possible in the description. Access requests that don't have enough information about the app or are vague or incomplete may be denied.


### Standard access denials
  * Demo video does not show the authentication flow.
    * You must include the user authentication flow in your video demo in order to demonstrate that your application is requesting API access correctly.
  * Demo does not demonstrate an approved user authorization flow.
    * The compliant way for an app to authenticate a user is by obtaining an [OAuth access token](https://developers.pinterest.com/docs/getting-started/set-up-authentication-and-authorization/). If you use other methods, such as collecting user login credentials or Pinterest session cookies, your upgrade request may be denied.
  * Demo video does not show live Pinterest integration.
    * Your demo video must show how you integrate Pinterest within your app. Wireframes or general platform demos that don't show Pinterest integration may be denied.


## Getting support with your application status
If you want to appeal a denial, [submit a ticket](https://help.pinterest.com/contact/) in our Help Center. Please allow a few days for teams to review your access requests before following up on your app's overall status.
Was this page helpful?

