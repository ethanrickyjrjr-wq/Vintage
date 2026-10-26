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
[Home](https://developer.ebay.com/)[Develop](https://developer.ebay.com/develop)[Data Handling Compliance](https://developer.ebay.com/api-docs/static/data-handling-update.html)
# Data Handling Compliance
We have updated our APIs to address requirements for third-party developers based in certain jurisdictions. Among those impacted are API users in China (and its territories), Russia, North Korea, Cuba, Iran, and Venezuela. 
**Note:** When retrieving username and financial information for U.S users, only a certain amount of unique user data can be retrieved over a given time period. Once this predetermined threshold is exceeded, an error will occur and the call will fail. For more information on this error, see [API Response Status Errors](https://developer.ebay.com/develop/api/sell/error_codes) (REST and GQL) and [Error by Number](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/Errors/errormessages.htm#524) (Trading API).
## Username Replacement for U.S. Buyers and Sellers
Effective September 26, 2025, developers in affected marketplaces will no longer receive private username data for U.S users. Instead, username values for all U.S. buyers and sellers will be replaced with an immutable user ID when calling impacted APIs. 
This includes:
  * **API responses** : All API responses that give out **username** in one form or another, such as: payer, payee, login name, username, etc.
  * **Notification payloads** : All notification payloads that return **username** in one form or another, such as: payer, payee, login name, username, etc.


**Note:** In API and notification payloads where both **username** and **userId** are returned, users in affected regions will now see the **userId** value returned in both the fields.
In addition, impacted APIs will now support both **username** and **userID** values in the request body, parameters, fieldgroups, filters, etc. to support this change.
Please refer to the tables below for a list of all APIs and fields impacted by this update:
**Traditional APIs:**  
| Request/Response  | API Name  | API Endpoint  | Field  |  
| --- | --- | --- | --- |  
| Request  |  **Trading API**  | AddSecondChanceItem  |  [AddSecondChanceItemRequest.RecipientBidderUserID](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/AddSecondChanceItem.html#Request.RecipientBidderUserID)  |  
| VerifyAddSecondChanceItem  |  [VerifyAddSecondChanceItemRequest.RecipientBidderUserID](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/VerifyAddSecondChanceItem.html#Request.RecipientBidderUserID)  |  
| CompleteSale  |  [CompleteSaleRequest.FeedbackInfo.TargetUser](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/CompleteSale.html#Request.FeedbackInfo.TargetUser)  |  
| GetBidderList   |  [GetBidderListRequest.UserID](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GetBidderList.html#Request.UserID)  |  
| GetFeedback   |  [GetFeedbackRequest.UserID](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GetFeedback.html#Request.UserID)  |  
| GetMessagePreferences   |  [GetMessagePreferencesRequest.SellerID](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GetMessagePreferences.html#Request.SellerID)  |  
| GetSellerList   |  [GetSellerListRequest.MotorsDealerUsers.UserID](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GetSellerList.html#Request.MotorsDealerUsers.UserID)  |  
| GetStore   |  [GetStoreRequest.UserID](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GetStore.html#Request.UserID)  |  
| GetUser   |  [GetUserRequest.UserID](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GetUser.html#Request.UserID)  |  
| GetUserContactDetails  |  [GetUserContactDetailsRequest.ContactID](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GetUserContactDetails.html#Request.ContactID)  |  
|  [GetUserContactDetailsRequest.RequesterID](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GetUserContactDetails.html#Request.RequesterID)  |  
| LeaveFeedback   |  [LeaveFeedbackRequest.TargetUser](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/LeaveFeedback.html#Request.TargetUser)  |  
| RespondToFeedback  |  [RespondToFeedbackRequest.TargetUserID](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/RespondToFeedback.html#Request.TargetUserID)  |  
| SetUserPreferences  |  [SetUserPreferencesRequest.UnpaidItemAssistancePreferences.ExcludedUser](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/SetUserPreferences.html#Request.UnpaidItemAssistancePreferences.ExcludedUser)  |  
| GetMemberMessages   |  [GetMemberMessagesRequest.SenderID](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GetMemberMessages.html#Request.SenderID)  |  
| AddMemberMessageAAQToPartner   |  [AddMemberMessageAAQToPartnerRequest.MemberMessage.RecipientID](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/AddMemberMessageAAQToPartner.html#Request.MemberMessage.RecipientID)  |  
| AddMemberMessageRTQ   |  [AddMemberMessageRTQRequest.MemberMessage.RecipientID](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/AddMemberMessageRTQ.html#Request.MemberMessage.RecipientID)  |  
| AddMemberMessagesAAQToBidder  |  [AddMemberMessagesAAQToBidderRequest.AddMemberMessagesAAQToBidderRequestContainer.MemberMessage.RecipientID](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/AddMemberMessagesAAQToBidder.html#Request.AddMemberMessagesAAQToBidderRequestContainer.MemberMessage.RecipientID)  |  
|  **Return Management API**  | getUserReturns   |  [getUserReturnsRequest.otherUserFilter.userId](https://developer.ebay.com/Devzone/return-management/CallRef/getUserReturns.html#Request.otherUserFilter.userId)  |  
| Response  | Trading API  | ConfirmIdentity  |  [ConfirmIdentityResponse.UserID](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/ConfirmIdentity.html#Response.UserID)  |  
|  GetAdFormatLeads   |  [GetAdFormatLeadsResponse.AdFormatLead.UserID](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GetAdFormatLeads.html#Response.AdFormatLead.UserID)  |  
| GetAllBidders  |  [GetAllBiddersResponse.HighBidder](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GetAllBidders.html#Response.HighBidder)  |  
|  [GetAllBiddersResponse.BidArray.Offer.User.UserID](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GetAllBidders.html#Response.BidArray.Offer.User.UserID)  |  
| GetBestOffers  |  [GetBestOffersResponse.BestOfferArray.BestOffer.Buyer.UserID](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GetBestOffers.html#Response.BestOfferArray.BestOffer.Buyer.UserID)  |  
|  [GetBestOffersResponse.ItemBestOffersArray.ItemBestOffers.BestOfferArray.BestOffer.Buyer.UserID](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GetBestOffers.html#Response.ItemBestOffersArray.ItemBestOffers.BestOfferArray.BestOffer.Buyer.UserID)  |  
| GetBidderList  |  [GetBidderListResponse.Bidder.UserID](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GetBidderList.html#Response.Bidder.UserID)  |  
|  [GetBidderListResponse.BidItemArray.Item.Seller.UserID](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GetBidderList.html#Response.BidItemArray.Item.Seller.UserID)  |  
|  [GetBidderListResponse.BidItemArray.Item.SellingStatus.HighBidder.UserID](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GetBidderList.html#Response.BidItemArray.Item.SellingStatus.HighBidder.UserID)  |  
| GetItem  |  [GetItemResponse.Item.Seller.UserID](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GetItem.html#Response.Item.Seller.UserID)  |  
|  [GetItemResponse.Item.SellingStatus.HighBidder.UserID](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GetItem.html#Response.Item.SellingStatus.HighBidder.UserID)  |  
|  [GetItemResponse.Item.Variations.Variation.SellingStatus.HighBidder.UserID](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GetItem.html#Response.Item.Variations.Variation.SellingStatus.HighBidder.UserID)  |  
| GetItemsAwaitingFeedback  |  [GetItemsAwaitingFeedbackResponse.ItemsAwaitingFeedback.TransactionArray.Transaction.Buyer.UserID](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GetItemsAwaitingFeedback.html#Response.ItemsAwaitingFeedback.TransactionArray.Transaction.Buyer.UserID)  |  
|  GetItemTransactions  |  [GetItemTransactionsResponse.TransactionArray.Transaction.MonetaryDetails.Payments.Payment.Payee](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GetItemTransactions.html#Response.TransactionArray.Transaction.MonetaryDetails.Payments.Payment.Payee)  |  
|  [GetItemTransactionsResponse.TransactionArray.Transaction.MonetaryDetails.Payments.Payment.Payer](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GetItemTransactions.html#Response.TransactionArray.Transaction.MonetaryDetails.Payments.Payment.Payer)  |  
|  [GetItemTransactionsResponse.Item.Seller.UserID](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GetItemTransactions.html#Response.Item.Seller.UserID)  |  
|  [GetItemTransactionsResponse.TransactionArray.Transaction.Buyer.UserID](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GetItemTransactions.html#Response.TransactionArray.Transaction.Buyer.UserID)  |  
| GetMyeBayBuying  |  [GetMyeBayBuyingResponse.FavoriteSearches.FavoriteSearch.SellerID](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GetMyeBayBuying.html#Response.FavoriteSearches.FavoriteSearch.SellerID)  |  
|  [GetMyeBayBuyingResponse.UserDefinedList.FavoriteSearches.FavoriteSearch.SellerID](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GetMyeBayBuying.html#Response.UserDefinedList.FavoriteSearches.FavoriteSearch.SellerID)  |  
|  [GetMyeBayBuyingResponse.FavoriteSearches.FavoriteSearch.SellerIDExclude](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GetMyeBayBuying.html#Response.FavoriteSearches.FavoriteSearch.SellerIDExclude)  |  
|  [GetMyeBayBuyingResponse.UserDefinedList.FavoriteSearches.FavoriteSearch.SellerIDExclude](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GetMyeBayBuying.html#Response.UserDefinedList.FavoriteSearches.FavoriteSearch.SellerIDExclude)  |  
|  [GetMyeBayBuyingResponse.BestOfferList.ItemArray.Item.Seller.UserID](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GetMyeBayBuying.html#Response.BestOfferList.ItemArray.Item.Seller.UserID)  |  
|  [GetMyeBayBuyingResponse.BidList.ItemArray.Item.Seller.UserID](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GetMyeBayBuying.html#Response.BidList.ItemArray.Item.Seller.UserID)  |  
|  [GetMyeBayBuyingResponse.BidList.ItemArray.Item.SellingStatus.HighBidder.UserID](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GetMyeBayBuying.html#Response.BidList.ItemArray.Item.SellingStatus.HighBidder.UserID)  |  
|  [GetMyeBayBuyingResponse.DeletedFromLostList.ItemArray.Item.Seller.UserID](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GetMyeBayBuying.html#Response.DeletedFromLostList.ItemArray.Item.Seller.UserID)  |  
|  [GetMyeBayBuyingResponse.DeletedFromLostList.ItemArray.Item.SellingStatus.HighBidder.UserID](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GetMyeBayBuying.html#Response.DeletedFromLostList.ItemArray.Item.SellingStatus.HighBidder.UserID)  |  
|  [GetMyeBayBuyingResponse.DeletedFromWonList.OrderTransactionArray.OrderTransaction.Order.TransactionArray.Transaction.Item.Seller.UserID](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GetMyeBayBuying.html#Response.DeletedFromWonList.OrderTransactionArray.OrderTransaction.Order.TransactionArray.Transaction.Item.Seller.UserID)  |  
|  [GetMyeBayBuyingResponse.DeletedFromWonList.OrderTransactionArray.OrderTransaction.Transaction.Item.Seller.UserID](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GetMyeBayBuying.html#Response.DeletedFromWonList.OrderTransactionArray.OrderTransaction.Transaction.Item.Seller.UserID)  |  
|  [GetMyeBayBuyingResponse.FavoriteSellers.FavoriteSeller.UserID](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GetMyeBayBuying.html#Response.FavoriteSellers.FavoriteSeller.UserID)  |  
|  [GetMyeBayBuyingResponse.LostList.ItemArray.Item.Seller.UserID](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GetMyeBayBuying.html#Response.LostList.ItemArray.Item.Seller.UserID)  |  
|  [GetMyeBayBuyingResponse.LostList.ItemArray.Item.SellingStatus.HighBidder.UserID](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GetMyeBayBuying.html#Response.LostList.ItemArray.Item.SellingStatus.HighBidder.UserID)  |  
|  [GetMyeBayBuyingResponse.UserDefinedList.FavoriteSellers.FavoriteSeller.UserID](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GetMyeBayBuying.html#Response.UserDefinedList.FavoriteSellers.FavoriteSeller.UserID)  |  
|  [GetMyeBayBuyingResponse.WatchList.ItemArray.Item.Seller.UserID](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GetMyeBayBuying.html#Response.WatchList.ItemArray.Item.Seller.UserID)  |  
|  [GetMyeBayBuyingResponse.WatchList.ItemArray.Item.SellingStatus.HighBidder.UserID](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GetMyeBayBuying.html#Response.LostList.ItemArray.Item.SellingStatus.HighBidder.UserID)  |  
|  [GetMyeBayBuyingResponse.WonList.OrderTransactionArray.OrderTransaction.Order.TransactionArray.Transaction.Item.Seller.UserID](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GetMyeBayBuying.html#Response.WonList.OrderTransactionArray.OrderTransaction.Order.TransactionArray.Transaction.Item.Seller.UserID)  |  
|  [GetMyeBayBuyingResponse.WonList.OrderTransactionArray.OrderTransaction.Transaction.Item.Seller.UserID](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GetMyeBayBuying.html#Response.WonList.OrderTransactionArray.OrderTransaction.Transaction.Item.Seller.UserID)  |  
| GetMyeBaySelling  |  [GetMyeBaySellingResponse.ActiveList.ItemArray.Item.SellingStatus.HighBidder.UserID](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GetMyeBaySelling.html#Response.ActiveList.ItemArray.Item.SellingStatus.HighBidder.UserID)  |  
|  [GetMyeBaySellingResponse.ActiveList.ItemArray.Item.Variations.Variation.SellingStatus.HighBidder.UserID](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GetMyeBaySelling.html#Response.ActiveList.ItemArray.Item.Variations.Variation.SellingStatus.HighBidder.UserID)  |  
|  [GetMyeBaySellingResponse.SoldList.OrderTransactionArray.OrderTransaction.Order.TransactionArray.Transaction.Buyer.UserID](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GetMyeBaySelling.html#Response.SoldList.OrderTransactionArray.OrderTransaction.Order.TransactionArray.Transaction.Buyer.UserID)  |  
|  [GetMyeBaySellingResponse.SoldList.OrderTransactionArray.OrderTransaction.Transaction.Buyer.UserID](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GetMyeBaySelling.html#Response.SoldList.OrderTransactionArray.OrderTransaction.Transaction.Buyer.UserID)  |  
| GetOrders  |  [GetOrdersResponse.OrderArray.Order.BuyerUserID](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GetOrders.html#Response.OrderArray.Order.BuyerUserID)  |  
|  [GetOrdersResponse.OrderArray.Order.MonetaryDetails.Payments.Payment.Payee](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GetOrders.html#Response.OrderArray.Order.MonetaryDetails.Payments.Payment.Payee)  |  
|  [GetOrdersResponse.OrderArray.Order.MonetaryDetails.Payments.Payment.Payer](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GetOrders.html#Response.OrderArray.Order.MonetaryDetails.Payments.Payment.Payer)  |  
|  [GetOrdersResponse.OrderArray.Order.SellerUserID](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GetOrders.html#Response.OrderArray.Order.SellerUserID)  |  
| GetSellerEvents  |  [GetSellerEventsResponse.ItemArray.Item.SellingStatus.HighBidder.UserID](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GetSellerEvents.html#Response.ItemArray.Item.SellingStatus.HighBidder.UserID)  |  
|  [GetSellerEventsResponse.ItemArray.Item.Variations.Variation.SellingStatus.HighBidder.UserID](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GetSellerEvents.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.HighBidder.UserID)  |  
| GetSellerList  |  [GetSellerListResponse.ItemArray.Item.SellingStatus.HighBidder.UserID](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GetSellerList.html#Response.ItemArray.Item.SellingStatus.HighBidder.UserID)  |  
|  [GetSellerListResponse.ItemArray.Item.Variations.Variation.SellingStatus.HighBidder.UserID](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GetSellerList.html#Response.ItemArray.Item.Variations.Variation.SellingStatus.HighBidder.UserID)  |  
|  [GetSellerListResponse.Seller.UserID](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GetSellerList.html#Response.Seller.UserID)  |  
| GetSellerTransactions  |  [GetSellerTransactionsResponse.TransactionArray.Transaction.MonetaryDetails.Payments.Payment.Payee](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GetSellerTransactions.html#Response.TransactionArray.Transaction.MonetaryDetails.Payments.Payment.Payee)  |  
|  [GetSellerTransactionsResponse.TransactionArray.Transaction.MonetaryDetails.Payments.Payment.Payer](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GetSellerTransactions.html#Response.TransactionArray.Transaction.MonetaryDetails.Payments.Payment.Payer)  |  
|  [GetSellerTransactionsResponse.Seller.UserID](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GetSellerTransactions.html#Response.Seller.UserID)  |  
|  [GetSellerTransactionsResponse.TransactionArray.Transaction.Buyer.UserID](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GetSellerTransactions.html#Response.TransactionArray.Transaction.Buyer.UserID)  |  
|  [GetSellerTransactionsResponse.TransactionArray.Transaction.MonetaryDetails.Refunds.Refund.RefundTo](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GetSellerTransactions.html#Response.TransactionArray.Transaction.MonetaryDetails.Refunds.Refund.RefundTo)  |  
| GetUser  |  [GetUserResponse.User.UserID](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GetUser.html#Response.User.UserID)  |  
| GetUserContactDetails  |  [GetUserContactDetailsResponse.UserID](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GetUserContactDetails.html#Response.UserID)  |  
| GetUserPreferences  |  [GetUserPreferencesResponse.UnpaidItemAssistancePreferences.ExcludedUser](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GetUserPreferences.html#Response.UnpaidItemAssistancePreferences.ExcludedUser)  |  
| PlaceOffer  |  [PlaceOfferResponse.SellingStatus.HighBidder.UserID](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/PlaceOffer.html#Response.SellingStatus.HighBidder.UserID)  |  
| GetMyMessages  |  [GetMyMessagesResponse.Messages.Message.SendToName](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GetMyMessages.html#Response.Messages.Message.SendToName)  |  
|  [GetMyMessagesResponse.Messages.Message.Sender](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GetMyMessages.html#Response.Messages.Message.Sender)  |  
|  [GetMyMessagesResponse.Messages.Message.RecipientUserID](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GetMyMessages.html#Response.Messages.Message.RecipientUserID)  |  
| GetMemberMessages  |  [GetMemberMessagesResponse.MemberMessage.MemberMessageExchange.Question.SenderID](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GetMemberMessages.html#Response.MemberMessage.MemberMessageExchange.Question.SenderID)  |  
|  [GetMemberMessagesResponse.MemberMessage.MemberMessageExchange.Question.RecipientID](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GetMemberMessages.html#Response.MemberMessage.MemberMessageExchange.Question.RecipientID)  |  
|  **Return Management API**  | getReturnDetail  |  [getReturnDetaiResponse.ReturnDetail.returnHistory.author.userId](https://developer.ebay.com/Devzone/return-management/CallRef/getReturnDetail.html#Response.ReturnDetail.returnHistory.author.userId)  |  
|  [getReturnDetailResponse.ReturnSummary.otherParty.userId](https://developer.ebay.com/Devzone/return-management/CallRef/getReturnDetail.html#Response.ReturnSummary.otherParty.userId)  |  
|  [getReturnDetailResponse.ReturnSummary.responseDue.party.userId](https://developer.ebay.com/Devzone/return-management/CallRef/getReturnDetail.html#Response.ReturnSummary.responseDue.party.userId)  |  
| getUserReturns  |  [getUserReturnsResponse.returns.otherParty.userId](https://developer.ebay.com/Devzone/return-management/CallRef/getUserReturns.html#Response.returns.otherParty.userId)  |  
|  [getUserReturnsResponse.returns.responseDue.party.userId](https://developer.ebay.com/Devzone/return-management/CallRef/getUserReturns.html#Response.returns.responseDue.party.userId)  |  
Rest APIs:  
| API Family  | Request/Response  | API Name  | API Endpoint  | Fields  |  
| --- | --- | --- | --- | --- |  
|  Sell  |  Request  |  **eDelivery International Shipping**  |  createPackage  |  [buyerId](https://developer.ebay.com/api-docs/sell/edelivery_international_shipping/resources/package/methods/createPackage#request.packageInfo.items.buyerId)  |  
|  **Feedback API**  |  getFeedback  |  [user_id](https://developer.ebay.com/api-docs/commerce/feedback/resources/feedback/methods/getFeedback#uri.user_id)  |  
|  respondToFeedback  |  [recipientUserId](https://developer.ebay.com/api-docs/commerce/feedback/resources/respond_to_feedback/methods/respondToFeedback#request.recipientUserId)  |  
|  Response  |  **Feedback API**  |  getFeedback  |  [userId](https://developer.ebay.com/api-docs/commerce/feedback/resources/feedback/methods/getFeedback#response.feedbackEntries.providerUserDetail.userId)  |  
|  **Fulfillment**  |  getOrder  |  [username ](https://developer.ebay.com/api-docs/sell/fulfillment/resources/order/methods/getOrder#response.buyer.username)  |  
|  [sellerId](https://developer.ebay.com/api-docs/sell/fulfillment/resources/order/methods/getOrder#response.lineItems.linkedOrderLineItems.sellerId)  |  
|  getOrders  |  [username](https://developer.ebay.com/api-docs/sell/fulfillment/resources/order/methods/getOrders#response.orders.buyer.username)  |  
|  [sellerId](https://developer.ebay.com/api-docs/sell/fulfillment/resources/order/methods/getOrders#response.orders.lineItems.linkedOrderLineItems.sellerId)  |  
|  getPaymentDispute  |  [buyerUsername](https://developer.ebay.com/api-docs/sell/fulfillment/resources/payment_dispute/methods/getPaymentDispute#response.buyerUsername)  |  
|  getPaymentDisputeSummaries  |  [buyerUsername](https://developer.ebay.com/api-docs/sell/fulfillment/resources/payment_dispute/methods/getPaymentDisputeSummaries#response.paymentDisputeSummaries.buyerUsername)  |  
|  **Finance**  |  getTransactions  |  [username](https://developer.ebay.com/api-docs/sell/finances/resources/transaction/methods/getTransactions#response.transactions.buyer.username)  |  
|  **Identity**  |  getUser  |  [username](https://developer.ebay.com/api-docs/commerce/identity/resources/user/methods/getUser#response.username)  |  
|  **Negotiation**  |  sendOfferToInterestedBuyers  |  [maskedUsername](https://developer.ebay.com/api-docs/sell/negotiation/resources/offer/methods/sendOfferToInterestedBuyers#response.offers.buyer.maskedUsername)  |  
|  [initiatedBy](https://developer.ebay.com/api-docs/sell/negotiation/resources/offer/methods/sendOfferToInterestedBuyers#response.offers.initiatedBy)  |  
|  **Post-Order Returns**  |  Get Return  |  [buyerLoginName](https://developer.ebay.com/devzone/post-order/post-order_v2_return-returnId__get.html#Response.detail.buyerLoginName)  |  
|  [sellerLoginName](https://developer.ebay.com/devzone/post-order/post-order_v2_return-returnId__get.html#Response.detail.sellerLoginName)  |  
|  Search Returns  |  [buyerLoginName](https://developer.ebay.com/devzone/post-order/post-order_v2_return_search__get.html#Response.members.buyerLoginName)  |  
|  [sellerLoginName](https://developer.ebay.com/devzone/post-order/post-order_v2_return_search__get.html#Response.members.sellerLoginName)  |  
|  Create Return Request  |  [buyerLoginName](https://developer.ebay.com/devzone/post-order/post-order_v2_return__post.html#Response.detail.detail.buyerLoginName)  |  
|  [sellerLoginName](https://developer.ebay.com/devzone/post-order/post-order_v2_return__post.html#Response.detail.detail.sellerLoginName)  |  
|  **Post-Order Cancellation**  |  Get Cancellation  |  [buyerLoginName](https://developer.ebay.com/devzone/post-order/post-order_v2_cancellation-cancelid__get.html#Response.cancelDetail.buyerLoginName)  |  
|  [sellerLoginName](https://developer.ebay.com/devzone/post-order/post-order_v2_cancellation-cancelid__get.html#Response.cancelDetail.sellerLoginName)  |  
|  Find Cancellations  |  [buyerLoginName](https://developer.ebay.com/devzone/post-order/post-order_v2_cancellation_search__get.html#Response.cancellations.buyerLoginName)  |  
|  [sellerLoginName](https://developer.ebay.com/devzone/post-order/post-order_v2_cancellation_search__get.html#Response.cancellations.sellerLoginName)  |  
|  **Post-Order Inquiry**  |  Search Inquiries  |  [buyer](https://developer.ebay.com/devzone/post-order/post-order_v2_inquiry_search__get.html#Response.members.buyer)  |  
|  [seller](https://developer.ebay.com/devzone/post-order/post-order_v2_inquiry_search__get.html#Response.members.seller)  |  
|  **Post-Order Case Management**  |  Search Cases  |  [buyer](https://developer.ebay.com/devzone/post-order/post-order_v2_casemanagement_search__get.html#Response.members.buyer)  |  
|  [seller](https://developer.ebay.com/devzone/post-order/post-order_v2_casemanagement_search__get.html#Response.members.seller)  |  
|  Buy  |  Request  |  **Feedback API**  |  getFeedback  |  [user_id](https://developer.ebay.com/api-docs/commerce/feedback/resources/feedback/methods/getFeedback#uri.user_id)  |  
|  respondToFeedback  |  [recipientUserId](https://developer.ebay.com/api-docs/commerce/feedback/resources/respond_to_feedback/methods/respondToFeedback#request.recipientUserId)  |  
|  Response  |  **Browse**  |  search  |  [username](https://developer.ebay.com/api-docs/buy/browse/resources/item_summary/methods/search#response.itemSummaries.seller.username)  |  
|  searchByImage  |  [username](https://developer.ebay.com/api-docs/buy/browse/resources/item_summary/methods/searchByImage#response.itemSummaries.seller.username)  |  
|  getItem  |  [username](https://developer.ebay.com/api-docs/buy/browse/resources/item/methods/getItem#response.seller.username)  |  
|  getItemByLegacyId  |  [username](https://developer.ebay.com/api-docs/buy/browse/resources/item/methods/getItemByLegacyId#response.seller.username)  |  
|  getItems  |  [username](https://developer.ebay.com/api-docs/buy/browse/resources/item/methods/getItems#response.items.seller.username)  |  
|  getItemsByItemGroup  |  [username](https://developer.ebay.com/api-docs/buy/browse/resources/item/methods/getItemsByItemGroup#response.items.seller.username)  |  
|  **eDelivery International Shipping**  |  getPackage  |  [username](https://developer.ebay.com/api-docs/sell/edelivery_international_shipping/resources/package/methods/getPackage#response.packageDetail.items.buyerId)  |  
|  **Feedback API**  |  getFeedback  |  [userId](https://developer.ebay.com/api-docs/commerce/feedback/resources/feedback/methods/getFeedback#response.feedbackEntries.providerUserDetail.userId)  |  
|  **Identity**  |  getUser  |  [username](https://developer.ebay.com/api-docs/commerce/identity/resources/user/methods/getUser#response.username)  |  
Notifications:   
| Notification Type  | Topic Name  | API Payload  | Fields  |  
| --- | --- | --- | --- |  
| Notifications via the new Notification Platform  |  [PLA_CAMPAIGN_BUDGET_STATUS](https://developer.ebay.com/api-docs/master/commerce/notification/asyncapi/pla_campaign_budget_status.yaml)  | N/A  |  user.username   |  
|  [PRIORITY_LISTING_REVISION](https://developer.ebay.com/api-docs/master/commerce/notification/asyncapi/priority_listing_revision.yaml)  | N/A  |  seller.userName   |  
|  [MARKETPLACE_ACCOUNT_DELETION](https://developer.ebay.com/api-docs/master/commerce/notification/asyncapi/marketplace_account_deletion.yaml)  | N/A  | username  |  
|  [AUTHORIZATION_REVOCATION](https://developer.ebay.com/api-docs/master/commerce/notification/asyncapi/authorization_revocation.yaml)  | N/A  | username  |  
|  [ITEM_AVAILABILITY](https://developer.ebay.com/api-docs/master/commerce/notification/asyncapi/item_availability.yaml)  | N/A  | seller.username  |  
|  [ITEM_PRICE_REVISION](https://developer.ebay.com/api-docs/master/commerce/notification/asyncapi/item_price_revision.yaml)  | N/A  |  seller.username   |  
|  [SELLER_STANDARDS_PROFILE_METRICS ](https://developer.ebay.com/api-docs/master/commerce/notification/asyncapi/seller_standards_profile_metrics.yaml)  | N/A  |  user.username   |  
|  [SELLER_CUSTOMER_SERVICE_METRIC_RATING](https://developer.ebay.com/api-docs/master/commerce/notification/asyncapi/seller_customer_service_metric_rating.yaml)  | N/A  | user.username  |  
|  [LISTING_PREVIEW_CREATION_TASK_STATUS](https://developer.ebay.com/api-docs/master/commerce/notification/asyncapi/listing_preview_creation_task_status.yaml)  | N/A  |  user.username   |  
|  [BUYER_QUESTION](https://developer.ebay.com/api-docs/master/commerce/notification/asyncapi/buyer_question.yaml)  | N/A  | senderUserName  |  
| N/A  | recipientUserName  |  
|  [NEW_MESSAGE](https://developer.ebay.com/api-docs/master/commerce/notification/asyncapi/new_message.yaml)  | N/A  | senderUserName  |  
| N/A  | recipientUserName  |  
| Legacy Notifications   | Outbid  |  [GetItem](https://developer.ebay.com/devzone/xml/docs/reference/ebay/getitem.html)  | N/A  |  
| EndOfAuction  |  [GetItemTransactions](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetItemTransactions.html)  | N/A  |  
| AuctionCheckoutComplete  |  [GetItemTransactions](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetItemTransactions.html)  | N/A  |  
| CheckoutBuyerRequestsTotal  |  [GetItemTransactions](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetItemTransactions.html)  | N/A  |  
| FeedbackForSeller  |  [GetFeedback](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetFeedback.html)  | N/A  |  
| FixedPriceTransaction  |  [GetItemTransactions](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetItemTransactions.html)  | N/A  |  
| AskSellerQuestion  |  [GetMemberMessages](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetMemberMessages.html)  | N/A  |  
| ItemListed  |  [GetItem](https://developer.ebay.com/devzone/xml/docs/reference/ebay/getitem.html)  | N/A  |  
| BestOffer  |  [GetBestOffers](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetBestOffers.html)  | N/A  |  
| ItemRevised  |  [GetItem](https://developer.ebay.com/devzone/xml/docs/reference/ebay/getitem.html)  | N/A  |  
| MyMessageseBayMessageHeader  |  [GetMyMessages](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetMyMessages.html)  | N/A  |  
| MyMessagseeBayMessage  |  [GetMyMessages](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetMyMessages.html)  | N/A  |  
| MyMessagesM2MMessageHeader  |  [GetMyMessages](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetMyMessages.html)  | N/A  |  
| MyMessagesM2MMessage  |  [GetMyMessages](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetMyMessages.html)  | N/A  |  
| ItemSold  |  [GetItem](https://developer.ebay.com/devzone/xml/docs/reference/ebay/getitem.html)  | N/A  |  
| ItemClosed  |  [GetItem](https://developer.ebay.com/devzone/xml/docs/reference/ebay/getitem.html)  | N/A  |  
| ItemExtended  |  [GetItem](https://developer.ebay.com/devzone/xml/docs/reference/ebay/getitem.html)  | N/A  |  
| BidPlaced  |  [GetItem](https://developer.ebay.com/devzone/xml/docs/reference/ebay/getitem.html)  | N/A  |  
| BidReceived  |  [GetItem](https://developer.ebay.com/devzone/xml/docs/reference/ebay/getitem.html)  | N/A  |  
| ItemWon  |  [GetItem](https://developer.ebay.com/devzone/xml/docs/reference/ebay/getitem.html)  | N/A  |  
| ItemUnsold  |  [GetItem](https://developer.ebay.com/devzone/xml/docs/reference/ebay/getitem.html)  | N/A  |  
| FeedbackLeft  |  [GetFeedback](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetFeedback.html)  | N/A  |  
| FeedbackStarChanged  |  [GetUser](https://developer.ebay.com/devzone/xml/docs/reference/ebay/getuser.html)  | N/A  |  
| BestOfferPlaced  |  [GetBestOffers](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetBestOffers.html)  | N/A  |  
| CounterOfferRecieved  |  [GetBestOffers](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetBestOffers.html)  | N/A  |  
| BestOfferDeclined  |  [GetBestOffers](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetBestOffers.html)  | N/A  |  
| FeedbackReceived  |  [GetFeedback](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetFeedback.html)  | N/A  |  
| ItemMarkedShipped  |  [GetItemTransactions](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetItemTransactions.html)  | N/A  |  
| MyMessagesHighPriorityMessage  |  [GetMyMessages](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetMyMessages.html)  | N/A  |  
| MyMessagesHighPriorityMessageHeader  |  [GetMyMessages](https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetMyMessages.html)  | N/A  |  
| BidItemEndingSoon  |  [GetItem](https://developer.ebay.com/devzone/xml/docs/reference/ebay/getitem.html)  | N/A  |  
| Post Order Notifications  |  EBPMyResponseDue   | N/A  | RecipientUserID  |  
| N/A  | OtherPartyId  |  
| EBPOtherPartyResponseDue  | N/A  | RecipientUserID  |  
| N/A  | OtherPartyId  |  
| EBPEscalatedCase  | N/A  | RecipientUserID  |  
| N/A  | OtherPartyId  |  
| EBPAppealedCase  | N/A  | RecipientUserID  |  
| N/A  | OtherPartyId  |  
| EBPPaymentDone  | N/A  | RecipientUserID  |  
| N/A  | OtherPartyId  |  
|  EBPClosedCase   | N/A  | RecipientUserID  |  
| N/A  | OtherPartyId  |  
|  EBPOnHoldCase   | N/A  | RecipientUserID  |  
| N/A  | OtherPartyId  |  
| ReturnCreated  | N/A  | RecipientUserID  |  
| N/A  | OtherPartyId  |  
| ReturnSellerInfoOverdue  | N/A  | RecipientUserID  |  
| N/A  | OtherPartyId  |  
| ReturnShipped  | N/A  | RecipientUserID  |  
| N/A  | OtherPartyId  |  
| ReturnDelivered  | N/A  | RecipientUserID  |  
| N/A  | OtherPartyId  |  
| ReturnRefundOverdue  | N/A  | RecipientUserID  |  
| N/A  | OtherPartyId  |  
| ReturnEscalated  | N/A  | RecipientUserID  |  
| N/A  | OtherPartyId  |  
| ReturnClosed  | N/A  | RecipientUserID  |  
| N/A  | OtherPartyId  |  
| WebnextMobilePhotoSync  | N/A  | RecipientUserID  |  
| BuyerCancelRequested  | N/A  | RecipientUserID  |  
| N/A  | OtherPartyId  |  
|  OrderInquiryReminderForEscalation   | N/A  | RecipientUserID  |  
| N/A  | OtherPartyId  |  
**Note:** Feed files downloaded through the Sell Feed API will also be impacted by this change. 
## Financial Data Handling for U.S. Buyers
Effective September 26, 2025, access to financial data related to U.S. buyers' payment methods and payment instruments will be limited to select developers only. For all other developers, any response field returning a U.S buyer’s payment details will have its values replaced with “CustomCode”. 
**Note:** The data for non-US persons will continue to be returned without change. 
Please refer to the tables below for a list of all APIs and fields impacted by this update: 
**Traditional APIs:**  
| Request/Response  | API Name  | API Endpoint  | Field  |  
| --- | --- | --- | --- |  
| Response  |  **Trading API**  | GetOrders  |  [OrderArray.Order.CheckoutStatus.PaymentInstrument](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GetOrders.html#Response.OrderArray.Order.CheckoutStatus.PaymentInstrument)  |  
|  [OrderArray.Order.CheckoutStatus.PaymentMethod](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GetOrders.html#Response.OrderArray.Order.CheckoutStatus.PaymentMethod)  |  
|  [OrderArray.Order.PaymentMethods](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GetOrders.html#Response.OrderArray.Order.PaymentMethods)  |  
|  [OrderArray.Order.TransactionArray.Transaction.Status.PaymentInstrument](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GetOrders.html#Response.OrderArray.Order.TransactionArray.Transaction.Status.PaymentInstrument)  |  
| GetItemTransactions  |  [TransactionArray.Transaction.Status.PaymentInstrument](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GetItemTransactions.html#Response.TransactionArray.Transaction.Status.PaymentInstrument)  |  
|  [TransactionArray.Transaction.Status.PaymentMethodUsed](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GetItemTransactions.html#Response.TransactionArray.Transaction.Status.PaymentMethodUsed)  |  
|  [TransactionArray.Transaction.Status.PaymentInstrument](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GetSellerTransactions.html#Response.TransactionArray.Transaction.Status.PaymentInstrument)  |  
| GetSellerTransactions  |  [TransactionArray.Transaction.Status.PaymentMethodUsed](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GetSellerTransactions.html#Response.TransactionArray.Transaction.Status.PaymentMethodUsed)  |  
**REST APIs:**  
| API Family  | Request/Response  | API Name  | API Endpoint  | Fields  |  
| --- | --- | --- | --- | --- |  
| Sell  | Response  |  **Fulfillment**  | getOrder  |  [paymentMethod](https://developer.ebay.com/api-docs/sell/fulfillment/resources/order/methods/getOrder#response.paymentSummary.payments.paymentMethod)  |  
| getOrders  |  [paymentMethod](https://developer.ebay.com/api-docs/sell/fulfillment/resources/order/methods/getOrders#response.orders.paymentSummary.payments.paymentMethod)  |  
|  **Feed**  | Order task download  | PaymentInstrument  |  
| PaymentMethod  |  
**Notifications:**  
| Notification Type  | Topic Name  | API Payload  | Fields  |  
| --- | --- | --- | --- |  
| Legacy Notifications  | FixedPriceTransaction  | GetItemTransactions  |  [TransactionArray.Transaction.Status.PaymentInstrument](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GetItemTransactions.html#Response.TransactionArray.Transaction.Status.PaymentInstrument)  |  
|  [TransactionArray.Transaction.Status.PaymentMethodUsed](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GetItemTransactions.html#Response.TransactionArray.Transaction.Status.PaymentMethodUsed)  |  
| AuctionCheckoutComplete  | GetItemTransactions  |  [TransactionArray.Transaction.Status.PaymentInstrument](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GetItemTransactions.html#Response.TransactionArray.Transaction.Status.PaymentInstrument)  |  
|  [TransactionArray.Transaction.Status.PaymentMethodUsed](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GetItemTransactions.html#Response.TransactionArray.Transaction.Status.PaymentMethodUsed)  |  
| EndOfAuction  | GetItemTransactions  |  [TransactionArray.Transaction.Status.PaymentInstrument](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GetItemTransactions.html#Response.TransactionArray.Transaction.Status.PaymentInstrument)  |  
|  [TransactionArray.Transaction.Status.PaymentMethodUsed](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GetItemTransactions.html#Response.TransactionArray.Transaction.Status.PaymentMethodUsed)  |  
| CheckoutBuyerRequestsTotal  | GetItemTransactions  |  [TransactionArray.Transaction.Status.PaymentInstrument](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GetItemTransactions.html#Response.TransactionArray.Transaction.Status.PaymentInstrument)  |  
|  [TransactionArray.Transaction.Status.PaymentMethodUsed](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GetItemTransactions.html#Response.TransactionArray.Transaction.Status.PaymentMethodUsed)  |  
| ItemMarkedShipped  | GetItemTransactions  |  [TransactionArray.Transaction.Status.PaymentInstrument](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GetItemTransactions.html#Response.TransactionArray.Transaction.Status.PaymentInstrument)  |  
|  [TransactionArray.Transaction.Status.PaymentMethodUsed](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GetItemTransactions.html#Response.TransactionArray.Transaction.Status.PaymentMethodUsed)  |  
**Note:** Feed files downloaded through the Sell Feed API will also be impacted by this change. 
## Implementation Timeline
These changes will be effective from September 26, 2025, for applications from the countries listed above.
## Related topics
  * [Start Here](https://developer.ebay.com/api-docs/static/ebay-rest-landing.html)
  * API Documentation
[Feed API](https://developer.ebay.com/api-docs/buy/feed/overview.html)[Browse API](https://developer.ebay.com/api-docs/buy/browse/overview.html)[Marketing API](https://developer.ebay.com/api-docs/buy/marketing/overview.html)[Offer API](https://developer.ebay.com/api-docs/buy/offer/overview.html)[Order API](https://developer.ebay.com/api-docs/buy/order/overview.html)[Marketplace Insights API](https://developer.ebay.com/api-docs/buy/marketplace-insights/overview.html)[Account API](https://developer.ebay.com/api-docs/sell/account/overview.html)[Inventory API](https://developer.ebay.com/api-docs/sell/inventory/overview.html)[Fulfillment API](https://developer.ebay.com/api-docs/sell/fulfillment/overview.html)[Finances API](https://developer.ebay.com/api-docs/sell/finances/overview.html)[Marketing API](https://developer.ebay.com/api-docs/sell/marketing/overview.html)[Negotiation API](https://developer.ebay.com/api-docs/sell/negotiation/overview.html)[Recommendation API](https://developer.ebay.com/api-docs/sell/recommendation/overview.html)[Analytics API](https://developer.ebay.com/api-docs/sell/analytics/overview.html)[Metadata API](https://developer.ebay.com/api-docs/sell/metadata/overview.html)[Compliance API](https://developer.ebay.com/api-docs/sell/compliance/overview.html)[Logistics API](https://developer.ebay.com/api-docs/sell/logistics/overview.html)[Listing API](https://developer.ebay.com/api-docs/sell/listing/overview.html)[Feed API](https://developer.ebay.com/api-docs/sell/feed/overview.html)[Catalog API](https://developer.ebay.com/api-docs/commerce/catalog/overview.html)[Identity API](https://developer.ebay.com/api-docs/commerce/identity/overview.html)[Taxonomy API](https://developer.ebay.com/api-docs/commerce/taxonomy/overview.html)[Translation API Beta](https://developer.ebay.com/api-docs/commerce/translation/overview.html)[Translation API Expermental](https://developer.ebay.com/api-docs/commerce/translation-exp/overview.html)[Analytics API](https://developer.ebay.com/api-docs/developer/analytics/overview.html)
  * Integration Guides
[Buying Integration Guide](https://developer.ebay.com/api-docs/buy/static/buying-ig-landing.html)[Selling Integration Guide](https://developer.ebay.com/api-docs/sell/static/selling-ig-landing.html)
  * Related Docs
[Sell API](https://developer.ebay.com/api-docs/sell/static/sell-landing.html)[Buy API](https://developer.ebay.com/api-docs/buy/static/buy-landing.html)[Commerce APIs](https://developer.ebay.com/api-docs/commerce/static/commerce-landing.html)[Developer APIs](https://developer.ebay.com/api-docs/developer/static/developer-landing.html)


On this page
[Username Replacement for U.S. Buyers and Sellers](https://developer.ebay.com/api-docs/static/data-handling-update.html#username-replacement)
[Financial Data Handling for U.S. Buyers](https://developer.ebay.com/api-docs/static/data-handling-update.html#financial-data-handling)
[Implementation Timeline](https://developer.ebay.com/api-docs/static/data-handling-update.html#implementation-timeline)
### eBay for Developers.
[Community Forum](https://community.ebay.com/t5/Developer-Groups/ct-p/developergroup)[Technical Support](https://developer.ebay.com/my/support/tickets)[APIs](https://developer.ebay.com/develop/api)[FAQs](https://developer.ebay.com/support/faq)
Copyright 1999—2026 eBay Inc. All rights reserved.
[API License Agreement](https://developer.ebay.com/join/api-license-agreement)[User agreement](http://pages.ebay.com/help/policies/user-agreement.html?rt=nc "opens in new window or tab")[Privacy policy](http://pages.ebay.com/help/policies/privacy-policy.html?rt=nc "opens in new window or tab")[Cookies](http://pages.ebay.com/help/account/cookies-web-beacons.html "opens in new window or tab")
#### Thank you for helping us to improve the eBay developer program.
While we are not able to respond directly to your comments, we will carefully review them to improve your experience with eBay developer program!
If you need help, contact [Developer Technical Support](https://developer.ebay.com/my/support/tickets) .

