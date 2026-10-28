Source: https://dev.epicgames.com/documentation/realityscan-mobile/realityscan-1-5-version?lang=en-US
Fetched: 2026-10-28 (crawl4ai)

  * [RealityScan Mobile Documentation](/documentation/realityscan-mobile/realityscan-documentation)
    * [Release Notes](/documentation/realityscan-mobile/realityscan-release-notes)
      * [RealityScan Mobile 1.8.1](/documentation/realityscan-mobile/realityscan-mobile-1-8-1)
      * [RealityScan Mobile 1.8](/documentation/realityscan-mobile/realityscan-mobile-1-8)
      * [RealityScan Mobile 1.7.1](/documentation/realityscan-mobile/realityscan-mobile-1-7-1)
      * [RealityScan Mobile 1.7](/documentation/realityscan-mobile/realityscan-mobile-1-7-release-notes)
      * [RealityScan Mobile 1.6.2](/documentation/realityscan-mobile/realityscan-mobile-1-6-2-release-notes)
      * [RealityScan Mobile 1.6](/documentation/realityscan-mobile/realityscan-mobile-1-6-release-notes)
      * [RealityScan 1.5.3 (iOS)](/documentation/realityscan-mobile/realityscan-mobile-1-5-3-release-notes-ios-only)
      * [RealityScan Mobile 1.5.2](/documentation/realityscan-mobile/realityscan-mobile-1-5-2-release-notes)
      * [RealityScan Mobile 1.5.1](/documentation/realityscan-mobile/realityscan-mobile-1-5-1)
      * RealityScan Mobile 1.5
      * [RealityScan Mobile 1.4](/documentation/realityscan-mobile/realityscan-1-4-version)
      * [RealityScan Mobile 1.3](/documentation/realityscan-mobile/realityscan-1-3-version)
      * [RealityScan Mobile 1.2](/documentation/realityscan-mobile/realityscan-1-2-version)
    * [System Requirements and Setup](/documentation/realityscan-mobile/RealityScan-System-Requirements-and-Installation)
    * [Navigate the User Interface](/documentation/realityscan-mobile/Navigate-the-RealityScan-User-Interface)
    * [Step-by-Step Guide](/documentation/realityscan-mobile/realityscan-step-by-step-guide)
    * [Useful Information](/documentation/realityscan-mobile/RealityScan-Useful-Information)


Table of Contents
  1. ![Epic Games](https://edc-cdn.net/assets/images/logo-epic.svg)[Developer](/)
  2. [Documentation](/documentation/ "Documentation")
  3. RealityScan Mobile
     * [Unreal Engine](/documentation/unreal-engine)
     * [Fortnite](/documentation/fortnite)
     * [Twinmotion](/documentation/twinmotion)
     * [MetaHuman](/documentation/metahuman)
     * [RealityScan](/documentation/realityscan)
     * [RealityScan Mobile](/documentation/realityscan-mobile)
     * [Fab](/documentation/fab)
  4. [RealityScan Mobile Documentation](/documentation/realityscan-mobile/realityscan-documentation "RealityScan Mobile Documentation")
  5. [Release Notes](/documentation/realityscan-mobile/realityscan-release-notes "Release Notes")
  6. RealityScan Mobile 1.5


# RealityScan Mobile 1.5
RealityScan 1.5 Release Notes 
On this page
###  What's New 
  * Download your 3D files to your device
    * Download your processed 3D models to save locally on your device or share with others. For iOS devices, downloads are in OBJ format. For Android devices, downloads are in GLB format. Note that projects created in previous versions will need to be processed again before you can visualize and download them in the app.
  * Optional sharing on Sketchfab
    * Sharing your scans on Sketchfab is now optional. After processing your model, tap the “Share on Sketchfab” button if you want to showcase your work to the community.
  * Faster and more efficient cropping
    * Cropping now happens on your device instead of on the server, making it almost instantaneous. Plus, you can now crop your models using a cylindrical volume, perfect for round objects like vases and tables.
  * Redesigned project list
    * The project list has a fresh new look! Not only is it more visually appealing, but you can now see the size of each project and filter the list for easier navigation.
  * Seamless switch between automatic and manual capture
  * Image count in gallery
    * You can now see how many images you’ve taken while you’re in your project’s image gallery.
  * Photo export from gallery
    * You can now export your projects’ photos from the gallery. Just tap the export button to export all images, or select specific images first.
  * Scanning quick start guide
    * Achieve better scans by following the advice in the new quick start guide. To access it, tap the ? icon shown on the top of the screen while capturing.
  * Changes to the application
    * To streamline the scanning workflow, the preview mesh has been removed. Previously, this step caused confusion as it wasn’t an accurate display of the model and delays due to internet connection issues and model complexity. Now, simply take your pictures, optionally set the scan area, and hit “Process Now” to process and download your model or upload it to Sketchfab.


###  Bugs Fixed 
####  Android 
  * Fixed Image capture failure on Xiaomi phones.
  * Fixed an issue where red and blue channels were inverted on some Xiaomi phones.
  * Fixed an issue where “Uploading” status was shown instead of “Processing” after pressing Process and Share.
  * Fixed an issue where the Process and Share button became unresponsive after denying notifications.
  * Fixed an issue where image count changed from 1 back to 0.iOS
  * Fixed an issue where photos did not upload after leaving the device idle for a while.
  * Fixed an inconsistency between crop UI, shading, and result.
  * Fixed an issue where the point cloud moved while photos were being analyzed in crop mode.
  * Fixed an issue where the crop box and point cloud randomly moved when adjusting the crop box and rotating the area.
  * Fixed Unexpected state error - Finalization failed - when switching from offline mode and sending for processing.


###  Known Bugs 
####  iOS 
  * Some projects remain stuck while submitting to Sketchfab.Workaround: Restart the app and submit to Sketchfab again.
  * Back button in the Crop 3D model screen applies the crop to the model.
  * Cylinder crop is not persistent in the app after uploading to Sketchfab.
  * Selection options in image gallery not appearing.


* * *
Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=realityscan)
Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/realityscan/learning)
On this page
  * [ What's New ](/documentation/realityscan-mobile/realityscan-1-5-version?lang=en-US#what'snew)
  * [ Bugs Fixed ](/documentation/realityscan-mobile/realityscan-1-5-version?lang=en-US#bugsfixed)
  * [ Android ](/documentation/realityscan-mobile/realityscan-1-5-version?lang=en-US#android)
  * [ Known Bugs ](/documentation/realityscan-mobile/realityscan-1-5-version?lang=en-US#knownbugs)
  * [ iOS ](/documentation/realityscan-mobile/realityscan-1-5-version?lang=en-US#ios)



