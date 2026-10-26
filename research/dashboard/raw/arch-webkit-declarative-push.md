[WebKit](https://webkit.org/)
  * [Downloads](https://webkit.org/downloads/)
  * [Feature Status](https://webkit.org/blog/16535/meet-declarative-web-push/#nav-sub-menu)
    * [CSS Features](https://webkit.org/css-status/)
    * [Standards Positions](https://webkit.org/standards-positions/)
  * [Documentation](https://webkit.org/blog/16535/meet-declarative-web-push/#nav-sub-menu)
    * [Web Inspector](https://webkit.org/web-inspector)
    * [Tracking Prevention](https://webkit.org/tracking-prevention/)
  * [Policies](https://webkit.org/blog/16535/meet-declarative-web-push/#nav-sub-menu)
    * [Project Goals](https://webkit.org/project/)
    * [Bug Prioritization](https://webkit.org/bug-prioritization/)
    * [Bug Report Guidelines](https://webkit.org/bug-report-guidelines/)
    * [Code Style Guidelines](https://webkit.org/code-style-guidelines/)
    * [Commit and Review Policy](https://webkit.org/commit-and-review-policy/)
    * [Feature Policy](https://webkit.org/feature-policy/)
    * [Security Policy](https://webkit.org/security-policy/)
    * [Tracking Prevention Policy](https://webkit.org/tracking-prevention-policy/)
  * [Contribute](https://webkit.org/blog/16535/meet-declarative-web-push/#nav-sub-menu)
    * [Getting Started](https://webkit.org/getting-started/)
    * [Contributing Code](https://webkit.org/contributing-code/)
    * [Testing Contributions](https://webkit.org/testing-contributions/)
    * [How to Report Bugs](https://webkit.org/reporting-bugs/)
    * [GitHub Repository](https://github.com/WebKit/WebKit)
  * [Blog](https://webkit.org/blog/16535/meet-declarative-web-push/#nav-sub-menu)
    * [News Posts](https://webkit.org/blog/category/news/)
    * [CSS Posts](https://webkit.org/blog/category/css/)
    * [Contributing Posts](https://webkit.org/blog/category/contributing/)
    * [Privacy Posts](https://webkit.org/blog/category/privacy/)
    * [Performance Posts](https://webkit.org/blog/category/performance/)
    * [JavaScript Posts](https://webkit.org/blog/category/javascript/)
    * [Standards Posts](https://webkit.org/blog/category/standards/)
    * [Web Inspector Posts](https://webkit.org/blog/category/web-inspector/)
    * [Safari Technology Preview Posts](https://webkit.org/blog/category/safari-technology-preview/)
  * 

# [Meet Declarative Web Push](https://webkit.org/blog/16535/meet-declarative-web-push/ "Permanent Link: Meet Declarative Web Push")
Mar 27, 2025
by Brady Eidson
###### Contents
  * [The status quo](https://webkit.org/blog/16535/meet-declarative-web-push/#the-status-quo)
  * [How to use Declarative Web Push](https://webkit.org/blog/16535/meet-declarative-web-push/#how-to-use-declarative-web-push)
  * [A note on backwards compatibility](https://webkit.org/blog/16535/meet-declarative-web-push/#a-note-on-backwards-compatibility)
  * [What if I can’t send the notification description through the internet?](https://webkit.org/blog/16535/meet-declarative-web-push/#what-if-i-can%e2%80%99t-send-the-notification-description-through-the-internet)
  * [Standards work](https://webkit.org/blog/16535/meet-declarative-web-push/#standards-work)


Web Push notifications are a powerful and important part of the web platform.
As someone’s very famous uncle once said, [with great power comes great responsibility](https://en.wikipedia.org/wiki/With_great_power_comes_great_responsibility#Use_in_Spider-Man_media). When we added Web Push to WebKit we knew it was imperative to maintain people’s expectations of power efficiency and privacy.
We took a deliberate approach to maintain those expectations when implementing [Web Push for Safari](https://webkit.org/blog/12945/meet-web-push/) on macOS, for [web apps saved to the Home Screen](https://webkit.org/blog/13878/web-push-for-web-apps-on-ios-and-ipados/) on iOS and iPadOS, and [web apps on Mac](https://webkit.org/blog/14205/news-from-wwdc23-webkit-features-in-safari-17-beta/#web-apps). We knew running extra code to display notifications could impact battery life. We knew that Web Push’s reliance on service worker JavaScript was at odds with our broad approach to user privacy on the web. We learned that the protections we felt necessary for user privacy challenged assumptions web developers had about Web Push in other browsers. So we challenged ourselves to [propose something better](https://github.com/WebKit/explainers/blob/main/DeclarativeWebPush/README.md) for end users, web developers, and browsers.
Declarative Web Push allows web developers to request a Web Push subscription and display user visible notifications without requiring an installed [service worker](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API/Using_Service_Workers). Service worker JavaScript can _optionally_ change the contents of an incoming notification. Unlike with original Web Push, there is no penalty for service workers failing to display a notification; the declarative push message itself is used as a fallback in case the optional JavaScript processing step fails.
Declarative Web Push is more energy efficient and more private by design. It is easier for you, the web developer to use. And it’s backwards compatible with existing Web Push notifications.
Keep reading for our thinking on the challenges that result from how Web Push works today. Or jump straight to [how to use Declarative Web Push](https://www.webkit.org/blog/16535/meet-declarative-web-push/#how-to-use-declarative-web-push). You can test it out on iOS 18.4, iPadOS 18.4, and on the macOS 15.5 beta.
##  The status quo
Existing Web Push notifications were designed with a JavaScript-first mindset. Instead of a remote push directly describing a user visible notification, the more abstract concept of a “push message” is handled by the website’s service worker JavaScript.
The website first needs to have a service worker registered. It can then use that `ServiceWorkerRegistration` to create a `PushSubscription`, which gives the website the information it needs to remotely send a push message to the browser.
To give users direct control, WebKit requires you as the developer to always show a notification; no silent push messages are allowed. Therefore we require push subscriptions to set the `userVisibleOnly` flag to `true`. While this can be frustrating, the original Web Push design made this necessary to protect user privacy and battery life.
Once a push message is received on the device, the browser makes sure there is an instance of the service worker JavaScript and then dispatches a `PushEvent` to it. The code handling that event inspects the data in the push message, using it to make a call to `ServiceWorkerRegistration.showNotification(...)` to display the user visible notification.
While some popular JavaScript libraries abstract away some of these complexities, there’s a lot of code involved, and a lot can subtly go wrong.
###  Challenge 1 — Silent push protection
Recall that WebKit requires the `userVisibleOnly` flag be set to true when registering for a push subscription. The JavaScript in a ServiceWorker’s `PushEvent` handler has the responsibility of showing that user visible notification. Allowing websites to remotely wake up a device for silent background work is a privacy violation and expends energy. So if an event handler doesn’t show the user visible notification for any reason we [revoke its push subscription](https://webkit.org/blog/12945/meet-web-push/#:~:text=Violations%20of%20the%20userVisibleOnly%20promise%20will%20result%20in%20a%20push%20subscription%20being%20revoked.)
Unfortunately bugs in a service worker script, networking conditions, or local device conditions all might prevent a timely call to `showNotification`. These scenarios might not always be the fault of the script author and can be difficult to debug. It would be better if there were technical enforcement of the `userVisibleOnly` promise and therefore the silent push penalty box could be ignored.
###  Challenge 2 — Tracking data
We’ve [blogged about it before](https://webkit.org/blog/category/privacy/) and we’ll blog about it again; Privacy is a fundamental human right.
Since the first version of Safari we’ve focused on privacy. WebKit goes above and beyond the privacy protections required by web standards. As the web platform evolved, so did our strategies to protect user privacy. This now includes active blocking and removal of website data, like with [Intelligent Tracking Prevention](https://webkit.org/blog/7675/intelligent-tracking-prevention/) (shortened as ITP).
ITP deletes all website data for websites you haven’t visited in a while. This includes service worker registrations. While this can be frustrating to web developers, it’s key to protecting user privacy. It’s a hard tradeoff we make intentionally given how committed we are to protecting users.
When we implemented Web Push that created a dilemma. Since creating and using a push subscription is inherently tied to having a service worker, ITP removing a service worker registration would render the push subscription useless. Since having strong anti-tracking prevention features seems to be fundamentally at odds with the JavaScript-driven nature of existing Web Push, wouldn’t it be better if Web Push notifications could be delivered without any JavaScript?
So what does Declarative Web Push look like in practice?
##  How to use Declarative Web Push
To use any flavor of Web Push you first use a `PushManager` to acquire a push subscription. Web Push on Apple’s platforms uses the same Apple Push Notification service that powers native push on all Apple devices. You do not need to be a member of the Apple Developer Program to use it.
The only `PushManager` available with original Web Push is `ServiceWorkerRegistration.pushManager`.  
Declarative Web Push also exposes `window.pushManager` to support subscription management without requiring a service worker.

```
const subscription = await window.pushManager.subscribe({
    userVisibleOnly: true,
    applicationServerKey: arrayForPublicKey
});

```

If you do also have a registered service worker scoped to the root level of your website domain, it shares the same push subscription as the window object. But the removal of that service worker registration will not affect the associated push subscription.
Sending a push message to that push subscription works exactly as before. For a notification to be handled declaratively the _contents_ of the push message must match the [declarative standard JSON format.](https://pr-preview.s3.amazonaws.com/w3c/push-api/pull/385.html#declarative-push-message) This standardized format guarantees that the browser has enough information to display a user-visible notification without any JavaScript.

```
{
    "web_push": 8030,
    "notification": {
        "title": "Webkit.org — Meet Declarative Web Push",
        "lang": "en-US",
        "dir": "ltr",
        "body": "Send push notifications without JavaScript or service worker!",
        "navigate": "https://webkit.org/blog/16535/meet-declarative-web-push/",
        "silent": false,
        "app_badge": "1"
    }
}

```

The top level `"web_push"` value is an homage to [RFC 8030](https://datatracker.ietf.org/doc/html/rfc8030) – Generic Event Delivery Using HTTP Push. This is the magic value that opts the rest of your push message into declarative parsing.
The `"notification"` value is a dictionary that describes the user visible notification to the browser. Like when you create a notification programmatically in JavaScript, a non-empty `"title"` value is required. Most of the optional members of the [NotificationOptions dictionary](https://notifications.spec.whatwg.org/#dictdef-notificationoptions) can also be specified.
So far we’ve mostly discussed the automatic display of a notification without JavaScript. Something useful needs to happen without JavaScript when a user activates a declarative notification. That’s where the required `"navigate"` value comes in. It describes a URL that will be navigated to by the browser upon activation.
Finally, if the web app supports running in an app-like mode that supports the [Badging API](https://www.w3.org/TR/badging/), such as [Home Screen web apps on iOS](https://webkit.org/blog/14112/badging-for-home-screen-web-apps/), the declarative message can include an updated application badge.
##  A note on backwards compatibility
In practice, a vast majority of Web Push messages are already JSON. They describe a user visible notification to be displayed. The service worker JavaScript handling those push messages simply parses the JSON to display the notification programatically. But the format of those JSON messages varies on a per-website basis.
Most applications will find it straightforward to send the declarative standard JSON in their push messages and rewrite their service worker’s `PushEvent` handler to display it. Once those two steps are taken, those Web Push messages become backwards compatible with browsers that do not yet support Declarative Web Push.
If your push message arrives to a newer browser, it’s handled declaratively by the browser. If it arrives to an older browser, it’s handled imperatively by JavaScript as it always had been.
Always standardizing on the declarative standard JSON has the nice side effect of introducing consistency across all projects, further reducing maintenance burden for prolific web developers.
##  What if I can’t send the notification description through the internet?
All apps — no matter their platform — might not be able to send the visible content of a notification through push services. How a notification should display often relies on application state local to the user’s device. Maybe the user has used the app in ways the server is not aware of yet, requiring an update to the notification. Or maybe the app is for secure communication and decryption keys for the notification payload only exist within the app on the device.
In these cases, code is needed to process the incoming push message to display something meaningful.
![](https://webkit.org/wp-content/uploads/declarative-web-push-notification.png)
Native iOS apps that run into these edge cases have a tool call [`UNNotificationServiceExtension`](https://developer.apple.com/documentation/usernotifications/unnotificationserviceextension) which allows a small snippet of application code to run in response to an incoming push notification. The incoming notification _always_ has enough content to display a user visible “fallback notification”, but the app’s notification service extension is given a short amount of time to consult the app’s local data storage and propose a new, more meaningful notification.
If there’s a bug in the notification extension, or the required data is not available, or some other unforeseen scenario causes it to fail to show a different notification in time, the original “fallback content” is displayed instead.
![](https://webkit.org/wp-content/uploads/declarative-web-push-secure.png)
For web apps with Declarative Web Push, service worker JavaScript fills the same role. When a Declarative Web Push message arrives and a service worker is installed, a push event is dispatched to it like before.
`PushEvent` now has the context of the “proposed notification” from the Declarative Web Push message. If the event handler displays a replacement notification properly, the proposed notification is ignored. If the event handler fails to display a replacement notification in time, the fallback is used.
Because there is always a user visible notification — therefore a privacy breaking silent push remains impossible — browsers don’t have to apply their “silent push penalties” to Declarative Web Push messages.
iOS also supports [offloading unused native apps](https://support.apple.com/en-al/guide/iphone/iph47c931112/ios#:~:text=Remove%20apps%20and%20data,Drive%20in%20the%20Files%20app.) which frees up the storage used by the application code while leaving minimal application functionality in place. In this scenario, the `UNNotificationServiceExtension` code is gone but unmodified notifications can still be displayed for the application.
This is quite similar to how Declarative Web Push notifications work on iOS after the website’s service worker JavaScript has been removed either by the user or by ITP. The modification of an incoming push message is no longer possible but the unmodified notification can still be displayed.
##  Standards work
We’re excited about Declarative Web Push and want it supported everywhere.
Around the time we published our [WebKit Declarative Web Push explainer](https://github.com/WebKit/explainers/blob/main/DeclarativeWebPush/README.md), we also approached the other browser vendors and interested parties about it at [TPAC 2023](https://www.w3.org/2023/09/TPAC/) and raised [an issue against the Push API](https://github.com/w3c/push-api/issues/360) to discuss it. While standards bodies will always nit pick on the details, the overall goal of the proposal was well met.
In 2024, we actively made proposals to the various specs involved, making changes to our implementation as well reasoned feedback came in:
  * [Allow notifications and actions to specify a navigable URL](https://github.com/whatwg/notifications/pull/213) against the Notifications API enables notifications to navigate without involving JavaScript after an end user clicks them. (We also made various editorial changes to the Notifications API as part of standardizing Declarative Web Push.)
  * [Add Declarative Web Push](https://github.com/w3c/push-api/pull/385) against the Push API specification defines the new declarative format.
  * [Expose pushManager on Window](https://github.com/w3c/push-api/pull/393) against the Push API specification enables the Push API API to be used without the need for a service worker.


We feel the feature has a good enough foundation for us to ship it and for web developers to start experimenting with it. We foresee future enhancements enabled by this solid foundation. And we hope it ends up widely available soon.
We encourage you to reach out to us on [WebKit’s Slack](https://webkit.slack.com/) or our [issue tracker](https://bugs.webkit.org/) to share your experiences working with this great new feature.
[ NextItem Flow, Part 1:   
A new unified concept for layoutLearn more ](https://webkit.org/blog/16587/item-flow-part-1-a-new-unified-concept-for-layout/)
[ PreviouslyRelease Notes for Safari Technology Preview 215Learn more ](https://webkit.org/blog/16523/release-notes-for-safari-technology-preview-215/)
  * [@webkit@front-end.social](https://front-end.social/@webkit)
  * [Site Map](https://webkit.org/sitemap/)
  * [Privacy Policy](http://www.apple.com/legal/privacy/)
  * [Licensing WebKit](https://webkit.org/licensing-webkit/)
  * [WebKit and the WebKit logo are trademarks of Apple Inc.](https://webkit.org/terms-of-use/)



