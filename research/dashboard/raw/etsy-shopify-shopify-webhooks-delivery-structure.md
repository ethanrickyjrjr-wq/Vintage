[Skip to main content](https://shopify.dev/docs/apps/build/webhooks/delivery-structure#main-content)
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
  * [Payload](https://shopify.dev/docs/apps/build/webhooks/delivery-structure#payload)
  * [Headers](https://shopify.dev/docs/apps/build/webhooks/delivery-structure#headers)
  * [include_fields](https://shopify.dev/docs/apps/build/webhooks/delivery-structure#include_fields)
  * [Example](https://shopify.dev/docs/apps/build/webhooks/delivery-structure#example)
  * [Next steps](https://shopify.dev/docs/apps/build/webhooks/delivery-structure#next-steps)


# Webhooks delivery structure
Install AI ToolkitAsk about this pageCopy MD
Each qualifying change sends a webhook delivery to the destination configured in your subscription's `uri`. Shopify supports webhook delivery through HTTPS, Amazon EventBridge, and Google Cloud Pub/Sub. See [Subscription fields](https://shopify.dev/docs/apps/build/webhooks/subscribe#subscription-fields) to configure your destination.
For HTTPS destinations, Shopify sends an HTTP POST with a JSON payload in the request body and delivery metadata in HTTP headers. For Amazon EventBridge and Google Cloud Pub/Sub, delivery metadata accompanies the payload in the message.
By default, the payload contains the full REST resource for the topic.
Add `include_fields` to receive only the specific fields your app needs.
![Modify payloads](https://shopify-assets.shopifycdn.com/shopifycloud/shopify-dev/production/assets/assets/images/apps/webhooks/customize/modify_payloads-ByCGW8QH.png)
* * *
## 
[Anchor to Payload](https://shopify.dev/docs/apps/build/webhooks/delivery-structure#payload)Payload
By default, the JSON payload contains the full REST resource for the subscribed topic. The shape and fields depend on the topic. See the [Webhooks reference](https://shopify.dev/docs/api/webhooks) for the payload structure of each topic. Amazon EventBridge and Google Cloud Pub/Sub messages include additional delivery metadata beyond these example payloads.
## Example payload (products/update)
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
14
15
16
17
18
19
{
"id": 9554194432293,
"title": "T-Shirt",
"status": "active",
"vendor": "My Store",
"product_type": "Shirts",
"updated_at": "2025-04-22T14:30:00-05:00",
"variants": [
{
"id": 123456789,
"title": "Default Title",
"price": "29.99",
"sku": "TSHIRT-001",
"taxable": true,
"updated_at": "2025-04-22T14:30:00-05:00"
}
],
"tags": "cotton, comfortable"
}
* * *
## 
[Anchor to Headers](https://shopify.dev/docs/apps/build/webhooks/delivery-structure#headers)Headers
HTTPS deliveries include the following HTTP headers. Treat header names as case-insensitive in your code, as HTTP/2 often lowercases them.
For Amazon EventBridge and Google Cloud Pub/Sub, delivery metadata accompanies the payload in the message. These delivery methods don't require [HMAC verification](https://shopify.dev/docs/apps/build/webhooks/verify-deliveries).  
| Header  | Description  |  
| --- | --- |  
| `X-Shopify-Topic`  | The topic name (for example, `products/update`).  |  
| `X-Shopify-Hmac-Sha256`  | Base64-encoded HMAC signature for verifying the delivery came from Shopify. HTTPS only.  |  
| `X-Shopify-Shop-Domain`  | The `myshopify.com` domain of the store that triggered the event.  |  
| `X-Shopify-API-Version`  | The API version used to serialize the payload.  |  
| `X-Shopify-Webhook-Id`  | A unique composite key per delivery. Use to identify and deduplicate individual deliveries.  |  
| `X-Shopify-Triggered-At`  | Timestamp of when Shopify triggered the delivery.  |  
| `X-Shopify-Event-Id`  | A unique ID shared across all deliveries produced by the same merchant action.  |  
|  `X-Shopify-Name` (optional)  | Developer-supplied subscription name, set via the `name` field in your subscription.  |  
* * *
## 
[Anchor to [object Object]](https://shopify.dev/docs/apps/build/webhooks/delivery-structure#include_fields)`include_fields`
`include_fields` is an optional array of field paths on a webhook subscription. When set, the delivery payload includes only the specified fields instead of the full resource.
Without `include_fields`, every delivery includes the complete resource payload:
## Without include_fields
shopify.app.toml{} Response
Copy
1
2
3
4
5
6
[webhooks]
api_version = "2026-10"
  

[[webhooks.subscriptions]]
topics = ["products/update"]
uri = "https://your-app.example.com/webhooks/products"
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
14
15
16
17
18
19
{
"id": 9554194432293,
"title": "T-Shirt",
"status": "active",
"vendor": "My Store",
"product_type": "Shirts",
"updated_at": "2025-04-22T14:30:00-05:00",
"variants": [
{
"id": 123456789,
"title": "Default Title",
"price": "29.99",
"sku": "TSHIRT-001",
"taxable": true,
"updated_at": "2025-04-22T14:30:00-05:00"
}
],
"tags": "cotton, comfortable"
}
##### shopify.app.toml

```
[webhooks]
api_version = "2026-10"

[[webhooks.subscriptions]]
topics = ["products/update"]
uri = "https://your-app.example.com/webhooks/products"
```

##### {} Response

```
{
  "id": 9554194432293,
  "title": "T-Shirt",
  "status": "active",
  "vendor": "My Store",
  "product_type": "Shirts",
  "updated_at": "2025-04-22T14:30:00-05:00",
  "variants": [
    {
      "id": 123456789,
      "title": "Default Title",
      "price": "29.99",
      "sku": "TSHIRT-001",
      "taxable": true,
      "updated_at": "2025-04-22T14:30:00-05:00"
    }
  ],
  "tags": "cotton, comfortable"
}
```

Adding `include_fields` narrows the payload to only the specified fields. You denote nested fields using a period (for example, `variants.price`). You can also set `include_fields` using the `includeFields` input in the [`webhookSubscriptionCreate`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/webhookSubscriptionCreate) mutation.
## With include_fields
shopify.app.toml{} Response
Copy
1
2
3
4
5
6
7
[webhooks]
api_version = "2026-10"
  

[[webhooks.subscriptions]]
topics = ["products/update"]
uri = "https://your-app.example.com/webhooks/products"
include_fields = ["id", "variants.id", "variants.price", "updated_at"]
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
"id": 9554194432293,
"variants": [
{
"id": 123456789,
"price": "29.99"
}
],
"updated_at": "2025-04-22T14:30:00-05:00"
}
##### shopify.app.toml

```
[webhooks]
api_version = "2026-10"

[[webhooks.subscriptions]]
topics = ["products/update"]
uri = "https://your-app.example.com/webhooks/products"
include_fields = ["id", "variants.id", "variants.price", "updated_at"]
```

##### {} Response

```
{
  "id": 9554194432293,
  "variants": [
    {
      "id": 123456789,
      "price": "29.99"
    }
  ],
  "updated_at": "2025-04-22T14:30:00-05:00"
}
```

### 
[Anchor to Debouncing](https://shopify.dev/docs/apps/build/webhooks/delivery-structure#debouncing)Debouncing
When `include_fields` reduces the payload to a small set of fields, multiple qualifying events might produce identical payloads. Shopify debounces deliveries with identical payloads that arrive within a short time window, dropping the later one. For example, a subscription to `orders/updated` with `include_fields = ["id", "line_items.title"]` would debounce consecutive price changes, since neither the order ID nor line item titles change between them.
To prevent debouncing, include a field that always has a unique value. For example, `updated_at` changes with every update, ensuring no two consecutive deliveries are identical.
### 
[Anchor to Combining with ,[object Object]](https://shopify.dev/docs/apps/build/webhooks/delivery-structure#combining-with-filter)Combining with `filter`
When both `filter` and `include_fields` are set, all fields referenced in the `filter` expression must also appear in `include_fields`.
## shopify.app.toml
Copy
1
2
3
4
5
6
7
8
[webhooks]
api_version = "2026-10"
  

[[webhooks.subscriptions]]
topics = ["products/update"]
uri = "https://example.com/webhooks"
include_fields = ["id", "status", "product_type", "variants.taxable", "variants.price", "variants.title", "updated_at"]
filter = "id:* AND status:active AND (product_type:Music OR product_type:Movies) AND variants.taxable:true AND variants.price:>=100 AND variants.title:'The Miseducation of'"
See [Delivery filtering](https://shopify.dev/docs/apps/build/webhooks/delivery-filtering) for filter syntax and examples.
* * *
## 
[Anchor to Example](https://shopify.dev/docs/apps/build/webhooks/delivery-structure#example)Example
Suppose you want deliveries only when an active product in the Music or Movies category has a variant priced above $100. The following subscription combines `include_fields` to narrow the payload and `filter` to gate delivery:
## Active high-price music or movies product
shopify.app.toml{} Response
Copy
1
2
3
4
5
6
7
8
[webhooks]
api_version = "2026-10"
  

[[webhooks.subscriptions]]
topics = ["products/update"]
uri = "https://your-app.example.com/webhooks/products"
include_fields = ["id", "status", "product_type", "variants.id", "variants.price", "updated_at"]
filter = "status:active AND (product_type:Music OR product_type:Movies) AND variants.price:>=100"
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
{
"id": 9554194432293,
"status": "active",
"product_type": "Music",
"variants": [
{
"id": 123456789,
"price": "129.99"
}
],
"updated_at": "2025-04-22T15:00:00-05:00"
}
##### shopify.app.toml

```
[webhooks]
api_version = "2026-10"

[[webhooks.subscriptions]]
topics = ["products/update"]
uri = "https://your-app.example.com/webhooks/products"
include_fields = ["id", "status", "product_type", "variants.id", "variants.price", "updated_at"]
filter = "status:active AND (product_type:Music OR product_type:Movies) AND variants.price:>=100"
```

##### {} Response

```
{
  "id": 9554194432293,
  "status": "active",
  "product_type": "Music",
  "variants": [
    {
      "id": 123456789,
      "price": "129.99"
    }
  ],
  "updated_at": "2025-04-22T15:00:00-05:00"
}
```

* * *
## 
[Anchor to Next steps](https://shopify.dev/docs/apps/build/webhooks/delivery-structure#next-steps)Next steps
  * [Delivery filtering](https://shopify.dev/docs/apps/build/webhooks/delivery-filtering): Gate deliveries with `filter` expressions.
  * [Verify deliveries](https://shopify.dev/docs/apps/build/webhooks/verify-deliveries): HMAC verification and deduplication.


* * *
Was this page helpful?
YesNo
  * [Payload](https://shopify.dev/docs/apps/build/webhooks/delivery-structure#payload)
  * [Headers](https://shopify.dev/docs/apps/build/webhooks/delivery-structure#headers)
  * [include_fields](https://shopify.dev/docs/apps/build/webhooks/delivery-structure#include_fields)
  * [Example](https://shopify.dev/docs/apps/build/webhooks/delivery-structure#example)
  * [Next steps](https://shopify.dev/docs/apps/build/webhooks/delivery-structure#next-steps)


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



