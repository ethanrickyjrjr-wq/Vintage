<!-- SOURCE: https://adrianroselli.com/2019/12/responsive-type-and-zoom.html (fetched 2026-10-29T05:16:25Z via curl + html->text) -->



Responsive Type and Zoom

		Updated 
October 20, 2025
, originally posted 
December 6, 2019
; 
24 Comments

Typography that responds to viewport width (‘fluid’ or ‘responsive’ typography) can be useful when you want to ensure text does not get clipped or spill out of some design elements. 
Carousels
, widget controls, or my 
Venn diagram
 are some examples.

I say viewport 
width
 because I rarely see responsive type consider the viewport height or the printed page. Not considering height can bw problematic for users holding their phone in landscape mode while trying to navigate pages with cookie consents and email form sign-ups. Not considering print can make for reams of 
wasted paper
.

Responsive vs. Static

The alternative approach is to just use static text sizing, ignoring the size of the viewport.

To demonstrate the difference I forked a five-year-old Codepen that had just been updated last week, 
Precision responsive typography
 and started zooming the page, capturing screen shots along the way.

Then

I duplicated the pen
, removing all the responsive sizing styles, ensuring the text started at the same size in an un-zoomed window. Then I zoomed and screen-shat it.

Screens

All screen shots were captured in Windows 10 / Firefox 72.0b1, but the effect is the same across browsers.

The first/left image is the responsive type example with no zoom. The second image is the same HTML, but no responsive type, with no zoom. The text is the same size in both.

The first/left image is the responsive type example at 200% zoom. The second image is the same HTML, but no responsive type, at 200% zoom. The size difference is apparent, but not overwhelming.

The first/left image is the responsive type example at 300% zoom. The second image is the same HTML, but no responsive type, at 300% zoom. Firefox users cannot zoom any more, which means the text cannot get any larger for them. The text cannot get to truly 200% its original size.

While Firefox limits zoom to 300%, Chrome goes higher and at 400% zoom the user of the responsive type page can finally get the text to almost 200% of its original size.

Code

For comparison, I have embedded the two different CSS blocks within this poorly-styled 
details
/
summary
 thinger…

 The original SCSS (comments stripped):

$min_width: 400;
$max_width: 800;
$min_font: 12;
$max_font: 24; 

