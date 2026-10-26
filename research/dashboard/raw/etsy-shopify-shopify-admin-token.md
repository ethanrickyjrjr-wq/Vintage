[Skip to main content](https://shopify.dev/docs/apps/build/authentication-authorization/legacy/admin-custom-apps#main-content)
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
  * [Make authenticated requests](https://shopify.dev/docs/apps/build/authentication-authorization/legacy/admin-custom-apps#make-authenticated-requests)
  * [Rotate or generate new credentials](https://shopify.dev/docs/apps/build/authentication-authorization/legacy/admin-custom-apps#rotate-or-generate-new-credentials)
  * [Change API scopes](https://shopify.dev/docs/apps/build/authentication-authorization/legacy/admin-custom-apps#change-api-scopes)
  * [Next steps](https://shopify.dev/docs/apps/build/authentication-authorization/legacy/admin-custom-apps#next-steps)


# Generate access tokens for admin-created custom apps
Install AI ToolkitAsk about this pageCopy MD
Caution
You can no longer create new admin-created custom apps. Existing apps are unaffected and continue to work. For new apps, use [Dev Dashboard](https://shopify.dev/docs/apps/build/dev-dashboard/create-apps-using-dev-dashboard) or [Shopify CLI](https://shopify.dev/docs/apps/build/cli-for-apps).
**Caution :**
You can no longer create new admin-created custom apps. Existing apps are unaffected and continue to work. For new apps, use [Dev Dashboard](https://shopify.dev/docs/apps/build/dev-dashboard/create-apps-using-dev-dashboard) or [Shopify CLI](https://shopify.dev/docs/apps/build/cli-for-apps).
Admin-created custom apps are apps created directly in the Shopify admin, without going through the OAuth installation flow. Shopify pre-generates API access tokens when the merchant installs the app. There's no authorization code grant, no `shopify.app.toml`, and no managed installation.
If you're maintaining an existing admin-created custom app, use this page to reference how to authenticate API requests, understand the limitations around credential rotation, and manage API scopes.
* * *
## 
[Anchor to Make authenticated requests](https://shopify.dev/docs/apps/build/authentication-authorization/legacy/admin-custom-apps#make-authenticated-requests)Make authenticated requests
Your app's API access token is shown only once, when it's generated, so store it somewhere secure at that point. To see whether it's still available, go to **Apps** > **Develop apps** > [your app] > **API credentials**. If the token is no longer retrievable, [generate a new one](https://shopify.dev/docs/apps/build/authentication-authorization/legacy/admin-custom-apps#rotate-or-generate-new-credentials). Use the token to authenticate requests to the GraphQL Admin API.
The following examples query the GraphQL Admin API to retrieve the first five products from a store.
Info
The following examples require the `SHOP_TOKEN` environment variable set to your Admin API access token with at least the `read_products` scope. Replace `{shop}` with your store's subdomain.
**Info :**
The following examples require the `SHOP_TOKEN` environment variable set to your Admin API access token with at least the `read_products` scope. Replace `{shop}` with your store's subdomain.
## cURL
Copy
$
$
$
$
$
$
$
$
$
$
$
$
$
$
$
$
$
$
$
$
$
curl -sX POST \
https://{shop}.myshopify.com/admin/api/2026-10/graphql.json \
-H 'Content-Type: application/json' \
-H "X-Shopify-Access-Token: ${SHOP_TOKEN}" \
-d @- <<EOF
{
"query": "{
products(first: 5) {
edges {
node {
id
handle
}
}
pageInfo {
hasNextPage
}
}
}"
}
EOF
You can pipe the response through [`jq`](https://jqlang.org/) to extract specific fields:
## cURL with jq
Copy
$
$
$
$
$
$
$
$
$
$
$
$
$
$
$
$
$
$
$
$
$
curl -sX POST \
https://{shop}.myshopify.com/admin/api/2026-10/graphql.json \
-H 'Content-Type: application/json' \
-H "X-Shopify-Access-Token: ${SHOP_TOKEN}" \
-d @- <<EOF | jq '.data.products.edges[].node | {id, handle}'
{
"query": "{
products(first: 5) {
edges {
node {
id
handle
}
}
pageInfo {
hasNextPage
}
}
}"
}
EOF
* * *
## 
[Anchor to Rotate or generate new credentials](https://shopify.dev/docs/apps/build/authentication-authorization/legacy/admin-custom-apps#rotate-or-generate-new-credentials)Rotate or generate new credentials
You can't rotate the API key or secret for an admin-created custom app. To generate a new access token, uninstall and reinstall the app from the Shopify admin. The app itself stays intact: uninstalling removes it from the store, and reinstalling generates a new token. Your app's requests and webhooks are disrupted until you update your code with the new token.
Caution
Don't delete the app itself. Deleting removes the app configuration from the Shopify admin permanently, and you can't create a new admin-created custom app to replace it. If you need a new app, use [Dev Dashboard](https://shopify.dev/docs/apps/build/dev-dashboard/create-apps-using-dev-dashboard) to create one with a proper OAuth flow.
**Caution :**
Don't delete the app itself. Deleting removes the app configuration from the Shopify admin permanently, and you can't create a new admin-created custom app to replace it. If you need a new app, use [Dev Dashboard](https://shopify.dev/docs/apps/build/dev-dashboard/create-apps-using-dev-dashboard) to create one with a proper OAuth flow.
If you need to rotate access tokens for a custom storefront built with the Headless channel, see [Rotate private access tokens](https://shopify.dev/docs/storefronts/headless/building-with-the-storefront-api/manage-headless-channels#rotate-private-access-tokens).
* * *
## 
[Anchor to Change API scopes](https://shopify.dev/docs/apps/build/authentication-authorization/legacy/admin-custom-apps#change-api-scopes)Change API scopes
Anyone with a [staff or collaborator account](https://help.shopify.com/en/manual/your-account/staff-accounts/staff-permissions) on a store can change what resources an admin-created custom app can access, provided they have the **Manage and install apps and channels** permission, the **Develop apps** permission, and the relevant permissions for the resource being changed.
The store owner can [change staff or collaborator permissions](https://help.shopify.com/en/manual/your-account/staff-accounts/staff-permissions) in the Shopify admin.
### 
[Anchor to Permissions required to assign scopes](https://shopify.dev/docs/apps/build/authentication-authorization/legacy/admin-custom-apps#permissions-required-to-assign-scopes)Permissions required to assign scopes
The following table shows what store permissions a staff or collaborator account needs to assign [Admin API access scopes](https://shopify.dev/docs/api/usage/access-scopes) to an admin-created custom app. The account must also have the **Develop apps** permission in all cases.  
| Admin API scope name  | Permissions required  |  
| --- | --- |  
| `read_analytics`  | View store metrics  |  
|  `read_assigned_fulfillment_orders`, `write_assigned_fulfillment_orders`  | View or manage fulfillment orders  |  
|  `read_customer_merge`, `write_customer_merge`  | View or manage customer profile merges  |  
|  `read_customers`, `write_customers`  | View or manage customers, customer addresses, order history, and customer groups  |  
|  `read_discounts`, `write_discounts`  | View or manage automatic discounts and discount codes  |  
|  `read_draft_orders`, `write_draft_orders`  | View or manage orders created by app users on behalf of customers  |  
|  `read_files`, `write_files`  | View or manage files  |  
|  `read_fulfillments`, `write_fulfillments`  | View or manage fulfillment services  |  
| `read_gdpr_data_request`  | View GDPR data requests  |  
|  `read_gift_cards`, `write_gift_cards`  | View or manage gift cards (Shopify Plus only)  |  
|  `read_inventory`, `write_inventory`  | View or manage inventory across multiple locations  |  
|  `read_legal_policies`, `write_legal_policies`  | View or manage a shop's legal policies  |  
| `read_locations`  | View the geographic location of stores, headquarters, and warehouses  |  
|  `read_marketing_events`, `write_marketing_events`  | View or manage marketing events and engagement data  |  
|  `read_merchant_managed_fulfillment_orders`, `write_merchant_managed_fulfillment_orders`  | View or manage fulfillment orders assigned to merchant-managed locations  |  
|  `read_metaobject_definitions`, `write_metaobject_definitions`  | View or manage metaobject definitions  |  
|  `read_metaobjects`, `write_metaobjects`  | View or manage metaobject entries  |  
| `read_online_store_navigation`  | View menus for display on the storefront  |  
|  `read_online_store_pages`, `write_online_store_pages`  | View or manage Online Store pages  |  
|  `read_order_edits`, `write_order_edits`  | View or manage edits to orders  |  
|  `read_orders`, `write_orders`, `read_all_orders`  | View or manage orders, transactions, fulfillments, and abandoned checkouts from the last 60 days, or view all past and future orders  |  
|  `read_price_rules`, `write_price_rules`  | View or manage conditional discounts  |  
|  `read_products`, `write_products`  | View or manage products, variants, and collections  |  
|  `read_product_listings`, `write_product_listings`  | View or manage product or collection listings  |  
|  `read_reports`, `write_reports`  | View or manage reports on the **Reports** page in the Shopify admin  |  
|  `read_resource_feedbacks`, `write_resource_feedbacks`  | View or manage the status of shops and resources  |  
|  `read_script_tags`, `write_script_tags`  | View or manage JavaScript code in storefront or order status pages  |  
|  `read_shipping`, `write_shipping`  | View or manage shipping carriers, countries, and provinces  |  
| `read_shopify_payments_accounts`  | View Shopify Payments accounts  |  
| `read_shopify_payments_bank_accounts`  | View bank accounts that can receive Shopify Payments payouts  |  
| `read_shopify_payments_disputes`  | View Shopify Payments disputes raised by buyers  |  
| `read_shopify_payments_payouts`  | View Shopify Payments payouts and the account's current balance  |  
|  `read_content`, `write_content`  | View or manage articles, blogs, comments, pages, and redirects  |  
|  `read_themes`, `write_themes`  | View or manage theme templates and assets  |  
|  `read_third_party_fulfillment_orders`, `write_third_party_fulfillment_orders`  | View or manage fulfillment orders assigned to a location managed by any fulfillment service  |  
|  `read_translations`, `write_translations`  | View or manage content that can be translated  |  
* * *
## 
[Anchor to Next steps](https://shopify.dev/docs/apps/build/authentication-authorization/legacy/admin-custom-apps#next-steps)Next steps
  * Learn how to [configure a webhook](https://shopify.dev/docs/apps/build/webhooks/subscribe) for your app and [manage webhooks for different API versions](https://shopify.dev/docs/apps/build/webhooks/subscribe#versioning).
  * Explore the [Webhooks references](https://shopify.dev/docs/api/webhooks) and [GraphQL Admin API](https://shopify.dev/docs/api/admin-graphql) references.


* * *
Was this page helpful?
YesNo
  * [Make authenticated requests](https://shopify.dev/docs/apps/build/authentication-authorization/legacy/admin-custom-apps#make-authenticated-requests)
  * [Rotate or generate new credentials](https://shopify.dev/docs/apps/build/authentication-authorization/legacy/admin-custom-apps#rotate-or-generate-new-credentials)
  * [Change API scopes](https://shopify.dev/docs/apps/build/authentication-authorization/legacy/admin-custom-apps#change-api-scopes)
  * [Next steps](https://shopify.dev/docs/apps/build/authentication-authorization/legacy/admin-custom-apps#next-steps)


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



