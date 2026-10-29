[Skip to main content](https://support.google.com/merchants/answer/6324448#hcfe-content)
[](https://support.google.com/?tab=uu)
[](https://support.google.com/?tab=uu)
[Google Merchant Center Help](https://support.google.com/merchants)
[](https://www.google.com/intl/en/about/products?tab=uh)
[Sign in](https://accounts.google.com/ServiceLogin?hl=en&passive=true&continue=http://support.google.com/merchants/answer/6324448&ec=GAZAdQ)
Send feedback on...
This help content & information
General Help Center experience
CloseNext
  * [Help Center](https://support.google.com/merchants/?hl=en)
  * [Community](https://support.google.com/merchants/community?hl=en&help_center_link=COCBggMSG0F2YWlsYWJpbGl0eSBbYXZhaWxhYmlsaXR5XQ)
  * [Announcements](https://support.google.com/merchants/announcements/6192467)


[Google Merchant Center](https://merchants.google.com/)
  * Get to know Merchant Center
  * Business settings
  * Upload your products
  * [Product data specification](https://support.google.com/merchants/topic/7259406?hl=en&ref_topic=7259405,)
  * Market your products
  * Add-ons and additional features
  * [Understand your performance](https://support.google.com/merchants/topic/11983633?hl=en&ref_topic=7259405,)
  * Troubleshoot
  * 3rd party platform integrations


# Availability [availability]
As part of our recent suspension of ads in Russia, we will also pause ads on Google properties and networks globally for advertisers based in Russia.
Due to the ongoing war in Ukraine, we will be temporarily pausing Google ads from serving to users located in Russia.
Use the availability `[availability]` attribute as a real-time status indicator across your online store to tell users and Google if an item is ready to ship immediately, temporarily out of stock, available for preorder, or backordered.
**Note** : If you need to temporarily stop accepting orders or hide a product from Google, do not delete the item. Adding an offer back after deletion will take a significant amount of time before it can show again. Instead, if you want to temporarily stop showing your product, use the [pause `[pause]`](https://support.google.com/merchants/answer/11909930) attribute. If your product is not in stock `[in_stock]` and you're temporarily not accepting orders for it, set availability `[availability]` to out of stock `[out_of_stock]`.
**Important:** Some of the descriptions of this article are not applicable to vehicle ads. Learn more about [how and when to submit the availability `[availability]` attribute for vehicle ads](https://support.google.com/merchants/answer/11192663).
Use the availability `[availability]` attribute to tell users and Google whether you have a product in stock.
**On this page**
  * [When to use](https://support.google.com/merchants/answer/6324448#When_to_use)
  * [Format](https://support.google.com/merchants/answer/6324448#Format)
  * [Minimum requirements](https://support.google.com/merchants/answer/6324448#Minimum_requirements)
  * [Best practices](https://support.google.com/merchants/answer/6324448#Best_practices)
  * [Examples](https://support.google.com/merchants/answer/6324448#Examples)
  * [Frequently asked questions](https://support.google.com/merchants/answer/6324448#Frequently_asked_questions)


* * *
##  When to use
![Required](https://storage.googleapis.com/support-kms-prod/ncoEh9hPBwKEuXOUKRffUwCyLKZVt7PeCt6w) **Required** for all products. The values in your data source should always match the information on your website.
These are the supported values that you can choose from:
  * **In stock** `[in_stock]`
    * You’re accepting orders for this product and can fulfill the purchase request. You’re certain that the product will ship or be in-transit to the customer in a timely manner because it's available for sale. You can deliver the product to all of the locations that you support in your product data and shipping.
  * **Out of stock** `[out_of_stock]`
    * You’re not accepting orders for this product, or the product isn't available for purchase.
  * **Preorder**`[preorder]`
    * You’re accepting orders for this product, but it’s not been released for sale. You're required to provide the [availability date `[availability_date]`](https://support.google.com/merchants/answer/6324470) attribute to indicate the day that the product becomes available for delivery. The availability date should be visible on the landing page.
  * **Backorder** `[backorder]`
    * The product isn't available at the moment, but you’re accepting orders and it will be shipped when it's available again. You're required to provide the [availability date `[availability_date]`](https://support.google.com/merchants/answer/6324470) attribute to indicate the day when it will be shipped. The availability date should be visible on the landing page.
  * **Build to order** `[build_to_order]` (Vehicle ads only) 
    * The vehicle isn’t immediately available in dealership inventory, but it can be customized and ordered by the customer directly.


**Note:** The preorder `[preorder]` value should only be used for new products that haven’t been released yet. Existing products that are out of stock and will be back in stock at a later date that you’re accepting orders for should use backorder `[backorder]`.
* * *
##  Format
Follow these formatting guidelines to make sure Google understands the data that you submit. Learn [when and how to submit your product data in English](https://support.google.com/merchants/answer/10668075).  
| **Formatting specifications**  |  
| --- |  
| **Technical name**  | `availability`  |  
| **Supported values**  | 
  * In stock `[in_stock]`
  * Out of stock `[out_of_stock]`
  * Preorder `[preorder]`
  * Backorder `[backorder]`

 |  
| **Repeated field**  | No  |  
| **Schema.org property ([What's this?](https://support.google.com/merchants/answer/6069143))**  |  `Offer.availability[](https://schema.org/availability)`, Type: `ItemAvailability` How to map to Merchant Center values:
  * `in_stock`: InStock, LimitedAvailability, OnlineOnly
  * `out_of_stock`: Discontinued, InStoreOnly, OutOfStock, SoldOut
  * `preorder`: PreOrder, PreSale
  * `backorder`: BackOrder
  * `build_to_order`: BuildToOrder

 |  
**Note** : [Structured data markup](https://support.google.com/merchants/answer/6069143) for availability `[availability]` is crucial, as it is a machine-readable representation of your product data directly on your site which can be used to share your product data with Google Merchant Center. The markup that's added to your HTML helps Google and other search engines understand and process your content reliably.
### File format examples
To ensure your attribute is recognized correctly, use the formatting specific to your data source type.  
| File format  | Example value  |  
| --- | --- |  
| **Text data source**  | `in_stock`  |  
| **XML data source**  | `<g:availability>in_stock</g:availability>`  |  
|  **Merchant API**  |  To format your data in the Merchant API, check the[ Merchant API](https://developers.google.com/merchant/api/reference/rest/products_v1/ProductAttributes) resource.  |  
**Note** : To ensure that this product data attribute gets recognized by our system correctly, remember to submit your data source file in a [format](https://support.google.com/merchants/answer/160567) that we support.
* * *
##  Minimum requirements
These are the requirements you need to meet to show your product. If you don't follow these requirements, we disapprove of your product and let you know in your Merchant Center account.
  * **Indicate the product availability on your landing page**. Learn more about [Requirements for landing pages](https://support.google.com/merchants/answer/4752265). 
    * Ensure your landing page clearly displays product availability for online purchases. 
      * For “in stock” offers, the “Buy” button should be active.
      * For “out of stock” products, you can display clear text such as "sold out" or "item not available" or use a disabled/greyed out “buy” button. If a page features multiple variants, you can disable specific options in the selection grid to indicate they are unavailable.
      * The page must feature a functional “buy” or “add to basket” button if the product is available for purchase.
      * For “preorder” or “backorder” items, the page must display the expected shipping date.
      * The landing page must clearly state any delivery restrictions, such as “store pickup only”.
  * **Match your product availability with your account shipping.**
    * **Ship the product to all of the locations that you support** in your product data and shipping. This way, the availability that users see matches what you submit.
    * **Match the availability listed in your product data with the availability listed on your landing page and checkout pages.** When users come to your website, they expect to find the same availability on your landing page and during checkout that's provided in your product data. One common availability mismatch is that your shipping settings don’t reflect your delivery locations accurately.
    * **Make sure the product can be shipped, not just picked up in store.** In-store pickup is not currently supported with the exception of Argentina and Chile.
    * **If there are fixed regions or zip codes within a country where you don’t sell or ship any products** , you may be able to [exclude this region or zip code in your shipping settings](https://support.google.com/merchants/answer/12577710). If you do this, ensure all shipping services have the same configuration to exclude this region.
  * **Show a consistent availability across the landing page, structured data (if available), checkout page, and your data source**. The availability of all of your products needs to match across all three. A mismatch in one of these will trigger a product disapproval.
  * **If your products are not available within the entire target country** , make sure your offers are set up as “out of stock” for the regions that the products are not available in. Check to see whether [regional availability and pricing](https://support.google.com/merchants/answer/14644124) is available in your target country. Make sure your offers are set up as “out of stock” for those regions the products are not available.
  * **If there are specific zip codes within a region where you don’t sell or ship any products** , ensure you’re setting up [regional availability and pricing](https://support.google.com/merchants/answer/14644124).
  * **Provide the most up-to-date data.** Availability and prices of your products can change frequently. Learn more [About maintaining high-quality product data](https://support.google.com/merchants/answer/188489).
  * **Provide the[availability date `[availability_date]`](https://support.google.com/merchants/answer/6324470) attribute** if you submit `[preorder]`or `[backorder]`as the availability value. This information should be visible on your landing page.


**Note** : Add the availability date to the product’s landing page in a way that's clear to your customers (for example, “May 6, 2023”). If you can't provide an exact date, use an estimated date (for example, “May 2023”).
* * *
##  Best practices
These best practices can help you go beyond the basic requirements to optimize your product data for performance.
  * **When your product is temporarily unavailable** in the target country and you’re not accepting orders for it, set the availability `[availability]` attribute to `out_of_stock`. If we find that a product is out of stock on your landing page or during checkout, but the availability attribute is set to `in_stock` in your product data, we disapprove the product.
  * **Don't set the availability attribute to`out_of_stock` when you take down your website for maintenance or a holiday**. Use the [excluded destination `[excluded_destination]`](https://support.google.com/merchants/answer/6324486) attribute instead. By following this best practice, you prevent unnecessary disapprovals in your account and get your products running again more quickly than if they'd been disapproved.
  * **Don’t use`out_of_stock` when you don't want your product to show**. If the product is available for sale but you want to stop your product showing on certain or all destinations, use the [excluded destination `[excluded_destination]`](https://support.google.com/merchants/answer/6324486) or [pause `[pause]`](https://support.google.com/merchants/answer/11909930) attribute. For example, you can deactivate your product from showing on Shopping ads, but still show your products through other formats, such as free listings. If we find that a product is in stock on your landing page or during checkout, but the availability attribute is set to `out_of_stock` in your product data, we disapprove the product.
  * **Temporarily pause your product**. If you want to stop your product from showing in ads or free listings for up to 14 days, with the option to reactivate quickly, use the [pause `[pause]`](https://support.google.com/merchants/answer/11909930) attribute.
  * **Don't set the availability attribute to`out_of_stock` for products that you're no longer selling**. Remove any discontinued products from your product data.
  * **Consider using automatic item updates to help you avoid availability mismatches**. Automatic item updates is a feature that uses your landing page status to automatically update your product data, which prevents disapprovals.
  * **Product variant availability in the data source should match the availability on the landing page**. The availability of a product variant (for example, a shoe in size 8) in your data source should match the availability of the same product variant on its landing page.
  * **Use the[expiration date [expiration_date]](https://support.google.com/merchants/answer/6324499) attribute to control how long limited-time or seasonal items show on Google**. For permanently discontinued products, delete them entirely from your data source rather than setting them to out of stock `[out_of_stock]` to avoid account disapprovals. 
* * *
##  Examples
### Product is available for sale  
| **Product data for an Android Squishable available for sale**  |  
| --- |  
| **Attribute**  | **Value**  |  
| Availability `[availability]`  | `in_stock`  |  
The landing page for this product should display an "in stock" status.
### Product inventory ran out  
| **Product data for an Android Squishable that is out of stock**  |  
| --- |  
| **Attribute**  | **Value**  |  
| Availability `[availability]`  | `out_of_stock`  |  
The landing page for this product should display an "out of stock" status.
### Product inventory on backorder  
| **Product data for an Android Squishable that is on backorder**  |  
| --- |  
| **Attribute**  | **Value**  |  
| Availability `[availability]`  | `backorder`  |  
| Availability date `[availability_date]`  | `2021-05-24T13:00-0800`  |  
The landing page for this product should display an "on backorder" status. The availability date information should be displayed on the landing page.
### Product inventory on preorder  
| **Product data for an Android Squishable that is on preorder**  |  
| --- |  
| **Attribute**  | **Value**  |  
| Availability `[availability]`  | `preorder`  |  
| Availability date `[availability_date]`  | `2021-05-24T13:00-0800`  |  
The landing page for this product should display an "available for preorder" status. The availability date information should be displayed on the landing page.
### Temporarily stop a product from showing on Google
If you want to temporarily stop displaying a product in certain locations on Google, but you still have the product marked as being in stock on your landing page, you can use the [excluded destination `[excluded_destination]`](https://support.google.com/merchants/answer/6324486) attribute. This attribute allows you to control where your product is shown.
To stop your product from showing in ads for up to 14 days, with the option to reactivate quickly, use the [pause `[pause]` ](https://support.google.com/merchants/answer/11909930)attribute.  
| **Product data for an Android Squishable that is in stock and shown as in stock on the landing page**  |  
| --- |  
| **Attribute**  | **Value**  |  
| Availability `[availability]`  | `in_stock`  |  
| Excluded destination `[excluded_destination]`  |  `Shopping_ads`*  |  
| Shown in Shopping ads?  | No  |  
| Shown in free listings?  | Yes  |  
| **Product data for an Android Squishable that is in stock and shown as in stock on the landing page**  |  
| --- |  
| **Attribute**  | **Value**  |  
| Availability `[availability]`  | `in_stock`  |  
| Excluded destination `[excluded_destination]`  | `Free_listings`  |  
| Shown in Shopping ads?  | Yes  |  
| Shown in free listings?  | No  |  
| **Product data for an Android Squishable that is in stock but paused for 14 days or less from showing in ads**  |  
| --- |  
| **Attribute**  | **Value**  |  
| Availability `[availability]`  | `in_stock`  |  
| Pause `[pause]`  | `ads`  |  
***Note** : Exclude all destinations that you don’t want to use. Learn more [About the `excluded_destination `product data attribute](https://support.google.com/merchants/answer/6324486).
###  Variants
If your product comes in multiple colors or sizes, you might have different availability for each of these variants. The availability of a product variant (for example, a shoe in size 8) in your data source should match the availability of the same product variant on its landing page.
Example:
![An example of ads without placeholder images](https://storage.googleapis.com/support-kms-prod/kuBxjE4BVnaaDU13OjIM3F8PNau4iBkzSOtD)  
| **Product data for a small green Google T-shirt priced at $10.99 USD**  |  
| --- |  
| **Attribute**  | **Value**  |  
| Title `[title]`  | Google T-Shirt - Green - Small  |  
| Price `[price]`  | 10.99 USD  |  
| Availability `[availability]`  | `in_stock`  |  
| Color `[color]`  | Green  |  
| Size `[size]`  | S  |  
| ID `[id]`  | 9876-S-GRN  |  
| Item group ID `[item_group_id]`  | 9876  |  
| **Product data for a small blue Google T-shirt priced at $10.99 USD**  |  
| --- |  
| **Attribute**  | **Value**  |  
| Title `[title]`  | Google T-Shirt - Blue - Small  |  
| Price `[price]`  | 10.99 USD  |  
| Availability `[availability]`  | `in_stock`  |  
| Color `[color]`  | Blue  |  
| Size `[size]`  | S  |  
| ID `[id]`  | 9876-S-BLU  |  
| Item group ID `[item_group_id]`  | 9876  |  
| **Product data for a small yellow Google T-shirt priced at $10.99 USD**  |  
| --- |  
| **Attribute**  | **Value**  |  
| Title `[title]`  | Google T-Shirt - Yellow - Small  |  
| Price `[price]`  | 10.99 USD  |  
| Availability `[availability]`  | `out_of_stock`  |  
| Color `[color]`  | Yellow  |  
| Size `[size]`  | S  |  
| ID `[id]`  | 9876-S-YELLOW  |  
| Item group ID `[item_group_id]`  | 9876  |  


##  Frequently asked questions
## How do I inform users if a product is in stock?
Users frequently search for direct confirmation on stock availability. By accurately using the `in_stock` value in your product data, you ensure that your product surfaces effectively for these high-intent, transactional queries.
## How should I handle out of stock products?
If a product is temporarily unavailable, assign the `out_of_stock` value to accurately reflect its status without deleting the listing. If the product will restock and you are currently taking orders, update the status to backorder or preorder and pair it with an accurate availability date `[availability_date]` to manage expectations.
Give feedback about this article
Choose a section to give feedback on
## Was this helpful?
How can we improve it?
Submit
## Need more help?
### Try these next steps:
[ Post to the help community  Get answers from community members  ](https://support.google.com/merchants/community?hl=en&help_center_link=COCBggMSG0F2YWlsYWJpbGl0eSBbYXZhaWxhYmlsaXR5XQ) [ Contact us Tell us more and we’ll help you get there ](https://support.google.com/merchants/gethelp)
false
![](https://lh3.googleusercontent.com/x36xi17ti6RjHrRH4FVCPeH1_jIonM5eY2Fc-wJW3fwxsF-vqiYQ6DM_X0J86M7UtN2S=w396-h196)
Troubleshoot my availability mismatched value issue
If you received a disapproval for mismatched value (page crawl), explore the guided troubleshooter for ways to resolve the issue.
[Open troubleshooter](https://support.google.com/merchants/troubleshooter/15107089)
©2026 Google 
  * [Privacy Policy](https://www.google.com/intl/en/privacy.html)
  * [Terms of Service](https://support.google.com/merchants/answer/160173)


Send feedback on...
This help content & information General Help Center experience
Enable Dark Mode
Language  dansk‎ Deutsch‎ eesti‎ English (Ireland)‎ English (United Kingdom)‎ español‎ español (Latinoamérica)‎ français‎ Gaeilge‎ hrvatski‎ Indonesia‎ italiano‎ latviešu‎ lietuvių‎ magyar‎ Malti‎ Nederlands‎ norsk‎ polski‎ português (Brasil)‎ română‎ slovenčina‎ slovenščina‎ suomi‎ svenska‎ Tiếng Việt‎ Türkçe‎ čeština‎ Ελληνικά‎ български‎ русский‎ українська‎ ‏עברית ‏العربية हिन्दी‎ ไทย‎ 中文（简体）‎ 中文（繁體）‎ 日本語‎ 한국어‎ English‎
English‎
  1. dansk‎
  2. Deutsch‎
  3. eesti‎
  4. English (Ireland)‎
  5. English (United Kingdom)‎
  6. español‎
  7. español (Latinoamérica)‎
  8. français‎
  9. Gaeilge‎
  10. hrvatski‎
  11. Indonesia‎
  12. italiano‎
  13. latviešu‎
  14. lietuvių‎
  15. magyar‎
  16. Malti‎
  17. Nederlands‎
  18. norsk‎
  19. polski‎
  20. português (Brasil)‎
  21. română‎
  22. slovenčina‎
  23. slovenščina‎
  24. suomi‎
  25. svenska‎
  26. Tiếng Việt‎
  27. Türkçe‎
  28. čeština‎
  29. Ελληνικά‎
  30. български‎
  31. русский‎
  32. українська‎
  33. ‏עברית
  34. ‏العربية
  35. हिन्दी‎
  36. ไทย‎
  37. 中文（简体）‎
  38. 中文（繁體）‎
  39. 日本語‎
  40. 한국어‎
  41. English‎


Search
Clear search
Close search
Google apps
Main menu
4388219900537285599
true
Search Help Center
false
true
true
true
[Google Help](https://support.google.com/)
[
  * Help Center](https://support.google.com/merchants/?hl=en) [
    * Get to know Merchant Center](https://support.google.com/merchants/topic/12158920?hl=en&ref_topic=7259405,)[
    * Business settings](https://support.google.com/merchants/topic/11983022?hl=en&ref_topic=7259405,)[
    * Upload your products](https://support.google.com/merchants/topic/11983731?hl=en&ref_topic=7259405,)[
    * Product data specification](https://support.google.com/merchants/topic/7259406?hl=en&ref_topic=7259405,)[
    * Market your products](https://support.google.com/merchants/topic/12500201?hl=en&ref_topic=7259405,)[
    * Add-ons and additional features](https://support.google.com/merchants/topic/13421785?hl=en&ref_topic=7259405,)[
    * Understand your performance](https://support.google.com/merchants/topic/11983633?hl=en&ref_topic=7259405,)[
    * Troubleshoot](https://support.google.com/merchants/topic/12375009?hl=en&ref_topic=7259405,)[
    * 3rd party platform integrations](https://support.google.com/merchants/topic/15190247?hl=en&ref_topic=7259405,) [
  * Community](https://support.google.com/merchants/community?hl=en&help_center_link=COCBggMSG0F2YWlsYWJpbGl0eSBbYXZhaWxhYmlsaXR5XQ)[
  * Google Merchant Center](https://merchants.google.com/)
[
  * Privacy Policy](https://www.google.com/intl/en/privacy.html)[
  * Terms of Service](https://support.google.com/merchants/answer/160173)
  * Submit feedback


[Get started](https://support.google.com/merchants/topic/15302229?hl=en&ref_topic=12158920,7259405,)[Set up your Merchant Center account](https://support.google.com/merchants/topic/12671531?hl=en&ref_topic=12158920,7259405,)[Comparison Shopping Services](https://support.google.com/merchants/topic/12652782?hl=en&ref_topic=12158920,7259405,)[Policies and requirements](https://support.google.com/merchants/topic/7286989?hl=en&ref_topic=12158920,7259405,)[Glossary](https://support.google.com/merchants/table/15620279?hl=en&ref_topic=12158920,7259405,)
[Manage your shipping settings](https://support.google.com/merchants/topic/12570808?hl=en&ref_topic=11983022,7259405,)[Manage your business settings](https://support.google.com/merchants/topic/12564660?hl=en&ref_topic=11983022,7259405,)[Manage integrations](https://support.google.com/merchants/topic/12564658?hl=en&ref_topic=11983022,7259405,)[Manage your account](https://support.google.com/merchants/topic/17153858?hl=en&ref_topic=11983022,7259405,)
[Add products](https://support.google.com/merchants/topic/12672304?hl=en&ref_topic=11983731,7259405,)[Product data specification](https://support.google.com/merchants/topic/7259406?hl=en&ref_topic=11983731,7259405,)[Maintain your product data](https://support.google.com/merchants/topic/12672214?hl=en&ref_topic=11983731,7259405,)[Set up rules for your product data sources](https://support.google.com/merchants/topic/14957981?hl=en&ref_topic=11983731,7259405,)[Create product data sources for Performance Max campaigns](https://support.google.com/merchants/topic/14958782?hl=en&ref_topic=11983731,7259405,)[Use AI and AR tools to show your products ](https://support.google.com/merchants/topic/15189223?hl=en&ref_topic=11983731,7259405,)[Troubleshoot product data source issues](https://support.google.com/merchants/topic/14957024?hl=en&ref_topic=11983731,7259405,)[Best practices for different product situations](https://support.google.com/merchants/topic/15712169?hl=en&ref_topic=11983731,7259405,)
[Ad campaigns](https://support.google.com/merchants/topic/15191542?hl=en&ref_topic=12500201,7259405,)[Automated discounts](https://support.google.com/merchants/topic/15303099?hl=en&ref_topic=12500201,7259405,)[Free listings](https://support.google.com/merchants/topic/15190028?hl=en&ref_topic=12500201,7259405,)[Local inventory ads and free local listings](https://support.google.com/merchants/topic/14607119?hl=en&ref_topic=12500201,7259405,)[Prepare for big events](https://support.google.com/merchants/topic/15710958?hl=en&ref_topic=12500201,7259405,)[YouTube Shopping affiliate program](https://support.google.com/merchants/topic/14813437?hl=en&ref_topic=12500201,7259405,)[Promotions](https://support.google.com/merchants/topic/13461580?hl=en&ref_topic=12500201,7259405,)[YouTube Store](https://support.google.com/merchants/topic/15643752?hl=en&ref_topic=12500201,7259405,)[Vehicle ads](https://support.google.com/merchants/topic/15174524?hl=en&ref_topic=12500201,7259405,)
[Automated discounts](https://support.google.com/merchants/topic/15303099?hl=en&ref_topic=13421785,7259405,)[Universal Commerce Protocol](https://support.google.com/merchants/topic/16837563?hl=en&ref_topic=13421785,7259405,)[Google Customer Reviews](https://support.google.com/merchants/topic/14628801?hl=en&ref_topic=13421785,7259405,)[Local inventory ads and free local listings](https://support.google.com/merchants/topic/14607119?hl=en&ref_topic=13421785,7259405,)[Loyalty programs](https://support.google.com/merchants/topic/15164622?hl=en&ref_topic=13421785,7259405,)[Merchant knowledge panel](https://support.google.com/merchants/topic/14111503?hl=en&ref_topic=13421785,7259405,)[Product Ratings](https://support.google.com/merchants/topic/14548703?hl=en&ref_topic=13421785,7259405,)[Product Studio](https://support.google.com/merchants/topic/15304400?hl=en&ref_topic=13421785,7259405,)[Promotions](https://support.google.com/merchants/topic/13461580?hl=en&ref_topic=13421785,7259405,)[Store Ratings](https://support.google.com/merchants/topic/15630416?hl=en&ref_topic=13421785,7259405,)[Vehicle ads](https://support.google.com/merchants/topic/15174524?hl=en&ref_topic=13421785,7259405,)[Regional availability and pricing](https://support.google.com/merchants/topic/16778522?hl=en&ref_topic=13421785,7259405,)
[About issues](https://support.google.com/merchants/topic/12565358?hl=en&ref_topic=12375009,7259405,)
[Manage your account with a Shopify integration](https://support.google.com/merchants/topic/13686797?hl=en&ref_topic=15190247,7259405,)
true
true
71525
false
false
## What is the issue with this selection?
What is the issue with this selection?
Inaccurate - doesn't match what I see in the product
Hard to understand - unclear or translation is wrong
Missing info - relevant but not comprehensive
Irrelevant - doesn’t match the title and / or my expectations
Minor errors - formatting issues, typos, and / or broken links
Other suggestions - ideas to improve the content
## Share additional info or suggestions
​
​
Do not share any personal info
Cancel
Submit
By continuing, you agree Google uses your answers, [account & system info](https://support.google.com/merchants/answer/6324448) to improve services, per our [Privacy](https://myaccount.google.com/privacypolicy?hl=en) & [Terms](https://policies.google.com/terms?hl=en).
true
false
false

