[Skip to content](https://supabase.com/docs/guides/observability/logs#docs-content-container)
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
[Observability](https://supabase.com/docs/guides/observability)
  * [Overview](https://supabase.com/docs/guides/observability)
  * Read project data
    * [Query logs with SQL](https://supabase.com/docs/guides/observability/advanced-log-filtering)
    * [Logs in Studio](https://supabase.com/docs/guides/observability/logs)
    * [Log sources and fields](https://supabase.com/docs/guides/observability/log-field-reference)
    * [Inspect the database](https://supabase.com/docs/guides/observability/inspect)
    * [Advisors](https://supabase.com/docs/guides/observability/advisors)
    * [Reports](https://supabase.com/docs/guides/observability/reports)
    * Metrics API
      * [Grafana Cloud](https://supabase.com/docs/guides/observability/metrics/grafana-cloud)
      * [Grafana self-hosted](https://supabase.com/docs/guides/observability/metrics/grafana-self-hosted)
      * [Datadog](https://docs.datadoghq.com/integrations/supabase/)
      * [Elastic](https://www.elastic.co/docs/reference/integrations/supabase)
      * [Vendor-agnostic setup](https://supabase.com/docs/guides/observability/metrics/vendor-agnostic)
  * Detect and diagnose
    * [Detection checks](https://supabase.com/docs/guides/observability/detecting)
    * [Troubleshooting](https://supabase.com/docs/guides/troubleshooting)
  * Agent prompts
    * [Overview](https://supabase.com/docs/guides/observability/automate-with-agents)
    * [Health](https://supabase.com/docs/guides/observability/automate-with-agents/health)
    * [Security](https://supabase.com/docs/guides/observability/automate-with-agents/security)
    * [Performance](https://supabase.com/docs/guides/observability/automate-with-agents/performance)
    * [Resources](https://supabase.com/docs/guides/observability/automate-with-agents/usage)
  * Configure and export
    * [Configure logging](https://supabase.com/docs/guides/observability/configure-logging)
    * [Log drains](https://supabase.com/docs/guides/observability/log-drains)
    * [Client-side tracing](https://supabase.com/docs/guides/observability/client-side-tracing)
    * [Sentry integration](https://supabase.com/docs/guides/observability/sentry-monitoring)


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
Observability
  1. [Observability](https://supabase.com/docs/guides/observability)
  2. Read project data
  3. [Logs in Studio](https://supabase.com/docs/guides/observability/logs)


Logs in Studio
Use [Logs](https://supabase.com/dashboard/project/_/logs) to inspect events across your hosted project's services. For SQL queries through [Explorer](https://supabase.com/dashboard/project/_/explorer), MCP, or the API, see [Query logs with SQL](https://supabase.com/docs/guides/observability/advanced-log-filtering).
## Find events [#](https://supabase.com/docs/guides/observability/logs#product-logs)
  1. Open [Logs](https://supabase.com/dashboard/project/_/logs).
  2. Set the **Time Range** in the sidebar, or select a range on the timeline.
  3. Select one or more **Log Type** values.
  4. Add filters in the filter bar, or type text to search event messages.
  5. Select a row to inspect the event.


Without a log type selection, Logs queries **Postgres** and **API Gateway**. Selecting types replaces this default set. The timeline groups events by success, warning, and error.
## Filter events[#](https://supabase.com/docs/guides/observability/logs#filter-events)  
| Filter  | Behavior  |  
| --- | --- |  
| Log Type  | Select API Gateway, Postgres, Auth, Storage, PostgREST, Edge Function, Realtime, or pooler events.  |  
| Level  | Match success, warning, or error.  |  
| Status  | Match an HTTP status or Postgres SQLSTATE.  |  
| Method  | Match an HTTP method.  |  
| Pathname  | Match a request path.  |  
| Event message  | Use **iLike** or **Not iLike** for case-insensitive text matching or exclusion. Plain text matches anywhere in the message; `%` specifies a wildcard pattern.  |  
| User  | Match the user's ID in Auth actor IDs or API Gateway JWT subjects. Other log types cannot match this filter.  |  
Filters other than **Event message** and **User** support **Equals** and **Not equal**. **User** supports **Equals**. Included values within a field match any selected value; exclusions remove every selected value. Filters on different fields must all match.
### Gateway and service logs[#](https://supabase.com/docs/guides/observability/logs#gateway-and-service-logs)
The nested service toggles under **API Gateway** include or exclude gateway request paths. Selecting the separate **Auth** , **Storage** , or **PostgREST** log type retrieves that service's own logs. These are different events.
For SQL source names, see the [Log field reference](https://supabase.com/docs/guides/observability/log-field-reference).
### Postgres [#](https://supabase.com/docs/guides/observability/logs#postgres)
Postgres logs contain database activity and errors. Connection events appear when [connection logging](https://supabase.com/docs/guides/platform/postgres-connection-logging) is enabled. Clear **Connection logs** under **Postgres** to hide them.
To record additional statement classes, see [Configure statement logging](https://supabase.com/docs/guides/observability/configure-logging#postgres-statements).
## Inspect an event [#](https://supabase.com/docs/guides/observability/logs#expanding-results)
Select a row to open its detail panel. **Overview** , when available for the log type, shows service details. **Raw JSON** shows the event data. Dock the panel at the bottom or on the right.
Edge Function invocations can include associated console output. In SQL, invocation events use `function_edge_logs` and console events use `function_logs`.
## Watch, share, and export[#](https://supabase.com/docs/guides/observability/logs#watch-share-and-export)
  * Select **Live** to fetch new events automatically. Select it again to pause. Starting live mode clears the fixed time range and sort; selecting a time range or sort stops live mode.
  * Copy the page URL to share the current filters. Recipients need access to the project.
  * Open **Download logs** , choose CSV or JSON, and select a result limit of 100, 500, or 1,000 rows. The export applies the current filters. Without a fixed time range, choose the duration to retrieve.


For continuous export, use [Log drains](https://supabase.com/docs/guides/observability/log-drains).
## Missing results [#](https://supabase.com/docs/guides/observability/logs#single-service-collections)
Check the time range, selected log types, and exclusions first. **User** combined with only Postgres or another unsupported type returns no matches. An empty result does not establish that the user had no activity.
Events must be recorded before they can appear in Logs. See [Configure logging](https://supabase.com/docs/guides/observability/configure-logging) and the [source limitations](https://supabase.com/docs/guides/observability/log-field-reference#capture-limits).
Retention depends on your [pricing plan](https://supabase.com/pricing). See [Manage Logs usage](https://supabase.com/docs/guides/platform/manage-your-usage/logs) for billing details.
[Edit this page on GitHub ](https://github.com/supabase/supabase/blob/master/apps/docs/content/guides/observability/logs.mdx)
## Is this helpful?
No Yes
## AI tools
[Connect your AI agent](https://supabase.com/docs/guides/ai-tools)Copy as Markdown[Ask ChatGPT](https://chatgpt.com/?hint=search&q=Read%20from%20https%3A%2F%2Fsupabase.com%2Fdocs%2Fguides%2Fobservability%2Flogs%20so%20I%20can%20ask%20questions%20about%20its%20contents)[Ask Claude](https://claude.ai/new?q=Read%20from%20https%3A%2F%2Fsupabase.com%2Fdocs%2Fguides%2Fobservability%2Flogs%20so%20I%20can%20ask%20questions%20about%20its%20contents)[Prefer on Google](https://www.google.com/preferences/source?q=supabase.com "Add Supabase as a preferred source on Google")
  * Need some help?
[Contact support](https://supabase.com/support)
  * Latest product updates?
[See Changelog](https://supabase.com/changelog)
  * Something's not right?
[Check system status](https://status.supabase.com/)


* * *
[© Supabase Inc](https://supabase.com/)—[Contributing](https://github.com/supabase/supabase/blob/master/apps/docs/DEVELOPERS.md)[Author Styleguide](https://github.com/supabase/supabase/blob/master/apps/docs/CONTRIBUTING.md)[Open Source](https://supabase.com/open-source)[SupaSquad](https://supabase.com/supasquad)Privacy Settings
[Twitter](https://twitter.com/supabase)[GitHub](https://github.com/supabase)[Discord](https://discord.supabase.com/)[Youtube](https://youtube.com/c/supabase)

