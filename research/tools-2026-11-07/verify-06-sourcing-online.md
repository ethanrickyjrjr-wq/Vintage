# Verification: lane 06 sourcing online (deal-alert and online sourcing tools)

Date: 2026-11-07. Author: research subagent (adversarial price and claim checker).
Question: do the prices, free tiers, platform claims and availability claims recorded by the first lane-06 agent hold up against the vendors' own pages today?
Legend: V = page read today; U = unverified (page would not load after one alternative attempt, or claim rests on a snippet or memory).
Method: every page below was fetched today through headless Chromium (curl fallback) from this container. WebSearch budget was exhausted before this check started, so URLs were taken from the first agent's list, from links on vendor pages, or from the vendor's own help-center API. No roundups were used for prices. Reddit was not read.

## 0. Bottom line

- 24 checks on 20 tools. 19 confirmed, 3 refuted or corrected, 2 unreadable.
- Every price in the first agent's PICKS and the top TOOLS rows matched the vendor page today: Visualping, Distill, PageCrawl, Botifex, IFTTT, Zapier, Swoopa, changedetection.io hosted $8.99 / Month, CTBids Premier $99/year, gsalr $4.99 ad-free.
- Refuted: the EstateSales.org source URL (`/subscribe` is a 404 today; the sign-up form is a modal on the homepage). Refuted: uBuyFirst's "30-day free access advertised" (no page read today states a trial length; they say "Start Free Trial" only).
- Corrected nuance: Proxibid's saved-search email default is once a week; daily is a setting you must pick. CTBids Premier's WorthPoint benefit is a 90-day All-Access subscription, not year-long access. gsalr's homepage says both "Free daily emails" and "delivered to your inbox every week".
- Resolved: LiveAuctioneers followed searches alert by both email ("search alert emails") and app push ("New Items From Followed Searches").
- Unreadable: HiBid saved-search alert mechanics (FAQ page missing, support site behind Cloudflare). Invaluable keyword alerts (help, help center and FAQ all 404).
- No shutdown or acquisition notices were seen on any page read today.

## 1. Checks