:root { font-size: #{$min_font}px; }

@media (min-width: #{$min_width}px) and (max-width: #{$max_width}px){
  :root { 
    font-size: calc( #{$min_font}px + (#{$max_font} - #{$min_font}) * ( (100vw - #{$min_width}px) / ( #{$max_width} - #{$min_width}) ));
  }
}
@media (min-width: #{$max_width}px){
   :root { 
     font-size: #{$max_font}px;
   }
}

 The entirety of the text sizing CSS in my pen:

:root {
  font-size: 150%;
}

Why It Matters

I have worked with users who scale text to this large. Some of them do it because they surf on their TV from their couch. Some do it when reading a recipe off their phone in the kitchen. Some do it when they need to present on a wall to a room full of a people. Some of them just have poor vision.

When people zoom a page, it is typically because they want the text to be bigger. When we anchor the text to the viewport size, even with a (fractional) multiplier, we can take away their ability to do that. It can be as much a 
barrier as disabling zoom
. If a user cannot get the text to 200% of the original size, you may also be looking at a 
WCAG 1.4.4 Resize text (AA)
 problem — check out 
Failure of Success Criterion 1.4.4 due to incorrect use of viewport units to resize text
.

I want to be clear — I am not picking on the specific example above. That example is only demonstrating what developers 
can
 do, not what they 
should
 do. There may be completely valid reasons to use these techniques and the example I borrowed shows one method to do that.

What to Do

Identify 
why
 you want responsive type. Is it based on user request? Surveys? Research? Or is it just that you or your team think it looks better? Or you want to try out this technique? The answers may tell you if you should even move ahead with responsive type.

Consider not setting a base font size. Maybe use the following rule (or similar or nothing) to inherit the font size from the browser, which may have been explicitly chosen by the user:

:root {
   font-size: 100%;
}

Then only set subsequent text size values using 
%
, 
em
, or 
rem
 units, avoiding values below 
100%
, 
1em
, or 
1rem
 (unless scaling down in something already scaled up).

Be careful when using 
vw
 or 
vh
 units. Then be careful if using 
calc()
. Be even more careful when using 
min()
, 
max()
, or 
clamp()
 (see 
CSS Values and Units Module Level 4
 for the Working Draft spec language).

If you are going to use responsive typography techniques anyway, you must test it by zooming. Zoom across devices, across browsers, across viewport sizes (
not everyone surfs full-screen
), and across viewport orientations.

Also, don’t forget print styles. Consider print units in 
pt
, and print to PDF to confirm it works without wasting paper.

Update: 7 January 2020

New York Times has an 
experimental interactive piece
 that demonstrates some of what I discuss above. Zooming out from a page should not make the text larger than zooming in.

The text is largest when at 80% zoom (first image), then much smaller at 110% zoom (middle image), then a bit larger at 133% zoom (last image).

Update: 20 May 2020

Scaling text by using the browser preferences to change the default text size will not affect any text on a page that is set in 
px
 units.

To say it a different way, if you set your text in 
px
, then it will not scale when a user explicitly chooses a larger or smaller default size. You 
px
-based text will stay the same size, laughing at your user.

Obviously full-page zoom overrides it, but many users still opt for a larger default size to avoid having to scale every site. So don’t set your text in 
px
.

Update: 26 September 2020

Apparently I need to keep saying this. The following is becoming my default comment on articles that 
keep

appearing

without

cautions
.

Please be careful with maximum text size, particularly on sites/pages that face the general public or employees. If you prevent the text from scaling up 200%, then that is a 
WCAG SC 1.4.4
 failure at Level AA. 
Viewport units have their own call-out
 as a major risk in WCAG.

No matter what technique you use, be sure that the page text can be zoomed at least 200%. And yes, I have written about 
responsive type and zoom
, and have cautioned against 
min()
, 
max()
, and 
clamp()
.

Update: 29 September 2020

This in response to a 
specific request
 on the post 
Linearly Scale font-size with CSS clamp() Based on the Viewport
. I referenced a 
simpler example
 from the post 
in my comment
, but figured I would use the final example here to be sure I caught all the affordances in the code.

See the Pen 

  Fluid typography example
 by Pedro Rodriguez (
@pprg1996
)
  on 
CodePen
.

I made a video showing that as I zoom to 200%, the text stops scaling at about the 150% point.

  Sorry, your browser doesn’t support embedded videos, but don’t worry, you can 
download it
.

Here I compare the original text, the page scaled to 200%, and then how the text should look if it was actually made it to 200%.

Here I show the 
<h1>
 at its initial size, when the page is zoomed to 200%, and when the text is actually 200% the size of the initial text. I aligned them on the baseline to make the difference between them more obvious.

Similarly, even a 
simple demo
 taken out of context can be a problem. Your text should never get smaller when the user zooms, and it certainly should not be smaller at 300% zoom.

  Sorry, your browser doesn’t support embedded videos, but don’t worry, you can 
download it
.

Update: 17 October 2020

Over at dev.to, Google’s developer support blog, Una Kravets posted 
min(), max(), and clamp(): three logical CSS functions to use today
 where she walks through how each of those CSS functions works and shows some examples.

There is a 
fluid typography example
 she borrowed from elsewhere that shows how text can scale and adjust to the viewport, using only the style declaration 
font-size: clamp(1.5rem, 5vw, 3rem)
. A video shows it in action.

If you have read this far, you may have spotted something that can cause a problem here. It’s not the use of 
clamp()
, since the upper limit, 
3rem
, is twice the size of the starting 
1.5rem
. It’s the use of 
vw
 units. For some users, the text can never get large enough to bump up against the 
3rem
.

I made a video to demonstrate it in action, but you can 
visit the original demo
 to try it yourself. Remember that Firefox can only zoom to 300%.

  Sorry, your browser doesn’t support embedded videos, but don’t worry, you can 
download it
.

This is a 1,024 pixel window in width, though I kept the height short and it has no impact on the demo. The text starts at 64px tall, at 200% zoom has only increased to 68px in height (a 6.25% increase), and at 300% zoom has only increased to 96px in height (a 150% increase).

If you use this code as-is, you have guaranteed a WCAG failure.

I 
filed a pull request
 (which they merged on 21-Oct) with a brief explanation:

 When you use 
vw
 units or limit how large text can get with 
clamp()
, there is a chance a user may be unable to scale the text to 200% of its original size. If that happens, it is WCAG failure under 
1.4.4 Resize text (AA)
 so be certain to 
test the results with zoom
.

…before 
merging another PR
 that removed the links. So, shrug emoji?

Update: 27 September 2022

I completely failed to link to W3C issues that may or may not have some impacts here:

#1671 Can large headings be exempt from Success Criterion 1.4.4 Resize text?
, filed against WCAG by Šime Vidas on 8 March 2021;

#6869 Browser zoom unit for accessibility [css-values-and-units]
, filed against CSS by Scott Kellum on 8 December 2021.

Not a lot of movement recently, but it is instructional to see the challenges and goals outlined by all parties.

Update: 17 November 2023

I kinda like this:

 Mudford cites Adrian Roselli, who appears to be 
the core source
 of the other warnings:

That may very well be true. I did not find others citing the very real (and easy to prove) WCAG failures developers were suddenly pushing into their projects. That was a little depressing, frankly (considering how easy it is to prove). I spent a lot of time grumping about this online, too. So yay me.

Anyway, Maxwell does the thing I did not — he tried to plot the curves and do the math to give developers guidance on how to write their CSS functions to create WCAG-conformant fluid type. I have not tested the assertions, but I definitely appreciate the effort.

It only took four years!

Update: 3 April 2025

This video may look familiar:

  Sorry, your browser doesn’t support embedded videos, but don’t worry, you can 
download it
.

A string of text in a browser window reads “This text fits to the available space.” It does not wrap to a second line. The user zooms the page and surrounding text gets larger, but not this text. It never changes size, becoming smaller and smaller relative to surrounding text.

I have videos in this post showing the same behavior with other responsive type techniques. But this technique is new. It’s meant to ensure a piece of text always fits the width of its parent. Wrapping does not seem to be an option.

Patrick Lauke posted this video as a 
comment on [css-fonts-4] Feature for making text always fit the width of its parent #2528
. He demonstrated that encoding this behavior into the CSS specification will create an almost guaranteed WCAG failure every time it is used. Unfortunately, the first response by a W3C CSS Working Group member was to say that 
WCAG should revise this SC
 which, unfortunately, seems to ignore the 
W3C Priority of Constituencies
 at the very minimum.

Update: 20 October 2025

Miriam Suzanne has been running at responsive type for a few months now, with a series of five posts (and a sixth about units in general) ending with 
Visualizing Responsive Typography
. None of them gives a definitive, absolute, copy-pasta-ready set of styles for responsive type that’s guaranteed not to trigger a 1.4.4 violation. Because this stuff is hard, as that series demonstrates.

Meanwhile, last week Matthias Ott posted 
Com­pressed Flu­id Typography
, which is another effort at trying to solve this and 
not
 fail WCAG. He acknowledges that in the post. What we are seeing is that there are many ways to detonate a cat but so far none leave the cat alive. 

24 Comments

Reply

Hey Adrian, I’m working on a design system that’s using a vw plus rem scaling 
font-size: calc(1rem + 0.2vw)
 and it seems to be responding just fine to both browser zoom and font-size settings in the browser config.

Have I not explored all the scenarios in which this kind of responsive type would break or do you think this solution is okay?

						In response to 
Mark Goho
.

Reply

Mark, I think 
0.2vw
 is such a small number that it might not matter. But be aware that for a user who zooms, the 
vw
 value in your 
calc()
 will not change with zoom. But since the 
rem
 is the major value it may not be a big deal except in very wide windows.

As always, test those edge cases so you at least know what happens.

Reply

I couldn’t replicate the zoom discrepancy between 
https://cdpn.io/aardrian/debug/XWJmjrN
 and 
https://cdpn.io/aardrian/debug/NWPPJRo
 . Both looks the same at 500% in firefox. What am I missing? Thanks for this post.

Reply

Oh sorry I see it now if I view it in the ‘Responsive design mode’. Cool. Thanks!

Reply

Hey Adrian, I think I might have a solution that respects zoom while resulting in the same effect. 

Basically I’m using javascript to multiply the root font size by some value which is clamped at a min or max. So it respects both a users font size and zoom. Of course it affects all elements that use REM, but that tends to be what I want. 

What do you think?

						In response to 
benton328@gmail.com
.

Reply

I think if it never prevents a user from getting the text to 200% 
and
 it does not spin their fans into oblivion, then sure.

Reply

Hey Adrian, you say “Then only set subsequent text size values using %, em, or rem units, avoiding values below 100%, 1em, or 1rem (unless scaling down in something already scaled up).” What’s the problem with setting a small font to 0.875rem (the equivalent of 14px, I believe)? It will still scale, if the users needs to make it bigger through the browser font settings. In fact in the Comments section on this blog, you use both 80% and 0.8rem, which seems a perfectly reasonable use case…

						In response to 
Jonathan Douglas Holden
.

Reply

That statement
 was in the context of setting the base font size to 100%, which keys off the user’s own settings / preferences.

You are suggesting setting the base font size smaller, using my comments section (which is set to 80% the size of the base size of the rest of the content) as justification.

You don’t note that my content size is 130%, or computed as 20.8px. That means my 80%-size comments are 16.64px in a default browser set-up, or still larger than the user’s default font size (104% of default).

So, to answer your question, I suggest you do not do that. Look at the computed values in the dev tools, not the CSS declarations.

						In response to 
Adrian Roselli
.

Reply

Aha! I wasn’t suggesting setting the base font to 80%, just noting that you do use 80%. What I didn’t check, as you say, is that the content font size is 130%. So that makes sense. You’re right, I should have checked the computed values! Thanks once again for your time.

Reply

Hi Adrian,

I’m still trying to unpick the mechanics of WHY this happens. Is it only when you have a prefferred value entirely in vw (because vw doesn’t change)?

Can I ask if this (
https://royalfig.github.io/fluid-typography-calculator/
) has solved around the issue or is there still a risk?

						In response to 
Nathan
.

Reply

Nathan, There is a WCAG failure that describes the issue with viewport units alone:  
Failure of Success Criterion 1.4.4 due to incorrect use of viewport units to resize text
.

As for the tool you linked, I don’t know without breaking it apart. However, note how when the slider at the bottom hits a viewport width of 1,950px, the base font stops getting bigger (it anchors at 20px). That comes from the “Max Font Size” set above, which at 1.25rem means a user may not be able to zoom it enough for their needs.

The simplest answer, IMO, is to never set a maximum font size (so do not use 
clamp()
) or, if you only care about minimum WCAG conformance, never set the maximum font size to a value below twice the base font size.

						In response to 
Adrian Roselli
.

Reply

If it helps, I have done some extra mathematical analysis of this and have found the following….

Even when not applying a max, you cna hit a “200% not possible” violation. The three biggest variables in this outcome are: 

(a) the steepness of the change (i.e. if a linear growth – the steeper the growth, the more likely 200% can’t be achieved)

(b) the max zoom of browsers (e.g. if sometimes you need to go to 300% to hit 200% text growth – eventually some browsers won’t be able to deliver the zoom scale needed.

(c) the worst case viewport width (on a growth curve from 2.625rem at 320px to 3.325rem at 1440px viewport and then larger to maintain linear growth beyond that, even at 300% zoom the 200% text increase is not possible on a 3840 screen. Whilst it is likely that a 4k screen is already upscaled, its not guaranteed.

So, since we don’t control screen sizes or browser zoom levels etc, there will always be a risk with responsive text and the only way around it is to avoid it or, when your growth curve hits a snag, add a breakpoint to go back to a value that avoids vw, etc.

						In response to 
Nathan
.

Reply

This is indeed interesting info. At the very least, having something to identify where the growth curve flatlines so you can add a breakpoint is handy.

						In response to 
Adrian Roselli
.

Reply

A few extra developments. After running a bunch of maths and creating a “Fluid Type” calculator in Excel to try and protect the upper bound, I also have the thoughr that can’t techniques be combined to meet the accessibility criteria?

Say for example your zoom topped out at 194% (never reaching the magic 200%). If the user also changes their browser settings to enlarge text then that would bump it over the 200% (assuming em/rem units are involved).

Thoughts?

Reply

Is this no longer an issue? Chrome on Android, Samsung browser, and Safari both seem to be zooming without breaking the layout now when viewport units are used.

						In response to 
Jonathan
.

Reply

Jonathan, this post deals with desktop browsers, though I could have been more explicit in the post instead of relying on the screen shots to convey that. You have cited mobile browsers where zooming (pinch/spread) is a very different model. Those are analogous to desktop browsers that also use pinch-zoom (via touch screen or track pad).

Reply

There’s strain to the eye if you have to read all the monitor, despite font size… that should be accounted for through the usage of columns and not zoom alone.

Reply

Thanks, Adrian, for highlighting this.

Reading the WCAG 1.4.4 it seems that:

“Content satisfies the Success Criterion if it can be scaled up to 200% using at least one text scaling mechanism supported by user agents.”

So, zoom alone is not sufficient to pass the test, but it is not true that if you fail the zoom (cmd/ctrl +), you don’t pass the 1.4.4 test, at least for what I read from the specs. Am I wrong?

This is also important for media queries that change the font size of an element based on the viewport, or for rem/em based media-query.

						In response to 
MakhBeth
.

Reply

MakhBeth, zoom alone 
can
 be sufficient for WCAG. However, if the user cannot use other methods (such as zoom) and relies on scaling text via 
ctrl
 + 
+
, then the user has a problem. And arguably a case to make.

Reply

There’s something I have a lot of difficulties to understand and check correctly, it’s the difference between the fluid problems and using media-queries to change the size. 

It says here ( 
https://www.w3.org/WAI/WCAG21/Techniques/failures/F94.html
 ) “If media queries were used to adjust the size of text or unit of measure at different screen sizes, it may not be a failure of Resize Text.”

And the site itself has different media queries that decrease the title size for smaller viewports. At 400% the h1 is 1.5rem, at 250% to 300% the h1 is 2rem, and at min 60em it’s 2.375rem.  So it’s never twice the default size and at some point it’s not getting bigger.

What’s the difference between decreasing/increasing the size with media queries  and using clamp ? If I set a lot of media-queries isn’t the result the same ?

						In response to 
Sonia
.

Reply

 At 400% the h1 is 1.5rem, at 250% to 300% the h1 is 2rem, and at min 60em it’s 2.375rem.

Width media queries (which is what I assume you are using) want length units that map to specific values. If they work with percentages (eg: 
@media (min-width: 250%)
), then that is something I’ve just learned but also never needed and never seen in the wild?

Meanwhile, 
clamp()
 sets an upper and lower bound for sizing (with a preferred in the middle). You could use 
clamp()
 instead of media queries for text sizing.

What’s the difference between decreasing/increasing the size with media queries and using clamp ? If I set a lot of media-queries isn’t the result the same ?

This post isn’t about you as the author setting a lot of sizes. This post is about you as the author not preventing the 
user
 from zooming regardless of your method for creating responsive type.

Reply

Sorry it wasn’t clear at all, the percentage was the browser zoom with ctrl+/- ^^”

If I zoom, the media query for smaller viewport is applied, so smaller font size.

I don’t want to prevent the user from zooming, that’s why I try to understand the difference and what not to do, but my brain doesn’t seem to click on how a media query don’t prevent the user from zooming when clamp do (other than the case when a text visibly get smaller when you zoom, but that could happen to with a weird media query) .

						In response to 
Sonia
.

Reply

This is my understanding:

– When zooming in using browser zoom, two things are happening. Firstly, the viewport is decreasing in size. For example, my normal width is 1920px. Doing a 110% zoom brings it to 1745px. Secondly, the actual browser is zooming in (i.e. one css pixel takes up more space on the screen).

– If you zoom in enough, you may even start hitting your mobile breakpoints (e.g. collapsing some side menu) because your viewport width has decreased that far in size.

– Case 1: Font size doesn’t scale with vw. Browser zoom doesn’t affect font size at all so it still takes up the same number of pixels but the pixels themselves become larger, resulting in the text getting larger.

– Case 2: Font size does scale with vw. Browser zoom causes viewport size to decrease resulting in calculated font size to decrease. At the same time, the pixels themselves become larger, resulting in the text getting larger. The overall neutralizing effect is that browser zoom does not appear to work in making the font size larger.

– This effect is not reliant on clamp or setting a max/min font size. By opting into responsive text size that scales with viewport size, decreasing viewport size must necessarily cause the calculated font size to decrease, thus neutralizing the browser zoom in effect.

– In fact, by having a min clamp, you can mitigate this effect a bit. Let’s say I clamp my minimum font size to 16px. Once I zoom in sufficiently far, any further viewport size decreases will no longer affect my font size which is capped at 16px. After this point, the zoom will behave exactly the same as a nonresponsive text page where font size is set to 16px. The same logic applies for max clamp helping mitigate the neutralizing effects of zooming out.

Hope that helps.

						In response to 
Brandon
.

Reply

To elaborate just a little bit more, I think in most reasonable cases, the aforementioned neutralizing effect is actually minimal and unnoticeable.

In the most extreme case, you can have something like font-size: 3vw. On an 800px wide viewport, the computed font size is 24px. When zooming in to 200%, the viewport shrinks to 400px, the font size becomes 12px, the pixels becomes 2x as wide, and so the end result is the text stays perfectly unchanged throughout the entire zoom.

Actually, if you look at the Responsive vs. Static example codepen at the top of this article, this is exactly what it’s doing! Shrinking the viewport by half (from 800px -> 400px) results in the font size exactly shrinking by half (from 24 -> 12px). That’s why the 200% and 300% screenshots show no change. The CSS additionally does clamping (any width above 800px is capped at 24px) so the first screenshot which is at a width > 800px is captured at 24px font size and most of the zoom towards 200% has no decreasing font size so there is a noticeable zoom between the 100% and 200% screenshots, thanks to the clamp.

In the real world, I think very few sites would have it set up so their font sizes shrink at exactly the same rate as their viewport (or even close). For example, 
https://utopia.fyi/type/calculator
, the default is 18px at 320px wide viewport and 20px at 1240px (and every size between is linearly interpolated). The font size decreases by a mere 10% for a 387.5% zoom which would slow down the rate of zoom imperceptibly until a clamp point is hit at which point the rate of zoom jumps back up to normal (also imperceptibly). The site itself uses the font size linear interpolation system it’s describing and I don’t perceive the zoom to be any slower or jarring compared to other sites.

If I’m using static breakpoints with set font sizes compared to linear interpolation, the same math applies. Say normal font size is 24px but at 400px wide viewport and below, it jumps to 12px. If starting at 800px and then slowly zooming to 200%, you would see the zoom take effect at normal speed but when reaching exactly 200%, the text will suddenly shrink back to the size at which you started zooming. Most sites use static breakpoints but never run into issues like this because at its core, the craziness is just a function of jumping an entire 12px in font size after only 400px of viewport width decrease.

Leave a Comment or Response 
Cancel response
Comment:

The form doesn’t support Markdown.
This form allows limited HTML.
Allowed HTML elements are 
<a href>
, 
<blockquote>
, 
<code>
, 
<del>
, 
<em>
, 
<ins>
, 
<q>
, 
<strong>
, and maybe some others. WordPress is fickle and randomly blocks or allows some.

If you want to include HTML 
examples
 in your comment, then HTML encode them. E.g. 
<code>&lt;div&gt;</code>
 (you can copy and paste that chunk).
Name 
*

Email 
*

Website

Δ


