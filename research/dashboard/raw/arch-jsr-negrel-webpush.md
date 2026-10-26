[Skip to main content](https://jsr.io/@negrel/webpush#main-content)
[HomeJSR](https://jsr.io/)
Search for packages
[PackagesBrowse packages](https://jsr.io/packages)|[Docs](https://jsr.io/docs)||[Sign in](https://jsr.io/login?redirect=%2F%40negrel%2Fwebpush)
Search for packages
# 
[@negrel](https://jsr.io/@negrel)/[webpush](https://jsr.io/@negrel/webpush)@0.5.0
Built and signed on GitHub Actions
Built and signed on GitHub Actions
latest
[negrel/webpush](https://github.com/negrel/webpush)
Works with
This package works with Cloudflare Workers, Deno, Bun, Browsers
![This package works with Cloudflare Workers](https://jsr.io/logos/cloudflare-workers.svg?__frsh_c=1624825e0783b6921e99693e10e30ae67b44119b)
![This package works with Deno](https://jsr.io/logos/deno.svg?__frsh_c=1624825e0783b6921e99693e10e30ae67b44119b)
![This package works with Bun](https://jsr.io/logos/bun.svg?__frsh_c=1624825e0783b6921e99693e10e30ae67b44119b)
![This package works with Browsers](https://jsr.io/logos/browsers.svg?__frsh_c=1624825e0783b6921e99693e10e30ae67b44119b)
•[JSR Score100%](https://jsr.io/@negrel/webpush/score)•
Downloads13,415/wk
•
Publisheda year ago (0.5.0)
Web Push library for Deno and other web compatible runtime.
[ Weekly downloads 13,415 ](https://jsr.io/@negrel/webpush/versions)
[Overview](https://jsr.io/@negrel/webpush)[Docs](https://jsr.io/@negrel/webpush/doc)[Files](https://jsr.io/@negrel/webpush/0.5.0)[Versions5](https://jsr.io/@negrel/webpush/versions)[Dependencies3](https://jsr.io/@negrel/webpush/dependencies)[Dependents1](https://jsr.io/@negrel/webpush/dependents)[Score](https://jsr.io/@negrel/webpush/score) 

#  [ ](https://jsr.io/@negrel/webpush#webpush---web-push-library-for-deno-and-other-web-compatible-runtime.)`webpush` - Web Push library for Deno and other web compatible runtime.
![jsr badge](https://jsr.io/badges/@negrel/webpush) ![license MIT badge](https://img.shields.io/github/license/negrel/webpush) ![code size badge](https://img.shields.io/github/languages/code-size/negrel/webpush)
`webpush` is a Web Push library ([RFC 8291](https://www.rfc-editor.org/rfc/rfc8291) and [RFC 8292](https://www.rfc-editor.org/rfc/rfc8292)) based on Web APIs.
> NOTE: This library hasn't been reviewed by crypto experts and may be unsecure. I've done my best to follow RFC recommandation and I only used primitives provided by the SubtleCrypto API.
`webpush` is available on [JSR](https://jsr.io/@negrel/webpush).
##  [ ](https://jsr.io/@negrel/webpush#getting-started)Getting started
Before sending Web Push message to a user agent, you need to create VAPID keys (see [RFC 8292](https://www.rfc-editor.org/rfc/rfc8292)) to identify your server (`Application`) to the `Push Service`:

```
+-------+           +--------------+       +-------------+
|  UA   |           | Push Service |       | Application |
+-------+           +--------------+       +-------------+
    |                      |                      |
    |        Setup         |                      |
    |<====================>|                      |
    |           Provide Subscription              |
    |-------------------------------------------->|
    |                      |                      |
    :                      :                      :
    |                      |     Push Message     |
    |    Push Message      |<---------------------|
    |<---------------------|                      |
    |                      |                      |

  
  
  


  
  


```

Run [`generate-vapid-keys`](https://github.com/negrel/webpush/blob/master/cmd/generate-vapid-keys.ts) script part of this repository to generate new keys:

```
# You can use any Web compatible runtime.
$ deno run https://raw.githubusercontent.com/negrel/webpush/master/cmd/generate-vapid-keys.ts

  
  
  


  
  


```

Copy the output of the command and save it in `example/vapid.json`. Now you can run example server.

```
$ cd example/
$ deno run -A ./main.ts

  
  
  


  
  


```

Code is commented be sure to read it.
I also wrote an [ok-ish blog post about Web Push and this library](https://www.negrel.dev/blog/deno-web-push-notifications/).
##  [ ](https://jsr.io/@negrel/webpush#dependencies)Dependencies
This library tries its best at keeping the minimum number of dependencies. It has no external dependencies except some runtime agnostic [`@std/`](https://jsr.io/@std/) packages maintained by Deno team and [`http-ece`](https://github.com/negrel/http-ece), which I maintain.
[`http-ece`](https://github.com/negrel/http-ece) also only depends on [`@std/`](https://jsr.io/@std/) packages.
##  [ ](https://jsr.io/@negrel/webpush#contributing)Contributing
If you want to contribute to `webpush` to add a feature or improve the code contact me at alexandre@negrel.dev, open an [issue](https://github.com/negrel/webpush/issues) or make a [pull request](https://github.com/negrel/webpush/pulls).
##  [ ](https://jsr.io/@negrel/webpush#:stars:-show-your-support):stars: Show your support
Please give a :star: if this project helped you!
[![buy me a coffee](https://github.com/negrel/.github/blob/master/.github/images/bmc-button.png?raw=true)](https://www.buymeacoffee.com/negrel)
##  [ ](https://jsr.io/@negrel/webpush#:scroll:-license):scroll: License
MIT © [Alexandre Negrel](https://www.negrel.dev/)
Built and signed on
GitHub Actions
[View transparency log](https://search.sigstore.dev/?logIndex=255556468)
Report package
## Report package
Please provide a reason for reporting this package. We will review your report and take appropriate action.
Please review the [JSR usage policy](https://jsr.io/docs/usage-policy#package-contents-and-metadata) before submitting a report.
Reason*
Cancel
### Use with
![Deno logo](https://jsr.io/logos/deno.svg?__frsh_c=1624825e0783b6921e99693e10e30ae67b44119b)
Deno
![Deno logo](https://jsr.io/logos/deno.svg?__frsh_c=1624825e0783b6921e99693e10e30ae67b44119b)
Deno
![pnpm logo](https://jsr.io/logos/pnpm_textless.svg?__frsh_c=1624825e0783b6921e99693e10e30ae67b44119b)
pnpm
![Yarn logo](https://jsr.io/logos/yarn_textless.svg?__frsh_c=1624825e0783b6921e99693e10e30ae67b44119b)
Yarn
![vlt logo](https://jsr.io/logos/vlt.svg?__frsh_c=1624825e0783b6921e99693e10e30ae67b44119b)
vlt
![npm logo](https://jsr.io/logos/npm_textless.svg?__frsh_c=1624825e0783b6921e99693e10e30ae67b44119b)
npm
![Bun logo](https://jsr.io/logos/bun.svg?__frsh_c=1624825e0783b6921e99693e10e30ae67b44119b)
Bun
Add Package

```
deno add jsr:@negrel/webpush

  
  
  


  
  


```

Import symbol

```
import * as webpush from "@negrel/webpush";

  
  
  


  
  


```

or
Import directly with a jsr specifier

```
import * as webpush from "jsr:@negrel/webpush@^0.5.0";

  
  
  


  
  


```

### Symbols
  * [I ExportedVapidKeys](https://jsr.io/@negrel/webpush/doc/~/ExportedVapidKeys "ExportedVapidKeys")
  * [f generateVapidKeys](https://jsr.io/@negrel/webpush/doc/~/generateVapidKeys "generateVapidKeys")
  * [f importVapidKeys](https://jsr.io/@negrel/webpush/doc/~/importVapidKeys "importVapidKeys")
  * [f exportVapidKeys](https://jsr.io/@negrel/webpush/doc/~/exportVapidKeys "exportVapidKeys")
  * [f exportApplicationServerKey](https://jsr.io/@negrel/webpush/doc/~/exportApplicationServerKey "exportApplicationServerKey")

[view all 11 symbols](https://jsr.io/@negrel/webpush/doc/all_symbols)
### Document Navigation
  * [webpush - Web Push library for Deno and other web compatible runtime.](https://jsr.io/@negrel/webpush#webpush---web-push-library-for-deno-and-other-web-compatible-runtime. "webpush - Web Push library for Deno and other web compatible runtime.")
    * [Getting started](https://jsr.io/@negrel/webpush#getting-started "Getting started")
    * [Dependencies](https://jsr.io/@negrel/webpush#dependencies "Dependencies")
    * [Contributing](https://jsr.io/@negrel/webpush#contributing "Contributing")
    * [:stars: Show your support](https://jsr.io/@negrel/webpush#:stars:-show-your-support ":stars: Show your support")
    * [:scroll: License](https://jsr.io/@negrel/webpush#:scroll:-license ":scroll: License")


JSR - It is 2026/10/26, 18:55:53 UTC - [Docs](https://jsr.io/docs) - [GitHub](https://github.com/jsr-io/jsr) - [Discord](https://discord.gg/hMqvhAn9xG) - [Bluesky](https://bsky.app/profile/jsr.io) - [X (ex Twitter)](https://x.com/jsr_io) - [YouTube](https://www.youtube.com/@jsr-io)

