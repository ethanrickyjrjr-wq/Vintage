[Skip to main content](https://support.google.com/merchants/answer/6324350?hl=en#hcfe-content)
[](https://support.google.com/?tab=uu)
[](https://support.google.com/?tab=uu)
[Google Merchant Center Help](https://support.google.com/merchants)
[](https://www.google.com/intl/en/about/products?tab=uh)
[Sign in](https://accounts.google.com/ServiceLogin?hl=en&passive=true&continue=http://support.google.com/merchants/answer/6324350%3Fhl%3Den&ec=GAZAdQ)
Send feedback on...
This help content & information
General Help Center experience
CloseNext
  * [Help Center](https://support.google.com/merchants/?hl=en)
  * [Community](https://support.google.com/merchants/community?hl=en&help_center_link=CP6AggMSF0ltYWdlIGxpbmsgW2ltYWdlX2xpbmtd)
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


# Image link [image_link]
Use the image link `[image_link]` attribute to add the primary image for your product. Your main image is the first thing potential customers see across Google channels. A high-quality image grabs shoppers' attention, builds trust, and helps your products stand out.
**Important: We recently announced new image size requirements of at least 500 x 500 pixels for all products beginning January 31, 2027**. However, to ensure best performance in all listing formats, we recommend that you provide images 1500x1500 pixels or above.
## Image best practices
[Google Merchant Center image guidelines: Requirements and best practices](https://www.youtube.com/watch?v=UkuQk-0DPsU)
To view subtitles in your language, [turn on YouTube captions](https://support.google.com/youtube/answer/100078). Select the **Settings** icon ![Image of YouTube settings icon](https://storage.googleapis.com/support-kms-prod/UrHzzlx74G5ig5vYXo9Nk43r7NM5fj72Tbu1) at the top right corner of the video player, select **Captions** , and then specify your language.
* * *
**On this page**
  * [When to use](https://support.google.com/merchants/answer/6324350?hl=en#Whentouse)
  * [Format](https://support.google.com/merchants/answer/6324350?hl=en#Format)
  * [Image requirements](https://support.google.com/merchants/answer/6324350?hl=en#Image_requirements)
  * [AI image metadata](https://support.google.com/merchants/answer/6324350?hl=en#AI_image_metadata)
  * [Best practices](https://support.google.com/merchants/answer/6324350?hl=en#Image_guidelines_best_practices)
  * [Helpful tips](https://support.google.com/merchants/answer/6324350?hl=en#Helpful_tips)


* * *
##  When to use
![Required](https://storage.googleapis.com/support-kms-prod/ncoEh9hPBwKEuXOUKRffUwCyLKZVt7PeCt6w) **Required** for each product
Use the `[image_link]` attribute for your main product image, and submit any alternative angles or detailed shots using the [additional_image_link `[additional_image_link]`](https://support.google.com/merchants/answer/6324370) attribute. If you have an in-context or lifestyle representation of the product, you can also include its URL in the [lifestyle representation `[lifestyle_image_link]`](https://support.google.com/merchants/answer/9103186) attribute.
* * *
##  Format
Follow these formatting guidelines to make sure Google understands the data you're submitting. Learn [when and how to submit your product data](https://support.google.com/merchants/answer/10668075).  
| **Formatting specifications**  |  
| --- |  
| **Technical name**  | `image_link`  |  
| **Type**  | URL (including `http` or `https`), ASCII characters only, and RFC 3986 compliant  |  
| **Limits**  | 1–2,000 characters  |  
| **Supported file formats**  |  JPEG (.jpg/.jpeg), WebP (.webp), PNG (.png), GIF (.gif), BMP (.bmp), and TIFF (.tif/.tiff) The image's file extension should correspond to its format. Ensure your image links point to valid images in one of these supported formats. Using incorrect file extensions (for example .jpg for a .png file) can lead to 'Unsupported image type' errors. If images are synced from third-party platforms, verify they generate correct image URLs and formats.  |  
| Size  | 
  * At least 500 x 500 pixels 
    * When possible, we recommend that you provide images around 1500x1500 pixels or above to ensure best performance in all listing formats.
  * No image larger than 64 megapixels
  * No image file larger than 16MB

 |  
| **Repeated field**  | No  |  
| **Schema.org property ([What’s this?](https://support.google.com/merchants/answer/6069143))**  |  `[Product.image](https://schema.org/image)`, Type: `URL`  |  
### URL guidelines
#### URL encoding and crawl access
  * **URL Encoding** : Replace symbols and spaces in your URL with standard URL-encoded entities. For example, replace an ampersand (`&`) with `%26`, and a comma (`,`) with `%2C`.
  * **Crawlability** : Ensure your `robots.txt` file allows access to both **Googlebot** and **Googlebot-image** so Google can fetch your images. 
    * Example setup: `User-agent: Googlebot` followed by `Allow: /` and `User-agent: Googlebot-image` followed by `Allow: /`.
    * Note that it may take 24-48 hours after updating `robots.txt` for changes to take effect.


#### Best practices and optimization
  * **Use stable URLs** : Avoid dynamic parameters (for example, timestamps or session IDs) that change on every feed submission. Static URLs prevent unnecessary recrawling and server load.
  * **Enable automatic image improvements** : Turn on automatic improvements in Merchant Center to allow Google to automatically fix minor image policy issues (like promotional overlays) and avoid disapprovals.


### File format examples
To ensure your attribute is recognized correctly, use the formatting specific to your data source type:  
| Data Source Format  | Example Entry  |  
| --- | --- |  
| Text (TSV or CSV)  | `https://www.example.com/image1.jpg`  |  
| XML feeds  | `<g:image_link>https://www.example.com/image1.jpg</g:image_link>`  |  
| Merchant API  | To format your data, check the [Merchant API](https://developers.google.com/merchant/api/reference/rest/products_v1/accounts.productInputs) resource.  |  
* * *
##  Image requirements
To prevent your product from being disapproved, ensure your image avoids the violations listed below. If your image doesn't meet these requirements, it won't appear on Google surfaces, and you'll see a notification in the Diagnostics section of your Merchant Center account.
### Avoid image disapprovals
  * ****Don’t use an image that contains promotional elements or overlays****
    * **Your product image must offer an unobstructed, clean view of the item for sale**. Adding post-production text, marketing callouts, or graphics distracts shoppers from your product and will cause an image disapproval. Keep your main image focused solely on the product itself. 
      * What to avoid: 
        * **Calls to action** : Text prompting action, such as "Buy", "Shop now", or "Order today".
        * **Price and shipping details** : Mentions of price, discounts, or offers like "Free shipping".
        * **Service-related information** : Extended service or warranty claims, such as "Includes 2-year warranty".
        * **Promotional adjectives** : Subjective marketing words, such as "Best", "Cheap", or "Top quality".
        * **Condition or compatibility text** : Added labels describing state or fit, such as "New", "2-piece set", or "Adaptable".
        * **Barcodes and tracking codes** : UPC barcodes, QR codes, or serial tags overlaid on the photo.
        * **Overlays and watermarks** : Stock photo watermarks, copyright symbols, or graphic stamps.
        * **Added brand, manufacturer, or retailer names and logos** : Superimposed logos or store names added in post-production (allowed only if they are an inherent, physical part of the product itself).
  * ****Don’t use a placeholder, generic image, or graphic that doesn't show your product****
    * **Your primary image must clearly display the exact item being sold**. Placeholders and generic visuals prevent shoppers from seeing what they are buying, which leads to image disapprovals. 
      * What to avoid: 
        * **Temporary or text-based placeholders:** Don't submit graphics with text such as "Coming soon", "No image available", or "Photo pending".
        * **Store logos and icons:** Don't use your company logo, brand watermark, or stock icons as a substitute for a product photo.
        * **Placeholders:** Don't use shared stand-in images or reuse one general photo across multiple distinct products where unique, individual images are required.
        * **Generic graphics and illustrations:** Don't submit line art, mockups, or illustrations that don't depict the physical product.
  * **Don't use a single-color image that is only a square of color.**
  * **Don't use an image with a border**. To ensure that your image works with a variety of design elements, don’t include borders around your image.
  * **Don't include any product that's not sold together with the main product**.


### Image categories that allow variations on the requirements above
  * **Exception** : A generic image, graphic, or illustration is allowed for a product in these categories: 
    * `Hardware` (ID: `632`)
    * `Vehicles & Parts` (ID: `888`)
    * `Software > Computer Software` (ID: `313`)


  * **Exception** : Software logos or icons can represent your software product in this product category: 
    * `Software > Computer Software` (ID: `313`)


  * **Exception** : A single-color image is allowed for a product in these Google product categories: 
    * `Vehicle Paint` (ID: `3812`)
    * `Craft Paint, Ink & Glaze` (ID: `505378`)
    * `Painting Consumables` (ID: `503740`)


* * *
##  AI image metadata
All images created using generative AI must contain meta data indicating that the image was AI-generated (for example, the IPTC [DigitalSourceTypeTrainedAlgorithmicMedia](https://cv.iptc.org/newscodes/digitalsourcetype/trainedAlgorithmicMedia) metadata tag). Don't remove embedded metadata tags such as the IPTC DigitalSourceType property from images created using generative AI tools, for example [Product Studio](https://support.google.com/merchants/answer/13708167). The following IPTC NewsCodes specify the type of digital source that was used to create the image, and should be preserved:
  * [TrainedAlgorithmicMedia](https://cv.iptc.org/newscodes/digitalsourcetype/trainedAlgorithmicMedia): The image was created using a model derived from sampled content.
  * [CompositeSynthetic](https://cv.iptc.org/newscodes/digitalsourcetype/compositeSynthetic): The image is a composite that includes synthetic elements.
  * [AlgorithmicMedia](https://cv.iptc.org/newscodes/digitalsourcetype/algorithmicMedia): The image was created purely by an algorithm not based on any sampled training data (for example, an image created by software using a mathematical formula).


**Note** : If you're planning to upload an image of a product in its original packaging, make sure that the image clearly displays multidimensional product packaging and not just the front of the packaging.
* * *
##  Best practices
These are the best practices that can help you go beyond the basic requirements to optimize your product data performance.  
| ![Green checkmark](https://lh3.googleusercontent.com/spsYuH7xNamHqATrzSMngI8HjLrcTw7jcOnYcr618IeGqWCFV0ff3DsyDocValGfb3I=w48)  |  **Use an image that shows a clear view of the main product being sold**. And meet all size requirements
  * At least 500x500 pixels 
    * When possible, we recommend that you provide images around 1500x1500 pixels or above to ensure best performance in all listing formats.
  * No image larger than 64 megapixels
  * No image file larger than 16MB

Any additional views of the product can be submitted with the [additional image link `[additional_image_link]`](https://support.google.com/merchants/answer/6324370) attribute.  |  
| --- | --- |  
![An example showing how additional images can appear alongside the main image](https://storage.googleapis.com/support-kms-prod/42julhL8ZhvlveRAfNm1lR60Bmapa7R9KwKS)  
| ![Green checkmark](https://lh3.googleusercontent.com/spsYuH7xNamHqATrzSMngI8HjLrcTw7jcOnYcr618IeGqWCFV0ff3DsyDocValGfb3I=w48)  |  **Submit a unique image that represents the distinguishing details of each variant** When selling products that come in multiple options, submit a distinct, dedicated image for every individual variant. Shoppers expect the image they see in ads and free listings to accurately reflect the exact version, color, and finish they are selecting. Key guidelines for variant imagery:
  * **Submit a unique image for each variant:** Don’t reuse one general photo across different product variations. Provide a separate, dedicated image for every SKU that highlights its specific features.
  * **Show the correct variant:** Match the image directly to the product option being sold. Ensure the photo accurately reflects the exact color, pattern, finish, and material.
  * **Show only one variant per image:** For products with multiple colors or styles, display only the single variant being sold in that listing. Avoid group photos that showcase multiple colorways together.
  * **Accurately represent customized products:** If you are selling a customized or personalized item, use an image that shows the customization. Do not use an uncustomized product photo for a customized listing, and vice versa. Learn more about [best practices for customized products](https://support.google.com/merchants/answer/7162856).![An example of an image in the product data that doesn't match what's on the landing page](https://lh3.googleusercontent.com/qJM6Nwtv-1h6UC2NMEAF-UDX0fiihav6kmERv7hhvU2dzNoVlpyA-LUp3Pst-l_SpEM=w895)

 |  
| --- | --- |  
| ![Green checkmark](https://lh3.googleusercontent.com/spsYuH7xNamHqATrzSMngI8HjLrcTw7jcOnYcr618IeGqWCFV0ff3DsyDocValGfb3I=w48)  |  **Frame your product in the image space** so that it takes up no less than 75%, but not more than 90%, of the full image.
  * Any additional views of the product showing highlighted areas can be submitted with the [additional image link `[additional_image_link]`](https://support.google.com/merchants/answer/6324370) attribute.

 |  
| --- | --- |  
![An example of an ad with an image that's too small](https://storage.googleapis.com/support-kms-prod/z8OTctobUQX1csqKVfprqN86DvstWpZ9wHtW)
**Note** : If you're planning to upload an image of a product in its original packaging, make sure that the image clearly displays multidimensional product packaging and not just the front of the packaging.
* * *
##  Helpful tips
  * Enhance your images with Product Studio: You can increase resolution, remove backgrounds, and generate custom scenes using [Product Studio](https://support.google.com/merchants/answer/13708167), available in Merchant Center and the Google & YouTube app on Shopify.
  * Keep in mind that images may be automatically cropped: Google may test subtle cropping on your image to better frame the item and highlight key product details for shoppers.


Give feedback about this article
Choose a section to give feedback on
## Was this helpful?
How can we improve it?
Submit
## Need more help?
### Try these next steps:
[ Post to the help community  Get answers from community members  ](https://support.google.com/merchants/community?hl=en&help_center_link=CP6AggMSF0ltYWdlIGxpbmsgW2ltYWdlX2xpbmtd) [ Contact us Tell us more and we’ll help you get there ](https://support.google.com/merchants/gethelp)
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
4723020511515895807
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
  * Community](https://support.google.com/merchants/community?hl=en&help_center_link=CP6AggMSF0ltYWdlIGxpbmsgW2ltYWdlX2xpbmtd)[
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
By continuing, you agree Google uses your answers, [account & system info](https://support.google.com/merchants/answer/6324350?hl=en) to improve services, per our [Privacy](https://myaccount.google.com/privacypolicy?hl=en) & [Terms](https://policies.google.com/terms?hl=en).
true
false
false

