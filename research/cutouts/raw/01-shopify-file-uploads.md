[Help](https://help.shopify.com/en)
[Start for free](https://admin.shopify.com/signup?language=en)
[Log in](https://help.shopify.com/en/user/login)
Contents
# Uploading and managing files
#### Caution
You should only ever upload files to the **Content** > **Files** section of your Shopify admin when they're intended for public access on your store, such as product media, downloadable content, and other storefront images. Never upload any documents that contain confidential, personal, or sensitive information about you, your business, or your customers.
The **Files** section is where you can manage all files uploaded to your store, including images, videos, 3D models, and other file types, such as PDFs and CSV files. You can upload, manage, and delete files from the [**Files**](https://admin.shopify.com/content/files) section in your Shopify admin.
The file picker is available in different areas of your Shopify admin, such as the following examples:
  * Adding media to a [product](https://help.shopify.com/en/manual/products/product-media/add-media).
  * Editing your [theme](https://help.shopify.com/en/manual/online-store/images/theme-images).
  * Creating [metafields](https://help.shopify.com/en/manual/custom-data/metafields).
  * Adding media in the [rich text editor](https://help.shopify.com/en/manual/shopify-admin/productivity-tools/rich-text-editor).


All files you upload through the file picker are added to the [**Files**](https://admin.shopify.com/content/files) page of your Shopify admin.
## On this page
  * [File requirements](https://help.shopify.com/en/manual/shopify-admin/productivity-tools/file-uploads#file-requirements)
  * [Upload a file on the Files page](https://help.shopify.com/en/manual/shopify-admin/productivity-tools/file-uploads#upload-a-file)
  * [Organize files into folders and manage folders](https://help.shopify.com/en/manual/shopify-admin/productivity-tools/file-uploads#folders)
  * [Search and filter the file list](https://help.shopify.com/en/manual/shopify-admin/productivity-tools/file-uploads#filter-the-file-list)
  * [Change the sort order of the file list](https://help.shopify.com/en/manual/shopify-admin/productivity-tools/file-uploads#change-the-sort-order)
  * [Make a file available for download](https://help.shopify.com/en/manual/shopify-admin/productivity-tools/file-uploads#make-a-file-available)
  * [Original media downloads](https://help.shopify.com/en/manual/shopify-admin/productivity-tools/file-uploads#original-media-downloads)
  * [Editing files](https://help.shopify.com/en/manual/shopify-admin/productivity-tools/file-uploads#edit-a-file)
  * [Delete a file](https://help.shopify.com/en/manual/shopify-admin/productivity-tools/file-uploads#delete-a-file)
  * [Replace files](https://help.shopify.com/en/manual/shopify-admin/productivity-tools/file-uploads#replace-files)
  * [Edit files without overwriting the existing file](https://help.shopify.com/en/manual/shopify-admin/productivity-tools/file-uploads#edit-files-without-overwriting-the-existing-file)
  * [File storage limits by plan](https://help.shopify.com/en/manual/shopify-admin/productivity-tools/file-uploads#file-limits)
  * [Video and 3D model limits by plan](https://help.shopify.com/en/manual/shopify-admin/productivity-tools/file-uploads#video-and-3d-model-limits)
  * [Best practices for file names](https://help.shopify.com/en/manual/shopify-admin/productivity-tools/file-uploads#best-practices-for-file-names)
  * [Generate image](https://help.shopify.com/en/manual/shopify-admin/productivity-tools/file-uploads#generate-image)


## File requirements
You can upload files to the [**Files**](https://admin.shopify.com/content/files) page in your Shopify admin. Files must meet the following requirements:
### Image file requirements  
Requirements for file size, resolution, aspect ratio, file format, and file naming conventions for images in the Shopify admin.  
| Attribute  | Requirement  |  
| --- | --- |  
| File size  | Maximum of 20 MB (megabytes)  |  
| Resolution  | Maximum of 25 MP (megapixels)  |  
| Aspect ratio  | Between 100:1 and 1:100  |  
| File formats  | JPEG, PNG, WEBP, HEIC, and GIF  |  
| File names  | File names can contain letters, numbers, spaces, and symbols, but must not begin with a period `.`  |  
#### Tip
Image file names can't end with the following words - `pico`, `icon`, `thumb`, `testing`, `small`, `compact`, `medium`, `large`, or `grande`. The Shopify content delivery network (CDN) can misinterpret these endings as image transformation requests, such as resizing. If you upload an image with a name such as `test_medium.png`, then a suffix is automatically added to the filename to prevent conflicts.
### Video file requirements  
Requirements for file size, file formats, resolution, video length, width and height, frame rate, and file naming conventions for videos in the Shopify admin.  
| Attribute  | Requirement  |  
| --- | --- |  
| File size  | Maximum of 1 GB (gigabyte)  |  
| Resolution  | Maximum resolution of UHD  |  
| Video length  | Maximum video length of 10 minutes  |  
| File formats  | MOV, MP4, and WEBM  |  
| Minimum width and height  | 100 pixels  |  
| Maximum width and height  | 4096 pixels  |  
| Maximum frame rate  | 120 frames per second  |  
| Minimum video length  | 0.25 seconds  |  
| File names  | File names can contain letters, numbers, spaces, and symbols, but can't begin with a period `.`  |  
#### Note
These limits don't apply to embedded Vimeo or YouTube links.
### Recommended video specifications  
Recommendations for aspect ratio, bitrates, frame rates, resolution, supported codecs, and supported color spaces for videos in the Shopify admin.  
| Feature  | Recommendation  |  
| --- | --- |  
| Aspect ratio  | The aspect ratio should be one of the following: 
  * 16:9
  * 9:16
  * 4:3
  * 3:4
  * 1:1

 |  
| Bitrates  | Incoming videos are processed, and the best quality is selected automatically. The input media is analyzed, and an appropriate bitrate is selected from the following ranges. 
  * HLS 
    * SD 480: Range from 900 kbps to 2800 kbps
    * HD 720: Range from 2000 kbps to 6500 kbps
    * HD 1080: Range from 3200 kbps to 10400 kbps
  * MP4 
    * SD 480: Range from 0.9 Mbps to 1.5 Mbps
    * HD 720: Range from 1.6 Mbps to 4.5 Mbps
    * HD 1080: Range from 2.5 Mbps to 7.2 Mbps

 |  
| Frame rate  | 
  * 60 fps
  * 30 fps
  * 25 fps

 |  
| Resolution  | 
  * 3840x2160 (UHD)
  * 1920x1080 (1080p)
  * 1280x720 (720p)
  * 854x480 (480p)

Vertical orientation is also recommended for these resolutions, for example, 720x1280 px.   |  
| Supported codecs  | 
  * Video: H.264 (AVC)
  * Audio: AAC, MP3, Opus

 |  
| Supported color spaces  | 
  * Rec.601
  * Rec.709
  * Rec.2020

 |  
### Generic file requirements
Generic files can be any file other than HTML, and are intended for downloading by the customer.  
Requirements for file size, file formats, and file naming conventions for generic files in the Shopify admin.  
| Attribute  | Requirement  |  
| --- | --- |  
| File size  | Maximum of 20 MB  |  
| File formats  | Any file type except HTML  |  
| File names  | File names can contain letters, numbers, spaces, and symbols, but must not begin with a period `.`  |  
### File format requirements
If you're on a paid plan, then you can upload any file format other than HTML.
If you're on a trial plan, then you can upload only the following file formats:
  * JS
  * CSS
  * GIF
  * JPEG
  * PNG
  * JSON
  * CSV
  * PDF
  * WebP
  * HEIC


You also need to [verify your email address](https://help.shopify.com/en/manual/privacy-and-security/account-security/verify-account-email) before you can upload PDF files.
If you're on a trial plan and you want to upload other file formats, then [check and update your plan](https://help.shopify.com/en/manual/your-account/manage-billing/managing-your-bills/billing-plan-changes#change-plan).
Different parts of your store, such as your theme, pages, and blogs, only support certain file formats. For more information about supported file formats, refer to the following resources:
  * [Using the rich text editor](https://help.shopify.com/en/manual/shopify-admin/productivity-tools/rich-text-editor): for pages, blog posts, product and collection descriptions, and theme elements
  * [Uploading media](https://help.shopify.com/en/manual/online-store/images/theme-images#image-formats): for images and videos in your theme


#### Tip
To share a video that's larger than 1GB or longer than 10 minutes, use a video hosting service such as [YouTube](https://www.youtube.com) or [Vimeo](https://vimeo.com), and then add the video's sharing link to your content.
#### Note
You can import [products](https://help.shopify.com/en/manual/products/import-export), [customers](https://help.shopify.com/en/manual/customers/import-export-customers), or [inventory data](https://help.shopify.com/en/manual/inventory-and-locations/setup/inventory-csv) using [CSV files](https://help.shopify.com/en/manual/shopify-admin/productivity-tools/csv-files#csv-files). Importing data by CSV file isn't done through the **Files** page, but through the respective page in your Shopify admin.
## Upload a file on the Files page
You can upload files to Shopify on the **Files** page. You can then use the uploaded files across your Shopify admin, including as [brand images](https://help.shopify.com/en/manual/promoting-marketing/managing-brand-assets), [product media](https://help.shopify.com/en/manual/products/product-media), and [metaobjects](https://help.shopify.com/en/manual/custom-data/metaobjects).
#### Steps:
Desktop
  1. From your Shopify admin, go to **Content** > [**Files**](https://admin.shopify.com/content/files).
  2. Click **Upload files**.
  3. Select up to 200 files to upload, and then click **Open**.

Mobile
  1. From the [Shopify app](https://www.shopify.com/install/detect), tap the ![Menu](https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/MenuIcon.svg) icon.
  2. In the **Content** menu, tap the ![arrow down](https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/ChevronDownIcon.svg) icon, and then tap **Files**.
  3. Tap **Upload files**.
  4. Select the files that you want to upload, and then tap **Open**.


#### Note
As part of verifying your domain, you might be asked to upload files to the root folder of your site. If you're [verifying your website with a third-party service](https://help.shopify.com/en/manual/promoting-marketing/seo/find-site-map#add-domain-properties-and-verify-your-site-with-google), then use meta tags instead.
### Troubleshoot an upload that stays in the uploading or processing state
A banner such as **Uploading 1 remaining** can remain in **Content** > **Files** after the upload finishes. The banner clears on its own.
Check **Content** > **Files** first. If you added the file to a product, then also check the product's **Media** section. If your file is in either place, then the upload succeeded and no action is needed.
If your file isn't in **Files** or in the product's **Media** section, then the file didn't finish processing. Files that are stuck uploading or processing are removed automatically, which can take up to 2 hours. After the banner clears, upload the file again. For a large video, compress the video or lower its resolution before you upload it again. If the banner is still displayed after 2 hours, then [contact Shopify Support](https://help.shopify.com/en/manual/your-account/contact-shopify-support).
For other upload errors, refer to [troubleshooting a failed media upload](https://help.shopify.com/en/manual/products/product-media/add-media#troubleshoot-uploads).
## Organize files into folders and manage folders
You can organize your files by creating folders within the **Files** page of your Shopify admin, and moving files into the folders. You can also create subfolders within other folders to create more granular file organization.
To navigate to a folder, click the name of the folder. To navigate back to the previous folder or main **Files** page, click the ![Back](https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/ChevronLeftIcon.svg) icon, or select the folder or main **Files** page from the breadcrumbs.
### Add a new folder
You can add a new folder to the main **Files** page, or as a subfolder inside of another. To add a subfolder, first navigate to the folder where you want to add the subfolder.
#### Steps:
  1. From your Shopify admin, go to **Content** > [**Files**](https://admin.shopify.com/content/files).
  2. Click **![Add folder](https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/FolderAddIcon.svg)New folder**.
  3. Enter a name.
  4. Click **Create**.


### Moving files and folders
You can reorganize files, folders, and subfolder files on your **Files** page by moving them. To move files or folders back to the main **Files** page, select **Files** as the destination.
You can also create a new folder to move your selected files to. The new folder is created within the current folder. You can still move your subfolder after you create it.
#### Steps:
  1. From your Shopify admin, go to **Content** > [**Files**](https://admin.shopify.com/content/files).
  2. Select any files, folders, or both that you want to move.
  3. Click **Move to**.
  4. In the **Move** dialog, click the **Select a destination** field, and then select the destination in either of the following ways:


  * To select an existing folder:
    1. Select the folder.
    2. Click **Move**.
  * To add a new folder:
    1. Click **![Add](https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/PlusCircleIcon.svg)New folder**.
    2. Enter a name.
    3. Click **Move and create**.


### Delete a folder
You can delete any folder on the **Files** page. If you delete a folder, then you also delete any contents of that folder. Before you delete a folder, first make sure you move any files or subfolders you don't want to delete to another folder, or to the main **Files** page.
#### Steps:
  1. From your Shopify admin, go to **Content** > [**Files**](https://admin.shopify.com/content/files).
  2. Select the checkbox beside the folder that you want to delete. You can select multiple folders, or a combination of files and folders.
  3. Click **Delete** , and then click **Delete** again to confirm.


## Search and filter the file list
You can filter the file list or search for a file from the **Content** > **Files** page of your Shopify admin or in the **File** picker.
You can filter your files in the following ways:
  * Search file attributes, including file names and types, using the search bar.
  * Filter by size using the **File size** range selector.
  * Filter by type using the **File type** menu.
  * Filter by file reference using the **Used in** menu.
  * Filter by alt text using the **Alt text** menu.


All filters are displayed in-line in the search bar, so you get a full view of the criteria influencing your search results. You can also use `is`/`is not` and `or`/`and` logical operators to create more advanced views with specific filter criteria.
#### Tip
If you need to perform the same searches or filter by the same terms regularly, then you can [save the filter view](https://help.shopify.com/en/manual/shopify-admin/productivity-tools/file-uploads#save-filters).
Learn more about [searching, filtering, and sorting your list views in the Shopify admin](https://help.shopify.com/en/manual/shopify-admin/productivity-tools/searching-filtering-views).
#### Steps:
  1. From your Shopify admin, go to **Content** > [**Files**](https://admin.shopify.com/content/files).
  2. Optional: Click **All** to open the view menu, and then select the view that you want to filter.
  3. Select an operator and value for your filter. The available values are different depending on the filter that you select.
  4. Optional: Continue entering keywords to add different filters and values to refine your search:
     * To include an additional filter with an `and` operator to your search, click ![Plus Circle Icon](https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/PlusCircleIcon.svg) or add a space, and then start entering the name of the additional filter that you want to include.
     * To include an additional value with an `or` operator to a filter, add a comma, and then start entering the name of the additional value that you want to include.
  5. Optional: Click the filter tags of any filter in the search bar to edit the filter.


### Save filter view
If you need to perform the same searches or filter by the same terms regularly, then you can save the filters as views so that they're easier to access. Saved views are added to the views list beside the **Files** search bar. You can click the selector to filter the files using the saved filter parameters.
#### Steps:
Desktop
  1. From your Shopify admin, go to **Content** > [**Files**](https://admin.shopify.com/content/files).
  2. Using the searchbar, apply the appropriate filters and search keywords.
  3. Click **Save**.
  4. In the **Save view as** dialog, enter a name for your saved filter view.
  5. Click **Save**.

Mobile
  1. From the [Shopify app](https://www.shopify.com/install/detect), tap the ![Menu](https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/MenuIcon.svg) icon.
  2. In the **Content** menu, tap the ![arrow down](https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/ChevronDownIcon.svg) icon, and then tap **Files**.
  3. Using the **Search and filter** option, apply the appropriate filters and search keywords.
  4. Tap ![Horizontal menu](https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/MenuHorizontalIcon.svg) > **Save as new view**.
  5. In the **Save view as** dialog, enter a name for your saved filter view.
  6. Tap **Save**.


### Edit columns in your Files list
You can edit columns in both default and custom views, and the changes that you make apply only to the view that you're currently on. You can hide or unhide columns, as well as reorder the columns, with the exception of the main leftmost column.
#### Steps:
  1. From your Shopify admin, go to **Content** > [**Files**](https://admin.shopify.com/content/files).
  2. Optional: Click **All** to open the view menu, and then select the custom view that you want to edit the columns for.
  3. Click the ![Layout Columns 3](https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/LayoutColumns3Icon.svg) icon to open the display option panel.
  4. In the **Columns** section, customize your view's columns by doing any of the following actions:
     * To hide a column, click ![View](https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/ViewIcon.svg).
     * To unhide a column, click ![Hide](https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/HideIcon.svg).
     * To rearrange a column, click ![Drag handle](https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/DragHandleIcon.svg) and drag the column up or down.
  5. Optional: To permanently apply the column order to your custom view, click **Save** > **Update view**.


### Use bulk action to delete multiple files
In any file view, you can select some or all of the files and delete them in bulk. You can switch between file views to continue selecting files, and apply filters or search using keywords to display only relevant files that you can also select.
#### Note
If you're on a desktop device, then you can click **Show all selected** to display only the files that you've currently selected.
Learn more about [using bulk actions in your Shopify admin](https://help.shopify.com/en/manual/shopify-admin/productivity-tools/bulk-actions).
#### Steps:
  1. From your Shopify admin, go to **Content** > [**Files**](https://admin.shopify.com/content/files).
  2. Click a file view.
  3. [Select the items that you want to delete](https://help.shopify.com/en/manual/shopify-admin/productivity-tools/bulk-actions#select-items-to-edit-in-bulk).
  4. Click **Delete files**.
  5. In the dialog, click **Delete**.


## Change the sort order of the file list
By default, files are listed from newest to oldest based on the date that they were uploaded.
#### Note
If you change the sort order of your files in the Shopify admin on desktop, then the file list reverts to the default sort order after it's refreshed, such as when you navigate to a different view. You can save an alternative sort order using the Shopify mobile app.
You can change the sort order of your file list to any of the following options:  
Shopify admin file list sorting options  
| Sorting option  | Value  | Description  |  
| --- | --- | --- |  
| Date added  | Sorted by date from **Newest first** or **Oldest first**.  | This option displays files in the order that the products were created. By default, the file list is sorted by **Date added** : **Newest first**.  |  
| File name  | Sorted alphabetically from **A-Z** or **Z-A**.  | This option displays files in alphabetical order by file name.  |  
| Size  | Sorted by file size from **Smallest first** or **Largest first**.  | This option displays files in order of file size.  |  
#### Steps:
Desktop
  1. From your Shopify admin, go to **Content** > [**Files**](https://admin.shopify.com/content/files).
  2. Optional: Click **All** to open the view menu, and then select the custom view that you want to review the sort order for.
  3. Click the ![Layout Columns 3](https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/LayoutColumns3Icon.svg) icon to open the display option panel.
  4. Click the ![Sort](https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/SortIcon.svg) **Sort by** menu, and then select a sort criteria option, as well as a sort order.

Mobile
  1. From the [Shopify app](https://www.shopify.com/install/detect), tap the ![Menu](https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/MenuIcon.svg) icon.
  2. In the **Content** menu, tap the ![arrow down](https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/ChevronDownIcon.svg) icon, and then tap **Files**.
  3. Optional: Tap **All** to open the view menu, and then select the custom view that you want to review the sort order for.
  4. Tap the ![Layout Columns 3](https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/LayoutColumns3Icon.svg) icon to open the display option panel.
  5. Tap the ![Sort](https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/SortIcon.svg) **Sort by** menu, and then select a sort criteria option, as well as a sort order.


## Make a file available for download
To make a file available for visitors to download, upload it on the **Files** page, and then add a link to it in a [page's content](https://help.shopify.com/en/manual/shopify-admin/productivity-tools/rich-text-editor#link-to-a-file) or in your online store menus. You can copy a link to the file to your clipboard by clicking the **Link** button beside the file.
#### Grow your business
Want to sell digital products in your store? Use the free [Digital Products app](https://help.shopify.com/en/manual/products/digital-service-product/digital-downloads) to set up and sell digital files to your customers.
## Original media downloads
The Shopify Imagery service manages your images and videos to ensure the best possible format is displayed at the appropriate place in your online store.
You can download the original, unoptimized file to your device using the download button in the **Preview and edit** window.
#### Steps:
Desktop
  1. From your Shopify admin, go to **Content** > [**Files**](https://admin.shopify.com/content/files).
  2. Click the file that you want, or use the filters to sort the list or narrow it to a specific media file.
  3. Click the download button. The original format saves to your device.

Mobile
  1. From the [Shopify app](https://www.shopify.com/install/detect), tap the ![Menu](https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/MenuIcon.svg) icon.
  2. In the **Content** menu, tap the ![arrow down](https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/ChevronDownIcon.svg) icon, and then tap **Files**.
  3. Tap the file that you want, or use the filters to sort the list or narrow it to a specific media file.
  4. Tap the download button. The original format saves to your device.


## Editing files
You can preview and edit files by clicking the file's thumbnail from the [**Files**](https://admin.shopify.com/content/files) page. Edits that you make on the **Files** page apply to all places the file is used in your store.
Review the following table to learn more about how to edit your files:  
List of actions that you can take for editing files in your Shopify admin.  
| Action  | Description  |  
| --- | --- |  
| Rename a file  | Update the name of your file by changing the **URL Handle** of your file. When you change your file's URL, the previous URL for that file no longer works.  |  
| Replace a file  | Replace an existing file with a new file, and keep the same file name and URL handle. You can replace a file only with the same file format, such as replace a JPEG file with another JPEG file.  |  
| Add alt text  | Add a brief description of the image or video for people with visual impairment or low-bandwidth connections.  |  
| Add a [focal point](https://help.shopify.com/en/manual/online-store/images/theme-images#focal-points) to an image  | Select the most important part of the image to help themes crop the image more intelligently.  |  
| Update a video cover image  | Update the video cover image that acts as a preview image for your video.  |  
You can also edit media files using the [media editor](https://help.shopify.com/en/manual/shopify-admin/productivity-tools/media-editor) and [AI-powered media generation](https://help.shopify.com/en/manual/ai-powered-tools/media-generation).
To make other types of edits, download the file, make the edits in an editing software of your choice, and then upload it again to the **Files** page.
## Delete a file
You can delete one or more files from the **Files** page. [Learn more about bulk actions](https://help.shopify.com/en/manual/shopify-admin/productivity-tools/bulk-actions).
#### Steps:
Desktop
  1. From your Shopify admin, go to **Content** > [**Files**](https://admin.shopify.com/content/files).
  2. Select the checkbox beside the file that you want to delete. You can select multiple files.
  3. Click **Delete** , and then click **Delete** again to confirm.

Mobile
  1. From the [Shopify app](https://www.shopify.com/install/detect), tap the ![Menu](https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/MenuIcon.svg) icon.
  2. In the **Content** menu, tap the ![arrow down](https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/ChevronDownIcon.svg) icon, and then tap **Files**.
  3. Select the checkbox beside the file that you want to delete. You can select multiple files.
  4. Tap **Delete** , and then tap **Delete** again to confirm.


## Replace files
You can replace a file from the **Files** page. You can't replace files as a bulk action.
#### Note
When you replace a file, the file name stays the same, but the file's link changes.
#### Steps:
  1. From your Shopify admin, go to **Content** > [**Files**](https://admin.shopify.com/content/files).
  2. Click the **Replace** icon next to the file name.
  3. Select the file that you want to upload.


## Edit files without overwriting the existing file
In the file editor, it's possible to make destructive edits to an image, such as changing the background of an image. To make changes without overwriting an existing file, save the changes as new.
#### Steps:
  1. From your Shopify admin, go to **Content** > [**Files**](https://admin.shopify.com/content/files).
  2. Select a media file to open the file editor.
  3. Make file edits.
  4. From the Save dropdown menu, select Save as new.


Saving as new saves the new file to your store's file system and preserves the original image in its original state.
## File storage limits by plan
The amount of storage that you have available for uploaded files varies depending on your Shopify subscription plan.
Review the following table to learn more about file storage limits.  
Storage limits for each type of Shopify subscription plan, for the files that you have in your Shopify admin.  
| Plan  | Limit per store  |  
| --- | --- |  
| Starter  | 100 GB  |  
| [Pause and Build](https://help.shopify.com/en/manual/your-account/manage-orgs-and-stores/manage-pricing-plan/pause-store)  | 100 GB  |  
| Retail  | 100 GB  |  
| Basic and Shopify Partner [development stores](https://help.shopify.com/partners/manage-clients-stores/development-stores/create-development-stores)  | 100 GB  |  
| Grow  | 300 GB  |  
| Advanced  | 500 GB  |  
| Plus and Shopify Partner [Plus sandbox stores](https://help.shopify.com/partners/manage-clients-stores/development-stores/plus-sandbox-store)  | 1 TB  |  
| Enterprise  | 10 TB  |  
#### Plan requirement
If you change to a plan with a lower storage limit, and your store currently uses more storage than the new plan allows, then your existing files aren't impacted. However, you can't upload new files until you [delete enough files](https://help.shopify.com/en/manual/shopify-admin/productivity-tools/file-uploads#delete-a-file) to bring your total storage below the new plan's limit.
### Paid storage increases
#### Early access
Access to paid storage increases is in early access, and is available only for Plus and Enterprise stores.
If you want to purchase additional file storage space for your organization, then the organization owner can contact Shopify Support to request an incremental storage increase.
The requested increase increments are added to one [production store](https://help.shopify.com/en/manual/your-account/manage-orgs-and-stores/manage-orgs/view-filter-stores#store-type), and up to two [development stores](https://help.shopify.com/en/manual/your-account/manage-orgs-and-stores/manage-orgs/view-filter-stores#store-type). All three of the included shops receive their own increase. The increment isn't split between them. Increases must be added in the available increments. Fractional paid increases aren't available.  
Available paid storage increases for each type of Shopify subscription plan, for the files that you have in your Shopify admin.  
| Plan  | Pricing Increment  |  
| --- | --- |  
| Plus  | $100 USD/month per 1 TB  |  
| Enterprise  | $1,000 USD/month per 10 TB  |  
## Video and 3D model limits by plan
The amount of both videos and 3D models that you have available to upload varies depending on your Shopify subscription plan.
Review the following table to learn more about video and 3D model limits.  
Video and 3D model upload limits for each type of Shopify subscription plan.  
| Plan  | Limit per store  |  
| --- | --- |  
| Starter  | 250  |  
| [Pause and Build](https://help.shopify.com/en/manual/your-account/manage-orgs-and-stores/manage-pricing-plan/pause-store)  | 250  |  
| Retail  | 250  |  
| Basic and Shopify Partner [development stores](https://help.shopify.com/partners/manage-clients-stores/development-stores/create-development-stores)  | 250  |  
| Grow  | 1,000  |  
| Advanced  | 5,000  |  
| Plus and Shopify Partner [Plus sandbox stores](https://help.shopify.com/partners/manage-clients-stores/development-stores/plus-sandbox-store)  | 50,000  |  
| Enterprise  | 100,000  |  
#### Note
If you're on a Plus or Enterprise plan, then you can [contact Shopify Support](https://help.shopify.com/en/manual/your-account/contact-shopify-support) to request increased video and 3D model upload limits.
### Video storage limits by plan
The amount of storage that you have available for uploaded videos varies depending on your Shopify subscription plan.
Review the following table to learn more about video storage limits.  
Video storage limits for each type of Shopify subscription plan.  
| Plan  | Limit per store  |  
| --- | --- |  
| Starter  | 50 GB  |  
| [Pause and Build](https://help.shopify.com/en/manual/your-account/manage-orgs-and-stores/manage-pricing-plan/pause-store)  | 50 GB  |  
| Retail  | 50 GB  |  
| Basic and Shopify Partner [development stores](https://help.shopify.com/partners/manage-clients-stores/development-stores/create-development-stores)  | 50 GB  |  
| Shopify Partner [Plus sandbox stores](https://help.shopify.com/partners/manage-clients-stores/development-stores/plus-sandbox-store)  | 60 GB  |  
| Grow  | 500 GB  |  
| Advanced  | 500 GB  |  
| Plus  | 2 TB  |  
| Enterprise  | 10 TB  |  
#### Note
This is a separate limit from the [total storage limit](https://help.shopify.com/en/manual/shopify-admin/productivity-tools/file-uploads#file-limits) for all files in your store. If you're on a Plus or Enterprise plan, then you can [contact Shopify Support](https://help.shopify.com/en/manual/your-account/contact-shopify-support) to request increased video-specific storage limits.
## Best practices for file names
When you upload an image file, a unique identifier might be added to the filename. This can happen in the following situations:
  * A file with the same name already exists in your store. This includes files uploaded directly to product pages that might not be displayed in **Content** > **Files**.
  * The filename contains special characters or formatting that conflicts with Shopify's content delivery network (CDN).


To prevent unique identifiers from being added to filenames, use the following file naming practices:
  * Ensure the filename is unique and doesn't match any existing files in your store.
  * Avoid using underscores immediately before image dimensions in the filename. For example, use `product-image-5x4.jpeg` instead of `product_image_5x4.jpeg`.
  * Use descriptive filenames that don't include special formatting.


If you need to change a filename after upload, then you can rename files from the **Content** > [**Files**](https://admin.shopify.com/content/files) page by editing the **URL Handle**.
## Generate image
You can generate images using AI directly in the unified file picker throughout the Shopify admin. This feature lets you create custom images for your products, content, and marketing materials without needing external tools.
When you generate an image, it's created temporarily and displayed in the file picker. To save the generated image to your store, you need to click **Keep**. If you don't explicitly save the image by clicking **Keep** , then the generated image is discarded and isn't saved to your store.
#### Note
Generated images that aren't saved by clicking **Keep** are automatically discarded and don't count toward your storage limits.
Leave feedback

