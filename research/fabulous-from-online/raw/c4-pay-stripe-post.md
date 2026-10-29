[Skip to content](https://docs.stripe.com/payment-links/post-payment#main-content)
After you receive payment from a payment link
[Create account](https://dashboard.stripe.com/register) or [Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayment-links%2Fpost-payment)
[The Stripe Docs logo](https://docs.stripe.com/)
Search`/`Ask AI
[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayment-links%2Fpost-payment)
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
[Overview](https://docs.stripe.com/payments)[Accept a payment](https://docs.stripe.com/payments/accept-a-payment)
Online payments
[Overview](https://docs.stripe.com/payments/online-payments)[Find your use case](https://docs.stripe.com/payments/use-cases/get-started)
[Use Payment Links](https://docs.stripe.com/payment-links)
[Create a payment link](https://docs.stripe.com/payment-links/create)
[Share a payment link](https://docs.stripe.com/payment-links/share)
[Track a payment link](https://docs.stripe.com/payment-links/url-parameters)
[Create a buy button](https://docs.stripe.com/payment-links/buy-button)
[Customize checkout for payment links](https://docs.stripe.com/payment-links/customize)
[Charge for shipping](https://docs.stripe.com/payments/no-code/charge-shipping)
[Promotion codes, optional items, and upsells](https://docs.stripe.com/payment-links/promotions)
After you receive payment from a payment link


[Build a payments page](https://docs.stripe.com/payments/checkout)
[Build a custom integration with Elements](https://docs.stripe.com/payments/advanced)
[Build an in-app integration](https://docs.stripe.com/payments/mobile)
[Use Managed Payments](https://docs.stripe.com/payments/managed-payments)
[Recurring payments](https://docs.stripe.com/recurring-payments)[Migrate legacy integrations](https://docs.stripe.com/payments/migrations)
In-person payments
[Overview](https://docs.stripe.com/terminal)[How Terminal works](https://docs.stripe.com/terminal/overview)[Availability](https://docs.stripe.com/terminal/payments/collect-card-payment/supported-card-brands)
[Readers](https://docs.stripe.com/terminal/payments/setup-reader)
[Ready-made apps](https://docs.stripe.com/terminal/payments/ready-made-apps)
Custom integration
Payment methods
[Add payment methods](https://docs.stripe.com/payments/payment-methods/overview)
Manage payment methods
[Faster checkout with Link](https://docs.stripe.com/payments/link)
Payment operations
[Analytics](https://docs.stripe.com/payments/analytics)
[Balances and settlement time](https://docs.stripe.com/payments/balances)
Compliance and security
[Currencies](https://docs.stripe.com/currencies)
[Declines](https://docs.stripe.com/declines)
[Disputes](https://docs.stripe.com/disputes)
Payouts
[Receipts](https://docs.stripe.com/receipts)[Refunds and cancellations](https://docs.stripe.com/refunds)
Advanced integrations
[Custom payment flows](https://docs.stripe.com/payments/more-payment-scenarios)
[Flexible acquiring](https://docs.stripe.com/payments/flexible-payments)
[Off-Session Payments](https://docs.stripe.com/payments/off-session-payments)
[Multiprocessor orchestration](https://docs.stripe.com/payments/orchestration)
Beyond payments
[Incorporate your company](https://docs.stripe.com/atlas)
[Agentic commerce](https://docs.stripe.com/agentic-commerce)
[Financial Connections](https://docs.stripe.com/financial-connections)
[Climate](https://docs.stripe.com/climate)
United StatesEnglish (United States)
  1. [Home](https://docs.stripe.com/)/
  2. [Payments](https://docs.stripe.com/payments)/
  3. [Use Payment Links](https://docs.stripe.com/payment-links)


#  After a payment link payment
## Learn what you can do after receiving a payment link payment.
Ask about this page
Copy for LLMView as Markdown
Set up agent
After you receive a payment through a payment link, you can perform actions such as track payments, manage fulfillment automatically, and view payment link metrics.
## Track payments 
Dashboard
API
After your customer makes a payment using a payment link, you can see it in the payments overview in the [Dashboard](https://dashboard.stripe.com/payments). If you’re new to Stripe, you receive an email after your first payment. To receive emails for all successful payments, update your notification preferences in your [Personal details](https://dashboard.stripe.com/settings/user) settings.
If you’re selling a subscription or [saving a payment method for future use](https://docs.stripe.com/payment-links/customize#save-payment-details-for-future-use) and don’t specify an existing customer, the Checkout Session creates a new [customer](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-customer_creation). For one-time payments, the Checkout Session uses a [guest customer](https://docs.stripe.com/payments/checkout/guest-customers) instead.
## Automatically handle fulfillment 
You can automatically handle fulfillment through a Stripe partner or programmatically with the Stripe API:
  * **Automation with a Stripe partner:** To automate post-purchase activities such as order fulfillment, emailing customers, and recording data to a spreadsheet, you can use a Stripe partner, such as [Zapier](https://help.zapier.com/hc/articles/10821467221133), to connect Stripe data to other applications.
  * **Handle fulfillment programmatically:** If you’re interested in handling fulfillment programmatically using the Stripe API and [webhooks](https://docs.stripe.com/webhooks), learn how to [fulfill orders after a customer pays](https://docs.stripe.com/checkout/fulfillment).


## Change confirmation behavior 
Dashboard
API
After a successful payment, your customer sees a localized confirmation message thanking them for their purchase. You can customize the confirmation message or redirect to a URL of your choice. To change the confirmation behavior on a payment link, click **After the payment** when [creating](https://dashboard.stripe.com/payment-links/create) or editing a payment link. Under **Confirmation page** , you can choose to replace the default message with a custom one.
You can also choose to redirect your customers to your website instead of providing a confirmation page. If you redirect your customers to your own confirmation page, you can include `{CHECKOUT_SESSION_ID}` in the redirect URL to dynamically pass the customer’s current Checkout Session ID. This is helpful if you want to tailor the success message on your website based on the information in the Checkout Session. You can also add [UTM codes](https://docs.stripe.com/payment-links/url-parameters#track-campaigns-with-utm-codes) as parameters in the query string of the payment link URL. The UTM codes are automatically added to your redirect URL when your customer completes a payment.
## Use payment links with Connect 
With Stripe Connect, you can split a payment with a connected account by taking application fees. Learn how to [use payment links with Connect](https://docs.stripe.com/connect/payment-links#collecting-fees).
## Let customers manage their subscriptions 
Create a link that you can send to customers, letting them log in and manage their subscriptions using the [customer portal](https://docs.stripe.com/billing/subscriptions/customer-portal).
## Send email receipts 
You can send receipts to customers [automatically](https://docs.stripe.com/receipts#automatic) or [manually](https://docs.stripe.com/receipts#manual) after the payment succeeds. Learn more about [receipts](https://docs.stripe.com/receipts).
## View payment link metrics 
You can see metrics such as views, sales, and revenue from a given payment link by clicking the **Payments and analytics** tab after selecting a payment link from the [list view](https://dashboard.stripe.com/payment-links). Be aware that Stripe can delay data for up to 18 hours, and isn’t available in a sandbox. Analytics aren’t supported for links that include recurring prices.
You can use this data to better understand how your link is performing and what its conversion rate is:
  * **Views** : The number of times your payment link was opened.
  * **Sales** : The number of times the payment link was used to complete a purchase.
  * **Revenue** : The gross sales volume that the link generated and is always in your default currency regardless of the presentment currency. Stripe converts the amounts using the exchange rate on the day the payment occurs.


## Refund payment links
To refund a payment using the Dashboard:
  1. Find the payment you want to refund in the [Payments](https://dashboard.stripe.com/payments) page.
  2. Click the overflow menu () to the right of the payment, then select **Refund payment**.
  3. By default, you issue a full refund. For a partial refund, enter a different refund amount.
  4. Select a reason for the refund. If you select **Other** , you must add a note that explains the reason for the refund. Click **Refund**.


### Bulk refunds
The Dashboard supports the bulk refunding of full payments. Select what payments you want to refund by checking the box to the left of each payment—even over multiple pages of results. Then, click **Refund** and select a reason. You can only issue full refunds in this way; partial refunds must be issued individually.
### Refund timing
It typically takes 5-10 business days for the refund to be processed and reflected on the customer’s bank statement. If there are any issues with insufficient funds in your Stripe balance, the refund might be set as pending until resolved.
Was this page helpful?
YesNo
  * Need help? [Contact Support](https://support.stripe.com/).
  * Chat with Stripe developers on [Discord](https://stripe.com/go/developer-chat).
  * Check out our [changelog](https://docs.stripe.com/changelog).
  * Questions? [Contact Sales](https://stripe.com/contact/sales).
  * LLM? [Read llms.txt](https://docs.stripe.com/llms.txt).
  * Powered by [Markdoc](https://markdoc.dev)


On this page
[Track payments](https://docs.stripe.com/payment-links/post-payment#track-payments "Track payments")
[Automatically handle fulfillment](https://docs.stripe.com/payment-links/post-payment#automatically-handle-fulfillment "Automatically handle fulfillment")
[Change confirmation behavior](https://docs.stripe.com/payment-links/post-payment#change-confirmation-behavior "Change confirmation behavior")
[Use payment links with Connect](https://docs.stripe.com/payment-links/post-payment#split-payment-with-a-connected-account "Use payment links with Connect")
[Let customers manage their subscriptions](https://docs.stripe.com/payment-links/post-payment#let-customers-manage-their-subscriptions "Let customers manage their subscriptions")
[Send email receipts](https://docs.stripe.com/payment-links/post-payment#send-email-receipts "Send email receipts")
[View payment link metrics](https://docs.stripe.com/payment-links/post-payment#view-payment-link-metrics "View payment link metrics")
[Refund payment links](https://docs.stripe.com/payment-links/post-payment#refund-payment-links "Refund payment links")
[Bulk refunds](https://docs.stripe.com/payment-links/post-payment#bulk-refunds "Bulk refunds")
[Refund timing](https://docs.stripe.com/payment-links/post-payment#refund-timing "Refund timing")

