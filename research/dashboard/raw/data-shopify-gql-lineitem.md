[Skip to main content](https://shopify.dev/docs/api/admin-graphql/latest/objects/LineItem#main-content)
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
[Anchor to LineItem](https://shopify.dev/docs/api/admin-graphql/latest/objects/LineItem#top)
# LineItem
object
Install AI ToolkitAsk about this pageCopy MD
Requires `read_orders` access scope, `read_marketplace_orders` access scope or `read_buyer_membership_orders` access scope.
The `LineItem` object represents a single product or service that a customer purchased in an [order](https://shopify.dev/docs/api/admin-graphql/latest/objects/Order). Each line item is associated with a [product variant](https://shopify.dev/docs/api/admin-graphql/latest/objects/ProductVariant) and can have multiple [discount allocations](https://shopify.dev/docs/api/admin-graphql/latest/objects/DiscountAllocation). Line items contain details about what was purchased, including the product variant, quantity, pricing, and fulfillment status.
Use the `LineItem` object to manage the following processes:
  * [Track the quantity of items](https://shopify.dev/docs/apps/build/orders-fulfillment/order-management-apps/build-fulfillment-solutions) ordered, fulfilled, and unfulfilled.
  * [Calculate prices](https://shopify.dev/docs/apps/build/orders-fulfillment/order-management-apps/edit-orders), including discounts and taxes.
  * Manage fulfillment through [fulfillment services](https://shopify.dev/docs/apps/build/orders-fulfillment/fulfillment-service-apps).
  * Manage [returns](https://shopify.dev/docs/apps/build/orders-fulfillment/returns-apps/build-return-management) and [exchanges](https://shopify.dev/docs/apps/build/orders-fulfillment/returns-apps/manage-exchanges).
  * Handle [subscriptions](https://shopify.dev/docs/apps/build/purchase-options/subscriptions) and recurring orders.


Line items can also include custom attributes and properties, allowing merchants to add specific details about each item in an order. Learn more about [managing orders and fulfillment](https://shopify.dev/docs/apps/build/orders-fulfillment).
## 
[Anchor to Fields](https://shopify.dev/docs/api/admin-graphql/latest/objects/LineItem#fields)Fields
  * contract (SubscriptionContract)
  * createdAt (DateTime!)
  * currentQuantity (Int!)
  * customAttributes ([Attribute!]!)
  * discountAllocations ([DiscountAllocation!]!)
  * discountedTotalSet (MoneyBag!)
  * discountedUnitPriceAfterAllDiscountsSet (MoneyBag!)
  * discountedUnitPriceSet (MoneyBag!)
  * duties ([Duty!]!)
  * id (ID!)
  * image (Image)
  * isGiftCard (Boolean!)
  * lineItemGroup (LineItemGroup)
  * merchantEditable (Boolean!)
  * name (String!)
  * nonFulfillableQuantity (Int!)
  * originalTotalSet (MoneyBag!)
  * originalUnitPriceSet (MoneyBag!)
  * priceAfterAllDiscountsBeforeTaxesSet (MoneyBag!)
  * product (Product)
  * quantity (Int!)
  * refundableQuantity (Int!)
  * requiresShipping (Boolean!)
  * restockable (Boolean!)
  * sellingPlan (LineItemSellingPlan)
  * sku (String)
  * staffMember (StaffMember)
  * suggestedReturnReasonDefinitions (ReturnReasonDefinitionConnection)
  * taxable (Boolean!)
  * taxLines ([TaxLine!]!)
  * title (String!)
  * totalDiscountSet (MoneyBag!)
  * unfulfilledDiscountedTotalSet (MoneyBag!)
  * unfulfilledOriginalTotalSet (MoneyBag!)
  * unfulfilledQuantity (Int!)
  * variant (ProductVariant)
  * variantTitle (String)
  * vendor (String)
  * weight (Weight)


[Anchor to contract](https://shopify.dev/docs/api/admin-graphql/latest/objects/LineItem#field-LineItem.fields.contract)contract
•[SubscriptionContract](https://shopify.dev/docs/api/admin-graphql/latest/objects/SubscriptionContract) 
    
The subscription contract associated with this line item.
Show fields
[Anchor to createdAt](https://shopify.dev/docs/api/admin-graphql/latest/objects/LineItem#field-LineItem.fields.createdAt)createdAt
•[DateTime!](https://shopify.dev/docs/api/admin-graphql/latest/scalars/DateTime)
non-null

    
The date and time when the line item was created.
[Anchor to currentQuantity](https://shopify.dev/docs/api/admin-graphql/latest/objects/LineItem#field-LineItem.fields.currentQuantity)currentQuantity
•[Int!](https://shopify.dev/docs/api/admin-graphql/latest/scalars/Int)
non-null

    
The number of units ordered, excluding refunded and removed units.
[Anchor to customAttributes](https://shopify.dev/docs/api/admin-graphql/latest/objects/LineItem#field-LineItem.fields.customAttributes)customAttributes
•[[Attribute!]!](https://shopify.dev/docs/api/admin-graphql/latest/objects/Attribute)
non-null

    
A list of attributes that represent custom features or special requests.
Show fields
[Anchor to discountAllocations](https://shopify.dev/docs/api/admin-graphql/latest/objects/LineItem#field-LineItem.fields.discountAllocations)discountAllocations
•[[DiscountAllocation!]!](https://shopify.dev/docs/api/admin-graphql/latest/objects/DiscountAllocation)
non-null

    
The discounts that have been allocated to the line item by discount applications, including discounts allocated to refunded and removed quantities.
Show fields
[Anchor to discountedTotalSet](https://shopify.dev/docs/api/admin-graphql/latest/objects/LineItem#field-LineItem.fields.discountedTotalSet)discountedTotalSet
•[MoneyBag!](https://shopify.dev/docs/api/admin-graphql/latest/objects/MoneyBag)
non-null

    
The total discounted price of the line item in shop and presentment currencies, including refunded and removed quantities. This value doesn't include order-level discounts. Code-based discounts aren't included by default.
Show fields
### Arguments
[Anchor to withCodeDiscounts](https://shopify.dev/docs/api/admin-graphql/latest/objects/LineItem#field-LineItem.fields.discountedTotalSet.arguments.withCodeDiscounts)withCodeDiscounts
•[Boolean](https://shopify.dev/docs/api/admin-graphql/latest/scalars/Boolean)
Default:false

    
Whether to include code-based discounts in the total.
* * *
[Anchor to discountedUnitPriceAfterAllDiscountsSet](https://shopify.dev/docs/api/admin-graphql/latest/objects/LineItem#field-LineItem.fields.discountedUnitPriceAfterAllDiscountsSet)discountedUnitPriceAfterAllDiscountsSet
•[MoneyBag!](https://shopify.dev/docs/api/admin-graphql/latest/objects/MoneyBag)
non-null

    
The approximate unit price of the line item in shop and presentment currencies. This value includes discounts applied to refunded and removed quantities.
Show fields
[Anchor to discountedUnitPriceSet](https://shopify.dev/docs/api/admin-graphql/latest/objects/LineItem#field-LineItem.fields.discountedUnitPriceSet)discountedUnitPriceSet
•[MoneyBag!](https://shopify.dev/docs/api/admin-graphql/latest/objects/MoneyBag)
non-null

    
The approximate unit price of the line item in shop and presentment currencies. This value includes line-level discounts and discounts applied to refunded and removed quantities. It doesn't include order-level or code-based discounts.
Show fields
[Anchor to duties](https://shopify.dev/docs/api/admin-graphql/latest/objects/LineItem#field-LineItem.fields.duties)duties
•[[Duty!]!](https://shopify.dev/docs/api/admin-graphql/latest/objects/Duty)
non-null

    
The duties associated with the line item.
Show fields
[Anchor to id](https://shopify.dev/docs/api/admin-graphql/latest/objects/LineItem#field-LineItem.fields.id)id
•[ID!](https://shopify.dev/docs/api/admin-graphql/latest/scalars/ID)
non-null

    
A globally-unique ID.
[Anchor to image](https://shopify.dev/docs/api/admin-graphql/latest/objects/LineItem#field-LineItem.fields.image)image
•[Image](https://shopify.dev/docs/api/admin-graphql/latest/objects/Image) 
    
The image associated to the line item's variant.
Show fields
### Arguments
[Anchor to crop](https://shopify.dev/docs/api/admin-graphql/latest/objects/LineItem#field-LineItem.fields.image.arguments.crop)crop
•[CropRegion](https://shopify.dev/docs/api/admin-graphql/latest/enums/CropRegion)
Deprecated

    
Show enum values
[Anchor to maxHeight](https://shopify.dev/docs/api/admin-graphql/latest/objects/LineItem#field-LineItem.fields.image.arguments.maxHeight)maxHeight
•[Int](https://shopify.dev/docs/api/admin-graphql/latest/scalars/Int)
Deprecated


[Anchor to maxWidth](https://shopify.dev/docs/api/admin-graphql/latest/objects/LineItem#field-LineItem.fields.image.arguments.maxWidth)maxWidth
•[Int](https://shopify.dev/docs/api/admin-graphql/latest/scalars/Int)
Deprecated


[Anchor to scale](https://shopify.dev/docs/api/admin-graphql/latest/objects/LineItem#field-LineItem.fields.image.arguments.scale)scale
•[Int](https://shopify.dev/docs/api/admin-graphql/latest/scalars/Int)
DeprecatedDefault:1


* * *
[Anchor to isGiftCard](https://shopify.dev/docs/api/admin-graphql/latest/objects/LineItem#field-LineItem.fields.isGiftCard)isGiftCard
•[Boolean!](https://shopify.dev/docs/api/admin-graphql/latest/scalars/Boolean)
non-null

    
Whether the line item represents the purchase of a gift card.
[Anchor to lineItemGroup](https://shopify.dev/docs/api/admin-graphql/latest/objects/LineItem#field-LineItem.fields.lineItemGroup)lineItemGroup
•[LineItemGroup](https://shopify.dev/docs/api/admin-graphql/latest/objects/LineItemGroup) 
    
The line item group associated to the line item.
Show fields
[Anchor to merchantEditable](https://shopify.dev/docs/api/admin-graphql/latest/objects/LineItem#field-LineItem.fields.merchantEditable)merchantEditable
•[Boolean!](https://shopify.dev/docs/api/admin-graphql/latest/scalars/Boolean)
non-null

    
Whether the line item can be edited or not.
[Anchor to name](https://shopify.dev/docs/api/admin-graphql/latest/objects/LineItem#field-LineItem.fields.name)name
•[String!](https://shopify.dev/docs/api/admin-graphql/latest/scalars/String)
non-null

    
The title of the product, optionally appended with the title of the variant (if applicable).
[Anchor to nonFulfillableQuantity](https://shopify.dev/docs/api/admin-graphql/latest/objects/LineItem#field-LineItem.fields.nonFulfillableQuantity)nonFulfillableQuantity
•[Int!](https://shopify.dev/docs/api/admin-graphql/latest/scalars/Int)
non-null

    
The total number of units that can't be fulfilled. For example, if items have been refunded, or the item is not something that can be fulfilled, like a tip. Please see the [FulfillmentOrder](https://shopify.dev/api/admin-graphql/latest/objects/FulfillmentOrder) object for more fulfillment details.
[Anchor to originalTotalSet](https://shopify.dev/docs/api/admin-graphql/latest/objects/LineItem#field-LineItem.fields.originalTotalSet)originalTotalSet
•[MoneyBag!](https://shopify.dev/docs/api/admin-graphql/latest/objects/MoneyBag)
non-null

    
In shop and presentment currencies, the total price of the line item when the order was created. This value doesn't include discounts.
Show fields
[Anchor to originalUnitPriceSet](https://shopify.dev/docs/api/admin-graphql/latest/objects/LineItem#field-LineItem.fields.originalUnitPriceSet)originalUnitPriceSet
•[MoneyBag!](https://shopify.dev/docs/api/admin-graphql/latest/objects/MoneyBag)
non-null

    
In shop and presentment currencies, the unit price of the line item when the order was created. This value doesn't include discounts.
Show fields
[Anchor to priceAfterAllDiscountsBeforeTaxesSet](https://shopify.dev/docs/api/admin-graphql/latest/objects/LineItem#field-LineItem.fields.priceAfterAllDiscountsBeforeTaxesSet)priceAfterAllDiscountsBeforeTaxesSet
•[MoneyBag!](https://shopify.dev/docs/api/admin-graphql/latest/objects/MoneyBag)
non-null

    
The total price of the line item in shop and presentment currencies, after all discounts are applied and excluding refunded and removed quantities. This value doesn't include taxes.
Show fields
[Anchor to product](https://shopify.dev/docs/api/admin-graphql/latest/objects/LineItem#field-LineItem.fields.product)product
•[Product](https://shopify.dev/docs/api/admin-graphql/latest/objects/Product) 
    
The Product object associated with this line item's variant.
Show fields
[Anchor to quantity](https://shopify.dev/docs/api/admin-graphql/latest/objects/LineItem#field-LineItem.fields.quantity)quantity
•[Int!](https://shopify.dev/docs/api/admin-graphql/latest/scalars/Int)
non-null

    
The number of units ordered, including refunded and removed units.
[Anchor to refundableQuantity](https://shopify.dev/docs/api/admin-graphql/latest/objects/LineItem#field-LineItem.fields.refundableQuantity)refundableQuantity
•[Int!](https://shopify.dev/docs/api/admin-graphql/latest/scalars/Int)
non-null

    
The number of units ordered, excluding refunded units and removed units.
[Anchor to requiresShipping](https://shopify.dev/docs/api/admin-graphql/latest/objects/LineItem#field-LineItem.fields.requiresShipping)requiresShipping
•[Boolean!](https://shopify.dev/docs/api/admin-graphql/latest/scalars/Boolean)
non-null

    
Whether physical shipping is required for the variant.
[Anchor to restockable](https://shopify.dev/docs/api/admin-graphql/latest/objects/LineItem#field-LineItem.fields.restockable)restockable
•[Boolean!](https://shopify.dev/docs/api/admin-graphql/latest/scalars/Boolean)
non-null

    
Whether the line item can be restocked.
[Anchor to sellingPlan](https://shopify.dev/docs/api/admin-graphql/latest/objects/LineItem#field-LineItem.fields.sellingPlan)sellingPlan
•[LineItemSellingPlan](https://shopify.dev/docs/api/admin-graphql/latest/objects/LineItemSellingPlan) 
    
The selling plan details associated with the line item.
Show fields
[Anchor to sku](https://shopify.dev/docs/api/admin-graphql/latest/objects/LineItem#field-LineItem.fields.sku)sku
•[String](https://shopify.dev/docs/api/admin-graphql/latest/scalars/String) 
    
The variant SKU number.
[Anchor to staffMember](https://shopify.dev/docs/api/admin-graphql/latest/objects/LineItem#field-LineItem.fields.staffMember)staffMember
•[StaffMember](https://shopify.dev/docs/api/admin-graphql/latest/objects/StaffMember) 
    
Staff attributed to the line item.
Show fields
[Anchor to suggestedReturnReasonDefinitions](https://shopify.dev/docs/api/admin-graphql/latest/objects/LineItem#field-LineItem.fields.suggestedReturnReasonDefinitions)suggestedReturnReasonDefinitions
•[ReturnReasonDefinitionConnection](https://shopify.dev/docs/api/admin-graphql/latest/connections/ReturnReasonDefinitionConnection) 
    
Return reasons suggested based on the line item's product category in Shopify's product taxonomy. Use [`returnReasonDefinitions`](https://shopify.dev/docs/api/admin-graphql/latest/queries/returnReasonDefinitions) to access the full library of available reasons.
Show fields
### Arguments
[Anchor to after](https://shopify.dev/docs/api/admin-graphql/latest/objects/LineItem#field-LineItem.fields.suggestedReturnReasonDefinitions.arguments.after)after
•[String](https://shopify.dev/docs/api/admin-graphql/latest/scalars/String) 
    
The elements that come after the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).
[Anchor to before](https://shopify.dev/docs/api/admin-graphql/latest/objects/LineItem#field-LineItem.fields.suggestedReturnReasonDefinitions.arguments.before)before
•[String](https://shopify.dev/docs/api/admin-graphql/latest/scalars/String) 
    
The elements that come before the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).
[Anchor to first](https://shopify.dev/docs/api/admin-graphql/latest/objects/LineItem#field-LineItem.fields.suggestedReturnReasonDefinitions.arguments.first)first
•[Int](https://shopify.dev/docs/api/admin-graphql/latest/scalars/Int) 
    
The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).
[Anchor to last](https://shopify.dev/docs/api/admin-graphql/latest/objects/LineItem#field-LineItem.fields.suggestedReturnReasonDefinitions.arguments.last)last
•[Int](https://shopify.dev/docs/api/admin-graphql/latest/scalars/Int) 
    
The last `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).
[Anchor to reverse](https://shopify.dev/docs/api/admin-graphql/latest/objects/LineItem#field-LineItem.fields.suggestedReturnReasonDefinitions.arguments.reverse)reverse
•[Boolean](https://shopify.dev/docs/api/admin-graphql/latest/scalars/Boolean)
Default:false

    
Reverse the order of the underlying list.
* * *
[Anchor to taxable](https://shopify.dev/docs/api/admin-graphql/latest/objects/LineItem#field-LineItem.fields.taxable)taxable
•[Boolean!](https://shopify.dev/docs/api/admin-graphql/latest/scalars/Boolean)
non-null

    
Whether the variant is taxable.
[Anchor to taxLines](https://shopify.dev/docs/api/admin-graphql/latest/objects/LineItem#field-LineItem.fields.taxLines)taxLines
•[[TaxLine!]!](https://shopify.dev/docs/api/admin-graphql/latest/objects/TaxLine)
non-null

    
The taxes charged for the line item, including taxes charged for refunded and removed quantities.
Show fields
### Arguments
[Anchor to first](https://shopify.dev/docs/api/admin-graphql/latest/objects/LineItem#field-LineItem.fields.taxLines.arguments.first)first
•[Int](https://shopify.dev/docs/api/admin-graphql/latest/scalars/Int) 
    
Truncate the array result to this size.
* * *
[Anchor to title](https://shopify.dev/docs/api/admin-graphql/latest/objects/LineItem#field-LineItem.fields.title)title
•[String!](https://shopify.dev/docs/api/admin-graphql/latest/scalars/String)
non-null

    
The title of the product at time of order creation.
[Anchor to totalDiscountSet](https://shopify.dev/docs/api/admin-graphql/latest/objects/LineItem#field-LineItem.fields.totalDiscountSet)totalDiscountSet
•[MoneyBag!](https://shopify.dev/docs/api/admin-graphql/latest/objects/MoneyBag)
non-null

    
The total discount allocated to the line item in shop and presentment currencies, including the total allocated to refunded and removed quantities. This value doesn't include order-level discounts.
Show fields
[Anchor to unfulfilledDiscountedTotalSet](https://shopify.dev/docs/api/admin-graphql/latest/objects/LineItem#field-LineItem.fields.unfulfilledDiscountedTotalSet)unfulfilledDiscountedTotalSet
•[MoneyBag!](https://shopify.dev/docs/api/admin-graphql/latest/objects/MoneyBag)
non-null

    
In shop and presentment currencies, the total discounted price of the unfulfilled quantity for the line item.
Show fields
[Anchor to unfulfilledOriginalTotalSet](https://shopify.dev/docs/api/admin-graphql/latest/objects/LineItem#field-LineItem.fields.unfulfilledOriginalTotalSet)unfulfilledOriginalTotalSet
•[MoneyBag!](https://shopify.dev/docs/api/admin-graphql/latest/objects/MoneyBag)
non-null

    
In shop and presentment currencies, the total price of the unfulfilled quantity for the line item. This value doesn't include discounts.
Show fields
[Anchor to unfulfilledQuantity](https://shopify.dev/docs/api/admin-graphql/latest/objects/LineItem#field-LineItem.fields.unfulfilledQuantity)unfulfilledQuantity
•[Int!](https://shopify.dev/docs/api/admin-graphql/latest/scalars/Int)
non-null

    
The number of units not yet fulfilled.
[Anchor to variant](https://shopify.dev/docs/api/admin-graphql/latest/objects/LineItem#field-LineItem.fields.variant)variant
•[ProductVariant](https://shopify.dev/docs/api/admin-graphql/latest/objects/ProductVariant) 
    
The Variant object associated with this line item.
Show fields
[Anchor to variantTitle](https://shopify.dev/docs/api/admin-graphql/latest/objects/LineItem#field-LineItem.fields.variantTitle)variantTitle
•[String](https://shopify.dev/docs/api/admin-graphql/latest/scalars/String) 
    
The title of the variant at time of order creation.
[Anchor to vendor](https://shopify.dev/docs/api/admin-graphql/latest/objects/LineItem#field-LineItem.fields.vendor)vendor
•[String](https://shopify.dev/docs/api/admin-graphql/latest/scalars/String) 
    
The name of the vendor who made the variant.
[Anchor to weight](https://shopify.dev/docs/api/admin-graphql/latest/objects/LineItem#field-LineItem.fields.weight)weight
•[Weight](https://shopify.dev/docs/api/admin-graphql/latest/objects/Weight) 
    
The weight of a line item unit.
Show fields
### Deprecated fields
  * canRestock (Boolean!): deprecated
  * discountedTotal (Money!): deprecated
  * discountedUnitPrice (Money!): deprecated
  * fulfillableQuantity (Int!): deprecated
  * fulfillmentService (FulfillmentService): deprecated
  * fulfillmentStatus (String!): deprecated
  * originalTotal (Money!): deprecated
  * originalUnitPrice (Money!): deprecated
  * totalDiscount (Money!): deprecated
  * unfulfilledDiscountedTotal (Money!): deprecated
  * unfulfilledOriginalTotal (Money!): deprecated


[Anchor to canRestock](https://shopify.dev/docs/api/admin-graphql/latest/objects/LineItem#field-LineItem.fields.canRestock)canRestock
•[Boolean!](https://shopify.dev/docs/api/admin-graphql/latest/scalars/Boolean)
non-nullDeprecated


[Anchor to discountedTotal](https://shopify.dev/docs/api/admin-graphql/latest/objects/LineItem#field-LineItem.fields.discountedTotal)discountedTotal
•[Money!](https://shopify.dev/docs/api/admin-graphql/latest/scalars/Money)
non-nullDeprecated


[Anchor to discountedUnitPrice](https://shopify.dev/docs/api/admin-graphql/latest/objects/LineItem#field-LineItem.fields.discountedUnitPrice)discountedUnitPrice
•[Money!](https://shopify.dev/docs/api/admin-graphql/latest/scalars/Money)
non-nullDeprecated


[Anchor to fulfillableQuantity](https://shopify.dev/docs/api/admin-graphql/latest/objects/LineItem#field-LineItem.fields.fulfillableQuantity)fulfillableQuantity
•[Int!](https://shopify.dev/docs/api/admin-graphql/latest/scalars/Int)
non-nullDeprecated


[Anchor to fulfillmentService](https://shopify.dev/docs/api/admin-graphql/latest/objects/LineItem#field-LineItem.fields.fulfillmentService)fulfillmentService
•[FulfillmentService](https://shopify.dev/docs/api/admin-graphql/latest/objects/FulfillmentService)
Deprecated

    
Show fields
[Anchor to fulfillmentStatus](https://shopify.dev/docs/api/admin-graphql/latest/objects/LineItem#field-LineItem.fields.fulfillmentStatus)fulfillmentStatus
•[String!](https://shopify.dev/docs/api/admin-graphql/latest/scalars/String)
non-nullDeprecated


[Anchor to originalTotal](https://shopify.dev/docs/api/admin-graphql/latest/objects/LineItem#field-LineItem.fields.originalTotal)originalTotal
•[Money!](https://shopify.dev/docs/api/admin-graphql/latest/scalars/Money)
non-nullDeprecated


[Anchor to originalUnitPrice](https://shopify.dev/docs/api/admin-graphql/latest/objects/LineItem#field-LineItem.fields.originalUnitPrice)originalUnitPrice
•[Money!](https://shopify.dev/docs/api/admin-graphql/latest/scalars/Money)
non-nullDeprecated


[Anchor to totalDiscount](https://shopify.dev/docs/api/admin-graphql/latest/objects/LineItem#field-LineItem.fields.totalDiscount)totalDiscount
•[Money!](https://shopify.dev/docs/api/admin-graphql/latest/scalars/Money)
non-nullDeprecated


[Anchor to unfulfilledDiscountedTotal](https://shopify.dev/docs/api/admin-graphql/latest/objects/LineItem#field-LineItem.fields.unfulfilledDiscountedTotal)unfulfilledDiscountedTotal
•[Money!](https://shopify.dev/docs/api/admin-graphql/latest/scalars/Money)
non-nullDeprecated


[Anchor to unfulfilledOriginalTotal](https://shopify.dev/docs/api/admin-graphql/latest/objects/LineItem#field-LineItem.fields.unfulfilledOriginalTotal)unfulfilledOriginalTotal
•[Money!](https://shopify.dev/docs/api/admin-graphql/latest/scalars/Money)
non-nullDeprecated


* * *
Was this section helpful?
YesNo
## Map
### Fields and connections with this object
  * {}[CalculatedRequestedOrderEditLineItem.lineItem](https://shopify.dev/docs/api/admin-graphql/latest/objects/CalculatedRequestedOrderEditLineItem#field-CalculatedRequestedOrderEditLineItem.fields.lineItem)
  * {}[ExchangeLineItem.lineItems](https://shopify.dev/docs/api/admin-graphql/latest/objects/ExchangeLineItem#field-ExchangeLineItem.fields.lineItems)
  * {}[FulfillmentLineItem.lineItem](https://shopify.dev/docs/api/admin-graphql/latest/objects/FulfillmentLineItem#field-FulfillmentLineItem.fields.lineItem)
  * {}[FulfillmentOrderLineItem.lineItem](https://shopify.dev/docs/api/admin-graphql/latest/objects/FulfillmentOrderLineItem#field-FulfillmentOrderLineItem.fields.lineItem)
  * {}[GiftCard.lineItem](https://shopify.dev/docs/api/admin-graphql/latest/objects/GiftCard#field-GiftCard.fields.lineItem)
  * {}[GiftCardSale.lineItem](https://shopify.dev/docs/api/admin-graphql/latest/objects/GiftCardSale#field-GiftCardSale.fields.lineItem)
  * <->[LineItemConnection.nodes](https://shopify.dev/docs/api/admin-graphql/latest/connections/LineItemConnection#returns-nodes)
  * {}[LineItemEdge.node](https://shopify.dev/docs/api/admin-graphql/latest/objects/LineItemEdge#field-LineItemEdge.fields.node)
  * {}[Order.lineItems](https://shopify.dev/docs/api/admin-graphql/latest/objects/Order#field-Order.fields.lineItems)
  * {}[Order.nonFulfillableLineItems](https://shopify.dev/docs/api/admin-graphql/latest/objects/Order#field-Order.fields.nonFulfillableLineItems)
  * {}[OrderStagedChangeDecrementItem.lineItem](https://shopify.dev/docs/api/admin-graphql/latest/objects/OrderStagedChangeDecrementItem#field-OrderStagedChangeDecrementItem.fields.lineItem)
  * {}[OrderStagedChangeIncrementItem.lineItem](https://shopify.dev/docs/api/admin-graphql/latest/objects/OrderStagedChangeIncrementItem#field-OrderStagedChangeIncrementItem.fields.lineItem)
  * {}[ProductSale.lineItem](https://shopify.dev/docs/api/admin-graphql/latest/objects/ProductSale#field-ProductSale.fields.lineItem)
  * {}[RefundLineItem.lineItem](https://shopify.dev/docs/api/admin-graphql/latest/objects/RefundLineItem#field-RefundLineItem.fields.lineItem)
  * {}[RequestedOrderEditLineItem.lineItem](https://shopify.dev/docs/api/admin-graphql/latest/objects/RequestedOrderEditLineItem#field-RequestedOrderEditLineItem.fields.lineItem)
  * {}[TipSale.lineItem](https://shopify.dev/docs/api/admin-graphql/latest/objects/TipSale#field-TipSale.fields.lineItem)

Show deprecations
* * *
## 
[Anchor to Interfaces](https://shopify.dev/docs/api/admin-graphql/latest/objects/LineItem#interfaces)Interfaces
  * Node


[Anchor to Node](https://shopify.dev/docs/api/admin-graphql/latest/objects/LineItem#interface-Node)[Node](https://shopify.dev/docs/api/admin-graphql/latest/interfaces/Node)
•interface 

* * *
Was this section helpful?
YesNo
##  ||-LineItem Implements
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



