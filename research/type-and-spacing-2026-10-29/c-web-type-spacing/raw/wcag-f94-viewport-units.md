<!-- SOURCE: https://www.w3.org/WAI/WCAG22/Techniques/failures/F94 (fetched 2026-10-29T05:16:06Z via curl + html->text) -->



Technique F94:
Failure of Success Criterion 1.4.4 due to incorrect use of viewport units to resize text

About this Technique

    This technique relates to

1.4.4 Resize Text

(
Failure
).

Failure techniques show examples of how content can fail particular WCAG success criteria. However, content may still satisfy those criteria if it includes equivalent/alternative content or functionality that 
does
 meet the normative requirements. See 
About WCAG Techniques
.

Description

The objective of this technique is to document the failure of text to re-scale when 
viewport units
 are used on text. As these units are relative to the viewport, it means they cannot be resized by zooming or adjusting text-size.

There are various methods to increase and decrease the size of text and other content, but viewport units applied to text (generally via 
font-size
 in CSS) prevent most available methods. Attempts to use browser controls to zoom or adjust text-size will not work. Only methods that completely override the CSS will work, and those could cause other issues such as layouts collapsing or text overlapping.

Some uses of viewport units may not prevent text-size adjustments, but if they are used as the primary method for defining text-size, they are likely to cause a failure of 
Success Criterion 1.4.4 Resize Text
.

Note

If media queries were used to adjust the size of text or unit of measure at different screen sizes, it may not be a failure of 
Resize Text
. On-page controls provided by the author are also a way of passing the resize text success criteria.

Examples

Failure example 1

The following CSS and HTML snippet uses VW units to size the text.

/* CSS */

.callout
 {

font-size
:
1vw
;
}

<
p

class
=
"callout"
>
Text that scales by viewport units
</
p
>

Example 
page with an example of text sized in 
vh
 units
.

Related Resources

No endorsement implied.

MDN
 CSS units
 including 
vh
 and 
vw
 units.

Viewport percentage lengths
 in the CSS Values and Units Module Level 4 specification.

Related Techniques

G179: Ensuring that there is no loss of content or functionality when the text resizes and text containers do not change their width

C12: Using percent for font sizes

C13: Using named font sizes

C14: Using em units for font sizes

Tests

Procedure

Visit the page to be tested.

Use any of the following methods to resize text when available:

the zoom feature of the browser,

the text-sizing feature of the browser,

on-page controls for resizing text.

Check that the text resizes by one of the methods above, and can be resized up to 200% of the default.

Expected Results

If the last step is false, then this failure condition applies and the content fails Success Criterion 1.4.4 Resize Text.

 Back to Top


