End of Other articles Links 
Rich Pins are Pins that automatically sync information from your site. You can identify rich Pins by the extra information above and below the image when you click into the Pin. If something changes on the original site, the rich Pin periodically updates to reflect that change.
Types of rich Pins
* **Recipe rich Pins** add a title, serving size, cook time, ratings, diet preference and a list of ingredients to recipes that you save from your site.
* **Article rich Pins** add the headline or title, the description and the author of the article or blog post from your site.
* **Product rich Pins** include the most up-to-date pricing, availability and product information right on your Pin.
How syncing works
Article rich Pins and recipe rich Pins will update automatically to reflect any edits that you make to your site. On the Pinterest side, if you make a manual edit to a recipe or article rich Pin, the new information you add will overwrite the rich metadata.
We’ll only show information about your product rich Pin if you've met our merchant guidelines and if the product is in stock. 
Add tags to your site
To ensure your data syncs correctly, add tags to your site. If you have product, article or recipe content on your site, you’ll need to add rich meta tags to those pages. 
All content from pages that have the correct meta tags will appear as rich Pins when you create a new Pin. Existing Pins that link back to pages with rich meta tags will now appear as Rich Pins. 
_Note: It may take up to 24 hours for the content from your site to sync to your rich Pin._
Remove rich Pin data
If you want to remove rich Pin data from a specific page on your site, add this tag to the header of your page before the closing body tag:

```
<meta name="pinterest-rich-pin" content="false" />
```

The tag will override the rich Pin meta tags on that page only. All other pages on your site will remain unaffected unless you add the tag to those individual pages. If you ever want to turn rich Pins back on, remove this tag.
Recipe rich Pins 
Recipe Pins let you add a title, serving size, cook time, ratings, and a list of ingredients to recipes from your site. You can also display if a recipe is paleo, vegetarian, vegan or gluten-free. 
Add recipe Pins to your site
If you want to integrate recipe rich Pin data to your site, add Schema.org or h-recipe markups between the <head> </head> section of your HTML code for each page that you want to enable recipe rich Pins on.
Once this is done, our system should start to populate rich Pin content for Pins linked to these rich Pin enabled pages.
Recipe ratings
You can add ratings info to your recipe rich Pins. To do so, add the meta tag needed via Schema.org markup. If you need help implementing ratings info to your site, visit Schema.org or take a look at this sample Pin to see how bettycrocker.com set up their Pin.
_Note: ratings info can only be added using Schema.org markup (not h-recipe) and ratings info will only appear on iOS and Android devices._
Schema.org and h-recipe markups
Here are the required rich Pin fields for each type of markup. Edit the fields in black to reflect your recipes:

```
<div itemscope itemtype="https://schema.org/Recipe">
    <span itemprop="name">
    Orange-Pineapple-Carrot Smoothie</span>
   <span itemprop="description">
    Description of your recipe.</span>
  <span itemprop="aggregateRating">
    Aggregate rating will show here</span>
    <meta itemprop="url"
    content="https://myrecipesite.com/pineapple.html" />
    <span itemprop="recipeYield">Serves 1</span>
    Ingredients:
        <span itemprop="ingredients">ingredient 1</span>,
        <span itemprop="ingredients">ingredient 2</span>,
        <span itemprop="ingredients">ingredient 3</span>,
        <span itemprop="ingredients">
    add as many ingredient tags as you need</span>.
    Instructions:
    <span itemprop="recipeInstructions">
    Put the pineapple, ice, orange juice, carrot and
    banana in a blender. Blend until smooth.</span>
</div> 

```

h-recipe tags:

```
<article class="h-recipe">
  <h1 class="p-name">Bagels</h1>
  <ul>
    <li class="p-ingredient">Flour</li>
    <li class="p-ingredient">Sugar</li>
    <li class="p-ingredient">Yeast</li>
  </ul>
  <p>Takes <time class="dt-duration" datetime="1H">1 hour</time>,
     serves <data class="p-yield" value="4">four people</data>.</p>
  <div class="e-instructions">
    <ol>
      <li>Start by mixing all the ingredients together.</li>
    </ol>
  </div>
</article>
```

Check out our developer site to learn more.
Article Pins 
An article is a page that contains text, like a news article or blog post. We do not consider listicles or pages with mostly images and little text to be articles.
Add article Pins to your site
If you want to integrate article rich Pin data to your site, Add Open Graph or Schema.org markups between the <head> </head> section of your HTML code for each page that you want to enable article rich Pins on.
Once this is done, our system should start to populate rich Pin content for Pins linked to these rich Pin enabled pages.
Open Graph and Schema.org markups
Here are the required rich Pin fields for each type of markup. Edit the capitalized fields to reflect your articles.
Open Graph markups:

```
<meta property="og:title" content="Title of your Article"/>
<meta property="og:description" content="Description of your article" />
<meta property="og:type" content="article" />
```

Schema.org markups:

```
<meta property="og:site_name" content="Example Site” />
<div itemscope itemtype="https://schema.org/article">
    <meta itemprop="url" content="Https://www.example.com/2013/10/article.html" />
    <span itemprop="name" content="Article Title” /> by <span itemprop="author" content="Johh Doe” />
    <span itemprop="description">A description or summary of the article.</span>
    </div>
```

Check out our developer site to learn more. 
Product Pins 
Product Pins are a type of rich Pin that feature the most up-to-date price, availability, product title and description from your site. In some cases, your Pin might have a "Best seller' badge if it’s one of the most purchased items within a Pinterest product category across different merchants. Or, it might have a "Popular" badge if it’s one of the most clicked product Pins within a product category on Pinterest.
_Note: This info will only show up on your product Pins if your product is in stock, the price is accurate, we've updated the data recently and you meet our_ merchant guidelines _._
Why and how to add product Pins to your site
Product Pins lead people on Pinterest to your site where they can purchase your products. This means people need to be able to buy the product directly from your site before you can add the product Pin to Pinterest.
You can create product Pins on your site as outlined below or by using catalogs. Use catalogs to upload a data source of your products and create product groups to group similar product Pins together. Only product Pins created using catalogs can be promoted as shopping ads.
Add product Pins to your site
If you want to integrate product rich Pin data to your site, add Open Graph or Schema.org markups between the <head> </head> section of your HTML code for each page on which you want to enable product Pins. 
Once this is done, our system should start to populate rich Pin content for Pins linked to these rich Pin enabled pages.
Open Graph and Schema.org markups
Here are the required rich Pin fields for each type of markup. Edit the capitalized or numeric green text to reflect your products.
Open Graph markups:

```
<meta property="og:title" content="De Young Copper Bookmark" />
<meta property="og:type" content="product" />
<meta property="product:price:amount" content="15.00" />
<meta property="product:price:currency" content="USD" />
```

Schema.org markups:

```
<div itemscope itemtype="https://schema.org/Product">
<meta itemprop="name" content="De Young Copper Bookmark" />
<meta itemprop="url" content="Https://shop.famsf.org/do/product/BK5160" />
<div itemprop="offers" itemscope itemtype="https://schema.org/Offer">
<span itemprop="price">.00</span>
<meta itemprop="priceCurrency" content="USD” />
<meta itemprop="availability" itemtype="https://schema.org/ItemAvailability"
content="https://schema.org/InStock" />
</div>
```

You do not need to add any markup if your site is hosted by Etsy, Teachers Pay Teachers, or eBay. New Pins from these sites will have product information on them within 24 hours.
Check out our developer site to learn more. 
End of Other articles Links 
Still need help?  Contact us 
User feedback
**Was this article helpful?**
## collection_fields
How can we make this article better?
Additional Response

