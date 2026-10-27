[Help](https://help.shopify.com/en)
[Start for free](https://admin.shopify.com/signup?language=en)
[Log in](https://help.shopify.com/en/user/login)
Contents
# Product media types
#### Tip
For a complete list of requirements and information about uploading files and using the file system in your Shopify store, refer to [_Uploading and managing files_](https://help.shopify.com/en/manual/shopify-admin/productivity-tools/file-uploads).
Customers browsing in your online store view media such as images on product pages. Using media such as video, 3D models, and augmented reality on your product page can increase a customer's confidence in your products, leading to a better customer experience and more sales. It's important that the media that you add for your products are high quality and meet the [required specifications](https://help.shopify.com/en/manual/shopify-admin/productivity-tools/file-uploads#file-requirements) so that they upload and are displayed properly.
To display videos or 3D models on product pages, your online store needs to use a theme that supports the media that you want to add. All themes support adding images to your products.
## On this page
  * [Images](https://help.shopify.com/en/manual/products/product-media/product-media-types#images)
  * [3D models](https://help.shopify.com/en/manual/products/product-media/product-media-types#3d-models)
  * [Videos](https://help.shopify.com/en/manual/products/product-media/product-media-types#videos)
  * [Supported themes for 3D models or videos](https://help.shopify.com/en/manual/products/product-media/product-media-types#supported-themes)
  * [Adding product media by using metafields](https://help.shopify.com/en/manual/products/product-media/product-media-types#media-metafields)


## Images
Product images are used to display products across Shopify's sales channels, including on your online store and in Shopify POS. The best file type for most product images is `PNG`, followed by `JPEG`. Other accepted file types are `TIFF`, `BMP`, `GIF`, `SVG`, `HEIC`, and `WebP`. Animated versions of GIF and WebP files are also supported. Shopify's Imagery service determines which image formats are supported by your customer's web client, and then automatically displays the image in the best format available. The exact way that images display on your store depends on your online store theme, but all themes support adding images.
Your product and collection images can be any size up to 5000 x 5000 px, or 25 megapixels. Product and collection images need to have a file size smaller than 20 MB to be added to Shopify.
High resolution photos look more polished and professional to your customers. For square product images, a size of 2048 x 2048 px usually displays best. For more advice about photographing your products, read _[The definitive DIY guide to beautiful product photography](https://www.shopify.ca/blog/12206313-the-ultimate-diy-guide-to-beautiful-product-photography)_ in the Shopify Blog.
#### Note
When product images are displayed side by side on [collection pages](https://help.shopify.com/en/manual/products/collections), they have different sizes. To make your images display to be the same size, you need to use a [consistent aspect ratio](https://help.shopify.com/en/manual/shopify-admin/productivity-tools/media-editor#understanding-image-aspect-ratio), or height-to-width ratio, for all the images that you add as your featured, or main, images. Themes can also use the [Shopify CDN](https://cdn.shopify.com) to request consistent sizing for images that might not be saved in the same aspect ratio.
When you add an image, different sizes are automatically created for use in different areas of your online store theme. For example, a product image's large version might be used on the product detail page, where the customer wants to view the product in detail. The compact version of the same image might be used on the collection templates, where a larger image isn't necessary.
#### Grow your business
Are you looking for royalty-free images to enhance your online store? You can download high resolution product and lifestyle photos from [Burst](https://burst.shopify.com).
## 3D models
3D models are virtual representations of an object in three dimensions. 3D models can provide your customers with a better sense of the size, scale, and the details of your products.
A customer who is browsing your store can view 3D product models from the product page. The models use the device's camera and screen to display the product in the customer's environment. Using the 3D model, the customer can view the object from any angle.
You need to make sure that your 3D model files meet the following requirements before you [add them to your online store](https://help.shopify.com/en/manual/products/product-media/add-media):
  * File size: Up to 500 MB
  * File type: `GLB`, `USDZ`


If you upload a 3D model file that exceeds 15 MB, then your file is automatically optimized. Optimization reduces file sizes and increases loading speeds.  
List of model sizes (in MB), the optimization rule, and the default conversion media type.  
| Model size  | Optimization  | Conversion  |  
| --- | --- | --- |  
| Smaller than 15 MB  | 3D model isn't optimized. Model geometry and materials aren't changed.  | Files are converted to ensure both a .USDZ and .GLB version of the model is available. Conversion ensures compatibility with both Android and iOS based devices.  |  
| Larger than 15 MB  | 3D model is optimized. Model geometry and textures are optimized, while preserving the visual output of the original file.  | Files are converted to ensure both a .USDZ and .GLB version of the model is available. Conversion ensures compatibility with both Android and iOS based devices.  |  
#### Grow your business
You can [hire a Shopify Partner](https://help.shopify.com/en/manual/partner-directory) to help you create quality 3D models to display your products.
## Videos
You can add videos for your product in two ways: uploading a video file, or embedding a YouTube or Vimeo video link. If you're uploading video files, then make sure that they meet the following requirements:
  * Video length: Up to 10 minutes
  * Video size: Up to 1 GB
  * Video resolution: Up to 4K (4096 x 2160 px)
  * Video file type: `.mp4`, `.mov`, or `.webm`


#### Note
`.webm` and `.mov` files can be uploaded in the Shopify admin, but Shopify converts and serves all videos as `.mp4` or `HLS` format for optimal compatibility to customers. Learn more about [file format specifications](https://help.shopify.com/en/manual/shopify-admin/productivity-tools/file-uploads#file-requirements).
You don't need to meet these requirements for embedding YouTube or Vimeo videos, however URLs other than YouTube or Vimeo URLs aren't supported.
In browsers that support streaming, videos display in either 480p, 720p, or 1080p, depending on the viewer's connection speed and the resolution of the uploaded video. In browsers that don't support streaming, videos display in the highest resolution available.
You can [add images, 3D models, or videos](https://help.shopify.com/en/manual/products/product-media/add-media) for your products from your Shopify admin or the Shopify app.
#### Grow your business
You can [hire a Shopify Partner](https://help.shopify.com/en/manual/partner-directory) to help you create custom videos and animations that feature your products.
## Supported themes for 3D models or videos
Your theme might already support 3D models or videos. You need to ensure that your theme is updated with the right version.
The following Shopify themes support the display of 3D models or videos on your online store:
  * All of the Online Store 2.0 themes built by Shopify. Learn more about [theme architecture](https://help.shopify.com/en/manual/online-store/themes/managing-themes/versions#theme-types).
  * All of the [Horizon family of themes](https://themes.shopify.com/collections/horizon-themes).


Certain themes have also been updated to provide an enhanced experience for Vimeo video playback. If you want to feature Vimeo videos in your theme, then consider updating your theme to one of the following versions:
  * [Craft](https://themes.shopify.com/themes/craft/styles/default?surface_detail=os2-themes&surface_inter_position=1&surface_intra_position=2&surface_type=collection)
  * [Crave](https://themes.shopify.com/themes/crave/styles/default?surface_detail=os2-themes&surface_inter_position=1&surface_intra_position=3&surface_type=collection)
  * [Dawn](https://themes.shopify.com/themes/dawn?utm_source=help-page&utm_medium=web&utm_campaign=2021-08-dawn-launch&utm_content=pr&utm_term=ex)
  * [Sense](https://themes.shopify.com/themes/sense/styles/default?surface_detail=free-themes&surface_inter_position=1&surface_intra_position=4&surface_type=collection)


Most third-party themes have recent versions that include 3D models or videos. If you use a theme developed by a third party, then you can contact the theme developer for support, or refer to your theme's help documentation.
## Adding product media by using metafields
If you want to customize the way that product media are displayed in your online store, then you can use [metafields](https://help.shopify.com/en/manual/custom-data/metafields) to create a file reference metafield for your products. File reference metafields support uploading images to display your products, or all other file types for your customers to download. You can display JPEG, PNG, WEBP, SVG, HEIC, or GIF images in metafields on your online store. A metafield can contain only one file at a time.
If you have a [compatible theme](https://help.shopify.com/en/manual/online-store/themes/managing-themes/versions#features), then you can connect file reference metafields to your theme by using the theme editor. If you're using vintage themes, then you can [edit your theme code](https://help.shopify.com/en/manual/custom-data/metafields/displaying-metafields-on-your-online-store#edit-code-metafields) or hire a [Shopify Partner](https://help.shopify.com/en/manual/partner-directory) to help you.
Leave feedback

