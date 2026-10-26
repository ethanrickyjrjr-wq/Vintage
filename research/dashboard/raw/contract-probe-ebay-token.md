# contract probe: eBay token endpoint, invalid client (no real creds), 2026-10-26

## POST https://api.ebay.com/identity/v1/oauth2/token  grant_type=client_credentials&scope=https%3A%2F%2Fapi.ebay.com%2Foauth%2Fapi_scope  Authorization: Basic base64(bad:bad)
HTTP 401
{"error":"invalid_client","error_description":"client authentication failed"}

## GET https://auth.ebay.com/oauth2/authorize (no params)
HTTP 302 (host answers; consent page needs client_id, redirect_uri=RuName, response_type=code, scope)