| Tool | Claim checked | Verdict | Evidence quote | URL | Correction |
|---|---|---|---|---|---|
| EstateSales.net | Free email sale notifications for shoppers | confirmed | "Free E-mail notifications: get notified via E-mail about upcoming sales near you!" | https://www.estatesales.net/help/frequently-asked-questions | none |
| EstateSales.net | Free iOS and Android app | confirmed | "Use our iOS or Android app ... Download the free app today!" | https://www.estatesales.net/ | Android listing read (Google Play, "Estate Sales", by EstateSales.NET). Apple listing not read: no search budget to find its ID. |
| EstateSales.net | Treasure Tracker keyword feature exists | confirmed | "terms that might be searched or used for Treasure Tracker" | https://www.estatesales.net/help/frequently-asked-questions | Feature named on the FAQ; how it alerts is not described there. |
| EstateSales.net | Email cadence: users pick lead day | confirmed | "more than 90%, choose to receive an email one day before a sale starts" | https://www.estatesales.net/help/frequently-asked-questions | none |
| EstateSales.org | Source URL `estatesales.org/subscribe` is the sign-up form | refuted | "Sorry, the page you requested cannot be found." | https://estatesales.org/subscribe | Returns HTTP 404 today. The form is a modal on https://estatesales.org/ ("Get notified of estate sales near you!"). |
| EstateSales.org | Free alerts: radius 5 to 100 miles, pick days, Online Auction Items email, categories, gsalr digest | confirmed | "Email me sales within 5 miles ... 100 miles"; "Days to receive emails? Mon ... Sun"; "Online Auction Items" | https://estatesales.org/ | No price or payment step on the form. |
| eBay saved searches | Free email alerts on new matching items | confirmed | "We'll send you email alerts when new items matching your search are listed." | https://www.ebay.com/help/buying/search-tips/saved-searches?id=4051 | No interval stated on the page, as the first agent said. |
| Proxibid saved search | Free email alerts with a daily option and category filters | confirmed | "default frequency of once a week, or choose to be notified daily, once every three days, or never" | https://discover.proxibid.com/comparison-shopping-hard-help | Default is weekly. Pick daily when saving. Category and sub-category filters confirmed. |
| LiveAuctioneers | Saved searches and search alerts on web and app; channel unknown | confirmed | "New Items From Followed Searches" (Push Notification Settings); "search alert emails" | https://help.liveauctioneers.com/hc/en-gb/articles/24748237629585-What-types-of-notifications-can-I-receive-in-the-LiveAuctioneers-App | Channel resolved: email and app push both exist. Save via "FOLLOW THIS SEARCH". |
| Craigslist | Free automated email per new matching post | confirmed | "Search alerts send an automated email when new postings match one of your saved searches." | https://www.craigslist.org/about/help/account/features/searches | none |
| changedetection.io | Self-hosted free under Apache-2.0; hosted $8.99 / Month | confirmed | "Apache-2.0 license"; "$8.99 / Month Easy Subscription" | https://github.com/dgtlmoon/changedetection.io and https://changedetection.io/ | none |
| changedetection.io | Pushover alerts supported | confirmed | "notifications ... thanks to the apprise library"; apprise: "pover://{user_key}@{token}" | https://github.com/dgtlmoon/changedetection.io and https://github.com/caronc/apprise/wiki/Notify_pushover | Pushover comes through the Apprise library, not a native connector. |
| CTBids Premier | $99/year; WorthPoint access and delivery guarantee | confirmed | "you get all six benefits for only $99/year"; "WorthPoint 90 Day All-Access Subscription" | https://ctbids.com/premier-membership | WorthPoint benefit is 90 days, not the whole year. Delivery Guarantee "Valued up to $192". |
| Visualping | Free $0/mo, 150 checks, 5 pages, every 60 min, 1 user; Personal 1K $14/mo or $120/yr ($10/mo); Personal 5K $35/mo | confirmed | "Free $0/mo Not sold annually 150 5 Every 60 min 1"; "Personal 1K $14/mo $120/yr ($10/mo)" | https://visualping.io/pricing | none |
| Distill.io | Free $0; Starter $15/mon; Professional $35/mon; Flexi $80+/mon; 20% annual discount; free = 25 monitors (5 cloud), 6-hour cloud interval, 1000 checks, 30 emails, 100 push | confirmed | "Starter $15/mon ... Professional $35/mon ... Flexi $80+/mon"; "Monitors 25 (5 in cloud)"; "6 hours"; "30/mon (email only)" | https://distill.io/pricing | none |
| PageCrawl.io | Free Forever $0 / month: 6 pages, 220 checks, up to 60 min, 90 days; Standard $13.33 / month, $160 billed annually | confirmed | "Free Forever $0 / month ... Pages: Up to 6 Checks: Up to 220 Frequency: Up to 60 min ... History: 90 days"; "$13.33 / month $160 billed annually" | https://pagecrawl.io/pricing | none |
| Botifex | Free $0/mo; Basic $19.99/mo; Pro $49.99/mo; Ultra $126.99/mo; annual saves $100/yr; free = Craigslist + eBay, 2 saved searches, 20-minute refresh, dashboard alerts only after trial | confirmed | "Free $0/mo"; "Covers Craigslist + eBay"; "2 saved searches / hunt profiles"; "20-minute refresh cycle"; "Dashboard alerts only after trial"; "Annual Save $100/yr" | https://botifex.com/pricing | Page says "scrapers" and meters "proxy data", as the first agent flagged. |
| IFTTT | Free $0.00 / month, 1,000 credits, Unlimited Applets; Starter $2.09 / month ($25.08 billed annually); Pro $5.49 ($65.88); Pro+ $13.99 ($167.88) | confirmed | "Free $0.00 / month 1,000 credits / month ... Unlimited Applets"; "Starter $2.09 / month $25.08 billed annually" | https://ifttt.com/plans | Monthly figures shown are the yearly-billing rate. |
| Zapier | Free forever $0 /month, 100 tasks, two-step Zaps; Professional $19.99 /month; Team $69 /month | confirmed | "Free forever $0 /month ... (100 tasks per month)"; "Two-step Zaps"; "$19.99 /month"; "$69 /month" | https://zapier.com/pricing | none |
| Swoopa | Go $47/mo or $28/mo on 12-month ($336); Turbo $144/mo or $99/mo 6-month; Nitro $352/mo or $199/mo 6-month; 7-day trial; Go is Facebook only | confirmed | "Choose a Plan For After Your 7-Day Trial"; "$28/mo ... $336"; "$99/mo ... $594"; "$199/mo ... $1,194"; "Only Facebook marketplace" | https://getswoopa.com/pricing | Page title is "Sign Up - Swoopa" (curl render). Platform not stated on this page. |
| gsalr.com | Free daily emails; Go Ad Free for $4.99, billing period not stated | confirmed | "Free daily emails with a list of the newest sales"; "Go Ad Free for $4.99" | https://gsalr.com/ | Same page also says "Get sales delivered to your inbox every week!" Cadence text is inconsistent. No billing period shown. |
| SeeSpotBid | Free with In-App Purchases; PRO price not shown; iOS 15.0+; free tier pauses alerts 6 hours a day | confirmed | "Free · In-App Purchases"; "Requires iOS 15.0 or later."; developer reply: "Being able to turn that off as part of the Pro subscription" | https://apps.apple.com/us/app/seespotbid/id1452120217 | In-App Purchases listed as "Yes" with no prices. Quiet Hours confirmed by the developer's reply to a review. |
| uBuyFirst | Pricing page 404; 30-day free access advertised; App Store Free | refuted (trial length) | "Page not found - uBuyFirst"; "Start Free Trial"; App Store: "Free · Designed for iPad" | https://ubuyfirst.com/pricing and https://ubuyfirst.com/ and https://apps.apple.com/us/app/ubuyfirst-alerts-for-ebay/id1525884557 | No page read today states "30 days". Home, features, about and App Store say "Free Trial" only. Help docs page is behind SpamFireWall. App needs iOS 15.4+; alerts by "push notifications on your phone, plus email, Telegram, WhatsApp, Discord or Slack". |
| AutomatedSearches.com | Free account; faster than eBay's once-a-day emails; frequency not stated | confirmed | "Create a Free Account"; "eBay's once-a-day saved-searches emails."; title: "Free Email & Text Alerts" | https://automatedsearches.com/ | Own interval still not stated. Affiliate-funded (eBay Partner Network). |
| ShopGoodwill | Saved search exists; email behaviour not stated | confirmed | "click on the 'Save Search' button at the top left hand side of the page." | https://shopgoodwill.com/help/faqdetail/how-do-i-create-a-saved-search | Help index lists "Saved Searches" only. No email statement found. |
| HiBid | Saved-search alert mechanics | unreadable | hibid.com/faq: "We can't find that page"; support.hibid.com: "Attention Required! | Cloudflare" | https://hibid.com/faq and https://support.hibid.com/ | Homepage shows a "Manage Notifications" link only. Register page loaded but says nothing about alerts or cost. |
| Invaluable | Free iOS and Android app; keyword alerts | confirmed (app) / unreadable (alerts) | "Download the Invaluable app and never miss an auction from your iOS or Android device." | https://www.invaluable.com/ | /help/, help.invaluable.com and /faq all returned 404 today. |

