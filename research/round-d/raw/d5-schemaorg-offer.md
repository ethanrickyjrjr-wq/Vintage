**Note** : You are viewing the development version of [Schema.org](https://schema.org). See [how we work](https://schema.org/docs/howwework.html) for more details. 
[Schema.org](https://schema.org/)
  * [Docs](https://schema.org/docs/documents.html)
  * [Schemas](https://schema.org/docs/schemas.html)
  * [Validate](https://validator.schema.org)
  * [About](https://schema.org/docs/about.html)


[ ](javascript:void\(0\);)
# Offer
A Schema.org Type
Usage: [ 10M+ Domains Based on monthly aggregations from Google's web index. ](https://schema.org/docs/usage_stats.html) (Google - August 2026) 
[Thing](https://schema.org/Thing "Thing") > [Intangible](https://schema.org/Intangible "Intangible") > [Offer](https://schema.org/Offer "Offer")   

**[more...]**
  * Canonical URL: https://schema.org/Offer
  * Equivalent Class: fibo-fnd-pas-pas:Offer   
Equivalent Class: unece:Offer 
  * [Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+Offer)


An offer to transfer some rights to an item or to provide a service — for example, an offer to sell tickets to an event, to rent the DVD of a movie, to stream a TV show over the internet, to repair a motorcycle, or to loan a book.  
  
Note: As the [businessFunction](https://schema.org/businessFunction) property, which identifies the form of offer (e.g. sell, lease, repair, dispose), defaults to http://purl.org/goodrelations/v1#Sell; an Offer without a defined businessFunction value can be assumed to be an offer to sell.  
  
For [GTIN](http://www.gs1.org/barcodes/technical/idkeys/gtin)-related fields, see [Check Digit calculator](http://www.gs1.org/barcodes/support/check_digit_calculator) and [validation guide](http://www.gs1us.org/resources/standards/gtin-validation-guide) from [GS1](http://www.gs1.org/).  
| Property  | Expected Type  | Description  |  
| --- | --- | --- |  
| Properties from [Offer](https://schema.org/Offer "Offer")  |  
| `               acceptedPaymentMethod[](https://schema.org/acceptedPaymentMethod "acceptedPaymentMethod")`  |  [LoanOrCredit](https://schema.org/LoanOrCredit "LoanOrCredit") or   
[PaymentMethod](https://schema.org/PaymentMethod "PaymentMethod") or   
[Text](https://schema.org/Text "Text")  | The payment method(s) that are accepted in general by an organization, or for some specific demand or offer.   |  
| `               addOn[](https://schema.org/addOn "addOn")`  |  [Offer](https://schema.org/Offer "Offer")  | An additional offer that can only be obtained in combination with the first base offer (e.g. supplements and extensions that are available for a surcharge).   |  
| `               additionalProperty[](https://schema.org/additionalProperty "additionalProperty")`  |  [PropertyValue](https://schema.org/PropertyValue "PropertyValue")  | A property-value pair representing an additional characteristic of the entity, e.g. a product feature or another characteristic for which there is no matching property in schema.org.  
  
Note: Publishers should be aware that applications designed to use specific schema.org properties (e.g. https://schema.org/width, https://schema.org/color, https://schema.org/gtin13, ...) will typically expect such data to be provided using those properties, rather than using the generic property/value mechanism.   |  
| `               advanceBookingRequirement[](https://schema.org/advanceBookingRequirement "advanceBookingRequirement")`  |  [QuantitativeValue](https://schema.org/QuantitativeValue "QuantitativeValue")  | The amount of time that is required between accepting the offer and the actual usage of the resource or service.   |  
| `               aggregateRating[](https://schema.org/aggregateRating "aggregateRating")`  |  [AggregateRating](https://schema.org/AggregateRating "AggregateRating")  | The overall rating, based on a collection of reviews or ratings, of the item.   |  
| `               areaServed[](https://schema.org/areaServed "areaServed")`  |  [AdministrativeArea](https://schema.org/AdministrativeArea "AdministrativeArea") or   
[GeoShape](https://schema.org/GeoShape "GeoShape") or   
[Place](https://schema.org/Place "Place") or   
[Text](https://schema.org/Text "Text")  | The geographic area where a service or offered item is provided. Supersedes [serviceArea](https://schema.org/serviceArea "serviceArea").   |  
| `               asin[](https://schema.org/asin "asin")`  |  [Text](https://schema.org/Text "Text") or   
[URL](https://schema.org/URL "URL")  | An Amazon Standard Identification Number (ASIN) is a 10-character alphanumeric unique identifier assigned by Amazon.com and its partners for product identification within the Amazon organization (summary from [Wikipedia](https://en.wikipedia.org/wiki/Amazon_Standard_Identification_Number)'s article).  
  
Note also that this is a definition for how to include ASINs in Schema.org data, and not a definition of ASINs in general - see documentation from Amazon for authoritative details. ASINs are most commonly encoded as text strings, but the [asin] property supports URL/URI as potential values too.   |  
| `               availability[](https://schema.org/availability "availability")`  |  [ItemAvailability](https://schema.org/ItemAvailability "ItemAvailability")  | The availability of this item—for example In stock, Out of stock, Pre-order, etc.   |  
| `               availabilityEnds[](https://schema.org/availabilityEnds "availabilityEnds")`  |  [Date](https://schema.org/Date "Date") or   
[DateTime](https://schema.org/DateTime "DateTime") or   
[Time](https://schema.org/Time "Time")  | The end of the availability of the product or service included in the offer.   |  
| `               availabilityStarts[](https://schema.org/availabilityStarts "availabilityStarts")`  |  [Date](https://schema.org/Date "Date") or   
[DateTime](https://schema.org/DateTime "DateTime") or   
[Time](https://schema.org/Time "Time")  | The beginning of the availability of the product or service included in the offer.   |  
| `               availableAtOrFrom[](https://schema.org/availableAtOrFrom "availableAtOrFrom")`  |  [Place](https://schema.org/Place "Place")  | The place(s) from which the offer can be obtained (e.g. store locations).   |  
| `               availableDeliveryMethod[](https://schema.org/availableDeliveryMethod "availableDeliveryMethod")`  |  [DeliveryMethod](https://schema.org/DeliveryMethod "DeliveryMethod")  | The delivery method(s) available for this offer.   |  
| `               businessFunction[](https://schema.org/businessFunction "businessFunction")`  |  [BusinessFunction](https://schema.org/BusinessFunction "BusinessFunction")  | The business function (e.g. sell, lease, repair, dispose) of the offer or component of a bundle (TypeAndQuantityNode). The default is http://purl.org/goodrelations/v1#Sell.   |  
| `               category[](https://schema.org/category "category")`  |  [CategoryCode](https://schema.org/CategoryCode "CategoryCode") or   
[PhysicalActivityCategory](https://schema.org/PhysicalActivityCategory "PhysicalActivityCategory") or   
[Text](https://schema.org/Text "Text") or   
[Thing](https://schema.org/Thing "Thing") or   
[URL](https://schema.org/URL "URL")  | A category for the item. Greater signs or slashes can be used to informally indicate a category hierarchy.   |  
| `               checkoutPageURLTemplate[](https://schema.org/checkoutPageURLTemplate "checkoutPageURLTemplate")`  |  [Text](https://schema.org/Text "Text")  | A URL template (RFC 6570) for a checkout page for an offer. This approach allows merchants to specify a URL for online checkout of the offered product, by interpolating parameters such as the logged in user ID, product ID, quantity, discount code etc. Parameter naming and standardization are not specified here.   |  
| `               deliveryLeadTime[](https://schema.org/deliveryLeadTime "deliveryLeadTime")`  |  [QuantitativeValue](https://schema.org/QuantitativeValue "QuantitativeValue")  | The typical delay between the receipt of the order and the goods either leaving the warehouse or being prepared for pickup, in case the delivery method is on site pickup.   |  
| `               eligibleCustomerType[](https://schema.org/eligibleCustomerType "eligibleCustomerType")`  |  [BusinessEntityType](https://schema.org/BusinessEntityType "BusinessEntityType")  | The type(s) of customers for which the given offer is valid.   |  
| `               eligibleDuration[](https://schema.org/eligibleDuration "eligibleDuration")`  |  [QuantitativeValue](https://schema.org/QuantitativeValue "QuantitativeValue")  | The duration for which the given offer is valid.   |  
| `               eligibleQuantity[](https://schema.org/eligibleQuantity "eligibleQuantity")`  |  [QuantitativeValue](https://schema.org/QuantitativeValue "QuantitativeValue")  | The interval and unit of measurement of ordering quantities for which the offer or price specification is valid. This allows e.g. specifying that a certain freight charge is valid only for a certain quantity.   |  
| `               eligibleRegion[](https://schema.org/eligibleRegion "eligibleRegion")`  |  [GeoShape](https://schema.org/GeoShape "GeoShape") or   
[Place](https://schema.org/Place "Place") or   
[Text](https://schema.org/Text "Text")  | The ISO 3166-1 (ISO 3166-1 alpha-2) or ISO 3166-2 code, the place, or the GeoShape for the geo-political region(s) for which the offer or delivery charge specification is valid.  
  
See also [ineligibleRegion](https://schema.org/ineligibleRegion).   |  
| `               eligibleTransactionVolume[](https://schema.org/eligibleTransactionVolume "eligibleTransactionVolume")`  |  [PriceSpecification](https://schema.org/PriceSpecification "PriceSpecification")  | The transaction volume, in a monetary unit, for which the offer or price specification is valid, e.g. for indicating a minimal purchasing volume, to express free shipping above a certain order volume, or to limit the acceptance of credit cards to purchases to a certain minimal amount.   |  
| `               gtin[](https://schema.org/gtin "gtin")`  |  [Text](https://schema.org/Text "Text") or   
[URL](https://schema.org/URL "URL")  | A Global Trade Item Number ([GTIN](https://www.gs1.org/standards/id-keys/gtin)). GTINs identify trade items, including products and services, using numeric identification codes.  
  
A correct [gtin](https://schema.org/gtin) value should be a valid GTIN, which means that it should be an all-numeric string of either 8, 12, 13 or 14 digits, or a "GS1 Digital Link" URL based on such a string. The numeric component should also have a [valid GS1 check digit](https://www.gs1.org/services/check-digit-calculator) and meet the other rules for valid GTINs. See also [GS1's GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin) and [Wikipedia](https://en.wikipedia.org/wiki/Global_Trade_Item_Number) for more details. Left-padding of the gtin values is not required or encouraged. The [gtin](https://schema.org/gtin) property generalizes the earlier [gtin8](https://schema.org/gtin8), [gtin12](https://schema.org/gtin12), [gtin13](https://schema.org/gtin13), and [gtin14](https://schema.org/gtin14) properties.  
  
The GS1 [digital link specifications](https://www.gs1.org/standards/Digital-Link/) expresses GTINs as URLs (URIs, IRIs, etc.). Digital Links should be populated into the [hasGS1DigitalLink](https://schema.org/hasGS1DigitalLink) attribute.  
  
Note also that this is a definition for how to include GTINs in Schema.org data, and not a definition of GTINs in general - see the GS1 documentation for authoritative details.   |  
| `               gtin12[](https://schema.org/gtin12 "gtin12")`  |  [Text](https://schema.org/Text "Text")  | The GTIN-12 code of the product, or the product to which the offer refers. The GTIN-12 is the 12-digit GS1 Identification Key composed of a U.P.C. Company Prefix, Item Reference, and Check Digit used to identify trade items. See [GS1 GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin) for more details.   |  
| `               gtin13[](https://schema.org/gtin13 "gtin13")`  |  [Text](https://schema.org/Text "Text")  | The GTIN-13 code of the product, or the product to which the offer refers. This is equivalent to 13-digit ISBN codes and EAN UCC-13. Former 12-digit UPC codes can be converted into a GTIN-13 code by simply adding a preceding zero. See [GS1 GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin) for more details.   |  
| `               gtin14[](https://schema.org/gtin14 "gtin14")`  |  [Text](https://schema.org/Text "Text")  | The GTIN-14 code of the product, or the product to which the offer refers. See [GS1 GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin) for more details.   |  
| `               gtin8[](https://schema.org/gtin8 "gtin8")`  |  [Text](https://schema.org/Text "Text")  | The GTIN-8 code of the product, or the product to which the offer refers. This code is also known as EAN/UCC-8 or 8-digit EAN. See [GS1 GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin) for more details.   |  
| `               hasAdultConsideration[](https://schema.org/hasAdultConsideration "hasAdultConsideration")`  |  [AdultOrientedEnumeration](https://schema.org/AdultOrientedEnumeration "AdultOrientedEnumeration")  | Used to tag an item to be intended or suitable for consumption or use by adults only.   |  
| `               hasDigitalProductPassport[](https://schema.org/hasDigitalProductPassport "hasDigitalProductPassport")`  |  [DigitalProductPassport](https://schema.org/DigitalProductPassport "DigitalProductPassport") or   
[URL](https://schema.org/URL "URL")  | A link to a Digital Product Passport (DPP) or a digital record detailing the lifecycle, sustainability, and compliance data for this product or offer. This may be a direct URL, a GS1 Digital Link URI, or a nested DigitalProductPassport object. Note: This property is aligned with the IANA 'dpp' link relation and the GS1 Web Vocabulary 'dpp' link type.   |  
| `               hasGS1DigitalLink[](https://schema.org/hasGS1DigitalLink "hasGS1DigitalLink")`  |  [URL](https://schema.org/URL "URL")  | The [GS1 digital link](https://www.gs1.org/standards/gs1-digital-link) associated with the object. This URL should conform to the particular requirements of digital links. The link should only contain the Application Identifiers (AIs) that are relevant for the entity being annotated, for instance a [Product](https://schema.org/Product) or an [Organization](https://schema.org/Organization), and for the correct granularity. In particular, for products:
  * A Digital Link that contains a serial number (AI `21`) should only be present on instances of [IndividualProduct](https://schema.org/IndividualProduct)
  * A Digital Link that contains a lot number (AI `10`) should be annotated as [SomeProducts](https://schema.org/SomeProducts) if only products from that lot are sold, or [IndividualProduct](https://schema.org/IndividualProduct) if there is only a specific product.
  * A Digital Link that contains a global model number (AI `8013`) should be attached to a [Product](https://schema.org/Product) or a [ProductModel](https://schema.org/ProductModel).

Other item types should be adapted similarly.   |  
| `               hasMeasurement[](https://schema.org/hasMeasurement "hasMeasurement")`  |  [QuantitativeValue](https://schema.org/QuantitativeValue "QuantitativeValue")  | A measurement of an item, For example, the inseam of pants, the wheel size of a bicycle, the gauge of a screw, or the carbon footprint measured for certification by an authority. Usually an exact measurement, but can also be a range of measurements for adjustable products, for example belts and ski bindings.   |  
| `               hasMerchantReturnPolicy[](https://schema.org/hasMerchantReturnPolicy "hasMerchantReturnPolicy")`  |  [MerchantReturnPolicy](https://schema.org/MerchantReturnPolicy "MerchantReturnPolicy")  | Specifies a MerchantReturnPolicy that may be applicable. Supersedes [hasProductReturnPolicy](https://schema.org/hasProductReturnPolicy "hasProductReturnPolicy").   |  
| `               includesObject[](https://schema.org/includesObject "includesObject")`  |  [TypeAndQuantityNode](https://schema.org/TypeAndQuantityNode "TypeAndQuantityNode")  | This links to a node or nodes indicating the exact quantity of the products included in an [Offer](https://schema.org/Offer) or [ProductCollection](https://schema.org/ProductCollection).   |  
| `               ineligibleRegion[](https://schema.org/ineligibleRegion "ineligibleRegion")`  |  [GeoShape](https://schema.org/GeoShape "GeoShape") or   
[Place](https://schema.org/Place "Place") or   
[Text](https://schema.org/Text "Text")  | The ISO 3166-1 (ISO 3166-1 alpha-2) or ISO 3166-2 code, the place, or the GeoShape for the geo-political region(s) for which the offer or delivery charge specification is not valid, e.g. a region where the transaction is not allowed.  
  
See also [eligibleRegion](https://schema.org/eligibleRegion).   |  
| `               inventoryLevel[](https://schema.org/inventoryLevel "inventoryLevel")`  |  [QuantitativeValue](https://schema.org/QuantitativeValue "QuantitativeValue")  | The current approximate inventory level for the item or items.   |  
| `               isFamilyFriendly[](https://schema.org/isFamilyFriendly "isFamilyFriendly")`  |  [Boolean](https://schema.org/Boolean "Boolean")  | Indicates whether this content is family friendly.   |  
| `               itemCondition[](https://schema.org/itemCondition "itemCondition")`  |  [OfferItemCondition](https://schema.org/OfferItemCondition "OfferItemCondition")  | A predefined value from OfferItemCondition specifying the condition of the product or service, or the products or services included in the offer. Also used for product return policies to specify the condition of products accepted for returns.   |  
| `               itemOffered[](https://schema.org/itemOffered "itemOffered")`  |  [AggregateOffer](https://schema.org/AggregateOffer "AggregateOffer") or   
[CreativeWork](https://schema.org/CreativeWork "CreativeWork") or   
[Event](https://schema.org/Event "Event") or   
[MenuItem](https://schema.org/MenuItem "MenuItem") or   
[Product](https://schema.org/Product "Product") or   
[Service](https://schema.org/Service "Service") or   
[Trip](https://schema.org/Trip "Trip")  | An item being offered (or demanded). The transactional nature of the offer or demand is documented using [businessFunction](https://schema.org/businessFunction), e.g. sell, lease etc. While several common expected types are listed explicitly in this definition, others can be used. Using a second type, such as Product or a subtype of Product, can clarify the nature of the offer.   
Inverse property: [offers](https://schema.org/offers "offers")  |  
| `               itemPopularity[](https://schema.org/itemPopularity "itemPopularity")`  |  [Number](https://schema.org/Number "Number") or   
[QuantitativeValue](https://schema.org/QuantitativeValue "QuantitativeValue")  | A measure of the relative popularity or sales rank of the offer within a marketplace, catalog, or platform (e.g. a platform-specific bestseller ranking or sales rank). This property is intended for platform-level or catalog-wide comparative rankings rather than self-asserted promotional claims.   |  
| `               leaseLength[](https://schema.org/leaseLength "leaseLength")`  |  [Duration](https://schema.org/Duration "Duration") or   
[QuantitativeValue](https://schema.org/QuantitativeValue "QuantitativeValue")  | Length of the lease for some [Accommodation](https://schema.org/Accommodation), either particular to some [Offer](https://schema.org/Offer) or in some cases intrinsic to the property.   |  
| `               mobileUrl[](https://schema.org/mobileUrl "mobileUrl")`  |  [Text](https://schema.org/Text "Text")  | The [mobileUrl](https://schema.org/mobileUrl) property is provided for specific situations in which data consumers need to determine whether one of several provided URLs is a dedicated 'mobile site'.  
  
To discourage over-use, and reflecting intial usecases, the property is expected only on [Product](https://schema.org/Product) and [Offer](https://schema.org/Offer), rather than [Thing](https://schema.org/Thing). The general trend in web technology is towards [responsive design](https://en.wikipedia.org/wiki/Responsive_web_design) in which content can be flexibly adapted to a wide range of browsing environments. Pages and sites referenced with the long-established [url](https://schema.org/url) property should ideally also be usable on a wide variety of devices, including mobile phones. In most cases, it would be pointless and counter productive to attempt to update all [url](https://schema.org/url) markup to use [mobileUrl](https://schema.org/mobileUrl) for more mobile-oriented pages. The property is intended for the case when items (primarily [Product](https://schema.org/Product) and [Offer](https://schema.org/Offer)) have extra URLs hosted on an additional "mobile site" alongside the main one. It should not be taken as an endorsement of this publication style.   |  
| `               mpn[](https://schema.org/mpn "mpn")`  |  [Text](https://schema.org/Text "Text")  | The Manufacturer Part Number (MPN) of the product, or the product to which the offer refers.   |  
| `               offeredBy[](https://schema.org/offeredBy "offeredBy")`  |  [Organization](https://schema.org/Organization "Organization") or   
[Person](https://schema.org/Person "Person")  | A pointer to the organization or person making the offer.   
Inverse property: [makesOffer](https://schema.org/makesOffer "makesOffer")  |  
| `               price[](https://schema.org/price "price")`  |  [Number](https://schema.org/Number "Number") or   
[Text](https://schema.org/Text "Text")  | The offer price of a product, or of a price component when attached to PriceSpecification and its subtypes.  
  
Usage guidelines:  
  

  * Use the [priceCurrency](https://schema.org/priceCurrency) property (with standard formats: [ISO 4217 currency format](http://en.wikipedia.org/wiki/ISO_4217), e.g. "USD"; [Ticker symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies) for cryptocurrencies, e.g. "BTC"; well known names for [Local Exchange Trading Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system) (LETS) and other currency types, e.g. "Ithaca HOUR") instead of including [ambiguous symbols](http://en.wikipedia.org/wiki/Dollar_sign#Currencies_that_use_the_dollar_or_peso_sign) such as '$' in the value.
  * Use '.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to indicate a decimal point. Avoid using these symbols as a readability separator.
  * Note that both [RDFa](http://www.w3.org/TR/xhtml-rdfa-primer/#using-the-content-attribute) and Microdata syntax allow the use of a "content=" attribute for publishing simple machine-readable values alongside more human-friendly formatting.
  * Use values from 0123456789 (Unicode 'DIGIT ZERO' (U+0030) to 'DIGIT NINE' (U+0039)) rather than superficially similar Unicode symbols.

 |  
| `               priceCurrency[](https://schema.org/priceCurrency "priceCurrency")`  |  [Text](https://schema.org/Text "Text")  | The currency of the price, or a price component when attached to [PriceSpecification](https://schema.org/PriceSpecification) and its subtypes.  
  
Use standard formats: [ISO 4217 currency format](http://en.wikipedia.org/wiki/ISO_4217), e.g. "USD"; [Ticker symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies) for cryptocurrencies, e.g. "BTC"; well known names for [Local Exchange Trading Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system) (LETS) and other currency types, e.g. "Ithaca HOUR".   |  
| `               priceSpecification[](https://schema.org/priceSpecification "priceSpecification")`  |  [PriceSpecification](https://schema.org/PriceSpecification "PriceSpecification")  | One or more detailed price specifications, indicating the unit price and delivery or payment charges.   |  
| `               priceValidUntil[](https://schema.org/priceValidUntil "priceValidUntil")`  |  [Date](https://schema.org/Date "Date")  | The date after which the price is no longer available.   |  
| `               review[](https://schema.org/review "review")`  |  [Review](https://schema.org/Review "Review")  | A review of the item. Supersedes [reviews](https://schema.org/reviews "reviews").   |  
| `               seller[](https://schema.org/seller "seller")`  |  [Organization](https://schema.org/Organization "Organization") or   
[Person](https://schema.org/Person "Person")  | An entity which offers (sells / leases / lends / loans) the services / goods. A seller may also be a provider. Supersedes [merchant](https://schema.org/merchant "merchant"), [vendor](https://schema.org/vendor "vendor").   |  
| `               serialNumber[](https://schema.org/serialNumber "serialNumber")`  |  [Text](https://schema.org/Text "Text")  | The serial number or any alphanumeric identifier of a particular product. When attached to an offer, it is a shortcut for the serial number of the product included in the offer.   |  
| `               shippingDetails[](https://schema.org/shippingDetails "shippingDetails")`  |  [OfferShippingDetails](https://schema.org/OfferShippingDetails "OfferShippingDetails")  | Indicates information about the shipping policies and options associated with an [Offer](https://schema.org/Offer).   |  
| `               sku[](https://schema.org/sku "sku")`  |  [Text](https://schema.org/Text "Text")  | The Stock Keeping Unit (SKU), i.e. a merchant-specific identifier for a product or service, or the product to which the offer refers.   |  
| `               validForMemberTier[](https://schema.org/validForMemberTier "validForMemberTier")`  |  [MemberProgramTier](https://schema.org/MemberProgramTier "MemberProgramTier")  | The membership program tier(s) an Offer (or a PriceSpecification, OfferShippingDetails, or MerchantReturnPolicy under an Offer) is valid for.   |  
| `               validFrom[](https://schema.org/validFrom "validFrom")`  |  [Date](https://schema.org/Date "Date") or   
[DateTime](https://schema.org/DateTime "DateTime")  | The date when the item becomes valid.   |  
| `               validThrough[](https://schema.org/validThrough "validThrough")`  |  [Date](https://schema.org/Date "Date") or   
[DateTime](https://schema.org/DateTime "DateTime")  | The date after when the item is not valid. For example the end of an offer, salary period, or a period of opening hours.   |  
| `               warranty[](https://schema.org/warranty "warranty")`  |  [WarrantyPromise](https://schema.org/WarrantyPromise "WarrantyPromise")  | The warranty promise(s) included in the offer. Supersedes [warrantyPromise](https://schema.org/warrantyPromise "warrantyPromise").   |  
| Properties from [Thing](https://schema.org/Thing "Thing")  |  
| `               additionalType[](https://schema.org/additionalType "additionalType")`  |  [Text](https://schema.org/Text "Text") or   
[URL](https://schema.org/URL "URL")  | An additional type for the item, typically used for adding more specific types from external vocabularies in microdata syntax. This is a relationship between something and a class that the thing is in. Typically the value is a URI-identified RDF class, and in this case corresponds to the use of rdf:type in RDF. Text values can be used sparingly, for cases where useful information can be added without their being an appropriate schema to reference. In the case of text values, the class label should follow the schema.org [style guide](https://schema.org/docs/styleguide.html).   |  
| `               alternateName[](https://schema.org/alternateName "alternateName")`  |  [Text](https://schema.org/Text "Text")  | An alias for the item.   |  
| `               description[](https://schema.org/description "description")`  |  [Text](https://schema.org/Text "Text") or   
[TextObject](https://schema.org/TextObject "TextObject")  | A description of the item.   |  
| `               disambiguatingDescription[](https://schema.org/disambiguatingDescription "disambiguatingDescription")`  |  [Text](https://schema.org/Text "Text")  | A sub property of description. A short description of the item used to disambiguate from other, similar items. Information from other properties (in particular, name) may be necessary for the description to be useful for disambiguation.   |  
| `               identifier[](https://schema.org/identifier "identifier")`  |  [PropertyValue](https://schema.org/PropertyValue "PropertyValue") or   
[Text](https://schema.org/Text "Text") or   
[URL](https://schema.org/URL "URL")  | The identifier property represents any kind of identifier for any kind of [Thing](https://schema.org/Thing), such as ISBNs, GTIN codes, UUIDs etc. Schema.org provides dedicated properties for representing many of these, either as textual strings or as URL (URI) links. See [background notes](https://schema.org/docs/datamodel.html#identifierBg) for more details.   |  
| `               image[](https://schema.org/image "image")`  |  [ImageObject](https://schema.org/ImageObject "ImageObject") or   
[URL](https://schema.org/URL "URL")  | An image of the item. This can be a [URL](https://schema.org/URL) or a fully described [ImageObject](https://schema.org/ImageObject).   |  
| `               mainEntityOfPage[](https://schema.org/mainEntityOfPage "mainEntityOfPage")`  |  [CreativeWork](https://schema.org/CreativeWork "CreativeWork") or   
[URL](https://schema.org/URL "URL")  | Indicates a page (or other CreativeWork) for which this thing is the main entity being described. See [background notes](https://schema.org/docs/datamodel.html#mainEntityBackground) for details.   
Inverse property: [mainEntity](https://schema.org/mainEntity "mainEntity")  |  
| `               name[](https://schema.org/name "name")`  |  [Text](https://schema.org/Text "Text")  | The name of the item.   |  
| `               owner[](https://schema.org/owner "owner")`  |  [Organization](https://schema.org/Organization "Organization") or   
[Person](https://schema.org/Person "Person")  | A person or organization who owns this Thing.   
Inverse property: [owns](https://schema.org/owns "owns")  |  
| `               potentialAction[](https://schema.org/potentialAction "potentialAction")`  |  [Action](https://schema.org/Action "Action")  | Indicates a potential Action, which describes an idealized action in which this thing would play an 'object' role.   |  
| `               sameAs[](https://schema.org/sameAs "sameAs")`  |  [URL](https://schema.org/URL "URL")  | URL of a reference Web page that unambiguously indicates the item's identity. E.g. the URL of the item's Wikipedia page, Wikidata entry, or official website.   |  
| `               subjectOf[](https://schema.org/subjectOf "subjectOf")`  |  [CreativeWork](https://schema.org/CreativeWork "CreativeWork") or   
[Event](https://schema.org/Event "Event")  | A CreativeWork or Event about this Thing.   
Inverse property: [about](https://schema.org/about "about")  |  
| `               url[](https://schema.org/url "url")`  |  [URL](https://schema.org/URL "URL")  | URL of the item.   |  
  

Instances of [Offer](https://schema.org/Offer "Offer") may appear as a value for the following properties  
| Property  | On Types  | Description  |  
| --- | --- | --- |  
|  [acceptedOffer](https://schema.org/acceptedOffer "acceptedOffer")  |  [Order](https://schema.org/Order "Order")  | The offer(s) -- e.g., product, quantity and price combinations -- included in the order.   |  
|  [addOn](https://schema.org/addOn "addOn")  |  [Offer](https://schema.org/Offer "Offer")  | An additional offer that can only be obtained in combination with the first base offer (e.g. supplements and extensions that are available for a surcharge).   |  
|  [expectsAcceptanceOf](https://schema.org/expectsAcceptanceOf "expectsAcceptanceOf")  |  [ActionAccessSpecification](https://schema.org/ActionAccessSpecification "ActionAccessSpecification") or   
[ConsumeAction](https://schema.org/ConsumeAction "ConsumeAction") or   
[MediaSubscription](https://schema.org/MediaSubscription "MediaSubscription")  | An Offer which must be accepted before the user can perform the Action. For example, the user may need to buy a movie before being able to watch it.   |  
|  [hasParticipationOffer](https://schema.org/hasParticipationOffer "hasParticipationOffer")  |  [Event](https://schema.org/Event "Event")  | An offer to participate in the event, for example, Call for Proposals, Call for Speakers, or Call for Performers.   |  
|  [hasSponsorshipOffer](https://schema.org/hasSponsorshipOffer "hasSponsorshipOffer")  |  [Event](https://schema.org/Event "Event")  | An offer to sponsor the event, for example, Sponsorship Prospectus, Sponsorship Opportunities, or Sponsor Packages.   |  
|  [makesOffer](https://schema.org/makesOffer "makesOffer")  |  [Organization](https://schema.org/Organization "Organization") or   
[Person](https://schema.org/Person "Person")  | A pointer to products or services offered by the organization or person.   |  
|  [offers](https://schema.org/offers "offers")  |  [AggregateOffer](https://schema.org/AggregateOffer "AggregateOffer") or   
[CreativeWork](https://schema.org/CreativeWork "CreativeWork") or   
[EducationalOccupationalProgram](https://schema.org/EducationalOccupationalProgram "EducationalOccupationalProgram") or   
[Event](https://schema.org/Event "Event") or   
[MenuItem](https://schema.org/MenuItem "MenuItem") or   
[Product](https://schema.org/Product "Product") or   
[Service](https://schema.org/Service "Service") or   
[Trip](https://schema.org/Trip "Trip")  | An offer to provide this item—for example, an offer to sell a product, rent the DVD of a movie, perform a service, or give away tickets to an event. Use [businessFunction](https://schema.org/businessFunction) to indicate the kind of transaction offered, i.e. sell, lease, etc. This property can also be used to describe a [Demand](https://schema.org/Demand). While this property is listed as expected on a number of common types, it can be used in others. In that case, using a second type, such as Product or a subtype of Product, can clarify the nature of the offer.   |  
  

#### More specific Types
  * [AggregateOffer](https://schema.org/AggregateOffer "AggregateOffer")
  * [OfferForLease](https://schema.org/OfferForLease "OfferForLease")
  * [OfferForPurchase](https://schema.org/OfferForPurchase "OfferForPurchase")


### Acknowledgements
GoodRelations Vocabulary Terms 
This term [uses](https://blog.schema.org/2012/11/08/good-relations-and-schema-org/) terminology from the GoodRelations Vocabulary for E-Commerce, created by Martin Hepp. GoodRelations is a data model for sharing e-commerce data on the Web. More information about GoodRelations can be found at <http://purl.org/goodrelations/>. 
### Examples
![Copy to clipboard](https://schema.org/docs/clipboard/clippy.svg) [Example 1](https://schema.org/Offer#eg-0010 "Link: #eg-0010")
Copied
No Markup Microdata RDFa JSON-LD Structure
Example notes or example HTML without markup.

```



  1. 
Kenmore White 17" Microwave  




  2. 
<img src="kenmore-microwave-17in.jpg" alt='Kenmore 17" Microwave' />  




  3. 
Rated 3.5/5 based on 11 customer reviews  




  4. 
  




  5. 
$55.00  




  6. 
In stock  




  7. 
  




  8. 
Product description:  




  9. 
0.7 cubic feet countertop microwave. Has six preset cooking categories and  




  10. 
 convenience features like Add-A-Minute and Child Lock.  




  11. 
  




  12. 
Customer reviews:  




  13. 
  




  14. 
Not a happy camper - by Ellie, April 1, 2011  




  15. 
1/5 stars  




  16. 
The lamp burned out and now I have to replace it.  




  17. 
  




  18. 
 Value purchase - by Lucas, March 25, 2011  




  19. 
4/5 stars  




  20. 
Great microwave for the price. It is small and fits in my apartment.  




  21. ...



```

Example encoded as [Microdata](https://en.wikipedia.org/wiki/Microdata_\(HTML\)) embedded in HTML.

```



  1. 
<div itemscope itemtype="https://schema.org/Product">  




  2. 
  <span itemprop="name">Kenmore White 17" Microwave</span>  




  3. 
  <img itemprop="image" src="kenmore-microwave-17in.jpg" alt='Kenmore 17" Microwave' />  




  4. 
  <div itemprop="aggregateRating"  




  5. 
    itemscope itemtype="https://schema.org/AggregateRating">  




  6. 
   Rated <span itemprop="ratingValue">3.5</span>/5  




  7. 
   based on <span itemprop="reviewCount">11</span> customer reviews  




  8. 
  </div>  




  9. 
  




  10. 
  <div itemprop="offers" itemscope itemtype="https://schema.org/Offer">  




  11. 
  




  12. 
    <!--price is 1000, a number, with locale-specific thousands separator  




  13. 
    and decimal mark, and the $ character is marked up with the  




  14. 
    machine-readable code "USD" -->  




  15. 
    <span itemprop="priceCurrency" content="USD">$</span><span  




  16. 
          itemprop="price" content="1000.00">1,000.00</span>  




  17. 
  




  18. 
    <link itemprop="availability" href="https://schema.org/InStock" />In stock  




  19. 
  </div>  




  20. 
  




  21. 
  Product description:  




  22. 
  <span itemprop="description">0.7 cubic feet countertop microwave.  




  23. 
  Has six preset cooking categories and convenience features like  




  24. 
  Add-A-Minute and Child Lock.</span>  




  25. 
  




  26. 
  Customer reviews:  




  27. 
  




  28. 
  <div itemprop="review" itemscope itemtype="https://schema.org/Review">  




  29. 
    <span itemprop="name">Not a happy camper</span> -  




  30. 
    by <span itemprop="author">Ellie</span>,  




  31. 
    <meta itemprop="datePublished" content="2011-04-01">April 1, 2011  




  32. 
    <div itemprop="reviewRating" itemscope itemtype="https://schema.org/Rating">  




  33. 
      <meta itemprop="worstRating" content = "1">  




  34. 
      <span itemprop="ratingValue">1</span>/  




  35. 
      <span itemprop="bestRating">5</span>stars  




  36. 
    </div>  




  37. 
    <span itemprop="reviewBody">The lamp burned out and now I have to replace  




  38. 
    it. </span>  




  39. 
  </div>  




  40. 
  




  41. 
  <div itemprop="review" itemscope itemtype="https://schema.org/Review">  




  42. 
    <span itemprop="name">Value purchase</span> -  




  43. 
    by <span itemprop="author">Lucas</span>,  




  44. 
    <meta itemprop="datePublished" content="2011-03-25">March 25, 2011  




  45. 
    <div itemprop="reviewRating" itemscope itemtype="https://schema.org/Rating">  




  46. 
      <meta itemprop="worstRating" content = "1"/>  




  47. 
      <span itemprop="ratingValue">4</span>/  




  48. 
      <span itemprop="bestRating">5</span>stars  




  49. 
    </div>  




  50. 
    <span itemprop="reviewBody">Great microwave for the price. It is small and  




  51. 
    fits in my apartment.</span>  




  52. 
  </div>  




  53. 
  ...  




  54. 
</div>




```

Example encoded as [RDFa](https://en.wikipedia.org/wiki/RDFa) embedded in HTML.

```



  1. 
<div vocab="https://schema.org/" typeof="Product">  




  2. 
  <span property="name">Kenmore White 17" Microwave</span>  




  3. 
  <img property="image" src="kenmore-microwave-17in.jpg" alt='Kenmore 17" Microwave' />  




  4. 
  <div property="aggregateRating"  




  5. 
     typeof="AggregateRating">  




  6. 
   Rated <span property="ratingValue">3.5</span>/5  




  7. 
   based on <span property="reviewCount">11</span> customer reviews  




  8. 
  </div>  




  9. 
  




  10. 
  <div property="offers" typeof="Offer">  




  11. 
    <!--price is 1000, a number, with locale-specific thousands separator  




  12. 
        and decimal mark, and the $ character is marked up with the  




  13. 
        machine-readable code "USD" -->  




  14. 
    <span property="priceCurrency" content="USD">$</span><span  




  15. 
      property="price" content="1000.00">1,000.00</span>  




  16. 
    <link property="availability" href="https://schema.org/InStock" />In stock  




  17. 
  </div>  




  18. 
  




  19. 
  Product description:  




  20. 
  <span property="description">0.7 cubic feet countertop microwave.  




  21. 
  Has six preset cooking categories and convenience features like  




  22. 
  Add-A-Minute and Child Lock.</span>  




  23. 
  




  24. 
  Customer reviews:  




  25. 
  




  26. 
  <div property="review" typeof="Review">  




  27. 
    <span property="name">Not a happy camper</span> -  




  28. 
    by <span property="author">Ellie</span>,  




  29. 
    <meta property="datePublished" content="2011-04-01">April 1, 2011  




  30. 
    <div property="reviewRating" typeof="Rating">  




  31. 
      <meta property="worstRating" content = "1">  




  32. 
      <span property="ratingValue">1</span>/  




  33. 
      <span property="bestRating">5</span>stars  




  34. 
    </div>  




  35. 
    <span property="reviewBody">The lamp burned out and now I have to replace  




  36. 
    it. </span>  




  37. 
  </div>  




  38. 
  




  39. 
  <div property="review" typeof="Review">  




  40. 
    <span property="name">Value purchase</span> -  




  41. 
    by <span property="author">Lucas</span>,  




  42. 
    <meta property="datePublished" content="2011-03-25">March 25, 2011  




  43. 
    <div property="reviewRating" typeof="Rating">  




  44. 
      <meta property="worstRating" content = "1"/>  




  45. 
      <span property="ratingValue">4</span>/  




  46. 
      <span property="bestRating">5</span>stars  




  47. 
    </div>  




  48. 
    <span property="reviewBody">Great microwave for the price. It is small and  




  49. 
    fits in my apartment.</span>  




  50. 
  </div>  




  51. 
  ...  




  52. 
</div>




```

Example encoded as [JSON-LD](https://en.wikipedia.org/wiki/JSON-LD) in a HTML script tag.

```



  1. 
<script type="application/ld+json">  




  2. 
{  




  3. 
  "@context": "https://schema.org",  




  4. 
  "@type": "Product",  




  5. 
  "aggregateRating": {  




  6. 
    "@type": "AggregateRating",  




  7. 
    "ratingValue": "3.5",  




  8. 
    "reviewCount": "11"  




  9. 
  },  




  10. 
  "description": "0.7 cubic feet countertop microwave. Has six preset cooking categories and convenience features like Add-A-Minute and Child Lock.",  




  11. 
  "name": "Kenmore White 17\" Microwave",  




  12. 
  "image": "kenmore-microwave-17in.jpg",  




  13. 
  "offers": {  




  14. 
    "@type": "Offer",  




  15. 
    "availability": "https://schema.org/InStock",  




  16. 
    "price": "55.00",  




  17. 
    "priceCurrency": "USD"  




  18. 
  },  




  19. 
  "review": [  




  20. 
    {  




  21. 
      "@type": "Review",  




  22. 
      "author": "Ellie",  




  23. 
      "datePublished": "2011-04-01",  




  24. 
      "reviewBody": "The lamp burned out and now I have to replace it.",  




  25. 
      "name": "Not a happy camper",  




  26. 
      "reviewRating": {  




  27. 
        "@type": "Rating",  




  28. 
        "bestRating": "5",  




  29. 
        "ratingValue": "1",  




  30. 
        "worstRating": "1"  




  31. 
      }  




  32. 
    },  




  33. 
    {  




  34. 
      "@type": "Review",  




  35. 
      "author": "Lucas",  




  36. 
      "datePublished": "2011-03-25",  




  37. 
      "reviewBody": "Great microwave for the price. It is small and fits in my apartment.",  




  38. 
      "name": "Value purchase",  




  39. 
      "reviewRating": {  




  40. 
        "@type": "Rating",  




  41. 
        "bestRating": "5",  




  42. 
        "ratingValue": "4",  




  43. 
        "worstRating": "1"  




  44. 
      }  




  45. 
    }  




  46. 
  ]  




  47. 
}  




  48. 
</script>




```

Structured representation of the JSON-LD example.
{ "@context": "https://schema.org", "@type": "Product", "aggregateRating": { "@type": "AggregateRating", "ratingValue": "3.5", "reviewCount": "11" }, "description": "0.7 cubic feet countertop microwave. Has six preset cooking categories and convenience features like Add-A-Minute and Child Lock.", "name": "Kenmore White 17\" Microwave", "image": "kenmore-microwave-17in.jpg", "offers": { "@type": "Offer", "availability": "https://schema.org/InStock", "price": "55.00", "priceCurrency": "USD" }, "review": [ { "@type": "Review", "author": "Ellie", "datePublished": "2011-04-01", "reviewBody": "The lamp burned out and now I have to replace it.", "name": "Not a happy camper", "reviewRating": { "@type": "Rating", "bestRating": "5", "ratingValue": "1", "worstRating": "1" } }, { "@type": "Review", "author": "Lucas", "datePublished": "2011-03-25", "reviewBody": "Great microwave for the price. It is small and fits in my apartment.", "name": "Value purchase", "reviewRating": { "@type": "Rating", "bestRating": "5", "ratingValue": "4", "worstRating": "1" } } ] }
![Copy to clipboard](https://schema.org/docs/clipboard/clippy.svg) [Example 2](https://schema.org/Offer#eg-0011 "Link: #eg-0011")
Copied
No Markup Microdata RDFa JSON-LD Structure
Example notes or example HTML without markup.

```



  1. 
<img src="dell-30in-lcd.jpg" alt="A Dell UltraSharp monitor" />  




  2. 
Dell UltraSharp 30" LCD Monitor  




  3. 
  




  4. 
87 out of 100 based on 24 user ratings  




  5. 
  




  6. 
$1250 to $1495 from 8 sellers  




  7. 
  




  8. 
Sellers:  




  9. 
<a href="save-a-lot-monitors.com/dell-30.html">  




  10. 
  Save A Lot Monitors - $1250</a>  




  11. 
<a href="jondoe-gadgets.com/dell-30.html">  




  12. 
  Jon Doe's Gadgets - $1350</a>  




  13. ...



```

Example encoded as [Microdata](https://en.wikipedia.org/wiki/Microdata_\(HTML\)) embedded in HTML.

```



  1. 
<div itemscope itemtype="https://schema.org/Product">  




  2. 
  <img itemprop="image" src="dell-30in-lcd.jpg" alt="A Dell UltraSharp monitor"/>  




  3. 
  <span itemprop="name">Dell UltraSharp 30" LCD Monitor</span>  




  4. 
  




  5. 
  <div itemprop="aggregateRating"  




  6. 
    itemscope itemtype="https://schema.org/AggregateRating">  




  7. 
    <span itemprop="ratingValue">87</span>  




  8. 
    out of <span itemprop="bestRating">100</span>  




  9. 
    based on <span itemprop="ratingCount">24</span> user ratings  




  10. 
  </div>  




  11. 
  




  12. 
  <div itemprop="offers" itemscope itemtype="https://schema.org/AggregateOffer">  




  13. 
    <meta itemprop="priceCurrency" content="USD" />  




  14. 
    <span itemprop="lowPrice" content="1250">$1250</span>  




  15. 
    to <span itemprop="highPrice" content="1495">$1495</span>  




  16. 
    from <span itemprop="offerCount">8</span> sellers  




  17. 
  




  18. 
    Sellers:  




  19. 
    <div itemprop="offers" itemscope itemtype="https://schema.org/Offer">  




  20. 
        <a itemprop="url" href="save-a-lot-monitors.com/dell-30.html">  




  21. 
        Save A Lot Monitors - $1250</a>  




  22. 
    </div>  




  23. 
    <div itemprop="offers" itemscope itemtype="https://schema.org/Offer">  




  24. 
        <a itemprop="url" href="jondoe-gadgets.com/dell-30.html">  




  25. 
        Jon Doe's Gadgets - $1350</a>  




  26. 
    </div>  




  27. 
  </div>  




  28. 
  ...  




  29. 
</div>




```

Example encoded as [RDFa](https://en.wikipedia.org/wiki/RDFa) embedded in HTML.

```



  1. 
<div vocab="https://schema.org/" typeof="Product">  




  2. 
    <img property="image" src="dell-30in-lcd.jpg" alt="A Dell UltraSharp monitor"> <span property="name">Dell UltraSharp 30" LCD Monitor</span>  




  3. 
    <div property="aggregateRating" typeof="AggregateRating">  




  4. 
        <span property="ratingValue">87</span> out of  




  5. 
        <span property="bestRating">100</span> based on  




  6. 
        <span property="ratingCount">24</span> user ratings  




  7. 
    </div>  




  8. 
    <div property="offers" typeof="AggregateOffer">  




  9. 
        <meta property="priceCurrency" content="USD" />  




  10. 
        <span property="lowPrice" content="1250">$1250</span> to  




  11. 
        <span property="highPrice" content="1495">$1495</span> from  




  12. 
        <span property="offerCount">8</span> sellers Sellers:  




  13. 
        <div property="offers" typeof="Offer">  




  14. 
            <a property="url" href="save-a-lot-monitors.com/dell-30.html">Save A Lot Monitors - $1250</a>  




  15. 
        </div>  




  16. 
        <div property="offers" typeof="Offer">  




  17. 
            <a property="url" href="jondoe-gadgets.com/dell-30.html">Jon Doe's Gadgets - $1350</a>  




  18. 
        </div>  




  19. 
        ...  




  20. 
    </div>  




  21. 
</div>




```

Example encoded as [JSON-LD](https://en.wikipedia.org/wiki/JSON-LD) in a HTML script tag.

```



  1. 
<script type="application/ld+json">  




  2. 
{  




  3. 
  "@context": "https://schema.org",  




  4. 
  "@type": "Product",  




  5. 
  "aggregateRating": {  




  6. 
    "@type": "AggregateRating",  




  7. 
    "bestRating": "100",  




  8. 
    "ratingCount": "24",  




  9. 
    "ratingValue": "87"  




  10. 
  },  




  11. 
  "image": "dell-30in-lcd.jpg",  




  12. 
  "name": "Dell UltraSharp 30\" LCD Monitor",  




  13. 
  "offers": {  




  14. 
    "@type": "AggregateOffer",  




  15. 
    "priceCurrency": "USD",  




  16. 
    "highPrice": "1495",  




  17. 
    "lowPrice": "1250",  




  18. 
    "offerCount": "8",  




  19. 
    "offers": [  




  20. 
      {  




  21. 
        "@type": "Offer",  




  22. 
        "url": "save-a-lot-monitors.com/dell-30.html"  




  23. 
      },  




  24. 
      {  




  25. 
        "@type": "Offer",  




  26. 
        "url": "jondoe-gadgets.com/dell-30.html"  




  27. 
      }  




  28. 
    ]  




  29. 
  }  




  30. 
}  




  31. 
</script>




```

Structured representation of the JSON-LD example.
{ "@context": "https://schema.org", "@type": "Product", "aggregateRating": { "@type": "AggregateRating", "bestRating": "100", "ratingCount": "24", "ratingValue": "87" }, "image": "dell-30in-lcd.jpg", "name": "Dell UltraSharp 30\" LCD Monitor", "offers": { "@type": "AggregateOffer", "priceCurrency": "USD", "highPrice": "1495", "lowPrice": "1250", "offerCount": "8", "offers": [ { "@type": "Offer", "url": "save-a-lot-monitors.com/dell-30.html" }, { "@type": "Offer", "url": "jondoe-gadgets.com/dell-30.html" } ] } }
![Copy to clipboard](https://schema.org/docs/clipboard/clippy.svg) [Example 3](https://schema.org/Offer#eg-0012 "Link: #eg-0012")
Copied
No Markup Microdata RDFa JSON-LD Structure
Example notes or example HTML without markup.

```



  1. 
<div class="event-wrapper">  




  2. 
  




  3. 
  <div class="event-date">Sat Sep 14</div>  




  4. 
  <div class="event-title">Typhoon with Radiation City</div>  




  5. 
  




  6. 
  <div class="event-venue">  




  7. 
    The Hi-Dive  




  8. 
    <div class="address">  




  9. 
      7 S. Broadway<br>  




  10. 
      Denver, CO 80209  




  11. 
    </div>  




  12. 
  </div>  




  13. 
  




  14. 
  <div class="event-time">9:30 PM</div>  




  15. 
  




  16. 
  <div class="event-price">$13.00</div>  




  17. 
  <a href="http://www.ticketfly.com/purchase/309433">Tickets</a>  




  18. 
  




  19. 
</div>




```

Example encoded as [Microdata](https://en.wikipedia.org/wiki/Microdata_\(HTML\)) embedded in HTML.

```



  1. 
<div class="event-wrapper" itemscope itemtype="https://schema.org/Event">  




  2. 
    <div class="event-date" itemprop="startDate" content="2013-09-14T21:30">  




  3. 
        Sat Sep 14  




  4. 
    </div>  




  5. 
    <div class="event-title" itemprop="name">  




  6. 
        Typhoon with Radiation City  




  7. 
    </div>  




  8. 
    <div class="event-venue" itemprop="location" itemscope itemtype="https://schema.org/Place">  




  9. 
        <span itemprop="name">The Hi-Dive</span>  




  10. 
        <div class="address" itemprop="address" itemscope itemtype="https://schema.org/PostalAddress">  




  11. 
            <span itemprop="streetAddress">7 S. Broadway</span><br>  




  12. 
            <span itemprop="addressLocality">Denver</span>, <span itemprop="addressRegion">CO</span> <span itemprop="postalCode">80209</span>  




  13. 
        </div>  




  14. 
    </div>  




  15. 
    <div class="event-time">9:30 PM</div>  




  16. 
    <div itemprop="offers" itemscope itemtype="https://schema.org/Offer">  




  17. 
        <div class="event-price" itemprop="price" content="13.00">$13.00</div>  




  18. 
        <meta itemprop="priceCurrency" content="USD"><a itemprop="url" href="http://www.ticketfly.com/purchase/309433">Tickets</a>  




  19. 
    </div>  




  20. 
</div>




```

Example encoded as [RDFa](https://en.wikipedia.org/wiki/RDFa) embedded in HTML.

```



  1. 
<div vocab="https://schema.org/" class="event-wrapper" typeof="Event">  




  2. 
  




  3. 
  <div class="event-date" property="startDate" content="2013-09-14T21:30">Sat Sep 14</div>  




  4. 
  <div class="event-title" property="name">Typhoon with Radiation City</div>  




  5. 
  




  6. 
  <div class="event-venue" property="location" typeof="Place">  




  7. 
    <span property="name">The Hi-Dive</span>  




  8. 
    <div class="address" property="address" typeof="PostalAddress">  




  9. 
      <span property="streetAddress">7 S. Broadway</span><br>  




  10. 
      <span property="addressLocality">Denver</span>,  




  11. 
      <span property="addressRegion">CO</span>  




  12. 
      <span property="postalCode">80209</span>  




  13. 
    </div>  




  14. 
  </div>  




  15. 
  




  16. 
  <div class="event-time">9:30 PM</div>  




  17. 
  




  18. 
 <span property="offers" typeof="Offer">  




  19. 
 <div class="event-price">  




  20. 
    <meta property="priceCurrency" content="USD" />$  




  21. 
    <meta property="price" content="13.00" />13.00  




  22. 
 </div>  




  23. 
 <a property="url" href="http://www.ticketfly.com/purchase/309433">Tickets</a>  




  24. 
 </span>  




  25. 
</div>




```

Example encoded as [JSON-LD](https://en.wikipedia.org/wiki/JSON-LD) in a HTML script tag.

```



  1. 
<script type="application/ld+json">  




  2. 
{  




  3. 
  "@context": "https://schema.org",  




  4. 
  "@type": "Event",  




  5. 
  "location": {  




  6. 
    "@type": "Place",  




  7. 
    "address": {  




  8. 
      "@type": "PostalAddress",  




  9. 
      "addressLocality": "Denver",  




  10. 
      "addressRegion": "CO",  




  11. 
      "postalCode": "80209",  




  12. 
      "streetAddress": "7 S. Broadway"  




  13. 
    },  




  14. 
    "name": "The Hi-Dive"  




  15. 
  },  




  16. 
  "name": "Typhoon with Radiation City",  




  17. 
  "offers": {  




  18. 
    "@type": "Offer",  




  19. 
    "price": "13.00",  




  20. 
    "priceCurrency": "USD",  




  21. 
    "url": "http://www.ticketfly.com/purchase/309433"  




  22. 
  },  




  23. 
  "startDate": "2013-09-14T21:30"  




  24. 
}  




  25. 
</script>




```

Structured representation of the JSON-LD example.
{ "@context": "https://schema.org", "@type": "Event", "location": { "@type": "Place", "address": { "@type": "PostalAddress", "addressLocality": "Denver", "addressRegion": "CO", "postalCode": "80209", "streetAddress": "7 S. Broadway" }, "name": "The Hi-Dive" }, "name": "Typhoon with Radiation City", "offers": { "@type": "Offer", "price": "13.00", "priceCurrency": "USD", "url": "http://www.ticketfly.com/purchase/309433" }, "startDate": "2013-09-14T21:30" }
![Copy to clipboard](https://schema.org/docs/clipboard/clippy.svg) [Example 4](https://schema.org/Offer#eg-0171 "Link: #eg-0171")
Copied
No Markup Microdata RDFa JSON-LD Structure
Example notes or example HTML without markup.

```



  1. 
<div class="event-wrapper">  




  2. 
  




  3. 
  <div class="event-date">Sat Sep 14</div>  




  4. 
  <div class="event-title">Typhoon with Radiation City</div>  




  5. 
  <div class="event-title">CANCELLED - Typhoon with Radiation City</div>  




  6. 
  




  7. 
  <div class="event-venue">  




  8. 
    The Hi-Dive  




  9. 
    <div class="address">  




  10. 
      7 S. Broadway<br>  




  11. 
      Denver, CO 80209  




  12. 
    </div>  




  13. 
  </div>  




  14. 
  




  15. 
  <div class="event-time">9:30 PM</div>  




  16. 
  




  17. 
  <div class="event-price">$13.00</div>  




  18. 
  <a href="http://www.ticketfly.com/purchase/309433">Tickets</a>  




  19. 
  




  20. 
</div>




```

Example encoded as [Microdata](https://en.wikipedia.org/wiki/Microdata_\(HTML\)) embedded in HTML.

```



  1. 
<div class="event-wrapper" itemscope itemtype="https://schema.org/Event">  




  2. 
    <div class="event-date" itemprop="startDate" content="2013-09-14T21:30">  




  3. 
        Sat Sep 14  




  4. 
    </div>  




  5. 
    <div class="event-title" itemprop="name">  




  6. 
        CANCELLED - Typhoon with Radiation City  




  7. 
    </div>  




  8. 
    <meta itemprop="eventStatus" content="https://schema.org/EventCancelled">  




  9. 
    <div class="event-venue" itemprop="location" itemscope itemtype="https://schema.org/Place">  




  10. 
        <span itemprop="name">The Hi-Dive</span>  




  11. 
        <div class="address" itemprop="address" itemscope itemtype="https://schema.org/PostalAddress">  




  12. 
            <span itemprop="streetAddress">7 S. Broadway</span><br>  




  13. 
            <span itemprop="addressLocality">Denver</span>, <span itemprop="addressRegion">CO</span> <span itemprop="postalCode">80209</span>  




  14. 
        </div>  




  15. 
    </div>  




  16. 
    <div class="event-time">9:30 PM</div>  




  17. 
    <div itemprop="offers" itemscope itemtype="https://schema.org/Offer">  




  18. 
        <div class="event-price" itemprop="price" content="13.00">$13.00</div>  




  19. 
        <meta itemprop="priceCurrency" content="USD">  




  20. 
        <a itemprop="url" href="http://www.ticketfly.com/purchase/309433">Tickets</a>  




  21. 
    </div>  




  22. 
</div>




```

Example encoded as [RDFa](https://en.wikipedia.org/wiki/RDFa) embedded in HTML.

```



  1. 
<div vocab="https://schema.org/" class="event-wrapper" typeof="Event">  




  2. 
    <div class="event-date" property="startDate" content="2013-09-14T21:30">  




  3. 
        Sat Sep 14  




  4. 
    </div>  




  5. 
    <div class="event-title" property="name">  




  6. 
        CANCELLED - Typhoon with Radiation City  




  7. 
    </div>  




  8. 
    <meta property="eventStatus" content="https://schema.org/EventCancelled">  




  9. 
    <div class="event-venue" property="location" typeof="Place">  




  10. 
        <span property="name">The Hi-Dive</span>  




  11. 
        <div class="address" property="address" typeof="PostalAddress">  




  12. 
            <span property="streetAddress">7 S. Broadway</span><br>  




  13. 
            <span property="addressLocality">Denver</span>, <span property="addressRegion">CO</span> <span property="postalCode">80209</span>  




  14. 
        </div>  




  15. 
    </div>  




  16. 
    <div class="event-time">9:30 PM</div>  




  17. 
    <div property="offers" typeof="Offer">  




  18. 
        $<div class="event-price" property="price">13.00</div>  




  19. 
        <meta property="priceCurrency" content="USD"><a property="url" href="http://www.ticketfly.com/purchase/309433">Tickets</a>  




  20. 
    </div>  




  21. 
</div>




```

Example encoded as [JSON-LD](https://en.wikipedia.org/wiki/JSON-LD) in a HTML script tag.

```



  1. 
<script type="application/ld+json">  




  2. 
{  




  3. 
  "@context": "https://schema.org",  




  4. 
  "@type": "Event",  




  5. 
  "eventStatus": "https://schema.org/EventCancelled",  




  6. 
  "location": {  




  7. 
    "@type": "Place",  




  8. 
    "address": {  




  9. 
      "@type": "PostalAddress",  




  10. 
      "addressLocality": "Denver",  




  11. 
      "addressRegion": "CO",  




  12. 
      "postalCode": "80209",  




  13. 
      "streetAddress": "7 S. Broadway"  




  14. 
    },  




  15. 
    "name": "The Hi-Dive"  




  16. 
  },  




  17. 
  "name": "CANCELLED - Typhoon with Radiation City",  




  18. 
  "offers": {  




  19. 
    "@type": "Offer",  




  20. 
    "price": "13.00",  




  21. 
    "priceCurrency": "USD",  




  22. 
    "url": "http://www.ticketfly.com/purchase/309433"  




  23. 
  },  




  24. 
  "startDate": "2013-09-14T21:30"  




  25. 
}  




  26. 
</script>




```

Structured representation of the JSON-LD example.
{ "@context": "https://schema.org", "@type": "Event", "eventStatus": "https://schema.org/EventCancelled", "location": { "@type": "Place", "address": { "@type": "PostalAddress", "addressLocality": "Denver", "addressRegion": "CO", "postalCode": "80209", "streetAddress": "7 S. Broadway" }, "name": "The Hi-Dive" }, "name": "CANCELLED - Typhoon with Radiation City", "offers": { "@type": "Offer", "price": "13.00", "priceCurrency": "USD", "url": "http://www.ticketfly.com/purchase/309433" }, "startDate": "2013-09-14T21:30" }
![Copy to clipboard](https://schema.org/docs/clipboard/clippy.svg) [Example 5](https://schema.org/Offer#eg-0172 "Link: #eg-0172")
Copied
No Markup Microdata RDFa JSON-LD Structure
Example notes or example HTML without markup.

```



  1. 
<div class="event-wrapper">  




  2. 
  <div class="event-date">Sat Oct 12</div>  




  3. 
  <div><span>(previously scheduled for Sept 14th)</span></div>  




  4. 
  <div class="event-title">Typhoon with Radiation City</div>  




  5. 
  <div class="event-venue">  




  6. 
    The Hi-Dive  




  7. 
    <div class="address">  




  8. 
      7 S. Broadway<br>  




  9. 
      Denver, CO 80209  




  10. 
    </div>  




  11. 
  </div>  




  12. 
  <div class="event-time">10:00 PM</div>  




  13. 
 <span>  




  14. 
  <div class="event-price">$13.00</div>  




  15. 
  <a href="http://www.ticketfly.com/purchase/309433">Tickets</a>  




  16. 
 </span>  




  17. 
</div>




```

Example encoded as [Microdata](https://en.wikipedia.org/wiki/Microdata_\(HTML\)) embedded in HTML.

```



  1. 
<div class="event-wrapper" itemscope itemtype="https://schema.org/Event">  




  2. 
    <div class="event-date" itemprop="startDate" content="2013-10-12T22:00">  




  3. 
        Sat Oct 12  




  4. 
    </div>  




  5. 
    <div class="event-title" itemprop="name">  




  6. 
        Typhoon with Radiation City  




  7. 
    </div>  




  8. 
    <meta itemprop="eventStatus" content="https://schema.org/EventRescheduled"><span itemprop="previousStartDate" content="2013-09-14T21:30">(previously scheduled for Sept 14th)</span>  




  9. 
    <div class="event-venue" itemprop="location" itemscope itemtype="https://schema.org/Place">  




  10. 
        <span itemprop="name">The Hi-Dive</span>  




  11. 
        <div class="address" itemprop="address" itemscope itemtype="https://schema.org/PostalAddress">  




  12. 
            <span itemprop="streetAddress">7 S. Broadway</span><br>  




  13. 
            <span itemprop="addressLocality">Denver</span>, <span itemprop="addressRegion">CO</span> <span itemprop="postalCode">80209</span>  




  14. 
        </div>  




  15. 
    </div>  




  16. 
    <div class="event-time">  




  17. 
        10:00 PM  




  18. 
    </div>  




  19. 
    <div itemprop="offers" itemscope itemtype="https://schema.org/Offer">  




  20. 
        <div class="event-price" itemprop="price" content="13.00">$13.00</div>  




  21. 
        <meta itemprop="priceCurrency" content="USD"><a itemprop="url" href="http://www.ticketfly.com/purchase/309433">Tickets</a>  




  22. 
    </div>  




  23. 
</div>




```

Example encoded as [RDFa](https://en.wikipedia.org/wiki/RDFa) embedded in HTML.

```



  1. 
<div vocab="https://schema.org/" class="event-wrapper" typeof="Event">  




  2. 
  <div class="event-date" property="startDate" content="2013-10-12T22:00">Sat Oct 12</div>  




  3. 
  <div class="event-title" property="name">Typhoon with Radiation City</div>  




  4. 
  <meta property="eventStatus" content="https://schema.org/EventRescheduled">  




  5. 
  <span property="previousStartDate" content="2013-09-14T21:30">(previously scheduled for Sept 14th)</span>  




  6. 
  




  7. 
  <div class="event-venue" property="location" typeof="Place">  




  8. 
    <span property="name">The Hi-Dive</span>  




  9. 
    <div class="address" property="address" typeof="PostalAddress">  




  10. 
      <span property="streetAddress">7 S. Broadway</span><br>  




  11. 
      <span property="addressLocality">Denver</span>,  




  12. 
      <span property="addressRegion">CO</span>  




  13. 
      <span property="postalCode">80209</span>  




  14. 
    </div>  




  15. 
  </div>  




  16. 
  <div class="event-time">10:00 PM</div>  




  17. 
  <span property="offers" typeof="Offer">  




  18. 
  <div class="event-price">  




  19. 
    <meta property="priceCurrency" content="USD" />$  




  20. 
    <meta property="price" content="13.00" />13.00  




  21. 
  </div>  




  22. 
  <a property="url" href="http://www.ticketfly.com/purchase/309433">Tickets</a>  




  23. 
  </span>  




  24. 
</div>




```

Example encoded as [JSON-LD](https://en.wikipedia.org/wiki/JSON-LD) in a HTML script tag.

```



  1. 
<script type="application/ld+json">  




  2. 
{  




  3. 
  "@context": "https://schema.org",  




  4. 
  "@graph": [  




  5. 
    {  




  6. 
      "@type": "Place",  




  7. 
      "address": {  




  8. 
        "@type": "PostalAddress",  




  9. 
        "addressLocality": "Denver",  




  10. 
        "addressRegion": "CO",  




  11. 
        "postalCode": "80209",  




  12. 
        "streetAddress": "7 S. Broadway"  




  13. 
      },  




  14. 
      "name": "The Hi-Dive"  




  15. 
    },  




  16. 
    {  




  17. 
      "@type": "Offer",  




  18. 
      "price": "13.00",  




  19. 
      "priceCurrency": "USD",  




  20. 
      "url": "http://www.ticketfly.com/purchase/309433"  




  21. 
    }  




  22. 
  ]  




  23. 
}  




  24. 
</script>




```

Structured representation of the JSON-LD example.
{ "@context": "https://schema.org", "@graph": [ { "@type": "Place", "address": { "@type": "PostalAddress", "addressLocality": "Denver", "addressRegion": "CO", "postalCode": "80209", "streetAddress": "7 S. Broadway" }, "name": "The Hi-Dive" }, { "@type": "Offer", "price": "13.00", "priceCurrency": "USD", "url": "http://www.ticketfly.com/purchase/309433" } ] }
![Copy to clipboard](https://schema.org/docs/clipboard/clippy.svg) [Example 6](https://schema.org/Offer#eg-0173 "Link: #eg-0173")
Copied
No Markup Microdata RDFa JSON-LD Structure
Example notes or example HTML without markup.

```



  1. 
<div class="event-wrapper">  




  2. 
  <div class="event-date">Sat Sep 14</div>  




  3. 
  <div class="event-title">SOLD OUT! Typhoon with Radiation City</div>  




  4. 
  <div class="event-venue">  




  5. 
    The Hi-Dive  




  6. 
    <div class="address">  




  7. 
      7 S. Broadway<br>  




  8. 
      Denver, CO 80209  




  9. 
    </div>  




  10. 
  </div>  




  11. 
  <div class="event-time">10:00 PM</div>  




  12. 
 <span>  




  13. 
  <div class="event-price">$13.00</div>  




  14. 
  <a href="http://www.ticketfly.com/purchase/309433">Tickets</a>  




  15. 
 </span>  




  16. 
</div>




```

Example encoded as [Microdata](https://en.wikipedia.org/wiki/Microdata_\(HTML\)) embedded in HTML.

```



  1. 
<div class="event-wrapper" itemscope itemtype="https://schema.org/Event">  




  2. 
    <div class="event-date" itemprop="startDate" content="2013-09-14T21:30">  




  3. 
        Sat Sep 14  




  4. 
    </div>  




  5. 
    <div class="event-title" itemprop="name">  




  6. 
        SOLD OUT! Typhoon with Radiation City  




  7. 
    </div>  




  8. 
    <div class="event-venue" itemprop="location" itemscope itemtype="https://schema.org/Place">  




  9. 
        <span itemprop="name">The Hi-Dive</span>  




  10. 
        <div class="address" itemprop="address" itemscope itemtype="https://schema.org/PostalAddress">  




  11. 
            <span itemprop="streetAddress">7 S. Broadway</span><br>  




  12. 
            <span itemprop="addressLocality">Denver</span>, <span itemprop="addressRegion">CO</span> <span itemprop="postalCode">80209</span>  




  13. 
        </div>  




  14. 
    </div>  




  15. 
    <div class="event-time">9:30 PM</div>  




  16. 
    <div itemprop="offers" itemscope itemtype="https://schema.org/Offer">  




  17. 
        <meta itemprop="availability" content="https://schema.org/SoldOut">  




  18. 
        <div class="event-price" itemprop="price" content="13.00">$13.00</div>  




  19. 
        <meta itemprop="priceCurrency" content="USD"><a itemprop="url" href="http://www.ticketfly.com/purchase/309433">Tickets</a>  




  20. 
    </div>  




  21. 
</div>




```

Example encoded as [RDFa](https://en.wikipedia.org/wiki/RDFa) embedded in HTML.

```



  1. 
<div vocab="https://schema.org/" class="event-wrapper" typeof="Event">  




  2. 
  




  3. 
  <div class="event-date" property="startDate" content="2013-09-14T21:30">Sat Sep 14</div>  




  4. 
  <div class="event-title" property="name">SOLD OUT! Typhoon with Radiation City</div>  




  5. 
  




  6. 
  <div class="event-venue" property="location" typeof="Place">  




  7. 
    <span property="name">The Hi-Dive</span>  




  8. 
    <div class="address" property="address" typeof="PostalAddress">  




  9. 
      <span property="streetAddress">7 S. Broadway</span><br>  




  10. 
      <span property="addressLocality">Denver</span>,  




  11. 
      <span property="addressRegion">CO</span>  




  12. 
      <span property="postalCode">80209</span>  




  13. 
    </div>  




  14. 
  </div>  




  15. 
  




  16. 
  <div class="event-time">9:30 PM</div>  




  17. 
  




  18. 
 <span property="offers" typeof="Offer">  




  19. 
  <meta property="availability" content="https://schema.org/SoldOut">  




  20. 
  <div class="event-price">  




  21. 
    <meta property="priceCurrency" content="USD" />$  




  22. 
    <meta property="price" content="13.00" />13.00  




  23. 
  </div>  




  24. 
  <a property="url" href="http://www.ticketfly.com/purchase/309433">Tickets</a>  




  25. 
 </span>  




  26. 
</div>




```

Example encoded as [JSON-LD](https://en.wikipedia.org/wiki/JSON-LD) in a HTML script tag.

```



  1. 
<script type="application/ld+json">  




  2. 
{  




  3. 
  "@context": "https://schema.org",  




  4. 
  "@type": "Event",  




  5. 
  "location": {  




  6. 
    "@type": "Place",  




  7. 
    "address": {  




  8. 
      "@type": "PostalAddress",  




  9. 
      "addressLocality": "Denver",  




  10. 
      "addressRegion": "CO",  




  11. 
      "postalCode": "80209",  




  12. 
      "streetAddress": "7 S. Broadway"  




  13. 
    },  




  14. 
    "name": "The Hi-Dive"  




  15. 
  },  




  16. 
  "name": "SOLD OUT! Typhoon with Radiation City",  




  17. 
  "offers": {  




  18. 
    "@type": "Offer",  




  19. 
    "availability": "https://schema.org/SoldOut",  




  20. 
    "price": "13.00",  




  21. 
    "priceCurrency": "USD",  




  22. 
    "url": "http://www.ticketfly.com/purchase/309433"  




  23. 
  },  




  24. 
  "startDate": "2013-09-14T21:30"  




  25. 
}  




  26. 
</script>




```

Structured representation of the JSON-LD example.
{ "@context": "https://schema.org", "@type": "Event", "location": { "@type": "Place", "address": { "@type": "PostalAddress", "addressLocality": "Denver", "addressRegion": "CO", "postalCode": "80209", "streetAddress": "7 S. Broadway" }, "name": "The Hi-Dive" }, "name": "SOLD OUT! Typhoon with Radiation City", "offers": { "@type": "Offer", "availability": "https://schema.org/SoldOut", "price": "13.00", "priceCurrency": "USD", "url": "http://www.ticketfly.com/purchase/309433" }, "startDate": "2013-09-14T21:30" }
![Copy to clipboard](https://schema.org/docs/clipboard/clippy.svg) [Example 7](https://schema.org/Offer#eg-0174 "Link: #eg-0174")
Copied
No Markup JSON-LD Structure
Example notes or example HTML without markup.

```

  1. JSON-LD description of a scheduled Event with limited ticket availability and performer details indicated using sameAs.


```

Example encoded as [JSON-LD](https://en.wikipedia.org/wiki/JSON-LD) in a HTML script tag.

```



  1. 
<script type="application/ld+json">  




  2. 
{  




  3. 
  "@context" : "https://schema.org",  




  4. 
  "@type" : "Event",  




  5. 
  "name" : "Typhoon with Radiation City",  




  6. 
  "startDate" : "2013-09-14T21:30",  




  7. 
  "location" : {  




  8. 
    "@type" : "Place",  




  9. 
    "sameAs" : "http://www.hi-dive.com",  




  10. 
    "name" : "The Hi-Dive",  




  11. 
    "address" : {  




  12. 
      "@type" : "PostalAddress",  




  13. 
      "streetAddress" : "7 S. Broadway",  




  14. 
      "addressLocality" : "Denver",  




  15. 
      "addressRegion" : "CO",  




  16. 
      "postalCode" : "80209" }  




  17. 
  },  




  18. 
  "performer" : [  




  19. 
    { "@type" : "MusicGroup",  




  20. 
      "name" : "Typhoon",  




  21. 
      "sameAs" : "http://en.wikipedia.org/wiki/Typhoon_(American_band)" },  




  22. 
    { "@type" : "MusicGroup",  




  23. 
      "name" : "RadiationCity",  




  24. 
      "sameAs" : "http://en.wikipedia.org/wiki/Radiation_City" }],  




  25. 
  "offers" : {  




  26. 
    "@type" : "Offer",  




  27. 
    "availability" : "https://schema.org/LimitedAvailability",  




  28. 
    "priceCurrency": "USD",  




  29. 
    "price" : "13.00",  




  30. 
    "url" : "http://www.ticketfly.com/purchase/309433" },  




  31. 
  "typicalAgeRange" : "18+"  




  32. 
}  




  33. 
</script>




```

Structured representation of the JSON-LD example.
{ "@context" : "https://schema.org", "@type" : "Event", "name" : "Typhoon with Radiation City", "startDate" : "2013-09-14T21:30", "location" : { "@type" : "Place", "sameAs" : "http://www.hi-dive.com", "name" : "The Hi-Dive", "address" : { "@type" : "PostalAddress", "streetAddress" : "7 S. Broadway", "addressLocality" : "Denver", "addressRegion" : "CO", "postalCode" : "80209" } }, "performer" : [ { "@type" : "MusicGroup", "name" : "Typhoon", "sameAs" : "http://en.wikipedia.org/wiki/Typhoon_(American_band)" }, { "@type" : "MusicGroup", "name" : "RadiationCity", "sameAs" : "http://en.wikipedia.org/wiki/Radiation_City" }], "offers" : { "@type" : "Offer", "availability" : "https://schema.org/LimitedAvailability", "priceCurrency": "USD", "price" : "13.00", "url" : "http://www.ticketfly.com/purchase/309433" }, "typicalAgeRange" : "18+" }
![Copy to clipboard](https://schema.org/docs/clipboard/clippy.svg) [Example 8](https://schema.org/Offer#eg-0201 "Link: #eg-0201")
Copied
No Markup JSON-LD Structure
Example notes or example HTML without markup.

```

  1. An example snippet of JSON-LD describing two B.B. King concerts.


```

Example encoded as [JSON-LD](https://en.wikipedia.org/wiki/JSON-LD) in a HTML script tag.

```



  1. 
<script type="application/ld+json">  




  2. 
[{  




  3. 
  "@context" : "https://schema.org",  




  4. 
  "@type" : "MusicEvent",  




  5. 
  "name" : "B.B. King",  




  6. 
  "startDate" : "2014-04-12T19:30",  




  7. 
  "location" : {  




  8. 
     "@type" : "Place",  




  9. 
     "name" : "Lupo's Heartbreak Hotel",  




  10. 
     "address" : "79 Washington St., Providence, RI"  




  11. 
  },  




  12. 
  "offers" : {  




  13. 
     "@type" : "Offer",  




  14. 
     "url" : "https://www.etix.com/ticket/1771656"  




  15. 
  }  




  16. 
},  




  17. 
{  




  18. 
  "@context" : "https://schema.org",  




  19. 
  "@type" : "MusicEvent",  




  20. 
  "name" : "B.B. King",  




  21. 
  "startDate" : "2014-04-13T20:00",  




  22. 
  "location" : {  




  23. 
     "@type" : "Place",  




  24. 
     "name" : "Lynn Auditorium",  




  25. 
     "address" : "Lynn, MA, 01901"  




  26. 
  },  




  27. 
  "offers" : {  




  28. 
     "@type" : "Offer",  




  29. 
     "url" : "http://frontgatetickets.com/venue.php?id=11766"  




  30. 
  }  




  31. 
}]  




  32. 
</script>




```

Structured representation of the JSON-LD example.
[{ "@context" : "https://schema.org", "@type" : "MusicEvent", "name" : "B.B. King", "startDate" : "2014-04-12T19:30", "location" : { "@type" : "Place", "name" : "Lupo's Heartbreak Hotel", "address" : "79 Washington St., Providence, RI" }, "offers" : { "@type" : "Offer", "url" : "https://www.etix.com/ticket/1771656" } }, { "@context" : "https://schema.org", "@type" : "MusicEvent", "name" : "B.B. King", "startDate" : "2014-04-13T20:00", "location" : { "@type" : "Place", "name" : "Lynn Auditorium", "address" : "Lynn, MA, 01901" }, "offers" : { "@type" : "Offer", "url" : "http://frontgatetickets.com/venue.php?id=11766" } }]
![Copy to clipboard](https://schema.org/docs/clipboard/clippy.svg) [Example 9](https://schema.org/Offer#eg-0202 "Link: #eg-0202")
Copied
No Markup JSON-LD Structure
Example notes or example HTML without markup.

```



  1. 
An example of a more fully specified MusicEvent, including a tour image,  




  2. full venue address, multiple performers, and multiple ticket classes.



```

Example encoded as [JSON-LD](https://en.wikipedia.org/wiki/JSON-LD) in a HTML script tag.

```



  1. 
<script type="application/ld+json">  




  2. 
[{  




  3. 
    "@context" : "https://schema.org",  




  4. 
    "@type" : "MusicEvent",  




  5. 
    "name" : "B.B. King with Jonathon \"Boogie\" Long",  




  6. 
    "image" : "http://www.bbking.com/gallery/b-b-king-live.jpg",  




  7. 
    "url" : "http://www.bbking.com/events/apr12-providence.html",  




  8. 
    "startDate" : "2014-04-12T19:30",  




  9. 
    "doorTime" : "18:30:00",  




  10. 
    "endDate" : "2014-04-12T22:00",  




  11. 
    "location" : {  




  12. 
        "@type" : "Place",  




  13. 
        "name" : "Lupo's Heartbreak Hotel",  




  14. 
        "sameAs" : "http://lupos.com/",  




  15. 
        "address" : {  




  16. 
            "@type" : "PostalAddress",  




  17. 
            "streetAddress" : "79 Washington St.",  




  18. 
            "addressLocality" : "Providence",  




  19. 
            "addressRegion" : "RI",  




  20. 
            "postalCode" : "02903",  




  21. 
            "addressCountry" : "US"  




  22. 
        }  




  23. 
    },  




  24. 
    "offers" : [ {  




  25. 
        "@type" : "Offer",  




  26. 
        "name" : "General Admission",  




  27. 
        "priceCurrency": "USD",  




  28. 
        "price" : "63.25",  




  29. 
        "availability" : "SoldOut",  




  30. 
        "url" : "http://www.ticketmaster.com/event/17004C29"  




  31. 
    },{  




  32. 
        "@type" : "Offer",  




  33. 
        "name" : "VIP Experience",  




  34. 
        "url" : "http://www.example.com/Abcde12345",  




  35. 
        "priceCurrency": "USD",  




  36. 
        "price" : "299.00",  




  37. 
        "validFrom" : "2014-02-05T10:00",  




  38. 
        "validThrough" : "2014-03-19T23:59"  




  39. 
    } ],  




  40. 
    "performer" : [ {  




  41. 
        "@type" : "MusicGroup",  




  42. 
        "name" : "B.B. King",  




  43. 
        "sameAs" : "http://en.wikipedia.org/wiki/B.B._King"  




  44. 
    },{  




  45. 
        "@type" : "MusicGroup",  




  46. 
        "name" : "Jonathon \"Boogie\" Long",  




  47. 
        "sameAs" : "http://jonathonboogielong.com/"  




  48. 
    } ],  




  49. 
    "eventStatus" : "EventRescheduled",  




  50. 
    "previousStartDate" : "2013-09-30T19:30",  




  51. 
    "typicalAgeRange" : "18+"  




  52. 
}]  




  53. 
</script>




```

Structured representation of the JSON-LD example.
[{ "@context" : "https://schema.org", "@type" : "MusicEvent", "name" : "B.B. King with Jonathon \"Boogie\" Long", "image" : "http://www.bbking.com/gallery/b-b-king-live.jpg", "url" : "http://www.bbking.com/events/apr12-providence.html", "startDate" : "2014-04-12T19:30", "doorTime" : "18:30:00", "endDate" : "2014-04-12T22:00", "location" : { "@type" : "Place", "name" : "Lupo's Heartbreak Hotel", "sameAs" : "http://lupos.com/", "address" : { "@type" : "PostalAddress", "streetAddress" : "79 Washington St.", "addressLocality" : "Providence", "addressRegion" : "RI", "postalCode" : "02903", "addressCountry" : "US" } }, "offers" : [ { "@type" : "Offer", "name" : "General Admission", "priceCurrency": "USD", "price" : "63.25", "availability" : "SoldOut", "url" : "http://www.ticketmaster.com/event/17004C29" },{ "@type" : "Offer", "name" : "VIP Experience", "url" : "http://www.example.com/Abcde12345", "priceCurrency": "USD", "price" : "299.00", "validFrom" : "2014-02-05T10:00", "validThrough" : "2014-03-19T23:59" } ], "performer" : [ { "@type" : "MusicGroup", "name" : "B.B. King", "sameAs" : "http://en.wikipedia.org/wiki/B.B._King" },{ "@type" : "MusicGroup", "name" : "Jonathon \"Boogie\" Long", "sameAs" : "http://jonathonboogielong.com/" } ], "eventStatus" : "EventRescheduled", "previousStartDate" : "2013-09-30T19:30", "typicalAgeRange" : "18+" }]
![Copy to clipboard](https://schema.org/docs/clipboard/clippy.svg) [Example 10](https://schema.org/Offer#eg-0208 "Link: #eg-0208")
Copied
No Markup Microdata RDFa JSON-LD Structure
Example notes or example HTML without markup.

```



  1. 
<div>  




  2. 
  <!-- http://multivarki.ru?filters%5Bprice%5D%5BLTE%5D=39600 -->  




  3. 
  <span>315</span>  




  4. 
  <div>  




  5. 
    <img alt="Photo of product" src="http://img01.multivarki.ru.ru/c9/f1/a5fe6642-18d0-47ad-b038-6fca20f1c923.jpeg" />  




  6. 
    <a href="http://multivarki.ru/brand_502/">  




  7. 
      <span>BRAND 502</span>  




  8. 
    </a>  




  9. 
    <div>  




  10. 
      <span>4399 р.</span>  




  11. 
    </div>...  




  12. 
    <div>  




  13. 
    ...  




  14. 
    </div>  




  15. 
  </div>  




  16. 
</div>




```

Example encoded as [Microdata](https://en.wikipedia.org/wiki/Microdata_\(HTML\)) embedded in HTML.

```



  1. 
<div itemscope itemtype="https://schema.org/ItemList">  




  2. 
    <link itemprop="url" href="http://multivarki.ru?filters%5Bprice%5D%5BLTE%5D=39600"><span itemprop="numberOfItems">315</span>  




  3. 
    <div itemprop="itemListElement" itemscope itemtype="https://schema.org/Product">  




  4. 
        <img alt="Photo of product" itemprop="image" src="http://img01.multivarki.ru.ru/c9/f1/a5fe6642-18d0-47ad-b038-6fca20f1c923.jpeg"> <a itemprop="url" href="http://multivarki.ru/brand_502/"><span itemprop="name">BRAND 502</span></a>  




  5. 
        <div itemprop="offers" itemscope itemtype="https://schema.org/Offer">  




  6. 
            <meta property="priceCurrency" content="RUB">  




  7. 
            <span itemprop="price" content="4399.00">4399 р.</span>  




  8. 
        </div>...  




  9. 
    </div>  




  10. 
    <div itemprop="itemListElement" itemscope itemtype="https://schema.org/Product">  




  11. 
        ...  




  12. 
    </div>  




  13. 
</div>




```

Example encoded as [RDFa](https://en.wikipedia.org/wiki/RDFa) embedded in HTML.

```



  1. 
<div vocab="https://schema.org/" typeof="ItemList">  




  2. 
    <link property="url" href="http://multivarki.ru?filters%5Bprice%5D%5BLTE%5D=39600"><span property="numberOfItems">315</span>  




  3. 
    <div property="itemListElement" typeof="Product">  




  4. 
        <img property="image" alt="Photo of product" src="http://img01.multivarki.ru.ru/c9/f1/a5fe6642-18d0-47ad-b038-6fca20f1c923.jpeg"> <a property="url" href="http://multivarki.ru/brand_502/"><span property="name">BRAND 502</span></a>  




  5. 
        <div property="offers" typeof="Offer">  




  6. 
            <meta property="priceCurrency" content="RUB">руб  




  7. 
            <meta property="price" content="4399.00">4 399,00  




  8. 
            <link property="itemCondition" href="https://schema.org/NewCondition">  




  9. 
        </div>...  




  10. 
    </div>  




  11. 
    <div property="itemListElement" typeof="Product">  




  12. 
        ...  




  13. 
    </div>  




  14. 
</div>




```

Example encoded as [JSON-LD](https://en.wikipedia.org/wiki/JSON-LD) in a HTML script tag.

```



  1. 
<script type="application/ld+json">  




  2. 
{  




  3. 
    "@context": "https://schema.org",  




  4. 
    "@type": "ItemList",  




  5. 
    "url": "http://multivarki.ru?filters%5Bprice%5D%5BLTE%5D=39600",  




  6. 
    "numberOfItems": "315",  




  7. 
    "itemListElement": [  




  8. 
        {  




  9. 
            "@type": "Product",  




  10. 
            "image": "http://img01.multivarki.ru.ru/c9/f1/a5fe6642-18d0-47ad-b038-6fca20f1c923.jpeg",  




  11. 
            "url": "http://multivarki.ru/brand_502/",  




  12. 
            "name": "Brand 502",  




  13. 
            "offers": {  




  14. 
                "@type": "Offer",  




  15. 
                "priceCurrency": "RUB",  




  16. 
                "price": "4399.00"  




  17. 
            }  




  18. 
        },  




  19. 
        {  




  20. 
            "@type": "Product",  




  21. 
            "name": "..."  




  22. 
        }  




  23. 
    ]  




  24. 
}  




  25. 
</script>




```

Structured representation of the JSON-LD example.
{ "@context": "https://schema.org", "@type": "ItemList", "url": "http://multivarki.ru?filters%5Bprice%5D%5BLTE%5D=39600", "numberOfItems": "315", "itemListElement": [ { "@type": "Product", "image": "http://img01.multivarki.ru.ru/c9/f1/a5fe6642-18d0-47ad-b038-6fca20f1c923.jpeg", "url": "http://multivarki.ru/brand_502/", "name": "Brand 502", "offers": { "@type": "Offer", "priceCurrency": "RUB", "price": "4399.00" } }, { "@type": "Product", "name": "..." } ] }
![Copy to clipboard](https://schema.org/docs/clipboard/clippy.svg) [Example 11](https://schema.org/Offer#eg-0393 "Link: #eg-0393")
Copied
No Markup Microdata RDFa JSON-LD Structure
Example notes or example HTML without markup.

```



  1. 
<!-- Uses both the "Book" and "Product" item types to support Offer relationships -->  




  2. 
  




  3. 
 <div>  




  4. 
   <h3>Le concerto</h3>  




  5. 
   <div>  




  6. 
       Bibliographic Details  




  7. 
       <table>  




  8. 
         <tr>  




  9. 
           <th>Main Author: </th>  




  10. 
           <td>Ferchault, Guy</td>  




  11. 
         </tr>  




  12. 
       </table>  




  13. 
   </div>  




  14. 
 </div>  




  15. 
  




  16. 
 <div>  




  17. 
     Holdings details from Anytown City Library  




  18. 
     <table>  




  19. 
       <!-- Example of a copy available for loan -->  




  20. 
       <tr>  




  21. 
         <th>Copy </th>  




  22. 
         <td>Available  




  23. 
           <div>Barcode: <span>CONC91000937</span></div>  




  24. 
           <div>Call number: <span>780 R2</span></div>  




  25. 
           <div>Library: <span>Anytown City Library</span></div>  




  26. 
         </td>  




  27. 
       </tr>  




  28. 
     <table>  




  29. 
 </div>




```

Example encoded as [Microdata](https://en.wikipedia.org/wiki/Microdata_\(HTML\)) embedded in HTML.

```



  1. 
 <!-- Uses both the "Book" and "Product" item types to support Offer relationships -->  




  2. 
  




  3. 
 <div itemscope itemtype="https://schema.org/Book" itemid="#record">  




  4. 
   <link itemprop="additionalType" href="https://schema.org/Product"/>  




  5. 
   <h3 itemprop="name">Le concerto</h3>  




  6. 
   <div>  




  7. 
       Bibliographic Details  




  8. 
       <table>  




  9. 
         <tr>  




  10. 
           <th>Main Author: </th>  




  11. 
           <td itemprop="author">Ferchault, Guy</td>  




  12. 
         </tr>  




  13. 
       </table>  




  14. 
   </div>  




  15. 
 </div>  




  16. 
  




  17. 
 <div>  




  18. 
     Holdings details from Anytown City Library  




  19. 
     <table>  




  20. 
       <!-- Example of a copy available for loan -->  




  21. 
       <tr itemscope itemtype="https://schema.org/Offer">  




  22. 
         <th>Copy </th>  




  23. 
         <td>Available  




  24. 
           <link itemprop="availability" href="https://schema.org/InStock">  




  25. 
           <div>Barcode: <span itemprop="serialNumber">CONC91000937</span></div>  




  26. 
           <div>Call number: <span itemprop="sku">780 R2</span></div>  




  27. 
           <div>Library: <span itemprop="offeredBy" itemscope itemtype="https://schema.org/Library" itemid="http://library.anytown.gov.uk" >Anytown City Library</span></div>  




  28. 
           <link itemprop="businessFunction" href="http://purl.org/goodrelations/v1#LeaseOut">  




  29. 
           <link itemprop="itemOffered" href="#record">  




  30. 
         </td>  




  31. 
       </tr>  




  32. 
     </table>  




  33. 
 </div>




```

Example encoded as [RDFa](https://en.wikipedia.org/wiki/RDFa) embedded in HTML.

```



  1. 
 <!-- Uses both the "Book" and "Product" item types to support Offer relationships -->  




  2. 
<div vocab="https://schema.org/" resource="#record" typeof="Book Product">  




  3. 
    <h3 property="name">  




  4. 
        Le concerto  




  5. 
    </h3>  




  6. 
    <div>  




  7. 
        Bibliographic Details  




  8. 
        <table>  




  9. 
            <tr>  




  10. 
                <th>  




  11. 
                    Main Author:  




  12. 
                </th>  




  13. 
                <td property="author">  




  14. 
                    Ferchault, Guy  




  15. 
                </td>  




  16. 
            </tr>  




  17. 
        </table>  




  18. 
    </div>  




  19. 
</div>  




  20. 
<div>  




  21. 
    Holdings details from Anytown City Library  




  22. 
    <table vocab="https://schema.org/">  




  23. 
        <!-- Example of a copy available for loan -->  




  24. 
        <tr typeof="Offer">  




  25. 
            <th>  




  26. 
                Copy  




  27. 
            </th>  




  28. 
            <td>  




  29. 
                Available  




  30. 
                <div>  




  31. 
                    Barcode: <span property="serialNumber">CONC91000937</span>  




  32. 
                </div>  




  33. 
                <div>  




  34. 
                    Call number: <span property="sku">780 R2</span>  




  35. 
                </div>  




  36. 
                <div>  




  37. 
                    Library: <span property="offeredBy" typeof="Library" resource="http://library.anytown.gov.uk">Anytown City Library</span>  




  38. 
                </div>  




  39. 
            </td>  




  40. 
        </tr>  




  41. 
    </table>  




  42. 
</div>




```

Example encoded as [JSON-LD](https://en.wikipedia.org/wiki/JSON-LD) in a HTML script tag.

```



  1. 
<script type="application/ld+json">  




  2. 
{  




  3. 
  "@context":  "https://schema.org/",  




  4. 
  "@id": "#record",  




  5. 
  "@type": "Book",  




  6. 
  "additionalType": "Product",  




  7. 
  "name": "Le concerto",  




  8. 
  "author": "Ferchault, Guy",  




  9. 
  "offers":{  




  10. 
      "@type": "Offer",  




  11. 
      "availability": "https://schema.org/InStock",  




  12. 
      "serialNumber": "CONC91000937",  




  13. 
      "sku": "780 R2",  




  14. 
      "offeredBy": {  




  15. 
          "@type": "Library",  




  16. 
          "@id": "http://library.anytown.gov.uk",  




  17. 
          "name": "Anytown City Library"  




  18. 
      },  




  19. 
      "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",  




  20. 
      "itemOffered": "#record"  




  21. 
    }  




  22. 
}  




  23. 
</script>




```

Structured representation of the JSON-LD example.
{ "@context": "https://schema.org/", "@id": "#record", "@type": "Book", "additionalType": "Product", "name": "Le concerto", "author": "Ferchault, Guy", "offers":{ "@type": "Offer", "availability": "https://schema.org/InStock", "serialNumber": "CONC91000937", "sku": "780 R2", "offeredBy": { "@type": "Library", "@id": "http://library.anytown.gov.uk", "name": "Anytown City Library" }, "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "itemOffered": "#record" } }
![Copy to clipboard](https://schema.org/docs/clipboard/clippy.svg) [Example 12](https://schema.org/Offer#eg-0394 "Link: #eg-0394")
Copied
No Markup RDFa JSON-LD Structure
Example notes or example HTML without markup.

```



  1. 
<body>  




  2. 
  <main>  




  3. 
    <article>  




  4. 
      <h1>  




  5. 
         <a href="http://example.com/explosive-tennis-balls">Explosive tennis balls</a>  




  6. 
      </h1>  




  7. 
      <img alt="Explosive tennis balls" title src="http://example.com/explosive-tennis-balls.jpg" />  




  8. 
      <p >  




  9. 
        $29.99 - In stock  




  10. 
      </p>  




  11. 
      <p >  




  12. 
        Tickle your friends!<br />  




  13. 
        Surprise your opponent!  




  14. 
      <p>  




  15. 
    </article>  




  16. 
  </main>  




  17. 
  <footer>  




  18. 
    <p>  




  19. 
      © <span>2015</span> - <span property="name">Acme Inc</span>  




  20. 
    </p>  




  21. 
    <ul>  




  22. 
      <li><a href="https://twitter.com/AcmeInc">Twitter</a></li>  




  23. 
      <li><a href="https://www.facebook.com/AcmeInc">Facebook</a></li>  




  24. 
      <li><a href="https://plus.google.com/u/0/+AcmeInc/">Google+</a></li>  




  25. 
    </ul>  




  26. 
  </footer>  




  27. 
</body>




```

Example encoded as [RDFa](https://en.wikipedia.org/wiki/RDFa) embedded in HTML.

```



  1. 
<body vocab="https://schema.org/" resource="http://example.com/explosive-tennis-balls" typeof="ItemPage">  




  2. 
  <link property="copyrightHolder publisher" href="#Organization" />  




  3. 
  <main>  




  4. 
    <article resource="#Product" property="mainEntity" typeof="Product">  




  5. 
      <h1 property="name">  




  6. 
         <a property="url" href="http://example.com/explosive-tennis-balls">Explosive tennis balls</a>  




  7. 
      </h1>  




  8. 
      <img property="image" alt="Explosive tennis balls" title src="http://example.com/explosive-tennis-balls.jpg" />  




  9. 
      <p resource="#Offer" property="offers" typeof="Offer">  




  10. 
        <meta property="priceCurrency" content="USD" />  




  11. 
        <meta property="price" content="1000.00" />  




  12. 
        <link property="availability" href="https://schema.org/InStock" />  




  13. 
        <link property="itemOffered" href="#Product" />  




  14. 
        <link property="businessFunction" href="http://purl.org/goodrelations/v1#Sell" />  




  15. 
        <link rev="makesOffer" href="#Organization" />  




  16. 
        $29.99 - In stock  




  17. 
      </p>  




  18. 
      <p property="description">  




  19. 
        Tickle your friends!<br />  




  20. 
        Surprise your opponent!  




  21. 
      <p>  




  22. 
    </article>  




  23. 
  </main>  




  24. 
  <footer>  




  25. 
    <p resource="#Organization" typeof="Organization">  




  26. 
      © <span resource="#CopyrightYear" typeof="rdfa:Pattern">2015</span> - <span property="name">Acme Inc</span>  




  27. 
      <link property="logo" href="http://example.com/acme-inc-logo.jpg" />  




  28. 
      <link property="url" href="http://example.com" />  




  29. 
      <link property="rdfa:copy" href="#SameAsResource"/>  




  30. 
    </p>  




  31. 
    <ul resource="#SameAsResource" typeof="rdfa:Pattern">  




  32. 
      <li><a property="sameAs" href="https://twitter.com/AcmeInc">Twitter</a></li>  




  33. 
      <li><a property="sameAs" href="https://www.facebook.com/AcmeInc">Facebook</a></li>  




  34. 
      <li><a property="sameAs" href="https://plus.google.com/u/0/+AcmeInc/">Google+</a></li>  




  35. 
    </ul>  




  36. 
  </footer>  




  37. 
</body>




```

Example encoded as [JSON-LD](https://en.wikipedia.org/wiki/JSON-LD) in a HTML script tag.

```



  1. 
<script type="application/ld+json">  




  2. 
{  




  3. 
  "@context":"https://schema.org",  




  4. 
  "@id":"http://example.com/explosive-tennis-balls",  




  5. 
  "@type":"ItemPage",  




  6. 
  "copyrightYear":"2015",  




  7. 
  "copyrightHolder":{"@id":"#Organization"},  




  8. 
  "publisher":{"@id":"#Organization"},  




  9. 
  "mainEntity":{  




  10. 
    "@id":"#Product",  




  11. 
    "@type":"Product",  




  12. 
    "name":"Explosive tennis balls",  




  13. 
    "description":"Tickle your friends! Surprise your opponent!",  




  14. 
    "image":"http://example.com/explosive-tennis-balls.jpg",  




  15. 
    "url":"http://example.com/explosive-tennis-balls",  




  16. 
    "offers":{  




  17. 
      "@id":"#Offer",  




  18. 
      "@type":"Offer",  




  19. 
      "priceCurrency":"USD",  




  20. 
      "price":"1000.00",  




  21. 
      "availability":"https://schema.org/InStock",  




  22. 
      "itemOffered":{"@id":"#Product"},  




  23. 
        "offeredBy":{  




  24. 
          "@id":"#Organization",  




  25. 
          "@type":"Organization",  




  26. 
          "name":"Acme Inc",  




  27. 
          "logo":"http://example.commple.com/acme-inc-logo.jpg",  




  28. 
          "url":"http://example.com/",  




  29. 
          "sameAs":["https://twitter.com/AcmeInc","https://www.facebook.com/AcmeInc","https://plus.google.com/u/0/+AcmeInc/"]  




  30. 
        }  




  31. 
    }  




  32. 
  }  




  33. 
}  




  34. 
</script>




```

Structured representation of the JSON-LD example.
{ "@context":"https://schema.org", "@id":"http://example.com/explosive-tennis-balls", "@type":"ItemPage", "copyrightYear":"2015", "copyrightHolder":{"@id":"#Organization"}, "publisher":{"@id":"#Organization"}, "mainEntity":{ "@id":"#Product", "@type":"Product", "name":"Explosive tennis balls", "description":"Tickle your friends! Surprise your opponent!", "image":"http://example.com/explosive-tennis-balls.jpg", "url":"http://example.com/explosive-tennis-balls", "offers":{ "@id":"#Offer", "@type":"Offer", "priceCurrency":"USD", "price":"1000.00", "availability":"https://schema.org/InStock", "itemOffered":{"@id":"#Product"}, "offeredBy":{ "@id":"#Organization", "@type":"Organization", "name":"Acme Inc", "logo":"http://example.commple.com/acme-inc-logo.jpg", "url":"http://example.com/", "sameAs":["https://twitter.com/AcmeInc","https://www.facebook.com/AcmeInc","https://plus.google.com/u/0/+AcmeInc/"] } } } }
![Copy to clipboard](https://schema.org/docs/clipboard/clippy.svg) [Example 13](https://schema.org/Offer#eg-0396 "Link: #eg-0396")
Copied
No Markup Microdata RDFa JSON-LD Structure
Example notes or example HTML without markup.

```



  1. 
ACME Home Cleaning offers a variety of services in Massachusetts, including:  




  2. 
<ul>  




  3. 
  <li>House cleaning</li>  




  4. 
  <ul>  




  5. 
    <li>Apartment light cleaning</li>  




  6. 
    <li>House light cleaning up to 2 bedrooms</li>  




  7. 
    <li>House light cleaning 3+ bedrooms</li>  




  8. 
  </ul>  




  9. 
  <li>One-time services</li>  




  10. 
  <ul>  




  11. 
    <li>Window washing</li>  




  12. 
    <li>Carpet deep cleaning</li>  




  13. 
    <li>Move in/out cleaning</li>  




  14. 
  </ul>  




  15. 
</ul>




```

Example encoded as [Microdata](https://en.wikipedia.org/wiki/Microdata_\(HTML\)) embedded in HTML.

```



  1. 
<div itemscope itemtype="https://schema.org/Service">  




  2. 
  <meta itemprop="serviceType" content="Home cleaning" />  




  3. 
  <span itemprop="provider" itemscope itemtype="https://schema.org/LocalBusiness">  




  4. 
    <span itemprop="name">ACME Home Cleaning</span>  




  5. 
  </span>  




  6. 
  offers a variety of services in  




  7. 
  <span itemprop="areaServed" itemscope itemtype="https://schema.org/State">  




  8. 
    <span itemprop="name">Massachusetts</span>, including  




  9. 
  </span>  




  10. 
  <ul itemprop="hasOfferCatalog" itemscope itemtype="https://schema.org/OfferCatalog">  




  11. 
    <li itemprop="itemListElement" itemscope itemtype="https://schema.org/OfferCatalog">  




  12. 
      <span itemprop="name">House cleaning</span>  




  13. 
      <ul itemprop="itemListElement" itemscope itemtype="https://schema.org/OfferCatalog">  




  14. 
        <li itemprop="itemListElement" itemscope itemtype="https://schema.org/Offer">  




  15. 
          <div itemprop="itemOffered" itemscope itemtype="https://schema.org/Service">  




  16. 
            <span itemprop="name">Apartment light cleaning</span>  




  17. 
          </div>  




  18. 
        </li>  




  19. 
        <li itemprop="itemListElement" itemscope itemtype="https://schema.org/Offer">  




  20. 
          <div itemprop="itemOffered" itemscope itemtype="https://schema.org/Service">  




  21. 
            <span itemprop="name">House light cleaning up to 2 bedrooms</span>  




  22. 
          </div>  




  23. 
        </li>  




  24. 
        <li itemprop="itemListElement" itemscope itemtype="https://schema.org/Offer">  




  25. 
          <div itemprop="itemOffered" itemscope itemtype="https://schema.org/Service">  




  26. 
            <span itemprop="name">House light cleaning 3+ bedrooms</span>  




  27. 
          </div>  




  28. 
        </li>  




  29. 
      </ul>  




  30. 
    <li itemprop="itemListElement" itemscope itemtype="https://schema.org/OfferCatalog">  




  31. 
      <span itemprop="name">One-time services</span>  




  32. 
      <ul itemprop="itemListElement" itemscope itemtype="https://schema.org/OfferCatalog">  




  33. 
        <li itemprop="itemListElement" itemscope itemtype="https://schema.org/Offer">  




  34. 
          <div itemprop="itemOffered" itemscope itemtype="https://schema.org/Service">  




  35. 
            <span itemprop="name">Window washing</span>  




  36. 
          </div>  




  37. 
        </li>  




  38. 
        <li itemprop="itemListElement" itemscope itemtype="https://schema.org/Offer">  




  39. 
          <div itemprop="itemOffered" itemscope itemtype="https://schema.org/Service">  




  40. 
            <span itemprop="name">Carpet deep cleaning</span>  




  41. 
          </div>  




  42. 
        </li>  




  43. 
        <li itemprop="itemListElement" itemscope itemtype="https://schema.org/Offer">  




  44. 
          <div itemprop="itemOffered" itemscope itemtype="https://schema.org/Service">  




  45. 
            <span itemprop="name">Move in/out cleaning</span>  




  46. 
          </div>  




  47. 
        </li>  




  48. 
      </ul>  




  49. 
    </li>  




  50. 
  </ul>  




  51. 
</div>




```

Example encoded as [RDFa](https://en.wikipedia.org/wiki/RDFa) embedded in HTML.

```



  1. 
<div vocab="https://schema.org/" typeof="Service">  




  2. 
  <meta property="serviceType" content="Home cleaning" />  




  3. 
  <span property="provider" typeof="LocalBusiness">  




  4. 
    <span property="name">ACME Home Cleaning</span>  




  5. 
  </span>  




  6. 
  offers a variety of services in  




  7. 
  <span property="areaServed" typeof="State">  




  8. 
    <span property="name">Massachusetts</span>, including  




  9. 
  </span>  




  10. 
  <ul property="hasOfferCatalog" typeof="OfferCatalog">  




  11. 
    <li property="itemListElement" typeof="OfferCatalog">  




  12. 
      <span property="name">House cleaning</span>  




  13. 
      <ul property="itemListElement" typeof="OfferCatalog">  




  14. 
        <li property="itemListElement" typeof="Offer">  




  15. 
          <div property="itemOffered" typeof="Service">  




  16. 
            <span property="name">Apartment light cleaning</span>  




  17. 
          </div>  




  18. 
        </li>  




  19. 
        <li property="itemListElement" typeof="Offer">  




  20. 
          <div property="itemOffered" typeof="Service">  




  21. 
            <span property="name">House light cleaning up to 2 bedrooms</span>  




  22. 
          </div>  




  23. 
        </li>  




  24. 
        <li property="itemListElement" typeof="Offer">  




  25. 
          <div property="itemOffered" typeof="Service">  




  26. 
            <span property="name">House light cleaning 3+ bedrooms</span>  




  27. 
          </div>  




  28. 
        </li>  




  29. 
      </ul>  




  30. 
    <li property="itemListElement" typeof="OfferCatalog">  




  31. 
      <span property="name">One-time services</span>  




  32. 
      <ul property="itemListElement" typeof="OfferCatalog">  




  33. 
        <li property="itemListElement" typeof="Offer">  




  34. 
          <div property="itemOffered" typeof="Service">  




  35. 
            <span property="name">Window washing</span>  




  36. 
          </div>  




  37. 
        </li>  




  38. 
        <li property="itemListElement" typeof="Offer">  




  39. 
          <div property="itemOffered" typeof="Service">  




  40. 
            <span property="name">Carpet deep cleaning</span>  




  41. 
          </div>  




  42. 
        </li>  




  43. 
        <li property="itemListElement" typeof="Offer">  




  44. 
          <div property="itemOffered" typeof="Service">  




  45. 
            <span property="name">Move in/out cleaning</span>  




  46. 
          </div>  




  47. 
        </li>  




  48. 
      </ul>  




  49. 
    </li>  




  50. 
  </ul>  




  51. 
</div>




```

Example encoded as [JSON-LD](https://en.wikipedia.org/wiki/JSON-LD) in a HTML script tag.

```



  1. 
<script type="application/ld+json">  




  2. 
{  




  3. 
  "@context": "https://schema.org/",  




  4. 
  "@type": "Service",  




  5. 
  "serviceType": "Weekly home cleaning",  




  6. 
  "provider": {  




  7. 
    "@type": "LocalBusiness",  




  8. 
    "name": "ACME Home Cleaning"  




  9. 
  },  




  10. 
  "areaServed": {  




  11. 
    "@type": "State",  




  12. 
    "name": "Massachusetts"  




  13. 
  },  




  14. 
  "hasOfferCatalog": {  




  15. 
    "@type": "OfferCatalog",  




  16. 
    "name": "Cleaning services",  




  17. 
    "itemListElement": [  




  18. 
      {  




  19. 
        "@type": "OfferCatalog",  




  20. 
        "name": "House Cleaning",  




  21. 
        "itemListElement": [  




  22. 
          {  




  23. 
            "@type": "Offer",  




  24. 
            "itemOffered": {  




  25. 
              "@type": "Service",  




  26. 
              "name": "Apartment light cleaning"  




  27. 
            }  




  28. 
          },  




  29. 
          {  




  30. 
            "@type": "Offer",  




  31. 
            "itemOffered": {  




  32. 
              "@type": "Service",  




  33. 
              "name": "House light cleaning up to 2 bedrooms"  




  34. 
            }  




  35. 
          },  




  36. 
          {  




  37. 
            "@type": "Offer",  




  38. 
            "itemOffered": {  




  39. 
              "@type": "Service",  




  40. 
              "name": "House light cleaning 3+ bedrooms"  




  41. 
            }  




  42. 
          }  




  43. 
        ]  




  44. 
      },  




  45. 
      {  




  46. 
        "@type": "OfferCatalog",  




  47. 
        "name": "One-time services",  




  48. 
        "itemListElement": [  




  49. 
          {  




  50. 
            "@type": "Offer",  




  51. 
            "itemOffered": {  




  52. 
              "@type": "Service",  




  53. 
              "name": "Window washing"  




  54. 
            }  




  55. 
          },  




  56. 
          {  




  57. 
            "@type": "Offer",  




  58. 
            "itemOffered": {  




  59. 
              "@type": "Service",  




  60. 
              "name": "Carpet cleaning"  




  61. 
            }  




  62. 
          },  




  63. 
          {  




  64. 
            "@type": "Offer",  




  65. 
            "itemOffered": {  




  66. 
              "@type": "Service",  




  67. 
              "name": "Move in/out cleaning"  




  68. 
            }  




  69. 
          }  




  70. 
        ]  




  71. 
      }  




  72. 
    ]  




  73. 
  }  




  74. 
}  




  75. 
</script>




```

Structured representation of the JSON-LD example.
{ "@context": "https://schema.org/", "@type": "Service", "serviceType": "Weekly home cleaning", "provider": { "@type": "LocalBusiness", "name": "ACME Home Cleaning" }, "areaServed": { "@type": "State", "name": "Massachusetts" }, "hasOfferCatalog": { "@type": "OfferCatalog", "name": "Cleaning services", "itemListElement": [ { "@type": "OfferCatalog", "name": "House Cleaning", "itemListElement": [ { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Apartment light cleaning" } }, { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "House light cleaning up to 2 bedrooms" } }, { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "House light cleaning 3+ bedrooms" } } ] }, { "@type": "OfferCatalog", "name": "One-time services", "itemListElement": [ { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Window washing" } }, { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Carpet cleaning" } }, { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Move in/out cleaning" } } ] } ] } }
![Copy to clipboard](https://schema.org/docs/clipboard/clippy.svg) [Example 14](https://schema.org/Offer#eg-0397 "Link: #eg-0397")
Copied
No Markup Microdata RDFa JSON-LD Structure
Example notes or example HTML without markup.

```



  1. 
Joes' Pizza  




  2. 
123 Main Street  




  3. 
Cambridge, MA 02142  




  4. delivers within 5 km of its store with a minimum order of $20.



```

Example encoded as [Microdata](https://en.wikipedia.org/wiki/Microdata_\(HTML\)) embedded in HTML.

```



  1. 
<div itemscope itemtype="https://schema.org/FoodEstablishment">  




  2. 
  <span itemprop="name">Joe's Pizza</span>  




  3. 
  <div itemprop="location" itemscope itemtype="https://schema.org/PostalAddress">  




  4. 
    <span itemprop="streetAddress">123 Main Street</span>  




  5. 
    <span itemprop="addressLocality">Cambridge</span>  




  6. 
    <span itemprop="addressRegion">MA</span>  




  7. 
    <span itemprop="postalCode">02142</span>  




  8. 
  </div>  




  9. 
  delivers within 5 km of its store  




  10. 
  <div itemprop="makesOffer" itemscope itemtype="https://schema.org/Offer">  




  11. 
    <div itemprop="eligibleRegion" itemscope itemtype="https://schema.org/GeoCircle">  




  12. 
      <div itemprop="address" itemscope itemtype="https://schema.org/PostalAddress">  




  13. 
        <meta itemprop="streetAddress" content="123 Main Street" />  




  14. 
        <meta itemprop="addressLocality" content="Cambridge" />  




  15. 
        <meta itemprop="addressRegion" content="MA" />  




  16. 
        <meta itemprop="postalCode" content="02142" />  




  17. 
      </div>  




  18. 
      <meta itemprop="geoRadius" content="5000" />  




  19. 
    </div>  




  20. 
  




  21. 
    with a minimum order of $20.  




  22. 
    <div itemprop="priceSpecification" itemscope itemtype="https://schema.org/DeliveryChargeSpecification">  




  23. 
      <meta itemprop="appliesToDeliveryMethod" link="http://purl.org/goodrelations/v1#DeliveryModeOwnFleet">  




  24. 
      <div itemprop="eligibleTransactionVolume" itemscope itemtype="https://schema.org/PriceSpecification">  




  25. 
        <meta itemprop="price" content="20.00" />  




  26. 
        <meta itemprop="priceCurrency" content="USD" />  




  27. 
      </div>  




  28. 
    </div>  




  29. 
  </div>  




  30. 
</div>




```

Example encoded as [RDFa](https://en.wikipedia.org/wiki/RDFa) embedded in HTML.

```



  1. 
<div vocab="https://schema.org/" typeof="FoodEstablishment">  




  2. 
  <span property="name">Joe's Pizza</span>  




  3. 
  <div property="location" typeof="PostalAddress">  




  4. 
    <span property="streetAddress">123 Main Street</span>  




  5. 
    <span property="addressLocality">Cambridge</span>  




  6. 
    <span property="addressRegion">MA</span>  




  7. 
    <span property="postalCode">02142</span>  




  8. 
  </div>  




  9. 
  delivers within 5 km of its store with a minimum order of $20.  




  10. 
  <div property="makesOffer" typeof="Offer">  




  11. 
    <div property="priceSpecification" typeof="DeliveryChargeSpecification">  




  12. 
      <meta property="appliesToDeliveryMethod" link="http://purl.org/goodrelations/v1#DeliveryModeOwnFleet">  




  13. 
      <div property="eligibleTransactionVolume" typeof="PriceSpecification">  




  14. 
        <meta property="price" content="20.00" />  




  15. 
        <meta property="priceCurrency" content="USD" />  




  16. 
      </div>  




  17. 
      <div property="eligibleRegion" typeof="GeoCircle">  




  18. 
        <div property="address" typeof="PostalAddress">  




  19. 
          <meta property="streetAddress" content="123 Main Street" />  




  20. 
          <meta property="addressLocality" content="Cambridge" />  




  21. 
          <meta property="addressRegion" content="MA" />  




  22. 
          <meta property="postalCode" content="02142" />  




  23. 
        </div>  




  24. 
        <meta property="geoRadius" content="5000" />  




  25. 
      </div>  




  26. 
    </div>  




  27. 
  </div>  




  28. 
</div>




```

Example encoded as [JSON-LD](https://en.wikipedia.org/wiki/JSON-LD) in a HTML script tag.

```



  1. 
<script type="application/ld+json">  




  2. 
  {  




  3. 
    "@context": "https://schema.org/",  




  4. 
    "@type": "FoodEstablishment",  




  5. 
    "name": "Joe's Pizza",  




  6. 
    "location": {  




  7. 
      "@type": "PostalAddress",  




  8. 
      "@id": "http://example.com/address",  




  9. 
      "streetAddress": "123 Main Street",  




  10. 
      "addressLocality": "Cambridge",  




  11. 
      "addressRegion": "MA",  




  12. 
      "postalCode": "02142"  




  13. 
    },  




  14. 
    "makesOffer": {  




  15. 
      "@type": "Offer",  




  16. 
      "priceSpecification": {  




  17. 
        "@type": "DeliveryChargeSpecification",  




  18. 
        "appliesToDeliveryMethod": "http://purl.org/goodrelations/v1#DeliveryModeOwnFleet",  




  19. 
        "eligibleTransactionVolume": {  




  20. 
          "@type": "PriceSpecification",  




  21. 
          "price": "20.00",  




  22. 
          "priceCurrency": "USD"  




  23. 
        },  




  24. 
        "eligibleRegion": {  




  25. 
          "@type": "GeoCircle",  




  26. 
          "address": {  




  27. 
            "@id": "http://www.example.com/address"  




  28. 
          },  




  29. 
          "geoRadius": "5000"  




  30. 
        }  




  31. 
      }  




  32. 
    }  




  33. 
  }  




  34. 
</script>




```

Structured representation of the JSON-LD example.
{ "@context": "https://schema.org/", "@type": "FoodEstablishment", "name": "Joe's Pizza", "location": { "@type": "PostalAddress", "@id": "http://example.com/address", "streetAddress": "123 Main Street", "addressLocality": "Cambridge", "addressRegion": "MA", "postalCode": "02142" }, "makesOffer": { "@type": "Offer", "priceSpecification": { "@type": "DeliveryChargeSpecification", "appliesToDeliveryMethod": "http://purl.org/goodrelations/v1#DeliveryModeOwnFleet", "eligibleTransactionVolume": { "@type": "PriceSpecification", "price": "20.00", "priceCurrency": "USD" }, "eligibleRegion": { "@type": "GeoCircle", "address": { "@id": "http://www.example.com/address" }, "geoRadius": "5000" } } } }
![Copy to clipboard](https://schema.org/docs/clipboard/clippy.svg) [Example 15](https://schema.org/Offer#eg-0462 "Link: #eg-0462")
Copied
No Markup Microdata RDFa JSON-LD Structure
Example notes or example HTML without markup.

```



  1. 
<a href="category/books.html">Books</a> >  




  2. 
 <a href="category/books-literature.html">Literature &amp; Fiction</a> >  




  3. 
 <a href="category/books-classics">Classics</a>  




  4. 
  




  5. 
<img src="catcher-in-the-rye-book-cover.jpg"  




  6. 
  alt="cover art: red horse, city in background"/>  




  7. 
The Catcher in the Rye - Mass Market Paperback  




  8. 
by <a href="/author/jd_salinger.html">J.D. Salinger</a>  




  9. 
4 stars - 3077 reviews  




  10. 
  




  11. 
Price: $6.99  




  12. 
In Stock  




  13. 
  




  14. 
Product details  




  15. 
224 pages  




  16. 
Publisher: Little, Brown, and Company - May 1, 1991  




  17. 
Language: English  




  18. 
ISBN-10: 0316769487  




  19. 
  




  20. 
Reviews:  




  21. 
  




  22. 
5 stars - <b>"A masterpiece of literature" </b>  




  23. 
by John Doe. Written on May 4, 2006  




  24. 
I really enjoyed this book. It captures the essential challenge people face  




  25. 
as they try make sense of their lives and grow to adulthood.  




  26. 
  




  27. 
4 stars - <b>"love it LOLOL111!" </b>  




  28. 
by Bob Smith, Written on June 15, 2006  




  29. Catcher in the Rye is a fun book. It's a good book to read.



```

Example encoded as [Microdata](https://en.wikipedia.org/wiki/Microdata_\(HTML\)) embedded in HTML.

```



  1. 
<body itemscope itemtype="https://schema.org/WebPage">  




  2. 
...  




  3. 
<div itemprop="breadcrumb">  




  4. 
  <a href="category/books.html">Books</a> >  




  5. 
  <a href="category/books-literature.html">Literature &amp; Fiction</a> >  




  6. 
  <a href="category/books-classics">Classics</a>  




  7. 
</div>  




  8. 
  




  9. 
<div itemprop="mainEntity" itemscope itemtype="https://schema.org/Book">  




  10. 
  




  11. 
<img itemprop="image" src="catcher-in-the-rye-book-cover.jpg"  




  12. 
     alt="cover art: red horse, city in background"/>  




  13. 
<span itemprop="name">The Catcher in the Rye</span> -  




  14. 
 <link itemprop="bookFormat" href="https://schema.org/Paperback">Mass Market Paperback  




  15. 
by <a itemprop="author" href="/author/jd_salinger.html">J.D. Salinger</a>  




  16. 
  




  17. 
<div itemprop="aggregateRating" itemscope itemtype="https://schema.org/AggregateRating">  




  18. 
  <span itemprop="ratingValue">4</span> stars -  




  19. 
  <span itemprop="reviewCount">3077</span> reviews  




  20. 
</div>  




  21. 
  




  22. 
<div itemprop="offers" itemscope itemtype="https://schema.org/Offer">  




  23. 
  Price: $<span itemprop="price">6.99</span>  




  24. 
  <meta itemprop="priceCurrency" content="USD" />  




  25. 
  <link itemprop="availability" href="https://schema.org/InStock">In Stock  




  26. 
</div>  




  27. 
  




  28. 
Product details  




  29. 
<span itemprop="numberOfPages">224</span> pages  




  30. 
Publisher: <span itemprop="publisher">Little, Brown, and Company</span> -  




  31. 
 <meta itemprop="datePublished" content="1991-05-01">May 1, 1991  




  32. 
Language: <span itemprop="inLanguage">English</span>  




  33. 
ISBN-10: <span itemprop="isbn">0316769487</span>  




  34. 
  




  35. 
Reviews:  




  36. 
  




  37. 
<div itemprop="review" itemscope itemtype="https://schema.org/Review">  




  38. 
  <span itemprop="reviewRating">5</span> stars -  




  39. 
  <b>"<span itemprop="name">A masterpiece of literature</span>"</b>  




  40. 
  by <span itemprop="author">John Doe</span>,  




  41. 
  Written on <meta itemprop="datePublished" content="2006-05-04">May 4, 2006  




  42. 
  <span itemprop="reviewBody">I really enjoyed this book. It captures the essential  




  43. 
  challenge people face as they try make sense of their lives and grow to adulthood.</span>  




  44. 
</div>  




  45. 
  




  46. 
<div itemprop="review" itemscope itemtype="https://schema.org/Review">  




  47. 
  <span itemprop="reviewRating">4</span> stars -  




  48. 
  <b>"<span itemprop="name">A good read.</span>" </b>  




  49. 
  by <span itemprop="author">Bob Smith</span>,  




  50. 
  Written on <meta itemprop="datePublished" content="2006-06-15">June 15, 2006  




  51. 
  <span itemprop="reviewBody">Catcher in the Rye is a fun book. It's a good book to read.</span>  




  52. 
</div>  




  53. 
  




  54. 
</div>  




  55. 
...  




  56. 
</body>




```

Example encoded as [RDFa](https://en.wikipedia.org/wiki/RDFa) embedded in HTML.

```



  1. 
<body vocab="https://schema.org/" typeof="WebPage">  




  2. 
...  




  3. 
<div property="breadcrumb">  




  4. 
  <a href="category/books.html">Books</a> >  




  5. 
  <a href="category/books-literature.html">Literature &amp; Fiction</a> >  




  6. 
  <a href="category/books-classics">Classics</a>  




  7. 
</div>  




  8. 
  




  9. 
<div property="mainEntity" typeof="Book">  




  10. 
  




  11. 
<img property="image" src="catcher-in-the-rye-book-cover.jpg"  




  12. 
    alt="cover art: red horse, city in background"/>  




  13. 
<span property="name">The Catcher in the Rye</span> -  




  14. 
 <link property="bookFormat" href="https://schema.org/Paperback">Mass Market Paperback  




  15. 
by <a property="author" href="/author/jd_salinger.html">J.D. Salinger</a>  




  16. 
  




  17. 
<div property="aggregateRating" typeof="AggregateRating">  




  18. 
  <span property="ratingValue">4</span> stars -  




  19. 
  <span property="reviewCount">3077</span> reviews  




  20. 
</div>  




  21. 
  




  22. 
<div property="offers" typeof="Offer">  




  23. 
  Price: $<span property="price">6.99</span>  




  24. 
  <meta property="priceCurrency" content="USD" />  




  25. 
  <link property="availability" href="https://schema.org/InStock">In Stock  




  26. 
</div>  




  27. 
  




  28. 
Product details  




  29. 
<span property="numberOfPages">224</span> pages  




  30. 
Publisher: <span property="publisher">Little, Brown, and Company</span> -  




  31. 
 <meta property="datePublished" content="1991-05-01">May 1, 1991  




  32. 
Language: <span property="inLanguage">English</span>  




  33. 
ISBN-10: <span property="isbn">0316769487</span>  




  34. 
  




  35. 
Reviews:  




  36. 
  




  37. 
<div property="review" typeof="Review">  




  38. 
  <span property="reviewRating">5</span> stars -  




  39. 
  <b>"<span property="name">A masterpiece of literature</span>"</b>  




  40. 
  by <span property="author">John Doe</span>,  




  41. 
  Written on <meta property="datePublished" content="2006-05-04">May 4, 2006  




  42. 
  <span property="reviewBody">I really enjoyed this book. It captures the essential  




  43. 
  challenge people face as they try make sense of their lives and grow to adulthood.</span>  




  44. 
</div>  




  45. 
  




  46. 
<div property="review" typeof="Review">  




  47. 
  <span property="reviewRating">4</span> stars -  




  48. 
  <b>"<span property="name">A good read.</span>" </b>  




  49. 
  by <span property="author">Bob Smith</span>,  




  50. 
  Written on <meta property="datePublished" content="2006-06-15">June 15, 2006  




  51. 
  <span property="reviewBody">Catcher in the Rye is a fun book. It's a good book to read.</span>  




  52. 
</div>  




  53. 
  




  54. 
</div>  




  55. 
...  




  56. 
</body>




```

Example encoded as [JSON-LD](https://en.wikipedia.org/wiki/JSON-LD) in a HTML script tag.

```



  1. 
<script type="application/ld+json">  




  2. 
{  




  3. 
  "@context": "https://schema.org",  




  4. 
  "@type": "WebPage",  




  5. 
  "breadcrumb": "Books > Literature & Fiction > Classics",  




  6. 
  "mainEntity":{  




  7. 
    "@type": "Book",  




  8. 
    "author": "/author/jd_salinger.html",  




  9. 
    "bookFormat": "https://schema.org/Paperback",  




  10. 
    "datePublished": "1991-05-01",  




  11. 
    "image": "catcher-in-the-rye-book-cover.jpg",  




  12. 
    "inLanguage": "English",  




  13. 
    "isbn": "0316769487",  




  14. 
    "name": "The Catcher in the Rye",  




  15. 
    "numberOfPages": "224",  




  16. 
    "offers": {  




  17. 
      "@type": "Offer",  




  18. 
      "availability": "https://schema.org/InStock",  




  19. 
      "price": "6.99",  




  20. 
      "priceCurrency": "USD"  




  21. 
    },  




  22. 
    "publisher": "Little, Brown, and Company",  




  23. 
    "aggregateRating": {  




  24. 
      "@type": "AggregateRating",  




  25. 
      "ratingValue": "4",  




  26. 
      "reviewCount": "3077"  




  27. 
    },  




  28. 
    "review": [  




  29. 
      {  




  30. 
        "@type": "Review",  




  31. 
        "author": "John Doe",  




  32. 
        "datePublished": "2006-05-04",  




  33. 
        "name": "A masterpiece of literature",  




  34. 
        "reviewBody": "I really enjoyed this book. It captures the essential challenge people face as they try make sense of their lives and grow to adulthood.",  




  35. 
        "reviewRating": {  




  36. 
            "@type": "Rating",  




  37. 
            "ratingValue": "5"  




  38. 
           }  




  39. 
      },  




  40. 
      {  




  41. 
        "@type": "Review",  




  42. 
        "author": "Bob Smith",  




  43. 
        "datePublished": "2006-06-15",  




  44. 
        "name": "A good read.",  




  45. 
        "reviewBody": "Catcher in the Rye is a fun book. It's a good book to read.",  




  46. 
        "reviewRating": "4"  




  47. 
      }  




  48. 
    ]  




  49. 
    }  




  50. 
}  




  51. 
</script>




```

Structured representation of the JSON-LD example.
{ "@context": "https://schema.org", "@type": "WebPage", "breadcrumb": "Books > Literature & Fiction > Classics", "mainEntity":{ "@type": "Book", "author": "/author/jd_salinger.html", "bookFormat": "https://schema.org/Paperback", "datePublished": "1991-05-01", "image": "catcher-in-the-rye-book-cover.jpg", "inLanguage": "English", "isbn": "0316769487", "name": "The Catcher in the Rye", "numberOfPages": "224", "offers": { "@type": "Offer", "availability": "https://schema.org/InStock", "price": "6.99", "priceCurrency": "USD" }, "publisher": "Little, Brown, and Company", "aggregateRating": { "@type": "AggregateRating", "ratingValue": "4", "reviewCount": "3077" }, "review": [ { "@type": "Review", "author": "John Doe", "datePublished": "2006-05-04", "name": "A masterpiece of literature", "reviewBody": "I really enjoyed this book. It captures the essential challenge people face as they try make sense of their lives and grow to adulthood.", "reviewRating": { "@type": "Rating", "ratingValue": "5" } }, { "@type": "Review", "author": "Bob Smith", "datePublished": "2006-06-15", "name": "A good read.", "reviewBody": "Catcher in the Rye is a fun book. It's a good book to read.", "reviewRating": "4" } ] } }
![Copy to clipboard](https://schema.org/docs/clipboard/clippy.svg) [Example 16](https://schema.org/Offer#eg-0475 "Link: #eg-0475")
Copied
No Markup JSON-LD Structure
Example notes or example HTML without markup.

```

  1. An example of an offer with a checkoutPageURLTemplate.


```

Example encoded as [JSON-LD](https://en.wikipedia.org/wiki/JSON-LD) in a HTML script tag.

```



  1. 
<script type="application/ld+json">  




  2. 
{  




  3. 
   "@context":"https://schema.org",  




  4. 
   "@type":"Product",  




  5. 
   "sku":"12345",  




  6. 
   "image":"https://example.com/fnobarizer.jpg",  




  7. 
   "name":"Advanced Fnobarizer",  




  8. 
   "brand":{  




  9. 
      "@type":"Brand",  




  10. 
      "name":"Nucleatronics Inc."  




  11. 
   },  




  12. 
   "offers":{  




  13. 
      "@type":"Offer",  




  14. 
      "checkoutPageURLTemplate":"https://www.example.com/checkout?items={VARIANT_ID_1}:{Quantity_1},{VARIANT_ID_2}:{Quantity_2}&discount={DISCOUNT_CODE}&store_id={pickup_store_id}",  




  15. 
      "priceSpecification":{  




  16. 
        "@type":"PriceSpecification",  




  17. 
        "price":"99.99",  




  18. 
        "priceCurrency":"USD"  




  19. 
      },  




  20. 
     "acceptedPaymentMethod":"http://purl.org/goodrelations/v1#GoogleCheckout"  




  21. 
     }  




  22. 
}  




  23. 
</script>




```

Structured representation of the JSON-LD example.
{ "@context":"https://schema.org", "@type":"Product", "sku":"12345", "image":"https://example.com/fnobarizer.jpg", "name":"Advanced Fnobarizer", "brand":{ "@type":"Brand", "name":"Nucleatronics Inc." }, "offers":{ "@type":"Offer", "checkoutPageURLTemplate":"https://www.example.com/checkout?items={VARIANT_ID_1}:{Quantity_1},{VARIANT_ID_2}:{Quantity_2}&discount={DISCOUNT_CODE}&store_id={pickup_store_id}", "priceSpecification":{ "@type":"PriceSpecification", "price":"99.99", "priceCurrency":"USD" }, "acceptedPaymentMethod":"http://purl.org/goodrelations/v1#GoogleCheckout" } }
![Copy to clipboard](https://schema.org/docs/clipboard/clippy.svg) [Example 17](https://schema.org/Offer#eg-4505 "Link: #eg-4505")
Copied
No Markup JSON-LD Structure
Example notes or example HTML without markup.

```



  1. 
<strong>Château Snotty 2020</strong>  




  2. 
  




  3. 
The snottiest red wine on the market.  




  4. 
<ul>  




  5. 
<li>Organic red wine, made in France</li>  




  6. 
<li>2020 Vintage, a very interesting year</li>  




  7. 
<li>75 cl bottle</li>  




  8. 
<li>Cru du Pichet d'Or</li>  




  9. 
<li>Best before 2026</li>  




  10. 
<li>Contains Sulfite</li>  




  11. 
<li>Please recycle the glass bottle</li>  




  12. 
</ul>




```

Example encoded as [JSON-LD](https://en.wikipedia.org/wiki/JSON-LD) in a HTML script tag.

```



  1. 
<script type="application/ld+json">  




  2. 
{  




  3. 
  "@context": {  




  4. 
    "@vocab": "https://schema.org/",  




  5. 
    "gs1": "https://ref.gs1.org/voc/",  




  6. 
    "unece": "https://vocabulary.uncefact.org/"  




  7. 
  },  




  8. 
  "@graph": [  




  9. 
    {  




  10. 
      "@type": [  




  11. 
        "https://schema.org/DefinedRegion",  




  12. 
        "https://schema.org/PostalAddress"  




  13. 
      ],  




  14. 
      "@id": "http://example.com/lechateausnottyaddress",  




  15. 
      "addressCountry": "FR",  




  16. 
      "addressLocality": "L'Introuvable",  




  17. 
      "addressRegion": "Charente"  




  18. 
    },  




  19. 
    {  




  20. 
      "@type": ["QuantitativeValue", "gs1:QuantitativeValue", "unece:MeasureType"],  




  21. 
      "@id": "http://example.com/lechateausnottynetmass",  




  22. 
      "name": "Net mass",  




  23. 
      "unitCode": "KGM",  




  24. 
      "unitText": "kg.",  




  25. 
      "value": 0.75,  




  26. 
      "gs1:unitCode": "KGM",  




  27. 
      "gs1:value": 0.75,  




  28. 
      "unece:MeasureTypeValue": 75,  




  29. 
      "unece:MeasureTypeCode": "unece:WeightUnitMeasureCode#KGM",  




  30. 
      "unece:measuredAttributeCode": "unece:MeasuredAttributeCodeList#AAA"  




  31. 
    },  




  32. 
    {  




  33. 
      "@type": ["QuantitativeValue", "gs1:QuantitativeValue", "unece:MeasureType"],  




  34. 
      "@id": "http://example.com/lechateausnottygrossmass",  




  35. 
      "name": "Gross mass",  




  36. 
      "unitCode": "KGM",  




  37. 
      "unitText": "kg.",  




  38. 
      "value": 1,  




  39. 
      "gs1:unitCode": "KGM",  




  40. 
      "gs1:value": 1,  




  41. 
      "unece:MeasureTypeValue": 1,  




  42. 
      "unece:MeasureTypeCode": "unece:WeightUnitMeasureCode#KGM",  




  43. 
      "unece:measuredAttributeCode": "unece:MeasuredAttributeCodeList#ACN"  




  44. 
    },  




  45. 
    {  




  46. 
      "@type": [  




  47. 
        "Organization",  




  48. 
        "gs1:Organization",  




  49. 
        "unece:TradeParty"  




  50. 
      ],  




  51. 
      "@id": "http://example.com/lechateausnotty",  




  52. 
      "name": "Domaine du Château Snotty",  




  53. 
      "address": {  




  54. 
        "@id": "http://example.com/lechateausnottyaddress"  




  55. 
      },  




  56. 
      "unece:allianceName": "Les Châteaux obscurs de Charente"  




  57. 
    },  




  58. 
    {  




  59. 
      "@type": [  




  60. 
        "Organization",  




  61. 
        "gs1:Organization"  




  62. 
      ],  




  63. 
      "@id": "http://example.com/oenologuesatteres",  




  64. 
      "name": "Association des Œnologues attérés"  




  65. 
    },  




  66. 
    {  




  67. 
      "@type": [  




  68. 
        "Certification",  




  69. 
        "unece:TradeProductCertification"  




  70. 
      ],  




  71. 
      "@id": "http://example.com/certifiedpretentiouswine",  




  72. 
      "name": "Certified Pretentious Wine",  




  73. 
      "certificationIdentification": "pichetdor",  




  74. 
      "issuedBy": {  




  75. 
        "@id": "http://example.com/oenologuesatteres"  




  76. 
      },  




  77. 
      "certificationRating": {  




  78. 
        "@type": "Rating",  




  79. 
        "ratingValue": "Pichet d'Or"  




  80. 
      }  




  81. 
    },  




  82. 
    {  




  83. 
      "@type": [  




  84. 
        "Product",  




  85. 
        "unece:TradeProduct",  




  86. 
        "gs1:Beverage"  




  87. 
      ],  




  88. 
      "name": "Château Snotty 2020",  




  89. 
      "description": [  




  90. 
        {  




  91. 
          "@value": "The snottiest red wine on the market.",  




  92. 
          "@language": "en"  




  93. 
        },  




  94. 
        {  




  95. 
          "@value": "Le vin le plus prétentieux du marché.",  




  96. 
          "@language": "fr"  




  97. 
        }  




  98. 
      ],  




  99. 
      "url": "https://www.example.com/chateau-snotty",  




  100. 
      "image": "https://www.example.com/chateau-snotty.jpg",  




  101. 
      "offers": {  




  102. 
        "@type": "Offer",  




  103. 
        "availability": "https://schema.org/InStock",  




  104. 
        "priceValidUntil": "2026-01-01",  




  105. 
        "price": "999.00",  




  106. 
        "priceCurrency": "EUR",  




  107. 
        "seller": {  




  108. 
          "@id": "http://example.com/lechateausnotty"  




  109. 
        },  




  110. 
        "hasMerchantReturnPolicy": {  




  111. 
          "@type": "MerchantReturnPolicy",  




  112. 
          "applicableCountry": "EU",  




  113. 
          "returnPolicyCategory": "https://schema.org/MerchantReturnNotPermitted"  




  114. 
        },  




  115. 
        "shippingDetails": {  




  116. 
          "@type": "OfferShippingDetails",  




  117. 
          "shippingDestination": {  




  118. 
            "@type": "DefinedRegion",  




  119. 
            "name": "Europe",  




  120. 
            "addressCountry": "EU"  




  121. 
          },  




  122. 
          "shippingRate": {  




  123. 
            "@type": "MonetaryAmount",  




  124. 
            "name": "Free",  




  125. 
            "value": 0,  




  126. 
            "currency": "EUR"  




  127. 
          },  




  128. 
          "deliveryTime": {  




  129. 
            "@type": "ShippingDeliveryTime",  




  130. 
            "handlingTime": {  




  131. 
              "@type": "QuantitativeValue",  




  132. 
              "minValue": 1,  




  133. 
              "maxValue": 2,  




  134. 
              "unitText": "Days",  




  135. 
              "unitCode": "DAY"  




  136. 
            },  




  137. 
            "transitTime": {  




  138. 
              "@type": "QuantitativeValue",  




  139. 
              "minValue": 1,  




  140. 
              "maxValue": 5,  




  141. 
              "unitText": "Days",  




  142. 
              "unitCode": "DAY"  




  143. 
            }  




  144. 
          },  




  145. 
          "hasShippingService": {  




  146. 
            "@type": "ShippingService",  




  147. 
            "name": "Postal Service",  




  148. 
            "fulfillmentType": "https://schema.org/FulfillmentTypeDelivery",  




  149. 
            "shippingConditions": {  




  150. 
              "@type": "ShippingConditions",  




  151. 
              "shippingOrigin": {  




  152. 
                "@id": "http://example.com/lechateausnottyaddress"  




  153. 
              },  




  154. 
              "orderValue": {  




  155. 
                "@type": "MonetaryAmount",  




  156. 
                "value": 100.0,  




  157. 
                "currency": "EUR"  




  158. 
              }  




  159. 
            }  




  160. 
          }  




  161. 
        }  




  162. 
      },  




  163. 
      "manufacturer": {  




  164. 
        "@id": "http://example.com/lechateausnotty"  




  165. 
      },  




  166. 
      "weight": [{  




  167. 
        "@id": "http://example.com/lechateausnottynetmass"  




  168. 
      }, {  




  169. 
        "@id": "http://example.com/lechateausnottygrossmass"  




  170. 
      }],  




  171. 
      "productionDate": "2020-10-01",  




  172. 
      "hasCertification": {  




  173. 
        "@id": "http://example.com/certifiedpretentiouswine"  




  174. 
      },  




  175. 
      "aggregateRating": {  




  176. 
        "@type": "AggregateRating",  




  177. 
        "ratingCount": 33,  




  178. 
        "ratingValue": 4.7,  




  179. 
        "bestRating": 5,  




  180. 
        "worstRating": 1  




  181. 
      },  




  182. 
      "review": {  




  183. 
        "@type": "Review",  




  184. 
        "reviewRating": {  




  185. 
          "@type": "Rating",  




  186. 
          "ratingValue": 5,  




  187. 
          "bestRating": 5,  




  188. 
          "worstRating": 1  




  189. 
        },  




  190. 
        "reviewBody": {  




  191. 
          "@value": "Oncques n'a jamais vu de vin plus prétentieux",  




  192. 
          "@language": "fr"  




  193. 
        },  




  194. 
        "author": {  




  195. 
          "@type": "Person",  




  196. 
          "name": "Jean d'Eau"  




  197. 
        }  




  198. 
      },  




  199. 
      "gs1:bestBeforeDate": "2027-01-01",  




  200. 
      "gs1:AdditiveDetails": {  




  201. 
        "@type": "gs1:AdditiveDetails",  




  202. 
        "gs1:additiveName": "Sulfite",  




  203. 
        "gs1:additiveLevelOfContainment": "gs1:LevelOfContainmentCode-CONTAINS"  




  204. 
      },  




  205. 
      "gs1:netWeight": {  




  206. 
        "@id": "http://example.com/lechateausnottynetmass"  




  207. 
      },  




  208. 
      "gs1:beverageVintage": "2020",  




  209. 
      "gs1:gpcCategoryCode": "10000276",  




  210. 
      "gs1:percentageOfAlcoholByVolume": 4.0,  




  211. 
      "gs1:vintner": "Domaine du Château Snotty",  




  212. 
      "gs1:alcoholicBeverageSubregion": "FR-16",  




  213. 
      "gs1:sweetnessLevelOfAlcoholicBeverage": "gs1:SweetnessLevelOfAlcoholicBeverageCode-DRY",  




  214. 
      "gs1:growingMethod": "gs1:GrowingMethodCode-ORGANIC",  




  215. 
      "gs1:packagingMarkedLabelAccreditation": "gs1:PackagingMarkedLabelAccreditationCode-EU_ECO_LABEL",  




  216. 
      "gs1:consumerSalesCondition": "gs1:ConsumerSalesConditionsCode-RESTRICTED_TO_SELL_16",  




  217. 
      "gs1:seller": {  




  218. 
        "@id": "http://example.com/lechateausnotty"  




  219. 
      },  




  220. 
      "unece:specifiedMarking": {  




  221. 
        "@type": "unece:Marking",  




  222. 
        "unece:packagingMarkingTypeCode": [  




  223. 
          "unece:PackagingMarkingCodeList#32",  




  224. 
          "unece:PackagingMarkingCodeList#9"  




  225. 
        ]  




  226. 
      },  




  227. 
      "unece:fromDeliveryLifeSpanMeasure": {  




  228. 
        "@type": "unece:SupplyChainPackaging",  




  229. 
        "unece:DurationUnitMeasureCode": "unece:DurationUnitMeasureCode#MON",  




  230. 
        "unece:DurationUnitMeasureTypeValue": 6  




  231. 
      },  




  232. 
      "unece:recyclableIndicator": true,  




  233. 
      "unece:applicableTradeProductCertification": {  




  234. 
        "@id": "http://example.com/certifiedpretentiouswine"  




  235. 
      },  




  236. 
      "unece:manufacturerParty": {  




  237. 
        "@id": "http://example.com/lechateausnotty"  




  238. 
      },  




  239. 
      "unece:netWeightMeasure": {  




  240. 
        "@id": "http://example.com/lechateausnottynetmass"  




  241. 
      },  




  242. 
      "unece:grossWeightMeasure": {  




  243. 
        "@id": "http://example.com/lechateausnottygrossmass"  




  244. 
      }  




  245. 
    }  




  246. 
  ]  




  247. 
}  




  248. 
</script>




```

Structured representation of the JSON-LD example.
{ "@context": { "@vocab": "https://schema.org/", "gs1": "https://ref.gs1.org/voc/", "unece": "https://vocabulary.uncefact.org/" }, "@graph": [ { "@type": [ "https://schema.org/DefinedRegion", "https://schema.org/PostalAddress" ], "@id": "http://example.com/lechateausnottyaddress", "addressCountry": "FR", "addressLocality": "L'Introuvable", "addressRegion": "Charente" }, { "@type": ["QuantitativeValue", "gs1:QuantitativeValue", "unece:MeasureType"], "@id": "http://example.com/lechateausnottynetmass", "name": "Net mass", "unitCode": "KGM", "unitText": "kg.", "value": 0.75, "gs1:unitCode": "KGM", "gs1:value": 0.75, "unece:MeasureTypeValue": 75, "unece:MeasureTypeCode": "unece:WeightUnitMeasureCode#KGM", "unece:measuredAttributeCode": "unece:MeasuredAttributeCodeList#AAA" }, { "@type": ["QuantitativeValue", "gs1:QuantitativeValue", "unece:MeasureType"], "@id": "http://example.com/lechateausnottygrossmass", "name": "Gross mass", "unitCode": "KGM", "unitText": "kg.", "value": 1, "gs1:unitCode": "KGM", "gs1:value": 1, "unece:MeasureTypeValue": 1, "unece:MeasureTypeCode": "unece:WeightUnitMeasureCode#KGM", "unece:measuredAttributeCode": "unece:MeasuredAttributeCodeList#ACN" }, { "@type": [ "Organization", "gs1:Organization", "unece:TradeParty" ], "@id": "http://example.com/lechateausnotty", "name": "Domaine du Château Snotty", "address": { "@id": "http://example.com/lechateausnottyaddress" }, "unece:allianceName": "Les Châteaux obscurs de Charente" }, { "@type": [ "Organization", "gs1:Organization" ], "@id": "http://example.com/oenologuesatteres", "name": "Association des Œnologues attérés" }, { "@type": [ "Certification", "unece:TradeProductCertification" ], "@id": "http://example.com/certifiedpretentiouswine", "name": "Certified Pretentious Wine", "certificationIdentification": "pichetdor", "issuedBy": { "@id": "http://example.com/oenologuesatteres" }, "certificationRating": { "@type": "Rating", "ratingValue": "Pichet d'Or" } }, { "@type": [ "Product", "unece:TradeProduct", "gs1:Beverage" ], "name": "Château Snotty 2020", "description": [ { "@value": "The snottiest red wine on the market.", "@language": "en" }, { "@value": "Le vin le plus prétentieux du marché.", "@language": "fr" } ], "url": "https://www.example.com/chateau-snotty", "image": "https://www.example.com/chateau-snotty.jpg", "offers": { "@type": "Offer", "availability": "https://schema.org/InStock", "priceValidUntil": "2026-01-01", "price": "999.00", "priceCurrency": "EUR", "seller": { "@id": "http://example.com/lechateausnotty" }, "hasMerchantReturnPolicy": { "@type": "MerchantReturnPolicy", "applicableCountry": "EU", "returnPolicyCategory": "https://schema.org/MerchantReturnNotPermitted" }, "shippingDetails": { "@type": "OfferShippingDetails", "shippingDestination": { "@type": "DefinedRegion", "name": "Europe", "addressCountry": "EU" }, "shippingRate": { "@type": "MonetaryAmount", "name": "Free", "value": 0, "currency": "EUR" }, "deliveryTime": { "@type": "ShippingDeliveryTime", "handlingTime": { "@type": "QuantitativeValue", "minValue": 1, "maxValue": 2, "unitText": "Days", "unitCode": "DAY" }, "transitTime": { "@type": "QuantitativeValue", "minValue": 1, "maxValue": 5, "unitText": "Days", "unitCode": "DAY" } }, "hasShippingService": { "@type": "ShippingService", "name": "Postal Service", "fulfillmentType": "https://schema.org/FulfillmentTypeDelivery", "shippingConditions": { "@type": "ShippingConditions", "shippingOrigin": { "@id": "http://example.com/lechateausnottyaddress" }, "orderValue": { "@type": "MonetaryAmount", "value": 100.0, "currency": "EUR" } } } } }, "manufacturer": { "@id": "http://example.com/lechateausnotty" }, "weight": [{ "@id": "http://example.com/lechateausnottynetmass" }, { "@id": "http://example.com/lechateausnottygrossmass" }], "productionDate": "2020-10-01", "hasCertification": { "@id": "http://example.com/certifiedpretentiouswine" }, "aggregateRating": { "@type": "AggregateRating", "ratingCount": 33, "ratingValue": 4.7, "bestRating": 5, "worstRating": 1 }, "review": { "@type": "Review", "reviewRating": { "@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1 }, "reviewBody": { "@value": "Oncques n'a jamais vu de vin plus prétentieux", "@language": "fr" }, "author": { "@type": "Person", "name": "Jean d'Eau" } }, "gs1:bestBeforeDate": "2027-01-01", "gs1:AdditiveDetails": { "@type": "gs1:AdditiveDetails", "gs1:additiveName": "Sulfite", "gs1:additiveLevelOfContainment": "gs1:LevelOfContainmentCode-CONTAINS" }, "gs1:netWeight": { "@id": "http://example.com/lechateausnottynetmass" }, "gs1:beverageVintage": "2020", "gs1:gpcCategoryCode": "10000276", "gs1:percentageOfAlcoholByVolume": 4.0, "gs1:vintner": "Domaine du Château Snotty", "gs1:alcoholicBeverageSubregion": "FR-16", "gs1:sweetnessLevelOfAlcoholicBeverage": "gs1:SweetnessLevelOfAlcoholicBeverageCode-DRY", "gs1:growingMethod": "gs1:GrowingMethodCode-ORGANIC", "gs1:packagingMarkedLabelAccreditation": "gs1:PackagingMarkedLabelAccreditationCode-EU_ECO_LABEL", "gs1:consumerSalesCondition": "gs1:ConsumerSalesConditionsCode-RESTRICTED_TO_SELL_16", "gs1:seller": { "@id": "http://example.com/lechateausnotty" }, "unece:specifiedMarking": { "@type": "unece:Marking", "unece:packagingMarkingTypeCode": [ "unece:PackagingMarkingCodeList#32", "unece:PackagingMarkingCodeList#9" ] }, "unece:fromDeliveryLifeSpanMeasure": { "@type": "unece:SupplyChainPackaging", "unece:DurationUnitMeasureCode": "unece:DurationUnitMeasureCode#MON", "unece:DurationUnitMeasureTypeValue": 6 }, "unece:recyclableIndicator": true, "unece:applicableTradeProductCertification": { "@id": "http://example.com/certifiedpretentiouswine" }, "unece:manufacturerParty": { "@id": "http://example.com/lechateausnotty" }, "unece:netWeightMeasure": { "@id": "http://example.com/lechateausnottynetmass" }, "unece:grossWeightMeasure": { "@id": "http://example.com/lechateausnottygrossmass" } } ] }
![Copy to clipboard](https://schema.org/docs/clipboard/clippy.svg) [Example 18](https://schema.org/Offer#eg-4878 "Link: #eg-4878")
Copied
No Markup JSON-LD Structure
Example notes or example HTML without markup.

```

  1. This example demonstrates a comprehensive electronics product (a fictional smart drone). It showcases how to group technical specifications using `valueGroup` on `PropertyValue`, display safety information using `consumerNotice`, link related accessories using `isOftenBoughtWith`, and model pricing and shipping constraints using `MaximumRetailPrice`, `itemPopularity`, and `minimumOrderValue`.


```

Example encoded as [JSON-LD](https://en.wikipedia.org/wiki/JSON-LD) in a HTML script tag.

```



  1. 
<script type="application/ld+json">  




  2. 
{  




  3. 
  "@context": "https://schema.org/",  




  4. 
  "@type": "Product",  




  5. 
  "name": "AeroQuad Pro Smart Drone",  




  6. 
  "description": "A high-performance quadcopter drone with 4K camera and obstacle avoidance.",  




  7. 
  "brand": {  




  8. 
    "@type": "Brand",  




  9. 
    "name": "AeroTech"  




  10. 
  },  




  11. 
  "image": "https://example.com/images/aeroquad-pro.jpg",  




  12. 
  "consumerNotice": {  




  13. 
    "@type": "TextObject",  




  14. 
    "name": "CHOKING_HAZARD",  




  15. 
    "text": "WARNING: Choking Hazard - Small parts. Not for children under 3 years. This product must be registered with the FAA before flight."  




  16. 
  },  




  17. 
  "isOftenBoughtWith": [  




  18. 
    {  




  19. 
      "@type": "Product",  




  20. 
      "name": "AeroQuad Replacement Propellers (4-Pack)",  




  21. 
      "sku": "AQ-PROP-4PK"  




  22. 
    },  




  23. 
    {  




  24. 
      "@type": "Product",  




  25. 
      "name": "AeroQuad High-Capacity Battery",  




  26. 
      "sku": "AQ-BATT-HC"  




  27. 
    }  




  28. 
  ],  




  29. 
  "specification": [  




  30. 
    {  




  31. 
      "@type": "PropertyValue",  




  32. 
      "valueGroup": "Camera Specs",  




  33. 
      "name": "Video Resolution",  




  34. 
      "value": "4K at 60fps"  




  35. 
    },  




  36. 
    {  




  37. 
      "@type": "PropertyValue",  




  38. 
      "valueGroup": "Camera Specs",  




  39. 
      "name": "Sensor Type",  




  40. 
      "value": "1-inch CMOS"  




  41. 
    },  




  42. 
    {  




  43. 
      "@type": "PropertyValue",  




  44. 
      "valueGroup": "Flight Performance",  




  45. 
      "name": "Max Flight Time",  




  46. 
      "value": "35 minutes"  




  47. 
    },  




  48. 
    {  




  49. 
      "@type": "PropertyValue",  




  50. 
      "valueGroup": "Flight Performance",  




  51. 
      "name": "Max Speed",  




  52. 
      "value": "45 mph"  




  53. 
    }  




  54. 
  ],  




  55. 
  "offers": {  




  56. 
    "@type": "Offer",  




  57. 
    "price": "799.00",  




  58. 
    "priceCurrency": "USD",  




  59. 
    "itemCondition": "https://schema.org/NewCondition",  




  60. 
    "availability": "https://schema.org/InStock",  




  61. 
    "itemPopularity": {  




  62. 
      "@type": "QuantitativeValue",  




  63. 
      "value": 54,  




  64. 
      "minValue": 1,  




  65. 
      "maxValue": 347,  




  66. 
      "name": "Category Popularity Rank"  




  67. 
    },  




  68. 
    "priceSpecification": [  




  69. 
      {  




  70. 
        "@type": "UnitPriceSpecification",  




  71. 
        "priceType": "https://schema.org/MaximumRetailPrice",  




  72. 
        "price": "899.00",  




  73. 
        "priceCurrency": "USD"  




  74. 
      },  




  75. 
      {  




  76. 
        "@type": "UnitPriceSpecification",  




  77. 
        "price": "799.00",  




  78. 
        "priceCurrency": "USD"  




  79. 
      }  




  80. 
    ],  




  81. 
    "shippingDetails": {  




  82. 
      "@type": "OfferShippingDetails",  




  83. 
      "provider": {  




  84. 
        "@type": "Organization",  




  85. 
        "name": "Acme Fast Freight"  




  86. 
      },  




  87. 
      "shippingDestination": {  




  88. 
        "@type": "DefinedRegion",  




  89. 
        "addressCountry": "US"  




  90. 
      },  




  91. 
      "shippingRate": {  




  92. 
        "@type": "ShippingRateSettings",  




  93. 
        "shippingRate": {  




  94. 
          "@type": "MonetaryAmount",  




  95. 
          "value": "0.00",  




  96. 
          "currency": "USD"  




  97. 
        },  




  98. 
        "minimumOrderValue": {  




  99. 
          "@type": "PriceSpecification",  




  100. 
          "price": "50.00",  




  101. 
          "priceCurrency": "USD"  




  102. 
        }  




  103. 
      }  




  104. 
    }  




  105. 
  }  




  106. 
}  




  107. 
</script>




```

Structured representation of the JSON-LD example.
{ "@context": "https://schema.org/", "@type": "Product", "name": "AeroQuad Pro Smart Drone", "description": "A high-performance quadcopter drone with 4K camera and obstacle avoidance.", "brand": { "@type": "Brand", "name": "AeroTech" }, "image": "https://example.com/images/aeroquad-pro.jpg", "consumerNotice": { "@type": "TextObject", "name": "CHOKING_HAZARD", "text": "WARNING: Choking Hazard - Small parts. Not for children under 3 years. This product must be registered with the FAA before flight." }, "isOftenBoughtWith": [ { "@type": "Product", "name": "AeroQuad Replacement Propellers (4-Pack)", "sku": "AQ-PROP-4PK" }, { "@type": "Product", "name": "AeroQuad High-Capacity Battery", "sku": "AQ-BATT-HC" } ], "specification": [ { "@type": "PropertyValue", "valueGroup": "Camera Specs", "name": "Video Resolution", "value": "4K at 60fps" }, { "@type": "PropertyValue", "valueGroup": "Camera Specs", "name": "Sensor Type", "value": "1-inch CMOS" }, { "@type": "PropertyValue", "valueGroup": "Flight Performance", "name": "Max Flight Time", "value": "35 minutes" }, { "@type": "PropertyValue", "valueGroup": "Flight Performance", "name": "Max Speed", "value": "45 mph" } ], "offers": { "@type": "Offer", "price": "799.00", "priceCurrency": "USD", "itemCondition": "https://schema.org/NewCondition", "availability": "https://schema.org/InStock", "itemPopularity": { "@type": "QuantitativeValue", "value": 54, "minValue": 1, "maxValue": 347, "name": "Category Popularity Rank" }, "priceSpecification": [ { "@type": "UnitPriceSpecification", "priceType": "https://schema.org/MaximumRetailPrice", "price": "899.00", "priceCurrency": "USD" }, { "@type": "UnitPriceSpecification", "price": "799.00", "priceCurrency": "USD" } ], "shippingDetails": { "@type": "OfferShippingDetails", "provider": { "@type": "Organization", "name": "Acme Fast Freight" }, "shippingDestination": { "@type": "DefinedRegion", "addressCountry": "US" }, "shippingRate": { "@type": "ShippingRateSettings", "shippingRate": { "@type": "MonetaryAmount", "value": "0.00", "currency": "USD" }, "minimumOrderValue": { "@type": "PriceSpecification", "price": "50.00", "priceCurrency": "USD" } } } } }
![Copy to clipboard](https://schema.org/docs/clipboard/clippy.svg) [Example 19](https://schema.org/Offer#eg-4891 "Link: #eg-4891")
Copied
No Markup
Example notes or example HTML without markup.

```

  1. Example 2 (DPP Page): The actual Digital Product Passport page itself, which provides the full compliance data, importer information, substances of concern, and compliance declarations.


```

![Copy to clipboard](https://schema.org/docs/clipboard/clippy.svg) [Example 20](https://schema.org/Offer#eg-4892 "Link: #eg-4892")
Copied
No Markup JSON-LD Structure
Example notes or example HTML without markup.

```

  1. Offer with free shipping in the US and Canada (in the V2 Shipping format).


```

Example encoded as [JSON-LD](https://en.wikipedia.org/wiki/JSON-LD) in a HTML script tag.

```



  1. 
<script type="application/ld+json">  




  2. 
{  




  3. 
  "@context": "https://schema.org/",  




  4. 
  "@type": "Product",  




  5. 
  "name": "JSON Example",  




  6. 
  "offers": {  




  7. 
    "@type": "Offer",  




  8. 
    "shippingDetails": {  




  9. 
      "@type": "OfferShippingDetails",  




  10. 
      "height": "12 in",  




  11. 
      "width": "45 cm",  




  12. 
      "depth": "0.3 m",  




  13. 
      "weight": "1.2 kg",  




  14. 
      "hasShippingService": {  




  15. 
        "@type": "ShippingService",  




  16. 
        "shippingConditions": {  




  17. 
          "@type": "ShippingConditions",  




  18. 
          "shippingDestination": [  




  19. 
            {  




  20. 
              "@type": "DefinedRegion",  




  21. 
              "addressCountry": "US"  




  22. 
            },  




  23. 
            {  




  24. 
              "@type": "DefinedRegion",  




  25. 
              "addressCountry": "CA"  




  26. 
            }  




  27. 
          ],  




  28. 
          "shippingRate": "0"  




  29. 
        }  




  30. 
      }  




  31. 
    }  




  32. 
  }  




  33. 
}  




  34. 
</script>




```

Structured representation of the JSON-LD example.
{ "@context": "https://schema.org/", "@type": "Product", "name": "JSON Example", "offers": { "@type": "Offer", "shippingDetails": { "@type": "OfferShippingDetails", "height": "12 in", "width": "45 cm", "depth": "0.3 m", "weight": "1.2 kg", "hasShippingService": { "@type": "ShippingService", "shippingConditions": { "@type": "ShippingConditions", "shippingDestination": [ { "@type": "DefinedRegion", "addressCountry": "US" }, { "@type": "DefinedRegion", "addressCountry": "CA" } ], "shippingRate": "0" } } } } }
![Copy to clipboard](https://schema.org/docs/clipboard/clippy.svg) [Example 21](https://schema.org/Offer#eg-4894 "Link: #eg-4894")
Copied
No Markup JSON-LD Structure
Example notes or example HTML without markup.

```

  1. Offer with shipping costs of $10 + $1/kg for orders $35-$200, to the US and Canada, with a handling time of 3.5 hours on weekdays (in the V2 format).


```

Example encoded as [JSON-LD](https://en.wikipedia.org/wiki/JSON-LD) in a HTML script tag.

```



  1. 
<script type="application/ld+json">  




  2. 
{  




  3. 
  "@context": "https://schema.org",  




  4. 
  "@type": "Product",  




  5. 
  "name": "JSON Example",  




  6. 
  "offers": {  




  7. 
    "@type": "Offer",  




  8. 
    "shippingDetails": {  




  9. 
      "@type": "OfferShippingDetails",  




  10. 
      "height": "12 in",  




  11. 
      "width": "45 cm",  




  12. 
      "depth": "300 mm",  




  13. 
      "weight": "1.2 kg",  




  14. 
      "hasShippingService": {  




  15. 
        "@type": "ShippingService",  




  16. 
        "handlingTime": {  




  17. 
          "@type": "ServicePeriod",  




  18. 
          "cutoffTime": "14:30:00-07:00",  




  19. 
          "duration": {  




  20. 
            "@type": "QuantitativeValue",  




  21. 
            "maxValue": "30",  




  22. 
            "unitCode": "min"  




  23. 
          }  




  24. 
        },  




  25. 
        "shippingConditions": {  




  26. 
          "@type": "ShippingConditions",  




  27. 
          "shippingDestination": [  




  28. 
            {  




  29. 
              "@type": "DefinedRegion",  




  30. 
              "addressCountry": "US"  




  31. 
            },  




  32. 
            {  




  33. 
              "@type": "DefinedRegion",  




  34. 
              "addressCountry": "CA"  




  35. 
            }  




  36. 
          ],  




  37. 
          "orderValue": {  




  38. 
            "@type": "MonetaryAmount",  




  39. 
            "minValue": "35",  




  40. 
            "maxValue": "200"  




  41. 
          },  




  42. 
          "shippingRate": {  




  43. 
            "@type": "ShippingRateSettings",  




  44. 
            "shippingRate": {  




  45. 
              "@type": "MonetaryAmount",  




  46. 
              "value": "10",  




  47. 
              "currency": "USD"  




  48. 
            },  




  49. 
            "weightPercentage": "1.0"  




  50. 
          },  




  51. 
          "transitTime": {  




  52. 
            "@type": "ServicePeriod",  




  53. 
            "duration": {  




  54. 
              "maxValue": "3.5",  




  55. 
              "unitCode": "h"  




  56. 
            },  




  57. 
            "businessDays": [  




  58. 
              {  




  59. 
                "dayOfWeek": "Monday"  




  60. 
              },  




  61. 
              {  




  62. 
                "dayOfWeek": "Tuesday"  




  63. 
              },  




  64. 
              {  




  65. 
                "dayOfWeek": "Wednesday"  




  66. 
              },  




  67. 
              {  




  68. 
                "dayOfWeek": "Thursday"  




  69. 
              },  




  70. 
              {  




  71. 
                "dayOfWeek": "Friday"  




  72. 
              }  




  73. 
            ]  




  74. 
          }  




  75. 
        }  




  76. 
      }  




  77. 
    }  




  78. 
  }  




  79. 
}  




  80. 
</script>




```

Structured representation of the JSON-LD example.
{ "@context": "https://schema.org", "@type": "Product", "name": "JSON Example", "offers": { "@type": "Offer", "shippingDetails": { "@type": "OfferShippingDetails", "height": "12 in", "width": "45 cm", "depth": "300 mm", "weight": "1.2 kg", "hasShippingService": { "@type": "ShippingService", "handlingTime": { "@type": "ServicePeriod", "cutoffTime": "14:30:00-07:00", "duration": { "@type": "QuantitativeValue", "maxValue": "30", "unitCode": "min" } }, "shippingConditions": { "@type": "ShippingConditions", "shippingDestination": [ { "@type": "DefinedRegion", "addressCountry": "US" }, { "@type": "DefinedRegion", "addressCountry": "CA" } ], "orderValue": { "@type": "MonetaryAmount", "minValue": "35", "maxValue": "200" }, "shippingRate": { "@type": "ShippingRateSettings", "shippingRate": { "@type": "MonetaryAmount", "value": "10", "currency": "USD" }, "weightPercentage": "1.0" }, "transitTime": { "@type": "ServicePeriod", "duration": { "maxValue": "3.5", "unitCode": "h" }, "businessDays": [ { "dayOfWeek": "Monday" }, { "dayOfWeek": "Tuesday" }, { "dayOfWeek": "Wednesday" }, { "dayOfWeek": "Thursday" }, { "dayOfWeek": "Friday" } ] } } } } } }
[Terms and conditions](https://schema.org/docs/terms.html)
• Schema.org • V30.1 | 2026-09-16 

