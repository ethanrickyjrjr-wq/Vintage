[WebKit](https://webkit.org/)
  * [Downloads](https://webkit.org/downloads/)
  * [Feature Status](https://webkit.org/blog/13878/web-push-for-web-apps-on-ios-and-ipados/#nav-sub-menu)
    * [CSS Features](https://webkit.org/css-status/)
    * [Standards Positions](https://webkit.org/standards-positions/)
  * [Documentation](https://webkit.org/blog/13878/web-push-for-web-apps-on-ios-and-ipados/#nav-sub-menu)
    * [Web Inspector](https://webkit.org/web-inspector)
    * [Tracking Prevention](https://webkit.org/tracking-prevention/)
  * [Policies](https://webkit.org/blog/13878/web-push-for-web-apps-on-ios-and-ipados/#nav-sub-menu)
    * [Project Goals](https://webkit.org/project/)
    * [Bug Prioritization](https://webkit.org/bug-prioritization/)
    * [Bug Report Guidelines](https://webkit.org/bug-report-guidelines/)
    * [Code Style Guidelines](https://webkit.org/code-style-guidelines/)
    * [Commit and Review Policy](https://webkit.org/commit-and-review-policy/)
    * [Feature Policy](https://webkit.org/feature-policy/)
    * [Security Policy](https://webkit.org/security-policy/)
    * [Tracking Prevention Policy](https://webkit.org/tracking-prevention-policy/)
  * [Contribute](https://webkit.org/blog/13878/web-push-for-web-apps-on-ios-and-ipados/#nav-sub-menu)
    * [Getting Started](https://webkit.org/getting-started/)
    * [Contributing Code](https://webkit.org/contributing-code/)
    * [Testing Contributions](https://webkit.org/testing-contributions/)
    * [How to Report Bugs](https://webkit.org/reporting-bugs/)
    * [GitHub Repository](https://github.com/WebKit/WebKit)
  * [Blog](https://webkit.org/blog/13878/web-push-for-web-apps-on-ios-and-ipados/#nav-sub-menu)
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

# [Web Push for Web Apps on iOS and iPadOS](https://webkit.org/blog/13878/web-push-for-web-apps-on-ios-and-ipados/ "Permanent Link: Web Push for Web Apps on iOS and iPadOS")
Feb 16, 2023
by Brady Eidson and Jen Simmons
Today marks the release of iOS and iPadOS 16.4 beta 1, and with it comes support for Web Push and other features for Home Screen web apps.
![iPhone Lock Screen showing a notification arriving](https://webkit.org/wp-content/uploads/Web_Push_on_iOS-1024x576.png)  

Today also brings the first beta of Safari 16.4. It’s a huge release, packed with over 135 features in WebKit — including RegExp lookbehind assertions, Import Maps, OffscreenCanvas, Media Queries Range Syntax, `@property`, `font-size-adjust`, Declarative Shadow DOM, and much more. We’ll [write all about these new WebKit features](https://webkit.org/blog/13966/webkit-features-in-safari-16-4/) when Safari 16.4 is released. Meanwhile, you can read a comprehensive list of new features and fixes in the [Safari 16.4 release notes](https://developer.apple.com/documentation/safari-release-notes/safari-16_4-release-notes).
But let’s set Safari aside and talk about Home Screen web apps on iOS and iPadOS.
Since the first iPhone, users could add any website to their Home Screen — whether it’s a brochure site, a blog, a newspaper, an online store, a social media platform, a streaming video site, productivity software, an application for creating artwork, or any other type of website. For the last ten years, users of Safari on iOS and iPadOS could do this by tapping the Share button to open the Share menu, and then tapping “Add to Home Screen”. The icon for that website then appears on their Home Screen, where a quick tap gets them back to the site.
Web developers have the option to create a [manifest file](https://developer.mozilla.org/en-US/docs/Web/Manifest) (with its [`display`](https://developer.mozilla.org/en-US/docs/Web/Manifest/display) member set to `standalone` or `fullscreen`) and serve it along with their website. If they do, that site becomes a Home Screen web app. Then, when you tap on its icon, the web app opens like any other app on iOS or iPadOS instead of opening in a browser. You can see its app preview in the [App Switcher](https://support.apple.com/en-us/HT202070), separate from Safari or any other browser.
## Web Push for Web Apps added to the Home Screen
Now with iOS and iPadOS 16.4, we are adding support for Web Push to Home Screen web apps. Web Push makes it possible for web developers to send push notifications to their users through the use of [Push API](https://developer.mozilla.org/en-US/docs/Web/API/Push_API), [Notifications API](https://developer.mozilla.org/en-US/docs/Web/API/Notifications_API), and [Service Workers](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API) all working together.
A web app that has been added to the Home Screen can request permission to receive push notifications as long as that request is in response to direct user interaction — such as tapping on a ‘subscribe’ button provided by the web app. iOS or iPadOS will then prompt the user to give the web app permission to send notifications. Once allowed, the user can [manage those permissions per web app](https://support.apple.com/en-us/HT201925) in Notifications Settings — just like any other app on iPhone and iPad.
The notifications from web apps work exactly like notifications from other apps. They show on the Lock Screen, in Notification Center, and on a paired Apple Watch.
This is the same W3C standards-based Web Push that was added in [Safari 16.1](https://webkit.org/blog/13399/webkit-features-in-safari-16-1/#web-push-for-macos-ventura) for macOS Ventura last fall. If you’ve implemented standards-based Web Push for your web app with industry best practices — such as using feature detection instead of browser detection — it will automatically work on iPhone and iPad.
Web Push on iOS and iPadOS uses the same Apple Push Notification service that powers native push on all Apple devices. You do not need to be a member of the Apple Developer Program to use it. Just be sure to allow URLs from `*.push.apple.com` if you are in control of your server push endpoints.
To learn more about how to setup Web Push, read the article [Meet Web Push](https://webkit.org/blog/12945/meet-web-push/) on webkit.org, or watch the WWDC22 session video [Meet Web Push](https://developer.apple.com/videos/play/wwdc2022/10098/).
## Focus support
Notifications are a powerful tool, but it’s easy for people to get into situations where they are overwhelmed by too many of them. Notifications for Home Screen web apps on iPhone and iPad integrate with [Focus](https://support.apple.com/en-us/HT212608), allowing users to precisely configure when or where to receive them. For users who add the same web app to their Home Screen on more than one iOS or iPadOS device, Focus modes automatically apply to all of them.
## Badging API
Home Screen web apps on iOS and iPadOS 16.4 now support the [Badging API](https://developer.mozilla.org/en-US/docs/Web/API/Badging_API). Just like any app on iOS and iPadOS, web apps are now able to set their badge count. Both `setAppBadge` and `clearAppBadge` change the count while the user has the web app open in the foreground or while the web app is handling push events in the background — even before permission to display the count has been granted.
Permission to display the badge on the app icon is granted in exactly the same way as other apps on iOS and iPadOS. Once a user gives permission to allow notifications, the icon on the Home Screen will immediately display the current badge count. Users can then configure permissions for Badging in Notifications Settings, just like any other app on iOS or iPadOS.
## Manifest ID
WebKit for iOS and iPadOS 16.4 adds support for the [`id` member](https://developer.mozilla.org/en-US/docs/Web/Manifest/id) from the Web Application Manifest standard. It’s a string (in the form of a URL) that acts as the unique identifier for the web application, intended to be used by an OS in whatever way desired. iOS and iPadOS use the Manifest ID for the purpose of syncing [Focus](https://support.apple.com/en-us/HT212608) settings across multiple devices.
iOS has supported multiple installs of the same web app since the very beginning. We believe the ability for people to install any web app more than once on their device can be useful — providing additional flexibility to support multiple accounts, separate work vs personal usage, and more.
When adding a web app to the Home Screen, users are given the opportunity to change the app’s name. iOS and iPadOS 16.4 combine this name with the Manifest ID to uniquely identify the web app. That way, a user can install multiple copies of the web app on one device and give them different identities. For example, notifications from “Shiny (personal)” can be silenced by Focus while notifications from “Shiny (work)” can be allowed. If the user gives their favorite website the same name on multiple devices, Focus settings on one device will sync and apply to the others as well.
## Third-party browser support for Add to Home Screen
In iOS and iPadOS 16.4, third-party browsers can now offer their users the ability to add websites and web apps to the Home Screen from the Share menu.
Applications on iOS and iPadOS present the Share menu by creating a `UIActivityViewController` with an array of `activityItems`. For “Add to Home Screen” to be included in the Share menu the following must be true:
  1. The application has the [com.apple.developer.web-browser](https://developer.apple.com/documentation/bundleresources/entitlements/com_apple_developer_web-browser) managed entitlement
  2. A WKWebView is included in the array of `activityItems`
  3. The WKWebView is displaying a document with an HTTP or HTTPS URL
  4. If the device is an iPad, it must not be configured as a [Shared iPad](https://support.apple.com/guide/deployment/shared-ipad-overview-dep9a34c2ba2/web)


As described above, after a user adds to Home Screen, any website with a Manifest file that sets the `display` member to `standalone` or `fullscreen` will open as a web app when a user taps its icon. This is true no matter which browser added the website to the Home Screen.
If there is no manifest file configured to request web app behavior (and no `meta` tag marking the site as web app capable), then that website will be saved as a Home Screen bookmark. Starting in iOS and iPadOS 16.4, Home Screen bookmarks will now open in the user’s current default browser.
## New Fallback Icon
Web developers usually provide icons to represent their website throughout the interface of a browser. If icons for the Home Screen are not provided, previously iOS and iPadOS would create an icon from a screenshot of the site. Now, iOS and iPadOS 16.4 will create and display a monogram icon using the first letter of the site’s name along with a color from the site instead.
To provide the icon to be used for your website or web app, list the [icons in the Manifest file](https://developer.mozilla.org/en-US/docs/Web/Manifest/icons) — a capability that’s been supported [since iOS and iPadOS 15.4](https://webkit.org/blog/12445/new-webkit-features-in-safari-15-4/#web-apps). Or you can use the long-supported technique of listing `apple-touch-icons` in the HTML document `head`. (If you do both, `apple-touch-icon` will take precedence over the Manifest-declared icons.)
## New Web API for Web Apps
Besides Web Push, Badging API, and Manifest ID, many of the other new features in Webkit for iOS and iPadOS 16.4 are of particular interest to web app developers focusing on Home Screen web apps. These include:
  * [Screen Wake Lock API](https://developer.mozilla.org/en-US/docs/Web/API/Screen_Wake_Lock_API)
  * [Screen Orientation API](https://developer.mozilla.org/en-US/docs/Web/API/Screen_Orientation_API)
  * [User Activation API](https://developer.mozilla.org/en-US/docs/Web/API/UserActivation)
  * [Web Codecs API](https://developer.mozilla.org/en-US/docs/Web/API/WebCodecs_API) video support


See the release notes for [Safari 16.4](https://developer.apple.com/documentation/safari-release-notes/safari-16_4-release-notes) for the full list of features.
## Feedback
Are you seeing a bug? That’s to be expected in a beta. Please help us such squash bugs before iOS and iPadOS 16.4 are released to the public by providing [feedback](https://feedbackassistant.apple.com/) from your iPhone or iPad. Feedback Assistant will collect all the information needed to help us understand what’s happening.
Also, we love hearing from you. You can find us on Mastodon at [@jensimmons@front-end.social](https://front-end.social/@jensimmons), [@bradeeoh@mastodon.social](https://mastodon.social/@bradeeoh) and [@jondavis@mastodon.social](https://mastodon.social/@jondavis). Or send a tweet to [@webkit](https://twitter.com/webkit) to share your thoughts on these new features.
[ NextRelease Notes for Safari Technology Preview 164Learn more ](https://webkit.org/blog/13902/release-notes-for-safari-technology-preview-164/)
[ PreviouslyThe User Activation APILearn more ](https://webkit.org/blog/13862/the-user-activation-api/)
  * [@webkit@front-end.social](https://front-end.social/@webkit)
  * [Site Map](https://webkit.org/sitemap/)
  * [Privacy Policy](http://www.apple.com/legal/privacy/)
  * [Licensing WebKit](https://webkit.org/licensing-webkit/)
  * [WebKit and the WebKit logo are trademarks of Apple Inc.](https://webkit.org/terms-of-use/)



