Getting Started
Copy Page 
Page actions
#  Introduction to Seller API 
The Whatnot Seller API is a REST API for managing your store on Whatnot — products, inventory, orders, shipments, shows, and analytics — from your own systems.
Looking for the old GraphQL docs? Go to [developers.old.whatnot.com](https://developers.old.whatnot.com/docs/getting-started/introduction).
##  What you can do 
  * **Products** — create and manage listings, including variants, pricing, and media.
  * **Inventory** — set or adjust available quantity on variants, individually or in batches.
  * **Merchandising** — control a product's sale format and which shows or profile shop it's published to.
  * **Orders** — retrieve orders and their line items, and cancel orders that haven't shipped.
  * **Shipments** — retrieve shipment details, generate shipping labels, and add tracking codes.
  * **Shows** — retrieve your scheduled, live, and past shows, along with their analytics.
  * **Users** — look up the seller behind the current token, and disconnect your app's access.


##  Base URL 

```
https://api.whatnot.com/seller-api/rest/v2

```
plaintextCopyCopied
##  Getting started 
  1. Get an API token — see [Authentication](https://developers.whatnot.com/getting-started/authentication) for the Bearer token format.
  2. Check [Rate limits](https://developers.whatnot.com/getting-started/rate-limits) so your integration behaves well under load.
  3. Try a request — see below.
  4. Set up [Webhooks](https://developers.whatnot.com/getting-started/webhooks) if you want to react to events instead of polling.
  5. Explore every endpoint in the [API Reference](https://developers.whatnot.com/api-reference), or connect an agent [via MCP](https://developers.whatnot.com/getting-started/mcp).


###  Trying out the API 
Use the [API Reference](https://developers.whatnot.com/api-reference) to explore every endpoint and try real requests against the API directly from your browser, using your own API token.
###  Making requests 
The Seller API follows standard REST conventions: resources are addressed by URL, and the HTTP method (`GET`, `POST`, `PATCH`, `DELETE`) determines the action. Request and response bodies are JSON.
Every request must include your API token in the `Authorization` header, and a `Content-Type` header on any request with a body:

```
Authorization: Bearer <Your Whatnot Seller API Key>
Content-Type: application/json

```
plaintextCopyCopied
For example, listing your products is a `GET` request to `/products`:

```
GET /products
Authorization: Bearer <Your Whatnot Seller API Key>

```
plaintextCopyCopied
See the [API Reference](https://developers.whatnot.com/api-reference) for the full set of endpoints, request/response schemas, and error responses.
[ Previous **Overview**](https://developers.whatnot.com/)[ Next **Authentication**](https://developers.whatnot.com/getting-started/authentication)
On This Page
  * [What you can do ](https://developers.whatnot.com/getting-started/introduction#what-you-can-do)
  * [Base URL ](https://developers.whatnot.com/getting-started/introduction#base-url)
  * [Getting started ](https://developers.whatnot.com/getting-started/introduction#getting-started)
  * [Trying out the API ](https://developers.whatnot.com/getting-started/introduction#trying-out-the-api)
  * [Making requests ](https://developers.whatnot.com/getting-started/introduction#making-requests)


[![Whatnot](https://developers.whatnot.com/logo-dark.svg) ](https://www.whatnot.com/)[ Get the app](https://whatnot.onelink.me/56MH/xfwb7ijr?af_qr=true)
**Whatnot** [Blog ](https://blog.teamwhatnot.com)[Careers ](https://www.whatnot.com/careers)[FAQ ](https://help.whatnot.com/hc/)[Whatnot Affiliates](https://www.whatnotaffiliates.com/)
**Get Help** [Order Status ](https://help.whatnot.com/hc/articles/360061605391-Tracking-the-Status-of-your-Order)[Shipping and Delivery ](https://help.whatnot.com/hc/sections/4417212485005-Shipping-delivery)[Returns ](https://help.whatnot.com/hc/articles/360061194552-Return-Policy-in-the-US-and-Canada)[Payment Options ](https://help.whatnot.com/hc/articles/17151383107725-Buy-Now-Pay-Later-as-a-Payment-Method)[Contact Us](https://help.whatnot.com/hc/articles/4406478493069-Contact-Whatnot-Support)
© 2026 Whatnot Inc. [Terms ](https://www.whatnot.com/terms)[Privacy](https://www.whatnot.com/privacy)
[ ](https://www.facebook.com/RealWhatnot)[ ](https://x.com/Whatnot)[ ](https://www.instagram.com/Whatnot)[ ](https://www.linkedin.com/company/whatnot-inc/)[](https://www.tiktok.com/@Whatnot)
Ask AI
  * Getting Started 
Close Group 
    * Introduction
    * Authentication
    * Rate limits
    * Webhooks
    * Connect via MCP
    * SDKs
  * Request IDs
  * Errors
  * Taxonomy
  * API reference 
Open Group 


Sidebar Menu[![logo](https://developers.whatnot.com/logo-light.svg)![logo](https://developers.whatnot.com/logo-light.svg)](https://developers.whatnot.com/)[DocsDocs](https://developers.whatnot.com/getting-started/introduction)[APIAPI](https://developers.whatnot.com/api-reference)[WebhooksWebhooks](https://developers.whatnot.com/webhooks)
Open Search Search Keyboard Shortcut:`CTRL⌃ K `
[SupportSupport](https://help.whatnot.com/hc/en-us/articles/4406478493069-Contact-Whatnot-Support)

