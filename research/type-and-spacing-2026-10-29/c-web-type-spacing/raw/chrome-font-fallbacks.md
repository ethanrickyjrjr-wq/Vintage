<!-- SOURCE: https://developer.chrome.com/blog/font-fallbacks (fetched 2026-10-29T05:12:49Z via curl + html->text) -->



          Chrome for Developers

          Blog

      Improved font fallbacks

      Stay organized with collections

      Save and categorize content based on your preferences.

            Katie Hempenius

Summary

This article is a deep dive into font fallbacks and the 
size-adjust
, 
ascent-override
, 
descent-override
, and 
line-gap-override
 APIs. These APIs make it possible to use local fonts to create fallback font faces that closely or exactly match the dimensions of a web font. This reduces or eliminates layout shifts caused by font swapping.

If you’d prefer to skip reading this article, these are some of the tools that you can use to start using these APIs immediately:

Framework tools:

@next/font
: Starting in Next 13, 
next/font
 automatically uses font metric overrides and 
size-adjust
 to provide matching font fallbacks.

@nuxtjs/fontaine
: Starting in Nuxt 3, you can use 
nuxt/fontaine
 to automatically generate and insert matching font fallbacks into the stylesheets used by your Nuxt app.

Non-framework tools:

Fontaine
: Fontaine is a library that automatically generates and inserts font fallbacks that use font metric overrides.

This 
repo
 contains the font metric overrides for all fonts hosted by Google Fonts. These values can be copied and pasted into your stylesheets.

Background

A fallback font is a font face that is used when the primary font face is not loaded yet, or is missing 
glyphs
 necessary to render page content. For example, the CSS below indicates that the 
sans-serif
 font family should be used as the font fallback for 
"Roboto"
.

font-family
:

"Roboto"

,

sans-serif
;

Fallback fonts can be used to render text more quickly (that is, by using 
font-display: swap
). As a result, page content is readable and useful earlier—however, historically, this has come at the cost of layout instability: layout shifts commonly occur when a fallback font is swapped out for the web font. However, the new APIs discussed below can reduce or eliminate this issue by making it possible to create fallback font faces that take up the same amount of space as their web font counterpart.

Improved font fallbacks

There are two possible approaches to generating "improved" font fallbacks. The simpler approach uses only the font metric overrides API. The more complicated (but more powerful) approach uses both the font metric overrides API and 
size-adjust
. This article explains both of these approaches.

How font metric overrides work

Intro

Font metric overrides provide a way to override the ascent, descent, and line-gap of a font:

Ascent
 measures the furthest distance that a font’s glyphs extend above the baseline.

Descent
 measures the furthest distance that a font’s glyphs extend below the baseline.

Line gap
, also called "leading", measures the distance between successive lines of text.

Font metric overrides can be used to override the ascent, descent, and line-gap of a fallback font to match the ascent, descent, and line-gap of the web font. As a result, the web font and the adjusted fallback font will always have the same vertical dimensions.

Font metric overrides are used in a stylesheet like this:

body

{

font-family
:

Poppins
,

"fallback for poppins"
;

}

@
font-face

{

font-family
:

"fallback for poppins"
;

src
:

local
(
"Times New Roman"
);

ascent-override
:

105
%;

descent-override
:

35
%;

line-gap-override
:

10
%;

}

The tools listed at the beginning of this article can generate the correct font metric override values. However, you can also calculate these values yourself.

Calculating font metric overrides

The following equations yield the font metric overrides for a given web font. The values of font metric overrides should be written as percentages (for example, 
105%
) rather than decimals.

ascent-override = ascent/unitsPerEm
descent-override = descent/unitsPerEm
line-gap-override = line-gap/unitsPerEm

Note:

Units per em (UPM)
 refers to the grid size that was used when designing the font. Although there are other grid sizes, 
1000
 (a 1000x1000 grid) or 
2048
 (a 2048x2048 grid) are by far the most popular. It’s important to know UPM in order to put other metrics into perspective. For example, an ascent of 
900
 means very different things depending on whether a font has an UPM of 
1000
 or 
2048
.

For example, these are the font metric overrides for the 
Poppins
 font:

/*

Poppins font metrics:

ascent = 1050

descent = 350

line-gap = 100

UPM: 1000

*/

ascent-override
:

105
%;

/* = 1050/1000 */

descent-override
:

35
%;

/* = 350/1000 */

line-gap-override
:

10
%;

/* = 100/1000 */

