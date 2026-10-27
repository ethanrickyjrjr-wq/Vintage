[Skip to main content](https://shopify.dev/docs/storefronts/headless/building-with-the-storefront-api#main-content)
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
Storefronts
  * [Overview](https://shopify.dev/docs/storefronts)


* * *
  * ### Themes
    * [Overview](https://shopify.dev/docs/storefronts/themes)
    * Getting started
    * Key concepts
    * Best practices
    * Agentic workflows
    * Developer Tools
    * Theme features
    * Sell themes
  * ### Headless
    * [Overview](https://shopify.dev/docs/storefronts/headless/overview)
    * [Building with mock.shop ](https://shopify.dev/docs/storefronts/headless/mock-shop)
  * ### Hydrogen
    * [Overview](https://shopify.dev/docs/storefronts/hydrogen)
    * Getting started
    * Data fetching
    * Request handling
    * Products and collections
    * Cart
    * [Customer accounts](https://shopify.dev/docs/storefronts/hydrogen/customer-accounts)
    * [Markets](https://shopify.dev/docs/storefronts/hydrogen/markets)
    * [Analytics and consent](https://shopify.dev/docs/storefronts/hydrogen/analytics)
    * Deploy
    * [Hydrogen CLI commands](https://shopify.dev/docs/api/shopify-cli/hydrogen)
    * [Hydrogen API reference](https://shopify.dev/docs/api/hydrogen)
    * [Migrate to the latest version of Hydrogen](https://shopify.dev/docs/storefronts/hydrogen/migrate)
    * Legacy Hydrogen
  * ### Mobile
    * [Overview](https://shopify.dev/docs/storefronts/mobile)
    * Checkout Kit
    * Accelerated checkouts
    * Mobile storefronts
  * ### Bring your own stack
    * [Overview](https://shopify.dev/docs/storefronts/headless/bring-your-own-stack)
    * Building with the Storefront API
    * Building with the Customer Account API
    * [Headless with B2B](https://shopify.dev/docs/storefronts/headless/bring-your-own-stack/b2b)
    * Shopify Plugin for WordPress
    * [Storefront Web Components](https://shopify.dev/docs/api/storefront-web-components)
    * Additional SDKs


Full index
ExpandOn this page
  * [What is the Storefront API?](https://shopify.dev/docs/storefronts/headless/building-with-the-storefront-api#what-is-the-storefront-api)
  * [When to use the Storefront API](https://shopify.dev/docs/storefronts/headless/building-with-the-storefront-api#when-to-use-the-storefront-api)
  * [API versioning](https://shopify.dev/docs/storefronts/headless/building-with-the-storefront-api#api-versioning)
  * [Authentication and authorization](https://shopify.dev/docs/storefronts/headless/building-with-the-storefront-api#authentication-and-authorization)
  * [What is the Headless channel?](https://shopify.dev/docs/storefronts/headless/building-with-the-storefront-api#what-is-the-headless-channel)
  * [Reference](https://shopify.dev/docs/storefronts/headless/building-with-the-storefront-api#reference)
  * [Developer tools](https://shopify.dev/docs/storefronts/headless/building-with-the-storefront-api#developer-tools)
  * [Limitations](https://shopify.dev/docs/storefronts/headless/building-with-the-storefront-api#limitations)
  * [Next steps](https://shopify.dev/docs/storefronts/headless/building-with-the-storefront-api#next-steps)


# Building with the Storefront API
Install AI ToolkitAsk about this pageCopy MD
The Storefront API is the foundational layer of custom storefronts. It provides you the commerce primitives to build custom, scalable, and performant shopping experiences
* * *
## 
[Anchor to What is the Storefront API?](https://shopify.dev/docs/storefronts/headless/building-with-the-storefront-api#what-is-the-storefront-api)What is the Storefront API?
The Storefront API provides access to Shopify's primitives and capabilities such as displaying products and collections, adding items to the cart, calculating contextual pricing, and more.
You can use the Storefront API to build unique commerce experiences on any platform, including the web, native apps, games, and social media, using the frontend tools of your choice.
![The Storefront API's function as layer between Shopify's backend and its commerce primitives, and customer touchpoints such as mobile, social media, and web](https://shopify-assets.shopifycdn.com/shopifycloud/shopify-dev/production/assets/assets/images/custom-storefronts/storefront-api/how-does-sfapi-work-C9V36b8L.png)
* * *
## 
[Anchor to When to use the Storefront API](https://shopify.dev/docs/storefronts/headless/building-with-the-storefront-api#when-to-use-the-storefront-api)When to use the Storefront API
The Storefront API helps you create a seamless and engaging shopping experience for your customers by leveraging the robust commerce functionality of Shopify. Headless builds are made efficient and performant with the following resources:
  * **Built-in commerce essentials** : Leverage the full power of the Shopify admin to manage your back-office products like pricing, inventory, and metafields. Use the Storefront API to deliver performant buyer experiences with optimized cart, contextual pricing, subscriptions, and more.
  * **Operate at a global scale** : Backed by the infrastructure that supports over 2 million Shopify businesses, build your custom storefront on the platform that's fast, flexible, and feature-rich.
  * **Build your way** : Bring your own tech stack, requirements, and experience. Build on top of Shopify's proven Storefront API that serves 1M+ queries per minute.
  * [**Developer tools**](https://shopify.dev/docs/storefronts/headless/building-with-the-storefront-api#developer-tools): Improve your developer experience by helping you learn about the API.
Because the Storefront API uses the Shopify backend, you can focus on building a unique and customized shopping experience with strong brand representation. You can create custom pages, themes, and order management experiences that are fully integrated with a storefront.


* * *
## 
[Anchor to API versioning](https://shopify.dev/docs/storefronts/headless/building-with-the-storefront-api#api-versioning)API versioning
The Storefront API is [versioned](https://shopify.dev/docs/api/usage/versioning), with new releases four times a year. We strongly recommend updating your apps to make requests to the latest stable API version every quarter. However, if your app uses a stable version that is no longer supported, then Shopify falls forward and responds to your request with the same behavior as the oldest supported stable version.
* * *
## 
[Anchor to Authentication and authorization](https://shopify.dev/docs/storefronts/headless/building-with-the-storefront-api#authentication-and-authorization)Authentication and authorization
The Storefront API supports both tokenless access and token-based authentication.
### 
[Anchor to Tokenless access](https://shopify.dev/docs/storefronts/headless/building-with-the-storefront-api#tokenless-access)Tokenless access
Tokenless access allows API queries without an access token providing access to essential features such as:
  * Products and Collections
  * Selling Plans
  * Search
  * Pages, Blogs, and Articles
  * Cart (read/write)
Tokenless access has a query complexity limit of 1,000. Query complexity is calculated based on the cost of each field in the query.


### 
[Anchor to Token-based authentication](https://shopify.dev/docs/storefronts/headless/building-with-the-storefront-api#token-based-authentication)Token-based authentication
For access to all Storefront API features, an access token is required. The following features require token-based authentication:
  * Product Tags
  * Metaobjects and Metafields
  * Menu (Online Store navigation)
  * Customers
The Storefront API has the following types of token-based access:
**Public Authentication** : The public token is used for client side queries and mutations. As every buyer has a different IP, the token scales to support large amounts of traffic.
**Private Access** : The private token provides authenticated access to the Storefront API and is used for server-side queries and mutations.


Caution
Unlike public access tokens, private access tokens should be treated as secret and not used on the client-side. We recommend only requesting the scopes that your app needs, to reduce the security risk if the token leaks.
**Caution :**
Unlike public access tokens, private access tokens should be treated as secret and not used on the client-side. We recommend only requesting the scopes that your app needs, to reduce the security risk if the token leaks.
Learn more about [authentication](https://shopify.dev/docs/api/usage/authentication).
* * *
## 
[Anchor to What is the Headless channel?](https://shopify.dev/docs/storefronts/headless/building-with-the-storefront-api#what-is-the-headless-channel)What is the Headless channel?
Make headless and self-hosted Hydrogen experiences possible in the Headless channel without needing to create a custom app.
The Headless channel provides a single place to create and manage access tokens for the [Storefront API](https://shopify.dev/docs/api/storefront). You can use the channel to create multiple custom storefronts. Storefronts that you create through the channel automatically include public and private access tokens with shop permission for the Storefront API. In the channel, you can rotate your private access token and manage storefront permissions.
Additionally, the channel gives you all of Shopify's channel features, such as product publishing and order attribution, and analytics and reporting sales by channel. 
Order attribution is at the channel level, and a Headless storefront is treated as a channel.
![An image of a developer installing the Headless channel. The channel provides public and private access tokens, options to manage storefront permissions, and tools for order attribution. Requests to the API for storefront data can be made from public and private contexts. The data is sent to the storefront, which serves data and passes back data such as what is used for attributing orders to the channel](https://shopify-assets.shopifycdn.com/shopifycloud/shopify-dev/production/assets/assets/images/custom-storefronts/storefront-api/headless-channel-b70XV1OD.png)
[Get started with the Headless channel](https://shopify.dev/docs/storefronts/headless/building-with-the-storefront-api/getting-started).
* * *
## 
[Anchor to Reference](https://shopify.dev/docs/storefronts/headless/building-with-the-storefront-api#reference)Reference
[ ![](https://shopify-assets.shopifycdn.com/shopifycloud/shopify-dev/production/assets/assets/images/icons/48/graphql-BcmzB7oU.png)![](https://shopify-assets.shopifycdn.com/shopifycloud/shopify-dev/production/assets/assets/images/icons/48/graphql-dark-BWvwojby.png) Storefront API referenceConsult the Storefront API reference for available objects, queries, and mutations. Storefront API reference Consult the Storefront API reference for available objects, queries, and mutations. ](https://shopify.dev/docs/api/storefront)
[Storefront API reference  
  
Consult the Storefront API reference for available objects, queries, and mutations.](https://shopify.dev/docs/api/storefront)
* * *
## 
[Anchor to Developer tools](https://shopify.dev/docs/storefronts/headless/building-with-the-storefront-api#developer-tools)Developer tools
Shopify provides tools to help you learn how to use the Storefront API.
[ ![](https://shopify-assets.shopifycdn.com/shopifycloud/shopify-dev/production/assets/assets/images/icons/48/graphql-BcmzB7oU.png)![](https://shopify-assets.shopifycdn.com/shopifycloud/shopify-dev/production/assets/assets/images/icons/48/graphql-dark-BWvwojby.png) Storefront API GraphiQL explorerUse the interactive GraphiQL explorer for the Storefront API on a demo shop. Storefront API GraphiQL explorer Use the interactive GraphiQL explorer for the Storefront API on a demo shop. ](https://shopify.dev/docs/storefronts/headless/building-with-the-storefront-api/api-exploration/graphiql-storefront-api)
[Storefront API GraphiQL explorer  
  
Use the interactive GraphiQL explorer for the Storefront API on a demo shop.](https://shopify.dev/docs/storefronts/headless/building-with-the-storefront-api/api-exploration/graphiql-storefront-api)
[ ![](https://shopify-assets.shopifycdn.com/shopifycloud/shopify-dev/production/assets/assets/images/icons/48/growth-YOTHrksj.png)![](https://shopify-assets.shopifycdn.com/shopifycloud/shopify-dev/production/assets/assets/images/icons/48/growth-dark-JWRn0vX8.png) Storefront API learning kitA downloadable package of a complete set of sample GraphQL queries to the Storefront API Storefront API learning kit A downloadable package of a complete set of sample GraphQL queries to the Storefront API ](https://github.com/Shopify/storefront-api-learning-kit)
[Storefront API learning kit  
  
A downloadable package of a complete set of sample GraphQL queries to the Storefront API](https://github.com/Shopify/storefront-api-learning-kit)
* * *
## 
[Anchor to Limitations](https://shopify.dev/docs/storefronts/headless/building-with-the-storefront-api#limitations)Limitations
  * You can have a maximum of 100 active storefronts and access tokens per shop.


* * *
## 
[Anchor to Next steps](https://shopify.dev/docs/storefronts/headless/building-with-the-storefront-api#next-steps)Next steps
  * [Get started](https://shopify.dev/docs/storefronts/headless/building-with-the-storefront-api/getting-started) building headless with the Storefront API and start querying data.


* * *
Was this page helpful?
YesNo
  * [What is the Storefront API?](https://shopify.dev/docs/storefronts/headless/building-with-the-storefront-api#what-is-the-storefront-api)
  * [When to use the Storefront API](https://shopify.dev/docs/storefronts/headless/building-with-the-storefront-api#when-to-use-the-storefront-api)
  * [API versioning](https://shopify.dev/docs/storefronts/headless/building-with-the-storefront-api#api-versioning)
  * [Authentication and authorization](https://shopify.dev/docs/storefronts/headless/building-with-the-storefront-api#authentication-and-authorization)
  * [What is the Headless channel?](https://shopify.dev/docs/storefronts/headless/building-with-the-storefront-api#what-is-the-headless-channel)
  * [Reference](https://shopify.dev/docs/storefronts/headless/building-with-the-storefront-api#reference)
  * [Developer tools](https://shopify.dev/docs/storefronts/headless/building-with-the-storefront-api#developer-tools)
  * [Limitations](https://shopify.dev/docs/storefronts/headless/building-with-the-storefront-api#limitations)
  * [Next steps](https://shopify.dev/docs/storefronts/headless/building-with-the-storefront-api#next-steps)


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



