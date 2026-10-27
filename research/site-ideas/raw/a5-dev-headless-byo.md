[Skip to main content](https://shopify.dev/docs/storefronts/headless/bring-your-own-stack#main-content)
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
  * [The APIs](https://shopify.dev/docs/storefronts/headless/bring-your-own-stack#the-apis)
  * [SDKs and integrations](https://shopify.dev/docs/storefronts/headless/bring-your-own-stack#sdks-and-integrations)
  * [Get your keys](https://shopify.dev/docs/storefronts/headless/bring-your-own-stack#get-your-keys)
  * [Next steps](https://shopify.dev/docs/storefronts/headless/bring-your-own-stack#next-steps)


# Bring your own headless stack
Install AI ToolkitAsk about this pageCopy MD
Shopify's headless APIs work with nearly any technology stack. You choose the language, framework, hosting, and workflows, and call Shopify's APIs directly without a Shopify toolkit.
If you want a JavaScript toolkit that handles the cart, variant selection, and other Shopify-specific logic for you, then refer to [Hydrogen](https://shopify.dev/docs/storefronts/hydrogen) instead.
* * *
## 
[Anchor to The APIs](https://shopify.dev/docs/storefronts/headless/bring-your-own-stack#the-apis)The APIs
Your storefront gets its data and commerce capabilities from two GraphQL APIs:
  * The [Storefront API](https://shopify.dev/docs/storefronts/headless/building-with-the-storefront-api) serves products, collections, search, markets, and the cart, and hands customers off to checkout.
  * The [Customer Account API](https://shopify.dev/docs/storefronts/headless/building-with-the-customer-account-api) lets customers sign in, and serves their orders, addresses, and profile.


You can call both APIs from any HTTP client. To build before you have a store, use [mock.shop](https://shopify.dev/docs/storefronts/headless/mock-shop), a public Storefront API with demo data.
* * *
## 
[Anchor to SDKs and integrations](https://shopify.dev/docs/storefronts/headless/bring-your-own-stack#sdks-and-integrations)SDKs and integrations
Shopify provides tools that you can use on top of the APIs:
  * [Additional SDKs](https://shopify.dev/docs/storefronts/headless/additional-sdks) include the Storefront API Client, Buy Button JS, and the JS Buy SDK for the web, and client libraries for Node.js, PHP, and Ruby on the server.
  * [Storefront Web Components](https://shopify.dev/docs/api/storefront-web-components) add products, carts, and checkout to any HTML page.
  * The [Shopify Plugin for WordPress](https://shopify.dev/docs/storefronts/headless/bring-your-own-stack/wordpress) displays products and collections from a Shopify store on a WordPress site.
  * [Headless with B2B](https://shopify.dev/docs/storefronts/headless/bring-your-own-stack/b2b) shows how to get B2B pricing, volume pricing, and quantity rules into your storefront queries and cart.


* * *
## 
[Anchor to Get your keys](https://shopify.dev/docs/storefronts/headless/bring-your-own-stack#get-your-keys)Get your keys
To connect a real store, install the Headless channel and create a storefront. The channel gives you Storefront API tokens and Customer Account API credentials, and lets you manage permissions and rotate credentials. Refer to [Get your keys](https://shopify.dev/docs/storefronts/headless/overview#get-your-keys).
* * *
## 
[Anchor to Next steps](https://shopify.dev/docs/storefronts/headless/bring-your-own-stack#next-steps)Next steps
[ ![](https://shopify-assets.shopifycdn.com/shopifycloud/shopify-dev/production/assets/assets/images/icons/48/graphql-BcmzB7oU.png)![](https://shopify-assets.shopifycdn.com/shopifycloud/shopify-dev/production/assets/assets/images/icons/48/graphql-dark-BWvwojby.png) Storefront APIQuery products and collections, and manage carts. Storefront API Query products and collections, and manage carts. ](https://shopify.dev/docs/storefronts/headless/building-with-the-storefront-api)
[Storefront API  
  
Query products and collections, and manage carts.](https://shopify.dev/docs/storefronts/headless/building-with-the-storefront-api)
[ ![](https://shopify-assets.shopifycdn.com/shopifycloud/shopify-dev/production/assets/assets/images/icons/48/key-DmNsZZzb.png)![](https://shopify-assets.shopifycdn.com/shopifycloud/shopify-dev/production/assets/assets/images/icons/48/key-DmNsZZzb.png) Customer Account APISign customers in, and show their orders and profile. Customer Account API Sign customers in, and show their orders and profile. ](https://shopify.dev/docs/storefronts/headless/building-with-the-customer-account-api)
[Customer Account API  
  
Sign customers in, and show their orders and profile.](https://shopify.dev/docs/storefronts/headless/building-with-the-customer-account-api)
[ ![](https://shopify-assets.shopifycdn.com/shopifycloud/shopify-dev/production/assets/assets/images/icons/32/shop-DV7EB4UW.png)![](https://shopify-assets.shopifycdn.com/shopifycloud/shopify-dev/production/assets/assets/images/icons/32/shop-DV7EB4UW.png) Headless with B2BBuild a dedicated or blended B2B storefront. Headless with B2B Build a dedicated or blended B2B storefront. ](https://shopify.dev/docs/storefronts/headless/bring-your-own-stack/b2b)
[Headless with B2B  
  
Build a dedicated or blended B2B storefront.](https://shopify.dev/docs/storefronts/headless/bring-your-own-stack/b2b)
[ ![](https://shopify-assets.shopifycdn.com/shopifycloud/shopify-dev/production/assets/assets/images/icons/64/integrations-CWeHaNwg.png)![](https://shopify-assets.shopifycdn.com/shopifycloud/shopify-dev/production/assets/assets/images/icons/64/integrations-dark-CX0b9PH2.png) Shopify Plugin for WordPressSell Shopify products on a WordPress site. Shopify Plugin for WordPress Sell Shopify products on a WordPress site. ](https://shopify.dev/docs/storefronts/headless/bring-your-own-stack/wordpress)
[Shopify Plugin for WordPress  
  
Sell Shopify products on a WordPress site.](https://shopify.dev/docs/storefronts/headless/bring-your-own-stack/wordpress)
[ ![](https://shopify-assets.shopifycdn.com/shopifycloud/shopify-dev/production/assets/assets/images/icons/48/blocks-DRGfrRdn.png)![](https://shopify-assets.shopifycdn.com/shopifycloud/shopify-dev/production/assets/assets/images/icons/48/blocks-dark-CZsU7rPs.png) Storefront Web ComponentsEmbed products, carts, and checkout in any HTML page. Storefront Web Components Embed products, carts, and checkout in any HTML page. ](https://shopify.dev/docs/api/storefront-web-components)
[Storefront Web Components  
  
Embed products, carts, and checkout in any HTML page.](https://shopify.dev/docs/api/storefront-web-components)
[ ![](https://shopify-assets.shopifycdn.com/shopifycloud/shopify-dev/production/assets/assets/images/icons/48/github-ByuPTTJu.png)![](https://shopify-assets.shopifycdn.com/shopifycloud/shopify-dev/production/assets/assets/images/icons/48/github-dark-CoaNuIDT.png) Additional SDKsUse Shopify's web and backend libraries in your stack. Additional SDKs Use Shopify's web and backend libraries in your stack. ](https://shopify.dev/docs/storefronts/headless/additional-sdks)
[Additional SDKs  
  
Use Shopify's web and backend libraries in your stack.](https://shopify.dev/docs/storefronts/headless/additional-sdks)
* * *
Was this page helpful?
YesNo
  * [The APIs](https://shopify.dev/docs/storefronts/headless/bring-your-own-stack#the-apis)
  * [SDKs and integrations](https://shopify.dev/docs/storefronts/headless/bring-your-own-stack#sdks-and-integrations)
  * [Get your keys](https://shopify.dev/docs/storefronts/headless/bring-your-own-stack#get-your-keys)
  * [Next steps](https://shopify.dev/docs/storefronts/headless/bring-your-own-stack#next-steps)


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



