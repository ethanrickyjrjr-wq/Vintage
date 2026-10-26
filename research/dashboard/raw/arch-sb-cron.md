[Skip to content](https://supabase.com/docs/guides/cron#docs-content-container)
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
[Cron](https://supabase.com/docs/guides/cron)
  * [Overview](https://supabase.com/docs/guides/cron)
  * Getting Started
    * [Install](https://supabase.com/docs/guides/cron/install)
    * [Quickstart](https://supabase.com/docs/guides/cron/quickstart)


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
Cron
  1. [Cron](https://supabase.com/docs/guides/cron)
  2. [Overview](https://supabase.com/docs/guides/cron)


Cron
Schedule Recurring Jobs with Cron Syntax in Postgres
Supabase Cron is a Postgres Module that simplifies scheduling recurring Jobs with cron syntax and monitoring Job runs inside Postgres.
Cron Jobs can be created via SQL or the [Integrations -> Cron](https://supabase.com/dashboard/project/_/integrations) interface inside the Dashboard, and can run anywhere from every second to once a year depending on your use case.
![Manage cron jobs via the Dashboard](https://supabase.com/docs/_next/image?url=%2Fdocs%2Fimg%2Fguides%2Fcron%2Fcron--light.jpg&w=3840&q=75&dpl=dpl_3WvkypGBbZNy4rLodKeg7tyzbGHW)
Every Job can run SQL snippets or database functions with zero network latency or make an HTTP request, such as invoking a Supabase Edge Function, with ease.
For best performance, we recommend no more than 8 Jobs run concurrently. Each Job should run no more than 10 minutes.
## How does Cron work?[#](https://supabase.com/docs/guides/cron#how-does-cron-work)
Under the hood, Supabase Cron uses the [`pg_cron`](https://github.com/citusdata/pg_cron) Postgres database extension which is the scheduling and execution engine for your Jobs.
The extension creates a `cron` schema in your database and all Jobs are stored on the `cron.job` table. Every Job's run and its status is recorded on the `cron.job_run_details` table.
The Supabase Dashboard provides an interface for you to schedule Jobs and monitor Job runs. You can also do the same with SQL.
## Resources[#](https://supabase.com/docs/guides/cron#resources)
  * [`pg_cron` GitHub Repository](https://github.com/citusdata/pg_cron)

[Edit this page on GitHub ](https://github.com/supabase/supabase/blob/master/apps/docs/content/guides/cron.mdx)
Watch video guide
![](https://supabase.com/docs/_next/image?url=https%3A%2F%2Fimg.youtube.com%2Fvi%2FmiRQPbIJOuQ%2F0.jpg&w=3840&q=75)
## Is this helpful?
No Yes
## AI tools
[Connect your AI agent](https://supabase.com/docs/guides/ai-tools)Copy as Markdown[Ask ChatGPT](https://chatgpt.com/?hint=search&q=Read%20from%20https%3A%2F%2Fsupabase.com%2Fdocs%2Fguides%2Fcron%20so%20I%20can%20ask%20questions%20about%20its%20contents)[Ask Claude](https://claude.ai/new?q=Read%20from%20https%3A%2F%2Fsupabase.com%2Fdocs%2Fguides%2Fcron%20so%20I%20can%20ask%20questions%20about%20its%20contents)[Prefer on Google](https://www.google.com/preferences/source?q=supabase.com "Add Supabase as a preferred source on Google")
  * Need some help?
[Contact support](https://supabase.com/support)
  * Latest product updates?
[See Changelog](https://supabase.com/changelog)
  * Something's not right?
[Check system status](https://status.supabase.com/)


* * *
[© Supabase Inc](https://supabase.com/)—[Contributing](https://github.com/supabase/supabase/blob/master/apps/docs/DEVELOPERS.md)[Author Styleguide](https://github.com/supabase/supabase/blob/master/apps/docs/CONTRIBUTING.md)[Open Source](https://supabase.com/open-source)[SupaSquad](https://supabase.com/supasquad)Privacy Settings
[Twitter](https://twitter.com/supabase)[GitHub](https://github.com/supabase)[Discord](https://discord.supabase.com/)[Youtube](https://youtube.com/c/supabase)

