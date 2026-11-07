# Verification of lane 11: customer service automation (messaging, bookings, small automations)

Date 2026-11-07. Author: research subagent (adversarial price and claim checker).
Question: Do the prices, free tiers, platform claims and availability claims recorded by the lane 11 agent match the vendors' own pages today?
Legend: V = vendor page read today (2026-11-07) with the session fetch script; U = unverified (snippet, memory, or the page would not load).
Method: every PICK plus the highest-fit TOOLS were re-opened on the vendor's own pricing, plans or help page. Verdict "confirmed" means the exact figure or claim is on the page read; "refuted" means the page says something different; "unreadable" means the page would not load after one alternative. Quotes are verbatim and under 25 words. 25 pages were fetched; WebSearch was unavailable (the shared per-turn budget was already spent), so one sub-claim stays U.

## 0. Bottom line

- The lane 11 agent's work holds up. 18 of 19 checks are confirmed on the vendor's page today. No tool was found shut down, acquired or renamed since the lane report.
- One minor refutation: n8n Cloud Starter was recorded as "20€ /mo, billed annually"; the pricing page today shows "$20 /mo, billed annually" for the same 2.5k executions. The figure is right, the currency symbol is not. The self-hosted Community edition claim (the actual PICK) is confirmed: "You can stick with the free Community edition indefinitely".
- One sub-claim could not be verified: Zapier Free's "15-minute polling". It is not on zapier.com/pricing today, and the help URL redirected to a "Zap limits" page that does not state an update interval. Everything else about Zapier is confirmed, including "Etsy has not yet built an integration on Zapier" and Shopify being a Premium app.
- Three omissions worth adding to the lane report: Appointo Free carries Appointo branding (removing it is a Pro feature) and Pro adds "Usage charge for text/whatsapp and 2% charge for subscriptions/bundles"; Beacons' 9% seller fee also applies on the $8.33/mo Creator plan (0% fees start at Creator Plus, $25/mo annual or $30 monthly); Judge.me now advertises "Judge.me Email is here! Get 15,000 emails/mo free".
- Etsy's help pages loaded today and confirm the key facts: auto-replies run "from an hour to a maximum of five days" or on a weekly schedule needing "at least 8 hours" on "at least 4 days a week"; both types "count as a reply towards your Star Seller messaging score"; "Auto-replies can only be managed on Etsy.com and not the Etsy Seller app".

## 1. Checks

