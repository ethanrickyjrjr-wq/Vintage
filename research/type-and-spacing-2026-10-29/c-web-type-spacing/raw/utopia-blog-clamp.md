<!-- SOURCE: https://utopia.fyi/blog/clamp/ (crawl4ai via tools/crawl.sh, 2026-10-29) -->
[![Utopia Logo](https://utopia.fyi/images/logo.svg)](https://utopia.fyi/)
  * [Type](https://utopia.fyi/type/calculator?c=360,18,1.2,1240,20,1.25,5,2,&s=0.75%7C0.5%7C0.25,1.5%7C2%7C3%7C4%7C6,s-l&g=s,l,xl,12)
  * [Space](https://utopia.fyi/space/calculator?c=360,18,1.2,1240,20,1.25,5,2,&s=0.75%7C0.5%7C0.25,1.5%7C2%7C3%7C4%7C6,s-l&g=s,l,xl,12)
  * [Grid](https://utopia.fyi/grid/calculator?c=360,18,1.2,1240,20,1.25,5,2,&s=0.75%7C0.5%7C0.25,1.5%7C2%7C3%7C4%7C6,s-l&g=s,l,xl,12)
  * [Clamp](https://utopia.fyi/clamp/calculator?a=360,1240)
  * [Blog](https://utopia.fyi/blog)
  * [Showcase](https://utopia.fyi/showcase)
  * [Merch](http://utopiafyi.teemill.com/)


# Clamp
**By Trys Mudford**
CSS has some exciting new features for fluid scaling. `clamp()`, `min()`, and `max()` are functions that cap and scale values as the browser grows and shrinks.
Much like their `Math.` equivalents in JavaScript, `min()` and `max()` return the respective minimum and maximum values at any given time.
Clamp is a superset of the two, letting you pass in a minimum, maximum, and 'preferred' size (this is a suggested size for the browser to use). A straightforward usage would be: `clamp(1rem, 1vw + 1rem, 2rem)`, where the browser will scale between `1rem` and `2rem`, trying to always be `1vw + 1rem`, assuming it doesn't drop below the minimum, or exceed the maximum values.
While this is good, it doesn't provide an obvious way to cap _where_ the minimum and maximums should be, and therefore how aggressively it should interpolate betweeen the two. It is possible, but isn't as clear as a CSS lock. Without some reasonably heavy mathematics, `clamp()` seems to be most useful when you want broadly fluid typography, without being 100% specific about the relationship between the varying sizes.
If you need more precision for a single typographic size, Pedro Rodriguez has written a [fantastic article](https://css-tricks.com/linearly-scale-font-size-with-css-clamp-based-on-the-viewport/) that gives you all the maths, and explains how to use `clamp()` to interpolate between two viewports and sizes. It includes a calculator to work out the angle and intersection point of the slope, required to accurately scale typography.
## Preparing clamp() for typographic scales
Utopia strives for precision, flexibility, and ease of use, helping you create harmonious and fluid typographic scales. We therefore wanted to see how Utopia could incorporate `clamp()` most effectively. For this example, we're going to interpolate between:  
|   | Min Font Size  | Max Font Size  | Min Viewport  | Max Viewport  |   |  
| --- | --- | --- | --- | --- | --- |  
|   | 1rem  | 2rem  | 320px  | 1440px  |   |  
### The equation
Here's the equation (thanks to Pedro) for calculating the clamp:

```
Slope = (MaxSize - MinSize) / (MaxWidth - MinWidth)
yIntersection = (-1 * MinWidth) * Slope + MinSize
font-size: clamp(MinSize[rem], yIntersection[rem] + Slope * 100vw, MaxSize[rem])

```

As with every abstraction, there's a trade-off between verbosity and flexibility. Here are three examples on that scale:
### 1. Move the calculation into CSS

```
:root {
  --f-max-w: 90; // 1440px in REM
  --f-min-w: 20; // 320px in REM
  --f-minus: (-1 * var(--f-min-w)); // Precalcuation for the -MinWidth we need
  --f-w: (var(--f-max-w) - var(--f-min-w)); // Precalculation for the (MaxWidth - MinWidth) we need

  /* Per step size */
  --f-0-min: 1; // Min font size
  --f-0-max: 2; // Max font size
  --f-0-slope: (var(--f-0-max) - var(--f-0-min)) / (var(--f-max-w) - var(--f-min-w));
  --f-0-intersection: ((-1 * var(--f-min-w)) * var(--f-slope) + var(--f-0-min));
  --step-0: clamp(var(--f-0-min) * 1rem, var(--f-0-intersection) * 1rem + var(--f-0-slope) * 100vw, var(--f-0-max) * 1rem);
}

```

We can recreate that calculation directly in CSS using Custom Properties. The first aim is to expose the four parameters: Min & Max font size, and Min & Max viewport. Given Utopia is concerned about the relationship between _multiple_ typographic sizes, we will separate the viewport sizing, and the steps themselves, to avoid duplication.
Each step calculates the slope and intersection as per the equation above, but with substituted custom properties.
### 2. One-line the calculation

```
:root {
  --f-max-w: 90; // 1440px in REM
  --f-min-w: 20; // 320px in REM
  --f-minus: (-1 * var(--f-min-w)); // Precalcuation for the -MinWidth we need
  --f-w: (var(--f-max-w) - var(--f-min-w)); // Precalculation for the (MaxWidth - MinWidth) we need
  
  /* Per step size */
  --f-0-min: 1; // Min font size
  --f-0-max: 2; // Max font size
  --step-0: clamp(var(--f-0-min) * 1rem, ((var(--f-minus) * ((var(--f-0-max) - var(--f-0-min)) / var(--f-w)) + var(--f-0-min)) * 1rem) + ((var(--f-0-max) - 1) / var(--f-w) * 100vw), var(--f-0-max) * 1rem);
}

```

It's possible to 'one-line' option 1. Not hugely readable, but vertically succinct, and still flexible.
### 3. Fully pre-calculated

```
:root {
  --step-0: clamp(1rem, 0.7143rem + 1.4286vw, 2rem);
}

```

Using [Pedro's formula](https://css-tricks.com/linearly-scale-font-size-with-css-clamp-based-on-the-viewport/), we can precalculate the `clamp()`—it's pretty darn elegant. One line, and total fluid type without a media query. The only complaint: the 'preferred' value isn't at all clear to read, and impossible to work out without a calculator. Changing the preferred value, or the `1rem/2rem` will also break the function.
## Adding clamp to Utopia
We've added the option to generate Utopian scales using `clamp()`, opting for the precalculated option. A pre-calculated clamp is considerably more succinct than a CSS lock, even if the result is less readable. If you're happy with that trade-off and are aware of the potential accessibility impacts, you can generate and download the `clamp()` version of Utopia with the [generator](https://utopia.fyi/generator-mk-ii).
## The dangers of clamp
[Adrian Roselli](https://adrianroselli.com/2019/12/responsive-type-and-zoom.html) quite rightly warns that clamp can have a knock-on effect to the maximum font-size when the user explicitly sets a browser text zoom preference. As with any feature affecting typography, **ensure you test thoroughly** before using in production.
* * *
First published on 25 September 2020
Created by [James Gilyead](https://www.hustlersquad.net/) & [Trys Mudford](https://www.trysmudford.com)
Supported by
[Clearleft ](https://clearleft.com)

