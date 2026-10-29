<!-- SOURCE: https://web.dev/articles/css-size-adjust (fetched 2026-10-29T05:12:49Z via curl + html->text) -->



          Home

          Articles

      CSS size-adjust for @font-face

      Stay organized with collections

      Save and categorize content based on your preferences.

As a web font loads, you can now adjust its scale, to normalize the document font sizes and prevent layout shift when switching between fonts

            Adam Argyle

Consider the following

demo

where the 
font-size
 is a consistent 
64px
, and the only difference between each of these headers is the 
font-family
. The examples on the left have not been adjusted and
have an inconsistent final size. The examples on the right use 
size-adjust
 to
ensure 
64px
 is the consistent final size.

   In this example Chrome DevTools CSS grid layout debug tools are used to show heights.

This post explores a 
new CSS font-face
descriptor
 called

size-adjust
. It also demonstrates a few ways to correct and normalize font sizes
for smoother user experience, consistent design systems and more predictable
page layout. One important use case is optimizing web font rendering to prevent

cumulative layout shift
 (CLS).

Browser Support

        92

        92

        92

        17

Source

Here's an interactive 
demo
 of the
problem space. Try changing the typeface with the dropdown and observe:

The height differences in the results.

Visually jarring content shifts.

Moving interactive target areas (the dropdown jumps around!).

Key term: 
 Font family vs Typeface: A 
typeface
 is referred to by its family name plus its font face. 
Helvetica Bold
 is referring to the specific bold typeface while 
Helvetica
 is generically referring to the entire family of 8+ typefaces (normal, bold, italic, etc). With CSS 
@font-face
 you'll be dealing with typefaces, even though to use them you need to write 
font-family
. 

How to scale fonts with 
size-adjust

An introduction to the syntax:

@
font
-
face

{

font
-
family
:

"Adjusted Typeface"
;

size
-
adjust
:

150
%
;

src
:

url
(
some
/
path
/
to
/
typeface
.
woff2
)

format
(
'
woff2
'
);

}

Creates a custom typeface named 
Adjusted Typeface
.

Uses 
size-adjust
 to scale up each glyph to 150% their default size.

Affects only the single imported typeface.

Use the above custom typeface like this:

h1

{

font-family
:

"Adjusted Typeface"
;

}

Warning: 
 If the second headline in the above demo is not larger than the first one, your browser does not support 
size-adjust
. 

Mitigating CLS with seamless font swapping

In the following gif, watch the examples on the left and how there's a shift
when the font is changed. This is just a small example with a single headline
element and the issue is very noticeable.

    The example on the left has layout shift, the one on the right does not.

To improve font rendering, a great technique is 
font
swapping
. Render a quick-loading
system font to show the content first, then swap that with a web font when
the web font finishes loading. This gives you the best of both worlds: the
content is visible as soon as possible, and you get a nicely styled page without
sacrificing your user's time to content. The problem however, is that sometimes
when the web font loads, it shifts the entire page around since it presents at a
slightly different box height size.

    more content equals more potential layout shift when font swaps

By putting 
size-adjust
 in the 
@font-face
 rule, it sets a global glyph
adjustment for the font face. Timing this right will lead to minimal visual
change, a seamless swap. To create a seamless swap, hand adjust or try this

size-adjust
calculator

by 
Malte Ubl
.

    Choose a 
Google Web Font
, get back a pre-adjusted 
@font-face
 snippet.

At the beginning of this post, fixing the font size issue was done by trial and
error. 
size-adjust
 was nudged in the source code until the same header in

Cookie
 and 
Arial
 rendered the same 
64px
 as 
Press Start 2P
 did naturally.
I aligned two fonts to a target font size.

@
font-face

{

font-family
:

'Adjusted Arial'
;

size-adjust
:

86
%;

src
:

local
(
Arial
);

}

@
font-face

{

font-family
:

'Cookie'
;

size-adjust
:

90
.
25
%;

src
:

url
(..
.
woff2
)

format
(
'woff2'
);

}

Calibrating fonts

You as the author determine the calibration target(s) for normalizing font
scale. You might normalize on Times, Arial, or a system font, then adjust custom
fonts to match. Or, you might adjust local fonts to match what you download.

Strategies for 
size-adjust
 calibration:

Remote target:
Adjust local fonts towards downloaded fonts.

Local target:
Adjust downloaded fonts towards local target fonts.

Example 1: Remote target

Consider the following snippet which adjusts a locally available font to size
match a remote src custom font. A remote custom font is the target for
calibration, a brand font perhaps:

@
font-face

{

font-family
:

"Adjusted Regular Arial For Brand"
;

src
:

local
(
Arial
);

size-adjust
:

90
%;

}

@
font-face

{

font-family
:

"Rad Brand"
;

src
:

url
(
some
/
path
/
to
/
a
.
woff2
)

format
(
'woff2'
);

}

html

