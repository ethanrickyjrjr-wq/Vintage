> ## Documentation Index
> Fetch the complete documentation index at: [/help/llms.txt](https://cal.com/help/llms.txt)
> Use this file to discover all available pages before exploring further.
[Skip to main content](https://cal.com/help/event-types/booking-questions#content-area)
[Cal.com Help home page![light logo](https://cal.com/calcom-help.svg)![dark logo](https://cal.com/calcom-help-light.svg)](https://cal.com/help)
Search...
⌘K
  * [Support](https://go.cal.com/support)
  * [Dashboard](https://app.cal.com)
  * [Dashboard](https://app.cal.com)


Search...
Navigation
Booking form
Booking Questions
  * [Documentation](https://cal.com/help/welcome)
  * [Developer](https://cal.com/docs)
  * [GitHub](https://github.com/calcom/cal.com)
  * [Blog](https://cal.com/blog)


### Documentation
  * [Welcome](https://cal.com/help/welcome)
  * Quick Start
  * Account settings
  * Enterprise
  * Billing and Usage
  * Links
    * [What are Links](https://cal.com/help/event-types/event-types)
    * [Link ID](https://cal.com/help/event-types/link-id)
    * [Adding booked links to your calendar](https://cal.com/help/event-types/add-events)
    * [Create your first link](https://cal.com/help/event-types/create-first-event)
    * [Create a recurring link](https://cal.com/help/event-types/create-recurring)
    * [Link slot display issues](https://cal.com/help/event-types/display-issues)
    * [Can Cal.com sponsor my open source project?](https://cal.com/help/event-types/sponsor)
    * [How to troubleshoot symbolic link issues on Windows](https://cal.com/help/event-types/symbolic-issues)
    * [User-level booking limits](https://cal.com/help/event-types/user-booking-limits)
    * Setup
    * Booking experience
      * Booking form
        * [Booking Questions](https://cal.com/help/event-types/booking-questions)
        * [Create a phone-only booking link](https://cal.com/help/event-types/create-phone-only-event-type)
        * [Require/Exclude Email Domains (Booking Question)](https://cal.com/help/event-types/email-bookingq)
        * [Disable guests](https://cal.com/help/event-types/disable-guests)
        * [How to split fullname into firstname and lastname in the public booking page](https://cal.com/help/event-types/split-name)
      * Confirmation
      * Appearance
      * Payments & Seats
    * Policies
    * Teams
  * Events
  * Discover
  * Availabilities
  * Bookings
  * Insights
  * Workflows
  * Cal.ai
  * Embedding
  * Auth and Provisioning
  * Routing
  * Apps and Integrations
  * Privacy and Compliance
  * Security
  * User Roles
  * Importing
  * Developers


## On this page
Back to top
  * [Booking question identifier](https://cal.com/help/event-types/booking-questions#booking-question-identifier)
    * [Where to find a question’s identifier](https://cal.com/help/event-types/booking-questions#where-to-find-a-question%E2%80%99s-identifier)
    * [Use the identifier as a workflow variable](https://cal.com/help/event-types/booking-questions#use-the-identifier-as-a-workflow-variable)
  * [Phone-based bookings](https://cal.com/help/event-types/booking-questions#phone-based-bookings)


Booking form
# Booking Questions
When you create a new link, a few basic booking questions are already created for your new link. If you’d like to collect more information about your attendees, you can use our booking questions feature and get the necessary information filled out by your attendees when booking. The booking questions can be either required or optional, depending on your needs. Let’s say that you require the phone number of each attendee. You must select the correct input type, write up your placeholder and label, and tick the requirement. A new field will appear on the booking page where attendees enter the booking details. You can also make use of the booking questions feature to allow prefilling the [**booking fields**](https://cal.com/docs/core-features/bookings/prefill-fields)
## 
[​](https://cal.com/help/event-types/booking-questions#booking-question-identifier)
Booking question identifier
Every booking question has an **identifier** , a unique key that the booker’s answer is saved under. Cal.com uses it to [prefill the question from the booking link](https://cal.com/help/bookings/prefill-fields), in webhook payloads, and to turn the answer into a [workflow variable](https://cal.com/help/workflows/workflowsoverview#booking-question-variables).
### 
[​](https://cal.com/help/event-types/booking-questions#where-to-find-a-question%E2%80%99s-identifier)
Where to find a question’s identifier
  1. Open the link and go to **Booking form**.
  2. Click **Edit** next to the question.
  3. The **Identifier** field is below **Label**.


![Question settings with the label Company size and the identifier Company-size](https://mintcdn.com/calcomhelp/1mGd7TpIKMGwuB58/images/booking-question-identifier.png?fit=max&auto=format&n=1mGd7TpIKMGwuB58&q=85&s=aa8247a512b299d3607e5a52808469d3)
When you add a question, the identifier is filled in from the label. Spaces and special characters are replaced with dashes, so “Company size” becomes `Company-size`. You can type your own identifier instead. Identifiers can contain letters, numbers, dashes and underscores. The default questions, such as name and email, have fixed identifiers that you can’t change.
### 
[​](https://cal.com/help/event-types/booking-questions#use-the-identifier-as-a-workflow-variable)
Use the identifier as a workflow variable
To add the booker’s answer to a workflow message, write the identifier in uppercase, replace its dashes with underscores, and wrap it in curly brackets. For example, `Company-size` becomes `{COMPANY_SIZE}`. See [booking question variables](https://cal.com/help/workflows/workflowsoverview#booking-question-variables) for details.
If you change an identifier, update any workflows, prefill links or webhook integrations that use the old one. When you edit a question’s label, its identifier changes with it unless you’ve set the identifier yourself.
## 
[​](https://cal.com/help/event-types/booking-questions#phone-based-bookings)
Phone-based bookings
By default, the booking form requires an attendee’s email address to confirm a booking. With phone-based bookings, you can require a phone number instead, so attendees can book using only their phone number without providing an email. This is useful when SMS is your primary channel for confirmations and reminders, when your audience is more likely to share a phone number than an email, or for regions and workflows where phone contact is the standard way to reach attendees. To enable phone-based bookings, go to the **Confirmation** section at the top of your link’s booking questions and switch the toggle from **Email** to **Phone**. This sets the phone number as the required field your booker must provide to receive confirmations, instead of an email address. Once you’ve selected **Phone** , click **Save**.
![Switch between Email and Phone confirmation](https://mintcdn.com/calcomhelp/9S5uZjJMCipJ22CJ/images/booking-questions-email-phone-toggle.png?fit=max&auto=format&n=9S5uZjJMCipJ22CJ&q=85&s=9b80a020ab3d532c97adc32e3e77254c)
[Restriction Schedule](https://cal.com/help/event-types/restriction-schedule)[Create a phone-only booking link](https://cal.com/help/event-types/create-phone-only-event-type)
[x](https://x.com/calcom)[github](https://github.com/calcom)[linkedin](https://www.linkedin.com/company/cal-com)
[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=calcomhelp)

