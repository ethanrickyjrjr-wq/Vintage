[Skip to main content](https://shopify.dev/docs/api/liquid/filters/structured_data#main-content)
[![Docs page](https://shopify-assets.shopifycdn.com/shopifycloud/shopify-dev/production/assets/dev-docs-logo-2-light-D4UI1jxY.svg)![Docs page](https://shopify-assets.shopifycdn.com/shopifycloud/shopify-dev/production/assets/dev-docs-logo-2-dark-BQ-Bk9XA.svg)](https://shopify.dev/docs)
  * [Apps](https://shopify.dev/docs/apps/build)
  * [Storefronts](https://shopify.dev/docs/storefronts)
  * [Agents](https://shopify.dev/docs/agents)
  * References
  * [Changelog](https://shopify.dev/changelog)


  * Ask assistant`/`
  * [Help](https://shopify.dev/support)
  * •
  * [Log in](http://dev.shopify.com/dashboard)


Collapse sidebar
[Back to all APIsLiquid](https://shopify.dev/docs/api)
  * [Overview](https://shopify.dev/docs/api/liquid)
  * [What is a template language?](https://shopify.dev/docs/api/liquid#what-is-a-template-language)
  * [Variations of Liquid](https://shopify.dev/docs/api/liquid#variations-of-liquid)
  * [Liquid basics](https://shopify.dev/docs/api/liquid#liquid-basics)
  * [Defining logic with tags](https://shopify.dev/docs/api/liquid#defining-logic-with-tags)
  * [Modifying output with filters](https://shopify.dev/docs/api/liquid#modifying-output-with-filters)
  * [Referencing objects](https://shopify.dev/docs/api/liquid#referencing-objects)
  * [Resources & tools](https://shopify.dev/docs/api/liquid#resources-and-tools)


* * *
  * [Basics](https://shopify.dev/docs/api/liquid/basics)
  * Tags
  * Filters
  * Objects


Full index
# structured_data
Install AI ToolkitAsk about this pageCopy MD
1
variable | structured_data
returns [string](https://shopify.dev/docs/api/liquid/basics#string)
Converts an object into a schema.org structured data format.
The `structured_data` filter can be used on the [`product`](https://shopify.dev/docs/api/liquid/objects/product) and [`article`](https://shopify.dev/docs/api/liquid/objects/article) objects.
Product objects are output as a [schema.org `Product`](https://schema.org/Product) if they have no variants, and a [`ProductGroup`](https://schema.org/ProductGroup) if they have one or more variants.
Article objects are output as a [schema.org `Article`.](https://schema.org/Article)
Code
Reset Code
1
2
3
<script type="application/ld+json">
{{ product | structured_data }}
</script>
##### Code

```
<script type="application/ld+json">
  {{ product | structured_data }}
</script>
```

## Output
1
2
3
<script type="application/ld+json">
{"@context":"http:\/\/schema.org\/","@id":"\/products\/crocodile-tears#product","@type":"Product","brand":{"@type":"Brand","name":"Polina's Potent Potions"},"category":"","description":"","image":"https:\/\/polinas-potent-potions.myshopify.com\/cdn\/shop\/products\/amber-beard-oil-bottle.jpg?v=1650642958\u0026width=1920","name":"Crocodile tears","offers":{"@id":"\/products\/crocodile-tears?variant=39888242344001#offer","@type":"Offer","availability":"http:\/\/schema.org\/OutOfStock","price":"56.00","priceCurrency":"CAD","url":"https:\/\/polinas-potent-potions.myshopify.com\/products\/crocodile-tears?variant=39888242344001"},"url":"https:\/\/polinas-potent-potions.myshopify.com\/products\/crocodile-tears"}
</script>
##### Output

```
<script type="application/ld+json">
  {"@context":"http:\/\/schema.org\/","@id":"\/products\/crocodile-tears#product","@type":"Product","brand":{"@type":"Brand","name":"Polina's Potent Potions"},"category":"","description":"","image":"https:\/\/polinas-potent-potions.myshopify.com\/cdn\/shop\/products\/amber-beard-oil-bottle.jpg?v=1650642958\u0026width=1920","name":"Crocodile tears","offers":{"@id":"\/products\/crocodile-tears?variant=39888242344001#offer","@type":"Offer","availability":"http:\/\/schema.org\/OutOfStock","price":"56.00","priceCurrency":"CAD","url":"https:\/\/polinas-potent-potions.myshopify.com\/products\/crocodile-tears?variant=39888242344001"},"url":"https:\/\/polinas-potent-potions.myshopify.com\/products\/crocodile-tears"}
</script>
```

Was this page helpful?
YesNo
### Updates
  * [Developer changelog](https://shopify.dev/changelog)
  * [Shopify Editions](https://www.shopify.com/editions)


### Business growth
  * [Shopify Partners Program](https://www.shopify.com/partners?shpxid=222dd762-CA08-48FF-E4D4-FF926B8FFCAD)
  * [Shopify App Store](https://apps.shopify.com/?shpxid=222dd762-CA08-48FF-E4D4-FF926B8FFCAD)


### Legal
  * [Terms of service](https://www.shopify.com/legal/terms?shpxid=222dd762-CA08-48FF-E4D4-FF926B8FFCAD)
  * [API terms of use](https://www.shopify.com/legal/api-terms?shpxid=222dd762-CA08-48FF-E4D4-FF926B8FFCAD)
  * [Privacy policy](https://www.shopify.com/legal/privacy?shpxid=222dd762-CA08-48FF-E4D4-FF926B8FFCAD)
  * [Partners Program Agreement](https://www.shopify.com/partners/terms?shpxid=222dd762-CA08-48FF-E4D4-FF926B8FFCAD)


### Shopify
  * [About Shopify](https://www.shopify.com/about?shpxid=222dd762-CA08-48FF-E4D4-FF926B8FFCAD)
  * [Shopify Plus](https://www.shopify.com/plus?shpxid=222dd762-CA08-48FF-E4D4-FF926B8FFCAD)
  * [Careers](https://www.shopify.com/careers?shpxid=222dd762-CA08-48FF-E4D4-FF926B8FFCAD)
  * [Investors](https://investors.shopify.com/home/default.aspx?shpxid=222dd762-CA08-48FF-E4D4-FF926B8FFCAD)
  * [Press and media](https://shopify.com/news?shpxid=7db0d4e4-24E8-4087-58FA-7EE470CA745A)



