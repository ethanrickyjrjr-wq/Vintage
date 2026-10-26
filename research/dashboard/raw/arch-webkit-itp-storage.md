[WebKit](https://webkit.org/)
  * [Downloads](https://webkit.org/downloads/)
  * [Feature Status](https://webkit.org/blog/10218/full-third-party-cookie-blocking-and-more/#nav-sub-menu)
    * [CSS Features](https://webkit.org/css-status/)
    * [Standards Positions](https://webkit.org/standards-positions/)
  * [Documentation](https://webkit.org/blog/10218/full-third-party-cookie-blocking-and-more/#nav-sub-menu)
    * [Web Inspector](https://webkit.org/web-inspector)
    * [Tracking Prevention](https://webkit.org/tracking-prevention/)
  * [Policies](https://webkit.org/blog/10218/full-third-party-cookie-blocking-and-more/#nav-sub-menu)
    * [Project Goals](https://webkit.org/project/)
    * [Bug Prioritization](https://webkit.org/bug-prioritization/)
    * [Bug Report Guidelines](https://webkit.org/bug-report-guidelines/)
    * [Code Style Guidelines](https://webkit.org/code-style-guidelines/)
    * [Commit and Review Policy](https://webkit.org/commit-and-review-policy/)
    * [Feature Policy](https://webkit.org/feature-policy/)
    * [Security Policy](https://webkit.org/security-policy/)
    * [Tracking Prevention Policy](https://webkit.org/tracking-prevention-policy/)
  * [Contribute](https://webkit.org/blog/10218/full-third-party-cookie-blocking-and-more/#nav-sub-menu)
    * [Getting Started](https://webkit.org/getting-started/)
    * [Contributing Code](https://webkit.org/contributing-code/)
    * [Testing Contributions](https://webkit.org/testing-contributions/)
    * [How to Report Bugs](https://webkit.org/reporting-bugs/)
    * [GitHub Repository](https://github.com/WebKit/WebKit)
  * [Blog](https://webkit.org/blog/10218/full-third-party-cookie-blocking-and-more/#nav-sub-menu)
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

# [Full Third-Party Cookie Blocking and More](https://webkit.org/blog/10218/full-third-party-cookie-blocking-and-more/ "Permanent Link: Full Third-Party Cookie Blocking and More")
Mar 24, 2020
by John Wilander
This blog post covers several enhancements to Intelligent Tracking Prevention (ITP) in iOS and iPadOS 13.4 and Safari 13.1 on macOS to address our latest discoveries in the industry around tracking.
## Full Third-Party Cookie Blocking
Cookies for cross-site resources are now blocked by default across the board. This is a significant improvement for privacy since it removes any sense of exceptions or “a little bit of cross-site tracking is allowed.”
It might seem like a bigger change than it is. But we’ve added so many restrictions to ITP since its initial release in 2017 that we are now at a place where most third-party cookies are already blocked in Safari. To keep supporting cross-site integration, we shipped the [Storage Access API](https://webkit.org/blog/8124/introducing-storage-access-api/) two years ago to provide the means for authenticated embeds to get cookie access _with mandatory user control_. It is going through the standards process [in the W3C Privacy Community Group](https://github.com/privacycg/storage-access) right now.
Regardless of the size of this change, there are further benefits, as explored below.
### Paves the Way For Other Browsers
Safari continues to pave the way for privacy on the web, this time as the first mainstream browser to fully block third-party cookies by default. As far as we know, only the [Tor Browser](https://2019.www.torproject.org/projects/torbrowser/design/#identifier-linkability) has featured full third-party cookie blocking by default before Safari, but [Brave just has a few exceptions](https://brave.com/ok-google/) left in its blocking so in practice they are in the same good place. We know Chrome wants this behavior too and they announced that they’ll be [shipping it by 2022](https://blog.chromium.org/2020/01/building-more-private-web-path-towards.html).
We will report on our experiences of full third-party cookie blocking to the privacy groups in W3C to help other browsers take the leap.
### Removes Statefulness From Cookie Blocking
Full third-party cookie blocking removes statefulness in cookie blocking. As discussed in our [December 2019 blog post](https://webkit.org/blog/9661/preventing-tracking-prevention-tracking/), the internal state of tracking prevention could be turned into a tracking vector. Full third-party cookie blocking makes sure there’s no ITP state that can be detected through cookie blocking behavior. We’d like to **again thank Google** for initiating this analysis through their report.
### Disables Login Fingerprinting
As discussed by Jeremiah Grossman [back in 2008](https://blog.jeremiahgrossman.com/2008/03/login-detection-whose-problem-is-it.html) and Tom Anthony [in 2012](https://www.tomanthony.co.uk/blog/detect-visitor-social-networks/), and set up by Robin Linus in 2016 as a [live demo with which you can test your browser](https://robinlinus.github.io/socialmedia-leak/), this technique allows a website to invisibly detect where you are logged in and is viable in any browser without full third-party cookie blocking.
Since “global browser state” has been top of mind in the web privacy community as of late, we’d like to point out that cookies themselves are global state and unless the browser blocks or partitions them in third-party contexts, they allow for cross-site leakage of user information such as login fingerprinting.
### Additional Benefits
In addition, there are further benefits to full third-party cookie blocking:
  * Disables [cross-site request forgery](https://en.wikipedia.org/wiki/Cross-site_request_forgery) attacks against websites through third-party requests. Note that you still need to protect against forged requests that come in through top frame navigations (see [SameSite cookies](https://tools.ietf.org/html/draft-ietf-httpbis-rfc6265bis-05#section-8.8.2) for guidance).
  * Removes the ability to use an auxiliary third-party domain to identify users. Such a setup could otherwise persist IDs even when users delete website data for the first party.
  * Simplifies things for developers. Now it’s as easy as possible: If you need cookie access as third-party, use the Storage Access API.


### What About the Classifier?
ITP’s classifier keeps working to detect bounce trackers, tracker collusion, and link decoration tracking.
### Developer Guidance
If yours is among the few websites that still relies on third-party cookies in Safari and has not been affected by ITP in its previous iterations, here’s how you can make things work for your users:
**Option 1** : [OAuth 2.0 Authorization](https://tools.ietf.org/html/rfc6749) with which the authenticating domain (in your case, the third-party that expects cookies) forwards an authorization token to your website which you consume and use to establish a first-party login session with a server-set [Secure and HttpOnly cookie](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies#Secure_and_HttpOnly_cookies).
**Option 2** : [The Storage Access API](https://webkit.org/blog/8124/introducing-storage-access-api/) with which the third-party can request permission to get access to its first-party cookies.
**Option 3** : The temporary compatibility fix for popups, see section “Temporary Compatibility Fix: Automatic Storage Access for Popups” in our [ITP 2.0 blog post](https://webkit.org/blog/8311/intelligent-tracking-prevention-2-0/). This compatibility fix allows the third-party to open a popup from your website and upon a tap or click in that popup gain temporary cookie access under the opener page on your website. Note that this compatibility fix will go away in a future version of Safari so only go this route if it saves you time and allows for a graceful transition period.
## Cookie Blocking Latch Mode
The original release of ITP featured what we call “cookie blocking latch mode.” It means once a request is blocked from using cookies, all redirects of that request are also blocked from using cookies. Back in 2017 we got a request to allow cookie blocking to open and close on redirects and implemented that behavior. But with full third-party cookie blocking in place, latch mode is back.
## 7-Day Cap on All Script-Writeable Storage
[Back in February 2019](https://webkit.org/blog/8613/intelligent-tracking-prevention-2-1/), we announced that ITP would cap the expiry of client-side cookies to seven days. That change curbed third-party scripts’ use of first-party cookies for the purposes of cross-site tracking.
However, as many anticipated, third-party scripts moved to other means of first-party storage such as LocalStorage. If you have a look at what’s stored in the first-party space on many websites today, it’s littered with data keyed as various forms of “tracker brand user ID.” To make matters worse, APIs like LocalStorage have no expiry function at all, i.e. websites cannot even ask browsers to put a limit on how long such storage should stay around.
Now ITP has aligned the remaining script-writable storage forms with the existing client-side cookie restriction, deleting all of a website’s script-writable storage after seven days of Safari use without user interaction on the site. These are the script-writable storage forms affected (excluding some legacy website data types):
  * Indexed DB
  * LocalStorage
  * Media keys
  * SessionStorage
  * Service Worker registrations and cache


### A Note On Web Applications Added to the Home Screen
As mentioned, the seven-day cap on script-writable storage is gated on “after seven days of Safari use without user interaction on the site.” That is the case in Safari. Web applications added to the home screen are not part of Safari and thus have their own counter of days of use. Their days of use will match actual use of the web application which resets the timer. We do not expect the first-party in such a web application to have its website data deleted.
If your web application does experience website data deletion, please let us know since we would consider it a serious bug. It is not the intention of Intelligent Tracking Prevention to delete website data for first parties in web applications.
## Cross-Site document.referrer Downgraded to Origin
All cross-site `document.referrer`s are downgraded to their origin. This matches the already [downgraded cross-site referrer request headers](https://webkit.org/blog/9661/preventing-tracking-prevention-tracking/).
## Detection of Delayed Bounce Tracking
Some trackers have started to delay their navigational redirects, probably to evade ITP’s bounce tracking detection. This manifests as the webpage disappearing and reloading shortly after you land on it. We’ve added logic to cover such delayed bounce tracking and detect them just like instant bounces.
## Testing Your Website
We encourage all developers to regularly test their websites with Safari Technology Preview (STP) and our betas of iOS, iPadOS, and macOS. Major changes to ITP and WebKit in general are included in the betas and STP, typically months before shipping. An easy way to stay ahead of the changes is to use STP as a daily development browser. This gives you access to the latest developer tools and helps you discover unexpected behavior in your websites with each release. If you come across bugs or breakage, please [file an open source bug report](https://bugs.webkit.org/).
[ NextRelease Notes for Safari Technology Preview 103Learn more ](https://webkit.org/blog/10243/release-notes-for-safari-technology-preview-103/)
[ PreviouslyRelease Notes for Safari Technology Preview 102Learn more ](https://webkit.org/blog/10067/release-notes-for-safari-technology-preview-102/)
  * [@webkit@front-end.social](https://front-end.social/@webkit)
  * [Site Map](https://webkit.org/sitemap/)
  * [Privacy Policy](http://www.apple.com/legal/privacy/)
  * [Licensing WebKit](https://webkit.org/licensing-webkit/)
  * [WebKit and the WebKit logo are trademarks of Apple Inc.](https://webkit.org/terms-of-use/)



