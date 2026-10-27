[Skip to content](https://docs.stripe.com/connect/risk-management#main-content)
Risk management with Connect
[Create account](https://dashboard.stripe.com/register/connect) or [Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Frisk-management)
[The Stripe Docs logo](https://docs.stripe.com/)
Search`/`Ask AI
[Create account](https://dashboard.stripe.com/register/connect)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Frisk-management)
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
Risk management with Connect
[Settlement reserves](https://docs.stripe.com/connect/risk-management/settlement-reserves)
[Managed Risk](https://docs.stripe.com/connect/risk-management/managed-risk)
[Create connected accounts with Managed Risk](https://docs.stripe.com/connect/risk-management/connected-accounts-with-managed-risk)
[API-based Managed Risk](https://docs.stripe.com/connect/risk-management/api-managed-risk)
[Best practices](https://docs.stripe.com/connect/risk-management/best-practices)
[Pause payments and payouts on accounts](https://docs.stripe.com/connect/pausing-payments-or-payouts-on-connected-accounts)
[Identify and configure the merchant of record](https://docs.stripe.com/connect/merchant-of-record)
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


#  Risk and liability management with Connect
## Learn how to manage risk and liability for your SaaS platform or marketplace.
Ask about this page
Copy for LLMView as Markdown
Set up agent
When planning your Connect integration, you need to decide how to handle risk and loss liability. This entails understanding the sources of risk for your business and taking steps to prevent and mitigate losses. As a Connect platform, you also need to determine how to handle the risk of unrecoverable losses associated with your connected accounts when you configure your integration. Depending on your business model and the payment types you use, your platform can take responsibility for losses incurred by your connected accounts, or you can assign that responsibility to Stripe.
## Connect platform risk options 
Negative transactions such as refunds and chargebacks can cause a connected account’s Stripe balance to become negative. Negative transactions apply to platform or connected account balances, based on whether the associated payment was a [direct charge](https://docs.stripe.com/connect/direct-charges) or [indirect charge](https://docs.stripe.com/connect/charges#types):
  * Direct charges occur on a connected account, so negative transactions for direct charges affect the connected account’s balance. SaaS platforms typically use direct charges.
  * Indirect charges occur on the platform, so negative transactions for indirect charges affect the platform’s balance. Marketplaces typically use indirect charges.


Your platform is always responsible for its own negative balances. However, responsibility for your connected accounts’ negative balances can belong to your platform or to Stripe, depending on your integration.
Regardless of ultimate responsibility, if a connected account’s balance becomes negative, Stripe first attempts to offset the negative amount by collecting funds from the account’s external account.
If your platform is responsible for negative connected account balances, Stripe also [holds funds in your platform account in reserve](https://docs.stripe.com/connect/account-balances#understanding-connected-reserve-balances), pending the collection of the funds from the connected account. In this case, if a connected account’s balance remains negative for 180 days, we transfer funds from the platform reserve to cover the negative amount.
#### Marketplace liability
Connected account balance liability applies only to connected account balances. It doesn’t affect negative platform balances caused by transactions related to indirect charges. If you use indirect charges, assign negative balance responsibility to your platform, not to Stripe. Assigning responsibility to Stripe doesn’t absolve your platform of responsibility for its own balance.
### Negative balance responsibility
Responsibility for negative balances affects many other configuration options and behaviors. Consider them carefully when designing your integration.
#### Preview API version required with the Express Dashboard
Combining Express Dashboard access with Stripe responsibility for negative balances is in [public preview](https://docs.stripe.com/release-phases). Use the current preview version string (`2026-09-30.preview`) in your Stripe SDK configuration when you create connected accounts.  
|   | Stripe is responsible  | Platform is responsible  |  
| --- | --- | --- |  
| Losses  | Stripe covers losses due to your connected accounts’ negative balances.  | Your platform can incur losses due to your connected accounts’ negative balances.  |  
| Payment fees  | Stripe can collect payment fees directly from connected accounts or from your platform.  | Stripe collects payment fees from your platform.  |  
| Operational responsibilities  | Stripe risk teams manage all payments-related connected account risk. Your platform can take advantage of [Managed Risk](https://docs.stripe.com/connect/risk-management/managed-risk), which automatically monitors risk signals and applies risk interventions.  | The platform manages all payments-related connected account risk. You can’t use Managed Risk.  |  
| Reserve funds  | Stripe doesn’t hold reserves on your platform account to cover negative connected account balances.  | Stripe might [hold reserves on your platform account](https://docs.stripe.com/connect/account-balances#understanding-connected-reserve-balances) to cover negative connected account balances. Your platform can [hold reserves on connected account balances](https://docs.stripe.com/connect/connected-account-reserves).  |  
| Connected account access  | Your connected accounts can use the full Stripe Dashboard or the Express Dashboard. Stripe directly contacts your connected accounts to prevent, mitigate, and resolve payments risk-related issues, and in some cases can take action against them.  | Your connected accounts can use the Stripe Express Dashboard, but not the full Stripe Dashboard. Your platform has a greater degree of control over the payments risk-related experience of your connected accounts.  |  
| Payment and payout pauses  | You can’t pause payments or payouts for your connected accounts.  | You can [pause payments or payouts](https://docs.stripe.com/connect/pausing-payments-or-payouts-on-connected-accounts) for your connected accounts.  |  
| Connected account debits  | You can’t directly debit connected account balances.  | In certain regions, you can [debit funds from your connected accounts](https://docs.stripe.com/connect/account-debits).  |  
| Know Your Customer (KYC) requirements  | Stripe is responsible for collecting KYC information from your connected accounts.  | Your platform is responsible for collecting KYC information from your connected accounts unless they use the Stripe Express Dashboard.  |  
| Stripe fees  | If you pay the listed prices for other Stripe fees, we don’t charge additional fees for negative balance liability.  | Stripe charges no additional fees.  |  
| Embedded finance  | Your platform can’t use [Stripe Treasury](https://docs.stripe.com/treasury/connect) or [Issuing](https://docs.stripe.com/issuing).  | Your platform can offer [Treasury](https://docs.stripe.com/treasury/connect) and [Issuing](https://docs.stripe.com/issuing) features to your connected accounts.  |  
### Identify negative balance responsibility
You can identify whether Stripe or your platform is responsible for a connected account’s negative balances by examining its properties. The specific property you need to check depends on the version of the Accounts API:
  * **Accounts v2:** [defaults.responsibilities.losses_collector](https://docs.stripe.com/api/v2/core/accounts/retrieve#v2_retrieve_accounts-response-defaults-responsibilities-losses_collector) (To retrieve the `defaults` hash, you must specify `defaults` in the `include` parameter.)
  * **Accounts v1:** [controller.losses.payments](https://docs.stripe.com/api/accounts/object#account_object-controller-losses-payments)


In both versions, if Stripe is responsible, the value is `stripe`, and if your platform is responsible, the value is `application`.
## Components of payments risk
Any approach to risk management involves many potential sources of payments risk, in two general types:
  * **Transaction risk** : The risk that a customer might charge back a transaction, such as [disputes](https://docs.stripe.com/disputes) or fraud identified from card testing. With [direct charges](https://docs.stripe.com/connect/direct-charges), transaction risk primarily affects connected accounts; with [destination charges](https://docs.stripe.com/connect/destination-charges) and [separate charges and transfers](https://docs.stripe.com/connect/separate-charges-and-transfers), transaction risk primarily affects platforms.
  * **Account risk** : The risk that a connected account is unable or unwilling to cover the costs of chargebacks on its transactions, leading to unrecoverable negative balances. Account risk primarily affects platforms.


The main types of account risk are _credit risk_ and _fraud risk_. Both can result in chargebacks and unrecoverable negative balances.  
| Type  | Description  | Examples  |  
| --- | --- | --- |  
| Credit risk  | The risk that connected accounts are unable to fulfill their obligations to their customers, such as failing to deliver orders due to unforeseen supply issues. If a connected account accumulates more refunds and chargebacks than it can financially cover, it can result in default.  | During the COVID pandemic, some hotels and short-term accommodation providers represented by connected accounts went out of business. As a result, customers who had pre-paid for future stays submitted chargebacks, which were covered by the platforms that processed those payments.  |  
| Fraud risk  | The risk that dishonest owners or employees of connected accounts intentionally don’t fulfill their obligations to their customers, such as taking orders for unavailable goods and services.  | 
  * **No intent to deliver** : A fraudulent online storefront charged customers for goods that they didn’t intend to deliver. The connected account then paid out the money to their external bank account. When the customers realized that their orders were never going to arrive, they submitted chargebacks, which were covered by the platform.
  * **Payment method cashing** : A fraudster stole a customer’s credit card number, opened a connected account, and made purchases through that account using the stolen payment method credentials. When the customer discovered the fraudulent charges, they submitted chargebacks, which were covered by the platform.

 |  
## Stripe solutions for risk management
Stripe provides several tools to help your platform manage transaction and account risk. The main tool is [Radar](https://docs.stripe.com/radar/account-fraud-prevention), which helps detect and prevent fraud by scanning every payment. It also offers tools to prevent, detect, and mitigate risks posed by your connected accounts.
Platforms that aren’t responsible for connected account negative balances can also take advantage of [Managed Risk](https://docs.stripe.com/connect/risk-management/managed-risk), a full-service solution that protects your platform by managing risk and covering any negative balances on your connected accounts.
## Know Your Customer (KYC) and compliance
In addition to operational risk management solutions, Stripe provides KYC and risk-based screening to help onboard connected accounts and maintain compliance with evolving regulations. Stripe screens include the following:
  * Identity verifications
  * Risk-based KYC and AML checks for individuals and businesses
  * Sanctions screening
  * MATCH (Member Alert To Control High-risk businesses) list checks
  * Secure credit card data tokenization for PCI compliance
  * Money transmitter licenses (MTL) in the US and e-money (EMI) licenses in the EU
  * [Prohibited business checks](https://stripe.com/legal/restricted-businesses)


Was this page helpful?
YesNo
  * Need help? [Contact Support](https://support.stripe.com/).
  * Chat with Stripe developers on [Discord](https://stripe.com/go/developer-chat).
  * Check out our [changelog](https://docs.stripe.com/changelog).
  * Questions? [Contact Sales](https://stripe.com/contact/sales).
  * LLM? [Read llms.txt](https://docs.stripe.com/llms.txt).
  * Powered by [Markdoc](https://markdoc.dev)


On this page
[Connect platform risk options](https://docs.stripe.com/connect/risk-management#risk-options "Connect platform risk options")
[Negative balance responsibility](https://docs.stripe.com/connect/risk-management#negative-balance-responsibility "Negative balance responsibility")
[Identify negative balance responsibility](https://docs.stripe.com/connect/risk-management#identify-negative-balance-responsibility "Identify negative balance responsibility")
[Components of payments risk](https://docs.stripe.com/connect/risk-management#components-of-payments-risk "Components of payments risk")
[Stripe solutions for risk management](https://docs.stripe.com/connect/risk-management#stripe-solutions-for-risk-management "Stripe solutions for risk management")
[Know Your Customer (KYC) and compliance](https://docs.stripe.com/connect/risk-management#know-your-customer-kyc-and-compliance "Know Your Customer \(KYC\) and compliance")

