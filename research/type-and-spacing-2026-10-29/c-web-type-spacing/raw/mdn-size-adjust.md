<!-- SOURCE: https://developer.mozilla.org/en-US/docs/Web/CSS/@font-face/size-adjust (fetched 2026-10-29T05:12:50Z via curl + html->text) -->



size-adjust
 CSS at-rule descriptor

          Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2023.

              See full compatibility

              Learn more

The 
size-adjust

CSS
 descriptor for the 
@font-face
 at-rule defines a multiplier for glyph outlines and metrics associated with this font. This makes it easier to harmonize the designs of various fonts when rendered at the same font size.

The 
size-adjust
 descriptor behaves in a similar fashion to the 
font-size-adjust
 property. It calculates an adjustment per font by matching ex heights.

Syntax

css
size-adjust: 90%;

Values

<percentage>

A 
<percentage>
 value with an initial value of 100%.

All metrics associated with this font are scaled by the given percentage. This includes glyph advances, baseline tables, and overrides provided by 
@font-face
 descriptors.

Formal definition

Related 
at-rule
@font-face
Initial value
100%
Percentages
as specified
Computed value
as specified

Formal syntax

size-adjust = 

<percentage [0,∞]>

Examples

Overriding metrics of a fallback font

The 
size-adjust
 property can help when overriding the metrics of a fallback font to better match those of a primary web font.

css
@font-face {
  font-family: "web-font";
  src: url("https://example.com/font.woff");
}

@font-face {
  font-family: "local-font";
  src: local("Local Font");
  size-adjust: 90%;
}

Specifications

            Specification

CSS Fonts Module Level 5
# size-adjust-desc

Browser compatibility

See also

font-display
 descriptor

font-family
 descriptor

font-weight
 descriptor

font-style
 descriptor

font-stretch
 descriptor

font-feature-settings

font-variation-settings
 descriptor

src
 descriptor

unicode-range
 descriptor

font-size-adjust
 property

            Help improve MDN

Learn how to contribute

    This page was last modified on 
Apr 20, 2026
 by 
MDN contributors
.

View this page on GitHub
 • 
Report a problem with this content


