<!-- SOURCE: https://developer.mozilla.org/en-US/docs/Web/CSS/@font-face/font-display (fetched 2026-10-29T05:16:07Z via curl + html->text) -->



font-display
 CSS at-rule descriptor

          Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since January 2020.

              See full compatibility

              Learn more

The 
font-display
 descriptor for the 
@font-face
 at-rule determines how a font face is displayed based on whether and when it is downloaded and ready to use.

Syntax

css
/* Keyword values */
font-display: auto;
font-display: block;
font-display: swap;
font-display: fallback;
font-display: optional;

Values

auto

The font display strategy is defined by the user agent.

block

Gives the font face a short block period and an infinite swap period.

swap

Gives the font face an extremely small block period and an infinite swap period.

fallback

Gives the font face an extremely small block period and a short swap period.

optional

Gives the font face an extremely small block period and no swap period.

Note:

In Firefox, the preferences 
gfx.downloadable_fonts.fallback_delay

and 
gfx.downloadable_fonts.fallback_delay_short
 provide the duration
of the "short" and "extremely small" periods, respectively.

Description

The font display timeline is based on a timer that begins the moment the user agent attempts to use a given downloaded font face. The timeline is divided into the three periods below which dictate the rendering behavior of any elements using the font face:

Font block period: If the font face is not loaded, any element attempting to use it must render an 
invisible
 fallback font face. If the font face successfully loads during this period, it is used normally.

Font swap period: If the font face is not loaded, any element attempting to use it must render a fallback font face. If the font face successfully loads during this period, it is used normally.

Font failure period: If the font face is not loaded, the user agent treats it as a failed load causing normal font fallback.

Formal definition

Related 
at-rule
@font-face
Initial value
auto
Computed value
as specified

Formal syntax

font-display = 

auto

|

block

|

swap

|

fallback

|

optional

Examples

Specifying fallback font-display

css
@font-face {
  font-family: "ExampleFont";
  src: url("/path/to/fonts/example-font.woff2") format("woff2");
  font-weight: normal;
  font-style: normal;
  font-display: fallback;
}

Specifications

            Specification

CSS Fonts Module Level 4
# font-display-desc

Browser compatibility

See also

font-family

font-stretch

font-style

font-weight

font-feature-settings

font-variation-settings

src

unicode-range

            Help improve MDN

Learn how to contribute

    This page was last modified on 
Sep 10, 2026
 by 
MDN contributors
.

View this page on GitHub
 • 
Report a problem with this content


