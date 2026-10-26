[Skip to main content](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#main-content)
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
[Anchor to WebhookSubscriptionTopic](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#top)
# WebhookSubscriptionTopic
enum
Install AI ToolkitAsk about this pageCopy MD
The supported topics for webhook subscriptions. You can use webhook subscriptions to receive notifications about particular events in a shop.
You create [mandatory webhooks](https://shopify.dev/apps/webhooks/configuration/mandatory-webhooks#mandatory-compliance-webhooks) either via the [Partner Dashboard](https://shopify.dev/apps/webhooks/configuration/mandatory-webhooks#subscribe-to-privacy-webhooks) or by updating the [app configuration file](https://shopify.dev/apps/tools/cli/configuration#app-configuration-file-example).
* * *
Tip
To configure your subscription using the app configuration file, refer to the [full list of topic names](https://shopify.dev/docs/api/webhooks?reference=graphql).
**Tip :**
To configure your subscription using the app configuration file, refer to the [full list of topic names](https://shopify.dev/docs/api/webhooks?reference=graphql).
**Tip:** To configure your subscription using the app configuration file, refer to the <a href="https://shopify.dev/docs/api/webhooks?reference=graphql">full list of topic names</a>.
* * *
## 
[Anchor to Valid values](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#valid-values)Valid values
  * APP_PURCHASES_ONE_TIME_UPDATE
  * APP_SCOPES_UPDATE
  * APP_SUBSCRIPTIONS_APPROACHING_CAPPED_AMOUNT
  * APP_SUBSCRIPTIONS_UPDATE
  * APP_UNINSTALLED
  * AUDIT_EVENTS_ADMIN_API_ACTIVITY
  * BULK_OPERATIONS_FINISH
  * CARTS_CREATE
  * CARTS_UPDATE
  * CHANNELS_DELETE
  * CHECKOUTS_CREATE
  * CHECKOUTS_DELETE
  * CHECKOUTS_UPDATE
  * COLLECTION_LISTINGS_ADD
  * COLLECTION_LISTINGS_REMOVE
  * COLLECTION_LISTINGS_UPDATE
  * COLLECTION_PUBLICATIONS_CREATE
  * COLLECTION_PUBLICATIONS_DELETE
  * COLLECTION_PUBLICATIONS_UPDATE
  * COLLECTIONS_CREATE
  * COLLECTIONS_DELETE
  * COLLECTIONS_UPDATE
  * COMPANIES_CREATE
  * COMPANIES_DELETE
  * COMPANIES_UPDATE
  * COMPANY_CONTACT_ROLES_ASSIGN
  * COMPANY_CONTACT_ROLES_REVOKE
  * COMPANY_CONTACTS_CREATE
  * COMPANY_CONTACTS_DELETE
  * COMPANY_CONTACTS_UPDATE
  * COMPANY_LOCATIONS_CREATE
  * COMPANY_LOCATIONS_DELETE
  * COMPANY_LOCATIONS_UPDATE
  * CUSTOMER_ACCOUNT_SETTINGS_UPDATE
  * CUSTOMER_GROUPS_CREATE
  * CUSTOMER_GROUPS_DELETE
  * CUSTOMER_GROUPS_UPDATE
  * CUSTOMER_JOINED_SEGMENT
  * CUSTOMER_LEFT_SEGMENT
  * CUSTOMER_PAYMENT_METHODS_CREATE
  * CUSTOMER_PAYMENT_METHODS_REVOKE
  * CUSTOMER_PAYMENT_METHODS_UPDATE
  * CUSTOMER_TAGS_ADDED
  * CUSTOMER_TAGS_REMOVED
  * CUSTOMERS_CREATE
  * CUSTOMERS_DELETE
  * CUSTOMERS_DISABLE
  * CUSTOMERS_EMAIL_MARKETING_CONSENT_UPDATE
  * CUSTOMERS_ENABLE
  * CUSTOMERS_MARKETING_CONSENT_UPDATE
  * CUSTOMERS_MERGE
  * CUSTOMERS_PURCHASING_SUMMARY
  * CUSTOMERS_UPDATE
  * CUSTOMERS_WHATS_APP_MARKETING_CONSENT_UPDATE
  * DELIVERY_PROMISE_SETTINGS_UPDATE
  * DISCOUNTS_CREATE
  * DISCOUNTS_DELETE
  * DISCOUNTS_REDEEMCODE_ADDED
  * DISCOUNTS_REDEEMCODE_REMOVED
  * DISCOUNTS_UPDATE
  * DISPUTES_CREATE
  * DISPUTES_UPDATE
  * DOMAINS_CREATE
  * DOMAINS_DESTROY
  * DOMAINS_UPDATE
  * DRAFT_ORDERS_CREATE
  * DRAFT_ORDERS_DELETE
  * DRAFT_ORDERS_UPDATE
  * FINANCE_APP_STAFF_MEMBER_DELETE
  * FINANCE_APP_STAFF_MEMBER_GRANT
  * FINANCE_APP_STAFF_MEMBER_REVOKE
  * FINANCE_APP_STAFF_MEMBER_UPDATE
  * FINANCE_KYC_INFORMATION_UPDATE
  * FULFILLMENT_EVENTS_CREATE
  * FULFILLMENT_EVENTS_DELETE
  * FULFILLMENT_HOLDS_ADDED
  * FULFILLMENT_HOLDS_RELEASED
  * FULFILLMENT_ORDERS_CANCELLATION_REQUEST_ACCEPTED
  * FULFILLMENT_ORDERS_CANCELLATION_REQUEST_REJECTED
  * FULFILLMENT_ORDERS_CANCELLATION_REQUEST_SUBMITTED
  * FULFILLMENT_ORDERS_CANCELLED
  * FULFILLMENT_ORDERS_FULFILLMENT_REQUEST_ACCEPTED
  * FULFILLMENT_ORDERS_FULFILLMENT_REQUEST_REJECTED
  * FULFILLMENT_ORDERS_FULFILLMENT_REQUEST_SUBMITTED
  * FULFILLMENT_ORDERS_FULFILLMENT_SERVICE_FAILED_TO_COMPLETE
  * FULFILLMENT_ORDERS_HOLD_RELEASED
  * FULFILLMENT_ORDERS_LINE_ITEMS_PREPARED_FOR_LOCAL_DELIVERY
  * FULFILLMENT_ORDERS_LINE_ITEMS_PREPARED_FOR_PICKUP
  * FULFILLMENT_ORDERS_MANUALLY_REPORTED_PROGRESS_STOPPED
  * FULFILLMENT_ORDERS_MERGED
  * FULFILLMENT_ORDERS_MOVED
  * FULFILLMENT_ORDERS_ORDER_ROUTING_COMPLETE
  * FULFILLMENT_ORDERS_PLACED_ON_HOLD
  * FULFILLMENT_ORDERS_PROGRESS_REPORTED
  * FULFILLMENT_ORDERS_RESCHEDULED
  * FULFILLMENT_ORDERS_SCHEDULED_FULFILLMENT_ORDER_READY
  * FULFILLMENT_ORDERS_SPLIT
  * FULFILLMENTS_CREATE
  * FULFILLMENTS_UPDATE
  * INVENTORY_ITEMS_CREATE
  * INVENTORY_ITEMS_DELETE
  * INVENTORY_ITEMS_UPDATE
  * INVENTORY_LEVELS_CONNECT
  * INVENTORY_LEVELS_DISCONNECT
  * INVENTORY_LEVELS_UPDATE
  * INVENTORY_SHIPMENTS_ADD_ITEMS
  * INVENTORY_SHIPMENTS_CREATE
  * INVENTORY_SHIPMENTS_DELETE
  * INVENTORY_SHIPMENTS_MARK_IN_TRANSIT
  * INVENTORY_SHIPMENTS_RECEIVE_ITEMS
  * INVENTORY_SHIPMENTS_REMOVE_ITEMS
  * INVENTORY_SHIPMENTS_UPDATE_ITEM_QUANTITIES
  * INVENTORY_SHIPMENTS_UPDATE_TRACKING
  * INVENTORY_TRANSFERS_ADD_ITEMS
  * INVENTORY_TRANSFERS_CANCEL
  * INVENTORY_TRANSFERS_COMPLETE
  * INVENTORY_TRANSFERS_READY_TO_SHIP
  * INVENTORY_TRANSFERS_REMOVE_ITEMS
  * INVENTORY_TRANSFERS_UPDATE_ITEM_QUANTITIES
  * INVENTORY_TRANSFERS_UPDATED
  * LOCALES_CREATE
  * LOCALES_DESTROY
  * LOCALES_UPDATE
  * LOCATIONS_ACTIVATE
  * LOCATIONS_CREATE
  * LOCATIONS_DEACTIVATE
  * LOCATIONS_DELETE
  * LOCATIONS_UPDATE
  * MARKETS_BACKUP_REGION_UPDATE
  * MARKETS_CREATE
  * MARKETS_DELETE
  * MARKETS_UPDATE
  * METAFIELD_DEFINITIONS_CREATE
  * METAFIELD_DEFINITIONS_DELETE
  * METAFIELD_DEFINITIONS_UPDATE
  * METAOBJECTS_CREATE
  * METAOBJECTS_DELETE
  * METAOBJECTS_UPDATE
  * ORDER_TRANSACTIONS_CREATE
  * ORDERS_CANCELLED
  * ORDERS_CREATE
  * ORDERS_DELETE
  * ORDERS_EDITED
  * ORDERS_FULFILLED
  * ORDERS_LINK_REQUESTED
  * ORDERS_PAID
  * ORDERS_PARTIALLY_FULFILLED
  * ORDERS_RISK_ASSESSMENT_CHANGED
  * ORDERS_SHOPIFY_PROTECT_ELIGIBILITY_CHANGED
  * ORDERS_UPDATED
  * PAYMENT_SCHEDULES_DUE
  * PAYMENT_TERMS_CREATE
  * PAYMENT_TERMS_DELETE
  * PAYMENT_TERMS_UPDATE
  * PRODUCT_FEEDS_CREATE
  * PRODUCT_FEEDS_FULL_SYNC
  * PRODUCT_FEEDS_FULL_SYNC_FINISH
  * PRODUCT_FEEDS_INCREMENTAL_SYNC
  * PRODUCT_FEEDS_UPDATE
  * PRODUCT_LISTINGS_ADD
  * PRODUCT_LISTINGS_REMOVE
  * PRODUCT_LISTINGS_UPDATE
  * PRODUCT_PUBLICATIONS_CREATE
  * PRODUCT_PUBLICATIONS_DELETE
  * PRODUCT_PUBLICATIONS_UPDATE
  * PRODUCTS_CREATE
  * PRODUCTS_DELETE
  * PRODUCTS_UPDATE
  * PROFILES_CREATE
  * PROFILES_DELETE
  * PROFILES_UPDATE
  * REFUNDS_CREATE
  * REQUESTED_ORDER_EDIT_CREATED
  * REQUESTED_ORDER_EDIT_DECLINED
  * REQUESTED_ORDER_EDIT_RESOLVED
  * RETURNS_APPROVE
  * RETURNS_CANCEL
  * RETURNS_CLOSE
  * RETURNS_DECLINE
  * RETURNS_PROCESS
  * RETURNS_REOPEN
  * RETURNS_REQUEST
  * RETURNS_UPDATE
  * REVERSE_DELIVERIES_ATTACH_DELIVERABLE
  * REVERSE_FULFILLMENT_ORDERS_DISPOSE
  * ROLLOUTS_CREATE
  * ROLLOUTS_DELETE
  * ROLLOUTS_RESOURCE_CHANGE_ADDED
  * ROLLOUTS_RESOURCE_CHANGE_REMOVED
  * ROLLOUTS_RESOURCE_CHANGE_UPDATED
  * ROLLOUTS_UPDATE
  * SCHEDULED_PRODUCT_LISTINGS_ADD
  * SCHEDULED_PRODUCT_LISTINGS_REMOVE
  * SCHEDULED_PRODUCT_LISTINGS_UPDATE
  * SEGMENTS_CREATE
  * SEGMENTS_DELETE
  * SEGMENTS_UPDATE
  * SELLING_PLAN_GROUPS_CREATE
  * SELLING_PLAN_GROUPS_DELETE
  * SELLING_PLAN_GROUPS_UPDATE
  * SHIPPING_ADDRESSES_CREATE
  * SHIPPING_ADDRESSES_UPDATE
  * SHOP_UPDATE
  * SUBSCRIPTION_BILLING_ATTEMPTS_CHALLENGED
  * SUBSCRIPTION_BILLING_ATTEMPTS_FAILURE
  * SUBSCRIPTION_BILLING_ATTEMPTS_SUCCESS
  * SUBSCRIPTION_BILLING_CYCLE_EDITS_CREATE
  * SUBSCRIPTION_BILLING_CYCLE_EDITS_DELETE
  * SUBSCRIPTION_BILLING_CYCLE_EDITS_UPDATE
  * SUBSCRIPTION_BILLING_CYCLES_SKIP
  * SUBSCRIPTION_BILLING_CYCLES_UNSKIP
  * SUBSCRIPTION_CONTRACTS_ACTIVATE
  * SUBSCRIPTION_CONTRACTS_CANCEL
  * SUBSCRIPTION_CONTRACTS_CREATE
  * SUBSCRIPTION_CONTRACTS_EXPIRE
  * SUBSCRIPTION_CONTRACTS_FAIL
  * SUBSCRIPTION_CONTRACTS_PAUSE
  * SUBSCRIPTION_CONTRACTS_UPDATE
  * TAX_SERVICES_CREATE
  * TAX_SERVICES_UPDATE
  * TENDER_TRANSACTIONS_CREATE
  * THEMES_CREATE
  * THEMES_DELETE
  * THEMES_PUBLISH
  * THEMES_UPDATE
  * VARIANTS_IN_STOCK
  * VARIANTS_OUT_OF_STOCK


[Anchor to APP_PURCHASES_ONE_TIME_UPDATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-APP_PURCHASES_ONE_TIME_UPDATE)APP_PURCHASES_ONE_TIME_UPDATE

    
The webhook topic for `app_purchases_one_time/update` events. Occurs whenever a one-time app charge is updated.
[Anchor to APP_SCOPES_UPDATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-APP_SCOPES_UPDATE)APP_SCOPES_UPDATE

    
The webhook topic for `app/scopes_update` events. Occurs whenever the access scopes of any installation are modified. Allows apps to keep track of the granted access scopes of their installations.
[Anchor to APP_SUBSCRIPTIONS_APPROACHING_CAPPED_AMOUNT](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-APP_SUBSCRIPTIONS_APPROACHING_CAPPED_AMOUNT)APP_SUBSCRIPTIONS_APPROACHING_CAPPED_AMOUNT

    
The webhook topic for `app_subscriptions/approaching_capped_amount` events. Occurs when the balance used on an app subscription crosses 90% of the capped amount.
[Anchor to APP_SUBSCRIPTIONS_UPDATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-APP_SUBSCRIPTIONS_UPDATE)APP_SUBSCRIPTIONS_UPDATE

    
The webhook topic for `app_subscriptions/update` events. Occurs whenever an app subscription is updated.
[Anchor to APP_UNINSTALLED](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-APP_UNINSTALLED)APP_UNINSTALLED

    
The webhook topic for `app/uninstalled` events. Occurs whenever a shop has uninstalled the app.
[Anchor to AUDIT_EVENTS_ADMIN_API_ACTIVITY](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-AUDIT_EVENTS_ADMIN_API_ACTIVITY)AUDIT_EVENTS_ADMIN_API_ACTIVITY

    
The webhook topic for `audit_events/admin_api_activity` events. Triggers for each auditable Admin API request. This topic is limited to one active subscription per Plus store and requires the use of Google Cloud Pub/Sub or AWS EventBridge. Requires the `read_audit_events` scope.
[Anchor to BULK_OPERATIONS_FINISH](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-BULK_OPERATIONS_FINISH)BULK_OPERATIONS_FINISH

    
The webhook topic for `bulk_operations/finish` events. Notifies when a Bulk Operation finishes.
[Anchor to CARTS_CREATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-CARTS_CREATE)CARTS_CREATE

    
The webhook topic for `carts/create` events. Occurs when a cart is created in the online store. Other types of carts aren't supported. For example, the webhook doesn't support carts that are created in a custom storefront. Requires the `read_orders` scope.
[Anchor to CARTS_UPDATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-CARTS_UPDATE)CARTS_UPDATE

    
The webhook topic for `carts/update` events. Occurs when a cart is updated in the online store. Other types of carts aren't supported. For example, the webhook doesn't support carts that are updated in a custom storefront. Requires the `read_orders` scope.
[Anchor to CHANNELS_DELETE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-CHANNELS_DELETE)CHANNELS_DELETE

    
The webhook topic for `channels/delete` events. Occurs whenever a channel is deleted. Requires the `read_publications` scope.
[Anchor to CHECKOUTS_CREATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-CHECKOUTS_CREATE)CHECKOUTS_CREATE

    
The webhook topic for `checkouts/create` events. Occurs whenever a checkout is created. Requires the `read_orders` scope.
[Anchor to CHECKOUTS_DELETE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-CHECKOUTS_DELETE)CHECKOUTS_DELETE

    
The webhook topic for `checkouts/delete` events. Occurs whenever a checkout is deleted. Requires the `read_orders` scope.
[Anchor to CHECKOUTS_UPDATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-CHECKOUTS_UPDATE)CHECKOUTS_UPDATE

    
The webhook topic for `checkouts/update` events. Occurs whenever a checkout is updated. Requires the `read_orders` scope.
[Anchor to COLLECTION_LISTINGS_ADD](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-COLLECTION_LISTINGS_ADD)COLLECTION_LISTINGS_ADD

    
The webhook topic for `collection_listings/add` events. Occurs whenever a collection listing is added. Requires the `read_product_listings` scope.
[Anchor to COLLECTION_LISTINGS_REMOVE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-COLLECTION_LISTINGS_REMOVE)COLLECTION_LISTINGS_REMOVE

    
The webhook topic for `collection_listings/remove` events. Occurs whenever a collection listing is removed. Requires the `read_product_listings` scope.
[Anchor to COLLECTION_LISTINGS_UPDATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-COLLECTION_LISTINGS_UPDATE)COLLECTION_LISTINGS_UPDATE

    
The webhook topic for `collection_listings/update` events. Occurs whenever a collection listing is updated. Requires the `read_product_listings` scope.
[Anchor to COLLECTION_PUBLICATIONS_CREATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-COLLECTION_PUBLICATIONS_CREATE)COLLECTION_PUBLICATIONS_CREATE

    
The webhook topic for `collection_publications/create` events. Occurs whenever a collection publication listing is created. Requires the `read_publications` scope.
[Anchor to COLLECTION_PUBLICATIONS_DELETE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-COLLECTION_PUBLICATIONS_DELETE)COLLECTION_PUBLICATIONS_DELETE

    
The webhook topic for `collection_publications/delete` events. Occurs whenever a collection publication listing is deleted. Requires the `read_publications` scope.
[Anchor to COLLECTION_PUBLICATIONS_UPDATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-COLLECTION_PUBLICATIONS_UPDATE)COLLECTION_PUBLICATIONS_UPDATE

    
The webhook topic for `collection_publications/update` events. Occurs whenever a collection publication listing is updated. Requires the `read_publications` scope.
[Anchor to COLLECTIONS_CREATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-COLLECTIONS_CREATE)COLLECTIONS_CREATE

    
The webhook topic for `collections/create` events. Occurs whenever a collection is created. Requires the `read_products` scope.
[Anchor to COLLECTIONS_DELETE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-COLLECTIONS_DELETE)COLLECTIONS_DELETE

    
The webhook topic for `collections/delete` events. Occurs whenever a collection is deleted. Requires the `read_products` scope.
[Anchor to COLLECTIONS_UPDATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-COLLECTIONS_UPDATE)COLLECTIONS_UPDATE

    
The webhook topic for `collections/update` events. Occurs whenever a collection is updated, including when a product is manually added or removed from the collection or when the collection rules change. Occurs once if multiple products are manually added or removed from a collection at the same time. Not fired when attribute changes affect whether a product matches a collection's rules. Requires the `read_products` scope.
[Anchor to COMPANIES_CREATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-COMPANIES_CREATE)COMPANIES_CREATE

    
The webhook topic for `companies/create` events. Occurs whenever a company is created. Requires at least one of the following scopes: read_customers, read_companies.
[Anchor to COMPANIES_DELETE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-COMPANIES_DELETE)COMPANIES_DELETE

    
The webhook topic for `companies/delete` events. Occurs whenever a company is deleted. Requires at least one of the following scopes: read_customers, read_companies.
[Anchor to COMPANIES_UPDATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-COMPANIES_UPDATE)COMPANIES_UPDATE

    
The webhook topic for `companies/update` events. Occurs whenever a company is updated. Requires at least one of the following scopes: read_customers, read_companies.
[Anchor to COMPANY_CONTACT_ROLES_ASSIGN](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-COMPANY_CONTACT_ROLES_ASSIGN)COMPANY_CONTACT_ROLES_ASSIGN

    
The webhook topic for `company_contact_roles/assign` events. Occurs whenever a role is assigned to a contact at a location. Requires at least one of the following scopes: read_customers, read_companies.
[Anchor to COMPANY_CONTACT_ROLES_REVOKE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-COMPANY_CONTACT_ROLES_REVOKE)COMPANY_CONTACT_ROLES_REVOKE

    
The webhook topic for `company_contact_roles/revoke` events. Occurs whenever a role is revoked from a contact at a location. Requires at least one of the following scopes: read_customers, read_companies.
[Anchor to COMPANY_CONTACTS_CREATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-COMPANY_CONTACTS_CREATE)COMPANY_CONTACTS_CREATE

    
The webhook topic for `company_contacts/create` events. Occurs whenever a company contact is created. Requires at least one of the following scopes: read_customers, read_companies.
[Anchor to COMPANY_CONTACTS_DELETE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-COMPANY_CONTACTS_DELETE)COMPANY_CONTACTS_DELETE

    
The webhook topic for `company_contacts/delete` events. Occurs whenever a company contact is deleted. Requires at least one of the following scopes: read_customers, read_companies.
[Anchor to COMPANY_CONTACTS_UPDATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-COMPANY_CONTACTS_UPDATE)COMPANY_CONTACTS_UPDATE

    
The webhook topic for `company_contacts/update` events. Occurs whenever a company contact is updated. Requires at least one of the following scopes: read_customers, read_companies.
[Anchor to COMPANY_LOCATIONS_CREATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-COMPANY_LOCATIONS_CREATE)COMPANY_LOCATIONS_CREATE

    
The webhook topic for `company_locations/create` events. Occurs whenever a company location is created. Requires at least one of the following scopes: read_customers, read_companies.
[Anchor to COMPANY_LOCATIONS_DELETE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-COMPANY_LOCATIONS_DELETE)COMPANY_LOCATIONS_DELETE

    
The webhook topic for `company_locations/delete` events. Occurs whenever a company location is deleted. Requires at least one of the following scopes: read_customers, read_companies.
[Anchor to COMPANY_LOCATIONS_UPDATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-COMPANY_LOCATIONS_UPDATE)COMPANY_LOCATIONS_UPDATE

    
The webhook topic for `company_locations/update` events. Occurs whenever a company location is updated. Requires at least one of the following scopes: read_customers, read_companies.
[Anchor to CUSTOMER_ACCOUNT_SETTINGS_UPDATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-CUSTOMER_ACCOUNT_SETTINGS_UPDATE)CUSTOMER_ACCOUNT_SETTINGS_UPDATE

    
The webhook topic for `customer_account_settings/update` events. Triggers when merchants change customer account setting.
[Anchor to CUSTOMER_GROUPS_CREATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-CUSTOMER_GROUPS_CREATE)CUSTOMER_GROUPS_CREATE

    
The webhook topic for `customer_groups/create` events. Occurs whenever a customer saved search is created. Requires the `read_customers` scope.
[Anchor to CUSTOMER_GROUPS_DELETE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-CUSTOMER_GROUPS_DELETE)CUSTOMER_GROUPS_DELETE

    
The webhook topic for `customer_groups/delete` events. Occurs whenever a customer saved search is deleted. Requires the `read_customers` scope.
[Anchor to CUSTOMER_GROUPS_UPDATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-CUSTOMER_GROUPS_UPDATE)CUSTOMER_GROUPS_UPDATE

    
The webhook topic for `customer_groups/update` events. Occurs whenever a customer saved search is updated. Requires the `read_customers` scope.
[Anchor to CUSTOMER_JOINED_SEGMENT](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-CUSTOMER_JOINED_SEGMENT)CUSTOMER_JOINED_SEGMENT

    
The webhook topic for `customer.joined_segment` events. Triggers when a customer joins a segment. Requires the `read_customers` scope.
[Anchor to CUSTOMER_LEFT_SEGMENT](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-CUSTOMER_LEFT_SEGMENT)CUSTOMER_LEFT_SEGMENT

    
The webhook topic for `customer.left_segment` events. Triggers when a customer leaves a segment. Requires the `read_customers` scope.
[Anchor to CUSTOMER_PAYMENT_METHODS_CREATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-CUSTOMER_PAYMENT_METHODS_CREATE)CUSTOMER_PAYMENT_METHODS_CREATE

    
The webhook topic for `customer_payment_methods/create` events. Occurs whenever a customer payment method is created. Requires the `read_customer_payment_methods` scope.
[Anchor to CUSTOMER_PAYMENT_METHODS_REVOKE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-CUSTOMER_PAYMENT_METHODS_REVOKE)CUSTOMER_PAYMENT_METHODS_REVOKE

    
The webhook topic for `customer_payment_methods/revoke` events. Occurs whenever a customer payment method is revoked. Requires the `read_customer_payment_methods` scope.
[Anchor to CUSTOMER_PAYMENT_METHODS_UPDATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-CUSTOMER_PAYMENT_METHODS_UPDATE)CUSTOMER_PAYMENT_METHODS_UPDATE

    
The webhook topic for `customer_payment_methods/update` events. Occurs whenever a customer payment method is updated. Requires the `read_customer_payment_methods` scope.
[Anchor to CUSTOMER_TAGS_ADDED](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-CUSTOMER_TAGS_ADDED)CUSTOMER_TAGS_ADDED

    
The webhook topic for `customer.tags_added` events. Triggers when tags are added to a customer. Requires the `read_customers` scope.
[Anchor to CUSTOMER_TAGS_REMOVED](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-CUSTOMER_TAGS_REMOVED)CUSTOMER_TAGS_REMOVED

    
The webhook topic for `customer.tags_removed` events. Triggers when tags are removed from a customer. Requires the `read_customers` scope.
[Anchor to CUSTOMERS_CREATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-CUSTOMERS_CREATE)CUSTOMERS_CREATE

    
The webhook topic for `customers/create` events. Occurs whenever a customer is created. Requires the `read_customers` scope.
[Anchor to CUSTOMERS_DELETE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-CUSTOMERS_DELETE)CUSTOMERS_DELETE

    
The webhook topic for `customers/delete` events. Occurs whenever a customer is deleted. Requires the `read_customers` scope.
[Anchor to CUSTOMERS_DISABLE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-CUSTOMERS_DISABLE)CUSTOMERS_DISABLE

    
The webhook topic for `customers/disable` events. Occurs whenever a customer account is disabled. Requires the `read_customers` scope.
[Anchor to CUSTOMERS_EMAIL_MARKETING_CONSENT_UPDATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-CUSTOMERS_EMAIL_MARKETING_CONSENT_UPDATE)CUSTOMERS_EMAIL_MARKETING_CONSENT_UPDATE

    
The webhook topic for `customers_email_marketing_consent/update` events. Occurs whenever a customer's email marketing consent is updated. Requires the `read_customers` scope.
[Anchor to CUSTOMERS_ENABLE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-CUSTOMERS_ENABLE)CUSTOMERS_ENABLE

    
The webhook topic for `customers/enable` events. Occurs whenever a customer account is enabled. Requires the `read_customers` scope.
[Anchor to CUSTOMERS_MARKETING_CONSENT_UPDATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-CUSTOMERS_MARKETING_CONSENT_UPDATE)CUSTOMERS_MARKETING_CONSENT_UPDATE

    
The webhook topic for `customers_marketing_consent/update` events. Occurs whenever a customer's SMS marketing consent is updated. Requires the `read_customers` scope.
[Anchor to CUSTOMERS_MERGE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-CUSTOMERS_MERGE)CUSTOMERS_MERGE

    
The webhook topic for `customers/merge` events. Triggers when two customers are merged Requires the `read_customer_merge` scope.
[Anchor to CUSTOMERS_PURCHASING_SUMMARY](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-CUSTOMERS_PURCHASING_SUMMARY)CUSTOMERS_PURCHASING_SUMMARY

    
The webhook topic for `customers/purchasing_summary` events. Occurs when a customer sales history change. Requires the `read_customers` scope.
[Anchor to CUSTOMERS_UPDATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-CUSTOMERS_UPDATE)CUSTOMERS_UPDATE

    
The webhook topic for `customers/update` events. Occurs whenever a customer is updated. Requires the `read_customers` scope.
[Anchor to CUSTOMERS_WHATS_APP_MARKETING_CONSENT_UPDATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-CUSTOMERS_WHATS_APP_MARKETING_CONSENT_UPDATE)CUSTOMERS_WHATS_APP_MARKETING_CONSENT_UPDATE

    
The webhook topic for `customers_whats_app_marketing_consent/update` events. Occurs whenever a customer's WhatsApp marketing consent is updated. Requires the `read_customers` scope.
[Anchor to DELIVERY_PROMISE_SETTINGS_UPDATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-DELIVERY_PROMISE_SETTINGS_UPDATE)DELIVERY_PROMISE_SETTINGS_UPDATE

    
The webhook topic for `delivery_promise_settings/update` events. Occurs when a promise setting is updated. Requires the `read_shipping` scope.
[Anchor to DISCOUNTS_CREATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-DISCOUNTS_CREATE)DISCOUNTS_CREATE

    
The webhook topic for `discounts/create` events. Occurs whenever a discount is created. Requires the `read_discounts` scope.
[Anchor to DISCOUNTS_DELETE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-DISCOUNTS_DELETE)DISCOUNTS_DELETE

    
The webhook topic for `discounts/delete` events. Occurs whenever a discount is deleted. Requires the `read_discounts` scope.
[Anchor to DISCOUNTS_REDEEMCODE_ADDED](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-DISCOUNTS_REDEEMCODE_ADDED)DISCOUNTS_REDEEMCODE_ADDED

    
The webhook topic for `discounts/redeemcode_added` events. Occurs whenever a redeem code is added to a code discount. Requires the `read_discounts` scope.
[Anchor to DISCOUNTS_REDEEMCODE_REMOVED](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-DISCOUNTS_REDEEMCODE_REMOVED)DISCOUNTS_REDEEMCODE_REMOVED

    
The webhook topic for `discounts/redeemcode_removed` events. Occurs whenever a redeem code on a code discount is deleted. Requires the `read_discounts` scope.
[Anchor to DISCOUNTS_UPDATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-DISCOUNTS_UPDATE)DISCOUNTS_UPDATE

    
The webhook topic for `discounts/update` events. Occurs whenever a discount is updated. Requires the `read_discounts` scope.
[Anchor to DISPUTES_CREATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-DISPUTES_CREATE)DISPUTES_CREATE

    
The webhook topic for `disputes/create` events. Occurs whenever a dispute is created. Requires the `read_shopify_payments_disputes` scope.
[Anchor to DISPUTES_UPDATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-DISPUTES_UPDATE)DISPUTES_UPDATE

    
The webhook topic for `disputes/update` events. Occurs whenever a dispute is updated. Requires the `read_shopify_payments_disputes` scope.
[Anchor to DOMAINS_CREATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-DOMAINS_CREATE)DOMAINS_CREATE

    
The webhook topic for `domains/create` events. Occurs whenever a domain is created.
[Anchor to DOMAINS_DESTROY](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-DOMAINS_DESTROY)DOMAINS_DESTROY

    
The webhook topic for `domains/destroy` events. Occurs whenever a domain is destroyed.
[Anchor to DOMAINS_UPDATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-DOMAINS_UPDATE)DOMAINS_UPDATE

    
The webhook topic for `domains/update` events. Occurs whenever a domain is updated.
[Anchor to DRAFT_ORDERS_CREATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-DRAFT_ORDERS_CREATE)DRAFT_ORDERS_CREATE

    
The webhook topic for `draft_orders/create` events. Occurs whenever a draft order is created. Requires the `read_draft_orders` scope.
[Anchor to DRAFT_ORDERS_DELETE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-DRAFT_ORDERS_DELETE)DRAFT_ORDERS_DELETE

    
The webhook topic for `draft_orders/delete` events. Occurs whenever a draft order is deleted. Requires the `read_draft_orders` scope.
[Anchor to DRAFT_ORDERS_UPDATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-DRAFT_ORDERS_UPDATE)DRAFT_ORDERS_UPDATE

    
The webhook topic for `draft_orders/update` events. Occurs whenever a draft order is updated. Requires the `read_draft_orders` scope.
[Anchor to FINANCE_APP_STAFF_MEMBER_DELETE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-FINANCE_APP_STAFF_MEMBER_DELETE)FINANCE_APP_STAFF_MEMBER_DELETE

    
The webhook topic for `finance_app_staff_member/delete` events. Triggers when a staff with access to all or some finance app has been removed. Requires the `read_financial_kyc_information` scope.
[Anchor to FINANCE_APP_STAFF_MEMBER_GRANT](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-FINANCE_APP_STAFF_MEMBER_GRANT)FINANCE_APP_STAFF_MEMBER_GRANT

    
The webhook topic for `finance_app_staff_member/grant` events. Triggers when a staff is granted access to all or some finance app. Requires the `read_financial_kyc_information` scope.
[Anchor to FINANCE_APP_STAFF_MEMBER_REVOKE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-FINANCE_APP_STAFF_MEMBER_REVOKE)FINANCE_APP_STAFF_MEMBER_REVOKE

    
The webhook topic for `finance_app_staff_member/revoke` events. Triggers when a staff's access to all or some finance app has been revoked. Requires the `read_financial_kyc_information` scope.
[Anchor to FINANCE_APP_STAFF_MEMBER_UPDATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-FINANCE_APP_STAFF_MEMBER_UPDATE)FINANCE_APP_STAFF_MEMBER_UPDATE

    
The webhook topic for `finance_app_staff_member/update` events. Triggers when a staff's information has been updated. Requires the `read_financial_kyc_information` scope.
[Anchor to FINANCE_KYC_INFORMATION_UPDATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-FINANCE_KYC_INFORMATION_UPDATE)FINANCE_KYC_INFORMATION_UPDATE

    
The webhook topic for `finance_kyc_information/update` events. Occurs whenever shop's finance KYC information was updated Requires the `read_financial_kyc_information` scope.
[Anchor to FULFILLMENT_EVENTS_CREATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-FULFILLMENT_EVENTS_CREATE)FULFILLMENT_EVENTS_CREATE

    
The webhook topic for `fulfillment_events/create` events. Occurs whenever a fulfillment event is created. Requires the `read_fulfillments` scope.
[Anchor to FULFILLMENT_EVENTS_DELETE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-FULFILLMENT_EVENTS_DELETE)FULFILLMENT_EVENTS_DELETE

    
The webhook topic for `fulfillment_events/delete` events. Occurs whenever a fulfillment event is deleted. Requires the `read_fulfillments` scope.
[Anchor to FULFILLMENT_HOLDS_ADDED](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-FULFILLMENT_HOLDS_ADDED)FULFILLMENT_HOLDS_ADDED

    
The webhook topic for `fulfillment_holds/added` events. Occurs each time that a hold is added to a fulfillment order.
For cases where multiple holds are applied to a fulfillment order, this webhook will trigger after each hold is applied. Requires at least one of the following scopes: read_merchant_managed_fulfillment_orders, read_assigned_fulfillment_orders, read_third_party_fulfillment_orders, read_marketplace_fulfillment_orders.
[Anchor to FULFILLMENT_HOLDS_RELEASED](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-FULFILLMENT_HOLDS_RELEASED)FULFILLMENT_HOLDS_RELEASED

    
The webhook topic for `fulfillment_holds/released` events. Occurs each time that a hold is released from a fulfillment order. For cases where multiple holds are released from a fulfillment order a the same time, this webhook will trigger for each released hold. Requires at least one of the following scopes: read_merchant_managed_fulfillment_orders, read_assigned_fulfillment_orders, read_third_party_fulfillment_orders, read_marketplace_fulfillment_orders.
[Anchor to FULFILLMENT_ORDERS_CANCELLATION_REQUEST_ACCEPTED](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-FULFILLMENT_ORDERS_CANCELLATION_REQUEST_ACCEPTED)FULFILLMENT_ORDERS_CANCELLATION_REQUEST_ACCEPTED

    
The webhook topic for `fulfillment_orders/cancellation_request_accepted` events. Occurs when a 3PL accepts a fulfillment cancellation request, received from a merchant. Requires at least one of the following scopes: read_merchant_managed_fulfillment_orders, read_assigned_fulfillment_orders, read_third_party_fulfillment_orders, read_marketplace_fulfillment_orders.
[Anchor to FULFILLMENT_ORDERS_CANCELLATION_REQUEST_REJECTED](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-FULFILLMENT_ORDERS_CANCELLATION_REQUEST_REJECTED)FULFILLMENT_ORDERS_CANCELLATION_REQUEST_REJECTED

    
The webhook topic for `fulfillment_orders/cancellation_request_rejected` events. Occurs when a 3PL rejects a fulfillment cancellation request, received from a merchant. Requires at least one of the following scopes: read_merchant_managed_fulfillment_orders, read_assigned_fulfillment_orders, read_third_party_fulfillment_orders, read_marketplace_fulfillment_orders.
[Anchor to FULFILLMENT_ORDERS_CANCELLATION_REQUEST_SUBMITTED](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-FULFILLMENT_ORDERS_CANCELLATION_REQUEST_SUBMITTED)FULFILLMENT_ORDERS_CANCELLATION_REQUEST_SUBMITTED

    
The webhook topic for `fulfillment_orders/cancellation_request_submitted` events. Occurs when a merchant requests a fulfillment request to be cancelled after that request was approved by a 3PL. Requires at least one of the following scopes: read_merchant_managed_fulfillment_orders, read_assigned_fulfillment_orders, read_third_party_fulfillment_orders, read_marketplace_fulfillment_orders.
[Anchor to FULFILLMENT_ORDERS_CANCELLED](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-FULFILLMENT_ORDERS_CANCELLED)FULFILLMENT_ORDERS_CANCELLED

    
The webhook topic for `fulfillment_orders/cancelled` events. Occurs when a fulfillment order is cancelled. Requires at least one of the following scopes: read_merchant_managed_fulfillment_orders, read_assigned_fulfillment_orders, read_third_party_fulfillment_orders, read_marketplace_fulfillment_orders.
[Anchor to FULFILLMENT_ORDERS_FULFILLMENT_REQUEST_ACCEPTED](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-FULFILLMENT_ORDERS_FULFILLMENT_REQUEST_ACCEPTED)FULFILLMENT_ORDERS_FULFILLMENT_REQUEST_ACCEPTED

    
The webhook topic for `fulfillment_orders/fulfillment_request_accepted` events. Occurs when a fulfillment service accepts a request to fulfill a fulfillment order. Requires at least one of the following scopes: read_merchant_managed_fulfillment_orders, read_assigned_fulfillment_orders, read_third_party_fulfillment_orders, read_marketplace_fulfillment_orders.
[Anchor to FULFILLMENT_ORDERS_FULFILLMENT_REQUEST_REJECTED](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-FULFILLMENT_ORDERS_FULFILLMENT_REQUEST_REJECTED)FULFILLMENT_ORDERS_FULFILLMENT_REQUEST_REJECTED

    
The webhook topic for `fulfillment_orders/fulfillment_request_rejected` events. Occurs when a 3PL rejects a fulfillment request that was sent by a merchant. Requires at least one of the following scopes: read_merchant_managed_fulfillment_orders, read_assigned_fulfillment_orders, read_third_party_fulfillment_orders, read_marketplace_fulfillment_orders.
[Anchor to FULFILLMENT_ORDERS_FULFILLMENT_REQUEST_SUBMITTED](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-FULFILLMENT_ORDERS_FULFILLMENT_REQUEST_SUBMITTED)FULFILLMENT_ORDERS_FULFILLMENT_REQUEST_SUBMITTED

    
The webhook topic for `fulfillment_orders/fulfillment_request_submitted` events. Occurs when a merchant submits a fulfillment request to a 3PL. Requires at least one of the following scopes: read_merchant_managed_fulfillment_orders, read_assigned_fulfillment_orders, read_third_party_fulfillment_orders, read_marketplace_fulfillment_orders.
[Anchor to FULFILLMENT_ORDERS_FULFILLMENT_SERVICE_FAILED_TO_COMPLETE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-FULFILLMENT_ORDERS_FULFILLMENT_SERVICE_FAILED_TO_COMPLETE)FULFILLMENT_ORDERS_FULFILLMENT_SERVICE_FAILED_TO_COMPLETE

    
The webhook topic for `fulfillment_orders/fulfillment_service_failed_to_complete` events. Occurs when a fulfillment service intends to close an in_progress fulfillment order. Requires at least one of the following scopes: read_merchant_managed_fulfillment_orders, read_assigned_fulfillment_orders, read_third_party_fulfillment_orders, read_marketplace_fulfillment_orders.
[Anchor to FULFILLMENT_ORDERS_HOLD_RELEASED](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-FULFILLMENT_ORDERS_HOLD_RELEASED)FULFILLMENT_ORDERS_HOLD_RELEASED

    
The webhook topic for `fulfillment_orders/hold_released` events. Occurs when a fulfillment order is released and is no longer on hold.
If a fulfillment order has multiple holds then this webhook will only be triggered once when the last hold is released and the status of the fulfillment order is no longer `ON_HOLD`. Requires at least one of the following scopes: read_merchant_managed_fulfillment_orders, read_assigned_fulfillment_orders, read_third_party_fulfillment_orders, read_marketplace_fulfillment_orders.
[Anchor to FULFILLMENT_ORDERS_LINE_ITEMS_PREPARED_FOR_LOCAL_DELIVERY](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-FULFILLMENT_ORDERS_LINE_ITEMS_PREPARED_FOR_LOCAL_DELIVERY)FULFILLMENT_ORDERS_LINE_ITEMS_PREPARED_FOR_LOCAL_DELIVERY

    
The webhook topic for `fulfillment_orders/line_items_prepared_for_local_delivery` events. Occurs whenever a fulfillment order's line items are prepared for local delivery. Requires at least one of the following scopes: read_merchant_managed_fulfillment_orders, read_assigned_fulfillment_orders, read_third_party_fulfillment_orders, read_marketplace_fulfillment_orders.
[Anchor to FULFILLMENT_ORDERS_LINE_ITEMS_PREPARED_FOR_PICKUP](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-FULFILLMENT_ORDERS_LINE_ITEMS_PREPARED_FOR_PICKUP)FULFILLMENT_ORDERS_LINE_ITEMS_PREPARED_FOR_PICKUP

    
The webhook topic for `fulfillment_orders/line_items_prepared_for_pickup` events. Triggers when one or more of the line items for a fulfillment order are prepared for pickup Requires at least one of the following scopes: read_merchant_managed_fulfillment_orders, read_assigned_fulfillment_orders, read_third_party_fulfillment_orders, read_marketplace_fulfillment_orders.
[Anchor to FULFILLMENT_ORDERS_MANUALLY_REPORTED_PROGRESS_STOPPED](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-FULFILLMENT_ORDERS_MANUALLY_REPORTED_PROGRESS_STOPPED)FULFILLMENT_ORDERS_MANUALLY_REPORTED_PROGRESS_STOPPED

    
The webhook topic for `fulfillment_orders/manually_reported_progress_stopped` events. Occurs when a fulfillment order that has previously been manually marked as in progress is marked back as open. Requires at least one of the following scopes: read_merchant_managed_fulfillment_orders, read_assigned_fulfillment_orders, read_third_party_fulfillment_orders.
[Anchor to FULFILLMENT_ORDERS_MERGED](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-FULFILLMENT_ORDERS_MERGED)FULFILLMENT_ORDERS_MERGED

    
The webhook topic for `fulfillment_orders/merged` events. Occurs when multiple fulfillment orders are merged into a single fulfillment order. Requires at least one of the following scopes: read_merchant_managed_fulfillment_orders, read_assigned_fulfillment_orders, read_third_party_fulfillment_orders.
[Anchor to FULFILLMENT_ORDERS_MOVED](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-FULFILLMENT_ORDERS_MOVED)FULFILLMENT_ORDERS_MOVED

    
The webhook topic for `fulfillment_orders/moved` events. Occurs whenever the location which is assigned to fulfill one or more fulfillment order line items is changed.
  * `original_fulfillment_order` - The final state of the original fulfillment order.
  * `moved_fulfillment_order` - The fulfillment order which now contains the re-assigned line items.
  * `source_location` - The original location which was assigned to fulfill the line items (available as of the `2023-04` API version).
  * `destination_location_id` - The ID of the location which is now responsible for fulfilling the line items.


**Note:** The [assignedLocation](https://shopify.dev/docs/api/admin-graphql/latest/objects/fulfillmentorder#field-fulfillmentorder-assignedlocation) of the `original_fulfillment_order` might be changed by the move operation. If you need to determine the originally assigned location, then you should refer to the `source_location`.
[Learn more about moving line items](https://shopify.dev/docs/api/admin-graphql/latest/mutations/fulfillmentOrderMove). Requires at least one of the following scopes: read_merchant_managed_fulfillment_orders, read_assigned_fulfillment_orders, read_third_party_fulfillment_orders, read_marketplace_fulfillment_orders.
[Anchor to FULFILLMENT_ORDERS_ORDER_ROUTING_COMPLETE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-FULFILLMENT_ORDERS_ORDER_ROUTING_COMPLETE)FULFILLMENT_ORDERS_ORDER_ROUTING_COMPLETE

    
The webhook topic for `fulfillment_orders/order_routing_complete` events. Occurs when an order has finished being routed and it's fulfillment orders assigned to a fulfillment service's location. Requires at least one of the following scopes: read_merchant_managed_fulfillment_orders, read_assigned_fulfillment_orders, read_third_party_fulfillment_orders, read_buyer_membership_orders, read_marketplace_fulfillment_orders.
[Anchor to FULFILLMENT_ORDERS_PLACED_ON_HOLD](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-FULFILLMENT_ORDERS_PLACED_ON_HOLD)FULFILLMENT_ORDERS_PLACED_ON_HOLD

    
The webhook topic for `fulfillment_orders/placed_on_hold` events. Occurs when a fulfillment order transitions to the `ON_HOLD` status
For cases where multiple holds are applied to a fulfillment order, this webhook will only trigger once when the first hold is applied and the fulfillment order status changes to `ON_HOLD`. Requires at least one of the following scopes: read_merchant_managed_fulfillment_orders, read_assigned_fulfillment_orders, read_third_party_fulfillment_orders, read_marketplace_fulfillment_orders.
[Anchor to FULFILLMENT_ORDERS_PROGRESS_REPORTED](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-FULFILLMENT_ORDERS_PROGRESS_REPORTED)FULFILLMENT_ORDERS_PROGRESS_REPORTED

    
The webhook topic for `fulfillment_orders/progress_reported` events. Occurs when progress is reported for a fulfillment order. Requires at least one of the following scopes: read_merchant_managed_fulfillment_orders, read_assigned_fulfillment_orders, read_third_party_fulfillment_orders.
[Anchor to FULFILLMENT_ORDERS_RESCHEDULED](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-FULFILLMENT_ORDERS_RESCHEDULED)FULFILLMENT_ORDERS_RESCHEDULED

    
The webhook topic for `fulfillment_orders/rescheduled` events. Triggers when a fulfillment order is rescheduled.
Fulfillment orders may be merged if they have the same `fulfillAt` datetime. If the fulfillment order is merged then the resulting fulfillment order will be indicated in the webhook body. Otherwise it will be the original fulfillment order with an updated `fulfill_at` datetime. Requires at least one of the following scopes: read_merchant_managed_fulfillment_orders, read_assigned_fulfillment_orders, read_third_party_fulfillment_orders, read_marketplace_fulfillment_orders.
[Anchor to FULFILLMENT_ORDERS_SCHEDULED_FULFILLMENT_ORDER_READY](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-FULFILLMENT_ORDERS_SCHEDULED_FULFILLMENT_ORDER_READY)FULFILLMENT_ORDERS_SCHEDULED_FULFILLMENT_ORDER_READY

    
The webhook topic for `fulfillment_orders/scheduled_fulfillment_order_ready` events. Occurs whenever a fulfillment order which was scheduled becomes due. Requires at least one of the following scopes: read_merchant_managed_fulfillment_orders, read_assigned_fulfillment_orders, read_third_party_fulfillment_orders, read_marketplace_fulfillment_orders.
[Anchor to FULFILLMENT_ORDERS_SPLIT](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-FULFILLMENT_ORDERS_SPLIT)FULFILLMENT_ORDERS_SPLIT

    
The webhook topic for `fulfillment_orders/split` events. Occurs when a fulfillment order is split into multiple fulfillment orders. Requires at least one of the following scopes: read_merchant_managed_fulfillment_orders, read_assigned_fulfillment_orders, read_third_party_fulfillment_orders.
[Anchor to FULFILLMENTS_CREATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-FULFILLMENTS_CREATE)FULFILLMENTS_CREATE

    
The webhook topic for `fulfillments/create` events. Occurs whenever a fulfillment is created. Requires at least one of the following scopes: read_fulfillments, read_marketplace_orders.
[Anchor to FULFILLMENTS_UPDATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-FULFILLMENTS_UPDATE)FULFILLMENTS_UPDATE

    
The webhook topic for `fulfillments/update` events. Occurs whenever a fulfillment is updated. Requires at least one of the following scopes: read_fulfillments, read_marketplace_orders.
[Anchor to INVENTORY_ITEMS_CREATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-INVENTORY_ITEMS_CREATE)INVENTORY_ITEMS_CREATE

    
The webhook topic for `inventory_items/create` events. Occurs whenever an inventory item is created. Requires at least one of the following scopes: read_inventory, read_products.
[Anchor to INVENTORY_ITEMS_DELETE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-INVENTORY_ITEMS_DELETE)INVENTORY_ITEMS_DELETE

    
The webhook topic for `inventory_items/delete` events. Occurs whenever an inventory item is deleted. Requires at least one of the following scopes: read_inventory, read_products.
[Anchor to INVENTORY_ITEMS_UPDATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-INVENTORY_ITEMS_UPDATE)INVENTORY_ITEMS_UPDATE

    
The webhook topic for `inventory_items/update` events. Occurs whenever an inventory item is updated. Requires at least one of the following scopes: read_inventory, read_products.
[Anchor to INVENTORY_LEVELS_CONNECT](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-INVENTORY_LEVELS_CONNECT)INVENTORY_LEVELS_CONNECT

    
The webhook topic for `inventory_levels/connect` events. Occurs whenever an inventory level is connected. Requires the `read_inventory` scope.
[Anchor to INVENTORY_LEVELS_DISCONNECT](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-INVENTORY_LEVELS_DISCONNECT)INVENTORY_LEVELS_DISCONNECT

    
The webhook topic for `inventory_levels/disconnect` events. Occurs whenever an inventory level is disconnected. Requires the `read_inventory` scope.
[Anchor to INVENTORY_LEVELS_UPDATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-INVENTORY_LEVELS_UPDATE)INVENTORY_LEVELS_UPDATE

    
The webhook topic for `inventory_levels/update` events. Occurs whenever an inventory level is updated. Requires the `read_inventory` scope.
[Anchor to INVENTORY_SHIPMENTS_ADD_ITEMS](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-INVENTORY_SHIPMENTS_ADD_ITEMS)INVENTORY_SHIPMENTS_ADD_ITEMS

    
The webhook topic for `inventory_shipments/add_items` events. Occurs whenever items are added to a shipment. Requires the `read_inventory_shipments` scope.
[Anchor to INVENTORY_SHIPMENTS_CREATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-INVENTORY_SHIPMENTS_CREATE)INVENTORY_SHIPMENTS_CREATE

    
The webhook topic for `inventory_shipments/create` events. Triggers when a shipment is created. Requires the `read_inventory_shipments` scope.
[Anchor to INVENTORY_SHIPMENTS_DELETE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-INVENTORY_SHIPMENTS_DELETE)INVENTORY_SHIPMENTS_DELETE

    
The webhook topic for `inventory_shipments/delete` events. Triggers when a shipment is deleted. Requires the `read_inventory_shipments` scope.
[Anchor to INVENTORY_SHIPMENTS_MARK_IN_TRANSIT](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-INVENTORY_SHIPMENTS_MARK_IN_TRANSIT)INVENTORY_SHIPMENTS_MARK_IN_TRANSIT

    
The webhook topic for `inventory_shipments/mark_in_transit` events. Triggers when a shipment is marked as in transit. Requires the `read_inventory_shipments` scope.
[Anchor to INVENTORY_SHIPMENTS_RECEIVE_ITEMS](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-INVENTORY_SHIPMENTS_RECEIVE_ITEMS)INVENTORY_SHIPMENTS_RECEIVE_ITEMS

    
The webhook topic for `inventory_shipments/receive_items` events. Triggers when items on a shipment are received. Requires the `read_inventory_shipments_received_items` scope.
[Anchor to INVENTORY_SHIPMENTS_REMOVE_ITEMS](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-INVENTORY_SHIPMENTS_REMOVE_ITEMS)INVENTORY_SHIPMENTS_REMOVE_ITEMS

    
The webhook topic for `inventory_shipments/remove_items` events. Occurs whenever items are removed from a shipment. Requires the `read_inventory_shipments` scope.
[Anchor to INVENTORY_SHIPMENTS_UPDATE_ITEM_QUANTITIES](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-INVENTORY_SHIPMENTS_UPDATE_ITEM_QUANTITIES)INVENTORY_SHIPMENTS_UPDATE_ITEM_QUANTITIES

    
The webhook topic for `inventory_shipments/update_item_quantities` events. Occurs whenever quantities change on a shipment. Requires the `read_inventory_shipments` scope.
[Anchor to INVENTORY_SHIPMENTS_UPDATE_TRACKING](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-INVENTORY_SHIPMENTS_UPDATE_TRACKING)INVENTORY_SHIPMENTS_UPDATE_TRACKING

    
The webhook topic for `inventory_shipments/update_tracking` events. Triggers when tracking info on a shipment is updated. Requires the `read_inventory_shipments` scope.
[Anchor to INVENTORY_TRANSFERS_ADD_ITEMS](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-INVENTORY_TRANSFERS_ADD_ITEMS)INVENTORY_TRANSFERS_ADD_ITEMS

    
The webhook topic for `inventory_transfers/add_items` events. Occurs any time items are added to a transfer. Requires the `read_inventory_transfers` scope.
[Anchor to INVENTORY_TRANSFERS_CANCEL](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-INVENTORY_TRANSFERS_CANCEL)INVENTORY_TRANSFERS_CANCEL

    
The webhook topic for `inventory_transfers/cancel` events. Triggers when a transfer is canceled. Requires the `read_inventory_transfers` scope.
[Anchor to INVENTORY_TRANSFERS_COMPLETE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-INVENTORY_TRANSFERS_COMPLETE)INVENTORY_TRANSFERS_COMPLETE

    
The webhook topic for `inventory_transfers/complete` events. Triggers when a transfer is completed. Requires the `read_inventory_transfers` scope.
[Anchor to INVENTORY_TRANSFERS_READY_TO_SHIP](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-INVENTORY_TRANSFERS_READY_TO_SHIP)INVENTORY_TRANSFERS_READY_TO_SHIP

    
The webhook topic for `inventory_transfers/ready_to_ship` events. Triggers when a transfer is marked as ready to ship. Requires the `read_inventory_transfers` scope.
[Anchor to INVENTORY_TRANSFERS_REMOVE_ITEMS](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-INVENTORY_TRANSFERS_REMOVE_ITEMS)INVENTORY_TRANSFERS_REMOVE_ITEMS

    
The webhook topic for `inventory_transfers/remove_items` events. Occurs any time items are removed from a transfer. Requires the `read_inventory_transfers` scope.
[Anchor to INVENTORY_TRANSFERS_UPDATE_ITEM_QUANTITIES](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-INVENTORY_TRANSFERS_UPDATE_ITEM_QUANTITIES)INVENTORY_TRANSFERS_UPDATE_ITEM_QUANTITIES

    
The webhook topic for `inventory_transfers/update_item_quantities` events. Occurs whenever the quantity of transfer line items changes. Requires the `read_inventory_transfers` scope.
[Anchor to INVENTORY_TRANSFERS_UPDATED](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-INVENTORY_TRANSFERS_UPDATED)INVENTORY_TRANSFERS_UPDATED

    
The webhook topic for `inventory_transfers/updated` events. Triggers when a shipment belonging to the transfer is created, edited, or removed. Re-fetch the transfer to get the latest state. Requires the `read_inventory_transfers` scope.
[Anchor to LOCALES_CREATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-LOCALES_CREATE)LOCALES_CREATE

    
The webhook topic for `locales/create` events. Occurs whenever a shop locale is created Requires the `read_locales` scope.
[Anchor to LOCALES_DESTROY](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-LOCALES_DESTROY)LOCALES_DESTROY

    
The webhook topic for `locales/destroy` events. Occurs whenever a shop locale is destroyed Requires the `read_locales` scope.
[Anchor to LOCALES_UPDATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-LOCALES_UPDATE)LOCALES_UPDATE

    
The webhook topic for `locales/update` events. Occurs whenever a shop locale is updated, such as published or unpublished Requires the `read_locales` scope.
[Anchor to LOCATIONS_ACTIVATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-LOCATIONS_ACTIVATE)LOCATIONS_ACTIVATE

    
The webhook topic for `locations/activate` events. Occurs whenever a deactivated location is re-activated. Requires the `read_locations` scope.
[Anchor to LOCATIONS_CREATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-LOCATIONS_CREATE)LOCATIONS_CREATE

    
The webhook topic for `locations/create` events. Occurs whenever a location is created. Requires the `read_locations` scope.
[Anchor to LOCATIONS_DEACTIVATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-LOCATIONS_DEACTIVATE)LOCATIONS_DEACTIVATE

    
The webhook topic for `locations/deactivate` events. Occurs whenever a location is deactivated. Requires the `read_locations` scope.
[Anchor to LOCATIONS_DELETE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-LOCATIONS_DELETE)LOCATIONS_DELETE

    
The webhook topic for `locations/delete` events. Occurs whenever a location is deleted. Requires the `read_locations` scope.
[Anchor to LOCATIONS_UPDATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-LOCATIONS_UPDATE)LOCATIONS_UPDATE

    
The webhook topic for `locations/update` events. Occurs whenever a location is updated. Requires the `read_locations` scope.
[Anchor to MARKETS_BACKUP_REGION_UPDATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-MARKETS_BACKUP_REGION_UPDATE)MARKETS_BACKUP_REGION_UPDATE

    
The webhook topic for `markets_backup_region/update` events. Occurs when a backup region is updated. Requires the `read_markets` scope.
[Anchor to MARKETS_CREATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-MARKETS_CREATE)MARKETS_CREATE

    
The webhook topic for `markets/create` events. Occurs when a new market is created. Requires the `read_markets` scope.
[Anchor to MARKETS_DELETE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-MARKETS_DELETE)MARKETS_DELETE

    
The webhook topic for `markets/delete` events. Occurs when a market is deleted. Requires the `read_markets` scope.
[Anchor to MARKETS_UPDATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-MARKETS_UPDATE)MARKETS_UPDATE

    
The webhook topic for `markets/update` events. Occurs when a market is updated. Requires the `read_markets` scope.
[Anchor to METAFIELD_DEFINITIONS_CREATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-METAFIELD_DEFINITIONS_CREATE)METAFIELD_DEFINITIONS_CREATE

    
The webhook topic for `metafield_definitions/create` events. Occurs when a metafield definition is created. Requires the `read_content` scope.
[Anchor to METAFIELD_DEFINITIONS_DELETE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-METAFIELD_DEFINITIONS_DELETE)METAFIELD_DEFINITIONS_DELETE

    
The webhook topic for `metafield_definitions/delete` events. Occurs when a metafield definition is deleted. Requires the `read_content` scope.
[Anchor to METAFIELD_DEFINITIONS_UPDATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-METAFIELD_DEFINITIONS_UPDATE)METAFIELD_DEFINITIONS_UPDATE

    
The webhook topic for `metafield_definitions/update` events. Occurs when a metafield definition is updated. Requires the `read_content` scope.
[Anchor to METAOBJECTS_CREATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-METAOBJECTS_CREATE)METAOBJECTS_CREATE

    
The webhook topic for `metaobjects/create` events. Occurs when a metaobject is created. Requires the `read_metaobjects` scope.
[Anchor to METAOBJECTS_DELETE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-METAOBJECTS_DELETE)METAOBJECTS_DELETE

    
The webhook topic for `metaobjects/delete` events. Occurs when a metaobject is deleted. Requires the `read_metaobjects` scope.
[Anchor to METAOBJECTS_UPDATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-METAOBJECTS_UPDATE)METAOBJECTS_UPDATE

    
The webhook topic for `metaobjects/update` events. Occurs when a metaobject is updated. Requires the `read_metaobjects` scope.
[Anchor to ORDER_TRANSACTIONS_CREATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-ORDER_TRANSACTIONS_CREATE)ORDER_TRANSACTIONS_CREATE

    
The webhook topic for `order_transactions/create` events. Occurs when a order transaction is created or when it's status is updated. Only occurs for transactions with a status of success, failure or error. Requires at least one of the following scopes: read_orders, read_marketplace_orders, read_buyer_membership_orders.
[Anchor to ORDERS_CANCELLED](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-ORDERS_CANCELLED)ORDERS_CANCELLED

    
The webhook topic for `orders/cancelled` events. Occurs whenever an order is cancelled. Requires at least one of the following scopes: read_orders, read_marketplace_orders, read_buyer_membership_orders.
[Anchor to ORDERS_CREATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-ORDERS_CREATE)ORDERS_CREATE

    
The webhook topic for `orders/create` events. Occurs whenever an order is created. Requires at least one of the following scopes: read_orders, read_marketplace_orders.
[Anchor to ORDERS_DELETE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-ORDERS_DELETE)ORDERS_DELETE

    
The webhook topic for `orders/delete` events. Occurs whenever an order is deleted. Requires the `read_orders` scope.
[Anchor to ORDERS_EDITED](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-ORDERS_EDITED)ORDERS_EDITED

    
The webhook topic for `orders/edited` events. Occurs whenever an order is edited. Requires at least one of the following scopes: read_orders, read_marketplace_orders, read_buyer_membership_orders.
[Anchor to ORDERS_FULFILLED](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-ORDERS_FULFILLED)ORDERS_FULFILLED

    
The webhook topic for `orders/fulfilled` events. Occurs whenever an order is fulfilled. Requires at least one of the following scopes: read_orders, read_marketplace_orders.
[Anchor to ORDERS_LINK_REQUESTED](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-ORDERS_LINK_REQUESTED)ORDERS_LINK_REQUESTED

    
The webhook topic for `orders/link_requested` events. Occurs whenever a customer requests a new order link from the expired order status page. Requires at least one of the following scopes: read_orders, read_marketplace_orders, read_buyer_membership_orders.
[Anchor to ORDERS_PAID](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-ORDERS_PAID)ORDERS_PAID

    
The webhook topic for `orders/paid` events. Occurs whenever an order is paid. Requires at least one of the following scopes: read_orders, read_marketplace_orders.
[Anchor to ORDERS_PARTIALLY_FULFILLED](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-ORDERS_PARTIALLY_FULFILLED)ORDERS_PARTIALLY_FULFILLED

    
The webhook topic for `orders/partially_fulfilled` events. Occurs whenever an order is partially fulfilled. Requires at least one of the following scopes: read_orders, read_marketplace_orders.
[Anchor to ORDERS_RISK_ASSESSMENT_CHANGED](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-ORDERS_RISK_ASSESSMENT_CHANGED)ORDERS_RISK_ASSESSMENT_CHANGED

    
The webhook topic for `orders/risk_assessment_changed` events. Triggers when a new risk assessment is available on the order. This can be the first or a subsequent risk assessment. New risk assessments can be provided until the order is marked as fulfilled. Includes the risk level, risk facts, the provider and the order ID. When the provider is Shopify, that field is null. Does not include the risk recommendation for the order. The Shop ID is available in the headers. Requires the `read_orders` scope.
[Anchor to ORDERS_SHOPIFY_PROTECT_ELIGIBILITY_CHANGED](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-ORDERS_SHOPIFY_PROTECT_ELIGIBILITY_CHANGED)ORDERS_SHOPIFY_PROTECT_ELIGIBILITY_CHANGED

    
The webhook topic for `orders/shopify_protect_eligibility_changed` events. Occurs whenever Shopify Protect's eligibility for an order is changed. Requires the `read_orders` scope.
[Anchor to ORDERS_UPDATED](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-ORDERS_UPDATED)ORDERS_UPDATED

    
The webhook topic for `orders/updated` events. Occurs whenever an order is updated. Requires at least one of the following scopes: read_orders, read_marketplace_orders, read_buyer_membership_orders.
[Anchor to PAYMENT_SCHEDULES_DUE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-PAYMENT_SCHEDULES_DUE)PAYMENT_SCHEDULES_DUE

    
The webhook topic for `payment_schedules/due` events. Occurs whenever payment schedules are due. Requires the `read_payment_terms` scope.
[Anchor to PAYMENT_TERMS_CREATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-PAYMENT_TERMS_CREATE)PAYMENT_TERMS_CREATE

    
The webhook topic for `payment_terms/create` events. Occurs whenever payment terms are created. Requires the `read_payment_terms` scope.
[Anchor to PAYMENT_TERMS_DELETE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-PAYMENT_TERMS_DELETE)PAYMENT_TERMS_DELETE

    
The webhook topic for `payment_terms/delete` events. Occurs whenever payment terms are deleted. Requires the `read_payment_terms` scope.
[Anchor to PAYMENT_TERMS_UPDATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-PAYMENT_TERMS_UPDATE)PAYMENT_TERMS_UPDATE

    
The webhook topic for `payment_terms/update` events. Occurs whenever payment terms are updated. Requires the `read_payment_terms` scope.
[Anchor to PRODUCT_FEEDS_CREATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-PRODUCT_FEEDS_CREATE)PRODUCT_FEEDS_CREATE

    
The webhook topic for `product_feeds/create` events. Triggers when product feed is created Requires the `read_product_listings` scope.
[Anchor to PRODUCT_FEEDS_FULL_SYNC](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-PRODUCT_FEEDS_FULL_SYNC)PRODUCT_FEEDS_FULL_SYNC

    
The webhook topic for `product_feeds/full_sync` events. Triggers when a full sync for a product feed is performed Requires the `read_product_listings` scope.
[Anchor to PRODUCT_FEEDS_FULL_SYNC_FINISH](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-PRODUCT_FEEDS_FULL_SYNC_FINISH)PRODUCT_FEEDS_FULL_SYNC_FINISH

    
The webhook topic for `product_feeds/full_sync_finish` events. Triggers when a full sync finishes Requires the `read_product_listings` scope.
[Anchor to PRODUCT_FEEDS_INCREMENTAL_SYNC](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-PRODUCT_FEEDS_INCREMENTAL_SYNC)PRODUCT_FEEDS_INCREMENTAL_SYNC

    
The webhook topic for `product_feeds/incremental_sync` events. Occurs whenever a product publication is created, updated or removed for a product feed Requires the `read_product_listings` scope.
[Anchor to PRODUCT_FEEDS_UPDATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-PRODUCT_FEEDS_UPDATE)PRODUCT_FEEDS_UPDATE

    
The webhook topic for `product_feeds/update` events. Triggers when product feed is updated Requires the `read_product_listings` scope.
[Anchor to PRODUCT_LISTINGS_ADD](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-PRODUCT_LISTINGS_ADD)PRODUCT_LISTINGS_ADD

    
The webhook topic for `product_listings/add` events. Occurs whenever an active product is listed on a channel. Requires the `read_product_listings` scope.
[Anchor to PRODUCT_LISTINGS_REMOVE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-PRODUCT_LISTINGS_REMOVE)PRODUCT_LISTINGS_REMOVE

    
The webhook topic for `product_listings/remove` events. Occurs whenever a product listing is removed from the channel. Requires the `read_product_listings` scope.
[Anchor to PRODUCT_LISTINGS_UPDATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-PRODUCT_LISTINGS_UPDATE)PRODUCT_LISTINGS_UPDATE

    
The webhook topic for `product_listings/update` events. Occurs whenever a product publication is updated. Requires the `read_product_listings` scope.
[Anchor to PRODUCT_PUBLICATIONS_CREATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-PRODUCT_PUBLICATIONS_CREATE)PRODUCT_PUBLICATIONS_CREATE

    
The webhook topic for `product_publications/create` events. Occurs whenever a product publication for an active product is created, or whenever an existing product publication is published on the app that is subscribed to this webhook topic. Note that a webhook is only emitted when there are publishing changes to the app that is subscribed to the topic (ie. no webhook will be emitted if there is a publishing change to the online store and the webhook subscriber of the topic is a third-party app). Requires the `read_publications` scope.
[Anchor to PRODUCT_PUBLICATIONS_DELETE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-PRODUCT_PUBLICATIONS_DELETE)PRODUCT_PUBLICATIONS_DELETE

    
The webhook topic for `product_publications/delete` events. Occurs whenever a product publication for an active product is removed, or whenever an existing product publication is unpublished from the app that is subscribed to this webhook topic. Note that a webhook is only emitted when there are publishing changes to the app that is subscribed to the topic (ie. no webhook will be emitted if there is a publishing change to the online store and the webhook subscriber of the topic is a third-party app). Requires the `read_publications` scope.
[Anchor to PRODUCT_PUBLICATIONS_UPDATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-PRODUCT_PUBLICATIONS_UPDATE)PRODUCT_PUBLICATIONS_UPDATE

    
The webhook topic for `product_publications/update` events. Occurs whenever a product publication is updated from the app that is subscribed to this webhook topic. Note that a webhook is only emitted when there are publishing changes to the app that is subscribed to the topic (ie. no webhook will be emitted if there is a publishing change to the online store and the webhook subscriber of the topic is a third-party app). Requires the `read_publications` scope.
[Anchor to PRODUCTS_CREATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-PRODUCTS_CREATE)PRODUCTS_CREATE

    
The webhook topic for `products/create` events. Occurs whenever a product is created. Requires the `read_products` scope.
[Anchor to PRODUCTS_DELETE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-PRODUCTS_DELETE)PRODUCTS_DELETE

    
The webhook topic for `products/delete` events. Occurs whenever a product is deleted. Requires the `read_products` scope.
[Anchor to PRODUCTS_UPDATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-PRODUCTS_UPDATE)PRODUCTS_UPDATE

    
The webhook topic for `products/update` events. Occurs whenever a product is updated, ordered, or variants are added, removed or updated. Requires the `read_products` scope.
[Anchor to PROFILES_CREATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-PROFILES_CREATE)PROFILES_CREATE

    
The webhook topic for `profiles/create` events. Occurs whenever a delivery profile is created Requires at least one of the following scopes: read_shipping, read_assigned_shipping.
[Anchor to PROFILES_DELETE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-PROFILES_DELETE)PROFILES_DELETE

    
The webhook topic for `profiles/delete` events. Occurs whenever a delivery profile is deleted Requires at least one of the following scopes: read_shipping, read_assigned_shipping.
[Anchor to PROFILES_UPDATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-PROFILES_UPDATE)PROFILES_UPDATE

    
The webhook topic for `profiles/update` events. Occurs whenever a delivery profile is updated Requires at least one of the following scopes: read_shipping, read_assigned_shipping.
[Anchor to REFUNDS_CREATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-REFUNDS_CREATE)REFUNDS_CREATE

    
The webhook topic for `refunds/create` events. Occurs whenever a new refund is created without errors on an order, independent from the movement of money. Requires at least one of the following scopes: read_orders, read_marketplace_orders, read_buyer_membership_orders.
[Anchor to REQUESTED_ORDER_EDIT_CREATED](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-REQUESTED_ORDER_EDIT_CREATED)REQUESTED_ORDER_EDIT_CREATED

    
The webhook topic for `requested_order_edit/created` events. Occurs when a customer requests an edit on an order. Requires at least one of the following scopes: read_orders, read_marketplace_orders, read_buyer_membership_orders.
[Anchor to REQUESTED_ORDER_EDIT_DECLINED](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-REQUESTED_ORDER_EDIT_DECLINED)REQUESTED_ORDER_EDIT_DECLINED

    
The webhook topic for `requested_order_edit/declined` events. Occurs when a requested order edit on an order is declined. Requires at least one of the following scopes: read_orders, read_marketplace_orders, read_buyer_membership_orders.
[Anchor to REQUESTED_ORDER_EDIT_RESOLVED](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-REQUESTED_ORDER_EDIT_RESOLVED)REQUESTED_ORDER_EDIT_RESOLVED

    
The webhook topic for `requested_order_edit/resolved` events. Occurs when a requested order edit on an order is resolved. Requires at least one of the following scopes: read_orders, read_marketplace_orders, read_buyer_membership_orders.
[Anchor to RETURNS_APPROVE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-RETURNS_APPROVE)RETURNS_APPROVE

    
The webhook topic for `returns/approve` events. Occurs whenever a return is approved. This means `Return.status` is `OPEN`. Requires at least one of the following scopes: read_returns, read_marketplace_returns, read_buyer_membership_orders.
[Anchor to RETURNS_CANCEL](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-RETURNS_CANCEL)RETURNS_CANCEL

    
The webhook topic for `returns/cancel` events. Occurs whenever a return is canceled. Requires at least one of the following scopes: read_orders, read_marketplace_orders, read_returns, read_marketplace_returns, read_buyer_membership_orders.
[Anchor to RETURNS_CLOSE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-RETURNS_CLOSE)RETURNS_CLOSE

    
The webhook topic for `returns/close` events. Occurs whenever a return is closed. Requires at least one of the following scopes: read_orders, read_marketplace_orders, read_returns, read_marketplace_returns, read_buyer_membership_orders.
[Anchor to RETURNS_DECLINE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-RETURNS_DECLINE)RETURNS_DECLINE

    
The webhook topic for `returns/decline` events. Occurs whenever a return is declined. This means `Return.status` is `DECLINED`. Requires at least one of the following scopes: read_returns, read_marketplace_returns, read_buyer_membership_orders.
[Anchor to RETURNS_PROCESS](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-RETURNS_PROCESS)RETURNS_PROCESS

    
The webhook topic for `returns/process` events. Occurs whenever a return is processed. Requires at least one of the following scopes: read_returns, read_marketplace_returns, read_buyer_membership_orders.
[Anchor to RETURNS_REOPEN](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-RETURNS_REOPEN)RETURNS_REOPEN

    
The webhook topic for `returns/reopen` events. Occurs whenever a closed return is reopened. Requires at least one of the following scopes: read_orders, read_marketplace_orders, read_returns, read_marketplace_returns, read_buyer_membership_orders.
[Anchor to RETURNS_REQUEST](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-RETURNS_REQUEST)RETURNS_REQUEST

    
The webhook topic for `returns/request` events. Occurs whenever a return is requested. This means `Return.status` is `REQUESTED`. Requires at least one of the following scopes: read_returns, read_marketplace_returns, read_buyer_membership_orders.
[Anchor to RETURNS_UPDATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-RETURNS_UPDATE)RETURNS_UPDATE

    
The webhook topic for `returns/update` events. Occurs whenever a return is updated. Requires at least one of the following scopes: read_returns, read_marketplace_returns, read_buyer_membership_orders.
[Anchor to REVERSE_DELIVERIES_ATTACH_DELIVERABLE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-REVERSE_DELIVERIES_ATTACH_DELIVERABLE)REVERSE_DELIVERIES_ATTACH_DELIVERABLE

    
The webhook topic for `reverse_deliveries/attach_deliverable` events. Occurs whenever a deliverable is attached to a reverse delivery. This occurs when a reverse delivery is created or updated with delivery metadata. Metadata includes the delivery method, label, and tracking information associated with a reverse delivery. Requires at least one of the following scopes: read_returns, read_marketplace_returns.
[Anchor to REVERSE_FULFILLMENT_ORDERS_DISPOSE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-REVERSE_FULFILLMENT_ORDERS_DISPOSE)REVERSE_FULFILLMENT_ORDERS_DISPOSE

    
The webhook topic for `reverse_fulfillment_orders/dispose` events. Occurs whenever a disposition is made on a reverse fulfillment order. This includes dispositions made on reverse deliveries that are associated with the reverse fulfillment order. Requires at least one of the following scopes: read_returns, read_marketplace_returns.
[Anchor to ROLLOUTS_CREATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-ROLLOUTS_CREATE)ROLLOUTS_CREATE

    
The webhook topic for `rollouts/create` events. Occurs when a rollout is created, including its initial treatments and attached changes. Requires the `read_rollouts` scope.
[Anchor to ROLLOUTS_DELETE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-ROLLOUTS_DELETE)ROLLOUTS_DELETE

    
The webhook topic for `rollouts/delete` events. Occurs when a rollout is deleted. Archiving a rollout instead produces a rollouts/update notification. Requires the `read_rollouts` scope.
[Anchor to ROLLOUTS_RESOURCE_CHANGE_ADDED](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-ROLLOUTS_RESOURCE_CHANGE_ADDED)ROLLOUTS_RESOURCE_CHANGE_ADDED

    
The webhook topic for `rollouts/resource_change_added` events. Occurs when a change is added to a rollout treatment. This does not indicate resource creation or activation. Requires the `read_rollouts` scope.
[Anchor to ROLLOUTS_RESOURCE_CHANGE_REMOVED](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-ROLLOUTS_RESOURCE_CHANGE_REMOVED)ROLLOUTS_RESOURCE_CHANGE_REMOVED

    
The webhook topic for `rollouts/resource_change_removed` events. Occurs when a change is removed from a rollout treatment. Other changes can still reference the same resource. Requires the `read_rollouts` scope.
[Anchor to ROLLOUTS_RESOURCE_CHANGE_UPDATED](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-ROLLOUTS_RESOURCE_CHANGE_UPDATED)ROLLOUTS_RESOURCE_CHANGE_UPDATED

    
The webhook topic for `rollouts/resource_change_updated` events. Occurs when a change in a rollout treatment targets a different resource. The change ID stays the same. Requires the `read_rollouts` scope.
[Anchor to ROLLOUTS_UPDATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-ROLLOUTS_UPDATE)ROLLOUTS_UPDATE

    
The webhook topic for `rollouts/update` events. Occurs when a rollout changes lifecycle status or its configuration, treatments, or attached changes are updated. Also occurs when a change to another rollout alters this rollout's effective traffic allocation. That notification can arrive shortly after the other change, and this rollout's updated_at stays the same. Deliveries can be duplicated or arrive out of order, so query the rollout when you need its current state. Requires the `read_rollouts` scope.
[Anchor to SCHEDULED_PRODUCT_LISTINGS_ADD](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-SCHEDULED_PRODUCT_LISTINGS_ADD)SCHEDULED_PRODUCT_LISTINGS_ADD

    
The webhook topic for `scheduled_product_listings/add` events. Occurs whenever a product is scheduled to be published. Requires the `read_product_listings` scope.
[Anchor to SCHEDULED_PRODUCT_LISTINGS_REMOVE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-SCHEDULED_PRODUCT_LISTINGS_REMOVE)SCHEDULED_PRODUCT_LISTINGS_REMOVE

    
The webhook topic for `scheduled_product_listings/remove` events. Occurs whenever a product is no longer scheduled to be published. Requires the `read_product_listings` scope.
[Anchor to SCHEDULED_PRODUCT_LISTINGS_UPDATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-SCHEDULED_PRODUCT_LISTINGS_UPDATE)SCHEDULED_PRODUCT_LISTINGS_UPDATE

    
The webhook topic for `scheduled_product_listings/update` events. Occurs whenever a product's scheduled availability date changes. Requires the `read_product_listings` scope.
[Anchor to SEGMENTS_CREATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-SEGMENTS_CREATE)SEGMENTS_CREATE

    
The webhook topic for `segments/create` events. Occurs whenever a segment is created. Requires the `read_customers` scope.
[Anchor to SEGMENTS_DELETE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-SEGMENTS_DELETE)SEGMENTS_DELETE

    
The webhook topic for `segments/delete` events. Occurs whenever a segment is deleted. Requires the `read_customers` scope.
[Anchor to SEGMENTS_UPDATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-SEGMENTS_UPDATE)SEGMENTS_UPDATE

    
The webhook topic for `segments/update` events. Occurs whenever a segment is updated. Requires the `read_customers` scope.
[Anchor to SELLING_PLAN_GROUPS_CREATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-SELLING_PLAN_GROUPS_CREATE)SELLING_PLAN_GROUPS_CREATE

    
The webhook topic for `selling_plan_groups/create` events. Notifies when a SellingPlanGroup is created. Requires the `read_products` scope.
[Anchor to SELLING_PLAN_GROUPS_DELETE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-SELLING_PLAN_GROUPS_DELETE)SELLING_PLAN_GROUPS_DELETE

    
The webhook topic for `selling_plan_groups/delete` events. Notifies when a SellingPlanGroup is deleted. Requires the `read_products` scope.
[Anchor to SELLING_PLAN_GROUPS_UPDATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-SELLING_PLAN_GROUPS_UPDATE)SELLING_PLAN_GROUPS_UPDATE

    
The webhook topic for `selling_plan_groups/update` events. Notifies when a SellingPlanGroup is updated. Requires the `read_products` scope.
[Anchor to SHIPPING_ADDRESSES_CREATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-SHIPPING_ADDRESSES_CREATE)SHIPPING_ADDRESSES_CREATE

    
The webhook topic for `shipping_addresses/create` events. Occurs whenever a shipping address is created. Requires the `read_shipping` scope.
[Anchor to SHIPPING_ADDRESSES_UPDATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-SHIPPING_ADDRESSES_UPDATE)SHIPPING_ADDRESSES_UPDATE

    
The webhook topic for `shipping_addresses/update` events. Occurs whenever a shipping address is updated. Requires the `read_shipping` scope.
[Anchor to SHOP_UPDATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-SHOP_UPDATE)SHOP_UPDATE

    
The webhook topic for `shop/update` events. Occurs whenever a shop is updated.
[Anchor to SUBSCRIPTION_BILLING_ATTEMPTS_CHALLENGED](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-SUBSCRIPTION_BILLING_ATTEMPTS_CHALLENGED)SUBSCRIPTION_BILLING_ATTEMPTS_CHALLENGED

    
The webhook topic for `subscription_billing_attempts/challenged` events. Occurs when the financial instutition challenges the subscripttion billing attempt charge as per 3D Secure. Requires the `read_own_subscription_contracts` scope.
[Anchor to SUBSCRIPTION_BILLING_ATTEMPTS_FAILURE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-SUBSCRIPTION_BILLING_ATTEMPTS_FAILURE)SUBSCRIPTION_BILLING_ATTEMPTS_FAILURE

    
The webhook topic for `subscription_billing_attempts/failure` events. Occurs whenever a subscription billing attempt fails. Requires the `read_own_subscription_contracts` scope.
[Anchor to SUBSCRIPTION_BILLING_ATTEMPTS_SUCCESS](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-SUBSCRIPTION_BILLING_ATTEMPTS_SUCCESS)SUBSCRIPTION_BILLING_ATTEMPTS_SUCCESS

    
The webhook topic for `subscription_billing_attempts/success` events. Occurs whenever a subscription billing attempt succeeds. Requires the `read_own_subscription_contracts` scope.
[Anchor to SUBSCRIPTION_BILLING_CYCLE_EDITS_CREATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-SUBSCRIPTION_BILLING_CYCLE_EDITS_CREATE)SUBSCRIPTION_BILLING_CYCLE_EDITS_CREATE

    
The webhook topic for `subscription_billing_cycle_edits/create` events. Occurs whenever a subscription contract billing cycle is edited. Requires the `read_own_subscription_contracts` scope.
[Anchor to SUBSCRIPTION_BILLING_CYCLE_EDITS_DELETE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-SUBSCRIPTION_BILLING_CYCLE_EDITS_DELETE)SUBSCRIPTION_BILLING_CYCLE_EDITS_DELETE

    
The webhook topic for `subscription_billing_cycle_edits/delete` events. Occurs whenever a subscription contract billing cycle edit is deleted. Requires the `read_own_subscription_contracts` scope.
[Anchor to SUBSCRIPTION_BILLING_CYCLE_EDITS_UPDATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-SUBSCRIPTION_BILLING_CYCLE_EDITS_UPDATE)SUBSCRIPTION_BILLING_CYCLE_EDITS_UPDATE

    
The webhook topic for `subscription_billing_cycle_edits/update` events. Occurs whenever a subscription contract billing cycle edit is updated. Requires the `read_own_subscription_contracts` scope.
[Anchor to SUBSCRIPTION_BILLING_CYCLES_SKIP](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-SUBSCRIPTION_BILLING_CYCLES_SKIP)SUBSCRIPTION_BILLING_CYCLES_SKIP

    
The webhook topic for `subscription_billing_cycles/skip` events. Occurs whenever a subscription contract billing cycle is skipped. Requires the `read_own_subscription_contracts` scope.
[Anchor to SUBSCRIPTION_BILLING_CYCLES_UNSKIP](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-SUBSCRIPTION_BILLING_CYCLES_UNSKIP)SUBSCRIPTION_BILLING_CYCLES_UNSKIP

    
The webhook topic for `subscription_billing_cycles/unskip` events. Occurs whenever a subscription contract billing cycle is unskipped. Requires the `read_own_subscription_contracts` scope.
[Anchor to SUBSCRIPTION_CONTRACTS_ACTIVATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-SUBSCRIPTION_CONTRACTS_ACTIVATE)SUBSCRIPTION_CONTRACTS_ACTIVATE

    
The webhook topic for `subscription_contracts/activate` events. Occurs when a subscription contract is activated. Requires the `read_own_subscription_contracts` scope.
[Anchor to SUBSCRIPTION_CONTRACTS_CANCEL](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-SUBSCRIPTION_CONTRACTS_CANCEL)SUBSCRIPTION_CONTRACTS_CANCEL

    
The webhook topic for `subscription_contracts/cancel` events. Occurs when a subscription contract is canceled. Requires the `read_own_subscription_contracts` scope.
[Anchor to SUBSCRIPTION_CONTRACTS_CREATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-SUBSCRIPTION_CONTRACTS_CREATE)SUBSCRIPTION_CONTRACTS_CREATE

    
The webhook topic for `subscription_contracts/create` events. Occurs whenever a subscription contract is created. Requires the `read_own_subscription_contracts` scope.
[Anchor to SUBSCRIPTION_CONTRACTS_EXPIRE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-SUBSCRIPTION_CONTRACTS_EXPIRE)SUBSCRIPTION_CONTRACTS_EXPIRE

    
The webhook topic for `subscription_contracts/expire` events. Occurs when a subscription contract expires. Requires the `read_own_subscription_contracts` scope.
[Anchor to SUBSCRIPTION_CONTRACTS_FAIL](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-SUBSCRIPTION_CONTRACTS_FAIL)SUBSCRIPTION_CONTRACTS_FAIL

    
The webhook topic for `subscription_contracts/fail` events. Occurs when a subscription contract is failed. Requires the `read_own_subscription_contracts` scope.
[Anchor to SUBSCRIPTION_CONTRACTS_PAUSE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-SUBSCRIPTION_CONTRACTS_PAUSE)SUBSCRIPTION_CONTRACTS_PAUSE

    
The webhook topic for `subscription_contracts/pause` events. Occurs when a subscription contract is paused. Requires the `read_own_subscription_contracts` scope.
[Anchor to SUBSCRIPTION_CONTRACTS_UPDATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-SUBSCRIPTION_CONTRACTS_UPDATE)SUBSCRIPTION_CONTRACTS_UPDATE

    
The webhook topic for `subscription_contracts/update` events. Occurs whenever a subscription contract is updated. Requires the `read_own_subscription_contracts` scope.
[Anchor to TAX_SERVICES_CREATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-TAX_SERVICES_CREATE)TAX_SERVICES_CREATE

    
The webhook topic for `tax_services/create` events. Occurs whenever a tax service is created. Requires the `read_taxes` scope.
[Anchor to TAX_SERVICES_UPDATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-TAX_SERVICES_UPDATE)TAX_SERVICES_UPDATE

    
The webhook topic for `tax_services/update` events. Occurs whenver a tax service is updated. Requires the `read_taxes` scope.
[Anchor to TENDER_TRANSACTIONS_CREATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-TENDER_TRANSACTIONS_CREATE)TENDER_TRANSACTIONS_CREATE

    
The webhook topic for `tender_transactions/create` events. Occurs when a tender transaction is created. Requires the `read_orders` scope.
[Anchor to THEMES_CREATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-THEMES_CREATE)THEMES_CREATE

    
The webhook topic for `themes/create` events. Occurs whenever a theme is created. Does not occur when theme files are created. Requires the `read_themes` scope.
[Anchor to THEMES_DELETE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-THEMES_DELETE)THEMES_DELETE

    
The webhook topic for `themes/delete` events. Occurs whenever a theme is deleted. Does not occur when theme files are deleted. Requires the `read_themes` scope.
[Anchor to THEMES_PUBLISH](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-THEMES_PUBLISH)THEMES_PUBLISH

    
The webhook topic for `themes/publish` events. Occurs whenever a theme with the main or mobile (deprecated) role is published. Requires the `read_themes` scope.
[Anchor to THEMES_UPDATE](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-THEMES_UPDATE)THEMES_UPDATE

    
The webhook topic for `themes/update` events. Occurs whenever a theme is updated. Does not occur when theme files are updated. Requires the `read_themes` scope.
[Anchor to VARIANTS_IN_STOCK](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-VARIANTS_IN_STOCK)VARIANTS_IN_STOCK

    
The webhook topic for `variants/in_stock` events. Occurs whenever a variant becomes in stock. Online channels receive this webhook only when the variant becomes in stock online. Requires the `read_products` scope.
[Anchor to VARIANTS_OUT_OF_STOCK](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#enums-VARIANTS_OUT_OF_STOCK)VARIANTS_OUT_OF_STOCK

    
The webhook topic for `variants/out_of_stock` events. Occurs whenever a variant becomes out of stock. Online channels receive this webhook only when the variant becomes out of stock online. Requires the `read_products` scope.
* * *
Was this section helpful?
YesNo
## 
[Anchor to Fields](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#fields)Fields
[Anchor to WebhookSubscription.topic](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#reference-WebhookSubscription.topic)[WebhookSubscription.topic](https://shopify.dev/docs/api/admin-graphql/latest/objects/WebhookSubscription#field-WebhookSubscription.fields.topic)
•OBJECT 
    
A webhook subscription is a persisted data object created by an app using the REST Admin API or GraphQL Admin API. It describes the topic that the app wants to receive, and a destination where Shopify should send webhooks of the specified topic. When an event for a given topic occurs, the webhook subscription sends a relevant payload to the destination. Learn more about the [webhooks system](https://shopify.dev/apps/webhooks).
[Anchor to QueryRoot.webhookSubscriptions(topics)](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#reference-QueryRoot.webhookSubscriptions\(topics\))[QueryRoot.webhookSubscriptions(topics)](https://shopify.dev/docs/api/admin-graphql/latest/objects/QueryRoot#field-QueryRoot.fields.webhookSubscriptions.arguments.topics)
•ARGUMENT 
    
The schema's entry-point for queries. This acts as the public, top-level API from which all queries must start.
[Anchor to eventBridgeWebhookSubscriptionCreate.topic](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#reference-eventBridgeWebhookSubscriptionCreate.topic)[eventBridgeWebhookSubscriptionCreate.topic](https://shopify.dev/docs/api/admin-graphql/latest/mutations/eventBridgeWebhookSubscriptionCreate#arguments-topic)
•ARGUMENT 

[Anchor to pubSubWebhookSubscriptionCreate.topic](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#reference-pubSubWebhookSubscriptionCreate.topic)[pubSubWebhookSubscriptionCreate.topic](https://shopify.dev/docs/api/admin-graphql/latest/mutations/pubSubWebhookSubscriptionCreate#arguments-topic)
•ARGUMENT 

[Anchor to webhookSubscriptionCreate.topic](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#reference-webhookSubscriptionCreate.topic)[webhookSubscriptionCreate.topic](https://shopify.dev/docs/api/admin-graphql/latest/mutations/webhookSubscriptionCreate#arguments-topic)
•ARGUMENT 

[Anchor to webhookSubscriptions.topics](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#reference-webhookSubscriptions.topics)[webhookSubscriptions.topics](https://shopify.dev/docs/api/admin-graphql/latest/queries/webhookSubscriptions#arguments-topics)
•ARGUMENT 

* * *
Was this section helpful?
YesNo
## Map
### Fields with this enum
  * <-|[WebhookSubscription.topic](https://shopify.dev/docs/api/admin-graphql/latest/objects/WebhookSubscription#field-WebhookSubscription.fields.topic)


### Arguments with this enum
  * <-|[QueryRoot.webhookSubscriptions(topics)](https://shopify.dev/docs/api/admin-graphql/latest/objects/QueryRoot#field-QueryRoot.fields.webhookSubscriptions.arguments.topics)
  * <-|[eventBridgeWebhookSubscriptionCreate.topic](https://shopify.dev/docs/api/admin-graphql/latest/mutations/eventBridgeWebhookSubscriptionCreate#arguments-topic)
  * <-|[pubSubWebhookSubscriptionCreate.topic](https://shopify.dev/docs/api/admin-graphql/latest/mutations/pubSubWebhookSubscriptionCreate#arguments-topic)
  * <-|[webhookSubscriptionCreate.topic](https://shopify.dev/docs/api/admin-graphql/latest/mutations/webhookSubscriptionCreate#arguments-topic)
  * <-|[webhookSubscriptions.topics](https://shopify.dev/docs/api/admin-graphql/latest/queries/webhookSubscriptions#arguments-topics)


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



