# contract probe: eBay host routing, unauthenticated / invalid-bearer calls, 2026-10-26

## GET https://api.ebay.com/sell/fulfillment/v1/order?limit=1  (Authorization: Bearer invalid)
HTTP 401
{ "errors": [ { "errorId": 1001, "domain": "OAuth", "category": "REQUEST", "message": "Invalid access token", "longMessage": "Invalid access token. Check the value of the Authorization HTTP request header." } ]}

## GET https://apiz.ebay.com/sell/fulfillment/v1/order?limit=1  (Authorization: Bearer invalid)
HTTP 404
{"errors":[{"errorId":2002,"domain":"ACCESS","category":"REQUEST","message":"Resource not found","longMessage":"A resource (URI) associated with the request could not be resolved.","parameters":[{"name":"reason","value":"HTTP 404 Not Found"}]}]}

## GET https://apiz.ebay.com/sell/fulfillment/v1/payment_dispute_summary  (Authorization: Bearer invalid)
HTTP 401
{ "errors": [ { "errorId": 1001, "domain": "OAuth", "category": "REQUEST", "message": "Invalid access token", "longMessage": "Invalid access token. Check the value of the Authorization HTTP request header." } ]}

## GET https://api.ebay.com/sell/fulfillment/v1/payment_dispute_summary  (Authorization: Bearer invalid)
HTTP 404


## GET https://api.ebay.com/sell/finances/v1/transaction?limit=1  (Authorization: Bearer invalid)
HTTP 404


## GET https://apiz.ebay.com/sell/finances/v1/transaction?limit=1  (Authorization: Bearer invalid)
HTTP 401
{ "errors": [ { "errorId": 1001, "domain": "OAuth", "category": "REQUEST", "message": "Invalid access token", "longMessage": "Invalid access token. Check the value of the Authorization HTTP request header." } ]}

## GET https://api.ebay.com/commerce/notification/v1/topic  (Authorization: Bearer invalid)
HTTP 401
{ "errors": [ { "errorId": 1001, "domain": "OAuth", "category": "REQUEST", "message": "Invalid access token", "longMessage": "Invalid access token. Check the value of the Authorization HTTP request header." } ]}

## GET https://apiz.ebay.com/commerce/notification/v1/topic  (Authorization: Bearer invalid)
HTTP 404
{"errors":[{"errorId":2002,"domain":"ACCESS","category":"REQUEST","message":"Resource not found","longMessage":"A resource (URI) associated with the request could not be resolved.","parameters":[{"name":"reason","value":"HTTP 404 Not Found"}]}]}

## GET https://api.ebay.com/buy/browse/v1/item_summary/search?q=lamp&limit=1  (Authorization: Bearer invalid)
HTTP 401
{ "errors": [ { "errorId": 1001, "domain": "OAuth", "category": "REQUEST", "message": "Invalid access token", "longMessage": "Invalid access token. Check the value of the Authorization HTTP request header." } ]}

## GET https://apiz.ebay.com/buy/browse/v1/item_summary/search?q=lamp&limit=1  (Authorization: Bearer invalid)
HTTP 404
{"errors":[{"errorId":2002,"domain":"ACCESS","category":"REQUEST","message":"Resource not found","longMessage":"A resource (URI) associated with the request could not be resolved.","parameters":[{"name":"reason","value":"HTTP 404 Not Found"}]}]}

## GET https://api.ebay.com/sell/inventory/v1/inventory_item?limit=1  (Authorization: Bearer invalid)
HTTP 401
{ "errors": [ { "errorId": 1001, "domain": "OAuth", "category": "REQUEST", "message": "Invalid access token", "longMessage": "Invalid access token. Check the value of the Authorization HTTP request header." } ]}

## GET https://api.ebay.com/sell/feed/v1/inventory_task  (Authorization: Bearer invalid)
HTTP 401
{ "errors": [ { "errorId": 1001, "domain": "OAuth", "category": "REQUEST", "message": "Invalid access token", "longMessage": "Invalid access token. Check the value of the Authorization HTTP request header." } ]}
