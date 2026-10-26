[Skip to main content](https://shopify.dev/docs/api/admin-graphql/latest/objects/TransactionFee#main-content)
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
[Back to all APIsGraphQL Admin API](https://shopify.dev/docs/api)
Choose a version:
unstable 2027-01 release candidate 2026-10 latest 2026-07 2026-04 2026-01
2026-10latest
  * [Overview](https://shopify.dev/docs/api/admin-graphql/2026-10)
  * [Client libraries](https://shopify.dev/docs/api/admin-graphql/2026-10#client-libraries)
  * [Authentication](https://shopify.dev/docs/api/admin-graphql/2026-10#authentication)
  * [Endpoints and queries](https://shopify.dev/docs/api/admin-graphql/2026-10#endpoints-and-queries)
  * [Rate limits](https://shopify.dev/docs/api/admin-graphql/2026-10#rate-limits)
  * [Status and error codes](https://shopify.dev/docs/api/admin-graphql/2026-10#status-and-error-codes)


* * *
  * Access
  * Analytics
  * Apps
  * B2B
  * Billing
  * Bulk operations
  * Cart
  * Checkout and accounts configurations
  * Checkout branding
  * Common objects
  * Customers
  * Discounts and marketing
  * Inventory
  * Localizations
  * Metafields
  * Metaobjects
  * Online store
  * Orders
  * Privacy
  * Products and collections
  * Retail
  * Shipping and fulfillment
  * Shopify Markets
  * Shopify Payments
  * Store properties
  * Timeline events
  * Webhooks
  * * * *
  * GraphQL Types


[Full index](https://shopify.dev/docs/api/admin-graphql/2026-10/full-index)
Choose a version:
unstable 2027-01 release candidate 2026-10 latest 2026-07 2026-04 2026-01
2026-10latest
[Anchor to TransactionFee](https://shopify.dev/docs/api/admin-graphql/latest/objects/TransactionFee#top)
# TransactionFee
object
Install AI ToolkitAsk about this pageCopy MD
Requires `read_orders` access scope.
Transaction fee related to an order transaction.
## 
[Anchor to Fields](https://shopify.dev/docs/api/admin-graphql/latest/objects/TransactionFee#fields)Fields
  * amount (MoneyV2!)
  * createdAt (DateTime!)
  * flatFee (MoneyV2!)
  * flatFeeName (String)
  * id (ID!)
  * rate (Decimal!)
  * rateName (String)
  * taxAmount (MoneyV2!)
  * type (String!)


[Anchor to amount](https://shopify.dev/docs/api/admin-graphql/latest/objects/TransactionFee#field-TransactionFee.fields.amount)amount
•[MoneyV2!](https://shopify.dev/docs/api/admin-graphql/latest/objects/MoneyV2)
non-null

    
Amount of the fee.
Show fields
[Anchor to createdAt](https://shopify.dev/docs/api/admin-graphql/latest/objects/TransactionFee#field-TransactionFee.fields.createdAt)createdAt
•[DateTime!](https://shopify.dev/docs/api/admin-graphql/latest/scalars/DateTime)
non-null

    
The date and time when the transaction fee was created.
[Anchor to flatFee](https://shopify.dev/docs/api/admin-graphql/latest/objects/TransactionFee#field-TransactionFee.fields.flatFee)flatFee
•[MoneyV2!](https://shopify.dev/docs/api/admin-graphql/latest/objects/MoneyV2)
non-null

    
Flat rate charge for a transaction.
Show fields
[Anchor to flatFeeName](https://shopify.dev/docs/api/admin-graphql/latest/objects/TransactionFee#field-TransactionFee.fields.flatFeeName)flatFeeName
•[String](https://shopify.dev/docs/api/admin-graphql/latest/scalars/String) 
    
Name of the credit card flat fee.
[Anchor to id](https://shopify.dev/docs/api/admin-graphql/latest/objects/TransactionFee#field-TransactionFee.fields.id)id
•[ID!](https://shopify.dev/docs/api/admin-graphql/latest/scalars/ID)
non-null

    
A globally-unique ID.
[Anchor to rate](https://shopify.dev/docs/api/admin-graphql/latest/objects/TransactionFee#field-TransactionFee.fields.rate)rate
•[Decimal!](https://shopify.dev/docs/api/admin-graphql/latest/scalars/Decimal)
non-null

    
Percentage charge.
[Anchor to rateName](https://shopify.dev/docs/api/admin-graphql/latest/objects/TransactionFee#field-TransactionFee.fields.rateName)rateName
•[String](https://shopify.dev/docs/api/admin-graphql/latest/scalars/String) 
    
Name of the credit card rate.
[Anchor to taxAmount](https://shopify.dev/docs/api/admin-graphql/latest/objects/TransactionFee#field-TransactionFee.fields.taxAmount)taxAmount
•[MoneyV2!](https://shopify.dev/docs/api/admin-graphql/latest/objects/MoneyV2)
non-null

    
Tax amount charged on the fee.
Show fields
[Anchor to type](https://shopify.dev/docs/api/admin-graphql/latest/objects/TransactionFee#field-TransactionFee.fields.type)type
•[String!](https://shopify.dev/docs/api/admin-graphql/latest/scalars/String)
non-null

    
Name of the type of fee.
* * *
Was this section helpful?
YesNo
## Map
### Fields with this object
  * {}[OrderTransaction.fees](https://shopify.dev/docs/api/admin-graphql/latest/objects/OrderTransaction#field-OrderTransaction.fields.fees)


* * *
## 
[Anchor to Interfaces](https://shopify.dev/docs/api/admin-graphql/latest/objects/TransactionFee#interfaces)Interfaces
  * Node


[Anchor to Node](https://shopify.dev/docs/api/admin-graphql/latest/objects/TransactionFee#interface-Node)[Node](https://shopify.dev/docs/api/admin-graphql/latest/interfaces/Node)
•interface 

* * *
Was this section helpful?
YesNo
##  ||-TransactionFee Implements
### Implements
  * ||-[Node](https://shopify.dev/docs/api/admin-graphql/latest/interfaces/Node)


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



