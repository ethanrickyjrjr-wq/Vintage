<!-- SOURCE: https://developer.chrome.com/docs/lighthouse/seo/font-size (fetched 2026-10-29T05:16:07Z via curl + html->text) -->



          Home

          Docs

          Lighthouse

          Get started

      Document doesn't use legible font sizes

      Stay organized with collections

      Save and categorize content based on your preferences.

Warning:
 This audit has been removed as of Lighthouse 13. For more information see 
What's new in Lighthouse 13
.

Many search engines rank pages based on how mobile-friendly they are. Font
sizes smaller than 12 px are often difficult to read on mobile devices
and may require users to zoom in to display text at a comfortable reading size.

How the Lighthouse font size audit fails

Lighthouse
 flags pages
with font sizes that are too small to read easily on mobile:

Lighthouse flags pages on which 40% or more of the text has a font size smaller
than 12 px. When a page fails the audit, Lighthouse lists the results in a
table with four columns:

Source

The source location of the CSS ruleset that is causing the illegible text.

Selector

The selector of the ruleset.

% of Page Text

The percentage of text on the page that is affected by the ruleset.

Font Size

The computed size of the text.

Note:
 Each SEO audit is weighted equally
in the Lighthouse SEO Score,
except for the manual 
Structured data is valid
 audit.
Learn more in the 
Lighthouse Scoring Guide
.

How to fix illegible fonts

Check font sizes in your CSS. Aim to have a font size of at least 12 px on
at least 60% of the text on your page.

How to fix a missing viewport config

If Lighthouse reports 
Text is illegible because of a missing viewport config
,
add a 
<meta name="viewport" content="width=device-width, initial-scale=1">

tag to the 
<head>
 of your document.

See the 
Does not have a 
<meta name="viewport">
 tag with 
width
 or 
initial-scale

post for more information.

Resources

Source code for 
Document does not use legible font sizes
 audit

Except as otherwise noted, the content of this page is licensed under the 
Creative Commons Attribution 4.0 License
, and code samples are licensed under the 
Apache 2.0 License
. For details, see the 
Google Developers Site Policies
. Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2019-05-02 UTC.


