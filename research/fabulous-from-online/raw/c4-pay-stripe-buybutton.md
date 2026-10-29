[Skip to content](https://docs.stripe.com/payment-links/buy-button#main-content)
Create a buy button
[Create account](https://dashboard.stripe.com/register) or [Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayment-links%2Fbuy-button)
[The Stripe Docs logo](https://docs.stripe.com/)
Search`/`Ask AI
[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayment-links%2Fbuy-button)
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
Create a buy button
[Customize checkout for payment links](https://docs.stripe.com/payment-links/customize)
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


#  Create an embeddable buy button
## Use Payment Links to create an embeddable buy button for your website.
Ask about this page
Copy for LLMView as Markdown
Set up agent
Create an embeddable buy button to sell a product, subscription, or accept a payment on your website. Start by selecting an existing link from the [Payment Links list view](https://dashboard.stripe.com/payment-links) or by [creating a new link](https://dashboard.stripe.com/payment-links/create) where you can decide which products to sell and customize the checkout UI. After you create your link, click **Buy button** to configure the buy button design and generate the code that you can copy and paste into your website.
## Customize the button
By default, your buy button uses the same branding and call to action configured for your payment link. You can:
  * Choose between a simple button and a card widget.
  * Set brand colors, shapes, and fonts to match your website.
  * Set the language of the button and payment page to match your website’s language.
  * Customize your button’s call to action.


![Customize the buy button](https://b.stripecdn.com/docs-statics-srv/assets/buy-button-card-layout.4003c3e9ffe3ce4378092dbdcd456ed9.png)
Customize the buy button
## Embed the button
Stripe provides an embed code composed of a `<script>` tag and a `<stripe-buy-button>` web component. Click **Copy code** to copy the code and paste it into your website.
If you’re using HTML, paste the embed code into the HTML. If you’re using React, include the `script` tag in your `index.html` page to mount the `<stripe-buy-button>` component.
#### Caution
The buy button uses your account’s [publishable API key](https://docs.stripe.com/keys#obtain-api-keys). If you revoke the API key, you need to update the embed code with your new publishable API key.
index.html
Select a language
HTML
HTML
React

```

<body>
  <h1>Purchase your new kit</h1>
  <!-- Paste your embed code script here. -->
  <script
    async
    src="https://js.stripe.com/v3/buy-button.js[](https://js.stripe.com/v3/buy-button.js)">
  </script>
  <stripe-buy-button
    buy-button-id=
"{{BUY_BUTTON_ID}}"

    publishable-key="pk_test_..."
  >
  </stripe-buy-button>
</body>

```

## Attributes to customize checkout  
| Parameter  | Description  | Syntax  |  
| --- | --- | --- |  
| `client-reference-id`  | Use `client-reference-id` to attach a unique string of your choice to the `CheckoutSession`. The string can be a customer ID, a cart ID, or something similar that you use to reconcile the `CheckoutSession` with your internal systems. If you pass this parameter to your `<stripe-buy-button>`, it’s sent in the [checkout.session.completed webhook](https://docs.stripe.com/api/events/types#event_types-checkout.session.completed) upon payment completion.  | The `client-reference-id` can contain alphanumeric characters, dashes, or underscores, and be any value up to 200 characters. Invalid values are silently dropped, but your payment page continues to work as expected.  |  
| `customer-email`  | Use `customer-email` to prefill the email address on the payment page. When the property is set, the buy button passes it to the `CheckoutSession`’s `customer_email` attribute. The customer can’t edit the email address on the payment page.  | The `customer-email` must be a valid email. Invalid values are silently dropped, but your payment pages continues to work as expected.  |  
| `customer-session-client-secret`  | Use `customer-session-client-secret` to [pass an existing customer](https://docs.stripe.com/payment-links/buy-button#pass-an-existing-customer).  | The `customer-session-client-secret` value must be generated from the [client_secret](https://docs.stripe.com/api/customer_sessions/object#customer_session_object-client_secret).  |  
## Pass an existing customer 
#### Use the Accounts v2 API to represent customers
The Accounts v2 API is generally available for Connect users, and in public preview for other Stripe users. If you’re part of the Accounts v2 preview, you need to specify a [preview version](https://docs.stripe.com/api-v2-overview#sdk-and-api-versioning) in your code.
To join the Accounts v2 preview, go to [Account previews and features](https://dashboard.stripe.com/settings/previews) in your Dashboard and enable **Reusable payment methods for Global Payouts**.
For most use cases, we recommend [modeling your customers as customer-configured Account objects](https://docs.stripe.com/accounts-v2/use-accounts-as-customers) instead of using [Customer](https://docs.stripe.com/api/customers) objects.
Accounts v2
Customer v1
You can provide an existing [customer-configured Account](https://docs.stripe.com/api/v2/core/accounts/object#v2_account_object-configuration-customer) object to `CheckoutSessions` created from the buy button. Authenticate the customer on the server, then create a `CustomerSession` for them and return the [client_secret](https://docs.stripe.com/api/customer_sessions/object#customer_session_object-client_secret) to the client.
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


curl https://api.stripe.com/v1/customer_sessions \
  -u "sk_test_...:" \
  -d "customer_account=
{{CUSTOMER_ACCOUNT_ID}}
" \
  -d "components[buy_button][enabled]=true"


```

Set the `customer-session-client-secret` attribute on the `<stripe-buy-button>` web component to the [client_secret](https://docs.stripe.com/api/customer_sessions/object#customer_session_object-client_secret) from the CustomerSession.
You must provide the [client_secret](https://docs.stripe.com/api/customer_sessions/object#customer_session_object-client_secret) within 30 minutes. After providing the client secret, you have an additional 30 minutes until the `CustomerSession` expires. After it expires, the buy button can’t create any `CheckoutSessions`.
Don’t cache the client secret. Instead, generate a new one every time you render a buy button.
index.html
Select a language
HTML
HTML
React

```


<body>
  <script
    async
    src="https://js.stripe.com/v3/buy-button.js[](https://js.stripe.com/v3/buy-button.js)">
  </script>
  <stripe-buy-button
    buy-button-id=
"{{BUY_BUTTON_ID}}"

    publishable-key="pk_test_..."
    customer-session-client-secret="{{CLIENT_SECRET}}"
  >
  </stripe-buy-button>
</body>



```

## Content Security Policy
If you’ve deployed a [Content Security Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP), the policy directives that the buy button requires are:
  * frame-src, https://js.stripe.com
  * script-src, https://js.stripe.com


## Limitations
Rendering the buy button requires a website domain. To test the buy button locally, run a local HTTP server to host your website’s `index.html` file over the localhost domain. To run a local HTTP server, use Python’s [SimpleHTTPServer](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/set_up_a_local_testing_server#running_a_simple_local_http_server) or the [http-server](https://www.npmjs.com/package/http-server) npm module.
## Track payments 
After your customer makes a payment using a payment link, you can see it in the [payments overview](https://dashboard.stripe.com/payments) in the Dashboard.
If you’re new to Stripe, you receive an email after your first payment. To receive emails for all successful payments, update your notification preferences in your [Personal details](https://dashboard.stripe.com/settings/user) settings.
If you’re selling a subscription or [saving a payment method for future use](https://docs.stripe.com/payment-links/customize#save-payment-details-for-future-use) and don’t specify an existing customer, the Checkout Session creates a new [customer](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-customer_creation). For one-time payments, the Checkout Session uses a [guest customer](https://docs.stripe.com/payments/checkout/guest-customers) instead.
Learn more about handling [payment links post-payment](https://docs.stripe.com/payment-links/post-payment), like how to configure post-payment behavior for a buy button or payment link.
Was this page helpful?
YesNo
  * Need help? [Contact Support](https://support.stripe.com/).
  * Chat with Stripe developers on [Discord](https://stripe.com/go/developer-chat).
  * Check out our [changelog](https://docs.stripe.com/changelog).
  * Questions? [Contact Sales](https://stripe.com/contact/sales).
  * LLM? [Read llms.txt](https://docs.stripe.com/llms.txt).
  * Powered by [Markdoc](https://markdoc.dev)


On this page
[Customize the button](https://docs.stripe.com/payment-links/buy-button#customize-the-button "Customize the button")
[Embed the button](https://docs.stripe.com/payment-links/buy-button#embed-the-button "Embed the button")
[Attributes to customize checkout](https://docs.stripe.com/payment-links/buy-button#attributes-to-customize-checkout "Attributes to customize checkout")
[Pass an existing customer](https://docs.stripe.com/payment-links/buy-button#pass-an-existing-customer "Pass an existing customer")
[Content Security Policy](https://docs.stripe.com/payment-links/buy-button#content-security-policy "Content Security Policy")
[Limitations](https://docs.stripe.com/payment-links/buy-button#limitations "Limitations")
[Track payments](https://docs.stripe.com/payment-links/buy-button#track-payments "Track payments")