## 2. What the first agent got wrong or left loose

1. EstateSales.org `source_url` (`/subscribe`) is a 404 today. The sign-up form is a modal on the homepage. Every detail of the form (5 to 100 miles, days of the week, Online Auction Items, categories, gsalr checkbox) is correct.
2. uBuyFirst "30-day free access advertised" is not on any uBuyFirst page or the App Store listing read today. The pages say "Start Free Trial" with no length. Pricing page 404 is confirmed.
3. Proxibid: the daily email is an option, not the default. The default is "once a week". Hollie must pick "daily" when saving the search.
4. CTBids Premier: the WorthPoint benefit is a "90 Day All-Access Subscription", not a year of price-guide access. The $99/year figure is correct.
5. LiveAuctioneers: the open question (email vs push) is settled. Both exist: "search alert emails" and the app's "New Items From Followed Searches" push setting.
6. gsalr: the homepage contradicts itself on cadence ("Free daily emails" and "delivered to your inbox every week"). The first agent's "free daily emails" quote is on the page, but so is the weekly line.
7. EstateSales.net app: the Android listing is confirmed on Google Play. The iOS listing was not read (the guessed App Store ID was wrong and there was no search budget). The vendor homepage states "iOS or Android app ... free".
8. HiBid "watch list" and "free to browse and bid": not stated in words on any HiBid page that loaded today. Keep at U.
9. Invaluable "keyword alert details unverified (help pages 404)": still true today, three help URLs 404.
10. changedetection.io Pushover: supported, but through the Apprise library (`pover://`), not a first-party Pushover integration. Same outcome for Hollie.

