[Developers Program](https://developer.ebay.com/)
  * Join
    * [Overview](https://developer.ebay.com/join)
    * [About the Program](https://developer.ebay.com/join/about-the-developers-program)
    * [Benefits](https://developer.ebay.com/join/benefits)
    * [Policies](https://developer.ebay.com/join/policies)
    * [API License Agreement](https://developer.ebay.com/join/api-license-agreement)
  * Develop
    * [Overview](https://developer.ebay.com/develop)
    * [Get Started with APIs](https://developer.ebay.com/develop/get-started)
      * [Overview](https://developer.ebay.com/develop/get-started)
      * [Authorization](https://developer.ebay.com/develop/guides/sell/authorization)
      * [Using eBay RESTful APIs](https://developer.ebay.com/develop/guides/sell/using-ebay-restful-apis)
      * [API Call Limits](https://developer.ebay.com/develop/api/sell/api_call_limits)
      * [API Deprecations](https://developer.ebay.com/develop/get-started/api-deprecation-status)
      * [API Status](https://developer.ebay.com/develop/get-started/api-status)
    * [Selling Applications](https://developer.ebay.com/develop/api/sell)
      * [Listing Management](https://developer.ebay.com/develop/api/sell/inventory_mapping#sell-inventory_mapping-query-listingpreviewscreationtaskbyid)
      * [Listing Metadata](https://developer.ebay.com/develop/api/sell/metadata_api#sell-metadata_api-marketplace-getautomotivepartscompatibilitypolicies)
      * [Account Management](https://developer.ebay.com/develop/api/sell/finances_api#sell-finances_api-order_earnings-getorderearnings)
      * [Order Management](https://developer.ebay.com/develop/api/sell/fulfillment_api#sell-fulfillment_api-order-getorder)
      * [Offers and Leads](https://developer.ebay.com/develop/api/sell/leads_api#sell-leads_api-classified_lead-getallclassifiedleads)
      * [Communication](https://developer.ebay.com/develop/api/sell/message_api#sell-message_api-conversation-bulkupdateconversation)
      * [Marketing and Promotions](https://developer.ebay.com/develop/api/sell/marketing_api#sell-marketing_api-ad-bulkcreateadsbyinventoryreference)
      * [Analytics and Reporting](https://developer.ebay.com/develop/api/sell/analytics_api#sell-analytics_api-customer_service_metric-getcustomerservicemetric)
      * [Other APIs](https://developer.ebay.com/develop/api/sell/identity_api#sell-identity_api-user-getuser)
      * [App Settings & Insight](https://developer.ebay.com/develop/api/sell/developer_analytics_api#sell-developer_analytics_api-rate_limit-getratelimits)
    * [Buying Applications](https://developer.ebay.com/develop/api/buy)
      * [Inventory Discovery & Refresh](https://developer.ebay.com/develop/api/buy/browse_api#buy-browse_api-item_summary-search)
      * [Marketing and Discounts](https://developer.ebay.com/develop/api/buy/deal_api#buy-deal_api-deal_item-getdealitems)
      * [Marketplace Metadata](https://developer.ebay.com/develop/api/buy/taxonomy_api#buy-taxonomy_api-category_tree-fetchitemaspects)
      * [Checkout/Bid](https://developer.ebay.com/develop/api/buy/offer_api#buy-offer_api-bidding-getbidding)
      * [Communication](https://developer.ebay.com/develop/api/buy/message_api#buy-message_api-conversation-bulkupdateconversation)
      * [Other APIs](https://developer.ebay.com/develop/api/buy/identity_api#buy-identity_api-user-getuser)
      * [App Settings & Insight](https://developer.ebay.com/develop/api/buy/developer_analytics_api#buy-developer_analytics_api-rate_limit-getratelimits)
    * [All guides](https://developer.ebay.com/develop/guides)
    * [SDKs & Widgets](https://developer.ebay.com/develop/sdks-and-widgets)
    * [Tools](https://developer.ebay.com/develop/tools)
      * [Overview](https://developer.ebay.com/develop/tools)
      * [eBay Sandbox](https://developer.ebay.com/develop/tools/sandbox)
        * [Overview](https://developer.ebay.com/develop/tools/sandbox)
        * [Create Test Users](https://developer.ebay.com/sandbox/register)
        * [Reset Password](https://developer.ebay.com/sandbox/reset-password)
        * [Sandbox Status](https://developer.ebay.com/support/api-status/sandbox)
        * [Sandbox Site](http://sandbox.ebay.com/)
      * [API Explorer](https://developer.ebay.com/my/api_test_tool)
      * [GraphQL Explorer](https://developer.ebay.com/my/graphql_explorer)
      * [WSDL Pruner](https://developer.ebay.com/develop/tools/wsdl-pruner)
  * Grow
    * [Overview](https://developer.ebay.com/grow)
    * [Application Growth Check](https://developer.ebay.com/grow/application-growth-check)
    * [Affiliate Program](https://developer.ebay.com/grow/affiliate-program)
    * [eBay Partner Program](https://developer.ebay.com/grow/ebay-partner-program)
    * [Events](https://developer.ebay.com/grow/events)
    * [Awards](https://developer.ebay.com/grow/awards)
  * Updates
    * [Overview](https://developer.ebay.com/updates)
    * [API Updates](https://developer.ebay.com/updates/api-updates)
    * [Newsletter](https://developer.ebay.com/updates/newsletter)
    * [Blog](https://developer.ebay.com/updates/blog)
    * [Survey](https://developer.ebay.com/survey)
  * Support
    * [Overview](https://developer.ebay.com/support)
    * [API Status](https://developer.ebay.com/support/api-status)
    * [FAQs](https://developer.ebay.com/support/faq)
    * [Developer Community Forum](https://developer.ebay.com/support/developer-community-forum)
    * [Knowledge Base](https://developer.ebay.com/support/knowledge-base)
    * [Developer Account Support](https://developer.ebay.com/support/developer-account-support)
    * [Developer Technical Support](https://developer.ebay.com/my/support/tickets)


[](https://developer.ebay.com/signin)[](https://developer.ebay.com/search)
[Home](https://developer.ebay.com/)[Develop](https://developer.ebay.com/develop)[API Documentation](https://developer.ebay.com/api-docs)[Inventory API Overview](https://developer.ebay.com/api-docs/sell/inventory/overview.html)
# Inventory API Overview
The Inventory API is used to create and manage inventory item records, and then convert these inventory items into product offers on eBay marketplaces. The Inventory API has the following entities: 
  * **Location** : a seller must have at least one store or warehouse inventory location set up before that seller can start creating and publishing offers with the Inventory API. Every inventory location must also have a seller-defined merchant location key value. 
  * **Inventory Item** : before a product can be sold in an offer on an eBay marketplace, an inventory item record must exist for that product. An inventory item record contains such things as product details, item condition, quantity available. Every Inventory Item must also have a seller-defined SKU value, and this value must be unique across the seller's inventory.
  * **Offer** : an offer is what becomes a live eBay listing. An offer is first created, and then it is published with the Inventory API. Each offer must be associated with an eBay marketplace, an inventory item, an inventory location, and a category ID. The offer will contain quantity available for the offer, the listing description, and an offer price. Every offer must also reference a payment, a fulfillment, and a return business policy, so the seller must be opted in, and have business policies available to apply against the offers.
  * **Inventory Item Group** : an inventory item group is necessary if the seller would like to create and manage multiple-variation listings through the Inventory API. An inventory item group is a collection of similar inventory items that might vary on a couple of aspects like color and size. 
  * **Compatible Products** : the product compatibility calls allow the seller to create a compatible vehicle list, or vehicles that are compatible with a motor vehicle part or accessory. 


**Important!** Publish offer note: Fields may be optional or conditionally required when calling a method, but become required when publishing the offer to create an active listing. For details, see [Required fields for publishing an offer](https://developer.ebay.com/api-docs/sell/static/inventory/publishing-offers.html).
## Technical overview
The Inventory API is more-or-less a "standalone" REST-based API, but it does have the following relationships with other APIs: 
  * Trading API: sellers may use the Trading API to get some listing-related metadata, and may also want to use **GetItem** call to view the listing that they have created through the Offer calls
  * Account API: sellers can use the Account API to opt in to Business Policies, and to create and manage business policies (that are used/referenced with the **createOffer** call in the Inventory API). Inventory API users may also need to use the **getRateTables** call of the Account API to get the unique identifiers of shipping rate tables that they may want to apply to a fulfillment business policy
  * Fulfillment API: sellers can use the Fulfillment API to get order details and manage shipment tracking.


## Business use cases
Below are the high-level use cases addressed by the Inventory API.
  * Create and manage inventory locations
  * Create and manage inventory item records
  * Create offers
  * Publish and manage offers
  * Migrate existing eBay listings to the Inventory API data model using the **bulkMigrateListings** call


The following use cases are not necessarily required, but they are available to sellers:
  * Get expected listing fees for unpublished offers
  * Create and manage inventory item groups (necessary if creating and managing multiple-variation listings)
  * Create compatible vehicle lists for motor vehicle parts (helpful if creating and managing motor vehicle parts or accessory listings)
  * Disable or enable inventory locations
  * Set available quantity for a SKU at specific warehouse locations
  * Apply extended producer responsibility regulations and custom policies to listings. These features are supported by a limited number of sites and specific categories. Refer to the [Sell Metadata API](https://developer.ebay.com/api-docs/sell/metadata/overview.html) to return the enabled sites and categories.


## Real-time Inventory Check
Real-time Inventory Check is a feature for the Inventory API that allows for inventory availability and quantity information to be automatically updated at the time of checkout. Merchants can provide an API endpoint to eBay, and eBay will make a call to this endpoint at checkout to verify that enough quantity exists to fulfill the order for an inventory item. 
For more information, see the [Real-time inventory check](https://developer.ebay.com/api-docs/sell/static/inventory/realtime-inventory-check.html) section of the Selling Integration Guide.
## Inventory API requirements and restrictions
**Important!** Currently, listings created through the **Inventory API** cannot be edited through Seller Hub or any other listing platform. Any revisions must be done through the **Inventory API**.
To use the Inventory API (or any other eBay public API), the user must have an eBay Developers Program account, and the user's seller account must be opted in to [business policies](https://developer.ebay.com/api-docs/sell/account/resources/program/methods/optInToProgram). Once opted in, use the [Account API v1](https://developer.ebay.com/api-docs/sell/account/resources/methods) to create and update policies including fulfillment (previously known as shipping), returns, and payment. These policies are required to create listings (also referred to as published offers) through the **Inventory API**. 
It is also a very good idea that the 'Out-of-Stock' Control feature is turned on for seller. With the 'Out-of-Stock' Control feature, a listing showing '0' available quantity is kept alive/active for up to 90 days, giving the seller a chance to load more inventory for the active listing. While an active listing is 'out of stock', it will be hidden from search so interested buyers don't view a listing with no available quantity. Sellers can turn on the 'Out-of-Stock' Control option in My eBay Site Preferences, or they can use the **SetUserPreferences** call of the Trading API to turn on this feature. 
If using the **bulkMigrateListings** call, there are additional requirements than the active eBay listing must meet before that listing can be converted to the Inventory API data model. These requirements are covered in the Selling Integration Guide.
### Supported marketplaces and listing types
The Inventory API is supported on all eBay marketplaces that have API support. The Inventory API supports both fixed-price and auction items. 
## Related topics
  * API Documentation
[Account v1 API](https://developer.ebay.com/api-docs/sell/account/overview.html)[Account v2 API](https://developer.ebay.com/api-docs/sell/account/v2/overview.html)[Inventory API](https://developer.ebay.com/api-docs/sell/inventory/overview.html)[Fulfillment API](https://developer.ebay.com/api-docs/sell/fulfillment/overview.html)[Finances API](https://developer.ebay.com/api-docs/sell/finances/overview.html)[Marketing API](https://developer.ebay.com/api-docs/sell/marketing/overview.html)[Negotiation API](https://developer.ebay.com/api-docs/sell/negotiation/overview.html)[Recommendation API](https://developer.ebay.com/api-docs/sell/recommendation/overview.html)[Analytics API](https://developer.ebay.com/api-docs/sell/analytics/overview.html)[Metadata API](https://developer.ebay.com/api-docs/sell/metadata/overview.html)[Compliance API](https://developer.ebay.com/api-docs/sell/compliance/overview.html)[Logistics API](https://developer.ebay.com/api-docs/sell/logistics/overview.html)[Feed API](https://developer.ebay.com/api-docs/sell/feed/overview.html)[Stores API](https://developer.ebay.com/api-docs/sell/stores/overview.html)
  * [Guides](https://developer.ebay.com/develop/guides)
  * Related Docs
[Using eBay RESTful APIs](https://developer.ebay.com/api-docs/static/ebay-rest-landing.html)[Commerce APIs](https://developer.ebay.com/develop/apis/restful-apis/commerce-apis)[Developer APIs](https://developer.ebay.com/develop/apis/restful-apis/developer-apis)[Trading API](https://developer.ebay.com/devzone/xml/docs/reference/ebay/index.html)[Post-Order API](https://developer.ebay.com/Devzone/post-order/index.html)[Finding API](https://developer.ebay.com/devzone/finding/callref/index.html)[Platform Notifications](https://developer.ebay.com/api-docs/static/platform-notifications-landing.html)


On this page
[Technical overview](https://developer.ebay.com/api-docs/sell/inventory/overview.html#overview)
[Business use cases](https://developer.ebay.com/api-docs/sell/inventory/overview.html#useCases)
[Real-time Inventory Check](https://developer.ebay.com/api-docs/sell/inventory/overview.html#RTIC)
[Inventory API requirements and restrictions](https://developer.ebay.com/api-docs/sell/inventory/overview.html#requirements)
### eBay for Developers.
[Community Forum](https://community.ebay.com/t5/Developer-Groups/ct-p/developergroup)[Technical Support](https://developer.ebay.com/my/support/tickets)[APIs](https://developer.ebay.com/develop/api)[FAQs](https://developer.ebay.com/support/faq)
Copyright 1999—2026 eBay Inc. All rights reserved.
[API License Agreement](https://developer.ebay.com/join/api-license-agreement)[User agreement](http://pages.ebay.com/help/policies/user-agreement.html?rt=nc "opens in new window or tab")[Privacy policy](http://pages.ebay.com/help/policies/privacy-policy.html?rt=nc "opens in new window or tab")[Cookies](http://pages.ebay.com/help/account/cookies-web-beacons.html "opens in new window or tab")
#### Thank you for helping us to improve the eBay developer program.
While we are not able to respond directly to your comments, we will carefully review them to improve your experience with eBay developer program!
If you need help, contact [Developer Technical Support](https://developer.ebay.com/my/support/tickets) .

