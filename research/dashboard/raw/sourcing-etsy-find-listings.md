Skip to main content
Menu
[![Open API v3 Logo](https://developer.etsy.com/img/logo.svg)**Open API v3**](https://developer.etsy.com/documentation)[Guides](https://developer.etsy.com/documentation/)[API Reference](https://developer.etsy.com/documentation/reference)
[Send feedback](https://github.com/etsy/open-api/discussions)
[![Open API v3 Logo](https://developer.etsy.com/img/logo.svg)**Open API v3**](https://developer.etsy.com/documentation)
  * [Guides](https://developer.etsy.com/documentation/)
  * [API Reference](https://developer.etsy.com/documentation/reference)
  * [Send feedback](https://github.com/etsy/open-api/discussions)


  * Authentication
  * Listing Management
    * BuyerTaxonomy
      * getgetBuyerTaxonomyNodes
      * getgetPropertiesByBuyerTaxonomyId
    * SellerTaxonomy
      * getgetSellerTaxonomyNodes
      * getgetPropertiesByTaxonomyId
    * ShopListing
      * postcreateDraftListing
      * getgetListingsByShop
      * deldeleteListing
      * getgetListing
      * getfindAllListingsActive
      * getfindAllActiveListingsByShop
      * getgetListingsByListingIds
      * getgetFeaturedListingsByShop
      * deldeleteListingProperty
      * putupdateListingProperty
      * getgetListingProperty
      * getgetListingProperties
      * getgetListingsShippingByListingIds
      * patchupdateListing
      * getgetListingsByShopReceipt
      * getgetListingsByShopReturnPolicy
      * getgetListingsByShopSectionId
    * ShopListing File
      * deldeleteListingFile
      * getgetListingFile
      * getgetAllListingFiles
      * postuploadListingFile
    * ShopListing Image
      * deldeleteListingImage
      * getgetListingImage
      * getgetListingImages
      * postuploadListingImage
    * ShopListing Inventory
      * getgetListingInventory
      * putupdateListingInventory
      * getgetListingsInventoryByListingIds
    * ShopListing Offering
      * getgetListingOffering
    * ShopListing Personalization
      * deldeleteListingPersonalization
      * postupdateListingPersonalization
      * getgetListingPersonalization
    * ShopListing Product
      * getgetListingProduct
    * ShopListing Translation
      * postcreateListingTranslation
      * getgetListingTranslation
      * putupdateListingTranslation
    * ShopListing VariationImage
      * getgetListingVariationImages
      * postupdateVariationImages
    * ShopListing Video
      * deldeleteListingVideo
      * getgetListingVideo
      * getgetListingVideos
      * postuploadListingVideo
  * Other
    * Other
      * getping
      * posttokenScopes
  * Payment Management
    * Ledger Entry
      * getgetShopPaymentAccountLedgerEntry
      * getgetShopPaymentAccountLedgerEntries
    * Payment
      * getgetPaymentAccountLedgerEntryPayments
      * getgetShopPaymentByReceiptId
      * getgetPayments
  * Receipt Management
    * Shop Receipt
      * getgetShopReceipt
      * putupdateShopReceipt
      * getgetShopReceipts
      * postcreateReceiptShipment
    * Shop Receipt Transactions
      * getgetShopReceiptTransactionsByListing
      * getgetShopReceiptTransactionsByReceipt
      * getgetShopReceiptTransaction
      * getgetShopReceiptTransactionsByShop
  * Review Management
    * Review
      * getgetReviewsByListing
      * getgetReviewsByShop
  * Shipping Management
    * Shop HolidayPreferences
      * getgetHolidayPreferences
      * putupdateHolidayPreferences
    * Shop ProcessingProfiles
      * postcreateShopReadinessStateDefinition
      * getgetShopReadinessStateDefinitions
      * deldeleteShopReadinessStateDefinition
      * getgetShopReadinessStateDefinition
      * putupdateShopReadinessStateDefinition
    * Shop ShippingProfile
      * getgetShippingCarriers
      * postcreateShopShippingProfile
      * getgetShopShippingProfiles
      * deldeleteShopShippingProfile
      * getgetShopShippingProfile
      * putupdateShopShippingProfile
      * postcreateShopShippingProfileDestination
      * getgetShopShippingProfileDestinationsByShippingProfile
      * deldeleteShopShippingProfileDestination
      * putupdateShopShippingProfileDestination
      * postcreateShopShippingProfileUpgrade
      * getgetShopShippingProfileUpgrades
      * deldeleteShopShippingProfileUpgrade
      * putupdateShopShippingProfileUpgrade
  * Shop Management
    * Shop
      * getgetShop
      * putupdateShop
      * getgetShopByOwnerUserId
      * getfindShops
    * Shop ProductionPartner
      * getgetShopProductionPartners
    * Shop Section
      * postcreateShopSection
      * getgetShopSections
      * deldeleteShopSection
      * getgetShopSection
      * putupdateShopSection
  * Shop Policy Management
    * Shop Return Policy
      * postconsolidateShopReturnPolicies
      * postcreateShopReturnPolicy
      * getgetShopReturnPolicies
      * deldeleteShopReturnPolicy
      * getgetShopReturnPolicy
      * putupdateShopReturnPolicy
  * User Management
    * User
      * getgetUser
      * getgetMe
    * UserAddress
      * getgetUserAddress
      * getgetUserAddresses


[Documentation Powered by ReDoc](https://github.com/Redocly/redoc)
# Etsy Open API v3 (3.0.0)
Download OpenAPI specification:[Download](https://www.etsy.com/openapi/generated/oas/3.0.0.json)
E-mail: developers@etsy.com [Terms of Service](https://www.etsy.com/legal/api)
Etsy's Open API provides a simple RESTful interface for various Etsy.com features.
If you'd like to report an issue or provide feedback on the API design, [please add an issue in Github](https://github.com/etsy/open-api/discussions).
© 2021-2026 Etsy, Inc. All Rights Reserved. Use of this code is subject to Etsy's [API Developer Terms of Use](https://www.etsy.com/legal/api). 
#  [](https://developer.etsy.com/documentation/reference/#section/Authentication)Authentication
##  [](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)api_key
Every request to a v3 API endpoint must include this data in the format `keystring:shared_secret`. Your keystring and shared secret are available on the [Your Apps](https://www.etsy.com/developers/your-apps) page.  
|  Security Scheme Type   |  API Key   |  
| --- | --- |  
|  Header parameter name:  |  x-api-key   |  
##  [](https://developer.etsy.com/documentation/reference/#section/Authentication/oauth2)oauth2
Open API v3 supports authenticating via OAuth 2.0. More information about Etsy's specific implementation of OAuth2 can be found [here](https://developer.etsy.com/documentation/essentials/oauth2).  
|  Security Scheme Type   |  OAuth2   |  
| --- | --- |  
|  authorizationCode OAuth Flow   |  **Authorization URL:** https://www.etsy.com/oauth/connect **Token URL:** https://openapi.etsy.com/v3/public/oauth/token **Scopes:**
  * `address_r` - see billing and shipping addresses
  * `address_w` - update billing and shipping addresses
  * `email_r` - read a user profile
  * `listings_d` - delete listings
  * `listings_r` - see all listings (including expired etc)
  * `listings_w` - create/edit listings
  * `profile_r` - see all profile data
  * `profile_w` - update user profile, avatar, etc
  * `shops_r` - see private shop info
  * `shops_w` - update shop
  * `transactions_r` - see all checkout/payment data
  * `transactions_w` - update receipts

 |  
#  [](https://developer.etsy.com/documentation/reference/#tag/BuyerTaxonomy)BuyerTaxonomy
##  [](https://developer.etsy.com/documentation/reference/#operation/getBuyerTaxonomyNodes)getBuyerTaxonomyNodes 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Retrieves the full hierarchy tree of buyer taxonomy nodes.
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)
### Responses
**200**
List the full hierarchy tree of buyer taxonomy nodes.
**500**
The server encountered an internal error. See the error message for details.
get/v3/application/buyer-taxonomy/nodes
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/buyer-taxonomy/nodes
###  Response samples 
  * 200
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
 
  *  "count": 0, 
 
  *  "results": [
    *  { 
      *  "id": 1, 
 
      *  "level": 0, 
 
      *  "name": "string", 
 
      *  "parent_id": null, 
 
      *  "children": [
        * { }
 ], 
 
      *  "full_path_taxonomy_ids": [
        * 1
 ] 
  } 
 ] 
 
 }`
##  [](https://developer.etsy.com/documentation/reference/#operation/getPropertiesByBuyerTaxonomyId)getPropertiesByBuyerTaxonomyId 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Retrieves a list of product properties, with applicable scales and values, supported for a specific buyer taxonomy ID.
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)
##### path Parameters  
|  taxonomy_id required   |  integer <int64> >= 1  The unique numeric ID of an Etsy taxonomy node, which is a metadata category for listings organized into the seller taxonomy hierarchy tree. For example, the "shoes" taxonomy node (ID: 1429, level: 1) is higher in the hierarchy than "girls' shoes" (ID: 1440, level: 2). The taxonomy nodes assigned to a listing support access to specific standardized product scales and properties. For example, listings assigned the taxonomy nodes "shoes" or "girls' shoes" support access to the "EU" shoe size scale with its associated property names and IDs for EU shoe sizes, such as property `value_id`:"1394", and `name`:"38".  |  
| --- | --- |  
### Responses
**200**
A list of product properties, with applicable scales and values.
**400**
There was a problem with the request data. See the error message for details.
**404**
A resource could not be found. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
get/v3/application/buyer-taxonomy/nodes/{taxonomy_id}/properties
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/buyer-taxonomy/nodes/{taxonomy_id}/properties
###  Response samples 
  * 200
  * 400
  * 404
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
 
  *  "count": 0, 
 
  *  "results": [
    *  { 
      *  "property_id": 1, 
 
      *  "name": "string", 
 
      *  "display_name": "string", 
 
      *  "scales": [
        *  { 
          *  "scale_id": 1, 
 
          *  "display_name": "string", 
 
          *  "description": "string" 
  } 
 ], 
 
      *  "is_required": true, 
 
      *  "supports_attributes": true, 
 
      *  "supports_variations": true, 
 
      *  "is_multivalued": true, 
 
      *  "max_values_allowed": 0, 
 
      *  "possible_values": [
        *  { 
          *  "value_id": 1, 
 
          *  "name": "string", 
 
          *  "scale_id": 1, 
 
          *  "equal_to": [
            * 0
 ] 
  } 
 ], 
 
      *  "selected_values": [
        *  { 
          *  "value_id": 1, 
 
          *  "name": "string", 
 
          *  "scale_id": 1, 
 
          *  "equal_to": [
            * 0
 ] 
  } 
 ] 
  } 
 ] 
 
 }`
#  [](https://developer.etsy.com/documentation/reference/#tag/SellerTaxonomy)SellerTaxonomy
##  [](https://developer.etsy.com/documentation/reference/#operation/getSellerTaxonomyNodes)getSellerTaxonomyNodes 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Retrieves the full hierarchy tree of seller taxonomy nodes.
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)
### Responses
**200**
List the full hierarchy tree of seller taxonomy nodes.
**500**
The server encountered an internal error. See the error message for details.
**503**
The service is unavailable
get/v3/application/seller-taxonomy/nodes
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/seller-taxonomy/nodes
###  Response samples 
  * 200
  * 500
  * 503


Content type
application/json
Copy
Expand all  Collapse all 
`{
 
  *  "count": 0, 
 
  *  "results": [
    *  { 
      *  "id": 1, 
 
      *  "level": 0, 
 
      *  "name": "string", 
 
      *  "parent_id": null, 
 
      *  "children": [
        * { }
 ], 
 
      *  "full_path_taxonomy_ids": [
        * 1
 ] 
  } 
 ] 
 
 }`
##  [](https://developer.etsy.com/documentation/reference/#operation/getPropertiesByTaxonomyId)getPropertiesByTaxonomyId 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Retrieves a list of product properties, with applicable scales and values, supported for a specific seller taxonomy ID.
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)
##### path Parameters  
|  taxonomy_id required   |  integer <int64> >= 1  The unique numeric ID of an Etsy taxonomy node, which is a metadata category for listings organized into the seller taxonomy hierarchy tree. For example, the "shoes" taxonomy node (ID: 1429, level: 1) is higher in the hierarchy than "girls' shoes" (ID: 1440, level: 2). The taxonomy nodes assigned to a listing support access to specific standardized product scales and properties. For example, listings assigned the taxonomy nodes "shoes" or "girls' shoes" support access to the "EU" shoe size scale with its associated property names and IDs for EU shoe sizes, such as property `value_id`:"1394", and `name`:"38".  |  
| --- | --- |  
##### query Parameters  
| supports_variations  |  boolean Nullable  When `true`, returns properties that support variations. When `false`, returns properties that do not support variations.  |  
| --- | --- |  
| supports_attributes  |  boolean Nullable  When `true`, returns properties that support attributes. When `false`, returns properties that do not support attributes.  |  
### Responses
**200**
A list of product properties, with applicable scales and values.
**400**
There was a problem with the request data. See the error message for details.
**404**
A resource could not be found. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
get/v3/application/seller-taxonomy/nodes/{taxonomy_id}/properties
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/seller-taxonomy/nodes/{taxonomy_id}/properties
###  Response samples 
  * 200
  * 400
  * 404
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
 
  *  "count": 0, 
 
  *  "results": [
    *  { 
      *  "property_id": 1, 
 
      *  "name": "string", 
 
      *  "display_name": "string", 
 
      *  "scales": [
        *  { 
          *  "scale_id": 1, 
 
          *  "display_name": "string", 
 
          *  "description": "string" 
  } 
 ], 
 
      *  "is_required": true, 
 
      *  "supports_attributes": true, 
 
      *  "supports_variations": true, 
 
      *  "is_multivalued": true, 
 
      *  "max_values_allowed": 0, 
 
      *  "possible_values": [
        *  { 
          *  "value_id": 1, 
 
          *  "name": "string", 
 
          *  "scale_id": 1, 
 
          *  "equal_to": [
            * 0
 ] 
  } 
 ], 
 
      *  "selected_values": [
        *  { 
          *  "value_id": 1, 
 
          *  "name": "string", 
 
          *  "scale_id": 1, 
 
          *  "equal_to": [
            * 0
 ] 
  } 
 ] 
  } 
 ] 
 
 }`
#  [](https://developer.etsy.com/documentation/reference/#tag/ShopListing)ShopListing
##  [](https://developer.etsy.com/documentation/reference/#operation/createDraftListing)createDraftListing 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Creates a physical draft [listing](https://developer.etsy.com/documentation/reference#tag/ShopListing) product in a shop on the Etsy channel.
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)[oauth2](https://developer.etsy.com/documentation/reference/#section/Authentication/oauth2) (`listings_w`) 
##### path Parameters  
|  shop_id required   |  integer <int64> >= 1  The unique positive non-zero numeric ID for an Etsy Shop.  |  
| --- | --- |  
##### Request Body schema: application/x-www-form-urlencoded  
|  quantity required   |  integer <int64> The positive non-zero number of products available for purchase in the listing. Note: The listing quantity is the sum of available offering quantities. You can request the quantities for individual offerings from the ListingInventory resource using the [getListingInventory](https://developer.etsy.com/documentation/reference#operation/getListingInventory) endpoint.  |  
| --- | --- |  
|  title required   |  string The listing's title string. When creating or updating a listing, valid title strings contain only letters, numbers, punctuation marks, mathematical symbols, whitespace characters, ™, ©, and ®. (regex: /[^\p{L}\p{Nd}\p{P}\p{Sm}\p{Zs}™©®]/u) You can only use the %, :, & and + characters once each.  |  
|  description required   |  string A description string of the product for sale in the listing.  |  
|  price required   |  number <float> The positive non-zero price of the product. (Sold product listings are private) Note: The price is the minimum possible price. The [`getListingInventory`](https://developer.etsy.com/documentation/reference/#operation/getListingInventory) method requests exact prices for available offerings.  |  
|  who_made required   |  string Enum: "i_did" "someone_else" "collective" An enumerated string indicating who made the product. Helps buyers locate the listing under the Handmade heading. Requires 'is_supply' and 'when_made'.  |  
|  when_made required   |  string Enum: "made_to_order" "2020_2026" "2010_2019" "2007_2009" "before_2007" "2000_2006" "1990s" "1980s" "1970s" "1960s" "1950s" "1940s" "1930s" "1920s" "1910s" "1900s" "1800s" "1700s" "before_1700" An enumerated string for the era in which the maker made the product in this listing. Helps buyers locate the listing under the Vintage heading. Requires 'is_supply' and 'who_made'.  |  
|  taxonomy_id required   |  integer <int64> >= 1  The numerical taxonomy ID of the listing. See [SellerTaxonomy](https://developer.etsy.com/documentation/reference#tag/SellerTaxonomy) and [BuyerTaxonomy](https://developer.etsy.com/documentation/reference#tag/BuyerTaxonomy) for more information.  |  
| shipping_profile_id  |  integer <int64> >= 1  Nullable  The numeric ID of the [shipping profile](https://developer.etsy.com/documentation/reference#operation/getShopShippingProfile) associated with the listing. Required when listing type is `physical`.  |  
| return_policy_id  |  integer <int64> >= 1  Nullable  The numeric ID of the [Return Policy](https://developer.etsy.com/documentation/reference#operation/getShopReturnPolicies).  |  
| materials  |  Array of strings Nullable  A list of material strings for materials used in the product. Valid materials strings contain only letters, numbers, and whitespace characters. (regex: /[^\p{L}\p{Nd}\p{Zs}]/u) Default value is null.  |  
| shop_section_id  |  integer <int64> >= 1  Nullable  The numeric ID of the [shop section](https://developer.etsy.com/documentation/reference#tag/Shop-Section) for this listing. Default value is null.  |  
| processing_min  |  integer <int64> Nullable  The minimum number of days required to process this listing. Default value is null.  |  
| processing_max  |  integer <int64> Nullable  The maximum number of days required to process this listing. Default value is null.  |  
| readiness_state_id  |  integer <int64> >= 1  Nullable  The numeric ID of the [processing profile](https://developer.etsy.com/documentation/reference#operation/getShopReadinessStateDefinition) associated with the listing. Returned only when the listing is `active` and of type `physical`, and the endpoint is either shop-scoped (path contains `shop_id`) or a single-listing request such as `getListing`. For every other case this field can be null.  |  
| tags  |  Array of strings Nullable  A comma-separated list of tag strings for the listing. When creating or updating a listing, valid tag strings contain only letters, numbers, whitespace characters, -, ', ™, ©, and ®. (regex: /[^\p{L}\p{Nd}\p{Zs}-'™©®]/u) Default value is null.  |  
| styles  |  Array of strings Nullable  An array of style strings for this listing, each of which is free-form text string such as "Formal", or "Steampunk". When creating or updating a listing, the listing may have up to two styles. Valid style strings contain only letters, numbers, and whitespace characters. (regex: /[^\p{L}\p{Nd}\p{Zs}]/u) Each style string is limited to 45 characters. Default value is null.  |  
| item_weight  |  number <float> [ 0 .. 1.79769313486e+308 ]  Nullable  The numeric weight of the product measured in units set in 'item_weight_unit'. Default value is null. If set, the value must be greater than 0.  |  
| item_length  |  number <float> [ 0 .. 1.79769313486e+308 ]  Nullable  The numeric length of the product measured in units set in 'item_dimensions_unit'. Default value is null. If set, the value must be greater than 0.  |  
| item_width  |  number <float> [ 0 .. 1.79769313486e+308 ]  Nullable  The numeric width of the product measured in units set in 'item_dimensions_unit'. Default value is null. If set, the value must be greater than 0.  |  
| item_height  |  number <float> [ 0 .. 1.79769313486e+308 ]  Nullable  The numeric height of the product measured in units set in 'item_dimensions_unit'. Default value is null. If set, the value must be greater than 0.  |  
| item_weight_unit  |  string Nullable  Enum: "oz" "lb" "g" "kg" A string defining the units used to measure the weight of the product. Default value is null.  |  
| item_dimensions_unit  |  string Nullable  Enum: "in" "ft" "mm" "cm" "m" "yd" "inches" A string defining the units used to measure the dimensions of the product. Default value is null.  |  
| production_partner_ids  |  Array of integers <int64> Nullable  An array of unique IDs of production partner ids.  |  
| image_ids  |  Array of integers <int64> Nullable  An array of numeric image IDs of the images in a listing, which can include up to 20 images.  |  
| ecgt_garan_brand  |  string Nullable  The brand or trademark name for the EU commercial guarantee (required under GPSR/ECGT for eligible EU traders). Maximum 25 characters. See the [Etsy Seller Handbook](https://help.etsy.com/hc/articles/43191692248343) for details. If any one of ecgt_garan_brand, ecgt_garan_model, ecgt_garan_years, or ecgt_garan_guarantee_details is provided and non-empty, all four are required. Silently ignored for digital listings and for sellers who are not eligible EU traders.  |  
| ecgt_garan_years  |  integer <int64> Nullable  Duration of the EU commercial guarantee in whole years (minimum 3, maximum 99). Required together with ecgt_garan_brand, ecgt_garan_model, and ecgt_garan_guarantee_details. Silently ignored for digital listings and for sellers who are not eligible EU traders.  |  
| ecgt_garan_model  |  string Nullable  The product model or reference number for the EU commercial guarantee label. Maximum 20 characters. Required together with ecgt_garan_brand, ecgt_garan_years, and ecgt_garan_guarantee_details. Silently ignored for digital listings and for sellers who are not eligible EU traders.  |  
| ecgt_garan_guarantee_details  |  string Nullable  Free-text description of the EU commercial guarantee terms and coverage. Maximum 255 characters. Required together with ecgt_garan_brand, ecgt_garan_model, and ecgt_garan_years. Silently ignored for digital listings and for sellers who are not eligible EU traders.  |  
| ecgt_other_commercial_guarantee_details  |  string Nullable  Free-text details of any additional commercial guarantee or warranty beyond the primary EU commercial guarantee. Maximum 255 characters. Silently ignored for digital listings and for sellers who are not eligible EU traders.  |  
| ecgt_after_sales_service_info  |  string Nullable  After-sales service, repairability, or eco-friendly delivery information required under EU GPSR/ECGT regulations. Maximum 255 characters. Silently ignored for digital listings and for sellers who are not eligible EU traders.  |  
| ecgt_software_update_details  |  string Nullable  Details of software update availability and the duration of such updates, as required under EU ECGT regulations for digital content. Maximum 255 characters. Silently ignored for physical listings and for sellers who are not eligible EU traders.  |  
| is_supply  |  boolean When true, tags the listing as a supply product, else indicates that it's a finished product. Helps buyers locate the listing under the Supplies heading. Requires 'who_made' and 'when_made'.  |  
| is_customizable  |  boolean When true, a buyer may contact the seller for a customized order. The default value is true when a shop accepts custom orders. Does not apply to shops that do not accept custom orders.  |  
| should_auto_renew  |  boolean When true, renews a listing for four months upon expiration.  |  
| is_taxable  |  boolean When true, applicable [shop](https://developer.etsy.com/documentation/reference#tag/Shop) tax rates apply to this listing at checkout.  |  
| type  |  string Enum: "physical" "download" "both" An enumerated type string that indicates whether the listing is physical or a digital download.  |  
### Responses
**201**
A single ShopListing
**400**
There was a problem with the request data. See the error message for details.
**401**
The request lacks valid authentication credentials. See the error message for details.
**403**
The request attempted to perform an operation it is not allowed to. See the error message for details.
**404**
A resource could not be found. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
post/v3/application/shops/{shop_id}/listings
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/shops/{shop_id}/listings
###  Response samples 
  * 201
  * 400
  * 401
  * 403
  * 404
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
 
  *  "listing_id": 1, 
 
  *  "user_id": 1, 
 
  *  "shop_id": 1, 
 
  *  "title": "string", 
 
  *  "description": "string", 
 
  *  "state": "active", 
 
  *  "creation_timestamp": 946684800, 
 
  *  "created_timestamp": 946684800, 
 
  *  "ending_timestamp": 946684800, 
 
  *  "original_creation_timestamp": 946684800, 
 
  *  "last_modified_timestamp": 946684800, 
 
  *  "updated_timestamp": 946684800, 
 
  *  "state_timestamp": 946684800, 
 
  *  "quantity": 0, 
 
  *  "shop_section_id": 1, 
 
  *  "featured_rank": 0, 
 
  *  "url": "string", 
 
  *  "num_favorers": 0, 
 
  *  "non_taxable": true, 
 
  *  "is_taxable": true, 
 
  *  "is_customizable": true, 
 
  *  "is_personalizable": true, 
 
  *  "listing_type": "physical", 
 
  *  "tags": [
    * "string"
 ], 
 
  *  "materials": [
    * "string"
 ], 
 
  *  "shipping_profile_id": 1, 
 
  *  "return_policy_id": 1, 
 
  *  "processing_min": 0, 
 
  *  "processing_max": 0, 
 
  *  "who_made": "i_did", 
 
  *  "when_made": "made_to_order", 
 
  *  "is_supply": true, 
 
  *  "item_weight": 0, 
 
  *  "item_weight_unit": "oz", 
 
  *  "item_length": 0, 
 
  *  "item_width": 0, 
 
  *  "item_height": 0, 
 
  *  "item_dimensions_unit": "in", 
 
  *  "is_private": true, 
 
  *  "style": [
    * "string"
 ], 
 
  *  "file_data": "string", 
 
  *  "has_variations": true, 
 
  *  "should_auto_renew": true, 
 
  *  "language": "string", 
 
  *  "price": { 
    *  "amount": 0, 
 
    *  "divisor": 0, 
 
    *  "currency_code": "string" 
  }, 
 
  *  "converted_price": { 
    *  "amount": 0, 
 
    *  "divisor": 0, 
 
    *  "currency_code": "string" 
  }, 
 
  *  "taxonomy_id": 0, 
 
  *  "readiness_state_id": 1, 
 
  *  "suggested_title": "string", 
 
  *  "ecgt_garan_brand": "string", 
 
  *  "ecgt_garan_years": 0, 
 
  *  "ecgt_garan_model": "string", 
 
  *  "ecgt_garan_guarantee_details": "string", 
 
  *  "ecgt_other_commercial_guarantee_details": "string", 
 
  *  "ecgt_after_sales_service_info": "string", 
 
  *  "ecgt_software_update_details": "string", 
 
  *  "ecgt_commercial_guarantee_enabled": true 
 
 }`
##  [](https://developer.etsy.com/documentation/reference/#operation/getListingsByShop)getListingsByShop 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Endpoint to list Listings that belong to a Shop. Listings can be filtered using the 'state' param.
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)[oauth2](https://developer.etsy.com/documentation/reference/#section/Authentication/oauth2) (`listings_r`) 
##### path Parameters  
|  shop_id required   |  integer <int64> >= 1  The unique positive non-zero numeric ID for an Etsy Shop.  |  
| --- | --- |  
##### query Parameters  
| state  |  string Default:  "active" Enum: "active" "inactive" "sold_out" "draft" "removed" "expired" When _updating_ a listing, this value can be either `active` or `inactive`. Note: Setting a `draft` listing to `active` will also publish the listing on etsy.com and requires that the listing have an image set. Setting a `sold_out` listing to active will update the quantity to 1 and renew the listing on etsy.com.  |  
| --- | --- |  
| limit  |  integer <int64> [ 1 .. 100 ]  Default:  25 The maximum number of results to return.  |  
| offset  |  integer <int64> >= 0  Default:  0 The number of records to skip before selecting the first result.  |  
| sort_on  |  string Default:  "created" Enum: "created" "price" "updated" "score" The value to sort a search result of listings on. NOTES: a) `sort_on` only works when combined with one of the search options (keywords, region, etc.). b) when using `score` the returned results will always be in _descending_ order, regardless of the `sort_order` parameter.  |  
| sort_order  |  string Default:  "desc" Enum: "asc" "ascending" "desc" "descending" "up" "down" The ascending(up) or descending(down) order to sort listings by. NOTE: sort_order only works when combined with one of the search options (keywords, region, etc.).  |  
| includes  |  Array of strings Default:  null Items Enum: "Shipping" "Images" "Shop" "User" "Translations" "Inventory" "Videos" "Personalization" "BuyerPrice" An enumerated string that attaches a valid association. Acceptable inputs are 'Shipping', 'Shop', 'Images', 'User', 'Translations', 'Videos', 'Inventory' and 'Personalization'.  |  
### Responses
**200**
A list of Listings
**400**
There was a problem with the request data. See the error message for details.
**401**
The request lacks valid authentication credentials. See the error message for details.
**403**
The request attempted to perform an operation it is not allowed to. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
get/v3/application/shops/{shop_id}/listings
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/shops/{shop_id}/listings
###  Response samples 
  * 200
  * 400
  * 401
  * 403
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
 
  *  "count": 0, 
 
  *  "results": [
    *  { 
      *  "listing_id": 1, 
 
      *  "user_id": 1, 
 
      *  "shop_id": 1, 
 
      *  "title": "string", 
 
      *  "description": "string", 
 
      *  "state": "active", 
 
      *  "creation_timestamp": 946684800, 
 
      *  "created_timestamp": 946684800, 
 
      *  "ending_timestamp": 946684800, 
 
      *  "original_creation_timestamp": 946684800, 
 
      *  "last_modified_timestamp": 946684800, 
 
      *  "updated_timestamp": 946684800, 
 
      *  "state_timestamp": 946684800, 
 
      *  "quantity": 0, 
 
      *  "shop_section_id": 1, 
 
      *  "featured_rank": 0, 
 
      *  "url": "string", 
 
      *  "num_favorers": 0, 
 
      *  "non_taxable": true, 
 
      *  "is_taxable": true, 
 
      *  "is_customizable": true, 
 
      *  "is_personalizable": true, 
 
      *  "listing_type": "physical", 
 
      *  "tags": [
        * "string"
 ], 
 
      *  "materials": [
        * "string"
 ], 
 
      *  "shipping_profile_id": 1, 
 
      *  "return_policy_id": 1, 
 
      *  "processing_min": 0, 
 
      *  "processing_max": 0, 
 
      *  "who_made": "i_did", 
 
      *  "when_made": "made_to_order", 
 
      *  "is_supply": true, 
 
      *  "item_weight": 0, 
 
      *  "item_weight_unit": "oz", 
 
      *  "item_length": 0, 
 
      *  "item_width": 0, 
 
      *  "item_height": 0, 
 
      *  "item_dimensions_unit": "in", 
 
      *  "is_private": true, 
 
      *  "style": [
        * "string"
 ], 
 
      *  "file_data": "string", 
 
      *  "has_variations": true, 
 
      *  "should_auto_renew": true, 
 
      *  "language": "string", 
 
      *  "price": { 
        *  "amount": 0, 
 
        *  "divisor": 0, 
 
        *  "currency_code": "string" 
  }, 
 
      *  "converted_price": { 
        *  "amount": 0, 
 
        *  "divisor": 0, 
 
        *  "currency_code": "string" 
  }, 
 
      *  "taxonomy_id": 0, 
 
      *  "readiness_state_id": 1, 
 
      *  "suggested_title": "string", 
 
      *  "ecgt_garan_brand": "string", 
 
      *  "ecgt_garan_years": 0, 
 
      *  "ecgt_garan_model": "string", 
 
      *  "ecgt_garan_guarantee_details": "string", 
 
      *  "ecgt_other_commercial_guarantee_details": "string", 
 
      *  "ecgt_after_sales_service_info": "string", 
 
      *  "ecgt_software_update_details": "string", 
 
      *  "ecgt_commercial_guarantee_enabled": true, 
 
      *  "shipping_profile": { 
        *  "shipping_profile_id": 1, 
 
        *  "title": "string", 
 
        *  "user_id": 1, 
 
        *  "origin_country_iso": "string", 
 
        *  "is_deleted": true, 
 
        *  "shipping_profile_destinations": [
          *  { 
            *  "shipping_profile_destination_id": 1, 
 
            *  "shipping_profile_id": 1, 
 
            *  "origin_country_iso": "string", 
 
            *  "destination_country_iso": "string", 
 
            *  "destination_region": "eu", 
 
            *  "primary_cost": { 
              *  "amount": 0, 
 
              *  "divisor": 0, 
 
              *  "currency_code": "string" 
  }, 
 
            *  "secondary_cost": { 
              *  "amount": 0, 
 
              *  "divisor": 0, 
 
              *  "currency_code": "string" 
  }, 
 
            *  "shipping_carrier_id": 0, 
 
            *  "mail_class": "string", 
 
            *  "min_delivery_days": 1, 
 
            *  "max_delivery_days": 1 
  } 
 ], 
 
        *  "shipping_profile_upgrades": [
          *  { 
            *  "shipping_profile_id": 1, 
 
            *  "upgrade_id": 1, 
 
            *  "upgrade_name": "string", 
 
            *  "type": 0, 
 
            *  "rank": 0, 
 
            *  "language": "string", 
 
            *  "price": { 
              *  "amount": 0, 
 
              *  "divisor": 0, 
 
              *  "currency_code": "string" 
  }, 
 
            *  "secondary_price": { 
              *  "amount": 0, 
 
              *  "divisor": 0, 
 
              *  "currency_code": "string" 
  }, 
 
            *  "shipping_carrier_id": 0, 
 
            *  "mail_class": "string", 
 
            *  "min_delivery_days": 1, 
 
            *  "max_delivery_days": 1 
  } 
 ], 
 
        *  "origin_postal_code": "string", 
 
        *  "profile_type": "manual", 
 
        *  "domestic_handling_fee": 0, 
 
        *  "international_handling_fee": 0 
  }, 
 
      *  "user": { 
        *  "user_id": 1, 
 
        *  "primary_email": "user@example.com", 
 
        *  "first_name": "string", 
 
        *  "last_name": "string", 
 
        *  "image_url_75x75": "string" 
  }, 
 
      *  "shop": { 
        *  "shop_id": 1, 
 
        *  "user_id": 1, 
 
        *  "shop_name": "string", 
 
        *  "create_date": 0, 
 
        *  "created_timestamp": 0, 
 
        *  "title": "string", 
 
        *  "announcement": "string", 
 
        *  "currency_code": "string", 
 
        *  "is_vacation": true, 
 
        *  "vacation_message": "string", 
 
        *  "sale_message": "string", 
 
        *  "digital_sale_message": "string", 
 
        *  "update_date": 0, 
 
        *  "updated_timestamp": 0, 
 
        *  "listing_active_count": 0, 
 
        *  "digital_listing_count": 0, 
 
        *  "login_name": "string", 
 
        *  "accepts_custom_requests": true, 
 
        *  "policy_welcome": "string", 
 
        *  "policy_payment": "string", 
 
        *  "policy_shipping": "string", 
 
        *  "policy_refunds": "string", 
 
        *  "policy_additional": "string", 
 
        *  "policy_seller_info": "string", 
 
        *  "policy_update_date": 0, 
 
        *  "policy_has_private_receipt_info": true, 
 
        *  "has_unstructured_policies": true, 
 
        *  "policy_privacy": "string", 
 
        *  "vacation_autoreply": "string", 
 
        *  "url": "string", 
 
        *  "image_url_760x100": "string", 
 
        *  "num_favorers": 0, 
 
        *  "languages": [
          * "string"
 ], 
 
        *  "icon_url_fullxfull": "string", 
 
        *  "is_using_structured_policies": true, 
 
        *  "has_onboarded_structured_policies": true, 
 
        *  "include_dispute_form_link": true, 
 
        *  "is_direct_checkout_onboarded": true, 
 
        *  "is_etsy_payments_onboarded": true, 
 
        *  "is_calculated_eligible": true, 
 
        *  "is_opted_in_to_buyer_promise": true, 
 
        *  "is_shop_us_based": true, 
 
        *  "transaction_sold_count": 0, 
 
        *  "shipping_from_country_iso": "string", 
 
        *  "shop_location_country_iso": "string", 
 
        *  "review_count": 0, 
 
        *  "review_average": 0 
  }, 
 
      *  "images": [
        *  { 
          *  "listing_id": 1, 
 
          *  "listing_image_id": 1, 
 
          *  "hex_code": "string", 
 
          *  "red": 0, 
 
          *  "green": 0, 
 
          *  "blue": 0, 
 
          *  "hue": 0, 
 
          *  "saturation": 0, 
 
          *  "brightness": 0, 
 
          *  "is_black_and_white": true, 
 
          *  "creation_tsz": 0, 
 
          *  "created_timestamp": 0, 
 
          *  "rank": 0, 
 
          *  "url_75x75": "string", 
 
          *  "url_170x135": "string", 
 
          *  "url_570xN": "string", 
 
          *  "url_fullxfull": "string", 
 
          *  "full_height": 0, 
 
          *  "full_width": 0, 
 
          *  "alt_text": "string" 
  } 
 ], 
 
      *  "videos": [
        *  { 
          *  "video_id": 1, 
 
          *  "height": 0, 
 
          *  "width": 0, 
 
          *  "thumbnail_url": "string", 
 
          *  "video_url": "string", 
 
          *  "video_state": "active" 
  } 
 ], 
 
      *  "inventory": { 
        *  "products": [
          *  { 
            *  "product_id": 1, 
 
            *  "sku": "string", 
 
            *  "is_deleted": true, 
 
            *  "offerings": [
              *  { 
                *  "offering_id": 1, 
 
                *  "quantity": 0, 
 
                *  "is_enabled": true, 
 
                *  "is_deleted": true, 
 
                *  "price": { 
                  *  "amount": 0, 
 
                  *  "divisor": 0, 
 
                  *  "currency_code": "string" 
  }, 
 
                *  "readiness_state_id": 1 
  } 
 ], 
 
            *  "property_values": [
              *  { 
                *  "property_id": 1, 
 
                *  "property_name": "string", 
 
                *  "scale_id": 1, 
 
                *  "scale_name": "string", 
 
                *  "value_ids": [
                  * 1
 ], 
 
                *  "values": [
                  * "string"
 ] 
  } 
 ] 
  } 
 ], 
 
        *  "price_on_property": [
          * 0
 ], 
 
        *  "quantity_on_property": [
          * 0
 ], 
 
        *  "sku_on_property": [
          * 0
 ], 
 
        *  "readiness_state_on_property": [
          * 1
 ] 
  }, 
 
      *  "production_partners": [
        *  { 
          *  "production_partner_id": 1, 
 
          *  "partner_name": "string", 
 
          *  "location": "string" 
  } 
 ], 
 
      *  "skus": [
        * "string"
 ], 
 
      *  "translations": { 
        *  "de": { 
          *  "listing_id": 1, 
 
          *  "language": "string", 
 
          *  "title": "string", 
 
          *  "description": "string", 
 
          *  "tags": [
            * "string"
 ] 
  }, 
 
        *  "en-GB": { 
          *  "listing_id": 1, 
 
          *  "language": "string", 
 
          *  "title": "string", 
 
          *  "description": "string", 
 
          *  "tags": [
            * "string"
 ] 
  }, 
 
        *  "en-IN": { 
          *  "listing_id": 1, 
 
          *  "language": "string", 
 
          *  "title": "string", 
 
          *  "description": "string", 
 
          *  "tags": [
            * "string"
 ] 
  }, 
 
        *  "en-US": { 
          *  "listing_id": 1, 
 
          *  "language": "string", 
 
          *  "title": "string", 
 
          *  "description": "string", 
 
          *  "tags": [
            * "string"
 ] 
  }, 
 
        *  "es": { 
          *  "listing_id": 1, 
 
          *  "language": "string", 
 
          *  "title": "string", 
 
          *  "description": "string", 
 
          *  "tags": [
            * "string"
 ] 
  }, 
 
        *  "fr": { 
          *  "listing_id": 1, 
 
          *  "language": "string", 
 
          *  "title": "string", 
 
          *  "description": "string", 
 
          *  "tags": [
            * "string"
 ] 
  }, 
 
        *  "it": { 
          *  "listing_id": 1, 
 
          *  "language": "string", 
 
          *  "title": "string", 
 
          *  "description": "string", 
 
          *  "tags": [
            * "string"
 ] 
  }, 
 
        *  "ja": { 
          *  "listing_id": 1, 
 
          *  "language": "string", 
 
          *  "title": "string", 
 
          *  "description": "string", 
 
          *  "tags": [
            * "string"
 ] 
  }, 
 
        *  "nl": { 
          *  "listing_id": 1, 
 
          *  "language": "string", 
 
          *  "title": "string", 
 
          *  "description": "string", 
 
          *  "tags": [
            * "string"
 ] 
  }, 
 
        *  "pl": { 
          *  "listing_id": 1, 
 
          *  "language": "string", 
 
          *  "title": "string", 
 
          *  "description": "string", 
 
          *  "tags": [
            * "string"
 ] 
  }, 
 
        *  "pt": { 
          *  "listing_id": 1, 
 
          *  "language": "string", 
 
          *  "title": "string", 
 
          *  "description": "string", 
 
          *  "tags": [
            * "string"
 ] 
  }, 
 
        *  "ru": { 
          *  "listing_id": 1, 
 
          *  "language": "string", 
 
          *  "title": "string", 
 
          *  "description": "string", 
 
          *  "tags": [
            * "string"
 ] 
  }, 
 
        *  "sv": { 
          *  "listing_id": 1, 
 
          *  "language": "string", 
 
          *  "title": "string", 
 
          *  "description": "string", 
 
          *  "tags": [
            * "string"
 ] 
  } 
  }, 
 
      *  "views": 0, 
 
      *  "personalization": {
        *  "personalization_questions": [
          *  { 
            *  "question_id": 1, 
 
            *  "question_text": "string", 
 
            *  "instructions": "string", 
 
            *  "question_type": "string", 
 
            *  "required": true, 
 
            *  "max_allowed_characters": 0, 
 
            *  "max_allowed_files": 0, 
 
            *  "add_on_price": { 
              *  "amount": 0, 
 
              *  "divisor": 0, 
 
              *  "currency_code": "string" 
  }, 
 
            *  "options": [
              *  { 
                *  "option_id": 1, 
 
                *  "label": "string" 
  } 
 ] 
  } 
 ] 
 }, 
 
      *  "buyer_price": { 
        *  "base_price": { 
          *  "amount": 0, 
 
          *  "divisor": 0, 
 
          *  "currency_code": "string" 
  }, 
 
        *  "shipping_cost": { 
          *  "amount": 0, 
 
          *  "divisor": 0, 
 
          *  "currency_code": "string" 
  }, 
 
        *  "is_free_shipping": true, 
 
        *  "original_price": { 
          *  "amount": 0, 
 
          *  "divisor": 0, 
 
          *  "currency_code": "string" 
  }, 
 
        *  "discounted_price": { 
          *  "amount": 0, 
 
          *  "divisor": 0, 
 
          *  "currency_code": "string" 
  }, 
 
        *  "discount_amount": { 
          *  "amount": 0, 
 
          *  "divisor": 0, 
 
          *  "currency_code": "string" 
  }, 
 
        *  "discount_percentage": 0, 
 
        *  "has_discount": true, 
 
        *  "discount_start_epoch": 0, 
 
        *  "discount_end_epoch": 0 
  } 
  } 
 ] 
 
 }`
##  [](https://developer.etsy.com/documentation/reference/#operation/deleteListing)deleteListing 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Open API V3 endpoint to delete a ShopListing. A ShopListing can be deleted only if the state is one of the following: SOLD_OUT, DRAFT, EXPIRED, INACTIVE, ACTIVE and is_available or ACTIVE and has seller flags: SUPRESSED (frozen), VACATION, CUSTOM_SHOPS (pattern), SELL_ON_FACEBOOK
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)[oauth2](https://developer.etsy.com/documentation/reference/#section/Authentication/oauth2) (`listings_d`) 
##### path Parameters  
|  listing_id required   |  integer <int64> >= 1  The numeric ID for the [listing](https://developer.etsy.com/documentation/reference#tag/ShopListing) associated to this transaction.  |  
| --- | --- |  
### Responses
**204**
The Listing resource was correctly deleted
**400**
There was a problem with the request data. See the error message for details.
**401**
The request lacks valid authentication credentials. See the error message for details.
**403**
The request attempted to perform an operation it is not allowed to. See the error message for details.
**404**
A resource could not be found. See the error message for details.
**409**
There was a request conflict with the current state of the target resource. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
delete/v3/application/listings/{listing_id}
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/listings/{listing_id}
###  Response samples 
  * 400
  * 401
  * 403
  * 404
  * 409
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
  *  "error": "string" 

 }`
##  [](https://developer.etsy.com/documentation/reference/#operation/getListing)getListing 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Retrieves a listing record by listing ID.
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)
##### path Parameters  
|  listing_id required   |  integer <int64> >= 1  The numeric ID for the [listing](https://developer.etsy.com/documentation/reference#tag/ShopListing) associated to this transaction.  |  
| --- | --- |  
##### query Parameters  
| includes  |  Array of strings Default:  null Items Enum: "Images" "Shop" "User" "Translations" "Videos" "Personalization" "BuyerPrice" An enumerated string that attaches a valid association. Acceptable inputs are 'Shop', 'Images', 'User', 'Translations', 'Videos', 'Personalization' and 'BuyerPrice'.  |  
| --- | --- |  
| language  |  string Default:  null The IETF language tag for the language of this translation. Ex: `de`, `en`, `es`, `fr`, `it`, `ja`, `nl`, `pl`, `pt`.  |  
| allow_suggested_title  |  boolean This parameter will include in the response a suggested title for the listing, if one is available. Since suggestions are only available to the listing's owner, client must submit an oauth_access_token scoped to the owner of the listing.  |  
### Responses
**200**
A single Listing.
**400**
There was a problem with the request data. See the error message for details.
**404**
A resource could not be found. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
get/v3/application/listings/{listing_id}
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/listings/{listing_id}
###  Response samples 
  * 200
  * 400
  * 404
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
 
  *  "listing_id": 1, 
 
  *  "user_id": 1, 
 
  *  "shop_id": 1, 
 
  *  "title": "string", 
 
  *  "description": "string", 
 
  *  "state": "active", 
 
  *  "creation_timestamp": 946684800, 
 
  *  "created_timestamp": 946684800, 
 
  *  "ending_timestamp": 946684800, 
 
  *  "original_creation_timestamp": 946684800, 
 
  *  "last_modified_timestamp": 946684800, 
 
  *  "updated_timestamp": 946684800, 
 
  *  "state_timestamp": 946684800, 
 
  *  "quantity": 0, 
 
  *  "shop_section_id": 1, 
 
  *  "featured_rank": 0, 
 
  *  "url": "string", 
 
  *  "num_favorers": 0, 
 
  *  "non_taxable": true, 
 
  *  "is_taxable": true, 
 
  *  "is_customizable": true, 
 
  *  "is_personalizable": true, 
 
  *  "listing_type": "physical", 
 
  *  "tags": [
    * "string"
 ], 
 
  *  "materials": [
    * "string"
 ], 
 
  *  "shipping_profile_id": 1, 
 
  *  "return_policy_id": 1, 
 
  *  "processing_min": 0, 
 
  *  "processing_max": 0, 
 
  *  "who_made": "i_did", 
 
  *  "when_made": "made_to_order", 
 
  *  "is_supply": true, 
 
  *  "item_weight": 0, 
 
  *  "item_weight_unit": "oz", 
 
  *  "item_length": 0, 
 
  *  "item_width": 0, 
 
  *  "item_height": 0, 
 
  *  "item_dimensions_unit": "in", 
 
  *  "is_private": true, 
 
  *  "style": [
    * "string"
 ], 
 
  *  "file_data": "string", 
 
  *  "has_variations": true, 
 
  *  "should_auto_renew": true, 
 
  *  "language": "string", 
 
  *  "price": { 
    *  "amount": 0, 
 
    *  "divisor": 0, 
 
    *  "currency_code": "string" 
  }, 
 
  *  "converted_price": { 
    *  "amount": 0, 
 
    *  "divisor": 0, 
 
    *  "currency_code": "string" 
  }, 
 
  *  "taxonomy_id": 0, 
 
  *  "readiness_state_id": 1, 
 
  *  "suggested_title": "string", 
 
  *  "ecgt_garan_brand": "string", 
 
  *  "ecgt_garan_years": 0, 
 
  *  "ecgt_garan_model": "string", 
 
  *  "ecgt_garan_guarantee_details": "string", 
 
  *  "ecgt_other_commercial_guarantee_details": "string", 
 
  *  "ecgt_after_sales_service_info": "string", 
 
  *  "ecgt_software_update_details": "string", 
 
  *  "ecgt_commercial_guarantee_enabled": true, 
 
  *  "shipping_profile": { 
    *  "shipping_profile_id": 1, 
 
    *  "title": "string", 
 
    *  "user_id": 1, 
 
    *  "origin_country_iso": "string", 
 
    *  "is_deleted": true, 
 
    *  "shipping_profile_destinations": [
      *  { 
        *  "shipping_profile_destination_id": 1, 
 
        *  "shipping_profile_id": 1, 
 
        *  "origin_country_iso": "string", 
 
        *  "destination_country_iso": "string", 
 
        *  "destination_region": "eu", 
 
        *  "primary_cost": { 
          *  "amount": 0, 
 
          *  "divisor": 0, 
 
          *  "currency_code": "string" 
  }, 
 
        *  "secondary_cost": { 
          *  "amount": 0, 
 
          *  "divisor": 0, 
 
          *  "currency_code": "string" 
  }, 
 
        *  "shipping_carrier_id": 0, 
 
        *  "mail_class": "string", 
 
        *  "min_delivery_days": 1, 
 
        *  "max_delivery_days": 1 
  } 
 ], 
 
    *  "shipping_profile_upgrades": [
      *  { 
        *  "shipping_profile_id": 1, 
 
        *  "upgrade_id": 1, 
 
        *  "upgrade_name": "string", 
 
        *  "type": 0, 
 
        *  "rank": 0, 
 
        *  "language": "string", 
 
        *  "price": { 
          *  "amount": 0, 
 
          *  "divisor": 0, 
 
          *  "currency_code": "string" 
  }, 
 
        *  "secondary_price": { 
          *  "amount": 0, 
 
          *  "divisor": 0, 
 
          *  "currency_code": "string" 
  }, 
 
        *  "shipping_carrier_id": 0, 
 
        *  "mail_class": "string", 
 
        *  "min_delivery_days": 1, 
 
        *  "max_delivery_days": 1 
  } 
 ], 
 
    *  "origin_postal_code": "string", 
 
    *  "profile_type": "manual", 
 
    *  "domestic_handling_fee": 0, 
 
    *  "international_handling_fee": 0 
  }, 
 
  *  "user": { 
    *  "user_id": 1, 
 
    *  "primary_email": "user@example.com", 
 
    *  "first_name": "string", 
 
    *  "last_name": "string", 
 
    *  "image_url_75x75": "string" 
  }, 
 
  *  "shop": { 
    *  "shop_id": 1, 
 
    *  "user_id": 1, 
 
    *  "shop_name": "string", 
 
    *  "create_date": 0, 
 
    *  "created_timestamp": 0, 
 
    *  "title": "string", 
 
    *  "announcement": "string", 
 
    *  "currency_code": "string", 
 
    *  "is_vacation": true, 
 
    *  "vacation_message": "string", 
 
    *  "sale_message": "string", 
 
    *  "digital_sale_message": "string", 
 
    *  "update_date": 0, 
 
    *  "updated_timestamp": 0, 
 
    *  "listing_active_count": 0, 
 
    *  "digital_listing_count": 0, 
 
    *  "login_name": "string", 
 
    *  "accepts_custom_requests": true, 
 
    *  "policy_welcome": "string", 
 
    *  "policy_payment": "string", 
 
    *  "policy_shipping": "string", 
 
    *  "policy_refunds": "string", 
 
    *  "policy_additional": "string", 
 
    *  "policy_seller_info": "string", 
 
    *  "policy_update_date": 0, 
 
    *  "policy_has_private_receipt_info": true, 
 
    *  "has_unstructured_policies": true, 
 
    *  "policy_privacy": "string", 
 
    *  "vacation_autoreply": "string", 
 
    *  "url": "string", 
 
    *  "image_url_760x100": "string", 
 
    *  "num_favorers": 0, 
 
    *  "languages": [
      * "string"
 ], 
 
    *  "icon_url_fullxfull": "string", 
 
    *  "is_using_structured_policies": true, 
 
    *  "has_onboarded_structured_policies": true, 
 
    *  "include_dispute_form_link": true, 
 
    *  "is_direct_checkout_onboarded": true, 
 
    *  "is_etsy_payments_onboarded": true, 
 
    *  "is_calculated_eligible": true, 
 
    *  "is_opted_in_to_buyer_promise": true, 
 
    *  "is_shop_us_based": true, 
 
    *  "transaction_sold_count": 0, 
 
    *  "shipping_from_country_iso": "string", 
 
    *  "shop_location_country_iso": "string", 
 
    *  "review_count": 0, 
 
    *  "review_average": 0 
  }, 
 
  *  "images": [
    *  { 
      *  "listing_id": 1, 
 
      *  "listing_image_id": 1, 
 
      *  "hex_code": "string", 
 
      *  "red": 0, 
 
      *  "green": 0, 
 
      *  "blue": 0, 
 
      *  "hue": 0, 
 
      *  "saturation": 0, 
 
      *  "brightness": 0, 
 
      *  "is_black_and_white": true, 
 
      *  "creation_tsz": 0, 
 
      *  "created_timestamp": 0, 
 
      *  "rank": 0, 
 
      *  "url_75x75": "string", 
 
      *  "url_170x135": "string", 
 
      *  "url_570xN": "string", 
 
      *  "url_fullxfull": "string", 
 
      *  "full_height": 0, 
 
      *  "full_width": 0, 
 
      *  "alt_text": "string" 
  } 
 ], 
 
  *  "videos": [
    *  { 
      *  "video_id": 1, 
 
      *  "height": 0, 
 
      *  "width": 0, 
 
      *  "thumbnail_url": "string", 
 
      *  "video_url": "string", 
 
      *  "video_state": "active" 
  } 
 ], 
 
  *  "inventory": { 
    *  "products": [
      *  { 
        *  "product_id": 1, 
 
        *  "sku": "string", 
 
        *  "is_deleted": true, 
 
        *  "offerings": [
          *  { 
            *  "offering_id": 1, 
 
            *  "quantity": 0, 
 
            *  "is_enabled": true, 
 
            *  "is_deleted": true, 
 
            *  "price": { 
              *  "amount": 0, 
 
              *  "divisor": 0, 
 
              *  "currency_code": "string" 
  }, 
 
            *  "readiness_state_id": 1 
  } 
 ], 
 
        *  "property_values": [
          *  { 
            *  "property_id": 1, 
 
            *  "property_name": "string", 
 
            *  "scale_id": 1, 
 
            *  "scale_name": "string", 
 
            *  "value_ids": [
              * 1
 ], 
 
            *  "values": [
              * "string"
 ] 
  } 
 ] 
  } 
 ], 
 
    *  "price_on_property": [
      * 0
 ], 
 
    *  "quantity_on_property": [
      * 0
 ], 
 
    *  "sku_on_property": [
      * 0
 ], 
 
    *  "readiness_state_on_property": [
      * 1
 ] 
  }, 
 
  *  "production_partners": [
    *  { 
      *  "production_partner_id": 1, 
 
      *  "partner_name": "string", 
 
      *  "location": "string" 
  } 
 ], 
 
  *  "skus": [
    * "string"
 ], 
 
  *  "translations": { 
    *  "de": { 
      *  "listing_id": 1, 
 
      *  "language": "string", 
 
      *  "title": "string", 
 
      *  "description": "string", 
 
      *  "tags": [
        * "string"
 ] 
  }, 
 
    *  "en-GB": { 
      *  "listing_id": 1, 
 
      *  "language": "string", 
 
      *  "title": "string", 
 
      *  "description": "string", 
 
      *  "tags": [
        * "string"
 ] 
  }, 
 
    *  "en-IN": { 
      *  "listing_id": 1, 
 
      *  "language": "string", 
 
      *  "title": "string", 
 
      *  "description": "string", 
 
      *  "tags": [
        * "string"
 ] 
  }, 
 
    *  "en-US": { 
      *  "listing_id": 1, 
 
      *  "language": "string", 
 
      *  "title": "string", 
 
      *  "description": "string", 
 
      *  "tags": [
        * "string"
 ] 
  }, 
 
    *  "es": { 
      *  "listing_id": 1, 
 
      *  "language": "string", 
 
      *  "title": "string", 
 
      *  "description": "string", 
 
      *  "tags": [
        * "string"
 ] 
  }, 
 
    *  "fr": { 
      *  "listing_id": 1, 
 
      *  "language": "string", 
 
      *  "title": "string", 
 
      *  "description": "string", 
 
      *  "tags": [
        * "string"
 ] 
  }, 
 
    *  "it": { 
      *  "listing_id": 1, 
 
      *  "language": "string", 
 
      *  "title": "string", 
 
      *  "description": "string", 
 
      *  "tags": [
        * "string"
 ] 
  }, 
 
    *  "ja": { 
      *  "listing_id": 1, 
 
      *  "language": "string", 
 
      *  "title": "string", 
 
      *  "description": "string", 
 
      *  "tags": [
        * "string"
 ] 
  }, 
 
    *  "nl": { 
      *  "listing_id": 1, 
 
      *  "language": "string", 
 
      *  "title": "string", 
 
      *  "description": "string", 
 
      *  "tags": [
        * "string"
 ] 
  }, 
 
    *  "pl": { 
      *  "listing_id": 1, 
 
      *  "language": "string", 
 
      *  "title": "string", 
 
      *  "description": "string", 
 
      *  "tags": [
        * "string"
 ] 
  }, 
 
    *  "pt": { 
      *  "listing_id": 1, 
 
      *  "language": "string", 
 
      *  "title": "string", 
 
      *  "description": "string", 
 
      *  "tags": [
        * "string"
 ] 
  }, 
 
    *  "ru": { 
      *  "listing_id": 1, 
 
      *  "language": "string", 
 
      *  "title": "string", 
 
      *  "description": "string", 
 
      *  "tags": [
        * "string"
 ] 
  }, 
 
    *  "sv": { 
      *  "listing_id": 1, 
 
      *  "language": "string", 
 
      *  "title": "string", 
 
      *  "description": "string", 
 
      *  "tags": [
        * "string"
 ] 
  } 
  }, 
 
  *  "views": 0, 
 
  *  "personalization": {
    *  "personalization_questions": [
      *  { 
        *  "question_id": 1, 
 
        *  "question_text": "string", 
 
        *  "instructions": "string", 
 
        *  "question_type": "string", 
 
        *  "required": true, 
 
        *  "max_allowed_characters": 0, 
 
        *  "max_allowed_files": 0, 
 
        *  "add_on_price": { 
          *  "amount": 0, 
 
          *  "divisor": 0, 
 
          *  "currency_code": "string" 
  }, 
 
        *  "options": [
          *  { 
            *  "option_id": 1, 
 
            *  "label": "string" 
  } 
 ] 
  } 
 ] 
 }, 
 
  *  "buyer_price": { 
    *  "base_price": { 
      *  "amount": 0, 
 
      *  "divisor": 0, 
 
      *  "currency_code": "string" 
  }, 
 
    *  "shipping_cost": { 
      *  "amount": 0, 
 
      *  "divisor": 0, 
 
      *  "currency_code": "string" 
  }, 
 
    *  "is_free_shipping": true, 
 
    *  "original_price": { 
      *  "amount": 0, 
 
      *  "divisor": 0, 
 
      *  "currency_code": "string" 
  }, 
 
    *  "discounted_price": { 
      *  "amount": 0, 
 
      *  "divisor": 0, 
 
      *  "currency_code": "string" 
  }, 
 
    *  "discount_amount": { 
      *  "amount": 0, 
 
      *  "divisor": 0, 
 
      *  "currency_code": "string" 
  }, 
 
    *  "discount_percentage": 0, 
 
    *  "has_discount": true, 
 
    *  "discount_start_epoch": 0, 
 
    *  "discount_end_epoch": 0 
  } 
 
 }`
##  [](https://developer.etsy.com/documentation/reference/#operation/findAllListingsActive)findAllListingsActive 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
A list of all active listings on Etsy paginated by their creation date. Without sort_order listings will be returned newest-first by default.
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)
##### query Parameters  
| limit  |  integer <int64> [ 1 .. 100 ]  Default:  25 The maximum number of results to return.  |  
| --- | --- |  
| offset  |  integer <int64> >= 0  Default:  0 The number of records to skip before selecting the first result.  |  
| keywords  |  string Default:  null Search term or phrase that must appear in all results.  |  
| sort_on  |  string Default:  "created" Enum: "created" "price" "updated" "score" The value to sort a search result of listings on. NOTES: a) `sort_on` only works when combined with one of the search options (keywords, region, etc.). b) when using `score` the returned results will always be in _descending_ order, regardless of the `sort_order` parameter.  |  
| sort_order  |  string Default:  "desc" Enum: "asc" "ascending" "desc" "descending" "up" "down" The ascending(up) or descending(down) order to sort listings by. NOTE: sort_order only works when combined with one of the search options (keywords, region, etc.).  |  
| min_price  |  number <float> Default:  null The minimum price of listings to be returned by a search result.  |  
| max_price  |  number <float> Default:  null The maximum price of listings to be returned by a search result.  |  
| taxonomy_id  |  integer <int64> >= 1  Default:  null The numerical taxonomy ID of the listing. See [SellerTaxonomy](https://developer.etsy.com/documentation/reference#tag/SellerTaxonomy) and [BuyerTaxonomy](https://developer.etsy.com/documentation/reference#tag/BuyerTaxonomy) for more information.  |  
| shop_location  |  string Default:  null Filters by shop location. If location cannot be parsed, Etsy responds with an error.  |  
| is_safe  |  boolean When true, filters out mature/adult content from search results.  |  
| currency  |  string Default:  null The ISO 4217 alphabetic currency code (e.g., EUR, MXN) for price conversion. If provided, the listing price will be converted to this currency.  |  
| buyer_country  |  string <ISO 3166-1 alpha-2> Default:  null The ISO 3166-1 alpha-2 country code (e.g., DE, MX). Filters results to listings that ship to this country.  |  
### Responses
**200**
A list of all active listings on Etsy paginated by their creation date. Without sort_order listings will be returned newest-first by default.
**404**
A resource could not be found. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
get/v3/application/listings/active
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/listings/active
###  Response samples 
  * 200
  * 404
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
 
  *  "count": 0, 
 
  *  "results": [
    *  { 
      *  "listing_id": 1, 
 
      *  "user_id": 1, 
 
      *  "shop_id": 1, 
 
      *  "title": "string", 
 
      *  "description": "string", 
 
      *  "state": "active", 
 
      *  "creation_timestamp": 946684800, 
 
      *  "created_timestamp": 946684800, 
 
      *  "ending_timestamp": 946684800, 
 
      *  "original_creation_timestamp": 946684800, 
 
      *  "last_modified_timestamp": 946684800, 
 
      *  "updated_timestamp": 946684800, 
 
      *  "state_timestamp": 946684800, 
 
      *  "quantity": 0, 
 
      *  "shop_section_id": 1, 
 
      *  "featured_rank": 0, 
 
      *  "url": "string", 
 
      *  "num_favorers": 0, 
 
      *  "non_taxable": true, 
 
      *  "is_taxable": true, 
 
      *  "is_customizable": true, 
 
      *  "is_personalizable": true, 
 
      *  "listing_type": "physical", 
 
      *  "tags": [
        * "string"
 ], 
 
      *  "materials": [
        * "string"
 ], 
 
      *  "shipping_profile_id": 1, 
 
      *  "return_policy_id": 1, 
 
      *  "processing_min": 0, 
 
      *  "processing_max": 0, 
 
      *  "who_made": "i_did", 
 
      *  "when_made": "made_to_order", 
 
      *  "is_supply": true, 
 
      *  "item_weight": 0, 
 
      *  "item_weight_unit": "oz", 
 
      *  "item_length": 0, 
 
      *  "item_width": 0, 
 
      *  "item_height": 0, 
 
      *  "item_dimensions_unit": "in", 
 
      *  "is_private": true, 
 
      *  "style": [
        * "string"
 ], 
 
      *  "file_data": "string", 
 
      *  "has_variations": true, 
 
      *  "should_auto_renew": true, 
 
      *  "language": "string", 
 
      *  "price": { 
        *  "amount": 0, 
 
        *  "divisor": 0, 
 
        *  "currency_code": "string" 
  }, 
 
      *  "converted_price": { 
        *  "amount": 0, 
 
        *  "divisor": 0, 
 
        *  "currency_code": "string" 
  }, 
 
      *  "taxonomy_id": 0, 
 
      *  "readiness_state_id": 1, 
 
      *  "suggested_title": "string", 
 
      *  "ecgt_garan_brand": "string", 
 
      *  "ecgt_garan_years": 0, 
 
      *  "ecgt_garan_model": "string", 
 
      *  "ecgt_garan_guarantee_details": "string", 
 
      *  "ecgt_other_commercial_guarantee_details": "string", 
 
      *  "ecgt_after_sales_service_info": "string", 
 
      *  "ecgt_software_update_details": "string", 
 
      *  "ecgt_commercial_guarantee_enabled": true 
  } 
 ] 
 
 }`
##  [](https://developer.etsy.com/documentation/reference/#operation/findAllActiveListingsByShop)findAllActiveListingsByShop 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Retrieves a list of all active listings on Etsy in a specific shop, paginated by listing creation date.
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)
##### path Parameters  
|  shop_id required   |  integer <int64> >= 1  The unique positive non-zero numeric ID for an Etsy Shop.  |  
| --- | --- |  
##### query Parameters  
| limit  |  integer <int64> [ 1 .. 100 ]  Default:  25 The maximum number of results to return.  |  
| --- | --- |  
| sort_on  |  string Default:  "created" Enum: "created" "price" "updated" "score" The value to sort a search result of listings on. NOTES: a) `sort_on` only works when combined with one of the search options (keywords, region, etc.). b) when using `score` the returned results will always be in _descending_ order, regardless of the `sort_order` parameter.  |  
| sort_order  |  string Default:  "desc" Enum: "asc" "ascending" "desc" "descending" "up" "down" The ascending(up) or descending(down) order to sort listings by. NOTE: sort_order only works when combined with one of the search options (keywords, region, etc.).  |  
| offset  |  integer <int64> >= 0  Default:  0 The number of records to skip before selecting the first result.  |  
| keywords  |  string Default:  null Search term or phrase that must appear in all results.  |  
### Responses
**200**
Retrieves a list of all active listings on Etsy in a specific shop, paginated by listing creation date.
**400**
There was a problem with the request data. See the error message for details.
**404**
A resource could not be found. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
get/v3/application/shops/{shop_id}/listings/active
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/shops/{shop_id}/listings/active
###  Response samples 
  * 200
  * 400
  * 404
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
 
  *  "count": 0, 
 
  *  "results": [
    *  { 
      *  "listing_id": 1, 
 
      *  "user_id": 1, 
 
      *  "shop_id": 1, 
 
      *  "title": "string", 
 
      *  "description": "string", 
 
      *  "state": "active", 
 
      *  "creation_timestamp": 946684800, 
 
      *  "created_timestamp": 946684800, 
 
      *  "ending_timestamp": 946684800, 
 
      *  "original_creation_timestamp": 946684800, 
 
      *  "last_modified_timestamp": 946684800, 
 
      *  "updated_timestamp": 946684800, 
 
      *  "state_timestamp": 946684800, 
 
      *  "quantity": 0, 
 
      *  "shop_section_id": 1, 
 
      *  "featured_rank": 0, 
 
      *  "url": "string", 
 
      *  "num_favorers": 0, 
 
      *  "non_taxable": true, 
 
      *  "is_taxable": true, 
 
      *  "is_customizable": true, 
 
      *  "is_personalizable": true, 
 
      *  "listing_type": "physical", 
 
      *  "tags": [
        * "string"
 ], 
 
      *  "materials": [
        * "string"
 ], 
 
      *  "shipping_profile_id": 1, 
 
      *  "return_policy_id": 1, 
 
      *  "processing_min": 0, 
 
      *  "processing_max": 0, 
 
      *  "who_made": "i_did", 
 
      *  "when_made": "made_to_order", 
 
      *  "is_supply": true, 
 
      *  "item_weight": 0, 
 
      *  "item_weight_unit": "oz", 
 
      *  "item_length": 0, 
 
      *  "item_width": 0, 
 
      *  "item_height": 0, 
 
      *  "item_dimensions_unit": "in", 
 
      *  "is_private": true, 
 
      *  "style": [
        * "string"
 ], 
 
      *  "file_data": "string", 
 
      *  "has_variations": true, 
 
      *  "should_auto_renew": true, 
 
      *  "language": "string", 
 
      *  "price": { 
        *  "amount": 0, 
 
        *  "divisor": 0, 
 
        *  "currency_code": "string" 
  }, 
 
      *  "converted_price": { 
        *  "amount": 0, 
 
        *  "divisor": 0, 
 
        *  "currency_code": "string" 
  }, 
 
      *  "taxonomy_id": 0, 
 
      *  "readiness_state_id": 1, 
 
      *  "suggested_title": "string", 
 
      *  "ecgt_garan_brand": "string", 
 
      *  "ecgt_garan_years": 0, 
 
      *  "ecgt_garan_model": "string", 
 
      *  "ecgt_garan_guarantee_details": "string", 
 
      *  "ecgt_other_commercial_guarantee_details": "string", 
 
      *  "ecgt_after_sales_service_info": "string", 
 
      *  "ecgt_software_update_details": "string", 
 
      *  "ecgt_commercial_guarantee_enabled": true 
  } 
 ] 
 
 }`
##  [](https://developer.etsy.com/documentation/reference/#operation/getListingsByListingIds)getListingsByListingIds 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Allows to query multiple listing ids at once. Limit 100 ids maximum per query.
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)
##### query Parameters  
|  listing_ids required   |  Array of integers <int64> The list of numeric IDS for the listings in a specific Etsy shop.  |  
| --- | --- |  
| includes  |  Array of strings Default:  null Items Enum: "Images" "Shop" "User" "Translations" "Videos" "Personalization" "BuyerPrice" An enumerated string that attaches a valid association. Acceptable inputs are 'Shop', 'Images', 'User', 'Translations', 'Videos', 'Personalization' and 'BuyerPrice'.  |  
| legacy  |  boolean This parameter is needed to enable new parameters and response values related to processing profiles.  |  
| currency  |  string Default:  null The ISO 4217 alphabetic currency code (e.g., EUR, MXN) for price conversion. If provided, the listing price will be converted to this currency.  |  
| buyer_country  |  string <ISO 3166-1 alpha-2> Default:  null The ISO 3166-1 alpha-2 country code (e.g., GB, DE). Used for buyer-facing price calculations (VAT, inclusive shipping). Does not filter listings.  |  
### Responses
**200**
A list of Listings
**400**
There was a problem with the request data. See the error message for details.
**404**
A resource could not be found. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
get/v3/application/listings/batch
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/listings/batch
###  Response samples 
  * 200
  * 400
  * 404
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
 
  *  "count": 0, 
 
  *  "results": [
    *  { 
      *  "listing_id": 1, 
 
      *  "user_id": 1, 
 
      *  "shop_id": 1, 
 
      *  "title": "string", 
 
      *  "description": "string", 
 
      *  "state": "active", 
 
      *  "creation_timestamp": 946684800, 
 
      *  "created_timestamp": 946684800, 
 
      *  "ending_timestamp": 946684800, 
 
      *  "original_creation_timestamp": 946684800, 
 
      *  "last_modified_timestamp": 946684800, 
 
      *  "updated_timestamp": 946684800, 
 
      *  "state_timestamp": 946684800, 
 
      *  "quantity": 0, 
 
      *  "shop_section_id": 1, 
 
      *  "featured_rank": 0, 
 
      *  "url": "string", 
 
      *  "num_favorers": 0, 
 
      *  "non_taxable": true, 
 
      *  "is_taxable": true, 
 
      *  "is_customizable": true, 
 
      *  "is_personalizable": true, 
 
      *  "listing_type": "physical", 
 
      *  "tags": [
        * "string"
 ], 
 
      *  "materials": [
        * "string"
 ], 
 
      *  "shipping_profile_id": 1, 
 
      *  "return_policy_id": 1, 
 
      *  "processing_min": 0, 
 
      *  "processing_max": 0, 
 
      *  "who_made": "i_did", 
 
      *  "when_made": "made_to_order", 
 
      *  "is_supply": true, 
 
      *  "item_weight": 0, 
 
      *  "item_weight_unit": "oz", 
 
      *  "item_length": 0, 
 
      *  "item_width": 0, 
 
      *  "item_height": 0, 
 
      *  "item_dimensions_unit": "in", 
 
      *  "is_private": true, 
 
      *  "style": [
        * "string"
 ], 
 
      *  "file_data": "string", 
 
      *  "has_variations": true, 
 
      *  "should_auto_renew": true, 
 
      *  "language": "string", 
 
      *  "price": { 
        *  "amount": 0, 
 
        *  "divisor": 0, 
 
        *  "currency_code": "string" 
  }, 
 
      *  "converted_price": { 
        *  "amount": 0, 
 
        *  "divisor": 0, 
 
        *  "currency_code": "string" 
  }, 
 
      *  "taxonomy_id": 0, 
 
      *  "readiness_state_id": 1, 
 
      *  "suggested_title": "string", 
 
      *  "ecgt_garan_brand": "string", 
 
      *  "ecgt_garan_years": 0, 
 
      *  "ecgt_garan_model": "string", 
 
      *  "ecgt_garan_guarantee_details": "string", 
 
      *  "ecgt_other_commercial_guarantee_details": "string", 
 
      *  "ecgt_after_sales_service_info": "string", 
 
      *  "ecgt_software_update_details": "string", 
 
      *  "ecgt_commercial_guarantee_enabled": true, 
 
      *  "shipping_profile": { 
        *  "shipping_profile_id": 1, 
 
        *  "title": "string", 
 
        *  "user_id": 1, 
 
        *  "origin_country_iso": "string", 
 
        *  "is_deleted": true, 
 
        *  "shipping_profile_destinations": [
          *  { 
            *  "shipping_profile_destination_id": 1, 
 
            *  "shipping_profile_id": 1, 
 
            *  "origin_country_iso": "string", 
 
            *  "destination_country_iso": "string", 
 
            *  "destination_region": "eu", 
 
            *  "primary_cost": { 
              *  "amount": 0, 
 
              *  "divisor": 0, 
 
              *  "currency_code": "string" 
  }, 
 
            *  "secondary_cost": { 
              *  "amount": 0, 
 
              *  "divisor": 0, 
 
              *  "currency_code": "string" 
  }, 
 
            *  "shipping_carrier_id": 0, 
 
            *  "mail_class": "string", 
 
            *  "min_delivery_days": 1, 
 
            *  "max_delivery_days": 1 
  } 
 ], 
 
        *  "shipping_profile_upgrades": [
          *  { 
            *  "shipping_profile_id": 1, 
 
            *  "upgrade_id": 1, 
 
            *  "upgrade_name": "string", 
 
            *  "type": 0, 
 
            *  "rank": 0, 
 
            *  "language": "string", 
 
            *  "price": { 
              *  "amount": 0, 
 
              *  "divisor": 0, 
 
              *  "currency_code": "string" 
  }, 
 
            *  "secondary_price": { 
              *  "amount": 0, 
 
              *  "divisor": 0, 
 
              *  "currency_code": "string" 
  }, 
 
            *  "shipping_carrier_id": 0, 
 
            *  "mail_class": "string", 
 
            *  "min_delivery_days": 1, 
 
            *  "max_delivery_days": 1 
  } 
 ], 
 
        *  "origin_postal_code": "string", 
 
        *  "profile_type": "manual", 
 
        *  "domestic_handling_fee": 0, 
 
        *  "international_handling_fee": 0 
  }, 
 
      *  "user": { 
        *  "user_id": 1, 
 
        *  "primary_email": "user@example.com", 
 
        *  "first_name": "string", 
 
        *  "last_name": "string", 
 
        *  "image_url_75x75": "string" 
  }, 
 
      *  "shop": { 
        *  "shop_id": 1, 
 
        *  "user_id": 1, 
 
        *  "shop_name": "string", 
 
        *  "create_date": 0, 
 
        *  "created_timestamp": 0, 
 
        *  "title": "string", 
 
        *  "announcement": "string", 
 
        *  "currency_code": "string", 
 
        *  "is_vacation": true, 
 
        *  "vacation_message": "string", 
 
        *  "sale_message": "string", 
 
        *  "digital_sale_message": "string", 
 
        *  "update_date": 0, 
 
        *  "updated_timestamp": 0, 
 
        *  "listing_active_count": 0, 
 
        *  "digital_listing_count": 0, 
 
        *  "login_name": "string", 
 
        *  "accepts_custom_requests": true, 
 
        *  "policy_welcome": "string", 
 
        *  "policy_payment": "string", 
 
        *  "policy_shipping": "string", 
 
        *  "policy_refunds": "string", 
 
        *  "policy_additional": "string", 
 
        *  "policy_seller_info": "string", 
 
        *  "policy_update_date": 0, 
 
        *  "policy_has_private_receipt_info": true, 
 
        *  "has_unstructured_policies": true, 
 
        *  "policy_privacy": "string", 
 
        *  "vacation_autoreply": "string", 
 
        *  "url": "string", 
 
        *  "image_url_760x100": "string", 
 
        *  "num_favorers": 0, 
 
        *  "languages": [
          * "string"
 ], 
 
        *  "icon_url_fullxfull": "string", 
 
        *  "is_using_structured_policies": true, 
 
        *  "has_onboarded_structured_policies": true, 
 
        *  "include_dispute_form_link": true, 
 
        *  "is_direct_checkout_onboarded": true, 
 
        *  "is_etsy_payments_onboarded": true, 
 
        *  "is_calculated_eligible": true, 
 
        *  "is_opted_in_to_buyer_promise": true, 
 
        *  "is_shop_us_based": true, 
 
        *  "transaction_sold_count": 0, 
 
        *  "shipping_from_country_iso": "string", 
 
        *  "shop_location_country_iso": "string", 
 
        *  "review_count": 0, 
 
        *  "review_average": 0 
  }, 
 
      *  "images": [
        *  { 
          *  "listing_id": 1, 
 
          *  "listing_image_id": 1, 
 
          *  "hex_code": "string", 
 
          *  "red": 0, 
 
          *  "green": 0, 
 
          *  "blue": 0, 
 
          *  "hue": 0, 
 
          *  "saturation": 0, 
 
          *  "brightness": 0, 
 
          *  "is_black_and_white": true, 
 
          *  "creation_tsz": 0, 
 
          *  "created_timestamp": 0, 
 
          *  "rank": 0, 
 
          *  "url_75x75": "string", 
 
          *  "url_170x135": "string", 
 
          *  "url_570xN": "string", 
 
          *  "url_fullxfull": "string", 
 
          *  "full_height": 0, 
 
          *  "full_width": 0, 
 
          *  "alt_text": "string" 
  } 
 ], 
 
      *  "videos": [
        *  { 
          *  "video_id": 1, 
 
          *  "height": 0, 
 
          *  "width": 0, 
 
          *  "thumbnail_url": "string", 
 
          *  "video_url": "string", 
 
          *  "video_state": "active" 
  } 
 ], 
 
      *  "inventory": { 
        *  "products": [
          *  { 
            *  "product_id": 1, 
 
            *  "sku": "string", 
 
            *  "is_deleted": true, 
 
            *  "offerings": [
              *  { 
                *  "offering_id": 1, 
 
                *  "quantity": 0, 
 
                *  "is_enabled": true, 
 
                *  "is_deleted": true, 
 
                *  "price": { 
                  *  "amount": 0, 
 
                  *  "divisor": 0, 
 
                  *  "currency_code": "string" 
  }, 
 
                *  "readiness_state_id": 1 
  } 
 ], 
 
            *  "property_values": [
              *  { 
                *  "property_id": 1, 
 
                *  "property_name": "string", 
 
                *  "scale_id": 1, 
 
                *  "scale_name": "string", 
 
                *  "value_ids": [
                  * 1
 ], 
 
                *  "values": [
                  * "string"
 ] 
  } 
 ] 
  } 
 ], 
 
        *  "price_on_property": [
          * 0
 ], 
 
        *  "quantity_on_property": [
          * 0
 ], 
 
        *  "sku_on_property": [
          * 0
 ], 
 
        *  "readiness_state_on_property": [
          * 1
 ] 
  }, 
 
      *  "production_partners": [
        *  { 
          *  "production_partner_id": 1, 
 
          *  "partner_name": "string", 
 
          *  "location": "string" 
  } 
 ], 
 
      *  "skus": [
        * "string"
 ], 
 
      *  "translations": { 
        *  "de": { 
          *  "listing_id": 1, 
 
          *  "language": "string", 
 
          *  "title": "string", 
 
          *  "description": "string", 
 
          *  "tags": [
            * "string"
 ] 
  }, 
 
        *  "en-GB": { 
          *  "listing_id": 1, 
 
          *  "language": "string", 
 
          *  "title": "string", 
 
          *  "description": "string", 
 
          *  "tags": [
            * "string"
 ] 
  }, 
 
        *  "en-IN": { 
          *  "listing_id": 1, 
 
          *  "language": "string", 
 
          *  "title": "string", 
 
          *  "description": "string", 
 
          *  "tags": [
            * "string"
 ] 
  }, 
 
        *  "en-US": { 
          *  "listing_id": 1, 
 
          *  "language": "string", 
 
          *  "title": "string", 
 
          *  "description": "string", 
 
          *  "tags": [
            * "string"
 ] 
  }, 
 
        *  "es": { 
          *  "listing_id": 1, 
 
          *  "language": "string", 
 
          *  "title": "string", 
 
          *  "description": "string", 
 
          *  "tags": [
            * "string"
 ] 
  }, 
 
        *  "fr": { 
          *  "listing_id": 1, 
 
          *  "language": "string", 
 
          *  "title": "string", 
 
          *  "description": "string", 
 
          *  "tags": [
            * "string"
 ] 
  }, 
 
        *  "it": { 
          *  "listing_id": 1, 
 
          *  "language": "string", 
 
          *  "title": "string", 
 
          *  "description": "string", 
 
          *  "tags": [
            * "string"
 ] 
  }, 
 
        *  "ja": { 
          *  "listing_id": 1, 
 
          *  "language": "string", 
 
          *  "title": "string", 
 
          *  "description": "string", 
 
          *  "tags": [
            * "string"
 ] 
  }, 
 
        *  "nl": { 
          *  "listing_id": 1, 
 
          *  "language": "string", 
 
          *  "title": "string", 
 
          *  "description": "string", 
 
          *  "tags": [
            * "string"
 ] 
  }, 
 
        *  "pl": { 
          *  "listing_id": 1, 
 
          *  "language": "string", 
 
          *  "title": "string", 
 
          *  "description": "string", 
 
          *  "tags": [
            * "string"
 ] 
  }, 
 
        *  "pt": { 
          *  "listing_id": 1, 
 
          *  "language": "string", 
 
          *  "title": "string", 
 
          *  "description": "string", 
 
          *  "tags": [
            * "string"
 ] 
  }, 
 
        *  "ru": { 
          *  "listing_id": 1, 
 
          *  "language": "string", 
 
          *  "title": "string", 
 
          *  "description": "string", 
 
          *  "tags": [
            * "string"
 ] 
  }, 
 
        *  "sv": { 
          *  "listing_id": 1, 
 
          *  "language": "string", 
 
          *  "title": "string", 
 
          *  "description": "string", 
 
          *  "tags": [
            * "string"
 ] 
  } 
  }, 
 
      *  "views": 0, 
 
      *  "personalization": {
        *  "personalization_questions": [
          *  { 
            *  "question_id": 1, 
 
            *  "question_text": "string", 
 
            *  "instructions": "string", 
 
            *  "question_type": "string", 
 
            *  "required": true, 
 
            *  "max_allowed_characters": 0, 
 
            *  "max_allowed_files": 0, 
 
            *  "add_on_price": { 
              *  "amount": 0, 
 
              *  "divisor": 0, 
 
              *  "currency_code": "string" 
  }, 
 
            *  "options": [
              *  { 
                *  "option_id": 1, 
 
                *  "label": "string" 
  } 
 ] 
  } 
 ] 
 }, 
 
      *  "buyer_price": { 
        *  "base_price": { 
          *  "amount": 0, 
 
          *  "divisor": 0, 
 
          *  "currency_code": "string" 
  }, 
 
        *  "shipping_cost": { 
          *  "amount": 0, 
 
          *  "divisor": 0, 
 
          *  "currency_code": "string" 
  }, 
 
        *  "is_free_shipping": true, 
 
        *  "original_price": { 
          *  "amount": 0, 
 
          *  "divisor": 0, 
 
          *  "currency_code": "string" 
  }, 
 
        *  "discounted_price": { 
          *  "amount": 0, 
 
          *  "divisor": 0, 
 
          *  "currency_code": "string" 
  }, 
 
        *  "discount_amount": { 
          *  "amount": 0, 
 
          *  "divisor": 0, 
 
          *  "currency_code": "string" 
  }, 
 
        *  "discount_percentage": 0, 
 
        *  "has_discount": true, 
 
        *  "discount_start_epoch": 0, 
 
        *  "discount_end_epoch": 0 
  } 
  } 
 ] 
 
 }`
##  [](https://developer.etsy.com/documentation/reference/#operation/getFeaturedListingsByShop)getFeaturedListingsByShop 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Retrieves Listings associated to a Shop that are featured.
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)
##### path Parameters  
|  shop_id required   |  integer <int64> >= 1  The unique positive non-zero numeric ID for an Etsy Shop.  |  
| --- | --- |  
##### query Parameters  
| limit  |  integer <int64> [ 1 .. 100 ]  Default:  25 The maximum number of results to return.  |  
| --- | --- |  
| offset  |  integer <int64> >= 0  Default:  0 The number of records to skip before selecting the first result.  |  
| legacy  |  boolean This parameter is needed to enable new parameters and response values related to processing profiles.  |  
### Responses
**200**
A list of Listings
**400**
There was a problem with the request data. See the error message for details.
**403**
The request attempted to perform an operation it is not allowed to. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
get/v3/application/shops/{shop_id}/listings/featured
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/shops/{shop_id}/listings/featured
###  Response samples 
  * 200
  * 400
  * 403
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
 
  *  "count": 0, 
 
  *  "results": [
    *  { 
      *  "listing_id": 1, 
 
      *  "user_id": 1, 
 
      *  "shop_id": 1, 
 
      *  "title": "string", 
 
      *  "description": "string", 
 
      *  "state": "active", 
 
      *  "creation_timestamp": 946684800, 
 
      *  "created_timestamp": 946684800, 
 
      *  "ending_timestamp": 946684800, 
 
      *  "original_creation_timestamp": 946684800, 
 
      *  "last_modified_timestamp": 946684800, 
 
      *  "updated_timestamp": 946684800, 
 
      *  "state_timestamp": 946684800, 
 
      *  "quantity": 0, 
 
      *  "shop_section_id": 1, 
 
      *  "featured_rank": 0, 
 
      *  "url": "string", 
 
      *  "num_favorers": 0, 
 
      *  "non_taxable": true, 
 
      *  "is_taxable": true, 
 
      *  "is_customizable": true, 
 
      *  "is_personalizable": true, 
 
      *  "listing_type": "physical", 
 
      *  "tags": [
        * "string"
 ], 
 
      *  "materials": [
        * "string"
 ], 
 
      *  "shipping_profile_id": 1, 
 
      *  "return_policy_id": 1, 
 
      *  "processing_min": 0, 
 
      *  "processing_max": 0, 
 
      *  "who_made": "i_did", 
 
      *  "when_made": "made_to_order", 
 
      *  "is_supply": true, 
 
      *  "item_weight": 0, 
 
      *  "item_weight_unit": "oz", 
 
      *  "item_length": 0, 
 
      *  "item_width": 0, 
 
      *  "item_height": 0, 
 
      *  "item_dimensions_unit": "in", 
 
      *  "is_private": true, 
 
      *  "style": [
        * "string"
 ], 
 
      *  "file_data": "string", 
 
      *  "has_variations": true, 
 
      *  "should_auto_renew": true, 
 
      *  "language": "string", 
 
      *  "price": { 
        *  "amount": 0, 
 
        *  "divisor": 0, 
 
        *  "currency_code": "string" 
  }, 
 
      *  "converted_price": { 
        *  "amount": 0, 
 
        *  "divisor": 0, 
 
        *  "currency_code": "string" 
  }, 
 
      *  "taxonomy_id": 0, 
 
      *  "readiness_state_id": 1, 
 
      *  "suggested_title": "string", 
 
      *  "ecgt_garan_brand": "string", 
 
      *  "ecgt_garan_years": 0, 
 
      *  "ecgt_garan_model": "string", 
 
      *  "ecgt_garan_guarantee_details": "string", 
 
      *  "ecgt_other_commercial_guarantee_details": "string", 
 
      *  "ecgt_after_sales_service_info": "string", 
 
      *  "ecgt_software_update_details": "string", 
 
      *  "ecgt_commercial_guarantee_enabled": true 
  } 
 ] 
 
 }`
##  [](https://developer.etsy.com/documentation/reference/#operation/deleteListingProperty)deleteListingProperty 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Deletes a property for a Listing.
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)[oauth2](https://developer.etsy.com/documentation/reference/#section/Authentication/oauth2) (`listings_w`) 
##### path Parameters  
|  shop_id required   |  integer <int64> >= 1  The unique positive non-zero numeric ID for an Etsy Shop.  |  
| --- | --- |  
|  listing_id required   |  integer <int64> >= 1  The numeric ID for the [listing](https://developer.etsy.com/documentation/reference#tag/ShopListing) associated to this transaction.  |  
|  property_id required   |  integer <int64> >= 1  The unique ID of an Etsy [listing property](https://developer.etsy.com/documentation/reference#operation/getListingProperties).  |  
### Responses
**204**
The ListingProperty resource was correctly deleted
**400**
There was a problem with the request data. See the error message for details.
**401**
The request lacks valid authentication credentials. See the error message for details.
**403**
The request attempted to perform an operation it is not allowed to. See the error message for details.
**404**
A resource could not be found. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
delete/v3/application/shops/{shop_id}/listings/{listing_id}/properties/{property_id}
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/shops/{shop_id}/listings/{listing_id}/properties/{property_id}
###  Response samples 
  * 400
  * 401
  * 403
  * 404
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
  *  "error": "string" 

 }`
##  [](https://developer.etsy.com/documentation/reference/#operation/updateListingProperty)updateListingProperty 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Updates or populates the properties list defining product offerings for a listing. Each offering requires both a `value` and a `value_id` that are valid for a `scale_id` assigned to the listing or that you assign to the listing with this request.
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)[oauth2](https://developer.etsy.com/documentation/reference/#section/Authentication/oauth2) (`listings_w`) 
##### path Parameters  
|  shop_id required   |  integer <int64> >= 1  The unique positive non-zero numeric ID for an Etsy Shop.  |  
| --- | --- |  
|  listing_id required   |  integer <int64> >= 1  The numeric ID for the [listing](https://developer.etsy.com/documentation/reference#tag/ShopListing) associated to this transaction.  |  
|  property_id required   |  integer <int64> >= 1  The unique ID of an Etsy [listing property](https://developer.etsy.com/documentation/reference#operation/getListingProperties).  |  
##### Request Body schema: application/x-www-form-urlencoded  
|  value_ids required   |  Array of integers <int64> An array of unique IDs of multiple Etsy [listing property](https://developer.etsy.com/documentation/reference#operation/getListingProperties) values. For example, if your listing is composed of different materials, then the value ID list contains value IDs for each material.  |  
| --- | --- |  
|  values required   |  Array of strings An array of value strings for multiple Etsy [listing property](https://developer.etsy.com/documentation/reference#operation/getListingProperties) values. For example, if your listing is painted in different colors, then the values array contains the color strings for each color. Note: parenthesis characters (`(` and `)`) are not allowed.  |  
| scale_id  |  integer <int64> >= 1  The numeric ID of a single Etsy.com measurement scale. For example, for shoe size, there are three `scale_id`s available - `UK`, `US/Canada`, and `EU`, where `US/Canada` has `scale_id` 19.  |  
### Responses
**200**
A single listing property.
**400**
There was a problem with the request data. See the error message for details.
**401**
The request lacks valid authentication credentials. See the error message for details.
**403**
The request attempted to perform an operation it is not allowed to. See the error message for details.
**404**
A resource could not be found. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
put/v3/application/shops/{shop_id}/listings/{listing_id}/properties/{property_id}
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/shops/{shop_id}/listings/{listing_id}/properties/{property_id}
###  Response samples 
  * 200
  * 400
  * 401
  * 403
  * 404
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
 
  *  "property_id": 1, 
 
  *  "property_name": "string", 
 
  *  "scale_id": 1, 
 
  *  "scale_name": "string", 
 
  *  "value_ids": [
    * 1
 ], 
 
  *  "values": [
    * "string"
 ] 
 
 }`
##  [](https://developer.etsy.com/documentation/reference/#operation/getListingProperty)getListingProperty 
Feedback only [Give feedback](https://github.com/etsy/open-api/discussions)
Development for this endpoint is in progress. It will only return a 501 response.
Retrieves a listing's property
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)
##### path Parameters  
|  listing_id required   |  integer <int64> >= 1  The numeric ID for the [listing](https://developer.etsy.com/documentation/reference#tag/ShopListing) associated to this transaction.  |  
| --- | --- |  
|  property_id required   |  integer <int64> >= 1  The unique ID of an Etsy [listing property](https://developer.etsy.com/documentation/reference#operation/getListingProperties).  |  
### Responses
**200**
A single ListingProperty.
**400**
There was a problem with the request data. See the error message for details.
**404**
A resource could not be found. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
**501**
This endpoint is not functional at this time.
get/v3/application/listings/{listing_id}/properties/{property_id}
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/listings/{listing_id}/properties/{property_id}
###  Response samples 
  * 200
  * 400
  * 404
  * 500
  * 501


Content type
application/json
Copy
Expand all  Collapse all 
`{
 
  *  "property_id": 1, 
 
  *  "property_name": "string", 
 
  *  "scale_id": 1, 
 
  *  "scale_name": "string", 
 
  *  "value_ids": [
    * 1
 ], 
 
  *  "values": [
    * "string"
 ] 
 
 }`
##  [](https://developer.etsy.com/documentation/reference/#operation/getListingProperties)getListingProperties 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Get a listing's properties
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)
##### path Parameters  
|  shop_id required   |  integer <int64> >= 1  The unique positive non-zero numeric ID for an Etsy Shop.  |  
| --- | --- |  
|  listing_id required   |  integer <int64> >= 1  The numeric ID for the [listing](https://developer.etsy.com/documentation/reference#tag/ShopListing) associated to this transaction.  |  
### Responses
**200**
A Listing's Properties
**400**
There was a problem with the request data. See the error message for details.
**404**
A resource could not be found. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
get/v3/application/shops/{shop_id}/listings/{listing_id}/properties
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/shops/{shop_id}/listings/{listing_id}/properties
###  Response samples 
  * 200
  * 400
  * 404
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
 
  *  "count": 0, 
 
  *  "results": [
    *  { 
      *  "property_id": 1, 
 
      *  "property_name": "string", 
 
      *  "scale_id": 1, 
 
      *  "scale_name": "string", 
 
      *  "value_ids": [
        * 1
 ], 
 
      *  "values": [
        * "string"
 ] 
  } 
 ] 
 
 }`
##  [](https://developer.etsy.com/documentation/reference/#operation/getListingsShippingByListingIds)getListingsShippingByListingIds 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Retrieves the shipping profile for each listing referenced by listing ID. Requires the `shops_r` OAuth scope. Limit 100 listing IDs per request. All requested listing IDs must exist — if any single ID is not found, the entire request returns a 404. Shipping profile data (including `shipping_profile_id`) is only returned for listings owned by the authenticated user; it is nulled out for listings owned by other sellers.
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)[oauth2](https://developer.etsy.com/documentation/reference/#section/Authentication/oauth2) (`shops_r`) 
##### query Parameters  
|  listing_ids required   |  Array of integers <int64> The list of numeric IDS for the listings in a specific Etsy shop.  |  
| --- | --- |  
### Responses
**200**
A list of listings with their shipping profiles.
**400**
There was a problem with the request data. See the error message for details.
**404**
A resource could not be found. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
get/v3/application/listings/batch/shipping
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/listings/batch/shipping
###  Response samples 
  * 200
  * 400
  * 404
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
 
  *  "count": 0, 
 
  *  "results": [
    *  { 
      *  "listing_id": 1, 
 
      *  "user_id": 1, 
 
      *  "shop_id": 1, 
 
      *  "title": "string", 
 
      *  "description": "string", 
 
      *  "state": "active", 
 
      *  "creation_timestamp": 946684800, 
 
      *  "created_timestamp": 946684800, 
 
      *  "ending_timestamp": 946684800, 
 
      *  "original_creation_timestamp": 946684800, 
 
      *  "last_modified_timestamp": 946684800, 
 
      *  "updated_timestamp": 946684800, 
 
      *  "state_timestamp": 946684800, 
 
      *  "quantity": 0, 
 
      *  "shop_section_id": 1, 
 
      *  "featured_rank": 0, 
 
      *  "url": "string", 
 
      *  "num_favorers": 0, 
 
      *  "non_taxable": true, 
 
      *  "is_taxable": true, 
 
      *  "is_customizable": true, 
 
      *  "is_personalizable": true, 
 
      *  "listing_type": "physical", 
 
      *  "tags": [
        * "string"
 ], 
 
      *  "materials": [
        * "string"
 ], 
 
      *  "shipping_profile_id": 1, 
 
      *  "return_policy_id": 1, 
 
      *  "processing_min": 0, 
 
      *  "processing_max": 0, 
 
      *  "who_made": "i_did", 
 
      *  "when_made": "made_to_order", 
 
      *  "is_supply": true, 
 
      *  "item_weight": 0, 
 
      *  "item_weight_unit": "oz", 
 
      *  "item_length": 0, 
 
      *  "item_width": 0, 
 
      *  "item_height": 0, 
 
      *  "item_dimensions_unit": "in", 
 
      *  "is_private": true, 
 
      *  "style": [
        * "string"
 ], 
 
      *  "file_data": "string", 
 
      *  "has_variations": true, 
 
      *  "should_auto_renew": true, 
 
      *  "language": "string", 
 
      *  "price": { 
        *  "amount": 0, 
 
        *  "divisor": 0, 
 
        *  "currency_code": "string" 
  }, 
 
      *  "converted_price": { 
        *  "amount": 0, 
 
        *  "divisor": 0, 
 
        *  "currency_code": "string" 
  }, 
 
      *  "taxonomy_id": 0, 
 
      *  "readiness_state_id": 1, 
 
      *  "suggested_title": "string", 
 
      *  "ecgt_garan_brand": "string", 
 
      *  "ecgt_garan_years": 0, 
 
      *  "ecgt_garan_model": "string", 
 
      *  "ecgt_garan_guarantee_details": "string", 
 
      *  "ecgt_other_commercial_guarantee_details": "string", 
 
      *  "ecgt_after_sales_service_info": "string", 
 
      *  "ecgt_software_update_details": "string", 
 
      *  "ecgt_commercial_guarantee_enabled": true, 
 
      *  "shipping_profile": { 
        *  "shipping_profile_id": 1, 
 
        *  "title": "string", 
 
        *  "user_id": 1, 
 
        *  "origin_country_iso": "string", 
 
        *  "is_deleted": true, 
 
        *  "shipping_profile_destinations": [
          *  { 
            *  "shipping_profile_destination_id": 1, 
 
            *  "shipping_profile_id": 1, 
 
            *  "origin_country_iso": "string", 
 
            *  "destination_country_iso": "string", 
 
            *  "destination_region": "eu", 
 
            *  "primary_cost": { 
              *  "amount": 0, 
 
              *  "divisor": 0, 
 
              *  "currency_code": "string" 
  }, 
 
            *  "secondary_cost": { 
              *  "amount": 0, 
 
              *  "divisor": 0, 
 
              *  "currency_code": "string" 
  }, 
 
            *  "shipping_carrier_id": 0, 
 
            *  "mail_class": "string", 
 
            *  "min_delivery_days": 1, 
 
            *  "max_delivery_days": 1 
  } 
 ], 
 
        *  "shipping_profile_upgrades": [
          *  { 
            *  "shipping_profile_id": 1, 
 
            *  "upgrade_id": 1, 
 
            *  "upgrade_name": "string", 
 
            *  "type": 0, 
 
            *  "rank": 0, 
 
            *  "language": "string", 
 
            *  "price": { 
              *  "amount": 0, 
 
              *  "divisor": 0, 
 
              *  "currency_code": "string" 
  }, 
 
            *  "secondary_price": { 
              *  "amount": 0, 
 
              *  "divisor": 0, 
 
              *  "currency_code": "string" 
  }, 
 
            *  "shipping_carrier_id": 0, 
 
            *  "mail_class": "string", 
 
            *  "min_delivery_days": 1, 
 
            *  "max_delivery_days": 1 
  } 
 ], 
 
        *  "origin_postal_code": "string", 
 
        *  "profile_type": "manual", 
 
        *  "domestic_handling_fee": 0, 
 
        *  "international_handling_fee": 0 
  }, 
 
      *  "user": { 
        *  "user_id": 1, 
 
        *  "primary_email": "user@example.com", 
 
        *  "first_name": "string", 
 
        *  "last_name": "string", 
 
        *  "image_url_75x75": "string" 
  }, 
 
      *  "shop": { 
        *  "shop_id": 1, 
 
        *  "user_id": 1, 
 
        *  "shop_name": "string", 
 
        *  "create_date": 0, 
 
        *  "created_timestamp": 0, 
 
        *  "title": "string", 
 
        *  "announcement": "string", 
 
        *  "currency_code": "string", 
 
        *  "is_vacation": true, 
 
        *  "vacation_message": "string", 
 
        *  "sale_message": "string", 
 
        *  "digital_sale_message": "string", 
 
        *  "update_date": 0, 
 
        *  "updated_timestamp": 0, 
 
        *  "listing_active_count": 0, 
 
        *  "digital_listing_count": 0, 
 
        *  "login_name": "string", 
 
        *  "accepts_custom_requests": true, 
 
        *  "policy_welcome": "string", 
 
        *  "policy_payment": "string", 
 
        *  "policy_shipping": "string", 
 
        *  "policy_refunds": "string", 
 
        *  "policy_additional": "string", 
 
        *  "policy_seller_info": "string", 
 
        *  "policy_update_date": 0, 
 
        *  "policy_has_private_receipt_info": true, 
 
        *  "has_unstructured_policies": true, 
 
        *  "policy_privacy": "string", 
 
        *  "vacation_autoreply": "string", 
 
        *  "url": "string", 
 
        *  "image_url_760x100": "string", 
 
        *  "num_favorers": 0, 
 
        *  "languages": [
          * "string"
 ], 
 
        *  "icon_url_fullxfull": "string", 
 
        *  "is_using_structured_policies": true, 
 
        *  "has_onboarded_structured_policies": true, 
 
        *  "include_dispute_form_link": true, 
 
        *  "is_direct_checkout_onboarded": true, 
 
        *  "is_etsy_payments_onboarded": true, 
 
        *  "is_calculated_eligible": true, 
 
        *  "is_opted_in_to_buyer_promise": true, 
 
        *  "is_shop_us_based": true, 
 
        *  "transaction_sold_count": 0, 
 
        *  "shipping_from_country_iso": "string", 
 
        *  "shop_location_country_iso": "string", 
 
        *  "review_count": 0, 
 
        *  "review_average": 0 
  }, 
 
      *  "images": [
        *  { 
          *  "listing_id": 1, 
 
          *  "listing_image_id": 1, 
 
          *  "hex_code": "string", 
 
          *  "red": 0, 
 
          *  "green": 0, 
 
          *  "blue": 0, 
 
          *  "hue": 0, 
 
          *  "saturation": 0, 
 
          *  "brightness": 0, 
 
          *  "is_black_and_white": true, 
 
          *  "creation_tsz": 0, 
 
          *  "created_timestamp": 0, 
 
          *  "rank": 0, 
 
          *  "url_75x75": "string", 
 
          *  "url_170x135": "string", 
 
          *  "url_570xN": "string", 
 
          *  "url_fullxfull": "string", 
 
          *  "full_height": 0, 
 
          *  "full_width": 0, 
 
          *  "alt_text": "string" 
  } 
 ], 
 
      *  "videos": [
        *  { 
          *  "video_id": 1, 
 
          *  "height": 0, 
 
          *  "width": 0, 
 
          *  "thumbnail_url": "string", 
 
          *  "video_url": "string", 
 
          *  "video_state": "active" 
  } 
 ], 
 
      *  "inventory": { 
        *  "products": [
          *  { 
            *  "product_id": 1, 
 
            *  "sku": "string", 
 
            *  "is_deleted": true, 
 
            *  "offerings": [
              *  { 
                *  "offering_id": 1, 
 
                *  "quantity": 0, 
 
                *  "is_enabled": true, 
 
                *  "is_deleted": true, 
 
                *  "price": { 
                  *  "amount": 0, 
 
                  *  "divisor": 0, 
 
                  *  "currency_code": "string" 
  }, 
 
                *  "readiness_state_id": 1 
  } 
 ], 
 
            *  "property_values": [
              *  { 
                *  "property_id": 1, 
 
                *  "property_name": "string", 
 
                *  "scale_id": 1, 
 
                *  "scale_name": "string", 
 
                *  "value_ids": [
                  * 1
 ], 
 
                *  "values": [
                  * "string"
 ] 
  } 
 ] 
  } 
 ], 
 
        *  "price_on_property": [
          * 0
 ], 
 
        *  "quantity_on_property": [
          * 0
 ], 
 
        *  "sku_on_property": [
          * 0
 ], 
 
        *  "readiness_state_on_property": [
          * 1
 ] 
  }, 
 
      *  "production_partners": [
        *  { 
          *  "production_partner_id": 1, 
 
          *  "partner_name": "string", 
 
          *  "location": "string" 
  } 
 ], 
 
      *  "skus": [
        * "string"
 ], 
 
      *  "translations": { 
        *  "de": { 
          *  "listing_id": 1, 
 
          *  "language": "string", 
 
          *  "title": "string", 
 
          *  "description": "string", 
 
          *  "tags": [
            * "string"
 ] 
  }, 
 
        *  "en-GB": { 
          *  "listing_id": 1, 
 
          *  "language": "string", 
 
          *  "title": "string", 
 
          *  "description": "string", 
 
          *  "tags": [
            * "string"
 ] 
  }, 
 
        *  "en-IN": { 
          *  "listing_id": 1, 
 
          *  "language": "string", 
 
          *  "title": "string", 
 
          *  "description": "string", 
 
          *  "tags": [
            * "string"
 ] 
  }, 
 
        *  "en-US": { 
          *  "listing_id": 1, 
 
          *  "language": "string", 
 
          *  "title": "string", 
 
          *  "description": "string", 
 
          *  "tags": [
            * "string"
 ] 
  }, 
 
        *  "es": { 
          *  "listing_id": 1, 
 
          *  "language": "string", 
 
          *  "title": "string", 
 
          *  "description": "string", 
 
          *  "tags": [
            * "string"
 ] 
  }, 
 
        *  "fr": { 
          *  "listing_id": 1, 
 
          *  "language": "string", 
 
          *  "title": "string", 
 
          *  "description": "string", 
 
          *  "tags": [
            * "string"
 ] 
  }, 
 
        *  "it": { 
          *  "listing_id": 1, 
 
          *  "language": "string", 
 
          *  "title": "string", 
 
          *  "description": "string", 
 
          *  "tags": [
            * "string"
 ] 
  }, 
 
        *  "ja": { 
          *  "listing_id": 1, 
 
          *  "language": "string", 
 
          *  "title": "string", 
 
          *  "description": "string", 
 
          *  "tags": [
            * "string"
 ] 
  }, 
 
        *  "nl": { 
          *  "listing_id": 1, 
 
          *  "language": "string", 
 
          *  "title": "string", 
 
          *  "description": "string", 
 
          *  "tags": [
            * "string"
 ] 
  }, 
 
        *  "pl": { 
          *  "listing_id": 1, 
 
          *  "language": "string", 
 
          *  "title": "string", 
 
          *  "description": "string", 
 
          *  "tags": [
            * "string"
 ] 
  }, 
 
        *  "pt": { 
          *  "listing_id": 1, 
 
          *  "language": "string", 
 
          *  "title": "string", 
 
          *  "description": "string", 
 
          *  "tags": [
            * "string"
 ] 
  }, 
 
        *  "ru": { 
          *  "listing_id": 1, 
 
          *  "language": "string", 
 
          *  "title": "string", 
 
          *  "description": "string", 
 
          *  "tags": [
            * "string"
 ] 
  }, 
 
        *  "sv": { 
          *  "listing_id": 1, 
 
          *  "language": "string", 
 
          *  "title": "string", 
 
          *  "description": "string", 
 
          *  "tags": [
            * "string"
 ] 
  } 
  }, 
 
      *  "views": 0, 
 
      *  "personalization": {
        *  "personalization_questions": [
          *  { 
            *  "question_id": 1, 
 
            *  "question_text": "string", 
 
            *  "instructions": "string", 
 
            *  "question_type": "string", 
 
            *  "required": true, 
 
            *  "max_allowed_characters": 0, 
 
            *  "max_allowed_files": 0, 
 
            *  "add_on_price": { 
              *  "amount": 0, 
 
              *  "divisor": 0, 
 
              *  "currency_code": "string" 
  }, 
 
            *  "options": [
              *  { 
                *  "option_id": 1, 
 
                *  "label": "string" 
  } 
 ] 
  } 
 ] 
 }, 
 
      *  "buyer_price": { 
        *  "base_price": { 
          *  "amount": 0, 
 
          *  "divisor": 0, 
 
          *  "currency_code": "string" 
  }, 
 
        *  "shipping_cost": { 
          *  "amount": 0, 
 
          *  "divisor": 0, 
 
          *  "currency_code": "string" 
  }, 
 
        *  "is_free_shipping": true, 
 
        *  "original_price": { 
          *  "amount": 0, 
 
          *  "divisor": 0, 
 
          *  "currency_code": "string" 
  }, 
 
        *  "discounted_price": { 
          *  "amount": 0, 
 
          *  "divisor": 0, 
 
          *  "currency_code": "string" 
  }, 
 
        *  "discount_amount": { 
          *  "amount": 0, 
 
          *  "divisor": 0, 
 
          *  "currency_code": "string" 
  }, 
 
        *  "discount_percentage": 0, 
 
        *  "has_discount": true, 
 
        *  "discount_start_epoch": 0, 
 
        *  "discount_end_epoch": 0 
  } 
  } 
 ] 
 
 }`
##  [](https://developer.etsy.com/documentation/reference/#operation/updateListing)updateListing 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Updates a listing, identified by a listing ID, for a specific shop identified by a shop ID. Note that this is a PATCH method type. When activating, or manually renewing a physical listing, the shipping profile referenced by the `shipping_profile_id`, and all of its fields, along with its entries and upgrades must be complete and valid. If the shipping profile is not complete and valid, we will throw an exception with an error message that guides the request sender to update whatever data is bad. Digital listings that are not made to order must have a file upload associated with it to be activated. While the listing is a draft, shipping profile and file upload are not required in any case.
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)[oauth2](https://developer.etsy.com/documentation/reference/#section/Authentication/oauth2) (`listings_w`) 
##### path Parameters  
|  shop_id required   |  integer <int64> >= 1  The unique positive non-zero numeric ID for an Etsy Shop.  |  
| --- | --- |  
|  listing_id required   |  integer <int64> >= 1  The numeric ID for the [listing](https://developer.etsy.com/documentation/reference#tag/ShopListing) associated to this transaction.  |  
##### Request Body schema: application/x-www-form-urlencoded  
| image_ids  |  Array of integers <int64> An array of numeric image IDs of the images in a listing, which can include up to 20 images.  |  
| --- | --- |  
| title  |  string The listing's title string. When creating or updating a listing, valid title strings contain only letters, numbers, punctuation marks, mathematical symbols, whitespace characters, ™, ©, and ®. (regex: /[^\p{L}\p{Nd}\p{P}\p{Sm}\p{Zs}™©®]/u) You can only use the %, :, & and + characters once each.  |  
| description  |  string A description string of the product for sale in the listing.  |  
| materials  |  Array of strings Nullable  A list of material strings for materials used in the product. Valid materials strings contain only letters, numbers, and whitespace characters. (regex: /[^\p{L}\p{Nd}\p{Zs}]/u) Default value is null.  |  
| should_auto_renew  |  boolean When true, renews a listing for four months upon expiration.  |  
| shipping_profile_id  |  integer <int64> >= 1  Nullable  The numeric ID of the [shipping profile](https://developer.etsy.com/documentation/reference#operation/getShopShippingProfile) associated with the listing. Required when listing type is `physical`.  |  
| return_policy_id  |  integer <int64> >= 1  Nullable  The numeric ID of the [Return Policy](https://developer.etsy.com/documentation/reference#operation/getShopReturnPolicies). Required for active physical listings. This requirement does not apply to listings of EU-based shops.  |  
| shop_section_id  |  integer <int64> Nullable  The numeric ID of the [shop section](https://developer.etsy.com/documentation/reference#tag/Shop-Section) for this listing. Default value is null.  |  
| item_weight  |  number <float> [ 0 .. 1.79769313486e+308 ]  Nullable  The numeric weight of the product measured in units set in 'item_weight_unit'. Default value is null. If set, the value must be greater than 0.  |  
| item_length  |  number <float> [ 0 .. 1.79769313486e+308 ]  Nullable  The numeric length of the product measured in units set in 'item_dimensions_unit'. Default value is null. If set, the value must be greater than 0.  |  
| item_width  |  number <float> [ 0 .. 1.79769313486e+308 ]  Nullable  The numeric width of the product measured in units set in 'item_dimensions_unit'. Default value is null. If set, the value must be greater than 0.  |  
| item_height  |  number <float> [ 0 .. 1.79769313486e+308 ]  Nullable  The numeric height of the product measured in units set in 'item_dimensions_unit'. Default value is null. If set, the value must be greater than 0.  |  
| item_weight_unit  |  string Nullable  Enum: "" "oz" "lb" "g" "kg" A string defining the units used to measure the weight of the product. Default value is null.  |  
| item_dimensions_unit  |  string Nullable  Enum: "" "in" "ft" "mm" "cm" "m" "yd" "inches" A string defining the units used to measure the dimensions of the product. Default value is null.  |  
| is_taxable  |  boolean When true, applicable [shop](https://developer.etsy.com/documentation/reference#tag/Shop) tax rates apply to this listing at checkout.  |  
| taxonomy_id  |  integer <int64> >= 1  The numerical taxonomy ID of the listing. See [SellerTaxonomy](https://developer.etsy.com/documentation/reference#tag/SellerTaxonomy) and [BuyerTaxonomy](https://developer.etsy.com/documentation/reference#tag/BuyerTaxonomy) for more information.  |  
| tags  |  Array of strings Nullable  A comma-separated list of tag strings for the listing. When creating or updating a listing, valid tag strings contain only letters, numbers, whitespace characters, -, ', ™, ©, and ®. (regex: /[^\p{L}\p{Nd}\p{Zs}-'™©®]/u) Default value is null.  |  
| who_made  |  string Enum: "i_did" "someone_else" "collective" An enumerated string indicating who made the product. Helps buyers locate the listing under the Handmade heading. Requires 'is_supply' and 'when_made'.  |  
| when_made  |  string Enum: "made_to_order" "2020_2026" "2010_2019" "2007_2009" "before_2007" "2000_2006" "1990s" "1980s" "1970s" "1960s" "1950s" "1940s" "1930s" "1920s" "1910s" "1900s" "1800s" "1700s" "before_1700" An enumerated string for the era in which the maker made the product in this listing. Helps buyers locate the listing under the Vintage heading. Requires 'is_supply' and 'who_made'.  |  
| state  |  string Enum: "active" "inactive" When _updating_ a listing, this value can be either `active` or `inactive`. Note: Setting a `draft` listing to `active` will also publish the listing on etsy.com and requires that the listing have an image set. Setting a `sold_out` listing to active will update the quantity to 1 and renew the listing on etsy.com.  |  
| is_supply  |  boolean When true, tags the listing as a supply product, else indicates that it's a finished product. Helps buyers locate the listing under the Supplies heading. Requires 'who_made' and 'when_made'.  |  
| production_partner_ids  |  Array of integers <int64> Nullable  An array of unique IDs of production partner ids.  |  
| type  |  string Nullable  Enum: "physical" "download" "both" An enumerated type string that indicates whether the listing is physical or a digital download.  |  
| ecgt_garan_brand  |  string Nullable  The brand or trademark name for the EU commercial guarantee (required under GPSR/ECGT for eligible EU traders). Maximum 25 characters. See the [Etsy Seller Handbook](https://help.etsy.com/hc/articles/43191692248343) for details. If any one of ecgt_garan_brand, ecgt_garan_model, ecgt_garan_years, or ecgt_garan_guarantee_details is provided and non-empty, all four are required. Silently ignored for digital listings and for sellers who are not eligible EU traders.  |  
| ecgt_garan_years  |  integer <int64> Nullable  Duration of the EU commercial guarantee in whole years (minimum 3, maximum 99). Required together with ecgt_garan_brand, ecgt_garan_model, and ecgt_garan_guarantee_details. Silently ignored for digital listings and for sellers who are not eligible EU traders.  |  
| ecgt_garan_model  |  string Nullable  The product model or reference number for the EU commercial guarantee label. Maximum 20 characters. Required together with ecgt_garan_brand, ecgt_garan_years, and ecgt_garan_guarantee_details. Silently ignored for digital listings and for sellers who are not eligible EU traders.  |  
| ecgt_garan_guarantee_details  |  string Nullable  Free-text description of the EU commercial guarantee terms and coverage. Maximum 255 characters. Required together with ecgt_garan_brand, ecgt_garan_model, and ecgt_garan_years. Silently ignored for digital listings and for sellers who are not eligible EU traders.  |  
| ecgt_other_commercial_guarantee_details  |  string Nullable  Free-text details of any additional commercial guarantee or warranty beyond the primary EU commercial guarantee. Maximum 255 characters. Silently ignored for digital listings and for sellers who are not eligible EU traders.  |  
| ecgt_after_sales_service_info  |  string Nullable  After-sales service, repairability, or eco-friendly delivery information required under EU GPSR/ECGT regulations. Maximum 255 characters. Silently ignored for digital listings and for sellers who are not eligible EU traders.  |  
| ecgt_software_update_details  |  string Nullable  Details of software update availability and the duration of such updates, as required under EU ECGT regulations for digital content. Maximum 255 characters. Silently ignored for physical listings and for sellers who are not eligible EU traders.  |  
### Responses
**200**
A single ShopListing
**400**
There was a problem with the request data. See the error message for details.
**401**
The request lacks valid authentication credentials. See the error message for details.
**403**
The request attempted to perform an operation it is not allowed to. See the error message for details.
**404**
A resource could not be found. See the error message for details.
**409**
There was a request conflict with the current state of the target resource. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
patch/v3/application/shops/{shop_id}/listings/{listing_id}
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/shops/{shop_id}/listings/{listing_id}
###  Response samples 
  * 200
  * 400
  * 401
  * 403
  * 404
  * 409
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
 
  *  "listing_id": 1, 
 
  *  "user_id": 1, 
 
  *  "shop_id": 1, 
 
  *  "title": "string", 
 
  *  "description": "string", 
 
  *  "state": "active", 
 
  *  "creation_timestamp": 946684800, 
 
  *  "created_timestamp": 946684800, 
 
  *  "ending_timestamp": 946684800, 
 
  *  "original_creation_timestamp": 946684800, 
 
  *  "last_modified_timestamp": 946684800, 
 
  *  "updated_timestamp": 946684800, 
 
  *  "state_timestamp": 946684800, 
 
  *  "quantity": 0, 
 
  *  "shop_section_id": 1, 
 
  *  "featured_rank": 0, 
 
  *  "url": "string", 
 
  *  "num_favorers": 0, 
 
  *  "non_taxable": true, 
 
  *  "is_taxable": true, 
 
  *  "is_customizable": true, 
 
  *  "is_personalizable": true, 
 
  *  "listing_type": "physical", 
 
  *  "tags": [
    * "string"
 ], 
 
  *  "materials": [
    * "string"
 ], 
 
  *  "shipping_profile_id": 1, 
 
  *  "return_policy_id": 1, 
 
  *  "processing_min": 0, 
 
  *  "processing_max": 0, 
 
  *  "who_made": "i_did", 
 
  *  "when_made": "made_to_order", 
 
  *  "is_supply": true, 
 
  *  "item_weight": 0, 
 
  *  "item_weight_unit": "oz", 
 
  *  "item_length": 0, 
 
  *  "item_width": 0, 
 
  *  "item_height": 0, 
 
  *  "item_dimensions_unit": "in", 
 
  *  "is_private": true, 
 
  *  "style": [
    * "string"
 ], 
 
  *  "file_data": "string", 
 
  *  "has_variations": true, 
 
  *  "should_auto_renew": true, 
 
  *  "language": "string", 
 
  *  "price": { 
    *  "amount": 0, 
 
    *  "divisor": 0, 
 
    *  "currency_code": "string" 
  }, 
 
  *  "converted_price": { 
    *  "amount": 0, 
 
    *  "divisor": 0, 
 
    *  "currency_code": "string" 
  }, 
 
  *  "taxonomy_id": 0, 
 
  *  "readiness_state_id": 1, 
 
  *  "suggested_title": "string", 
 
  *  "ecgt_garan_brand": "string", 
 
  *  "ecgt_garan_years": 0, 
 
  *  "ecgt_garan_model": "string", 
 
  *  "ecgt_garan_guarantee_details": "string", 
 
  *  "ecgt_other_commercial_guarantee_details": "string", 
 
  *  "ecgt_after_sales_service_info": "string", 
 
  *  "ecgt_software_update_details": "string", 
 
  *  "ecgt_commercial_guarantee_enabled": true 
 
 }`
##  [](https://developer.etsy.com/documentation/reference/#operation/getListingsByShopReceipt)getListingsByShopReceipt 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Gets all listings associated with a receipt.
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)[oauth2](https://developer.etsy.com/documentation/reference/#section/Authentication/oauth2) (`transactions_r`) 
##### path Parameters  
|  receipt_id required   |  integer <int64> >= 1  The numeric ID for the [receipt](https://developer.etsy.com/documentation/reference#tag/Shop-Receipt) associated to this transaction.  |  
| --- | --- |  
|  shop_id required   |  integer <int64> >= 1  The unique positive non-zero numeric ID for an Etsy Shop.  |  
##### query Parameters  
| limit  |  integer <int64> [ 1 .. 100 ]  Default:  25 The maximum number of results to return.  |  
| --- | --- |  
| offset  |  integer <int64> >= 0  Default:  0 The number of records to skip before selecting the first result.  |  
| legacy  |  boolean This parameter is needed to enable new parameters and response values related to processing profiles.  |  
### Responses
**200**
A set of ShopListing resources.
**400**
There was a problem with the request data. See the error message for details.
**401**
The request lacks valid authentication credentials. See the error message for details.
**403**
The request attempted to perform an operation it is not allowed to. See the error message for details.
**404**
A resource could not be found. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
get/v3/application/shops/{shop_id}/receipts/{receipt_id}/listings
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/shops/{shop_id}/receipts/{receipt_id}/listings
###  Response samples 
  * 200
  * 400
  * 401
  * 403
  * 404
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
 
  *  "count": 0, 
 
  *  "results": [
    *  { 
      *  "listing_id": 1, 
 
      *  "user_id": 1, 
 
      *  "shop_id": 1, 
 
      *  "title": "string", 
 
      *  "description": "string", 
 
      *  "state": "active", 
 
      *  "creation_timestamp": 946684800, 
 
      *  "created_timestamp": 946684800, 
 
      *  "ending_timestamp": 946684800, 
 
      *  "original_creation_timestamp": 946684800, 
 
      *  "last_modified_timestamp": 946684800, 
 
      *  "updated_timestamp": 946684800, 
 
      *  "state_timestamp": 946684800, 
 
      *  "quantity": 0, 
 
      *  "shop_section_id": 1, 
 
      *  "featured_rank": 0, 
 
      *  "url": "string", 
 
      *  "num_favorers": 0, 
 
      *  "non_taxable": true, 
 
      *  "is_taxable": true, 
 
      *  "is_customizable": true, 
 
      *  "is_personalizable": true, 
 
      *  "listing_type": "physical", 
 
      *  "tags": [
        * "string"
 ], 
 
      *  "materials": [
        * "string"
 ], 
 
      *  "shipping_profile_id": 1, 
 
      *  "return_policy_id": 1, 
 
      *  "processing_min": 0, 
 
      *  "processing_max": 0, 
 
      *  "who_made": "i_did", 
 
      *  "when_made": "made_to_order", 
 
      *  "is_supply": true, 
 
      *  "item_weight": 0, 
 
      *  "item_weight_unit": "oz", 
 
      *  "item_length": 0, 
 
      *  "item_width": 0, 
 
      *  "item_height": 0, 
 
      *  "item_dimensions_unit": "in", 
 
      *  "is_private": true, 
 
      *  "style": [
        * "string"
 ], 
 
      *  "file_data": "string", 
 
      *  "has_variations": true, 
 
      *  "should_auto_renew": true, 
 
      *  "language": "string", 
 
      *  "price": { 
        *  "amount": 0, 
 
        *  "divisor": 0, 
 
        *  "currency_code": "string" 
  }, 
 
      *  "converted_price": { 
        *  "amount": 0, 
 
        *  "divisor": 0, 
 
        *  "currency_code": "string" 
  }, 
 
      *  "taxonomy_id": 0, 
 
      *  "readiness_state_id": 1, 
 
      *  "suggested_title": "string", 
 
      *  "ecgt_garan_brand": "string", 
 
      *  "ecgt_garan_years": 0, 
 
      *  "ecgt_garan_model": "string", 
 
      *  "ecgt_garan_guarantee_details": "string", 
 
      *  "ecgt_other_commercial_guarantee_details": "string", 
 
      *  "ecgt_after_sales_service_info": "string", 
 
      *  "ecgt_software_update_details": "string", 
 
      *  "ecgt_commercial_guarantee_enabled": true 
  } 
 ] 
 
 }`
##  [](https://developer.etsy.com/documentation/reference/#operation/getListingsByShopReturnPolicy)getListingsByShopReturnPolicy 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Gets all listings associated with a Return Policy.
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)[oauth2](https://developer.etsy.com/documentation/reference/#section/Authentication/oauth2) (`listings_r`) 
##### path Parameters  
|  return_policy_id required   |  integer <int64> >= 1  The numeric ID of the [Return Policy](https://developer.etsy.com/documentation/reference#operation/getShopReturnPolicies).  |  
| --- | --- |  
|  shop_id required   |  integer <int64> >= 1  The unique positive non-zero numeric ID for an Etsy Shop.  |  
##### query Parameters  
| legacy  |  boolean This parameter is needed to enable new parameters and response values related to processing profiles.  |  
| --- | --- |  
### Responses
**200**
A set of ShopListing resources.
**400**
There was a problem with the request data. See the error message for details.
**401**
The request lacks valid authentication credentials. See the error message for details.
**403**
The request attempted to perform an operation it is not allowed to. See the error message for details.
**404**
A resource could not be found. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
get/v3/application/shops/{shop_id}/policies/return/{return_policy_id}/listings
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/shops/{shop_id}/policies/return/{return_policy_id}/listings
###  Response samples 
  * 200
  * 400
  * 401
  * 403
  * 404
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
 
  *  "count": 0, 
 
  *  "results": [
    *  { 
      *  "listing_id": 1, 
 
      *  "user_id": 1, 
 
      *  "shop_id": 1, 
 
      *  "title": "string", 
 
      *  "description": "string", 
 
      *  "state": "active", 
 
      *  "creation_timestamp": 946684800, 
 
      *  "created_timestamp": 946684800, 
 
      *  "ending_timestamp": 946684800, 
 
      *  "original_creation_timestamp": 946684800, 
 
      *  "last_modified_timestamp": 946684800, 
 
      *  "updated_timestamp": 946684800, 
 
      *  "state_timestamp": 946684800, 
 
      *  "quantity": 0, 
 
      *  "shop_section_id": 1, 
 
      *  "featured_rank": 0, 
 
      *  "url": "string", 
 
      *  "num_favorers": 0, 
 
      *  "non_taxable": true, 
 
      *  "is_taxable": true, 
 
      *  "is_customizable": true, 
 
      *  "is_personalizable": true, 
 
      *  "listing_type": "physical", 
 
      *  "tags": [
        * "string"
 ], 
 
      *  "materials": [
        * "string"
 ], 
 
      *  "shipping_profile_id": 1, 
 
      *  "return_policy_id": 1, 
 
      *  "processing_min": 0, 
 
      *  "processing_max": 0, 
 
      *  "who_made": "i_did", 
 
      *  "when_made": "made_to_order", 
 
      *  "is_supply": true, 
 
      *  "item_weight": 0, 
 
      *  "item_weight_unit": "oz", 
 
      *  "item_length": 0, 
 
      *  "item_width": 0, 
 
      *  "item_height": 0, 
 
      *  "item_dimensions_unit": "in", 
 
      *  "is_private": true, 
 
      *  "style": [
        * "string"
 ], 
 
      *  "file_data": "string", 
 
      *  "has_variations": true, 
 
      *  "should_auto_renew": true, 
 
      *  "language": "string", 
 
      *  "price": { 
        *  "amount": 0, 
 
        *  "divisor": 0, 
 
        *  "currency_code": "string" 
  }, 
 
      *  "converted_price": { 
        *  "amount": 0, 
 
        *  "divisor": 0, 
 
        *  "currency_code": "string" 
  }, 
 
      *  "taxonomy_id": 0, 
 
      *  "readiness_state_id": 1, 
 
      *  "suggested_title": "string", 
 
      *  "ecgt_garan_brand": "string", 
 
      *  "ecgt_garan_years": 0, 
 
      *  "ecgt_garan_model": "string", 
 
      *  "ecgt_garan_guarantee_details": "string", 
 
      *  "ecgt_other_commercial_guarantee_details": "string", 
 
      *  "ecgt_after_sales_service_info": "string", 
 
      *  "ecgt_software_update_details": "string", 
 
      *  "ecgt_commercial_guarantee_enabled": true 
  } 
 ] 
 
 }`
##  [](https://developer.etsy.com/documentation/reference/#operation/getListingsByShopSectionId)getListingsByShopSectionId 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Retrieves all the listings from the section of a specific shop.
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)
##### path Parameters  
|  shop_id required   |  integer <int64> >= 1  The unique positive non-zero numeric ID for an Etsy Shop.  |  
| --- | --- |  
##### query Parameters  
|  shop_section_ids required   |  Array of integers <int64> A list of numeric IDS for all sections in a specific Etsy shop.  |  
| --- | --- |  
| limit  |  integer <int64> [ 1 .. 100 ]  Default:  25 The maximum number of results to return.  |  
| offset  |  integer <int64> >= 0  Default:  0 The number of records to skip before selecting the first result.  |  
| sort_on  |  string Default:  "created" Enum: "created" "price" "updated" "score" The value to sort a search result of listings on. NOTES: a) `sort_on` only works when combined with one of the search options (keywords, region, etc.). b) when using `score` the returned results will always be in _descending_ order, regardless of the `sort_order` parameter.  |  
| sort_order  |  string Default:  "desc" Enum: "asc" "ascending" "desc" "descending" "up" "down" The ascending(up) or descending(down) order to sort listings by. NOTE: sort_order only works when combined with one of the search options (keywords, region, etc.).  |  
| legacy  |  boolean This parameter is needed to enable new parameters and response values related to processing profiles.  |  
### Responses
**200**
A list of listings from a shop section.
**400**
There was a problem with the request data. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
get/v3/application/shops/{shop_id}/shop-sections/listings
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/shops/{shop_id}/shop-sections/listings
###  Response samples 
  * 200
  * 400
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
 
  *  "count": 0, 
 
  *  "results": [
    *  { 
      *  "listing_id": 1, 
 
      *  "user_id": 1, 
 
      *  "shop_id": 1, 
 
      *  "title": "string", 
 
      *  "description": "string", 
 
      *  "state": "active", 
 
      *  "creation_timestamp": 946684800, 
 
      *  "created_timestamp": 946684800, 
 
      *  "ending_timestamp": 946684800, 
 
      *  "original_creation_timestamp": 946684800, 
 
      *  "last_modified_timestamp": 946684800, 
 
      *  "updated_timestamp": 946684800, 
 
      *  "state_timestamp": 946684800, 
 
      *  "quantity": 0, 
 
      *  "shop_section_id": 1, 
 
      *  "featured_rank": 0, 
 
      *  "url": "string", 
 
      *  "num_favorers": 0, 
 
      *  "non_taxable": true, 
 
      *  "is_taxable": true, 
 
      *  "is_customizable": true, 
 
      *  "is_personalizable": true, 
 
      *  "listing_type": "physical", 
 
      *  "tags": [
        * "string"
 ], 
 
      *  "materials": [
        * "string"
 ], 
 
      *  "shipping_profile_id": 1, 
 
      *  "return_policy_id": 1, 
 
      *  "processing_min": 0, 
 
      *  "processing_max": 0, 
 
      *  "who_made": "i_did", 
 
      *  "when_made": "made_to_order", 
 
      *  "is_supply": true, 
 
      *  "item_weight": 0, 
 
      *  "item_weight_unit": "oz", 
 
      *  "item_length": 0, 
 
      *  "item_width": 0, 
 
      *  "item_height": 0, 
 
      *  "item_dimensions_unit": "in", 
 
      *  "is_private": true, 
 
      *  "style": [
        * "string"
 ], 
 
      *  "file_data": "string", 
 
      *  "has_variations": true, 
 
      *  "should_auto_renew": true, 
 
      *  "language": "string", 
 
      *  "price": { 
        *  "amount": 0, 
 
        *  "divisor": 0, 
 
        *  "currency_code": "string" 
  }, 
 
      *  "converted_price": { 
        *  "amount": 0, 
 
        *  "divisor": 0, 
 
        *  "currency_code": "string" 
  }, 
 
      *  "taxonomy_id": 0, 
 
      *  "readiness_state_id": 1, 
 
      *  "suggested_title": "string", 
 
      *  "ecgt_garan_brand": "string", 
 
      *  "ecgt_garan_years": 0, 
 
      *  "ecgt_garan_model": "string", 
 
      *  "ecgt_garan_guarantee_details": "string", 
 
      *  "ecgt_other_commercial_guarantee_details": "string", 
 
      *  "ecgt_after_sales_service_info": "string", 
 
      *  "ecgt_software_update_details": "string", 
 
      *  "ecgt_commercial_guarantee_enabled": true 
  } 
 ] 
 
 }`
#  [](https://developer.etsy.com/documentation/reference/#tag/ShopListing-File)ShopListing File
##  [](https://developer.etsy.com/documentation/reference/#operation/deleteListingFile)deleteListingFile 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Deletes a file from a specific listing. When you delete the final file for a digital listing, the listing converts into a physical listing. The response to a delete request returns a list of the remaining file records associated with the given listing.
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)[oauth2](https://developer.etsy.com/documentation/reference/#section/Authentication/oauth2) (`listings_w`) 
##### path Parameters  
|  shop_id required   |  integer <int64> >= 1  The unique positive non-zero numeric ID for an Etsy Shop.  |  
| --- | --- |  
|  listing_id required   |  integer <int64> >= 1  The numeric ID for the [listing](https://developer.etsy.com/documentation/reference#tag/ShopListing) associated to this transaction.  |  
|  listing_file_id required   |  integer <int64> >= 1  The unique numeric ID of a file associated with a digital listing.  |  
### Responses
**204**
The ShopListingFile resource was correctly deleted
**400**
There was a problem with the request data. See the error message for details.
**401**
The request lacks valid authentication credentials. See the error message for details.
**403**
The request attempted to perform an operation it is not allowed to. See the error message for details.
**404**
A resource could not be found. See the error message for details.
**409**
There was a request conflict with the current state of the target resource. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
delete/v3/application/shops/{shop_id}/listings/{listing_id}/files/{listing_file_id}
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/shops/{shop_id}/listings/{listing_id}/files/{listing_file_id}
###  Response samples 
  * 400
  * 401
  * 403
  * 404
  * 409
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
  *  "error": "string" 

 }`
##  [](https://developer.etsy.com/documentation/reference/#operation/getListingFile)getListingFile 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Retrieves a single file associated with the given digital listing. Requesting a file from a physical listing returns an empty result.
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)[oauth2](https://developer.etsy.com/documentation/reference/#section/Authentication/oauth2) (`listings_r`) 
##### path Parameters  
|  shop_id required   |  integer <int64> >= 1  The unique positive non-zero numeric ID for an Etsy Shop.  |  
| --- | --- |  
|  listing_id required   |  integer <int64> >= 1  The numeric ID for the [listing](https://developer.etsy.com/documentation/reference#tag/ShopListing) associated to this transaction.  |  
|  listing_file_id required   |  integer <int64> >= 1  The unique numeric ID of a file associated with a digital listing.  |  
### Responses
**200**
The metadata for a file associated with a digital listing.
**400**
There was a problem with the request data. See the error message for details.
**401**
The request lacks valid authentication credentials. See the error message for details.
**403**
The request attempted to perform an operation it is not allowed to. See the error message for details.
**404**
A resource could not be found. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
get/v3/application/shops/{shop_id}/listings/{listing_id}/files/{listing_file_id}
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/shops/{shop_id}/listings/{listing_id}/files/{listing_file_id}
###  Response samples 
  * 200
  * 400
  * 401
  * 403
  * 404
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
 
  *  "listing_file_id": 1, 
 
  *  "listing_id": 1, 
 
  *  "rank": 0, 
 
  *  "filename": "string", 
 
  *  "filesize": "string", 
 
  *  "size_bytes": 0, 
 
  *  "filetype": "string", 
 
  *  "create_timestamp": 946684800, 
 
  *  "created_timestamp": 946684800 
 
 }`
##  [](https://developer.etsy.com/documentation/reference/#operation/getAllListingFiles)getAllListingFiles 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Retrieves all the files associated with the given digital listing. Requesting files from a physical listing returns an empty result.
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)[oauth2](https://developer.etsy.com/documentation/reference/#section/Authentication/oauth2) (`listings_r`) 
##### path Parameters  
|  listing_id required   |  integer <int64> >= 1  The numeric ID for the [listing](https://developer.etsy.com/documentation/reference#tag/ShopListing) associated to this transaction.  |  
| --- | --- |  
|  shop_id required   |  integer <int64> >= 1  The unique positive non-zero numeric ID for an Etsy Shop.  |  
### Responses
**200**
A list of metadata objects for the file resources associated with a listing.
**400**
There was a problem with the request data. See the error message for details.
**401**
The request lacks valid authentication credentials. See the error message for details.
**404**
A resource could not be found. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
get/v3/application/shops/{shop_id}/listings/{listing_id}/files
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/shops/{shop_id}/listings/{listing_id}/files
###  Response samples 
  * 200
  * 400
  * 401
  * 404
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
 
  *  "count": 0, 
 
  *  "results": [
    *  { 
      *  "listing_file_id": 1, 
 
      *  "listing_id": 1, 
 
      *  "rank": 0, 
 
      *  "filename": "string", 
 
      *  "filesize": "string", 
 
      *  "size_bytes": 0, 
 
      *  "filetype": "string", 
 
      *  "create_timestamp": 946684800, 
 
      *  "created_timestamp": 946684800 
  } 
 ] 
 
 }`
##  [](https://developer.etsy.com/documentation/reference/#operation/uploadListingFile)uploadListingFile 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Uploads a new file for a digital listing, or associates an existing file with a specific listing. You must either provide the `listing_file_id` of an existing file, or the name and binary file data for a file to upload. Associating an existing file to a physical listing converts the physical listing into a digital listing, which removes all shipping costs and any product and inventory variations.
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)[oauth2](https://developer.etsy.com/documentation/reference/#section/Authentication/oauth2) (`listings_w`) 
##### path Parameters  
|  shop_id required   |  integer <int64> >= 1  The unique positive non-zero numeric ID for an Etsy Shop.  |  
| --- | --- |  
|  listing_id required   |  integer <int64> >= 1  The numeric ID for the [listing](https://developer.etsy.com/documentation/reference#tag/ShopListing) associated to this transaction.  |  
##### Request Body schema: multipart/form-data  
| listing_file_id  |  integer <int64> >= 1  The unique numeric ID of a file associated with a digital listing.  |  
| --- | --- |  
| file  |  string <binary> Nullable  A binary file to upload.  |  
| name  |  string The file name string of a file to upload  |  
| rank  |  integer <int64> >= 1  Default:  1 The positive non-zero numeric position in the images displayed in a listing, with rank 1 images appearing in the left-most position in a listing.  |  
### Responses
**201**
The metadata for a file associated with a digital listing.
**400**
There was a problem with the request data. See the error message for details.
**401**
The request lacks valid authentication credentials. See the error message for details.
**403**
The request attempted to perform an operation it is not allowed to. See the error message for details.
**404**
A resource could not be found. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
post/v3/application/shops/{shop_id}/listings/{listing_id}/files
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/shops/{shop_id}/listings/{listing_id}/files
###  Response samples 
  * 201
  * 400
  * 401
  * 403
  * 404
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
 
  *  "listing_file_id": 1, 
 
  *  "listing_id": 1, 
 
  *  "rank": 0, 
 
  *  "filename": "string", 
 
  *  "filesize": "string", 
 
  *  "size_bytes": 0, 
 
  *  "filetype": "string", 
 
  *  "create_timestamp": 946684800, 
 
  *  "created_timestamp": 946684800 
 
 }`
#  [](https://developer.etsy.com/documentation/reference/#tag/ShopListing-Image)ShopListing Image
##  [](https://developer.etsy.com/documentation/reference/#operation/deleteListingImage)deleteListingImage 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Open API V3 endpoint to delete a listing image. A copy of the file remains on our servers, and so a deleted image may be re-associated with the listing without re-uploading the original image; see uploadListingImage.
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)[oauth2](https://developer.etsy.com/documentation/reference/#section/Authentication/oauth2) (`listings_w`) 
##### path Parameters  
|  shop_id required   |  integer <int64> >= 1  The unique positive non-zero numeric ID for an Etsy Shop.  |  
| --- | --- |  
|  listing_id required   |  integer <int64> >= 1  The numeric ID for the [listing](https://developer.etsy.com/documentation/reference#tag/ShopListing) associated to this transaction.  |  
|  listing_image_id required   |  integer <int64> >= 1  The numeric ID of the primary [listing image](https://developer.etsy.com/documentation/reference#tag/ShopListing-Image) for this transaction.  |  
### Responses
**204**
The ListingImage resource was correctly deleted
**400**
There was a problem with the request data. See the error message for details.
**401**
The request lacks valid authentication credentials. See the error message for details.
**403**
The request attempted to perform an operation it is not allowed to. See the error message for details.
**404**
A resource could not be found. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
delete/v3/application/shops/{shop_id}/listings/{listing_id}/images/{listing_image_id}
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/shops/{shop_id}/listings/{listing_id}/images/{listing_image_id}
###  Response samples 
  * 400
  * 401
  * 403
  * 404
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
  *  "error": "string" 

 }`
##  [](https://developer.etsy.com/documentation/reference/#operation/getListingImage)getListingImage 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Retrieves the references and metadata for a listing image with a specific image ID.
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)
##### path Parameters  
|  listing_id required   |  integer <int64> >= 1  The numeric ID for the [listing](https://developer.etsy.com/documentation/reference#tag/ShopListing) associated to this transaction.  |  
| --- | --- |  
|  listing_image_id required   |  integer <int64> >= 1  The numeric ID of the primary [listing image](https://developer.etsy.com/documentation/reference#tag/ShopListing-Image) for this transaction.  |  
### Responses
**200**
A single ListingImage
**400**
There was a problem with the request data. See the error message for details.
**403**
The request attempted to perform an operation it is not allowed to. See the error message for details.
**404**
A resource could not be found. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
get/v3/application/listings/{listing_id}/images/{listing_image_id}
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/listings/{listing_id}/images/{listing_image_id}
###  Response samples 
  * 200
  * 400
  * 403
  * 404
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
 
  *  "listing_id": 1, 
 
  *  "listing_image_id": 1, 
 
  *  "hex_code": "string", 
 
  *  "red": 0, 
 
  *  "green": 0, 
 
  *  "blue": 0, 
 
  *  "hue": 0, 
 
  *  "saturation": 0, 
 
  *  "brightness": 0, 
 
  *  "is_black_and_white": true, 
 
  *  "creation_tsz": 0, 
 
  *  "created_timestamp": 0, 
 
  *  "rank": 0, 
 
  *  "url_75x75": "string", 
 
  *  "url_170x135": "string", 
 
  *  "url_570xN": "string", 
 
  *  "url_fullxfull": "string", 
 
  *  "full_height": 0, 
 
  *  "full_width": 0, 
 
  *  "alt_text": "string" 
 
 }`
##  [](https://developer.etsy.com/documentation/reference/#operation/getListingImages)getListingImages 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Retrieves all listing image resources for a listing with a specific listing ID.
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)
##### path Parameters  
|  listing_id required   |  integer <int64> >= 1  The numeric ID for the [listing](https://developer.etsy.com/documentation/reference#tag/ShopListing) associated to this transaction.  |  
| --- | --- |  
### Responses
**200**
An array of ListingImage
**400**
There was a problem with the request data. See the error message for details.
**403**
The request attempted to perform an operation it is not allowed to. See the error message for details.
**404**
A resource could not be found. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
get/v3/application/listings/{listing_id}/images
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/listings/{listing_id}/images
###  Response samples 
  * 200
  * 400
  * 403
  * 404
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
 
  *  "count": 0, 
 
  *  "results": [
    *  { 
      *  "listing_id": 1, 
 
      *  "listing_image_id": 1, 
 
      *  "hex_code": "string", 
 
      *  "red": 0, 
 
      *  "green": 0, 
 
      *  "blue": 0, 
 
      *  "hue": 0, 
 
      *  "saturation": 0, 
 
      *  "brightness": 0, 
 
      *  "is_black_and_white": true, 
 
      *  "creation_tsz": 0, 
 
      *  "created_timestamp": 0, 
 
      *  "rank": 0, 
 
      *  "url_75x75": "string", 
 
      *  "url_170x135": "string", 
 
      *  "url_570xN": "string", 
 
      *  "url_fullxfull": "string", 
 
      *  "full_height": 0, 
 
      *  "full_width": 0, 
 
      *  "alt_text": "string" 
  } 
 ] 
 
 }`
##  [](https://developer.etsy.com/documentation/reference/#operation/uploadListingImage)uploadListingImage 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Uploads or assigns an image to a listing identified by a shop ID with a listing ID. To upload a new image, set the image file as the value for the `image` parameter. You can assign a previously deleted image to a listing using the deleted image's image ID in the `listing_image_id` parameter. When a request contains both `image` and `listing_image_id` parameter values, the endpoint uploads the image in the `image` parameter only. Note: When uploading a new image, data such as colors and size may return as null values due to asynchronous processing of the image. Use getListingImage endpoint to fetch these values.
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)[oauth2](https://developer.etsy.com/documentation/reference/#section/Authentication/oauth2) (`listings_w`) 
##### path Parameters  
|  shop_id required   |  integer <int64> >= 1  The unique positive non-zero numeric ID for an Etsy Shop.  |  
| --- | --- |  
|  listing_id required   |  integer <int64> >= 1  The numeric ID for the [listing](https://developer.etsy.com/documentation/reference#tag/ShopListing) associated to this transaction.  |  
##### Request Body schema: multipart/form-data  
| image  |  string <binary> Nullable  The file name string of a file to upload  |  
| --- | --- |  
| listing_image_id  |  integer <int64> >= 1  The numeric ID of the primary [listing image](https://developer.etsy.com/documentation/reference#tag/ShopListing-Image) for this transaction.  |  
| rank  |  integer <int64> >= 0  Default:  1 The positive non-zero numeric position in the images displayed in a listing, with rank 1 images appearing in the left-most position in a listing.  |  
| overwrite  |  boolean Default:  false When true, this request replaces the existing image at a given rank.  |  
| is_watermarked  |  boolean Default:  false When true, indicates that the uploaded image has a watermark.  |  
| alt_text  |  string Default:  "" Alt text for the listing image. Max length 500 characters.  |  
### Responses
**201**
A single ListingImage
**400**
There was a problem with the request data. See the error message for details.
**401**
The request lacks valid authentication credentials. See the error message for details.
**403**
The request attempted to perform an operation it is not allowed to. See the error message for details.
**404**
A resource could not be found. See the error message for details.
**409**
There was a request conflict with the current state of the target resource. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
post/v3/application/shops/{shop_id}/listings/{listing_id}/images
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/shops/{shop_id}/listings/{listing_id}/images
###  Response samples 
  * 201
  * 400
  * 401
  * 403
  * 404
  * 409
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
 
  *  "listing_id": 1, 
 
  *  "listing_image_id": 1, 
 
  *  "hex_code": "string", 
 
  *  "red": 0, 
 
  *  "green": 0, 
 
  *  "blue": 0, 
 
  *  "hue": 0, 
 
  *  "saturation": 0, 
 
  *  "brightness": 0, 
 
  *  "is_black_and_white": true, 
 
  *  "creation_tsz": 0, 
 
  *  "created_timestamp": 0, 
 
  *  "rank": 0, 
 
  *  "url_75x75": "string", 
 
  *  "url_170x135": "string", 
 
  *  "url_570xN": "string", 
 
  *  "url_fullxfull": "string", 
 
  *  "full_height": 0, 
 
  *  "full_width": 0, 
 
  *  "alt_text": "string" 
 
 }`
#  [](https://developer.etsy.com/documentation/reference/#tag/ShopListing-Inventory)ShopListing Inventory
##  [](https://developer.etsy.com/documentation/reference/#operation/getListingInventory)getListingInventory 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Retrieves the inventory record for a listing. Listings you did not edit using the Etsy.com inventory tools have no inventory records. This endpoint returns SKU data if you are the owner of the inventory records being fetched.
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)[oauth2](https://developer.etsy.com/documentation/reference/#section/Authentication/oauth2) (`listings_r`) 
##### path Parameters  
|  listing_id required   |  integer <int64> >= 1  The numeric ID for the [listing](https://developer.etsy.com/documentation/reference#tag/ShopListing) associated to this transaction.  |  
| --- | --- |  
##### query Parameters  
| show_deleted  |  boolean A boolean value for inventory whether to include deleted products and their offerings. Default value is false.  |  
| --- | --- |  
| includes  |  string Value: "Listing" An enumerated string that attaches a valid association. Default value is null.  |  
### Responses
**200**
A single listing inventory record.
**400**
There was a problem with the request data. See the error message for details.
**401**
The request lacks valid authentication credentials. See the error message for details.
**404**
A resource could not be found. See the error message for details.
**422**
There was a problem processing your request. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
get/v3/application/listings/{listing_id}/inventory
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/listings/{listing_id}/inventory
###  Response samples 
  * 200
  * 400
  * 401
  * 404
  * 422
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
 
  *  "products": [
    *  { 
      *  "product_id": 1, 
 
      *  "sku": "string", 
 
      *  "is_deleted": true, 
 
      *  "offerings": [
        *  { 
          *  "offering_id": 1, 
 
          *  "quantity": 0, 
 
          *  "is_enabled": true, 
 
          *  "is_deleted": true, 
 
          *  "price": { 
            *  "amount": 0, 
 
            *  "divisor": 0, 
 
            *  "currency_code": "string" 
  }, 
 
          *  "readiness_state_id": 1 
  } 
 ], 
 
      *  "property_values": [
        *  { 
          *  "property_id": 1, 
 
          *  "property_name": "string", 
 
          *  "scale_id": 1, 
 
          *  "scale_name": "string", 
 
          *  "value_ids": [
            * 1
 ], 
 
          *  "values": [
            * "string"
 ] 
  } 
 ] 
  } 
 ], 
 
  *  "price_on_property": [
    * 0
 ], 
 
  *  "quantity_on_property": [
    * 0
 ], 
 
  *  "sku_on_property": [
    * 0
 ], 
 
  *  "readiness_state_on_property": [
    * 1
 ], 
 
  *  "listing": { 
    *  "listing_id": 1, 
 
    *  "user_id": 1, 
 
    *  "shop_id": 1, 
 
    *  "title": "string", 
 
    *  "description": "string", 
 
    *  "state": "active", 
 
    *  "creation_timestamp": 946684800, 
 
    *  "created_timestamp": 946684800, 
 
    *  "ending_timestamp": 946684800, 
 
    *  "original_creation_timestamp": 946684800, 
 
    *  "last_modified_timestamp": 946684800, 
 
    *  "updated_timestamp": 946684800, 
 
    *  "state_timestamp": 946684800, 
 
    *  "quantity": 0, 
 
    *  "shop_section_id": 1, 
 
    *  "featured_rank": 0, 
 
    *  "url": "string", 
 
    *  "num_favorers": 0, 
 
    *  "non_taxable": true, 
 
    *  "is_taxable": true, 
 
    *  "is_customizable": true, 
 
    *  "is_personalizable": true, 
 
    *  "listing_type": "physical", 
 
    *  "tags": [
      * "string"
 ], 
 
    *  "materials": [
      * "string"
 ], 
 
    *  "shipping_profile_id": 1, 
 
    *  "return_policy_id": 1, 
 
    *  "processing_min": 0, 
 
    *  "processing_max": 0, 
 
    *  "who_made": "i_did", 
 
    *  "when_made": "made_to_order", 
 
    *  "is_supply": true, 
 
    *  "item_weight": 0, 
 
    *  "item_weight_unit": "oz", 
 
    *  "item_length": 0, 
 
    *  "item_width": 0, 
 
    *  "item_height": 0, 
 
    *  "item_dimensions_unit": "in", 
 
    *  "is_private": true, 
 
    *  "style": [
      * "string"
 ], 
 
    *  "file_data": "string", 
 
    *  "has_variations": true, 
 
    *  "should_auto_renew": true, 
 
    *  "language": "string", 
 
    *  "price": { 
      *  "amount": 0, 
 
      *  "divisor": 0, 
 
      *  "currency_code": "string" 
  }, 
 
    *  "converted_price": { 
      *  "amount": 0, 
 
      *  "divisor": 0, 
 
      *  "currency_code": "string" 
  }, 
 
    *  "taxonomy_id": 0, 
 
    *  "readiness_state_id": 1, 
 
    *  "suggested_title": "string", 
 
    *  "ecgt_garan_brand": "string", 
 
    *  "ecgt_garan_years": 0, 
 
    *  "ecgt_garan_model": "string", 
 
    *  "ecgt_garan_guarantee_details": "string", 
 
    *  "ecgt_other_commercial_guarantee_details": "string", 
 
    *  "ecgt_after_sales_service_info": "string", 
 
    *  "ecgt_software_update_details": "string", 
 
    *  "ecgt_commercial_guarantee_enabled": true 
  } 
 
 }`
##  [](https://developer.etsy.com/documentation/reference/#operation/updateListingInventory)updateListingInventory 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Updates the inventory for a listing identified by a listing ID. The update fails if the supplied values for product sku, offering quantity, price, and/or processing profile are incompatible with values in `*_on_property` fields. When setting a price, assign a float equal to amount divided by divisor as specified in the Money resource.
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)[oauth2](https://developer.etsy.com/documentation/reference/#section/Authentication/oauth2) (`listings_w`) 
##### path Parameters  
|  listing_id required   |  integer <int64> >= 1  The numeric ID for the [listing](https://developer.etsy.com/documentation/reference#tag/ShopListing) associated to this transaction.  |  
| --- | --- |  
##### query Parameters  
| max_variations_supported  |  string Enum: "2" "3" This parameter determines whether a third variation can be added to or updated for a listing. It accepts values of 2 or 3, where 3 enables third-variation support.  |  
| --- | --- |  
| enable_scale_validation  |  boolean This temporary parameter indicates whether scale validation should be enabled for the request. It will be removed in the near future, at which point scale validation will be mandatory for all requests.  |  
##### Request Body schema: application/json  
|  products required   |  Array of objects A JSON array of products available in a listing, even if only one product. All field names in the JSON blobs are lowercase.  |  
| --- | --- |  
| price_on_property  |  Array of integers <int64> An array of unique [listing property](https://developer.etsy.com/documentation/reference#operation/getListingInventory) ID integers for the properties that change product prices, if any. For example, if you charge specific prices for different sized products in the same listing, then this array contains the property ID for size.  |  
| quantity_on_property  |  Array of integers <int64> An array of unique [listing property](https://developer.etsy.com/documentation/reference#operation/getListingInventory) ID integers for the properties that change the quantity of the products, if any. For example, if you stock specific quantities of different colored products in the same listing, then this array contains the property ID for color.  |  
| sku_on_property  |  Array of integers <int64> An array of unique [listing property](https://developer.etsy.com/documentation/reference#operation/getListingInventory) ID integers for the properties that change the product SKU, if any. For example, if you use specific skus for different colored products in the same listing, then this array contains the property ID for color.  |  
| readiness_state_on_property  |  Array of integers <int64> Nullable  An array of unique [listing property](https://developer.etsy.com/documentation/reference#operation/getListingInventory) ID integers for the properties that change processing profile, if any. For example, if you need specific processing profiles for different colored products in the same listing, then this array contains the property ID for color.  |  
### Responses
**200**
A single listing's inventory record.
**400**
There was a problem with the request data. See the error message for details.
**401**
The request lacks valid authentication credentials. See the error message for details.
**403**
The request attempted to perform an operation it is not allowed to. See the error message for details.
**404**
A resource could not be found. See the error message for details.
**409**
There was a request conflict with the current state of the target resource. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
put/v3/application/listings/{listing_id}/inventory
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/listings/{listing_id}/inventory
###  Request samples 
  * Payload


Content type
application/json
Copy
Expand all  Collapse all 
`{
 
  *  "products": [
    *  { 
      *  "sku": "string", 
 
      *  "property_values": [
        *  { 
          *  "property_id": 1, 
 
          *  "value_ids": [
            * 1
 ], 
 
          *  "scale_id": 1, 
 
          *  "property_name": "string", 
 
          *  "values": [
            * "string"
 ] 
  } 
 ], 
 
      *  "offerings": [
        *  { 
          *  "price": 0, 
 
          *  "quantity": 0, 
 
          *  "is_enabled": true, 
 
          *  "readiness_state_id": 1 
  } 
 ] 
  } 
 ], 
 
  *  "price_on_property": [
    * 0
 ], 
 
  *  "quantity_on_property": [
    * 0
 ], 
 
  *  "sku_on_property": [
    * 0
 ], 
 
  *  "readiness_state_on_property": [
    * 1
 ] 
 
 }`
###  Response samples 
  * 200
  * 400
  * 401
  * 403
  * 404
  * 409
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
 
  *  "products": [
    *  { 
      *  "product_id": 1, 
 
      *  "sku": "string", 
 
      *  "is_deleted": true, 
 
      *  "offerings": [
        *  { 
          *  "offering_id": 1, 
 
          *  "quantity": 0, 
 
          *  "is_enabled": true, 
 
          *  "is_deleted": true, 
 
          *  "price": { 
            *  "amount": 0, 
 
            *  "divisor": 0, 
 
            *  "currency_code": "string" 
  }, 
 
          *  "readiness_state_id": 1 
  } 
 ], 
 
      *  "property_values": [
        *  { 
          *  "property_id": 1, 
 
          *  "property_name": "string", 
 
          *  "scale_id": 1, 
 
          *  "scale_name": "string", 
 
          *  "value_ids": [
            * 1
 ], 
 
          *  "values": [
            * "string"
 ] 
  } 
 ] 
  } 
 ], 
 
  *  "price_on_property": [
    * 0
 ], 
 
  *  "quantity_on_property": [
    * 0
 ], 
 
  *  "sku_on_property": [
    * 0
 ], 
 
  *  "readiness_state_on_property": [
    * 1
 ] 
 
 }`
##  [](https://developer.etsy.com/documentation/reference/#operation/getListingsInventoryByListingIds)getListingsInventoryByListingIds 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Retrieves the inventory record for each listing referenced by listing ID. Requires the `listings_r` OAuth scope. Limit 100 listing IDs per request. All requested listing IDs must exist — if any single ID is not found, the entire request returns a 404. SKUs within product records are only returned for listings owned by the authenticated user; they are stripped (returned as empty string) for listings owned by other sellers.
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)[oauth2](https://developer.etsy.com/documentation/reference/#section/Authentication/oauth2) (`listings_r`) 
##### query Parameters  
|  listing_ids required   |  Array of integers <int64> The list of numeric IDS for the listings in a specific Etsy shop.  |  
| --- | --- |  
### Responses
**200**
A list of listings with their inventory records.
**400**
There was a problem with the request data. See the error message for details.
**404**
A resource could not be found. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
get/v3/application/listings/batch/inventory
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/listings/batch/inventory
###  Response samples 
  * 200
  * 400
  * 404
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
 
  *  "count": 0, 
 
  *  "results": [
    *  { 
      *  "listing_id": 1, 
 
      *  "user_id": 1, 
 
      *  "shop_id": 1, 
 
      *  "title": "string", 
 
      *  "description": "string", 
 
      *  "state": "active", 
 
      *  "creation_timestamp": 946684800, 
 
      *  "created_timestamp": 946684800, 
 
      *  "ending_timestamp": 946684800, 
 
      *  "original_creation_timestamp": 946684800, 
 
      *  "last_modified_timestamp": 946684800, 
 
      *  "updated_timestamp": 946684800, 
 
      *  "state_timestamp": 946684800, 
 
      *  "quantity": 0, 
 
      *  "shop_section_id": 1, 
 
      *  "featured_rank": 0, 
 
      *  "url": "string", 
 
      *  "num_favorers": 0, 
 
      *  "non_taxable": true, 
 
      *  "is_taxable": true, 
 
      *  "is_customizable": true, 
 
      *  "is_personalizable": true, 
 
      *  "listing_type": "physical", 
 
      *  "tags": [
        * "string"
 ], 
 
      *  "materials": [
        * "string"
 ], 
 
      *  "shipping_profile_id": 1, 
 
      *  "return_policy_id": 1, 
 
      *  "processing_min": 0, 
 
      *  "processing_max": 0, 
 
      *  "who_made": "i_did", 
 
      *  "when_made": "made_to_order", 
 
      *  "is_supply": true, 
 
      *  "item_weight": 0, 
 
      *  "item_weight_unit": "oz", 
 
      *  "item_length": 0, 
 
      *  "item_width": 0, 
 
      *  "item_height": 0, 
 
      *  "item_dimensions_unit": "in", 
 
      *  "is_private": true, 
 
      *  "style": [
        * "string"
 ], 
 
      *  "file_data": "string", 
 
      *  "has_variations": true, 
 
      *  "should_auto_renew": true, 
 
      *  "language": "string", 
 
      *  "price": { 
        *  "amount": 0, 
 
        *  "divisor": 0, 
 
        *  "currency_code": "string" 
  }, 
 
      *  "converted_price": { 
        *  "amount": 0, 
 
        *  "divisor": 0, 
 
        *  "currency_code": "string" 
  }, 
 
      *  "taxonomy_id": 0, 
 
      *  "readiness_state_id": 1, 
 
      *  "suggested_title": "string", 
 
      *  "ecgt_garan_brand": "string", 
 
      *  "ecgt_garan_years": 0, 
 
      *  "ecgt_garan_model": "string", 
 
      *  "ecgt_garan_guarantee_details": "string", 
 
      *  "ecgt_other_commercial_guarantee_details": "string", 
 
      *  "ecgt_after_sales_service_info": "string", 
 
      *  "ecgt_software_update_details": "string", 
 
      *  "ecgt_commercial_guarantee_enabled": true, 
 
      *  "shipping_profile": { 
        *  "shipping_profile_id": 1, 
 
        *  "title": "string", 
 
        *  "user_id": 1, 
 
        *  "origin_country_iso": "string", 
 
        *  "is_deleted": true, 
 
        *  "shipping_profile_destinations": [
          *  { 
            *  "shipping_profile_destination_id": 1, 
 
            *  "shipping_profile_id": 1, 
 
            *  "origin_country_iso": "string", 
 
            *  "destination_country_iso": "string", 
 
            *  "destination_region": "eu", 
 
            *  "primary_cost": { 
              *  "amount": 0, 
 
              *  "divisor": 0, 
 
              *  "currency_code": "string" 
  }, 
 
            *  "secondary_cost": { 
              *  "amount": 0, 
 
              *  "divisor": 0, 
 
              *  "currency_code": "string" 
  }, 
 
            *  "shipping_carrier_id": 0, 
 
            *  "mail_class": "string", 
 
            *  "min_delivery_days": 1, 
 
            *  "max_delivery_days": 1 
  } 
 ], 
 
        *  "shipping_profile_upgrades": [
          *  { 
            *  "shipping_profile_id": 1, 
 
            *  "upgrade_id": 1, 
 
            *  "upgrade_name": "string", 
 
            *  "type": 0, 
 
            *  "rank": 0, 
 
            *  "language": "string", 
 
            *  "price": { 
              *  "amount": 0, 
 
              *  "divisor": 0, 
 
              *  "currency_code": "string" 
  }, 
 
            *  "secondary_price": { 
              *  "amount": 0, 
 
              *  "divisor": 0, 
 
              *  "currency_code": "string" 
  }, 
 
            *  "shipping_carrier_id": 0, 
 
            *  "mail_class": "string", 
 
            *  "min_delivery_days": 1, 
 
            *  "max_delivery_days": 1 
  } 
 ], 
 
        *  "origin_postal_code": "string", 
 
        *  "profile_type": "manual", 
 
        *  "domestic_handling_fee": 0, 
 
        *  "international_handling_fee": 0 
  }, 
 
      *  "user": { 
        *  "user_id": 1, 
 
        *  "primary_email": "user@example.com", 
 
        *  "first_name": "string", 
 
        *  "last_name": "string", 
 
        *  "image_url_75x75": "string" 
  }, 
 
      *  "shop": { 
        *  "shop_id": 1, 
 
        *  "user_id": 1, 
 
        *  "shop_name": "string", 
 
        *  "create_date": 0, 
 
        *  "created_timestamp": 0, 
 
        *  "title": "string", 
 
        *  "announcement": "string", 
 
        *  "currency_code": "string", 
 
        *  "is_vacation": true, 
 
        *  "vacation_message": "string", 
 
        *  "sale_message": "string", 
 
        *  "digital_sale_message": "string", 
 
        *  "update_date": 0, 
 
        *  "updated_timestamp": 0, 
 
        *  "listing_active_count": 0, 
 
        *  "digital_listing_count": 0, 
 
        *  "login_name": "string", 
 
        *  "accepts_custom_requests": true, 
 
        *  "policy_welcome": "string", 
 
        *  "policy_payment": "string", 
 
        *  "policy_shipping": "string", 
 
        *  "policy_refunds": "string", 
 
        *  "policy_additional": "string", 
 
        *  "policy_seller_info": "string", 
 
        *  "policy_update_date": 0, 
 
        *  "policy_has_private_receipt_info": true, 
 
        *  "has_unstructured_policies": true, 
 
        *  "policy_privacy": "string", 
 
        *  "vacation_autoreply": "string", 
 
        *  "url": "string", 
 
        *  "image_url_760x100": "string", 
 
        *  "num_favorers": 0, 
 
        *  "languages": [
          * "string"
 ], 
 
        *  "icon_url_fullxfull": "string", 
 
        *  "is_using_structured_policies": true, 
 
        *  "has_onboarded_structured_policies": true, 
 
        *  "include_dispute_form_link": true, 
 
        *  "is_direct_checkout_onboarded": true, 
 
        *  "is_etsy_payments_onboarded": true, 
 
        *  "is_calculated_eligible": true, 
 
        *  "is_opted_in_to_buyer_promise": true, 
 
        *  "is_shop_us_based": true, 
 
        *  "transaction_sold_count": 0, 
 
        *  "shipping_from_country_iso": "string", 
 
        *  "shop_location_country_iso": "string", 
 
        *  "review_count": 0, 
 
        *  "review_average": 0 
  }, 
 
      *  "images": [
        *  { 
          *  "listing_id": 1, 
 
          *  "listing_image_id": 1, 
 
          *  "hex_code": "string", 
 
          *  "red": 0, 
 
          *  "green": 0, 
 
          *  "blue": 0, 
 
          *  "hue": 0, 
 
          *  "saturation": 0, 
 
          *  "brightness": 0, 
 
          *  "is_black_and_white": true, 
 
          *  "creation_tsz": 0, 
 
          *  "created_timestamp": 0, 
 
          *  "rank": 0, 
 
          *  "url_75x75": "string", 
 
          *  "url_170x135": "string", 
 
          *  "url_570xN": "string", 
 
          *  "url_fullxfull": "string", 
 
          *  "full_height": 0, 
 
          *  "full_width": 0, 
 
          *  "alt_text": "string" 
  } 
 ], 
 
      *  "videos": [
        *  { 
          *  "video_id": 1, 
 
          *  "height": 0, 
 
          *  "width": 0, 
 
          *  "thumbnail_url": "string", 
 
          *  "video_url": "string", 
 
          *  "video_state": "active" 
  } 
 ], 
 
      *  "inventory": { 
        *  "products": [
          *  { 
            *  "product_id": 1, 
 
            *  "sku": "string", 
 
            *  "is_deleted": true, 
 
            *  "offerings": [
              *  { 
                *  "offering_id": 1, 
 
                *  "quantity": 0, 
 
                *  "is_enabled": true, 
 
                *  "is_deleted": true, 
 
                *  "price": { 
                  *  "amount": 0, 
 
                  *  "divisor": 0, 
 
                  *  "currency_code": "string" 
  }, 
 
                *  "readiness_state_id": 1 
  } 
 ], 
 
            *  "property_values": [
              *  { 
                *  "property_id": 1, 
 
                *  "property_name": "string", 
 
                *  "scale_id": 1, 
 
                *  "scale_name": "string", 
 
                *  "value_ids": [
                  * 1
 ], 
 
                *  "values": [
                  * "string"
 ] 
  } 
 ] 
  } 
 ], 
 
        *  "price_on_property": [
          * 0
 ], 
 
        *  "quantity_on_property": [
          * 0
 ], 
 
        *  "sku_on_property": [
          * 0
 ], 
 
        *  "readiness_state_on_property": [
          * 1
 ] 
  }, 
 
      *  "production_partners": [
        *  { 
          *  "production_partner_id": 1, 
 
          *  "partner_name": "string", 
 
          *  "location": "string" 
  } 
 ], 
 
      *  "skus": [
        * "string"
 ], 
 
      *  "translations": { 
        *  "de": { 
          *  "listing_id": 1, 
 
          *  "language": "string", 
 
          *  "title": "string", 
 
          *  "description": "string", 
 
          *  "tags": [
            * "string"
 ] 
  }, 
 
        *  "en-GB": { 
          *  "listing_id": 1, 
 
          *  "language": "string", 
 
          *  "title": "string", 
 
          *  "description": "string", 
 
          *  "tags": [
            * "string"
 ] 
  }, 
 
        *  "en-IN": { 
          *  "listing_id": 1, 
 
          *  "language": "string", 
 
          *  "title": "string", 
 
          *  "description": "string", 
 
          *  "tags": [
            * "string"
 ] 
  }, 
 
        *  "en-US": { 
          *  "listing_id": 1, 
 
          *  "language": "string", 
 
          *  "title": "string", 
 
          *  "description": "string", 
 
          *  "tags": [
            * "string"
 ] 
  }, 
 
        *  "es": { 
          *  "listing_id": 1, 
 
          *  "language": "string", 
 
          *  "title": "string", 
 
          *  "description": "string", 
 
          *  "tags": [
            * "string"
 ] 
  }, 
 
        *  "fr": { 
          *  "listing_id": 1, 
 
          *  "language": "string", 
 
          *  "title": "string", 
 
          *  "description": "string", 
 
          *  "tags": [
            * "string"
 ] 
  }, 
 
        *  "it": { 
          *  "listing_id": 1, 
 
          *  "language": "string", 
 
          *  "title": "string", 
 
          *  "description": "string", 
 
          *  "tags": [
            * "string"
 ] 
  }, 
 
        *  "ja": { 
          *  "listing_id": 1, 
 
          *  "language": "string", 
 
          *  "title": "string", 
 
          *  "description": "string", 
 
          *  "tags": [
            * "string"
 ] 
  }, 
 
        *  "nl": { 
          *  "listing_id": 1, 
 
          *  "language": "string", 
 
          *  "title": "string", 
 
          *  "description": "string", 
 
          *  "tags": [
            * "string"
 ] 
  }, 
 
        *  "pl": { 
          *  "listing_id": 1, 
 
          *  "language": "string", 
 
          *  "title": "string", 
 
          *  "description": "string", 
 
          *  "tags": [
            * "string"
 ] 
  }, 
 
        *  "pt": { 
          *  "listing_id": 1, 
 
          *  "language": "string", 
 
          *  "title": "string", 
 
          *  "description": "string", 
 
          *  "tags": [
            * "string"
 ] 
  }, 
 
        *  "ru": { 
          *  "listing_id": 1, 
 
          *  "language": "string", 
 
          *  "title": "string", 
 
          *  "description": "string", 
 
          *  "tags": [
            * "string"
 ] 
  }, 
 
        *  "sv": { 
          *  "listing_id": 1, 
 
          *  "language": "string", 
 
          *  "title": "string", 
 
          *  "description": "string", 
 
          *  "tags": [
            * "string"
 ] 
  } 
  }, 
 
      *  "views": 0, 
 
      *  "personalization": {
        *  "personalization_questions": [
          *  { 
            *  "question_id": 1, 
 
            *  "question_text": "string", 
 
            *  "instructions": "string", 
 
            *  "question_type": "string", 
 
            *  "required": true, 
 
            *  "max_allowed_characters": 0, 
 
            *  "max_allowed_files": 0, 
 
            *  "add_on_price": { 
              *  "amount": 0, 
 
              *  "divisor": 0, 
 
              *  "currency_code": "string" 
  }, 
 
            *  "options": [
              *  { 
                *  "option_id": 1, 
 
                *  "label": "string" 
  } 
 ] 
  } 
 ] 
 }, 
 
      *  "buyer_price": { 
        *  "base_price": { 
          *  "amount": 0, 
 
          *  "divisor": 0, 
 
          *  "currency_code": "string" 
  }, 
 
        *  "shipping_cost": { 
          *  "amount": 0, 
 
          *  "divisor": 0, 
 
          *  "currency_code": "string" 
  }, 
 
        *  "is_free_shipping": true, 
 
        *  "original_price": { 
          *  "amount": 0, 
 
          *  "divisor": 0, 
 
          *  "currency_code": "string" 
  }, 
 
        *  "discounted_price": { 
          *  "amount": 0, 
 
          *  "divisor": 0, 
 
          *  "currency_code": "string" 
  }, 
 
        *  "discount_amount": { 
          *  "amount": 0, 
 
          *  "divisor": 0, 
 
          *  "currency_code": "string" 
  }, 
 
        *  "discount_percentage": 0, 
 
        *  "has_discount": true, 
 
        *  "discount_start_epoch": 0, 
 
        *  "discount_end_epoch": 0 
  } 
  } 
 ] 
 
 }`
#  [](https://developer.etsy.com/documentation/reference/#tag/ShopListing-Offering)ShopListing Offering
##  [](https://developer.etsy.com/documentation/reference/#operation/getListingOffering)getListingOffering 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Get an Offering for a Listing
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)
##### path Parameters  
|  listing_id required   |  integer <int64> >= 1   |  
| --- | --- |  
|  product_id required   |  integer <int64> >= 1   |  
|  product_offering_id required   |  integer <int64> >= 1   |  
##### query Parameters  
| legacy  |  boolean This parameter is needed to enable new parameters and response values related to processing profiles.  |  
| --- | --- |  
### Responses
**200**
A single ListingInventoryProductOffering
**400**
There was a problem with the request data. See the error message for details.
**404**
A resource could not be found. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
get/v3/application/listings/{listing_id}/products/{product_id}/offerings/{product_offering_id}
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/listings/{listing_id}/products/{product_id}/offerings/{product_offering_id}
###  Response samples 
  * 200
  * 400
  * 404
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
 
  *  "offering_id": 1, 
 
  *  "quantity": 0, 
 
  *  "is_enabled": true, 
 
  *  "is_deleted": true, 
 
  *  "price": { 
    *  "amount": 0, 
 
    *  "divisor": 0, 
 
    *  "currency_code": "string" 
  }, 
 
  *  "readiness_state_id": 1 
 
 }`
#  [](https://developer.etsy.com/documentation/reference/#tag/ShopListing-Personalization)ShopListing Personalization
##  [](https://developer.etsy.com/documentation/reference/#operation/deleteListingPersonalization)deleteListingPersonalization 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Deletes personalization for a listing.
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)[oauth2](https://developer.etsy.com/documentation/reference/#section/Authentication/oauth2) (`listings_w`) 
##### path Parameters  
|  shop_id required   |  integer <int64> >= 1  The unique positive non-zero numeric ID for an Etsy Shop.  |  
| --- | --- |  
|  listing_id required   |  integer <int64> >= 1  The numeric ID for the [listing](https://developer.etsy.com/documentation/reference#tag/ShopListing) associated to this transaction.  |  
### Responses
**204**
The ListingPersonalization resource was correctly deleted
**400**
There was a problem with the request data. See the error message for details.
**401**
The request lacks valid authentication credentials. See the error message for details.
**403**
The request attempted to perform an operation it is not allowed to. See the error message for details.
**404**
A resource could not be found. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
delete/v3/application/shops/{shop_id}/listings/{listing_id}/personalization
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/shops/{shop_id}/listings/{listing_id}/personalization
###  Response samples 
  * 400
  * 401
  * 403
  * 404
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
  *  "error": "string" 

 }`
##  [](https://developer.etsy.com/documentation/reference/#operation/updateListingPersonalization)updateListingPersonalization 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Creates or updates personalization settings for a listing, allowing the seller to collect personalization from the buyer. This endpoint will fully replace any existing personalization on the listing.
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)[oauth2](https://developer.etsy.com/documentation/reference/#section/Authentication/oauth2) (`listings_w`) 
##### path Parameters  
|  shop_id required   |  integer <int64> >= 1  The unique positive non-zero numeric ID for an Etsy Shop.  |  
| --- | --- |  
|  listing_id required   |  integer <int64> >= 1  The numeric ID for the [listing](https://developer.etsy.com/documentation/reference#tag/ShopListing) associated to this transaction.  |  
##### query Parameters  
| supports_multiple_personalization_questions  |  boolean Nullable  This query parameter indicates that the caller supports up to 5 personalization questions and the following question types: 'text_input', 'dropdown', 'unlabeled_upload', 'labeled_upload'. Sending this param without updating your application can lead to inadvertently deleting seller-entered data.  |  
| --- | --- |  
##### Request Body schema: application/json  
|  personalization_questions required   |  Array of objects  |  
| --- | --- |  
### Responses
**201**
A single Listing Personalization record
**400**
There was a problem with the request data. See the error message for details.
**401**
The request lacks valid authentication credentials. See the error message for details.
**403**
The request attempted to perform an operation it is not allowed to. See the error message for details.
**404**
A resource could not be found. See the error message for details.
**409**
There was a request conflict with the current state of the target resource. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
post/v3/application/shops/{shop_id}/listings/{listing_id}/personalization
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/shops/{shop_id}/listings/{listing_id}/personalization
###  Request samples 
  * Payload


Content type
application/json
Copy
Expand all  Collapse all 
`{
  *  "personalization_questions": [
    *  { 
      *  "question_id": 1, 
 
      *  "question_text": "string", 
 
      *  "instructions": "string", 
 
      *  "question_type": "text_input", 
 
      *  "required": true, 
 
      *  "max_allowed_files": 0, 
 
      *  "max_allowed_characters": 0, 
 
      *  "options": [
        *  { 
          *  "option_id": 1, 
 
          *  "label": "string" 
  } 
 ], 
 
      *  "add_on_price": 0 
  } 
 ] 

 }`
###  Response samples 
  * 201
  * 400
  * 401
  * 403
  * 404
  * 409
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
  *  "personalization_questions": [
    *  { 
      *  "question_id": 1, 
 
      *  "question_text": "string", 
 
      *  "instructions": "string", 
 
      *  "question_type": "string", 
 
      *  "required": true, 
 
      *  "max_allowed_characters": 0, 
 
      *  "max_allowed_files": 0, 
 
      *  "add_on_price": { 
        *  "amount": 0, 
 
        *  "divisor": 0, 
 
        *  "currency_code": "string" 
  }, 
 
      *  "options": [
        *  { 
          *  "option_id": 1, 
 
          *  "label": "string" 
  } 
 ] 
  } 
 ] 

 }`
##  [](https://developer.etsy.com/documentation/reference/#operation/getListingPersonalization)getListingPersonalization 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Retrieves a listing's personalization questions by listing ID.
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)
##### path Parameters  
|  listing_id required   |  integer <int64> >= 1  The numeric ID for the [listing](https://developer.etsy.com/documentation/reference#tag/ShopListing) associated to this transaction.  |  
| --- | --- |  
### Responses
**200**
A listing personalization questions
**400**
There was a problem with the request data. See the error message for details.
**403**
The request attempted to perform an operation it is not allowed to. See the error message for details.
**404**
A resource could not be found. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
get/v3/application/listings/{listing_id}/personalization
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/listings/{listing_id}/personalization
###  Response samples 
  * 200
  * 400
  * 403
  * 404
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
  *  "personalization_questions": [
    *  { 
      *  "question_id": 1, 
 
      *  "question_text": "string", 
 
      *  "instructions": "string", 
 
      *  "question_type": "string", 
 
      *  "required": true, 
 
      *  "max_allowed_characters": 0, 
 
      *  "max_allowed_files": 0, 
 
      *  "add_on_price": { 
        *  "amount": 0, 
 
        *  "divisor": 0, 
 
        *  "currency_code": "string" 
  }, 
 
      *  "options": [
        *  { 
          *  "option_id": 1, 
 
          *  "label": "string" 
  } 
 ] 
  } 
 ] 

 }`
#  [](https://developer.etsy.com/documentation/reference/#tag/ShopListing-Product)ShopListing Product
##  [](https://developer.etsy.com/documentation/reference/#operation/getListingProduct)getListingProduct 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Open API V3 endpoint to retrieve a ListingProduct by ID.
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)[oauth2](https://developer.etsy.com/documentation/reference/#section/Authentication/oauth2) (`listings_r`) 
##### path Parameters  
|  listing_id required   |  integer <int64> >= 1  The listing to return a ListingProduct for.  |  
| --- | --- |  
|  product_id required   |  integer <int64> >= 1  The numeric ID for a specific [product](https://developer.etsy.com/documentation/reference#tag/ShopListing-Product) purchased from a listing.  |  
##### query Parameters  
| legacy  |  boolean This parameter is needed to enable new parameters and response values related to processing profiles.  |  
| --- | --- |  
### Responses
**200**
A single ListingInventoryProduct
**400**
There was a problem with the request data. See the error message for details.
**401**
The request lacks valid authentication credentials. See the error message for details.
**404**
A resource could not be found. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
get/v3/application/listings/{listing_id}/inventory/products/{product_id}
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/listings/{listing_id}/inventory/products/{product_id}
###  Response samples 
  * 200
  * 400
  * 401
  * 404
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
 
  *  "product_id": 1, 
 
  *  "sku": "string", 
 
  *  "is_deleted": true, 
 
  *  "offerings": [
    *  { 
      *  "offering_id": 1, 
 
      *  "quantity": 0, 
 
      *  "is_enabled": true, 
 
      *  "is_deleted": true, 
 
      *  "price": { 
        *  "amount": 0, 
 
        *  "divisor": 0, 
 
        *  "currency_code": "string" 
  }, 
 
      *  "readiness_state_id": 1 
  } 
 ], 
 
  *  "property_values": [
    *  { 
      *  "property_id": 1, 
 
      *  "property_name": "string", 
 
      *  "scale_id": 1, 
 
      *  "scale_name": "string", 
 
      *  "value_ids": [
        * 1
 ], 
 
      *  "values": [
        * "string"
 ] 
  } 
 ] 
 
 }`
#  [](https://developer.etsy.com/documentation/reference/#tag/ShopListing-Translation)ShopListing Translation
##  [](https://developer.etsy.com/documentation/reference/#operation/createListingTranslation)createListingTranslation 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Creates a ListingTranslation by listing_id and language
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)[oauth2](https://developer.etsy.com/documentation/reference/#section/Authentication/oauth2) (`listings_w`) 
##### path Parameters  
|  shop_id required   |  integer <int64> >= 1  The unique positive non-zero numeric ID for an Etsy Shop.  |  
| --- | --- |  
|  listing_id required   |  integer <int64> >= 1  The numeric ID for the [listing](https://developer.etsy.com/documentation/reference#tag/ShopListing) associated to this transaction.  |  
|  language required   |  string The IETF language tag for the language of this translation. Ex: `de`, `en`, `es`, `fr`, `it`, `ja`, `nl`, `pl`, `pt`.  |  
##### Request Body schema: application/x-www-form-urlencoded  
|  title required   |  string The title of the Listing of this Translation.  |  
| --- | --- |  
|  description required   |  string The description of the Listing of this Translation.  |  
| tags  |  Array of strings The tags of the Listing of this Translation.  |  
### Responses
**200**
A single ListingTranslation
**400**
There was a problem with the request data. See the error message for details.
**401**
The request lacks valid authentication credentials. See the error message for details.
**403**
The request attempted to perform an operation it is not allowed to. See the error message for details.
**404**
A resource could not be found. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
post/v3/application/shops/{shop_id}/listings/{listing_id}/translations/{language}
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/shops/{shop_id}/listings/{listing_id}/translations/{language}
###  Response samples 
  * 200
  * 400
  * 401
  * 403
  * 404
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
 
  *  "listing_id": 1, 
 
  *  "language": "string", 
 
  *  "title": "string", 
 
  *  "description": "string", 
 
  *  "tags": [
    * "string"
 ] 
 
 }`
##  [](https://developer.etsy.com/documentation/reference/#operation/getListingTranslation)getListingTranslation 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Get a Translation for a Listing in the given language
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)
##### path Parameters  
|  shop_id required   |  integer <int64> >= 1  The unique positive non-zero numeric ID for an Etsy Shop.  |  
| --- | --- |  
|  listing_id required   |  integer <int64> >= 1  The numeric ID for the [listing](https://developer.etsy.com/documentation/reference#tag/ShopListing) associated to this transaction.  |  
|  language required   |  string The IETF language tag for the language of this translation. Ex: `de`, `en`, `es`, `fr`, `it`, `ja`, `nl`, `pl`, `pt`.  |  
### Responses
**200**
A single ListingTranslation
**400**
There was a problem with the request data. See the error message for details.
**404**
A resource could not be found. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
get/v3/application/shops/{shop_id}/listings/{listing_id}/translations/{language}
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/shops/{shop_id}/listings/{listing_id}/translations/{language}
###  Response samples 
  * 200
  * 400
  * 404
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
 
  *  "listing_id": 1, 
 
  *  "language": "string", 
 
  *  "title": "string", 
 
  *  "description": "string", 
 
  *  "tags": [
    * "string"
 ] 
 
 }`
##  [](https://developer.etsy.com/documentation/reference/#operation/updateListingTranslation)updateListingTranslation 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Updates a ListingTranslation by listing_id and language
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)[oauth2](https://developer.etsy.com/documentation/reference/#section/Authentication/oauth2) (`listings_w`) 
##### path Parameters  
|  shop_id required   |  integer <int64> >= 1  The unique positive non-zero numeric ID for an Etsy Shop.  |  
| --- | --- |  
|  listing_id required   |  integer <int64> >= 1  The numeric ID for the [listing](https://developer.etsy.com/documentation/reference#tag/ShopListing) associated to this transaction.  |  
|  language required   |  string The IETF language tag for the language of this translation. Ex: `de`, `en`, `es`, `fr`, `it`, `ja`, `nl`, `pl`, `pt`.  |  
##### Request Body schema: application/x-www-form-urlencoded  
|  title required   |  string The title of the Listing of this Translation.  |  
| --- | --- |  
|  description required   |  string The description of the Listing of this Translation.  |  
| tags  |  Array of strings The tags of the Listing of this Translation.  |  
### Responses
**200**
A single ListingTranslation
**400**
There was a problem with the request data. See the error message for details.
**401**
The request lacks valid authentication credentials. See the error message for details.
**403**
The request attempted to perform an operation it is not allowed to. See the error message for details.
**404**
A resource could not be found. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
put/v3/application/shops/{shop_id}/listings/{listing_id}/translations/{language}
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/shops/{shop_id}/listings/{listing_id}/translations/{language}
###  Response samples 
  * 200
  * 400
  * 401
  * 403
  * 404
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
 
  *  "listing_id": 1, 
 
  *  "language": "string", 
 
  *  "title": "string", 
 
  *  "description": "string", 
 
  *  "tags": [
    * "string"
 ] 
 
 }`
#  [](https://developer.etsy.com/documentation/reference/#tag/ShopListing-VariationImage)ShopListing VariationImage
##  [](https://developer.etsy.com/documentation/reference/#operation/getListingVariationImages)getListingVariationImages 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Gets all variation images on a listing.
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)
##### path Parameters  
|  shop_id required   |  integer <int64> >= 1  The unique positive non-zero numeric ID for an Etsy Shop.  |  
| --- | --- |  
|  listing_id required   |  integer <int64> >= 1  The numeric ID for the [listing](https://developer.etsy.com/documentation/reference#tag/ShopListing) associated to this transaction.  |  
### Responses
**200**
A list of ListingVariationImages
**400**
There was a problem with the request data. See the error message for details.
**403**
The request attempted to perform an operation it is not allowed to. See the error message for details.
**404**
A resource could not be found. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
get/v3/application/shops/{shop_id}/listings/{listing_id}/variation-images
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/shops/{shop_id}/listings/{listing_id}/variation-images
###  Response samples 
  * 200
  * 400
  * 403
  * 404
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
 
  *  "count": 0, 
 
  *  "results": [
    *  { 
      *  "property_id": 1, 
 
      *  "value_id": 1, 
 
      *  "value": "string", 
 
      *  "image_id": 1 
  } 
 ] 
 
 }`
##  [](https://developer.etsy.com/documentation/reference/#operation/updateVariationImages)updateVariationImages 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Creates variation images on a listing. `variation_images` is an array with inputs for the `property_id`, `value_id`, and `image_id` fields. `image_ids` are associated with a `ListingImage` on the listing associated with the provided `listing_id`. `property_id` and `value_id` pairs are associated with a `ListingProduct` on the listing associated with the provided `listing_id`. `variation_images` should not contain any duplicates. `variation_images` does not contain more than one `property_id` as variation images can only be associated on one property. The update overwrites all existing variation images on a listing, so if your request is successful, the variation images on the listing will be exactly those you specify. 
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)[oauth2](https://developer.etsy.com/documentation/reference/#section/Authentication/oauth2) (`listings_w`) 
##### path Parameters  
|  shop_id required   |  integer <int64> >= 1  The unique positive non-zero numeric ID for an Etsy Shop.  |  
| --- | --- |  
|  listing_id required   |  integer <int64> >= 1  The numeric ID for the [listing](https://developer.etsy.com/documentation/reference#tag/ShopListing) associated to this transaction.  |  
##### Request Body schema: application/json  
|  variation_images required   |  Array of objects A list of variation image data.  |  
| --- | --- |  
### Responses
**200**
A single ListingVariationImage
**400**
There was a problem with the request data. See the error message for details.
**401**
The request lacks valid authentication credentials. See the error message for details.
**403**
The request attempted to perform an operation it is not allowed to. See the error message for details.
**404**
A resource could not be found. See the error message for details.
**409**
There was a request conflict with the current state of the target resource. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
post/v3/application/shops/{shop_id}/listings/{listing_id}/variation-images
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/shops/{shop_id}/listings/{listing_id}/variation-images
###  Request samples 
  * Payload


Content type
application/json
Copy
Expand all  Collapse all 
`{
  *  "variation_images": [
    *  { 
      *  "property_id": 1, 
 
      *  "value_id": 1, 
 
      *  "image_id": 1 
  } 
 ] 

 }`
###  Response samples 
  * 200
  * 400
  * 401
  * 403
  * 404
  * 409
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
 
  *  "count": 0, 
 
  *  "results": [
    *  { 
      *  "property_id": 1, 
 
      *  "value_id": 1, 
 
      *  "value": "string", 
 
      *  "image_id": 1 
  } 
 ] 
 
 }`
#  [](https://developer.etsy.com/documentation/reference/#tag/ShopListing-Video)ShopListing Video
##  [](https://developer.etsy.com/documentation/reference/#operation/deleteListingVideo)deleteListingVideo 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Open API V3 endpoint to delete a listing video. A copy of the video remains on our servers, and so a deleted video may be re-associated with the listing without re-uploading the original video; see uploadListingVideo.
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)[oauth2](https://developer.etsy.com/documentation/reference/#section/Authentication/oauth2) (`listings_w`) 
##### path Parameters  
|  shop_id required   |  integer <int64> >= 1  The unique positive non-zero numeric ID for an Etsy Shop.  |  
| --- | --- |  
|  listing_id required   |  integer <int64> >= 1  The numeric ID for the [listing](https://developer.etsy.com/documentation/reference#tag/ShopListing) associated to this transaction.  |  
|  video_id required   |  integer <int64> >= 1  The unique ID of a video associated with a listing.  |  
### Responses
**204**
The ListingVideo resource was correctly deleted
**400**
There was a problem with the request data. See the error message for details.
**401**
The request lacks valid authentication credentials. See the error message for details.
**403**
The request attempted to perform an operation it is not allowed to. See the error message for details.
**404**
A resource could not be found. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
delete/v3/application/shops/{shop_id}/listings/{listing_id}/videos/{video_id}
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/shops/{shop_id}/listings/{listing_id}/videos/{video_id}
###  Response samples 
  * 400
  * 401
  * 403
  * 404
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
  *  "error": "string" 

 }`
##  [](https://developer.etsy.com/documentation/reference/#operation/getListingVideo)getListingVideo 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Retrieves a single video associated with the given listing. Requesting a video from a listing returns an empty result.
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)
##### path Parameters  
|  video_id required   |  integer <int64> >= 1  The unique ID of a video associated with a listing.  |  
| --- | --- |  
|  listing_id required   |  integer <int64> >= 1  The numeric ID for the [listing](https://developer.etsy.com/documentation/reference#tag/ShopListing) associated to this transaction.  |  
### Responses
**200**
The metadata for a video associated with a listing.
**400**
There was a problem with the request data. See the error message for details.
**401**
The request lacks valid authentication credentials. See the error message for details.
**403**
The request attempted to perform an operation it is not allowed to. See the error message for details.
**404**
A resource could not be found. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
get/v3/application/listings/{listing_id}/videos/{video_id}
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/listings/{listing_id}/videos/{video_id}
###  Response samples 
  * 200
  * 400
  * 401
  * 403
  * 404
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
 
  *  "video_id": 1, 
 
  *  "height": 0, 
 
  *  "width": 0, 
 
  *  "thumbnail_url": "string", 
 
  *  "video_url": "string", 
 
  *  "video_state": "active" 
 
 }`
##  [](https://developer.etsy.com/documentation/reference/#operation/getListingVideos)getListingVideos 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Retrieves all listing video resources for a listing with a specific listing ID.
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)
##### path Parameters  
|  listing_id required   |  integer <int64> >= 1  The numeric ID for the [listing](https://developer.etsy.com/documentation/reference#tag/ShopListing) associated to this transaction.  |  
| --- | --- |  
### Responses
**200**
A list of videos for a listing
**400**
There was a problem with the request data. See the error message for details.
**403**
The request attempted to perform an operation it is not allowed to. See the error message for details.
**404**
A resource could not be found. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
get/v3/application/listings/{listing_id}/videos
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/listings/{listing_id}/videos
###  Response samples 
  * 200
  * 400
  * 403
  * 404
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
 
  *  "count": 0, 
 
  *  "results": [
    *  { 
      *  "video_id": 1, 
 
      *  "height": 0, 
 
      *  "width": 0, 
 
      *  "thumbnail_url": "string", 
 
      *  "video_url": "string", 
 
      *  "video_state": "active" 
  } 
 ] 
 
 }`
##  [](https://developer.etsy.com/documentation/reference/#operation/uploadListingVideo)uploadListingVideo 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Uploads a new video for a listing, or associates an existing video with a specific listing. You must either provide the `video_id` of an existing video, or the name and binary file data for a video to upload. If providing a `video_id`, the video must already be associated with the same shop as the listing, but it does not need to be currently associated with the listing. It's important to consider there is a rate limiting to perform 10 uploads per listing per day.
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)[oauth2](https://developer.etsy.com/documentation/reference/#section/Authentication/oauth2) (`listings_w`) 
##### path Parameters  
|  shop_id required   |  integer <int64> >= 1  The unique positive non-zero numeric ID for an Etsy Shop.  |  
| --- | --- |  
|  listing_id required   |  integer <int64> >= 1  The numeric ID for the [listing](https://developer.etsy.com/documentation/reference#tag/ShopListing) associated to this transaction.  |  
##### Request Body schema: multipart/form-data  
| video_id  |  integer <int64> >= 1  The unique ID of a video associated with a listing.  |  
| --- | --- |  
| video  |  string <binary> Nullable  A video file to upload.  |  
| name  |  string The file name string for the video to upload.  |  
### Responses
**201**
The metadata for a file associated with a digital listing.
**400**
There was a problem with the request data. See the error message for details.
**401**
The request lacks valid authentication credentials. See the error message for details.
**403**
The request attempted to perform an operation it is not allowed to. See the error message for details.
**404**
A resource could not be found. See the error message for details.
**409**
There was a request conflict with the current state of the target resource. See the error message for details.
**429**
The request exceeded the valid number of uploaded videos per listing per day. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
post/v3/application/shops/{shop_id}/listings/{listing_id}/videos
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/shops/{shop_id}/listings/{listing_id}/videos
###  Response samples 
  * 201
  * 400
  * 401
  * 403
  * 404
  * 409
  * 429
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
 
  *  "video_id": 1, 
 
  *  "height": 0, 
 
  *  "width": 0, 
 
  *  "thumbnail_url": "string", 
 
  *  "video_url": "string", 
 
  *  "video_state": "active" 
 
 }`
#  [](https://developer.etsy.com/documentation/reference/#tag/Other)Other
##  [](https://developer.etsy.com/documentation/reference/#operation/ping)ping 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Check to confirm connectivity to the Etsy API with an application
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)
### Responses
**200**
A confirmation that the current application has access to the Open API
**401**
Missing or invalid API key.
**404**
App does not have the proper permissions to access this resource.
**500**
The server encountered an internal error. See the error message for details.
get/v3/application/openapi-ping
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/openapi-ping
###  Response samples 
  * 200
  * 401
  * 404
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
  *  "application_id": 1 

 }`
##  [](https://developer.etsy.com/documentation/reference/#operation/tokenScopes)tokenScopes 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Check the scopes of the provided token
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)
##### Request Body schema: application/x-www-form-urlencoded  
|  token required   |  string  |  
| --- | --- |  
### Responses
**200**
A confirmation that the current application has access to the Open API
**401**
Missing or invalid API key.
**500**
The server encountered an internal error. See the error message for details.
post/v3/application/scopes
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/scopes
###  Response samples 
  * 200
  * 401
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{ }`
#  [](https://developer.etsy.com/documentation/reference/#tag/Ledger-Entry)Ledger Entry
##  [](https://developer.etsy.com/documentation/reference/#operation/getShopPaymentAccountLedgerEntry)getShopPaymentAccountLedgerEntry 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Get a single Shop Payment Account Ledger's Entry
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)[oauth2](https://developer.etsy.com/documentation/reference/#section/Authentication/oauth2) (`transactions_r`) 
##### path Parameters  
|  shop_id required   |  integer <int64> >= 1  The unique positive non-zero numeric ID for an Etsy Shop.  |  
| --- | --- |  
|  ledger_entry_id required   |  integer <int64> >= 1  The unique ID of the shop owner ledger entry.  |  
### Responses
**200**
A single of PaymentAccountLedgerEntry
**400**
There was a problem with the request data. See the error message for details.
**401**
The request lacks valid authentication credentials. See the error message for details.
**403**
The request attempted to perform an operation it is not allowed to. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
get/v3/application/shops/{shop_id}/payment-account/ledger-entries/{ledger_entry_id}
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/shops/{shop_id}/payment-account/ledger-entries/{ledger_entry_id}
###  Response samples 
  * 200
  * 400
  * 401
  * 403
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
 
  *  "entry_id": 1, 
 
  *  "ledger_id": 1, 
 
  *  "sequence_number": 0, 
 
  *  "amount": 0, 
 
  *  "currency": "string", 
 
  *  "description": "string", 
 
  *  "balance": 0, 
 
  *  "create_date": 0, 
 
  *  "created_timestamp": 0, 
 
  *  "ledger_type": "string", 
 
  *  "reference_type": "string", 
 
  *  "reference_id": "string", 
 
  *  "parent_entry_id": 0, 
 
  *  "payment_adjustments": [
    *  { 
      *  "payment_adjustment_id": 1, 
 
      *  "payment_id": 1, 
 
      *  "status": "string", 
 
      *  "is_success": true, 
 
      *  "user_id": 1, 
 
      *  "reason_code": "string", 
 
      *  "total_adjustment_amount": 0, 
 
      *  "shop_total_adjustment_amount": 0, 
 
      *  "buyer_total_adjustment_amount": 0, 
 
      *  "total_fee_adjustment_amount": 0, 
 
      *  "create_timestamp": 946684800, 
 
      *  "created_timestamp": 946684800, 
 
      *  "update_timestamp": 946684800, 
 
      *  "updated_timestamp": 946684800, 
 
      *  "payment_adjustment_items": [
        *  { 
          *  "payment_adjustment_id": 1, 
 
          *  "payment_adjustment_item_id": 1, 
 
          *  "adjustment_type": "string", 
 
          *  "amount": 0, 
 
          *  "shop_amount": 0, 
 
          *  "transaction_id": 1, 
 
          *  "bill_payment_id": 1, 
 
          *  "created_timestamp": 946684800, 
 
          *  "updated_timestamp": 946684800 
  } 
 ] 
  } 
 ] 
 
 }`
##  [](https://developer.etsy.com/documentation/reference/#operation/getShopPaymentAccountLedgerEntries)getShopPaymentAccountLedgerEntries 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Get a Shop Payment Account Ledger's Entries
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)[oauth2](https://developer.etsy.com/documentation/reference/#section/Authentication/oauth2) (`transactions_r`) 
##### path Parameters  
|  shop_id required   |  integer <int64> >= 1  The unique positive non-zero numeric ID for an Etsy Shop.  |  
| --- | --- |  
##### query Parameters  
|  min_created required   |  integer <int64> >= 946684800  The earliest unix timestamp for when a record was created.  |  
| --- | --- |  
|  max_created required   |  integer <int64> >= 946684800  The latest unix timestamp for when a record was created.  |  
| limit  |  integer <int64> [ 1 .. 100 ]  Default:  25 The maximum number of results to return.  |  
| offset  |  integer <int64> >= 0  Default:  0 The number of records to skip before selecting the first result.  |  
### Responses
**200**
A list of PaymentAccountLedgerEntries
**400**
There was a problem with the request data. See the error message for details.
**401**
The request lacks valid authentication credentials. See the error message for details.
**403**
The request attempted to perform an operation it is not allowed to. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
get/v3/application/shops/{shop_id}/payment-account/ledger-entries
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/shops/{shop_id}/payment-account/ledger-entries
###  Response samples 
  * 200
  * 400
  * 401
  * 403
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
 
  *  "count": 0, 
 
  *  "results": [
    *  { 
      *  "entry_id": 1, 
 
      *  "ledger_id": 1, 
 
      *  "sequence_number": 0, 
 
      *  "amount": 0, 
 
      *  "currency": "string", 
 
      *  "description": "string", 
 
      *  "balance": 0, 
 
      *  "create_date": 0, 
 
      *  "created_timestamp": 0, 
 
      *  "ledger_type": "string", 
 
      *  "reference_type": "string", 
 
      *  "reference_id": "string", 
 
      *  "parent_entry_id": 0, 
 
      *  "payment_adjustments": [
        *  { 
          *  "payment_adjustment_id": 1, 
 
          *  "payment_id": 1, 
 
          *  "status": "string", 
 
          *  "is_success": true, 
 
          *  "user_id": 1, 
 
          *  "reason_code": "string", 
 
          *  "total_adjustment_amount": 0, 
 
          *  "shop_total_adjustment_amount": 0, 
 
          *  "buyer_total_adjustment_amount": 0, 
 
          *  "total_fee_adjustment_amount": 0, 
 
          *  "create_timestamp": 946684800, 
 
          *  "created_timestamp": 946684800, 
 
          *  "update_timestamp": 946684800, 
 
          *  "updated_timestamp": 946684800, 
 
          *  "payment_adjustment_items": [
            *  { 
              *  "payment_adjustment_id": 1, 
 
              *  "payment_adjustment_item_id": 1, 
 
              *  "adjustment_type": "string", 
 
              *  "amount": 0, 
 
              *  "shop_amount": 0, 
 
              *  "transaction_id": 1, 
 
              *  "bill_payment_id": 1, 
 
              *  "created_timestamp": 946684800, 
 
              *  "updated_timestamp": 946684800 
  } 
 ] 
  } 
 ] 
  } 
 ] 
 
 }`
#  [](https://developer.etsy.com/documentation/reference/#tag/Payment)Payment
##  [](https://developer.etsy.com/documentation/reference/#operation/getPaymentAccountLedgerEntryPayments)getPaymentAccountLedgerEntryPayments 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Get a Payment from a PaymentAccount Ledger Entry ID, if applicable
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)[oauth2](https://developer.etsy.com/documentation/reference/#section/Authentication/oauth2) (`transactions_r`) 
##### path Parameters  
|  shop_id required   |  integer <int64> >= 1  The unique positive non-zero numeric ID for an Etsy Shop.  |  
| --- | --- |  
##### query Parameters  
|  ledger_entry_ids required   |  Array of integers <int64>  |  
| --- | --- |  
### Responses
**200**
A list of Payments
**400**
There was a problem with the request data. See the error message for details.
**401**
The request lacks valid authentication credentials. See the error message for details.
**403**
The request attempted to perform an operation it is not allowed to. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
get/v3/application/shops/{shop_id}/payment-account/ledger-entries/payments
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/shops/{shop_id}/payment-account/ledger-entries/payments
###  Response samples 
  * 200
  * 400
  * 401
  * 403
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
 
  *  "count": 0, 
 
  *  "results": [
    *  { 
      *  "payment_id": 1, 
 
      *  "buyer_user_id": 1, 
 
      *  "shop_id": 1, 
 
      *  "receipt_id": 1, 
 
      *  "amount_gross": { 
        *  "amount": 0, 
 
        *  "divisor": 0, 
 
        *  "currency_code": "string" 
  }, 
 
      *  "amount_fees": { 
        *  "amount": 0, 
 
        *  "divisor": 0, 
 
        *  "currency_code": "string" 
  }, 
 
      *  "amount_net": { 
        *  "amount": 0, 
 
        *  "divisor": 0, 
 
        *  "currency_code": "string" 
  }, 
 
      *  "posted_gross": { 
        *  "amount": 0, 
 
        *  "divisor": 0, 
 
        *  "currency_code": "string" 
  }, 
 
      *  "posted_fees": { 
        *  "amount": 0, 
 
        *  "divisor": 0, 
 
        *  "currency_code": "string" 
  }, 
 
      *  "posted_net": { 
        *  "amount": 0, 
 
        *  "divisor": 0, 
 
        *  "currency_code": "string" 
  }, 
 
      *  "adjusted_gross": { 
        *  "amount": 0, 
 
        *  "divisor": 0, 
 
        *  "currency_code": "string" 
  }, 
 
      *  "adjusted_fees": { 
        *  "amount": 0, 
 
        *  "divisor": 0, 
 
        *  "currency_code": "string" 
  }, 
 
      *  "adjusted_net": { 
        *  "amount": 0, 
 
        *  "divisor": 0, 
 
        *  "currency_code": "string" 
  }, 
 
      *  "currency": "string", 
 
      *  "shop_currency": "string", 
 
      *  "buyer_currency": "string", 
 
      *  "shipping_user_id": 1, 
 
      *  "shipping_address_id": 1, 
 
      *  "billing_address_id": 9223372036854776000, 
 
      *  "status": "string", 
 
      *  "shipped_timestamp": 946684800, 
 
      *  "create_timestamp": 946684800, 
 
      *  "created_timestamp": 946684800, 
 
      *  "update_timestamp": 946684800, 
 
      *  "updated_timestamp": 946684800, 
 
      *  "payment_adjustments": [
        *  { 
          *  "payment_adjustment_id": 1, 
 
          *  "payment_id": 1, 
 
          *  "status": "string", 
 
          *  "is_success": true, 
 
          *  "user_id": 1, 
 
          *  "reason_code": "string", 
 
          *  "total_adjustment_amount": 0, 
 
          *  "shop_total_adjustment_amount": 0, 
 
          *  "buyer_total_adjustment_amount": 0, 
 
          *  "total_fee_adjustment_amount": 0, 
 
          *  "create_timestamp": 946684800, 
 
          *  "created_timestamp": 946684800, 
 
          *  "update_timestamp": 946684800, 
 
          *  "updated_timestamp": 946684800, 
 
          *  "payment_adjustment_items": [
            *  { 
              *  "payment_adjustment_id": 1, 
 
              *  "payment_adjustment_item_id": 1, 
 
              *  "adjustment_type": "string", 
 
              *  "amount": 0, 
 
              *  "shop_amount": 0, 
 
              *  "transaction_id": 1, 
 
              *  "bill_payment_id": 1, 
 
              *  "created_timestamp": 946684800, 
 
              *  "updated_timestamp": 946684800 
  } 
 ] 
  } 
 ] 
  } 
 ] 
 
 }`
##  [](https://developer.etsy.com/documentation/reference/#operation/getShopPaymentByReceiptId)getShopPaymentByReceiptId 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Retrieves a payment from a specific receipt, identified by `receipt_id`, from a specific shop, identified by `shop_id`
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)[oauth2](https://developer.etsy.com/documentation/reference/#section/Authentication/oauth2) (`transactions_r`) 
##### path Parameters  
|  shop_id required   |  integer <int64> >= 1  The unique positive non-zero numeric ID for an Etsy Shop.  |  
| --- | --- |  
|  receipt_id required   |  integer <int64> >= 1  The numeric ID for the [receipt](https://developer.etsy.com/documentation/reference#tag/Shop-Receipt) associated to this transaction.  |  
### Responses
**200**
A single payment
**400**
There was a problem with the request data. See the error message for details.
**401**
The request lacks valid authentication credentials. See the error message for details.
**403**
The request attempted to perform an operation it is not allowed to. See the error message for details.
**404**
A resource could not be found. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
get/v3/application/shops/{shop_id}/receipts/{receipt_id}/payments
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/shops/{shop_id}/receipts/{receipt_id}/payments
###  Response samples 
  * 200
  * 400
  * 401
  * 403
  * 404
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
 
  *  "count": 0, 
 
  *  "results": [
    *  { 
      *  "payment_id": 1, 
 
      *  "buyer_user_id": 1, 
 
      *  "shop_id": 1, 
 
      *  "receipt_id": 1, 
 
      *  "amount_gross": { 
        *  "amount": 0, 
 
        *  "divisor": 0, 
 
        *  "currency_code": "string" 
  }, 
 
      *  "amount_fees": { 
        *  "amount": 0, 
 
        *  "divisor": 0, 
 
        *  "currency_code": "string" 
  }, 
 
      *  "amount_net": { 
        *  "amount": 0, 
 
        *  "divisor": 0, 
 
        *  "currency_code": "string" 
  }, 
 
      *  "posted_gross": { 
        *  "amount": 0, 
 
        *  "divisor": 0, 
 
        *  "currency_code": "string" 
  }, 
 
      *  "posted_fees": { 
        *  "amount": 0, 
 
        *  "divisor": 0, 
 
        *  "currency_code": "string" 
  }, 
 
      *  "posted_net": { 
        *  "amount": 0, 
 
        *  "divisor": 0, 
 
        *  "currency_code": "string" 
  }, 
 
      *  "adjusted_gross": { 
        *  "amount": 0, 
 
        *  "divisor": 0, 
 
        *  "currency_code": "string" 
  }, 
 
      *  "adjusted_fees": { 
        *  "amount": 0, 
 
        *  "divisor": 0, 
 
        *  "currency_code": "string" 
  }, 
 
      *  "adjusted_net": { 
        *  "amount": 0, 
 
        *  "divisor": 0, 
 
        *  "currency_code": "string" 
  }, 
 
      *  "currency": "string", 
 
      *  "shop_currency": "string", 
 
      *  "buyer_currency": "string", 
 
      *  "shipping_user_id": 1, 
 
      *  "shipping_address_id": 1, 
 
      *  "billing_address_id": 9223372036854776000, 
 
      *  "status": "string", 
 
      *  "shipped_timestamp": 946684800, 
 
      *  "create_timestamp": 946684800, 
 
      *  "created_timestamp": 946684800, 
 
      *  "update_timestamp": 946684800, 
 
      *  "updated_timestamp": 946684800, 
 
      *  "payment_adjustments": [
        *  { 
          *  "payment_adjustment_id": 1, 
 
          *  "payment_id": 1, 
 
          *  "status": "string", 
 
          *  "is_success": true, 
 
          *  "user_id": 1, 
 
          *  "reason_code": "string", 
 
          *  "total_adjustment_amount": 0, 
 
          *  "shop_total_adjustment_amount": 0, 
 
          *  "buyer_total_adjustment_amount": 0, 
 
          *  "total_fee_adjustment_amount": 0, 
 
          *  "create_timestamp": 946684800, 
 
          *  "created_timestamp": 946684800, 
 
          *  "update_timestamp": 946684800, 
 
          *  "updated_timestamp": 946684800, 
 
          *  "payment_adjustment_items": [
            *  { 
              *  "payment_adjustment_id": 1, 
 
              *  "payment_adjustment_item_id": 1, 
 
              *  "adjustment_type": "string", 
 
              *  "amount": 0, 
 
              *  "shop_amount": 0, 
 
              *  "transaction_id": 1, 
 
              *  "bill_payment_id": 1, 
 
              *  "created_timestamp": 946684800, 
 
              *  "updated_timestamp": 946684800 
  } 
 ] 
  } 
 ] 
  } 
 ] 
 
 }`
##  [](https://developer.etsy.com/documentation/reference/#operation/getPayments)getPayments 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Retrieves a list of payments from a shop identified by `shop_id`. You can also filter results using a list of payment IDs.
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)[oauth2](https://developer.etsy.com/documentation/reference/#section/Authentication/oauth2) (`transactions_r`) 
##### path Parameters  
|  shop_id required   |  integer <int64> >= 1  The unique positive non-zero numeric ID for an Etsy Shop.  |  
| --- | --- |  
##### query Parameters  
|  payment_ids required   |  Array of integers <int64> A comma-separated array of Payment IDs numbers.  |  
| --- | --- |  
### Responses
**200**
A list of payments from a specific shop.
**400**
There was a problem with the request data. See the error message for details.
**401**
The request lacks valid authentication credentials. See the error message for details.
**403**
The request attempted to perform an operation it is not allowed to. See the error message for details.
**404**
A resource could not be found. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
get/v3/application/shops/{shop_id}/payments
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/shops/{shop_id}/payments
###  Response samples 
  * 200
  * 400
  * 401
  * 403
  * 404
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
 
  *  "count": 0, 
 
  *  "results": [
    *  { 
      *  "payment_id": 1, 
 
      *  "buyer_user_id": 1, 
 
      *  "shop_id": 1, 
 
      *  "receipt_id": 1, 
 
      *  "amount_gross": { 
        *  "amount": 0, 
 
        *  "divisor": 0, 
 
        *  "currency_code": "string" 
  }, 
 
      *  "amount_fees": { 
        *  "amount": 0, 
 
        *  "divisor": 0, 
 
        *  "currency_code": "string" 
  }, 
 
      *  "amount_net": { 
        *  "amount": 0, 
 
        *  "divisor": 0, 
 
        *  "currency_code": "string" 
  }, 
 
      *  "posted_gross": { 
        *  "amount": 0, 
 
        *  "divisor": 0, 
 
        *  "currency_code": "string" 
  }, 
 
      *  "posted_fees": { 
        *  "amount": 0, 
 
        *  "divisor": 0, 
 
        *  "currency_code": "string" 
  }, 
 
      *  "posted_net": { 
        *  "amount": 0, 
 
        *  "divisor": 0, 
 
        *  "currency_code": "string" 
  }, 
 
      *  "adjusted_gross": { 
        *  "amount": 0, 
 
        *  "divisor": 0, 
 
        *  "currency_code": "string" 
  }, 
 
      *  "adjusted_fees": { 
        *  "amount": 0, 
 
        *  "divisor": 0, 
 
        *  "currency_code": "string" 
  }, 
 
      *  "adjusted_net": { 
        *  "amount": 0, 
 
        *  "divisor": 0, 
 
        *  "currency_code": "string" 
  }, 
 
      *  "currency": "string", 
 
      *  "shop_currency": "string", 
 
      *  "buyer_currency": "string", 
 
      *  "shipping_user_id": 1, 
 
      *  "shipping_address_id": 1, 
 
      *  "billing_address_id": 9223372036854776000, 
 
      *  "status": "string", 
 
      *  "shipped_timestamp": 946684800, 
 
      *  "create_timestamp": 946684800, 
 
      *  "created_timestamp": 946684800, 
 
      *  "update_timestamp": 946684800, 
 
      *  "updated_timestamp": 946684800, 
 
      *  "payment_adjustments": [
        *  { 
          *  "payment_adjustment_id": 1, 
 
          *  "payment_id": 1, 
 
          *  "status": "string", 
 
          *  "is_success": true, 
 
          *  "user_id": 1, 
 
          *  "reason_code": "string", 
 
          *  "total_adjustment_amount": 0, 
 
          *  "shop_total_adjustment_amount": 0, 
 
          *  "buyer_total_adjustment_amount": 0, 
 
          *  "total_fee_adjustment_amount": 0, 
 
          *  "create_timestamp": 946684800, 
 
          *  "created_timestamp": 946684800, 
 
          *  "update_timestamp": 946684800, 
 
          *  "updated_timestamp": 946684800, 
 
          *  "payment_adjustment_items": [
            *  { 
              *  "payment_adjustment_id": 1, 
 
              *  "payment_adjustment_item_id": 1, 
 
              *  "adjustment_type": "string", 
 
              *  "amount": 0, 
 
              *  "shop_amount": 0, 
 
              *  "transaction_id": 1, 
 
              *  "bill_payment_id": 1, 
 
              *  "created_timestamp": 946684800, 
 
              *  "updated_timestamp": 946684800 
  } 
 ] 
  } 
 ] 
  } 
 ] 
 
 }`
#  [](https://developer.etsy.com/documentation/reference/#tag/Shop-Receipt)Shop Receipt
##  [](https://developer.etsy.com/documentation/reference/#operation/getShopReceipt)getShopReceipt 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Retrieves a receipt, identified by a receipt id, from an Etsy shop. **NOTE** Access to ShopReceipt's first_line, second_line, city, state, zip, country_iso and formatted_address is contingent in some regions to a preferred partnership status with Etsy
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)[oauth2](https://developer.etsy.com/documentation/reference/#section/Authentication/oauth2) (`transactions_r`) 
##### path Parameters  
|  shop_id required   |  integer <int64> >= 1  The unique positive non-zero numeric ID for an Etsy Shop.  |  
| --- | --- |  
|  receipt_id required   |  integer <int64> >= 1  The numeric ID for the [receipt](https://developer.etsy.com/documentation/reference#tag/Shop-Receipt) associated to this transaction.  |  
##### query Parameters  
| legacy  |  boolean This parameter needed to enable new parameters and response values related to processing profiles.  |  
| --- | --- |  
### Responses
**200**
A single Shop Receipt
**400**
There was a problem with the request data. See the error message for details.
**401**
The request lacks valid authentication credentials. See the error message for details.
**403**
The request attempted to perform an operation it is not allowed to. See the error message for details.
**404**
A resource could not be found. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
get/v3/application/shops/{shop_id}/receipts/{receipt_id}
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/shops/{shop_id}/receipts/{receipt_id}
###  Response samples 
  * 200
  * 400
  * 401
  * 403
  * 404
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
 
  *  "receipt_id": 1, 
 
  *  "receipt_type": 0, 
 
  *  "seller_user_id": 1, 
 
  *  "seller_email": "user@example.com", 
 
  *  "buyer_user_id": 1, 
 
  *  "buyer_email": "string", 
 
  *  "name": "string", 
 
  *  "first_line": "string", 
 
  *  "second_line": "string", 
 
  *  "city": "string", 
 
  *  "state": "string", 
 
  *  "zip": "string", 
 
  *  "status": "paid", 
 
  *  "formatted_address": "string", 
 
  *  "country_iso": "string", 
 
  *  "payment_method": "string", 
 
  *  "payment_email": "string", 
 
  *  "message_from_seller": "string", 
 
  *  "message_from_buyer": "string", 
 
  *  "message_from_payment": "string", 
 
  *  "is_paid": true, 
 
  *  "is_shipped": true, 
 
  *  "create_timestamp": 946684800, 
 
  *  "created_timestamp": 946684800, 
 
  *  "update_timestamp": 946684800, 
 
  *  "updated_timestamp": 946684800, 
 
  *  "is_gift": true, 
 
  *  "gift_message": "string", 
 
  *  "gift_sender": "string", 
 
  *  "grandtotal": { 
    *  "amount": 0, 
 
    *  "divisor": 0, 
 
    *  "currency_code": "string" 
  }, 
 
  *  "subtotal": { 
    *  "amount": 0, 
 
    *  "divisor": 0, 
 
    *  "currency_code": "string" 
  }, 
 
  *  "total_price": { 
    *  "amount": 0, 
 
    *  "divisor": 0, 
 
    *  "currency_code": "string" 
  }, 
 
  *  "total_shipping_cost": { 
    *  "amount": 0, 
 
    *  "divisor": 0, 
 
    *  "currency_code": "string" 
  }, 
 
  *  "total_tax_cost": { 
    *  "amount": 0, 
 
    *  "divisor": 0, 
 
    *  "currency_code": "string" 
  }, 
 
  *  "total_vat_cost": { 
    *  "amount": 0, 
 
    *  "divisor": 0, 
 
    *  "currency_code": "string" 
  }, 
 
  *  "discount_amt": { 
    *  "amount": 0, 
 
    *  "divisor": 0, 
 
    *  "currency_code": "string" 
  }, 
 
  *  "gift_wrap_price": { 
    *  "amount": 0, 
 
    *  "divisor": 0, 
 
    *  "currency_code": "string" 
  }, 
 
  *  "shipments": [
    *  { 
      *  "receipt_shipping_id": 1, 
 
      *  "shipment_notification_timestamp": 946684800, 
 
      *  "carrier_name": "string", 
 
      *  "tracking_code": "string" 
  } 
 ], 
 
  *  "transactions": [
    *  { 
      *  "transaction_id": 1, 
 
      *  "title": "string", 
 
      *  "description": "string", 
 
      *  "seller_user_id": 1, 
 
      *  "buyer_user_id": 1, 
 
      *  "create_timestamp": 946684800, 
 
      *  "created_timestamp": 946684800, 
 
      *  "paid_timestamp": 946684800, 
 
      *  "shipped_timestamp": 946684800, 
 
      *  "quantity": 0, 
 
      *  "listing_image_id": 1, 
 
      *  "receipt_id": 1, 
 
      *  "is_digital": true, 
 
      *  "file_data": "string", 
 
      *  "listing_id": 0, 
 
      *  "transaction_type": "string", 
 
      *  "product_id": 1, 
 
      *  "sku": "string", 
 
      *  "price": { 
        *  "amount": 0, 
 
        *  "divisor": 0, 
 
        *  "currency_code": "string" 
  }, 
 
      *  "shipping_cost": { 
        *  "amount": 0, 
 
        *  "divisor": 0, 
 
        *  "currency_code": "string" 
  }, 
 
      *  "variations": [
        *  { 
          *  "property_id": 0, 
 
          *  "value_id": 0, 
 
          *  "formatted_name": "string", 
 
          *  "formatted_value": "string", 
 
          *  "question_id": 0, 
 
          *  "mime_type": "image/jpeg" 
  } 
 ], 
 
      *  "product_data": [
        *  { 
          *  "property_id": 1, 
 
          *  "property_name": "string", 
 
          *  "scale_id": 1, 
 
          *  "scale_name": "string", 
 
          *  "value_ids": [
            * 1
 ], 
 
          *  "values": [
            * "string"
 ] 
  } 
 ], 
 
      *  "shipping_profile_id": 1, 
 
      *  "min_processing_days": 0, 
 
      *  "max_processing_days": 0, 
 
      *  "shipping_method": "string", 
 
      *  "shipping_upgrade": "string", 
 
      *  "expected_ship_date": 946684800, 
 
      *  "buyer_coupon": 0, 
 
      *  "shop_coupon": 0 
  } 
 ], 
 
  *  "refunds": [
    *  { 
      *  "amount": { 
        *  "amount": 0, 
 
        *  "divisor": 0, 
 
        *  "currency_code": "string" 
  }, 
 
      *  "created_timestamp": 946684800, 
 
      *  "reason": "string", 
 
      *  "note_from_issuer": "string", 
 
      *  "status": "string" 
  } 
 ] 
 
 }`
##  [](https://developer.etsy.com/documentation/reference/#operation/updateShopReceipt)updateShopReceipt 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Updates the status of a receipt, identified by a receipt id, from an Etsy shop. **NOTE** Access to ShopReceipt's first_line, second_line, city, state, zip, country_iso and formatted_address is contingent in some regions to a preferred partnership status with Etsy
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)[oauth2](https://developer.etsy.com/documentation/reference/#section/Authentication/oauth2) (`transactions_w`) 
##### path Parameters  
|  shop_id required   |  integer <int64> >= 1  The unique positive non-zero numeric ID for an Etsy Shop.  |  
| --- | --- |  
|  receipt_id required   |  integer <int64> >= 1  The numeric ID for the [receipt](https://developer.etsy.com/documentation/reference#tag/Shop-Receipt) associated to this transaction.  |  
##### query Parameters  
| legacy  |  boolean This parameter needed to enable new parameters and response values related to processing profiles.  |  
| --- | --- |  
##### Request Body schema: application/x-www-form-urlencoded  
| was_shipped  |  boolean Nullable  When `true`, returns receipts where the seller shipped the product(s) in this receipt. When `false`, returns receipts where shipment has not been set.  |  
| --- | --- |  
| was_paid  |  boolean Nullable  When `true`, returns receipts where the seller has received payment for the receipt. When `false`, returns receipts where payment has not been received.  |  
### Responses
**200**
Update A Shop Receipt
**400**
There was a problem with the request data. See the error message for details.
**401**
The request lacks valid authentication credentials. See the error message for details.
**403**
The request attempted to perform an operation it is not allowed to. See the error message for details.
**404**
A resource could not be found. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
put/v3/application/shops/{shop_id}/receipts/{receipt_id}
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/shops/{shop_id}/receipts/{receipt_id}
###  Response samples 
  * 200
  * 400
  * 401
  * 403
  * 404
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
 
  *  "receipt_id": 1, 
 
  *  "receipt_type": 0, 
 
  *  "seller_user_id": 1, 
 
  *  "seller_email": "user@example.com", 
 
  *  "buyer_user_id": 1, 
 
  *  "buyer_email": "string", 
 
  *  "name": "string", 
 
  *  "first_line": "string", 
 
  *  "second_line": "string", 
 
  *  "city": "string", 
 
  *  "state": "string", 
 
  *  "zip": "string", 
 
  *  "status": "paid", 
 
  *  "formatted_address": "string", 
 
  *  "country_iso": "string", 
 
  *  "payment_method": "string", 
 
  *  "payment_email": "string", 
 
  *  "message_from_seller": "string", 
 
  *  "message_from_buyer": "string", 
 
  *  "message_from_payment": "string", 
 
  *  "is_paid": true, 
 
  *  "is_shipped": true, 
 
  *  "create_timestamp": 946684800, 
 
  *  "created_timestamp": 946684800, 
 
  *  "update_timestamp": 946684800, 
 
  *  "updated_timestamp": 946684800, 
 
  *  "is_gift": true, 
 
  *  "gift_message": "string", 
 
  *  "gift_sender": "string", 
 
  *  "grandtotal": { 
    *  "amount": 0, 
 
    *  "divisor": 0, 
 
    *  "currency_code": "string" 
  }, 
 
  *  "subtotal": { 
    *  "amount": 0, 
 
    *  "divisor": 0, 
 
    *  "currency_code": "string" 
  }, 
 
  *  "total_price": { 
    *  "amount": 0, 
 
    *  "divisor": 0, 
 
    *  "currency_code": "string" 
  }, 
 
  *  "total_shipping_cost": { 
    *  "amount": 0, 
 
    *  "divisor": 0, 
 
    *  "currency_code": "string" 
  }, 
 
  *  "total_tax_cost": { 
    *  "amount": 0, 
 
    *  "divisor": 0, 
 
    *  "currency_code": "string" 
  }, 
 
  *  "total_vat_cost": { 
    *  "amount": 0, 
 
    *  "divisor": 0, 
 
    *  "currency_code": "string" 
  }, 
 
  *  "discount_amt": { 
    *  "amount": 0, 
 
    *  "divisor": 0, 
 
    *  "currency_code": "string" 
  }, 
 
  *  "gift_wrap_price": { 
    *  "amount": 0, 
 
    *  "divisor": 0, 
 
    *  "currency_code": "string" 
  }, 
 
  *  "shipments": [
    *  { 
      *  "receipt_shipping_id": 1, 
 
      *  "shipment_notification_timestamp": 946684800, 
 
      *  "carrier_name": "string", 
 
      *  "tracking_code": "string" 
  } 
 ], 
 
  *  "transactions": [
    *  { 
      *  "transaction_id": 1, 
 
      *  "title": "string", 
 
      *  "description": "string", 
 
      *  "seller_user_id": 1, 
 
      *  "buyer_user_id": 1, 
 
      *  "create_timestamp": 946684800, 
 
      *  "created_timestamp": 946684800, 
 
      *  "paid_timestamp": 946684800, 
 
      *  "shipped_timestamp": 946684800, 
 
      *  "quantity": 0, 
 
      *  "listing_image_id": 1, 
 
      *  "receipt_id": 1, 
 
      *  "is_digital": true, 
 
      *  "file_data": "string", 
 
      *  "listing_id": 0, 
 
      *  "transaction_type": "string", 
 
      *  "product_id": 1, 
 
      *  "sku": "string", 
 
      *  "price": { 
        *  "amount": 0, 
 
        *  "divisor": 0, 
 
        *  "currency_code": "string" 
  }, 
 
      *  "shipping_cost": { 
        *  "amount": 0, 
 
        *  "divisor": 0, 
 
        *  "currency_code": "string" 
  }, 
 
      *  "variations": [
        *  { 
          *  "property_id": 0, 
 
          *  "value_id": 0, 
 
          *  "formatted_name": "string", 
 
          *  "formatted_value": "string", 
 
          *  "question_id": 0, 
 
          *  "mime_type": "image/jpeg" 
  } 
 ], 
 
      *  "product_data": [
        *  { 
          *  "property_id": 1, 
 
          *  "property_name": "string", 
 
          *  "scale_id": 1, 
 
          *  "scale_name": "string", 
 
          *  "value_ids": [
            * 1
 ], 
 
          *  "values": [
            * "string"
 ] 
  } 
 ], 
 
      *  "shipping_profile_id": 1, 
 
      *  "min_processing_days": 0, 
 
      *  "max_processing_days": 0, 
 
      *  "shipping_method": "string", 
 
      *  "shipping_upgrade": "string", 
 
      *  "expected_ship_date": 946684800, 
 
      *  "buyer_coupon": 0, 
 
      *  "shop_coupon": 0 
  } 
 ], 
 
  *  "refunds": [
    *  { 
      *  "amount": { 
        *  "amount": 0, 
 
        *  "divisor": 0, 
 
        *  "currency_code": "string" 
  }, 
 
      *  "created_timestamp": 946684800, 
 
      *  "reason": "string", 
 
      *  "note_from_issuer": "string", 
 
      *  "status": "string" 
  } 
 ] 
 
 }`
##  [](https://developer.etsy.com/documentation/reference/#operation/getShopReceipts)getShopReceipts 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Requests the Shop Receipts from a specific Shop, unfiltered or filtered by receipt id range or offset, date, paid, and/or shipped purchases. **NOTE** Access to ShopReceipt's first_line, second_line, city, state, zip, country_iso and formatted_address is contingent in some regions to a preferred partnership status with Etsy
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)[oauth2](https://developer.etsy.com/documentation/reference/#section/Authentication/oauth2) (`transactions_r`) 
##### path Parameters  
|  shop_id required   |  integer <int64> >= 1  The unique positive non-zero numeric ID for an Etsy Shop.  |  
| --- | --- |  
##### query Parameters  
| min_created  |  integer <int64> >= 946684800  Default:  null The earliest unix timestamp for when a record was created.  |  
| --- | --- |  
| max_created  |  integer <int64> >= 946684800  Default:  null The latest unix timestamp for when a record was created.  |  
| min_last_modified  |  integer <int64> >= 946684800  Default:  null The earliest unix timestamp for when a record last changed.  |  
| max_last_modified  |  integer <int64> >= 946684800  Default:  null The latest unix timestamp for when a record last changed.  |  
| limit  |  integer <int64> [ 1 .. 100 ]  Default:  25 The maximum number of results to return.  |  
| offset  |  integer <int64> >= 0  Default:  0 The number of records to skip before selecting the first result.  |  
| sort_on  |  string Default:  "created" Enum: "created" "updated" "receipt_id" The value to sort a search result of listings on.  |  
| sort_order  |  string Default:  "desc" Enum: "asc" "ascending" "desc" "descending" "up" "down" The ascending(up) or descending(down) order to sort receipts by.  |  
| was_paid  |  boolean Nullable  When `true`, returns receipts where the seller has received payment for the receipt. When `false`, returns receipts where payment has not been received.  |  
| was_shipped  |  boolean Nullable  When `true`, returns receipts where the seller shipped the product(s) in this receipt. When `false`, returns receipts where shipment has not been set.  |  
| was_delivered  |  boolean Nullable  When `true`, returns receipts that have been marked as delivered. When `false`, returns receipts where shipment has not been marked as delivered.  |  
| was_canceled  |  boolean Nullable  When `true`, the endpoint will only return the canceled receipts. When `false`, the endpoint will only return non-canceled receipts.  |  
| legacy  |  boolean This parameter needed to enable new parameters and response values related to processing profiles.  |  
### Responses
**200**
A list of Shop Receipts
**400**
There was a problem with the request data. See the error message for details.
**401**
The request lacks valid authentication credentials. See the error message for details.
**403**
The request attempted to perform an operation it is not allowed to. See the error message for details.
**404**
A resource could not be found. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
get/v3/application/shops/{shop_id}/receipts
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/shops/{shop_id}/receipts
###  Response samples 
  * 200
  * 400
  * 401
  * 403
  * 404
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
 
  *  "count": 0, 
 
  *  "results": [
    *  { 
      *  "receipt_id": 1, 
 
      *  "receipt_type": 0, 
 
      *  "seller_user_id": 1, 
 
      *  "seller_email": "user@example.com", 
 
      *  "buyer_user_id": 1, 
 
      *  "buyer_email": "string", 
 
      *  "name": "string", 
 
      *  "first_line": "string", 
 
      *  "second_line": "string", 
 
      *  "city": "string", 
 
      *  "state": "string", 
 
      *  "zip": "string", 
 
      *  "status": "paid", 
 
      *  "formatted_address": "string", 
 
      *  "country_iso": "string", 
 
      *  "payment_method": "string", 
 
      *  "payment_email": "string", 
 
      *  "message_from_seller": "string", 
 
      *  "message_from_buyer": "string", 
 
      *  "message_from_payment": "string", 
 
      *  "is_paid": true, 
 
      *  "is_shipped": true, 
 
      *  "create_timestamp": 946684800, 
 
      *  "created_timestamp": 946684800, 
 
      *  "update_timestamp": 946684800, 
 
      *  "updated_timestamp": 946684800, 
 
      *  "is_gift": true, 
 
      *  "gift_message": "string", 
 
      *  "gift_sender": "string", 
 
      *  "grandtotal": { 
        *  "amount": 0, 
 
        *  "divisor": 0, 
 
        *  "currency_code": "string" 
  }, 
 
      *  "subtotal": { 
        *  "amount": 0, 
 
        *  "divisor": 0, 
 
        *  "currency_code": "string" 
  }, 
 
      *  "total_price": { 
        *  "amount": 0, 
 
        *  "divisor": 0, 
 
        *  "currency_code": "string" 
  }, 
 
      *  "total_shipping_cost": { 
        *  "amount": 0, 
 
        *  "divisor": 0, 
 
        *  "currency_code": "string" 
  }, 
 
      *  "total_tax_cost": { 
        *  "amount": 0, 
 
        *  "divisor": 0, 
 
        *  "currency_code": "string" 
  }, 
 
      *  "total_vat_cost": { 
        *  "amount": 0, 
 
        *  "divisor": 0, 
 
        *  "currency_code": "string" 
  }, 
 
      *  "discount_amt": { 
        *  "amount": 0, 
 
        *  "divisor": 0, 
 
        *  "currency_code": "string" 
  }, 
 
      *  "gift_wrap_price": { 
        *  "amount": 0, 
 
        *  "divisor": 0, 
 
        *  "currency_code": "string" 
  }, 
 
      *  "shipments": [
        *  { 
          *  "receipt_shipping_id": 1, 
 
          *  "shipment_notification_timestamp": 946684800, 
 
          *  "carrier_name": "string", 
 
          *  "tracking_code": "string" 
  } 
 ], 
 
      *  "transactions": [
        *  { 
          *  "transaction_id": 1, 
 
          *  "title": "string", 
 
          *  "description": "string", 
 
          *  "seller_user_id": 1, 
 
          *  "buyer_user_id": 1, 
 
          *  "create_timestamp": 946684800, 
 
          *  "created_timestamp": 946684800, 
 
          *  "paid_timestamp": 946684800, 
 
          *  "shipped_timestamp": 946684800, 
 
          *  "quantity": 0, 
 
          *  "listing_image_id": 1, 
 
          *  "receipt_id": 1, 
 
          *  "is_digital": true, 
 
          *  "file_data": "string", 
 
          *  "listing_id": 0, 
 
          *  "transaction_type": "string", 
 
          *  "product_id": 1, 
 
          *  "sku": "string", 
 
          *  "price": { 
            *  "amount": 0, 
 
            *  "divisor": 0, 
 
            *  "currency_code": "string" 
  }, 
 
          *  "shipping_cost": { 
            *  "amount": 0, 
 
            *  "divisor": 0, 
 
            *  "currency_code": "string" 
  }, 
 
          *  "variations": [
            *  { 
              *  "property_id": 0, 
 
              *  "value_id": 0, 
 
              *  "formatted_name": "string", 
 
              *  "formatted_value": "string", 
 
              *  "question_id": 0, 
 
              *  "mime_type": "image/jpeg" 
  } 
 ], 
 
          *  "product_data": [
            *  { 
              *  "property_id": 1, 
 
              *  "property_name": "string", 
 
              *  "scale_id": 1, 
 
              *  "scale_name": "string", 
 
              *  "value_ids": [
                * 1
 ], 
 
              *  "values": [
                * "string"
 ] 
  } 
 ], 
 
          *  "shipping_profile_id": 1, 
 
          *  "min_processing_days": 0, 
 
          *  "max_processing_days": 0, 
 
          *  "shipping_method": "string", 
 
          *  "shipping_upgrade": "string", 
 
          *  "expected_ship_date": 946684800, 
 
          *  "buyer_coupon": 0, 
 
          *  "shop_coupon": 0 
  } 
 ], 
 
      *  "refunds": [
        *  { 
          *  "amount": { 
            *  "amount": 0, 
 
            *  "divisor": 0, 
 
            *  "currency_code": "string" 
  }, 
 
          *  "created_timestamp": 946684800, 
 
          *  "reason": "string", 
 
          *  "note_from_issuer": "string", 
 
          *  "status": "string" 
  } 
 ] 
  } 
 ] 
 
 }`
##  [](https://developer.etsy.com/documentation/reference/#operation/createReceiptShipment)createReceiptShipment 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Submits tracking information for a Shop Receipt, which creates a Shop Receipt Shipment entry for the given receipt_id. Each time you successfully submit tracking info, Etsy sends a notification email to the buyer User. When send_bcc is true, Etsy sends shipping notifications to the seller as well. When tracking_code and carrier_name aren't sent, the receipt is marked as shipped only. If the carrier is not supported, you may use `other` as the carrier name so you can provide the tracking code. **NOTES** When shipping within the United States AND the order is over $10 _or_ when shipping to India, tracking code and carrier name ARE required. **ACCESS RESTRICTION** In regions where Etsy's Preferred Partner Program is enforced, this endpoint is only available to applications that are approved fulfillment partners. Requests from other applications return `403 Forbidden`, even when the API key is valid, the OAuth token has the `transactions_w` scope and other receipt endpoints respond successfully. A request is authorized if the application is a commercial-access application categorized as Fulfillment or Print On Demand, if it is a personal-use application owned by the authenticated seller, or if the seller authorized the application before the Preferred Partner Program launched in their region. If your application doesn't meet these criteria, contact Etsy API support to ask about partner eligibility. Access to ShopReceipt's first_line, second_line, city, state, zip, country_iso and formatted_address is contingent in some regions to a preferred partnership status with Etsy
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)[oauth2](https://developer.etsy.com/documentation/reference/#section/Authentication/oauth2) (`transactions_w`) 
##### path Parameters  
|  shop_id required   |  integer <int64> >= 1  The unique positive non-zero numeric ID for an Etsy Shop.  |  
| --- | --- |  
|  receipt_id required   |  integer <int64> >= 1  The receipt to submit tracking for.  |  
##### query Parameters  
| legacy  |  boolean This parameter needed to enable new parameters and response values related to processing profiles.  |  
| --- | --- |  
##### Request Body schema: application/json  
| tracking_code  |  string The tracking code for this receipt.  |  
| --- | --- |  
| carrier_name  |  string The carrier name for this receipt.  |  
| send_bcc  |  boolean If true, the shipping notification will be sent to the seller as well  |  
| note_to_buyer  |  string Message to include in notification to the buyer.  |  
| mail_class  |  string Nullable  The service level of postal or carrier service selected for the shipment (e.g., First-Class, Priority, Ground, Express).  |  
| weight  |  number <float> Nullable  The total weight of the package.  |  
| weight_units  |  string Nullable  Unit of measurement used for package weight (oz, grams, etc.).  |  
| length  |  number <float> Nullable  Longest side of the package.  |  
| width  |  number <float> Nullable  Second longest side of the package.  |  
| height  |  number <float> Nullable  Third longest side of the package.  |  
| dimension_units  |  string Nullable  Unit of measurement used for package dimensions (in, cm...).  |  
| shipping_label_cost  |  number <float> Nullable  The purchase price the seller paid for the shipping label.  |  
| shipping_label_currency  |  string Nullable  The currency in which the shipping label was purchased.  |  
| revenue_eligibility  |  string Nullable  A flag indicating if the shipment is tied to a revenue share agreement between Etsy and the vendor.  |  
| ship_from_country  |  string Nullable  Where the package ships from.  |  
| ship_to_country  |  string Nullable  Package destination.  |  
| incoterm  |  string Nullable  The specific incoterm (e.g., DDU, DDP) designated for the shipment.  |  
| customs_data  |  Array of objects Nullable  Contains custom data like country of origin, declared value and HS code.  |  
| duty_amount  |  number <float> Nullable  The estimated or actual amount of import duties and taxes assessed by customs for the shipment.  |  
| duty_currency  |  string Nullable  The currency in which the duty was paid.  |  
| ship_date  |  string Nullable  The date package was shipped.  |  
### Responses
**200**
A single ShopReceipt
**400**
There was a problem with the request data. See the error message for details.
**401**
The request lacks valid authentication credentials. See the error message for details.
**403**
The request attempted to perform an operation it is not allowed to. See the error message for details.
**404**
A resource could not be found. See the error message for details.
**409**
There was a request conflict with the current state of the target resource. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
post/v3/application/shops/{shop_id}/receipts/{receipt_id}/tracking
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/shops/{shop_id}/receipts/{receipt_id}/tracking
###  Request samples 
  * Payload


Content type
application/json
Copy
Expand all  Collapse all 
`{
 
  *  "tracking_code": "string", 
 
  *  "carrier_name": "string", 
 
  *  "send_bcc": true, 
 
  *  "note_to_buyer": "string", 
 
  *  "mail_class": "string", 
 
  *  "weight": 0, 
 
  *  "weight_units": "string", 
 
  *  "length": 0, 
 
  *  "width": 0, 
 
  *  "height": 0, 
 
  *  "dimension_units": "string", 
 
  *  "shipping_label_cost": 0, 
 
  *  "shipping_label_currency": "string", 
 
  *  "revenue_eligibility": "string", 
 
  *  "ship_from_country": "string", 
 
  *  "ship_to_country": "string", 
 
  *  "incoterm": "string", 
 
  *  "customs_data": [
    *  { 
      *  "country_of_origin": null, 
 
      *  "declared_value": null, 
 
      *  "HS_code": null 
  } 
 ], 
 
  *  "duty_amount": 0, 
 
  *  "duty_currency": "string", 
 
  *  "ship_date": "string" 
 
 }`
###  Response samples 
  * 200
  * 400
  * 401
  * 403
  * 404
  * 409
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
 
  *  "receipt_id": 1, 
 
  *  "receipt_type": 0, 
 
  *  "seller_user_id": 1, 
 
  *  "seller_email": "user@example.com", 
 
  *  "buyer_user_id": 1, 
 
  *  "buyer_email": "string", 
 
  *  "name": "string", 
 
  *  "first_line": "string", 
 
  *  "second_line": "string", 
 
  *  "city": "string", 
 
  *  "state": "string", 
 
  *  "zip": "string", 
 
  *  "status": "paid", 
 
  *  "formatted_address": "string", 
 
  *  "country_iso": "string", 
 
  *  "payment_method": "string", 
 
  *  "payment_email": "string", 
 
  *  "message_from_seller": "string", 
 
  *  "message_from_buyer": "string", 
 
  *  "message_from_payment": "string", 
 
  *  "is_paid": true, 
 
  *  "is_shipped": true, 
 
  *  "create_timestamp": 946684800, 
 
  *  "created_timestamp": 946684800, 
 
  *  "update_timestamp": 946684800, 
 
  *  "updated_timestamp": 946684800, 
 
  *  "is_gift": true, 
 
  *  "gift_message": "string", 
 
  *  "gift_sender": "string", 
 
  *  "grandtotal": { 
    *  "amount": 0, 
 
    *  "divisor": 0, 
 
    *  "currency_code": "string" 
  }, 
 
  *  "subtotal": { 
    *  "amount": 0, 
 
    *  "divisor": 0, 
 
    *  "currency_code": "string" 
  }, 
 
  *  "total_price": { 
    *  "amount": 0, 
 
    *  "divisor": 0, 
 
    *  "currency_code": "string" 
  }, 
 
  *  "total_shipping_cost": { 
    *  "amount": 0, 
 
    *  "divisor": 0, 
 
    *  "currency_code": "string" 
  }, 
 
  *  "total_tax_cost": { 
    *  "amount": 0, 
 
    *  "divisor": 0, 
 
    *  "currency_code": "string" 
  }, 
 
  *  "total_vat_cost": { 
    *  "amount": 0, 
 
    *  "divisor": 0, 
 
    *  "currency_code": "string" 
  }, 
 
  *  "discount_amt": { 
    *  "amount": 0, 
 
    *  "divisor": 0, 
 
    *  "currency_code": "string" 
  }, 
 
  *  "gift_wrap_price": { 
    *  "amount": 0, 
 
    *  "divisor": 0, 
 
    *  "currency_code": "string" 
  }, 
 
  *  "shipments": [
    *  { 
      *  "receipt_shipping_id": 1, 
 
      *  "shipment_notification_timestamp": 946684800, 
 
      *  "carrier_name": "string", 
 
      *  "tracking_code": "string" 
  } 
 ], 
 
  *  "transactions": [
    *  { 
      *  "transaction_id": 1, 
 
      *  "title": "string", 
 
      *  "description": "string", 
 
      *  "seller_user_id": 1, 
 
      *  "buyer_user_id": 1, 
 
      *  "create_timestamp": 946684800, 
 
      *  "created_timestamp": 946684800, 
 
      *  "paid_timestamp": 946684800, 
 
      *  "shipped_timestamp": 946684800, 
 
      *  "quantity": 0, 
 
      *  "listing_image_id": 1, 
 
      *  "receipt_id": 1, 
 
      *  "is_digital": true, 
 
      *  "file_data": "string", 
 
      *  "listing_id": 0, 
 
      *  "transaction_type": "string", 
 
      *  "product_id": 1, 
 
      *  "sku": "string", 
 
      *  "price": { 
        *  "amount": 0, 
 
        *  "divisor": 0, 
 
        *  "currency_code": "string" 
  }, 
 
      *  "shipping_cost": { 
        *  "amount": 0, 
 
        *  "divisor": 0, 
 
        *  "currency_code": "string" 
  }, 
 
      *  "variations": [
        *  { 
          *  "property_id": 0, 
 
          *  "value_id": 0, 
 
          *  "formatted_name": "string", 
 
          *  "formatted_value": "string", 
 
          *  "question_id": 0, 
 
          *  "mime_type": "image/jpeg" 
  } 
 ], 
 
      *  "product_data": [
        *  { 
          *  "property_id": 1, 
 
          *  "property_name": "string", 
 
          *  "scale_id": 1, 
 
          *  "scale_name": "string", 
 
          *  "value_ids": [
            * 1
 ], 
 
          *  "values": [
            * "string"
 ] 
  } 
 ], 
 
      *  "shipping_profile_id": 1, 
 
      *  "min_processing_days": 0, 
 
      *  "max_processing_days": 0, 
 
      *  "shipping_method": "string", 
 
      *  "shipping_upgrade": "string", 
 
      *  "expected_ship_date": 946684800, 
 
      *  "buyer_coupon": 0, 
 
      *  "shop_coupon": 0 
  } 
 ], 
 
  *  "refunds": [
    *  { 
      *  "amount": { 
        *  "amount": 0, 
 
        *  "divisor": 0, 
 
        *  "currency_code": "string" 
  }, 
 
      *  "created_timestamp": 946684800, 
 
      *  "reason": "string", 
 
      *  "note_from_issuer": "string", 
 
      *  "status": "string" 
  } 
 ] 
 
 }`
#  [](https://developer.etsy.com/documentation/reference/#tag/Shop-Receipt-Transactions)Shop Receipt Transactions
##  [](https://developer.etsy.com/documentation/reference/#operation/getShopReceiptTransactionsByListing)getShopReceiptTransactionsByListing 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Retrieves the list of transactions associated with a listing.
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)[oauth2](https://developer.etsy.com/documentation/reference/#section/Authentication/oauth2) (`transactions_r`) 
##### path Parameters  
|  shop_id required   |  integer <int64> >= 1  The unique positive non-zero numeric ID for an Etsy Shop.  |  
| --- | --- |  
|  listing_id required   |  integer <int64> >= 1  The numeric ID for the [listing](https://developer.etsy.com/documentation/reference#tag/ShopListing) associated to this transaction.  |  
##### query Parameters  
| limit  |  integer <int64> [ 1 .. 100 ]  Default:  25 The maximum number of results to return.  |  
| --- | --- |  
| offset  |  integer <int64> >= 0  Default:  0 The number of records to skip before selecting the first result.  |  
| legacy  |  boolean This parameter needed to enable new parameters and response values related to processing profiles.  |  
### Responses
**200**
A list of transactions
**400**
There was a problem with the request data. See the error message for details.
**401**
The request lacks valid authentication credentials. See the error message for details.
**403**
The request attempted to perform an operation it is not allowed to. See the error message for details.
**404**
A resource could not be found. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
get/v3/application/shops/{shop_id}/listings/{listing_id}/transactions
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/shops/{shop_id}/listings/{listing_id}/transactions
###  Response samples 
  * 200
  * 400
  * 401
  * 403
  * 404
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
 
  *  "count": 0, 
 
  *  "results": [
    *  { 
      *  "transaction_id": 1, 
 
      *  "title": "string", 
 
      *  "description": "string", 
 
      *  "seller_user_id": 1, 
 
      *  "buyer_user_id": 1, 
 
      *  "create_timestamp": 946684800, 
 
      *  "created_timestamp": 946684800, 
 
      *  "paid_timestamp": 946684800, 
 
      *  "shipped_timestamp": 946684800, 
 
      *  "quantity": 0, 
 
      *  "listing_image_id": 1, 
 
      *  "receipt_id": 1, 
 
      *  "is_digital": true, 
 
      *  "file_data": "string", 
 
      *  "listing_id": 0, 
 
      *  "transaction_type": "string", 
 
      *  "product_id": 1, 
 
      *  "sku": "string", 
 
      *  "price": { 
        *  "amount": 0, 
 
        *  "divisor": 0, 
 
        *  "currency_code": "string" 
  }, 
 
      *  "shipping_cost": { 
        *  "amount": 0, 
 
        *  "divisor": 0, 
 
        *  "currency_code": "string" 
  }, 
 
      *  "variations": [
        *  { 
          *  "property_id": 0, 
 
          *  "value_id": 0, 
 
          *  "formatted_name": "string", 
 
          *  "formatted_value": "string", 
 
          *  "question_id": 0, 
 
          *  "mime_type": "image/jpeg" 
  } 
 ], 
 
      *  "product_data": [
        *  { 
          *  "property_id": 1, 
 
          *  "property_name": "string", 
 
          *  "scale_id": 1, 
 
          *  "scale_name": "string", 
 
          *  "value_ids": [
            * 1
 ], 
 
          *  "values": [
            * "string"
 ] 
  } 
 ], 
 
      *  "shipping_profile_id": 1, 
 
      *  "min_processing_days": 0, 
 
      *  "max_processing_days": 0, 
 
      *  "shipping_method": "string", 
 
      *  "shipping_upgrade": "string", 
 
      *  "expected_ship_date": 946684800, 
 
      *  "buyer_coupon": 0, 
 
      *  "shop_coupon": 0 
  } 
 ] 
 
 }`
##  [](https://developer.etsy.com/documentation/reference/#operation/getShopReceiptTransactionsByReceipt)getShopReceiptTransactionsByReceipt 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Retrieves the list of transactions associated with a specific receipt.
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)[oauth2](https://developer.etsy.com/documentation/reference/#section/Authentication/oauth2) (`transactions_r`) 
##### path Parameters  
|  shop_id required   |  integer <int64> >= 1  The unique positive non-zero numeric ID for an Etsy Shop.  |  
| --- | --- |  
|  receipt_id required   |  integer <int64> >= 1  The numeric ID for the [receipt](https://developer.etsy.com/documentation/reference#tag/Shop-Receipt) associated to this transaction.  |  
##### query Parameters  
| legacy  |  boolean This parameter needed to enable new parameters and response values related to processing profiles.  |  
| --- | --- |  
### Responses
**200**
A list of transactions
**400**
There was a problem with the request data. See the error message for details.
**401**
The request lacks valid authentication credentials. See the error message for details.
**403**
The request attempted to perform an operation it is not allowed to. See the error message for details.
**404**
A resource could not be found. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
get/v3/application/shops/{shop_id}/receipts/{receipt_id}/transactions
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/shops/{shop_id}/receipts/{receipt_id}/transactions
###  Response samples 
  * 200
  * 400
  * 401
  * 403
  * 404
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
 
  *  "count": 0, 
 
  *  "results": [
    *  { 
      *  "transaction_id": 1, 
 
      *  "title": "string", 
 
      *  "description": "string", 
 
      *  "seller_user_id": 1, 
 
      *  "buyer_user_id": 1, 
 
      *  "create_timestamp": 946684800, 
 
      *  "created_timestamp": 946684800, 
 
      *  "paid_timestamp": 946684800, 
 
      *  "shipped_timestamp": 946684800, 
 
      *  "quantity": 0, 
 
      *  "listing_image_id": 1, 
 
      *  "receipt_id": 1, 
 
      *  "is_digital": true, 
 
      *  "file_data": "string", 
 
      *  "listing_id": 0, 
 
      *  "transaction_type": "string", 
 
      *  "product_id": 1, 
 
      *  "sku": "string", 
 
      *  "price": { 
        *  "amount": 0, 
 
        *  "divisor": 0, 
 
        *  "currency_code": "string" 
  }, 
 
      *  "shipping_cost": { 
        *  "amount": 0, 
 
        *  "divisor": 0, 
 
        *  "currency_code": "string" 
  }, 
 
      *  "variations": [
        *  { 
          *  "property_id": 0, 
 
          *  "value_id": 0, 
 
          *  "formatted_name": "string", 
 
          *  "formatted_value": "string", 
 
          *  "question_id": 0, 
 
          *  "mime_type": "image/jpeg" 
  } 
 ], 
 
      *  "product_data": [
        *  { 
          *  "property_id": 1, 
 
          *  "property_name": "string", 
 
          *  "scale_id": 1, 
 
          *  "scale_name": "string", 
 
          *  "value_ids": [
            * 1
 ], 
 
          *  "values": [
            * "string"
 ] 
  } 
 ], 
 
      *  "shipping_profile_id": 1, 
 
      *  "min_processing_days": 0, 
 
      *  "max_processing_days": 0, 
 
      *  "shipping_method": "string", 
 
      *  "shipping_upgrade": "string", 
 
      *  "expected_ship_date": 946684800, 
 
      *  "buyer_coupon": 0, 
 
      *  "shop_coupon": 0 
  } 
 ] 
 
 }`
##  [](https://developer.etsy.com/documentation/reference/#operation/getShopReceiptTransaction)getShopReceiptTransaction 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Retrieves a transaction by transaction ID.
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)[oauth2](https://developer.etsy.com/documentation/reference/#section/Authentication/oauth2) (`transactions_r`) 
##### path Parameters  
|  shop_id required   |  integer <int64> >= 1  The unique positive non-zero numeric ID for an Etsy Shop.  |  
| --- | --- |  
|  transaction_id required   |  integer <int64> >= 1  The unique numeric ID for a transaction.  |  
### Responses
**200**
A single transaction
**400**
There was a problem with the request data. See the error message for details.
**401**
The request lacks valid authentication credentials. See the error message for details.
**403**
The request attempted to perform an operation it is not allowed to. See the error message for details.
**404**
A resource could not be found. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
get/v3/application/shops/{shop_id}/transactions/{transaction_id}
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/shops/{shop_id}/transactions/{transaction_id}
###  Response samples 
  * 200
  * 400
  * 401
  * 403
  * 404
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
 
  *  "transaction_id": 1, 
 
  *  "title": "string", 
 
  *  "description": "string", 
 
  *  "seller_user_id": 1, 
 
  *  "buyer_user_id": 1, 
 
  *  "create_timestamp": 946684800, 
 
  *  "created_timestamp": 946684800, 
 
  *  "paid_timestamp": 946684800, 
 
  *  "shipped_timestamp": 946684800, 
 
  *  "quantity": 0, 
 
  *  "listing_image_id": 1, 
 
  *  "receipt_id": 1, 
 
  *  "is_digital": true, 
 
  *  "file_data": "string", 
 
  *  "listing_id": 0, 
 
  *  "transaction_type": "string", 
 
  *  "product_id": 1, 
 
  *  "sku": "string", 
 
  *  "price": { 
    *  "amount": 0, 
 
    *  "divisor": 0, 
 
    *  "currency_code": "string" 
  }, 
 
  *  "shipping_cost": { 
    *  "amount": 0, 
 
    *  "divisor": 0, 
 
    *  "currency_code": "string" 
  }, 
 
  *  "variations": [
    *  { 
      *  "property_id": 0, 
 
      *  "value_id": 0, 
 
      *  "formatted_name": "string", 
 
      *  "formatted_value": "string", 
 
      *  "question_id": 0, 
 
      *  "mime_type": "image/jpeg" 
  } 
 ], 
 
  *  "product_data": [
    *  { 
      *  "property_id": 1, 
 
      *  "property_name": "string", 
 
      *  "scale_id": 1, 
 
      *  "scale_name": "string", 
 
      *  "value_ids": [
        * 1
 ], 
 
      *  "values": [
        * "string"
 ] 
  } 
 ], 
 
  *  "shipping_profile_id": 1, 
 
  *  "min_processing_days": 0, 
 
  *  "max_processing_days": 0, 
 
  *  "shipping_method": "string", 
 
  *  "shipping_upgrade": "string", 
 
  *  "expected_ship_date": 946684800, 
 
  *  "buyer_coupon": 0, 
 
  *  "shop_coupon": 0 
 
 }`
##  [](https://developer.etsy.com/documentation/reference/#operation/getShopReceiptTransactionsByShop)getShopReceiptTransactionsByShop 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Retrieves the list of transactions associated with a shop.
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)[oauth2](https://developer.etsy.com/documentation/reference/#section/Authentication/oauth2) (`transactions_r`) 
##### path Parameters  
|  shop_id required   |  integer <int64> >= 1  The unique positive non-zero numeric ID for an Etsy Shop.  |  
| --- | --- |  
##### query Parameters  
| limit  |  integer <int64> [ 1 .. 100 ]  Default:  25 The maximum number of results to return.  |  
| --- | --- |  
| offset  |  integer <int64> >= 0  Default:  0 The number of records to skip before selecting the first result.  |  
| legacy  |  boolean This parameter needed to enable new parameters and response values related to processing profiles.  |  
### Responses
**200**
A list of transactions
**401**
The request lacks valid authentication credentials. See the error message for details.
**403**
The request attempted to perform an operation it is not allowed to. See the error message for details.
**404**
A resource could not be found. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
get/v3/application/shops/{shop_id}/transactions
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/shops/{shop_id}/transactions
###  Response samples 
  * 200
  * 401
  * 403
  * 404
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
 
  *  "count": 0, 
 
  *  "results": [
    *  { 
      *  "transaction_id": 1, 
 
      *  "title": "string", 
 
      *  "description": "string", 
 
      *  "seller_user_id": 1, 
 
      *  "buyer_user_id": 1, 
 
      *  "create_timestamp": 946684800, 
 
      *  "created_timestamp": 946684800, 
 
      *  "paid_timestamp": 946684800, 
 
      *  "shipped_timestamp": 946684800, 
 
      *  "quantity": 0, 
 
      *  "listing_image_id": 1, 
 
      *  "receipt_id": 1, 
 
      *  "is_digital": true, 
 
      *  "file_data": "string", 
 
      *  "listing_id": 0, 
 
      *  "transaction_type": "string", 
 
      *  "product_id": 1, 
 
      *  "sku": "string", 
 
      *  "price": { 
        *  "amount": 0, 
 
        *  "divisor": 0, 
 
        *  "currency_code": "string" 
  }, 
 
      *  "shipping_cost": { 
        *  "amount": 0, 
 
        *  "divisor": 0, 
 
        *  "currency_code": "string" 
  }, 
 
      *  "variations": [
        *  { 
          *  "property_id": 0, 
 
          *  "value_id": 0, 
 
          *  "formatted_name": "string", 
 
          *  "formatted_value": "string", 
 
          *  "question_id": 0, 
 
          *  "mime_type": "image/jpeg" 
  } 
 ], 
 
      *  "product_data": [
        *  { 
          *  "property_id": 1, 
 
          *  "property_name": "string", 
 
          *  "scale_id": 1, 
 
          *  "scale_name": "string", 
 
          *  "value_ids": [
            * 1
 ], 
 
          *  "values": [
            * "string"
 ] 
  } 
 ], 
 
      *  "shipping_profile_id": 1, 
 
      *  "min_processing_days": 0, 
 
      *  "max_processing_days": 0, 
 
      *  "shipping_method": "string", 
 
      *  "shipping_upgrade": "string", 
 
      *  "expected_ship_date": 946684800, 
 
      *  "buyer_coupon": 0, 
 
      *  "shop_coupon": 0 
  } 
 ] 
 
 }`
#  [](https://developer.etsy.com/documentation/reference/#tag/Review)Review
##  [](https://developer.etsy.com/documentation/reference/#operation/getReviewsByListing)getReviewsByListing 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Open API V3 to retrieve the reviews for a listing given its ID.
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)
##### path Parameters  
|  listing_id required   |  integer <int64> >= 1  The numeric ID for the [listing](https://developer.etsy.com/documentation/reference#tag/ShopListing) associated to this transaction.  |  
| --- | --- |  
##### query Parameters  
| limit  |  integer <int64> [ 1 .. 100 ]  Default:  25 The maximum number of results to return.  |  
| --- | --- |  
| offset  |  integer <int64> >= 0  Default:  0 The number of records to skip before selecting the first result.  |  
| min_created  |  integer <int64> >= 946684800  Nullable  The earliest unix timestamp for when a record was created.  |  
| max_created  |  integer <int64> >= 946684800  Nullable  The latest unix timestamp for when a record was created.  |  
### Responses
**200**
A set of Transaction Reviews by Listing ID
**400**
There was a problem with the request data. See the error message for details.
**404**
A resource could not be found. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
get/v3/application/listings/{listing_id}/reviews
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/listings/{listing_id}/reviews
###  Response samples 
  * 200
  * 400
  * 404
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
 
  *  "count": 0, 
 
  *  "results": [
    *  { 
      *  "shop_id": 1, 
 
      *  "listing_id": 1, 
 
      *  "rating": 1, 
 
      *  "review": "string", 
 
      *  "language": "string", 
 
      *  "image_url_fullxfull": "string", 
 
      *  "create_timestamp": 946684800, 
 
      *  "created_timestamp": 946684800, 
 
      *  "update_timestamp": 946684800, 
 
      *  "updated_timestamp": 946684800 
  } 
 ] 
 
 }`
##  [](https://developer.etsy.com/documentation/reference/#operation/getReviewsByShop)getReviewsByShop 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Open API V3 to retrieve the reviews from a shop given its ID.
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)
##### path Parameters  
|  shop_id required   |  integer <int64> >= 1  The unique positive non-zero numeric ID for an Etsy Shop.  |  
| --- | --- |  
##### query Parameters  
| limit  |  integer <int64> [ 1 .. 100 ]  Default:  25 The maximum number of results to return.  |  
| --- | --- |  
| offset  |  integer <int64> >= 0  Default:  0 The number of records to skip before selecting the first result.  |  
| min_created  |  integer <int64> >= 946684800  Nullable  The earliest unix timestamp for when a record was created.  |  
| max_created  |  integer <int64> >= 946684800  Nullable  The latest unix timestamp for when a record was created.  |  
### Responses
**200**
A set of Transaction Reviews By Shop ID
**400**
There was a problem with the request data. See the error message for details.
**404**
A resource could not be found. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
get/v3/application/shops/{shop_id}/reviews
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/shops/{shop_id}/reviews
###  Response samples 
  * 200
  * 400
  * 404
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
 
  *  "count": 0, 
 
  *  "results": [
    *  { 
      *  "shop_id": 1, 
 
      *  "listing_id": 1, 
 
      *  "transaction_id": 1, 
 
      *  "buyer_user_id": 1, 
 
      *  "rating": 1, 
 
      *  "review": "", 
 
      *  "language": "string", 
 
      *  "image_url_fullxfull": "string", 
 
      *  "create_timestamp": 946684800, 
 
      *  "created_timestamp": 946684800, 
 
      *  "update_timestamp": 946684800, 
 
      *  "updated_timestamp": 946684800 
  } 
 ] 
 
 }`
#  [](https://developer.etsy.com/documentation/reference/#tag/Shop-HolidayPreferences)Shop HolidayPreferences
##  [](https://developer.etsy.com/documentation/reference/#operation/getHolidayPreferences)getHolidayPreferences 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Retrieves a list of holidays that are available to a shop to set a preference for. Currently only supported in the US and CA
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)[oauth2](https://developer.etsy.com/documentation/reference/#section/Authentication/oauth2) (`shops_r`) 
##### path Parameters  
|  shop_id required   |  integer <int64> >= 1  The unique positive non-zero numeric ID for an Etsy Shop.  |  
| --- | --- |  
### Responses
**200**
A list of holiday preferences
**400**
There was a problem with the request data. See the error message for details.
**403**
The request attempted to perform an operation it is not allowed to. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
get/v3/application/shops/{shop_id}/holiday-preferences
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/shops/{shop_id}/holiday-preferences
###  Response samples 
  * 200
  * 400
  * 403
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`[
  *  { 
    *  "shop_id": 1, 
 
    *  "holiday_id": 1, 
 
    *  "country_iso": "string", 
 
    *  "is_working": true, 
 
    *  "holiday_name": "string" 
  } 

 ]`
##  [](https://developer.etsy.com/documentation/reference/#operation/updateHolidayPreferences)updateHolidayPreferences 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Updates the preference for whether the seller will process orders or not on the holiday. Currently only supported in the US and CA
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)[oauth2](https://developer.etsy.com/documentation/reference/#section/Authentication/oauth2) (`shops_w`) 
##### path Parameters  
|  shop_id required   |  integer <int64> >= 1  The unique positive non-zero numeric ID for an Etsy Shop.  |  
| --- | --- |  
|  holiday_id required   |  integer <int64> Enum: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 The unique id that maps to the holiday a country observes. See the [Fulfillment Tutorial docs](https://developer.etsy.com/documentation/tutorials/fulfillment/#country-holidays) for more info  |  
##### Request Body schema: application/x-www-form-urlencoded  
|  is_working required   |  boolean A boolean value for whether the shop will process orders on a particular holiday.  |  
| --- | --- |  
### Responses
**200**
The updated holiday preferences
**400**
There was a problem with the request data. See the error message for details.
**403**
The request attempted to perform an operation it is not allowed to. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
put/v3/application/shops/{shop_id}/holiday-preferences/{holiday_id}
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/shops/{shop_id}/holiday-preferences/{holiday_id}
###  Response samples 
  * 200
  * 400
  * 403
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
 
  *  "shop_id": 1, 
 
  *  "holiday_id": 1, 
 
  *  "country_iso": "string", 
 
  *  "is_working": true, 
 
  *  "holiday_name": "string" 
 
 }`
#  [](https://developer.etsy.com/documentation/reference/#tag/Shop-ProcessingProfiles)Shop ProcessingProfiles
##  [](https://developer.etsy.com/documentation/reference/#operation/createShopReadinessStateDefinition)createShopReadinessStateDefinition 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Creates a new ReadinessStateDefinition. If an existing definition matches the input values, this endpoint will throw a Conflict error, please refer to the Content-Location header to obtain the get endpoint url for the values of the existing definition. Does not affect the product offering-readiness states definition relationship.
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)[oauth2](https://developer.etsy.com/documentation/reference/#section/Authentication/oauth2) (`shops_w`) 
##### path Parameters  
|  shop_id required   |  integer <int64> >= 1  The unique positive non-zero numeric ID for an Etsy Shop.  |  
| --- | --- |  
##### Request Body schema: application/x-www-form-urlencoded  
|  readiness_state required   |  string Enum: "ready_to_ship" "made_to_order" The readiness state of a product: "1" means "ready_to_ship", and "2" means "made_to_order"  |  
| --- | --- |  
|  min_processing_time required   |  integer <int64> [ 1 .. 10 ]  The minimum number of days or weeks for processing a specific product.  |  
|  max_processing_time required   |  integer <int64> [ 1 .. 10 ]  The maximum number of days or weeks for processing a specific product.  |  
| processing_time_unit  |  string Default:  "days" Enum: "days" "weeks" The unit used to represent how long a processing time is. A week is equivalent to how many days the seller works per week as stated in their processing schedule. If none is provided, the unit is set to "days".  |  
### Responses
**201**
A single ReadinessStateDefinition
**400**
There was a problem with the request data. See the error message for details.
**401**
The request lacks valid authentication credentials. See the error message for details.
**409**
There was a request conflict with the current state of the target resource. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
post/v3/application/shops/{shop_id}/readiness-state-definitions
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/shops/{shop_id}/readiness-state-definitions
###  Response samples 
  * 201
  * 400
  * 401
  * 409
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
 
  *  "shop_id": 1, 
 
  *  "readiness_state_id": 1, 
 
  *  "readiness_state": "ready_to_ship", 
 
  *  "min_processing_days": 0, 
 
  *  "max_processing_days": 0, 
 
  *  "processing_days_display_label": "string" 
 
 }`
##  [](https://developer.etsy.com/documentation/reference/#operation/getShopReadinessStateDefinitions)getShopReadinessStateDefinitions 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Retrieves a list of ProcessingProfiles available in the specific Etsy shop identified by its shop ID.
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)[oauth2](https://developer.etsy.com/documentation/reference/#section/Authentication/oauth2) (`shops_r`) 
##### path Parameters  
|  shop_id required   |  integer <int64> >= 1  The unique positive non-zero numeric ID for an Etsy Shop.  |  
| --- | --- |  
##### query Parameters  
| limit  |  integer <int64> [ 1 .. 100 ]  Default:  25 The maximum number of results to return.  |  
| --- | --- |  
| offset  |  integer <int64> >= 0  Default:  0 The number of records to skip before selecting the first result.  |  
### Responses
**200**
A list of ProcessingProfiles
**400**
There was a problem with the request data. See the error message for details.
**401**
The request lacks valid authentication credentials. See the error message for details.
**404**
A resource could not be found. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
get/v3/application/shops/{shop_id}/readiness-state-definitions
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/shops/{shop_id}/readiness-state-definitions
###  Response samples 
  * 200
  * 400
  * 401
  * 404
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
 
  *  "count": 0, 
 
  *  "results": [
    *  { 
      *  "shop_id": 1, 
 
      *  "readiness_state_id": 1, 
 
      *  "readiness_state": "ready_to_ship", 
 
      *  "min_processing_days": 0, 
 
      *  "max_processing_days": 0, 
 
      *  "processing_days_display_label": "string" 
  } 
 ] 
 
 }`
##  [](https://developer.etsy.com/documentation/reference/#operation/deleteShopReadinessStateDefinition)deleteShopReadinessStateDefinition 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Deletes a ReadinessStateDefinition by given readiness state definition ID. If there any active offerings linked to the definition, this endpoint will throw a Bad Request error. If you want to delete a ReadinessStateDefinition that is linked to active offerings, you must link the offerings to a different readiness state definition.
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)[oauth2](https://developer.etsy.com/documentation/reference/#section/Authentication/oauth2) (`shops_w`) 
##### path Parameters  
|  shop_id required   |  integer <int64> >= 1  The unique positive non-zero numeric ID for an Etsy Shop.  |  
| --- | --- |  
|  readiness_state_definition_id required   |  integer <int64> >= 1  The numeric ID of the [processing profile](https://developer.etsy.com/documentation/reference#operation/getShopReadinessStateDefinition) associated with the listing. Returned only when the listing is `active` and of type `physical`, and the endpoint is either shop-scoped (path contains `shop_id`) or a single-listing request such as `getListing`. For every other case this field can be null.  |  
### Responses
**204**
The ReadinessStateDefinition was successfully deleted
**400**
There was a problem with the request data. See the error message for details.
**401**
The request lacks valid authentication credentials. See the error message for details.
**403**
The request attempted to perform an operation it is not allowed to. See the error message for details.
**404**
A resource could not be found. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
delete/v3/application/shops/{shop_id}/readiness-state-definitions/{readiness_state_definition_id}
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/shops/{shop_id}/readiness-state-definitions/{readiness_state_definition_id}
###  Response samples 
  * 400
  * 401
  * 403
  * 404
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
  *  "error": "string" 

 }`
##  [](https://developer.etsy.com/documentation/reference/#operation/getShopReadinessStateDefinition)getShopReadinessStateDefinition 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Retrieves a ProcessingProfile referenced by readiness state definition ID.
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)[oauth2](https://developer.etsy.com/documentation/reference/#section/Authentication/oauth2) (`shops_r`) 
##### path Parameters  
|  shop_id required   |  integer <int64> >= 1  The unique positive non-zero numeric ID for an Etsy Shop.  |  
| --- | --- |  
|  readiness_state_definition_id required   |  integer <int64> >= 1  The numeric ID of the [processing profile](https://developer.etsy.com/documentation/reference#operation/getShopReadinessStateDefinition) associated with the listing. Returned only when the listing is `active` and of type `physical`, and the endpoint is either shop-scoped (path contains `shop_id`) or a single-listing request such as `getListing`. For every other case this field can be null.  |  
### Responses
**200**
A single ProcessingProfile
**400**
There was a problem with the request data. See the error message for details.
**401**
The request lacks valid authentication credentials. See the error message for details.
**404**
A resource could not be found. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
get/v3/application/shops/{shop_id}/readiness-state-definitions/{readiness_state_definition_id}
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/shops/{shop_id}/readiness-state-definitions/{readiness_state_definition_id}
###  Response samples 
  * 200
  * 400
  * 401
  * 404
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
 
  *  "shop_id": 1, 
 
  *  "readiness_state_id": 1, 
 
  *  "readiness_state": "ready_to_ship", 
 
  *  "min_processing_days": 0, 
 
  *  "max_processing_days": 0, 
 
  *  "processing_days_display_label": "string" 
 
 }`
##  [](https://developer.etsy.com/documentation/reference/#operation/updateShopReadinessStateDefinition)updateShopReadinessStateDefinition 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Updates an existing ReadinessStateDefinition. If an existing definition matches the input values, this endpoint will throw a Conflict error, please refer to the Content-Location header to obtain the get endpoint url for the values of the existing definition. Does not affect the product offering-readiness states definition relationship.
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)[oauth2](https://developer.etsy.com/documentation/reference/#section/Authentication/oauth2) (`shops_w`) 
##### path Parameters  
|  shop_id required   |  integer <int64> >= 1  The unique positive non-zero numeric ID for an Etsy Shop.  |  
| --- | --- |  
|  readiness_state_definition_id required   |  integer <int64> >= 1  The numeric ID of the [processing profile](https://developer.etsy.com/documentation/reference#operation/getShopReadinessStateDefinition) associated with the listing. Returned only when the listing is `active` and of type `physical`, and the endpoint is either shop-scoped (path contains `shop_id`) or a single-listing request such as `getListing`. For every other case this field can be null.  |  
##### Request Body schema: application/x-www-form-urlencoded  
| readiness_state  |  string Enum: "ready_to_ship" "made_to_order" The readiness state of a product: "1" means "ready_to_ship", and "2" means "made_to_order"  |  
| --- | --- |  
| min_processing_time  |  integer <int64> [ 1 .. 10 ]  The minimum number of days or weeks for processing a specific product.  |  
| max_processing_time  |  integer <int64> [ 1 .. 10 ]  The maximum number of days or weeks for processing a specific product.  |  
| processing_time_unit  |  string Default:  "days" Enum: "days" "weeks" The unit used to represent how long a processing time is. A week is equivalent to how many days the seller works per week as stated in their processing schedule. If none is provided, the unit is set to "days".  |  
### Responses
**200**
The updated ReadinessStateDefinition
**400**
There was a problem with the request data. See the error message for details.
**401**
The request lacks valid authentication credentials. See the error message for details.
**404**
A resource could not be found. See the error message for details.
**409**
There was a request conflict with the current state of the target resource. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
put/v3/application/shops/{shop_id}/readiness-state-definitions/{readiness_state_definition_id}
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/shops/{shop_id}/readiness-state-definitions/{readiness_state_definition_id}
###  Response samples 
  * 200
  * 400
  * 401
  * 404
  * 409
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
 
  *  "shop_id": 1, 
 
  *  "readiness_state_id": 1, 
 
  *  "readiness_state": "ready_to_ship", 
 
  *  "min_processing_days": 0, 
 
  *  "max_processing_days": 0, 
 
  *  "processing_days_display_label": "string" 
 
 }`
#  [](https://developer.etsy.com/documentation/reference/#tag/Shop-ShippingProfile)Shop ShippingProfile
##  [](https://developer.etsy.com/documentation/reference/#operation/getShippingCarriers)getShippingCarriers 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Retrieves a list of available shipping carriers and the mail classes associated with them for a given country
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)
##### query Parameters  
|  origin_country_iso required   |  string <ISO 3166-1 alpha-2> The ISO code of the country from which the listing ships.  |  
| --- | --- |  
### Responses
**200**
A set of ShippingCarriers
**400**
There was a problem with the request data. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
get/v3/application/shipping-carriers
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/shipping-carriers
###  Response samples 
  * 200
  * 400
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
 
  *  "count": 0, 
 
  *  "results": [
    *  { 
      *  "shipping_carrier_id": 1, 
 
      *  "name": "string", 
 
      *  "domestic_classes": [
        *  { 
          *  "mail_class_key": "string", 
 
          *  "name": "string" 
  } 
 ], 
 
      *  "international_classes": [
        *  { 
          *  "mail_class_key": "string", 
 
          *  "name": "string" 
  } 
 ] 
  } 
 ] 
 
 }`
##  [](https://developer.etsy.com/documentation/reference/#operation/createShopShippingProfile)createShopShippingProfile 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Creates a new ShippingProfile. You can pass a country iso code or a region when creating a ShippingProfile, but not both. Only one is required. You must pass either a shipping_carrier_id AND mail_class, or both min and max_delivery_days.
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)[oauth2](https://developer.etsy.com/documentation/reference/#section/Authentication/oauth2) (`shops_w`) 
##### path Parameters  
|  shop_id required   |  integer <int64> >= 1  The unique positive non-zero numeric ID for an Etsy Shop.  |  
| --- | --- |  
##### Request Body schema: application/x-www-form-urlencoded  
|  title required   |  string The name string of this shipping profile.  |  
| --- | --- |  
|  origin_country_iso required   |  string <ISO 3166-1 alpha-2> The ISO code of the country from which the listing ships.  |  
|  primary_cost required   |  number <float> >= 0  The cost of shipping to this country/region alone, measured in the store's default currency.  |  
|  secondary_cost required   |  number <float> >= 0  The cost of shipping to this country/region with another item, measured in the store's default currency.  |  
| min_processing_time  |  integer <int64> [ 1 .. 10 ]  The minimum time required to process to ship listings with this shipping profile.  |  
| max_processing_time  |  integer <int64> [ 1 .. 10 ]  The maximum processing time the listing needs to ship.  |  
| processing_time_unit  |  string Default:  "business_days" Enum: "business_days" "weeks" The unit used to represent how long a processing time is. A week is equivalent to the set processing schedule (default to 5 business days). If none is provided, the unit is set to "business_days".  |  
| destination_country_iso  |  string <ISO 3166-1 alpha-2> Default:  null The ISO code of the country to which the listing ships. If null, request sets destination to destination_region. Required if destination_region is null or not provided.  |  
| destination_region  |  string Default:  "none" Enum: "eu" "non_eu" "none" The code of the region to which the listing ships. A region represents a set of countries. Supported regions are Europe Union and Non-Europe Union (countries in Europe not in EU). If `none`, request sets destination to destination_country_iso. Required if destination_country_iso is null or not provided.  |  
| origin_postal_code  |  string Default:  "" The postal code string (not necessarily a number) for the location from which the listing ships. Required if the `origin_country_iso` supports postal codes. See the [Fulfillment Tutorial docs](https://developer.etsy.com/documentation/tutorials/fulfillment/#countries-requiring-postal-codes) for more info  |  
| shipping_carrier_id  |  integer <int64> >= 0  Default:  0 The unique ID of a supported shipping carrier, which is used to calculate an Estimated Delivery Date. **Required with`mail_class`** if `min_delivery_days` and `max_delivery_days` are null.  |  
| mail_class  |  string Default:  null The unique ID string of a shipping carrier's mail class, which is used to calculate an estimated delivery date. **Required with`shipping_carrier_id`** if `min_delivery_days` and `max_delivery_days` are null.  |  
| min_delivery_days  |  integer <int64> [ 1 .. 45 ]  Default:  null The minimum number of business days a buyer can expect to wait to receive their purchased item once it has shipped. **Required with`max_delivery_days`** if `mail_class` is null.  |  
| max_delivery_days  |  integer <int64> [ 1 .. 45 ]  Default:  null The maximum number of business days a buyer can expect to wait to receive their purchased item once it has shipped. **Required with`min_delivery_days`** if `mail_class` is null.  |  
### Responses
**200**
A single ShippingProfile
**400**
There was a problem with the request data. See the error message for details.
**401**
The request lacks valid authentication credentials. See the error message for details.
**403**
The request attempted to perform an operation it is not allowed to. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
post/v3/application/shops/{shop_id}/shipping-profiles
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/shops/{shop_id}/shipping-profiles
###  Response samples 
  * 200
  * 400
  * 401
  * 403
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
 
  *  "shipping_profile_id": 1, 
 
  *  "title": "string", 
 
  *  "user_id": 1, 
 
  *  "origin_country_iso": "string", 
 
  *  "is_deleted": true, 
 
  *  "shipping_profile_destinations": [
    *  { 
      *  "shipping_profile_destination_id": 1, 
 
      *  "shipping_profile_id": 1, 
 
      *  "origin_country_iso": "string", 
 
      *  "destination_country_iso": "string", 
 
      *  "destination_region": "eu", 
 
      *  "primary_cost": { 
        *  "amount": 0, 
 
        *  "divisor": 0, 
 
        *  "currency_code": "string" 
  }, 
 
      *  "secondary_cost": { 
        *  "amount": 0, 
 
        *  "divisor": 0, 
 
        *  "currency_code": "string" 
  }, 
 
      *  "shipping_carrier_id": 0, 
 
      *  "mail_class": "string", 
 
      *  "min_delivery_days": 1, 
 
      *  "max_delivery_days": 1 
  } 
 ], 
 
  *  "shipping_profile_upgrades": [
    *  { 
      *  "shipping_profile_id": 1, 
 
      *  "upgrade_id": 1, 
 
      *  "upgrade_name": "string", 
 
      *  "type": 0, 
 
      *  "rank": 0, 
 
      *  "language": "string", 
 
      *  "price": { 
        *  "amount": 0, 
 
        *  "divisor": 0, 
 
        *  "currency_code": "string" 
  }, 
 
      *  "secondary_price": { 
        *  "amount": 0, 
 
        *  "divisor": 0, 
 
        *  "currency_code": "string" 
  }, 
 
      *  "shipping_carrier_id": 0, 
 
      *  "mail_class": "string", 
 
      *  "min_delivery_days": 1, 
 
      *  "max_delivery_days": 1 
  } 
 ], 
 
  *  "origin_postal_code": "string", 
 
  *  "profile_type": "manual", 
 
  *  "domestic_handling_fee": 0, 
 
  *  "international_handling_fee": 0 
 
 }`
##  [](https://developer.etsy.com/documentation/reference/#operation/getShopShippingProfiles)getShopShippingProfiles 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Retrieves a list of shipping profiles available in the specific Etsy shop identified by its shop ID.
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)[oauth2](https://developer.etsy.com/documentation/reference/#section/Authentication/oauth2) (`shops_r`) 
##### path Parameters  
|  shop_id required   |  integer <int64> >= 1  The unique positive non-zero numeric ID for an Etsy Shop.  |  
| --- | --- |  
### Responses
**200**
A list of shipping profiles
**400**
There was a problem with the request data. See the error message for details.
**403**
The request attempted to perform an operation it is not allowed to. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
get/v3/application/shops/{shop_id}/shipping-profiles
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/shops/{shop_id}/shipping-profiles
###  Response samples 
  * 200
  * 400
  * 403
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
 
  *  "count": 0, 
 
  *  "results": [
    *  { 
      *  "shipping_profile_id": 1, 
 
      *  "title": "string", 
 
      *  "user_id": 1, 
 
      *  "origin_country_iso": "string", 
 
      *  "is_deleted": true, 
 
      *  "shipping_profile_destinations": [
        *  { 
          *  "shipping_profile_destination_id": 1, 
 
          *  "shipping_profile_id": 1, 
 
          *  "origin_country_iso": "string", 
 
          *  "destination_country_iso": "string", 
 
          *  "destination_region": "eu", 
 
          *  "primary_cost": { 
            *  "amount": 0, 
 
            *  "divisor": 0, 
 
            *  "currency_code": "string" 
  }, 
 
          *  "secondary_cost": { 
            *  "amount": 0, 
 
            *  "divisor": 0, 
 
            *  "currency_code": "string" 
  }, 
 
          *  "shipping_carrier_id": 0, 
 
          *  "mail_class": "string", 
 
          *  "min_delivery_days": 1, 
 
          *  "max_delivery_days": 1 
  } 
 ], 
 
      *  "shipping_profile_upgrades": [
        *  { 
          *  "shipping_profile_id": 1, 
 
          *  "upgrade_id": 1, 
 
          *  "upgrade_name": "string", 
 
          *  "type": 0, 
 
          *  "rank": 0, 
 
          *  "language": "string", 
 
          *  "price": { 
            *  "amount": 0, 
 
            *  "divisor": 0, 
 
            *  "currency_code": "string" 
  }, 
 
          *  "secondary_price": { 
            *  "amount": 0, 
 
            *  "divisor": 0, 
 
            *  "currency_code": "string" 
  }, 
 
          *  "shipping_carrier_id": 0, 
 
          *  "mail_class": "string", 
 
          *  "min_delivery_days": 1, 
 
          *  "max_delivery_days": 1 
  } 
 ], 
 
      *  "origin_postal_code": "string", 
 
      *  "profile_type": "manual", 
 
      *  "domestic_handling_fee": 0, 
 
      *  "international_handling_fee": 0 
  } 
 ] 
 
 }`
##  [](https://developer.etsy.com/documentation/reference/#operation/deleteShopShippingProfile)deleteShopShippingProfile 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Deletes a ShippingProfile by given id.
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)[oauth2](https://developer.etsy.com/documentation/reference/#section/Authentication/oauth2) (`shops_w`) 
##### path Parameters  
|  shop_id required   |  integer <int64> >= 1  The unique positive non-zero numeric ID for an Etsy Shop.  |  
| --- | --- |  
|  shipping_profile_id required   |  integer <int64> >= 1  The numeric ID of the [shipping profile](https://developer.etsy.com/documentation/reference#operation/getShopShippingProfile) associated with the listing. Required when listing type is `physical`.  |  
### Responses
**204**
The ShopShippingProfile resource was correctly deleted
**400**
There was a problem with the request data. See the error message for details.
**401**
The request lacks valid authentication credentials. See the error message for details.
**403**
The request attempted to perform an operation it is not allowed to. See the error message for details.
**404**
A resource could not be found. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
delete/v3/application/shops/{shop_id}/shipping-profiles/{shipping_profile_id}
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/shops/{shop_id}/shipping-profiles/{shipping_profile_id}
###  Response samples 
  * 400
  * 401
  * 403
  * 404
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
  *  "error": "string" 

 }`
##  [](https://developer.etsy.com/documentation/reference/#operation/getShopShippingProfile)getShopShippingProfile 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Retrieves a Shipping Profile referenced by shipping profile ID.
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)[oauth2](https://developer.etsy.com/documentation/reference/#section/Authentication/oauth2) (`shops_r`) 
##### path Parameters  
|  shop_id required   |  integer <int64> >= 1  The unique positive non-zero numeric ID for an Etsy Shop.  |  
| --- | --- |  
|  shipping_profile_id required   |  integer <int64> >= 1  The numeric ID of the [shipping profile](https://developer.etsy.com/documentation/reference#operation/getShopShippingProfile) associated with the listing. Required when listing type is `physical`.  |  
### Responses
**200**
A single ShippingProfile
**400**
There was a problem with the request data. See the error message for details.
**401**
The request lacks valid authentication credentials. See the error message for details.
**403**
The request attempted to perform an operation it is not allowed to. See the error message for details.
**404**
A resource could not be found. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
get/v3/application/shops/{shop_id}/shipping-profiles/{shipping_profile_id}
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/shops/{shop_id}/shipping-profiles/{shipping_profile_id}
###  Response samples 
  * 200
  * 400
  * 401
  * 403
  * 404
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
 
  *  "shipping_profile_id": 1, 
 
  *  "title": "string", 
 
  *  "user_id": 1, 
 
  *  "origin_country_iso": "string", 
 
  *  "is_deleted": true, 
 
  *  "shipping_profile_destinations": [
    *  { 
      *  "shipping_profile_destination_id": 1, 
 
      *  "shipping_profile_id": 1, 
 
      *  "origin_country_iso": "string", 
 
      *  "destination_country_iso": "string", 
 
      *  "destination_region": "eu", 
 
      *  "primary_cost": { 
        *  "amount": 0, 
 
        *  "divisor": 0, 
 
        *  "currency_code": "string" 
  }, 
 
      *  "secondary_cost": { 
        *  "amount": 0, 
 
        *  "divisor": 0, 
 
        *  "currency_code": "string" 
  }, 
 
      *  "shipping_carrier_id": 0, 
 
      *  "mail_class": "string", 
 
      *  "min_delivery_days": 1, 
 
      *  "max_delivery_days": 1 
  } 
 ], 
 
  *  "shipping_profile_upgrades": [
    *  { 
      *  "shipping_profile_id": 1, 
 
      *  "upgrade_id": 1, 
 
      *  "upgrade_name": "string", 
 
      *  "type": 0, 
 
      *  "rank": 0, 
 
      *  "language": "string", 
 
      *  "price": { 
        *  "amount": 0, 
 
        *  "divisor": 0, 
 
        *  "currency_code": "string" 
  }, 
 
      *  "secondary_price": { 
        *  "amount": 0, 
 
        *  "divisor": 0, 
 
        *  "currency_code": "string" 
  }, 
 
      *  "shipping_carrier_id": 0, 
 
      *  "mail_class": "string", 
 
      *  "min_delivery_days": 1, 
 
      *  "max_delivery_days": 1 
  } 
 ], 
 
  *  "origin_postal_code": "string", 
 
  *  "profile_type": "manual", 
 
  *  "domestic_handling_fee": 0, 
 
  *  "international_handling_fee": 0 
 
 }`
##  [](https://developer.etsy.com/documentation/reference/#operation/updateShopShippingProfile)updateShopShippingProfile 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Changes the settings in a shipping profile. You can pass a country iso code or a region when updating a ShippingProfile, but not both. Only one is required. You must pass either a shipping_carrier_id AND mail_class, or both min and max_delivery_days.
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)[oauth2](https://developer.etsy.com/documentation/reference/#section/Authentication/oauth2) (`shops_w`) 
##### path Parameters  
|  shop_id required   |  integer <int64> >= 1  The unique positive non-zero numeric ID for an Etsy Shop.  |  
| --- | --- |  
|  shipping_profile_id required   |  integer <int64> >= 1  The numeric ID of the [shipping profile](https://developer.etsy.com/documentation/reference#operation/getShopShippingProfile) associated with the listing. Required when listing type is `physical`.  |  
##### Request Body schema: application/x-www-form-urlencoded  
| title  |  string The name string of this shipping profile.  |  
| --- | --- |  
| origin_country_iso  |  string <ISO 3166-1 alpha-2> The ISO code of the country from which the listing ships.  |  
| min_processing_time  |  integer <int64> [ 1 .. 10 ]  The minimum time required to process to ship listings with this shipping profile.  |  
| max_processing_time  |  integer <int64> [ 1 .. 10 ]  The maximum processing time the listing needs to ship.  |  
| processing_time_unit  |  string Default:  "business_days" Enum: "business_days" "weeks" The unit used to represent how long a processing time is. A week is equivalent to the set processing schedule (default to 5 business days). If none is provided, the unit is set to "business_days".  |  
| origin_postal_code  |  string Default:  null The postal code string (not necessarily a number) for the location from which the listing ships. Required if the `origin_country_iso` supports postal codes. See the [Fulfillment Tutorial docs](https://developer.etsy.com/documentation/tutorials/fulfillment/#countries-requiring-postal-codes) for more info  |  
### Responses
**200**
The updated shipping profile.
**400**
There was a problem with the request data. See the error message for details.
**401**
The request lacks valid authentication credentials. See the error message for details.
**403**
The request attempted to perform an operation it is not allowed to. See the error message for details.
**404**
A resource could not be found. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
**503**
This function is temporarily unavailable. Please try again later.
put/v3/application/shops/{shop_id}/shipping-profiles/{shipping_profile_id}
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/shops/{shop_id}/shipping-profiles/{shipping_profile_id}
###  Response samples 
  * 200
  * 400
  * 401
  * 403
  * 404
  * 500
  * 503


Content type
application/json
Copy
Expand all  Collapse all 
`{
 
  *  "shipping_profile_id": 1, 
 
  *  "title": "string", 
 
  *  "user_id": 1, 
 
  *  "origin_country_iso": "string", 
 
  *  "is_deleted": true, 
 
  *  "shipping_profile_destinations": [
    *  { 
      *  "shipping_profile_destination_id": 1, 
 
      *  "shipping_profile_id": 1, 
 
      *  "origin_country_iso": "string", 
 
      *  "destination_country_iso": "string", 
 
      *  "destination_region": "eu", 
 
      *  "primary_cost": { 
        *  "amount": 0, 
 
        *  "divisor": 0, 
 
        *  "currency_code": "string" 
  }, 
 
      *  "secondary_cost": { 
        *  "amount": 0, 
 
        *  "divisor": 0, 
 
        *  "currency_code": "string" 
  }, 
 
      *  "shipping_carrier_id": 0, 
 
      *  "mail_class": "string", 
 
      *  "min_delivery_days": 1, 
 
      *  "max_delivery_days": 1 
  } 
 ], 
 
  *  "shipping_profile_upgrades": [
    *  { 
      *  "shipping_profile_id": 1, 
 
      *  "upgrade_id": 1, 
 
      *  "upgrade_name": "string", 
 
      *  "type": 0, 
 
      *  "rank": 0, 
 
      *  "language": "string", 
 
      *  "price": { 
        *  "amount": 0, 
 
        *  "divisor": 0, 
 
        *  "currency_code": "string" 
  }, 
 
      *  "secondary_price": { 
        *  "amount": 0, 
 
        *  "divisor": 0, 
 
        *  "currency_code": "string" 
  }, 
 
      *  "shipping_carrier_id": 0, 
 
      *  "mail_class": "string", 
 
      *  "min_delivery_days": 1, 
 
      *  "max_delivery_days": 1 
  } 
 ], 
 
  *  "origin_postal_code": "string", 
 
  *  "profile_type": "manual", 
 
  *  "domestic_handling_fee": 0, 
 
  *  "international_handling_fee": 0 
 
 }`
##  [](https://developer.etsy.com/documentation/reference/#operation/createShopShippingProfileDestination)createShopShippingProfileDestination 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Creates a new shipping destination, which sets the shipping cost, carrier, and class for a destination in a [shipping profile](https://developer.etsy.com/documentation/reference/#tag/Shop-ShippingProfile). createShopShippingProfileDestination assigns costs using the currency of the associated shop. Set the destination using either `destination_country_iso` or `destination_region`; `destination_country_iso` and `destination_region` are mutually exclusive — set one or the other. Setting both triggers error 400. If the request sets neither `destination_country_iso` nor `destination_region`, the default destination is "everywhere". You must also either assign both a `shipping_carrier_id` AND `mail_class` or both `min_delivery_days` AND `max_delivery_days`.
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)[oauth2](https://developer.etsy.com/documentation/reference/#section/Authentication/oauth2) (`shops_w`) 
##### path Parameters  
|  shop_id required   |  integer <int64> >= 1  The unique positive non-zero numeric ID for an Etsy Shop.  |  
| --- | --- |  
|  shipping_profile_id required   |  integer <int64> >= 1  The numeric ID of the [shipping profile](https://developer.etsy.com/documentation/reference#operation/getShopShippingProfile) associated with the listing. Required when listing type is `physical`.  |  
##### Request Body schema: application/x-www-form-urlencoded  
|  primary_cost required   |  number <float> >= 0  The cost of shipping to this country/region alone, measured in the store's default currency.  |  
| --- | --- |  
|  secondary_cost required   |  number <float> >= 0  The cost of shipping to this country/region with another item, measured in the store's default currency.  |  
| destination_country_iso  |  string <ISO 3166-1 alpha-2> Default:  null The ISO code of the country to which the listing ships. If null, request sets destination to destination_region. Required if destination_region is null or not provided.  |  
| destination_region  |  string Default:  "none" Enum: "eu" "non_eu" "none" The code of the region to which the listing ships. A region represents a set of countries. Supported regions are Europe Union and Non-Europe Union (countries in Europe not in EU). If `none`, request sets destination to destination_country_iso. Required if destination_country_iso is null or not provided.  |  
| shipping_carrier_id  |  integer <int64> >= 0  Default:  0 The unique ID of a supported shipping carrier, which is used to calculate an Estimated Delivery Date. **Required with`mail_class`** if `min_delivery_days` and `max_delivery_days` are null.  |  
| mail_class  |  string Default:  null The unique ID string of a shipping carrier's mail class, which is used to calculate an estimated delivery date. **Required with`shipping_carrier_id`** if `min_delivery_days` and `max_delivery_days` are null.  |  
| min_delivery_days  |  integer <int64> [ 1 .. 45 ]  Default:  null The minimum number of business days a buyer can expect to wait to receive their purchased item once it has shipped. **Required with`max_delivery_days`** if `mail_class` is null.  |  
| max_delivery_days  |  integer <int64> [ 1 .. 45 ]  Default:  null The maximum number of business days a buyer can expect to wait to receive their purchased item once it has shipped. **Required with`min_delivery_days`** if `mail_class` is null.  |  
### Responses
**201**
A single shipping destination.
**400**
There was a problem with the request data. See the error message for details.
**401**
The request lacks valid authentication credentials. See the error message for details.
**403**
The request attempted to perform an operation it is not allowed to. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
post/v3/application/shops/{shop_id}/shipping-profiles/{shipping_profile_id}/destinations
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/shops/{shop_id}/shipping-profiles/{shipping_profile_id}/destinations
###  Response samples 
  * 201
  * 400
  * 401
  * 403
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
 
  *  "shipping_profile_destination_id": 1, 
 
  *  "shipping_profile_id": 1, 
 
  *  "origin_country_iso": "string", 
 
  *  "destination_country_iso": "string", 
 
  *  "destination_region": "eu", 
 
  *  "primary_cost": { 
    *  "amount": 0, 
 
    *  "divisor": 0, 
 
    *  "currency_code": "string" 
  }, 
 
  *  "secondary_cost": { 
    *  "amount": 0, 
 
    *  "divisor": 0, 
 
    *  "currency_code": "string" 
  }, 
 
  *  "shipping_carrier_id": 0, 
 
  *  "mail_class": "string", 
 
  *  "min_delivery_days": 1, 
 
  *  "max_delivery_days": 1 
 
 }`
##  [](https://developer.etsy.com/documentation/reference/#operation/getShopShippingProfileDestinationsByShippingProfile)getShopShippingProfileDestinationsByShippingProfile 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Retrieves a list of shipping destination objects associated with a shipping profile.
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)[oauth2](https://developer.etsy.com/documentation/reference/#section/Authentication/oauth2) (`shops_r`) 
##### path Parameters  
|  shop_id required   |  integer <int64> >= 1  The unique positive non-zero numeric ID for an Etsy Shop.  |  
| --- | --- |  
|  shipping_profile_id required   |  integer <int64> >= 1  The numeric ID of the [shipping profile](https://developer.etsy.com/documentation/reference#operation/getShopShippingProfile) associated with the listing. Required when listing type is `physical`.  |  
##### query Parameters  
| limit  |  integer <int64> [ 1 .. 100 ]  Default:  25 The maximum number of results to return.  |  
| --- | --- |  
| offset  |  integer <int64> >= 0  Default:  0 The number of records to skip before selecting the first result.  |  
### Responses
**200**
A list of shipping destination objects.
**400**
There was a problem with the request data. See the error message for details.
**401**
The request lacks valid authentication credentials. See the error message for details.
**403**
The request attempted to perform an operation it is not allowed to. See the error message for details.
**404**
A resource could not be found. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
get/v3/application/shops/{shop_id}/shipping-profiles/{shipping_profile_id}/destinations
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/shops/{shop_id}/shipping-profiles/{shipping_profile_id}/destinations
###  Response samples 
  * 200
  * 400
  * 401
  * 403
  * 404
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
 
  *  "count": 0, 
 
  *  "results": [
    *  { 
      *  "shipping_profile_destination_id": 1, 
 
      *  "shipping_profile_id": 1, 
 
      *  "origin_country_iso": "string", 
 
      *  "destination_country_iso": "string", 
 
      *  "destination_region": "eu", 
 
      *  "primary_cost": { 
        *  "amount": 0, 
 
        *  "divisor": 0, 
 
        *  "currency_code": "string" 
  }, 
 
      *  "secondary_cost": { 
        *  "amount": 0, 
 
        *  "divisor": 0, 
 
        *  "currency_code": "string" 
  }, 
 
      *  "shipping_carrier_id": 0, 
 
      *  "mail_class": "string", 
 
      *  "min_delivery_days": 1, 
 
      *  "max_delivery_days": 1 
  } 
 ] 
 
 }`
##  [](https://developer.etsy.com/documentation/reference/#operation/deleteShopShippingProfileDestination)deleteShopShippingProfileDestination 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Deletes a shipping destination and removes the destination option from every listing that uses the associated shipping profile. A shipping profile requires at least one shipping destination, so this endpoint cannot delete the final shipping destination for any shipping profile. To delete the final shipping destination from a shipping profile, you must [delete the entire shipping profile](https://developer.etsy.com/documentation/reference/#operation/deleteShopShippingProfile).
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)[oauth2](https://developer.etsy.com/documentation/reference/#section/Authentication/oauth2) (`shops_w`) 
##### path Parameters  
|  shop_id required   |  integer <int64> >= 1  The unique positive non-zero numeric ID for an Etsy Shop.  |  
| --- | --- |  
|  shipping_profile_id required   |  integer <int64> >= 1  The numeric ID of the [shipping profile](https://developer.etsy.com/documentation/reference#operation/getShopShippingProfile) associated with the listing. Required when listing type is `physical`.  |  
|  shipping_profile_destination_id required   |  integer <int64> >= 1  The numeric ID of the shipping profile destination in the [shipping profile](https://developer.etsy.com/documentation/reference#tag/Shop-ShippingProfile) associated with the listing.  |  
### Responses
**204**
Etsy deleted the shipping profile destination.
**400**
There was a problem with the request data. See the error message for details.
**401**
The request lacks valid authentication credentials. See the error message for details.
**403**
The request attempted to perform an operation it is not allowed to. See the error message for details.
**404**
A resource could not be found. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
delete/v3/application/shops/{shop_id}/shipping-profiles/{shipping_profile_id}/destinations/{shipping_profile_destination_id}
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/shops/{shop_id}/shipping-profiles/{shipping_profile_id}/destinations/{shipping_profile_destination_id}
###  Response samples 
  * 400
  * 401
  * 403
  * 404
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
  *  "error": "string" 

 }`
##  [](https://developer.etsy.com/documentation/reference/#operation/updateShopShippingProfileDestination)updateShopShippingProfileDestination 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Updates an existing shipping destination, which can set or reassign the shipping cost, carrier, and class for a destination.
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)[oauth2](https://developer.etsy.com/documentation/reference/#section/Authentication/oauth2) (`shops_w`) 
##### path Parameters  
|  shop_id required   |  integer <int64> >= 1  The unique positive non-zero numeric ID for an Etsy Shop.  |  
| --- | --- |  
|  shipping_profile_id required   |  integer <int64> >= 1  The numeric ID of the [shipping profile](https://developer.etsy.com/documentation/reference#operation/getShopShippingProfile) associated with the listing. Required when listing type is `physical`.  |  
|  shipping_profile_destination_id required   |  integer <int64> >= 1  The numeric ID of the shipping profile destination in the [shipping profile](https://developer.etsy.com/documentation/reference#tag/Shop-ShippingProfile) associated with the listing.  |  
##### Request Body schema: application/x-www-form-urlencoded  
| primary_cost  |  number <float> >= 0  Default:  null The cost of shipping to this country/region alone, measured in the store's default currency.  |  
| --- | --- |  
| secondary_cost  |  number <float> >= 0  Default:  null The cost of shipping to this country/region with another item, measured in the store's default currency.  |  
| destination_country_iso  |  string <ISO 3166-1 alpha-2> Default:  null The ISO code of the country to which the listing ships. If null, request sets destination to destination_region. Required if destination_region is null or not provided.  |  
| destination_region  |  string Default:  "none" Enum: "eu" "non_eu" "none" The code of the region to which the listing ships. A region represents a set of countries. Supported regions are Europe Union and Non-Europe Union (countries in Europe not in EU). If `none`, request sets destination to destination_country_iso. Required if destination_country_iso is null or not provided.  |  
| shipping_carrier_id  |  integer <int64> >= 0  Default:  null The unique ID of a supported shipping carrier, which is used to calculate an Estimated Delivery Date. **Required with`mail_class`** if `min_delivery_days` and `max_delivery_days` are null.  |  
| mail_class  |  string Default:  null The unique ID string of a shipping carrier's mail class, which is used to calculate an estimated delivery date. **Required with`shipping_carrier_id`** if `min_delivery_days` and `max_delivery_days` are null.  |  
| min_delivery_days  |  integer <int64> [ 1 .. 45 ]  Default:  null The minimum number of business days a buyer can expect to wait to receive their purchased item once it has shipped. **Required with`max_delivery_days`** if `mail_class` is null.  |  
| max_delivery_days  |  integer <int64> [ 1 .. 45 ]  Default:  null The maximum number of business days a buyer can expect to wait to receive their purchased item once it has shipped. **Required with`min_delivery_days`** if `mail_class` is null.  |  
### Responses
**200**
A single shipping destination.
**400**
There was a problem with the request data. See the error message for details.
**401**
The request lacks valid authentication credentials. See the error message for details.
**403**
The request attempted to perform an operation it is not allowed to. See the error message for details.
**404**
A resource could not be found. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
**503**
This function is temporarily unavailable. Please try again later.
put/v3/application/shops/{shop_id}/shipping-profiles/{shipping_profile_id}/destinations/{shipping_profile_destination_id}
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/shops/{shop_id}/shipping-profiles/{shipping_profile_id}/destinations/{shipping_profile_destination_id}
###  Response samples 
  * 200
  * 400
  * 401
  * 403
  * 404
  * 500
  * 503


Content type
application/json
Copy
Expand all  Collapse all 
`{
 
  *  "shipping_profile_destination_id": 1, 
 
  *  "shipping_profile_id": 1, 
 
  *  "origin_country_iso": "string", 
 
  *  "destination_country_iso": "string", 
 
  *  "destination_region": "eu", 
 
  *  "primary_cost": { 
    *  "amount": 0, 
 
    *  "divisor": 0, 
 
    *  "currency_code": "string" 
  }, 
 
  *  "secondary_cost": { 
    *  "amount": 0, 
 
    *  "divisor": 0, 
 
    *  "currency_code": "string" 
  }, 
 
  *  "shipping_carrier_id": 0, 
 
  *  "mail_class": "string", 
 
  *  "min_delivery_days": 1, 
 
  *  "max_delivery_days": 1 
 
 }`
##  [](https://developer.etsy.com/documentation/reference/#operation/createShopShippingProfileUpgrade)createShopShippingProfileUpgrade 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Creates a new shipping profile upgrade, which can establish a price for a shipping option, such as an alternate carrier or faster delivery.
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)[oauth2](https://developer.etsy.com/documentation/reference/#section/Authentication/oauth2) (`shops_w`) 
##### path Parameters  
|  shop_id required   |  integer <int64> >= 1  The unique positive non-zero numeric ID for an Etsy Shop.  |  
| --- | --- |  
|  shipping_profile_id required   |  integer <int64> >= 1  The numeric ID of the [shipping profile](https://developer.etsy.com/documentation/reference#operation/getShopShippingProfile) associated with the listing. Required when listing type is `physical`.  |  
##### Request Body schema: application/x-www-form-urlencoded  
|  type required   |  integer <int64> Enum: 0 1 The type of the shipping upgrade. Domestic (0) or international (1).  |  
| --- | --- |  
|  upgrade_name required   |  string Name for the shipping upgrade shown to shoppers at checkout, e.g. USPS Priority.  |  
|  price required   |  number <float> >= 0  Additional cost of adding the shipping upgrade.  |  
|  secondary_price required   |  number <float> >= 0  Additional cost of adding the shipping upgrade for each additional item.  |  
| shipping_carrier_id  |  integer <int64> >= 0  Default:  0 The unique ID of a supported shipping carrier, which is used to calculate an Estimated Delivery Date. **Required with`mail_class`** if `min_delivery_days` and `max_delivery_days` are null.  |  
| mail_class  |  string Default:  null The unique ID string of a shipping carrier's mail class, which is used to calculate an estimated delivery date. **Required with`shipping_carrier_id`** if `min_delivery_days` and `max_delivery_days` are null.  |  
| min_delivery_days  |  integer <int64> [ 1 .. 45 ]  Default:  null The minimum number of business days a buyer can expect to wait to receive their purchased item once it has shipped. **Required with`max_delivery_days`** if `mail_class` is null.  |  
| max_delivery_days  |  integer <int64> [ 1 .. 45 ]  Default:  null The maximum number of business days a buyer can expect to wait to receive their purchased item once it has shipped. **Required with`min_delivery_days`** if `mail_class` is null.  |  
### Responses
**200**
A single shipping profile upgrade.
**400**
There was a problem with the request data. See the error message for details.
**401**
The request lacks valid authentication credentials. See the error message for details.
**403**
The request attempted to perform an operation it is not allowed to. See the error message for details.
**404**
A resource could not be found. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
post/v3/application/shops/{shop_id}/shipping-profiles/{shipping_profile_id}/upgrades
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/shops/{shop_id}/shipping-profiles/{shipping_profile_id}/upgrades
###  Response samples 
  * 200
  * 400
  * 401
  * 403
  * 404
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
 
  *  "shipping_profile_id": 1, 
 
  *  "upgrade_id": 1, 
 
  *  "upgrade_name": "string", 
 
  *  "type": 0, 
 
  *  "rank": 0, 
 
  *  "language": "string", 
 
  *  "price": { 
    *  "amount": 0, 
 
    *  "divisor": 0, 
 
    *  "currency_code": "string" 
  }, 
 
  *  "secondary_price": { 
    *  "amount": 0, 
 
    *  "divisor": 0, 
 
    *  "currency_code": "string" 
  }, 
 
  *  "shipping_carrier_id": 0, 
 
  *  "mail_class": "string", 
 
  *  "min_delivery_days": 1, 
 
  *  "max_delivery_days": 1 
 
 }`
##  [](https://developer.etsy.com/documentation/reference/#operation/getShopShippingProfileUpgrades)getShopShippingProfileUpgrades 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Retrieves the list of shipping profile upgrades assigned to a specific shipping profile.
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)[oauth2](https://developer.etsy.com/documentation/reference/#section/Authentication/oauth2) (`shops_r`) 
##### path Parameters  
|  shop_id required   |  integer <int64> >= 1  The unique positive non-zero numeric ID for an Etsy Shop.  |  
| --- | --- |  
|  shipping_profile_id required   |  integer <int64> >= 1  The numeric ID of the [shipping profile](https://developer.etsy.com/documentation/reference#operation/getShopShippingProfile) associated with the listing. Required when listing type is `physical`.  |  
### Responses
**200**
A list of shipping profile upgrades.
**400**
There was a problem with the request data. See the error message for details.
**401**
The request lacks valid authentication credentials. See the error message for details.
**403**
The request attempted to perform an operation it is not allowed to. See the error message for details.
**404**
A resource could not be found. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
get/v3/application/shops/{shop_id}/shipping-profiles/{shipping_profile_id}/upgrades
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/shops/{shop_id}/shipping-profiles/{shipping_profile_id}/upgrades
###  Response samples 
  * 200
  * 400
  * 401
  * 403
  * 404
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
 
  *  "count": 0, 
 
  *  "results": [
    *  { 
      *  "shipping_profile_id": 1, 
 
      *  "upgrade_id": 1, 
 
      *  "upgrade_name": "string", 
 
      *  "type": 0, 
 
      *  "rank": 0, 
 
      *  "language": "string", 
 
      *  "price": { 
        *  "amount": 0, 
 
        *  "divisor": 0, 
 
        *  "currency_code": "string" 
  }, 
 
      *  "secondary_price": { 
        *  "amount": 0, 
 
        *  "divisor": 0, 
 
        *  "currency_code": "string" 
  }, 
 
      *  "shipping_carrier_id": 0, 
 
      *  "mail_class": "string", 
 
      *  "min_delivery_days": 1, 
 
      *  "max_delivery_days": 1 
  } 
 ] 
 
 }`
##  [](https://developer.etsy.com/documentation/reference/#operation/deleteShopShippingProfileUpgrade)deleteShopShippingProfileUpgrade 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Deletes a shipping profile upgrade and removes the upgrade option from every listing that uses the associated shipping profile.
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)[oauth2](https://developer.etsy.com/documentation/reference/#section/Authentication/oauth2) (`shops_w`) 
##### path Parameters  
|  shop_id required   |  integer <int64> >= 1  The unique positive non-zero numeric ID for an Etsy Shop.  |  
| --- | --- |  
|  shipping_profile_id required   |  integer <int64> >= 1  The numeric ID of the shipping profile.  |  
|  upgrade_id required   |  integer <int64> >= 1  The numeric ID that is associated with a shipping upgrade  |  
### Responses
**204**
Etsy deleted the shipping profile upgrade.
**400**
There was a problem with the request data. See the error message for details.
**401**
The request lacks valid authentication credentials. See the error message for details.
**403**
The request attempted to perform an operation it is not allowed to. See the error message for details.
**404**
A resource could not be found. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
delete/v3/application/shops/{shop_id}/shipping-profiles/{shipping_profile_id}/upgrades/{upgrade_id}
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/shops/{shop_id}/shipping-profiles/{shipping_profile_id}/upgrades/{upgrade_id}
###  Response samples 
  * 400
  * 401
  * 403
  * 404
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
  *  "error": "string" 

 }`
##  [](https://developer.etsy.com/documentation/reference/#operation/updateShopShippingProfileUpgrade)updateShopShippingProfileUpgrade 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Updates a shipping profile upgrade and updates any listings that use the shipping profile.
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)[oauth2](https://developer.etsy.com/documentation/reference/#section/Authentication/oauth2) (`shops_w`) 
##### path Parameters  
|  shop_id required   |  integer <int64> >= 1  The unique positive non-zero numeric ID for an Etsy Shop.  |  
| --- | --- |  
|  shipping_profile_id required   |  integer <int64> >= 1  The numeric ID of the [shipping profile](https://developer.etsy.com/documentation/reference#operation/getShopShippingProfile) associated with the listing. Required when listing type is `physical`.  |  
|  upgrade_id required   |  integer <int64> >= 1  The numeric ID that is associated with a shipping upgrade  |  
##### Request Body schema: application/x-www-form-urlencoded  
| upgrade_name  |  string Default:  null Name for the shipping upgrade shown to shoppers at checkout, e.g. USPS Priority.  |  
| --- | --- |  
| type  |  integer <int64> Enum: 0 1 The type of the shipping upgrade. Domestic (0) or international (1).  |  
| price  |  number <float> >= 0  Default:  null Additional cost of adding the shipping upgrade.  |  
| secondary_price  |  number <float> >= 0  Default:  null Additional cost of adding the shipping upgrade for each additional item.  |  
| shipping_carrier_id  |  integer <int64> >= 0  Default:  null The unique ID of a supported shipping carrier, which is used to calculate an Estimated Delivery Date. **Required with`mail_class`** if `min_delivery_days` and `max_delivery_days` are null.  |  
| mail_class  |  string Default:  null The unique ID string of a shipping carrier's mail class, which is used to calculate an estimated delivery date. **Required with`shipping_carrier_id`** if `min_delivery_days` and `max_delivery_days` are null.  |  
| min_delivery_days  |  integer <int64> [ 1 .. 45 ]  Default:  null The minimum number of business days a buyer can expect to wait to receive their purchased item once it has shipped. **Required with`max_delivery_days`** if `mail_class` is null.  |  
| max_delivery_days  |  integer <int64> [ 1 .. 45 ]  Default:  null The maximum number of business days a buyer can expect to wait to receive their purchased item once it has shipped. **Required with`min_delivery_days`** if `mail_class` is null.  |  
### Responses
**200**
A single shipping profile upgrade.
**400**
There was a problem with the request data. See the error message for details.
**401**
The request lacks valid authentication credentials. See the error message for details.
**403**
The request attempted to perform an operation it is not allowed to. See the error message for details.
**404**
A resource could not be found. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
**503**
This function is temporarily unavailable. Please try again later.
put/v3/application/shops/{shop_id}/shipping-profiles/{shipping_profile_id}/upgrades/{upgrade_id}
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/shops/{shop_id}/shipping-profiles/{shipping_profile_id}/upgrades/{upgrade_id}
###  Response samples 
  * 200
  * 400
  * 401
  * 403
  * 404
  * 500
  * 503


Content type
application/json
Copy
Expand all  Collapse all 
`{
 
  *  "shipping_profile_id": 1, 
 
  *  "upgrade_id": 1, 
 
  *  "upgrade_name": "string", 
 
  *  "type": 0, 
 
  *  "rank": 0, 
 
  *  "language": "string", 
 
  *  "price": { 
    *  "amount": 0, 
 
    *  "divisor": 0, 
 
    *  "currency_code": "string" 
  }, 
 
  *  "secondary_price": { 
    *  "amount": 0, 
 
    *  "divisor": 0, 
 
    *  "currency_code": "string" 
  }, 
 
  *  "shipping_carrier_id": 0, 
 
  *  "mail_class": "string", 
 
  *  "min_delivery_days": 1, 
 
  *  "max_delivery_days": 1 
 
 }`
#  [](https://developer.etsy.com/documentation/reference/#tag/Shop)Shop
##  [](https://developer.etsy.com/documentation/reference/#operation/getShop)getShop 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Retrieves the shop identified by a specific shop ID.
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)
##### path Parameters  
|  shop_id required   |  integer <int64> >= 1  The unique positive non-zero numeric ID for an Etsy Shop.  |  
| --- | --- |  
### Responses
**200**
A single Shop
**400**
There was a problem with the request data. See the error message for details.
**404**
A resource could not be found. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
get/v3/application/shops/{shop_id}
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/shops/{shop_id}
###  Response samples 
  * 200
  * 400
  * 404
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
 
  *  "shop_id": 1, 
 
  *  "user_id": 1, 
 
  *  "shop_name": "string", 
 
  *  "create_date": 0, 
 
  *  "created_timestamp": 0, 
 
  *  "title": "string", 
 
  *  "announcement": "string", 
 
  *  "currency_code": "string", 
 
  *  "is_vacation": true, 
 
  *  "vacation_message": "string", 
 
  *  "sale_message": "string", 
 
  *  "digital_sale_message": "string", 
 
  *  "update_date": 0, 
 
  *  "updated_timestamp": 0, 
 
  *  "listing_active_count": 0, 
 
  *  "digital_listing_count": 0, 
 
  *  "login_name": "string", 
 
  *  "accepts_custom_requests": true, 
 
  *  "policy_welcome": "string", 
 
  *  "policy_payment": "string", 
 
  *  "policy_shipping": "string", 
 
  *  "policy_refunds": "string", 
 
  *  "policy_additional": "string", 
 
  *  "policy_seller_info": "string", 
 
  *  "policy_update_date": 0, 
 
  *  "policy_has_private_receipt_info": true, 
 
  *  "has_unstructured_policies": true, 
 
  *  "policy_privacy": "string", 
 
  *  "vacation_autoreply": "string", 
 
  *  "url": "string", 
 
  *  "image_url_760x100": "string", 
 
  *  "num_favorers": 0, 
 
  *  "languages": [
    * "string"
 ], 
 
  *  "icon_url_fullxfull": "string", 
 
  *  "is_using_structured_policies": true, 
 
  *  "has_onboarded_structured_policies": true, 
 
  *  "include_dispute_form_link": true, 
 
  *  "is_direct_checkout_onboarded": true, 
 
  *  "is_etsy_payments_onboarded": true, 
 
  *  "is_calculated_eligible": true, 
 
  *  "is_opted_in_to_buyer_promise": true, 
 
  *  "is_shop_us_based": true, 
 
  *  "transaction_sold_count": 0, 
 
  *  "shipping_from_country_iso": "string", 
 
  *  "shop_location_country_iso": "string", 
 
  *  "review_count": 0, 
 
  *  "review_average": 0 
 
 }`
##  [](https://developer.etsy.com/documentation/reference/#operation/updateShop)updateShop 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Updates a shop. Assumes that all string parameters are provided in the shop's primary language. Please note that the policy_additional field should only be set for shops located in the EU. Passing a value for this field for shops outside of the EU, will result in an error.
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)[oauth2](https://developer.etsy.com/documentation/reference/#section/Authentication/oauth2) (`shops_r``shops_w`) 
##### path Parameters  
|  shop_id required   |  integer <int64> >= 1  The unique positive non-zero numeric ID for an Etsy Shop.  |  
| --- | --- |  
##### Request Body schema: application/x-www-form-urlencoded  
| title  |  string A brief heading string for the shop's main page.  |  
| --- | --- |  
| announcement  |  string An announcement string to buyers that displays on the shop's homepage.  |  
| sale_message  |  string A message string sent to users who complete a purchase from this shop.  |  
| digital_sale_message  |  string A message string sent to users who purchase a digital item from this shop.  |  
| policy_additional  |  string The shop's additional policies string (may be blank).  |  
### Responses
**200**
A single Shop.
**400**
There was a problem with the request data. See the error message for details.
**401**
The request lacks valid authentication credentials. See the error message for details.
**403**
The request attempted to perform an operation it is not allowed to. See the error message for details.
**404**
A resource could not be found. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
put/v3/application/shops/{shop_id}
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/shops/{shop_id}
###  Response samples 
  * 200
  * 400
  * 401
  * 403
  * 404
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
 
  *  "shop_id": 1, 
 
  *  "user_id": 1, 
 
  *  "shop_name": "string", 
 
  *  "create_date": 0, 
 
  *  "created_timestamp": 0, 
 
  *  "title": "string", 
 
  *  "announcement": "string", 
 
  *  "currency_code": "string", 
 
  *  "is_vacation": true, 
 
  *  "vacation_message": "string", 
 
  *  "sale_message": "string", 
 
  *  "digital_sale_message": "string", 
 
  *  "update_date": 0, 
 
  *  "updated_timestamp": 0, 
 
  *  "listing_active_count": 0, 
 
  *  "digital_listing_count": 0, 
 
  *  "login_name": "string", 
 
  *  "accepts_custom_requests": true, 
 
  *  "policy_welcome": "string", 
 
  *  "policy_payment": "string", 
 
  *  "policy_shipping": "string", 
 
  *  "policy_refunds": "string", 
 
  *  "policy_additional": "string", 
 
  *  "policy_seller_info": "string", 
 
  *  "policy_update_date": 0, 
 
  *  "policy_has_private_receipt_info": true, 
 
  *  "has_unstructured_policies": true, 
 
  *  "policy_privacy": "string", 
 
  *  "vacation_autoreply": "string", 
 
  *  "url": "string", 
 
  *  "image_url_760x100": "string", 
 
  *  "num_favorers": 0, 
 
  *  "languages": [
    * "string"
 ], 
 
  *  "icon_url_fullxfull": "string", 
 
  *  "is_using_structured_policies": true, 
 
  *  "has_onboarded_structured_policies": true, 
 
  *  "include_dispute_form_link": true, 
 
  *  "is_direct_checkout_onboarded": true, 
 
  *  "is_etsy_payments_onboarded": true, 
 
  *  "is_calculated_eligible": true, 
 
  *  "is_opted_in_to_buyer_promise": true, 
 
  *  "is_shop_us_based": true, 
 
  *  "transaction_sold_count": 0, 
 
  *  "shipping_from_country_iso": "string", 
 
  *  "shop_location_country_iso": "string", 
 
  *  "review_count": 0, 
 
  *  "review_average": 0 
 
 }`
##  [](https://developer.etsy.com/documentation/reference/#operation/getShopByOwnerUserId)getShopByOwnerUserId 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Retrieves the shop identified by the shop owner's user ID.
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)
##### path Parameters  
|  user_id required   |  integer <int64> >= 1  The numeric user ID of the [user](https://developer.etsy.com/documentation/reference#tag/User) who owns this shop.  |  
| --- | --- |  
### Responses
**200**
A single Shop
**400**
There was a problem with the request data. See the error message for details.
**403**
The request attempted to perform an operation it is not allowed to. See the error message for details.
**404**
A resource could not be found. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
get/v3/application/users/{user_id}/shops
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/users/{user_id}/shops
###  Response samples 
  * 200
  * 400
  * 403
  * 404
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
 
  *  "shop_id": 1, 
 
  *  "user_id": 1, 
 
  *  "shop_name": "string", 
 
  *  "create_date": 0, 
 
  *  "created_timestamp": 0, 
 
  *  "title": "string", 
 
  *  "announcement": "string", 
 
  *  "currency_code": "string", 
 
  *  "is_vacation": true, 
 
  *  "vacation_message": "string", 
 
  *  "sale_message": "string", 
 
  *  "digital_sale_message": "string", 
 
  *  "update_date": 0, 
 
  *  "updated_timestamp": 0, 
 
  *  "listing_active_count": 0, 
 
  *  "digital_listing_count": 0, 
 
  *  "login_name": "string", 
 
  *  "accepts_custom_requests": true, 
 
  *  "policy_welcome": "string", 
 
  *  "policy_payment": "string", 
 
  *  "policy_shipping": "string", 
 
  *  "policy_refunds": "string", 
 
  *  "policy_additional": "string", 
 
  *  "policy_seller_info": "string", 
 
  *  "policy_update_date": 0, 
 
  *  "policy_has_private_receipt_info": true, 
 
  *  "has_unstructured_policies": true, 
 
  *  "policy_privacy": "string", 
 
  *  "vacation_autoreply": "string", 
 
  *  "url": "string", 
 
  *  "image_url_760x100": "string", 
 
  *  "num_favorers": 0, 
 
  *  "languages": [
    * "string"
 ], 
 
  *  "icon_url_fullxfull": "string", 
 
  *  "is_using_structured_policies": true, 
 
  *  "has_onboarded_structured_policies": true, 
 
  *  "include_dispute_form_link": true, 
 
  *  "is_direct_checkout_onboarded": true, 
 
  *  "is_etsy_payments_onboarded": true, 
 
  *  "is_calculated_eligible": true, 
 
  *  "is_opted_in_to_buyer_promise": true, 
 
  *  "is_shop_us_based": true, 
 
  *  "transaction_sold_count": 0, 
 
  *  "shipping_from_country_iso": "string", 
 
  *  "shop_location_country_iso": "string", 
 
  *  "review_count": 0, 
 
  *  "review_average": 0 
 
 }`
##  [](https://developer.etsy.com/documentation/reference/#operation/findShops)findShops 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Open API V3 endpoint for searching shops by name. Note: We make every effort to ensure that frozen or removed shops are not included in the search results. However, rarely, due to timing issues, they may appear.
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)
##### query Parameters  
|  shop_name required   |  string The shop's name string.  |  
| --- | --- |  
| limit  |  integer <int64> [ 1 .. 100 ]  Default:  25 The maximum number of results to return.  |  
| offset  |  integer <int64> >= 0  Default:  0 The number of records to skip before selecting the first result.  |  
### Responses
**200**
A list of Shops
**500**
The server encountered an internal error. See the error message for details.
get/v3/application/shops
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/shops
###  Response samples 
  * 200
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
 
  *  "count": 0, 
 
  *  "results": [
    *  { 
      *  "shop_id": 1, 
 
      *  "user_id": 1, 
 
      *  "shop_name": "string", 
 
      *  "create_date": 0, 
 
      *  "created_timestamp": 0, 
 
      *  "title": "string", 
 
      *  "announcement": "string", 
 
      *  "currency_code": "string", 
 
      *  "is_vacation": true, 
 
      *  "vacation_message": "string", 
 
      *  "sale_message": "string", 
 
      *  "digital_sale_message": "string", 
 
      *  "update_date": 0, 
 
      *  "updated_timestamp": 0, 
 
      *  "listing_active_count": 0, 
 
      *  "digital_listing_count": 0, 
 
      *  "login_name": "string", 
 
      *  "accepts_custom_requests": true, 
 
      *  "policy_welcome": "string", 
 
      *  "policy_payment": "string", 
 
      *  "policy_shipping": "string", 
 
      *  "policy_refunds": "string", 
 
      *  "policy_additional": "string", 
 
      *  "policy_seller_info": "string", 
 
      *  "policy_update_date": 0, 
 
      *  "policy_has_private_receipt_info": true, 
 
      *  "has_unstructured_policies": true, 
 
      *  "policy_privacy": "string", 
 
      *  "vacation_autoreply": "string", 
 
      *  "url": "string", 
 
      *  "image_url_760x100": "string", 
 
      *  "num_favorers": 0, 
 
      *  "languages": [
        * "string"
 ], 
 
      *  "icon_url_fullxfull": "string", 
 
      *  "is_using_structured_policies": true, 
 
      *  "has_onboarded_structured_policies": true, 
 
      *  "include_dispute_form_link": true, 
 
      *  "is_direct_checkout_onboarded": true, 
 
      *  "is_etsy_payments_onboarded": true, 
 
      *  "is_calculated_eligible": true, 
 
      *  "is_opted_in_to_buyer_promise": true, 
 
      *  "is_shop_us_based": true, 
 
      *  "transaction_sold_count": 0, 
 
      *  "shipping_from_country_iso": "string", 
 
      *  "shop_location_country_iso": "string", 
 
      *  "review_count": 0, 
 
      *  "review_average": 0 
  } 
 ] 
 
 }`
#  [](https://developer.etsy.com/documentation/reference/#tag/Shop-ProductionPartner)Shop ProductionPartner
##  [](https://developer.etsy.com/documentation/reference/#operation/getShopProductionPartners)getShopProductionPartners 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Retrieves a list of production partners available in the specific Etsy shop identified by its shop ID.
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)[oauth2](https://developer.etsy.com/documentation/reference/#section/Authentication/oauth2) (`shops_r`) 
##### path Parameters  
|  shop_id required   |  integer <int64> >= 1  The unique positive non-zero numeric ID for an Etsy Shop.  |  
| --- | --- |  
### Responses
**200**
A list of shop production partners
**400**
There was a problem with the request data. See the error message for details.
**403**
The request attempted to perform an operation it is not allowed to. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
get/v3/application/shops/{shop_id}/production-partners
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/shops/{shop_id}/production-partners
###  Response samples 
  * 200
  * 400
  * 403
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
 
  *  "count": 0, 
 
  *  "results": [
    *  { 
      *  "production_partner_id": 1, 
 
      *  "partner_name": "string", 
 
      *  "location": "string" 
  } 
 ] 
 
 }`
#  [](https://developer.etsy.com/documentation/reference/#tag/Shop-Section)Shop Section
##  [](https://developer.etsy.com/documentation/reference/#operation/createShopSection)createShopSection 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Creates a new section in a specific shop.
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)[oauth2](https://developer.etsy.com/documentation/reference/#section/Authentication/oauth2) (`shops_w`) 
##### path Parameters  
|  shop_id required   |  integer <int64> >= 1  The unique positive non-zero numeric ID for an Etsy Shop.  |  
| --- | --- |  
##### Request Body schema: application/x-www-form-urlencoded  
|  title required   |  string The title string for a shop section.  |  
| --- | --- |  
### Responses
**200**
A Shop Section resource
**400**
There was a problem with the request data. See the error message for details.
**401**
The request lacks valid authentication credentials. See the error message for details.
**403**
The request attempted to perform an operation it is not allowed to. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
**503**
This function is temporarily unavailable. Please try again later.
post/v3/application/shops/{shop_id}/sections
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/shops/{shop_id}/sections
###  Response samples 
  * 200
  * 400
  * 401
  * 403
  * 500
  * 503


Content type
application/json
Copy
Expand all  Collapse all 
`{
 
  *  "shop_section_id": 1, 
 
  *  "title": "string", 
 
  *  "rank": 0, 
 
  *  "user_id": 1, 
 
  *  "active_listing_count": 0 
 
 }`
##  [](https://developer.etsy.com/documentation/reference/#operation/getShopSections)getShopSections 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Retrieves the list of shop sections in a specific shop identified by shop ID.
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)
##### path Parameters  
|  shop_id required   |  integer <int64> >= 1  The unique positive non-zero numeric ID for an Etsy Shop.  |  
| --- | --- |  
### Responses
**200**
A list of shop sections.
**400**
There was a problem with the request data. See the error message for details.
**404**
A resource could not be found. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
get/v3/application/shops/{shop_id}/sections
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/shops/{shop_id}/sections
###  Response samples 
  * 200
  * 400
  * 404
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
 
  *  "count": 0, 
 
  *  "results": [
    *  { 
      *  "shop_section_id": 1, 
 
      *  "title": "string", 
 
      *  "rank": 0, 
 
      *  "user_id": 1, 
 
      *  "active_listing_count": 0 
  } 
 ] 
 
 }`
##  [](https://developer.etsy.com/documentation/reference/#operation/deleteShopSection)deleteShopSection 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Deletes a section in a specific shop given a valid shop_section_id.
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)[oauth2](https://developer.etsy.com/documentation/reference/#section/Authentication/oauth2) (`shops_w`) 
##### path Parameters  
|  shop_id required   |  integer <int64> >= 1  The unique positive non-zero numeric ID for an Etsy Shop.  |  
| --- | --- |  
|  shop_section_id required   |  integer <int64> >= 1  The numeric ID of a section in a specific Etsy shop.  |  
### Responses
**204**
The shop section resource was correctly deleted
**400**
There was a problem with the request data. See the error message for details.
**401**
The request lacks valid authentication credentials. See the error message for details.
**403**
The request attempted to perform an operation it is not allowed to. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
**503**
This function is temporarily unavailable. Please try again later.
delete/v3/application/shops/{shop_id}/sections/{shop_section_id}
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/shops/{shop_id}/sections/{shop_section_id}
###  Response samples 
  * 400
  * 401
  * 403
  * 500
  * 503


Content type
application/json
Copy
Expand all  Collapse all 
`{
  *  "error": "string" 

 }`
##  [](https://developer.etsy.com/documentation/reference/#operation/getShopSection)getShopSection 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Retrieves a shop section, referenced by section ID and shop ID.
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)
##### path Parameters  
|  shop_id required   |  integer <int64> >= 1  The unique positive non-zero numeric ID for an Etsy Shop.  |  
| --- | --- |  
|  shop_section_id required   |  integer <int64> >= 1  The numeric ID of a section in a specific Etsy shop.  |  
### Responses
**200**
A shop section resource
**400**
There was a problem with the request data. See the error message for details.
**404**
A resource could not be found. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
get/v3/application/shops/{shop_id}/sections/{shop_section_id}
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/shops/{shop_id}/sections/{shop_section_id}
###  Response samples 
  * 200
  * 400
  * 404
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
 
  *  "shop_section_id": 1, 
 
  *  "title": "string", 
 
  *  "rank": 0, 
 
  *  "user_id": 1, 
 
  *  "active_listing_count": 0 
 
 }`
##  [](https://developer.etsy.com/documentation/reference/#operation/updateShopSection)updateShopSection 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Updates a section in a specific shop given a valid shop_section_id.
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)[oauth2](https://developer.etsy.com/documentation/reference/#section/Authentication/oauth2) (`shops_w`) 
##### path Parameters  
|  shop_id required   |  integer <int64> >= 1  The unique positive non-zero numeric ID for an Etsy Shop.  |  
| --- | --- |  
|  shop_section_id required   |  integer <int64> >= 1  The numeric ID of a section in a specific Etsy shop.  |  
##### Request Body schema: application/x-www-form-urlencoded  
|  title required   |  string The title string for a shop section.  |  
| --- | --- |  
### Responses
**200**
A Shop Section resource
**400**
There was a problem with the request data. See the error message for details.
**401**
The request lacks valid authentication credentials. See the error message for details.
**403**
The request attempted to perform an operation it is not allowed to. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
**503**
This function is temporarily unavailable. Please try again later.
put/v3/application/shops/{shop_id}/sections/{shop_section_id}
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/shops/{shop_id}/sections/{shop_section_id}
###  Response samples 
  * 200
  * 400
  * 401
  * 403
  * 500
  * 503


Content type
application/json
Copy
Expand all  Collapse all 
`{
 
  *  "shop_section_id": 1, 
 
  *  "title": "string", 
 
  *  "rank": 0, 
 
  *  "user_id": 1, 
 
  *  "active_listing_count": 0 
 
 }`
#  [](https://developer.etsy.com/documentation/reference/#tag/Shop-Return-Policy)Shop Return Policy
##  [](https://developer.etsy.com/documentation/reference/#operation/consolidateShopReturnPolicies)consolidateShopReturnPolicies 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Consolidates Return Policies by moving all listings from a source return policy to a destination return policy, and deleting the source return policy. This is commonly used in the event that a user attempts to update a Return Policy such that its data is a duplicate of some other Return Policy, which is prevented.
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)[oauth2](https://developer.etsy.com/documentation/reference/#section/Authentication/oauth2) (`shops_w`) 
##### path Parameters  
|  shop_id required   |  integer <int64> >= 1  The unique positive non-zero numeric ID for an Etsy Shop.  |  
| --- | --- |  
##### Request Body schema: application/x-www-form-urlencoded  
|  source_return_policy_id required   |  integer <int64> >= 1  The numeric ID of the [Return Policy](https://developer.etsy.com/documentation/reference#operation/getShopReturnPolicies).  |  
| --- | --- |  
|  destination_return_policy_id required   |  integer <int64> >= 1  The numeric ID of the [Return Policy](https://developer.etsy.com/documentation/reference#operation/getShopReturnPolicies).  |  
### Responses
**200**
The updated target Return Policy
**400**
There was a problem with the request data. See the error message for details.
**401**
The request lacks valid authentication credentials. See the error message for details.
**403**
The request attempted to perform an operation it is not allowed to. See the error message for details.
**404**
A resource could not be found. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
post/v3/application/shops/{shop_id}/policies/return/consolidate
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/shops/{shop_id}/policies/return/consolidate
###  Response samples 
  * 200
  * 400
  * 401
  * 403
  * 404
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
 
  *  "return_policy_id": 1, 
 
  *  "shop_id": 1, 
 
  *  "accepts_returns": true, 
 
  *  "accepts_exchanges": true, 
 
  *  "return_deadline": 0 
 
 }`
##  [](https://developer.etsy.com/documentation/reference/#operation/createShopReturnPolicy)createShopReturnPolicy 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Creates a new Return Policy. Note: if either accepts_returns or accepts_exchanges is true, then a return_deadline is required.
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)[oauth2](https://developer.etsy.com/documentation/reference/#section/Authentication/oauth2) (`shops_w`) 
##### path Parameters  
|  shop_id required   |  integer <int64> >= 1  The unique positive non-zero numeric ID for an Etsy Shop.  |  
| --- | --- |  
##### Request Body schema: application/x-www-form-urlencoded  
|  accepts_returns required   |  boolean  |  
| --- | --- |  
|  accepts_exchanges required   |  boolean  |  
| return_deadline  |  integer <int64> Nullable  The deadline for the Return Policy, measured in days. The value must be one of the following: [7, 14, 21, 30, 45, 60, 90].  |  
### Responses
**200**
A single Return Policy
**400**
There was a problem with the request data. See the error message for details.
**401**
The request lacks valid authentication credentials. See the error message for details.
**403**
The request attempted to perform an operation it is not allowed to. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
post/v3/application/shops/{shop_id}/policies/return
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/shops/{shop_id}/policies/return
###  Response samples 
  * 200
  * 400
  * 401
  * 403
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
 
  *  "return_policy_id": 1, 
 
  *  "shop_id": 1, 
 
  *  "accepts_returns": true, 
 
  *  "accepts_exchanges": true, 
 
  *  "return_deadline": 0 
 
 }`
##  [](https://developer.etsy.com/documentation/reference/#operation/getShopReturnPolicies)getShopReturnPolicies 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Returns a shop's list of existing Return Policies
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)
##### path Parameters  
|  shop_id required   |  integer <int64> >= 1  The unique positive non-zero numeric ID for an Etsy Shop.  |  
| --- | --- |  
### Responses
**200**
List of shop's Return Policies
**400**
There was a problem with the request data. See the error message for details.
**401**
The request lacks valid authentication credentials. See the error message for details.
**404**
A resource could not be found. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
get/v3/application/shops/{shop_id}/policies/return
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/shops/{shop_id}/policies/return
###  Response samples 
  * 200
  * 400
  * 401
  * 404
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
 
  *  "count": 0, 
 
  *  "results": [
    *  { 
      *  "return_policy_id": 1, 
 
      *  "shop_id": 1, 
 
      *  "accepts_returns": true, 
 
      *  "accepts_exchanges": true, 
 
      *  "return_deadline": 0 
  } 
 ] 
 
 }`
##  [](https://developer.etsy.com/documentation/reference/#operation/deleteShopReturnPolicy)deleteShopReturnPolicy 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Deletes an existing Return Policy. Deletion is only allowed for policies which have no associated listings – move them to another policy before attempting deletion.
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)[oauth2](https://developer.etsy.com/documentation/reference/#section/Authentication/oauth2) (`shops_w`) 
##### path Parameters  
|  shop_id required   |  integer <int64> >= 1  The unique positive non-zero numeric ID for an Etsy Shop.  |  
| --- | --- |  
|  return_policy_id required   |  integer <int64> >= 1  The numeric ID of the [Return Policy](https://developer.etsy.com/documentation/reference#operation/getShopReturnPolicies).  |  
### Responses
**204**
The Return Policy was successfully deleted.
**400**
There was a problem with the request data. See the error message for details.
**401**
The request lacks valid authentication credentials. See the error message for details.
**403**
The request attempted to perform an operation it is not allowed to. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
delete/v3/application/shops/{shop_id}/policies/return/{return_policy_id}
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/shops/{shop_id}/policies/return/{return_policy_id}
###  Response samples 
  * 400
  * 401
  * 403
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
  *  "error": "string" 

 }`
##  [](https://developer.etsy.com/documentation/reference/#operation/getShopReturnPolicy)getShopReturnPolicy 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Retrieves an existing Return Policy.
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)
##### path Parameters  
|  shop_id required   |  integer <int64> >= 1  The unique positive non-zero numeric ID for an Etsy Shop.  |  
| --- | --- |  
|  return_policy_id required   |  integer <int64> >= 1  The numeric ID of the [Return Policy](https://developer.etsy.com/documentation/reference#operation/getShopReturnPolicies).  |  
### Responses
**200**
A single Return Policy
**400**
There was a problem with the request data. See the error message for details.
**401**
The request lacks valid authentication credentials. See the error message for details.
**404**
A resource could not be found. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
get/v3/application/shops/{shop_id}/policies/return/{return_policy_id}
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/shops/{shop_id}/policies/return/{return_policy_id}
###  Response samples 
  * 200
  * 400
  * 401
  * 404
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
 
  *  "return_policy_id": 1, 
 
  *  "shop_id": 1, 
 
  *  "accepts_returns": true, 
 
  *  "accepts_exchanges": true, 
 
  *  "return_deadline": 0 
 
 }`
##  [](https://developer.etsy.com/documentation/reference/#operation/updateShopReturnPolicy)updateShopReturnPolicy 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Updates an existing Return Policy. Note: if either accepts_returns or accepts_exchanges is true, then a return_deadline is required.
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)[oauth2](https://developer.etsy.com/documentation/reference/#section/Authentication/oauth2) (`shops_w`) 
##### path Parameters  
|  shop_id required   |  integer <int64> >= 1  The unique positive non-zero numeric ID for an Etsy Shop.  |  
| --- | --- |  
|  return_policy_id required   |  integer <int64> >= 1  The numeric ID of the [Return Policy](https://developer.etsy.com/documentation/reference#operation/getShopReturnPolicies).  |  
##### Request Body schema: application/x-www-form-urlencoded  
|  accepts_returns required   |  boolean  |  
| --- | --- |  
|  accepts_exchanges required   |  boolean  |  
| return_deadline  |  integer <int64> Nullable  The deadline for the Return Policy, measured in days. The value must be one of the following: [7, 14, 21, 30, 45, 60, 90].  |  
### Responses
**200**
An updated Return Policy
**400**
There was a problem with the request data. See the error message for details.
**401**
The request lacks valid authentication credentials. See the error message for details.
**403**
The request attempted to perform an operation it is not allowed to. See the error message for details.
**404**
A resource could not be found. See the error message for details.
**409**
There was a request conflict with the current state of the target resource. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
put/v3/application/shops/{shop_id}/policies/return/{return_policy_id}
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/shops/{shop_id}/policies/return/{return_policy_id}
###  Response samples 
  * 200
  * 400
  * 401
  * 403
  * 404
  * 409
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
 
  *  "return_policy_id": 1, 
 
  *  "shop_id": 1, 
 
  *  "accepts_returns": true, 
 
  *  "accepts_exchanges": true, 
 
  *  "return_deadline": 0 
 
 }`
#  [](https://developer.etsy.com/documentation/reference/#tag/User)User
##  [](https://developer.etsy.com/documentation/reference/#operation/getUser)getUser 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Retrieves a user profile based on a unique user ID. Access is limited to profiles of the authenticated user or linked buyers. For the primary_email field, specific app-based permissions are required and granted case-by-case.
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)[oauth2](https://developer.etsy.com/documentation/reference/#section/Authentication/oauth2) (`email_r`) 
##### path Parameters  
|  user_id required   |  integer <int64> >= 1   |  
| --- | --- |  
### Responses
**200**
A single User
**400**
There was a problem with the request data. See the error message for details.
**401**
The request lacks valid authentication credentials. See the error message for details.
**404**
A resource could not be found. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
get/v3/application/users/{user_id}
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/users/{user_id}
###  Response samples 
  * 200
  * 400
  * 401
  * 404
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
 
  *  "user_id": 1, 
 
  *  "primary_email": "user@example.com", 
 
  *  "first_name": "string", 
 
  *  "last_name": "string", 
 
  *  "image_url_75x75": "string" 
 
 }`
##  [](https://developer.etsy.com/documentation/reference/#operation/getMe)getMe 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Returns basic info for the user making the request.
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)[oauth2](https://developer.etsy.com/documentation/reference/#section/Authentication/oauth2) (`shops_r`) 
### Responses
**200**
Fetches basic info about the requesting user
**400**
There was a problem with the request data. See the error message for details.
**401**
The request lacks valid authentication credentials. See the error message for details.
**404**
A resource could not be found. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
get/v3/application/users/me
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/users/me
###  Response samples 
  * 200
  * 400
  * 401
  * 404
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
 
  *  "user_id": 1, 
 
  *  "shop_id": 1 
 
 }`
#  [](https://developer.etsy.com/documentation/reference/#tag/UserAddress)UserAddress
##  [](https://developer.etsy.com/documentation/reference/#operation/getUserAddress)getUserAddress 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Open API V3 endpoint to retrieve a UserAddress for a User.
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)[oauth2](https://developer.etsy.com/documentation/reference/#section/Authentication/oauth2) (`address_r`) 
##### path Parameters  
|  user_address_id required   |  integer <int64> >= 1  The numeric ID of the user's address.  |  
| --- | --- |  
### Responses
**200**
A single UserAddress
**400**
There was a problem with the request data. See the error message for details.
**401**
The request lacks valid authentication credentials. See the error message for details.
**404**
A resource could not be found. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
get/v3/application/user/addresses/{user_address_id}
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/user/addresses/{user_address_id}
###  Response samples 
  * 200
  * 400
  * 401
  * 404
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
 
  *  "user_address_id": 1, 
 
  *  "user_id": 1, 
 
  *  "name": "string", 
 
  *  "first_line": "string", 
 
  *  "second_line": "string", 
 
  *  "city": "string", 
 
  *  "state": "string", 
 
  *  "zip": "string", 
 
  *  "iso_country_code": "string", 
 
  *  "country_name": "string", 
 
  *  "is_default_shipping_address": true 
 
 }`
##  [](https://developer.etsy.com/documentation/reference/#operation/getUserAddresses)getUserAddresses 
General Release[Report bug](https://github.com/etsy/open-api/discussions)
This endpoint is ready for production use.
Open API V3 endpoint to retrieve UserAddresses for a User.
##### Authorizations: 
[api_key](https://developer.etsy.com/documentation/reference/#section/Authentication/api_key)[oauth2](https://developer.etsy.com/documentation/reference/#section/Authentication/oauth2) (`address_r`) 
##### query Parameters  
| limit  |  integer <int64> [ 1 .. 100 ]  Default:  25 The maximum number of results to return.  |  
| --- | --- |  
| offset  |  integer <int64> >= 0  Default:  0 The number of records to skip before selecting the first result.  |  
### Responses
**200**
A list of UserAddress records
**401**
The request lacks valid authentication credentials. See the error message for details.
**404**
A resource could not be found. See the error message for details.
**500**
The server encountered an internal error. See the error message for details.
get/v3/application/user/addresses
Base URL for all Open API endpoints.
https://openapi.etsy.com/v3/application/user/addresses
###  Response samples 
  * 200
  * 401
  * 404
  * 500


Content type
application/json
Copy
Expand all  Collapse all 
`{
 
  *  "count": 0, 
 
  *  "results": [
    *  { 
      *  "user_address_id": 1, 
 
      *  "user_id": 1, 
 
      *  "name": "string", 
 
      *  "first_line": "string", 
 
      *  "second_line": "string", 
 
      *  "city": "string", 
 
      *  "state": "string", 
 
      *  "zip": "string", 
 
      *  "iso_country_code": "string", 
 
      *  "country_name": "string", 
 
      *  "is_default_shipping_address": true 
  } 
 ] 
 
 }`
#### Documentation
  * [Guides](https://developer.etsy.com/documentation)
  * [API Reference](https://developer.etsy.com/documentation/reference)


#### Community
  * [Stack Overflow](https://stackoverflow.com/c/etsy/questions/tagged/docsbuilder)
  * [Google Group](https://groups.google.com/g/etsy-api-v2)


#### More
  * [Get help](https://developer.etsy.com/documentation/get-help)
  * [Terms of use](https://www.etsy.com/legal/api)


© 2021 Etsy, Inc.

