[Skip to main content](https://shopify.dev/docs/api/admin-rest#main-content)
[![Docs page](https://shopify-assets.shopifycdn.com/shopifycloud/shopify-dev/production/assets/dev-docs-logo-2-light-D4UI1jxY.svg)![Docs page](https://shopify-assets.shopifycdn.com/shopifycloud/shopify-dev/production/assets/dev-docs-logo-2-dark-BQ-Bk9XA.svg)](https://shopify.dev/docs)
  * [Apps](https://shopify.dev/docs/apps/build)
  * [Storefronts](https://shopify.dev/docs/storefronts)
  * [Agents](https://shopify.dev/docs/agents)
  * References
  * [Changelog](https://shopify.dev/changelog)


  * Ask assistant`/`
  * [Help](https://shopify.dev/support)
  * •
  * [Log in](http://dev.shopify.com/dashboard)


Collapse sidebar
[Back to all APIsREST Admin API](https://shopify.dev/docs/api)
Choose a version:
unstable 2027-01 release candidate 2026-10 latest 2026-07 2026-04 2026-01
2026-10latest
  * [Overview](https://shopify.dev/docs/api/admin-rest)
  * [Client libraries](https://shopify.dev/docs/api/admin-rest#client-libraries)
  * [Authentication](https://shopify.dev/docs/api/admin-rest#authentication)
  * [Endpoints and requests](https://shopify.dev/docs/api/admin-rest#endpoints-and-requests)
  * [Rate limits](https://shopify.dev/docs/api/admin-rest#rate-limits)
  * [Status and error codes](https://shopify.dev/docs/api/admin-rest#status-and-error-codes)


* * *
  * Access
  * Billing
  * Customers
  * Discounts
  * Events
  * Gift Cards
  * Inventory
  * Marketing Event
  * Metafield
  * Mobile Support
  * Online Store
  * Orders
  * Plus
  * Products
  * Sales Channels
  * Shipping And Fulfillment
  * Shopify Payments
  * Store Properties
  * Tender Transaction
  * Webhooks
  * Deprecated API Calls


Full index
![](https://shopify-assets.shopifycdn.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://shopify-assets.shopifycdn.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)
The REST Admin API is a legacy API as of October 1, 2024. Starting April 1, 2025, all new public apps must be built exclusively with the [GraphQL Admin API](https://shopify.dev/docs/api/admin-graphql).
# REST Admin API reference
The Admin API lets you build apps and integrations that extend and enhance the Shopify admin.
Some newer platform features may only be available in [GraphQL](https://shopify.dev/docs/api/admin-graphql).
Install AI ToolkitAsk about this pageCopy MD
Choose a version:
unstable 2027-01 release candidate 2026-10 latest 2026-07 2026-04 2026-01
2026-10latest
## 
[Anchor to Client libraries](https://shopify.dev/docs/api/admin-rest#client-libraries)Client libraries
Use Shopify’s officially supported libraries to build fast, reliable apps with the programming languages and frameworks you already know.
![](https://shopify-assets.shopifycdn.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/CURL-DNth-3tL.svg)![](https://shopify-assets.shopifycdn.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/CURL-dark-Dltnwzzq.svg)
cURL
Use the [curl utility](https://curl.se/) to make API queries directly from the command line.
![](https://shopify-assets.shopifycdn.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/Remix-CsgrNfMr.svg)![](https://shopify-assets.shopifycdn.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/Remix-dark-pBuEP-h0.svg)
Remix
The official package for Remix applications, with full TypeScript support.
  * [Docs](https://shopify.dev/docs/api/shopify-app-remix)
  * [npm package](https://www.npmjs.com/package/@shopify/shopify-app-remix)
  * [GitHub repo](https://github.com/Shopify/shopify-app-js/tree/main/packages/apps/shopify-app-remix#readme)


![](https://shopify-assets.shopifycdn.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/Nodejs-DcYew0um.svg)![](https://shopify-assets.shopifycdn.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/Nodejs-dark-DB-77f7o.svg)
Node.js
The official client library for Node.js applications, with full TypeScript support. It has no framework dependencies, so it can be used by any Node.js app.
  * [Docs](https://github.com/Shopify/shopify-app-js/tree/main/packages/apps/shopify-api#readme)
  * [npm package](https://www.npmjs.com/package/@shopify/shopify-api)
  * [GitHub repo](https://github.com/Shopify/shopify-app-js/tree/main/packages/apps/shopify-api)


![](https://shopify-assets.shopifycdn.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/Ruby-C1_5iUYm.svg)![](https://shopify-assets.shopifycdn.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/Ruby-C1_5iUYm.svg)
Ruby
The official client library for Ruby apps.
  * [Docs](https://shopify.github.io/shopify-api-ruby/)
  * [Ruby gem](https://rubygems.org/gems/shopify_api)
  * [GitHub repo](https://github.com/Shopify/shopify-api-ruby)

Other
Need a different language? Check the list of [community-supported libraries](https://shopify.dev/docs/api/libraries-and-templates#third-party-api-libraries).
cURLRemixNode.jsRuby
Copy
1
2
3
# cURL is often available by default on macOS and Linux.
#
# See http://curl.se/docs/install.html for more details.
1
2
3
npm install --save @shopify/shopify-app-remix
# or
yarn add @shopify/shopify-app-remix
1
2
3
npm install --save @shopify/shopify-api
# or
yarn add @shopify/shopify-api
1
bundle add shopify_api
##### cURL

```
# cURL is often available by default on macOS and Linux.
#
# See http://curl.se/docs/install.html for more details.
```

##### Remix

```
npm install --save @shopify/shopify-app-remix
# or
yarn add @shopify/shopify-app-remix
```

##### Node.js

```
npm install --save @shopify/shopify-api
# or
yarn add @shopify/shopify-api
```

##### Ruby

```
bundle add shopify_api
```

* * *
## 
[Anchor to Authentication](https://shopify.dev/docs/api/admin-rest#authentication)Authentication
All REST Admin API queries require a valid Shopify access token.
Public and custom apps created in the Dev Dashboard generate tokens using [OAuth](https://shopify.dev/apps/auth/oauth), and custom apps made in the Shopify admin are [authenticated in the Shopify admin](https://shopify.dev/apps/auth/admin-app-access-tokens). To simplify the authentication process, use one of the recommended Shopify client libraries.
Include your token as a `X-Shopify-Access-Token` header on all API queries. Using Shopify’s supported [client libraries](https://shopify.dev/apps/tools/api-libraries) can simplify this process.
To keep the platform secure, apps need to request specific [access scopes](https://shopify.dev/docs/api/usage/access-scopes) during the install process. Only request as much data access as your app needs to work.
Learn more about [getting started with authentication](https://shopify.dev/apps/auth) and [building apps](https://shopify.dev/apps/getting-started).
cURLRemixNode.jsRuby
Copy
1
2
3
curl -X GET \ https://{shop}.myshopify.com/admin/api/2026-10/shop.json \
-H 'Content-Type: application/json' \
-H 'X-Shopify-Access-Token: {password}'
1
2
const { admin } = await authenticate.admin(request);
const response = admin.rest.get({path: 'shop'});
1
2
const client = new shopify.clients.Rest({session});
const response = client.get({path: 'shop'});
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
session = ShopifyAPI::Auth::Session.new(
shop: 'your-development-store.myshopify.com',
access_token: access_token,
)
  

ShopifyAPI::Context.setup(
api_key: 'client_id',
api_secret_key: 'client_secret',
api_version: 'api_version', # Example: '2026-10'
scope: 'read_products',
is_private: false, # Set to true if you are using a private app
is_embedded: true # Set to true if you are using an embedded app
)
  

ShopifyAPI::Context.activate_session(session)
  

client = ShopifyAPI::Clients::Rest::Admin.new(
session: session
)
response = client.get(path: 'shop')
##### cURL

```
curl -X GET \ https://{shop}.myshopify.com/admin/api/2026-10/shop.json \
  -H 'Content-Type: application/json' \
  -H 'X-Shopify-Access-Token: {password}'
```

##### Remix

```
const { admin } = await authenticate.admin(request);
const response = admin.rest.get({path: 'shop'});
```

##### Node.js

```
const client = new shopify.clients.Rest({session});
const response = client.get({path: 'shop'});
```

##### Ruby

```
session = ShopifyAPI::Auth::Session.new(
  shop: 'your-development-store.myshopify.com',
  access_token: access_token,
)

ShopifyAPI::Context.setup(
  api_key: 'client_id',
  api_secret_key: 'client_secret',
  api_version: 'api_version', # Example: '2026-10'
  scope: 'read_products',
  is_private: false, # Set to true if you are using a private app
  is_embedded: true # Set to true if you are using an embedded app
)

ShopifyAPI::Context.activate_session(session)

client = ShopifyAPI::Clients::Rest::Admin.new(
  session: session
)
response = client.get(path: 'shop')
```

* * *
## 
[Anchor to Endpoints and requests](https://shopify.dev/docs/api/admin-rest#endpoints-and-requests)Endpoints and requests
Admin REST API endpoints are organized by resource type. You’ll need to use different endpoints depending on your app’s requirements.
All Admin REST API endpoints follow this pattern:
`https://{store_name}.myshopify.com/admin/api/2026-10/{resource}.json`
POST
Example POST request
Create a new product.
This example illustrates how to create a new product using the Product resource and the `/admin/api/2026-10/products.json` endpoint. Replace `{store_name}` with your store’s domain and `{access_token}` with the access token you generated in the Authentication section.
GET
Example GET request
Retrieve a single product.
This example illustrates how to retrieve information for a single product using the Product resource and the `admin/api/2026-10/products/{product_id}.json` endpoint. Replace `{store_name}` with your store’s domain and `{access_token}` with the access token you generated in the Authentication section.
PUT
Example PUT request
Update a product.
This example illustrates how to update a product using the Product resource and the `admin/api/2026-10/products/{product_id}.json` endpoint. Replace `{store_name}` with your store’s domain and `{access_token}` with the access token you generated in the Authentication section.
DEL
Example DELETE request
Delete a product.
This example illustrates how to delete a product using the Product resource and the `admin/api/2026-10/products/{product_id}.json` endpoint. Replace `{store_name}` with your store’s domain and `{access_token}` with the access token you generated in the Authentication section.
POST
## /admin/api/2026-10/products.json
cURLNode.jsRuby
Copy
1
2
3
4
5
6
7
8
9
10
11
12
# Create a new product record
curl -X POST \
https://{store_name}.myshopify.com/admin/api/2026-10/products.json \
-H 'Content-Type: application/json' \
-H 'X-Shopify-Access-Token: {access_token}' \
-d '
{
"product": {
"title": "Hiking backpack"
}
}
'
1
2
3
4
5
6
7
8
9
10
11
12
const body = {
product: {
title: "Hiking backpack"
}
};
// `session` is built as part of the OAuth process
const client = new shopify.clients.Rest({session});
await client.post({
path: 'products',
data: body,
type: DataType.JSON,
});
1
2
3
4
5
6
7
8
9
10
11
12
13
body = {
product: {
title: "Hiking backpack"
}
}
# `session` is built as part of the OAuth process
client = ShopifyAPI::Clients::Rest::Admin.new(
session: session
)
response = client.post(
path: "products",
body: body
)
##### cURL

```
# Create a new product record
curl -X POST \
  https://{store_name}.myshopify.com/admin/api/2026-10/products.json \
  -H 'Content-Type: application/json' \
  -H 'X-Shopify-Access-Token: {access_token}' \
  -d '
  {
    "product": {
      "title": "Hiking backpack"
    }
  }
  '
```

##### Node.js

```
const body = {
  product: {
    title: "Hiking backpack"
  }
};
// `session` is built as part of the OAuth process
const client = new shopify.clients.Rest({session});
await client.post({
  path: 'products',
  data: body,
  type: DataType.JSON,
});
```

##### Ruby

```
body = {
  product: {
    title: "Hiking backpack"
  }
}
# `session` is built as part of the OAuth process
client = ShopifyAPI::Clients::Rest::Admin.new(
  session: session
)
response = client.post(
  path: "products",
  body: body
)
```

## {} Response
Copy
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
HTTP/1.1 200 OK
{
"product": {
"id": 11235813213455,
"title": "Hiking backpack",
"body_html": null,
"vendor": "",
"product_type": "",
"created_at": "<NOW>",
"handle": "hiking-backpack",
"updated_at": "<NOW>",
"published_at": "<NOW>",
"template_suffix": null,
"status": "active",
"published_scope": "web",
"tags": "",
"admin_graphql_api_id": "gid://shopify/Product/11235813213455",
"variants": [
{
"id": 16180339887498,
"product_id": 11235813213455,
"title": "Default Title",
"price": "0.00",
"sku": "",
"position": 1,
"inventory_policy": "deny",
"compare_at_price": null,
"fulfillment_service": "manual",
"inventory_management": null,
"option1": "Default Title",
"option2": null,
"option3": null,
"created_at": "<NOW>",
"updated_at": "<NOW>",
"taxable": true,
"barcode": null,
"grams": 0,
"image_id": null,
"weight": 0,
"weight_unit": "kg",
"inventory_item_id": 2233311419,
"inventory_quantity": 0,
"old_inventory_quantity": 0,
"requires_shipping": true,
"admin_graphql_api_id": "gid://shopify/ProductVariant/16180339887498"
}
],
"options": [
{
"id": 46910141521222530,
"product_id": 11235813213455,
"name": "Title",
"position": 1,
"values": [
"Default Title"
]
}
],
"images": [],
"image": null
}
}
GET
## /admin/api/2026-10/products/(product_id).json
cURLRemixNode.jsRuby
Copy
1
2
3
4
curl -X GET \
https://{store_name}.myshopify.com/admin/api/2026-10/products/11235813213455.json?fields=id,title \
-H 'Content-Type: application/json' \
-H 'X-Shopify-Access-Token: {access_token}'
1
2
3
4
5
6
7
const productId = "11235813213455";
  

const { admin } = await authenticate.admin(request);
const product = await admin.rest.get({
path: `products/${productId}`,
query: {id: 1, title: "title"}
});
1
2
3
4
5
6
7
const productId = "11235813213455";
// `session` is built as part of the OAuth process
const client = new shopify.clients.Rest({session});
const product = await client.get({
path: `products/${productId}`,
query: {id: 1, title: "title"}
});
1
2
3
4
5
6
7
8
9
product_id = "11235813213455"
# `session` is built as part of the OAuth process
client = ShopifyAPI::Clients::Rest::Admin.new(
session: session
)
response = client.get(
path: "products/#{product_id}",
query: ["id" => 1, "title" => "title"]
)
##### cURL

```
curl -X GET \
  https://{store_name}.myshopify.com/admin/api/2026-10/products/11235813213455.json?fields=id,title \
  -H 'Content-Type: application/json' \
  -H 'X-Shopify-Access-Token: {access_token}'
```

##### Remix

```
const productId = "11235813213455";

const { admin } = await authenticate.admin(request);
const product = await admin.rest.get({
  path: `products/${productId}`,
  query: {id: 1, title: "title"}
});
```

##### Node.js

```
const productId = "11235813213455";
// `session` is built as part of the OAuth process
const client = new shopify.clients.Rest({session});
const product = await client.get({
  path: `products/${productId}`,
  query: {id: 1, title: "title"}
});
```

##### Ruby

```
product_id = "11235813213455"
# `session` is built as part of the OAuth process
client = ShopifyAPI::Clients::Rest::Admin.new(
  session: session
)
response = client.get(
  path: "products/#{product_id}",
  query: ["id" => 1, "title" => "title"]
)
```

## {} Response
Copy
1
2
3
4
5
6
7
HTTP/1.1 200 OK
{
"product": {
"id": 11235813213455,
"title": "Hiking backpack"
}
}
PUT
## /admin/api/2026-10/products/(product_id).json
cURLNode.jsRuby
Copy
1
2
3
4
5
6
7
8
9
10
11
curl -X PUT \
https://{store_name}.myshopify.com/admin/api/2026-10/products/11235813213455.json \
-H 'Content-Type: application/json' \
-H 'X-Shopify-Access-Token: {access_token}' \
-d '
{
"product": {
"title": "Mountaineering backpack"
}
}
'
1
2
3
4
5
6
7
8
9
10
11
12
const productId = 11235813213455;
const body = {
product: {
title: "Mountaineering backpack"
}
};
// `session` is built as part of the OAuth process
const client = new shopify.clients.Rest({session});
const response = await client.put({
path: `products/${productId}`,
data: body,
});
1
2
3
4
5
6
7
8
9
10
11
12
13
14
product_id = "11235813213455"
body = {
product: {
title: "Mountaineering backpack"
}
}
# `session` is built as part of the OAuth process
client = ShopifyAPI::Clients::Rest::Admin.new(
session: session
)
response = client.put(
path: "products/#{product_id}",
body: body
)
##### cURL

```
curl -X PUT \
  https://{store_name}.myshopify.com/admin/api/2026-10/products/11235813213455.json \
  -H 'Content-Type: application/json' \
  -H 'X-Shopify-Access-Token: {access_token}' \
	-d '
	{
		"product": {
			"title": "Mountaineering backpack"
		}
	}
	'
```

##### Node.js

```
const productId = 11235813213455;
const body = {
  product: {
    title: "Mountaineering backpack"
  }
};
// `session` is built as part of the OAuth process
const client = new shopify.clients.Rest({session});
const response = await client.put({
  path: `products/${productId}`,
  data: body,
});
```

##### Ruby

```
product_id = "11235813213455"
body = {
  product: {
      title: "Mountaineering backpack"
  }
}
# `session` is built as part of the OAuth process
client = ShopifyAPI::Clients::Rest::Admin.new(
  session: session
)
response = client.put(
  path: "products/#{product_id}",
  body: body
)
```

## {} Response
Copy
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
HTTP/1.1 200 OK
{
"product": {
"id": 11235813213455,
"title": "Mountaineering backpack",
"body_html": null,
"vendor": "",
"product_type": "",
"created_at": "<NOW>",
"handle": "hiking-backpack",
"updated_at": "<NOW>",
"published_at": "<NOW>",
"template_suffix": null,
"status": "active",
"published_scope": "web",
"tags": "",
"admin_graphql_api_id": "gid://shopify/Product/11235813213455",
"variants": [
{
"id": 16180339887498,
"product_id": 11235813213455,
"title": "Default Title",
"price": "0.00",
"sku": "",
"position": 1,
"inventory_policy": "deny",
"compare_at_price": null,
"fulfillment_service": "manual",
"inventory_management": null,
"option1": "Default Title",
"option2": null,
"option3": null,
"created_at": "<NOW>",
"updated_at": "<NOW>",
"taxable": true,
"barcode": null,
"grams": 0,
"image_id": null,
"weight": 0,
"weight_unit": "kg",
"inventory_item_id": 2233311419,
"inventory_quantity": 0,
"old_inventory_quantity": 0,
"requires_shipping": true,
"admin_graphql_api_id": "gid://shopify/ProductVariant/16180339887498"
}
],
"options": [
{
"id": 46910141521222530,
"product_id": 11235813213455,
"name": "Title",
"position": 1,
"values": [
"Default Title"
]
}
],
"images": [],
"image": null
}
}
## 
DEL
/admin/api/2025-07/products/(product_id).json
cURLNode.jsRuby
Copy
1
2
3
4
curl -X DELETE \
https://{store_name}.myshopify.com/admin/api/2026-10/products/11235813213455.json \
-H 'Content-Type: application/json' \
-H 'X-Shopify-Access-Token: {access_token}'
1
2
3
4
5
6
const productId = "11235813213455";
// `session` is built as part of the OAuth process
const client = new shopify.clients.Rest({session});
const product = await client.delete({
path: `products/${productId}`
});
1
2
3
4
5
6
product_id = "11235813213455"
# `session` is built as part of the OAuth process
client = ShopifyAPI::Clients::Rest::Admin.new(
session: session
)
response = client.delete(path: "products/#{product_id}")
##### cURL

```
curl -X DELETE \
  https://{store_name}.myshopify.com/admin/api/2026-10/products/11235813213455.json \
  -H 'Content-Type: application/json' \
  -H 'X-Shopify-Access-Token: {access_token}'
```

##### Node.js

```
const productId = "11235813213455";
// `session` is built as part of the OAuth process
const client = new shopify.clients.Rest({session});
const product = await client.delete({
  path: `products/${productId}`
});
```

##### Ruby

```
product_id = "11235813213455"
# `session` is built as part of the OAuth process
client = ShopifyAPI::Clients::Rest::Admin.new(
  session: session
)
response = client.delete(path: "products/#{product_id}")
```

## {} Response
Copy
1
2
HTTP/1.1 200 OK
{}
All REST endpoints support [cursor-based pagination](https://shopify.dev/docs/api/admin-rest/usage/pagination). All requests produce HTTP [response status codes](https://shopify.dev/api/usage/response-codes).
Learn more about [API usage](https://shopify.dev/docs/api).
### 
[Anchor to Versioning](https://shopify.dev/docs/api/admin-rest#versioning)Versioning
The Admin REST API is [versioned](https://shopify.dev/docs/api/usage/versioning). To keep your app stable, make sure that you specify a supported version in the URL.
* * *
## 
[Anchor to Rate limits](https://shopify.dev/docs/api/admin-rest#rate-limits)Rate limits
The REST Admin API supports a limit of 40 requests per app per store per minute. This allotment replenishes at a rate of 2 requests per second. The rate limit is increased by a factor of 10 for Shopify Plus stores.
### 
[Anchor to Usage limitations](https://shopify.dev/docs/api/admin-rest#usage-limitations)Usage limitations
REST Admin API supports a limit of **40 requests per app per store per minute**.
Past the limit, the API will return a `429 Too Many Requests` error.
All REST API responses include the `X-Shopify-Shop-Api-Call-Limit` header, which shows how many requests the client has made, and the total number allowed per minute.
A `429` response will also include a `Retry-After` header with the number of seconds to wait until retrying your query.
Learn more about [rate limits](https://shopify.dev/docs/api/admin-rest/usage/rate-limits).
## {} Header
Copy
1
2
X-Shopify-Shop-Api-Call-Limit: 40/40
Retry-After: 2.0
## {} Response
Copy
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
HTTP/1.1 429 Too Many Requests
{
"customers": [
{
"id": 207119551,
"email": "bob.norman@hostmail.com",
"accepts_marketing": false,
"created_at": "2021-02-12T13:48:32-05:00",
"updated_at": "2021-02-12T13:48:32-05:00",
"first_name": "Bob",
"last_name": "Norman",
"orders_count": 1,
"state": "disabled",
"total_spent": "199.65",
"last_order_id": 450789469,
"note": null,
"verified_email": true,
"multipass_identifier": null,
"tax_exempt": false,
"phone": "+16136120707",
"tags": "",
"last_order_name": "#1001",
"currency": "USD",
"addresses": [
{
"id": 207119551,
"customer_id": 207119551,
"first_name": null,
"last_name": null,
"company": null,
"address1": "Chestnut Street 92",
"address2": "",
"city": "Louisville",
"province": "Kentucky",
"country": "United States",
"zip": "40202",
"phone": "+1(800)-555-2181",
"name": "",
"province_code": "KY",
"country_code": "US",
"country_name": "United States",
"default": true
}
],
},
],
"accepts_marketing_updated_at": "2005-06-12T11:57:11-04:00",
"marketing_opt_in_level": null,
"tax_exemptions": [],
"admin_graphql_api_id": "gid://shopify/Customer/207119551",
"default_address": {
"id": 207119551,
"customer_id": 207119551,
"first_name": null,
"last_name": null,
"company": null,
"address1": "Chestnut Street 92",
"address2": "",
"city": "Louisville",
"province": "Kentucky",
"country": "United States",
"zip": "40202",
"phone": "+1(800)-555-2181",
"name": "",
"province_code": "KY",
"country_code": "US",
"country_name": "United States",
"default": true
}
}
* * *
## 
[Anchor to Status and error codes](https://shopify.dev/docs/api/admin-rest#status-and-error-codes)Status and error codes
All API queries return HTTP status codes that can tell you more about the response.
* * *
#### 
[Anchor to [object Object]](https://shopify.dev/docs/api/admin-rest#401-unauthorized)`401 Unauthorized`
The client doesn’t have correct [authentication](https://shopify.dev/docs/api/admin-rest#authentication) credentials.
* * *
#### 
[Anchor to [object Object]](https://shopify.dev/docs/api/admin-rest#402-payment-required)`402 Payment Required`
The shop is frozen. The shop owner will need to pay the outstanding balance to [unfreeze](https://help.shopify.com/en/manual/your-account/pause-close-store#unfreeze-your-shopify-store) the shop.
* * *
#### 
[Anchor to [object Object]](https://shopify.dev/docs/api/admin-rest#403-forbidden)`403 Forbidden`
The server is refusing to respond. This is typically caused by incorrect [access scopes](https://shopify.dev/docs/api/usage/access-scopes).
* * *
#### 
[Anchor to [object Object]](https://shopify.dev/docs/api/admin-rest#404-not-found)`404 Not Found`
The requested resource was not found but could be available again in the future.
* * *
#### 
[Anchor to [object Object]](https://shopify.dev/docs/api/admin-rest#422-unprocessable-entity)`422 Unprocessable Entity`
The request body contains semantic errors. This is typically caused by incorrect formatting, omitting required fields, or logical errors such as initiating a checkout for an out-of-stock product.
* * *
#### 
[Anchor to [object Object]](https://shopify.dev/docs/api/admin-rest#429-too-many-requests)`429 Too Many Requests`
The client has exceeded the [rate limit](https://shopify.dev/docs/api/admin-rest#rate-limits).
* * *
#### 
[Anchor to [object Object]](https://shopify.dev/docs/api/admin-rest#5xx-errors)`5xx Errors`
An internal error occurred in Shopify. Check out the [Shopify status page](https://www.shopifystatus.com) for more information.
* * *
Didn’t find the status code you’re looking for?
View the complete list of [API status response and error codes](https://shopify.dev/api/usage/response-codes).
**Didn’t find the status code you’re looking for? :**
View the complete list of [API status response and error codes](https://shopify.dev/api/usage/response-codes).
## {} Sample error codes
401402403404422429500
Copy
1
2
3
4
HTTP/1.1 401 Unauthorized
{
"errors": "[API] Invalid API key or access token (unrecognized login or wrong password)"
}
1
2
3
4
HTTP/1.1 402 Payment Required
{
"errors": "This shop's plan does not have access to this feature"
}
1
2
3
4
HTTP/1.1 403 Access Denied
{
"errors": "User does not have access"
}}
1
2
3
4
HTTP/1.1 404 Not Found
{
"errors": "Not Found"
}
1
2
3
4
5
6
HTTP/1.1 422 Unprocessable Entity
{
"errors": [
"The fulfillment order is not in an open state."
]
}
1
2
3
4
HTTP/1.1 429 Too Many Requests
{
"errors": "Exceeded 2 calls per second for api client. Reduce request rates to resume uninterrupted service."
}
1
2
3
4
HTTP/1.1 500 Internal Server Error
{
"errors": "An unexpected error occurred"
}
##### 401

```
HTTP/1.1 401 Unauthorized
{
  "errors": "[API] Invalid API key or access token (unrecognized login or wrong password)"
}
```

##### 402

```
HTTP/1.1 402 Payment Required
{
  "errors": "This shop's plan does not have access to this feature"
}
```

##### 403

```
HTTP/1.1 403 Access Denied
{
  "errors": "User does not have access"
}}
```

##### 404

```
HTTP/1.1 404 Not Found
{
  "errors": "Not Found"
}
```

##### 422

```
HTTP/1.1 422 Unprocessable Entity
{
  "errors": [
    "The fulfillment order is not in an open state."
  ]
}
```

##### 429

```
HTTP/1.1 429 Too Many Requests
{
  "errors": "Exceeded 2 calls per second for api client. Reduce request rates to resume uninterrupted service."
}
```

##### 500

```
HTTP/1.1 500 Internal Server Error
{
  "errors": "An unexpected error occurred"
}
```

* * *
Was this page helpful?
YesNo
### Updates
  * [Developer changelog](https://shopify.dev/changelog)
  * [Shopify Editions](https://www.shopify.com/editions)


### Business growth
  * [Shopify Partners Program](https://www.shopify.com/partners?shpxid=222dd762-CA08-48FF-E4D4-FF926B8FFCAD)
  * [Shopify App Store](https://apps.shopify.com/?shpxid=222dd762-CA08-48FF-E4D4-FF926B8FFCAD)


### Legal
  * [Terms of service](https://www.shopify.com/legal/terms?shpxid=222dd762-CA08-48FF-E4D4-FF926B8FFCAD)
  * [API terms of use](https://www.shopify.com/legal/api-terms?shpxid=222dd762-CA08-48FF-E4D4-FF926B8FFCAD)
  * [Privacy policy](https://www.shopify.com/legal/privacy?shpxid=222dd762-CA08-48FF-E4D4-FF926B8FFCAD)
  * [Partners Program Agreement](https://www.shopify.com/partners/terms?shpxid=222dd762-CA08-48FF-E4D4-FF926B8FFCAD)


### Shopify
  * [About Shopify](https://www.shopify.com/about?shpxid=222dd762-CA08-48FF-E4D4-FF926B8FFCAD)
  * [Shopify Plus](https://www.shopify.com/plus?shpxid=222dd762-CA08-48FF-E4D4-FF926B8FFCAD)
  * [Careers](https://www.shopify.com/careers?shpxid=222dd762-CA08-48FF-E4D4-FF926B8FFCAD)
  * [Investors](https://investors.shopify.com/home/default.aspx?shpxid=222dd762-CA08-48FF-E4D4-FF926B8FFCAD)
  * [Press and media](https://shopify.com/news?shpxid=7db0d4e4-24E8-4087-58FA-7EE470CA745A)



