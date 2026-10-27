[Help](https://help.shopify.com/en)
[Start for free](https://admin.shopify.com/signup?language=en)
[Log in](https://help.shopify.com/en/user/login)
Contents
# Understanding conditions for collections
You can add one or more conditions for a collection to match products or variants based on many details, including the title or type, tags, price, or inventory stock. A single collection can have a maximum of 60 total conditions.
Defining conditions for collections can help automatically organize products without manual management, saving time as your catalog grows. You can use conditions with collections that have **Products** or **Variants** [sources](https://help.shopify.com/en/manual/products/collections/create-collection#product-sources).
All the condition types on this page apply for setting conditions to include specific [products](https://help.shopify.com/en/manual/products/collections/create-collection#product-list) or [variants](https://help.shopify.com/en/manual/products/collections/create-collection#add-variants) in your collections. For [excluding specific products](https://help.shopify.com/en/manual/products/collections/create-collection#exclude-products) from a collection, only the [category](https://help.shopify.com/en/manual/products/collections/conditions#category), [tag](https://help.shopify.com/en/manual/products/collections/conditions#tags), [type, and vendor](https://help.shopify.com/en/manual/products/collections/conditions#title-type-vendor) condition types apply.
## On this page
  * [Set conditions based on product title, variant title, type, or vendor](https://help.shopify.com/en/manual/products/collections/conditions#title-type-vendor)
  * [Set conditions based on product category](https://help.shopify.com/en/manual/products/collections/conditions#category)
  * [Set conditions based on product tags](https://help.shopify.com/en/manual/products/collections/conditions#tags)
  * [Set conditions based on product status](https://help.shopify.com/en/manual/products/collections/conditions#status)
  * [Set conditions based on price, compare at price, weight, or inventory stock](https://help.shopify.com/en/manual/products/collections/conditions#set-conditions-based-on-price-compare-at-price-weight-or-inventory-stock)
  * [Set metafield definition conditions based on metafield values](https://help.shopify.com/en/manual/products/collections/conditions#set-metafield-definition-conditions-based-on-metafield-values)
  * [Set conditions based on metaobject reference metafields](https://help.shopify.com/en/manual/products/collections/conditions#set-conditions-based-on-metaobject-reference-metafields)
  * [Using multiple selection conditions](https://help.shopify.com/en/manual/products/collections/conditions#using-multiple-selection-conditions)
  * [Setting multiple conditions to define a range](https://help.shopify.com/en/manual/products/collections/conditions#setting-multiple-conditions-to-define-a-range)
  * [Troubleshooting collection conditions](https://help.shopify.com/en/manual/products/collections/conditions#troubleshooting-collection-conditions)


## Set conditions based on product title, variant title, type, or vendor
You can add a condition to include a product or variant in a collection based on the product title, variant title, type, or vendor. You can also use type or vendor conditions to exclude specific products from a collection.
Review the following table for details about how products are matched with the condition value that you set for product title, variant title, type, or vendor.  
Names and description of condition behaviors for adding products to collections.  
| Term  | Description  |  
| --- | --- |  
| **is equal to**  | The product title, variant title, type, or vendor needs to exactly match the whole value that you enter or select.  |  
| **is not equal to**  | The product title, variant title, type, or vendor can't match the value that you enter or select.  |  
| **starts with**  | The beginning of the product title, variant title, type, or vendor matches the value that you enter or select.  |  
| **ends with**  | The end of the product title, variant title, type, or vendor matches the value that you enter or select.  |  
| **contains**  | The product title, variant title, type, or vendor contains the value that you enter. You need to specify a value that is at least 3 characters long, and the value can't start or end with spaces.  |  
| **does not contain**  | The product title, variant title, type, or vendor doesn't contain the value that you enter. You need to specify a value that is at least 3 characters long, and the value can't start or end with spaces.  |  
## Set conditions based on product category
You can add a condition to include products or variants, or to exclude products, that have or don't have a particular [product category](https://help.shopify.com/en/manual/products/details/product-type#product-category-and-product-types). The **Product category** condition type has options of `is equal to` and `is not equal to` to control how a product or variant needs to match the condition values that you select.
For example, to set up a condition that selects products or variants with the product category `Electronics`:
  1. In a **Products** or **Variants** [source](https://help.shopify.com/en/manual/products/collections/create-collection#product-sources), click **![Add](https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/PlusCircleIcon.svg)Add condition** > **Product category**.
  2. In the second drop-down menu, select **is equal to**.
  3. Click the **Select category** field, and then select **Electronics**.


You can also include products from all sub-categories of a product category by selecting **Include subcategories** in the drop-down menu. This returns products for all categories that are children subcategories of the parent product category that you select.
For example, to set up a condition that selects products or variants with the product category `Toys & Games` and all of its sub-categories, such as `Puzzles`, `Card Games`, and `Bath Toys`:
  1. In a **Products** or **Variants** [source](https://help.shopify.com/en/manual/products/collections/create-collection#product-sources), click **![Add](https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/PlusCircleIcon.svg)Add condition** > **Product category**.
  2. In the second drop-down menu, select **is equal to**.
  3. Click the **Select category** field, select **Include subcategories** in the drop-down menu, and then click **Toys & Games**.


## Set conditions based on product tags
You can add a condition to include products or variants, or to exclude products, that have or don't have a particular [product tag](https://help.shopify.com/en/manual/products/details/tags). The **Tag** condition type has options of `includes` and `does not include` to control how a product or variant needs to match the condition values that you select.
#### Note
Although you can create product tags that use some special characters, they might not work as expected in searches or as conditions in your collections. Special characters in tags are either ignored or are treated as being the same.
For example, you have a condition for a collection of **Tag** > **includes** > **red-new**. All products that have the tags `red_new`, `red+new`, `red&new` are also included in the collection.
### Example: Set up a condition that includes products tagged with accessories
  1. In a **Products** or **Variants** [source](https://help.shopify.com/en/manual/products/collections/create-collection#product-sources), click **![Add](https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/PlusCircleIcon.svg)Add condition** > **Tag**.
  2. In the second drop-down menu, select **includes**.
  3. Click the **Select tag** field, and then select **Accessories**.


### Example: Set up a condition that excludes products tagged with accessories
  1. In a **Products** or **Variants** [source](https://help.shopify.com/en/manual/products/collections/create-collection#product-sources), click **![Add](https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/PlusCircleIcon.svg)Add condition** > **Tag**.
  2. In the second drop-down menu, select **does not include**.
  3. Click the **Select tag** field, and then select **Accessories**.


For more information about tags, refer to [_Tag formats_](https://help.shopify.com/en/manual/products/details/tags).
## Set conditions based on product status
You can add a condition to include products or variants that have or don't have a particular [product status](https://help.shopify.com/en/manual/products/details/product-details-page#product-status). The **Product status** condition type has options of `is equal to` and `is not equal to` to control how a product or variant needs to match the condition values that you select.
A product status condition can only add products or variants to a collection, and it isn't available in the **Exclude** section of a source. If a source uses **Match any condition** , then a product status condition adds every product or variant that matches the status, even when those products don't match the source's other conditions. To filter a collection by product status, use **Match all conditions** in the source.
#### Note
Archiving a product doesn't remove it from any collections that the product is included in. Archived products stay in collections and are listed in the **Collection items** section, but customers can't view them because archived products are hidden from your online store.
To set up a condition that selects only your archived products or variants for a collection that you keep unpublished to refer back to in your Shopify admin:
  1. In a **Products** or **Variants** [source](https://help.shopify.com/en/manual/products/collections/create-collection#product-sources), click **![Add](https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/PlusCircleIcon.svg)Add condition** > **Product status**.
  2. In the second drop-down menu, select **is equal to**.
  3. Click the **Select status** field, and then select **Archived**.


To set up a condition that keeps your archived products or variants out of a collection:
  1. In a **Products** or **Variants** [source](https://help.shopify.com/en/manual/products/collections/create-collection#product-sources), click **![Add](https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/PlusCircleIcon.svg)Add condition** > **Product status**.
  2. In the second drop-down menu, select **is not equal to**.
  3. Click the **Select status** field, and then select **Archived**.


Conditions apply only to products or variants that are matched automatically. If you [manually add products](https://help.shopify.com/en/manual/products/collections/create-collection#manual-add-products) to a collection, then a condition doesn't remove them. To take those products out of the collection, [remove the manually added products](https://help.shopify.com/en/manual/products/collections/manage-sources#remove-manually-added-products-or-variants).
## Set conditions based on price, compare at price, weight, or inventory stock
You can add a condition to include products or variants in a collection based on their price, compare at price, weight, or inventory stock.
Review the following table for details about how products are matched with the condition value that you set for price, compare at price, weight, or inventory stock.  
Names and description of condition behaviors for adding products to collections.  
| Term  | Description  |  
| --- | --- |  
| **is equal to**  | A product or variant's relevant value needs to exactly match the entered value.  |  
| **is not equal to**  | A product or variant's relevant value can't match the entered value.  |  
| **is greater than**  | A product or variant's relevant value is greater than the entered value.  |  
| **is less than**  | A product or variant's relevant value is less than the entered value.  |  
| **is not set**  | Applies only to the **Compare at price** condition. A product matches when any of its variants has an empty **[Compare-at price](https://help.shopify.com/en/manual/products/details/product-pricing/sale-pricing)** value.  |  
| **is set**  | Applies only to the **Compare at price** condition. A product matches when all of its variants have a **[Compare-at price](https://help.shopify.com/en/manual/products/details/product-pricing/sale-pricing)** value. The value can be 0.  |  
The behavior for **Compare at price** > **is not set** and **Compare at price** > **is set** is based on the values of all a product's variants in the following ways:
  * If any variant has an empty compare-at price, then the product matches the **is not set** condition.
  * For the **is set** condition, all variants must have a compare-at price value (including 0) for the product to match.


### Conditions for variants
When you have a **Products** source, and you set up a condition in the source that targets a product with variants, the condition is true if any variant matches the condition. This applies regardless of whether you select **Match all conditions** or **Match any condition** in the source.
For example, suppose you have a product with 5 variants. Four of the variants have inventory, but one is out of stock. If you have a collection that has a condition in a **Products** source of `Inventory stock is greater than 0`, then the product is included in the collection because at least one of the variants matches the condition.
#### Note
Variant titles are based on the option values for the variant, separated by spaces and a forward slash. For example, if a T-shirt variant has the option values `blue` and `large`, then its variant title is **blue / large**. Make sure to include the spaces on both sides of the forward slash when you enter a complete variant title.
## Set metafield definition conditions based on metafield values
You can add a condition to include products or variants that have a particular [metafield](https://help.shopify.com/en/manual/custom-data/metafields) value.
To have the metafields available to you when creating collections, you need to [activate the collections setting for the metafield definition](https://help.shopify.com/en/manual/custom-data/metafields/collections#activating-collections). You can have the collections setting activated on a maximum of 128 definitions per product metafield definitions and variant metafield definitions.
When a collection's source is set to **Variants** , category metafield conditions narrow the collection to specific variants only when the related product option is connected to a category metafield. Connected product options display the ![database](https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/DatabaseIcon.svg) icon on the product details page.
For example, if the **Color** option is connected to the **Color** category metafield, then the condition `Color is red` includes only variants with the `red` color option value.
If an option isn't connected to a category metafield, then a condition for that metafield can still match the product, but the condition doesn't narrow the collection to specific variants for that option.
For example, to set up a condition that selects products with the metafield definition `Color` and the value `#FF0000`:
  1. In a **Products** or **Variants** [source](https://help.shopify.com/en/manual/products/collections/create-collection#product-sources), click **![Add](https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/PlusCircleIcon.svg)Add condition** > **Metafield**.
  2. Select **Color** as the metafield definition.
  3. Click the **Select value** field, and then select **#FF0000**.


Learn more about [collections by metafields](https://help.shopify.com/en/manual/custom-data/metafields/collections).
Metafield types support the following conditions.  
Supported conditions for metafield types  
| Metafield definition type  | Conditions  |  
| --- | --- |  
| True or false  | The **True or false** metafield definition type supports the following conditions: 
  * is equal to

 |  
| Integer  | The **Integer** metafield definition type supports the following conditions: 
  * is equal to
  * is greater than
  * is less than

 |  
| Decimal  | The **Decimal** metafield definition type supports the following conditions: 
  * is equal to
  * is greater than
  * is less than

 |  
| Rating  | The **Rating** metafield definition type supports the following conditions: 
  * is equal to
  * is greater than
  * is less than

 |  
| Single line text  | The **Single line text** metafield definition type can be a single value or a list of values and supports the following conditions: 
  * is equal to

 |  
#### Note
Collections by metafields is available for both product and variant metafields.
## Set conditions based on metaobject reference metafields
You can add a condition to include a product or variant in a collection based on the value of a [metaobject reference metafield](https://help.shopify.com/en/manual/custom-data/metaobjects/referencing-metaobjects). You can set conditions for both product and variant metaobject reference metafields.
For example, to set up a condition that selects products with the metaobject reference metafield `Material` that has the value `Cotton`:
  1. In a **Products** or **Variants** [source](https://help.shopify.com/en/manual/products/collections/create-collection#product-sources), click **![Add](https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/PlusCircleIcon.svg)Add condition**.
  2. Click **Material**.
  3. In the second drop-down menu, select **is equal to**.
  4. Enter or select `Cotton` as the value.


Setting conditions based on metaobject reference metafields lets you create collections that are based on [standard taxonomy attributes](https://help.shopify.com/en/manual/products/details/product-category).
## Using multiple selection conditions
You can set more than one selection condition to control which products or variants are included in a collection. You can choose whether products or variants must match all the conditions to be included in the collection, or whether they can match any of the conditions.
For example, suppose that you set the following conditions for a collection:
  * Product tag is tagged with `shirt`.
  * Price is less than `$100.01 USD`.


If you select **Match all conditions** , then products or variants are included only if they're tagged with `shirt` and are also priced at $100 USD or less. Products or variants need to match both conditions to be included in the collection.
If you select **Match any condition** , then products or variants are included if they're tagged with `shirt` or if they're priced at $100 USD or less. Products or variants need to match only one condition to be included in the collection.
## Setting multiple conditions to define a range
To include products or variants with a price, weight, or inventory value that's within a specified range, you need to set more than one condition. The low end of the range is defined in one condition, and the high end of the range in a second condition. You need to select **Match all conditions** to include only the products or variants that fall within the range.
For example, to set up a collection that includes products or variants priced within a range of $50 USD to $150 USD, you would set up the following conditions:
  * Price is greater than `$49.99 USD`.
  * Price is less than `$150.01 USD`.


## Troubleshooting collection conditions
If you're experiencing issues with your collection conditions, then review the following troubleshooting information.
Troubleshoot collection contains incorrect products
In rare cases, collections might contain the wrong products. The collection might contain products that don't match its conditions, or fail to contain products that do match its conditions.
If this happens, then try the following workarounds to refresh the collection:
#### Refresh the collection by duplicating and removing a condition
  1. From your Shopify admin, go to [**Products**](https://admin.shopify.com/products) > [**Collections**](https://admin.shopify.com/collections).
  2. Click the collection that contains incorrect products.
  3. Choose any existing condition, such as "Product tag is equal to summer", and add a copy of that exact same condition. This forces the collection to update during the process of avoiding adding unwanted products to the collection.
  4. Click **Save**.
  5. Delete the duplicated condition and click **Save** again.
  6. Check to confirm if the issue has been resolved in both the Shopify admin and your storefront.


#### Refresh the collection by updating products
If only specific products are missing or incorrectly included, then you can force those products to update:
  1. From your Shopify admin, go to [**Products**](https://admin.shopify.com/products).
  2. Click the product that's missing from or incorrectly included in the collection.
  3. Make a minor change to the product, such as adding a space to the description or entering a compare-at price.
  4. Click **Save**.
  5. Revert the change by removing what you added.
  6. Click **Save** again.
  7. Refresh the collection page to confirm if the product is now correctly included or excluded from the collection.

Troubleshoot collection doesn't update when product or variant changes
If you make a change to a product or variant that should cause it to match or not match a collection's variant-based conditions, but the product remains incorrectly included or excluded from the collection, then you can resolve this by temporarily changing and then reverting the collection's conditions:
  1. From your Shopify admin, go to [**Products**](https://admin.shopify.com/products) > [**Collections**](https://admin.shopify.com/collections).
  2. Click the collection that isn't updating.
  3. In the **Conditions** section, make a temporary change to any condition. For example, change a price condition value by $0.01.
  4. Click **Save**. The collection refreshes. After the collection finishes refreshing, revert the condition to its original value.
  5. Click **Save** again.

Troubleshoot understanding condition operators
Review the following common issues with condition operators to ensure your collections work as expected.
#### Exact vs partial matching
When setting up conditions, it's important to understand the difference between exact and partial matching:
  * **is equal to** : A product must match exactly the whole value that you enter. For example, if you enter `summer sale`, only products with exactly that phrase will match, not products with `summer sale 2024`.
  * **contains** : The product attribute contains the value that you enter anywhere within it. For example, `sale` would match products with `summer sale`, `sale items`, or `clearance sale`.
  * **is not equal to** : A product can't match the exact value. This is different from **does not contain** , which means the value can't be included anywhere in the attribute.


#### Numeric operators and workarounds
Collections don't have "greater than or equal to" or "less than or equal to" operators. To include the target value in your range, offset the value by 1 cent:
  * To include products **priced at $100 USD or less** , use: Product price **is less than** `$100.01 USD`
  * To include products **priced at $50 USD or more** , use: Product price **is greater than** `$49.99 USD`


#### Compare-at price conditions
Compare-at price conditions have specific behaviors that might be unexpected:
  * **Zero (0) isn't the same as empty** : A compare-at price of $0.00 USD isn't considered empty. To find products with a compare-at price set (including zero), use **is set** or **is greater than** `0.00`.
  * **Variant-level evaluation** : If any variant of a product has an empty compare-at price, then the entire product matches the **is not set** condition. For **is set** , all variants must have a compare-at price value (including zero).
  * **Default is NULL** : By default, products and variants have a compare-at price value of NULL (empty), which isn't recognized by compare-at price conditions. You need to manually set a value on the product or variant for it to be recognized.
  * **Setting to $0.00 USD excludes from sale collections** : If you want to exclude a product from collections that use **compare-at price is set** , set the compare-at price to $0.00 USD.


#### Excluding products with "is not equal to"
When using **is not equal to** to exclude products based on categories such as Vendor or Type, the condition might not filter products correctly, especially when using multiple exclusions:
  * With **all conditions** , a product must not match any of the exclusion criteria to be included. This can be challenging when trying to exclude multiple vendors.
  * With **any condition** , a product is included if it doesn't match at least one exclusion criterion, which can inadvertently include products you want to exclude.


Consider using product tags with the **is equal to** condition instead for more reliable exclusions.
Leave feedback

