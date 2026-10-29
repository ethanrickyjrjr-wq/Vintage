<!-- SOURCE: https://fonts.google.com/knowledge/glossary/optical_size_axis (crawl4ai via tools/crawl.sh, 2026-10-29) -->
[ Skip to content ](https://fonts.google.com/main-content)
[font_downloadFonts](https://fonts.google.com/)[languageNoto](https://fonts.google.com/noto)[interestsIcons](https://fonts.google.com/icons)[schoolKnowledge](https://fonts.google.com/knowledge)[helpFAQ](https://fonts.google.com/faq)
dark_mode
close
  * [Overview](https://fonts.google.com/knowledge)
  * Sections 
  * [Glossary](https://fonts.google.com/knowledge/glossary)


[](https://fonts.google.com/)
shopping_bag
View selected families.  Dismiss 
menu Sections 
  1. [Knowledge](https://fonts.google.com/knowledge)chevron_right
  2. [Glossary](https://fonts.google.com/knowledge/glossary)chevron_right
  3. Optical Size axis (opsz) 


# Optical Size axis (opsz)
“Optical Size” (controlled with `font-optical-sizing` or `font-variation-setting: ‘opsz’ VALUE` in CSS) is an [axis](https://fonts.google.com/knowledge/glossary/axis_in_variable_fonts) found in some [variable fonts](https://fonts.google.com/knowledge/glossary/variable_fonts). It controls the [font](https://fonts.google.com/knowledge/glossary/font) file’s [optical size](https://fonts.google.com/knowledge/glossary/optical_sizes) optimizations.
The [Google Fonts CSS v2 API](https://developers.google.com/fonts/docs/css2) defines the axis as:  
| Default:  | Min:  | Max:  | Step:  |  
| --- | --- | --- | --- |  
| 14  | 6  | 144  | 0.1  |  
![Two side-by-side type specimens of the word “glaze”, each shown with a variable axis represented beneath as a horizontal slider. The first specimen, with the slider most of the way to the left to represent a lower value on the axis, shows a small \(or body-like\) optical size. The second specimen, with the slider most of the way to the right to represent a higher value on the axis, shows a large \(or display-like\) optical size, with a shorter x-height and greater stroke contrast.](https://fonts.gstatic.com/s/img/knowledge/glossary/terms/optical_size_axis/images/thumbnail_439626857.svg)
Typeface: [Amstelvar](https://github.com/googlefonts/amstelvar)
Optical sizes in a variable font are different versions of a [typeface](https://fonts.google.com/knowledge/glossary/typeface) optimized for use at singular specific sizes, such as 14 pt or 144 pt. Small (or [body](https://fonts.google.com/knowledge/glossary/body)) optical sizes tend to have less [stroke](https://fonts.google.com/knowledge/glossary/stroke) [contrast](https://fonts.google.com/knowledge/glossary/contrast), more open and wider spacing, and a taller [x-height](https://fonts.google.com/knowledge/glossary/x_height) than those of their large (or [display](https://fonts.google.com/knowledge/glossary/display)) counterparts.
The concept is that the numeric value for this axis should match the rendered font size in typographic points (1/72nd of an inch) in print, although browsers instead match it to the CSS `px` unit, since they have no concept of physical size. A new CSS attribute was introduced to go along with it: `font-optical-sizing`. The default is `auto`, and this is supported behavior in all modern browsers.

```
body {
  font-optical-sizing: auto;
}

```

We can force it to `none` if we’d prefer to turn it off, or we can set an explicit `px` value by using `font-variation-settings`, like so:

```
body {
  font-variation-settings: 'opsz' 16;
}
h1 {
  font-variation-settings: 'opsz' 48;
}

```

The changes made across an Optical Size axis are intended by typeface designers to optimize the type, but parametric axes can be used to further adjust and fine-tune things. Explore more in our article, [“Introducing parametric axes.”](https://fonts.google.com/lesson/introducing_parametric_axes)
In line with the current CSS spec, the four-character code for this axis should be referenced in lowercase (as only the five axes registered in the OpenType format specification should appear in lowercase). Also, when using the Google Fonts API, the lowercase axes have to appear first in the URL, followed by the uppercase, each in alphabetical order.
#  Related articles 
[![](https://fonts.gstatic.com/s/img/knowledge/modules/introducing_type/lessons/introducing_variable_fonts/images/thumbnail_411126311.svg) Introducing variable fonts  ](https://fonts.google.com/knowledge/introducing_type/introducing_variable_fonts)[![](https://fonts.gstatic.com/s/img/knowledge/modules/using_type/lessons/designing_with_variable_fonts_in_desktop_apps/images/thumbnail_411126311.svg) Designing with variable fonts in desktop apps  ](https://fonts.google.com/knowledge/using_type/designing_with_variable_fonts_in_desktop_apps)[![](https://fonts.gstatic.com/s/img/knowledge/modules/using_type/lessons/styling_type_on_the_web_with_variable_fonts/images/thumbnail_411126311.svg) Styling type on the web with variable fonts  ](https://fonts.google.com/knowledge/using_type/styling_type_on_the_web_with_variable_fonts)
## License
This content is owned by Google and is licensed under [Creative Commons: CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)
To contribute, see the source files on [ GitHub ](https://github.com/google/fonts/tree/main/cc-by-sa/knowledge/glossary/terms/optical_size_axis)
Google Fonts makes it easy to bring personality and performance to your websites and products. Our robust catalog of open-source fonts and icons makes it easy to integrate expressive type and icons seamlessly — no matter where you are in the world. 
  * [ About us Making the web more beautiful, fast, and open through great typography & icons  ](https://fonts.google.com/about)
  * [ Fonts GitHub This repository contains the binary font files served by Google Fonts  ](https://github.com/google/fonts)
  * [ Icons GitHub This repository contains the binary font files served by Google Icons  ](https://github.com/google/material-design-icons)


  * [ Fonts blog This blog has stories about how different fonts were designed for various languages and scripts  ](https://fonts.googleblog.com/)
  * [ Material Design A cross-platform design system for creating high-quality digital experiences  ](https://m3.material.io/styles/typography/overview)
  * [ Google Design Google Design highlights the breadth and craft of design and fonts from speculation, to work-in-progress, to finished product  ](https://design.google/tags/typography)


[ Privacy ](https://policies.google.com/privacy?hl=en)[ Terms of service ](https://policies.google.com/terms?hl=en)
feedback

