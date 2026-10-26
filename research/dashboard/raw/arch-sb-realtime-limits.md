[Skip to content](https://supabase.com/docs/guides/realtime/limits#docs-content-container)
[![Supabase wordmark](https://supabase.com/docs/supabase-dark.svg?dpl=dpl_3WvkypGBbZNy4rLodKeg7tyzbGHW)![Supabase wordmark](https://supabase.com/docs/supabase-light.svg?dpl=dpl_3WvkypGBbZNy4rLodKeg7tyzbGHW)DOCS](https://supabase.com/docs)
  * [Start](https://supabase.com/docs/guides/getting-started)
  * Products
  * Build
  * Manage
  * Reference
  * Resources


[![Supabase wordmark](https://supabase.com/docs/supabase-dark.svg?dpl=dpl_3WvkypGBbZNy4rLodKeg7tyzbGHW)![Supabase wordmark](https://supabase.com/docs/supabase-light.svg?dpl=dpl_3WvkypGBbZNy4rLodKeg7tyzbGHW)DOCS](https://supabase.com/docs)
Search docs...
Ctrl K
Main menu
[Realtime](https://supabase.com/docs/guides/realtime)
  * [Overview](https://supabase.com/docs/guides/realtime)
  * [Getting Started](https://supabase.com/docs/guides/realtime/getting_started)
  * Usage
    * [Broadcast](https://supabase.com/docs/guides/realtime/broadcast)
    * [Presence](https://supabase.com/docs/guides/realtime/presence)
    * [Postgres Changes](https://supabase.com/docs/guides/realtime/postgres-changes)
    * [Settings](https://supabase.com/docs/guides/realtime/settings)
  * Security
    * [Authorization](https://supabase.com/docs/guides/realtime/authorization)
  * Guides
    * [Realtime Reports](https://supabase.com/docs/guides/realtime/reports)
    * [Subscribing to Database Changes](https://supabase.com/docs/guides/realtime/subscribing-to-database-changes)
    * [Using Realtime with Next.js](https://supabase.com/docs/guides/realtime/realtime-with-nextjs)
    * [Using Realtime Presence with Flutter](https://supabase.com/docs/guides/realtime/realtime-user-presence)
    * [Listening to Postgres Changes with Flutter](https://supabase.com/docs/guides/realtime/realtime-listening-flutter)
  * Deep dive
    * [Limits](https://supabase.com/docs/guides/realtime/limits)
    * [Pricing](https://supabase.com/docs/guides/realtime/pricing)
    * [Architecture](https://supabase.com/docs/guides/realtime/architecture)
    * [Concepts](https://supabase.com/docs/guides/realtime/concepts)
    * [Protocol](https://supabase.com/docs/guides/realtime/protocol)
    * [Benchmarks](https://supabase.com/docs/guides/realtime/benchmarks)
  * Debugging
    * [Operational Error Codes](https://supabase.com/docs/guides/realtime/error_codes)
    * [Troubleshooting](https://supabase.com/docs/guides/realtime/troubleshooting)


[![Supabase wordmark](https://supabase.com/docs/supabase-dark.svg?dpl=dpl_3WvkypGBbZNy4rLodKeg7tyzbGHW)![Supabase wordmark](https://supabase.com/docs/supabase-light.svg?dpl=dpl_3WvkypGBbZNy4rLodKeg7tyzbGHW)DOCS](https://supabase.com/docs)
  * [Start](https://supabase.com/docs/guides/getting-started)
  * Products
  * Build
  * Manage
  * Reference
  * Resources


[![Supabase wordmark](https://supabase.com/docs/supabase-dark.svg?dpl=dpl_3WvkypGBbZNy4rLodKeg7tyzbGHW)![Supabase wordmark](https://supabase.com/docs/supabase-light.svg?dpl=dpl_3WvkypGBbZNy4rLodKeg7tyzbGHW)DOCS](https://supabase.com/docs)
Search docs...
Ctrl K
Realtime
  1. [Realtime](https://supabase.com/docs/guides/realtime)
  2. Deep dive
  3. [Limits](https://supabase.com/docs/guides/realtime/limits)


Realtime Limits
Our cluster supports millions of concurrent connections and message throughput for production workloads.
Upgrade your plan to increase your limits. Without a spend cap, or on an Enterprise plan, some limits are still in place to protect budgets. All limits are configurable per project. [Contact support](https://supabase.com/dashboard/support/new) if you need your limits increased.
## Limits by plan[#](https://supabase.com/docs/guides/realtime/limits#limits-by-plan)  
|   | Free  | Pro  | Pro (no spend cap)  | Team  | Enterprise  |  
| --- | --- | --- | --- | --- | --- |  
| **Concurrent connections**  | 200  | 500  | 10,000  | 10,000  | 10,000+  |  
| **Messages per second**  | 100  | 500  | 2,500  | 2,500  | 2,500+  |  
| **Channel joins per second**  | 100  | 500  | 2,500  | 2,500  | 2,500+  |  
| **Channels per connection**  | 100  | 100  | 100  | 100  | 100+  |  
| **Presence keys per object**  | 10  | 10  | 10  | 10  | 10+  |  
| **Presence messages per second**  | 20  | 50  | 1,000  | 1,000  | 1,000+  |  
| **Presence calls per client, per 30 seconds**  | 5  | 5  | 5  | 5  | 5  |  
| **Broadcast payload size**  | 256 KB  | 3,000 KB  | 3,000 KB  | 3,000 KB  | 3,000+ KB  |  
| **Postgres change payload size ([**read more**](https://supabase.com/docs/guides/realtime/limits#postgres-changes-payload-limit))**  | 1,024 KB  | 1,024 KB  | 1,024 KB  | 1,024 KB  | 1,024+ KB  |  
| **Broadcast replay retention ([**read more**](https://supabase.com/docs/guides/realtime/broadcast#broadcast-replay))**  | 72 hours  | 72 hours  | 72 hours  | 72 hours  | 72 hours  |  
| **Broadcast replay messages per request**  | 25  | 25  | 25  | 25  | 25  |  
Beyond the Free and Pro Plan you can customize your limits by [contacting support](https://supabase.com/dashboard/support/new).
## Limit errors[#](https://supabase.com/docs/guides/realtime/limits#limit-errors)
When you exceed a limit, errors will appear in the backend logs and client-side messages in the WebSocket connection.
  * **Logs** : check the [Realtime logs](https://supabase.com/dashboard/project/_/database/realtime-logs) inside your project Dashboard.
  * **WebSocket errors** : Use your browser's developer tools to find the WebSocket initiation request and view individual messages.


Realtime Inspector
You can use the [Realtime Inspector](https://realtime.supabase.com/inspector/new) to reproduce an error and share those connection details with Supabase support.
Some limits can cause a Channel join to be refused. Realtime will reply with one of the following WebSocket messages:
###  `too_many_channels`[#](https://supabase.com/docs/guides/realtime/limits#toomanychannels)
Too many channels currently joined for a single connection.
###  `too_many_connections`[#](https://supabase.com/docs/guides/realtime/limits#toomanyconnections)
Too many total concurrent connections for a project.
###  `too_many_joins`[#](https://supabase.com/docs/guides/realtime/limits#toomanyjoins)
Too many Channel joins per second.
###  `tenant_events`[#](https://supabase.com/docs/guides/realtime/limits#tenantevents)
Connections will be disconnected if your project is generating too many messages per second. `supabase-js` will reconnect automatically when the message throughput decreases below your plan limit. An `event` is a WebSocket message delivered to, or sent from a client.
## Postgres changes payload limit[#](https://supabase.com/docs/guides/realtime/limits#postgres-changes-payload-limit)
When this limit is reached, the `new` and `old` record payloads only include the fields with a value size of less than or equal to 64 bytes.
[Edit this page on GitHub ](https://github.com/supabase/supabase/blob/master/apps/docs/content/guides/realtime/limits.mdx)
## Is this helpful?
No Yes
## AI tools
[Connect your AI agent](https://supabase.com/docs/guides/ai-tools)Copy as Markdown[Ask ChatGPT](https://chatgpt.com/?hint=search&q=Read%20from%20https%3A%2F%2Fsupabase.com%2Fdocs%2Fguides%2Frealtime%2Flimits%20so%20I%20can%20ask%20questions%20about%20its%20contents)[Ask Claude](https://claude.ai/new?q=Read%20from%20https%3A%2F%2Fsupabase.com%2Fdocs%2Fguides%2Frealtime%2Flimits%20so%20I%20can%20ask%20questions%20about%20its%20contents)[Prefer on Google](https://www.google.com/preferences/source?q=supabase.com "Add Supabase as a preferred source on Google")
  * Need some help?
[Contact support](https://supabase.com/support)
  * Latest product updates?
[See Changelog](https://supabase.com/changelog)
  * Something's not right?
[Check system status](https://status.supabase.com/)


* * *
[© Supabase Inc](https://supabase.com/)—[Contributing](https://github.com/supabase/supabase/blob/master/apps/docs/DEVELOPERS.md)[Author Styleguide](https://github.com/supabase/supabase/blob/master/apps/docs/CONTRIBUTING.md)[Open Source](https://supabase.com/open-source)[SupaSquad](https://supabase.com/supasquad)Privacy Settings
[Twitter](https://twitter.com/supabase)[GitHub](https://github.com/supabase)[Discord](https://discord.supabase.com/)[Youtube](https://youtube.com/c/supabase)

