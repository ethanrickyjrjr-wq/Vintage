[Skip to main content](https://docs.immich.app/features/mobile-app/#__docusaurus_skipToContent_fallback)
[ ![Immich Logo](https://docs.immich.app/img/immich-logo-inline-light.png)![Immich Logo](https://docs.immich.app/img/immich-logo-inline-dark.png) ](https://docs.immich.app/)
[Home](https://immich.app/)[GitHub](https://github.com/immich-app/immich)
[Buy Immich](https://buy.immich.app)
  * [Overview](https://docs.immich.app/overview/quick-start)
  * [Install](https://docs.immich.app/install/requirements)
  * [Features](https://docs.immich.app/features/mobile-backup)
    * [Mobile Backup](https://docs.immich.app/features/mobile-backup)
    * [Chromecast support](https://docs.immich.app/features/casting)
    * [The Immich CLI](https://docs.immich.app/features/command-line-interface)
    * [Duplicates Utility](https://docs.immich.app/features/duplicates-utility)
    * [Editing](https://docs.immich.app/features/editing)
    * [Facial Recognition](https://docs.immich.app/features/facial-recognition)
    * [Folder View](https://docs.immich.app/features/folder-view)
    * [Hardware Transcoding](https://docs.immich.app/features/hardware-transcoding)
    * [External Libraries](https://docs.immich.app/features/libraries)
    * [Locked Folder](https://docs.immich.app/features/locked-folder)
    * [Hardware-Accelerated Machine Learning](https://docs.immich.app/features/ml-hardware-acceleration)
    * [Mobile App](https://docs.immich.app/features/mobile-app)
    * [Monitoring](https://docs.immich.app/features/monitoring)
    * [Partner Sharing](https://docs.immich.app/features/partner-sharing)
    * [Reverse Geocoding](https://docs.immich.app/features/reverse-geocoding)
    * [Searching](https://docs.immich.app/features/searching)
    * [Sharing](https://docs.immich.app/features/sharing)
    * [Supported Media Formats](https://docs.immich.app/features/supported-formats)
    * [Tags](https://docs.immich.app/features/tags)
    * [User Settings](https://docs.immich.app/features/user-settings)
    * [XMP Sidecars](https://docs.immich.app/features/xmp-sidecars)
  * [Administration](https://docs.immich.app/administration/backup-and-restore)
  * [Developer](https://docs.immich.app/developer/architecture)
  * [Guides](https://docs.immich.app/guides/better-facial-clusters)
  * [FAQ](https://docs.immich.app/FAQ)
  * [API](https://docs.immich.app/api)


  * [](https://docs.immich.app/)
  * Features
  * Mobile App


On this page
# Mobile App
## Download[​](https://docs.immich.app/features/mobile-app/#download "Direct link to Download")
The mobile app can be downloaded from the following places:
  * [Apple App Store](https://apps.apple.com/us/app/immich/id1613945652)
  * [Google Play Store](https://play.google.com/store/apps/details?id=app.alextran.immich)
  * [GitHub Releases (APK)](https://github.com/immich-app/immich/releases)
  * Obtainium: You can get your Obtainium config link from the [Utilities page of your Immich server](https://my.immich.app/utilities).
  * [FUTO F-Droid](https://get.immich.app/fdroid)


Android verification
Below are the SHA-256 fingerprints for the certificates signing the android applications.
  * Google Play releases: `5A:22:C1:83:47:54:05:F5:49:C4:EB:9F:B2:6C:2E:93:A3:EF:9C:57:66:15:0A:7A:F3:8C:8D:3F:E5:15:CC:D6`
  * GitHub releases: `86:C5:C4:55:DF:AF:49:85:92:3A:8F:35:AD:B3:1D:0C:9E:0B:95:7D:7F:94:C2:D2:AF:6A:24:38:AA:96:00:20`
  * F-Droid releases: `FA:8B:43:95:F4:A6:47:71:A0:53:D1:C7:57:73:5F:A2:30:13:74:F5:3D:58:0D:D1:75:AA:F7:A1:35:72:9C:BF`


## Login[​](https://docs.immich.app/features/mobile-app/#login "Direct link to Login")
Login to the mobile app with the server endpoint URL at `http://<machine-ip-address>:2283`
![](https://docs.immich.app/assets/images/sign-in-phone-92be8a8eab0f72d121e8b62e6f69df17.webp)
## Backup[​](https://docs.immich.app/features/mobile-app/#backup "Direct link to Backup")
  1. Navigate to the backup screen by clicking on the cloud icon in the top right corner of the screen.

![](https://docs.immich.app/features/mobile-app/)
  1. You can select which album(s) you want to back up to the Immich server from the backup screen.

![](https://docs.immich.app/assets/images/album-selection-6073c429378c94a70f6929262d09f807.webp)
  1. Scroll down to the bottom and press "**Enable Backup** " to start the backup process. This will upload all the assets in the selected albums.


info
You can read more about backup options [here](https://docs.immich.app/features/mobile-backup).
## Sync only selected photos[​](https://docs.immich.app/features/mobile-app/#sync-only-selected-photos "Direct link to Sync only selected photos")
If you have a large number of photos on the device, and you would prefer not to backup all the photos, then it might be prudent to only backup selected photos from device to the Immich server.
First, you need to enable the Storage Indicator in your app's settings. Navigate to **Settings - > Photo Grid** and enable **`Show Storage indicator on asset tiles`**; this makes it easy to distinguish local-only assets and synced assets.
note
This will enable a small cloud icon on the bottom right corner of the asset tile, indicating that the asset is synced to the server:
  1. - Local-only asset; not synced to the server
  2. - Asset is synced to the server


Now make sure that the local album is selected in the backup screen (steps 1-2 above). You can find these albums listed in **Library - > On this device**. To selectively upload photos from these albums, simply select the local-only photos and tap on the `Upload` button in the dynamic bottom menu.
![](https://docs.immich.app/assets/images/mobile-upload-selected-photos-369db69b80fcf389bc06c483851f0be9.webp)
## Free Up Space[​](https://docs.immich.app/features/mobile-app/#free-up-space "Direct link to Free Up Space")
**Free Up Space** allows you to remove local media files from your device that have already been successfully backed up to your Immich server (and are not in Immich trash). This helps reclaim storage on your mobile device without losing your memories.
### How it works[​](https://docs.immich.app/features/mobile-app/#how-it-works "Direct link to How it works")
![](https://docs.immich.app/assets/images/free-up-space-458df20288634d366eb7626fbb892a17.webp)
  1. **Configuration:**
     * **Cutoff date:** Free Up Space will only look for photos and videos **on or before** this date. Photos removed from the device don't show up in other (messaging) apps and have to be shared from Immich in order to send them.
     * **Keep favorites:** This works the same way `Keep albums` does. By default, favorited assets are preserved on your device.
     * **Keep albums:** Hold all photos and videos in the selected albums on your device, regardless of other settings. By default, `WhatsApp` [related albums](https://docs.immich.app/features/mobile-app/#external-app-dependencies) are selected to be kept on the device. Assets not already on the device will not be re-downloaded.
     * **Keep on device:** You can choose to restrict removal to `Always keep` **All photos** or **All videos** , regardless of other settings. This setting can hamper freeing up space significantly — with 80 GB of videos and 40 GB photos, selecting `Always keep photos` retains thousands of photos on your device.
  2. **Scan & Review:** Before any files are removed, you are presented with a review screen to verify which items will be deleted and how much storage is reclamable.
  3. **Deletion:** Confirmed items are moved to your device's native Trash/Recycle Bin. For large queues, Immich processes deletion in batches for stability (`2000` assets per batch on Android, `10000` per batch on iOS).


reclaim storage
To use the reclaimed space right away, you must empty the system/gallery trash manually outside of Immich.
Provided the server is healthy and [backed up](https://docs.immich.app/administration/backup-and-restore), assets removed by Free Up Space can always be accessed in the Immich app.
### iCloud Photos[​](https://docs.immich.app/features/mobile-app/#icloud-photos "Direct link to iCloud Photos")
If you use **iCloud Photos** alongside Immich, it is vital to understand how deletion affects your data. After using **Free Up Space** , the photo will be stored **only** on your Immich server (and your phone's "Recently Deleted" folder for 30 days).
Assets that are part of an **iCloud Shared Album** are automatically excluded from the cleanup scan because iCloud does not allow removing the items in Shared Album from the device.
iCloud & Backups
If, in addition to Immich, you rely on iCloud as a secondary backup (as part of your [3-2-1](https://www.backblaze.com/blog/the-3-2-1-backup-strategy/) backup strategy), you should instead use `Optimize iPhone Storage` in [iCloud Photos](https://support.apple.com/en-us/105061).
iCloud utilizes a two-way sync; this means deleting a photo, or using Free Up Space from your iPhone will **also delete it from iCloud** and all other devices (Mac, iPad) where you're signed in with the same Apple Account. See [Apple Support](https://support.apple.com/en-us/108922#iCloud_photo_library) for more info.
### External App Dependencies (WhatsApp, etc.)[​](https://docs.immich.app/features/mobile-app/#external-app-dependencies "Direct link to External App Dependencies \(WhatsApp, etc.\)")
Android applications like **WhatsApp** rely on local files to display media in chat history.
If Immich backs up your WhatsApp folder and you run **Free Up Space** , the local copies of these images will be deleted. Consequently, **media in your WhatsApp chats will appear blurry or missing.** You will only be able to view these photos inside the Immich app; they will no longer be visible within the WhatsApp interface.
**Recommendation:** If keeping chat history intact is important, exclude WhatsApp with `Keep albums` in Free Up Space and review the deletion list carefully. You have to enable [Album Sync](https://docs.immich.app/features/mobile-app/#album-sync) for WhatsApp to show up in the list. Alternatively, don't [back up](https://docs.immich.app/features/mobile-app/#backup) WhatsApp with Immich.
## Album Sync[​](https://docs.immich.app/features/mobile-app/#album-sync "Direct link to Album Sync")
You can sync or mirror an album from your phone to the Immich server on your account. For example, if you select Recents, Camera and Videos album for backup, the corresponding album with the same name will be created on the server. Once the assets from those albums are uploaded, they will be put into the target albums automatically.
### Album Synchronization Highlights[​](https://docs.immich.app/features/mobile-app/#album-synchronization-highlights "Direct link to Album Synchronization Highlights")
  * **One-Way Sync:** Synchronization is one-way, from the device to the server.
  * **Name Matching:** If an album on the server has the same name as the album on the device, images from the device will be merged with the existing images in the server album.
  * **Shared Albums:** If the matching album on the server is shared, the new photos merged into the album will also be shared.
  * **Album Structure:** When an album is created for the first time, its structure is based on the initial state. Future updates made on the phone (such as deleting or repositioning photos) will not be reflected in Immich.
  * **User-Specific Sync:** Album synchronization is unique to each server user and does not sync between different users or partners.
  * **Mobile-Only Feature:** Album synchronization is currently only available on mobile. For similar options on a computer, refer to [Libraries](https://docs.immich.app/features/libraries) for further details.


### Synchronizing albums from the past[​](https://docs.immich.app/features/mobile-app/#synchronizing-albums-from-the-past "Direct link to Synchronizing albums from the past")
![](https://docs.immich.app/assets/images/backup-album-sync-1b36292651f7f7123f71b177e652f3f8.webp)
Albums can be synchronized to the server even if they did not exist on the server before. You can enable this feature at any time and use the **Reorganize into album** button to backfill existing uploads into their corresponding albums.
Sync albums delete/move photos
If you delete/move photos in the local album on your device, it will not be reflected in the album on the server **even if** you click Sync albums It will only reflect files you add.
## Read-only/kid Mode[​](https://docs.immich.app/features/mobile-app/#read-onlykid-mode "Direct link to Read-only/kid Mode")
You can set the app to read-only mode to prevent accidental deletion of photos from your device, and only allow viewing photos on the timeline.
To toggle this feature, long-press the profile icon or go to `Settings > Advanced > Read-only Mode`.
![](https://docs.immich.app/assets/images/read-only-mode-8613670baff9adfeb0b86c0958a96378.webp)
[Edit this page](https://github.com/immich-app/immich/tree/main/docs/docs/features/mobile-app.mdx)
Last updated on **Oct 21, 2026** by **immich-push-o-matic[bot]**
[Previous Hardware-Accelerated Machine Learning](https://docs.immich.app/features/ml-hardware-acceleration)[Next Monitoring](https://docs.immich.app/features/monitoring)
  * [Download](https://docs.immich.app/features/mobile-app/#download)
  * [Login](https://docs.immich.app/features/mobile-app/#login)
  * [Backup](https://docs.immich.app/features/mobile-app/#backup)
  * [Sync only selected photos](https://docs.immich.app/features/mobile-app/#sync-only-selected-photos)
  * [Free Up Space](https://docs.immich.app/features/mobile-app/#free-up-space)
    * [How it works](https://docs.immich.app/features/mobile-app/#how-it-works)
    * [iCloud Photos](https://docs.immich.app/features/mobile-app/#icloud-photos)
    * [External App Dependencies (WhatsApp, etc.)](https://docs.immich.app/features/mobile-app/#external-app-dependencies)
  * [Album Sync](https://docs.immich.app/features/mobile-app/#album-sync)
    * [Album Synchronization Highlights](https://docs.immich.app/features/mobile-app/#album-synchronization-highlights)
    * [Synchronizing albums from the past](https://docs.immich.app/features/mobile-app/#synchronizing-albums-from-the-past)
  * [Read-only/kid Mode](https://docs.immich.app/features/mobile-app/#read-onlykid-mode)


Download
  * [Android](https://get.immich.app/android)
  * [iOS](https://get.immich.app/ios)
  * [Server](https://immich.app/download)


Company
  * [FUTO](https://futo.tech/)
  * [Purchase](https://buy.immich.app/)
  * [Merch](https://immich.store/)


Sites
  * [Home](https://immich.app)
  * [My Immich](https://my.immich.app/)
  * [Awesome Immich](https://awesome.immich.app/)
  * [Immich API](https://api.immich.app/)
  * [Immich Data](https://data.immich.app/)
  * [Immich Datasets](https://datasets.immich.app/)


Miscellaneous
  * [Roadmap](https://immich.app/roadmap)
  * [Cursed Knowledge](https://immich.app/cursed-knowledge)
  * [Privacy Policy](https://immich.app/privacy-policy)


Social
  * [GitHub](https://github.com/immich-app/immich)
  * [YouTube](https://www.youtube.com/@immich-app)
  * [Discord](https://discord.immich.app)
  * [Reddit](https://www.reddit.com/r/immich/)


Immich is available as open source under the terms of the GNU AGPL v3 License.