| Tool | Claim checked | Verdict | Evidence quote | URL | Correction |
|---|---|---|---|---|---|
| Etsy Messages auto-replies and quick replies | Free, built in; temporary auto-reply up to 5 days; weekly schedule needs at least 8 hours a day on at least 4 days; auto-replies count toward Star Seller; auto-replies only on Etsy.com; US writing assistant | confirmed | "Auto-replies are sent in response to messages you receive over the duration of time you select, from an hour to a maximum of five days." Also: "your available hours must be at least 8 hours long on the days you choose, and you need to select at least 4 days a week." And: "Auto-replies can only be managed on Etsy.com and not the Etsy Seller app." And: "US sellers can also use the writing assistant" | https://help.etsy.com/hc/en-us/articles/115015654988-How-to-Send-Messages-to-Buyers | none; no price is shown because the feature is part of the shop |
| Etsy Star Seller rule | 95% of first messages within 24 hours; eligible 90 days after first sale with 5 orders and $300 over 3 months | confirmed | "Message response rate: reply to 95% of first messages in a thread within 24 hours" and "starting 90 days after your first sale ... at least 5 orders and $300 in sales over the past 3 months" | https://help.etsy.com/hc/en-us/articles/4403058372503-What-is-the-Star-Seller-Badge | none |
| Cal.com Free | Free forever for 1 user, unlimited links and calendars, Stripe and PayPal payments, no usage limits; Teams $12 per user/month yearly | confirmed | "Start scheduling for free, with no usage limits." Plan list: "1 user", "Unlimited links & calendars", "Accept Stripe & PayPal payments", "Mobile App", "Browser Extension". Teams: "YEARLY $12per user/month" | https://cal.com/pricing | none |
| Espanso | Free, GPL-3, Windows, macOS, Linux | confirmed | "Espanso is open-source, licensed under the GPL-3 license." and "Espanso supports Windows, Linux and macOS." | https://espanso.org/ | none |
| Linktree | Free: unlimited basic links; Starter $7/mo billed annually or $9 monthly; Pro $14 or $17; Premium $30 or $35; Instagram auto-replies on Premium | confirmed | "Free Unlimited basic links Email and phone sign-ups"; Starter "$7 /mo Billed annually, or $9 monthly"; Pro "$14 /mo Billed annually, or $17 monthly"; Premium "$30 /mo Billed annually, or $35 monthly" with "Unlimited Instagram auto-replies" | https://linktr.ee/s/pricing | none |
| Shopify Basic plan | $39 USD/mo monthly or $29 USD/mo yearly | confirmed | "Pay monthly $39 USD/mo" and "Pay yearly $29 USD/mo" (Basic column) | https://www.shopify.com/pricing | none |
| Shopify Inbox | Free; quick replies, business hours, optional AI agent; desktop, iOS and Android apps | confirmed | App Store: "Pricing Free"; features list "Quick replies", "Business hours". Help: "the Shopify Inbox app for desktop, the Shopify Inbox app for iOS, or the Shopify Inbox app for Android" | https://apps.shopify.com/inbox and https://help.shopify.com/en/manual/inbox | none; one merchant review notes no API and no reply by email |
| Shopify Flow | Free on Basic, Grow, Advanced, Plus | confirmed | "Shopify Flow is a free app available on the Basic, Grow, Advanced, and Plus plans." | https://help.shopify.com/en/manual/shopify-flow | none; Send HTTP Request action needs Grow or above |
| Shopify Email | 10,000 emails a month free, then $1 USD per 1,000 | confirmed | "send up to 10,000 manual or automated emails for free. After that, only pay for what you use at $1 USD per 1,000 additional emails" | https://www.shopify.com/email-marketing | none |
| Judge.me Free | Free $0 per month; Awesome $15 per month is the maximum; unlimited review requests; Etsy import | confirmed | "$15 per month is the most you can ever pay us." Free plan: "Unlimited product & store reviews". FAQ: "Our Forever Free plan includes unlimited review requests". Import & Sync Reviews lists "Etsy" | https://judge.me/pricing | none; new banner "Judge.me Email is here! Get 15,000 emails/mo free" |
| n8n self-hosted Community edition | Free indefinitely; licence allows internal business use | confirmed | "You can stick with the free Community edition indefinitely". Licence: "You may use or modify the software only for your own internal business purposes or for non-commercial or personal use." | https://docs.n8n.io/n8n-community-license and https://docs.n8n.io/hosting/community-edition-features/ | none; the licence is Sustainable Use (fair-code), not open source by OSI definition |
| n8n Cloud Starter | 20€ /mo billed annually, 2.5k executions | refuted | "Starter ... $20 /mo, billed annually 2.5k workflow executions with unlimited steps" | https://n8n.io/pricing/ | Page shows $20, not 20€, today. Executions figure (2.5k) and annual billing match. Enterprise on the same page renders "667€", so currency display is mixed |
| Appointo (Shopify) | Free: unlimited services and bookings, email notification; Pro $14 / month or $151/year; Premium $25; Advanced $39 | confirmed | "Free ... Unlimited Services Unlimited Bookings Email Notification"; "Pro $14 / month or $151/year and save 10%"; "Premium $25 / month"; "Advanced $39 / month" | https://apps.shopify.com/appointo-appointments-and-bookings | none, but two omissions: "No Appointo Branding" is a Pro feature (Free shows branding); Pro has "Usage charge for text/whatsapp and 2% charge for subscriptions/bundles" |
| Setmore Free | Free $0, up to 4 users, unlimited appointments, accept payments, email reminders, iOS and Android apps; Pro $5 user / month annual billing | confirmed | "Up to 4 users $0 user / month ... Unlimited appointments Accept payments ... Email reminders ... iOS and Android apps"; "annual billing - free plan $0 per month, pro plan $5 per month, team $5 per month." | https://www.setmore.com/pricing | none; Pro adds "SMS & email reminders" and "Unlimited users" |
| Pushover | $4.99 USD one-time per platform; 30-day trial; 10,000 messages a month free to send | confirmed | "it's just a $4.99 USD one-time purchase on each platform (iPhone/iPad, Android, and Desktop)"; "try it out free for 30 days"; "Each user can send up to 10,000 messages per month for free." | https://pushover.net/pricing | none |
| ntfy | Free without sign-up, open source, self-hostable; Supporter $6 monthly or $5 annually; Pro $12 or $10 | confirmed | "Try ntfy for free without sign-up, or check out our paid plans. Or, since it's open source, you can always self-host it." Plans: Supporter "$6 / $5", Pro "$12 / $10" | https://ntfy.sh/ | none |
| Beacons | Free forever $0/month with 9% seller fees, 50 email sends, Smart Reply IG auto-DM; Creator $8.33/mo ($100 billed annually) or $10 monthly; Creator Plus $25/mo | confirmed | "Free forever $0 /month ... 9% seller fees 50 email sends per month Smart Reply IG auto-DM"; Creator "$100 billed annually $8.33 /mo $10"; Creator Plus "$300 billed annually $25 /mo $30 ... 0% seller fees" | https://beacons.ai/i/pricing | none, but omission: Creator keeps the 9% fee ("All features in Free, and" custom domain, 500 emails); 0% fees start at Creator Plus ($30 monthly) |
| Zapier | Free $0 /month, 100 tasks per month, two-step Zaps; Professional starting from $19.99 /month; Shopify is Premium; Etsy has no integration; 15-minute polling | confirmed (except polling, U) | "Free forever $0 /month ... (100 tasks per month)" and "Two-step Zaps"; "Professional Starting from $19.99 /month"; Shopify page: "Premium apps: Shopify"; Etsy page: "Etsy has not yet built an integration on Zapier." | https://zapier.com/pricing, https://zapier.com/apps/shopify/integrations, https://zapier.com/apps/etsy/integrations | "15-minute polling" not on the pricing page or the Zap-limits help page read today; whether $19.99 is the yearly or monthly rate is still not stated in the page text (both "Pay monthly" and "Pay yearly (Save 33%)" toggles exist) |
| TextExpander | Free $0 forever: 5 active snippets, 1 snippet swap every 2 weeks; Pro $5 /user/mo billed annually at $60 USD; Business $10 billed annually at $120 | confirmed | "Active Snippets 5 Unlimited Unlimited Unlimited"; "Snippet Swap 1 every 2 weeks"; "$5 /user/mo Price in USD per user per month. Billed annually at $60 USD."; "$10 /user/mo ... Billed annually at $120 USD." | https://textexpander.com/pricing | none; platform header reads "Mac Windows Chrome iPhone and iPad Android" with no "(beta)" marker in the text read |
| Calendly | Free: one event type, one calendar connection, browser extension; payments on paid tier; Standard Plus $18 /seat/mo (with Notetaker add-on) | confirmed | Free "Always free ... One event type One calendar connection ... Browser extension"; "Standard Plus Add Notetaker & Callie $18 /seat/mo ... Payments Connect Stripe, PayPal" | https://calendly.com/pricing | none; the page text today shows only the Notetaker-bundled prices, so the base Standard price is not visible in text |

