[Skip to main content](https://shopify.dev/docs/apps/build/compliance/privacy-law-compliance#main-content)
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
  * [Mandatory compliance webhooks](https://shopify.dev/docs/apps/build/compliance/privacy-law-compliance#mandatory-compliance-webhooks)
  * [customers/data_request](https://shopify.dev/docs/apps/build/compliance/privacy-law-compliance#customers-data_request)
  * [customers/redact](https://shopify.dev/docs/apps/build/compliance/privacy-law-compliance#customers-redact)
  * [shop/redact](https://shopify.dev/docs/apps/build/compliance/privacy-law-compliance#shop-redact)
  * [Next steps](https://shopify.dev/docs/apps/build/compliance/privacy-law-compliance#next-steps)


# Privacy law compliance
Install AI ToolkitAsk about this pageCopy MD
Data privacy rules and regulations, such as the General Data Protection Regulation (GDPR) and California Privacy Rights Act (CPRA), set requirements for parties that collect, store, or process personal data of individuals. However, Shopify takes a standardized approach and requires public apps to provide the same privacy rights for all personal data, regardless of where an individual is located.
* * *
## 
[Anchor to Mandatory compliance webhooks](https://shopify.dev/docs/apps/build/compliance/privacy-law-compliance#mandatory-compliance-webhooks)Mandatory compliance webhooks
Mandatory compliance webhooks are callback methods that Shopify requires for apps listed on the Shopify App Store. Shopify requires mandatory compliance webhooks as a way to manage the personal data that an app collects.
Any app that you distribute through the Shopify App Store must respond to data subject requests, regardless of whether the app collects personal data. Shopify provides mandatory compliance webhooks to help.
[ ![](https://shopify-assets.shopifycdn.com/shopifycloud/shopify-dev/production/assets/assets/images/icons/32/webhooks-CTBIB8Gw.png)![](https://shopify-assets.shopifycdn.com/shopifycloud/shopify-dev/production/assets/assets/images/icons/32/webhooks-dark-BwZ9WDtY.png) WebhooksUse webhooks to stay in sync with Shopify or execute code after a specific event occurs in a store. Webhooks Use webhooks to stay in sync with Shopify or execute code after a specific event occurs in a store. ](https://shopify.dev/docs/apps/build/webhooks)
[Webhooks  
  
Use webhooks to stay in sync with Shopify or execute code after a specific event occurs in a store.](https://shopify.dev/docs/apps/build/webhooks)
[ ![](https://shopify-assets.shopifycdn.com/shopifycloud/shopify-dev/production/assets/assets/images/icons/48/app-B9pr02rY.png)![](https://shopify-assets.shopifycdn.com/shopifycloud/shopify-dev/production/assets/assets/images/icons/48/app-dark-D3_H1074.png) Checklist of requirementsFollow requirements to make sure your app provides a high-quality experience to merchants. This is the same checklist that the Shopify App Review team uses to review apps. Checklist of requirements Follow requirements to make sure your app provides a high-quality experience to merchants. This is the same checklist that the Shopify App Review team uses to review apps. ](https://shopify.dev/docs/apps/launch/app-requirements-checklist)
[Checklist of requirements  
  
Follow requirements to make sure your app provides a high-quality experience to merchants. This is the same checklist that the Shopify App Review team uses to review apps.](https://shopify.dev/docs/apps/launch/app-requirements-checklist)
### 
[Anchor to How it works](https://shopify.dev/docs/apps/build/compliance/privacy-law-compliance#how-it-works)How it works
You must ensure that your app is subscribed to and verifies all mandatory compliance webhooks before you submit your app to be reviewed by Shopify.
Apps must meet the following webhook requirements:
  * The app must implement the mandatory compliance webhooks.
  * The app must handle `POST` requests with a JSON body and `Content-Type` header set to `application/json` sent to mandatory compliance webhooks.
  * If a mandatory compliance webhook sends a request with an invalid Shopify `HMAC` header, then the app must return a `401 Unauthorized` HTTP status. Learn more about [Verifying webhook deliveries](https://shopify.dev/docs/apps/build/webhooks/verify-deliveries#hmac-verification).


If you don't provide URLs for the mandatory compliance webhooks, or your app doesn't [respond to these webhooks](https://shopify.dev/docs/apps/build/compliance/privacy-law-compliance#respond-to-compliance-webhooks) as required, then your app will be rejected and you'll need to fix the identified problem before submitting your app for another review.
Caution
This page isn't intended to provide you with legal advice. It sets out Shopify's privacy requirements for app developers and items that you need to consider if you're handling personal data.
**Caution :**
This page isn't intended to provide you with legal advice. It sets out Shopify's privacy requirements for app developers and items that you need to consider if you're handling personal data.
### 
[Anchor to Compliance webhook topics](https://shopify.dev/docs/apps/build/compliance/privacy-law-compliance#compliance-webhook-topics)Compliance webhook topics
Every app that's distributed through the Shopify App Store must subscribe to the following compliance webhook topics:  
Compliance webhook topics for apps  
| Topic  | Event  |  
| --- | --- |  
| `customers/data_request[](https://shopify.dev/docs/apps/build/compliance/privacy-law-compliance#customers-data_request)`  | Requests to view stored customer data  |  
| `customers/redact[](https://shopify.dev/docs/apps/build/compliance/privacy-law-compliance#customers-redact)`  | Requests to delete customer data  |  
| `shop/redact[](https://shopify.dev/docs/apps/build/compliance/privacy-law-compliance#shop-redact)`  | Requests to delete shop data  |  
### 
[Anchor to Subscribe to compliance webhooks](https://shopify.dev/docs/apps/build/compliance/privacy-law-compliance#subscribe-to-compliance-webhooks)Subscribe to compliance webhooks
You must subscribe to compliance webhooks before publishing your app. To subscribe to compliance webhooks, you need to register endpoints and then configure them in your [app config TOML](https://shopify.dev/docs/apps/structure/configuration#app-configuration-file-example%5D).
  1. Register an endpoint for each compliance webhook. For HTTPS urls, this will require a valid SSL certificate that can correctly process webhook event notifications. For more information, refer to [register an endpoint](https://shopify.dev/docs/apps/build/webhooks/verify-deliveries#https-delivery-considerations) for HTTPS, [set up an event source](https://shopify.dev/docs/apps/build/webhooks/get-started) for AWS EventBridge, or [retrieve your Shopify service account address](https://shopify.dev/docs/apps/build/webhooks/get-started) for Google Pub/Sub.
  2. You can subscribe to the compliance webhook topics by making the following changes to your app's `shopify.app.toml` file in the app's root folder. Learn more about [configuring your app with the TOML file](https://shopify.dev/docs/apps/build/cli-for-apps/app-configuration).
## shopify.app.toml
Copy
1
2
3
4
5
6
[webhooks]
api_version = "2024-07"
  

[[webhooks.subscriptions]]
compliance_topics = ["customers/data_request", "customers/redact", "shop/redact"]
uri = "https://app.example.com/webhooks"


Info
The following is the structure of the URL you should use for the URI when working with **Google Cloud Pub/Sub** :
`pubsub://{project-id}:{topic-id}`
Where `{project-id}` is the ID of your Google Cloud Platform project, and `{topic-id}` is the ID of the topic that you set up in Google Cloud Pub/Sub.
For **Amazon EventBridge** , your URL will be similar to the following example:
`arn:aws:events:<aws_region>::event-source/aws.partner/shopify.com/<app_id>/<event_source_name>`
**Info :**
The following is the structure of the URL you should use for the URI when working with **Google Cloud Pub/Sub** :
`pubsub://{project-id}:{topic-id}`
Where `{project-id}` is the ID of your Google Cloud Platform project, and `{topic-id}` is the ID of the topic that you set up in Google Cloud Pub/Sub.
For **Amazon EventBridge** , your URL will be similar to the following example:
`arn:aws:events:<aws_region>::event-source/aws.partner/shopify.com/<app_id>/<event_source_name>`
### 
[Anchor to Respond to compliance webhooks](https://shopify.dev/docs/apps/build/compliance/privacy-law-compliance#respond-to-compliance-webhooks)Respond to compliance webhooks
When you receive one of the compliance webhooks, you need to take the following actions:
  * Confirm that you've received the request by responding with a `200` series status code.
  * Complete the action within 30 days of receiving the request. However, if you're unable to comply with a redaction request because you're legally required to retain data, then you shouldn't complete the action.
Learn more about how to [receive and respond](https://shopify.dev/docs/apps/build/webhooks/subscribe) to webhooks.


* * *
## 
[Anchor to customers/data_request](https://shopify.dev/docs/apps/build/compliance/privacy-law-compliance#customers-data_request)customers/data_request
Customers can request their data from a store owner. When this happens, Shopify sends a [payload](https://shopify.dev/docs/apps/build/compliance/privacy-law-compliance#customers-data_request-payload) on the `customers/data_request` topic to the apps that are installed on that store.
If your app has been granted access to [customer or order data](https://shopify.dev/docs/api/usage/access-scopes#authenticated-access-scopes), then it will receive a data request webhook. The webhook contains the resource IDs of the customer data that you need to provide to the store owner directly. In some cases, a customer record contains only the customer's email address.
### 
[Anchor to [object Object], payload](https://shopify.dev/docs/apps/build/compliance/privacy-law-compliance#customers-data_request-payload)`customers/data_request` payload
Copy
1
2
3
4
5
6
7
8
9
10
11
12
13
{
"shop_id": 954889,
"shop_domain": "{shop}.myshopify.com",
"orders_requested": [299938, 280263, 220458],
"customer": {
"id": 191167,
"email": "john@example.com",
"phone": "555-625-1199"
},
"data_request": {
"id": 9999
}
}
* * *
## 
[Anchor to customers/redact](https://shopify.dev/docs/apps/build/compliance/privacy-law-compliance#customers-redact)customers/redact
Store owners can request that data is deleted on behalf of a customer. When this happens, Shopify sends a [payload](https://shopify.dev/docs/apps/build/compliance/privacy-law-compliance#customers-redact-payload) on the `customers/redact` topic to the apps installed on that store.
If your app has been granted access to the store's customer or order data, then it will receive a redaction request webhook with the resource IDs that you need to redact or delete. In some cases, a customer record contains only the customer's email address.
If a customer hasn't placed an order in the past six months, then Shopify sends the payload 10 days after the deletion request. Otherwise, the request is withheld until six months have passed.
### 
[Anchor to [object Object], payload](https://shopify.dev/docs/apps/build/compliance/privacy-law-compliance#customers-redact-payload)`customers/redact` payload
Copy
1
2
3
4
5
6
7
8
9
10
{
"shop_id": 954889,
"shop_domain": "{shop}.myshopify.com",
"customer": {
"id": 191167,
"email": "john@example.com",
"phone": "555-625-1199"
},
"orders_to_redact": [299938, 280263, 220458]
}
* * *
## 
[Anchor to shop/redact](https://shopify.dev/docs/apps/build/compliance/privacy-law-compliance#shop-redact)shop/redact
48 hours after a store owner uninstalls your app, Shopify sends a [payload](https://shopify.dev/docs/apps/build/compliance/privacy-law-compliance#shop-redact-payload) on the `shop/redact` topic. This webhook provides the store's `shop_id` and `shop_domain` so that you can erase data for that store from your database.
### 
[Anchor to [object Object], payload](https://shopify.dev/docs/apps/build/compliance/privacy-law-compliance#shop-redact-payload)`shop/redact` payload
Copy
1
2
3
4
{
"shop_id": 954889,
"shop_domain": "{shop}.myshopify.com"
}
* * *
## 
[Anchor to Next steps](https://shopify.dev/docs/apps/build/compliance/privacy-law-compliance#next-steps)Next steps
  * Test your configuration by manually triggering a webhook delivery using the Shopify CLI [`webhook trigger`](https://shopify.dev/docs/api/shopify-cli/app/app-webhook-trigger) command. Manually triggering webhooks doesn't test your webhook subscriptions.
  * Learn how to [manage webhooks for different API versions](https://shopify.dev/docs/apps/build/webhooks/subscribe#versioning).
  * Learn about the available topics for [REST Admin API webhooks](https://shopify.dev/docs/api/admin-rest/latest/resources/webhook).
  * Learn about the available topics for [GraphQL Admin API webhooks](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic).


  * Familiarize yourself with [data privacy concepts](https://shopify.dev/docs/apps/launch/privacy-requirements) for apps including privacy policies, data rights, and consent for marketing services.


* * *
Was this page helpful?
YesNo
  * [Mandatory compliance webhooks](https://shopify.dev/docs/apps/build/compliance/privacy-law-compliance#mandatory-compliance-webhooks)
  * [customers/data_request](https://shopify.dev/docs/apps/build/compliance/privacy-law-compliance#customers-data_request)
  * [customers/redact](https://shopify.dev/docs/apps/build/compliance/privacy-law-compliance#customers-redact)
  * [shop/redact](https://shopify.dev/docs/apps/build/compliance/privacy-law-compliance#shop-redact)
  * [Next steps](https://shopify.dev/docs/apps/build/compliance/privacy-law-compliance#next-steps)


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



