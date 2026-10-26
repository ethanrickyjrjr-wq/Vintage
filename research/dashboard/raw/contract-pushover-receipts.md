[ ![Pushover](https://pushover.net/assets/writing-header-c251fe65a610047a0209640b75d38e79f7b23b67d64135f629e6062f3e25c2f3.png) ](https://pushover.net/)
  * [Android](https://pushover.net/clients/android)
  * [iPhone & iPad](https://pushover.net/clients/ios)
  * [Desktop](https://pushover.net/clients/desktop)
  * [Integrations](https://pushover.net/apps)
  * [Pricing](https://pushover.net/pricing)
  * [Teams](https://pushover.net/teams)
  * [API](https://pushover.net/api)


  * [Blog](https://blog.pushover.net/)
  * [Help](https://support.pushover.net/)
  * [Login or Signup](https://pushover.net/login)


Latest Pushover News: [Deprecating GitHub Notification Endpoint, Migrating to Webhooks](https://blog.pushover.net/posts/2026/6/github)
    * [Message API](https://pushover.net/api)
    * [User/Group Validation API](https://pushover.net/api#validate)
    * [Receipt and Callback API](https://pushover.net/api/receipts)
    * [ Callback URLs](https://pushover.net/api/receipts#callback)
    * [ Canceling Retries](https://pushover.net/api/receipts#cancel)
    * [ Canceling By Tag](https://pushover.net/api/receipts#cancel_by_tag)
    * [Subscription API](https://pushover.net/api/subscriptions)
    * [Groups API](https://pushover.net/api/groups)
    * [Glances API](https://pushover.net/api/glances)
    * [Teams API](https://pushover.net/api/teams)
    * [Licensing API](https://pushover.net/api/licensing)
    * [Open Client API](https://pushover.net/api/client)


## Receipts and Callbacks API
Applications sending [emergency-priority](https://pushover.net/api#priority) notifications will receive a `receipt` parameter from our API when a notification has been queued. This parameter is a 30 character string containing the character set `[A-Za-z0-9]`. This receipt can be used to periodically poll our receipts API to get the status of your notification, up to 1 week after your notification has been received. 
Submit a GET request (no faster than once every 5 seconds) to: 
`https://api.pushover.net/1/receipts/_(your           receipt)_.json?token=_(your app token)_`
Include the receipt in the URL and your application's token as the `token` parameter. If the receipt is valid, our API will respond with some integer-valued parameters about your notification: 
`status` = `1` _(indicating your receipt request was successful)_
`acknowledged` = `1` _(1 or 0 whether the user has acknowledged the notification)_
`acknowledged_at` = `1360019238` _(a Unix timestamp of when the user acknowledged, or 0)_
`acknowledged_by` = `(user key)` _(the user key of the user that first acknowledged the notification)_
`acknowledged_by_device` = `(device name)` _(the device name of the user that first acknowledged the notification)_
`last_delivered_at` = `1360001238` _(a Unix timestamp of when the notification was last retried, or 0)_
`expired` = `1` _(1 or 0 whether the expiration date has passed)_
`expires_at` = `1360019290` _(a Unix timestamp of when the notification will stop being retried)_
`called_back` = `1` _(1 or 0 whether our server has called back to your callback URL if any)_
`called_back_at` = `1360019239` _(a Unix timestamp of when our server called back, or 0)_
### Callback URLs
Rather than periodically polling our receipts API, you may also include a `callback` parameter when submitting your emergency notification. This must be a URL (HTTP or HTTPS) that is reachable from the Internet that our servers will call out to as soon as the notification has been acknowledged. If a callback URL exists, we will submit a POST request to the URL with the following parameters: 
`receipt` = `(your receipt ID)`
`acknowledged` = `1`
`acknowledged_at` = `1360019238` _(a Unix timestamp of when the notification was acknowledged)_
`acknowledged_by` = `(user key)` _(the user key of the user that first acknowledged the notification)_
`acknowledged_by_device` = `(device name)` _(the device name of the user that first acknowledged the notification)_
If our API servers do not receive a successful (2xx) HTTP response from your callback URL, we will retry again in one minute. 
### Canceling Emergency-Priority Retries
An [emergency-priority](https://pushover.net/api#priority2) notification will continue to be sent to devices until it reaches its original `expire` value. To cancel an emergency-priority notification early, you can send a POST request to our API: 
`https://api.pushover.net/1/receipts/_(your           receipt)_/cancel.json`
  

Along with your POST request, include your application's API token as the `token` parameter. 
### Canceling Emergency-Priority Retries By Tag
[Canceling](https://pushover.net/api/receipts#cancel) retries normally requires a receipt ID which is returned by our API when the message is [created](https://pushover.net/api) and must be stored by your application. If your application is not capable of storing receipt IDs or you want to cancel a handful of similar messages (possibly sent to different recipients) all at once, you can use tags. 
When [creating](https://pushover.net/api#priority2) an emergency-priority message, a `tags` parameter may be supplied which stores a comma-separated list of arbitrary tags with the message. Any of these tags may be used to cancel all emergency-priority messages with that tag that were sent by your application. 
For example, a network monitor application sending a "down" event might include tags of the affected server, rack, and location. 
`message` = `Server mail01 failed to respond to 3         pings`
`tags` = `s=mail01,r=23,l=chicago`
If many messages for down servers were sent but later correlated to a single datacenter outage, the network monitor may generate an "up" event that cancels all retries for messages with the `l=chicago` tag. 
To cancel retries for all messages with a given tag, submit a POST request to: 
`https://api.pushover.net/1/receipts/cancel_by_tag/_(your         tag)_.json`
  

Along with your POST request, include your application's API token as the `token` parameter. All active emergency-priority messages with the given tag will be canceled. 
[ Pushover on Bluesky](https://bsky.app/profile/pushover.net)   
[Privacy](https://pushover.net/privacy) | [Terms of Service](https://pushover.net/terms) | [API Status](https://status.pushover.net/)
Pushover® is a registered trademark of Pushover, LLC.  
Copyright © 2012-2026 Pushover, LLC. All rights reserved. 

