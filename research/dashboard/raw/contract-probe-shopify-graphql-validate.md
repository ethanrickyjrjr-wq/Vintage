# contract probe: Shopify GraphQL Admin 2026-10 query validation + live cost, 2026-10-26

What this is: the queries the builder will copy, checked three ways.
1. Schema validation with graphql-js `validate()` against the full 2026-10 introspection (3,716 types) from
   `POST https://shopify.dev/admin-graphql-direct-proxy/2026-10` (no auth; Shopify's docs introspection proxy).
2. Deprecation check of every field used (0 deprecated, 0 missing).
3. Execution of the same queries on that same proxy, which answers from a SHOPIFY DEMO STORE (CAD orders #1001...,
   not Ricky's store). It returned `data` plus `extensions.cost`. So response SHAPES and COSTS are live-verified;
   plan/bucket figures are NOT Ricky's plan (bucket on the demo store: maximumAvailable 2000, restoreRate 100).
   Protected-customer-data behavior on Ricky's real store is NOT tested here (these queries select no email/name/address).

## Query: orders (stored fields) - VALID against 2026-10, executed OK on proxy
```graphql
query Orders($first: Int!, $after: String, $query: String) {
  orders(first: $first, after: $after, query: $query, sortKey: UPDATED_AT) {
    pageInfo { hasNextPage endCursor }
    edges { cursor node {
      id name createdAt updatedAt displayFinancialStatus displayFulfillmentStatus
      totalPriceSet { shopMoney { amount currencyCode } }
      subtotalPriceSet { shopMoney { amount currencyCode } }
      totalShippingPriceSet { shopMoney { amount currencyCode } }
      totalTaxSet { shopMoney { amount currencyCode } }
      lineItems(first: 5) { edges { node {
        id title sku quantity
        originalUnitPriceSet { shopMoney { amount currencyCode } }
        product { id }
      } } }
    } }
  }
}
```
variables: `{"first": 25, "query": "updated_at:>='2026-10-26T00:00:00Z'"}`
(The `$first` variable form passed schema validation; the cost run below used literal first values; the `updated_at:>=` filter string was accepted by the proxy without errors.)

## Query: products - VALID, executed OK
```graphql
query Products($first: Int!, $after: String, $query: String) {
  products(first: $first, after: $after, query: $query, sortKey: UPDATED_AT) {
    pageInfo { hasNextPage endCursor }
    edges { node { id title status onlineStoreUrl updatedAt
      variants(first: 5) { edges { node { id sku price inventoryQuantity } } } } }
  }
}
```

## Query: granted scopes - VALID (not executed; the proxy app is not ours)
`{ currentAppInstallation { accessScopes { handle } } }`

## Mutation: webhookSubscriptionCreate - VALID (not executed; it would write to a store)
```graphql
mutation($topic: WebhookSubscriptionTopic!, $sub: WebhookSubscriptionInput!) {
  webhookSubscriptionCreate(topic: $topic, webhookSubscription: $sub) {
    webhookSubscription { id topic uri } userErrors { field message }
  }
}
```
Introspected `WebhookSubscriptionInput` fields (2026-10): format:WebhookSubscriptionFormat, includeFields:[String!], filter:String, metafieldNamespaces:[String!], metafields:[HasMetafieldsMetafieldIdentifierInput!], name:String, uri:String. There is no `callbackUrl` field in 2026-10; use `uri`.
`WebhookSubscriptionFormat`: JSON, XML. `webhookSubscriptionCreate` args: topic:WebhookSubscriptionTopic!, webhookSubscription:WebhookSubscriptionInput!; not deprecated.
`WebhookSubscriptionEndpoint` union: WebhookEventBridgeEndpoint, WebhookHttpEndpoint, WebhookPubSubEndpoint.
`WebhookSubscriptionTopic` values present: ORDERS_CREATE, ORDERS_PAID, ORDERS_FULFILLED, ORDERS_UPDATED, ORDERS_CANCELLED, ORDERS_EDITED, ORDERS_DELETE, ORDERS_PARTIALLY_FULFILLED, PRODUCTS_CREATE, PRODUCTS_UPDATE, PRODUCTS_DELETE, INVENTORY_LEVELS_UPDATE, INVENTORY_LEVELS_CONNECT, INVENTORY_LEVELS_DISCONNECT, INVENTORY_ITEMS_UPDATE, APP_UNINSTALLED.

## Introspected types (2026-10)
- `QueryRoot.orders(first, after, last, before, reverse, sortKey: OrderSortKeys, query: String, savedSearchId)`: OrderConnection!
- `OrderSortKeys`: CREATED_AT, CURRENT_TOTAL_PRICE, CUSTOMER_NAME, DESTINATION, FINANCIAL_STATUS, FULFILLMENT_STATUS, ID, ORDER_NUMBER, PO_NUMBER, PROCESSED_AT, RELEVANCE, TOTAL_ITEMS_QUANTITY, TOTAL_PRICE, UPDATED_AT
- `Order.displayFinancialStatus`: OrderDisplayFinancialStatus! = PENDING, AUTHORIZED, PARTIALLY_PAID, PARTIALLY_REFUNDED, VOIDED, PAID, REFUNDED, EXPIRED
- `Order.displayFulfillmentStatus`: OrderDisplayFulfillmentStatus! = UNFULFILLED, PARTIALLY_FULFILLED, FULFILLED, RESTOCKED, PENDING_FULFILLMENT, OPEN, IN_PROGRESS, ON_HOLD, SCHEDULED, REQUEST_DECLINED, FULFILLMENT_NOT_REQUIRED
- `Order.totalPriceSet`: MoneyBag!; `subtotalPriceSet`: MoneyBag (nullable); `totalShippingPriceSet`: MoneyBag!; `totalTaxSet`: MoneyBag (nullable). `MoneyBag` = presentmentMoney, shopMoney. `MoneyV2` = amount:Decimal!, currencyCode:CurrencyCode!
- `LineItem.sku`: String (nullable); `LineItem.product`: Product (nullable, e.g. deleted products); `LineItem.originalUnitPriceSet`: MoneyBag!
- `Product.status`: ProductStatus! = ACTIVE, ARCHIVED, DRAFT, UNLISTED; `Product.onlineStoreUrl`: URL (nullable)
- `ProductVariant.price`: Money! (scalar, decimal string); `ProductVariant.inventoryQuantity`: Int (nullable)
- search syntax rows (from the `query` arg descriptions): orders `updated_at:'2020-10-21T23:39:20Z'`, `updated_at:<now`, `updated_at:<=2024`; products `updated_at:>'2020-10-21T23:39:20Z'`; orders `financial_status:` paid|pending|authorized|partially_paid|partially_refunded|refunded|voided|expired; orders `fulfillment_status:` unshipped|shipped|fulfilled|partial|scheduled|on_hold|unfulfilled|request_declined; products `status:active,draft`.

## Live cost on the proxy (requestedQueryCost / actualQueryCost); the 1,000-point single-query cap is on REQUESTED cost
| orders first | lineItems first | requested | actual |
|---|---|---|---|
| 50 | 50 | 121 | 9 |
| 50 | 5 | 65 | 12 |
| 25 | 5 | 56 | 18 |
| 10 | 5 | 38 | 22 |

| products first | variants first | requested | actual |
|---|---|---|---|
| 50 | 50 | 72 | 23 |
| 25 | 5 | 38 | 26 |
| 10 | 5 | 26 | 18 |

Reading: even first:50 x 50 is far under 1,000. The real numbers are much smaller than a naive first x children product. Use `first: 25` orders and `lineItems(first: 5)` anyway (quantity-1 shop) and read `extensions.cost` on the first real call.
throttleStatus on the demo store: `{"maximumAvailable":2000,"restoreRate":100}`. Ricky's own bucket: read it from his first response.

## Sample live response (demo store, 2026-10), shapes only
Order: `{"id":"gid://shopify/Order/1984311263254","name":"#1003","createdAt":"2020-09-01T19:00:37Z","updatedAt":"2025-06-26T18:39:08Z","displayFinancialStatus":"PAID","displayFulfillmentStatus":"FULFILLED","totalPriceSet":{"shopMoney":{"amount":"66.0","currencyCode":"CAD"}},"subtotalPriceSet":{"shopMoney":{"amount":"66.0","currencyCode":"CAD"}},"totalShippingPriceSet":{"shopMoney":{"amount":"0.0","currencyCode":"CAD"}},"totalTaxSet":{"shopMoney":{"amount":"0.0","currencyCode":"CAD"}},"lineItems":{"edges":[{"node":{"id":"gid://shopify/LineItem/4557257703446","title":"Aged Wood Wallet","sku":"","quantity":1,"originalUnitPriceSet":{"shopMoney":{"amount":"66.0","currencyCode":"CAD"}},"product":{"id":"gid://shopify/Product/1974211182614"}}}]}}`
Product: `{"id":"gid://shopify/Product/1974208331798","title":"Wandering Thunder Blouse","status":"ACTIVE","onlineStoreUrl":null,"updatedAt":"2026-07-22T04:23:29Z","variants":{"edges":[{"node":{"id":"gid://shopify/ProductVariant/19523123249174","sku":"","price":"9.00","inventoryQuantity":0}}]}}`
Note: money `amount` is a decimal STRING; `sku` can be the empty string; `onlineStoreUrl` is null for a product not on the Online Store channel.

Method: graphql-js@16.9.0 `buildClientSchema(introspection.data)` + `validate(schema, parse(q))` gave VALID for all four documents; a deprecation scan of the 32 fields used gave 0 problems. Scripts lived in the session scratchpad, not the repo.
