[Skip to main content](https://shopify.dev/docs/api/usage/limits#main-content)
[![Docs page](https://shopify-assets.shopifycdn.com/shopifycloud/shopify-dev/production/assets/dev-docs-logo-2-light-D4UI1jxY.svg)![Docs page](https://shopify-assets.shopifycdn.com/shopifycloud/shopify-dev/production/assets/dev-docs-logo-2-dark-BQ-Bk9XA.svg)](https://shopify.dev/docs)
  * [Apps](https://shopify.dev/docs/apps/build)
  * [Storefronts](https://shopify.dev/docs/storefronts)
  * [Agents](https://shopify.dev/docs/agents)
  * References
  * [Changelog](https://shopify.dev/changelog)


  * Ask assistant`/`
  * [Help](https://shopify.dev/support)
  * •
  * [Log in](http://dev.shopify.com/dashboard)


Collapse sidebar
API references
  * [Overview](https://shopify.dev/docs/api)


* * *
  * ### Core concepts
    * [Versioning](https://shopify.dev/docs/api/usage/versioning)
    * [API authentication](https://shopify.dev/docs/api/usage/authentication)
    * [Access scopes](https://shopify.dev/docs/api/usage/access-scopes)
    * [GraphQL pagination ](https://shopify.dev/docs/api/usage/pagination-graphql)
    * [Search query syntax](https://shopify.dev/docs/api/usage/search-syntax)
    * [Global IDs](https://shopify.dev/docs/api/usage/gids)
    * [Response status codes](https://shopify.dev/docs/api/usage/response-codes)
    * [Limits](https://shopify.dev/docs/api/usage/limits)
    * [Idempotent requests](https://shopify.dev/docs/api/usage/idempotent-requests)
    * [Feature previews](https://shopify.dev/docs/apps/build/stores/feature-previews)
  * ### Dev tools
    * [Shopify CLI](https://shopify.dev/docs/api/shopify-cli)
    * [Shopify GitHub app ](https://shopify.dev/docs/api/github-app)
    * [React Router app package](https://shopify.dev/docs/api/shopify-app-react-router)
    * [Stores](https://shopify.dev/docs/apps/build/stores)
    * [Libraries and templates](https://shopify.dev/docs/api/libraries-and-templates)
  * ### App data and logic
    * [GraphQL Admin API ](https://shopify.dev/docs/api/admin-graphql)
    * [Shopify Functions](https://shopify.dev/docs/api/functions)
    * [ShopifyQL for analytics ](https://shopify.dev/docs/api/shopifyql/latest)
    * [Events](https://shopify.dev/docs/api/events)
    * [Webhooks](https://shopify.dev/docs/api/webhooks)
    * [Payments Apps API](https://shopify.dev/docs/api/payments-apps)
    * REST Admin API (legacy)
  * ### Polaris
    * [Polaris references](https://shopify.dev/docs/api/polaris)
    * [App Home (iframe)](https://shopify.dev/docs/api/app-home)
    * [App Home (UI extension)](https://shopify.dev/docs/api/app-home-ui-extension)
    * [Admin](https://shopify.dev/docs/api/admin-extensions)
    * [Checkout](https://shopify.dev/docs/api/checkout-ui-extensions)
    * [Customer accounts](https://shopify.dev/docs/api/customer-account-ui-extensions)
    * [POS](https://shopify.dev/docs/api/pos-ui-extensions)
    * [Using web components](https://shopify.dev/docs/api/polaris/using-polaris-web-components)
  * ### Storefronts
    * [Storefront API](https://shopify.dev/docs/api/storefront)
    * [Liquid](https://shopify.dev/docs/api/liquid)
    * Ajax API
    * [Hydrogen framework](https://shopify.dev/docs/api/hydrogen)
    * [Hydrogen React library](https://shopify.dev/docs/api/hydrogen-react)
    * [Storefront Web Components](https://shopify.dev/docs/api/storefront-web-components)
    * [Standard events and actions](https://shopify.dev/docs/api/storefront-events-and-actions)
    * [Customer Privacy API](https://shopify.dev/docs/api/customer-privacy)
    * [Customer Account API](https://shopify.dev/docs/api/customer)
    * [WebMCP Tools ](https://shopify.dev/docs/api/web-mcp)
  * ### App management
    * [Partner API](https://shopify.dev/docs/api/partner)
    * [App Events API](https://shopify.dev/docs/api/app-events)
  * ### Additional APIs
    * Customer authentication
    * Web pixel
    * [Shop API](https://shopify.dev/docs/api/shop)
    * Shop Minis
    * [Shop Pay Wallet API](https://shopify.dev/docs/api/commerce-components/pay)


Full index
ExpandOn this page
  * [Rate limits](https://shopify.dev/docs/api/usage/limits#rate-limits)
  * [Input limits](https://shopify.dev/docs/api/usage/limits#input-limits)
  * [Pagination limits](https://shopify.dev/docs/api/usage/limits#pagination-limits)


# Shopify API limits
Install AI ToolkitAsk about this pageCopy MD
Some Shopify APIs limit the inputs they accept, and most are rate-limited. This page covers the limits that apply across the APIs, and points to the figures for each one.
* * *
## 
[Anchor to Rate limits](https://shopify.dev/docs/api/usage/limits#rate-limits)Rate limits
Rate limits keep the platform stable and fair for everyone. How a limit is calculated, and the figures that apply to you, vary by API. Use [industry standard techniques](https://shopify.dev/docs/api/usage/limits#avoiding-rate-limit-errors) for limiting calls, caching results, and retrying requests responsibly.
### 
[Anchor to Rate limits by API](https://shopify.dev/docs/api/usage/limits#rate-limits-by-api)Rate limits by API
Every API applies limits differently, so the figures and the mechanics are documented with each API, including:  
| API  | Rate limits  |  
| --- | --- |  
| GraphQL Admin API  | [Calculated query cost, by plan](https://shopify.dev/docs/apps/build/apis/graphql-admin/rate-limits)  |  
| REST Admin API  | [Request-based bucket and headers](https://shopify.dev/docs/api/admin-rest/usage/rate-limits)  |  
| Storefront API  | [Bot and crawler limits, checkout throttle](https://shopify.dev/docs/api/storefront#rate-limits)  |  
| Customer Account API  | [Cost points per store and customer, plus 3,000 requests per minute per customer](https://shopify.dev/docs/api/customer#rate-limits)  |  
| Payments Apps API  | [Calculated query cost, by plan](https://shopify.dev/docs/api/payments-apps#rate-limits)  |  
| Partner API  | [Request-based limit per API client](https://shopify.dev/docs/api/partner#rate-limits)  |  
| App Events API  | [Request-based limit per app](https://shopify.dev/docs/api/app-events/latest/creating-events#rate-limits)  |  
### 
[Anchor to The leaky bucket algorithm](https://shopify.dev/docs/api/usage/limits#the-leaky-bucket-algorithm)The leaky bucket algorithm
Most Shopify rate limits are enforced with a [leaky bucket algorithm](https://en.wikipedia.org/wiki/Leaky_bucket). The main points to understand about the leaky bucket metaphor are as follows:
  * Each app has access to a bucket. Its size is set by the API and by your plan.
  * Each API request tosses some number of marbles into the bucket. How many depends on the API's rate-limiting method.
  * The bucket leaks continuously at that API's restore rate, which frees up capacity for more marbles.
  * If the bucket fills, you get a throttle error and have to wait for more bucket capacity to become available.


Both the bucket size and the restore rate vary by API and by plan, so refer to [rate limits by API](https://shopify.dev/docs/api/usage/limits#rate-limits-by-api) for the figures that apply to you. This model means that apps that manage API calls responsibly keep capacity for bursts: as long as your average stays under the restore rate, a short burst above it still succeeds.
The Storefront API works differently. Buyer traffic isn't rate-limited at all, and the limits it does apply are described in [Storefront API rate limits](https://shopify.dev/docs/api/storefront#rate-limits).
Shopify may temporarily reduce API rate limits to protect platform stability. We will strive to keep these instances brief and rare. However, your application should be built to handle limits gracefully.
### 
[Anchor to Resource-based rate limits](https://shopify.dev/docs/api/usage/limits#resource-based-rate-limits)Resource-based rate limits
Once a store has 500,000 product variants, no more than 10,000 new variants can be created per day, on any API.
The resources and mutations that are subject to the throttle are listed with each API's rate limits: [GraphQL Admin API](https://shopify.dev/docs/apps/build/apis/graphql-admin/rate-limits#resource-based-rate-limits) and [REST Admin API](https://shopify.dev/docs/api/admin-rest/usage/rate-limits#resource-based-rate-limits).
Plus
The variant creation throttle doesn't apply to stores on the [Shopify Plus](https://www.shopify.com/plus) plan.
**Plus :**
The variant creation throttle doesn't apply to stores on the [Shopify Plus](https://www.shopify.com/plus) plan.
### 
[Anchor to Avoiding rate limit errors](https://shopify.dev/docs/api/usage/limits#avoiding-rate-limit-errors)Avoiding rate limit errors
Designing your app with best practices in mind is the best way to avoid throttling errors. For example, you can stagger API requests in a queue and do other processing tasks while waiting for the next queued job to run. Consider the following best practices when designing your app:
  * Optimize your code to only get the data that your app requires.
  * Use caching for data that your app uses often.
  * Regulate the rate of your requests for smoother distribution.
  * Include code that catches errors. If you ignore these errors and keep trying to make requests, then your app won't be able to gracefully recover.
  * Use metadata about your app's API usage, included with all API responses, to manage your app's behavior dynamically.
  * Your code should stop making additional API requests until enough time has passed to retry. The recommended backoff time is one second.


* * *
## 
[Anchor to Input limits](https://shopify.dev/docs/api/usage/limits#input-limits)Input limits
Input arguments that accept an array have a maximum size of 250, on every Shopify API. Requests return an error if an input array exceeds 250 items.
* * *
## 
[Anchor to Pagination limits](https://shopify.dev/docs/api/usage/limits#pagination-limits)Pagination limits
Pagination of arrays of objects caps at 25,000 objects, and the cap applies to count queries too. For how the limit behaves and what to do when you need to page past it, refer to [GraphQL pagination](https://shopify.dev/docs/api/usage/pagination-graphql#pagination-limits).
* * *
Was this page helpful?
YesNo
  * [Rate limits](https://shopify.dev/docs/api/usage/limits#rate-limits)
  * [Input limits](https://shopify.dev/docs/api/usage/limits#input-limits)
  * [Pagination limits](https://shopify.dev/docs/api/usage/limits#pagination-limits)


### Updates
  * [Developer changelog](https://shopify.dev/changelog)
  * [Shopify Editions](https://www.shopify.com/editions)


### Business growth
  * [Shopify Partners Program](https://www.shopify.com/partners?shpxid=222dd762-CA08-48FF-E4D4-FF926B8FFCAD)
  * [Shopify App Store](https://apps.shopify.com/?shpxid=222dd762-CA08-48FF-E4D4-FF926B8FFCAD)


### Legal
  * [Terms of service](https://www.shopify.com/legal/terms?shpxid=222dd762-CA08-48FF-E4D4-FF926B8FFCAD)
  * [API terms of use](https://www.shopify.com/legal/api-terms?shpxid=222dd762-CA08-48FF-E4D4-FF926B8FFCAD)
  * [Privacy policy](https://www.shopify.com/legal/privacy?shpxid=222dd762-CA08-48FF-E4D4-FF926B8FFCAD)
  * [Partners Program Agreement](https://www.shopify.com/partners/terms?shpxid=222dd762-CA08-48FF-E4D4-FF926B8FFCAD)


### Shopify
  * [About Shopify](https://www.shopify.com/about?shpxid=222dd762-CA08-48FF-E4D4-FF926B8FFCAD)
  * [Shopify Plus](https://www.shopify.com/plus?shpxid=222dd762-CA08-48FF-E4D4-FF926B8FFCAD)
  * [Careers](https://www.shopify.com/careers?shpxid=222dd762-CA08-48FF-E4D4-FF926B8FFCAD)
  * [Investors](https://investors.shopify.com/home/default.aspx?shpxid=222dd762-CA08-48FF-E4D4-FF926B8FFCAD)
  * [Press and media](https://shopify.com/news?shpxid=7db0d4e4-24E8-4087-58FA-7EE470CA745A)



