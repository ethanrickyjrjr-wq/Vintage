---
title: Notification API
description: "The eBay **Notification API** provides a comprehensive set of resources for developers to manage the entire lifecycle of asynchronous notifications from eBay. Users can browse available notification topics, configure and manage destination endpoints for receiving notifications, create and manage subscriptions to specific topics with optional filtering, and validate the integrity of received message payloads using public keys. The API supports both application-based and user-based subscriptions, utilizing OAuth 2.0 grant flows, and is essential for applications requiring timely updates on events such as order confirmations, listing revisions, feedback received, and user account changes."
api_version: 1.0
api_name: notification_api
api_type: REST
api_group: sell/notification_api
source_url:
  html: https://developer.ebay.com/develop/api/sell/notification_api
  md: https://developer.ebay.com/develop/api/sell/notification_api.md
---

# Notification API API

The eBay **Notification API** provides a comprehensive set of resources for developers to manage the entire lifecycle of asynchronous notifications from eBay. Users can browse available notification topics, configure and manage destination endpoints for receiving notifications, create and manage subscriptions to specific topics with optional filtering, and validate the integrity of received message payloads using public keys. The API supports both application-based and user-based subscriptions, utilizing OAuth 2.0 grant flows, and is essential for applications requiring timely updates on events such as order confirmations, listing revisions, feedback received, and user account changes.

## API Methods

The following API methods are available:

### getConfig

#### GET /config
**Description:** This method allows applications to retrieve a previously created configuration.

### updateConfig

#### PUT /config
**Description:** This method allows applications to create a new configuration or update an existing configuration. This app-level configuration allows developers to set up alerts.
**Parameters:**
- **Content-Type** (string) *required*
  - This header indicates the format of the request body provided by the client. Its value should be set to **application/json**.

### createDestination

#### POST /destination
**Description:** This method allows applications to create a destination. A destination is an endpoint that receives HTTP push notifications.  
  
A single destination for all topics is valid, as is individual destinations for each topic.  
  
