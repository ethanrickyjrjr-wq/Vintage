[Skip to main content](https://shopify.dev/docs/storefronts/headless/overview#main-content)
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
  * [How headless works](https://shopify.dev/docs/storefronts/headless/overview#how-headless-works)
  * [When to build headless](https://shopify.dev/docs/storefronts/headless/overview#when-to-build-headless)
  * [The headless APIs](https://shopify.dev/docs/storefronts/headless/overview#the-headless-apis)
  * [Choose how to build](https://shopify.dev/docs/storefronts/headless/overview#choose-how-to-build)
  * [Get your keys](https://shopify.dev/docs/storefronts/headless/overview#get-your-keys)
  * [Manage your Headless storefronts](https://shopify.dev/docs/storefronts/headless/overview#manage-your-headless-storefronts)
  * [Configure routes](https://shopify.dev/docs/storefronts/headless/overview#configure-routes)
  * [Next steps](https://shopify.dev/docs/storefronts/headless/overview#next-steps)


# About headless commerce
Install AI ToolkitAsk about this pageCopy MD
Headless commerce separates your storefront's frontend from its backend. You build the frontend, and Shopify's APIs handle the commerce underneath. You can sell on a website, in a mobile app, in a game or a livestream, on a smart device, or through a buy button on a site that you already have.
* * *
## 
[Anchor to How headless works](https://shopify.dev/docs/storefronts/headless/overview#how-headless-works)How headless works
You choose the stack, framework, and hosting for your frontend. It gets its data and commerce capabilities from Shopify. Data includes [products](https://shopify.dev/docs/api/storefront/latest/objects/Product), [collections](https://shopify.dev/docs/api/storefront/latest/objects/Collection), and [customers](https://shopify.dev/docs/api/storefront/latest/objects/Customer). Commerce capabilities include the [cart](https://shopify.dev/docs/storefronts/headless/building-with-the-storefront-api/cart/manage), checkout, and [international pricing](https://shopify.dev/docs/storefronts/headless/building-with-the-storefront-api/markets/international-pricing).
![Websites, mobile apps, and social experiences get commerce primitives and capabilities from the Storefront API, which sits on top of Shopify's backend](https://shopify-assets.shopifycdn.com/shopifycloud/shopify-dev/production/assets/assets/images/custom-storefronts/how-custom-storefronts-work-mjjaTy6T.png)
Because the frontend and backend are separate, you can also connect other business systems to either side, like a content management system (CMS), customer relationship management (CRM), enterprise resource planning (ERP), or product information management (PIM) system.
* * *
## 
[Anchor to When to build headless](https://shopify.dev/docs/storefronts/headless/overview#when-to-build-headless)When to build headless
If a merchant's business systems, processes, or customer experience can't be achieved with Shopify's sales channels, [themes](https://shopify.dev/docs/storefronts/themes), and apps, then consider building headless. For example, build headless in the following cases:
  * You're building a storefront experience that existing web or mobile tools can't support, or can't support easily.
  * You have a web frontend stack that doesn't use [Liquid](https://shopify.dev/docs/api/liquid).
  * You want to add Shopify commerce to infrastructure that you already have.
  * You sell on several channels that Shopify doesn't support out of the box.
  * You use a CMS, or plan to, for content that's integrated with your storefront.


A headless storefront costs more to build and run than a theme. Before you commit, make sure that the merchant accepts the added cost and complexity, and has developers to maintain the storefront after launch.
* * *
## 
[Anchor to The headless APIs](https://shopify.dev/docs/storefronts/headless/overview#the-headless-apis)The headless APIs
Shopify offers two headless APIs:
  * The [Storefront API](https://shopify.dev/docs/api/storefront) serves products, collections, search, and the cart, and hands customers off to checkout.
  * The [Customer Account API](https://shopify.dev/docs/api/customer) lets customers sign in, and serves their orders, addresses, and profile.


To build before you have a store, use [mock.shop](https://shopify.dev/docs/storefronts/headless/mock-shop), a public Storefront API with demo data. It doesn't need a store or an access token. When you're ready to connect a real store, [get your keys](https://shopify.dev/docs/storefronts/headless/overview#get-your-keys).
* * *
## 
[Anchor to Choose how to build](https://shopify.dev/docs/storefronts/headless/overview#choose-how-to-build)Choose how to build
The options differ in how you build the storefront and call Shopify's APIs:  
| You want to  | Build with  |  
| --- | --- |  
| Build a full storefront in a JavaScript framework, like Next.js or React Router  |  [Hydrogen](https://shopify.dev/docs/storefronts/hydrogen), Shopify's headless toolkit  |  
| Sell in a native iOS, Android, or React Native app  |  [Mobile commerce](https://shopify.dev/docs/storefronts/mobile), with the Storefront API and Checkout Kit  |  
| Build everything yourself, in any language or stack, without a Shopify toolkit  |  [Bring your own stack](https://shopify.dev/docs/storefronts/headless/bring-your-own-stack), with the Storefront API and the Customer Account API called directly  |  
| Add products and buy buttons to a site that you already have  |  [Storefront Web Components](https://shopify.dev/docs/api/storefront-web-components) or [Buy Button JS](https://shopify.dev/docs/storefronts/headless/additional-sdks/buy-button)  |  
| Sell Shopify products on a WordPress site  | The [Shopify Plugin for WordPress](https://shopify.dev/docs/storefronts/headless/bring-your-own-stack/wordpress)  |  
For the full list of SDKs, refer to [Additional SDKs](https://shopify.dev/docs/storefronts/headless/additional-sdks).
* * *
## 
[Anchor to Get your keys](https://shopify.dev/docs/storefronts/headless/overview#get-your-keys)Get your keys
You get Storefront API and Customer Account API access through a sales channel in the Shopify admin. Shopify offers two channels for headless storefronts:  
| Channel  | Use it when  |  
| --- | --- |  
| [Headless](https://shopify.dev/docs/storefronts/headless/overview#the-headless-channel)  | You host the storefront yourself, on any stack. This includes mobile apps, and Hydrogen storefronts that you deploy somewhere other than Oxygen, like Vercel.  |  
| [Hydrogen](https://shopify.dev/docs/storefronts/headless/overview#the-hydrogen-channel)  | You build with Hydrogen and deploy to Oxygen, Shopify's hosting for Hydrogen storefronts.  |  
Each channel gives your storefront the following credentials:
  * Storefront API tokens: A public access token and a private access token. Use the public token for requests from a browser or mobile app, where it's visible to buyers. Use the private token for requests from your server. The private token is a secret. Never expose it in client-side code or a mobile app, and never give it a browser prefix like `NEXT_PUBLIC_`. To learn how to send each token, refer to [Storefront API authentication](https://shopify.dev/docs/api/storefront#authentication).
  * Customer Account API credentials: A client ID, and a client secret for confidential clients that run on a server. To set them up, refer to [Getting started with the Customer Account API](https://shopify.dev/docs/storefronts/headless/building-with-the-customer-account-api/getting-started).


You don't need a token for [tokenless access](https://shopify.dev/docs/api/storefront#authentication) to the Storefront API. Tokenless access covers products, collections, search, and the cart, with a query complexity limit of 1,000.
### 
[Anchor to The Headless channel](https://shopify.dev/docs/storefronts/headless/overview#the-headless-channel)The Headless channel
![Flow chart of a headless architecture built on Shopify. A developer uses the Shopify admin to control access to the Storefront API and Customer Account API. Those API resources are then rendered to display to customers.](https://shopify-assets.shopifycdn.com/shopifycloud/shopify-dev/production/assets/assets/images/custom-storefronts/headless/headless-channel-DvaOH6om.png)
The [Headless channel](https://apps.shopify.com/headless) gives you a single place to manage API access for all your client applications, without creating a custom app. Use it for any storefront that you host yourself, whatever the stack.
In the Headless channel, you can do the following tasks:
  * Create multiple storefronts. Each storefront has its own Storefront API tokens, but all storefronts in the channel share the same API permissions.
  * Get each storefront's public and private Storefront API tokens, and rotate them.
  * Configure the Customer Account API for each storefront, and get its client ID and client secret.
  * Manage which store data the Storefront API and Customer Account API can access.
  * Publish products to the Headless channel, and get order attribution, analytics, and sales reporting by channel.


To set up the channel, [install it](https://shopify.dev/docs/storefronts/headless/overview#install-the-headless-channel) and [create a storefront](https://shopify.dev/docs/storefronts/headless/overview#create-a-storefront). For more ways to manage it, like renaming storefronts and order attribution, refer to [Manage the Headless channel](https://shopify.dev/docs/storefronts/headless/building-with-the-storefront-api/manage-headless-channels).
Info
If you want to display products on an existing site or platform, then you can skip installing the Headless channel and use [Storefront Web Components](https://shopify.dev/docs/api/storefront-web-components) instead.
**Info :**
If you want to display products on an existing site or platform, then you can skip installing the Headless channel and use [Storefront Web Components](https://shopify.dev/docs/api/storefront-web-components) instead.
### 
[Anchor to The Hydrogen channel](https://shopify.dev/docs/storefronts/headless/overview#the-hydrogen-channel)The Hydrogen channel
The [Hydrogen channel](https://apps.shopify.com/hydrogen) connects Hydrogen storefronts to your store and deploys them to Oxygen. Use it when you build with Hydrogen and host on Oxygen.
In the Hydrogen channel, you can do the following tasks:
  * Create storefronts. Each storefront links to one app, and holds its environments, environment variables, and deployments.
  * Deploy to Oxygen, from GitHub or from your own CI/CD system.
  * Configure the Customer Account API in each storefront's **Storefront settings**.
  * Publish products to the Hydrogen channel.


You don't copy tokens by hand on Oxygen. When you create a storefront, Shopify adds the environment variables that your app needs, including `PRIVATE_STOREFRONT_API_TOKEN`, `PUBLIC_STOREFRONT_ID`, `PUBLIC_CUSTOMER_ACCOUNT_API_CLIENT_ID`, and `SHOP_ID`. To use the same values locally, run `npx shopify hydrogen link` and `npx shopify hydrogen env pull`.
To install the channel and create a storefront, refer to [Deploy to Oxygen](https://shopify.dev/docs/storefronts/hydrogen/deploy/oxygen). For the full list of variables and how to rotate your private token, refer to [Environments and variables](https://shopify.dev/docs/storefronts/hydrogen/deploy/oxygen/environments).
* * *
## 
[Anchor to Manage your Headless storefronts](https://shopify.dev/docs/storefronts/headless/overview#manage-your-headless-storefronts)Manage your Headless storefronts
The following tasks set up and maintain storefronts in the Headless channel. They apply to any storefront that gets its API access from the Headless channel, whatever it's built with. This includes Hydrogen storefronts that use the Headless channel, like Vercel Shop.
If you deploy a Hydrogen storefront to Oxygen, then you manage it in the Hydrogen channel instead, and these tasks don't apply. To rotate its private token, refer to [Rotate your private Storefront API token](https://shopify.dev/docs/storefronts/hydrogen/deploy/oxygen/environments#rotate-your-private-storefront-api-token).
### 
[Anchor to Install the Headless channel](https://shopify.dev/docs/storefronts/headless/overview#install-the-headless-channel)Install the Headless channel
  1. Install the [Headless channel](https://apps.shopify.com/headless) from the Shopify App Store.
  2. On installation, click **Create storefront** to generate your first storefront's public and private access tokens.


### 
[Anchor to Create a storefront](https://shopify.dev/docs/storefronts/headless/overview#create-a-storefront)Create a storefront
You can create multiple storefronts in the Headless channel. Each storefront has its own set of API tokens, but all storefronts in the Headless channel share the same API permissions.
  1. From your Shopify admin, under **Sales channels** , click **Headless**.
  2. Click **Add storefront**.
  3. Optional: On the storefront detail page, click **Rename** to edit the storefront's default name.


### 
[Anchor to Manage API permissions](https://shopify.dev/docs/storefronts/headless/overview#manage-api-permissions)Manage API permissions
You can control which store data is available through the Storefront API and the Customer Account API. All storefronts in the Headless channel share the same API permissions.
  1. From your Shopify admin, under **Sales channels** , click **Headless**.
  2. Click the name of the storefront that you want to update.
  3. Under **Manage API access** , click **Manage** for the API that you want to update.
  4. Under **Permissions** , click the edit icon.
  5. Check the permission scopes that you want enabled.
  6. Click **Save**.


### 
[Anchor to Rotate API credentials](https://shopify.dev/docs/storefronts/headless/overview#rotate-api-credentials)Rotate API credentials
For security purposes, you can update your API credentials at any time. Rotate them right away if a private token or client secret is exposed.
  1. From your Shopify admin, under **Sales channels** , click **Headless**.
  2. Click the name of the storefront to update.
  3. Under **Manage API access** , click **Manage** for the API that you want to update.
  4. Under **Rotate credentials** , click **Generate new token**. Both the old and new credentials are valid until you delete the old credentials.
  5. Update your client apps with the new credentials.
     * The Storefront API uses an access token.
     * The Customer Account API uses a client ID, and might also use a client secret, depending on the type of access.
  6. After you've updated your apps, delete the old credentials by clicking **Revoke**.


### 
[Anchor to Delete a storefront](https://shopify.dev/docs/storefronts/headless/overview#delete-a-storefront)Delete a storefront
Deleting a storefront in the Headless channel revokes all its access tokens. You need to update any clients that use those tokens.
  1. From your Shopify admin, under **Sales channels** , click **Headless**.
  2. Click the name of the storefront that you want to delete.
  3. Click **Delete storefront**.
  4. To confirm, click **Delete storefront**.


* * *
## 
[Anchor to Configure routes](https://shopify.dev/docs/storefronts/headless/overview#configure-routes)Configure routes
The standard format for product URLs is `/products/:handle`. If your storefront uses a different structure, then provide a server-side redirect (3XX) from the expected `/products/:handle` path to the product page.
Your storefront should also support [cart permalinks](https://help.shopify.com/en/manual/checkout-settings/cart-permalink). For an example, refer to this [cart permalink route](https://github.com/Shopify/hydrogen-demo-store/blob/b19212adc431c9ee3c510f022ee994bb5d24b0df/app/routes/\(%24locale\).cart.%24lines.tsx). Hydrogen handles cart permalinks for you with its [request handlers](https://shopify.dev/docs/storefronts/hydrogen/request-handlers).
* * *
## 
[Anchor to Next steps](https://shopify.dev/docs/storefronts/headless/overview#next-steps)Next steps
[ ![](https://shopify-assets.shopifycdn.com/shopifycloud/shopify-dev/production/assets/assets/images/icons/48/hydrogen-3-B2fOSrOp.png)![](https://shopify-assets.shopifycdn.com/shopifycloud/shopify-dev/production/assets/assets/images/icons/48/hydrogen-3-B2fOSrOp.png) HydrogenBuild a full storefront with Shopify's headless toolkit. Hydrogen Build a full storefront with Shopify's headless toolkit. ](https://shopify.dev/docs/storefronts/hydrogen)
[Hydrogen  
  
Build a full storefront with Shopify's headless toolkit.](https://shopify.dev/docs/storefronts/hydrogen)
[ ![](https://shopify-assets.shopifycdn.com/shopifycloud/shopify-dev/production/assets/assets/images/icons/48/app-B9pr02rY.png)![](https://shopify-assets.shopifycdn.com/shopifycloud/shopify-dev/production/assets/assets/images/icons/48/app-dark-D3_H1074.png) Mobile commerceBuild iOS, Android, and React Native apps with the Storefront API and Checkout Kit. Mobile commerce Build iOS, Android, and React Native apps with the Storefront API and Checkout Kit. ](https://shopify.dev/docs/storefronts/mobile)
[Mobile commerce  
  
Build iOS, Android, and React Native apps with the Storefront API and Checkout Kit.](https://shopify.dev/docs/storefronts/mobile)
[ ![](https://shopify-assets.shopifycdn.com/shopifycloud/shopify-dev/production/assets/assets/images/icons/48/custom-storefronts-CXVa75uA.png)![](https://shopify-assets.shopifycdn.com/shopifycloud/shopify-dev/production/assets/assets/images/icons/48/custom-storefronts-dark-CC4sWpPm.png) Bring your own stackCall the Storefront API and Customer Account API directly from any stack. Bring your own stack Call the Storefront API and Customer Account API directly from any stack. ](https://shopify.dev/docs/storefronts/headless/bring-your-own-stack)
[Bring your own stack  
  
Call the Storefront API and Customer Account API directly from any stack.](https://shopify.dev/docs/storefronts/headless/bring-your-own-stack)
[ ![](https://shopify-assets.shopifycdn.com/shopifycloud/shopify-dev/production/assets/assets/images/icons/32/shop-DV7EB4UW.png)![](https://shopify-assets.shopifycdn.com/shopifycloud/shopify-dev/production/assets/assets/images/icons/32/shop-DV7EB4UW.png) Build with mock.shopBuild and test against demo data before you connect a store. Build with mock.shop Build and test against demo data before you connect a store. ](https://shopify.dev/docs/storefronts/headless/mock-shop)
[Build with mock.shop  
  
Build and test against demo data before you connect a store.](https://shopify.dev/docs/storefronts/headless/mock-shop)
* * *
Was this page helpful?
YesNo
  * [How headless works](https://shopify.dev/docs/storefronts/headless/overview#how-headless-works)
  * [When to build headless](https://shopify.dev/docs/storefronts/headless/overview#when-to-build-headless)
  * [The headless APIs](https://shopify.dev/docs/storefronts/headless/overview#the-headless-apis)
  * [Choose how to build](https://shopify.dev/docs/storefronts/headless/overview#choose-how-to-build)
  * [Get your keys](https://shopify.dev/docs/storefronts/headless/overview#get-your-keys)
  * [Manage your Headless storefronts](https://shopify.dev/docs/storefronts/headless/overview#manage-your-headless-storefronts)
  * [Configure routes](https://shopify.dev/docs/storefronts/headless/overview#configure-routes)
  * [Next steps](https://shopify.dev/docs/storefronts/headless/overview#next-steps)


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



