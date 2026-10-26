Skip to main content
Menu
[![Open API v3 Logo](https://developers.etsy.com/img/logo.svg)**Open API v3**](https://developers.etsy.com/documentation)[Guides](https://developers.etsy.com/documentation/)[API Reference](https://developers.etsy.com/documentation/reference)
[Send feedback](https://github.com/etsy/open-api/discussions)
[![Open API v3 Logo](https://developers.etsy.com/img/logo.svg)**Open API v3**](https://developers.etsy.com/documentation)
  * [Guides](https://developers.etsy.com/documentation/)
  * [API Reference](https://developers.etsy.com/documentation/reference)
  * [Send feedback](https://github.com/etsy/open-api/discussions)


Menu
  * [Introduction](https://developers.etsy.com/documentation/)
  * [API Essentials](https://developers.etsy.com/documentation/essentials/webhooks/#!)
    * [Authentication](https://developers.etsy.com/documentation/essentials/authentication)
    * [URL Syntax](https://developers.etsy.com/documentation/essentials/urlsyntax)
    * [Definitions](https://developers.etsy.com/documentation/essentials/definitions)
    * [Request Standards](https://developers.etsy.com/documentation/essentials/requests)
    * [Rate Limits](https://developers.etsy.com/documentation/essentials/rate-limits)
    * [Webhooks](https://developers.etsy.com/documentation/essentials/webhooks)
    * [Get help](https://developers.etsy.com/documentation/get-help)
    * [API testing policy](https://www.etsy.com/legal/policy/api-testing-policy/169130941112)
  * [Tutorials](https://developers.etsy.com/documentation/essentials/webhooks/#!)
    * [Overview](https://developers.etsy.com/documentation/tutorials/overview)
    * [Quick Start Tutorial](https://developers.etsy.com/documentation/tutorials/quickstart)
    * [Fulfillment Tutorial](https://developers.etsy.com/documentation/tutorials/fulfillment)
    * [Listings Tutorial](https://developers.etsy.com/documentation/tutorials/listings)
    * [Inventory and Shipping Data Migration Tutorial](https://developers.etsy.com/documentation/tutorials/inventory-shipping-migration)
    * [Processing Profiles Migration](https://developers.etsy.com/documentation/tutorials/migration)
    * [Rotating Your Shared Secret](https://developers.etsy.com/documentation/tutorials/shared-secret-rotation)
    * [Shop Management Tutorial](https://developers.etsy.com/documentation/tutorials/shopmanagement)
    * [Third Variation Tutorial](https://developers.etsy.com/documentation/tutorials/third-variation)
    * [Payments Tutorial](https://developers.etsy.com/documentation/tutorials/payments)
    * [Personalization Migration](https://developers.etsy.com/documentation/essentials/webhooks/#!)
      * [Personalization Migration Guide](https://developers.etsy.com/documentation/tutorials/personalization-migration)
      * [Personalization Examples](https://developers.etsy.com/documentation/tutorials/personalization/examples)
      * [Personalization Add-On Pricing](https://developers.etsy.com/documentation/tutorials/personalization-addon-pricing)
  * [MCP Server](https://developers.etsy.com/documentation/essentials/webhooks/#!)
    * [Dev MCP Server](https://developers.etsy.com/documentation/mcp_server/devmcpserver)
  * [Manage your apps](https://www.etsy.com/developers)
  * [Terms of use](https://www.etsy.com/legal/api)


# Webhooks
Webhooks provide real-time notifications to approved Etsy applications when defined events occur. Rather than polling the API for changes, your app can subscribe to webhook events and receive updates as soon as they happen.
You can see our available events [here](https://developers.etsy.com/documentation/essentials/webhooks/#available-events). Watch our GitHub Announcements for updates: <https://github.com/etsy/open-api/discussions/categories/announcements>
Webhook functionality is available for both **commercial** and **personal** applications!
##  Webhook Concepts[#](https://developers.etsy.com/documentation/essentials/webhooks/#webhook-concepts "Direct link to heading")
  * **Endpoints** – A destination URL where Etsy delivers webhook messages for the events you subscribe to.
  * **Events** – Specific actions or changes that trigger a webhook.
  * **Messages/Deliveries** – Each time an event occurs, Etsy sends a message (payload) to the configured endpoint.
  * **Signing Secrets** – Used to validate the authenticity of incoming webhook requests.
  * **Retries** – Etsy automatically retries delivery when your endpoint fails to acknowledge receipt.


##  Managing Webhooks[#](https://developers.etsy.com/documentation/essentials/webhooks/#managing-webhooks "Direct link to heading")
###  Prerequisites[#](https://developers.etsy.com/documentation/essentials/webhooks/#prerequisites "Direct link to heading")
  * You must have a valid OAuth 2.0 access token with the appropriate scopes (depending on your app’s function).
    * For webhook delivery, provide a publicly accessible callback URL configured to receive POST requests from Etsy.


##  Available Events[#](https://developers.etsy.com/documentation/essentials/webhooks/#available-events "Direct link to heading")
Webhooks events are organized into three domains: **Order** , **Listing** , and **Inventory**. Each domain covers a distinct area of shop activity and delivers a different payload structure.
###  Order[#](https://developers.etsy.com/documentation/essentials/webhooks/#order "Direct link to heading")
  * `order.paid` – delivered when an order receives payment.
  * `order.canceled` - delivered when a seller initiates a cancelation.
  * `order.shipped` - delivered when shipping information is created for a product of a shop's receipt.
  * `order.delivered` - delivered when an order is marked as delivered.


###  Listing[#](https://developers.etsy.com/documentation/essentials/webhooks/#listing "Direct link to heading")
  * `listing.created` – delivered when a listing is created.
  * `listing.updated` – delivered when a listing is updated. Changes to the following fields will trigger this event: `Title`, `Description`, `Personalization`, `Taxonomy`, `Images`, `Attributes`, and `State`.
  * `listing.deleted` – delivered when a listing is deleted.


###  Inventory[#](https://developers.etsy.com/documentation/essentials/webhooks/#inventory "Direct link to heading")
  * `inventory.created` – delivered when a product is created.
  * `inventory.updated` – delivered when a product is updated. Changes to the following fields will trigger this event: `Price`, `Readiness State`,`SKU`, and `State`.
  * `inventory.deleted` – delivered when a product is deleted.
  * `inventory.out_of_stock` – delivered when a product's quantity reaches 0.


##### Listings VS. Products
A listing is a container for one or more products. For example, a t-shirt.
A product is the specific purchasable variant of a listing, defined by a unique combination of variations. For example, a t-shirt that is size small and primary color blue.
Stay tuned to our [announcements](https://github.com/etsy/open-api/discussions/categories/announcements) for more events coming soon!
##  Payload Structure[#](https://developers.etsy.com/documentation/essentials/webhooks/#payload-structure "Direct link to heading")
Each webhook event is delivered as a JSON payload. Payloads differ by domain, but all webhook deliveries share the following common fields:
  * `event_type` – The name of the event that triggered the webhook (e.g., `order.paid`).
  * `resource_url` - A prepared URL to call back and get the updated data related to the event that was triggered.
  * `shop_id` - The id of the shop related to the event that was triggered.

  
| Field  | Order events  | Listing events  | Inventory events  |  
| --- | --- | --- | --- |  
| `event_type`  | ✓  | ✓  | ✓  |  
| `resource_url`  | ✓  | ✓  | ✓  |  
| `shop_id`  | ✓  | ✓  | ✓  |  
| `listing_id`  |   | ✓  | ✓  |  
| `product_id`  |   |   | ✓  |  
###  Order Payload[#](https://developers.etsy.com/documentation/essentials/webhooks/#order-payload "Direct link to heading")
Order events include only the common fields listed above. The `resource_url` points to the [getShopReceipt](https://developers.etsy.com/documentation/reference#operation/getShopReceipt) endpoint, which returns the receipt object for the order.
Here’s an example of how an `order.paid` payload would look like:
{
"event_type":"order.paid",
"resource_url":"https://api.etsy.com/v3/application/shops/{YOUR_SHOP_ID}/receipts/{RECEIPT_ID}",
"shop_id":"{YOUR_SHOP_ID}"
}
Copy
###  Listing Payload[#](https://developers.etsy.com/documentation/essentials/webhooks/#listing-payload "Direct link to heading")
Listing events include the common fields listed above, plus the `listing_id` field. The `resource_url` points to the [getListing](https://developers.etsy.com/documentation/reference#operation/getListing) endpoint, which returns the listing object for the listing. The URL also appends `?includes=Images,Personalization` to fetch the Image and Personalization data associated with the listing, since Images and Personalization are both tracked in the `listing.updated` event.
Here’s an example of how a `listing.updated` payload would look like:
{
"event_type":"listing.updated",
"resource_url":"https://api.etsy.com/v3/application/shops/{YOUR_SHOP_ID}/listings/{LISTING_ID}?includes=Images,Personalization",
"shop_id":"{YOUR_SHOP_ID}",
"listing_id":"{LISTING_ID}"
}
Copy
###  Inventory Payload[#](https://developers.etsy.com/documentation/essentials/webhooks/#inventory-payload "Direct link to heading")
Inventory events include the common fields listed above, plus the `listing_id` and `product_id` fields. The `resource_url` points to the [getListingProduct](https://developers.etsy.com/documentation/reference#operation/getListingProduct) endpoint, which returns the product object for the product.
Here’s an example of how an `inventory.updated` payload would look like:
{
"event_type":"inventory.updated",
"resource_url":"https://api.etsy.com/v3/application/shops/{YOUR_SHOP_ID}/listings/{LISTING_ID}/products/{PRODUCT_ID}",
"shop_id":"{YOUR_SHOP_ID}",
"listing_id":"{LISTING_ID}",
"product_id":"{PRODUCT_ID}"
}
Copy
##  Verifying Webhook Signatures[#](https://developers.etsy.com/documentation/essentials/webhooks/#verifying-webhook-signatures "Direct link to heading")
###  Why signature verification matters[#](https://developers.etsy.com/documentation/essentials/webhooks/#why-signature-verification-matters "Direct link to heading")
Without verifying signatures, malicious actors could send forged webhook requests to your endpoint and trigger unintended behaviour. Proper verification ensures that:
  * The request originated from Etsy
  * The payload has not been tampered with
  * You avoid processing duplicate or replayed messages


###  What do you need[#](https://developers.etsy.com/documentation/essentials/webhooks/#what-do-you-need "Direct link to heading")
  * A signing secret, which you can retrieve from your Webhook Portal ![img](https://developers.etsy.com/assets/images/signing_secret-4c35a363be251ea116371faec17fab7e.png)
  * You can find this in the details of your webhook event.
  * Three special headers + raw body from each request, to be used to validate the payload


###  What you will see on incoming requests[#](https://developers.etsy.com/documentation/essentials/webhooks/#what-you-will-see-on-incoming-requests "Direct link to heading")
Each webhook request will be an HTTP POST to your endpoint that includes:
  * Raw request body (JSON)
  * Headers:
    * `webhook-id` – unique ID of the webhook call (even on retries)
    * `webhook-timestamp` – unix timestamp (seconds) when the event was emitted
    * `webhook-signature` – this is what will be used to compare with your signing secret


###  How to compute and verify the signature[#](https://developers.etsy.com/documentation/essentials/webhooks/#how-to-compute-and-verify-the-signature "Direct link to heading")
  1. Build the "signed content” string such as:


signed_content = webhook-id + "." + webhook-timestamp + "." + raw_body
Copy
In this example, `raw_body` is the exact bytes/string of the HTTP body **before** any JSON parsing.
  1. Derive the secret key.


  * Take your secret from the dashboard  
![img](https://developers.etsy.com/assets/images/signing_secret-4c35a363be251ea116371faec17fab7e.png)
  * Remove the `whsec_` prefix. 
  * Base64-decode the remaining part of the bytes.


  1. Compute the expected signature:


  * HMAC-SHA256 over `signed_content` (step 1) using the decoded secret key (step 2). 
  * Base64-encode the result


Here’s a pseudo code example of what this would look like:
secret_bytes = base64_decode(secret.split("_")[1])
expected_sig = base64_encode(HMAC_SHA256(secret_bytes, signed_content))
Copy
  1. Compare against the `webhook-signature` header.


  * Check if any of the entries (if more than one) equals your `expected_sig` (step 3).
  * If there’s **no match** , **reject** the webhook.
  * If it’s a match, you may proceed with JSON parsing of the raw body or what your integration requires to interpret this data.


###  Preventing Replay Attacks[#](https://developers.etsy.com/documentation/essentials/webhooks/#preventing-replay-attacks "Direct link to heading")
Even if the signature matches, an attacker could replay an old, captured request. To mitigate that:
  1. Read webhook-timestamp 
  2. Compare it to your current server time 
  3. Reject if it’s older/newer than your allowed margin.


In your code, it should roughly look like this:
now = current_unix_time()
if abs(now - webhook-timestamp) > 300:
reject("Stale timestamp")
Copy
##  Managing Webhook Events[#](https://developers.etsy.com/documentation/essentials/webhooks/#managing-webhook-events "Direct link to heading")
From the Webhooks section of your application dashboard, you can:
  * View a list of your active webhook subscriptions.
  * Inspect details of each subscription, including event type, callback URL, secret (masked), creation date, and delivery history.
  * Delete or disable subscriptions you no longer need, which will immediately stop event deliveries.


When you subscribe to an event, Etsy will send a POST request to your callback URL when the event is triggered.
###  Access the Webhooks Portal[#](https://developers.etsy.com/documentation/essentials/webhooks/#access-the-webhooks-portal "Direct link to heading")
  1. Navigate to **Manage your apps** in the Developer Portal.


![img](https://developers.etsy.com/assets/images/manage_your_app_step_1-44afde2a232735de449f79ce710bfe6a.png)
  1. Click the dropdown menu for your **commercial** app and select **Go to Webhook portal**.


![img](https://developers.etsy.com/assets/images/dropdown_menu-d1124d8094ced477635869a00790cf3d.png)
![img](https://developers.etsy.com/assets/images/dropdown_menu_show-e0962fb2e37550facf49c7a7dec3d970.png)
You will see your portal.
![img](https://developers.etsy.com/assets/images/portal_view-9296ab48b0ea1401f24a84f4ee9dbedf.png)
###  Configure a Subscription[#](https://developers.etsy.com/documentation/essentials/webhooks/#configure-a-subscription "Direct link to heading")
Assuming you followed the steps from [Access the Webhooks Portal](https://developers.etsy.com/documentation/essentials/webhooks/#access-the-webhooks-portal), to configure a subscription:
  1. Choose **+Add Endpoint**.


![img](https://developers.etsy.com/assets/images/add_endpoint-e71abe6d7c4af498053b59625e7e649e.png)
  1. Enter your **callback URL** and the event you wish to subscribe to.


![img](https://developers.etsy.com/assets/images/create_form-e8dd20c373813bae831976a7efee9830.png)
  1. Click **Create**.


Once saved, your callback URL will receive webhook payloads when the event occurs.
##### Important
Because webhooks deliver asynchronous notifications, ensure your server can handle incoming POST requests and validate signatures.
###  How to Unsubscribe (Delete or Disable a Webhook)[#](https://developers.etsy.com/documentation/essentials/webhooks/#how-to-unsubscribe-delete-or-disable-a-webhook "Direct link to heading")
##### warning
Disabled endpoints remain visible in your dashboard and can be re-enabled at any time. _Deleted endpoints cannot be recovered._
####  Delete a Webhook[#](https://developers.etsy.com/documentation/essentials/webhooks/#delete-a-webhook "Direct link to heading")
Assuming you followed the steps from [Access the Webhooks Portal](https://developers.etsy.com/documentation/essentials/webhooks/#access-the-webhooks-portal),to fully delete a webhook subscription:
  1. Select the subscription you wish to remove.
  2. Click the 3 dots on the upper right corner and select **Delete**. ![img](https://developers.etsy.com/assets/images/select_dropdown-67006efeabdeab843a71e01886dec35c.png) ![img](https://developers.etsy.com/assets/images/delete_select-52642e3c42bd4547ec72cb06fb2555b2.png)
  3. Confirm deletion. ![img](https://developers.etsy.com/assets/images/confirm_delete-05d139ee919b98a04b7db1590295b33e.png)


After deletion, no further events will be delivered for that subscription.
##### caution
Deleting an endpoint will permanently delete all of its data. 
####  Disable a Webhook[#](https://developers.etsy.com/documentation/essentials/webhooks/#disable-a-webhook "Direct link to heading")
Assuming you followed the steps from [Access the Webhooks Portal](https://developers.etsy.com/documentation/essentials/webhooks/#access-the-webhooks-portal), to disable a webhook subscription:
  1. Select the subscription you wish to disable.
  2. Click the 3 dots on the upper right corner and select **Disable Endpoint**. ![img](https://developers.etsy.com/assets/images/select_dropdown-67006efeabdeab843a71e01886dec35c.png) ![img](https://developers.etsy.com/assets/images/disable_select-f87acd8b9265456a431ef4fcff23e3cf.png)


To enable the event again, do the same process but click **Enable Endpoint**. ![img](https://developers.etsy.com/assets/images/enable_endpoint-4b5cf0487c6d2166a4e261098f2fe8b6.png)
##  Monitoring Webhook Activity[#](https://developers.etsy.com/documentation/essentials/webhooks/#monitoring-webhook-activity "Direct link to heading")
Each subscription includes tools and data to help monitor webhook performance and flow. These insights allow developers to troubleshoot issues and understand how the webhook behaves over time.
###  General Information[#](https://developers.etsy.com/documentation/essentials/webhooks/#general-information "Direct link to heading")
The detail view displays metadata about the subscription, including the date and time it was created. This helps track when the webhook was first configured.
![img](https://developers.etsy.com/assets/images/webhook_detail-ac7ff9178ed5a17c3100f4a75fa9cd28.png)
###  Delivery Stats[#](https://developers.etsy.com/documentation/essentials/webhooks/#delivery-stats "Direct link to heading")
The monitoring section provides an overview of delivery performance. This may include the number of events delivered, recent activity, and overall delivery patterns.
![img](https://developers.etsy.com/assets/images/stats-9c9a98a641913d7aa4219e1ad04edf38.png)
###  Message Attempts[#](https://developers.etsy.com/documentation/essentials/webhooks/#message-attempts "Direct link to heading")
For each attempted delivery, you can view whether a message was successfully delivered or if retries occurred. This supports debugging of callback endpoints and helps identify transient or persistent delivery issues.
![img](https://developers.etsy.com/assets/images/message_attempts-6f6f0eb7ca2e74cfd720c4dde7418e58.png)
###  Payload Details[#](https://developers.etsy.com/documentation/essentials/webhooks/#payload-details "Direct link to heading")
Recent event payloads appear in the activity log. Developers can inspect these payloads to validate data fields, ensure that their system is parsing them correctly, or verify that events are arriving in the expected format.
By clicking one of the message attempts, you can see the message’s details.
![img](https://developers.etsy.com/assets/images/payload_details-2695c3e53277a800cf13fe1e7ae0ad01.png)
###  Endpoint Status[#](https://developers.etsy.com/documentation/essentials/webhooks/#endpoint-status "Direct link to heading")
The detail view displays whether the endpoint is active or disabled. Disabled endpoints do not receive events until re-enabled.
![img](https://developers.etsy.com/assets/images/endpoint_status-40a36c54511edae3ec69b0fc113a9e0e.png)
##  Delivery Retries[#](https://developers.etsy.com/documentation/essentials/webhooks/#delivery-retries "Direct link to heading")
We attempt to deliver each webhook message based on a retry schedule with exponential backoff.
###  The Schedule[#](https://developers.etsy.com/documentation/essentials/webhooks/#the-schedule "Direct link to heading")
Each message is attempted based on the following schedule, where each period is started following the failure of the preceding attempt:
  * Immediately
  * 5 seconds
  * 5 minutes
  * 30 minutes
  * 2 hours
  * 5 hours
  * 10 hours
  * 10 hours (in addition to the previous)


If an endpoint is removed or disabled, delivery attempts to the endpoint will be disabled as well.
For example, an attempt that fails three times before eventually succeeding will be delivered roughly 35 minutes and 5 seconds following the first attempt.
###  Manual retries[#](https://developers.etsy.com/documentation/essentials/webhooks/#manual-retries "Direct link to heading")
You can also use the application portal to manually retry each message at any time, or automatically retry ("Recover") all failed messages starting from a given date.
![img](https://developers.etsy.com/assets/images/recover_replay-f4a77e2c3f9637ce3f86ebc463fb04a1.png)
##  Testing Webhooks[#](https://developers.etsy.com/documentation/essentials/webhooks/#testing-webhooks "Direct link to heading")
The Webhook Portal includes tools for sending test events to your endpoint. Use this to validate:
  * Endpoint availability
  * Signature verification
  * Event-processing logic
  * Error-handling behavior


You can access the testing tab of your webhook event by clicking the event to access its details.
![img](https://developers.etsy.com/assets/images/access_details-28b0aab552bf9091be7aa9748e85ea2a.png)
And then selecting the **Testing** tab.
![img](https://developers.etsy.com/assets/images/testing_tab-b88920ca304fcca418449a66fdd95e5d.png)
[Previous « Rate Limits](https://developers.etsy.com/documentation/essentials/rate-limits)
[Next Get help »](https://developers.etsy.com/documentation/get-help)
  * [Webhook Concepts](https://developers.etsy.com/documentation/essentials/webhooks/#webhook-concepts)
  * [Managing Webhooks](https://developers.etsy.com/documentation/essentials/webhooks/#managing-webhooks)
    * [Prerequisites](https://developers.etsy.com/documentation/essentials/webhooks/#prerequisites)
  * [Available Events](https://developers.etsy.com/documentation/essentials/webhooks/#available-events)
    * [Order](https://developers.etsy.com/documentation/essentials/webhooks/#order)
    * [Listing](https://developers.etsy.com/documentation/essentials/webhooks/#listing)
    * [Inventory](https://developers.etsy.com/documentation/essentials/webhooks/#inventory)
  * [Payload Structure](https://developers.etsy.com/documentation/essentials/webhooks/#payload-structure)
    * [Order Payload](https://developers.etsy.com/documentation/essentials/webhooks/#order-payload)
    * [Listing Payload](https://developers.etsy.com/documentation/essentials/webhooks/#listing-payload)
    * [Inventory Payload](https://developers.etsy.com/documentation/essentials/webhooks/#inventory-payload)
  * [Verifying Webhook Signatures](https://developers.etsy.com/documentation/essentials/webhooks/#verifying-webhook-signatures)
    * [Why signature verification matters](https://developers.etsy.com/documentation/essentials/webhooks/#why-signature-verification-matters)
    * [What do you need](https://developers.etsy.com/documentation/essentials/webhooks/#what-do-you-need)
    * [What you will see on incoming requests](https://developers.etsy.com/documentation/essentials/webhooks/#what-you-will-see-on-incoming-requests)
    * [How to compute and verify the signature](https://developers.etsy.com/documentation/essentials/webhooks/#how-to-compute-and-verify-the-signature)
    * [Preventing Replay Attacks](https://developers.etsy.com/documentation/essentials/webhooks/#preventing-replay-attacks)
  * [Managing Webhook Events](https://developers.etsy.com/documentation/essentials/webhooks/#managing-webhook-events)
    * [Access the Webhooks Portal](https://developers.etsy.com/documentation/essentials/webhooks/#access-the-webhooks-portal)
    * [Configure a Subscription](https://developers.etsy.com/documentation/essentials/webhooks/#configure-a-subscription)
    * [How to Unsubscribe (Delete or Disable a Webhook)](https://developers.etsy.com/documentation/essentials/webhooks/#how-to-unsubscribe-delete-or-disable-a-webhook)
  * [Monitoring Webhook Activity](https://developers.etsy.com/documentation/essentials/webhooks/#monitoring-webhook-activity)
    * [General Information](https://developers.etsy.com/documentation/essentials/webhooks/#general-information)
    * [Delivery Stats](https://developers.etsy.com/documentation/essentials/webhooks/#delivery-stats)
    * [Message Attempts](https://developers.etsy.com/documentation/essentials/webhooks/#message-attempts)
    * [Payload Details](https://developers.etsy.com/documentation/essentials/webhooks/#payload-details)
    * [Endpoint Status](https://developers.etsy.com/documentation/essentials/webhooks/#endpoint-status)
  * [Delivery Retries](https://developers.etsy.com/documentation/essentials/webhooks/#delivery-retries)
    * [The Schedule](https://developers.etsy.com/documentation/essentials/webhooks/#the-schedule)
    * [Manual retries](https://developers.etsy.com/documentation/essentials/webhooks/#manual-retries)
  * [Testing Webhooks](https://developers.etsy.com/documentation/essentials/webhooks/#testing-webhooks)


#### Documentation
  * [Guides](https://developers.etsy.com/documentation)
  * [API Reference](https://developers.etsy.com/documentation/reference)


#### Community
  * [Stack Overflow](https://stackoverflow.com/c/etsy/questions/tagged/docsbuilder)
  * [Google Group](https://groups.google.com/g/etsy-api-v2)


#### More
  * [Get help](https://developers.etsy.com/documentation/get-help)
  * [Terms of use](https://www.etsy.com/legal/api)


© 2021 Etsy, Inc.
Copy as Markdown

