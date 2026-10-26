[Skip to main content](https://shopify.dev/docs/api/admin-graphql/latest/objects/OrderTransaction#main-content)
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
[Anchor to OrderTransaction](https://shopify.dev/docs/api/admin-graphql/latest/objects/OrderTransaction#top)
# OrderTransaction
object
Install AI ToolkitAsk about this pageCopy MD
Requires `read_orders` access scope, `read_marketplace_orders` access scope or `read_buyer_membership_orders` access scope.
The `OrderTransaction` object represents a payment transaction that's associated with an order. An order transaction is a specific action or event that happens within the context of an order, such as a customer paying for a purchase or receiving a refund, or other payment-related activity.
Use the `OrderTransaction` object to capture the complete lifecycle of a payment, from initial authorization to final settlement, including refunds and currency exchanges. Common use cases for using the `OrderTransaction` object include:
  * Processing new payments for orders
  * Managing payment authorizations and captures
  * Processing refunds for returned items
  * Tracking payment status and errors
  * Managing multi-currency transactions
  * Handling payment gateway integrations


Each `OrderTransaction` object has a [`kind`](https://shopify.dev/docs/api/admin-graphql/latest/enums/OrderTransactionKind) that defines the type of transaction and a [`status`](https://shopify.dev/docs/api/admin-graphql/latest/enums/OrderTransactionStatus) that indicates the current state of the transaction. The object stores detailed information about payment methods, gateway processing, and settlement details.
Learn more about [payment processing](https://help.shopify.com/manual/payments) and [payment gateway integrations](https://www.shopify.com/ca/payment-gateways).
## 
[Anchor to Fields](https://shopify.dev/docs/api/admin-graphql/latest/objects/OrderTransaction#fields)Fields
  * accountNumber (String)
  * amountRoundingSet (MoneyBag)
  * amountSet (MoneyBag!)
  * authorizationExpiresAt (DateTime)
  * createdAt (DateTime!)
  * currencyExchangeAdjustment (CurrencyExchangeAdjustment)
  * device (PointOfSaleDevice)
  * errorCode (OrderTransactionErrorCode)
  * fees ([TransactionFee!]!)
  * formattedGateway (String)
  * gateway (String)
  * id (ID!)
  * kind (OrderTransactionKind!)
  * location (Location)
  * manuallyCapturable (Boolean!)
  * manualPaymentGateway (Boolean!)
  * maximumRefundableV2 (MoneyV2)
  * multiCapturable (Boolean!)
  * order (Order)
  * parentTransaction (OrderTransaction)
  * paymentDetails (PaymentDetails)
  * paymentIcon (Image)
  * paymentId (String)
  * processedAt (DateTime)
  * receiptJson (JSON)
  * settlementCurrency (CurrencyCode)
  * settlementCurrencyRate (Decimal)
  * shopifyPaymentsSet (ShopifyPaymentsTransactionSet)
  * status (OrderTransactionStatus!)
  * test (Boolean!)
  * totalUnsettledSet (MoneyBag)
  * user (StaffMember)


[Anchor to accountNumber](https://shopify.dev/docs/api/admin-graphql/latest/objects/OrderTransaction#field-OrderTransaction.fields.accountNumber)accountNumber
•[String](https://shopify.dev/docs/api/admin-graphql/latest/scalars/String) 
    
The masked account number associated with the payment method.
[Anchor to amountRoundingSet](https://shopify.dev/docs/api/admin-graphql/latest/objects/OrderTransaction#field-OrderTransaction.fields.amountRoundingSet)amountRoundingSet
•[MoneyBag](https://shopify.dev/docs/api/admin-graphql/latest/objects/MoneyBag) 
    
The rounding adjustment applied on the cash amount in shop and presentment currencies.
Show fields
[Anchor to amountSet](https://shopify.dev/docs/api/admin-graphql/latest/objects/OrderTransaction#field-OrderTransaction.fields.amountSet)amountSet
•[MoneyBag!](https://shopify.dev/docs/api/admin-graphql/latest/objects/MoneyBag)
non-null

    
The amount and currency of the transaction in shop and presentment currencies.
Show fields
[Anchor to authorizationExpiresAt](https://shopify.dev/docs/api/admin-graphql/latest/objects/OrderTransaction#field-OrderTransaction.fields.authorizationExpiresAt)authorizationExpiresAt
•[DateTime](https://shopify.dev/docs/api/admin-graphql/latest/scalars/DateTime) 
    
The time when the authorization expires. This field is available only to stores on a Shopify Plus plan.
[Anchor to createdAt](https://shopify.dev/docs/api/admin-graphql/latest/objects/OrderTransaction#field-OrderTransaction.fields.createdAt)createdAt
•[DateTime!](https://shopify.dev/docs/api/admin-graphql/latest/scalars/DateTime)
non-null

    
Date and time when the transaction was created.
[Anchor to currencyExchangeAdjustment](https://shopify.dev/docs/api/admin-graphql/latest/objects/OrderTransaction#field-OrderTransaction.fields.currencyExchangeAdjustment)currencyExchangeAdjustment
•[CurrencyExchangeAdjustment](https://shopify.dev/docs/api/admin-graphql/latest/objects/CurrencyExchangeAdjustment) 
    
An adjustment on the transaction showing the amount lost or gained due to fluctuations in the currency exchange rate.
Show fields
[Anchor to device](https://shopify.dev/docs/api/admin-graphql/latest/objects/OrderTransaction#field-OrderTransaction.fields.device)device
•[PointOfSaleDevice](https://shopify.dev/docs/api/admin-graphql/latest/objects/PointOfSaleDevice) 
    
The Shopify Point of Sale device used to process the transaction.
Show fields
[Anchor to errorCode](https://shopify.dev/docs/api/admin-graphql/latest/objects/OrderTransaction#field-OrderTransaction.fields.errorCode)errorCode
•[OrderTransactionErrorCode](https://shopify.dev/docs/api/admin-graphql/latest/enums/OrderTransactionErrorCode) 
    
A standardized error code, independent of the payment provider.
Show enum values
[Anchor to fees](https://shopify.dev/docs/api/admin-graphql/latest/objects/OrderTransaction#field-OrderTransaction.fields.fees)fees
•[[TransactionFee!]!](https://shopify.dev/docs/api/admin-graphql/latest/objects/TransactionFee)
non-null

    
The transaction fees charged on the order transaction. Only present for Shopify Payments transactions.
Show fields
[Anchor to formattedGateway](https://shopify.dev/docs/api/admin-graphql/latest/objects/OrderTransaction#field-OrderTransaction.fields.formattedGateway)formattedGateway
•[String](https://shopify.dev/docs/api/admin-graphql/latest/scalars/String) 
    
The human-readable payment gateway name used to process the transaction.
[Anchor to gateway](https://shopify.dev/docs/api/admin-graphql/latest/objects/OrderTransaction#field-OrderTransaction.fields.gateway)gateway
•[String](https://shopify.dev/docs/api/admin-graphql/latest/scalars/String) 
    
The payment gateway used to process the transaction.
[Anchor to id](https://shopify.dev/docs/api/admin-graphql/latest/objects/OrderTransaction#field-OrderTransaction.fields.id)id
•[ID!](https://shopify.dev/docs/api/admin-graphql/latest/scalars/ID)
non-null

    
A globally-unique ID.
[Anchor to kind](https://shopify.dev/docs/api/admin-graphql/latest/objects/OrderTransaction#field-OrderTransaction.fields.kind)kind
•[OrderTransactionKind!](https://shopify.dev/docs/api/admin-graphql/latest/enums/OrderTransactionKind)
non-null

    
The kind of transaction.
Show enum values
[Anchor to location](https://shopify.dev/docs/api/admin-graphql/latest/objects/OrderTransaction#field-OrderTransaction.fields.location)location
•[Location](https://shopify.dev/docs/api/admin-graphql/latest/objects/Location) 
    
The physical location where the transaction was processed.
Show fields
[Anchor to manuallyCapturable](https://shopify.dev/docs/api/admin-graphql/latest/objects/OrderTransaction#field-OrderTransaction.fields.manuallyCapturable)manuallyCapturable
•[Boolean!](https://shopify.dev/docs/api/admin-graphql/latest/scalars/Boolean)
non-null

    
Whether the transaction can be manually captured.
[Anchor to manualPaymentGateway](https://shopify.dev/docs/api/admin-graphql/latest/objects/OrderTransaction#field-OrderTransaction.fields.manualPaymentGateway)manualPaymentGateway
•[Boolean!](https://shopify.dev/docs/api/admin-graphql/latest/scalars/Boolean)
non-null

    
Whether the transaction is processed by manual payment gateway.
[Anchor to maximumRefundableV2](https://shopify.dev/docs/api/admin-graphql/latest/objects/OrderTransaction#field-OrderTransaction.fields.maximumRefundableV2)maximumRefundableV2
•[MoneyV2](https://shopify.dev/docs/api/admin-graphql/latest/objects/MoneyV2) 
    
Specifies the available amount with currency to refund on the gateway. This value is only available for transactions of type `SuggestedRefund`.
Show fields
[Anchor to multiCapturable](https://shopify.dev/docs/api/admin-graphql/latest/objects/OrderTransaction#field-OrderTransaction.fields.multiCapturable)multiCapturable
•[Boolean!](https://shopify.dev/docs/api/admin-graphql/latest/scalars/Boolean)
non-null

    
Whether the transaction can be captured multiple times.
[Anchor to order](https://shopify.dev/docs/api/admin-graphql/latest/objects/OrderTransaction#field-OrderTransaction.fields.order)order
•[Order](https://shopify.dev/docs/api/admin-graphql/latest/objects/Order) 
    
The associated order.
Show fields
[Anchor to parentTransaction](https://shopify.dev/docs/api/admin-graphql/latest/objects/OrderTransaction#field-OrderTransaction.fields.parentTransaction)parentTransaction
•[OrderTransaction](https://shopify.dev/docs/api/admin-graphql/latest/objects/OrderTransaction) 
    
The associated parent transaction, for example the authorization of a capture.
Show fields
[Anchor to paymentDetails](https://shopify.dev/docs/api/admin-graphql/latest/objects/OrderTransaction#field-OrderTransaction.fields.paymentDetails)paymentDetails
•[PaymentDetails](https://shopify.dev/docs/api/admin-graphql/latest/unions/PaymentDetails) 
    
The payment details for the transaction.
Show union types
[Anchor to paymentIcon](https://shopify.dev/docs/api/admin-graphql/latest/objects/OrderTransaction#field-OrderTransaction.fields.paymentIcon)paymentIcon
•[Image](https://shopify.dev/docs/api/admin-graphql/latest/objects/Image) 
    
The payment icon to display for the transaction.
Show fields
### Arguments
[Anchor to crop](https://shopify.dev/docs/api/admin-graphql/latest/objects/OrderTransaction#field-OrderTransaction.fields.paymentIcon.arguments.crop)crop
•[CropRegion](https://shopify.dev/docs/api/admin-graphql/latest/enums/CropRegion)
Deprecated

    
Show enum values
[Anchor to maxHeight](https://shopify.dev/docs/api/admin-graphql/latest/objects/OrderTransaction#field-OrderTransaction.fields.paymentIcon.arguments.maxHeight)maxHeight
•[Int](https://shopify.dev/docs/api/admin-graphql/latest/scalars/Int)
Deprecated


[Anchor to maxWidth](https://shopify.dev/docs/api/admin-graphql/latest/objects/OrderTransaction#field-OrderTransaction.fields.paymentIcon.arguments.maxWidth)maxWidth
•[Int](https://shopify.dev/docs/api/admin-graphql/latest/scalars/Int)
Deprecated


[Anchor to scale](https://shopify.dev/docs/api/admin-graphql/latest/objects/OrderTransaction#field-OrderTransaction.fields.paymentIcon.arguments.scale)scale
•[Int](https://shopify.dev/docs/api/admin-graphql/latest/scalars/Int)
DeprecatedDefault:1


* * *
[Anchor to paymentId](https://shopify.dev/docs/api/admin-graphql/latest/objects/OrderTransaction#field-OrderTransaction.fields.paymentId)paymentId
•[String](https://shopify.dev/docs/api/admin-graphql/latest/scalars/String) 
    
The payment ID associated with the transaction.
[Anchor to processedAt](https://shopify.dev/docs/api/admin-graphql/latest/objects/OrderTransaction#field-OrderTransaction.fields.processedAt)processedAt
•[DateTime](https://shopify.dev/docs/api/admin-graphql/latest/scalars/DateTime) 
    
Date and time when the transaction was processed.
[Anchor to receiptJson](https://shopify.dev/docs/api/admin-graphql/latest/objects/OrderTransaction#field-OrderTransaction.fields.receiptJson)receiptJson
•[JSON](https://shopify.dev/docs/api/admin-graphql/latest/scalars/JSON) 
    
The transaction receipt that the payment gateway attaches to the transaction.
* * *
Note
This field is **gateway-specific** and **not a stable contract**. Its structure and contents can vary by payment gateway and may change without notice. Apps **shouldn't parse or rely on this field for business logic** ; prefer typed fields on `OrderTransaction` and related objects.
**Note :**
This field is **gateway-specific** and **not a stable contract**. Its structure and contents can vary by payment gateway and may change without notice. Apps **shouldn't parse or rely on this field for business logic** ; prefer typed fields on `OrderTransaction` and related objects.
**Note:** <strong></strong> This field is <strong>gateway-specific</strong> and <strong>not a stable contract</strong>. Its structure and contents can vary by payment gateway and may change without notice. Apps <strong>shouldn&#39;t parse or rely on this field for business logic</strong>; prefer typed fields on <code><span class="PreventFireFoxApplyingGapToWBR">Order<wbr/>Transaction</span></code> and related objects.
* * *
[Anchor to settlementCurrency](https://shopify.dev/docs/api/admin-graphql/latest/objects/OrderTransaction#field-OrderTransaction.fields.settlementCurrency)settlementCurrency
•[CurrencyCode](https://shopify.dev/docs/api/admin-graphql/latest/enums/CurrencyCode) 
    
The settlement currency.
Show enum values
[Anchor to settlementCurrencyRate](https://shopify.dev/docs/api/admin-graphql/latest/objects/OrderTransaction#field-OrderTransaction.fields.settlementCurrencyRate)settlementCurrencyRate
•[Decimal](https://shopify.dev/docs/api/admin-graphql/latest/scalars/Decimal) 
    
The rate used when converting the transaction amount to settlement currency.
[Anchor to shopifyPaymentsSet](https://shopify.dev/docs/api/admin-graphql/latest/objects/OrderTransaction#field-OrderTransaction.fields.shopifyPaymentsSet)shopifyPaymentsSet
•[ShopifyPaymentsTransactionSet](https://shopify.dev/docs/api/admin-graphql/latest/objects/ShopifyPaymentsTransactionSet) 
    
Contains all Shopify Payments information related to an order transaction. This field is available only to stores on a Shopify Plus plan.
Show fields
[Anchor to status](https://shopify.dev/docs/api/admin-graphql/latest/objects/OrderTransaction#field-OrderTransaction.fields.status)status
•[OrderTransactionStatus!](https://shopify.dev/docs/api/admin-graphql/latest/enums/OrderTransactionStatus)
non-null

    
The status of this transaction.
Show enum values
[Anchor to test](https://shopify.dev/docs/api/admin-graphql/latest/objects/OrderTransaction#field-OrderTransaction.fields.test)test
•[Boolean!](https://shopify.dev/docs/api/admin-graphql/latest/scalars/Boolean)
non-null

    
Whether the transaction is a test transaction.
[Anchor to totalUnsettledSet](https://shopify.dev/docs/api/admin-graphql/latest/objects/OrderTransaction#field-OrderTransaction.fields.totalUnsettledSet)totalUnsettledSet
•[MoneyBag](https://shopify.dev/docs/api/admin-graphql/latest/objects/MoneyBag) 
    
The amount of the original authorization that remains unsettled, in shop and presentment currencies. During a pending capture, this reflects the full outstanding balance including the pending amount. When no capture is pending, this equals the capturable amount. Only available when an amount is capturable or manually marked as paid.
Show fields
[Anchor to user](https://shopify.dev/docs/api/admin-graphql/latest/objects/OrderTransaction#field-OrderTransaction.fields.user)user
•[StaffMember](https://shopify.dev/docs/api/admin-graphql/latest/objects/StaffMember) 
    
Staff member who was logged into the Shopify POS device when the transaction was processed.
Show fields
### Deprecated fields
  * amount (Money!): deprecated
  * amountV2 (MoneyV2!): deprecated
  * authorizationCode (String): deprecated
  * maximumRefundable (Money): deprecated
  * paymentMethod (PaymentMethods): deprecated
  * totalUnsettled (Money): deprecated
  * totalUnsettledV2 (MoneyV2): deprecated


[Anchor to amount](https://shopify.dev/docs/api/admin-graphql/latest/objects/OrderTransaction#field-OrderTransaction.fields.amount)amount
•[Money!](https://shopify.dev/docs/api/admin-graphql/latest/scalars/Money)
non-nullDeprecated


[Anchor to amountV2](https://shopify.dev/docs/api/admin-graphql/latest/objects/OrderTransaction#field-OrderTransaction.fields.amountV2)amountV2
•[MoneyV2!](https://shopify.dev/docs/api/admin-graphql/latest/objects/MoneyV2)
non-nullDeprecated

    
Show fields
[Anchor to authorizationCode](https://shopify.dev/docs/api/admin-graphql/latest/objects/OrderTransaction#field-OrderTransaction.fields.authorizationCode)authorizationCode
•[String](https://shopify.dev/docs/api/admin-graphql/latest/scalars/String)
Deprecated


[Anchor to maximumRefundable](https://shopify.dev/docs/api/admin-graphql/latest/objects/OrderTransaction#field-OrderTransaction.fields.maximumRefundable)maximumRefundable
•[Money](https://shopify.dev/docs/api/admin-graphql/latest/scalars/Money)
Deprecated


[Anchor to paymentMethod](https://shopify.dev/docs/api/admin-graphql/latest/objects/OrderTransaction#field-OrderTransaction.fields.paymentMethod)paymentMethod
•[PaymentMethods](https://shopify.dev/docs/api/admin-graphql/latest/enums/PaymentMethods)
Deprecated

    
Show enum values
[Anchor to totalUnsettled](https://shopify.dev/docs/api/admin-graphql/latest/objects/OrderTransaction#field-OrderTransaction.fields.totalUnsettled)totalUnsettled
•[Money](https://shopify.dev/docs/api/admin-graphql/latest/scalars/Money)
Deprecated


[Anchor to totalUnsettledV2](https://shopify.dev/docs/api/admin-graphql/latest/objects/OrderTransaction#field-OrderTransaction.fields.totalUnsettledV2)totalUnsettledV2
•[MoneyV2](https://shopify.dev/docs/api/admin-graphql/latest/objects/MoneyV2)
Deprecated

    
Show fields
* * *
Was this section helpful?
YesNo
## Map
### Fields and connections with this object
  * {}[CashTrackingSession.cashTransactions](https://shopify.dev/docs/api/admin-graphql/latest/objects/CashTrackingSession#field-CashTrackingSession.fields.cashTransactions)
  * {}[CashTransactionActivity.orderTransaction](https://shopify.dev/docs/api/admin-graphql/latest/objects/CashTransactionActivity#field-CashTransactionActivity.fields.orderTransaction)
  * {}[Order.transactions](https://shopify.dev/docs/api/admin-graphql/latest/objects/Order#field-Order.fields.transactions)
  * {}[OrderPaymentStatus.transactions](https://shopify.dev/docs/api/admin-graphql/latest/objects/OrderPaymentStatus#field-OrderPaymentStatus.fields.transactions)
  * {}[OrderTransaction.parentTransaction](https://shopify.dev/docs/api/admin-graphql/latest/objects/OrderTransaction#field-OrderTransaction.fields.parentTransaction)
  * <->[OrderTransactionConnection.nodes](https://shopify.dev/docs/api/admin-graphql/latest/connections/OrderTransactionConnection#returns-nodes)
  * {}[OrderTransactionEdge.node](https://shopify.dev/docs/api/admin-graphql/latest/objects/OrderTransactionEdge#field-OrderTransactionEdge.fields.node)
  * {}[Refund.transactions](https://shopify.dev/docs/api/admin-graphql/latest/objects/Refund#field-Refund.fields.transactions)
  * {}[Return.transactions](https://shopify.dev/docs/api/admin-graphql/latest/objects/Return#field-Return.fields.transactions)
  * {}[SubscriptionBillingAttempt.transactions](https://shopify.dev/docs/api/admin-graphql/latest/objects/SubscriptionBillingAttempt#field-SubscriptionBillingAttempt.fields.transactions)
  * {}[SuggestedOrderTransaction.parentTransaction](https://shopify.dev/docs/api/admin-graphql/latest/objects/SuggestedOrderTransaction#field-SuggestedOrderTransaction.fields.parentTransaction)


### Possible type in
  * [StoreCreditAccountTransactionOrigin](https://shopify.dev/docs/api/admin-graphql/latest/unions/StoreCreditAccountTransactionOrigin)


* * *
## 
[Anchor to Mutations](https://shopify.dev/docs/api/admin-graphql/latest/objects/OrderTransaction#mutations)Mutations
  * orderCapture (OrderCapturePayload)
  * transactionVoid (TransactionVoidPayload)


[Anchor to orderCapture](https://shopify.dev/docs/api/admin-graphql/latest/objects/OrderTransaction#mutation-orderCapture)[orderCapture](https://shopify.dev/docs/api/admin-graphql/latest/mutations/orderCapture)
•mutation 
    
Captures payment for an authorized transaction on an order. Use this mutation to claim the money that was previously reserved by an authorization transaction.
The `orderCapture` mutation can be used in the following scenarios:
  * To capture the full amount of an authorized transaction
  * To capture a partial payment by specifying an amount less than the total order amount
  * To perform multiple captures on the same order, as long as the order transaction is [multi-capturable](https://shopify.dev/docs/api/admin-graphql/latest/objects/ordertransaction#field-OrderTransaction.fields.multiCapturable)


* * *
Note
Multi-capture functionality is only available to stores on a [Shopify Plus plan](https://help.shopify.com/manual/intro-to-shopify/pricing-plans/plans-features/shopify-plus-plan). For multi-currency orders, the [`currency`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/orderCapture#arguments-input.fields.currency) field is required and should match the presentment currency from the order.
**Note :**
Multi-capture functionality is only available to stores on a [Shopify Plus plan](https://help.shopify.com/manual/intro-to-shopify/pricing-plans/plans-features/shopify-plus-plan). For multi-currency orders, the [`currency`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/orderCapture#arguments-input.fields.currency) field is required and should match the presentment currency from the order.
**Note:** Multi-capture functionality is only available to stores on a <a href="https://help.shopify.com/manual/intro-to-shopify/pricing-plans/plans-features/shopify-plus-plan">Shopify Plus plan</a>. For multi-currency orders, the <a href="https://shopify.dev/docs/api/admin-graphql/latest/mutations/orderCapture#arguments-input.fields.currency"><code>currency</code></a> field is required and should match the presentment currency from the order.
* * *
After capturing a payment, you can:
  * View the transaction details including status, amount, and processing information.
  * Track the captured amount in both shop and presentment currencies.
  * Monitor the transaction's settlement status.


Learn more about [order transactions](https://shopify.dev/docs/api/admin-graphql/latest/objects/OrderTransaction).
Show payload
### Arguments
[Anchor to input](https://shopify.dev/docs/api/admin-graphql/latest/objects/OrderTransaction#mutation-orderCapture.arguments.input)input
•[OrderCaptureInput!](https://shopify.dev/docs/api/admin-graphql/latest/input-objects/OrderCaptureInput)
required

    
The input for the mutation.
Show input fields
* * *
[Anchor to transactionVoid](https://shopify.dev/docs/api/admin-graphql/latest/objects/OrderTransaction#mutation-transactionVoid)[transactionVoid](https://shopify.dev/docs/api/admin-graphql/latest/mutations/transactionVoid)
•mutation 
    
Trigger the voiding of an uncaptured authorization transaction.
Show payload
### Arguments
[Anchor to parentTransactionId](https://shopify.dev/docs/api/admin-graphql/latest/objects/OrderTransaction#mutation-transactionVoid.arguments.parentTransactionId)parentTransactionId
•[ID!](https://shopify.dev/docs/api/admin-graphql/latest/scalars/ID)
required

    
An uncaptured authorization transaction.
* * *
* * *
Was this section helpful?
YesNo
##  <~> OrderTransaction Mutations
### Mutated by
  * <~>[orderCapture](https://shopify.dev/docs/api/admin-graphql/latest/mutations/orderCapture)
  * <~>[transactionVoid](https://shopify.dev/docs/api/admin-graphql/latest/mutations/transactionVoid)


* * *
## 
[Anchor to Interfaces](https://shopify.dev/docs/api/admin-graphql/latest/objects/OrderTransaction#interfaces)Interfaces
  * Node


[Anchor to Node](https://shopify.dev/docs/api/admin-graphql/latest/objects/OrderTransaction#interface-Node)[Node](https://shopify.dev/docs/api/admin-graphql/latest/interfaces/Node)
•interface 

* * *
Was this section helpful?
YesNo
##  ||-OrderTransaction Implements
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



