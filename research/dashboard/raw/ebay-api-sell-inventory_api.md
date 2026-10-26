---
title: Inventory API
description: "The **Inventory API** is used to create and manage inventory, and then to publish and manage this inventory on an eBay marketplace. There are also methods in this API that will convert eligible, active eBay listings into the Inventory API model."
api_version: 1.0
api_name: inventory_api
api_type: REST
api_group: sell/inventory_api
source_url:
  html: https://developer.ebay.com/develop/api/sell/inventory_api
  md: https://developer.ebay.com/develop/api/sell/inventory_api.md
---

# Inventory API API

The **Inventory API** is used to create and manage inventory, and then to publish and manage this inventory on an eBay marketplace. There are also methods in this API that will convert eligible, active eBay listings into the Inventory API model.

## API Methods

The following API methods are available:

### bulkCreateOrReplaceInventoryItem

#### POST /bulk_create_or_replace_inventory_item
**Description:** **Note:** Please note that any eBay listing created using the Inventory API cannot be revised or relisted using the Trading API calls.  
**Note:** Each listing can be revised up to 250 times in one calendar day. If this revision threshold is reached, the seller will be blocked from revising the item until the next calendar day.  
This call can be used to create and/or update up to 25 new inventory item records. It is up to sellers whether they want to create a complete inventory item records right from the start, or sellers can provide only some information with the initial **bulkCreateOrReplaceInventoryItem** call, and then make one or more additional **bulkCreateOrReplaceInventoryItem** calls to complete all required fields for the inventory item records and prepare for publishing. Upon first creating inventory item records, only the SKU values are required.  
  

