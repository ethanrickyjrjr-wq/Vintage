[Help](https://help.shopify.com/en)
[Start for free](https://admin.shopify.com/signup?language=en)
[Log in](https://help.shopify.com/en/user/login)
Contents
# Hiding out of stock products
You can use [collections](https://help.shopify.com/en/manual/products/collections/create-collection) to hide out of stock products from your customers. You can [do this manually](https://help.shopify.com/en/manual/inventory-and-locations/setup/hide-out-of-stock#hide-out-of-stock-products-from-your-collections) on the **Collections** page of your Shopify admin, or use an inventory management app to do it for you.
Consider also hiding products in your store's default **Catalog** collection.
## On this page
  * [Hide out of stock products from your collections](https://help.shopify.com/en/manual/inventory-and-locations/setup/hide-out-of-stock#hide-out-of-stock-products-from-your-collections)
  * [Hide out of stock products in your default Catalog collection](https://help.shopify.com/en/manual/inventory-and-locations/setup/hide-out-of-stock#hide-out-of-stock-products-in-your-default-catalog-collection)
  * [Hide out of stock products using an app](https://help.shopify.com/en/manual/inventory-and-locations/setup/hide-out-of-stock#hide-out-of-stock-products-using-an-app)
  * [Hide out of stock products using Shopify Flow](https://help.shopify.com/en/manual/inventory-and-locations/setup/hide-out-of-stock#hide-out-of-stock-products-using-shopify-flow)


## Hide out of stock products from your collections
Before you can hide out of stock products from your collections, you need to turn on inventory tracking in your Shopify admin. Inventory tracking automatically keeps track of the inventory level of each product that you carry.
When you hide out of stock products, they're removed from your collections and won't be displayed to your customers. Any out of stock products display in your collections again after you receive inventory.
#### Steps:
  1. [Turn on inventory tracking for your products](https://help.shopify.com/en/manual/inventory-and-locations/setup/initial-inventory-setup).
  2. [Change the collection conditions](https://help.shopify.com/en/manual/products/collections/conditions) for each of your collections, and add the following conditions:
     * For **Inventory stock** , select **is greater than** and enter `0`.
     * Select **Match all conditions**.


#### Note
This solution for hiding out of stock products won't work if you set **Products must match** to **any condition**.
## Hide out of stock products in your default Catalog collection
By default, your store comes with a collection that displays all your in stock products at the URL `your-store.myshopify.com/collections/all`. You can hide out of stock products from this collection.
#### Steps:
  1. Take control of your Catalog page by [overriding it with your own collection](https://help.shopify.com/en/manual/online-store/themes/customizing-themes/common-customizations/change-catalog-page).
  2. [Set the automated conditions](https://help.shopify.com/en/manual/products/collections/conditions) of that collection to hide out of stock products.


## Hide out of stock products using an app
If you don't want to [change your collections](https://help.shopify.com/en/manual/inventory-and-locations/setup/hide-out-of-stock#hide-out-of-stock-products-from-your-collections) to hide out of stock products, then you can use an [inventory management app](https://apps.shopify.com/categories/inventory) from the Shopify App Store. Some of these apps can automatically hide or delete products from your store when they're out of stock.
## Hide out of stock products using Shopify Flow
You can [create a workflow](https://help.shopify.com/en/manual/shopify-flow/create/create-workflow) using Shopify Flow to automate actions on products based on their inventory level:
  * To use a pre-built workflow, use the **Publish and unpublish products based on inventory level** template in Shopify Flow.
  * To build a workflow manually, you can use the **Product variant inventory quantity changed** trigger to start a workflow that checks the `productVariant.inventoryQuantity` variable value and includes the **Unpublish product** action when your conditions are met.


[Learn more about inventory and merchandising workflows](https://help.shopify.com/en/manual/shopify-flow/getting-started/workflow-examples#inventory-and-merch).
Leave feedback

