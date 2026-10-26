[Skip to main content](https://community.ebay.com/forum/talk-to-your-fellow-developers-57970/topic/api-rate-limit-recommendations-and-api-rate-limit-increases-167243/#skip-target)
[![eBay Community logo](https://res.cloudinary.com/startup-grind/image/upload/fl_sanitize/c_limit,w_640/f_svg/q_auto/v1/gcs/platform-data-ebay/contentbuilder/Logo%20ebay_AbUsNcJ.svg?_a=BAVMn6Gg0)](https://www.ebay.com)
[](https://community.ebay.com/search)
  * [Home](https://community.ebay.com/)
  * [News & Updates](https://community.ebay.com/forum/announcements-57928/)
  * Buying & Selling
    * [Buying](https://community.ebay.com/forum/buying-57914/)
    * [Selling](https://community.ebay.com/forum/selling-57920/)
    * [New to selling on eBay](https://community.ebay.com/forum/new-to-selling-on-ebay-57916/)
    * [Seller Tools](https://community.ebay.com/forum/seller-tools-57919/)
    * [Shipping](https://community.ebay.com/forum/shipping-57923/)
    * [Returns](https://community.ebay.com/forum/returns-57918/)
    * [eBay Advertising](https://community.ebay.com/forum/ebay-advertising-57924/)
    * [Payments](https://community.ebay.com/forum/payments-57917/)
    * [Mobile Apps](https://community.ebay.com/forum/mobile-apps-57915/)
  * Explore Categories
    * eBay Categories
      * [eBay Motors](https://community.ebay.com/forum/motors-58025/)
      * [Electronics](https://community.ebay.com/forum/electronics-58010/)
      * [Collectibles & Art](https://community.ebay.com/forum/collectibles-art-57994/)
      * [Home & Garden](https://community.ebay.com/forum/home-garden-58016/)
      * [Clothing, Shoes & Accessories](https://community.ebay.com/forum/clothing-shoes-accessories-57982/)
      * [Toys & Hobbies](https://community.ebay.com/forum/toys-hobbies-58036/)
      * [Sporting Goods](https://community.ebay.com/forum/sporting-goods-58032/)
      * [Books, Movies & Music](https://community.ebay.com/forum/books-movies-music-57977/)
      * [Health & Beauty](https://community.ebay.com/forum/health-beauty-58015/)
      * [Business & Industrial](https://community.ebay.com/forum/business-industrial-57981/)
      * [Jewelry & Watches](https://community.ebay.com/forum/jewelry-watches-58019/)
      * [Specialty Services](https://community.ebay.com/forum/specialty-services-58031/)
    * Special Categories
      * [eBay Partner Network](https://community.ebay.com/ebay-partner-network/)
      * [Accessibility](https://community.ebay.com/forum/disabled-e-bayers-discussion-group-57946/)
      * [eBay Cafe](https://community.ebay.com/forum/ebay-cafe-57949/)
    * Private Groups
      * [eBay Live](https://community.ebay.com/ebay-live/)
      * [Community Mentors](https://community.ebay.com/community-mentor-lounge/)
    * eBay Developers Program
      * [APIs Feedback, Comments and Suggestions](https://community.ebay.com/forum/apis-feedback-comments-and-suggestions-57951/)
      * [Post Order APIs](https://community.ebay.com/forum/post-order-apis-57952/)
      * [RESTful Buy APIs](https://community.ebay.com/forum/restful-buy-apis-57956/)
      * [RESTful Sell APIs](https://community.ebay.com/forum/restful-sell-apis-57959/)
      * [Token, Messaging, Sandbox Related Issues](https://community.ebay.com/forum/token-messaging-sandbox-related-issues-57963/)
      * [Traditional APIs](https://community.ebay.com/forum/traditional-apis-57964/)
      * [eBay APIs](https://community.ebay.com/forum/ebay-apis-57968/)
    * [Ask a Mentor](https://community.ebay.com/forum/ask-a-mentor-57913/)
  * About
    * [About the Community](https://community.ebay.com/forum/about-the-community-57910/)
    * [Share Community Platform Feedback](https://community.ebay.com/feedback/)
    * [Report eBay Technical Issues](https://community.ebay.com/forum/report-ebay-technical-issues-57911/)
    * [About eBay](https://www.ebayinc.com/company/)
  * Community Events
    * [Events](https://community.ebay.com/events/)
    * [Seller Circle Hosts](https://community.ebay.com/seller-circles-hosts-only/)
    * [Seller Circles](https://community.ebay.com/chapters/)
  * [eBay Help](https://www.ebay.com/help/home)
  * [](https://community.ebay.com/search)


[All Posts](https://community.ebay.com/feed/)[Discussions](https://community.ebay.com/discussion/)[Blogs](https://community.ebay.com/blogs/)[Ideas](https://community.ebay.com/ideas/)[Questions](https://community.ebay.com/questions/)
Categories
[
  * Special CategoriesChevronRightIcon ](https://community.ebay.com/forum/special-categories-57944/)[
  * eBay Developers ProgramChevronRightIcon ](https://community.ebay.com/forum/ebay-developers-program-57950/)[
  * eBay APIsChevronRightIcon ](https://community.ebay.com/forum/ebay-apis-57968/)[
  * Talk to your fellow developersChevronRightIcon ](https://community.ebay.com/forum/talk-to-your-fellow-developers-57970/) 

##### API Rate Limit Recommendations and API Rate Limit Increases
Hello,
I'm in need of some **advice related to API rate limiting** (and I apologize for the length of this post).
I'm in the process of developing an application that performs a lot of searches
for specific items. Some of the specifics of the searches add up to large search queries that would be greater than the 300 character limit for a search, so I've broken them up into multiple searches.
Right now each search is run once an hour for default accounts, and slightly more often for other account types.
That works wonderfully, and for a few users, will remain in the 5000 daily limit on the API.
My problem is when I launch and start trying to scale my application beyond ~200 default users, I will begin going over that 5000 daily limit. The problem is compounded by adding the additional accounts I plan to provide as I was hoping to have a smaller time window on obtaining search results (i.e. every 30 minutes, 5 minutes).
I've tried to minimize the number of searches as much as possible, however I have no other idea how to search for specific results other than filtering on category, item aspect and keywords.
For example, if I was searching for a video games "Donkey Kong Country" and "Super Mario World" I would limit to the games category, with the aspect filter on Platforms to the correct game system and a search string like so: include_this_term ("donkey kong country","super mario world") -ignore_this_term  
  
This search string gets fairly long if the search was for say 50 items -- I have to split it into multiple similar queries.  
  
**My first question: Is there any recommendation on how I can further reduce API search queries?**
**My concern** is I complete my application for growth, but it is denied for one reason or another. I then would have developed an entire platform dependent on searching and can't actually deploy it.
**My second question: Is there anyone I can contact (people, teams, etc.) or anyway I can get pre-approval based on concepts being actively developed and implemented?**
Thanks in advanced for all your help!
![bekindpleaserewind](https://res.cloudinary.com/startup-grind/image/upload/c_fill,w_250,h_250,g_center/c_fill,dpr_2.0,f_auto,g_center,q_auto:good/v1/gcs/platform-data-ebay/avatars/__2cc14b7f.PNG)
bekindpleaserewind
[171](https://feedback.ebay.com/fdbk/feedback_profile/bekindpleaserewind?ssPageName=STRK:ME:UFS)[View listings](https://www.ebay.com/usr/bekindpleaserewind)
Posted 2 years ago·Last reply 2 years ago
2 comments
![](https://res.cloudinary.com/startup-grind/image/upload/c_limit,w_96/f_auto/q_auto/v1/gcs/platform-data-ebay/contentbuilder/avatar_ci86VQ0.png?_a=BAVMn6Gg0)
Comment
Newest
![developer_support@ebay](https://res.cloudinary.com/startup-grind/image/upload/c_fill,w_250,h_250,g_center/c_fill,dpr_2.0,f_auto,g_center,q_auto:good/v1/gcs/platform-data-ebay/avatars/developer_supportebay__1b76cb4b.png)
developer_support@ebay
![eBay Staff](https://res.cloudinary.com/startup-grind/image/upload/c_fill,dpr_2,f_auto,g_center,q_auto:good/v1/gcs/platform-data-ebaysandbox/contentbuilder/ebay-badge_OZSpzSi.png)2 years ago
[0](https://feedback.ebay.com/fdbk/feedback_profile/developer_support@ebay?ssPageName=STRK:ME:UFS)[View listings](https://www.ebay.com/usr/developer_support@ebay)
Hi @bekindpleaserewind @elho4024,
You can submit a "[Application Growth Check](https://developer.ebay.com/grow/application-growth-check)" request to increase the API call limits for your application when your application is close to hit the daily API limit. The application growth check is a free service that the eBay Developers Program provides to its members.
For more details, refer to the "[Request an application growth check](https://developer.ebay.com/api-docs/static/gs_request-an-application-growth.html)" guide. 
![elho4024](https://res.cloudinary.com/startup-grind/image/upload/c_fill,w_250,h_250,g_center/c_fill,dpr_2.0,f_auto,g_center,q_auto:good/v1/gcs/platform-data-ebay/avatars/elho4024__49cd781d.png)
elho4024
·2 years ago
[0](https://feedback.ebay.com/fdbk/feedback_profile/elho4024?ssPageName=STRK:ME:UFS)[View listings](https://www.ebay.com/usr/elho4024)
Consider implementing caching to store frequent search results, reducing API calls. Also, use dynamic rate limits and batch requests where possible to stay within the API limits.
More[Discussions](https://community.ebay.com/discussion/)
API Rate Limit Recommendations and API Rate Limit Increases | Talk to your fellow developers | eBay Community

