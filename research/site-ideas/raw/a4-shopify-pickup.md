[Help](https://help.shopify.com/en)
[Start for free](https://admin.shopify.com/signup?language=en)
[Log in](https://help.shopify.com/en/user/login)
Contents
# Setting up pickup in store for online orders
You can set up a pickup in store option in your checkout to let your customers pick up their online orders at one of your retail locations.
You can also set up store transfers for your pickup locations. Store transfers let you automatically transfer inventory from one or more locations to your pickup location when inventory is unavailable at the pickup location.
If your store is on the Shopify Plus plan, then you can replace the default pickup in store feature with a custom app.
## On this page
  * [Requirements for setting up pickup in store](https://help.shopify.com/en/manual/fulfillment/setup/delivery-methods/pickup-in-store#requirements-for-setting-up-pickup-in-store)
  * [Considerations for setting up pickup in store](https://help.shopify.com/en/manual/fulfillment/setup/delivery-methods/pickup-in-store#considerations-for-setting-up-pickup-in-store)
  * [Set up pickup in store](https://help.shopify.com/en/manual/fulfillment/setup/delivery-methods/pickup-in-store#set-up-pickup)
  * [Set up store transfers](https://help.shopify.com/en/manual/fulfillment/setup/delivery-methods/pickup-in-store#store-transfers)
  * [Set up transfer exclusions](https://help.shopify.com/en/manual/fulfillment/setup/delivery-methods/pickup-in-store#transfer-exclusions)
  * [Activate a pickup service](https://help.shopify.com/en/manual/fulfillment/setup/delivery-methods/pickup-in-store#activate-a-pickup-service)
  * [Transfer items manually](https://help.shopify.com/en/manual/fulfillment/setup/delivery-methods/pickup-in-store#transfer-items-manually)
  * [Fulfilling a pickup in store order](https://help.shopify.com/en/manual/fulfillment/setup/delivery-methods/pickup-in-store#fulfill)
  * [Checkout experience](https://help.shopify.com/en/manual/fulfillment/setup/delivery-methods/pickup-in-store#checkout-experience)
  * [Displaying pickup availability to your customers](https://help.shopify.com/en/manual/fulfillment/setup/delivery-methods/pickup-in-store#display-pickup)
  * [Turn off pickup in store](https://help.shopify.com/en/manual/fulfillment/setup/delivery-methods/pickup-in-store#turn-off-pickup-in-store)
  * [Troubleshooting pickup in store](https://help.shopify.com/en/manual/fulfillment/setup/delivery-methods/pickup-in-store#troubleshooting-pickup-in-store)


## Requirements for setting up pickup in store
To set up pickup in store in your Shopify admin, you need to meet the following requirements:
  * You need to have at least one [location that fulfills online orders](https://help.shopify.com/en/manual/inventory-and-locations/locations/fulfillment).
  * Your store needs to use the latest version of checkout. If you aren't using the latest version of checkout, then an upgrade notice is displayed in **Settings** > [**Checkout**](https://admin.shopify.com/settings/checkout).


## Considerations for setting up pickup in store
Before you set up pickup in store, review the following considerations:
  * A customer can choose to have some items shipped and some items picked up in the same order. If a store transfer is needed for pickup items, then the checkout displays an estimated pickup time that accounts for the transfer.
  * If you use a theme that supports pickup availability, then the customer can view whether a product is available for pickup before they add it to their cart. Products that are available through a [store transfer](https://help.shopify.com/en/manual/fulfillment/setup/delivery-methods/pickup-in-store#store-transfers) are displayed as available for pickup, with an adjusted estimated pickup time.


#### Plan requirement
Shopify Plus and Enterprise only: If you've activated the [ship and pickup in one order feature test drive](https://help.shopify.com/en/manual/checkout-settings/ship-and-pickup), then you must have at least 1 location set to offer in-store pickup to use the feature.
## Set up pickup in store
You can set up pickup in store for your locations. You need to set up pickup in store for each location where customers can pick up their orders.
#### Steps:
  1. From your Shopify admin, go to **Settings** > [**Shipping and delivery**](https://admin.shopify.com/settings/shipping).
  2. In the **Additional delivery methods** section, click **Pickup in store**.
  3. Click the location that you want to activate pickup in store for.
  4. In the **Location status** section, activate the **Let customers pick up orders directly at this location** option.
  5. In the **Expected pickup date** section, select a processing time for in-store pickup from the drop-down menu. This information is displayed to your customers.
  6. Optional: To [set up store transfer](https://help.shopify.com/en/manual/fulfillment/setup/delivery-methods/pickup-in-store#store-transfers), complete the following tasks:
    1. In the **Store transfers** section, select the locations that you want to transfer inventory from when inventory is unavailable at the in-store pickup location.
    2. To set up a different processing time for orders that require a store transfer, select **Set a different processing time at checkout when a store transfer is needed** , and then select a processing time from the drop-down menu.
  7. In the **Ready for pickup notification** section, enter pickup instructions for your customers. This field replaces any customizations that you have in the `email_body` variable in the **Ready for pickup** notification template.
  8. Optional: In the **Checkout preview** section, preview how your in-store pickup option displays at checkout.
  9. Click **Save**.


## Set up store transfers
By default, pickup in store is available only when the entire order is in stock at the pickup location. If you have multiple locations, then you can set up store transfers that let you transfer inventory from one or more locations to your pickup location. You can also set up different processing times for orders that require a store transfer. If no single location can transfer all of the inventory, then multiple transfers are created for the order. Locations closest to the pickup location with available inventory are prioritized.
#### Steps:
  1. From your Shopify admin, go to **Settings** > [**Shipping and delivery**](https://admin.shopify.com/settings/shipping).
  2. In the **Additional delivery methods** section, click **Pickup in store**.
  3. Click a location that you want to set up store transfers for.
  4. In the **Store transfers** section, select the locations that you want to transfer inventory from when inventory is unavailable at the pickup location.
  5. Optional: To set up a different processing time for orders that require a store transfer, select **Set a different processing time at checkout when a store transfer is needed** , and then select a processing time from the drop-down menu.
  6. Click **Save**.


## Set up transfer exclusions
You can exclude specific product collections from store transfers. For example, if some of your products are too large to transfer to a pickup location, then you can exclude these products from store transfers. You can exclude product collections, but not specific products.
Before you begin, [create a collection](https://help.shopify.com/en/manual/products/collections) for products that can't be transferred to a pickup location. To avoid displaying your collection to customers, ensure that the collection isn't included in any sales channels.
#### Steps:
  1. From your Shopify admin, go to **Settings** > [**Shipping and delivery**](https://admin.shopify.com/settings/shipping).
  2. In the **Additional delivery methods** section, click **Pickup in store**.
  3. In the **Transfer exclusions** section, click **Add collections**.
  4. Select any collections that you want to exclude from store transfers, and then click **Done**.
  5. Click **Save**.


## Activate a pickup service
#### Plan requirement
This feature is available only to stores on the Shopify Plus plan.
If you want to use a custom app to manage pickup in store, then you can activate a pickup service in your Shopify admin and replace the existing pickup in store settings. Learn more about [custom pickup in store apps](https://shopify.dev/docs/apps/fulfillment/order-routing-apps/local-pickup-delivery-option-generators).
#### Steps:
  1. From your Shopify admin, go to **Settings** > [**Shipping and delivery**](https://admin.shopify.com/settings/shipping).
  2. In the **Additional delivery methods** section, click **Pickup in store**.
  3. In the **Pickup service** section, click **Change**.
  4. Select a custom app that you want to use for your pickup in store feature, and then click **Save**.
  5. Click **Choose pickup service**.


## Transfer items manually
If you can't fulfill a pickup in store order and need to transfer items from somewhere else, or the automatically chosen location for a store transfer isn't possible, then you can manually change the location of a pickup in store order. You can't change the pickup location chosen by the customer at checkout.
#### Steps
  1. From your Shopify admin, go to [**Orders**](https://admin.shopify.com/orders).
  2. Click the pickup in store order that you want to fulfill.
  3. In the **Unfulfilled** section, click the ![Horizontal menu](https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/MenuHorizontalIcon.svg) button.
  4. Click **Change location**.
  5. Select the items to choose a new location for.
  6. In the **Change location** section, select a new location.
  7. Click **Change location**.


## Fulfilling a pickup in store order
You can fulfill a pickup in store order from your Shopify admin by marking it as ready for pickup and then marking it as picked up after the customer collects their order. At each stage, you can send notification emails to keep your customer informed. If a product transfer is required for your pickup in store order, then the **Transfer required** badge is displayed next to your pickup location.
### Mark an order as ready for pickup
When you mark an order as ready for pickup, a **Ready for pickup** notification email is sent to your customer. You can view or resend this email from the [order timeline](https://help.shopify.com/en/manual/fulfillment/managing-orders/managing-order-details#view-an-orders-timeline). 
#### Steps:
  1. From your Shopify admin, go to [**Orders**](https://admin.shopify.com/orders).
  2. Click the pickup in store order that you want to fulfill.
  3. Optional: If a transfer is required to move items to the pickup location, then click **Transfer to pickup location** when you make the necessary preparations. You can undo this action only by [transferring the items manually](https://help.shopify.com/en/manual/fulfillment/setup/delivery-methods/pickup-in-store#transfer-items-manually).
  4. Click **Ready for pickup**.
  5. Click **Mark as ready for pickup**.


### Mark an order as picked up
After your customer picks up their order, you can mark the order as picked up and send a confirmation email.
#### Steps:
  1. From your Shopify admin, go to [**Orders**](https://admin.shopify.com/orders).
  2. Click the pickup in store order that you want to mark as picked up.
  3. Click **Mark as picked up**.
  4. Optional: To send the **Picked up by customer** confirmation email to your customer, select **Send notification to customer**.
  5. Click **Mark as picked up** to mark the order as fulfilled.


## Checkout experience
After you activate pickup in store, your customers can choose between **Ship** and **Pick up** options in the **Delivery** section of your checkout. When they select the **Pick up** option, they can choose the location where they want to pick up their order. Customers can view pickup locations only in their country. If there are no pickup locations in their country, then **There are no pickup locations available** displays during checkout. They can change their country by clicking **Change my location**.
The processing time that you select in the pickup in store settings is displayed at checkout.
## Displaying pickup availability to your customers
Some themes let you display to customers whether a product is available for pickup in store. On each product page, a pickup availability section displays whether the product is available, and the estimated time frame for pickup.
After pickup in store is activated, the product page displays whether the product is available for pickup at one or more of your pickup locations. This information is displayed only for products that are stocked at least one pickup location and have the **Physical product** setting activated in the **Shipping** section of a product variant's details.
If you have pickup in store activated for only one location, then the location and pickup availability is displayed for that location. Customers can click **View store information** to learn more about the pickup location.
If you have pickup in store activated for more than one location, then the pickup availability section displays the location and pickup availability for one of your stores. Customers can click **Check availability at other stores** to check the product's availability at all of your locations that have pickup activated.
This feature is currently available in [Dawn](https://themes.shopify.com/themes/dawn/styles/default), the [Horizon family of themes](https://themes.shopify.com/collections/horizon-themes), and multiple paid themes in the [Shopify Theme Store](https://themes.shopify.com/themes?product-page=product-pickup-availability).
#### Grow your business
If pickup in store availability isn't available in your theme, then you can hire a Shopify Partner to help you to add it. Learn more about [hiring a Shopify Partner](https://help.shopify.com/en/manual/partner-directory).
## Turn off pickup in store
If you no longer want to offer pickup in store at your location, then you can turn it off.
#### Steps:
  1. From your Shopify admin, go to **Settings** > [**Shipping and delivery**](https://admin.shopify.com/settings/shipping).
  2. In the **Pickup in store** section, click the **›** icon.
  3. Click a location where you want to turn off pickup in store.
  4. Click **Turn off pickup in store**.
  5. In the dialog, click **Turn off pickup in store**.


## Troubleshooting pickup in store
If you're experiencing issues with pickup in store, then review the following common issues and solutions.
Troubleshoot ready for pickup notification showing different content than template
If the **Ready for pickup** notification that customers receive is different from your template in **Settings** > **Notifications** , then this might be caused by location-specific pickup instructions.
Location-specific pickup instructions override the general notification template. If you've added custom pickup instructions in the location settings, then these instructions are used in the notification instead of the content in your notification template.
To resolve this issue, complete one of these tasks:
  * Edit or remove the pickup instructions in your location settings. From your Shopify admin, go to **Settings** > [**Shipping and delivery**](https://admin.shopify.com/settings/shipping) > **Pickup in store** , click the location, and then edit the **Ready for pickup notification** section.
  * Remove the `{{ pickup_instructions }}` variable from your notification template. From your Shopify admin, go to **Settings** > [**Notifications**](https://admin.shopify.com/settings/notifications) > **Ready for pickup** , and then remove the `{{ pickup_instructions }}` variable from the template.


#### Note
Location-specific pickup instructions are used in the notification even if the pickup option has been deactivated, as long as the order was set to be picked up at that location.
Troubleshoot error: Your order isn't available for pickup
If customers get the error `Your order isn't available for pickup. Enter a shipping address` at checkout, then this is caused by a missing shipping zone for your pickup location.
This error appears when there's no shipping zone associated with the physical location where customers pick up orders. In your shipping settings, `Not shipping from` might display next to your pickup location.
To resolve this issue:
  1. From your Shopify admin, go to **Settings** > **Shipping and delivery**.
  2. In the shipping zone for your pickup location, click **Add rate** > **New rate**.
  3. Click **Done** without adding any actual shipping rates.


You don't need to add shipping rates to the zone. The zone itself needs to exist for the pickup location to work properly.
Leave feedback

