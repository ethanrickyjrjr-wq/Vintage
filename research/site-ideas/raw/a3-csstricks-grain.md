[Skip to main content](https://css-tricks.com/grainy-gradients/#maincontent)
[ CSS-Tricks ](https://css-tricks.com/) Since 2007
  * [Articles](https://css-tricks.com/category/articles/)
  * [Almanac](https://css-tricks.com/almanac)
  * [Guides](https://css-tricks.com/guides)
  * [Links](https://css-tricks.com/category/links/)
  * [Newsletter](https://css-tricks.com/newsletters/)
  * [Shop](https://css-tricks.com/shop/)
  * [Account icon-account ](https://css-tricks.com/account)
  * [Search ](https://www.google.com/search?q=site:css-tricks.com%20layout)


[background](https://css-tricks.com/tag/background/) [filter](https://css-tricks.com/tag/filter/) [gradients](https://css-tricks.com/tag/gradients/) [svg filters](https://css-tricks.com/tag/svg-filters/)
#  Grainy Gradients 
![](https://secure.gravatar.com/avatar/8e8b77b70bae89c98f5f01175ace6cfe1d1af0409c5b2e12d3c90724084e7934?s=80&d=retro&r=pg)
By [ Jimmy Chion ](https://css-tricks.com/author/jimmychion/) on  Sep 13, 2021 
Browse through Dribbble or Behance, and you’ll find designers using a simple technique to add texture to an image: noise. Adding noise makes otherwise solid colors or smooth gradients, such as shadows, more realistic. But despite designers’ affinity for texture, noise is rarely used in web design.
In this article, we’ll generate colorful noise to add texture to a gradient with only a small amount of CSS and SVG. Alright, let’s make some noise!
![](https://css-tricks.com/wp-content/uploads/2021/09/d310e584818869.5d68b0aa18fdf-edited.png)Illustration by [Hank Washington on Behance](https://www.behance.net/gallery/84818869/Fuzzies-vol-1?tracking_source=search_projects_recommended%7Cgrainy%20texture)
![](https://css-tricks.com/wp-content/uploads/2021/09/bbd2fd6b992fd0f7759109f4097dd1f7-edited-1.jpg)Illustration by [Jordan Kay on Dribbble](https://dribbble.com/shots/16212730-Hovedspr-ng-Double-LP-Release-Book)
###  [](https://css-tricks.com/grainy-gradients/#interactive-playground)Interactive playground
[Check it out here](https://grainy-gradients.vercel.app). The quickest way to understand what’s happening is to play with the parameters that make up the layers.
[![](https://css-tricks.com/wp-content/uploads/2021/09/sajJQP9o.png)](https://grainy-gradients.vercel.app)
###  [](https://css-tricks.com/grainy-gradients/#the-trick-svg-noise-and-css-gradients)The trick: SVG noise and CSS gradients
![](https://css-tricks.com/wp-content/uploads/2021/09/s_3A90A1111308726B36B9818ECFB4B0D40907F129F2D467CA72A5B8EFE38BD08D_1630545908739_diagram-1024x499.png)
The core technique in this article is built on top of a Stack Overflow answer by Chris Pachl to the question: [Can you add noise to a CSS gradient?](https://stackoverflow.com/questions/4011113/can-you-add-noise-to-a-css3-gradient)
The trick is to use an SVG filter to create the noise, then apply that noise as a background. Layer it underneath a gradient, boost the brightness and contrast, and that’s it — you have gradient that gradually dithers away.
####  [](https://css-tricks.com/grainy-gradients/#the-key-ingredients)The key ingredients
Here’s what we’re working with under the hood:
  * **SVG turbulence:** This is our noise filter.
  * **Background with gradient and SVG:** Next, we drop that filter into CSS as a background image that combines the filter with a CSS gradient.
  * **Boost brightness and contrast:** Then we turn to CSS `filter` to increase the brightness and contrast of the noise.
  * **Blend gradients:** Finally, we optionally use `mix-blend-mode` to further filter out colors and blend gradients together.


Let’s go into detail on each of these parts.
####  [](https://css-tricks.com/grainy-gradients/#using-svg-turbulence)Using SVG turbulence
Within the realm of SVG, we can define [filters](https://developer.mozilla.org/en-US/docs/Web/SVG/Element/filter), and one such filter lets us create Perlin noise. It’s called [`<feTurbulence>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Element/feTurbulence) and we can define attributes, such as whether it is “turbulence” or “noise” and how fine or coarse it is. [Bence Szabó explains it in much more detail](https://css-tricks.com/creating-patterns-with-svg-filters/) as he demonstrates how it can be used to create patterns.

```
<svg viewBox="0 0 200 200" xmlns='http://www.w3.org/2000/svg'>
  <filter id='noiseFilter'>
    <feTurbulence 
      type='fractalNoise' 
      baseFrequency='0.65' 
      numOctaves='3' 
      stitchTiles='stitch' />
  </filter>

  <rect width='100%' height='100%' filter='url(#noiseFilter)' />
</svg>
```

This SVG example creates a filter and renders a `<rect>` element that we can use for our grainy gradients. Notice that the SVG `<filter>` is defined separately from the `<rect>`, and the `<rect>` simply references it.
[Play around](https://codepen.io/cjimmy/pen/RwVmgGR) with changing some of the properties of `<feTurbulence>`
CodePen Embed Fallback
We’re going to save this SVG as a separate file. We reference an external link to grab the SVG in the demos throughout in this article. In practice, though, you would reference a local file or your own CDN. It doesn’t work to reference the SVG by its `id` in CSS, for some quirky reason, but you can [inline the SVG](https://css-tricks.com/using-svg/), as we show in the [playground demo](https://grainy-gradients.vercel.app). We don’t do this in the demos for legibility reasons.
####  [](https://css-tricks.com/grainy-gradients/#creating-a-css-background-with-svg-and-a-gradient)Creating a CSS `background` with SVG and a gradient
After we have the SVG file stored somewhere we can reference it by a URL or path, we can now use it in a CSS `background`, combined with a gradient.

```
.noise {
  /* ... */
  background:
    linear-gradient(to right, blue, transparent),
    url(https://grainy-gradients.vercel.app/noise.svg);
}
```

Order matters here. In this particular example, we want a solid color (i.e. no noise) to transition into noise and then into another color. We also want one end of the gradient to be transparent so that the noise shows through.
Like this:
CodePen Embed Fallback
However, this isn’t particularly nice because the noise is too muddled. We need to fray it and make it _grainier_. We can do that by…
####  [](https://css-tricks.com/grainy-gradients/#boosting-the-brightness-and-contrast)Boosting the brightness and contrast
Adding a CSS `filter` makes the noise more stark, pushing the most faded colors towards white or black. The filter applies to the entire `<div>`, so the leftmost blue is a different blue than the pure blue we started with.

```
.noise {
  /* ... */
  background: 
    linear-gradient(to right, blue, transparent), 
    url(https://grainy-gradients.vercel.app/noise.svg);
  filter: contrast(170%) brightness(1000%);  
}
```

You can play around with how contrast and brightness affect the gradient. Boosting the brightness and contrast pushes out the muddled grays in the follow demo.
CodePen Embed Fallback
####  [](https://css-tricks.com/grainy-gradients/#the-noise-is-not-uniform-in-color)The noise is not uniform in color
If you zoom in, you’ll notice that the noise is made up of many colors. The SVG filter was colorful to begin with, and increasing the brightness and contrast emphasized certain colors. Although hardly noticeable, if this confetti is unwelcome, we can continue to filter out colors with CSS blending (i.e. `mix-blend-mode` and `background-blend-mode` ).
![](https://css-tricks.com/wp-content/uploads/2021/09/s_3A90A1111308726B36B9818ECFB4B0D40907F129F2D467CA72A5B8EFE38BD08D_1629408325248_ScreenShot2021-08-19at4.48.17PM.png)
![](https://css-tricks.com/wp-content/uploads/2021/09/s_3A90A1111308726B36B9818ECFB4B0D40907F129F2D467CA72A5B8EFE38BD08D_1629408278778_ScreenShot2021-08-19at5.23.02PM.png)
####  [](https://css-tricks.com/grainy-gradients/#css-blending)CSS blending
Let’s make a grainy gradient that transitions between two colors. CSS blending allows us to stack layers of color. In the next example, we’re adding another `<div>` to the markup, positioning it over the original gradient, then applying `mix-blend-mode: multiply;` to smooth things out.

```
<section>
  <div class="isolate">
    <div class="noise"></div>
    <div class="overlay"></div>
  </div>
</section>
```

```
.noise {
  /* ... */
  background: 
    linear-gradient(20deg, rebeccapurple, transparent), 
    url(https://grainy-gradients.vercel.app/noise.svg); 
  contrast(170%) brightness(1000%);
}
.overlay {
  /* ... */
  background: moccasin;
  mix-blend-mode: multiply;
}
```

We can use the CSS [`isolation`](https://css-tricks.com/almanac/properties/i/isolation/) property to create a new stacking context and choose what gets blended. If we were to leave out `isolation` in the next example, the gradient and overlay would blend with the background color. Try it in the Pen and comment out that line!

```
/* Same as before */

.isolate {
  isolation: isolate;
  /* ... */
}
```

CodePen Embed Fallback
###  [](https://css-tricks.com/grainy-gradients/#some-use-cases)Some use cases
We’ve looked at a pretty simple example of how to make a noisy gradient, but where might you use one? Let’s consider several use cases.
####  [](https://css-tricks.com/grainy-gradients/#light-and-shadows-with-grain)Light and shadows, with grain
Where do gradients naturally occur? Light and shadows, for one. We can take advantage of the CSS property `mix-blend-mode` to smoothly blend gradients and selectively filter the colors we want to see in the noise.
CodePen Embed Fallback
In the “shadow” example, we create a dark gradient, and invert it to create the effect in the “light” example. In both cases, `mix-blend-mode` allows us to blend it with other gradients.
CodePen Embed Fallback
####  [](https://css-tricks.com/grainy-gradients/#holographic-foil)Holographic foil
The drastic brightness and contrast boost creates a rainbow effect that’s reminiscent of holographic foil.
CodePen Embed Fallback
###  [](https://css-tricks.com/grainy-gradients/#taking-things-further)Taking things further
Try [the playground](https://grainy-gradients.vercel.app) and mess around with the different parameters to see how they affect the texture.
Beyond that, here are some ways to continue fiddling with this technique:
  * **Use a different SVG:** All of the gradients in this article use the same SVG, but you can toy with the parameters that generates the noise to adjust the coarseness as well as the look and feel in [the playground](https://grainy-gradients.vercel.app).
  * **Try different gradients:** Besides `linear-gradient`, CSS offers four more types of gradients. Can you name them? ([Here’s one.](https://developer.mozilla.org/en-US/docs/Web/CSS/gradient/repeating-conic-gradient))
  * **Add more layers:** With CSS blending, you can stack as many any layers as you’d like and blend them down.
  * **Apply different SVG filters:** There are all kinds of filters, including Gaussian blur and different types of lighting. Plus, they can be referenced in a CSS filter and [applied to _any_ element](https://developer.mozilla.org/en-US/docs/Web/SVG/Applying_SVG_effects_to_HTML_content) in addition to SVG.


What else can you think of? Please let us know what you discover in the comments.
###  [](https://css-tricks.com/grainy-gradients/#browser-support)Browser support
We can’t escape talking about browser support here. The core of this technique is supported by all modern browsers. As you might expect, it does not work in Internet Explorer. That said, Internet Explorer does support [SVG as a background in CSS](https://caniuse.com/svg-css) (just not with the actual CSS `filter` property).
####  [](https://css-tricks.com/grainy-gradients/#svg-as-a-css-background-image)SVG as a CSS background image
This browser support data is from [Caniuse](http://caniuse.com/#feat=svg-css), which has more detail. A number indicates that browser supports the feature at that version and up.
#### Desktop  
| Chrome  | Firefox  | IE  | Edge  | Safari  |  
| --- | --- | --- | --- | --- |  
| 5  | 24  | 9  | 16  | 5  |  
#### Mobile / Tablet  
| Android Chrome  | Android Firefox  | Android  | iOS Safari  |  
| --- | --- | --- | --- |  
| 156  | 158  | 3  | 4.2-4.3  |  
####  [](https://css-tricks.com/grainy-gradients/#css-filter-effects)CSS filter effects
This browser support data is from [Caniuse](http://caniuse.com/#feat=css-filters), which has more detail. A number indicates that browser supports the feature at that version and up.
#### Desktop  
| Chrome  | Firefox  | IE  | Edge  | Safari  |  
| --- | --- | --- | --- | --- |  
| 18*  | 35  | No  | 79  | 6*  |  
#### Mobile / Tablet  
| Android Chrome  | Android Firefox  | Android  | iOS Safari  |  
| --- | --- | --- | --- |  
| 156  | 158  | 4.4*  | 6.0-6.1*  |  
I’ve also noticed that Blink-based browsers (e.g. Chrome) and WebKit-based one (e.g. Safari) implement `mix-blend-mode` slightly differently, so please be sure to test across browsers if using CSS blending. In my own projects, I’ve used [browser-specific media queries](http://browserhacks.com) to manually reconcile the visual differences with small tweaks to CSS.
* * *
That’s it! Now that you have a grasp of SVG filters and how to combine them with CSS filters as a background, you have yet another neat visual effect to add depth and texture to a design.
[ ![CSS-Tricks star logo](https://css-tricks.com/wp-content/uploads/2019/08/css-tricks-logo-blur.png) ](https://css-tricks.com/advertising)
#### Sponsor CSS-Tricks!
[We've got lots of ways to help you connect with the greatest front-end community in all the land.](https://css-tricks.com/support)
[ ![](https://css-tricks.com/wp-content/uploads/2022/09/email-envelope.jpg) ](https://css-tricks.com/newsletters)
#### CSS-Tricks Newsletter
[Sign up to get front-end roundups, browser updates, and exclusive content sent to your inbox bi-weekly.](https://css-tricks.com/newsletters)
Ads are self-hosted
##  Comments
  1. Lars Ejaas
[Permalink to comment#](https://css-tricks.com/grainy-gradients/#comment-1782394) September 14, 2021
Wow! Really cool. I have been playing around with different techniques to create a grainy effect but never thought of svg filters…
  2. Calinou
[Permalink to comment#](https://css-tricks.com/grainy-gradients/#comment-1782416) September 14, 2021
Note that adding noise isn’t just just for artistic purposes. Adding subtle noise can also be useful to combat banding when you use long gradients with subtle color changes.
  3. Ian
[Permalink to comment#](https://css-tricks.com/grainy-gradients/#comment-1782685) September 21, 2021
This is really cool (and useful!).
Is it possible to use this technique / effect with CSS box-shadow? Looking for a way to add noise to a drop shadow
     * Jimmy Chion
[Permalink to comment#](https://css-tricks.com/grainy-gradients/#comment-1782795) September 22, 2021
Hey Ian – I don’t think you’ll be able to use it with box-shadow, but I tried to create the effect of a box-shadow in this Pen: <https://codepen.io/cjimmy/pen/wvexYoJ> (I’ve only tested it in Safari. Results may differ with other browsers)
The main idea is that you can add more `linear-gradient()`s to create a shape and then invert it. I made a border of a box with dark grainy gradients: dark borders, light inside. You can then inverted it: dark rectangle inside, light outside. To remove the light part with `mix-blend-mode`.
It may not be exactly what you’re seeking, but perhaps it inspires a better method for you. (If so, please do share!)
  4. JL Garcia
[Permalink to comment#](https://css-tricks.com/grainy-gradients/#comment-1782755) September 22, 2021
I don’t know where, I don’t know how, but I’m going to use this.
  5. sowg
[Permalink to comment#](https://css-tricks.com/grainy-gradients/#comment-1782978) September 27, 2021
Can you use two colours that look familiar for Grainy Gradients?
  6. Ryan Killeen
[Permalink to comment#](https://css-tricks.com/grainy-gradients/#comment-1783170) October 1, 2021
Ever since I read this article, I can’t help but wonder if you could use this grainy noise effect as a mask on the edge of a div.
If any SVG wizards want to give it a whirl, let me know!
  7. Thomas Rettig
[Permalink to comment#](https://css-tricks.com/grainy-gradients/#comment-1783285) October 5, 2021
If only this trick didn’t have to suck performance-wise…
  8. F
[Permalink to comment#](https://css-tricks.com/grainy-gradients/#comment-1788286) January 17, 2022
By relying on extreme contrast and brightness, this methods forgoes a huge range of colors.
Using a mask is a much more effective way of achieving this effect.
  9. Petr Haluza
[Permalink to comment#](https://css-tricks.com/grainy-gradients/#comment-1808139) March 19, 2024
I needed a more simpliest solution, so i used only one :before css line to achieve this: <https://jsfiddle.net/PetrHaluza/jre3dxhq/>


This comment thread is closed. If you have important information to share, please [contact us](https://css-tricks.com/contact/). 
[ Ad ![](https://css-tricks.com/wp-content/uploads/2026/10/concentric-layers.jpg) CSS-Tricks Members Join our community of front-end nerds! You'll get into the Discord server and member-only perks and free swag. ](https://css-tricks.com/memberships)
[ Ad ![](https://css-tricks.com/wp-content/uploads/2026/10/timeline-pattern-square.jpg) CSS-Tricks Newsletter Sign up to get front-end roundups, browser updates, and exclusive content sent to your inbox bi-weekly. ](https://css-tricks.com/newsletters)
[ Ad ![](https://css-tricks.com/wp-content/uploads/2026/10/unisex-staple-t-shirt-vintage-white-front-6ad516c9a55fc.jpg?fit=1000%2C1000&ssl=1) CSS-Tricks Store Get your t-shirts, prints, stickers, and yes, even mousepads at the brand-spankin' new CSS-Tricks store, now open. ](https://css-tricks.com/shop)
CSS-Tricks is powered by a small team of real-life [humans](https://css-tricks.com/about). 
#### Get Curated Front-End Roundups Right in Your Inbox
Coming back November 10! [See past issues →](https://css-tricks.com/newsletters)
Enter your email
##### CSS-Tricks
  * [Guest Writing](https://css-tricks.com/guest-writing/)
  * [Memberships](https://css-tricks.com/memberships/)
  * [CSS-Tricks Store](https://css-tricks.com/shop/)
  * [Support Us](https://css-tricks.com/support/)
  * [Advertising](https://css-tricks.com/advertising/)
  * [Contact Us](https://css-tricks.com/contact/)


##### Social
  * [RSS Feeds](https://css-tricks.com/rss-feeds/)
  * [Bluesky](https://bsky.app/profile/css-tricks.bsky.social)
  * [Mastodon](https://mastodon.social/@csstricks)
  * [CodePen](https://codepen.io/team/css-tricks)
  * [X / Twitter](https://x.com/css)
  * [LinkedIn](https://linkedin.com/company/css-tricks-dot-com/)


##### Legalese
  * [CSS-Tricks License](https://css-tricks.com/license/)
  * [AI Statement](https://css-tricks.com/ai/)
  * [Terms of Use](https://css-tricks.com/terms/)
  * [Privacy Policy](https://css-tricks.com/privacy/)


[ Back to Top ](https://css-tricks.com/grainy-gradients/#top-of-site) ![](https://pixel.wp.com/g.gif?v=ext&blog=45537868&post=351302&tz=-6&srv=css-tricks.com&j=1%3A16.3.1&host=css-tricks.com&ref=&rand=0.2291135661189917)

