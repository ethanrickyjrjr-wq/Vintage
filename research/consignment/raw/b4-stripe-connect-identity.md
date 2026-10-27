[Skip to content](https://docs.stripe.com/connect/identity-verification#main-content)
Identity verification for connected accounts
[Create account](https://dashboard.stripe.com/register/connect) or [Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fidentity-verification)
[The Stripe Docs logo](https://docs.stripe.com/)
Search`/`Ask AI
[Create account](https://dashboard.stripe.com/register/connect)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fidentity-verification)
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
[Account capabilities and configurations](https://docs.stripe.com/connect/account-capabilities)
[Required verification information](https://docs.stripe.com/connect/required-verification-information)
[Handle verification updates](https://docs.stripe.com/connect/handle-verification-updates)
[Handle verification with the API](https://docs.stripe.com/connect/handling-api-verification)
[Handle verification with tokens](https://docs.stripe.com/connect/account-tokens)
[Test account verification](https://docs.stripe.com/connect/testing-verification)
Identity verification for connected accounts
[Update verified info](https://docs.stripe.com/connect/update-verified-information)
[Additional verifications](https://docs.stripe.com/connect/additional-verifications)


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
  3. Capabilities and information requirements/
  4. [Required verification information](https://docs.stripe.com/connect/required-verification-information)


#  Identity verification for connected accounts
## Use identity verification to reduce risk on your platform when using Connect.
Ask about this page
Copy for LLMView as Markdown
Set up agent
### Applicable connected accounts
This content applies only to connected accounts with [certain configurations](https://docs.stripe.com/connect/integration-recommendations).
This content applies to connected accounts where the platform is responsible for collecting updated information when requirements are due or change.
Every country has its own requirements that accounts must meet so that Stripe can pay out funds to individuals and companies. These are typically known as [Know Your Customer](https://support.stripe.com/questions/know-your-customer-obligations) (KYC) requirements. Regardless of the country, broadly speaking, the requirements Stripe must meet are:
  * Collecting information about the individual or company receiving funds
  * Verifying information to establish that we know who our customers are


[Connect](https://docs.stripe.com/connect) platforms collect the required information from users and provide it to Stripe. This can include information about the legal entity and personal information about the representative of the business, and those who own or control the business. Stripe then attempts verification. In some cases, Stripe might be able to verify an account by confirming some or all of the keyed-in data provided. In other cases, Stripe might require additional information, including, for example, a scan of a valid government-issued ID, a proof of address document, or both.
### Additional verifications
You can proactively verify identity requirements beyond standard KYC using [additional document verification for connected accounts](https://docs.stripe.com/connect/additional-verifications/identity-document).
This page explains the verification flow options to meet Stripe KYC requirements, but the recommended way to manage verification is to integrate [Connect Onboarding](https://docs.stripe.com/connect/custom/hosted-onboarding), which lets Stripe take care of the complexity around the basic KYC obligations. Handling the details of account verification is initially complex and requires vigilance to keep up with the constantly evolving regulatory changes around the world.
If you decide to handle account verification yourself, continue reading to learn about the verification flow options, how API fields translate to companies and individuals, and how to localize information requests. Also, read [Handling Identity Verification with the API](https://docs.stripe.com/connect/handling-api-verification) to learn how to programmatically provide information and handle requests.
Even after Stripe verifies a connected account, platforms still must [monitor for and prevent fraud](https://docs.stripe.com/connect/risk-management/best-practices#fraud). Don’t rely on Stripe’s verification to meet any independent legal KYC or verification requirements.
## Verification requirements 
Verification requirements for connected accounts vary by account, depending on:
  * Country
  * Capabilities
  * Business type (for example, individual, company)
  * Business structure (for example, public corporation, private partnership)
  * The service agreement type between Stripe and the connected account
  * The risk level


You must collect and verify specific information to enable charges and [payouts](https://docs.stripe.com/payouts). For example, for a company in the US, you might need to collect:
  * Information about the business (for example, name, address, tax ID number).
  * Information about the person opening the Stripe account (for example, name, date of birth).
  * Information about [beneficial owners](https://support.stripe.com/questions/beneficial-owner-and-director-definitions) (for example, name, email).


At certain variable thresholds—usually when a specified amount of time has passed or volume of charges have been made—you might need to collect and verify additional information. Stripe temporarily pauses charges or payouts if the information isn’t provided or verified according to the thresholds for [required information](https://docs.stripe.com/connect/required-verification-information). For example, additional information might include verification of the company tax ID number.
## Onboarding flows 
As the platform, you must decide if you want to collect the required information from your connected accounts up front or incrementally. Up-front onboarding collects the `eventually_due` requirements for the account, while incremental onboarding only collects the `currently_due` requirements. You can control this behavior using the [collection_options.fields](https://docs.stripe.com/api/account_links/create#create_account_link-collection_options-fields) parameter.  
| Onboarding type  | Advantages  |  
| --- | --- |  
| **Up-front**  | 
  * Normally requires only one request for all information
  * Avoids the possibility of payout and processing issues due to missed deadlines
  * Exposes potential risk early when accounts refuse to provide information

 |  
| **Incremental**  | 
  * Accounts can onboard quickly because they don’t have to provide as much information

 |  
To determine whether to use up-front or incremental onboarding, review the [requirements](https://docs.stripe.com/connect/required-verification-information) for your connected accounts’ locations and capabilities. While Stripe tries to minimize any impact to connected accounts, requirements might change over time.
For connected accounts where you’re responsible for requirement collection, you can customize the behavior of [future requirements](https://docs.stripe.com/connect/handle-verification-updates) using the `collection_options` parameter. To collect the account’s future requirements, set [collection_options.future_requirements](https://docs.stripe.com/api/account_links/create#create_account_link-collection_options-future_requirements) to `include`.
### Collect additional public details
Stripe collects the required public details for each connected account. You can choose additional fields to collect during onboarding according to your business needs. Any fields you choose that Stripe doesn’t require appear as optional, and connected accounts can choose whether to provide them.
  1. In the [Public details](https://dashboard.stripe.com/settings/connect/onboarding-options/public-details) settings in the Dashboard, enable the **Collect public details** toggle.
  2. Select the fields to show to connected accounts during onboarding.
  3. Click **Save**.


#### Available fields
You can collect the following public details:  
| Field  | Description  |  
| --- | --- |  
| [Statement descriptor](https://docs.stripe.com/connect/statement-descriptors)  | The text that appears on a customer’s credit card or bank statement for payments made to the connected account.  |  
| Customer support phone number  | A phone number customers can call for support related to the connected account.  |  
| Customer support address  | A mailing address customers can use to contact the connected account.  |  
| Customer support email  | An email address customers can use to contact the connected account.  |  
#### Requirements vary
Stripe’s requirements vary by connected account based on their business type, country, and requested capabilities. Enable fields to make sure they always appear during onboarding, whether or not they’re required.
## Business type 
The specific KYC information depends on the [type of business entity](https://docs.stripe.com/api/accounts/object#account_object-business_type). They’re:
  * `individual`: Collect information about the person.
  * `company`: Collect information about the company. Depending on the countries your connected accounts are in, you might also have to collect information about [beneficial owners](https://support.stripe.com/questions/beneficial-owner-and-director-definitions).
  * `non_profit`: Collect information about the non-profit organization.
  * `government_entity` (available for US connected accounts only): Collect information about the government entity.


If you or your users are unsure of their entity type, the information might be in the business formation documents or tax documents for that entity.
See the [list of requirements](https://docs.stripe.com/connect/required-verification-information) for different business types by country. When you know what information to collect, you can read more about [handling identity verification with the API](https://docs.stripe.com/connect/handling-api-verification).
## Business structure 
For all business types other than `individual`, you can further classify your user’s business by identifying its legal (business) structure. A business structure describes the details of a business entity such as day-to-day operations, tax burdens, liability, and organizational schema. You can classify it by using [company[structure]](https://docs.stripe.com/api/accounts/create#create_account-company-structure) in the `Accounts` object.
Providing this information to Stripe gets you the most accurate business classification for compliance purposes. While it isn’t required, it can reduce onboarding requirements. For example, you’re required to provide owner information for private companies, but not for public companies. If you don’t provide information on the `structure`, Stripe defaults to classifying the company as private and requires you to provide owner information. See the [list of requirements](https://docs.stripe.com/connect/required-verification-information) for the supported business structures in all countries.
Country:
Australia (AU) Canada (CA) Germany (DE) Singapore (SG) Thailand (TH) United Arab Emirates (AE) United Kingdom (GB) Hong Kong (HK) United States (US)
### Companies
See the table below for descriptions of the different business structures that you can use to classify a `company`. Refer to the [US required verification information](https://docs.stripe.com/connect/required-verification-information#minimum-verification-requirements-for-united-states) section for more details on requirements.
If you or your users think the entity type should be `company` but are unsure, the information might be in the business formation documents or tax documents for that entity.  
| Business structure  | Description  |  
| --- | --- |  
| `multi_member_llc`  | A business with multiple owners or members that’s registered in a US state as a Limited Liability Company (LLC).  |  
| `private_corporation`  | A business incorporated in a US state that’s privately owned. It doesn’t have shares that are traded on a public stock exchange. It’s also called a closely-held corporation. If you’re a single-member LLC that has elected to be treated as a corporation for tax purposes, use this classification.  |  
| `private_partnership`  | A business jointly owned by two or more people that’s created through a partnership agreement.  |  
| `public_corporation`  | A business incorporated under the laws of a US state. Ownership shares of this corporation are traded on a public stock exchange.  |  
| `public_partnership`  | A business formed by a partnership agreement with one or more people, but has shares that are publicly traded on a stock exchange.  |  
| `single_member_llc`  | A business entity registered with a US state as a limited liability company (LLC) and that has only one member or owner.  |  
| `sole_proprietorship`  | A business that isn’t a separate legal entity from its individual owner.  |  
| `unincorporated_association`  | A business venture of two or more people that doesn’t have a formal corporate or entity structure.  |  
### Non-profits 
See the table below for descriptions of the different business structures that you can use to classify a `non_profit` with. Refer to the [US required verification information](https://docs.stripe.com/connect/required-verification-information#minimum-verification-requirements-for-united-states) section for more details on requirements.  
| Business structure  | Description  |  
| --- | --- |  
| `incorporated_non_profit`  | An organization incorporated under the laws of a US state that has obtained tax-exempt status as a non-profit entity under either state or federal law (for example, 501(c)(3)).  |  
| `unincorporated_non_profit`  | An organization that’s pursuing an objective other than profits, such as a social cause, and has obtained tax-exempt status in the US under either state or federal law (for example, 501(c)(3)) but hasn’t formally incorporated.  |  
### Government entities
See the table below for descriptions of the different business structures that you can use to classify a `government_entity` with. Refer to the [US required verification information](https://docs.stripe.com/connect/required-verification-information#minimum-verification-requirements-for-united-states) section for more details on requirements.  
| Business structure  | Description  |  
| --- | --- |  
| `government_instrumentality`  | An organization formed by a government statute or body based in the US to perform a certain function, but not the actual government body itself.  |  
| `governmental_unit`  | A branch of the state, local, or federal government of the US  |  
| `tax_exempt_government_instrumentality`  | An organization created by or pursuant to government statute and operated for public purposes. It has obtained federal tax-exempt status under state or federal law (for example, 501(c)(3)).  |  
## Internationalization and localization
If you support users in multiple countries, consider internationalization and localization when asking for information. Creating an interface that uses not only the user’s preferred language but also the proper localized terminology results in a smoother onboarding experience.
For example, instead of requesting a business tax ID from your users, regardless of country, request:
  * EIN, US
  * Business Number, Canada
  * Company Number, UK


You can find recommended country-specific labels along with the other [required verification information](https://docs.stripe.com/connect/required-verification-information).
## See also
  * [Stripe-hosted onboarding](https://docs.stripe.com/connect/hosted-onboarding)
  * [Updating Accounts](https://docs.stripe.com/connect/updating-service-agreements)
  * [Handling additional verifications with the API](https://docs.stripe.com/connect/handling-api-verification)
  * [Account tokens](https://docs.stripe.com/connect/account-tokens)
  * [Testing verification](https://docs.stripe.com/connect/testing-verification)


Was this page helpful?
YesNo
  * Need help? [Contact Support](https://support.stripe.com/).
  * Chat with Stripe developers on [Discord](https://stripe.com/go/developer-chat).
  * Check out our [changelog](https://docs.stripe.com/changelog).
  * Questions? [Contact Sales](https://stripe.com/contact/sales).
  * LLM? [Read llms.txt](https://docs.stripe.com/llms.txt).
  * Powered by [Markdoc](https://markdoc.dev)


On this page
[Verification requirements](https://docs.stripe.com/connect/identity-verification#verification-requirements "Verification requirements")
[Onboarding flows](https://docs.stripe.com/connect/identity-verification#onboarding-flows "Onboarding flows")
[Collect additional public details](https://docs.stripe.com/connect/identity-verification#collect-additional-public-details "Collect additional public details")
[Business type](https://docs.stripe.com/connect/identity-verification#business-type "Business type")
[Business structure](https://docs.stripe.com/connect/identity-verification#business-structure "Business structure")
[Companies](https://docs.stripe.com/connect/identity-verification#companies "Companies")
[Non-profits](https://docs.stripe.com/connect/identity-verification#us-nonprofits "Non-profits")
[Government entities](https://docs.stripe.com/connect/identity-verification#government-entities "Government entities")
[Internationalization and localization](https://docs.stripe.com/connect/identity-verification#internationalization-and-localization "Internationalization and localization")
[See also](https://docs.stripe.com/connect/identity-verification#see-also "See also")

