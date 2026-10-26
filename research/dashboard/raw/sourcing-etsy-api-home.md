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
  * [API Essentials](https://developers.etsy.com/documentation/#!)
    * [Authentication](https://developers.etsy.com/documentation/essentials/authentication)
    * [URL Syntax](https://developers.etsy.com/documentation/essentials/urlsyntax)
    * [Definitions](https://developers.etsy.com/documentation/essentials/definitions)
    * [Request Standards](https://developers.etsy.com/documentation/essentials/requests)
    * [Rate Limits](https://developers.etsy.com/documentation/essentials/rate-limits)
    * [Webhooks](https://developers.etsy.com/documentation/essentials/webhooks)
    * [Get help](https://developers.etsy.com/documentation/get-help)
    * [API testing policy](https://www.etsy.com/legal/policy/api-testing-policy/169130941112)
  * [Tutorials](https://developers.etsy.com/documentation/#!)
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
    * [Personalization Migration](https://developers.etsy.com/documentation/#!)
      * [Personalization Migration Guide](https://developers.etsy.com/documentation/tutorials/personalization-migration)
      * [Personalization Examples](https://developers.etsy.com/documentation/tutorials/personalization/examples)
      * [Personalization Add-On Pricing](https://developers.etsy.com/documentation/tutorials/personalization-addon-pricing)
  * [MCP Server](https://developers.etsy.com/documentation/#!)
    * [Dev MCP Server](https://developers.etsy.com/documentation/mcp_server/devmcpserver)
  * [Manage your apps](https://www.etsy.com/developers)
  * [Terms of use](https://www.etsy.com/legal/api)


# Etsy Open API v3
Welcome to the improved Etsy Open API v3, a REST API that extends support for inventory, sales orders, and shop management on the Etsy platform. These guides support current and future app developers as they build tools to integrate with and automate processes for Etsy shops and customers.
##  Getting started[#](https://developers.etsy.com/documentation/#getting-started "Direct link to heading")
Our updated documentation is divided into a few sections, geared towards different use cases.
  * [Quick Start Guide](https://developers.etsy.com/documentation/tutorials/quickstart)
  * [API reference](https://developers.etsy.com/documentation/reference)
  * [API essentials](https://developers.etsy.com/documentation/essentials/oauth2/)
  * [Tutorials](https://developers.etsy.com/documentation/tutorials/overview)
  * [MCP Server](https://developers.etsy.com/documentation/mcp_server/devmcpserver)


##  Build with AI[#](https://developers.etsy.com/documentation/#build-with-ai "Direct link to heading")
The [OpenAPI Dev MCP server](https://developers.etsy.com/documentation/mcp_server/devmcpserver) connects AI coding assistants directly to the Etsy Open API, providing access to endpoint details, request and response schemas, authentication requirements, and OAuth scopes. Ask your assistant questions like "How do I create a listing?" or "What fields are in a ShopReceipt?" and get accurate, current answers backed by the live API spec.
Compatible with Claude, Cursor, VS Code, and other MCP-compatible tools. No API key is required to use the MCP server.
##  Developing a New Open API App[#](https://developers.etsy.com/documentation/#developing-a-new-open-api-app "Direct link to heading")
To build with Etsy's Open API v3, you need to register an app in the Etsy Developer Portal. Registering an app creates an Etsy App API keystring and a shared secret, which you can find in [Your Apps](https://www.etsy.com/developers).
There are two main paths for creating an app, depending on what you want to build:
  1. **Seller App** — for sellers building tools for their own shop.
  2. **Personal App, with the option to request Commercial Access later** — for developers building tools that may be used by other buyers or sellers.


Choose the path that best matches your use case.
##  Seller Apps[#](https://developers.etsy.com/documentation/#seller-apps "Direct link to heading")
Seller Apps are for individual Etsy sellers who want to connect an app to their own shop data.
This is the recommended starting point if you are a shop owner building custom tools, automations, reports, or workflows for your shop only.
###  Eligibility[#](https://developers.etsy.com/documentation/#eligibility "Direct link to heading")
Any seller with an active Etsy shop in good standing who doesn't already have an active app.
###  What's included[#](https://developers.etsy.com/documentation/#whats-included "Direct link to heading")
Seller App access includes access to all public and OAuth-authenticated endpoints, scoped only to your registered shop.
###  How to apply[#](https://developers.etsy.com/documentation/#how-to-apply "Direct link to heading")
Register your app in the Developer Portal by selecting [Create a seller app](https://www.etsy.com/developers/register-seller-app).
Eligible sellers are approved within minutes, with no manual review queue.
###  Important limitation[#](https://developers.etsy.com/documentation/#important-limitation "Direct link to heading")
Seller App Access is for your own shop use only. You will only be allowed to authenticate your app with your shop. It cannot be used to access other sellers' private shop data or to build applications for the broader Etsy seller community.
* * *
##  Personal Apps and Commercial Access[#](https://developers.etsy.com/documentation/#personal-apps-and-commercial-access "Direct link to heading")
A Personal App is the starting point for developers who want to build on Etsy's API for uses beyond their own shop.
This includes tools that other buyers or sellers may use at a limited scale. If your app needs to grow beyond limited-scale use, you can request an upgrade to **Commercial Access**.
Commercial Access is not a separate app creation path at first. It is reached through a two-step process:
  1. Create a **Personal App** in the Developer Portal.
  2. After the Personal App is approved, request **Commercial Access** for that app.


###  Personal App Access[#](https://developers.etsy.com/documentation/#personal-app-access "Direct link to heading")
Personal App access lets you build and test an app for use cases beyond your own shop, including tools that other buyers or sellers may use at limited scale.
####  Eligibility[#](https://developers.etsy.com/documentation/#eligibility-1 "Direct link to heading")
Any registered developer with a qualifying use case.
####  What's included[#](https://developers.etsy.com/documentation/#whats-included-1 "Direct link to heading")
Personal App access allows you to build with Etsy's API beyond your own shop, subject to Etsy's review and applicable limits.
####  How to apply[#](https://developers.etsy.com/documentation/#how-to-apply-1 "Direct link to heading")
Register your app in the Developer Portal and select [**Create a personal app**](https://www.etsy.com/developers/register).
Personal Apps go through a deeper review process than Seller Apps.
* * *
###  Commercial Access[#](https://developers.etsy.com/documentation/#commercial-access "Direct link to heading")
Commercial Access is for developers building applications that other Etsy sellers will connect to and use at a broader scale.
You must have an approved Personal App before you can request Commercial Access.
####  Eligibility[#](https://developers.etsy.com/documentation/#eligibility-2 "Direct link to heading")
Any registered developer with an approved Personal App and a qualifying commercial application.
####  What's included[#](https://developers.etsy.com/documentation/#whats-included-2 "Direct link to heading")
Commercial Access includes access to all public and OAuth-authenticated endpoints for any seller who grants OAuth consent, governed by OAuth token scopes.
####  How to apply[#](https://developers.etsy.com/documentation/#how-to-apply-2 "Direct link to heading")
To request Commercial Access:
  1. Create and receive approval for a **Personal App**.
  2. Go to [Apps You've Made](https://www.etsy.com/developers).
  3. Click **Request Commercial Access** next to your app.


If you are an individual seller looking to connect only to your own shop data, apply for a **Seller App** instead.
Commercial Access requests are reviewed manually. Review time may vary depending on your proposed use case.
* * *
##  Commercial Access Review Criteria[#](https://developers.etsy.com/documentation/#commercial-access-review-criteria "Direct link to heading")
Etsy reviews Commercial Access requests against the following criteria:
  * Applications and their home pages must comply with Etsy's [API Terms of Use](https://www.etsy.com/legal/api).
  * Applications must follow the caching policies identified in [Section 1](https://www.etsy.com/legal/api#license) of the API Terms of Use.
  * Applications must clearly distinguish themselves from Etsy, as noted in [Section 6](https://www.etsy.com/legal/api#marks) of the API Terms of Use. The following phrase must appear in a prominent position: "The term 'Etsy' is a trademark of Etsy, Inc. This application uses the Etsy API but is not endorsed or certified by Etsy, Inc."
  * Applications must not sidestep the API to retrieve or post Etsy data. Screen-scraping is not allowed.
  * Applications that access private member data must use OAuth authentication.
  * Application names and artwork must follow Etsy's [Trademark Policy](https://www.etsy.com/help/article/481).
  * Applications with Commercial Access that use the `transaction_r` permission scope must request access to the `buyer_email` field separately.


* * *
##  Not Sure Which Path Is Right for You?[#](https://developers.etsy.com/documentation/#not-sure-which-path-is-right-for-you "Direct link to heading")  
|   | **Seller App**  | **Personal App**  | **Commercial Access**  |  
| --- | --- | --- | --- |  
| Who it's for  | Individual sellers building for their own shop  | Developers building beyond their own shop at limited scale  | Developers building apps for other sellers at broader scale  |  
| Where to start  | Select **Create a seller app**  | Select **Create a personal app**  | Start by creating a Personal App, then request Commercial Access  |  
| Approval  | Automated, near-instant for eligible sellers  | Deeper review process  | Manual commercial review  |  
| Shop access  | Your shop only  | Limited-scale access based on approved use case  | Any seller who grants OAuth consent  |  
| Commercial use  | Not permitted  | Limited, based on approved use case  | Permitted after approval  |  
| Best for  | Shop owners building their own tools  | Developers testing or launching a limited-scale tool  | Developers scaling an app for use by many sellers  |  
###  Choosing the Right Option[#](https://developers.etsy.com/documentation/#choosing-the-right-option "Direct link to heading")
Choose **Create a seller app** if you are a shop owner and your app will only connect to your own Etsy shop.
Choose **Create a personal app** if you are building a tool that may be used by other buyers or sellers, but you do not yet need full Commercial Access.
Choose **Commercial Access** if your approved Personal App is ready to support other Etsy sellers at a broader scale.
##  Get Help[#](https://developers.etsy.com/documentation/#get-help "Direct link to heading")
When you need more support, please refer to the resources on our [help page](https://developers.etsy.com/documentation/get-help).
[Next Authentication »](https://developers.etsy.com/documentation/essentials/authentication)
  * [Getting started](https://developers.etsy.com/documentation/#getting-started)
  * [Build with AI](https://developers.etsy.com/documentation/#build-with-ai)
  * [Developing a New Open API App](https://developers.etsy.com/documentation/#developing-a-new-open-api-app)
  * [Seller Apps](https://developers.etsy.com/documentation/#seller-apps)
    * [Eligibility](https://developers.etsy.com/documentation/#eligibility)
    * [What's included](https://developers.etsy.com/documentation/#whats-included)
    * [How to apply](https://developers.etsy.com/documentation/#how-to-apply)
    * [Important limitation](https://developers.etsy.com/documentation/#important-limitation)
  * [Personal Apps and Commercial Access](https://developers.etsy.com/documentation/#personal-apps-and-commercial-access)
    * [Personal App Access](https://developers.etsy.com/documentation/#personal-app-access)
    * [Commercial Access](https://developers.etsy.com/documentation/#commercial-access)
  * [Commercial Access Review Criteria](https://developers.etsy.com/documentation/#commercial-access-review-criteria)
  * [Not Sure Which Path Is Right for You?](https://developers.etsy.com/documentation/#not-sure-which-path-is-right-for-you)
    * [Choosing the Right Option](https://developers.etsy.com/documentation/#choosing-the-right-option)
  * [Get Help](https://developers.etsy.com/documentation/#get-help)


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

