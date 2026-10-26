---
title: Browse API
description: "The **Browse API** lets shoppers search eBay listings by keyword, category, GTIN, product, charity, compatibility criteria, or image, and refine results with filters such as aspects, compatibility, field values, and UI parameters through the **item\\_summary** resource. The **item** resource lets applications retrieve detailed information for a specific item or all items in an item group, and check whether a product is compatible with a specified item, such as whether a specific vehicle is compatible with a specific part. The **item** resource also supports legacy item identifiers alongside RESTful item IDs, which use different formats. This helps developers work with stored or historical legacy item IDs when using the **Browse API**. All methods in the **Browse API** require an Application access token, which is obtained using the [client credentials grant flow](/develop/guides-v2/authorization#the-client-credentials-grant-flow)."
api_version: 1.0
api_name: browse_api
api_type: REST
api_group: buy/browse_api
source_url:
  html: https://developer.ebay.com/develop/api/buy/browse_api
  md: https://developer.ebay.com/develop/api/buy/browse_api.md
---

# Browse API API

The **Browse API** lets shoppers search eBay listings by keyword, category, GTIN, product, charity, compatibility criteria, or image, and refine results with filters such as aspects, compatibility, field values, and UI parameters through the **item\_summary** resource.  
  
The **item** resource lets applications retrieve detailed information for a specific item or all items in an item group, and check whether a product is compatible with a specified item, such as whether a specific vehicle is compatible with a specific part. The **item** resource also supports legacy item identifiers alongside RESTful item IDs, which use different formats. This helps developers work with stored or historical legacy item IDs when using the **Browse API**.  
  