The values of 
ascent
, 
descent
, 
line-gap
, and 
unitsPerEm
 all come from the metadata of the web font. The next section of this article explains how to obtain these values.

Reading font tables

A font’s metadata (specifically, its 
font tables
) contains all the information that you’ll need to calculate its font metric overrides.

Using FontForge to view font metadata

Here are some tools you can use to read a font’s metadata:

fontkit
 is a font engine built for Node.js. This 
code snippet
 shows how to use fontkit to calculate font metric overrides.

Capsize
 is a font sizing and layout library. Capsize provides an API for getting information about various font metrics.

fontdrop.info
 is a website that allows you to view font tables and other font-related information from the browser.

Font Forge
 is a popular desktop font editor. To view 
ascent
, 
descent
, and 
line-gap
: open the 
Font Info
 dialog, select the 
OS/2
 menu, then select the 
Metrics
 tab. To view 
UPM
: open the 
Font Info
 dialog, then select the 
General
 menu.

Note:
 Some font-related JavaScript libraries approximate ascent, descent, and line-gap by drawing glyphs to canvas and measuring the result. However, this approach is less accurate than reading the font metrics directly from the font table.

Understanding font tables

You may notice that concepts like "ascent" are referred to by multiple metrics—for example, there are 
hheaAscent
, 
typoAscent
, and 
winAscent
 metrics. This is the result of different operating systems taking different approaches to font rendering: programs on OSX devices generally use 
hhea*
 font metrics—while programs on Windows devices generally use 
typo*
 (also referred to as 
sTypo*
) or 
win*
 font metrics.

Note:
 More specifically, programs on Windows devices typically follow the convention of using 
typo*
 metrics if a font has set 
USE_TYPO_METRICS
 and using 
win*
 metrics if not. 
USE_TYPO_METRICS
 is a boolean parameter that was introduced to allow designers to set a preference between using 
typo*
 and 
win*
 metrics.

Depending on the font, browser, and operating system, a font will be rendered using either 
hhea
, 
typo
, or 
win
 metrics.

Mac

Windows

Chromium

Uses metrics from "hhea" table.

Uses metrics from "typo" table if "USE_TYPO_METRICS" has been set, otherwise uses metrics from "win" table.

Firefox

Uses metrics from "typo" table if "USE_TYPO_METRICS" has been set, otherwise uses metrics from "hhea" table.

Uses metrics from "typo" table if "USE_TYPO_METRICS" has been set, otherwise uses metrics from "win" table.

Safari

Uses metrics from "hhea" table.

Uses metrics from "typo" table if "USE_TYPO_METRICS" has been set, otherwise uses metrics from "win" table.

For more information on how font metrics work across operating systems, see 
this article on vertical metrics
.

Cross-device compatibility

For the vast majority of fonts (for example, ~90% of the fonts hosted by Google Fonts) font metrics overrides can be safely used without knowing the user’s operating system: in other words, for these fonts the values of 
ascent-override
, 
descent-override
, and 
linegap-override
 remain exactly the same regardless of whether 
hhea
, 
typo
, or 
win
 metrics apply. This 
repo
 provides information on which fonts this does and does not apply to.

If you are using a font that requires using separate sets of font metric overrides for OSX and Windows devices, using font metric overrides and 
size-adjust
 is only recommended if you have the ability to vary your stylesheets based on the user’s operating system.

Note:
 This section explains how to determine whether a font uses the same font metric overrides on both OSX and Windows devices.

First, determine if the font has enabled 
USE_TYPO_METRICS
.

If 
USE_TYPO_METRICS
 is enabled, the font will be rendered using 
hhea
 metrics on OSX devices and 
typo
 metrics on Windows devices.

To calculate normal line height on OSX, use the following equation: 
(hheaAscent + hheaDescent + hheaLineGap)/unitsPerEm
.

To calculate normal line height on Windows, use the following equation: 
(typoAscent + typoDescent + typoLineGap)/unitsPerEm
.

If the line height on OSX and Windows are the same, you can use the same font metric overrides for both operating systems.

If 
USE_TYPO_METRICS
 is not enabled, the font will be rendered using 
hhea
 metrics on OSX devices and 
win
 metrics on Windows devices.

To calculate normal line height on OSX, use the following equation: 
(hheaAscent + hheaDescent + hheaLineGap)/unitsPerEm
.

To calculate normal line height on Windows, use the following equation: 
(winAscent + winDescent)/unitsPerEm
. (Note: there is no such thing as 
winLineGap
).

