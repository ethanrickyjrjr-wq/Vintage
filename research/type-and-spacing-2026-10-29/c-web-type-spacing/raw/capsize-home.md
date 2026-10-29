<!-- SOURCE: https://seek-oss.github.io/capsize/ (curl, 2026-10-29) -->
<!-- SOURCE: https://seek-oss.github.io/capsize/ (fetched 2026-10-29T05:12:51Z via curl + html->text) -->

Capsize
Flipping how we define
typography in CSS
Capsize makes the sizing and layout of text as predictable as every other element on the screen.
Using font metadata, text can now be sized according to the height of its capital letters while trimming the space above capital letters and below the baseline.
npm install @capsizecss/core
GitHub
1
.

Choose a font
Google Fonts
System
Url
Upload
Google font name
System font name
Choose a system font
-apple-system
Arial
BlinkMacSystemFont
Brush Script
Courier New
Georgia
Helvetica
Helvetica Neue
Lucida Grande
Oxygen
Roboto
Segoe UI
Tahoma
Times New Roman
Trebuchet MS
Verdana
TEST
Font url
Submit
Font file
Browse
Measurements
JSON
Em square (2048)
Cap Height (1456)
Descender (500)
Ascender (1900)
Line Height
Hg
{
  familyName: "Roboto",
  fullName: "Roboto Regular",
  postscriptName: "Roboto-Regular",
  category: "sans-serif",
  capHeight: 1456,
  ascent: 1900,
  descent: -500,
  lineGap: 0,
  unitsPerEm: 2048,
  xHeight: 1082,
  xWidthAvg: 911,
  subsets: {
    latin: {
      xWidthAvg: 911
    },
    thai: {
      xWidthAvg: 908
    }
  }
}
2
.

Adjust size & spacing
Snap to grid?
Cap Height
Font Size
Line Gap
Leading
Lorem ipsum Lolor sit amet, Lonsectetur adipiscing elit. Duis eu ornare nisi, sed feugiat metus. Pellentesque rutrum vel metus non dignissim. Aenean egestas neque mattis mi maximus luctus. Praesent et commodo dui, nec eleifend lectus. Pellentesque blandit nisi tellus, id efficitur urna consectetur id. Sed convallis tempor dui vel aliquet.
3
.

Apply the styles
JavaScript
CSS
import { createStyleObject } from '@capsizecss/core';
import fontMetrics from '@capsizecss/metrics/roboto';

const styles = createStyleObject({
  capHeight: 48,
  lineGap: 24,
  fontMetrics
});

.capsizedText {
  font-size: 67.5165px;
  line-height: 72px;
}

.capsizedText::before {
  content: "";
  margin-bottom: -0.1641em;
  display: table;
}

.capsizedText::after {
  content: "";
  margin-top: -0.1914em;
  display: table;
}
FAQs
#
Why use pseudo elements instead of applying the negative margin directly?
The negative margins are applied to pseudo elements to guard against

margin collapse
. Combining the use of pseudo elements and padding on the parent container prevents the margins from being collapsed into the parent element. The collapsing is most visible when text is used directly inside a container that has a background colour applied.
What is the recommended way to handle metrics for fallback fonts?
Until the trimming of leading and trailing white space around text is natively supported in CSS, supporting fallback fonts perfectly will have its trade-offs.
Typically the font stack should not specify wildly different font families as fallbacks, and in practice that means the cap heights and descenders should have similar scales proportionate to their font. While not having a pixel-perfect match to the font, it should still perform the trim effectively enough.
For web fonts that are more display focused, using a library such as

webfontloader

would allow applying fallback metrics as a separate class.
What is the recommended way to handle text overflow/truncation?
Applying standard text overflow techniques on the same element will result in descenders/ascenders getting cut off due to the overflow needing to be hidden, e.g.:
.truncate {
  text-overflow: ellipsis;
  overflow: hidden;
  white-space: nowrap;
}
Ideally you should not be adding further layout-related styles to the element that is capsized to prevent styles possibly clashing with the trim. We handle this by applying the truncation styles to a block level span element, e.g.:
<p class="capsizedText">
  <span class="truncate">
    ...
  </span>
</p>
If using a component system you can conditionally add the span only when using truncation.
What does this mean for diacritic and accent marks in non-Latin alphabets?
Diacritics and accent marks

can have an impact on the perceived cap height and baseline. Given the location of the marks being at the extremities of the fonts line box, it is necessary to increase the white space by increasing the

line-height

and container

padding

to accomodate. This is the case today even without using Capsize.
What can browser vendors do to make this easier?
Over time more of Capsize’s text trimming capabilities are being built into the browsers and available using standard CSS properties.
The

text-box

CSS property is now being implemented, meaning the required CSS for trimming the line box to cap height would be:
.capsizedText {
  text-box: trim-both cap alphabetic;
}
Since Capsize was first built,

cap

units are now available natively in CSS across all major browsers.
Currently, there is no proposal for a way to define the

line-height

using the

lineGap

style mental model. With the rise of properties like

gap

for CSS grid and flexbox, maybe this will feed into a future proposal.
