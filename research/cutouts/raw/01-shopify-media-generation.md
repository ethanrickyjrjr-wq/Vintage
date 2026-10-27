[Help](https://help.shopify.com/en)
[Start for free](https://admin.shopify.com/signup?language=en)
[Log in](https://help.shopify.com/en/user/login)
Contents
# Media generation in the file editor
#### Plan requirement
Media generation with Sidekick is only available for stores on the Basic plan, Grow plan, Advanced plan, and Shopify Plus plan.
You can modify images using the power of artificial intelligence (AI) with media generation directly in the file editor. AI-powered media generation can help you create professional product images quickly without specialized design skills.
You can do the following actions with media generation:
  * **Color background** : [Replace](https://help.shopify.com/en/manual/ai-powered-tools/media-generation#color-background) an image's background with a solid color, with automatic subject detection and manual correction if needed
  * **Generate** : [Transform](https://help.shopify.com/en/manual/ai-powered-tools/media-generation#generate) your image using simple natural language prompts to change backgrounds, lighting, or other aspects of the image


#### Note
Shopify prioritizes originality and respects creators' rights, and doesn't support or endorse uploading images from the web or copyright infringement.
To report potential infringement, rights holders can use Shopify's existing copyright and trademark reporting forms. Learn more about [_Legal removals and intellectual property_](https://help.shopify.com/en/manual/compliance/intellectual-property).
## On this page
  * [Pricing](https://help.shopify.com/en/manual/ai-powered-tools/media-generation#pricing)
  * [Considerations and tips for editing images with media generation](https://help.shopify.com/en/manual/ai-powered-tools/media-generation#considerations)
  * [Color background](https://help.shopify.com/en/manual/ai-powered-tools/media-generation#color-background)
  * [Generate images](https://help.shopify.com/en/manual/ai-powered-tools/media-generation#generate)
  * [Extend images](https://help.shopify.com/en/manual/ai-powered-tools/media-generation#outpainting)
  * [Save generated images to your device](https://help.shopify.com/en/manual/ai-powered-tools/media-generation#save-image)
  * [Report the content in generated images](https://help.shopify.com/en/manual/ai-powered-tools/media-generation#report-image)
  * [Frequently Asked Questions](https://help.shopify.com/en/manual/ai-powered-tools/media-generation#faq)


## Pricing
For a limited time, media generation in the file editor is available on all Shopify plans at no additional cost.
## Considerations and tips for editing images with media generation
Before you start using media generation, review the following considerations:
  * **Image resolution and format** :
    * The default resolution for generated images is 1 megapixel (MP) resolution based on your image's aspect ratio. Aim to use images that are close to 1 megapixel in dimension.
    * Images larger than 1 MP are scaled down, whereas images under 1 MP are scaled up.
    * Modified images are saved in the original format. All images with [transparent backgrounds](https://help.shopify.com/en/manual/ai-powered-tools/media-generation#color-background) should be saved as a new file in PNG format to maintain the transparent background. Other image formats can't save a transparent background.
    * If you create images with transparent backgrounds, they should be saved as PNG files to maintain the transparent background. Other image formats can't save a transparent background.
  * **Image quality** :
    * Use images with clearly visible subjects and good contrast for best results.
    * Images with clean edges and simple compositions work better for background removal.
  * **Editing and saving** :
    * The Shopify AI image editor creates 1 AI-generated scene at a time. Additional sets can be generated, but any unused scenes are deleted when you close the editor unless you [save the images to your device](https://help.shopify.com/en/manual/ai-powered-tools/media-generation#save-image).
  * **Copyright and Usage** :
    * An invisible watermark is applied to all generated images, which doesn't restrict commercial use but can't be removed.


#### Grow your business
Not sure how to create great product images? The Shopify Blog has lots of articles to help you get started with [product photography](https://www.shopify.com/ca/blog/search?q=product+photography).
Learn more about [taking product photographs](https://help.shopify.com/en/manual/products/product-media/product-photography).
### Customizing your media generation with text prompts
When using the **Generate** feature, you can transform your images with effective text prompts. Use simple, natural language to describe what you want:
  * **Background changes** : "change background to a studio" or "kitchen setting with warm lighting"
  * **Scene descriptions** : "in a sunny park with grass and trees"
  * **Style specifications** : "professional ad photography" or "warm even lighting"
  * **Combined elements** : "studio setting with concrete backdrop and ambient lighting"


Consider these prompt tips:
Aesthetic and style keywords and phrases can help improve final touches to the rendering. Some examples to consider include the following types of descriptors:
  * **Location** : `indoors`, `outdoors`, `underwater`, `in the city`
  * **Lighting** : `warm even light`, `ambient`, `overcast`, `neon`, `studio lights`, `flash photography`
  * **Color** : `vibrant`, `muted`, `bright`, `monochromatic`, `black and white`, `pastel`
  * **Size** (relative to the subject): `extreme closeup`, `wide shot`, `6" x 4" x 2"`
  * **Camera angle** : `front shot`, `closeup`, `from above`


When crafting your text prompt, consider the following best practices:
  * Text prompts should be at least 3-7 words long. Ideally, format the prompt with short keywords or phrases separated by commas.
  * Avoid long lists of requests and instructions. Unlike a large language model (LLM) or chatbot, the text prompter for media generation isn't conversational.
  * If your product seems too large or too small compared to the context of the background scene, then include sizing information to help the generator scale the background to your product correctly. For example, `8oz jar candle` or `26" x 18" suitcase`.
  * To avoid objects 'floating' in the background scene, specify how the object should be grounded in relation to the background. For example, `drink bottle sitting on table` or `boots resting on floor against wall`.


## Color background
You can replace an image's background with a solid color or make it transparent. The feature automatically detects and separates the subject from the background, and you can manually correct the selection if needed.
### Steps:
Desktop
  1. From your Shopify admin, go to the media file that you want to edit.
  2. Click the thumbnail to open the file editor.
  3. In the file editor, click **Color background**.
  4. The feature automatically detects the subject in your image. If the automatic selection needs correction, then you can manually adjust which parts of the image are considered the subject by selecting **Choose subject**.
  5. Select the background color you want by doing one of the following options:
     * Click one of the preset color swatches from **Monochrome** or **Standard colors**.
     * In the **Custom** section, click `+` to use the color picker or enter a specific color code.
  6. Click **Save** or **Save as new** to save your image.


To discard all changes to the image, click **Revert to original**.
Mobile
  1. From the [Shopify app](https://www.shopify.com/install/detect), go to the media file that you want to edit.
  2. Tap on the image you want to edit.
  3. Tap **Background**.
  4. The feature automatically detects the subject in your image.
  5. Select the background color you want by tapping one of the color swatches or using the custom color picker.
  6. Tap **Save** or **Save as new** to save your image.


## Generate images
You can transform your image using simple natural language prompts. This feature lets you change backgrounds, settings, or other aspects of your image by simply describing what you want.
For example, you can type "in a sunny park, grass, bench under a tree, professional ad photography" or "change background to a studio" and the AI will transform your image accordingly.
### Steps:
Desktop
  1. From your Shopify admin, go to the media file that you want to edit.
  2. Click the thumbnail to open the file editor.
  3. In the file editor, click **Generate**.
  4. In the text prompt box, describe how you want to transform your image using natural language. You can:
     * Change the background ("change background to a living room")
     * Set a scene ("in a sunny park with grass and trees")
     * Specify a style ("professional ad photography")
     * Combine multiple elements ("studio setting with warm lighting")
  5. Click **Submit**.
  6. Click **Save** or **Save as new** to save your image.


To discard all changes to the image, click **Revert to original**.
Mobile
  1. From the [Shopify app](https://www.shopify.com/install/detect), go to the media file that you want to edit.
  2. Tap on the image you want to edit.
  3. Tap **Generate**.
  4. In the text prompt box, describe how you want to transform your image using natural language.
  5. Tap ![Circle Up](https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/CircleUpIcon.svg).
  6. Preview the generated option, and use the ![Undo icon](https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/UndoIcon.svg) or ![Redo icon](https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/RedoIcon.svg) as needed.
  7. Tap **Save** or **Save as new** to save your image.


## Extend images
You can extend image backgrounds beyond their original borders. This process, called outpainting, lets you add space or adjust framing around your subject. Outpainting images isn't available on the Shopify mobile app.
#### Steps:
  1. From your Shopify admin, go to the media file that you want to edit.
  2. Click the thumbnail to open the file editor.
  3. In the file editor, click **Crop and transform** and select the aspect ratio. 
  4. Using the slider, adjust the size of the canvas you want to expand.
  5. Click the ![Image Magic](https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/ImageMagicIcon.svg) icon to extend the background of your image. 
  6. Click **Save** or **Save as new** to save your image.


To revert all changes to the image, click **Discard**.
## Save generated images to your device
You can save any image you generate directly to your device's local storage or share on a mobile device. Generated images that aren't saved are lost when the editing session is finished.
### Steps:
Desktop
  1. Follow the steps to use [Color background](https://help.shopify.com/en/manual/ai-powered-tools/media-generation#color-background) or [Generate](https://help.shopify.com/en/manual/ai-powered-tools/media-generation#generate), click **Save** or **Save as new** to save your image.
  2. Click the thumbnail for the image you want to save.
  3. In the image preview, click the **↧** icon to download the image to your device's local storage.

Mobile
  1. Follow the steps to use [Color background](https://help.shopify.com/en/manual/ai-powered-tools/media-generation#color-background) or [Generate](https://help.shopify.com/en/manual/ai-powered-tools/media-generation#generate), and tap **Save** or **Save as new** to save your image.
  2. In the image preview, tap the ![Horizontal menu](https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/MenuHorizontalIcon.svg) > **↧** icon to download or share the image.


## Report the content in generated images
Media generation uses trained models that implement filters and safeguards to recognize and block harmful or offensive content. However, you can manually report any generated images that still contain inappropriate or harmful content. Your feedback helps improve the quality of scenes generated by media generation.
#### Note
Shopify prioritizes originality and respects creators' rights, and doesn't support or endorse uploading images from the web or copyright infringement.
To report potential infringement, rights holders can use Shopify's existing copyright and trademark reporting forms. Learn more about [_Legal removals and intellectual property_](https://help.shopify.com/en/manual/compliance/intellectual-property).
### Steps:
After you've generated images using [Generate](https://help.shopify.com/en/manual/ai-powered-tools/media-generation#generate) and encountered inappropriate or harmful content:
  1. Click the report icon in the bottom corner of the image.
  2. Choose the reason for reporting.
  3. Click **Submit**.


Desktop
  1. Click the thumbnail for the image that you want to report.
  2. In the image preview, click the ⚐ flag icon to **Report content**.
  3. In the **Report image** dialog, select what you want to report about the image.
  4. Optional: In the **Add more details** section, enter specific information about what you want to report.
  5. Click **Submit**.

Mobile
  1. Tap the thumbnail for the image that you want to report.
  2. In the image preview, tap ![Horizontal menu](https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/MenuHorizontalIcon.svg) > **Report image**.
  3. In the **Report image** dialog, select what you want to report about the image.
  4. Optional: In the **Add more details** section, enter specific information about what you want to report.
  5. Tap **Submit**.


## Frequently Asked Questions
### How do I report issues with generated images?
You can report any image directly from the image editor by [using the Report content feature](https://help.shopify.com/en/manual/ai-powered-tools/media-generation#report-image).
### What is the source of generated images and how is copyright handled?
Media generation relies on multiple generative media models and follows Shopify's privacy and data protection principles.
Rights holders can report potential infringement using the [copyright and trademark reporting forms](https://help.shopify.com/en/manual/compliance/intellectual-property).
### What are the ownership and usage rights for AI-edited images?
Shopify doesn't claim ownership over images merchants create using media generation, nor restrict where they can use those images. Images created can be used for merchants' business purposes, both within and outside of Shopify.
#### Note
An invisible watermark is applied as a form of 'metadata' on content that's generated with AI, but this is undetectable to the human eye and won't impact the final result of the image.
Leave feedback

