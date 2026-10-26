[Skip to main content](https://shopify.dev/docs/apps/build/authentication-authorization/client-credentials-grant?lang=node#main-content)
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
Apps
  * [Overview](https://shopify.dev/docs/apps/build)


* * *
  * ### Building and deploying apps
    * [Scaffold an app](https://shopify.dev/docs/apps/build/scaffold-app)
    * [Build an app](https://shopify.dev/docs/apps/build/build)
    * Deployment
    * Distribution
  * ### Dev tools
    * [Shopify AI Toolkit](https://shopify.dev/docs/apps/build/ai-toolkit)
    * Shopify CLI
    * Dev Dashboard
  * ### Building blocks
    * APIs
    * Authentication
    * Custom data
    * Events and webhooks
    * Extensions
    * Functions
  * ### Design and quality
    * Design guidelines
    * Security
    * App performance
    * Built for Shopify
  * ### App surfaces
    * Admin
    * App Home
    * Checkout
    * Customer accounts
    * Online store
    * Point of Sale
  * ### Use cases
    * AI and agents
    * Analytics
    * B2B
    * Flow
    * Global markets
    * Inventory management
    * Marketing and web pixels
    * Orders and fulfillment
    * Payments
    * Products and pricing
    * Sales channels
  * ### Selling and growing your app
    * Shopify App Store
    * Billing
    * Marketing and growth


Full index
# Authenticate an app for stores in your organization
Install AI ToolkitAsk about this pageCopy MD
This tutorial shows how to use the [client credentials grant](https://shopify.dev/docs/apps/build/authentication-authorization/access-tokens#client-credentials-grant) to get access tokens for a server-side app acting on stores in your own Shopify organization. Of the three grants, it takes the least setup: your app exchanges its own client ID and secret for a token, with no redirect flow to implement.
With a client credentials grant, you won't see a token in the Shopify admin. Instead, you request tokens programmatically when you need them.
Info
If you're building apps for other merchants, use [Shopify CLI](https://shopify.dev/docs/apps/build/cli-for-apps), which handles authentication automatically. To learn how authentication works for other common approaches, see [About app authentication](https://shopify.dev/docs/apps/build/authentication-authorization).
**Info :**
If you're building apps for other merchants, use [Shopify CLI](https://shopify.dev/docs/apps/build/cli-for-apps), which handles authentication automatically. To learn how authentication works for other common approaches, see [About app authentication](https://shopify.dev/docs/apps/build/authentication-authorization).
## 
[Anchor to What you'll learn](https://shopify.dev/docs/apps/build/authentication-authorization/client-credentials-grant?lang=node#what-youll-learn)What you'll learn
In this tutorial, you'll learn how to do the following tasks:
  * Find your app credentials in the Dev Dashboard
  * Exchange credentials for an access token programmatically
  * Use the access token to call Shopify APIs


## Requirements
[Dev Dashboard app](https://shopify.dev/docs/apps/build/dev-dashboard/create-apps-using-dev-dashboard)
You've created an app in the Dev Dashboard.
[Access scopes](https://shopify.dev/docs/apps/build/dev-dashboard/create-apps-using-dev-dashboard#step-2-create-a-version)
You've selected the access scopes your app needs on your app's version in the Dev Dashboard.
[Installed app](https://shopify.dev/docs/apps/build/dev-dashboard/create-apps-using-dev-dashboard#step-3-install-your-app)
You've installed your app on your store.
## Project
Language:
Node.js Python cURL
Node.js
[View on GitHub](https://github.com/Shopify/example-auth--client-credentials-grant)
## 
[Anchor to Get your credentials](https://shopify.dev/docs/apps/build/authentication-authorization/client-credentials-grant?lang=node#get-your-credentials)Get your credentials
Find your **Client ID** and **Client secret** in the Dev Dashboard. These credentials identify your app when requesting access tokens.
Caution
Keep your Client secret secure. Set it as an environment variable rather than putting it in a file you might commit, and never commit secrets to version control. In production, read it from your platform's environment configuration or a secret manager.
**Caution :**
Keep your Client secret secure. Set it as an environment variable rather than putting it in a file you might commit, and never commit secrets to version control. In production, read it from your platform's environment configuration or a secret manager.
### 
[Anchor to Locate your credentials](https://shopify.dev/docs/apps/build/authentication-authorization/client-credentials-grant?lang=node#locate-your-credentials)Locate your credentials
  1. Open your app in the [Dev Dashboard](https://dev.shopify.com/dashboard/).
  2. Go to **Settings**.
  3. Copy your **Client ID** and **Client secret**.

![Dev Dashboard settings page showing the Client ID and Secret fields.](https://shopify-assets.shopifycdn.com/shopifycloud/shopify-dev/production/assets/assets/images/apps/dev-dashboard/app-settings-BH6auFM7.png)
[About the Dev Dashboard](https://shopify.dev/docs/apps/build/dev-dashboard)
[About the Dev Dashboard](https://shopify.dev/docs/apps/build/dev-dashboard)
Skip to code
## 
[Anchor to Set your credentials as environment variables](https://shopify.dev/docs/apps/build/authentication-authorization/client-credentials-grant?lang=node#set-your-credentials-as-environment-variables)Set your credentials as environment variables
Keep your credentials out of your code so that you can't commit them and can use different values per environment.
### 
[Anchor to Add your credentials](https://shopify.dev/docs/apps/build/authentication-authorization/client-credentials-grant?lang=node#add-your-credentials)Add your credentials
The example code reads three variables from the environment. `SHOPIFY_SHOP` is your store's `myshopify.com` subdomain, without `.myshopify.com`:
Copy
1
2
3
export SHOPIFY_SHOP=your-store
export SHOPIFY_CLIENT_ID=your-client-id
export SHOPIFY_CLIENT_SECRET=your-client-secret
The examples also read a `.env` file when one is present, and environment variables take precedence over it. If you use a `.env` file, add it to your `.gitignore`.
Skip to code
Only show updated code lines
index.js
Copy
## 
/node/index.js
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
71
72
73
74
75
76
77
78
79
80
81
82
83
import { existsSync } from 'node:fs';
import { URLSearchParams } from 'node:url';
  

// Credentials come from the environment. Also read .env when one happens to be
// there, since the Shopify CLI writes credentials to that file. Real environment
// variables win over the file, so a platform's config always takes precedence.
// loadEnvFile needs Node.js 20.12 or later, and throws if the file is missing.
if (existsSync('.env')) {
process.loadEnvFile('.env');
}
  

const SHOP = process.env.SHOPIFY_SHOP;
const CLIENT_ID = process.env.SHOPIFY_CLIENT_ID;
const CLIENT_SECRET = process.env.SHOPIFY_CLIENT_SECRET;
  

if (!SHOP || !CLIENT_ID || !CLIENT_SECRET) {
throw new Error(
'Set SHOPIFY_SHOP, SHOPIFY_CLIENT_ID, and SHOPIFY_CLIENT_SECRET in your environment.'
);
}
  

let token = null;
let tokenExpiresAt = 0;
  

async function getToken() {
if (token && Date.now() < tokenExpiresAt - 60_000) return token;
  

const response = await fetch(
`https://${SHOP}.myshopify.com/admin/oauth/access_token`,
{
method: 'POST',
headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
body: new URLSearchParams({
grant_type: 'client_credentials',
client_id: CLIENT_ID,
client_secret: CLIENT_SECRET,
}),
}
);
  

if (!response.ok) throw new Error(`Token request failed: ${response.status}`);
  

const { access_token, expires_in } = await response.json();
token = access_token;
tokenExpiresAt = Date.now() + expires_in * 1000;
return token;
}
  

async function graphql(query, variables = {}) {
const response = await fetch(
`https://${SHOP}.myshopify.com/admin/api/2025-01/graphql.json`,
{
method: 'POST',
headers: {
'Content-Type': 'application/json',
'X-Shopify-Access-Token': await getToken(),
},
body: JSON.stringify({ query, variables }),
}
);
  

if (!response.ok) {
throw new Error(`GraphQL request failed: ${response.status}`);
}
  

const { data, errors } = await response.json();
if (errors?.length) {
throw new Error(`GraphQL errors: ${JSON.stringify(errors)}`);
}
return data;
}
  

async function main() {
const query =
'{ products(first: 3) { edges { node { id title handle } } } }';
const data = await graphql(query);
console.log('Products:', JSON.stringify(data, null, 2));
}
  

main().catch((error) => {
console.error(error);
process.exitCode = 1;
});
## 
[Anchor to Request an access token](https://shopify.dev/docs/apps/build/authentication-authorization/client-credentials-grant?lang=node#request-an-access-token)Request an access token
Use your credentials to make a programmatic request to Shopify's token endpoint.
### 
[Anchor to Exchange credentials for a token](https://shopify.dev/docs/apps/build/authentication-authorization/client-credentials-grant?lang=node#exchange-credentials-for-a-token)Exchange credentials for a token
The code reads your credentials from the environment and exchanges them for an access token. Tokens expire after 24 hours, so the example caches the token and refreshes it before expiry rather than requesting a new one per call.
* * *
Token response format
Copy
1
2
3
4
5
{
"access_token": "f85632530bf277ec9ac6f649fc327f17",
"scope": "read_products",
"expires_in": 86399
}
  * `access_token`: The token to include in API requests. Store this securely.
  * `scope`: The [access scopes](https://shopify.dev/docs/api/usage/access-scopes) granted to your app. The token request doesn't ask for scopes, so this is a readback of what you selected on your app's version in the Dev Dashboard. If a scope you need is missing, [release a new version](https://shopify.dev/docs/apps/build/dev-dashboard/create-apps-using-dev-dashboard#step-2-create-a-version) with it and approve the change on the store.
  * `expires_in`: Seconds until expiration. Always 86399 (24 hours).


* * *
Troubleshooting
##### 
[Anchor to [object Object], error](https://shopify.dev/docs/apps/build/authentication-authorization/client-credentials-grant?lang=node#shop_not_permitted-error)`shop_not_permitted` error
**Problem:** You receive the error `Oauth error shop_not_permitted: Client credentials cannot be performed on this shop.`
**Solution:** The client credentials grant only works when the app and the store belong to the same Shopify organization. "Same organization" means both appear under the same org in the Dev Dashboard. Owning a store or having it installed doesn't automatically place it in your org.
To verify:
  1. Open the [Dev Dashboard](https://dev.shopify.com/dashboard/) and click **Apps**. Confirm your app is listed.
  2. Click **Dev stores** in the sidebar and confirm your target store appears in the list. If the store isn't listed, it's not in this organization.
  3. Check that your `SHOPIFY_SHOP` value matches the store's `*.myshopify.com` subdomain exactly (without `.myshopify.com`).


Common causes:
  * **Dev store created outside the Dev Dashboard:** If you created a dev store from the Shopify admin rather than from the Dev Dashboard, it won't be in your org. Create a new dev store from the **Dev stores** page in the Dev Dashboard instead.
  * **Multiple organizations:** If you have access to more than one organization, the app and store might be in different ones. Check the organization ID in the URL (`dev.shopify.com/dashboard/<org-id>`) and verify both the app and store are under the same one.
  * **Acting on another organization's stores:** Client credentials can't reach a store outside your organization, including a client's store. Distribute your app to that store with [custom distribution](https://shopify.dev/docs/apps/launch/distribution/select-distribution-method) so that a merchant installs it, then use [token exchange](https://shopify.dev/docs/apps/build/authentication-authorization/implement-token-exchange) if your app runs inside the Shopify admin, or the [authorization code grant](https://shopify.dev/docs/apps/build/authentication-authorization/authenticate-standalone-apps) if it runs outside. [Shopify CLI](https://shopify.dev/docs/apps/build/cli-for-apps) handles OAuth for you.


##### 
[Anchor to External tool asks you to "copy a token"](https://shopify.dev/docs/apps/build/authentication-authorization/client-credentials-grant?lang=node#external-tool-asks-you-to-copy-a-token)External tool asks you to "copy a token"
**Problem:** Some external tools ask you to copy a token or provide a "Shopify API key." These tools expect the older authentication flow.
**Solution:** Contact the tool vendor about updating their integration to use OAuth.
##### 
[Anchor to "Invalid API key or access token" error](https://shopify.dev/docs/apps/build/authentication-authorization/client-credentials-grant?lang=node#invalid-api-key-or-access-token-error)"Invalid API key or access token" error
**Problem:** You're sending your `client_id` or `client_secret` directly to the GraphQL Admin API.
**Solution:** First exchange your credentials for an `access_token` using the token endpoint, then use that token in your API requests.
Skip to code
Only show updated code lines
index.js
Copy
## 
/node/index.js
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
71
72
73
74
75
76
77
78
79
80
81
82
83
import { existsSync } from 'node:fs';
import { URLSearchParams } from 'node:url';
  

// Credentials come from the environment. Also read .env when one happens to be
// there, since the Shopify CLI writes credentials to that file. Real environment
// variables win over the file, so a platform's config always takes precedence.
// loadEnvFile needs Node.js 20.12 or later, and throws if the file is missing.
if (existsSync('.env')) {
process.loadEnvFile('.env');
}
  

const SHOP = process.env.SHOPIFY_SHOP;
const CLIENT_ID = process.env.SHOPIFY_CLIENT_ID;
const CLIENT_SECRET = process.env.SHOPIFY_CLIENT_SECRET;
  

if (!SHOP || !CLIENT_ID || !CLIENT_SECRET) {
throw new Error(
'Set SHOPIFY_SHOP, SHOPIFY_CLIENT_ID, and SHOPIFY_CLIENT_SECRET in your environment.'
);
}
  

let token = null;
let tokenExpiresAt = 0;
  

async function getToken() {
if (token && Date.now() < tokenExpiresAt - 60_000) return token;
  

const response = await fetch(
`https://${SHOP}.myshopify.com/admin/oauth/access_token`,
{
method: 'POST',
headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
body: new URLSearchParams({
grant_type: 'client_credentials',
client_id: CLIENT_ID,
client_secret: CLIENT_SECRET,
}),
}
);
  

if (!response.ok) throw new Error(`Token request failed: ${response.status}`);
  

const { access_token, expires_in } = await response.json();
token = access_token;
tokenExpiresAt = Date.now() + expires_in * 1000;
return token;
}
  

async function graphql(query, variables = {}) {
const response = await fetch(
`https://${SHOP}.myshopify.com/admin/api/2025-01/graphql.json`,
{
method: 'POST',
headers: {
'Content-Type': 'application/json',
'X-Shopify-Access-Token': await getToken(),
},
body: JSON.stringify({ query, variables }),
}
);
  

if (!response.ok) {
throw new Error(`GraphQL request failed: ${response.status}`);
}
  

const { data, errors } = await response.json();
if (errors?.length) {
throw new Error(`GraphQL errors: ${JSON.stringify(errors)}`);
}
return data;
}
  

async function main() {
const query =
'{ products(first: 3) { edges { node { id title handle } } } }';
const data = await graphql(query);
console.log('Products:', JSON.stringify(data, null, 2));
}
  

main().catch((error) => {
console.error(error);
process.exitCode = 1;
});
## 
[Anchor to Make API requests](https://shopify.dev/docs/apps/build/authentication-authorization/client-credentials-grant?lang=node#make-api-requests)Make API requests
Include the `access_token` in the `X-Shopify-Access-Token` header when calling Shopify APIs.
### 
[Anchor to Query the GraphQL Admin API](https://shopify.dev/docs/apps/build/authentication-authorization/client-credentials-grant?lang=node#query-the-graphql-admin-api)Query the GraphQL Admin API
Use the access token to authenticate requests to any Shopify API. This example queries products using the GraphQL Admin API.
[ ![](https://shopify-assets.shopifycdn.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://shopify-assets.shopifycdn.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg) GraphQL Admin API](https://shopify.dev/docs/api/admin-graphql)[Access scopes](https://shopify.dev/docs/api/usage/access-scopes)
[ ![](https://shopify-assets.shopifycdn.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://shopify-assets.shopifycdn.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg) GraphQL Admin API](https://shopify.dev/docs/api/admin-graphql) [Access scopes](https://shopify.dev/docs/api/usage/access-scopes)
Skip to code
Only show updated code lines
index.js
Copy
## 
/node/index.js
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
71
72
73
74
75
76
77
78
79
80
81
82
83
import { existsSync } from 'node:fs';
import { URLSearchParams } from 'node:url';
  

// Credentials come from the environment. Also read .env when one happens to be
// there, since the Shopify CLI writes credentials to that file. Real environment
// variables win over the file, so a platform's config always takes precedence.
// loadEnvFile needs Node.js 20.12 or later, and throws if the file is missing.
if (existsSync('.env')) {
process.loadEnvFile('.env');
}
  

const SHOP = process.env.SHOPIFY_SHOP;
const CLIENT_ID = process.env.SHOPIFY_CLIENT_ID;
const CLIENT_SECRET = process.env.SHOPIFY_CLIENT_SECRET;
  

if (!SHOP || !CLIENT_ID || !CLIENT_SECRET) {
throw new Error(
'Set SHOPIFY_SHOP, SHOPIFY_CLIENT_ID, and SHOPIFY_CLIENT_SECRET in your environment.'
);
}
  

let token = null;
let tokenExpiresAt = 0;
  

async function getToken() {
if (token && Date.now() < tokenExpiresAt - 60_000) return token;
  

const response = await fetch(
`https://${SHOP}.myshopify.com/admin/oauth/access_token`,
{
method: 'POST',
headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
body: new URLSearchParams({
grant_type: 'client_credentials',
client_id: CLIENT_ID,
client_secret: CLIENT_SECRET,
}),
}
);
  

if (!response.ok) throw new Error(`Token request failed: ${response.status}`);
  

const { access_token, expires_in } = await response.json();
token = access_token;
tokenExpiresAt = Date.now() + expires_in * 1000;
return token;
}
  

async function graphql(query, variables = {}) {
const response = await fetch(
`https://${SHOP}.myshopify.com/admin/api/2025-01/graphql.json`,
{
method: 'POST',
headers: {
'Content-Type': 'application/json',
'X-Shopify-Access-Token': await getToken(),
},
body: JSON.stringify({ query, variables }),
}
);
  

if (!response.ok) {
throw new Error(`GraphQL request failed: ${response.status}`);
}
  

const { data, errors } = await response.json();
if (errors?.length) {
throw new Error(`GraphQL errors: ${JSON.stringify(errors)}`);
}
return data;
}
  

async function main() {
const query =
'{ products(first: 3) { edges { node { id title handle } } } }';
const data = await graphql(query);
console.log('Products:', JSON.stringify(data, null, 2));
}
  

main().catch((error) => {
console.error(error);
process.exitCode = 1;
});
index.js
Copy
## 
/node/index.js
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
71
72
73
74
75
76
77
78
79
80
81
82
83
import { existsSync } from 'node:fs';
import { URLSearchParams } from 'node:url';
  

// Credentials come from the environment. Also read .env when one happens to be
// there, since the Shopify CLI writes credentials to that file. Real environment
// variables win over the file, so a platform's config always takes precedence.
// loadEnvFile needs Node.js 20.12 or later, and throws if the file is missing.
if (existsSync('.env')) {
process.loadEnvFile('.env');
}
  

const SHOP = process.env.SHOPIFY_SHOP;
const CLIENT_ID = process.env.SHOPIFY_CLIENT_ID;
const CLIENT_SECRET = process.env.SHOPIFY_CLIENT_SECRET;
  

if (!SHOP || !CLIENT_ID || !CLIENT_SECRET) {
throw new Error(
'Set SHOPIFY_SHOP, SHOPIFY_CLIENT_ID, and SHOPIFY_CLIENT_SECRET in your environment.'
);
}
  

let token = null;
let tokenExpiresAt = 0;
  

async function getToken() {
if (token && Date.now() < tokenExpiresAt - 60_000) return token;
  

const response = await fetch(
`https://${SHOP}.myshopify.com/admin/oauth/access_token`,
{
method: 'POST',
headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
body: new URLSearchParams({
grant_type: 'client_credentials',
client_id: CLIENT_ID,
client_secret: CLIENT_SECRET,
}),
}
);
  

if (!response.ok) throw new Error(`Token request failed: ${response.status}`);
  

const { access_token, expires_in } = await response.json();
token = access_token;
tokenExpiresAt = Date.now() + expires_in * 1000;
return token;
}
  

async function graphql(query, variables = {}) {
const response = await fetch(
`https://${SHOP}.myshopify.com/admin/api/2025-01/graphql.json`,
{
method: 'POST',
headers: {
'Content-Type': 'application/json',
'X-Shopify-Access-Token': await getToken(),
},
body: JSON.stringify({ query, variables }),
}
);
  

if (!response.ok) {
throw new Error(`GraphQL request failed: ${response.status}`);
}
  

const { data, errors } = await response.json();
if (errors?.length) {
throw new Error(`GraphQL errors: ${JSON.stringify(errors)}`);
}
return data;
}
  

async function main() {
const query =
'{ products(first: 3) { edges { node { id title handle } } } }';
const data = await graphql(query);
console.log('Products:', JSON.stringify(data, null, 2));
}
  

main().catch((error) => {
console.error(error);
process.exitCode = 1;
});
## 
[Anchor to Tutorial complete!](https://shopify.dev/docs/apps/build/authentication-authorization/client-credentials-grant?lang=node#tutorial-complete)Tutorial complete!
You've successfully authenticated your Dev Dashboard app using the client credentials grant and made API requests.
### 
[Anchor to Next steps](https://shopify.dev/docs/apps/build/authentication-authorization/client-credentials-grant?lang=node#next-steps)Next steps
[ ![](https://shopify-assets.shopifycdn.com/shopifycloud/shopify-dev/production/assets/assets/images/icons/32/gear-Dp8iz837.png)![](https://shopify-assets.shopifycdn.com/shopifycloud/shopify-dev/production/assets/assets/images/icons/32/gear-dark-cBM9HQwb.png) Manage your credentialsFind your client ID and secret, secure them, and rotate your client secret. Manage your credentials Find your client ID and secret, secure them, and rotate your client secret. ](https://shopify.dev/docs/apps/build/authentication-authorization/manage-credentials)
[Manage your credentials  
  
Find your client ID and secret, secure them, and rotate your client secret.](https://shopify.dev/docs/apps/build/authentication-authorization/manage-credentials)
[ ![](https://shopify-assets.shopifycdn.com/shopifycloud/shopify-dev/production/assets/assets/images/icons/32/key-4B2yHMmv.png)![](https://shopify-assets.shopifycdn.com/shopifycloud/shopify-dev/production/assets/assets/images/icons/32/key-dark-BYWGft3h.png) Manage access scopesFind the scopes that common resources need, and where to declare them for a Dev Dashboard app. Manage access scopes Find the scopes that common resources need, and where to declare them for a Dev Dashboard app. ](https://shopify.dev/docs/apps/build/authentication-authorization/manage-access-scopes)
[Manage access scopes  
  
Find the scopes that common resources need, and where to declare them for a Dev Dashboard app.](https://shopify.dev/docs/apps/build/authentication-authorization/manage-access-scopes)
[ ![](https://shopify-assets.shopifycdn.com/shopifycloud/shopify-dev/production/assets/assets/images/icons/32/build-Cs_-e-f5.png)![](https://shopify-assets.shopifycdn.com/shopifycloud/shopify-dev/production/assets/assets/images/icons/32/build-dark-Dg-kCZSs.png) GraphQL Admin APIStart building with the GraphQL Admin API. GraphQL Admin API Start building with the GraphQL Admin API. ](https://shopify.dev/docs/api/admin-graphql)
[GraphQL Admin API  
  
Start building with the GraphQL Admin API.](https://shopify.dev/docs/api/admin-graphql)
[ ![](https://shopify-assets.shopifycdn.com/shopifycloud/shopify-dev/production/assets/assets/images/icons/32/gear-Dp8iz837.png)![](https://shopify-assets.shopifycdn.com/shopifycloud/shopify-dev/production/assets/assets/images/icons/32/gear-dark-cBM9HQwb.png) Monitor app performanceAccess logs and metrics to understand and optimize your app's performance. Monitor app performance Access logs and metrics to understand and optimize your app's performance. ](https://shopify.dev/docs/apps/build/dev-dashboard/monitoring-and-logs)
[Monitor app performance  
  
Access logs and metrics to understand and optimize your app's performance.](https://shopify.dev/docs/apps/build/dev-dashboard/monitoring-and-logs)
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



