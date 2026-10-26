# contract probe: Pushover messages.json with invalid token/user (nothing delivered), 2026-10-26

## POST https://api.pushover.net/1/messages.json token=bad user=bad message=probe priority=2 (no retry/expire)
HTTP/1.1 400 Bad Request
Date: Mon, 26 Oct 2026 19:37:03 GMT
Content-Type: application/json; charset=utf-8
Transfer-Encoding: chunked
Connection: keep-alive
Server: cloudflare
X-Frame-Options: SAMEORIGIN
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-Download-Options: noopen
X-Permitted-Cross-Domain-Policies: none
Referrer-Policy: strict-origin-when-cross-origin
Access-Control-Allow-Origin: *
Access-Control-Allow-Methods: POST, OPTIONS
Access-Control-Allow-Headers: X-Requested-With, X-Prototype-Version, Origin, Accept, Content-Type, X-CSRF-Token, X-Pushover-App, Authorization
Access-Control-Max-Age: 1728000
Cache-Control: no-cache
X-Request-Id: 69a6ddf8-9aca-4791-bcaf-06286ea1ee53
X-Runtime: 0.005971
cf-cache-status: DYNAMIC
CF-RAY: a50be9d13e6d1f08-MIA

{"token":"invalid","errors":["application token is invalid, see https://pushover.net/api"],"status":0,"request":"69a6ddf8-9aca-4791-bcaf-06286ea1ee53"}