To update a destination, use the [updateDestination](/develop/api/sell/notification_api#sell-notification_api-destination-updatedestination) call.  
  
The destination created will need to be referenced while creating or updating a subscription to a topic.  
  
**Note:** The destination should be created and ready to respond with the expected **challengeResponse** for the endpoint to be registered successfully. See the [Communications Guide](/develop/guides/sell/sell-communications-guide#retrievingeBaynotifications) for more information.
**Parameters:**
- **Content-Type** (string) *required*
  - This header indicates the format of the request body provided by the client. Its value should be set to **application/json**.

### deleteDestination

#### DELETE /destination/{destination_id}
**Description:** This method provides applications a way to delete a destination.  
  
The same destination ID can be used by many destinations.  
  
Trying to delete an active destination results in an error. You can disable a subscription, and when the destination is no longer in use, you can delete it.
**Parameters:**
- **destination_id** (string) *required*
  - The unique identifier of the destination to delete. Only disabled or marked down destinations can be deleted, and enabled destinations cannot be deleted. Use [getDestination](/develop/api/sell/notification_api#sell-notification_api-destination-getdestination) or [getDestinations](/develop/api/sell/notification_api#sell-notification_api-destination-getdestinations) to see the current status of a destination.

### getDestination

#### GET /destination/{destination_id}
**Description:** This method allows applications to fetch the details for a destination. The details include the destination name, status, and configuration, including the endpoint and verification token.
**Parameters:**
- **destination_id** (string) *required*
  - The unique identifier of the destination to retrieve. Use [getDestinations](/develop/api/sell/notification_api#sell-notification_api-destination-getdestinations) to retrieve destination IDs.

### getDestinations

#### GET /destination
**Description:** This method allows applications to retrieve a paginated collection of destination resources and related details. The details include the destination names, statuses, and configurations, including the endpoints and verification tokens.
**Parameters:**
- **continuation_token** (string)
  - This string value can be used to return the next page in the result set. The string to use here is returned in the **next** field of the current page of results.
- **limit** (string)
  - The maximum number of destinations to return per page from the result set.  
  
**Min:** 10  
  
**Max:** 100  
  
**Default:** 20

### updateDestination

#### PUT /destination/{destination_id}
**Description:** This method allows applications to update a destination.  
  
**Note:** The destination should be created and ready to respond with the expected **challengeResponse** for the endpoint to be registered successfully.
**Parameters:**
- **Content-Type** (string) *required*
  - This header indicates the format of the request body provided by the client. Its value should be set to **application/json**.
- **destination_id** (string) *required*
  - The unique identifier for the destination.

### getPublicKey

#### GET /public_key/{public_key_id}
**Description:** This method allows users to retrieve a public key using a specified key ID. The public key that is returned in the response payload is used to process and validate eBay notifications.  
  
The public key ID, which is a required request parameter for this method, is retrieved from the Base64-encoded **X-EBAY-SIGNATURE** header that is included in the eBay notification.  
  

**Important!** The retrieved public key value should be cached for a temporary — but reasonable — amount of time (e.g., one-hour is recommended.) This key should not be requested for every notification since doing so can result in exceeding [API call limits](/develop/apis/api-call-limits) if a large number of notification requests is received.

  
**Note:** For more details about how to process eBay push notifications and validate notification message payloads, see the [Communications Guide](/develop/guides-v2/sell-communications-guide#overview).
**Parameters:**
- **public_key_id** (string) *required*
  - The unique key ID that is used to retrieve the public key.  
  
**Note:** This is retrieved from the **X-EBAY-SIGNATURE** header that is included with the push notification.

### createSubscription

#### POST /subscription
**Description:** This method allows applications to create a subscription for a topic and supported schema version. Subscriptions allow applications to express interest in notifications and keep receiving the information relevant to their business.  
  
Each application and topic-schema pairing to a subscription should have a 1:1 cardinality.  
  
You can create the subscription in disabled mode, test it (see the **test** method), and when everything is ready, you can enable the subscription (see the [enableSubscription](/develop/api/sell/notification_api#sell-notification_api-subscription-enablesubscription) method).  
  
**Note:** If an application is not authorized to subscribe to a topic, for example, if your authorization does not include the list of scopes required for the topic, an error code of 195011 is returned.
**Parameters:**
- **Content-Type** (string) *required*
  - This header indicates the format of the request body provided by the client. Its value should be set to **application/json**.

### createSubscriptionFilter

#### POST /subscription/{subscription_id}/filter
**Description:** This method allows applications to create a filter for a subscription. Filters allow applications to only be sent notifications that match a provided criteria. Notifications that do not match this criteria will not be sent to the destination.  
  
The **filterSchema** value must be a valid [JSON Schema Core document](<https://json-schema.org >) (version 2020-12 or later). The **filterSchema** provided must describe the subscription's notification payload such that it supplies valid criteria to filter the subscription's notifications. The user does not need to provide `$schema` and `$id` definitions.  
  
When a filter is first created, it is not immediately active on the subscription. If the request has a valid JSON body, the successful call returns the HTTP status code **201 Created**. Newly created filters are in `PENDING` status until they are reviewed. If a filter is valid, it will move from `PENDING` status to `ENABLED` status. You can find the status of a filter using the [getSubscriptionFilter](/develop/api/sell/notification_api#sell-notification_api-subscription-getsubscriptionfilter) method.  
  
**Note:** Only one filter can be in `ENABLED` (which means active) status on a subscription at a time. If an `ENABLED` filter is overwritten by a new call to `CREATE` a filter for the subscription, it stays in **ENABLED** status until the new **PENDING** filter becomes the `ENABLED` filter, and the existing filter then becomes `DISABLED`.
**Parameters:**
- **Content-Type** (string) *required*
  - This header indicates the format of the request body provided by the client. Its value should be set to **application/json**.
- **subscription_id** (string) *required*
  - The unique identifier of the subscription for which a filter will be created.

### deleteSubscription

#### DELETE /subscription/{subscription_id}
**Description:** This method allows applications to delete a subscription. Subscriptions can be deleted regardless of status.
**Parameters:**
- **subscription_id** (string) *required*
  - The unique identifier of the subscription to delete. Use [getSubscriptions](/develop/api/sell/notification_api#sell-notification_api-subscription-getsubscriptions) to retrieve subscription IDs.

### deleteSubscriptionFilter

#### DELETE /subscription/{subscription_id}/filter/{filter_id}
**Description:** This method allows applications to disable the active filter on a subscription, so that a new subscription filter may be added.  
  
**Note:** Subscription filters in `PENDING` status can not be disabled. However, a new filter can be created instead with the [createSubscriptionFilter](/develop/api/sell/notification_api#sell-notification_api-subscription-createsubscriptionfilter) method and this new filter will override the `PENDING` filter.
**Parameters:**
- **filter_id** (string) *required*
  - The unique identifier of the subscription filter to delete. Filter ID values, if configured for a subscription, will be shown in the **subscriptions.filterId** field in **getSubscription** and **getSubscription** responses. The filter ID value is also returned in the Location response header when a filter is created with [createSubscriptionFilter](/develop/api/sell/notification_api#sell-notification_api-subscription-createsubscriptionfilter).
- **subscription_id** (string) *required*
  - The unique identifier of the subscription associated with the filter to delete. Use [getSubscriptions](/develop/api/sell/notification_api#sell-notification_api-subscription-getsubscriptions) to retrieve subscription IDs.

### disableSubscription

#### POST /subscription/{subscription_id}/disable
**Description:** This method disables a subscription, which prevents the subscription from providing notifications. To restart a subscription, call [enableSubscription](/develop/api/sell/notification_api#sell-notification_api-subscription-enablesubscription).
**Parameters:**
- **subscription_id** (string) *required*
  - The unique identifier of an enabled subscription that will be disabled. Use [getSubscriptions](/develop/api/sell/notification_api#sell-notification_api-subscription-getsubscriptions) to retrieve subscription IDs.

### enableSubscription

#### POST /subscription/{subscription_id}/enable
**Description:** This method allows applications to enable a disabled subscription. To pause (or disable) an enabled subscription, call [disableSubscription](/develop/api/sell/notification_api#sell-notification_api-subscription-disablesubscription).
**Parameters:**
- **subscription_id** (string) *required*
  - The unique identifier of a disabled subscription that will be enabled. Use [getSubscriptions](/develop/api/sell/notification_api#sell-notification_api-subscription-getsubscriptions) to retrieve subscription IDs.

### getSubscription

#### GET /subscription/{subscription_id}
**Description:** This method allows applications to retrieve subscription details for the specified subscription.  
  
Specify the subscription to retrieve using the **subscription\_id**. Use the [getSubscriptions](/develop/api/sell/notification_api#sell-notification_api-subscription-getsubscriptions) method to browse all subscriptions if you do not know the **subscription\_id**.  
  
Subscriptions allow applications to express interest in notifications and keep receiving the information relevant to their business.
**Parameters:**
- **subscription_id** (string) *required*
  - The unique identifier of the subscription to retrieve. Use [getSubscriptions](/develop/api/sell/notification_api#sell-notification_api-subscription-getsubscriptions) to retrieve subscription IDs.

### getSubscriptionFilter

#### GET /subscription/{subscription_id}/filter/{filter_id}
**Description:** This method allows applications to retrieve the filter details for the specified subscription filter.  
  
Specify the subscription filter to retrieve by using the **subscription\_id** and the **filter\_id** associated with the subscription filter. The **filter\_id** can be found in the response body for the **getSubscription** method, if there is a filter applied on the subscription.  
  
Filters allow applications to only be sent notifications that match a provided criteria. Notifications that do not match this criteria will not be sent to the destination.
**Parameters:**
- **filter_id** (string) *required*
  - The unique identifier of the subscription filter. Filter ID values, if configured for a subscription, will be shown in the **subscriptions.filterId** field in **getSubscription** and **getSubscription** responses. The filter ID value is also returned in the Location response header when a filter is created with **createSubscriptionFilter**.
- **subscription_id** (string) *required*
  - The unique identifier of the subscription associated with the filter. Use [getSubscriptions](/develop/api/sell/notification_api#sell-notification_api-subscription-getsubscriptions) to retrieve subscription IDs.

### getSubscriptions

#### GET /subscription
**Description:** This method allows applications to retrieve a list of all subscriptions. The list returned is a paginated collection of subscription resources.  
  
Subscriptions allow applications to express interest in notifications and keep receiving the information relevant to their business.
**Parameters:**
- **continuation_token** (string)
  - This string value can be used to return the next page in the result set. The string to use here is returned in the next field of the current page of results.
- **limit** (string)
  - The maximum number of subscriptions to return per page from the result set.  
  
**Min:** 10  
  
**Max:** 100  
  
**Default:** 20

### testSubscription

#### POST /subscription/{subscription_id}/test
**Description:** This method triggers a mocked test payload that includes a notification ID, publish date, and so on. Use this method to test your subscription end-to-end.  
  
You can create the subscription in disabled mode, test it using this method, and when everything is ready, you can enable the subscription (see the [enableSubscription](/develop/api/sell/notification_api#sell-notification_api-subscription-enablesubscription) method).  
  
**Note:** Use the **notificationId** to tell the difference between a test payload and a real payload.
**Parameters:**
- **subscription_id** (string) *required*
  - The unique identifier of the subscription to test. Use [getSubscriptions](/develop/api/sell/notification_api#sell-notification_api-subscription-getsubscriptions) to retrieve subscription IDs.

### updateSubscription

#### PUT /subscription/{subscription_id}
**Description:** This method allows applications to update a subscription. Subscriptions allow applications to express interest in notifications and keep receiving the information relevant to their business.  
  
**Note:** This call returns an error if an application is not authorized to subscribe to a topic.  
  
You can pause and restart a subscription. See the [disableSubscription](/develop/api/sell/notification_api#sell-notification_api-subscription-disablesubscription) and [enableSubscription](/develop/api/sell/notification_api#sell-notification_api-subscription-enablesubscription)methods.
**Parameters:**
- **Content-Type** (string) *required*
  - This header indicates the format of the request body provided by the client. Its value should be set to **application/json**.
- **subscription_id** (string) *required*
  - The unique identifier for the subscription to update. Use [getSubscriptions](/develop/api/sell/notification_api#sell-notification_api-subscription-getsubscriptions) to retrieve subscription IDs.

### getTopic

#### GET /topic/{topic_id}
**Description:** This method allows applications to retrieve details for the specified topic. This information includes supported schema versions, formats, and other metadata for the topic.  
  
Applications can subscribe to any of the topics for a supported schema version and format, limited by the authorization scopes required to subscribe to the topic.  
  
A topic specifies the type of information to be received and the data types associated with an event. An event occurs in the eBay system, such as when a user requests deletion or revokes access for an application. An event is an instance of an event type (topic).  
  
Specify the topic to retrieve using the **topic\_id** URI parameter.  
  
**Note:** Use the [getTopics](/develop/api/sell/notification_api#sell-notification_api-topic-gettopics) method to find a topic if you do not know the topic ID.
**Parameters:**
- **topic_id** (string) *required*
  - The unique identifier of the notification topic for which the details are retrieved. Use [getTopics](/develop/api/sell/notification_api#sell-notification_api-topic-gettopics) to retrieve the topic ID.

### getTopics

#### GET /topic
**Description:** This method returns a paginated collection of all supported topics, along with the details for the topics. This information includes supported schema versions, formats, and other metadata for the topics.  
  
Applications can subscribe to any of the topics for a supported schema version and format, limited by the authorization scopes required to subscribe to the topic.  
  
A topic specifies the type of information to be received and the data types associated with an event. An event occurs in the eBay system, such as when a user requests deletion or revokes access for an application. An event is an instance of an event type (topic).
**Parameters:**
- **continuation_token** (string)
  - This string value can be used to return the next page in the result set. The string to use here is returned in the **next** field of the current page of results.
- **limit** (string)
  - The maximum number of notification topics to return per page from the result set.  
  
**Min:** 10  
  
**Max:** 100  
  
**Default:** 20

## Error Codes

The following error codes may be returned by this API:

### APPLICATION Errors

#### 195026 - API_NOTIFICATION
**Description:** Configuration Not Found.

#### 195000 - API_NOTIFICATION
**Description:** There was a problem with an eBay internal system or process. Contact eBay developer support for assistance.

### REQUEST Errors

#### 195025 - API_NOTIFICATION
**Description:** Invalid or missing email.

#### 195016 - API_NOTIFICATION
**Description:** Invalid name. Markups or lengths greater than 64 not supported

#### 195017 - API_NOTIFICATION
**Description:** Invalid or missing endpoint.

#### 195018 - API_NOTIFICATION
**Description:** Invalid or missing destination status. Supported values:\[ENABLED,DISABLED\]

#### 195019 - API_NOTIFICATION
**Description:** Invalid or missing verification token for this endpoint.

#### 195003 - API_NOTIFICATION
**Description:** Please provide configurations required for notifications. Refer to /config

#### 195020 - API_NOTIFICATION
**Description:** Challenge verification failed for requested endpoint

#### 195021 - API_NOTIFICATION
**Description:** Destination exists for this endpoint

#### 195022 - API_NOTIFICATION
**Description:** Invalid or missing destination id.

#### 195024 - API_NOTIFICATION
**Description:** Destination is in use and cannot be deleted.

#### 195004 - API_NOTIFICATION
**Description:** Invalid limit. Supported ranges 10 - 100.

#### 195005 - API_NOTIFICATION
**Description:** Invalid continuation token.

#### 195001 - API_NOTIFICATION
**Description:** The specified key id is invalid.

#### 195006 - API_NOTIFICATION
**Description:** Invalid or missing subscription status.

#### 195007 - API_NOTIFICATION
**Description:** Invalid or missing destination id.

#### 195008 - API_NOTIFICATION
**Description:** Invalid or missing schema version. Please refer to /topic/{topic\_id} for supported schema versions.

#### 195009 - API_NOTIFICATION
**Description:** Specified format is not supported for the topic.

#### 195010 - API_NOTIFICATION
**Description:** Invalid or missing protocol

#### 195027 - API_NOTIFICATION
**Description:** Invalid or missing topic id.

#### 195011 - API_NOTIFICATION
**Description:** Not authorized for this topic.

#### 195012 - API_NOTIFICATION
**Description:** Subscription already exists

#### 195015 - API_NOTIFICATION
**Description:** The subscription cannot be enabled since the destination is not enabled.

#### 195032 - API_NOTIFICATION
**Description:** The specified subscription topic is not filterable.

#### 195033 - API_NOTIFICATION
**Description:** The specified 'filterSchema' value is invalid.

#### 195028 - API_NOTIFICATION
**Description:** The application is not authorized to access the specified subscription.

#### 195013 - API_NOTIFICATION
**Description:** The subscription id does not exist.

#### 195031 - API_NOTIFICATION
**Description:** The specified subscription id does not match the specified filter id.

#### 195029 - API_NOTIFICATION
**Description:** Invalid subscription filter id.

#### 195014 - API_NOTIFICATION
**Description:** The subscription cannot be enabled since the topic or payload is no longer supported.

#### 195002 - API_NOTIFICATION
**Description:** Invalid or missing topic id.

## Types

### Config
**Description:** The type that defines the fields for the **alertEmail** field.
**Type:** object

**Properties:**
- **alertEmail** (string)
  - This field is used to add or modify an email address that will be used for Notification API alerts associated with the application. [getConfig](/develop/api/sell/notification_api#sell-notification_api-config-getconfig) can be used to get the email address currently being used for alerts.

### Error
**Description:** This type defines the fields that can be returned in an error.
**Type:** object

**Properties:**
- **category** (string)
  - Identifies the type of error.
- **domain** (string)
  - Name for the primary system where the error occurred. This is relevant for application errors.
- **errorId** (integer)
  - A unique number to identify the error.
- **inputRefIds** (array)
  - An array of request elements most closely associated to the error.
- **longMessage** (string)
  - A more detailed explanation of the error.
- **message** (string)
  - Information on how to correct the problem, in the end user's terms and language where applicable.
- **outputRefIds** (array)
  - An array of request elements most closely associated to the error.
- **parameters** (array)
  - An array of name/value pairs that describe details the error condition. These are useful when multiple errors are returned.
- **subdomain** (string)
  - Further helps indicate which subsystem the error is coming from. System subcategories include: Initialization, Serialization, Security, Monitoring, Rate Limiting, etc.

### ErrorParameter
**Description:** This type defines the name and value of the error.
**Type:** object

**Properties:**
- **name** (string)
  - The object of the error.
- **value** (string)
  - The value of the object.

### DeliveryConfig
**Description:** A type that contains information about the delivery configuration.
**Type:** object

**Properties:**
- **endpoint** (string)
  - The endpoint for this destination.  
  
**Note:** The provided endpoint URL should use the HTTPS protocol, and it should not contain an internal IP address or `localhost` in its path.
- **verificationToken** (string)
  - The verification token associated with this endpoint.  
  
**Note:** The provided verification token must be between 32 and 80 characters. Allowed characters include alphanumeric characters, underscores (`_`), and hyphens (`-`); no other characters are allowed.

### DestinationRequest
**Description:** A type that contains information about the destination request.
**Type:** object

**Properties:**
- **deliveryConfig** (DeliveryConfig)
  - This container is used to specify the destination endpoint and verification token associated with this endpoint.
- **name** (string)
  - The seller-specified name for the destination endpoint.
- **status** (DestinationStatusEnum)
  - This field sets the status for the destination endpoint as `ENABLED` or `DISABLED`.  
  
**Note:** The **MARKED\_DOWN** value is set by eBay systems and cannot be used in a create or update call by applications.

### DestinationStatusEnum
**Description:** An enumerated type that describes the current status of a notification destination endpoint. | - **ENABLED**: This enumeration value indicates the destination is active and can receive notifications. - **DISABLED**: This enumeration value indicates the destination exists but is turned off and will not receive notifications. - **MARKED_DOWN**: This enumeration value indicates the destination has been automatically marked down by eBay systems (e.g., due to failures) and this value cannot be set via create/update calls.
**Type:** object

### Destination
**Description:** A type that contains information about the destination.
**Type:** object

**Properties:**
- **deliveryConfig** (DeliveryConfig)
  - The configuration associated with this destination.
- **destinationId** (string)
  - The unique identifier for the destination.
- **name** (string)
  - The name associated with this destination.
- **status** (DestinationStatusEnum)
  - The status for this destination.  
  
**Note:** The `MARKED_DOWN` value is set by eBay systems and cannot be used in a create or update call by applications.  
  
**Valid values:**

*   `ENABLED`
*   `DISABLED`
*   `MARKED_DOWN`

### DestinationSearchResponse
**Description:** A type that contains information about the destination search response.
**Type:** object

**Properties:**
- **destinations** (array)
  - An array that contains the destination details.
- **href** (string)
  - The path to the call URI that produced the current page of results.
- **limit** (integer)
  - The number of records to show in the current response.  
  
**Default:** 20
- **next** (string)
  - The URL to access the next set of results. This field includes a **continuation\_token**. No **prev** field is returned, but this value is persistent during the session so that you can use it to return to the next page.  
  
This field is not returned if fewer records than specified by the **limit** field are returned.
- **total** (integer)
  - The total number of matches for the search criteria.

### PublicKey
**Description:** A type that defines the public key for a unique key ID.
**Type:** object

**Properties:**
- **algorithm** (string)
  - The algorithm associated with the public key that is returned, such as Elliptic Curve Digital Signature Algorithm (ECDSA).
- **digest** (string)
  - The digest associated with the public key that is returned, such as Secure Hash Algorithm 1 (SHA1).
- **key** (string)
  - The public key that is returned for the specified key ID.  
  
This value is used to validate the eBay push notification message payload.

### CreateSubscriptionRequest
**Description:** This type contains information about a subscription request.
**Type:** object

**Properties:**
- **destinationId** (string)
  - The unique identifier of the destination endpoint that will receive notifications associated with this subscription. Use the [getDestinations](/develop/api/sell/notification_api#sell-notification_api-destination-getdestinations) method to retrieve destination IDs.
- **payload** (SubscriptionPayloadDetail)
  - The payload associated with the notification topic. Use [getTopics](/develop/api/sell/notification_api#sell-notification_api-topic-gettopics) or [getTopic](/api-docs/commerce/notification/resources/topic/methods/getTopic) to get the supported payload for the topic.
- **status** (SubscriptionStatusEnum)
  - Set the status of the subscription to `ENABLED` or `DISABLED`.
- **topicId** (string)
  - The unique identifier of the notification topic to subscribe to. Use [getTopics](/develop/api/sell/notification_api#sell-notification_api-topic-gettopics) to get topic IDs.

### FormatTypeEnum
**Description:** An enumerated type that describes the format of the subscription's payload. | - **JSON**: Presently, only `JSON` is supported.
**Type:** object

### ProtocolEnum
**Description:** An enumerated type that defines the allowed transport protocol for payload delivery. | - **HTTPS**: Presently, `HTTPS` is the only supported format.
**Type:** object

### SubscriptionPayloadDetail
**Description:** A type that describes the details of the subscription payload.
**Type:** object

**Properties:**
- **deliveryProtocol** (ProtocolEnum)
  - The supported delivery protocol of the notification topic.  
  
**Note:** `HTTPS` is currently the only supported delivery protocol of all notification topics.
- **format** (FormatTypeEnum)
  - The supported data format of the payload.  
  
**Note:** JSON is currently the only supported format for all notification topics.
- **schemaVersion** (string)
  - The supported schema version for the notification topic. See the **supportedPayloads.schemaVersion** field for the topic in [getTopics](/develop/api/sell/notification_api#sell-notification_api-topic-gettopics) or [getTopic](/api-docs/commerce/notification/resources/topic/methods/getTopic) response.

### SubscriptionStatusEnum
**Description:** An enumerated type that describes whether a subscription is active. | - **ENABLED**: The subscription is active and eBay will send notifications for that subscription. - **DISABLED**: The subscription is turned off and no notifications will be sent for that subscription.
**Type:** object

### CreateSubscriptionFilterRequest
**Description:** This type defines the request fields for the **createSubscriptionFilter** method.
**Type:** object

**Properties:**
- **filterSchema** (object)
  - The content of a subscription filter as a valid [JSON Schema Core document](<https://json-schema.org >) (version 2020-12 or later). The **filterSchema** provided must describe the subscription's notification payload such that it supplies valid criteria to filter the subscription's notifications.  
  
**Note:** Not all topics can have filters applied to them. Use [getTopic](/api-docs/commerce/notification/resources/topic/methods/getTopic) and [getTopics](/api-docs/commerce/notification/resources/topic/methods/getTopics) requests to determine if a specific topic is filterable. Filterable topics have the boolean **filterable** returned as `true` in the response.  
**Note:** If the JSON supplied as a subscription filter specifies a field that does not exist in the notifications for a topic, or if the topic is not filterable, the filter will be rejected and become `DISABLED`. If it is valid, however, the filter will move from `PENDING` status to `ENABLED` status.  
Initially, when the **createSubscriptionFilter** request has been made, if the request has a valid JSON body a **201 Created** is returned. After that, the validation of the **filterSchema** happens.

### Subscription
**Description:** A type that describes the subscription.
**Type:** object

**Properties:**
- **creationDate** (string)
  - The creation date for this subscription.
- **destinationId** (string)
  - The unique identifier for the destination associated with this subscription.
- **filterId** (string)
  - The unique identifier for the filter associated with this subscription.
- **payload** (SubscriptionPayloadDetail)
  - The payload associated with this subscription.
- **status** (SubscriptionStatusEnum)
  - The status of this subscription.
- **subscriptionId** (string)
  - The unique identifier for the subscription.
- **topicId** (string)
  - The unique identifier for the topic associated with this subscription.

### SubscriptionFilter
**Description:** This type defines filter details for the specified subscription filter.
**Type:** object

**Properties:**
- **creationDate** (string)
  - The creation date for this subscription filter.
- **filterId** (string)
  - The unique identifier for this subscription filter.
- **filterSchema** (object)
  - The content of this subscription filter as a valid [JSON Schema Core document](<https://json-schema.org >) (version 2020-12 or later). The **filterSchema** provided must describe the subscription's notification payload such that it supplies valid criteria to filter the subscription's notifications.
- **filterStatus** (SubscriptionFilterStatus)
  - The status of this subscription filter.
- **subscriptionId** (string)
  - The unique identifier for the subscription.

### SubscriptionFilterStatus
**Description:** An enumerated type that indicates the current status of the subscription filter. | - **DISABLED**: The subscription filter exists but is currently turned off; it does not affect which notifications are sent. - **ENABLED**: The subscription filter is active and is being applied to determine which notifications are delivered. - **PENDING**: The subscription filter has been created but is not yet active (e.g., awaiting processing/activation).
**Type:** object

### SubscriptionSearchResponse
**Description:** A type that describes the details of the subscription search response.
**Type:** object

**Properties:**
- **href** (string)
  - The path to the call URI that produced the current page of results.
- **limit** (integer)
  - The value of the limit parameter submitted in the request, which is the maximum number of items to return per page, from the result set. A result set is the complete set of results returned by the method.  
  
**Note:** Though this parameter is not required to be submitted in the request, the parameter defaults to `20` if omitted.  
  
**Default:** 20
- **next** (string)
  - The URL to access the next set of results. This field includes a **continuation\_token**. No **prev** field is returned, but this value is persistent during the session so that you can use it to return to the next page.  
  
This field is not returned if fewer records than specified by the **limit** field are returned.
- **subscriptions** (array)
  - The subscriptions that match the search criteria.
- **total** (integer)
  - The total number of matches for the search criteria.

### UpdateSubscriptionRequest
**Description:** A type that describes the details of the update subscription request.
**Type:** object

**Properties:**
- **destinationId** (string)
  - The unique identifier of the destination endpoint that will receive notifications associated with this subscription. Use [getDestinations](/develop/api/sell/notification_api#sell-notification_api-destination-getdestinations) to retrieve destination IDs.
- **payload** (SubscriptionPayloadDetail)
  - The payload associated with this subscription.
- **status** (SubscriptionStatusEnum)
  - Set the status of the subscription being updated to `ENABLED` or `DISABLED`.

### ContextEnum
**Description:** An enumerated type that represents the business context of a notification. | - **BUY**: BUY - **SELL**: This value represents notifications related to seller-side use cases (listing, selling, and order handling). - **COMMERCE**: This value represents notifications that apply to broader commerce flows spanning buy/sell (e.g., account or marketplace–level events). - **DEVELOPER**: This value represents notifications aimed at developer-level concerns or tooling.
**Type:** object

### PayloadDetail
**Description:** A type that describes the details about a topic's payload.
**Type:** object

**Properties:**
- **deliveryProtocol** (ProtocolEnum)
  - The supported delivery protocols.
- **deprecated** (boolean)
  - A deprecation indicator.
- **format** (array)
  - The supported format. Presently, `JSON` is the only supported format.
- **schemaVersion** (string)
  - The supported schema version.

### ScopeEnum
**Description:** An enumerated type that indicates whether a notification topic is scoped to an application or to an individual user. | - **APPLICATION**: This enumeration value indicates the topic is subscribed to and managed at the application level. - **USER**: This enumeration value indicates the topic is subscribed to and managed per user account.
**Type:** object

### StatusEnum
**Description:** An enumerated type that represents the status of the notification topic. | - **ENABLED**: This enumeration value indicates the topic is active and can be subscribed to and used. - **DISABLED**: This enumeration value indicates the topic is turned off and not available for active use. - **DEPRECATED**: This enumeration value indicates the topic is deprecated and will be removed or replaced.
**Type:** object

### Topic
**Description:** A type that describes the details of the topic.
**Type:** object

**Properties:**
- **authorizationScopes** (array)
  - The authorization scopes required to subscribe to this topic.
- **context** (ContextEnum)
  - The business context associated with this topic.
- **description** (string)
  - The description of the topic.
- **filterable** (boolean)
  - The indicator of whether this topic is filterable or not.
- **scope** (ScopeEnum)
  - The scope of this topic.
- **status** (StatusEnum)
  - The status of this topic.
- **supportedPayloads** (array)
  - The supported payloads for this topic.
- **topicId** (string)
  - The unique identifier for the topic.

### TopicSearchResponse
**Description:** A type that describes the details of the topic search response.
**Type:** object

**Properties:**
- **href** (string)
  - The path to the call URI that produced the current page of results.
- **limit** (integer)
  - The value of the limit parameter submitted in the request, which is the maximum number of items to return per page, from the result set. A result set is the complete set of results returned by the method.  
  
**Note:** Though this parameter is not required to be submitted in the request, the parameter defaults to `20` if omitted.
- **next** (string)
  - The URL to access the next set of results. This field includes a **continuation\_token**. No **prev** field is returned, but this value is persistent during the session so that you can use it to return to the next page.  
  
This field is not returned if fewer records than specified by the **limit** field are returned.
- **topics** (array)
  - An array of topics that match the specified criteria.
- **total** (integer)
  - The total number of matches for the search criteria.

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
*Generated on 2026-09-02T16:51:04.439Z*