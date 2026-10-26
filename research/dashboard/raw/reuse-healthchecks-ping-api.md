Toggle navigation [ ![Healthchecks.io](https://healthchecks.io/static/img/logo-rounded-ua2.svg) ](https://healthchecks.io/)
  * [Pricing](https://healthchecks.io/pricing/)
  * [Docs](https://healthchecks.io/docs/)
  * [Blog](https://blog.healthchecks.io/)
  * [About](https://healthchecks.io/about/)
  * [Log In](https://healthchecks.io/accounts/login/)


  * Healthchecks.io
  * [Introduction](https://healthchecks.io/docs/)
  * [Configuring checks](https://healthchecks.io/docs/configuring_checks/)
  * [Configuring notifications](https://healthchecks.io/docs/configuring_notifications/)
  * [Projects and teams](https://healthchecks.io/docs/projects_teams/)
  * [Badges](https://healthchecks.io/docs/badges/)
  * [FAQ](https://healthchecks.io/faq/)
  * API
  * [Pinging API](https://healthchecks.io/docs/http_api/)
  * [Management API](https://healthchecks.io/docs/api/)
  * [Slug URLs](https://healthchecks.io/docs/slug_urls/)
  * Guides
  * [Monitoring cron jobs](https://healthchecks.io/docs/monitoring_cron_jobs/)
  * [Monitoring Systemd tasks](https://healthchecks.io/docs/monitoring_systemd_tasks/)
  * [Signaling failures](https://healthchecks.io/docs/signaling_failures/)
  * [Measuring script run time](https://healthchecks.io/docs/measuring_script_run_time/)
  * [Attaching logs](https://healthchecks.io/docs/attaching_logs/)
  * [Cloning checks](https://healthchecks.io/docs/cloning_checks/)
  * [Auto provisioning](https://healthchecks.io/docs/autoprovisioning/)
  * [Configuring Prometheus](https://healthchecks.io/docs/configuring_prometheus/)
  * Pinging Examples
  * [Reliability tips](https://healthchecks.io/docs/reliability_tips/)
  * [Shell scripts](https://healthchecks.io/docs/bash/)
  * [Arduino](https://healthchecks.io/docs/arduino/)
  * [Network Routers](https://healthchecks.io/docs/network_routers/)
  * [C#](https://healthchecks.io/docs/csharp/)
  * [Email](https://healthchecks.io/docs/email/)
  * [GitHub Actions](https://healthchecks.io/docs/github_actions/)
  * [Go](https://healthchecks.io/docs/go/)
  * [Javascript](https://healthchecks.io/docs/javascript/)
  * [PHP](https://healthchecks.io/docs/php/)
  * [PowerShell](https://healthchecks.io/docs/powershell/)
  * [Python](https://healthchecks.io/docs/python/)
  * [Ruby](https://healthchecks.io/docs/ruby/)
  * Developer Tools
  * [Third-party resources](https://healthchecks.io/docs/resources/)
  * Self-hosted
  * [Overview](https://healthchecks.io/docs/self_hosted/)
  * [Configuration](https://healthchecks.io/docs/self_hosted_configuration/)
  * [Running with Docker](https://healthchecks.io/docs/self_hosted_docker/)
  * Reference
  * [Cron syntax cheatsheet](https://healthchecks.io/docs/cron/)
  * [Compared to Sentry](https://healthchecks.io/docs/healthchecks_sentry_comparison/)
  * [Compared to Cronitor](https://healthchecks.io/docs/healthchecks_cronitor_comparison/)


# Pinging API
With the Pinging API, you can signal **success** , **start** , **failure** , and **log** events from your systems.
## General Notes
All ping endpoints support:
  * HTTP and HTTPS
  * HTTP 1.0, HTTP 1.1, and HTTP 2
  * IPv4 and IPv6
  * HEAD, GET, and POST request methods. For HTTP POST requests, clients can optionally include diagnostic information in the request body. If the request body looks like a UTF-8 string, Healthchecks.io stores the request body (limited to the first 100 kB for each received ping).


Successful responses will have the "200 OK" HTTP response status code and a short "OK" string in the response body.
## UUIDs and Slugs
Each Pinging API request needs to identify a check uniquely. Healthchecks.io supports two ways of identifying a check: by the check's UUID or by a combination of the project's Ping Key and the check's slug.
**Check's UUID** is automatically assigned when the check is created. It is immutable. You cannot replace the automatically assigned UUID with a manually chosen one. When you delete a check, you lose its UUID and cannot get it back.
You can look up the UUIDs of your checks in web UI or via [Management API](https://healthchecks.io/docs/api/) calls.
**Check's slug** can be chosen by the user. The slug should only contain the following characters: `a-z`, `0-9`, hyphens, and underscores. A common practice is to derive the slug from the check's name (for example, a check named "Database Backup" might have a slug "database-backup"), but the user is free to pick arbitrary slug values.
Check's slug **can be changed** by the user, from the web interface or by using [Management API](https://healthchecks.io/docs/api/) calls.
Check's slug is **not guaranteed to be unique**. If you make a Pinging API request using a non-unique slug, Healthchecks.io will return the "409 Conflict" HTTP status code and ignore the request.
Slug URLs optionally support **auto-provisioning** : if you make a Pinging API request to a slug with no corresponding check, Healthchecks.io will create the check automatically. Auto-provisioning is off by default. To enable it, add a `create=1` query parameter to the ping URL.
## Rate Limits
Please be nice to our servers. Do not ping a check more frequently than is necessary. If you ping a check more than 5 times per minute, some of the requests may get rate limited and not recorded to the database. In extreme cases we will block the client's IP address.
## Endpoints  
| Endpoint Name  | Endpoint Address  |  
| --- | --- |  
| [Success (UUID)](https://healthchecks.io/docs/http_api/#success-uuid)  | `https://hc-ping.com/<uuid>`  |  
| [Start (UUID)](https://healthchecks.io/docs/http_api/#start-uuid)  | `https://hc-ping.com/<uuid>/start`  |  
| [Failure (UUID)](https://healthchecks.io/docs/http_api/#fail-uuid)  | `https://hc-ping.com/<uuid>/fail`  |  
| [Log (UUID)](https://healthchecks.io/docs/http_api/#log-uuid)  | `https://hc-ping.com/<uuid>/log`  |  
| [Report script's exit status (UUID)](https://healthchecks.io/docs/http_api/#exitcode-uuid)  | `https://hc-ping.com/<uuid>/<exit-status>`  |  
| [Success (slug)](https://healthchecks.io/docs/http_api/#success-slug)  | `https://hc-ping.com/<ping-key>/<slug>`  |  
| [Start (slug)](https://healthchecks.io/docs/http_api/#start-slug)  | `https://hc-ping.com/<ping-key>/<slug>/start`  |  
| [Failure (slug)](https://healthchecks.io/docs/http_api/#fail-slug)  | `https://hc-ping.com/<ping-key>/<slug>/fail`  |  
| [Log (slug)](https://healthchecks.io/docs/http_api/#log-slug)  | `https://hc-ping.com/<ping-key>/<slug>/log`  |  
| [Report script's exit status (slug)](https://healthchecks.io/docs/http_api/#exitcode-slug)  | `https://hc-ping.com/<ping-key>/<slug>/<exit-status>`  |  
## Send a "success" Signal Using UUID

```
HEAD|GET|POST https://hc-ping.com/<uuid>

```

Signals to Healthchecks.io that the job has been completed successfully (or a continuously running process is still running and healthy).
Healthchecks.io identifies the check by the UUID value included in the URL.
The response may optionally contain a `Ping-Body-Limit: <n>` response header. If this header is present, its value is an integer, and it specifies how many bytes from the request body Healthchecks.io will store per request. For example, if n=100, but the client sends 123 bytes in the request body, Healthchecks.io will store the first 100 bytes and ignore the remaining 23. The client can use this header to decide how much data to send in the request bodies of subsequent requests.
### Query Parameters 

rid=<uuid>
    
Optional, specifies a run ID of this ping. If run ID is specified, Healthchecks.io uses it to match the correct corresponding start ping for this ping and calculate an accurate duration. The value must be a client-picked UUID in the canonical textual representation.
Example: `rid=123e4567-e89b-12d3-a456-426614174000`.
### Response Codes 

200 OK
    The request succeeded. 

200 OK (not found)
    Could not find a check with the specified UUID. 

200 OK (rate limited)
    Rate limit exceeded, request was ignored. Please do not ping a single check more than 5 times per minute. 

400 invalid url format
    The URL does not match the expected format.
**Example**

```
GET /5bf66975-d4c7-4bf5-bcc8-b8d8a82ea278 HTTP/1.0
Host: hc-ping.com

```


```
HTTP/1.1 200 OK
Server: nginx
Date: Wed, 29 Jan 2020 09:58:23 GMT
Content-Type: text/plain; charset=utf-8
Content-Length: 2
Connection: close
Access-Control-Allow-Origin: *
Ping-Body-Limit: 100000

OK

```

## Send a "start" Signal Using UUID

```
HEAD|GET|POST https://hc-ping.com/<uuid>/start

```

Sends a "job has started!" message to Healthchecks.io. Sending a "start" signal is optional, but it enables a few extra features:
  * Healthchecks.io will measure and display job execution times
  * Healthchecks.io will detect if the job runs longer than its configured grace time


Healthchecks.io identifies the check by the UUID value included in the URL.
The response may optionally contain a `Ping-Body-Limit: <n>` response header. If this header is present, its value is an integer, and it specifies how many bytes from the request body Healthchecks.io will store per request. For example, if n=100, but the client sends 123 bytes in the request body, Healthchecks.io will store the first 100 bytes and ignore the remaining 23. The client can use this header to decide how much data to send in the request bodies of subsequent requests.
### Query Parameters 

rid=<uuid>
    
Optional, specifies a run ID of this ping. If run ID is specified, Healthchecks.io uses it to match the correct corresponding completion ping for this ping and calculate an accurate duration. The value must be a client-picked UUID in the canonical textual representation.
Example: `rid=123e4567-e89b-12d3-a456-426614174000`.
### Response Codes 

200 OK
    The request succeeded. 

200 OK (not found)
    Could not find a check with the specified UUID. 

200 OK (rate limited)
    Rate limit exceeded, request was ignored. Please do not ping a single check more than 5 times per minute. 

400 invalid url format
    The URL does not match the expected format.
**Example**

```
GET /5bf66975-d4c7-4bf5-bcc8-b8d8a82ea278/start HTTP/1.0
Host: hc-ping.com

```


```
HTTP/1.1 200 OK
Server: nginx
Date: Wed, 29 Jan 2020 09:58:23 GMT
Content-Type: text/plain; charset=utf-8
Content-Length: 2
Connection: close
Access-Control-Allow-Origin: *
Ping-Body-Limit: 100000

OK

```

## Send a "failure" Signal Using UUID

```
HEAD|GET|POST https://hc-ping.com/<uuid>/fail

```

Signals to Healthchecks.io that the job has failed. Actively signaling a failure minimizes the delay from your monitored service failing to you receiving an alert.
Healthchecks.io identifies the check by the UUID value included in the URL.
The response may optionally contain a `Ping-Body-Limit: <n>` response header. If this header is present, its value is an integer, and it specifies how many bytes from the request body Healthchecks.io will store per request. For example, if n=100, but the client sends 123 bytes in the request body, Healthchecks.io will store the first 100 bytes and ignore the remaining 23. The client can use this header to decide how much data to send in the request bodies of subsequent requests.
### Query Parameters 

rid=<uuid>
    
Optional, specifies a run ID of this ping. If run ID is specified, Healthchecks.io uses it to match the correct corresponding start ping for this ping and calculate an accurate duration. The value must be a client-picked UUID in the canonical textual representation.
Example: `rid=123e4567-e89b-12d3-a456-426614174000`.
### Response Codes 

200 OK
    The request succeeded. 

200 OK (not found)
    Could not find a check with the specified UUID. 

200 OK (rate limited)
    Rate limit exceeded, request was ignored. Please do not ping a single check more than 5 times per minute. 

400 invalid url format
    The URL does not match the expected format.
**Example**

```
GET /5bf66975-d4c7-4bf5-bcc8-b8d8a82ea278/fail HTTP/1.0
Host: hc-ping.com

```


```
HTTP/1.1 200 OK
Server: nginx
Date: Wed, 29 Jan 2020 09:58:23 GMT
Content-Type: text/plain; charset=utf-8
Content-Length: 2
Connection: close
Access-Control-Allow-Origin: *
Ping-Body-Limit: 100000

OK

```

## Send a "log" Signal Using UUID

```
HEAD|GET|POST https://hc-ping.com/<uuid>/log

```

Sends logging information to Healthchecks.io without signaling success or failure. Healthchecks.io will log the event and display it in the check's "Events" section with the "Log" label. The check's status will remain the same.
Healthchecks.io identifies the check by the UUID value included in the URL.
The response may optionally contain a `Ping-Body-Limit: <n>` response header. If this header is present, its value is an integer, and it specifies how many bytes from the request body Healthchecks.io will store per request. For example, if n=100, but the client sends 123 bytes in the request body, Healthchecks.io will store the first 100 bytes and ignore the remaining 23. The client can use this header to decide how much data to send in the request bodies of subsequent requests.
### Query Parameters 

rid=<uuid>
    
Optional, specifies a run ID of this ping. The value must be a client-picked UUID in the canonical textual representation.
Example: `rid=123e4567-e89b-12d3-a456-426614174000`.
### Response Codes 

200 OK
    The request succeeded. 

404 not found
    Could not find a check with the specified UUID.
**Example**

```
POST /5bf66975-d4c7-4bf5-bcc8-b8d8a82ea278/log HTTP/1.1
Host: hc-ping.com
Content-Type: text/plain
Content-Length: 11

Hello World

```


```
HTTP/1.1 200 OK
Server: nginx
Date: Wed, 29 Jan 2020 09:58:23 GMT
Content-Type: text/plain; charset=utf-8
Content-Length: 2
Connection: close
Access-Control-Allow-Origin: *
Ping-Body-Limit: 100000

OK

```

## Report Script's Exit Status (Using UUID)

```
HEAD|GET|POST https://hc-ping.com/<uuid>/<exit-status>

```

Sends a success or failure signal depending on the exit status included in the URL. The exit status is a 0-255 integer. Healthchecks.io interprets 0 as a success and all other values as a failure.
Healthchecks.io identifies the check by the UUID value included in the URL.
The response may optionally contain a `Ping-Body-Limit: <n>` response header. If this header is present, its value is an integer, and it specifies how many bytes from the request body Healthchecks.io will store per request. For example, if n=100, but the client sends 123 bytes in the request body, Healthchecks.io will store the first 100 bytes and ignore the remaining 23. The client can use this header to decide how much data to send in the request bodies of subsequent requests.
### Query Parameters 

rid=<uuid>
    
Optional, specifies a run ID of this ping. If run ID is specified, Healthchecks.io uses it to match the correct corresponding start ping for this ping and calculate an accurate duration. The value must be a client-picked UUID in the canonical textual representation.
Example: `rid=123e4567-e89b-12d3-a456-426614174000`.
### Response Codes 

200 OK
    The request succeeded. 

200 OK (not found)
    Could not find a check with the specified UUID. 

200 OK (rate limited)
    Rate limit exceeded, request was ignored. Please do not ping a single check more than 5 times per minute. 

400 invalid url format
    The URL does not match the expected format.
**Example**

```
GET /5bf66975-d4c7-4bf5-bcc8-b8d8a82ea278/1 HTTP/1.0
Host: hc-ping.com

```


```
HTTP/1.1 200 OK
Server: nginx
Date: Wed, 29 Jan 2020 09:58:23 GMT
Content-Type: text/plain; charset=utf-8
Content-Length: 2
Connection: close
Access-Control-Allow-Origin: *
Ping-Body-Limit: 100000

OK

```

## Send a "success" Signal (Using Slug)

```
HEAD|GET|POST https://hc-ping.com/<ping-key>/<slug>

```

Signals to Healthchecks.io that the job has been completed successfully (or a continuously running process is still running and healthy).
Healthchecks.io identifies the check by project's ping key and check's slug included in the URL. The slug should consist of lowercase ASCII letters (`a-z`), digits (`0-9`), underscores (`_`), and hyphens (`-`) only.
The response may optionally contain a `Ping-Body-Limit: <n>` response header. If this header is present, its value is an integer, and it specifies how many bytes from the request body Healthchecks.io will store per request. For example, if n=100, but the client sends 123 bytes in the request body, Healthchecks.io will store the first 100 bytes and ignore the remaining 23. The client can use this header to decide how much data to send in the request bodies of subsequent requests.
### Query Parameters 

create=0|1
    
Optional, default "0". If set to "1", and if the slug in the URL does not match any existing check in the project, Healthchecks.io creates a new check automatically.
Example: `create=1` 

rid=<uuid>
    
Optional, specifies a run ID of this ping. If run ID is specified, Healthchecks.io uses it to match the correct corresponding start ping for this ping, and calculate an accurate duration. The value must be a client-picked UUID in the canonical textual representation.
Example: `rid=123e4567-e89b-12d3-a456-426614174000`.
### Response Codes 

200 OK
    The request succeeded. 

201 Created
    A new check was automatically created, the request succeeded. 

400 invalid url format
    The URL does not match the expected format. 

404 not found
    Could not find a check with the specified ping key and slug combination. 

409 ambiguous slug
    Ambiguous, the slug matched multiple checks. 

429 rate limit exceeded
    Rate limit exceeded. Please do not ping a single check more than 5 times per minute.
**Example**

```
GET /fqOOd6-F4MMNuCEnzTU01w/database-backup HTTP/1.0
Host: hc-ping.com

```


```
HTTP/1.1 200 OK
Server: nginx
Date: Wed, 29 Jan 2020 09:58:23 GMT
Content-Type: text/plain; charset=utf-8
Content-Length: 2
Connection: close
Access-Control-Allow-Origin: *
Ping-Body-Limit: 100000

OK

```

## Send a "start" Signal (Using Slug)

```
HEAD|GET|POST https://hc-ping.com/<ping-key>/<slug>/start

```

Sends a "job has started!" message to Healthchecks.io. Sending a "start" signal is optional, but it enables a few extra features:
  * Healthchecks.io will measure and display job execution times
  * Healthchecks.io will detect if the job runs longer than its configured grace time


Healthchecks.io identifies the check by project's ping key and check's slug included in the URL. The slug should consist of lowercase ASCII letters (`a-z`), digits (`0-9`), underscores (`_`), and hyphens (`-`) only.
The response may optionally contain a `Ping-Body-Limit: <n>` response header. If this header is present, its value is an integer, and it specifies how many bytes from the request body Healthchecks.io will store per request. For example, if n=100, but the client sends 123 bytes in the request body, Healthchecks.io will store the first 100 bytes, and ignore the remaining 23. The client can use this header to decide how much data to send in the request bodies of subsequent requests.
### Query Parameters 

create=0|1
    
Optional, default "0". If set to "1", and if the slug in the URL does not match any existing check in the project, Healthchecks.io creates a new check automatically.
Example: `create=1` 

rid=<uuid>
    
Optional, specifies a run ID of this ping. If run ID is specified, Healthchecks.io uses it to match the correct corresponding completion ping for this ping, and calculate an accurate duration. The value must be a client-picked UUID in the canonical textual representation.
Example: `rid=123e4567-e89b-12d3-a456-426614174000`.
### Response Codes 

200 OK
    The request succeeded. 

201 Created
    A new check was automatically created, the request succeeded. 

400 invalid url format
    The URL does not match the expected format. 

404 not found
    Could not find a check with the specified ping key and slug combination. 

409 ambiguous slug
    Ambiguous, the slug matched multiple checks. 

429 rate limit exceeded
    Rate limit exceeded. Please do not ping a single check more than 5 times per minute.
**Example**

```
GET /fqOOd6-F4MMNuCEnzTU01w/database-backup/start HTTP/1.0
Host: hc-ping.com

```


```
HTTP/1.1 200 OK
Server: nginx
Date: Wed, 29 Jan 2020 09:58:23 GMT
Content-Type: text/plain; charset=utf-8
Content-Length: 2
Connection: close
Access-Control-Allow-Origin: *
Ping-Body-Limit: 100000

OK

```

## Send a "failure" Signal (Using slug)

```
HEAD|GET|POST https://hc-ping.com/<ping-key/<slug>/fail

```

Signals to Healthchecks.io that the job has failed. Actively signaling a failure minimizes the delay from your monitored service failing to you receiving an alert.
Healthchecks.io identifies the check by project's ping key and check's slug included in the URL. The slug should consist of lowercase ASCII letters (`a-z`), digits (`0-9`), underscores (`_`), and hyphens (`-`) only.
The response may optionally contain a `Ping-Body-Limit: <n>` response header. If this header is present, its value is an integer, and it specifies how many bytes from the request body Healthchecks.io will store per request. For example, if n=100, but the client sends 123 bytes in the request body, Healthchecks.io will store the first 100 bytes, and ignore the remaining 23. The client can use this header to decide how much data to send in the request bodies of subsequent requests.
### Query Parameters 

create=0|1
    
Optional, default "0". If set to "1", and if the slug in the URL does not match any existing check in the project, Healthchecks.io creates a new check automatically.
Example: `create=1` 

rid=<uuid>
    
Optional, specifies a run ID of this ping. If run ID is specified, Healthchecks.io uses it to match the correct corresponding start ping for this ping, and calculate an accurate duration. The value must be a client-picked UUID in the canonical textual representation.
Example: `rid=123e4567-e89b-12d3-a456-426614174000`.
### Response Codes 

200 OK
    The request succeeded. 

201 Created
    A new check was automatically created, the request succeeded. 

400 invalid url format
    The URL does not match the expected format. 

404 not found
    Could not find a check with the specified ping key and slug combination. 

409 ambiguous slug
    Ambiguous, the slug matched multiple checks. 

429 rate limit exceeded
    Rate limit exceeded. Please do not ping a single check more than 5 times per minute.
**Example**

```
GET /fqOOd6-F4MMNuCEnzTU01w/database-backup/fail HTTP/1.0
Host: hc-ping.com

```


```
HTTP/1.1 200 OK
Server: nginx
Date: Wed, 29 Jan 2020 09:58:23 GMT
Content-Type: text/plain; charset=utf-8
Content-Length: 2
Connection: close
Access-Control-Allow-Origin: *
Ping-Body-Limit: 100000

OK

```

## Send a "log" Signal (Using slug)

```
HEAD|GET|POST https://hc-ping.com/<ping-key/<slug>/log

```

Sends logging information to Healthchecks.io without signaling success or failure. Healthchecks.io will log the event and display it in check's "Events" section with the "Log" label. The check's status will not change.
Healthchecks.io identifies the check by project's ping key and check's slug included in the URL. The slug should consist of lowercase ASCII letters (`a-z`), digits (`0-9`), underscores (`_`), and hyphens (`-`) only.
The response may optionally contain a `Ping-Body-Limit: <n>` response header. If this header is present, its value is an integer, and it specifies how many bytes from the request body Healthchecks.io will store per request. For example, if n=100, but the client sends 123 bytes in the request body, Healthchecks.io will store the first 100 bytes, and ignore the remaining 23. The client can use this header to decide how much data to send in the request bodies of subsequent requests.
### Query Parameters 

create=0|1
    
Optional, default "0". If set to "1", and if the slug in the URL does not match any existing check in the project, Healthchecks.io creates a new check automatically.
Example: `create=1` 

rid=<uuid>
    
Optional, specifies a run ID of this ping. The value must be a client-picked UUID in the canonical textual representation.
Example: `rid=123e4567-e89b-12d3-a456-426614174000`.
### Response Codes 

200 OK
    The request succeeded. 

201 Created
    A new check was automatically created, the request succeeded. 

404 not found
    Could not find a check with the specified ping key and slug combination. 

409 ambiguous slug
    Ambiguous, the slug matched multiple checks.
**Example**

```
POST /fqOOd6-F4MMNuCEnzTU01w/database-backup/log HTTP/1.1
Host: hc-ping.com
Content-Type: text/plain
Content-Length: 11

Hello World

```


```
HTTP/1.1 200 OK
Server: nginx
Date: Wed, 29 Jan 2020 09:58:23 GMT
Content-Type: text/plain; charset=utf-8
Content-Length: 2
Connection: close
Access-Control-Allow-Origin: *
Ping-Body-Limit: 100000

OK

```

## Report Script's Exit Status (Using Slug)

```
HEAD|GET|POST https://hc-ping.com/<ping-key>/<slug>/<exit-status>

```

Sends a success or failure signal depending on the exit status included in the URL. The exit status is a 0-255 integer. Healthchecks.io interprets 0 as a success and all other values as a failure.
Healthchecks.io identifies the check by project's ping key and check's slug included in the URL. The slug should consist of lowercase ASCII letters (`a-z`), digits (`0-9`), underscores (`_`), and hyphens (`-`) only.
The response may optionally contain a `Ping-Body-Limit: <n>` response header. If this header is present, its value is an integer, and it specifies how many bytes from the request body Healthchecks.io will store per request. For example, if n=100, but the client sends 123 bytes in the request body, Healthchecks.io will store the first 100 bytes, and ignore the remaining 23. The client can use this header to decide how much data to send in the request bodies of subsequent requests.
### Query Parameters 

create=0|1
    
Optional, default "0". If set to "1", and if the slug in the URL does not match any existing check in the project, Healthchecks.io creates a new check automatically.
Example: `create=1` 

rid=<uuid>
    
Optional, specifies a run ID of this ping. If run ID is specified, Healthchecks.io uses it to match the correct corresponding start ping for this ping, and calculate an accurate duration. The value must be a client-picked UUID in the canonical textual representation.
Example: `rid=123e4567-e89b-12d3-a456-426614174000`.
### Response Codes 

200 OK
    The request succeeded. 

201 Created
    A new check was automatically created, the request succeeded. 

400 invalid url format
    The URL does not match the expected format. 

404 not found
    Could not find a project matching the specified ping key. 

409 ambiguous slug
    Ambiguous, the slug matched multiple checks. 

429 rate limit exceeded
    Rate limit exceeded. Please do not ping a single check more than 5 times per minute.
**Example**

```
GET /fqOOd6-F4MMNuCEnzTU01w/database-backup/1 HTTP/1.0
Host: hc-ping.com

```


```
HTTP/1.1 200 OK
Server: nginx
Date: Wed, 29 Jan 2020 09:58:23 GMT
Content-Type: text/plain; charset=utf-8
Content-Length: 2
Connection: close
Access-Control-Allow-Origin: *
Ping-Body-Limit: 100000

OK

```

  * © 2015-2026 SIA Monkey See Monkey Do
  * [Terms](https://healthchecks.io/terms/)
  * [Privacy](https://healthchecks.io/privacy/)
  * [Pricing](https://healthchecks.io/pricing/)
  * [FAQ](https://healthchecks.io/faq/)
  * [API](https://healthchecks.io/docs/api/)
  * [Blog](https://blog.healthchecks.io)
  * [Contact](https://healthchecks.io/about/)
  * [Status](https://status.healthchecks.io/)



