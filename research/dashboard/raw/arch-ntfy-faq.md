[ Skip to content ](https://docs.ntfy.sh/faq/#frequently-asked-questions-faq)
If you like ntfy, please consider sponsoring me via [**GitHub Sponsors**](https://github.com/sponsors/binwiederhier) or [**Liberapay**](https://en.liberapay.com/ntfy/) , or subscribing to [**ntfy Pro**](https://ntfy.sh/app). 
[ ![logo](https://docs.ntfy.sh/static/img/ntfy.png) ](https://docs.ntfy.sh/ "ntfy")
ntfy 
FAQs 
[ ](https://docs.ntfy.sh/faq/?q= "Share")
Initializing search 
[ binwiederhier/ntfy 
  * v2.34.0
  * 35.1k
  * 1.7k

](https://github.com/binwiederhier/ntfy "Go to repository")
[ ![logo](https://docs.ntfy.sh/static/img/ntfy.png) ](https://docs.ntfy.sh/ "ntfy") ntfy 
[ binwiederhier/ntfy 
  * v2.34.0
  * 35.1k
  * 1.7k

](https://github.com/binwiederhier/ntfy "Go to repository")
  * [ Getting started  ](https://docs.ntfy.sh/)
  * Publishing  Publishing 
    * [ Sending messages  ](https://docs.ntfy.sh/publish/)
  * Subscribing  Subscribing 
    * [ From your phone  ](https://docs.ntfy.sh/subscribe/phone/)
    * [ From the Web app  ](https://docs.ntfy.sh/subscribe/web/)
    * [ From the Desktop  ](https://docs.ntfy.sh/subscribe/pwa/)
    * [ From the CLI  ](https://docs.ntfy.sh/subscribe/cli/)
    * [ Using the API  ](https://docs.ntfy.sh/subscribe/api/)
  * Self-hosting  Self-hosting 
    * [ Installation  ](https://docs.ntfy.sh/install/)
    * [ Configuration  ](https://docs.ntfy.sh/config/)
  * Other things  Other things 
    * FAQs  [ FAQs  ](https://docs.ntfy.sh/faq/) Table of contents 
      * [ Isn't this like ...?  ](https://docs.ntfy.sh/faq/#isnt-this-like)
      * [ Can I use this in my app? Will it stay free?  ](https://docs.ntfy.sh/faq/#can-i-use-this-in-my-app-will-it-stay-free)
      * [ What are the uptime guarantees?  ](https://docs.ntfy.sh/faq/#what-are-the-uptime-guarantees)
      * [ What happens if there are multiple subscribers to the same topic?  ](https://docs.ntfy.sh/faq/#what-happens-if-there-are-multiple-subscribers-to-the-same-topic)
      * [ Will you know what topics exist, can you spy on me?  ](https://docs.ntfy.sh/faq/#will-you-know-what-topics-exist-can-you-spy-on-me)
      * [ Can I self-host it?  ](https://docs.ntfy.sh/faq/#can-i-self-host-it)
      * [ Is Firebase used?  ](https://docs.ntfy.sh/faq/#is-firebase-used)
      * [ How much battery does the Android app use?  ](https://docs.ntfy.sh/faq/#how-much-battery-does-the-android-app-use)
      * [ Paid plans? I thought it was open source?  ](https://docs.ntfy.sh/faq/#paid-plans-i-thought-it-was-open-source)
      * [ What is instant delivery?  ](https://docs.ntfy.sh/faq/#what-is-instant-delivery)
      * [ Can you implement feature X?  ](https://docs.ntfy.sh/faq/#can-you-implement-feature-x)
      * [ I'm having issues with iOS, can you help? The iOS app is behind compared to the Android app, can you fix that?  ](https://docs.ntfy.sh/faq/#im-having-issues-with-ios-can-you-help-the-ios-app-is-behind-compared-to-the-android-app-can-you-fix-that)
      * [ Can I disable the web app? Can I protect it with a login screen?  ](https://docs.ntfy.sh/faq/#can-i-disable-the-web-app-can-i-protect-it-with-a-login-screen)
      * [ If topic names are public, could I not just brute force them?  ](https://docs.ntfy.sh/faq/#if-topic-names-are-public-could-i-not-just-brute-force-them)
      * [ Where can I donate?  ](https://docs.ntfy.sh/faq/#where-can-i-donate)
      * [ Can I email you? Can I DM you on Discord/Matrix?  ](https://docs.ntfy.sh/faq/#can-i-email-you-can-i-dm-you-on-discordmatrix)
    * [ Examples  ](https://docs.ntfy.sh/examples/)
    * [ Integrations + projects  ](https://docs.ntfy.sh/integrations/)
    * [ Release notes  ](https://docs.ntfy.sh/releases/)
    * [ Emojis 🥳 🎉  ](https://docs.ntfy.sh/emojis/)
    * [ Template functions  ](https://docs.ntfy.sh/publish/template-functions/)
    * [ Troubleshooting  ](https://docs.ntfy.sh/troubleshooting/)
    * [ Known issues  ](https://docs.ntfy.sh/known-issues/)
    * [ Deprecation notices  ](https://docs.ntfy.sh/deprecations/)
    * [ Development  ](https://docs.ntfy.sh/develop/)
    * [ Contributing  ](https://docs.ntfy.sh/contributing/)
    * [ AI policy  ](https://docs.ntfy.sh/ai-policy/)
    * [ Privacy policy  ](https://docs.ntfy.sh/privacy/)
    * [ Terms of Service  ](https://docs.ntfy.sh/terms/)
    * [ Contact  ](https://docs.ntfy.sh/contact/)


# Frequently asked questions (FAQ)[¶](https://docs.ntfy.sh/faq/#frequently-asked-questions-faq "Permanent link")
## Isn't this like ...?[¶](https://docs.ntfy.sh/faq/#isnt-this-like "Permanent link")
Who knows. I didn't do a lot of research before making this. It was fun making it.
## Can I use this in my app? Will it stay free?[¶](https://docs.ntfy.sh/faq/#can-i-use-this-in-my-app-will-it-stay-free "Permanent link")
Yes. As long as you don't abuse it, it'll be available and free of charge. While I will always allow usage of the ntfy.sh server without signup and free of charge, I may also offer paid plans in the future.
## What are the uptime guarantees?[¶](https://docs.ntfy.sh/faq/#what-are-the-uptime-guarantees "Permanent link")
Best effort. 
ntfy currently runs on a single DigitalOcean droplet, without any scale out strategy or redundancies. When the time comes, I'll add scale out features, but for now it is what it is.
In the first year of its life, and to this day (Dec'22), ntfy had **no outages** that I can remember. Other than short blips and some HTTP 500 spikes, it has been rock solid. 
There is a [status page](https://ntfy.statuspage.io/) which is updated based on some automated checks via the amazingly awesome [healthchecks.io](https://healthchecks.io/) (_no affiliation, just a fan_).
## What happens if there are multiple subscribers to the same topic?[¶](https://docs.ntfy.sh/faq/#what-happens-if-there-are-multiple-subscribers-to-the-same-topic "Permanent link")
As per usual with pub-sub, all subscribers receive notifications if they are subscribed to a topic.
## Will you know what topics exist, can you spy on me?[¶](https://docs.ntfy.sh/faq/#will-you-know-what-topics-exist-can-you-spy-on-me "Permanent link")
If you don't trust me or your messages are sensitive, run your own server. It's open source. That said, the logs do contain topic names and IP addresses, but I don't use them for anything other than troubleshooting and rate limiting. Messages are cached for the duration configured in `server.yml` (12h by default) to facilitate service restarts, message polling and to overcome client network disruptions.
## Can I self-host it?[¶](https://docs.ntfy.sh/faq/#can-i-self-host-it "Permanent link")
Yes. The server (including this Web UI) can be self-hosted, and the Android/iOS app supports adding topics from your own server as well. Check out the [install instructions](https://docs.ntfy.sh/install/).
## Is Firebase used?[¶](https://docs.ntfy.sh/faq/#is-firebase-used "Permanent link")
In addition to caching messages locally and delivering them to long-polling subscribers, all messages are also published to Firebase Cloud Messaging (FCM) (if `FirebaseKeyFile` is set, which it is on ntfy.sh). This is to facilitate notifications on Android. 
If you do not care for Firebase, I suggest you install the [F-Droid version](https://f-droid.org/en/packages/io.heckel.ntfy/) of the app and [self-host your own ntfy server](https://docs.ntfy.sh/install/).
## How much battery does the Android app use?[¶](https://docs.ntfy.sh/faq/#how-much-battery-does-the-android-app-use "Permanent link")
If you use the ntfy.sh server, and you don't use the [instant delivery](https://docs.ntfy.sh/subscribe/phone/#instant-delivery) feature, the Android/iOS app uses no additional battery, since Firebase Cloud Messaging (FCM) is used. If you use your own server, or you use _instant delivery_ (Android only), or install from F-droid ([which does not support FCM](https://f-droid.org/docs/Inclusion_Policy/)), the app has to maintain a constant connection to the server, which consumes about 0-1% of battery in 17h of use (on my phone). There has been a ton of testing and improvement around this. I think it's pretty decent now.
## Paid plans? I thought it was open source?[¶](https://docs.ntfy.sh/faq/#paid-plans-i-thought-it-was-open-source "Permanent link")
All of ntfy will remain open source, with a free software license (Apache 2.0 and GPLv2). If you'd like to self-host, you can (and should do that). The paid plans I am offering are for people that do not want to self-host, and/or need higher limits.
## What is instant delivery?[¶](https://docs.ntfy.sh/faq/#what-is-instant-delivery "Permanent link")
[Instant delivery](https://docs.ntfy.sh/subscribe/phone/#instant-delivery) is a feature in the Android app. If turned on, the app maintains a constant connection to the server and listens for incoming notifications. This consumes additional battery (see above), but delivers notifications instantly.
## Can you implement feature X?[¶](https://docs.ntfy.sh/faq/#can-you-implement-feature-x "Permanent link")
Yes, maybe. Check out [existing GitHub issues](https://github.com/binwiederhier/ntfy/issues) to see if somebody else had the same idea before you, or file a new issue. I'll likely get back to you within a few days.
## I'm having issues with iOS, can you help? The iOS app is behind compared to the Android app, can you fix that?[¶](https://docs.ntfy.sh/faq/#im-having-issues-with-ios-can-you-help-the-ios-app-is-behind-compared-to-the-android-app-can-you-fix-that "Permanent link")
The iOS is very bare bones and quite frankly a little buggy. I wanted to get something out the door to make the iOS users happy, but halfway through I got frustrated with iOS development and paused development. I will eventually get back to it, or hopefully, somebody else will come along and help out. Please review the [known issues](https://docs.ntfy.sh/known-issues/) for details.
## Can I disable the web app? Can I protect it with a login screen?[¶](https://docs.ntfy.sh/faq/#can-i-disable-the-web-app-can-i-protect-it-with-a-login-screen "Permanent link")
The web app is a static website without a backend (other than the ntfy API). All data is stored locally in the browser cache and local storage. That means it does not need to be protected with a login screen, and it poses no additional security risk. So technically, it does not need to be disabled.
However, if you still want, you can require login with the `require-login: true` option, or disable it with the `web-root: disable` option in the `server.yml` file. 
Think of the ntfy web app like an Android/iOS app. It is freely available and accessible to anyone, yet useless without a proper backend. So as long as you secure your backend with ACLs, exposing the ntfy web app to the Internet is harmless.
## If topic names are public, could I not just brute force them?[¶](https://docs.ntfy.sh/faq/#if-topic-names-are-public-could-i-not-just-brute-force-them "Permanent link")
If you don't have [ACLs set up](https://docs.ntfy.sh/config/#access-control), the topic name is your password, it says so everywhere. If you choose a easy-to-guess/dumb topic name, people will be able to guess it. If you choose a randomly generated topic name, the topic is as good as a good password.
As for brute forcing: It's not possible to brute force a ntfy server for very long, as you'll get quickly rate limited. In the default configuration, you'll be able to do 60 requests as a burst, and then 1 request per 10 seconds. Assuming you choose a random 10 digit topic name using only A-Z, a-z, 0-9, _ and -, there are 64^10 possible topic names. Even if you could do hundreds of requests per seconds (which you cannot), it would take many years to brute force a topic name.
For ntfy.sh, there are additional protections in place which will ban your IP pretty quickly. If you think you have been banned from ntfy.sh, you can check at [am-i-banned.ntfy.sh](https://am-i-banned.ntfy.sh/).
## Where can I donate?[¶](https://docs.ntfy.sh/faq/#where-can-i-donate "Permanent link")
I have just very recently started accepting donations via [GitHub Sponsors](https://github.com/sponsors/binwiederhier). I would be humbled if you helped me carry the server and developer account costs. Even small donations are very much appreciated.
## Can I email you? Can I DM you on Discord/Matrix?[¶](https://docs.ntfy.sh/faq/#can-i-email-you-can-i-dm-you-on-discordmatrix "Permanent link")
For community support, please use the public channels listed on the [contact page](https://docs.ntfy.sh/contact/). I generally **do not respond to direct messages** about ntfy, unless you are paying for a [ntfy Pro](https://ntfy.sh/#pricing) plan (see [paid support](https://docs.ntfy.sh/contact/#paid-support)), or you are inquiring about business opportunities (see [other inquiries](https://docs.ntfy.sh/contact/#other-inquiries)).
I am sorry, but answering individual questions about ntfy on a 1-on-1 basis is not scalable. Answering your questions in public forums benefits others, since I can link to the discussion at a later point in time, or other users may be able to help out. I hope you understand.
Made with ❤️ by Philipp C. Heckel 
Made with [ Material for MkDocs ](https://squidfunk.github.io/mkdocs-material/)
[ ](https://github.com/binwiederhier "github.com")

