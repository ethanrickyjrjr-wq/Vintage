[Skip to content](https://developers.cloudflare.com/tunnel/#main-content)
> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/tunnel/llms.txt  
> Use this file to discover all available pages before exploring further.
[![](https://developers.cloudflare.com/_astro/logo.te5VL_aD.svg)Docs](https://developers.cloudflare.com/)[Directory](https://developers.cloudflare.com/directory/)[API](https://developers.cloudflare.com/api/)[SDKs](https://developers.cloudflare.com/fundamentals/api/reference/sdks/)[Changelog](https://developers.cloudflare.com/changelog/)
Search`Ctrl``K`[](https://github.com/cloudflare/cloudflare-docs)[Log inDashboard](https://dash.cloudflare.com/)
[](https://developers.cloudflare.com/)[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/)
`/`
  * [Overview](https://developers.cloudflare.com/tunnel/)
  * Get started
    * [Overview](https://developers.cloudflare.com/tunnel/get-started/)
    * [Quick Tunnels](https://developers.cloudflare.com/tunnel/get-started/quick-tunnels/)
  * Concepts
    * [Overview](https://developers.cloudflare.com/tunnel/concepts/)
    * [Routing](https://developers.cloudflare.com/tunnel/concepts/routing/)
  * Features
    * Locally-managed tunnels
      * [Overview](https://developers.cloudflare.com/tunnel/features/locally-managed-tunnels/)
      * [Create a locally-managed tunnel](https://developers.cloudflare.com/tunnel/features/locally-managed-tunnels/create-local-tunnel/)
      * [Configuration file](https://developers.cloudflare.com/tunnel/features/locally-managed-tunnels/configuration-file/)
      * Run as a service
        * [Overview](https://developers.cloudflare.com/tunnel/features/locally-managed-tunnels/as-a-service/)
        * [Linux](https://developers.cloudflare.com/tunnel/features/locally-managed-tunnels/as-a-service/linux/)
        * [macOS](https://developers.cloudflare.com/tunnel/features/locally-managed-tunnels/as-a-service/macos/)
        * [Windows](https://developers.cloudflare.com/tunnel/features/locally-managed-tunnels/as-a-service/windows/)
      * [Useful commands](https://developers.cloudflare.com/tunnel/features/locally-managed-tunnels/tunnel-useful-commands/)
      * [Tunnel permissions](https://developers.cloudflare.com/tunnel/features/locally-managed-tunnels/tunnel-permissions/)
      * [Useful terms](https://developers.cloudflare.com/tunnel/features/locally-managed-tunnels/local-tunnel-terms/)
    * [Tunnels for Platforms](https://developers.cloudflare.com/tunnel/features/tunnels-for-platforms/)
  * Guides
    * [Overview](https://developers.cloudflare.com/tunnel/guides/)
    * [Ansible](https://developers.cloudflare.com/tunnel/guides/ansible/)
    * [AWS](https://developers.cloudflare.com/tunnel/guides/aws/)
    * [Azure](https://developers.cloudflare.com/tunnel/guides/azure/)
    * [GCP](https://developers.cloudflare.com/tunnel/guides/google-cloud-platform/)
    * [Kubernetes](https://developers.cloudflare.com/tunnel/guides/kubernetes/)
    * [Terraform](https://developers.cloudflare.com/tunnel/guides/terraform/)
    * [Update cloudflared](https://developers.cloudflare.com/tunnel/guides/update-cloudflared/)
    * [Granular permissions](https://developers.cloudflare.com/tunnel/guides/granular-permissions/)
  * [Tutorials](https://developers.cloudflare.com/tunnel/tutorials/)
  * [Configuration](https://developers.cloudflare.com/tunnel/configuration/)
  * Reference
    * [Run parameters](https://developers.cloudflare.com/tunnel/reference/run-parameters/)
    * [Origin parameters](https://developers.cloudflare.com/tunnel/reference/origin-parameters/)
    * [Tunnel tokens](https://developers.cloudflare.com/tunnel/reference/tunnel-tokens/)
  * [Observability](https://developers.cloudflare.com/tunnel/observability/)
  * Platform
    * [System requirements](https://developers.cloudflare.com/tunnel/platform/system-requirements/)
    * [Changelog](https://developers.cloudflare.com/tunnel/platform/changelog/)
  * [Integrations](https://developers.cloudflare.com/tunnel/integrations/)
  * [Downloads](https://developers.cloudflare.com/tunnel/downloads/)
  * Troubleshooting
    * [Overview](https://developers.cloudflare.com/tunnel/troubleshooting/)
    * [HTTPS origins](https://developers.cloudflare.com/tunnel/troubleshooting/https-origins/)
  * Agent resources
    * [Agent setup ↗︎](https://developers.cloudflare.com/agent-setup/)
    * [Cloudflare Skills ↗︎](https://github.com/cloudflare/skills)
    * [Code Mode MCP Server ↗︎](https://github.com/cloudflare/mcp)
    * [Domain-specific MCP Servers ↗︎MCP](https://github.com/cloudflare/mcp-server-cloudflare)
    * [Cloudflare Tunnel llms.txt ↗︎](https://developers.cloudflare.com/tunnel/llms.txt)
    * [Cloudflare Tunnel llms-full.txt ↗︎](https://developers.cloudflare.com/tunnel/llms-full.txt)
    * [Cloudflare Docs llms.txt ↗︎](https://developers.cloudflare.com/llms.txt)
    * [Cloudflare Docs llms-full.txt ↗︎](https://developers.cloudflare.com/llms-full.txt)


  1. [Home](https://developers.cloudflare.com/)
  2. /Cloudflare Tunnel


# Cloudflare Tunnel
Last updated Sep 11, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/tunnel/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)
Overview How it works Use cases Get started
Securely connect your origin servers, APIs, and services to Cloudflare with post-quantum encrypted tunnels — no public IPs required.
Available on all plans
Looking for private networking or Zero Trust?
This documentation covers Cloudflare Tunnel use cases for public applications. For VPN replacement, private network access, and network traffic filtering, refer to the [Cloudflare One Tunnel documentation](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/).
Cloudflare Tunnel connects your infrastructure to Cloudflare through an outbound-only, [post-quantum encrypted](https://developers.cloudflare.com/ssl/post-quantum-cryptography/) connection. Instead of exposing a public IP, you install a lightweight daemon called `cloudflared` on your server. It creates a persistent tunnel to Cloudflare's global network, so all traffic to your origins flows through Cloudflare — where CDN caching, WAF, Bot Management, and DDoS protection are applied automatically.
No open inbound ports. No public IPs. No attack surface.
## How it works
[](https://developers.cloudflare.com/tunnel/#how-it-works)
  1. Install `cloudflared` on your server or network.
  2. `cloudflared` establishes outbound, post-quantum encrypted connections to Cloudflare — no inbound ports or firewall changes required.
  3. Map public hostnames to local services (for example, `app.example.com` to `http://localhost:8080`).
  4. Traffic flows through Cloudflare's network to your origin, with full CDN and security applied.


Each tunnel maintains four long-lived connections to two Cloudflare data centers for built-in redundancy. You can run multiple `cloudflared` [replicas](https://developers.cloudflare.com/tunnel/configuration/#replicas-and-high-availability) for additional high availability.
![How an HTTP request reaches an origin connected with Cloudflare Tunnel](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1768,height=1102,format=webp/_astro/handshake.eh3a-Ml1.jpg)
## Use cases
[](https://developers.cloudflare.com/tunnel/#use-cases)
  * **Secure origin connectivity** — Eliminate public origin IPs. All traffic flows through Cloudflare with CDN, WAF, and DDoS protection applied.
  * **Public ingress routing** — Publish internal applications to the internet by mapping public hostnames to local services. Supports HTTP, HTTPS, TCP, SSH, RDP, and [more](https://developers.cloudflare.com/tunnel/concepts/routing/#supported-protocols).
  * **Workers VPC** — Enable [Cloudflare Workers](https://developers.cloudflare.com/workers-vpc/) to securely access private databases, APIs, and services through your tunnel.
  * **Load Balancing** — Use tunnels as origin endpoints in [Cloudflare Load Balancer](https://developers.cloudflare.com/load-balancing/) pools for high availability and intelligent traffic steering.


## Get started
[](https://developers.cloudflare.com/tunnel/#get-started)
### [Create your first tunnel](https://developers.cloudflare.com/tunnel/get-started/)
Set up a tunnel in under 5 minutes using the dashboard or API.
### [Routing](https://developers.cloudflare.com/tunnel/concepts/routing/)
DNS records, protocols, and load balancing for published applications.
### [Integrations](https://developers.cloudflare.com/tunnel/integrations/)
Cloudflare One, Workers VPC, Load Balancing, Access, and more.
### [Configuration](https://developers.cloudflare.com/tunnel/configuration/)
Replicas, firewall rules, tokens, and runtime parameters.
[NextOverview](https://developers.cloudflare.com/tunnel/get-started/)
Was this helpful?
YesNo
[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/tunnel/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
## On this page
  * [Overview](https://developers.cloudflare.com/tunnel/#_top)
  * [How it works](https://developers.cloudflare.com/tunnel/#how-it-works)
  * [Use cases](https://developers.cloudflare.com/tunnel/#use-cases)
  * [Get started](https://developers.cloudflare.com/tunnel/#get-started)


Was this helpful?
YesNo
[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/tunnel/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
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

