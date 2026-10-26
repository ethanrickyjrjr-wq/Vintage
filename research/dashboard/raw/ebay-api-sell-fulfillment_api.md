---
title: Fulfillment
description: "The outcome of a buyer's eBay checkout process is an _order_. The **Fulfillment API** enables sellers to manage the completion of an order in accordance with the payment method and timing specified at checkout. The line items in the order are grouped into one or more packages. As the seller addresses, handles, and ships each package, the set of specifications for this process is known as a _fulfillment_. Use the Fulfillment API to facilitate and monitor these activities from the order to completion. Sellers' status on eBay depend partly on their record of timely fulfillment. **Note:** The **Fulfillment API** includes only transactions that have completed checkout. Specifically, the [getOrders](/develop/api/sell/fulfillment_api#sell-fulfillment_api-order-getorders) method does not include pending-payment purchases that require upfront payment before shipment."
api_version: 1.0
api_name: fulfillment_api
api_type: REST
api_group: sell/fulfillment_api
source_url:
  html: https://developer.ebay.com/develop/api/sell/fulfillment_api
  md: https://developer.ebay.com/develop/api/sell/fulfillment_api.md
---

# Fulfillment API

The outcome of a buyer's eBay checkout process is an _order_. The **Fulfillment API** enables sellers to manage the completion of an order in accordance with the payment method and timing specified at checkout. The line items in the order are grouped into one or more packages. As the seller addresses, handles, and ships each package, the set of specifications for this process is known as a _fulfillment_. Use the Fulfillment API to facilitate and monitor these activities from the order to completion. Sellers' status on eBay depend partly on their record of timely fulfillment.

