<!-- SOURCE: https://developer.mozilla.org/en-US/docs/Web/CSS/@font-face/ascent-override (fetched 2026-10-29T05:12:50Z via curl + html->text) -->



ascent-override
 CSS at-rule descriptor

          Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.
Want more browser support for this feature? 
Tell us why.

              See full compatibility

              Learn more

The 
ascent-override

CSS
 descriptor for the 
@font-face
 at-rule defines the ascent metric for the font. The ascent metric is the height above the baseline that CSS uses to lay out line boxes in an inline formatting context.

Syntax

css
ascent-override: normal;
ascent-override: 90%;

Values

normal

The default value. When used the metric value is obtained from the font file.

<percentage>

A 
<percentage>
 value.

Formal definition

Related 
at-rule
@font-face
Initial value
normal
Percentages
as specified
Computed value
as specified

Formal syntax

ascent-override = 

[

normal

|

<percentage [0,∞]>

]
{1,2}

Examples

Overriding metrics of a fallback font

The 
ascent-override
 property can help when overriding the metrics of a fallback font to better match those of a primary web font.

css
@font-face {
  font-family: "web-font";
  src: url("https://example.com/font.woff");
}

@font-face {
  font-family: "local-font";
  src: local("Local Font");
  ascent-override: 125%;
}

Specifications

            Specification

CSS Fonts Module Level 4
# font-metrics-override-desc

Browser compatibility

See also

descent-override

font-display

font-family

font-weight

font-style

font-stretch

font-feature-settings

font-variation-settings

line-gap-override

src

size-adjust

unicode-range
 descriptor

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