{

font-family
:

"Rad Brand"
,

"Adjusted Regular Arial For Brand"
;

}

In this example, local font Arial is adjusting in anticipation of a loaded custom font, for a
seamless swap.

This strategy has an advantage of offering designers and developers the same
font for sizing and typography. 
The brand is the calibration target.
 This is
great news for design systems.

Having a brand typeface as the target is also how Malte's calculator works.
Choose a Google Font and it will calculate how to adjust Arial to seamlessly
swap with it. Here's an example of Roboto CSS from 
the
calculator
,
where Arial is loaded and named "Roboto-fallback":

@
font-face

{

font-family
:

"Roboto-fallback"
;

size-adjust
:

100
.
06
%;

src
:

local
(
"Arial"
);

}

Warning: 
 The order of 
font-family
 is critical. It's where order and priority go. Ensure the typeface you want the most, is first. Furthermore, 
local(Arial)
 may not be available on all your user's devices, therefore it's important to provide multiple fallbacks in the font-family. 

To create a fully cross platform adjustment, see the following example which provides 2 adjusted local fallback fonts in anticipation of a brand font.

@
font-face

{

font-family
:

"Roboto-fallback-1"
;

size-adjust
:

100
.
06
%;

src
:

local
(
"Arial"
);

}

@
font-face

{

font-family
:

"Roboto-fallback-2"
;

size-adjust
:

99
.
94
%;

src
:

local
(
"Arimo"
);

}

@
font-face

{

font-family
:

"Roboto Regular"
;

src
:

url
(
some
/
path
/
to
/
roboto
.
woff2
)

format
(
'woff2'
);

}

html

{

font-family
:

"Roboto Regular"
,

"Roboto-fallback-1"
,

"Roboto-fallback-2"
;

}

Example 2: Local target

Consider the following snippet which adjusts a brand custom font to match Arial:

@font
-
face

{

font
-
family
:

"Rad Brand - Adjusted For Arial"
;

src
:

url
(
some
/
path
/
to
/
a
.
woff2
)

format
(
'woff2'
);

size
-
adjust
:

110
%
;

}

html

{

font
-
family
:

"Rad Brand - Adjusted For Arial"
,

Arial
;

}

This strategy has the advantage of rendering without any adjustments, then
adjusting any incoming fonts to match.

Finer tuning with 
ascent-override
, 
descent-override
 and 
line-gap-override

If generic scaling of glyphs isn't enough adjustment for your design or loading
strategies, here are some finer tuning options that work along with

size-adjust
. The

ascent-override
,

descent-override
,
and

line-gap-override

properties are currently implemented in Chromium 87+, and Firefox 89+.

ascent-override

Browser Support

        87

        87

        89

Source

The 
ascent-override
 descriptor defines the height above the baseline of a
font.

@
font-face

{

font-family
:

"Ascent Adjusted Arial Bold"
;

src
:

local
(
Arial

Bold
);

ascent-override
:

71
%;

}

The red headline (unadjusted) has space above it's capital letter A and O, while
the blue headline has been adjusted so it's 
cap
height
 fits snug against the overall
bounding box.

descent-override

Browser Support

        87

        87

        89

Source

The 
descent-override
 descriptor defines the height below the baseline of the
font.

@
font-face

{

font-family
:

"Ascent Adjusted Arial Bold"
;

src
:

local
(
Arial

Bold
);

descent-override
:

0
%;

}

The red headline (unadjusted) has space below it's D and O

baselines
, while the blue
headline has been adjusted so it's letters rest snug on the baseline.

line-gap-override

Browser Support

        87

        87

        89

Source

The 
line-gap-override
 descriptor defines the line-gap metric for the font.
 This is the font recommended line-gap or external leading.

@
font-face

{

font-family
:

"Line Gap Adjusted Arial"
;

src
:

local
(
Arial
);

line-gap-override
:

50
%;

}

The red headline (unadjusted) has no 
line-gap-override
, essentially it's at

0%
, while the blue headline has been adjusted up by 50%, creating space above
and below the letters accordingly.

Putting it all together

Each of these overrides offer an additional way to trim excess from the web's
safe text bounding box. You can tailor the text box for precise presentation.

Warning: 
 If any of the above demos aren't showing differences, your browser does not support the overrides. 

Conclusion

The 
@font-face

size-adjust
 CSS feature is an exciting way to customize the
text bounding box of your web layouts to improve the font swapping experience
thus avoiding layout shift for your users. To learn more, check out these
resources:

CSS Fonts Level 5
Spec

Size Adjust on
MDN

Seamless swap @font-face
generator

Cumulative Layout Shift (CLS) on web.dev

A New Way To Reduce Font Loading Impact: CSS Font Descriptors

Except as otherwise noted, the content of this page is licensed under the 
Creative Commons Attribution 4.0 License
, and code samples are licensed under the 
Apache 2.0 License
. For details, see the 
Google Developers Site Policies
. Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2021-06-09 UTC.


