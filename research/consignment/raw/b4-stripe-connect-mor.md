[Skip to content](https://docs.stripe.com/connect/merchant-of-record#main-content)
Identify and configure the merchant of record
[Create account](https://dashboard.stripe.com/register/connect) or [Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fmerchant-of-record)
[The Stripe Docs logo](https://docs.stripe.com/)
Search`/`Ask AI
[Create account](https://dashboard.stripe.com/register/connect)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fmerchant-of-record)
  * [Get started ](https://docs.stripe.com/get-started)
  * [Payments ](https://docs.stripe.com/payments)
  * [Revenue ](https://docs.stripe.com/revenue)
  * [Risk ](https://docs.stripe.com/risk)
  * [Data ](https://docs.stripe.com/data)
  * [Money management ](https://docs.stripe.com/money-management)
  * [Stablecoins ](https://docs.stripe.com/stablecoins)
  * [Embedded finance ](https://docs.stripe.com/connect)
  * [Developer resources ](https://docs.stripe.com/development)

More
APIs & SDKsHelp
[Overview](https://docs.stripe.com/connect)
Stripe Connect
[How Connect works](https://docs.stripe.com/connect/how-connect-works)
Get started with Connect
[Connect and the Accounts v2 API](https://docs.stripe.com/connect/accounts-v2)
[SaaS platforms and marketplaces](https://docs.stripe.com/connect/saas-platforms-and-marketplaces)
[Risk management with Connect](https://docs.stripe.com/connect/risk-management)
Identify and configure the merchant of record
[Migrate to account controller properties](https://docs.stripe.com/connect/migrate-to-controller-properties)
[Compare SaaS platform configurations for Accounts v1 and Accounts v2](https://docs.stripe.com/connect/accounts-v2/saas-platform-payments-billing)
[Accounts v1 support for new Connect integrations](https://docs.stripe.com/connect/accounts-v2/account-creation)
[Upcoming requirements updates](https://docs.stripe.com/connect/upcoming-requirements-updates)


Design your integration
Integration fundamentals
Capabilities and information requirements
Configure account Dashboards
Onboard connected accounts
Manage your Connect platform
Payment processing
Accept payments
Pay out to accounts
Embedded financial products
[Treasury for platforms](https://docs.stripe.com/treasury/connect)
[Issuing](https://docs.stripe.com/issuing)
Capital for platforms
[Managed support](https://docs.stripe.com/managed-support)
United StatesEnglish (United States)
  1. [Home](https://docs.stripe.com/)/
  2. [Embedded finance](https://docs.stripe.com/connect)/
  3. Get started with Connect


#  Determine and configure the merchant of record (MoR)
## Determine the appropriate merchant of record for your business and configure your Connect integration to reflect it.
Ask about this page
Copy for LLMView as Markdown
Set up agent
Before configuring a Connect payment flow, determine which entity is the merchant of record (MoR) for your transactions. The MoR is the entity that the customer understands they’re buying from. It’s also the business that’s responsible for the transaction and for providing customer recourse in scenarios such as refunds and disputes. Determine the MoR based on the business model and the relationship between the customer, connected account, and platform. Don’t base it on the charge type or payment configuration.
#### Customer definition
In this document, “customer” always refers to the end customer who makes a purchase and ultimately receives the goods or services. This is important for configurations where ownership technically passes between the platform and connected accounts. “Customer” in the context of transactions between an external customer and a Connect integration never refers to the connected account or the platform.
## Why the merchant of record matters
You need to identify the correct MoR because card network compliance rules require a brand’s identity to be clear and consistent throughout the transaction. Your website, checkout, terms, receipts, statement descriptor, and Connect configuration all need to reflect the same entity. Misalignment can confuse customers, increase unrecognized transactions and disputes, require your platform to take remediation actions, and possibly lead to card-network scrutiny or enforcement, including fines.
For example, a customer might buy an item from a branded storefront. If a different business appears on their card statement, receipt, or dispute correspondence, the customer might not recognize the transaction or know who’s responsible for resolving a problem. That inconsistency can lead to disputes and card-network compliance concerns.
## Identify the merchant of record
Determine the MoR by looking at the transaction from the customer’s perspective. Identify the entity that the customer understands they’re buying from and would expect to be responsible for the transaction, including providing support for issues such as refunds and disputes.
Assess the complete customer-facing commercial arrangement using the criteria below. Don’t determine the MoR solely from your platform label, charge type, or preferred payment configuration.
### Assess the transaction from the customer’s perspective
Use the following framework for each transaction.  
| Criterion  | What to review  |  
| --- | --- |  
| The entity that the customer thinks they’re purchasing from  | Check the branding of the storefront, checkout page, invoice, receipt, and customer terms. Identify whether the brand is the platform, the connected account, or some other entity.  |  
| The entity that’s liable to the customer for chargebacks  | Identify who provides refunds, responds to disputes and chargebacks, and bears the financial and operational responsibility for customer recourse. (This entity can differ from the entity whose balance Stripe directly debits for chargebacks.)  |  
| The entity whose name appears on the transaction statement descriptor  | Review the final statement descriptor, including any prefix or dynamic suffix, to confirm that it clearly identifies the same brand that the customer sees throughout their transaction.  |  
| The owner or titleholder of the product or service being sold  |  Determine who holds legal title to (or has a reseller license for) the product, or who is offering the service. Keep in mind that the customer’s perspective is more important than the technical details. For example, if the product title technically transfers briefly to the platform as part of the transaction, that isn’t enough to qualify the platform as the MoR. The platform can only be the MoR if the customer believes they’re purchasing from the platform.  |  
If one entity consistently satisfies these criteria, it’s typically the MoR. If you remain unsure which entity is the MoR, we recommend consulting your legal or other professional advisers before implementing or changing your payment flow.
### Common Connect scenarios  
| Scenario  | Typical MoR  | Key considerations  | Example business  |  
| --- | --- | --- | --- |  
| SaaS platform where a connected account sells directly to customers  | Connected account  | The connected account operates the storefront, is named at checkout, issues receipts, handles disputes, and is responsible for customer support.  | The platform is a SaaS provider that offers payment processing and scheduling services to independent pet groomers, who are paid directly by their customers.  |  
| Marketplace selling in its own name  | Marketplace (platform)  | All customer-facing transaction details and the Connect configuration need to reflect the marketplace as the MoR.  | The platform is a rideshare app where customers book rides and pay the platform directly, then the platform pays out funds to individual drivers.  |  
| Marketplace that facilitates sales by distinct sellers  | Marketplace (platform)  | These Marketplaces usually want to be responsible for disputes, and are the primary brand that customers interact with.  | The platform is an online craft marketplace where customers can purchase goods from a variety of independent sellers through the platform’s branded storefront.  |  
Labels such as “SaaS platform” or “marketplace” don’t determine the MoR. The customer-facing commercial arrangement does.
## Configure Connect to reflect the correct merchant of record
First, determine the appropriate MoR using the above guidance. Then, configure a payment flow that reflects that MoR for each transaction. The following must match the MoR:
  * The entity reflected in the Connect payment flow
  * The charge type
  * The statement descriptor
  * The invoice
  * The receipt
  * The transaction presentation
  * The `merchant` account configuration (when using the Accounts v2 API)


Your payment configuration must reflect the appropriate MoR as defined by the customer-facing transaction; the technical payment flow doesn’t determine the MoR. A Connect payment flow can be valid in a technical sense for more than one business model.
### Select a charge type
Select a [charge type](https://docs.stripe.com/connect/charges) for your connected accounts only after determining the appropriate MoR. The following table shows the valid charge types for each MoR:  
| Merchant of record (MoR)  | Allowed charge types  | Parameter requirements  |  
| --- | --- | --- |  
| Platform   | Destination charges  | Without `on_behalf_of`  |  
| Separate Charges and Transfers  | Without `on_behalf_of`  |  
| Connected account   | Direct charges  | N/A  |  
| Destination charges  | With `on_behalf_of`  |  
| Separate charges and transfers  | With `on_behalf_of`  |  
### Configure statement descriptors
The statement descriptor needs to clearly identify the appropriate MoR. It can’t create ambiguity or contradict the brand shown at checkout, on the receipt, or in the customer terms.
  * For non-card payments, you can provide the full statement descriptor when you create the payment. If you don’t provide one, Stripe uses the MoR’s configured default statement descriptor.
  * For card payments, use a static descriptor or provide a dynamic statement-descriptor suffix. Stripe combines a dynamic suffix with the MoR’s descriptor prefix using an asterisk and space. You can’t set a full static card statement descriptor at payment creation time.


If you use a dynamic descriptor, it must help the customer recognize the MoR without obscuring or contradicting the brand identity.
For descriptor formats and requirements, see [statement descriptors](https://docs.stripe.com/connect/statement-descriptors).
### Use the Accounts v2 API
For connected accounts created with Accounts v2, a connected account that acts as the MoR must have [the merchant configuration](https://docs.stripe.com/connect/account-capabilities?accounts-namespace=v2#merchant). Otherwise, payments can fail.
### Customer-facing transaction details
If the platform is the MoR, consistently represent the platform as the MoR to the customer, and take responsibility for the transaction and any followup actions (such as disputes).
If the connected account is the MoR, clearly represent the connected account as the MoR, and configure your payment flow to reflect that. Don’t present one party as MoR at checkout and another on the statement, receipt, customer terms, or dispute process.
## Card network compliance and consequences
Card networks can scrutinize both a platform’s overall design and individual transactions. A single transaction that misrepresents the MoR can create compliance exposure. Inconsistent brand identity can also increase customer confusion and disputes. Non-compliance can lead to remediation work, operational disruption, network scrutiny, fines, and other enforcement consequences.
Make sure to establish a consistent transaction model before designing and building or changing your integration. If you aren’t certain of the appropriate MoR, don’t simply choose a payment flow and assume that it’s valid.
## Validate your implementation
Before you launch or change your integration, make sure the same brand is consistently shown for each transaction across all customer-facing interfaces, communications, and records. That includes your website and checkout, statement descriptors, receipts, invoices, terms, customer support and refund processes, and Connect configuration (including charge flow and `on_behalf_of`).
## Get help with unclear or unusual models
The central rule is straightforward: The entity that your Connect setup reflects as the MoR needs to be the entity that you:
  * Show to the customer as the brand
  * Name throughout the relevant transaction experience
  * Present as responsible for the transaction


If, after following this guide, you still aren’t certain of the appropriate MoR, consult your legal or other professional advisers. If you require further assistance, contact your Stripe account team or [Stripe support](https://support.stripe.com/contact).
Was this page helpful?
YesNo
  * Need help? [Contact Support](https://support.stripe.com/).
  * Chat with Stripe developers on [Discord](https://stripe.com/go/developer-chat).
  * Check out our [changelog](https://docs.stripe.com/changelog).
  * Questions? [Contact Sales](https://stripe.com/contact/sales).
  * LLM? [Read llms.txt](https://docs.stripe.com/llms.txt).
  * Powered by [Markdoc](https://markdoc.dev)


On this page
[Why the merchant of record matters](https://docs.stripe.com/connect/merchant-of-record#why-the-merchant-of-record-matters "Why the merchant of record matters")
[Identify the merchant of record](https://docs.stripe.com/connect/merchant-of-record#identify-the-merchant-of-record "Identify the merchant of record")
[Assess the transaction from the customer’s perspective](https://docs.stripe.com/connect/merchant-of-record#assess-the-transaction-from-the-customers-perspective "Assess the transaction from the customer’s perspective")
[Common Connect scenarios](https://docs.stripe.com/connect/merchant-of-record#common-connect-scenarios "Common Connect scenarios")
[Configure Connect to reflect the correct merchant of record](https://docs.stripe.com/connect/merchant-of-record#configure-connect-to-reflect-the-correct-merchant-of-record "Configure Connect to reflect the correct merchant of record")
[Select a charge type](https://docs.stripe.com/connect/merchant-of-record#select-a-charge-type "Select a charge type")
[Configure statement descriptors](https://docs.stripe.com/connect/merchant-of-record#configure-statement-descriptors "Configure statement descriptors")
[Use the Accounts v2 API](https://docs.stripe.com/connect/merchant-of-record#use-the-accounts-v2-api "Use the Accounts v2 API")
[Customer-facing transaction details](https://docs.stripe.com/connect/merchant-of-record#customer-facing-transaction-details "Customer-facing transaction details")
[Card network compliance and consequences](https://docs.stripe.com/connect/merchant-of-record#card-network-compliance-and-consequences "Card network compliance and consequences")
[Validate your implementation](https://docs.stripe.com/connect/merchant-of-record#validate-your-implementation "Validate your implementation")
[Get help with unclear or unusual models](https://docs.stripe.com/connect/merchant-of-record#get-help-with-unclear-or-unusual-models "Get help with unclear or unusual models")

