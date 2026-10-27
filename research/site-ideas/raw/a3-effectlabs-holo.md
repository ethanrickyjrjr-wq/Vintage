[Effect.Labs](https://effect-labs.com/en/) [ FR ](https://effect-labs.com/pages/blog/effet-holographique-css.html "Version française")
[Effects ▾](https://effect-labs.com/en/pages/tous-les-effets.html)[Templates](https://effect-labs.com/en/pages/templates.html)[Blog](https://effect-labs.com/en/pages/blog.html)[♥](https://effect-labs.com/en/pages/favorites.html "Favorites")[✨ Premium](https://effect-labs.com/en/#pricing)
[Effect.Labs](https://effect-labs.com/en/) ×
#### Fundamentals
[Buttons](https://effect-labs.com/en/pages/buttons.html) [Text & Typography](https://effect-labs.com/en/pages/text.html) [Forms](https://effect-labs.com/en/pages/forms.html) [Navigation & UI](https://effect-labs.com/en/pages/navigation.html) [Loaders](https://effect-labs.com/en/pages/loaders.html)
#### Design & Visuals
[Backgrounds](https://effect-labs.com/en/pages/backgrounds.html) [Glass & Morphism](https://effect-labs.com/en/pages/glassmorphism.html) [Visual Effects](https://effect-labs.com/en/pages/distortion.html) [Liquid & Morphing](https://effect-labs.com/en/pages/liquid.html) [SVG & Art](https://effect-labs.com/en/pages/svg.html)
#### Animations & Scroll
[Scroll & Parallax](https://effect-labs.com/en/pages/scroll.html) [Transitions](https://effect-labs.com/en/pages/transitions.html) [Hover & Interactions](https://effect-labs.com/en/pages/hover.html) [3D & Depth](https://effect-labs.com/en/pages/3d.html) [Cursors](https://effect-labs.com/en/pages/cursors.html)[Gestures & Webcam](https://effect-labs.com/en/pages/gestures.html)
#### Gallery & More
[Cards & Layouts](https://effect-labs.com/en/pages/cards.html) [Gallery & Media](https://effect-labs.com/en/pages/carousel.html) [Data & Visualization](https://effect-labs.com/en/pages/dataviz.html) [Atmosphere](https://effect-labs.com/en/pages/particle-systems.html) [Utilities](https://effect-labs.com/en/pages/utilities.html)
[Favorites](https://effect-labs.com/en/pages/favorites.html) [Templates](https://effect-labs.com/en/pages/templates.html) [Blog](https://effect-labs.com/en/pages/blog.html) [Tips](https://effect-labs.com/en/pages/astuces.html) [✨ Go Premium](https://effect-labs.com/en/#pricing)
[Blog](https://effect-labs.com/en/pages/blog.html) / CSS
CSS
# CSS Holographic Effect: Iridescent and Chrome
Discover how to create spectacular holographic effects in pure CSS: rainbow iridescent, metallic chrome, Pokemon-style cards, prisms and foil effects. Complete tutorial with interactive demos.
EL
Effect.Labs
Editorial team
4 Fev 2026  8 min read 
## Introduction
Holographic effects are among the most striking trends in modern web design. Inspired by trading cards, premium packaging and cyberpunk aesthetics, these effects add a unique visual dimension to your interfaces.
In this in-depth tutorial, we will explore **5 different techniques** to create holographic effects in pure CSS. Each technique is accompanied by an interactive demo and the complete code.
💡
Prerequisites
This tutorial assumes a basic knowledge of CSS, including gradients, `@keyframes` animations and `::before` and `::after` pseudo-elements.
## 1. Iridescent effect (animated rainbow)
The iridescent effect reproduces the shifting reflections seen on soap bubbles or CDs. It uses an animated multicolor gradient that gives the impression of colors moving across the element's surface.
Iridescent
iridescent.css
Copy 

```
.iridescent {
  width: 200px;
  height: 200px;
  border-radius: 20px;
  position: relative;
  overflow: hidden;

  /* Gradient arc-en-ciel */
  background: linear-gradient(
    135deg,
    #ff0080 0%,
    #ff8c00 14%,
    #40e0d0 28%,
    #7b68ee 42%,
    #ff0080 57%,
    #ff8c00 71%,
    #40e0d0 85%,
    #7b68ee 100%
  );
  background-size: 400% 400%;
  animation: iridescent 4s ease infinite;
}

/* Additional shine effect */
.iridescent::before {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(
    45deg,
    transparent 30%,
    rgba(255,255,255,0.4) 50%,
    transparent 70%
  );
  background-size: 200% 200%;
  animation: shimmer 2s ease-in-out infinite;
}

@keyframes iridescent {
  0%, 100% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
}

@keyframes shimmer {
  0% { background-position: -100% -100%; }
  100% { background-position: 100% 100%; }
}
```

### Key points of the technique
  * **Color repetition** : The gradient repeats colors for a smooth transition during the animation
  * **background-size: 400%** : Allows moving the gradient over a large surface
  * **::before pseudo-element** : Adds a white reflection that crosses the element


## 2. Chrome / Metallic effect
The chrome effect simulates a reflective metallic surface. It uses transitions between dark and light tones to create the illusion of reflections.
Chrome
chrome.css
Copy 

```
.chrome {
  width: 200px;
  height: 200px;
  border-radius: 20px;
  position: relative;

  /* Gradient metallique */
  background: linear-gradient(
    135deg,
    #1a1a2e 0%,
    #4a4a6a 20%,
    #e8e8e8 40%,
    #4a4a6a 60%,
    #1a1a2e 80%,
    #4a4a6a 100%
  );
  background-size: 200% 200%;
  animation: chrome 3s ease infinite;

  /* Shadows for depth */
  box-shadow:
    0 10px 40px rgba(0,0,0,0.4),
    inset 0 1px 0 rgba(255,255,255,0.3),
    inset 0 -1px 0 rgba(0,0,0,0.2);
}

/* Top reflection */
.chrome::after {
  content: '';
  position: absolute;
  inset: 2px;
  border-radius: 18px;
  background: linear-gradient(
    180deg,
    rgba(255,255,255,0.2) 0%,
    transparent 50%
  );
  pointer-events: none;
}

@keyframes chrome {
  0%, 100% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
}
```

### Tips for realistic chrome
  * **High contrast** : Alternate between very dark and very light tones
  * **Inner shadows** : Use `inset box-shadow` to simulate beveled edges
  * **Top highlight** : A white gradient at the top adds realism


## 3. Holographic card (Pokemon style)
This effect reproduces the famous holographic trading cards. The effect activates on hover and reacts to mouse movement for an ultra-realistic result.
★
Carte Rare
Hover for holo effect
holo-card.css
Copy 

```
.holo-card {
  width: 220px;
  height: 300px;
  border-radius: 16px;
  background: linear-gradient(135deg, #1a1a2e, #2d2d44);
  position: relative;
  overflow: hidden;
  cursor: pointer;
  transform-style: preserve-3d;
  transition: transform 0.1s;
  box-shadow: 0 20px 50px rgba(0,0,0,0.5);
}

/* Overlay holographique */
.holo-card::before {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(
    125deg,
    #ff0080, #ff8c00, #40e0d0, #7b68ee,
    #ff0080, #ff8c00, #40e0d0, #7b68ee,
    #ff0080, #ff8c00, #40e0d0
  );
  background-size: 200% 200%;
  opacity: 0;
  mix-blend-mode: color-dodge;
  transition: opacity 0.3s;
  animation: holoGradient 5s ease infinite;
  pointer-events: none;
}

/* Holographic grid */
.holo-card::after {
  content: '';
  position: absolute;
  inset: 0;
  background:
    repeating-linear-gradient(
      0deg,
      transparent, transparent 2px,
      rgba(255,255,255,0.03) 2px,
      rgba(255,255,255,0.03) 4px
    ),
    repeating-linear-gradient(
      90deg,
      transparent, transparent 2px,
      rgba(255,255,255,0.03) 2px,
      rgba(255,255,255,0.03) 4px
    );
  opacity: 0;
  transition: opacity 0.3s;
  pointer-events: none;
}

/* Activation on hover */
.holo-card:hover::before { opacity: 0.7; }
.holo-card:hover::after { opacity: 1; }

@keyframes holoGradient {
  0%, 100% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
}
```

🛠
Interactive 3D effect
For an even more immersive effect, add JavaScript to make the card tilt follow the mouse movement. The code is provided in the JavaScript section below.
**35+ card effects ready to copy**
Live preview, customizer, vanilla code — zero dependencies.
[Browse card effects](https://effect-labs.com/en/pages/cards.html#effect-holo-tilt-glare)
## 4. Prism / Refraction effect
The prism effect simulates the decomposition of white light into a color spectrum, as through a glass prism. It uses a `conic-gradient` to create the spectrum.
PRISME
prism.css
Copy 

```
.prism {
  width: 200px;
  height: 200px;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
}

/* Color spectrum */
.prism::before {
  content: '';
  position: absolute;
  width: 100%;
  height: 100%;
  background: conic-gradient(
    from 0deg,
    #ff0000, #ff8000, #ffff00,
    #80ff00, #00ff00, #00ff80,
    #00ffff, #0080ff, #0000ff,
    #8000ff, #ff00ff, #ff0080,
    #ff0000
  );
  /* Forme triangulaire */
  clip-path: polygon(50% 0%, 100% 100%, 0% 100%);
  animation: prismRotate 8s linear infinite;
}

/* Dark center of the prism */
.prism::after {
  content: '';
  position: absolute;
  width: 90%;
  height: 90%;
  background: rgba(10, 10, 15, 0.8);
  clip-path: polygon(50% 5%, 95% 95%, 5% 95%);
}

@keyframes prismRotate {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}
```

## 5. Foil Stamp effect (gilding)
The foil stamp effect reproduces the gold or silver finishes found on luxury packaging and premium business cards. It combines a metallic gradient with a shine effect.
PREMIUM
Edition limitee
foil-stamp.css
Copy 

```
.foil-text {
  font-size: 1.5rem;
  font-weight: 900;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  position: relative;

  /* Gradient dore */
  background: linear-gradient(
    90deg,
    #bf953f,
    #fcf6ba,
    #b38728,
    #fbf5b7,
    #aa771c,
    #bf953f
  );
  background-size: 200% 100%;

  /* Apply to text */
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;

  animation: foilShine 3s linear infinite;
}

/* Sweeping shine effect */
.foil-text::after {
  content: attr(data-text);
  position: absolute;
  inset: 0;
  background: linear-gradient(
    120deg,
    transparent 30%,
    rgba(255,255,255,0.8) 50%,
    transparent 70%
  );
  background-size: 200% 100%;
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: foilGlint 2s ease-in-out infinite;
}

@keyframes foilShine {
  0% { background-position: 0% 50%; }
  100% { background-position: 200% 50%; }
}

@keyframes foilGlint {
  0%, 100% { background-position: -100% 0; }
  50% { background-position: 200% 0; }
}
```

### Color variants
You can easily adapt the foil effect for other metallic finishes:
  * **Silver** : `#c0c0c0, #ffffff, #808080, #ffffff, #a8a8a8`
  * **Rose gold** : `#b76e79, #f5d0c5, #d4a5a5, #f5d0c5, #b76e79`
  * **Bronze** : `#cd7f32, #e6c89c, #8b4513, #daa520, #cd7f32`


## Best practices
### Performance
  * **Limit animations** : Animated gradients can be resource-intensive. Use `will-change: background-position` if necessary
  * **Prefer transform and opacity** : These properties are GPU-optimized
  * **Test on mobile** : Complex effects can slow down less powerful devices


### Accessibility
accessibility.css
Copy 

```
/* Respect user preferences */
@media (prefers-reduced-motion: reduce) {
  .iridescent,
  .chrome,
  .holo-card::before,
  .prism::before,
  .foil-text,
  .foil-text::after {
    animation: none;
  }
}

/* Alternative for high contrast */
@media (prefers-contrast: high) {
  .foil-text {
    background: #d4af37;
    -webkit-text-fill-color: initial;
    color: #000;
  }
}
```

⚠
Epilepsy warning
Fast animations and bright color changes can trigger seizures in photosensitive individuals. Avoid flashing above 3 Hz.
### Design
  * **Dark background recommended** : Holographic effects stand out better on dark backgrounds
  * **Use sparingly** : A single holographic element per section is sufficient
  * **Appropriate context** : Reserve these effects for premium elements, badges, or special cards


## Interactive JavaScript (bonus)
For the holographic card, here is the JavaScript that makes the effect react to mouse movement:
holo-card.js
Copy 

```
const card = document.querySelector('.holo-card');

card.addEventListener('mousemove', (e) => {
  const rect = card.getBoundingClientRect();
  const x = e.clientX - rect.left;
  const y = e.clientY - rect.top;

  // Calculate rotation (-15 to 15 degrees)
  const centerX = rect.width / 2;
  const centerY = rect.height / 2;
  const rotateX = (y - centerY) / centerY * -15;
  const rotateY = (x - centerX) / centerX * 15;

  card.style.transform =
    `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg)`;
});

card.addEventListener('mouseleave', () => {
  card.style.transform = 'perspective(1000px) rotateX(0) rotateY(0)';
});
```

## Conclusion
Holographic effects are an excellent way to add a premium and modern touch to your interfaces. By mastering animated gradients, pseudo-elements and CSS blend modes, you can create visually impressive effects without any external dependency.
Don't forget to always test your effects on different devices and respect users' accessibility preferences. Use these techniques sparingly to maximize their visual impact.
🎨
Explore further
Find over 50 visual effects ready to use in our [effects library](https://effect-labs.com/en/#categories), with copyable code and interactive demos.
Don't miss the next effects: [follow @effect_labs on X](https://x.com/intent/follow?screen_name=effect_labs)
Table of Contents
  * [Introduction](https://effect-labs.com/en/pages/blog/effet-holographique-css.html#introduction)
  * [1. Iridescent effect](https://effect-labs.com/en/pages/blog/effet-holographique-css.html#iridescent)
  * [2. Chrome effect](https://effect-labs.com/en/pages/blog/effet-holographique-css.html#chrome)
  * [3. Carte holographique](https://effect-labs.com/en/pages/blog/effet-holographique-css.html#holographic-card)
  * [4. Prism effect](https://effect-labs.com/en/pages/blog/effet-holographique-css.html#prism)
  * [5. Foil Stamp Effect](https://effect-labs.com/en/pages/blog/effet-holographique-css.html#foil)
  * [Best practices](https://effect-labs.com/en/pages/blog/effet-holographique-css.html#best-practices)
  * [JavaScript (bonus)](https://effect-labs.com/en/pages/blog/effet-holographique-css.html#javascript)
  * [Conclusion](https://effect-labs.com/en/pages/blog/effet-holographique-css.html#conclusion)


Share
## Related Articles
[ CSS Create a Glow Button with Pure CSS 8 min read ](https://effect-labs.com/en/pages/blog/bouton-glow-css.html) [ CSS / JS Interactive 3D Cards with CSS and JavaScript 10 min read ](https://effect-labs.com/en/pages/blog/cartes-3d-interactives.html) [ CSS Animated Backgrounds in Modern CSS 7 min read ](https://effect-labs.com/en/pages/blog/backgrounds-animes-css.html)
## Get our tutorials
One technical article per week, straight to your inbox.
Subscribe
### Effect.Labs
The largest library of CSS and JavaScript effects to create exceptional websites.
[](https://x.com/effect_labs "@effect_labs sur X")
#### Product
[All effects](https://effect-labs.com/en/#categories) [Pricing](https://effect-labs.com/en/#pricing) [FAQ](https://effect-labs.com/en/#faq) [Tips](https://effect-labs.com/en/pages/astuces.html)
#### Categories
[Buttons](https://effect-labs.com/en/pages/buttons.html) [Text](https://effect-labs.com/en/pages/text.html) [Cards](https://effect-labs.com/en/pages/cards.html) [Loaders](https://effect-labs.com/en/pages/loaders.html)
#### Legal
[Legal notices](https://effect-labs.com/en/pages/mentions-legales.html) [Terms](https://effect-labs.com/en/pages/cgv.html) [Privacy](https://effect-labs.com/en/pages/confidentialite.html) [Contact & Support](https://effect-labs.com/en/pages/contact.html)
© 2026 Effect.Labs - All rights reserved
[🆕 New](https://effect-labs.com/en/pages/nouveautes.html)[🎛️ Generators Premium](https://effect-labs.com/en/pages/generators.html)[All effects →](https://effect-labs.com/en/pages/tous-les-effets.html)
[🔘Buttons27 effects](https://effect-labs.com/en/pages/buttons.html)[✍️Text & Type56 effects](https://effect-labs.com/en/pages/text.html)[🃏Cards & Layouts33 effects](https://effect-labs.com/en/pages/cards.html)[🌌Backgrounds50 effects](https://effect-labs.com/en/pages/backgrounds.html)[👆Hover & Interactions48 effects](https://effect-labs.com/en/pages/hover.html)[⏳Loading28 effects](https://effect-labs.com/en/pages/loaders.html)[📜Scroll & Parallax64 effects](https://effect-labs.com/en/pages/scroll.html)[🧭Navigation & UI36 effects](https://effect-labs.com/en/pages/navigation.html)[🖱️Cursors26 effects](https://effect-labs.com/en/pages/cursors.html)[🖐️Gestures & Webcam11 effects](https://effect-labs.com/en/pages/gestures.html)[🔷3D & Depth50 effects](https://effect-labs.com/en/pages/3d.html)[📊Data & Dataviz28 effects](https://effect-labs.com/en/pages/dataviz.html)[📝Forms20 effects](https://effect-labs.com/en/pages/forms.html)[📺Visual Effects30 effects](https://effect-labs.com/en/pages/distortion.html)[🌊Liquid & Morphing30 effects](https://effect-labs.com/en/pages/liquid.html)[🧊Glass & Morphism42 effects](https://effect-labs.com/en/pages/glassmorphism.html)[🔄Transitions50 effects](https://effect-labs.com/en/pages/transitions.html)[🎨SVG & Generative28 effects](https://effect-labs.com/en/pages/svg.html)[🎠Gallery & Media46 effects](https://effect-labs.com/en/pages/carousel.html)[💫Particles50 effects](https://effect-labs.com/en/pages/particle-systems.html)[🔧Utilities40 effects](https://effect-labs.com/en/pages/utilities.html)

