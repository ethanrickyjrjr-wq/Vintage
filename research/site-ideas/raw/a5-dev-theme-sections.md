[Skip to main content](https://shopify.dev/docs/storefronts/themes/architecture/sections#main-content)
[![Docs page](https://shopify-assets.shopifycdn.com/shopifycloud/shopify-dev/production/assets/dev-docs-logo-2-light-D4UI1jxY.svg)![Docs page](https://shopify-assets.shopifycdn.com/shopifycloud/shopify-dev/production/assets/dev-docs-logo-2-dark-BQ-Bk9XA.svg)](https://shopify.dev/docs)
  * [Apps](https://shopify.dev/docs/apps/build)
  * [Storefronts](https://shopify.dev/docs/storefronts)
  * [Agents](https://shopify.dev/docs/agents)
  * References
  * [Changelog](https://shopify.dev/changelog)


  * Ask assistant`/`
  * [Help](https://shopify.dev/support)
  * •
  * [Log in](http://dev.shopify.com/dashboard)


Collapse sidebar
Storefronts
  * [Overview](https://shopify.dev/docs/storefronts)


* * *
  * ### Themes
    * [Overview](https://shopify.dev/docs/storefronts/themes)
    * Getting started
    * Key concepts
    * Best practices
    * Agentic workflows
    * Developer Tools
    * Theme features
    * Sell themes
  * ### Headless
    * [Overview](https://shopify.dev/docs/storefronts/headless/overview)
    * [Building with mock.shop ](https://shopify.dev/docs/storefronts/headless/mock-shop)
  * ### Hydrogen
    * [Overview](https://shopify.dev/docs/storefronts/hydrogen)
    * Getting started
    * Data fetching
    * Request handling
    * Products and collections
    * Cart
    * [Customer accounts](https://shopify.dev/docs/storefronts/hydrogen/customer-accounts)
    * [Markets](https://shopify.dev/docs/storefronts/hydrogen/markets)
    * [Analytics and consent](https://shopify.dev/docs/storefronts/hydrogen/analytics)
    * Deploy
    * [Hydrogen CLI commands](https://shopify.dev/docs/api/shopify-cli/hydrogen)
    * [Hydrogen API reference](https://shopify.dev/docs/api/hydrogen)
    * [Migrate to the latest version of Hydrogen](https://shopify.dev/docs/storefronts/hydrogen/migrate)
    * Legacy Hydrogen
  * ### Mobile
    * [Overview](https://shopify.dev/docs/storefronts/mobile)
    * Checkout Kit
    * Accelerated checkouts
    * Mobile storefronts
  * ### Bring your own stack
    * [Overview](https://shopify.dev/docs/storefronts/headless/bring-your-own-stack)
    * Building with the Storefront API
    * Building with the Customer Account API
    * [Headless with B2B](https://shopify.dev/docs/storefronts/headless/bring-your-own-stack/b2b)
    * Shopify Plugin for WordPress
    * [Storefront Web Components](https://shopify.dev/docs/api/storefront-web-components)
    * Additional SDKs


Full index
ExpandOn this page
  * [Location](https://shopify.dev/docs/storefronts/themes/architecture/sections#location)
  * [Content](https://shopify.dev/docs/storefronts/themes/architecture/sections#content)
  * [Usage](https://shopify.dev/docs/storefronts/themes/architecture/sections#usage)


# Sections
Install AI ToolkitAsk about this pageCopy MD
Sections are Liquid files that allow you to create reusable modules of content that can be customized by merchants. They can also include [blocks](https://shopify.dev/docs/storefronts/themes/architecture/sections/section-schema#blocks) which allow merchants to add, remove, and reorder content within a section.
For example, you can create an **Image with text** section that displays an image and text side-by-side with options for merchants to choose the image, set the text, and select the display order.
Sections can be dynamically added to pages using [JSON templates](https://shopify.dev/docs/storefronts/themes/architecture/templates/json-templates) or [section groups](https://shopify.dev/docs/storefronts/themes/architecture/section-groups), giving merchants flexibility to easily customize page layouts. Sections that are included in JSON templates or section groups can support [app blocks](https://shopify.dev/docs/storefronts/themes/architecture/blocks/app-blocks), which give merchants the option to include app content within a section without having to edit theme code. JSON templates and section groups can render up to 25 sections, and each section can have up to 50 [blocks](https://shopify.dev/docs/storefronts/themes/architecture/sections/section-schema#blocks).
Sections can also be [included statically](https://shopify.dev/docs/storefronts/themes/architecture/sections#statically-render-a-section), which can provide merchants with in-context customization options for static content.
By default, sections are available for any template or section group. You can limit which templates and section groups have access in the [section schema](https://shopify.dev/docs/storefronts/themes/architecture/sections/section-schema).
The following diagram shows the main theme architecture components with sections highlighted in blue and blocks highlighted in red:
![Diagram of theme architecture components with sections highlighted in blue and blocks highlighted in red.](https://shopify-assets.shopifycdn.com/shopifycloud/shopify-dev/production/assets/assets/images/themes/architecture/section-and-block-BGj5HnqS.png)
* * *
## 
[Anchor to Location](https://shopify.dev/docs/storefronts/themes/architecture/sections#location)Location
Section files are located in the `sections` directory of the theme:
Copy
1
2
3
4
5
└── theme
...
├── templates
├── sections
...
* * *
## 
[Anchor to Content](https://shopify.dev/docs/storefronts/themes/architecture/sections#content)Content
Sections can contain three main types of content:  
| Type  | Description  | Required  |  
| --- | --- | --- |  
| **Main content**  |  Any HTML or Liquid content you might want to include in the section. Sections have the same access to [global objects](https://shopify.dev/docs/api/liquid/objects), [tags](https://shopify.dev/docs/api/liquid/tags), and [filters](https://shopify.dev/docs/api/liquid/filters) as other Liquid theme files, as well as the following section-specific objects:
  * **The[`section` object](https://shopify.dev/docs/api/liquid/objects/section)** - Contains the section's properties and setting values.
  * **The[`block` object](https://shopify.dev/docs/api/liquid/objects/block)** - Contains the properties and setting values of a single section block.

Aside from global objects, variables created outside of sections aren't accessible within sections. The section and block objects, as well as variables created within sections, aren't available outside of their respective section. The only exception is when you reference section and block objects within a snippet that's rendered inside the section you're referencing.  | No  |  
| **Assets**  |  Sections can bundle their own JavaScript and stylesheet assets with the following section-specific Liquid tags:
  * [`{% javascript %}`](https://shopify.dev/docs/storefronts/themes/best-practices/javascript-and-stylesheet-tags#javascript)
  * [`{% stylesheet %}`](https://shopify.dev/docs/storefronts/themes/best-practices/javascript-and-stylesheet-tags#stylesheet)

To learn more, refer to [Section assets](https://shopify.dev/docs/storefronts/themes/best-practices/javascript-and-stylesheet-tags).  | No  |  
| **Schema**  |  Sections support the `{% schema %}` Liquid tag. This tag is used to define the following section attributes and settings:
  * [name](https://shopify.dev/docs/storefronts/themes/architecture/sections/section-schema#name)
  * [tag](https://shopify.dev/docs/storefronts/themes/architecture/sections/section-schema#tag)
  * [class](https://shopify.dev/docs/storefronts/themes/architecture/sections/section-schema#class)
  * [limit](https://shopify.dev/docs/storefronts/themes/architecture/sections/section-schema#limit)
  * [settings](https://shopify.dev/docs/storefronts/themes/architecture/sections/section-schema#settings)
  * [blocks](https://shopify.dev/docs/storefronts/themes/architecture/sections/section-schema#blocks)
  * [app blocks](https://shopify.dev/docs/storefronts/themes/architecture/blocks/app-blocks)
  * [max_blocks](https://shopify.dev/docs/storefronts/themes/architecture/sections/section-schema#max_blocks)
  * [presets](https://shopify.dev/docs/storefronts/themes/architecture/sections/section-schema#presets)
  * [defaults](https://shopify.dev/docs/storefronts/themes/architecture/sections/section-schema#default)
  * [locales](https://shopify.dev/docs/storefronts/themes/architecture/sections/section-schema#locales)
  * [enabled_on](https://shopify.dev/docs/storefronts/themes/architecture/sections/section-schema#enabled_on)
  * [disabled_on](https://shopify.dev/docs/storefronts/themes/architecture/sections/section-schema#disabled_on)

To learn more, refer to [Section schema](https://shopify.dev/docs/storefronts/themes/architecture/sections/section-schema).  | Yes  |  
* * *
## 
[Anchor to Usage](https://shopify.dev/docs/storefronts/themes/architecture/sections#usage)Usage
When working with sections, you should familiarize yourself with the following:
  * [How to render a section](https://shopify.dev/docs/storefronts/themes/architecture/sections#render-a-section)
  * [How to integrate sections with the theme editor](https://shopify.dev/docs/storefronts/themes/architecture/sections#integrate-sections-with-the-theme-editor)
  * [Support app blocks](https://shopify.dev/docs/storefronts/themes/architecture/sections#support-app-blocks)


### 
[Anchor to Render a section](https://shopify.dev/docs/storefronts/themes/architecture/sections#render-a-section)Render a section
You can render sections in one of the following ways:
  * Reference the section in a [JSON template](https://shopify.dev/docs/storefronts/themes/architecture/templates/json-templates), or a [section group](https://shopify.dev/docs/storefronts/themes/architecture/section-groups) in a [layout](https://shopify.dev/docs/storefronts/themes/architecture/layouts) file.
  * [Statically render](https://shopify.dev/docs/storefronts/themes/architecture/sections#statically-render-a-section) the section with the `section` Liquid tag.
  * Use the [Section Rendering API](https://shopify.dev/docs/api/ajax/section-rendering).


Tip
If you want to render sections inside a template, then use a JSON template. JSON templates provide more extensive customization options for merchants, and improve the theme editor's performance.
**Tip :**
If you want to render sections inside a template, then use a JSON template. JSON templates provide more extensive customization options for merchants, and improve the theme editor's performance.
#### 
[Anchor to Statically render a section](https://shopify.dev/docs/storefronts/themes/architecture/sections#statically-render-a-section)Statically render a section
Caution
Whenever possible, you should avoid statically rendering sections. Instead, you should reference them in a JSON template or section group. Statically rendered sections can't be removed or reordered by merchants.
**Caution :**
Whenever possible, you should avoid statically rendering sections. Instead, you should reference them in a JSON template or section group. Statically rendered sections can't be removed or reordered by merchants.
You can statically render a section using the Liquid [section tag](https://shopify.dev/docs/api/liquid/tags/section).
For example, to include a section in a [Liquid template](https://shopify.dev/docs/storefronts/themes/architecture/templates/liquid-templates), you can include it with a section tag:
## /templates/customers/register.liquid
Copy
1
{% section 'featured-product' %}
Note
You can include a statically rendered section in multiple theme files. However, only one instance of the section exists. If you change section settings in one location, then the change will be applied to all locations where the section is rendered.
**Note :**
You can include a statically rendered section in multiple theme files. However, only one instance of the section exists. If you change section settings in one location, then the change will be applied to all locations where the section is rendered.
### 
[Anchor to Integrate sections with the theme editor](https://shopify.dev/docs/storefronts/themes/architecture/sections#integrate-sections-with-the-theme-editor)Integrate sections with the theme editor
When users customize sections and blocks through the theme editor, their HTML is dynamically added, removed, or re-rendered directly onto the existing DOM, without reloading the entire page. However, any associated JavaScript that runs when the page loads won't run again.
Additionally, you must make sure that when a section or block is selected, that section or block becomes, and remains, visible while it’s selected. For example, a slideshow section should scroll into view when the section is selected, slide to a selected block (slide), and pause while that block is selected.
To help identify theme editor actions like section and block selection or reordering, you can use the [JavaScript events](https://shopify.dev/docs/storefronts/themes/best-practices/editor/integrate-sections-and-blocks#javascript-events) emitted by the theme editor.
You might also want to prevent specific code from running in the theme editor. To do so, you can use Liquid and JavaScript variables for [detecting the theme editor](https://shopify.dev/docs/storefronts/themes/best-practices/editor/integrate-sections-and-blocks#detect-the-theme-editor).
Tip
Section and block files must define [presets](https://shopify.dev/docs/storefronts/themes/architecture/sections/section-schema#presets) in their schema to support being added to JSON templates using the theme editor. Files without presets should be included in the JSON file manually, and can't be removed using the theme editor.
**Tip :**
Section and block files must define [presets](https://shopify.dev/docs/storefronts/themes/architecture/sections/section-schema#presets) in their schema to support being added to JSON templates using the theme editor. Files without presets should be included in the JSON file manually, and can't be removed using the theme editor.
### 
[Anchor to Support app blocks](https://shopify.dev/docs/storefronts/themes/architecture/sections#support-app-blocks)Support app blocks
App blocks allow app developers to create blocks for merchants to add app content to their theme without having to directly edit theme code.
To learn more about how to make your theme compatible with app blocks, refer to [App blocks](https://shopify.dev/docs/storefronts/themes/architecture/blocks/app-blocks).
* * *
Was this page helpful?
YesNo
  * [Location](https://shopify.dev/docs/storefronts/themes/architecture/sections#location)
  * [Content](https://shopify.dev/docs/storefronts/themes/architecture/sections#content)
  * [Usage](https://shopify.dev/docs/storefronts/themes/architecture/sections#usage)


### Updates
  * [Developer changelog](https://shopify.dev/changelog)
  * [Shopify Editions](https://www.shopify.com/editions)


### Business growth
  * [Shopify Partners Program](https://www.shopify.com/partners?shpxid=222dd762-CA08-48FF-E4D4-FF926B8FFCAD)
  * [Shopify App Store](https://apps.shopify.com/?shpxid=222dd762-CA08-48FF-E4D4-FF926B8FFCAD)


### Legal
  * [Terms of service](https://www.shopify.com/legal/terms?shpxid=222dd762-CA08-48FF-E4D4-FF926B8FFCAD)
  * [API terms of use](https://www.shopify.com/legal/api-terms?shpxid=222dd762-CA08-48FF-E4D4-FF926B8FFCAD)
  * [Privacy policy](https://www.shopify.com/legal/privacy?shpxid=222dd762-CA08-48FF-E4D4-FF926B8FFCAD)
  * [Partners Program Agreement](https://www.shopify.com/partners/terms?shpxid=222dd762-CA08-48FF-E4D4-FF926B8FFCAD)


### Shopify
  * [About Shopify](https://www.shopify.com/about?shpxid=222dd762-CA08-48FF-E4D4-FF926B8FFCAD)
  * [Shopify Plus](https://www.shopify.com/plus?shpxid=222dd762-CA08-48FF-E4D4-FF926B8FFCAD)
  * [Careers](https://www.shopify.com/careers?shpxid=222dd762-CA08-48FF-E4D4-FF926B8FFCAD)
  * [Investors](https://investors.shopify.com/home/default.aspx?shpxid=222dd762-CA08-48FF-E4D4-FF926B8FFCAD)
  * [Press and media](https://shopify.com/news?shpxid=7db0d4e4-24E8-4087-58FA-7EE470CA745A)