All methods in the **Browse API** require an Application access token, which is obtained using the [client credentials grant flow](/develop/guides-v2/authorization#the-client-credentials-grant-flow).

## API Methods

The following API methods are available:

### search

#### GET /item_summary/search
**Description:** This method searches for eBay items by various query parameters and retrieves summaries of the items. You can search by keyword, category, eBay product ID (ePID), or GTIN, charity ID, or a combination of these.  
  
**Note:** Only listings where `FIXED_PRICE` (Buy It Now) is a buying option are returned by default. To retrieve listings that do not have `FIXED_PRICE` as a buying option, the `buyingOptions` filter can be used to retrieve those listings.  
  
Note that an auction listing enabled with the _Buy it Now_ feature will initially show `AUCTION` and `FIXED_PRICE` as buying options, but if/when that auction listing receives a qualifying bid, only `AUCTION` remains as a buying option. If this happens, the `buyingOptions` filter would need to be used to retrieve that auction listing.  
This method also supports the following:

*   Filtering by the value of one or multiple fields, such as listing format, item condition, price range, location, and more. For the fields supported by this method, refer to the **filter** parameter.
*   Retrieving the refinements (metadata) of an item, such as item aspects (color, brand) condition, category, etc. using the **fieldgroups** parameter.
*   Filtering by item aspects and other refinements using the **aspect\_filter** parameter.
*   Filtering for items that are compatible with a specific product, using the **compatibility\_filter** parameter.
*   Creating aspects histograms, which enables shoppers to drill down in each refinement narrowing the search results.

For additional information and examples of these capabilities, refer to [Browse API](/api-docs/buy/static/api-browse.html) in the Buying Integration Guide.  
  
**Pagination and sort controls**  
There are pagination controls (**limit** and **offset** fields) and **sort** query parameters that control/sort the data that are returned. By default, results are sorted by _Best Match_. For more information about Best Match, refer to [Best Match](<https://pages.ebay.com/help/sell/searchstanding.html >).  
  
**Restrictions**  
This method can return a maximum of 10,000 items. For a list of supported sites and other restrictions, refer to [Buy APIs Requirements](/api-docs/buy/static/buy-requirements.html).  
  
**eBay Partner Network:** In order to receive a commission for your sales, you must use the URL returned in the `itemAffiliateWebUrl` field to forward your buyer to the ebay.com site.
**Parameters:**
- **aspect_filter** (string)
  - This field lets you filter by item aspects. The aspect name/value pairs and category, which is required, is used to limit the results to specific aspects of the item. For example, in a clothing category one aspect pair would be Color/Red.  
  
**Note:** The category ID must be specified _twice_:

*   Once as a URI parameter in the `category_ids` field
*   Once as part of the `aspect_filter` field

These two values **must** be the same.  
For example, to return items for a woman's red shirt, issue the following request:  

/buy/browse/v1/item\_summary/search?q=shirt&category\_ids=15724&aspect\_filter=categoryId:15724,Color:{Red}

To get a list of the aspect pairs and the category, which is returned in the `dominantCategoryId` field, set `fieldgroups` to `ASPECT_REFINEMENTS` as illustrated here:

/buy/browse/v1/item\_summary/search?q=shirt&fieldgroups=ASPECT\_REFINEMENTS

**Note:** The pipe symbol is used as a delimiter between aspect filter values. If a value contains a pipe symbol (for example, the brand name 'Bed|StÃ¼'), you must enter a backslash before the pipe character to prevent it from being evaluated as a delimiter.  
  
The following example illustrates the correct format for entering two brand names as aspect filter values, one of which contains a pipe symbol:

/buy/browse/v1/item\_summary/search?limit=50&category\_ids=3034&filter=buyingOptions:{AUCTION|FIXED\_PRICE}&aspect\_filter=categoryId:3034,Brand:{Bed\\|StÃ¼|Nike}
- **auto_correct** (string)
  - A query parameter that enables auto correction.  
  
A sample is shown below:

/buy/browse/v1/item\_summary/search?auto\_correct=KEYWORD

**Note:** Auto correction is currently supported in the following marketplaces:

*   United States
*   Austria
*   Australia
*   Canada
*   Switzerland
*   Germany
*   Spain
*   France
*   United Kingdom
*   Ireland
*   Italy

  
**Valid Values:** `KEYWORD`
- **category_ids** (string)
  - The category ID is used to limit the results that are returned. This field may pass in one category ID or a comma separated list of IDs as illustrated in the following examples:

/buy/browse/v1/item\_summary/search?category\_ids=29792

/buy/browse/v1/item\_summary/search?category\_ids=267,29792

**Note:** Currently, you can pass in only one category ID per request.  
To refine the set of information that is returned, `category_ids` may be combined with **EITHER**:

*   `epid` and/or `gtin` values
*   `q` keywords

For example, when looking of a toy phone, simply searching for "phone" will return mobile phones because that is the "Best Match" for the search. To further refine the request to include toy phones, include the **Toys & Hobbies** category ID as illustrated here:

/buy/browse/v1/item\_summary/search?q=phone&category\_ids=220

Because the list of eBay category IDs is not published and category IDs are not the same across all eBay marketplaces, category IDs may be determined by:

*   Visiting the [Category Changes page](<https://pages.ebay.com/sellerinformation/news/categorychanges.html >)
*   Using the Taxonomy API. Refer to [Get Categories for Buy APIs](/api-docs/buy/buy-categories.html) for complete information.
*   Issuing the following call to retrieve the `dominantCategoryId` for an item:
    
    /buy/browse/v1/item\_summary/search?q= _keyword_&fieldgroups=ASPECT\_REFINEMENTS
    

**Note:** If a top-level (L1) category is specified, you **must** also include a `q` query parameter.
- **charity_ids** (string)
  - The charity ID filters results to return only those items associated with the specified charity.  
  
**Note:** `charity_ids` is only supported by the US and UK marketplaces.  
Charity ID is a charity's unique identification number:

*   In the US, this is the **Employer Identification Number (EIN)**.
*   In the UK, this is the Charity Registration Number (CRN), commonly called **Charity Number**.

  
`charity_ids` may be retrieved/determined as follows:

*   Search for a supported charity using the Charity API's [getCharityOrgs](/api-docs/commerce/charity/resources/charity_org/methods/getCharityOrgs) method.  
      
    
    **Important!** The value to be passed in as `charity_ids` is that returned in the `registrationId` field.
    
*   Search for a supported charity by visiting [Charity Search](<https://charity.ebay.com/search >). Click on the charity's name to display its information. The EIN number is included in the charity's information block at the top of the page.  
      
    For example, the charity ID for [American Red Cross](<https://charity.ebay.com/charity/American-Red-Cross/3843 >), is `530196605`.

Up to 20 comma-separated `charity_ids` may be specified in each query. Additionally, `charity_ids` may be combined with `category_ids` and/or `q` keyword values to further filter returned results.  
  
A sample query using `charity_ids` is:  

/buy/browse/v1/item\_summary/search?charity\_ids=13-1788491,300108469
- **compatibility_filter** (string)
  - This field specifies the attributes used to define a specific product. The service searches for items matching the keyword, or matching the keyword and a product attribute value in the title of the item.  
  
**Note:** The only products supported are cars, trucks, and motorcycles.  
For example, if the keyword is `brakes` and `compatibility-filter=Year:2018;Make:BMW`, the items returned are items with **brakes**, **2018**, or **BMW** in the title.  
  
The service uses the product attributes to determine whether the item is compatible. The service returns the attributes that are compatible and the [CompatibilityMatchEnum](/develop/api/buy/browse_api#buy-browse_api-item_summary-search.itemsummary.compatibilitymatch) value that indicates how well the item matches the attributes.  
  

**Tip:** Refer to the **Samples** for a detailed example.

  
**Best Practice:** Submit all of the [product attributes](/api-docs/buy/static/api-browse.html#product-attributes) for the specific product.  
  
To find the attributes and values for a specific marketplace, use the [getCompatibilityProperties](/api-docs/commerce/taxonomy/resources/category_tree/methods/getCompatibilityProperties) method in the [Taxonomy API](/api-docs/commerce/taxonomy/resources/methods).  
  
For more information, refer to [Check compatibility](/api-docs/buy/static/api-browse.html#Check) in the Buying Integration Guide.  
  
**Note:** Testing in Sandbox is only supported using mock data. Refer to [Testing search in the Sandbox](/api-docs/buy/static/api-browse.html#sbox-test) for details.  
**Required:**

*   `q` (keyword)
*   One parts-compatibility-supported category ID (such as `33559` Brakes)
*   At least one [vehicle attribute](/api-docs/buy/static/api-browse.html#product-attributes) name/value pair
- **epid** (string)
  - The ePID is the eBay product identifier of a product from the eBay product catalog. This field limits the results to only items in the specified ePID.  
  
Use the [product\_summary/search](/api-docs/commerce/catalog/resources/product_summary/methods/search) method in the [Catalog](/api-docs/commerce/catalog/overview.html) API to search for the ePID of the product.  
  
For example:

/buy/browse/v1/item\_summary/search?epid=15032

**Note:** When constructing a query, `epid` may be combined with a `gtin` value. However, _do not_ specify keywords using the `q` parameter â keywords cannot be used in conjunction with an `epid`.
- **fieldgroups** (string)
  - A comma-separated list of values that controls what is returned in the response. The default is `MATCHING_ITEMS`, which returns the items that match the keyword or category specified. The other values return data that can be used to create histograms or provide additional information.  
  
**Valid Values:**

*   `ASPECT_REFINEMENTS`  
    This field group adds the [aspectDistributions](/develop/api/buy/browse_api#buy-browse_api-item_summary-search.refinement.aspectdistributions) container to the response.  
      
    **Note:** Information returned by `ASPECT_REFINEMENTS` is category specific.
*   `BUYING_OPTION_REFINEMENTS`  
    This field group adds the [buyingOptionDistributions](/develop/api/buy/browse_api#buy-browse_api-item_summary-search.refinement.buyingoptiondistributions) container to the response.
*   `CATEGORY_REFINEMENTS`  
    This field group adds the [categoryDistributions](/develop/api/buy/browse_api#buy-browse_api-item_summary-search.refinement.categorydistributions) container to the response.
*   `CONDITION_REFINEMENTS`  
    This field group adds the [conditionDistributions](/develop/api/buy/browse_api#buy-browse_api-item_summary-search.refinement.conditiondistributions) containers, such as `NEW`, `USED`, etc., to the response. Within these groups are multiple states of the condition.  
      
    For example, `NEW` can be _New without tag_, _New in box_, _New without box_, etc.
*   `EXTENDED`  
    This field group adds the following fields to the response:
    *   [shortDescription](/develop/api/buy/browse_api#buy-browse_api-item_summary-search.itemsummary.shortdescription)
    *   [itemLocation.city](/develop/api/buy/browse_api#buy-browse_api-item_summary-search.itemlocationimpl.city)
*   `MATCHING_ITEMS` (**default value**)  
    This field group is intended to be used with one or more of the refinement values listed above. This is used to return the specified refinements and all matching items.
*   `FULL`  
    This field group returns all refinement containers and all matching items.

**Default:** `MATCHING_ITEMS`
- **filter** (string)
  - An array of field filters that can be used to limit/customize the result set.  
  
Refer to [Buy API Field Filters](/api-docs/buy/static/ref-buy-browse-filters.html) for additional information and examples of all supported filters.  
  
For example, to filter shirts based on a specific range of prices, include the filter illustrated here:

/buy/browse/v1/item\_summary/search?q=shirt&filter=price:\[10..50\]

Filters may also be combined within a single request as illustrated in the sample below which further refines results to return only those shirts available from specific sellers:

/buy/browse/v1/item\_summary/search?q=shirt&filter=price:\[10..50\],sellers:{rpseller|bigSal}
- **gtin** (string)
  - This field lets you search for a product by specifying a Global Trade Item Number (GTIN) of the product. Supported GTIN types are UPC, EAN, and ISBN.  
  
For example:  

/buy/browse/v1/item\_summary/search?gtin=099482432621

**Note:** When constructing a query, `gtin` value may be combined with an `epid` value, but neither an `epid` or `gtin` value should be combined with a keywords search through the `q` parameter.
- **limit** (string)
  - The number of items from the result set returned in a single page.  
  
**Note:** If a value is set in the `limit` field, the value of `offset` must be either zero or a multiple of the `limit` value. An error is returned for invalid `offset` values.  
**Note:** This method can return a maximum of 10,000 items in one results set.  
**Min:** 1  
  
**Max:** 200  
  
**Default:** 50
- **offset** (string)
  - Specifies the number of items to skip in the result set. This is used with the `limit` field to control the pagination of the output.  
  
For example:

*   If `offset` is 0 and `limit` is 10, the method will retrieve items 1-10 from the list of items returned
*   If `offset` is 10 and `limit` is 10, the method will retrieve items 11-20 from the list of items returned.

**Note:** The value of `offset` must be either zero or a multiple of the value set in the `limit` field. An error is returned for invalid `offset` values.  
**Note:** This method can return a maximum of 10,000 items in one results set.  
**Min**: 0  
  
**Max:** 9,999  
  
**Default:** 0
- **q** (string)
  - A string consisting of one or more keywords used to search for items on eBay.  
  
**Note:** The `*` wildcard character is **not** allowed in this field.  
When providing two or more keywords in a single query, the string is processed as follows:

*   When successive keywords are separated by a space, the list of keywords is processed as an `AND` request. For example, to retrieve items that include **both** of the keywords **iphone** AND **ipad**, submit the following query:  
    
    /buy/browse/v1/item\_summary/search?q=iphone ipad
    
*   When successive keywords are comma-separated and surrounded by a single pair of parentheses, OR if the keywords are each URL-encoded, the list of keywords is processed as an `OR` request. For example, to retrieve items that include **iphone** OR **ipad**, submit one of the following queries:  
    
    /buy/browse/v1/item\_summary/search?q=(iphone, ipad)
    
    /buy/browse/v1/item\_summary/search?q=%28iphone%2c%20ipad%29
    

  
**Note:** When specifying keywords using the `q` parameter:

*   _Do not include_ an `epid` or `gtin` parameter value as neither can be used in conjunction with a keyword search.
*   Strings longer than 100-characters are truncated.

  
  
**Maximum length:** 100 characters
- **sort** (string)
  - Specifies the criteria on which returned items are to be sorted.  
  
Items can be sorted in ascending order based on:

*   Price (`sort=price`)  
    Returned items are sorted based on their total cost (i.e., _price + shipping cost_).  
      
    Items with the lowest combined price are shown first.  
      
    When sorting by price, it is highly recommended that:
    
    *   The `X-EBAY-C-ENDUSERCTX` request header is used, **and**
    *   The `contextualLocation` parameter specifies the delivery country and postal code.
      
    These values must be _URL-encoded_.
    
    Refer to the following example:
    
    X-EBAY-C-ENDUSERCTX: contextualLocation=country%3DUS%2Czip%3D19406
    
    **Descending price order**  
    To sort items from _highest price_ to _lowest price_ insert a minus sign (-) before `price` as the search criterion:
    
    sort=-price
    
*   Distance (`sort=distance`)  
    Returned items are sorted based on their distance from the buyer's location.  
      
    Items that are closest to the buyer are listed first.  
      
    
    **Important!** When sorting by distance, all required [pickup filters](/api-docs/buy/static/ref-buy-browse-filters.html#pickupCountry) must be included in the request.
    
*   Date  
    Items can be sorted by date based on:
    *   Listing date (`sort=newlyListed`)  
        Returned items are sorted based on their [itemOriginDate](/develop/api/buy/browse_api#buy-browse_api-item_summary-search.itemsummary.itemorigindate).  
          
        Newly listed items are shown first.
    *   End date (`sort=endingSoonest`)  
        Returned items are sorted based on the date/time on which their listing is scheduled to end.  
          
        Items that are closest to their scheduled ending date/time are shown first.

If no sort parameter is submitted, the result set is sorted by "Best Match". Refer to [Optimizing your listings for Best Match](<https://www.ebay.com/help/selling/listings/listing-tips/optimising-listings-best-match?id=4166 >) for additional information.
- **X-EBAY-C-ENDUSERCTX** (string)
  - This header is required to support revenue sharing for eBay Partner Network and to improve the accuracy of shipping and delivery time estimations.  
  
For additional information, refer to [Use request headers](/api-docs/buy/static/api-browse.html#Headers) in the [Buying Integration Guide](/api-docs/buy/static/buying-ig-landing.html).
- **X-EBAY-C-MARKETPLACE-ID** (string)
  - This header identifies the seller's eBay marketplace. It is required for all marketplaces outside of the US.  
  
**Note:** If the marketplace ID value is invalid or missing, the default value of `EBAY_US` is used.  
See [MarketplaceIdEnum](/develop/api/buy/browse_api#buy-browse_api-item_summary-search.marketplaceidenum) for a list of supported marketplaces.  
  
**Default:** `EBAY_US`
- **Accept-Language** (string)
  - This header is used to indicate the natural language and locale preferred by the user for the response.  
  
This header is required when targeting a specific locale of a marketplace that supports multiple locales. For example:

*   When targeting the French locale of the Belgium marketplace, it is required to pass in `fr-BE` to specify this. If this locale is not specified, the language will default to Dutch.
*   When targeting the French locale of the Canadian marketplace, it is required to pass in `fr-CA` to specify this. If this locale is not specified, the language will default to English.

### searchByImage

#### POST /item_summary/search_by_image
**Description:** This method searches for eBay items based on a image and retrieves summaries of the items. You pass in a Base64 image in the request payload and can refine the search by category, or with other available filters.  
  
To get the Base64 image string, you can use sites such as [https://codebeautify.org/image-to-base64-converter](<https://codebeautify.org/image-to-base64-converter >).  
  
This method also supports the following:

*   Filtering by the value of one or multiple fields, such as listing format, item condition, price range, location, and more. For the fields supported by this method, refer to the **filter** parameter.
*   Filtering by item aspects using the **aspect\_filter** parameter.

For details and examples of these capabilities, refer to [Browse API](/api-docs/buy/static/api-browse.html) in the Buying Integration Guide.  
  
**URL Encoding for Parameters**  
Query parameter values need to be URL encoded. For details, refer to [URL encoding query parameter values](/api-docs/static/rest-request-components.html#parameters). For readability, code examples in this document have not been URL encoded.  
  
**Restrictions**  
This method can return a maximum of 10,000 items. For a list of supported sites and other restrictions, refer to [Buy APIs Requirements](/api-docs/buy/static/buy-requirements.html).  
  
**eBay Partner Network:** In order to receive a commission for your sales, you must use the URL returned in the `itemAffiliateWebUrl` field to forward your buyer to the ebay.com site.
**Parameters:**
- **aspect_filter** (string)
  - This field lets you filter by item aspects. The aspect name/value pairs and category, which is required, is used to limit the results to specific aspects of the item. For example, in a clothing category one aspect pair would be Color/Red.  
  
**Note:** The category ID must be specified _twice_:

*   Once as a URI parameter in the `category_ids` field
*   Once as part of the `aspect_filter` field

These two values **must** be the same.  
For example, to return items for a woman's red shirt, issue the following request:  

/buy/browse/v1/item\_summary/search\_by\_image?category\_ids=15724&aspect\_filter=categoryId:15724,Color:{Red}

To get a list of the aspect pairs and the category, which is returned in the `dominantCategoryId` field, set `fieldgroups` to `ASPECT_REFINEMENTS` as illustrated here:

/buy/browse/v1/item\_summary/search\_by\_image?fieldgroups=ASPECT\_REFINEMENTS

**Note:** The pipe symbol is used as a delimiter between aspect filter values. If a value contains a pipe symbol (for example, the brand name 'Bed|StÃ¼'), you must enter a backslash before the pipe character to prevent it from being evaluated as a delimiter.  
  
The following example illustrates the correct format for entering two brand names as aspect filter values, one of which contains a pipe symbol:

/buy/browse/v1/item\_summary/search\_by\_image?limit=50&category\_ids=3034&filter=buyingOptions:{AUCTION|FIXED\_PRICE}&aspect\_filter=categoryId:3034,Brand:{Bed\\|StÃ¼|Nike}
- **category_ids** (string)
  - The category ID is used to limit the results that are returned. This field may pass in one category ID or a comma separated list of IDs as illustrated in the following examples:

/buy/browse/v1/item\_summary/searchByImage?category\_ids=29792

/buy/browse/v1/item\_summary/searchByImage?category\_ids=267,29792

**Note:** Currently, you can pass in only one category ID per request.  
To refine the set of information that is returned, `category_ids` may be combined with other available filters.  
  
Because the list of eBay category IDs is not published and category IDs are not the same across all eBay marketplaces, category IDs may be determined by:

*   Visiting the [Category Changes page](<https://pages.ebay.com/sellerinformation/news/categorychanges.html >)
*   Using the Taxonomy API. Refer to [Get Categories for Buy APIs](/api-docs/buy/buy-categories.html) for complete information.
*   Issuing the following call to retrieve the `dominantCategoryId` for an item:
    
    /buy/browse/v1/item\_summary/searchByImage?fieldgroups=ASPECT\_REFINEMENTS
- **charity_ids** (string)
  - The charity ID filters results to return only those items associated with the specified charity.  
  
**Note:** `charity_ids` is only supported by the US and UK marketplaces.  
Charity ID is a charity's unique identification number:

*   In the US, this is the **Employer Identification Number (EIN)**.
*   In the UK, this is the Charity Registration Number (CRN), commonly called **Charity Number**.

  
`charity_ids` may be retrieved/determined as follows:

*   Search for a supported charity using the Charity API's [getCharityOrgs](</api-docs/commerce/charity/resources/charity_org/methods/getCharityOrgs >) method.  
      
    
    **Important!** The value to be passed in as `charity_ids` is that returned in the `registrationId` field.
    
*   Search for a supported charity by visiting [Charity Search](<https://charity.ebay.com/search >). Click on the charity's name to display its information. The EIN number is included in the charity's information block at the top of the page.  
      
    For example, the charity ID for [American Red Cross](<https://charity.ebay.com/charity/American-Red-Cross/3843 >), is `530196605`.

Up to 20 comma-separated `charity_ids` may be specified in each query. Additionally, `charity_ids` may be combined with `category_ids` values to further filter returned results.  
  
A sample query using `charity_ids` is:  

/buy/browse/v1/item\_summary/search\_by\_image?charity\_ids=13-1788491,300108469
- **fieldgroups** (string)
  - A comma-separated list of values that controls what is returned in the response. The default is `MATCHING_ITEMS`, which returns the items that match the keyword or category specified. The other values return data that can be used to create histograms or provide additional information.  
  
**Valid Values:**

*   `ASPECT_REFINEMENTS`  
    This field group adds the [aspectDistributions](/develop/api/buy/browse_api#buy-browse_api-item_summary-searchbyimage.refinement.aspectdistributions) container to the response.  
      
    **Note:** Information returned by `ASPECT_REFINEMENTS` is category specific.
*   `BUYING_OPTION_REFINEMENTS`  
    This field group adds the [buyingOptionDistributions](/develop/api/buy/browse_api#buy-browse_api-item_summary-searchbyimage.refinement.buyingoptiondistributions) container to the response.
*   `CATEGORY_REFINEMENTS`  
    This field group adds the [categoryDistributions](/develop/api/buy/browse_api#buy-browse_api-item_summary-searchbyimage.refinement.categorydistributions) container to the response.
*   `CONDITION_REFINEMENTS`  
    This field group adds the [conditionDistributions](/develop/api/buy/browse_api#buy-browse_api-item_summary-searchbyimage.refinement.conditiondistributions) containers, such as `NEW`, `USED`, etc., to the response. Within these groups are multiple states of the condition.  
      
    For example, `NEW` can be _New without tag_, _New in box_, _New without box_, etc.
*   `EXTENDED`  
    This field group adds the following fields to the response:
    *   [shortDescription](/api-docs/buy/browse/resources/item_summary/methods/search#response.itemSummaries.shortDescription)
    *   [itemLocation.city](/develop/api/buy/browse_api#buy-browse_api-item_summary-searchbyimage.itemlocationimpl.city)
*   `MATCHING_ITEMS` (**default value**)  
    This field group is intended to be used with one or more of the refinement values listed above. This is used to return the specified refinements and all matching items.
*   `FULL`  
    This field group returns all refinement containers and all matching items.

**Default:** `MATCHING_ITEMS`
- **filter** (string)
  - An array of field filters that can be used to limit/customize the result set.  
  
Refer to [Buy API Field Filters](/api-docs/buy/static/ref-buy-browse-filters.html) for the information about available filters.  
  
For example, to filter shirts based on a specific range of prices, include the filter illustrated here:

/buy/browse/v1/item\_summary/search\_by\_image?filter=price:\[10..50\]

Filters may also be combined within a single request as illustrated in the sample below which further refines results to return only those shirts available from specific sellers:

/buy/browse/v1/item\_summary/search\_by\_image?filter=price:\[10..50\],sellers:{rpseller|bigSal}

**Note:** Refer to [Buy API Field Filters](/api-docs/buy/static/ref-buy-browse-filters.html) for additional information and examples of all supported filters.
- **limit** (string)
  - The number of items from the result set returned in a single page.  
  
**Note:** If a value is set in the `limit` field, the value of `offset` must be either zero or a multiple of the `limit` value. An error is returned for invalid `offset` values.  
**Note:** This method can return a maximum of 10,000 items in one results set.  
**Min:** 1  
  
**Max:** 200  
  
**Default:** 50
- **offset** (string)
  - Specifies the number of items to skip in the result set. This is used with the `limit` field to control the pagination of the output.  
  
For example:

*   If `offset` is 0 and `limit` is 10, the method will retrieve items 1-10 from the list of items returned
*   If `offset` is 10 and `limit` is 10, the method will retrieve items 11-20 from the list of items returned.

**Note:** The value of `offset` must be either zero or a multiple of the value set in the `limit` field. An error is returned for invalid `offset` values.  
**Note:** This method can return a maximum of 10,000 items in one results set.  
**Min**: 0  
  
**Max:** 9,999  
  
**Default:** 0
- **sort** (string)
  - **Note:** This call currently returns results in a best-match order. This query parameter presently has no practical use.
- **X-EBAY-C-ENDUSERCTX** (string)
  - This header is required to support revenue sharing for eBay Partner Network and to improve the accuracy of shipping and delivery time estimations.  
  
For additional information, refer to [Use request headers](/api-docs/buy/static/api-browse.html#Headers) in the [Buying Integration Guide](/api-docs/buy/static/buying-ig-landing.html).
- **X-EBAY-C-MARKETPLACE-ID** (string)
  - This header identifies the seller's eBay marketplace. It is required for all marketplaces outside of the US.  
  
**Note:** If the marketplace ID value is invalid or missing, the default value of `EBAY_US` is used.  
See [MarketplaceIdEnum](/develop/api/buy/browse_api#buy-browse_api-item_summary-searchbyimage.marketplaceidenum) for a list of supported marketplaces.  
  
**Default:** `EBAY_US`
- **Content-Type** (string) *required*
  - This header indicates the format of the request body provided by the client. Its value should be set to `application/json`.  
  
For more information, refer to [HTTP request headers](/api-docs/static/rest-request-components.html#HTTP).
- **Accept-Language** (string)
  - This header is used to indicate the natural language and locale preferred by the user for the response.  
  
This header is required when targeting a specific locale of a marketplace that supports multiple locales. For example:

*   When targeting the French locale of the Belgium marketplace, it is required to pass in `fr-BE` to specify this. If this locale is not specified, the language will default to Dutch.
*   When targeting the French locale of the Canadian marketplace, it is required to pass in `fr-CA` to specify this. If this locale is not specified, the language will default to English.

### getItem

#### GET /item/{item_id}
**Description:** This method retrieves the details of a specific item, such as description, price, category, all item aspects, condition, return policies, seller feedback and score, shipping options, shipping costs, estimated delivery, and other information the buyer needs to make a purchasing decision.  
  
The Buy APIs are designed to let you create an eBay shopping experience in your app or website. This means you will need to know when something, such as the availability, quantity, etc., has changed in any eBay item you are offering. This is easily achieved by setting the **fieldgroups** URI parameter to one of the following values:

*   `COMPACT`  
    Reduces the response to only those fields necessary in order to determine if any item detail has changed. This field group **must** be used alone.
*   `PRODUCT`  
    Adds fields to the default response that return information about the product/item. This field group may also be used in conjunction with `ADDITIONAL_SELLER_DETAILS`.
*   `ADDITIONAL_SELLER_DETAILS`  
    Adds an additional field to the response that returns the seller's user ID. This field group may also be used in conjunction with `PRODUCT`.
*   `CHARITY_DETAILS`  
    Adds additional fields to the response that return charity information associated with the item, if applicable.

For additional information, refer to **fieldgroups**.  
  
**Restrictions**  
For a list of supported sites and other restrictions, refer to [Buy APIs Restrictions](/api-docs/buy/static/buy-requirements.html).  
  
**eBay Partner Network:** In order to be commissioned for your sales, you must use the URL returned in the `itemAffiliateWebUrl` field to forward your buyer to the ebay.com site.
**Parameters:**
- **fieldgroups** (string)
  - This parameter controls what is returned in the response. If this field is not set, the method returns all the details of the item.  
  
**Note:** Multiple **fieldgroups** can be set and applied simultaneously. However, **COMPACT** **must** be used alone. Otherwise, an error will occur.  
**Valid Values:**

*   **PRODUCT**  
    This field group adds the [product](/develop/api/buy/browse_api#buy-browse_api-item-getitem.item.product) container to the response.
*   **COMPACT**  
    This field group returns only the following fields which let you quickly check if the availability or price of the item has changed, if the item has been revised by the seller, or if an item's top-rated plus status has changed for items you have stored.
    
    *   **itemId**
    *   **bidCount**
    *   **currentBidPrice**
    *   **eligibleForInlineCheckout**
    *   **estimatedAvailabilities**
    *   **gtin**
    *   **immediatePay**
    *   **itemAffiliateWebURL**
    *   **itemCreationDate**
    *   **itemWebUrl**
    *   **legacyItemId**
    *   **minimumPriceToBid**
    *   **price**
    *   **priorityListing**
    *   **reservePriceMet**
    *   **sellerItemRevision**
    *   **shippingOptions**
    *   **taxes**
    *   **topRatedBuyingExperience**
    *   **uniqueBidderCount**
    
    For Example:  
    To determine if a stored item's information is current, perform the following:
    1.  Pass in the item ID and set `fieldgroups` to `COMPACT`.
        
        item/v1|4\*\*\*\*\*\*\*\*\*\*8|0?fieldgroups=COMPACT
        
    2.  Do one of the following:
        *   If **sellerItemRevision** is returned and a revision number for this item _has not_ been stored, record the number and pass in the item ID in the **getItem** method to retrieve the most recent information.
        *   If the revision number is different from the value you have stored, update the value and pass in the item ID in the **getItem** method to retrieve the most recent information.
        *   If `sellerItemRevision` is _not_ returned or has not changed, where needed, update the item information with the information returned in the response.
*   **ADDITIONAL\_SELLER\_DETAILS**  
    This adds the [userId](/develop/api/buy/browse_api#buy-browse_api-item-getitem.sellerdetail.userid) field to the response.
*   **CHARITY\_DETAILS**  
    This adds the [charityTerms](/develop/api/buy/browse_api#buy-browse_api-item-getitem.item.charityterms) container to the response, if applicable.
- **item_id** (string) *required*
  - This path parameter specifies the unique RESTful identifier of the item being retrieved.  
  
**RESTful Item ID Format:** `v1`|`_#_`|`_#_`  
  
For a single SKU listing, pass in the item ID:

v1|2\*\*\*\*\*\*\*\*\*\*2|0

For a multi-SKU listing, pass in the identifier of the variation:

v1|1\*\*\*\*\*\*\*\*\*\*2|4\*\*\*\*\*\*\*\*\*\*2

  
For more information about item IDs for RESTful APIs, refer to [Item ID legacy API compatibility overview](/api-docs/buy/static/api-browse.html#Legacy) in the [Buying Integration Guide](/api-docs/buy/static/buying-ig-landing.html).
- **X-EBAY-C-ENDUSERCTX** (string)
  - This header is can be used in following two situations:  

*   To retrieve the **itemAffiliateWebUrl** field in the response, the ePN affiliate can pass in their affiliate credentials using this header. For more information, see [Header for affiliate information.](/api-docs/buy/static/api-browse.html#affiliate-header)
*   If the listing is using calculated or flat-rate shipping with shipping rate tables, the user can use this header to provide country and postal code in order for the **shippingOption** container, which includes shipping costs and delivery estimates, to be returned. For more information, see [Header for shipping information accuracy.](/api-docs/buy/static/api-browse.html#X-EBAY-C-ENDUSERCTX-context)
- **X-EBAY-C-MARKETPLACE-ID** (string)
  - This header identifies the seller's eBay marketplace. It is required for all marketplaces outside of the US.  
  
**Note:** If the marketplace ID value is invalid or missing, the default value of `EBAY_US` is used.  
See [MarketplaceIdEnum](/develop/api/buy/browse_api#buy-browse_api-item-getitem.marketplaceidenum) for a list of supported marketplaces.  
  
**Default:** `EBAY_US`
- **Accept-Language** (string)
  - This header is used to indicate the natural language and locale preferred by the user for the response.  
  
This header is required when targeting a specific locale of a marketplace that supports multiple locales. For example:

*   When targeting the French locale of the Belgium marketplace, it is required to pass in `fr-BE` to specify this. If this locale is not specified, the language will default to Dutch.
*   When targeting the French locale of the Canadian marketplace, it is required to pass in `fr-CA` to specify this. If this locale is not specified, the language will default to English.
- **quantity_for_shipping_estimate** (string)
  - This query parameter sets the item quantity to be used when calculating the shipping estimate information returned in the [shippingOptions](/develop/api/buy/browse_api#buy-browse_api-item-getitem.item.shippingoptions) container of the response.  
  
This value must be a positive integer value and should not exceed the quantity available in the listing. This field is not recommended for auction listings, as they will always have a quantity of 1.

### getItemByLegacyId

#### GET /item/get_item_by_legacy_id
**Description:** This method is a bridge between the eBay legacy APIs and the eBay Buy APIs. There are differences between how legacy APIs and RESTful APIs return the identifier of an "item" and what the item ID represents. This method lets you use the legacy item ids retrieve the details of a specific item, such as description, price, and other information the buyer needs to make a purchasing decision. It also returns the RESTful **item\_id**, which you can use with all the Buy API methods.  
  
For additional information about how to use legacy ids with the Buy APIs, refer to [Item ID legacy API compatibility overview](/api-docs/buy/static/api-browse.html#Legacy) in the Buying Integration guide.  
  
This method returns the item details and requires you to pass in either the **item\_id** of a non-variation item or the **item\_id** values for both the parent and child of an item group.  
  
**Note:** An item group is an item that has various aspect differences, such as color, size, storage capacity, etc.  
When an item group is created, one of the item variations, such as the red shirt size L, is chosen as the "parent". All other items in the group are the children, such as the blue shirt size L, red shirt size M, etc.  
  
The **fieldgroups** URI parameter lets you control what is returned in the response:

*   Setting **fieldgroups** to `PRODUCT` adds additional fields to the default response that return information about the product of the item.
*   Setting the **fieldgroups** to `ADDITIONAL_SELLER_DETAILS` adds an additional field to the response that returns the seller's user ID.
*   Setting the **fieldgroups** to `CHARITY_DETAILS` adds additional fields to the response that return charity information associated with the item, if applicable.

These **fieldgroups** can be used independently or at the same time. For additional information, refer to .  
  
**Restrictions**  
For a list of supported sites and other restrictions, refer to [Buy APIs Requirements](/api-docs/buy/static/buy-requirements.html).  
  
**eBay Partner Network:** In order to be commissioned for your sales, you must use the URL returned in the `itemAffiliateWebUrl` field to forward your buyer to the ebay.com site.
**Parameters:**
- **fieldgroups** (string)
  - This field controls what is returned in the response. If this field is not set, the method returns all details about the item. Multiple `fieldgroups` can be set.  
  
**Valid Values:**

*   **PRODUCT**  
    This field group adds the [product](/develop/api/buy/browse_api#buy-browse_api-item-getitembylegacyid.item.product) container to the response.
*   **ADDITIONAL\_SELLER\_DETAILS**  
    This field group adds the [userId](/develop/api/buy/browse_api#buy-browse_api-item-getitembylegacyid.sellerdetail.userid) field to the response.
*   **CHARITY\_DETAILS**  
    This field group adds the [charityTerms](/develop/api/buy/browse_api#buy-browse_api-item-getitembylegacyid.item.charityterms) container to the response, if applicable.
- **legacy_item_id** (string) *required*
  - This query parameter is the unique identifier that specifies the item being retrieved.  
  
**Note:** When passing in the ID for a multi-variation listing, you must also use the `legacy_variation_id` field and pass in the ID of the specific item variation. If not, all variation within the multi-SKU listing will be retrieved.  
The following is an example of using the value of the **ItemID** field for a specific item to get the RESTful `itemId` value.

```
browse/v1/item/get_item_by_legacy_id?legacy_item_id=1**********9
```
- **legacy_variation_id** (string)
  - This query parameter specifies the legacy item ID of a specific item in a multi-variation listing, such as that for the _red shirt size L_ item.  
  

**Important!** A `legacy_item_id` value must always be passed in when specifying a `legacy_variation_id` value.
- **legacy_variation_sku** (string)
  - This query parameter specifies the legacy SKU of an item. SKUs are the unique identifiers of an item created by the seller.  
  
The following is an example of using the value of the `ItemID` and `SKU` fields to get the RESTful `itemId` value.

```
browse/v1/item/get_item_by_legacy_id?legacy_item_id=1**********9&legacy_variation_sku=V**********M
```

**Important!** A `legacy_item_id` value must always be passed in when specifying a `legacy_variation_sku` value.
- **X-EBAY-C-ENDUSERCTX** (string)
  - This header is can be used in following two situations:  

*   To retrieve the **itemAffiliateWebUrl** field in the response, the ePN affiliate can pass in their affiliate credentials using this header. For more information, see [Header for affiliate information.](/api-docs/buy/static/api-browse.html#affiliate-header)
*   If the listing is using calculated or flat-rate shipping with shipping rate tables, the user can use this header to provide country and postal code in order for the **shippingOption** container, which includes shipping costs and delivery estimates, to be returned. For more information, see [Header for shipping information accuracy.](/api-docs/buy/static/api-browse.html#X-EBAY-C-ENDUSERCTX-context)
- **X-EBAY-C-MARKETPLACE-ID** (string)
  - This header identifies the seller's eBay marketplace. It is required for all marketplaces outside of the US.  
  
**Note:** If the marketplace ID value is invalid or missing, the default value of `EBAY_US` is used.  
See [MarketplaceIdEnum](/develop/api/buy/browse_api#buy-browse_api-item-getitembylegacyid.marketplaceidenum) for a list of supported marketplaces.  
  
**Default:** `EBAY_US`
- **Accept-Language** (string)
  - This header is used to indicate the natural language and locale preferred by the user for the response.  
  
This header is required when targeting a specific locale of a marketplace that supports multiple locales. For example:

*   When targeting the French locale of the Belgium marketplace, it is required to pass in `fr-BE` to specify this. If this locale is not specified, the language will default to Dutch.
*   When targeting the French locale of the Canadian marketplace, it is required to pass in `fr-CA` to specify this. If this locale is not specified, the language will default to English.
- **quantity_for_shipping_estimate** (string)
  - This query parameter sets the item quantity to be used when calculating the shipping estimate information returned in the [shippingOptions](/develop/api/buy/browse_api#buy-browse_api-item-getitembylegacyid.item.shippingoptions) container of the response.  
  
This value must be a positive integer value and should not exceed the quantity available in the listing. This field is not recommended for auction listings, as they will always have a quantity of 1.

### getItems

#### GET /item
**Description:** This method retrieves the details about specific items that buyers need to make a purchasing decision.  
  
**Note:** This is a [![Limited Release](/cms/img/docs/partners-api.svg "Limited Release")(Limited Release)](</api-docs/static/versioning.html#limited >) available only to select Partners.  
  
For this method, only the following fields are returned: `bidCount`, `currentBidPrice`, `eligibleForInlineCheckout`, `enabledForGuestCheckout`, `estimatedAvailabilities`, `gtin`, `immediatePay`, `itemAffiliateWebUrl`, `itemCreationDate`, `itemEndDate`, `itemId`, `itemWebUrl`, `legacyItemId`, `minimumPriceToBid`, `price`, `priorityListing`, `reservePriceMet`, `sellerItemRevision`, `taxes`, `topRatedBuyingExperience`, and `uniqueBidderCount`.  
  
The array `shippingOptions`, which comprises multiple fields, is also returned if the **X-EBAY-C-ENDUSERCTX** header is supplied.  
  
**Restrictions**  
For a list of supported sites and other restrictions, refer to [Buy APIs Requirements](/api-docs/buy/static/buy-requirements.html).  
  
**eBay Partner Network:** In order to be commissioned for your sales, you must use the URL returned in the itemAffiliateWebUrl field to forward your buyer to the ebay.com site.
**Parameters:**
- **item_ids** (string)
  - A comma separated list of the unique identifiers of the items to retrieve (maximum 20).  
  
**Note:** In any given request, either `item_ids` **or** `item_group_ids` can be retrieved. Attempting to retrieve both will result in an error.  
**RESTful Item ID Format:** `v1`|`_#_`|`_#_`  
  
For a single SKU listing, pass in the item ID:

v1|2\*\*\*\*\*\*\*\*\*\*2|0

For a multi-SKU listing, pass in the identifier of the variation:

v1|1\*\*\*\*\*\*\*\*\*\*2|4\*\*\*\*\*\*\*\*\*\*2

  
For more information about item IDs for RESTful APIs, refer to [Item ID legacy API compatibility overview](/api-docs/buy/static/api-browse.html#Legacy) in the [Buying Integration Guide](/api-docs/buy/static/buying-ig-landing.html).
- **item_group_ids** (string)
  - A comma separated list of the unique identifiers of the item groups being retrieved (maximum 10).  
  
**Note:** In any given request, either `item_ids` **or** `item_group_ids` can be retrieved. Attempting to retrieve both will result in an error.  
**RESTful Group Item ID Format:** `############`  
  
For example:

3\*\*\*\*\*\*\*\*\*\*9
- **X-EBAY-C-ENDUSERCTX** (string)
  - This header is can be used in following two situations:  

*   To retrieve the **itemAffiliateWebUrl** field in the response, the ePN affiliate can pass in their affiliate credentials using this header. For more information, see [Header for affiliate information.](/api-docs/buy/static/api-browse.html#affiliate-header)
*   If the listing is using calculated or flat-rate shipping with shipping rate tables, the user can use this header to provide country and postal code in order for the **shippingOption** container, which includes shipping costs and delivery estimates, to be returned. For more information, see [Header for shipping information accuracy.](/api-docs/buy/static/api-browse.html#X-EBAY-C-ENDUSERCTX-context)
- **X-EBAY-C-MARKETPLACE-ID** (string)
  - This header identifies the seller's eBay marketplace. It is required for all marketplaces outside of the US.  
  
**Note:** If the marketplace ID value is invalid or missing, the default value of `EBAY_US` is used.  
See [MarketplaceIdEnum](/develop/api/buy/browse_api#buy-browse_api-item-getitembylegacyid.marketplaceidenum) for a list of supported marketplaces.  
  
**Default:** `EBAY_US`
- **Accept-Language** (string)
  - This header is used to indicate the natural language and locale preferred by the user for the response.  
  
This header is required when targeting a specific locale of a marketplace that supports multiple locales. For example:

*   When targeting the French locale of the Belgium marketplace, it is required to pass in `fr-BE` to specify this. If this locale is not specified, the language will default to Dutch.
*   When targeting the French locale of the Canadian marketplace, it is required to pass in `fr-CA` to specify this. If this locale is not specified, the language will default to English.
- **quantity_for_shipping_estimate** (string)
  - This query parameter sets the item quantity to be used when calculating the shipping estimate information returned in the [shippingOptions](/develop/api/buy/browse_api#buy-browse_api-item-getitembylegacyid.item.shippingoptions) container of the response.  
  
This value must be a positive integer value and should not exceed the quantity available in the listing. This field is not recommended for auction listings, as they will always have a quantity of 1.

### getItemsByItemGroup

#### GET /item/get_items_by_item_group
**Description:** This method retrieves details about individual items in an item group. An item group is an item that has various aspect differences, such as color, size, storage capacity, etc.  
  
You pass in the **item\_group\_id** as a URI parameter.  
  
This method returns two main containers:

*   **items**  
    This container has an array of containers with the details about each item in the group.
*   **commonDescriptions**  
    This container has an array of containers for a description and the `item_ids` for all items that have this exact description. Because items within an item group often have the same description, this decreases the size of the response.

Setting the **fieldgroup** to `ADDITIONAL_SELLER_DETAILS` adds an additional field to the response that returns the seller's user ID. Setting the **fieldgroup** to `CHARITY_DETAILS` adds additional fields to the response that returns charity information associated with the item, if applicable. For more information, refer to **fieldgroups**.  
  
**Restrictions**  
For a list of supported sites and other restrictions, refer to [Buy APIs Restrictions](/api-docs/buy/static/buy-requirements.html).  
  
**eBay Partner Network:** In order to be commissioned for your sales, you must use the URL returned in the `itemAffiliateWebUrl` field to forward your buyer to the ebay.com site.
**Parameters:**
- **fieldgroups** (string)
  - This field controls what is returned in the response. If this field is not set, the method returns all details about the item.  
  
**Valid Values:**  
  
**ADDITIONAL\_SELLER\_DETAILS** - This field group adds the [userId](/develop/api/buy/browse_api#buy-browse_api-item-getitemsbyitemgroup.sellerdetail.userid) field to the response.  
  
**CHARITY\_DETAILS** - This field group adds the [charityTerms](/develop/api/buy/browse_api#buy-browse_api-item-getitemsbyitemgroup.item.charityterms) container to the response, if applicable.
- **item_group_id** (string) *required*
  - This query parameter specifies the unique identifier of an item group for which information is to be returned. An item group is an item that has various aspect differences, such as color, size, storage capacity, etc.  
  
This ID is returned in the **itemGroupHref** field of the [search](/develop/api/buy/browse_api#buy-browse_api-item_summary-search) and [getItem](/develop/api/buy/browse_api#buy-browse_api-item-getitem) methods.  
  
**For Example:**

https://api.ebay.com/buy/browse/v1/item/get\_items\_by\_item\_group?item\_group\_id=3\*\*\*\*\*\*\*\*\*\*6
- **X-EBAY-C-ENDUSERCTX** (string)
  - This header is can be used in following two situations:  

*   To retrieve the **itemAffiliateWebUrl** field in the response, the ePN affiliate can pass in their affiliate credentials using this header. For more information, see [Header for affiliate information.](/api-docs/buy/static/api-browse.html#affiliate-header)
*   If the listing is using calculated or flat-rate shipping with shipping rate tables, the user can use this header to provide country and postal code in order for the **shippingOption** container, which includes shipping costs and delivery estimates, to be returned. For more information, see [Header for shipping information accuracy.](/api-docs/buy/static/api-browse.html#X-EBAY-C-ENDUSERCTX-context)
- **X-EBAY-C-MARKETPLACE-ID** (string)
  - This header identifies the seller's eBay marketplace. It is required for all marketplaces outside of the US.  
  
**Note:** If the marketplace ID value is invalid or missing, the default value of `EBAY_US` is used.  
See [MarketplaceIdEnum](/develop/api/buy/browse_api#buy-browse_api-item-getitemsbyitemgroup.marketplaceidenum) for a list of supported marketplaces.  
  
**Default:** `EBAY_US`
- **Accept-Language** (string)
  - This header is used to indicate the natural language and locale preferred by the user for the response.  
  
This header is required when targeting a specific locale of a marketplace that supports multiple locales. For example:

*   When targeting the French locale of the Belgium marketplace, it is required to pass in `fr-BE` to specify this. If this locale is not specified, the language will default to Dutch.
*   When targeting the French locale of the Canadian marketplace, it is required to pass in `fr-CA` to specify this. If this locale is not specified, the language will default to English.
- **quantity_for_shipping_estimate** (string)
  - This query parameter sets the item quantity to be used when calculating the shipping estimate information returned in the [shippingOptions](/develop/api/buy/browse_api#buy-browse_api-item-getitemsbyitemgroup.item.shippingoptions) container of the response.  
  
This value must be a positive integer value and should not exceed the quantity available in the listing. This field is not recommended for auction listings, as they will always have a quantity of 1.

### checkCompatibility

#### POST /item/{item_id}/check_compatibility
**Description:** This method checks if a product is compatible with the specified item. You can use this method to check the compatibility of cars, trucks, and motorcycles with a specific part listed on eBay.  
  
For example, to check the compatibility of a part, you pass in the **item\_id** of the part as a URI parameter and specify all the attributes used to define a specific car within the **compatibilityProperties** container. If the call is successful, the response will be `COMPATIBLE`, `NOT_COMPATIBLE`, or `UNDETERMINED`. Refer to [compatibilityStatus](/develop/api/buy/browse_api#buy-browse_api-item-checkcompatibility.compatibilityresponse.compatibilitystatus) for details.  
  
**Note:** The only products supported are cars, trucks, and motorcycles.  
To find the attributes and values for a specific marketplace, you can use the compatibility methods in the [Taxonomy API](/api-docs/commerce/taxonomy/resources/methods). You can use this data to create menus to help buyers specify the product, such as their car.  
  
For more information and a list of required attributes for the US marketplace that describe motor vehicles, refer to [Check compatibility](/api-docs/buy/static/api-browse.html#Check) in the _Buying Integration Guide_.  
  
For an example, refer to the **Samples** section.  
  
**Note:** This method is supported in Sandbox but _only_ when passing in the specified `item_id` and compatibility name-value pairs listed in **Sample: Sandbox Sample**.  
**Restrictions**  
For a list of supported sites and other restrictions, refer to [Buy APIs Restrictions](/api-docs/buy/static/buy-requirements.html).
**Parameters:**
- **item_id** (string) *required*
  - This path parameter specifies the unique RESTful identifier of an item (such as the park you want to check).  
  
**RESTful Item ID Format:** `v1`|`_#_`|`_#_`  
  
For a single SKU listing, pass in the item ID:

v1|2\*\*\*\*\*\*\*\*\*\*2|0

For a multi-SKU listing, pass in the identifier of the variation:

v1|1\*\*\*\*\*\*\*\*\*\*2|4\*\*\*\*\*\*\*\*\*\*2

  
For more information about item IDs for RESTful APIs, refer to [Item ID legacy API compatibility overview](/api-docs/buy/static/api-browse.html#Legacy) in the [Buying Integration Guide](/api-docs/buy/static/buying-ig-landing.html).
- **X-EBAY-C-MARKETPLACE-ID** (string)
  - This header identifies the seller's eBay marketplace. It is required for all marketplaces outside of the US.  
  
**Note:** If the marketplace ID value is invalid or missing, the default value of `EBAY_US` is used.  
See [MarketplaceIdEnum](/develop/api/buy/browse_api#buy-browse_api-item-getitem.marketplaceidenum) for a list of supported marketplaces.  
  
**Default:** `EBAY_US`
- **Content-Type** (string) *required*
  - This header indicates the format of the request body provided by the client.  
  
Its value should be set to `application/json`.  
  
For more information, refer to [HTTP request headers](/api-docs/static/rest-request-components.html#HTTP) in the [Using eBay RESTful APIs](/api-docs/static/ebay-rest-landing.html) guide.
- **Accept-Language** (string)
  - This header is used to indicate the natural language and locale preferred by the user for the response.  
  
This header is required when targeting a specific locale of a marketplace that supports multiple locales. For example:

*   When targeting the French locale of the Belgium marketplace, it is required to pass in `fr-BE` to specify this. If this locale is not specified, the language will default to Dutch.
*   When targeting the French locale of the Canadian marketplace, it is required to pass in `fr-CA` to specify this. If this locale is not specified, the language will default to English.

## Error Codes

The following error codes may be returned by this API:

### REQUEST Errors

#### 12001 - API_BROWSE
**Description:** The call must have a valid 'q', 'category\_ids', 'epid' or 'gtin' query parameter.

#### 12004 - API_BROWSE
**Description:** The 'offset' value cannot be negative.

#### 12005 - API_BROWSE
**Description:** The 'offset' value must be an integer.

#### 12006 - API_BROWSE
**Description:** The 'limit' value should be between 1 and 200 (inclusive).

#### 12007 - API_BROWSE
**Description:** The 'limit' value must be an integer value.

#### 12023 - API_BROWSE
**Description:** This keyword search results in a response that is too large to return. Either change the keyword or add additional query parameters and/or filters.

#### 12025 - API_BROWSE
**Description:** The 'charity\_ids' field has exceeded the maximum limit of 20.

#### 12026 - API_BROWSE
**Description:** The 'charity\_ids' field is not supported for the marketplace {marketplaceId}. Valid marketplaces are: {validMarketplaces}.

#### 12027 - API_BROWSE
**Description:** The 'auto\_correct' value is invalid. For the valid values, refer to the API call documentation.

#### 12028 - API_BROWSE
**Description:** The 'auto\_correct' is not supported for the marketplace {marketplaceId}. Valid marketplaces are: {validMarketplaces}.

#### 12029 - API_BROWSE
**Description:** The maximum number of listings that can be retrieved is 10,000, so your offset value must be less than 10,000. If 10,000 or more listings are matching your search criteria, consider narrowing the scope of your search.

#### 12030 - API_BROWSE
**Description:** The number of categories in the request has exceeded the limit. Please reduce the number of categories to {allowedMaxCategories} or less.

#### 12032 - API_BROWSE
**Description:** The number of sellers in the filter has exceeded the limit. Please reduce the number of sellers to {allowedMaxSellersInFilter} or less.

#### 12033 - API_BROWSE
**Description:** The 'qualifiedPrograms' filter for {filterValue} requires valid 'deliveryPostalCode' and 'deliveryCountry' filter values.

#### 12034 - API_BROWSE
**Description:** The 'buyingOptions' filter value {filterValue} is not supported for the sort by {sortOption}. For the supported values, refer to the API call documentation.

#### 12503 - API_BROWSE
**Description:** There is no compatibility information found either because there is no compatibility results or the data provided in the compatibility\_filter is invalid or insufficient.

#### 12504 - API_BROWSE
**Description:** You must provide a category ID that supports fitment.

#### 12505 - API_BROWSE
**Description:** The following compatibility attributes in the request are not supported: {attributes}.

#### 12506 - API_BROWSE
**Description:** The category ID submitted does not support fitment.

#### 12507 - API_BROWSE
**Description:** To filter by 'guaranteedDeliveryInDays', you must include 'deliveryCountry'.

#### 12508 - API_BROWSE
**Description:** To filter by 'guaranteedDeliveryInDays', you must include 'deliveryPostalCode' for the 'deliveryCountry'.

#### 12509 - API_BROWSE
**Description:** The 'guaranteedDeliveryInDays' value {guaranteedDeliveryInDays} is invalid for 'deliveryCountry' value {deliveryCountry}. Valid values for 'guaranteedDeliveryInDays' for {deliveryCountry} must be in the range of {rangeLowerBound} to {rangeUpperBound} inclusive.

#### 12510 - API_BROWSE
**Description:** The 'guaranteedDeliveryInDays' filter is not supported for the marketplace {marketplaceId}. Valid marketplaces are: {validMarketplaces}.

#### 12512 - API_BROWSE
**Description:** The 'qualifiedPrograms' filter for {filterValue} is not supported for the marketplace {marketplaceId}. Valid marketplaces are: {validMarketplaces}.

#### 12515 - API_BROWSE
**Description:** The 'offset' value must be either zero or a multiple of the 'limit' value.

#### 12516 - API_BROWSE
**Description:** The 'q' value is invalid. It must be longer than one character when using the 'searchInDescription' filter.

#### 12517 - API_BROWSE
**Description:** Only one item location filter can be applied at a time. Refer to the API call documentation.

#### 12518 - API_BROWSE
**Description:** The 'itemLocationRegion' filter value is not supported for the marketplace {marketplaceId}. Valid values are: {validRegionValues}.

#### 12520 - API_BROWSE
**Description:** The 'conditionIds' filter value is invalid or not supported. For the supported values, refer to the API call documentation.

#### 12521 - API_BROWSE
**Description:** The request contains malformed URL encoding. Please check that all percent-encoded characters (%) are properly formatted.

#### 12500 - API_BROWSE
**Description:** This image search results in a response that is too large to return. Either change the image or add additional query parameters and/or filters.

#### 12501 - API_BROWSE
**Description:** The image data is empty, is not Base64 encoded, or is invalid.

#### 11001 - API_BROWSE
**Description:** The specified item ID was not found.

#### 11002 - API_BROWSE
**Description:** The specified item group was not found.

#### 11004 - API_BROWSE
**Description:** The item is not available for purchase. This can be for many reasons, such as when the listing is being updated by the seller. Wait a few minutes and try the call again.

#### 11005 - API_BROWSE
**Description:** The item group ID is invalid. Use {itemHref} to get the item details.

#### 11008 - API_BROWSE
**Description:** The item group is not available. This can be for many reasons, such as when the listing is being updated by the seller. Wait a few minutes and try the call again.

#### 11011 - API_BROWSE
**Description:** The marketplace value {marketplaceId} is not supported. The supported values are: {allowedMarketplaces}

#### 11012 - API_BROWSE
**Description:** The specified item IDs are invalid, or the format of the specified values are invalid.

#### 11013 - API_BROWSE
**Description:** The specified group IDs are invalid, or the format of the specified values are invalid.

#### 11014 - API_BROWSE
**Description:** An item\_ids and an item\_group\_ids list cannot be used at same time. Please use only one of these lists.

#### 11015 - API_BROWSE
**Description:** The maximum number of item ids has been exceeded. Please reduce the number of item ids to {maxAllowedItemIds} or less.

#### 11016 - API_BROWSE
**Description:** The maximum number of item group IDs has been exceeded. Please reduce the number of item group ids to {maxAllowedItemGroupIds} or less.

#### 11018 - API_BROWSE
**Description:** The specified fieldgroups are invalid. The COMPACT fieldgroup cannot be combined with another fieldgroup.

#### 11019 - API_BROWSE
**Description:** The quantity\_for\_shipping\_estimate value {quantityForShippingEstimate} is invalid. Please enter a positive value.

#### 11020 - API_BROWSE
**Description:** The X-EBAY-C-ENDUSERCTX header value is in an invalid format. Please ensure that all values are key=value pairs.

#### 11501 - API_BROWSE
**Description:** The 'fieldgroups' value(s) are invalid: {fieldgroups}. The supported fieldgroups are: {supportedFieldgroups}.

#### 11003 - API_BROWSE
**Description:** The specified legacy item ID was not found.

#### 11006 - API_BROWSE
**Description:** The legacy ID is invalid. Use {itemGroupHref} to get the item group details.

#### 11009 - API_BROWSE
**Description:** The legacy variation sku is invalid.

#### 11010 - API_BROWSE
**Description:** You cannot submit legacy\_variation\_sku and legacy\_variation\_id in the same request. For help, see the documentation.

#### 11017 - API_BROWSE
**Description:** An item\_ids or an item\_group\_ids list is required. Please use one of these lists.

#### 11503 - API_BROWSE
**Description:** The request is either empty or incomplete. For help, see the documentation for this call.

#### 11504 - API_BROWSE
**Description:** The following compatibilityProperties (attributes name/value pairs) are missing: {attributes}.

#### 11505 - API_BROWSE
**Description:** The item is not valid for compatibility validation.

#### 11506 - API_BROWSE
**Description:** The 'name' {compatibilityNames} appears more than once in the request.

#### 11507 - API_BROWSE
**Description:** The following name(s) in the request are not supported {attributes}.

### BUSINESS Errors

#### 12013 - API_BROWSE
**Description:** Top level category browsing is not allowed. Please provide keywords or more filters for the applied top level category.

#### 12019 - API_BROWSE
**Description:** Currently, the {marketplaceId} marketplace is not supported. The supported Marketplaces are: {allowedMarketplaces} .

#### 12020 - API_BROWSE
**Description:** The 'fieldgroups' value {fieldgroups} is invalid when multiple 'category\_ids' are specified. Either change the call to have only one value in 'category\_ids' or remove the 'fieldgroups'.

#### 12513 - API_BROWSE
**Description:** The 'priorityListing' filter is not supported for the marketplace {marketplaceId}. Valid marketplaces are: {validMarketplaces}.

#### 12514 - API_BROWSE
**Description:** The 'priorityListing' filter is not supported for the specified sort option. Refer to the API call documentation.

### APPLICATION Errors

#### 12000 - API_BROWSE
**Description:** There was a problem with an eBay internal system or process. Contact eBay developer support for assistance.

#### 11000 - API_BROWSE
**Description:** There was a problem with an eBay internal system or process. Contact eBay developer support for assistance.

## Types

### AspectDistribution
**Description:** The type that define the fields for the aspect information. Aspects are the variations of an item, such as color, size, etc.
**Type:** object

**Properties:**
- **aspectValueDistributions** (array)
  - An array of containers for the various values of the aspect and the match count, and a HATEOAS reference (`refinementHref`) for this aspect.
- **localizedAspectName** (string)
  - The name of an aspect, such as _Brand_, _Color_, etc.

### AspectValueDistribution
**Description:** This type contains information about one value of a specified aspect. This value serves as a product refinement.
**Type:** object

**Properties:**
- **localizedAspectValue** (string)
  - The value of an aspect. For example, Red is a value for the aspect Color.
- **matchCount** (integer)
  - The number of items with this aspect.
- **refinementHref** (string)
  - A HATEOAS reference for this aspect.

### AutoCorrections
**Description:** This type defines the automatically spell-corrected keyword from the request.
**Type:** object

**Properties:**
- **q** (string)
  - The automatically spell-corrected keyword from the request.

### BuyingOptionDistribution
**Description:** This type defines the fields for the buying options refinements. This container is returned when `fieldgroups` is set to `BUYING_OPTION_REFINEMENTS` or `FULL` in the request.
**Type:** object

**Properties:**
- **buyingOption** (string)
  - The container that returns the buying option type. This will be AUCTION, FIXED\_PRICE, CLASSIFIED\_AD, or a combination of these options. For details, see [buyingOptions](/develop/api/buy/browse_api#buy-browse_api-item_summary-search.itemsummary.buyingoptions).
- **matchCount** (integer)
  - The number of items having this buying option.
- **refinementHref** (string)
  - The HATEOAS reference for this buying option.

### Category
**Description:** This type is used by the `categories` container in the response of the **search** method, and contains the name and ID of the item category.
**Type:** object

**Properties:**
- **categoryId** (string)
  - The unique identifier of the category.
- **categoryName** (string)
  - The name of the category.

### CategoryDistribution
**Description:** This type defines the fields for the category refinements. This container is returned when `fieldgroups` is set to `CATEGORY_REFINEMENTS` or `FULL` in the request.
**Type:** object

**Properties:**
- **categoryId** (string)
  - The unique identifier of the category.
- **categoryName** (string)
  - The name of the category, such as **Baby & Toddler Clothing**.
- **matchCount** (integer)
  - The number of items in this category.
- **refinementHref** (string)
  - The HATEOAS reference of this category.

### CompatibilityMatchEnum
**Description:** An enumerated type for the values that represent how well the item matches the `compatibility_filter` product attributes. | - **EXACT**: Indicates the item is compatible with all the product attributes submitted. - **POSSIBLE**: Indicates the item could fit the product. To further check for compatibility, you can add more product attributes.
**Type:** string

### CompatibilityProperty
**Description:** This type returns the product attribute name/value pairs that are compatible with the keyword. These attributes are submitted in the `compatibility_filter` request field.
**Type:** object

**Properties:**
- **localizedName** (string)
  - The name of the product attribute that as been translated to the language of the site.
- **name** (string)
  - The name of the product attribute, such as Make, Model, Year, etc.
- **value** (string)
  - The value for the `name` attribute, such as **BMW**, **R1200GS**, **2011**, etc.

### ConditionDistribution
**Description:** This type defines the fields for the conditions refinements. This container is returned when `fieldgroups` is set to `CONDITION_REFINEMENTS` or `FULL` in the request.
**Type:** object

**Properties:**
- **condition** (string)
  - The text describing the condition of the item, such as _New_ or _Used_. For a list of condition names, refer to [Item Condition IDs and Names](</api-docs/sell/static/metadata/condition-id-values.html >).
- **conditionId** (string)
  - The identifier of the condition. For example, `1000` is the identifier for `NEW`.
- **matchCount** (integer)
  - The number of items having the condition.
- **refinementHref** (string)
  - The HATEOAS reference of this condition.

### ConvertedAmount
**Description:** This type defines the monetary value of an amount. It can provide the amount in both the currency used on the eBay site where an item is being offered and the conversion of that value into another currency, if applicable.
**Type:** object

**Properties:**
- **convertedFromCurrency** (CurrencyCodeEnum)
  - The three-letter [ISO 4217](<https://www.iso.org/iso-4217-currency-codes.html >) code representing the currency of the amount in the `convertedFromValue` field. This value is required or returned only if currency conversion/localization is required, and represents the pre-conversion currency.
- **convertedFromValue** (string)
  - The monetary amount before any conversion is performed, in the currency specified by the **convertedFromCurrency** field. This value is required or returned only if currency conversion/localization is required. The **value** field contains the converted amount of this value, in the currency specified by the **currency** field.
- **currency** (CurrencyCodeEnum)
  - The three-letter [ISO 4217](<https://www.iso.org/iso-4217-currency-codes.html >) code representing the currency of the amount in the `value` field. If currency conversion/localization is required, this is the post-conversion currency of the amount in the `value` field.  
  
**Default:** The currency of the authenticated user's country.
- **value** (string)
  - The monetary amount, in the currency specified by the **currency** field. If currency conversion/localization is required, this value is the converted amount, and the **convertedFromValue** field contains the amount in the original currency.

### CountryCodeEnum
**Description:** This enumerated type defines the two-letter [ISO 3166](https://www.iso.org/iso-3166-country-codes.html) standard code representing a country. | - **AD**: Indicates the country is Andorra. - **AE**: Indicates the country is United Arab Emirates. - **AF**: Indicates the country is Afghanistan. - **AG**: Indicates the country is Antigua and Barbuda. - **AI**: Indicates the country is Anguilla. - **AL**: Indicates the country is Albania. - **AM**: Indicates the country is Armenia. - **AN**: Indicates the country is Netherlands Antilles. - **AO**: Indicates the country is Angola. - **AQ**: Indicates the country is Antarctica. - **AR**: Indicates the country is Argentina. - **AS**: Indicates the country is American Samoa. - **AT**: Indicates the country is Austria. - **AU**: Indicates the country is Australia. - **AW**: Indicates the country is Aruba. - **AX**: Indicates the country is Aland Islands. - **AZ**: Indicates the country is Azerbaijan. - **BA**: Indicates the country is Bosnia and Herzegovina. - **BB**: Indicates the country is Barbados. - **BD**: Indicates the country is Bangladesh. - **BE**: Indicates the country is Belgium. - **BF**: Indicates the country is Burkina Faso. - **BG**: Indicates the country is Bulgaria. - **BH**: Indicates the country is Bahrain. - **BI**: Indicates the country is Burundi. - **BJ**: Indicates the country is Benin. - **BL**: Indicates the country is Saint Barthelemy. - **BM**: Indicates the country is Bermuda. - **BN**: Indicates the country is Brunei Darussalam. - **BO**: Indicates the country is Bolivia. - **BQ**: Indicates the country is Bonaire, Sint Eustatius, and Saba. - **BR**: Indicates the country is Brazil. - **BS**: Indicates the country is Bahamas. - **BT**: Indicates the country is Bhutan. - **BV**: Indicates the country is Bouvet Island. - **BW**: Indicates the country is Botswana. - **BY**: Indicates the country is Belarus. - **BZ**: Indicates the country is Belize. - **CA**: Indicates the country is Canada. - **CC**: Indicates the country is Cocos (Keeling) Islands. - **CD**: Indicates the country is The Democratic Republic of the Congo. - **CF**: Indicates the country is Central African Republic. - **CG**: Indicates the country is Congo. - **CH**: Indicates the country is Switzerland. - **CI**: Indicates the country is Cote d'Ivoire. - **CK**: Indicates the country is Cook Islands. - **CL**: Indicates the country is Chile. - **CM**: Indicates the country is Cameroon. - **CN**: Indicates the country is China. - **CO**: Indicates the country is Colombia. - **CR**: Indicates the country is Costa Rica. - **CU**: Indicates the country is Cuba. - **CV**: Indicates the country is Cape Verde. - **CW**: Indicates the country is Curacao. - **CX**: Indicates the country is Christmas Island. - **CY**: Indicates the country is Cyprus. - **CZ**: Indicates the country is Czech Republic. - **DE**: Indicates the country is Germany. - **DJ**: Indicates the country is Djibouti. - **DK**: Indicates the country is Denmark. - **DM**: Indicates the country is Dominica. - **DO**: Indicates the country is Dominican Republic. - **DZ**: Indicates the country is Algeria. - **EC**: Indicates the country is Ecuador. - **EE**: Indicates the country is Estonia. - **EG**: Indicates the country is Egypt. - **EH**: Indicates the country is Western Sahara. - **ER**: Indicates the country is Eritrea. - **ES**: Indicates the country is Spain. - **ET**: Indicates the country is Ethiopia. - **FI**: Indicates the country is Finland. - **FJ**: Indicates the country is Fiji. - **FK**: Indicates the country is Falkland Islands (Malvinas). - **FM**: Indicates the country is Federated States of Micronesia. - **FO**: Indicates the country is Faroe Islands. - **FR**: Indicates the country is France. - **GA**: Indicates the country is Gabon. - **GB**: Indicates the country is United Kingdom. - **GD**: Indicates the country is Grenada. - **GE**: Indicates the country is Georgia. - **GF**: Indicates the country is French Guiana. - **GG**: Indicates the country is Guernsey. - **GH**: Indicates the country is Ghana. - **GI**: Indicates the country is Gibraltar. - **GL**: Indicates the country is Greenland. - **GM**: Indicates the country is Gambia. - **GN**: Indicates the country is Guinea. - **GP**: Indicates the country is Guadeloupe. - **GQ**: Indicates the country is Equatorial Guinea. - **GR**: Indicates the country is Greece. - **GS**: Indicates the country is South Georgia and the South Sandwich Islands. - **GT**: Indicates the country is Guatemala. - **GU**: Indicates the country is Guam. - **GW**: Indicates the country is Guinea-Bissau. - **GY**: Indicates the country is Guyana. - **HK**: Indicates the country is Hong Kong. - **HM**: Indicates the country is Heard Island and McDonald Islands. - **HN**: Indicates the country is Honduras. - **HR**: Indicates the country is Croatia. - **HT**: Indicates the country is Haiti. - **HU**: Indicates the country is Hungary. - **ID**: Indicates the country is Indonesia. - **IE**: Indicates the country is Ireland. - **IL**: Indicates the country is Israel. - **IM**: Indicates the country is Isle of Man. - **IN**: Indicates the country is India. - **IO**: Indicates the country is British Indian Ocean Territory. - **IQ**: Indicates the country is Iraq. - **IR**: Indicates the country is Islamic Republic of Iran. - **IS**: Indicates the country is Iceland. - **IT**: Indicates the country is Italy. - **JE**: Indicates the country is Jersey. - **JM**: Indicates the country is Jamaica. - **JO**: Indicates the country is Jordan. - **JP**: Indicates the country is Japan. - **KE**: Indicates the country is Kenya. - **KG**: Indicates the country is Kyrgyzstan. - **KH**: Indicates the country is Cambodia. - **KI**: Indicates the country is Kiribati. - **KM**: Indicates the country is Comoros. - **KN**: Indicates the country is Saint Kitts and Nevis. - **KP**: Indicates the country is Democratic People's Republic of Korea. - **KR**: Indicates the country is Republic of Korea. - **KW**: Indicates the country is Kuwait. - **KY**: Indicates the country is Cayman Islands. - **KZ**: Indicates the country is Kazakhstan. - **LA**: Indicates the country is Lao People's Democratic Republic. - **LB**: Indicates the country is Lebanon. - **LC**: Indicates the country is Saint Lucia. - **LI**: Indicates the country is Liechtenstein. - **LK**: Indicates the country is Sri Lanka. - **LR**: Indicates the country is Liberia. - **LS**: Indicates the country is Lesotho. - **LT**: Indicates the country is Lithuania. - **LU**: Indicates the country is Luxembourg. - **LV**: Indicates the country is Latvia. - **LY**: Indicates the country is Libyan Arab Jamahiriya. - **MA**: Indicates the country is Morocco. - **MC**: Indicates the country is Monaco. - **MD**: Indicates the country is Republic of Moldova. - **ME**: Indicates the country is Montenegro. - **MF**: Indicates the country is Saint Martin (French part). - **MG**: Indicates the country is Madagascar. - **MH**: Indicates the country is Marshall Islands. - **MK**: Indicates the country is The Former Yugoslav Republic of Macedonia. - **ML**: Indicates the country is Mali. - **MM**: Indicates the country is Myanmar. - **MN**: Indicates the country is Mongolia. - **MO**: Indicates the country is Macao. - **MP**: Indicates the country is Northern Mariana Islands. - **MQ**: Indicates the country is Martinique. - **MR**: Indicates the country is Mauritania. - **MS**: Indicates the country is Montserrat. - **MT**: Indicates the country is Malta. - **MU**: Indicates the country is Mauritius. - **MV**: Indicates the country is Maldives. - **MW**: Indicates the country is Malawi. - **MX**: Indicates the country is Mexico. - **MY**: Indicates the country is Malaysia. - **MZ**: Indicates the country is Mozambique. - **NA**: Indicates the country is Namibia. - **NC**: Indicates the country is New Caledonia. - **NE**: Indicates the country is Niger. - **NF**: Indicates the country is Norfolk Island. - **NG**: Indicates the country is Nigeria. - **NI**: Indicates the country is Nicaragua. - **NL**: Indicates the country is Netherlands. - **NO**: Indicates the country is Norway. - **NP**: Indicates the country is Nepal. - **NR**: Indicates the country is Nauru. - **NU**: Indicates the country is Niue. - **NZ**: Indicates the country is New Zealand. - **OM**: Indicates the country is Oman. - **PA**: Indicates the country is Panama. - **PE**: Indicates the country is Peru. - **PF**: Indicates the country is French Polynesia. Includes Tahiti. - **PG**: Indicates the country is Papua New Guinea. - **PH**: Indicates the country is Philippines. - **PK**: Indicates the country is Pakistan. - **PL**: Indicates the country is Poland. - **PM**: Indicates the country is Saint Pierre and Miquelon. - **PN**: Indicates the country is Pitcairn. - **PR**: Indicates the country is Puerto Rico. - **PS**: Indicates the country is Palestinian territory Occupied. - **PT**: Indicates the country is Portugal. - **PW**: Indicates the country is Palau. - **PY**: Indicates the country is Paraguay. - **QA**: Indicates the country is Qatar. - **RE**: Indicates the country is Reunion. - **RO**: Indicates the country is Romania. - **RS**: Indicates the country is Serbia. - **RU**: Indicates the country is Russian Federation. - **RW**: Indicates the country is Rwanda. - **SA**: Indicates the country is Saudi Arabia. - **SB**: Indicates the country is Solomon Islands. - **SC**: Indicates the country is Seychelles. - **SD**: Indicates the country is Sudan. - **SE**: Indicates the country is Sweden. - **SG**: Indicates the country is Singapore. - **SH**: Indicates the country is Saint Helena. - **SI**: Indicates the country is Slovenia. - **SJ**: Indicates the country is Svalbard and Jan Mayen. - **SK**: Indicates the country is Slovakia. - **SL**: Indicates the country is Sierra Leone. - **SM**: Indicates the country is San Marino. - **SN**: Indicates the country is Senegal. - **SO**: Indicates the country is Somalia. - **SR**: Indicates the country is Suriname. - **ST**: Indicates the country is Sao Tome and Principe. - **SV**: Indicates the country is El Salvador. - **SX**: Indicates the country is Sint Maarten (Dutch part). - **SY**: Indicates the country is Syrian Arab Republic. - **SZ**: Indicates the country is Swaziland. - **TC**: Indicates the country is Turks and Caicos Islands. - **TD**: Indicates the country is Chad. - **TF**: Indicates the country is French Southern Territories. - **TG**: Indicates the country is Togo. - **TH**: Indicates the country is Thailand. - **TJ**: Indicates the country is Tajikistan. - **TK**: Indicates the country is Tokelau. - **TL**: Indicates the country is Timor-Leste. - **TM**: Indicates the country is Turkmenistan. - **TN**: Indicates the country is Tunisia. - **TO**: Indicates the country is Tonga. - **TR**: Indicates the country is Turkey. - **TT**: Indicates the country is Trinidad and Tobago. - **TV**: Indicates the country is Tuvalu. - **TW**: Indicates the country is Taiwan. - **TZ**: Indicates the country is Tanzania. - **UA**: Indicates the country is Ukraine. - **UG**: Indicates the country is Uganda. - **UM**: Indicates the country is United States Minor Outlying Islands. - **US**: Indicates the country is United States. - **UY**: Indicates the country is Uruguay. - **UZ**: Indicates the country is Uzbekistan. - **VA**: Indicates the country is Holy See (Vatican City state). - **VC**: Indicates the country is Saint Vincent and the Grenadines. - **VE**: Indicates the country is Venezuela. - **VG**: Indicates the country is British Virgin Islands. - **VI**: Indicates the country is the U.S. Virgin Islands. - **VN**: Indicates the country is Vietnam. - **VU**: Indicates the country is Vanuatu. - **WF**: Indicates the country is Wallis and Futuna. - **WS**: Indicates the country is Samoa. - **YE**: Indicates the country is Yemen. - **YT**: Indicates the country is Mayotte. - **ZA**: Indicates the country is South Africa. - **ZM**: Indicates the country is Zambia. - **ZW**: Indicates the country is Zimbabwe.
**Type:** string

### CurrencyCodeEnum
**Description:** This enumerated type defines the three-letter [ISO 4217](https://www.iso.org/iso-4217-currency-codes.html) code representing a world currency. | - **AED**: Indicates the currency is United Arab Emirates dirham. - **AFN**: Indicates the currency is Afghan afghani. - **ALL**: Indicates the currency is Albanian lek. - **AMD**: Indicates the currency is Armenian dram. - **ANG**: Indicates the currency is Netherlands Antillean guilder. - **AOA**: Indicates the currency is Angolan kwanza. - **ARS**: Indicates the currency is Argentine peso. - **AUD**: Indicates the currency is Australian dollar. - **AWG**: Indicates the currency is Aruban florin. - **AZN**: Indicates the currency is Azerbaijani manat. - **BAM**: Indicates the currency is Bosnia and Herzegovina convertible mark. - **BBD**: Indicates the currency is Barbados dollar. - **BDT**: Indicates the currency is a Bangladeshi taka. - **BGN**: Indicates the currency is Bulgarian lev. - **BHD**: Indicates the currency is Bahraini dinar. - **BIF**: Indicates the currency is Burundian franc. - **BMD**: Indicates the currency is Bermudian dollar. - **BND**: Indicates the currency is Brunei dollar. - **BOB**: Indicates the currency is Bolivian Boliviano. - **BRL**: Indicates the currency is Brazilian real. - **BSD**: Indicates the currency is Bahamian dollar. - **BTN**: Indicates the currency is Bhutanese ngultrum. - **BWP**: Indicates the currency is Botswana pula. - **BYR**: Indicates the currency is Belarusian ruble. - **BZD**: Indicates the currency is Belize dollar. - **CAD**: Indicates the currency is Canadian dollar. - **CDF**: Indicates the currency is Congolese franc. - **CHF**: Indicates the currency is a Swiss franc. - **CLP**: Indicates the currency is Chilean peso. - **CNY**: Indicates the currency is Chinese yuan renminbi. - **COP**: Indicates the currency is Colombian peso. - **CRC**: Indicates the currency is Costa Rican colon. - **CUP**: Indicates the currency is Cuban peso. - **CVE**: Indicates the currency is Cape Verde escudo. - **CZK**: Indicates the currency is Czech koruna. - **DJF**: Indicates the currency is Djiboutian franc. - **DKK**: Indicates the currency is Danish krone. - **DOP**: Indicates the currency is Dominican peso. - **DZD**: Indicates the currency is Algerian dinar. - **EGP**: Indicates the currency is Egyptian pound. - **ERN**: Indicates the currency is Eritrean nakfa. - **ETB**: Indicates the currency is Ethiopian birr. - **EUR**: Indicates the currency is European Union euro. - **FJD**: Indicates the currency is Fiji dollar. - **FKP**: Indicates the currency is Falkland Islands pound. - **GBP**: Indicates the currency is British pound sterling. - **GEL**: Indicates the currency is Georgian lari. - **GHS**: Indicates the currency is Ghanaian cedi. - **GIP**: Indicates the currency is Gibraltar pound. - **GMD**: Indicates the currency is Gambian dalasi. - **GNF**: Indicates the currency is Guinean franc. - **GTQ**: Indicates the currency is Guatemalan quetzal. - **GYD**: Indicates the currency is Guyanese dollar. - **HKD**: Indicates the currency is Hong Kong dollar. - **HNL**: Indicates the currency is Honduran lempira. - **HRK**: Indicates the currency is Croatian kuna. - **HTG**: Indicates the currency is Haitian gourde. - **HUF**: Indicates the currency is Hungarian forint. - **IDR**: Indicates the currency is Indonesian rupiah. - **ILS**: Indicates the currency is Israeli new shekel. - **INR**: Indicates the currency is Indian rupee. - **IQD**: Indicates the currency is Iraqi dinar. - **IRR**: Indicates the currency is Iranian rial. - **ISK**: Indicates the currency is Icelandic krona. - **JMD**: Indicates the currency is Jamaican dollar. - **JOD**: Indicates the currency is Jordanian dinar. - **JPY**: Indicates the currency is Japanese yen. - **KES**: Indicates the currency is Kenyan shilling. - **KGS**: Indicates the currency is Kyrgyzstani som. - **KHR**: Indicates the currency is Cambodian riel. - **KMF**: Indicates the currency is Comoro franc. - **KPW**: Indicates the currency is North Korean won. - **KRW**: Indicates the currency is South Korean won. - **KWD**: Indicates the currency is Kuwaiti dinar. - **KYD**: Indicates the currency is Cayman Islands dollar. - **KZT**: Indicates the currency is Kazakhstani tenge. - **LAK**: Indicates the currency is Lao kip. - **LBP**: Indicates the currency is Lebanese pound. - **LKR**: Indicates the currency is Sri Lankan rupee. - **LRD**: Indicates the currency is Liberian dollar. - **LSL**: Indicates the currency is Lesotho loti. - **LTL**: Indicates the currency is Lithuanian litas. - **LYD**: Indicates the currency is Libyan dinar. - **MAD**: Indicates the currency is Moroccan dirham. - **MDL**: Indicates the currency is Moldovan leu. - **MGA**: Indicates the currency is Malagasy ariary. - **MKD**: Indicates the currency is Macedonian denar. - **MMK**: Indicates the currency is Myanmar kyat. - **MNT**: Indicates the currency is Mongolian tugrik. - **MOP**: Indicates the currency is Macanese pataca. - **MRO**: Indicates the currency is Mauritanian ouguiya. - **MUR**: Indicates the currency is Mauritian rupee. - **MVR**: Indicates the currency is Maldivian rufiyaa. - **MWK**: Indicates the currency is Malawian kwacha. - **MXN**: Indicates the currency is Mexican peso. - **MYR**: Indicates the currency is Malaysian ringgit. - **MZN**: Indicates the currency is Mozambican metical. - **NAD**: Indicates the currency is Namibian dollar. - **NGN**: Indicates the currency is Nigerian naira. - **NIO**: Indicates the currency is Nicaraguan cordoba oro. - **NOK**: Indicates the currency is Norwegian krone. - **NPR**: Indicates the currency is Nepalese rupee. - **NZD**: Indicates the currency is New Zealand dollar. - **OMR**: Indicates the currency is Omani rial. - **PAB**: Indicates the currency is Panamanian balboa. - **PEN**: Indicates the currency is Peruvian sol. - **PGK**: Indicates the currency is Papua New Guinean kina. - **PHP**: Indicates the currency is Philippine peso. - **PKR**: Indicates the currency is Pakistani rupee. - **PLN**: Indicates the currency is Polish zloty. - **PYG**: Indicates the currency is Paraguayan guarani. - **QAR**: Indicates the currency is Qatari riyal. - **RON**: Indicates the currency is Romanian leu. - **RSD**: Indicates the currency is Serbian dinar. - **RUB**: Indicates the currency is Russian ruble. - **RWF**: Indicates the currency is Rwandan franc. - **SAR**: Indicates the currency is Saudi riyal. - **SBD**: Indicates the currency is Solomon Islands dollar. - **SCR**: Indicates the currency is Seychelles rupee. - **SDG**: Indicates the currency is Sudanese pound. - **SEK**: Indicates the currency is Swedish krona. - **SGD**: Indicates the currency is Singapore dollar. - **SHP**: Indicates the currency is Saint Helena pound. - **SLL**: Indicates the currency is Sierra Leonean leone. - **SOS**: Indicates the currency is Somali shilling. - **SRD**: Indicates the currency is Surinamese dollar. - **STD**: Indicates the currency is Sao Tome and Principe dobra. - **SYP**: Indicates the currency is Syrian pound. - **SZL**: Indicates the currency is Swazi lilangeni. - **THB**: Indicates the currency is Thai baht. - **TJS**: Indicates the currency is Tajikistani somoni. - **TMT**: Indicates the currency is Turkmenistani manat. - **TND**: Indicates the currency is Tunisian dinar. - **TOP**: Indicates the currency is Tongan pa'anga. - **TRY**: Indicates the currency is Turkish lira. - **TTD**: Indicates the currency is Trinidad and Tobago dollar. - **TWD**: Indicates the currency is New Taiwan dollar. - **TZS**: Indicates the currency is Tanzanian shilling. - **UAH**: Indicates the currency is Ukrainian hryvnia. - **UGX**: Indicates the currency is Ugandan shilling. - **USD**: Indicates the currency is United States dollar. - **UYU**: Indicates the currency is Uruguayan peso. - **UZS**: Indicates the currency is Uzbekistani som. - **VEF**: Indicates the currency is Venezuelan bolivar. - **VND**: Indicates the currency is Vietnamese dong. - **VUV**: Indicates the currency is Vanuatu vatu. - **WST**: Indicates the currency is Samoan tala. - **XAF**: Indicates the currency is CFA franc BEAC. - **XCD**: Indicates the currency is East Caribbean dollar. - **XOF**: Indicates the currency is CFA franc BCEAO. - **XPF**: Indicates the currency is CFP franc. - **YER**: Indicates the currency is Yemeni rial. - **ZAR**: Indicates the currency is South African rand. - **ZMW**: Indicates the currency is Zambian kwacha. - **ZWL**: Indicates the currency is Zimbabwean dollar.
**Type:** string

### ErrorDetailV3
**Description:** The type that defines the fields that can be returned in an error.
**Type:** object

**Properties:**
- **category** (string)
  - This string value indicates the error category. There are three categories of errors: _request errors_, _application errors_, and _system errors_.
- **domain** (string)
  - The name of the primary system where the error occurred. This is relevant for application errors.
- **errorId** (integer)
  - A unique code that identifies the particular error or warning that occurred. Your application can use error codes as identifiers in your customized error-handling algorithms.
- **inputRefIds** (array)
  - An array of reference IDs that identify the specific request elements most closely associated to the error or warning, if any.
- **longMessage** (string)
  - A detailed description of the condition that caused the error or warning, and information on what to do to correct the problem.
- **message** (string)
  - A description of the condition that caused the error or warning.
- **outputRefIds** (array)
  - An array of reference IDs that identify the specific response elements most closely associated to the error or warning, if any.
- **parameters** (array)
  - An array of warning and error messages that return one or more variables contextual information about the error or warning. This is often the field or value that triggered the error or warning.
- **subdomain** (string)
  - The name of the subdomain in which the error or warning occurred.

### ErrorParameterV3
**Description:** An array of name/value pairs that provide details regarding the error.
**Type:** object

**Properties:**
- **name** (string)
  - This is the name of input field that caused an issue with the call request.
- **value** (string)
  - This is the actual value that was passed in for the element specified in the `name` field.

### Image
**Description:** This type defines the details of an image, such as size and image URL. Currently, only `imageUrl` is populated. The `height` and `width` are reserved for future use.
**Type:** object

**Properties:**
- **height** (integer)
  - Reserved for future use.
- **imageUrl** (string)
  - The URL of the image.
- **width** (integer)
  - Reserved for future use.

### ItemLocationImpl
**Description:** The type that defines the fields for the location of an item, such as information typically used for an address, including postal code, county, state/province, street address, city, and country (2-digit ISO code).
**Type:** object

**Properties:**
- **addressLine1** (string)
  - The first line of the street address.
- **addressLine2** (string)
  - The second line of the street address. This field may contain such values as an apartment or suite number.
- **city** (string)
  - The city in which the item is located.  
  
**Restriction:** This field is populated in the `search` method response _only_ when `fieldgroups` = `EXTENDED`.
- **country** (CountryCodeEnum)
  - The two-letter [ISO 3166](<https://www.iso.org/iso-3166-country-codes.html >) standard code that indicates the country in which the item is located.
- **county** (string)
  - The county in which the item is located.
- **postalCode** (string)
  - The postal code (or zip code in US) where the item is located. Sellers set a postal code for items when they are listed. The postal code is used for calculating proximity searches. It is anonymized when returned in `itemLocation.postalCode` via the API.
- **stateOrProvince** (string)
  - The state or province in which the item is located.

### ItemSummary
**Description:** The type that defines the fields for the details of a specific item.
**Type:** object

**Properties:**
- **additionalImages** (array)
  - An array of containers with the URLs for the images that are in addition to the primary image. The primary image is returned in the `image.imageUrl` field.
- **adultOnly** (boolean)
  - This indicates if the item is for adults only. For more information about adult-only items on eBay, refer to the [Adult items policy](<https://www.ebay.com/help/policies/prohibited-restricted-items/adult-items-policy?id=4278 >).
- **availableCoupons** (boolean)
  - This boolean attribute indicates if coupons are available for the item.  
  
**Note:** The Browse API only acknowledges item-level coupons. This field will only be returned as true if a coupon is linked with an item. It does not recognize store-level coupons offered by sellers across their entire store.
- **bidCount** (integer)
  - This integer value indicates the total number of bids that have been placed for an auction item. This field is only returned for auction items.
- **buyingOptions** (array)
  - A comma separated list of all the purchase options available for the item.  
  
**Values Returned:**

*   `FIXED_PRICE`  
    Indicates the buyer can purchase the item for a set price using the _Buy It Now_ button.
*   `AUCTION`  
    Indicates the buyer can place a bid for the item. After the first bid is placed, this becomes a live auction item and is the only buying option for this item.
*   `BEST_OFFER`  
    Items where the buyer can send the seller a price they are willing to pay for the item. The seller can accept, reject, or send a counter offer. For additional information about Best Offer, refer to [Adding Best Offer to your listing and sending offers to buyers](<https://www.ebay.com/help/selling/listings/selling-buy-now/adding-best-offer-listing?id=4144 >).
*   `CLASSIFIED_AD`  
    Indicates that the final sales transaction is to be completed outside of the eBay environment.
- **categories** (array)
  - This array returns the name and ID of each category associated with the item, including top level, branch, and leaf categories.
- **compatibilityMatch** (CompatibilityMatchEnum)
  - This indicates how well an item matches the `compatibility_filter` product attributes.  
  
**Valid Values:**

*   `EXACT`
*   `POSSIBLE`
- **compatibilityProperties** (array)
  - This container returns only the product attributes that are compatible with the item. These attributes were specified in the `compatibility_filter` in the request. This means that if you passed in 5 attributes and only 4 are compatible, only those 4 are returned. If none of the attributes are compatible, this container is not returned.
- **condition** (string)
  - The text describing the condition of the item, such as **New** or **Used**. For a list of condition names, refer to [Item Condition IDs and Names](</api-docs/sell/static/metadata/condition-id-values.html >).
- **conditionId** (string)
  - The identifier of the condition of the item. For example, `1000` is the identifier for `NEW`. For a list of condition names and IDs, refer to [Item Condition IDs and Names](</api-docs/sell/static/metadata/condition-id-values.html >).
- **currentBidPrice** (ConvertedAmount)
  - This container returns the current highest bid for an auction item. The `value` field shows the dollar value of the current highest bid, and the `currency` field (3-digit ISO code) denotes the currency associated with that bid value. This field is only returned for auction items.
- **distanceFromPickupLocation** (TargetLocation)
  - This container returns the distance away that the item is from the `pickupPostalCode` value that was supplied in the method request. This container is only returned if the "local pickup" filter fields are used in the request.
- **energyEfficiencyClass** (string)
  - This indicates the [European energy efficiency](<https://en.wikipedia.org/wiki/European_Union_energy_label >) rating (EEK) of the item. Energy efficiency ratings apply to products listed by commercial vendors in electronics categories only.  
  
Currently, this field is only applicable for the Germany site, and is returned only if the seller specifies the energy efficiency rating through item specifics at listing time. Rating values include `A+++`, `A++`, `A+`, `A`, `B`, `C`, `D`, `E`, `F`, and `G`.
- **epid** (string)
  - An ePID is the eBay product identifier of a product from the eBay product catalog. This indicates the product in which the item belongs.
- **image** (Image)
  - The URL to the primary image of the item.
- **itemAffiliateWebUrl** (string)
  - The URL to the View Item page of the item which includes the affiliate tracking ID.  
  
**Note:** In order to receive commissions on sales, eBay Partner Network affiliates must use this URL to forward buyers to the listing on the eBay marketplace.  
The `itemAffiliateWebUrl` is returned only if:

*   The marketplace through which the item is being viewed is part of the eBay Partner Network. Currently Singapore (`EBAY_SG`) is **not** supported.  
      
    For additional information, refer to [eBay Partner Network](<https://partnerhelp.ebay.com/helpcenter/s/article/countries-available-as-a-program-in-EPN?language=en_US >).
*   The seller enables affiliate tracking for the item by including the `[X-EBAY-C-ENDUSERCTX](/api-docs/buy/static/api-browse.html#Headers)` request header in the method.
- **itemCreationDate** (string)
  - The date and time when the item listing was created. This value is returned in UTC format (`yyyy-MM-ddThh:mm:ss.sssZ`), which you can convert into the local time of the buyer.  
  
This field is always returned with **itemSummaries**.
- **itemEndDate** (string)
  - A timestamp that indicates the date and time a listing is scheduled to end.  
  
This value is returned in UTC format (`yyyy-MM-ddThh:mm:ss.sssZ`), which can be converted into the local time of the buyer.
- **itemGroupHref** (string)
  - The HATEOAS reference of the parent page of the item group. An item group is an item that has various aspect differences, such as color, size, storage capacity, etc.  
  
**Note:** This field is returned only for item groups.
- **itemGroupType** (string)
  - The indicates the item group type. An item group is an item that has various aspect differences, such as color, size, storage capacity, etc.  
  
Currently only the `SELLER_DEFINED_VARIATIONS` is supported and indicates this is an item group created by the seller.  
  
**Note:** This field is returned only for item groups.
- **itemHref** (string)
  - The URI for the Browse API [getItem](/develop/api/buy/browse_api#buy-browse_api-item-getitem) method, which can be used to retrieve more details about items in the search results.
- **itemId** (string)
  - The unique RESTful identifier of the item.
- **itemLocation** (ItemLocationImpl)
  - This container returns the location of the item. This container consists of fields you typically see for an address, including postal code, county, state/province, street address, city, and country (2-digit ISO code).
- **itemOriginDate** (string)
  - The date and time when the listing was first made available. This date will be retained if an item is relisted. This value is returned in UTC format (`yyyy-MM-ddThh:mm:ss.sssZ`), which you can convert into the local time of the buyer.  
  
This timestamp is used to sort the response when the `sort=newlyListed` parameter is used.  
  
This field is always returned with **itemSummaries**.
- **itemWebUrl** (string)
  - The URL to the View Item page of the item. This enables you to include a "Report Item on eBay" hyperlink that takes the buyer to the View Item page on eBay. From there they can report any issues regarding this item to eBay.
- **leafCategoryIds** (array)
  - The leaf category IDs of the item. When the item belongs to two leaf categories, the ID values are returned in the order primary, secondary.
- **legacyItemId** (string)
  - The unique identifier of the eBay listing that contains the item. This is the traditional/legacy ID that is often seen in the URL of the listing View Item page.
- **listingMarketplaceId** (MarketplaceIdEnum)
  - The ID of the eBay marketplace on which the seller listed the item.
- **marketingPrice** (MarketingPrice)
  - This container is returned if the item is eligible for a seller discount and contains the item's original price, and the seller discount amount and percentage.
- **pickupOptions** (array)
  - This container returns the local pickup options available to the buyer. This container is returned only if the user is searching for local pickup items and set the local pickup filters in the method request.
- **price** (ConvertedAmount)
  - The price of the item after it has been converted into another currency.  
  
The price includes the value-added tax (VAT) for applicable jurisdictions when requested from supported marketplaces. In this case, users must do one or more of the following to view VAT-inclusive pricing:

*   Pass the [`X-EBAY-C-MARKETPLACE-ID`](/api-docs/static/rest-request-components.html#HTTP) request header specifying the supported marketplace (such as `EBAY_GB`)
*   Pass the `contextualLocation` values for the supported marketplace in the [`X-EBAY-C-ENDUSERCTX`](/api-docs/buy/static/api-browse.html#Headers) request header
*   Specify the supported marketplace using the [`deliveryCountry`](/api-docs/buy/static/ref-buy-browse-filters.html#deliveryCountry) `filter` URI parameter (such as `filter=deliveryCountry:GB`)

**Note:** For more information on VAT, refer to [Your VAT Obligations in the UK & EU](<https://www.ebay.co.uk/help/listings/default/vat-obligations-eu?id=4650 >).
- **priceDisplayCondition** (PriceDisplayConditionEnum)
  - Indicates when in the buying flow the item's price can appear for minimum advertised price (MAP) items, which is the lowest price a retailer can advertise/show for this item.
- **priorityListing** (boolean)
  - This field is returned as `true` if the listing is part of a Promoted Listing campaign. Promoted Listings are available to **Above Standard** and **Top Rated** sellers with recent sales activity.  
  
**Note:** Priority Listing is returned only with a Best Match sort and will not be returned for other sort options.
- **qualifiedPrograms** (array)
  - An array of the qualified programs available for the item, such as `EBAY_PLUS`, `AUTHENTICITY_GUARANTEE`, and `AUTHENTICITY_VERIFICATION`.  
  
eBay Plus is a premium account option for buyers, which provides benefits such as fast, free domestic shipping and free returns on selected items. Sellers must commit to next-day delivery of those items.The eBay [Authenticity Guarantee](<https://pages.ebay.com/authenticity-guarantee/ >) program enables third-party authenticators to perform authentication verification inspections on items such as watches and sneakers.  
  
**Note:** eBay Plus was recently deprecated on the eBay Germany marketplace, and this feature is now only available on eBay Australia marketplace.
- **seller** (Seller)
  - This container returns basic information about the seller of the item, such as name, feedback score, etc.
- **shippingOptions** (array)
  - This container returns the shipping options available to ship the item.
- **shortDescription** (string)
  - This text string is derived from the item condition and the item aspects (such as size, color, capacity, model, brand, etc.) Sometimes the title does not provide enough information but the description is too big. Surfacing the `shortDescription` can often provide buyers with the additional information that could help them make a buying decision.  
  
For example:

"**title**": "Petrel U42W FPV Drone RC Quadcopter w/HD Camera Live Video One Key Off / Landing",  
"**shortDescription**": "1 U42W Quadcopter. Syma X5SW-V3 Wifi FPV RC Drone Quadcopter 2.4Ghz 6-Axis Gyro with Headless Mode. Syma X20 Pocket Drone 2.4Ghz Mini RC Quadcopter Headless Mode Altitude Hold. One Key Take Off / Landing function: allow beginner to easy to fly the drone without any skill.",

  
**Restriction:** This field is returned by the **search** method only when `fieldgroups` = `EXTENDED`.
- **thumbnailImages** (array)
  - An array of thumbnail images for the item.
- **title** (string)
  - The seller-created title of the item.  
  
**Maximum Length:** 80 characters
- **topRatedBuyingExperience** (boolean)
  - This indicates if the item is a top-rated plus item. There are three benefits of a top-rated plus item: a minimum 30-day money-back return policy; shipping the item in 1 business day with tracking provided; and the added comfort of knowing that this item is from an experienced seller with the highest buyer ratings. For more information, refer to [Look for Top Rated Plus Items](<https://pages.ebay.com/topratedplus/index.html >) and [Seller performance overview](<https://www.ebay.com/help/selling/seller-levels-performance-standards/seller-levels-performance-standards?id=4080 >).
- **tyreLabelImageUrl** (string)
  - The URL to the image that shows the information on the tyre label.
- **unitPrice** (ConvertedAmount)
  - The price per unit for the item. Some European countries require listings for certain types of products to include the price per unit so buyers can accurately compare prices.  
  
For example:

"unitPricingMeasure": "100g",  
 "unitPrice": {  
  "value": "7.99",  
  "currency": "GBP"
- **unitPricingMeasure** (string)
  - The designation, such as size, weight, volume, count, etc., that was used to specify the quantity of the item. This helps buyers compare prices.  
  
For example, the following tells the buyer that the item is 7.99 per 100 grams.

"unitPricingMeasure": "100g",  
 "unitPrice": {  
  "value": "7.99",  
  "currency": "GBP"
- **watchCount** (integer)
  - The number of users that have added the item to their watch list.  
  
**Note:** This field is restricted to applications that have been granted permission to access this feature. You must submit an [App Check ticket](</my/support/tickets?tab=app-check >) to request this access. In the App Check form, add a note to the **Application Title/Summary** and/or **Application Details** fields indicating that you want access to Watch Count data in the Browse API.

### MarketingPrice
**Description:** The type that defines the fields that describe a seller discount.
**Type:** object

**Properties:**
- **discountAmount** (ConvertedAmount)
  - This container returns the monetary amount of the seller discount.
- **discountPercentage** (string)
  - This field expresses the percentage of the seller discount based on the value in the **originalPrice** container.
- **originalPrice** (ConvertedAmount)
  - This container returns the monetary amount of the item without the discount.
- **priceTreatment** (PriceTreatmentEnum)
  - Indicates the pricing treatment (discount) that was applied to the price of the item.  
  
**Note:** The pricing treatment affects the way and where the discounted price can be displayed.

### MarketplaceIdEnum
**Description:** An enumerated type for the values that represent eBay marketplaces. | - **EBAY_AU**: This enumeration value indicates that the eBay Marketplace is the Australia site (ebay.com.au). - **EBAY_AT**: This enumeration value indicates that the eBay Marketplace is the Austria site (ebay.at). - **EBAY_BE**: This enumeration value indicates that the eBay marketplace is the Belgium (Dutch) site (www.ebay.be). - **EBAY_CA**: This enumeration value indicates that the eBay Marketplace is the Canada (English) site (ebay.ca). - **EBAY_CH**: This enumeration value indicates that the eBay Marketplace is the Switzerland site (ebay.ch). - **EBAY_CN**: This enumeration value indicates that the eBay Marketplace is the China site (ebay.com/sch/China). - **EBAY_CZ**: This enumeration value indicates that the eBay Marketplace is the Czech Republic site (ebay.com/sch/Czech-Republic). - **EBAY_DE**: This enumeration value indicates that the eBay Marketplace is the Germany site (ebay.de). - **EBAY_DK**: This enumeration value indicates that the eBay Marketplace is the Denmark site (ebay.com/sch/Denmark). - **EBAY_ES**: This enumeration value indicates that the eBay Marketplace is the Spain site (ebay.es). - **EBAY_FI**: This enumeration value indicates that the eBay Marketplace is the Finland site (ebay.com/sch/Finland). - **EBAY_FR**: This enumeration value indicates that the eBay Marketplace is the France site (ebay.fr). - **EBAY_GB**: This enumeration value indicates that the eBay Marketplace is the UK site (ebay.co.uk). - **EBAY_GR**: This enumeration value indicates that the eBay Marketplace is the Greece site (ebay.com/sch/Greece). - **EBAY_HALF_US**: This enumeration value is no longer applicable as the Half.com site no longer exists. - **EBAY_HK**: This enumeration value indicates that the eBay Marketplace is the Hong Kong site (ebay.com.hk). - **EBAY_HU**: This enumeration value indicates that the eBay Marketplace is the Hungary site (ebay.com/sch/Hungary). - **EBAY_ID**: This enumeration value indicates that the eBay Marketplace is the Indonesia site (id.ebay.com). - **EBAY_IE**: This enumeration value indicates that the eBay Marketplace is the Ireland site (ebay.ie). - **EBAY_IL**: This enumeration value indicates that the eBay Marketplace is the Israel site (ebay.com/sch/Israel). - **EBAY_IN**: This enumeration value indicates that the eBay Marketplace is the India site (ebay.in). Note: eBay India is no longer a functioning eBay marketplace. - **EBAY_IT**: This enumeration value indicates that the eBay Marketplace is the Italy site (ebay.it). - **EBAY_JP**: This enumeration value indicates that the eBay Marketplace is the Japan site (ebay.co.jp). - **EBAY_MOTORS_US**: This enumeration value indicates that the eBay Marketplace is the US eBay Motors site (ebay.com/motors). - **EBAY_MY**: This enumeration value indicates that the eBay Marketplace is the Malaysia site (ebay.com/my). - **EBAY_NL**: This enumeration value indicates that the eBay Marketplace is the Netherlands site (ebay.nl). - **EBAY_NO**: This enumeration value indicates that the eBay Marketplace is the Norway site (ebay.com/sch/Norway). - **EBAY_NZ**: This enumeration value indicates that the eBay Marketplace is the New Zealand site (ebay.com/sch/New-Zealand). - **EBAY_PE**: This enumeration value indicates that the eBay Marketplace is the Peru site (ebay.com/sch/Peru). - **EBAY_PH**: This enumeration value indicates that the eBay Marketplace is the Philippines site (ebay.ph). - **EBAY_PL**: This enumeration value indicates that the eBay Marketplace is the Poland site (ebay.pl). - **EBAY_PR**: This enumeration value indicates that the eBay Marketplace is the Puerto Rico site (ebay.com/sch/Puerto-Rico). - **EBAY_PT**: This enumeration value indicates that the eBay Marketplace is the Portugal site (ebay.com/sch/Portugal). - **EBAY_RU**: This enumeration value indicates that the eBay Marketplace is the Russia site (ebay.com/sch/Russia). - **EBAY_SE**: This enumeration value indicates that the eBay Marketplace is the Sweden site (ebay.com/sch/Sweden). - **EBAY_SG**: This enumeration value indicates that the eBay Marketplace is the Singapore site (ebay.com/sg). - **EBAY_TH**: This enumeration value indicates that the eBay Marketplace is the Thailand site (export.ebay.co.th). - **EBAY_TW**: This enumeration value indicates that the eBay Marketplace is the Taiwan site (ebay.com/tw). - **EBAY_US**: This enumeration value indicates that the eBay Marketplace is the US site (ebay.com). - **EBAY_VN**: This enumeration value indicates that the eBay Marketplace is the Vietnam site (ebay.vn). - **EBAY_ZA**: This enumeration value indicates that the eBay Marketplace is the South Africa site (ebay.com/sch/South-Africa).
**Type:** string

### PickupOptionSummary
**Description:** The type that defines the fields for the local pickup options that are available for the item. It is used by the `pickupOptions` container.
**Type:** object

**Properties:**
- **pickupLocationType** (string)
  - This container returns the local pickup options available to the buyer. Possible values are `ARRANGED_LOCATION` and `STORE`.

### PriceDisplayConditionEnum
**Description:** An enumerated type for the values that represent when in the buying flow the item's price can appear for minimum advertised price (MAP) items, which is the lowest price a retailer can advertise/show for this item. | - **ONLY_SHOW_WHEN_ADDED_IN_CART**: Indicates the minimum advertised price of the item can be shown only after the item has been added to the cart. - **ONLY_SHOW_ON_REQUEST**: Indicates the minimum advertised price can be shown only when the buyer requests to see it. - **ALWAYS_SHOW**: Indicates there are no restrictions as to when the minimum advertised price of the item can be shown.
**Type:** string

### PriceTreatmentEnum
**Description:** An enumerated type for the values that represent a discount type. | - **MINIMUM_ADVERTISED_PRICE**: Indicates the price treatment is Minimum Advertised Price (MAP). This is the lowest price the item is allowed to be advertised/shown at and can be shown only after the item has been added to the cart. For details about when in the buying flow the item's price can appear, refer to [priceDisplayConditionEnum](/develop/api/buy/browse_api#buy-browse_api-item_summary-search.itemsummary.pricedisplaycondition). - **LIST_PRICE**: Indicates the price treatment is Strike Through Pricing (STP). For this treatment, the list price, which is crossed off (struck through) and discounted price are shown. List price is the price a seller recently listed the item for sale or sold the item for. - **MARKDOWN**: Indicates the price treatment is a markdown. The price before the markdown (Was price) is shown as well as the discount price. This item is part of a seller promotion and has an end date.
**Type:** string

### Refinement
**Description:** This type defines the fields for the various refinements of an item. You can use the information in this container to create histograms, which help shoppers choose exactly what they want.
**Type:** object

**Properties:**
- **aspectDistributions** (array)
  - An array of containers for the all the aspect refinements.
- **buyingOptionDistributions** (array)
  - An array of containers for the all the buying option refinements.
- **categoryDistributions** (array)
  - An array of containers for the all the category refinements.
- **conditionDistributions** (array)
  - An array of containers for the all the condition refinements.
- **dominantCategoryId** (string)
  - The identifier of the category that most of the items are part of.

### SearchPagedCollection
**Description:** The type that defines the fields for a paginated result set. The response consists of 0 or more sequenced _pages_ where each page has 0 or more items.
**Type:** object

**Properties:**
- **autoCorrections** (AutoCorrections)
  - The auto-corrected inputs.
- **href** (string)
  - The URI of the current page of results.  
  
The following example of the **search** method returns items 1 thru 5 from the list of items found.

https://api.ebay.com/buy/v1/item\_summary/search?q=shirt&limit=5&offset=0
- **itemSummaries** (array)
  - An array of the items on this page. The items are sorted according to the sorting method specified in the request.
- **limit** (integer)
  - The value of the `limit` parameter submitted in the request, which is the maximum number of items to return on a page, from the result set. A result set is the complete set of items returned by the method.
- **next** (string)
  - The URI for the next page of results. This value is returned if there is an additional page of results to return from the result set.  
  
The following example of the **search** method returns items 5 thru 10 from the list of items found.

https://api.ebay.com/buy/v1/item\_summary/search?query=t-shirts&limit=5&offset=10

  
  
**Note:** If the `next` field is not returned in the response, it indicates that you have reached the last page of results and there are no additional records available for retrieval.
- **offset** (integer)
  - This value indicates the `offset` used for current page of items being returned. Assume the initial request used an `offset` of `0` and a `limit` of `3`. Then in the first page of results, this value would be `0`, and items 1-3 are returned. For the second page, this value is `3` and so on.
- **prev** (string)
  - The URI for the previous page of results. This is returned if there is a previous page of results from the result set.  
  
The following example of the **search** method returns items 1 thru 5 from the list of items found, which would be the first set of items returned.

https://api.ebay.com/buy/v1/item\_summary/search?query=t-shirts&limit=5&offset=0
- **refinement** (Refinement)
  - The container for all the search refinements.
- **total** (integer)
  - The total number of items that match the input criteria.  
  
**Note:** `total` is just an indicator of the number of listings for a given query. It could vary based on the number of listings with variations included in the result. It is strongly recommended that `total` not be used in pagination use cases. Instead, use [next](</api-docs/buy/browse/resources/item_summary/methods/search#response.next >) to determine the results on the next page.
- **warnings** (array)
  - The container with all the warnings for the request.

### Seller
**Description:** The type that defines the fields for basic information about the seller of the item returned by the `item_summary` resource.
**Type:** object

**Properties:**
- **feedbackPercentage** (string)
  - The percentage of the total positive feedback.
- **feedbackScore** (integer)
  - The feedback score of the seller. This value is based on the ratings from eBay members that bought items from this seller.
- **sellerAccountType** (string)
  - Indicates if the seller is a business or an individual. This is determined when the seller registers with eBay:

*   If they register for a business account, this value will be `BUSINESS`.
*   If they register for a private account, this value will be `INDIVIDUAL`.

This designation is required by the tax laws in some countries.  
  
This field is returned only on the following sites:  
  
EBAY\_AT, EBAY\_BE, EBAY\_CH, EBAY\_DE, EBAY\_ES, EBAY\_FR, EBAY\_GB, EBAY\_IE, EBAY\_IT, EBAY\_PL  
  
**Valid Values:** `BUSINESS` or `INDIVIDUAL`
- **username** (string)
  - The user name created by the seller for use on eBay.  
  
**Note:** Effective September 26, 2025, select developers will no longer receive username data for U.S. users through this field. Instead, an immutable user ID will be returned in its place. For more information, please refer to [Data Handling Compliance](/api-docs/static/data-handling-update.html).

### ShippingOptionSummary
**Description:** The type that defines the fields for the shipping information.
**Type:** object

**Properties:**
- **guaranteedDelivery** (boolean)
  - Although this field is still returned, it can be ignored since eBay Guaranteed Delivery is no longer a supported feature on any marketplace. This field may get removed from the schema in the future.
- **maxEstimatedDeliveryDate** (string)
  - The end date of the delivery window (latest projected delivery date). This value is returned in UTC format (yyyy-MM-ddThh:mm:ss.sssZ), which you can convert into the local time of the buyer.  
  
**Note:** For the best accuracy, always include the `contextualLocation` values in the [`X-EBAY-C-ENDUSERCTX`](/api-docs/buy/static/api-browse.html#Headers) request header.  
**Note:** Estimated delivery dates are not returned for CBT items.
- **minEstimatedDeliveryDate** (string)
  - The start date of the delivery window (earliest projected delivery date). This value is returned in UTC format (yyyy-MM-ddThh:mm:ss.sssZ), which you can convert into the local time of the buyer.  
  
**Note:** For the best accuracy, always include the `contextualLocation` values in the [`X-EBAY-C-ENDUSERCTX`](/api-docs/buy/static/api-browse.html#Headers) request header.  
**Note:** Estimated delivery dates are not returned for CBT items.
- **shippingCost** (ConvertedAmount)
  - This is the estimated price to ship the item.  
  
The price includes the value-added tax (VAT) for applicable jurisdictions when requested from supported marketplaces. In this case, users must do one or more of the following to see VAT-inclusive pricing:

*   Pass the [`X-EBAY-C-MARKETPLACE-ID`](/api-docs/static/rest-request-components.html#HTTP) request header specifying the supported marketplace (such as `EBAY_GB`)
*   Pass the `contextualLocation` values for the supported marketplace in the [`X-EBAY-C-ENDUSERCTX`](/api-docs/buy/static/api-browse.html#Headers) request header
*   Specify the supported marketplace using the [`deliveryCountry`](/api-docs/buy/static/ref-buy-browse-filters.html#deliveryCountry) **filter** URI parameter (such as `filter=deliveryCountry:GB`)

**Note:**For more information on VAT, refer to [Your VAT Obligations in the UK & EU](<https://www.ebay.co.uk/help/listings/default/vat-obligations-eu?id=4650 >).
- **shippingCostType** (string)
  - Indicates the type of shipping used to ship the item. Possible values are `FIXED` (flat-rate shipping) and `CALCULATED` (shipping cost calculated based on item and buyer location).

### TargetLocation
**Description:** The type that defines the fields for the distance between the item location and the buyer's location.
**Type:** object

**Properties:**
- **unitOfMeasure** (string)
  - This value shows the unit of measurement used to measure the distance between the location of the item and the buyer's location. This value is typically `mi` or `km`.
- **value** (string)
  - This value indicates the distance (measured in the measurement unit in the **unitOfMeasure** field) between the item location and the buyer's location.

### SearchByImageRequest
**Description:** The type that defines the fields for the image information.
**Type:** object

**Properties:**
- **image** (string)
  - The Base64 string of the image.  
  
To get the Base64 image string, you can use sites such as [https://codebeautify.org/image-to-base64-converter](<https://codebeautify.org/image-to-base64-converter >).

### AdditionalProductIdentity
**Description:** The type that defines the array of product identifiers associated with the item. This container is returned if the seller has associated the eBay Product Identifier (ePID) with the item, and in the request `fieldgroups` is set to `PRODUCT`.
**Type:** object

**Properties:**
- **productIdentity** (array)
  - An array of product identifier/value pairs for the product associated with the item. This is returned if the seller has associated the eBay Product Identifier (ePID) with the item and the request has `fieldgroups` set to `PRODUCT`.  
  
The following table shows what is returned, based on the item information provided by the seller, when `fieldgroups` is set to `PRODUCT`.  
  

ePID Provided

Product ID(s) Provided

Response

No

No

The `AdditionalProductIdentity` container is _not_ returned.

No

Yes

The `AdditionalProductIdentity` container is _not_ returned but the product identifiers specified by the seller are returned in the `localizedAspects` container.

Yes

No

The `AdditionalProductIdentity` container is returned listing the product identifiers of the product.

Yes

Yes

The `AdditionalProductIdentity` container is returned listing all the product identifiers of the product and the product identifiers specified by the seller are returned in the `localizedAspects` container.

### AddonService
**Description:** This type defines an add-on service that may be selected for an item or that may apply automatically. A charge may be associated with the add-on service.
**Type:** object

**Properties:**
- **selection** (AddonServiceSelectionEnum)
  - This field indicates whether the add-on service must be selected for the item.
- **serviceFee** (ConvertedAmount)
  - The amount charged for the add-on service.
- **serviceId** (string)
  - The ID number of the add-on service.
- **serviceType** (AddonServiceTypeEnum)
  - The type of add-on service, such as `AUTHENTICITY_GUARANTEE`.

### AddonServiceSelectionEnum
**Description:** An enumerated type that indicates if an add-on service is optional or automatically included. | - **OPTIONAL**: This value indicates that the add-on service may be selected as an option. - **REQUIRED**: This value indicates that the add-on service applies automatically and is not a selectable option.
**Type:** object

### AddonServiceTypeEnum
**Description:** An enumerated type that defines add-on services. | - **AUTHENTICITY_GUARANTEE**: This enum value indicates that the add-on service is eBay Authenticity Guarantee service, in which a product's authenticity is verified by experts before shipping to the buyer. For more information, refer to [Authenticity Guarantee](<https://pages.ebay.com/authenticity-guarantee-seller >) on the eBay Seller site.
**Type:** object

### Address
**Description:** The type that defines the fields for an address.
**Type:** object

**Properties:**
- **addressLine1** (string)
  - The first line of the street address.  
  
**Note:** This is conditionally returned in the `itemLocation` field.
- **addressLine2** (string)
  - The second line of the street address. This field is not always used, but can be used for "Suite Number" or "Apt Number".
- **city** (string)
  - The city of the address.
- **country** (CountryCodeEnum)
  - The two-letter [ISO 3166](<https://www.iso.org/iso-3166-country-codes.html >) standard code for the country of the address.
- **county** (string)
  - The county of the address.
- **postalCode** (string)
  - The postal code (or zip code in US) code of the address. Sellers set a postal code (or zip code in US) for items when they are listed. The postal code is used for calculating proximity searches. It is anonymized when returned in `itemLocation.postalCode` via the API.
- **stateOrProvince** (string)
  - The state or province of the address.  
  
**Note:** This is conditionally returned in the `itemLocation` field.

### Amount
**Description:** This type describes the value of a monetary amount as represented by a global currency.
**Type:** object

**Properties:**
- **currency** (CurrencyCodeEnum)
  - The list of valid currencies. Each [ISO 4217](<https://www.iso.org/iso-4217-currency-codes.html >) currency code includes the currency name followed by the numeric value.  
  
For example, the Canadian Dollar code (CAD) would take the following form: `Canadian Dollar, 124`.
- **value** (string)
  - The monetary value of the amount in the currency defined by the **currency** field.

### Aspect
**Description:** The type that defines the fields for the name/value pairs for the aspects of the product. For example: BRAND/Apple
**Type:** object

**Properties:**
- **localizedName** (string)
  - The text representing the name of the aspect for the name/value pair, such as Brand.
- **localizedValues** (array)
  - The text representing the value of the aspect for the name/value pair, such as Apple.

### AspectGroup
**Description:** This type defines the aspects and localized name of a groups of an aspect group.
**Type:** object

**Properties:**
- **aspects** (array)
  - An array of the name/value pairs for the aspects of the product. For example: BRAND/Apple
- **localizedGroupName** (string)
  - The name of a group of aspects.  
  
In the following example, **Product Identifiers** and **Process** are product aspect group names. Under the group name are the product aspect name/value pairs.  
  
**Product Identifiers**  
   Brand/Apple  
   Product Family/iMac  
  
**Processor**  
   Processor Type/Intel  
   Processor Speed/3.10

### AuthenticityGuaranteeProgram
**Description:** A type that identifies whether the item is qualified for the Authenticity Guarantee program.
**Type:** object

**Properties:**
- **description** (string)
  - An indication that the item is qualified for the Authenticity Guarantee program.
- **termsWebUrl** (string)
  - The URL to the Authenticity Guarantee program terms of use.

### AuthenticityVerificationProgram
**Description:** A type that identifies whether the item is from a verified seller.
**Type:** object

**Properties:**
- **description** (string)
  - An indication that the item is from a verified seller.
- **termsWebUrl** (string)
  - The URL to the Authenticity Verification program terms of use.

### AvailabilityStatusEnum
**Description:** An enumerated type for the values that represent the inventory status of an item. | - **IN_STOCK**: Indicates the item is available for purchase. - **LIMITED_STOCK**: Indicates the item is available for purchase but the supply of this item is low. - **OUT_OF_STOCK**: Indicates the item is not available for purchase because the supply of this item is currently zero.
**Type:** object

### AvailabilityThresholdEnum
**Description:** An enumerated type for the values that represent the availability of an item. | - **MORE_THAN**: Indicates that quantity of the item is more than 10. If the quantity is less than 10, the quantity is returned in the **estimatedAvailableQuantity** field.
**Type:** object

### AvailableCoupon
**Description:** This type defines the specifics of an available coupon, such as its constraints, discount amount, discount type, description, coupon code, and terms of use.
**Type:** object

**Properties:**
- **constraint** (CouponConstraint)
  - The limitations or restrictions of the coupon.
- **discountAmount** (Amount)
  - The discount amount after the coupon is applied.
- **discountType** (CouponDiscountTypeEnum)
  - The type of discount that the coupon applies.
- **message** (string)
  - A description of the coupon.  
  
**Note:** The value returned in the `termsWebUrl` field should appear for all experiences when displaying coupons. The value in the `availableCoupons.message` field must also be included if returned in the API response.
- **redemptionCode** (string)
  - The coupon code.
- **termsWebUrl** (string)
  - The URL to the coupon terms of use.  
  
**Note:** The value returned in the `termsWebUrl` field should appear for all experiences when displaying coupons. The value in the `availableCoupons.message` field must also be included if returned in the API response.

### CompanyAddress
**Description:** This type is used to provide contact information for the manufacturer of the product.
**Type:** object

**Properties:**
- **addressLine1** (string)
  - The first line of the product manufacturer's street address.
- **addressLine2** (string)
  - The second line of the product manufacturer's street address. This field is not always used, but can be used for secondary address information such as 'Suite Number' or 'Apt Number'.
- **city** (string)
  - The city of the product manufacturer's street address.
- **companyName** (string)
  - The company name of the product manufacturer.
- **contactUrl** (string)
  - The contact URL of the product manufacturer.
- **country** (CountryCodeEnum)
  - The two-letter [ISO 3166](<https://www.iso.org/iso-3166-country-codes.html >) standard code for the country of the address.
- **countryName** (string)
  - The country name of the product manufacturer's street address.
- **county** (string)
  - The county of the product manufacturer's street address.
- **email** (string)
  - The product manufacturer's business email address.
- **phone** (string)
  - The product manufacturer's business phone number.
- **postalCode** (string)
  - The postal code of the product manufacturer's street address.
- **stateOrProvince** (string)
  - The state or province of the product manufacturer's street address.

### ConditionDescriptor
**Description:** This type displays additional information about the condition of an item in a structured format.
**Type:** object

**Properties:**
- **name** (string)
  - The name of a condition descriptor. The value(s) for this condition descriptor is returned in the associated **values** array.
- **values** (array)
  - This array displays the value(s) for a condition descriptor (denoted by the associated **name** field), as well as any other additional information about the condition of the item.

### ConditionDescriptorValue
**Description:** This type displays the value(s) associated with the specified condition descriptor name, as well as any additional information about a condition descriptor.
**Type:** object

**Properties:**
- **additionalInfo** (array)
  - Additional information about the condition of an item as it relates to a condition descriptor. This array elaborates on the value specified in the **content** field and provides additional details about the condition of an item.
- **content** (string)
  - The value for the condition descriptor indicated in the associated **name** field.

### CouponConstraint
**Description:** This type is used to provide the expiration date of a coded coupon.
**Type:** object

**Properties:**
- **expirationDate** (string)
  - This timestamp provides the expiration date of the coded coupon.

### DeliveryOptionsEnum
**Description:** The enumerated type that defines the values that represent how the item can be delivered.  
  
Code so that your app gracefully handles any future changes to this list. | - **SHIP_TO_HOME**: Indicates the item can be shipped to the recipient. - **SELLER_ARRANGED_LOCAL_PICKUP**: Indicates the seller will arrange to have the buyer pick-up the item. (Local delivery option) - **IN_STORE_PICKUP**: Indicates the buyer will pick-up the item in a store. (Local delivery option) - **PICKUP_DROP_OFF**: Indicates the item is dropped off or sent to a pickup location and the buyer collects the item at that location. - **DIGITAL_DELIVERY**: Indicates the item is delivered via email.
**Type:** object

### EconomicOperator
**Description:** The type that provides required Economic Operator information about the manufacturer and/or supplier of the item.
**Type:** object

**Properties:**
- **companyName** (string)
  - The company name of the registered Economic Operator.
- **addressLine1** (string)
  - The first line of the registered Economic Operator's street address.
- **addressLine2** (string)
  - The second line, if any, of the registered Economic Operator's street address. This field is not always used, but can be used for 'Suite Number' or 'Apt Number'.
- **city** (string)
  - The city of the registered Economic Operator's street address.
- **stateOrProvince** (string)
  - The state or province of the registered Economic Operator's street address.
- **postalCode** (string)
  - The postal code of the registered Economic Operator's street address.
- **country** (string)
  - The two-letter [ISO 3166](<https://www.iso.org/iso-3166-country-codes.html >) standard abbreviation of the country of the registered Economic Operator's address.
- **phone** (string)
  - The registered Economic Operator's business phone number.
- **email** (string)
  - The registered Economic Operator's business email address.

### EstimatedAvailability
**Description:** The type that defines the fields for the estimated item availability information.
**Type:** object

**Properties:**
- **availabilityThreshold** (integer)
  - This field is return only when the seller sets their '[display item quantity](#display-item-quantity)' preference to **Display "More than 10 available" in your listing (if applicable)**. The value of this field will be "10", which is the threshold value.  
  
Code so that your app gracefully handles any future changes to this value.
- **availabilityThresholdType** (AvailabilityThresholdEnum)
  - This field is return only when the seller sets their **Display Item Quantity** preference to **Display "More than 10 available" in your listing (if applicable)**. The value of this field will be `MORE_THAN`. This indicates that the seller has more than the 'quantity display preference', which is 10, in stock for this item.  
  
The following are the display item quantity preferences the seller can set.  

*   **Display "More than 10 available" in your listing (if applicable)**
    *   If the seller enables this preference, this field is returned as long as there are more than 10 of this item in inventory.
    *   If the quantity is equal to 10 or drops below 10, this field is not returned and the estimated quantity of the item is returned in the **estimatedAvailableQuantity** field.
*   **Display the exact quantity in your items**  
    If the seller enables this preference, the **availabilityThresholdType** and **availabilityThreshold** fields are not returned and the estimated quantity of the item is returned in the **estimatedAvailableQuantity** field.  
      
    **Note:** Because the quantity of an item can change several times within a second, it is impossible to return the exact quantity.

  
Code so that your app gracefully handles any future changes to these preferences.
- **deliveryOptions** (array)
  - An array of available delivery options.  
  
**Valid Values:** SHIP\_TO\_HOME, SELLER\_ARRANGED\_LOCAL\_PICKUP, IN\_STORE\_PICKUP, PICKUP\_DROP\_OFF, or DIGITAL\_DELIVERY  
  
Code so that your app gracefully handles any future changes to this list.
- **estimatedAvailabilityStatus** (AvailabilityStatusEnum)
  - An enumeration value representing the inventory status of this item.  
  
**Note:** Be sure to review the **itemEndDate** field to determine whether the item is available for purchase.  
  
**Valid Values:** IN\_STOCK, LIMITED\_STOCK, or OUT\_OF\_STOCK  
  
Code so that your app gracefully handles any future changes to this list.
- **estimatedAvailableQuantity** (integer)
  - The estimated number of this item that are available for purchase. Because the quantity of an item can change several times within a second, it is impossible to return the exact quantity. So instead of returning quantity, the estimated availability of the item is returned.  
  
**Note:** To see if a listing is available for purchase, review the [itemEndDate](/develop/api/buy/browse_api#buy-browse_api-item-getitem.item.itemenddate) and [estimatedAvailablityStatus](/develop/api/buy/browse_api#buy-browse_api-item-getitem.estimatedavailability.estimatedavailabilitystatus) fields. If the item has an **EndDate** in the past, or the **estimatedAvailabilityStatus** is `OUT_OF_STOCK`, the item is unavailable for purchase.
- **estimatedRemainingQuantity** (integer)
  - The estimated number of this item that are available for purchase. Because the quantity of an item can change several times within a second, it is impossible to return the exact quantity. So instead of returning quantity, the estimated availability of the item is returned.  
  
**Note:** To see if a listing is available for purchase, review the [itemEndDate](/develop/api/buy/browse_api#buy-browse_api-item-getitem.item.itemenddate) and [estimatedAvailablityStatus](/develop/api/buy/browse_api#buy-browse_api-item-getitem.estimatedavailability.estimatedavailabilitystatus) fields. If the item has an **EndDate** in the past, or the **estimatedAvailabilityStatus** is `OUT_OF_STOCK`, the item is unavailable for purchase.
- **estimatedSoldQuantity** (integer)
  - The estimated number of this item that have been sold.

### FulfilledThroughEnum
**Description:** An enumerated type that defines the values that represent fulfillment programs. | - **GLOBAL_SHIPPING**: Indicates the item is being shipped using the eBay [Global Shipping Program](<https://pages.ebay.com/seller-center/shipping/global-shipping-program.html >). - **INTERNATIONAL_SHIPPING**: Indicates the item is being shipped using the eBay International Shipping program.
**Type:** object

### HazardPictogram
**Description:** A type that defines the pictogram for the type of hazard that a hazardous material represents.
**Type:** object

**Properties:**
- **pictogramDescription** (string)
  - The description of the hazard pictogram, such as Flammable.
- **pictogramId** (string)
  - The ID of the hazard pictogram.
- **pictogramUrl** (string)
  - The URL of the hazard pictogram.

### HazardStatement
**Description:** A type that defines the hazard statement for a hazardous material.
**Type:** object

**Properties:**
- **statementDescription** (string)
  - A description of the nature of the hazard, such as whether the material is toxic if swallowed.
- **statementId** (string)
  - The ID of the hazard statement.

### HazardousMaterialsLabels
**Description:** A type that defines the hazardous materials labels for an item.
**Type:** object

**Properties:**
- **additionalInformation** (string)
  - Additional information about the hazardous materials labels.
- **pictograms** (array)
  - An array of hazard pictograms that apply to the item.
- **signalWord** (string)
  - The signal word for the hazardous materials label (such as Danger or Warning).
- **signalWordId** (string)
  - The ID of the signal word for the hazardous materials label.
- **statements** (array)
  - An array of hazard statements for the item.

### Item
**Description:** This type describes the details of an item that can be purchased.
**Type:** object

**Properties:**
- **additionalImages** (array)
  - An array of containers with the URLs for the images that are in addition to the primary image. The primary image is returned in the **image.imageUrl** field.
- **addonServices** (array)
  - A list of add-on services that may be selected for the item or that may apply automatically.
- **adultOnly** (boolean)
  - This indicates if the item is for adults only. For more information about adult-only items on eBay, see [Adult items policy](<https://pages.ebay.com/help/policies/adult-only.html >) for sellers and [Adult-Only items on eBay](https://www.ebay.com/help/terms-conditions/default/searching-adult-items?id=4661) for buyers.
- **ageGroup** (string)
  - (Primary Item Aspect) The age group for which the product is recommended. For example, newborn, infant, toddler, kids, adult, etc. All the item aspects, including this aspect, are returned in the **localizedAspects** container.
- **authenticityGuarantee** (AuthenticityGuaranteeProgram)
  - A container for information about whether an item, or the item group when returned for the **getItemsByItemGroup** method, is qualified for the Authenticity Guarantee program.  
  
**Note:** The `AUTHENTICITY_GUARANTEE` value being returned by the **getItemsByItemGroup** method indicates that at least one item in the item group supports this program, but doesn't guarantee that the program is available to all items in the item group. To verify if the Authenticity Program is indeed available for the item that you are interested in, grab the **items.itemId** value for that item and use the **getItem** method. This method will return specific details on that particular item, including whether or not the Authenticity Guarantee Program is available for the item. Look for the **qualifiedPrograms** array and **authenticityGuarantee** container in the **getItem** response for this information.  
  
Under the Authenticity Guarantee program, the seller ships a purchased item to a a third-party authenticator who inspects the item and provides an authentication card for it before the item is shipped to the buyer. If the buyer returns the item, the authenticator first verifies that it is the same item in the same condition before returning it to the seller.  
  
**Note:** Refer to the [Authenticity Guarantee](<https://pages.ebay.com/authenticity-guarantee/ >) page for more information.
- **authenticityVerification** (AuthenticityVerificationProgram)
  - A container for information about whether an item is from a verified seller.
- **availableCoupons** (array)
  - A list of available coupons for the item.  
  
**Note:** The Browse API only acknowledges item-level coupons. This array will only return coupons linked with an item. Store-level coupons offered by sellers across their entire store will not be returned.
- **bidCount** (integer)
  - This integer value indicates the total number of bids that have been placed against an auction item. This field is returned only for auction items.
- **brand** (string)
  - (Primary Item Aspect) The name brand of the item, such as Nike, Apple, etc. All the item aspects, including this aspect, are returned in the **localizedAspects** container.
- **buyingOptions** (array)
  - A comma separated list of all the purchase options available for the item. The values returned are:

*   `FIXED_PRICE` - Indicates the buyer can purchase the item for a set price using the Buy It Now button.
*   `AUCTION` - Indicates the buyer can place a bid for the item. After the first bid is placed, this becomes a live auction item and is the only buying option for this item.
*   `BEST_OFFER` - Indicates the buyer can send the seller a price they're willing to pay for the item. The seller can accept, reject, or send a counter offer. For more information on how this works, see [Making a Best Offer](<https://www.ebay.com/help/buying/buy-now/making-best-offer?id=4019 >).
*   `CLASSIFIED_AD` - Indicates that the final sales transaction is to be completed outside of the eBay environment.

Code so that your app gracefully handles any future changes to this list.
- **categoryId** (string)
  - The ID of the leaf category for this item. A leaf category is the lowest level in that category and has no children.
- **categoryIdPath** (string)
  - The IDs of every category in the item path, separated by pipe characters, starting with the top level parent category.  
  
For example, if an item belongs to the top level category Home and Garden (category ID 11700), followed by Home Improvement (159907), Heating, Cooling and Air (69197), and Thermostats (115947), the field would return the value: `11700|159907|69197|115947`.
- **categoryPath** (string)
  - Text that shows the category hierarchy of the item. For example: Computers/Tablets & Networking, Laptops & Netbooks, PC Laptops & Netbooks
- **charityTerms** (ItemCharityTerms)
  - This container returns any applicable charity information associated with the specified item.  
  
This container is only returned if the **fieldgroups** query parameter is set to `CHARITY_DETAILS`.
- **color** (string)
  - (Primary Item Aspect) Text describing the color of the item. All the item aspects, including this aspect, are returned in the **localizedAspects** container.
- **condition** (string)
  - A short text description for the condition of the item, such as New or Used. For a list of condition names, see [Item Condition IDs and Names](</api-docs/sell/static/metadata/condition-id-values.html >).  
  
Code so that your app gracefully handles any future changes to this list.
- **conditionDescription** (string)
  - A full text description for the condition of the item. This field elaborates on the value specified in the **condition** field and provides full details for the condition of the item.
- **conditionDescriptors** (array)
  - This array is used by the seller to provide additional information about the condition of an item in a structured format. Condition descriptors are name-value attributes that indicate details about a particular condition of an item.  
  
**Note:** Condition descriptors are currently only available for the following trading card categories:

*   Non-Sport Trading Card Singles
*   CCG Individual Cards
*   Sports Trading Card Singles
- **conditionId** (string)
  - The identifier of the condition of the item. For example, 1000 is the identifier for NEW. For a list of condition names and IDs, see [Item Condition IDs and Names](</api-docs/sell/static/metadata/condition-id-values.html >).  
  
Code so that your app gracefully handles any future changes to this list.
- **currentBidPrice** (ConvertedAmount)
  - The container that returns the current highest bid for an auction item. The value (string) field shows the dollar value of the current highest bid, and the currency (3-digit ISO code) field denotes the currency associated with that bid value. This container will only be returned for auction items.
- **description** (string)
  - The full description of the item that was created by the seller. This can be plain text or rich content and can be very large.
- **ecoParticipationFee** (ConvertedAmount)
  - The Eco Participation fee, a fee paid by the buyer that is applied to the cost of the eventual disposal of the purchased item. The fee is remitted in full to the eco organization.  
  
Currently, this value is required for electronic devices and furniture.
- **eligibleForInlineCheckout** (boolean)
  - This field indicates if the item can be purchased using the Buy [Order API](/api-docs/buy/order/resources/methods).

*   If the value of this field is `true`, this indicates that the item can be purchased using the **Order API**.
*   If the value of this field is `false`, this indicates that the item cannot be purchased using the **Order API** and must be purchased on the eBay site.
- **enabledForGuestCheckout** (boolean)
  - This indicates if the item can be purchased using Guest Checkout in the [Order API](/api-docs/buy/order/resources/methods). You can use this flag to exclude items from your inventory that are not eligible for Guest Checkout, such as gift cards.
- **energyEfficiencyClass** (string)
  - This indicates the [European energy efficiency](<https://en.wikipedia.org/wiki/European_Union_energy_label >) rating (EEK) of the item. This field is returned only if the seller specified the energy efficiency rating.  
  
The rating is a set of energy efficiency classes from A to G, where 'A' is the most energy efficient and 'G' is the least efficient. This rating helps buyers choose between various models.  
  
When the manufacturer's specifications for this item are available, the link to this information is returned in the **productFicheWebUrl** field.
- **epid** (string)
  - An EPID is the eBay product identifier of a product from the eBay product catalog. This indicates the product in which the item belongs.
- **estimatedAvailabilities** (array)
  - The estimated number of this item that are available for purchase. Because the quantity of an item can change several times within a second, it is impossible to return the exact quantity. So instead of returning quantity, the estimated availability of the item is returned.
- **gender** (string)
  - (Primary Item Aspect) The gender for the item. This is used for items that could vary by gender, such as clothing. For example: male, female, or unisex. All the item aspects, including this aspect, are returned in the **localizedAspects** container.
- **gtin** (string)
  - The unique Global Trade Item number of the item as defined by [https://www.gtin.info](<https://www.gtin.info >). This can be a UPC (Universal Product Code), EAN (European Article Number), or an ISBN (International Standard Book Number) value.
- **hazardousMaterialsLabels** (HazardousMaterialsLabels)
  - Hazardous materials labels for the item.
- **image** (Image)
  - The URL of the primary image of the item. The other images of the item are returned in the **additionalImages** container.
- **immediatePay** (boolean)
  - A value of `true` indicates that the seller requires immediate payment from the buyer when purchasing an item.  
  
**Note:** It is possible for this field to be set to `true`, but not apply in some scenarios. For example, immediate payment is not applicable for auction listings that have a winning bidder, for buyers purchases that involve the Best Offer feature, or for offline transactions.
- **inferredEpid** (string)
  - The ePID (eBay Product ID of a product from the eBay product catalog) for the item, which has been programmatically determined by eBay using the item's title, aspects, and other data.  
  
If the seller provided an ePID for the item, the seller's value is returned in the **epid** field.  
  
**Note:** This field is returned only for authorized Partners.
- **itemAffiliateWebUrl** (string)
  - The URL to the View Item page of the item which includes the affiliate tracking ID.  
  
**Note:** In order to receive commissions on sales, eBay Partner Network affiliates must use this URL to forward buyers to the listing on the eBay marketplace.  
The **itemAffiliateWebUrl** is only returned if:

*   The marketplace through which the item is being viewed is part of the eBay Partner Network. Currently Singapore (`EBAY_SG`) is **not** supported.  
      
    For additional information, refer to [eBay Partner Network](<https://partnerhelp.ebay.com/helpcenter/s/article/countries-available-as-a-program-in-EPN?language=en_US >).
*   The seller enables affiliate tracking for the item by including the `[X-EBAY-C-ENDUSERCTX](/api-docs/buy/static/api-browse.html#Headers)` request header in the method.
- **itemCreationDate** (string)
  - A timestamp that indicates the date and time an item listing was created.  
  
This value is returned in UTC format (yyyy-MM-ddThh:mm:ss.sssZ), which can be converted into the local time of the buyer.
- **itemEndDate** (string)
  - A timestamp that indicates the date and time an auction listing will end.  
  
If a fixed-price listing has ended, this field indicates the date and time the listing ended.  
  
This value is returned in UTC format (`yyyy-MM-ddThh:mm:ss.sssZ`), which can be converted into the local time of the buyer.
- **itemId** (string)
  - The unique RESTful identifier of the item.
- **itemLocation** (Address)
  - The physical location of the item.
- **itemWebUrl** (string)
  - The URL of the View Item page of the item. This enables you to include a "Report Item on eBay" link that takes the buyer to the View Item page on eBay. From there they can report any issues regarding this item to eBay.
- **legacyItemId** (string)
  - The unique identifier of the eBay listing that contains the item. This is the traditional/legacy ID that is often seen in the URL of the listing View Item page.
- **listingMarketplaceId** (MarketplaceIdEnum)
  - The ID of the eBay marketplace where the item is listed.
- **localizedAspects** (array)
  - An array of containers that show the complete list of the aspect name/value pairs that describe the variation of the item.
- **lotSize** (integer)
  - The number of items in a lot. In other words, a lot size is the number of items that are being sold together.  
  
A lot is a set of two or more items included in a single listing that must be purchased together in a single order line item. All the items in the lot are the same but there can be multiple items in a single lot, such as the package of batteries shown in the example below.  
  

Item

Lot Definition

Lot Size

A package of 24 AA batteries

A box of 10 packages

10

A P235/75-15 Goodyear tire

4 tires

4

Fashion Jewelry Rings

Package of 100 assorted rings

100

  
  
**Note:** Lots are not supported in all categories.
- **manufacturer** (CompanyAddress)
  - Contact information for the manufacturer of the product.
- **marketingPrice** (MarketingPrice)
  - The original price and the discount amount and percentage.
- **material** (string)
  - (Primary Item Aspect) Text describing what the item is made of. For example, silk. All the item aspects, including this aspect, are returned in the **localizedAspects** container.
- **minimumPriceToBid** (ConvertedAmount)
  - The minimum price of the next bid, which means to place a bid it must be equal to or greater than this amount. If the auction hasn't received any bids, the minimum bid price is the same as the starting bid. Otherwise, the minimum bid price is equal to the current bid plus the bid increment. For details about bid increments, see [Automatic bidding](<https://www.ebay.com/help/buying/bidding/automatic-bidding?id=4014 >).
- **mpn** (string)
  - The manufacturer's part number, which is a unique number that identifies a specific product. To identify the product, this is always used along with brand.
- **pattern** (string)
  - (Primary Item Aspect) Text describing the pattern used on the item. For example, paisley. All the item aspects, including this aspect, are returned in the **localizedAspects** container.
- **paymentMethods** (array)
  - The payment methods for the item, including the payment method types, brands, and instructions for the buyer.
- **price** (ConvertedAmount)
  - The cost of just the item. This amount does not include any adjustments such as discounts or shipping costs.  
  
**Note:** The price does include the value-added tax (VAT) for applicable jurisdictions when requested from supported marketplaces. In this case, users must pass the [`X-EBAY-C-MARKETPLACE-ID`](/api-docs/static/rest-request-components.html#HTTP) request header specifying the supported marketplace (such as `EBAY_GB`) to see the VAT-inclusive pricing. For more information on VAT, refer to [VAT Obligations in the EU](https://www.ebay.co.uk/help/listings/default/vat-obligations-eu?id=4650&st=12&pos=1&query=Your%20VAT%20obligations%20in%20the%20EU&intent=VAT).
- **priceDisplayCondition** (PriceDisplayConditionEnum)
  - Indicates when in the buying flow the item's price can appear for minimum advertised price (MAP) items, which is the lowest price a retailer can advertise/show for this item.
- **primaryItemGroup** (ItemGroupSummary)
  - The container that returns details of a primary item group (parent ID of an item group). An item group is an item that has various aspect differences, such as color, size, storage capacity, etc.  
  
When an item group is created, one of the item variations, such as the red shirt size L, is chosen as the "parent". All the other items in the group are the children, such as the blue shirt size L, red shirt size M, etc.  
  
**Note:** This container is returned only if the **item\_id** in the request is for an item group (items with variations, such as color and size).
- **primaryProductReviewRating** (ReviewRating)
  - The container that returns the product rating details, such as review count, rating histogram, and average rating.
- **priorityListing** (boolean)
  - This field is returned as `true` if the listing is part of a Promoted Listing campaign. Promoted Listings are available to Above Standard and Top Rated sellers with recent sales activity.  
  
For more information, see [Promoted Listings](<https://pages.ebay.com/seller-center/listing-and-marketing/promoted-listings.html >).
- **product** (Product)
  - The container that returns the product information of the item.
- **productFicheWebUrl** (string)
  - The URL of a page containing the manufacturer's specification of this item, which helps buyers make a purchasing decision. This information is available only for items that include the European energy efficiency rating (EEK) but is not available for _all_ items with an EEK rating and is returned only if this information is available. The EEK rating of the item is returned in the **energyEfficiencyClass** field.
- **productSafetyLabels** (ProductSafetyLabels)
  - This container provides product safety labels which were provided by the seller, for the listing.  
  
The [getProductSafetyLabels](/api-docs/sell/metadata/resources/marketplace/methods/getProductSafetyLabels) method of the [Sell Metadata API](/api-docs/sell/metadata/static/overview.html) can be used to retrieve the full set of available Product Safety pictogram labels and safety statements.
- **qualifiedPrograms** (array)
  - An array of the qualified programs available for the item, such as `EBAY_PLUS`, `AUTHENTICITY_GUARANTEE`, and `AUTHENTICITY_VERIFICATION`.  
  
eBay Plus is a premium account option for buyers, which provides benefits such as fast, free domestic shipping and free returns on selected items. Sellers must commit to next-day delivery of those items.The eBay [Authenticity Guarantee](<https://pages.ebay.com/authenticity-guarantee/ >) program enables third-party authenticators to perform authentication verification inspections on items such as watches and sneakers.  
  
**Note:** eBay Plus was recently deprecated on the eBay Germany marketplace, and this feature is now only available on eBay Australia marketplace.
- **quantityLimitPerBuyer** (integer)
  - The maximum number for a specific item that one buyer can purchase.
- **repairScore** (string)
  - A score that describes how easy it is to repair the product. Score values range from 0.1 (hardest to repair) to 10.0 (easiest), always including a single decimal place.
- **reservePriceMet** (boolean)
  - This indicates if the reserve price of the item has been met. A reserve price is set by the seller and is the minimum amount the seller is willing to sell the item for.

If the highest bid is not equal to or higher than the reserve price when the auction ends, the listing ends and the item is not sold.

**Note:** This is returned only for auctions that have a reserve price.
- **responsiblePersons** (array)
  - This array provides information about one or more EU-based Responsible Persons or entities associated with the listing.
- **returnTerms** (ItemReturnTerms)
  - The container that returns an overview of the seller's return policy.
- **seller** (SellerDetail)
  - The container that returns basic and detailed about the seller of the item, such as name, feedback score, and contact information.
- **sellerCustomPolicies** (array)
  - A list of the custom policies that are applied to a listing.
- **sellerItemRevision** (string)
  - An identifier generated/incremented when a seller revises the item. There are two types of item revisions:

*   Seller changes, such as changing the title
*   eBay system changes, such as changing the quantity when an item is purchased

This ID is changed _only_ when the seller makes a change to the item. This means you cannot use this value to determine if the quantity has changed.
- **shippingOptions** (array)
  - An array of shipping options containers that have the details about cost, carrier, etc. of one shipping option.  
  
**Note:** For items with calculated shipping, this array is only returned if the **X-EBAY-C-ENDUSERCTX** header is supplied.
- **shipToLocations** (ShipToLocations)
  - The container that returns the geographic regions to be included and excluded that define where the item can be shipped.
- **shortDescription** (string)
  - This text string is derived from the item condition and the item aspects (such as size, color, capacity, model, brand, etc.).
- **size** (string)
  - (Primary Item Aspect) The size of the item. For example, '7' for a size 7 shoe. All the item aspects, including this aspect, are returned in the **localizedAspects** container.
- **sizeSystem** (string)
  - (Primary Item Aspect) The sizing system of the country. All the item aspects, including this aspect, are returned in the **localizedAspects** container.  
  
**Valid Values:**  
AU (Australia),  
BR (Brazil),  
CN (China),  
DE (Germany),  
EU (European Union),  
FR (France),  
IT (Italy),  
JP (Japan),  
MX (Mexico),  
US (USA),  
UK (United Kingdom)  
  
Code so that your app gracefully handles any future changes to this list.
- **sizeType** (string)
  - (Primary Item Aspect) Text describing a size group in which the item would be included, such as regular, petite, plus, big-and-tall or maternity. All the item aspects, including this aspect, are returned in the **localizedAspects** container.
- **subtitle** (string)
  - A subtitle is optional and allows the seller to provide more information about the product, possibly including keywords that may assist with search results.
- **taxes** (array)
  - The container for the tax information for the item.
- **title** (string)
  - The seller-created title of the item.  
  
**Maximum Length:** 80 characters
- **topRatedBuyingExperience** (boolean)
  - This indicates if the item a top-rated plus item. There are three benefits of a top-rated plus item: a minimum 30-day money-back return policy, shipping the items in 1 business day with tracking provided, and the added comfort of knowing this item is from experienced sellers with the highest buyer ratings. See the [Top Rated Plus Items](<https://pages.ebay.com/topratedplus/index.html >) and [Becoming a Top Rated Seller and qualifying for Top Rated Plus](<https://pages.ebay.com/help/sell/top-rated.html >) help topics for more information.
- **tyreLabelImageUrl** (string)
  - The URL to the image that shows the information on the tyre label.
- **uniqueBidderCount** (integer)
  - This integer value indicates the number of different eBay users who have placed one or more bids on an auction item. This field is only applicable to auction items.
- **unitPrice** (ConvertedAmount)
  - This is the price per unit for the item. Some European countries require listings for certain types of products to include the price per unit so buyers can accurately compare prices.  
  
For example:  
  
`"unitPricingMeasure": "100g",   "unitPrice": {     "value": "7.99",     "currency": "GBP"`
- **unitPricingMeasure** (string)
  - The designation, such as size, weight, volume, count, etc., that was used to specify the quantity of the item. This helps buyers compare prices.  
  
For example, the following tells the buyer that the item is 7.99 per 100 grams.  
  
`"unitPricingMeasure": "100g",   "unitPrice": {     "value": "7.99",     "currency": "GBP"`
- **warnings** (array)
  - An array of warning messages. These types of errors do not prevent the method from executing but should be checked.
- **watchCount** (integer)
  - The number of users that have added the item to their watch list.  
  
**Note:** This field is restricted to applications that have been granted permission to access this feature. You must submit an [App Check ticket](<https://developer.ebay.com/my/support/tickets?tab=app-check >) to request this access. In the App Check form, add a note to the **Application Title/Summary** and/or **Application Details** fields that you want access to Watch Count data in the Browse API.

### ItemCharityTerms
**Description:** This type defines the fields for any applicable charity information associated with an item.
**Type:** object

**Properties:**
- **charityOrgId** (string)
  - The eBay-assigned unique identifier of the charitable organization that will receive a percentage of the sales proceeds from the item.
- **donationPercentage** (number)
  - The percentage of the purchase price of the item that the charitable organization (identified in the **charityOrgId** field) will receive for each sale.
- **LogoImage** (Image)
  - The details of the charity's logo image, such as the size and URL.  
  
**Note:** Currently, only the **imageUrl** is populated.
- **name** (string)
  - The name of the charity organization.
- **website** (string)
  - The URL to the charity's eBay page.

### ItemGroupSummary
**Description:** The type that defines the fields for the details of each item in an item group. An item group is an item that has various aspect differences, such as color, size, storage capacity, etc. When an item group is created, one of the item variations, such as the red shirt size L, is chosen as the "parent". All the other items in the group are the children, such as the blue shirt size L, red shirt size M, etc.  
  
**Note:** This container is returned only if the **item\_id** in the request is an item group (parent ID of an item with variations).
**Type:** object

**Properties:**
- **itemGroupAdditionalImages** (array)
  - An array of containers with the URLs for images that are in addition to the primary image of the item group. The primary image is returned in the **itemGroupImage** field.
- **itemGroupHref** (string)
  - The HATEOAS reference of the parent page of the item group. An item group is an item that has various aspect differences, such as color, size, storage capacity, etc.
- **itemGroupId** (string)
  - The unique identifier for the item group. An item group is an item that has various aspect differences, such as color, size, storage capacity, etc.
- **itemGroupImage** (Image)
  - The URL of the primary image of the item group. An item group is an item that has various aspect differences, such as color, size, storage capacity, etc.
- **itemGroupTitle** (string)
  - The title of the item that appears on the item group page. An item group is an item that has various aspect differences, such as color, size, storage capacity, etc.
- **itemGroupType** (ItemGroupTypeEnum)
  - An enumeration value that indicates the type of the item group. An item group is an item that has various aspect differences, such as color, size, storage capacity, etc.

### ItemGroupTypeEnum
**Description:** An enumerated type for the values that represent the type of the item group. An item group is an item that has various aspect differences, such as color, size, storage capacity, etc.  
  
Code so that your app gracefully handles any future changes to this list. | - **SELLER_DEFINED_VARIATIONS**: Indicates this group was created by the seller. Currently, this is the only value supported.
**Type:** object

### ItemReturnTerms
**Description:** The type that defines the fields for the seller's return policy.
**Type:** object

**Properties:**
- **extendedHolidayReturnsOffered** (boolean)
  - This indicates if the seller has enabled the Extended Holiday Returns feature on the item. Extended Holiday Returns are only applicable during the US holiday season, and gives buyers extra time to return an item. This 'extra time' will typically extend beyond what is set through the **returnPeriod** value.
- **refundMethod** (RefundMethodEnum)
  - An enumeration value that indicates how a buyer is refunded when an item is returned.  
  
**Valid Values:** MONEY\_BACK or MERCHANDISE\_CREDIT  
  
Code so that your app gracefully handles any future changes to this list.
- **restockingFeePercentage** (string)
  - This string field indicates the restocking fee percentage that the seller has set on the item. Sellers have the option of setting no restocking fee for an item, or they can set the percentage to 10, 15, or 20 percent. So, if the cost of the item was $100, and the restocking percentage was 20 percent, the buyer would be charged $20 to return that item, so instead of receiving a $100 refund, they would receive $80 due to the restocking fee.
- **returnInstructions** (string)
  - Text written by the seller describing what the buyer needs to do in order to return the item.
- **returnMethod** (ReturnMethodEnum)
  - An enumeration value that indicates the alternative methods for a full refund when an item is returned. This field is returned if the seller offers the buyer an item replacement or exchange instead of a monetary refund.  
  
**Valid Values:**

*   **REPLACEMENT** - Indicates that the buyer has the option of receiving money back for the returned item, or they can choose to have the seller replace the item with an identical item.
*   **EXCHANGE** - Indicates that the buyer has the option of receiving money back for the returned item, or they can exchange the item for another similar item.

Code so that your app gracefully handles any future changes to this list.
- **returnPeriod** (TimeDuration)
  - The amount of time the buyer has to return the item after the purchase date.
- **returnsAccepted** (boolean)
  - Indicates whether the seller accepts returns for the item.
- **returnShippingCostPayer** (ReturnShippingCostPayerEnum)
  - This enumeration value indicates whether the buyer or seller is responsible for return shipping costs when an item is returned.  
  
**Valid Values:**

*   **SELLER** - Indicates the seller will pay for the shipping costs to return the item.
*   **BUYER** - Indicates the buyer will pay for the shipping costs to return the item.

Code so that your app gracefully handles any future changes to this list.

### LegalAddress
**Description:** This type defines the fields for the seller's address.
**Type:** object

**Properties:**
- **addressLine1** (string)
  - The first line of the street address.
- **addressLine2** (string)
  - The second line of the street address. This field is not always used, but can be used for 'Suite Number' or 'Apt Number'.
- **city** (string)
  - The city of the address.
- **country** (CountryCodeEnum)
  - The two-letter [ISO 3166](<https://www.iso.org/iso-3166-country-codes.html >) standard code for the country of the address.
- **countryName** (string)
  - The name of the country of the address.
- **county** (string)
  - The name of the county of the address.
- **postalCode** (string)
  - The postal code of the address.
- **stateOrProvince** (string)
  - The state or province of the address.

### PaymentInstructionEnum
**Description:** An enumerated type for the values that represent the payment instructions, such as _cash in person_ or _contact seller_. | - **DIRECT_DEBIT**: This enumeration value indicates that eBay will use the debit card information input by the buyer to process the payment. - **ACH**: This enumeration value indicates that the Payflow ACH Payment Service will be used, which enables eBay to process payments through the ACH network and request credit or debit information from the buyer's checking or savings account. - **EFT**: This enumeration value indicates that eBay will process the payment via electronic funds transfer. - **CIP**: This enumeration value indicates that the payment method will be cash, and the transaction will occur in-person. - **MONEY_TRANSFER**: This enumeration value indicates that eBay will process the payment via money transfer. - **CASH_IN_PERSON**: This enumeration value indicates that the payment method will be cash, and the transaction will occur in-person. - **CASH_ON_PICKUP**: This enumeration value indicates that the payment method will be cash, and the transaction will occur when the buyer picks up the item. - **CASH_ON_DELIVERY**: This enumeration value indicates that the payment method will be cash, and the transaction will occur after the item is delivered to the buyer. - **CONTACT_SELLER**: This enumeration value indicates that the buyer should contact the seller for payment instructions. - **PAY_UPON_INVOICE**: This enumeration value indicates that eBay will process the payment upon invoice.
**Type:** object

### PaymentMethod
**Description:** This type defines information about the payment method for a listing.
**Type:** object

**Properties:**
- **paymentMethodType** (PaymentMethodTypeEnum)
  - The payment method type, such as credit card or cash.
- **paymentMethodBrands** (array)
  - The payment method brands, including the payment method brand type and logo image.
- **paymentInstructions** (array)
  - The payment instructions for the buyer, such as _cash in person_ or _contact seller_.
- **sellerInstructions** (array)
  - The seller instructions to the buyer, such as _accepts credit cards_ or _see description_.

### PaymentMethodBrand
**Description:** This type defines information about the brand for a payment method.
**Type:** object

**Properties:**
- **paymentMethodBrandType** (PaymentMethodBrandEnum)
  - The payment method brand, such as Visa or PayPal.
- **logoImage** (Image)
  - The details of the logo image, such as the size and URL.  
  
**Note:** Currently, only the **imageUrl** is populated.

### PaymentMethodBrandEnum
**Description:** An enumerated type for the values that represent the payment method brand, such as Visa or PayPal. | - **VISA**: This enumeration value indicates that Visa is an authorized brand for credit or debit card transactions. - **MASTERCARD**: This enumeration value indicates that Mastercard is an authorized brand for credit or debit card transactions. - **DISCOVER**: This enumeration value indicates that Discover is an authorized brand for credit card transactions. - **AMERICAN_EXPRESS**: This enumeration value indicates that American Express is an authorized brand for credit card transactions. - **CB_NATIONALE**: This enumeration value indicates that Carte Bancaire (CB) Nationale is an authorized brand for credit card transactions. - **CETELEM**: This enumeration value indicates that Cetelem is an authorized brand for credit card transactions. - **COFIDIS**: This enumeration value indicates that Confidis is an authorized brand for credit card transactions. - **COFINOGA**: This enumeration value indicates that Cofinoga is an authorized brand for credit card transactions. - **MAESTRO**: This enumeration value indicates that Maestro is an authorized brand for credit card transactions. - **SWITCH**: This enumeration value indicates that Switch is an authorized brand for credit card transactions. - **POSTEPAY**: This enumeration value indicates that Postepay is an authorized brand for credit card transactions. - **CB**: This enumeration value indicates that Carte Bancaire is an authorized brand for credit card transactions. - **DINERS_CLUB**: This enumeration value indicates that Diners Club is an authorized brand for credit card transactions. - **UNION_PAY**: This enumeration value indicates that UnionPay is an authorized brand for credit card transactions. - **PAYPAL_CREDIT**: This enumeration value indicates that PayPal is an authorized brand for credit transactions. - **PAYPAL**: This enumeration value indicates that PayPal is an authorized brand for Wallet transactions. - **GOOGLE_PAY**: GOOGLE_PAY - **APPLE_PAY**: This enumeration value indicates that Apple Pay is an authorized brand for Wallet transactions. - **QIWI**: This enumeration value indicates that Qiwi is an authorized brand for Wallet transactions.
**Type:** object

### PaymentMethodTypeEnum
**Description:** An enumerated type for the values that represent the payment method, such as credit card or cash.  
  
Code so that your app gracefully handles any future changes to this list. | - **CREDIT_CARD**: This enumeration value indicates that the payment can be processed via credit card, using the brand(s) specified in the corresponding **paymentMethodBrands** array. - **WALLET**: This enumeration value indicates that the payment can be processed via wallet, using the brand(s) specified in the corresponding **paymentMethodBrands** array. - **DEBIT_CARD**: This enumeration value indicates that the payment can be processed via debit card, using the brand(s) specified in the corresponding **paymentMethodBrands** array. - **CREDIT**: This enumeration value indicates that the payment can be processed via PayPal credit. - **BANK**: This enumeration value indicates that the payment can be processed through bank transfer, using the method(s) specified in the corresponding **paymentInstructions** array. - **CASH**: This enumeration value indicates that the payment can be made via cash transaction, using the method(s) specified in the corresponding **paymentInstructions** array. - **OTHER**: This enumeration value indicates that no payment methods have been specified. Contact the seller for more information or see the **SellerInstructionEnum** response for details. - **CHECK**: This enumeration value indicates that the payment can be processed via check. - **MONEY_ORDER**: This enumeration value indicates that the payment can be processed via money order. - **WIRE_TRANSFER**: This enumeration value indicates that the payment can be processed via wire-transfer. - **DEFERRED**: This enumeration value indicates that the payment will be processed upon invoice, as specified in the **paymentInstructions** array.
**Type:** object

### Product
**Description:** The type that defines the fields for the product information of the item.
**Type:** object

**Properties:**
- **additionalImages** (array)
  - An array of containers with the URLs for the product images that are in addition to the primary image.
- **additionalProductIdentities** (array)
  - An array of product identifiers associated with the item. This container is returned if the seller has associated the eBay Product Identifier (ePID) with the item and in the request **fieldgroups** is set to `PRODUCT`.
- **aspectGroups** (array)
  - An array of containers for the product aspects. Each group contains the aspect group name and the aspect name/value pairs.
- **brand** (string)
  - The brand associated with product. To identify the product, this is always used along with MPN (manufacturer part number).
- **description** (string)
  - The rich description of an eBay product, which might contain HTML.
- **gtins** (array)
  - An array of all the possible GTINs values associated with the product. A GTIN is a unique Global Trade Item number of the item as defined by [https://www.gtin.info](<https://www.gtin.info >). This can be a UPC (Universal Product Code), EAN (European Article Number), or an ISBN (International Standard Book Number) value.
- **image** (Image)
  - The primary image of the product. This is often a stock photo.
- **mpns** (array)
  - An array of all possible MPN values associated with the product. A MPNs is manufacturer part number of the product. To identify the product, this is always used along with brand.
- **title** (string)
  - The title of the product.

### ProductIdentity
**Description:** The type that defines the fields for the product identifier type/value pairs of product associated with an item.
**Type:** object

**Properties:**
- **identifierType** (string)
  - The type of product identifier, such as UPC and EAN.
- **identifierValue** (string)
  - The product identifier value.

### ProductSafetyLabelPictogram
**Description:** This type is used to provide product safety pictogram(s) for the listing.
**Type:** object

**Properties:**
- **pictogramDescription** (string)
  - The description of the safety label pictogram.
- **pictogramId** (string)
  - The identifier of the safety label pictogram.
- **pictogramUrl** (string)
  - The URL of the safety label pictogram.

### ProductSafetyLabelStatement
**Description:** This type is used to describe the seller provided product safety label statement.
**Type:** object

**Properties:**
- **statementDescription** (string)
  - A description of the nature of the product safety label statement.
- **statementId** (string)
  - The identifier of the product safety label statement.

### ProductSafetyLabels
**Description:** This type contains seller provided product safety pictograms and statements for the listing.
**Type:** object

**Properties:**
- **pictograms** (array)
  - An array of seller provided comma-separated string values that provides identifier, URL, and description for one or more pictograms associated with the listing.
- **statements** (array)
  - An array of seller provided comma-separated string values that provide identifier and description for one or more product safety statements associated with the listing.

### RatingHistogram
**Description:** The type that defines the fields for product ratings. Only products that are in the eBay product catalog can be reviewed and rated.
**Type:** object

**Properties:**
- **count** (integer)
  - The total number of user ratings that the product has received.
- **rating** (string)
  - This is the average rating for the product. As part of a product review, users rate the product. Products are rated from one star (terrible) to five stars (excellent), with each star having a corresponding point value - one star gets 1 point, two stars get 2 points, and so on. If a product had one four-star rating and one five-star rating, its average rating would be `4.5`, and this is the value that would appear in this field.

### RefundMethodEnum
**Description:** An enumerated type for the values that represent how a refund is given to the buyer when an item is returned.  
  
Code so that your app gracefully handles any future changes to this list. | - **MONEY_BACK**: Indicates the buyer gets their money back for the returned item. If the item has a restocking fee (see the **restockingFeePercentage** field), the buyer's refund will be reduced by this amount. - **MERCHANDISE_CREDIT**: If this field is returned, the buyer actually has the option of getting their money back, or the buyer may choose to request an exchange or replacement for the returned item. The value in the **returnMethod** field will indicate whether the seller does exchanges or replacements.
**Type:** object

### Region
**Description:** This type is used to provide region details for a tax jurisdiction.
**Type:** object

**Properties:**
- **regionName** (string)
  - A localized text string that indicates the name of the region. Taxes are generally charged at the state/province level or at the country level in the case of VAT tax.
- **regionType** (RegionTypeEnum)
  - An enumeration value that indicates the type of region for the tax jurisdiction.  
  
**Valid Values:**

*   **STATE\_OR\_PROVINCE** \- Indicates the region is a state or province within a country, such as California or New York in the US, or Ontario or Alberta in Canada.
*   **COUNTRY** \- Indicates the region is a single country.

Code so that your app gracefully handles any future changes to this list.

### RegionTypeEnum
**Description:** An enumerated type for the values that represent geographic regions. This type is used to indicate the shipping region level/type for a shipping region, and is also used to indicate level/type of a tax jurisdiction. | - **COUNTRY_REGION**: This enumeration value indicates the region is a domestic region or special location within a country. A seller will generally specify these regions as places they are not willing to ship to within a country.  
  
For examples of `COUNTRY_REGION` IDs and values, refer to the [regionId](/develop/api/buy/browse_api#buy-browse_api-item-getitem.shiptoregion.regionid) and/or [regionName](/api-docs/buy/browse/resources/item/methods/getItem#response.shipToLocations.regionExcluded.regionName) field descriptions.  
  
This value is not applicable for a tax jurisdiction. - **STATE_OR_PROVINCE**: This enumeration value indicates the region is a state or province within a country, such as California or New York in the US, or Ontario or Alberta in Canada.  
  
For examples of `STATE_OR_PROVINCE` IDs and values, refer to the [regionId](/develop/api/buy/browse_api#buy-browse_api-item-getitem.shiptoregion.regionid) and/or [regionName](/develop/api/buy/browse_api#buy-browse_api-item-getitem.shiptoregion.regionname) field descriptions. - **COUNTRY**: This enumeration value indicates the region is a country. The two-letter code for the country, as defined by the [ISO 3166](<https://www.iso.org/iso-3166-country-codes.html >) standard, will be returned in the `regionId` field, and in the `regionName` field, the name of the country will be a localized text string. - **WORLD_REGION**: This enumeration value indicates the region is a continent or a large geographical region.  
  
For examples of `WORLD_REGION` IDs and values, refer to the [regionId](/develop/api/buy/browse_api#buy-browse_api-item-getitem.shiptoregion.regionid) and/or [regionName](/develop/api/buy/browse_api#buy-browse_api-item-getitem.shiptoregion.regionname) field descriptions.  
  
This value is not applicable for a tax jurisdiction. - **WORLDWIDE**: Indicates the region is the entire world.  
  
This value is _only_ applicable to included shipping regions and not apply to excluded shipping regions. If a seller ships to many global locations, but does have a few regions and/or countries that are exceptions, that seller may specify `WORLDWIDE` as the included region, and will also specify the exceptions through the excluded regions list.  
  
In the `regionName` field, "Worldwide" will be localized, and in the `regionId` field, the value will be `WORLDWIDE`  
  
This value is not applicable for a tax jurisdiction.
**Type:** object

### ResponsiblePerson
**Description:** This type provides information, such as name and contact details, for an EU-based Responsible Person or entity, associated with the product.
**Type:** object

**Properties:**
- **addressLine1** (string)
  - The first line of the Responsible Person's street address.
- **addressLine2** (string)
  - The second line of the Responsible Person's address. This field is not always used, but can be used for secondary address information such as 'Suite Number' or 'Apt Number'.
- **city** (string)
  - The city of the Responsible Person's street address.
- **companyName** (string)
  - The name of the Responsible Person or entity.
- **contactUrl** (string)
  - The contact URL of the Responsible Person or entity.
- **country** (CountryCodeEnum)
  - The two-letter [ISO 3166](<https://www.iso.org/iso-3166-country-codes.html >) standard of the country of the address.
- **countryName** (string)
  - The country name of the Responsible Person's street address.
- **county** (string)
  - The county of the Responsible Person's street address.
- **email** (string)
  - The email of the Responsible Person's street address.
- **phone** (string)
  - The phone number of the Responsible Person's street address.
- **postalCode** (string)
  - The postal code of the Responsible Person's street address.
- **stateOrProvince** (string)
  - The state or province of the Responsible Person's street address.
- **types** (array)
  - The type(s) associated with the Responsible Person or entity.

### ResponsiblePersonTypeEnum
**Description:** This enumerated type is used to indicate the type of EU Responsible Person associated with a listing. | - **EU_RESPONSIBLE_PERSON**: This enum value indicates the Responsible person is an EU Responsible Person. An EU Responsible Person is crucial for ensuring that products comply with all relevant regulations and safety standards to protect human health.
**Type:** object

### ReturnMethodEnum
**Description:** An enumerated type for the values that represent the alternative methods for a full refund when an item is returned.  
  
Code so that your app gracefully handles any future changes to this list. | - **REPLACEMENT**: Indicates that the buyer has the option of receiving money back for the returned item, or they can choose to have the seller replace the item with an identical item. - **EXCHANGE**: Indicates that the buyer has the option of receiving money back for the returned item, or they can exchange the item for another similar item.
**Type:** object

### ReturnShippingCostPayerEnum
**Description:** An enumerated type for the values that represent who will pay the return shipping costs. | - **SELLER**: Indicates the seller will pay for the shipping costs to return the item. - **BUYER**: Indicates the buyer will pay for the shipping costs to return the item.
**Type:** object

### ReviewRating
**Description:** The type that defines the fields for the rating of a product review.
**Type:** object

**Properties:**
- **averageRating** (string)
  - The average rating given to a product based on customer reviews.
- **ratingHistograms** (array)
  - An array of containers for the product rating histograms that shows the review counts and the product rating.
- **reviewCount** (integer)
  - The total number of reviews for the item.

### SellerCustomPolicy
**Description:** This type defines the custom policies that apply to a listed item.
**Type:** object

**Properties:**
- **description** (string)
  - The seller-defined description of the policy.
- **label** (string)
  - The seller-defined label for an individual custom policy.
- **type** (SellerCustomPolicyTypeEnum)
  - The type of custom policy, such as PRODUCT\_COMPLIANCE or TAKE\_BACK.

### SellerCustomPolicyTypeEnum
**Description:** An enumerated type for the kinds of custom policy that sellers may apply to a listing. | - **PRODUCT_COMPLIANCE**: A policy that provides the required regulatory information and disclosures for certain product types. - **TAKE_BACK**: A policy that applies when applicable law requires the seller to take back a used product when the buyer buys a new product.
**Type:** object

### SellerDetail
**Description:** The type that defines the fields for basic and detailed information about the seller of the item returned by the **item** resource.
**Type:** object

**Properties:**
- **feedbackPercentage** (string)
  - The percentage of the total positive feedback.
- **feedbackScore** (integer)
  - The feedback score of the seller. This value is based on the ratings from eBay members that bought items from this seller.
- **sellerAccountType** (string)
  - This indicates if the seller is a business or an individual. This is determined when the seller registers with eBay. If they register for a business account, this value will be `BUSINESS`. If they register for a private account, this value will be `INDIVIDUAL`. This designation is required by the tax laws in the following countries:  
  
This field is applicable only on the following marketplaces:  

*   EBAY\_AT
*   EBAY\_BE
*   EBAY\_CH
*   EBAY\_DE
*   EBAY\_ES
*   EBAY\_FR
*   EBAY\_GB
*   EBAY\_IE
*   EBAY\_IT
*   EBAY\_PL

**Note:** This field will be returned empty on unsupported marketplaces.  
**Valid Values:** `BUSINESS` or `INDIVIDUAL`
- **sellerLegalInfo** (SellerLegalInfo)
  - The container with the seller's contact info and fields that are required by law.
- **userId** (string)
  - The unique identifier of an eBay user across all eBay sites. This value does not change, even when a user changes their username.
- **username** (string)
  - The user name created by the seller for use on eBay.  
  
**Note:** Effective September 26, 2025, select developers will no longer receive username data for U.S. users through this field. Instead, an immutable user ID will be returned in its place. For more information, please refer to [Data Handling Compliance](/api-docs/static/data-handling-update.html).

### SellerInstructionEnum
**Description:** An enumerated type for the values that represent the seller instructions to the buyer.  
  
Code so that your app gracefully handles any future changes to this list. | - **ACCEPTS_CREDIT_CARD**: This enumeration value indicates that credit card is an acceptable payment method for the seller. - **SEE_DESCRIPTION**: This enumeration value indicates that the seller has provided special instructions within the listing description.
**Type:** object

### SellerLegalInfo
**Description:** The type that defines the fields for the contact information for a seller.
**Type:** object

**Properties:**
- **email** (string)
  - The seller's business email address.
- **fax** (string)
  - The seller' business fax number.
- **imprint** (string)
  - This is a free-form string created by the seller. This is information often found on business cards, such as address. This is information used by some countries.
- **legalContactFirstName** (string)
  - The seller's first name.
- **legalContactLastName** (string)
  - The seller's last name.
- **name** (string)
  - The name of the seller's business.
- **phone** (string)
  - The seller's business phone number.
- **registrationNumber** (string)
  - The seller's registration number. This is information used by some countries.
- **sellerProvidedLegalAddress** (LegalAddress)
  - The container that returns the seller's address to be used to contact them.
- **termsOfService** (string)
  - This is a free-form string created by the seller. This is the seller's terms or condition, which is in addition to the seller's return policies.
- **vatDetails** (array)
  - An array of the seller's VAT (value added tax) IDs and the issuing country. VAT is a tax added by some European countries.
- **economicOperator** (EconomicOperator)
  - Provides required information about the manufacturer and/or supplier of the item.
- **weeeNumber** (string)
  - The Waste Electrical and Electronic Equipment (WEEE) registration number required for any seller to place electrical and electronic equipment on the market in Germany. This manufacturer number is assigned to the first distributors of electrical and electronic equipment and comprises a country code and an 8-digit sequence of digits (e.g. 'WEEE Reg. No. DE 12345678').

### ShipToLocation
**Description:** The type that defines the fields for the country and postal code of where an item is to be shipped.
**Type:** object

**Properties:**
- **country** (CountryCodeEnum)
  - The two-letter [ISO 3166](<https://www.iso.org/iso-3166-country-codes.html >) standard of the country for where the item is to be shipped.
- **postalCode** (string)
  - The zip code (postal code) for where the item is to be shipped.

### ShipToLocations
**Description:** The type that defines the fields that include and exclude geographic regions affecting where the item can be shipped. The seller defines these regions when listing the item.
**Type:** object

**Properties:**
- **regionExcluded** (array)
  - An array of containers that express the large geographical regions, countries, state/provinces, or special locations within a country where the seller is not willing to ship to.
- **regionIncluded** (array)
  - An array of containers that express the large geographical regions, countries, or state/provinces within a country where the seller is willing to ship to. Prospective buyers must look at the shipping regions under this container, as well as the shipping regions that are under the **regionExcluded** to see where the seller is willing to ship items. Sellers can specify that they ship 'Worldwide', but then add several large geographical regions (e.g. Asia, Oceania, Middle East) to the exclusion list, or sellers can specify that they ship to Europe and Africa, but then add several individual countries to the exclusion list.

### ShipToRegion
**Description:** This type is used provide details about included and excluded shipping regions.
**Type:** object

**Properties:**
- **regionId** (string)
  - The unique identifier of the shipping region. The value returned here is dependent on the corresponding **regionType** value. The **regionId** value for a region does not vary based on the eBay marketplace. However, the corresponding **regionName** value for a region is a localized, text-based description of the shipping region.  
  
If the **regionType** value is `WORLDWIDE`, the **regionId** value will also be `WORLDWIDE`.  
  
If the **regionType** value is `WORLD_REGION`, the **regionId** value will be one of the following: `AFRICA`, `AMERICAS`, `ASIA`, `AUSTRALIA`, `CENTRAL_AMERICA_AND_CARIBBEAN`, `EUROPE`, `EUROPEAN_UNION`, `GREATER_CHINA`, `MIDDLE_EAST`, `NORTH_AMERICA`, `OCEANIA`, `SOUTH_AMERICA`, `SOUTHEAST_ASIA` or `CHANNEL_ISLANDS`.  
  
If the **regionType** value is `COUNTRY`, the **regionId** value will be the two-letter code for the country, as defined in the [ISO 3166](<https://www.iso.org/iso-3166-country-codes.html >) standard.  
  
If the **regionType** value is `STATE_OR_PROVINCE`, the **regionId** value will either be the two-letter code for US states and DC (as defined on this [Social Security Administration](<https://www.ssa.gov/international/coc-docs/states.html >) page), or the two-letter code for Canadian provinces (as defined by this [Canada Post](<https://www.canadapost.ca/tools/pg/manual/PGaddress-e.asp?ecid=murl10006450#1442131 >) page).  
  
If the **regionType** value is `COUNTRY_REGION`, the **regionId** value may be one of following: `_AH` (if a seller is not willing to ship to Alaska/Hawaii), `_PR` (if the seller is not willing to ship to US Protectorates), `_AP` (if seller is not willing to ship to a US Army or Fleet Post Office), and `PO_BOX` (if the seller is not willing to ship to a Post Office Box).
- **regionName** (string)
  - A localized text string that indicates the name of the shipping region. The value returned here is dependent on the corresponding **regionType** value.  
  
If the **regionType** value is `WORLDWIDE`, the **regionName** value will show `Worldwide`.  
  
If the **regionType** value is `WORLD_REGION`, the **regionName** value will be a localized text string for one of the following large geographical regions: Africa, Americas, Asia, Australia, Central America and Caribbean, Europe, European Union, Greater China, Middle East, North America, Oceania, South America, Southeast Asia, or Channel Islands.  
  
If the **regionType** value is `COUNTRY`, the **regionName** value will be a localized text string for any country in the world.  
  
If the **regionType** value is `STATE_OR_PROVINCE`, the **regionName** value will be a localized text string for any US state or Canadian province.  
  
If the **regionType** value is `COUNTRY_REGION`, the **regionName** value may be a localized version of one of the following: Alaska/Hawaii, US Protectorates, APO/FPO (Army or Fleet Post Office), or PO BOX.
- **regionType** (RegionTypeEnum)
  - An enumeration value that indicates the level or type of shipping region.  
  
**Valid Values:**

*   **COUNTRY\_REGION** \- Indicates the region is a domestic region or special location within a country.
*   **STATE\_OR\_PROVINCE** \- Indicates the region is a state or province within a country, such as California or New York in the US, or Ontario or Alberta in Canada.
*   **COUNTRY** \- Indicates the region is a single country.
*   **WORLD\_REGION** \- Indicates the region is a world region, such as Africa, the Middle East, or Southeast Asia.
*   **WORLDWIDE** \- Indicates the region is the entire world. This value is only applicable for included shiping regions, and not excluded shipping regions.

For more detail on the actual **regionName**/**regionId** values that will be returned based on the **regionType** value, see the [regionId](/develop/api/buy/browse_api#buy-browse_api-item-getitem.shiptoregion.regionid) and/or [regionName](/develop/api/buy/browse_api#buy-browse_api-item-getitem.shiptoregion.regionname) field descriptions.  
  
Code so that your app gracefully handles any future changes to this list.

### ShippingOption
**Description:** The type that defines the fields for the details of a shipping provider.
**Type:** object

**Properties:**
- **additionalShippingCostPerUnit** (ConvertedAmount)
  - Any per item additional shipping costs for a multi-item purchase. For example, let's say the shipping cost for a power cord is $3. But for an additional cord, the shipping cost is only $1. So if you bought 3 cords, the **shippingCost** would be $3 and this value would be $2 ($1 for each additional item).
- **cutOffDateUsedForEstimate** (string)
  - The deadline date that the item must be purchased by in order to be received by the buyer within the delivery window ( **maxEstimatedDeliveryDate** and **minEstimatedDeliveryDate** fields). This field is returned only for items that are eligible for 'Same Day Handling'. For these items, the value of this field is what is displayed in the **Delivery** line on the View Item page.  
  
This value is returned in UTC format (yyyy-MM-ddThh:mm:ss.sssZ), which you can convert into the local time of the buyer.
- **fulfilledThrough** (FulfilledThroughEnum)
  - If the item is being shipped by the eBay [Global Shipping program](<https://pages.ebay.com/seller-center/shipping/global-shipping-program.html >), this field returns `GLOBAL_SHIPPING`.  
  
If the item is being shipped using the eBay International Shipping program, this field returns `INTERNATIONAL_SHIPPING`.  
  
Otherwise, this field is null.
- **guaranteedDelivery** (boolean)
  - Although this field is still returned, it can be ignored since eBay Guaranteed Delivery is no longer a supported feature on any marketplace. This field may get removed from the schema in the future.
- **importCharges** (ConvertedAmount)
  - The [Global Shipping Program](<https://pages.ebay.com/seller-center/shipping/global-shipping-program.html >) import charges for this item.
- **maxEstimatedDeliveryDate** (string)
  - The end date of the delivery window (latest projected delivery date). This value is returned in UTC format (yyyy-MM-ddThh:mm:ss.sssZ), which you can convert into the local time of the buyer.  
  
**Note:** For the best accuracy, always include the location of where the item is be shipped in the `contextualLocation` values of the [`X-EBAY-C-ENDUSERCTX`](/api-docs/buy/static/api-browse.html#Headers) request header.
- **minEstimatedDeliveryDate** (string)
  - The start date of the delivery window (earliest projected delivery date). This value is returned in UTC format (yyyy-MM-ddThh:mm:ss.sssZ), which you can convert into the local time of the buyer.  
  
**Note:** For the best accuracy, always include the location of where the item is be shipped in the `contextualLocation` values of the [`X-EBAY-C-ENDUSERCTX`](/api-docs/buy/static/api-browse.html#Headers) request header.
- **quantityUsedForEstimate** (integer)
  - The number of items used when calculating the estimation information.  
  
This field will reflect the value input in the **quantity\_for\_shipping\_estimate** query parameter.
- **shippingCarrierCode** (string)
  - The name of the shipping provider, such as FedEx, or USPS.
- **shippingCost** (ConvertedAmount)
  - The final shipping cost for all the items after all discounts are applied.  
  
This container will reflect the cost for the quantity specified through the **quantity\_for\_shipping\_estimate** query parameter.  
  
**Note:** The cost does include the value-added tax (VAT) for applicable jurisdictions when requested from supported marketplaces. In this case, users must pass the [`X-EBAY-C-MARKETPLACE-ID`](/api-docs/static/rest-request-components.html#HTTP) request header specifying the supported marketplace (such as `EBAY_GB`) to see the VAT-inclusive cost. For more information on VAT, refer to [VAT Obligations in the EU](https://www.ebay.co.uk/help/listings/default/vat-obligations-eu?id=4650&st=12&pos=1&query=Your%20VAT%20obligations%20in%20the%20EU&intent=VAT).
- **shippingCostType** (string)
  - Indicates the class of the shipping cost.  
  
**Valid Values:** FIXED or CALCULATED  
  
Code so that your app gracefully handles any future changes to this list.
- **shippingServiceCode** (string)
  - The type of shipping service. For example, USPS First Class.
- **shipToLocationUsedForEstimate** (ShipToLocation)
  - The container that returns the country and postal code of where the item is to be shipped. These values come from the `contextualLocation` values in the [`X-EBAY-C-ENDUSERCTX`](/api-docs/buy/static/api-browse.html#Headers) request header. If the header is not submitted, marketplace is used.
- **trademarkSymbol** (string)
  - Any trademark symbol, such as ™ or ®, that needs to be shown in superscript next to the shipping service name.
- **type** (string)
  - The type of a shipping option, such as EXPEDITED, ONE\_DAY, STANDARD, ECONOMY, PICKUP, etc.

### TaxJurisdiction
**Description:** The type that defines the fields for the tax jurisdiction details.
**Type:** object

**Properties:**
- **region** (Region)
  - The region of the tax jurisdiction.
- **taxJurisdictionId** (string)
  - The identifier of the tax jurisdiction.

### Taxes
**Description:** The type that defines the tax fields.
**Type:** object

**Properties:**
- **ebayCollectAndRemitTax** (boolean)
  - This field is only returned if `true`, and indicates that eBay will collect tax (sales tax, Goods and Services tax, or VAT) for at least one line item in the order, and remit the tax to the taxing authority of the buyer's residence.
- **includedInPrice** (boolean)
  - This indicates if tax was applied for the cost of the item.
- **shippingAndHandlingTaxed** (boolean)
  - This indicates if tax is applied for the shipping cost.
- **taxJurisdiction** (TaxJurisdiction)
  - The container that returns the tax jurisdiction.
- **taxPercentage** (string)
  - The percentage of tax.
- **taxType** (TaxTypeEnum)
  - This field indicates the type of tax that may be collected for the item.

### TimeDuration
**Description:** The type that defines the fields for a period of time in the time-measurement units supplied.
**Type:** object

**Properties:**
- **unit** (TimeDurationUnitEnum)
  - An enumeration value that indicates the units of the time span (e.g., `HOURS`). The enumeration value in this field defines the period of time being used to measure the duration.  
  
Refer to [TimeDurationUnitEnum](/api-docs/buy/browse/types/ba:TimeDurationUnitEnum) for the list of supported values.
- **value** (integer)
  - Retrieves the duration of the time span (no units). The value in this field indicates the number of years, months, days, hours, or minutes in the defined period.

### TimeDurationUnitEnum
**Description:** An enumerated type that defines the values that represent the period of time being used. | - **YEAR**: Indicates the time duration is based on the number of years. - **MONTH**: Indicates the time duration is based on the number of months. - **DAY**: Indicates the time duration is based on the number of days. - **HOUR**: Indicates the time duration is based on the number of hours. - **CALENDAR_DAY**: Indicates the time duration is based on the calendar, meaning Sunday through Saturday and does not exclude holidays. - **BUSINESS_DAY**: Indicates the time duration is based on the number of business days, meaning "working days". So it excludes all holidays for the location and in some locations can include Saturday. - **MINUTE**: Indicates the time duration is based on the number of minutes. - **SECOND**: Indicates the time duration is based on the number of seconds. - **MILLISECOND**: Indicates the time duration is based on the number of milliseconds.
**Type:** object

### TypedNameValue
**Description:** The type that defines the fields for the name/value pairs for item aspects.
**Type:** object

**Properties:**
- **name** (string)
  - The text representing the name of the aspect for the name/value pair, such as Color.
- **type** (ValueTypeEnum)
  - This indicates if the value being returned is a string or an array of values.  
  
**Valid Values:**

*   **STRING** - Indicates the value returned is a string.
*   **STRING\_ARRAY** - Indicates the value returned is an array of strings.

Code so that your app gracefully handles any future changes to this list.
- **value** (string)
  - The value of the aspect for the name/value pair, such as Red.

### ValueTypeEnum
**Description:** An enumerated type for the values that represent the data type of value being returned for the item aspects. | - **STRING**: Indicates the value returned is a string. - **STRING_ARRAY**: Indicates the value returned is an array of strings.
**Type:** object

### VatDetail
**Description:** The type the defines the fields for the VAT (value add tax) information.
**Type:** object

**Properties:**
- **issuingCountry** (CountryCodeEnum)
  - The two-letter [ISO 3166](<https://www.iso.org/iso-3166-country-codes.html >) standard of the country issuing the seller's VAT (value added tax) ID. VAT is a tax added by some European countries.
- **vatId** (string)
  - The seller's VAT (value added tax) ID. VAT is a tax added by some European countries.

### CouponDiscountTypeEnum
**Description:** This enumeration type contains the list of coded coupon discount types. Currently, the only supported discount type is an item price discount. | - **ITEM_PRICE**: ITEM_PRICE
**Type:** object

### TaxTypeEnum
**Description:** An enumerated type for the values that represent the type of tax.  
  
Code so that your app gracefully handles any future changes to this list. | - **STATE_SALES_TAX**: STATE_SALES_TAX - **VAT**: VAT - **PROVINCE_SALES_TAX**: PROVINCE_SALES_TAX - **REGION**: REGION - **GST**: GST
**Type:** object

### CoreItem
**Description:** This type defines the array of containers with the details for all of the items returned.
**Type:** object

**Properties:**
- **additionalImages** (array)
  - An array of containers with the URLs for the images that are in addition to the primary image. The primary image is returned in the **image.imageUrl** field.
- **adultOnly** (boolean)
  - This indicates if the item is for adults only. For more information about adult-only items on eBay, see [Adult items policy](<https://pages.ebay.com/help/policies/adult-only.html >) for sellers and [Adult-Only items on eBay](<https://www.ebay.com/help/terms-conditions/default/searching-adult-items?id=4661 >) for buyers.
- **ageGroup** (string)
  - (Primary Item Aspect) The age group for which the product is recommended. For example, newborn, infant, toddler, kids, adult, etc. All the item aspects, including this aspect, are returned in the **localizedAspects** container.
- **authenticityGuarantee** (AuthenticityGuaranteeProgram)
  - A container for information about whether an item is qualified for the Authenticity Guarantee program.  
  
Under the Authenticity Guarantee program, the seller ships a purchased item to a a third-party authenticator who inspects the item and provides an authentication card for it before the item is shipped to the buyer. If the buyer returns the item, the authenticator first verifies that it is the same item in the same condition before returning it to the seller.  
  
**Note:** Refer to the [Authenticity Guarantee](<https://pages.ebay.com/authenticity-guarantee/ >) page for more information.
- **authenticityVerification** (AuthenticityVerificationProgram)
  - A container for information about whether an item is from a verified seller.
- **availableCoupons** (array)
  - A list of available coupons for the item.
- **bidCount** (integer)
  - This integer value indicates the total number of bids that have been placed against an auction item. This field is returned only for auction items.
- **brand** (string)
  - (Primary Item Aspect) The name brand of the item, such as Nike, Apple, etc. All the item aspects, including this aspect, are returned in the **localizedAspects** container.
- **buyingOptions** (array)
  - A comma separated list of all the purchase options available for the item. The values returned are:

*   `FIXED_PRICE` - Indicates the buyer can purchase the item for a set price using the Buy It Now button.
*   `AUCTION` - Indicates the buyer can place a bid for the item. After the first bid is placed, this becomes a live auction item and is the only buying option for this item.
*   `BEST_OFFER` - Indicates the buyer can send the seller a price they're willing to pay for the item. The seller can accept, reject, or send a counter offer. For more information on how this works, see [Making a Best Offer](<https://www.ebay.com/help/buying/buy-now/making-best-offer?id=4019 >).
*   `CLASSIFIED_AD` - Indicates that the final sales transaction is to be completed outside of the eBay environment.

Code so that your app gracefully handles any future changes to this list.
- **categoryId** (string)
  - The ID of the leaf category for this item. A leaf category is the lowest level in that category and has no children.
- **categoryPath** (string)
  - Text that shows the category hierarchy of the item. For example: Computers/Tablets & Networking, Laptops & Netbooks, PC Laptops & Netbooks
- **color** (string)
  - (Primary Item Aspect) Text describing the color of the item. All the item aspects, including this aspect, are returned in the **localizedAspects** container.
- **charityTerms** (ItemCharityTerms)
  - This container returns any applicable charity information associated with the specified item.  
  
This container is only returned if the **fieldgroups** query parameter is set to `CHARITY_DETAILS`.
- **condition** (string)
  - A short text description for the condition of the item, such as New or Used. For a list of condition names, see [Item Condition IDs and Names](</api-docs/sell/static/metadata/condition-id-values.html >).  
  
Code so that your app gracefully handles any future changes to this list.
- **conditionDescription** (string)
  - A full text description for the condition of the item. This field elaborates on the value specified in the **condition** field and provides full details for the condition of the item.
- **conditionId** (string)
  - The identifier of the condition of the item. For example, 1000 is the identifier for NEW. For a list of condition names and IDs, see [Item Condition IDs and Names](</api-docs/sell/static/metadata/condition-id-values.html >).  
  
Code so that your app gracefully handles any future changes to this list.
- **currentBidPrice** (ConvertedAmount)
  - The container that returns the current highest bid for an auction item. The value (string) field shows the dollar value of the current highest bid, and the currency (3-digit ISO code) field denotes the currency associated with that bid value. This container will only be returned for auction items.
- **description** (string)
  - The full description of the item that was created by the seller. This can be plain text or rich content and can be very large.
- **eligibleForInlineCheckout** (boolean)
  - This field indicates if the item can be purchased using the Buy [Order API](/api-docs/buy/order/resources/methods).

*   If the value of this field is `true`, this indicates that the item can be purchased using the **Order API**.
*   If the value of this field is `false`, this indicates that the item cannot be purchased using the **Order API** and must be purchased on the eBay site.
- **enabledForGuestCheckout** (boolean)
  - This indicates if the item can be purchased using Guest Checkout in the [Order API](/api-docs/buy/order/resources/methods). You can use this flag to exclude items from your inventory that are not eligible for Guest Checkout, such as gift cards.
- **energyEfficiencyClass** (string)
  - This indicates the [European energy efficiency](<https://en.wikipedia.org/wiki/European_Union_energy_label >) rating (EEK) of the item. This field is returned only if the seller specified the energy efficiency rating.  
  
The rating is a set of energy efficiency classes from A to G, where 'A' is the most energy efficient and 'G' is the least efficient. This rating helps buyers choose between various models.  
  
When the manufacturer's specifications for this item are available, the link to this information is returned in the **productFicheWebUrl** field.
- **epid** (string)
  - An EPID is the eBay product identifier of a product from the eBay product catalog. This indicates the product in which the item belongs.
- **estimatedAvailabilities** (array)
  - The estimated number of this item that are available for purchase. Because the quantity of an item can change several times within a second, it is impossible to return the exact quantity. So instead of returning quantity, the estimated availability of the item is returned.
- **gender** (string)
  - (Primary Item Aspect) The gender for the item. This is used for items that could vary by gender, such as clothing. For example: male, female, or unisex. All the item aspects, including this aspect, are returned in the **localizedAspects** container.
- **gtin** (string)
  - The unique Global Trade Item number of the item as defined by [https://www.gtin.info](<https://www.gtin.info >). This can be a UPC (Universal Product Code), EAN (European Article Number), or an ISBN (International Standard Book Number) value.
- **image** (Image)
  - The URL of the primary image of the item. The other images of the item are returned in the **additionalImages** container.
- **immediatePay** (boolean)
  - A value of `true` indicates that the seller requires immediate payment from the buyer when purchasing an item.  
  
**Note:** It is possible for this field to be set to `true`, but not apply in some scenarios. For example, immediate payment is not applicable for auction listings that have a winning bidder, for buyers' purchases that involve the Best Offer feature, or for offline transactions.
- **inferredEpid** (string)
  - The ePID (eBay Product ID of a product from the eBay product catalog) for the item, which has been programmatically determined by eBay using the item's title, aspects, and other data.  
  
If the seller provided an ePID for the item, the seller's value is returned in the **epid** field.  
  
**Note:** This field is returned only for authorized Partners.
- **itemAffiliateWebUrl** (string)
  - The URL to the View Item page of the item which includes the affiliate tracking ID.  
  
**Note:** In order to receive commissions on sales, eBay Partner Network affiliates must use this URL to forward buyers to the listing on the eBay marketplace.  
The **itemAffiliateWebUrl** is only returned if:

*   The marketplace through which the item is being viewed is part of the eBay Partner Network. Currently Singapore (`EBAY_SG`) is **not** supported.  
      
    For additional information, refer to [eBay Partner Network](<https://partnerhelp.ebay.com/helpcenter/s/article/countries-available-as-a-program-in-EPN?language=en_US >).
*   The seller enables affiliate tracking for the item by including the `[X-EBAY-C-ENDUSERCTX](/api-docs/buy/static/api-browse.html#Headers)` request header in the method.
- **itemCreationDate** (string)
  - A timestamp that indicates the date and time an item listing was created.  
  
This value is returned in UTC format (yyyy-MM-ddThh:mm:ss.sssZ), which can be converted into the local time of the buyer.
- **itemEndDate** (string)
  - A timestamp that indicates the date and time an auction listing will end.  
  
If a fixed-price listing has ended, this field indicates the date and time the listing ended.  
  
This value is returned in UTC format (`yyyy-MM-ddThh:mm:ss.sssZ`), which can be converted into the local time of the buyer.
- **itemId** (string)
  - The unique RESTful identifier of the item.
- **itemLocation** (Address)
  - The physical location of the item.
- **itemWebUrl** (string)
  - The URL of the View Item page of the item. This enables you to include a "Report Item on eBay" link that takes the buyer to the View Item page on eBay. From there they can report any issues regarding this item to eBay.
- **legacyItemId** (string)
  - The unique identifier of the eBay listing that contains the item. This is the traditional/legacy ID that is often seen in the URL of the listing View Item page.
- **localizedAspects** (array)
  - An array of containers that show the complete list of the aspect name/value pairs that describe the variation of the item.
- **lotSize** (integer)
  - The number of items in a lot. In other words, a lot size is the number of items that are being sold together.  
  
A lot is a set of two or more items included in a single listing that must be purchased together in a single order line item. All the items in the lot are the same but there can be multiple items in a single lot, such as the package of batteries shown in the example below.  
  

Item

Lot Definition

Lot Size

A package of 24 AA batteries

A box of 10 packages

10

A P235/75-15 Goodyear tire

4 tires

4

Fashion Jewelry Rings

Package of 100 assorted rings

100

  
  
**Note:** Lots are not supported in all categories.
- **marketingPrice** (MarketingPrice)
  - The original price and the discount amount and percentage.
- **material** (string)
  - (Primary Item Aspect) Text describing what the item is made of. For example, silk. All the item aspects, including this aspect, are returned in the **localizedAspects** container.
- **minimumPriceToBid** (ConvertedAmount)
  - The minimum price of the next bid, which means to place a bid it must be equal to or greater than this amount. If the auction hasn't received any bids, the minimum bid price is the same as the starting bid. Otherwise, the minimum bid price is equal to the current bid plus the bid increment. For details about bid increments, see [Automatic bidding](<https://www.ebay.com/help/buying/bidding/automatic-bidding?id=4014 >).
- **mpn** (string)
  - The manufacturer's part number, which is a unique number that identifies a specific product. To identify the product, this is always used along with brand.
- **pattern** (string)
  - (Primary Item Aspect) Text describing the pattern used on the item. For example, paisley. All the item aspects, including this aspect, are returned in the **localizedAspects** container.
- **paymentMethods** (array)
  - The payment methods for the item, including the payment method types, brands, and instructions for the buyer.
- **price** (ConvertedAmount)
  - The cost of just the item. This amount does not include any adjustments such as discounts or shipping costs.  
  
**Note:** The price does include the value-added tax (VAT) for applicable jurisdictions when requested from supported marketplaces. In this case, users must pass the [`X-EBAY-C-MARKETPLACE-ID`](/api-docs/static/rest-request-components.html#HTTP) request header specifying the supported marketplace (such as `EBAY_GB`) to see the VAT-inclusive pricing. For more information on VAT, refer to [VAT Obligations in the EU](https://www.ebay.co.uk/help/listings/default/vat-obligations-eu?id=4650&st=12&pos=1&query=Your%20VAT%20obligations%20in%20the%20EU&intent=VAT).
- **priceDisplayCondition** (PriceDisplayConditionEnum)
  - Indicates when in the buying flow the item's price can appear for minimum advertised price (MAP) items, which is the lowest price a retailer can advertise/show for this item.
- **primaryItemGroup** (ItemGroupSummary)
  - The container that returns details of a primary item group (parent ID of an item group). An item group is an item that has various aspect differences, such as color, size, storage capacity, etc.  
  
When an item group is created, one of the item variations, such as the red shirt size L, is chosen as the "parent". All the other items in the group are the children, such as the blue shirt size L, red shirt size M, etc.  
  
**Note:** This container is returned if the **item\_id** in the request is for an item group (items with variations, such as color and size). This container is also returned on a request for **item\_group\_ids**.
- **primaryProductReviewRating** (ReviewRating)
  - The container that returns the product rating details, such as review count, rating histogram, and average rating.
- **priorityListing** (boolean)
  - This field is returned as `true` if the listing is part of a Promoted Listing campaign. Promoted Listings are available to Above Standard and Top Rated sellers with recent sales activity.  
  
For more information, see [Promoted Listings](<https://pages.ebay.com/seller-center/listing-and-marketing/promoted-listings.html >).
- **product** (Product)
  - The container that returns the product information of the item.
- **productFicheWebUrl** (string)
  - The URL of a page containing the manufacturer's specification of this item, which helps buyers make a purchasing decision. This information is available only for items that include the European energy efficiency rating (EEK) but is not available for _all_ items with an EEK rating and is returned only if this information is available. The EEK rating of the item is returned in the **energyEfficiencyClass** field.
- **qualifiedPrograms** (array)
  - An array of the qualified programs available for the item, such as `EBAY_PLUS`, `AUTHENTICITY_GUARANTEE`, and `AUTHENTICITY_VERIFICATION`.  
  
eBay Plus is a premium account option for buyers, which provides benefits such as fast, free domestic shipping and free returns on selected items. Sellers must commit to next-day delivery of those items.The eBay [Authenticity Guarantee](<https://pages.ebay.com/authenticity-guarantee/ >) program enables third-party authenticators to perform authentication verification inspections on items such as watches and sneakers.  
  
**Note:** eBay Plus was recently deprecated on the eBay Germany marketplace, and this feature is now only available on eBay Australia marketplace.
- **quantityLimitPerBuyer** (integer)
  - The maximum number for a specific item that one buyer can purchase.
- **reservePriceMet** (boolean)
  - This indicates if the reserve price of the item has been met. A reserve price is set by the seller and is the minimum amount the seller is willing to sell the item for.

If the highest bid is not equal to or higher than the reserve price when the auction ends, the listing ends and the item is not sold.

**Note:** This is returned only for auctions that have a reserve price.
- **returnTerms** (ItemReturnTerms)
  - The container that returns an overview of the seller's return policy.
- **seller** (SellerDetail)
  - The container that returns basic and detailed about the seller of the item, such as name, feedback score, and contact information.
- **sellerItemRevision** (string)
  - An identifier generated/incremented when a seller revises the item. There are two types of item revisions:

*   Seller changes, such as changing the title
*   eBay system changes, such as changing the quantity when an item is purchased

This ID is changed _only_ when the seller makes a change to the item. This means you cannot use this value to determine if the quantity has changed.
- **shippingOptions** (array)
  - An array of shipping options containers that have the details about cost, carrier, etc. of one shipping option.  
  
**Note:** For items with calculated shipping, this array is only returned if the **X-EBAY-C-ENDUSERCTX** header is supplied.
- **shipToLocations** (ShipToLocations)
  - The container that returns the geographic regions to be included and excluded that define where the item can be shipped.
- **shortDescription** (string)
  - This text string is derived from the item condition and the item aspects (such as size, color, capacity, model, brand, etc.).
- **size** (string)
  - (Primary Item Aspect) The size of the item. For example, '7' for a size 7 shoe. All the item aspects, including this aspect, are returned in the **localizedAspects** container.
- **sizeSystem** (string)
  - (Primary Item Aspect) The sizing system of the country. All the item aspects, including this aspect, are returned in the **localizedAspects** container.  
  
**Valid Values:**  
AU (Australia),  
BR (Brazil),  
CN (China),  
DE (Germany),  
EU (European Union),  
FR (France),  
IT (Italy),  
JP (Japan),  
MX (Mexico),  
US (USA),  
UK (United Kingdom)  
  
Code so that your app gracefully handles any future changes to this list.
- **sizeType** (string)
  - (Primary Item Aspect) Text describing a size group in which the item would be included, such as regular, petite, plus, big-and-tall or maternity. All the item aspects, including this aspect, are returned in the **localizedAspects** container.
- **subtitle** (string)
  - A subtitle is optional and allows the seller to provide more information about the product, possibly including keywords that may assist with search results.
- **taxes** (array)
  - The container for the tax information for the item.
- **title** (string)
  - The seller-created title of the item.  
  
**Maximum Length:** 80 characters
- **topRatedBuyingExperience** (boolean)
  - This indicates if the item a top-rated plus item. There are three benefits of a top-rated plus item: a minimum 30-day money-back return policy, shipping the items in 1 business day with tracking provided, and the added comfort of knowing this item is from experienced sellers with the highest buyer ratings. See the [Top Rated Plus Items](<https://pages.ebay.com/topratedplus/index.html >) and [Becoming a Top Rated Seller and qualifying for Top Rated Plus](<https://pages.ebay.com/help/sell/top-rated.html >) help topics for more information.
- **tyreLabelImageUrl** (string)
  - The URL to the image that shows the information on the tyre label.
- **uniqueBidderCount** (integer)
  - This integer value indicates the number of different eBay users who have placed one or more bids on an auction item. This field is only applicable to auction items.
- **unitPrice** (ConvertedAmount)
  - This is the price per unit for the item. Some European countries require listings for certain types of products to include the price per unit so buyers can accurately compare prices.  
  
For example:  
  
`"unitPricingMeasure": "100g",   "unitPrice": {     "value": "7.99",     "currency": "GBP"`
- **unitPricingMeasure** (string)
  - The designation, such as size, weight, volume, count, etc., that was used to specify the quantity of the item. This helps buyers compare prices.  
  
For example, the following tells the buyer that the item is 7.99 per 100 grams.  
  
`"unitPricingMeasure": "100g",   "unitPrice": {     "value": "7.99",     "currency": "GBP"`

### Items
**Description:** This type defines a list of items.
**Type:** object

**Properties:**
- **items** (array)
  - An array/list of all the items.
- **total** (integer)
  - The total number of items retrieved.
- **warnings** (array)
  - An array of warning messages. These types of errors do not prevent the method from executing but should be checked.

### CommonDescriptions
**Description:** The type that defines the fields for the `item_id` values that all use a common description. Often the item variations within an item group all have the same description. Instead of repeating this description in the item details of each item, a description that is shared by at least one other item is returned in this container. If the description is unique, it is returned in the `items.description` field.
**Type:** object

**Properties:**
- **description** (string)
  - The item description that is used by more than one of the item variations.
- **itemIds** (array)
  - A list of item ids that have this description.

### ItemGroup
**Description:** The type that defines the fields for the item details.
**Type:** object

**Properties:**
- **commonDescriptions** (array)
  - An array of containers for a description and the item IDs of all the items that have this exact description. Often the item variations within an item group all have the same description. Instead of repeating this description in the item details of each item, a description that is shared by at least one other item is returned in this container. If the description is unique, it is returned in the **items.description** field.
- **items** (array)
  - An array of containers for all the item variation details, excluding the description.
- **warnings** (array)
  - An array of warning messages. These types of errors do not prevent the method from executing but should be checked.

### AttributeNameValue
**Description:** The type the defines attribute name/value pair fields that specify a product. The type of data depends on the context. For example, if you were using this to specify a specific vehicle, the attribute names would be _Make_, _Model_, _Year_, etc.
**Type:** object

**Properties:**
- **name** (string)
  - The name of the product attribute, such as _Make_, _Model_, _Year_, etc.
- **value** (string)
  - The value for the `name` attribute, such as _BMW_, _R1200GS_, _2011_, etc.

### CompatibilityPayload
**Description:** This type defines an array of attribute name/value pairs used to define a specific product. For example: If you wanted to specify a specific car, one of the name/value pairs would be:  
  
`"name" : "Year",   "value" : "2019"`  
  
For a list of the attributes required for cars and trucks and motorcycles refer to [Check compatibility](/api-docs/buy/static/api-browse.html#Check) in the [Buying Integration Guide](/api-docs/buy/static/buying-ig-landing.html).
**Type:** object

**Properties:**
- **compatibilityProperties** (array)
  - An array of attribute name/value pairs used to define a specific product. For example: If you wanted to specify a specific car, one of the name/value pairs would be  
  
`"name" : "Year",   "value" : "2019"`  
  
For a list of the attributes required for cars and trucks and motorcycles see [Check compatibility](/api-docs/buy/static/api-browse.html#Check) in the Buy Integration Guide.

### CompatibilityResponse
**Description:** The type that defines the response fields for **checkCompatibility**.
**Type:** object

**Properties:**
- **compatibilityStatus** (CompatibilityStatusEnum)
  - An enumeration value that tells you if the item is compatible with the product.  
  
The values are:

*   **COMPATIBLE** - Indicates the item is compatible with the product specified in the request.
*   **NOT\_COMPATIBLE** - Indicates the item is not compatible with the product specified in the request. Be sure to check all the **value** fields to ensure they are correct as errors in the value can also cause this response.
*   **UNDETERMINED** - Indicates one or more attributes for the specified product are missing so compatibility cannot be determined. The response returns the attributes that are missing.

Code so that your app gracefully handles any future changes to this list.
- **warnings** (array)
  - An array of warning messages. These types of errors do not prevent the method from executing but should be checked.

### CompatibilityStatusEnum
**Description:** An enumerated type for the values that represent if an item is compatible with the specified product.  
  
Code so that your app gracefully handles any future changes to this list. | - **COMPATIBLE**: COMPATIBLE - **NOT_COMPATIBLE**: NOT_COMPATIBLE - **UNDETERMINED**: UNDETERMINED
**Type:** object

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
*Generated on 2026-10-19T15:15:35.057Z*