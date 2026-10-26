eBay Trading APIVersion 1489
[ ![eBay Developers Program logo](https://developer.ebay.com/DevZone/assets/edp-logo.svg) ](https://developer.ebay.com/)
  * [Join](https://developer.ebay.com/join)
    * [About the Developers Program](https://developer.ebay.com/join/about-the-developers-program)
    * [Benefits](https://developer.ebay.com/join/benefits)
    * [Policies](https://developer.ebay.com/join/policies)
    * [API License Agreement](https://developer.ebay.com/join/api-license-agreement)
  * [DevelopNew](https://developer.ebay.com/develop)
    * [Get Started](https://developer.ebay.com/develop/get-started)
      * [Authorization](https://developer.ebay.com/api-docs/static/authorization_guide_landing.html)
      * [Using eBay RESTful APIs](https://developer.ebay.com/api-docs/static/ebay-rest-landing.html)
      * [API Call Limits](https://developer.ebay.com/develop/get-started/api-call-limits)
      * [API Deprecations](https://developer.ebay.com/develop/get-started/api-deprecation-status)
      * [API Site Status](https://developer.ebay.com/develop/get-started/api-status)
    * [Selling Apps](https://developer.ebay.com/develop/selling-apps)
      * [Listing Management](https://developer.ebay.com/develop/selling-apps/listing-management)
      * [Selling Metadata](https://developer.ebay.com/develop/selling-apps/selling-metadata)
      * [Account Management](https://developer.ebay.com/develop/selling-apps/account-management)
      * [Order Management](https://developer.ebay.com/develop/selling-apps/order-management)
      * [Communication](https://developer.ebay.com/develop/selling-apps/communication)
      * [Marketing and Promotions](https://developer.ebay.com/develop/selling-apps/marketing-and-promotions-1)
      * [Analytics and Reporting](https://developer.ebay.com/develop/selling-apps/analytics-and-reporting)
      * [Other APIs](https://developer.ebay.com/develop/selling-apps/other-apis-1)
    * [Buying Apps](https://developer.ebay.com/develop/buying-apps)
      * [Inventory Discovery & Refresh](https://developer.ebay.com/develop/buying-apps/inventory-discovery-and-refresh)
      * [Marketing and Discounts](https://developer.ebay.com/develop/buying-apps/marketing-and-discounts)
      * [Marketplace Metadata](https://developer.ebay.com/develop/buying-apps/marketplace-metadata)
      * [Checkout/Bid](https://developer.ebay.com/develop/buying-apps/checkout-bid)
      * [Research APIs](https://developer.ebay.com/develop/buying-apps/research-apis)
      * [Other APIs](https://developer.ebay.com/develop/buying-apps/other-apis)
    * [Apps Settings & Insights](https://developer.ebay.com/develop/application-settings-and-insights)
    * [SDKs & Widgets](https://developer.ebay.com/develop/sdks-and-widgets)
    * [Tools](https://developer.ebay.com/develop/tools)
      * [ eBay Sandbox ](http://sandbox.ebay.com/)
        * [Create Test Users](https://developer.ebay.com/sandbox/register)
        * [Reset Password](https://developer.ebay.com/sandbox/reset-password)
        * [Sandbox Status](https://developer.ebay.com/support/api-status/sandbox)
      * [API Explorer](https://developer.ebay.com/my/api_test_tool)
      * [WSDL Pruner](https://developer.ebay.com/develop/tools/wsdl-pruner)
  * [Grow](https://developer.ebay.com/grow)
    * [Application Growth Check](https://developer.ebay.com/grow/application-growth-check)
    * [Affiliate Program](https://developer.ebay.com/grow/affiliate-program)
    * [Loyalty Program](https://developer.ebay.com/grow/loyalty-program)
    * [Events](https://developer.ebay.com/grow/events)
    * [Awards](https://developer.ebay.com/grow/awards)
  * [Updates](https://developer.ebay.com/updates)
    * [API updates](https://developer.ebay.com/updates/api-updates)
    * [Newsletter](https://developer.ebay.com/updates/newsletter)
    * [Blog](https://developer.ebay.com/updates/blog)
  * [Support](https://developer.ebay.com/support)
    * [API Status](https://developer.ebay.com/support/api-status)
    * [FAQs](https://developer.ebay.com/support/faq)
    * [ Developer Community Forum ](https://forums.developer.ebay.com/index.html)
    * [Knowledge Base](https://developer.ebay.com/support/knowledge-base)
    * [Developer Account Support](https://developer.ebay.com/support/developer-account-support)
    * [Developer Technical Support](https://developer.ebay.com/my/support/tickets)
  * [ ](https://developer.ebay.com/signin)
    * [Application Keysets](https://developer.ebay.com/my/keys)
    * [User Access Tokens](https://developer.ebay.com/my/auth)
    * [ Alerts and Notifications ](https://developer.ebay.com/devzone/xml/docs/reference/ebay/my/push)
    * [Application Reports](https://developer.ebay.com/devzone/xml/docs/reference/ebay/my/stats)
    * [Profile & contacts](https://developer.ebay.com/my/profile)
  * [ ](https://developer.ebay.com/search)


  * [User Guide](https://developer.ebay.com/api-docs/user-guides/static/trading-user-guide-landing.html)
  * [Making a Call](https://developer.ebay.com/api-docs/user-guides/static/make-a-call-landing.html)
  * [API Reference](https://developer.ebay.com/devzone/xml/docs/Reference/eBay/index.html)
  * [Tutorials](https://developer.ebay.com/devzone/xml/docs/HowTo/index.html)
  * [Release Notes](https://developer.ebay.com/devzone/xml/docs/ReleaseNotes.html)


# GetSellerList
Use this call to retrieve items listed by the authenticated user, including item data.
**GetSellerList** returns an array of zero or more items, depending on the user's activity and the inputs used in the call. Input fields can increase or filter the data returned. See [Browsing a Seller's Items](https://developer.ebay.com/devzone/guides/ebayfeatures/Development/Items-Retrieving.html#BrowsingaSellersItems) for a detailed description of retrieving items using **GetSellerList**.
**Short-duration call rate limit:** To protect eBay's infrastructure and servers from being overloaded and/or destabilized, the **GetSellerList** call has a short-duration call rate limit to restrict bursts of very high traffic.   
  
Per (seller) user ID, no more than **300**GetSellerList** calls can be executed within any 15-second interval**. If this call rate limit is exceeded at any time, the application making the called is blocked. Each time an application is blocked, the user/application must wait until the block is reset after 15 seconds. This short-duration call rate limit applies to all seller accounts, and sellers/developers cannot appeal or request for a higher limit.    

## Usage Details
In **all calls** , at least one date-range filter must be specified. 
You can specify a **DetailLevel** to control the response data. If you set a **DetailLevel** , you **must** set pagination values.
**GetSellerList** returns a maximum of 5,000 items per call (this is possible if you do not specify a Detail Level, and thus return the smallest set of data for each item). However, if you specify any **DetailLevel** value (and thus increase the fields returned for each item), you might need to use **Pagination** values to obtain the complete result set. If you use a **DetailLevel** , the response can contain no more than 200 items per call.
Many item details (such as item descriptions and listing enhancements) don't change often, and getting these values adds to the overhead of your calls. After you initially download the details for a set of items, subsequent requests for those items should retrieve only the item information that is likely to change. It is best to avoid using a **DetailLevel** of `ReturnAll` or a **GranularityLevel** of `Fine` with **GetSellerList**. Or consider using **GetSellerEvents** instead of **GetSellerList**.
If you need to use `ReturnAll` to retrieve all the item details, use a smaller **EntriesPerPage** value to limit the number of items returned from the call. To improve performance, specify a shorter time range with **EndTimeFrom** and **EndTimeTo**. 
You can specify either a **DetailLevel** or a **GranularityLevel** in your request, but not both. See [Specifying Detail Levels and Granularity Levels](https://developer.ebay.com/devzone/guides/ebayfeatures/Basics/Call-StandardCallData.html#SpecifyingDetailLevelsandGranularityLeve) for more information about detail levels.
Use **Pagination** to control the pages of data returned. The **Pagination.EntriesPerPage** field controls how many items are returned per call, and **Pagination.PageNumber** specifies which page of data to retrieve in the current call. The value specified for **EntriesPerPage** must be between 1 and 200.
You can use multiple date-range filters in the same call. For example, you can use **StartTimeFrom** and **StartTimeTo** if you want the response to contain listings that started between the two times. Use **EndTimeFrom** and **EndTimeTo** to return listings ending between the two times.
### Working with the Response
**GetSellerList** returns a list of the sellers items in an **ItemArray** container.
  * The response data contains **ItemType** objects, within the **ItemArray**.
  * Each **ItemType** object contains the data for a listing.
  * Store the item data needed by your application.


In the output, the **ReturnedItemCountActual** property indicates how many items were returned by the call; **Count** indicates how many items could be returned. **HasMoreItems** , if true, indicates that there are more items to be returned, requiring one or more additional calls. **PageNumber** indicates the page of data returned and **ItemsPerPage** indicates the number of items returned per call.
### Testing GetSellerList
You can test this call in the Sandbox environment after you use **AddItem** to add at least two items.
Some values are only returned if the call requestor is the seller of the item. To test the call from the perspective of another user, call **GetSellerList** with a user other than the one who listed the item.
For applications that list different types of items (such as Chinese auctions and fixed-price items), create all possible types of listings using **AddItem** , then attempt to retrieve the data with **GetSellerList**.
If applicable to the application's use cases, list test items with flat and calculated shipping rates. Then retrieve the items with **GetSellerList**.
For applications that create competitive-bid item listings (Chinese auctions), bid on the items using the Sandbox user interface before retrieving the item using **GetSellerList**. This will populate the high bidder data for items in the result set.
Test calls to **GetSellerList** with different combinations of detail level, pagination, and date-based filtering to cover all of the possible scenarios the application might have to accommodate under real world conditions.
### Related Information
See [Browse a seller's items](https://developer.ebay.com/api-docs/user-guides/static/trading-user-guide/browse-seller.html).
See also the reference documentation for this call:
  * [GetItem](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetItem.html) - The **GetItem** call returns listing data such as title, description, price information, user information, and so on, for the specified **ItemID**.


  
  
  
|  Input [Output](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Output "Details about every field that might be returned by this call") [Detail Controls](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#detailControls "Details about input fields which can restrict the amount of information returned by this call") [Samples](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Samples "Illustrations of how to use this call") [Change History](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#ChangeHistory "Details about changes to this call")  |  
| --- |  
## Input
See also [Samples](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Samples).
The box below lists _all fields that could be included_ in the call request. To learn more about an individual field or its type, click its name in the box (or scroll down to find it in the table below the box).
See also the Deprecated Objects link above. Fields presented in this color are deprecated, and fields presented in this color are (or soon will be) non-operational. 
The XML prototype does not include requester credentials. This is a documentation limitation only (see [Standard Requester Credentials for Making Calls](https://developer.ebay.com/devzone/xml/docs/reference/ebay/index.html#Limitations)). 

```
<?xml version="1.0" encoding="utf-8"?>
<GetSellerListRequest xmlns="urn:ebay:apis:eBLBaseComponents">
  <!-- Call-specific Input Fields -->
  <AdminEndedItemsOnly[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Request.AdminEndedItemsOnly)> boolean[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean) </AdminEndedItemsOnly[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Request.AdminEndedItemsOnly)>
  <CategoryID[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Request.CategoryID)> int[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#int) </CategoryID[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Request.CategoryID)>
  <EndTimeFrom[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Request.EndTimeFrom)> dateTime[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#dateTime) </EndTimeFrom[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Request.EndTimeFrom)>
  <EndTimeTo[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Request.EndTimeTo)> dateTime[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#dateTime) </EndTimeTo[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Request.EndTimeTo)>
  <GranularityLevel[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Request.GranularityLevel)> GranularityLevelCodeType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/GranularityLevelCodeType.html) </GranularityLevel[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Request.GranularityLevel)>
  <IncludeVariations[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Request.IncludeVariations)> boolean[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean) </IncludeVariations[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Request.IncludeVariations)>
  <IncludeWatchCount[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Request.IncludeWatchCount)> boolean[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean) </IncludeWatchCount[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Request.IncludeWatchCount)>
  <MotorsDealerUsers[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Request.MotorsDealerUsers)> UserIDArrayType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/UserIDArrayType.html)
    <UserID[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Request.MotorsDealerUsers.UserID)> UserIDType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/UserIDType.html) (string[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string)) </UserID[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Request.MotorsDealerUsers.UserID)>
    <!-- ... more UserID values allowed here ... -->
  </MotorsDealerUsers[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Request.MotorsDealerUsers)>
  <Pagination[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Request.Pagination)> PaginationType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/PaginationType.html)
    <EntriesPerPage[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Request.Pagination.EntriesPerPage)> int[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#int) </EntriesPerPage[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Request.Pagination.EntriesPerPage)>
    <PageNumber[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Request.Pagination.PageNumber)> int[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#int) </PageNumber[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Request.Pagination.PageNumber)>
  </Pagination[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Request.Pagination)>
  <SKUArray[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Request.SKUArray)> SKUArrayType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/SKUArrayType.html)
    <SKU[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Request.SKUArray.SKU)> SKUType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/SKUType.html) (string[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string)) </SKU[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Request.SKUArray.SKU)>
    <!-- ... more SKU values allowed here ... -->
  </SKUArray[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Request.SKUArray)>
  <Sort[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Request.Sort)> int[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#int) </Sort[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Request.Sort)>
  <StartTimeFrom[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Request.StartTimeFrom)> dateTime[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#dateTime) </StartTimeFrom[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Request.StartTimeFrom)>
  <StartTimeTo[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Request.StartTimeTo)> dateTime[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#dateTime) </StartTimeTo[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Request.StartTimeTo)>
  <!-- Standard Input Fields -->
  <DetailLevel[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Request.DetailLevel)> DetailLevelCodeType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/DetailLevelCodeType.html) </DetailLevel[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Request.DetailLevel)>
  <!-- ... more DetailLevel values allowed here ... -->
  <ErrorLanguage[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Request.ErrorLanguage)> string[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string) </ErrorLanguage[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Request.ErrorLanguage)>
  <MessageID[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Request.MessageID)> string[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string) </MessageID[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Request.MessageID)>
  <OutputSelector[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Request.OutputSelector)> string[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string) </OutputSelector[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Request.OutputSelector)>
  <!-- ... more OutputSelector values allowed here ... -->
  <Version[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Request.Version)> string[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string) </Version[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Request.Version)>
  <WarningLevel[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Request.WarningLevel)> WarningLevelCodeType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/WarningLevelCodeType.html) </WarningLevel[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Request.WarningLevel)>
</GetSellerListRequest>

```
  
| Argument  | Type  | Occurrence  | Meaning  |  
| --- | --- | --- | --- |  
|  **Call-specific Input Fields** [[Jump to standard fields]](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#stdInputFields)  |  
| --- |  
|  **AdminEndedItemsOnly**  | [boolean](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean)  | Optional  |  This boolean field can be included and set to `true` if the seller would like to retrieve any listings that were administratively ended by eBay due to a listing policy violation.  
**Default:** false.   |  
| --- | --- | --- | --- |  
|  **CategoryID**  | [int](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#int)  | Optional  |  If you specify a **CategoryID** value, the response will only contain listings in the category you specify.   |  
|  **EndTimeFrom**  | [dateTime](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#dateTime)  | Conditional  |  Specifies the earliest (oldest) date to use in a date range filter based on item end time. Specify either an end-time range or a start-time range filter in every call request. Each of the time ranges must be a value less than 120 days.   |  
|  **EndTimeTo**  | [dateTime](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#dateTime)  | Conditional  |  Specifies the latest (most recent) date to use in a date range filter based on item end time. Must be specified if **EndTimeFrom** is specified.   |  
|  **GranularityLevel**  | [GranularityLevelCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/GranularityLevelCodeType.html)  | Optional  |  This field allows the user to control the amount of data that is returned in the response. See the [Granularity Level](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) table on this page for a list of the fields that are returned for each granularity level. Either **GranularityLevel** or **DetailLevel** can be used in a **GetSellerList** call, but not both. If both are specified, **DetailLevel** is ignored. If neither are used, the response fields will be the ones shown for 'Coarse' granularity.  
**Default:** Coarse.   
  
**Applicable values** :   
  


Coarse
    (in) For each record in the response, retrieves less data than Medium. See the [Standard input data](https://developer.ebay.com/api-docs/user-guides/static/make-a-call/tapi-input-data.html#details) section of the Making a Trading API call guide for a list of the output fields that are returned when this level is specified. 

CustomCode
    (in)  

Fine
    (in) For each record in the response, retrieves more data than Medium. See the [Standard input data](https://developer.ebay.com/api-docs/user-guides/static/make-a-call/tapi-input-data.html#details) section of the Making a Trading API call guide for a list of the output fields that are returned when this level is specified. 

Medium
    (in) For each record in the response, retrieves more data than Coarse and less data than Fine. See the [Standard input data](https://developer.ebay.com/api-docs/user-guides/static/make-a-call/tapi-input-data.html#details) section of the Making a Trading API call guide for a list of the output fields that are returned when this level is specified.  |  
|  **IncludeVariations**  | [boolean](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean)  | Optional  |  If this field is included and set to `true`, the **Variations** node is returned for all multi-variation listings in the response.   
  
**Note:** If the seller has many multiple-variation listings, that seller may not want to include variations in the **GetSellerList** response. Or, a seller can include variations data, but possibly limit the response by specifying shorter date ranges with the date range filters, or by reducing the number of listings returned per results (decreasing the **Pagination.EntriesPerPage** value).   |  
|  **IncludeWatchCount**  | [boolean](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean)  | Optional  |  This field may be included and set to `true` if the seller wishes to see the number of eBay users that are watching each listing.  
**Default:** false.   |  
|  **MotorsDealerUsers**  | [UserIDArrayType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/UserIDArrayType.html)  | Optional  |  Specifies the list of Motors Dealer sellers for which a special set of metrics can be requested. Applies to eBay Motors Pro applications only.   |  
|  MotorsDealerUsers.**UserID**  | [UserIDType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/UserIDType.html) ([string](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string))  | Optional,   
[repeatable](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#repeatable): [0..*]  |  Unique eBay user ID for the user. Applies to eBay Motors Pro applications only.   
  
**Note:** Effective September 26, 2025, both usernames and public user IDs will be accepted in this field. For more information, please refer to [Data Handling Compliance](https://developer.ebay.com/api-docs/static/data-handling-update.html).   |  
|  **Pagination**  | [PaginationType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/PaginationType.html)  | Required  |  This container controls the maximum number of listings that can appear on one page of the result set, as well as the page number of the result to return.   
  
The **GetSellerList** call requires that the **EntriesPerPage** value be set. The **PageNumber** field is not required but will default to `1` if not included.   |  
|  Pagination.**EntriesPerPage**  | [int](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#int)  | Required  |  This integer value is used to specify the maximum number of entries to return in a single "page" of data. This value, along with the number of entries that match the input criteria, will determine the total pages (see **PaginationResult.TotalNumberOfPages**) in the result set.   
  
The maximum and default values are not the same for all calls. For most **Trading API** calls, the maximum value is 200 and the default value is 25 entries per page.   
 |  
|  Pagination.**PageNumber**  | [int](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#int)  | Required  |  Specifies the number of the page of data to return in the current call. Default is 1 for most calls. For some calls, the default is 0. Specify a positive value equal to or lower than the number of pages available (which you determine by examining the results of your initial request). See the documentation for the individual calls to determine the correct default value.  
 |  
|  **SKUArray**  | [SKUArrayType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/SKUArrayType.html)  | Optional  |  This container can be used to specify one or multiple SKUs, and only listings associated with these SKUs are retrieved. Note that all other request criteria are also considered when one or more SKU values are specified.   
  
**Note:** Listings with matching SKUs are returned regardless of their **Item.InventoryTrackingMethod** setting.   |  
|  SKUArray.**SKU**  | [SKUType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/SKUType.html) ([string](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string))  | Optional,   
[repeatable](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#repeatable): [0..*]  |  A SKU (stock keeping unit) is an identifier defined by a seller. Some sellers use SKUs to track complex flows of products and information on the client side. A seller can specify a SKU when listing an item with AddItem and related calls. eBay preserves the SKU on the item, enabling you to obtain it before and after an order line item is created. (SKU is recommended as an alternative to ApplicationData.)  
  
A SKU is not required to be unique. A seller can specify a particular SKU value on one item or on multiple items. Different sellers can use the same SKUs.  
  
If the SKU is unique across a seller's active listings, and if the seller listed the item by using AddFixedPriceItem or RelistFixedPriceItem, the seller can also set Item.InventoryTrackingMethod to SKU. This allows the seller to use SKU instead of ItemID as a unique identifier in subsequent calls, such as GetItem and ReviseInventoryStatus.  
**Max length:** 50.   |  
|  **Sort**  | [int](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#int)  | Optional  |  This field can be used to control the order in which returned listings are sorted (based on the listings' actual/scheduled end dates). Valid values are as follows: 
  * `1` (descending order)
  * `2` (ascending order)

  
**Default:** 2 (Ascending).   |  
|  **StartTimeFrom**  | [dateTime](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#dateTime)  | Conditional  |  Specifies the earliest (oldest) date to use in a date range filter based on item start time. Each of the time ranges must be a value less than 120 days. In all calls, at least one date-range filter must be specified (i.e., you must specify either the end time range or start time range in every request).   |  
|  **StartTimeTo**  | [dateTime](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#dateTime)  | Conditional  |  Specifies the latest (most recent) date to use in a date range filter based on item start time. Must be specified if **StartTimeFrom** is specified.   |  
|  **Standard Input Fields**  |  
| --- |  
|  **DetailLevel**  | [DetailLevelCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/DetailLevelCodeType.html)  | Optional,   
[repeatable](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#repeatable): [0..*]  |  Detail levels are instructions that define standard subsets of data to return for particular data components (e.g., each Item, Transaction, or User) within the response payload. For example, a particular detail level might cause the response to include buyer-related data in every result (e.g., for every Item), but no seller-related data.   
  
Specifying a detail level is like using a predefined attribute list in the SELECT clause of an SQL query. Use the **DetailLevel** element to specify the required detail level that the client application needs pertaining to the data components that are applicable to the request.   
  
The **DetailLevelCodeType** defines the global list of available detail levels for all request types. Most request types support certain detail levels or none at all. If you pass a detail level that exists in the schema but that isn't valid for a particular request, eBay ignores it and processes the request without it.   
  
For each request type, see the detail level tables in the Input/Output Reference to determine which detail levels are applicable and which elements are returned for each applicable detail level.   
  
Note that **DetailLevel** is required input for **GetMyMessages**.   
  
With **GetSellerList** and other calls that retrieve large data sets, please avoid using **ReturnAll** when possible. For example, if you use **GetSellerList** , use **GranularityLevel** instead, or use **GetSellerEvents**. If you do use 'ReturnAll' with **GetSellerList** , use a small **Pagination.EntriesPerPage** value and a narrow **EndTimeFrom** /**EndTimeTo** date range for better performance.   
  
**Applicable values** :   
  


ItemReturnDescription
    (in) Returns the description, plus the **ListingDesigner** node and some additional information if applicable 

ReturnAll
    (in) Returns all available data. With **GetSellerList** and other calls that retrieve large data sets, please avoid using **ReturnAll** when possible. For example, if you use **GetSellerList** , use a **GranularityLevel** or use the **GetSellerEvents** call instead. If you use **ReturnAll** with **GetSellerList** , use a small **EntriesPerPage** value and a short **EndTimeFrom** /**EndTimeTo** range for better performance.   
(Not all values in [DetailLevelCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/DetailLevelCodeType.html) apply to this field.)  
 |  
| --- | --- | --- | --- |  
|  **ErrorLanguage**  | [string](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string)  | Optional  |  Use **ErrorLanguage** to return error strings for the call in a different language from the language commonly associated with the site that the requesting user is registered with. Below are some examples from different countries.   
  
  
 | ID  | Country  |  
| --- | --- |  
| en_AU  | Australia  |  
| de_AT  | Austria  |  
| nl_BE  | Belgium (Dutch)  |  
| fr_BE  | Belgium (French)  |  
| en_CA  | Canada  |  
| fr_CA  | Canada (French)  |  
| zh_CN  | China  |  
| fr_FR  | France  |  
| de_DE  | Germany  |  
| zh_HK  | Hong Kong  |  
| en_IN  | India  |  
| en_IE  | Ireland  |  
| it_IT  | Italy  |  
| nl_NL  | Netherlands  |  
| en_SG  | Singapore  |  
| es_ES  | Spain  |  
| de_CH  | Switzerland  |  
| en_GB  | United Kingdom  |  
| en_US  |  United States  |  
 |  
|  **MessageID**  | [string](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string)  | Optional  |  Most Trading API calls support a **MessageID** element in the request and a **CorrelationID** element in the response. If you pass in a **MessageID** in a request, the same value will be returned in the **CorrelationID** field in the response. Pairing these values can help you track and confirm that a response is returned for every request and to match specific responses to specific requests. If you do not pass a **MessageID** value in the request, **CorrelationID** is not returned.   |  
|  **OutputSelector**  | [string](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string)  | Optional,   
[repeatable](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#repeatable): [0..*]  |  You can use the **OutputSelector** field to restrict the data returned by a call. This field can make the call response easier to manage, especially when a large payload is returned. If you use the **OutputSelector** field, the output data will only include the field(s) you specified in the request, as well as all of its child fields (if a field is a container) and its parent fields (if any). Note that it is possible that a field included through an **OutputSelector** field may still not be returned if it is not applicable, or if it is not found based on other criteria set up in the request payload.   
  
For example, if you are using **GetItem** and you only want to retrieve the URL of the View Item page (emitted in **ViewItemURL** field) and the item's Buy It Now price (emitted in **BuyItNowPrice** field), you would include two separate **OutputSelector** fields and set the value for each one as **ViewItemURL** and **BuyItNowPrice** as in the following example:   
  

```
 **If the following output selectors are used:**   
  
...  
 <OutputSelector>ViewItemURL</OutputSelector>  
 <OutputSelector>BuyItNowPrice</OutputSelector>   
...   
  
 **...the response might look like the following**   
  
  <Item>  
 <BuyItNowPrice currencyID="USD">0.0</BuyItNowPrice>  
 <ListingDetails>  
 <ViewItemURL>http://www.ebay.com/itm/Tag-Heuer-Mens-Watch/182879833261</ViewItemURL>  
 </ListingDetails>  
 </Item>  
```
See [OutputSelector](https://developer.ebay.com/api-docs/user-guides/static/make-a-call/tapi-input-data.html#output-sel).  |  
|  **Version**  | [string](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string)  | Conditional  |  The version number of the API code that you are programming against (e.g., 1149). The version you specify for a call has these basic effects: 
  * It indicates the version of the code lists and other data that eBay should use to process your request.
  * It indicates the schema version you are using.

You need to use a version that is greater than or equal to the lowest supported version.   
**For the SOAP API:** If you are using the SOAP API, this field is required. Specify the version of the WSDL your application is using.  
  
**For the XML API:** If you are using the XML API, this field has no effect. Instead, specify the version in the **X-EBAY-API-COMPATIBILITY-LEVEL** HTTP header. (If you specify **Version** in the body of an XML API request and it is different from the value in the HTTP header, eBay returns an informational warning that the value in the HTTP header was used instead.) See:   
[HTTP headers](https://developer.ebay.com/api-docs/user-guides/static/make-a-call/using-xml.html#headers)   
[eBay Schema Versioning Strategy](https://developer.ebay.com/devzone/xml/docs/HowTo/eBayWS/eBaySchemaVersioning.html)   
[Lowest Supported Version](https://developer.ebay.com/devzone/xml/docs/HowTo/eBayWS/eBaySchemaVersioning.html#VersionSupportSchedule)  |  
|  **WarningLevel**  | [WarningLevelCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/WarningLevelCodeType.html)  | Optional  |  Controls whether or not to return warnings when the application passes unrecognized or deprecated elements in a request.  
  
An unrecognized element is one that is not defined in any supported version of the schema. Schema element names are case-sensitive, so using **WarningLevel** can also help you remove any potential hidden bugs within your application due to incorrect case or spelling in field names before you put your application into the Production environment.  
  
**WarningLevel** only validates elements; it doesn't validate XML attributes. It also doesn't control warnings related to user-entered strings or numbers, or warnings for logical errors.  
  
We recommend that you only use this during development and debugging. Do not use this in requests performed in the Production environment.   
  
**Applicable values** :   
  


High
    (in) The **WarningLevel** value is set to `High` if the user wishes to receive warnings when the application passes unrecognized or deprecated elements in an API call request. Setting the **WarningLevel** value to `High` is not recommended in a production environment. Instead, it should only be used during the development/debugging stage. 

Low
    (in) The **WarningLevel** value is set to `Low` if the user does not wish to receive warnings when the application passes unrecognized or deprecated elements in an API call request. This is the default value if **WarningLevel** is not specified in the call request. See [Warning Level](https://ebaydts.com/eBayKBDetails?KBid=499).  |  
  
  
  
|  [Input](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Input "Details about every field that can be used in this call") Output [Detail Controls](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#detailControls "Details about input fields which can restrict the amount of information returned by this call") [Samples](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Samples "Illustrations of how to use this call") [Change History](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#ChangeHistory "Details about changes to this call")  |  
| --- |  
## Output
See also [Samples](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Samples).
The box below lists _all fields that might be returned_ in the response. To learn more about an individual field or its type, click its name in the box (or scroll down to find it in the table below the box).
See also the Deprecated Objects link above. Fields presented in this color are deprecated, and fields presented in this color are not returned (or soon will not be returned) or are not operational (or soon will be non-operational).

```
<?xml version="1.0" encoding="utf-8"?>
<GetSellerListResponse xmlns="urn:ebay:apis:eBLBaseComponents">
  <!-- Call-specific Output Fields -->
  <HasMoreItems[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.HasMoreItems)> boolean[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean) </HasMoreItems[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.HasMoreItems)>
  <ItemArray[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray)> ItemArrayType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/ItemArrayType.html)
    <Item[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item)> ItemType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/ItemType.html)
      <ApplicationData[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ApplicationData)> string[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string) </ApplicationData[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ApplicationData)>
      <AutoPay[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.AutoPay)> boolean[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean) </AutoPay[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.AutoPay)>
      <BuyerGuaranteePrice[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.BuyerGuaranteePrice) currencyID="CurrencyCodeType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html)"> AmountType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/AmountType.html) (double[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#double)) </BuyerGuaranteePrice[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.BuyerGuaranteePrice)>
      <BuyerProtection[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.BuyerProtection)> BuyerProtectionCodeType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/BuyerProtectionCodeType.html) </BuyerProtection[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.BuyerProtection)>
      <BuyerRequirementDetails[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.BuyerRequirementDetails)> BuyerRequirementDetailsType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/BuyerRequirementDetailsType.html)
        <MaximumItemRequirements[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.BuyerRequirementDetails.MaximumItemRequirements)> MaximumItemRequirementsType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/MaximumItemRequirementsType.html)
          <MaximumItemCount[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.BuyerRequirementDetails.MaximumItemRequirements.MaximumItemCount)> int[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#int) </MaximumItemCount[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.BuyerRequirementDetails.MaximumItemRequirements.MaximumItemCount)>
          <MinimumFeedbackScore[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.BuyerRequirementDetails.MaximumItemRequirements.MinimumFeedbackScore)> int[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#int) </MinimumFeedbackScore[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.BuyerRequirementDetails.MaximumItemRequirements.MinimumFeedbackScore)>
        </MaximumItemRequirements[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.BuyerRequirementDetails.MaximumItemRequirements)>
        <MaximumUnpaidItemStrikesInfo[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.BuyerRequirementDetails.MaximumUnpaidItemStrikesInfo)> MaximumUnpaidItemStrikesInfoType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/MaximumUnpaidItemStrikesInfoType.html)
          <Count[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.BuyerRequirementDetails.MaximumUnpaidItemStrikesInfo.Count)> int[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#int) </Count[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.BuyerRequirementDetails.MaximumUnpaidItemStrikesInfo.Count)>
          <Period[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.BuyerRequirementDetails.MaximumUnpaidItemStrikesInfo.Period)> PeriodCodeType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/PeriodCodeType.html) </Period[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.BuyerRequirementDetails.MaximumUnpaidItemStrikesInfo.Period)>
        </MaximumUnpaidItemStrikesInfo[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.BuyerRequirementDetails.MaximumUnpaidItemStrikesInfo)>
        <ShipToRegistrationCountry[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.BuyerRequirementDetails.ShipToRegistrationCountry)> boolean[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean) </ShipToRegistrationCountry[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.BuyerRequirementDetails.ShipToRegistrationCountry)>
        <ZeroFeedbackScore[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.BuyerRequirementDetails.ZeroFeedbackScore)> boolean[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean) </ZeroFeedbackScore[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.BuyerRequirementDetails.ZeroFeedbackScore)>
      </BuyerRequirementDetails[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.BuyerRequirementDetails)>
      <BuyItNowPrice[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.BuyItNowPrice) currencyID="CurrencyCodeType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html)"> AmountType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/AmountType.html) (double[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#double)) </BuyItNowPrice[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.BuyItNowPrice)>
      <Charity[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Charity)> CharityType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CharityType.html)
        <CharityID[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Charity.CharityID)> string[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string) </CharityID[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Charity.CharityID)>
        <CharityListing[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Charity.CharityListing)> boolean[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean) </CharityListing[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Charity.CharityListing)>
        <CharityName[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Charity.CharityName)> string[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string) </CharityName[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Charity.CharityName)>
        <DonationPercent[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Charity.DonationPercent)> float[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#float) </DonationPercent[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Charity.DonationPercent)>
        <LogoURL[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Charity.LogoURL)> string[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string) </LogoURL[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Charity.LogoURL)>
        <Mission[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Charity.Mission)> string[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string) </Mission[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Charity.Mission)>
        <Status[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Charity.Status)> CharityStatusCodeType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CharityStatusCodeType.html) </Status[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Charity.Status)>
      </Charity[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Charity)>
      <ConditionDescription[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ConditionDescription)> string[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string) </ConditionDescription[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ConditionDescription)>
      <Country[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Country)> CountryCodeType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CountryCodeType.html) </Country[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Country)>
      <CrossBorderTrade[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.CrossBorderTrade)> string[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string) </CrossBorderTrade[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.CrossBorderTrade)>
      <!-- ... more CrossBorderTrade values allowed here ... -->
      <Currency[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Currency)> CurrencyCodeType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html) </Currency[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Currency)>
      <Description[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Description)> string[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string) </Description[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Description)>
      <DisableBuyerRequirements[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.DisableBuyerRequirements)> boolean[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean) </DisableBuyerRequirements[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.DisableBuyerRequirements)>
      <DiscountPriceInfo[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.DiscountPriceInfo)> DiscountPriceInfoType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/DiscountPriceInfoType.html)
        <MadeForOutletComparisonPrice[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.DiscountPriceInfo.MadeForOutletComparisonPrice) currencyID="CurrencyCodeType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html)"> AmountType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/AmountType.html) (double[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#double)) </MadeForOutletComparisonPrice[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.DiscountPriceInfo.MadeForOutletComparisonPrice)>
        <MinimumAdvertisedPrice[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.DiscountPriceInfo.MinimumAdvertisedPrice) currencyID="CurrencyCodeType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html)"> AmountType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/AmountType.html) (double[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#double)) </MinimumAdvertisedPrice[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.DiscountPriceInfo.MinimumAdvertisedPrice)>
        <MinimumAdvertisedPriceExposure[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.DiscountPriceInfo.MinimumAdvertisedPriceExposure)> MinimumAdvertisedPriceExposureCodeType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/MinimumAdvertisedPriceExposureCodeType.html) </MinimumAdvertisedPriceExposure[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.DiscountPriceInfo.MinimumAdvertisedPriceExposure)>
        <OriginalRetailPrice[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.DiscountPriceInfo.OriginalRetailPrice) currencyID="CurrencyCodeType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html)"> AmountType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/AmountType.html) (double[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#double)) </OriginalRetailPrice[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.DiscountPriceInfo.OriginalRetailPrice)>
        <PricingTreatment[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.DiscountPriceInfo.PricingTreatment)> PricingTreatmentCodeType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/PricingTreatmentCodeType.html) </PricingTreatment[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.DiscountPriceInfo.PricingTreatment)>
        <SoldOffeBay[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.DiscountPriceInfo.SoldOffeBay)> boolean[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean) </SoldOffeBay[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.DiscountPriceInfo.SoldOffeBay)>
        <SoldOneBay[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.DiscountPriceInfo.SoldOneBay)> boolean[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean) </SoldOneBay[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.DiscountPriceInfo.SoldOneBay)>
      </DiscountPriceInfo[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.DiscountPriceInfo)>
      <ExtendedSellerContactDetails[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ExtendedSellerContactDetails)> ExtendedContactDetailsType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/ExtendedContactDetailsType.html)
        <ContactHoursDetails[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ExtendedSellerContactDetails.ContactHoursDetails)> ContactHoursDetailsType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/ContactHoursDetailsType.html)
          <Hours1AnyTime[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ExtendedSellerContactDetails.ContactHoursDetails.Hours1AnyTime)> boolean[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean) </Hours1AnyTime[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ExtendedSellerContactDetails.ContactHoursDetails.Hours1AnyTime)>
          <Hours1Days[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ExtendedSellerContactDetails.ContactHoursDetails.Hours1Days)> DaysCodeType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/DaysCodeType.html) </Hours1Days[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ExtendedSellerContactDetails.ContactHoursDetails.Hours1Days)>
          <Hours1From[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ExtendedSellerContactDetails.ContactHoursDetails.Hours1From)> time[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#time) </Hours1From[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ExtendedSellerContactDetails.ContactHoursDetails.Hours1From)>
          <Hours1To[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ExtendedSellerContactDetails.ContactHoursDetails.Hours1To)> time[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#time) </Hours1To[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ExtendedSellerContactDetails.ContactHoursDetails.Hours1To)>
          <Hours2AnyTime[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ExtendedSellerContactDetails.ContactHoursDetails.Hours2AnyTime)> boolean[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean) </Hours2AnyTime[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ExtendedSellerContactDetails.ContactHoursDetails.Hours2AnyTime)>
          <Hours2Days[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ExtendedSellerContactDetails.ContactHoursDetails.Hours2Days)> DaysCodeType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/DaysCodeType.html) </Hours2Days[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ExtendedSellerContactDetails.ContactHoursDetails.Hours2Days)>
          <Hours2From[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ExtendedSellerContactDetails.ContactHoursDetails.Hours2From)> time[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#time) </Hours2From[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ExtendedSellerContactDetails.ContactHoursDetails.Hours2From)>
          <Hours2To[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ExtendedSellerContactDetails.ContactHoursDetails.Hours2To)> time[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#time) </Hours2To[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ExtendedSellerContactDetails.ContactHoursDetails.Hours2To)>
          <TimeZoneID[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ExtendedSellerContactDetails.ContactHoursDetails.TimeZoneID)> string[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string) </TimeZoneID[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ExtendedSellerContactDetails.ContactHoursDetails.TimeZoneID)>
        </ContactHoursDetails[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ExtendedSellerContactDetails.ContactHoursDetails)>
      </ExtendedSellerContactDetails[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ExtendedSellerContactDetails)>
      <FreeAddedCategory[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.FreeAddedCategory)> CategoryType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CategoryType.html)
        <CategoryID[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.FreeAddedCategory.CategoryID)> string[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string) </CategoryID[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.FreeAddedCategory.CategoryID)>
        <CategoryName[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.FreeAddedCategory.CategoryName)> string[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string) </CategoryName[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.FreeAddedCategory.CategoryName)>
      </FreeAddedCategory[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.FreeAddedCategory)>
      <HideFromSearch[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.HideFromSearch)> boolean[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean) </HideFromSearch[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.HideFromSearch)>
      <HitCount[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.HitCount)> long[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#long) </HitCount[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.HitCount)>
      <IntegratedMerchantCreditCardEnabled[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.IntegratedMerchantCreditCardEnabled)> boolean[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean) </IntegratedMerchantCreditCardEnabled[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.IntegratedMerchantCreditCardEnabled)>
      <InventoryTrackingMethod[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.InventoryTrackingMethod)> InventoryTrackingMethodCodeType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/InventoryTrackingMethodCodeType.html) </InventoryTrackingMethod[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.InventoryTrackingMethod)>
      <IsSecureDescription[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.IsSecureDescription)> boolean[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean) </IsSecureDescription[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.IsSecureDescription)>
      <ItemID[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ItemID)> ItemIDType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/ItemIDType.html) (string[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string)) </ItemID[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ItemID)>
      <ItemPolicyViolation[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ItemPolicyViolation)> ItemPolicyViolationType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/ItemPolicyViolationType.html)
        <PolicyID[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ItemPolicyViolation.PolicyID)> long[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#long) </PolicyID[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ItemPolicyViolation.PolicyID)>
        <PolicyText[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ItemPolicyViolation.PolicyText)> string[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string) </PolicyText[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ItemPolicyViolation.PolicyText)>
      </ItemPolicyViolation[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ItemPolicyViolation)>
      <ListingDetails[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ListingDetails)> ListingDetailsType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/ListingDetailsType.html)
        <Adult[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ListingDetails.Adult)> boolean[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean) </Adult[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ListingDetails.Adult)>
        <BestOfferAutoAcceptPrice[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ListingDetails.BestOfferAutoAcceptPrice) currencyID="CurrencyCodeType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html)"> AmountType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/AmountType.html) (double[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#double)) </BestOfferAutoAcceptPrice[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ListingDetails.BestOfferAutoAcceptPrice)>
        <BindingAuction[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ListingDetails.BindingAuction)> boolean[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean) </BindingAuction[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ListingDetails.BindingAuction)>
        <CheckoutEnabled[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ListingDetails.CheckoutEnabled)> boolean[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean) </CheckoutEnabled[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ListingDetails.CheckoutEnabled)>
        <ConvertedBuyItNowPrice[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ListingDetails.ConvertedBuyItNowPrice) currencyID="CurrencyCodeType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html)"> AmountType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/AmountType.html) (double[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#double)) </ConvertedBuyItNowPrice[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ListingDetails.ConvertedBuyItNowPrice)>
        <ConvertedReservePrice[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ListingDetails.ConvertedReservePrice) currencyID="CurrencyCodeType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html)"> AmountType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/AmountType.html) (double[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#double)) </ConvertedReservePrice[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ListingDetails.ConvertedReservePrice)>
        <ConvertedStartPrice[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ListingDetails.ConvertedStartPrice) currencyID="CurrencyCodeType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html)"> AmountType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/AmountType.html) (double[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#double)) </ConvertedStartPrice[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ListingDetails.ConvertedStartPrice)>
        <EndTime[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ListingDetails.EndTime)> dateTime[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#dateTime) </EndTime[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ListingDetails.EndTime)>
        <HasPublicMessages[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ListingDetails.HasPublicMessages)> boolean[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean) </HasPublicMessages[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ListingDetails.HasPublicMessages)>
        <HasReservePrice[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ListingDetails.HasReservePrice)> boolean[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean) </HasReservePrice[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ListingDetails.HasReservePrice)>
        <HasUnansweredQuestions[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ListingDetails.HasUnansweredQuestions)> boolean[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean) </HasUnansweredQuestions[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ListingDetails.HasUnansweredQuestions)>
        <MinimumBestOfferPrice[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ListingDetails.MinimumBestOfferPrice) currencyID="CurrencyCodeType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html)"> AmountType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/AmountType.html) (double[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#double)) </MinimumBestOfferPrice[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ListingDetails.MinimumBestOfferPrice)>
        <RelistedItemID[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ListingDetails.RelistedItemID)> ItemIDType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/ItemIDType.html) (string[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string)) </RelistedItemID[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ListingDetails.RelistedItemID)>
        <StartTime[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ListingDetails.StartTime)> dateTime[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#dateTime) </StartTime[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ListingDetails.StartTime)>
        <ViewItemURL[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ListingDetails.ViewItemURL)> anyURI[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#anyURI) </ViewItemURL[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ListingDetails.ViewItemURL)>
        <ViewItemURLForNaturalSearch[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ListingDetails.ViewItemURLForNaturalSearch)> anyURI[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#anyURI) </ViewItemURLForNaturalSearch[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ListingDetails.ViewItemURLForNaturalSearch)>
      </ListingDetails[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ListingDetails)>
      <ListingDuration[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ListingDuration)> token[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#token) </ListingDuration[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ListingDuration)>
      <ListingEnhancement[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ListingEnhancement)> ListingEnhancementsCodeType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/ListingEnhancementsCodeType.html) </ListingEnhancement[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ListingEnhancement)>
      <!-- ... more ListingEnhancement values allowed here ... -->
      <ListingSubtype2[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ListingSubtype2)> ListingSubtypeCodeType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/ListingSubtypeCodeType.html) </ListingSubtype2[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ListingSubtype2)>
      <ListingType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ListingType)> ListingTypeCodeType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/ListingTypeCodeType.html) </ListingType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ListingType)>
      <Location[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Location)> string[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string) </Location[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Location)>
      <PaymentMethods[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.PaymentMethods)> BuyerPaymentMethodCodeType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/BuyerPaymentMethodCodeType.html) </PaymentMethods[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.PaymentMethods)>
      <!-- ... more PaymentMethods values allowed here ... -->
      <PickupInStoreDetails[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.PickupInStoreDetails)> PickupInStoreDetailsType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/PickupInStoreDetailsType.html)
        <EligibleForPickupDropOff[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.PickupInStoreDetails.EligibleForPickupDropOff)> boolean[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean) </EligibleForPickupDropOff[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.PickupInStoreDetails.EligibleForPickupDropOff)>
        <EligibleForPickupInStore[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.PickupInStoreDetails.EligibleForPickupInStore)> boolean[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean) </EligibleForPickupInStore[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.PickupInStoreDetails.EligibleForPickupInStore)>
      </PickupInStoreDetails[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.PickupInStoreDetails)>
      <PictureDetails[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.PictureDetails)> PictureDetailsType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/PictureDetailsType.html)
        <GalleryType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.PictureDetails.GalleryType)> GalleryTypeCodeType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/GalleryTypeCodeType.html) </GalleryType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.PictureDetails.GalleryType)>
      </PictureDetails[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.PictureDetails)>
      <PrimaryCategory[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.PrimaryCategory)> CategoryType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CategoryType.html)
        <CategoryID[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.PrimaryCategory.CategoryID)> string[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string) </CategoryID[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.PrimaryCategory.CategoryID)>
        <CategoryName[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.PrimaryCategory.CategoryName)> string[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string) </CategoryName[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.PrimaryCategory.CategoryName)>
      </PrimaryCategory[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.PrimaryCategory)>
      <PrivateListing[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.PrivateListing)> boolean[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean) </PrivateListing[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.PrivateListing)>
      <ProxyItem[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ProxyItem)> boolean[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean) </ProxyItem[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ProxyItem)>
      <Quantity[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Quantity)> int[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#int) </Quantity[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Quantity)>
      <QuantityAvailableHint[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.QuantityAvailableHint)> QuantityAvailableHintCodeType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/QuantityAvailableHintCodeType.html) </QuantityAvailableHint[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.QuantityAvailableHint)>
      <QuantityThreshold[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.QuantityThreshold)> int[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#int) </QuantityThreshold[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.QuantityThreshold)>
      <ReasonHideFromSearch[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ReasonHideFromSearch)> ReasonHideFromSearchCodeType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/ReasonHideFromSearchCodeType.html) </ReasonHideFromSearch[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ReasonHideFromSearch)>
      <ReservePrice[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ReservePrice) currencyID="CurrencyCodeType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html)"> AmountType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/AmountType.html) (double[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#double)) </ReservePrice[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ReservePrice)>
      <ReturnPolicy[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ReturnPolicy)> ReturnPolicyType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/ReturnPolicyType.html)
        <Description[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ReturnPolicy.Description)> string[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string) </Description[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ReturnPolicy.Description)>
        <InternationalRefundOption[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ReturnPolicy.InternationalRefundOption)> token[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#token) </InternationalRefundOption[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ReturnPolicy.InternationalRefundOption)>
        <InternationalReturnsAcceptedOption[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ReturnPolicy.InternationalReturnsAcceptedOption)> token[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#token) </InternationalReturnsAcceptedOption[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ReturnPolicy.InternationalReturnsAcceptedOption)>
        <InternationalReturnsWithinOption[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ReturnPolicy.InternationalReturnsWithinOption)> token[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#token) </InternationalReturnsWithinOption[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ReturnPolicy.InternationalReturnsWithinOption)>
        <InternationalShippingCostPaidByOption[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ReturnPolicy.InternationalShippingCostPaidByOption)> token[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#token) </InternationalShippingCostPaidByOption[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ReturnPolicy.InternationalShippingCostPaidByOption)>
        <Refund[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ReturnPolicy.Refund)> string[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string) </Refund[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ReturnPolicy.Refund)>
        <RefundOption[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ReturnPolicy.RefundOption)> token[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#token) </RefundOption[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ReturnPolicy.RefundOption)>
        <ReturnsAccepted[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ReturnPolicy.ReturnsAccepted)> string[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string) </ReturnsAccepted[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ReturnPolicy.ReturnsAccepted)>
        <ReturnsAcceptedOption[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ReturnPolicy.ReturnsAcceptedOption)> token[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#token) </ReturnsAcceptedOption[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ReturnPolicy.ReturnsAcceptedOption)>
        <ReturnsWithin[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ReturnPolicy.ReturnsWithin)> string[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string) </ReturnsWithin[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ReturnPolicy.ReturnsWithin)>
        <ReturnsWithinOption[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ReturnPolicy.ReturnsWithinOption)> token[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#token) </ReturnsWithinOption[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ReturnPolicy.ReturnsWithinOption)>
        <ShippingCostPaidBy[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ReturnPolicy.ShippingCostPaidBy)> string[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string) </ShippingCostPaidBy[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ReturnPolicy.ShippingCostPaidBy)>
        <ShippingCostPaidByOption[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ReturnPolicy.ShippingCostPaidByOption)> token[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#token) </ShippingCostPaidByOption[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ReturnPolicy.ShippingCostPaidByOption)>
      </ReturnPolicy[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ReturnPolicy)>
      <ReviseStatus[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ReviseStatus)> ReviseStatusType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/ReviseStatusType.html)
        <ItemRevised[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ReviseStatus.ItemRevised)> boolean[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean) </ItemRevised[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ReviseStatus.ItemRevised)>
      </ReviseStatus[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ReviseStatus)>
      <SecondaryCategory[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SecondaryCategory)> CategoryType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CategoryType.html)
        <CategoryID[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SecondaryCategory.CategoryID)> string[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string) </CategoryID[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SecondaryCategory.CategoryID)>
        <CategoryName[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SecondaryCategory.CategoryName)> string[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string) </CategoryName[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SecondaryCategory.CategoryName)>
      </SecondaryCategory[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SecondaryCategory)>
      <SellerContactDetails[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellerContactDetails)> AddressType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/AddressType.html) </SellerContactDetails[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellerContactDetails)>
      <SellerProfiles[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellerProfiles)> SellerProfilesType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/SellerProfilesType.html)
        <SellerPaymentProfile[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellerProfiles.SellerPaymentProfile)> SellerPaymentProfileType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/SellerPaymentProfileType.html)
          <PaymentProfileID[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellerProfiles.SellerPaymentProfile.PaymentProfileID)> long[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#long) </PaymentProfileID[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellerProfiles.SellerPaymentProfile.PaymentProfileID)>
          <PaymentProfileName[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellerProfiles.SellerPaymentProfile.PaymentProfileName)> string[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string) </PaymentProfileName[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellerProfiles.SellerPaymentProfile.PaymentProfileName)>
        </SellerPaymentProfile[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellerProfiles.SellerPaymentProfile)>
        <SellerReturnProfile[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellerProfiles.SellerReturnProfile)> SellerReturnProfileType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/SellerReturnProfileType.html)
          <ReturnProfileID[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellerProfiles.SellerReturnProfile.ReturnProfileID)> long[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#long) </ReturnProfileID[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellerProfiles.SellerReturnProfile.ReturnProfileID)>
          <ReturnProfileName[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellerProfiles.SellerReturnProfile.ReturnProfileName)> string[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string) </ReturnProfileName[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellerProfiles.SellerReturnProfile.ReturnProfileName)>
        </SellerReturnProfile[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellerProfiles.SellerReturnProfile)>
        <SellerShippingProfile[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellerProfiles.SellerShippingProfile)> SellerShippingProfileType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/SellerShippingProfileType.html)
          <ShippingProfileID[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellerProfiles.SellerShippingProfile.ShippingProfileID)> long[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#long) </ShippingProfileID[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellerProfiles.SellerShippingProfile.ShippingProfileID)>
          <ShippingProfileName[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellerProfiles.SellerShippingProfile.ShippingProfileName)> string[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string) </ShippingProfileName[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellerProfiles.SellerShippingProfile.ShippingProfileName)>
        </SellerShippingProfile[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellerProfiles.SellerShippingProfile)>
      </SellerProfiles[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellerProfiles)>
      <SellingStatus[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus)> SellingStatusType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/SellingStatusType.html)
        <AdminEnded[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.AdminEnded)> boolean[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean) </AdminEnded[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.AdminEnded)>
        <BidCount[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.BidCount)> int[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#int) </BidCount[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.BidCount)>
        <BidIncrement[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.BidIncrement) currencyID="CurrencyCodeType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html)"> AmountType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/AmountType.html) (double[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#double)) </BidIncrement[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.BidIncrement)>
        <ConvertedCurrentPrice[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.ConvertedCurrentPrice) currencyID="CurrencyCodeType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html)"> AmountType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/AmountType.html) (double[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#double)) </ConvertedCurrentPrice[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.ConvertedCurrentPrice)>
        <CurrentPrice[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.CurrentPrice) currencyID="CurrencyCodeType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html)"> AmountType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/AmountType.html) (double[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#double)) </CurrentPrice[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.CurrentPrice)>
        <HighBidder[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.HighBidder)> UserType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/UserType.html)
          <AboutMePage[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.HighBidder.AboutMePage)> boolean[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean) </AboutMePage[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.HighBidder.AboutMePage)>
          <BuyerInfo[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.HighBidder.BuyerInfo)> BuyerType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/BuyerType.html)
            <ShippingAddress[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.HighBidder.BuyerInfo.ShippingAddress)> AddressType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/AddressType.html)
              <Country[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.HighBidder.BuyerInfo.ShippingAddress.Country)> CountryCodeType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CountryCodeType.html) </Country[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.HighBidder.BuyerInfo.ShippingAddress.Country)>
              <PostalCode[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.HighBidder.BuyerInfo.ShippingAddress.PostalCode)> string[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string) </PostalCode[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.HighBidder.BuyerInfo.ShippingAddress.PostalCode)>
            </ShippingAddress[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.HighBidder.BuyerInfo.ShippingAddress)>
          </BuyerInfo[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.HighBidder.BuyerInfo)>
          <eBayGoodStanding[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.HighBidder.eBayGoodStanding)> boolean[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean) </eBayGoodStanding[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.HighBidder.eBayGoodStanding)>
          <EIASToken[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.HighBidder.EIASToken)> string[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string) </EIASToken[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.HighBidder.EIASToken)>
          <Email[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.HighBidder.Email)> string[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string) </Email[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.HighBidder.Email)>
          <FeedbackPrivate[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.HighBidder.FeedbackPrivate)> boolean[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean) </FeedbackPrivate[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.HighBidder.FeedbackPrivate)>
          <FeedbackRatingStar[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.HighBidder.FeedbackRatingStar)> FeedbackRatingStarCodeType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/FeedbackRatingStarCodeType.html) </FeedbackRatingStar[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.HighBidder.FeedbackRatingStar)>
          <FeedbackScore[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.HighBidder.FeedbackScore)> int[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#int) </FeedbackScore[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.HighBidder.FeedbackScore)>
          <IDVerified[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.HighBidder.IDVerified)> boolean[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean) </IDVerified[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.HighBidder.IDVerified)>
          <NewUser[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.HighBidder.NewUser)> boolean[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean) </NewUser[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.HighBidder.NewUser)>
          <RegistrationDate[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.HighBidder.RegistrationDate)> dateTime[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#dateTime) </RegistrationDate[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.HighBidder.RegistrationDate)>
          <Site[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.HighBidder.Site)> SiteCodeType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/SiteCodeType.html) </Site[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.HighBidder.Site)>
          <Status[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.HighBidder.Status)> UserStatusCodeType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/UserStatusCodeType.html) </Status[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.HighBidder.Status)>
          <UserAnonymized[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.HighBidder.UserAnonymized)> boolean[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean) </UserAnonymized[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.HighBidder.UserAnonymized)>
          <UserID[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.HighBidder.UserID)> UserIDType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/UserIDType.html) (string[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string)) </UserID[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.HighBidder.UserID)>
          <UserIDChanged[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.HighBidder.UserIDChanged)> boolean[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean) </UserIDChanged[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.HighBidder.UserIDChanged)>
          <UserIDLastChanged[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.HighBidder.UserIDLastChanged)> dateTime[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#dateTime) </UserIDLastChanged[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.HighBidder.UserIDLastChanged)>
          <VATStatus[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.HighBidder.VATStatus)> VATStatusCodeType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/VATStatusCodeType.html) </VATStatus[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.HighBidder.VATStatus)>
        </HighBidder[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.HighBidder)>
        <LeadCount[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.LeadCount)> int[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#int) </LeadCount[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.LeadCount)>
        <ListingStatus[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.ListingStatus)> ListingStatusCodeType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/ListingStatusCodeType.html) </ListingStatus[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.ListingStatus)>
        <MinimumToBid[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.MinimumToBid) currencyID="CurrencyCodeType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html)"> AmountType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/AmountType.html) (double[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#double)) </MinimumToBid[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.MinimumToBid)>
        <PromotionalSaleDetails[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.PromotionalSaleDetails)> PromotionalSaleDetailsType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/PromotionalSaleDetailsType.html)
          <EndTime[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.PromotionalSaleDetails.EndTime)> dateTime[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#dateTime) </EndTime[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.PromotionalSaleDetails.EndTime)>
          <OriginalPrice[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.PromotionalSaleDetails.OriginalPrice) currencyID="CurrencyCodeType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html)"> AmountType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/AmountType.html) (double[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#double)) </OriginalPrice[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.PromotionalSaleDetails.OriginalPrice)>
          <StartTime[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.PromotionalSaleDetails.StartTime)> dateTime[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#dateTime) </StartTime[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.PromotionalSaleDetails.StartTime)>
        </PromotionalSaleDetails[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.PromotionalSaleDetails)>
        <QuantitySold[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.QuantitySold)> int[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#int) </QuantitySold[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.QuantitySold)>
        <ReserveMet[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.ReserveMet)> boolean[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean) </ReserveMet[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.ReserveMet)>
        <SecondChanceEligible[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.SecondChanceEligible)> boolean[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean) </SecondChanceEligible[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.SecondChanceEligible)>
      </SellingStatus[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus)>
      <ShippingDetails[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails)> ShippingDetailsType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/ShippingDetailsType.html)
        <CalculatedShippingRate[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.CalculatedShippingRate)> CalculatedShippingRateType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CalculatedShippingRateType.html)
          <InternationalPackagingHandlingCosts[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.CalculatedShippingRate.InternationalPackagingHandlingCosts) currencyID="CurrencyCodeType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html)"> AmountType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/AmountType.html) (double[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#double)) </InternationalPackagingHandlingCosts[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.CalculatedShippingRate.InternationalPackagingHandlingCosts)>
          <PackagingHandlingCosts[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.CalculatedShippingRate.PackagingHandlingCosts) currencyID="CurrencyCodeType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html)"> AmountType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/AmountType.html) (double[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#double)) </PackagingHandlingCosts[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.CalculatedShippingRate.PackagingHandlingCosts)>
        </CalculatedShippingRate[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.CalculatedShippingRate)>
        <ExcludeShipToLocation[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.ExcludeShipToLocation)> string[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string) </ExcludeShipToLocation[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.ExcludeShipToLocation)>
        <!-- ... more ExcludeShipToLocation values allowed here ... -->
        <GlobalShipping[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.GlobalShipping)> boolean[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean) </GlobalShipping[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.GlobalShipping)>
        <InternationalShippingServiceOption[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.InternationalShippingServiceOption)> InternationalShippingServiceOptionsType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/InternationalShippingServiceOptionsType.html)
          <ShippingService[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.InternationalShippingServiceOption.ShippingService)> token[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#token) </ShippingService[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.InternationalShippingServiceOption.ShippingService)>
          <ShippingServiceAdditionalCost[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.InternationalShippingServiceOption.ShippingServiceAdditionalCost) currencyID="CurrencyCodeType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html)"> AmountType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/AmountType.html) (double[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#double)) </ShippingServiceAdditionalCost[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.InternationalShippingServiceOption.ShippingServiceAdditionalCost)>
          <ShippingServiceCost[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.InternationalShippingServiceOption.ShippingServiceCost) currencyID="CurrencyCodeType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html)"> AmountType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/AmountType.html) (double[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#double)) </ShippingServiceCost[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.InternationalShippingServiceOption.ShippingServiceCost)>
          <ShippingServicePriority[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.InternationalShippingServiceOption.ShippingServicePriority)> int[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#int) </ShippingServicePriority[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.InternationalShippingServiceOption.ShippingServicePriority)>
          <ShipToLocation[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.InternationalShippingServiceOption.ShipToLocation)> string[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string) </ShipToLocation[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.InternationalShippingServiceOption.ShipToLocation)>
          <!-- ... more ShipToLocation values allowed here ... -->
        </InternationalShippingServiceOption[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.InternationalShippingServiceOption)>
        <!-- ... more InternationalShippingServiceOption nodes allowed here ... -->
        <PaymentEdited[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.PaymentEdited)> boolean[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean) </PaymentEdited[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.PaymentEdited)>
        <RateTableDetails[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.RateTableDetails)> RateTableDetailsType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/RateTableDetailsType.html)
          <DomesticRateTable[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.RateTableDetails.DomesticRateTable)> string[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string) </DomesticRateTable[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.RateTableDetails.DomesticRateTable)>
          <DomesticRateTableId[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.RateTableDetails.DomesticRateTableId)> string[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string) </DomesticRateTableId[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.RateTableDetails.DomesticRateTableId)>
          <InternationalRateTable[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.RateTableDetails.InternationalRateTable)> string[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string) </InternationalRateTable[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.RateTableDetails.InternationalRateTable)>
          <InternationalRateTableId[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.RateTableDetails.InternationalRateTableId)> string[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string) </InternationalRateTableId[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.RateTableDetails.InternationalRateTableId)>
        </RateTableDetails[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.RateTableDetails)>
        <SalesTax[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.SalesTax)> SalesTaxType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/SalesTaxType.html)
          <SalesTaxPercent[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.SalesTax.SalesTaxPercent)> float[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#float) </SalesTaxPercent[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.SalesTax.SalesTaxPercent)>
          <SalesTaxState[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.SalesTax.SalesTaxState)> string[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string) </SalesTaxState[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.SalesTax.SalesTaxState)>
          <ShippingIncludedInTax[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.SalesTax.ShippingIncludedInTax)> boolean[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean) </ShippingIncludedInTax[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.SalesTax.ShippingIncludedInTax)>
        </SalesTax[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.SalesTax)>
        <SellerExcludeShipToLocationsPreference[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.SellerExcludeShipToLocationsPreference)> boolean[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean) </SellerExcludeShipToLocationsPreference[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.SellerExcludeShipToLocationsPreference)>
        <ShippingServiceOptions[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.ShippingServiceOptions)> ShippingServiceOptionsType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/ShippingServiceOptionsType.html)
          <ExpeditedService[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.ShippingServiceOptions.ExpeditedService)> boolean[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean) </ExpeditedService[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.ShippingServiceOptions.ExpeditedService)>
          <ShippingService[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.ShippingServiceOptions.ShippingService)> token[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#token) </ShippingService[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.ShippingServiceOptions.ShippingService)>
          <ShippingServiceAdditionalCost[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.ShippingServiceOptions.ShippingServiceAdditionalCost) currencyID="CurrencyCodeType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html)"> AmountType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/AmountType.html) (double[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#double)) </ShippingServiceAdditionalCost[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.ShippingServiceOptions.ShippingServiceAdditionalCost)>
          <ShippingServiceCost[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.ShippingServiceOptions.ShippingServiceCost) currencyID="CurrencyCodeType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html)"> AmountType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/AmountType.html) (double[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#double)) </ShippingServiceCost[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.ShippingServiceOptions.ShippingServiceCost)>
          <ShippingServicePriority[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.ShippingServiceOptions.ShippingServicePriority)> int[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#int) </ShippingServicePriority[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.ShippingServiceOptions.ShippingServicePriority)>
          <ShippingTimeMax[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.ShippingServiceOptions.ShippingTimeMax)> int[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#int) </ShippingTimeMax[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.ShippingServiceOptions.ShippingTimeMax)>
          <ShippingTimeMin[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.ShippingServiceOptions.ShippingTimeMin)> int[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#int) </ShippingTimeMin[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.ShippingServiceOptions.ShippingTimeMin)>
        </ShippingServiceOptions[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.ShippingServiceOptions)>
        <!-- ... more ShippingServiceOptions nodes allowed here ... -->
        <TaxTable[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.TaxTable)> TaxTableType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/TaxTableType.html)
          <TaxJurisdiction[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.TaxTable.TaxJurisdiction)> TaxJurisdictionType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/TaxJurisdictionType.html)
            <JurisdictionID[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.TaxTable.TaxJurisdiction.JurisdictionID)> string[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string) </JurisdictionID[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.TaxTable.TaxJurisdiction.JurisdictionID)>
            <SalesTaxPercent[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.TaxTable.TaxJurisdiction.SalesTaxPercent)> float[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#float) </SalesTaxPercent[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.TaxTable.TaxJurisdiction.SalesTaxPercent)>
            <ShippingIncludedInTax[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.TaxTable.TaxJurisdiction.ShippingIncludedInTax)> boolean[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean) </ShippingIncludedInTax[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.TaxTable.TaxJurisdiction.ShippingIncludedInTax)>
          </TaxJurisdiction[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.TaxTable.TaxJurisdiction)>
          <!-- ... more TaxJurisdiction nodes allowed here ... -->
        </TaxTable[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.TaxTable)>
        <ThirdPartyCheckout[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.ThirdPartyCheckout)> boolean[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean) </ThirdPartyCheckout[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.ThirdPartyCheckout)>
      </ShippingDetails[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails)>
      <ShippingServiceCostOverrideList[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingServiceCostOverrideList)> ShippingServiceCostOverrideListType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/ShippingServiceCostOverrideListType.html)
        <ShippingServiceCostOverride[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingServiceCostOverrideList.ShippingServiceCostOverride)> ShippingServiceCostOverrideType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/ShippingServiceCostOverrideType.html)
          <ShippingServiceAdditionalCost[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingServiceCostOverrideList.ShippingServiceCostOverride.ShippingServiceAdditionalCost) currencyID="CurrencyCodeType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html)"> AmountType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/AmountType.html) (double[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#double)) </ShippingServiceAdditionalCost[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingServiceCostOverrideList.ShippingServiceCostOverride.ShippingServiceAdditionalCost)>
          <ShippingServiceCost[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingServiceCostOverrideList.ShippingServiceCostOverride.ShippingServiceCost) currencyID="CurrencyCodeType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html)"> AmountType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/AmountType.html) (double[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#double)) </ShippingServiceCost[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingServiceCostOverrideList.ShippingServiceCostOverride.ShippingServiceCost)>
          <ShippingServicePriority[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingServiceCostOverrideList.ShippingServiceCostOverride.ShippingServicePriority)> int[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#int) </ShippingServicePriority[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingServiceCostOverrideList.ShippingServiceCostOverride.ShippingServicePriority)>
          <ShippingServiceType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingServiceCostOverrideList.ShippingServiceCostOverride.ShippingServiceType)> ShippingServiceType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/ShippingServiceType.html) </ShippingServiceType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingServiceCostOverrideList.ShippingServiceCostOverride.ShippingServiceType)>
        </ShippingServiceCostOverride[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingServiceCostOverrideList.ShippingServiceCostOverride)>
        <!-- ... more ShippingServiceCostOverride nodes allowed here ... -->
      </ShippingServiceCostOverrideList[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingServiceCostOverrideList)>
      <ShipToLocations[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShipToLocations)> string[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string) </ShipToLocations[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShipToLocations)>
      <!-- ... more ShipToLocations values allowed here ... -->
      <Site[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Site)> SiteCodeType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/SiteCodeType.html) </Site[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Site)>
      <SKU[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SKU)> SKUType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/SKUType.html) (string[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string)) </SKU[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SKU)>
      <StartPrice[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.StartPrice) currencyID="CurrencyCodeType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html)"> AmountType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/AmountType.html) (double[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#double)) </StartPrice[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.StartPrice)>
      <Storefront[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Storefront)> StorefrontType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/StorefrontType.html)
        <StoreCategory2ID[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Storefront.StoreCategory2ID)> long[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#long) </StoreCategory2ID[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Storefront.StoreCategory2ID)>
        <StoreCategoryID[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Storefront.StoreCategoryID)> long[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#long) </StoreCategoryID[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Storefront.StoreCategoryID)>
        <StoreURL[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Storefront.StoreURL)> anyURI[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#anyURI) </StoreURL[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Storefront.StoreURL)>
      </Storefront[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Storefront)>
      <TimeLeft[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.TimeLeft)> duration[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#duration) </TimeLeft[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.TimeLeft)>
      <Title[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Title)> string[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string) </Title[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Title)>
      <TotalQuestionCount[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.TotalQuestionCount)> long[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#long) </TotalQuestionCount[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.TotalQuestionCount)>
      <Variations[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations)> VariationsType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/VariationsType.html)
        <Variation[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation)> VariationType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/VariationType.html)
          <Quantity[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.Quantity)> int[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#int) </Quantity[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.Quantity)>
          <SellingStatus[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus)> SellingStatusType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/SellingStatusType.html)
            <AdminEnded[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.AdminEnded)> boolean[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean) </AdminEnded[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.AdminEnded)>
            <BidCount[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.BidCount)> int[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#int) </BidCount[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.BidCount)>
            <BidIncrement[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.BidIncrement) currencyID="CurrencyCodeType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html)"> AmountType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/AmountType.html) (double[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#double)) </BidIncrement[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.BidIncrement)>
            <ConvertedCurrentPrice[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.ConvertedCurrentPrice) currencyID="CurrencyCodeType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html)"> AmountType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/AmountType.html) (double[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#double)) </ConvertedCurrentPrice[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.ConvertedCurrentPrice)>
            <CurrentPrice[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.CurrentPrice) currencyID="CurrencyCodeType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html)"> AmountType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/AmountType.html) (double[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#double)) </CurrentPrice[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.CurrentPrice)>
            <HighBidder[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.HighBidder)> UserType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/UserType.html)
              <AboutMePage[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.HighBidder.AboutMePage)> boolean[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean) </AboutMePage[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.HighBidder.AboutMePage)>
              <BuyerInfo[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.HighBidder.BuyerInfo)> BuyerType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/BuyerType.html)
                <ShippingAddress[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.HighBidder.BuyerInfo.ShippingAddress)> AddressType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/AddressType.html)
                  <Country[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.HighBidder.BuyerInfo.ShippingAddress.Country)> CountryCodeType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CountryCodeType.html) </Country[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.HighBidder.BuyerInfo.ShippingAddress.Country)>
                  <PostalCode[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.HighBidder.BuyerInfo.ShippingAddress.PostalCode)> string[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string) </PostalCode[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.HighBidder.BuyerInfo.ShippingAddress.PostalCode)>
                </ShippingAddress[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.HighBidder.BuyerInfo.ShippingAddress)>
              </BuyerInfo[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.HighBidder.BuyerInfo)>
              <eBayGoodStanding[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.HighBidder.eBayGoodStanding)> boolean[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean) </eBayGoodStanding[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.HighBidder.eBayGoodStanding)>
              <EIASToken[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.HighBidder.EIASToken)> string[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string) </EIASToken[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.HighBidder.EIASToken)>
              <Email[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.HighBidder.Email)> string[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string) </Email[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.HighBidder.Email)>
              <FeedbackPrivate[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.HighBidder.FeedbackPrivate)> boolean[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean) </FeedbackPrivate[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.HighBidder.FeedbackPrivate)>
              <FeedbackRatingStar[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.HighBidder.FeedbackRatingStar)> FeedbackRatingStarCodeType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/FeedbackRatingStarCodeType.html) </FeedbackRatingStar[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.HighBidder.FeedbackRatingStar)>
              <FeedbackScore[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.HighBidder.FeedbackScore)> int[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#int) </FeedbackScore[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.HighBidder.FeedbackScore)>
              <IDVerified[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.HighBidder.IDVerified)> boolean[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean) </IDVerified[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.HighBidder.IDVerified)>
              <NewUser[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.HighBidder.NewUser)> boolean[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean) </NewUser[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.HighBidder.NewUser)>
              <RegistrationDate[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.HighBidder.RegistrationDate)> dateTime[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#dateTime) </RegistrationDate[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.HighBidder.RegistrationDate)>
              <Site[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.HighBidder.Site)> SiteCodeType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/SiteCodeType.html) </Site[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.HighBidder.Site)>
              <Status[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.HighBidder.Status)> UserStatusCodeType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/UserStatusCodeType.html) </Status[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.HighBidder.Status)>
              <UserAnonymized[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.HighBidder.UserAnonymized)> boolean[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean) </UserAnonymized[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.HighBidder.UserAnonymized)>
              <UserID[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.HighBidder.UserID)> UserIDType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/UserIDType.html) (string[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string)) </UserID[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.HighBidder.UserID)>
              <UserIDChanged[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.HighBidder.UserIDChanged)> boolean[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean) </UserIDChanged[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.HighBidder.UserIDChanged)>
              <UserIDLastChanged[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.HighBidder.UserIDLastChanged)> dateTime[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#dateTime) </UserIDLastChanged[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.HighBidder.UserIDLastChanged)>
              <VATStatus[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.HighBidder.VATStatus)> VATStatusCodeType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/VATStatusCodeType.html) </VATStatus[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.HighBidder.VATStatus)>
            </HighBidder[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.HighBidder)>
            <LeadCount[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.LeadCount)> int[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#int) </LeadCount[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.LeadCount)>
            <ListingStatus[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.ListingStatus)> ListingStatusCodeType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/ListingStatusCodeType.html) </ListingStatus[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.ListingStatus)>
            <MinimumToBid[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.MinimumToBid) currencyID="CurrencyCodeType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html)"> AmountType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/AmountType.html) (double[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#double)) </MinimumToBid[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.MinimumToBid)>
            <PromotionalSaleDetails[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.PromotionalSaleDetails)> PromotionalSaleDetailsType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/PromotionalSaleDetailsType.html)
              <EndTime[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.PromotionalSaleDetails.EndTime)> dateTime[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#dateTime) </EndTime[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.PromotionalSaleDetails.EndTime)>
              <OriginalPrice[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.PromotionalSaleDetails.OriginalPrice) currencyID="CurrencyCodeType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html)"> AmountType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/AmountType.html) (double[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#double)) </OriginalPrice[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.PromotionalSaleDetails.OriginalPrice)>
              <StartTime[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.PromotionalSaleDetails.StartTime)> dateTime[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#dateTime) </StartTime[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.PromotionalSaleDetails.StartTime)>
            </PromotionalSaleDetails[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.PromotionalSaleDetails)>
            <QuantitySold[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.QuantitySold)> int[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#int) </QuantitySold[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.QuantitySold)>
            <ReserveMet[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.ReserveMet)> boolean[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean) </ReserveMet[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.ReserveMet)>
            <SecondChanceEligible[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.SecondChanceEligible)> boolean[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean) </SecondChanceEligible[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.SecondChanceEligible)>
          </SellingStatus[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus)>
          <SKU[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SKU)> SKUType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/SKUType.html) (string[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string)) </SKU[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SKU)>
          <StartPrice[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.StartPrice) currencyID="CurrencyCodeType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html)"> AmountType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/AmountType.html) (double[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#double)) </StartPrice[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.StartPrice)>
          <VariationProductListingDetails[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.VariationProductListingDetails)> VariationProductListingDetailsType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/VariationProductListingDetailsType.html)
            <EAN[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.VariationProductListingDetails.EAN)> string[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string) </EAN[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.VariationProductListingDetails.EAN)>
            <ISBN[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.VariationProductListingDetails.ISBN)> string[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string) </ISBN[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.VariationProductListingDetails.ISBN)>
            <UPC[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.VariationProductListingDetails.UPC)> string[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string) </UPC[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.VariationProductListingDetails.UPC)>
          </VariationProductListingDetails[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.VariationProductListingDetails)>
          <VariationSpecifics[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.VariationSpecifics)> NameValueListArrayType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/NameValueListArrayType.html)
            <NameValueList[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.VariationSpecifics.NameValueList)> NameValueListType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/NameValueListType.html)
              <Name[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.VariationSpecifics.NameValueList.Name)> string[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string) </Name[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.VariationSpecifics.NameValueList.Name)>
              <Value[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.VariationSpecifics.NameValueList.Value)> string[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string) </Value[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.VariationSpecifics.NameValueList.Value)>
              <!-- ... more Value values allowed here ... -->
            </NameValueList[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.VariationSpecifics.NameValueList)>
            <!-- ... more NameValueList nodes allowed here ... -->
          </VariationSpecifics[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.VariationSpecifics)>
          <!-- ... more VariationSpecifics nodes allowed here ... -->
        </Variation[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation)>
        <!-- ... more Variation nodes allowed here ... -->
      </Variations[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations)>
      <WatchCount[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.WatchCount)> long[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#long) </WatchCount[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.WatchCount)>
    </Item[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item)>
    <!-- ... more Item nodes allowed here ... -->
  </ItemArray[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray)>
  <ItemsPerPage[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemsPerPage)> int[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#int) </ItemsPerPage[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemsPerPage)>
  <PageNumber[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.PageNumber)> int[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#int) </PageNumber[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.PageNumber)>
  <PaginationResult[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.PaginationResult)> PaginationResultType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/PaginationResultType.html)
    <TotalNumberOfEntries[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.PaginationResult.TotalNumberOfEntries)> int[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#int) </TotalNumberOfEntries[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.PaginationResult.TotalNumberOfEntries)>
    <TotalNumberOfPages[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.PaginationResult.TotalNumberOfPages)> int[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#int) </TotalNumberOfPages[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.PaginationResult.TotalNumberOfPages)>
  </PaginationResult[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.PaginationResult)>
  <ReturnedItemCountActual[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ReturnedItemCountActual)> int[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#int) </ReturnedItemCountActual[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ReturnedItemCountActual)>
  <Seller[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller)> UserType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/UserType.html)
    <AboutMePage[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.AboutMePage)> boolean[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean) </AboutMePage[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.AboutMePage)>
    <eBayGoodStanding[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.eBayGoodStanding)> boolean[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean) </eBayGoodStanding[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.eBayGoodStanding)>
    <Email[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.Email)> string[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string) </Email[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.Email)>
    <FeedbackPrivate[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.FeedbackPrivate)> boolean[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean) </FeedbackPrivate[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.FeedbackPrivate)>
    <FeedbackRatingStar[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.FeedbackRatingStar)> FeedbackRatingStarCodeType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/FeedbackRatingStarCodeType.html) </FeedbackRatingStar[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.FeedbackRatingStar)>
    <FeedbackScore[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.FeedbackScore)> int[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#int) </FeedbackScore[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.FeedbackScore)>
    <IDVerified[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.IDVerified)> boolean[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean) </IDVerified[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.IDVerified)>
    <NewUser[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.NewUser)> boolean[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean) </NewUser[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.NewUser)>
    <RegistrationDate[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.RegistrationDate)> dateTime[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#dateTime) </RegistrationDate[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.RegistrationDate)>
    <SellerInfo[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.SellerInfo)> SellerType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/SellerType.html)
      <AllowPaymentEdit[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.SellerInfo.AllowPaymentEdit)> boolean[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean) </AllowPaymentEdit[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.SellerInfo.AllowPaymentEdit)>
      <CheckoutEnabled[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.SellerInfo.CheckoutEnabled)> boolean[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean) </CheckoutEnabled[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.SellerInfo.CheckoutEnabled)>
      <CIPBankAccountStored[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.SellerInfo.CIPBankAccountStored)> boolean[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean) </CIPBankAccountStored[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.SellerInfo.CIPBankAccountStored)>
      <GoodStanding[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.SellerInfo.GoodStanding)> boolean[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean) </GoodStanding[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.SellerInfo.GoodStanding)>
      <QualifiesForB2BVAT[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.SellerInfo.QualifiesForB2BVAT)> boolean[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean) </QualifiesForB2BVAT[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.SellerInfo.QualifiesForB2BVAT)>
      <SafePaymentExempt[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.SellerInfo.SafePaymentExempt)> boolean[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean) </SafePaymentExempt[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.SellerInfo.SafePaymentExempt)>
      <SellerLevel[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.SellerInfo.SellerLevel)> SellerLevelCodeType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/SellerLevelCodeType.html) </SellerLevel[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.SellerInfo.SellerLevel)>
      <StoreOwner[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.SellerInfo.StoreOwner)> boolean[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean) </StoreOwner[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.SellerInfo.StoreOwner)>
      <StoreURL[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.SellerInfo.StoreURL)> anyURI[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#anyURI) </StoreURL[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.SellerInfo.StoreURL)>
      <TopRatedSeller[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.SellerInfo.TopRatedSeller)> boolean[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean) </TopRatedSeller[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.SellerInfo.TopRatedSeller)>
    </SellerInfo[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.SellerInfo)>
    <Site[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.Site)> SiteCodeType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/SiteCodeType.html) </Site[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.Site)>
    <Status[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.Status)> UserStatusCodeType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/UserStatusCodeType.html) </Status[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.Status)>
    <UserAnonymized[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.UserAnonymized)> boolean[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean) </UserAnonymized[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.UserAnonymized)>
    <UserID[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.UserID)> UserIDType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/UserIDType.html) (string[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string)) </UserID[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.UserID)>
    <UserIDChanged[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.UserIDChanged)> boolean[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean) </UserIDChanged[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.UserIDChanged)>
    <UserIDLastChanged[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.UserIDLastChanged)> dateTime[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#dateTime) </UserIDLastChanged[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.UserIDLastChanged)>
    <VATStatus[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.VATStatus)> VATStatusCodeType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/VATStatusCodeType.html) </VATStatus[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.VATStatus)>
  </Seller[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller)>
  <!-- Standard Output Fields -->
  <Ack[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Ack)> AckCodeType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/AckCodeType.html) </Ack[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Ack)>
  <Build[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Build)> string[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string) </Build[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Build)>
  <CorrelationID[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.CorrelationID)> string[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string) </CorrelationID[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.CorrelationID)>
  <Errors[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Errors)> ErrorType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/ErrorType.html)
    <ErrorClassification[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Errors.ErrorClassification)> ErrorClassificationCodeType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/ErrorClassificationCodeType.html) </ErrorClassification[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Errors.ErrorClassification)>
    <ErrorCode[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Errors.ErrorCode)> token[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#token) </ErrorCode[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Errors.ErrorCode)>
    <ErrorParameters[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Errors.ErrorParameters) ParamID="string[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string)"> ErrorParameterType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/ErrorParameterType.html)
      <Value[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Errors.ErrorParameters.Value)> string[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string) </Value[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Errors.ErrorParameters.Value)>
    </ErrorParameters[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Errors.ErrorParameters)>
    <!-- ... more ErrorParameters nodes allowed here ... -->
    <LongMessage[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Errors.LongMessage)> string[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string) </LongMessage[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Errors.LongMessage)>
    <SeverityCode[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Errors.SeverityCode)> SeverityCodeType[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/SeverityCodeType.html) </SeverityCode[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Errors.SeverityCode)>
    <ShortMessage[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Errors.ShortMessage)> string[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string) </ShortMessage[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Errors.ShortMessage)>
  </Errors[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Errors)>
  <!-- ... more Errors nodes allowed here ... -->
  <HardExpirationWarning[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.HardExpirationWarning)> string[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string) </HardExpirationWarning[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.HardExpirationWarning)>
  <Timestamp[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Timestamp)> dateTime[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#dateTime) </Timestamp[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Timestamp)>
  <Version[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Version)> string[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string) </Version[](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Version)>
</GetSellerListResponse>

```
  
| Return Value  | Type  | Occurrence  | Meaning  |  
| --- | --- | --- | --- |  
|  **Call-specific Output Fields** [[Jump to standard fields]](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#stdOutputFields)  |  
| --- |  
|  **HasMoreItems**  | [boolean](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean)  | Always  |  This field's value is returned as `true` if there are more pages in the current result set to view, or `false` if the current page being viewed is the last (or only) page of the result set.   
  
If there are more listings to view in the result set, additional **GetSellerList** calls can be made but with changes to the **Pagination** values in the request. For example, if the **Pagination.PageNumber** value in the request for the last call was `1`, you can make another **GetSellerList** call, keeping everything the same except changing the value of the **Pagination.PageNumber** field from `1` to `2`.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll. Also returned if DetailLevel is not provided on input.   |  
| --- | --- | --- | --- |  
|  **ItemArray**  | [ItemArrayType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/ItemArrayType.html)  | Always  |  This container is an array of one or more listings that match the input criteria. If none of the seller's listings match the input criteria, this container is returned as an empty tag.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll. Also returned if DetailLevel is not provided on input.   |  
|  ItemArray.**Item**  | [ItemType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/ItemType.html)  | Conditionally,   
[repeatable](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#repeatable): [0..*]  |  Contains the data properties that define one item listing. **GetSellerEvents** and **GetSellerList** only return items if any are available for the seller within the time window specified in the request.  
  
Some optional fields are only returned if the seller defined them for the item. Some fields are only returned under particular conditions specified in the individual field descriptions. For example, a buyer's contact information might only be returned if the member who is making the request (as identified in the **eBayAuthToken**) has an order relationship with that buyer.   
  
For calls that support detail levels, the set of fields returned is also controlled by the value of **DetailLevel** in the request. For some calls, other parameters in the request can also control the data returned for each item. For example, **GranularityLevel** controls the fields to return for each item in the **GetSellerList** response.   
**Note:** When making a **GetSellerList** call, items that are on-hold due to an eBay policy violation will not be returned in the response.    
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll. Also returned if DetailLevel is not provided on input.   |  
|  ItemArray.Item.**ApplicationData**  | [string](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string)  | Conditionally  |  Return custom, application-specific data associated with the item. The data you specify is stored by eBay with the item for your own reference, but it is not used by eBay in any way. Use **ApplicationData** to store special information for yourself, such as a part number. For a SKU in an eBay.com listing, use the **SKU** element instead. To remove this value when revising or relisting an item, use **DeletedField**.  
**Max length:** 32.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Coarse, Fine, Medium.   |  
|  ItemArray.Item.**AutoPay**  | [boolean](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean)  | Conditionally  |  This field is included and set to if `true` in an Add/Revise/Relist call if the seller wants to require immediate payment from the buyer. If this field is set to `false` or not included, the seller is not requesting immediate payment.   
  
Note that this field may be set to `true`, but that does not necessarily mean that the buyer will be required to pay right away. For example, immediate payment is not currently applicable to auctions items won in a competitive bidding process or to items where the buyer and seller negotiated the price through the Best Offer feature. Immediate payment is also not applicable to listings where the payment happens offline between the buyer and seller.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Coarse, Fine, Medium.   |  
|  ItemArray.Item  
.**BuyerGuaranteePrice**  |  [AmountType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/AmountType.html) ([double](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#double))  | Conditionally  |  The eBay Best Price Guarantee price. The [Best Price Guarantee](https://pages.ebay.com.au/buy/Best_Price_Guarantee/) program is only available on the eBay Australia marketplace.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Coarse, Fine, Medium.   |  
| ItemArray.Item  
.**BuyerGuaranteePrice**  
[ attribute **currencyID** ]  | [CurrencyCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html)  | Conditionally  |  The eBay Best Price Guarantee price. The [Best Price Guarantee](https://pages.ebay.com.au/buy/Best_Price_Guarantee/) program is only available on the eBay Australia marketplace.  
  
For a list of possible enumeration values, see [CurrencyCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html).   |  
|  ItemArray.Item.**BuyerProtection**  | [BuyerProtectionCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/BuyerProtectionCodeType.html)  | Conditionally  |  The enumeration value returned in this field indicates whether an item is eligible for the buyer protection.   
  
**Applicable values** : See [BuyerProtection](https://developer.ebay.com/devzone/xml/docs/reference/ebay/extra/gtsllrlst.rspns.itmarry.itm.byrprtctn.html).   
Code so that your app gracefully handles any future changes to this list.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Coarse, Fine, Medium.   |  
|  ItemArray.Item  
.**BuyerRequirementDetails**  | [BuyerRequirementDetailsType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/BuyerRequirementDetailsType.html)  | Conditionally  |  This container is returned if the seller has applied one or more buyer requirement criteria to the listing. Buyer requirement settings are managed in the Selling Preferences section of the seller's account in My eBay.   |  
|  ItemArray.Item  
.BuyerRequirementDetails  
.**MaximumItemRequirements**  | [MaximumItemRequirementsType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/MaximumItemRequirementsType.html)  | Conditionally  |  This container is returned if the seller has set a maximum quantity threshold buyer requirement. With this buyer requirement, a buyer is limited in regards to the quantity of a line item that may be purchased.   
  
This buyer requirement is only applicable to fixed-price listings where multiple quantity is available for purchase.   
  
In addition to setting a maximum quantity threshold buyer requirement, the seller can also choose to apply this threshold to only those prospective buyers who don't meet or exceed the minimum Feedback score threshold.   |  
|  ItemArray.Item  
.BuyerRequirementDetails  
.MaximumItemRequirements  
.**MaximumItemCount**  | [int](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#int)  | Conditionally  |  This field indicates the maximum quantity of a line item that one prospective buyer may purchase from the listing.   
  
This buyer requirement is only applicable to fixed-price listings where multiple quantity is available for purchase.   
  
If the **MinimumFeedbackScore** field is also set/returned, the maximum quantity threshold value will only apply to those prospective buyers who don't meet or exceed the minimum Feedback score threshold returned in that field. If the **MinimumFeedbackScore** field not set/returned, the maximum quantity threshold value will apply to all prospective buyers.   
  
This field is always returned along with the **MaximumItemRequirements** container.   |  
|  ItemArray.Item  
.BuyerRequirementDetails  
.MaximumItemRequirements  
.**MinimumFeedbackScore**  | [int](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#int)  | Conditionally  |  If this field is returned, it indicates that the seller has set a maximum quantity threshold value, but this maximum quantity threshold value (returned in **MaximumItemCount** will only apply to those prospective buyers who don't meet or exceed the minimum Feedback score threshold returned in this field. If this field is not returned, the maximum quantity threshold value will apply to all prospective buyers.   |  
|  ItemArray.Item  
.BuyerRequirementDetails  
.**MaximumUnpaidItemStrikesInfo**  | [MaximumUnpaidItemStrikesInfoType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/MaximumUnpaidItemStrikesInfoType.html)  | Conditionally  |  This container is returned if the seller has enabled a setting to block prospective buyers who have one or more unpaid items and/or buyer-initiated cancellations on their account during a specified time period.   |  
|  ItemArray.Item  
.BuyerRequirementDetails  
.MaximumUnpaidItemStrikesInfo  
.**Count**  | [int](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#int)  | Conditionally  |  This integer value indicates the maximum number of unpaid items and/or buyer-initiated cancellations that a prospective buyer is allowed to have during a specified time period (**MaximumUnpaidItemStrikesInfo.Period**) before being blocked from buying or bidding on the item.   |  
|  ItemArray.Item  
.BuyerRequirementDetails  
.MaximumUnpaidItemStrikesInfo  
.**Period**  | [PeriodCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/PeriodCodeType.html)  | Conditionally  |  This enumerated value defines the length of time over which a prospective buyer's unpaid items and/or buyer-initiated cancellations will be counted. If the prospective buyer's number of unpaid items and/or buyer-initiated cancellations during this defined period exceeds the value set in the **MaximumUnpaidItemStrikesInfo.Count** field, that prospective buyer is blocked from buying/bidding on the item.   
  
If the **Count** value is 2, and the specified **Period** is `Days_30` (counting back 30 days from the present day), any prospective buyer that has had three or more unpaid items and/or buyer-initiated cancellations is blocked from buying/bidding on the item.   
  
**Applicable values** :   
  


CustomCode
    (out) This value is reserved for future or internal use. 

Days_180
    (out) This value indicates that the evaluation period is set back 180 days (approximately 6 months) from the present date. 

Days_30
    (out) This value indicates that the evaluation period is set back 30 days from the present date. 

Days_360
    (out) This value indicates that the evaluation period is set back 360 days (approximately 12 months) from the present date.   
Code so that your app gracefully handles any future changes to this list.   |  
|  ItemArray.Item  
.BuyerRequirementDetails  
.**ShipToRegistrationCountry**  | [boolean](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean)  | Conditionally  |  This field is returned as `true` if the seller has enabled the setting to block buyers/bidders who reside (according to their eBay primary shipping address) in countries that are on the seller's ship-to exclusion list.   
  
**Default:** false.   |  
|  ItemArray.Item  
.BuyerRequirementDetails  
.**ZeroFeedbackScore**  | [boolean](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean)  | Conditionally  |  This field is returned as `true` if the seller has enabled the setting to block buyers/bidders with a feedback score of 0 from buying items.   
  
**Default:** false.   |  
|  ItemArray.Item.**BuyItNowPrice**  |  [AmountType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/AmountType.html) ([double](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#double))  | Conditionally  |  This field is only applicable for auction listings. By specifying a 'Buy It Now' price, a seller is allowing prospective buyers the opportunity to purchase the item in the auction listing at this price immediately. When a buyer uses the 'Buy It Now' option to purchase the item, the auction listing will end immediately.   
  
By including this field and specifying a 'Buy It Now' price, the seller is enabling the 'Buy It Now' feature on the auction listing. If the seller includes this field for any other listing type other than an auction, this field and its price will just be ignored.   
  
The price in this field must be at least 30 percent higher than the starting bid price (which is specified in an Add call through the **Item.StartPrice** field). Once a bid is made on an auction listing, and the bid meets or exceeds the **Item.ReservePrice** value (if set), the 'Buy It Now' option becomes unavailable, and this field will no longer be applicable. If there is no Reserve Price, the first bid will nullify the 'Buy It Now' option.   
  
Keep in mind that **GetItem** (and other 'Get' calls that retrieve the Item details) may still return the **BuyItNowPrice** field for an auction item even if the 'Buy It Now' option is no longer available. Instead, a user should look for the **ListingDetails.BuyItNowAvailable** boolean field in the **GetItem** response to determine if the 'Buy It Now' option is still available for the auction item.   
  
**Note:** For the US site, new eBay sellers are subject to [Seller Limits](https://developer.ebay.com/api-docs/user-guides/static/make-a-call/fg-replaced.html), which limit the quantity of items that may be listed and/or the total cumulative value of these listings. While subject to these selling limits, an eBay seller can use the **GetMyeBaySelling** call to retrieve both the remaining number of listings they can create and the remaining cumulative value of these listings. These values are shown in the **Summary.QuantityLimitRemaining** and **Summary.AmountLimitRemaining** fields in the **GetMyeBaySelling** response. If a call to add an item or revise an item would result in the exceeding of these limits, the add item or revise item call will fail. These fields will only be returned if the seller is subject to seller limits.    
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine, Medium.   |  
| ItemArray.Item.**BuyItNowPrice**  
[ attribute **currencyID** ]  | [CurrencyCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html)  | Conditionally  |  This field is only applicable for auction listings. By specifying a 'Buy It Now' price, a seller is allowing prospective buyers the opportunity to purchase the item in the auction listing at this price immediately. When a buyer uses the 'Buy It Now' option to purchase the item, the auction listing will end immediately.   
  
By including this field and specifying a 'Buy It Now' price, the seller is enabling the 'Buy It Now' feature on the auction listing. If the seller includes this field for any other listing type other than an auction, this field and its price will just be ignored.   
  
The price in this field must be at least 30 percent higher than the starting bid price (which is specified in an Add call through the **Item.StartPrice** field). Once a bid is made on an auction listing, and the bid meets or exceeds the **Item.ReservePrice** value (if set), the 'Buy It Now' option becomes unavailable, and this field will no longer be applicable. If there is no Reserve Price, the first bid will nullify the 'Buy It Now' option.   
  
Keep in mind that **GetItem** (and other 'Get' calls that retrieve the Item details) may still return the **BuyItNowPrice** field for an auction item even if the 'Buy It Now' option is no longer available. Instead, a user should look for the **ListingDetails.BuyItNowAvailable** boolean field in the **GetItem** response to determine if the 'Buy It Now' option is still available for the auction item.   
  
**Note:** For the US site, new eBay sellers are subject to [Seller Limits](https://developer.ebay.com/api-docs/user-guides/static/make-a-call/fg-replaced.html), which limit the quantity of items that may be listed and/or the total cumulative value of these listings. While subject to these selling limits, an eBay seller can use the **GetMyeBaySelling** call to retrieve both the remaining number of listings they can create and the remaining cumulative value of these listings. These values are shown in the **Summary.QuantityLimitRemaining** and **Summary.AmountLimitRemaining** fields in the **GetMyeBaySelling** response. If a call to add an item or revise an item would result in the exceeding of these limits, the add item or revise item call will fail. These fields will only be returned if the seller is subject to seller limits.   
  
For a list of possible enumeration values, see [CurrencyCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html).   |  
|  ItemArray.Item.**Charity**  | [CharityType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CharityType.html)  | Conditionally  |  This container identifies the nonprofit organization that will benefit with a percentage of the proceeds from each sale of an item through an auction or fixed-price listing. Charity names and IDs can be found by going to [eBay for Charity](https://charity.ebay.com/charity-auctions/my-causes) page and doing a search. The donation percentage can be set in 5 percent increments from 10 percent to 100 percent.   
  
When it comes to revising an auction or fixed-price listing, you can add a benefitting charity (as long as there is at least 12 hours left before end of listing/close of auction), but you cannot remove or change a nonprofit company once one is already established in the original listing.   
  
**For Revise calls** : The non-profit organization and donation percentage can now be modified in a Revise call as long as there are no active bids on an auction listing, or no pending Best Offers/Counter Offers on a listing.   
  
This container will only be returned in Get calls for charitable listings. Charitable listings are only supported in the following marketplaces: US, UK, CA, DE, and Motors.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Coarse, Fine, Medium. See:   
[Buying and selling on eBay to benefit nonprofit organizations](https://www.ebay.com/help/account/donating-ebay-charity/buying-selling-ebay-benefit-nonprofit-organizations?id=4668)   
[Charitable listings](https://developer.ebay.com/api-docs/user-guides/static/trading-user-guide/charitable-listings.html)  |  
|  ItemArray.Item.Charity  
.**CharityID**  | [string](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string)  | Conditionally  |  The unique identifier that eBay creates and assigns to each nonprofit organization.   
  
The field is conditionally required in an Add/Revise/Relist call if the seller will be donating a percentage of the sale proceeds to this organization for each sale generated by the listing.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   |  
|  ItemArray.Item.Charity  
.**CharityListing**  | [boolean](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean)  | Conditionally  |  If this field is returned as `true`, a percentage of order line item's purchase price will be donated to a nonprofit organization.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   |  
|  ItemArray.Item.Charity  
.**CharityName**  | [string](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string)  | Conditionally  |  The full name of the nonprofit organization.   
  
  
**Max length:** 150.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   |  
|  ItemArray.Item.Charity  
.**DonationPercent**  | [float](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#float)  | Conditionally  |  The percentage of the purchase price that the seller chooses to donate to the selected nonprofit organization. This percentage is displayed in the eBay for Charity listing. **Possible values** : 10.0 to 100.0. 
  * Percentages must increment by 5.0. 
  * Minimum donation percentages may be required for eBay for Charity listings, see [ Selling to benefit nonprofit organizations](http://pages.ebay.com/help/sell/selling-nonprofit.html) for details. 

The **DonationPercent** field is required in an Add/Revise/Relist call if the seller will be donating a percentage of the sale proceeds for each sale generated by the listing.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   |  
|  ItemArray.Item.Charity.**LogoURL**  | [string](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string)  | Conditionally  |  The full URL to the nonprofit organization's logo image file. This logo image file is the image that is displayed in all eBay listings that benefit that charity. This field is returned as long as it is defined for the nonprofit organization.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   |  
|  ItemArray.Item.Charity.**Mission**  | [string](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string)  | Conditionally  |  The stated mission of the nonprofit charity organization. This mission statement is displayed in the eBay for Charity section of the View Item page.   
  
  
**Max length:** 511.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   |  
|  ItemArray.Item.Charity.**Status**  | [CharityStatusCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CharityStatusCodeType.html)  | Conditionally  |  This enumeration value indicates whether or not the nonprofit organization is a valid eBay for Charity organization, and is able to receive proceeds from eBay sales.   
  
**Applicable values** :   
  


CustomCode
    (out) Reserved for internal or future use. 

NoLongerValid
    (out) The specified nonprofit charity organization is no longer a valid nonprofit charity organization according to the requirements of the PayPal Giving Fund. 

Valid
    (out) The specified nonprofit charity organization is a valid nonprofit charity organization according to the requirements of the PayPal Giving Fund.   
Code so that your app gracefully handles any future changes to this list.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   |  
|  ItemArray.Item  
.**ConditionDescription**  | [string](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string)  | Conditionally  |  This string field is used by the seller to more clearly describe the condition of items that are not brand new.   
  
The **ConditionDescription** field is available for all categories, including categories where the condition type is not applicable (e.g., Antiques). This field is applicable for all item conditions except 'New', 'Brand New', 'New with tags', and 'New in box'. If **ConditionDescription** is used with these conditions (Condition IDs 1000-1499), eBay will simply ignore this field if included, and eBay will return a warning message to the user.   
  
The **ConditionDescription** field is returned by **GetItem** (and other related calls that return the Item object) if a condition description is specified in the listing.   
**Note:** This field should not be included if **ConditionDescriptors** are being used. If it is used, a warning will be triggered and the field will be dropped from the listing.   
**Note:** For **GetItem** , this field is returned only if it is set in the listing.  
**Max length:** 1000.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Coarse, Fine, Medium.   |  
|  ItemArray.Item.**Country**  | [CountryCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CountryCodeType.html)  | Conditionally  |  This two-digit enumeration value indicates the country where the item is located. **CountryCodeType** defines the supported values. The [GeteBayDetails](https://developer.ebay.com/DevZone/XML/docs/Reference/eBay/GeteBayDetails.html) call can also be used (include the **DetailName** field and set its value to **CountryDetails**) to see the full list of supported country codes.   
  
In an Add/Revise/Relist/Verify call, this field is required.   
  
**Applicable values** : See [Country](https://developer.ebay.com/devzone/xml/docs/reference/ebay/extra/gtsllrlst.rspns.itmarry.itm.cntry.html).   
Code so that your app gracefully handles any future changes to this list.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Coarse.   |  
|  ItemArray.Item  
.**CrossBorderTrade**  | [string](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string)  | Conditionally,   
[repeatable](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#repeatable): [0..*]  |  This field is used by sellers who want their listing to be returned in the search results for other eBay sites. This feature is currently only supported by the US, UK, eBay Canada, and eBay Ireland sites. See [Getting exposure on international sites](https://pages.ebay.com/help/sell/globalexposure.html) for full requirements on using this feature. There is a small listing fee for each country specified as a Cross Border Trade country.   
  
US listings that offer shipping to Canada, North America, or worldwide are automatically returned on eBay.ca at no extra charge, so US listings that offer shipping to these locations do not need to specify Canada as a Cross Border Trade country.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Coarse, Fine, Medium. See [Cross-border trading](https://developer.ebay.com/api-docs/user-guides/static/trading-user-guide/cross-border-trading.html).  |  
|  ItemArray.Item.**Currency**  | [CurrencyCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html)  | Conditionally  |  In an Add/Revise/Relist/Verify call, this required three-digit enumeration value defines the currency associated with the listing site. The item price and all costs passed in the call request will be using this currency. Similarly, the listing fees and other cost-related data will be using this currency. Since the Trading API can only be used for a select number of eBay sites, only a subset of values are supporting when adding/revising/relisting an item. These supported values are discussed in the top section of **CurrencyCodeType**.   
  
In 'Get' calls, it is possible that any of the values in **CurrencyCodeType** may appear, as some cost-related fields will show the buyer's currency type.   
  
**Applicable values** : See [Currency](https://developer.ebay.com/devzone/xml/docs/reference/ebay/extra/gtsllrlst.rspns.itmarry.itm.crrncy.html).   
Code so that your app gracefully handles any future changes to this list.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Coarse, Fine, Medium.   |  
|  ItemArray.Item.**Description**  | [string](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string)  | Conditionally  |  The seller's description of the item. In listing requests, you can submit your description using CDATA if you want to use HTML or XML-reserved characters in the description. However, a seller can not use any active content in their listing description. Active content includes animation or video via JavaScript, Flash, plug-ins, or form actions. All active content will be blocked/removed from a listing. Removing/blocking active content will lead to faster load times of listings, make listings more mobile-friendly, improve SEO performance, and lead to a more secure eBay Marketplace.   
  
**Note:** To ensure that a listing description is optimized to be viewed on a mobile devices, see [Mobile device optimization](https://developer.ebay.com/api-docs/user-guides/static/trading-user-guide/mobile.html) in the Trading User Guide.   
  
Note that the mobile-friendly description snippet feature described in this topic is currently only available in the following eBay marketplaces: US, UK, Australia, France, Germany, Italy, Spain, and eBay Motors.    
In the listing description, sellers are only allowed to provide links to product videos, freight shipping services, or other legally required information, and when providing these links in the listing description, the secure 'https' protocol must be used instead of 'http'. In addition, any valid links to sites outside of eBay should use the _target="_blank"_ attribute in the **a href** tag so a new browser window will be loaded when the link is clicked instead of buyers being redirected off of eBay. For more information on using links in the listing description, see eBay's [Links policy](http://pages.ebay.com/help/policies/listing-links.html). For more information about the stronger security standards that eBay is using, see the [Use secure HTTPS for enhanced browser security](https://pages.ebay.com/seller-center/seller-updates/2018-fall/marketplace-update.html#use-secure-https) topic in the 2018 Fall Seller Update. The [getListingViolations](https://developer.ebay.com/api-docs/sell/compliance/resources/listing_violation/methods/getListingViolations) method of the Compliance API can be used to see if any of the seller's active listings are not 'HTTPS' compliant.   
  
If you embed pictures in the description (by using IMG tags) instead of using **PictureURL** , but you want a camera icon to appear in search and listing pages, specify the following null-image URL in the **PictureURL** field: https://pics.ebay.com/aw/pics/dot_clear.gif. See [Add pictures](https://developer.ebay.com/api-docs/user-guides/static/trading-user-guide/pictures.html) in the Trading API User Guide.   
  
This field is conditionally required for all listings. The exception is when the seller specifies a product identifier, such as a GTIN or ePID, through the **ProductListingDetails** container and a product match is found in the eBay product catalog. If a matching product is found in the eBay product catalog, the item description will be created automatically (as long as the **ProductListingDetails.IncludeeBayProductDetails** value is `true`).   
  
**Max length:** 500000 (some sites may allow more, but the exact number may vary).   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   |  
|  ItemArray.Item  
.**DisableBuyerRequirements**  | [boolean](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean)  | Conditionally  |  This field can be included and set to `true` in an Add or Revise call if the seller wishes to disable all buyer requirements (that are set in the seller's account) for the listing. (from **Item.BuyerRequirementDetails** or Buyer requirements preferences in My eBay) are ignored.   
  
This field will only be returned in 'Get' calls if `true`.  
**Default:** false.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   |  
|  ItemArray.Item  
.**DiscountPriceInfo**  | [DiscountPriceInfoType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/DiscountPriceInfoType.html)  | Conditionally  |  This container provides information for an item that has a Strikethrough Price (STP) or a Minimum Advertised Price (MAP) discount pricing treatment. STP and MAP apply only to fixed-price listings. STP is available on the US, eBay Motors, UK, Germany, Canada (English and French), France, Italy, Spain, and Ireland sites, while MAP is available only on the US site.   
  
Discount pricing is available to qualified sellers (and their associated developers) who participate in the Discount Pricing Program. Once qualified, sellers receive a 'special account flag' (SAF) that allows them to apply Discount Pricing to both single-variation and multi-variation items. STP is intended for eBay partners and their sellers only.   
  
As a seller listing Discount Price items, you are required to maintain records of your discount pricing in the event you are called upon to substantiate your item pricing.   
  
**For AddFixedPriceItem, RelistFixedPriceItem, ReviseFixedPriceItem, and VerifyAddFixedPriceItem** : If you are listing variations (MSKU items), use **Variation.DiscountPriceInfo** for each variation.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   |  
|  ItemArray.Item  
.DiscountPriceInfo  
.**MadeForOutletComparisonPrice**  |  [AmountType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/AmountType.html) ([double](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#double))  | Conditionally  |  Applicable only if the item was specifically made for sale through dedicated eBay outlet pages (e.g., eBay Fashion Outlet).  
  
The comparison price is the price of a comparable product sold through non-outlet channels on eBay (or elsewhere), or not specifically made for the outlet.  
  
In fashion, a "comparable" product shares the same design, but is not considered an identical product. Some products are specifically made for outlets, and may have a different SKU than the "comparable" product. These made-for-outlet products may be manufactured in a different place, with different materials, or according to different specifications (i.e. different stitch pattern, seam reinforcement, button quality, etc.)   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   |  
| ItemArray.Item  
.DiscountPriceInfo  
.**MadeForOutletComparisonPrice**  
[ attribute **currencyID** ]  | [CurrencyCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html)  | Conditionally  |  Applicable only if the item was specifically made for sale through dedicated eBay outlet pages (e.g., eBay Fashion Outlet).  
  
The comparison price is the price of a comparable product sold through non-outlet channels on eBay (or elsewhere), or not specifically made for the outlet.  
  
In fashion, a "comparable" product shares the same design, but is not considered an identical product. Some products are specifically made for outlets, and may have a different SKU than the "comparable" product. These made-for-outlet products may be manufactured in a different place, with different materials, or according to different specifications (i.e. different stitch pattern, seam reinforcement, button quality, etc.)  
  
For a list of possible enumeration values, see [CurrencyCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html).   |  
|  ItemArray.Item  
.DiscountPriceInfo  
.**MinimumAdvertisedPrice**  |  [AmountType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/AmountType.html) ([double](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#double))  | Conditionally  |  Minimum Advertised Price (MAP) is an agreement between suppliers (or manufacturers (OEM)) and the retailers (sellers) stipulating the lowest price an item is allowed to be advertised at. Sellers can offer prices below MAP by means of other discounts. This only applies to fixed-price listings and auction listings with the Buy It Now option.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   |  
| ItemArray.Item  
.DiscountPriceInfo  
.**MinimumAdvertisedPrice**  
[ attribute **currencyID** ]  | [CurrencyCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html)  | Conditionally  |  Minimum Advertised Price (MAP) is an agreement between suppliers (or manufacturers (OEM)) and the retailers (sellers) stipulating the lowest price an item is allowed to be advertised at. Sellers can offer prices below MAP by means of other discounts. This only applies to fixed-price listings and auction listings with the Buy It Now option.  
  
For a list of possible enumeration values, see [CurrencyCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html).   |  
|  ItemArray.Item  
.DiscountPriceInfo  
.**MinimumAdvertisedPriceExposure**  | [MinimumAdvertisedPriceExposureCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/MinimumAdvertisedPriceExposureCodeType.html)  | Conditionally  |  For MinimumAdvertisedPrice (MAP) listings only. A seller cannot show the actual discounted price on eBay's View Item page. Instead, the buyer can either click on a pop-up on eBay's View Item page, or the discount price will be shown during checkout.   
  
**Applicable values** :   
  


CustomCode
    (in/out) Reserved for future use. 

DuringCheckout
    (in/out) This enumeration value indicates that the discounted price will only be shown to the buyer once the buyer reaches the eBay Checkout page. To enable this pricing treatment when adding/revising/relisting an item, include the **DiscountPriceInfo.MinimumAdvertisedPriceExposure** field in an Add/Revise/Relist calls and set its value to `DuringCheckout`. 

None
    (in/out) The value None is no longer valid. If provided in the request, it will be mapped to `PreCheckout`. 

PreCheckout
    (in/out) This enumeration value indicates that the buyer must add the item to his/her cart before the discounted price can be displayed. To enable this pricing treatment when adding/revising/relisting an item, include the **DiscountPriceInfo.MinimumAdvertisedPriceExposure** field in an Add/Revise/Relist calls and set its value to `PreCheckout`.   
Code so that your app gracefully handles any future changes to this list.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   |  
|  ItemArray.Item  
.DiscountPriceInfo  
.**OriginalRetailPrice**  |  [AmountType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/AmountType.html) ([double](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#double))  | Conditionally  |  The actual retail price set by the manufacturer (OEM). eBay does not maintain or validate the **OriginalRetailPrice** supplied by the seller. **OriginalRetailPrice** should always be more than **StartPrice**. Compare the **StartPrice** /**BuyItNowPrice** to **OriginalRetailPrice** to determine the amount of savings to the buyer.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   |  
| ItemArray.Item  
.DiscountPriceInfo  
.**OriginalRetailPrice**  
[ attribute **currencyID** ]  | [CurrencyCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html)  | Conditionally  |  The actual retail price set by the manufacturer (OEM). eBay does not maintain or validate the **OriginalRetailPrice** supplied by the seller. **OriginalRetailPrice** should always be more than **StartPrice**. Compare the **StartPrice** /**BuyItNowPrice** to **OriginalRetailPrice** to determine the amount of savings to the buyer.  
  
For a list of possible enumeration values, see [CurrencyCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html).   |  
|  ItemArray.Item  
.DiscountPriceInfo  
.**PricingTreatment**  | [PricingTreatmentCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/PricingTreatmentCodeType.html)  | Conditionally  |  Based on **OriginalRetailPrice** , **MinimumAdvertisedPrice** , and **StartPrice** values, eBay identifies whether the listing falls under MAP or STP (aka **OriginalRetailPrice**). **GetItem** returns this for items listed with one of these discount pricing treatments. **GetSellerList** returns the **DiscountPriceInfo** container. This field is not applicable for Add/Revise/Relist calls.  
**Default:** false.   
  
**Applicable values** :   
  


CustomCode
    (out) Reserved for future use. 

MAP
    (out) This enumeration value indicates that Minimum Advertised Pricing is enabled for the order line item. If this value is returned, the minimum advertised price is found in the **MinimumAdvertisedPrice** field. 

MFO
    (out) This enumeration value indicates that Made For Outlet Comparison Pricing is enabled for the order line item. If this value is returned, the Made For Outlet Comparison price is found in the **MadeForOutletComparisonPrice** field. 

None
    (out) This enumeration value indicates that neither Strikethrough Pricing or Minimum Advertised Pricing is enabled for the order line item. 

STP
    (out) This enumeration value indicates that Strikethrough Pricing is enabled for the order line item. If this value is returned, the price in the **OriginalRetailPrice** field will be crossed out in the View Item page.   
Code so that your app gracefully handles any future changes to this list.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   |  
|  ItemArray.Item  
.DiscountPriceInfo.**SoldOffeBay**  | [boolean](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean)  | Conditionally  |  Used by the eBay UK and eBay Germany (DE) sites, this flag indicates that the discount price (specified as StartPrice) is the price for which the seller offered the same (or similar) item for sale on a Web site or offline store other than eBay in the previous 30 days. The discount price is always in reference to the seller's own price for the item.   
  
If this field is set to `true`, eBay displays 'Was*' in the UK and 'Ursprunglich*' in Germany, next to the discounted price of the item. In the event both **SoldOffeBay** and **SoldOneBay** fields are set to `true`, **SoldOneBay** takes precedence.   
  
**Default:** false.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   |  
|  ItemArray.Item  
.DiscountPriceInfo.**SoldOneBay**  | [boolean](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean)  | Conditionally  |  Used by the eBay UK and eBay Germany (DE) sites, this flag indicates that the discount price (specified as **StartPrice**) is the price for which the seller offered the same (or similar) item for sale on eBay within the previous 30 days. The discount price is always in reference to the seller's own price for the item.   
  
If this field is set to `true`, eBay displays 'Was' in the UK and 'Ursprunglich' in Germany, next to the discounted price of the item. In the event both **SoldOffeBay** and **SoldOneBay** fields are set to `true`, **SoldOneBay** takes precedence.   
  
**Default:** false.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   |  
|  ItemArray.Item  
.**ExtendedSellerContactDetails**  | [ExtendedContactDetailsType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/ExtendedContactDetailsType.html)  | Conditionally  |  Extended contact information for sellers using the Classified Ad format. Specifies the days and hours when the seller can be contacted. To remove seller contact information when revising or relisting an item, use **DeletedField**.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll. Also returned if DetailLevel is not provided on input.   |  
|  ItemArray.Item  
.ExtendedSellerContactDetails  
.**ContactHoursDetails**  | [ContactHoursDetailsType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/ContactHoursDetailsType.html)  | Conditionally  |  This containers consists of fields that allows the seller of a Classified Ad listing to tell potential buyers what days and times they may be contacted to inquire about the listing.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll. Also returned if DetailLevel is not provided on input.   |  
|  ItemArray.Item  
.ExtendedSellerContactDetails  
.ContactHoursDetails  
.**Hours1AnyTime**  | [boolean](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean)  | Conditionally  |  Indicates whether or not a user is available to be contacted 24 hours a day during the range of days specified using the Hours1Days element. True indicates the user is available 24 hours a day, false indicates otherwise. In the case of this field being true, all values provided for Hours1From and Hours1To will be ignored. In the case of this field being false, the values provided Hours1From and Hours1To will be considered.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll. Also returned if DetailLevel is not provided on input.   |  
|  ItemArray.Item  
.ExtendedSellerContactDetails  
.ContactHoursDetails  
.**Hours1Days**  | [DaysCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/DaysCodeType.html)  | Conditionally  |  Indicates the range of days for which the primary contact hours specified by Hours1AnyTime or Hours1From and Hours1To apply. If a value of None is provided for this field, the values provided for Hours1AnyTime, Hours1From, Hours1To are ignored.   
  
**Applicable values** :   
  


CustomCode
    (in/out) Reserved for internal or future use. 

EveryDay
    (in/out) Seller can be contacted any day during the specified contact hours. 

None
    (in/out) Seller does not want to be contacted. Contact hours will not be supported for any days. If contact hours are specified, they will be ignored. 

Weekdays
    (in/out) Seller can be contacted Monday through Friday during the specified contact hours. 

Weekends
    (in/out) Seller can be contacted Saturday or Sunday during the specified contact hours.   
Code so that your app gracefully handles any future changes to this list.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll. Also returned if DetailLevel is not provided on input.   |  
|  ItemArray.Item  
.ExtendedSellerContactDetails  
.ContactHoursDetails  
.**Hours1From**  | [time](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#time)  | Conditionally  |  Indicates the starting time of day this eBay user is available for other eBay members to contact for the range of days specified using Hours1Days. Enter times in 30 minute increments from the top of the hour. That is, enter values either on the hour (:00) or 30 minutes past the hour (:30). Other values will be will be rounded down to the next closest 30 minute increment. Times entered should be local to the value provided for TimeZoneID.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll. Also returned if DetailLevel is not provided on input.   |  
|  ItemArray.Item  
.ExtendedSellerContactDetails  
.ContactHoursDetails.**Hours1To**  | [time](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#time)  | Conditionally  |  Indicates the ending time of day this eBay user is available for other eBay members to contact them for the range of days specified using Hours1Days. Enter times in 30 minute increments from the top of the hour. That is, enter values either on the hour (:00) or 30 minutes past the hour (:30). Other values will be will be rounded down to the next closest 30 minute increment. Times entered should be local to the value provided for TimeZoneID.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll. Also returned if DetailLevel is not provided on input.   |  
|  ItemArray.Item  
.ExtendedSellerContactDetails  
.ContactHoursDetails  
.**Hours2AnyTime**  | [boolean](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean)  | Conditionally  |  Indicates whether or not a user is available to be contacted 24 hours a day during the range of days specified using the Hours2Days element. True indicates the user is available 24 hours a day, false indicates otherwise. In the case of this field being true, all values provided for Hours2From and Hours2To will be ignored. In the case of this field being false, the values provided Hours2From and Hours2To will be considered.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll. Also returned if DetailLevel is not provided on input.   |  
|  ItemArray.Item  
.ExtendedSellerContactDetails  
.ContactHoursDetails  
.**Hours2Days**  | [DaysCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/DaysCodeType.html)  | Conditionally  |  Indicates the range of days for which the secondary contact hours specified by Hours2AnyTime or Hours2From and Hours2To apply. If a value of None is provided for this field, the values provided for Hours2AnyTime, Hours2From, Hours2To are ignored.   
**Note:** You cannot set Hours2Days to EveryDay. If Hours1Days is set to EveryDay, secondary contact hours do not apply. Hours2Days cannot be set to the same value as Hours1Days.   
  
**Applicable values** :   
  


CustomCode
    (in/out) Reserved for internal or future use. 

EveryDay
    (in/out) Seller can be contacted any day during the specified contact hours. 

None
    (in/out) Seller does not want to be contacted. Contact hours will not be supported for any days. If contact hours are specified, they will be ignored. 

Weekdays
    (in/out) Seller can be contacted Monday through Friday during the specified contact hours. 

Weekends
    (in/out) Seller can be contacted Saturday or Sunday during the specified contact hours.   
Code so that your app gracefully handles any future changes to this list.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll. Also returned if DetailLevel is not provided on input.   |  
|  ItemArray.Item  
.ExtendedSellerContactDetails  
.ContactHoursDetails  
.**Hours2From**  | [time](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#time)  | Conditionally  |  Indicates the starting time of day this eBay user is available for other eBay members to contact for the range of days specified using Hours2Days. Enter times in 30 minute increments from the top of the hour. That is, enter values either on the hour (:00) or 30 minutes past the hour (:30). Other values will be will be rounded down to the next closest 30 minute increment. Times entered should be local to the value provided for TimeZoneID.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll. Also returned if DetailLevel is not provided on input.   |  
|  ItemArray.Item  
.ExtendedSellerContactDetails  
.ContactHoursDetails.**Hours2To**  | [time](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#time)  | Conditionally  |  Indicates the ending time of day this eBay user is available for other eBay members to contact them for the range of days specified using Hours1Days. Enter times in 30 minute increments from the top of the hour. That is, enter values either on the hour (:00) or 30 minutes past the hour (:30). Other values will be will be rounded down to the next closest 30 minute increment. Times entered should be local to the value provided for TimeZoneID.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll. Also returned if DetailLevel is not provided on input.   |  
|  ItemArray.Item  
.ExtendedSellerContactDetails  
.ContactHoursDetails  
.**TimeZoneID**  | [string](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string)  | Conditionally  |  Indicates the local time zone of the values provided for Hours1From/Hours1To and Hours2From/Hours2To. If you specify a contact hours time range with Hours1From and Hours1To, you must provide a local time zone. To retrieve a complete list of the TimeZoneID values supported by eBay, call **GeteBayDetails** with **DetailName** set to **TimeZoneDetails**.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll. Also returned if DetailLevel is not provided on input.   |  
|  ItemArray.Item  
.**FreeAddedCategory**  | [CategoryType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CategoryType.html)  | Conditionally  |  The unique identifier for a secondary category that eBay has added as a free promotion. You cannot add this yourself. This container is only returned if the item was listed in a single category and eBay added a free secondary category.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   |  
|  ItemArray.Item  
.FreeAddedCategory.**CategoryID**  | [string](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string)  | Conditionally  |  This string value is the unique identifier of an eBay category. For listing calls, this ID must be a valid leaf on the category tree for the listing site. Validate against that marketplace's Taxonomy tree (for example, [getCategorySubtree](https://developer.ebay.com/api-docs/commerce/taxonomy/resources/category_tree/methods/getCategorySubtree) on tree 100 for eBay Motors). In **GetItem** and related calls, see the **CategoryName** field for the text name of the category. The parent category of this eBay category can be retrieved through the [Taxonomy API's](https://developer.ebay.com/api-docs/commerce/taxonomy/resources/methods) **getCategoryTree** or **getCategorySubtree** methods and inspecting the **parentCategoryTreeNodeHref** field in the response.   
**Note:** When listing in categoryID 173651 (Auto Performance Tuning Devices & Software), use of catalog products is required. For more information, see [Tuning devices and software](https://developer.ebay.com/api-docs/user-guides/static/trading-user-guide/tuning-devices-and-software.html).  In an Add call, the **PrimaryCategory.CategoryID** is conditionally required unless the seller successfully uses the **ProductListingDetails** container to find an eBay catalog product match. When the seller successfully uses an eBay catalog product to create a listing, the listing title, listing description, item specifics, listing category, and stock photo defined in the catalog product is used to create the listing.   
  
In an Add/Revise/Relist call, the **SecondaryCategory.CategoryID** is conditionally required if a Secondary Category is used. Using a Secondary Category can incur a listing fee. The secondary category ID must be a valid leaf category on the category tree for the listing site; an ID valid only on another marketplace tree is rejected. Validate against that marketplace's Taxonomy tree (for example, [getCategorySubtree](https://developer.ebay.com/api-docs/commerce/taxonomy/resources/category_tree/methods/getCategorySubtree) on tree 100 for eBay Motors).   
  
**For ReviseItem only:** Previously, removing the listing from a secondary category was only possible within 12 hours of the listing's scheduled end time when an auction listing had no active bids or a multiple-quantity, fixed-price listing had no items sold, but this restriction no longer exists. Now, the secondary category can be dropped for any active listing at any time, regardless of whether an auction listing has bids or a fixed-price listing has sales. To drop a secondary category, the seller passes in a value of `0` in the **SecondaryCategory.CategoryID** field.   
  
**Max length:** 10.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   |  
|  ItemArray.Item  
.FreeAddedCategory  
.**CategoryName**  | [string](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string)  | Conditionally  |  This string value is the display name of the eBay primary category, as it would appear on the eBay site. In **GetItem** , this will be a fully-qualified category name (e.g., Collectibles:Decorative Collectibles:Hummel, Goebel).   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   |  
|  ItemArray.Item.**HideFromSearch**  | [boolean](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean)  | Conditionally  |  This boolean field is returned as `true` if the listing has been hidden from all searches occurring on eBay. If a listing is hidden from eBay searches, the reason can be found in the **ReasonHideFromSearch** field.   |  
|  ItemArray.Item.**HitCount**  | [long](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#long)  | Conditionally  |  This value indicates the number of page views that a listing has received in the last 30 days.  
  
We recommend that you use the [getTrafficReport](https://developer.ebay.com/api-docs/sell/analytics/resources/traffic_report/methods/getTrafficReport) method of the **Analytics API** to return user traffic details received by a seller's listings. This RESTful method returns metrics such as click-through rate, listing impressions, listing views, sales conversion rate, and the number of completed transactions.  
  
**Note:** This field is only returned to authorized applications.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine.   |  
|  ItemArray.Item  
.**IntegratedMerchantCreditCardEnabled**  | [boolean](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean)  | Conditionally  |  This field is no longer applicable as eBay sellers can no longer use iMCC gateway accounts to handle buyer payments.   
**Note:** This field will stop being returned in order management calls on January 31, 2024.    
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine.   |  
|  ItemArray.Item  
.**InventoryTrackingMethod**  | [InventoryTrackingMethodCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/InventoryTrackingMethodCodeType.html)  | Conditionally  |  Indicates whether you prefer to track your eBay listings by eBay Item ID or by your own SKU.   
  
If a seller will be converting an existing eBay listing into the new Inventory model using the **bulkMigrateListings** call of the **Inventory API** , the **InventoryTrackingMethod** value must be set to `ItemID` (default value), but the item must also have a SKU value (Item.**SKU** or Variation.**SKU**) associated with it. **For GetItem and related calls** : Only returned when the value is `SKU`; not returned when the value is `ItemID`.   
  
  
**Applicable values** :   
  


CustomCode
    (in/out) Reserved for internal or future use. 

ItemID
    (in/out) Indicates the seller prefers to track the listing by its eBay item ID. This is the default for all listings. 

SKU
    (in/out) Indicates the seller prefers to track the listing by their own SKU.   
  
When you track by SKU, it means you can pass in your SKU instead of the eBay item ID in other calls that support SKU as an input field. If you choose SKU as your tracking preference for a listing, the value in **Item.SKU** must be unique across your active listings. You cannot create new listings with the same **Item.SKU** value while the listing is active (that is, until the existing listing with that SKU has ended).   
  
However, you can use **ReviseInventoryStatus** to update the quantity and/or price for the existing SKU as needed. When revising a listing where the **InventoryTrackingMethod** was set to SKU, you must pass in both the **InventoryTrackingMethod** tag (with the value set to SKU) and the SKU tag with the SKU value from your original listing.   
Code so that your app gracefully handles any future changes to this list.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll. See [eBay Merchant Data API](https://developer.ebay.com/DevZone/merchant-data/CallRef/index.html) for AddFixedPriceItem and ReviseFixedPriceItem.  |  
|  ItemArray.Item  
.**IsSecureDescription**  | [boolean](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean)  | Conditionally  |  This boolean field indicates whether or not the listing description is HTTPS secure/compliant. To be HTTPS secure/compliant, the **Item.Description** field may not contain any links to site pages that use the HTTP (and not HTTPS) protocol. This field will be returned with each listing that is found unless one or more **OutputSelector** fields are used and `Item.IsSecureDescription` is not one of the values passed in to one of these fields.   
  
If this field is returned as `true`, the listing is HTTPs secure/compliant, and the whole listing description will appear on the View Item page for the listing. If this field is returned as `false`, the listing is not HTTPs secure/compliant, and only a partial/brief listing description will appear on the View Item page for the listing, with a link to the full listing description that will load in another tab.   
  
If the listing description is not HTTPS compliant, the fix is to call **ReviseItem** or **ReviseFixedPriceItem** and update the **Item.Description** field, removing all links to HTTP pages.   
  
For more information about why eBay made this change, please see the [Policy Updates](http://pages.ebay.com/seller-center/seller-updates/2017-fall/policy-updates.html) page of the Fall 2017 Seller Updates page.   |  
|  ItemArray.Item.**ItemID**  | [ItemIDType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/ItemIDType.html) ([string](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string))  | Conditionally  |  The unique identifier of the eBay listing. This identifier is generated by eBay and returned in the response of an Add call if an item is successfully listed. Once an item is successfully created, the **ItemID** cannot be modified.   
  
**Note:** Although we represent item IDs as strings in the schema, we recommend you store them as 64-bit signed integers. If you choose to store item IDs as strings, allocate at least 19 characters (assuming decimal digits are used) to hold them. Your code should be prepared to handle IDs of up to 19 digits.    
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll. Also returned if DetailLevel is not provided on input.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Coarse, Fine, Medium.   |  
|  ItemArray.Item  
.**ItemPolicyViolation**  | [ItemPolicyViolationType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/ItemPolicyViolationType.html)  | Conditionally  |  Specifies the details of policy violations if the item was administratively canceled.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   |  
|  ItemArray.Item  
.ItemPolicyViolation.**PolicyID**  | [long](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#long)  | Conditionally  |  Policy ID of the violated policy which resulted in item being administratively canceled.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine.   |  
|  ItemArray.Item  
.ItemPolicyViolation  
.**PolicyText**  | [string](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string)  | Conditionally  |  Brief information of the violated policy which resulted in item being administratively canceled.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine.   |  
|  ItemArray.Item.**ListingDetails**  | [ListingDetailsType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/ListingDetailsType.html)  | Conditionally  |  Various details about a listing, some of which are calculated or derived after the item is listed. These include the start and end time, converted (localized) prices, and certain flags that indicate whether the seller specified fields whose values are not visible to the requesting user. For **GetMyeBayBuying** , returned as a self-closed element if no listings meet the request criteria.   
  
In an Add/Revise/Relist call, this container is used to set the Best Offer Auto-Accept and Best Offer Auto-Decline threshold values.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll. Also returned if DetailLevel is not provided on input.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Coarse, Fine, Medium.   |  
|  ItemArray.Item.ListingDetails  
.**Adult**  | [boolean](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean)  | Conditionally  |  If `true`, the item is listed in a Mature category. Users must accept the Mature Category agreement on the eBay site to retrieve items listed in Mature categories. (Users do not need to sign this agreement to be able to list items in Mature Categories.)   
**Note:** This field will stop being returned in **GetItemTransactions** and **GetSellerTransactions** on January 31, 2024.    
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine, Medium.   |  
|  ItemArray.Item.ListingDetails  
.**BestOfferAutoAcceptPrice**  |  [AmountType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/AmountType.html) ([double](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#double))  | Conditionally  |  The price at which Best Offers are automatically accepted. Similar in use to **MinimumBestOfferPrice**. If a buyer submits a Best Offer that is at or above this value, the offer is automatically accepted by the seller. This applies only to items listed in categories that support the **BestOfferAutoAcceptPrice** feature.   
  
For this setting to have an effect, the Best Offer feature must be enabled for the listing, and only the seller who listed the item will see **BestOfferAutoAcceptPrice** in a call response.   
  
**For Revise and Relist calls:** If a seller wanted to disable the Best Offer Auto-Accept and/or Best Offer Auto-Reject feature when revising or relisting an item, the full path to one or both of these two corresponding fields would be provided in a **DeletedField** tag, like the following:   

```
 Item.ListingDetails.BestOfferAutoAcceptPrice 
```
  
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   |  
| ItemArray.Item.ListingDetails  
.**BestOfferAutoAcceptPrice**  
[ attribute **currencyID** ]  | [CurrencyCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html)  | Conditionally  |  The price at which Best Offers are automatically accepted. Similar in use to **MinimumBestOfferPrice**. If a buyer submits a Best Offer that is at or above this value, the offer is automatically accepted by the seller. This applies only to items listed in categories that support the **BestOfferAutoAcceptPrice** feature.   
  
For this setting to have an effect, the Best Offer feature must be enabled for the listing, and only the seller who listed the item will see **BestOfferAutoAcceptPrice** in a call response.   
  
**For Revise and Relist calls:** If a seller wanted to disable the Best Offer Auto-Accept and/or Best Offer Auto-Reject feature when revising or relisting an item, the full path to one or both of these two corresponding fields would be provided in a **DeletedField** tag, like the following:   

```
 Item.ListingDetails.BestOfferAutoAcceptPrice 
```
  
  
For a list of possible enumeration values, see [CurrencyCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html).   |  
|  ItemArray.Item.ListingDetails  
.**BindingAuction**  | [boolean](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean)  | Conditionally  |  Applicable for Real Estate auctions only. If `true`, buyers and sellers are expected to follow through on the sale. If false, bids for the Real Estate auction are only expressions of interest.   
**Note:** This field will stop being returned in **GetItemTransactions** and **GetSellerTransactions** on January 31, 2024.    
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine, Medium.   |  
|  ItemArray.Item.ListingDetails  
.**CheckoutEnabled**  | [boolean](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean)  | Conditionally  |  Indicates whether or not the seller's Checkout Enabled preference is turned on.   
**Note:** A 'Checkout Enabled' setting is no longer available to sellers, and this field is always returned as `true`.  **Note:** This field will stop being returned in **GetItemTransactions** and **GetSellerTransactions** on January 31, 2024.    
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine, Medium.   |  
|  ItemArray.Item.ListingDetails  
.**ConvertedBuyItNowPrice**  |  [AmountType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/AmountType.html) ([double](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#double))  | Conditionally  |    
Converted value of the **BuyItNowPrice** in the currency of the site that returned this response. For active items, refresh this value every 24 hours to pick up the current conversion rates.   
**Note:** The **ListingDetails.ConvertedBuyItNowPrice** field will stop being returned in **GetItemTransactions** , **GetSellerTransactions** , and **GetMyeBaySelling** (SoldList and DeletedFromSoldList) on January 31, 2024.    
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine, Medium.   |  
| ItemArray.Item.ListingDetails  
.**ConvertedBuyItNowPrice**  
[ attribute **currencyID** ]  | [CurrencyCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html)  | Conditionally  |    
Converted value of the **BuyItNowPrice** in the currency of the site that returned this response. For active items, refresh this value every 24 hours to pick up the current conversion rates.   
**Note:** The **ListingDetails.ConvertedBuyItNowPrice** field will stop being returned in **GetItemTransactions** , **GetSellerTransactions** , and **GetMyeBaySelling** (SoldList and DeletedFromSoldList) on January 31, 2024.   
  
For a list of possible enumeration values, see [CurrencyCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html).   |  
|  ItemArray.Item.ListingDetails  
.**ConvertedReservePrice**  |  [AmountType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/AmountType.html) ([double](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#double))  | Conditionally  |    
Converted value of the **ReservePrice** in the currency of the site that returned this response. Only returned for listings with a reserve price when the requesting user is the listing's seller. For active items, refresh this value every 24 hours to pick up the current conversion rates. Not applicable to fixed-price listings.   
**Note:** The **ListingDetails.ConvertedReservePrice** field will stop being returned in **GetItemTransactions** , **GetSellerTransactions** , and **GetMyeBaySelling** (SoldList and DeletedFromSoldList) on January 31, 2024.    
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine.   |  
| ItemArray.Item.ListingDetails  
.**ConvertedReservePrice**  
[ attribute **currencyID** ]  | [CurrencyCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html)  | Conditionally  |    
Converted value of the **ReservePrice** in the currency of the site that returned this response. Only returned for listings with a reserve price when the requesting user is the listing's seller. For active items, refresh this value every 24 hours to pick up the current conversion rates. Not applicable to fixed-price listings.   
**Note:** The **ListingDetails.ConvertedReservePrice** field will stop being returned in **GetItemTransactions** , **GetSellerTransactions** , and **GetMyeBaySelling** (SoldList and DeletedFromSoldList) on January 31, 2024.   
  
For a list of possible enumeration values, see [CurrencyCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html).   |  
|  ItemArray.Item.ListingDetails  
.**ConvertedStartPrice**  |  [AmountType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/AmountType.html) ([double](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#double))  | Conditionally  |    
Converted value of the **StartPrice** in the currency of the site that returned this response. For active items, refresh this value every 24 hours to pick up the current conversion rates.  
  
In multi-variation listings, this value matches the lowest-priced variation that is still available for sale.   
**Note:** The **ListingDetails.ConvertedStartPrice** field will stop being returned in **GetItemTransactions** , **GetSellerTransactions** , and **GetMyeBaySelling** (SoldList and DeletedFromSoldList) on January 31, 2024.    
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine.   |  
| ItemArray.Item.ListingDetails  
.**ConvertedStartPrice**  
[ attribute **currencyID** ]  | [CurrencyCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html)  | Conditionally  |    
Converted value of the **StartPrice** in the currency of the site that returned this response. For active items, refresh this value every 24 hours to pick up the current conversion rates.  
  
In multi-variation listings, this value matches the lowest-priced variation that is still available for sale.   
**Note:** The **ListingDetails.ConvertedStartPrice** field will stop being returned in **GetItemTransactions** , **GetSellerTransactions** , and **GetMyeBaySelling** (SoldList and DeletedFromSoldList) on January 31, 2024.   
  
For a list of possible enumeration values, see [CurrencyCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html).   |  
|  ItemArray.Item.ListingDetails  
.**EndTime**  | [dateTime](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#dateTime)  | Conditionally  |  Time stamp (in GMT) when the listing is scheduled to end, or the actual end time if the item has ended.   
  
For auction listings that are eligible for extended bidding, this value reflects the effective current listing end time and may change if the listing close is extended. If an extension occurs, this value reflects the extended end time.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll. Also returned if DetailLevel is not provided on input.   |  
|  ItemArray.Item.ListingDetails  
.**HasPublicMessages**  | [boolean](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean)  | Conditionally  |  Indicates whether the item has any publicly displayed messages. Use **GetMemberMessages** to retrieve public messages for the item if this flag indicates that there are any.   
**Note:** The **HasPublicMessages** field will stop being returned in **GetItemTransactions** and **GetSellerTransactions** , on January 31, 2024.    
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   |  
|  ItemArray.Item.ListingDetails  
.**HasReservePrice**  | [boolean](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean)  | Conditionally  |  If `true`, the seller specified a value in **ReservePrice**.   
**Note:** This field will stop being returned in **GetItemTransactions** and **GetSellerTransactions** on January 31, 2024.    
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine, Medium.   |  
|  ItemArray.Item.ListingDetails  
.**HasUnansweredQuestions**  | [boolean](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean)  | Conditionally  |  Indicates whether the item has any unanswered questions. Use **GetMemberMessages** to retrieve unanswered questions for the item if this flag indicates that there are any.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   |  
|  ItemArray.Item.ListingDetails  
.**MinimumBestOfferPrice**  |  [AmountType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/AmountType.html) ([double](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#double))  | Conditionally  |  Specifies the minimum acceptable Best Offer price. If a buyer submits a Best Offer that is below this value, the offer is automatically declined. This applies only to items listed in categories that support the Best Offer auto-decline feature.   
  
In order for this setting to have an effect, Best Offer must be enabled for the listing, and this value will only be exposed to the seller who listed the item.   
  
**For Revise and Relist calls:** If a seller wanted to disable the Best Offer auto-accept and/or Best Offer auto-reject feature when revising or relisting an item, the full path to one or both of these two corresponding fields would be provided in a **DeletedField** tag, like the following:   

```
 Item.ListingDetails.MinimumBestOfferPrice 
```
  
**Note:** This field will stop being returned in **GetItemTransactions** and **GetSellerTransactions** on January 31, 2024.    
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   |  
| ItemArray.Item.ListingDetails  
.**MinimumBestOfferPrice**  
[ attribute **currencyID** ]  | [CurrencyCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html)  | Conditionally  |  Specifies the minimum acceptable Best Offer price. If a buyer submits a Best Offer that is below this value, the offer is automatically declined. This applies only to items listed in categories that support the Best Offer auto-decline feature.   
  
In order for this setting to have an effect, Best Offer must be enabled for the listing, and this value will only be exposed to the seller who listed the item.   
  
**For Revise and Relist calls:** If a seller wanted to disable the Best Offer auto-accept and/or Best Offer auto-reject feature when revising or relisting an item, the full path to one or both of these two corresponding fields would be provided in a **DeletedField** tag, like the following:   

```
 Item.ListingDetails.MinimumBestOfferPrice 
```
  
**Note:** This field will stop being returned in **GetItemTransactions** and **GetSellerTransactions** on January 31, 2024.   
  
For a list of possible enumeration values, see [CurrencyCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html).   |  
|  ItemArray.Item.ListingDetails  
.**RelistedItemID**  | [ItemIDType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/ItemIDType.html) ([string](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string))  | Conditionally  |  Indicates the new item ID for a re-listed item. When an item is re-listed, the item ID for the new item is added to the old listing, so buyers can navigate to the new listing. This value only appears when the old listing is retrieved. The **RelistedItemID** of the original item will reflect the last relist.   
**Note:** This field will stop being returned in **GetItemTransactions** and **GetSellerTransactions** on January 31, 2024.    
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   |  
|  ItemArray.Item.ListingDetails  
.**StartTime**  | [dateTime](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#dateTime)  | Conditionally  |  The **StartTime** value returned by non-search calls such as **GetItem** is the time stamp (in GMT) for when the item was listed.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll. Also returned if DetailLevel is not provided on input.   |  
|  ItemArray.Item.ListingDetails  
.**ViewItemURL**  | [anyURI](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#anyURI)  | Conditionally  |  The URL of the Web page where a user can view the listing. On the US site, this is called the View Item page. If you enabled affiliate tracking in a search-related call (for example, if you used the **AffiliateTrackingDetails** container in an applicable call), **ViewItemURL** contains a string that includes affiliate tracking information (see the [eBay Partner Network](https://www.ebaypartnernetwork.com)).   
**Note:** This field will stop being returned in **GetItemTransactions** and **GetSellerTransactions** on January 31, 2024.    
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   |  
|  ItemArray.Item.ListingDetails  
.**ViewItemURLForNaturalSearch**  | [anyURI](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#anyURI)  | Conditionally  |  This URL takes you to the same View Item page as ViewItemURL, but this URL is optimized to support natural search. That is, this URL is designed to make items on eBay easier to find via popular Internet search engines. The URL includes the item title along with other optimizations. To note, "?" (question mark) optimizes to "_W0QQ", "&" (ampersand) optimizes to "QQ", and "=" (equals sign) optimizes to "Z".   
  
If you are an eBay affiliate, use this URL to promote your affiliate information.   
  
**Note:** This URL may include additional query parameters that don't appear in **ViewItemURL** and vice versa. You should not modify the query syntax. For example, eBay won't recognize the URL if you change QQ to ?.  **Note:** This field will stop being returned in **GetItemTransactions** and **GetSellerTransactions** on January 31, 2024.    
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   |  
|  ItemArray.Item.**ListingDuration**  | [token](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#token)  | Conditionally  |  Describes the number of days the seller wants the listing to be active (available for bidding/buying). The duration specifies the seller's initial intent at listing time.   
  
The end time for a listing is calculated by adding the duration to the item's start time. If the listing ends early, the value of the listing duration does not change. When a listing's duration is changed, any related fees (e.g., 10-day fee) may be debited or credited (as applicable).   
  
The valid choice of values depends on the listing format (see **Item.ListingType**). For a list of valid listing-duration values for a specific leaf category, use the **Metadata API** [getListingTypePolicies](https://developer.ebay.com/api-docs/sell/metadata/resources/marketplace/methods/getListingTypePolicies) method and inspect the **listingTypePolicies.listingDurations** field for the returned category.   
  
When you revise a listing, the duration cannot be reduced if it will result in ending the listing within 24 hours of the current date-time. You are only allowed to increase the duration of the listing if fewer than 2 hours have passed since you initially listed the item and the listing has no bids. You can decrease the value of this field only if the listing has no bids (or no items have sold) and the listing does not end within 12 hours.   
  
**Note:** As of April 1, 2019, 'GTC' is the only supported listing duration for all eBay marketplaces with the following exceptions: 
  * The following eBay Motors US categories are exempt from this change: _Cars & Trucks_ (6001), _Motorcycles_ (6024), _Other Vehicles & Trailers_ (6038), _Boats_ (26429), _Powersports_ (66466).
  * All child categories under _Cars, Motorcycles & Vehicles_ (9800) categories on the eBay UK and eBay Italy sites are also exempt from this change. 

If any other listing duration value besides `GTC` is specified in this field, it will be ignored, and `GTC` will be used instead.    
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.  
  
**Applicable values** : See [ListingDurationCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/ListingDurationCodeType.html)  |  
|  ItemArray.Item  
.**ListingEnhancement**  | [ListingEnhancementsCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/ListingEnhancementsCodeType.html)  | Conditionally,   
[repeatable](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#repeatable): [0..*]  |  Describes listing upgrades that sellers can select for a fee, such as the **BoldTitle** upgrade.   
  
You can add a listing upgrade when you revise a listing, but you cannot remove a listing upgrade. When you relist an item, use **DeletedField** to remove a listing upgrade.   
  
**Applicable values** :   
  


BoldTitle
    (in/out) This value is used if the seller wants the listing title to be in boldface type. This feature will incur a listing fee. Note that this enhancement will not put the listing subtitle in boldface type (if a subtitle is used). 

CustomCode
    (in/out) Reserved for internal or future use.   
Code so that your app gracefully handles any future changes to this list.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   |  
|  ItemArray.Item.**ListingSubtype2**  | [ListingSubtypeCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/ListingSubtypeCodeType.html)  | Conditionally  |  Indicates a specific type of lead generation format listing, such as classified ad or local market best offer listing. Only applicable when **ListingType** = **LeadGeneration**.   
  
**Note:** **ListingSubtype2** replaces the deprecated **ListingSubtype** field. If both are specified in a request, **ListingSubtype2** takes precedence.    
  
**Applicable values** :   
  


ClassifiedAd
    (in/out) This value indicates that the lead generation listing is a classifed ad. Note that only some eBay categories support classified ad listings. To determine whether a specific leaf category on a specific eBay marketplace supports Classified Ad listings, use the **Metadata API** [getClassifiedAdPolicies](https://developer.ebay.com/api-docs/sell/metadata/resources/marketplace/methods/getClassifiedAdPolicies) method. Pass the target marketplace_id and the leaf category ID in the filter query parameter, and then inspect the **classifiedAdPolicies.adFormatEnabled** field for the returned category. 

CustomCode
    (in/out) Reserved for internal or future use 

LocalMarketBestOfferOnly
    (in/out) This value indicates that the lead generation listing is a US Motors Local Market listing. Note that only some eBay Motors categories support Motors Local Market listings. To determine whether a specific leaf category supports Motors Local Market Classified Ad listings, use the **Metadata API** [getMotorsListingPolicies](https://developer.ebay.com/api-docs/sell/metadata/resources/marketplace/methods/getMotorsListingPolicies) method. For eBay US Motors categories, specify **marketplace_id** as `EBAY_MOTORS_US`, pass the leaf category ID in the filter query parameter, and then inspect the **motorsListingPolicies.localMarketAdFormatEnabled** field for the returned category.   
Code so that your app gracefully handles any future changes to this list.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll. See:   
[About Local Market Listings](https://pages.ebay.com/help/sell/motors-selling-locally.html)   
[Advertising with Classified Ads](https://pages.ebay.com/help/sell/f-ad.html)  |  
|  ItemArray.Item.**ListingType**  | [ListingTypeCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/ListingTypeCodeType.html)  | Conditionally  |  The selling format of the eBay listing, such as auction (indicated with `Chinese` value), fixed-price (indicated with `FixedPriceItem` value), or classified ad (indicated with `AdType` value).   
  
If this field is not included in an **AddItem** , **AddItems** , or **VerifyAddItem** call, the listing type defaults to auction   
  
For **AddFixedPriceItem** , **RelistFixedPriceItem** , or **VerifyAddFixedPriceItem** call, this field must be included and set to `FixedPriceItem`, since these calls only work with fixed-price listings.   
  
This field is not applicable to Revise calls because the selling format of active listings cannot be changed.   
  
**Applicable values** :   
  


AdType
    (in/out) This enumeration value represents a classified ad in a Real Estate category. This listing type is only used to solicit inquiries from interested parties. To express interest, a buyer fills in a contact form that eBay forwards to the seller as a lead. This format does not enable buyers and sellers to transact online through eBay, and eBay Feedback is not available for ad format listings.   
<br>Because listing durations vary by marketplace and leaf category, use the **Metadata API** [getListingTypePolicies](https://developer.ebay.com/api-docs/sell/metadata/resources/marketplace/methods/getListingTypePolicies) method for the target marketplace and category. Inspect the listingTypePolicies.listingDurations array in the response and look for the entry whose **listingType** value is `AD_TYPE` to see the supported durationValues for real estate classified ad listings. 

Chinese
    (in/out) This value indicates an auction listing. In an auction listing, prospective buyers engage in a competitive bidding process, although Buy It Now may be offered as long as no bids have been placed. Auctions occur on the eBay marketplace site, and the auction listings will also appear in the seller's eBay Store (if the seller has an eBay Store).   
  
Because listing durations vary by marketplace and leaf category, use the **Metadata API** [getListingTypePolicies](https://developer.ebay.com/api-docs/sell/metadata/resources/marketplace/methods/getListingTypePolicies) method for the target marketplace and category. Inspect the **listingTypePolicies.listingDurations** array in the response and look for the entry whose **listingType** value is `AUCTION` to see the supported **durationValues** for auction listings. 

CustomCode
    (in/out) Reserved for internal or future use. 

FixedPriceItem
    (in/out) With this listing format, the selling is offering the item at a fixed price, although it is still possible for the seller to negotiate the price with prospective buyers using the Best Offer feature. A fixed-price listing can offer a single item, or if the seller has multiple quantity of the same item, multiple quantity of that same item can be made available for sale through the same listing. Additionally, the seller can set up a multiple-variation, fixed-price listing, where similar items can be sold through the same listing. An example of a multiple-variation, fixed-price listing might be a t-shirt (or another article of clothing) that is available in multiple color and size combinations.   
  
Traditionally, listing durations for fixed-prices listings have varied by eBay marketplace and category. Typical listing durations for fixed-price listings ranged from three to 30 days, or GTC (Good 'Til Cancelled). As of April 1, 2019, 'GTC' is the only supported listing duration for all eBay marketplaces with the following exceptions: 
  * The following eBay Motors US categories are exempt from this change: _Cars & Trucks_ (6001), _Motorcycles_ (6024), _Other Vehicles & Trailers_ (6038), _Boats_ (26429), _Powersports_ (66466).
  * All child categories under _Cars, Motorcycles & Vehicles_ (9800) categories on the eBay UK and eBay Italy sites are also exempt from this change. 

  
With the 'GTC' listing duration, the listing will remain active as long as the listing shows that inventory is available for purchase (available quantity is '1' or more). For sellers listing motor vehicles on the eBay US Motors, eBay UK, or eBay Italy sites, to retrieve the supported listing durations for a fixed-price listing in a specific leaf category and marketplace, use the **Metadata API** [getListingTypePolicies](https://developer.ebay.com/api-docs/sell/metadata/resources/marketplace/methods/getListingTypePolicies) method. Inspect the **listingTypePolicies.listingDurations** array in the response and look for the entry whose **listingType** value is `FIXED_PRICE_ITEM` to see the supported **durationValues** for that category.   
  
**Note:** As long as a fixed-price listing has inventory available, or if the out-of-stock control feature is being used, GTC listings are automatically renewed each month according to the calendar day.  

LeadGeneration
    (in/out) This enumeration value represents a (non-Real Estate) classified ad listing. The `AdType` enumeration value represents Real Estate classified ads. This listing type is only used to solicit inquiries from interested parties. To express interest, a buyer fills in a contact form that eBay forwards to the seller as a lead. This format does not enable buyers and sellers to transact online through eBay, and eBay Feedback is not available for ad format listings. Non-Real Estate classified ads are only available in a limited number of eBay categories, including Business and Industrial categories, Travel, ans Specialty Services.   
  
Because listing durations vary by marketplace and leaf category, use the **Metadata API** [getListingTypePolicies](https://developer.ebay.com/api-docs/sell/metadata/resources/marketplace/methods/getListingTypePolicies) method for the target marketplace and category. Inspect the **listingTypePolicies.listingDurations** array in the response and look for the entry whose **listingType** value is `LEAD_GENERATION` to see the supported **durationValues** for non-Real Estate classified ad listings.   
(Not all values in [ListingTypeCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/ListingTypeCodeType.html) apply to this field.)  
  
Code so that your app gracefully handles any future changes to this list.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll. See [Listing types](https://developer.ebay.com/api-docs/user-guides/static/trading-user-guide/listing-types.html).  |  
|  ItemArray.Item.**Location**  | [string](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string)  | Conditionally  |  Indicates the geographical location of the item (along with the value in the **Country** field). When you revise a listing, you can add or change this value only if the listing has no bids (or no items have sold) and it does not end within 12 hours.   
  
If you do not specify **Location** , you must specify **Item.PostalCode**. If you specify a postal code, but do not specify a location, then the location is given a default value derived from the postal code.   
  
**For GetOrders, GetItemTransactions, GetSellerTransactions:** If the item is shipped from a fulfillment center location through the Multi-Warehouse Program, this field will return the location details (including the country and zip code) of the fulfillment center closest to the buyer.   
  
**For Revise/Relist calls:** When updating an **Item.Location** , you must also include the **Item.PostalCode** corresponding to the **Item.Location** in the revise/relist call; otherwise, the location will not be updated.   
  
**Note:** For the Classified Ad format for motors vehicle listings, the value provided in the **Location** field is used as item location only if the **SellerContactDetails.Street** and the **SellerContactDetails.Street2** are empty. Else, the **SellerContactDetails.Street** and the **SellerContactDetails.Street2** will be used for item location.    
  
**Max length:** 200.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Coarse, Fine, Medium.   |  
|  ItemArray.Item.**PaymentMethods**  | [BuyerPaymentMethodCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/BuyerPaymentMethodCodeType.html)  | Conditionally,   
[repeatable](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#repeatable): [0..*]  |  **For Add/Revise/Relist calls** : A **PaymentMethods** field is required for each offline payment method supported by the seller for the listing.   
**Note:** Sellers no longer have to specify any electronic payment methods for listings, so one or more **PaymentMethods** fields will only be needed for listings that require/support payments off of eBay's platform. If an electronic payment is supplied in a **PaymentMethods** field, a warning will be triggered and the payment method will be dropped.  **Note:** If you are already referencing a payments business policy in an Add/Revise/Relist call with the **SellerProfiles.SellerPaymentProfile** container, no **PaymentMethods** fields will be needed, as these settings will already be set in the payments business policy.  Payment methods are not applicable to any classified ad listings, as any agreement and payment is handled off of the eBay platform.   
  
**For Get calls that return**PaymentMethods** fields **: One or more **PaymentMethods** fields will only be returned if the seller set one or more offline payment methods for the listing.   
**Note:** This field will stop being returned in order management calls on January 31, 2024.    
  
**Applicable values** :   
  


CashOnPickup
    (in/out) This enumeration value indicates that cash on pickup is accepted for payment. This value is only applicable for offline payments.   
**Note:** To see whether this payment method is supported for a category, call [getCategoryPolicies](https://developer.ebay.com/api-docs/sell/metadata/resources/marketplace/methods/getCategoryPolicies) and inspect the **paymentMethods** field.  

COD
    (in/out) This enumeration value indicates that a COD (Cash On Delivery) is accepted for payment. This value is only applicable for offline payments and is not supported on all marketplaces.   
**Note:** To see whether this payment method is supported for a category, call [getCategoryPolicies](https://developer.ebay.com/api-docs/sell/metadata/resources/marketplace/methods/getCategoryPolicies) and inspect the **paymentMethods** field.  

CustomCode
    (in/out) Reserved for internal or future use. 

MOCC
    (in/out) This enumeration value indicates that a money order or cashiers check is accepted for payment. This value is only applicable for offline payments and is not supported on all marketplaces.   
**Note:** To see whether this payment method is supported for a category, call [getCategoryPolicies](https://developer.ebay.com/api-docs/sell/metadata/resources/marketplace/methods/getCategoryPolicies) and inspect the **paymentMethods** field.  

PersonalCheck
    (in/out) This enumeration value indicates that a personal check is accepted for payment. This value is only applicable for offline payments and is not supported on all marketplaces.   
**Note:** To see whether this payment method is supported for a category, call [getCategoryPolicies](https://developer.ebay.com/api-docs/sell/metadata/resources/marketplace/methods/getCategoryPolicies) and inspect the **paymentMethods** field.    
(Not all values in [BuyerPaymentMethodCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/BuyerPaymentMethodCodeType.html) apply to this field.)  
  
Code so that your app gracefully handles any future changes to this list.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine.   |  
|  ItemArray.Item  
.**PickupInStoreDetails**  | [PickupInStoreDetailsType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/PickupInStoreDetailsType.html)  | Conditionally  |  **Note:** BOPIS (Buy Online, Pick Up In Store) is no longer supported. This container remains relevant for Click and Collect-related fields in the Trading API.   |  
|  ItemArray.Item  
.PickupInStoreDetails  
.**EligibleForPickupDropOff**  | [boolean](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean)  | Conditionally  |  For sellers opted in to Click and Collect, this field was once used to set Click and Collect eligibility at the listing level. However, now the seller can only opt in to Click and Collect at the account level, and then each of their listings will be automatically evaluated by eBay for Click and Collect eligibility.   
  
**Note:** Until this field is fully deprecated in the Trading WSDL (and in Add/Revise/Relist/Verify calls), it can still be used, but it will have no functional affect. However, if set in an Add/Revise/Relist/Verify call, it will get returned in **GetItem** , but it won't be a true indicator if the item is actually available for the Click and Collect fulfillment method. Instead, the **Item.AvailableForPickupDropOff** field should be referenced to see if the listing actually has inventory that is available for pickup via the Click and Collect fulfillment method.   |  
|  ItemArray.Item  
.PickupInStoreDetails  
.**EligibleForPickupInStore**  | [boolean](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean)  | Conditionally  |  **Note:** BOPIS (Buy Online, Pick Up In Store) is no longer supported. This field is deprecated and should no longer be used.   |  
|  ItemArray.Item.**PictureDetails**  | [PictureDetailsType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/PictureDetailsType.html)  | Conditionally  |  This container consists of the data associated with photos within the listing. Sellers can have up to 24 pictures in almost any category at no cost. Motor vehicle listings are an exception. The number of included pictures in motor vehicle listings depend on the selected vehicle package (see [Fees for selling vehicles on eBay Motors](https://www.ebay.com/help/selling/fees-credits-invoices/motors-fees?id=4127)). These photos can be hosted by eBay Picture Services (EPS), or the seller can host pictures on a non-eBay server. If pictures are externally-hosted, they must be hosted on a site that is using the 'https' protocol.   
  
It is required that all listings have at least one picture.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll. Also returned if DetailLevel is not provided on input. See:   
[Add pictures](https://developer.ebay.com/api-docs/user-guides/static/trading-user-guide/pictures.html)   
[Adding photos to your listing](https://pages.ebay.com/help/sell/pictures.html)  |  
|  ItemArray.Item.PictureDetails  
.**GalleryType**  | [GalleryTypeCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/GalleryTypeCodeType.html)  | Conditionally  |  This field is used to specify the type of picture gallery to use for the listing. If this field is omitted, a standard picture gallery is used for the listing. There is no listing fee for a standard picture gallery.   
  
To use the Gallery Plus feature, you must include this field and set its value to `Plus`.   
  
The Gallery image will be the first URL passed into the first **PictureURL** field, so if you want a specific picture to be the Gallery image, you should make sure you pass the URL for this picture in the first **PictureURL** field.   
  
When revising a listing, if you disable the Gallery Plus feature by including the **GalleryType** field and setting its value to `Gallery`, the original feature fee for this feature will not be credited to the seller.   
  
  
**Applicable values** :   
  


CustomCode
    (in/out) Reserved for internal use **only**. 

Gallery
    (in/out) This feature, which is free on all sites, adds a Gallery image in the search results. A Gallery image is an image that was uploaded and copied to EPS (eBay Picture Service). This copy is stored for 30 days or until the image is associated with a listing. Once the image is associated with a listing, the period is extended to 90 days after the item's sale_end date and is extended again if the item is relisted or used in subsequent listings. As part of storing a copy, EPS also makes additional sizes available (thumbnail, main image, supersize, popup, etc.), which are used by the various Gallery enhancements.   
  
All images must comply to the [Picture Requirements.](https://developer.ebay.com/api-docs/user-guides/static/trading-user-guide/pictures.html) 

None
    (in/out) Gallery is supported free on all sites. So this field is useful only for removing an existing feature setting when using **RelistItem**. 

Plus
    (in/out) Adds a Gallery Plus icon to the listing.   
  
When Plus is selected in a request that specifies at least two images (using ItemType.PictureDetailsType.PictureURL), the Gallery Plus feature automatically includes a Gallery Showcase of all the listing's images.   
  
The Gallery Showcase displays when hovering over or clicking on the listing's Gallery Plus icon in the search results. The Showcase window displays a large (400px x 400px) preview image which is first image specified PictureURL, as well as up to 11 (64 px x 64 px) selectable thumbnails for the remaining EPS images. Clicking on the preview image displays the item's listing page.   
  
If Plus is selected and the request includes only one EPS image or any self-hosted images, the listing includes a Gallery Plus icon that, when hovered over or clicked, displays a large (400px x 400px) preview image of the item. Clicking the image displays the View Item page for that listing.   
  
When using RelistItem or ReviseItem (item has no bids and more than 12 hours before the listing's end), Plus can be unselected in the request. However, the Plus fee will still apply if a previous request selected Plus. There is at most one Plus fee per listing.   
  
When "Plus" is included in an item listing, the listing also automatically gets the Gallery functionality at no extra cost. "Gallery" does not need to be specified separately in the listing.   
  
Listing images that are originally smaller than 400px x 400px are centered in the preview frame. Images that are originally larger than 400px x 400px are scaled down to 400px on their longest side (maintaining their original aspect ratio).   
Code so that your app gracefully handles any future changes to this list.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll. Also returned if DetailLevel is not provided on input.   |  
|  ItemArray.Item.**PrimaryCategory**  | [CategoryType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CategoryType.html)  | Conditionally  |  Use this container to set the primary listing category. The **PrimaryCategory.CategoryID** must be a valid leaf category on the category tree for the request site (`X-EBAY-API-SITEID` / listing **Item.Site**). A category ID that is valid only on another site's tree is rejected. This field is conditionally required in an Add call unless the seller successfully uses the **ProductListingDetails** container to find an eBay catalog product match. When the seller successfully uses an eBay catalog product to create a listing, the listing title, listing description, Item Specifics, listing category, and stock photo defined in the catalog product is used to create the listing.  
  
Once you determine the appropriate eBay category for your product, use the applicable **Sell Metadata API** method for the specific category-level feature you want to verify. To discover required, recommended, and optional Item Specifics for a category, use the [getItemAspectsForCategory](https://developer.ebay.com/api-docs/commerce/taxonomy/resources/category_tree/methods/getItemAspectsForCategory) method of the Taxonomy API.   
  
If you do use an eBay catalog product, it is advised that you do not include this field, as any primary category ID you specify in this field may get dropped if this category is different than the primary category defined in the eBay catalog product.   
  
**For ReviseItem only:** When revising a listing, you can change the primary category only if an auction listing has no bids or a multiple-quantity, fixed-price listing has no sales, and the listing does not end within 12 hours. If you change the listing category, any Item Specifics that were previously specified may be dropped from the listing if they aren't valid for the new category.   
  
When you list an event ticket on the US site, you must specify one of the leaf categories under the Tickets & Experiences meta category.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Coarse, Fine, Medium. See:   
[Applying Categories](https://developer.ebay.com/api-docs/user-guides/static/trading-user-guide/categories.html)   
[Maintaining Category Data](https://developer.ebay.com/api-docs/user-guides/static/trading-user-guide/categories.html)  |  
|  ItemArray.Item.PrimaryCategory  
.**CategoryID**  | [string](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string)  | Conditionally  |  This string value is the unique identifier of an eBay category. For listing calls, this ID must be a valid leaf on the category tree for the listing site. Validate against that marketplace's Taxonomy tree (for example, [getCategorySubtree](https://developer.ebay.com/api-docs/commerce/taxonomy/resources/category_tree/methods/getCategorySubtree) on tree 100 for eBay Motors). In **GetItem** and related calls, see the **CategoryName** field for the text name of the category. The parent category of this eBay category can be retrieved through the [Taxonomy API's](https://developer.ebay.com/api-docs/commerce/taxonomy/resources/methods) **getCategoryTree** or **getCategorySubtree** methods and inspecting the **parentCategoryTreeNodeHref** field in the response.   
**Note:** When listing in categoryID 173651 (Auto Performance Tuning Devices & Software), use of catalog products is required. For more information, see [Tuning devices and software](https://developer.ebay.com/api-docs/user-guides/static/trading-user-guide/tuning-devices-and-software.html).  In an Add call, the **PrimaryCategory.CategoryID** is conditionally required unless the seller successfully uses the **ProductListingDetails** container to find an eBay catalog product match. When the seller successfully uses an eBay catalog product to create a listing, the listing title, listing description, item specifics, listing category, and stock photo defined in the catalog product is used to create the listing.   
  
In an Add/Revise/Relist call, the **SecondaryCategory.CategoryID** is conditionally required if a Secondary Category is used. Using a Secondary Category can incur a listing fee. The secondary category ID must be a valid leaf category on the category tree for the listing site; an ID valid only on another marketplace tree is rejected. Validate against that marketplace's Taxonomy tree (for example, [getCategorySubtree](https://developer.ebay.com/api-docs/commerce/taxonomy/resources/category_tree/methods/getCategorySubtree) on tree 100 for eBay Motors).   
  
**For ReviseItem only:** Previously, removing the listing from a secondary category was only possible within 12 hours of the listing's scheduled end time when an auction listing had no active bids or a multiple-quantity, fixed-price listing had no items sold, but this restriction no longer exists. Now, the secondary category can be dropped for any active listing at any time, regardless of whether an auction listing has bids or a fixed-price listing has sales. To drop a secondary category, the seller passes in a value of `0` in the **SecondaryCategory.CategoryID** field.   
  
**Max length:** 10.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   |  
|  ItemArray.Item.PrimaryCategory  
.**CategoryName**  | [string](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string)  | Conditionally  |  This string value is the display name of the eBay primary category, as it would appear on the eBay site. In **GetItem** , this will be a fully-qualified category name (e.g., Collectibles:Decorative Collectibles:Hummel, Goebel).   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   |  
|  ItemArray.Item.**PrivateListing**  | [boolean](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean)  | Conditionally  |  A `true` value in this field indicates that the listing is private. Sellers may want to use this option when they believe that a listing's potential bidders/buyers would not want their obfuscated user IDs (and feedback scores) exposed to other users.   
  
**For ReviseItem/ReviseFixedPriceItem** : The seller will not be able change this setting if the listing has any pending bids, any pending best offers, previous sales (for multiple-quantity, fixed-price listing), or if the listing will end within 12 hours.   
  
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   |  
|  ItemArray.Item.**ProxyItem**  | [boolean](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean)  | Conditionally  |  Some listings on the eBay platform originate from eBay affiliates. Depending on the relationship the affiliate has with eBay, there are times when the affiliate retains ownership of the listing. When this occurs the representation of the listing on eBay is considered a proxy item. Proxy items can only be edited using API requests from the applications that originally listed them.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Coarse, Fine, Medium.   |  
|  ItemArray.Item.**Quantity**  | [int](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#int)  | Conditionally  |  **For**AddItem** family of calls:** The **Quantity** value for auction listings must always be `1`. For a fixed-price listing, the **Quantity** value indicates the number of identical items the seller has available for sale in the listing. If this field is not included when creating a new fixed-price listing, quantity defaults to '1'. If variations are specified in **AddFixedPriceItem** or **VerifyAddFixedPriceItem** , the **Item.Quantity** is not required since the quantity of variations is specified in **Variation.Quantity** instead. See the [Creating a listing with variations](https://pages.ebay.com/help/sell/listing-variations.html) eBay Help page for more information on variations.   
  
**For ReviseItem and ReviseFixedPriceItem:** This value can only be changed for a fixed-price listing with no variations. The quantity of variations is controlled in the **Variation.Quantity** field and the **Item.Quantity** value for an auction listing should always be `1`.   
  
**For RelistItem and RelistFixedPriceItem:** Like most fields, when you use **RelistItem** or **RelistFixedPriceItem** , **Quantity** retains its original value unless you specifically change it. This means that the item is relisted with the value that was already in **Quantity** , not with the remaining quantity available. For example, if the original **Quantity** value was `10`, and three items have been sold, eBay sets the relisted item's **Quantity** to `10` by default, and not `7`. So, we strongly recommend that you always set **Quantity** to the correct value (your actual quantity available) in your relist requests.  
  
When eBay auto-renews a GTC listing (**ListingDuration** = **GTC**) on your behalf, eBay relists with correct quantity available.   
  
**For GetSellerEvents:** **Quantity** is only returned for listings where item quantity is greater than 1.   
  
**For GetItem and related calls:** This is the total of the number of items available for sale plus the quantity already sold. To determine the number of items available, subtract **SellingStatus.QuantitySold** from this value.   
  
**For order line item calls with variations:** In **GetItemTransactions** , **Item.Quantity** is the same as **GetItem** (the total quantity across all variations). In **GetSellerTransactions** , **Transaction.Item.Quantity** is the total quantity of the applicable variation (quantity available plus quantity sold).   
  
**Note:** For the US site, new eBay sellers are subject to [Seller Limits](https://developer.ebay.com/api-docs/user-guides/static/make-a-call/fg-replaced.html), which limit the quantity of items that may be listed and/or the total cumulative value of these listings. While subject to these selling limits, an eBay seller can use the **GetMyeBaySelling** call to retrieve both the remaining number of listings they can create and the remaining cumulative value of these listings. These values are shown in the **Summary.QuantityLimitRemaining** and **Summary.AmountLimitRemaining** fields in the **GetMyeBaySelling** response. If a call to add an item or revise an item would result in the exceeding of these limits, the add item or revise item call will fail. These fields will only be returned if the seller is subject to seller limits.    
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Coarse, Fine, Medium.   |  
|  ItemArray.Item  
.**QuantityAvailableHint**  | [QuantityAvailableHintCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/QuantityAvailableHintCodeType.html)  | Conditionally  |  Indicates the type of message that will be returned describing the quantity available for the item.   
  
**Applicable values** :   
  


CustomCode
    (out) Reserved for internal or future use. 

Limited
    (out) The message "Limited quantity available" is shown in the web flow (e.g., for a flash sale or a Daily Deal). 

MoreThan
    (out) The message "More than 10 available" is shown in the web flow. 10 is the value of QuantityThreshold tag based on the seller's preference.   
Code so that your app gracefully handles any future changes to this list.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Coarse, Fine, Medium.   |  
|  ItemArray.Item  
.**QuantityThreshold**  | [int](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#int)  | Conditionally  |  The quantity threshold above which the seller prefers not to show the actual quantity available. Returned when the quantity available is greater than the value of quantity threshold. Currently, 10 is the only available value for this threshold.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Coarse, Fine, Medium.   |  
|  ItemArray.Item  
.**ReasonHideFromSearch**  | [ReasonHideFromSearchCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/ReasonHideFromSearchCodeType.html)  | Conditionally  |  This field is returned only when the listing is currently being hidden from any searches occurring on eBay. Listings may be hidden from search if an active listing is currently out of stock or if the listing has been determined by eBay to be a duplicate listing.   
  
**Applicable values** :   
  


DuplicateListing
    (out) This value indicates that the listing is being hidden from search on the eBay site because the listing has been determined by eBay to be a duplicate listing.   
  
This enumeration value is associated with eBay Duplicate Listings Policy, which is applicable on the US, CA, CA-FR, and eBay Motors (Parts and Accessories only) sites. Event Tickets, Real Estate, and Motor Vehicle categories are excluded from this policy. For more information, read [eBay's Duplicate Listings Policy](http://pages.ebay.com/help/policies/listing-multi.html) help page. 

OutOfStock
    (out) This value indicates that the listing is currently hidden from search because the quantity in the listing is zero. However, the listing is still alive and will reappear in the search results when the quantity is set to something greater than zero. The 'Out-of-stock' option is set by the seller at the account level. This option can be enabled in My eBay Site Preferences, or the seller can use the [OutOfStockControlPreference](https://developer.ebay.com/DevZone/XML/docs/Reference/ebay/SetUserPreferences.html#Request.OutOfStockControlPreference) field in the **SetUserPreferences** call.   
Code so that your app gracefully handles any future changes to this list.   |  
|  ItemArray.Item.**ReservePrice**  |  [AmountType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/AmountType.html) ([double](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#double))  | Conditionally  |  This field is used to set the lowest price at which the seller is willing to sell an auction item. The **StartPrice** value must be lower than the **ReservePrice** value. Note that setting a reserve price will incur a listing fee of $5 or 7.5% of the reserve price, whichever is greater, and this fee is charged regardless of whether or not the auction item has a qualifying, winning bidder.   
  
As long as no bidder has matched your reserve price, and the scheduled end time of the auction is 12 or more hours away, you can lower or remove the reserve price. However, even if you remove the reserve price from an active listing, you will still be charged the fee and not eligible for a credit.   
  
In 'get' calls that retrieve item data, the **ReservePrice** field will only be returned to the seller of that particular auction item, and only if a reserve price has been set up. The reserve price is never exposed to anyone other than the seller of the item.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine. See:   
[Revise a US eBay motors listing](https://developer.ebay.com/api-docs/user-guides/static/trading-user-guide/ebay-motors-revise-listing.html)   
[Setting a reserve price (eBay help topic)](https://www.ebay.com/help/selling/listings/selling-auctions/reserve-prices?id=4143)   
[Fees for optional listing upgrades (eBay help topic)](https://www.ebay.com/help/selling/fees-credits-invoices/selling-fees?id=4822#section5)  |  
| ItemArray.Item.**ReservePrice**  
[ attribute **currencyID** ]  | [CurrencyCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html)  | Conditionally  |  This field is used to set the lowest price at which the seller is willing to sell an auction item. The **StartPrice** value must be lower than the **ReservePrice** value. Note that setting a reserve price will incur a listing fee of $5 or 7.5% of the reserve price, whichever is greater, and this fee is charged regardless of whether or not the auction item has a qualifying, winning bidder.   
  
As long as no bidder has matched your reserve price, and the scheduled end time of the auction is 12 or more hours away, you can lower or remove the reserve price. However, even if you remove the reserve price from an active listing, you will still be charged the fee and not eligible for a credit.   
  
In 'get' calls that retrieve item data, the **ReservePrice** field will only be returned to the seller of that particular auction item, and only if a reserve price has been set up. The reserve price is never exposed to anyone other than the seller of the item.  
  
For a list of possible enumeration values, see [CurrencyCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html).   |  
|  ItemArray.Item.**ReturnPolicy**  | [ReturnPolicyType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/ReturnPolicyType.html)  | Conditionally  |  Describes the seller's return policy. Most categories on most eBay sites require the seller to clearly specify whether or not returns are accepted (see **ReturnsAcceptedOption**).   
**Note:** As a part of Digital Services Act (DSA) requirements, as of April 3, 2023, buyers in the EU must be allowed to return an item within 14 days or more, unless the item is exempt. Where applicable, sellers should update their return policies to reflect this requirement of accepting returns from EU buyers. This update can be made through the **ReturnPolicy** container or through a return business policy that is referenced through the **SellerProfiles.SellerReturnProfile** container.   
**Note:** If you are using a return business policy set up through My eBay or via the [Account API](https://developer.ebay.com/api-docs/sell/account/resources/return_policy/methods/createReturnPolicy), then you should not populate the fields in this **ReturnPolicy** container. Instead, indicate your return policy using the **SellerProfiles.SellerReturnProfile** container.   
  
However, if you _do not_ configure a return policy, all the fields in this **ReturnPolicy** container that are marked **conditional** must be populated in your request.    
**For the**AddItem** family of calls:** Required for most categories on most sites. To determine whether return policy metadata is required for a specific leaf category, use the **Metadata API** [getReturnPolicies](https://developer.ebay.com/api-docs/sell/metadata/resources/marketplace/methods/getReturnPolicies) method and inspect the [required](https://developer.ebay.com/develop/api/sell/metadata_api#sell-metadata_api-marketplace-getreturnpolicies.returnpolicy.required) boolean field. Use the returned category-level domestic and international return policy metadata from **getReturnPolicies** to determine which **ReturnPolicy** fields and values are supported for the applicable leaf category.   
  
Australia (AU) and US eBay Motors Parts and Accessories categories typically support but do not require a return policy. (However, we strongly recommend that you specify a clear return policy whenever possible.)  
  
**For ReviseItem only:** If the listing has bids or sales and it ends within 12 hours, you can't change the return policy details. If the listing is a GTC listing that has sales or ends within 12 hours (one or the other, but not both), you can add a return policy to the GTC listing (but you can't change return policy details if already present). If the listing has no bids or sales and more than 12 hours remain before the listing ends, you can add or change the return policy. When you revise your return policy, you only need to specify the fields you want to add or change. You don't need to specify all the other **ReturnPolicy** fields again. The other fields will retain their existing settings.  
  
**For the GetItem family of calls:** Only returned if the site you sent the request to supports the seller's return policy. Typically, the return policy details are only returned when the request is sent to the listing site.   
  
**Note:** For category-level domestic and international return-policy metadata, use the **Metadata API** [getReturnPolicies](https://developer.ebay.com/api-docs/sell/metadata/resources/marketplace/methods/getReturnPolicies) method instead of GeteBayDetails.   
**Note:** In May 2018, eBay added the ability to create a separate international return policy for items that are shipped to international customers. If a seller does not add a separate international return policy, the settings in the domestic return policy will be used instead for international returns. For more information on setting separate domestic and international return policies, see the [International returns policy](https://pages.ebay.com/seller-center/seller-updates/2018-summer/simplified-returns.html#international-returns-policy) help topic. For the international equivalent of this field, see the **InternationalRefundMethodValues** field.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Coarse, Fine, Medium. See [Specify a return policy](https://developer.ebay.com/api-docs/user-guides/static/trading-user-guide/specify-return-policy.html).  |  
|  ItemArray.Item.ReturnPolicy  
.**Description**  | [string](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string)  | Conditionally  |  This field contains the seller's detailed explanation for their return policy and is displayed in the Return Policy section of the View Item page. This field is valid in only the following marketplaces (the field is otherwise ignored): 
  * Germany (DE)
  * Austria (AT)
  * France (FR)
  * Italy (IT)
  * Spain (ES)

Where valid, sellers can use this field to add details about their return policies. eBay uses this text string as-is in the additional details section of the View Item page. Avoid HTML and avoid character entity references (such as &pound; or &#163;). If you include special characters in the return policy description, use the literal UTF-8 or ISO-8559-1 character (e.g. £).    
  
**For AddItem, VerifyAddItem, and RelistItem:** If the seller accepts returns (**ReturnsAcceptedOption** = `ReturnsAccepted`) but does not specify this field when listing the item, **GetItem** returns this as an empty node.   
  
**For ReviseItem only:** You cannot change the value of this field if the listing has bids or sales, or if the listing ends within 12 hours. For more details, see the **ReturnPolicy** description.   
  
**Max length:** 8000 (for DE, AT); 5000 (for FR, IT, ES).   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Coarse, Fine, Medium.   |  
|  ItemArray.Item.ReturnPolicy  
.**InternationalRefundOption**  | [token](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#token)  | Conditionally  |  This field indicates how the seller compensates international buyers for returns. `MoneyBack` is the only supported value for all marketplaces except for the US. On the US marketplace, you can set this value to either `MoneyBack` or `MoneyBackOrReplacement`. `MoneyBackOrReplacement` can be used by sellers that have the depth of inventory to support an exchange for an identical item. However, ultimately, it is up to the buyer on whether they want money back or a replacement item.   
  
**For ReviseItem only:** You cannot change the value of this field if the listing has bids or sales, or if the listing ends within 12 hours. For more details, see the **ReturnPolicy** description.   
  
**Note:** If a seller does not add a separate international return policy, the settings in the domestic return policy will be used instead. So if this field is not used in an add/revise/relist call, the refund option(s) for international returns will default to the value specified in the **RefundOption** field.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Coarse, Fine, Medium. See [International Refund Methods (in getReturnPolicies)](https://developer.ebay.com/api-docs/sell/metadata/resources/marketplace/methods/getReturnPolicies) for supported international refund methods for each marketplace and category.   
  
**Applicable values** : See [RefundOptionsCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/RefundOptionsCodeType.html)  |  
|  ItemArray.Item.ReturnPolicy  
.**InternationalReturnsAcceptedOption**  | [token](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#token)  | Conditionally  |  This field is conditionally required if a seller wants to use a separate return policy for international returns. The value in this field indicates whether or not the seller accepts returns from international buyers.   
  
Applicable values are `ReturnsAccepted` or `ReturnsNotAccepted`. When set to `ReturnsAccepted`, this option indicates the seller allows international buyers to return items. Specify **ReturnsNotAccepted** for a listing if returns are not accepted from international buyers.   
  
On the eBay DE, IE, and UK, registered business sellers must accept returns for fixed-price items (including auction items with Buy It Now and any other fixed price formats) when the category requires a return policy. On some European sites, such as eBay Germany (DE), registered business sellers are required to accept returns. Use the Trading call **GetUser** to determine the status of an eBay business seller in DE, IE, and UK. Review the **User.SellerInfo.SellerBusinessType** field in the response.   
  
**For ReviseItem only:** You cannot change the value of this field if the listing has bids or sales, or if the listing ends within 12 hours. For more details, see the **ReturnPolicy** description.   
  
**Note:** If a seller does not add a separate international return policy, the settings in the domestic return policy will be used instead. So if this field is not used in an add/revise/relist call, the return accepted value for international returns will default to the value specified in the **ReturnsAcceptedOption** field.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Coarse, Fine, Medium. See [International Returns Accepted Values (in getReturnPolicies)](https://developer.ebay.com/api-docs/sell/metadata/resources/marketplace/methods/getReturnPolicies) for supported international returns accepted values for each marketplace and category.   
  
**Applicable values** : See [ReturnsAcceptedOptionsCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/ReturnsAcceptedOptionsCodeType.html)  |  
|  ItemArray.Item.ReturnPolicy  
.**InternationalReturnsWithinOption**  | [token](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#token)  | Conditionally  |  This field is conditionally required if a seller is using a separate return policy for international returns, and is accepting international returns. The value in this field indicates the number of days that an international buyer has to return an item. The time period begins on the day that the buyer receives the item. Most marketplaces and categories support 30-day and 60-day return periods. eBay sites often set 30-days as the default value for this field and sellers are obligated to honor the values that are set for a listing.   
  
**Applicable values:** To determine which international return periods are supported for a specific leaf category on a specific eBay marketplace, use the **Metadata API** [getReturnPolicies](https://developer.ebay.com/api-docs/sell/metadata/resources/marketplace/methods/getReturnPolicies) method. Pass the target **marketplace_id** and the category ID in the filter query parameter, and then inspect the **returnPolicies.international.returnPeriods** field in the response.   
  
**For AddItem, VerifyAddItem, and RelistItem:** If the seller accepts international returns (InternationalReturnsAcceptedOption is set to ReturnsAccepted) but does not specify this field for a listing, eBay sets a default value (often Days_30) and the seller is obligated to honor this setting.   
  
**For ReviseItem only:** You cannot change the value of this field if the listing has bids or sales, or if the listing ends within 12 hours. For more details, see the **ReturnPolicy** description.   
  
**Note:** If a seller does not add a separate international return policy, the settings in the domestic return policy will be used instead. So if this field is not used in an add/revise/relist call, the return period for international returns will default to the value specified in the **ReturnsWithinOption** field.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Coarse, Fine, Medium. See [International Return Durations (in getReturnPolicies)](https://developer.ebay.com/api-docs/sell/metadata/resources/marketplace/methods/getReturnPolicies) for supported international return durations for each marketplace and category.   
  
**Applicable values** : See [ReturnsWithinOptionsCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/ReturnsWithinOptionsCodeType.html)  |  
|  ItemArray.Item.ReturnPolicy  
.**InternationalShippingCostPaidByOption**  | [token](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#token)  | Conditionally  |  This field is conditionally required if a seller is using a separate return policy for international returns, and is accepting international returns. The value in this field specifies whether the buyer or the seller pays for international return shipping charges. Accepted values are `Buyer` or `Seller`. eBay sites often set `Seller` as the default value for this field, and sellers are obligated to honor the values that are set for a listing.   
  
Depending on the seller's return policy and the specifics of a return, either the buyer or the seller can be responsible for the return shipping costs. Note that the seller is always responsible for return shipping costs for SNAD-related issues or for late shipments.   
  
**For ReviseItem only:** You cannot change the value of this field if the listing has bids or sales, or if the listing ends within 12 hours. For more details, see the **ReturnPolicy** description.   
  
**Note:** If a seller does not add a separate international return policy, the settings in the domestic return policy will be used instead. So if this field is not used in an add/revise/relist call, return shipping cost payee for international returns will default to the value specified in the **ShippingCostPaidByOption** field.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Coarse, Fine, Medium. See [Return Shipping Cost Payee Values (in getReturnPolicies)](https://developer.ebay.com/api-docs/sell/metadata/resources/marketplace/methods/getReturnPolicies) for supported international return shipping cost payee values for each marketplace and category.   
  
**Applicable values** : See [ShippingCostPaidByOptionsCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/ShippingCostPaidByOptionsCodeType.html)  |  
|  ItemArray.Item.ReturnPolicy  
.**Refund**  | [string](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string)  | Conditionally  |  Display string that buyer applications can use to present **RefundOption** in a more user-friendly format to buyers. For example, in **GetItem** and related calls, this value is usually localized and can contain spaces. If necessary, you can predict the choice of values based on the **Refund.Description** options returned by **GeteBayDetails**.   
  
This field is applicable to only the US marketplace and is not applicable as input to the **Add** /**Revise** /**Relist** family of calls. (Use **RefundOption** instead.)   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Coarse, Fine, Medium.   |  
|  ItemArray.Item.ReturnPolicy  
.**RefundOption**  | [token](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#token)  | Conditionally  |  This field indicates how the seller compensates buyers for returns. `MoneyBack` is the only supported value for all marketplaces except for the US. On the US marketplace, you can set this value to either `MoneyBack` or `MoneyBackOrReplacement`. `MoneyBackOrReplacement` can be used by sellers that have the depth of inventory to support an exchange for an identical item. However, ultimately, it is up to the buyer on whether they want money back or a replacement item.   
  
**For ReviseItem only:** You cannot change the value of this field if the listing has bids or sales, or if the listing ends within 12 hours. For more details, see the **ReturnPolicy** description.   
  
**Note:** If a seller ships internationally, and wants to define and use a separate international returns policy, the international equivalent of this field is the **InternationalRefundOption** field.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Coarse, Fine, Medium. See [Domestic Refund Methods (in getReturnPolicies)](https://developer.ebay.com/api-docs/sell/metadata/resources/marketplace/methods/getReturnPolicies) for supported domestic refund methods for each marketplace and category.   
  
**Applicable values** : See [RefundOptionsCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/RefundOptionsCodeType.html)  |  
|  ItemArray.Item.ReturnPolicy  
.**ReturnsAccepted**  | [string](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string)  | Conditionally  |  Display string that buyer applications can use to present **ReturnsAcceptedOption** in a more user-friendly format to buyers. For example, in **GetItem** and related calls, this value is usually localized and can contain spaces.   
  
If necessary, you can predict the choice of values based on the **ReturnsAccepted.Description** options returned by **GeteBayDetails**.   
  
Not applicable as input to the **AddItem** family of calls. (Use **ReturnsAcceptedOption** instead.)   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Coarse, Fine, Medium.   |  
|  ItemArray.Item.ReturnPolicy  
.**ReturnsAcceptedOption**  | [token](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#token)  | Conditionally  |  This required field indicates whether or not the seller accepts returns.   
  
Applicable values are `ReturnsAccepted` or `ReturnsNotAccepted`. When set to `ReturnsAccepted`, this option indicates the seller allows items to be returned. Specify **ReturnsNotAccepted** for a listing if returns are not accepted.   
  
On the eBay DE, IE, and UK marketplaces, registered business sellers must accept returns for fixed-price items (including auction items with Buy It Now and any other fixed price formats) when the category requires a return policy. On some European sites, such as eBay Germany (DE), registered business sellers are required to accept returns. Use the Trading call **GetUser** to determine the status of an eBay business seller in DE, IE, and UK. Review the **User.SellerInfo.SellerBusinessType** field in the response.   
  
**Note:** In order for Top-Rated sellers to receive a Top-Rated Plus seal for their listings, returns must be accepted for their items (**ReturnsAcceptedOption** = `ReturnsAccepted`) and handling time should be set to zero-day (same-day shipping) or one-day shipping. Set the handling time (in days) using the **Item.DispatchTimeMax** field.   
**For ReviseItem only:** You cannot change the value of this field if the listing has bids or sales, or if the listing ends within 12 hours. For more details, see the **ReturnPolicy** description.   
  
**Note:** If a seller ships internationally, and wants to define and use a separate international returns policy, the international equivalent of this field is the **InternationalReturnsAcceptedOption** field.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Coarse, Fine, Medium. See [Domestic Returns Accepted Values (in getReturnPolicies)](https://developer.ebay.com/api-docs/sell/metadata/resources/marketplace/methods/getReturnPolicies) for supported domestic returns accepted values for each marketplace and category.   
  
**Applicable values** : See [ReturnsAcceptedOptionsCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/ReturnsAcceptedOptionsCodeType.html)  |  
|  ItemArray.Item.ReturnPolicy  
.**ReturnsWithin**  | [string](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string)  | Conditionally  |  Display string that buyer applications can use to present **ReturnsWithinOption** in a more user-friendly format to buyers. For example, in **GetItem** and related calls, this value is usually localized and can contain spaces.   
  
If necessary, you can predict the choice of values based on the **ReturnsWithin.Description** options returned by **GeteBayDetails**.   
  
Not applicable as input to the **AddItem** family of calls. (Use **ReturnsWithinOption** instead.)   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Coarse, Fine, Medium.   |  
|  ItemArray.Item.ReturnPolicy  
.**ReturnsWithinOption**  | [token](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#token)  | Conditionally  |  Specifies the amount of time the buyer has to return an item. The return period begins when the item is marked "delivered" at the buyer's specified ship-to location. Most marketplaces and categories support 30-day and 60-day return periods. eBay sites often set 30-days as the default value for this field and sellers are obligated to honor the values that are set for a listing. This value is required if **ReturnsAcceptedOption=ReturnsAccepted**.   
**Note:** Eligible Parts & Accessories (P&A) listings require sellers to offer buyers free returns with a minimum return period of 30 days. See [Support for easy returns in Parts and Accessories](https://developer.ebay.com/api-docs/user-guides/static/trading-user-guide/ebay-motors-parts-accessories-easy-returns.html) for details.   
**Applicable values:** To determine which domestic return periods are supported for a specific leaf category on a specific eBay marketplace, use the **Metadata API** [getReturnPolicies](https://developer.ebay.com/api-docs/sell/metadata/resources/marketplace/methods/getReturnPolicies) method. Pass the target **marketplace_id** and the category ID in the filter query parameter, and then inspect the **returnPolicies.domestic.returnPeriods** field in the response.   
  
**For ReviseItem only:** You cannot change the value of this field if the listing has bids or sales, or if the listing ends within 12 hours. For more details, see the **ReturnPolicy** description.   
  
**Note:** If a seller ships internationally, and wants to define and use a separate international returns policy, the international equivalent of this field is the **InternationalReturnsWithinOption** field.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Coarse, Fine, Medium. See [Domestic Return Durations (in getReturnPolicies)](https://developer.ebay.com/api-docs/sell/metadata/resources/marketplace/methods/getReturnPolicies) for supported domestic return durations for each marketplace and category.   
  
**Applicable values** : See [ReturnsWithinOptionsCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/ReturnsWithinOptionsCodeType.html)  |  
|  ItemArray.Item.ReturnPolicy  
.**ShippingCostPaidBy**  | [string](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string)  | Conditionally  |  This is a display string that buyer applications can use to present **ShippingCostPaidByOption** in a more user-friendly format to buyers. For example, in **GetItem** and related calls, this value is usually localized and can contain spaces.   
  
If necessary, you can predict the choice of values based on the **ShippingCostPaidBy.Description** options returned by **GeteBayDetails**.   
  
Not applicable as input to the **AddItem** family of calls. (Use **ShippingCostPaidByOption** instead.)   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Coarse, Fine, Medium.   |  
|  ItemArray.Item.ReturnPolicy  
.**ShippingCostPaidByOption**  | [token](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#token)  | Conditionally  |  This option specifies whether the buyer or the seller pays for return shipping charges. Accepted values are `Buyer` or `Seller`. eBay sites often set `Seller` as the default value for this field, and sellers are obligated to honor the values that are set for a listing. This value is required if **ReturnsAcceptedOption=ReturnsAccepted**.   
  
Depending on the seller's return policy and the specifics of a return, either the buyer or the seller can be responsible for the return shipping costs. Note that the seller is always responsible for return shipping costs for SNAD-related issues or for late shipments.   
**Note:** Eligible Parts & Accessories (P&A) listings require sellers to offer buyers free returns with a minimum return period of 30 days. See [Support for easy returns in Parts and Accessories](https://developer.ebay.com/api-docs/user-guides/static/trading-user-guide/ebay-motors-parts-accessories-easy-returns.html) for details.   
**For ReviseItem only:** You cannot change the value of this field if the listing has bids or sales, or if the listing ends within 12 hours. For more details, see the **ReturnPolicy** description.   
  
**Note:** If a seller ships internationally, and wants to define and use a separate international returns policy, the international equivalent of this field is the **InternationalShippingCostPaidByOption** field.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Coarse, Fine, Medium. See [Return Shipping Cost Payee Values (in getReturnPolicies)](https://developer.ebay.com/api-docs/sell/metadata/resources/marketplace/methods/getReturnPolicies) for supported domestic return shipping cost payee values for each marketplace and category.   
  
**Applicable values** : See [ShippingCostPaidByOptionsCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/ShippingCostPaidByOptionsCodeType.html)  |  
|  ItemArray.Item.**ReviseStatus**  | [ReviseStatusType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/ReviseStatusType.html)  | Conditionally  |  This container is returned if a listing has been revised in any way since it first became active. One or more boolean fields will be returned under this container based on the type of revision(s) that occured, including a general revision, a price change, or a feature added or removed.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Coarse, Fine, Medium.   |  
|  ItemArray.Item.ReviseStatus  
.**ItemRevised**  | [boolean](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean)  | Conditionally  |  This field is returned as `true` if the original listing has been revised. This field is always returned with the **ReviseStatus** container.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   |  
|  ItemArray.Item  
.**SecondaryCategory**  | [CategoryType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CategoryType.html)  | Conditionally  |  The unique identifier for a secondary category. This field is only applicable if the seller decides to list the item under two categories. For this optional second listing category, if supplied, the **SecondaryCategory.CategoryID** must also be a valid leaf category on the category tree for the request site. Two-category listings are allowed only when both category IDs are valid on that same site tree. Validate against that marketplace's Taxonomy tree (for example, [getCategorySubtree](https://developer.ebay.com/api-docs/commerce/taxonomy/resources/category_tree/methods/getCategorySubtree) on tree 100 for eBay Motors).   
  
Some category programs or category combinations may still limit whether an item can be listed in two categories, and a secondary category may incur an additional listing fee. Any secondary category used must still comply with the request site (`X-EBAY-API-SITEID` / **Item.Site**) category-tree requirements described above.   
  
You cannot list US eBay Motors vehicles in two categories. Some **Parts & Accessories** listings may be eligible for a secondary category, and a secondary category may incur an additional listing fee. Any secondary category used must still comply with the listing site's category-tree requirements described above.   
  
If eBay has designated a listing category as a value category, and that listing category will be the seller's primary category, the seller will not be able to list their item in a secondary category. If a seller's request payload includes a primary or a secondary category that is designated as a value category, then eBay drops the **SecondaryCategory** ID and only lists the item in the category specified with the **PrimaryCategory** ID. Also, if the listing request includes Item Specifics (in **ItemSpecifics**) that are associated with the **SecondaryCategory** , eBay drops those values as well when the **SecondaryCategory** is dropped. The same logic is used if you revise an existing listing to add a secondary category, or to change one of the categories: If either the primary or secondary category is a value category, eBay drops the secondary category from your request. To determine whether a specific leaf category is a value category, use the **Metadata API** [getCategoryPolicies](https://developer.ebay.com/api-docs/sell/metadata/resources/marketplace/methods/getCategoryPolicies) method and inspect the **valueCategory** field.   
  
To remove this value when relisting an item, use **DeletedField**.   
  
**For ReviseItem only:** When revising a listing within 12 hours of the listing's scheduled end time, you can only add or change the secondary category when an auction listing has no active bids or a multiple-quantity, fixed-price listing has no items sold. If you change the secondary category, any corresponding Item Specifics that were previously specified may be dropped from the listing if they aren't valid for the category.   
  
**For ReviseItem only:** Previously, removing the listing from a secondary category was only possible within 12 hours of the listing's scheduled end time when an auction listing had no active bids or a multiple-quantity, fixed-price listing had no items sold, but this restriction no longer exists. Now, the secondary category can be dropped for any active listing at any time, regardless of whether an auction listing has bids or a fixed-price listing has sales. To drop a secondary category, the seller passes in a value of `0` in the **SecondaryCategory.CategoryID** field.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   |  
|  ItemArray.Item  
.SecondaryCategory.**CategoryID**  | [string](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string)  | Conditionally  |  This string value is the unique identifier of an eBay category. For listing calls, this ID must be a valid leaf on the category tree for the listing site. Validate against that marketplace's Taxonomy tree (for example, [getCategorySubtree](https://developer.ebay.com/api-docs/commerce/taxonomy/resources/category_tree/methods/getCategorySubtree) on tree 100 for eBay Motors). In **GetItem** and related calls, see the **CategoryName** field for the text name of the category. The parent category of this eBay category can be retrieved through the [Taxonomy API's](https://developer.ebay.com/api-docs/commerce/taxonomy/resources/methods) **getCategoryTree** or **getCategorySubtree** methods and inspecting the **parentCategoryTreeNodeHref** field in the response.   
**Note:** When listing in categoryID 173651 (Auto Performance Tuning Devices & Software), use of catalog products is required. For more information, see [Tuning devices and software](https://developer.ebay.com/api-docs/user-guides/static/trading-user-guide/tuning-devices-and-software.html).  In an Add call, the **PrimaryCategory.CategoryID** is conditionally required unless the seller successfully uses the **ProductListingDetails** container to find an eBay catalog product match. When the seller successfully uses an eBay catalog product to create a listing, the listing title, listing description, item specifics, listing category, and stock photo defined in the catalog product is used to create the listing.   
  
In an Add/Revise/Relist call, the **SecondaryCategory.CategoryID** is conditionally required if a Secondary Category is used. Using a Secondary Category can incur a listing fee. The secondary category ID must be a valid leaf category on the category tree for the listing site; an ID valid only on another marketplace tree is rejected. Validate against that marketplace's Taxonomy tree (for example, [getCategorySubtree](https://developer.ebay.com/api-docs/commerce/taxonomy/resources/category_tree/methods/getCategorySubtree) on tree 100 for eBay Motors).   
  
**For ReviseItem only:** Previously, removing the listing from a secondary category was only possible within 12 hours of the listing's scheduled end time when an auction listing had no active bids or a multiple-quantity, fixed-price listing had no items sold, but this restriction no longer exists. Now, the secondary category can be dropped for any active listing at any time, regardless of whether an auction listing has bids or a fixed-price listing has sales. To drop a secondary category, the seller passes in a value of `0` in the **SecondaryCategory.CategoryID** field.   
  
**Max length:** 10.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   |  
|  ItemArray.Item  
.SecondaryCategory  
.**CategoryName**  | [string](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string)  | Conditionally  |  This string value is the display name of the eBay primary category, as it would appear on the eBay site. In **GetItem** , this will be a fully-qualified category name (e.g., Collectibles:Decorative Collectibles:Hummel, Goebel).   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   |  
|  ItemArray.Item  
.**SellerContactDetails**  | [AddressType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/AddressType.html)  | Conditionally  |  This container is used by sellers of Classified Ad listings to provide contact information.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll. See [Classified ad listings](https://developer.ebay.com/api-docs/user-guides/static/trading-user-guide/classified-ads.html).  |  
|  ItemArray.Item.**SellerProfiles**  | [SellerProfilesType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/SellerProfilesType.html)  | Conditionally  |  This container is used if the seller would like to use/reference business policies to create, revise, relist, or verify their listing. The seller's account must be opted in to business policies to use this container. If this container is used, exactly one Payment Business Policy, one Shipping Business Policy, and one Return Business Policy must be specified and applied to the listing. If the seller's account is not opted in to business policies, that seller may not use this container. Sellers must opt-in to business policies through My eBay or by using the **optInToProgram** call of the **eBay Account API**.   
  
If business policies are applied to a listing, all payment, shipping, and return policy settings in these policies will override any other payment, shipping, or return policy legacy fields that are included in the call request.   
**Note:** To make sure that the shipping cost override and policies are set correctly on an item (that is using business policies and has one or more shipping service cost overrides set up), the **Item.SellerProfiles.SellerShippingProfile** container and the **Item.ShippingServiceCostOverrideList.ShippingServiceCostOverride** container(s) must be included, even if no changes are being made.  This container is only returned in 'Get' calls if business policies are set for the listing, and the person making the API call is the seller of the listing.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   |  
|  ItemArray.Item.SellerProfiles  
.**SellerPaymentProfile**  | [SellerPaymentProfileType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/SellerPaymentProfileType.html)  | Conditionally  |  The **SellerPaymentProfile** container is used in an Add/Revise/Relist/Verify API call to reference and use the settings/values of a payment business policy. Payment business policies contain a setting to control whether immediate payment is required, settings to specify due dates for the deposit and full payment of a motor vehicle listing (Motors policy only), and settings to specify which offline payment methods are avaiable to buyers for sales transactions that happen off of eBay's platform. Multiple payment business policies can be created and saved at the account level by sellers.   
  
This container is only returned in 'Get' calls if Business Policies are set for the listing, and the person making the API call is the seller of the listing.   
  
**Note:** Sellers will never have to specify electronic payment methods, but offline payment methods are required for listings where offline payment is required or supported.    
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   |  
|  ItemArray.Item.SellerProfiles  
.SellerPaymentProfile  
.**PaymentProfileID**  | [long](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#long)  | Conditionally  |  The unique identifier of a payment business policy. A **PaymentProfileID** and/or a **PaymentProfileName** value is used in the Add/Revise/Relist/Verify call to reference and use the payment settings/values of a payment business policy. If both fields are provided and their values don't match, the **PaymentProfileID** takes precedence.   
  
Payment profile IDs can be retrieved with the **getPaymentPolicies** call of the **Account API** or with the **getSellerProfiles** call of the **Business Policies Management API**. Business policy IDs can also be retrieved through the Business policies section of My eBay.   
  
In the 'Get' calls, the **PaymentProfileID** value will always be returned if business policies are set for the listing, and the person making the API call is the seller of the listing. The **PaymentProfileName** value will be returned if a name is assigned to the payment business policy.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   |  
|  ItemArray.Item.SellerProfiles  
.SellerPaymentProfile  
.**PaymentProfileName**  | [string](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string)  | Conditionally  |  The name of a payment business policy. A **PaymentProfileID** and/or a **PaymentProfileName** value is used in the Add/Revise/Relist/Verify call to reference and use the payment settings/values of a payment business policy. If both fields are provided and their values don't match, the **PaymentProfileID** takes precedence.   
  
In the 'Get' calls, the **PaymentProfileID** value will always be returned if business policies are set for the listing, and the person making the API call is the seller of the listing. The **PaymentProfileName** value will be returned if a name is assigned to the payment business policy.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   |  
|  ItemArray.Item.SellerProfiles  
.**SellerReturnProfile**  | [SellerReturnProfileType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/SellerReturnProfileType.html)  | Conditionally  |  The **SellerReturnProfile** container is used in an Add/Revise/Relist/Verify Trading API call to reference and use the settings/values of a return business policy. Return business policies contain detailed information on the seller's return policy for domestic and international buyers (if the seller ships internationally), including whether or not the seller accepts returns from domestic and international buyers, how many days the buyer has to return the item for a refund, and who pays the return shipping costs. Multiple return policy business policies can be created and saved at the account level by sellers.   
**Note:** As a part of Digital Services Act (DSA) requirements, as of April 3, 2023, buyers in the EU must be allowed to return an item within 14 days or more, unless the item is exempt. Where applicable, sellers should update their return policies to reflect this requirement of accepting returns from EU buyers. This update can be made through the **ReturnPolicy** container or through a return business policy that is referenced through the **SellerProfiles.SellerReturnProfile** container.   
  
This container is only returned in 'Get' calls if Business Policies are set for the listing and the person making the API call is the seller of the listing.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   |  
|  ItemArray.Item.SellerProfiles  
.SellerReturnProfile  
.**ReturnProfileID**  | [long](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#long)  | Conditionally  |  The unique identifier of a return policy business policy. A **ReturnProfileID** and/or a **ReturnProfileName** value is used in the Add/Revise/Relist/Verify call to reference and use the return policy settings/values of a return policy business policy. If both fields are provided and their values don't match, the **ReturnProfileID** takes precedence.   
  
Return policy profile IDs can be retrieved with the **getReturnPolicies** call of the **Account API** or with the **getSellerProfiles** call of the **Business Policies Management API**. Business policy IDs can also be retrieved through the Business policies section of My eBay.   
  
In the 'Get' calls, the **ReturnProfileID** value will always be returned if business policies are set for the listing, and the person making the API call is the seller of the listing. The **ReturnProfileName** value will be returned if a name is assigned to the return policy business policy.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   |  
|  ItemArray.Item.SellerProfiles  
.SellerReturnProfile  
.**ReturnProfileName**  | [string](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string)  | Conditionally  |  The name of a return policy business policy. A **ReturnProfileID** and/or a **ReturnProfileName** value is used in the Add/Revise/Relist/Verify call to reference and use the return policy settings/values of a return policy business policy. If both fields are provided and their values don't match, the **ReturnProfileID** takes precedence.   
  
In the 'Get' calls, the **ReturnProfileID** value will always be returned if business policies are set for the listing, and the person making the API call is the seller of the listing. The **ReturnProfileName** value will be returned if a name is assigned to the return policy business policy.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   |  
|  ItemArray.Item.SellerProfiles  
.**SellerShippingProfile**  | [SellerShippingProfileType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/SellerShippingProfileType.html)  | Conditionally  |  The **SellerShippingProfile** container is used in an Add/Revise/Relist/Verify Trading API call to reference and use the settings/values of a specific shipping business policy. Shipping business policies contain detailed information on domestic and international shipping, including shipping service options and costs, handling time, shipping discount information, and excluded ship-to locations. Multiple shipping business policies can be created and saved at the account level by sellers.   
**Note:** Any shipping inclusions specified through this container can be overridden by the eBay International Shipping exclusions toggle located under **Shipping Preferences** in **My eBay**. For more information on eBay International Shipping, see [eBay International Shipping program](https://www.ebay.com/help/selling/shipping-items/setting-shipping-options/ebay-international-shipping-program?id=5348).  This container is only returned in 'Get' calls if Business Policies are set for the listing, and the person making the API call is the seller of the listing.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   |  
|  ItemArray.Item.SellerProfiles  
.SellerShippingProfile  
.**ShippingProfileID**  | [long](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#long)  | Conditionally  |  The unique identifier of a shipping business policy. A **ShippingProfileID** and/or a **ShipppingProfileName** value is used in the Add/Revise/Relist/Verify call to reference and use the shippping-related settings/values of a shipping business policy. If both fields are provided and their values don't match, the **ShipppingProfileID** takes precedence.   
  
Shipping profile IDs can be retrieved with the **getFulfillmentPolicies** call of the **Account API** or with the **getSellerProfiles** call of the **Business Policies Management API**. Business policy IDs can also be retrieved through the Business policies section of My eBay.   
  
In the 'Get' calls, the **ShipppingProfileID** value will always be returned if business policies are set for the listing, and the person making the API call is the seller of the listing. The **ShipppingProfileName** value will be returned if a name is assigned to the shipping business policy.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   |  
|  ItemArray.Item.SellerProfiles  
.SellerShippingProfile  
.**ShippingProfileName**  | [string](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string)  | Conditionally  |  The name of a shipping business policy. A **ShippingProfileID** and/or a **ShippingProfileName** value is used in the Add/Revise/Relist/Verify call to reference and use the shipping-related settings/values of a shipping business policy. If both fields are provided and their values don't match, the **ShippingProfileID** takes precedence.   
  
In the 'Get' calls, the **ShippingProfileID** value will always be returned if business policies are set for the listing, and the person making the API call is the seller of the listing. The **ShippingProfileName** value will be returned if a name is assigned to the shipping business policy.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   |  
|  ItemArray.Item.**SellingStatus**  | [SellingStatusType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/SellingStatusType.html)  | Conditionally  |  Various details about the current status of the listing, such as the current number of bids, the current high bidder, quantity sold, current price, and listing status.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine.   |  
|  ItemArray.Item.SellingStatus  
.**AdminEnded**  | [boolean](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean)  | Conditionally  |  If included in the response as `true`, indicates that the listing was administratively canceled due to a violation of eBay's listing policies and that the item can be relisted using **RelistItem**.   
  
**Note:** **GetItem** returns an error (invalid item ID) in the response if **Item.SellingStatus.AdminEnded** = `true` and the requesting user is not the seller of the item.    
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   |  
|  ItemArray.Item.SellingStatus  
.**BidCount**  | [int](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#int)  | Conditionally  |  Number of bids placed so far against the auction item.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine.   |  
|  ItemArray.Item.SellingStatus  
.**BidIncrement**  |  [AmountType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/AmountType.html) ([double](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#double))  | Conditionally  |  The minimum amount a progressive bid must be above the current high bid to be accepted. This field is only applicable to auction listings. The value of this field will always be '0.00' for Classified Ad and fixed-price listings.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine.   |  
| ItemArray.Item.SellingStatus  
.**BidIncrement**  
[ attribute **currencyID** ]  | [CurrencyCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html)  | Conditionally  |  The minimum amount a progressive bid must be above the current high bid to be accepted. This field is only applicable to auction listings. The value of this field will always be '0.00' for Classified Ad and fixed-price listings.  
  
For a list of possible enumeration values, see [CurrencyCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html).   |  
|  ItemArray.Item.SellingStatus  
.**ConvertedCurrentPrice**  |  [AmountType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/AmountType.html) ([double](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#double))  | Conditionally  |  Converted value of the **CurrentPrice** in the currency of the site that returned this response. For active items, refresh the listing's data every 24 hours to pick up the current conversion rates. Only returned when the item's **CurrentPrice** on the listing site is in different currency than the currency of the host site for the user/application making the API call. **ConvertedCurrentPrice** is not returned for Classified listings (Classified listings are not available on all sites).  
  
In multi-variation listings, this value matches the lowest-priced variation that is still available for sale.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine.   |  
| ItemArray.Item.SellingStatus  
.**ConvertedCurrentPrice**  
[ attribute **currencyID** ]  | [CurrencyCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html)  | Conditionally  |  Converted value of the **CurrentPrice** in the currency of the site that returned this response. For active items, refresh the listing's data every 24 hours to pick up the current conversion rates. Only returned when the item's **CurrentPrice** on the listing site is in different currency than the currency of the host site for the user/application making the API call. **ConvertedCurrentPrice** is not returned for Classified listings (Classified listings are not available on all sites).  
  
In multi-variation listings, this value matches the lowest-priced variation that is still available for sale.  
  
For a list of possible enumeration values, see [CurrencyCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html).   |  
|  ItemArray.Item.SellingStatus  
.**CurrentPrice**  |  [AmountType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/AmountType.html) ([double](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#double))  | Conditionally  |  The current price of the item in the original listing currency.   
  
For auction listings, this price is the starting minimum price (if the listing has no bids) or the current highest bid (if bids have been placed) for the item. This does not reflect the **BuyItNow** price.   
  
For fixed-price and ad format listings, this is the current listing price.   
  
In multi-variation, fixed-price listings, this value matches the lowest-priced variation that is still available for sale.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine.   |  
| ItemArray.Item.SellingStatus  
.**CurrentPrice**  
[ attribute **currencyID** ]  | [CurrencyCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html)  | Conditionally  |  The current price of the item in the original listing currency.   
  
For auction listings, this price is the starting minimum price (if the listing has no bids) or the current highest bid (if bids have been placed) for the item. This does not reflect the **BuyItNow** price.   
  
For fixed-price and ad format listings, this is the current listing price.   
  
In multi-variation, fixed-price listings, this value matches the lowest-priced variation that is still available for sale.  
  
For a list of possible enumeration values, see [CurrencyCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html).   |  
|  ItemArray.Item.SellingStatus  
.**HighBidder**  | [UserType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/UserType.html)  | Conditionally  |  For ended auction listings that have a winning bidder, this field is a container for the high bidder's user ID. For ended, single-item, fixed-price listings, this field is a container for the user ID of the purchaser. This field isn't returned for auctions with no bids, or for active fixed-price listings.   
  
In the case of **PlaceOffer** , for auction listings, this field is a container for the high bidder's user ID. In the **PlaceOffer** response, the following applies: For multiple-quantity, fixed-price listings, the high bidder is only returned if there is just one order line item (or only for the first order line item that is created).   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine.   |  
|  ItemArray.Item.SellingStatus  
.HighBidder.**AboutMePage**  | [boolean](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean)  | Conditionally  |    
A value of `true` indicates that the user has set up an About Me page.   
**Note:** This field will stop being returned in **GetItemTransactions** and **GetSellerTransactions** on January 31, 2024.    
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine.   |  
|  ItemArray.Item.SellingStatus  
.HighBidder.**BuyerInfo**  | [BuyerType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/BuyerType.html)  | Conditionally  |  Contains information about the user as a buyer, such as the shipping address. See **BuyerType** for its child elements.   
  
Since a bidder's user info is anonymous, this tag will be returned only to that bidder, and to the seller of an item that the user is bidding on.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine. See [Anonymous user information](https://developer.ebay.com/api-docs/user-guides/static/trading-user-guide/user-mgmt-anonymous-info.html).  |  
|  ItemArray.Item.SellingStatus  
.HighBidder.BuyerInfo  
.**ShippingAddress**  | [AddressType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/AddressType.html)  | Conditionally  |  This container shows the buyer's shipping address.   
  
**Note:** For an Authenticity Guarantee program order returned in **GetItemTransactions** or **GetSellerTransactions** , this is the address of the authenticator's warehouse. The authenticator is responsible for delivery to the buyer's shipping address.  **Note:** For Click and Collect orders, this is the address of the merchant's store where the buyer will pick up the order. This is only applicable for **GetItemTransactions** and **GetSellerTransactions** calls.  **Note:** For eBay Vault scenarios: **GetItemTransactions** calls, and **GetSellerTransactions** calls (Seller View only), mock address details are returned for:   
  
-_Vault to vault orders: Buyer and Seller View_  
  
-_Ship to vault orders_ : Mock addresses are returned for the Buyer View (only); the address returned for the Seller View will be the authenticator&apos;s address.  
  
-_Vault in-hand submission orders_ : the address returned for the Buyer View will be the authenticator's address (**GetItemTransactions** only).  
  
The following address details are returned for mock addresses:  
```
 <ShippingAddress>   
   <Name>eBay Vault</Name>   
   <AddressID>Invalid Request</AddressID>   
   <AddressOwner>eBay</AddressOwner>   
   <AddressUsage>Invalid</AddressUsage>   
   <CityName>Invalid Request</CityName>   
   <Country>US</Country>   
   <CountryName>Invalid Request</CountryName>   
   <ExternalAddressID>Invalid Request</ExternalAddressID>   
   <Phone>Invalid Request</Phone>   
   <PostalCode>Invalid Request</PostalCode>   
   <StateOrProvince>Invalid Request</StateOrProvince>   
   <Street1>Invalid Request</Street1>   
   <Street2></Street2>   
 </ShippingAddress> 
```
  
  
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine.   |  
|  ItemArray.Item.SellingStatus  
.HighBidder.BuyerInfo  
.ShippingAddress.**Country**  | [CountryCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CountryCodeType.html)  | Conditionally  |  The two-digit code representing the country of the user.  
  
If not provided as input, eBay uses the country associated with the eBay Site ID when the call is made.  
  
  
  
**Applicable values** : See [Country](https://developer.ebay.com/devzone/xml/docs/reference/ebay/extra/gtsllrlst.rspns.itmarry.itm.sllngstts.hghbddr.byrinf.shppngaddrss.cntry.html).   
Code so that your app gracefully handles any future changes to this list.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine.   |  
|  ItemArray.Item.SellingStatus  
.HighBidder.BuyerInfo  
.ShippingAddress.**PostalCode**  | [string](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string)  | Conditionally  |  User's postal code.  
  
**Max length:** GB, DE - 35; US, CA - 40; AU - 80; Other countries - 50.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine.   |  
|  ItemArray.Item.SellingStatus  
.HighBidder.**eBayGoodStanding**  | [boolean](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean)  | Conditionally  |    
This boolean field is returned as `true` if the eBay user is in good standing with eBay.   
**Note:** This field will stop being returned in **GetItemTransactions** and **GetSellerTransactions** on January 31, 2024.    
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine.   |  
|  ItemArray.Item.SellingStatus  
.HighBidder.**EIASToken**  | [string](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string)  | Conditionally  |  Unique identifier for the user that does not change when the eBay user name is changed. Use when an application needs to associate a new eBay user name with the corresponding eBay user.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine. See [Anonymous user information](https://developer.ebay.com/api-docs/user-guides/static/trading-user-guide/user-mgmt-anonymous-info.html).  |  
|  ItemArray.Item.SellingStatus  
.HighBidder.**Email**  | [string](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string)  | Conditionally  |  Email address for the user. Please see the links below to the topics related to anonymous user information and static email addresses. You cannot retrieve an email address for any user with whom you do not have an order relationship, regardless of site.   
  
An email address of another user is only returned if you and the other user are in an order relationship, within a certain time of order line item creation (although this limitation isn't applicable to the **GetAllBidders** call in the case of motor vehicles categories.) Based on Trust and Safety policies, the time is unspecified and can vary by site.   
  
Since a bidder's user info is anonymous, this tag will be returned only to that bidder, and to the seller of an item that the user is bidding on.   
  
For the **GetOrders** call, the buyer's email address will be returned (to the seller only) for orders less than two weeks old, but for orders that occurred more than two weeks in the past, the buyer's email address will no longer be returned. This **Email** field will still be returned, but 'dummy data', such as `Invalid Request` will replace the actual email address.   
  
**Note:** For the **GetItemTransactions** call, this field is only returned to the seller of the order; this field is not returned for the buyer or third party.   
**Max length:** 64 for US. May differ for other countries. Note: The eBay database allocates up to 128 characters for this field .   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll. See:   
[Anonymous user information](https://developer.ebay.com/api-docs/user-guides/static/trading-user-guide/user-mgmt-anonymous-info.html)   
[Member communications](https://developer.ebay.com/api-docs/user-guides/static/trading-user-guide/member-communications.html)  |  
|  ItemArray.Item.SellingStatus  
.HighBidder.**FeedbackPrivate**  | [boolean](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean)  | Conditionally  |  Indicates whether the user has chosen to make their feedback score and feedback details private (hidden from other users). The percentage of positive feedback can still be returned, even if other feedback details are private.   
  
Since a bidder's user info is anonymous, this tag will be returned only to that bidder, and to the seller of an item that the user is bidding on.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine. See [Anonymous user information](https://developer.ebay.com/api-docs/user-guides/static/trading-user-guide/user-mgmt-anonymous-info.html).  |  
|  ItemArray.Item.SellingStatus  
.HighBidder.**FeedbackRatingStar**  | [FeedbackRatingStarCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/FeedbackRatingStarCodeType.html)  | Conditionally  |    
A visual indicator of an eBay user's Feedback score. A different colored star is used for each range of Feedback scores. See **FeedbackRatingStarCodeType** for specific values.   
**Note:** This field will stop being returned in **GetItemTransactions** and **GetSellerTransactions** on January 31, 2024.    
  
**Applicable values** : See [FeedbackRatingStar](https://developer.ebay.com/devzone/xml/docs/reference/ebay/extra/gtsllrlst.rspns.itmarry.itm.sllngstts.hghbddr.fdbckrtngstr.html).   
Code so that your app gracefully handles any future changes to this list.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine.   |  
|  ItemArray.Item.SellingStatus  
.HighBidder.**FeedbackScore**  | [int](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#int)  | Conditionally  |  The aggregate feedback score for a user. A user's feedback score is the net positive feedback minus the net negative feedback left for the user. Feedback scores are a quantitative expression of the desirability of dealing with a user as a buyer or a seller in either side of an order.   
  
Each order line item can result in one feedback entry for a given user (the buyer can leave feedback for the seller, and the seller can leave feedback for the buyer.). That one feedback can be positive, negative, or neutral. The aggregated feedback counts for a particular user represent that user's overall feedback score (referred to as a "feedback rating" on the eBay site).   
  
If the user has chosen to make their feedback private and that user is not the user identified in the request's authentication token, **FeedbackScore** is not returned and **FeedbackPrivate** is returned with a value of `true`.   
  
In **GetMyeBayBuying** and **GetMyeBaySelling** , feedback information (**FeedbackScore** and **FeedbackRatingStar**) is returned in **BidList.ItemArray.Item.Seller**. For **GetMyeBayBuying** , the feedback score of each seller with an item having received a bid from the buyer is returned. For **GetMyeBaySelling** , the feedback score of the seller is returned.   
  
**GetMyeBayBuying** and **GetMyeBaySelling** also return feedback information (**FeedbackScore** and **FeedbackRatingStar**) in **BidList.ItemArray.Item.SellingStatus.HighBidder**. **GetMyeBayBuying** returns feedback information on the high bidder of each item the buyer is bidding on. **GetMyeBaySelling** returns feedback information on the high bidder of each item the seller is selling.  
  
Since a bidder's user info is anonymous, the real feedback score will be returned only to that bidder, and to the seller of an item that the user is bidding on. For all other users, the value -99 is returned.   
  
**For GetOrders and GetItemTransactions only:** If using Trading WSDL Version 1019 or above, this field will only be returned to the buyer or seller, and no longer returned at all to third parties. If using a Trading WSDL older than Version 1019, the accurate Feedback Score for the user is returned to the buyer or seller, but a dummy value of `0` will be returned to all third parties.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine. See [Anonymous user information](https://developer.ebay.com/api-docs/user-guides/static/trading-user-guide/user-mgmt-anonymous-info.html).  |  
|  ItemArray.Item.SellingStatus  
.HighBidder.**IDVerified**  | [boolean](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean)  | Conditionally  |    
Indicates whether the user has been verified. For more information about the ID Verify program, see: [Protecting your account](https://pages.ebay.com/help/policies/identity-idverify.html)   
**Note:** This field will stop being returned in **GetItemTransactions** and **GetSellerTransactions** on January 31, 2024.    
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine.   |  
|  ItemArray.Item.SellingStatus  
.HighBidder.**NewUser**  | [boolean](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean)  | Conditionally  |  This boolean is returned as `true` if the eBay user has been registered on eBay for 30 days or less.   
**Note:** The **Buyer.NewUser** field will stop being returned in **GetItemTransactions** and **GetSellerTransactions** on January 31, 2024.    
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine.   |  
|  ItemArray.Item.SellingStatus  
.HighBidder.**RegistrationDate**  | [dateTime](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#dateTime)  | Conditionally  |  Indicates the date the specified user originally registered with eBay.   
  
Since a bidder's user info is anonymous, this tag will be returned only to that bidder, and to the seller of an item that the user is bidding on.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine. See [Anonymous user information](https://developer.ebay.com/api-docs/user-guides/static/trading-user-guide/user-mgmt-anonymous-info.html).  |  
|  ItemArray.Item.SellingStatus  
.HighBidder.**Site**  | [SiteCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/SiteCodeType.html)  | Conditionally  |  eBay site the user is registered with.   
  
Since a bidder's user info is anonymous, this tag will be returned only to that bidder, and to the seller of an item that the user is bidding on.   
  
**Applicable values** : See [Site](https://developer.ebay.com/devzone/xml/docs/reference/ebay/extra/gtsllrlst.rspns.itmarry.itm.sllngstts.hghbddr.st.html).   
Code so that your app gracefully handles any future changes to this list.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine. See [Anonymous user information](https://developer.ebay.com/api-docs/user-guides/static/trading-user-guide/user-mgmt-anonymous-info.html).  |  
|  ItemArray.Item.SellingStatus  
.HighBidder.**Status**  | [UserStatusCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/UserStatusCodeType.html)  | Conditionally  |  Indicates the user's registration/user status.   
  
**Applicable values** : See [Status](https://developer.ebay.com/devzone/xml/docs/reference/ebay/extra/gtsllrlst.rspns.itmarry.itm.sllngstts.hghbddr.stts.html).   
Code so that your app gracefully handles any future changes to this list.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine.   |  
|  ItemArray.Item.SellingStatus  
.HighBidder.**UserAnonymized**  | [boolean](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean)  | Always  |  Indicates whether or not the User container has been made anonymous. If `true`, some elements in the User container have either been removed, or had their values changed to remove identifying characteristics. If false, all expected elements are returned, and no values are changed.   
  
Since a bidder's user info is anonymous, this tag is returned as false only to the bidder, and to the seller of an item that the user is bidding on. For all other users, this tag is returned as `true`.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine. See [Anonymous user information](https://developer.ebay.com/api-docs/user-guides/static/trading-user-guide/user-mgmt-anonymous-info.html).  |  
|  ItemArray.Item.SellingStatus  
.HighBidder.**UserID**  | [UserIDType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/UserIDType.html) ([string](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string))  | Conditionally  |  Unique eBay user ID for the user.  
  
**Note:** Effective September 26, 2025, select developers will no longer receive username data for U.S. users through this field. Instead, an immutable user ID will be returned in its place. For more information, please refer to [Data Handling Compliance](https://developer.ebay.com/api-docs/static/data-handling-update.html).    
Since a bidder's user info is anonymous, this tag contains the actual value of an ID only for that bidder, and for the seller of an item that the user is bidding on. For other users, the actual value is replaced by an anonymous value, according to these rules:   
  
When bidding on items, **UserID** is replaced with the value "a****b" where a and b are random characters from the **UserID**. For example, if the **UserID** = `IBidALot`, it might be displayed as, "I****A".   
  
**Important:** In this format, the anonymous bidder ID can change for each auction.  For **GetMyeBayBuying** only, when bidding on items: **UserID** is replaced with the value "a****b" where a and b are random characters from the **UserID**.   
  
When bidding on items listed on the Philippines site: **UserID** is replaced with the value "Bidder X" where X is a number indicating the order of that user's first bid. For example, if the user was the third bidder, **UserID** = `Bidder 3`. Note that in this Philippines site format, the anonymous bidder ID stays the same for a given auction, but is different for different auctions. For example, a bidder who is the third and then the seventh bidder in an auction will be listed for both bids as "Bidder 3". However, if that same bidder is the first bidder on a different auction, the bidder will be listed for that auction as "Bidder 1", not "Bidder 3".   
  
For **GetMyeBayBuying** only, when bidding on items listed on the UK and AU sites: **UserID** is replaced with the string "High Bidder".   
  
For **PlaceOffer** , see also **SellingStatus.HighBidder**.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine. See [Anonymous user information](https://developer.ebay.com/api-docs/user-guides/static/trading-user-guide/user-mgmt-anonymous-info.html).  |  
|  ItemArray.Item.SellingStatus  
.HighBidder.**UserIDChanged**  | [boolean](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean)  | Conditionally  |  If `true`, identifies a user whose ID has changed within the last 30 days. Does not indicate a new user (see **NewUser**).   
  
Since a bidder's user info is anonymous, this tag will be returned only to that bidder, and to the seller of an item that the user is bidding on.   
  
**Note:** For the **GetItemTransactions** call, this field is only returned to the seller of the order; this field is not returned for the buyer or third party.    
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine. See [Anonymous user information](https://developer.ebay.com/api-docs/user-guides/static/trading-user-guide/user-mgmt-anonymous-info.html).  |  
|  ItemArray.Item.SellingStatus  
.HighBidder.**UserIDLastChanged**  | [dateTime](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#dateTime)  | Conditionally  |    
Date and time when the user last changed their eBay user ID (in GMT).   
**Note:** The **Buyer.UserIDLastChanged** field will stop being returned in **GetItemTransactions** and **GetSellerTransactions** on January 31, 2024.    
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine. See [Anonymous user information](https://developer.ebay.com/api-docs/user-guides/static/trading-user-guide/user-mgmt-anonymous-info.html).  |  
|  ItemArray.Item.SellingStatus  
.HighBidder.**VATStatus**  | [VATStatusCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/VATStatusCodeType.html)  | Conditionally  |  Indicates whether or not the user is subject to VAT. Users who have registered with eBay as VAT-exempt are not subject to VAT. See documentation on Value-Added Tax (VAT).   
  
**Applicable values** :   
  


CustomCode
    (out) Reserved for internal or future use 

NoVATTax
    (out) VAT is not applicable 

VATExempt
    (out) Residence in a country with VAT and user is registered as VAT-exempt 

VATTax
    (out) Residence in a country with VAT and user is not registered as VAT-exempt   
Code so that your app gracefully handles any future changes to this list.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine. See [Vat-exempt sellers](https://developer.ebay.com/api-docs/user-guides/static/trading-user-guide/taxes-vat.html#exempt).  |  
|  ItemArray.Item.SellingStatus  
.**LeadCount**  | [int](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#int)  | Conditionally  |  Applicable to Ad type listings only. Indicates how many leads to potential buyers are associated with this item. Returns 0 (zero) for listings in other formats. You must be the seller of the item to retrieve the lead count.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ReturnAll.   |  
|  ItemArray.Item.SellingStatus  
.**ListingStatus**  | [ListingStatusCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/ListingStatusCodeType.html)  | Conditionally  |  Specifies an active or ended listing's status in eBay's processing workflow. 
  * If a listing ends with a sale (or sales), eBay needs to update the sale details (e.g., total price and buyer/high bidder) and the transaction fees. This processing can take several minutes.
  * If you retrieve a sold item and no details about the buyer/high bidder are returned or no transaction fees are available, use this listing status information to determine whether eBay has finished processing the listing.

  
  
**Applicable values** :   
  


Active
    (out) The listing is still active or the listing has ended with a sale but eBay has not completed processing the sale details. If the listing has ended with a sale but this Active status is returned, please allow several minutes for eBay to finish processing the listing. 

Completed
    (out) The listing has closed and eBay has completed processing the sale. All sale information returned from eBay should be considered accurate and complete. In this state, all transaction fees should be calculated. 

Custom
    (out) Reserved for internal or future use. 

CustomCode
    (out) Reserved for internal or future use. 

Ended
    (out) The listing has ended. If the listing ended with a sale, eBay has completed processing of the sale. All sale information returned from eBay should be considered accurate and complete. However, the transaction fees are not yet available.   
Code so that your app gracefully handles any future changes to this list.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine.   |  
|  ItemArray.Item.SellingStatus  
.**MinimumToBid**  |  [AmountType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/AmountType.html) ([double](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#double))  | Conditionally  |  Smallest amount the next bid on the item can be. Returns same value as **Item.StartPrice** (if no bids have yet been placed) or **CurrentPrice** plus **BidIncrement** (if at least one bid has been placed). Only applicable to auction listings. Returns null for fixed-price and Ad type listings.   
  
In multi-variation listings, this value matches the lowest-priced variation that is still available for sale.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine.   |  
| ItemArray.Item.SellingStatus  
.**MinimumToBid**  
[ attribute **currencyID** ]  | [CurrencyCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html)  | Conditionally  |  Smallest amount the next bid on the item can be. Returns same value as **Item.StartPrice** (if no bids have yet been placed) or **CurrentPrice** plus **BidIncrement** (if at least one bid has been placed). Only applicable to auction listings. Returns null for fixed-price and Ad type listings.   
  
In multi-variation listings, this value matches the lowest-priced variation that is still available for sale.  
  
For a list of possible enumeration values, see [CurrencyCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html).   |  
|  ItemArray.Item.SellingStatus  
.**PromotionalSaleDetails**  | [PromotionalSaleDetailsType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/PromotionalSaleDetailsType.html)  | Conditionally  |  If a seller has reduced the price of a listed item with the Promotional Price Display feature, this field contains the original price of the discounted item, along with the start-time and end-time of the discount.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   |  
|  ItemArray.Item.SellingStatus  
.PromotionalSaleDetails  
.**EndTime**  | [dateTime](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#dateTime)  | Conditionally  |  End time of a discount for an item whose price a seller has reduced with the Promotional Price Display feature.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   |  
|  ItemArray.Item.SellingStatus  
.PromotionalSaleDetails  
.**OriginalPrice**  |  [AmountType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/AmountType.html) ([double](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#double))  | Conditionally  |  Original price of an item whose price a seller has reduced with the Promotional Price Display feature.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   |  
| ItemArray.Item.SellingStatus  
.PromotionalSaleDetails  
.**OriginalPrice**  
[ attribute **currencyID** ]  | [CurrencyCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html)  | Conditionally  |  Original price of an item whose price a seller has reduced with the Promotional Price Display feature.  
  
For a list of possible enumeration values, see [CurrencyCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html).   |  
|  ItemArray.Item.SellingStatus  
.PromotionalSaleDetails  
.**StartTime**  | [dateTime](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#dateTime)  | Conditionally  |  Start time of a discount for an item whose price a seller has reduced with the Promotional Price Display feature.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   |  
|  ItemArray.Item.SellingStatus  
.**QuantitySold**  | [int](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#int)  | Conditionally  |  The total number of items purchased so far (in the listing's lifetime). Subtract this from **Quantity** to determine the quantity available.   
  
If the listing has Item Variations, then in **GetItem** (and related calls) and **GetItemTransactions** , **Item.SellingStatus.QuantitySold** contains the sum of all quantities sold across all variations in the listing, and **Variation.SellingStatus.QuantitySold** contains the number of items sold for that variation.   
  
In **GetSellerTransactions** , **Transaction.Item.SellingStatus.QuantitySold** contains the number of items sold in that order line item.  
  
For order line item calls, also see **Transaction.QuantityPurchased** for the number of items purchased in the order line item.  
In multi-variation listings, this value matches total quantity sold across all variations.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine.   |  
|  ItemArray.Item.SellingStatus  
.**ReserveMet**  | [boolean](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean)  | Conditionally  |  Indicates whether the reserve price has been met for the listing. Returns true if the reserve price was met or no reserve price was specified.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine.   |  
|  ItemArray.Item.SellingStatus  
.**SecondChanceEligible**  | [boolean](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean)  | Conditionally  |  Part of the Second Chance Offer feature, indicates whether the seller can extend a second chance offer for the item.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine.   |  
|  ItemArray.Item.**ShippingDetails**  | [ShippingDetailsType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/ShippingDetailsType.html)  | Conditionally  |  The shipping-related details for an order, including flat and calculated shipping costs.   
  
**Note:** For sellers who are using a shipping (aka Fulfillment) business policy to create/revise/relist an item, none of the fields under the **ShippingDetails** container are necessary. A fulfillment business policy can be set up and/or modified in My eBay, or via the [Account API](https://developer.ebay.com/api-docs/sell/account/resources/fulfillment_policy/methods/createFulfillmentPolicy). A fulfillment business policy is associated to a listing through the **Item.SellerProfiles.SellerShippingProfile** container.   
  
If you _do not_ use a fulfillment business policy, many of the fields under this **ShippingDetails** container become required in your request.  **Note:** **For ReviseItem and ReviseFixedPriceItem calls:** If you are updating any field under the **ShippingDetails** container, you must include all containers and fields set under this container even if their values are not changing. If you do not do this, some fields may be removed from the listing. To find out the values included in the current listing, call [GetItem](https://developer.ebay.com/devzone/xml/docs/Reference/eBay/GetItem.html#GetItem) and look through the **ShippingDetails** container in the response. For additional information, see [Revise shipping details](https://developer.ebay.com/api-docs/user-guides/static/trading-user-guide/shipping-revise.html).  New users who list their first items in selected categories on the US site must specify at least one domestic shipping service. This applies to a category if the **Metadata API** [getShippingPolicies](https://developer.ebay.com/api-docs/sell/metadata/resources/marketplace/methods/getShippingPolicies) method returns `true` for the **shippingTermsRequired** field.   
  
For multi-quantity, fixed-price listings, a seller can revise all shipping details of the listing (except for sales tax and for shipping type of Freight) for all unsold items. This applies to both domestic and international shipping. Checkout is not affected for those who bought items prior to the seller's shipping changes—the shipping details that were in effect at the time of purchase are used for that buyer at the time of checkout.   
  
Shipping details are not applicable to any classified ad listings, as shipping/delivery/pickup is handled by the buyer and seller off of the eBay platform.   
  
**Note:** To create a listing that is 'Local Pickup only' (buyer picks up, with no shipping/delivery available), the user does the following two things: 
  * Either omit the entire **ShippingDetails** container, or pass in an empty **ShippingDetails** container - <ShippingDetails/>
  * Pass in one **ShipToLocations** field, with its value set to `None` - <ShipToLocations>None</ShipToLocations>

  
For **GetMyeBayBuying, GetMyeBaySelling** : **ShippingDetails** is not returned.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Coarse, Fine, Medium. See:   
[Shipping costs](https://developer.ebay.com/api-docs/user-guides/static/trading-user-guide/shipping-costs.html)   
[Revising Items](https://developer.ebay.com/api-docs/user-guides/static/trading-user-guide/revise-listing.html) for restrictions on changing item properties with ReviseItem   |  
|  ItemArray.Item.ShippingDetails  
.**CalculatedShippingRate**  | [CalculatedShippingRateType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CalculatedShippingRateType.html)  | Conditionally  |  Details pertinent to one or more items for which calculated shipping has been offered by the seller, such as package dimension and weight and packaging/handling costs. If your call specifies a large-dimension item listed with UPS, see [Dimensional Weight limit on UPS shipping services results in failure of shipping calculator](https://developer.ebay.com/support/kb-article?KBid=1159).   
  
**Note:** The **CalculatedShippingRate** container should only be used to specify values for the **InternationalPackagingHandlingCosts** and/or **PackagingHandlingCosts** fields. The rest of the fields in the **CalculatedShippingRate** container are used to specify package dimensions and package weight, and these values should now be specified in the **ShippingPackageDetails** container instead.    
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   |  
|  ItemArray.Item.ShippingDetails  
.CalculatedShippingRate  
.**InternationalPackagingHandlingCosts**  |  [AmountType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/AmountType.html) ([double](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#double))  | Conditionally  |  This field shows any package handling cost applied to international shipping. This cost will be in addition to any shipping cost applicable to each international shipping service option.   
  
For international calculated shipping only.   |  
| ItemArray.Item.ShippingDetails  
.CalculatedShippingRate  
.**InternationalPackagingHandlingCosts**  
[ attribute **currencyID** ]  | [CurrencyCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html)  | Conditionally  |  This field shows any package handling cost applied to international shipping. This cost will be in addition to any shipping cost applicable to each international shipping service option.   
  
For international calculated shipping only.  
  
For a list of possible enumeration values, see [CurrencyCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html).   |  
|  ItemArray.Item.ShippingDetails  
.CalculatedShippingRate  
.**PackagingHandlingCosts**  |  [AmountType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/AmountType.html) ([double](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#double))  | Conditionally  |  Fees a seller might assess for the shipping of the item (in addition to whatever the shipping service might charge). Any packaging/handling cost specified on input is added to each shipping service on output.   
  
If domestic and international calculated shipping is offered for an item and if packaging/handling cost is specified only for domestic shipping, that cost will be applied by eBay as the international packaging/handling cost. (To specify a international packaging/handling cost, you must always specify a domestic packaging/handling cost, even if it is 0.) When UPS is one of the shipping services offered by the seller, package dimensions are required on list/relist/revise.   
**Note:** If the listing only has one domestic shipping service and it is free shipping, the domestic package handling cost will be ignored and will not be applied to the listing.    
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   |  
| ItemArray.Item.ShippingDetails  
.CalculatedShippingRate  
.**PackagingHandlingCosts**  
[ attribute **currencyID** ]  | [CurrencyCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html)  | Conditionally  |  Fees a seller might assess for the shipping of the item (in addition to whatever the shipping service might charge). Any packaging/handling cost specified on input is added to each shipping service on output.   
  
If domestic and international calculated shipping is offered for an item and if packaging/handling cost is specified only for domestic shipping, that cost will be applied by eBay as the international packaging/handling cost. (To specify a international packaging/handling cost, you must always specify a domestic packaging/handling cost, even if it is 0.) When UPS is one of the shipping services offered by the seller, package dimensions are required on list/relist/revise.   
**Note:** If the listing only has one domestic shipping service and it is free shipping, the domestic package handling cost will be ignored and will not be applied to the listing.   
  
For a list of possible enumeration values, see [CurrencyCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html).   |  
|  ItemArray.Item.ShippingDetails  
.**ExcludeShipToLocation**  | [string](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string)  | Conditionally,   
[repeatable](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#repeatable): [0..*]  |  Use this field in an Add/Revise/Relist call to specify an international country or region, or a special domestic location, such as 'PO Box' (in US) or 'Packstation' (in DE), to where you will not ship the associated item. Repeat this element in the call request for each location that you want to exclude as a shipping destination for your item.   
  
The exclude ship-to location values are eBay regions and countries. To see the valid exclude ship-to locations for a specified site, call **GeteBayDetails** with **DetailName** set to **ExcludeShippingLocationDetails** , and then look for the **ExcludeShippingLocationDetails.Location** fields in the response. Repeat **GeteBayDetails** for each site on which you list.   
  
This field works in conjunction with **Item.ShipToLocation** s to create a set of international countries and regions to where you will, and will not, ship. You can list a region in the **ShipToLocations** field, then exclude specific countries within that region with this field (for example, you can specify Africa in **ShipToLocations** , yet exclude Chad with a **ExcludeShipToLocation** setting). In addition, if your **ShipToLocations** is `Worldwide`, you can use this field to specify both regions and countries that you want to exclude from your shipping destinations.   
  
**Note:** The **ShipToLocations** and **ShippingDetails.ExcludeShipToLocation** containers are not applicable for motor vehicle listings on the US, CA, or UK marketplaces. If these containers are sent in the request, they are ignored and a warning is returned.  **Note:** Any shipping exclusions specified by this field can be overridden by the eBay International Shipping exclusions toggle located under **Shipping Preferences** in **My eBay**. For more information on eBay International Shipping, see [eBay International Shipping program](https://www.ebay.com/help/selling/shipping-items/setting-shipping-options/ebay-international-shipping-program?id=5348).    
You can specify a default set of locations to where you will not ship in My eBay. If you create an Exclude Ship-To List, it is, by default, in effect when you list items. However, if you specify any value in this field on input, it nullifies the default settings in your Exclude Ship-To List. (If you use **ExcludeShipToLocation** when you list an item, you will need to list all the locations to where you will not ship the associated item, regardless of the default settings in your Exclude Ship-To List.)   
  
Specify `none` in this field to override the default Exclude Ship-To List you might have set up in My eBay and indicate that you do not want to exclude any shipping locations from the respective item listing.   
**Note:** This field will stop being returned in **GetItemTransactions** and **GetSellerTransactions** responses on January 31, 2024.    
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.  
  
**Applicable values** : See [CountryCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CountryCodeType.html)  |  
|  ItemArray.Item.ShippingDetails  
.**GlobalShipping**  | [boolean](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean)  | Conditionally  |  **Note:** The **Global Shipping Program** (GSP) is only available on the UK marketplace. On the US marketplace, the **Global Shipping Program** was replaced by the intermediated international shipping program called **eBay International Shipping**.   
  
**eBay International Shipping** is an account level setting, and no field will need to be set in a add/revise call to enable this setting. As long as the US seller's account is opted in to **eBay International Shipping** , this shipping option will be automatically enabled for all listings where international shipping is available. Even if the US seller is opted into **eBay International Shipping** , that same seller can still also specify individual international shipping service options through the ShippingDetails.InternationalShippingServiceOption container.  In an Add/Revise/Relist call, this boolean field can be included and set to `True` if the seller would like to use eBay's Global Shipping Program for orders that are shipped internationally.   
  
In 'Get' calls, if this field is returned as `True`, it indicates that international shipping through the Global Shipping Program is available for the listing. If this field is returned as `False`, the seller is responsible for shipping the item internationally using one of the specified international shipping service options set for the listing.   
  
When calling **RelistFixedPriceItem** , **RelistItem** , **ReviseFixedPriceItem** or **ReviseItem** , you can omit this field if its value doesn't need to change.   
  
  
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnAttributes, ItemReturnDescription, ReturnAll. Also returned if DetailLevel is not provided on input.   |  
|  ItemArray.Item.ShippingDetails  
.**InternationalShippingServiceOption**  | [InternationalShippingServiceOptionsType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/InternationalShippingServiceOptionsType.html)  | Conditionally,   
[repeatable](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#repeatable): [0..*]  |  Shipping costs and options related to an international shipping service. Unless a fulfillment business policy is being used, at least one **ShippingServiceOptions** or **InternationalShippingServiceOption** container will be required.   
  
If you specify multiple **InternationalShippingServiceOption** nodes, the repeating nodes must be contiguous. That is, you cannot insert other nodes between **InternationalShippingServiceOption** nodes.   
  
All specified domestic and international shipping services must be the same shipping type (for example, Flat versus Calculated).   
  
A seller can offer up to four domestic shipping services and up to five international shipping services. However, if the seller is opted in to the Global Shipping Program or eBay International Shipping, only four other international shipping services may be offered (regardless of whether or not Global Shipping or eBay International Shipping is offered for the listing).   
  
If you specify **ShippingDetails** when you revise or relist an item but you omit **InternationalShippingServiceOption** , eBay will drop the international shipping services (except the Global Shipping Program or eBay International Shipping) from the listing. This may also have unintended side effects, as other fields that depend on this data may be dropped as well. To retain the shipping services and dependent fields when you modify other shipping details, it may be simplest to specify all **ShippingDetails** that you still want to include in the listing.   
  
For **GetItemShipping** , results are filtered: if any service is not available in the buyer's region, it is removed. If no services remain after this filtering, a warning is returned.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll. See [Repeating (unbounded) fields](https://developer.ebay.com/api-docs/user-guides/static/make-a-call/tapi-validation.html#unbounded) for rules regarding repeating instances of a nodes (nodes for which maxOccurs is "unbounded" or is greater than 1).  |  
|  ItemArray.Item.ShippingDetails  
.InternationalShippingServiceOption  
.**ShippingService**  | [token](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#token)  | Conditionally  |  An international shipping service being offered by the seller to ship an item to a buyer. For a list of valid values, call **GeteBayDetails** with **DetailName** set to **ShippingServiceDetails**.   
  
To view the full list of International shipping service options in the response, look for the **ShippingService** fields in the **ShippingServiceDetails** containers that contain a **InternationalService** = `true` field, as this indicates that the **ShippingService** value is an International shipping service option.   
  
The **ShippingServiceDetails.ValidForSellingFlow** flag must also be present. Otherwise, that particular shipping service option is no longer valid and cannot be offered to buyers through a listing.   
  
For flat and calculated shipping.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll. See [GeteBayDetails](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GeteBayDetails.html).   
  
**Applicable values** : See [ShippingServiceCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/ShippingServiceCodeType.html)  |  
|  ItemArray.Item.ShippingDetails  
.InternationalShippingServiceOption  
.**ShippingServiceAdditionalCost**  |  [AmountType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/AmountType.html) ([double](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#double))  | Conditionally  |  The cost of shipping each additional item if the same buyer purchases multiple quantity of the same line item. This field is required when creating a multiple-quantity, fixed-price listing. Generally, the seller will give the buyer a shipping discount if that buyer purchases multiple quantity of the item, so this value should usually be less than the value set for **ShippingServiceCost**.   
  
The value of this field can even be set to `0` if the seller wants to encourage buyers to buy multiple quantity of the item, or it could be that the seller can fit multiple quantities of the line item in a single shipping package, so the seller is just passing this shipping savings onto the buyer. This field is not applicable for single-quantity listings.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   |  
| ItemArray.Item.ShippingDetails  
.InternationalShippingServiceOption  
.**ShippingServiceAdditionalCost**  
[ attribute **currencyID** ]  | [CurrencyCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html)  | Conditionally  |  The cost of shipping each additional item if the same buyer purchases multiple quantity of the same line item. This field is required when creating a multiple-quantity, fixed-price listing. Generally, the seller will give the buyer a shipping discount if that buyer purchases multiple quantity of the item, so this value should usually be less than the value set for **ShippingServiceCost**.   
  
The value of this field can even be set to `0` if the seller wants to encourage buyers to buy multiple quantity of the item, or it could be that the seller can fit multiple quantities of the line item in a single shipping package, so the seller is just passing this shipping savings onto the buyer. This field is not applicable for single-quantity listings.  
  
For a list of possible enumeration values, see [CurrencyCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html).   |  
|  ItemArray.Item.ShippingDetails  
.InternationalShippingServiceOption  
.**ShippingServiceCost**  |  [AmountType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/AmountType.html) ([double](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#double))  | Conditionally  |  The base cost of shipping the item using the shipping service specified in the **ShippingService** field. In the case of a multiple-quantity, fixed-price listing, the **ShippingServiceAdditionalCost** field shows the cost to ship each additional item if the buyer purchases multiple quantity of the same line item.   
  
When returned by **GetItemShipping** , it includes the packaging and handling cost. For flat and calculated shipping.   
  
If a shipping service has been specified (even LocalPickup), **GetItem** returns the shipping service cost, even if the cost is zero. Otherwise, cost is not returned.   
  
If this is for calculated shipping for a listing that has not yet ended, note that the cost cannot be determined until the listing has ended and the buyer has specified a postal code.   
  
For **GetItemShipping** , promotional shipping savings is reflected in the cost, if applicable. If the promotional shipping option is lower than other shipping services being offered, the savings is reflected in the returned shipping cost. The shipping service named Promotional Shipping Service (or whatever is the localized name for it) is included among the shipping services. If the promotional shipping cost is lower than the cost of other shipping services being offered, it is presented first in the list. (The LOWEST shipping service cost is always presented first, regardless of whether there is promotional shipping.)   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll. See [https://developer.ebay.com/api-docs/user-guides/static/trading-user-guide/shipping-types-rates.html](https://developer.ebay.com/devzone/xml/docs/reference/ebay/Shipping%20types).  |  
| ItemArray.Item.ShippingDetails  
.InternationalShippingServiceOption  
.**ShippingServiceCost**  
[ attribute **currencyID** ]  | [CurrencyCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html)  | Conditionally  |  The base cost of shipping the item using the shipping service specified in the **ShippingService** field. In the case of a multiple-quantity, fixed-price listing, the **ShippingServiceAdditionalCost** field shows the cost to ship each additional item if the buyer purchases multiple quantity of the same line item.   
  
When returned by **GetItemShipping** , it includes the packaging and handling cost. For flat and calculated shipping.   
  
If a shipping service has been specified (even LocalPickup), **GetItem** returns the shipping service cost, even if the cost is zero. Otherwise, cost is not returned.   
  
If this is for calculated shipping for a listing that has not yet ended, note that the cost cannot be determined until the listing has ended and the buyer has specified a postal code.   
  
For **GetItemShipping** , promotional shipping savings is reflected in the cost, if applicable. If the promotional shipping option is lower than other shipping services being offered, the savings is reflected in the returned shipping cost. The shipping service named Promotional Shipping Service (or whatever is the localized name for it) is included among the shipping services. If the promotional shipping cost is lower than the cost of other shipping services being offered, it is presented first in the list. (The LOWEST shipping service cost is always presented first, regardless of whether there is promotional shipping.)  
  
For a list of possible enumeration values, see [CurrencyCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html).   |  
|  ItemArray.Item.ShippingDetails  
.InternationalShippingServiceOption  
.**ShippingServicePriority**  | [int](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#int)  | Conditionally  |  This integer value controls the order (relative to other shipping services) in which the corresponding **ShippingService** will appear in the View Item and Checkout page. Sellers can specify up to five international shipping services (with five **InternationalShippingServiceOption** containers), so valid values are 1, 2, 3, 4, and 5. A shipping service with a **ShippingServicePriority** value of `1` appears at the top. Conversely, a shipping service with a **ShippingServicePriority** value of 5 appears at the bottom of a list of five shipping service options. If the Global Shipping Program is enabled on the listing for international shipping, only four additional shipping services may be specified.   
  
If this field is omitted from international shipping service options, the order of the shipping service options in View Item and Checkout pages will be determined by the order that these shipping service options are presented in the request payload of an Add/Revise/Relist call.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   |  
|  ItemArray.Item.ShippingDetails  
.InternationalShippingServiceOption  
.**ShipToLocation**  | [string](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string)  | Conditionally,   
[repeatable](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#repeatable): [0..*]  |  An international location or region to where the item seller will ship the item.   
  
Use **GeteBayDetails** with **DetailName** set to **ShippingLocationDetails** to determine which locations are valid per site. In the **GeteBayDetails** response, look for the ShippingLoca**tionDetails.ShippingLocation** fields.   
  
For the **AddItem** family of calls, this field is required if any international shipping service is specified.   
  
**For GetOrders and GetItemTransactions only:** If using Trading WSDL Version 1019 or above, **ShipToLocation** fields will only be returned to the buyer or seller, and no longer returned at all to third parties. If using a Trading WSDL older than Version 1019, **ShipToLocation** fields are only returned to the buyer or seller, and a string value of `Unavailable` will be returned to all third parties.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll. See [Shipping information](https://developer.ebay.com/api-docs/user-guides/static/trading-user-guide/shipping-info.html).   
  
**Applicable values** : See [CountryCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CountryCodeType.html)  |  
|  ItemArray.Item.ShippingDetails  
.**PaymentEdited**  | [boolean](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean)  | Conditionally  |  Whether the seller allows the buyer to edit the payment amount for the order. (Sellers enable this property in their My eBay user preferences on the eBay site.)   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   |  
|  ItemArray.Item.ShippingDetails  
.**RateTableDetails**  | [RateTableDetailsType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/RateTableDetailsType.html)  | Conditionally  |  This container is used to reference and apply a seller's domestic and/or international shipping rate tables to a listing. Shipping rate tables allow sellers to configure specific shipping costs based on the shipping destinations and level of service (e.g. economy, standard, expedited, and one-day). Generally speaking, sellers want to use these shipping rate tables so they can charge a higher shipping cost to the buyer whenever shipping costs are higher for them as well. For example, shipping to Alaska or Hawaii is generally more expensive than shipping to any other of the 48 US states, or in regards to international shipping, shipping to some regions and countries are more expensive than others.   
  
Sellers configure domestic and international shipping rate tables in My eBay Shipping Preferences. To apply shipping rate tables to a listing, the shipping cost type must be flat-rate.   
  
For domestic shipping rate tables, the three supported domestic regions are Alaska & Hawaii, US Protectorates (e.g. Puerto Rico and Guam), and APO/FPO destinations, which are US military bases/locations outside of the continental US. In addition to setting one flat rate based on the destination and service level, the seller also has the option of adding an extra charge based on the weight of the shipping package, or they can add a surcharge instead. To determine if a domestic shipping rate table is set up for the seller's account, the **GetUser** call can be used, and then the seller will look for a value of `true` in the **User.SellerInfo.DomesticRateTable** field. Although the **GetUser** call can be used to see if a domestic shipping rate table exists for the seller's account, details of the shipping rate table, including all specified costs for the different regions, can only be viewed and modified in My eBay Shipping Preferences. This functionality is not yet available in any public APIs.   
  
For international shipping rate tables, specific rates may be set up for any and all of the nine geographical regions and individual countries within those regions. Similar to domestic shipping rate tables, the seller has the option of adding an extra charge based on the weight of the shipping package. Sellers cannot add a surcharge for international shipping. To determine if a international shipping rate table is set up for the seller's account, the **GetUser** call can be used, and then the seller will look for a value of `true` in the **User.SellerInfo.InternationalRateTable** field. Although the **GetUser** call can be used to see if an international shipping rate table exists for the seller's account, details of the shipping rate table, including all specified costs for the different regions/countries, can only be viewed and modified in My eBay Shipping Preferences. This functionality is not yet available in any public APIs.   
  
If you are applying a domestic or international shipping rate table that specifies a surcharge by weight, you must specify the item weight in the **ShippingPackageDetails** container's **WeightMajor** and **WeightMinor** fields, even though the listing is using flat-rate shipping. Do not use any other fields in the **ShippingPackageDetails** container because none of those fields are applicable in this use case.   
  
This container is only returned in the 'Get' calls if one or more shipping rate tables have been applied to the listing, and if the call is being made by the seller who listed the item.   
  
**Note:** The capability to create and use multiple domestic and international shipping rate tables (up to 40 per seller account) has rolled out to the US, Australia, Canada (English and French), Italy, UK, and Germany sites. For other sites, only one domestic and one international shipping rate table may be set up per seller. Whether a seller is using the old default domestic and international shipping rate tables or the new shipping rate tables, these shipping rate tables are set up in My eBay Shipping Preferences or as part of a Shipping Business Policy. If using the Trading API to create a listing that will use the new shipping rate tables, the **DomesticRateTableId** and **InternationalRateTableId** fields are used to reference and apply these new shipping rate tables to the listing. If desired, sellers can still use the old default shipping rate tables, but they are not allowed to mix and match old and new shipping rate tables, meaning that they will get an error if they pass in both the old fields (**DomesticRateTable** and **InternationalRateTable**) and the new fields (**DomesticRateTableId** and **InternationalRateTableId**). The new shipping rate tables have all of the functionality of the old shipping rate tables, plus the seller has access to all domestic regions and not just the special regions (such as Alaska & Hawaii, US Protectorates, and APO/FPO locations in US).   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll. See [Shipping rate tables](https://developer.ebay.com/api-docs/user-guides/static/trading-user-guide/shipping-rate-tables.html) for more information on using shipping rate tables..  |  
|  ItemArray.Item.ShippingDetails  
.RateTableDetails  
.**DomesticRateTable**  | [string](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string)  | Conditionally  |  This field is used in an Add/Revise/Relist/Verify call to apply the domestic shipping rate table to the listing.   
  
In all cases, sellers pass in a string value of `Default` to apply the domestic shipping rate table. The shipping rates and/or surcharges set up in the domestic shipping rate table will only be applicable based on the location of the buyer, and if that shipping service level is covered in one of the specified shipping service options in the listing. Basically, domestic shipping costs and surcharges are set in one or more **ShippingServiceOptions** containers in the listing, and based on the settings and costs in the domestic shipping rate table, these shipping costs and/or surcharges may be overridden based on the buyer's location. For example, if the buyer lives in Alaska, and the domestic shipping rate table has one or more shipping rates set up for the _Alaska & Hawaii_ domestic region, the buyer will see these rates in the View Item page and not the rates/costs that are defined in the **ShippingServiceOptions** containers.   
  
If a seller is revising or relisting an item, the domestic shipping rate table can be unassociated from the listing by using the empty tag: `<DomesticRateTable />`   
  
This field is returned in the 'Get' calls if a domestic rate table is being applied to the listing, and it is only returned for the seller who listed the item.   
  
**Note:** The capability to create and use multiple domestic and international shipping rate tables (up to 40 per seller account) has rolled out to the US, Australia, Canada (English and French), Italy, UK, and Germany sites. Currently, for sites other than the ones stated, only one domestic and one international shipping rate table may be set up per seller. Until the seller's account is updated with the new shipping rate tables in My eBay, the seller will continue to use the **DomesticRateTable** and **InternationalRateTable** tags and pass in `Default` as the value. Once the seller's account is updated with the new shipping rate tables in My eBay, the seller will be required to use the new **DomesticRateTableId** and **InternationalRateTableId** tags, and the **DomesticRateTable** and **InternationalRateTable** tags will not work. Note that shipping rate tables can also be applied to Shipping business policies that are applied against a listing. The new shipping rate tables have all of the functionality of the old shipping rate tables, plus the seller has access to all domestic regions and not just the special regions (such as Alaska & Hawaii, US Protectorates, and APO/FPO locations in US).  
**Max length:** 50.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll. See [Shipping rate tables](https://developer.ebay.com/api-docs/user-guides/static/trading-user-guide/shipping-rate-tables.html) for more information on using shipping rate tables..  |  
|  ItemArray.Item.ShippingDetails  
.RateTableDetails  
.**DomesticRateTableId**  | [string](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string)  | Conditionally  |  **Note:** This field is only available for sellers on the US, Australia, Canada (English and French), Italy, UK, and Germany sites. The unique shipping rate identifiers that will be passed into this field can be retrieved using the **getRateTables** call of the **Account API** , or these identifiers can be viewed in the displayed URL when the seller selects a specific shipping rate table in the Shipping rate tables UI in My eBay.    
This field is included in an Add/Revise/Relist/Verify call if the seller wants to apply a customized domestic shipping rate table to the listing. The string value that is supplied in this field is the unique identifier of the shipping rate table. If the **DomesticRateTableId** field is used, the seller must make sure that the **DomesticRateTable** and **InternationalRateTable** fields are not used, as the old and new rate tables cannot be used together or an error will occur.   
  
In domestic shipping rate tables, sellers customize the flat-rate cost of shipping based on shipping destination (region/state/province) and shipping service level (one-day, expedited, standard, economy in US). In addition to setting one flat rate based on the destination and service level, the seller also has the option of adding an extra charge based on the weight of the shipping package, or they can add a surcharge instead.   
  
When using a **Revise** or **Relist** call, the seller must include the **DomesticRateTableId** field: 
  * To keep the current domestic shipping rate table, pass the same **DomesticRateTableId**.
  * To switch to a different table, pass the identifier of the desired domestic shipping rate table. 
  * To remove the association, revise or relist the item and send an empty tag: `<DomesticRateTableId />`

This field is returned in the 'Get' calls if a customized domestic rate table is being applied to the listing, and it is only returned for the seller who listed the item.   
  
**Note:** The capability to create and use multiple domestic and international shipping rate tables (up to 40 per seller account) has rolled out to the US, Australia, Canada (English and French), Italy, UK, and Germany sites. For other sites, only one domestic and one international shipping rate table may be set up per seller. Until the seller's account is updated with the new shipping rate tables in My eBay, the seller will continue to use the **DomesticRateTable** and **InternationalRateTable** tags and pass in `Default` as the value. Once the seller's account is updated with the new shipping rate tables in My eBay, the seller will be required to use the new **DomesticRateTableId** and **InternationalRateTableId** tags, and the **DomesticRateTable** and **InternationalRateTable** tags will not work. Note that shipping rate tables can also be applied to Shipping business policies that are applied against a listing. The new shipping rate tables have all of the functionality of the old shipping rate tables, plus the seller has access to all domestic regions and not just the special regions (such as Alaska & Hawaii, US Protectorates, and APO/FPO locations in US).  
**Max length:** 50.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   |  
|  ItemArray.Item.ShippingDetails  
.RateTableDetails  
.**InternationalRateTable**  | [string](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string)  | Conditionally  |  This field is used in an Add/Revise/Relist/Verify call to apply the international shipping rate table to the listing. International shipping rate tables can be used only for items listed on the eBay US, UK, and DE sites.   
  
In all cases, sellers pass in a string value of `Default` to apply the international shipping rate table. The shipping rates set up in the international shipping rate table will only be applicable based on the location of the buyer, and if that shipping service level is covered in one of the specified international shipping service options in the listing. Basically, international shipping costs are set in one or more **InternationalShippingServiceOption** containers in the listing, and based on the settings and costs in the international shipping rate table, these shipping costs may be overridden based on the buyer's location. For example, if the buyer lives in Argentina, and the international shipping rate table has one or more shipping rates set up for the country of _Argentina_ , the buyer will see these rates in the View Item page and not the rates/costs that are defined in the **InternationalShippingServiceOption** containers.   
  
If a seller is revising or relisting an item, the international shipping rate table can be unassociated from the listing by using the empty tag: `<InternationalRateTable />`   
  
This field is returned in the 'Get' calls if an international rate table is being applied to the listing, and it is only returned for the seller who listed the item.   
  
**Note:** The capability to create and use multiple domestic and international shipping rate tables (up to 40 per seller account) has rolled out to the US, Australia, Canada (English and French), Italy, UK, and Germany sites. Currently, for sites other than the ones stated, only one domestic and one international shipping rate table may be set up per seller. Until the seller's account is updated with the new shipping rate tables in My eBay, the seller will continue to use the **DomesticRateTable** and **InternationalRateTable** tags and pass in `Default` as the value. Once the seller's account is updated with the new shipping rate tables in My eBay, the seller will be required to use the new **DomesticRateTableId** and **InternationalRateTableId** tags, and the **DomesticRateTable** and **InternationalRateTable** tags will not work. Note that shipping rate tables can also be applied to Shipping business policies that are applied against a listing. The new shipping rate tables have all of the functionality of the old shipping rate tables, plus the seller has access to all domestic regions and not just the special regions (such as Alaska & Hawaii, US Protectorates, and APO/FPO locations in US).  
**Max length:** 50.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll. See [Shipping rate tables](https://developer.ebay.com/api-docs/user-guides/static/trading-user-guide/shipping-rate-tables.html) for more information on using shipping rate tables..  |  
|  ItemArray.Item.ShippingDetails  
.RateTableDetails  
.**InternationalRateTableId**  | [string](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string)  | Conditionally  |  **Note:** This field is only available to sellers on specific sites. See [Marketplace support](https://developer.ebay.com/api-docs/user-guides/static/trading-user-guide/shipping-rate-tables.html#marketplaces) for a list of marketplaces that support International shipping rate tables. The unique shipping rate identifiers that will be passed into this field can be retrieved using the **getRateTables** call of the **Account API** , or these identifiers can be viewed in the displayed URL when the seller selects a specific shipping rate table in the Shipping rate tables UI in My eBay.    
This field is included in an Add/Revise/Relist/Verify call if the seller wants to apply a customized international shipping rate table to the listing. The string value that is supplied in this field is the unique identifier of the shipping rate table. If the **InternationalRateTableId** field is used, the seller must make sure that the **DomesticRateTable** and **InternationalRateTable** fields are not used, as the old and new rate tables cannot be used together or an error will occur.   
  
In international shipping rate tables, sellers customize the flat-rate cost of shipping based on shipping destination (continent/region/country) and shipping service level (expedited, standard, economy in US). In addition to setting one flat rate based on the destination and service level, the seller also has the option of adding an extra charge based on the weight of the shipping package. Unlike domestic shipping, sellers cannot add a surcharge for international shipping.   
  
When using a **Revise** or **Relist** call, the seller must include the **InternationalRateTableId** field: 
  * To keep the current international shipping rate table, pass the same **InternationalRateTableId**.
  * To switch to a different table, pass the identifier of the desired international shipping rate table. 
  * To remove the association, revise or relist the item and send an empty tag: `<InternationalRateTableId />`

This field is returned in the 'Get' calls if a customized international rate table is being applied to the listing, and it is only returned for the seller who listed the item.   
  
**Note:** The capability to create and use multiple domestic and international shipping rate tables (up to 40 per seller account) has rolled out to the US, Australia, Canada (English and French), Italy, UK, and Germany sites. For other sites, only one domestic and one international shipping rate table may be set up per seller. Until the seller's account is updated with the new shipping rate tables in My eBay, the seller will continue to use the **DomesticRateTable** and **InternationalRateTable** tags and pass in `Default` as the value. Once the seller's account is updated with the new shipping rate tables in My eBay, the seller will be required to use the new **DomesticRateTableId** and **InternationalRateTableId** tags, and the **DomesticRateTable** and **InternationalRateTable** tags will not work. Note that shipping rate tables can also be applied to Shipping business policies that are applied against a listing. The new shipping rate tables have all of the functionality of the old shipping rate tables, plus the seller has access to all domestic regions and not just the special regions (such as Alaska & Hawaii, US Protectorates, and APO/FPO locations in US).  
**Max length:** 50.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   |  
|  ItemArray.Item.ShippingDetails  
.**SalesTax**  | [SalesTaxType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/SalesTaxType.html)  | Conditionally  |  This container shows sales tax information for an item in a specific tax jurisdiction. The concept of 'sales tax' is only applicable to eBay US and Canada (English and French) sites.   
  
This container can be used in an Add/Revise/Relist/Verify call to set sales tax settings for a specific tax jurisdiction, but it is actually a better practice if a user sets up sales tax rates through the Sales Tax Table tool in My eBay (or by using the **SetTaxTable** call). A seller's Sales Tax Table is applied to the listing by including the **UseTaxTable** field in the request and setting its value to `true`. The **GetTaxTable** call can be used to retrieve the current sales tax rates for different tax jurisdictions.   
  
This container is only returned in order management 'Get' calls if sales tax is applicable to the order line item. For eBay Collect and Remit states, the sales tax information is displayed in the **Transaction.Taxes** container instead.   
  
**Note:** Buyers in all 50 US states and DC are automatically charged sales tax for eBay purchases, and eBay collects and remits this sales tax to the proper taxing authority on the buyer's behalf. Because of this, if a sales tax percentage rate is applied to a listing by a seller in one of these states, this field will be ignored during the checkout process.   
  
Currently, sales tax percentage rates can only be specified by sellers in Canada and 5 US territories, including American Samoa (AS), Guam (GU), Northern Mariana Islands (MP), Palau (PW), and Virgin Islands (VI).    
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine. See [Multi-jurisdiction sales tax](https://developer.ebay.com/api-docs/user-guides/static/trading-user-guide/taxes.html).  |  
|  ItemArray.Item.ShippingDetails  
.SalesTax.**SalesTaxPercent**  | [float](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#float)  | Conditionally  |  This float value is the sales tax percentage rate applicable to the corresponding tax jurisdiction (US state or Canadian province). Sellers are responsible for providing accurate sales tax rates for each jurisdiction. This sales tax rate comes into play when a buyer from that tax jurisdiction makes a purchase from the seller. The value passed in is stored with a precision of 3 digits after the decimal point (##.###).   
  
This field is only returned in order management calls if sales tax applies to the order line item, and is only in **GetItem** (and other 'Get' calls) if sales tax is applicable to the listing or order line item, and the seller is the person making the call.   
  
Although this field will be returned at the order level in order management calls for a single line item order, sales tax is applied at the line item level and not order level. For multiple line item orders, this field will not be returned at all at the order level.   
  
**Note:** Buyers in all 50 US states and DC are automatically charged sales tax for eBay purchases, and eBay collects and remits this sales tax to the proper taxing authority on the buyer's behalf. Because of this, if a sales tax percentage rate is applied to a listing by a seller in one of these states, this field will be ignored during the checkout process.   
  
Currently, sales tax percentage rates can only be specified by sellers in Canada and 5 US territories, including American Samoa (AS), Guam (GU), Northern Mariana Islands (MP), Palau (PW), and Virgin Islands (VI).    
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine.   |  
|  ItemArray.Item.ShippingDetails  
.SalesTax.**SalesTaxState**  | [string](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string)  | Conditionally  |  This is the unique, two-digit identifier of the tax jurisdiction (such as 'CA' for California). To retrieve all two-digit identifiers for all states/territories/provinces for a site, a seller can either use a **GetTaxTable** call with **DetailLevel** set to `ReturnAll`, or they can use the **GeteBayDetails** call with **DetailLevel** name set to `TaxJurisdiction`. Please note that both **GetTaxTable** and **GeteBayDetails** calls use a **JurisdictionID** field to express these tax jurisdiction identifiers instead of **SalesTaxState** , but the values used in these fields are the same.   
  
The **SalesTaxState** field is conditionally required in an Add/Revise/Relist/Verify call if the seller is applying sales tax to a listing for a particular jurisdiction, and is returned with each **SalesTax** container to identify the tax jurisdiction.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   |  
|  ItemArray.Item.ShippingDetails  
.SalesTax  
.**ShippingIncludedInTax**  | [boolean](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean)  | Conditionally  |  This field is included in an Add/Revise/Relist/Verify call and set to `true` if the seller wants sales tax for the jurisdiction to apply to the cumulative amount of item cost and shipping charges. This value defaults to `false` if not specified.   
  
This field is always returned with the **SalesTax** container (whether `true` or `false`).   
  
**Note:** Buyers in all 50 US states and DC are automatically charged sales tax for eBay purchases, and eBay collects and remits this sales tax to the proper taxing authority on the buyer's behalf. Because of this, if a sales tax percentage rate is applied to a listing by a seller in one of these states, this field will be ignored during the checkout process.   
  
Currently, sales tax percentage rates can only be specified by sellers in Canada and 5 US territories, including American Samoa (AS), Guam (GU), Northern Mariana Islands (MP), Palau (PW), and Virgin Islands (VI).    
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine.   |  
|  ItemArray.Item.ShippingDetails  
.**SellerExcludeShipToLocationsPreference**  | [boolean](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean)  | Conditionally  |  Sellers can set up a global Exclude Ship-To List through their My eBay account. This list defines the countries to which the seller does not ship by default.   
  
This field returns `true` when the listing does not have an item-level Exclude Ship-To List that is newer than the seller's My eBay Exclude Ship-To List. This includes listings with no item-level Exclude Ship-To List, including cases where the seller has no My eBay Exclude Ship-To List and did not specify **ExcludeShipToLocation**.   
  
This field returns `false` when the listing has an item-level Exclude Ship-To List that is newer than the seller's My eBay Exclude Ship-To List. An item-level list can be stored when the seller specifies **ExcludeShipToLocation** in an Add, Relist, or Revise request, or when the seller omits **ExcludeShipToLocation** and the seller's My eBay Exclude Ship-To List is applied at listing time.   
  
A value of `false` does not mean that shipping exclusions were not applied. A value of `true` does not by itself mean that a My eBay Exclude Ship-To List exists.   
  
In the response, **ExcludeShipToLocation** fields list the locations to which the seller will not ship the item, regardless of the value of this field.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine.   |  
|  ItemArray.Item.ShippingDetails  
.**ShippingServiceOptions**  | [ShippingServiceOptionsType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/ShippingServiceOptionsType.html)  | Conditionally,   
[repeatable](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#repeatable): [0..*]  |  This container is used to provide details on a specific domestic shipping service option, including the unique identifier of the shipping service option and the costs related to domestic shipping service. A separate **ShippingServiceOptions** container is needed for each domestic shipping service option that is available to ship the item. Unless a fulfillment business policy is being used, at least one **ShippingServiceOptions** or **InternationalShippingServiceOption** container will be required.   
  
If you specify multiple **ShippingServiceOptions** nodes, the repeating nodes must be contiguous. For example, you can insert **InternationalShippingServiceOption** nodes after a list of repeating **ShippingServiceOptions** nodes, but not between them:   
  
` <ShippingServiceOptions>...</ShippingServiceOptions>  
 <ShippingServiceOptions>...</ShippingServiceOptions>  
 <ShippingServiceOptions>...</ShippingServiceOptions>  
 <InternationalShippingServiceOption>...</InternationalShippingServiceOption>  
 <InternationalShippingServiceOption>...</InternationalShippingServiceOption> `   
  
If you specify **ShippingDetails** when you revise or relist an item but you omit **ShippingServiceOptions** , eBay will drop the domestic shipping services from the listing. This may also have unintended side effects, as other fields that depend on this data may be dropped as well.   
  
To retain the shipping services and dependent fields when you modify other shipping details, it may be simplest to specify all **ShippingDetails** that you still want to include in the listing.   
  
A seller can offer up to four domestic shipping services and up to five international shipping services. However, if the seller is opted in to the Global Shipping Program or eBay International Shipping, only four other international shipping services may be offered (regardless of whether or not Global Shipping shipment or eBay International Shipping is offered for the listing). All specified domestic and international shipping services must be the same shipping type (for example, Flat versus Calculated).   
  
**Note:** If the seller has set the shipping cost model to 'Flat' or 'Calculated' (**ShippingDetails.ShippingType** field), at least one actual shipping service option must be specified through a **ShippingServiceOptions** container. In the past, eBay allowed users to set the shipping cost model to 'Flat' or 'Calculated', and then just pass in one **ShippingServiceOptions** container with the **ShippingServiceOptions.ShipppingService** value set to a 'Local Pickup' option. Now, sellers must pass in at least one actual domestic shipping service option in addition to any 'Local Pickup' option, or the listing will be blocked with the following error: _17510 - You must specify at least one domestic shipping service, other than or in addition to Local Pickup._   
For **GetItemShipping** , results are filtered: if any service is not available in the buyer's region, it is removed. If no services remain after this filtering, a warning is returned.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll. See [Repeating (unbounded) fields](https://developer.ebay.com/api-docs/user-guides/static/make-a-call/tapi-validation.html#unbounded) for rules regarding repeating instances of a nodes (nodes for which maxOccurs is "unbounded" or is greater than 1).  |  
|  ItemArray.Item.ShippingDetails  
.ShippingServiceOptions  
.**ExpeditedService**  | [boolean](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean)  | Conditionally  |  This field is returned as `true` if the domestic shipping service is considered an expedited shipping service. An expedited service is typically a shipping service that can ship an order that will arrive at the buyer's location within one to two business days.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   |  
|  ItemArray.Item.ShippingDetails  
.ShippingServiceOptions  
.**ShippingService**  | [token](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#token)  | Conditionally  |  This enumeration value indicates a specific domestic shipping service option being offered by the seller to ship an item to a buyer who is located within the same country as the item. This field is required to identify each domestic shipping service option that is specified with a **ShippingServiceOptions** container.   
  
For a list of valid **ShippingService** values, call **GeteBayDetails** with **DetailName** set to `ShippingServiceDetails`. The **ShippingServiceDetails.ValidForSellingFlow** flag must also be present. Otherwise, that particular shipping service option is no longer valid and cannot be offered to buyers through a listing.  
  
To view the full list of domestic shipping service options in the response, look for the **ShippingServiceDetails.ShippingService** fields. Domestic shipping service options will not have a **InternationalService** = `true` field, as this indicates that the **ShippingService** value is an International shipping service option.  
  
**Note:** The eBay standard envelope (eSE) is a domestic envelope service with tracking through eBay. This service applies to specific sub-categories of **Trading Cards** , and to coins & paper money, postcards, stamps, patches, and similar [eligible categories](https://www.ebay.com/sellercenter/shipping/choosing-a-carrier-and-service/ebay-standard-envelope#eligible-categories), and is only available on the US marketplace. See [eBay standard envelope](https://pages.ebay.com/seller-center/shipping/ebay-standard-envelope.html#lower-cost-way) for details, restrictions, and an [envelope size template](https://ir.ebaystatic.com/pictures/sc/Shipping/ebay_standard_envelope_template.pdf). To use this service, send envelopes using the USPS mail and set the **ShippingService** field to `US_eBayStandardEnvelope`.   
  
For the REST equivalent, see [Using the eBay standard envelope (eSE) service](https://developer.ebay.com/api-docs/sell/static/seller-accounts/using-the-ebay-standard-envelope-service.html).    
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll. See [GeteBayDetails](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GeteBayDetails.html).   
  
**Applicable values** : See [ShippingServiceCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/ShippingServiceCodeType.html)  |  
|  ItemArray.Item.ShippingDetails  
.ShippingServiceOptions  
.**ShippingServiceAdditionalCost**  |  [AmountType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/AmountType.html) ([double](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#double))  | Conditionally  |  The cost of shipping each additional item if the same buyer purchases multiple quantity of the same line item. This field is required when creating a multiple-quantity, fixed-price listing. Generally, the seller will give the buyer a shipping discount if that buyer purchases multiple quantity of the item, so this value should usually be less than the value set for **ShippingServiceCost**.   
  
The value of this field can even be set to `0` if the seller wants to encourage buyers to buy multiple quantity of the item, or it could be that the seller can fit multiple quantities of the line item in a single shipping package, so the seller is just passing this shipping savings onto the buyer. This field is not applicable for single-quantity listings.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   |  
| ItemArray.Item.ShippingDetails  
.ShippingServiceOptions  
.**ShippingServiceAdditionalCost**  
[ attribute **currencyID** ]  | [CurrencyCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html)  | Conditionally  |  The cost of shipping each additional item if the same buyer purchases multiple quantity of the same line item. This field is required when creating a multiple-quantity, fixed-price listing. Generally, the seller will give the buyer a shipping discount if that buyer purchases multiple quantity of the item, so this value should usually be less than the value set for **ShippingServiceCost**.   
  
The value of this field can even be set to `0` if the seller wants to encourage buyers to buy multiple quantity of the item, or it could be that the seller can fit multiple quantities of the line item in a single shipping package, so the seller is just passing this shipping savings onto the buyer. This field is not applicable for single-quantity listings.  
  
For a list of possible enumeration values, see [CurrencyCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html).   |  
|  ItemArray.Item.ShippingDetails  
.ShippingServiceOptions  
.**ShippingServiceCost**  |  [AmountType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/AmountType.html) ([double](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#double))  | Conditionally  |  The base cost of shipping one unit of the item using the shipping service specified in the corresponding **ShippingService** field.   
  
In the case of a multiple-quantity, fixed-price listing, the **ShippingServiceAdditionalCost** field also becomes applicable, and shows the cost to ship each additional unit of the item if the buyer purchases multiple quantity of the same line item.   
  
**Note:** If the corresponding shipping service option is set as a 'free shipping' option (**FreeShipping** set to `true`) and flat-rate shipping is being used domestically (**ShippingType** is set to `Flat` or `FlatDomesticCalculatedInternational`), the seller must still include this **ShippingServiceCost** field and set its value to `0.0`, as eBay will not do this automatically. Do not include **ShippingServiceCost** when the domestic shipping service option is set to represent domestic calculated shipping (**ShippingType** is set to `Calculated` or `CalculatedDomesticFlatInternational`), as error 10019 occurs.    
When returned by **GetItemShipping** , it includes the packaging and handling cost.   
  
Note that if **ShippingService** is set to `LocalPickup`, **ShippingServiceCost** must be set to `0.0`. Also, if a shipping service has been specified (even **LocalPickup**), **GetItem** returns the shipping service cost, even if the cost is zero.   
  
If this is for calculated shipping for a listing that has not yet ended, note that the cost cannot be determined until the listing has ended and the buyer has specified a postal code.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   |  
| ItemArray.Item.ShippingDetails  
.ShippingServiceOptions  
.**ShippingServiceCost**  
[ attribute **currencyID** ]  | [CurrencyCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html)  | Conditionally  |  The base cost of shipping one unit of the item using the shipping service specified in the corresponding **ShippingService** field.   
  
In the case of a multiple-quantity, fixed-price listing, the **ShippingServiceAdditionalCost** field also becomes applicable, and shows the cost to ship each additional unit of the item if the buyer purchases multiple quantity of the same line item.   
  
**Note:** If the corresponding shipping service option is set as a 'free shipping' option (**FreeShipping** set to `true`) and flat-rate shipping is being used domestically (**ShippingType** is set to `Flat` or `FlatDomesticCalculatedInternational`), the seller must still include this **ShippingServiceCost** field and set its value to `0.0`, as eBay will not do this automatically. Do not include **ShippingServiceCost** when the domestic shipping service option is set to represent domestic calculated shipping (**ShippingType** is set to `Calculated` or `CalculatedDomesticFlatInternational`), as error 10019 occurs.    
When returned by **GetItemShipping** , it includes the packaging and handling cost.   
  
Note that if **ShippingService** is set to `LocalPickup`, **ShippingServiceCost** must be set to `0.0`. Also, if a shipping service has been specified (even **LocalPickup**), **GetItem** returns the shipping service cost, even if the cost is zero.   
  
If this is for calculated shipping for a listing that has not yet ended, note that the cost cannot be determined until the listing has ended and the buyer has specified a postal code.  
  
For a list of possible enumeration values, see [CurrencyCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html).   |  
|  ItemArray.Item.ShippingDetails  
.ShippingServiceOptions  
.**ShippingServicePriority**  | [int](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#int)  | Conditionally  |  Controls the order (relative to other shipping services) in which the corresponding **ShippingService** will appear in the View Item and Checkout page.   
  
Sellers can specify up to four domestic shipping services (with four **ShippingServiceOptions** containers), so valid values are 1, 2, 3, and 4. A shipping service with a **ShippingServicePriority** value of 1 appears at the top. Conversely, a shipping service with a **ShippingServicePriority** value of 4 appears at the bottom of a list of four shipping service options.   
  
If this field is omitted from domestic shipping service options, the order of the shipping service options in View Item and Checkout pages will be determined by the order that these shipping service options are presented in the request payload of an Add/Revise/Relist call.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   |  
|  ItemArray.Item.ShippingDetails  
.ShippingServiceOptions  
.**ShippingTimeMax**  | [int](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#int)  | Conditionally  |  The integer value returned here indicates the maximum number of business days that the shipping service (indicated in the corresponding **ShippingService** field) will take to be delivered to the buyer.   
  
This maximum shipping time does not include the seller's handling time, and the clock starts on the shipping time only after the seller has delivered the item to the shipping carrier for shipment to the buyer. 'Business days' can vary by shipping carrier and by country, but 'business days' are generally Monday through Friday, excluding holidays. This field is returned if defined for that particular shipping service option.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   |  
|  ItemArray.Item.ShippingDetails  
.ShippingServiceOptions  
.**ShippingTimeMin**  | [int](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#int)  | Conditionally  |  The integer value returned here indicates the minimum number of business days that the shipping service (indicated in the corresponding **ShippingService** field) will take to be delivered to the buyer.   
  
This minimum shipping time does not include the seller's handling time, and the clock starts on the shipping time only after the seller has delivered the item to the shipping carrier for shipment to the buyer. 'Business days' can vary by shipping carrier and by country, but 'business days' are generally Monday through Friday, excluding holidays. This field is returned if defined for that particular shipping service option.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   |  
|  ItemArray.Item.ShippingDetails  
.**TaxTable**  | [TaxTableType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/TaxTableType.html)  | Conditionally  |  Tax details for a jurisdiction, such as a state or province. If no tax table is associated with the item, a tax table is not returned.   
  
For **GetItem** , a tax table is returned if it exists when: 
  * **DetailLevel** is set to `ReturnAll` or **ItemReturnDescription** (in this case, the value of **IncludeTaxTable** does not matter)
  * **IncludeTaxTable** is set to `true` and **DetailLevel** is not set or it is set to `ItemReturnAttributes`

  
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Coarse, Fine, Medium.   |  
|  ItemArray.Item.ShippingDetails  
.TaxTable.**TaxJurisdiction**  | [TaxJurisdictionType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/TaxJurisdictionType.html)  | Conditionally,   
[repeatable](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#repeatable): [0..*]  |  In a **SetTaxTable** , a **TaxJurisdiction** container is required for each tax jurisdiction that the seller wishes to make additions/changes. Sales tax details for zero or more jurisdictions (states, provinces, etc). This can be just one jurisdiction, up to all jurisdictions defined for the site's country. Any values specified through a **TaxJurisdiction** container will override any existing values defined in the seller's Sales Tax Table.   
  
If **GetTaxTable** is called without the **DetailLevel** field, only tax jurisdictions where sales tax rates have been set up are returned. However, if the **DetailLevel** field is included in the request and set to `ReturnAll`, all tax jurisdictions are returned, regardless of whether or not the seller has modified settings for any/all of these jurisdictions.   
  
This container is only returned in order-related 'Get' calls if sales tax is applicable to the order line item.   
  
**Note:** Buyers in all 50 US states and DC are automatically charged sales tax for eBay purchases, and eBay collects and remits this sales tax to the proper taxing authority on the buyer's behalf. Because of this, if a sales tax percentage rate is applied to a listing by a seller in one of these states, this field will be ignored during the checkout process.   
  
Currently, sales tax percentage rates can only be specified by sellers in Canada and 5 US territories, including American Samoa (AS), Guam (GU), Northern Mariana Islands (MP), Palau (PW), and Virgin Islands (VI).    
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   |  
|  ItemArray.Item.ShippingDetails  
.TaxTable.TaxJurisdiction  
.**JurisdictionID**  | [string](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string)  | Conditionally  |  This is the unique, two-digit identifier of the tax jurisdiction (such as 'CA' for California). To retrieve all **JurisdictionID** values for a site, a seller can either use a **GetTaxTable** call with **DetailLevel** set to `ReturnAll`, or they can use the **GeteBayDetails** call with **DetailLevel** name set to `TaxJurisdiction`.   
  
The **JurisdictionID** field is always required in a **SetTaxTable** call, and always returned with each **TaxJurisdiction** container to identify the tax jurisdiction.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ReturnAll. Also returned if DetailLevel is not provided on input.   |  
|  ItemArray.Item.ShippingDetails  
.TaxTable.TaxJurisdiction  
.**SalesTaxPercent**  | [float](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#float)  | Conditionally  |  This float value is the sales tax percentage rate applicable to the corresponding tax jurisdiction. Sellers are responsible for providing accurate sales tax rates for each jurisdiction. This sales tax rate comes into play when a buyer from that tax jurisdiction makes a purchase from the seller. The value passed in is stored with a precision of 3 digits after the decimal point (##.###).   
  
This field is only returned in **GetTaxTable** (and other 'Get' calls) if a sales tax percentage rate has been set.   
  
**Note:** Buyers in all 50 US states and DC are automatically charged sales tax for eBay purchases, and eBay collects and remits this sales tax to the proper taxing authority on the buyer's behalf. Because of this, if a sales tax percentage rate is applied to a listing by a seller in one of these states, this field will be ignored during the checkout process.   
  
Currently, sales tax percentage rates can only be specified by sellers in Canada and 5 US territories, including American Samoa (AS), Guam (GU), Northern Mariana Islands (MP), Palau (PW), and Virgin Islands (VI).    
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ReturnAll. Also returned if DetailLevel is not provided on input.   |  
|  ItemArray.Item.ShippingDetails  
.TaxTable.TaxJurisdiction  
.**ShippingIncludedInTax**  | [boolean](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean)  | Conditionally  |  This field is included in a **SetTaxTable** call and set to `true` if the seller wants sales tax for the jurisdiction to apply to the cumulative amount of item cost and shipping charges. This value defaults to `false` if not specified.   
  
This field is always returned with each **TaxJurisdiction** container (whether `true` or `false`).   
  
**Note:** Buyers in all 50 US states and DC are automatically charged sales tax for eBay purchases, and eBay collects and remits this sales tax to the proper taxing authority on the buyer's behalf. Because of this, if a sales tax percentage rate is applied to a listing by a seller in one of these states, this field will be ignored during the checkout process.   
  
Currently, sales tax percentage rates can only be specified by sellers in Canada and 5 US territories, including American Samoa (AS), Guam (GU), Northern Mariana Islands (MP), Palau (PW), and Virgin Islands (VI).    
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ReturnAll. Also returned if DetailLevel is not provided on input.   |  
|  ItemArray.Item.ShippingDetails  
.**ThirdPartyCheckout**  | [boolean](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean)  | Conditionally  |    
**Note:** This field is deprecated and will stop being returned in **GetItemTransactions** and **GetSellerTransactions** on January 31, 2024.    
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine.   |  
|  ItemArray.Item  
.**ShippingServiceCostOverrideList**  | [ShippingServiceCostOverrideListType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/ShippingServiceCostOverrideListType.html)  | Conditionally  |  This container is used when the seller wants to override the flat shipping costs for all domestic and/or all international shipping services defined in the shipping business policy referenced in the **SellerProfiles.SellerShippingProfile.ShippingProfileID** field. Shipping costs include the cost to ship one item, the cost to ship each additional identical item, and any shipping surcharges applicable to domestic shipping services.   
  
A **ShippingServiceCostOverrideList.ShippingServiceCostOverride** container is required for each domestic and/or international shipping service that is defined in the **domesticShippingPolicyInfoService** and **intlShippingPolicyInfoService** containers of the shipping business policy.   
**Note:** To make sure that the shipping cost override and policies are set correctly on an item (that is using business policies and has one or more shipping service cost overrides set up), the **Item.SellerProfiles.SellerShippingProfile** container and the **Item.ShippingServiceCostOverrideList.ShippingServiceCostOverride** container(s) must be included, even if no changes are being made.  Shipping service cost overrides are a listing-level concept, and the shipping costs specified through each **ShippingServiceCostOverrideList.ShippingServiceCostOverride** container will not change the shipping costs defined for the same shipping services in the shipping business policy.   
  
**For Revise and Relist calls** : To delete all shipping service cost overrides when you revise or relist, specify **Item.ShippingServiceCostOverrideList** in **DeletedField** , and don't pass **ShippingServiceCostOverrideList** in the request.   |  
|  ItemArray.Item  
.ShippingServiceCostOverrideList  
.**ShippingServiceCostOverride**  | [ShippingServiceCostOverrideType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/ShippingServiceCostOverrideType.html)  | Conditionally,   
[repeatable](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#repeatable): [0..*]  |  A **ShippingServiceCostOverride** container is required for each domestic and/or international shipping service option, defined in the **domesticShippingPolicyInfoService** and **intlShippingPolicyInfoService** containers of the Business Policies shipping profile, that the seller wishes to override the shipping costs. Shipping costs include the cost to ship one item, the cost to ship each additional identical item, and any shipping surcharges applicable to domestic shipping services.   
  
Shipping service cost overrides are a listing-level concept, and the shipping costs specified through each **ShippingServiceCostOverride** container will not change the shipping costs defined for the same shipping service options in the Business Policies shipping profile.   
  
To override the shipping costs for any domestic shipping service option in the Business Policies shipping profile, the **ShippingServiceType** field should be set to 'Domestic', and to override the shipping costs for any international shipping service option, the **ShippingServiceType** field should be set to 'International'. For both domestic and international shipping services, the **ShippingServicePriority** value should match the **sortOrderId** value for the matching shipping service in the shipping profile. If any of the domestic and/or international shipping service priorities and shipping service options in the Add/Revise/Relist call and Business Policies shipping profile do not match, an error occurs.   
  
If shipping service cost overrides are used in a listing, the **ShippingServiceCostOverride** container will be returned in the **GetItem** , and **GetSellerList** calls.   |  
|  ItemArray.Item  
.ShippingServiceCostOverrideList  
.ShippingServiceCostOverride  
.**ShippingServiceAdditionalCost**  |  [AmountType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/AmountType.html) ([double](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#double))  | Conditionally  |  This dollar value indicates the cost to ship each additional identical item to the buyer. If the shipping service costs override operation is successful, this value will override the corresponding **shippingServiceAdditionalCost** value set in the **domesticShippingPolicyInfoService** (domestic shipping service) or **intlShippingPolicyInfoService** (international shipping service) containers in the Business Policies shipping profile.   
  
This field is only applicable to multi-quantity, fixed-price listings.   |  
| ItemArray.Item  
.ShippingServiceCostOverrideList  
.ShippingServiceCostOverride  
.**ShippingServiceAdditionalCost**  
[ attribute **currencyID** ]  | [CurrencyCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html)  | Conditionally  |  This dollar value indicates the cost to ship each additional identical item to the buyer. If the shipping service costs override operation is successful, this value will override the corresponding **shippingServiceAdditionalCost** value set in the **domesticShippingPolicyInfoService** (domestic shipping service) or **intlShippingPolicyInfoService** (international shipping service) containers in the Business Policies shipping profile.   
  
This field is only applicable to multi-quantity, fixed-price listings.  
  
For a list of possible enumeration values, see [CurrencyCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html).   |  
|  ItemArray.Item  
.ShippingServiceCostOverrideList  
.ShippingServiceCostOverride  
.**ShippingServiceCost**  |  [AmountType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/AmountType.html) ([double](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#double))  | Conditionally  |  This dollar value indicates the shipping service cost to ship one item to the buyer. If the shipping service costs override operation is successful, this value will override the corresponding **shippingServiceCost** value set in the **domesticShippingPolicyInfoService** (domestic shipping service) or **intlShippingPolicyInfoService** (international shipping service) containers in the Business Policies shipping profile.   |  
| ItemArray.Item  
.ShippingServiceCostOverrideList  
.ShippingServiceCostOverride  
.**ShippingServiceCost**  
[ attribute **currencyID** ]  | [CurrencyCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html)  | Conditionally  |  This dollar value indicates the shipping service cost to ship one item to the buyer. If the shipping service costs override operation is successful, this value will override the corresponding **shippingServiceCost** value set in the **domesticShippingPolicyInfoService** (domestic shipping service) or **intlShippingPolicyInfoService** (international shipping service) containers in the Business Policies shipping profile.  
  
For a list of possible enumeration values, see [CurrencyCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html).   |  
|  ItemArray.Item  
.ShippingServiceCostOverrideList  
.ShippingServiceCostOverride  
.**ShippingServicePriority**  | [int](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#int)  | Conditionally  |  This integer value maps the particular instance of the **ShippingServiceCostOverride** container to the **domesticShippingPolicyInfoService** or **intlShippingPolicyInfoService** container of the Business Policies shipping profile. The **ShippingServicePriority** value should match the **sortOrderId** value for the matching shipping service in the Business Policies shipping profile. If overriding the shipping costs for a domestic shipping service, the **ShippingServiceType** field should be set to 'Domestic', and to override the shipping costs for an international shipping service, the **ShippingServiceType** field should be set to 'International'.   
  
If any of the domestic and/or international shipping service priorities and shipping service options in the Add/Revise/Relist call and Business Policies shipping profile do not match, an error occurs.   |  
|  ItemArray.Item  
.ShippingServiceCostOverrideList  
.ShippingServiceCostOverride  
.**ShippingServiceType**  | [ShippingServiceType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/ShippingServiceType.html)  | Conditionally  |  This enumerated value indicates whether the shipping costs of a domestic or an international shipping costs are being overridden. To override the shipping costs for any domestic shipping service in the Business Policies shipping profile, this field should be set to 'Domestic', and to override the shipping costs for any international shipping service, this field should be set to 'International'.   
  
**Applicable values** :   
  


Domestic
    (in/out) This value should be used if the seller is overriding shipping costs for all domestic shipping services defined in the Business Policies shipping profile. 

International
    (in/out) This value should be used if the seller is overriding shipping costs for all international shipping services defined in the Business Policies shipping profile.   
Code so that your app gracefully handles any future changes to this list.   |  
|  ItemArray.Item.**ShipToLocations**  | [string](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string)  | Conditionally,   
[repeatable](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#repeatable): [0..*]  |  An international location or region to which the seller is willing to ship, regardless of shipping service. The country of the listing site is added by eBay.   
  
**Note:** For sellers who are using a shipping (aka Fulfillment) business policy to create/revise/relist an item, the **ShipToLocations** field should not be used in the request. A fulfillment business policy can be set up and/or modified in My eBay, or via the [Account API](https://developer.ebay.com/api-docs/sell/account/resources/fulfillment_policy/methods/createFulfillmentPolicy). A fulfillment business policy is associated to a listing through the **Item.SellerProfiles.SellerShippingProfile** container.    
Use **GeteBayDetails** with a **DetailName** of **ShippingLocationDetails** to determine which international locations are valid for the site. Omit **ShipToLocations** if you want to ship only within the country of the listing site. To state that you do not wish to ship at all, set **ShipToLocations** to `None`. **ReviseItem** can add a **ShipToLocations**. On output, **ShipToLocations** is the collection of all input item-level **ShipToLocations** plus international shipping service-level ShipToLocation values.   
  
**Note:** The **ShipToLocations** and **ShippingDetails.ExcludeShipToLocation** containers are not applicable for motor vehicle listings on the US, CA, or UK marketplaces. If these containers are sent in the request, they are ignored and a warning is returned.    
If you have specified a region to which you will ship (such as Asia), you can use **ExcludeShipToLocation** to exclude certain countries within that region to where you will not ship (such as Afghanistan).   
  
**Note:** To create a listing that is 'Local Pickup only' (buyer picks up, with no shipping/delivery available), the user does the following two things: 
  * Either omit the entire **ShippingDetails** container, or pass in an empty **ShippingDetails** container - <ShippingDetails/>
  * Pass in one **ShipToLocations** field, with its value set to `None` - <ShipToLocations>None</ShipToLocations>

  
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Coarse, Fine, Medium. See:   
[Shipping information](https://developer.ebay.com/api-docs/user-guides/static/trading-user-guide/shipping-info.html)   
[GeteBayDetails](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html)   
  
**Applicable values** : See [CountryCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CountryCodeType.html)  |  
|  ItemArray.Item.**Site**  | [SiteCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/SiteCodeType.html)  | Conditionally  |  The name of the eBay listing site. The listing site affects the business logic and validation rules that are applied to the request, which in turn affect the values that are returned in the response, as well as values that appear on the eBay site. For example, the listing site can affect the validation of **Category** in listing requests, international business seller requirements, the values of converted (localized) prices in responses, the item-related time stamps that are displayed on the eBay site, the visibility of the item in some types of searches (e.g., **GetCategoryListings**), and other information. In some cases, the rules are determined by a combination of the site, the user's registration address, and other information. You cannot change the site when you revise a listing.  
  
When you specify **Item.Site** in **AddItem** or **AddFixedPriceItem** , it must be consistent with the numeric site ID that you specify in the request URL (for the SOAP API) or the **X-EBAY-API-SITEID** header (for the XML API).   
  
**Applicable values** : See [Site](https://developer.ebay.com/devzone/xml/docs/reference/ebay/extra/gtsllrlst.rspns.itmarry.itm.st.html).   
Code so that your app gracefully handles any future changes to this list.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Coarse, Fine, Medium.   |  
|  ItemArray.Item.**SKU**  | [SKUType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/SKUType.html) ([string](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string))  | Conditionally  |  A SKU (Stock Keeping Unit) value is a seller-defined identifier for a product. Each product within a seller's inventory should be unique. Most large-volume sellers use SKUs, but eBay only requires a SKU value if the **InventoryTrackingMethod** field is included in an **AddFixedPriceItem** call and its value is set to `SKU`. Setting the **InventoryTrackingMethod** field to `SKU` allows the seller to use a SKU value instead of an **ItemID** value as a unique identifier in calls such as **GetItem** and **ReviseInventoryStatus**   
  
A seller can specify a SKU when listing an item with **AddItem** and related calls. eBay preserves the SKU on the item, enabling you to obtain it before and after an order line item is created. (**SKU** is recommended as an alternative to **ApplicationData**.)   
  
If both **ItemID** and **SKU** are specified in calls that support the use of SKU as a unique identifier, the **ItemID** value takes precedence.  
  
If a seller wants to use SKUs for multiple-variation listings, the SKU value for each product variation is actually specified at the variation level (Item.Variations.Variation.**SKU**) field, and the Item.**SKU**) field should not be included in the call request.   
  
**Note:** The eBay site cannot identify listings by SKU. For example, My eBay pages and Search pages all identify listings by item ID. When a buyer contacts you via eBay's messaging functionality, eBay uses the item ID as the identifier. Buyer-focused APIs (like the Shopping API) also do not support SKU as an identifier.  **For revising and relisting only:** To remove a SKU when you revise or relist an item, use **DeletedField**. (You cannot remove a SKU when **Item.InventoryTrackingMethod** is set to SKU.)  
  
For **GetItem** , **GetMyeBaySelling** , and other 'Get' call, the **SKU** value will only be returned if defined for the listing.   
  
**Max length:** 50.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll. See [eBay Merchant Data API](https://developer.ebay.com/DevZone/merchant-data/CallRef/index.html) for AddFixedPriceItem and ReviseFixedPriceItem.  |  
|  ItemArray.Item.**StartPrice**  |  [AmountType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/AmountType.html) ([double](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#double))  | Conditionally  |  The original price of the item at listing or re-listing time. If this value changes when the item is revised, the new value becomes the original price.   
  
**For auction listings:** Competitive bidding starts at this value. Once at least one bid has been placed, **StartPrice** remains the same but **CurrentPrice** is incremented to the amount of each succeeding bid. If **ReservePrice** is also specified, the value of **StartPrice** must be lower than the value of **ReservePrice**.   
  
**For input on fixed-price listings (**FixedPriceItem**): ** This is the constant price at which a buyer may purchase the item.   
  
**GetMyeBaySelling** does not return **Item.StartPrice** for fixed price items—it returns **Item.SellingStatus.CurrentPrice**.   
  
**For AddFixedPriceItem and VerifyAddFixedPriceItem:** Required when no variations are specified. If variations are specified, use **Variation.StartPrice** for each variation instead.   
  
**For Revise calls:** If the **StartPrice** value for a fixed-price item is changed with a Revise call, the **MinimumBestOfferPrice** and **BestOfferAutoAcceptPrice** fields in the **ListingDetails** container will be dropped (if set), basically turning off the Best Offer Auto Accept and/or Auto Decline features. If the seller wanted to reintroduce either of these Best Offer threshold values in the listing again, an additional Revise call would have to be made, passing in the desired threshold values.   
  
**Note:** For the US site, new eBay sellers are subject to [Seller Limits](https://developer.ebay.com/api-docs/user-guides/static/make-a-call/fg-replaced.html), which limit the quantity of items that may be listed and/or the total cumulative value of these listings. While subject to these selling limits, an eBay seller can use the **GetMyeBaySelling** call to retrieve both the remaining number of listings they can create and the remaining cumulative value of these listings. These values are shown in the **Summary.QuantityLimitRemaining** and **Summary.AmountLimitRemaining** fields in the **GetMyeBaySelling** response. If a call to add an item or revise an item would result in the exceeding of these limits, the add item or revise item call will fail. These fields will only be returned if the seller is subject to seller limits.    
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine. See [Listing Policies](https://developer.ebay.com/api-docs/user-guides/static/make-a-call/fg-replaced.html).  |  
| ItemArray.Item.**StartPrice**  
[ attribute **currencyID** ]  | [CurrencyCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html)  | Conditionally  |  The original price of the item at listing or re-listing time. If this value changes when the item is revised, the new value becomes the original price.   
  
**For auction listings:** Competitive bidding starts at this value. Once at least one bid has been placed, **StartPrice** remains the same but **CurrentPrice** is incremented to the amount of each succeeding bid. If **ReservePrice** is also specified, the value of **StartPrice** must be lower than the value of **ReservePrice**.   
  
**For input on fixed-price listings (**FixedPriceItem**): ** This is the constant price at which a buyer may purchase the item.   
  
**GetMyeBaySelling** does not return **Item.StartPrice** for fixed price items—it returns **Item.SellingStatus.CurrentPrice**.   
  
**For AddFixedPriceItem and VerifyAddFixedPriceItem:** Required when no variations are specified. If variations are specified, use **Variation.StartPrice** for each variation instead.   
  
**For Revise calls:** If the **StartPrice** value for a fixed-price item is changed with a Revise call, the **MinimumBestOfferPrice** and **BestOfferAutoAcceptPrice** fields in the **ListingDetails** container will be dropped (if set), basically turning off the Best Offer Auto Accept and/or Auto Decline features. If the seller wanted to reintroduce either of these Best Offer threshold values in the listing again, an additional Revise call would have to be made, passing in the desired threshold values.   
  
**Note:** For the US site, new eBay sellers are subject to [Seller Limits](https://developer.ebay.com/api-docs/user-guides/static/make-a-call/fg-replaced.html), which limit the quantity of items that may be listed and/or the total cumulative value of these listings. While subject to these selling limits, an eBay seller can use the **GetMyeBaySelling** call to retrieve both the remaining number of listings they can create and the remaining cumulative value of these listings. These values are shown in the **Summary.QuantityLimitRemaining** and **Summary.AmountLimitRemaining** fields in the **GetMyeBaySelling** response. If a call to add an item or revise an item would result in the exceeding of these limits, the add item or revise item call will fail. These fields will only be returned if the seller is subject to seller limits.   
  
For a list of possible enumeration values, see [CurrencyCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html).   |  
|  ItemArray.Item.**Storefront**  | [StorefrontType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/StorefrontType.html)  | Conditionally  |  This container provides details about the seller's eBay store.   
  
In an Add/Revise/Relist call, the seller can include this container to set/change which customized eBay store category that the item will be placed in.   
  
For 'Get' calls, this container is returned if the seller of the item has an eBay store.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Coarse, Fine, Medium.   |  
|  ItemArray.Item.Storefront  
.**StoreCategory2ID**  | [long](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#long)  | Conditionally  |  Unique identifier for the secondary custom category in which to list the item. Set this field to a root-level custom category or a custom category that has no child categories (subcategories).   
  
The system resets the value to 0 (None) in the following cases:   
- The values of **StoreCategoryID** and **StoreCategory2ID** field are the same   
- You specify **StoreCategory2ID** but not **StoreCategoryID**   
  
  
In other words, **StoreCategoryID** must be set to a valid custom category and be different from **StoreCategory2ID**.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Coarse, Fine, Medium.   |  
|  ItemArray.Item.Storefront  
.**StoreCategoryID**  | [long](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#long)  | Conditionally  |  Unique identifier of a primary custom category in which to list the item. A custom category is a category that the seller created in their eBay Store. eBay Store sellers can create up to three levels of custom categories for their stores, but the API only supports root-level categories.   
  
To list an item using the categories in a seller's store, you must set this field to a root-level custom category or a custom category that has no child categories (subcategories). If you attempt to list an item in a category that has subcategories, the call response contains a warning, and the item is listed in the 'Other' store category.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Coarse, Fine, Medium.   |  
|  ItemArray.Item.Storefront  
.**StoreURL**  | [anyURI](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#anyURI)  | Conditionally  |  The URL of the seller's eBay Stores page.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Coarse, Fine, Medium.   |  
|  ItemArray.Item.**TimeLeft**  | [duration](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#duration)  | Conditionally  |  Time left before the listing ends. The duration is represented in the ISO 8601 duration format (PnYnMnDTnHnMnS). See Data Types in the Trading API Guide for information about this format. For ended listings, the time left is PT0S (zero seconds).   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Coarse, Fine, Medium.   |  
|  ItemArray.Item.**Title**  | [string](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string)  | Conditionally  |  This field is used to specify the title of the listing. This field is conditionally required in an Add call unless the seller successfully uses the **ProductListingDetails** container to find an eBay catalog product match. When the seller successfully uses an eBay catalog product to create a listing, the listing title, listing description, Item Specifics, and stock photo defined in the catalog product are used to create the listing.   
  
You cannot use HTML or JavaScript in the Title. (HTML characters will be interpreted literally as plain text.)  
  
The listing title can only be changed if the active listing has yet to have any bids or sales, and the listing does not end within 12 hours.   
**Note:** When making a **GetSellerEvents** call, this field will be returned masked as `*****************` for on-hold listings.  **Note:** When making a **GetSellerTransactions** or **GetMyeBaySelling** call, the item ID value of the listing will be returned in this field to indicate that the listing is on hold.  **Note:** When a line item comes from a multiple-variation listing, the variation aspect name-value pair will be appended to this title.   
**Max length:** 80 for Add/Revise/Relist/Verify Item family of calls; 120 for GetOrders/GetItemTransactions/GetSellerTransactions calls.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Coarse, Fine, Medium.   |  
|  ItemArray.Item  
.**TotalQuestionCount**  | [long](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#long)  | Conditionally  |  The number of questions asked about this item. Applies to eBay Motors Pro applications only.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   |  
|  ItemArray.Item.**Variations**  | [VariationsType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/VariationsType.html)  | Conditionally  |    
Variations are similar (but not identical) items in a multiple-variation, fixed-price listing. For example, a T-shirt listing could contain multiple items of the same brand that vary by color and size (like "Blue, Large" and "Black, Medium"). Each variation specifies a combination of one of these colors and sizes. Each variation can have a different quantity and price. You can buy multiple items from one variation at the same time. (That is, one order line item can contain multiple items from a single variation.)   
  
If you list in two categories, both categories must support listing with variations. Use the **Metadata API** [getListingStructurePolicies](https://developer.ebay.com/api-docs/sell/metadata/resources/marketplace/methods/getListingStructurePolicies) method and inspect the **variationsSupported** field to determine whether a specific leaf category supports variations.  
  
**For ReviseFixedPriceItem and RelistFixedPriceItem:** Once a listing has been submitted with variations, you can't delete all the variations when you revise or relist the listing (because it would be considered a different listing). You also can't add or change variation specifics (because they are unique identifiers). However, you can delete or replace individual variations as needed to match your current inventory. If a variation has no purchases, use the **Variation.Delete** field to delete the variation. If it has inventory, set the Quantity to 0.  
  
As a best practice, if you want to revise multiple variations in the same listing at the same time (i.e., within a very short period), use a single **ReviseFixedPriceItem** request and include all the variation revisions in the same request. If your application design requires you to revise each variation individually, then avoid using multiple parallel threads. Instead, use a serial, synchronous process. That is, wait until each revision has been processed by eBay before submitting the next revision request for another variation in the same listing.  
  
**For GetItem and related calls** Only returned when a listing has variations.   
  
**For GetSellerList:** Only returned when a listing has variations, **IncludeVariations** was set to `true` in the request, the **DetailLevel** was set to **ReturnAll** , and an applicable pagination value and time range were specified.  
  
**For GetItemTransactions** Only returned in Item when a listing has variations and **IncludeVariations** was set to `true` in the request. (Also see **Variation** returned in **Transaction** for information about which variation was actually purchased.)   
  
**For GetSellerEvents, GetMyeBayBuying, and GetMyeBaySelling:** Only returned when a listing has variations and **HideVariations** was set to `false` or not specified in the request.   
**Note:** This container will stop being returned in **GetItemTransactions** on January 31, 2024.    
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll. See [Multiple-variation listings](https://developer.ebay.com/api-docs/user-guides/static/trading-user-guide/variations.html).  |  
|  ItemArray.Item.Variations  
.**Variation**  | [VariationType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/VariationType.html)  | Conditionally,   
[repeatable](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#repeatable): [0..*]  |    
Contains data that distinguishes one item variation from another. For example, if an item varies by color and size, each **Variation** node specifies a combination of one of those colors and sizes.  
  
When listing or relisting an item, you are allowed to create a listing with only one item variation, and you might have a plan to add more item variations to the listing in the future. However, if you don't plan to add other item variations in the future, we recommend that you avoid listing with only one variation, so that you avoid confusing buyers.   
  
If you specify multiple **Variation** containers in an add/revise/relist/verify add call to define multiple item variations, the **Variation** containers must be contiguous or an error will occur. This means that you would not want to input a **Pictures** or a **VariationSpecificsSet** container in between **Variation** containers in an API call.   
  
When you modify an item variation with a **ReviseFixedPriceItem** call, the best practice is to include all applicable fields under the **Variation** container, even if some of the values/settings are not being modified. The **StartPrice** and **VariationSpecifics** must be included when modifying an existing item variation, even if these values are not being changed. If a SKU value is defined for the item variation, it is strongly recommended that you include the **SKU** field, regardless of whether the SKU value is changing or not. If the **SKU** field is not included, any existing SKU value will be removed from the item variation. It is also strongly recommended that you include the **Quantity** field and input an accurate value, because if the **Quantity** field is omitted in the API call, the quantity for the item variation is set to `0`.   
**Note:** The **Item.Variations** container and its child fields will stop being returned in **GetItemTransactions** on January 31, 2024.    
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll. See [Multiple-variation listings](https://developer.ebay.com/api-docs/user-guides/static/trading-user-guide/variations.html).  |  
|  ItemArray.Item.Variations  
.Variation.**Quantity**  | [int](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#int)  | Conditionally  |    
This value indicates the quantity of the specific variation that are available for purchase. If you set **Variation.Quantity** to `0` when you create, revise, or relist an item listing, the variation is dropped from the listing. To prevent this, you can set [SetUserPreferences.OutOfStockControlPreference](https://developer.ebay.com/DevZone/XML/docs/Reference/ebay/SetUserPreferences.html#Request.OutOfStockControlPreference) to `true`.   
  
For **GetItem** (and other related calls that retrieve the Item object), the **Variation.Quantity** value indicates the total quantity associated with the variation, including the quantity available and the quantity sold. To calculate the quantity available for sale, subtract **SellingStatus.QuantitySold** from this value.  
  
**For RelistFixedPriceItem:**
  * For an item variation that had an available quantity greater than `0` when the listing ended, the **Quantity** value of the item variation for the newly relisted item is set to the actual quantity available. For item variations, there is actually no **QuantityAvailable** field, but this value may be derived if you look at the corresponding item variation in a **GetMyeBaySelling**) response and subtract the **Variation.QuantitySold** value from the **Variation.Quantity** value, which represents the original **Variation.Quantity** value at creation time of the previous listing. 
  * For item variations with an available quantity of `0` when the listing ended, the relisted item will retain the **Variaton.Quantity** value that was passed in at creation time of the previous listing. 

So, if you are relisting an item that had one or more item variations with an available quantity of `0` when the listing ended, we strongly recommend that you pass in the correct available quantity through the corresponding **Variation.Quantity** field of a relist call. Alternatively, you can update the correct quantity available by using a **ReviseInventoryStatus** call and passing in a **Quantity** value, while also making sure to pass in the correct **SKU** value(s) to identify the correct item variation. A **ReviseInventoryStatus** call can be used to revise the quantity of up to four single item listings and/or item variations (from the same or different listings).   
  
**For ReviseFixedPriceItem:** You can revise a variation's quantity at any time, even if it has purchases. However, unless you set the [OutOfStockControlPreference](https://developer.ebay.com/DevZone/XML/docs/Reference/ebay/SetUserPreferences.html#Request.OutOfStockControlPreference) boolean field of the **SetUserPreferences** call to `true`, at least one variation must remain with a non-zero quantity in order for the listing to remain active. If you set the **OutOfStockControlPreference** field to `true`, a multiple-variation listing will remain active but hidden from search even if the quantity of all variations in the listing is set to `0`. When you modify a variation during revise or relist, you need to include both its **StartPrice** and **Quantity**. If you revise the **Quantity** value for a variation after items have already sold, specify the quantity available for sale. (eBay will automatically add the quantity sold to the value you specify.) If you set the quantity to `0` and the variation has no purchases, the variation may be dropped from the listing.   
  
**For GetSellerTransactions:** See **Item.Quantity** instead.  
  
See the [Trading API User Guide](https://developer.ebay.com/api-docs/user-guides/static/trading-user-guide/update-variations.html) for more details about setting and modifying a variation's quantity.   
  
**Note:** The number in the **Variation.Quantity** field represents the current quantity of the item variation that is available using the "Ship to home" fulfillment method. This number does not take into account any quantity of the item variation that is available through "local" fulfillment methods such as Click and Collect. This is due to the fact that there is no current implementation (or API field) where the seller informs eBay about the quantity of item variations available through each local fulfillment method. In the case where a listing is only offering the item variations through a local fulfillment method, this value should default to `0`, and the **Item.IgnoreQuantity** will also be returned as `True`.    
**Note:** The **Item.Variations** container and its child fields will stop being returned in **GetItemTransactions** on January 31, 2024.    
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll. See:   
[Set and adjust a variation's quantity](https://developer.ebay.com/api-docs/user-guides/static/trading-user-guide/variations.html#qty)   
[Out-of-Stock control](https://developer.ebay.com/api-docs/user-guides/static/trading-user-guide/out-of-stock.html)  |  
|  ItemArray.Item.Variations  
.Variation.**SellingStatus**  | [SellingStatusType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/SellingStatusType.html)  | Conditionally  |  Contains the variation's quantity sold. Always returned when variations are present.   
**Note:** The **Item.Variations** container and its child fields will stop being returned in **GetItemTransactions** on January 31, 2024.    
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   |  
|  ItemArray.Item.Variations  
.Variation.SellingStatus  
.**AdminEnded**  | [boolean](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean)  | Conditionally  |  If included in the response as `true`, indicates that the listing was administratively canceled due to a violation of eBay's listing policies and that the item can be relisted using **RelistItem**.   
  
**Note:** **GetItem** returns an error (invalid item ID) in the response if **Item.SellingStatus.AdminEnded** = `true` and the requesting user is not the seller of the item.   |  
|  ItemArray.Item.Variations  
.Variation.SellingStatus  
.**BidCount**  | [int](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#int)  | Conditionally  |  Number of bids placed so far against the auction item.   |  
|  ItemArray.Item.Variations  
.Variation.SellingStatus  
.**BidIncrement**  |  [AmountType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/AmountType.html) ([double](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#double))  | Conditionally  |  The minimum amount a progressive bid must be above the current high bid to be accepted. This field is only applicable to auction listings. The value of this field will always be '0.00' for Classified Ad and fixed-price listings.   |  
| ItemArray.Item.Variations  
.Variation.SellingStatus  
.**BidIncrement**  
[ attribute **currencyID** ]  | [CurrencyCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html)  | Conditionally  |  The minimum amount a progressive bid must be above the current high bid to be accepted. This field is only applicable to auction listings. The value of this field will always be '0.00' for Classified Ad and fixed-price listings.  
  
For a list of possible enumeration values, see [CurrencyCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html).   |  
|  ItemArray.Item.Variations  
.Variation.SellingStatus  
.**ConvertedCurrentPrice**  |  [AmountType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/AmountType.html) ([double](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#double))  | Conditionally  |  Converted value of the **CurrentPrice** in the currency of the site that returned this response. For active items, refresh the listing's data every 24 hours to pick up the current conversion rates. Only returned when the item's **CurrentPrice** on the listing site is in different currency than the currency of the host site for the user/application making the API call. **ConvertedCurrentPrice** is not returned for Classified listings (Classified listings are not available on all sites).  
  
In multi-variation listings, this value matches the lowest-priced variation that is still available for sale.   |  
| ItemArray.Item.Variations  
.Variation.SellingStatus  
.**ConvertedCurrentPrice**  
[ attribute **currencyID** ]  | [CurrencyCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html)  | Conditionally  |  Converted value of the **CurrentPrice** in the currency of the site that returned this response. For active items, refresh the listing's data every 24 hours to pick up the current conversion rates. Only returned when the item's **CurrentPrice** on the listing site is in different currency than the currency of the host site for the user/application making the API call. **ConvertedCurrentPrice** is not returned for Classified listings (Classified listings are not available on all sites).  
  
In multi-variation listings, this value matches the lowest-priced variation that is still available for sale.  
  
For a list of possible enumeration values, see [CurrencyCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html).   |  
|  ItemArray.Item.Variations  
.Variation.SellingStatus  
.**CurrentPrice**  |  [AmountType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/AmountType.html) ([double](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#double))  | Conditionally  |  The current price of the item in the original listing currency.   
  
For auction listings, this price is the starting minimum price (if the listing has no bids) or the current highest bid (if bids have been placed) for the item. This does not reflect the **BuyItNow** price.   
  
For fixed-price and ad format listings, this is the current listing price.   
  
In multi-variation, fixed-price listings, this value matches the lowest-priced variation that is still available for sale.   |  
| ItemArray.Item.Variations  
.Variation.SellingStatus  
.**CurrentPrice**  
[ attribute **currencyID** ]  | [CurrencyCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html)  | Conditionally  |  The current price of the item in the original listing currency.   
  
For auction listings, this price is the starting minimum price (if the listing has no bids) or the current highest bid (if bids have been placed) for the item. This does not reflect the **BuyItNow** price.   
  
For fixed-price and ad format listings, this is the current listing price.   
  
In multi-variation, fixed-price listings, this value matches the lowest-priced variation that is still available for sale.  
  
For a list of possible enumeration values, see [CurrencyCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html).   |  
|  ItemArray.Item.Variations  
.Variation.SellingStatus  
.**HighBidder**  | [UserType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/UserType.html)  | Conditionally  |  For ended auction listings that have a winning bidder, this field is a container for the high bidder's user ID. For ended, single-item, fixed-price listings, this field is a container for the user ID of the purchaser. This field isn't returned for auctions with no bids, or for active fixed-price listings.   
  
In the case of **PlaceOffer** , for auction listings, this field is a container for the high bidder's user ID. In the **PlaceOffer** response, the following applies: For multiple-quantity, fixed-price listings, the high bidder is only returned if there is just one order line item (or only for the first order line item that is created).   |  
|  ItemArray.Item.Variations  
.Variation.SellingStatus  
.HighBidder.**AboutMePage**  | [boolean](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean)  | Conditionally  |    
A value of `true` indicates that the user has set up an About Me page.   
**Note:** This field will stop being returned in **GetItemTransactions** and **GetSellerTransactions** on January 31, 2024.    
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine.   |  
|  ItemArray.Item.Variations  
.Variation.SellingStatus  
.HighBidder.**BuyerInfo**  | [BuyerType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/BuyerType.html)  | Conditionally  |  Contains information about the user as a buyer, such as the shipping address. See **BuyerType** for its child elements.   
  
Since a bidder's user info is anonymous, this tag will be returned only to that bidder, and to the seller of an item that the user is bidding on.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine. See [Anonymous user information](https://developer.ebay.com/api-docs/user-guides/static/trading-user-guide/user-mgmt-anonymous-info.html).  |  
|  ItemArray.Item.Variations  
.Variation.SellingStatus  
.HighBidder.BuyerInfo  
.**ShippingAddress**  | [AddressType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/AddressType.html)  | Conditionally  |  This container shows the buyer's shipping address.   
  
**Note:** For an Authenticity Guarantee program order returned in **GetItemTransactions** or **GetSellerTransactions** , this is the address of the authenticator's warehouse. The authenticator is responsible for delivery to the buyer's shipping address.  **Note:** For Click and Collect orders, this is the address of the merchant's store where the buyer will pick up the order. This is only applicable for **GetItemTransactions** and **GetSellerTransactions** calls.  **Note:** For eBay Vault scenarios: **GetItemTransactions** calls, and **GetSellerTransactions** calls (Seller View only), mock address details are returned for:   
  
-_Vault to vault orders: Buyer and Seller View_  
  
-_Ship to vault orders_ : Mock addresses are returned for the Buyer View (only); the address returned for the Seller View will be the authenticator&apos;s address.  
  
-_Vault in-hand submission orders_ : the address returned for the Buyer View will be the authenticator's address (**GetItemTransactions** only).  
  
The following address details are returned for mock addresses:  
```
 <ShippingAddress>   
   <Name>eBay Vault</Name>   
   <AddressID>Invalid Request</AddressID>   
   <AddressOwner>eBay</AddressOwner>   
   <AddressUsage>Invalid</AddressUsage>   
   <CityName>Invalid Request</CityName>   
   <Country>US</Country>   
   <CountryName>Invalid Request</CountryName>   
   <ExternalAddressID>Invalid Request</ExternalAddressID>   
   <Phone>Invalid Request</Phone>   
   <PostalCode>Invalid Request</PostalCode>   
   <StateOrProvince>Invalid Request</StateOrProvince>   
   <Street1>Invalid Request</Street1>   
   <Street2></Street2>   
 </ShippingAddress> 
```
  
  
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine.   |  
|  ItemArray.Item.Variations  
.Variation.SellingStatus  
.HighBidder.BuyerInfo  
.ShippingAddress.**Country**  | [CountryCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CountryCodeType.html)  | Conditionally  |  The two-digit code representing the country of the user.  
  
If not provided as input, eBay uses the country associated with the eBay Site ID when the call is made.  
  
  
  
**Applicable values** : See [Country](https://developer.ebay.com/devzone/xml/docs/reference/ebay/extra/gtsllrlst.rspns.itmarry.itm.vrtns.vrtn.sllngstts.hghbddr.byrinf.shppngaddrss.cntry.html).   
Code so that your app gracefully handles any future changes to this list.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine.   |  
|  ItemArray.Item.Variations  
.Variation.SellingStatus  
.HighBidder.BuyerInfo  
.ShippingAddress.**PostalCode**  | [string](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string)  | Conditionally  |  User's postal code.  
  
**Max length:** GB, DE - 35; US, CA - 40; AU - 80; Other countries - 50.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine.   |  
|  ItemArray.Item.Variations  
.Variation.SellingStatus  
.HighBidder.**eBayGoodStanding**  | [boolean](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean)  | Conditionally  |    
This boolean field is returned as `true` if the eBay user is in good standing with eBay.   
**Note:** This field will stop being returned in **GetItemTransactions** and **GetSellerTransactions** on January 31, 2024.    
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine.   |  
|  ItemArray.Item.Variations  
.Variation.SellingStatus  
.HighBidder.**EIASToken**  | [string](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string)  | Conditionally  |  Unique identifier for the user that does not change when the eBay user name is changed. Use when an application needs to associate a new eBay user name with the corresponding eBay user.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine. See [Anonymous user information](https://developer.ebay.com/api-docs/user-guides/static/trading-user-guide/user-mgmt-anonymous-info.html).  |  
|  ItemArray.Item.Variations  
.Variation.SellingStatus  
.HighBidder.**Email**  | [string](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string)  | Conditionally  |  Email address for the user. Please see the links below to the topics related to anonymous user information and static email addresses. You cannot retrieve an email address for any user with whom you do not have an order relationship, regardless of site.   
  
An email address of another user is only returned if you and the other user are in an order relationship, within a certain time of order line item creation (although this limitation isn't applicable to the **GetAllBidders** call in the case of motor vehicles categories.) Based on Trust and Safety policies, the time is unspecified and can vary by site.   
  
Since a bidder's user info is anonymous, this tag will be returned only to that bidder, and to the seller of an item that the user is bidding on.   
  
For the **GetOrders** call, the buyer's email address will be returned (to the seller only) for orders less than two weeks old, but for orders that occurred more than two weeks in the past, the buyer's email address will no longer be returned. This **Email** field will still be returned, but 'dummy data', such as `Invalid Request` will replace the actual email address.   
  
**Note:** For the **GetItemTransactions** call, this field is only returned to the seller of the order; this field is not returned for the buyer or third party.   
**Max length:** 64 for US. May differ for other countries. Note: The eBay database allocates up to 128 characters for this field .   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll. See:   
[Anonymous user information](https://developer.ebay.com/api-docs/user-guides/static/trading-user-guide/user-mgmt-anonymous-info.html)   
[Member communications](https://developer.ebay.com/api-docs/user-guides/static/trading-user-guide/member-communications.html)  |  
|  ItemArray.Item.Variations  
.Variation.SellingStatus  
.HighBidder.**FeedbackPrivate**  | [boolean](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean)  | Conditionally  |  Indicates whether the user has chosen to make their feedback score and feedback details private (hidden from other users). The percentage of positive feedback can still be returned, even if other feedback details are private.   
  
Since a bidder's user info is anonymous, this tag will be returned only to that bidder, and to the seller of an item that the user is bidding on.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine. See [Anonymous user information](https://developer.ebay.com/api-docs/user-guides/static/trading-user-guide/user-mgmt-anonymous-info.html).  |  
|  ItemArray.Item.Variations  
.Variation.SellingStatus  
.HighBidder.**FeedbackRatingStar**  | [FeedbackRatingStarCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/FeedbackRatingStarCodeType.html)  | Conditionally  |    
A visual indicator of an eBay user's Feedback score. A different colored star is used for each range of Feedback scores. See **FeedbackRatingStarCodeType** for specific values.   
**Note:** This field will stop being returned in **GetItemTransactions** and **GetSellerTransactions** on January 31, 2024.    
  
**Applicable values** : See [FeedbackRatingStar](https://developer.ebay.com/devzone/xml/docs/reference/ebay/extra/gtsllrlst.rspns.itmarry.itm.vrtns.vrtn.sllngstts.hghbddr.fdbckrtngstr.html).   
Code so that your app gracefully handles any future changes to this list.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine.   |  
|  ItemArray.Item.Variations  
.Variation.SellingStatus  
.HighBidder.**FeedbackScore**  | [int](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#int)  | Conditionally  |  The aggregate feedback score for a user. A user's feedback score is the net positive feedback minus the net negative feedback left for the user. Feedback scores are a quantitative expression of the desirability of dealing with a user as a buyer or a seller in either side of an order.   
  
Each order line item can result in one feedback entry for a given user (the buyer can leave feedback for the seller, and the seller can leave feedback for the buyer.). That one feedback can be positive, negative, or neutral. The aggregated feedback counts for a particular user represent that user's overall feedback score (referred to as a "feedback rating" on the eBay site).   
  
If the user has chosen to make their feedback private and that user is not the user identified in the request's authentication token, **FeedbackScore** is not returned and **FeedbackPrivate** is returned with a value of `true`.   
  
In **GetMyeBayBuying** and **GetMyeBaySelling** , feedback information (**FeedbackScore** and **FeedbackRatingStar**) is returned in **BidList.ItemArray.Item.Seller**. For **GetMyeBayBuying** , the feedback score of each seller with an item having received a bid from the buyer is returned. For **GetMyeBaySelling** , the feedback score of the seller is returned.   
  
**GetMyeBayBuying** and **GetMyeBaySelling** also return feedback information (**FeedbackScore** and **FeedbackRatingStar**) in **BidList.ItemArray.Item.SellingStatus.HighBidder**. **GetMyeBayBuying** returns feedback information on the high bidder of each item the buyer is bidding on. **GetMyeBaySelling** returns feedback information on the high bidder of each item the seller is selling.  
  
Since a bidder's user info is anonymous, the real feedback score will be returned only to that bidder, and to the seller of an item that the user is bidding on. For all other users, the value -99 is returned.   
  
**For GetOrders and GetItemTransactions only:** If using Trading WSDL Version 1019 or above, this field will only be returned to the buyer or seller, and no longer returned at all to third parties. If using a Trading WSDL older than Version 1019, the accurate Feedback Score for the user is returned to the buyer or seller, but a dummy value of `0` will be returned to all third parties.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine. See [Anonymous user information](https://developer.ebay.com/api-docs/user-guides/static/trading-user-guide/user-mgmt-anonymous-info.html).  |  
|  ItemArray.Item.Variations  
.Variation.SellingStatus  
.HighBidder.**IDVerified**  | [boolean](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean)  | Conditionally  |    
Indicates whether the user has been verified. For more information about the ID Verify program, see: [Protecting your account](https://pages.ebay.com/help/policies/identity-idverify.html)   
**Note:** This field will stop being returned in **GetItemTransactions** and **GetSellerTransactions** on January 31, 2024.    
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine.   |  
|  ItemArray.Item.Variations  
.Variation.SellingStatus  
.HighBidder.**NewUser**  | [boolean](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean)  | Conditionally  |  This boolean is returned as `true` if the eBay user has been registered on eBay for 30 days or less.   
**Note:** The **Buyer.NewUser** field will stop being returned in **GetItemTransactions** and **GetSellerTransactions** on January 31, 2024.    
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine.   |  
|  ItemArray.Item.Variations  
.Variation.SellingStatus  
.HighBidder.**RegistrationDate**  | [dateTime](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#dateTime)  | Conditionally  |  Indicates the date the specified user originally registered with eBay.   
  
Since a bidder's user info is anonymous, this tag will be returned only to that bidder, and to the seller of an item that the user is bidding on.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine. See [Anonymous user information](https://developer.ebay.com/api-docs/user-guides/static/trading-user-guide/user-mgmt-anonymous-info.html).  |  
|  ItemArray.Item.Variations  
.Variation.SellingStatus  
.HighBidder.**Site**  | [SiteCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/SiteCodeType.html)  | Conditionally  |  eBay site the user is registered with.   
  
Since a bidder's user info is anonymous, this tag will be returned only to that bidder, and to the seller of an item that the user is bidding on.   
  
**Applicable values** : See [Site](https://developer.ebay.com/devzone/xml/docs/reference/ebay/extra/gtsllrlst.rspns.itmarry.itm.vrtns.vrtn.sllngstts.hghbddr.st.html).   
Code so that your app gracefully handles any future changes to this list.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine. See [Anonymous user information](https://developer.ebay.com/api-docs/user-guides/static/trading-user-guide/user-mgmt-anonymous-info.html).  |  
|  ItemArray.Item.Variations  
.Variation.SellingStatus  
.HighBidder.**Status**  | [UserStatusCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/UserStatusCodeType.html)  | Conditionally  |  Indicates the user's registration/user status.   
  
**Applicable values** : See [Status](https://developer.ebay.com/devzone/xml/docs/reference/ebay/extra/gtsllrlst.rspns.itmarry.itm.vrtns.vrtn.sllngstts.hghbddr.stts.html).   
Code so that your app gracefully handles any future changes to this list.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine.   |  
|  ItemArray.Item.Variations  
.Variation.SellingStatus  
.HighBidder.**UserAnonymized**  | [boolean](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean)  | Always  |  Indicates whether or not the User container has been made anonymous. If `true`, some elements in the User container have either been removed, or had their values changed to remove identifying characteristics. If false, all expected elements are returned, and no values are changed.   
  
Since a bidder's user info is anonymous, this tag is returned as false only to the bidder, and to the seller of an item that the user is bidding on. For all other users, this tag is returned as `true`.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine. See [Anonymous user information](https://developer.ebay.com/api-docs/user-guides/static/trading-user-guide/user-mgmt-anonymous-info.html).  |  
|  ItemArray.Item.Variations  
.Variation.SellingStatus  
.HighBidder.**UserID**  | [UserIDType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/UserIDType.html) ([string](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string))  | Conditionally  |  Unique eBay user ID for the user.  
  
**Note:** Effective September 26, 2025, select developers will no longer receive username data for U.S. users through this field. Instead, an immutable user ID will be returned in its place. For more information, please refer to [Data Handling Compliance](https://developer.ebay.com/api-docs/static/data-handling-update.html).    
Since a bidder's user info is anonymous, this tag contains the actual value of an ID only for that bidder, and for the seller of an item that the user is bidding on. For other users, the actual value is replaced by an anonymous value, according to these rules:   
  
When bidding on items, **UserID** is replaced with the value "a****b" where a and b are random characters from the **UserID**. For example, if the **UserID** = `IBidALot`, it might be displayed as, "I****A".   
  
**Important:** In this format, the anonymous bidder ID can change for each auction.  For **GetMyeBayBuying** only, when bidding on items: **UserID** is replaced with the value "a****b" where a and b are random characters from the **UserID**.   
  
When bidding on items listed on the Philippines site: **UserID** is replaced with the value "Bidder X" where X is a number indicating the order of that user's first bid. For example, if the user was the third bidder, **UserID** = `Bidder 3`. Note that in this Philippines site format, the anonymous bidder ID stays the same for a given auction, but is different for different auctions. For example, a bidder who is the third and then the seventh bidder in an auction will be listed for both bids as "Bidder 3". However, if that same bidder is the first bidder on a different auction, the bidder will be listed for that auction as "Bidder 1", not "Bidder 3".   
  
For **GetMyeBayBuying** only, when bidding on items listed on the UK and AU sites: **UserID** is replaced with the string "High Bidder".   
  
For **PlaceOffer** , see also **SellingStatus.HighBidder**.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine. See [Anonymous user information](https://developer.ebay.com/api-docs/user-guides/static/trading-user-guide/user-mgmt-anonymous-info.html).  |  
|  ItemArray.Item.Variations  
.Variation.SellingStatus  
.HighBidder.**UserIDChanged**  | [boolean](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean)  | Conditionally  |  If `true`, identifies a user whose ID has changed within the last 30 days. Does not indicate a new user (see **NewUser**).   
  
Since a bidder's user info is anonymous, this tag will be returned only to that bidder, and to the seller of an item that the user is bidding on.   
  
**Note:** For the **GetItemTransactions** call, this field is only returned to the seller of the order; this field is not returned for the buyer or third party.    
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine. See [Anonymous user information](https://developer.ebay.com/api-docs/user-guides/static/trading-user-guide/user-mgmt-anonymous-info.html).  |  
|  ItemArray.Item.Variations  
.Variation.SellingStatus  
.HighBidder.**UserIDLastChanged**  | [dateTime](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#dateTime)  | Conditionally  |    
Date and time when the user last changed their eBay user ID (in GMT).   
**Note:** The **Buyer.UserIDLastChanged** field will stop being returned in **GetItemTransactions** and **GetSellerTransactions** on January 31, 2024.    
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine. See [Anonymous user information](https://developer.ebay.com/api-docs/user-guides/static/trading-user-guide/user-mgmt-anonymous-info.html).  |  
|  ItemArray.Item.Variations  
.Variation.SellingStatus  
.HighBidder.**VATStatus**  | [VATStatusCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/VATStatusCodeType.html)  | Conditionally  |  Indicates whether or not the user is subject to VAT. Users who have registered with eBay as VAT-exempt are not subject to VAT. See documentation on Value-Added Tax (VAT).   
  
**Applicable values** :   
  


CustomCode
    (out) Reserved for internal or future use 

NoVATTax
    (out) VAT is not applicable 

VATExempt
    (out) Residence in a country with VAT and user is registered as VAT-exempt 

VATTax
    (out) Residence in a country with VAT and user is not registered as VAT-exempt   
Code so that your app gracefully handles any future changes to this list.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine. See [Vat-exempt sellers](https://developer.ebay.com/api-docs/user-guides/static/trading-user-guide/taxes-vat.html#exempt).  |  
|  ItemArray.Item.Variations  
.Variation.SellingStatus  
.**LeadCount**  | [int](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#int)  | Conditionally  |  Applicable to Ad type listings only. Indicates how many leads to potential buyers are associated with this item. Returns 0 (zero) for listings in other formats. You must be the seller of the item to retrieve the lead count.   |  
|  ItemArray.Item.Variations  
.Variation.SellingStatus  
.**ListingStatus**  | [ListingStatusCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/ListingStatusCodeType.html)  | Conditionally  |  Specifies an active or ended listing's status in eBay's processing workflow. 
  * If a listing ends with a sale (or sales), eBay needs to update the sale details (e.g., total price and buyer/high bidder) and the transaction fees. This processing can take several minutes.
  * If you retrieve a sold item and no details about the buyer/high bidder are returned or no transaction fees are available, use this listing status information to determine whether eBay has finished processing the listing.

  
  
**Applicable values** :   
  


Active
    (out) The listing is still active or the listing has ended with a sale but eBay has not completed processing the sale details. If the listing has ended with a sale but this Active status is returned, please allow several minutes for eBay to finish processing the listing. 

Completed
    (out) The listing has closed and eBay has completed processing the sale. All sale information returned from eBay should be considered accurate and complete. In this state, all transaction fees should be calculated. 

Custom
    (out) Reserved for internal or future use. 

CustomCode
    (out) Reserved for internal or future use. 

Ended
    (out) The listing has ended. If the listing ended with a sale, eBay has completed processing of the sale. All sale information returned from eBay should be considered accurate and complete. However, the transaction fees are not yet available.   
Code so that your app gracefully handles any future changes to this list.   |  
|  ItemArray.Item.Variations  
.Variation.SellingStatus  
.**MinimumToBid**  |  [AmountType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/AmountType.html) ([double](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#double))  | Conditionally  |  Smallest amount the next bid on the item can be. Returns same value as **Item.StartPrice** (if no bids have yet been placed) or **CurrentPrice** plus **BidIncrement** (if at least one bid has been placed). Only applicable to auction listings. Returns null for fixed-price and Ad type listings.   
  
In multi-variation listings, this value matches the lowest-priced variation that is still available for sale.   |  
| ItemArray.Item.Variations  
.Variation.SellingStatus  
.**MinimumToBid**  
[ attribute **currencyID** ]  | [CurrencyCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html)  | Conditionally  |  Smallest amount the next bid on the item can be. Returns same value as **Item.StartPrice** (if no bids have yet been placed) or **CurrentPrice** plus **BidIncrement** (if at least one bid has been placed). Only applicable to auction listings. Returns null for fixed-price and Ad type listings.   
  
In multi-variation listings, this value matches the lowest-priced variation that is still available for sale.  
  
For a list of possible enumeration values, see [CurrencyCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html).   |  
|  ItemArray.Item.Variations  
.Variation.SellingStatus  
.**PromotionalSaleDetails**  | [PromotionalSaleDetailsType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/PromotionalSaleDetailsType.html)  | Conditionally  |  If a seller has reduced the price of a listed item with the Promotional Price Display feature, this field contains the original price of the discounted item, along with the start-time and end-time of the discount.   |  
|  ItemArray.Item.Variations  
.Variation.SellingStatus  
.PromotionalSaleDetails  
.**EndTime**  | [dateTime](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#dateTime)  | Conditionally  |  End time of a discount for an item whose price a seller has reduced with the Promotional Price Display feature.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   |  
|  ItemArray.Item.Variations  
.Variation.SellingStatus  
.PromotionalSaleDetails  
.**OriginalPrice**  |  [AmountType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/AmountType.html) ([double](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#double))  | Conditionally  |  Original price of an item whose price a seller has reduced with the Promotional Price Display feature.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   |  
| ItemArray.Item.Variations  
.Variation.SellingStatus  
.PromotionalSaleDetails  
.**OriginalPrice**  
[ attribute **currencyID** ]  | [CurrencyCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html)  | Conditionally  |  Original price of an item whose price a seller has reduced with the Promotional Price Display feature.  
  
For a list of possible enumeration values, see [CurrencyCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html).   |  
|  ItemArray.Item.Variations  
.Variation.SellingStatus  
.PromotionalSaleDetails  
.**StartTime**  | [dateTime](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#dateTime)  | Conditionally  |  Start time of a discount for an item whose price a seller has reduced with the Promotional Price Display feature.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   |  
|  ItemArray.Item.Variations  
.Variation.SellingStatus  
.**QuantitySold**  | [int](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#int)  | Conditionally  |  The total number of items purchased so far (in the listing's lifetime). Subtract this from **Quantity** to determine the quantity available.   
  
If the listing has Item Variations, then in **GetItem** (and related calls) and **GetItemTransactions** , **Item.SellingStatus.QuantitySold** contains the sum of all quantities sold across all variations in the listing, and **Variation.SellingStatus.QuantitySold** contains the number of items sold for that variation.   
  
In **GetSellerTransactions** , **Transaction.Item.SellingStatus.QuantitySold** contains the number of items sold in that order line item.  
  
For order line item calls, also see **Transaction.QuantityPurchased** for the number of items purchased in the order line item.  
In multi-variation listings, this value matches total quantity sold across all variations.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine.   |  
|  ItemArray.Item.Variations  
.Variation.SellingStatus  
.**ReserveMet**  | [boolean](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean)  | Conditionally  |  Indicates whether the reserve price has been met for the listing. Returns true if the reserve price was met or no reserve price was specified.   |  
|  ItemArray.Item.Variations  
.Variation.SellingStatus  
.**SecondChanceEligible**  | [boolean](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean)  | Conditionally  |  Part of the Second Chance Offer feature, indicates whether the seller can extend a second chance offer for the item.   |  
|  ItemArray.Item.Variations  
.Variation.**SKU**  | [SKUType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/SKUType.html) ([string](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string))  | Conditionally  |    
A SKU (stock keeping unit) is a seller-defined identifier. It is only intended for the seller's use (not for buyers). A SKU value is not required, but many large sellers like to add SKU value to their listings. If defined on a listing, a SKU value can be used by sellers to reconcile their eBay inventory with your own inventory system, instead of using the **VariationSpecifics** identifying values.   
  
If specified, all SKU values must be unique within the **Variations** node. That is, no two variations within the same listing can have the same SKU.   
  
If you include the **Item.InventoryTrackingMethod** field in an 'FixedPriceItem' call and set its value to `SKU`, the **Variation.SKU** values become required for each variation..  
  
**For GetItem, GetOrders and other 'Get' calls:** Only returned if the seller specified a SKU for the variation.   
**Note:** The **Item.Variations** container and its child fields will stop being returned in **GetItemTransactions** on January 31, 2024.   
**Max length:** 80.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll. See [SKU identifiers](https://developer.ebay.com/api-docs/user-guides/static/trading-user-guide/skus.html).  |  
|  ItemArray.Item.Variations  
.Variation.**StartPrice**  |  [AmountType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/AmountType.html) ([double](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#double))  | Conditionally  |    
The fixed price for this item variation. For example, a "Blue, Large" variation price could be USD 10.00, and a "Black, Medium" variation price could be USD 5.00.  
  
Each variation requires this field, and the prices can be the same for all variations, or be different for each variation. This enables sellers to provide discounts on certain variations without affecting the price of others. Required (and always returned) for listings with variations.  
  
You can revise a variation's price at any time (even if it has purchases). When you modify a variation during revise or relist, you need to include both its **StartPrice** and **Quantity**.   
**Note:** The **Item.Variations** container and its child fields will stop being returned in **GetItemTransactions** on January 31, 2024.    
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll. See [Pricing](https://developer.ebay.com/api-docs/user-guides/static/trading-user-guide/variations.html#price).  |  
| ItemArray.Item.Variations  
.Variation.**StartPrice**  
[ attribute **currencyID** ]  | [CurrencyCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html)  | Conditionally  |    
The fixed price for this item variation. For example, a "Blue, Large" variation price could be USD 10.00, and a "Black, Medium" variation price could be USD 5.00.  
  
Each variation requires this field, and the prices can be the same for all variations, or be different for each variation. This enables sellers to provide discounts on certain variations without affecting the price of others. Required (and always returned) for listings with variations.  
  
You can revise a variation's price at any time (even if it has purchases). When you modify a variation during revise or relist, you need to include both its **StartPrice** and **Quantity**.   
**Note:** The **Item.Variations** container and its child fields will stop being returned in **GetItemTransactions** on January 31, 2024.   
  
For a list of possible enumeration values, see [CurrencyCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/CurrencyCodeType.html).   |  
|  ItemArray.Item.Variations  
.Variation  
.**VariationProductListingDetails**  | [VariationProductListingDetailsType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/VariationProductListingDetailsType.html)  | Conditionally  |  This container is used to provide one or more product identifiers for a product variation within a multiple-variation, fixed-price listing. The same product identifier type(s) must be used for all product variations within the listing. For instance, if one product variation uses ISBNs, all product variations must use ISBN values.   
  
When you include the **VariationProductListingDetails** container in a call, you must specify at least one GTIN or ePID. If an ePID is provided, a matching eBay catalog product must exist for the value that is passed in.   
  
**For ReviseItem and RelistItem only:** When you revise a listing, if it ends within 12 hours, you cannot change the product identifier and you cannot remove existing product variation listing details data.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   |  
|  ItemArray.Item.Variations  
.Variation  
.VariationProductListingDetails  
.**EAN**  | [string](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string)  | Conditionally  |  This field is used if the seller wants to, or is required to identify each product variation within a multiple-variation listing by an EAN (European Article Number) value. An EAN is a unique 8 or 13-digit identifier that many industries (such as book publishers) use to identify products. To determine whether a specific leaf category supports or requires an EAN value for a variation listing, use the **Taxonomy API** [getItemAspectsForCategory](https://developer.ebay.com/api-docs/commerce/taxonomy/resources/category_tree/methods/getItemAspectsForCategory) method. Inspect the **localizedAspectName** field to find the EAN aspect for the category, and then use the **aspectRequired** and **aspectUsage** fields to determine whether the EAN value is required, recommended, or optional.   
  
**Note:** If the listing is being posted to a category that expects an EAN value, but one doesn't exist for the product, the seller must provide a string indicating that the product identifier is unavailable. This text varies by marketplace. Refer to [Product Identifier Text](https://developer.ebay.com/api-docs/sell/static/inventory/product-identifier-text.html) for the specific text based on the listing marketplace.    
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   |  
|  ItemArray.Item.Variations  
.Variation  
.VariationProductListingDetails  
.**ISBN**  | [string](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string)  | Conditionally  |  This field is used if the seller wants to, or is required to identify each product variation within a multiplge-variation listing by an ISBN (International Standard Book Number) value. An ISBN is a unique identifer for books. Both 10 and 13-character ISBNs are supported. When specifying a 13-character ISBN, the value must begin with either '978' or '979'. To determine whether a specific leaf category supports or requires an ISBN value for a variation listing, use the **Taxonomy API** [getItemAspectsForCategory](https://developer.ebay.com/api-docs/commerce/taxonomy/resources/category_tree/methods/getItemAspectsForCategory) method. Inspect the **localizedAspectName** field to find the ISBN aspect for the category, and then use the **aspectRequired** and **aspectUsage** fields to determine whether the ISBN value is required, recommended, or optional.   
  
**Note:** If the listing is being posted to a category that expects an ISBN value, but one doesn't exist for the product, the seller must provide a string indicating that the product identifier is unavailable. This text varies by marketplace. Refer to [Product Identifier Text](https://developer.ebay.com/api-docs/sell/static/inventory/product-identifier-text.html) for the specific text based on the listing marketplace.    
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   |  
|  ItemArray.Item.Variations  
.Variation  
.VariationProductListingDetails  
.**UPC**  | [string](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string)  | Conditionally  |  This field is used if the seller wants to, or is required to identify each product variation within a multiple-variation listing by a UPC (Universal Product Code) value. A UPC is a commonly-used identifier for many different products. To determine whether a specific leaf category supports or requires a UPC value for a variation listing, use the **Taxonomy API** [getItemAspectsForCategory](https://developer.ebay.com/api-docs/commerce/taxonomy/resources/category_tree/methods/getItemAspectsForCategory) method. Inspect the **localizedAspectName** field to find the UPC aspect for the category, and then use the **aspectRequired** and **aspectUsage** fields to determine whether the UPC value is required, recommended, or optional.   
  
**Note:** If the listing is being posted to a category that expects a UPC value, but one doesn't exist for the product, the seller must provide a string indicating that the product identifier is unavailable. This text varies by marketplace. Refer to [Product Identifier Text](https://developer.ebay.com/api-docs/sell/static/inventory/product-identifier-text.html) for the specific text based on the listing marketplace.    
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   |  
|  ItemArray.Item.Variations  
.Variation.**VariationSpecifics**  | [NameValueListArrayType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/NameValueListArrayType.html)  | Conditionally,   
[repeatable](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#repeatable): [2..5]  |    
A list of name/value pairs that uniquely identify the variation within the listing. All variations must specify the same set of Item Specific names, but each variation must provide a unique combination of values for those Item Specific names. For example, if the items vary by color and size, then every variation must specify 'Color' and 'Size' as Item Specific names, but no two variations can specify the same combination of 'Color' and 'Size' values.  
  
When you revise a listing that includes variations, you can change names of **Variationpecifics** by using the **Variations.ModifyNameList** container. You can also add, delete, or replace individual variations as needed to match your current inventory. Use the **Variation.Delete** field to delete a variation that has no sales (order line items). If the variation has sales, then set the Quantity to 0.  
  
**For GetSellerEvents** To keep the **GetSellerEvents** response smaller, **Variationpecifics** are not returned if the variation has a SKU. If the variation has no SKU, then **Variationpecifics** are returned instead. Optionally, you can pass **IncludeVariationSpecifics** as `true` in the request to force **Variationpecifics** to be returned, even when the SKU is returned.   
**Note:** The **Item.Variations** container and its child fields will stop being returned in **GetItemTransactions** on January 31, 2024.    
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll. See:   
[Configure variation-selection widgets for buyers (View Item)](https://developer.ebay.com/api-docs/user-guides/static/trading-user-guide/variations.html#widgets)   
[Revise and relist with variations](https://developer.ebay.com/api-docs/user-guides/static/trading-user-guide/update-variations.html)  |  
|  ItemArray.Item.Variations  
.Variation.VariationSpecifics  
.**NameValueList**  | [NameValueListType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/NameValueListType.html)  | Conditionally,   
[repeatable](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#repeatable): [0..*]  |  **For the**AddItem** family of calls:** Contains the name and value(s) for an Item Specific. Only required when the **ItemSpecifics** container is specified.  
**For the AddFixedPriceItem family of calls:** The same NameValueList schema is used for the **ItemSpecifics** node, the **VariationSpecifics** node, and the **VariationSpecifcsSet** node.  
  
If the listing has variations, any name that you use in the **VariationSpecifics** and **VariationSpecificsSet** nodes can't be used in the **ItemSpecifics** node.  
When you list with Item Variations:  

  * Specify shared Item Specifics (e.g., Brand) in the **ItemSpecifics** node. 
  * Specify up to five **VariationSpecifics** in each Variation node. 
  * Specify all applicable names with all their supported values in the **VariationSpecificSet** node. 

See the Variation sample in the **AddFixedPriceItem** call reference for examples.  
  
**For PlaceOffer:** Required if the item being purchased includes Item Variations.   
  
**For AddToWatchList and RemoveFromWatchList:** The **ItemID** value of the multiple-variation listing and the name-value pair to identify each variation in the listing are required.   
  
**Note:** As of August 30, 2018, California will require sellers to display a Proposition 65 warning on online retail sites if products contain chemicals and/or substances that may impact the health of California buyers. This requirement is applicable to most eBay US categories, including eBay Motors, Motors Parts & Accessories, and catalog-enabled categories. The warning message can be customized by the seller, but should contain the following basic information: 
  * The name of at least one listed chemical that prompted the warning
  * Text stating that the product 'can expose you to' the chemical(s) in the product 
  * The URL for OEHHA's new Proposition 65 warnings website, which is [www.P65Warnings.ca.gov](https://developer.ebay.com/devzone/xml/docs/reference/ebay/www.P65Warnings.ca.gov)

Unlike standard item specifics that allow a maximum of 65 characters in the **Value** field, the matching value for the 'California Prop 65 Warning' item specific allows up to 800 characters of text. When a seller passes in this item specific, eBay will automatically insert a warning symbol icon for the listing.   
  
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   |  
|  ItemArray.Item.Variations  
.Variation.VariationSpecifics  
.NameValueList.**Name**  | [string](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string)  | Conditionally  |  Depending on the call and context, this value is either a name of an Item/Variation Specific, or a Parts Compatibility name.   
  
**For the AddItem and AddFixedPriceItem families of calls:** In the **Item.ItemSpecifics** context, the value in this field will either be the name of a required/recommended/optional item specific name for the category, or it may be a seller's customized item specific name.   
  
**For the**AddFixedPriceItem** family of calls:** In the **Compatibility.NameValueList** context, this value is a motor vehicle aspect such as _Year_ , _Make_ , and _Model_. A **Compatibility.NameValueList** container is applicable for motor vehicle parts and accessories listings.   
  
**For PlaceOffer:** Required if the line item being purchased is an item variation within a multiple-variation listing.   
  
**Note:** For required and recommended item specifics that are returned in the [getItemAspectsForCategory](https://developer.ebay.com/api-docs/commerce/taxonomy/resources/category_tree/methods/getItemAspectsForCategory) method of the Taxonomy API, the seller should pass in the name of these item specifics just as they are shown in the **getItemAspectsForCategory** response. Similarly, for catalog-enabled categories, the seller should pass in the name of instance aspects just as they are shown in the **getItemAspectsForCategory** response. Instance aspects are additional details unique to a specific item or listing that a seller can include along with the product aspects that are already defined in the eBay catalog product associated with the listing. Instance aspects common to many catalog-enabled categories include 'Bundle Description' and 'Modification Description'. eBay US sellers who ship to California are required to pass in a 'California Prop 65 Warning' item specific if the item in the listing contains one or more chemicals known to be harmful to human health. This item specific is passed at the listing level for both single-variation and multiple-variation listings. The 'California Prop 65 Warning' is considered an instance specific because it will be retained on the listing even when the seller lists using an eBay catalog product. The 'California Prop 65 Warning' may be applicable in most eBay US categories, including eBay Motors, Motors Parts & Accessories, and catalog-enabled categories.  **Note:** If Brand and MPN (Manufacturer Part Number) are being used to identify product variations in a multiple-variation listing, the Brand must be specified at the item level (**ItemSpecifics** container) and the MPN for each product variation must be specified at the variation level (**VariationSpecifics** container). The Brand name must be the same for all variations within a single listing.   
**Max length:** 65.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   |  
|  ItemArray.Item.Variations  
.Variation.VariationSpecifics  
.NameValueList.**Value**  | [string](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string)  | Conditionally,   
[repeatable](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#repeatable): [0..*]  |  Depending on the call and context, this value is either the value of an Item/Variation Specific, a Parts Compatibility value, or a product identifier.  
  
**For the**AddItem** family of calls:** Multiple values can only be specified for an Item Specific if the [itemToAspectCardinality](https://developer.ebay.com/api-docs/commerce/taxonomy/resources/category_tree/methods/getItemAspectsForCategory#response.aspects.aspectConstraint.itemToAspectCardinality) field of the **getItemAspectsForCategory** method shows a value of `MULTI`. If an item specific only supports a single value, only the first item specific value specified in the request will be used.   
  
For the **Compatibility.NameValueList** context, this is the corresponding value of a motor vehicle aspect such as _Year_ , _Make_ , and _Model_. A **Compatibility.NameValueList** container is applicable for motor vehicle parts and accessories listings.   
  
**For PlaceOffer:** Required if the line item being purchased is an item variation within a multiple-variation listing.   
  
**Note:** The standard maximum length for the value of an item specific is 65, but the maximum allowed length increases for instance aspects such as 'Bundle Description' and 'Modification Description'. For item specifics with max lengths greater than 65, the actual max length will be returned in a corresponding [aspectMaxLength](https://developer.ebay.com/api-docs/commerce/taxonomy/resources/category_tree/methods/getItemAspectsForCategory#response.aspects.aspectConstraint.aspectMaxLength) field. The maximum allowed length for the new 'California Prop 65 Warning' item specific is 800 characters. For more information about the 'California Prop 65 Warning' item specific, see the **ItemSpecifics.NameValueList** field description.   
**Max length:** 65 (but longer for some instance aspects, including 800 for 'California Prop 65 Warning').   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   |  
|  ItemArray.Item.**WatchCount**  | [long](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#long)  | Conditionally  |  The number of watches placed on this item from buyers' My eBay accounts. Specify **IncludeWatchCount** as `true` in the request. Returned by **GetMyeBaySelling** only if greater than 0.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll.   |  
|  **ItemsPerPage**  | [int](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#int)  | Always  |  This value reflects the value that was set in the **Pagination.EntriesPerPage** field in the request. This is the maximum number of listings that may be returned per page of the result set. Note that this value is only the maximum threshold and does not necessarily reflect the number of listings appearing on the current page of data.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll. Also returned if DetailLevel is not provided on input.   |  
|  **PageNumber**  | [int](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#int)  | Always  |  This value indicates the current page of data in the result set that is being displayed. This value reflects the value specified in the **Pagination.PageNumber** field in the request. Note that page number defaults to `1` if the **Pagination.PageNumber** field was not included in the request.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll. Also returned if DetailLevel is not provided on input.   |  
|  **PaginationResult**  | [PaginationResultType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/PaginationResultType.html)  | Always  |  This container shows the total number or pages in the result set, as well as the total number of listings that match the current input criteria.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll. Also returned if DetailLevel is not provided on input.   |  
|  PaginationResult  
.**TotalNumberOfEntries**  | [int](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#int)  | Conditionally  |  Indicates the total number of entries that could be returned by repeated call requests. Returned with a value of 0 if no entries are available.   |  
|  PaginationResult  
.**TotalNumberOfPages**  | [int](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#int)  | Conditionally  |  Indicates the total number of pages of data that could be returned by repeated requests. Returned with a value of 0 if no pages are available.   |  
|  **ReturnedItemCountActual**  | [int](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#int)  | Always  |  This value indicates the total number of listings being shown on the current page of the results set.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll. Also returned if DetailLevel is not provided on input.   |  
|  **Seller**  | [UserType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/UserType.html)  | Conditionally  |  This container consists of detailed information about the seller and the seller's account. This container is only returned if the **GranularityLevel** field is included in the request and set to `Fine`.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine.   |  
|  Seller.**AboutMePage**  | [boolean](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean)  | Always  |    
A value of `true` indicates that the user has set up an About Me page.   
**Note:** This field will stop being returned in **GetItemTransactions** and **GetSellerTransactions** on January 31, 2024.    
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll. Also returned if DetailLevel is not provided on input.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine.   |  
|  Seller.**eBayGoodStanding**  | [boolean](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean)  | Always  |    
This boolean field is returned as `true` if the eBay user is in good standing with eBay.   
**Note:** This field will stop being returned in **GetItemTransactions** and **GetSellerTransactions** on January 31, 2024.    
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll. Also returned if DetailLevel is not provided on input.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine.   |  
|  Seller.**Email**  | [string](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string)  | Conditionally  |  Email address for the user. Please see the links below to the topics related to anonymous user information and static email addresses. You cannot retrieve an email address for any user with whom you do not have an order relationship, regardless of site.   
  
An email address of another user is only returned if you and the other user are in an order relationship, within a certain time of order line item creation (although this limitation isn't applicable to the **GetAllBidders** call in the case of motor vehicles categories.) Based on Trust and Safety policies, the time is unspecified and can vary by site.   
  
Since a bidder's user info is anonymous, this tag will be returned only to that bidder, and to the seller of an item that the user is bidding on.   
  
For the **GetOrders** call, the buyer's email address will be returned (to the seller only) for orders less than two weeks old, but for orders that occurred more than two weeks in the past, the buyer's email address will no longer be returned. This **Email** field will still be returned, but 'dummy data', such as `Invalid Request` will replace the actual email address.   
  
**Note:** For the **GetItemTransactions** call, this field is only returned to the seller of the order; this field is not returned for the buyer or third party.   
**Max length:** 64 for US. May differ for other countries. Note: The eBay database allocates up to 128 characters for this field .   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ReturnAll. See:   
[Anonymous user information](https://developer.ebay.com/api-docs/user-guides/static/trading-user-guide/user-mgmt-anonymous-info.html)   
[Member communications](https://developer.ebay.com/api-docs/user-guides/static/trading-user-guide/member-communications.html)  |  
|  Seller.**FeedbackPrivate**  | [boolean](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean)  | Always  |  Indicates whether the user has chosen to make their feedback score and feedback details private (hidden from other users). The percentage of positive feedback can still be returned, even if other feedback details are private.   
  
Since a bidder's user info is anonymous, this tag will be returned only to that bidder, and to the seller of an item that the user is bidding on.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll. Also returned if DetailLevel is not provided on input.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine. See [Anonymous user information](https://developer.ebay.com/api-docs/user-guides/static/trading-user-guide/user-mgmt-anonymous-info.html).  |  
|  Seller.**FeedbackRatingStar**  | [FeedbackRatingStarCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/FeedbackRatingStarCodeType.html)  | Always  |    
A visual indicator of an eBay user's Feedback score. A different colored star is used for each range of Feedback scores. See **FeedbackRatingStarCodeType** for specific values.   
**Note:** This field will stop being returned in **GetItemTransactions** and **GetSellerTransactions** on January 31, 2024.    
  
**Applicable values** : See [FeedbackRatingStar](https://developer.ebay.com/devzone/xml/docs/reference/ebay/extra/gtsllrlst.rspns.sllr.fdbckrtngstr.html).   
Code so that your app gracefully handles any future changes to this list.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll. Also returned if DetailLevel is not provided on input.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine.   |  
|  Seller.**FeedbackScore**  | [int](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#int)  | Always  |  The aggregate feedback score for a user. A user's feedback score is the net positive feedback minus the net negative feedback left for the user. Feedback scores are a quantitative expression of the desirability of dealing with a user as a buyer or a seller in either side of an order.   
  
Each order line item can result in one feedback entry for a given user (the buyer can leave feedback for the seller, and the seller can leave feedback for the buyer.). That one feedback can be positive, negative, or neutral. The aggregated feedback counts for a particular user represent that user's overall feedback score (referred to as a "feedback rating" on the eBay site).   
  
If the user has chosen to make their feedback private and that user is not the user identified in the request's authentication token, **FeedbackScore** is not returned and **FeedbackPrivate** is returned with a value of `true`.   
  
In **GetMyeBayBuying** and **GetMyeBaySelling** , feedback information (**FeedbackScore** and **FeedbackRatingStar**) is returned in **BidList.ItemArray.Item.Seller**. For **GetMyeBayBuying** , the feedback score of each seller with an item having received a bid from the buyer is returned. For **GetMyeBaySelling** , the feedback score of the seller is returned.   
  
**GetMyeBayBuying** and **GetMyeBaySelling** also return feedback information (**FeedbackScore** and **FeedbackRatingStar**) in **BidList.ItemArray.Item.SellingStatus.HighBidder**. **GetMyeBayBuying** returns feedback information on the high bidder of each item the buyer is bidding on. **GetMyeBaySelling** returns feedback information on the high bidder of each item the seller is selling.  
  
Since a bidder's user info is anonymous, the real feedback score will be returned only to that bidder, and to the seller of an item that the user is bidding on. For all other users, the value -99 is returned.   
  
**For GetOrders and GetItemTransactions only:** If using Trading WSDL Version 1019 or above, this field will only be returned to the buyer or seller, and no longer returned at all to third parties. If using a Trading WSDL older than Version 1019, the accurate Feedback Score for the user is returned to the buyer or seller, but a dummy value of `0` will be returned to all third parties.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll. Also returned if DetailLevel is not provided on input.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine. See [Anonymous user information](https://developer.ebay.com/api-docs/user-guides/static/trading-user-guide/user-mgmt-anonymous-info.html).  |  
|  Seller.**IDVerified**  | [boolean](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean)  | Always  |    
Indicates whether the user has been verified. For more information about the ID Verify program, see: [Protecting your account](https://pages.ebay.com/help/policies/identity-idverify.html)   
**Note:** This field will stop being returned in **GetItemTransactions** and **GetSellerTransactions** on January 31, 2024.    
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll. Also returned if DetailLevel is not provided on input.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine.   |  
|  Seller.**NewUser**  | [boolean](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean)  | Always  |  This boolean is returned as `true` if the eBay user has been registered on eBay for 30 days or less.   
**Note:** The **Buyer.NewUser** field will stop being returned in **GetItemTransactions** and **GetSellerTransactions** on January 31, 2024.    
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll. Also returned if DetailLevel is not provided on input.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine.   |  
|  Seller.**RegistrationDate**  | [dateTime](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#dateTime)  | Always  |  Indicates the date the specified user originally registered with eBay.   
  
Since a bidder's user info is anonymous, this tag will be returned only to that bidder, and to the seller of an item that the user is bidding on.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll. Also returned if DetailLevel is not provided on input.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine. See [Anonymous user information](https://developer.ebay.com/api-docs/user-guides/static/trading-user-guide/user-mgmt-anonymous-info.html).  |  
|  Seller.**SellerInfo**  | [SellerType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/SellerType.html)  | Always  |    
Contains information about a seller, including listing settings, listing preferences, seller rankings, and seller type.   
**Note:** This container will stop being returned in **GetItemTransactions** and **GetSellerTransactions** on January 31, 2024.    
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll. Also returned if DetailLevel is not provided on input.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Coarse, Fine, Medium.   |  
|  Seller.SellerInfo  
.**AllowPaymentEdit**  | [boolean](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean)  | Always  |    
Indicates whether the seller allows buyers to edit the total cost of an item during checkout.   
**Note:** The **SellerInfo** container and its child fields will stop being returned in **GetItemTransactions** and **GetSellerTransactions** on January 31, 2024.    
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll. Also returned if DetailLevel is not provided on input.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine.   |  
|  Seller.SellerInfo  
.**CheckoutEnabled**  | [boolean](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean)  | Always  |    
This flag indicates whether or not the seller's Checkout Enabled preference is turned on.   
**Note:** The **SellerInfo** container and its child fields will stop being returned in **GetItemTransactions** and **GetSellerTransactions** on January 31, 2024.    
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll. Also returned if DetailLevel is not provided on input.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine.   |  
|  Seller.SellerInfo  
.**CIPBankAccountStored**  | [boolean](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean)  | Always  |    
This boolean field indicates whether or not the seller has stored bank account information on file with eBay.   
**Note:** The **SellerInfo** container and its child fields will stop being returned in **GetItemTransactions** and **GetSellerTransactions** on January 31, 2024.    
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll. Also returned if DetailLevel is not provided on input.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine.   |  
|  Seller.SellerInfo.**GoodStanding**  | [boolean](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean)  | Always  |    
This boolean field indicates whether or not the seller is in good standing with eBay.   
**Note:** The **SellerInfo** container and its child fields will stop being returned in **GetItemTransactions** and **GetSellerTransactions** on January 31, 2024.    
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll. Also returned if DetailLevel is not provided on input.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine.   |  
|  Seller.SellerInfo  
.**QualifiesForB2BVAT**  | [boolean](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean)  | Always  |    
Indicates whether the user is subject to VAT. Users who have registered with eBay as VAT-exempt are not subject to VAT.   
**Note:** The **SellerInfo** container and its child fields will stop being returned in **GetItemTransactions** and **GetSellerTransactions** on January 31, 2024.    
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll. Also returned if DetailLevel is not provided on input.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine.   |  
|  Seller.SellerInfo  
.**SafePaymentExempt**  | [boolean](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean)  | Always  |    
If this field is `true`, the user is exempt from the requirement to offer at least one safe payment method when listing items.   
**Note:** The **SellerInfo** container and its child fields will stop being returned in **GetItemTransactions** and **GetSellerTransactions** on January 31, 2024.   
**Default:** false.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll. Also returned if DetailLevel is not provided on input.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine.   |  
|  Seller.SellerInfo.**SellerLevel**  | [SellerLevelCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/SellerLevelCodeType.html)  | Always  |    
This enumeration value indicates the user's eBay PowerSeller tier.   
**Note:** The **SellerInfo** container and its child fields will stop being returned in **GetItemTransactions** and **GetSellerTransactions** on January 31, 2024.    
  
**Applicable values** : See [SellerLevel](https://developer.ebay.com/devzone/xml/docs/reference/ebay/extra/gtsllrlst.rspns.sllr.sllrinf.sllrlvl.html).   
Code so that your app gracefully handles any future changes to this list.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll. Also returned if DetailLevel is not provided on input.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine.   |  
|  Seller.SellerInfo.**StoreOwner**  | [boolean](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean)  | Conditionally  |    
Boolean value indicates whether or not the seller is an eBay Store owner.   
**Note:** The **SellerInfo** container and its child fields will stop being returned in **GetItemTransactions** and **GetSellerTransactions** on January 31, 2024.    
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll. Also returned if DetailLevel is not provided on input.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine.   |  
|  Seller.SellerInfo.**StoreURL**  | [anyURI](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#anyURI)  | Conditionally  |    
The URL for the seller's eBay Store. This field is only returned if the seller is a store owner (look for a value of `true` in the **SellerInfo.StoreOwner** field).   
**Note:** The **SellerInfo** container and its child fields will stop being returned in **GetItemTransactions** and **GetSellerTransactions** on January 31, 2024.    
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll. Also returned if DetailLevel is not provided on input.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine.   |  
|  Seller.SellerInfo  
.**TopRatedSeller**  | [boolean](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean)  | Conditionally  |  This boolean field indicates if the seller is certified as a _Top Rated Seller_. Only Top Rated Sellers can qualify for Top Rated Plus listings, which receive the Top Rated Plus seal and other benefits.   
This field is only returned for the following sites: US, Germany, Austria, Switzerland, UK, Ireland, and Australia. The Top Rated Seller and Top Rated Plus listing requirements will differ by site. Below are some links to Help pages that discuss these requirements: 
  * eBay US: [Requirements to become Top Rated](https://www.ebay.com/help/policies/selling-policies/seller-standards-policy?id=4347&#section3)
  * eBay UK/IE: [Requirements to become Top Rated and the eBay Premium Service](https://www.ebay.co.uk/help/policies/selling-policies/seller-standards-policy?id=4347&#section3)
  * eBay DE/AT/CH: [ Anforderungen fur den Verkaufer mit Top-Bewertung](https://pages.ebay.de/help/sell/top-rated/2.html)
  * eBay AU: [ Requirements to become Top Rated](https://www.ebay.com.au/help/policies/selling-policies/seller-standards-policy?id=4347&#section3)

Top Rated Sellers, registered in the US, can qualify for Top Rated Seller programs in other countries as long as they meet the selling requirements in those countries. However, even if US sellers qualify for programs in other countries, they will not receive the Final Value Fee discount on sales in those countries.   
**Note:** The **SellerInfo** container and its child fields will stop being returned in **GetItemTransactions** and **GetSellerTransactions** on January 31, 2024.    
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll. Also returned if DetailLevel is not provided on input.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine.   |  
|  Seller.**Site**  | [SiteCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/SiteCodeType.html)  | Always  |  eBay site the user is registered with.   
  
Since a bidder's user info is anonymous, this tag will be returned only to that bidder, and to the seller of an item that the user is bidding on.   
  
**Applicable values** : See [Site](https://developer.ebay.com/devzone/xml/docs/reference/ebay/extra/gtsllrlst.rspns.sllr.st.html).   
Code so that your app gracefully handles any future changes to this list.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll. Also returned if DetailLevel is not provided on input.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine. See [Anonymous user information](https://developer.ebay.com/api-docs/user-guides/static/trading-user-guide/user-mgmt-anonymous-info.html).  |  
|  Seller.**Status**  | [UserStatusCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/UserStatusCodeType.html)  | Always  |  Indicates the user's registration/user status.   
  
**Applicable values** : See [Status](https://developer.ebay.com/devzone/xml/docs/reference/ebay/extra/gtsllrlst.rspns.sllr.stts.html).   
Code so that your app gracefully handles any future changes to this list.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll. Also returned if DetailLevel is not provided on input.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine.   |  
|  Seller.**UserAnonymized**  | [boolean](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean)  | Always  |  Indicates whether or not the User container has been made anonymous. If `true`, some elements in the User container have either been removed, or had their values changed to remove identifying characteristics. If false, all expected elements are returned, and no values are changed.   
  
Since a bidder's user info is anonymous, this tag is returned as false only to the bidder, and to the seller of an item that the user is bidding on. For all other users, this tag is returned as `true`.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine. See [Anonymous user information](https://developer.ebay.com/api-docs/user-guides/static/trading-user-guide/user-mgmt-anonymous-info.html).  |  
|  Seller.**UserID**  | [UserIDType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/UserIDType.html) ([string](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string))  | Always  |  Unique eBay user ID for the user.  
  
**Note:** Effective September 26, 2025, select developers will no longer receive username data for U.S. users through this field. Instead, an immutable user ID will be returned in its place. For more information, please refer to [Data Handling Compliance](https://developer.ebay.com/api-docs/static/data-handling-update.html).    
Since a bidder's user info is anonymous, this tag contains the actual value of an ID only for that bidder, and for the seller of an item that the user is bidding on. For other users, the actual value is replaced by an anonymous value, according to these rules:   
  
When bidding on items, **UserID** is replaced with the value "a****b" where a and b are random characters from the **UserID**. For example, if the **UserID** = `IBidALot`, it might be displayed as, "I****A".   
  
**Important:** In this format, the anonymous bidder ID can change for each auction.  For **GetMyeBayBuying** only, when bidding on items: **UserID** is replaced with the value "a****b" where a and b are random characters from the **UserID**.   
  
When bidding on items listed on the Philippines site: **UserID** is replaced with the value "Bidder X" where X is a number indicating the order of that user's first bid. For example, if the user was the third bidder, **UserID** = `Bidder 3`. Note that in this Philippines site format, the anonymous bidder ID stays the same for a given auction, but is different for different auctions. For example, a bidder who is the third and then the seventh bidder in an auction will be listed for both bids as "Bidder 3". However, if that same bidder is the first bidder on a different auction, the bidder will be listed for that auction as "Bidder 1", not "Bidder 3".   
  
For **GetMyeBayBuying** only, when bidding on items listed on the UK and AU sites: **UserID** is replaced with the string "High Bidder".   
  
For **PlaceOffer** , see also **SellingStatus.HighBidder**.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll. Also returned if DetailLevel is not provided on input.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine. See [Anonymous user information](https://developer.ebay.com/api-docs/user-guides/static/trading-user-guide/user-mgmt-anonymous-info.html).  |  
|  Seller.**UserIDChanged**  | [boolean](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#boolean)  | Always  |  If `true`, identifies a user whose ID has changed within the last 30 days. Does not indicate a new user (see **NewUser**).   
  
Since a bidder's user info is anonymous, this tag will be returned only to that bidder, and to the seller of an item that the user is bidding on.   
  
**Note:** For the **GetItemTransactions** call, this field is only returned to the seller of the order; this field is not returned for the buyer or third party.    
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll. Also returned if DetailLevel is not provided on input.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine. See [Anonymous user information](https://developer.ebay.com/api-docs/user-guides/static/trading-user-guide/user-mgmt-anonymous-info.html).  |  
|  Seller.**UserIDLastChanged**  | [dateTime](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#dateTime)  | Always  |    
Date and time when the user last changed their eBay user ID (in GMT).   
**Note:** The **Buyer.UserIDLastChanged** field will stop being returned in **GetItemTransactions** and **GetSellerTransactions** on January 31, 2024.    
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll. Also returned if DetailLevel is not provided on input.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine. See [Anonymous user information](https://developer.ebay.com/api-docs/user-guides/static/trading-user-guide/user-mgmt-anonymous-info.html).  |  
|  Seller.**VATStatus**  | [VATStatusCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/VATStatusCodeType.html)  | Always  |  Indicates whether or not the user is subject to VAT. Users who have registered with eBay as VAT-exempt are not subject to VAT. See documentation on Value-Added Tax (VAT).   
  
**Applicable values** :   
  


CustomCode
    (out) Reserved for internal or future use 

NoVATTax
    (out) VAT is not applicable 

VATExempt
    (out) Residence in a country with VAT and user is registered as VAT-exempt 

VATTax
    (out) Residence in a country with VAT and user is not registered as VAT-exempt   
Code so that your app gracefully handles any future changes to this list.   
  
[**DetailLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#DetailLevel) ItemReturnDescription, ReturnAll. Also returned if DetailLevel is not provided on input.   
  
[**GranularityLevel:**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#GranularityLevel) Fine. See [Vat-exempt sellers](https://developer.ebay.com/api-docs/user-guides/static/trading-user-guide/taxes-vat.html#exempt).  |  
|  **Standard Output Fields**  |  
| --- |  
|  **Ack**  | [AckCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/AckCodeType.html)  | Always  |  A token representing the application-level acknowledgement code that indicates the response status (e.g., success). The **AckCodeType** list specifies the possible values for the **Ack** field.   
  
**Applicable values** :   
  


CustomCode
    (out) Reserved for internal or future use. 

Failure
    (out) This value indicates that the call request processing failed. 

Success
    (out) This value indicates that the call request was processed successfully without any issues. 

Warning
    (out) This value indicates that the call request was successful, but processing was not without any issues. These issues can be checked in the **Errors** container, that will also be returned when one or more known issues occur with the call request.   
(Not all values in [AckCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/AckCodeType.html) apply to this field.)  
  
Code so that your app gracefully handles any future changes to this list.   |  
| --- | --- | --- | --- |  
|  **Build**  | [string](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string)  | Always  |  This refers to the specific software build that eBay used when processing the request and generating the response. This includes the version number plus additional information. eBay Developer Support may request the build information when helping you resolve technical issues.   |  
|  **CorrelationID**  | [string](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string)  | Conditionally  |  Most Trading API calls support a **MessageID** element in the request and a **CorrelationID** element in the response. If you pass in a **MessageID** in a request, the same value will be returned in the **CorrelationID** field in the response. Pairing these values can help you track and confirm that a response is returned for every request and to match specific responses to specific requests. If you do not pass a **MessageID** value in the request, **CorrelationID** is not returned.   |  
|  **Errors**  | [ErrorType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/ErrorType.html)  | Conditionally,   
[repeatable](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#repeatable): [0..*]  |  A list of application-level errors (if any) that occurred when eBay processed the request.   |  
|  Errors.**ErrorClassification**  | [ErrorClassificationCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/ErrorClassificationCodeType.html)  | Conditionally  |  API errors are divided between two classes: system errors and request errors.   
  
**Applicable values** :   
  


CustomCode
    (out) Reserved for internal or future use. 

RequestError
    (out) An error has occurred either as a result of a problem in the sending application or because the application's end-user has attempted to submit invalid data (or missing data). In these cases, do not retry the request. The problem must be corrected before the request can be made again. If the problem is due to something in the application (such as a missing required field), the application must be changed. If the problem is a result of end-user data, the application must alert the end-user to the problem and provide the means for the end-user to correct the data. Once the problem in the application or data is resolved, resend the request to eBay with the corrected data. 

SystemError
    (out) Indicates that an error has occurred on the eBay system side, such as a database or server down. An application can retry the request as-is a reasonable number of times (eBay recommends twice). If the error persists, contact Developer Technical Support. Once the problem has been resolved, the request may be resent in its original form.   
Code so that your app gracefully handles any future changes to this list.   |  
|  Errors.**ErrorCode**  | [token](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#token)  | Conditionally  |  A unique code that identifies the particular error condition that occurred. Your application can use error codes as identifiers in your customized error-handling algorithms. See [Errors By Number](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/Errors/ErrorMessages.html#ErrorsByNumber).  |  
|  Errors.**ErrorParameters**  | [ErrorParameterType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/ErrorParameterType.html)  | Conditionally,   
[repeatable](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#repeatable): [0..*]  |  This optional element carries a list of context-specific error variables that indicate details about the error condition. These are useful when multiple instances of **ErrorType** are returned.   |  
| Errors.**ErrorParameters**  
[ attribute **ParamID** ]  | [string](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string)  | Conditionally  |  This optional element carries a list of context-specific error variables that indicate details about the error condition. These are useful when multiple instances of **ErrorType** are returned.   |  
|  Errors.ErrorParameters.**Value**  | [string](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string)  | Conditionally  |  This is the value of the request parameter noted in the **ParamID** attribute. So, if the **ParamID** value was **ItemID** , the value in this field would be the actual value of that **ItemID**.   |  
|  Errors.**LongMessage**  | [string](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string)  | Conditionally  |  A more detailed description of the condition that raised the error.   |  
|  Errors.**SeverityCode**  | [SeverityCodeType](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/SeverityCodeType.html)  | Conditionally  |  Indicates whether the error is a severe error (causing the request to fail) or an informational error (a warning) that should be communicated to the user.   
  
**Applicable values** :   
  


CustomCode
    (out) Reserved for internal or future use. 

Error
    (out) The request that triggered the error was not processed successfully. When a serious application-level error occurs, the error is returned instead of the business data.   
  
If the source of the problem is within the application (such as a missing required element), change the application before you retry the request. 
  * If the problem is due to end-user input data, please alert the end-user to the problem and provide the means for them to correct the data. Once the problem in the application or data is resolved, you can attempt to re-send the request to eBay. 
  * If the source of the problem is on eBay's side, An application can retry the request as-is a reasonable number of times (eBay recommends twice). If the error persists, contact Developer Technical Support. Once the problem has been resolved, the request may be resent in its original form. 

  
  
See the [Error handling](https://developer.ebay.com/api-docs/user-guides/static/make-a-call/error-handling.html) section of the Making a Trading API call guide for more information. 

Warning
    (out) The request was processed successfully, but something occurred that may affect your application or the user. For example, eBay may have changed a value the user sent in. In this case, eBay returns a normal, successful response and also returns the warning.   
  
When a warning occurs, the error is returned in addition to the business data. In this case, you do not need to retry the request (as the original request was successful). However, depending on the cause or nature of the warning, you might need to contact either the end user or eBay to effect a long term solution to the problem to prevent it from reoccurring in the future.   
Code so that your app gracefully handles any future changes to this list.   |  
|  Errors.**ShortMessage**  | [string](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string)  | Conditionally  |  A brief description of the condition that raised the error.   |  
|  **HardExpirationWarning**  | [string](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string)  | Conditionally  |  Expiration date of the user's authentication token. Only returned within the 7-day period prior to a token's expiration. To ensure that user authentication tokens are secure and to help avoid a user's token being compromised, tokens have a limited life span. A token is only valid for a period of time (set by eBay). After this amount of time has passed, the token expires and must be replaced with a new token.   |  
|  **Timestamp**  | [dateTime](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#dateTime)  | Always  |  This value represents the date and time when eBay processed the request. The time zone of this value is GMT and the format is the ISO 8601 date and time format (YYYY-MM-DDTHH:MM:SS.SSSZ). See the **Time Values** section in the eBay Features Guide for information about this time format and converting to and from the GMT time zone.   
  
**Note:** Trading API calls are designed to retrieve very large sets of metadata that change once a day or less often. To improve performance, these calls return cached responses when you request all available data (with no filters). When this occurs, this time value reflects the time the cached response was created. Thus, this value is not necessarily when the request was processed. However, if you specify an input filter to reduce the amount of data returned, the calls retrieve the latest data (not cached). When this occurs, this time value does reflect when the request was processed.  |  
|  **Version**  | [string](https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/simpletypes.html#string)  | Always  |  The version of the response payload schema. Indicates the version of the schema that eBay used to process the request. See the **Standard Data for All Calls** section in the eBay Features Guide for information on using the response version when troubleshooting **CustomCode** values that appear in the response.   |  
  
  
  
|  [Input](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Input "Details about every field that can be used in this call") [Output](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Output "Details about every field that might be returned by this call") Detail Controls [Samples](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Samples "Illustrations of how to use this call") [Change History](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#ChangeHistory "Details about changes to this call")  |  
| --- |  
## Detail Controls
  

### DetailLevel
The [DetailLevel](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Request.DetailLevel) input field influences which [call-specific fields](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#callOutputFields) may be returned. (All [standard output fields](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#stdOutputFields) are returned regardless of DetailLevel.)
The **none** column indicates the fields that are returned when you do not specify a DetailLevel.
Please avoid using a DetailLevel of ReturnAll with GetSellerList when possible. 
Many item details, such as item descriptions and listing enhancements, are unlikely to change. After an initial request for detailed information about items, subsequent requests can omit the DetailLevel field and thus obtain only the information about items that is likely to change. (Alternatively, consider using GetSellerEvents instead of GetSellerList.) If you need to use ReturnAll to retrieve all details for a set of items, please use a smaller EntriesPerPage value to limit the number of items returned per call. Also, use a shorter time range in EndTimeFrom and EndTimeTo for better performance.   
| Y  | The field is always returned.  |  
| --- | --- |  
| (Y)  | The field is conditionally returned. See the field documentation for clarification of conditions.  |  
| -  | The field is not returned.  |  
| Output Field  | none  | ItemReturnAttributes  | ItemReturnDescription  | ReturnAll  |  
| --- | --- | --- | --- | --- |  
| [**HasMoreItems**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.HasMoreItems)  | Y  | -  | Y  | Y  |  
| [**ItemArray**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray)  | Y  | -  | Y  | Y  |  
| [ItemArray.**Item**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item)  | (Y)  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.**ApplicationData**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ApplicationData)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.**AutoPay**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.AutoPay)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.**BuyerGuaranteePrice**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.BuyerGuaranteePrice)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.**BuyerProtection**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.BuyerProtection)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.**BuyItNowPrice**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.BuyItNowPrice)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.**Charity**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Charity)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.Charity.**CharityID**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Charity.CharityID)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.Charity.**CharityListing**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Charity.CharityListing)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.Charity.**CharityName**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Charity.CharityName)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.Charity.**DonationPercent**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Charity.DonationPercent)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.Charity.**LogoURL**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Charity.LogoURL)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.Charity.**Mission**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Charity.Mission)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.Charity.**Status**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Charity.Status)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.**ConditionDescription**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ConditionDescription)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.**Country**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Country)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.**CrossBorderTrade**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.CrossBorderTrade)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.**Currency**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Currency)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.**Description**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Description)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.**DisableBuyerRequirements**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.DisableBuyerRequirements)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.**DiscountPriceInfo**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.DiscountPriceInfo)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.DiscountPriceInfo.**MadeForOutletComparisonPrice**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.DiscountPriceInfo.MadeForOutletComparisonPrice)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.DiscountPriceInfo.**MinimumAdvertisedPrice**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.DiscountPriceInfo.MinimumAdvertisedPrice)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.DiscountPriceInfo.**MinimumAdvertisedPriceExposure**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.DiscountPriceInfo.MinimumAdvertisedPriceExposure)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.DiscountPriceInfo.**OriginalRetailPrice**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.DiscountPriceInfo.OriginalRetailPrice)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.DiscountPriceInfo.**PricingTreatment**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.DiscountPriceInfo.PricingTreatment)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.DiscountPriceInfo.**SoldOffeBay**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.DiscountPriceInfo.SoldOffeBay)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.DiscountPriceInfo.**SoldOneBay**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.DiscountPriceInfo.SoldOneBay)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.**ExtendedSellerContactDetails**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ExtendedSellerContactDetails)  | (Y)  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.ExtendedSellerContactDetails.**ContactHoursDetails**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ExtendedSellerContactDetails.ContactHoursDetails)  | (Y)  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.ExtendedSellerContactDetails.ContactHoursDetails  
.**Hours1AnyTime**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ExtendedSellerContactDetails.ContactHoursDetails.Hours1AnyTime)  | (Y)  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.ExtendedSellerContactDetails.ContactHoursDetails  
.**Hours1Days**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ExtendedSellerContactDetails.ContactHoursDetails.Hours1Days)  | (Y)  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.ExtendedSellerContactDetails.ContactHoursDetails  
.**Hours1From**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ExtendedSellerContactDetails.ContactHoursDetails.Hours1From)  | (Y)  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.ExtendedSellerContactDetails.ContactHoursDetails  
.**Hours1To**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ExtendedSellerContactDetails.ContactHoursDetails.Hours1To)  | (Y)  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.ExtendedSellerContactDetails.ContactHoursDetails  
.**Hours2AnyTime**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ExtendedSellerContactDetails.ContactHoursDetails.Hours2AnyTime)  | (Y)  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.ExtendedSellerContactDetails.ContactHoursDetails  
.**Hours2Days**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ExtendedSellerContactDetails.ContactHoursDetails.Hours2Days)  | (Y)  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.ExtendedSellerContactDetails.ContactHoursDetails  
.**Hours2From**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ExtendedSellerContactDetails.ContactHoursDetails.Hours2From)  | (Y)  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.ExtendedSellerContactDetails.ContactHoursDetails  
.**Hours2To**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ExtendedSellerContactDetails.ContactHoursDetails.Hours2To)  | (Y)  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.ExtendedSellerContactDetails.ContactHoursDetails  
.**TimeZoneID**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ExtendedSellerContactDetails.ContactHoursDetails.TimeZoneID)  | (Y)  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.**FreeAddedCategory**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.FreeAddedCategory)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.FreeAddedCategory.**CategoryID**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.FreeAddedCategory.CategoryID)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.FreeAddedCategory.**CategoryName**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.FreeAddedCategory.CategoryName)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.**HitCount**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.HitCount)  | -  | -  | -  | (Y)  |  
| [ItemArray.Item.**IntegratedMerchantCreditCardEnabled**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.IntegratedMerchantCreditCardEnabled)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.**InventoryTrackingMethod**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.InventoryTrackingMethod)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.**ItemID**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ItemID)  | (Y)  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.**ItemPolicyViolation**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ItemPolicyViolation)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.ItemPolicyViolation.**PolicyID**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ItemPolicyViolation.PolicyID)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.ItemPolicyViolation.**PolicyText**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ItemPolicyViolation.PolicyText)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.**ListingDetails**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ListingDetails)  | (Y)  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.ListingDetails.**Adult**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ListingDetails.Adult)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.ListingDetails.**BestOfferAutoAcceptPrice**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ListingDetails.BestOfferAutoAcceptPrice)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.ListingDetails.**BindingAuction**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ListingDetails.BindingAuction)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.ListingDetails.**CheckoutEnabled**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ListingDetails.CheckoutEnabled)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.ListingDetails.**ConvertedBuyItNowPrice**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ListingDetails.ConvertedBuyItNowPrice)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.ListingDetails.**ConvertedReservePrice**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ListingDetails.ConvertedReservePrice)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.ListingDetails.**ConvertedStartPrice**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ListingDetails.ConvertedStartPrice)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.ListingDetails.**EndTime**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ListingDetails.EndTime)  | (Y)  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.ListingDetails.**HasPublicMessages**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ListingDetails.HasPublicMessages)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.ListingDetails.**HasReservePrice**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ListingDetails.HasReservePrice)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.ListingDetails.**HasUnansweredQuestions**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ListingDetails.HasUnansweredQuestions)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.ListingDetails.**MinimumBestOfferPrice**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ListingDetails.MinimumBestOfferPrice)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.ListingDetails.**RelistedItemID**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ListingDetails.RelistedItemID)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.ListingDetails.**StartTime**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ListingDetails.StartTime)  | (Y)  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.ListingDetails.**ViewItemURL**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ListingDetails.ViewItemURL)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.ListingDetails.**ViewItemURLForNaturalSearch**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ListingDetails.ViewItemURLForNaturalSearch)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.**ListingDuration**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ListingDuration)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.**ListingEnhancement**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ListingEnhancement)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.**ListingSubtype2**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ListingSubtype2)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.**ListingType**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ListingType)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.**Location**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Location)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.**PaymentMethods**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.PaymentMethods)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.**PictureDetails**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.PictureDetails)  | (Y)  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.PictureDetails.**GalleryType**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.PictureDetails.GalleryType)  | (Y)  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.**PrimaryCategory**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.PrimaryCategory)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.PrimaryCategory.**CategoryID**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.PrimaryCategory.CategoryID)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.PrimaryCategory.**CategoryName**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.PrimaryCategory.CategoryName)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.**PrivateListing**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.PrivateListing)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.**ProxyItem**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ProxyItem)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.**Quantity**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Quantity)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.**QuantityAvailableHint**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.QuantityAvailableHint)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.**QuantityThreshold**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.QuantityThreshold)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.**ReservePrice**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ReservePrice)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.**ReturnPolicy**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ReturnPolicy)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.ReturnPolicy.**Description**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ReturnPolicy.Description)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.ReturnPolicy.**InternationalRefundOption**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ReturnPolicy.InternationalRefundOption)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.ReturnPolicy.**InternationalReturnsAcceptedOption**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ReturnPolicy.InternationalReturnsAcceptedOption)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.ReturnPolicy.**InternationalReturnsWithinOption**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ReturnPolicy.InternationalReturnsWithinOption)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.ReturnPolicy.**InternationalShippingCostPaidByOption**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ReturnPolicy.InternationalShippingCostPaidByOption)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.ReturnPolicy.**Refund**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ReturnPolicy.Refund)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.ReturnPolicy.**RefundOption**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ReturnPolicy.RefundOption)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.ReturnPolicy.**ReturnsAccepted**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ReturnPolicy.ReturnsAccepted)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.ReturnPolicy.**ReturnsAcceptedOption**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ReturnPolicy.ReturnsAcceptedOption)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.ReturnPolicy.**ReturnsWithin**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ReturnPolicy.ReturnsWithin)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.ReturnPolicy.**ReturnsWithinOption**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ReturnPolicy.ReturnsWithinOption)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.ReturnPolicy.**ShippingCostPaidBy**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ReturnPolicy.ShippingCostPaidBy)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.ReturnPolicy.**ShippingCostPaidByOption**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ReturnPolicy.ShippingCostPaidByOption)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.**ReviseStatus**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ReviseStatus)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.ReviseStatus.**ItemRevised**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ReviseStatus.ItemRevised)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.**SecondaryCategory**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SecondaryCategory)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.SecondaryCategory.**CategoryID**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SecondaryCategory.CategoryID)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.SecondaryCategory.**CategoryName**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SecondaryCategory.CategoryName)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.**SellerContactDetails**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellerContactDetails)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.**SellerProfiles**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellerProfiles)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.SellerProfiles.**SellerPaymentProfile**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellerProfiles.SellerPaymentProfile)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.SellerProfiles.SellerPaymentProfile  
.**PaymentProfileID**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellerProfiles.SellerPaymentProfile.PaymentProfileID)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.SellerProfiles.SellerPaymentProfile  
.**PaymentProfileName**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellerProfiles.SellerPaymentProfile.PaymentProfileName)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.SellerProfiles.**SellerReturnProfile**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellerProfiles.SellerReturnProfile)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.SellerProfiles.SellerReturnProfile.**ReturnProfileID**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellerProfiles.SellerReturnProfile.ReturnProfileID)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.SellerProfiles.SellerReturnProfile  
.**ReturnProfileName**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellerProfiles.SellerReturnProfile.ReturnProfileName)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.SellerProfiles.**SellerShippingProfile**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellerProfiles.SellerShippingProfile)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.SellerProfiles.SellerShippingProfile  
.**ShippingProfileID**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellerProfiles.SellerShippingProfile.ShippingProfileID)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.SellerProfiles.SellerShippingProfile  
.**ShippingProfileName**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellerProfiles.SellerShippingProfile.ShippingProfileName)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.**SellingStatus**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.SellingStatus.**AdminEnded**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.AdminEnded)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.SellingStatus.**BidCount**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.BidCount)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.SellingStatus.**BidIncrement**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.BidIncrement)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.SellingStatus.**ConvertedCurrentPrice**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.ConvertedCurrentPrice)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.SellingStatus.**CurrentPrice**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.CurrentPrice)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.SellingStatus.**HighBidder**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.HighBidder)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.SellingStatus.HighBidder.**AboutMePage**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.HighBidder.AboutMePage)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.SellingStatus.HighBidder.**BuyerInfo**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.HighBidder.BuyerInfo)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.SellingStatus.HighBidder.BuyerInfo.**ShippingAddress**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.HighBidder.BuyerInfo.ShippingAddress)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.SellingStatus.HighBidder.BuyerInfo.ShippingAddress  
.**Country**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.HighBidder.BuyerInfo.ShippingAddress.Country)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.SellingStatus.HighBidder.BuyerInfo.ShippingAddress  
.**PostalCode**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.HighBidder.BuyerInfo.ShippingAddress.PostalCode)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.SellingStatus.HighBidder.**eBayGoodStanding**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.HighBidder.eBayGoodStanding)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.SellingStatus.HighBidder.**EIASToken**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.HighBidder.EIASToken)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.SellingStatus.HighBidder.**Email**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.HighBidder.Email)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.SellingStatus.HighBidder.**FeedbackPrivate**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.HighBidder.FeedbackPrivate)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.SellingStatus.HighBidder.**FeedbackRatingStar**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.HighBidder.FeedbackRatingStar)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.SellingStatus.HighBidder.**FeedbackScore**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.HighBidder.FeedbackScore)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.SellingStatus.HighBidder.**IDVerified**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.HighBidder.IDVerified)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.SellingStatus.HighBidder.**NewUser**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.HighBidder.NewUser)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.SellingStatus.HighBidder.**RegistrationDate**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.HighBidder.RegistrationDate)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.SellingStatus.HighBidder.**Site**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.HighBidder.Site)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.SellingStatus.HighBidder.**Status**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.HighBidder.Status)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.SellingStatus.HighBidder.**UserID**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.HighBidder.UserID)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.SellingStatus.HighBidder.**UserIDChanged**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.HighBidder.UserIDChanged)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.SellingStatus.HighBidder.**UserIDLastChanged**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.HighBidder.UserIDLastChanged)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.SellingStatus.HighBidder.**VATStatus**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.HighBidder.VATStatus)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.SellingStatus.**LeadCount**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.LeadCount)  | -  | -  | -  | (Y)  |  
| [ItemArray.Item.SellingStatus.**ListingStatus**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.ListingStatus)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.SellingStatus.**MinimumToBid**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.MinimumToBid)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.SellingStatus.**PromotionalSaleDetails**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.PromotionalSaleDetails)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.SellingStatus.PromotionalSaleDetails.**EndTime**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.PromotionalSaleDetails.EndTime)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.SellingStatus.PromotionalSaleDetails.**OriginalPrice**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.PromotionalSaleDetails.OriginalPrice)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.SellingStatus.PromotionalSaleDetails.**StartTime**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.PromotionalSaleDetails.StartTime)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.SellingStatus.**QuantitySold**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.QuantitySold)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.SellingStatus.**ReserveMet**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.ReserveMet)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.SellingStatus.**SecondChanceEligible**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.SecondChanceEligible)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.**ShippingDetails**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.ShippingDetails.**CalculatedShippingRate**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.CalculatedShippingRate)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.ShippingDetails.CalculatedShippingRate  
.**PackagingHandlingCosts**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.CalculatedShippingRate.PackagingHandlingCosts)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.ShippingDetails.**ExcludeShipToLocation**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.ExcludeShipToLocation)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.ShippingDetails.**GlobalShipping**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.GlobalShipping)  | (Y)  | (Y)  | (Y)  | (Y)  |  
| [ItemArray.Item.ShippingDetails.**InternationalShippingServiceOption**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.InternationalShippingServiceOption)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.ShippingDetails.InternationalShippingServiceOption  
.**ShippingService**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.InternationalShippingServiceOption.ShippingService)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.ShippingDetails.InternationalShippingServiceOption  
.**ShippingServiceAdditionalCost**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.InternationalShippingServiceOption.ShippingServiceAdditionalCost)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.ShippingDetails.InternationalShippingServiceOption  
.**ShippingServiceCost**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.InternationalShippingServiceOption.ShippingServiceCost)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.ShippingDetails.InternationalShippingServiceOption  
.**ShippingServicePriority**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.InternationalShippingServiceOption.ShippingServicePriority)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.ShippingDetails.InternationalShippingServiceOption  
.**ShipToLocation**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.InternationalShippingServiceOption.ShipToLocation)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.ShippingDetails.**PaymentEdited**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.PaymentEdited)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.ShippingDetails.**RateTableDetails**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.RateTableDetails)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.ShippingDetails.RateTableDetails.**DomesticRateTable**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.RateTableDetails.DomesticRateTable)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.ShippingDetails.RateTableDetails  
.**DomesticRateTableId**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.RateTableDetails.DomesticRateTableId)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.ShippingDetails.RateTableDetails  
.**InternationalRateTable**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.RateTableDetails.InternationalRateTable)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.ShippingDetails.RateTableDetails  
.**InternationalRateTableId**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.RateTableDetails.InternationalRateTableId)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.ShippingDetails.**SalesTax**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.SalesTax)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.ShippingDetails.SalesTax.**SalesTaxPercent**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.SalesTax.SalesTaxPercent)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.ShippingDetails.SalesTax.**SalesTaxState**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.SalesTax.SalesTaxState)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.ShippingDetails.SalesTax.**ShippingIncludedInTax**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.SalesTax.ShippingIncludedInTax)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.ShippingDetails  
.**SellerExcludeShipToLocationsPreference**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.SellerExcludeShipToLocationsPreference)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.ShippingDetails.**ShippingServiceOptions**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.ShippingServiceOptions)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.ShippingDetails.ShippingServiceOptions  
.**ExpeditedService**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.ShippingServiceOptions.ExpeditedService)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.ShippingDetails.ShippingServiceOptions  
.**ShippingService**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.ShippingServiceOptions.ShippingService)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.ShippingDetails.ShippingServiceOptions  
.**ShippingServiceAdditionalCost**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.ShippingServiceOptions.ShippingServiceAdditionalCost)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.ShippingDetails.ShippingServiceOptions  
.**ShippingServiceCost**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.ShippingServiceOptions.ShippingServiceCost)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.ShippingDetails.ShippingServiceOptions  
.**ShippingServicePriority**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.ShippingServiceOptions.ShippingServicePriority)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.ShippingDetails.ShippingServiceOptions  
.**ShippingTimeMax**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.ShippingServiceOptions.ShippingTimeMax)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.ShippingDetails.ShippingServiceOptions  
.**ShippingTimeMin**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.ShippingServiceOptions.ShippingTimeMin)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.ShippingDetails.**TaxTable**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.TaxTable)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.ShippingDetails.TaxTable.**TaxJurisdiction**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.TaxTable.TaxJurisdiction)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.ShippingDetails.TaxTable.TaxJurisdiction  
.**JurisdictionID**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.TaxTable.TaxJurisdiction.JurisdictionID)  | (Y)  | -  | -  | (Y)  |  
| [ItemArray.Item.ShippingDetails.TaxTable.TaxJurisdiction  
.**SalesTaxPercent**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.TaxTable.TaxJurisdiction.SalesTaxPercent)  | (Y)  | -  | -  | (Y)  |  
| [ItemArray.Item.ShippingDetails.TaxTable.TaxJurisdiction  
.**ShippingIncludedInTax**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.TaxTable.TaxJurisdiction.ShippingIncludedInTax)  | (Y)  | -  | -  | (Y)  |  
| [ItemArray.Item.ShippingDetails.**ThirdPartyCheckout**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.ThirdPartyCheckout)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.**ShipToLocations**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShipToLocations)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.**Site**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Site)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.**SKU**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SKU)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.**StartPrice**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.StartPrice)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.**Storefront**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Storefront)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.Storefront.**StoreCategory2ID**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Storefront.StoreCategory2ID)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.Storefront.**StoreCategoryID**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Storefront.StoreCategoryID)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.Storefront.**StoreURL**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Storefront.StoreURL)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.**TimeLeft**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.TimeLeft)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.**Title**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Title)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.**TotalQuestionCount**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.TotalQuestionCount)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.**Variations**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.Variations.**Variation**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.Variations.Variation.**Quantity**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.Quantity)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.Variations.Variation.**SellingStatus**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.Variations.Variation.SellingStatus.HighBidder  
.**AboutMePage**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.HighBidder.AboutMePage)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.Variations.Variation.SellingStatus.HighBidder  
.**BuyerInfo**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.HighBidder.BuyerInfo)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.Variations.Variation.SellingStatus.HighBidder  
.BuyerInfo.**ShippingAddress**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.HighBidder.BuyerInfo.ShippingAddress)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.Variations.Variation.SellingStatus.HighBidder  
.BuyerInfo.ShippingAddress.**Country**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.HighBidder.BuyerInfo.ShippingAddress.Country)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.Variations.Variation.SellingStatus.HighBidder  
.BuyerInfo.ShippingAddress.**PostalCode**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.HighBidder.BuyerInfo.ShippingAddress.PostalCode)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.Variations.Variation.SellingStatus.HighBidder  
.**eBayGoodStanding**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.HighBidder.eBayGoodStanding)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.Variations.Variation.SellingStatus.HighBidder  
.**EIASToken**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.HighBidder.EIASToken)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.Variations.Variation.SellingStatus.HighBidder  
.**Email**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.HighBidder.Email)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.Variations.Variation.SellingStatus.HighBidder  
.**FeedbackPrivate**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.HighBidder.FeedbackPrivate)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.Variations.Variation.SellingStatus.HighBidder  
.**FeedbackRatingStar**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.HighBidder.FeedbackRatingStar)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.Variations.Variation.SellingStatus.HighBidder  
.**FeedbackScore**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.HighBidder.FeedbackScore)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.Variations.Variation.SellingStatus.HighBidder  
.**IDVerified**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.HighBidder.IDVerified)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.Variations.Variation.SellingStatus.HighBidder  
.**NewUser**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.HighBidder.NewUser)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.Variations.Variation.SellingStatus.HighBidder  
.**RegistrationDate**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.HighBidder.RegistrationDate)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.Variations.Variation.SellingStatus.HighBidder.**Site**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.HighBidder.Site)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.Variations.Variation.SellingStatus.HighBidder  
.**Status**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.HighBidder.Status)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.Variations.Variation.SellingStatus.HighBidder  
.**UserID**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.HighBidder.UserID)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.Variations.Variation.SellingStatus.HighBidder  
.**UserIDChanged**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.HighBidder.UserIDChanged)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.Variations.Variation.SellingStatus.HighBidder  
.**UserIDLastChanged**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.HighBidder.UserIDLastChanged)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.Variations.Variation.SellingStatus.HighBidder  
.**VATStatus**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.HighBidder.VATStatus)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.Variations.Variation.SellingStatus  
.PromotionalSaleDetails.**EndTime**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.PromotionalSaleDetails.EndTime)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.Variations.Variation.SellingStatus  
.PromotionalSaleDetails.**OriginalPrice**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.PromotionalSaleDetails.OriginalPrice)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.Variations.Variation.SellingStatus  
.PromotionalSaleDetails.**StartTime**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.PromotionalSaleDetails.StartTime)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.Variations.Variation.SellingStatus.**QuantitySold**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.QuantitySold)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.Variations.Variation.**SKU**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SKU)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.Variations.Variation.**StartPrice**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.StartPrice)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.Variations.Variation  
.**VariationProductListingDetails**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.VariationProductListingDetails)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.Variations.Variation  
.VariationProductListingDetails.**EAN**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.VariationProductListingDetails.EAN)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.Variations.Variation  
.VariationProductListingDetails.**ISBN**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.VariationProductListingDetails.ISBN)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.Variations.Variation  
.VariationProductListingDetails.**UPC**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.VariationProductListingDetails.UPC)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.Variations.Variation.**VariationSpecifics**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.VariationSpecifics)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.Variations.Variation.VariationSpecifics  
.**NameValueList**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.VariationSpecifics.NameValueList)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.Variations.Variation.VariationSpecifics  
.NameValueList.**Name**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.VariationSpecifics.NameValueList.Name)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.Variations.Variation.VariationSpecifics  
.NameValueList.**Value**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.VariationSpecifics.NameValueList.Value)  | -  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.**WatchCount**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.WatchCount)  | -  | -  | (Y)  | (Y)  |  
| [**ItemsPerPage**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemsPerPage)  | Y  | -  | Y  | Y  |  
| [**PageNumber**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.PageNumber)  | Y  | -  | Y  | Y  |  
| [**PaginationResult**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.PaginationResult)  | Y  | -  | Y  | Y  |  
| [**ReturnedItemCountActual**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ReturnedItemCountActual)  | Y  | -  | Y  | Y  |  
| [Seller.**AboutMePage**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.AboutMePage)  | Y  | -  | Y  | Y  |  
| [Seller.**eBayGoodStanding**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.eBayGoodStanding)  | Y  | -  | Y  | Y  |  
| [Seller.**Email**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.Email)  | -  | -  | -  | (Y)  |  
| [Seller.**FeedbackPrivate**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.FeedbackPrivate)  | Y  | -  | Y  | Y  |  
| [Seller.**FeedbackRatingStar**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.FeedbackRatingStar)  | Y  | -  | Y  | Y  |  
| [Seller.**FeedbackScore**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.FeedbackScore)  | Y  | -  | Y  | Y  |  
| [Seller.**IDVerified**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.IDVerified)  | Y  | -  | Y  | Y  |  
| [Seller.**NewUser**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.NewUser)  | Y  | -  | Y  | Y  |  
| [Seller.**RegistrationDate**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.RegistrationDate)  | Y  | -  | Y  | Y  |  
| [Seller.**SellerInfo**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.SellerInfo)  | Y  | -  | Y  | Y  |  
| [Seller.SellerInfo.**AllowPaymentEdit**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.SellerInfo.AllowPaymentEdit)  | Y  | -  | Y  | Y  |  
| [Seller.SellerInfo.**CheckoutEnabled**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.SellerInfo.CheckoutEnabled)  | Y  | -  | Y  | Y  |  
| [Seller.SellerInfo.**CIPBankAccountStored**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.SellerInfo.CIPBankAccountStored)  | Y  | -  | Y  | Y  |  
| [Seller.SellerInfo.**GoodStanding**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.SellerInfo.GoodStanding)  | Y  | -  | Y  | Y  |  
| [Seller.SellerInfo.**QualifiesForB2BVAT**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.SellerInfo.QualifiesForB2BVAT)  | Y  | -  | Y  | Y  |  
| [Seller.SellerInfo.**SafePaymentExempt**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.SellerInfo.SafePaymentExempt)  | Y  | -  | Y  | Y  |  
| [Seller.SellerInfo.**SellerLevel**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.SellerInfo.SellerLevel)  | Y  | -  | Y  | Y  |  
| [Seller.SellerInfo.**StoreOwner**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.SellerInfo.StoreOwner)  | (Y)  | -  | (Y)  | (Y)  |  
| [Seller.SellerInfo.**StoreURL**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.SellerInfo.StoreURL)  | (Y)  | -  | (Y)  | (Y)  |  
| [Seller.SellerInfo.**TopRatedSeller**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.SellerInfo.TopRatedSeller)  | (Y)  | -  | (Y)  | (Y)  |  
| [Seller.**Site**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.Site)  | Y  | -  | Y  | Y  |  
| [Seller.**Status**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.Status)  | Y  | -  | Y  | Y  |  
| [Seller.**UserID**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.UserID)  | Y  | -  | Y  | Y  |  
| [Seller.**UserIDChanged**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.UserIDChanged)  | Y  | -  | Y  | Y  |  
| [Seller.**UserIDLastChanged**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.UserIDLastChanged)  | Y  | -  | Y  | Y  |  
| [Seller.**VATStatus**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.VATStatus)  | Y  | -  | Y  | Y  |  
  

### GranularityLevel
The [GranularityLevel](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Request.GranularityLevel) input field influences which [call-specific fields](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#callOutputFields) may be returned. (All [standard output fields](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#stdOutputFields) are returned regardless of GranularityLevel.)
The **none** column indicates the fields that are returned when you do not specify a GranularityLevel.
Please avoid using a DetailLevel of ReturnAll with GetSellerList when possible. 
Many item details, such as item descriptions and listing enhancements, are unlikely to change. After an initial request for detailed information about items, subsequent requests can omit the DetailLevel field and thus obtain only the information about items that is likely to change. (Alternatively, consider using GetSellerEvents instead of GetSellerList.) If you need to use ReturnAll to retrieve all details for a set of items, please use a smaller EntriesPerPage value to limit the number of items returned per call. Also, use a shorter time range in EndTimeFrom and EndTimeTo for better performance.   
| Y  | The field is always returned.  |  
| --- | --- |  
| (Y)  | The field is conditionally returned. See the field documentation for clarification of conditions.  |  
| -  | The field is not returned.  |  
| Output Field  | Coarse  | Fine  | Medium  |  
| --- | --- | --- | --- |  
| [ItemArray.Item.**ApplicationData**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ApplicationData)  | (Y)  | (Y)  | (Y)  |  
| [ItemArray.Item.**AutoPay**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.AutoPay)  | (Y)  | (Y)  | (Y)  |  
| [ItemArray.Item.**BuyerGuaranteePrice**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.BuyerGuaranteePrice)  | (Y)  | (Y)  | (Y)  |  
| [ItemArray.Item.**BuyerProtection**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.BuyerProtection)  | (Y)  | (Y)  | (Y)  |  
| [ItemArray.Item.**BuyItNowPrice**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.BuyItNowPrice)  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.**Charity**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Charity)  | (Y)  | (Y)  | (Y)  |  
| [ItemArray.Item.**ConditionDescription**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ConditionDescription)  | (Y)  | (Y)  | (Y)  |  
| [ItemArray.Item.**Country**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Country)  | (Y)  | -  | -  |  
| [ItemArray.Item.**CrossBorderTrade**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.CrossBorderTrade)  | (Y)  | (Y)  | (Y)  |  
| [ItemArray.Item.**Currency**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Currency)  | (Y)  | (Y)  | (Y)  |  
| [ItemArray.Item.**HitCount**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.HitCount)  | -  | (Y)  | -  |  
| [ItemArray.Item.**IntegratedMerchantCreditCardEnabled**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.IntegratedMerchantCreditCardEnabled)  | -  | (Y)  | -  |  
| [ItemArray.Item.**ItemID**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ItemID)  | (Y)  | (Y)  | (Y)  |  
| [ItemArray.Item.ItemPolicyViolation.**PolicyID**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ItemPolicyViolation.PolicyID)  | -  | (Y)  | -  |  
| [ItemArray.Item.ItemPolicyViolation.**PolicyText**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ItemPolicyViolation.PolicyText)  | -  | (Y)  | -  |  
| [ItemArray.Item.**ListingDetails**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ListingDetails)  | (Y)  | (Y)  | (Y)  |  
| [ItemArray.Item.ListingDetails.**Adult**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ListingDetails.Adult)  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.ListingDetails.**BindingAuction**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ListingDetails.BindingAuction)  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.ListingDetails.**CheckoutEnabled**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ListingDetails.CheckoutEnabled)  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.ListingDetails.**ConvertedBuyItNowPrice**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ListingDetails.ConvertedBuyItNowPrice)  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.ListingDetails.**ConvertedReservePrice**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ListingDetails.ConvertedReservePrice)  | -  | (Y)  | -  |  
| [ItemArray.Item.ListingDetails.**ConvertedStartPrice**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ListingDetails.ConvertedStartPrice)  | -  | (Y)  | -  |  
| [ItemArray.Item.ListingDetails.**HasReservePrice**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ListingDetails.HasReservePrice)  | -  | (Y)  | (Y)  |  
| [ItemArray.Item.**Location**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Location)  | (Y)  | (Y)  | (Y)  |  
| [ItemArray.Item.**PaymentMethods**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.PaymentMethods)  | -  | (Y)  | -  |  
| [ItemArray.Item.**PrimaryCategory**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.PrimaryCategory)  | (Y)  | (Y)  | (Y)  |  
| [ItemArray.Item.**ProxyItem**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ProxyItem)  | (Y)  | (Y)  | (Y)  |  
| [ItemArray.Item.**Quantity**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Quantity)  | (Y)  | (Y)  | (Y)  |  
| [ItemArray.Item.**QuantityAvailableHint**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.QuantityAvailableHint)  | (Y)  | (Y)  | (Y)  |  
| [ItemArray.Item.**QuantityThreshold**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.QuantityThreshold)  | (Y)  | (Y)  | (Y)  |  
| [ItemArray.Item.**ReservePrice**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ReservePrice)  | -  | (Y)  | -  |  
| [ItemArray.Item.**ReturnPolicy**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ReturnPolicy)  | (Y)  | (Y)  | (Y)  |  
| [ItemArray.Item.ReturnPolicy.**Description**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ReturnPolicy.Description)  | (Y)  | (Y)  | (Y)  |  
| [ItemArray.Item.ReturnPolicy.**InternationalRefundOption**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ReturnPolicy.InternationalRefundOption)  | (Y)  | (Y)  | (Y)  |  
| [ItemArray.Item.ReturnPolicy.**InternationalReturnsAcceptedOption**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ReturnPolicy.InternationalReturnsAcceptedOption)  | (Y)  | (Y)  | (Y)  |  
| [ItemArray.Item.ReturnPolicy.**InternationalReturnsWithinOption**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ReturnPolicy.InternationalReturnsWithinOption)  | (Y)  | (Y)  | (Y)  |  
| [ItemArray.Item.ReturnPolicy.**InternationalShippingCostPaidByOption**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ReturnPolicy.InternationalShippingCostPaidByOption)  | (Y)  | (Y)  | (Y)  |  
| [ItemArray.Item.ReturnPolicy.**Refund**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ReturnPolicy.Refund)  | (Y)  | (Y)  | (Y)  |  
| [ItemArray.Item.ReturnPolicy.**RefundOption**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ReturnPolicy.RefundOption)  | (Y)  | (Y)  | (Y)  |  
| [ItemArray.Item.ReturnPolicy.**ReturnsAccepted**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ReturnPolicy.ReturnsAccepted)  | (Y)  | (Y)  | (Y)  |  
| [ItemArray.Item.ReturnPolicy.**ReturnsAcceptedOption**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ReturnPolicy.ReturnsAcceptedOption)  | (Y)  | (Y)  | (Y)  |  
| [ItemArray.Item.ReturnPolicy.**ReturnsWithin**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ReturnPolicy.ReturnsWithin)  | (Y)  | (Y)  | (Y)  |  
| [ItemArray.Item.ReturnPolicy.**ReturnsWithinOption**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ReturnPolicy.ReturnsWithinOption)  | (Y)  | (Y)  | (Y)  |  
| [ItemArray.Item.ReturnPolicy.**ShippingCostPaidBy**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ReturnPolicy.ShippingCostPaidBy)  | (Y)  | (Y)  | (Y)  |  
| [ItemArray.Item.ReturnPolicy.**ShippingCostPaidByOption**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ReturnPolicy.ShippingCostPaidByOption)  | (Y)  | (Y)  | (Y)  |  
| [ItemArray.Item.**ReviseStatus**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ReviseStatus)  | (Y)  | (Y)  | (Y)  |  
| [ItemArray.Item.**SellingStatus**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus)  | -  | (Y)  | -  |  
| [ItemArray.Item.SellingStatus.**BidCount**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.BidCount)  | -  | (Y)  | -  |  
| [ItemArray.Item.SellingStatus.**BidIncrement**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.BidIncrement)  | -  | (Y)  | -  |  
| [ItemArray.Item.SellingStatus.**ConvertedCurrentPrice**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.ConvertedCurrentPrice)  | -  | (Y)  | -  |  
| [ItemArray.Item.SellingStatus.**CurrentPrice**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.CurrentPrice)  | -  | (Y)  | -  |  
| [ItemArray.Item.SellingStatus.**HighBidder**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.HighBidder)  | -  | (Y)  | -  |  
| [ItemArray.Item.SellingStatus.HighBidder.**AboutMePage**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.HighBidder.AboutMePage)  | -  | (Y)  | -  |  
| [ItemArray.Item.SellingStatus.HighBidder.**BuyerInfo**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.HighBidder.BuyerInfo)  | -  | (Y)  | -  |  
| [ItemArray.Item.SellingStatus.HighBidder.BuyerInfo.**ShippingAddress**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.HighBidder.BuyerInfo.ShippingAddress)  | -  | (Y)  | -  |  
| [ItemArray.Item.SellingStatus.HighBidder.BuyerInfo.ShippingAddress  
.**Country**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.HighBidder.BuyerInfo.ShippingAddress.Country)  | -  | (Y)  | -  |  
| [ItemArray.Item.SellingStatus.HighBidder.BuyerInfo.ShippingAddress  
.**PostalCode**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.HighBidder.BuyerInfo.ShippingAddress.PostalCode)  | -  | (Y)  | -  |  
| [ItemArray.Item.SellingStatus.HighBidder.**eBayGoodStanding**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.HighBidder.eBayGoodStanding)  | -  | (Y)  | -  |  
| [ItemArray.Item.SellingStatus.HighBidder.**EIASToken**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.HighBidder.EIASToken)  | -  | (Y)  | -  |  
| [ItemArray.Item.SellingStatus.HighBidder.**FeedbackPrivate**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.HighBidder.FeedbackPrivate)  | -  | (Y)  | -  |  
| [ItemArray.Item.SellingStatus.HighBidder.**FeedbackRatingStar**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.HighBidder.FeedbackRatingStar)  | -  | (Y)  | -  |  
| [ItemArray.Item.SellingStatus.HighBidder.**FeedbackScore**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.HighBidder.FeedbackScore)  | -  | (Y)  | -  |  
| [ItemArray.Item.SellingStatus.HighBidder.**IDVerified**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.HighBidder.IDVerified)  | -  | (Y)  | -  |  
| [ItemArray.Item.SellingStatus.HighBidder.**NewUser**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.HighBidder.NewUser)  | -  | (Y)  | -  |  
| [ItemArray.Item.SellingStatus.HighBidder.**RegistrationDate**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.HighBidder.RegistrationDate)  | -  | (Y)  | -  |  
| [ItemArray.Item.SellingStatus.HighBidder.**Site**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.HighBidder.Site)  | -  | (Y)  | -  |  
| [ItemArray.Item.SellingStatus.HighBidder.**Status**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.HighBidder.Status)  | -  | (Y)  | -  |  
| [ItemArray.Item.SellingStatus.HighBidder.**UserAnonymized**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.HighBidder.UserAnonymized)  | -  | Y  | -  |  
| [ItemArray.Item.SellingStatus.HighBidder.**UserID**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.HighBidder.UserID)  | -  | (Y)  | -  |  
| [ItemArray.Item.SellingStatus.HighBidder.**UserIDChanged**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.HighBidder.UserIDChanged)  | -  | (Y)  | -  |  
| [ItemArray.Item.SellingStatus.HighBidder.**UserIDLastChanged**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.HighBidder.UserIDLastChanged)  | -  | (Y)  | -  |  
| [ItemArray.Item.SellingStatus.HighBidder.**VATStatus**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.HighBidder.VATStatus)  | -  | (Y)  | -  |  
| [ItemArray.Item.SellingStatus.**ListingStatus**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.ListingStatus)  | -  | (Y)  | -  |  
| [ItemArray.Item.SellingStatus.**MinimumToBid**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.MinimumToBid)  | -  | (Y)  | -  |  
| [ItemArray.Item.SellingStatus.**QuantitySold**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.QuantitySold)  | -  | (Y)  | -  |  
| [ItemArray.Item.SellingStatus.**ReserveMet**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.ReserveMet)  | -  | (Y)  | -  |  
| [ItemArray.Item.SellingStatus.**SecondChanceEligible**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.SecondChanceEligible)  | -  | (Y)  | -  |  
| [ItemArray.Item.**ShippingDetails**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails)  | (Y)  | (Y)  | (Y)  |  
| [ItemArray.Item.ShippingDetails.**SalesTax**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.SalesTax)  | -  | (Y)  | -  |  
| [ItemArray.Item.ShippingDetails.SalesTax.**SalesTaxPercent**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.SalesTax.SalesTaxPercent)  | -  | (Y)  | -  |  
| [ItemArray.Item.ShippingDetails.SalesTax.**ShippingIncludedInTax**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.SalesTax.ShippingIncludedInTax)  | -  | (Y)  | -  |  
| [ItemArray.Item.ShippingDetails  
.**SellerExcludeShipToLocationsPreference**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.SellerExcludeShipToLocationsPreference)  | -  | (Y)  | -  |  
| [ItemArray.Item.ShippingDetails.**TaxTable**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.TaxTable)  | (Y)  | (Y)  | (Y)  |  
| [ItemArray.Item.ShippingDetails.**ThirdPartyCheckout**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShippingDetails.ThirdPartyCheckout)  | -  | (Y)  | -  |  
| [ItemArray.Item.**ShipToLocations**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.ShipToLocations)  | (Y)  | (Y)  | (Y)  |  
| [ItemArray.Item.**Site**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Site)  | (Y)  | (Y)  | (Y)  |  
| [ItemArray.Item.**StartPrice**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.StartPrice)  | -  | (Y)  | -  |  
| [ItemArray.Item.**Storefront**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Storefront)  | (Y)  | (Y)  | (Y)  |  
| [ItemArray.Item.Storefront.**StoreCategory2ID**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Storefront.StoreCategory2ID)  | (Y)  | (Y)  | (Y)  |  
| [ItemArray.Item.Storefront.**StoreCategoryID**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Storefront.StoreCategoryID)  | (Y)  | (Y)  | (Y)  |  
| [ItemArray.Item.Storefront.**StoreURL**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Storefront.StoreURL)  | (Y)  | (Y)  | (Y)  |  
| [ItemArray.Item.**TimeLeft**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.TimeLeft)  | (Y)  | (Y)  | (Y)  |  
| [ItemArray.Item.**Title**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Title)  | (Y)  | (Y)  | (Y)  |  
| [ItemArray.Item.Variations.Variation.SellingStatus.HighBidder  
.**AboutMePage**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.HighBidder.AboutMePage)  | -  | (Y)  | -  |  
| [ItemArray.Item.Variations.Variation.SellingStatus.HighBidder  
.**BuyerInfo**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.HighBidder.BuyerInfo)  | -  | (Y)  | -  |  
| [ItemArray.Item.Variations.Variation.SellingStatus.HighBidder  
.BuyerInfo.**ShippingAddress**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.HighBidder.BuyerInfo.ShippingAddress)  | -  | (Y)  | -  |  
| [ItemArray.Item.Variations.Variation.SellingStatus.HighBidder  
.BuyerInfo.ShippingAddress.**Country**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.HighBidder.BuyerInfo.ShippingAddress.Country)  | -  | (Y)  | -  |  
| [ItemArray.Item.Variations.Variation.SellingStatus.HighBidder  
.BuyerInfo.ShippingAddress.**PostalCode**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.HighBidder.BuyerInfo.ShippingAddress.PostalCode)  | -  | (Y)  | -  |  
| [ItemArray.Item.Variations.Variation.SellingStatus.HighBidder  
.**eBayGoodStanding**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.HighBidder.eBayGoodStanding)  | -  | (Y)  | -  |  
| [ItemArray.Item.Variations.Variation.SellingStatus.HighBidder  
.**EIASToken**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.HighBidder.EIASToken)  | -  | (Y)  | -  |  
| [ItemArray.Item.Variations.Variation.SellingStatus.HighBidder  
.**FeedbackPrivate**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.HighBidder.FeedbackPrivate)  | -  | (Y)  | -  |  
| [ItemArray.Item.Variations.Variation.SellingStatus.HighBidder  
.**FeedbackRatingStar**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.HighBidder.FeedbackRatingStar)  | -  | (Y)  | -  |  
| [ItemArray.Item.Variations.Variation.SellingStatus.HighBidder  
.**FeedbackScore**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.HighBidder.FeedbackScore)  | -  | (Y)  | -  |  
| [ItemArray.Item.Variations.Variation.SellingStatus.HighBidder  
.**IDVerified**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.HighBidder.IDVerified)  | -  | (Y)  | -  |  
| [ItemArray.Item.Variations.Variation.SellingStatus.HighBidder  
.**NewUser**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.HighBidder.NewUser)  | -  | (Y)  | -  |  
| [ItemArray.Item.Variations.Variation.SellingStatus.HighBidder  
.**RegistrationDate**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.HighBidder.RegistrationDate)  | -  | (Y)  | -  |  
| [ItemArray.Item.Variations.Variation.SellingStatus.HighBidder.**Site**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.HighBidder.Site)  | -  | (Y)  | -  |  
| [ItemArray.Item.Variations.Variation.SellingStatus.HighBidder  
.**Status**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.HighBidder.Status)  | -  | (Y)  | -  |  
| [ItemArray.Item.Variations.Variation.SellingStatus.HighBidder  
.**UserAnonymized**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.HighBidder.UserAnonymized)  | -  | Y  | -  |  
| [ItemArray.Item.Variations.Variation.SellingStatus.HighBidder  
.**UserID**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.HighBidder.UserID)  | -  | (Y)  | -  |  
| [ItemArray.Item.Variations.Variation.SellingStatus.HighBidder  
.**UserIDChanged**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.HighBidder.UserIDChanged)  | -  | (Y)  | -  |  
| [ItemArray.Item.Variations.Variation.SellingStatus.HighBidder  
.**UserIDLastChanged**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.HighBidder.UserIDLastChanged)  | -  | (Y)  | -  |  
| [ItemArray.Item.Variations.Variation.SellingStatus.HighBidder  
.**VATStatus**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.HighBidder.VATStatus)  | -  | (Y)  | -  |  
| [ItemArray.Item.Variations.Variation.SellingStatus.**QuantitySold**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.QuantitySold)  | -  | (Y)  | -  |  
| [**Seller**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller)  | -  | (Y)  | -  |  
| [Seller.**AboutMePage**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.AboutMePage)  | -  | Y  | -  |  
| [Seller.**eBayGoodStanding**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.eBayGoodStanding)  | -  | Y  | -  |  
| [Seller.**FeedbackPrivate**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.FeedbackPrivate)  | -  | Y  | -  |  
| [Seller.**FeedbackRatingStar**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.FeedbackRatingStar)  | -  | Y  | -  |  
| [Seller.**FeedbackScore**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.FeedbackScore)  | -  | Y  | -  |  
| [Seller.**IDVerified**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.IDVerified)  | -  | Y  | -  |  
| [Seller.**NewUser**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.NewUser)  | -  | Y  | -  |  
| [Seller.**RegistrationDate**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.RegistrationDate)  | -  | Y  | -  |  
| [Seller.**SellerInfo**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.SellerInfo)  | Y  | Y  | Y  |  
| [Seller.SellerInfo.**AllowPaymentEdit**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.SellerInfo.AllowPaymentEdit)  | -  | Y  | -  |  
| [Seller.SellerInfo.**CheckoutEnabled**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.SellerInfo.CheckoutEnabled)  | -  | Y  | -  |  
| [Seller.SellerInfo.**CIPBankAccountStored**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.SellerInfo.CIPBankAccountStored)  | -  | Y  | -  |  
| [Seller.SellerInfo.**GoodStanding**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.SellerInfo.GoodStanding)  | -  | Y  | -  |  
| [Seller.SellerInfo.**QualifiesForB2BVAT**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.SellerInfo.QualifiesForB2BVAT)  | -  | Y  | -  |  
| [Seller.SellerInfo.**SafePaymentExempt**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.SellerInfo.SafePaymentExempt)  | -  | Y  | -  |  
| [Seller.SellerInfo.**SellerLevel**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.SellerInfo.SellerLevel)  | -  | Y  | -  |  
| [Seller.SellerInfo.**StoreOwner**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.SellerInfo.StoreOwner)  | -  | (Y)  | -  |  
| [Seller.SellerInfo.**StoreURL**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.SellerInfo.StoreURL)  | -  | (Y)  | -  |  
| [Seller.SellerInfo.**TopRatedSeller**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.SellerInfo.TopRatedSeller)  | -  | (Y)  | -  |  
| [Seller.**Site**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.Site)  | -  | Y  | -  |  
| [Seller.**Status**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.Status)  | -  | Y  | -  |  
| [Seller.**UserAnonymized**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.UserAnonymized)  | -  | Y  | -  |  
| [Seller.**UserID**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.UserID)  | -  | Y  | -  |  
| [Seller.**UserIDChanged**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.UserIDChanged)  | -  | Y  | -  |  
| [Seller.**UserIDLastChanged**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.UserIDLastChanged)  | -  | Y  | -  |  
| [Seller.**VATStatus**](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Response.Seller.VATStatus)  | -  | Y  | -  |  
  
  
  
|  [Input](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Input "Details about every field that can be used in this call") [Output](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Output "Details about every field that might be returned by this call") [Detail Controls](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#detailControls "Details about input fields which can restrict the amount of information returned by this call") Samples [Change History](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#ChangeHistory "Details about changes to this call")  |  
| --- |  
## Samples
New to making API calls? Please see [Making a Call](https://developer.ebay.com/api-docs/user-guides/static/make-a-call-landing.html).
Note: Some item IDs, user IDs, or other data in these samples might no longer be active on eBay. If necessary, you can substitute current eBay data in your requests.
Sample: Basic Call
Returns a group of listings that either started or ended during a specified time period.
**Description**
A seller wants a list of all items that she listed on eBay during a particular two-week period.
**Input**
Since the call does not specify a **UserID** , **GetSellerList** lists the items for the user making the call. Use **StartTimeFrom** and **StartTimeTo** to define the two week period. The seller also chooses to limit the number of listings retrieved per page to two.

```
**XML format**.

<?xml version="1.0" encoding="utf-8"?>
<GetSellerListRequest xmlns="urn:ebay:apis:eBLBaseComponents">
  <RequesterCredentials>
    <eBayAuthToken>A*******3</eBayAuthToken>
  </RequesterCredentials>
  <ErrorLanguage>en_US</ErrorLanguage>
  <WarningLevel>High</WarningLevel>
  <GranularityLevel>Coarse</GranularityLevel> 
  <StartTimeFrom>2019-10-12T21:59:59.005Z</StartTimeFrom> 
  <StartTimeTo>2019-10-26T21:59:59.005Z</StartTimeTo> 
  <IncludeWatchCount>true</IncludeWatchCount> 
  <Pagination> 
    <EntriesPerPage>2</EntriesPerPage> 
  </Pagination> 
</GetSellerListRequest>

```

**Output**

```
**XML format**.
<?xml version="1.0" encoding="UTF-8"?>
<GetSellerListResponse 
  xmlns="urn:ebay:apis:eBLBaseComponents">
  <Timestamp>2019-11-05T18:28:30.517Z</Timestamp>
  <Ack>Success</Ack>
  <Version>1131</Version>
  <Build>E1131_CORE_APISELLING_19099826_R1</Build>
  <PaginationResult>
    <TotalNumberOfPages>5</TotalNumberOfPages>
    <TotalNumberOfEntries>9</TotalNumberOfEntries>
  </PaginationResult>
  <HasMoreItems>true</HasMoreItems>
  <ItemArray>
    <Item>
      <AutoPay>false</AutoPay>
      <BuyerProtection>ItemIneligible</BuyerProtection>
      <Country>US</Country>
      <Currency>USD</Currency>
      <HitCounter>NoHitCounter</HitCounter>
      <ItemID>1**********7</ItemID>
      <ListingDetails>
        <RelistedItemID>1**********0</RelistedItemID>
        <StartTime>2019-10-13T00:31:36.000Z</StartTime>
        <EndTime>2019-10-20T00:31:36.000Z</EndTime>
        <ViewItemURL>https://www.ebay.com/itm/Brinns-American-Tradition-First-Lady-Gown-Series-Louisa-Johnson-Adams-/1**********7</ViewItemURL>
        <HasUnansweredQuestions>false</HasUnansweredQuestions>
        <HasPublicMessages>false</HasPublicMessages>
        <ViewItemURLForNaturalSearch>https://www.ebay.com/itm/Brinns-American-Tradition-First-Lady-Gown-Series-Louisa-Johnson-Adams-/1**********7</ViewItemURLForNaturalSearch>
      </ListingDetails>
      <ListingDuration>Days_7</ListingDuration>
      <Location>T***y, California</Location>
      <PrimaryCategory>
        <CategoryID>36549</CategoryID>
        <CategoryName>Dolls & Bears:Dolls:By Brand, Company, Character:Other Brand & Character Dolls</CategoryName>
      </PrimaryCategory>
      <Quantity>1</Quantity>
      <ReviseStatus>
        <ItemRevised>false</ItemRevised>
      </ReviseStatus>
      <SellingStatus>
        <BidCount>0</BidCount>
        <BidIncrement currencyID="USD">0.5</BidIncrement>
        <ConvertedCurrentPrice currencyID="USD">8.75</ConvertedCurrentPrice>
        <CurrentPrice currencyID="USD">8.75</CurrentPrice>
        <MinimumToBid currencyID="USD">8.75</MinimumToBid>
        <QuantitySold>0</QuantitySold>
        <SecondChanceEligible>false</SecondChanceEligible>
        <ListingStatus>Completed</ListingStatus>
      </SellingStatus>
      <ShippingDetails>
        <ShippingDiscountProfileID>0</ShippingDiscountProfileID>
        <InternationalShippingDiscountProfileID>*</InternationalShippingDiscountProfileID>
      </ShippingDetails>
      <ShipToLocations>Worldwide</ShipToLocations>
      <Site>US</Site>
      <Storefront>
        <StoreCategoryID>1</StoreCategoryID>
        <StoreCategory2ID>0</StoreCategory2ID>
        <StoreURL>https://stores.ebay.com/a***s</StoreURL>
      </Storefront>
      <TimeLeft>PT0S</TimeLeft>
      <Title>Brinn's American Tradition First Lady Gown Series Louisa Johnson Adams</Title>
      <WatchCount>0</WatchCount>
      <BestOfferDetails>
        <BestOfferCount>0</BestOfferCount>
        <BestOfferEnabled>true</BestOfferEnabled>
        <NewBestOffer>false</NewBestOffer>
      </BestOfferDetails>
      <LocationDefaulted>true</LocationDefaulted>
      <BuyerResponsibleForShipping>false</BuyerResponsibleForShipping>
      <PostalCode>9***1</PostalCode>
      <PictureDetails>
        <GalleryURL>https://i*********.com/*********/***0.jpg</GalleryURL>
        <PhotoDisplay>PicturePack</PhotoDisplay>
        <PictureURL>hhttps://i*********.com/*********/***0.jpg</PictureURL>
        <PictureURL>https://i*********.com/*********/***1.jpg</PictureURL>
        <PictureURL>https://i*********.com/*********/***2.jpg</PictureURL>
        <PictureURL>https://i*********.com/*********/***3.jpg</PictureURL>
      </PictureDetails>
      <ProxyItem>false</ProxyItem>
      <BuyerGuaranteePrice currencyID="USD">20000.0</BuyerGuaranteePrice>
      <BuyerRequirementDetails>
        <ShipToRegistrationCountry>true</ShipToRegistrationCountry>
      </BuyerRequirementDetails>
      <ReturnPolicy>
        <RefundOption>MoneyBackOrReplacement</RefundOption>
        <Refund>Money back or replacement (buyer's choice)</Refund>
        <ReturnsWithinOption>Days_60</ReturnsWithinOption>
        <ReturnsWithin>60 Days</ReturnsWithin>
        <ReturnsAcceptedOption>ReturnsAccepted</ReturnsAcceptedOption>
        <ReturnsAccepted>Returns Accepted</ReturnsAccepted>
        <ShippingCostPaidByOption>Buyer</ShippingCostPaidByOption>
        <ShippingCostPaidBy>Buyer</ShippingCostPaidBy>
      </ReturnPolicy>
      <ConditionID>1000</ConditionID>
      <ConditionDisplayName>New</ConditionDisplayName>
      <PostCheckoutExperienceEnabled>false</PostCheckoutExperienceEnabled>
      <SellerProfiles>
        <SellerShippingProfile>
          <ShippingProfileID>1**********0</ShippingProfileID>
          <ShippingProfileName>C*********************************************0</ShippingProfileName>
        </SellerShippingProfile>
        <SellerReturnProfile>
          <ReturnProfileID>1**********0</ReturnProfileID>
          <ReturnProfileName>R******************************************r</ReturnProfileName>
        </SellerReturnProfile>
        <SellerPaymentProfile>
          <PaymentProfileID>1**********0</PaymentProfileID>
          <PaymentProfileName>P****l</PaymentProfileName>
        </SellerPaymentProfile>
      </SellerProfiles>
      <RelistParentID>1**********4</RelistParentID>
      <HideFromSearch>false</HideFromSearch>
      <eBayPlus>false</eBayPlus>
      <eBayPlusEligible>false</eBayPlusEligible>
      <IsSecureDescription>true</IsSecureDescription>
    </Item>
    <Item>
      <AutoPay>false</AutoPay>
      <BuyerProtection>ItemIneligible</BuyerProtection>
      <Country>US</Country>
      <Currency>USD</Currency>
      <HitCounter>NoHitCounter</HitCounter>
      <ItemID>1**********2</ItemID>
      <ListingDetails>
        <RelistedItemID>1**********9</RelistedItemID>
        <StartTime>2019-10-15T12:20:04.000Z</StartTime>
        <EndTime>2019-10-22T12:20:04.000Z</EndTime>
        <ViewItemURL>https://www.ebay.com/itm/Our-Lady-Lourdes-Plate-1-Bradford-Exchange-Certified-Authentic-Garrido-/1**********2</ViewItemURL>
        <HasUnansweredQuestions>false</HasUnansweredQuestions>
        <HasPublicMessages>false</HasPublicMessages>
        <ViewItemURLForNaturalSearch>https://www.ebay.com/itm/Our-Lady-Lourdes-Plate-1-Bradford-Exchange-Certified-Authentic-Garrido-/1**********2</ViewItemURLForNaturalSearch>
      </ListingDetails>
      <ListingDuration>Days_7</ListingDuration>
      <Location>T***y, California</Location>
      <PrimaryCategory>
        <CategoryID>11135</CategoryID>
        <CategoryName>Collectibles:Decorative Collectibles:Decorative Collectible Brands:Roman:Other Roman</CategoryName>
      </PrimaryCategory>
      <Quantity>1</Quantity>
      <ReviseStatus>
        <ItemRevised>false</ItemRevised>
      </ReviseStatus>
      <SellingStatus>
        <BidCount>0</BidCount>
        <BidIncrement currencyID="USD">0.5</BidIncrement>
        <ConvertedCurrentPrice currencyID="USD">10.1</ConvertedCurrentPrice>
        <CurrentPrice currencyID="USD">10.1</CurrentPrice>
        <MinimumToBid currencyID="USD">10.1</MinimumToBid>
        <QuantitySold>0</QuantitySold>
        <SecondChanceEligible>false</SecondChanceEligible>
        <ListingStatus>Completed</ListingStatus>
      </SellingStatus>
      <ShippingDetails>
        <ShippingDiscountProfileID>0</ShippingDiscountProfileID>
        <InternationalShippingDiscountProfileID>*</InternationalShippingDiscountProfileID>
      </ShippingDetails>
      <ShipToLocations>US</ShipToLocations>
      <Site>US</Site>
      <Storefront>
        <StoreCategoryID>1</StoreCategoryID>
        <StoreCategory2ID>0</StoreCategory2ID>
        <StoreURL>https://stores.ebay.com/a***s</StoreURL>
      </Storefront>
      <TimeLeft>PT0S</TimeLeft>
      <Title>Our Lady of Lourdes Plate #1 - Bradford Exchange Certified Authentic- Garrido</Title>
      <WatchCount>0</WatchCount>
      <BestOfferDetails>
        <BestOfferCount>0</BestOfferCount>
        <BestOfferEnabled>true</BestOfferEnabled>
        <NewBestOffer>false</NewBestOffer>
      </BestOfferDetails>
      <LocationDefaulted>true</LocationDefaulted>
      <BuyerResponsibleForShipping>false</BuyerResponsibleForShipping>
      <PostalCode>9***1</PostalCode>
      <PictureDetails>
        <GalleryURL>https://i*********.com/*********/$**7.JPG?set_id=8*******0F</GalleryURL>
        <PhotoDisplay>PicturePack</PhotoDisplay>
        <PictureURL>https://i*********.com/*********/***0.jpg</PictureURL>
        <PictureURL>https://i*********.com/*********/***1.jpg</PictureURL>
        <PictureURL>https://i*********.com/*********/***2.jpg</PictureURL>
        <PictureURL>https://i*********.com/*********/***3.jpg</PictureURL>
        <PictureURL>https://i*********.com/*********/***4.jpg</PictureURL>
        <PictureURL>https://i*********.com/*********/***5.jpg</PictureURL>
      </PictureDetails>
      <ProxyItem>false</ProxyItem>
      <BuyerGuaranteePrice currencyID="USD">20000.0</BuyerGuaranteePrice>
      <BuyerRequirementDetails>
        <ShipToRegistrationCountry>true</ShipToRegistrationCountry>
      </BuyerRequirementDetails>
      <ReturnPolicy>
        <RefundOption>MoneyBackOrReplacement</RefundOption>
        <Refund>Money back or replacement (buyer's choice)</Refund>
        <ReturnsWithinOption>Days_14</ReturnsWithinOption>
        <ReturnsWithin>14 Days</ReturnsWithin>
        <ReturnsAcceptedOption>ReturnsAccepted</ReturnsAcceptedOption>
        <ReturnsAccepted>Returns Accepted</ReturnsAccepted>
        <ShippingCostPaidByOption>Buyer</ShippingCostPaidByOption>
        <ShippingCostPaidBy>Buyer</ShippingCostPaidBy>
      </ReturnPolicy>
      <ConditionID>1000</ConditionID>
      <ConditionDisplayName>New</ConditionDisplayName>
      <PostCheckoutExperienceEnabled>false</PostCheckoutExperienceEnabled>
      <SellerProfiles>
        <SellerShippingProfile>
          <ShippingProfileID>1**********0</ShippingProfileID>
          <ShippingProfileName>C*********************************************1</ShippingProfileName>
        </SellerShippingProfile>
        <SellerReturnProfile>
          <ReturnProfileID>1**********0</ReturnProfileID>
          <ReturnProfileName>R********************************************0</ReturnProfileName>
        </SellerReturnProfile>
        <SellerPaymentProfile>
          <PaymentProfileID>1**********0</PaymentProfileID>
          <PaymentProfileName>P****l</PaymentProfileName>
        </SellerPaymentProfile>
      </SellerProfiles>
      <RelistParentID>1**********6</RelistParentID>
      <HideFromSearch>false</HideFromSearch>
      <eBayPlus>false</eBayPlus>
      <eBayPlusEligible>false</eBayPlusEligible>
      <IsSecureDescription>true</IsSecureDescription>
    </Item>
  </ItemArray>
  <ItemsPerPage>2</ItemsPerPage>
  <PageNumber>1</PageNumber>
  <ReturnedItemCountActual>2</ReturnedItemCountActual>
</GetSellerListResponse>

```

  
  
  
|  [Input](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Input "Details about every field that can be used in this call") [Output](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Output "Details about every field that might be returned by this call") [Detail Controls](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#detailControls "Details about input fields which can restrict the amount of information returned by this call") [Samples](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetSellerList.html#Samples "Illustrations of how to use this call") Change History  |  
| --- |  
## Change History  
| Change Date  | Description  |  
| --- | --- |  
|  **1349**  
2024-02-26  | 
  * **CalculatedShippingRate** (modified): The **OriginatingPostalCode** field has been decommissioned and removed from **CalculatedShippingRateType**. Use Item.PostalCode instead.

 |  
|  **1323**  
2023-08-25  | 
  * **SiteCodeType** (modified): `Czechia` and `Cyprus` have been added to **SiteCodeType** as enumeration values. These sites cannot be set in the **X-EBAY-API-SITEID header** , nor in the **Site** field of a request payload.
  * **CalculatedShippingRate** (modified): The **OriginatingPostalCode** field has been deprecated and is not usable. Currently ignored. Use Item.PostalCode instead.

 |  
|  **1257**  
2022-05-06  | 
  * **Item.HitCount** (modified): The logic of HitCount has been modified to show page views for the latest 30-day period, instead of tracking page views for the lifetime of the listing.

 |  
|  **1247**  
2022-02-25  | 
  * **Item.HitCounter** (deprecated): Hit counters are no longer shown in View Item pages, so this field is no longer applicable.

 |  
|  **1193**  
2021-02-12  | 
  * **ShippingServiceCostOverride.ShippingSurcharge** (deprecated): This element has been removed from the WSDL.

 |  
|  **1161**  
2020-07-06  | 
  * **Item.ListingDesigner** (deprecated): This container removed from WSDL, although it is possible that this container may still get returned in a response for an existing listing that was already using a Listing Designer template before this feature was retired.

 |  
|  **1157**  
2020-06-05  | 
  * **Item.ListingDesigner** (deprecated): Sellers are no longer able to use Listing Designer templates when they create or revise listings. Existing listings that are already using a Listing Designer template will remain unchanged.
  * **Item.ReturnPolicy** (doc change): Updated return policy-related documentation to make it more clear that if a seller does not add a separate international return policy for an item, the settings in the domestic return policy will be used instead.

 |  
|  **1145**  
2020-03-13  | 
  * **Charity.CharityID, Charity.CharityNumber** (doc change): Clarified the difference between **CharityID** (eBay identifier) and **CharityNumber** (PayPal Giving Fund identifier), and also added a note about **CharityNumber** field being scheduled for deprecation.

 |  
|  **1119**  
2019-08-02  | 
  * **GalleryTypeCodeType** (modified): The `Featured` value of **GalleryTypeCodeType** is no longer applicable with the scheduled deprecation of the Featured Gallery listing feature. Once the Featured Gallery listing feature is wired off, any existing listings with the **GalleryType** value set to `Featured` will default to a value of `Gallery`
  * **ShippingServiceOptions.ShippingSurcharge** (deprecated): The **ShippingSurcharge** field in **ShippingServiceOptionsType** has been removed from the Trading WSDL. For the next 18 months, this field will still be supported if used in a Add/Revise/Relist call, but it is recommended that sellers configure shipping surcharges in Shipping rate tables instead. Shipping rate tables can be added and modified through the Shipping Preferences in My eBay. Note that this field may still get returned in 'Get' calls if configured through Shipping rate tables.

 |  
|  **1091**  
2019-01-18  | 
  * **ListingDetails.MinimumBestOfferPrice** (modified): Sellers accepting Best Offers for an auction listing can now set the Best Offer Auto Reject threshold price to a dollar value higher than the auction starting price.
  * **Item.MotorsGermanySearchable** (deprecated): This field was deprecated since placing eBay Germany motor vehicle listings on the **mobile.de** site is no longer supported.
  * **Seller.MotorsDealer** (deprecated): This field was deprecated since eBay Motors Pro is a deprecated feature.
  * **Item.ShippingTermsInDescription** (deprecated): This field is no longer applicable, so was deprecated.

 |  
|  **1085**  
2018-10-26  | 
  * **Item.PaymentMethods** (modified): For sellers enrolled in the new eBay Managed Payments program, a specified payment method is not necessary. If a payment method is specified, such as PayPal, it will be dropped from the listing and the seller will get a warning message when the call is run.
  * **Item.AutoPay** (modified): The immediate payment feature is also available for sellers enrolled in the new eBay Managed Payments program. In the past, this feature was only available to sellers who were offering PayPal as the only available payment method.
  * **ShippingDetails.SalesTax** (doc change): Added a note to state that the Sales Tax rate for a US tax jurisdiction that is subject to the 'eBay Collect and Remit Tax' program will be ignored during the checkout process, since eBay will be collecting and remitting this tax to the tax authorities without the seller's involvement.

 |  
|  **1081**  
2018-09-28  | 
  * **Item.ListingDuration** (modified): A 30-day listing duration (`Days_30`) can now be set for eBay Motors listings. The 21-day listing duration (`Days_21`) will soon be wired off for eBay Motors listings.
  * **RateTableDetails.DomesticRateTableId** (modified): Regional shipping rate tables have been enabled for the following sites: Canada (English), Canada (French), and Italy. With regional shipping rate tables, the seller can customize and set the shipping rates based on shipping speed and distance to specified domestic regions. Regional shipping rate tables are required for sellers opted into the eBay Guaranteed Delivery feature and using the 'Door-to-Door' option.

 |  
|  **1073**  
2018-08-03  | 
  * **ReturnPolicy.InternationalReturnsWithinOption, ReturnPolicy.ReturnsWithinOption** (modified): The `Months_1` enumeration value (a valid value for DE and AT sites) is being deprecated, and should no longer be used.

 |  
|  **1061**  
2018-05-11  | 
  * **ReturnPolicy.InternationRefundOption** (added): This release adds the option to specify return policies for international returns (which are items returned using an international shipping service). If you sell internationally, your international return policy is by default inherited from your domestic return policy (in this case **ReturnPolicy.RefundOption**). Set this option so st set up an international return policy if you want to differentiate your international return policy from your domestic return policy. For details, see the [Release Notes](https://developer.ebay.com/Devzone/XML/docs/ReleaseNotes.html#1061).
  * **ReturnPolicy.InternationReturnsAcceptedOption** (added): This release adds the option to specify return policies for international returns.
  * **ReturnPolicy.InternationReturnsWithinOption** (added): This release adds the option to specify return policies for international returns.
  * **ReturnPolicy.InternationShippingCostPaidByOption** (added): This release adds the option to specify return policies for international returns.
  * **ReturnPolicy.ExtendedHolidayReturns** (deprecated): This release deprecates ExtendedHolidayReturns. Values passed to this field are ignored.
  * **ReturnPolicy.RestockingFeeValueOption** (deprecated): This release deprecates RestockingFeeValueOption. As of this release, sellers are no longer allowed to specify a special restocking fee for returned items. Values passed to this field are ignored.
  * **ReturnPolicy.WarrantyDurationOption** (deprecated): This release deprecates WarrantyDurationOption. As of this release, eBay no longer supports item warranties. Values passed to this field are ignored.
  * **ReturnPolicy.WarrantyOfferedOption** (deprecated): This release deprecates WarrantyOfferedOption. As of this release, eBay no longer supports item warranties. Values passed to this field are ignored.
  * **ReturnPolicy.WarrantyTypeOption** (deprecated): This release deprecates WarrantyTypeOption. As of this release, eBay no longer supports item warranties. Values passed to this field are ignored.
  * **ReturnPolicy.Description** (modified): This field is now valid for only the following marketplaces: `EBAY_DE` `EBAY_ES` `EBAY_FR` `EBAY_IT`. Values passed to this field in other marketplaces are ignored.
  * **ReturnPolicy.RefundOption** (modified): This field is now valid only on the US marketplace.
  * **ReturnPolicy.ReturnsWithin** (modified): The `Days_14` option is being deprecated in many eBay categories. You might receive an error if you attempt to list an item with a 14-day return period. For details, see the [Release Notes](https://developer.ebay.com/Devzone/XML/docs/ReleaseNotes.html#1061).

 |  
|  **1039**  
2017-10-17  | 
  * **Item.IsSecureDescription** (added): This boolean field indicates whether or not the listing description is HTTPS secure/compliant. To be HTTPS secure/compliant, the listing description field may not contain any links to site pages that use the HTTP (and not HTTPS) protocol.
  * **ReturnPolicy.RestockingFeeValueOption** (modified): The Percent_20 value indicates that the seller reserves the right to charge a restocking fee percentage for returned items of up to 20 percent (of sale price), but at the seller's discretion, they can also charge less than 20 percent.
  * **ReturnPolicy.RestockingFeeValue** (modified): The 20% value indicates that the seller reserves the right to charge a restocking fee percentage for returned items of up to 20 percent (of sale price), but at the seller's discretion, they can also charge less than 20 percent.
  * **ShippingDetails.RateTableDetails** (modified): Once a seller's account is updated with the new shipping rate tables in My eBay, the seller will be required to use the new DomesticRateTableId and InternationalRateTableId fields, and the DomesticRateTable and InternationalRateTable tags will no longer work. The required IDs for these tables can be retrieved with the getRateTables method of the Account API.

 |  
|  **1029**  
2017-08-18  | 
  * **ListingEnhancementsCodeType** (modified): The following enumeration values are no longer applicable, as the listing enhancements associated with these enumeration values are no longer supported on any eBay Marketplace site: `BasicUpgradePackBundle`, `Border`, `Featured`, `Highlight`, `ProPackBundle`, and `ProPackPlusBundle`.

 |  
|  **1027**  
2017-08-04  | 
  * **ListingTypeCodeType** (modified): The `Half` enumeration value is being deprecated, as API support for Half.com listings is being deprecated.
  * **UserStatusCodeType** (modified): The `CreditCardVerifyHalfOptIn` and `UnconfirmedHalfOptIn` enumeration values are being deprecated, as API support for Half.com listings is being deprecated.

 |  
|  **1019**  
2017-06-09  | 
  * **RateTableDetails.DomesticRateTableId** (added): New field added to support new domestic shipping rate tables. The new shipping rate tables are currently only available on US and Australia sites, but will be coming soon to UK and Germany sites.
  * **RateTableDetails.InternationalRateTableId** (added): New field added to support new international shipping rate tables. The new shipping rate tables are currently only available on US and Australia sites, but will be coming soon to UK and Germany sites.

 |  
|  **0997**  
2017-01-20  | 
  * **CalculatedShippingRate.PackageDepth** (deprecated): This field is being deprecated. It will still be supported for 18 additional months, but for it to be available, the user will have to use Version 995 or older.
  * **CalculatedShippingRate.PackageLength** (deprecated): This field is being deprecated. It will still be supported for 18 additional months, but for it to be available, the user will have to use Version 995 or older.
  * **CalculatedShippingRate.PackageWidth** (deprecated): This field is being deprecated. It will still be supported for 18 additional months, but for it to be available, the user will have to use Version 995 or older.
  * **CalculatedShippingRate.ShippingPackage** (deprecated): This field is being deprecated. It will still be supported for 18 additional months, but for it to be available, the user will have to use Version 995 or older.
  * **CalculatedShippingRate.WeightMajor** (deprecated): This field is being deprecated. It will still be supported for 18 additional months, but for it to be available, the user will have to use Version 995 or older.
  * **CalculatedShippingRate.WeightMinor** (deprecated): This field is being deprecated. It will still be supported for 18 additional months, but for it to be available, the user will have to use Version 995 or older.
  * **Item.ListingCheckoutRedirectPreference** (deprecated): This field is being deprecated. Third-party checkout has been deprecated.
  * **Item.PostCheckoutExperienceEnabled** (deprecated): This field is being deprecated. The Post-Checkout Experience feature has been deprecated.
  * **Item.SkypeContactOption** (deprecated): This field is being deprecated. Member communication through Skype has been deprecated.
  * **Item.SkypeEnabled** (deprecated): This field is being deprecated. Member communication through Skype has been deprecated.
  * **Item.SkypeID** (deprecated): This field is being deprecated. Member communication through Skype has been deprecated.
  * **Item.ThirdPartyCheckoutIntegration** (deprecated): This field is being deprecated. Third-party checkout has been deprecated.
  * **PictureDetails.GalleryURL** (deprecated): This field is being deprecated from public WSDL. It is only used internally.
  * **ReturnPolicy.EAN** (deprecated): This field is being deprecated. The EAN value will no longer be a part of the seller's return policy. If specified for a product, the EAN value can be found in the **ProductListingDetails** or **VariationProductListingDetails** (for prouct variations) containers.
  * **ShippingDetails.InsuranceFee** (deprecated): This field is being deprecated.
  * **ShippingDetails.InsuranceOption** (deprecated): This field is being deprecated.

 |  
|  **0955**  
2016-02-12  | 
  * **BuyerPaymentMethodCodeType** (modified): The Moneybookers, ProPay, and Paymate enumeration values have been deprecated, and will no longer be returned in any calls.

 |  
|  **0945**  
2015-10-15  | 
  * **BuyerPaymentMethodCodeType** (modified): Moneybookers, ProPay, or Paymate will no longer be accepted as valid PaymentMethods for new listings. However, these payment methods will still be allowed for existing listings, so these values may still get returned until these payment methods are completely removed from all listings.

 |  
|  **0933**  
2015-07-24  | 
  * **eBayPlusEligible** (added): This new field returns a boolean value that indicates whether an item is is eligible to be listed under the eBay Plus program. eBay Plus is a premium account option for buyers, which provides benefits such as fast free domestic shipping and free returns on selected items. Currently available only in Germany.
  * **eBayPlus** (added): This new field returns a boolean value that indicates whether the eBay Plus program is being offered on an item listing. eBay Plus is a premium account option for buyers, which provides benefits such as fast free domestic shipping and free returns on selected items. Currently available only in Germany.

 |  
|  **0925**  
2015-05-29  | 
  * **NameValueList.Name** (modified): In a multiple-variation listing, the Brand should be returned at the item level (ItemSpecifics container) and the MPN for the product variation should be returned at the variation level (VariationSpecifics container).
  * **Item.ProductListingDetails** (modified): In a multiple-variation listing, the product identifier (EAN, ISBN or UPC) for a product variation should be returned in the Variation.VariationProductListingDetails container instead.
  * **BrandMPN.Brand** (modified): Decreased maximum length of string value to 65 characters. If Brand and MPN (Manufacturer Part Number) are being used to identify product variations in a multiple-variation listing, the Brand should be returned at the item level (this field and the ItemSpecifics container) and the MPN for each product variation should be returned at the variation level (VariationSpecifics container).
  * **BrandMPN.MPN** (modified): Decreased maximum length of string value to 65 characters. If Brand and MPN (Manufacturer Part Number) are being used to identify product variations in a multiple-variation listing, the Brand should be returned at the item level (this field and the ItemSpecifics container) and the MPN for each product variation should be returned at the variation level (VariationSpecifics container).
  * **ProductListingDetails.EAN** (modified): In a multiple-variation listing, the EAN of a product variation should be returned in the VariationProductListingDetails container instead. If the listing is in a category that expects an EAN value, but one doesn't exist for the product, this field may contain text similar or identical to 'Does not apply'.
  * **ProductListingDetails.ISBN** (modified): In a multiple-variation listing, the ISBN of a product variation should be returned in the VariationProductListingDetails container instead. If the listing is in a category that expects an ISBN value, but one doesn't exist for the product, this field may contain text similar or identical to 'Does not apply'.
  * **ProductListingDetails.UPC** (modified): In a multiple-variation listing, the UPC of a product variation should be returned in the VariationProductListingDetails container instead. If the listing is in a category that expects a UPC value, but one doesn't exist for the product, this field may contain text similar or identical to 'Does not apply'.
  * **VariationProductListingDetails** (added): This container is returned if a product variation within a multiple-variation listing was identified with an EAN, an ISBN, or a UPC value.

 |  
|  **0905**  
2015-01-09  | 
  * **CalculatedShippingRateType** (modified): Data fields in this container used to specify shipping package weight and dimensions should no longer be used. Instead, the equivalents fields in ShippingPackageDetailsType should be used.

 |  
|  **0899**  
2014-11-04  | 
  * **BuyerPaymentMethodCodeType** (modified): 'QIWI' added as enumeration value. This payment method can only be specified on the US site and is only applicable to Russian buyers.

 |  
|  **0897**  
2014-10-21  | 
  * **SiteCodeType** (modified): 'Russia' added as enumeration value to support selling on the new Russia site.

 |  
|  **0879**  
2014-06-17  | 
  * **PickupInStoreDetails.EligibleForPickupDropOff** (added): This boolean field is returned as 'true' if the listing is enabled for the "Click and Collect" feature.

 |  
|  **0861**  
2014-02-11  | 
  * **StorefrontType.StoreCategoryName** (added): This field is used by eBay Stores sellers to list an item under one of their custom categories using the category name.
  * **StorefrontType.StoreCategory2Name** (added): This field is used by eBay Stores sellers to list an item under a second category using one of their custom categories names.

 |  
|  **0859**  
2014-01-28  | 
  * **Item.OutOfStockControl** (modified): OutOfStockControl can now be used with BestOffer.

 |  
|  **0851**  
2013-11-19  | 
  * **Item.ConditionDescription** (modified): ConditionDescription is now supported on the following eBay sites: US and US Motors (0, 100), CA (2), CAFR (210), UK (3), AU (15), AT (16), BEFR (23), BENL (123) FR (71), DE (77), IT (101), NL (146), ES (186), CH (193), IE (205), PL (212).

 |  
|  **0849**  
2013-11-05  | 
  * **Item.ConditionDescription** (modified): In addition to the eBay US and US eBay Motors (0), UK (3), CA (2), CAFR (210) and AU (15) sites, ConditionDescription is now supported on the AT (16), FR (71), IT (101) and ES (186) sites.
  * **Item.PaymentMethods** (modified): 'CreditCard' and 'DirectDebit' added as acceptable buyer payment methods. These two values will only be returned for eBay Now-enabled listings.
  * **ShippingServiceOptions.ShippingService** (modified): 'eBayNowImmediateDelivery' added as an acceptable value in the ShippingService field. This value will only be returned for eBay Now-enabled listings.

 |  
|  **0841**  
2013-09-19  | 
  * **Item.ShippingServiceCostOverrideList** (added): This container is returned for a listing that is using shipping costs overrides to override the flat shipping costs for all domestic and/or all international shipping services defined in the Business Policies shipping profile referenced by the listing.
  * **Item.eBayNowEligible** (added): This boolean field indicates if the listing is enabled for eBay Now delivery. A seller must be eligible for the eBay Now delivery feature to list an item that is eligible for eBay Now delivery.

 |  
|  **0831**  
2013-07-03  | 
  * **Item.PickupInStoreDetails** (added): A new container that is used to enable a multi-quantity, fixed-price listing with the In-Store Pickup option. If an eligible seller/merchant enables the In-Store Pickup option, the buyer of the item will have the option of picking up that item at one of the merchant's retail locations at no charge. Besides including and setting the EligibleForPickupInStore flag to 'true', there are additional requirements that the seller must follow when listing an In-Store Pickup item. These requirements are discussed in the description of the EligibleForPickupInStore field.

 |  
|  **0829**  
2013-06-19  | 
  * **ReturnPolicy.RefundOption** (modified): A new 'MoneyBackOrReplacement' value is now supported. This value should be used by a seller opted in to eBay-managed returns who wants to give buyers the choice of receiving a refund for a returned item, or receiving a replacement item.

 |  
|  **0825**  
2013-05-22  | 
  * **ReturnPolicy.ReturnsWithinOption** (modified): A new 'Months_1' value is now supported. This value indicates a one-month return policy.

 |  
|  **0823**  
2013-05-08  | 
  * **Item.OutOfStockControl** (added): Flag that when set to 'true' hides a listing when the quantity of the item goes to 0 (zero) but keeps the listing alive. While the "quantity available" value is 0, the listing would be hidden from eBay search, and if that item was specifically searched for with **GetItem** (or related call), the 'OutOfStock' Enum would be returned. This is useful for a seller who is waiting for additional stock of an item. Instead of ending the listing and then recreating it when the inventory arrives, they can use this flag to hide the listing. Then when they have the item available they can update the inventory of the item (through the **Item.Quantity** or **Item.Variations.Variation.Quantity** fields in an **AddFixedPriceItem** call) and the listing would appear again.

 |  
|  **0799**  
2012-11-07  | 
  * **ShippingDetailsType.InternationalShippingServiceOption** (doc change): The description clarifies that a seller can offer up to four domestic shipping services and up to five international shipping services. However, if the seller is opted in to the Global Shipping Program, only four other international shipping services may be offered (regardless of whether or not Global Shipping is offered for the listing).

 |  
|  **0793**  
2012-09-26  | 
  * **ShippingDetails.GlobalShipping** (added): If the value of GlobalShipping is true, the Global Shipping Program is the default international shipping option for the listing, and eBay designates an appropriate international shipping service. If the value of GlobalShipping is false, the seller is responsible for specifying an international shipping service for the listing if desired.
  * **BuyerInfo.ShippingAddress** (modified): For a Global Shipping Program order, the Country field and the PostalCode field now return the country code and postal code, respectively, of the buyer, not those of the international shipping provider.

 |  
|  **0791**  
2012-09-12  | 
  * **InternationalShippingServiceOption.ShippingService** (modified): New International shipping services added for UK and DE sites as part of the EU delivery estimate project. For UK, these new enumeration values are UK_ParcelForceIntlExpress, UK_ParcelForceIntlValue, and UK_ParcelForceIntlEconomy. For DE, these new enumeration values are DE_DeutschePostBriefIntlEcon and DE_DeutschePostBriefIntlPriority.

 |  
|  **0789**  
2012-08-29  | 
  * **Item.ConditionDescription** (added): This string field is used by the seller to more clearly describe the condition of items that are not brand new.
  * **Item.ListingSubtype2** (doc change): A note was added to clarify that this value indicates a classified ad (or digital download) listing on ebay.com websites, not on ebayclassifieds.com. The ebayclassifieds.com site is not supported by the Trading API.

 |  
|  **0787**  
2012-08-15  | 
  * **Item.ShippingDetails.RateTableDetails** (doc change): Documentation for this container and its fields has been revised to be more accurate and easier to understand.
  * **Item.ShippingDetails.RateTableDetails.InternationalRateTable** (added): This field specifies which international shipping rate table to apply to a listing. International rate tables can be used only for items listed on the DE or UK site, and the seller must have previously configured a table in My eBay site preferences. Shipping rate tables enable sellers to tailor the flat shipping rates offered for an item to fit the shipping destination. They can specify a base rate for a large region, then define alternative rates or surcharges for shipping to individual countries within the region.

 |  
|  **0783**  
2012-07-18  | 
  * **ReturnPolicy.RestockingFeeValueOption** (added): This enumeration value indicates the restocking fee charged by the seller for returned items. In order to charge the buyer a restocking fee when an item is returned, a US seller must input a restocking fee value as part of the return policy.
  * **ReturnPolicy.RestockingFeeValue** (added): This value is directly related to the RestockingFeeValueOption value, with the difference being that applications can use RestockingFeeValue to present the RestockingFeeValueOption value in a more user-friendly format.

 |  
|  **0781**  
2012-07-04  | 
  * **ShippingServiceCodeType** (modified): AU_StandardDeliveryFromOutsideAU added as a shipping service option. This option can be specified by sellers on the AU site if the item is being shipped from a location outside of Australia using standard delivery.

 |  
|  **0765**  
2012-03-14  | 
  * **Seller.SellerInfo.SellereBayPaymentProcessConsent** (added): This response container is returned to DE/AT sellers ramped up in the new eBay payment process. This container consists of information related to the seller's signing of the supplemental user agreement and payout preferences.
  * **Seller.SellerInfo.SellereBayPaymentProcessStatus** (added): This response field contains an enumeration value that indicates the current status of a DE or AT seller's account related to the new eBay payment process.

 |  
|  **0763**  
2012-02-29  | 
  * **Item.SellerProfiles.SellerPaymentProfile** (added): This container is returned if a Business Policies payment profile was applied to the listing. This feature is currently only available for testing in a Sandbox environment and will not be available in Production until May 2012.
  * **Item.SellerProfiles.SellerReturnProfile** (added): This container is returned if a Business Policies return policy profile was applied to the listing. This feature is currently only available for testing in a Sandbox environment and will not be available in Production until May 2012.
  * **Item.SellerProfiles.SellerShippingProfile** (added): This container is returned if a Business Policies shipping profile was applied to the listing. This feature is currently only available for testing in a Sandbox environment and will not be available in Production until May 2012.
  * **Item.ShippingPackageDetails** (added): If the seller is using calculated shipping, this container is used to specify the weight and dimensions of an item's shipping package. This feature is currently only available for testing in a Sandbox environment and will not be available in Production until May 2012.

 |  
|  **0735**  
2011-08-17  | 
  * **Item.ItemSpecifics** (modified): Ticket listings return custom item specifics instead of ID-based attributes.
  * **Item.ReturnPolicy.RefundOption** (modified): MoneyBackOrExchange value is now supported.

 |  
|  **0719**  
2011-04-27  | 
  * **ShippingServiceCodeType** (modified): 15 new shipping services added for the Australia and Canada sites. The nine new Australia carrier-specific shipping services include AU_AusPostRegisteredPostInternationalPaddedBag1kg, AU_AusPostRegisteredPostInternationalPaddedBag500g, AU_AusPostRegisteredPostInternationalParcel, AU_AustralianAirExpressFlatRate1kg, AU_AustralianAirExpressFlatRate3kg, AU_AustralianAirExpressFlatRate5kg, AU_AustralianAirExpressMetro15kg, AU_eBayAusPost3kgFlatRateSatchel, and AU_eBayAusPost500gFlatRateSatchel. The nine new Australia generic service level shipping services include AU_EconomyDeliveryFromOutsideAU, AU_ExpeditedDeliveryFromOutsideAU, AU_ExpressDelivery, AU_Freight, and AU_StandardDelivery. The new Canada shipping service is CA_Freight.
  * **Item.ShippingDetails.ShippingServiceOptions** (modified): '4' has been added as a valid integer value to account for the additional international shipping service that may be specified by the seller.
  * **Item.ShippingDetails.InternationalShippingServiceOption** (modified): '4' and '5' have been added as valid integer values to account for the additional international shipping services that may be specified by the seller.

 |  
|  **0689**  
2010-09-20  | 
  * **ShippingType.ApplyShippingDiscount** (deprecated): As of version 689, **ApplyShippingDiscount** is deprecated and removed from the schema.

 |  
|  **0679**  
2010-07-21  | 
  * **ItemType.QuantityThreshold, Itemtype.QuantityAvailableHint** (added): Set a quantity threshold for the number of items available. As long as the number of items remains above the threshold, GetSellerList will return a quantity in the form, "More than n available," where n is the quantity threshold.

 |  
|  **0663**  
2010-03-31  | 
  * **ShippingType.ApplyShippingDiscount** (deprecated): This tag is no longer being used. It will be officially deprecated later in 2010.

 |  
|  **0635**  
2009-09-16  | 
  * **ExcludeShipToLocation, SellerExcludeShipToLocationsPreference** (added): Sellers can now exclude specific regions and countries from where they will ship items.
  * **InsuranceDetails, InsuranceFee, InsuranceOption, InternationalInsuranceDetails, InsuranceWanted, ShippingInsuranceCost** (modified): Sellers can no longer give buyers the option to purchase shipping insurance for either domestic or international items. The buyer-paid shipping insurance option has been removed from the following sites:   
` BEFR, BENL, CA, CAFR, HK, IE, IN, MY, Motors, NL, PH, PL, SG, UK, US`   
Insurance tags are returned only when the associated item has buyer-paid shipping insurance values.

 |  
|  **0629**  
2009-08-05  | 
  * **TopRatedSeller** (added): Returned when seller is a Top-Rated Seller.

 |  
|  **0619**  
2009-05-27  | 
  * **IncludeVariations, Variations** (added): Use IncludeVariations to retrieve details about multi-variation listings.

 |  
|  **0605**  
2009-02-18  | 
  * **NowAndNew** (deprecated): Now & New (Sofort & Neu) has been retired as of this release.

 |  
|  **0603**  
2009-02-04  | 
  * **Item.IntegratedMerchantCreditCardEnabled** (added): Indicates that the IntegratedMerchantCreditCard payment method applies to the item.

 |  
|  **0599**  
2009-1-07  | 
  * **NowAndNew** (doc change): eBay will retire Now & New (Sofort & Neu) by March 2009.

 |  
|  **0581**  
2008-09-03  | 
  * **ItemArray.Item.ReturnPolicy** (added): Specifies the seller's return policy.

 |  
|  **0573**  
2008-07-09  | 
  * **ItemArray.Item.DigitalDeliveryDetails** (deprecated): The digital delivery feature is disabled as of March 28, 2008. GetSellerList no longer returns digital delivery details for digital download items.

 |  
|  **0567**  
2008-05-28  | 
  * **CategoryID** (added): You can specify a category ID for the items retrieved.
  * **EndTimeFrom, EndTimeTo, StartTimeFrom, StartTimeTo** (modified): The maximum time range allowed in a request is 120 days.

 |  
|  **0563**  
2008-04-30  | 
  * **Item.BuyerGuaranteePrice** (added): On the Australia site, by early June 2008, BuyerGuaranteePrice is the PayPal Buyer Protection coverage, offered for the item at the time of purchase. Details of coverage are in the following sections of the View Item page: the Buy Safely section and the Payment Details section.
  * **BuyerProtection.NoCoverage** (added): On the Australia site, by early June 2008, indicates that there is no PayPal Buyer Protection coverage.

 |  
|  **0561**  
2008-04-16  | 
  * **Item.ListingType.Express** (deprecated): Due to the shutdown of UK and Germany eBay Express sites Item.ListingType.Express has been deprecated.

 |  
|  **0559**  
2008-04-02  | 
  * **Item.CrossBorderTrade** (added): For a fee, enables a listing to be displayed in the default search results of another eBay site. Applicable beginning in early May 2008.

 |  
|  **0557**  
2008-03-19  | 
  * **Item.SellingStatus.AdminEnded** (added): If included in the response as true, indicates that the listing was canceled due to a violation of eBay's listing policies and that the item can be relisted using RelistItem.
  * **Item.ItemPolicyViolation.PolicyID** (added): If a violation of an eBay listing policy has occurred, indicates the integer ID of the violated policy in the response. Applies to all eBay sites, including eBay Motors and Express (does not include Half.com).
  * **Item.ItemPolicyViolation.PolicyText** (added): If a violation of an eBay listing policy has occurred, provides a textual description of the violated policy in the response. Applies to all eBay sites, including eBay Motors and Express (does not include Half.com).
  * **AdminEndedItemsOnly** (added): If included in the request as true, the response will return only administratively ended items for any policy violation.

 |  
|  **0555**  
2008-03-05  | 
  * **GetSellerListRequestType.UserIDType** (modified): Note that since user information is anonymous to everyone except the bidder and the seller (during an active auction), only sellers looking for information about their own listings and bidders who know the user IDs of their sellers will be able to make this API call successfully.

 |  
|  **0553**  
2008-02-20  | 
  * **ProductListingDetails.StockPhotoURL** (doc change): The documentation has been corrected to remove this container and element.

 |  
|  **0551**  
2008-02-06  | 
  * **HitCount** (added): The number of hits on an item.

 |  
|  **0537**  
2007-10-31  | 
  * **Item.PaymentMethods.PaisaPayEscrow, Item.PaymentMethods.PaisaPayEscrowEMI** (added): These enum will be returned for items offering PaisaPayEscrow and PaisaPayEscrowEMI payment methods.
  * **BestOfferAutoAcceptPrice** (added): The price at which best offers are automatically accepted.

 |  
|  **0507**  
2007-04-04  | 
  * **PayPerLeadEnabled** (added): Added for the pay-per-lead feature, applicable beginning in upcoming months on the US site.

 |  
|  **0503**  
2007-03-07  | 
  * **SellerType.SafePaymentExcempt** (added): This field indicates whether a seller is exempt from providing a safe payment method. If a seller is exempt, any safe payment restrictions for a site or a category do not apply.

 |  
|  **0499**  
2007-02-07  | 
  * **AnythingPoints, ProximitySearchDetails.PostalCode, SellerKey, ShippingDetails.AllowPaymentEdit, ShippingDetails.SellerPostalCode, SiteHostedPicture, SkypeOption, VendorHostedPicture** (modified): Deleted previously deprecated objects from the latest schema. Some of these objects are still supported with lower request versions. See [Deprecated Objects](https://developer.ebay.com/devzone/xml/docs/reference/ebay/deprObjects.html).
  * **ItemArray.Item.Storefront.StoreCategoryID, ItemArray.Item.Storefront.StoreCategory2ID** (modified): The data types for IDs used for eBay Stores have changed from xs:int to xs:long to prepare for future increases in ID values.
  * **ExtendedSellerContactDetails** (added): Returns seller contact details.

 |  
|  **0497**  
2007-01-24  | 
  * **ItemArray.Item.SellingStatus.PromotionalSaleDetails** (added): If a seller has reduced the price of a listed item with the Promotional Price Display feature, this field contains the original price of the discounted item, along with the start-time and end-time of the discount.

 |  
|  **0491**  
2006-12-13  | 
  * **Item.ListingCheckoutRedirectPreference.ProStoresStoreName** (doc change): Added this existing field to the GetSellerList documentation.
  * **Item.SellingStatus.HighBidder.MotorsDealer** (doc change): Not returned. Removed from output topic.
  * **Item.ShippingDetails** (doc change): InternationalShippingServiceOption.ShippingInsuranceCost and ShippingServiceOptions.ShippingInsuranceCost are not returned. Removed from output topic.
  * **Item.ListingDetails.ViewItemURLForNaturalSearch** (added): A variation of ViewItemURL optimized for popular search engines.
  * **UserType** (modified): Starting Jan 2007, selected tags in the User container will be made anonymous for listings that have a current price of $200.00 USD or higher. See [Working with Anonymous User Information](https://developer.ebay.com/devzone/guides/ebayfeatures/Development/CRM-UserInformation.html#WorkingwithAnonymousUserInformation) for a list of effected fields.

 |  
|  **0489**  
2006-11-29  | 
  * **ItemArray.Item.WatchCount** (doc change): ItemArray.Item.WatchCount added to GetSellerList output fields.

 |  
|  **0483**  
2006-10-18  | 
  * **Item.AnythingPoints** (deprecated): No longer returned as of request version 483.
  * **Item.ProximitySearchDetails** (deprecated): No longer returned as of request version 483. Use Item.PostalCode instead.
  * **Item.ShippingDetails.SellerPostalCode** (deprecated): No longer returned as of request version 483. Use Item.PostalCode instead.

 |  
|  **0477**  
2006-09-06  | 
  * **ListingType** (modified): Chinese auction listings with Buy It Now are eligible for Express US.
  * **ShippingTypes: CalculatedDomesticFlatInternational, FlatDomesticCalculatedInternational** (added): Two more shipping types were introduced to enable a seller to use flat rate shipping for the domestic services and calculated shipping for the international shipping services, or vice versa. See the [Managing Shipping](https://developer.ebay.com/devzone/guides/ebayfeatures/Development/Shipping-Managing.html) documentation for details.
  * **ShippingServiceOptions.ShippingSurcharge** (added): A cost that the seller can add for flat rate shipping for eBay US and Motors Parts and Accessories. See the [Managing Shipping](https://developer.ebay.com/devzone/guides/ebayfeatures/Development/Shipping-Managing.html) documentation for details.
  * **ShippingDetails.InternationalPackagingHandlingCosts** (added): A means of distinguishing international packaging/handling costs from domestic costs. See the [Managing Shipping](https://developer.ebay.com/devzone/guides/ebayfeatures/Development/Shipping-Managing.html) documentation for details.
  * **ShippingDetails.InsuranceDetails** (added): A container of details about insurance for the domestic shipping services. See the [Managing Shipping](https://developer.ebay.com/devzone/guides/ebayfeatures/Development/Shipping-Managing.html) documentation for details.
  * **ShippingDetails.InternationalInsuranceDetails** (added): A container of details about insurance for the international shipping services.

 |  
|  **0471**  
2006-7-26  | 
  * **DetailLevel** (doc change): Clarified best practices. Please avoid using ReturnAll when possible. Use a GranularityLevel or use GetSellerEvents instead. If you use ReturnAll, use a small EntriesPerPage value and short end time range for better performance.

 |  
|  **0469**  
2006-7-12  | 
  * **Seller.SellerInfo.ExpressWallet** (added): Indicates whether the seller has an Express wallet.
  * **ItemArray.Item.SellingStatus.HighBidder.MotorsDealer** (added): Indicates if an item is listed for sale by owner (FSBO) or listed by a dealer. Applies to eBay Motors Pro applications only.
  * **ItemArray.Item.ProxyItem** (added): Affiliate-related field.
  * **MotorsDealerUsers** (added): Specifies the list of Motors Dealer sellers for which a special set of metrics can be requested.
  * **ItemArray.Item.TotalQuestionCount** (added): The number of questions asked about the item.

 |  
|  **0465**  
2006-06-14  | 
  * **ItemArray.Item.ListingCheckoutRedirectPreference** (added): ProStores listing level preferences regarding the store to which checkout should be redirected for the listing if ThirdPartyCheckout is true.
  * **ItemArray.Item.SkypeContactOption** (added): Specifies the Skype contact options supported.

 |  
|  **0463**  
2006-5-31  | 
  * **Sample** (doc change): A DetailLevel of ReturnAll should NOT be used with this call.

 |  
|  **0459**  
2006-05-03  | 
  * **Seller.SellerInfo.ExpressEligible** (added): Indicates whether the seller is eligible to list on Express.
  * **ItemArray.Item.ListingDetails.ExpressListing** (added): Indicates whether the listing is included on Express.
  * **ItemArray.Item.ListingType [Express]** (added): Added a new Express-only format for Express Germany users.

 |  
|  **0455**  
2006-5-5  | 
  * **Item.ThirdPartyCheckoutIntegration** (added): Used by third party checkout providers to opt an item into eBay Express (and thus approve handling of checkout by eBay Express).

 |  
|  **0453**  
2006-3-22  | 
  * **Item.BuyerRequirements and Item.DisableBuyerRequirements** (added): Buyer requirements can now be specified per listing (and not just via My eBay). Buyer requirements can also be updated on active listings, applying only to subsequent bids.

 |  
|  **0439**  
2005-12-14  | 
  * **Item.PictureDetails** (added): SiteHostedPicture and VendorHostedPicture contain data for pictures associated with an item. With compatibility level 439 and higher, that data will be returned in PictureDetails instead, regardless of the input.

 |  
|  **0427**  
2005-09-21  | 
  * **Item.SellingStatus.ListingStatus** (added): Specifies an active or ended listing's status in eBay's processing workflow. For items that have sold, this to determine whether eBay has finished processing total price, winning bidder/buyer, and Final Value Fee details.

 |  
|  **0425**  
2005-9-7  | 
  * **IncludeWatchCount** (added): Input argument that returns the WatchList element in Item objects.

 |  
|  **0419**  
2005-7-27  | 
  * **GranularityLevel** (added): Filter to control the amount of data returned per record (similar to DetailLevel).

 |  
|  **0415**  
2005-5-29  | 
  * **Item.GetItFast** (added): This field supports the new Get It Fast feature.

 |  
|  **0411**  
2005-6-1  | 
  * **BuyerResponsibleForShipping** (added): For eBay Motors vehicle listings, flag that indicates shipping arrangements.
  * **InsuranceOption** (modified): New NotOfferedOnSite value added to ShippingDetails.InsuranceOption.
  * **ShippingPackage** (modified): A new value, ExtraLargePack, has been added.
  * **LimitedWarrantyEligible** (added): For eBay Motors vehicle listings, flag that indicates that the vehicle has not been modified or is not a special type.

 |  
[FAQs](https://developer.ebay.com/support/faq) [Developer Community Forum](https://community.ebay.com/t5/Developer-Groups/ct-p/developergroup) [Developer Technical Support](https://developer.ebay.com/my/support/tickets) [APIs](https://developer.ebay.com/develop/apis) [API License Agreement](https://developer.ebay.com/join/api-license-agreement)
Copyright 1999-2026 eBay Inc. All rights reserved. [User agreement](http://pages.ebay.com/help/policies/user-agreement.html?rt=nc "opens in new window or tab"), [Privacy policy](http://pages.ebay.com/help/policies/privacy-policy.html?rt=nc "opens in new window or tab"), [Cookies](http://pages.ebay.com/help/account/cookies-web-beacons.html "opens in new window or tab"). 

