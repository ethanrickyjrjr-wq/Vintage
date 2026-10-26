# contract probe: Healthchecks.io ping to a nonexistent check, 2026-10-26

## GET https://hc-ping.com/00000000-0000-4000-8000-000000000001
HTTP/1.1 200 OK
server: nginx
date: Mon, 26 Oct 2026 19:38:16 GMT
content-type: text/plain; charset=utf-8
content-length: 14
access-control-allow-origin: *
ping-body-limit: 100000
alt-svc: h3=":443"; ma=86400

OK (not found)