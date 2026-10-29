[Skip to content](https://developers.cloudflare.com/turnstile/#main-content)
> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/turnstile/llms.txt  
> Use this file to discover all available pages before exploring further.
[![](https://developers.cloudflare.com/_astro/logo.te5VL_aD.svg)Docs](https://developers.cloudflare.com/)[Directory](https://developers.cloudflare.com/directory/)[API](https://developers.cloudflare.com/api/)[SDKs](https://developers.cloudflare.com/fundamentals/api/reference/sdks/)[Changelog](https://developers.cloudflare.com/changelog/)
Search`Ctrl``K`[](https://github.com/cloudflare/cloudflare-docs)[Log inDashboard](https://dash.cloudflare.com/)
[](https://developers.cloudflare.com/)[Turnstile](https://developers.cloudflare.com/turnstile/)
`/`
  * [Overview](https://developers.cloudflare.com/turnstile/)
  * [Plans](https://developers.cloudflare.com/turnstile/plans/)
  * [Spin](https://developers.cloudflare.com/turnstile/spin/)
  * Concepts
    * [Turnstile widgets](https://developers.cloudflare.com/turnstile/concepts/widget/)
    * [Cloudflare Challenges ↗︎](https://developers.cloudflare.com/cloudflare-challenges/)
  * Get started
    * [Overview](https://developers.cloudflare.com/turnstile/get-started/)
    * Widget management
      * [Cloudflare dashboard](https://developers.cloudflare.com/turnstile/get-started/widget-management/dashboard/)
      * [API](https://developers.cloudflare.com/turnstile/get-started/widget-management/api/)
      * [Terraform](https://developers.cloudflare.com/turnstile/get-started/widget-management/terraform/)
    * Embed the widget
      * [Overview](https://developers.cloudflare.com/turnstile/get-started/client-side-rendering/)
      * [Widget configurations](https://developers.cloudflare.com/turnstile/get-started/client-side-rendering/widget-configurations/)
    * [Validate the token](https://developers.cloudflare.com/turnstile/get-started/server-side-validation/)
    * [Mobile implementation](https://developers.cloudflare.com/turnstile/get-started/mobile-implementation/)
  * Additional configurations
    * Hostname management
      * [Overview](https://developers.cloudflare.com/turnstile/additional-configuration/hostname-management/)
      * [Pre-clearance configuration](https://developers.cloudflare.com/turnstile/additional-configuration/hostname-management/pre-clearance/)
      * [Any Hostname](https://developers.cloudflare.com/turnstile/additional-configuration/hostname-management/any-hostname/)
    * [Pre-clearance support ↗︎](https://developers.cloudflare.com/cloudflare-challenges/concepts/clearance/#pre-clearance-support-in-turnstile)
    * [Ephemeral IDs](https://developers.cloudflare.com/turnstile/additional-configuration/ephemeral-id/)
    * [Offlabel](https://developers.cloudflare.com/turnstile/additional-configuration/offlabel/)
  * Turnstile Analytics
    * [Overview](https://developers.cloudflare.com/turnstile/turnstile-analytics/)
    * [Challenge outcome](https://developers.cloudflare.com/turnstile/turnstile-analytics/challenge-outcomes/)
    * [Token validation](https://developers.cloudflare.com/turnstile/turnstile-analytics/token-validation/)
  * Migration
    * [Overview](https://developers.cloudflare.com/turnstile/migration/)
    * [Migrate from reCAPTCHA](https://developers.cloudflare.com/turnstile/migration/recaptcha/)
    * [Migrate from hCaptcha](https://developers.cloudflare.com/turnstile/migration/hcaptcha/)
  * [Tutorials](https://developers.cloudflare.com/turnstile/tutorials/)
  * Troubleshooting
    * [Testing](https://developers.cloudflare.com/turnstile/troubleshooting/testing/)
    * [Rotate secret key](https://developers.cloudflare.com/turnstile/troubleshooting/rotate-secret-key/)
    * Client-side errors
      * [Overview](https://developers.cloudflare.com/turnstile/troubleshooting/client-side-errors/)
      * [Error codes](https://developers.cloudflare.com/turnstile/troubleshooting/client-side-errors/error-codes/)
    * [Challenge solve issues ↗︎](https://developers.cloudflare.com/cloudflare-challenges/troubleshooting/challenge-solve-issues/)
    * [Feedback reports](https://developers.cloudflare.com/turnstile/troubleshooting/feedback-reports/)
  * Extensions
    * [Pages Plugin ↗︎](https://developers.cloudflare.com/pages/functions/plugins/turnstile/)
    * [Google Firebase](https://developers.cloudflare.com/turnstile/extensions/google-firebase/)
    * [Waiting Room Analytics ↗︎](https://developers.cloudflare.com/waiting-room/waiting-room-analytics/#turnstile-widget-traffic)
  * Reference
    * [Content Security Policy](https://developers.cloudflare.com/turnstile/reference/content-security-policy/)
    * [Turnstile Privacy Addendum](https://www.cloudflare.com/turnstile-privacy-policy/)
    * [Supported languages](https://developers.cloudflare.com/turnstile/reference/supported-languages/)
    * [Supported browsers ↗︎](https://developers.cloudflare.com/cloudflare-challenges/reference/supported-browsers/)
  * [Community resources](https://developers.cloudflare.com/turnstile/community-resources/)
  * [Changelog](https://developers.cloudflare.com/turnstile/changelog/)
  * Agent resources
    * [Agent setup ↗︎](https://developers.cloudflare.com/agent-setup/)
    * [Cloudflare Skills ↗︎](https://github.com/cloudflare/skills)
    * [Code Mode MCP Server ↗︎](https://github.com/cloudflare/mcp)
    * [Domain-specific MCP Servers ↗︎MCP](https://github.com/cloudflare/mcp-server-cloudflare)
    * [Turnstile llms.txt ↗︎](https://developers.cloudflare.com/turnstile/llms.txt)
    * [Turnstile llms-full.txt ↗︎](https://developers.cloudflare.com/turnstile/llms-full.txt)
    * [Cloudflare Docs llms.txt ↗︎](https://developers.cloudflare.com/llms.txt)
    * [Cloudflare Docs llms-full.txt ↗︎](https://developers.cloudflare.com/llms-full.txt)


  1. [Home](https://developers.cloudflare.com/)
  2. /Turnstile


# Cloudflare Turnstile
Last updated Aug 14, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/turnstile/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)
Overview How Turnstile works Widget types Accessibility Features Related products More resources
Cloudflare's smart CAPTCHA alternative.
Turnstile can be embedded into any website without sending traffic through Cloudflare and works without showing visitors a CAPTCHA.
Cloudflare issues challenges through the [Challenge Platform](https://developers.cloudflare.com/cloudflare-challenges/), which is the same underlying technology powering [Turnstile](https://developers.cloudflare.com/turnstile/).
In contrast to our Challenge page offerings, Turnstile allows you to run challenges anywhere on your site in a less-intrusive way without requiring the use of Cloudflare's CDN.
## How Turnstile works
[](https://developers.cloudflare.com/turnstile/#how-turnstile-works)
![Turnstile Overview](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=3757,height=2700,format=webp/_astro/turnstile-overview.BlA8uXVD.png)
Turnstile adapts the challenge outcome to the individual visitor or browser. First, we run a series of small non-interactive JavaScript challenges to gather signals about the visitor or browser environment.
These challenges include proof-of-work (computational puzzles), proof-of-space, probing for web APIs, and various other challenges for detecting browser-quirks and human behavior. As a result, we can fine-tune the difficulty of the challenge to the specific request and avoid showing a visual or interactive puzzle to a user.
Turnstile performs client-side security challenges on behalf of the website operator to distinguish human visitors from automated traffic. To do so, Turnstile processes only the data strictly necessary to provide this security function. Turnstile does not access, store, or transmit user communications, form entries, or other page inputs.
Note
For detailed information on Turnstile's data privacy practices, refer to the [Turnstile Privacy Addendum ↗︎](https://www.cloudflare.com/turnstile-privacy-policy/).
### Widget types
[](https://developers.cloudflare.com/turnstile/#widget-types)
Turnstile [widget types](https://developers.cloudflare.com/turnstile/concepts/widget/) include:
  * **Managed** (recommended): Automatically decides whether to show a checkbox based on visitor risk level.
  * **Non-interactive** : Visitors never need to interact with the widget.
  * **Invisible** : The widget is completely hidden from the visitor.


* * *
## Accessibility
[](https://developers.cloudflare.com/turnstile/#accessibility)
Turnstile is WCAG 2.2 AA compliant.
* * *
## Features
[](https://developers.cloudflare.com/turnstile/#features)
[Turnstile Analytics](https://developers.cloudflare.com/turnstile/turnstile-analytics/)
Assess the number of challenges issued, evaluate the [challenge solve rate](https://developers.cloudflare.com/cloudflare-challenges/reference/challenge-solve-rate/), and view the metrics of issued challenges.
Use Turnstile Analytics
[Pre-clearance](https://developers.cloudflare.com/cloudflare-challenges/concepts/clearance/#pre-clearance-support-in-turnstile)
Integrate Cloudflare challenges on single-page applications (SPAs) by allowing Turnstile to issue a Pre-Clearance cookie.
Use Pre-clearance
* * *
## Related products
[](https://developers.cloudflare.com/turnstile/#related-products)
[Bots](https://developers.cloudflare.com/bots/)
Cloudflare bot solutions identify and mitigate automated traffic to protect your domain from bad bots.
[DDoS Protection](https://developers.cloudflare.com/ddos-protection/)
Detect and mitigate Distributed Denial of Service (DDoS) attacks using Cloudflare's Autonomous Edge.
[WAF](https://developers.cloudflare.com/waf/)
Get automatic protection from vulnerabilities and the flexibility to create custom rules.
* * *
## More resources
[](https://developers.cloudflare.com/turnstile/#more-resources)
### [Plans](https://developers.cloudflare.com/turnstile/plans/)
Learn more about Turnstile's plan availability.
[NextPlans](https://developers.cloudflare.com/turnstile/plans/)
Was this helpful?
YesNo
[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/turnstile/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
## On this page
  * [Overview](https://developers.cloudflare.com/turnstile/#_top)
  * [How Turnstile works](https://developers.cloudflare.com/turnstile/#how-turnstile-works)
  * [Widget types](https://developers.cloudflare.com/turnstile/#widget-types)
  * [Accessibility](https://developers.cloudflare.com/turnstile/#accessibility)
  * [Features](https://developers.cloudflare.com/turnstile/#features)
  * [Related products](https://developers.cloudflare.com/turnstile/#related-products)
  * [More resources](https://developers.cloudflare.com/turnstile/#more-resources)


[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/turnstile/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
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

