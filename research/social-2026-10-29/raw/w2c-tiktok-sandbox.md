[![TikTok for Developers](https://sf16-sg.tiktokcdn.com/obj/eden-sg/wv_k4aa/ljhwZthlaukjlkulzlp/doc_station/tt4d_logo_dark.ac59d2631b2b.svg)](https://developers.tiktok.com/)
Products[Docs](https://developers.tiktok.com/docs)[Support](https://developers.tiktok.com/portal/support?origin_site=doc-station)[Blog](https://developers.tiktok.com/blogs)
Get started
# Developer Docs
Introduction/.../Add a Sandbox
ENSearch⌘ K
Introduction
  * [Welcome](https://developers.tiktok.com/docs/en/welcome)
  * [Get Started](https://developers.tiktok.com/docs/en/get-started)
  * [Account Management](https://developers.tiktok.com/docs/en/working-with-organizations)
  * [App Management](https://developers.tiktok.com/docs/en/getting-started-create-an-app)
    * [Register Your App](https://developers.tiktok.com/docs/en/getting-started-create-an-app)
    * [Add a Sandbox](https://developers.tiktok.com/docs/en/add-a-sandbox)
    * [App Review FAQ](https://developers.tiktok.com/docs/en/getting-started-faq)
  * [Our Guidelines](https://developers.tiktok.com/docs/en/app-review-guidelines)
  * [Integration Essentials](https://developers.tiktok.com/docs/en/mobile-sdk-ios-quickstart)
  * [TikTok Minis](https://developers.tiktok.com/docs/en/perpare-your-developer-account)
  * [Monetization](https://developers.tiktok.com/docs/en/monetization-overview)
  * [Scopes](https://developers.tiktok.com/docs/en/scopes-overview)
  * [Legacy Products](https://developers.tiktok.com/docs/en/tiktok-api-v2-introduction)
  * [Changelog](https://developers.tiktok.com/docs/en/changelog)


[Introduction](https://developers.tiktok.com/docs/en/welcome)/[App Management](https://developers.tiktok.com/docs/en/getting-started-create-an-app)/Add a SandboxIntroduction/App Management/Add a SandboxLast updated August 4, 2026
  * [Prerequisites](https://developers.tiktok.com/docs/en/add-a-sandbox#prerequisites_)
  * [Create a Sandbox](https://developers.tiktok.com/docs/en/add-a-sandbox#create_a_sandbox)
  * [Manage target users](https://developers.tiktok.com/docs/en/add-a-sandbox#manage_target_users_)
    * [Authorize target users with Login Kit](https://developers.tiktok.com/docs/en/add-a-sandbox#authorize_target_users_with_login_kit)
  * [Import your Sandbox configuration](https://developers.tiktok.com/docs/en/add-a-sandbox#import_your_sandbox_configuration_)


On this page
# Add a Sandbox
**Sandbox** mode is a restricted environment that allows you to try out integrations without having to submit your app for review. You can create multiple sandboxes for your app to experiment with different configurations without compromising the live version of your app. You can create up to 5 sandboxes. 
##  [#](https://developers.tiktok.com/docs/en/add-a-sandbox#prerequisites_)Prerequisites 
Before registering your app, do the following:
  1. Create a TikTok developer account from [our signup page](https://developers.tiktok.com/signup) using your email.
  2. Create or join an [organization](https://developers.tiktok.com/docs/en/working-with-organizations) representing the owning group of the app. This step is highly recommended but not required.


You will also need access to a URL decoder to [authorize target users](https://developers.tiktok.com/docs/en/add-a-sandbox#authorize_target_users_with_login_kit). 
##  [#](https://developers.tiktok.com/docs/en/add-a-sandbox#create_a_sandbox)Create a Sandbox
This workflow demonstrates how to create your first sandbox. 
  1. Go to the **Manage apps** page, then select an app or **Connect an app** if you don't have one yet.
  2. On the app page, switch the toggle next to your app's name to **Sandbox**. 


![](https://sf16-sg.tiktokcdn.com/obj/tiktok-open-platform-sg/ttop_doc_images/edcb9ea5ba07e6136636cb2fdb1ec2fe)
  1. Click the **Create Sandbox** button, then enter a name. You can choose to clone an existing configuration from your app's production versions or another sandbox. 


![](https://sf16-sg.tiktokcdn.com/obj/tiktok-open-platform-sg/ttop_doc_images/1da64668f04efd425e7d3f86c834b50d)
  1. Click **Confirm** to create the sandbox. 
  2. Configure the sandbox as desired by editing **App details** and adding products. 


Note: Sandbox mode does not offer access to Content Posting API for public videos or Data Portability API. 
  1. Click **Apply changes** to save changes and make your configuration take effect. 


To create another sandbox, click the [**+**] button (**Create Sandbox**) in the left navigation panel. 
![](https://sf16-sg.tiktokcdn.com/obj/tiktok-open-platform-sg/ttop_doc_images/bca5622c079cf61412f2773cb46961fe)
##  [#](https://developers.tiktok.com/docs/en/add-a-sandbox#manage_target_users_)Manage target users 
Adding target users to a sandbox allows them to try out your sandbox configurations. To add a TikTok account that you own as a target user, you must provide its login credentials. You can add up to 10 accounts. 
![](https://sf16-sg.tiktokcdn.com/obj/tiktok-open-platform-sg/ttop_doc_images/b96946aa5493d8c17de62e2f25d51b5d)
  1. Go to **Sandbox settings** on the app page. 
  2. Under **Target users** , click **Add account**. You will be redirected to log in to a TikTok account. 
  3. Log in to the TikTok account and agree to the TikTok Developer Terms of Service. 


Your target users will be displayed on your app page after they have been added. Results may take up to an hour to show after you refresh the page.
![](https://sf16-sg.tiktokcdn.com/obj/tiktok-open-platform-sg/ttop_doc_images/10669c5c932bae02c680c6d1229a7aed)
###  [#](https://developers.tiktok.com/docs/en/add-a-sandbox#authorize_target_users_with_login_kit)Authorize target users with Login Kit
After you add target users, you may authorize them if you want to use Login Kit and the other products dependent on it. Authorization workflows for Web, Desktop, iOS, and Android are available in the [Login Kit documentation](https://developers.tiktok.com/docs/en/login-kit-overview). 
##  [#](https://developers.tiktok.com/docs/en/add-a-sandbox#import_your_sandbox_configuration_)Import your Sandbox configuration 
You can import a sandbox's configuration to a **Draft** of your app in production. Doing so will overwrite the draft's existing configuration with the chosen sandbox configuration. 
![](https://sf16-sg.tiktokcdn.com/obj/tiktok-open-platform-sg/ttop_doc_images/55d7d912f013e1a9242d7df9ebb6af77)
Note: You can only import a sandbox configuration to a **Draft** in **Production** mode. 
  1. On the app page, switch the toggle next to your app's name to **Production**. 
  2. Click **Draft** in the left navigation panel. 
  3. Click **Import** , then select the sandbox you want to import from. 


If you have a version of the app that has been approved and is live, you can revert back to that configuration by clicking **Revert to Live version** in the**Import** dropdown.
When you are ready to [submit your app](https://developers.tiktok.com/docs/en/getting-started-create-an-app#submit_your_app_for_review), make sure that it follows our [app review guidelines](https://developers.tiktok.com/docs/en/app-review-guidelines). 
For further inquiries or assistance, contact us through our [Support form](https://developers.tiktok.com/support?topic=sandbox). 
  

On this page
  * [Prerequisites](https://developers.tiktok.com/docs/en/add-a-sandbox#prerequisites_)
  * [Create a Sandbox](https://developers.tiktok.com/docs/en/add-a-sandbox#create_a_sandbox)
  * [Manage target users](https://developers.tiktok.com/docs/en/add-a-sandbox#manage_target_users_)
    * [Authorize target users with Login Kit](https://developers.tiktok.com/docs/en/add-a-sandbox#authorize_target_users_with_login_kit)
  * [Import your Sandbox configuration](https://developers.tiktok.com/docs/en/add-a-sandbox#import_your_sandbox_configuration_)


Prerequisites
[![TikTok for Developers](https://sf16-sg.tiktokcdn.com/obj/eden-sg/wv_k4aa/ljhwZthlaukjlkulzlp/doc_station/tt4d_logo_dark.ac59d2631b2b.svg)](https://developers.tiktok.com/)
Products
  * [Share Kit](https://developers.tiktok.com/products/share-kit)
  * [Login Kit](https://developers.tiktok.com/products/login-kit)
  * [Content Posting API](https://developers.tiktok.com/products/content-posting-api)
  * [Research API](https://developers.tiktok.com/products/research-api)
  * [Display API](https://developers.tiktok.com/docs/en/display-api-get-started)


  * [Embed Videos](https://developers.tiktok.com/docs/en/embed-videos)
  * [Data Portability API](https://developers.tiktok.com/products/data-portability-api)
  * [Green Screen Kit](https://developers.tiktok.com/products/share-kit#green-screen)
  * [Commercial Content API](https://developers.tiktok.com/products/commercial-content-api)


Other platforms
  * [TikTok Embeds](https://www.tiktok.com/embed "TikTok Embeds")
  * [TikTok for Business](https://www.tiktok.com/business "TikTok for Business")
  * [Advertise on TikTok](https://www.tiktok.com/business/&attr_source=tt_official_site&attr_medium=tt_official_site_guidance "Advertise on TikTok")
  * [TikTok Creative Center](https://ads.tiktok.com/business/creativecenter/ "TikTok Creative Center")
  * [TikTok.com](https://www.tiktok.com "TikTok")
  * [Policy Center](https://developers.tiktok.com/policy/en "Policy Center")


Company
  * [About TikTok](https://www.tiktok.com/about "About TikTok")
  * [Newsroom](https://newsroom.tiktok.com "TikTok Newsroom")
  * [Contact](https://www.tiktok.com/about/contact "Contact TikTok")
  * [Careers](https://careers.tiktok.com "TikTok Careers page")
  * [ByteDance](https://www.bytedance.com "About ByteDance")
  * [Transparency Center](https://www.tiktok.com/transparency "TikTok")


© 2026 TikTok[Terms of Service](https://www.tiktok.com/legal/page/global/tik-tok-developer-terms-of-service/en)[Privacy Policy](https://www.tiktok.com/legal/page/global/partner-privacy-policy/en)[Resources & Legal](https://developers.tiktok.com/docs/en/add-a-sandbox#site-footer)
![](https://sf16-va.tiktokcdn.com/obj/eden-va2/61eh7vboznuhog/root/ai-bot/ai-bot.png)

