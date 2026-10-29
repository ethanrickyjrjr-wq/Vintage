<!-- COMPUTED locally 2026-10-29 with Utopia's published formula (utopia-blog-clamp.md): slope=(max-min)/(maxVW-minVW); intercept=-minVW*slope+min; clamp(min, intercept + slope*100vw, max). Script: scripts/utopia.py -->
Utopia steps, base 16->18, ratio 1.2->1.25, viewports 360->1500
step -2        11.11->  11.52px  clamp(0.6944rem, 0.6864rem + 0.0359vw, 0.7200rem)   @768=11.3px @1024=11.3px  200%-zoom@1500 ratio 1.95x
step -1        13.33->  14.40px  clamp(0.8333rem, 0.8123rem + 0.0936vw, 0.9000rem)   @768=13.7px @1024=14.0px  200%-zoom@1500 ratio 1.90x
step +0        16.00->  18.00px  clamp(1.0000rem, 0.9605rem + 0.1754vw, 1.1250rem)   @768=16.7px @1024=17.2px  200%-zoom@1500 ratio 1.85x
step +1        19.20->  22.50px  clamp(1.2000rem, 1.1349rem + 0.2895vw, 1.4062rem)   @768=20.4px @1024=21.1px  200%-zoom@1500 ratio 1.81x
step +2        23.04->  28.12px  clamp(1.4400rem, 1.3396rem + 0.4461vw, 1.7578rem)   @768=24.9px @1024=26.0px  200%-zoom@1500 ratio 1.76x
step +3        27.65->  35.16px  clamp(1.7280rem, 1.5798rem + 0.6586vw, 2.1973rem)   @768=30.3px @1024=32.0px  200%-zoom@1500 ratio 1.72x
step +4        33.18->  43.95px  clamp(2.0736rem, 1.8611rem + 0.9445vw, 2.7466rem)   @768=37.0px @1024=39.4px  200%-zoom@1500 ratio 1.68x
step +5        39.81->  54.93px  clamp(2.4883rem, 2.1899rem + 1.3262vw, 3.4332rem)   @768=45.2px @1024=48.6px  200%-zoom@1500 ratio 1.64x
step +6        47.78->  68.66px  clamp(2.9860rem, 2.5737rem + 1.8324vw, 4.2915rem)   @768=55.3px @1024=59.9px  200%-zoom@1500 ratio 1.60x

hero           56.00-> 130.00px  clamp(3.5000rem, 2.0395rem + 6.4912vw, 8.1250rem)   @768=82.5px @1024=99.1px  200%-zoom@1500 ratio 1.25x
hero(86 now)   86.00-> 130.00px  clamp(5.3750rem, 4.5066rem + 3.8596vw, 8.1250rem)   @768=101.7px @1024=111.6px  200%-zoom@1500 ratio 1.55x
label          11.00->  12.00px  clamp(0.6875rem, 0.6678rem + 0.0877vw, 0.7500rem)   @768=11.4px @1024=11.6px  200%-zoom@1500 ratio 1.89x
current hero @360/768/1024/1500: [86, 86, 86, 124.5]  200%-zoom ratio 1.38

hero52         52.00-> 130.00px  clamp(3.2500rem, 1.7105rem + 6.8421vw, 8.1250rem)   @768=79.9px @1024=97.4px  200%-zoom@1500 ratio 1.21x
gutter         16.00->  32.00px  clamp(1.0000rem, 0.6842rem + 1.4035vw, 2.0000rem)   @768=21.7px @1024=25.3px  200%-zoom@1500 ratio 1.34x
section        48.00->  96.00px  clamp(3.0000rem, 2.0526rem + 4.2105vw, 6.0000rem)   @768=65.2px @1024=76.0px  200%-zoom@1500 ratio 1.34x
sec-gap        24.00->  48.00px  clamp(1.5000rem, 1.0263rem + 2.1053vw, 3.0000rem)   @768=32.6px @1024=38.0px  200%-zoom@1500 ratio 1.34x
body zoom 2/3/5x -> on-screen text growth vs 100% at 1500px: {2: 1.85, 3: 2.71, 5: 4.44}
h2 zoom 2/3/5x -> on-screen text growth vs 100% at 1500px: {2: 1.72, 3: 2.44, 5: 3.93}
h1 zoom 2/3/5x -> on-screen text growth vs 100% at 1500px: {2: 1.64, 3: 2.28, 5: 3.62}
hero52 zoom 2/3/5x -> on-screen text growth vs 100% at 1500px: {2: 1.21, 3: 1.42, 5: 2.0}
hero80 zoom 2/3/5x -> on-screen text growth vs 100% at 1500px: {2: 1.49, 3: 1.99, 5: 3.08}
hero86 zoom 2/3/5x -> on-screen text growth vs 100% at 1500px: {2: 1.55, 3: 2.11, 5: 3.31}
