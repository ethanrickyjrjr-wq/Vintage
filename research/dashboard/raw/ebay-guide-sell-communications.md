# Sell Communications Guide

**Guide Group:** Communications

---

## Overview

The eBay Sell Communication APIs include functionality that allows sellers to retrieve business-critical notifications from eBay, send discounted offers to prospective buyers that are watching their items, interact with buyers and potential customers and answer their inquiries, and programmatically manage their eBay InBox messages and folders.

## API use cases

[Subscribing to and retrieving eBay notifications](#retrievingeBaynotifications)  
[Sending discounted offers to interested buyers](#offersinterestedbuyers)  
[Managing buyer/seller communications](#buyersellercommunications)  
[Handling feedback](#handlingfeedback)

#### Subscribing to and retrieving eBay notifications

Integrating with eBay's Notification API allows third-party platforms to subscribe to and receive various types of notifications that eBay will send to the user's destination endpoint. For the complete list of supported Sell notification events, see [Sell notification events](/develop/api/sell/notification_events).

The following steps will allow you to start receiving these notifications to your configured endpoint:

[Prepare to receive notifications](#prepare)  
[Subscribe to a notification topic](#subscribe)  
[Create a subscription filter for a topic](#filter)  
[Verify the validity of a notification](#verify)

##### Prepare to receive notifications

The following must be completed before users can subscribe to notification topics: 

###### Create an alert config

Before an endpoint destination can be set up to receive notifications, an alert configuration must first be created. The [updateConfig](/develop/api/commerce/notification_api/config/updateConfig) method allows users to create a new alert configuration (or update an existing configuration) and specify an alert email for their application.

**Note:** If an alert configuration has already been created, the [getConfig](/develop/api/commerce/notification_api/config/getConfig) method can be used to retrieve and verify the existing configuration data.

###### Create an endpoint destination

Before being able to subscribe to and receive eBay notifications, users must prepare their endpoint destinations to receive a challenge code from eBay, and then use this challenge code to validate the legitimacy of the endpoint URL. eBay needs to verify that the user owns/has access to the provided endpoint URL. 

To do so: 

1.  The [createDestination](/develop/api/sell/notification_api/destination/createDestination) method can be used to create and specify the destination endpoint and verification token. Immediately after the developer provides and saves an endpoint URL and a verification token, eBay will send a challenge code to that URL in the form of a GET call. This GET call will use this format:
    
    GET https://<callback\_URL>?challenge\_code=123
    
    **Note:** The **challenge\_code** query parameter value will be unique for the request. The provided endpoint URL should use the HTTPS protocol, and it should not contain an internal IP address or localhost in its path.
    
2.  Upon receiving this unique challenge code, the endpoint must be set up to hash together the challenge code, verification token, and endpoint URL, and then reply back to eBay with a **200 OK** and the hashed value through a **challengeResponse** field in JSON format:  
    
    {
    "challengeResponse":"52161ff4651cb71888801b47bae62f44d7f6d0aab17e70d00f64fc84368ca38f"
    }
    
    **Important:** The **content-type** header for this response must be set to application/json and the three parameters must be hashed in the following order, or the verification will fail: `challengeCode + verificationToken + endpoint`
    
    eBay will verify the hexadecimal string before the endpoint can be officially subscribed to notifications. The endpoint and verification token are values specific to the destination, but the challenge code variable will come from eBay in the form of the **challenge\_code** query parameter, which is randomly generated and unique to the request.
    
    **Note:** The verification token must be between 32 and 80 characters. Allowed characters include alphanumeric characters, underscores (\_), and hyphens (-); no other characters are allowed.
    
    Code snippets in Node.js, Java, Python, and PHP for computing the challenge response are provided below:
    
    _Node.js_
    
    ```
    const hash = createHash('sha256');
    hash.update(challengeCode);
    hash.update(verificationToken);
    hash.update(endpoint);
    const responseHash = hash.digest('hex');
    console.log(new Buffer.from(responseHash).toString());
    ```
    
    _Java_
    
    ```
    MessageDigest digest = MessageDigest.getInstance("SHA-256");
    digest.update(challengeCode.getBytes(StandardCharsets.UTF_8));
    digest.update(verificationToken.getBytes(StandardCharsets.UTF_8));
    byte[] bytes = digest.digest(endpoint.getBytes(StandardCharsets.UTF_8));
    System.out.println(org.apache.commons.codec.binary.Hex.encodeHexString(bytes));
    ```
    
    _Python  
    _
    
    ```
    m = hashlib.sha256(challengeCode+verificationToken+endpoint);
    print(m.hexdigest());
    ```
    
    _PHP  
    _
    
    ```
    $hash = hash_init('sha256');
    hash_update($hash, $challengeCode);
    hash_update($hash, $verificationToken);
    hash_update($hash, $endpoint);
    $responseHash = hash_final($hash);
    echo $responseHash;
    ```
    
3.  Once you have tested your code and endpoint and feel confident that the endpoint is ready to process and reply back to eBay's challenge code, you can proceed to subscribing to the eBay notifications.

##### Subscribe to a notification topic

After users have tested their code and destination endpoint, and feel confident that the endpoint is ready to process and reply back to eBay's challenge code, a subscription to an eBay  notification topic can be established.

Use [createSubscription](/develop/api/sell/notification_api/subscription/createSubscription) to subscribe to a topic. Information such as the [topicId](/develop/api/sell/notification_api/subscription/createSubscription#request.topicId) value for the topic, the endpoint that will receive these notifications, and set the [status](/develop/api/sell/notification_api/subscription/createSubscription#request.status) will be required. Use [getTopics](/develop/api/commerce/notification_api/topic/getTopics) to retrieve the full list of notification topics available and their topic ID values. 

When creating a new subscription, it is important to include the appropriate scopes for the type of subscription: 

*   **For application-based subscriptions**, the following scope must be included and the OAuth token must be created using the client credentials grant flow: `https://api.ebay.com/oauth/api_scope`
*   **For user-based subscriptions**, the following scope must be included and the OAuth token must be created using the authorization code grant flow: `https://api.ebay.com/oauth/api_scope/commerce.notification.subscription`

##### Create as a subscription filter for a topic

Once a user has created an endpoint destination and subscribed to a notification topic, a subscription filter can be added to the subscription that allows applications to only receive notifications that match the provided criteria; notifications that do not match will not be sent to the destination.

**Note:** Not all topics are able to have filters applied to them. Use the [getTopic](/develop/api/commerce/notification_api/subscription/getTopic) and [getTopics](/develop/api/commerce/notification_api/topic/getTopics) requests to determine if the selected topic is filterable. Filterable topics have the boolean **filterable** set to `true` in the response.

The [createSubscriptionFilter](/develop/api/sell/notification_api) method is used to create a subscription filter. Make sure the subscription filter adheres to the following:

*   A filter request must be for an enabled subscription owned by the user
*   The subscription must be to a topic that is filterable. Use the [getTopic](/develop/api/commerce/notification_api/subscription/getTopic) and [getTopics](/develop/api/commerce/notification_api/topic/getTopics) requests to determine if the selected topic is filterable. Filterable topics are indicated with the boolean **filterable** set to `true` in the response.  If the topic is not filterable, the filter will be rejected, become `DISABLED`, and return a 195032 error code
*   The **filterSchema** value provided must be a valid [JSON Core document](https://json-schema.org/) (version 2020-12 or later) and must describe the subscription's notification payload such that it supplies valid criteria to filter the subscription's notifications. If the supplied JSON specifies a field that does not exist in the notifications for a topic, the filter will be rejected, become `DISABLED`, and return a 195033 error code

Initially, when the [createSubscriptionFilter](/develop/api/sell/notification_api) request has been made, if the request has a valid JSON body, a **201 Created** is returned and the filter will be in `PENDING` state while it undergoes review. If the filter is approved, it will move from the `PENDING` status to the `ENABLED` status. You can find the status of a filter using the [getSubscriptionFilter](/develop/api/sell/notification_api#sell-notification_api-subscription-getsubscriptionfilter) method

##### Verify the validity of a notification

After the notification payload and header are received, users should verify that the notification actually came from eBay. 

For every notification sent to the endpoint, extract the Base64-encoded **X-EBAY-SIGNATURE** header included in the eBay notification. Pass this value as a path parameter in the [getPublicKey](/develop/api/sell/notification_api#sell-notification_api-public_key-getpublickey) method. The key value returned in the response is used to validate the eBay push notification message payload.

Notifications can also be validated using the Event Notification SDKs listed in the **Best practices** section of this guide. 

Below are some of the other supporting methods of the Notification API:

*   The destination resource has the following additional methods available:
    *   Use [getDestination](https://developer.ebay.com/api-docs/commerce/notification/resources/destination/methods/getDestination) to retrieve details about one specific destination endpoint.
    *   Use [getDestinations](https://developer.ebay.com/api-docs/commerce/notification/resources/destination/methods/getDestinations) to retrieve all configured destination endpoints.
    *   Use [updateDestination](https://developer.ebay.com/api-docs/commerce/notification/resources/destination/methods/updateDestination) to make updates to a destination endpoint.
    *   Use [deleteDestination](https://developer.ebay.com/api-docs/commerce/notification/resources/destination/methods/deleteDestination) to delete a disabled destination endpoint.
*   The subscription resource has the following additional methods available:
    *   Use [getSubscriptions](https://developer.ebay.com/api-docs/commerce/notification/resources/subscription/methods/getSubscriptions) to obtain details about all notification topic subscriptions. Use [updateSubscription](https://developer.ebay.com/api-docs/commerce/notification/resources/subscription/methods/updateSubscription) to modify an existing subscription.
    *   Use [enableSubscription](https://developer.ebay.com/api-docs/commerce/notification/resources/subscription/methods/enableSubscription) to enable previously disabled topic subscriptions and use [disableSubscription](https://developer.ebay.com/api-docs/commerce/notification/resources/subscription/methods/disableSubscription) to disable active topic subscriptions.
    *   Use [testSubscription](https://developer.ebay.com/api-docs/commerce/notification/resources/subscription/methods/testSubscription) to send a test notification and verify the subscription's functionality.
    *   Use [deleteSubscription](https://developer.ebay.com/api-docs/commerce/notification/resources/subscription/methods/deleteSubscription) to remove a subscription, stopping notification delivery for that topic.
    *   Use [getSubscriptionFilter](https://developer.ebay.com/api-docs/commerce/notification/resources/subscription/methods/getSubscriptionFilter) to access detailed information about a particular filter, such as its criteria, status, and creation date.
    *   Use [deleteSubscriptionFilter](https://developer.ebay.com/api-docs/commerce/notification/resources/subscription/methods/deleteSubscriptionFilter) to deactivate and remove an active filter, enabling the creation of a new filter with revised criteria.

##### Subscribing to Platform Notification events

Integrating with eBay's Trading API enables users to subscribe to and manage various platform notifications triggered by specific eBay events. Below are some of the key buyer-focused or buyer/seller event types and their purpose:

*   **BestOfferDeclined:** This buyer-facing notification is sent when a seller declines the buyer's Best Offer on an item.
*   **BestOfferPlaced:** This buyer-facing notification is sent each time a prospective buyer places a Best Offer on an item.
*   **BidItemEndingSoon:** This notification is sent to a subscribed buyer when the auction item where the buyer has an active bid is about to end.
*   **BidPlaced:** This buyer-facing notification is sent when the buyer places a bid for an auction item.
*   **CounterOfferReceived:** This buyer-facing notification is sent when a seller makes a counteroffer to the buyer's Best Offer on an item.
*   **Feedback:** This notification is applicable to both buyers and sellers and is sent when the user has left feedback for, or received feedback from, the other party in the order.
*   **FeedbackLeft:** This notification is applicable to both buyers and sellers and is sent when the user leaves feedback for an order partner.
*   **FeedbackReceived:** This notification is applicable to both buyers and sellers and is sent when the user receives feedback from an order partner.
*   **FeedbackStarChanged:** This notification is applicable to both buyers and sellers and is sent when the user's feedback star level changes.
*   **ItemAddedToWatchList:** This buyer-facing notification is sent when the buyer adds an item to the Watch List.
*   **ItemLost:** This buyer-facing notification is sent if the buyer did not end up as the highest bidder for an auction item.
*   **ItemMarkedPaid:** This notification is sent to a subscribed buyer and seller when the seller has marked an order as paid.
*   **ItemMarkedShipped:** This notification is sent to a subscribed buyer and seller when the seller has marked an item as shipped.
*   **ItemReadyForPickup:** This notification is sent to a subscribed buyer when an In-Store Pickup or Click and Collect order is ready to be picked up.
*   **ItemRemovedFromWatchList:** This buyer-facing notification is sent when the buyer removes an item from the Watch List.
*   **ItemWon:** This buyer-facing notification is sent if the buyer is the winner of an auction item.
*   **MyMessageseBayMessage:** This notification is sent to a subscribed buyer or seller when eBay sends a message to that user's InBox.
*   **MyMessagesM2MMessage:** This notification is sent to a subscribed buyer or seller when another eBay user sends a message to that user's InBox.
*   **OutBid:** This buyer-facing notification is sent when another buyer has outbid the subscribed buyer on an auction listing.
*   **PaymentReminder:** This notification is sent to a subscribed buyer if payment is still due for an order.
*   **ReturnCreated:** This notification is applicable to both buyers and sellers and is sent when a return request involving those users is created.
*   **ReturnClosed:** This notification is applicable to both buyers and sellers and is sent when a return request is closed.
*   **ReturnShipped:** This notification is applicable to both buyers and sellers and is sent when the buyer has shipped a return item back to the seller.
*   **ShoppingCartItemEndingSoon:** This notification is sent to a subscribed buyer when an item in the buyer's shopping cart is about to end.
*   **WatchedItemEndingSoon:** This buyer-facing notification is sent when a listing that the buyer is watching is ending soon.

For a complete list of available notification event types, refer to [NotificationEventTypeCodeType](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/types/NotificationEventTypeCodeType.html). Detailed information about these event types is available in the [Platform Notifications](https://developer.ebay.com/Devzone/XML/docs/HowTo/PlatformNotifications.html) guide.

The Trading API has the following calls to subscribe to and manage platform notifications:

*   Use the [SetNotificationPreferences](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/SetNotificationPreferences.html) call to subscribe to specific notification event types. Define the destination for these notifications, such as an email address or a URL endpoint.
*   Use the [GetNotificationPreferences](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GetNotificationPreferences.html) call to retrieve your current notification preferences. This enables you to confirm the event types you are subscribed to and review your notification delivery settings.
*   Use the [GetNotificationsUsage](https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GetNotificationsUsage.html) call to access details about the notifications that have been sent to you. Reviewing this information allows you to evaluate whether your notification setup is working as intended and determine if any adjustments are needed.

#### Sending discounted offers to interested buyers

The **Negotiation API** is used to help sellers identify items eligible for special offers and engage potential buyers by sending them discounted offers. By targeting buyers who have shown interest in specific listings, sellers can enhance their chances of closing sales.

*   Use [findEligibleItems](/api-docs/sell/negotiation/resources/offer/methods/findEligibleItems) to pinpoint listings that are eligible for seller-initiated offers.
*   Use [sendOfferToInterestedBuyers](/api-docs/sell/negotiation/resources/offer/methods/sendOfferToInterestedBuyers) to present discounted offers to buyers who have expressed interest in these eligible listings.

#### Managing buyer/seller communications

**Managing communications using the Message API**

The [Message API](/api-docs/commerce/message/overview.html) allows users to send messages, retrieve conversations, and modify the status of conversations.

**Sending a message:**

The [sendMessage](/api-docs/commerce/message/resources/conversation/methods/sendMessage) method can be used to start a conversation with another user, or send a message in an existing conversation.

When sending a message through the [sendMessage](/api-docs/commerce/message/resources/conversation/methods/sendMessage) method, the [messageText](/api-docs/commerce/message/resources/conversation/methods/sendMessage#request.messageText) field is required to specify the content of the message. One of the following fields is also required to specify whether the message is being sent in an existing conversation or to start a new conversation:

*   [conversationId](/api-docs/commerce/message/resources/conversation/methods/sendMessage#request.conversationId)**:** The identifier of the existing conversation for which to send the message. This field is required if sending a message in an existing conversation. This ID can be retrieved using the [getConversations](/api-docs/commerce/message/resources/conversation/methods/getConversations) method.
*   [otherPartyUsername](/api-docs/commerce/message/resources/conversation/methods/sendMessage#request.otherPartyUsername)**:** The eBay username of the intended recipient of the message. This field is required if starting a new conversation with another eBay user.

Additionally, optional information can be attached to a message through the following containers:

*   [messageMedia](/api-docs/commerce/message/resources/conversation/methods/sendMessage#request.messageMedia): This container can be used to attach media files to a message. Up to five forms of media can be sent per message. The following types of media can be attached to a message:
    *   `IMAGE`
        
        **Note:** See [Managing images](/api-docs/sell/static/inventory/managing-image-media.html#image-requiremen) for details on image requirements.
        
    *   `PDF`
    *   `DOC`
    *   `TXT`
*   [reference](/api-docs/commerce/message/resources/conversation/methods/sendMessage#request.reference): This container can be used to specify that a message is referencing a specific eBay listing. The type of reference can be specified through the [referenceType](/api-docs/commerce/message/resources/conversation/methods/sendMessage#request.reference.referenceType) field, while the identifier of the reference can be specified through the [referenceID](/api-docs/commerce/message/resources/conversation/methods/sendMessage#request.reference.referenceId) field. Currently, only listings are supported, so the [referenceType](/api-docs/commerce/message/resources/conversation/methods/sendMessage#request.reference.referenceType) will always be `LISTING`, and the [referenceID](/api-docs/commerce/message/resources/conversation/methods/sendMessage#request.reference.referenceId) will be the item ID value of the listing.

A successful call sends the message based on the provided information, and returns details about the message such as its creation date and message ID value.

**Updating a conversation:**

The [updateConversation](/api-docs/commerce/message/resources/conversation/methods/updateConversation) and [bulkUpdateConversation](/api-docs/commerce/message/resources/conversation/methods/bulkUpdateConversation) methods can be used to update the status of one or more conversations. This includes the conversation status, such as if it is active, archived, or deleted, as well as the read status, such as if it has been marked as read or unread.

When updating a conversation through these methods, the following fields are required in the request payload to specify the conversation or conversations being updated:

*   [conversationId](/api-docs/commerce/message/resources/conversation/methods/updateConversation#request.conversationId)**:** The unique identifier of the conversation that is to be updated. The [getConversations](/api-docs/commerce/message/resources/conversation/methods/getConversations) method can be used to retrieve this value.
*   [conversationType](/api-docs/commerce/message/resources/conversation/methods/updateConversation#request.conversationType): The existing conversation type of the conversation being updated. This value cannot be updated through this method, but is required as part of the request payload. The following string values are supported:
    *   `FROM_MEMBERS`: This string value indicates that the conversation is with another eBay member, such as a buyer or seller.
    *   `FROM_EBAY`: This string value indicates that the conversation is with eBay itself.

Once the conversation ID and type are specified, the status of the specified conversation or conversations can then be updated. Using these methods, either the conversation status or read status of a conversation can be changed.

**Important:** Only the conversation status or read status of a conversation can be changed at a time per call.

The following fields can be used to update the status of a conversation:

*   [conversationStatus](/api-docs/commerce/message/resources/conversation/methods/updateConversation#request.conversationStatus)**:** The status for which to update the specified conversation. The following string values are supported:
    *   `ACTIVE`: This string value updates the conversation to `ACTIVE` status, meaning that it is a currently active conversation with an eBay member or eBay itself.
    *   `ARCHIVE`: This string value updates the conversation to `ARCHIVE` status, meaning that it will be archived, but not deleted. Archived conversations are stored and can be moved back to `ACTIVE` status using this method if needed.
    *   `DELETE`: This string value updates the conversation to `DELETE` status, meaning that it will be deleted. Deleted conversations cannot be recovered.
    *   `READ`: This string value updates the conversation to `READ` status, meaning that it will be shown as being read by the recipient. Note that there is a separate [read](/api-docs/commerce/message/resources/conversation/methods/updateConversation#request.read) boolean field in the [updateConversation](/api-docs/commerce/message/resources/conversation/methods/updateConversation#request.conversationStatus) method that takes care of this function.
    *   `UNREAD`: This string value updates the conversation to `UNREAD` status, meaning that it will be shown as unread by the recipient. Note that there is a separate [read](/api-docs/commerce/message/resources/conversation/methods/updateConversation#request.read) boolean field in the [updateConversation](/api-docs/commerce/message/resources/conversation/methods/updateConversation#request.conversationStatus) method that takes care of this function.

A successful call will update the status of the conversation or conversations to the specified status.

**Retrieving conversations:**

The [getConversation](/api-docs/commerce/message/resources/conversation/methods/getConversation) and [getConversations](/api-docs/commerce/message/resources/conversation/methods/getConversations) methods can be used to retrieve messages within one or more conversations.

The [getConversation](/api-docs/commerce/message/resources/conversation/methods/getConversation) method can be used to retrieve messages within a specified conversation. The conversation from which to retrieve messages is specified by its [conversation\_id](/api-docs/commerce/message/resources/conversation/methods/getConversation#uri.conversation_id) value. The type of the conversation must be also specified through the [conversation\_type](/api-docs/commerce/message/resources/conversation/methods/getConversation#uri.conversation_type) query parameter. If the call is successful, details about each message within the specified conversation that meet the specified filter criteria will be returned. This can include information such as the message text and ID, its read status, and the usernames of the sender and recipient.

Alternatively, the [getConversations](/api-docs/commerce/message/resources/conversation/methods/getConversations) method can be used to retrieve up to 10 conversations. The following query parameters are available to refine your conversation search:

*   [conversationStatus](/api-docs/commerce/message/resources/conversation/methods/getConversations#uri.conversation_status)**:** The status of the conversations being retrieved. Only conversations in the specified status will be retrieved. The following values are supported:
    *   `ACTIVE`: The conversation is currently active and has not been archived or deleted.
    *   `ARCHIVED`: The conversation has been archived, and can still be referenced or moved back to active status if needed.
    *   `DELETED`: The conversation has been deleted and can no longer be accessed.
    *   `READ`: The most recent message in the conversation has been read by the recipient.
    *   `UNREAD`: The most recent message in the conversation has not yet been read by the recipient.
*   [conversation\_type](/api-docs/commerce/message/resources/conversation/methods/getConversations#uri.conversation_type)**:** The type of conversations being retrieved. Only conversations of the specified type will be returned. The following values are supported:
    *   `FROM_EBAY`: The conversation is from eBay.
    *   `FROM_MEMBERS`: The conversation is with an eBay member.
*   [reference\_id](/api-docs/commerce/message/resources/conversation/methods/getConversations#uri.reference_id)**:** The unique identifier of the reference, such as the item ID value, associated with the conversation. Only conversations referencing the specified value will be returned.
*   [reference\_type](/api-docs/commerce/message/resources/conversation/methods/getConversations#uri.reference_type)**:** The type of reference, if any, associated with a conversation. For example, a value of `LISTING` specifies that the conversation is associated with a specific listing specified by the corresponding [reference\_id](/api-docs/commerce/message/resources/conversation/methods/getConversations#uri.reference_id) value. Currently, only `LISTING` is supported.
*   [start\_time](/api-docs/commerce/message/resources/conversation/methods/getConversations#uri.start_time) and [end\_time](/api-docs/commerce/message/resources/conversation/methods/getConversations#uri.end_time)**:** Only conversations sent between this time period will be returned.
*   [other\_party\_username](/api-docs/commerce/message/resources/conversation/methods/getConversations#uri.other_party_username)**:** The user name of an eBay user for which to retrieve conversations. Only conversations with this specified user will be returned.

The following pagination parameters are available to control the amount of data returned in the response payload:

*   [limit](/api-docs/commerce/message/resources/conversation/methods/getConversations#uri.limit)**:** Specifies the number of items from the result set returned on a single page.
*   [offset](/api-docs/commerce/message/resources/conversation/methods/getConversations#uri.offset)**:** Specifies the number of items to skip in the result set.

**Managing communications using the Trading API**

Facilitating effective communication between buyers and sellers is crucial for smooth transactions on eBay. This use case outlines the methods available to enable message exchanges between buyer and seller, and to retrieve and manage eBay InBox messages and folders.

The API calls for managing buyer/seller communications are discussed below:

*   Use [AddMemberMessageAAQToPartner](/Devzone/XML/docs/Reference/eBay/AddMemberMessageAAQToPartner.html) to enable a buyer and a seller in an order relationship to send messages to each other's My Messages Inboxes, fostering direct communication.
*   Use [AddMemberMessageRTQ](/Devzone/XML/docs/Reference/eBay/AddMemberMessageRTQ.html) to allow a seller to reply to a buyer's question about an active item listing, ensuring prompt responses to inquiries.
*   Use [AddMemberMessagesAAQToBidder](/Devzone/XML/docs/Reference/eBay/AddMemberMessagesAAQToBidder.html) to enable a seller to send up to 10 messages to bidders or users who have made offers via Best Offer, regarding an active item listing, facilitating communication with potential buyers.
*   Use [GetUserContactDetails](/Devzone/XML/docs/Reference/eBay/GetUserContactDetails.html) to return contact information for a specified user, provided there is a bidding relationship, as either a buyer or seller, between the caller and the user, aiding in direct communication when necessary.

The API calls for retrieving and managing eBay InBox messages and folders are discussed below:

*   Use [GetMyMessages](/Devzone/XML/docs/Reference/eBay/GetMyMessages.html) to retrieve information about the messages sent to a user, providing an overview of all communications received. This call has multiple filters available to control which messages are returned, including date range filters, message folder IDs, or message IDs.
*   Use [GetMemberMessages](/Devzone/XML/docs/Reference/eBay/GetMemberMessages.html) to retrieve a list of messages buyers have posted about your active item listings, allowing sellers to address buyer inquiries and concerns.
*   Use [GetMessagePreferences](/Devzone/XML/docs/Reference/eBay/GetMessagePreferences.html) to return a seller's Ask Seller a Question subjects, each in its own **Subject** field, enabling sellers to view their current message preferences.
*   Use [SetMessagePreferences](/Devzone/XML/docs/Reference/eBay/SetMessagePreferences.html) to enable a seller to add, remove, or modify custom Ask Seller a Question subjects, or to reset any custom subjects to their default values.
*   Use [ReviseMyMessages](/Devzone/XML/docs/Reference/eBay/ReviseMyMessages.html) to mark messages as Read, to flag or unflag messages, and/or to move all specified messages into a different InBox folder.
*   Use [ReviseMyMessagesFolders](/Devzone/XML/docs/Reference/eBay/ReviseMyMessagesFolders.html) to create a new folder, rename an existing folder, or delete an empty folder.
*   Use [DeleteMyMessages](/Devzone/XML/docs/Reference/eBay/DeleteMyMessages.html) to delete selected messages for a given user.

#### Handling feedback

Effective feedback management builds transparency and trust between buyers and sellers on eBay. This use case explains how to retrieve, leave, and respond to feedback to keep transactions smooth, resolve issues, and maintain a positive reputation. You can use the [Feedback API](#feedback-thru-feedback-api) REST API, or the [Trading API](#feedback-thru-trading-api) legacy API to handle feedback.

##### Using the Feedback API

The **Feedback API** manages transaction feedback through the methods contained in the following table.

Method

Description

[getItemsAwaitingFeedback](/api-docs/commerce/feedback/resources/awaiting_feedback/methods/getItemsAwaitingFeedback)

Retrieves a filtered list of line items for which feedback is pending from the user based on their role.

[getFeedback](/api-docs/commerce/feedback/resources/feedback/methods/getFeedback)

Retrieves a filtered list of line items for which feedback is available from the user based on their role. This method also retrieves detailed metrics for sellers.

[leaveFeedback](/api-docs/commerce/feedback/resources/feedback/methods/leaveFeedback)

Submits feedback associated with a line item for an order partner, generating a unique ID for tracking and reference purposes.

[respondToFeedback](/api-docs/commerce/feedback/resources/respond_to_feedback/methods/respondToFeedback)

Responds to feedback provided by the order partner on a specific line item in an order.

[getFeedbackRatingSummary](/api-docs/commerce/feedback/resources/feedback_rating_summary/methods/getFeedbackRatingSummary)

Returns a categorized summary of feedback metrics for an eBay seller, filtered by criteria.

The following scenarios describe key uses:

*   **Get items awaiting feedback**  
    
    To retrieve a list of items that still require feedback, whether acting as buyer or seller, call the [getItemsAwaitingFeedback](/api-docs/commerce/feedback/resources/awaiting_feedback/methods/getItemsAwaitingFeedback) method.
    
*   **Retrieve feedback**  
    
    Use the [getFeedback](/api-docs/commerce/feedback/resources/feedback/methods/getFeedback) method to gather feedback for a specified user, with filtering options based on transaction, item, comment type, [AI-filtered](#retrieve-ai-filtered-items) topics, or feedback containing photos. This method also retrieves detailed metrics for sellers. With this in mind, this method supports various feedback retrieval scenarios:
    
    *   All feedback for a user
    *   Feedback received by the user
    *   Feedback left by the user
    *   Specific feedback entries
    *   Feedback on a particular listing or line item
    *   Feedback of a specific type
    *   Feedback for the user acting as either a seller or a buyer
*   **Retrieve AI-filtered feedback**  
    
    You can specify a topic and have AI generate any associated applicable feedback items through the [getFeedback](/api-docs/commerce/feedback/resources/feedback/methods/getFeedback) method. Specify the topic and then only feedback for those listings are returned. For example, to have AI generate and return the last 30 days of positive feedback items associated with shipping as a seller, use: `filter=commentType:POSITIVE,topics:shipping,period:30,role:SELLER`  
    See the topics value in the filter query parameter for specific topics available.
    
*   **Leave feedback**  
    
    Buyers and sellers submit feedback for completed line items by calling the [leaveFeedback](/api-docs/commerce/feedback/resources/feedback/methods/leaveFeedback) method.
    
*   **Get feedback rating summary**  
    
    To return aggregated feedback metrics for review, call the [getFeedbackRatingSummary](/api-docs/commerce/feedback/resources/feedback_rating_summary/methods/getFeedbackRatingSummary) method. These ratings are only for sellers and can return metrics like on time delivery, shipping costs, and communication.
    
*   **Respond to feedback received**  
    
    Buyers and sellers can reply to feedback left by their order partner by calling the [respondToFeedback](/api-docs/commerce/feedback/resources/respond_to_feedback/methods/respondToFeedback) method.
    
*   **Using rating templates**  
    
    Rating templates, if used, define the feedback rating options available for transactions, covering key aspects like on-time delivery and overall experience, two examples of detailed seller ratings, and open comments. Detailed seller ratings are only applicable when buyers leave feedback for sellers. Each rating specifies the label presented to users, whether the field is required, the enabled status, and the format of accepted input, such as predefined choices, range, or free text. Call the [getItemsAwaitingFeedback](/api-docs/commerce/feedback/resources/awaiting_feedback/methods/getItemsAwaitingFeedback) method to return any available rating templates. See the following for examples of rating templates returned.
    
    _PREDEFINED yes/no rating type for ON\_TIME\_DELIVERY_
    
    {
      "ratingKey": "ON\_TIME\_DELIVERY",
      "ratingLabel": "Did this item arrive on time?",
      "required": false,
      "ratingValueType": "PREDEFINED",
      "enabled": true,
      "acceptableValues": \[
        {
          "value": "2",
          "valueLabel": "Yes",
          "enabled": true
        },
        {
          "value": "3",
          "valueLabel": "No",
          "enabled": true
        }
      \]
    }
    
    _PREDEFINED with positive, neutral, and negative feedback for OVERALL\_EXPERIENCE_
    
    {
      "ratingKey": "OVERALL\_EXPERIENCE",
      "ratingLabel": "How was your experience?",
      "required": true,
      "ratingValueType": "PREDEFINED",
      "enabled": true,
      "acceptableValues": \[
        {
          "value": "POSITIVE",
          "valueLabel": "Positive",
          "enabled": true
        },
        {
          "value": "NEUTRAL",
          "valueLabel": "Neutral",
          "enabled": true
        },
        {
          "value": "NEGATIVE",
          "valueLabel": "Negative",
          "enabled": true
        }
      \]
    }
    
    _Freetext rating type for OVERALL\_EXPERIENCE\_COMMENT_
    
    {
      "ratingKey": "OVERALL\_EXPERIENCE\_COMMENT",
      "ratingLabel": "What else would you add?",
      "maximumCharactersAllowed": 500,
      "required": true,
      "ratingValueType": "FREETEXT",
      "enabled": true
    }
    
    _RANGE rating type that takes values between 1 and 5 for DSR\_ITEM\_AS\_DESCRIBED_
    
    {
      "ratingKey": "DSR\_ITEM\_AS\_DESCRIBED",
      "ratingLabel": "Item description",
      "required": false,
      "ratingValueType": "RANGE",
      "enabled": true,
      "acceptableValues": \[
        {
          "value": "1",
          "valueLabel": "Very inaccurate",
          "enabled": true
        },
        {
          "value": "2",
          "valueLabel": "Inaccurate",
          "enabled": true
        },
        {
          "value": "3",
          "valueLabel": "Neither inaccurate nor accurate",
          "enabled": true
        },
        {
          "value": "4",
          "valueLabel": "Accurate",
          "enabled": true
        },
        {
          "value": "5",
          "valueLabel": "Very accurate",
          "enabled": true
        }
      \]
    }
    

##### Using the Trading API to manage feedback

The following API calls manage transaction feedback through the **Trading API**:

*   A seller can use [GetFeedback](/Devzone/XML/docs/Reference/eBay/GetFeedback.html) to retrieve Feedback entries they received from a buyer or Feedback entries they left for a buyer. This call also retrieves detailed Feedback ratings and metrics for the seller.
*   The [GetItemsAwaitingFeedback](/Devzone/XML/docs/Reference/eBay/GetItemsAwaitingFeedback.html) call will return all sales transactions where the seller has yet to leave Feedback for the buyer.
*   A seller uses [LeaveFeedback](/Devzone/XML/docs/Reference/eBay/LeaveFeedback.html) to provide Feedback to the buyer for a specific sales transaction.
*   Use [RespondToFeedback](/Devzone/XML/docs/Reference/eBay/RespondToFeedback.html) to address feedback or include follow-up remarks. This allows sellers to clarify any issues or express appreciation, further enhancing buyer-seller relationships.

## Code samples

## Error handling

*   If [createDestination](/api-docs/sell/notification/resources/destination/methods/createDestination) or [updateDestination](/api-docs/sell/notification/resources/destination/methods/updateDestination) fails with an invalid endpoint error, check to make sure your endpoint uses the HTTPS protocol, and does not contain an internal IP address or _localhost_ in its path.
*   If [createDestination](/api-docs/sell/notification/resources/destination/methods/createDestination) or [updateDestination](/api-docs/sell/notification/resources/destination/methods/updateDestination) fails with an invalid verification error, check to make sure the token is 32 to 80 characters in length, and only contains alphanumeric characters, underscores (\_), and hyphens (-).
*   If [createSubscription](/api-docs/sell/notification/resources/subscription/methods/createSubscription) fails due to an invalid [topicId](/api-docs/sell/notification/resources/subscription/methods/createSubscription#request.topicId), use [getTopics](/api-docs/commerce/notification/resources/topic/methods/getTopics) to retrieve the correct ID, and ensure the destination endpoint is correctly configured and enabled to receive notifications.
*   If you encounter an error retrieving the public key, confirm the Base64-encoded X-EBAY-SIGNATURE header is correctly extracted and passed as a parameter, and validate the signature against the payload to ensure data integrity.

## Best practices

*   Regularly use [getSubscriptions](/api-docs/sell/notification/resources/subscription/methods/getSubscriptions) to audit and manage your active subscriptions, ensuring they align with your current notification needs.
*   Use [createSubscriptionFilter](/api-docs/sell/notification/resources/subscription/methods/createSubscriptionFilter) to refine notifications based on specific criteria, reducing unnecessary data processing.
*   Periodically review all configured endpoints with [getDestinations](/api-docs/sell/notification/resources/destination/methods/getDestinations) to ensure they are up-to-date and secure.
*   Test endpoints using [testSubscription](/api-docs/sell/notification/resources/subscription/methods/testSubscription) to confirm they are correctly receiving notifications.
*   Always validate incoming notification payloads to ensure they are genuine and untampered with by using either the [getPublicKey](https://developer.ebay.com/api-docs/sell/notification/resources/public_key/methods/getPublicKey) method or one of the following eBay Event Notification SDKs:
    *   [Java SDK](https://github.com/eBay/event-notification-java-sdk)
    *   [.NET SDK](https://github.com/eBay/eBay-Notification-SDK-Dot-Net-Core)
    *   [Node.js SDK](https://github.com/eBay/event-notification-nodejs-sdk)
    *   [PHP SDK](https://github.com/eBay/event-notification-php-sdk)
    *   [Go SDK](https://github.com/eBay/event-notification-golang-sdk)

## Code Samples

### Retrieving eligible eBay listings for seller-initiated offers on eBay US Marketplace

**Label:** Retrieving eligible eBay listings for seller-initiated offers on eBay US Marketplace

#### Bash Sample

```bash
curl -X GET "https://api.ebay.com/sell/negotiation/v1/find_eligible_items"
-H "Authorization:Bearer OAUTH_token"
-H X-EBAY-C-MARKETPLACE-ID:EBAY_US
```

### Retrieve all notification topics

**Label:** Retrieve all notification topics

#### Bash Sample

```bash
curl -X GET "https://api.ebay.com/commerce/notification/v1/topic"
-H "Authorization:Bearer OAUTH_token"
```

## Related Topics

- [Notification API](/api-docs/sell/notification/resources/methods)
- [Negotiation API](/api-docs/sell/negotiation/overview.html)
- [Trading Notification APIs](/api-docs/static/platform-notifications-landing.html)
- [Trading Feedback APIs](/Devzone/XML/docs/Reference/eBay/CommunicationIndex.html#itemfeedback)
- [Trading Messaging APIs](/Devzone/XML/docs/Reference/eBay/CommunicationIndex.html#eBaymessaging)
- [eBay Seller Standards program](https://www.sps.ebay.com/sd/sdrequirements)
- [More Guides](/develop/guides)

