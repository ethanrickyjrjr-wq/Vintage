<!-- SOURCE: https://developer.mozilla.org/en-US/docs/Web/CSS/font-optical-sizing (fetched 2026-10-29T05:10:51Z via curl + html->text) -->



font-optical-sizing
 CSS property

          Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since March 2020.

              See full compatibility

              Learn more

The 
font-optical-sizing

CSS
 property sets whether text rendering is optimized for viewing at different sizes.

Try it

font-optical-sizing: auto;

font-optical-sizing: none;

<section id="default-example">
  <div id="example-element">
    <h2>Chapter 3</h2>
    <p>
      On this particular Thursday, something was moving quietly through the
      ionosphere many miles above the surface of the planet; several somethings
      in fact, several dozen huge yellow chunky slablike somethings, huge as
      office blocks, silent as birds.
    </p>
  </div>
</section>

@font-face {
  src: url("/shared-assets/fonts/variable-fonts/AmstelvarAlpha-VF.woff2");
  font-family: "Amstelvar";
  font-style: normal;
}

#example-element {
  font-family: "Amstelvar", serif;
  text-align: left;
}

#example-element h2 {
  font-size: 36px;
}

#example-element p {
  font-size: 12px;
}

Syntax

css
/* keyword values */
font-optical-sizing: none;
font-optical-sizing: auto; /* default */

/* Global values */
font-optical-sizing: inherit;
font-optical-sizing: initial;
font-optical-sizing: revert;
font-optical-sizing: revert-layer;
font-optical-sizing: unset;

Values

This property is specified as one of the following keyword values:

none

The browser will not modify the shape of glyphs for optimal viewing.

auto

The browser will modify the shape of glyphs for optimal viewing.

Description

Optical sizing is enabled by default for fonts that have an optical size variation axis. The optical size variation axis is represented by 
opsz
 in 
font-variation-settings
.

When optical sizing is used, small text sizes are often rendered with thicker strokes and larger serifs, whereas larger text is often rendered more delicately with more contrast between thicker and thinner strokes.

Formal definition

Initial value
auto
Applies to
all elements and text. It also applies to 
::first-letter
 and 
::first-line
.
Inherited
yes
Computed value
as specified
Animation type
discrete

Formal syntax

font-optical-sizing = 

auto

|

none

Examples

Disabling optical sizing

html
<p class="optical-sizing">
  This paragraph is optically sized. This is the default across browsers.
</p>

<p class="no-optical-sizing">
  This paragraph is not optically sized. You should see a difference in
  supporting browsers.
</p>

css
@font-face {
  src: url("AmstelvarAlpha-VF.woff2");
  font-family: "Amstelvar";
  font-style: normal;
}

p {
  font-size: 36px;
  font-family: "Amstelvar", serif;
}

.no-optical-sizing {
  font-optical-sizing: none;
}

Note:

The font referenced above — which includes optical sizing and is freely-licensed — is good for testing. You can 
download it on GitHub
.

Specifications

            Specification

CSS Fonts Module Level 4
# font-optical-sizing-def

Browser compatibility

See also

font-size

font-size-adjust

Learn: Fundamental text and font styling

            Help improve MDN

Learn how to contribute

    This page was last modified on 
Sep 17, 2026
 by 
MDN contributors
.

View this page on GitHub
 • 
Report a problem with this content


