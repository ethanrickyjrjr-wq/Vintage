Source: https://forums.unrealengine.com/t/realityscan-mobile-1-8-release-notes/2676487
Fetched: 2026-10-28 (crawl4ai)

[ Skip to main content ](https://forums.unrealengine.com/t/realityscan-mobile-1-8-release-notes/2676487#main-container)
​ 
[ ![Epic Developer Community Forums](https://d3kjluh73b9h9o.cloudfront.net/original/4X/7/1/3/713c9d3f58553f0de89543d76a8a3a2779dc9fa4.png) ](https://forums.unrealengine.com/)
  * [ Developer ](https://dev.epicgames.com)
  * [ Forum ](https://forums.unrealengine.com/t/realityscan-mobile-1-8-release-notes/2676487)
  * [ RealityScan ](https://forums.unrealengine.com/t/realityscan-mobile-1-8-release-notes/2676487)
​ 
  * [ ... ](https://forums.unrealengine.com/c/general/announcements/49)
  * [ Release Notes ](https://forums.unrealengine.com/c/general/announcements/release-notes/206)
  * [ RealityScan Mobile 1.8 Release Notes ](https://forums.unrealengine.com/t/realityscan-mobile-1-8-release-notes/2676487)


Sign In
  * ​ 
  * ​ 


All outgoing email has been globally disabled by an administrator. No email notifications of any kind will be sent.
#  [ RealityScan Mobile 1.8 Release Notes ](https://forums.unrealengine.com/t/realityscan-mobile-1-8-release-notes/2676487)
[General](https://forums.unrealengine.com/c/general/10)[Announcements](https://forums.unrealengine.com/c/general/announcements/49)[Release Notes](https://forums.unrealengine.com/c/general/announcements/release-notes/206)
  * [ realityscan](https://forums.unrealengine.com/tag/realityscan/11534)
  * [ realityscan-mobile](https://forums.unrealengine.com/tag/realityscan-mobile/11535)


You have selected **0** posts.
[ select all ](https://forums.unrealengine.com/t/realityscan-mobile-1-8-release-notes/2676487)
[ cancel selecting ](https://forums.unrealengine.com/t/realityscan-mobile-1-8-release-notes/2676487)
[ Nov 2025  ](https://forums.unrealengine.com/t/realityscan-mobile-1-8-release-notes/2676487/1 "Jump to the first post")
1 / 1 
Nov 2025 
[ Nov 2025 ](https://forums.unrealengine.com/t/realityscan-mobile-1-8-release-notes/2676487/1)
##  post by Piotr_Ignatowicz on Nov 19, 2025 
[ ![](https://d3kjluh73b9h9o.cloudfront.net/original/4X/2/8/5/28502927f1d97ba1051b3b47ccfe17233bf41ef0.png) ](https://dev.epicgames.com/community/api/user_profiles/tab-redirect/about?discourse_username=Piotr_Ignatowicz)
[ Piotr Ignatowicz ](https://dev.epicgames.com/community/api/user_profiles/tab-redirect/about?discourse_username=Piotr_Ignatowicz) [ @Piotr_Ignatowicz ](https://dev.epicgames.com/community/api/user_profiles/tab-redirect/about?discourse_username=Piotr_Ignatowicz)
25 
posts 
0 
answers 
[ Piotr Ignatowicz  ](https://dev.epicgames.com/community/api/user_profiles/tab-redirect/about?discourse_username=Piotr_Ignatowicz) [ Staff ](https://forums.unrealengine.com/g/Epic_Games_Inc)
[ Nov 2025 ](https://forums.unrealengine.com/t/realityscan-mobile-1-8-release-notes/2676487 "Post date")
RealityScan 1.8 is now available.
  * Android version: [Link](https://play.google.com/store/apps/details?id=com.epicgames.realityscan&hl=en)
  * iOS version: [Link ](https://apps.apple.com/us/app/realityscan-3d-scanning-app/id1584832280)


##  [](https://forums.unrealengine.com/t/realityscan-mobile-1-8-release-notes/2676487#p-4992978-whats-new-1)What’s New
  * **New shooting modes**
    * You now have three distinct shooting modes to match your scanning needs: 
      * **AR Guidance** – Uses Augmented Reality to display a live quality point cloud over your subject, along with real-time visualization of your captured photo positions, allowing you to check where more pictures are needed as you scan.
      * **Object Mode** – Features advanced camera controls with **automatic background removal** , allowing you to flip, rotate, and move your object for a complete scan of all sides of an object. Make sure that the object doesn’t change shape when moved.
      * **Standard Mode** – Offers the same advanced camera controls as Object Mode, but without background removal. Suitable if you want to scan an object and its environment together.
  * **New viewport controls**
    * Take full control of your 3D view with the new interactive view cube. Easily rotate your model from any angle, or tap one of the cube’s faces to instantly switch to a predefined orthographic view.
  * **Mesh Clean Up tools:**
    * Gain more control over your generated mesh with new filtering options. Use the lasso and rectangle selection tools to quickly select and remove unwanted areas of your model.
  * **Focus peaking:**
    * Introducing focus peaking — a color overlay/highlighter that visually indicates which parts of the image are in sharp focus.
  * **Capture Interval Timer:**
    * Allows you to automatically capture photos at pre-set time intervals, designed to be used when scanning with a turntable or when the phone is fixed on a tripod.
  * **Water tight mesh option:**
    * When processing your scan, you can choose whether to generate a water-tight mesh (which is useful, for example, for 3D printing), or a non-water tight mesh (which might have less artifacts, especially if you didn’t scan with masks).
  * **Continuous light mode:**
    * Ability to constantly turn your flash light on or off, useful for scanning in darker environments. You can choose to use this mode instead of using the flash.


##  [](https://forums.unrealengine.com/t/realityscan-mobile-1-8-release-notes/2676487#p-4992978-bugs-fixed-2)Bugs Fixed
Android
  * Poor image quality & large HEIF file size for scans made in AR mode
  * Wrong photo orientation on Rog 6D Ultimate device.


iOS
  * Message Flash ON/OFF is missing.
  * Projects are stuck in Processing status.
  * User gets signed out of the app when trying to scan.
  * First message in CC mode is for Autocapture.
  * Share to Sketchfab fails when minimizing the app (new).


##  [](https://forums.unrealengine.com/t/realityscan-mobile-1-8-release-notes/2676487#p-4992978-known-bugs-3)Known Bugs
Android
  * Reprocessed model may get incorrectly cropped


iOS
  * Newly processed projects sometimes remain stuck at “Processing…”
  * Top<->Back transition is not smooth.
  * RAW image files don’t match JPEG files
  * Black camera view on clean install


  

​ 
​  ​ 
1.7k views  2 links 
Report Reply
  

###  New & Unread Topics   
Topic list, column headers with buttons are sortable.  
|  Topic   |  Replies   |  Views   |  Activity   | Votes  |  
| --- | --- | --- | --- | --- |  
|  [RealityScan Mobile 1.8.1 Release Notes](https://forums.unrealengine.com/t/realityscan-mobile-1-8-1-release-notes/2681163) [Release Notes](https://forums.unrealengine.com/c/general/announcements/release-notes/206)
  * [ realityscan](https://forums.unrealengine.com/tag/realityscan/11534)
  * [ realityscan-mobile](https://forums.unrealengine.com/tag/realityscan-mobile/11535)

[ RealityScan 1.8.1 is now available. Android version: Link iOS version: Link Bugs Fixed Android Tutorial video crashes the app in offline mode Reality Scan Crashing on start Delay in updating image count in image ga… read more ](https://forums.unrealengine.com/t/realityscan-mobile-1-8-1-release-notes/2681163)  |  [ 1 ](https://forums.unrealengine.com/t/realityscan-mobile-1-8-1-release-notes/2681163/1)  |  1.3k  |  [Jun 25](https://forums.unrealengine.com/t/realityscan-mobile-1-8-1-release-notes/2681163/2)  |  /10   |  
|  [RealityScan Mobile 1.9 Release Notes](https://forums.unrealengine.com/t/realityscan-mobile-1-9-release-notes/2746621) [Release Notes](https://forums.unrealengine.com/c/general/announcements/release-notes/206)
  * [ realityscan](https://forums.unrealengine.com/tag/realityscan/11534)
  * [ realityscan-mobile](https://forums.unrealengine.com/tag/realityscan-mobile/11535)

[ RealityScan 1.9 is now available. Android version: Link iOS version: Link What’s New Capture Improvements: Users can now delete photos at any time, not just while capturing, we added the option to “Take More Pict… read more ](https://forums.unrealengine.com/t/realityscan-mobile-1-9-release-notes/2746621)  |  [ 0 ](https://forums.unrealengine.com/t/realityscan-mobile-1-9-release-notes/2746621/1)  |  265  |  [Aug 26](https://forums.unrealengine.com/t/realityscan-mobile-1-9-release-notes/2746621/1)  |  /10   |  
|  [How to change clipping plane in asset viewport? NOT A SCENE VIEWPORT.](https://forums.unrealengine.com/t/how-to-change-clipping-plane-in-asset-viewport-not-a-scene-viewport/2717919) [Getting Started & Setup](https://forums.unrealengine.com/c/development-discussion/getting-started/150)
  * [ unreal-engine](https://forums.unrealengine.com/tag/unreal-engine/705)

[ I can’t find how to change near clipping plane for asset viewports. Not the scene viewport. How to change clipping distance in skeletal mesh viewport? No, changing near clipping plane in project settings doesn’t help. Y… read more ](https://forums.unrealengine.com/t/how-to-change-clipping-plane-in-asset-viewport-not-a-scene-viewport/2717919)  |  [ 0 ](https://forums.unrealengine.com/t/how-to-change-clipping-plane-in-asset-viewport-not-a-scene-viewport/2717919/1)  |  73  |  [Apr 25](https://forums.unrealengine.com/t/how-to-change-clipping-plane-in-asset-viewport-not-a-scene-viewport/2717919/1)  |  /10   |  
|  [mengzhishanghun - SimpleLevelSeqSmooth ](https://forums.unrealengine.com/t/mengzhishanghun-simplelevelseqsmooth/2740397) [Product Discussion](https://forums.unrealengine.com/c/distribution/product-discussion/237)
  * [ fab](https://forums.unrealengine.com/tag/fab/11497)

[ # Simple Level Sequence Smooth ## Documentation https://github.com/MZSH-UEPlugins/UEPluginDocs/blob/main/SimpleLevelSeqSmooth/README.md --- Level sequence data filtering plugin with 12 smoothing algorithms: Movin… read more ](https://forums.unrealengine.com/t/mengzhishanghun-simplelevelseqsmooth/2740397)  |  [ 0 ](https://forums.unrealengine.com/t/mengzhishanghun-simplelevelseqsmooth/2740397/1)  |  27  |  [Aug 3](https://forums.unrealengine.com/t/mengzhishanghun-simplelevelseqsmooth/2740397/1)  |  /10   |  
|  [ronlagasca - Low Poly Medieval Fishing Net Rack - Stylized ](https://forums.unrealengine.com/t/ronlagasca-low-poly-medieval-fishing-net-rack-stylized/2834619) [Product Discussion](https://forums.unrealengine.com/c/distribution/product-discussion/237)
  * [ fab](https://forums.unrealengine.com/tag/fab/11497)

[ This stylized low poly medieval fishing net rack adds a practical fishing prop to riverside settlements, fishing villages, docks, and waterfront environments. The rustic wooden rack with rolled fishing nets helps create … read more ](https://forums.unrealengine.com/t/ronlagasca-low-poly-medieval-fishing-net-rack-stylized/2834619)  |  [ 0 ](https://forums.unrealengine.com/t/ronlagasca-low-poly-medieval-fishing-net-rack-stylized/2834619/1)  |  36  |  [Sep 27](https://forums.unrealengine.com/t/ronlagasca-low-poly-medieval-fishing-net-rack-stylized/2834619/1)  |  /10   |  
###  Want to read more? Browse other topics in [Release Notes](https://forums.unrealengine.com/c/general/announcements/release-notes/206) or [view latest topics](https://forums.unrealengine.com/latest). 

