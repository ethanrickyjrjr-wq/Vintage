Skip to main content
Menu
[![Open API v3 Logo](https://developer.etsy.com/img/logo.svg)**Open API v3**](https://developer.etsy.com/documentation)[Guides](https://developer.etsy.com/documentation/)[API Reference](https://developer.etsy.com/documentation/reference)
[Send feedback](https://github.com/etsy/open-api/discussions)
[![Open API v3 Logo](https://developer.etsy.com/img/logo.svg)**Open API v3**](https://developer.etsy.com/documentation)
  * [Guides](https://developer.etsy.com/documentation/)
  * [API Reference](https://developer.etsy.com/documentation/reference)
  * [Send feedback](https://github.com/etsy/open-api/discussions)


Menu
  * [Introduction](https://developer.etsy.com/documentation/)
  * [API Essentials](https://developer.etsy.com/documentation/essentials/rate-limits/#!)
    * [Authentication](https://developer.etsy.com/documentation/essentials/authentication)
    * [URL Syntax](https://developer.etsy.com/documentation/essentials/urlsyntax)
    * [Definitions](https://developer.etsy.com/documentation/essentials/definitions)
    * [Request Standards](https://developer.etsy.com/documentation/essentials/requests)
    * [Rate Limits](https://developer.etsy.com/documentation/essentials/rate-limits)
    * [Webhooks](https://developer.etsy.com/documentation/essentials/webhooks)
    * [Get help](https://developer.etsy.com/documentation/get-help)
    * [API testing policy](https://www.etsy.com/legal/policy/api-testing-policy/169130941112)
  * [Tutorials](https://developer.etsy.com/documentation/essentials/rate-limits/#!)
    * [Overview](https://developer.etsy.com/documentation/tutorials/overview)
    * [Quick Start Tutorial](https://developer.etsy.com/documentation/tutorials/quickstart)
    * [Fulfillment Tutorial](https://developer.etsy.com/documentation/tutorials/fulfillment)
    * [Listings Tutorial](https://developer.etsy.com/documentation/tutorials/listings)
    * [Inventory and Shipping Data Migration Tutorial](https://developer.etsy.com/documentation/tutorials/inventory-shipping-migration)
    * [Processing Profiles Migration](https://developer.etsy.com/documentation/tutorials/migration)
    * [Rotating Your Shared Secret](https://developer.etsy.com/documentation/tutorials/shared-secret-rotation)
    * [Shop Management Tutorial](https://developer.etsy.com/documentation/tutorials/shopmanagement)
    * [Third Variation Tutorial](https://developer.etsy.com/documentation/tutorials/third-variation)
    * [Payments Tutorial](https://developer.etsy.com/documentation/tutorials/payments)
    * [Personalization Migration](https://developer.etsy.com/documentation/essentials/rate-limits/#!)
      * [Personalization Migration Guide](https://developer.etsy.com/documentation/tutorials/personalization-migration)
      * [Personalization Examples](https://developer.etsy.com/documentation/tutorials/personalization/examples)
      * [Personalization Add-On Pricing](https://developer.etsy.com/documentation/tutorials/personalization-addon-pricing)
  * [MCP Server](https://developer.etsy.com/documentation/essentials/rate-limits/#!)
    * [Dev MCP Server](https://developer.etsy.com/documentation/mcp_server/devmcpserver)
  * [Manage your apps](https://www.etsy.com/developers)
  * [Terms of use](https://www.etsy.com/legal/api)


# Rate Limits
##  Rate Limits and Authentication Types[#](https://developer.etsy.com/documentation/essentials/rate-limits/#rate-limits-and-authentication-types "Direct link to heading")
The API enforces **application-based rate limits** , which consist of Queries Per Day (**QPD**) and Queries Per Second (**QPS**). Rate limits are applied at the API key level for both public auth and private auth.
**You can see your application's current rate limits in the[Developer Portal](https://www.etsy.com/developers/your-apps).**
* * *
##  Daily Limit Mechanism (Sliding Window Structure)[#](https://developer.etsy.com/documentation/essentials/rate-limits/#daily-limit-mechanism-sliding-window-structure "Direct link to heading")
The Queries Per Day (**QPD**) limit does not operate on a fixed 24-hour cycle (e.g., midnight-to-midnight). Instead, we employ a progressive **Sliding Window Rate Limiting Algorithm** to maximize your API usage.
This mechanism calculates your usage based on the requests made over the **last rolling 24-hour period**.
###  How the Sliding Window Works[#](https://developer.etsy.com/documentation/essentials/rate-limits/#how-the-sliding-window-works "Direct link to heading")
  1. **Buckets:** The 24-hour period is divided into a number of smaller, fixed time intervals called **buckets**. Your requests are recorded within these specific buckets.
  2. **Calculation:** Your application's total usage is the sum of requests recorded in all buckets that fall within the current rolling 24-hour window.
  3. **Sliding:** As time passes, the oldest bucket exits the 24-hour window, and a new, empty bucket enters. The quota consumed by the requests in the exiting bucket is **immediately freed up** and becomes available for use.


![Rate Limit Sliding Window](https://developer.etsy.com/assets/images/sliding_window_rate_limit_diagram-a89ed718930bedc79c3d8130b26950cc.png)
* * *
##  Rate Limit Headers[#](https://developer.etsy.com/documentation/essentials/rate-limits/#rate-limit-headers "Direct link to heading")
###  Successful Response[#](https://developer.etsy.com/documentation/essentials/rate-limits/#successful-response "Direct link to heading")
Every successful API response includes headers detailing your application's current usage status against its allocated limits.  
| Header Name  | Description  | Example Value  |  
| --- | --- | --- |  
| **`x-limit-per-second`** |  The total QPS limit for your application's API key.  | 150  |  
| **`x-remaining-this-secon`** |  The remaining number of calls your application can make in the current second.  | 149  |  
| **`x-limit-per-day`** |  The total QPD limit (sliding 24-hour window) for your application's API key.  | 100000  |  
| **`x-remaining-today`** |  The remaining number of calls your application can make within the current 24-hour sliding window.  | 99998  |  
###  Response to Exceeded Limits and Warnings[#](https://developer.etsy.com/documentation/essentials/rate-limits/#response-to-exceeded-limits-and-warnings "Direct link to heading")
Rate limits are evaluated in order: **QPS first, then QPD**. If either limit is exceeded, an error status `429` is returned, along with the `retry-after` header.   
| Header Name  | Description  |  
| --- | --- |  
| **`retry-after`** |  The estimated time (in seconds) the client should wait before retrying a request after hitting a rate limit.  |  
* * *
##  Requesting Higher Limits and Recommendations[#](https://developer.etsy.com/documentation/essentials/rate-limits/#requesting-higher-limits-and-recommendations "Direct link to heading")
###  Request for Increased Quota[#](https://developer.etsy.com/documentation/essentials/rate-limits/#request-for-increased-quota "Direct link to heading")
Applications needing higher limits must contact contact us developer@etsy.com to submit an upgrade request. This process requires:
  1. A detailed description of the application.
  2. An estimate of the required call usage (QPD/QPS).


###  Optimization Recommendations[#](https://developer.etsy.com/documentation/essentials/rate-limits/#optimization-recommendations "Direct link to heading")
To maximize your existing quota and improve application responsiveness:
  * **Implement Caching:** Utilize caching strategies to minimize the number of redundant API calls.
  * **Handle`429` Responses:** Implement a robust retry strategy, such as **exponential backoff** , when receiving a `429` error. While the `retry-after` header provides an estimate, a strategic backoff prevents immediate retry storms.


[Previous « Request Standards](https://developer.etsy.com/documentation/essentials/requests)
[Next Webhooks »](https://developer.etsy.com/documentation/essentials/webhooks)
  * [Rate Limits and Authentication Types](https://developer.etsy.com/documentation/essentials/rate-limits/#rate-limits-and-authentication-types)
  * [Daily Limit Mechanism (Sliding Window Structure)](https://developer.etsy.com/documentation/essentials/rate-limits/#daily-limit-mechanism-sliding-window-structure)
    * [How the Sliding Window Works](https://developer.etsy.com/documentation/essentials/rate-limits/#how-the-sliding-window-works)
  * [Rate Limit Headers](https://developer.etsy.com/documentation/essentials/rate-limits/#rate-limit-headers)
    * [Successful Response](https://developer.etsy.com/documentation/essentials/rate-limits/#successful-response)
    * [Response to Exceeded Limits and Warnings](https://developer.etsy.com/documentation/essentials/rate-limits/#response-to-exceeded-limits-and-warnings)
  * [Requesting Higher Limits and Recommendations](https://developer.etsy.com/documentation/essentials/rate-limits/#requesting-higher-limits-and-recommendations)
    * [Request for Increased Quota](https://developer.etsy.com/documentation/essentials/rate-limits/#request-for-increased-quota)
    * [Optimization Recommendations](https://developer.etsy.com/documentation/essentials/rate-limits/#optimization-recommendations)


#### Documentation
  * [Guides](https://developer.etsy.com/documentation)
  * [API Reference](https://developer.etsy.com/documentation/reference)


#### Community
  * [Stack Overflow](https://stackoverflow.com/c/etsy/questions/tagged/docsbuilder)
  * [Google Group](https://groups.google.com/g/etsy-api-v2)


#### More
  * [Get help](https://developer.etsy.com/documentation/get-help)
  * [Terms of use](https://www.etsy.com/legal/api)


© 2021 Etsy, Inc.
Copy as Markdown