If both of the following conditions are true, you can use the same font metric overrides on OSX and Windows: a) 
hheaLineGap == 0
, b) line height on OSX and Windows are the same.

Using font metric overrides

Because font metric overrides are calculated using measurements that come from the metadata of the web font (and not the fallback font), they stay the same regardless of which font is used as the fallback font. For example:

body

{

font-family
:

"Poppins"
,

"fallback for Poppins"
,

"another fallback for Poppins"
;

}

@
font-face

{

font-family
:

"fallback for Poppins"
;

src
:

local
(
"Arial"
);

ascent-override
:

105
%;

descent-override
:

35
%;

line-gap-override
:

10
%;

}

@
font-face

{

font-family
:

"another fallback for Poppins"
;

src
:

local
(
"Roboto"
);

ascent-override
:

105
%;

descent-override
:

35
%;

line-gap-override
:

10
%;

}

How size-adjust works

Intro

The 
size-adjust
 CSS descriptor proportionally scales the width and height of font glyphs. For example, 
size-adjust: 200%
 scales font glyphs to twice their original size; 
size-adjust: 50%
 scales font glyphs to half their original size.

By itself, 
size-adjust
 has limited applications for improving font fallbacks: in most cases, a fallback font needs to be narrowed or widened slightly (rather than scaled proportionally) in order to match a web font. However, combining 
size-adjust
 with font metric overrides makes it possible to make any two fonts match each other both horizontally and vertically.

This is how 
size-adjust
 is used in stylesheets:

@
font-face

{

font-family
:

"fallback for poppins"
;

src
:

local
(
"Arial"
);

size-adjust
:

60
.
85099821
%;

ascent-override
:

164
.
3358416
%;

descent-override
:

57
.
51754455
%;

line-gap-override
:

16
.
43358416
%;

}

Because of how 
size-adjust
 is calculated (which is explained in the next section), the value of 
size-adjust
 (and the corresponding font metric overrides) changes depending on which fallback font is used:

body

{

font-family
:

"Poppins"
,

"fallback for Poppins"
,

"another fallback for Poppins"
;

}

@
font-face

{

font-family
:

poppins-fallback
;

src
:

local
(
"Arial"
);

size-adjust
:

60
.
85099821
%;

ascent-override
:

164
.
3358416
%;

descent-override
:

57
.
51754455
%;

line-gap-override
:

16
.
43358416
%;

}

@
font-face

{

font-family
:

poppins-fallback-android
;

src
:

local
(
"Roboto"
);

size-adjust
:

55
.
5193474
%:

ascent-override
:

180
.
1173909
%;

descent-override
:

63
.
04108683
%;

line-gap-override
:

18
.
01173909
%;

}

Note:
 Font metric overrides and 
size-adjust
 are both declared using percentages—but these percentages are defined differently: for example, 
size-adjust: 10%
 scales a font to 1/10th its original size; whereas 
ascent-override: 10%
 wouldn’t necessarily make a font smaller—rather, it changes the proportions of the font (that is, the size of the ascent would be equal to 10% of the UPM).

Calculating size-adjust and font metric overrides

These are the equations for calculating 
size-adjust
 and font metric overrides:

size-adjust = avgCharacterWidth of web font / avgCharacterWidth of fallback font
ascent-override = web font ascent / (web font UPM * size-adjust)
descent-override = web font descent / (web font UPM * size-adjust)
line-gap-override = web font line-gap / (web font UPM * size-adjust)

Most of these inputs (that is, ascent, descent, and line-gap) can be read directly from the web font’s metadata. However, 
avgCharacterWidth
 needs to be approximated.

Approximating average character width

In general, average character width can only be approximated—but there are some scenarios where this can be calculated exactly: for example, when using a 
monospaced font
 or when the contents of a text string are known in advance.

Note:
 Fonts can either be monospaced or fixed-width: in monospaced fonts, all characters take up the same amount of horizontal space; in fixed-width fonts, characters have different widths. Monospaced fonts are commonly used in IDEs—but on the web they are typically less common than fixed-width fonts.

Note:
 For the sake of simplicity, this article refers to the "width" of a glyph. Although this terminology is not wrong per se—"advance", 
"advance width"
, or "horizontal advance" are the terminology typically used in the typography field.

An example of a naive approach to calculating 
avgCharacterWidth
 is to take the average width of all 
[a-z\s]
 characters.

Width of Roboto glyphs

However, weighting all characters equally will likely underweight the width of frequently used letters (for example, 
e
) and overweight the width of infrequently used letters (for example, 
z
).

