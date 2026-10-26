[Skip to main content](https://shopify.dev/docs/apps/build/apis/graphql-admin/rate-limits#main-content)
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
  * [Cost calculation](https://shopify.dev/docs/apps/build/apis/graphql-admin/rate-limits#cost-calculation)
  * [Requested and actual cost](https://shopify.dev/docs/apps/build/apis/graphql-admin/rate-limits#requested-and-actual-cost)
  * [Single query limit](https://shopify.dev/docs/apps/build/apis/graphql-admin/rate-limits#single-query-limit)
  * [Input limits](https://shopify.dev/docs/apps/build/apis/graphql-admin/rate-limits#input-limits)
  * [GraphQL response](https://shopify.dev/docs/apps/build/apis/graphql-admin/rate-limits#graphql-response)
  * [Resource-based rate limits](https://shopify.dev/docs/apps/build/apis/graphql-admin/rate-limits#resource-based-rate-limits)
  * [Bulk operations](https://shopify.dev/docs/apps/build/apis/graphql-admin/rate-limits#bulk-operations)
  * [Avoiding rate limit errors](https://shopify.dev/docs/apps/build/apis/graphql-admin/rate-limits#avoiding-rate-limit-errors)
  * [Next steps](https://shopify.dev/docs/apps/build/apis/graphql-admin/rate-limits#next-steps)


# GraphQL Admin API rate limits
Install AI ToolkitAsk about this pageCopy MD
Calls to the GraphQL Admin API are limited based on calculated query cost, which means you should consider the cost of requests over time rather than the number of requests.
GraphQL Admin API rate limits are based on the combination of the app and store. Calls from one app don't affect the rate limits of another app, even on the same store. Similarly, calls to one store don't affect the rate limits of another store, even from the same app.
Each combination of app and store is given a bucket size and restore rate based on the store's plan. By making simpler, lower-cost queries, you can maximize your throughput and make more queries over time.  
| Plan  | Rate limit  |  
| --- | --- |  
| Standard  | 100 points/second  |  
| Advanced Shopify  | 200 points/second  |  
| Shopify Plus  | 1000 points/second  |  
| Shopify for enterprise (Commerce Components)  | 2000 points/second  |  
Limits are enforced with a [leaky bucket](https://shopify.dev/docs/api/usage/limits#the-leaky-bucket-algorithm): your quota refills continuously, so short bursts are fine as long as your average cost stays under the restore rate.
* * *
## 
[Anchor to Cost calculation](https://shopify.dev/docs/apps/build/apis/graphql-admin/rate-limits#cost-calculation)Cost calculation
Every field in the schema has an integer cost value assigned to it. The cost of a query is the maximum of possible fields selected. Running a query is the best way to find out its true cost.
By default, a field's cost is based on what the field returns:  
| Field returns  | Cost value  |  
| --- | --- |  
| Scalar  | 0  |  
| Enum  | 0  |  
| Object  | 1  |  
| Interface  | Maximum of possible selections  |  
| Union  | Maximum of possible selections  |  
| Connection  | Sized by `first` and `last` arguments  |  
| Mutation  | 10  |  
Although these default costs are in place, Shopify also reserves the right to set manual costs on fields.
* * *
## 
[Anchor to Requested and actual cost](https://shopify.dev/docs/apps/build/apis/graphql-admin/rate-limits#requested-and-actual-cost)Requested and actual cost
Shopify calculates the cost of a query both before and after execution.
  * The **requested cost** is based on the composition of fields selected in the request.
  * The **actual cost** is based on the query results, and may be lower than requested cost due to the actual objects returned or connections that return fewer edges than requested.


Rate limits use a combination of the requested and actual query cost. Before execution begins, an app's bucket must have enough capacity for the requested cost of a query. When execution is complete, the bucket is refunded the difference between the requested cost and the actual cost of the query.
* * *
## 
[Anchor to Single query limit](https://shopify.dev/docs/apps/build/apis/graphql-admin/rate-limits#single-query-limit)Single query limit
A single query may not exceed a cost of 1,000 points, regardless of plan limits. This limit is enforced before a query is executed based on the query's requested cost.
* * *
## 
[Anchor to Input limits](https://shopify.dev/docs/apps/build/apis/graphql-admin/rate-limits#input-limits)Input limits
Input arguments that accept an array have a maximum size of 250, on every Shopify API. Requests return an error if an input array exceeds 250 items.
* * *
## 
[Anchor to GraphQL response](https://shopify.dev/docs/apps/build/apis/graphql-admin/rate-limits#graphql-response)GraphQL response
The response includes information about the cost of the request and the state of the throttle. This data is returned under the `extensions` key:
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
"extensions": {
"cost": {
"requestedQueryCost": 101,
"actualQueryCost": 46,
"throttleStatus": {
"maximumAvailable": 1000,
"currentlyAvailable": 954,
"restoreRate": 50
}
}
}
To get a detailed breakdown of how each field contributes to the requested cost, you can include the header `Shopify-GraphQL-Cost-Debug=1` in your request.
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
"extensions": {
"cost": {
"requestedQueryCost": 101,
"actualQueryCost": 46,
"throttleStatus": ...,
"fields": [
{
"path": [
"shop"
],
"definedCost": 1,
"requestedTotalCost": 101,
"requestedChildrenCost": 100
},
...
]
}
}
* * *
## 
[Anchor to Resource-based rate limits](https://shopify.dev/docs/apps/build/apis/graphql-admin/rate-limits#resource-based-rate-limits)Resource-based rate limits
Once a store has 500,000 product variants, no more than 10,000 new variants can be created per day, on any API.
Past that threshold, the following GraphQL Admin API mutations are subject to the daily throttle, and an app that reaches it receives a `429 Too Many Requests` response with a message that a throttle has been applied.
  * [`productCreate`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/productcreate)
  * [`productUpdate`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/productupdate)
  * [`productVariantCreate`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/productvariantcreate)


In certain cases, Shopify needs to enforce rate limiting in order to prevent abuse of the platform. Therefore, your app should be prepared to handle rate limiting on all endpoints, rather than just those listed here.
Plus
These additional limits don't apply to stores on the [Shopify Plus](https://www.shopify.com/plus) plan.
**Plus :**
These additional limits don't apply to stores on the [Shopify Plus](https://www.shopify.com/plus) plan.
* * *
## 
[Anchor to Bulk operations](https://shopify.dev/docs/apps/build/apis/graphql-admin/rate-limits#bulk-operations)Bulk operations
To query and fetch large amounts of data, you should use [bulk operations](https://shopify.dev/docs/apps/build/apis/graphql-admin/bulk-operations/queries) instead of single queries. Bulk operations are designed for handling large amounts of data, and they don't have the max cost limits or rate limits that single queries have.
* * *
## 
[Anchor to Avoiding rate limit errors](https://shopify.dev/docs/apps/build/apis/graphql-admin/rate-limits#avoiding-rate-limit-errors)Avoiding rate limit errors
The practices for staying under a rate limit are the same on every Shopify API. Refer to [avoiding rate limit errors](https://shopify.dev/docs/api/usage/limits#avoiding-rate-limit-errors).
* * *
## 
[Anchor to Next steps](https://shopify.dev/docs/apps/build/apis/graphql-admin/rate-limits#next-steps)Next steps
  * Read how [bulk operations](https://shopify.dev/docs/apps/build/apis/graphql-admin/bulk-operations/queries) avoid these limits for large reads and writes.
  * Learn how to [safely retry a request](https://shopify.dev/docs/api/usage/idempotent-requests) that might have failed.


* * *
Was this page helpful?
YesNo
  * [Cost calculation](https://shopify.dev/docs/apps/build/apis/graphql-admin/rate-limits#cost-calculation)
  * [Requested and actual cost](https://shopify.dev/docs/apps/build/apis/graphql-admin/rate-limits#requested-and-actual-cost)
  * [Single query limit](https://shopify.dev/docs/apps/build/apis/graphql-admin/rate-limits#single-query-limit)
  * [Input limits](https://shopify.dev/docs/apps/build/apis/graphql-admin/rate-limits#input-limits)
  * [GraphQL response](https://shopify.dev/docs/apps/build/apis/graphql-admin/rate-limits#graphql-response)
  * [Resource-based rate limits](https://shopify.dev/docs/apps/build/apis/graphql-admin/rate-limits#resource-based-rate-limits)
  * [Bulk operations](https://shopify.dev/docs/apps/build/apis/graphql-admin/rate-limits#bulk-operations)
  * [Avoiding rate limit errors](https://shopify.dev/docs/apps/build/apis/graphql-admin/rate-limits#avoiding-rate-limit-errors)
  * [Next steps](https://shopify.dev/docs/apps/build/apis/graphql-admin/rate-limits#next-steps)


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



