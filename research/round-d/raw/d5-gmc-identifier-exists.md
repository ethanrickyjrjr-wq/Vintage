[Skip to main content](https://support.google.com/merchants/answer/6324478#hcfe-content)
[](https://support.google.com/?tab=uu)
[](https://support.google.com/?tab=uu)
[Google Merchant Center Help](https://support.google.com/merchants)
[](https://www.google.com/intl/en/about/products?tab=uh)
[Sign in](https://accounts.google.com/ServiceLogin?hl=en&passive=true&continue=http://support.google.com/merchants/answer/6324478&ec=GAZAdQ)
Send feedback on...
This help content & information
General Help Center experience
CloseNext
  * [Help Center](https://support.google.com/merchants/?hl=en)
  * [Community](https://support.google.com/merchants/community?hl=en&help_center_link=CP6BggMSJUlkZW50aWZpZXIgZXhpc3RzIFtpZGVudGlmaWVyX2V4aXN0c10)
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


# Identifier exists [identifier_exists]
Use the identifier exists `[identifier_exists]` attribute to indicate that unique product identifiers (UPIs) aren’t available for your product. Unique product identifiers are submitted using the [GTIN `[gtin]`](https://support.google.com/merchants/answer/6324461), [MPN `[mpn]`](https://support.google.com/merchants/answer/6324482), and [brand `[brand]`](https://support.google.com/merchants/answer/6324351) attributes.
**On this page**
  * [When to use](https://support.google.com/merchants/answer/6324478#When_to_use)
  * [Format](https://support.google.com/merchants/answer/6324478#Format)
  * [Supported values](https://support.google.com/merchants/answer/6324478#Supported_values)
  * [Minimum requirements](https://support.google.com/merchants/answer/6324478#Minimum_requirements)
  * [Examples](https://support.google.com/merchants/answer/6324478#Examples)


* * *
##  When to use
![Required](https://storage.googleapis.com/support-kms-prod/ncoEh9hPBwKEuXOUKRffUwCyLKZVt7PeCt6w) **Recommended** for products that don’t have a [GTIN `[gtin]`](https://support.google.com/merchants/answer/6324461), [MPN `[mpn]`](https://support.google.com/merchants/answer/6324482), or [brand `[brand]`](https://support.google.com/merchants/answer/6324351).
If your product is new (which you submit using the [condition `[condition]`](https://support.google.com/merchants/answer/6324469) attribute) and it doesn’t have assigned product identifiers that meet the requirements below, you should submit the identifier exists `[identifier_exists]` attribute with a value of no `[no]` or false `[false]`. Note this value must be submitted in English.
Products that might not have unique product identifiers include:
  * **Custom goods or one-of-a-kind products** , like custom T-shirts, art, or handmade goods
  * **Products produced before GTINs were introduced** , like vintage products, antiques, books published before 1970, and other special products.


* * *
##  Format
Follow these formatting guidelines to make sure Google understands the data you're submitting.
Learn [when and how to submit your product data in English](https://support.google.com/merchants/answer/160637)  
| **Formatting specifications**  |  
| --- |  
| **Technical name**  | `identifier_exists`  |  
| Type  | Boolean  |  
| Supported values  
(Text and XML data sources)  |  `yes`, `true`, `no`, `false`  |  
| Supported values  
(Merchant API data sources)  |  `true`,` false`  |  
| Repeated field  | No  |  
| Schema.org property ([What's this?](https://support.google.com/merchants/answer/6069143))  | No  |  
#### File format examples
To ensure your attribute is recognized correctly, use the formatting specific to your data source type.  
| Data source format  | Example entry  |  
| --- | --- |  
| **Text (TSV or CSV) data sources**  | `no`  |  
| **XML data sources**  | `<g:identifier_exists>no</g:identifier_exists>`  |  
| **Merchant API**  | To format your data for Merchant API, see the [Merchant API](https://developers.google.com/merchant/api/reference/rest/products_v1/accounts.productInputs) resource.  |  
**Note** : To ensure that this product data attribute gets recognized by our system correctly, remember to submit your data source file in a [format](https://support.google.com/merchants/answer/160567) that we support.
* * *
##  Minimum requirements
Follow these guidelines to make sure you submit high-quality data for your products.
  * **Ensure that you only set the value to no`[no]` or false `[false]` for this attribute if you're certain that your product doesn’t have any assigned unique product identifiers**. Note that the value must be submitted in English.
  * **Products for which the identifier exists`[identifier_exists]` attribute is incorrectly set to no `[no]` or false `[false]` and for which there is evidence that a unique product identifier exists, will receive a warning**. Note that the value must be submitted in English.


* * *
##  Examples
Products without GTINs, MPNs & brands
![An illustration of a woman wearing a black dress](https://storage.googleapis.com/support-kms-prod/khZlOkKG6Es0VO7lvLoAdYszi933kt4yxSTZ)  
| **Product data for a new customized black dress, size medium, 32 USD**  |  
| --- |  
| **Attribute**  | **Value**  |  
| Title `[title]`  | Customized Black Dress  |  
| Price `[price]`  | 32 USD  |  
| Color `[color]`  | Black  |  
| Size `[size]`  | M  |  
| Identifier exists `[identifier_exists]`  | `no`  |  
| Condition `[condition]`  | `new`  |  
| Bundle `[is_bundle]`  | `yes`  |  
| GTIN `[gtin]`  | _(Leave blank, since the dress is custom made and doesn't have a GTIN)_  |  
| MPN `[mpn]`  | _(Leave blank, since the dress is custom made and doesn't have an MPN)_  |  
![An illustration of a scarf that's in new condition](https://storage.googleapis.com/support-kms-prod/7KgGYFeiDY7I5i3lec4JkTrwBpX2cmncZoqW)  
| **Product data for a new, hand-knitted, orange and black polka dot wool scarf, 15 USD**  |  
| --- |  
| **Attribute**  | **Value**  |  
| Title `[title]`  | Hand knitted polka dot wool scarf - orange / black  |  
| Price `[price]`  | 15 USD  |  
| Color `[color]`  | Orange / black  |  
| Identifier exists `[identifier_exists]`  | `no`  |  
| Condition `[condition]`  | `new`  |  
| GTIN `[gtin]`  | _(Leave blank, since the scarf is custom made and doesn't have a GTIN)_  |  
| MPN `[mpn]`  | _(Leave blank, since the scarf is custom made and doesn't have an MPN)_  |  
Give feedback about this article
Choose a section to give feedback on
## Was this helpful?
How can we improve it?
Submit
## Need more help?
### Try these next steps:
[ Post to the help community  Get answers from community members  ](https://support.google.com/merchants/community?hl=en&help_center_link=CP6BggMSJUlkZW50aWZpZXIgZXhpc3RzIFtpZGVudGlmaWVyX2V4aXN0c10) [ Contact us Tell us more and we’ll help you get there ](https://support.google.com/merchants/gethelp)
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
14768055315758363937
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
  * Community](https://support.google.com/merchants/community?hl=en&help_center_link=CP6BggMSJUlkZW50aWZpZXIgZXhpc3RzIFtpZGVudGlmaWVyX2V4aXN0c10)[
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
By continuing, you agree Google uses your answers, [account & system info](https://support.google.com/merchants/answer/6324478) to improve services, per our [Privacy](https://myaccount.google.com/privacypolicy?hl=en) & [Terms](https://policies.google.com/terms?hl=en).
true
false
false