**Important!**Publish offer note: Fields may be optional or conditionally required when calling this method, but become required when publishing the offer to create an active listing. For this method, see [Inventory item fields](</api-docs/sell/static/inventory/publishing-offers.html#inventory_item >) for a list of fields required to publish an offer.

  
**Note:** In addition to the `authorization` header, which is required for all eBay REST API calls, this call also requires the `Content-Language` and `Content-Type` headers.  
In the case of updating existing inventory item records, the **bulkCreateOrReplaceInventoryItem** call will do a complete replacement of the existing inventory item records, so all fields that are currently defined for the inventory item record are required in that update action, regardless of whether their values changed. So, when replacing/updating an inventory item record, it is advised that the seller run a 'Get' call to retrieve the full details of the inventory item records and see all of its current values/settings before attempting to update the records. Any changes that are made to inventory item records that are part of one or more active eBay listings, a successful call will automatically update these active listings.  
  
The key information that is set with the **bulkCreateOrReplaceInventoryItem** call include:

*   Seller-defined SKU value for the product. Each seller product, including products within an item inventory group, must have their own SKU value.
*   Condition of the item
*   Product details, including any product identifier(s), such as a UPC, ISBN, EAN, or Brand/Manufacturer Part Number pair, a product description, a product title, product/item aspects, and links to images. eBay will use any supplied eBay Product ID (ePID) or a GTIN (UPC, ISBN, or EAN) and attempt to match those identifiers to a product in the eBay Catalog, and if a product match is found, the product details for the inventory item will automatically be populated.
*   Quantity of the inventory item that is available for purchase
*   Package weight and dimensions, which is required if the seller will be offering calculated shipping options. The package weight will also be required if the seller will be providing flat-rate shipping services, but charging a weight surcharge.

For those who prefer to create or update a single inventory item record, the [createOrReplaceInventoryItem](/develop/api/sell/inventory_api#sell-inventory_api-inventory_item-createorreplaceinventoryitem) method can be used.
**Parameters:**
- **Content-Type** (string) *required*
  - This header indicates the format of the request body provided by the client. Its value should be set to **application/json**.
- **Content-Language** (string) *required*
  - This header sets the natural language that will be used in the field values of the request payload. For example, the value passed in this header should be `en-US` for English or `de-DE` for German.

### bulkGetInventoryItem

#### POST /bulk_get_inventory_item
**Description:** This call retrieves up to 25 inventory item records. The SKU value of each inventory item record to retrieve is specified in the request payload.  
  
**Note:** In addition to the `authorization` header, which is required for all Inventory API calls, this call also requires the `Content-Type` header.  
For those who prefer to retrieve only one inventory item record by SKU value, the [getInventoryItem](/develop/api/sell/inventory_api#sell-inventory_api-inventory_item-getinventoryitem) method can be used. To retrieve all inventory item records defined on the seller's account, the [getInventoryItems](/develop/api/sell/inventory_api#sell-inventory_api-inventory_item-getinventoryitems) method can be used (with pagination control if desired).
**Parameters:**
- **Content-Type** (string) *required*
  - This header indicates the format of the request body provided by the client. Its value should be set to **application/json**.

### bulkUpdatePriceQuantity

#### POST /bulk_update_price_quantity
**Description:** This call is used by the seller to update the total ship-to-home quantity of one inventory item, and/or to update the price and/or quantity of one or more offers associated with one inventory item. Up to 25 offers associated with an inventory item may be updated with one **bulkUpdatePriceQuantity** call. Only one SKU (one product) can be updated per call.  
  
**Note:** Each listing can be revised up to 250 times in one calendar day. If this revision threshold is reached, the seller will be blocked from revising the item until the next calendar day.  
**Note:** In addition to the `authorization` header, which is required for all Inventory API calls, this call also requires the `Content-Type` header.  
The [getOffers](/develop/api/sell/inventory_api#sell-inventory_api-offer-getoffers) call can be used to retrieve all offers associated with a SKU. The seller will just pass in the correct SKU value through the **sku** query parameter. To update an offer, the **offerId** value is required, and this value is returned in the **getOffers** call response. It is also useful to know which offers are unpublished and which ones are published. To get this status, look for the **status** value in the **getOffers** call response. Offers in the published state are live eBay listings, and these listings will be revised with a successful **bulkUpdatePriceQuantity** call.  
  
An issue will occur if duplicate **offerId** values are passed through the same **offers** container, or if one or more of the specified offers are associated with different products/SKUs.  
  
**Note:** For multiple-variation listings, it is recommended that the [bulkUpdatePriceQuantity](/develop/api/sell/inventory_api#sell-inventory_api-inventory_item-bulkupdatepricequantity) call be used to update price and quantity information for each SKU within that multiple-variation listing instead of using [createOrReplaceInventoryItem](/develop/api/sell/inventory_api#sell-inventory_api-inventory_item-createorreplaceinventoryitem) calls to update the price and quantity for each SKU. Just remember that only one SKU (one product variation) can be updated per call.
**Parameters:**
- **Content-Type** (string) *required*
  - This header indicates the format of the request body provided by the client. Its value should be set to **application/json**.

### getInventoryItem

#### GET /inventory_item/{sku}
**Description:** This call retrieves the inventory item record for a given SKU. The SKU value is passed in at the end of the call URI. There is no request payload for this call.  
  
The `authorization` header is the only required HTTP header for this call, and it is required for all Inventory API calls. See the **HTTP request headers** section for more information.  
  
For those who prefer to retrieve numerous inventory item records by SKU value with one call (up to 25 at a time), the **bulkGetInventoryItem** method can be used. To retrieve all inventory item records defined on the seller's account, the **getInventoryItems** method can be used (with pagination control if desired).
**Parameters:**
- **sku** (string) *required*
  - This path parameter specifies the seller-defined SKU value of the product whose inventory item record you wish to retrieve.  
  
Use the [getInventoryItems](/develop/api/sell/inventory_api#sell-inventory_api-inventory_item-getinventoryitems) method to retrieve SKU values.  
  
**Maximum length**: 50

### createOrReplaceInventoryItem

#### PUT /inventory_item/{sku}
**Description:** **Note:** Please note that any eBay listing created using the Inventory API cannot be revised or relisted using the Trading API calls.  
**Note:** Each listing can be revised up to 250 times in one calendar day. If this revision threshold is reached, the seller will be blocked from revising the item until the next calendar day.  
This call creates a new inventory item record or replaces an existing inventory item record. It is up to sellers whether they want to create a complete inventory item record right from the start, or sellers can provide only some information with the initial **createOrReplaceInventoryItem** call, and then make one or more additional **createOrReplaceInventoryItem** calls to complete all required fields for the inventory item record and prepare it for publishing. Upon first creating an inventory item record, only the SKU value in the call path is required.  
  

**Important!**Publish offer note: Fields may be optional or conditionally required when calling this method, but become required when publishing the offer to create an active listing. For this method, see [Inventory item fields](/api-docs/sell/static/inventory/publishing-offers.html#inventory_item) for a list of fields required to publish an offer.

  
**Note:** In addition to the `authorization` header, which is required for all Inventory API calls, this call also requires the `Content-Type` and `Content-Language` headers.  
In the case of replacing an existing inventory item record, the **createOrReplaceInventoryItem** call will do a complete replacement of the existing inventory item record, so all fields that are currently defined for the inventory item record are required in that update action, regardless of whether their values changed. So, when replacing/updating an inventory item record, it is advised that the seller run a [getInventoryItem](/develop/api/sell/inventory_api#sell-inventory_api-inventory_item-getinventoryitem) call to retrieve the full inventory item record and see all of its current values/settings before attempting to update the record. And if changes are made to an inventory item that is part of one or more active eBay listings, a successful call will automatically update these eBay listings.  
  
The key information that is set with the **createOrReplaceInventoryItem** call include:

*   The seller-defined SKU value for the product. Each seller product, including products within an item inventory group, must have their own SKU value. This SKU value is passed in at the end of the call URI.
*   The condition of the item.
*   Product details, including any product identifier(s), such as a UPC, ISBN, EAN, or Brand/Manufacturer Part Number pair, a product description, a product title, product/item aspects, and links to images. eBay will use any supplied eBay Product ID (ePID) or a GTIN (UPC, ISBN, or EAN) and attempt to match those identifiers to a product in the eBay Catalog, and if a product match is found, the product details for the inventory item will automatically be populated.
*   The quantity of the inventory item that is available for purchase.
*   Package weight and dimensions, which is required if the seller will be offering calculated shipping options. The package weight will also be required if the seller will be providing flat-rate shipping services, but charging a weight surcharge.

In addition to the `authorization` header, which is required for all eBay REST API calls, the **createOrReplaceInventoryItem** call also requires the `Content-Language` header, that sets the natural language that will be used in the field values of the request payload. For US English, the code value passed in this header should be `en-US`. To view other supported `Content-Language` values, and to read more about all supported HTTP headers for eBay REST API calls, see the [HTTP request headers](/api-docs/static/rest-request-components.html#HTTP) topic in the **Using eBay RESTful APIs** document.

For those who prefer to create or update numerous inventory item records with one call (up to 25 at a time), the [bulkCreateOrReplaceInventoryItem](/develop/api/sell/inventory_api#sell-inventory_api-inventory_item-bulkcreateorreplaceinventoryitem) method can be used.
**Parameters:**
- **Content-Language** (string) *required*
  - This header sets the natural language that will be used in the field values of the request payload. For example, the value passed in this header should be `en-US` for English or `de-DE` for German.
- **sku** (string) *required*
  - This path parameter specifies the seller-defined SKU value for the inventory item being created or updated. SKU values must be unique across the seller's inventory.  
  
**Maximum length**: 50
- **Content-Type** (string) *required*
  - This header indicates the format of the request body provided by the client. Its value should be set to **application/json**.

### deleteInventoryItem

#### DELETE /inventory_item/{sku}
**Description:** This call is used to delete an inventory item record associated with a specified SKU. A successful call will not only delete that inventory item record, but will also have the following effects:

*   Delete any and all unpublished offers associated with that SKU;
*   Delete any and all single-variation eBay listings associated with that SKU;
*   Automatically remove that SKU from a multiple-variation listing and remove that SKU from any and all inventory item groups in which that SKU was a member.

The `authorization` header is the only required HTTP header for this call. See the **HTTP request headers** section for more information.
**Parameters:**
- **sku** (string) *required*
  - This path parameter specifies the seller-defined SKU value of the product whose inventory item record you wish to delete.  
  
Use the [getInventoryItems](/develop/api/sell/inventory_api#sell-inventory_api-inventory_item-getinventoryitems) method to retrieve SKU values.  
  
**Maximum length**: 50

### getInventoryItems

#### GET /inventory_item
**Description:** This call retrieves all inventory item records defined for the seller's account. The **limit** query parameter allows the seller to control how many records are returned per page, and the **offset** query parameter is used to retrieve a specific page of records. The seller can make multiple calls to scan through multiple pages of records. There is no request payload for this call.  
  
The `authorization` header is the only required HTTP header for this call, and it is required for all Inventory API calls. See the **HTTP request headers** section for more information.  
  
For those who prefer to retrieve numerous inventory item records by SKU value with one call (up to 25 at a time), the **bulkGetInventoryItem** method can be used.
**Parameters:**
- **limit** (string)
  - The value passed in this query parameter sets the maximum number of records to return per page of data. Although this field is a string, the value passed in this field should be an integer from `1` to `200`.  
  
**Min:** 1  
  
**Max:** 200  
  
**Default:** 25
- **offset** (string)
  - The value passed in this query parameter sets the page number to retrieve. The first page of records has a value of `0`, the second page of records has a value of `1`, and so on. If this query parameter is not set, its value defaults to `0`, and the first page of records is returned.

### getProductCompatibility

#### GET /inventory_item/{sku}/product_compatibility
**Description:** This call is used by the seller to retrieve the list of products that are compatible with the inventory item. The SKU value for the inventory item is passed into the call URI, and a successful call with return the compatible vehicle list associated with this inventory item. Product compatibility is currently only applicable to motor vehicle parts and accessory categories, but more categories may be supported in the future.
**Parameters:**
- **sku** (string) *required*
  - This path parameter specifies the SKU (stock keeping unit) of the inventory item associated with the product compatibility list being retrieved.  
  
Use the [getInventoryItems](/develop/api/sell/inventory_api#sell-inventory_api-inventory_item-getinventoryitems) method to retrieve SKU values.

### createOrReplaceProductCompatibility

#### PUT /inventory_item/{sku}/product_compatibility
**Description:** This call is used by the seller to create or replace a list of products that are compatible with the inventory item. The inventory item is identified with a SKU value in the URI. Product compatibility is currently only applicable to motor vehicle parts and accessory categories, but more categories may be supported in the future.  
  
**Note:** In addition to the `authorization` header, which is required for all Inventory API calls, this call also requires the `Content-Type` and `Content-Language` headers.
**Parameters:**
- **Content-Language** (string) *required*
  - This header sets the natural language that will be used in the field values of the request payload. For example, the value passed in this header should be `en-US` for English or `de-DE` for German.
- **sku** (string) *required*
  - This path parameter specifies the SKU (stock keeping unit) of the inventory item associated with the compatibility list being created.  
  
Use the [getInventoryItems](/develop/api/sell/inventory_api#sell-inventory_api-inventory_item-getinventoryitems) method to retrieve SKU values.
- **Content-Type** (string) *required*
  - This header indicates the format of the request body provided by the client. Its value should be set to **application/json**.

### deleteProductCompatibility

#### DELETE /inventory_item/{sku}/product_compatibility
**Description:** This call is used by the seller to delete the list of products that are compatible with the inventory item that is associated with the compatible product list. The inventory item is identified with a SKU value in the URI. Product compatibility is currently only applicable to motor vehicle parts and accessory categories, but more categories may be supported in the future.
**Parameters:**
- **sku** (string) *required*
  - This path parameter specifies the SKU (stock keeping unit) of the inventory item that is associated with the product compatibility list that is being deleted.  
  
Use the [getInventoryItems](/develop/api/sell/inventory_api#sell-inventory_api-inventory_item-getinventoryitems) method to retrieve SKU values.

### getInventoryItemGroup

#### GET /inventory_item_group/{inventoryItemGroupKey}
**Description:** This call retrieves the inventory item group for a given **inventoryItemGroupKey** value. The **inventoryItemGroupKey** value is passed in at the end of the call URI.
**Parameters:**
- **inventoryItemGroupKey** (string) *required*
  - This path parameter specifies the unique identifier of the inventory item group being retrieved. This value is assigned by the seller when an inventory item group is created.

### createOrReplaceInventoryItemGroup

#### PUT /inventory_item_group/{inventoryItemGroupKey}
**Description:** **Note:** Each listing can be revised up to 250 times in one calendar day. If this revision threshold is reached, the seller will be blocked from revising the item until the next calendar day.  
This call creates a new inventory item group or updates an existing inventory item group. It is up to sellers whether they want to create a complete inventory item group record right from the start, or sellers can provide only some information with the initial **createOrReplaceInventoryItemGroup** call, and then make one or more additional **createOrReplaceInventoryItemGroup** calls to complete the inventory item group record. Upon first creating an inventory item group record, the only required elements are the [inventoryItemGroupKey](/develop/api/sell/inventory_api#sell-inventory_api-inventory_item_group-createorreplaceinventoryitemgroup.inventoryitemgroup.subtitle) identifier in the call URI, and the members of the inventory item group specified through the [variantSKUs](/develop/api/sell/inventory_api#sell-inventory_api-inventory_item_group-createorreplaceinventoryitemgroup.inventoryitemgroup.variantskus) array in the request payload.  
  

**Important!**Publish offer note: Fields may be optional or conditionally required when calling this method, but become required when publishing the offer to create an active listing. For this method, see [Inventory item group fields](/api-docs/sell/static/inventory/publishing-offers.html#inventory_item_group) for a list of fields required to publish an offer.

  
**Note:** In addition to the `authorization` header, which is required for all Inventory API calls, this call also requires the `Content-Type` and `Content-Language` headers.  
In the case of updating/replacing an existing inventory item group, this call does a complete replacement of the existing inventory item group record, so all fields (including the member SKUs) that make up the inventory item group are required, regardless of whether their values changed. So, when replacing/updating an inventory item group record, it is advised that the seller run a [getInventoryItemGroup](/develop/api/sell/inventory_api#sell-inventory_api-inventory_item_group-getinventoryitemgroup) call for that inventory item group to see all of its current values/settings/members before attempting to update the record. And if changes are made to an inventory item group that is part of a live, multiple-variation eBay listing, these changes automatically update the eBay listing. For example, if a SKU value is removed from the inventory item group, the corresponding product variation will be removed from the eBay listing as well.  
  
In addition to the required inventory item group identifier and member SKUs, other key information that is set with this call include:

*   Title and description of the inventory item group. The string values provided in these fields will actually become the listing title and listing description of the listing once the first SKU of the inventory item group is published successfully
*   Common aspects that inventory items in the group share
*   Product aspects that vary within each product variation
*   Links to images demonstrating the variations of the product, and these images should correspond to the product aspect that is set with the [variesBy.aspectsImageVariesBy](/develop/api/sell/inventory_api#sell-inventory_api-listing-bulkmigratelisting) field

  
**Note:** For more information, see [Creating and managing inventory item groups](/api-docs/sell/static/inventory/inventory-item-groups.html).
**Parameters:**
- **Content-Language** (string) *required*
  - This header sets the natural language that will be used in the field values of the request payload. For example, the value passed in this header should be `en-US` for English or `de-DE` for German.
- **inventoryItemGroupKey** (string) *required*
  - This path parameter specifies the unique identifier of the inventory item group being created or updated. This identifier is defined by the seller.  
  
This value cannot be changed once it is set.  
  
**Maximum length:** 50
- **Content-Type** (string) *required*
  - This header indicates the format of the request body provided by the client. Its value should be set to **application/json**.

### deleteInventoryItemGroup

#### DELETE /inventory_item_group/{inventoryItemGroupKey}
**Description:** This call deletes the inventory item group for a given **inventoryItemGroupKey** value.
**Parameters:**
- **inventoryItemGroupKey** (string) *required*
  - This path parameter specifies the unique identifier of the inventory item group being deleted. This value is assigned by the seller when an inventory item group is created.

### bulkMigrateListing

#### POST /bulk_migrate_listing
**Description:** This call is used to convert existing eBay Listings to the corresponding Inventory API objects. If an eBay listing is successfully migrated to the Inventory API model, new Inventory Location, Inventory Item, and Offer objects are created. For a multiple-variation listing that is successfully migrated, in addition to the three new Inventory API objects just mentioned, an Inventory Item Group object will also be created. If the eBay listing is a motor vehicle part or accessory listing with a compatible vehicle list (**ItemCompatibilityList** container in Trading API's Add/Revise/Relist/Verify calls), a Product Compatibility object will be created.  
  

#### Migration Requirements

  
To be eligible for migration, the active eBay listings must meet the following requirements:

*   Listing type is Fixed-Price
    
    **Note:** Auction listings are supported by the Inventory API, but the **bulkMigrateListing** method cannot be used to migrate auction listings.
    
*   The item(s) in the listings must have seller-defined SKU values associated with them, and in the case of a multiple-variation listing, each product variation must also have its own SKU value
*   Business Polices (Payment, Return Policy, and Shipping) must be used on the listing, as legacy payment, return policy, and shipping fields will not be accepted. With the Payment Policy associated with a listing, the immediate payment requirement must be enabled.
*   The postal/zip code (**PostalCode** field in Trading's **ItemType**) or city (**Location** field in Trading's **ItemType**) must be set in the listing; the country is also needed, but this value is required in Trading API, so it will always be set for every listing

  

### Unsupported Listing Features

  
The following features are not yet available to be set or modified through the Inventory API, but they will remain on the active eBay listing, even after a successful migration to the Inventory model. The downside to this is that the seller will be completely blocked (in APIs or My eBay) from revising these features/settings once the migration takes place:

*   Any listing-level Buyer Requirements
*   Listing enhancements like a bold listing title or Gallery Plus

  

### Making the Call

  
In the request payload of the **bulkMigrateListings** call, the seller will pass in an array of one to five eBay listing IDs (aka Item IDs). To save time and hassle, that seller should do a pre-check on each listing to make sure those listings meet the requirements to be migrated to the new Inventory model. This method also requires the `Content-Type` request header. There are no path or query parameters for this call.  
  

### Call Response

  
If an eBay listing is migrated successfully to the new Inventory model, the following will occur:

*   An Inventory Item object will be created for the item(s) in the listing, and this object will be accessible through the Inventory API
*   An Offer object will be created for the listing, and this object will be accessible through the Inventory API
*   An Inventory Location object will be created and associated with the Offer object, as an Inventory Location must be associated with a published Offer

The response payload of the Bulk Migrate Listings call will show the results of each listing migration. These results include an HTTP status code to indicate the success or failure of each listing migration, the SKU value associated with each item, and if the migration is successful, an Offer ID value. The SKU value will be used in the Inventory API to manage the Inventory Item object, and the Offer ID value will be used in the Inventory API to manage the Offer object. Errors and/or warnings containers will be returned for each listing where an error and/or warning occurred with the attempted migration.  
  
If a multiple-variation listing is successfully migrated, along with the Offer and Inventory Location objects, an Inventory Item object will be created for each product variation within the listing, and an Inventory Item Group object will also be created, grouping those variations together in the Inventory API platform. For a motor vehicle part or accessory listing that has a specified list of compatible vehicles, in addition to the Inventory Item, Inventory Location, and Offer objects that are created, a Product Compatibility object will also be created in the Inventory API platform.
**Parameters:**
- **Content-Type** (string) *required*
  - This header indicates the format of the request body provided by the client. Its value should be set to **application/json**.

### getSkuLocationMapping

#### GET /listing/{listingId}/sku/{sku}/locations
**Description:** This method allows sellers to retrieve the locations mapped to a specific SKU within a listing.  
  
The **listingId** and **sku** of the listing are passed in as path parameters. This method only retrieves location mappings for a single SKU value; if a seller wishes to retrieve the location mappings for all items in a multiple-variation listing, this method must be called for each variation in the listing.  
  
If there are fulfillment center locations mapped to the SKU, they will be returned in the **locations** array. If no locations are mapped to the SKU, status code **404 Not Found** will be returned.
**Parameters:**
- **listingId** (string) *required*
  - This path parameter specifies the unique identifier of the listing that the SKU belongs to for which all mapped locations will be retrieved.  
  
Use the [getOffers](/develop/api/sell/inventory_api#sell-inventory_api-offer-getoffers) method of the **Inventory API** or the [GetMyEbaySelling](/devzone/xml/docs/reference/ebay/getmyebayselling.html) method of the **Trading API** to retrieve all listing IDs for all active listings.
- **sku** (string) *required*
  - This path parameter specifies the seller-defined SKU value of the item/variation for which location mappings will be retrieved. This SKU value must be defined in the listing specified in **listingId** parameter  
  
Use the [getOffers](/develop/api/sell/inventory_api#sell-inventory_api-offer-getoffers) method of the **Inventory API** or the [GetMyEbaySelling](/devzone/xml/docs/reference/ebay/getmyebayselling.html) method of the **Trading API** to retrieve all SKUs for all active listings.

### createOrReplaceSkuLocationMapping

#### PUT /listing/{listingId}/sku/{sku}/locations
**Description:** This method allows sellers to map multiple fulfillment center locations to single-SKU listing, or to a single SKU within a multiple-variation listing. This allows eBay to leverage the location metadata associated with a seller's fulfillment centers to calculate more accurate estimated delivery dates on their listing.  
  
**Note:** While location mappings can be created for listings on any eBay marketplace, the improved delivery date estimate feature is currently only supported for US-based fulfillment centers shipping domestically within the US.  
The listing for which the locations will be mapped is specified through the **listingId** and **sku** values associated with the item. Note that only a single SKU value can be identified; if the seller wishes to map locations to multiple/all SKU values in a multiple-variation listing, this method must be called for each of those SKUs within the listing.  
  
**Note:** Sellers should keep track of **listingId**/**sku** pairs that have been used for location mapping, as there is no programmatic way to retrieve or delete these pairs at this time.  
In the case of replacing/updating existing location mappings, this method will do a complete replacement of the location mappings associated with a SKU. This means that each existing location mappings that the seller wants to continue to associate with the SKU are required in the update call, regardless of if they are affected by the update.  
  
This method is only supported for inventory locations that have `FULFILLMENT_CENTER` as one of their **locationTypes**. For more information on fulfillment center locations, see [Create a fulfillment center location](/api-docs/sell/static/inventory/multi-warehouse-program.html#create-location).  
  
For more information on location mapping features, see [Multi-warehouse program](/api-docs/sell/static/inventory/multi-warehouse-program.html) in the Selling Integration Guide.  
  
**Note:** Only listings with SKU values are supported. Sellers using listings creating through the Trading API can add a SKU value to their single variation listing through the [Item.SKU](/Devzone/XML/docs/Reference/eBay/AddFixedPriceItem.html#Request.Item.SKU) field during listing creation or by using the **ReviseItem** family of calls.
**Parameters:**
- **listingId** (string) *required*
  - This path parameter specifies the unique identifier of the listing for which multiple fulfillment center locations will be mapped to a SKU within that listing.  
  
Use the [getOffers](/develop/api/sell/inventory_api#sell-inventory_api-offer-getoffers) method of the Inventory API or the [GetMyEbaySelling](/devzone/xml/docs/reference/ebay/getmyebayselling.html) method of the Trading API to retrieve all listing IDs for all active listings.
- **sku** (string) *required*
  - This path parameter specifies the seller-defined SKU value of the item/variation for which multiple fulfillment center locations will be mapped. This SKU value must be defined in the listing specified in **listingId** parameter.  
  
Use the [getOffers](/develop/api/sell/inventory_api#sell-inventory_api-offer-getoffers) method of the Inventory API or the [GetMyEbaySelling](/devzone/xml/docs/reference/ebay/getmyebayselling.html) method of the Trading API to retrieve all listing IDs for all active listings.  
  
**Note:** SKU values can be updated by a seller at any time. If a seller updates a SKU value that is being used for location mapping, this change will not be reflected until the mapping is updated through the **createOrReplaceSkuLocationMapping** method.
- **Content-Type** (string) *required*
  - This header indicates the format of the request body provided by the client. Its value should be set to **application/json**.

### deleteSkuLocationMapping

#### DELETE /listing/{listingId}/sku/{sku}/locations
**Description:** This method allows sellers to remove all location mappings associated with a specific SKU within a listing.  
  
The **listingId** and **sku** of the listing are passed in as path parameters.  
  

**Important!** To remove all location mappings from a multiple-variation listing, this method must be used for each individual SKU in the listing.
**Parameters:**
- **listingId** (string) *required*
  - This path parameter specifies the unique identifier of the listing that the SKU belongs to for which all mapped locations will be removed.  
  
Use the [getOffers](/develop/api/sell/inventory_api#sell-inventory_api-offer-getoffers) method of the **Inventory API** or the [GetMyEbaySelling](/devzone/xml/docs/reference/ebay/getmyebayselling.html) method of the **Trading API** to retrieve all listing IDs for all active listings.
- **sku** (string) *required*
  - This path parameter specifies the seller-defined SKU value of the item/variation for which location mappings will be removed. This SKU value must be defined in the listing specified in **listingId** parameter  
  
Use the [getOffers](/develop/api/sell/inventory_api#sell-inventory_api-offer-getoffers) method of the **Inventory API** or the [GetMyEbaySelling](/devzone/xml/docs/reference/ebay/getmyebayselling.html) method of the **Trading API** to retrieve all SKUs for all active listings.

### bulkCreateOffer

#### POST /bulk_create_offer
**Description:** This call creates multiple offers (up to 25) for specific inventory items on a specific eBay marketplace. Although it is not a requirement for the seller to create complete offers (with all necessary details) right from the start, eBay recommends that the seller provide all necessary details with this call since there is currently no bulk operation available to update multiple offers with one call. The following fields are always required in the request payload: [sku](/develop/api/sell/inventory_api#sell-inventory_api-offer-bulkcreateoffer.ebayofferdetailswithkeys.sku), [marketplaceId](/develop/api/sell/inventory_api#sell-inventory_api-offer-bulkcreateoffer.ebayofferdetailswithkeys.marketplaceid), and (listing) [format](/develop/api/sell/inventory_api#sell-inventory_api-offer-bulkcreateoffer.ebayofferdetailswithkeys.format).  
  

**Important!**Publish offer note: Fields may be optional or conditionally required when calling this method, but become required when publishing the offer to create an active listing. For this method, see [Offer fields](/api-docs/sell/static/inventory/publishing-offers.html#offer) for a list of fields required to publish an offer.

  
Other information that will be required before a offer can be published are highlighted below:

*   Inventory location
*   Offer price
*   Available quantity
*   eBay listing category
*   Referenced listing policy profiles to set payment, return, and fulfillment values/settings

**Note:** Though the [includeCatalogProductDetails](/develop/api/sell/inventory_api#sell-inventory_api-offer-bulkcreateoffer.ebayofferdetailswithkeys.includecatalogproductdetails) parameter is not required to be submitted in the request, the parameter defaults to `true` if omitted.  
**Note:** In addition to the `authorization` header, which is required for all Inventory API calls, this call also requires the `Content-Type` and `Content-Language` headers.

If the call is successful, unique [offerId](/develop/api/sell/inventory_api#sell-inventory_api-offer-bulkcreateoffer.offerskuresponse.offerid) values are returned in the response for each successfully created offer. The **offerId** value will be required for many other offer-related calls. Note that this call only stages an offer for publishing. The seller must run either the [publishOffer](/develop/api/sell/inventory_api#sell-inventory_api-offer-publishoffer), [bulkPublishOffer](/develop/api/sell/inventory_api#sell-inventory_api-offer-bulkpublishoffer), or [publishOfferByInventoryItemGroup](/develop/api/sell/inventory_api#sell-inventory_api-offer-publishofferbyinventoryitemgroup) call to convert offer(s) into an active single- or multiple-variation listing.

For those who prefer to create a single offer per call, the [createOffer](/develop/api/sell/inventory_api#sell-inventory_api-offer-createoffer) method can be used instead.
**Parameters:**
- **Content-Language** (string) *required*
  - This header sets the natural language that will be used in the field values of the request payload. For example, the value passed in this header should be `en-US` for English or `de-DE` for German.
- **Content-Type** (string) *required*
  - This header indicates the format of the request body provided by the client. Its value should be set to **application/json**.

### bulkPublishOffer

#### POST /bulk_publish_offer
**Description:** **Note:** Each listing can be revised up to 250 times in one calendar day. If this revision threshold is reached, the seller will be blocked from revising the item until the next calendar day.  
This call is used to convert unpublished offers (up to 25) into published offers, or live eBay listings. The unique identifier ([offerId](/develop/api/sell/inventory_api#sell-inventory_api-offer-bulkpublishoffer.offerkeywithid.offerid)) of each offer to publish is passed into the request payload. It is possible that some unpublished offers will be successfully created into eBay listings, but others may fail. The response payload will show the results for each **offerId** value that is passed into the request payload. The [errors](/develop/api/sell/inventory_api#sell-inventory_api-offer-bulkpublishoffer.offerresponsewithlistingid.errors) and [warnings](/develop/api/sell/inventory_api#sell-inventory_api-offer-bulkpublishoffer.offerresponsewithlistingid.warnings) containers will be returned for an offer that had one or more issues being published.  
  

**Important!**Publish offer note: Fields may be optional or conditionally required when calling the create or update methods, but become required when publishing the offer to create active listings. For this method, see [Offer fields](/api-docs/sell/static/inventory/publishing-offers.html#offer) for a list of fields required to publish an offer.

  
For those who prefer to publish one offer per call, the [publishOffer](/develop/api/sell/inventory_api#sell-inventory_api-offer-publishoffer) method can be used instead. In the case of a multiple-variation listing, the [publishOfferByInventoryItemGroup](/develop/api/sell/inventory_api#sell-inventory_api-offer-publishofferbyinventoryitemgroup) call should be used instead, as this call will convert all unpublished offers associated with an inventory item group into a multiple-variation listing.
**Parameters:**
- **Content-Type** (string) *required*
  - This header indicates the format of the request body provided by the client. Its value should be set to **application/json**.

### getOffers

#### GET /offer
**Description:** This call retrieves all existing offers for the specified SKU value. The seller has the option of limiting the offers that are retrieved to a specific eBay marketplace, or to a listing format.  
  
**Note:** At this time, the same SKU value can not be offered across multiple eBay marketplaces, so the **marketplace\_id** query parameter currently does not have any practical use for this call.  
**Note:** The same SKU can be offered through an auction and a fixed-price listing concurrently. If this is the case, **getOffers** will return two offers. Otherwise, only one offer will be returned.  
The `authorization` header is the only required HTTP header for this call. See the **HTTP request headers** section for more information.
**Parameters:**
- **format** (string)
  - This enumeration value sets the listing format for the offers being retrieved. This query parameter will be passed in if the seller only wants to see offers in a specified listing format, such as `FIXED_PRICE`.
- **limit** (string)
  - The value passed in this query parameter sets the maximum number of records to return per page of data. Although this field is a string, the value passed in this field should be a positive integer value. If this query parameter is not set, up to 100 records will be returned on each page of results.
- **marketplace_id** (string)
  - The unique identifier of the eBay marketplace. This query parameter will be passed in if the seller only wants to see the product's offers on a specific eBay marketplace.  
  
**Note:** At this time, the same SKU value can not be offered across multiple eBay marketplaces, so the **marketplace\_id** query parameter currently does not have any practical use for this call.
- **offset** (string)
  - The value passed in this query parameter sets the page number to retrieve. Although this field is a string, the value passed in this field should be a integer value equal to or greater than `0`. The first page of records has a value of `0`, the second page of records has a value of `1`, and so on. If this query parameter is not set, its value defaults to `0`, and the first page of records is returned.
- **sku** (string) *required*
  - The seller-defined SKU value is passed in as a query parameter. All offers associated with this product are returned in the response.  
  
**Note:** The same SKU can be offered through an auction and a fixed-price listing concurrently. If this is the case, **getOffers** will return two offers. Otherwise, only one offer will be returned.  
Use the [getInventoryItems](/develop/api/sell/inventory_api#sell-inventory_api-inventory_item-getinventoryitems) method to retrieve SKU values.  
  
**Maximum length**: 50.

### createOffer

#### POST /offer
**Description:** This call creates an offer for a specific inventory item on a specific eBay marketplace. It is up to the sellers whether they want to create a complete offer (with all necessary details) right from the start, or sellers can provide only some information with the initial **createOffer** call, and then make one or more subsequent [updateOffer](/develop/api/sell/inventory_api#sell-inventory_api-offer-updateoffer) calls to complete the offer and prepare to publish the offer. Upon first creating an offer, the following fields are required in the request payload: [sku](/develop/api/sell/inventory_api#sell-inventory_api-offer-createoffer.ebayofferdetailswithkeys.sku), [marketplaceId](/develop/api/sell/inventory_api#sell-inventory_api-offer-createoffer.ebayofferdetailswithkeys.marketplaceid), and (listing) [format](/develop/api/sell/inventory_api#sell-inventory_api-offer-createoffer.ebayofferdetailswithkeys.format).  
  

**Important!**Publish offer note: Fields may be optional or conditionally required when calling this method, but become required when publishing the offer to create an active listing. For this method, see [Offer fields](/api-docs/sell/static/inventory/publishing-offers.html#offer) for a list of fields required to publish an offer.

  
Other information that will be required before an offer can be published are highlighted below. These settings are either set with **createOffer**, or they can be set with a subsequent **updateOffer** call:

*   Inventory location
*   Offer price
*   Available quantity
*   eBay listing category
*   Referenced listing policy profiles to set payment, return, and fulfillment values/settings

**Note:** Though the [includeCatalogProductDetails](/develop/api/sell/inventory_api#sell-inventory_api-offer-bulkcreateoffer.ebayofferdetailswithkeys.includecatalogproductdetails) parameter is not required to be submitted in the request, the parameter defaults to `true` if omitted.

**Note:** In addition to the `authorization` header, which is required for all Inventory API calls, this call also requires the `Content-Type` and `Content-Language` headers.

If the call is successful, a unique [offerId](/develop/api/sell/inventory_api#sell-inventory_api-offer-bulkcreateoffer.offerskuresponse.offerid) value is returned in the response. This value will be required for many other offer-related calls. Note that this call only stages an offer for publishing. The seller must run the [publishOffer](/develop/api/sell/inventory_api#sell-inventory_api-offer-publishoffer) call to convert the offer to an active eBay listing.

For those who prefer to create multiple offers (up to 25 at a time) with one call, the [bulkCreateOffer](/develop/api/sell/inventory_api#sell-inventory_api-offer-bulkcreateoffer) method can be used.
**Parameters:**
- **Content-Language** (string) *required*
  - This header sets the natural language that will be used in the field values of the request payload. For example, the value passed in this header should be `en-US` for English or `de-DE` for German.
- **Content-Type** (string) *required*
  - This header indicates the format of the request body provided by the client. Its value should be set to **application/json**.

### getOffer

#### GET /offer/{offerId}
**Description:** This call retrieves a specific published or unpublished offer. The unique identifier of the offer (**offerId**) is passed in at the end of the call URI.

The `authorization` header is the only required HTTP header for this call. See the **HTTP request headers** section for more information.
**Parameters:**
- **offerId** (string) *required*
  - This path parameter specifies the unique identifier of the offer that is to be retrieved.  
  
Use the [getOffers](/develop/api/sell/inventory_api#sell-inventory_api-offer-getoffers) method to retrieve offer IDs.

### updateOffer

#### PUT /offer/{offerId}
**Description:** This call updates an existing offer. An existing offer may be in published state (active eBay listing), or in an unpublished state and yet to be published with the [publishOffer](/develop/api/sell/inventory_api#sell-inventory_api-offer-publishoffer) call. The unique identifier (**offerId**) for the offer to update is passed in at the end of the call URI.  
  
The **updateOffer** call does a complete replacement of the existing offer object, so all fields that make up the current offer object are required, regardless of whether their values changed.  
  

**Important!**Publish offer note: Fields may be optional or conditionally required when calling this method, but become required when publishing the offer to create an active listing. For this method, see [Offer fields](/api-docs/sell/static/inventory/publishing-offers.html#offer) for a list of fields required to publish an offer.

  
Other information that is required before an unpublished offer can be published or before a published offer can be revised include:

*   Inventory location
*   Offer price
*   Available quantity
*   eBay listing category
*   Referenced listing policy profiles to set payment, return, and fulfillment values/settings

**Note:** Though the **includeCatalogProductDetails** parameter is not required to be submitted in the request, the parameter defaults to `true` if omitted from both the **updateOffer** and the **createOffer** calls. If a value is specified in the **updateOffer** call, this value will be used.  
**Note:** In addition to the `authorization` header, which is required for all Inventory API calls, this call also requires the `Content-Type` and `Content-Language` headers.  
**Note:** Each listing can be revised up to 250 times in one calendar day. If this revision threshold is reached, the seller will be blocked from revising the item until the next calendar day.

For published offers, the **listingDescription** field is also required to update the offer/eBay listing. For unpublished offers, this field is not necessarily required unless it is already set for the unpublished offer.
**Parameters:**
- **Content-Language** (string) *required*
  - This header sets the natural language that will be used in the field values of the request payload. For example, the value passed in this header should be `en-US` for English or `de-DE` for German.
- **offerId** (string) *required*
  - This path parameter specifies the unique identifier of the offer being updated.  
  
Use the [getOffers](/develop/api/sell/inventory_api#sell-inventory_api-offer-getoffers) method to retrieve offer IDs.
- **Content-Type** (string) *required*
  - This header indicates the format of the request body provided by the client. Its value should be set to **application/json**.

### deleteOffer

#### DELETE /offer/{offerId}
**Description:** If used against an unpublished offer, this call will permanently delete that offer. In the case of a published offer (or live eBay listing), a successful call will either end the single-variation listing associated with the offer, or it will remove that product variation from the eBay listing and also automatically remove that product variation from the inventory item group. In the case of a multiple-variation listing, the **deleteOffer** will not remove the product variation from the listing if that variation has one or more sales. If that product variation has one or more sales, the seller can alternately just set the available quantity of that product variation to `0`, so it is not available in the eBay search or View Item page, and then the seller can remove that product variation from the inventory item group at a later time.
**Parameters:**
- **offerId** (string) *required*
  - This path parameter specifies the unique identifier of the offer being deleted.  
  
Use the [getOffers](/develop/api/sell/inventory_api#sell-inventory_api-offer-getoffers) method to retrieve offer IDs.

### getListingFees

#### POST /offer/get_listing_fees
**Description:** This call is used to retrieve the expected listing fees for up to 250 unpublished offers. An array of one or more [\>offerId](/develop/api/sell/inventory_api#sell-inventory_api-offer-getlistingfees.offerkeywithid.offerid) values are passed in under the [offers](/develop/api/sell/inventory_api#sell-inventory_api-offer-getlistingfees.offerkeyswithid.offers) container.  
  
In the response payload, all listing fees are grouped by eBay marketplace, and listing fees per offer are not shown. A [fees](/develop/api/sell/inventory_api#sell-inventory_api-offer-getlistingfees.feesummary.fees) container will be returned for each eBay marketplace where the seller is selling the products associated with the specified offers.  
  
Errors will occur if the seller passes in **offerIds** that represent published offers, so this call should be made before the seller publishes offers with the [publishOffer](/develop/api/sell/inventory_api#sell-inventory_api-offer-publishoffer).
**Parameters:**
- **Content-Type** (string) *required*
  - This header indicates the format of the request body provided by the client. Its value should be set to **application/json**.

### publishOffer

#### POST /offer/{offerId}/publish
**Description:** **Note:** Each listing can be revised up to 250 times in one calendar day. If this revision threshold is reached, the seller will be blocked from revising the item until the next calendar day.  
This call is used to convert an unpublished offer into a published offer, or live eBay listing. The unique identifier of the offer (**offerId**) is passed in at the end of the call URI.  
  

**Important!**Publish offer note: Fields may be optional or conditionally required when calling the create or update methods, but become required when publishing the offer to create active listings. For this method, see [Offer fields](/api-docs/sell/static/inventory/publishing-offers.html#offer) for a list of fields required to publish an offer.

  
For those who prefer to publish multiple offers (up to 25 at a time) with one call, the [bulkPublishOffer](/develop/api/sell/inventory_api#sell-inventory_api-offer-bulkpublishoffer) method can be used. In the case of a multiple-variation listing, the [publishOfferByInventoryItemGroup](/develop/api/sell/inventory_api#sell-inventory_api-offer-publishofferbyinventoryitemgroup) call should be used instead, as this call will convert all unpublished offers associated with an inventory item group into a multiple-variation listing.
**Parameters:**
- **offerId** (string) *required*
  - This path parameter specifies the unique identifier of the offer that is to be published.  
  
Use the [getOffers](/develop/api/sell/inventory_api#sell-inventory_api-offer-getoffers) method to retrieve offer IDs.

### publishOfferByInventoryItemGroup

#### POST /offer/publish_by_inventory_item_group
**Description:** **Note:** Please note that any eBay listing created using the Inventory API cannot be revised or relisted using the Trading API calls.  
**Note:** Each listing can be revised up to 250 times in one calendar day. If this revision threshold is reached, the seller will be blocked from revising the item until the next calendar day.  
This call is used to convert all unpublished offers associated with an inventory item group into an active, multiple-variation listing.  
  

**Important!**Publish offer note: Fields may be optional or conditionally required when calling the create or update methods, but become required when publishing the offer to create active listings. For this method, see [Offer fields](/api-docs/sell/static/inventory/publishing-offers.html#offer) for a list of fields required to publish an offer.

  
The unique identifier of the inventory item group ([inventoryItemGroupKey](/develop/api/sell/inventory_api#sell-inventory_api-offer-publishofferbyinventoryitemgroup.publishbyinventoryitemgrouprequest.inventoryitemgroupkey)) is passed in the request payload. All inventory items and their corresponding offers in the inventory item group must be valid (meet all requirements) for the **publishOfferByInventoryItemGroup** call to be completely successful. For any inventory items in the group that are missing required data or have no corresponding offers, the **publishOfferByInventoryItemGroup** will create a new multiple-variation listing, but any inventory items with missing required data/offers will not be in the newly-created listing. If any inventory items in the group to be published have invalid data, or one or more of the inventory items have conflicting data with one another, the **publishOfferByInventoryItemGroup** call will fail. Be sure to check for any error or warning messages in the call response for any applicable information about one or more inventory items/offers having issues.
**Parameters:**
- **Content-Type** (string) *required*
  - This header indicates the format of the request body provided by the client. Its value should be set to **application/json**.

### withdrawOffer

#### POST /offer/{offerId}/withdraw
**Description:** This call is used to end a single-variation listing that is associated with the specified offer. This call is used in place of the [deleteOffer](/develop/api/sell/inventory_api#sell-inventory_api-offer-deleteoffer) call if the seller only wants to end the listing associated with the offer but does not want to delete the offer object. With this call, the offer object remains, but it goes into the unpublished state, and will require a [publishOffer](/develop/api/sell/inventory_api#sell-inventory_api-offer-publishoffer) call to relist the offer.  
  
To end a multiple-variation listing that is associated with an inventory item group, the [withdrawOfferByInventoryItemGroup](/develop/api/sell/inventory_api#sell-inventory_api-offer-withdrawofferbyinventoryitemgroup) method can be used. This call only ends the multiple-variation listing associated with an inventory item group but does not delete the inventory item group object, nor does it delete any of the offers associated with the inventory item group, but instead all of these offers go into the unpublished state.
**Parameters:**
- **offerId** (string) *required*
  - This path parameter specifies the unique identifier of the offer that is to be withdrawn.  
  
Use the [getOffers](/develop/api/sell/inventory_api#sell-inventory_api-offer-getoffers) method to retrieve offer IDs.

### withdrawOfferByInventoryItemGroup

#### POST /offer/withdraw_by_inventory_item_group
**Description:** This call is used to end a multiple-variation eBay listing that is associated with the specified inventory item group. This call only ends multiple-variation eBay listing associated with the inventory item group but does not delete the inventory item group object. Similarly, this call also does not delete any of the offers associated with the inventory item group, but instead all of these offers go into the unpublished state. If the seller wanted to relist the multiple-variation eBay listing, they could use the [publishOfferByInventoryItemGroup](/develop/api/sell/inventory_api#sell-inventory_api-offer-publishofferbyinventoryitemgroup) method.
**Parameters:**
- **Content-Type** (string) *required*
  - This header indicates the format of the request body provided by the client. Its value should be set to **application/json**.

### getInventoryLocation

#### GET /location/{merchantLocationKey}
**Description:** This call retrieves all defined details of the inventory location that is specified by the **merchantLocationKey** path parameter.  
  
A successful call will return an HTTP status value of `200 OK`.
**Parameters:**
- **merchantLocationKey** (string) *required*
  - This path parameter specifies the unique merchant-defined key (ID) for an inventory location that is being retrieved.  
  
Use the [getInventoryLocations](/develop/api/sell/inventory_api#sell-inventory_api-location-getinventorylocations) method to retrieve merchant location keys.  
  
**Maximum length**: 36

### createInventoryLocation

#### POST /location/{merchantLocationKey}
**Description:** Use this call to create a new inventory location. In order to create and publish an offer (and create an eBay listing), a seller must have at least one location, as every offer must be associated with at least one location.  
  

**Important!**Publish offer note: Fields may be optional or conditionally required when calling this method, but become required when publishing the offer to create an active listing. For this method, see [Location fields](</api-docs/sell/static/inventory/publishing-offers.html#location >) for a list of fields required to publish an offer.

  
Upon first creating an inventory location, only a seller-defined location identifier and a physical location is required, and once set, these values can not be changed. The unique identifier value ([merchantLocationKey](/develop/api/sell/inventory_api#sell-inventory_api-location-getinventorylocations.inventorylocationresponse.merchantlocationkey)) is passed in at the end of the call URI. This **merchantLocationKey** value will be used in other Inventory Location calls to identify the location to perform an action against.  
  
When creating an inventory location, the [locationTypes](/develop/api/sell/inventory_api#sell-inventory_api-location-createinventorylocation.inventorylocationfull.locationtypes) can be specified to define the function of a location. At this time, the following **locationTypes** are supported:

*   **Fulfillment center** locations are used by sellers selling products through the Multi-warehouse program to get improved estimated delivery dates on their listings. A full address is required when creating a fulfillment center location, as well as the **fulfillmentCenterSpecifications** of the location. For more information on using the fulfillment center location type to get improved delivery dates, see [Multi-warehouse program](/api-docs/sell/static/inventory/multi-warehouse-program.html).
*   **Warehouse** locations are used for traditional shipping. A full street address is not needed, but the **postalCode** and **country** OR **city**, **stateOrProvince**, and **country** of the location must be provided.

  
Note that all inventory locations are "enabled" by default when they are created, and you must specifically disable them (by passing in a value of `DISABLED` in the **merchantLocationStatus** field) if you want them to be set to the disabled state. The seller's inventory cannot be loaded to inventory locations in the disabled state.  
  
Unless one or more errors and/or warnings occur with the call, there is no response payload for this call. A successful call will return an HTTP status value of `204 No Content`.
**Parameters:**
- **merchantLocationKey** (string) *required*
  - This path parameter specifies the unique merchant-defined key (ID) for the inventory location that is to be deleted.  
  
Use the [getInventoryLocations](/develop/api/sell/inventory_api#sell-inventory_api-location-getinventorylocations) method to retrieve merchant location keys.  
  
**Maximum length**: 36
- **Content-Type** (string) *required*
  - This header indicates the format of the request body provided by the client. Its value should be set to **application/json**.

### deleteInventoryLocation

#### DELETE /location/{merchantLocationKey}
**Description:** This call deletes the inventory location that is specified in the **merchantLocationKey** path parameter. Note that deleting a location will not affect any active eBay listings associated with the deleted location, but the seller will not be able modify the offers associated with the location once it is deleted.

**Note:** Deletion is not currently supported for fulfillment center locations, as location mappings will still be retained despite the location being deleted. Instead, fulfillment center locations should be disabled using the [disableInventoryLocation](/develop/api/sell/inventory_api#sell-inventory_api-location-disableinventorylocation) method.  
Unless one or more errors and/or warnings occur with the call, there is no response payload for this call. A successful call will return an HTTP status value of `200 OK`.
**Parameters:**
- **merchantLocationKey** (string) *required*
  - This path parameter specifies the unique merchant-defined key (ID) for the inventory location that is to be deleted.  
  
Use the [getInventoryLocations](/develop/api/sell/inventory_api#sell-inventory_api-location-getinventorylocations) method to retrieve merchant location keys.  
  
**Maximum length**: 36

### disableInventoryLocation

#### POST /location/{merchantLocationKey}/disable
**Description:** This call disables the inventory location that is specified in the **merchantLocationKey** path parameter. Sellers can not load/modify inventory to disabled locations. Note that disabling a location will not affect any active eBay listings associated with the disabled location, but the seller will not be able modify the offers associated with a disabled location.

A successful call will return an HTTP status value of `200 OK`.
**Parameters:**
- **merchantLocationKey** (string) *required*
  - This path parameter specifies the unique merchant-defined key (ID) for an inventory location that is to be disabled.  
  
Use the [getInventoryLocations](/develop/api/sell/inventory_api#sell-inventory_api-location-getinventorylocations) method to retrieve merchant location keys.  
  
**Maximum length**: 36

### enableInventoryLocation

#### POST /location/{merchantLocationKey}/enable
**Description:** This call enables a disabled inventory location that is specified in the **merchantLocationKey** path parameter. Once a disabled location is enabled, sellers can start loading/modifying inventory to that location.  
  
A successful call will return an HTTP status value of `200 OK`.
**Parameters:**
- **merchantLocationKey** (string) *required*
  - This path parameter specifies unique merchant-defined key (ID) for a `disabled` inventory location that is to be enabled.  
  
Use the [getInventoryLocations](/develop/api/sell/inventory_api#sell-inventory_api-location-getinventorylocations) method to retrieve merchant location keys.  
  
**Maximum length**: 36

### getInventoryLocations

#### GET /location
**Description:** This call retrieves all defined details for every inventory location associated with the seller's account. There are no required parameters for this call and no request payload. However, there are two optional query parameters, **limit** and **offset**. The **limit** query parameter sets the maximum number of locations returned on one page of data, and the **offset** query parameter specifies the page of data to return. These query parameters are discussed more in the **URI parameters** table below.

The `authorization` HTTP header is the only required request header for this call.  
  
A successful call will return an HTTP status value of `200 OK`.
**Parameters:**
- **limit** (string)
  - The value passed in this query parameter sets the maximum number of records to return per page of data. Although this field is a string, the value passed in this field should be a positive integer value. If this query parameter is not set, up to 100 records will be returned on each page of results.  
  
**Min**: 1
- **offset** (string)
  - Specifies the number of locations to skip in the result set before returning the first location in the paginated response.

Combine **offset** with the **limit** query parameter to control the items returned in the response. For example, if you supply an **offset** of `0` and a **limit** of `10`, the first page of the response contains the first 10 items from the complete list of items retrieved by the call. If **offset** is `10` and **limit** is `20`, the first page of the response contains items 11-30 from the complete result set.

**Default:** 0

### updateInventoryLocation

#### POST /location/{merchantLocationKey}/update_location_details
**Description:** Use this call to update location details for an existing inventory location. Specify the inventory location you want to update using the **merchantLocationKey** path parameter.

You can update the following text-based fields: **name**, **phone**, **timeZoneId**, **geoCoordinates**, **fulfillmentCenterSpecifications**, **locationTypes**, **locationWebUrl**, **locationInstructions** and **locationAdditionalInformation** any number of times for any location type.

For warehouse inventory locations, address fields can be updated any number of times. Address fields **cannot** be updated for fulfillment center locations. However, if any address fields were omitted during the **createInventoryLocation** call, they can be added through this method.  
**Note:** When updating a warehouse location to a fulfillment center, sellers can update any of the address fields a single time during the same call used to make this update. After this, they can no longer be updated.

Whatever text is passed in for these fields in an **updateInventoryLocation** call will replace the current text strings defined for these fields.

Unless one or more errors and/or warnings occurs with the call, there is no response payload for this call. A successful call will return an HTTP status value of `204 No Content`.
**Parameters:**
- **merchantLocationKey** (string) *required*
  - This path parameter specifies the unique merchant-defined key (ID) for an inventory location that is to be updated.  
  
Use the [getInventoryLocations](/develop/api/sell/inventory_api#sell-inventory_api-location-getinventorylocations) method to retrieve merchant location keys.  
  
**Maximum length**: 36
- **Content-Type** (string) *required*
  - This header indicates the format of the request body provided by the client. Its value should be set to **application/json**.

## Error Codes

The following error codes may be returned by this API:

### REQUEST Errors

#### 25002 - API_INVENTORY
**Description:** Any User error. {additionalInfo}

#### 25003 - API_INVENTORY
**Description:** Invalid price. {additionalInfo}

#### 25004 - API_INVENTORY
**Description:** Invalid quantity. {additionalInfo}

#### 25005 - API_INVENTORY
**Description:** Invalid category. {additionalInfo}

#### 25006 - API_INVENTORY
**Description:** Invalid listing option. {additionalInfo}

#### 25007 - API_INVENTORY
**Description:** Invalid Shipping policy information. {additionalInfo}

#### 25008 - API_INVENTORY
**Description:** Invalid Payment policy information. {additionalInfo}

#### 25009 - API_INVENTORY
**Description:** Invalid Return policy information. {additionalInfo}

#### 25011 - API_INVENTORY
**Description:** Invalid tax information. {additionalInfo}

#### 25012 - API_INVENTORY
**Description:** Invalid location. {additionalInfo}

#### 25013 - API_INVENTORY
**Description:** This error code is associated with multiple possible errors. See [25013 Invalid data in the Inventory Item Group](</api-docs/sell/static/inventory/inventory-error-details.html#25013 >) for the full list of messages returned and any available troubleshooting information.

#### 25014 - API_INVENTORY
**Description:** Invalid pictures. {additionalInfo}

#### 25015 - API_INVENTORY
**Description:** Invalid picture URL. {additionalInfo}

#### 25016 - API_INVENTORY
**Description:** Invalid {fieldName}. {additionalInfo}

#### 25017 - API_INVENTORY
**Description:** This error code is associated with multiple possible errors. See [25017 Missing information in fields](</api-docs/sell/static/inventory/inventory-error-details.html#25017 >) for the full list of messages returned and any available troubleshooting information.

#### 25018 - API_INVENTORY
**Description:** This error code is associated with multiple possible errors. See [25018 Incomplete account information](</api-docs/sell/static/inventory/inventory-error-details.html#25018 >) for the full list of messages returned and any available troubleshooting information.

#### 25019 - API_INVENTORY
**Description:** This error code is associated with multiple possible errors. See [25019 Cannot revise the listing](</api-docs/sell/static/inventory/inventory-error-details.html#25019 >) for the full list of messages returned and any available troubleshooting information.

#### 25020 - API_INVENTORY
**Description:** Invalid package details. {additionalInfo}

#### 25021 - API_INVENTORY
**Description:** Invalid condition information. {additionalInfo}

#### 25022 - API_INVENTORY
**Description:** Invalid attribute. {fieldName}

#### 25023 - API_INVENTORY
**Description:** Invalid compatibility information. {additionalInfo}

#### 25026 - API_INVENTORY
**Description:** Selling limits exceeded. {additionalInfo}

#### 25097 - API_INVENTORY
**Description:** This listing is on hold due to a policy violation, and revisions are not possible. Please check your email for more information.

#### 25098 - API_INVENTORY
**Description:** {replaceable\_value} transaction is not possible as the parent listing is on-hold. Please check your email for further information.

#### 25123 - API_INVENTORY
**Description:** This P&A listing has a non-compliant domestic return policy. Please update the return window to 30-days (or more) and/or update return shipping cost payer to Seller, and then make another call. Sellers using business policies must make the same changes to their return business policy and then make another call. To learn more, visit https://www.ebay.com/sellercenter/news/2025-june/parts-accessories-return-policy.

#### 25129 - API_INVENTORY
**Description:** The product aspects for this category no longer support custom values for {productAspectName}. Your listing was not published. Update your request to use our standard values for {productAspectName}. Use getItemAspectsForCategory for your marketplace and leaf category to get the standard values for {productAspectName}.

#### 25501 - API_INVENTORY
**Description:** Invalid picture. {additionalInfo}

#### 25502 - API_INVENTORY
**Description:** Invalid attribute information. {additionalInfo}

#### 25503 - API_INVENTORY
**Description:** Invalid product information. {additionalInfo}

#### 25601 - API_INVENTORY
**Description:** Invalid attribute. {fieldName}

#### 25604 - API_INVENTORY
**Description:** Input error. {additionalInfo}

#### 25701 - API_INVENTORY
**Description:** These SKU(s) are not in the system

#### 25702 - API_INVENTORY
**Description:** SKU {additionalInfo} is not available in the system

#### 25707 - API_INVENTORY
**Description:** Invalid sku. sku has to be alphanumeric with upto 50 characters in length

#### 25708 - API_INVENTORY
**Description:** Invalid sku

#### 25709 - API_INVENTORY
**Description:** Invalid request. Invalid value for field {additionalInfo}

#### 25710 - API_INVENTORY
**Description:** We didn't find the resource/entity you are requesting. Please verify the request

#### 25713 - API_INVENTORY
**Description:** This Offer is not available : {additionalInfo}.

#### 25715 - API_INVENTORY
**Description:** Invalid Dimension and Weight

#### 25727 - API_INVENTORY
**Description:** The number of InventoryItems in the request cannot exceed {additionalInfo}.

#### 25728 - API_INVENTORY
**Description:** InventoryItems should be unique in the request.

#### 25733 - API_INVENTORY
**Description:** Valid SKU and locale information are required for all the InventoryItems in the request.

#### 25759 - API_INVENTORY
**Description:** shipToLocationAvailability quantity value should be greater than or equal to auction allocation. Please provide valid quantity or unpublish auction offers of the sku.

#### 25734 - API_INVENTORY
**Description:** SKU should be unique in the request.

#### 25029 - API_INVENTORY
**Description:** {field} is required for this category.

#### 25031 - API_INVENTORY
**Description:** {field} is not valid and needs to be a number between {min} and {max}

#### 25034 - API_INVENTORY
**Description:** Only {max value} policies can be specified

#### 25035 - API_INVENTORY
**Description:** The specified policy is not found for the market place

#### 25036 - API_INVENTORY
**Description:** The policy(ies) {PolicyId} is not of type {PolicyEnum}

#### 25038 - API_INVENTORY
**Description:** {ItemId} cannot be revised if the item has a bid or a best offer or is ending within 12 hours

#### 25039 - API_INVENTORY
**Description:** {ItemId} cannot be revised if the item has a bid or a best offer and is ending within 12 hours

#### 25040 - API_INVENTORY
**Description:** {ItemId} cannot be revised if the item has a bid or a best offer and is ending within 12 hours

#### 25041 - API_INVENTORY
**Description:** When listing an item with Refurbished condition, maximum handling time must be {replaceable\_value} business day(s).

#### 25042 - API_INVENTORY
**Description:** When listing an item with Refurbished condition, free shipping must be provided.

#### 25043 - API_INVENTORY
**Description:** When listing an item with Refurbished condition, returns must be accepted.

#### 25044 - API_INVENTORY
**Description:** When listing an item with Refurbished condition, refund must be provided as Money Back.

#### 25045 - API_INVENTORY
**Description:** When listing an item with Refurbished condition, the minimum time you'll accept returns must be {replaceable\_value} days.

#### 25046 - API_INVENTORY
**Description:** When listing an item with Refurbished condition, seller must pay the cost for return shipping.

#### 25047 - API_INVENTORY
**Description:** Seller is not eligible to use Refurbished Item Condition

#### 25048 - API_INVENTORY
**Description:** Seller is not eligible to use Refurbished Item Condition in this Category

#### 25049 - API_INVENTORY
**Description:** Seller is not eligible to use Refurbished Item Condition for the selected Brand

#### 25050 - API_INVENTORY
**Description:** When listing an item with Refurbished condition, {replaceable\_value} cannot be used in the Title.

#### 25051 - API_INVENTORY
**Description:** When listing an item with Refurbished condition, {replaceable\_value} cannot be used in the Subtitle

#### 25052 - API_INVENTORY
**Description:** When listing an item with Refurbished condition, at least {replaceable\_value} images must be provided

#### 25076 - API_INVENTORY
**Description:** {replaceable\_value} ID(s) {replaceable\_value} not found. Please use valid ID(s).

#### 25077 - API_INVENTORY
**Description:** Duplicate Regulatory ID(s) {replaceable\_value} sent in the request. Duplicate ID(s) have been ignored.

#### 25078 - API_INVENTORY
**Description:** Hazmat structure incorrect for {replaceable\_value}.

#### 25079 - API_INVENTORY
**Description:** Repair score invalid. Repair score must be in the range from {replaceable\_value} to {replaceable\_value} with one decimal place.

#### 25080 - API_INVENTORY
**Description:** The value of the {0} field is invalid. Field must not exceed {replaceable\_value} characters.

#### 25081 - API_INVENTORY
**Description:** Hazardous material information incomplete. Your listing must include hazardous statements.

#### 25083 - API_INVENTORY
**Description:** Energy efficiency image is missing. Image is required with image description.

#### 25084 - API_INVENTORY
**Description:** The listing must have both an energy efficiency label and a product information sheet.

#### 25086 - API_INVENTORY
**Description:** The URL provided must be an eBay Picture Service URL.

#### 25088 - API_INVENTORY
**Description:** The email address provided is formatted incorrectly.

#### 25089 - API_INVENTORY
**Description:** No more than {replaceable\_value} global compliance policies allowed. Excess policies ignored.

#### 25090 - API_INVENTORY
**Description:** No more than {replaceable\_value} compliance policies per region allowed. Excess policies ignored.

#### 25091 - API_INVENTORY
**Description:** No more than a total of {replaceable\_value} compliance policies allowed. Excess policies ignored.

#### 25092 - API_INVENTORY
**Description:** No more than {replaceable\_value} global takeback policy allowed.

#### 25093 - API_INVENTORY
**Description:** No more than {replaceable\_value} takeback policy per region allowed. Excess policies ignored.

#### 25094 - API_INVENTORY
**Description:** No more than a total of {replaceable\_value} takeback policies allowed.

#### 25095 - API_INVENTORY
**Description:** Region invalid for regional custom policy. Regions allowed are {replaceable\_value}.

#### 25104 - API_INVENTORY
**Description:** Regulatory document ID(s) {replaceable\_value} not found. Please use valid ID(s).

#### 25106 - API_INVENTORY
**Description:** Regulatory document structure incorrect. Max allowed number of entries is {replaceable\_value}.

#### 25107 - API_INVENTORY
**Description:** Invalid document state for ID(s) {replaceable\_value}. Documents must be in the SUBMITTED or ACCEPTED state.

#### 25108 - API_INVENTORY
**Description:** Product Safety structure incorrect for {replaceable\_value}. Max allowed number of entries is {replaceable\_value}.

#### 25109 - API_INVENTORY
**Description:** Product safety information incomplete. Your listing must include pictograms or safety statements.

#### 25110 - API_INVENTORY
**Description:** Manufacturer address information is incomplete. When providing the address, please provide the street, city, postal code and country

#### 25111 - API_INVENTORY
**Description:** Manufacturer information is incomplete. Please provide the company name.

#### 25112 - API_INVENTORY
**Description:** Responsible Person structure incorrect for {replaceable\_value}. Max allowed number of entries is {replaceable\_value}.

#### 25113 - API_INVENTORY
**Description:** Responsible Person address information is incomplete. When providing the address, please provide the street, city, postal code and country

#### 25114 - API_INVENTORY
**Description:** Responsible Person information is incomplete. Please provide the company name.

#### 25115 - API_INVENTORY
**Description:** Either the Manufacturer or at least one of the Responsible Persons must be located in the EU.

#### 25116 - API_INVENTORY
**Description:** Please provide a minimum of {replaceable\_value} and a maximum of {replaceable\_value} types for a Responsible Person.

#### 25118 - API_INVENTORY
**Description:** Seller must provide at least one form of contact info for Manufacturer - either address, email, contact URL or phone.

#### 25119 - API_INVENTORY
**Description:** Seller must provide at least one form of contact info for Responsible Person - either address, email, contact URL or phone.

#### 25120 - API_INVENTORY
**Description:** When listing in {categoryName}, key information such as {fieldName} comes from eBay's catalog and should be left blank.

#### 25121 - API_INVENTORY
**Description:** When listing in {categoryName}, sellers are required to adopt eBay's catalog data which will provide all the necessary details for the product.

#### 25122 - API_INVENTORY
**Description:** The contact URL is incorrectly formatted. Please update the formatting.

#### 25752 - API_INVENTORY
**Description:** listingStartDate provided is invalid.

#### 25760 - API_INVENTORY
**Description:** shipToLocationAvailability quantity insufficient to create auction listings.

#### 25766 - API_INVENTORY
**Description:** The takeBackPolicyId field must be a long value type. Please correct the error.

#### 25767 - API_INVENTORY
**Description:** The productCompliancePolicyId field must be a long value type. Please correct the error.

#### 25706 - API_INVENTORY
**Description:** You have provided invalid pagination values. {additionalInfo}.

#### 25739 - API_INVENTORY
**Description:** User input error. The number of compatibilityProperties in the request cannot exceed {additionalInfo}.

#### 25740 - API_INVENTORY
**Description:** User input error. Invalid name for compatibilityProperties. The length should be between 1 and {additionalInfo} characters.

#### 25741 - API_INVENTORY
**Description:** User input error. Invalid value for compatibilityProperties. The length should be between 1 and {additionalInfo} characters.

#### 25742 - API_INVENTORY
**Description:** User input error. productFamilyProperties and compatibilityProperties cannot be used together. Please use compatibilityProperties.

#### 25705 - API_INVENTORY
**Description:** The Inventory Item Group named {inventoryItemGroupKey} could not be found or is not available in the system.

#### 25024 - API_INVENTORY
**Description:** Invalid Best Offer information. {additionalInfo}

#### 25703 - API_INVENTORY
**Description:** The following SKU is already a member of another group. SKU : {skuValue} groupId : {inventoryItemGroupKey}

#### 25704 - API_INVENTORY
**Description:** The following SKU is already listed as a single SKU listing. SKU : {skuValue} Listing ID : {listingId}

#### 25756 - API_INVENTORY
**Description:** Auction format is not permitted with a SKU that is part of an InventoryItemGroup.

#### 25718 - API_INVENTORY
**Description:** Cannot migrate listing. {additionalInfo}

#### 25904 - API_INVENTORY
**Description:** Invalid listing ID or the listing does not belong to the seller.

#### 25905 - API_INVENTORY
**Description:** Invalid SKU value or the SKU value is not defined in the listing.

#### 25900 - API_INVENTORY
**Description:** One or more inventory locations could not be found for the seller.

#### 25901 - API_INVENTORY
**Description:** Missing a location. Please specify one or more inventory locations.

#### 25902 - API_INVENTORY
**Description:** One or more duplicate inventory locations were specified. Unique inventory locations must be used.

#### 25906 - API_INVENTORY
**Description:** The provided inventory location must be a Fulfillment Center. Please use a Fulfillment Center location or use updateInventoryLocation to change location type to FULFILLMENT\_CENTER.

#### 25729 - API_INVENTORY
**Description:** The combination of SKU, marketplaceId and format should be unique.

#### 25730 - API_INVENTORY
**Description:** The number of offers in the request cannot exceed {additionalInfo}

#### 25735 - API_INVENTORY
**Description:** Invalid SKU, marketplaceId or format.

#### 25755 - API_INVENTORY
**Description:** listingDuration is required for auction offer.

#### 25757 - API_INVENTORY
**Description:** auctionStartPrice is required for auction offer.

#### 25758 - API_INVENTORY
**Description:** auctionStartPrice and auctionReservePrice are not supported for fixed price offer.

#### 25761 - API_INVENTORY
**Description:** Discount pricing is not applicable for auction offer.

#### 25762 - API_INVENTORY
**Description:** availableQuantity is not applicable for auction offer.

#### 25763 - API_INVENTORY
**Description:** quantityLimitPerBuyer is not applicable for auction offer.

#### 25764 - API_INVENTORY
**Description:** eBayPlusIfEligible is not applicable for auction offer.

#### 25032 - API_INVENTORY
**Description:** {field} is not valid

#### 25731 - API_INVENTORY
**Description:** OfferId should be unique in the request.

#### 25732 - API_INVENTORY
**Description:** Offers associated with SKUs that are part of a variation group cannot be published using this endpoint.

#### 25754 - API_INVENTORY
**Description:** One or more provided offerId(s) are invalid. All offerId(s) in the request should belong to an inventoryItem or inventoryItemGroup for a specific marketplaceId and format.

#### 25725 - API_INVENTORY
**Description:** No offer found

#### 25804 - API_INVENTORY
**Description:** Input error. {additionalInfo}

#### 25805 - API_INVENTORY
**Description:** {fieldName} Not Found.

#### 25800 - API_INVENTORY
**Description:** Invalid {fieldName}.

#### 25801 - API_INVENTORY
**Description:** Missing field {fieldName}.

#### 25802 - API_INVENTORY
**Description:** Input error. {additionalInfo}

#### 25803 - API_INVENTORY
**Description:** {fieldName} already exists.

#### 25806 - API_INVENTORY
**Description:** Deletion is not allowed when the location type of an inventory location has been set to fulfillment center. However, you may disable it.

### APPLICATION Errors

#### 25001 - API_INVENTORY
**Description:** Any System error. {additionalInfo}

#### 25025 - API_INVENTORY
**Description:** Concurrent access of Inventory or InventoryItemGroup. Please try again later

## Types

### Availability
**Description:** This type is used to specify the quantity of the inventory item that is available for purchase if the item will be shipped to the buyer.
**Type:** object

**Properties:**
- **pickupAtLocationAvailability** (array)
  - **Deprecated.** Do not use as STORE location types are no longer supported.
- **shipToLocationAvailability** (ShipToLocationAvailability)
  - This container specifies the quantity of the inventory item that are available for purchase across one or more eBay marketplaces.

### AvailabilityDistribution
**Description:** This type is used to set the available quantity of the inventory item at one or more warehouse locations.
**Type:** object

**Properties:**
- **fulfillmentTime** (TimeDuration)
  - This container is used to indicate the expected fulfillment time if the inventory item is shipped from the warehouse location identified in the corresponding **merchantLocationKey** field. The fulfillment time is the estimated number of business days after purchase that the buyer can expect the item to be delivered.  
  
This field is optional, and is used by eBay to provide the estimated delivery date to buyers. This field is returned by [getInventoryItem](/develop/api/sell/inventory_api#sell-inventory_api-inventory_item-getinventoryitem) and [getInventoryItems](/develop/api/sell/inventory_api#sell-inventory_api-inventory_item-getinventoryitems) if set for the inventory item.
- **merchantLocationKey** (string)
  - The unique identifier of an inventory location where quantity is available for the inventory item. This field is conditionally required to identify the inventory location that has quantity of the inventory item.  
  
Use the [getInventoryLocations](/develop/api/sell/inventory_api#sell-inventory_api-location-getinventorylocations) method to retrieve merchant location keys.
- **quantity** (integer)
  - The integer value passed into this field indicates the quantity of the inventory item that is available at this inventory location. This field is conditionally required.

### AvailabilityTypeEnum
**Description:** **Deprecated.** Do not use as STORE location types are no longer supported. | - **IN_STOCK**: IN_STOCK - **OUT_OF_STOCK**: OUT_OF_STOCK - **SHIP_TO_STORE**: SHIP_TO_STORE
**Type:** object

### BulkInventoryItem
**Description:** The base request of the **bulkCreateOrReplaceInventoryItem** method.
**Type:** object

**Properties:**
- **requests** (array)
  - The details of each inventory item that is being created or updated is passed in under this container. Up to 25 inventory item records can be created and/or updated with one **bulkCreateOrReplaceInventoryItem** call.

### BulkInventoryItemResponse
**Description:** This type is used by the base response of the **bulkCreateOrReplaceInventoryItem** method.
**Type:** object

**Properties:**
- **responses** (array)
  - This is the base container of the **bulkCreateOrReplaceInventoryItem** response. The results of each attempted inventory item creation/update is captured under this container.

### ConditionDescriptor
**Description:** This type is used by the seller to provide additional information about the condition of an item in a structured format.
**Type:** object

**Properties:**
- **additionalInfo** (string)
  - This string provides additional information about a condition descriptor. Open text is passed in this field.  
  
In the case of trading cards and coins, this field houses the optional **Certification Number** condition descriptor for graded items. For salvage, this field houses the optional **Damage Code** condition descriptor for graded items.  
  

**Important!** Condition grading for salvage items is only available for eligible sellers.

  
**Max Length:** 30 characters
- **name** (string)
  - This string provides the name of a condition descriptor. A numeric ID is passed in this field. This numeric ID maps to the name of a condition descriptor. Condition descriptor name-value pairs provide more information about an item's condition in a structured way.  
  
To retrieve all condition descriptor name numeric IDs for a category, refer to the **conditionDescriptorId** field returned in the [getItemConditionPolicies](/develop/api/sell/metadata_api#sell-metadata_api-marketplace-getitemconditionpolicies) method of Metadata API.  
  
In the case of trading cards, this field is used to provide condition descriptors for a card. For graded cards, the condition descriptors for **Grader** and **Grade** are required, while the condition descriptor for **Certification Number** is optional. For ungraded cards, only the **Card Condition** condition descriptor is required.  
  
In the case of coins, this field is used to provide condition descriptors for a coin. For graded coins, the condition descriptors for **Grader**, **Number Grade**, and **Letter Grade** are required, while the condition descriptor for **Certification Number** is optional. For ungraded coins, only the **Coin Condition** condition descriptor is required.  
  
In the case of salvage, this field is used to provide condition descriptors for the item. If the salvage is graded, the condition descriptor for **Grade** is required, while the condition descriptor for **Damage Code** is optional.  
  

**Important!** Condition grading for salvage items is only available for eligible sellers.
- **values** (array)
  - This array provides the value(s) associated with a condition descriptor. One or more numeric IDs is passed in this field. Commas are used as delimiters between successive name/value pairs. These numeric IDs map to the values associated with a condition descriptor name. Condition descriptor name-value pairs provide more information about an item's condition in a structured way.  
  
To retrieve all condition descriptor value numeric IDs for a category, refer to the **ConditionDescriptorValueId** array returned in the [getItemConditionPolicies](</develop/api/sell/metadata_api#sell-metadata_api-marketplace-getitemconditionpolicies >) method of Metadata API.  
  
In the case of trading cards, this field houses the information on the **Grader** and **Grade** descriptors of graded cards and the **Card Condition** descriptor for ungraded cards.  
  
In the case of coins, this field houses the information on the **Grader** and **Number Grade**, and **Letter Grade** descriptors of graded coins and the **Coin Condition** descriptor for ungraded coins.  
  
In the case of salvage, this field houses the information on the **Grade** descriptor of a graded item.  
  

**Important!** Condition grading for salvage items is only available for eligible sellers.

### ConditionEnum
**Description:** This enumeration type is used to indicate the condition of the item. Item conditions can vary with each eBay Category. For more information on item conditions, including condition ID and name values, see [Item condition ID and name values](/api-docs/sell/static/metadata/condition-id-values.html). | - **NEW**: This enumeration value indicates that the inventory item is a brand-new, unopened item in its original packaging.  
  
This enumeration value should be used if the Condition ID value is `1000`. - **LIKE_NEW**: This enumeration value indicates that the inventory item is in 'like-new' condition. In other words, the item has been opened, but very lightly used if used at all. This condition typically applies to books or DVDs.  
  
This enumeration value should be used if the Condition ID value is `2750`.  
  
**Note:** This condition enumeration value should be used for trading card and coin categories to indicate that the item is **Graded**. - **NEW_OTHER**: This enumeration value indicates that the inventory item is a new, unused item, but it may be missing the original packaging or perhaps not sealed. When a seller specifies this condition for an item, that seller should also provide a more detailed explanation of the item's condition in the **conditionDescription** field.  
  
This enumeration value should be used if the Condition ID value is `` 1500`.` `` - **NEW_WITH_DEFECTS**: This enumeration value indicates that the inventory item is a new, unused item, but it has defects. This item condition is typically applicable to clothing or shoes that may have scuffs, hanging threads, missing buttons, etc. When a seller specifies this condition for an item, that seller should also provide a more detailed explanation of the item's condition in the **conditionDescription** field.  
  
This enumeration value should be used if the Condition ID value is `1750`. - **MANUFACTURER_REFURBISHED**: **Important!** This enumeration value should no longer be used, as the 'Manufacturer Refurbished' item condition is no longer a valid item condition on any eBay marketplace.

  
In all eBay marketplaces, Condition ID `2000` now maps to item condition 'Certified Refurbished', and not 'Manufacturer Refurbished'. If the `MANUFACTURER_REFURBISHED` enum is used, it will be accepted but automatically converted by eBay to `CERTIFIED_REFURBISHED`. In the future, the `MANUFACTURER_REFURBISHED` may trigger an error if used. - **CERTIFIED_REFURBISHED**: This enumeration value indicates that the inventory item is in pristine, like-new condition and has been inspected, cleaned, and refurbished by the manufacturer or a manufacturer-approved vendor. The item will be in new packaging with original or new accessories.  
  
This enumeration value should be used if the Condition ID value is `2000`.  
  
**Note:** This `CERTIFIED_REFURBISHED` value has replaced the deprecated `MANUFACTURER_REFURBISHED` value. eBay will automatically convert the condition value of existing inventory items from `MANUFACTURER_REFURBISHED` to `CERTIFIED_REFURBISHED`.  
  
Sellers must go through an application and qualification process to become eligible to list with 'Certified - Refurbished' item condition. Sellers interested in the eligibility requirements to list with 'Certified Refurbished' should see the [Certified refurbished program](https://pages.ebay.com/seller-center/listing-and-marketing/certified-refurbished-program.html) page in Seller Center. - **EXCELLENT_REFURBISHED**: This enumeration value indicates that the inventory item is in like new condition and has been inspected, cleaned, and refurbished by the manufacturer or a manufacturer-approved vendor. When a seller specifies this condition for an item, that seller should also provide a more detailed explanation of the item's condition in the **conditionDescription** field.  
  
This enumeration value should be used if the Condition ID value is `2010`.  
  
**Note:** This item condition is limited to a select number of eBay marketplaces and categories. See [Category and marketplace support for the eBay Refurbished Program](/api-docs/sell/static/metadata/condition-id-values.html#Category) for more information.  
  
Sellers must go through an application and qualification process to become eligible to list with the 'Excellent - Refurbished' item condition. Sellers interested in the eligibility requirements to list with 'Excellent Refurbished' should see the [Certified refurbished program](https://pages.ebay.com/seller-center/listing-and-marketing/certified-refurbished-program.html) page in Seller Center. - **VERY_GOOD_REFURBISHED**: This enumeration value indicates that the inventory item shows minimal wear and has been inspected, cleaned, and refurbished by the manufacturer or a manufacturer-approved vendor. When a seller specifies this condition for an item, that seller should also provide a more detailed explanation of the item's condition in the **conditionDescription** field.  
  
This enumeration value should be used if the Condition ID value is `2020`.  
  
**Note:** This item condition is limited to a select number of eBay marketplaces and categories. See [Category and marketplace support for the eBay Refurbished Program](/api-docs/sell/static/metadata/condition-id-values.html#Category) for more information.  
  
Sellers must go through an application and qualification process to become eligible to list with the 'Very Good - Refurbished' item condition. Sellers interested in the eligibility requirements to list with 'Very Good Refurbished' should see the [Certified refurbished program](https://pages.ebay.com/seller-center/listing-and-marketing/certified-refurbished-program.html) page in Seller Center. - **GOOD_REFURBISHED**: This enumeration value indicates that the inventory item shows moderate wear and has been inspected, cleaned, and refurbished by the manufacturer or a manufacturer-approved vendor. When a seller specifies this condition for an item, that seller should also provide a more detailed explanation of the item's condition in the **conditionDescription** field.  
  
This enumeration value should be used if the Condition ID value is `2030`.  
  
**Note:** This item condition is limited to a select number of eBay marketplaces and categories. See [Category and marketplace support for the eBay Refurbished Program](/api-docs/sell/static/metadata/condition-id-values.html#Category) for more information.  
  
Sellers must go through an application and qualification process to become eligible to list with the 'Good - Refurbished' item condition. Sellers interested in the eligibility requirements to list with 'Good Refurbished' should see the [Certified refurbished program](https://pages.ebay.com/seller-center/listing-and-marketing/certified-refurbished-program.html) page in Seller Center. - **SELLER_REFURBISHED**: This enumeration value indicates that the inventory item has been restored to working order by the eBay seller or a third party. This means the item was inspected, cleaned, and repaired to full working order and is in excellent condition. This item may or may not be in original packaging. When a seller specifies this condition for an item, that seller should also provide a more detailed explanation of the item's condition in the **conditionDescription** field.  
  
This enumeration value should be used if the Condition ID value is `2500`.  
  
**Note:** This item condition has been replaced by the 'Excellent - Refurbished', 'Very Good - Refurbished', and 'Good - Refurbished' item conditions in a select number of eBay marketplaces and categories. See [Category and marketplace support for the eBay Refurbished Program](/api-docs/sell/static/metadata/condition-id-values.html#Category) for more information. - **USED_EXCELLENT**: This enumeration value indicates that the inventory item is used but in excellent condition. When a seller specifies this condition for an item, that seller should also provide a more detailed explanation of the item's condition in the **conditionDescription** field.  
  
This enumeration value should be used if the Condition ID value is `3000`.  
  
**Note:** This condition enumeration value should be used for apparel categories to indicate that the condition is **Pre-owned - Good**. This condition means that the item has been gently used, but is in good condition and has light signs of wear. - **USED_VERY_GOOD**: This enumeration value indicates that the inventory item is used but in very good condition. When a seller specifies this condition for an item, that seller should also provide a more detailed explanation of the item's condition in the **conditionDescription** field.  
  
This enumeration value should be used if the Condition ID value is `4000`.  
  
**Note:** This condition enumeration value should be used for trading card and coin categories to indicate that the item is **Ungraded**. - **USED_GOOD**: This enumeration value indicates that the inventory item is used but in good condition. When a seller specifies this condition for an item, that seller should also provide a more detailed explanation of the item's condition in the **conditionDescription** field.  
  
This enumeration value should be used if the Condition ID value is `5000`. - **USED_ACCEPTABLE**: This enumeration value indicates that the inventory item is in acceptable condition. When a seller specifies this condition for an item, that seller should also provide a more detailed explanation of the item's condition in the **conditionDescription** field.  
  
This enumeration value should be used if the Condition ID value is `6000`. - **FOR_PARTS_OR_NOT_WORKING**: This enumeration value indicates that the inventory item is not fully functioning as originally designed. A buyer will generally buy an item in this condition knowing that the item will need to be repaired, or a buyer will buy that item just to use one or more of the parts/components that comprise the item. When a seller specifies this condition for an item, that seller should also provide a more detailed explanation of the item's condition in the **conditionDescription** field.  
  
This enumeration value should be used if the Condition ID value is `7000`. - **PRE_OWNED_EXCELLENT**: This enumeration value indicates that the inventory item has been previously owned, but is in excellent condition. The item may have been previously worn, but is like new with little to no signs of wear. When a seller specifies this condition for an item, that seller should also provide a more detailed explanation of the item's condition in the **conditionDescription** field.  
  
This enumeration value should be used if the Condition ID value is `2990`.  
  
**Note:** This condition enumeration value is only applicable for apparel categories. - **PRE_OWNED_FAIR**: This enumeration value indicates that the inventory item has been previously owned and is in fair condition. The item has significant visible flaws, heavy signs of wear, and/or missing or damaged components. When a seller specifies this condition for an item, that seller should also provide a more detailed explanation of the item's condition in the **conditionDescription** field.  
  
This enumeration value should be used if the Condition ID value is 3010.  
  
**Note:** This condition enumeration value is only applicable for apparel categories.
**Type:** object

### Dimension
**Description:** This type is used to specify the dimensions (and the unit used to measure those dimensions) of a shipping package. The **dimensions** container is conditionally required if the seller will be offering calculated shipping rates to determine shipping cost. See the [Calculated shipping](<https://pages.ebay.com/help/pay/calculated-shipping.html >) help page for more information on calculated shipping.
**Type:** object

**Properties:**
- **height** (number)
  - The actual height (in the measurement unit specified in the **unit** field) of the shipping package. All fields of the **dimensions** container are required if package dimensions are specified.  
  
If a shipping package measured 21.5 inches in length, 15.0 inches in width, and 12.0 inches in height, the **dimensions** container would look as follows:  

"dimensions": {  
 "length": 21.5,  
 "width": 15.0,  
 "height": 12.0,  
 "unit": "INCH"  
 }
- **length** (number)
  - The actual length (in the measurement unit specified in the **unit** field) of the shipping package. All fields of the **dimensions** container are required if package dimensions are specified.  
  
If a shipping package measured 21.5 inches in length, 15.0 inches in width, and 12.0 inches in height, the **dimensions** container would look as follows:  

"dimensions": {  
 "length": 21.5,  
 "width": 15.0,  
 "height": 12.0,  
 "unit": "INCH"  
 }
- **unit** (LengthUnitOfMeasureEnum)
  - The unit of measurement used to specify the dimensions of a shipping package. All fields of the **dimensions** container are required if package dimensions are specified. If the English system of measurement is being used, the applicable values for dimension units are `FEET` and `INCH`. If the metric system of measurement is being used, the applicable values for weight units are `METER` and `CENTIMETER`. The metric system is used by most countries outside of the US.
- **width** (number)
  - The actual width (in the measurement unit specified in the **unit** field) of the shipping package. All fields of the **dimensions** container are required if package dimensions are specified.  
  
If a shipping package measured 21.5 inches in length, 15.0 inches in width, and 12.0 inches in height, the **dimensions** container would look as follows:  

"dimensions": {  
 "length": 21.5,  
 "width": 15.0,  
 "height": 12.0,  
 "unit": "INCH"  
 }

### ErrorDetailV3
**Description:** This type is used to express detailed information on errors and warnings that may occur with a call request.
**Type:** object

**Properties:**
- **category** (string)
  - This string value indicates the error category. There are three categories of errors: request errors, application errors, and system errors.
- **domain** (string)
  - The name of the domain in which the error or warning occurred.
- **errorId** (integer)
  - A unique code that identifies the particular error or warning that occurred. Your application can use error codes as identifiers in your customized error-handling algorithms.
- **inputRefIds** (array)
  - An array of one or more reference IDs which identify the specific request element(s) most closely associated to the error or warning, if any.
- **longMessage** (string)
  - A detailed description of the condition that caused the error or warning, and information on what to do to correct the problem.
- **message** (string)
  - A description of the condition that caused the error or warning.
- **outputRefIds** (array)
  - An array of one or more reference IDs which identify the specific response element(s) most closely associated to the error or warning, if any.
- **parameters** (array)
  - Various warning and error messages return one or more variables that contain contextual information about the error or warning. This is often the field or value that triggered the error or warning.
- **subdomain** (string)
  - The name of the subdomain in which the error or warning occurred.

### ErrorParameterV3
**Description:** This type is used to indicate the parameter field/value that caused an issue with the call request.
**Type:** object

**Properties:**
- **name** (string)
  - This type contains the name and value of an input parameter that contributed to a specific error or warning condition.
- **value** (string)
  - This is the actual value that was passed in for the element specified in the **name** field.

### InventoryItemResponse
**Description:** This type is used by the response of the **bulkCreateOrReplaceInventoryItem** method to indicate the success or failure of creating and/or updating each inventory item record. The **sku** value in this type identifies each inventory item record.
**Type:** object

**Properties:**
- **errors** (array)
  - This container will be returned if there were one or more errors associated with the creation or update to the inventory item record.
- **locale** (LocaleEnum)
  - This field returns the natural language that was provided in the field values of the request payload (i.e., en\_AU, en\_GB or de\_DE).
- **sku** (string)
  - The seller-defined Stock-Keeping Unit (SKU) of the inventory item. The seller should have a unique SKU value for every product that they sell.
- **statusCode** (integer)
  - The HTTP status code returned in this field indicates the success or failure of creating or updating the inventory item record for the inventory item indicated in the **sku** field. See the **HTTP status codes** table to see which each status code indicates.
- **warnings** (array)
  - This container will be returned if there were one or more warnings associated with the creation or update to the inventory item record.

### InventoryItemWithSkuLocale
**Description:** This type is used to define/modify each inventory item record that is being created and/or updated with the **bulkCreateOrReplaceInventoryItem** method. Up to 25 inventory item records can be created and/or updated with one call.
**Type:** object

**Properties:**
- **availability** (Availability)
  - This container is used to specify the quantity of the inventory item that are available for purchase.  
  
Availability data must also be passed if an inventory item is being updated and availability data already exists for that inventory item.  
  
Since an inventory item must have specified quantity before being published in an offer, this container is always returned in the 'Get' calls for SKUs that are part of a published offer. If a SKU is not part of a published offer, this container will only be returned if set for the inventory item.
- **condition** (ConditionEnum)
  - This enumeration value indicates the condition of the item. Supported item condition values will vary by eBay site and category. To see which item condition values that a particular eBay category supports, use the [getItemConditionPolicies](/develop/api/sell/metadata_api#sell-metadata_api-marketplace-getitemconditionpolicies) method of the **Metadata API**. This method returns condition ID values that map to the enumeration values defined in the [ConditionEnum](/develop/api/sell/inventory_api#sell-inventory_api-inventory_item-getinventoryitem.conditionenum) type. The [Item condition ID and name values](/api-docs/sell/static/metadata/condition-id-values.html) topic in the **Selling Integration Guide** has a table that maps condition ID values to **ConditionEnum** values. The **getItemConditionPolicies** call reference page has more information.  
  
A **condition** value is optional up until the seller is ready to publish an offer with the SKU, at which time it becomes required for most eBay categories.  
  

**Important!**Publish offer note: This field is required before an offer can be published to create an active listing.
- **conditionDescription** (string)
  - This string field is used by the seller to more clearly describe the condition of a used inventory item, or an inventory item whose **condition** value is not `NEW`, `LIKE_NEW`, `NEW_OTHER`, or `NEW_WITH_DEFECTS`.  
  
The **conditionDescription** field is available for all eBay categories. If the **conditionDescription** field is used with an item in one of the new conditions (mentioned in previous paragraph), eBay will simply ignore this field if included, and eBay will return a warning message to the user.  
  
This field should only be used to further clarify the condition of the used item. It should not be used for branding, promotions, shipping, returns, payment or other information unrelated to the condition of the used item. Make sure that the **condition** value, condition description, listing description, and the item's pictures do not contradict one another.  
  
This field is not always required, but is required if an inventory item is being updated and a condition description already exists for that inventory item.  
  
This field is returned in the **getInventoryItem**, **bulkGetInventoryItem**, and **getInventoryItems** calls if a condition description was provided for a used inventory item.  
  
**Maximum length**: 1000
- **conditionDescriptors** (array)
  - This container is used by the seller to provide additional information about the condition of an item in a structured format. Condition descriptors are name-value attributes that can be either closed set or open text inputs.  
  
For trading card coin listings in applicable categories, sellers must use either `LIKE_NEW` (2750) or `USED_VERY_GOOD` (4000) item condition to specify the item as **Graded** or **Ungraded**, respectively. Use of either of these conditions requires the seller to use this array to provide one or more applicable Condition Descriptor name-value pairs.  
  
To retrieve all condition descriptor numeric IDs for a category, use the [getItemConditionPolicies](/develop/api/sell/metadata_api#sell-metadata_api-marketplace-getitemconditionpolicies) method of the Metadata API.
- **locale** (LocaleEnum)
  - This request parameter sets the natural language that was provided in the field values of the request payload (i.e., en\_AU, en\_GB or de\_DE).
- **packageWeightAndSize** (PackageWeightAndSize)
  - This container is used if the seller is offering one or more calculated shipping options for the inventory item, or if the seller is offering flat-rate shipping but is including a shipping surcharge based on the item's weight. This container is used to specify the dimensions and weight of a shipping package.  
  
**Note:** Package weight and dimensions are only supported for the following marketplaces: AU, CA, DE, IT, UK, US, and Motors. If this information is provided on other marketplaces, it will be ignored.  
This container is not always required, but is required if an inventory item is being updated and shipping package data already exists for that inventory item.  
  
This container is returned in the **getInventoryItem**, **bulkGetInventoryItem**, and **getInventoryItems** calls if package type, package weight, and/or package dimensions are specified for an inventory item.  
  
See the [Calculated shipping](<https://pages.ebay.com/help/pay/calculated-shipping.html >) help page for more information on calculated shipping.
- **product** (Product)
  - This container is used to define the product details, such as product title, product description, product identifiers (eBay Product ID, GTIN, or Brand/MPN pair), product aspects/item specifics, and product images. Note that an eBay Product ID (ePID) or a Global Trade Item Number (GTIN) value can be used in an attempt to find a matching product in the eBay Catalog. If a product match is found, the inventory item record will automatically pick up all product details associated with the eBay Catalog product.  
  
Many eBay categories will require at least one product identifier (a GTIN or a Brand/MPN pair). To discover which product identifier(s) that an eBay category might require or support, use the [getItemAspectsForCategory](/develop/api/sell/taxonomy_api#sell-taxonomy_api-category_tree-getitemaspectsforcategory) method in the Taxonomy API. In the **getItemAspectsForCategory** response, look for product identifier names (`brand`, `mpn`, `upc`, `ean`, `isbn`) in the **localizedAspectName** fields, and then look for the correspondinng **aspectRequired** boolean fields as well as the corresponding **aspectUsage** field, which will indicate if the aspect is required, recommended, or optional. In some cases, a product identifier type may be required, but not known/applicable for a product. If this is the case, the seller must still include the corresponding field in the inventory item record, but pass in a default text string. This text string can vary by site, so the seller should use the **GeteBayDetails** call of the Trading API to get this string value. In the **GeteBayDetails** call, the seller should include a **DetailName** field with its value set to `ProductDetails`. In the response of the call, the seller can see the default string value in the **ProductDetails.ProductIdentifierUnavailableText** field. The seller will use this value in one or more of the product identifier fields (**ean**, **isbn**, **upc**, or **mpn**) if a product ID isn't known or applicable.  
  
This container is not initially required, but it is required before an inventory item can be published as an offer, and/or if an inventory item is being updated and product data already exists for that inventory item.  
  
This container is always returned for published offers in the **getInventoryItem**, **bulkGetInventoryItem**, and **getInventoryItems** calls since product data must be defined for published offers, but for unpublished inventory items, this container will only be returned if product details have been defined for the inventory item.  
  

**Important!**Publish offer note: This container and a few of its child fields (as noted below) are required before an offer can be published to create an active listing.
- **sku** (string)
  - This is the seller-defined SKU value of the product that will be listed on the eBay site (specified in the **marketplaceId** field). Only one offer (in unpublished or published state) may exist for each **sku**/**marketplaceId**/**format** combination. This field is required.  
  
**Maximum length**: 50

### LengthUnitOfMeasureEnum
**Description:** This enumeration type is used to specify/indicate the unit of measurement with which the dimensions of the shipping package are being measured. | - **INCH**: This enumeration value indicates that the dimensions of the shipping package is being measured in inches. - **FEET**: This enumeration value indicates that the dimensions of the shipping package is being measured in feet. - **CENTIMETER**: This enumeration value indicates that the dimensions of the shipping package is being measured in centimeters. - **METER**: This enumeration value indicates that the dimensions of the shipping package is being measured in meters.
**Type:** object

### LocaleEnum
**Description:** This enumeration type contains the different locales that can be used. The **locale** value indicates the language that is used to express the inventory item details. | - **en_US**: This value indicates the content is localized for US English. - **en_CA**: This value indicates the content is localized for Canadian English. - **fr_CA**: This value indicates the content is localized for Canadian French. - **en_GB**: This value indicates the content is localized for UK English. - **en_AU**: This value indicates the content is localized for Australian English. - **en_IN**: This value indicates the content is localized for English but on the India site.  
  
**Note**: eBay India is no longer a functioning eBay marketplace. - **de_AT**: This value indicates the content is localized for German speakers on the Austria site. - **fr_BE**: This value indicates the content is localized for French speakers on the Belgium site. - **fr_FR**: This value indicates the content is localized for French speakers on the France site. - **de_DE**: This value indicates the content is localized for German speakers on the Germany site. - **it_IT**: This value indicates the content is localized for Italian speakers on the Italy site. - **nl_BE**: This value indicates the content is localized for Dutch speakers on the Belgium site. - **nl_NL**: This value indicates the content is localized for Dutch speakers on the Netherlands site. - **es_ES**: This value indicates the content is localized for Spanish speakers on the Spain site. - **de_CH**: This value indicates the content is localized for Germany speakers on the Switzerland site. - **fi_FI**: This value indicates the content is localized for Finnish speakers. - **zh_HK**: This value indicates the content is localized for Chinese speakers on the Hong Kong site. - **hu_HU**: This value indicates the content is localized for Hungarian speakers. - **en_PH**: This value indicates the content is localized for English speakers on the Philippines site. - **pl_PL**: This value indicates the content is localized for Polish speakers on the Poland site. - **pt_PT**: This value indicates the content is localized for Portuguese speakers. - **ru_RU**: This value indicates the content is localized for Russian speakers. - **en_SG**: This value indicates the content is localized for English on the Singapore site. - **en_IE**: This value indicates the content is localized for English on the Ireland site. - **en_MY**: This value indicates the content is localized for English on the Malaysia site.
**Type:** object

### PackageTypeEnum
**Description:** This enumerated type is used to indicate what type of shipping package will be used to ship an inventory item.  
  
**Note:** You can use the [GeteBayDetails](/Devzone/XML/docs/Reference/eBay/GeteBayDetails.html#Response.ShippingPackageDetails) Trading API call to retrieve a list of supported package types for a specific marketplace. | - **LETTER**: This enumeration value indicates that the package type used to ship the inventory item is a letter. - **BULKY_GOODS**: This enumeration value indicates that the inventory item is considered a "bulky good". - **CARAVAN**: This enumeration value indicates that the package type used to ship the inventory item is a caravan. - **CARS**: This enumeration value indicates that the inventory item is a car. - **EUROPALLET**: This enumeration value indicates that the package type used to ship the inventory item is a Euro pallet. - **EXPANDABLE_TOUGH_BAGS**: This enumeration value indicates that the package type used to ship the inventory item is an expandable tough bag. - **EXTRA_LARGE_PACK**: This enumeration value indicates that the package type used to ship the inventory item is an extra large pack. - **FURNITURE**: This enumeration value indicates that the inventory item is a furniture item. - **INDUSTRY_VEHICLES**: This enumeration value indicates that the inventory item is an industry vehicle. - **LARGE_CANADA_POSTBOX**: This enumeration value indicates that the package type used to ship the inventory item is a Canada Post large box. - **LARGE_CANADA_POST_BUBBLE_MAILER**: This enumeration value indicates that the package type used to ship the inventory item is a Canada Post large bubble mailer. - **LARGE_ENVELOPE**: This enumeration value indicates that the package type used to ship the inventory item is a large envelope. - **MAILING_BOX**: This enumeration value indicates that the package type used to ship the inventory item is a standard mailing box. - **MEDIUM_CANADA_POST_BOX**: This enumeration value indicates that the package type used to ship the inventory item is a medium Canada Post box. - **MEDIUM_CANADA_POST_BUBBLE_MAILER**: This enumeration value indicates that the package type used to ship the inventory item is a medium Canada Post bubble mailer. - **MOTORBIKES**: This enumeration value indicates that the inventory item is a motorcycle. - **ONE_WAY_PALLET**: This enumeration value indicates that the package type used to ship the inventory item is a one-way pallet. - **PACKAGE_THICK_ENVELOPE**: This enumeration value indicates that the package type used to ship the inventory item is an thick envelope. - **PADDED_BAGS**: This enumeration value indicates that the package type used to ship the inventory item is a padded bag. - **PARCEL_OR_PADDED_ENVELOPE**: This enumeration value indicates that the package type used to ship the inventory item is a parcel or a padded envelope. - **ROLL**: This enumeration value indicates that the package type used to ship the inventory item is a roll. - **SMALL_CANADA_POST_BOX**: This enumeration value indicates that the package type used to ship the inventory item is a small Canada Post box. - **SMALL_CANADA_POST_BUBBLE_MAILER**: This enumeration value indicates that the package type used to ship the inventory item is a small Canada Post bubble mailer. - **TOUGH_BAGS**: This enumeration value indicates that the package type used to ship the inventory item is a a tough bag. - **UPS_LETTER**: This enumeration value indicates that the package type used to ship the inventory item is a UPS letter. - **USPS_FLAT_RATE_ENVELOPE**: This enumeration value indicates that the package type used to ship the inventory item is a USPS flat-rate envelope. - **USPS_LARGE_PACK**: This enumeration value indicates that the package type used to ship the inventory item is a USPS large pack. - **VERY_LARGE_PACK**: This enumeration value indicates that the package type used to ship the inventory item is a USPS very large pack. - **WINE_PAK**: This enumeration value indicates that the package type used to ship the inventory item is a wine pak.
**Type:** object

### PackageWeightAndSize
**Description:** This type is used to indicate the package type, weight, and dimensions of the shipping package. Package weight and dimensions are required when calculated shipping rates are used, and weight alone is required when flat-rate shipping is used, but with a weight surcharge. See the [Calculated shipping](<https://pages.ebay.com/help/pay/calculated-shipping.html >) help page for more information on calculated shipping.
**Type:** object

**Properties:**
- **dimensions** (Dimension)
  - This container is used to indicate the length, width, and height of the shipping package that will be used to ship the inventory item. The dimensions of a shipping package are needed when calculated shipping is used.  
  
This container will be returned if package dimensions are set for the inventory item.
- **packageType** (PackageTypeEnum)
  - This enumeration value indicates the type of shipping package used to ship the inventory item. The supported values for this field can be found in the [PackageTypeEnum](/develop/api/sell/inventory_api#sell-inventory_api-inventory_item-bulkcreateorreplaceinventoryitem.packagetypeenum) type.  
  
This field will be returned if the package type is set for the inventory item.  
  
**Note:** You can use the [GeteBayDetails](/Devzone/XML/docs/Reference/eBay/GeteBayDetails.html#Response.ShippingPackageDetails) Trading API call to retrieve a list of supported package types for a specific marketplace.
- **shippingIrregular** (boolean)
  - A value of `true` indicates that the package is irregular and cannot go through the stamping machine at the shipping service office. This field applies to calculated shipping only. Irregular packages require special or fragile handling.
- **weight** (Weight)
  - This container is used to specify the weight of the shipping package that will be used to ship the inventory item. The weight of a shipping package are needed when calculated shipping is used, or if flat-rate shipping rates are used, but with a weight surcharge.  
  
This field will be returned if package weight is set for the inventory item.

### PickupAtLocationAvailability
**Description:** **Deprecated.** Do not use as STORE location types are no longer supported.
**Type:** object

**Properties:**
- **availabilityType** (AvailabilityTypeEnum)
  - The enumeration value in this field indicates the availability status of the inventory item at the merchant's physical store specified by the **pickupAtLocationAvailability.merchantLocationKey** field. This field is required if the **pickupAtLocationAvailability** container is used, and is always returned with the **pickupAtLocationAvailability** container.  
  
See [AvailabilityTypeEnum](/develop/api/sell/inventory_api#sell-inventory_api-inventory_item-bulkcreateorreplaceinventoryitem.availabilitytypeenum) for more information about how/when you use each enumeration value.
- **fulfillmentTime** (TimeDuration)
  - This container is used to indicate how soon an In-Store Pickup order will be available for pickup by the buyer after the order takes place. This container is required if the **pickupAtLocationAvailability** container is used, and is always returned with the **pickupAtLocationAvailability** container.
- **merchantLocationKey** (string)
  - The unique identifier of a merchant's store where the In-Store Pickup inventory item is currently located, or where inventory will be sent to. If the merchant's store is currently awaiting for inventory, the **availabilityType** value should be `SHIP_TO_STORE`. This field is required if the **pickupAtLocationAvailability** container is used, and is always returned with the **pickupAtLocationAvailability** container.  
  
Use the [getInventoryLocations](/develop/api/sell/inventory_api#sell-inventory_api-location-getinventorylocations) method to retrieve merchant location keys.  
  
**Maximum length**: 36
- **quantity** (integer)
  - This integer value indicates the quantity of the inventory item that is available for In-Store Pickup at the store identified by the **merchantLocationKey** value. The value of **quantity** should be an integer value greater than `0`, unless the inventory item is out of stock. This field is required if the **pickupAtLocationAvailability** container is used, and is always returned with the **pickupAtLocationAvailability** container.

### Product
**Description:** This type is used to define the product details, such as a title, a product description, product aspects/item specifics, and links to images for the product. Optionally, in a **createOrReplaceInventoryItem** call, a seller can pass in an eBay Product Identifier (ePID) or a Global Trade Item Number (GTIN) value, such as an EAN, an ISBN, a UPC, to identify a product to be matched with a product in the eBay Catalog. The information in this type is also returned in the **getInventoryItem**, **getInventoryItems**, and **bulkGetInventoryItem** calls if defined.
**Type:** object

**Properties:**
- **aspects** (string)
  - This is a collection of item specifics (aka product aspects) name-value pairs that provide more information about the product and might make it easier for buyers to find. To view required/recommended product aspects/item specifics names (and corresponding values) for a specific eBay category, sellers can use the [getItemAspectsForCategory](/develop/api/sell/taxonomy_api#sell-taxonomy_api-category_tree-getitemaspectsforcategory) method of the Taxonomy API. Alternatively, sellers can view similar items on eBay.com in the same category to get an idea of what other sellers are using for product aspects/item specifics.  
  

**Important!** Effective from December 28th, 2024, sellers offering certain rechargeable devices in EU and Northern Ireland markets must comply with the Common Charger Directive (CCD) and list appropriate charger-related aspects and values on their listings. See [Common Charger Directive](/api-docs/sell/static/inventory/common-charger-directive.html) for more information.

  
Sellers also have the option of specifying an eBay Product ID (ePID) or optionally, a Global Trade Item Number (GTIN) through the corresponding fields in the **product** container in an attempt to find a product match in the eBay Catalog. If a match is found based on the ePID or GTIN value, the product aspects that are defined for the eBay Catalog product will automatically get picked up by the newly created/updated inventory item.  
  
Below is an example of the proper JSON syntax to use when manually inputting item specifics. Note that one item specific name, such as 'Features', can have more than one value. If an item specific name has more than one value, each value is delimited with a comma.  
  

"aspects": {  
 "Brand": \["GoPro"\],  
 "Storage Type": \["Removable"\]  
 }

  
Note that inventory items that will become part of an inventory item group and multiple-variation listing should have the same attributes that are defined for the inventory item group.  
  
This container will be returned if one or more item specific pairs are defined for the inventory item.  
  

**Important!**Publish offer note: This field is required before an offer can be published to create an active listing.

  
**Maximum length for Aspect Name**: 40  
  
**Maximum length for Aspect Value**: 50
- **brand** (string)
  - The brand of the product. This field is often paired with the **mpn** field to identify a specific product by Manufacturer Part Number. This field is conditionally required if the eBay category requires a Manufacturer Part Number (MPN) value. If eBay is able to find a product match in the eBay Catalog when an eBay Product ID (ePID) or GTIN value (UPC, ISBN, or EAN) is supplied, all product details of that eBay Catalog product is picked up by the inventory item record (including brand) if the **createOrReplaceInventoryItem** call is successful.  
  
This field is returned if defined for an inventory item. If a brand was passed in as an item specific name-value pair through the **aspects** array in a **createOrReplaceInventoryItem** call, this value is also picked up by the **brand** field.  
  
**Maximum length**: 65
- **description** (string)
  - The description of the product. The description of an existing inventory item can be added or modified with a **createOrReplaceInventoryItem** call. The description of an inventory item is automatically populated if the seller specifies an eBay Product ID (ePID) or a Global Trade Item Number (GTIN) and eBay is able to find a matching product in the eBay Catalog.  
  
Note that this field is optional but recommended. If a **listingDescription** field is omitted when creating and publishing a single-variation offer, the text in this field will be used instead. If neither the **product.description** field for the inventory item nor the **listingDescription** field for the offer exist, the **publishOffer** call will fail. If the inventory item will be part of an inventory item group/multiple-variation listing, this field should definitely be used to specify how the corresponding product variation is different (e.g. _This is the green, extra-large version of the shirt_). However, in the case of an inventory item group, the text in the **description** field of the inventory item group will become the listing description of the actual eBay listing instead of the text in this field.  
  
Basic HTML tags are supported, including the following tags:

*   <b>
*   <strong>
*   <br>
*   <ol>
*   <ul>
*   <li>
*   Table tags including <table>, <tr>, <td>, <th>, <thead>, <tfoot>, <tbody>, <caption>, <colgroup>, and <col>

A seller can not use any active content in their listing description. Active content includes animation or video via JavaScript, Flash, plug-ins, or form actions.  
  
This field is returned if defined for an inventory item. If one of the GTIN types (e.g. UPC) was passed in when the inventory item was created/modified and a product match was found in the eBay catalog, product description is one of the details that gets picked up from the catalog product.  
  

**Important!**Publish offer note: This field is required before an offer can be published to create an active listing.

  
**Maximum length**: 4000
- **ean** (array)
  - The European Article Number/International Article Number (EAN) for the product. Although an ePID value is preferred when trying to find a product match in the eBay Catalog, this field can also be used in an attempt to find a product match in the eBay Catalog. If a product match is found in the eBay Catalog, the inventory item is automatically populated with available product details such as a title, a product description, product aspects (including the specified EAN value), and a link to any stock image that exists for the catalog product.  
  
This field is returned if defined for an inventory item. If an EAN was passed in as an item specific name-value pair through the **aspects** array in a **createOrReplaceInventoryItem** call, this value is also picked up by the **ean** field.

**Note:** If the item is being listed in a category that requires an EAN value, but one doesn't exist for the product, the seller must provide a string indicating that the product identifier is unavailable. This text varies by marketplace. Refer to [Product Identifier Text](/api-docs/sell/static/inventory/product-identifier-text.html) for the specific text based on the listing marketplace.
- **epid** (string)
  - The eBay Product Identifier (ePID) for the product. This field can be used to directly identify an eBay Catalog product. Based on its specified ePID value, eBay will search for the product in the eBay Catalog, and if a match is found, the inventory item is automatically populated with available product details such as product title, product description, product aspects, and a link to any stock image that exists for the catalog product.  
  
In an attempt to find a eBay Catalog product match, an ePID value is always preferred over the other product identifiers, since it is possible that one GTIN value can be associated with multiple eBay Catalog products, and if multiple products are found, product details will not be picked up by the Inventory Item object.

  
**Note:** When listing in categoryID 173651 (Auto Performance Tuning Devices & Software), the use of catalog products is required. For more information, see [Tuning devices and software](/api-docs/sell/static/inventory/tuning-devices-and-software-rest.html).

  
This field is returned if defined for an inventory item.
- **imageUrls** (array)
  - An array of one or more links to images for the product. URLs must use the "HTTPS" protocol. Images can be self-hosted by the seller, or sellers can use the [UploadSiteHostedPictures](</Devzone/XML/docs/Reference/eBay/UploadSiteHostedPictures.html >) call of the Trading API to upload images to an eBay Picture Server. If successful, the response of the [UploadSiteHostedPictures](</Devzone/XML/docs/Reference/eBay/UploadSiteHostedPictures.html >) call will contain a full URL to the image on an eBay Picture Server. This is the URL that will be passed in through the **imageUrls** array. Before an offer can be published, at least one image must exist for the inventory item. In almost any category at no cost, sellers can include up to 24 pictures in one listing. For inventory items that are a part of an inventory item group/multiple-variation listings, a maximum of 12 pictures may be used per inventory item in the group. Motor vehicle listings are an exception. The number of included pictures in motor vehicle listings depend on the selected vehicle package (see [Fees for selling vehicles on eBay Motors](<https://www.ebay.com/help/selling/fees-credits-invoices/motors-fees?id=4127 >)).  
  
A link to a stock image for a product may automatically be populated for an inventory item if the seller specifies an eBay Product ID (ePID) or a Global Trade Item Number (GTIN) and eBay is able to find a matching product in the eBay Catalog.  
  
This container will always be returned for an inventory item that is part of a published offer since a published offer will always have at least one picture, but this container will only be returned if defined for inventory items that are not a part of a published offer.  
  

**Important!**Publish offer note: This array is required and at least one image URL must be specified before an offer can be published to create an active listing.
- **isbn** (array)
  - The International Standard Book Number (ISBN) value for the product. Although an ePID value is preferred when trying to find a product match in the eBay Catalog, this field can also be used in an attempt to find a product match in the eBay Catalog. If a product match is found in the eBay Catalog, the inventory item is automatically populated with available product details such as a title, a product description, product aspects (including the specified ISBN value), and a link to any stock image that exists for the catalog product.  
  
This field is returned if defined for an inventory item. If an ISBN was passed in as an item specific name-value pair through the **aspects** array in a **createOrReplaceInventoryItem** call, this value is also picked up by the **isbn** field.

**Note:** If the item is being listed in a category that requires an ISBN value, but one doesn't exist for the product, the seller must provide a string indicating that the product identifier is unavailable. This text varies by marketplace. Refer to [Product Identifier Text](/api-docs/sell/static/inventory/product-identifier-text.html) for the specific text based on the listing marketplace.
- **mpn** (string)
  - The Manufacturer Part Number (MPN) of a product. This field is paired with the **brand** field to identify a product. Some eBay categories require MPN values. The getItemAspectsForCategory method in the Taxonomy API can be used to see if a category requires an MPN. The MPN value for a product may automatically be populated for an inventory item if the seller specifies an eBay Product ID (ePID) or a Global Trade Item Number (GTIN) and eBay is able to find a matching product in the eBay Catalog.  
  
This field is returned if defined for an inventory item. If an MPN was passed in as an item specific name-value pair through the **aspects** array in a **createOrReplaceInventoryItem** call, this value is also picked up by the **mpn** field.

**Note:** If the item is being listed in a category that requires an MPN value, but one doesn't exist for the product, the seller must provide a string indicating that the product identifier is unavailable. This text varies by marketplace. Refer to [Product Identifier Text](/api-docs/sell/static/inventory/product-identifier-text.html) for the specific text based on the listing marketplace.

**Maximum length**: 65
- **subtitle** (string)
  - A subtitle is an optional listing feature that allows the seller to provide more information about the product, possibly including keywords that may assist with search results. An additional listing fee will be charged to the seller if a subtitle is used. For more information on using listing subtitles on the US site, see the [Adding a subtitle to your listings](<https://pages.ebay.com/help/sell/itemsubtitle.html >) help page. The subtitle of an existing inventory item can added, modified, or removed with a **createOrReplaceInventoryItem** call.  
  
Note that the same **subtitle** text should be used for each inventory item that will be part of an inventory item group, and ultimately become one product variation within a multiple-variation listing.  
  
This field will only be returned if set for an inventory item.  
  
**Maximum length**: 55
- **title** (string)
  - The title of an inventory item can be added or modified with a **createOrReplaceInventoryItem** call. Although not immediately required, a title will be needed before an offer with the inventory item is published. The title of an inventory item is automatically populated if the seller specifies an eBay Product ID (ePID) or a Global Trade Item Number (GTIN) and eBay is able to find a matching product in the eBay Catalog. If the inventory item will become part of a single-variation offer, and the listing is not a product-based listing, the text in this field will become the actual listing title for the published offer. However, if the inventory item will become part of a multiple-variation offer, the text in **title** field of the inventory item group entity will actually become the listing title for the published offer instead, although a title can still be provided for the inventory item, and it will actually become the title of the variation.  
  
This field will always be returned for an inventory item that is part of a published offer since a published offer will always have a listing title, but this field will only be returned if defined for inventory items that are not a part of a published offer.  
  

**Important!**Publish offer note: This field is required before an offer can be published to create an active listing.

  
**Maximum length**: 80
- **upc** (array)
  - The Universal Product Code (UPC) value for the product. Although an ePID value is preferred when trying to find a product match in the eBay Catalog, this field can also be used in an attempt to find a product match in the eBay Catalog. If a product match is found in the eBay Catalog, the inventory item is automatically populated with available product details such as a title, a product description, product aspects (including the specified UPC value), and a link to any stock image that exists for the catalog product.  
  
This field is returned if defined for an inventory item. If a UPC was passed in as an item specific name-value pair through the **aspects** array in a **createOrReplaceInventoryItem** call, this value is also picked up by the **upc** field.

**Note:** If the item is being listed in a category that requires a UPC value, but one doesn't exist for the product, the seller must provide a string indicating that the product identifier is unavailable. This text varies by marketplace. Refer to [Product Identifier Text](/api-docs/sell/static/inventory/product-identifier-text.html) for the specific text based on the listing marketplace.
- **videoIds** (array)
  - An array of one or more **videoId** values for the product. A video ID is a unique identifier that is automatically created by eBay when a seller successfully uploads a video to eBay using the [uploadVideo](/develop/api/sell/media_api#sell-media_api-video-uploadvideo) method of the [Media API](/develop/api/sell/media_api).  
  
For information on supported marketplaces and platforms, as well as other requirements and limitations of video support, please refer to [Managing videos](</api-docs/sell/static/inventory/managing-video-media.html >).  
  
**Note:** Only one video per listing is supported.

### ShipToLocationAvailability
**Description:** This type is used to specify the total 'ship-to-home' quantity of the inventory item that will be available for purchase through one or more published offers.
**Type:** object

**Properties:**
- **availabilityDistributions** (array)
  - This container is used to set the available quantity of the inventory item at one or more warehouse locations.  
  
This container will be returned if available quantity is set for one or more inventory locations.
- **quantity** (integer)
  - This container is used to set the total 'ship-to-home' quantity of the inventory item that will be available for purchase through one or more published offers.  
  
This field represents the total quantity of the item that is available for sale across all marketplaces. To update the available quantity allocated to a specific marketplace, use the [**availableQuantity**](/develop/api/sell/inventory_api#sell-inventory_api-inventory_item-bulkupdatepricequantity.offerpricequantity.availablequantity) field in the **offer** container associated with that marketplace.  
  
**Note:** To ensure that the available quantity allocated to a specific marketplace doesn't exceed the total available stock, the quantity specified on a listing will be the minimum value between this field and the [**availableQuantity**](/develop/api/sell/inventory_api#sell-inventory_api-inventory_item-bulkupdatepricequantity.offerpricequantity.availablequantity) field.  
If an existing inventory item is being updated, and the 'ship-to-home' quantity already exists for the inventory item record, this field should be included again, even if the value is not changing, or the available quantity data will be lost.  
  

**Important!** This field is not immediately required, but 'ship-to-home' quantity must be set before an offer of the inventory item can be published.

### TimeDuration
**Description:** This type is used to indicate the fulfillment time for an order that will be shipped to the buyer.
**Type:** object

**Properties:**
- **unit** (TimeDurationUnitEnum)
  - This enumeration value indicates the time unit used to specify the fulfillment time, such as `BUSINESS_DAY`.
- **value** (integer)
  - The integer value in this field, along with the time unit in the **unit** field, will indicate the fulfillment time.  
  
For standard orders that will be shipped, this value will indicate the expected fulfillment time if the inventory item is shipped from the inventory location. If the value of this field is `4`, and the value of the **unit** field is `BUSINESS_DAY`, then the estimated delivery date after purchase is 4 business days.

### TimeDurationUnitEnum
**Description:** This enumeration type is used by the **unit** field of the **TimeDuration** type to specify the time unit that is used to indicate the fulfillment time for an order that will be shipped to the buyer. Typically, the unit value will be `BUSINESS_DAY`. | - **YEAR**: Time duration is based on a number of years. - **MONTH**: Time duration is based on a number of months - **DAY**: Time duration is based on a number of days. - **HOUR**: Time duration is based on a number of hours. - **CALENDAR_DAY**: Time duration is based on a number of calendar days, including Saturday and Sunday. This time duration does not exclude holidays. - **BUSINESS_DAY**: Time duration is based on a number of business days, or 'working days' (normally Monday through Friday). This excludes Sunday and all holidays in the time duration and, depending on the location, can include or exclude Saturday. - **MINUTE**: Time duration is based on a number of minutes. - **SECOND**: Time duration is based on a number of seconds. - **MILLISECOND**: Time duration is based on a number of milliseconds.
**Type:** object

### Weight
**Description:** This type is used to specify the weight (and the unit used to measure that weight) of a shipping package. The **weight** container is conditionally required if the seller will be offering calculated shipping rates to determine shipping cost, or is using flat-rate costs, but charging a weight surcharge. See the [Calculated shipping](<https://pages.ebay.com/help/pay/calculated-shipping.html >) help page for more information on calculated shipping.
**Type:** object

**Properties:**
- **unit** (WeightUnitOfMeasureEnum)
  - The unit of measurement used to specify the weight of a shipping package. Both the **unit** and **value** fields are required if the **weight** container is used. If the English system of measurement is being used, the applicable values for weight units are `POUND` and `OUNCE`. If the metric system of measurement is being used, the applicable values for weight units are `KILOGRAM` and `GRAM`. The metric system is used by most countries outside of the US.
- **value** (number)
  - The actual weight (in the measurement unit specified in the **unit** field) of the shipping package. Both the **unit** and **value** fields are required if the **weight** container is used. If a shipping package weighed 20.5 ounces, the container would look as follows:  

"weight": {  
 "value": 20.5,  
 "unit": "OUNCE"  
 }

### WeightUnitOfMeasureEnum
**Description:** This enumerated type is used to indicate what unit of measurement is used to measure the weight of a shipping package. The weight and dimensions of a shipping package are generally required when calculated shipping rates are used, and weight is required if flat-rate shipping is used, but the seller is charging a weight surcharge. | - **POUND**: This enumeration value indicates that the unit of measurement used for measuring the weight of the shipping package is pounds. - **KILOGRAM**: This enumeration value indicates that the unit of measurement used for measuring the weight of the shipping package is kilograms. - **OUNCE**: This enumeration value indicates that the unit of measurement used for measuring the weight of the shipping package is ounces. - **GRAM**: This enumeration value indicates that the unit of measurement used for measuring the weight of the shipping package is grams.
**Type:** object

### AvailabilityWithAll
**Description:** This type is used to specify the quantity of the inventory items that are available for purchase if the items will be shipped to the buyer.
**Type:** object

**Properties:**
- **pickupAtLocationAvailability** (array)
  - **Deprecated.** Do not use as STORE location types are no longer supported.
- **shipToLocationAvailability** (ShipToLocationAvailabilityWithAll)
  - This container specifies the quantity of the inventory items that are available for a standard purchase, where the item is shipped to the buyer.

### BulkGetInventoryItem
**Description:** This type is used by the base request of the **bulkGetInventoryItem** method.
**Type:** object

**Properties:**
- **requests** (array)
  - The seller passes in multiple SKU values under this container to retrieve multiple inventory item records. Up to 25 inventory item records can be retrieved at one time.

### BulkGetInventoryItemResponse
**Description:** This type is used by the base response of the **bulkGetInventoryItem** method.
**Type:** object

**Properties:**
- **responses** (array)
  - This is the base container of the **bulkGetInventoryItem** response. The results of each attempted inventory item retrieval is captured under this container.

### FormatAllocation
**Description:** This type is used to indicate the quantities of the inventory items that are reserved for the different listing formats of the SKU offers.
**Type:** object

**Properties:**
- **auction** (integer)
  - This integer value indicates the quantity of the inventory item that is reserved for the published auction format offers of the SKU.
- **fixedPrice** (integer)
  - This integer value indicates the quantity of the inventory item that is available for the fixed-price offers of the SKU.

### GetInventoryItem
**Description:** The seller-defined Stock-Keeping Unit (SKU) of each inventory item that the user wants to retrieve is passed in the request of the **bulkGetInventoryItem** method.
**Type:** object

**Properties:**
- **sku** (string)
  - An array of SKU values are passed in under the **sku** container to retrieve up to 25 inventory item records.  
  
Use the [getInventoryItems](/develop/api/sell/inventory_api#sell-inventory_api-inventory_item-getinventoryitems) method to retrieve SKU values.

### GetInventoryItemResponse
**Description:** This type is used by the response of the **bulkGetInventoryItem** method to give the status of each inventory item record that the user tried to retrieve.
**Type:** object

**Properties:**
- **errors** (array)
  - This container will be returned if there were one or more errors associated with retrieving the inventory item record.
- **inventoryItem** (InventoryItemWithSkuLocaleGroupKeys)
  - This container consists of detailed information on the inventory item specified in the **sku** field.
- **sku** (string)
  - The seller-defined Stock-Keeping Unit (SKU) of the inventory item. The seller should have a unique SKU value for every product that they sell.
- **statusCode** (integer)
  - The HTTP status code returned in this field indicates the success or failure of retrieving the inventory item record for the inventory item specified in the **sku** field. See the **HTTP status codes** table to see which each status code indicates.
- **warnings** (array)
  - This container will be returned if there were one or more warnings associated with retrieving the inventory item record.

### InventoryItemWithSkuLocaleGroupKeys
**Description:** This type is used to provide details about each retrieved inventory item record.
**Type:** object

**Properties:**
- **availability** (AvailabilityWithAll)
  - This container shows the quantity of the inventory item that is available for purchase if the item will be shipped to the buyer.
- **condition** (ConditionEnum)
  - This enumeration value indicates the condition of the item. Supported item condition values will vary by eBay site and category.  
  
Since the condition of an inventory item must be specified before being published in an offer, this field is always returned in the 'Get' calls for SKUs that are part of a published offer. If a SKU is not part of a published offer, this field will only be returned if set for the inventory item.
- **conditionDescription** (string)
  - This string field is used by the seller to more clearly describe the condition of used items, or items that are not 'Brand New', 'New with tags', or 'New in box'. The ConditionDescription field is available for all categories. If the ConditionDescription field is used with an item in a new condition (Condition IDs 1000-1499), eBay will simply ignore this field if included, and eBay will return a warning message to the user. This field should only be used to further clarify the condition of the used item. It should not be used for branding, promotions, shipping, returns, payment or other information unrelated to the condition of the item. Make sure that the condition value, condition description, listing description, and the item's pictures do not contradict one another.  
  
Maximum length: 1000
- **conditionDescriptors** (array)
  - This container is used by the seller to provide additional information about the condition of an item in a structured format. Condition descriptors are name-value attributes that can be either closed set or open text.  
  
For trading card coin listings in applicable categories, sellers must use either `LIKE_NEW` (2750) or `USED_VERY_GOOD` (4000) item condition to specify the item as **Graded** or **Ungraded**, respectively. Use of either of these conditions requires the seller to use this array to provide one or more applicable Condition Descriptor name-value pairs.  
  
\>To retrieve all condition descriptor numeric IDs for a category, use the [getItemConditionPolicies](/develop/api/sell/metadata_api#sell-metadata_api-marketplace-getitemconditionpolicies) method of the Metadata API.
- **inventoryItemGroupKeys** (array)
  - This array is returned if the inventory item is associated with any inventory item group(s). The value(s) returned in this array are the unique identifier(s) of the inventory item's variation in a multiple-variation listing. This array is not returned if the inventory item is not associated with any inventory item groups.
- **locale** (LocaleEnum)
  - This field returns the natural language that was provided in the field values of the request payload (i.e., en\_AU, en\_GB or de\_DE).
- **packageWeightAndSize** (PackageWeightAndSize)
  - This container is used to specify the dimensions and weight of a shipping package.
- **product** (Product)
  - This container is used in a **createOrReplaceInventoryItem** call to pass in a Global Trade Item Number (GTIN) or a Brand and Manufacturer Part Number (MPN) pair to identify a product to be matched with a product in the eBay catalog. If a match is found in the eBay product catalog, the inventory item is automatically populated with available product details such as a title, a subtitle, a product description, item specifics, and links to stock images for the product.
- **sku** (string)
  - The seller-defined Stock-Keeping Unit (SKU) of the inventory item. The seller should have a unique SKU value for every product that they sell.

### ShipToLocationAvailabilityWithAll
**Description:** This type is used to specify the total 'ship-to-home' quantity of the inventory items that will be available for purchase through one or more published offers.
**Type:** object

**Properties:**
- **allocationByFormat** (FormatAllocation)
  - This container is used to specify the quantity of the inventory item that is available for purchase, allocated by the offer types.
- **availabilityDistributions** (array)
  - This container is used to set the available quantity of the inventory item at one or more warehouse locations.  
  
This container will be returned if the available quantity is set for one or more inventory locations.
- **quantity** (integer)
  - **Important!** Publish offer note: Although this field is not required before an offer can be published to create an active listing, out of stock listings will result if this field is omitted or set to `0`.

  
This field is used to set the total 'ship-to-home' quantity of the inventory item that will be available for purchase through one or more published offers. This field is not immediately required, but 'ship-to-home' quantity must be set before an offer of the inventory item can be published.  
  
If an existing inventory item is being updated, and the 'ship-to-home' quantity already exists for the inventory item record, this field should be included again, even if the value is not changing, or the available quantity data will be lost.

### Amount
**Description:** This type is used to express a dollar value and the applicable currency.
**Type:** object

**Properties:**
- **currency** (string)
  - A three-letter string value representing the type of currency being used. Both the **value** and **currency** fields are required/always returned when expressing prices.  
  
See [ISO 4217](https://www.iso.org/iso-4217-currency-codes.html) for more information and links to the full list of currencies and their corresponding three-letter string values.
- **value** (string)
  - A string representation of a dollar value expressed in the currency specified in the **currency** field. Both the **value** and **currency** fields are required/always returned when expressing prices.

### BulkPriceQuantity
**Description:** This type is used by the base request payload of the **bulkUpdatePriceQuantity** call. The **bulkUpdatePriceQuantity** call allows the seller to update the total 'ship-to-home' quantity of one or more inventory items (up to 25) and/or to update the price and/or quantity of one or more specific published offers.
**Type:** object

**Properties:**
- **requests** (array)
  - This container is used by the seller to update the total 'ship-to-home' quantity of one or more inventory items (up to 25) and/or to update the price and/or quantity of one or more specific published offers.

### BulkPriceQuantityResponse
**Description:** This type is use by the base response payload of the **bulkUpdatePriceQuantity** call. The **bulkUpdatePriceQuantity** call response will return an HTTP status code, offer ID, and SKU value for each offer/inventory item being updated, as well as an **errors** and/or **warnings** container if any errors or warnings are triggered while trying to update those offers/inventory items.
**Type:** object

**Properties:**
- **responses** (array)
  - This container will return an HTTP status code, offer ID, and SKU value for each offer/inventory item being updated, as well as an **errors** and/or **warnings** container if any errors or warnings are triggered while trying to update those offers/inventory items.

### OfferPriceQuantity
**Description:** This type is used by the **offers** container in a **Bulk Update Price and Quantity** call to update the current price and/or quantity of one or more offers associated with a specific inventory item.
**Type:** object

**Properties:**
- **availableQuantity** (integer)
  - This field is used if the seller wants to modify the current quantity of the inventory item that will be available for purchase in the offer (identified by the corresponding **offerId** value).  
  
This value represents the quantity of the item that is available in the marketplace specified within the offer, not the total quantity available. Because of this, this value should not exceed the value specified in the [quantity](/develop/api/sell/inventory_api#sell-inventory_api-inventory_item-bulkupdatepricequantity.shiptolocationavailability.quantity) field of the **shipToLocationAvailability** container (the total available quantity of the item across all marketplaces).  
  
**Note:** To ensure that the available quantity allocated to a specific marketplace doesn't exceed the total available stock, the quantity specified on a listing will be the minimum value between this field and the [**quantity**](/develop/api/sell/inventory_api#sell-inventory_api-inventory_item-bulkupdatepricequantity.shiptolocationavailability.quantity) field.  
Either the **availableQuantity** field or the **price** container is required, but not necessarily both.
- **offerId** (string)
  - This field is the unique identifier of the offer. If an **offers** container is used to update one or more offers associated to a specific inventory item, the **offerId** value is required in order to identify the offer to update with a modified price and/or quantity.  
  
The seller can use the [getOffers](/develop/api/sell/inventory_api#method-offer-getOffers) method (passing in the correct SKU value as a query parameter) to retrieve **offerId** values for offers associated with the SKU.
- **price** (Amount)
  - This container is used if the seller wants to modify the current price of the inventory item. The dollar value set here will be the new price of the inventory item in the offer (identified by the corresponding **offerId** value). Either the **availableQuantity** field or the **price** container is required, but not necessarily both.

### PriceQuantity
**Description:** This type is used to update the total "ship-to-home" quantity for one or more inventory items and/or to update the price and/or quantity of one or more specific offers associated with one or more inventory items.
**Type:** object

**Properties:**
- **offers** (array)
  - This container is needed if the seller is updating the price and/or quantity of one or more published offers, and a successful call will actually update the active eBay listing with the revised price and/or available quantity.  
  
This call is not designed to work with unpublished offers. For unpublished offers, the seller should use the **updateOffer** call to update the available quantity and/or price.  
  
If the seller is also using the **shipToLocationAvailability** container and **sku** field to update the total 'ship-to-home' quantity of the inventory item, the SKU value associated with the corresponding **offerId** value(s) must be the same as the corresponding **sku** value that is passed in, or an error will occur.  
  

**Important!** A separate (**OfferPriceQuantity**) node is required for each offer being updated.
- **shipToLocationAvailability** (ShipToLocationAvailability)
  - This container is needed if the seller is updating the total 'ship-to-home' quantity for the corresponding inventory item (specified in the **sku** field). A successful call will update the inventory item record associated with the **sku** value.
- **sku** (string)
  - This is the seller-defined SKU value of the inventory item whose total 'ship-to-home' quantity will be updated. This field is only required when the seller is updating the total quantity of an inventory item using the **shipToLocationAvailability** container. If the seller is updating the price and/or quantity of one or more specific offers, one or more **offerId** values are used instead, and the **sku** value is not needed.  
  
If the seller wants to update the price and/or quantity of one or more offers, and also wants to update the total 'ship-to-home' quantity of the corresponding inventory item, the SKU value associated with the **offerId** value(s) must be the same as the corresponding **sku** value that is passed in, or an error will occur.  
  
Use the [getInventoryItems](/develop/api/sell/inventory_api#sell-inventory_api-inventory_item-getinventoryitems) method to retrieve SKU values.  
  
**Maximum length**: 50

### PriceQuantityResponse
**Description:** This type is used to display the result for each offer and/or inventory item that the seller attempted to update with a **bulkUpdatePriceQuantity** call. If any errors or warnings occur, the error/warning data is returned at the offer/inventory item level.
**Type:** object

**Properties:**
- **errors** (array)
  - This array will be returned if there were one or more errors associated with the update to the offer or inventory item record.
- **offerId** (string)
  - The unique identifier of the offer that was updated. This field will not be returned in situations where the seller is only updating the total 'ship-to-home' quantity of an inventory item record.
- **sku** (string)
  - This is the seller-defined SKU value of the product. This field is returned whether the seller attempted to update an offer with the SKU value or just attempted to update the total 'ship-to-home' quantity of an inventory item record.  
  
**Maximum length**: 50
- **statusCode** (integer)
  - The value returned in this container will indicate the status of the attempt to update the price and/or quantity of the offer (specified in the corresponding **offerId** field) or the attempt to update the total 'ship-to-home' quantity of an inventory item (specified in the corresponding **sku** field). For a completely successful update of an offer or inventory item record, a value of `200` will appear in this field. A user can view the **HTTP status codes** section for information on other status codes that may be returned with the **bulkUpdatePriceQuantity** method.
- **warnings** (array)
  - This array will be returned if there were one or more warnings associated with the update to the offer or inventory item record.

### InventoryItemWithSkuLocaleGroupid
**Description:** This type is used to provide details of a single inventory item.
**Type:** object

**Properties:**
- **availability** (AvailabilityWithAll)
  - This container is used to specify the quantity of the inventory item that is available for purchase if the item will be shipped to the buyer.
- **condition** (ConditionEnum)
  - This enumeration value indicates the condition of the item. Supported item condition values will vary by eBay site and category.  
  
Since the condition of an inventory item must be specified before being published in an offer, this field is always returned in the 'Get' calls for SKUs that are part of a published offer. If a SKU is not part of a published offer, this field will only be returned if set for the inventory item.
- **conditionDescription** (string)
  - This string field is used by the seller to more clearly describe the condition of used items, or items that are not 'Brand New', 'New with tags', or 'New in box'. The ConditionDescription field is available for all categories. If the ConditionDescription field is used with an item in a new condition (Condition IDs 1000-1499), eBay will simply ignore this field if included, and eBay will return a warning message to the user. This field should only be used to further clarify the condition of the used item. It should not be used for branding, promotions, shipping, returns, payment or other information unrelated to the condition of the item. Make sure that the condition value, condition description, listing description, and the item's pictures do not contradict one another.  
  
**Maximum length**: 1000
- **conditionDescriptors** (array)
  - This container is used by the seller to provide additional information about the condition of an item in a structured format. Condition descriptors are name-value attributes that can be either closed set or open text.  
  
For trading card coin listings in applicable categories, sellers must use either `LIKE_NEW` (2750) or `USED_VERY_GOOD` (4000) item condition to specify the item as **Graded** or **Ungraded**, respectively. Use of either of these conditions requires the seller to use this array to provide one or more applicable Condition Descriptor name-value pairs.  
  
retrieve all condition descriptor numeric IDs for a category, use the [getItemConditionPolicies](/develop/api/sell/metadata_api#sell-metadata_api-marketplace-getitemconditionpolicies) method of the Metadata API.
- **groupIds** (array)
  - This array is returned if the inventory item is associated with any inventory item group(s). The value(s) returned in this array are the unique identifier(s) of the inventory item group(s). This array is not returned if the inventory item is not associated with any inventory item groups.
- **inventoryItemGroupKeys** (array)
  - This array is returned if the inventory item is associated with any inventory item group(s). The value(s) returned in this array are the unique identifier(s) of the inventory item's variation in a multiple-variation listing. This array is not returned if the inventory item is not associated with any inventory item groups.
- **locale** (LocaleEnum)
  - This field returns the natural language that was provided in the field values of the request payload (i.e., en\_AU, en\_GB or de\_DE).
- **packageWeightAndSize** (PackageWeightAndSize)
  - This container is used to specify the dimensions and weight of a shipping package.
- **product** (Product)
  - This container is used in a **createOrReplaceInventoryItem** call to pass in a Global Trade Item Number (GTIN) or a Brand and Manufacturer Part Number (MPN) pair to identify a product to be matched with a product in the eBay catalog. If a match is found in the eBay product catalog, the inventory item is automatically populated with available product details such as a title, a subtitle, a product description, item specifics, and links to stock images for the product.
- **sku** (string)
  - The seller-defined Stock-Keeping Unit (SKU) of the inventory item. The seller should have a unique SKU value for every product that they sell.

### BaseResponse
**Description:** This is the base response of the **createOrReplaceInventoryItem**, **createOrReplaceInventoryItemGroup**, and **createOrReplaceProductCompatibility** calls. A response payload will only be returned for these three calls if one or more errors or warnings occur with the call.
**Type:** object

**Properties:**
- **warnings** (array)
  - This container will be returned in a call response payload if one or more warnings or errors are triggered when an Inventory API call is made. This container will contain detailed information about the error or warning.

### InventoryItem
**Description:** This type is used to provide detailed information about an inventory item.
**Type:** object

**Properties:**
- **availability** (Availability)
  - This container is used to specify the quantity of the inventory item that are available for purchase.  
  
This container is optional up until the seller is ready to publish an offer with the SKU, at which time it becomes required. Availability data must also be passed if an inventory item is being updated and availability data already exists for that inventory item.  
  
Since an inventory item must have specified quantity before being published in an offer, this container is always returned in the 'Get' calls for SKUs that are part of a published offer. If a SKU is not part of a published offer, this container will only be returned if set for the inventory item.
- **condition** (ConditionEnum)
  - This enumeration value indicates the condition of the item. Supported item condition values will vary by eBay site and category. To see which item condition values that a particular eBay category supports, use the [getItemConditionPolicies](/develop/api/sell/metadata_api#sell-metadata_api-marketplace-getitemconditionpolicies) method of the **Metadata API**. This method returns condition ID values that map to the enumeration values defined in the [ConditionEnum](/develop/api/sell/inventory_api#sell-inventory_api-inventory_item-getinventoryitems.conditionenum) type. The [Item condition ID and name values](/api-docs/sell/static/metadata/condition-id-values.html) topic in the **Selling Integration Guide** has a table that maps condition ID values to **ConditionEnum** values. The **getItemConditionPolicies** call reference page has more information.  
  
A **condition** value is optional up until the seller is ready to publish an offer with the SKU, at which time it becomes required for most eBay categories.  
  

**Important!**Publish offer note: This field is required before an offer can be published to create an active listing.
- **conditionDescription** (string)
  - This string field is used by the seller to more clearly describe the condition of a used inventory item, or an inventory item whose **condition** value is not `NEW`, `LIKE_NEW`, `NEW_OTHER`, or `NEW_WITH_DEFECTS`.  
  
The **conditionDescription** field is available for all eBay categories. If the **conditionDescription** field is used with an item in one of the new conditions (mentioned in previous paragraph), eBay will simply ignore this field if included, and eBay will return a warning message to the user.  
  
This field should only be used to further clarify the condition of the used item. It should not be used for branding, promotions, shipping, returns, payment or other information unrelated to the condition of the used item. Make sure that the **condition** value, condition description, listing description, and the item's pictures do not contradict one another.  
  
This field is not always required, but is required if an inventory item is being updated and a condition description already exists for that inventory item.  
  
This field is returned in the **getInventoryItem** and **getInventoryItems** calls if a condition description was provided for a used inventory item.  
  
**Maximum length**: 1000.
- **conditionDescriptors** (array)
  - This container is used by the seller to provide additional information about the condition of an item in a structured format. Condition descriptors are name-value attributes that can be either closed set or open text inputs.  
  
For trading card and coin listings in applicable categories, categories, sellers must use either `LIKE_NEW` (2750) or `USED_VERY_GOOD` (4000) item condition to specify the item as **Graded** or **Ungraded**, respectively. Use of either of these conditions requires the seller to use this array to provide one or more applicable Condition Descriptor name-value pairs.  
  
To retrieve all condition descriptor numeric IDs for a category, use the [getItemConditionPolicies](/develop/api/sell/metadata_api#sell-metadata_api-marketplace-getitemconditionpolicies) method of the Metadata API.
- **packageWeightAndSize** (PackageWeightAndSize)
  - This container is used if the seller is offering one or more calculated shipping options for the inventory item, or if the seller is offering flat-rate shipping but is including a shipping surcharge based on the item's weight. This container is used to specify the dimensions and weight of a shipping package.  
  
**Note:** Package weight and dimensions are only supported for the following marketplaces: AU, CA, DE, IT, UK, US, and Motors. If this information is provided on other marketplaces, it will be ignored.  
This container is not always required, but is required if an inventory item is being updated and shipping package data already exists for that inventory item.  
  
This container is returned in the **getInventoryItem** and **getInventoryItems** calls if package type, package weight, and/or package dimensions are specified for an inventory item.  
  
See the [Calculated shipping](<https://pages.ebay.com/help/pay/calculated-shipping.html >) help page for more information on calculated shipping.
- **product** (Product)
  - This container is used to define the product details, such as product title, product description, product identifiers (eBay Product ID, GTIN, or Brand/MPN pair), product aspects/item specifics, and product images. Note that an eBay Product ID (ePID) or a Global Trade Item Number (GTIN) value can be used in an attempt to find a matching product in the eBay Catalog. If a product match is found, the inventory item record will automatically pick up all product details associated with the eBay Catalog product.  
  
Many eBay categories will require at least one product identifier (a GTIN or a Brand/MPN pair). To discover which product identifier(s) that an eBay category might require or support, use the [getItemAspectsForCategory](/develop/api/sell/taxonomy_api#sell-taxonomy_api-category_tree-getitemaspectsforcategory) method in the Taxonomy API. In the **getItemAspectsForCategory** response, look for product identifier names (`brand`, `mpn`, `upc`, `ean`, `isbn`) in the **localizedAspectName** fields, and then look for the corresponding **aspectRequired** boolean fields as well as the corresponding **aspectUsage** field, which will indicate if the aspect is required, recommended, or optional. In some cases, a product identifier type may be required, but not known/applicable for a product. If this is the case, the seller must still include the corresponding field in the inventory item record, but pass in a default text string. This text string can vary by site, so the seller should use the **GeteBayDetails** call of the Trading API to get this string value. In the **GeteBayDetails** call, the seller should include a **DetailName** field with its value set to `ProductDetails`. In the response of the call, the seller can see the default string value in the **ProductDetails.ProductIdentifierUnavailableText** field. The seller will use this value in one or more of the product identifier fields (**ean**, **isbn**, **upc**, or **mpn**) if a product ID isn't known or applicable.  
  
This container is not initially required, but it is required before an inventory item can be published as an offer, and/or if an inventory item is being updated and product data already exists for that inventory item.  
  
This container is always returned for published offers in the **getInventoryItem**, **bulkGetInventoryItem**, and **getInventoryItems** calls since product data must be defined for published offers, but for unpublished inventory items, this container will only be returned if product details have been defined for the inventory item.  
  

**Important!**Publish offer note: This container and a few of its child fields (as noted below) are required before an offer can be published to create an active listing.

### Address
**Description:** This type is used to define the physical address of an inventory location.
**Type:** object

**Properties:**
- **addressLine1** (string)
  - The first line of a street address. This field is required for fulfillment center locations. A street address is not required for warehouse locations.  
  
This field will be returned if defined for an inventory location.  
  
**Maximum length**: 128
- **addressLine2** (string)
  - The second line of a street address. This field can be used for additional address information, such as a suite or apartment number.  
  
This field will be returned if defined for an inventory location.  
  
**Maximum length**: 128
- **city** (string)
  - The city in which the inventory location resides. This field is required for fulfillment center locations. For warehouse locations, this field is conditionally required as part of a **city** and **stateOrProvince** pair if a **postalCode** is not provided. If a **postalCode** is provided, the city is derived from the provided postal code and this field is technically optional.  
  
This field is returned if defined for an inventory location.  
  
**Maximum length**: 128
- **country** (CountryCodeEnum)
  - The country in which the address resides, represented as two-letter [ISO 3166](<https://www.iso.org/iso-3166-country-codes.html > "https://www.iso.org ") country code. For example, `US` represents the United States, and `DE` represents Germany.
- **county** (string)
  - The county in which the address resides.  
  
This field is returned if defined for an inventory location.
- **postalCode** (string)
  - The postal/zip code of the address. eBay also uses postal codes (origin and destination) to estimate shipping costs when the seller uses calculated shipping. This field is required for fulfillment center locations.  
  
For warehouse locations, this field is conditionally required if a **city** and **stateOrProvince** pair is not provided.  
  
**Note:** For warehouse locations, **city** and **stateOrProvince** pair can be used instead of a **postalCode** value, and then the postal code is just derived from the city and state/province.  
This field is returned if defined for an inventory location.  
  
**Maximum length**: 16
- **stateOrProvince** (string)
  - The state/province in which the inventory location resides. This field is required for fulfillment center locations. For warehouse locations, this field is conditionally required as part of a **city** and **stateOrProvince** pair if a **postalCode** is not provided. If a **postalCode** is provided, the state or province is derived from the provided zip code and this field is technically optional.  
  
**Maximum length**: 128

### BestOffer
**Description:** This type is used by the [bestOfferTerms](/develop/api/sell/inventory_api#sell-inventory_api-offer-createoffer.listingpolicies.bestofferterms) container, which is used if the seller would like to support the Best Offer feature on their listing.
**Type:** object

**Properties:**
- **autoAcceptPrice** (Amount)
  - This is the price at which Best Offers are automatically accepted. If a buyer submits a Best Offer that is equal to or above this value, the offer is automatically accepted on behalf of the seller. This field is only applicable if the **bestOfferEnabled** value is set to `true`.  
  
The price set here must be lower than the current 'Buy it Now' price. This field is only returned by [getOffer](/develop/api/sell/inventory_api#sell-inventory_api-offer-getoffer) and [getOffers](/develop/api/sell/inventory_api#sell-inventory_api-offer-getoffers) if set.
- **autoDeclinePrice** (Amount)
  - This is the price at which Best Offers are automatically declined. If a buyer submits a Best Offer that is equal to or below this value, the offer is automatically declined on behalf of the seller. This field is only applicable if the **bestOfferEnabled** value is set to `true`.  
  
The price set here must be lower than the current 'Buy it Now' price and the price set in the **autoAcceptPrice** field (if used). This field is only returned by [getOffer](/develop/api/sell/inventory_api#sell-inventory_api-offer-getoffer) and [getOffers](/develop/api/sell/inventory_api#sell-inventory_api-offer-getoffers) if set.
- **bestOfferEnabled** (boolean)
  - This field indicates whether or not the Best Offer feature is enabled for the listing. A seller can enable the Best Offer feature for a listing as long as the category supports the Best Offer feature.  
  
The seller includes this field and sets its value to `true` to enable Best Offer feature.  
  
**Note:** Best Offer is not available for multi-variation listings.

### BulkEbayOfferDetailsWithKeys
**Description:** This type is used by the base request of the **bulkCreateOffer** method, which is used to create up to 25 new offers.
**Type:** object

**Properties:**
- **requests** (array)
  - The details of each offer that is being created is passed in under this container. Up to 25 offers can be created with one **bulkCreateOffer** call.

### BulkMigrateListing
**Description:** This type is used by the base container of the **bulkMigrateListings** request payload.
**Type:** object

**Properties:**
- **requests** (array)
  - This is the base container of the **bulkMigrateListings** request payload. One to five eBay listings will be included under this container.

### BulkMigrateListingResponse
**Description:** This type is used by the response payload of the **bulkMigrateListings** call.
**Type:** object

**Properties:**
- **responses** (array)
  - This is the base container of the response payload of the **bulkMigrateListings** call. The results of each attempted listing migration is captured under this container.

### BulkOffer
**Description:** This type is used by the base request of the **bulkPublishOffer** method, which is used to publish up to 25 different offers.
**Type:** object

**Properties:**
- **requests** (array)
  - This container is used to pass in an array of offers to publish. Up to 25 offers can be published with one **bulkPublishOffer** method.

### BulkOfferResponse
**Description:** This type is used by the base response of the **bulkCreateOffer** method.
**Type:** object

**Properties:**
- **responses** (array)
  - This object contains the responses that show the status of each offer that the seller attempted to create with the method call.

### BulkPublishResponse
**Description:** This type is used by the base response of the **bulkPublishOffer** method.
**Type:** object

**Properties:**
- **responses** (array)
  - A node is returned under the **responses** container to indicate the success or failure of each offer that the seller was attempting to publish.

### Charity
**Description:** This type is used to identify the charitable organization associated with the listing, and the percentage of the sale proceeds that the charitable organization will receive for each sale generated by the listing.  
  
In order to receive a percentage of the sales proceeds, the charitable organization must be registered with the PayPal Giving Fund, which is a partner of eBay for Charity.
**Type:** object

**Properties:**
- **charityId** (string)
  - The eBay-assigned unique identifier of the charitable organization that will receive a percentage of the sales proceeds. The charitable organization must be reqistered with the PayPal Giving Fund in order to receive sales proceeds through eBay listings.  
  
This field is conditionally required if a seller is planning on donating a percentage of the sale proceeds to a charitable organization.  
  
The eBay-assigned unique identifier of a charitable organization can be found using the [getCharityOrgs](/develop/api/sell/charity_api#sell-charity_api-charity_org-getcharityorgs) method of the Charity API. In the **getCharityOrgs** response, this unique identifier is shown in the [charityOrgId](/develop/api/sell/charity_api#sell-charity_api-charity_org-getcharityorgs.charityorg.logoimage) field.
- **donationPercentage** (string)
  - This field is the percentage of the purchase price that the charitable organization (identified in the **charityId** field) will receive for each sale that the listing generates. This field is conditionally required if a seller is planning on donating a percentage of the sale proceeds to a charitable organization. This numeric value can range from 10 to 100, and in any 5 (percent) increments in between this range (e.g. `10`, `15`, `20`...`95`,... `100`). The seller would pass in `10` for 10 percent, `15` for 15 percent, `20` for 20 percent, and so on, all the way to `100` for 100 percent.

### Compatibility
**Description:** This type is used by the **createOrReplaceProductCompatibility** call to associate compatible vehicles to an inventory item. This type is also the base response of the **getProductCompatibility** call.
**Type:** object

**Properties:**
- **compatibleProducts** (array)
  - This container consists of an array of motor vehicles (make, model, year, trim, engine) that are compatible with the motor vehicle part or accessory specified by the sku value.
- **sku** (string)
  - The seller-defined SKU value of the inventory item that will be associated with the compatible vehicles.  
  
**Note:** This field is not applicable to the **createOrReplaceProductCompatibility** method, as the SKU value for the inventory item is passed in as part of the call URI and not in the request payload. It is always returned with the [getProductCompatibility](/develop/api/sell/inventory_api#sell-inventory_api-product_compatibility-getproductcompatibility) method.

### CompatibleProduct
**Description:** This type is used to specify/indicate the motor vehicles that are compatible with the corresponding inventory item.
**Type:** object

**Properties:**
- **compatibilityProperties** (array)
  - This container consists of an array of motor vehicles that are compatible with the motor vehicle part or accessory specified by the SKU value in the call URI. Each motor vehicle is defined through a separate set of name/value pairs. In the **name** field, the vehicle aspect (such as 'make', 'model', 'year', 'trim', or 'engine') will be identified, and the **value** field will be used to identify the value of each aspect.  
  
The [getCompatibilityProperties](/develop/api/sell/taxonomy_api#sell-taxonomy_api-category_tree-getcompatibilityproperties) method of the Taxonomy API can be used to retrieve applicable vehicle aspect names for a specified category, and the [getCompatibilityPropertyValues](/develop/api/sell/taxonomy_api#sell-taxonomy_api-category_tree-getcompatibilitypropertyvalues) method of the Taxonomy API can be used to retrieve possible values for these same vehicle aspect names.  
  
Below is an example of identifying one motor vehicle using the **compatibilityProperties** container:  
  

"compatibilityProperties" : \[  
  {  
   "name" : "make",  
   "value" : "Subaru"  
  },  
  {  
   "name" : "model",  
   "value" : "GL"  
  },  
  {  
   "name" : "year",  
   "value" : "1983"  
  },  
  {  
   "name" : "trim",  
   "value" : "Base Wagon 4-Door"  
  },  
  {  
   "name" : "engine",  
   "value" : "1.8L Turbocharged"  
  }  
\]

  
  
Typically, the make, model, and year of the motor vehicle are always required, with the trim and engine being necessary sometimes, but it will be dependent on the part or accessory, and on the vehicle class.  
  
**Note:** The **productFamilyProperties** container is deprecated and should no longer be used. The **compatibilityProperties** container should be used instead.
- **notes** (string)
  - This field is used by the seller to input any notes pertaining to the compatible vehicle list being defined. The seller might use this field to specify the placement of the part on a vehicle or other applicable information.  
  
This field will only be returned if specified by the seller.  
  
**Maximum length**: 500
- **productFamilyProperties** (ProductFamilyProperties)
  - **Important!** The **productFamilyProperties** container is deprecated and should no longer be used. The **compatibilityProperties** container should be used instead.
- **productIdentifier** (ProductIdentifier)
  - This container is used in a **createOrReplaceProductCompatibility** call to identify a motor vehicle that is compatible with the inventory item. The user specifies either an eBay Product ID (ePID) or K-Type value to identify a vehicle, and if the motor vehicle is found in the eBay product catalog, the motor vehicle properties (make, model, year, trim, engine) will automatically be populated for the vehicle. If the vehicle cannot be found using these identifiers, the vehicle will not be added to the compatible vehicle list.  
  
Note that this container will not be returned in the **getProductCompatibility** call.

### CountryCodeEnum
**Description:** This enumerated type lists the two-letter [ISO 3166-1 Alpha-2](<https://www.iso.org/iso/country_codes >) code representing a country. | - **AD**: Andorra - **AE**: United Arab Emirates - **AF**: Afghanistan - **AG**: Antigua and Barbuda - **AI**: Anguilla - **AL**: Albania - **AM**: Armenia - **AN**: Netherlands Antilles - **AO**: Angola - **AQ**: Antarctica - **AR**: Argentina - **AS**: American Samoa - **AT**: Austria - **AU**: Australia - **AW**: Aruba - **AX**: Aland Islands - **AZ**: Azerbaijan - **BA**: Bosnia and Herzegovina - **BB**: Barbados - **BD**: Bangladesh - **BE**: Belgium - **BF**: Burkina Faso - **BG**: Bulgaria - **BH**: Bahrain - **BI**: Burundi - **BJ**: Benin - **BL**: Saint Barthelemy - **BM**: Bermuda - **BN**: Brunei Darussalam - **BO**: Bolivia - **BQ**: Bonaire, Sint Eustatius, and Saba - **BR**: Brazil - **BS**: Bahamas - **BT**: Bhutan - **BV**: Bouvet Island - **BW**: Botswana - **BY**: Belarus - **BZ**: Belize - **CA**: Canada - **CC**: Cocos (Keeling) Islands - **CD**: The Democratic Republic of the Congo - **CF**: Central African Republic - **CG**: Congo - **CH**: Switzerland - **CI**: Cote d'Ivoire - **CK**: Cook Islands - **CL**: Chile - **CM**: Cameroon - **CN**: China - **CO**: Colombia - **CR**: Costa Rica - **CU**: Cuba - **CV**: Cape Verde - **CW**: Curacao - **CX**: Christmas Island - **CY**: Cyprus - **CZ**: Czech Republic - **DE**: Germany - **DJ**: Djibouti - **DK**: Denmark - **DM**: Dominica - **DO**: Dominican Republic - **DZ**: Algeria - **EC**: Ecuador - **EE**: Estonia - **EG**: Egypt - **EH**: Western Sahara - **ER**: Eritrea - **ES**: Spain - **ET**: Ethiopia - **FI**: Finland - **FJ**: Fiji - **FK**: Falkland Islands (Malvinas) - **FM**: Federated States of Micronesia - **FO**: Faroe Islands - **FR**: France - **GA**: Gabon - **GB**: United Kingdom - **GD**: Grenada - **GE**: Georgia - **GF**: French Guiana - **GG**: Guernsey - **GH**: Ghana - **GI**: Gibraltar - **GL**: Greenland - **GM**: Gambia - **GN**: Guinea - **GP**: Guadeloupe - **GQ**: Equatorial Guinea - **GR**: Greece - **GS**: South Georgia and the South Sandwich Islands - **GT**: Guatemala - **GU**: Guam - **GW**: Guinea-Bissau - **GY**: Guyana - **HK**: Hong Kong - **HM**: Heard Island and McDonald Islands - **HN**: Honduras - **HR**: Croatia - **HT**: Haiti - **HU**: Hungary - **ID**: Indonesia - **IE**: Ireland - **IL**: Israel - **IM**: Isle of Man - **IN**: India - **IO**: British Indian Ocean Territory - **IQ**: Iraq - **IR**: Islamic Republic of Iran - **IS**: Iceland - **IT**: Italy - **JE**: Jersey - **JM**: Jamaica - **JO**: Jordan - **JP**: Japan - **KE**: Kenya - **KG**: Kyrgyzstan - **KH**: Cambodia - **KI**: Kiribati - **KM**: Comoros - **KN**: Saint Kitts and Nevis - **KP**: Democratic People's Republic of Korea - **KR**: Republic of Korea - **KW**: Kuwait - **KY**: Cayman Islands - **KZ**: Kazakhstan - **LA**: Lao People's Democratic Republic - **LB**: Lebanon - **LC**: Saint Lucia - **LI**: Liechtenstein - **LK**: Sri Lanka - **LR**: Liberia - **LS**: Lesotho - **LT**: Lithuania - **LU**: Luxembourg - **LV**: Latvia - **LY**: Libyan Arab Jamahiriya - **MA**: Morocco - **MC**: Monaco - **MD**: Republic of Moldova - **ME**: Montenegro - **MF**: Saint Martin (French part) - **MG**: Madagascar - **MH**: Marshall Islands - **MK**: The Former Yugoslav Republic of Macedonia - **ML**: Mali - **MM**: Myanmar - **MN**: Mongolia - **MO**: Macao - **MP**: Northern Mariana Islands - **MQ**: Martinique - **MR**: Mauritania - **MS**: Montserrat - **MT**: Malta - **MU**: Mauritius - **MV**: Maldives - **MW**: Malawi - **MX**: Mexico - **MY**: Malaysia - **MZ**: Mozambique - **NA**: Namibia - **NC**: New Caledonia - **NE**: Niger - **NF**: Norfolk Island - **NG**: Nigeria - **NI**: Nicaragua - **NL**: Netherlands - **NO**: Norway - **NP**: Nepal - **NR**: Nauru - **NU**: Niue - **NZ**: New Zealand - **OM**: Oman - **PA**: Panama - **PE**: Peru - **PF**: French Polynesia. Includes Tahiti - **PG**: Papua New Guinea - **PH**: Philippines - **PK**: Pakistan - **PL**: Poland - **PM**: Saint Pierre and Miquelon - **PN**: Pitcairn - **PR**: Puerto Rico - **PS**: Palestinian territory Occupied - **PT**: Portugal - **PW**: Palau - **PY**: Paraguay - **QA**: Qatar - **RE**: Reunion - **RO**: Romania - **RS**: Serbia - **RU**: Russian Federation - **RW**: Rwanda - **SA**: Saudi Arabia - **SB**: Solomon Islands - **SC**: Seychelles - **SD**: Sudan - **SE**: Sweden - **SG**: Singapore - **SH**: Saint Helena - **SI**: Slovenia - **SJ**: Svalbard and Jan Mayen - **SK**: Slovakia - **SL**: Sierra Leone - **SM**: San Marino - **SN**: Senegal - **SO**: Somalia - **SR**: Suriname - **ST**: Sao Tome and Principe - **SV**: El Salvador - **SX**: Sint Maarten (Dutch part) - **SY**: Syrian Arab Republic - **SZ**: Swaziland - **TC**: Turks and Caicos Islands - **TD**: Chad - **TF**: French Southern Territories - **TG**: Togo - **TH**: Thailand - **TJ**: Tajikistan - **TK**: Tokelau - **TL**: Timor-Leste - **TM**: Turkmenistan - **TN**: Tunisia - **TO**: Tonga - **TR**: Turkey - **TT**: Trinidad and Tobago - **TV**: Tuvalu - **TW**: Taiwan - **TZ**: Tanzania - **UA**: Ukraine - **UG**: Uganda - **UM**: United States Minor Outlying Islands - **US**: United States - **UY**: Uruguay - **UZ**: Uzbekistan - **VA**: Holy See (Vatican City state) - **VC**: Saint Vincent and the Grenadines - **VE**: Venezuela - **VG**: British Virgin Islands - **VI**: the U.S. Virgin Islands - **VN**: Vietnam - **VU**: Vanuatu - **WF**: Wallis and Futuna - **WS**: Samoa - **YE**: Yemen - **YT**: Mayotte - **ZA**: South Africa - **ZM**: Zambia - **ZW**: Zimbabwe
**Type:** object

### CountryPolicy
**Description:** This type specifies custom product compliance and/or take-back policies that apply to a specified country.
**Type:** object

**Properties:**
- **country** (CountryCodeEnum)
  - The two-letter [ISO 3166-1](<https://www.iso.org/iso-3166-country-codes.html >) country code identifying the country to which the policy or policies specified in the corresponding policyIds array will apply.
- **policyIds** (array)
  - An array of custom policy identifiers that apply to the country specified by [listingPolicies.regionalTakeBackPolicies.countryPolicies.country](/develop/api/sell/inventory_api#sell-inventory_api-offer-bulkcreateoffer.countrypolicy.country).  
  
Product compliance and take-back policy information may be returned using the following methods:

*   [getCustomPolicies](/develop/api/sell/account_api_v1#sell-account_api_v1-get-getcustompolicies)  
      
    Set `policy_types` to:
    
    *   `PRODUCT_COMPLIANCE` for product compliance policies
    *   `TAKE_BACK` for takeback policies
    
      
    This returns the list of specified policies and corresponding **customPolicyId** values a seller has created.
*   [getCustomPolicy](/develop/api/sell/account_api_v1#sell-account_api_v1-get-getcustompolicy) with `custom_policy_id = customPolicyId`  
      
    Returns the details of the policy specified by **customPolicyId**

For information about creating and managing custom policies, refer to the [custom\_policy](/api-docs/sell/account/resources/methods#h2-custom_policy) resource in the **Account API v1**.

### DayOfWeekEnum
**Description:** An enumerated type defining the days of the week. This type is used by the **weeklySchedule** container to specify cut-off hours for a fulfillment center. | - **MONDAY**: This enumeration value indicates that a fulfillment center has a cut-off time specified through the weeklySchedule.cutOffTime field on Monday. - **TUESDAY**: This enumeration value indicates that a fulfillment center has a cut-off time specified through the weeklySchedule.cutOffTime field on Tuesday. - **WEDNESDAY**: This enumeration value indicates that a fulfillment center has a cut-off time specified through the weeklySchedule.cutOffTime field on Wednesday. - **THURSDAY**: This enumeration value indicates that a fulfillment center has a cut-off time specified through the weeklySchedule.cutOffTime field on Thursday. - **FRIDAY**: This enumeration value indicates that a fulfillment center has a cut-off time specified through the weeklySchedule.cutOffTime field on Friday. - **SATURDAY**: This enumeration value indicates that a fulfillment center has a cut-off time specified through the weeklySchedule.cutOffTime field on Saturday. - **SUNDAY**: This enumeration value indicates that a fulfillment center has a cut-off time specified through the weeklySchedule.cutOffTime field on Sunday.
**Type:** object

### Document
**Description:** This type provides an array of one or more regulatory documents associated with a listing for Regulatory Compliance.
**Type:** object

**Properties:**
- **documentId** (string)
  - The unique identifier of a regulatory document associated with the listing.  
  
This value can be found in the response of the [createDocument](/develop/api/sell/media_api#sell-media_api-document-createdocument) method of the Media API.

### EbayOfferDetailsWithAll
**Description:** This type provides details of an offer, and is used by the response payloads of the **getOffer** and the **getOffers** calls.
**Type:** object

**Properties:**
- **availableQuantity** (integer)
  - This integer value indicates the quantity of the inventory item (specified by the **sku** value) that will be available for purchase by buyers shopping on the eBay site specified in the **marketplaceId** field.
- **categoryId** (string)
  - The unique identifier of the primary eBay category that the inventory item is listed under. This field is always returned for published offers, but is only returned if set for unpublished offers.
- **charity** (Charity)
  - This container is returned if a charitable organization will receive a percentage of sale proceeds for each sale generated by the listing. This container consists of the **charityId** field to identify the charitable organization, and the **donationPercentage** field that indicates the percentage of the sales proceeds that will be donated to the charitable organization.
- **extendedProducerResponsibility** (ExtendedProducerResponsibility)
  - This container is used to provide the eco-participation fee for a product. Use the [getExtendedProducerResponsibilityPolicies](/develop/api/sell/metadata_api#sell-metadata_api-marketplace-getextendedproducerresponsibilitypolicies) method of the **Sell Metadata API** to retrieve categories that support eco-participation fee for a specified marketplace.
- **format** (FormatTypeEnum)
  - This enumerated value indicates the listing format of the offer.
- **hideBuyerDetails** (boolean)
  - This field is returned as `true` if the private listing feature has been enabled for the offer. Sellers may want to use this feature when they believe that a listing's potential bidders/buyers would not want their obfuscated user IDs (and feedback scores) exposed to other users.  
  
This field is always returned even if not explicitly set in the offer. It defaults to `false`, so will get returned as `false` if seller does not set this feature with a 'Create' or 'Update' offer method.
- **includeCatalogProductDetails** (boolean)
  - This field indicates whether or not eBay product catalog details are applied to a listing. A value of `true` indicates the listing corresponds to the eBay product associated with the provided product identifier. The product identifier is provided in **createOrReplaceInventoryItem**.

**Note:** Though the **includeCatalogProductDetails** parameter is not required to be submitted in the request, the parameter defaults to 'true' if omitted.
- **listing** (ListingDetails)
  - For published offers, this container is always returned in the **getOffer** and **getOffers** calls, and includes the eBay listing ID associated with the offer, the status of the listing, and the quantity sold through the listing. The **listing** container is not returned at all for unpublished offers.
- **listingDescription** (string)
  - The description of the eBay listing that is part of the unpublished or published offer. This field is always returned for published offers, but is only returned if set for unpublished offers.  
  
**Maximum length**: 500,000 (which includes HTML markup/tags)
- **listingDuration** (ListingDurationEnum)
  - This field indicates the number of days that the listing will be active.  
  
This field is returned for both auction and fixed-price listings; however, the value returned for fixed-price listings will always be `GTC`. The GTC (Good 'Til Cancelled) listings are automatically renewed each calendar month until the seller decides to end the listing.  
  
**Note:** If the listing duration expires for an auction offer, the listing then becomes available as a fixed-price offer and will be GTC.
- **listingPolicies** (ListingPolicies)
  - This container indicates the listing policies that are applied to the offer. Listing policies include business policies, custom listing policies, and fields that override shipping costs, enable eBay Plus eligibility, or enable the Best Offer feature.  
  
It is required that the seller be opted into Business Policies before being able to create live eBay listings through the Inventory API. Sellers can opt-in to Business Policies through My eBay or by using the Account API v1's **optInToProgram** call. Payment, return, and fulfillment listing policies may be created/managed in My eBay or by using the listing policy calls of the sell **Account API v1**. The sell **Account API v1** can also be used to create and manage custom policies. For more information, see the sell [Account API v1](/develop/api/sell/account_api_v1).  
  
For unpublished offers where business policies have yet to be specified, this container will be returned as empty.
- **listingStartDate** (string)
  - This timestamp is the date/time (in UTC format) that the seller set for the scheduled listing. With the scheduled listing feature, the seller can set a time in the future that the listing will become active, instead of the listing becoming active immediately after a **publishOffer** call.  
  
For example: 2023-05-30T19:08:00Z.  
  
Scheduled listings do not always start at the exact date/time specified by the seller, but the date/time of the timestamp returned in **getOffer**/**getOffers** will be the same as the timestamp passed into a 'Create' or 'Update' offer call.  
  
This field is returned if set for an offer.
- **lotSize** (integer)
  - This field is only applicable and returned if the listing is a lot listing. A lot listing is a listing that has multiple quantity of the same product. An example would be a set of four identical car tires. The integer value in this field is the number of identical items being sold through the lot listing.
- **marketplaceId** (MarketplaceEnum)
  - This enumeration value is the unique identifier of the eBay site on which the offer is available, or will be made available.
- **merchantLocationKey** (string)
  - The unique identifier of the inventory location. This identifier is set up by the merchant when the inventory location is first created with the **createInventoryLocation** call. Once this value is set for an inventory location, it can not be modified. To get more information about this inventory location, the [getInventoryLocation](/develop/api/sell/inventory_api#sell-inventory_api-location-getinventorylocation) method can be used, passing in this value at the end of the call URI.  
  
This field is always returned for published offers, but is only returned if set for unpublished offers.  
  
**Maximum length**: 36
- **offerId** (string)
  - The unique identifier of the offer. This identifier is used in many offer-related calls, and it is also used in the **bulkUpdatePriceQuantity** call.
- **pricingSummary** (PricingSummary)
  - This container shows the listing price for the product offer, and if applicable, the settings for the Minimum Advertised Price and Strikethrough Pricing features. The Minimum Advertised Price feature is only available on the US site. Strikethrough Pricing is available on the US, eBay Motors, UK, Germany, Canada (English and French), France, Italy, and Spain sites.  
  
For unpublished offers where pricing information has yet to be specified, this container will be returned as empty.
- **quantityLimitPerBuyer** (integer)
  - This field is only applicable and set if the seller wishes to set a restriction on the purchase quantity of an inventory item per seller. If this field is set by the seller for the offer, then each distinct buyer may purchase up to, but not exceed the quantity in this field. So, if this field's value is `5`, each buyer may purchase a quantity of the inventory item between one and five, and the purchases can occur in one multiple-quantity purchase, or over multiple transactions. If a buyer attempts to purchase one or more of these products, and the cumulative quantity will take the buyer beyond the quantity limit, that buyer will be blocked from that purchase.
- **regulatory** (Regulatory)
  - This container is used by the seller to provide regulatory information.
- **secondaryCategoryId** (string)
  - The unique identifier for a secondary category. This field is applicable if the seller decides to list the item under two categories. Sellers can use the [getCategorySuggestions](/develop/api/sell/taxonomy_api#sell-taxonomy_api-category_tree-getcategorysuggestions) method of the Taxonomy API to retrieve suggested category ID values. A fee may be charged when adding a secondary category to a listing.  
  
**Note:** You cannot list **US eBay Motors** vehicles in two categories. However, you can list **Parts & Accessories** in two categories.
- **sku** (string)
  - This is the seller-defined SKU value of the product in the offer.  
  
**Maximum length**: 50
- **status** (OfferStatusEnum)
  - The enumeration value in this field specifies the status of the offer - either `PUBLISHED` or `UNPUBLISHED`.
- **storeCategoryNames** (array)
  - This container is returned if the seller chose to place the inventory item into one or two eBay store categories that the seller has set up for their eBay store. The string value(s) in this container will be the full path(s) to the eBay store categories, as shown below:  

"storeCategoryNames": \[  
 "/Fashion/Men/Shirts",   
 "/Fashion/Men/Accessories" \],
- **tax** (Tax)
  - This container is only returned if a sales tax table, a Value-Added Tax (VAT) rate, and/or a tax exception category code was applied to the offer. Only Business Sellers can apply VAT to their listings. It is possible that the **applyTax** field will be included with a value of `true`, but a buyer's purchase will not involve sales tax. A sales tax rate must be set up in the seller's sales tax table for the buyer's state/tax jurisdiction in order for that buyer to be subject to sales tax.  
  
See the [Using a tax table](<https://pages.ebay.com/help/pay/checkout-tax-table.html >) help page for more information on setting up and using a sales tax table.

### EbayOfferDetailsWithId
**Description:** updateOffer call. Every field that is currently set with the unpublished/published offer must also be passed into the **updateOffer** call, even those fields whose values are not changing. Note that for published offers, a successful **updateOffer** call will actually update the active eBay listing with whatever changes were made.
**Type:** object

**Properties:**
- **availableQuantity** (integer)
  - This integer value sets the quantity of the inventory item that will be available through the offer. Quantity must be set to `1` or more in order for the inventory item to be purchasable. This value should not be more than the quantity that is specified for the inventory item record. For auction listings, this field should not be provided.  
  
If this field exists for the current unpublished or published offer, it should be provided again in the **updateOffer** call, even if the value is not changing. If this particular field is omitted in an **updateOffer** call, the general available quantity set for the inventory item record may be used instead, and this may not be accurate if the inventory item is being sold across multiple marketplaces.
- **categoryId** (string)
  - The unique identifier of the eBay category that the inventory item is/will be listed under. This field is not immediately required for an unpublished offer, but will be required before publishing the offer. Sellers can use the [getCategorySuggestions](/develop/api/sell/taxonomy_api#sell-taxonomy_api-category_tree-getcategorysuggestions) method of the Taxonomy API to retrieve suggested category ID values. The seller passes in a query string like "_iPhone 6_", and category ID values for suggested categories are returned in the response.  
If this field exists for the current unpublished offer, it should be provided again in the **updateOffer** call, even if the eBay category is not changing. For a published offer (aka active eBay listing), this field must be provided or an error may occur. The eBay category of an active eBay listing cannot be changed once the listing has one or more sales, or if the listing is scheduled to end in less than 12 hours.  
  

**Important!**Publish offer note: This field is required before an offer can be published to create an active listing.
- **charity** (Charity)
  - This container is used if the seller wishes to update a published or unpublished offer with a charitable organization that will receive a percentage of sale proceeds for each sale generated by the eBay listing. This container consists of the **charityId** field to identify the charitable organization, and the **donationPercentage** field that indicates the percentage of the sales proceeds that will be donated to the charitable organization for each sale. Both fields in this container are conditionally required for charitable listings.
- **extendedProducerResponsibility** (ExtendedProducerResponsibility)
  - This container is used to provide the eco-participation fee for a product. Use the [getExtendedProducerResponsibilityPolicies](/develop/api/sell/metadata_api#sell-metadata_api-marketplace-getextendedproducerresponsibilitypolicies) method of the **Sell Metadata API** to retrieve categories that support eco-participation fee for a specified marketplace.
- **hideBuyerDetails** (boolean)
  - This field is included and set to `true` if the seller wishes to update a published or unpublished offer with the private listing feature. Alternatively, the seller could also remove the private listing feature (if already set for a published or unpublished offer) by including this field and setting it to `false`.  
  
Sellers may want to use this option when they believe that a listing's potential bidders/buyers would not want their obfuscated user IDs (and feedback scores) exposed to other users.
- **includeCatalogProductDetails** (boolean)
  - This field indicates whether or not eBay product catalog details are applied to a listing. A value of `true` indicates the listing corresponds to the eBay product associated with the provided product identifier. The product identifier is provided in **createOrReplaceInventoryItem**.

**Note:** Though the **includeCatalogProductDetails** parameter is not required to be submitted in the request, the parameter defaults to 'true' if omitted.
- **listingDescription** (string)
  - The text in this field is (published offers), or will become (unpublished offers) the description of the eBay listing. This field is not immediately required for an unpublished offer, but will be required before publishing the offer. Note that if the **listingDescription** field was omitted in the **createOffer** call for the offer, the offer entity should have picked up the text provided in the **product.description** field of the inventory item record, or if the inventory item is part of a group, the offer entity should have picked up the text provided in the **description** field of the inventory item group record.  
  
HTML tags and markup can be used in listing descriptions, but each character counts toward the Maximum length limit.  
  
**Note:** To ensure that their short listing description is optimized when viewed on mobile devices, sellers should strongly consider using eBay's [View Item description summary feature](<https://pages.ebay.com/sell/itemdescription/customizeyoursummary.html >) when listing their items. Keep in mind that the 'short' listing description is what prospective buyers first see when they view the listing on a mobile device. The 'full' listing description is also available to mobile users when they click on the short listing description, but the full description is not automatically optimized for viewing in mobile devices, and many users won't even drill down to the full description.  
  
Using HTML div and span tag attributes, this feature allows sellers to customize and fully control the short listing description that is displayed to prospective buyers when viewing the listing on a mobile device. The short listing description on mobile devices is limited to 800 characters, and whenever the full listing description (provided in this field, in UI, or seller tool) exceeds this limit, eBay uses a special algorithm to derive the best possible short listing description within the 800-character limit. However, due to some short listing description content being removed, it is definitely not ideal for the seller, and could lead to a bad buyer experience and possibly to a Significantly not as described (SNAD) case, since the buyer may not get complete details on the item when viewing the short listing description. See the eBay help page for more details on using the HTML div and span tags.  
  
If this field exists for the current unpublished offer, it should be provided again in the **updateOffer** call, even if the text is not changing. For a published offer (aka active eBay listing), this field must be provided or an error may occur.  
  
**Maximum length**: 500,000 (which includes HTML markup/tags)
- **listingDuration** (ListingDurationEnum)
  - This field indicates the number of days that the listing will be active. For fixed-price listings, this value must be set to `GTC`, but auction listings support different listing durations.  
  
The GTC (Good 'Til Cancelled) listings are automatically renewed each calendar month until the seller decides to end the listing.  
  
**Note:** If the listing duration expires for an auction offer without a winning bidder, the listing then becomes available as a fixed-price offer and listing duration will be `GTC`.  

**Important!**Publish offer note: This field is required before an offer can be published to create an active listing.
- **listingPolicies** (ListingPolicies)
  - This container sets listing policies that will be used to construct the listing. Listing policies include business policies, custom listing policies, and fields that override shipping costs, enable eBay Plus eligibility, or enable the Best Offer feature. This container is not initially required when creating an offer but will become required before the offer can be published. Busines policies (payment, return, fulfillment policies) will always be required before publishing an offer. Other policies, including the seller created compliance policies and seller created take-back policy, will be required as needed by the marketplace, category, or product.  
  
This container is required for updating published offers, regardless of whether or not the business policies are being changed. For an unpublished offer, this field is not necessarily required, but will be required before an offer can be published.  
  
It is required that the seller be opted in to Business Policies before being able to create live eBay listings through the Inventory API. Sellers can opt-in to Business Policies through My eBay or by using the Account API v1's **optInToProgram** call. Similarly, payment, return, and fulfillment business policies may be created/managed in My eBay or by using the business policy calls of the **Account API v1**.  
  

**Important!**Publish offer note: This container and a few of its child fields (as noted below) are required before an offer can be published to create an active listing.
- **listingStartDate** (string)
  - This field can be used with an unpublished offer if the seller wants to specify a time in the future that the listing will become active on eBay. The timestamp supplied in this field should be in UTC format, and it should be far enough in the future so that the seller will have enough time to publish the listing with the **publishOffer** method.  
  
For example: 2023-05-30T19:08:00Z.  
  
This field is optional, and it doesn't apply to offers where the corresponding listing is already active. If this field is not provided, the listing starts immediately after a successful **publishOffer** method.
- **lotSize** (integer)
  - This field is only applicable if the listing is a lot listing. A lot listing is a listing that has multiple quantity of the same item, such as four identical tires being sold as a single offer, or it can be a mixed lot of similar items, such as used clothing items or an assortment of baseball cards. Whether the lot listing involved identical items or a mixed lot, the integer value passed into this field is the total number of items in the lot. Lots can be used for auction and fixed-price listings.
- **merchantLocationKey** (string)
  - The unique identifier of a merchant's inventory location (where the inventory item in the offer is located).  
  
To get more information about inventory locations, the [getInventoryLocations](/develop/api/sell/inventory_api#sell-inventory_api-location-getinventorylocations) method can be used.br>  
**Note:** This field is not initially required upon first creating an offer, but will become required before an offer can be published.  
**Maximum length**: 36
- **pricingSummary** (PricingSummary)
  - This container shows the listing price for the product offer, and if applicable, the settings for the Minimum Advertised Price and Strikethrough Pricing features. The Minimum Advertised Price feature is only available on the US site. Strikethrough Pricing is available on the US, eBay Motors, UK, Germany, Canada (English and French), France, Italy, and Spain sites.  
  
This container is required for updating published offers, regardless of whether or not the pricing information is being changed or not. For an unpublished offer, this container is not necessarily required, but an offer price will be required before an offer can be published, and if a **pricingSummary** container already exists for an unpublished offer, it must be provided again, even if the values are not changing.  
  

**Important!**Publish offer note: This container and its child container, **price**, are required before an offer can be published to create an active listing.
- **quantityLimitPerBuyer** (integer)
  - This field is only applicable and set if the seller wishes to set a restriction on the purchase quantity per seller. If this field is set by the seller for the offer, then each distinct buyer may purchase up to, but not exceeding the quantity specified for this field. So, if this field's value is `5`, each buyer may purchase between one to five of these products, and the purchases can occur in one multiple-quantity purchase, or over multiple transactions. If a buyer attempts to purchase one or more of these products, and the cumulative quantity will take the buyer beyond the quantity limit, that buyer will be blocked from that purchase.  
  
If this field currently exists for an unpublished or published offer, it should be provided again in an **updateOffer** call, even if the value is not changing.
- **regulatory** (Regulatory)
  - This container is used by the seller to provide regulatory information.
- **secondaryCategoryId** (string)
  - The unique identifier for a secondary category. This field is applicable if the seller decides to list the item under two categories. Sellers can use the [getCategorySuggestions](/develop/api/sell/taxonomy_api#sell-taxonomy_api-category_tree-getcategorysuggestions) method of the Taxonomy API to retrieve suggested category ID values. A fee may be charged when adding a secondary category to a listing.  
  
**Note:** You cannot list **US eBay Motors** vehicles in two categories. However, you can list **Parts & Accessories** in two categories.
- **storeCategoryNames** (array)
  - This container is used if the seller would like to place the inventory item into one or two store categories that the seller has set up for their eBay store. The string value(s) passed in to this container will be the full path(s) to the store categories, as shown below:  

"storeCategoryNames": \[  
 "/Fashion/Men/Shirts",   
 "/Fashion/Men/Accessories" \], 

If this field currently exists for an unpublished or published offer, it should be provided again in an **updateOffer** call, even if the eBay categories are not changing.
- **tax** (Tax)
  - This container is only applicable and used if a sales tax table, a Value-Added Tax (VAT) rate, or a tax exception category code will be applied to the offer. Only Business Sellers can apply VAT to their listings. It is possible that the **applyTax** field will be included with a value of `true`, but a buyer's purchase will not involve sales tax. A sales tax rate must be set up in the seller's sales tax table for the buyer's state/tax jurisdiction in order for that buyer to be subject to sales tax. Sales tax rates for different jurisdictions can be added/modified in the Payment Preferences section of My eBay, or the seller can use the sales tax calls of the **Account API v1**.  
  
If tax information currently exists for an unpublished or published offer, it should be provided again in an **updateOffer** call, even if none of the tax settings are changing.  
  
See the [Using a tax table](<https://pages.ebay.com/help/pay/checkout-tax-table.html >) help page for more information on setting up and using a sales tax table.

### EbayOfferDetailsWithKeys
**Description:** This type provides details of an offer, and is used by the base request payload of the **createOffer** and **bulkCreateOffer** methods.
**Type:** object

**Properties:**
- **availableQuantity** (integer)
  - This integer value sets the quantity of the inventory item (specified by the **sku** value) that will be available for purchase by buyers shopping on the eBay site specified in the **marketplaceId** field. Quantity must be set to `1` or more in order for the inventory item to be purchasable, but this field is not necessarily required, even for published offers, if the general quantity of the inventory item has already been set in the inventory item record.  
  
For auction listings, this field should not be provided.  
  
**Note:** The **availableQuantity** field if set here overrides the **quantity** field set in the inventory item. See the note in [Offer fields](/api-docs/sell/static/inventory/publishing-offers.html#offer) for details.
- **categoryId** (string)
  - The unique identifier of the eBay category that the product will be listed under. This field is not immediately required upon creating an offer, but will be required before publishing the offer.  
  
Sellers can use the [getCategorySuggestions](/develop/api/sell/taxonomy_api#sell-taxonomy_api-category_tree-getcategorysuggestions) method of the Taxonomy API to retrieve suggested category ID values. The seller passes in a query string like "_iPhone 6_", and category ID values for suggested categories are returned in the response.  
  

**Important!**Publish offer note: This field is required before an offer can be published to create an active listing.

**Note:** When listing in categoryID 173651 (Auto Performance Tuning Devices & Software), use of catalog products is required. For more information, see [Tuning devices and software](/api-docs/sell/static/inventory/tuning-devices-and-software-rest.html).
- **charity** (Charity)
  - This container is used if the seller wishes to select a charitable organization that will receive a percentage of sale proceeds for each sale generated by the eBay listing. This container consists of the **charityId** field to identify the charitable organization, and the **donationPercentage** field that indicates the percentage of the sales proceeds that will be donated to the charitable organization for each sale. Both fields in this container are conditionally required for charitable listings.
- **extendedProducerResponsibility** (ExtendedProducerResponsibility)
  - This container is used to provide the eco-participation fee for a product.  
  
Use the [getExtendedProducerResponsibilityPolicies](develop/api/sell/metadata_api#sell-metadata_api-marketplace-getextendedproducerresponsibilitypolicies) method of the **Sell Metadata API** to retrieve categories that support eco-participation fee for a specified marketplace.
- **format** (FormatTypeEnum)
  - This enumerated value indicates the listing format of the offer.  
  
Supported values are `FIXED_PRICE` and `AUCTION`.
- **hideBuyerDetails** (boolean)
  - This field is included and set to `true` if the seller wishes to create a private listing.  
  
Sellers may want to use this option when they believe that a listing's potential bidders/buyers would not want their obfuscated user IDs (and feedback scores) exposed to other users.
- **includeCatalogProductDetails** (boolean)
  - This field indicates whether or not eBay product catalog details are applied to a listing. A value of `true` indicates the listing corresponds to the eBay product associated with the provided product identifier. The product identifier is provided in [createOrReplaceInventoryItem](/develop/api/sell/inventory_api#sell-inventory_api-inventory_item-createorreplaceinventoryitem).  
  
**Default:** true

**Note:** Though the **includeCatalogProductDetails** parameter is not required to be submitted in the request, the parameter defaults to `true` if omitted.
- **listingDescription** (string)
  - The text in this field is (published offers), or will become (unpublished offers) the description of the eBay listing. This field is not immediately required for an unpublished offer, but will be required before publishing the offer. Note that if the **listingDescription** field was omitted in the **createOffer** call for the offer, the offer entity should have picked up the text provided in the **product.description** field of the inventory item record, or if the inventory item is part of a group, the offer entity should have picked up the text provided in the **description** field of the inventory item group record.  
  
HTML tags and markup can be used in listing descriptions, but each character counts toward the maximum length limit.  
  
**Note:** To ensure that their short listing description is optimized when viewed on mobile devices, sellers should strongly consider using eBay's [View Item description summary feature](<https://pages.ebay.com/sell/itemdescription/customizeyoursummary.html >) when listing their items. Keep in mind that the 'short' listing description is what prospective buyers first see when they view the listing on a mobile device. The 'full' listing description is also available to mobile users when they click on the short listing description, but the full description is not automatically optimized for viewing in mobile devices, and many users won't even drill down to the full description.  
  
Using HTML div and span tag attributes, this feature allows sellers to customize and fully control the short listing description that is displayed to prospective buyers when viewing the listing on a mobile device. The short listing description on mobile devices is limited to 800 characters, and whenever the full listing description (provided in this field, in UI, or seller tool) exceeds this limit, eBay uses a special algorithm to derive the best possible short listing description within the 800-character limit. However, due to some short listing description content being removed, it is definitely not ideal for the seller, and could lead to a bad buyer experience and possibly to a Significantly not as described (SNAD) case, since the buyer may not get complete details on the item when viewing the short listing description. See the eBay help page for more details on using the HTML div and span tags.  
  
**Maximum length**: 500,000 (which includes HTML markup/tags)
- **listingDuration** (ListingDurationEnum)
  - This field indicates the number of days that the listing will be active. For fixed-price listings, this value must be set to `GTC`, but auction listings support different listing durations.  
  
The GTC (Good 'Til Cancelled) listings are automatically renewed each calendar month until the seller decides to end the listing.  
  
**Note:** If the listing duration expires for an auction offer without a winning bidder, the listing then becomes available as a fixed-price offer and listing duration will be `GTC`.  

**Important!**Publish offer note: This field is required before an offer can be published to create an active listing.
- **listingPolicies** (ListingPolicies)
  - This container sets listing policies that will be used to construct the listing. Listing policies include business policies, custom listing policies, and fields that override shipping costs, enable eBay Plus eligibility, or enable the Best Offer feature. This container is not initially required when creating an offer but will become required before the offer can be published. Busines policies (payment, return, fulfillment policies) will always be required before publishing an offer. Other policies, including the seller created compliance policies and seller created take-back policy, will be required as needed by the marketplace, category, or product.  
  
It is required that the seller be opted into Business Policies before being able to create live eBay listings through the Inventory API. Sellers can opt-in to Business Policies through My eBay or by using the Account API v1's **optInToProgram** call. Payment, return, and fulfillment listing policies may be created/managed in My eBay or by using the listing policy calls of the sell **Account API v1**. The sell **Account API v1** can also be used to create and manage custom policies. For more information, see the sell [Account API v1](/develop/api/sell/account_api_v1).  
  

**Important!**Publish offer note: This container and a few of its child fields (as noted below) are required before an offer can be published to create an active listing.
- **listingStartDate** (string)
  - This field can be used if the seller wants to specify a time in the future that the listing will become active on eBay. The timestamp supplied in this field should be in UTC format, and it should be far enough in the future so that the seller will have enough time to publish the listing with the **publishOffer** method.  
  
For example: 2023-05-30T19:08:00Z.  
  
This field is optional. If this field is not provided, the listing starts immediately after a successful **publishOffer** method.
- **lotSize** (integer)
  - This field is only applicable if the listing is a lot listing. A lot listing is a listing that has multiple quantity of the same item, such as four identical tires being sold as a single offer, or it can be a mixed lot of similar items, such as used clothing items or an assortment of baseball cards. Whether the lot listing involved identical items or a mixed lot, the integer value passed into this field is the total number of items in the lot. Lots can be used for auction and fixed-price listings.
- **marketplaceId** (MarketplaceEnum)
  - This enumeration value is the unique identifier of the eBay site for which the offer will be made available. See **MarketplaceEnum** for the list of supported enumeration values. This field is required.
- **merchantLocationKey** (string)
  - The unique identifier of a merchant's inventory location (where the inventory item in the offer is located).  
  
To get more information about inventory locations, the [getInventoryLocations](/develop/api/sell/inventory_api#sell-inventory_api-location-getinventorylocations) method can be used.  
  
**Note:** This field is not initially required upon first creating an offer, but will become required before an offer can be published.  

**Important!**Publish offer note: This field is required before an offer can be published to create an active listing.

  
**Maximum length**: 36
- **pricingSummary** (PricingSummary)
  - This container shows the listing price for the product offer, and if applicable, the settings for the Minimum Advertised Price and Strikethrough Pricing features. The Minimum Advertised Price feature is only available on the US site. Strikethrough Pricing is available on the US, eBay Motors, UK, Germany, Canada (English and French), France, Italy, and Spain sites.  
  
This container is not initially required upon first creating an offer, but the price of the offer will become required before an offer can be published.  
  

**Important!**Publish offer note: This container and its child container, **price**, are required before an offer can be published to create an active listing.
- **quantityLimitPerBuyer** (integer)
  - This field is only applicable and set if the seller wishes to set a restriction on the purchase quantity per seller. If this field is set by the seller for the offer, then each distinct buyer may purchase up to, but not exceed the quantity specified for this field. So, if this field's value is `5`, each buyer may purchase between one to five of these products, and the purchases can occur in one multiple-quantity purchase, or over multiple transactions. If a buyer attempts to purchase one or more of these products, and the cumulative quantity will take the buyer beyond the quantity limit, that buyer will be blocked from that purchase.
- **regulatory** (Regulatory)
  - This container is used by the seller to provide regulatory information.
- **secondaryCategoryId** (string)
  - The unique identifier for a secondary category. This field is applicable if the seller decides to list the item under two categories. Sellers can use the [getCategorySuggestions](/develop/api/sell/taxonomy_api#sell-taxonomy_api-category_tree-getcategorysuggestions) method of the Taxonomy API to retrieve suggested category ID values. A fee may be charged when adding a secondary category to a listing.  
  
**Note:** You cannot list **US eBay Motors** vehicles in two categories. However, you can list **Parts & Accessories** in two categories.

**Note:** When listing in categoryID 173651 (Auto Performance Tuning Devices & Software), use of catalog products is required. For more information, see [Tuning devices and software](/api-docs/sell/static/inventory/tuning-devices-and-software-rest.html).
- **sku** (string)
  - The seller-defined SKU value of the product that will be listed on the eBay site (specified in the **marketplaceId** field). Only one offer (in unpublished or published state) may exist for each **sku**/**marketplaceId**/**format** combination. This field is required.  
  
Use the [getInventoryItems](/develop/api/sell/inventory_api#sell-inventory_api-inventory_item-getinventoryitems) method to retrieve SKU values.  
  
**Maximum length**: 50
- **storeCategoryNames** (array)
  - This container is used if the seller would like to place the inventory item into one or two eBay store categories that the seller has set up for their eBay store. The string value(s) passed in to this container will be the full path(s) to the eBay store categories, as shown below:  

"storeCategoryNames": \[  
 "/Fashion/Men/Shirts",   
 "/Fashion/Men/Accessories" \],
- **tax** (Tax)
  - This container is applicable and used only if a sales-tax table, a Value-Added Tax (VAT) rate, or a tax exception category code will be applied to the offer. Only Business Sellers can apply VAT to their listings. It is possible that the **applyTax** field will be included with a value of `true`, but a buyer's purchase will not involve sales tax.  
  
A sales-tax rate must be set up in the seller's sales-tax table for the buyer's state/tax jurisdiction in order for that buyer to be subject to sales tax. Sales-tax rates for different jurisdictions can be added/modified in the Payment Preferences section of My eBay, or the seller can use the sales tax calls of the **Account API v1**.  
  
**Note:** Sales-tax tables are available only for the US and Canada marketplaces.  
Refer to [Taxes and import charges](<https://www.ebay.com/help/selling/fees-credits-invoices/taxes-import-charges?id=4121 >) for more information on setting up and using a sales tax table.

### EnergyEfficiencyLabel
**Description:** This type provides information about the energy efficiency for certain durable goods.  
  

**Important!** When providing energy efficiency information on an appliance or smartphones and tablets listing, the energy efficiency **rating** and **range** of the item must be specified through the the [aspects](/develop/api/sell/inventory_api#sell-inventory_api-inventory_item-bulkcreateorreplaceinventoryitem.product.aspects) field when creating the inventory item record. Use the [getItemAspectsForCategory](/develop/api/sell/taxonomy_api#sell-taxonomy_api-category_tree-getitemaspectsforcategory) method of the Taxonomy API to retrieve applicable rating and range values for a specified category.
**Type:** object

**Properties:**
- **imageDescription** (string)
  - A brief verbal summary of the information included on the Energy Efficiency Label for an item.  
  
For example, _On a scale of A to G the rating is E._
- **imageURL** (string)
  - The URL to the Energy Efficiency Label image that is applicable to an item.
- **productInformationSheet** (string)
  - The URL to the Product Information Sheet that provides complete manufacturer-provided efficiency information about an item.

### ExtendedProducerResponsibility
**Description:** This type provides IDs for the producer or importer related to the new item, packaging, added documentation, or an eco-participation fee. In some markets, such as in France, this may be the importer of the item.
**Type:** object

**Properties:**
- **ecoParticipationFee** (Amount)
  - This is the fee paid for new items to the eco-organization (for example, "eco-organisme" in France). It is a contribution to the financing of the elimination of the item responsibly.  
  
**Note:** `0` should not be used as a default value.  
**Minimum:** 0.0
- **producerProductId** (string)
  - **Note:** **THIS FIELD IS DEPRECATED AND NO LONGER SUPPORTED.** For sellers selling on the eBay France Marketplace, Extended Producer Responsibility ID fields are no longer set at the listing level. Instead, sellers must provide these IDs for each applicable category in their My eBay accounts. The URL will be based on the seller's home/registration site, and will use this pattern: https://accountsettings./epr-fr. Sellers based in the US will use [https://accountsettings.ebay.com/epr-fr](https://accountsettings.ebay.com/epr-fr), sellers based in France will use [https://accountsettings.ebay.fr/epr-fr](https://accountsettings.ebay.fr/epr-fr), and so on.
- **productDocumentationId** (string)
  - **Note:** **THIS FIELD IS DEPRECATED AND NO LONGER SUPPORTED.** For sellers selling on the eBay France Marketplace, Extended Producer Responsibility ID fields are no longer set at the listing level. Instead, sellers must provide these IDs for each applicable category in their My eBay accounts. The URL will be based on the seller's home/registration site, and will use this pattern: https://accountsettings./epr-fr. Sellers based in the US will use [https://accountsettings.ebay.com/epr-fr](https://accountsettings.ebay.com/epr-fr), sellers based in France will use [https://accountsettings.ebay.fr/epr-fr](https://accountsettings.ebay.fr/epr-fr), and so on.
- **productPackageId** (string)
  - **Note:** **THIS FIELD IS DEPRECATED AND NO LONGER SUPPORTED.** For sellers selling on the eBay France Marketplace, Extended Producer Responsibility ID fields are no longer set at the listing level. Instead, sellers must provide these IDs for each applicable category in their My eBay accounts. The URL will be based on the seller's home/registration site, and will use this pattern: https://accountsettings./epr-fr. Sellers based in the US will use [https://accountsettings.ebay.com/epr-fr](https://accountsettings.ebay.com/epr-fr), sellers based in France will use [https://accountsettings.ebay.fr/epr-fr](https://accountsettings.ebay.fr/epr-fr), and so on.
- **shipmentPackageId** (string)
  - **Note:** **THIS FIELD IS DEPRECATED AND NO LONGER SUPPORTED.** For sellers selling on the eBay France Marketplace, Extended Producer Responsibility ID fields are no longer set at the listing level. Instead, sellers must provide these IDs for each applicable category in their My eBay accounts. The URL will be based on the seller's home/registration site, and will use this pattern: https://accountsettings./epr-fr. Sellers based in the US will use [https://accountsettings.ebay.com/epr-fr](https://accountsettings.ebay.com/epr-fr), sellers based in France will use [https://accountsettings.ebay.fr/epr-fr](https://accountsettings.ebay.fr/epr-fr), and so on.

### Fee
**Description:** This type is used to express expected listing fees that the seller may incur for one or more unpublished offers, as well as any eBay-related promotional discounts being applied toward a specific fee. These fees are the expected cumulative fees per eBay marketplace (which is indicated in the **marketplaceId** field).
**Type:** object

**Properties:**
- **amount** (Amount)
  - This dollar value in this container is the actual dollar value of the listing fee type specified in the **feeType** field.
- **feeType** (string)
  - The value returned in this field indicates the type of listing fee that the seller may incur if one or more unpublished offers (offers are specified in the call request) are published on the marketplace specified in the **marketplaceId** field. Applicable listing fees will often include things such as `InsertionFee` or `SubtitleFee`, but many fee types will get returned even when they are `0.0`.  
  
See the [Standard selling fees](<https://pages.ebay.com/help/sell/fees.html >) help page for more information on listing fees.
- **promotionalDiscount** (Amount)
  - The dollar value in this container indicates any eBay promotional discount applied toward the listing fee type specified in the **feeType** field. If there was no discount applied toward the fee, this container is still returned but its value is `0.0`.

### FeeSummary
**Description:** This type is used to display the expected listing fees for each unpublished offer specified in the request of the **getListingFees** call.
**Type:** object

**Properties:**
- **fees** (array)
  - This container is an array of listing fees that can be expected to be applied to an offer on the specified eBay marketplace (**marketplaceId** value). Many fee types will get returned even when they are `0.0`.  
  
See the [Standard selling fees](<https://pages.ebay.com/help/sell/fees.html >) help page for more information on listing fees.
- **marketplaceId** (MarketplaceEnum)
  - This is the unique identifier of the eBay site for which listing fees for the offer are applicable.
- **warnings** (array)
  - This container will contain an array of errors and/or warnings when a call is made, and errors and/or warnings occur.

### FeesSummaryResponse
**Description:** This type is used by the base response payload for the **getListingFees** call.
**Type:** object

**Properties:**
- **feeSummaries** (array)
  - This container consists of an array of one or more listing fees that the seller can expect to pay for unpublished offers specified in the call request. Many fee types will get returned even when they are `0.0`.

### FormatTypeEnum
**Description:** This enumeration type is used to indicate the listing format of the offer.  
  
**Note:** When creating an _auction_ offer, one of the available quantities for the inventory item are reserved for the auction offer. If the offer ends without a bid, the allocated quantity will be released and available for fixed-price offers. | - **AUCTION**: This enumeration value indicates that the listing format of the offer is auction. - **FIXED_PRICE**: This enumeration value indicates that the listing format of the offer is fixed-price.
**Type:** object

### FulfillmentCenterSpecifications
**Description:** This type is used to provide shipping specification details, such as the weekly cut-off schedule for order handling and cut-off override(s), for a fulfillment center location.
**Type:** object

**Properties:**
- **sameDayShippingCutOffTimes** (SameDayShippingCutOffTimes)
  - **Note:** This container only applies to listings with same-day handling.  
This container specifies cut-off time(s) for order handling (and optionally cut-off overrides) at a fulfillment center location.  
  
For example, if the cut-off time for order handling is `14:00`, any orders made after this time will be handled on the next available business day.  
  
**Note:** Shipping cut-off times must be specified if one of the **locationTypes** of the inventory location is `FULFILLMENT_CENTER`.

### GeoCoordinates
**Description:** This type is used to express the Global Positioning System (GPS) latitude and longitude coordinates of an inventory location.
**Type:** object

**Properties:**
- **latitude** (number)
  - The latitude (North-South) component of the geographic coordinate. This field is required if a **geoCoordinates** container is used.  
  
This field is returned if geographical coordinates are set for the location.  
  
**Example:** `33.089805`
- **longitude** (number)
  - The longitude (East-West) component of the geographic coordinate. This field is required if a **geoCoordinates** container is used.  
  
This field is returned if geographical coordinates are set for the location.  
  
**Example:** `-88.709822`

### Hazmat
**Description:** This container is used by the seller to provide hazardous material information for the listing.  
  
The **statements** element is required to complete the hazmat section of a listing.  
  
The following elements are optional:

*   **pictograms**
*   **signalWord**
*   **component**
**Type:** object

**Properties:**
- **component** (string)
  - This field is used by the seller to provide component information for the listing. For example, component information can provide the specific material of Hazmat concern.  
  
**Maximum length:** 120
- **pictograms** (array)
  - An array of comma-separated string values listing applicable pictogram code(s) for Hazard Pictogram(s).  
  
If your product contains hazardous substances or mixtures, please select the values corresponding to the hazard pictograms that are stated on your product's Safety Data Sheet. The selected hazard information will be displayed on your listing.  
  
**Note:** Use the [getHazardousMaterialsLabels](/develop/api/sell/metadata_api#sell-metadata_api-marketplace-gethazardousmaterialslabels) method in the Metadata API to find supported values for a specific marketplace/site. Refer to [Pictogram sample values](/api-docs/sell/static/metadata/feature-regulatorhazmatcontainer.html#Pictogra) for additional information.
- **signalWord** (string)
  - This field sets the signal word for hazardous materials in the listing.  
  
If your product contains hazardous substances or mixtures, please select a value corresponding to the signal word that is stated on your product's Safety Data Sheet. The selected hazard information will be displayed on your listing.  
  
**Note:** Use the [getHazardousMaterialsLabels](/develop/api/sell/metadata_api#sell-metadata_api-marketplace-gethazardousmaterialslabels) method in the [Metadata API](/develop/api/sell/metadata_api) to find supported values for a specific marketplace/site. Refer to [Signal word information](/api-docs/sell/static/metadata/feature-regulatorhazmatcontainer.html#Signal) for additional information.
- **statements** (array)
  - An array of comma-separated string values specifying applicable statement code(s) for hazard statement(s) for the listing.  
  
If your product contains hazardous substances or mixtures, please select the values corresponding to the hazard statements that are stated on your product's Safety Data Sheet. The selected hazard information will be displayed on your listing.  
  
**Note:** Use the [getHazardousMaterialsLabels](/develop/api/sell/metadata_api#sell-metadata_api-marketplace-gethazardousmaterialslabels) method in the Metadata API to find supported values for a specific marketplace/site. Refer to [Hazard statement sample values](/api-docs/sell/static/metadata/feature-regulatorhazmatcontainer.html#Hazard) for additional information.  
This field is required if hazardous material information is provided for the listing.

### Interval
**Description:** **Deprecated.** Do not use as STORE location types are no longer supported.
**Type:** object

**Properties:**
- **close** (string)
  - The **close** value is actually the time that the store location closes. Local time (in Military format) is used. So, if a store closed at 8 PM local time, the **close** time would look like the following: `20:00:00`. This field is conditionally required if the **intervals** container is used to specify working hours or special hours for a store.  
  
This field is returned if set for the store location.
- **open** (string)
  - The **open** value is actually the time that the store opens. Local time (in Military format) is used. So, if a store opens at 9 AM local time, the **open** time would look like the following: `09:00:00`. This field is conditionally required if the **intervals** container is used to specify working hours or special hours for a store.  
  
This field is returned if set for the store location.

### InventoryItemGroup
**Description:** This type is used by the base request payload of the **createOrReplaceInventoryItemGroup** call and the base response payload of the **getInventoryItemGroup** call.
**Type:** object

**Properties:**
- **aspects** (string)
  - This is a collection of item specifics (aka product aspects) name-value pairs that are shared by all product variations within the inventory item group. Common aspects for the inventory item group are not immediately required upon creating an inventory item group, but these aspects will be required before the first offer of the group is published. Common aspects for a men's t-shirt might be pattern and sleeve length.  
  

**Important!** Effective from December 28th, 2024, sellers offering certain rechargeable devices in EU and Northern Ireland markets must comply with the Common Charger Directive (CCD) and list appropriate charger-related aspects and values on their listings. See [Common Charger Directive](/api-docs/sell/static/inventory/common-charger-directive.html) for more information.

  
Below is an example of the proper JSON syntax to use when manually inputting item specifics. Note that one item specific name, such as 'Features', can have more than one value. If an item specific name has more than one value, each value is delimited with a comma.  

"aspects": {  
 "pattern": \["solid"\],  
 "sleeves": \["short"\]  
 }

This container is always returned if one or more offers associated with the inventory item group have been published, and is only returned if set for an inventory item group if that group has yet to have any offers published.  
  

**Important!**Publish offer note: This field is required before an offer can be published to create an active listing.
- **description** (string)
  - The description of the inventory item group. This description should fully describe the product and the variations of the product that are available in the inventory item group, since this description will ultimately become the listing description once the first offer of the group is published. This field is not initially required when first creating an inventory item group, but will be required before the first offer of the group is published.  
  
**Note:** Since this description will ultimately become the listing description in a multiple-variation listing, the seller should omit the **listingDescription** field when creating the offers for each variation. If they include the **listingDescription** field for the individual offer(s) in an item group, the text in that field for a published offer will overwrite the text provided in this **description** field for the inventory item group.  
  
HTML tags and markup can be used in this field, but each character counts toward the maximum length limit.  
  
**Note:** To ensure that their short listing description is optimized when viewed on mobile devices, sellers should strongly consider using eBay's [View Item description summary feature](<https://pages.ebay.com/sell/itemdescription/customizeyoursummary.html >) when listing their items. Keep in mind that the 'short' listing description is what prospective buyers first see when they view the listing on a mobile device. The 'full' listing description is also available to mobile users when they click on the short listing description, but the full description is not automatically optimized for viewing in mobile devices, and many users won't even drill down to the full description.  
  
Using HTML div and span tag attributes, this feature allows sellers to customize and fully control the short listing description that is displayed to prospective buyers when viewing the listing on a mobile device. The short listing description on mobile devices is limited to 800 characters, and whenever the full listing description (provided in this field, in UI, or seller tool) exceeds this limit, eBay uses a special algorithm to derive the best possible short listing description within the 800-character limit. However, due to some short listing description content being removed, it is definitely not ideal for the seller, and could lead to a bad buyer experience and possibly to a Significantly not as described (SNAD) case, since the buyer may not get complete details on the item when viewing the short listing description. See the eBay help page for more details on using the HTML div and span tags.  
  
This field is always returned if one or more offers associated with the inventory item group have been published, and is only returned if set for an inventory item group if that group has yet to have any offers published.  
  

**Important!**Publish offer note: This field is required before an offer can be published to create an active listing.

  
**Maximum length**: 500,000 (which includes HTML markup/tags)
- **imageUrls** (array)
  - An array of one or more links to images for the inventory item group. URLs must use the "HTTPS" protocol. Images can be self-hosted by the seller, or sellers can use the [UploadSiteHostedPictures](</Devzone/XML/docs/Reference/eBay/UploadSiteHostedPictures.html >) call of the Trading API to upload images to an eBay Picture Server. If successful, the response of the [UploadSiteHostedPictures](</Devzone/XML/docs/Reference/eBay/UploadSiteHostedPictures.html >) call will contain a full URL to the image on an eBay Picture Server. This is the URL that will be passed in through the **imageUrls** array.  
  
**Note:** Before any offer can be published, at least one image must exist for the offer. Links to images can either be passed in through this **imageUrls** container, or they can be passed in through the **product.imageUrls** container when creating each inventory item in the group. If the **variesBy.aspectsImageVariesBy** field is used to specify the main product aspect where the variations vary, the links to the images must be passed in through this **imageUrls** container, and there should be a picture for each variation. So, if the **variesBy.aspectsImageVariesBy** field is set to `Color`, a link should be included to an image demonstrating each available color in the group.  
  
In almost any category at no cost, sellers can include up to 24 pictures in one listing. For inventory items that are a part of an inventory item group/multiple-variation listings, a maximum of 12 pictures may be used per inventory item in the group. Motor vehicle listings are an exception. The number of included pictures in motor vehicle listings depend on the selected vehicle package (see [Fees for selling vehicles on eBay Motors](<https://www.ebay.com/help/selling/fees-credits-invoices/motors-fees?id=4127 >)).  
  
This container will always be returned for an inventory item group that has at least one published offer since a published offer will always have at least one picture, but this container will only be returned if defined for inventory item groups that have yet to have any published offers.
- **inventoryItemGroupKey** (string)
  - This is the unique identifier of the inventory item group. This identifier is created by the seller when an inventory item group is created.  
  
**Note:** This field is only applicable to the **getInventoryItemGroup** call and not to the **createOrReplaceInventoryItemGroup** call. In the **createOrReplaceInventoryItemGroup** call, the **inventoryItemGroupKey** value is passed into the end of the call URI instead.
- **subtitle** (string)
  - A subtitle is an optional listing feature that allows the seller to provide more information about the product, possibly including keywords that may assist with search results. An additional listing fee will be charged to the seller if a subtitle is used. For more information on using listing subtitles on the US site, see the [Adding a subtitle to your listings](<https://pages.ebay.com/help/sell/itemsubtitle.html >) help page.  
  
**Note:** Since this subtitle will ultimately become the subtitle in a multiple-variation listing, the seller should not include the **subtitle** field when creating the inventory items that are members of the group. If they do include the **subtitle** field in an inventory item record, the text in that field will overwrite the text provided in this **subtitle** field for each inventory item in the group that is published.  
  
This field will only be returned if set for an inventory item.  
  
**Maximum length**: 55
- **title** (string)
  - The title of the inventory item group. This title will ultimately become the listing title once the first offer of the group is published. This field is not initially required when first creating an inventory item group, but will be required before the first offer of the group is published.  
  
**Note:** Since this title will ultimately become the listing title in a multiple-variation listing, the seller should omit the **title** field when creating the inventory items that are members of the group. If they do include the **title** field in an inventory item record, the text in that field will overwrite the text provided in this **title** field for each inventory item in the group that is published.  
  
This field is always returned if one or more offers associated with the inventory item group have been published, and is only returned if set for an inventory item group if that group has yet to have any offers published.  
  

**Important!**Publish offer note: This field is required before an offer can be published to create an active listing.

  
**Maximum length**: 80
- **variantSKUs** (array)
  - This required container is used to assign individual inventory items to the inventory item group. Multiple SKU values are passed in to this container. If updating an existing inventory item group, the seller should make sure that all member SKU values are passed in, as long as the seller wants that SKU to remain in the group.  
  
It is also possible to add or remove SKUs with a **createOrReplaceInventoryItemGroup** call. If the seller wants to remove a SKU from the group, that seller will just omit that SKU value from this container to remove that inventory item/SKU from the inventory item group and any published, multiple-variation listing. However, a variation cannot be removed from the group if that variation has one or more sales for that listing. A workaround for this is to set that variation's quantity to `0` and it will be 'grayed out' in the View Item page.  
  
This container is always returned.
- **variesBy** (VariesBy)
  - This container is used to specify product aspects for which variations within an inventory item group vary, and a complete list of all those variances. For example, t-shirts in an inventory item group may be available in multiple sizes and colors. If this is the case, `Color` and `Size` would both be values in the **specifications.name** fields, and the available colors and sizes would be values under the corresponding **specifications.values** array. If the seller will be including multiple images in the listing that will demonstrate how each variation differs, that seller will also include the **aspectsImageVariesBy** field, and call out the product aspect where the listing images differ. In the t-shirts example, this product aspect would be `Color`, and the seller could either include URLs to images of the t-shirt (in available colors) through the inventory item group entity, or the seller could also included URLs to images of the t-shirt through the individual inventory item entities of the group.  
  
This container is not initially required when first creating an inventory item group, but the **variesBy.specifications** container will be required before the first offer of the group is published.  
  
This container is always returned if one or more offers associated with the inventory item group have been published, and is only returned if set for an inventory item group if that group has yet to have any offers published.  
  

**Important!**Publish offer note: This container and its child fields (as noted below) are required before an offer can be published to create an active listing.
- **videoIds** (array)
  - An array of one or more **videoId** values for the inventory item group. A video ID is a unique identifier that is automatically created by eBay when a seller successfully uploads a video to eBay using the [uploadVideo](/develop/api/sell/media_api#sell-media_api-video-uploadvideo) method of the [Media API](/develop/api/sell/media_api).  
  
For information on supported marketplaces and platforms, as well as other requirements and limitations of video support, please refer to [Managing videos](</api-docs/sell/static/inventory/managing-video-media.html >).  
  
**Note:** Only one video per listing is supported.

### InventoryItemListing
**Description:** This type is used by the **inventoryItems** container that is returned in the response of the **bulkMigrateListing** call. Up to five **sku**/**offerId** pairs may be returned under the **inventoryItems** container, dependent on how many eBay listings the seller is attempting to migrate to the inventory model.
**Type:** object

**Properties:**
- **offerId** (string)
  - Upon a successful migration of a listing, eBay auto-generates this unique identifier, and this offer ID value will be used to retrieve and manage the newly-created offer object. This value will only be generated and returned if the eBay listing is migrated successfully.
- **sku** (string)
  - This is the seller-defined SKU value associated with the item(s) in a listing. This same SKU value will be used to retrieve and manage the newly-created inventory item object if the listing migration is successful. This SKU value will get returned even if the migration is not successful.

### InventoryItems
**Description:** This type is used by the base response payload of **getInventoryItems** call.
**Type:** object

**Properties:**
- **href** (string)
  - This is the URL to the current page of inventory items.
- **inventoryItems** (array)
  - This container is an array of one or more inventory items, with detailed information on each inventory item.
- **limit** (integer)
  - This integer value is the number of inventory items that will be displayed on each results page.
- **next** (string)
  - This is the URL to the next page of inventory items. This field will only be returned if there are additional inventory items to view.
- **prev** (string)
  - This is the URL to the previous page of inventory items. This field will only be returned if there are previous inventory items to view.
- **size** (integer)
  - This integer value indicates the total number of pages of results that are available. This number will depend on the total number of inventory items available for viewing, and on the **limit** value.
- **total** (integer)
  - This integer value is the total number of inventory items that exist for the seller's account. Based on this number and on the **limit** value, the seller may have to toggle through multiple pages to view all inventory items.

### InventoryLocation
**Description:** This type is used by the **updateInventoryLocation** call to update operating hours, special hours, phone number, and other minor details of an inventory location.
**Type:** object

**Properties:**
- **location** (LocationDetails)
  - This container is used to add any additional physical address and geographical coordinate information for a warehouse or fulfillment center inventory location.  
  
**Note:** For warehouse inventory locations, address fields can be updated any number of times. For fulfillment center locations, address fields cannot be updated. However, if any address fields were omitted during the **createInventoryLocation** call, they can be added through this method.  
**Note:** When updating a warehouse location to a fulfillment center, sellers can update any of the address fields a single time during the same call used to make this update. After this, they can no longer be updated.
- **locationAdditionalInformation** (string)
  - This text field is used by the merchant to provide/update additional information about an inventory location. Whatever text is passed in this field will replace the current text string defined for this field. If the text will not change, the same text should be passed in once again.  
  
**Maximum length**: 256
- **locationInstructions** (string)
  - **Deprecated.** Do not use as STORE location types are no longer supported.
- **locationTypes** (array)
  - This container is used to update the location type(s) associated with an inventory location.
- **locationWebUrl** (string)
  - This text field is used by the merchant to provide/update the Website address (URL) associated with the inventory location. The URL that is passed in this field will replace any other URL that may be defined for this field.  
  
**Maximum length**: 512
- **name** (string)
  - This text field is used by the merchant to update the name of the inventory location. This name should be a human-friendly name. A name is not required for warehouse locations. The name that is passed in this field will replace any other name that may be defined for this field.
- **operatingHours** (array)
  - **Deprecated.** Do not use as STORE location types are no longer supported.
- **phone** (string)
  - This text field is used by the merchant to provide/update the phone number for the inventory location. The phone number that is passed in this field will replace any other phone number that may be defined for this field.  
  
**Maximum length**: 36
- **specialHours** (array)
  - **Deprecated.** Do not use as STORE location types are no longer supported.
- **timeZoneId** (string)
  - This field is used to provide/update the time zone of the inventory location being created. This value should be in Olson format (for example `America/Vancouver`). For supported values, see [Java Supported Zone Ids and Offsets](https://howtodoinjava.com/java/date-time/supported-zone-ids-offsets/#3-java-supported-zone-ids-and-offsets).  
  
**Note:** If specified, this time zone will be used for all hour related fields. If this field is not specified, the time zone will be calculated from the provided address fields.
- **fulfillmentCenterSpecifications** (FulfillmentCenterSpecifications)
  - This container is used to update information about a fulfillment center's shipping specifications, such as the weekly cut-off time schedule for order handling and any cut-off overrides.

### InventoryLocationFull
**Description:** This type is used by the **createInventoryLocation** call to provide details on the inventory location, including the location's name, physical address, operating hours, special hours, phone number and other details of an inventory location.
**Type:** object

**Properties:**
- **location** (LocationDetails)
  - This required container is used to set the physical address and geographical coordinates of a warehouse or fulfillment center inventory location. A warehouse location only requires the postal code and country OR city, province/state, and country, and does not require a full street address. However, the seller may still supply a full street address for a warehouse location. A complete address (**addressLine1**, **city**, **stateOrProvince**, **postalCode**, and **country**) is required for fulfillment center locations.  
  
**Note:** For fulfillment center locations, the **addressLine1**, **stateOrProvince**, **country** and **postalCode** fields cannot be changed once they have been set, though they can be added through the **updateInventoryLocation** method if they were omitted during location creation.
- **locationAdditionalInformation** (string)
  - This text field is used by the merchant to provide additional information about an inventory location.  
  
**Maximum length**: 256
- **locationInstructions** (string)
  - **Deprecated.** Do not use as STORE location types are no longer supported.
- **locationTypes** (array)
  - This array is used to define the function of the inventory location as either a `WAREHOUSE` or a `FULFILLMENT_CENTER`.  
  
To utilize the Multi-warehouse program, use `FULFILLMENT_CENTER`.  
  
**Default**: `WAREHOUSE`
- **locationWebUrl** (string)
  - This text field is used by the merchant to provide the Website address (URL) associated with the inventory location.  
  
**Maximum length**: 512
- **merchantLocationStatus** (StatusEnum)
  - This field is used to indicate whether the inventory location will be enabled (inventory can be loaded to location) or disabled (inventory cannot be loaded to location). If this field is omitted, a successful **createInventoryLocation** call will automatically enable the location. A merchant may want to create a new location but leave it as disabled if the location is not yet ready for active inventory. Once the location is ready, the merchant can use the **enableInventoryLocation** call to enable a location that is in a disabled state.  
  
See [StatusEnum](/develop/api/sell/inventory_api#sell-inventory_api-location-getinventorylocation.statusenum) for the supported values.  
  
**Default**: ENABLED
- **name** (string)
  - The seller-defined name of the inventory location. This name should be a human-friendly name.  
  
**Maximum length**: 1000
- **operatingHours** (array)
  - **Deprecated.** Do not use as STORE location types are no longer supported.
- **phone** (string)
  - This field is used to specify the phone number for an inventory location.  
  
**Maximum length**: 36
- **specialHours** (array)
  - **Deprecated.** Do not use as STORE location types are no longer supported.
- **timeZoneId** (string)
  - This field specifies the time zone of the inventory location being created. This value should be in Olson format (for example `America/Vancouver`). For supported values, see [Java Supported Zone Ids and Offsets](https://howtodoinjava.com/java/date-time/supported-zone-ids-offsets/#3-java-supported-zone-ids-and-offsets).  
  
**Note:** If specified, this time zone will be used for all hour related fields. If this field is not specified for a fulfillment center location, the time zone will be calculated from the provided address fields.
- **fulfillmentCenterSpecifications** (FulfillmentCenterSpecifications)
  - This container is used to specify information about a fulfillment center's shipping specifications, such as the weekly cut-off time schedule for order handling and any cut-off time overrides.  
  
**Note:** This container is required if one of the **locationTypes** of the inventory location is `FULFILLMENT_CENTER`, and is not applicable to other location types.

### InventoryLocationResponse
**Description:** This type is used by the base response of the **getInventoryLocation** and **getInventoryLocations** calls. These responses provide details about inventory location(s) defined for the merchant's account.
**Type:** object

**Properties:**
- **location** (Location)
  - This container provides details of an inventory location. The **address** container will always be returned, but it will not always have a complete street address, as a WAREHOUSE location does not require a full street address. The **geoCoordinates** container will only be returned if the seller provided geographical coordinates. The **locationId** field is always returned, but this value is only used internally by eBay.
- **locationAdditionalInformation** (string)
  - This text field provides additional information about an inventory location. This field is returned if it is set for the location.
- **locationInstructions** (string)
  - **Deprecated.** Do not use as STORE location types are no longer supported.
- **locationTypes** (array)
  - This array indicates if the inventory location is a warehouse or a fulfillment center.
- **locationWebUrl** (string)
  - This text field shows the Website address (URL) associated with the inventory location. This field is returned if defined for the location.
- **merchantLocationKey** (string)
  - The unique identifier of the inventory location. This identifier is set up by the merchant when the location is first created with the **createInventoryLocation** call.
- **merchantLocationStatus** (StatusEnum)
  - This field indicates whether the inventory location is enabled (inventory can be loaded to location) or disabled (inventory cannot be loaded to location). The merchant can use the **enableInventoryLocation** call to enable a location in disabled status, or the **disableInventoryLocation** call to disable a location in enabled status.
- **name** (string)
  - The name of the inventory location. This name should be a human-friendly name.
- **operatingHours** (array)
  - **Deprecated.** Do not use as STORE location types are no longer supported.
- **phone** (string)
  - **Deprecated.** Do not use as STORE location types are no longer supported.
- **specialHours** (array)
  - **Deprecated.** Do not use as STORE location types are no longer supported.
- **timeZoneId** (string)
  - This field specifies the time zone of the inventory location being created. This value should be in Olson format (for example `America/Vancouver`). For supported values, see [Java Supported Zone Ids and Offsets](https://howtodoinjava.com/java/date-time/supported-zone-ids-offsets/#3-java-supported-zone-ids-and-offsets).
- **fulfillmentCenterSpecifications** (FulfillmentCenterSpecifications)
  - This container provides information about a fulfillment center's shipping specifications, such as the weekly cut-off time schedule for order handling and any cut-off time overrides.  
  
**Note:** This field is only returned for fulfillment center locations.

### ListingDetails
**Description:** This type is used by the **listing** container in the **getOffer** and **getOffers** calls to provide the eBay listing ID, the listing status, and quantity sold for the offer. The **listing** container is only returned for published offers, and is not returned for unpublished offers.
**Type:** object

**Properties:**
- **listingId** (string)
  - The unique identifier of the eBay listing that is associated with the published offer.
- **listingOnHold** (boolean)
  - Indicates if a listing is on hold due to an eBay policy violation.  
  
If a listing is put on hold, users are unable to view the listing details, the listing is hidden from search, and all attempted purchases, offers, and bids for the listing are blocked. eBay, however, gives sellers the opportunity to address violations and get listings fully reinstated. A listing will be ended if a seller does not address a violation, or if the violation can not be rectified.  
  
If a listing is fixable, the seller should be able to view the listing details and this boolean will be returned as true.  
  
Once a listing is fixed, this boolean will no longer be returned.
- **listingStatus** (ListingStatusEnum)
  - The enumeration value returned in this field indicates the status of the listing that is associated with the published offer.
- **soldQuantity** (integer)
  - This integer value indicates the quantity of the product that has been sold for the published offer.

### ListingDurationEnum
**Description:** This enumerated type defines listing duration periods.  
  
**Note:** The `GTC` value is valid and applicable only to fixed-price listings; the `DAYS_nn` values are applicable to auction listings. | - **DAYS_1**: This enum value indicates that the auction listing offer is valid for 1 day, after which time unsold inventory will move to the common pool that is shared between active fixed-price listings and new offers. - **DAYS_3**: This enum value indicates that the auction listing offer is valid for 3 days, after which time unsold inventory will move to the common pool that is shared between active fixed-price listings and new offers. - **DAYS_5**: This enum value indicates that the auction listing offer is valid for 5 days, after which time unsold inventory will move to the common pool that is shared between active fixed-price listings and new offers. - **DAYS_7**: This enum value indicates that the auction listing offer is valid for 7 days, after which time unsold inventory will move to the common pool that is shared between active fixed-price listings and new offers. - **DAYS_10**: This enum value indicates that the auction listing offer is valid for 10 days, after which time unsold inventory will move to the common pool that is shared between active fixed-price listings and new offers. - **DAYS_21**: This enum value indicates that the auction listing offer is valid for 21 days, after which time unsold inventory will move to the common pool that is shared between active fixed-price listings and new offers. - **DAYS_30**: This enum value indicates that the auction listing offer is valid for 30 days, after which time unsold inventory will move to the common pool that is shared between active fixed-price listings and new offers. - **GTC**: This enum value indicates that the listing is a fixed-price offer. 'GTC' stands for Good 'Til Cancelled, which means that a fixed-price listing will remain active until the seller cancels/ends the listing. 'GTC' listings are automatically renewed every calendar month.  
  
For example, if a GTC listing is created July 5, the next monthly renewal date will be August 5. If a GTC listing is created on the 31st of the month, but the following month only has 30 days, the renewal will happen on the 30th in the following month. Finally, if a GTC listing is created on January 29-31, the renewal will happen on February 28th (or 29th during a 'Leap Year').  
  
**Note**: The GTC value is currently the only supported listing duration for fixed-price litings.
**Type:** object

### ListingPolicies
**Description:** This type is used to identify business policies including payment, return, and fulfillment policies, as well as to identify custom policies. These policies are, or will be, associated with the listing. Every published offer must have a payment, return, and fulfillment business policy associated with it. Additionally, depending on the country/countries in which sellers are offering products and/or services to consumers (e.g., residents of the European Union), specifying additional polices may be required.  
  
This type is also used to override the shipping costs of one or more shipping service options that are associated with the fulfillment policy, to enable eBay Plus eligibility for a listing, or to enable the Best Offer feature on the listing.
**Type:** object

**Properties:**
- **bestOfferTerms** (BestOffer)
  - This container is used if the seller would like to support the Best Offer feature on their listing. To enable the Best Offer feature, the seller will have to set the **bestOfferEnabled** field to `true`, and the seller also has the option of setting 'auto-accept' and 'auto-decline' price thresholds.  
  
**Note:** Best Offer is unavailable for multi-variation listings.  
This container is only returned if Best Offer is enabled on listing.
- **eBayPlusIfEligible** (boolean)
  - This field is included in an offer and set to `true` if a Top-Rated seller is opted in to the eBay Plus program. With the eBay Plus program, qualified sellers must commit to next-day delivery of the item, and the buyers must have an eBay Plus subscription to be eligible to receive the benefits of this program, which are free, next-day delivery, as well as free returns.  
  
**Note:** Currently, this program is only available on the Germany and Australian sites.  
This field will be returned in the [getOffer](/develop/api/sell/inventory_api#sell-inventory_api-offer-getoffer) and [getOffers](/develop/api/sell/inventory_api#sell-inventory_api-offer-getoffers) methods if set for the offer.
- **fulfillmentPolicyId** (string)
  - This unique identifier indicates the fulfillment business policy that will be used once an offer is published and converted to an eBay listing. This fulfillment business policy will set all fulfillment-related settings for the eBay listing.  
  
Business policies are not immediately required for offers, but are required before an offer can be published. The seller should review the fulfillment business policy before assigning it to the offer to make sure it is compatible with the inventory item and the offer settings. The seller may also want to review the shipping service costs in the fulfillment policy, and that seller might decide to override the shipping costs for one or more shipping service options by using the **shippingCostOverrides** container.  
  
Business policies can be created and managed in My eBay or with the [Account API v1](/develop/api/sell/account_api_v1). To get a list of all return policies associated with a seller's account on a specific eBay Marketplace, use the Account API v1's [getFulfillmentPolicies](/develop/api/sell/account_api_v1#sell-account_api_v1-get-getfulfillmentpolicies) method. There are also calls in the **Account API v1** to retrieve a fulfillment policy by policy ID or policy name.  
  
This field will be returned in the [getOffer](/develop/api/sell/inventory_api#sell-inventory_api-offer-getoffer) and [getOffers](/develop/api/sell/inventory_api#sell-inventory_api-offer-getoffers) methods if set for the offer.  
  

**Important!**Publish offer note: This field is required before an offer can be published to create an active listing.
- **paymentPolicyId** (string)
  - This unique identifier indicates the payment business policy that will be used once an offer is published and converted to an eBay listing. This payment business policy will set all payment-related settings for the eBay listing.  
  
Business policies are not immediately required for offers, but are required before an offer can be published. The seller should review the payment business policy to make sure that it is compatible with the marketplace and listing category before assigning it to the offer.  
  
Business policies can be created and managed in My eBay or with the [Account API v1](/develop/api/sell/account_api_v1). To get a list of all payment policies associated with a seller's account on a specific eBay Marketplace, use the Account API v1's [getPaymentPolicies](/develop/api/sell/account_api_v1#sell-account_api_v1-get-getpaymentpolicies) method. There are also calls in the **Account API v1** to retrieve a payment policy by policy ID or policy name.  
  
This field will be returned in the [getOffer](/develop/api/sell/inventory_api#sell-inventory_api-offer-getoffer) and [getOffers](/develop/api/sell/inventory_api#sell-inventory_api-offer-getoffers) methods if set for the offer.  
  

**Important!**Publish offer note: This field is required before an offer can be published to create an active listing.
- **productCompliancePolicyIds** (array)
  - This field contains the array of unique identifiers indicating the seller-created _global_ product compliance policies that will be used once an offer is published and converted to a listing.  
  
Product compliance policies provide buyers with important information and disclosures about products. For example, if you sell batteries and specific disclosures are required to be shared with all potential buyers, your global product compliance policy could contain the required disclosures.  
  
A maximum of six (6) global product compliance policies may apply to _each offer_.**Note:** For countries that support country-specific policies, use [regionalProductCompliancePolicies](#request.listingPolicies.regionalProductCompliancePolicies) to apply them to an offer.
- **regionalProductCompliancePolicies** (RegionalProductCompliancePolicies)
  - A comma-delimited list of unique identifiers indicating the seller-created _country-specific_ product compliance policies that that will be used once an offer is published and converted to a listing.  
  
Product compliance policies provide buyers with important information and disclosures about products. For example, if you sell batteries in a country requiring disclosures that apply _only_ to that country, a country-specific product compliance policy could contain this information.  
  
Each offer may include up to six (6) product compliance policies for _each_ of the following countries:

*   United Kingdom \[GB\]
*   Germany \[DE\]
*   France \[FR\]
*   Italy \[IT\]
*   Spain \[ES\]

  
For example, if a seller offers products in the UK, Germany, and Italy, each of which requires custom product compliance information, up to 18 policies (i.e., 6 policies x 3 countries,) may be included with each offer.**Note:** Product compliance policies that apply to _all_ countries to which a seller ships are specified using [productCompliancePolicyIds](#request.listingPolicies.productCompliancePolicyIds).
- **regionalTakeBackPolicies** (RegionalTakeBackPolicies)
  - The list of unique identifiers indicating the seller-created _country-specific_ take-back policies that will be used once an offer is published and converted to a listing. The law in some countries may require sellers to take back a used product when the buyer buys a new product.  
  
Each offer may include one (1) country-specific take-back policy for _each_ of the following countries:

*   United Kingdom \[GB\]
*   Germany \[DE\]
*   France \[FR\]
*   Italy \[IT\]
*   Spain \[ES\]

  
**Note:** Take-back policies that apply to _all_ countries to which a seller ships are specified using [takeBackPolicyId](#request.listingPolicies.takeBackPolicyId).
- **returnPolicyId** (string)
  - This unique identifier indicates the return business policy that will be used once an offer is published and converted to an eBay listing. This return business policy will set all return policy settings for the eBay listing.  
  
**Note:** As a part of Digital Services Act (DSA) requirements, as of April 3, 2023, buyers in the EU must be allowed to return an item within 14 days or more, unless the item is exempt. Where applicable, sellers should update their return policies to reflect this requirement of accepting returns from EU buyers.  
Business policies are not immediately required for offers, but are required before an offer can be published. The seller should review the return business policy before assigning it to the offer to make sure it is compatible with the inventory item and the offer settings.  
  
Business policies can be created and managed in My eBay or with the [Account API v1](/develop/api/sell/account_api_v1). To get a list of all return policies associated with a seller's account on a specific eBay Marketplace, use the Account API v1's [getReturnPolicies](/develop/api/sell/account_api_v1#sell-account_api_v1-get-getreturnpolicies) call. There are also calls in the **Account API v1** to retrieve a return policy by policy ID or policy name.  
  
This field will be returned in the [getOffer](/develop/api/sell/inventory_api#sell-inventory_api-offer-getoffer) and [getOffers](/develop/api/sell/inventory_api#sell-inventory_api-offer-getoffers) methods if set for the offer.  
  

**Important!**Publish offer note: This field is required before an offer can be published to create an active listing.
- **shippingCostOverrides** (array)
  - This container is used if the seller wishes to override the shipping costs or surcharge for one or more domestic or international shipping service options defined in the fulfillment listing policy. To override the costs of a specific domestic or international shipping service option, the seller must know the priority/order of that shipping service in the fulfillment listing policy. The name of a shipping service option can be found in the **shippingOptions.shippingServices.shippingServiceCode** field of the fulfillment policy, and the priority/order of that shipping service option is found in the **shippingOptions.shippingServices.sortOrderId** field. Both of these values can be retrieved by searching for that fulfillment policy with the **getFulfillmentPolicies** or **getFulfillmentPolicyByName** calls of the **Account API v1**. The **shippingCostOverrides.priority** value should match the **shippingOptions.shippingServices.sortOrderId** in order to override the shipping costs for that shipping service option. The seller must also ensure that the **shippingServiceType** value is set to `DOMESTIC` to override a domestic shipping service option, or to `INTERNATIONAL` to override an international shipping service option.  
  
A separate **ShippingCostOverrides** node is needed for each shipping service option whose costs are being overridden. All defined fields of the **shippingCostOverrides** container should be included, even if the shipping costs and surcharge values are not changing.  
  
The **shippingCostOverrides** container is returned in the [getOffer](/develop/api/sell/inventory_api#sell-inventory_api-offer-getoffer) and [getOffers](/develop/api/sell/inventory_api#sell-inventory_api-offer-getoffers) calls if one or more shipping cost overrides are being applied to the fulfillment policy.
- **takeBackPolicyId** (string)
  - This unique identifier indicates the seller-created _global_ take-back policy that will be used once an offer is published and converted to a listing.  
  
One (1) global take-back policy may be specified _per offer_.  
**Note:** For countries that support country-specific policies, use [regionalTakeBackPolicies](#request.listingPolicies.regionalTakeBackPolicies) to apply them to an offer.

### ListingStatusEnum
**Description:** This enumeration type is used to indicate the status of the eBay listing that is associated with the corresponding offer. | - **ACTIVE**: This enumeration value indicates that the eBay listing associated with the offer is active. - **OUT_OF_STOCK**: This enumeration value indicates that the eBay listing associated with the offer is still active, but that the product is currently out-of-stock. If a single-variation listing is out-of-stock, that listing will be kept alive but hidden from search. If a variation inside a multiple-variation listing is out-of-stock, only that variation is hidden, but the listing remains active and discoverable. - **INACTIVE**: This enumeration value indicates that the eBay listing associated with the offer is currently inactive. - **ENDED**: This enumeration value indicates that the eBay listing associated with the offer has ended. - **EBAY_ENDED**: This enumeration value indicates that the eBay customer service has administratively ended the eBay listing associated with the offer. - **NOT_LISTED**: This enumeration value indicates that the eBay listing associated with the offer has yet to be listed.
**Type:** object

### Location
**Description:** A complex type that is used to provide the physical address of a location, and it geo-coordinates.
**Type:** object

**Properties:**
- **address** (Address)
  - The **address** container is always returned in **getInventoryLocation**/**getInventoryLocations** calls. Except in the case of a fulfillment center location, a full address is not a requirement when setting up an inventory location.
- **geoCoordinates** (GeoCoordinates)
  - This container displays the Global Positioning System (GPS) latitude and longitude coordinates for the inventory location.  
  
This container is only returned if the geo-coordinates are set for an inventory location.
- **locationId** (string)
  - A unique eBay-assigned ID for the location.  
  
**Note:** This field should not be confused with the seller-defined **merchantLocationKey** value. It is the **merchantLocationKey** value which is used to identify an inventory location when working with inventory location API calls. The **locationId** value is only used internally by eBay.

### LocationAvailabilityDetails
**Description:** This type provides the unique identifier of an inventory location that is associated with a SKU within a listing.
**Type:** object

**Properties:**
- **merchantLocationKey** (string)
  - The unique identifier of a seller's fulfillment center location where inventory is available for the item or item variation.  
  
**Note:** When creating a location mapping using the **createOrReplaceSkuLocationMapping** method, the value entered in this field **must** be associated with a location with the `FULFILLMENT_CENTER` location type, or an error will occur. Sellers can check the [locationTypes](/develop/api/sell/inventory_api#sell-inventory_api-location-getinventorylocations#response.locations.locationTypes) array in the response of the [getInventoryLocations](/develop/api/sell/inventory_api#sell-inventory_api-location-getinventorylocations) method to see if their location has a value of `FULFILLMENT_CENTER`.

### LocationDetails
**Description:** This type is used by the **createInventoryLocation** call to provide an full or partial address of an inventory location.
**Type:** object

**Properties:**
- **address** (Address)
  - This required container sets the physical address of an inventory location. Except in the case of a fulfillment center location, a full address is not a requirement when setting up a location. For warehouse locations, the fields required in this container are either of the following sets:

*   **city**, **stateOrProvince**, and **country**
*   **postalCode** and **country**
- **geoCoordinates** (GeoCoordinates)
  - This container is used to set the Global Positioning System (GPS) latitude and longitude coordinates for the inventory location. Geo-coordinates are used for FULFILLMENT\_CENTER locations for delivery route-planning purposes (shorter distance to buyer generally means faster delivery). They are optional for WAREHOUSE locations.

### LocationMapping
**Description:** This type provides an array of locations that are associated with a SKU within a listing.
**Type:** object

**Properties:**
- **locations** (array)
  - This array represents a collection of fulfillment center locations mapped to a SKU.  
  
**Note:** Only the first 50 locations mapped to a SKU will be considered when calculating estimated delivery dates. Sellers can set up more than 50 locations using this method, but only the first 50 locations will be considered for calculating the estimates.

### LocationResponse
**Description:** This type is used by the base response payload for the **getInventoryLocations** call.
**Type:** object

**Properties:**
- **href** (string)
  - The URI of the current page of results from the result set.
- **limit** (integer)
  - The number of items returned on a single page from the result set.
- **next** (string)
  - The URI for the following page of results. This value is returned only if there is an additional page of results to display from the result set.  
  
**Maximum length**: 2048
- **offset** (integer)
  - The number of results skipped in the result set before listing the first returned result. This value is set in the request with the **offset** query parameter.

**Note:** The items in a paginated result set use a zero-based list where the first item in the list has an offset of `0`.
- **prev** (string)
  - The URI for the preceding page of results. This value is returned only if there is a previous page of results to display from the result set.  
  
**Maximum length**: 2048
- **total** (integer)
  - The total number of items retrieved in the result set.  
  
If no items are found, this field is returned with a value of `0`.
- **locations** (array)
  - An array of one or more of the merchant's inventory locations.

### Manufacturer
**Description:** This type provides name and contact information about the manufacturer of the item.
**Type:** object

**Properties:**
- **addressLine1** (string)
  - The first line of the product manufacturer's street address.  
  
**Maximum length**: 180 characters
- **addressLine2** (string)
  - The second line of the product manufacturer's street address. This field is not always used, but can be used for secondary address information such as 'Suite Number' or 'Apt Number'.  
  
**Maximum length**: 180 characters
- **city** (string)
  - The city of the product manufacturer's street address.  
  
**Maximum length**: 64 characters
- **companyName** (string)
  - The company name of the product manufacturer.  
  
**Maximum length**: 100 characters
- **contactUrl** (string)
  - The contact URL of the product manufacturer.  
  
**Maximum length**: 250 characters
- **country** (CountryCodeEnum)
  - This defines the list of valid country codes, adapted from [ISO 3166-1](http://www.iso.org/iso/country_codes) country codes. List elements take the form of a two-letter code (Alpha-2), a three-letter code (Alpha-3), and a three-digit code (Numeric). For example, the entry for Japan includes JP, JPN, 392. Short codes provide uniform recognition, avoiding language-dependent country names. The numeric code is helpful where Latin script may be problematic. Not all listed codes are universally recognized as countries. For example, Antarctica is AQ, ATA, 010.
- **email** (string)
  - The product manufacturer's business email address.  
  
**Maximum length**: 180 characters
- **phone** (string)
  - The product manufacturer's business phone number.  
  
**Maximum length**: 64 characters
- **postalCode** (string)
  - The postal code of the product manufacturer's street address.  
  
**Maximum length**: 9 characters
- **stateOrProvince** (string)
  - The state or province of the product manufacturer's street address.  
  
**Maximum length**: 64 characters

### MarketplaceEnum
**Description:** This enumeration type is used to indicate the different eBay marketplace sites. | - **EBAY_US**: This enumeration value indicates that the eBay Marketplace is the US site (ebay.com). - **EBAY_MOTORS**: This enumeration value indicates that the eBay Marketplace is the US eBay Motors site (ebay.com/motors). - **EBAY_CA**: This enumeration value indicates that the eBay Marketplace is the Canada (English) site (ebay.ca). - **EBAY_GB**: This enumeration value indicates that the eBay Marketplace is the UK site (ebay.co.uk). - **EBAY_AU**: This enumeration value indicates that the eBay Marketplace is the Australia site (ebay.com.au). - **EBAY_AT**: This enumeration value indicates that the eBay Marketplace is the Austria site (ebay.at). - **EBAY_BE**: This enumeration value indicates that the eBay marketplace is the Belgium (Dutch) site (www.ebay.be). - **EBAY_FR**: This enumeration value indicates that the eBay Marketplace is the France site (ebay.fr). - **EBAY_DE**: This enumeration value indicates that the eBay Marketplace is the Germany site (ebay.de). - **EBAY_IT**: This enumeration value indicates that the eBay Marketplace is the Italy site (ebay.it). - **EBAY_NL**: This enumeration value indicates that the eBay Marketplace is the Netherlands site (ebay.nl). - **EBAY_ES**: This enumeration value indicates that the eBay Marketplace is the Spain site (ebay.es). - **EBAY_CH**: This enumeration value indicates that the eBay Marketplace is the Switzerland site (ebay.ch). - **EBAY_TW**: This enumeration value indicates that the eBay Marketplace is the Taiwan site (ebay.com/tw). - **EBAY_CZ**: This enumeration value indicates that the eBay Marketplace is the Czech Republic site (ebay.com/sch/Czech-Republic). - **EBAY_DK**: This enumeration value indicates that the eBay Marketplace is the Denmark site (ebay.com/sch/Denmark). - **EBAY_FI**: This enumeration value indicates that the eBay Marketplace is the Finland site (ebay.com/sch/Finland). - **EBAY_GR**: This enumeration value indicates that the eBay Marketplace is the Greece site (ebay.com/sch/Greece). - **EBAY_HK**: This enumeration value indicates that the eBay Marketplace is the Hong Kong site (ebay.com.hk). - **EBAY_HU**: This enumeration value indicates that the eBay Marketplace is the Hungary site (ebay.com/sch/Hungary). - **EBAY_IN**: This enumeration value indicates that the eBay Marketplace is the India site (ebay.in).  
  
**Note**: eBay India is no longer a functioning eBay marketplace. - **EBAY_ID**: This enumeration value indicates that the eBay Marketplace is the Indonesia site (id.ebay.com). - **EBAY_IE**: This enumeration value indicates that the eBay Marketplace is the Ireland site (ebay.ie). - **EBAY_IL**: This enumeration value indicates that the eBay Marketplace is the Israel site (ebay.com/sch/Israel). - **EBAY_MY**: This enumeration value indicates that the eBay Marketplace is the Malaysia site (ebay.com/my). - **EBAY_NZ**: This enumeration value indicates that the eBay Marketplace is the New Zealand site (ebay.com/sch/New-Zealand). - **EBAY_NO**: This enumeration value indicates that the eBay Marketplace is the Norway site (ebay.com/sch/Norway). - **EBAY_PH**: This enumeration value indicates that the eBay Marketplace is the Philippines site (ebay.ph). - **EBAY_PL**: This enumeration value indicates that the eBay Marketplace is the Poland site (ebay.pl). - **EBAY_PT**: This enumeration value indicates that the eBay Marketplace is the Portugal site (ebay.com/sch/Portugal). - **EBAY_PR**: This enumeration value indicates that the eBay Marketplace is the Puerto Rico site (ebay.com/sch/Puerto-Rico). - **EBAY_RU**: This enumeration value indicates that the eBay Marketplace is the Russia site (ebay.com/sch/Russia). - **EBAY_SG**: This enumeration value indicates that the eBay Marketplace is the Singapore site (ebay.com/sg). - **EBAY_ZA**: This enumeration value indicates that the eBay Marketplace is the South Africa site (ebay.com/sch/South-Africa). - **EBAY_SE**: This enumeration value indicates that the eBay Marketplace is the Sweden site (ebay.com/sch/Sweden). - **EBAY_TH**: This enumeration value indicates that the eBay Marketplace is the Thailand site (export.ebay.co.th). - **EBAY_VN**: This enumeration value indicates that the eBay Marketplace is the Vietnam site (ebay.vn). - **EBAY_CN**: This enumeration value indicates that the eBay Marketplace is the China site (ebay.com/sch/China). - **EBAY_PE**: This enumeration value indicates that the eBay Marketplace is the Peru site (ebay.com/sch/Peru). - **EBAY_JP**: This enumeration value indicates that the eBay Marketplace is the Japan site (ebay.co.jp).
**Type:** object

### MigrateListing
**Description:** This type is used to specify one to five eBay listings that will be migrated to the new Inventory model.
**Type:** object

**Properties:**
- **listingId** (string)
  - The unique identifier of the eBay listing to migrate to the new Inventory model. In the Trading API, this field is known as the **ItemID**.  
  
Up to five unique eBay listings may be specified here in separate **listingId** fields. The seller should make sure that each of these listings meet the requirements that are stated at the top of this Call Reference page.

### MigrateListingResponse
**Description:** This type is used to display the results of each listing that the seller attempted to migrate.
**Type:** object

**Properties:**
- **errors** (array)
  - If one or more errors occur with the attempt to migrate the listing, this container will be returned with detailed information on each error.
- **inventoryItemGroupKey** (string)
  - This field will only be returned for a multiple-variation listing that the seller attempted to migrate. Its value is auto-generated by eBay. For a multiple-variation listing that is successfully migrated to the new Inventory model, eBay automatically creates an inventory item group object for the listing, and the seller will be able to retrieve and manage that new inventory item group object by using the value in this field.
- **inventoryItems** (array)
  - This container exists of an array of SKU values and offer IDs. For single-variation listings, this will only be one SKU value and one offer ID (if listing was successfully migrated), but multiple SKU values and offer IDs will be returned for multiple-variation listings.
- **listingId** (string)
  - The unique identifier of the eBay listing that the seller attempted to migrate.
- **marketplaceId** (MarketplaceEnum)
  - This is the unique identifier of the eBay Marketplace where the listing resides. The value fo the eBay US site will be `EBAY_US`.
- **statusCode** (integer)
  - This field is returned for each listing that the seller attempted to migrate. See the **HTTP status codes** table to see which each status code indicates.
- **warnings** (array)
  - If one or more warnings occur with the attempt to migrate the listing, this container will be returned with detailed information on each warning. It is possible that a listing can be successfully migrated even if a warning occurs.

### MinimumAdvertisedPriceHandlingEnum
**Description:** This type is used to control how/when the Minimum Advertised Price is shown for an offer. The Minimum Advertised Price (MAP) feature is only available on the US site. | - **NONE**: This enumeration value is used if the seller does not wish to include the Minimum Advertised Price in the offer. - **PRE_CHECKOUT**: This enumeration value is used if the seller wish to dispay the Minimum Advertised Price to prospective buyers prior to checkout. - **DURING_CHECKOUT**: This enumeration value is used if the seller wish to dispay the Minimum Advertised Price after the buyer already commits to buy the item.
**Type:** object

### NameValueList
**Description:** This type is used by the **compatibilityProperties** container to identify a motor vehicle using name/value pairs.
**Type:** object

**Properties:**
- **name** (string)
  - This string value identifies the motor vehicle aspect, such as 'make', 'model', 'year', 'trim', and 'engine'. Typically, the make, model, and year of the motor vehicle are always required, with the trim and engine being necessary sometimes, but it will be dependent on the part or accessory, and on the vehicle class.  
  
The [getCompatibilityProperties](/develop/api/sell/taxonomy_api#sell-taxonomy_api-category_tree-getcompatibilityproperties) method of the Taxonomy API can be used to retrieve applicable vehicle aspect names for a specified category.
- **value** (string)
  - This string value identifies the motor vehicle aspect specified in the corresponding **name** field. For example, if the **name** field is 'make', this field may be 'Toyota', or if the **name** field is 'model', this field may be 'Camry'.  
  
The [getCompatibilityPropertyValues](/develop/api/sell/taxonomy_api#sell-taxonomy_api-category_tree-getcompatibilitypropertyvalues) method of the Taxonomy API can be used to retrieve possible values for vehicle aspect names.

### OfferKeyWithId
**Description:** This type is used by the [getListingFees](/develop/api/sell/inventory_api#sell-inventory_api-offer-getlistingfees) call to indicate the unpublished offer(s) for which expected listing fees will be retrieved. The user passes in one or more [offerId](/develop/api/sell/inventory_api#sell-inventory_api-offer-bulkpublishoffer.offerkeywithid.offerid) values (a maximum of 250). See the [Standard selling fees](https://pages.ebay.com/help/sell/fees.html) help page for more information on listing fees.
**Type:** object

**Properties:**
- **offerId** (string)
  - The unique identifier of an unpublished offer for which expected listing fees will be retrieved. One to 250 **offerId** values can be passed in to the [offers](/develop/api/sell/inventory_api#sell-inventory_api-offer-getlistingfees.offerkeyswithid.offers) container for one [getListingFees](/develop/api/sell/inventory_api#sell-inventory_api-offer-getlistingfees.offerkeyswithid.offers) call.  
  
Use the [getOffers](/develop/api/sell/inventory_api#sell-inventory_api-offer-getoffers) method to retrieve offer IDs.  
  
**Note:** Errors will occur if **offerId** values representing published offers are passed in.

### OfferKeysWithId
**Description:** This type is used by the base request payload of the **getListingFees** call.
**Type:** object

**Properties:**
- **offers** (array)
  - This container is used to identify one or more (up to 250) unpublished offers for which expected listing fees will be retrieved. The user passes one or more **offerId** values (maximum of 250) in to this container to identify the unpublished offers in which to retrieve expected listing fees. This call is only applicable for offers in the unpublished state.  
  
The call response gives aggregate fee amounts per eBay marketplace, and does not give fee information at the individual offer level.

### OfferResponse
**Description:** This type is used by the response payload of the **createOffer** and **updateOffer** calls. The **offerId** field contains the unique identifier for the offer if the offer is successfully created by the **createOffer** call. The **warnings** field contains any errors and/or warnings that may have been triggered by the call.

**Note:** The **offerId** value is only returned with a successful **createOffer** call. This field will not be returned in the **updateOffer** response.
**Type:** object

**Properties:**
- **offerId** (string)
  - The unique identifier of the offer that was just created with a **createOffer** call. It is not returned if the **createOffer** call fails to create an offer. This identifier will be needed for many offer-related calls.

**Note:** The **offerId** value is only returned with a successful **createOffer** call. This field will not be returned in the **updateOffer** response.
- **warnings** (array)
  - This container will contain an array of errors and/or warnings when a call is made, and errors and/or warnings occur.

### OfferResponseWithListingId
**Description:** This type is used to indicate the status of each offer that the user attempted to publish. If an offer is successfully published, an eBay listing ID (also known as an Item ID) is returned. If there is an issue publishing the offer and creating the new eBay listing, the information about why the listing failed should be returned in the **errors** and/or **warnings** containers.
**Type:** object

**Properties:**
- **errors** (array)
  - This container will be returned if there were one or more errors associated with publishing the offer.
- **listingId** (string)
  - The unique identifier of the newly-created eBay listing. This field is only returned if the seller successfully published the offer and created the new eBay listing.
- **offerId** (string)
  - The unique identifier of the offer that the seller published (or attempted to publish).
- **statusCode** (integer)
  - The HTTP status code returned in this field indicates the success or failure of publishing the offer specified in the **offerId** field. See the **HTTP status codes** table to see which each status code indicates.
- **warnings** (array)
  - This container will be returned if there were one or more warnings associated with publishing the offer.

### OfferSkuResponse
**Description:** This type is used by the **bulkCreateOffer** response to show the status of each offer that the seller attempted to create with the **bulkCreateOffer** method. For each offer that is created successfully, the returned **statusCode** value should be `200`, and a unique **offerId** should be created for each offer. If any issues occur with the creation of any offers, **errors** and/or **warnings** containers will be returned.
**Type:** object

**Properties:**
- **errors** (array)
  - This container will be returned at the offer level, and will contain one or more errors if any occurred with the attempted creation of the corresponding offer.
- **format** (FormatTypeEnum)
  - This enumeration value indicates the listing format of the offer.
- **marketplaceId** (MarketplaceEnum)
  - This enumeration value is the unique identifier of the eBay marketplace for which the offer will be made available. This enumeration value should be the same for all offers since the **bulkCreateOffer** method can only be used to create offers for one eBay marketplace at a time.
- **offerId** (string)
  - The unique identifier of the newly-created offer. This identifier should be automatically created by eBay if the creation of the offer was successful. It is not returned if the creation of the offer was not successful. In which case, the user may want to scan the corresponding **errors** and/or **warnings** container to see what the issue may be.
- **sku** (string)
  - The seller-defined Stock-Keeping Unit (SKU) of the inventory item. The **sku** value is required for each product offer that the seller is trying to create, and it is always returned to identified the product that is associated with the offer.
- **statusCode** (integer)
  - The integer value returned in this field is the http status code. If an offer is created successfully, the value returned in this field should be `200`. A user can view the **HTTP status codes** section for information on other status codes that may be returned with the **bulkCreateOffer** method.
- **warnings** (array)
  - This container will be returned at the offer level, and will contain one or more warnings if any occurred with the attempted creation of the corresponding offer. Note that it is possible that an offer can be created successfully even if one or more warnings are triggered.

### OfferStatusEnum
**Description:** This enumeration type is used to indicate the current status of the offer (published or unpublished). | - **PUBLISHED**: This enumeration value indicates that the offer is in the published state, and is a part of a single or multiple-variation eBay listing. For published offers, more information on the eBay listing, including the listing ID and the listing status, can be found in the listing container. - **UNPUBLISHED**: This enumeration value indicates that the offer is in the unpublished state and has yet to be converted to an active eBay listing.
**Type:** object

### Offers
**Description:** This type is used by the base response of the **getOffers** call, and it is an array of one or more of the seller's offers, along with pagination data.
**Type:** object

**Properties:**
- **href** (string)
  - This is the URL to the current page of offers.
- **limit** (integer)
  - This integer value is the number of offers that will be displayed on each results page.
- **next** (string)
  - This is the URL to the next page of offers. This field will only be returned if there are additional offers to view.
- **offers** (array)
  - This container is an array of one or more of the seller's offers for the SKU value that is passed in through the required **sku** query parameter.  
  
**Note:** Currently, the Inventory API does not support the same SKU across multiple eBay marketplaces.  
**Max Occurs:** 25
- **prev** (string)
  - This is the URL to the previous page of offers. This field will only be returned if there are previous offers to view.
- **size** (integer)
  - This integer value indicates the number of offers being displayed on the current page of results. This number will generally be the same as the **limit** value if there are additional pages of results to view.  
  
**Note:** The same SKU can be offered through an auction and a fixed-price listing concurrently. If this is the case, **getOffers** will return two offers and this value will be `2`. Otherwise, only one offer will be returned and this value will be `1`.
- **total** (integer)
  - This integer value is the total number of offers that exist for the specified SKU value. Based on this number and on the **limit** value, the seller may have to toggle through multiple pages to view all offers.  
  
**Note:** The same SKU can be offered through an auction and a fixed-price listing concurrently. If this is the case, **getOffers** will return two offers, so this value would be `2`. Otherwise, only one offer will be returned and this value will be `1`.

### OperatingHours
**Description:** **Deprecated.** Do not use as STORE location types are no longer supported.
**Type:** object

**Properties:**
- **dayOfWeekEnum** (DayOfWeekEnum)
  - A **dayOfWeekEnum** value is required for each day of the week that the store location has regular operating hours.  
  
This field is returned if operating hours are defined for the store location.
- **intervals** (array)
  - This container is used to define the opening and closing times of a store location's working day (defined in the **dayOfWeekEnum** field). An **intervals** container is needed for each day of the week that the store location is open. If a store location closes for lunch (or any other period during the day) and then reopens, multiple **open** and **close** pairs are needed  
  
This container is returned if operating hours are defined for the store location.

### Overrides
**Description:** This type defines the override dates for cut-off times. This allows sellers to set special hours for their inventory location and specify different cut-off times on these days.
**Type:** object

**Properties:**
- **cutOffTime** (string)
  - This field is used to override the cut-off time(s) specified in the **weeklySchedule** container. If an order is placed after this time in the specified date or date range, it will be handled by the seller on the following day.  
  
**Format:** `00:00`
- **endDate** (string)
  - The end date of the cut-off time override in [ISO 8601](<https://www.iso.org/iso-8601-date-and-time-format.html > "https://www.iso.org ") format, which is based on the 24-hour Coordinated Universal Time (UTC) clock.  
  
**Note:** If the cut-off time override is only for a single day, input the same date in the **startDate** and **endDate** fields.  
**Format:** `[YYYY]-[MM]-[DD]`  
  
**Example:** `2024-08-06`  
  
**Note:** The time zone for this date is specified from the **timeZoneId** field. If this field is not used, the time zone will be derived from the provided address.
- **startDate** (string)
  - The start date of the cut-off time override in [ISO 8601](<https://www.iso.org/iso-8601-date-and-time-format.html > "https://www.iso.org ") format, which is based on the 24-hour Coordinated Universal Time (UTC) clock.  
  
**Note:** If the cut-off time override is only for a single day, input the same date in the **startDate** and **endDate** fields.  
**Format:** `[YYYY]-[MM]-[DD]`  
  
**Example:** `2024-08-04`  
  
**Note:** The time zone for this date is specified from the **timeZoneId** field. If this field is not used, the time zone will be derived from the provided address.

### PricingSummary
**Description:** This type is used to specify the listing price for the product and settings for the Minimum Advertised Price and Strikethrough Pricing features. The **price** field must be supplied before an offer is published, but a seller may create an offer without supplying a price initially. The Minimum Advertised Price feature is only available on the US site. Strikethrough Pricing is available on the US, eBay Motors, UK, Germany, Canada (English and French), France, Italy, and Spain sites.
**Type:** object

**Properties:**
- **auctionReservePrice** (Amount)
  - This field indicates the lowest price at which the seller is willing to sell an item through an auction listing. Note that setting a Reserve Price will incur a listing fee of $5 or 7.5% of the Reserve Price, whichever is greater. The minimum fee is $5.  
  
**Important:** This fee is charged regardless of whether or not the item is sold.
- **auctionStartPrice** (Amount)
  - This field indicates the minimum bidding price for the auction. The bidding starts at this price.  
  
**Note:** If the **auctionReservePrice** is also specified, the value of **auctionStartPrice** must be lower than the value of **auctionReservePrice**.
- **minimumAdvertisedPrice** (Amount)
  - This container is needed if the Minimum Advertised Price (MAP) feature will be used in the offer. Minimum Advertised Price (MAP) is an agreement between suppliers (or manufacturers (OEM)) and the retailers (sellers) stipulating the lowest price an item is allowed to be advertised at. Sellers can only offer prices below this price through the use of other discounts. The MAP feature is only available to eligible US sellers. This field will be ignored if the seller and or the listing is not eligible for the MAP feature.  
  
This container will be returned by [getOffer](/develop/api/sell/inventory_api#sell-inventory_api-offer-getoffer) and [getOffers](/develop/api/sell/inventory_api#sell-inventory_api-offer-getoffers) if set for the offer.
- **originallySoldForRetailPriceOn** (SoldOnEnum)
  - This field is needed if the Strikethrough Pricing (STP) feature will be used in the offer. This field indicates that the product was sold for the price in the **originalRetailPrice** field on an eBay site, or sold for that price by a third-party retailer. When using the **createOffer** or **updateOffer** calls, the seller will pass in a value of `ON_EBAY` to indicate that the product was sold for the **originalRetailPrice** on an eBay site, or the seller will pass in a value of `OFF_EBAY` to indicate that the product was sold for the **originalRetailPrice** through a third-party retailer. This field and the **originalRetailPrice** field are only applicable if the seller and listing are eligible to use the Strikethrough Pricing feature, a feature which is limited to the US (core site and Motors), UK, Germany, Canada (English and French versions), France, Italy, and Spain sites.  
  
This field will be returned by [getOffer](/develop/api/sell/inventory_api#sell-inventory_api-offer-getoffer) and [getOffers](/develop/api/sell/inventory_api#sell-inventory_api-offer-getoffers) if set for the offer.
- **originalRetailPrice** (Amount)
  - This container is needed if the Strikethrough Pricing (STP) feature will be used in the offer. The dollar value passed into this field indicates the original retail price set by the manufacturer (OEM). eBay does not maintain or validate the value supplied here by the seller. The dollar value in this field should always be more than the dollar value in the **price** container. This field and the **originallySoldForRetailPriceOn** field are only applicable if the seller and listing are eligible to use the Strikethrough Pricing feature, a feature which is limited to the US (core site and Motors), UK, Germany, Canada (English and French versions), France, Italy, and Spain sites. Compare the **originalRetailPrice** and the dollar value in the **price** field to determine the amount of savings to the buyer. This Original Retail Price will have a strikethrough line through for a marketing affect.  
  
This container will be returned by [getOffer](/develop/api/sell/inventory_api#sell-inventory_api-offer-getoffer) and [getOffers](/develop/api/sell/inventory_api#sell-inventory_api-offer-getoffers) if set for the offer.
- **price** (Amount)
  - This is the listing price of the product. A listing price must be specified before publishing an offer, but it is possible to create an offer without a price.  
  
For published offers, this container will always be returned, but for unpublished offers, this container will only be returned if set for the offer.  
  

**Important!**Publish offer note: This container and its two child fields (**currency** and **value**) are required before an offer can be published to create an active listing.
- **pricingVisibility** (MinimumAdvertisedPriceHandlingEnum)
  - This field is needed if the Minimum Advertised Price (MAP) feature will be used in the offer. This field is only applicable if an eligible US seller is using the Minimum Advertised Price (MAP) feature and a **minimumAdvertisedPrice** has been specified. The value set in this field will determine whether the MAP price is shown to a prospective buyer prior to checkout through a pop-up window accessed from the View Item page, or if the MAP price is not shown until the checkout flow after the buyer has already committed to buying the item. To show the MAP price prior to checkout, the seller will set this value to `PRE_CHECKOUT`. To show the MAP price after the buyer already commits to buy the item, the seller will set this value to `DURING_CHECKOUT`. This field will be ignored if the seller and/or the listing is not eligible for the MAP feature.  
  
This field will be returned by [getOffer](/develop/api/sell/inventory_api#sell-inventory_api-offer-getoffer) and [getOffers](/develop/api/sell/inventory_api#sell-inventory_api-offer-getoffers) if set for the offer.

### ProductFamilyProperties
**Description:** This type is used to specify the details of a motor vehicle that is compatible with the inventory item specified through the SKU value in the call URI.
**Type:** object

**Properties:**
- **engine** (string)
  - **Important!** The **productFamilyProperties** container is no longer supported.
- **make** (string)
  - **Important!** The **productFamilyProperties** container is no longer supported.
- **model** (string)
  - **Important!** The **productFamilyProperties** container is no longer supported.
- **trim** (string)
  - **Important!** The **productFamilyProperties** container is no longer supported.
- **year** (string)
  - **Important!** The **productFamilyProperties** container is no longer supported.

### ProductIdentifier
**Description:** This type is used to identify a motor vehicle that is compatible with the corresponding inventory item (the SKU that is passed in as part of the call URI). The motor vehicle can be identified through an eBay Product ID or a K-Type value. The **gtin** field (for inputting Global Trade Item Numbers) is for future use only. If a motor vehicle is found in the eBay product catalog, the motor vehicle properties (engine, make, model, trim, and year) will automatically get picked up for that motor vehicle.  
  
**Note:** Currently, parts compatibility is only applicable for motor vehicles, but it is possible that the Product Compatibility feature is expanded to other (non-vehicle) products in the future.
**Type:** object

**Properties:**
- **epid** (string)
  - This field can be used if the seller already knows the eBay catalog product ID (ePID) associated with the motor vehicle that is to be added to the compatible product list. If this eBay catalog product ID is found in the eBay product catalog, the motor vehicle properties (e.g. make, model, year, engine, and trim) will automatically get picked up for that motor vehicle.
- **gtin** (string)
  - This field can be used if the seller knows the Global Trade Item Number for the motor vehicle that is to be added to the compatible product list. If this GTIN value is found in the eBay product catalog, the motor vehicle properties (e.g. make, model, year, engine, and trim will automatically get picked up for that motor vehicle.  
  
**Note:** This field is for future use.
- **ktype** (string)
  - This field can be used if the seller knows the K Type Number for the motor vehicle that is to be added to the compatible product list. If this K Type value is found in the eBay product catalog, the motor vehicle properties (e.g. make, model, year, engine, and trim) will automatically get picked up for that motor vehicle.  
  
Only the AU, DE, ES, FR, IT, and UK marketplaces support the use of K Type Numbers.

### ProductSafety
**Description:** This type is used to define the **pictograms** and **statement** containers, and the optional **component** field, that provide product safety and compliance related information.
**Type:** object

**Properties:**
- **component** (string)
  - This field is used by the seller to provide product safety component information for the listing. For example, component information can include specific warnings related to product safety, such as 'Tipping hazard'.  
  
**Note:** Component information can only be specified if used with the **pictograms** and/or **statements** field; if the component is provided without one or both of these fields, an error will occur.  
**Maximum length:** 120 characters
- **pictograms** (array)
  - An array of comma-separated string values used to provide product safety pictogram(s) for the listing.  
  
If your product shows universal product safety or compliance symbols, please select the values corresponding to the product safety pictograms for display in the product safety section of the listing. The seller specifies the identifier of each pictogram in this field.  
  
**Note:** For product safety pictograms, use the [getProductSafetyLabels](/develop/api/sell/metadata_api#sell-metadata_api-marketplace-getproductsafetylabels) method of the **Metadata API** to find supported values for a specific marketplace/site.  
A maximum of 2 pictograms are allowed for product safety.
- **statements** (array)
  - An array of comma-separated string values used to provide product safety statement(s) for the listing.  
  
If your product shows universal product safety or compliance warnings, please select the values corresponding to the product safety statements for display in the product safety section of the listing. The seller specifies the identifier of each statement in this field.  
  
**Note:** For product safety statements, use the [getProductSafetyLabels](/develop/api/sell/metadata_api#sell-metadata_api-marketplace-getproductsafetylabels) method of the **Metadata API** to find supported values for a specific marketplace/site.  
A maximum of 8 statements are allowed for product safety.

### PublishByInventoryItemGroupRequest
**Description:** This type is used by the request payload of the **publishByInventoryItemGroup** call. The identifier of the inventory item group to publish and the eBay marketplace where the listing will be published is needed in the request payload.
**Type:** object

**Properties:**
- **inventoryItemGroupKey** (string)
  - This is the unique identifier of the inventory item group. All unpublished offers associated with this inventory item group will be published as a multiple-variation listing if the **publishByInventoryItemGroup** call is successful. The **inventoryItemGroupKey** identifier is automatically generated by eBay once an inventory item group is created.  
  
To retrieve an **inventoryItemGroupKey** value, you can use the [getInventoryItem](/develop/api/sell/inventory_api#sell-inventory_api-inventory_item-getinventoryitem) method to retrieve an inventory item that is known to be in the inventory item group to publish, and then look for the inventory item group identifier under the **groupIds** container in the response of that call.
- **marketplaceId** (MarketplaceEnum)
  - This is the unique identifier of the eBay site on which the multiple-variation listing will be published. The **marketplaceId** enumeration values are found in **MarketplaceEnum**.

### PublishResponse
**Description:** This type is used by the base response payload of the **publishOffer** and **publishOfferByInventoryItemGroup** calls.
**Type:** object

**Properties:**
- **listingId** (string)
  - The unique identifier of the newly created eBay listing. This field is returned if the single offer (if **publishOffer** call was used) or group of offers in an inventory item group (if **publishOfferByInventoryItemGroup** call was used) was successfully converted into an eBay listing.
- **warnings** (array)
  - This container will contain an array of errors and/or warnings if any occur when a **publishOffer** or **publishOfferByInventoryItemGroup** call is made.

### RegionalProductCompliancePolicies
**Description:** This type lists regional product compliance policies to be used by an offer when it is published and converted to a listing.
**Type:** object

**Properties:**
- **countryPolicies** (array)
  - The array of country-specific product compliance policies to be used by an offer when it is published and converted to a listing.

### RegionalTakeBackPolicies
**Description:** This type lists regional take-back policies to be used by an offer when it is published and converted to a listing.
**Type:** object

**Properties:**
- **countryPolicies** (array)
  - The array of country-specific take-back policies to be used by an offer when it is published and converted to a listing.

### Regulatory
**Description:** Type defining regulatory information that the seller is required to disclose.
**Type:** object

**Properties:**
- **documents** (array)
  - This container provides a collection of regulatory documents associated with the listing.  
  
For information on removing one or more files from a listing using the [updateOffer](/develop/api/sell/inventory_api#sell-inventory_api-offer-updateoffer) method, see [Remove documents from listings.](/api-docs/sell/static/inventory/managing-document-media.html#revise) .  
  
**Note:** As a part of General Product Safety Regulation (GPSR) requirements effective on December 13th, 2024, sellers operating in, or shipping to, EU-based countries or Northern Ireland are conditionally required to provide regulatory document information in their eBay listings. For more information on GPSR, see [General Product Safety Regulation (GPSR)](<https://www.ebay.com/sellercenter/resources/general-product-safety-regulation >).
- **energyEfficiencyLabel** (EnergyEfficiencyLabel)
  - This container provides information about the energy efficiency for certain durable goods.  
  
**Note:** This container can be used to provide European energy efficiency (EEK) information for listings in the **Tyres** and **Appliance** categories for sellers in the EU and UK, and **Smartphones and Tablets** categories for sellers in the US, AU, CA, EU, and UK. If no EEK information is specified through this container, it may be retrieved through a third party vendor. For more information, see [Energy efficiency information](/api-docs/sell/static/inventory/energy-efficiency.html).  
**Note:** Energy efficiency information is not required for all categories. Use the [getRegulatoryPolicies](/develop/api/sell/metadata_api#sell-metadata_api-marketplace-getregulatorypolicies) method of the **Metadata API** to return metadata on the eBay categories that recommend or require energy efficiency-related fields.  

**Important!** When providing energy efficiency information on an appliance or smartphones and tablets listing, the energy efficiency **rating** and **range** of the item must be specified through the [aspects](develop/api/sell/inventory_api#sell-inventory_api-inventory_item-createorreplaceinventoryitem.product.aspects) field when creating the inventory item record. Use the [getItemAspectsForCategory](/develop/api/sell/taxonomy_api#sell-taxonomy_api-category_tree-getitemaspectsforcategory) method of the Taxonomy API to retrieve applicable rating and range values for a specified category.
- **hazmat** (Hazmat)
  - This container is used by the seller to provide hazardous material information for the listing.  
  
The **statements** element is required to complete the Hazmat section of a listing.  
  
The following elements are optional:

*   **pictograms**
*   **signalWord**
*   **component**

**Note:** Hazmat information is not required for all categories. Use the [getRegulatoryPolicies](/develop/api/sell/metadata_api#sell-metadata_api-marketplace-getregulatorypolicies) method of the **Metadata API** to return metadata on the eBay categories that recommend or require Hazmat-related fields.
- **manufacturer** (Manufacturer)
  - This container provides information about the manufacturer of the item.  
  
**Note:** As a part of General Product Safety Regulation (GPSR) requirements effective on December 13th, 2024, sellers operating in, or shipping to, EU-based countries or Northern Ireland are conditionally required to provide regulatory manufacturer information in their eBay listings. Manufacturer information is not required for all categories. Use the [getRegulatoryPolicies](/develop/api/sell/metadata_api#sell-metadata_api-marketplace-getregulatorypolicies) method of the **Metadata API** to return metadata on the eBay categories that recommend or require manufacturer-related fields. For more information on GPSR, see [General Product Safety Regulation (GPSR)](https://www.ebay.com/sellercenter/resources/general-product-safety-regulation).
- **productSafety** (ProductSafety)
  - This container is used to provide product safety information for the listing. One of the following elements is required to complete the Product Safety section for a listing: **pictograms** or **statements**. The **component** element is optional.  
  
**Note:** As a part of General Product Safety Regulation (GPSR) requirements effective on December 13th, 2024, sellers operating in, or shipping to, EU-based countries or Northern Ireland are conditionally required to provide regulatory product safety information in their eBay listings. Product safety information is not required for all categories. Use the [getRegulatoryPolicies](/develop/api/sell/metadata_api#sell-metadata_api-marketplace-getregulatorypolicies) method of the **Metadata API** to return metadata on the eBay categories that recommend or require product safety-related fields. For more information on GPSR, see [General Product Safety Regulation (GPSR)](<https://www.ebay.com/sellercenter/resources/general-product-safety-regulation >).
- **repairScore** (number)
  - This field represents the repair index for the listing.  
  
The repair index identifies the manufacturer's repair score for a product (i.e., how easy is it to repair the product). This field is a floating point value between 0.0 (i.e., difficult to repair) and 10.0 (i.e., easily repaired).  
  
**Note:** `0` should not be used as a default value, as it implies the product is not repairable.  
The format for **repairScore** is limited to one decimal place. For example:

*   `7.9` and `0.0` are both valid scores
*   `5.645` and `2.10` are both invalid scores

  
**Note:** Repair score is not applicable to all categories. Use the [getExtendedProducerResponsibilityPolicies](/develop/api/sell/metadata_api#sell-metadata_api-marketplace-getextendedproducerresponsibilitypolicies) method of the **Metadata API** to see where repair score is applicable.
- **responsiblePersons** (array)
  - This container provides information about the EU-based Responsible Persons or entities associated with the listing.  
  
A maximum of 5 EU Responsible Persons are supported.  
  
**Note:** As a part of General Product Safety Regulation (GPSR) requirements effective on December 13th, 2024, sellers operating in, or shipping to, EU-based countries or Northern Ireland are conditionally required to provide regulatory Responsible Persons information in their eBay listings. For more information on GPSR, see [General Product Safety Regulation (GPSR)](<https://www.ebay.com/sellercenter/resources/general-product-safety-regulation >).

### ResponsiblePerson
**Description:** This type provides information, such as name and contact details, for an EU-based Responsible Person or entity, associated with the product.
**Type:** object

**Properties:**
- **addressLine1** (string)
  - The first line of the Responsible Person's street address.  
  
**Maximum length**: 180 characters
- **addressLine2** (string)
  - The second line of the Responsible Person's address. This field is not always used, but can be used for secondary address information such as 'Suite Number' or 'Apt Number'.  
  
**Maximum length**: 180 characters
- **city** (string)
  - The city of the Responsible Person's street address.  
  
**Maximum length**: 64 characters
- **companyName** (string)
  - The name of the Responsible Person or entity.  
  
**Maximum length**: 100 characters
- **contactUrl** (string)
  - The contact URL of the Responsible Person or entity.  
  
**Maximum length**: 250 characters
- **country** (CountryCodeEnum)
  - This defines the list of valid country codes, adapted from [ISO 3166-1](http://www.iso.org/iso/country_codes) country codes. List elements take the form of a two-letter code (Alpha-2), a three-letter code (Alpha-3), and a three-digit code (Numeric). For example, the entry for Japan includes JP, JPN, 392. Short codes provide uniform recognition, avoiding language-dependent country names. The numeric code is helpful where Latin script may be problematic. Not all listed codes are universally recognized as countries. For example, Antarctica is AQ, ATA, 010.
- **email** (string)
  - The Responsible Person's email address.  
  
**Maximum length**: 180 characters
- **phone** (string)
  - The Responsible Person's business phone number.  
  
**Maximum length**: 64 characters
- **postalCode** (string)
  - The postal code of the Responsible Person's street address.  
  
**Maximum length**: 9 characters
- **stateOrProvince** (string)
  - The state of province of the Responsible Person's street address.  
  
**Maximum length**: 64 characters
- **types** (array)
  - The type(s) associated with the Responsible Person or entity.  
  
**Note:** Currently, the only supported value is `EUResponsiblePerson`.

### ResponsiblePersonTypeEnum
**Description:** This enumeration type is used to indicate the type of EU Responsible Person associated with a listing. | - **EU_RESPONSIBLE_PERSON**: This enum value indicates the Responsible person is an EU Responsible Person. An EU Responsible Person is crucial for ensuring that products comply with all relevant regulations and safety standards to protect human health.
**Type:** object

### SameDayShippingCutOffTimes
**Description:** This type is used by the **createInventoryLocation** call to specify cut-off time(s) for an inventory location, as well as any overrides for these times.
**Type:** object

**Properties:**
- **overrides** (array)
  - This container can be used to override the existing cut-off time(s), specified in the **weeklySchedule** container, for a specific date or date range.
- **weeklySchedule** (array)
  - This container is used to specify the weekly schedule for shipping and handling cut-off times. A cut-off time is required for each business day that the fulfillment center operates. Any orders made after the specified **cutOffTime** on the specified day(s) of the week will be handled on the next day.

### ShippingCostOverride
**Description:** This type is used if the seller wants to override the shipping costs or surcharge associated with a specific domestic or international shipping service option defined in the fulfillment listing policy that is being applied toward the offer. The shipping-related costs that can be overridden include the shipping cost to ship one item, the shipping cost to ship each additional item (if multiple quantity are purchased), and the shipping surcharge applied to the shipping service option.
**Type:** object

**Properties:**
- **additionalShippingCost** (Amount)
  - The dollar value passed into this field will override the additional shipping cost that is currently set for the applicable shipping service option. The "Additional shipping cost" is the cost to ship each additional identical product to the buyer using the corresponding shipping service. The shipping service option in the fulfillment policy to override is controlled by the **shippingServiceType** and **priority** values.  
  
If using an **updateOffer** call, and this field is defined for the offer being updated, this field must be supplied again, even if its value is not changing.  
  
This field is returned in the [getOffer](/develop/api/sell/inventory_api#sell-inventory_api-offer-getoffer) and [getOffers](/develop/api/sell/inventory_api#sell-inventory_api-offer-getoffers) calls if defined.
- **priority** (integer)
  - The integer value input into this field, along with the **shippingServiceType** value, sets which domestic or international shipping service option in the fulfillment policy will be modified with updated shipping costs. Specifically, the **shippingCostOverrides.shippingServiceType** value in a **createOffer** or **updateOffer** call must match the **shippingOptions.optionType** value in a fulfillment listing policy, and the **shippingCostOverrides.priority** value in a **createOffer** or **updateOffer** call must match the **shippingOptions.shippingServices.sortOrderId** value in a fulfillment listing policy.  
  
This field is always required when overriding the shipping costs of a shipping service option, and will be always be returned for each shipping service option whose costs are being overridden.
- **shippingCost** (Amount)
  - The dollar value passed into this field will override the shipping cost that is currently set for the applicable shipping service option. This value will be the cost to ship one item to the buyer using the corresponding shipping service. The shipping service option in the fulfillment policy to override is controlled by the **shippingServiceType** and **priority** values.  
  
If using an **updateOffer** call, and this field is defined for the offer being updated, this field must be supplied again, even if its value is not changing.  
  
This field is returned in the [getOffer](/develop/api/sell/inventory_api#sell-inventory_api-offer-getoffer) and [getOffers](/develop/api/sell/inventory_api#sell-inventory_api-offer-getoffers) calls if defined.
- **shippingServiceType** (ShippingServiceTypeEnum)
  - This enumerated value indicates whether the shipping service specified in the **priority** field is a domestic or an international shipping service option. To override the shipping costs for a specific domestic shipping service in the fulfillment listing policy, this field should be set to `DOMESTIC`, and to override the shipping costs for each international shipping service, this field should be set to `INTERNATIONAL`. This value, along with **priority** value, sets which domestic or international shipping service option in the fulfillment policy that will be modified with updated shipping costs. Specifically, the **shippingCostOverrides.shippingServiceType** value in a **createOffer** or **updateOffer** call must match the **shippingOptions.optionType** value in a fulfillment listing policy, and the **shippingCostOverrides.priority** value in a **createOffer** or **updateOffer** call must match the **shippingOptions.shippingServices.sortOrderId** value in a fulfillment listing policy.  
  
This field is always required when overriding the shipping costs of a shipping service option, and will be always be returned for each shipping service option whose costs are being overridden.
- **surcharge** (Amount)
  - **Note:** DO NOT USE THIS FIELD. Shipping surcharges for shipping service options can no longer be set with fulfillment business policies. To set a shipping surcharge for a shipping service option, only the **Shipping rate tables** tool in My eBay can be used.  
The dollar value passed into this field will override the shipping surcharge that is currently set for the applicable shipping service option. The shipping service option in the fulfillment policy to override is controlled by the **shippingServiceType** and **priority** values.  
  
If using an **updateOffer** call, and this field is defined for the offer being updated, this field must be supplied again, even if its value is not changing.  
  
This field is returned in the [getOffer](/develop/api/sell/inventory_api#sell-inventory_api-offer-getoffer) and [getOffers](/develop/api/sell/inventory_api#sell-inventory_api-offer-getoffers) calls if defined.

### ShippingServiceTypeEnum
**Description:** This enumeration type is used to specify/indicate whether the shipping service option whose shipping costs will be overridden is a domestic or an international shipping service. | - **DOMESTIC**: This enumeration value indicates that the shipping service option whose shipping costs will be overridden is a domestic shipping service. - **INTERNATIONAL**: This enumeration value indicates that the shipping service option whose shipping costs will be overridden is an international shipping service.
**Type:** object

### SoldOnEnum
**Description:** This enumeration type is used to indicate if the product was sold for the price in the **originalRetailPrice** field on an eBay site, or sold for that price by a third-party retailer. This type is only applicable if the seller and listing are eligible to use the Strikethrough Pricing feature, a feature which is limited to the US (core site and Motors), UK, Germany, Canada (English and French versions), France, Italy, and Spain. | - **ON_EBAY**: This enumeration value indicates that the product was sold for the price in the **originalRetailPrice** field on an eBay site. - **OFF_EBAY**: This enumeration value indicates that the product was sold for the **originalRetailPrice** through a third-party retailer. - **ON_AND_OFF_EBAY**: This enumeration value indicates that the product was sold for the **originalRetailPrice** on an eBay site and through a third-party retailer.
**Type:** object

### SpecialHours
**Description:** **Deprecated.** Do not use as STORE location types are no longer supported.
**Type:** object

**Properties:**
- **date** (string)
  - A **date** value is required for each specific date that the store location has special operating hours or is closed for that date.  
  
The timestamp is formatted as an [ISO 8601](<https://www.iso.org/iso-8601-date-and-time-format.html > "https://www.iso.org ") string, which is based on the 24-hour Coordinated Universal Time (UTC) clock.  
  
**Format:** `[YYYY]-[MM]-[DD]T[hh]:[mm]:[ss].[sss]Z`  
**Example:** `2025-08-04T00:00:00.000Z`  
  
This field is returned if set for the store location.
- **intervals** (array)
  - This array is used to set the operating hours for the date specified in the corresponding **date** field. These special operating hours on this specific date will override the normal operating hours for that day of the week that is specified through the **operatingHours** array.  
  
To specify a location as closed on the corresponding **date**, include the **intervals** array as empty.  
  
If a location closes for lunch (or any other period during the day) and then reopens, multiple **open** and **close** pairs are needed to specify each interval where the location is open.  
  
This container is returned if set for the store location.

### Specification
**Description:** This type is used to specify product aspects for which variations within an inventory item group vary, and the order in which they appear in the listing. For example, t-shirts in an inventory item group may be available in multiple sizes and colors.
**Type:** object

**Properties:**
- **name** (string)
  - This is the name of product variation aspect. Typically, for clothing, typical aspect names are `"Size"` and `"Color"`. Product variation aspects are not required immediately upon creating an inventory item group, but these aspects will be required before a multiple-variation listing containing this inventory item group is published. For each product variation aspect that is specified through the **specifications** container, one **name** value is required and two or more variations of this aspect are required through the **values** array.  
  
**Note:** Each member of the inventory item group should have these same aspect names specified through the **product.aspects** container when the inventory item is created with the **createOrReplaceInventoryItem** or **bulkCreateOrReplaceInventoryItem** call.  

**Important!**Publish offer note: This field is required before an offer can be published to create an active listing.

  
**Maximum length**: 40
- **values** (array)
  - This is an array of values pertaining to the corresponding product variation aspect (specified in the **name** field). Below is a sample of how these values will appear under a **specifications** container:  

"specifications": \[{  
 "name": "Size",  
 "values": \["Small",  
 "Medium",  
 "Large"\]  
 },  
 {   
 "name": "Color",  
 "values": \["Blue",  
 "White",  
 "Red"\]   
 }\] 

**Note:** Each member of the inventory item group should have these same aspect names, and each individual inventory item should have each variation of the product aspect values specified through the **product.aspects** container when the inventory item is created with the **createOrReplaceInventoryItem** or **bulkCreateOrReplaceInventoryItem** call.  

**Important!**Publish offer note: This array is required and at least one value that matches the corresponding aspect name must be specified.

  
**Maximum length**: 50

### StatusEnum
**Description:** An enumerated type defining the possible states of an inventory location. | - **DISABLED**: This enumeration value indicates that an inventory location is disabled (inventory cannot be loaded to location). - **ENABLED**: This enumeration value indicates that an inventory location is disabled (inventory can be loaded to location).
**Type:** object

### StoreTypeEnum
**Description:** An enumerated type defining the inventory location types. | - **STORE**: **Deprecated.** Do not use as STORE location types are no longer supported. - **WAREHOUSE**: This enumeration value indicates the inventory location is a merchant's warehouse. - **FULFILLMENT_CENTER**: This enumeration value indicates the inventory location is a merchant's fulfillment center.  
  
**Note**: This location type must be used to take advantage of the Multi-warehouse program to get improved EDD on listing.
**Type:** object

### Tax
**Description:** This type is used to enable the use of a sales-tax table, to pass in a tax exception category code, or to specify a VAT percentage.  
  
**Note:** Sales-tax tables are available only for the US and Canada marketplaces.
**Type:** object

**Properties:**
- **applyTax** (boolean)
  - When set to `true`, the seller's account-level sales-tax table will be used to calculate sales tax for an order.  
  
**Note:** Sales-tax tables are available only for the US and Canada marketplaces.  

**Important!** In the US, eBay now calculates, collects, and remits sales tax to the proper taxing authorities in all 50 states and Washington, DC. Sellers can no longer specify sales-tax rates for these jurisdictions using a tax table.  
  
However, sellers may continue to use a sales-tax table to set rates for the following US territories:

*   American Samoa (AS)
*   Guam (GU)
*   Northern Mariana Islands (MP)
*   Palau (PW)
*   US Virgin Islands (VI)

  
For complete information about using sales-tax tables, refer to [Establishing sales-tax tables](/api-docs/sell/static/seller-accounts/tax-tables.html).  
  
Note that a seller can enable the use of a sales-tax table, but if a sales-tax rate is not specified for the buyer's tax jurisdiction, sales tax will not be applied to the order.  
  
When a `thirdPartyTaxCategory` value is used, `applyTax` must also be set to `true`.  
  
This field will be returned by [getOffer](/develop/api/sell/inventory_api#sell-inventory_api-offer-getoffer) and [getOffers](/develop/api/sell/inventory_api#sell-inventory_api-offer-getoffers) if set for the offer.  
  
For additional information, refer to [Taxes and import charges](<https://www.ebay.com/help/selling/fees-credits-invoices/taxes-import-charges?id=4121 >).
- **thirdPartyTaxCategory** (string)
  - The tax exception category code. If this field is used, sales tax will also apply to a service/fee, and not just the item price. This is to be used only by sellers who have opted into sales tax being calculated by a sales tax calculation vendor. If you are interested in becoming a tax calculation vendor partner with eBay, contact [developer-relations@ebay.com](<mailto:developer-relations@ebay.com >). One supported value for this field is `WASTE_RECYCLING_FEE`. If this field is used, the **applyTax** field must also be used and set to `true`  
  
This field will be returned by [getOffer](/develop/api/sell/inventory_api#sell-inventory_api-offer-getoffer) and [getOffers](/develop/api/sell/inventory_api#sell-inventory_api-offer-getoffers) if set for the offer.
- **vatPercentage** (number)
  - This value is the Value Add Tax (VAT) rate for the item, if any. When a VAT percentage is specified, the item's VAT information appears on the listing's View Item page. In addition, the seller can choose to print an invoice that includes the item's net price, VAT percent, VAT amount, and total price. Since VAT rates vary depending on the item and on the user's country of residence, a seller is responsible for entering the correct VAT rate; it is not calculated by eBay.  
  
To use VAT, a seller must be a business seller with a VAT-ID registered with eBay, and must be listing the item on a VAT-enabled site. Max applicable length is 6 characters, including the decimal (e.g., 12.345). The scale is 3 decimal places. (If you pass in 12.3456, eBay may round up the value to 12.346).  
  
This field will be returned by [getOffer](/develop/api/sell/inventory_api#sell-inventory_api-offer-getoffer) and [getOffers](/develop/api/sell/inventory_api#sell-inventory_api-offer-getoffers) if set for the offer.

### VariesBy
**Description:** This type is used to specify the product aspect(s) where individual items of the group vary, as well as a list of the available variations of those aspects.
**Type:** object

**Properties:**
- **aspectsImageVariesBy** (array)
  - Use this container when the seller wants to include multiple images to demonstrate how variations within a multiple-variation listing differ. In this array, specify the product aspect used to drive the image variation, such as `Color`. If `Color` is specified in this field, `Color` must also be one of the **specifications.name** values, and all available colors must appear in the corresponding **specifications.values** array.  
  
If this container is used, provide links to images of each variation through the **imageUrls** container of the inventory item group, or the seller can choose to include those links to images in each inventory item record for the inventory items in the group.  
  

**Note:** Only the first aspect in the array is used to determine image variation. Additional aspects in the array are ignored; effectively, this field supports only one aspect.

  
  

**Important!**Publish offer note: This array is required and at least one aspect (such as `Color`) must be specified before an offer can be published to create an active listing.
- **specifications** (array)
  - This container consists of an array of one or more product aspects where each variation differs, and values for each of those product aspects. This container is not immediately required, but will be required before the first offer of the inventory item group is published.  
  
If a product aspect is specified in the **aspectsImageVariesBy** container, this product aspect (along with all variations of that product aspect) must be included in the **specifications** container. Before offers related to the inventory item group are published, the product aspects and values specified through the **specifications** container should be in synch with the name-value pairs specified through the **product.aspects** containers of the inventory items contained in the group. For example, if `Color` and `Size` are in this **specifications** container, each inventory item of the group should also have `Color` and `Size` as aspect names in their inventory item records.  
  
This container is always returned if one or more offers associated with the inventory item group have been published. For inventory item groups that have yet to have any published offers, this container is only returned if set.  
  

**Important!**Publish offer note: This array is required and at least one aspect with the available variations must be specified.

### WeeklySchedule
**Description:** This type describes the weekly schedule for cut-off times.
**Type:** object

**Properties:**
- **cutOffTime** (string)
  - This field specifies the cut-off times (in 24-hour format) for the business day(s) specified in the **dayOfWeekEnum** array.  
  
Cut-off times default to the time zone of the specified address if the **timeZoneId** is not provided.  
  
**Note:** If cut-off hours are not specified for a particular day, the fulfillment center is considered to be on holiday for that day.  
**Format:** `00:00`
- **dayOfWeekEnum** (array)
  - This comma-separated array defines the days of week for which the specified **cutOffTime** is used.

### WithdrawByInventoryItemGroupRequest
**Description:** This type is used by the base request of the **WithdrawByInventoryItemGroup** method, which is used to end a multiple-variation listing.
**Type:** object

**Properties:**
- **inventoryItemGroupKey** (string)
  - This is the unique identifier of the inventory item group. This identifier is automatically generated by eBay once an inventory item group is created.  
  
To retrieve an **inventoryItemGroupKey** value, you can use the [getInventoryItem](/develop/api/sell/inventory_api#sell-inventory_api-inventory_item-getinventoryitem) method to retrieve an inventory item that is known to be in the inventory item group to publish, and then look for the inventory item group identifier under the **groupIds** container in the response of that call.
- **marketplaceId** (MarketplaceEnum)
  - This is the unique identifier of the eBay site for which the offer will be made available. See **MarketplaceEnum** for supported values.

### WithdrawResponse
**Description:** The base response of the **withdrawOffer** call.
**Type:** object

**Properties:**
- **listingId** (string)
  - The unique identifier of the eBay listing associated with the offer that was withdrawn. This field will not be returned if the eBay listing was not successfully ended.
- **warnings** (array)
  - This container will be returned if there were one or more warnings associated with the attempt to withdraw the offer.

## Rate Limits

See [API Call Limits](https://developer.ebay.com/develop/get-started/api-call-limits) on the eBay Developer Program.

## Resources

### Documentation

- [eBay Developer Program](https://developer.ebay.com/)
- [API Documentation](https://developer.ebay.com/develop/api/)
- [SDKs and Widgets](https://developer.ebay.com/develop/sdks-and-widgets)
- [Developer Community Forum](https://community.ebay.com/t5/Developer-Groups/ct-p/developergroup)

### Tools

- [API Explorer](https://developer.ebay.com/my/api_test_tool)
- [GraphQL Explorer](https://developer.ebay.com/my/graphql_explorer)

### Support

- [Developer Support](https://developer.ebay.com/support/)
- [API Status](https://developer.ebay.com/support/api-status)
- [Release Notes](https://developer.ebay.com/develop/api/release_notes/)

---
*Generated on 2026-09-28T16:26:57.508Z*