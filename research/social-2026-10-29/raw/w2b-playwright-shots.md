[Skip to main content](https://playwright.dev/docs/screenshots#__docusaurus_skipToContent_fallback)
[ ![Playwright logo](https://playwright.dev/img/playwright-logo.svg)![Playwright logo](https://playwright.dev/img/playwright-logo.svg) **Playwright**](https://playwright.dev/)[Docs](https://playwright.dev/docs/intro)[MCP](https://playwright.dev/mcp/introduction)[CLI](https://playwright.dev/agent-cli/introduction)[API](https://playwright.dev/docs/api/class-playwright)
[Node.js](https://playwright.dev/docs/screenshots)
  * [Node.js](https://playwright.dev/docs/screenshots)
  * [Python](https://playwright.dev/python/docs/screenshots)
  * [Java](https://playwright.dev/java/docs/screenshots)
  * [.NET](https://playwright.dev/dotnet/docs/screenshots)


[](https://github.com/microsoft/playwright)[](https://aka.ms/playwright/discord)
Search
  * [Getting Started](https://playwright.dev/docs/intro)
    * [Installation](https://playwright.dev/docs/intro)
    * [Writing tests](https://playwright.dev/docs/writing-tests)
    * [Generating tests](https://playwright.dev/docs/codegen-intro)
    * [Running and debugging tests](https://playwright.dev/docs/running-tests)
    * [Trace viewer](https://playwright.dev/docs/trace-viewer-intro)
    * [Setting up CI](https://playwright.dev/docs/ci-intro)
    * [VS Code](https://playwright.dev/docs/getting-started-vscode)
  * [Release notes](https://playwright.dev/docs/release-notes)
  * [Canary releases](https://playwright.dev/docs/canary-releases)
  * [Playwright Test](https://playwright.dev/docs/test-agents)
    * [Agents](https://playwright.dev/docs/test-agents)
    * [Annotations](https://playwright.dev/docs/test-annotations)
    * [Command line](https://playwright.dev/docs/test-cli)
    * [Configuration](https://playwright.dev/docs/test-configuration)
    * [Configuration (use)](https://playwright.dev/docs/test-use-options)
    * [Emulation](https://playwright.dev/docs/emulation)
    * [Fixtures](https://playwright.dev/docs/test-fixtures)
    * [Global setup and teardown](https://playwright.dev/docs/test-global-setup-teardown)
    * [Parallelism](https://playwright.dev/docs/test-parallel)
    * [Parameterize tests](https://playwright.dev/docs/test-parameterize)
    * [Projects](https://playwright.dev/docs/test-projects)
    * [Reporters](https://playwright.dev/docs/test-reporters)
    * [Retries](https://playwright.dev/docs/test-retries)
    * [Sharding](https://playwright.dev/docs/test-sharding)
    * [Timeouts](https://playwright.dev/docs/test-timeouts)
    * [TypeScript](https://playwright.dev/docs/test-typescript)
    * [UI Mode](https://playwright.dev/docs/test-ui-mode)
    * [Web server](https://playwright.dev/docs/test-webserver)
  * [Guides](https://playwright.dev/docs/library)
    * [Library](https://playwright.dev/docs/library)
    * [Accessibility testing](https://playwright.dev/docs/accessibility-testing)
    * [Actions](https://playwright.dev/docs/input)
    * [Assertions](https://playwright.dev/docs/test-assertions)
    * [API testing](https://playwright.dev/docs/api-testing)
    * [Authentication](https://playwright.dev/docs/auth)
    * [Auto-waiting](https://playwright.dev/docs/actionability)
    * [Best Practices](https://playwright.dev/docs/best-practices)
    * [Browsers](https://playwright.dev/docs/browsers)
    * [Chrome extensions](https://playwright.dev/docs/chrome-extensions)
    * [Clock](https://playwright.dev/docs/clock)
    * [Component testing](https://playwright.dev/docs/test-components)
    * [Debugging Tests](https://playwright.dev/docs/debug)
    * [Dialogs](https://playwright.dev/docs/dialogs)
    * [Downloads](https://playwright.dev/docs/downloads)
    * [Evaluating JavaScript](https://playwright.dev/docs/evaluating)
    * [Events](https://playwright.dev/docs/events)
    * [Extensibility](https://playwright.dev/docs/extensibility)
    * [Frames](https://playwright.dev/docs/frames)
    * [Handles](https://playwright.dev/docs/handles)
    * [Isolation](https://playwright.dev/docs/browser-contexts)
    * [Locators](https://playwright.dev/docs/locators)
    * [Mock APIs](https://playwright.dev/docs/mock)
    * [Mock browser APIs](https://playwright.dev/docs/mock-browser-apis)
    * [Navigations](https://playwright.dev/docs/navigations)
    * [Network](https://playwright.dev/docs/network)
    * [Other locators](https://playwright.dev/docs/other-locators)
    * [Pages](https://playwright.dev/docs/pages)
    * [Page object models](https://playwright.dev/docs/pom)
    * [Screenshots](https://playwright.dev/docs/screenshots)
    * [Service Workers](https://playwright.dev/docs/service-workers)
    * [Snapshot testing](https://playwright.dev/docs/aria-snapshots)
    * [Test generator](https://playwright.dev/docs/codegen)
    * [Touch events (legacy)](https://playwright.dev/docs/touch-events)
    * [Trace viewer](https://playwright.dev/docs/trace-viewer)
    * [Videos](https://playwright.dev/docs/videos)
    * [Visual comparisons](https://playwright.dev/docs/test-snapshots)
    * [WebView2](https://playwright.dev/docs/webview2)
  * [Migration](https://playwright.dev/docs/protractor)
  * [Integrations](https://playwright.dev/docs/docker)
  * [Supported languages](https://playwright.dev/docs/languages)


  * [](https://playwright.dev/)
  * Guides
  * Screenshots


On this page
# Screenshots
## Introduction[​](https://playwright.dev/docs/screenshots#introduction "Direct link to Introduction")
Here is a quick way to capture a screenshot and save it into a file:

```


await page.screenshot({ path: 'screenshot.png' });  



```

[Screenshots API](https://playwright.dev/docs/api/class-page#page-screenshot) accepts many parameters for image format, clip area, quality, etc. Make sure to check them out.
## Full page screenshots[​](https://playwright.dev/docs/screenshots#full-page-screenshots "Direct link to Full page screenshots")
Full page screenshot is a screenshot of a full scrollable page, as if you had a very tall screen and the page could fit it entirely.

```


await page.screenshot({ path: 'screenshot.png', fullPage: true });  



```

## Capture into buffer[​](https://playwright.dev/docs/screenshots#capture-into-buffer "Direct link to Capture into buffer")
Rather than writing into a file, you can get a buffer with the image and post-process it or pass it to a third party pixel diff facility.

```


const buffer = await page.screenshot();  





console.log(buffer.toString('base64'));  



```

## Element screenshot[​](https://playwright.dev/docs/screenshots#element-screenshot "Direct link to Element screenshot")
Sometimes it is useful to take a screenshot of a single element.

```


await page.locator('.header').screenshot({ path: 'screenshot.png' });  



```

[Previous Page object models](https://playwright.dev/docs/pom)[Next Service Workers](https://playwright.dev/docs/service-workers)
  * [Introduction](https://playwright.dev/docs/screenshots#introduction)
  * [Full page screenshots](https://playwright.dev/docs/screenshots#full-page-screenshots)
  * [Capture into buffer](https://playwright.dev/docs/screenshots#capture-into-buffer)
  * [Element screenshot](https://playwright.dev/docs/screenshots#element-screenshot)


Learn
  * [Getting started](https://playwright.dev/docs/intro)
  * [Playwright Training](https://learn.microsoft.com/en-us/training/modules/build-with-playwright/)
  * [Learn Videos](https://playwright.dev/community/learn-videos)
  * [Feature Videos](https://playwright.dev/community/feature-videos)


Community
  * [Stack Overflow](https://stackoverflow.com/questions/tagged/playwright)
  * [Discord](https://aka.ms/playwright/discord)
  * [X](https://x.com/playwrightweb)
  * [LinkedIn](https://www.linkedin.com/company/playwrightweb)


More
  * [GitHub](https://github.com/microsoft/playwright)
  * [YouTube](https://www.youtube.com/channel/UC46Zj8pDH5tDosqm1gd7WTg)
  * [Blog](https://dev.to/playwright)
  * [Ambassadors](https://playwright.dev/community/ambassadors)
  * [Microsoft Privacy Statement](https://go.microsoft.com/fwlink/?LinkId=521839)


Copyright © 2026 Microsoft

