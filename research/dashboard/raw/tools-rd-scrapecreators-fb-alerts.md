[![ScrapeCreators](https://scrapecreators.com/logo.png)ScrapeCreators](https://scrapecreators.com/)
APIs
[Pricing](https://scrapecreators.com/#pricing)[Docs](https://docs.scrapecreators.com/)[Status](https://scrapecreators.com/status)[Skills](https://scrapecreators.com/skills)[Blog](https://scrapecreators.com/blog)[Changelog](https://scrapecreators.com/changelog)
[Get started](https://app.scrapecreators.com)
Facebook  11 min read • Sep 13, 2026
#  5 Ways to Get Facebook Marketplace Alerts Faster in 2026
Compare five ways to get Facebook Marketplace alerts, from free saved-search notifications to apps, APIs, scheduled Actors, and a self-hosted monitor. 
![Adrian Horning](https://thewebscrapingguy.com/me.png)
by Adrian Horning
Sep 13, 2026 
Copy link
![Decision map comparing native notifications, alert apps, APIs, scheduled Actors, and self-hosted Facebook Marketplace monitors](https://scrapecreators.com/_astro/featured.BigF932f_WD03p.png)
**Facebook’s saved-search notifications are the simplest free way to get Marketplace alerts. Use a dedicated app if you want ready-made phone alerts. Use an API if you need exact filters, your own polling schedule, price-drop logic, or alerts inside a product.** No option can promise every listing the second it appears, so test the method in the city and category you care about.
I run ScrapeCreators, which is one of the API options below. I checked each provider’s current product and pricing pages on September 13, 2026. I also ran the ScrapeCreators Marketplace search and item endpoints. I did not run a controlled speed test across all five options.
## Quick comparison  
| Rank  | Method  | Best for  | Cost checked September 13, 2026  | Main tradeoff  |  
| --- | --- | --- | --- | --- |  
| 1  | [Facebook notifications](https://www.facebook.com/help/2229494877335159)  | A free personal saved search  | Free with a Facebook account  | Little control over timing, state, or delivery  |  
| 2  | [ScrapeCreators API](https://scrapecreators.com/facebookMarketplace-api)  | Custom alerts inside an app or workflow  | 1 credit per successful search or item request  | You build the scheduler, storage, and notification  |  
| 3  | [Swoopa](https://getswoopa.com/)  | A ready-made alert app, especially for vehicles  | 7-day trial; basic Go plan starts at $47 month to month  | Fixed product and subscription rather than an API  |  
| 4  | [Apify Marketplace Scraper](https://apify.com/apify/facebook-marketplace-scraper)  | Scheduled Actor runs and datasets  | Actor page lists pricing from $2.60 per 1,000 listings  | More run and dataset plumbing  |  
| 5  | [AI Marketplace Monitor](https://github.com/BoPeng/ai-marketplace-monitor)  | A self-hosted hobby project  | Open-source software; hosting, proxy, and AI costs vary  | You maintain Python, Playwright, login, and CAPTCHA handling  |  
These numbers use different units. ScrapeCreators charges per request, Swoopa sells plans, Apify quotes a listing-based Actor rate, and self-hosting shifts the bill to infrastructure and your own time. Estimate the whole alert loop, not the smallest number in one pricing box.
## What a useful alert system needs
A Marketplace alert is only useful when it answers four questions:
  1. Is this listing actually new to me?
  2. Does it match my location, price, condition, and category rules?
  3. Has its price changed since I last saw it?
  4. Can I open the original listing before it disappears?


Speed matters, but bad matching creates noise. The stronger design is usually a narrow search, a stored set of listing IDs, and a clear delivery rule. If a search returns the same 24 listings every minute, your system should send zero new alerts after the first baseline run.
Audience research pointed to the same problem. In one public Reddit thread, the original poster said Facebook’s built-in alert was too slow and good deals were sold before the notification arrived. Replies suggested constant refreshing, paid alert apps, and a DIY Python job. Other users asked for Android support, cheaper plans, reliable location filters, and price-drop alerts. A YouTube tutorial about newest-first Marketplace URLs drew comments from resellers who cared about seeing recent items rather than Facebook’s suggested feed.
That is why this list includes both simple consumer options and developer tools. They solve different versions of the job.
## Five ways to get Facebook Marketplace alerts
### 1. Start with Facebook’s own notifications
Facebook has a Marketplace notification category for saved searches. Its [Help Center instructions](https://www.facebook.com/help/2229494877335159) point users to Marketplace profile, Settings, Notifications, then the category they want to enable or disable.
This is the right first step for one or two personal searches. It costs nothing, lives in the Facebook app, and does not require another account or service.
The limitation is control. You do not choose a polling interval, inspect raw result IDs, keep your own price history, or route events into a business workflow. Public user reports also complain about delayed or inconsistent saved-search alerts. Those reports are anecdotes, not a measured platform-wide failure rate, but they explain why alert apps exist.
Choose this if you are a casual buyer and can tolerate checking Marketplace manually too.
### 2. Build the alert around a Marketplace search API
A search API is the best fit when an alert is part of software rather than a personal shopping habit. [ScrapeCreators’ Facebook Marketplace API](https://scrapecreators.com/facebookMarketplace-api) exposes three relevant read endpoints:
  * Location search turns a place name into coordinates.
  * [Marketplace search](https://docs.scrapecreators.com/v1/facebook/marketplace/search/) accepts a keyword, latitude, longitude, radius, price range, sort order, condition, date listed, availability, category, and pagination cursor.
  * [Marketplace item](https://docs.scrapecreators.com/v1/facebook/marketplace/item/) fetches a known listing by ID or URL for fields such as description, photos, attributes, location, price, and status when Facebook exposes them.


The search docs are unusually direct about alerting: even with `sort_by=creation_time_descend`, identical requests can return slightly different ordering. Scrape multiple pages when coverage matters and deduplicate by listing ID. Do not decide that the first array element is always the newest record.
ScrapeCreators returns JSON. It does not send the final notification. That is deliberate. You control whether a new listing goes to email, SMS, Slack, Discord, a mobile push service, or a queue inside your own product.
Each successful search costs one credit. An item detail lookup costs another credit. The current public pricing shows 25,000 credits for $47 and 500,000 for $497, with 100 free credits for a new account. A cheap design runs one search per interval and fetches details only for new candidates.
Choose this if you need custom rules, state, multiple delivery channels, or an alert feature for your users.
### 3. Use Swoopa for a ready-made phone app
[Swoopa](https://getswoopa.com/) is built around private-party deal alerts. Its current site says it monitors Facebook Marketplace plus Craigslist, OfferUp, Kijiji, Gumtree, Nextdoor, and eBay. Users configure keywords, price, distance, and condition, then receive app or email notifications.
The product now leans heavily toward vehicle sourcing. Its filters include make, model, year, mileage, and location. Higher plans add faster alert tiers, price-drop alerts, and AI deal evaluation.
The pricing page showed a 7-day trial on September 13, 2026. The basic Swoopa Go plan was $47 month to month or $28 per month with a 12-month commitment. Turbo and Nitro were more expensive, and the page placed price-drop alerts on Nitro. Recheck the plan before buying because the feature and commitment matter more than the headline monthly number.
This is easier than writing a worker and database. It is also less flexible. You use the filters, alert speeds, supported marketplaces, and delivery experience the app provides.
Choose Swoopa if you want a no-code mobile product and its vehicle focus matches your work.
### 4. Schedule the Apify Marketplace Actor
[Apify’s maintained Facebook Marketplace Scraper](https://apify.com/apify/facebook-marketplace-scraper) accepts Marketplace location, category, search, or item URLs. The Actor page says it can collect titles, URLs, prices, location, photos, seller details, videos, status, and delivery type. It can run through an API, export datasets, and use Apify schedules and integrations.
That makes it a reasonable alert source for a team already using Actors. Schedule the run, read the resulting dataset, compare listing IDs with the prior dataset, then send notifications from an integration or webhook step.
The Actor page displayed pricing from $2.60 per 1,000 listings when checked. It also showed a 3.9 rating from 31 reviews, 736 monthly active users, and a one-day issue response time. Those storefront numbers can move, so treat them as a dated snapshot.
The tradeoff is workflow shape. An Actor run and dataset are useful for batch collection, but they are not the same as one synchronous search response. Your alert latency includes the schedule, run time, dataset read, and notification step.
Choose Apify if you already want its Actor, dataset, and integration model.
### 5. Self-host AI Marketplace Monitor
[AI Marketplace Monitor](https://github.com/BoPeng/ai-marketplace-monitor) is an open-source Python project that opens a browser, searches Facebook Marketplace, evaluates listings, and sends notifications through services including Pushbullet, Pushover, Telegram, Ntfy, and email.
The project supports keyword, price, location, and exclusion rules. Its README also documents multiple AI providers and local Ollama models. On September 13, 2026, the GitHub repository showed 336 stars, 88 forks, 149 commits, 12 open issues, and 6 open pull requests.
This route gives you the code and the most local control. It also gives you the maintenance. The current quick start requires Python 3.10 or newer and Playwright. The Docker instructions include an interactive browser path for Facebook login or CAPTCHA. The project’s own legal notice says Facebook’s EULA prohibits unauthorized automated collection and that users are responsible for compliance.
Choose it for a technical hobby project where self-hosting and browser maintenance are acceptable. Do not pick it because the software has no license fee and then ignore server, proxy, AI, and engineering costs.
## Build a custom alert with the API
A dependable custom alert has two stages. Search first. Fetch item details only after a listing passes the cheap rules.
This Node.js example stores a listing’s last seen price in a JSON file. In production, use a database with a unique key on the listing ID and a transaction around each update.

```
1import { readFile, writeFile } from "node:fs/promises";2 3const endpoint = new URL(4  "https://api.scrapecreators.com/v1/facebook/marketplace/search",5);6endpoint.search = new URLSearchParams({7  query: "electric bike",8  lat: "30.2677",9  lng: "-97.7475",10  radius_km: "65",11  max_price: "900",12  sort_by: "creation_time_descend",13  date_listed: "1",14  availability: "available",15}).toString();16 17const response = await fetch(endpoint, {18  headers: { "x-api-key": process.env.SCRAPE_CREATORS_API_KEY },19});20if (!response.ok) throw new Error(`Marketplace search failed: ${response.status}`);21 22const body = await response.json();23const previous = JSON.parse(24  await readFile("marketplace-state.json", "utf8").catch(() => "{}"),25);26const next = { ...previous };27const alerts = [];28 29for (const listing of body.listings ?? []) {30  const price = listing.price?.amount ?? null;31  const oldPrice = previous[listing.id]?.price ?? null;32 33  if (!previous[listing.id]) {34    alerts.push({ type: "new", listing });35  } else if (price !== null && oldPrice !== null && price < oldPrice) {36    alerts.push({ type: "price_drop", oldPrice, listing });37  }38 39  next[listing.id] = {40    price,41    lastSeenAt: new Date().toISOString(),42    url: listing.url,43  };44}45 46await writeFile("marketplace-state.json", JSON.stringify(next, null, 2));47console.log(alerts);
```

Run the first request as a baseline without sending anything. On later runs, notify only for a new ID or a lower stored price. This avoids blasting yourself with every existing result when the worker first starts.
A production version should also:
  * lock overlapping jobs so two polls do not send the same alert;
  * expire old state after a reasonable retention period;
  * follow pagination when missing a listing would be costly;
  * handle null prices and missing dates;
  * retry temporary failures without treating an empty response as a real market event;
  * fetch item details only after the search result passes your first filter.


Do not use one universal polling interval. A collector buying vehicles may accept a paid frequent schedule. A rental research dashboard might run every few hours. More polling means more requests, more duplicates to process, and more exposure to upstream changes.
## What I verified in a live request
I ran one Marketplace search on September 13, 2026 with these parameters:

```
1query=bike2lat=30.26773lng=-97.74754radius_km=655count=56sort_by=creation_time_descend7date_listed=18availability=available
```

The endpoint returned HTTP 200, 24 listing rows, and a pagination cursor. The first result included a stable listing ID, URL, title, a `$650` price, `creation_time`, `listing_date_text`, Austin location data, and a category ID. The returned page was larger than the requested `count=5`, so do not assume `count` is a hard cap.
I then sent that listing URL to the item endpoint. It returned HTTP 200 with the same ID and title plus description, exact coordinates, currency, condition, four photos, delivery type, messaging availability, and live/sold status fields. The seller field was null on this item. That is a useful reminder that optional fields really are optional.
This was a two-request field and contract check, not a claim about average speed or uptime.
## Limits and safety
Facebook Marketplace is a moving source. Listings disappear, prices change, fields are absent, and the same search can shift between requests. Build the alert as a fallible observation system, not a perfect inventory feed.
  * A newest-first sort is a preference, not a guarantee of stable ordering.
  * A null date does not prove a listing is old.
  * A missing seller does not make an item invalid.
  * A price drop requires your own earlier observation. One current price is not price history.
  * Public listing access does not grant permission to republish personal data without limits.
  * Monitoring listings is not the same as automating messages, purchases, or account actions.


Review [Meta’s Automated Data Collection Terms](https://www.facebook.com/legal/automated_data_collection_terms) and get legal advice for regulated, high-risk, or large-scale collection. Our [web scraping legal guide](https://scrapecreators.com/blog/web-scraping-legal) is a practical starting point, not legal advice.
If your actual goal is broad data collection rather than alerts, read the [Facebook Marketplace API and scraper comparison](https://scrapecreators.com/blog/facebook-marketplace-api-tools). For monitoring across several social platforms, the [social media scraping API guide](https://scrapecreators.com/blog/best-social-media-scraping-apis) covers a wider set of tools.
## Sources checked
I checked these primary pages on September 13, 2026:
  * [Facebook Help Center: turn Marketplace notifications on or off](https://www.facebook.com/help/2229494877335159)
  * [Meta Automated Data Collection Terms](https://www.facebook.com/legal/automated_data_collection_terms)
  * [ScrapeCreators Facebook Marketplace API](https://scrapecreators.com/facebookMarketplace-api), [search docs](https://docs.scrapecreators.com/v1/facebook/marketplace/search/), [item docs](https://docs.scrapecreators.com/v1/facebook/marketplace/item/), and the public pricing section
  * [Swoopa product page](https://getswoopa.com/) and [pricing](https://getswoopa.com/subscription-options/)
  * [Apify Facebook Marketplace Scraper](https://apify.com/apify/facebook-marketplace-scraper)
  * [AI Marketplace Monitor repository](https://github.com/BoPeng/ai-marketplace-monitor)


Prices, alert speeds, storefront statistics, fields, and access rules can change. Recheck the source before committing to a plan or promising a field to a customer.
FAQ
## Frequently asked  
questions
Can't find what you're looking for? Email us.
### How do I get alerts for new Facebook Marketplace listings?
### Can Facebook Marketplace notify me about price drops?
### What is the fastest Facebook Marketplace alert option?
### Does ScrapeCreators send Facebook Marketplace notifications?
### Can I automate messages to Facebook Marketplace sellers?
![Adrian Horning](https://thewebscrapingguy.com/me.png)
Written by
Adrian Horning
Founder of ScrapeCreators 
Connect
[ ](https://x.com/adrian_horning_) [ ](https://linkedin.com/in/adrianhorning)
Scrape social media data in seconds.
Production-ready APIs
For real-world use.
Instant access
No setup. No waiting.
Built for reliability
Scale with confidence.
![Purple gift box representing 100 free ScrapeCreators credits](https://scrapecreators.com/_astro/gift.GRji_2eH.png)
_100_ credits for free
No credit card required. Start building for free.
[ Get started free ](https://app.scrapecreators.com/)
Join 10,000+ developers building with ScrapeCreators APIs. 
Related articles
[View all](https://scrapecreators.com/blog)
[ ![6 best Facebook post scrapers in 2026](https://scrapecreators.com/_astro/featured.Bq92T4e0_Z1FCnUW.webp) 6 best Facebook post scrapers in 2026 ](https://scrapecreators.com/blog/facebook-post-scrapers)[ ![5 Ways to Export Facebook Marketplace Listings to CSV in 2026](https://scrapecreators.com/_astro/featured.PvIu77Zh_Zkb64u.webp) 5 Ways to Export Facebook Marketplace Listings to CSV in 2026 ](https://scrapecreators.com/blog/facebook-marketplace-csv-export)
On this page 
  * [Quick comparison](https://scrapecreators.com/blog/facebook-marketplace-alerts#quick-comparison)
  * [What a useful alert system needs](https://scrapecreators.com/blog/facebook-marketplace-alerts#what-a-useful-alert-system-needs)
  * [Five ways to get Facebook Marketplace alerts](https://scrapecreators.com/blog/facebook-marketplace-alerts#five-ways-to-get-facebook-marketplace-alerts)
  * [Build a custom alert with the API](https://scrapecreators.com/blog/facebook-marketplace-alerts#build-a-custom-alert-with-the-api)

Show 3 more sections 
  * [What I verified in a live request](https://scrapecreators.com/blog/facebook-marketplace-alerts#what-i-verified-in-a-live-request)
  * [Limits and safety](https://scrapecreators.com/blog/facebook-marketplace-alerts#limits-and-safety)
  * [Sources checked](https://scrapecreators.com/blog/facebook-marketplace-alerts#sources-checked)


[![ScrapeCreators](https://scrapecreators.com/logo.png)ScrapeCreators](https://scrapecreators.com/)
Social Media Scraping API  
for Developers
Real-time data from TikTok, Instagram, YouTube, X, Facebook, Reddit, and more.
Real-time Data
Fresh, accurate, always up-to-date.
No Proxies
We handle the infrastructure.
Developer First
Simple API. Powerful results.
![TikTok logo](https://www.google.com/s2/favicons?domain=tiktok.com&sz=64)![Instagram logo](https://www.google.com/s2/favicons?domain=instagram.com&sz=64)![YouTube logo](https://www.google.com/s2/favicons?domain=youtube.com&sz=64)![X logo](https://www.google.com/s2/favicons?domain=x.com&sz=64)![Facebook logo](https://www.google.com/s2/favicons?domain=facebook.com&sz=64)![Reddit logo](https://www.google.com/s2/favicons?domain=reddit.com&sz=64)
{200 OK
"platform": "youtube",
"type": "video",
"title": "Never Gonna Give You Up",
"views": 12504321,
"transcript": "We're no strangers to love...",
}
Success124ms
![Purple gift box representing 100 free ScrapeCreators credits](https://scrapecreators.com/_astro/gift.GRji_2eH.png)
Get 100 credits on us - instantly.
No credit card required. Start building for free.
Try the API, on us.
New developers get 100 free credits automatically when they sign up. No credit card required.
[Get started free](https://app.scrapecreators.com/)
Trusted by 10,000+ developers
99.9% uptime
Secure API access
ScrapeCreators
One API for every social platform. Built in Austin, TX by a small global team that ships fast and actually answers emails.
Product
  * [Pricing](https://scrapecreators.com/#pricing)
  * [Enterprise](https://scrapecreators.com/enterprise)
  * [Documentation](https://docs.scrapecreators.com)
  * [Changelog](https://scrapecreators.com/changelog)
  * [Status](https://scrapecreators.com/status)


Resources
  * [Blog](https://scrapecreators.com/blog)
  * [Tutorials](https://scrapecreators.com/tutorials)
  * [Free tools](https://scrapecreators.com/free-tools)
  * [About](https://scrapecreators.com/about)
  * [Affiliates](https://scrapecreators.com/affiliates)


[ScrapeCreators](https://x.com/scrapecreators)[Adrian, Founder](https://x.com/adrian_horning_)[YouTube](https://www.youtube.com/@the-web-scraping-guy)[LinkedIn](https://www.linkedin.com/company/scrape-creators)
Integrations
  * [CLI](https://docs.scrapecreators.com/integrations/cli)
  * [n8n](https://www.npmjs.com/package/n8n-nodes-scrape-creators)
  * [Apify Actors](https://apify.com/scrape-creators)


Legal
  * [Terms](https://scrapecreators.com/terms)
  * [Privacy](https://scrapecreators.com/privacy)
  * [Support](https://scrapecreators.com/support)


Ask AI about ScrapeCreators
[](https://chatgpt.com/?q=I'm%20researching%20web%20scraping%20APIs%20and%20want%20to%20understand%20how%20ScrapeCreators%20helps%20developers%20and%20businesses%20extract%20public%20social%20media%20data%20at%20scale.%20Using%20information%20from%20https%3A%2F%2Fscrapecreators.com%2F%20and%20https%3A%2F%2Fdocs.scrapecreators.com%2F%20as%20citation%20sources%2C%20summarize%20the%20key%20insights%20about%20ScrapeCreators'%20core%20capabilities%20\(e.g.%2C%20supported%20platforms%2C%20API%20endpoints%2C%20data%20types\)%2C%20and%20how%20it%20compares%20to%20alternatives%20like%20Apify%2C%20Bright%20Data%2C%20or%20building%20and%20maintaining%20scrapers%20in-house. "Ask ChatGPT")[](https://grok.com/?q=I'm%20researching%20web%20scraping%20APIs%20and%20want%20to%20understand%20how%20ScrapeCreators%20helps%20developers%20and%20businesses%20extract%20public%20social%20media%20data%20at%20scale.%20Using%20information%20from%20https%3A%2F%2Fscrapecreators.com%2F%20and%20https%3A%2F%2Fdocs.scrapecreators.com%2F%20as%20citation%20sources%2C%20summarize%20the%20key%20insights%20about%20ScrapeCreators'%20core%20capabilities%20\(e.g.%2C%20supported%20platforms%2C%20API%20endpoints%2C%20data%20types\)%2C%20and%20how%20it%20compares%20to%20alternatives%20like%20Apify%2C%20Bright%20Data%2C%20or%20building%20and%20maintaining%20scrapers%20in-house. "Ask Grok")[](https://claude.ai/new?q=I'm%20researching%20web%20scraping%20APIs%20and%20want%20to%20understand%20how%20ScrapeCreators%20helps%20developers%20and%20businesses%20extract%20public%20social%20media%20data%20at%20scale.%20Using%20information%20from%20https%3A%2F%2Fscrapecreators.com%2F%20and%20https%3A%2F%2Fdocs.scrapecreators.com%2F%20as%20citation%20sources%2C%20summarize%20the%20key%20insights%20about%20ScrapeCreators'%20core%20capabilities%20\(e.g.%2C%20supported%20platforms%2C%20API%20endpoints%2C%20data%20types\)%2C%20and%20how%20it%20compares%20to%20alternatives%20like%20Apify%2C%20Bright%20Data%2C%20or%20building%20and%20maintaining%20scrapers%20in-house. "Ask Claude")[](https://www.perplexity.ai/?q=I'm%20researching%20web%20scraping%20APIs%20and%20want%20to%20understand%20how%20ScrapeCreators%20helps%20developers%20and%20businesses%20extract%20public%20social%20media%20data%20at%20scale.%20Using%20information%20from%20https%3A%2F%2Fscrapecreators.com%2F%20and%20https%3A%2F%2Fdocs.scrapecreators.com%2F%20as%20citation%20sources%2C%20summarize%20the%20key%20insights%20about%20ScrapeCreators'%20core%20capabilities%20\(e.g.%2C%20supported%20platforms%2C%20API%20endpoints%2C%20data%20types\)%2C%20and%20how%20it%20compares%20to%20alternatives%20like%20Apify%2C%20Bright%20Data%2C%20or%20building%20and%20maintaining%20scrapers%20in-house. "Ask Perplexity")
© 2026 ScrapeCreators. All rights reserved.
Proudly built in Austin, TX 🇺🇸

