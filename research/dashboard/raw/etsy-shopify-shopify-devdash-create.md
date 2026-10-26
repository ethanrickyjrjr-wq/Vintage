[Skip to main content](https://shopify.dev/docs/apps/build/dev-dashboard/create-apps-using-dev-dashboard#main-content)
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


Expand sidebar
Apps
  * [Overview](https://shopify.dev/docs/apps/build)


* * *
  * ### Building and deploying apps
    * [Scaffold an app](https://shopify.dev/docs/apps/build/scaffold-app)
    * [Build an app](https://shopify.dev/docs/apps/build/build)
    * Deployment
    * Distribution
  * ### Dev tools
    * [Shopify AI Toolkit](https://shopify.dev/docs/apps/build/ai-toolkit)
    * Shopify CLI
    * Dev Dashboard
      * [Overview](https://shopify.dev/docs/apps/build/dev-dashboard)
      * Apps
      * Stores
      * [Create saved catalogs](https://shopify.dev/docs/apps/build/dev-dashboard/catalogs)
      * [Configure user permissions](https://shopify.dev/docs/apps/build/dev-dashboard/user-permissions)
      * [Get technical updates](https://shopify.dev/docs/apps/build/dev-dashboard/technical-updates)
      * [Migrate from the Partner Dashboard](https://shopify.dev/docs/apps/build/dev-dashboard/migrate-from-partners)
  * ### Building blocks
    * APIs
    * Authentication
    * Custom data
    * Events and webhooks
    * Extensions
    * Functions
  * ### Design and quality
    * Design guidelines
    * Security
    * App performance
    * Built for Shopify
  * ### App surfaces
    * Admin
    * App Home
    * Checkout
    * Customer accounts
    * Online store
    * Point of Sale
  * ### Use cases
    * AI and agents
    * Analytics
    * B2B
    * Flow
    * Global markets
    * Inventory management
    * Marketing and web pixels
    * Orders and fulfillment
    * Payments
    * Products and pricing
    * Sales channels
  * ### Selling and growing your app
    * Shopify App Store
    * Billing
    * Marketing and growth


Full index
ExpandOn this page
  * [What you'll learn](https://shopify.dev/docs/apps/build/dev-dashboard/create-apps-using-dev-dashboard#what-youll-learn)
  * [Requirements](https://shopify.dev/docs/apps/build/dev-dashboard/create-apps-using-dev-dashboard#requirements)
  * [Step 1: Create a new app](https://shopify.dev/docs/apps/build/dev-dashboard/create-apps-using-dev-dashboard#step-1-create-a-new-app)
  * [Step 2: Create a version](https://shopify.dev/docs/apps/build/dev-dashboard/create-apps-using-dev-dashboard#step-2-create-a-version)
  * [Step 3: Install your app](https://shopify.dev/docs/apps/build/dev-dashboard/create-apps-using-dev-dashboard#step-3-install-your-app)
  * [Step 4: Authenticate your app](https://shopify.dev/docs/apps/build/dev-dashboard/create-apps-using-dev-dashboard#step-4-authenticate-your-app)
  * [Next steps](https://shopify.dev/docs/apps/build/dev-dashboard/create-apps-using-dev-dashboard#next-steps)


# Create apps using the Dev Dashboard
Install AI ToolkitAsk about this pageCopy MD
The Dev Dashboard provides a simplified interface for creating apps and integrating them with the Shopify admin. This makes it the best choice for quick integrations, such as connecting an existing system to Shopify.
Info
Creating an app for the app store? [Build using Shopify CLI instead](https://shopify.dev/docs/apps/build/cli-for-apps).
**Info :**
Creating an app for the app store? [Build using Shopify CLI instead](https://shopify.dev/docs/apps/build/cli-for-apps).
* * *
## 
[Anchor to What you'll learn](https://shopify.dev/docs/apps/build/dev-dashboard/create-apps-using-dev-dashboard#what-youll-learn)What you'll learn
In this tutorial, you'll learn how to do the following tasks:
  * Create and configure a new app using the Dev Dashboard
  * Install your app on a dev store
  * Authenticate your app to make API requests


* * *
## 
[Anchor to Requirements](https://shopify.dev/docs/apps/build/dev-dashboard/create-apps-using-dev-dashboard#requirements)Requirements
  * You're a [user with app development permissions](https://shopify.dev/docs/apps/build/dev-dashboard/user-permissions).


* * *
## 
[Anchor to Step 1: Create a new app](https://shopify.dev/docs/apps/build/dev-dashboard/create-apps-using-dev-dashboard#step-1-create-a-new-app)Step 1: Create a new app
You can create a new Shopify app right from your [Dev Dashboard](https://dev.shopify.com/dashboard/).
  1. From the Dev Dashboard, be sure you're on **Apps** in the left-panel navigation and select **Create app** in the top, right corner of the screen.
  2. Select **Start from Dev Dashboard**.
  3. Name your app, then select **Create**.


* * *
## 
[Anchor to Step 2: Create a version](https://shopify.dev/docs/apps/build/dev-dashboard/create-apps-using-dev-dashboard#step-2-create-a-version)Step 2: Create a version
Once you've created the app, you can create a version. A version is a snapshot of your app's current configuration, URLs, and settings. Your app must have at least one version before it can be installed on a store.
From the **Versions** page of your app in the Dev Dashboard, fill in the fields your app needs:
  * **App URL** : Where Shopify loads your app. If your app isn't embedded in the Shopify admin, you can use the default `https://shopify.dev/apps/default-app-home`.
  * **Webhooks API version** : Typically the newest version.
  * **Scopes** : The data and features your app can access. Access to protected customer data or other sensitive information [requires approval](https://shopify.dev/docs/apps/launch/protected-customer-data#request-access-to-protected-customer-data). Refer to [access scopes](https://shopify.dev/docs/apps/build/cli-for-apps/app-configuration#access_scopes).


Then select **Release**.
![An app's Versions page in the Dev Dashboard, listing each version by date with the active one badged and a Create version button.](https://shopify-assets.shopifycdn.com/shopifycloud/shopify-dev/production/assets/assets/images/apps/dev-dashboard/app-versions-17NSSy8u.png)
Versions enable you to track changes to your app configuration over time and roll back to previous configurations if needed.
When you update scopes in a new version of your app, updates aren't applied automatically to the stores your app is installed on. Merchants still need to manually approve the new scopes in the Shopify admin.
* * *
## 
[Anchor to Step 3: Install your app](https://shopify.dev/docs/apps/build/dev-dashboard/create-apps-using-dev-dashboard#step-3-install-your-app)Step 3: Install your app
Complete the following steps to install your app on a store:
  1. Open your app and select **Install app** , at the top of the **Installs** card. The same action is in the three-dot menu (**⋯**) on the app's row in the **Apps** list.
  2. The install link opens the OAuth flow in a new tab. Select or create the store for your app.
  3. Select **Install**.


Your app is now installed. To start making API calls, you'll need to authenticate your app as described in the next step.
* * *
## 
[Anchor to Step 4: Authenticate your app](https://shopify.dev/docs/apps/build/dev-dashboard/create-apps-using-dev-dashboard#step-4-authenticate-your-app)Step 4: Authenticate your app
To make API requests, your app needs an access token. If your app is only used by stores in your own organization, you can use the client credentials grant:
  1. From your app in the Dev Dashboard, select **App settings**.
  2. Copy your **Client ID** and **Client secret**.
  3. Use these credentials to programmatically request an access token from Shopify's OAuth endpoint. Tokens expire after 24 hours, so your code can request a new one when needed.


![The Credentials card in an app's settings, showing the client ID and a hidden client secret with the date the credentials were created.](https://shopify-assets.shopifycdn.com/shopifycloud/shopify-dev/production/assets/assets/images/apps/dev-dashboard/app-credentials-DJT24KRg.png)
For code examples, response details, and troubleshooting, see [Authenticate an app for stores in your organization](https://shopify.dev/docs/apps/build/authentication-authorization/client-credentials-grant).
Info
If you're building with [Shopify CLI](https://shopify.dev/docs/apps/build/cli-for-apps), authentication is handled automatically.
**Info :**
If you're building with [Shopify CLI](https://shopify.dev/docs/apps/build/cli-for-apps), authentication is handled automatically.
* * *
## 
[Anchor to Next steps](https://shopify.dev/docs/apps/build/dev-dashboard/create-apps-using-dev-dashboard#next-steps)Next steps
  * Start building with the [GraphQL Admin API](https://shopify.dev/docs/api/admin-graphql) to read and write store data.
  * Configure [Events and webhooks](https://shopify.dev/docs/apps/build/events-webhooks) to receive real-time notifications about changes in the stores your app is installed on.
  * Use the Dev Dashboard to [monitor your app's performance](https://shopify.dev/docs/apps/build/dev-dashboard/monitoring-and-logs) once merchants are using it.


* * *
Was this page helpful?
YesNo
  * [What you'll learn](https://shopify.dev/docs/apps/build/dev-dashboard/create-apps-using-dev-dashboard#what-youll-learn)
  * [Requirements](https://shopify.dev/docs/apps/build/dev-dashboard/create-apps-using-dev-dashboard#requirements)
  * [Step 1: Create a new app](https://shopify.dev/docs/apps/build/dev-dashboard/create-apps-using-dev-dashboard#step-1-create-a-new-app)
  * [Step 2: Create a version](https://shopify.dev/docs/apps/build/dev-dashboard/create-apps-using-dev-dashboard#step-2-create-a-version)
  * [Step 3: Install your app](https://shopify.dev/docs/apps/build/dev-dashboard/create-apps-using-dev-dashboard#step-3-install-your-app)
  * [Step 4: Authenticate your app](https://shopify.dev/docs/apps/build/dev-dashboard/create-apps-using-dev-dashboard#step-4-authenticate-your-app)
  * [Next steps](https://shopify.dev/docs/apps/build/dev-dashboard/create-apps-using-dev-dashboard#next-steps)


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


Assistant

