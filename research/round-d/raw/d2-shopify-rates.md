[Help](https://help.shopify.com/en)
[Start for free](https://admin.shopify.com/signup?language=en)
[Log in](https://help.shopify.com/en/user/login)
Contents
# Setting up shipping zones and rates
#### Note
Shipping profiles and shipping rates are gradually moving to [shipping options by market](https://help.shopify.com/en/manual/fulfillment/setup/shipping-options), a new way to manage shipping from your markets. Most stores still use shipping profiles and shipping rates, and your store keeps its current setup until it's upgraded. When your store is upgraded, your existing rates are migrated for you, so most merchants don't need to take any action. Learn more about [upgrading to shipping options by market](https://help.shopify.com/en/manual/fulfillment/setup/shipping-options/whats-changing-with-shipping).
Shipping zones and rates define where you ship your products to and how much you charge for shipping. A shipping zone is a group of countries or regions, such as Europe or North America. Within each zone, you create shipping rates that determine what your customers pay for shipping at checkout.
You can set up the following types of shipping rates:
  * **Flat rates** : You set the price and can offer different rate options:
    * **Flat** : General flat rate for all orders.
    * **Order amount** : Price-based rates with conditions on order value.
    * **Weight** : Weight-based rates with conditions based on the item weight.
  * **Carrier or app calculated rates** : Shipping carriers such as UPS or FedEx determine the shipping cost based on order details such as weight, dimensions, and destination.


You can also offer free shipping for any of the shipping rates that you set up.
## On this page
  * [Before you start](https://help.shopify.com/en/manual/fulfillment/setup/shipping-rates/setting-up-shipping-rates#before-you-start)
  * [Setting up flat shipping rates](https://help.shopify.com/en/manual/fulfillment/setup/shipping-rates/setting-up-shipping-rates#setting-up-flat-shipping-rates)
  * [Setting up carrier or app calculated shipping rates](https://help.shopify.com/en/manual/fulfillment/setup/shipping-rates/setting-up-shipping-rates#setting-up-carrier-or-app-calculated-shipping-rates)
  * [Add free shipping to your existing shipping option](https://help.shopify.com/en/manual/fulfillment/setup/shipping-rates/setting-up-shipping-rates#add-free-shipping-to-your-existing-shipping-option)
  * [Edit shipping zones and rates](https://help.shopify.com/en/manual/fulfillment/setup/shipping-rates/setting-up-shipping-rates#edit-shipping-zones-and-rates)
  * [Delete shipping zones and rates](https://help.shopify.com/en/manual/fulfillment/setup/shipping-rates/setting-up-shipping-rates#delete-shipping-zones-and-rates)
  * [Customer experience choosing shipping rates](https://help.shopify.com/en/manual/fulfillment/setup/shipping-rates/setting-up-shipping-rates#customer-experience-choosing-shipping-rates)


## Before you start
Before you set up shipping zones and rates, review the following information:
  * **Shipping profiles** : Get familiar with [shipping profiles](https://help.shopify.com/en/manual/fulfillment/setup/shipping-profiles). Shipping profiles let you create different shipping rules for specific products and locations. The instructions on this page apply to setting up zones and rates within a shipping profile.
  * **Markets** : If you want to sell to customers in a particular country, then the country must be in an active [market](https://admin.shopify.com/markets). To add a shipping zone for a new country, first [add a market](https://help.shopify.com/en/manual/markets/getting-started/set-up-markets#create-market) including that country, then activate the market and set up your rates. Customers in inactive markets can't place orders even when their country is in a shipping zone with available rates. Learn more about [shipping zones and markets](https://help.shopify.com/en/manual/international/shipping/shipping-zones).
  * **Shipping zone structure** : Within a group of locations in a shipping profile, a country or region can exist in only one shipping zone. You must remove a country or region from one shipping zone before adding it to another.
  * **Product weights** : If you plan to use weight-based shipping rates, then make sure that all your products have [weight values](https://help.shopify.com/en/manual/products/details/product-details-page#product-details-shipping). Without accurate weight information, shipping rates don't calculate correctly at checkout.
  * **Carrier or app calculated rates** : You can use built-in carrier integrations that are available on all plans, such as USPS in the United States or Canada Post in Canada. If you want to connect your own carrier accounts with carriers such as UPS, FedEx, or USPS, then you need to activate [third-party carrier-calculated shipping](https://help.shopify.com/en/manual/fulfillment/setup/shipping-rates/third-party-carrier-calculated-shipping) that requires specific Shopify plans or an additional monthly fee on your Shopify account.


## Setting up flat shipping rates
Flat rate shipping lets you set the shipping cost for orders. You can charge a fixed amount, offer free shipping, or vary the price based on order value or weight. For example, you can charge $10 USD for all orders, $5 USD for orders over $50 USD, or offer free shipping for orders over $100 USD.
#### Tip
By default, flat rates apply one time per order. If you want to charge shipping for each product in an order, then you need to set up separate shipping rates or use a third-party app. Most merchants charge a single flat rate per order regardless of the number of products.
### Set up flat shipping rates
  1. From your Shopify admin, go to **Settings** > [**Shipping and delivery**](https://admin.shopify.com/settings/shipping).
  2. In the **Shipping profiles** section, click the shipping profile that you want to add shipping rates to.
  3. Optional: To add a new shipping zone, complete the following steps:
    1. In the **Shipping zones** section, click **Add zone**.
    2. In the **Zone name** field, enter a name for your shipping zone.
    3. In the **Regions** section, select the countries and regions that are part of the zone, and then click **Done**.
  4. For the shipping zone where you want to add a shipping option, click **Add shipping option** , and then add shipping rates:
    1. In the **Name** field, add a name for your shipping option. This name is displayed to your customers at checkout.
    2. Optional: To add delivery details for your shipping option, such as `Tracked shipping`, click **Add delivery details** , and then enter the details. Delivery details are displayed to your customers at checkout.
    3. From the **Rate type** drop-down menu, select **Flat**.
    4. In the **Price** field, enter an amount that you charge your customers for this shipping option. To make the shipping rate free, leave this field empty or enter `0`.
    5. Optional: To display [transit time](https://help.shopify.com/en/manual/fulfillment/setup/shipping-rates/transit-time) to your customers at checkout, complete the following steps:
      1. From the **Transit time** drop-down menu, select a suggested transit time or enter a custom transit time
      2. If you select the **Custom** transit time, then enter a custom range or a single value for your transit time, such as `3-5 days` or `3 days`), and then click **Done**.
    6. Optional: To offer free shipping, select **Offer free shipping** , and then enter the minimum amount for an order to qualify for free shipping.
  5. Click **Done**.
  6. Click **Save**.


### Set up order amount-based rates
Order amount-based shipping rates, also known as price-based rates, let you charge different shipping prices based on the total value of the order.
For example, you can charge $24.99 USD shipping for orders from $0 USD to $100 USD, $9.99 USD shipping for orders from $100.01 USD to $200 USD, and offer free shipping for orders over $200.01 USD. Review the following table that displays example price-based rates:  
Example of price-based shipping rates  
| Order value  | Shipping rate price  |  
| --- | --- |  
| $0 USD - $100.00 USD  | $24.99 USD  |  
| $100.01 USD - $200.00 USD  | $9.99 USD  |  
| $200.01 USD and above  | $0 USD (free)  |  
When an order contains products from multiple shipping profiles, Shopify combines the applicable price-based rates. For example, if a `Discounted shipping` rate of $5 USD is active in two profiles for orders over $50 USD, then an order totaling $55 USD with products from both profiles displays a combined shipping rate of $10 USD at checkout.
#### Steps:
  1. From your Shopify admin, go to **Settings** > [**Shipping and delivery**](https://admin.shopify.com/settings/shipping).
  2. In the **Shipping profiles** section, click the shipping profile that you want to add shipping rates to.
  3. Optional: To add a new shipping zone, complete the following steps:
    1. In the **Shipping zones** section, click **Add zone**.
    2. In the **Zone name** field, enter a name for your shipping zone.
    3. In the **Regions** section, select the countries and regions that are part of the zone, and then click **Done**.
  4. For the shipping zone where you want to add a shipping option, click **Add shipping option** , and then add shipping rates:
    1. In the **Name** field, add a name for your shipping option. This name is displayed to your customers at checkout.
    2. Optional: To add delivery details for your shipping option, such as `Tracked shipping`, click **Add delivery details** , and then enter the details. Delivery details are displayed to your customers at checkout.
    3. From the **Rate type** drop-down menu, select **Order amount**.
    4. Set up your price ranges by entering the following information for each range:
      1. In the **Minimum** field, enter the minimum order value for this rate.
      2. In the **Maximum** field, enter the maximum order value for this rate. If you don't want a maximum limit, then leave this field empty.
      3. In the **Price** field, enter an amount that you charge your customers for this shipping rate. To make the shipping rate free, leave this field empty or enter `0`.
      4. Optional: From the **Transit time** drop-down menu, select a suggested transit time. If you select **Custom** transit time, then enter a custom range or a single value for your transit time, such as `3-5 days` or `3 days`, and click **Done**.
    5. To add additional price ranges, click the ![Plus icon](https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/PlusIcon.svg) icon.
    6. Optional: To offer free shipping, select **Offer free shipping** , and then enter the minimum amount for an order to qualify for free shipping.
  5. Click **Done**.
  6. Click **Save**.


### Set up weight-based rates
Weight-based rates let you charge different shipping prices based on the combined weight of items shipping from the same location with the same shipping option. Make sure that all your products have accurate weight data before setting up weight-based rates. If products are missing weight information, then shipping rates don't calculate correctly at checkout.
For example, you could charge $4.99 USD shipping for orders from 0 lb to 0.99 lb, $9.99 USD shipping for orders from 1 lb to 4.99 lb, and $19.99 USD shipping for orders from 5 lb to 9.99 lb. Review the following table that displays example weight-based rates:  
Example of weight-based shipping rates  
| Order total weight  | Shipping rate price  |  
| --- | --- |  
| 0 lb - 0.99 lb  | $4.99 USD  |  
| 1 lb - 4.99 lb  | $9.99 USD  |  
| 5 lb - 9.99 lb  | $19.99 USD  |  
When combining weight-based shipping rates, Shopify combines rates that apply to the weights of the individual products, with your [store default package](https://help.shopify.com/en/manual/fulfillment/setup/packaging/setting-up-packages#edit-store-default-package) weight added to each product. Learn more about [combined shipping rates](https://help.shopify.com/en/manual/fulfillment/setup/shipping-profiles/combined-shipping-rates).
#### Steps:
  1. From your Shopify admin, go to **Settings** > [**Shipping and delivery**](https://admin.shopify.com/settings/shipping).
  2. In the **Shipping profiles** section, click the shipping profile that you want to add shipping rates to.
  3. Optional: To add a new shipping zone, complete the following steps:
    1. In the **Shipping zones** section, click **Add zone**.
    2. In the **Zone name** field, enter a name for your shipping zone.
    3. In the **Regions** section, select the countries and regions that are part of the zone, and then click **Done**.
  4. For the shipping zone where you want to add a shipping option, click **Add shipping option** , and then add shipping rates:
    1. In the **Name** field, add a name for your shipping option. This name is displayed to your customers at checkout.
    2. Optional: To add delivery details for your shipping option, such as `Tracked shipping`, click **Add delivery details** , and then enter the details. Delivery details are displayed to your customers at checkout.
    3. From the **Rate type** drop-down menu, select **Weight**.
    4. Set up your weight ranges by entering the following information for each range:
      1. In the **Minimum** field, enter the minimum order weight for this rate.
      2. In the **Maximum** field, enter the maximum order weight for this rate. If you don't want a maximum limit, then leave this field empty.
      3. In the **Price** field, enter an amount that you charge your customers for this shipping rate. To make the shipping rate free, leave this field empty or enter `0`.
      4. Optional: From the **Transit time** drop-down menu, select a suggested transit time. If you select **Custom** transit time, then enter a custom range or a single value for your transit time, such as `3-5 days` or `3 days`, and click **Done**.
    5. To add additional weight ranges, click the ![Plus icon](https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/PlusIcon.svg) icon.
    6. Optional: To offer free shipping, select **Offer free shipping** , and then enter the minimum amount for an order to qualify for free shipping.
  5. Click **Done**.
  6. Click **Save**.


### Creating flat rates in local currencies
#### Note
Only stores using Shopify Payments can use this feature. Refer to the [list of supported countries](https://help.shopify.com/en/manual/payments/shopify-payments/supported-countries) to find out if Shopify Payments is available to you.
You can create flat rates in local currencies for customers from different markets. For example, you can offer $10 USD flat rate shipping for customers in the United States, but €15 EUR flat rate shipping for customers in Europe.
Shipping rates are automatically displayed in the customer's local currency when you [activate local currencies](https://help.shopify.com/en/manual/markets/getting-started/overview) for your market. If you want to set specific fixed rates for different regions rather than relying on automatic conversion, then create separate shipping zones for each region. For example, if your **Europe** market contains France, Germany, and Sweden, then automatic conversion displays your €10 EUR rate as approximately 120 SEK for Swedish customers. If you want to charge exactly 120 SEK for Sweden (rather than the converted amount), then create separate zones: one for Euro countries (France and Germany) with a €10 EUR rate, and another for Sweden with a 120 SEK rate.
## Setting up carrier or app calculated shipping rates
#### Caution
As of September 25, 2025, Canada Post is on strike. Shipments processed through Canada Post might be delayed.
For more information about the strike, refer to [Canada Post's page](https://www.canadapost-postescanada.ca/cpc/en/our-company/news-and-media/corporate-news/negotiations-list.page).
Carrier-calculated shipping rates display rates from carriers such as UPS, FedEx, or USPS at checkout. The carriers determine the rates based on the order details, including weight, dimensions, and destination. This helps you charge your customers the exact amount that a shipping carrier charges you when you purchase a shipping label.
Shipping carriers use the following factors when determining how much to charge for shipping:
  * Shipping origin
  * Shipping destination
  * Weight of the shipment
  * Value of the shipment
  * Dimensions of the shipment box
  * Dimensional weight
  * Requested speed of delivery


You need to enter accurate product weights to ensure accurate carrier-calculated rates at checkout. These rates display expected transit time, but they don't include your processing time. To display delivery dates that include both processing and transit time, refer to [Setting up delivery dates](https://help.shopify.com/en/manual/fulfillment/setup/delivery-expectations/manual-delivery-dates).
### Carrier-calculated rates availability
Carrier-calculated rates are available in specific scenarios. Review the following table to learn more about carrier-calculated rates and their availability in different regions:  
Carrier-calculated rates availability by fulfillment location  
| Fulfillment location  | Available carrier-calculated rates  |  
| --- | --- |  
| United States  | USPS, DHL, and UPS  |  
| Canada  | Canada Post and Purolator  |  
| United Kingdom  | DPD UK, InPost UK and Royal Mail  |  
| Italy  | BRT  |  
| Germany  | DHL Paket  |  
| Spain  | Seur  |  
#### Tip
The carrier-calculated rates in the table above use Shopify's built-in carrier integrations and are available on all plans. If you want to connect your own carrier accounts, then you need to [activate third-party carrier-calculated shipping](https://help.shopify.com/en/manual/fulfillment/setup/shipping-rates/third-party-carrier-calculated-shipping) and connect your carrier accounts. This requires specific Shopify plans or an additional monthly fee on your Shopify account.
### Set up carrier-calculated rates
  1. From your Shopify admin, go to **Settings** > [**Shipping and delivery**](https://admin.shopify.com/settings/shipping).
  2. In the **Shipping profiles** section, click the shipping profile that you want to add shipping rates to.
  3. Optional: To add a new shipping zone, complete the following steps:
    1. In the **Shipping zones** section, click **Add zone**.
    2. In the **Zone name** field, enter a name for your shipping zone.
    3. In the **Regions** section, select the countries and regions that are part of the zone, and then click **Done**.
  4. For the shipping zone where you want to add a shipping option, click **Add shipping option** , and then add shipping rates:
    1. Optional: To add delivery details for your shipping option, such as `Tracked shipping`, click **Add delivery details** , and then enter the details. Delivery details are displayed to your customers at checkout.
    2. From the **Rate type** drop-down menu, select **Carrier or app calculated**.
    3. Click **Choose carrier and apps** , and then complete the following steps:
      1. From the **Carrier or app** drop-down menu, select a shipping carrier or app.
      2. Select the shipping services that you want to display to your customers at checkout. If no services are available to select, then rates are displayed automatically by the carrier or app.
      3. Optional: To automatically include new shipping services when they become available, select **Automatically include new services when they become available**.
      4. Optional: In the **Handling fee** section, enter a percentage or a fixed amount to add to the carrier rate. You can use this to account for packaging and handling costs.
      5. Click **Done**.
    4. Optional: To offer free shipping when orders meet a minimum value, select **Offer free shipping** , and then enter the minimum amount for an order to qualify for free shipping.
  5. Click **Done**.
  6. Click **Save**.


### Mark up or discount carrier-calculated rates
You can adjust carrier-calculated shipping rates to mark up or discount the rates that display to your customers at checkout. For example, if the rate is too high to attract customers, then you could discount it by a certain percentage to increase sales. Instead, if the rate is too low to cover your packaging and handling costs, then you can increase it.
You can mark up carrier-calculated rates by an additional flat fee or by a percentage of the total shipping rate. If you adjust a carrier-calculated rate to include both an additional flat fee and a percentage markup, then the percentage is calculated before the flat fee is added. For example, a $5.00 USD rate with 50% markup and a $1.00 USD flat fee costs the customer $8.50 USD, not $9.00 USD.
If you want to offer discounted shipping, then enter a negative value, such as `-5`% or $`-2.50`.
#### Note
When [activating USPS calculated rates](https://help.shopify.com/en/manual/fulfillment/setup/shipping-rates/third-party-carrier-calculated-shipping/usps), you can activate the more expensive USPS retail rates instead of USPS commercial rates.
#### Steps:
  1. From your Shopify admin, go to **Settings** > [**Shipping and delivery**](https://admin.shopify.com/settings/shipping).
  2. In the **Shipping profiles** section, click the shipping profile that you want to edit.
  3. Next to the carrier-calculated rate that you want to adjust, click ![Horizontal menu](https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/MenuHorizontalIcon.svg), and then click **Edit shipping option**.
  4. In the **Handling fee** section, set the rate adjustments.
  5. Click **Done** , and then click **Save**.


#### Note
Your [store default package dimensions](https://help.shopify.com/en/manual/fulfillment/setup/packaging/packages-and-weights) are also used by your carrier to calculate shipping rates.
## Add free shipping to your existing shipping option
You can offer free shipping for your existing shipping option. You need to enter a minimum amount for an order to qualify for free shipping. For example, you can enter $50 USD as your minimum amount. This means that orders of $50 USD or more are eligible for free shipping.
#### Steps:
  1. From your Shopify admin, go to **Settings** > [**Shipping and delivery**](https://admin.shopify.com/settings/shipping).
  2. In the **Shipping profiles** section, click the shipping profile that you want to edit.
  3. In the **Shipping zones** section, click ![Horizontal menu](https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/MenuHorizontalIcon.svg) for the shipping option that you want to edit, and then click **Edit shipping option**.
  4. Select **Offer free shipping** , and then enter the minimum amount for an order to qualify for free shipping.
  5. Click **Done**.
  6. Click **Save**.


### Conditional rates and free shipping coverage
You can offer free shipping on any rate type. How free shipping applies depends on whether the rate has conditions:
  * **Rates with no conditions** : Free shipping applies to every order that the rate covers.
  * **Order amount-based or weight-based rates** : Free shipping applies only when an order falls within a tier that covers its total or weight.


When you use order amount-based or weight-based tiers, make sure that your tiers cover the full range of order totals or weights.
#### Caution
If an order falls outside your tiers, such as above your highest tier when that tier has a maximum value set, then no rate applies and the customer receives a shipping error at checkout. To prevent a coverage gap, leave the **Maximum** field empty on your highest tier so that it also covers larger orders.
### Adding free shipping for specific products or specific customers
You can add free shipping for specific products or specific customers:
  * To offer free shipping on only certain products, you need to [create a custom shipping profile](https://help.shopify.com/en/manual/fulfillment/setup/shipping-profiles/setting-up-shipping-profiles#set-up-general-profile) and include the relevant products, and then create a flat rate that offers free shipping.
  * To offer free shipping to specific customers, you need to [create a free shipping discount](https://help.shopify.com/en/manual/discounts/discount-methods/discount-codes). Customers who are eligible for the discount can enter the discount code during checkout, and then free shipping is applied to their order. If you want the customer to receive both a monetary discount and a free shipping discount, then [create a draft order](https://help.shopify.com/en/manual/fulfillment/managing-orders/create-orders) for your customer.


## Edit shipping zones and rates
  1. From your Shopify admin, go to **Settings** > [**Shipping and delivery**](https://admin.shopify.com/settings/shipping).
  2. In the **Shipping profiles** section, click the shipping profile that you want to edit.
  3. Next to the shipping zone or rate that you want to edit, click ![Horizontal menu](https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/MenuHorizontalIcon.svg).
  4. Click **Edit zone** or **Edit shipping option**.
  5. Make any changes, and then click **Done**.
  6. Click **Save**.


## Delete shipping zones and rates
  1. From your Shopify admin, go to **Settings** > [**Shipping and delivery**](https://admin.shopify.com/settings/shipping).
  2. In the **Shipping profiles** section, click the shipping profile that you want to edit.
  3. Next to the shipping zone or rate that you want to delete, click ![Horizontal menu](https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/MenuHorizontalIcon.svg).
  4. Click **Delete**.
  5. Click **Save**.


## Customer experience choosing shipping rates
Your shipping settings determine which rates display to customers at checkout. After you set up your shipping rates, you can place a test order to verify the rates your customers can choose from. Learn more about [troubleshooting and testing shipping rates](https://help.shopify.com/en/manual/fulfillment/setup/shipping-rates/troubleshooting).
Customers aren't offered any shipping rates until they enter a delivery address. After a customer enters a shipping address at checkout, applicable shipping rates display. Each customer is offered only rates that apply to their order, and the cheapest rate displays as the default. If a customer changes their order contents after reaching checkout, then shipping rates recalculate when they continue to the final purchase step.
Customers who enter a shipping address in a region that isn't included in your shipping zones receive a notice that no shipping rate is available for their region.
Leave feedback

