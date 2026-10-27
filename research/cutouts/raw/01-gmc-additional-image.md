[Skip to main content](https://support.google.com/merchants/answer/6324370?hl=en#hcfe-content)
[](https://support.google.com/?tab=uu)
[](https://support.google.com/?tab=uu)
[Google Merchant Center Help](https://support.google.com/merchants)
[](https://www.google.com/intl/en/about/products?tab=uh)
[Sign in](https://accounts.google.com/ServiceLogin?hl=en&passive=true&continue=http://support.google.com/merchants/answer/6324370%3Fhl%3Den&ec=GAZAdQ)
Send feedback on...
This help content & information
General Help Center experience
CloseNext
  * [Help Center](https://support.google.com/merchants/?hl=en)
  * [Community](https://support.google.com/merchants/community?hl=en&help_center_link=CJKBggMSLUFkZGl0aW9uYWwgaW1hZ2UgbGluayBbYWRkaXRpb25hbF9pbWFnZV9saW5rXQ)
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


# Additional image link [additional_image_link]
Use the additional image link `[additional_image_link]` attribute to provide more images for your product beyond the main image you provide in the [image link `[image_link]`](https://support.google.com/merchants/answer/6324350) attribute. Additional images for your product can appear to potential customers and are commonly used to show a product from different angles or with product staging elements.
**Important: We recently announced new image size requirements of at least 500 x 500 pixels for all products beginning January 31, 2027**. However, to ensure best performance in all listing formats, we recommend that you provide images 1500x1500 pixels or above.
![Example ad that shows where additional images can appear with your product](https://storage.googleapis.com/support-kms-prod/vj3wDs0VDPD5rmtogIqqxOjh4buGFBvc4kKm)
**On this page**
  * [When to use](https://support.google.com/merchants/answer/6324370?hl=en#Whentouse)
  * [Format](https://support.google.com/merchants/answer/6324370?hl=en#Format)
  * [Minimum requirements](https://support.google.com/merchants/answer/6324370?hl=en#Minirequirements)
  * [Best practices](https://support.google.com/merchants/answer/6324370?hl=en#Bestpractices)
  * [Examples](https://support.google.com/merchants/answer/6324370?hl=en#Examples)


* * *
##  When to use
![Optional](https://storage.googleapis.com/support-kms-prod/p4E0rwqEBmdrMxeIBZGYPLtLvUYbXguSiydf) **Optional** but recommended for each product
* * *
##  Format
Follow these formatting guidelines to make sure Google understands the data you're submitting. Learn [when and how to submit your product data](https://support.google.com/merchants/answer/10668075).  
| **Formatting specifications**  |  
| --- |  
| **Technical name**  | `additional_image_link`  |  
| **Type**  | URL (including `http` or `https`), ASCII characters only, and RFC 3986 compliant  |  
| **Limits**  | 1–2,000 characters  |  
| **Supported file formats**  |  JPEG (.jpg/.jpeg), WebP (.webp), PNG (.png), GIF (.gif), BMP (.bmp), and TIFF (.tif/.tiff) The file extensions for these images should correspond to their format.  |  
| **Repeated field ([What's this?](https://support.google.com/merchants/answer/7278995))**  | Include up to 10 additional images  |  
| **Schema.org property ([What’s this?](https://support.google.com/merchants/answer/6069143))**  | No  |  
### File format examples
To ensure your attribute is recognized correctly, use the formatting specific to your data source type.  
| **Data source format**  | **Examples**  |  
| --- | --- |  
| **Text data sources**  |  **To submit one image,** submit the (encoded) URL: `https://www.example.com/image2.jpg` **To submit more than one image (up to 10),** separate each URL with a comma ( `,` ): `https://www.example.com/image2.jpg,https://www.example.com/image3.jpg` Make sure to encode any commas (as `%2C`) within the URL, but don’t encode the comma that you use to separate each image URL: `https://www.example.com/image2%2C3.jpg,https://www.example.com/image2%2C4.jpg` Alternatively, you can enclose each individual URL with quotation marks (`“”`), and separate the URLs with commas, for example: `“https://www.example.com/image2,3.jpg","https://www.example.com/image2,4.jpg”` Note that content in the quoted values is treated as a single value. Learn more about [Quoted attributes](https://support.google.com/merchants/answer/14998273).  |  
| **XML data sources**  | `<g:additional_image_link>https://www.example.com/image2.jpg </g:additional_image_link> <g:additional_image_link>https://www.example.com/image3.jpg </g:additional_image_link>`  |  
| **Merchant API**  | To format your data, check the [Merchant API](https://developers.google.com/merchant/api/reference/rest/products_v1/accounts.productInputs) resource.  |  
* * *
##  Minimum requirements
These are the requirements you'll need to meet to show your product. If you don't follow these requirements, we'll disapprove your product and let you know in your Merchant Center account.  
| ![Green checkmark](https://lh3.googleusercontent.com/spsYuH7xNamHqATrzSMngI8HjLrcTw7jcOnYcr618IeGqWCFV0ff3DsyDocValGfb3I=w48)  |  **Meet the requirements for the** [image link `[image_link]`](https://support.google.com/merchants/answer/6324350) attribute. The additional image can also: 
  * **Include product staging or show the product in use.**
  * **Highlight parts of the product** without showing the entire product.
  * **Show parts of a bundle** instead of showing all products in the bundle. When you submit a custom bundle of products, use the [bundle `[is_bundle]`](https://support.google.com/merchants/answer/6324449) attribute.
  * **Display the entire multipack.** When you submit a custom multipack of products, use the [multipack `[multipack]`](https://support.google.com/merchants/answer/6324488) attribute.

 |  
| --- | --- |  
| ![Green checkmark](https://lh3.googleusercontent.com/spsYuH7xNamHqATrzSMngI8HjLrcTw7jcOnYcr618IeGqWCFV0ff3DsyDocValGfb3I=w48)  |  All images created using generative AI must contain meta data indicating that the image was AI-generated (for example, the IPTC [`DigitalSourceType`](https://cv.iptc.org/newscodes/digitalsourcetype/)[`TrainedAlgorithmicMedia`](https://cv.iptc.org/newscodes/digitalsourcetype/trainedAlgorithmicMedia) metadata tag). Don't remove embedded metadata tags such as the IPTC `DigitalSourceType` property from images created using generative AI tools, for example [Product Studio](https://support.google.com/merchants/answer/13708167). The following IPTC NewsCodes specify the type of digital source that was used to create the image, and should be preserved:
  * [`TrainedAlgorithmicMedia`](https://cv.iptc.org/newscodes/digitalsourcetype/trainedAlgorithmicMedia): The image was created using a model derived from sampled content.
  * [`CompositeSynthetic`](https://cv.iptc.org/newscodes/digitalsourcetype/compositeSynthetic): The image is a composite that includes synthetic elements.
  * [`AlgorithmicMedia`](https://cv.iptc.org/newscodes/digitalsourcetype/algorithmicMedia): The image was created purely by an algorithm not based on any sampled training data (for example, an image created by software using a mathematical formula).

Learn more about [using AI content label settings and disclosures](https://support.google.com/merchants/answer/17231950).  |  
* * *
##  Best practices
These best practices can help you go beyond the basic requirements to optimize your product data for performance.
  * **Follow the best practices for the** [image link `[image_link]`](https://support.google.com/merchants/answer/6324350) attribute.  
For example, do not submit: 
    * Brand-only or logo images
    * Blurry or misshapen images
    * Images with a watermark, or text not relevant to the image such as trademark or store info
  * **Submit images that meet the size requirements.** If you include images that are under the minimum size requirements, your product won’t be disapproved, but your images won’t be shown.
  * **Use additional images to show the product from different angles or the product being used.** For example, if the main image shows product packaging, including images of the box contents in the additional images can help customers better understand what they are buying.
  * **Use lifestyle images.** Lifestyle images submitted with the [lifestyle image link `[lifestyle_image_link]`](https://support.google.com/merchants/answer/9103186) attribute are used to showcase your product in a real world context, for example, clothing worn by a model, furniture staged within a room, multiple products displayed as a complete set, or products shown with vivid background colors or presented in playful situations. Read more about [lifestyle images](https://support.google.com/merchants/answer/9103186).


**Note:** You can increase resolution, remove backgrounds, and generate a scene for your products using [Product Studio](https://support.google.com/merchants/answer/13708167) which is available for Merchant Center users and within the Google & YouTube app in Shopify.
* * *
##  Examples
### Product with one additional image  
| **Attribute**  | **Value**  | **Additional product information**  |  
| --- | --- | --- |  
| Image link `[image_link]`  | https://example.com/image1.jpg  | Only the couch on a white background  |  
| Additional image link `[additional_image_link]`  | https://example.com/image2.jpg  | The couch with two pillows and a living room setting  |  
### Product with three additional images  
| **Attribute**  | **Value**  | **Additional product information**  |  
| --- | --- | --- |  
| Image link `[image_link]`  | https://example.com/ring1.jpg  | Only the ring on a white background  |  
| Additional image link `[additional_image_link]`  | https://example.com/ring2.jpg  | Only the ring on a white background from a different angle  |  
| Additional image link `[additional_image_link]`  | https://example.com/ring3.jpg  | The ring on a model wearing a matching outfit  |  
| Additional image link `[additional_image_link]`  | https://example.com/ring4.jpg  | The ring inside its gift box packaging  |  
![An example showing how additional images can appear alongside the main image](https://storage.googleapis.com/support-kms-prod/42julhL8ZhvlveRAfNm1lR60Bmapa7R9KwKS)  
| **Attribute**  | **Value**  | **Additional product information**  |  
| --- | --- | --- |  
| Image link `[image_link]`  | https://example.com/image1.jpg  | Only the pie pan on a white background  |  
| Additional image link `[additional_image_link]`  | https://example.com/image2.jpg  | The end product - a slice of pie on a plate  |  
| Additional image link `[additional_image_link]`  | https://example.com/image3.jpg  | The baker holding the finished pie in the pan  |  
| Additional image link `[additional_image_link]`  | https://example.com/image4.jpg  | The pie pan in close up showing the finished pie  |  
### Bundle  
| **Attribute**  | **Value**  | **Additional product information**  |  
| --- | --- | --- |  
| Bundle `[is_bundle]`  | `yes`  |   |  
| Image link `[image_link]`  | https://example.com/camerabundle1.jpg  | All products in the bundle on a white background  |  
| Additional image link `[additional_image_link]`  | https://example.com/camerabundle2.jpg  | Only the camera body on a white background  |  
### Multipack  
| **Attribute**  | **Value**  | **Additional product information**  |  
| --- | --- | --- |  
| Multipack `[multipack]`  | 3  |   |  
| Image link `[image_link]`  | https://example.com/soap1.jpg  | Only one bar of soap on a white background  |  
| Additional image link `[additional_image_link]`  | https://example.com/soap2.jpg  | Three bars of soap on a white background  |  
Give feedback about this article
Choose a section to give feedback on
## Was this helpful?
How can we improve it?
Submit
## Need more help?
### Try these next steps:
[ Post to the help community  Get answers from community members  ](https://support.google.com/merchants/community?hl=en&help_center_link=CJKBggMSLUFkZGl0aW9uYWwgaW1hZ2UgbGluayBbYWRkaXRpb25hbF9pbWFnZV9saW5rXQ) [ Contact us Tell us more and we’ll help you get there ](https://support.google.com/merchants/gethelp)
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


16274312260506444333
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
  * Community](https://support.google.com/merchants/community?hl=en&help_center_link=CJKBggMSLUFkZGl0aW9uYWwgaW1hZ2UgbGluayBbYWRkaXRpb25hbF9pbWFnZV9saW5rXQ)[
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
By continuing, you agree Google uses your answers, [account & system info](https://support.google.com/merchants/answer/6324370?hl=en) to improve services, per our [Privacy](https://myaccount.google.com/privacypolicy?hl=en) & [Terms](https://policies.google.com/terms?hl=en).
true
false
false
Search
Clear search
Close search
Main menu
Google apps

