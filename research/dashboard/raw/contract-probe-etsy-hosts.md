# contract probe: Etsy hosts, invalid key, 2026-10-26

## GET https://api.etsy.com/v3/application/openapi-ping (x-api-key: bad:bad)
HTTP 403
{"error":"API key not found or not active, or incorrect shared secret for API key."}


## GET https://openapi.etsy.com/v3/application/openapi-ping (x-api-key: bad:bad)
HTTP 403
{"error":"API key not found or not active, or incorrect shared secret for API key."}


## POST https://api.etsy.com/v3/public/oauth/token grant_type=refresh_token client_id=bad refresh_token=bad
HTTP 403
{"error":"API key not found or not active, or incorrect shared secret for API key."}


## POST https://openapi.etsy.com/v3/public/oauth/token grant_type=refresh_token client_id=bad refresh_token=bad
HTTP 403
{"error":"API key not found or not active, or incorrect shared secret for API key."}


## POST api.etsy.com token with grant_type=refresh_code (the doc-prose variant)
HTTP 403
{"error":"API key not found or not active, or incorrect shared secret for API key."}

