![](https://developers.buffer.com/image/banner-line.svg) ![](https://developers.buffer.com/image/banner-dot.svg) ![](https://developers.buffer.com/image/banner-line.svg) ![](https://developers.buffer.com/image/banner-dot.svg)
![Buffer Commit](https://developers.buffer.com/image/banner-commit-logo.svg)
Join Buffer’s first Build Contest. October 28 - November 13
[Register](https://buffer.com/api/commit?utm_source=buffer&utm_medium=banner&utm_campaign=buffer_commit&utm_content=developer_portal)
[ ![Buffer API](https://developers.buffer.com/logo.svg) ](https://developers.buffer.com/index.html)
Search docs... `⌘K`
[ ](https://discord.gg/9skbzTz6vQ "Discord")
[API Status](https://status.buffer.com/) [Get API Key](https://publish.buffer.com/settings/api)
Guides 
[Introduction](https://developers.buffer.com/guides/introduction.html) [Quick Start](https://developers.buffer.com/guides/getting-started.html) [Authentication](https://developers.buffer.com/guides/authentication.html) [Building Apps](https://developers.buffer.com/guides/building-apps.html) [Your First Post](https://developers.buffer.com/guides/your-first-post.html) [GraphQL for REST Devs](https://developers.buffer.com/guides/graphql-intro.html) [REST API Migration](https://developers.buffer.com/guides/rest-migration.html) [Data Model](https://developers.buffer.com/guides/data-model.html) [Posts & Scheduling](https://developers.buffer.com/guides/posts-and-scheduling.html) [Ideas](https://developers.buffer.com/guides/ideas.html) [Content Items Experimental](https://developers.buffer.com/guides/content-items.html) [Hosting Media](https://developers.buffer.com/guides/hosting-media.html) [Tags Experimental](https://developers.buffer.com/guides/tags.html) [Post Metrics](https://developers.buffer.com/guides/post-metrics.html) [API Standards](https://developers.buffer.com/guides/api-standards.html) [Character Limits](https://developers.buffer.com/guides/character-limits.html) [Error Handling](https://developers.buffer.com/guides/error-handling.html) [Rate Limits](https://developers.buffer.com/guides/api-limits.html) [Pagination](https://developers.buffer.com/guides/pagination.html) [Efficient API Usage](https://developers.buffer.com/guides/efficient-api-usage.html)
Examples 
[Aggregate Post Metrics](https://developers.buffer.com/examples/aggregate-post-metrics.html) [Create Draft Post](https://developers.buffer.com/examples/create-draft-post.html) [Create Idea](https://developers.buffer.com/examples/create-idea.html) [Create Image Post](https://developers.buffer.com/examples/create-image-post.html) [Create Instagram Post With User Tags](https://developers.buffer.com/examples/create-instagram-post-with-user-tags.html) [Create Scheduled Post](https://developers.buffer.com/examples/create-scheduled-post.html) [Create Tag Experimental](https://developers.buffer.com/examples/create-tag.html) [Create Text Post](https://developers.buffer.com/examples/create-text-post.html) [Create Threaded Post](https://developers.buffer.com/examples/create-threaded-post.html) [Create Video Post](https://developers.buffer.com/examples/create-video-post.html) [Delete Tag Experimental](https://developers.buffer.com/examples/delete-tag.html) [Get Channel](https://developers.buffer.com/examples/get-channel.html) [Get Channels](https://developers.buffer.com/examples/get-channels.html) [Get Filtered Channels](https://developers.buffer.com/examples/get-filtered-channels.html) [Get Organizations](https://developers.buffer.com/examples/get-organizations.html) [Get Paginated Posts](https://developers.buffer.com/examples/get-paginated-posts.html) [Get Post Metrics](https://developers.buffer.com/examples/get-post-metrics.html) [Get Posts For Channels](https://developers.buffer.com/examples/get-posts-for-channels.html) [Get Posts With Assets](https://developers.buffer.com/examples/get-posts-with-assets.html) [Get Posts With Metrics](https://developers.buffer.com/examples/get-posts-with-metrics.html) [Get Quarterly Performance Report](https://developers.buffer.com/examples/get-quarterly-performance-report.html) [Get Scheduled Posts](https://developers.buffer.com/examples/get-scheduled-posts.html) [Get Tag Experimental](https://developers.buffer.com/examples/get-tag.html) [Get Tags Experimental](https://developers.buffer.com/examples/get-tags.html) [Update Tag Experimental](https://developers.buffer.com/examples/update-tag.html)
[ CLI](https://developers.buffer.com/guides/cli.html) [ Integrations](https://developers.buffer.com/guides/integrations.html) [ Explorer](https://developers.buffer.com/explorer.html) [ Changelog](https://developers.buffer.com/changelog.html) [ Roadmap](https://developers.buffer.com/roadmap.html) [ Legacy Apps](https://buffer.com/developers/legacy-api)
API Reference
[ Account](https://developers.buffer.com/reference.html#account)[ Organizations](https://developers.buffer.com/reference.html#organizations)[ Channels](https://developers.buffer.com/reference.html#channels)[ Tags](https://developers.buffer.com/reference.html#tags)[ Posts](https://developers.buffer.com/reference.html#posts)[ Ideas](https://developers.buffer.com/reference.html#ideas)[ Other](https://developers.buffer.com/reference.html#other)
API DesignRate Limits
# Rate Limits
Copy Page
Ask AI assistant Chat with the docs AI assistant Copy page Copy this page as Markdown View as Markdown Open this page as plain Markdown Open in Claude Ask Claude about this page Open in ChatGPT Ask ChatGPT about this page Open in Perplexity Ask Perplexity about this page
To ensure that Buffer API stays healthy, performant, and fair for everyone, Buffer applies API rate limits. The limits for your API keys and MCP connections depend on your Buffer plan. Each app client you build has its own limits, which grow with the number of Buffer users who authorize it. We ask developers to use suggested industry-standard techniques for honoring enforced rate limits and re-trying requests responsibly.
## Buffer API Rate Limits[](https://developers.buffer.com/guides/api-limits.html#buffer-api-rate-limits)
Your Buffer plan sets how many API keys and app clients you can create, and how many requests your API keys and MCP connections can make in each 15-minute, 24-hour, and 30-day window.  
| Feature  | Free  | Essentials  | Team  |  
| --- | --- | --- | --- |  
| API Keys  | 1  | 3  | 5  |  
| App Clients  | 1  | 3  | 5  |  
| 15-min limit  | 150  | 450  | 1,500  |  
| 24-hr limit  | 600  | 1,800  | 6,000  |  
| 30-day limit  | 1,000 per channel, up to 3,000  | 3,000 per channel, up to 30,000  | 10,000 per channel, up to 100,000  |  
The 30-day limit grows with the number of unlocked channels in your organization, up to your plan's maximum. For example, a Free organization with 2 channels gets 2,000 requests per 30 days, and an Essentials organization with 5 channels gets 15,000.
All of your API keys and MCP connections share one set of limits. They aren't applied per key, so creating another key doesn't give you more requests.
### App client limits[](https://developers.buffer.com/guides/api-limits.html#app-client-limits)
Each app client has its own limits, separate from your API keys and from your plan. They grow with the number of Buffer users who have authorized your app:  
| Window  | Base  | Per authorized user  |  
| --- | --- | --- |  
| 15 minutes  | 100  | 10  |  
| 24 hours  | 500  | 25  |  
| 30 days  | 15,000  | 100  |  
An authorized user is a Buffer account that has authorized your app. Up to 1,000 authorized users count toward the limits. For example, an app authorized by 40 users can make 500 requests per 15 minutes, 1,500 per 24 hours, and 19,000 per 30 days. When someone new authorizes your app, the limits grow within a few minutes.
> Does your integration require higher limits? Reach out to developersupport@buffer.com.
## Using Response Headers to check Rate Limits[](https://developers.buffer.com/guides/api-limits.html#using-response-headers-to-check-rate-limits)
Response headers provide you the details you can use to build the back-off logic. Watching `r` (requests remaining) decrease lets you apply client-side throttle, spread the work out, or pause a job before a `429` happens, rather than finding out about a limit only when a request fails.
Every response includes rate-limit information as structured `RateLimit` headers. Each of the three windows - 15-minute, 24-hour, and 30-day - contributes one policy, so you'll see three of each header:
Copy Copied! 
```
RateLimit:        "150-in-15min";r=98;t=897
RateLimit:        "600-in-1day";r=598;t=86397
RateLimit:        "3000-in-30days";r=2969;t=696980
RateLimit-Policy: "150-in-15min";q=150;w=900;pk=:ZjJjZjVmNzM5M2Zm:
RateLimit-Policy: "600-in-1day";q=600;w=86400;pk=:ZjJjZjVmNzM5M2Zm:
RateLimit-Policy: "3000-in-30days";q=3000;w=2592000;pk=:ZjJjZjVmNzM5M2Zm:
```

> The numbers above are from one example response. The quotas you see depend on your plan.
`RateLimit` reports the live status of each policy, and `RateLimit-Policy` describes the limit behind it:  
| Header  | Field  | What it means  |  
| --- | --- | --- |  
| `RateLimit`  | `r`  | The requests remaining.  |  
| `RateLimit`  | `t`  | The seconds until that window resets.  |  
| `RateLimit-Policy`  | `q`  | The quota.  |  
| `RateLimit-Policy`  | `w`  | The window length in seconds.  |  
| `RateLimit-Policy`  | `pk`  | The partition key identifying your rate-limit bucket.  |  
Policy names like `150-in-15min` are generated from your quota and window, so they change with your plan. Match a policy by its window length (`w`) rather than by name:  
| Window  | `w`  |  
| --- | --- |  
| 15 minutes  | `900`  |  
| 24 hours  | `86400`  |  
| 30 days  | `2592000`  |  
### Reading the headers[](https://developers.buffer.com/guides/api-limits.html#reading-the-headers)
The headers come back on every authenticated GraphQL response, so you can read them off requests you already make:
Node.jsPythonPHP
Copy Copied! 
```
// POST your GraphQL query to the API as usual
const response = await fetch('https://api.buffer.com', {
  method: 'POST',
  headers: {
    Authorization: `Bearer ${apiKey}`,
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({ query: '{ account { id } }' }),
})

// fetch joins the repeated RateLimit headers into one string, one entry per window
const policies = response.headers.get('ratelimit').split(/,\s*(?=")/)
// ['"150-in-15min"; r=98; t=897', '"600-in-1day"; r=598; t=86397', ...]

const remaining = Object.fromEntries(
  policies.map((p) => [p.match(/"([^"]+)"/)[1], Number(p.match(/r=(\d+)/)[1])])
)
// { '150-in-15min': 98, '600-in-1day': 598, '3000-in-30days': 2969 }
```

Copy Copied! 
```
import re
import requests

response = requests.post(
    'https://api.buffer.com',
    headers={
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json',
    },
    json={'query': '{ account { id } }'},
)

# urllib3 keeps the repeated headers, so ask for them as a list
policies = response.raw.headers.getlist('RateLimit')
# ['"150-in-15min"; r=98; t=897', '"600-in-1day"; r=598; t=86397', ...]

remaining = {
    re.search(r'"([^"]+)"', policy).group(1): int(re.search(r'r=(\d+)', policy).group(1))
    for policy in policies
}
# {'150-in-15min': 98, '600-in-1day': 598, '3000-in-30days': 2969}
```

Copy Copied! 
```
<?php

$policies = [];

$ch = curl_init('https://api.buffer.com');
curl_setopt_array($ch, [
    CURLOPT_POST => true,
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_HTTPHEADER => [
        'Authorization: Bearer ' . $apiKey,
        'Content-Type: application/json',
    ],
    CURLOPT_POSTFIELDS => json_encode(['query' => '{ account { id } }']),
    // each repeated RateLimit header arrives here as its own line
    CURLOPT_HEADERFUNCTION => function ($ch, $line) use (&$policies) {
        if (stripos($line, 'ratelimit:') === 0) {
            $policies[] = trim(substr($line, strlen('ratelimit:')));
        }
        return strlen($line);
    },
]);

$body = curl_exec($ch);
curl_close($ch);

$remaining = [];
foreach ($policies as $policy) {
    preg_match('/"([^"]+)"/', $policy, $name);
    preg_match('/r=(\d+)/', $policy, $r);
    $remaining[$name[1]] = (int) $r[1];
}
// ['150-in-15min' => 98, '600-in-1day' => 598, '3000-in-30days' => 2969]
```

> How repeated headers are exposed varies by HTTP client, as the tabs above show - some hand you a list or separate lines, others join them into one string - so match whichever your language gives you. Note the space after each `;`, which the API sends and a strict parser will trip over. If you use a GraphQL client library instead of a raw HTTP call, read the response headers through whatever mechanism it provides.
## Handling errors caused by rate limiting[](https://developers.buffer.com/guides/api-limits.html#handling-errors-caused-by-rate-limiting)
When you exceed a rate limit, the API returns HTTP `429 Too Many Requests`. A `429` carries a response body which names the exhausted window, and response headers that tell you how long you should wait until making another request. 
**The response body**
Copy Copied! 
```
{
  "errors": [
    {
      "message": "Too many requests from this client. Please try again later.",
      "extensions": {
        "code": "RATE_LIMIT_EXCEEDED",
        "window": "15m"
      }
    }
  ]
}
```

**The response headers**
Copy Copied! 
```
HTTP/2 429
retry-after:      753
ratelimit:        "150-in-15min"; r=0; t=753
ratelimit-policy: "150-in-15min"; q=150; w=900; pk=:ZjJjZjVmNzM5M2Zm:
content-type:     application/json; charset=utf-8
```
  
| Header  | Example  | What it tells you  |  
| --- | --- | --- |  
| `Retry-After`  | `753`  | How many seconds to wait before retrying. This is the number to sleep on.  |  
| `RateLimit`  | `"150-in-15min"; r=0; t=753`  | Which policy tripped. `r=0` confirms it is exhausted and `t` counts down to its reset.  |  
| `RateLimit-Policy`  | `"150-in-15min"; q=150; w=900`  | The quota (`q`) and window length in seconds (`w`) of that same policy.  |  
`Retry-After` always matches `t` on the returned policy, and both count down in real time, so you can retry the moment it reaches zero.
### Implementing the retry logic[](https://developers.buffer.com/guides/api-limits.html#implementing-the-retry-logic)
The retry logic is the same in any language:
Copy Copied! 
```
send the request
if the status is 429:
    if you are out of attempts, or Retry-After is longer than you will wait:
        surface the failure
    otherwise wait Retry-After seconds, plus a little jitter, and retry
```

The examples below show a sample implementation of this loop. Each retries a `429` until the request goes through, sleeping `Retry-After` seconds in between. `MAX_ATTEMPTS` caps how many tries it makes and `MAX_WAIT_SECONDS` caps how long any one sleep runs, so it always stops instead of hanging. Treat them as starting points rather than drop-in code - the attempt limit, the wait cap, and how you surface a final failure are all yours to decide.
Node.jsPythonPHP
Copy Copied! 
```
const MAX_ATTEMPTS = 3
const MAX_WAIT_SECONDS = 900 // a 30d Retry-After can be weeks away

async function bufferRequest(query) {
  for (let attempt = 1; ; attempt++) {
    const response = await fetch('https://api.buffer.com', {
      method: 'POST',
      headers: {
        Authorization: `Bearer ${apiKey}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ query }),
    })

    if (response.status !== 429) return response.json()

    // Read Retry-After fresh each time: it counts down, so an older value is stale.
    const retryAfter = Number(response.headers.get('retry-after'))
    const { errors } = await response.json()
    const window = errors[0].extensions.window

    if (attempt >= MAX_ATTEMPTS || !(retryAfter > 0) || retryAfter > MAX_WAIT_SECONDS) {
      throw new Error(`Rate limited on the ${window} window, retry in ${retryAfter}s`)
    }

    // Retry-After is exact, so every client waiting it out returns at the same
    // instant. A little jitter spreads them back out.
    const wait = retryAfter + Math.random() * 5

    console.warn(`Rate limited on the ${window} window, waiting ${Math.round(wait)}s`)
    await new Promise((resolve) => setTimeout(resolve, wait * 1000))
  }
}
```

Copy Copied! 
```
import random
import time

import requests

MAX_ATTEMPTS = 3
MAX_WAIT_SECONDS = 900  # a 30d Retry-After can be weeks away


def buffer_request(query):
    for attempt in range(1, MAX_ATTEMPTS + 1):
        response = requests.post(
            'https://api.buffer.com',
            headers={
                'Authorization': f'Bearer {api_key}',
                'Content-Type': 'application/json',
            },
            json={'query': query},
        )

        if response.status_code != 429:
            return response.json()

        # Read Retry-After fresh each time: it counts down, so an older value is stale.
        retry_after = int(response.headers.get('Retry-After', 0))
        window = response.json()['errors'][0]['extensions']['window']

        if attempt == MAX_ATTEMPTS or not 0 < retry_after <= MAX_WAIT_SECONDS:
            raise RuntimeError(f'Rate limited on the {window} window, retry in {retry_after}s')

        # Retry-After is exact, so every client waiting it out returns at the same
        # instant. A little jitter spreads them back out.
        wait = retry_after + random.uniform(0, 5)

        print(f'Rate limited on the {window} window, waiting {round(wait)}s')
        time.sleep(wait)
```

Copy Copied! 
```
<?php

const MAX_ATTEMPTS = 3;
const MAX_WAIT_SECONDS = 900; // a 30d Retry-After can be weeks away

function bufferRequest($query, $apiKey) {
    for ($attempt = 1; $attempt <= MAX_ATTEMPTS; $attempt++) {
        $retryAfter = 0;

        $ch = curl_init('https://api.buffer.com');
        curl_setopt_array($ch, [
            CURLOPT_POST => true,
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_HTTPHEADER => [
                'Authorization: Bearer ' . $apiKey,
                'Content-Type: application/json',
            ],
            CURLOPT_POSTFIELDS => json_encode(['query' => $query]),
            // Read Retry-After fresh each time: it counts down, so an older value is stale.
            CURLOPT_HEADERFUNCTION => function ($ch, $line) use (&$retryAfter) {
                if (stripos($line, 'retry-after:') === 0) {
                    $retryAfter = (int) trim(substr($line, strlen('retry-after:')));
                }
                return strlen($line);
            },
        ]);

        $body = curl_exec($ch);
        $status = curl_getinfo($ch, CURLINFO_RESPONSE_CODE);
        curl_close($ch);

        if ($status !== 429) {
            return json_decode($body, true);
        }

        $window = json_decode($body, true)['errors'][0]['extensions']['window'];

        if ($attempt === MAX_ATTEMPTS || $retryAfter <= 0 || $retryAfter > MAX_WAIT_SECONDS) {
            throw new RuntimeException("Rate limited on the {$window} window, retry in {$retryAfter}s");
        }

        // Retry-After is exact, so every client waiting it out returns at the same
        // instant. A little jitter spreads them back out.
        $wait = $retryAfter + random_int(0, 5);

        error_log("Rate limited on the {$window} window, waiting {$wait}s");
        sleep($wait);
    }
}
```

If the requests come from an AI agent or an MCP client rather than from your own code, the same rule holds but nothing enforces it for you. An agent will usually rephrase a failed call and try again rather than wait. Tell it to stop on a `429` and report the `Retry-After` value instead of retrying, since the header already says exactly how long the wait is and there is nothing left to guess at. The [Efficient API Usage](https://developers.buffer.com/guides/efficient-api-usage.html) guide has prompts you can paste into an agent's instructions.
## Monitoring Your Usage[](https://developers.buffer.com/guides/api-limits.html#monitoring-your-usage)
You don't have to track headers by hand to see where you stand:
  * **Developer Dashboard** - your [API settings page](https://publish.buffer.com/settings/api) shows live usage per window for each of your clients.
  * **Buffer CLI** - the [CLI](https://developers.buffer.com/guides/cli.html) reads these headers on every command. Run any command with `--verbose` to print a rate-limit summary for each window, and it warns you when you're running low even without it (silence it with `--quiet`). On a `429` it reports the exhausted window and how long to wait, then exits with code `3`:


Copy Copied! 
```
Error: Rate limit exceeded (`15m` window). Retry after `9m 51s`. (api · code 3)
```

## Regulating the request rate[](https://developers.buffer.com/guides/api-limits.html#regulating-the-request-rate)
Make sure you optimize your API usage, make only the requests you need and use techniques to reduce your usage before you hit the rate limit errors:
  1. **Slow down before you hit zero.** `r` on the `RateLimit` header tells you what is left in each window. Throttling when it gets low is cheaper than recovering from a `429`. The [CLI](https://developers.buffer.com/guides/cli.html) uses 10% remaining as its warning threshold, which is a reasonable default to copy.
  2. **Back off, then retry.** When you do get a `429`, wait `Retry-After` seconds before your next attempt. See [Implementing the retry logic](https://developers.buffer.com/guides/api-limits.html#implementing-the-retry-logic).
  3. **Stagger scheduled jobs.** If several jobs share one API key, starting them all on the hour concentrates your whole budget into a few minutes. Offsetting their start times spreads the same work across the window.
  4. **Optimize your API usage.** You can employ quite a few different techniques to use the API more efficiently and reduce the number of requests your app makes. Check out the [Efficient API Usage](https://developers.buffer.com/guides/efficient-api-usage.html) guide for some of the best practices.


Buffer aims to ensure that the API stays reliable, performant, and fair for everyone. In specific cases where clients continuously send an excessive number of requests, Buffer may reduce, and in severe cases suspend, API access to protect platform health and stability. This only applies to rare cases, but it's important to always ensure that your applications handle rate limits gracefully.
## Query Limits[](https://developers.buffer.com/guides/api-limits.html#query-limits)
In addition to rate limits, we enforce query-level limits to protect against overly complex or expensive GraphQL queries. 
### Query Complexity[](https://developers.buffer.com/guides/api-limits.html#query-complexity)
Each query is assigned a cost based on the fields it requests:
  * **Scalar fields** (e.g., `id`, `name`): 1 point each
  * **Object fields** (e.g., `organization`, `channel`): 2 points each
  * **Nesting multiplier** : Nested fields are multiplied by a factor of 1.5x per level of depth


The maximum allowed query cost is **175,000 points**. If your query exceeds this, you will receive an error asking you to simplify it.
### Query Depth[](https://developers.buffer.com/guides/api-limits.html#query-depth)
Queries are limited to a maximum depth of **25 levels**. Deeply nested queries can cause exponential resource consumption, so keep your queries as flat as possible.
### Aliases[](https://developers.buffer.com/guides/api-limits.html#aliases)
A maximum of **30 aliases** are allowed per query. Aliases let you rename fields in a response, but excessive use can be used to amplify query cost.
### Directives[](https://developers.buffer.com/guides/api-limits.html#directives)
Queries are limited to a maximum of **50 directives**.
### Tokens[](https://developers.buffer.com/guides/api-limits.html#tokens)
Queries are limited to a maximum of **15,000 tokens**. This is a parser-level limit on the overall size of the query document.
### Query Limit Error Responses[](https://developers.buffer.com/guides/api-limits.html#query-limit-error-responses)
When a query limit is exceeded, you will receive a GraphQL error response:
Copy Copied! 
```
{
  "errors": [
    {
      "message": "Query exceeds maximum allowed complexity. Please simplify your query."
    }
  ]
}
```

The error message will indicate which limit was exceeded (complexity, depth, aliases, directives, or tokens).
These limits may change as we evolve the API, so keep an eye on your usage.
## Frequently asked questions[](https://developers.buffer.com/guides/api-limits.html#frequently-asked-questions)
**What happens when I hit a rate limit?**
The request is rejected with a `429`. The response carries `Retry-After` header telling you how many seconds to wait, and the body naming the limit you hit. 
**Do rejected requests count against my quota?**
A `429` does not consume quota and does not extend how long you are locked out. However, it is very important to implement the `Retry-After` logic to handle the errors gracefully and ensure fair use of the API.
**Is there an endpoint that reports my current limits?**
No. Read the `RateLimit` headers on any response, or use the [API settings page](https://publish.buffer.com/settings/api) or the [CLI](https://developers.buffer.com/guides/cli.html). See [Monitoring Your Usage](https://developers.buffer.com/guides/api-limits.html#monitoring-your-usage).
**Do limits apply per channel or per organization?**
Both, in different ways. The 30-day limit depends on how many unlocked channels your organization has, up to your plan's maximum. All of your API keys and MCP connections share one set of limits, so the limit is per account, not per key. Each app client has its own set of limits, which grows with the number of Buffer users who have authorized it.
**Does usage through MCP or an AI assistant count against my limits?**
Yes. A request through the MCP server counts the same as a request made with an API key. MCP connections share one rate-limit bucket with your personal API keys, so connecting Buffer to another assistant does not give you more quota. Your [API settings page](https://publish.buffer.com/settings/api) lists your MCP connections alongside your keys.
**Are these the same as posting limits?**
Rate limits cap how many API requests you can make. Daily posting limits cap how many posts a channel can publish in a day, and you read them with the `dailyPostingLimits` query. Hitting one has no bearing on the other.
**I need higher limits. What are my options?**
Reduce your request count using the suggestions above first, since most integrations have room to. If your use case genuinely needs more, email developersupport@buffer.com.
[ Previous Error Handling ](https://developers.buffer.com/guides/error-handling.html) [ Next Pagination ](https://developers.buffer.com/guides/pagination.html)
On this page
[Buffer API Rate Limits](https://developers.buffer.com/guides/api-limits.html#buffer-api-rate-limits) [App client limits](https://developers.buffer.com/guides/api-limits.html#app-client-limits) [Using Response Headers to check Rate Limits](https://developers.buffer.com/guides/api-limits.html#using-response-headers-to-check-rate-limits) [Reading the headers](https://developers.buffer.com/guides/api-limits.html#reading-the-headers) [Handling errors caused by rate limiting](https://developers.buffer.com/guides/api-limits.html#handling-errors-caused-by-rate-limiting) [Implementing the retry logic](https://developers.buffer.com/guides/api-limits.html#implementing-the-retry-logic) [Monitoring Your Usage](https://developers.buffer.com/guides/api-limits.html#monitoring-your-usage) [Regulating the request rate](https://developers.buffer.com/guides/api-limits.html#regulating-the-request-rate) [Query Limits](https://developers.buffer.com/guides/api-limits.html#query-limits) [Query Complexity](https://developers.buffer.com/guides/api-limits.html#query-complexity) [Query Depth](https://developers.buffer.com/guides/api-limits.html#query-depth) [Aliases](https://developers.buffer.com/guides/api-limits.html#aliases) [Directives](https://developers.buffer.com/guides/api-limits.html#directives) [Tokens](https://developers.buffer.com/guides/api-limits.html#tokens) [Query Limit Error Responses](https://developers.buffer.com/guides/api-limits.html#query-limit-error-responses) [Frequently asked questions](https://developers.buffer.com/guides/api-limits.html#frequently-asked-questions)
`Esc`
`↑``↓` Navigate `Enter` Open `Esc` Close

