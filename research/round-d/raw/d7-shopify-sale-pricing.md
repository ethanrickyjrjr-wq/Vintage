[Help](https://help.shopify.com/en)
[Start for free](https://admin.shopify.com/signup?language=en)
[Log in](https://help.shopify.com/en/user/login)
Contents
# Setting sale prices for products
When you lower the price of a product, you might want a customer to be able to understand the price comparison.
To set a sale price, set the value of the **Compare-at price** field in your Shopify admin to the original price of the product. Make sure that the value in the **Compare-at price** field is higher than the value in the **Price** field to display the sale price.
Using sale prices is different from setting up [discounts](https://help.shopify.com/en/manual/discounts). If you set a sale price and a compare-at price, then both these amounts can be displayed on product pages and collection pages, but only the sale price is displayed at checkout.
To display savings from [discounts](https://help.shopify.com/en/manual/discounts) with crossed-out (strikethrough) prices on product pages and collection pages, you need to use a [third-party discount app](https://apps.shopify.com/categories/marketing-and-conversion-promotions-discounts?&programs%5B%5D=built_for_shopify), or [hire a Shopify Partner](https://help.shopify.com/en/manual/partner-directory) to build a custom solution for you. Savings from automatic discounts or discounts that require a code to be entered are always displayed with a crossed-out price at checkout.
#### Note
[Fixed prices](https://help.shopify.com/en/manual/markets/customizations/catalogs) override prices and compare-at prices set in your Shopify admin.
To create fixed [sale prices](https://help.shopify.com/en/manual/products/details/product-pricing/sale-pricing) for products in your international markets, you can [import prices using a CSV file](https://help.shopify.com/en/manual/markets/customizations/catalogs#import-export). Sale prices can't be created within the Shopify admin.
## On this page
  * [Displaying sale prices](https://help.shopify.com/en/manual/products/details/product-pricing/sale-pricing#displaying-sale-prices)
  * [Example of setting a sale price](https://help.shopify.com/en/manual/products/details/product-pricing/sale-pricing#example-of-setting-a-sale-price)
  * [Setting a compare-at price](https://help.shopify.com/en/manual/products/details/product-pricing/sale-pricing#set-a-compare-at-price-for-a-product)
  * [Troubleshooting sale prices](https://help.shopify.com/en/manual/products/details/product-pricing/sale-pricing#troubleshooting-sale-prices)


## Displaying sale prices
You set sale prices in your Shopify admin. Your theme controls whether sale prices are displayed on your storefront, and where they're displayed.
For example, your theme might add a badge with a message or percentage off to product listing and collection pages. Sale price styling on your storefront can often be customized through [your theme settings](https://help.shopify.com/en/manual/online-store/themes/customizing-themes/theme-editor/theme-settings). Refer to your theme's documentation or [contact your theme's developer for support](https://help.shopify.com/en/manual/online-store/themes/theme-support#where-to-find-support-for-your-theme) to learn what customization settings are available.
Your theme doesn't control how sale prices are displayed on AI channels that find products through Shopify Catalog, such as ChatGPT and Microsoft Copilot. If your store is eligible for Shopify Catalog, then you can [choose whether Shopify Catalog uses the price or the compare-at price as the list price](https://help.shopify.com/en/manual/shopify-catalog/mapping#compare-at-prices) for AI agents. Each AI channel decides whether to display the list price next to the current price.
## Example of setting a sale price
For example, you sell t-shirts with seasonal designs for $30. At the beginning of a new season, you put the previous season's designs on sale for $10.
In your Shopify admin, you change the **Price** value to `$10 USD`, and then set the **Compare-at price** value to `$30 USD`. On your storefront, your theme displays both prices alongside a badge with a sale message.
## Setting a compare-at price
You can set a compare-at price value for a product or variant from the product details page of your Shopify admin. You can also [bulk edit multiple variants](https://help.shopify.com/en/manual/products/variants/edit-variants#edit-variant-details-in-bulk) and [bulk edit multiple products](https://help.shopify.com/en/manual/shopify-admin/productivity-tools/bulk-editing#select-bulk).
#### Steps:
Desktop
  1. From your Shopify admin, go to [**Products**](https://admin.shopify.com/products).
  2. Click the product that you want to edit.
  3. To edit a variant, in the **Variants** section, click **`XX` variants**.
  4. In the **Price** section, complete the following steps:
    1. Click **Compare at**.
    2. In the **Compare-at price** field, enter the original price.
    3. In the **Price** field, enter the new price.
  5. Click **Save**.

Mobile
  1. From the [Shopify app](https://www.shopify.com/install/detect), tap the ![Products](https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/ProductIcon.svg) icon .
  2. Tap the product that you want to edit.
  3. To edit a product, tap the product price area. To edit a variant, complete the following steps:
    1. In the **Variants** section, tap **`XX` variants**.
    2. Tap the variant that you want to edit.
    3. Tap the product variant price area.
  4. In the **Compare-at price** field, enter the original price.
  5. In the **Price** field, enter the new price.
  6. Tap **Save** or **✓**.


## Troubleshooting sale prices
If you're experiencing issues with sale prices, then review the following troubleshooting information.
Compare-at price doesn't display on collection pages
If your compare-at price displays correctly on product pages but doesn't display on collection pages, then it's likely because some variants have conflicting compare-at pricing.
When a product is displayed on a collection page, the product displays the most general information that applies to all variants. If some variants have compare-at prices that are inconsistent (such as some variants having a compare-at price of $0.00 USD, or some being empty, or different values across variants), then the collection page won't display the product as being on sale, even if individual variants are.
On product pages, the compare-at price displays correctly because it displays the pricing for the specific variant that's selected.
To resolve this issue, make sure all variants have consistent compare-at pricing:
  1. From your Shopify admin, go to [**Products**](https://admin.shopify.com/products).
  2. Click the product with the issue.
  3. In the **Variants** section, review the compare-at prices for all variants.
  4. Either remove all conflicting compare-at pricing and leave them blank, or ensure all compare-at prices are higher than their respective regular prices. A compare-at price of $0.00 USD isn't the same as an empty compare-at price. Make sure to clear the field entirely for variants that shouldn't display a compare-at price.
  5. Click **Save**.


Leave feedback

