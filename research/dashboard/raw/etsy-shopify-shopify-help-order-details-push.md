[Help](https://help.shopify.com/en)
[Start for free](https://admin.shopify.com/signup?language=en)
[Log in](https://help.shopify.com/en/user/login)
Contents
# Viewing and managing order details
From the **Orders** page in your Shopify admin, you can click an order to view and manage its details. You can review its product information and subtotals, view its timeline, check its currency, add notes and tags, and contact your customer.
#### Note
The number next to the **Orders** tab in your Shopify admin is the count of your current open orders.
## On this page
  * [Understanding order product information](https://help.shopify.com/en/manual/fulfillment/managing-orders/managing-order-details#understanding-order-product-information)
  * [Understanding order subtotals](https://help.shopify.com/en/manual/fulfillment/managing-orders/managing-order-details#subtotal-calculations)
  * [View an order's Timeline](https://help.shopify.com/en/manual/fulfillment/managing-orders/managing-order-details#view-an-orders-timeline)
  * [Check an order's currency](https://help.shopify.com/en/manual/fulfillment/managing-orders/managing-order-details#check-an-order-s-currency)
  * [Attach a note or comment to an order](https://help.shopify.com/en/manual/fulfillment/managing-orders/managing-order-details#notes-comments)
  * [Attach an order tag](https://help.shopify.com/en/manual/fulfillment/managing-orders/managing-order-details#attach_an_order_tag)
  * [Contact a customer or resend an order email](https://help.shopify.com/en/manual/fulfillment/managing-orders/managing-order-details#contact-a-customer-or-resend-an-order-email)
  * [View the order status page](https://help.shopify.com/en/manual/fulfillment/managing-orders/managing-order-details#view-the-order-status-page)
  * [Subscribe to your orders feed](https://help.shopify.com/en/manual/fulfillment/managing-orders/managing-order-details#subscribe-to-your-orders-feed)
  * [Activate push notifications](https://help.shopify.com/en/manual/fulfillment/managing-orders/managing-order-details#activate-push-notifications)


## Understanding order product information
When you view an order, the product information displayed (such as product titles, prices, and weights) reflects what was true at the time the order was placed. This information is locked when the order is created and doesn't update when you change the product details in your Shopify admin.
If you click a product link in an order and it takes you to a product page with a different title or details, then it's because the product was updated after the order was placed. The product link in the order still points to the current version of that product, but the order itself displays the historical information from when the purchase was made.
This applies to all product details in an order, including the following information:
  * Product titles
  * Product descriptions
  * Prices and compare-at prices
  * Product weights
  * Variant names and options


## Understanding order subtotals
The subtotal displayed on the order details page in your Shopify admin is calculated differently from the subtotal data that's available through the Shopify API or apps such as Order Printer.
**Admin order page subtotal** : The subtotal displayed in your Shopify admin excludes discounts. Discounts are displayed as a separate line item.
**API and Order Printer subtotal** : Apps that use the Shopify API (such as Order Printer and third-party apps like Klaviyo) retrieve subtotal data that includes discounts already applied.
This means that the subtotal displayed in Order Printer templates or third-party app exports might be higher than the subtotal displayed on the order page in your admin. Both calculations are correct—they're just using different data points.
If you need the Order Printer or a third-party app to display subtotals that match your admin, then you might need to customize the template or app settings to calculate the subtotal in the same way as the admin (subtracting discounts from the line item totals).
## View an order's Timeline
You can view the detailed history of each order in the order's Timeline. You can also enter notes and comments in the Timeline.
You can also do the following from the Timeline:
  * communicate with staff
  * attach files
  * link to other products, orders, and customers


#### Steps:
Desktop
  1. From your Shopify admin, go to [**Orders**](https://admin.shopify.com/orders).
  2. Click the order that you want to view the timeline for.
  3. On the order details page, go to the **Timeline** section.

Mobile
  1. From the [Shopify app](https://www.shopify.com/install/detect), tap the ![Orders](https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/OrderIcon.svg) icon .
  2. Tap the order that you want to view the timeline for.
  3. On the order details screen, go to the **Timeline** section.


For more information, refer to [_Timeline_](https://help.shopify.com/en/manual/shopify-admin/productivity-tools/timeline).
#### Note
All notes and comments are internal and aren't visible to your customers.
### View payment events from the Timeline
When a customer pays for their order, the payment details are noted in the Timeline as a payment event. You can expand payment events for more details. Payment events can be helpful if you need to troubleshoot a failed payment capture or refund.
If your customer didn't complete the checkout, then instead go to the [abandoned checkout timeline](https://help.shopify.com/en/manual/promoting-marketing/create-marketing/abandoned-checkouts#view-payment-events) to view payment events.
#### Steps:
  1. From your Shopify admin, go to [**Orders**](https://admin.shopify.com/orders).
  2. Click the order that you want to view payment events for.
  3. On the order details page, go to the **Timeline** section.
  4. Click a payment event.
  5. For more details from the payment gateway, click **Information from the gateway**.


## Check an order's currency
If you're [selling in multiple currencies](https://help.shopify.com/en/manual/international/pricing) and a customer's payment is processed in a local currency through a compatible payment provider, then the **Paid** section displays the amount paid in the customer's currency, also called the presentment currency. If the customer's payment is converted back to your store currency at checkout, then the order doesn't display as a multi-currency order.
#### Steps:
  1. From your Shopify admin, go to [**Orders**](https://admin.shopify.com/orders).
  2. Click the order that you want to check the currency for.
  3. In the **Paid** section, review the amount paid in the customer's currency.
  4. In the payment section, review the order total and any currency conversion details.


## Attach a note or comment to an order
_Notes_ are messages or special instructions that have been included in an order. _Comments_ are for internal communication between staff members.
### Add a note
You can add or edit order notes in the **Notes** section of the order. Customers can also add notes to their order themselves when you have activated [order notes](https://help.shopify.com/en/manual/online-store/themes/customizing-themes/common-customizations/add-order-notes) in your store.
Desktop
  1. From your Shopify admin, go to [**Orders**](https://admin.shopify.com/orders).
  2. Click the order that you want to add a note to.
  3. In the **Notes** section, click the pencil icon.
  4. Write your note, and then click **Save**.

Mobile
  1. From the [Shopify app](https://www.shopify.com/install/detect), tap the ![Orders](https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/OrderIcon.svg) icon .
  2. Tap the order that you want to add a note to.
  3. Tap ![Horizontal menu](https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/MenuHorizontalIcon.svg) or ![Vertical menu](https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/MenuVerticalIcon.svg), and then tap **Add note**.
  4. Write your note, and then tap **Save** or **✓**.


### Add a comment
You can add internal comments or special instructions to the order using [Timeline](https://help.shopify.com/en/manual/shopify-admin/productivity-tools/timeline). Comments added to the Timeline can only be read by you and other staff members.
Desktop
  1. From your Shopify admin, go to [**Orders**](https://admin.shopify.com/orders).
  2. Click the order that you want to add a comment to.
  3. In the **Timeline** section, click the **Leave a comment...** text field, and then enter your comment. You can add emoji, mention a staff member, reference a page, or attach a file as well.
  4. Click **Post** to add the comment.

Mobile
  1. From the [Shopify app](https://www.shopify.com/install/detect), tap the ![Orders](https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/OrderIcon.svg) icon .
  2. Tap the order that you want to add a comment to.
  3. In the **Timeline** section, tap the **Leave a comment...** text field, and then enter your comment. You can add emoji, mention a staff member with **@** , or attach a photo or file by tapping the paperclip icon as well.
  4. Tap the paper airplane icon to post the comment.


## Attach an order tag
[Tags](https://help.shopify.com/en/manual/shopify-admin/productivity-tools/using-tags) help you categorize and organize your orders based on custom terms. To create an order view based on a tag, filter your store's orders by tag, then [save the results in the order view](https://help.shopify.com/en/manual/fulfillment/managing-orders/viewing-orders/searching-orders#edit-an-order-view).
#### Caution
Order tags are limited to 40 characters (letters and numbers) per tag. If you've created an order tag in the past that exceeds 40 characters, then you can't add it again to another order.
#### Steps:
Desktop
  1. From your Shopify admin, go to [**Orders**](https://admin.shopify.com/orders).
  2. Click the order that you want to tag.
  3. In the **Tags** section, add new tags or select from existing tags:
     * To add new tags, enter the tag names separated by a comma. For example, `urgent, reviewed, wholesale`.
     * To select from existing tags, click the pencil icon. Click the tags, then click **Done** to apply them to the order.

Mobile
  1. From the [Shopify app](https://www.shopify.com/install/detect), tap the ![Orders](https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/OrderIcon.svg) icon .
  2. Tap the order that you want to tag.
  3. In the **Tags** section, add new tags or select from existing tags:
     * To add new tags, tap **Add tag** and enter the tag names separated by a comma. For example, `urgent, reviewed, wholesale`.
     * To select from existing tags, tap **View all tags** , and then tap the tags.
  4. To apply the tags to the order, tap **Save** or **✓**.


You can also [bulk-edit order tags](https://help.shopify.com/en/manual/shopify-admin/productivity-tools/using-tags#bulk-edit-order-tags) from the **Orders** page.
## Contact a customer or resend an order email
You can contact a customer directly from the order page, or resend an order confirmation email to the customer or to yourself.
### Contact a customer about an order
Shopify stores all your customers' contact information. You can add additional contact information by clicking **Edit** in the **Contact** section of the order page and entering the details. If you give customers the option of entering either an email address or a phone number at checkout, then you might only have the contact information that they chose to enter in the **Contact** section. To contact a customer who chose to enter a phone number, call the number that they entered.
#### Steps:
Desktop
  1. From your Shopify admin, go to [**Orders**](https://admin.shopify.com/orders).
  2. Click the order from the customer that you want to contact.
  3. In the **Contact** section, click the customer's email address.
  4. In the **Contact customer** dialog, enter the message that you want to send.
  5. If you want to send a copy of your message to your own email address or the store owner's email, then click the box beside the address that you want to use. For more information on setting your store's email, refer to [changing your Shopify email address](https://help.shopify.com/en/manual/your-account/manage-orgs-and-stores/manage-store-details#manage-details).
  6. Click **Review email**.
  7. Review your email and then click **Send notification** , or click **Back** to make any changes.

Mobile
  1. From the [Shopify app](https://www.shopify.com/install/detect), tap the ![Orders](https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/OrderIcon.svg) icon .
  2. Tap the order from the customer that you want to contact.
  3. In the **Contact** section, tap one of the icons to contact the customer by email, phone call, or text message.


### Resend an order email
You can resend an order email to the customer, or send a copy to yourself for reference.
#### Steps:
  1. From your Shopify admin, go to [**Orders**](https://admin.shopify.com/orders).
  2. Click the order that you want to resend an email for.
  3. In the **Timeline** section, click **Resend email** under the email that you want to send again.
  4. In the **Resend order confirmation?** dialog, select the relevant option:
     * Resend the email to the customer
     * Send the email to yourself, so you can get a copy of the email that the customer received.
  5. Click **Send**.


## View the order status page
When your customers complete a checkout, they're given a URL to the order status page, which is the final page of the checkout process. They can track the status of their order on this page, and might contact you if they have questions.
For more information, refer to [_Order status page_](https://help.shopify.com/en/manual/fulfillment/setup/order-status-page).
#### Steps:
  1. From your Shopify admin, go to [**Orders**](https://admin.shopify.com/orders).
  2. Use the search box to find your customer's order. You can search for the order if you have any of the following information:
     * order number
     * receipt number if the order was created in Shopify POS
     * customer name
     * customer email address
  3. Click the order to view its details.
  4. Click the **More actions** menu, then click **View order status page**. You're redirected to the same order status page that your customer can view.


## Subscribe to your orders feed
You can track your store's orders using its RSS feed.
Your orders feed URL is:

```
https://admin.shopify.com/store/shopname/orders.rss
```

You can find your store's orders feed on the `/admin/feed` page in your Shopify admin.
#### Note
This is a protected feed that requires authentication to be read. Archived orders won't display in the feed.
## Activate push notifications
#### Note
When you activate notifications in the Shopify app, make sure to activate notifications in the main settings of your device.
You can set up push notifications in the [Shopify app](https://www.shopify.com/install/detect) to get instant alerts on your phone about the following important store updates:
  * Critical alerts
  * Fulfillments
  * New orders
  * Setup tips
  * Timeline mentions


iPhone
#### Steps:
  1. From the [Shopify app](https://www.shopify.com/install/detect), tap ![Menu](https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/MenuIcon.svg), and then tap ![Settings](https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/SettingsIcon.svg) **Settings**.
  2. In the **App settings** section, tap **Store notifications**.
  3. In the **Push notifications** section, activate the relevant options.


### Activate the Shopify app badge
If you activate push notifications for orders, then you can also activate the Shopify app badge to see how many open orders you have from your iPhone's home screen.
The Shopify app badge shows the number of open orders for one store only. If you're logged in to [more than one account](https://help.shopify.com/en/manual/your-account/logging-in) with the Shopify app, then the badge shows the number of open orders for the last account to have the option activated.
#### Steps:
  1. From the [Shopify app](https://www.shopify.com/install/detect), tap ![Menu](https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/MenuIcon.svg), and then tap ![Settings](https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/SettingsIcon.svg) **Settings**.
  2. In the **App settings** section, tap **Notifications**.
  3. In the **Orders** section, make sure that push notifications are activated.
  4. Activate the **Badge app icon** option.

Android
You can use the [Shopify app](https://www.shopify.com/install/detect) to activate push notifications so that you receive an alert on your phone whenever an order is placed with your store.
#### Steps:
  1. From the [Shopify app](https://www.shopify.com/install/detect), tap ![Menu](https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/MenuIcon.svg), and then tap ![Settings](https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/SettingsIcon.svg) **Settings**.
  2. Tap **Store notifications**.
  3. From the **Push notifications** screen, activate the notification by tapping the toggle button beside each option.


Leave feedback

