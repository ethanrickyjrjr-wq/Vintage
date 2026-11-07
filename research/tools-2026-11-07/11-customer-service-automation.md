# Lane 11. Customer service automation: messaging, bookings, link pages and small workflows

Date 2026-11-07. Author: research subagent (lane 11-customer-service-automation).
Question: Which tools automate buyer messages, replies, bookings, link pages and small workflows for a one-person vintage shop (Holliewood and Vine), and what do they cost today?
Legend: V = vendor page read today (2026-11-07) with the fetch script; U = unverified (snippet, memory, or the page would not load). Prices are quoted as the vendor writes them. WebSearch ran out after three queries (shared budget), so most pages were reached by direct URL; see section 4.

## 0. Bottom line

- Etsy already ships the message automation Hollie needs, free: temporary and weekly auto-replies, quick replies (Etsy's templates or her own), and a US-only AI writing assistant inside Messages. Auto-replies count as a reply toward the Star Seller target (95% of first messages answered within 24 hours). Auto-replies are set on Etsy.com only, not in the Etsy Seller app. (V)
- Shopify's free layer covers the Shopify side once the store exists: Shopify Inbox (free; quick replies, availability hours, optional AI "Inbox agent"; desktop, iOS and Android apps), Shopify Flow (free on Basic), Shopify Email (10,000 emails a month free), and pickup in store (built in). The only cost is the Shopify plan: Basic is $39 USD/mo monthly or $29 USD/mo yearly. (V)
- Bookings for Hire Hollie: Cal.com Free is the pick. Free for one user, "no usage limits", and it accepts Stripe and PayPal payments on the free tier, which matches the rule "payment online before any visit". Setmore Free (up to 4 users, accepts payments, email reminders) is the backup. Calendly Free allows one event type and puts payments on the paid tier. Acuity has no free plan ($16/ month Starter). Square Appointments is $0/mo but you pay card processing (2.6% + 15 cents in person, 2.9% + 30 cents online). (V)
- If the booking must live inside Shopify: Appointo Free (unlimited services and bookings, email notification), then Pro at $14 / month for reminders and calendar sync. BTA Free stops at 10 bookings. Sesami's free plan is for development stores only; paid starts at $19 / month. (V)
- Small workflows: Zapier Free gives 100 tasks a month and two-step Zaps, but Shopify is a Premium app on Zapier (paid plan) and Etsy has no Zapier integration at all. n8n self-hosted Community edition is free indefinitely and its licence allows "your own internal business purposes"; it can run on the Fedora box. IFTTT Free gives 1,000 credits a month with hourly polling. Make's pricing page was walled today (U). (V unless marked)
- Link page: Linktree Free (unlimited basic links) or Beacons Free (includes "Smart Reply IG auto-DM" but 9% seller fees on anything sold through it). Instagram auto-replies on Linktree need Premium ($30 /mo billed annually). Stan Store's price page would not load (U) and it is built for digital creators, not a resale shop.
- Text expansion on the Windows PC: Espanso, free, GPL-3, Windows/macOS/Linux. TextExpander Free caps at 5 active snippets; Pro is $5 /user/mo billed annually at $60. PowerToys is free but is not a snippet expander.
- Help desks (Tidio, Gorgias, Help Scout, Crisp, tawk.to) are overkill for one person selling one-of-one pieces. If a shared inbox is ever needed: Tidio Free (50 conversations), Crisp Free (2 seats), Help Scout Free (5 users, 1 inbox, 100 contacts a month), or Gorgias Helpdesk Starter at $10/mo for 50 tickets.
- Phone: Google Voice personal gives a US number of your choice and free calls to the US and Canada, but its Acceptable Use Policy bans "sending messages via an automated process, such as a script", so no scripted SMS through it. OpenPhone now sells as Quo: Starter $15 per user/per month billed annually at $180, plus a one-time $19.50 carrier registration fee for business texting.
- Reviews: Judge.me Free has unlimited review requests; $15 per month is "the most you can ever pay". It lists Etsy among review import sources. Drafting replies and policies: Claude Free or Pro ($17 per month annual, $20 monthly); ChatGPT Plus $20/month, monthly billing only. Pushover ($4.99 one-time per platform) and ntfy (free, open source) stay as the alert channel already decided.

## 1. Comparison table

| Tool | What it does | Price (verbatim quote) | Free tier | Platform | Fit for Hollie | V/U | Source URL |
|---|---|---|---|---|---|---|---|
| Etsy Messages: auto-replies, quick replies, writing assistant | Built-in buyer messaging with away auto-replies, canned replies and AI drafts | Included with an Etsy shop; no price shown | Yes (built in) | Etsy.com web; Etsy Seller app (quick replies only) | High: covers Etsy messaging on day one | V | https://help.etsy.com/hc/en-us/articles/115015654988-How-to-Send-Messages-to-Buyers |
| Etsy Star Seller rule | The response target automation must hit | "reply to 95% of first messages in a thread within 24 hours" | n/a | Etsy | High: sets the bar for auto-replies | V | https://help.etsy.com/hc/en-us/articles/4403058372503-What-is-the-Star-Seller-Badge |
| Etsy Seller app | Phone app for orders and messages; push notifications | Free (no price shown on pages read) | Yes | iOS, Android | High for replying from the iPhone; notification details unverified | U (existence V) | https://help.etsy.com/hc/en-us/articles/115015654988-How-to-Send-Messages-to-Buyers |
| eBay automatic feedback | Leaves positive feedback for buyers automatically | "Seller Hub ... It's free to use" | Yes | eBay web (Selling preferences) | Medium: useful once eBay opens; one toggle | V | https://www.ebay.com/help/selling/feedback-policies/automatic-feedback?id=4101 |
| eBay automated buyer messages / time away | Auto-response while away | Not reached today | Unknown | eBay web | Medium | U | (eBay help page not reached; see section 4) |
| Shopify Inbox | Store chat with quick replies, hours, optional AI agent | "Pricing Free" | Yes (whole app) | Shopify app; desktop, iOS, Android apps | High once the Shopify site is live | V | https://apps.shopify.com/inbox |
| Shopify Flow | Trigger/condition/action automations inside Shopify | "a free app available on the Basic, Grow, Advanced, and Plus plans" | Yes with any paid plan | Shopify app | High: tag orders, notify, auto-email | V | https://help.shopify.com/en/manual/shopify-flow |
| Shopify Sidekick | AI assistant in admin; can build Flow workflows | No price on pages read; plan requirement not stated | Unknown | Shopify admin desktop; Shopify app | Medium: handy, not essential | V (price U) | https://help.shopify.com/en/manual/ai-powered-tools/sidekick |
| Shopify Email | Email campaigns and automations | "up to 10,000 manual or automated emails for free. After that ... $1 USD per 1,000 additional emails" | Yes, 10,000/mo | Shopify app | High for order and review follow-ups | V | https://www.shopify.com/email-marketing |
| Shopify pickup in store | Local pickup option at checkout | Built in; no fee shown | Yes | Shopify admin | High for Fort Myers/Naples hand-offs | V | https://help.shopify.com/en/manual/fulfillment/setup/delivery-methods/pickup-in-store |
| Shopify plan (context) | Required for all Shopify tools above | "Pay monthly $39 USD/mo ... Pay yearly $29 USD/mo" (Basic) | 3-day trial, then $1/month for 3 months | Web | Required cost, already decided elsewhere | V | https://www.shopify.com/pricing |
| Tidio | Live chat, ticketing, Lyro AI agent, Flows | Starter "$24.17 /mo." (annual toggle shown); Growth "Starts at $49.17 /mo." | "Free Plan 50 Billable conversations $0/mo." | Web app; Shopify app | Low: more than one person needs | V | https://www.tidio.com/pricing/ |
| Gorgias | Ecommerce help desk plus AI agent | Helpdesk Starter "$10/mo Billed monthly" for "50 tickets / month"; with AI Agent "$40/mo" | Trial only | Web; Shopify app | Low: built for brands with teams | V | https://www.gorgias.com/pricing |
| Help Scout | Shared inbox and docs site | Standard "$25 per user/mo" | "The Free plan includes 5 users, 1 Inbox, and 1 Docs site" (100 contacts/mo) | Web; mobile app | Low to medium: free tier is fine if email volume grows | V | https://www.helpscout.com/pricing/ |
| Crisp | Chat widget and shared inbox | Mini "45 per month, per workspace" | "Free forever": widget, 2 seats, mobile apps | Web; mobile apps | Low to medium | V | https://crisp.chat/en/pricing/ |
| tawk.to | Free live chat widget | Remove branding "$29/month"; AI Assist "from as little as $29/month" | "free for life" with branding | Web widget | Medium: free chat for a non-Shopify site | V | https://www.tawk.to/why-free/ |
| Zapier | Cloud automations between apps | Professional "Starting from $19.99 /month" (toggle not confirmed) | "Free forever $0 /month ... 100 tasks per month", two-step Zaps | Web | Medium: Shopify is a Premium app; no Etsy integration | V | https://zapier.com/pricing |
| Make | Cloud automations | Page walled today | Memory: free tier exists | Web | Medium | U | https://www.make.com/en/pricing (HTTP 403) |
| n8n | Workflow automation, cloud or self-hosted | Cloud Starter "20€ /mo, billed annually" for "2.5k workflow executions" | Self-hosted Community edition "free ... indefinitely" | Self-host (Docker); web cloud | High if the Fedora box runs it; licence allows internal business use | V | https://n8n.io/pricing/ and https://docs.n8n.io/n8n-community-license |
| IFTTT | Simple applets between services | Starter "$2.09 / month $25.08 billed annually"; Pro "$5.49 / month $65.88 billed annually" | "Free $0.00 / month 1,000 credits / month", hourly polling | Web; mobile apps (not checked today) | Medium: cheap, simple, few commerce apps | V | https://ifttt.com/plans |
| Google Voice (personal) | US phone number for calls, texts, voicemail | Personal price not shown; "almost all Google Voice calls to the US and Canada are free" | Yes (personal) | Web (Windows, macOS, Chrome OS), iPhone, Android | High for a shop number; no scripted texting allowed | V | https://support.google.com/voice/answer/115061 |
| Google Voice (Workspace) | Business phone tiers | Tiers listed at "$10", "$20", "$30" | No | Web, mobile | Low: needs Workspace | V | https://workspace.google.com/products/voice/ |
| Quo (formerly OpenPhone) | Business phone and texting with shared inbox | Starter "$15 Per user/per month Billed annually at $180" | 7-day trial | Web; apps not checked today | Low to medium: only if a business line with texting is wanted | V | https://www.quo.com/pricing |
| Calendly | Booking page | Standard Plus "$18 /seat/mo" (with Notetaker add-on shown) | "Always free": "One event type", "One calendar connection" | Web; browser extension | Medium: free tier has no payments | V | https://calendly.com/pricing |
| Cal.com | Booking page, open source | Teams "$12per user/month" yearly | "Free forever": 1 user, unlimited links, "Accept Stripe & PayPal payments" | Web; mobile app; browser extension | High: free with payments, fits Hire Hollie | V | https://cal.com/pricing |
| Acuity Scheduling | Booking with payments and forms | Starter "$16/ month" (annual toggle shown); Standard "$27/ month"; Premium "$55/ month" | "7-day trial, no credit card needed"; no free plan | Web | Medium: good, but paid from day one | V | https://acuityscheduling.com/pricing |
| Square Appointments | Booking site with Square payments | "$0/mo. per location", "$49/mo. per location", "$149/mo. per location" | Yes: "no monthly subscription costs - you only pay processing fees" | Web; Square apps | Medium: free, but 2.9% + 30 cents online | V | https://squareup.com/us/en/appointments/pricing |
| Setmore | Booking page with payments | Pro "$5 user / month" annual billing | "Up to 4 users $0 user / month", unlimited appointments, accept payments | Web; iOS and Android apps | High as a free backup to Cal.com | V | https://www.setmore.com/pricing |
| Sesami (Shopify) | Bookings sold as Shopify products | Small "$19 / month"; Pro "$129 / month"; Premium "$299 / month" | Free plan "Available for development stores" only | Shopify app | Low: free tier is not for live stores | V | https://apps.shopify.com/sesami |
| BTA Appointment Booking (Shopify) | Bookings inside Shopify | Lite "$25 / month or $250/year and save 17%" | "FREE ... 10 bookings" | Shopify app | Low to medium: 10 bookings then $25 | V | https://apps.shopify.com/bookthatapp |
| Appointo (Shopify) | Bookings inside Shopify | Pro "$14 / month or $151/year and save 10%" | "Free ... Unlimited Services, Unlimited Bookings, Email Notification" | Shopify app | High if booking must be on Shopify | V | https://apps.shopify.com/appointo-appointments-and-bookings |
| Linktree | Link-in-bio page | Starter "$7 /mo Billed annually, or $9 monthly"; Pro "$14 /mo ... or $17 monthly"; Premium "$30 /mo ... or $35 monthly" | "Free: Unlimited basic links, Email and phone sign-ups" | Web; mobile | High for the Instagram bio | V | https://linktr.ee/s/pricing |
| Beacons | Link-in-bio with store and IG auto-DM | Creator "$8.33 /mo" ($100 billed annually) or "$10" monthly | "Free forever $0 /month", "9% seller fees", "Smart Reply IG auto-DM" | Web; mobile | Medium: free IG auto-DM, but fees if selling through it | V | https://beacons.ai/i/pricing |
| Stan Store | Creator storefront and link page | Price page 404 today | "Try Stan for 14 Days Free"; "0% Transaction Fees, Always." | Web; mobile | Low: built for courses and coaching | U (price) | https://stan.store/ |
| Espanso | Text expander | Free | Yes, "licensed under the GPL-3 license" | Windows, macOS, Linux | High: free canned replies anywhere on the PC | V | https://espanso.org/ |
| TextExpander | Text expander with sync | Pro "$5 /user/mo ... Billed annually at $60 USD"; Business "$10 /user/mo" | "$0 forever": "Active Snippets 5", "Snippet Swap 1 every 2 weeks" | Mac, Windows, Chrome, iPhone and iPad, Android (beta) | Medium: only if iPhone snippets matter | V | https://textexpander.com/pricing |
| Microsoft PowerToys | Windows utilities (Advanced Paste, Keyboard Manager) | Free | Yes, "free, open-source utilities" | Windows | Low: not a snippet tool | V | https://learn.microsoft.com/en-us/windows/powertoys/ |
| Claude | Draft replies, policies, listing copy | Pro "$17 Per month with annual subscription discount ($200 billed up front). $20 if billed monthly." | "Free $0" with usage limits | Web, desktop, mobile | High for policy drafting; Haiku already planned for listings | V | https://claude.com/pricing |
| ChatGPT | Draft replies and policies | Plus "$20/month (billed monthly)"; "we do not support annual billing" | Free plan exists | Web and apps | Medium: duplicate of Claude | V | https://help.openai.com/en/articles/6950777-what-is-chatgpt-plus |
| Judge.me | Review requests and display | "Awesome $15 per month" | "Free $0 per month ... Unlimited product & store reviews" | Shopify app (also other platforms); imports Etsy reviews | High for Shopify reviews, free | V | https://judge.me/pricing |
| Google Forms | Intake forms (styling requests, pickup times) | No price on page read | Common knowledge that it is free with a Google account (not stated on page) | Web | Medium: free intake for Hire Hollie | U (page V, price U) | https://workspace.google.com/products/forms/ |
| Typeform | Branded forms | Basic "28 USD / mo" (annual toggle shown) for "100 responses/mo" | Free plan with "a limited number of responses per month" | Web | Low: Google Forms does the job | V | https://www.typeform.com/pricing |
| Pushover | Push alerts (already decided) | "$4.99 USD one-time purchase on each platform" | 30-day trial; "10,000 messages per month for free" | iOS, Android, Desktop | Already in use | V | https://pushover.net/pricing |
| ntfy | Push alerts (already decided) | Supporter "$6" monthly or "$5" annually "/ month" | "Try ntfy for free without sign-up"; open source | Web, iOS, Android, self-host | Already in use | V | https://ntfy.sh/ |
| Facebook Marketplace API | Automation of Marketplace listings or messages | n/a | n/a | n/a | None: only "Marketplace Partnerships" for approved partners | V | https://developers.facebook.com/docs/marketplace/ |

## 2. Notes per tool

### Etsy Messages (auto-replies, quick replies, writing assistant). V
- Two auto-reply types. Temporary: "from an hour to a maximum of five days"; for longer, Etsy says use Vacation Mode. Weekly: "your available hours must be at least 8 hours long on the days you choose, and you need to select at least 4 days a week."
- "Both temporary and weekly auto replies are only sent in response to the first message a shopper sends you, and count as a reply towards your Star Seller messaging score."
- "Auto-replies can only be managed on Etsy.com and not the Etsy Seller app." Quick replies work on both.
- Quick replies: "you have the option to use pre-written messages created by Etsy, or make your own replies and categories." Limits on count were not on the page.
- "US sellers can also use the writing assistant to automatically draft quick, accurate, and personalized messages to buyers." It can be turned off under Reply preferences.
- Attachments: up to 3 files, .jpg, .gif, .pdf or .png, up to 100MB.
- Listing pages show the shop's average response time to shoppers.

### Etsy Star Seller and customer service standards. V
- Star Seller: "Message response rate: reply to 95% of first messages in a thread within 24 hours"; "On-time shipping & tracking: 95%"; "Average review ratings: 4.8+". Eligible "starting 90 days after your first sale" with "at least 5 orders and $300 in sales over the past 3 months". Reviewed on the 1st of each month over the past 3 months.
- Minimum customer service standard (all sellers): "Reply to 80% of first messages in a thread within 24–48 hours". Falling below "may lower your search visibility".
- Implication: a weekly auto-reply covering the hours Hollie is away satisfies the 24-hour clock without a paid tool.

### Etsy Seller app. U (existence V)
- Etsy's help page refers to "the Etsy Seller app" for messages and orders. The App Store and Google Play listings I tried returned 404 (wrong IDs), so push-notification details are unverified today.

### eBay automatic feedback. V
- Setting lives in "the All listings and orders section of the Selling preferences page". Options: "After the buyer has paid" or "After the buyer has paid and left you positive feedback"; stored positive comments are used at random and can be edited. Seller Hub "is free to use".
- Automated buyer messages and the time-away auto-response page were not reached (the id I tried redirected to the seller-performance article; the feedback article hit a captcha). U.
- Terms gotcha (V, eBay User Agreement): you may not "use any robot, spider, scraper, data mining tools, data gathering and extraction tools, or other automated means (including, without limitation buy-for-me agents, LLM-driven bots ...) to access our Services for any purpose, except with the prior express permission of eBay". Any eBay automation must go through official tools or the eBay API, never a browser bot.

### Shopify Inbox. V
- App Store pricing: "Free". Feature list includes "Quick replies", "Automated responses", "FAQs", "Business hours", "Push notifications".
- Help: "turn on an Inbox agent to respond to customers automatically", trained on "your product catalog, store policies, Knowledge Base facts and files, and published storefront content". Staff can "send product links, send discount codes, and send images". Apps for desktop, iOS and Android.
- Reviews: 4.5 from 5,820. Requires a Shopify plan.

### Shopify Flow. V
- "Shopify Flow is a free app available on the Basic, Grow, Advanced, and Plus plans." Gotcha: "Stores on the Grow, Advanced, and Plus plans can use the Send HTTP Request action", so on Basic, Flow cannot call outside webhooks (for example to Pushover or n8n) directly. Basic can still use Flow's built-in actions (tag, email, internal notifications) and installed apps' actions.

### Shopify Sidekick. V (plan requirement U)
- "Sidekick can build Shopify Flow workflows that do repeated work for you." Works "from any page in your Shopify admin on desktop or in the Shopify app". Neither page read stated a price or a plan gate.

### Shopify Email. V
- "Every month, you can send up to 10,000 manual or automated emails for free. After that, only pay for what you use at $1 USD per 1,000 additional emails sent". Plenty for review requests and pickup reminders at Hollie's volume. The help-center pricing page returned 403; the marketing page was read instead.

### Shopify pickup in store. V
- Requirements: "at least one location that fulfills online orders" and "the latest version of checkout". Customers can mix shipped and pickup items in one order. Note the space is unconfirmed as a home (CLAUDE.md), so pickup address and hours need Ricky's decision before this is switched on.

### Tidio. V
- Free Plan: "50 Billable conversations $0/mo.", Lyro "50 Lyro AI conversations (one-time)", Flows "100 visitors reached". "Your first 50 conversations are free (lifetime)" reads as a lifetime cap on the free AI, not monthly; the FAQ says the free limit "will refresh after 30 days" for conversations. Starter $24.17/mo. and Growth from $49.17/mo. were shown with the annual toggle. Branding removal is a paid feature ("No Tidio branding"). Overkill for one person.

### Gorgias. V
- Helpdesk-only Starter "$10/mo Billed monthly · cancel anytime", "50 tickets / month", "Then a $0.40 per-ticket fee past your limit." Adding AI Agent makes it "$40/mo" with "30 automated interactions" then "$1.50 per automated interaction". Basic is $60/mo helpdesk-only (300 tickets) or $90 monthly / $77 annual with AI. Built for Shopify brands with support teams. Skip.

### Help Scout. V
- "The Free plan includes 5 users, 1 Inbox, and 1 Docs site." Free contacts "100/mo". Standard "$25 per user/mo" (annual toggle, -16%). Reasonable if a shared email inbox is ever wanted; not needed now.

### Crisp. V
- Free "forever": "Website chat widget", "2 seats included", "No AI credits included", "Shared inbox", "Mobile applications", "E-Commerce integrations". Mini "45 per month, per workspace". A fair free widget for a non-Shopify site.

### tawk.to. V
- "Don't remove it, and it is free for life." Branding removal "$29/month". AI Assist "from as little as $29/month. We also have a forever-free plan for sites with limited chat volume." Human agents "$1/hour". The pricing URL redirects to the "why free" page. Good free chat for a standalone site; Shopify Inbox is the simpler choice on Shopify.

### Zapier. V
- Free: "$0 /month ... Zaps, Tables, and Forms included (100 tasks per month)", "Two-step Zaps", "Zapier checks for new data every 15 min on the Free plan". Professional "Starting from $19.99 /month" (the page has monthly and yearly toggles; which one rendered was not confirmed, so the monthly price may be higher).
- Gotchas: Shopify is marked "Premium" ("Premium apps: Shopify"), and premium apps are a Professional-plan feature ("Unlimited premium apps"). "Etsy has not yet built an integration on Zapier." So the Etsy-first phase gets nothing from Zapier without webhooks.

### Make. U
- make.com/en/pricing returned HTTP 403 twice and three help.make.com URLs were 404. From memory only: a free tier with about 1,000 operations a month and a Core plan near $9 to $11 a month. Treat as unverified.

### n8n. V
- Cloud: Starter "20€ /mo, billed annually" for "2.5k workflow executions", Pro "50€ /mo, billed annually" for 10k. Self-hosted: "You can stick with the free Community edition indefinitely, register for free to unlock extra features".
- Licence (Sustainable Use License): "You may use or modify the software only for your own internal business purposes or for non-commercial or personal use." Hollie's own shop automations are internal business use, so the free Community edition is allowed. Not an OSI open-source licence; do not resell it as a service.
- Fit: runs as a container on the Fedora box next to crawl4ai; can poll Etsy's API, post to Pushover or ntfy, and write to Supabase. Needs setup time; the dashboard plan already covers much of this.

### IFTTT. V
- Free "$0.00 / month", "1,000 credits / month", "Unlimited Applets", polling "Every hour". Starter "$2.09 / month $25.08 billed annually"; Pro "$5.49 / month $65.88 billed annually" with 5-minute polling. Few commerce services; fine for simple phone or calendar nudges.

### Google Voice. V
- Personal setup page: "Google Voice gives you a phone number for calls, texts, and voicemails ... If you're in the US, you can choose your own number." "When you call from the US, almost all Google Voice calls to the US and Canada are free." Supported: Chrome OS, macOS, Windows, iPhone, Android. The personal plan's $0 price was not stated on the pages read; the Workspace Voice page lists business tiers at $10, $20 and $30.
- Terms gotcha (Acceptable Use Policy): "Do not send or facilitate the transmission of spam, large numbers of commercial messages, or automated messages", including "sending messages via an automated process, such as a script". So Google Voice is a shop phone number, not an SMS automation channel.

### Quo (formerly OpenPhone). V
- openphone.com/pricing redirects to quo.com/pricing; footer reads "© 2026 OpenPhone Technologies, Inc." Starter "$15 Per user/per month Billed annually at $180"; Business "$23" ($276/yr); Scale "$35" ($420/yr). Monthly-billing prices did not render. Includes "One new or ported phone number (local or toll-free) per user" and "1,000 free automation credits". Gotcha: US business texting registration via "The Campaign Registry ... one-time fee of $19.50". Only worth it if Hire Hollie needs a separate texting line.

### Calendly. V
- Free: "Always free", "One event type", "One calendar connection", "Browser extension". Payments ("Connect Stripe, PayPal") sit in Standard Plus at "$18 /seat/mo" as displayed (bundled with Notetaker and Callie; a cheaper plain Standard may exist but did not render). For paid-before-visit bookings, free Calendly does not do it.

### Cal.com. V
- "Free forever", "1 user", "Unlimited links & calendars", "Email & SMS notifications", "Mobile App", "Browser Extension", "Accept Stripe & PayPal payments", "1-click import Calendly events". "Free for individuals, no credit card, no usage limits." Teams "$12per user/month" yearly removes branding. Open source and self-hostable, but the hosted free plan is enough.
- Fit: the hire page has no booking link; the handoff says no Cal.com link is configured. A Cal.com event type with a Stripe payment step satisfies "payment online before any visit" and the free Screen Test can be a separate free event type.

### Acuity Scheduling. V
- Starter "$16/ month": "1 calendar", "Payments via Stripe, Square, PayPal, Venmo", "Email reminders", "Custom client forms". Standard "$27/ month" adds text reminders and waitlist; Premium "$55/ month". "7-day trial, no credit card needed." The page loaded with "Pay annually Save 20%" shown first, so these may be annual rates. No free plan. The old squarespace.com/scheduling/pricing URL is a "Moved" page.

### Square Appointments. V
- Plans: "$0/mo. per location", "$49/mo. per location", "$149/mo. per location". "With Square Free, there are no monthly subscription costs - you only pay processing fees". Free tier: "Online booking site and integrations", "Appointment reminders", "Unlimited staff calendars". Fees: in person "2.6% + 15¢", online "2.9% + 30¢", manually entered or card on file "3.5% + 15¢". Fine if Ricky also wants Square for in-person card sales; otherwise Cal.com plus Stripe is simpler.

### Setmore. V
- Free: "Up to 4 users $0 user / month", "Unlimited appointments", "Accept payments", "Branded Booking Page", "Email reminders", "iOS and Android apps". Pro "$5 user / month" (annual billing) adds "SMS & email reminders", "Remove Setmore branding", "Google Reviews". Solid free backup.

### Shopify booking apps. V
- Sesami: free plan "Available for development stores" only; Small "$19 / month" (5 resources, 1 email flow); Pro "$129 / month"; Premium "$299 / month"; "10-day free trial".
- BTA (BookThatApp): "FREE ... 10 bookings"; Lite "$25 / month or $250/year and save 17%" for "50 monthly bookings", "1 staff account", "1 booking type"; Premium "$49.95 / month"; Business "$110 / month". Rated 4.7 (421).
- Appointo: "Free ... Unlimited Services, Unlimited Bookings, Email Notification, Block Specific Dates, Multi Timezone & Language, POS, Admin Reschedule/Cancel"; Pro "$14 / month or $151/year and save 10%" adds "Email Reminders", "Google/Outlook Calendar Integration", "No Appointo Branding"; "Usage charge for text/whatsapp and 2% charge for subscriptions/bundles". Premium "$25 / month"; Advanced "$39 / month". Rated 4.9 (947). Best value if the booking should be a Shopify product with Shopify checkout.

### Linktree. V
- Free: "Unlimited basic links", "Email and phone sign-ups". Starter "$7 /mo Billed annually, or $9 monthly"; Pro "$14 /mo Billed annually, or $17 monthly" ("Remove Linktree branding", "Sell and earn with 0% fees"); Premium "$30 /mo Billed annually, or $35 monthly" ("Unlimited Instagram auto-replies", "Social media scheduling").

### Beacons. V
- Free: "$0 /month", "30 daily AI credits", "Sell unlimited digital products", "9% seller fees", "50 email sends per month", "Smart Reply IG auto-DM". Creator "$8.33 /mo" ("$100 billed annually") or "$10" monthly, "Free custom domain". Creator Plus "$25 /mo" ("$300 billed annually") with "0% seller fees". Gotcha: anything sold through the free page pays 9%.

### Stan Store. U
- stan.store/pricing and www.stan.store/pricing returned 404; the help center has no price page. Home page (V): "Try Stan for 14 Days Free", "0% Transaction Fees, Always." Built for "courses, digital products, and bookings"; memory says about $29/mo. Skip for a resale shop.

### Espanso. V
- "Espanso is open-source, licensed under the GPL-3 license." "Espanso supports Windows, Linux and macOS." Free. Snippets are YAML files, so the same canned replies can be versioned in the repo and reused on the Fedora box.

### TextExpander. V
- Free "$0 forever": "Active Snippets 5", "Snippet Swap 1 every 2 weeks", "Team members (users) 5". Pro "$5 /user/mo", "Billed annually at $60 USD"; Business "$10 /user/mo", "Billed annually at $120 USD". Platforms: "Mac, Windows, Chrome, iPhone and iPad, Android BETA". The iPhone keyboard is the only reason to pay; the free tier's 5 active snippets is too tight for reply templates.

### Microsoft PowerToys. V
- "a set of free, open-source utilities" for Windows. Utilities listed include Advanced Paste, Always On Top, Awake, Color Picker, Command Not Found and more; no snippet expander appeared in the section read. Useful for the PC, not for canned replies.

### Claude and ChatGPT. V
- Claude: Free "$0", "Limited usage every 5 hours and every week", "Chat on web, desktop, and mobile". Pro "$17 Per month with annual subscription discount ($200 billed up front). $20 if billed monthly." Max "$100 Per month".
- ChatGPT Plus: "$20/month (billed monthly)"; "we do not support annual billing". A Free plan exists.
- For Hollie: draft shop policies, FAQ and the quick-reply library once with Claude Free, paste into Etsy quick replies and Espanso. Etsy's own writing assistant handles live buyer replies on Etsy.com.

### Judge.me. V
- "Free $0 per month": "Unlimited product & store reviews", "Unlimited photo & video reviews", "Google Rich Snippets". "Awesome $15 per month" adds AI replies, social sharing, referrals. "$15 per month is the most you can ever pay us." Import sources listed include "Etsy", "Amazon", "Google Business Profile"; integrations include "Workflow Automation: Shopify Flow". Shopify app first; the page compares Shopify against other platforms.
- Etsy's own automatic review requests: no Etsy page on this was reached today (U). Etsy's quick-reply help mentions "asking buyers for a post-purchase review" as a quick-reply use.

### Google Forms and Typeform. V page, U price for Forms
- Google Forms page read; it has no price text (Forms is part of a Google account; U today). Typeform Basic "28 USD / mo" for "100 responses/mo included" (annual toggle shown); the free plan has "a limited number of responses per month". Use Google Forms for the Hire Hollie intake; skip Typeform.

### Pushover and ntfy. V (already in use, one line each)
- Pushover: "$4.99 USD one-time purchase on each platform", "up to 10,000 messages per month for free". ntfy: "100% free software", "Try ntfy for free without sign-up"; Supporter $5 to $6 a month if reserved topics are wanted.

### Facebook Marketplace. V
- Meta's developer page offers only "Marketplace Partnerships - Enable partners to distribute their products on the Facebook platform." Nothing for an individual seller to automate listings or messages. Treat Marketplace as manual-only.

## 3. Recommendation for Hollie

Install or sign up today (all free):
1. Etsy Messages: set a weekly auto-reply for the hours Hollie is away, write 8 to 12 quick replies (shipping time, local pickup, dimensions, condition, holds, "is it still available", review ask), keep the writing assistant on. This alone protects the Star Seller 24-hour metric.
2. Cal.com Free: one paid event type for Hire Hollie consults with Stripe collection, one free event type for the Screen Test. Put the link on site/hire.html when Ricky gives the inbox address. Setmore Free is the fallback if Cal.com's Stripe step disappoints.
3. Espanso on the Windows PC with the same reply library, so eBay, Shopify Inbox and email get identical answers.
4. Linktree Free for the Instagram bio, pointing at Etsy, the site and the hire page.
5. Google Voice personal number for the shop phone (calls free to US and Canada); never script texts through it.
6. Google Forms for Hire Hollie intake (room photos, budget, dates).

Once the Shopify store exists (included in the plan, no extra cost):
7. Shopify Inbox with quick replies and hours; turn on the Inbox agent only after the policies and Knowledge Base are written.
8. Shopify Flow for order tagging and internal alerts; Shopify Email for pickup and review follow-ups (10,000 free a month); pickup in store once the pickup address is decided.
9. Judge.me Free for review requests; it can also import Etsy reviews.

Pay only once it earns it:
- Appointo Pro at $14 / month if bookings must be Shopify products with reminders and calendar sync.
- Cal.com Teams at $12 per user/month yearly only to remove branding.
- Zapier Professional ($19.99 /month as displayed) only when a Shopify-to-outside automation cannot be done in Flow or n8n; remember Etsy has no Zapier app.
- n8n self-hosted (free) on the Fedora box if the dashboard plan needs glue the Supabase build does not cover; licence allows internal business use.
- Quo Starter ($15 per user/per month annual) only if Hire Hollie needs a business texting line.
- Linktree Premium ($30 /mo annual) or Beacons Free for Instagram auto-DM, if DM volume ever justifies it.

Skip and why:
- Gorgias, Tidio paid, Help Scout paid, Crisp paid: team help desks; one person with a few messages a day does not need ticket queues.
- Sesami: free tier is for development stores only; $19 / month minimum.
- BTA: 10 free bookings then $25 / month, worse than Appointo.
- Acuity: no free plan; Cal.com does the same for $0.
- Typeform: 100 responses for 28 USD / mo when Google Forms is free.
- Stan Store: creator courses and memberships; price unverified.
- TextExpander Free: 5 active snippets; Espanso has no cap.
- Any browser bot on eBay or Facebook Marketplace: eBay's User Agreement bans "LLM-driven bots" and scrapers without permission; Marketplace has partner-only access.

## 4. Gaps and pages that would not load

- WebSearch ran out after three queries (shared per-turn budget across agents). Everything after that was reached by direct URL. Pages I could not find a URL for: eBay automated buyer messages and time-away auto-response; Etsy automatic review request settings; the Etsy Seller app store listing (two guessed IDs returned 404).
- https://www.make.com/en/pricing and https://www.make.com/en/plans: HTTP 403 (bot wall). help.make.com/subscription-plans, /pricing and /make-pricing: 404. Make is U.
- https://stan.store/pricing and https://www.stan.store/pricing: 404. Stan's price is U.
- https://openai.com/chatgpt/pricing/: HTTP 403. Used help.openai.com (V) instead.
- https://help.shopify.com/en/manual/promoting-marketing/create-marketing/shopify-email/pricing: HTTP 403. Used shopify.com/email-marketing (V) instead.
- https://help.etsy.com/hc/en-us/articles/4403023219351: 404 (wrong ID). Used articles 4403058372503 and 29654393638679 and etsy.com/starseller (V).
- https://www.squarespace.com/scheduling/pricing: "Moved" page. Used acuityscheduling.com/pricing (V).
- https://www.ebay.com/help/selling/leaving-feedback-buyers/leaving-feedback-buyers?id=4078: eBay captcha ("Security Measure"). The automatic-feedback article (id=4101) and the User Agreement (id=4259) loaded.
- https://www.ebay.com/help/selling/listings/creating-managing-listings/time-away?id=4785: redirected to "Monitoring and improving your seller performance" (wrong ID).
- https://apps.apple.com/us/app/etsy-seller-manage-your-shop/id1570538540 and https://play.google.com/store/apps/details?id=com.etsy.android.soe: 404.
- https://manychat.com/pricing: HTTP 403. Dropped.
- https://voice.google.com/about: redirected to the Workspace Voice product page; personal plan price not shown.
- Toggle ambiguity: Tidio, Acuity, Zapier, Typeform and Calendly rendered one billing toggle; where the page did not label it, the note says so. Quo rendered only annual prices.
- Not verified today: Tidio, IFTTT and Quo mobile apps; Shopify Sidekick plan gating; Etsy quick-reply count limits; Google Forms being free.

## 5. Sources

https://apps.shopify.com/inbox
https://help.shopify.com/en/manual/shopify-flow
https://www.shopify.com/sidekick
https://help.shopify.com/en/manual/ai-powered-tools/sidekick
https://help.shopify.com/en/manual/inbox
https://www.shopify.com/email-marketing
https://help.shopify.com/en/manual/fulfillment/setup/delivery-methods
https://help.shopify.com/en/manual/fulfillment/setup/delivery-methods/pickup-in-store
https://www.shopify.com/pricing
https://www.tidio.com/pricing/
https://www.gorgias.com/pricing
https://www.helpscout.com/pricing/
https://crisp.chat/en/pricing/
https://www.tawk.to/why-free/ (redirect from https://www.tawk.to/pricing/)
https://zapier.com/pricing
https://zapier.com/apps/etsy/integrations
https://zapier.com/apps/shopify/integrations
https://www.make.com/en/pricing (HTTP 403)
https://www.make.com/en/plans (HTTP 403)
https://help.make.com/subscription-plans (404)
https://help.make.com/pricing (404)
https://help.make.com/make-pricing (404)
https://n8n.io/pricing/
https://docs.n8n.io/n8n-community-license (redirect from https://docs.n8n.io/sustainable-use-license/)
https://docs.n8n.io/deploy/host-n8n/community-edition-features
https://ifttt.com/plans
https://workspace.google.com/products/voice/ (redirect from https://voice.google.com/about)
https://support.google.com/voice/answer/115061
https://support.google.com/voice/answer/9230450
https://www.quo.com/pricing (redirect from https://www.openphone.com/pricing)
https://calendly.com/pricing
https://cal.com/pricing
https://www.squarespace.com/scheduling/pricing (Moved page)
https://acuityscheduling.com/pricing
https://squareup.com/us/en/appointments/pricing
https://www.setmore.com/pricing
https://apps.shopify.com/sesami
https://apps.shopify.com/bookthatapp
https://apps.shopify.com/appointo-appointments-and-bookings
https://linktr.ee/s/pricing
https://beacons.ai/i/pricing
https://stan.store/pricing (404)
https://www.stan.store/pricing (404)
https://stan.store/
https://help.stan.store/
https://espanso.org/
https://textexpander.com/pricing
https://learn.microsoft.com/en-us/windows/powertoys/
https://claude.com/pricing
https://openai.com/chatgpt/pricing/ (HTTP 403)
https://help.openai.com/en/articles/6950777-what-is-chatgpt-plus
https://judge.me/pricing
https://workspace.google.com/products/forms/
https://www.typeform.com/pricing
https://pushover.net/pricing
https://ntfy.sh/
https://help.etsy.com/hc/en-us/articles/115015654988-How-to-Send-Messages-to-Buyers
https://help.etsy.com/hc/en-us/articles/4403058372503-What-is-the-Star-Seller-Badge
https://help.etsy.com/hc/en-us/articles/29654393638679-How-Do-Star-Seller-Metrics-Compare-to-Customer-Service-Standards
https://www.etsy.com/starseller
https://help.etsy.com/hc/en-us/articles/4403023219351 (404)
https://help.etsy.com/hc/en-us/search?query=Etsy+Seller+app+notifications (no matching article)
https://apps.apple.com/us/app/etsy-seller-manage-your-shop/id1570538540 (404)
https://play.google.com/store/apps/details?id=com.etsy.android.soe (404)
https://www.ebay.com/help/selling/feedback-policies/automatic-feedback?id=4101
https://www.ebay.com/help/selling/leaving-feedback-buyers/leaving-feedback-buyers?id=4078 (captcha)
https://www.ebay.com/help/policies/member-behaviour-policies/user-agreement?id=4259
https://www.ebay.com/help/selling/listings/creating-managing-listings/time-away?id=4785 (redirected to seller performance article)
https://developers.facebook.com/docs/marketplace/
https://manychat.com/pricing (HTTP 403)
