[Help](https://help.shopify.com/en)
[Start for free](https://admin.shopify.com/signup?language=en)
[Log in](https://help.shopify.com/en/user/login)
Contents
# Setting up staff notifications
#### Note
Account owners receive notifications on all new orders by default. This can be deactivated by going to **Settings** > **Notifications** > **Staff notifications**.
You can create and edit email notifications to let you or staff know when the following events occur in your Shopify admin:
  * **Store order summary** : A summary of your store orders, sales, and top products for the week. Sent by default every Monday at 9AM in your local timezone. You can specify the day and time in your notification settings, and you can set it to daily instead and choose the time. Recipients with this staff notification activated receive the notification regardless of their order or location permissions.
  * **New order** : Sent when a customer places an order.
  * **New return request** : Sent when a customer requests a return on an order.
  * **Sales attribution ended** : Sent to order notification recipients when the attributed staff on an order is edited.
  * **New draft order** : Sent when a customer submits a draft order. Only sent to the store owner.
  * **Order dispute updates** : Sent when a chargeback or inquiry is opened, escalated, reopened, won, lost, or prevented, and when evidence is submitted.


You need the **Orders** and **Manage settings** permissions to make changes to order notifications. Learn more about [staff permissions](https://help.shopify.com/en/manual/your-account/users/roles/permissions).
## On this page
  * [Add a recipient for staff notifications](https://help.shopify.com/en/manual/fulfillment/setup/notifications/staff-notifications#add-a-recipient-for-staff-notifications)
  * [Deactivate or reactivate staff notifications](https://help.shopify.com/en/manual/fulfillment/setup/notifications/staff-notifications#adjust-new-order-notifications)
  * [Edit staff notifications sent to a recipient](https://help.shopify.com/en/manual/fulfillment/setup/notifications/staff-notifications#edit-staff-notifications-sent-to-a-recipient)
  * [Delete a staff order notification recipient](https://help.shopify.com/en/manual/fulfillment/setup/notifications/staff-notifications#delete-a-staff-order-notification-recipient)
  * [Order dispute updates](https://help.shopify.com/en/manual/fulfillment/setup/notifications/staff-notifications#order-dispute-updates)
  * [Customize the timing and frequency of your Store order summary](https://help.shopify.com/en/manual/fulfillment/setup/notifications/staff-notifications#customize-the-timing-and-frequency-of-your-store-order-summary)
  * [Customize new order template](https://help.shopify.com/en/manual/fulfillment/setup/notifications/staff-notifications#customize-new-order-template)


## Add a recipient for staff notifications
Desktop
  1. From your Shopify admin, go to **Settings** > [**Notifications**](https://admin.shopify.com/settings/notifications).
  2. Click **Staff notifications**.
  3. In the **Recipients** section, click **Add recipient**.
  4. From the first drop-down menu, select the notification recipient from the following options:
     * Select **Email address** , and then enter a new email address that you want to send the order notification to.
     * Select a staff to send notifications to their email.
  5. Optional: If you have the POS sales channel installed and you want to create notifications for orders from a particular POS location or from the web, then select a location from the list. You can select **All** to create notifications for all orders. To add notifications for more than one specific location, you need to create them as separate order notifications.
  6. Click **Add recipient**.

Mobile
  1. From the [Shopify app](https://www.shopify.com/install/detect), tap ![Menu](https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/MenuIcon.svg), and then tap ![Settings](https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/SettingsIcon.svg) **Settings**.
  2. In the **Store settings** section, tap **Notifications**.
  3. Tap **Staff notifications**.
  4. In the **Recipients** section, tap **Add recipient**.
  5. From the first drop-down menu, select the notification recipient from the following options:
     * Select **Email address** , and then enter a new email address that you want to send the order notification to.
     * Select a staff to send notifications to their email.
  6. Optional: If you have the POS sales channel installed and you want to create notifications for orders from a particular POS location or from the web, then select a location from the list. You can select **All** to create notifications for all orders. To add notifications for more than one specific location, you need to create them as separate order notifications.
  7. Tap **Add recipient**.


After you've set up a staff notification for an email address, you can test it by clicking **Send test notification**. Test notification include fake order and customer information.
#### Tip
You can [get push notifications on your mobile device](https://help.shopify.com/en/manual/fulfillment/managing-orders/managing-order-details#activate-push-notifications) when you are using the [mobile app](https://www.shopify.com/mobile).
## Deactivate or reactivate staff notifications
You can temporarily deactivate staff notifications instead of deleting the recipient. Afterward, you can reactivate the notifications.
#### Steps:
  1. From your Shopify admin, go to **Settings** > [**Notifications**](https://admin.shopify.com/settings/notifications).
  2. Click **Staff notifications**.
  3. Click **& #8230**, and then do one of the following to adjust each recipient's notification settings:
     * To deactivate the notification, select **Turn off**.
     * To reactivate the notification, select **Turn on**.


## Edit staff notifications sent to a recipient
You can edit a recipient to only receive a staff notification for some staff notifications.
#### Steps:
  1. From your Shopify admin, go to **Settings** > [**Notifications**](https://admin.shopify.com/settings/notifications).
  2. Click **Staff notifications**.
  3. Click **& #8230**, and then click **Edit recipient**.
  4. Select or deselect the staff notifications that you want the recipient to receive.
  5. Click **Save**.


## Delete a staff order notification recipient
Desktop
  1. From your Shopify admin, go to **Settings** > [**Notifications**](https://admin.shopify.com/settings/notifications).
  2. Click **Staff notifications**.
  3. Find the recipient, and then click **& #8230** > **Remove**.

Mobile
  1. From the [Shopify app](https://www.shopify.com/install/detect), tap ![Menu](https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/MenuIcon.svg), and then tap ![Settings](https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/SettingsIcon.svg) **Settings**.
  2. In the **Store settings** section, tap **Notifications**.
  3. Tap **Staff notifications**.
  4. Find the recipient, and then tap ![Horizontal menu](https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/MenuHorizontalIcon.svg) or ![Vertical menu](https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/MenuVerticalIcon.svg) > **Remove**.


## Order dispute updates
The **Order dispute updates** notification controls who receives email about [chargebacks and inquiries](https://help.shopify.com/en/manual/payments/chargebacks/chargeback-process). A staff member receives these emails only when both of the following are true:
  * They have the [**Disputes** > **Manage** permission](https://help.shopify.com/en/manual/your-account/users/roles/permissions/store-permissions#orders-permissions).
  * **Order dispute updates** is turned on for them in **Settings** > **Notifications** > **Staff notifications**.


These recipients can also be emailed when a customer sends a new message on a PayPal inquiry, including after the inquiry closes.
You can turn the notification off for your whole store, or for individual recipients. To change it for one recipient, [edit the staff notifications sent to that recipient](https://help.shopify.com/en/manual/fulfillment/setup/notifications/staff-notifications#edit-staff-notifications-sent-to-a-recipient).
Review the following considerations for **Order dispute updates** :
  * Recipients that you add are set to receive dispute updates by default.
  * On stores that existed before this notification became available, only the store owner receives dispute updates until you turn the notification on for other recipients.
  * Dispute updates go to staff members only. Recipients that you added as a plain email address, rather than as a staff member, don't receive them.
  * You can't customize the **Order dispute updates** email template.


## Customize the timing and frequency of your Store order summary
By default, the **Store order summary** notification is set as weekly every Monday at 9AM in your local time. You can update the **Store order summary** to send on a different day or time, and you can set it to daily.
#### Steps:
  1. From your Shopify admin, go to **Settings** > [**Notifications**](https://admin.shopify.com/settings/notifications).
  2. Click **Staff notifications**.
  3. Click **Store order summary**.
  4. In the **Frequency** drop-down menu, select either **Weekly** or **Daily**.
  5. If you selected **Weekly** , then in the **Day of the week** drop-down menu, select the day.
  6. In the **Time** drop-down, select the time.
  7. Click **Save**.


## Customize new order template
You can customize your new order template by editing the code in the email template.
### Include a link to the order page
Desktop
  1. From your Shopify admin, go to **Settings** > [**Notifications**](https://admin.shopify.com/settings/notifications).
  2. Click **Staff notifications**.
  3. Click **New order**.
  4. Click **Edit code** to open the template in the online code editor.
  5. At the bottom of the template, above `{% endif %}`, add:



```
You can review details of this order in your shop admin at {{ shop.url }}/admin/orders/{{ id }}.
```

  1. Click **Save**.

Mobile
  1. From the [Shopify app](https://www.shopify.com/install/detect), tap ![Menu](https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/MenuIcon.svg), and then tap ![Settings](https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/SettingsIcon.svg) **Settings**.
  2. In the **Store settings** section, tap **Notifications**.
  3. Tap **Staff notifications**.
  4. Tap **New order**.
  5. Tap **Edit code** to open the template in the online code editor.
  6. At the bottom of the template, above `{% endif %}`, add:



```
You can review details of this order in your shop admin at {{ shop.url }}/admin/orders/{{ id }}.
```

  1. Tap **Save** or **✓**.


### Find the order number or ID
You can find the order ID :

```
Order {{ order_name }}
```

This will return something like:

```
Order #1001
```

### Include special instructions
#### Steps:
Desktop
  1. From your Shopify admin, go to **Settings** > [**Notifications**](https://admin.shopify.com/settings/notifications).
  2. Click **Staff notifications** , and then click **New order**.
  3. Click **Edit code** to open the template in the online code editor.
  4. At the bottom of the **New order** email template, add the following code:



```
{% unless note == blank %}
  Special instructions: {{ note }}
  {% endunless %}
```

  1. Click **Save**.

Mobile
  1. From the [Shopify app](https://www.shopify.com/install/detect), tap ![Menu](https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/MenuIcon.svg), and then tap ![Settings](https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/SettingsIcon.svg) **Settings**.
  2. In the **Store settings** section, tap **Notifications**.
  3. Tap **Staff notifications** , and then tap **New order**.
  4. Tap **Edit code** to open the template in the online code editor.
  5. At the bottom of the **New order** email template, add the following code:



```
{% unless note == blank %}
  Special instructions: {{ note }}
  {% endunless %}
```

  1. Tap **Save** or **✓**.


Leave feedback

