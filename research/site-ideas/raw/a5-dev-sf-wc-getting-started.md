[Skip to main content](https://shopify.dev/docs/api/storefront-web-components/getting-started#main-content)
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


Expand sidebar
[Back to all APIsStorefront web components](https://shopify.dev/docs/api)
  * [Overview](https://shopify.dev/docs/api/storefront-web-components)
  * [How Storefront Web Components work](https://shopify.dev/docs/api/storefront-web-components#how-storefront-web-components-work)
  * [Resources](https://shopify.dev/docs/api/storefront-web-components#resources)


* * *
  *     * [Getting started](https://shopify.dev/docs/api/storefront-web-components/getting-started)
    * [Step 1: Connect your store](https://shopify.dev/docs/api/storefront-web-components/getting-started#step-1-connect-your-store)
    * [Step 2: Set the context](https://shopify.dev/docs/api/storefront-web-components/getting-started#step-2-set-the-context)
    * [Step 3: Load Shopify data](https://shopify.dev/docs/api/storefront-web-components/getting-started#step-3-load-shopify-data)
    * [Step 4: Format components](https://shopify.dev/docs/api/storefront-web-components/getting-started#step-4-format-components)
    * [Step 5: Connect to checkout](https://shopify.dev/docs/api/storefront-web-components/getting-started#step-5-connect-to-checkout)
    * [Next steps](https://shopify.dev/docs/api/storefront-web-components/getting-started#next-steps)
    * [Common patterns](https://shopify.dev/docs/api/storefront-web-components/common-patterns)
    * [Custom data](https://shopify.dev/docs/api/storefront-web-components/custom-data)
    * attributes
    * components


Full index
# Getting started
This guide provides step-by-step instructions for adding Storefront Web Components to your website. If you want to use an LLM to generate code, include the [LLMs.txt](https://webcomponents.shopify.dev/llms.txt) file with your prompt to guide the model's output.
Install AI ToolkitAsk about this pageCopy MD
* * *
## 
[Anchor to Step 1: Connect your store](https://shopify.dev/docs/api/storefront-web-components/getting-started#step-1-connect-your-store)Step 1: Connect your store
Open the HTML file in the project where you want to use Storefront Web Components, and add the script tag shown here. Beneath it, add a [`<shopify-store>` component](https://shopify.dev/docs/api/storefront-web-components/components/shopify-store), with the domain of your store (for example, `https://demostore.mock.shop/`).
The `<shopify-store>` component supports optional country and language attributes that let you display pricing and content for a specific market.
You don't need an access token to use Storefront Web Components. However, if you want to display the inventory count or any custom data about a product, then you need to add an access token to the `<shopify-store>` component as well. To get an access token:
  1. Install the [Headless channel](https://apps.shopify.com/headless) from the Shopify App Store.
  2. To generate an access token, navigate to the Headless channel in your Shopify admin and click **Create storefront**.
  3. In the **Manage API access** section, click **Manage** for the Storefront API, and then copy the public access token.
  4. In your project, add a `public-access-token` attribute with your token to the `<shopify-store>` component (for example, `public-access-token="your-access-token"`).


Using LLMs with Storefront Web Components
If you want to use an LLM to generate code, include the [LLMs.txt](https://webcomponents.shopify.dev/llms.txt) file with your prompt to guide the model's output.
**Using LLMs with Storefront Web Components :**
If you want to use an LLM to generate code, include the [LLMs.txt](https://webcomponents.shopify.dev/llms.txt) file with your prompt to guide the model's output.
## Storefront Web Components setup
Copy
* * *
## 
[Anchor to Step 2: Set the context](https://shopify.dev/docs/api/storefront-web-components/getting-started#step-2-set-the-context)Step 2: Set the context
After adding the script tag and `<shopify-store>` component, add a [`<shopify-context>` component](https://shopify.dev/docs/api/storefront-web-components/components/shopify-context). This defines which Shopify data will be available.
Each `<shopify-context>` component requires two attributes:
  * `type`: Specifies what kind of data you want (for example, `product`).
  * `handle`: Identifies the specific item. For example, the handle for the URL [`demostore.hydrogen.mock.shop/products/men-t-shirt`](https://demostore.hydrogen.mock.shop/products/men-t-shirt?utm_source=docs) is `men-t-shirt`.


If you're working with a single storefront, then you can add the `<shopify-context>` component anywhere on your page (it doesn't need to be inside the `<shopify-store>` component). If you're working with multiple storefronts, then nest the context inside its corresponding store component.
Every `<shopify-context>` component also requires a template component, which contains the data you want to display. That template won't render until the context loads. You'll populate this component in the next step.
## Setup context
Copy
* * *
## 
[Anchor to Step 3: Load Shopify data](https://shopify.dev/docs/api/storefront-web-components/getting-started#step-3-load-shopify-data)Step 3: Load Shopify data
Inside a context template, you can use any standard HTML markup along with Shopify's data components.
The [`shopify-data`](https://shopify.dev/docs/api/storefront-web-components/components/shopify-data) component is used to display Shopify data on your page. Here's how it works:
  * It requires a `query` attribute that specifies which data to display.
  * The query uses dot notation to access data fields (for example, `query="product.title"`).
  * It looks for the nearest matching `<shopify-context>` component to find the data.
  * It outputs plain text that you can style with your own HTML elements.


In this example, `<shopify-data query="product.title">` finds the nearest product context (based on its `handle` attribute), accesses its `title` property, and displays it as text.
Since the component outputs a text node, to match your site's design you can wrap it in any necessary HTML elements. The component also supports rich text fields like `product.descriptionHtml`.
## Data loading
Copy
* * *
## 
[Anchor to Step 4: Format components](https://shopify.dev/docs/api/storefront-web-components/getting-started#step-4-format-components)Step 4: Format components
Some types of data , like `currency` and `media`, require extra formatting to display properly. For these types of data, you can use the following components:
  * [`shopify-money`](https://shopify.dev/docs/api/storefront-web-components/components/shopify-money): Accepts a query reference to a money object, and uses the store's country and language market to format it correctly.
  * [`shopify-media`](https://shopify.dev/docs/api/storefront-web-components/components/shopify-media): Accepts an image reference and generates an image element with `srcset` and `sizes` attributes.


## Formatting components
Copy
* * *
## 
[Anchor to Step 5: Connect to checkout](https://shopify.dev/docs/api/storefront-web-components/getting-started#step-5-connect-to-checkout)Step 5: Connect to checkout
You can add buttons to your components that let customers buy products, view product details, or [add products to their cart](https://shopify.dev/docs/api/storefront-web-components/components/shopify-cart).
To add a "Buy now" button that redirects the customer to the checkout page:
  1. Add a `button` component inside a [shopify-context component](https://shopify.dev/docs/api/storefront-web-components/components/shopify-context) that's associated with a product.
  2. Call the `buyNow()` method in the `button` component's `onclick` attribute, and make sure it includes an event object whose target is inside a `shopify-context` component.


When the customer clicks the button, the component will redirect them to the checkout page with the selected product.
To learn more about different button actions, see [Common patterns](https://shopify.dev/docs/api/storefront-web-components/common-patterns).
## Buy now button example
Copy
* * *
## 
[Anchor to Next steps](https://shopify.dev/docs/api/storefront-web-components/getting-started#next-steps)Next steps
Now that you've set up the basic Storefront Web Components, you can use others to add new types of data or functionality to your website. Components are available for common commerce features and design patterns, including:
  * [`shopify-list-context`](https://shopify.dev/docs/api/storefront-web-components/components/shopify-list-context): Displays multiple items in a repeating format, like a list of products or collections.
  * [`shopify-cart`](https://shopify.dev/docs/api/storefront-web-components/components/shopify-cart): Provides simple shopping cart using a native [HTML `<dialog>` element](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dialog).
  * [`shopify-variant-selector`](https://shopify.dev/docs/api/storefront-web-components/components/shopify-variant-selector): Creates a form that lets customers choose between different product options (like sizes, colors, or materials).


[ ![](https://shopify-assets.shopifycdn.com/shopifycloud/shopify-dev/production/assets/assets/images/icons/32/custom-storefronts-BaLaCBnH.png)![](https://shopify-assets.shopifycdn.com/shopifycloud/shopify-dev/production/assets/assets/images/icons/32/custom-storefronts-dark-BITMPSF8.png) ExploreStorefront Web Components playground Explore Storefront Web Components playground ](https://webcomponents.shopify.dev/playground)
[Explore - Storefront Web Components playground](https://webcomponents.shopify.dev/playground)
[ ![](https://shopify-assets.shopifycdn.com/shopifycloud/shopify-dev/production/assets/assets/images/icons/32/tutorial-B74KVyQw.png)![](https://shopify-assets.shopifycdn.com/shopifycloud/shopify-dev/production/assets/assets/images/icons/32/tutorial-dark-C9K_Le6U.png) Learn moreStorefront Web Components reference Learn more Storefront Web Components reference ](https://shopify.dev/docs/api/storefront-web-components/components/shopify-cart)
[Learn more - Storefront Web Components reference](https://shopify.dev/docs/api/storefront-web-components/components/shopify-cart)
* * *
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


Assistant