**Note:** The **Fulfillment API** includes only transactions that have completed checkout. Specifically, the [getOrders](/develop/api/sell/fulfillment_api#sell-fulfillment_api-order-getorders) method does not include pending-payment purchases that require upfront payment before shipment.

## API Methods

The following API methods are available:

### getOrder

#### GET /order/{orderId}
**Description:** Use this call to retrieve the contents of an order based on its unique identifier, _orderId_. This value is returned in the [getOrders](/develop/api/sell/fulfillment_api#sell-fulfillment_api-order-getorders) call's **orders.orderId** field when you search for orders by creation date, modification date, or fulfillment status. Include the optional **fieldGroups** query parameter set to `TAX_BREAKDOWN` to return a breakdown of the taxes and fees.  
  
The returned **Order** object contains information you can use to create and process fulfillments, including the following:

*   Information about the buyer and seller
*   Information about the order's line items
*   The plans for packaging, addressing, and shipping the order
*   The status of payment, packaging, addressing, and shipping the order
*   A summary of monetary amounts specific to the order such as pricing, payments, and shipping costs
*   A summary of applied taxes and fees and, optionally, a breakdown of each
**Parameters:**
- **fieldGroups** (string)
  - This parameter lets you control what is returned in the response.  
  
**Note:** The only presently supported value is `TAX_BREAKDOWN`. This field group adds addition fields to the response that return a breakdown of taxes and fees.
- **orderId** (string) *required*
  - This path parameter is used to specify the unique identifier of the order being retrieved.  
  
Use the [getOrders](/develop/api/sell/fulfillment_api#sell-fulfillment_api-order-getorders) method to retrieve order IDs. Order ID values are also shown in My eBay/Seller Hub.  
  
**Note:** [getOrders](/develop/api/sell/fulfillment_api#sell-fulfillment_api-order-getorders) can return orders up to two years old. Do not provide the **orderId** for an order created more than two years in the past.

### getOrders

#### GET /order
**Description:** Use this method to search for and retrieve one or more orders based on their creation date, last modification date, or fulfillment status using the **filter** parameter. You can alternatively specify a list of orders using the **orderIds** parameter. Include the optional **fieldGroups** query parameter set to `TAX_BREAKDOWN` to return a breakdown of the taxes and fees. By default, when no filters are used this call returns all orders created within the last 90 days.  
  
The returned **Order** objects contain information you can use to create and process fulfillments, including:

*   Information about the buyer and seller
*   Information about the order's line items
*   The plans for packaging, addressing and shipping the order
*   The status of payment, packaging, addressing, and shipping the order
*   A summary of monetary amounts specific to the order such as pricing, payments, and shipping costs
*   A summary of applied taxes and fees, and optionally a breakdown of each

  
**Important:** In this call, the **cancelStatus.cancelRequests** array is returned but is always empty. Use the [getOrder](/develop/api/sell/fulfillment_api#sell-fulfillment_api-order-getorder) call instead, which returns this array fully populated with information about any cancellation requests.
**Parameters:**
- **fieldGroups** (string)
  - This parameter lets you control what is returned in the response.  
  
**Note:** The only presently supported value is `TAX_BREAKDOWN`. This field group adds addition fields to the response that return a breakdown of taxes and fees.
- **filter** (string)
  - One or more comma-separated criteria for narrowing down the collection of orders returned by this call. These criteria correspond to specific fields in the response payload. Multiple filter criteria combine to further restrict the results.  
  
**Note:** [getOrders](/develop/api/sell/fulfillment_api#sell-fulfillment_api-order-getorders) can return orders up to two years old. Do not set the `creationdate` filter to a date beyond two years in the past.  
**Note:** If the **orderIds** parameter is included in the request, the **filter** parameter will be ignored.  
The available criteria are as follows:

`**creationdate**`

The time period during which qualifying orders were created (the **orders.creationDate** field). In the URI, this is expressed as a starting timestamp, with or without an ending timestamp (in brackets). The timestamps are in [ISO 8601](<https://www.iso.org/iso-8601-date-and-time-format.html > "https://www.iso.org ") format, which uses the 24-hour Universal Coordinated Time (UTC) clock.For example:

*   `creationdate:[2016-02-21T08:25:43.511Z..]` identifies orders created on or after the given timestamp.
*   `creationdate:[2016-02-21T08:25:43.511Z..2016-04-21T08:25:43.511Z]` identifies orders created between the given timestamps, inclusive.

`**lastmodifieddate**`

The time period during which qualifying orders were last modified (the **orders.modifiedDate** field). In the URI, this is expressed as a starting timestamp, with or without an ending timestamp (in brackets). The timestamps are in [ISO 8601](<https://www.iso.org/iso-8601-date-and-time-format.html > "https://www.iso.org ") format, which uses the 24-hour Universal Coordinated Time (UTC) clock.For example:

*   `lastmodifieddate:[2016-05-15T08:25:43.511Z..]` identifies orders modified on or after the given timestamp.
*   `lastmodifieddate:[2016-05-15T08:25:43.511Z..2016-05-31T08:25:43.511Z]` identifies orders modified between the given timestamps, inclusive.

**Note:** If **creationdate** and **lastmodifieddate** are both included, only **creationdate** is used.  

`**orderfulfillmentstatus**`

The degree to which qualifying orders have been shipped (the **orders.orderFulfillmentStatus** field). In the URI, this is expressed as one of the following value combinations:

*   `orderfulfillmentstatus:{NOT_STARTED|IN_PROGRESS}` specifies orders for which no shipping fulfillments have been started, plus orders for which at least one shipping fulfillment has been started but not completed.
*   `orderfulfillmentstatus:{FULFILLED|IN_PROGRESS}` specifies orders for which all shipping fulfillments have been completed, plus orders for which at least one shipping fulfillment has been started but not completed.

**Note:** The values `NOT_STARTED`, `IN_PROGRESS`, and `FULFILLED` can be used in various combinations, but only the combinations shown here are currently supported.

Here is an example of a **getOrders** call using all of these filters:  

GET https://api.ebay.com/sell/v1/order?  
filter=**creationdate**:%5B2016-03-21T08:25:43.511Z..2016-04-21T08:25:43.511Z%5D,  
**lastmodifieddate**:%5B2016-05-15T08:25:43.511Z..%5D,  
**orderfulfillmentstatus**:%7BNOT\_STARTED%7CIN\_PROGRESS%7D

**Note:** This call requires that certain special characters in the URI query string be percent-encoded:  
    `[` = `%5B`       `]` = `%5D`       `{` = `%7B`       `|` = `%7C`       `}` = `%7D`  
This query filter example uses these codes.
- **limit** (string)
  - The number of orders to return per page of the result set. Use this parameter in conjunction with the **offset** parameter to control the pagination of the output.  
  
For example, if **offset** is set to `10` and **limit** is set to `10`, the call retrieves orders 11 through 20 from the result set.  
  
If a limit is not set, the **limit** defaults to 50 and returns up to 50 orders. If a requested limit is more than 200, the call fails and returns an error.  
  
**Note:** This feature employs a zero-based list, where the first item in the list has an offset of `0`. If the **orderIds** parameter is included in the request, this parameter will be ignored.  
**Maximum:** `200`  
**Default:** `50`
- **offset** (string)
  - Specifies the number of orders to skip in the result set before returning the first order in the paginated response.

Combine **offset** with the **limit** query parameter to control the items returned in the response. For example, if you supply an **offset** of `0` and a **limit** of `10`, the first page of the response contains the first 10 items from the complete list of items retrieved by the call. If **offset** is `10` and **limit** is `20`, the first page of the response contains items 11-30 from the complete result set.

**Default:** 0
- **orderIds** (string)
  - A comma-separated list of the unique identifiers of the orders to retrieve (maximum 50). If one or more order ID values are specified through the **orderIds** query parameter, all other query parameters will be ignored.  
  
**Note:** [getOrders](/develop/api/sell/fulfillment_api#sell-fulfillment_api-order-getorders) can return orders up to two years old. Do not provide the **orderId** for an order created more than two years in the past.

### issueRefund

#### POST /order/{order_id}/issue_refund
**Description:** This method allows a seller to issue a full or partial refund to a buyer for an order. Full or partial refunds can be issued at the order level or line item level. The refunds issued through this method are processed asynchronously, so the refund will not show as 'Refunded' right away. A seller will have to make a subsequent getOrder call to check the status of the refund. The status of an order refund can be found in the paymentSummary.refunds.refundStatus field of the getOrder response.
**Parameters:**
- **order_id** (string) *required*
  - This path parameter is used to specify the unique identifier of the order associated with a refund.  
  
Use the [getOrders](/develop/api/sell/fulfillment_api#sell-fulfillment_api-order-getorders) method to retrieve order IDs.
- **Content-Type** (string) *required*
  - This header indicates the format of the request body provided by the client. Its value should be set to **application/json**.

### getShippingFulfillments

#### GET /order/{orderId}/shipping_fulfillment
**Description:** Use this call to retrieve the contents of all fulfillments currently defined for a specified order based on the order's unique identifier, **orderId**. This value is returned in the [getOrders](/develop/api/sell/fulfillment_api#sell-fulfillment_api-order-getorders) call's **members.orderId** field when you search for orders by creation date or shipment status.
**Parameters:**
- **orderId** (string) *required*
  - This path parameter is used to specify the unique identifier of the order associated with the shipping fulfillments being retrieved.  
  
Use the [getOrders](/develop/api/sell/fulfillment_api#sell-fulfillment_api-order-getorders) method to retrieve order IDs. Order ID values are also shown in My eBay/Seller Hub.

### createShippingFulfillment

#### POST /order/{orderId}/shipping_fulfillment
**Description:** When you group an order's line items into one or more packages, each package requires a corresponding plan for handling, addressing, and shipping; this is _shipping fulfillment_. For each package, execute this call once to generate the shipping fulfillment associated with that package.  
  
**Note:** A single line item in an order can consist of multiple units of a purchased item, and one unit can consist of multiple parts or components. Although these components might be provided by the manufacturer in separate packaging, the seller must include all components of a given line item in the same package.  
Before using this call for a given package, you must determine which line items are in the package. If the package has been shipped, you should provide the date of shipment in the request. If not provided, it will default to the current date and time.  
  
This method can also be used to provide proof of delivery for contested payment disputes. To do so, use this method to create a shipping fulfillment and provide shipment tracking information for all line items involved in the dispute. EBay will then pick up this information for the dispute directly.
**Parameters:**
- **orderId** (string) *required*
  - This path parameter is used to specify the unique identifier of the order associated with the shipping fulfillment being created.  
  
Use the [getOrders](/develop/api/sell/fulfillment_api#sell-fulfillment_api-order-getorders) method to retrieve order IDs.
- **Content-Type** (string) *required*
  - This header indicates the format of the request body provided by the client. Its value should be set to **application/json**.

### getShippingFulfillment

#### GET /order/{orderId}/shipping_fulfillment/{fulfillmentId}
**Description:** Use this call to retrieve the contents of a fulfillment based on its unique identifier, **fulfillmentId** (combined with the associated order's **orderId**). The **fulfillmentId** value was originally generated by the **createShippingFulfillment** call and is returned by the [getShippingFulfillments](/develop/api/sell/fulfillment_api#sell-fulfillment_api-shipping_fulfillment-getshippingfulfillments) call in the **members.fulfillmentId** field.
**Parameters:**
- **fulfillmentId** (string) *required*
  - This path parameter is used to specify the unique identifier of the shipping fulfillment being retrieved.  
  
Use the [getShippingFulfillments](/develop/api/sell/fulfillment_api#sell-fulfillment_api-shipping_fulfillment-getshippingfulfillments) method to retrieve fulfillment IDs.
- **orderId** (string) *required*
  - This path parameter is used to specify the unique identifier of the order associated with the shipping fulfillment being retrieved.  
  
Use the [getOrders](/develop/api/sell/fulfillment_api#sell-fulfillment_api-order-getorders) method to retrieve order IDs. Order ID values are also shown in My eBay/Seller Hub.

### getPaymentDispute

#### GET /payment_dispute/{payment_dispute_id}
**Description:** This method retrieves detailed information on a specific payment dispute. The payment dispute identifier is passed in as path parameter at the end of the call URI.  
  
Below is a summary of the information that is retrieved:

*   Current status of payment dispute
*   Amount of the payment dispute
*   Reason the payment dispute was opened
*   Order and line items associated with the payment dispute
*   Seller response options if an action is currently required on the payment dispute
*   Details on the results of the payment dispute if it has been closed
*   Details on any evidence that was provided by the seller to fight the payment dispute
**Parameters:**
- **payment_dispute_id** (string) *required*
  - This parameter is used to specify the unique identifier of the payment dispute being retrieved.  
  
Use the [getPaymentDisputeSummaries](/develop/api/sell/fulfillment_api#sell-fulfillment_api-payment_dispute-getpaymentdisputesummaries) method to retrieve payment dispute IDs.

### fetchEvidenceContent

#### GET /payment_dispute/{payment_dispute_id}/fetch_evidence_content
**Description:** This call retrieves a specific evidence file for a payment dispute. The following three identifying parameters are needed in the call URI:

*   **payment\_dispute\_id**: the identifier of the payment dispute. The identifier of each payment dispute is returned in the [getPaymentDisputeSummaries](/develop/api/sell/fulfillment_api#sell-fulfillment_api-payment_dispute-getpaymentdisputesummaries) response.
*   **evidence\_id**: the identifier of the evidential file set. The identifier of an evidential file set for a payment dispute is returned under the **evidence** array in the [getPaymentDispute](/develop/api/sell/fulfillment_api#sell-fulfillment_api-payment_dispute-getpaymentdispute) response.
*   **file\_id**: the identifier of an evidential file. This file must belong to the evidential file set identified through the **evidence\_id** query parameter. The identifier of each evidential file is returned under the **evidence.files** array in the [getPaymentDispute](/develop/api/sell/fulfillment_api#sell-fulfillment_api-payment_dispute-getpaymentdispute) response.

An actual binary file is returned if the call is successful. An error will occur if any of three identifiers are invalid.
**Parameters:**
- **payment_dispute_id** (string) *required*
  - This path parameter is used to specify the unique identifier of the payment dispute associated with the evidence file being retrieved.  
  
Use the [getPaymentDisputeSummaries](/develop/api/sell/fulfillment_api#sell-fulfillment_api-payment_dispute-getpaymentdisputesummaries) method to retrieve payment dispute IDs.
- **evidence_id** (string) *required*
  - This query parameter is used to specify the unique identifier of the evidential file set.  
  
The identifier of an evidential file set for a payment dispute is returned under the **evidence** array in the [getPaymentDispute](/develop/api/sell/fulfillment_api#sell-fulfillment_api-payment_dispute-getpaymentdispute) response.
- **file_id** (string) *required*
  - This query parameter is used to specify the unique identifier of an evidential file. This file must belong to the evidential file set identified through the **evidence\_id** query parameter.  
  
The identifier of each evidential file is returned under the **evidence.files** array in the [getPaymentDispute](/develop/api/sell/fulfillment_api#sell-fulfillment_api-payment_dispute-getpaymentdispute) response.

### getActivities

#### GET /payment_dispute/{payment_dispute_id}/activity
**Description:** This method retrieves the activity log for a payment dispute. The identifier of the payment dispute is passed in as a path parameter. The output includes a timestamp for each action of the payment dispute, from creation to resolution, and all steps in between.
**Parameters:**
- **payment_dispute_id** (string) *required*
  - This parameter is used to specify the unique identifier of the payment dispute associated with the activity log being retrieved.  
  
Use the [getPaymentDisputeSummaries](/develop/api/sell/fulfillment_api#sell-fulfillment_api-payment_dispute-getpaymentdisputesummaries) method to retrieve payment dispute IDs.

### getPaymentDisputeSummaries

#### GET /payment_dispute_summary
**Description:** This method is used retrieve one or more payment disputes filed against the seller. These payment disputes can be open or recently closed. The following filter types are available in the request payload to control the payment disputes that are returned:

*   Dispute filed against a specific order (**order\_id** parameter is used)
*   Dispute(s) filed by a specific buyer (**buyer\_username** parameter is used)
*   Dispute(s) filed within a specific date range (**open\_date\_from** and/or **open\_date\_to** parameters are used)
*   Disputes in a specific state (**payment\_dispute\_status** parameter is used)

More than one of these filter types can be used together. See the request payload request fields for more information about how each filter is used.  
  
If none of the filters are used, all open and recently closed payment disputes are returned.  
  
Pagination is also available. See the **limit** and **offset** fields for more information on how pagination is used for this method.
**Parameters:**
- **order_id** (string)
  - This filter is used if the seller wishes to retrieve one or more payment disputes filed against a specific order. It is possible that there can be more than one dispute filed against an order if the order has multiple line items. If this filter is used, any other filters are ignored.  
  
Use the [getOrders](/develop/api/sell/fulfillment_api#sell-fulfillment_api-order-getorders) method to retrieve order IDs. Order ID values are also shown in My eBay/Seller Hub.
- **buyer_username** (string)
  - This filter is used if the seller wishes to retrieve one or more payment disputes opened by a specific buyer. The string that is passed in to this query parameter is the eBay user ID of the buyer.
- **open_date_from** (string)
  - The **open\_date\_from** and/or **open\_date\_to** date filters are used if the seller wishes to retrieve payment disputes opened within a specific date range. A maximum date range that may be set with the **open\_date\_from** and/or **open\_date\_to** filters is 90 days. These date filters use the [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html "https://www.iso.org ") 24-hour date and time format, and time zone used is Universal Coordinated Time (UTC), also known as Greenwich Mean Time (GMT), or Zulu.  
  
The **open\_date\_from** field sets the beginning date of the date range, and can be set as far back as 18 months from the present time. If a **open\_date\_from** field is used, but a **open\_date\_to** field is not used, the **open\_date\_to** value will default to 90 days after the date specified in the **open\_date\_from** field, or to the present time if less than 90 days in the past.  
  
The ISO 8601 format looks like this: _yyyy-MM-ddThh:mm.ss.sssZ_. An example would be `2019-08-04T19:09:02.768Z`.
- **open_date_to** (string)
  - The **open\_date\_from** and/or **open\_date\_to** date filters are used if the seller wishes to retrieve payment disputes opened within a specific date range. A maximum date range that may be set with the **open\_date\_from** and/or **open\_date\_to** filters is 90 days. These date filters use the [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html "https://www.iso.org ") 24-hour date and time format, and the time zone used is Universal Coordinated Time (UTC), also known as Greenwich Mean Time (GMT), or Zulu.  
  
The **open\_date\_to** field sets the ending date of the date range, and can be set up to 90 days from the date set in the **open\_date\_from** field.  
  
The ISO 8601 format looks like this: _yyyy-MM-ddThh:mm.ss.sssZ_. An example would be `2019-08-04T19:09:02.768Z`.
- **payment_dispute_status** (string)
  - This filter is used if the seller wishes to only retrieve payment disputes in one or more specific states. To filter by more than one status value, a separate **payment\_dispute\_status** filter must be used for each value, as shown below:  
  
_https://apiz.ebay.com/sell/fulfillment/v1/payment\_dispute\_summary?payment\_dispute\_status=OPEN&payment\_dispute\_status=ACTION\_NEEDED_  
  
If no **payment\_dispute\_status** filter is used, payment disputes in all states are returned in the response.  
  
See [DisputeStateEnum](/develop/api/sell/fulfillment_api#sell-fulfillment_api-payment_dispute-getpaymentdispute.disputestateenum) type for supported values.
- **limit** (string)
  - The value passed in this query parameter sets the maximum number of payment disputes to return per page of data. The value passed in this field should be an integer from 1 to 200. If this query parameter is not set, up to 200 records will be returned on each page of results.  
  
**Min**: 1  
  
**Max**: 200  
  
**Default**: 200
- **offset** (string)
  - This field is used to specify the number of records to skip in the result set before returning the first payment dispute in the paginated response. A zero-based index is used, so if you set the **offset** value to `0` (default value), the first payment dispute in the result set appears at the top of the response.  
  
Combine **offset** with the **limit** parameter to control the payment disputes returned in the response. For example, if you supply an **offset** value of `0` and a **limit** value of `10`, the response will contain the first 10 payment disputes from the result set that matches the input criteria. If you supply an **offset** value of `10` and a **limit** value of `20`, the response will contain payment disputes 11-30 from the result set that matches the input criteria.  
  
**Min**: 0  
  
**Default**: 0

### contestPaymentDispute

#### POST /payment_dispute/{payment_dispute_id}/contest
**Description:** This method is used if the seller wishes to contest a payment dispute initiated by the buyer. The unique identifier of the payment dispute is passed in as a path parameter, and unique identifiers for payment disputes can be retrieved with the [getPaymentDisputeSummaries](/develop/api/sell/fulfillment_api#sell-fulfillment_api-payment_dispute-getpaymentdisputesummaries) method.  
  
**Note:** Before contesting a payment dispute, the seller must upload all supporting files using the **addEvidence** and **updateEvidence** methods. Once the seller has officially contested the dispute (using **contestPaymentDispute**), the **addEvidence** and **updateEvidence** methods can no longer be used. In the **evidenceRequests** array of the **getPaymentDispute** response, eBay prompts the seller with the type of supporting file(s) that will be needed to contest the payment dispute.  
If a seller decides to contest a payment dispute, that seller should be prepared to provide supporting documents such as proof of delivery, proof of authentication, or other documents. The type of supporting documents that the seller will provide will depend on why the buyer filed the payment dispute.  
  
The **revision** field in the request payload is required, and the **returnAddress** field should be supplied if the seller is expecting the buyer to return the item. See the Request Payload section for more information on these fields.
**Parameters:**
- **payment_dispute_id** (string) *required*
  - This parameter is used to specify the unique identifier of the payment dispute being contested.  
  
Use the [getPaymentDisputeSummaries](/develop/api/sell/fulfillment_api#sell-fulfillment_api-payment_dispute-getpaymentdisputesummaries) method to retrieve payment dispute IDs.
- **Content-Type** (string) *required*
  - This header indicates the format of the request body provided by the client. Its value should be set to **application/json**.

### acceptPaymentDispute

#### POST /payment_dispute/{payment_dispute_id}/accept
**Description:** This method is used if the seller wishes to accept a payment dispute. The unique identifier of the payment dispute is passed in as a path parameter, and unique identifiers for payment disputes can be retrieved with the [getPaymentDisputeSummaries](/develop/api/sell/fulfillment_api#sell-fulfillment_api-payment_dispute-getpaymentdisputesummaries) method.  
  
The **revision** field in the request payload is required, and the **returnAddress** field should be supplied if the seller is expecting the buyer to return the item. See the Request Payload section for more information on theste fields.
**Parameters:**
- **payment_dispute_id** (string) *required*
  - This parameter is used to specify the unique identifier of the payment dispute being accepted.  
  
Use the [getPaymentDisputeSummaries](/develop/api/sell/fulfillment_api#sell-fulfillment_api-payment_dispute-getpaymentdisputesummaries) method to retrieve payment dispute IDs.
- **Content-Type** (string) *required*
  - This header indicates the format of the request body provided by the client. Its value should be set to **application/json**.

### uploadEvidenceFile

#### POST /payment_dispute/{payment_dispute_id}/upload_evidence_file
**Description:** This method is used to upload an evidence file for a contested payment dispute. The unique identifier of the payment dispute is passed in as a path parameter, and unique identifiers for payment disputes can be retrieved with the [getPaymentDisputeSummaries](/develop/api/sell/fulfillment_api#sell-fulfillment_api-payment_dispute-getpaymentdisputesummaries) method.  
  
**Note:** The **uploadEvidenceFile** only uploads an encrypted, binary image file (using **multipart/form-data** HTTP request header), and does not have a JSON-based request payload.  
  
Use 'file' as the name of the key that you use to upload the image file. The upload will not be successful if a different key name is used.  
  
The three image formats supported at this time are **.JPEG**, **.JPG**, and **.PNG**.  
After the file is successfully uploaded, the seller will need to grab the **fileId** value in the response payload to add this file to a new evidence set using the **addEvidence** method, or to add this file to an existing evidence set using the **updateEvidence** method.  
  

**Important!** This method only supports file upload. If `PROOF_OF_DELIVERY` is requested when contesting a payment dispute, do **not** upload shipment tracking information for proof of order delivery using this method. Instead, use the [createShippingFulfillment](/develop/api/sell/fulfillment_api#sell-fulfillment_api-shipping_fulfillment-createshippingfulfillment) to provide tracking information evidence for a dispute.
**Parameters:**
- **payment_dispute_id** (string) *required*
  - This parameter is used to specify the unique identifier of the contested payment dispute for which the user intends to upload an evidence file.  
  
Use the [getPaymentDisputeSummaries](/develop/api/sell/fulfillment_api#sell-fulfillment_api-payment_dispute-getpaymentdisputesummaries) method to retrieve payment dispute IDs.
- **Content-Type** (string) *required*
  - This header indicates the format of the request body provided by the client. Its value should be set to **multipart/form-data**.

### addEvidence

#### POST /payment_dispute/{payment_dispute_id}/add_evidence
**Description:** This method is used by the seller to add one or more evidence files to address a payment dispute initiated by the buyer. The unique identifier of the payment dispute is passed in as a path parameter, and unique identifiers for payment disputes can be retrieved with the [getPaymentDisputeSummaries](/develop/api/sell/fulfillment_api#sell-fulfillment_api-payment_dispute-getpaymentdisputesummaries) method.  
  
**Note:** All evidence files should be uploaded using **addEvidence** and **updateEvidence** before the seller decides to contest the payment dispute. Once the seller has officially contested the dispute (using **contestPaymentDispute** or through My eBay), the **addEvidence** and **updateEvidence** methods can no longer be used. In the **evidenceRequests** array of the **getPaymentDispute** response, eBay prompts the seller with the type of evidence file(s) that will be needed to contest the payment dispute.  
  
The file(s) to add are identified through the **files** array in the request payload. Adding one or more new evidence files for a payment dispute triggers the creation of an evidence file, and the unique identifier for the new evidence file is automatically generated and returned in the **evidenceId** field of the **addEvidence** response payload upon a successful call.  
  
The type of evidence being added should be specified in the **evidenceType** field. All files being added (if more than one) should correspond to this evidence type.  
  
Upon a successful call, an **evidenceId** value is returned in the response. This indicates that a new evidence set has been created for the payment dispute, and this evidence set includes the evidence file(s) that were passed in to the **fileId** array. The **evidenceId** value will be needed if the seller wishes to add to the evidence set by using the **updateEvidence** method, or if they want to retrieve a specific evidence file within the evidence set by using the [fetchEvidenceContent](/develop/api/sell/fulfillment_api#sell-fulfillment_api-payment_dispute-fetchevidencecontent) method.
**Parameters:**
- **payment_dispute_id** (string) *required*
  - This parameter is used to specify the unique identifier of the contested payment dispute for which the seller wishes to add evidence files.  
  
Use the [getPaymentDisputeSummaries](/develop/api/sell/fulfillment_api#sell-fulfillment_api-payment_dispute-getpaymentdisputesummaries) method to retrieve payment dispute IDs.
- **Content-Type** (string) *required*
  - This header indicates the format of the request body provided by the client. Its value should be set to **application/json**.

### updateEvidence

#### POST /payment_dispute/{payment_dispute_id}/update_evidence
**Description:** This method is used by the seller to update an existing evidence set for a payment dispute with one or more evidence files. The unique identifier of the payment dispute is passed in as a path parameter, and unique identifiers for payment disputes can be retrieved with the [getPaymentDisputeSummaries](/develop/api/sell/fulfillment_api#sell-fulfillment_api-payment_dispute-getpaymentdisputesummaries) method.  
  
**Note:** All evidence files should be uploaded using **addEvidence** and **updateEvidence** before the seller decides to contest the payment dispute. Once the seller has officially contested the dispute (using **contestPaymentDispute** or through My eBay), the **addEvidence** and **updateEvidence** methods can no longer be used. In the **evidenceRequests** array of the **getPaymentDispute** response, eBay prompts the seller with the type of evidence file(s) that will be needed to contest the payment dispute.  
The unique identifier of the evidence set to update is specified through the **evidenceId** field, and the file(s) to add are identified through the **files** array in the request payload. The unique identifier for an evidence file is automatically generated and returned in the **fileId** field of the **uploadEvidence** response payload upon a successful call. Sellers must make sure to capture the **fileId** value for each evidence file that is uploaded with the **uploadEvidence** method.  
  
The type of evidence being added should be specified in the **evidenceType** field. All files being added (if more than one) should correspond to this evidence type.  
  
Upon a successful call, an http status code of `204 Success` is returned. There is no response payload unless an error occurs. To verify that a new file is a part of the evidence set, the seller can use the [fetchEvidenceContent](/develop/api/sell/fulfillment_api#sell-fulfillment_api-payment_dispute-fetchevidencecontent) method, passing in the proper **evidenceId** and **fileId** values.
**Parameters:**
- **payment_dispute_id** (string) *required*
  - This parameter is used to specify the unique identifier of the contested payment dispute for which the user plans to update the evidence set.  
  
Use the [getPaymentDisputeSummaries](/develop/api/sell/fulfillment_api#sell-fulfillment_api-payment_dispute-getpaymentdisputesummaries) method to retrieve payment dispute IDs.
- **Content-Type** (string) *required*
  - This header indicates the format of the request body provided by the client. Its value should be set to **application/json**.

## Error Codes

The following error codes may be returned by this API:

### REQUEST Errors

#### 32100 - API_FULFILLMENT
**Description:** Invalid order ID: {orderId}

#### 32800 - API_FULFILLMENT
**Description:** Invalid field group: {fieldGroup}

#### 30700 - API_FULFILLMENT
**Description:** Invalid filter name: {fieldname}

#### 30800 - API_FULFILLMENT
**Description:** Invalid filter value {fieldvalue} for filter {fieldname}

#### 30810 - API_FULFILLMENT
**Description:** Invalid date format

#### 30820 - API_FULFILLMENT
**Description:** Start date is missing

#### 30830 - API_FULFILLMENT
**Description:** Time range between start date and end date must be within '{allowedTime}' years.

#### 30840 - API_FULFILLMENT
**Description:** Start date should be before end date

#### 30850 - API_FULFILLMENT
**Description:** Start and end dates can't be in the future

#### 30900 - API_FULFILLMENT
**Description:** Exceeded maximum number of order IDs (the current limit is `50`)

#### 31000 - API_FULFILLMENT
**Description:** Invalid offset: {offsetvalue}

#### 31100 - API_FULFILLMENT
**Description:** Invalid limit: {limitvalue}

#### 34901 - API_FULFILLMENT
**Description:** Order id can't be null or empty.

#### 34902 - API_FULFILLMENT
**Description:** Request can't be empty.

#### 34903 - API_FULFILLMENT
**Description:** The refund reason must be specified.

#### 34905 - API_FULFILLMENT
**Description:** Either **orderLevelRefundAmount** or **refundItems** must be specified.

#### 34906 - API_FULFILLMENT
**Description:** The amount value must be specified.

#### 34907 - API_FULFILLMENT
**Description:** The amount value must be positive and within two decimals.

#### 34908 - API_FULFILLMENT
**Description:** The amount currency must be specified.

#### 34909 - API_FULFILLMENT
**Description:** The amount currency isn't correct.

#### 34910 - API_FULFILLMENT
**Description:** Either legacyReference or lineItemId must be specified for item level refund.

#### 34911 - API_FULFILLMENT
**Description:** Legacy item id must be specified for item level refund if you use legacyReference.

#### 34912 - API_FULFILLMENT
**Description:** Legacy transaction id must be specified for item level refund if you use legacyReference.

#### 34914 - API_FULFILLMENT
**Description:** Can't find the item in the order.

#### 34915 - API_FULFILLMENT
**Description:** The refund amount exceeds order amount.

#### 34921 - API_FULFILLMENT
**Description:** The comment exceeds the length limit, please make sure it doesn't exceed 1000 characters.

#### 34922 - API_FULFILLMENT
**Description:** Refund cannot be issued while previous refund is processing.

#### 34923 - API_FULFILLMENT
**Description:** Refund cannot be issued for this type of order.

#### 1001 - OAUTH
**Description:** Invalid access token. Check the value of the Authorization HTTP request header.

#### 1100 - ACCESS
**Description:** Insufficient permissions to fulfill the request.

#### 34913 - API_FULFILLMENT
**Description:** Can not find the order.

#### 34919 - API_FULFILLMENT
**Description:** Unauthorized access.

#### 34929 - API_FULFILLMENT
**Description:** You cannot refund this order yet since the buyer payment has not been processed. Please try again later.

#### 34930 - API_FULFILLMENT
**Description:** Default payment method limit exceeded. Please use a different payment option or try again later.

#### 32200 - API_FULFILLMENT
**Description:** Invalid line item id: {lineItemId}

#### 32210 - API_FULFILLMENT
**Description:** Duplicate line item in the request

#### 32300 - API_FULFILLMENT
**Description:** Invalid shipment tracking number or carrier

#### 32400 - API_FULFILLMENT
**Description:** Requested user is suspended

#### 32500 - API_FULFILLMENT
**Description:** Invalid shipped date

#### 32600 - API_FULFILLMENT
**Description:** Invalid input data

#### 34100 - API_FULFILLMENT
**Description:** Maximum tracking number for order is exceeded

#### 34200 - API_FULFILLMENT
**Description:** Line Items contain Global Shipping Program and non-Global Shipping Program orders

#### 34300 - API_FULFILLMENT
**Description:** Mark As Shipped for multiple Global Shipping Program line items is not supported

#### 34500 - API_FULFILLMENT
**Description:** Please use PUT operation for updating shipping fulfillment

#### 32110 - API_FULFILLMENT
**Description:** Invalid shipping fulfillment ID: {fulfillmentId}

#### 33001 - API_FULFILLMENT
**Description:** Invalid Payment Dispute Id.

#### 33002 - API_FULFILLMENT
**Description:** Invalid Evidence Id.

#### 33003 - API_FULFILLMENT
**Description:** Invalid Evidence File Id.

#### 33100 - API_FULFILLMENT
**Description:** Invalid input request.

#### 33011 - API_FULFILLMENT
**Description:** There was a change in payment dispute attributes. Please use get payment dispute api to get latest details.

#### 33101 - API_FULFILLMENT
**Description:** Invalid payment dispute state.

#### 33102 - API_FULFILLMENT
**Description:** No evidence available for contest.

#### 33005 - API_FULFILLMENT
**Description:** File type is invalid.

#### 33006 - API_FULFILLMENT
**Description:** File size should be 1.5 MB or less.

#### 33106 - API_FULFILLMENT
**Description:** The file name should not be empty and should not exceed 255 characters.

#### 33107 - API_FULFILLMENT
**Description:** Only one file can be uploaded per request.

#### 33004 - API_FULFILLMENT
**Description:** Upload file for evidence is not permitted for given payment dispute state.

#### 33105 - API_FULFILLMENT
**Description:** You reached the maximum number of files you can upload.

#### 33007 - API_FULFILLMENT
**Description:** Invalid line items.

#### 33008 - API_FULFILLMENT
**Description:** Invalid evidence type.

#### 33009 - API_FULFILLMENT
**Description:** User did not echo back the evidence metadata correctly.

#### 33103 - API_FULFILLMENT
**Description:** Exceed allowed file count.

#### 33104 - API_FULFILLMENT
**Description:** The combined size of attached files should be 1.5MB or less.

#### 33010 - API_FULFILLMENT
**Description:** Evidence Id is invalid.

### APPLICATION Errors

#### 30500 - API_FULFILLMENT
**Description:** System error

#### 34900 - API_FULFILLMENT
**Description:** There was a problem with an eBay internal system or process. Contact eBay developer support for assistance.

#### 33000 - API_FULFILLMENT
**Description:** There was a problem with an eBay internal system or process. Contact eBay developer support for assistance.

### BUSINESS Errors

#### 34916 - API_FULFILLMENT
**Description:** A post-transaction case exists on this order, seller refund can't be triggered.

#### 34917 - API_FULFILLMENT
**Description:** This order was already refunded.

#### 34920 - API_FULFILLMENT
**Description:** It's too late to issue a refund for this order.

#### 34918 - API_FULFILLMENT
**Description:** This is not an eBay managed payments order.

#### 34924 - API_FULFILLMENT
**Description:** The item refund amount exceeds the item remaining amount.

#### 34925 - API_FULFILLMENT
**Description:** The refund operation could not be completed with any of the payment methods saved to the seller's account.

#### 34926 - API_FULFILLMENT
**Description:** A suitable payment method could not be found for the refund operation. Please resolve in Seller Hub.

#### 34927 - API_FULFILLMENT
**Description:** The selected payment method for the refund operation was invalid or declined.

#### 34928 - API_FULFILLMENT
**Description:** Your refund did not go through because we could not verify your payment option. Please change your payment option and try again.

## Rate Limits

See [API Call Limits](https://developer.ebay.com/develop/get-started/api-call-limits) on the eBay Developer Program.

## Resources

### Documentation

- [eBay Developer Program](https://developer.ebay.com/)
- [API Documentation](https://developer.ebay.com/develop/api/)
- [SDKs and Widgets](https://developer.ebay.com/develop/sdks-and-widgets)
- [Developer Community Forum](https://community.ebay.com/t5/Developer-Groups/ct-p/developergroup)

### Tools

- [API Explorer](https://developer.ebay.com/my/api_test_tool)
- [GraphQL Explorer](https://developer.ebay.com/my/graphql_explorer)

### Support

- [Developer Support](https://developer.ebay.com/support/)
- [API Status](https://developer.ebay.com/support/api-status)
- [Release Notes](https://developer.ebay.com/develop/api/release_notes/)

---
*Generated on 2026-08-04T15:52:37.077Z*