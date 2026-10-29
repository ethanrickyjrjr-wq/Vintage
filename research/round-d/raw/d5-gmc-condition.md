[Skip to main content](https://support.google.com/merchants/answer/6324469#hcfe-content)
[](https://support.google.com/?tab=uu)
[](https://support.google.com/?tab=uu)
[Google Merchant Center Help](https://support.google.com/merchants)
[](https://www.google.com/intl/en/about/products?tab=uh)
[Sign in](https://accounts.google.com/ServiceLogin?hl=en&passive=true&continue=http://support.google.com/merchants/answer/6324469&ec=GAZAdQ)
Send feedback on...
This help content & information
General Help Center experience
CloseNext
  * [Help Center](https://support.google.com/merchants/?hl=en)
  * [Community](https://support.google.com/merchants/community?hl=en&help_center_link=CPWBggMSFUNvbmRpdGlvbiBbY29uZGl0aW9uXQ)
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


# Condition [condition]
As part of our recent suspension of ads in Russia, we will also pause ads on Google properties and networks globally for advertisers based in Russia.
Due to the ongoing war in Ukraine, we will be temporarily pausing Google ads from serving to users located in Russia.
**Note** : Regardless of the campaign type, used and refurbished products aren’t displayed on YouTube organic and Discover surfaces. These items can still serve as ads on YouTube, the Google Display Network, and Gmail.
Use the condition `[condition]` attribute to tell potential customers about the condition of the product you're selling. It’s important to set this value correctly since it is used to refine search results.
![An illustration of a shoe that isn't in new condition](https://lh3.googleusercontent.com/ZS6tl8L298dvlnFb6pbFpOnNnQzEkwEUp3pn1q5y77GS772d5XAQm35Nx_I22H1WuQ=w895)
**On this page**
  * [When to use](https://support.google.com/merchants/answer/6324469#Whentouse)
  * [Supported values](https://support.google.com/merchants/answer/6324469#Supported_values)
  * [Format](https://support.google.com/merchants/answer/6324469#Format)
  * [Minimum requirements](https://support.google.com/merchants/answer/6324469#Minirequirements)
  * [Additional guidelines](https://support.google.com/merchants/answer/6324469#Additional_guidelines)
  * [Best practices](https://support.google.com/merchants/answer/6324469#Bestpractices)
  * [Examples](https://support.google.com/merchants/answer/6324469#Examples)


* * *
##  When to use
![Optional](https://storage.googleapis.com/support-kms-prod/p4E0rwqEBmdrMxeIBZGYPLtLvUYbXguSiydf)**Optional** for each new product
![Required](https://storage.googleapis.com/support-kms-prod/ncoEh9hPBwKEuXOUKRffUwCyLKZVt7PeCt6w)**Required** for each used and refurbished product
* * *
## Supported values
These are the supported values for this attribute:  
|  **Supported value**  |   |  
| --- | --- |  
| **New`[new]`**  | Your product is new and has never been used. It's in its original packaging, and has not been opened.  |  
| **Refurbished`[refurbished]`**  | While your product isn’t new, it's been professionally restored to working order so that it appears new, and comes with a warranty. The product might or might not be in its original packaging and is sometimes referred to as "remanufactured". This value isn’t supported for Vehicle ads.  |  
| **Used`[used]`**  | Your product is second-hand or has been modified from the original condition as sold by the manufacturer. For example, the product shows wear or has been used before, the original packaging has been opened or is missing, or the product has been customized, repackaged, autographed, or otherwise modified from its original state.  |  
* * *
##  Format
Follow these formatting guidelines to make sure Google understands the data you're submitting. Learn [when and how to submit your product data](https://support.google.com/merchants/answer/10668075).  
| Formatting specifications  |  
| --- |  
| Technical name  | `condition`  |  
| Supported values  | 
  * `new`
  * `refurbished`
  * `used`

 |  
| Repeated field  | No  |  
| Schema.org property  
([What's this?](https://support.google.com/merchants/answer/6069143))  |  [Offer.itemCondition](http://schema.org/itemCondition), Type: `OfferItemCondition` Mapping:
  * `new`: `NewCondition`
  * `refurbished`: `RefurbishedCondition`
  * `used`: `DamagedCondition`, `UsedCondition`

 |  
### File format examples
To ensure your attribute is recognized correctly, use the formatting specific to your data source type.  
| **Data source format**  | **Examples**  |  
| --- | --- |  
| **Text data source**  | `used`  |  
| **XML data source**  | `<g:condition>used</g:condition>`  |  
| **Merchant API**  | To format your data for Merchant API, check the [Merchant API](https://developers.google.com/merchant/api/reference/rest/products_v1/accounts.productInputs) resource.  |  
* * *
##  Minimum requirements
These are the requirements you'll need to meet to show your product. If you don't follow these requirements, we'll disapprove your product and let you know in your Merchant Center account.
  * **Comply with local laws and regulations when submitting refurbished products**. Your target country may have certain laws that relate to refurbished products, so before selling a refurbished product, make sure it complies with the local laws and regulations and with the relevant [Shopping policies and requirements](https://support.google.com/merchants/topic/7286989).
  * **Submit the correct unique product identifiers for your product**. What information you should submit can vary based on your product’s condition. Learn more [About unique product identifiers](https://support.google.com/merchants/answer/160161).
  * **If you sell products of third party manufacturers that are compatible with Original Equipment Manufacturer (OEM) products,** review the [additional guidelines for compatible or refurbished third party products](https://support.google.com/merchants/answer/7558050).


* * *
## Additional guidelines
Review each section closely to determine if the requirements apply to your country or product.
Printer cartridges
The condition you submit depends on whether the printer cartridge you’re selling is used, refurbished, refilled, or new. Learn more [about requirements for printer cartridges](https://support.google.com/merchants/answer/7558050#printercartridges).
[ ](https://support.google.com/merchants/answer/7558050#printercartridges)
Vehicle ads
Vehicle ads support only new and used conditions. A vehicle is generally defined as "new" if the mileage is 200 miles (200 km) or less. However, note that this specific mileage limit doesn’t apply to Germany.
* * *
##  Best practices
These best practices can help you go beyond the basic requirements to optimize your product data for performance.
**Consider using automatic item updates to help you avoid condition mismatches.** Automatic item updates is a feature that compares the values you submit in other parts of your product data against the values submitted for the condition `[condition]` attribute to automatically update the condition of your products, preventing disapprovals.
* * *
##  Examples
Apparel
![An illustration of a scarf that isn't in new condition](https://lh3.googleusercontent.com/5mC3lwo4MuQTz3Ua6NhiBoAn8tkUy0fCUXtBwN4QJ0KtWPFrfCTvul3pD5sBJbzGKw=w895)  
| **Product data for a new orange polka-dot scarf**  |  
| --- |  
| **Attribute**  | **Value**  |  
| Title `[title]`  | Polka dot scarf - orange and black  |  
| Condition `[condition]`  | `new`  |  
| Price `[price]`  | 15.00 USD  |  
| Color `[color]`  | Orange/black  |  
| **Product data for a used orange polka-dotted scarf**  |  
| --- |  
| **Attribute**  | **Value**  |  
| Title `[title]`  | Polka dot scarf - used - orange and black  |  
| Condition `[condition]`  | `used`  |  
| Price `[price]`  | 5.00 USD  |  
| Color `[color]`  | Orange/black  |  
![An illustration of a shoe that isn't in new condition](https://lh3.googleusercontent.com/ZS6tl8L298dvlnFb6pbFpOnNnQzEkwEUp3pn1q5y77GS772d5XAQm35Nx_I22H1WuQ=w895)  
| **Product data for new pink high heel shoes, size 6**  |  
| --- |  
| **Attribute**  | **Value**  |  
| Title `[title]`  | High Heels - hot pink - Size 6  |  
| Condition `[condition]`  | `new`  |  
| Price `[price]`  | 59.00 USD  |  
| Color `[color]`  | Hot pink  |  
| Size `[size]`  | 6  |  
| **Product data for vintage pink high heel shoes, size 6**  |  
| --- |  
| **Attribute**  | **Value**  |  
| Title `[title]`  | Hot Pink Vintage High Heels - 1930s - Size 6  |  
| Condition `[condition]`  | `used`  |  
| Price `[price]`  | 10.00 USD  |  
| Color `[color]`  | Hot pink  |  
| Size `[size]`  | 6  |  
Electronics
![](https://storage.googleapis.com/support-kms-prod/Tv7w8CagAwnf4aYOBFt5nzrRBdzAHz9yYCh5)  
| **Product data for a black Chromecast 2, 1080p, wi-fi, new**  |  
| --- |  
| **Attribute**  | **Value**  |  
| Title `[title]`  | Google Chromecast 2 - 1080p - Wi-Fi - Black  |  
| Condition `[condition]`  | `new`  |  
| GTIN `[gtin]`  | 0811571016518  |  
| Brand `[brand]`  | Google  |  
| **Product data for a black Chromecast 2, 1080p, wi-fi, refurbished**  |  
| --- |  
| **Attribute**  | **Value**  |  
| Title `[title]`  | Refurbished Google Chromecast 2 - 1080p - Wi-Fi - Black  |  
| Condition `[condition]`  | `refurbished`  |  
| GTIN `[gtin]`  | 0811571016518  |  
| Brand `[brand]`  | Google  |  
Phone and tablet 
![An illustration with 3 different colors of one mobile phone](https://storage.googleapis.com/support-kms-prod/LrpBnwjSdFJKSbV3jbM1FPpbXpTWDBv6Zjsy)  
| **Product data for a Google Pixel 3, 32 GB, midnight blue, unlocked, new**  |  
| --- |  
| **Attribute**  | **Value**  |  
| Title `[title]`  | Google Pixel 3 ;- 32 GB - Midnight Blue - unlocked  |  
| Condition `[condition]`  | `new`  |  
| GTIN `[gtin]`  | 3234567890126  |  
| Brand `[brand]`  | Google  |  
| Google product category `[google_product_category]`  | `Electronics > Communications > Telephony > Mobile Phones`  |  
| **Product data for a Google Pixel 2, 32 GB, midnight blue, unlocked, refurbished**  |  
| --- |  
| **Attribute**  | **Value**  |  
| Title `[title]`  | Google Pixel 2 - Refurbished- 32 GB - Midnight Blue - unlocked  |  
| Condition `[condition]`  | `refurbished`  |  
| GTIN `[gtin]`  | 3234567890126  |  
| Brand `[brand]`  | Google  |  
| Google product category `[google_product_category]`  |  `Electronics > Communications > Telephony > Mobile Phones`  |  
Memorabilia
![](https://storage.googleapis.com/support-kms-prod/ComEpyP7pQKNHDhyBH8leugYCMsEmMXoDGTK)  
| **Product data for new collectible memorabilia**  |  
| --- |  
| **Attribute**  | **Value**  |  
| Title `[title]`  | Limited edition 2020 championship hat  |  
| Condition `[condition]`  | `new`  |  
| Price `[price]`  | 129.00 USD  |  
| Color `[color]`  | Blue  |  
| **Product data for modified collectible memorabilia**  |  
| --- |  
| **Attribute**  | **Value**  |  
| Title `[title]`  | Limited edition 2020 championship hat - signed - in display case.  |  
| Condition `[condition]`  | `used`  |  
| Price `[price]`  | 155.00 USD  |  
| Color `[color]`  | Blue  |  
Give feedback about this article
Choose a section to give feedback on
## Was this helpful?
How can we improve it?
Submit
## Need more help?
### Try these next steps:
[ Post to the help community  Get answers from community members  ](https://support.google.com/merchants/community?hl=en&help_center_link=CPWBggMSFUNvbmRpdGlvbiBbY29uZGl0aW9uXQ) [ Contact us Tell us more and we’ll help you get there ](https://support.google.com/merchants/gethelp)
false
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
4637796269331854655
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
  * Community](https://support.google.com/merchants/community?hl=en&help_center_link=CPWBggMSFUNvbmRpdGlvbiBbY29uZGl0aW9uXQ)[
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
By continuing, you agree Google uses your answers, [account & system info](https://support.google.com/merchants/answer/6324469) to improve services, per our [Privacy](https://myaccount.google.com/privacypolicy?hl=en) & [Terms](https://policies.google.com/terms?hl=en).
true
false
false

