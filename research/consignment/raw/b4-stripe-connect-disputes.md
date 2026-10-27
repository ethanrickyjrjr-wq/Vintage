[Skip to content](https://docs.stripe.com/connect/disputes#main-content)
Disputes on Connect
[Create account](https://dashboard.stripe.com/register) or [Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fdisputes)
[The Stripe Docs logo](https://docs.stripe.com/)
Search`/`Ask AI
[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fdisputes)
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
Design your integration
Integration fundamentals
Capabilities and information requirements
Configure account Dashboards
Onboard connected accounts
Manage your Connect platform
Payment processing
Accept payments
[Charges in a Connect integration](https://docs.stripe.com/connect/charges)
[Set statement descriptors](https://docs.stripe.com/connect/statement-descriptors)
[Set MCCs](https://docs.stripe.com/connect/setting-mcc)
[Handle multiple currencies](https://docs.stripe.com/connect/currencies)
[Create payment links with Connect](https://docs.stripe.com/connect/payment-links)
[Use Radar with Connect](https://docs.stripe.com/connect/radar)
Disputes on Connect
[Create subscriptions](https://docs.stripe.com/connect/subscriptions)
[Create invoices](https://docs.stripe.com/connect/invoices)
[Manage payment methods](https://docs.stripe.com/connect/manage-payment-methods)
[Account balance](https://docs.stripe.com/connect/account-balances)


Pay out to accounts
Embedded financial products
[Treasury for platforms](https://docs.stripe.com/treasury/connect)
[Issuing](https://docs.stripe.com/issuing)
Capital for platforms
[Managed support](https://docs.stripe.com/managed-support)
United StatesEnglish (United States)
  1. [Home](https://docs.stripe.com/)/
  2. [Embedded finance](https://docs.stripe.com/connect)/
  3. Accept payments


#  Disputes on Connect platforms
## Learn about the dispute responsibilities on Connect platforms.
Ask about this page
Copy for LLMView as Markdown
Set up agent
You can view all disputes filed against your platform and connected accounts in your Dashboard. When one of your connected accounts receives a dispute against a payment, the [charge type](https://docs.stripe.com/connect/charges#types) and negative balance responsibility determine:
  * Whether you or your connected account responds to that dispute to accept or challenge it.
  * Which account Stripe debits for the chargeback and fees.


This guide describes how Stripe processes disputes for each charge type and how you can handle them.  
| Behavior  | Direct charges  | Indirect charges  |  
| --- | --- | --- |  
| Account to use when responding through the API  | Connected account. Use its ID in the [`Stripe-Account` header](https://docs.stripe.com/connect/authentication#stripe-account-header).  | Platform account.  |  
| Balance debited for the disputed amount  | Connected account’s balance.  | Platform’s balance, with or without `on_behalf_of`.  |  
| Account debited for dispute-related fees  | Depends on the connected account’s [fee configuration](https://docs.stripe.com/connect/direct-charges-fee-payer-behavior).  | Platform account.  |  
## Direct charges
For connected accounts that use [direct charges](https://docs.stripe.com/connect/direct-charges), Stripe always attempts to debit disputed amounts from the connected account’s balance. However, if Stripe can’t debit the amount, ultimate responsibility depends on whether Stripe or the platform is [responsible for negative balances](https://docs.stripe.com/connect/risk-management#identify-negative-balance-responsibility).
For dispute-related fees, responsibility depends on your connected account options. The following table shows whether Stripe debits dispute-related fees from the platform or the connected account:  
| Account option  | Dispute fee payer  |  
| --- | --- |  
| v2 `Account` with [defaults.responsibilities.fees_collector](https://docs.stripe.com/api/v2/core/accounts/object#v2_account_object-defaults-responsibilities-fees_collector) = `application`  | Platform  |  
| v2 `Account` with [defaults.responsibilities.fees_collector](https://docs.stripe.com/api/v2/core/accounts/object#v2_account_object-defaults-responsibilities-fees_collector) = any of the following values, including legacy Standard, Express, and Custom accounts:
  * `stripe`
  * `application_custom`
  * `application_express`

 | Connected account  |  
| v2 `Account` with [defaults.responsibilities.fees_collector](https://docs.stripe.com/api/v2/core/accounts/object#v2_account_object-defaults-responsibilities-fees_collector) = `application_unified_accounts_beta`  | Connected account (for information about changing the payer to your platform, [contact Stripe Support](https://support.stripe.com/))  |  
| v1 `Account` with [controller.fees.payer](https://docs.stripe.com/api/accounts/create#create_account-controller-fees-payer) = `application`  | Platform  |  
| v1 `Account` with [controller.fees.payer](https://docs.stripe.com/api/accounts/create#create_account-controller-fees-payer) = any of the following values, including legacy Standard, Express, and Custom accounts:
  * `account`
  * `application_custom`
  * `application_express`

 | Connected account  |  
| v1 `Account` with [controller.fees.payer](https://docs.stripe.com/api/accounts/create#create_account-controller-fees-payer) = `application_unified_accounts_beta`  | Connected account (for information about changing the payer to your platform, [contact Stripe Support](https://support.stripe.com/))  |  
## Destination and separate charges and transfers
For [destination charges](https://docs.stripe.com/connect/destination-charges) and [separate charges and transfers](https://docs.stripe.com/connect/separate-charges-and-transfers), with or without `on_behalf_of`, Stripe debits dispute amounts and fees from your platform account.
Set up [a webhook](https://docs.stripe.com/webhooks) to listen for [dispute created events](https://docs.stripe.com/api/events/types#event_types-charge.dispute.created).
You can reverse the transfer to your connected account through the [Dashboard](https://dashboard.stripe.com/test/transfers) or by [creating a transfer reversal](https://docs.stripe.com/api/transfer_reversals/create) to recover the dispute chargeback funds. If the connected account has a negative balance, Stripe attempts to debit its external account if [debit_negative_balances](https://docs.stripe.com/connect/account-balances#automatically-debit-connected-accounts) is set to `true`.
Time your reversal according to how you choose to handle the dispute:
  * If you accept the dispute, you can reverse the transfer immediately.
  * If you challenge the dispute, wait for the dispute outcome before reversing the transfer.
    * If you win, don’t reverse the transfer.
    * If you lose, reverse the transfer.


If you reverse the transfer for a disputed payment that you challenge and win, transfering those funds back to a connected account can have unexpected results:
  * If your platform has an insufficient balance, the transfer fails. Prevent insufficient balance errors by [adding funds to your Stripe balance](https://docs.stripe.com/get-started/account/add-funds).
  * [Cross-border transfer restrictions](https://docs.stripe.com/connect/account-capabilities#transfers-cross-border) might prevent you from repaying your connected account. 


If Stripe is responsible for the connected account’s negative balances, a transfer reversal can fail when the account has insufficient available funds. Handle reversal failures by retrying when sufficient funds become available.
To automate dispute management and handle chargebacks, browse [Fraud Stripe Apps](https://marketplace.stripe.com/categories/fraud) on the App Marketplace.
## Provide Connect embedded components to allow your connected accounts to respond to disputes
Your connected accounts can use [Connect embedded components](https://docs.stripe.com/connect/get-started-connect-embedded-components) to manage disputes from within your site.
The following components support dispute management:
  * [Payments component](https://docs.stripe.com/connect/supported-embedded-components/payments): Displays all of an account’s payments and disputes.
  * [Disputes list component](https://docs.stripe.com/connect/supported-embedded-components/disputes-list): Displays all of an account’s disputes.
  * [Disputes for a payment component](https://docs.stripe.com/connect/supported-embedded-components/disputes-for-a-payment): Displays the disputes for a single specified payment. You can use it to include dispute management functionality on a page with your payments UI.


## Smart Disputes
If you use [Smart Disputes](https://docs.stripe.com/disputes/smart-disputes), you can [enable Smart Disputes auto-responses for your connected accounts](https://docs.stripe.com/disputes/smart-disputes/auto-respond?dashboard-or-api=dashboard#settings-for-connect-platforms).
## See also
  * [Dispute categories](https://docs.stripe.com/disputes/categories)
  * [Use Radar with Connect](https://docs.stripe.com/connect/radar)
  * [Smart Disputes](https://docs.stripe.com/disputes/smart-disputes)
  * [Smart Disputes fee passthrough](https://docs.stripe.com/connect/smart-disputes-fee-passthrough)


Was this page helpful?
YesNo
  * Need help? [Contact Support](https://support.stripe.com/).
  * Chat with Stripe developers on [Discord](https://stripe.com/go/developer-chat).
  * Check out our [changelog](https://docs.stripe.com/changelog).
  * Questions? [Contact Sales](https://stripe.com/contact/sales).
  * LLM? [Read llms.txt](https://docs.stripe.com/llms.txt).
  * Powered by [Markdoc](https://markdoc.dev)


On this page
[Direct charges](https://docs.stripe.com/connect/disputes#direct-charges "Direct charges")
[Destination and separate charges and transfers](https://docs.stripe.com/connect/disputes#destination-and-separate-charges-and-transfers "Destination and separate charges and transfers")
[Provide Connect embedded components to allow your connected accounts to respond to disputes](https://docs.stripe.com/connect/disputes#provide-connect-embedded-components-to-allow-your-connected-accounts-to-respond-to-disputes "Provide Connect embedded components to allow your connected accounts to respond to disputes")
[Smart Disputes](https://docs.stripe.com/connect/disputes#smart-disputes "Smart Disputes")
[See also](https://docs.stripe.com/connect/disputes#see-also "See also")