## 2. What the first agent got wrong or left out

1. n8n Cloud Starter currency: recorded "20€ /mo, billed annually"; the page shows "$20 /mo, billed annually" today. Same 2.5k executions. Minor, and the PICK (self-hosted Community, free) is unaffected.
2. Zapier "15-minute polling" on the Free plan: not on the pricing page or the Zap-limits help page read today. Treat as U until a Zapier page states it.
3. Appointo omissions: the Free plan shows Appointo branding ("No Appointo Branding" is listed under Pro), and Pro carries "Usage charge for text/whatsapp and 2% charge for subscriptions/bundles". The lane report's $14 Pro figure is right.
4. Beacons omission: the 9% seller fee is not only a Free-tier thing. Creator ($8.33/mo annual, $10 monthly) lists "All features in Free, and" a custom domain and 500 emails; "0% seller fees" first appears under Creator Plus ($25/mo annual, $30 monthly).
5. TextExpander "Android (beta)": the pricing page header lists "Android" with no beta marker in the text read. Not a price error.
6. Judge.me new fact: the pricing page now carries "NEW Judge.me Email is here! Get 15,000 emails/mo free". Not in the lane report.
7. Everything else checked (Etsy rules, Cal.com, Espanso, Linktree, Shopify plan/Inbox/Flow/Email, Setmore, Pushover, ntfy, Calendly, Zapier Etsy and Shopify status) matches the vendor page today.

## 3. Gaps and pages that would not load

- No page failed to load. Etsy help pages, which the brief warned might wall the fetcher, returned HTTP 200 today.
- WebSearch was unavailable (shared per-turn budget already spent), so the Zapier update-interval help page could not be located; the guessed help URL redirected to "Zap limits", which does not state an interval.
- Not re-checked today (outside the 12 to 16 target, and lower fit): Tidio, Gorgias, Help Scout, Crisp, tawk.to, Make, IFTTT, Google Voice, Quo, Acuity, Square Appointments, Sesami, BTA, Stan Store, PowerToys, Claude, ChatGPT Plus, Google Forms, Typeform, Facebook Marketplace API, eBay automatic feedback.

## 4. Sources (every URL fetched today)

https://cal.com/pricing
https://espanso.org/
https://linktr.ee/s/pricing
https://judge.me/pricing
https://docs.n8n.io/n8n-community-license
https://n8n.io/pricing/
https://docs.n8n.io/hosting/community-edition-features/ (redirects to https://docs.n8n.io/deploy/host-n8n/community-edition-features)
https://apps.shopify.com/appointo-appointments-and-bookings
https://apps.shopify.com/inbox
https://www.shopify.com/pricing
https://www.shopify.com/email-marketing
https://help.shopify.com/en/manual/shopify-flow
https://help.shopify.com/en/manual/inbox
https://help.etsy.com/hc/en-us/articles/115015654988-How-to-Send-Messages-to-Buyers
https://help.etsy.com/hc/en-us/articles/4403058372503-What-is-the-Star-Seller-Badge
https://www.setmore.com/pricing
https://pushover.net/pricing
https://ntfy.sh/
https://beacons.ai/i/pricing
https://zapier.com/pricing
https://zapier.com/apps/etsy/integrations
https://zapier.com/apps/shopify/integrations
https://help.zapier.com/hc/en-us/articles/8496181445261-What-is-the-update-time-for-a-Zap (redirects to https://help.zapier.com/hc/en-us/articles/8496181445261-Zap-limits)
https://textexpander.com/pricing
https://calendly.com/pricing
