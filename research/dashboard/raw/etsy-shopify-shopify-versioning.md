[Skip to main content](https://shopify.dev/docs/api/usage/versioning#main-content)
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
  * [Versioned and unversioned APIs](https://shopify.dev/docs/api/usage/versioning#versioned-and-unversioned-apis)
  * [Release schedule](https://shopify.dev/docs/api/usage/versioning#release-schedule)
  * [Making requests to an API version](https://shopify.dev/docs/api/usage/versioning#making-requests-to-an-api-version)
  * [Deprecation practices](https://shopify.dev/docs/api/usage/versioning#deprecation-practices)


# About Shopify API versioning
Install AI ToolkitAsk about this pageCopy MD
Shopify releases new API versions on a predictable quarterly schedule, giving you time to adopt changes before older versions are retired.
Each version's [release notes](https://shopify.dev/changelog/release-notes) list the changes in that version, including anything that requires action. Subscribe to the [developer changelog](https://shopify.dev/changelog) and [keep your developer contact details up to date](https://shopify.dev/docs/apps/build/dev-dashboard/technical-updates#update-your-developer-contact-details) to stay informed about upcoming changes.
* * *
## 
[Anchor to Versioned and unversioned APIs](https://shopify.dev/docs/api/usage/versioning#versioned-and-unversioned-apis)Versioned and unversioned APIs
Not all Shopify APIs follow the same versioning model. Versioned APIs and libraries follow the quarterly release schedule described below. Unversioned APIs and surfaces may change at any time.
### 
[Anchor to Versioned APIs](https://shopify.dev/docs/api/usage/versioning#versioned-apis)Versioned APIs  
| Category  | APIs  | Notes  |  
| --- | --- | --- |  
| GraphQL  | 
  * [GraphQL Admin API](https://shopify.dev/docs/api/admin-graphql)
  * [Customer Account API](https://shopify.dev/docs/api/customer)
  * [Events](https://shopify.dev/docs/api/events)
  * [Function APIs](https://shopify.dev/docs/api/functions)
  * [Partner API](https://shopify.dev/docs/api/partner)
  * [Payments Apps API](https://shopify.dev/docs/api/payments-apps)
  * [Storefront API](https://shopify.dev/docs/api/storefront)
  * [Webhooks](https://shopify.dev/docs/api/webhooks)

 |  Webhook payloads are versioned the same way as API responses. Shopify falls forward when your selected version becomes inaccessible, and webhooks include the `X-Shopify-Api-Version` header to confirm which version was used. [Learn more](https://shopify.dev/docs/apps/build/webhooks). Events is currently available in the `unstable` version and will follow Shopify's API versioning policy soon.  |  
| ShopifyQL  | 
  * [ShopifyQL](https://shopify.dev/docs/api/shopifyql)

 |  When you use ShopifyQL through the GraphQL Admin API, ShopifyQL uses the API version selected for the [`shopifyqlQuery`](https://shopify.dev/docs/api/admin-graphql/current/queries/shopifyqlQuery) request. When you call `shopifyqlQuery` through the `unstable` version of the GraphQL Admin API, Shopify resolves the ShopifyQL schema and API version to the release candidate version.  |  
| Libraries  | 
  * [Hydrogen](https://shopify.dev/docs/api/hydrogen)
  * [Hydrogen React](https://shopify.dev/docs/api/hydrogen-react)
  * [Shopify App React Router](https://shopify.dev/docs/api/shopify-app-react-router)

 | Versioned by major release.  |  
| Polaris  | 
  * [Admin UI extensions](https://shopify.dev/docs/api/admin-extensions)
  * [App Home UI extensions](https://shopify.dev/docs/api/app-home-ui-extension)
  * [Checkout UI extensions](https://shopify.dev/docs/api/checkout-ui-extensions)
  * [Customer account UI extensions](https://shopify.dev/docs/api/customer-account-ui-extensions)
  * [POS UI extensions](https://shopify.dev/docs/api/pos-ui-extensions)

 | Only the last four stable versions have published docs on Shopify.dev. Older versions continue to work, but won't have dedicated reference docs. [Shopify CLI](https://shopify.dev/docs/api/shopify-cli) prevents deploys targeting versions older than 12 months.  |  
### 
[Anchor to Unversioned APIs](https://shopify.dev/docs/api/usage/versioning#unversioned-apis)Unversioned APIs
The following APIs and surfaces aren't versioned and might change at any time:
  * [Ajax API](https://shopify.dev/docs/api/ajax)
  * [App Home](https://shopify.dev/docs/api/app-home) App Bridge APIs (App Home Polaris components are versioned)
  * [Catalog API](https://shopify.dev/docs/api/catalog-api)
  * [Customer Privacy API](https://shopify.dev/docs/api/customer-privacy)
  * [Liquid](https://shopify.dev/docs/api/liquid)
  * [OAuth](https://shopify.dev/docs/apps/build/authentication-authorization) endpoints, including `AccessScope`
  * [Shop Minis](https://shopify.dev/docs/api/shop-minis)
  * [Shop Pay Wallet](https://shopify.dev/docs/api/commerce-components/pay)
  * [Storefront Web Components](https://shopify.dev/docs/api/storefront-web-components)
  * [Web Pixels API](https://shopify.dev/docs/api/web-pixels-api)
  * Any other resources not explicitly listed as versioned


* * *
## 
[Anchor to Release schedule](https://shopify.dev/docs/api/usage/versioning#release-schedule)Release schedule
Shopify releases a new API version every three months at 5pm UTC on the first day of the quarter. Version names are date-based (for example, `2026-04`). Each stable version is supported for a minimum of 12 months, with at least nine months of overlap between consecutive versions.
Version
2025202620272028
Q2Q3Q4Q1Q2Q3Q4Q1Q2Q3Q4Q1
October 26, 2026
  * UnstableIn development
  * 2027-01Release candidateRCStableUnsupported
  * 2026-10Latest stableRCStableUnsupported
  * 2026-07StableRCStableUnsupported
  * 2026-04StableRCStableUnsupported
  * 2026-01StableRCStableUnsupported
  * 2025-10UnsupportedRCStableUnsupported
  * 2025-07UnsupportedRCStableUnsupported
  * 2025-04UnsupportedStableUnsupported


For early testingFor use in developmentFor use in productionNot usable  
Shopify API release schedule  
| Stable version  | Release date  | Accessible until  | Status  |  
| --- | --- | --- | --- |  
| 2025-04  | April 1, 2025  | April 16, 2026 15:00 UTC  | Unsupported  |  
| 2025-07  | July 1, 2025  | July 16, 2026 15:00 UTC  | Unsupported  |  
| 2025-10  | October 1, 2025  | October 16, 2026 15:00 UTC  | Unsupported  |  
| 2026-01  | January 1, 2026  | January 16, 2027 15:00 UTC  | Stable  |  
| 2026-04  | April 1, 2026  | April 16, 2027 15:00 UTC  | Stable  |  
| 2026-07  | July 1, 2026  | July 16, 2027 15:00 UTC  | Stable  |  
| 2026-10  | October 1, 2026  | October 16, 2027 15:00 UTC  | Latest stable  |  
| 2027-01  | January 1, 2027  | January 16, 2028 15:00 UTC  | Release candidate  |  
We recommend updating to the latest stable version each quarter and always specifying a version in your requests. If your app targets an inaccessible version, Shopify falls forward and responds using the oldest accessible stable version. For example, a request targeting a retired `2024-10` is served by the oldest accessible stable version instead.
* * *
## 
[Anchor to Making requests to an API version](https://shopify.dev/docs/api/usage/versioning#making-requests-to-an-api-version)Making requests to an API version
You specify the API version in your request URL. The format varies by API, so refer to each API's reference for the exact URL pattern. If you're using an [official Shopify library](https://shopify.dev/docs/api/libraries-and-templates) or a [Storefront SDK](https://shopify.dev/docs/storefronts/headless/additional-sdks), version configuration is handled for you automatically.
API responses include the `X-Shopify-API-Version` header reflecting the version used to fulfill the request. If it differs from what you requested, your app is targeting an inaccessible version and Shopify has fallen forward to the default.
Shopify supports three version types:
  * **Stable:** Recommended for production. Guaranteed not to change for its supported lifetime.
  * **Release candidate:** Published on the same date as the stable release. For example, when `2026-04` releases on April 1, 2026, the `2026-07` release candidate also becomes available. May include backwards-incompatible changes, so not recommended for production.
  * **Unstable:** Updated continuously with in-progress changes. Features can be added or removed at any time with no guarantee of release. Use it for early testing only.


* * *
## 
[Anchor to Deprecation practices](https://shopify.dev/docs/api/usage/versioning#deprecation-practices)Deprecation practices
When part of a Shopify API becomes unnecessary, unsafe, or outdated, it's deprecated across all supported stable versions and announced in the [developer changelog](https://shopify.dev/changelog) with migration guidance. Deprecated fields or types are removed in a subsequent release—for example, something deprecated in `2026-10` might be removed in `2027-01`. Because versions overlap by at least nine months, you'll always have time to update before removal.
An entire API can be deprecated, not only parts of one. A deprecated API stays available but is unsupported, and it can stop working at any time, so migrate to the supported alternative as soon as one is announced.
Deprecations are communicated through one or more of the following:
  * Your app's [alerts in the Dev Dashboard](https://shopify.dev/docs/apps/build/dev-dashboard/monitoring-and-logs#alert-statuses) flag deprecated calls and the deadline for fixing them.
  * Deprecation warnings appear in API client tools like the [GraphiQL Explorer](https://shopify.dev/docs/apps/build/apis/graphql-admin/api-exploration/admin-graphiql-explorer).
  * A notice is posted in the [developer changelog](https://shopify.dev/changelog).
  * The API reference is updated with deprecated fields and alternatives.
  * For imminent backwards-incompatible changes, your app's [emergency developer contact](https://shopify.dev/docs/apps/build/dev-dashboard/technical-updates) might be notified.


Deprecated calls are attributed to the app whose access token made them, so don't use an app's access token outside the app. A support team's Postman or Insomnia collection using it raises the alert against your app.
If your app continues to use unsupported resources after the upgrade deadline, it's delisted from the Shopify App Store. Users are blocked from installing it for a minimum of seven days, and they'll see warnings in the Shopify admin until seven days after the last detected use of unsupported resources.
Warning
If your API is used in a standalone app (such as a desktop or mobile app), your users will need to update before the upgrade deadline. Ship your update early enough to give them time. Calls to unsupported resources could result in your app being delisted or users being blocked from installing it.
**Warning :**
If your API is used in a standalone app (such as a desktop or mobile app), your users will need to update before the upgrade deadline. Ship your update early enough to give them time. Calls to unsupported resources could result in your app being delisted or users being blocked from installing it.
* * *
Was this page helpful?
YesNo
  * [Versioned and unversioned APIs](https://shopify.dev/docs/api/usage/versioning#versioned-and-unversioned-apis)
  * [Release schedule](https://shopify.dev/docs/api/usage/versioning#release-schedule)
  * [Making requests to an API version](https://shopify.dev/docs/api/usage/versioning#making-requests-to-an-api-version)
  * [Deprecation practices](https://shopify.dev/docs/api/usage/versioning#deprecation-practices)


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



