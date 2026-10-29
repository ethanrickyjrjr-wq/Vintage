[Skip to content](https://docs.stripe.com/payment-links/customize#main-content)
Customize checkout for payment links
[Create account](https://dashboard.stripe.com/register) or [Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayment-links%2Fcustomize)
[The Stripe Docs logo](https://docs.stripe.com/)
Search`/`Ask AI
[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayment-links%2Fcustomize)
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
Customize checkout for payment links
[Charge for shipping](https://docs.stripe.com/payments/no-code/charge-shipping)
[Promotion codes, optional items, and upsells](https://docs.stripe.com/payment-links/promotions)
[After you receive payment from a payment link](https://docs.stripe.com/payment-links/post-payment)


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


#  Customize checkout for Payment Links
## Collect additional information, taxes, or update your branding.
Ask about this page
Copy for LLMView as Markdown
Set up agent
When you create a payment link, you can customize the look and feel of a Checkout Session for your user. You can also choose what type of customer information to collect and save for later.
See [After a payment link payment](https://docs.stripe.com/payment-links/post-payment) for more information about customizing a session post-payment, such as redirecting the customer to a branded confirmation page or emailing a receipt.
## Limit the number of times a payment link can be paid 
You can limit the number of times a payment link is paid for. For example, you can place a limit if you have limited inventory, or only want the links to be used once. When the payment link reaches the limit, it automatically deactivates and customers can’t use it to make a purchase. If a customer tries to open the link after the limit has been reached, they’re shown the default message for deactivated links or [a message that you can customize](https://docs.stripe.com/payment-links/customize#custom-deactivated-link-message).
A payment link is considered “paid for” when a Checkout Session is complete. You can see the payments for completed sessions in two different ways, depending on the type of payment link:
  * For payment links that include subscriptions (that is, any link that has a [recurring price](https://docs.stripe.com/products-prices/pricing-models)), go to **Billing** > **Subscriptions**.
  * For all other payment links, go to the payment link’s details page, then **Payments and analytics** > **Recent payments**.


Dashboard
API
To limit the number of payments using the Dashboard:
  1. [Create](https://dashboard.stripe.com/payment-links/create) or edit a payment link.
  2. Select **Limit the number of payments** and enter the number of payments you want to allow before the link deactivates.


## Set a custom message for deactivated links 
If customers try to open a deactivated payment link, they’re shown a default message. You can customize this message in the Dashboard or with the API.
Dashboard
API
You can customize the message for a deactivated link in the Dashboard in two ways:
  * When you [create](https://dashboard.stripe.com/payment-links/create) or edit a payment link, select **Limit the number of payments**. Then select **Change deactivation message** and add your custom message.
  * When you attempt to deactivate a payment link, a modal with a prompt to change the default deactivation message appears. Use that to update the message.


## Collect customer addresses and phone numbers 
You can collect addresses and phone numbers with payment links by adding those fields to the `Checkout Session`.
Dashboard
API
### Collect an address
To collect addresses from your customers:
  1. [Create](https://dashboard.stripe.com/payment-links/create) or edit a payment link.
To edit a payment link go to its details page and click the overflow menu ().
  2. Select **Collect customer addresses** in the **Options** section.
  3. You can collect **Billing addresses only** or you can collect **Billing and shipping addresses**. Choosing either makes these fields required for customers.
  4. If you collect shipping addresses:
     * You need to select the countries you ship to. These countries appear in the **Country** dropdown in the **Shipping Address form** in the checkout session.
     * You can optionally add shipping rates.


### Collect a phone number
If you need to collect phone numbers to complete the transaction:
  1. [Create](https://dashboard.stripe.com/payment-links/create) or edit a payment link.
  2. Select **Require customers to provide a phone number**.


You can configure Payment Links to always collect a billing address, or always collect both a billing and a shipping address. When you collect shipping addresses, you can define the allowed values for shipping countries, and create one or more shipping rates to include in your link.
You can configure Payment Links to collect a phone number for shipping or invoicing. Only collect phone numbers if you need them for the transaction. When choosing this option, the payment page shows a required field to capture your customer’s phone number.
## Collect customer business names and full names 
Collect customers’ business names and full names as fields on your Payment Links.
Dashboard
API
To collect names from your customers using the Dashboard:
  1. [Create](https://dashboard.stripe.com/payment-links/create) or edit a payment link.
  2. Select **Collect customer names**
  3. Configure whether you want to collect business names, individual names or both.
  4. (Optional) Select **Mark as optional** if you want customers to provide their names if they choose. Otherwise, the name fields will be required before checkout.


## Collect business customer tax IDs 
To display a customer’s tax ID and legal business name on invoices, enable tax ID collection on your Payment Links. Learn how to [collect customer tax IDs with Checkout](https://docs.stripe.com/tax/checkout/tax-ids).
## Collect taxes 
Stripe Tax
Managed Payments
Payment Links work with [Stripe Tax](https://stripe.com/tax) to calculate and collect tax on your payments. Stripe Tax is a paid product that automatically calculates the tax on your transactions without the need to define the rates and rules. Fees only apply after you’ve added at least one location where you’re registered to calculate and remit tax.
To get started, [activate Stripe Tax](https://dashboard.stripe.com/tax) in the Dashboard. Learn how to use [products, prices, tax codes, and tax behavior](https://docs.stripe.com/tax/products-prices-tax-codes-tax-behavior) to automatically calculate tax.
Dashboard
API
To enable automatic tax collection using the Dashboard:
  1. [Create](https://dashboard.stripe.com/payment-links/create) or edit a payment link.
  2. Select **Collect tax automatically**.


To accurately determine tax, Stripe Tax collects the customer’s billing address (full address for US customers).
## Collect agreement to your terms of service 
Dashboard
API
You can require that your customers accept your terms of service before completing their purchase. When you set a terms of service URL in your account’s [Public details](https://dashboard.stripe.com/settings/public), you have the option to require a terms of service agreement when you create a payment link in the Dashboard. Enabling this setting requires that your customers click a checkbox to accept your terms in the checkout page. The checkout page also links to your privacy policy if you set a privacy policy URL in your account’s [Public details](https://dashboard.stripe.com/settings/public).
## Add custom fields 
#### Caution
Don’t use custom fields to collect personal, protected, or sensitive data, or information restricted by law.
Dashboard
API
You can add custom fields on the payment form to collect additional information from your customers. The information is available after the payment is complete and is useful for fulfilling the purchase. You can add the following types of fields:  
| Type  | Description  |  
| --- | --- |  
| Text  | Collects freeform text up to 255 characters.  |  
| Numbers only  | Collects only numerical values up to 255 digits.  |  
| Dropdown  | Presents your customers with a list of options to select from. Payment links created through the Dashboard support up to 10 options. You can add up to 200 options after you create a link through the API.  |  
  1. Click **Add custom fields** in the **Options** section.
  2. Select a type of field to add.
  3. Enter a label for the field.
  4. (Optional) Mark your field as required.


Labels for custom fields aren’t translated, but you can use the `locale` [URL parameter](https://docs.stripe.com/payment-links/customize#customize-checkout-with-url-parameters) to set the language of your payment link to match the same language as your labels.
![](https://b.stripecdn.com/docs-statics-srv/assets/customize-payment-link.8d578e56ad9a6171b4763b46e027aa01.png)
After your customer completes the payment, you can view the fields on the payment details page in the Dashboard.
![](https://b.stripecdn.com/docs-statics-srv/assets/payment.56e708902bb56215b40e523371418a6e.png)
The custom fields are also included in the [checkout.session.completed](https://docs.stripe.com/api/events/types#event_types-checkout.session.completed) [webhook](https://docs.stripe.com/webhooks) upon payment completion.
## Automatically convert prices to local currencies 
Each Payment Link you share automatically allows your customers to complete payment in their local currency with [Adaptive Pricing](https://docs.stripe.com/payments/currencies/localize-prices/adaptive-pricing).
You can also set pricing manually for each currency using [manual currency prices](https://docs.stripe.com/payments/checkout/localize-prices/manual-currency-prices).
## Save payment details for future use 
#### Caution
Consult with your legal counsel or compliance team regarding saving and using payment details. For example, the European Data Protection Board issued [guidance](https://www.edpb.europa.eu/documents/recommendation/recommendations-022021-on-the-legal-basis-for-the-storage-of-credit-card) regarding the saving of payment details for faster future checkouts.
If you want to save the payment method information to provide returning customers optional one-click payments in the future, we recommend using [Link](https://docs.stripe.com/payments/link/checkout-link).
To save payment details for a customer, select **Save payment details for future use** in the **Advanced options** section when you [create a Payment Link](https://dashboard.stripe.com/test/payment-links/create).
## Apply branding 
You can customize the [look and feel](https://docs.stripe.com/payments/checkout/customization/appearance#font-compatibility) of the payment page in the Stripe Dashboard. Go to your [branding settings](https://dashboard.stripe.com/account/branding/checkout) to:
  * Upload a logo or icon
  * Customize the payment page’s background color, button color, font, and shapes


You can also customize branding for Payment Links through [Checkout studio](https://docs.stripe.com/payments/checkout-studio/how-it-works#customize-launch-checkout-integration), which provides a visual editor for configuring your Payment Links integration alongside your other Checkout integrations.
## Use your own domain 
If you have your own custom domain, you can add it in the Stripe Dashboard. Instead of Stripe-branded payment links (`buy.stripe.com/`), you can create links using your own subdomain (`pay.example.com`). Learn more about [custom domains](https://docs.stripe.com/payments/checkout/custom-domains).
## Set store policies and contact information 
You can display your return, refund, and legal policies on the payment page in addition to your support contact information.
Go to the [Checkout and Payment Links settings](https://dashboard.stripe.com/settings/checkout) to configure the information you want to display.
Presenting this information can increase customer confidence and minimize [cart abandonment](https://docs.stripe.com/payments/checkout/abandoned-carts).
## Customize checkout with URL parameters 
URL parameters allow you to add additional context to your payment page and streamline checkout. Specify the language that appears during checkout, prefill an email address or promotional code for your customers, track campaigns, and streamline reconciliation.
You can configure URL parameters directly from the Stripe Dashboard, and use them in the query string of your payment link URL. From the [payment links page](https://dashboard.stripe.com/payment-links), click a specific payment link, then click the dropdown menu on the **Copy** button to add URL parameters.
Here’s an example link with prefilled email, promotional code, and locale parameters.

```

https://buy.stripe.com/test_eVa3do41l4Ye6KkcMN?prefilled_email=jenny%40example.com&prefilled_promo_code=20off&locale=de


```
  
| Parameter  | Description  | Syntax  |  
| --- | --- | --- |  
| `prefilled_email`  | Use `prefilled_email` to enter an email address on the payment page automatically. Your end customer can still edit this field, so the email you pass in for `prefilled_email` might not be the same email that your customer uses to complete the payment.  |  `prefilled_email` must be a valid email address. Invalid values are disregarded and your payment page continues to work as expected. We recommend [encoding](https://en.wikipedia.org/wiki/Percent-encoding) email addresses that you attach as URL parameters to reduce the risk of them not being passed through to your payment page.  |  
| `locked_prefilled_email`  | Use `locked_prefilled_email` to enter an uneditable email address on the payment page automatically.  |  `locked_prefilled_email` must be a valid email address. Invalid values are disregarded and your payment page continues to work as expected. If both `prefilled_email` and `locked_prefilled_email` are passed, `locked_prefilled_email` takes precedence. We recommend [encoding](https://en.wikipedia.org/wiki/Percent-encoding) email addresses that you attach as URL parameters to reduce the risk of them not being passed through to your payment page.  |  
| `prefilled_promo_code`  |  Use `prefilled_promo_code` to enter a [promotion code](https://docs.stripe.com/api/promotion_codes) on the payment page automatically. Your customer can still edit this field, so the promotion code you pass in for `prefilled_promo_code` might not be the same promotion code that your customer uses to complete the payment. You must also [enable promotion codes](https://docs.stripe.com/payment-links/promotions) on your payment link, or this parameter has no effect.  | `prefilled_promo_code` must be composed of alphanumeric characters and can’t use any special characters. Promotion codes are case insensitive. Invalid values are disregarded and your payment page continues to work as expected.  |  
| `prefilled_amount`  | Use `prefilled_amount` to set the initial amount on a pay-what-you-want payment link. Your customer can still edit this amount before completing the payment. This parameter has no effect on fixed-price payment links.  |  `prefilled_amount` must be a positive integer in the custom price currency’s smallest unit. For example, to preset 20.00 USD, pass `prefilled_amount=2000`. The value must also satisfy the custom price’s configured minimum and maximum amounts. Invalid values are disregarded. Checkout uses the payment link’s stored preset amount as the fallback, or displays the default empty state if the link has no stored preset. `prefilled_amount` limits the functionality of [multi-currency prices](https://docs.stripe.com/products-prices/manage-prices#use-multi-currency-prices). The amount is always in the price’s default currency, preventing Checkout from automatically using the customer’s local currency and raising an error when the payment link is created with the [currency](https://docs.stripe.com/api/payment-link/create#create_payment_link-currency) parameter set to a non-default currency.  |  
| `locale`  | Use `locale` to display your payment link in a specific language for your customers regardless of their location.  | View the complete list of all [supported languages](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-locale).  |  
You can also use URL parameters to [track payment links and related campaigns](https://docs.stripe.com/payment-links/url-parameters).
## Limit customers to one subscription 
You can redirect customers that already have a subscription to the [customer portal](https://docs.stripe.com/billing/subscriptions/customer-portal) or your website to manage their subscription. Learn more about [limiting customers to one subscription](https://docs.stripe.com/payments/checkout/limit-subscriptions).
## Support free trials without collecting payment method details 
For Payment Links that you create with a product that includes a free trial, you can allow customers to sign up for a subscription without providing their payment method details.
Dashboard
API
To configure trials without payment methods for Payment Links in the Dashboard:
  * When you [create](https://dashboard.stripe.com/payment-links/create) or edit a payment link with a subscription product, select **Include a free trial**. Then select **Let customers start trial without payment method**.
  * Set [subscription email reminders](https://docs.stripe.com/payments/checkout/free-trials#collect-payment) to make sure that Stripe prompts your customer to add their payment information before the trial ends. Otherwise, Stripe pauses the trial.


## Allow adjustable quantities 
You can configure payment links to allow your customers to update the quantity of the items they purchase.
Dashboard
API
To let your customers update the quantity of the items they purchase, [create a payment link](https://docs.stripe.com/payment-links/create) and add a product. In the payment link editor, go to **Payment page** > **Product** section, and then select **Let customers adjust quantity** in the product description. You can optionally set the minimum and maximum quantities.
## Collect surcharges 
Automatic surcharge adds a surcharge to your Payment Links payments based on your customer’s card details, including card brand, funding type, and issuing country. Stripe enables the ability to seamlessly use a third-party surcharging provider to compliantly calculate the surcharge amount.
This feature is in private preview. [Request access.](https://docs.stripe.com/payment-links/customize#checkout_beta_preview)
Automatic surcharge
Enter your email to request access.
Email
Email
Submit
[Privacy policy](https://stripe.com/privacy)
#### Warning
Surcharging laws vary by jurisdiction. Before using this feature, review the [Compliance requirements](https://docs.stripe.com/payments/checkout/surcharge/automatic-surcharge#compliance) to understand your obligations.
### Install a surcharge provider app
Before you can use automatic surcharge, install a surcharge provider’s Stripe App from the [Dashboard App Marketplace](https://marketplace.stripe.com/) and complete the onboarding process. Stripe supports [Yeeld](https://marketplace.stripe.com/apps/yeeld) and [InterPayments](https://marketplace.stripe.com/apps/interpayments) to provide surcharges.
#### Warning
You’re responsible for verifying your provider is calculating surcharges in compliance with applicable laws and card network rules in each jurisdiction where you operate.
### Create a payment link with automatic surcharge
#### API version
This feature requires a preview API version. Set the `Stripe-Version` header to a preview API version when creating the payment link.
Automatic surcharge for Payment Links is available through the API only. It works with one-off products and [customer-chooses-what-to-pay](https://docs.stripe.com/products-prices/how-products-and-prices-work#variable-pricing) pricing, but doesn’t support payment links that include subscriptions (that is, any link that has a [recurring price](https://docs.stripe.com/products-prices/pricing-models)). It also isn’t compatible with [Adaptive Pricing](https://docs.stripe.com/payments/checkout/localize-prices/adaptive-pricing).
Set [automatic_surcharge[enabled]](https://docs.stripe.com/api/payment-link/create#create_payment_link-automatic_surcharge-enabled) to `true` when creating a payment link, along with an `automatic_surcharge[calculation_basis]`.
Command Line
Select a language
cURL
cURL
Stripe CLI
Ruby
Python
PHP
Java
Node.js
Go
.NET

```


curl https://api.stripe.com/v1/payment_links \
  -u "sk_test_...:" \
  -H "Stripe-Version: 2026-09-30.preview" \
  -d "line_items[0][price]=
{{PRICE_ID}}
" \
  -d "line_items[0][quantity]=1" \
  -d "automatic_surcharge[enabled]=true" \
  -d "automatic_surcharge[calculation_basis]=total_before_tax"





```

### Calculation basis
The [automatic_surcharge[calculation_basis]](https://docs.stripe.com/api/payment-link/create#create_payment_link-automatic_surcharge-calculation_basis) determines which amount is used as the basis for calculating the surcharge.  
| Value   | Description   | Use when   |  
| --- | --- | --- |  
| `total_before_tax`  | Calculates the surcharge on the subtotal before taxes. For example, a 3% surcharge on a 100 USD order with 10 USD tax = 3.00 USD surcharge.  | Regulations or business policy require surcharging only on the pre-tax amount.  |  
| `total_after_tax`  | Calculates the surcharge on the total after taxes. For example, a 3% surcharge on a 100 USD order with 10 USD tax = 3.30 USD surcharge (calculated on 110 USD).  | You want the surcharge to cover payment processing costs on the full charged amount.  |  
### Tax compatibility
Automatic surcharge is compatible with [Stripe Tax](https://docs.stripe.com/tax) using automatic tax. Use [automatic_surcharge[tax_behavior]](https://docs.stripe.com/api/payment-link/create#create_payment_link-automatic_surcharge-tax_behavior) to control whether the surcharge is calculated inclusive or exclusive of tax.
#### Private preview
During this private preview, automatic surcharge is only supported in the United States. Supported payment methods are cards and Apple Pay. Transactions with a non-supported payment method don’t have any applicable surcharge.
Was this page helpful?
YesNo
  * Need help? [Contact Support](https://support.stripe.com/).
  * Chat with Stripe developers on [Discord](https://stripe.com/go/developer-chat).
  * Check out our [changelog](https://docs.stripe.com/changelog).
  * Questions? [Contact Sales](https://stripe.com/contact/sales).
  * LLM? [Read llms.txt](https://docs.stripe.com/llms.txt).
  * Powered by [Markdoc](https://markdoc.dev)


On this page
[Limit the number of times a payment link can be paid](https://docs.stripe.com/payment-links/customize#limit-payments "Limit the number of times a payment link can be paid")
[Set a custom message for deactivated links](https://docs.stripe.com/payment-links/customize#custom-deactivated-link-message "Set a custom message for deactivated links")
[Collect customer addresses and phone numbers](https://docs.stripe.com/payment-links/customize#collect-addresses-and-phone-numbers "Collect customer addresses and phone numbers")
[Collect an address](https://docs.stripe.com/payment-links/customize#collect-an-address "Collect an address")
[Collect a phone number](https://docs.stripe.com/payment-links/customize#collect-a-phone-number "Collect a phone number")
[Collect customer business names and full names](https://docs.stripe.com/payment-links/customize#collect-names "Collect customer business names and full names")
[Collect business customer tax IDs](https://docs.stripe.com/payment-links/customize#collect-business-customer-tax-ids "Collect business customer tax IDs")
[Collect taxes](https://docs.stripe.com/payment-links/customize#collect-taxes "Collect taxes")
[Collect agreement to your terms of service](https://docs.stripe.com/payment-links/customize#collect-agreement-to-terms-of-services "Collect agreement to your terms of service")
[Add custom fields](https://docs.stripe.com/payment-links/customize#add-custom-fields "Add custom fields")
[Automatically convert prices to local currencies](https://docs.stripe.com/payment-links/customize#convert-to-local-currency "Automatically convert prices to local currencies")
[Save payment details for future use](https://docs.stripe.com/payment-links/customize#save-payment-details-for-future-use "Save payment details for future use")
[Apply branding](https://docs.stripe.com/payment-links/customize#apply-branding "Apply branding")
[Use your own domain](https://docs.stripe.com/payment-links/customize#custom-domains "Use your own domain")
[Set store policies and contact information](https://docs.stripe.com/payment-links/customize#set-store-policies-and-contact-information "Set store policies and contact information")
[Customize checkout with URL parameters](https://docs.stripe.com/payment-links/customize#customize-checkout-with-url-parameters "Customize checkout with URL parameters")
[Limit customers to one subscription](https://docs.stripe.com/payment-links/customize#limit-subscriptions "Limit customers to one subscription")
[Support free trials without collecting payment method details](https://docs.stripe.com/payment-links/customize#trials-without-payment-method "Support free trials without collecting payment method details")
[Allow adjustable quantities](https://docs.stripe.com/payment-links/customize#allow-adjustable-quantities "Allow adjustable quantities")
[Collect surcharges](https://docs.stripe.com/payment-links/customize#collect-surcharges "Collect surcharges")
[Install a surcharge provider app](https://docs.stripe.com/payment-links/customize#install-a-surcharge-provider-app "Install a surcharge provider app")
[Create a payment link with automatic surcharge](https://docs.stripe.com/payment-links/customize#create-a-payment-link-with-automatic-surcharge "Create a payment link with automatic surcharge")
[Calculation basis](https://docs.stripe.com/payment-links/customize#calculation-basis "Calculation basis")
[Tax compatibility](https://docs.stripe.com/payment-links/customize#tax-compatibility "Tax compatibility")