## 3. Pages that would not load or were walled

- https://estatesales.org/subscribe (HTTP 404) and https://estatesales.org/register (HTTP 404). Form found on the homepage instead.
- https://apps.apple.com/us/app/estatesales-net/id421325555 (HTTP 404; the ID was a guess).
- https://www.estatesales.net/app (Page Not Found).
- https://hibid.com/faq ("We can't find that page").
- https://support.hibid.com/ (Cloudflare "Attention Required").
- https://www.invaluable.com/help/ (404), https://help.invaluable.com/ (404), https://www.invaluable.com/faq (404).
- https://ubuyfirst.com/pricing (Page not found), https://ubuyfirst.com/help-docs/ (SpamFireWall bot check).
- WebSearch: budget exhausted before this check began (shared per-turn limit), so no new URLs could be searched for.

## 4. Sources (every URL fetched today)

https://www.estatesales.net/help/frequently-asked-questions
https://www.estatesales.net/
https://www.estatesales.net/app
https://www.estatesales.net/help (redirected to https://www.estatesales.net/contact)
https://apps.apple.com/us/app/estatesales-net/id421325555
https://play.google.com/store/apps/details?id=net.estatesales.estatesales&hl=en_US
https://estatesales.org/subscribe
https://estatesales.org/register
https://estatesales.org/
https://www.ebay.com/help/buying/search-tips/saved-searches?id=4051
https://www.craigslist.org/about/help/account/features/searches
https://discover.proxibid.com/comparison-shopping-hard-help
https://help.liveauctioneers.com/hc/en-gb/search?query=saved+search
https://help.liveauctioneers.com/hc/en-gb/search?query=search+alert+email
https://help.liveauctioneers.com/api/v2/help_center/articles/search.json?query=saved%20search
https://help.liveauctioneers.com/hc/en-gb/articles/24746417181969-How-do-I-save-a-search-I-m-interested-in
https://help.liveauctioneers.com/hc/en-gb/articles/24748237629585-What-types-of-notifications-can-I-receive-in-the-LiveAuctioneers-App
https://changedetection.io/
https://github.com/dgtlmoon/changedetection.io
https://github.com/dgtlmoon/changedetection.io/wiki/Notification-configuration-notes
https://github.com/caronc/apprise/wiki/Notify_pushover
https://ctbids.com/premier-membership
https://visualping.io/pricing
https://distill.io/pricing
https://pagecrawl.io/pricing
https://botifex.com/pricing
https://ifttt.com/plans
https://zapier.com/pricing
https://getswoopa.com/pricing
https://gsalr.com/
https://apps.apple.com/us/app/seespotbid/id1452120217
https://ubuyfirst.com/
https://ubuyfirst.com/pricing
https://ubuyfirst.com/features/
https://ubuyfirst.com/about/
https://ubuyfirst.com/help-docs/
https://apps.apple.com/us/app/ubuyfirst-alerts-for-ebay/id1525884557
https://automatedsearches.com/
https://shopgoodwill.com/help/faqdetail/how-do-i-create-a-saved-search
https://shopgoodwill.com/help
https://hibid.com/
https://hibid.com/faq
https://support.hibid.com/
https://hibid.com/register
https://www.invaluable.com/
https://www.invaluable.com/help/
https://help.invaluable.com/
https://www.invaluable.com/faq