A more complex approach that improves accuracy is to take 
letter frequency
into account and instead calculate the frequency-weighted average width of 
[a-z\s]
 characters. This 
article
 is a good reference for the letter frequency and average word length of English texts.

Letter frequency in English

Note:
 This article discusses how to calculate 
avgCharacterWidth
 for font fallbacks that will be used with English text—however these same concepts can be applied to other languages and character sets as well. We would be very interested in hearing about your experiences using this technique with content that is not in English.

Note:
 Another possible approach to approximating 
avgCharacterWidth
 is to use 
xAvgCharWidth
. 
xAvgCharWidth
 is a pre-populated value that exists within a font’s 
OS/2 table
. However, be aware that this metric isn’t always correct—for example, many font subsetting tools don’t update 
xAvgCharWidth
 when glyphs are added or removed from a font. In addition, even if 
xAvgCharWidth
 is calculated correctly, the methodology for calculating 
xAvgcharWidth
 has 
changed
 over the years: you can expect the value of 
xAvgCharWidth
 to vary depending on which 
version of the OS/2 table
 is used by the font.

Choosing an approach

The two approaches discussed in this article each have their advantages and disadvantages:

Using font metric overrides by themselves is a good approach to use if you are getting started with optimizing your font fallbacks. Although this is the simpler of the two approaches—it is typically powerful enough to noticeably reduce the magnitude of font-related layout shifts.

On the other hand, if you want greater precision and are willing to do a bit more work and testing, incorporating 
size-adjust
 is a good approach to use. When implemented correctly, this approach can effectively eliminate font-related layout-shifts.

Note:
 You may be wondering why you can’t just set a fixed 
line-height
 instead of using font metric overrides or 
size-adjust
. Although 
line-height
 can sometimes be successfully used to reduce or eliminate font-related layout shifts—this practice is not recommended. Font metric overrides and 
size-adjust
 address the root issue behind web font/fallback font mismatches—
line-height
 does not (
line-height
 sets the height of the CSS 
line box
). In addition, you are likely to find that using 
line-height
 for this purpose is more confusing than you originally anticipated. This 
article
 is a good overview of things to be aware of when working with 
line-height
.

Choosing fallback fonts

The techniques described in this article rely on using font metric overrides and 
size-adjust
 to transform widely available local fonts—rather than attempting to find a local font that closely approximates the web font. When choosing local fonts it’s important to keep in mind that very few fonts have widespread local availability and no single font will exist on all devices.

Arial
 is the recommended fallback font for sans-serif fonts and 
Times New Roman
 is the recommended fallback font for serif fonts. However, neither of these fonts is available on Android (
Roboto
 is the only system font on Android).

The example below uses three fallback fonts to ensure widespead device coverage: a fallback font that targets Windows/Mac devices, a fallback font that targets Android devices, and a fallback font that uses a 
generic font family
.

body

{

font-family
:

"Poppins"
,

poppins-fallback
,

poppins-fallback-android
,

sans-serif
;

}

/*

Poppins font metrics:

- ascent = 1050

- descent = 350

- line-gap = 100

- UPM: 1000

AvgCharWidth:

- Poppins: 538.0103768

- Arial: 884.1438804

- Roboto: 969.0502537

*/

@
font-face

{

font-family
:

poppins-fallback
;

src
:

local
(
"Arial"
);

size-adjust
:

60
.
85099821
%;

ascent-override
:

164
.
3358416
%;

descent-override
:

57
.
51754455
%;

line-gap-override
:

16
.
43358416
%;

}

@
font-face

{

font-family
:

poppins-fallback-android
;

src
:

local
(
"Roboto"
);

size-adjust
:

55
.
5193474
%:

ascent-override
:

180
.
1173909
%;

descent-override
:

63
.
04108683
%;

line-gap-override
:

18
.
01173909
%;

}

Note:
 There are other local fonts that can be used as font fallbacks—but doing so requires knowing a user’s operating system. For example, 
"Calibri"
, 
"Lucinda Sans"
, and 
"Impact"
 are fonts that are all widely available on Windows—but not on other operating systems.

Request for feedback

Please reach out if you have any feedback on your experience using font metric overrides and 
size-adjust
.

Except as otherwise noted, the content of this page is licensed under the 
Creative Commons Attribution 4.0 License
, and code samples are licensed under the 
Apache 2.0 License
. For details, see the 
Google Developers Site Policies
. Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2023-02-10 UTC.


