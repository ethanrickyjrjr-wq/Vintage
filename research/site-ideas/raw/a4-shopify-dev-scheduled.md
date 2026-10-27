[Skip to main content](https://shopify.dev/docs/apps/build/sales-channels/scheduled-product-publishing#main-content)
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
  * [Validation workflow](https://shopify.dev/docs/apps/build/sales-channels/scheduled-product-publishing#validation-workflow)
  * [Requirements](https://shopify.dev/docs/apps/build/sales-channels/scheduled-product-publishing#requirements)
  * [Step 1: Identify products that are scheduled for publication](https://shopify.dev/docs/apps/build/sales-channels/scheduled-product-publishing#step-1-identify-products-that-are-scheduled-for-publication)
  * [Step 2: Subscribe to webhooks](https://shopify.dev/docs/apps/build/sales-channels/scheduled-product-publishing#step-2-subscribe-to-webhooks)


# Scheduled publishing
Install AI ToolkitAsk about this pageCopy MD
Merchants can schedule products to be published to a sales channel at a specific datetime. Common use cases include product drops and timed sales, where merchants want to reserve sufficient inventory to meet spikes in customer demand.
* * *
## 
[Anchor to Validation workflow](https://shopify.dev/docs/apps/build/sales-channels/scheduled-product-publishing#validation-workflow)Validation workflow
If your channel app requires products to meet requirements before they can display to customers, then you need to validate products before their scheduled publication datetime. This gives merchants time to update products and resubmit them for validation. Otherwise, the channel validates the products at the scheduled datetime, and any updates required might delay their publication.
The following is the recommended workflow for channels that include validation:
  1. A merchant schedules a product to be published on the channel app at a specified datetime.
  2. Shopify sends a `scheduled_product_listings/add` event to the channel app.
  3. The channel app validates the product against requirements for displaying it on the channel.
  4. If the product fails validation, then the channel app sends feedback to the merchant using the `ResourceFeedback` object.
  5. The merchant updates the product to meet the requirements.
  6. Shopify sends a `scheduled_product_listings/update` event to the channel app.
  7. The channel app validates the product against the requirements.
  8. At the scheduled datetime, Shopify sends a `product_listings/add` event.
  9. The channel app reads the product data and displays the product.

![An image of the scheduled publishing workflow](https://shopify-assets.shopifycdn.com/shopifycloud/shopify-dev/production/assets/assets/images/apps/scheduled-publishing-validation-DPu_9Gvu.png)
* * *
## 
[Anchor to Requirements](https://shopify.dev/docs/apps/build/sales-channels/scheduled-product-publishing#requirements)Requirements
  * You've completed the [getting started tutorials](https://shopify.dev/docs/apps/build/sales-channels/start-building).
  * Your app requires the `read_product_listings` [access scope](https://shopify.dev/docs/api/usage/access-scopes#read_product_listings) and the `read_publications` [access scope](https://shopify.dev/docs/api/usage/access-scopes#read_publications).


* * *
## 
[Anchor to Step 1: Identify products that are scheduled for publication](https://shopify.dev/docs/apps/build/sales-channels/scheduled-product-publishing#step-1-identify-products-that-are-scheduled-for-publication)Step 1: Identify products that are scheduled for publication
Request `resourcePublicationsV2` with `onlyPublished: false` on the [GraphQL Admin API's Product](https://shopify.dev/docs/api/admin-graphql/latest/objects/product) object. Setting `onlyPublished` to `false` includes publications that are scheduled for the future, not only the ones that are currently published.
By default, the connection returns the product's publications to every app sales channel, not only yours. Find the node whose `publication.id` matches your channel's publication. If that node has a `publishDate` in the future and `isPublished` is `false`, then the product is scheduled to display on your channel at the specified datetime.
## POST /api/{api_version}/graphql.json
GraphQL queryJSON response
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
{
products(first: 10){
edges {
node {
title
resourcePublicationsV2(first: 10, onlyPublished: false){
nodes {
publication {
id
}
publishDate
isPublished
}
}
}
}
}
}
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
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
{
"data":{
"products":{
"edges":[
{
"node":{
"title":"Baseball",
"resourcePublicationsV2":{
"nodes":[
{
"publication":{
"id":"gid://shopify/Publication/2"
},
"publishDate":"2021-09-23T17:30:00Z",
"isPublished":false
}
]
}
}
},
{
"node":{
"title":"Soccer ball",
"resourcePublicationsV2":{
"nodes":[
{
"publication":{
"id":"gid://shopify/Publication/2"
},
"publishDate":"2021-09-10T17:30:00Z",
"isPublished":true
}
]
}
}
}
]
}
}
}
##### GraphQL query

```
{
  products(first: 10) {
    edges {
      node {
        title
        resourcePublicationsV2(first: 10, onlyPublished: false) {
          nodes {
            publication {
              id
            }
            publishDate
            isPublished
          }
        }
      }
    }
  }
}
```

##### JSON response

```
{
   "data":{
      "products":{
         "edges":[
            {
               "node":{
                  "title":"Baseball",
                  "resourcePublicationsV2":{
                     "nodes":[
                        {
                           "publication":{
                              "id":"gid://shopify/Publication/2"
                           },
                           "publishDate":"2021-09-23T17:30:00Z",
                           "isPublished":false
                        }
                     ]
                  }
               }
            },
            {
               "node":{
                  "title":"Soccer ball",
                  "resourcePublicationsV2":{
                     "nodes":[
                        {
                           "publication":{
                              "id":"gid://shopify/Publication/2"
                           },
                           "publishDate":"2021-09-10T17:30:00Z",
                           "isPublished":true
                        }
                     ]
                  }
               }
            }
         ]
      }
   }
}
```

* * *
## 
[Anchor to Step 2: Subscribe to webhooks](https://shopify.dev/docs/apps/build/sales-channels/scheduled-product-publishing#step-2-subscribe-to-webhooks)Step 2: Subscribe to webhooks
Note
This step is only required if the channel [validates products against requirements before displaying them](https://shopify.dev/docs/apps/build/sales-channels/scheduled-product-publishing#validation-workflow).
**Note :**
This step is only required if the channel [validates products against requirements before displaying them](https://shopify.dev/docs/apps/build/sales-channels/scheduled-product-publishing#validation-workflow).
Shopify's [`SCHEDULED_PRODUCT_LISTINGS`](https://shopify.dev/docs/api/admin-graphql/latest/enums/webhooksubscriptiontopic) webhooks notify channels when products are scheduled to be published.
The following is an example payload:
## Example webhook payload
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
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
{
"product_listing": {
"product_id": 788032119674292922,
"created_at": null,
"updated_at": "2021-10-01T17:12:26-04:00",
"body_html": null,
"handle": "example-t-shirt",
"product_type": "Shirts",
"title": "Example T-Shirt",
"vendor": "Acme",
"available": false,
"tags": "example, mens, t-shirt",
"publish_at": "2021-10-01T17:12:26-04:00",
"variants": [
{
"id": 642667041472713922,
"title": "",
"option_values": [
{
"option_id": 527050010214937811,
"name": "Title",
"value": "Small"
}
],
"price": "19.99",
"formatted_price": "$19.99",
"compare_at_price": "24.99",
"grams": 200,
"requires_shipping": true,
"sku": "example-shirt-s",
"barcode": null,
"taxable": true,
"position": 0,
"available": false,
"inventory_policy": "deny",
"inventory_quantity": 0,
"inventory_management": "shopify",
"fulfillment_service": "manual",
"weight": 200.0,
"weight_unit": "g",
"image_id": null,
"created_at": null,
"updated_at": null
}
],
"images": [
{
"id": 539438707724640965,
"created_at": null,
"position": 0,
"updated_at": null,
"product_id": 788032119674292922,
"src": "//cdn.shopify.com/shopifycloud/shopify/assets/shopify_shirt-39bb555874ecaeed0a1170417d58bbcf792f7ceb56acfe758384f788710ba635.png",
"variant_ids": [],
"width": 323,
"height": 434
}
],
"options": [
{
"id": 527050010214937811,
"name": "Title",
"product_id": 788032119674292922,
"position": 1,
"values": [
"Small",
"Medium",
"Large"
]
}
]
}
}
* * *
Was this page helpful?
YesNo
  * [Validation workflow](https://shopify.dev/docs/apps/build/sales-channels/scheduled-product-publishing#validation-workflow)
  * [Requirements](https://shopify.dev/docs/apps/build/sales-channels/scheduled-product-publishing#requirements)
  * [Step 1: Identify products that are scheduled for publication](https://shopify.dev/docs/apps/build/sales-channels/scheduled-product-publishing#step-1-identify-products-that-are-scheduled-for-publication)
  * [Step 2: Subscribe to webhooks](https://shopify.dev/docs/apps/build/sales-channels/scheduled-product-publishing#step-2-subscribe-to-webhooks)


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



