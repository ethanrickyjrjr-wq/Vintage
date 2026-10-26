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
  * [API Essentials](https://developers.etsy.com/documentation/essentials/authentication/#!)
    * [Authentication](https://developers.etsy.com/documentation/essentials/authentication)
    * [URL Syntax](https://developers.etsy.com/documentation/essentials/urlsyntax)
    * [Definitions](https://developers.etsy.com/documentation/essentials/definitions)
    * [Request Standards](https://developers.etsy.com/documentation/essentials/requests)
    * [Rate Limits](https://developers.etsy.com/documentation/essentials/rate-limits)
    * [Webhooks](https://developers.etsy.com/documentation/essentials/webhooks)
    * [Get help](https://developers.etsy.com/documentation/get-help)
    * [API testing policy](https://www.etsy.com/legal/policy/api-testing-policy/169130941112)
  * [Tutorials](https://developers.etsy.com/documentation/essentials/authentication/#!)
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
    * [Personalization Migration](https://developers.etsy.com/documentation/essentials/authentication/#!)
      * [Personalization Migration Guide](https://developers.etsy.com/documentation/tutorials/personalization-migration)
      * [Personalization Examples](https://developers.etsy.com/documentation/tutorials/personalization/examples)
      * [Personalization Add-On Pricing](https://developers.etsy.com/documentation/tutorials/personalization-addon-pricing)
  * [MCP Server](https://developers.etsy.com/documentation/essentials/authentication/#!)
    * [Dev MCP Server](https://developers.etsy.com/documentation/mcp_server/devmcpserver)
  * [Manage your apps](https://www.etsy.com/developers)
  * [Terms of use](https://www.etsy.com/legal/api)


# Authentication
The Etsy Open API requires two credentials: an **API key** for app authentication, and an **OAuth 2.0 token** for user authorization on scoped endpoints.
  1. **API key** — required on **every** request, regardless of endpoint.
  2. **OAuth 2.0** — additionally required for endpoints that access private user data or perform write operations.


##  API Key[#](https://developers.etsy.com/documentation/essentials/authentication/#api-key "Direct link to heading")
Every request to a v3 endpoint must include an `x-api-key` header containing your _keystring_ and _shared secret_ separated by a colon:
x-api-key: <keystring>:<shared_secret>
Copy
You can find both values on the [Your Apps](https://www.etsy.com/developers/your-apps) page. For example, if your keystring is `1aa2bb33c44d55eeeeee6fff` and your shared secret is `a1b2c3d4e5`:
x-api-key: 1aa2bb33c44d55eeeeee6fff:a1b2c3d4e5
Copy
##  OAuth 2.0[#](https://developers.etsy.com/documentation/essentials/authentication/#oauth-20 "Direct link to heading")
Etsy’s Open API supports OAuth 2.0 [Authorization Code Grants](https://tools.ietf.org/html/rfc6749#page-24) to generate OAuth tokens for app security. Authorization code grants require users to approve access, which generates an authorization code an app includes in a token request (`https://api.etsy.com/v3/public/oauth/token`) from the [OAuth resource](https://developers.etsy.com/documentation/reference#section/Authentication/oauth2).
[OAuth 2.0](https://tools.ietf.org/html/rfc6749) is fairly well-standardized, so this document focuses on Etsy’s specific implementation of OAuth2.
##  Requesting an OAuth Token[#](https://developers.etsy.com/documentation/essentials/authentication/#requesting-an-oauth-token "Direct link to heading")
Gather the following information before starting the **authorization code** grant flow:
  1. Your Etsy App API Key _keystring_ , which you can find in [Your Apps](https://www.etsy.com/developers/your-apps).
  2. A _callback URL_ your app uses to receive the authorization code. Typically, this is a page or script that starts the token request using the authorization code, and therefore must implement TLS and use an `https://` prefix. See [Redirect URIs](https://developers.etsy.com/documentation/essentials/authentication/#redirect-uris) below.
  3. The _scopes_ your application requires to use specific endpoints. The [Open API Reference](https://developers.etsy.com/documentation/reference) lists the authorizations required to use each endpoint. For example, the endpoint to [create a listing](https://developers.etsy.com/documentation/reference#operation/createDraftListing) requires an oauth2 token with `listings_w` scope. See [Scopes](https://developers.etsy.com/documentation/essentials/authentication/#scopes) below.
  4. (Recommended) A _state_ string, similar to a [strong password](https://techjury.net/blog/how-to-create-a-strong-password), which protects against [Cross-site request forgery](https://en.wikipedia.org/wiki/Cross-site_request_forgery) exploits. OAuth 2.1 clients relying on PKCE for CSRF protection may omit `state`, but including it is still best practice.
  5. A _code verifier_ and generated _code challenge_ proof key for code exchange (PKCE) pair required in the token request and authorization code request respectively. See [PKCE](https://developers.etsy.com/documentation/essentials/authentication/#proof-key-for-code-exchange-pkce) below.


###  Step 1: Request an Authorization Code[#](https://developers.etsy.com/documentation/essentials/authentication/#step-1-request-an-authorization-code "Direct link to heading")
To begin the flow, direct the user to `https://www.etsy.com/oauth/connect` with a GET request including the following URL parameters:  
| Parameter Name  | Description  |  
| --- | --- |  
| `response_type`  | Must always be the value `code` (no quotes).  |  
| `client_id`  | An Etsy App API Key _keystring_ for the app.  |  
| `redirect_uri`  | A URI your app uses to receive the authorization code or error message; see [Redirect URIs](https://developers.etsy.com/documentation/essentials/authentication/#redirect-uris) below. The URL must have the `https://` prefix or the request will fail.  |  
| `scope`  | A URL-encoded, space-separated list of one or more scopes (e.g., `shops_r%20shops_w`); see [Scopes](https://developers.etsy.com/documentation/essentials/authentication/#scopes) below.  |  
| `state`  | (Recommended) A single-use token generated specifically for a given request. It is important that the state parameter is impossible to guess, associated with a specific request, and used once. When present, it must be non-empty; Etsy echoes it back in the redirect response, allowing your app to verify the response matches the request and guard against [CSRF attacks](https://en.wikipedia.org/wiki/Cross-site_request_forgery). OAuth 2.1 clients relying on PKCE for CSRF protection may omit `state`, but including it is still best practice.  |  
| `code_challenge`  | The PKCE _code challenge_ SHA256-image of a random value for this request flow; see [PKCE](https://developers.etsy.com/documentation/essentials/authentication/#proof-key-for-code-exchange-pkce) below.  |  
| `code_challenge_method`  | Must always be the value `S256` (no quotes).  |  
For example, to request an authorization code for an Etsy app with an App API Key _keystring_ of `1aa2bb33c44d55eeeeee6fff`, initiate a GET request with the following URL:
https://www.etsy.com/oauth/connect?
response_type=code
&redirect_uri=https://www.example.com/some/location
&scope=transactions_r%20transactions_w
&client_id=1aa2bb33c44d55eeeeee6fff&state=superstate
&code_challenge=DSWlW2Abh-cf8CeLL8-g3hQ2WQyYdKyiu83u_s7nRhI
&code_challenge_method=S256
Copy
where:
  * `response_type=code` is required to request an authorization code.
  * `redirect_uri=https://www.example.com/some/location` directs etsy to send an authorization code response to `https://www.example.com/some/location`.
  * `scope=transactions_r%20transactions_w` adds read and write access to transactions in the authorization _scope_ for the request, which is required to [request shop receipts](https://developers.etsy.com/documentation/reference#operation/getShopReceipts). see [Scopes](https://developers.etsy.com/documentation/essentials/authentication/#scopes) below.
  * `client_id=1aa2bb33c44d55eeeeee6fff` is an API Key _keystring_ for the app.
  * `state=superstate` assigns the _state_ string to `superstate` which Etsy.com should return with the authorization code
  * `code_challenge=DSWlW2Abh-cf8CeLL8-g3hQ2WQyYdKyiu83u_s7nRhI` is the PKCE _code challenge_ generated from the _code verifier_ `vvkdljkejllufrvbhgeiegrnvufrhvrffnkvcknjvfid`, which must be in the OAuth token request with the authorization code.
  * `code_challenge_method=S256` is required to correctly interpret the _code_challenge_.


###  Step 2: Grant Access[#](https://developers.etsy.com/documentation/essentials/authentication/#step-2-grant-access "Direct link to heading")
If the authorization code request is valid, Etsy.com responds by prompting an Etsy.com user (typically the app user) to grant the application access the requested scopes.
![OAuth2 authorization confirmation page](https://img0.etsystatic.com/site-assets/open-api/oauth2-authorize.png)
If the user grants access, Etsy.com sends a request back to the app's `redirect_uri` with the following `GET` parameters:  
| Parameter Name  | Description  |  
| --- | --- |  
| `state`  | The _state_ parameter, exactly as set in the authorization request. Only present if `state` was included in the original request.  |  
| `code`  | An OAuth _authorization code_ required to request an OAuth token  |  
For example, the following response indicates that the user grants access and supplies an authorization code:
https://www.example.com/some/location?
code=bftcubu-wownsvftz5kowdmxnqtsuoikwqkha7_4na3igu1uy-ztu1bsken68xnw4spzum8larqbry6zsxnea4or9etuicpra5zi
&state=superstate
Copy
If you included `state` in your authorization request, validate that the _state_ string in the response matches the value you sent. If they do not match, halt authentication as the request is vulnerable to CSRF attacks. If they match, make a note never to use that _state_ again, and make your next authorization code request with a new _state_ string.
####  Errors[#](https://developers.etsy.com/documentation/essentials/authentication/#errors "Direct link to heading")
If the user does not consent, or there is some other error (e.g. a missing parameter), Etsy.com sends a response to the specified `redirect_uri` with the following `GET` parameters:  
| Parameter Name  | Description  |  
| --- | --- |  
| `state`  | The _state_ parameter, exactly as set in the authorization request. Only present if `state` was included in the original request.  |  
| `error`  | An error code from [RFC 6749](https://tools.ietf.org/html/rfc6749#section-5.2)  |  
| `error_description`  | A human-readable explanation of the error (always in English)  |  
| `error_uri`  | (Optional) A URL with more information about the error.  |  
###  Step 3: Request an Access Token[#](https://developers.etsy.com/documentation/essentials/authentication/#step-3-request-an-access-token "Direct link to heading")
Request an OAuth access token using the _authorization code_ in a POST request to the Etsy Open API `/oauth/token` resource. Most requests to the Etsy Open API require this access token, which has a functional life of 1 hour. The Etsy Open API delivers a [refresh token](https://developers.etsy.com/documentation/essentials/authentication/#Refreshing-an-OAuth-Token) with the access token, which you can use to obtain a new access token through the [refresh_token grant](https://tools.ietf.org/html/rfc6749#section-6), and has a longer functional lifetime (90 days).
To obtain an access token, make a POST request to `https://api.etsy.com/v3/public/oauth/token` with the following parameters in the request body in `application/x-www-form-urlencoded` format:  
| Parameter Name  | Description  |  
| --- | --- |  
| `grant_type`  | Must always be the value `authorization_code`  |  
| `client_id`  | An Etsy App API Key _keystring_ for the app.  |  
| `redirect_uri`  | (Optional) The redirect_uri used in the prior authorization code request. OAuth 2.1 clients may omit this. When present, it must exactly match the value used at the authorization endpoint.  |  
| `code`  | The _authorization code_ sent back from Etsy.com after [granting access](https://developers.etsy.com/documentation/essentials/authentication/#step-2-grant-access).  |  
| `code_verifier`  | The PKCE _code verifier_ preimage of the `code_challenge` used in the prior authorization code request; see [PKCE](https://developers.etsy.com/documentation/essentials/authentication/#proof-key-for-code-exchange-pkce) below.  |  
For example, to request access for an Etsy app with an App API Key _keystring_ of `1aa2bb33c44d55eeeeee6fff`, initiate a POST request:
curl -X POST https://api.etsy.com/v3/public/oauth/token \
-H 'Content-Type: application/x-www-form-urlencoded' \
-d grant_type=authorization_code \
-d client_id=1aa2bb33c44d55eeeeee6fff \
-d redirect_uri=https://www.example.com/some/location \
-d code=bftcubu-wownsvftz5kowdmxnqtsuoikwqkha7_4na3igu1uy-ztu1bsken68xnw4spzum8larqbry6zsxnea4or9etuicpra5zi \
-d code_verifier=vvkdljkejllufrvbhgeiegrnvufrhvrffnkvcknjvfid
Copy
where:
  * `grant_type=authorization_code` is required to request an OAuth token in an authorization token grant flow.
  * `client_id=1aa2bb33c44d55eeeeee6fff` is an API Key _keystring_ for the app.
  * `redirect_uri=https://www.example.com/some/location` is optional; when included, it must match the value used in the prior authorization code request. When omitted, the check is skipped.
  * `code=bftcubu-wownsvftz5kowdmxnqtsuoikwqkha7_4na3igu1uy-ztu1bsken68xnw4spzum8larqbry6zsxnea4or9etuicpra5zi` is the authorization code sent from Etsy.com after the user grants access
  * `code_verifier=vvkdljkejllufrvbhgeiegrnvufrhvrffnkvcknjvfid` is the PKCE _code verifier_ used to generate the _code challenge_ `DSWlW2Abh-cf8CeLL8-g3hQ2WQyYdKyiu83u_s7nRhI`, which we used in the authorization code request.


The Etsy Open API responds to an authentic request for an OAuth token with the following information in JSON format:
{
"access_token": "12345678.O1zLuwveeKjpIqCQFfmR-PaMMpBmagH6DljRAkK9qt05OtRKiANJOyZlMx3WQ_o2FdComQGuoiAWy3dxyGI4Ke_76PR",
"token_type": "Bearer",
"expires_in": 3600,
"refresh_token": "12345678.JNGIJtvLmwfDMhlYoOJl8aLR1BWottyHC6yhNcET-eC7RogSR5e1GTIXGrgrelWZalvh3YvvyLfKYYqvymd-u37Sjtx",
"scope": "transactions_r transactions_w"
}
Copy
where:
  * `access_token` is the OAuth grant token with a user id numeric prefix (`12345678` in the example above), which is the internal `user_id` of the Etsy.com user who grants the application access. The V3 Open API requires the combined user id prefix and OAuth token as formatted in this parameter to authenticate requests.
* * *
NOTE: This numeric OAuth `user_id` is only available from the authorization code grant flow
* * *
  * `token_type` is always `Bearer` which indicates that the OAuth token is a bearer token.
  * `expires_in` is the valid duration of the OAuth token in seconds from the moment it is granted; 3600 seconds is 1 hour.
  * `refresh_token` is the OAuth code to request a refresh token with a user id numeric prefix (`12345678` in the example). Use this for a refresh grant access request for a fresh OAuth token without requesting access from the user/seller an additional time.
  * `scope` is a space-delimited string of the scopes actually granted to the access token, which may be a subset of the requested scopes.


##  Redirect URIs[#](https://developers.etsy.com/documentation/essentials/authentication/#redirect-uris "Direct link to heading")
All `redirect_uri` parameter values must match a precise _callback URL_ string registered with Etsy. These values can be provided by editing your application at [etsy.com/developers/your-apps](https://www.etsy.com/developers/your-apps).
Authorization code or token requests with unregistered or non-matching `redirect_uri` values send an error to the user and Etsy.com does **not** redirect the user back to your app.
URL matching is case-sensitive and is specifically the URL established when you registered. For example, if your registered redirect URL is `https://www.example.com/some/location`, the following strings **fail** to match:
  * `http://www.example.com/some/location` (http, not https)
  * `https://www.example.com/some/location/` (additional trailing slash)
  * `https://www.example.com/some/location?` (additional trailing question mark)
  * `Https://www.example.com/some/location` (uppercase H in https)
  * `https://example.com/some/location` (no www subdomain)


##  Scopes[#](https://developers.etsy.com/documentation/essentials/authentication/#scopes "Direct link to heading")
Methods and fields in the Etsy API are tagged with "permission scopes" that control which operations an app can perform and which data an app can read with a given set of credentials. Scopes are the permissions you request from the user, and the access token proves you have permission to act from that user.
The following scopes are available at this time, though are subject to change. The availability of a scope does not necessarily imply the existence of an endpoint to perform that action. Each API endpoint may require zero, one, or more scopes for access. Consult the [Open API Reference](https://developers.etsy.com/documentation/reference) to determine the scopes required for each specific endpoint.  
| Name  | Description  |  
| --- | --- |  
| `address_r`  | Read a member's shipping addresses.  |  
| `address_w`  | Update and delete a member's shipping address.  |  
| `email_r`  | Read a user profile  |  
| `listings_d`  | Delete a member's listings.  |  
| `listings_r`  | Read a member's inactive and expired (i.e., non-public) listings.  |  
| `listings_w`  | Create and edit a member's listings.  |  
| `profile_r`  | Read a member's private profile information.  |  
| `profile_w`  | Update a member's private profile information.  |  
| `shops_r`  | See a member's shop description, messages and sections, even if not (yet) public.  |  
| `shops_w`  | Update a member's shop description, messages and sections.  |  
| `transactions_r`  | Read a member's purchase and sales data. This applies to buyers as well as sellers.  |  
| `transactions_w`  | Update a member's sales data.  |  
Scopes are associated with every access token, and any change in scope requires the user to re-authorize the application; to change scopes, you must go through the authorization code grant flow again. Conversely, users are generally less likely to authorize an application that makes a request for more scopes than it requires. As such, you should carefully tailor scope requests to your application.
To request multiple scopes, add them in a space-separated list. For example, to request the scopes to see a user’s shipping addresses and email address, add the `email_r%20address_r` strings for the scope parameter in the request for an authentication code.
##  Proof Key for Code Exchange (PKCE)[#](https://developers.etsy.com/documentation/essentials/authentication/#proof-key-for-code-exchange-pkce "Direct link to heading")
A Proof Key for Code Exchange (PKCE) is the implementation of an OAuth2 extension standardized in RFC 7636 that guarantees that an authorization code is valid for only one application and cannot be intercepted by the user or an attacker. The Etsy Open API requires a PKCE on every authorization flow request.
A PKCE works by using a code **verifier** , which must be a high-entropy random string consisting of between 43 and 128 characters from the range `[A-Za-z0-9._~-]` (i.e. unreserved URI characters).
You can generate an appropriate verifier using a cryptographically secure source of randomness and encode 32 bytes of random data into url-safe base 64. Store this value in association with a particular authorization code request.
Then construct a code **challenge** by taking the URL-safe base64-encoded output of the SHA256 hash of the code verifier, and use it in the authorization code request to `https://www.etsy.com/oauth/connect`.
You must provide the verifier in the request for an access token from the Etsy API server, which proves that you are the source of the original authorization request.
For an example of how to generate a code verifier and matching challenge, see [Appendix B of RFC 7636](https://tools.ietf.org/html/rfc7636#appendix-B).
##  Requesting a Refresh OAuth Token[#](https://developers.etsy.com/documentation/essentials/authentication/#requesting-a-refresh-oauth-token "Direct link to heading")
Etsy's Open API supports OAuth 2.0 [Refresh Grants](https://datatracker.ietf.org/doc/html/rfc6749#section-1.5) to generate OAuth tokens after the seller grants a user an initial Authorization Code grant token. Refresh tokens do not require sellers to re-approve access and have the same scope as the token granted by the initial Authorization Code grant token. You cannot change the scope of a refresh token from the scope established in the initial Authentication Grant token.
To obtain a refresh token, make a POST request to `https://api.etsy.com/v3/public/oauth/token` with the following parameters in the request body in `application/x-www-form-urlencoded` format:  
| Parameter Name  | Description  |  
| --- | --- |  
| `grant_type`  | Must be the value `refresh_token`  |  
| `client_id`  | An Etsy App API Key _keystring_ for the app.  |  
| `refresh_token`  | The _refresh token_ string sent with a prior Authorization Code Grant or Refresh Grant.  |  
For example, to request a refresh token for an Etsy app with an App API Key _keystring_ of `1aa2bb33c44d55eeeeee6fff`, initiate a POST request:
https://api.etsy.com/v3/public/oauth/token?
grant_type=refresh_token
&client_id=1aa2bb33c44d55eeeeee6fff
&refresh_token=12345678.JNGIJtvLmwfDMhlYoOJl8aLR1BWottyHC6yhNcET-eC7RogSR5e1GTIXGrgrelWZalvh3YvvyLfKYYqvymd-u37Sjtx
Copy
where:
  * `grant_type=refresh_code` is required to request an OAuth token in a refresh grant context.
  * `client_id=1aa2bb33c44d55eeeeee6fff` is an API Key _keystring_ for the app.
  * `refresh_token=12345678.JNGIJtvLmwfDMhlYoOJl8aLR1BWottyHC6yhNcET-eC7RogSR5e1GTIXGrgrelWZalvh3YvvyLfKYYqvymd-u37Sjtx` is the refresh code sent from Etsy.com after granting a prior authorization grant token or refresh grant token.


The Etsy Open API responds to an authentic request for an OAuth token with the following information in JSON format:
{
"access_token": "12345678.O1zLuwveeKjpIqCQFfmR-PaMMpBmagH6DljRAkK9qt05OtRKiANJOyZlMx3WQ_o2FdComQGuoiAWy3dxyGI4Ke_76PR",
"token_type": "Bearer",
"expires_in": 3600,
"refresh_token": "12345678.JNGIJtvLmwfDMhlYoOJl8aLR1BWottyHC6yhNcET-eC7RogSR5e1GTIXGrgrelWZalvh3YvvyLfKYYqvymd-u37Sjtx",
"scope": "transactions_r transactions_w"
}
Copy
where:
  * `access_token` is the OAuth refresh code with a user id numeric prefix (`12345678` in the example above), which is the internal `user_id` of the Etsy.com user who grants the application access.
  * `token_type` is always `Bearer` which indicates that the OAuth token is a bearer token.
  * `expires_in` is the valid duration of the OAuth token in seconds from the moment it is granted; 3600 seconds is 1 hour.
  * `refresh_token` is the OAuth code to request another refresh token with a user id numeric prefix (`12345678` in the example). Use this for a refresh grant access request for a fresh OAuth token without requesting access from the user/seller an additional time.
  * `scope` is a space-delimited string of the scopes granted to the access token.


##  APIv2 Endpoints and OAuth2 Tokens[#](https://developers.etsy.com/documentation/essentials/authentication/#apiv2-endpoints-and-oauth2-tokens "Direct link to heading")
Requests to v2 endpoints cannot use tokens generated through the OAuth 2.0 flow described above.
Requests to v3 endpoints must use OAuth 2.0 tokens. See [Exchange OAuth 1.0 Token for OAuth 2.0 Token](https://developers.etsy.com/documentation/essentials/authentication/#exchange-oauth-10-token-for-oauth-20-token) to upgrade existing tokens.
###  Scopes changed for OAuth 1.0 in the V3 Open API[#](https://developers.etsy.com/documentation/essentials/authentication/#scopes-changed-for-oauth-10-in-the-v3-open-api "Direct link to heading")
The V3 Open API supports most of the same scopes for OAuth 1.0 that were supported in V2. However, the following scopes are different from the scopes supported for V2, so you should update them if you use them:
  1. Several combined read and write scopes from v2 are split into separate read scopes and write scopes in v3

  
| V2 scope  | V3 scopes  | Description  | Affected Resources  |  
| --- | --- | --- | --- |  
| `favorites_rw`  | `favorites_r`  | View a member's favorite listings and users.  | FavoriteListing and FavoriteUser  |  
|   | `favorites_w`  | Add to and remove from a member's favorite listings and users.  | FavoriteListing and FavoriteUser  |  
| `shops_rw`  | `shops_r`  | View a member's shop description, messages and ections.  | Shop and ShopSection  |  
|   | `shops_w`  | Update a member's shop description, messages and sections.  | Shop and ShopSection  |  
| `cart_rw`  | `cart_r`  | View listings from a member's shopping cart.  | Cart and CartListing  |  
|   | `cart_w`  | Add and remove listings from a member's shopping cart.  | Cart and CartListing  |  
| `recommend_rw`  | `recommend_r`  | View a member's recommended listings.  | Listing  |  
|   | `recommend_w`  | Accept and reject a member's recommended listings.  | Listing  |  
  1. `collection_rw`, `page_collection_rw`, and `activity_r` are not implemented because no active end points use them.
  2. `treasury_r` and `treasury_w` are not valid because we discontinued the treasury feature.


###  Exchange OAuth 1.0 Token for OAuth 2.0 Token[#](https://developers.etsy.com/documentation/essentials/authentication/#exchange-oauth-10-token-for-oauth-20-token "Direct link to heading")
Etsy now supports OAuth 2.0 and existing Open API v3 applications that use OAuth 1.0 must either exchange their OAuth 1.0 access tokens for OAuth 2.0 access tokens or generate OAuth 2.0 access tokens using the OAuth 2.0 Authentication Code flow to use Open API v3 endpoints.
To exchange an OAuth 1.0 token for a new OAuth 2.0 token, make a POST request to `https://api.etsy.com/v3/public/oauth/token` with the following parameters in the request body in `application/x-www-form-urlencoded` format:  
| Parameter Name  | Description  |  
| --- | --- |  
| `grant_type`  | Must be the value `token_exchange`  |  
| `client_id`  | An Etsy App API Key _keystring_ for the app.  |  
| `legacy_token`  | The _legacy token_ is the current OAuth 1.0 token used by the application.  |  
For example, to exchange an access for a new OAuth 2.0 access token on an Etsy app with an App API Key _keystring_ of `1aa2bb33c44d55eeeeee6fff` and legacy token of `eeb39b80e3f43a4671b00dbedaa74e`, initiate a POST request:
https://api.etsy.com/v3/public/oauth/token?
grant_type=token_exchange
&client_id=1aa2bb33c44d55eeeeee6fff
&legacy_token=eeb39b80e3f43a4671b00dbedaa74e
Copy
The Etsy Open API responds to an authentic token exchange request with the following information in JSON format:
{
"access_token": "14099992.HZ3dHl_DTh-mhPntSLRPg_Q6hb2S9hsWsX8T-DxkEyzxYzFNFjhl7GsNhS8sps03RVDWlHttE8_0Am9aA4dy9Xztwdz",
"token_type": "Bearer",
"expires_in": 3600,
"refresh_token": "14099992.nJME1eWEAMw0asH3PG_mYilsD9neDny5x5WXF3FRIBXW_xylVH0sILgbu2ER7TQRCmBdluHakZdffPF7qEtQ0kBlWb8"
}
Copy
**Note:** OAuth 2.0 tokens generated from an OAuth 1.0 token exchange retain the scope(s) of the original OAuth 1.0 token.
[Previous « Etsy Open API v3](https://developers.etsy.com/documentation/)
[Next URL Syntax »](https://developers.etsy.com/documentation/essentials/urlsyntax)
  * [API Key](https://developers.etsy.com/documentation/essentials/authentication/#api-key)
  * [OAuth 2.0](https://developers.etsy.com/documentation/essentials/authentication/#oauth-20)
  * [Requesting an OAuth Token](https://developers.etsy.com/documentation/essentials/authentication/#requesting-an-oauth-token)
    * [Step 1: Request an Authorization Code](https://developers.etsy.com/documentation/essentials/authentication/#step-1-request-an-authorization-code)
    * [Step 2: Grant Access](https://developers.etsy.com/documentation/essentials/authentication/#step-2-grant-access)
    * [Step 3: Request an Access Token](https://developers.etsy.com/documentation/essentials/authentication/#step-3-request-an-access-token)
  * [Redirect URIs](https://developers.etsy.com/documentation/essentials/authentication/#redirect-uris)
  * [Scopes](https://developers.etsy.com/documentation/essentials/authentication/#scopes)
  * [Proof Key for Code Exchange (PKCE)](https://developers.etsy.com/documentation/essentials/authentication/#proof-key-for-code-exchange-pkce)
  * [Requesting a Refresh OAuth Token](https://developers.etsy.com/documentation/essentials/authentication/#requesting-a-refresh-oauth-token)
  * [APIv2 Endpoints and OAuth2 Tokens](https://developers.etsy.com/documentation/essentials/authentication/#apiv2-endpoints-and-oauth2-tokens)
    * [Scopes changed for OAuth 1.0 in the V3 Open API](https://developers.etsy.com/documentation/essentials/authentication/#scopes-changed-for-oauth-10-in-the-v3-open-api)
    * [Exchange OAuth 1.0 Token for OAuth 2.0 Token](https://developers.etsy.com/documentation/essentials/authentication/#exchange-oauth-10-token-for-oauth-20-token)


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

