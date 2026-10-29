[Skip to content](https://developers.cloudflare.com/containers/platform/pricing/#main-content)
> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/containers/llms.txt  
> Use this file to discover all available pages before exploring further.
[![](https://developers.cloudflare.com/_astro/logo.te5VL_aD.svg)Docs](https://developers.cloudflare.com/)[Directory](https://developers.cloudflare.com/directory/)[API](https://developers.cloudflare.com/api/)[SDKs](https://developers.cloudflare.com/fundamentals/api/reference/sdks/)[Changelog](https://developers.cloudflare.com/changelog/)
Search`Ctrl``K`[](https://github.com/cloudflare/cloudflare-docs)[Log inDashboard](https://dash.cloudflare.com/)
[](https://developers.cloudflare.com/)[Containers](https://developers.cloudflare.com/containers/)
`/`
  * [Overview](https://developers.cloudflare.com/containers/)
  * [Get started](https://developers.cloudflare.com/containers/get-started/)
  * Concepts
    * [Overview](https://developers.cloudflare.com/containers/concepts/)
    * [Lifecycle of a Container](https://developers.cloudflare.com/containers/concepts/architecture/)
    * [Placement](https://developers.cloudflare.com/containers/concepts/placement/)
  * Guides
    * [Deploy Containers](https://developers.cloudflare.com/containers/guides/deploy/)
    * [Local Development](https://developers.cloudflare.com/containers/guides/local-dev/)
    * [Execute commands](https://developers.cloudflare.com/containers/guides/execute-commands/)
    * [Image Management](https://developers.cloudflare.com/containers/guides/image-management/)
    * [SSH](https://developers.cloudflare.com/containers/guides/ssh/)
    * [Use snapshots](https://developers.cloudflare.com/containers/guides/snapshots/)
    * [Migrate from the Container class to the Durable Object Container API](https://developers.cloudflare.com/containers/guides/migrate-to-durable-object-container-api/)
    * [Migrate to the Durable Object scheduling policy](https://developers.cloudflare.com/containers/guides/migrate-to-durable-object-scheduling-policy/)
  * Configuration
    * [Wrangler configuration](https://developers.cloudflare.com/containers/configuration/wrangler/)
    * [Scheduling Policies](https://developers.cloudflare.com/containers/configuration/scheduling-policy/)
    * [Connect to Workers and Bindings](https://developers.cloudflare.com/containers/configuration/workers-connections/)
    * [Environment Variables](https://developers.cloudflare.com/containers/configuration/environment-variables/)
    * [Scaling and Routing](https://developers.cloudflare.com/containers/configuration/scaling-and-routing/)
    * [Rollouts](https://developers.cloudflare.com/containers/configuration/rollouts/)
    * [Handle outbound traffic](https://developers.cloudflare.com/containers/configuration/outbound-traffic/)
  * API
    * [Overview](https://developers.cloudflare.com/containers/api/)
    * [Durable Object Container API](https://developers.cloudflare.com/containers/api/durable-object-container/)
    * [Container class](https://developers.cloudflare.com/containers/api/container-class/)
  * Examples
    * [Stateless instances](https://developers.cloudflare.com/containers/examples/stateless/)
    * [Static frontend, container backend](https://developers.cloudflare.com/containers/examples/container-backend/)
    * [Cron container](https://developers.cloudflare.com/containers/examples/cron/)
    * [Monitor container lifecycle](https://developers.cloudflare.com/containers/examples/status-hooks/)
    * [Environment variables and secrets](https://developers.cloudflare.com/containers/examples/env-vars-and-secrets/)
    * [WebSocket to container](https://developers.cloudflare.com/containers/examples/websocket/)
    * [Mount R2 buckets with FUSE](https://developers.cloudflare.com/containers/examples/r2-fuse-mount/)
    * [More examples](https://developers.cloudflare.com/containers/examples/durable-object-interface/)
  * Reference
    * [Wrangler Configuration ↗︎](https://developers.cloudflare.com/workers/wrangler/configuration/#containers)
    * [Wrangler Commands ↗︎](https://developers.cloudflare.com/workers/wrangler/commands/containers/)
  * [Frequently Asked Questions](https://developers.cloudflare.com/containers/faq/)
  * Platform
    * [Limits and Instance Types](https://developers.cloudflare.com/containers/platform/limits/)
    * [Pricing](https://developers.cloudflare.com/containers/platform/pricing/)
  * Agent resources
    * [Agent setup ↗︎](https://developers.cloudflare.com/agent-setup/)
    * [Cloudflare Skills ↗︎](https://github.com/cloudflare/skills)
    * [Code Mode MCP Server ↗︎](https://github.com/cloudflare/mcp)
    * [Domain-specific MCP Servers ↗︎MCP](https://github.com/cloudflare/mcp-server-cloudflare)
    * [Containers llms.txt ↗︎](https://developers.cloudflare.com/containers/llms.txt)
    * [Containers llms-full.txt ↗︎](https://developers.cloudflare.com/containers/llms-full.txt)
    * [Cloudflare Docs llms.txt ↗︎](https://developers.cloudflare.com/llms.txt)
    * [Cloudflare Docs llms-full.txt ↗︎](https://developers.cloudflare.com/llms-full.txt)


  1. [Home](https://developers.cloudflare.com/)
  2. /[Containers](https://developers.cloudflare.com/containers/)
  3. /Platform
  4. /Pricing


# Pricing
Last updated Oct 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/containers/platform/pricing/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)
Overview vCPU, Memory and Disk Network Egress Workers and Durable Objects Pricing Logs and Observability
## vCPU, Memory and Disk
[](https://developers.cloudflare.com/containers/platform/pricing/#vcpu-memory-and-disk)
Containers are billed for every 10ms that they are actively running at the following rates, with included monthly usage as part of the $5 USD per month [Workers Paid plan](https://developers.cloudflare.com/workers/platform/pricing/):  
|   | Memory  | CPU  | Disk  |  
| --- | --- | --- | --- |  
| **Free**  | N/A  | N/A  |   |  
| **Workers Paid**  | 25 GiB-hours/month included   
+$0.0000025 per additional GiB-second  | 375 vCPU-minutes/month   
+ $0.000020 per additional vCPU-second  | 200 GB-hours/month   
+$0.00000007 per additional GB-second  |  
You only pay for what you use — charges start when a request is sent to the container or when it is manually started. Charges stop after the container instance goes to sleep, which can happen automatically after a timeout. This makes it easy to scale to zero, and allows you to get high utilization even with bursty traffic.
Memory and disk usage are based on the _provisioned resources_ for the instance type you select, while CPU usage is based on _active usage_ only.
#### Instance Types
[](https://developers.cloudflare.com/containers/platform/pricing/#instance-types)
When you deploy a container, you specify an [instance type](https://developers.cloudflare.com/containers/platform/limits/#instance-types).
The instance type you select will impact your bill — larger instances include more memory and disk, incurring additional costs, and higher CPU capacity, which allows you to incur higher CPU costs based on active usage.
The following instance types are currently available:  
| Instance Type  | vCPU  | Memory  | Disk  |  
| --- | --- | --- | --- |  
| lite  | 1/16  | 256 MiB  | 2 GB  |  
| basic  | 1/4  | 1 GiB  | 4 GB  |  
| standard-1  | 1/2  | 4 GiB  | 8 GB  |  
| standard-2  | 1  | 6 GiB  | 12 GB  |  
| standard-3  | 2  | 8 GiB  | 16 GB  |  
| standard-4  | 4  | 12 GiB  | 20 GB  |  
## Network Egress
[](https://developers.cloudflare.com/containers/platform/pricing/#network-egress)
Egress from Containers is priced at the following rates:  
| Region  | Price per GB  | Included Allotment per month  |  
| --- | --- | --- |  
| North America & Europe  | $0.025  | 1 TB  |  
| Oceania, Korea, Taiwan  | $0.05  | 500 GB  |  
| Everywhere Else  | $0.04  | 500 GB  |  
## Workers and Durable Objects Pricing
[](https://developers.cloudflare.com/containers/platform/pricing/#workers-and-durable-objects-pricing)
When you use Containers, incoming requests to your containers are handled by your [Worker](https://developers.cloudflare.com/workers/platform/pricing/), and each container has its own [Durable Object](https://developers.cloudflare.com/durable-objects/platform/pricing/). You are billed for your usage of both Workers and Durable Objects.
## Logs and Observability
[](https://developers.cloudflare.com/containers/platform/pricing/#logs-and-observability)
Containers are integrated with the [Workers Logs](https://developers.cloudflare.com/workers/observability/logs/workers-logs/) platform, and billed at the same rate. Refer to [Workers Logs pricing](https://developers.cloudflare.com/workers/observability/logs/workers-logs/#pricing) for details.
When you [turn on observability for your Worker](https://developers.cloudflare.com/workers/observability/logs/workers-logs/#enable-workers-logs), or configure `observability` on a specific container, logs from that container will show in both the Containers and Observability sections of the Cloudflare dashboard.
[PreviousLimits and Instance Types](https://developers.cloudflare.com/containers/platform/limits/)
Was this helpful?
YesNo
[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/containers/platform/pricing.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
## On this page
  * [Overview](https://developers.cloudflare.com/containers/platform/pricing/#_top)
  * [vCPU, Memory and Disk](https://developers.cloudflare.com/containers/platform/pricing/#vcpu-memory-and-disk)
  * [Network Egress](https://developers.cloudflare.com/containers/platform/pricing/#network-egress)
  * [Workers and Durable Objects Pricing](https://developers.cloudflare.com/containers/platform/pricing/#workers-and-durable-objects-pricing)
  * [Logs and Observability](https://developers.cloudflare.com/containers/platform/pricing/#logs-and-observability)


Was this helpful?
YesNo
[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/containers/platform/pricing.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
Getting started
[Plans](https://www.cloudflare.com/plans/)[Contact sales](https://www.cloudflare.com/resource/contact-enterprise-sales/)[Partners](https://www.cloudflare.com/partners/)[Find a partner](https://partnerlocator.cloudflare.com/dashboard)[Startups](https://www.cloudflare.com/startups/)[Under attack?](https://www.cloudflare.com/under-attack-hotline/)[Domain name search](https://domains.cloudflare.com/)
Company
[About](https://www.cloudflare.com/about/)[Careers](https://www.cloudflare.com/careers/)[Investors](https://cloudflare.net/)[Press](https://www.cloudflare.com/press/)[Press kit](https://www.cloudflare.com/press/press-kit/)[Global network](https://www.cloudflare.com/network/)
Public interest
[Project Galileo](https://www.cloudflare.com/galileo/)[Athenian Project](https://www.cloudflare.com/athenian/)[Cloudflare for Campaigns](https://www.cloudflare.com/campaigns/)[Project Fairshot](https://www.cloudflare.com/fair-shot/)[Impact/ESG](https://www.cloudflare.com/impact/)
Compliance
[Compliance resources](https://www.cloudflare.com/trust-hub/compliance-resources/)[Trust Hub](https://www.cloudflare.com/trust-hub/)[Data Protection](https://www.cloudflare.com/trust-hub/gdpr/)[Responsible AI](https://www.cloudflare.com/trust-hub/responsible-ai/)[Transparency report](https://www.cloudflare.com/transparency/)[Report abuse](https://www.cloudflare.com/trust-hub/abuse-approach/)
Resources
[App innovation report](https://www.cloudflare.com/resource/app-innovation-report/)[Cloudflare Radar](https://radar.cloudflare.com/)[Case studies](https://www.cloudflare.com/case-studies/)[Status](https://www.cloudflarestatus.com/)[Support](https://support.cloudflare.com/)[Events](https://www.cloudflare.com/events/)[Blog](https://blog.cloudflare.com/)
Developers
[Documentation](https://developers.cloudflare.com/)[Learning center](https://www.cloudflare.com/learning/)[Community](https://community.cloudflare.com/)
Solutions
[SSE and SASE platform](https://www.cloudflare.com/sase/)[Cloudflare AI Cloud](https://www.cloudflare.com/solutions/ai/)[AI Security](https://www.cloudflare.com/solutions/ai-security/)[Frontend Development Platform](https://www.cloudflare.com/solutions/frontends/)[Multi-Tenant Platform Development](https://www.cloudflare.com/solutions/platforms/)[Web Security Platform](https://www.cloudflare.com/solutions/security/)
[Start Building](https://dash.cloudflare.com/sign-up)[Log In](https://dash.cloudflare.com/login)
© 2026 Cloudflare, Inc.
[Privacy policy](https://www.cloudflare.com/policies/privacy/)| [Report security issues](https://www.cloudflare.com/disclosure/)| [Terms of use](https://www.cloudflare.com/policies/terms/)| [Trademark](https://www.cloudflare.com/trademark/)
|
![privacy options](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=26,height=12,format=svg/_astro/privacyoptions.BWXSiJOZ.svg)Your privacy choices
[![](https://developers.cloudflare.com/_astro/logo.te5VL_aD.svg)Docs](https://developers.cloudflare.com/)

