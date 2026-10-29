# Account, favorites and room-saving placement

Research and layout decision, 2026-10-29. Ricky asked for the controls to appear on the live site now, even while they lead to Coming soon screens. Account creation and online room saving remain inactive.

## Evidence

- [Nielsen Norman Group: Utility Navigation](https://www.nngroup.com/articles/utility-navigation/) recommends putting account and sign-in utilities in the upper right, placing content-specific tools beside the content they affect, and using visible text labels. Its warning about hiding useful tools behind menus matters on a small screen.
- [Nielsen Norman Group: Icon Usability](https://www.nngroup.com/articles/icon-usability/) recommends persistent text labels because icon meanings are often ambiguous and hover descriptions do not help on touch screens.
- [Baymard: Product Page UX](https://baymard.com/research-articles/current-state-ecommerce-product-page-ux) recommends allowing guest users to save favorites instead of requiring registration first. The existing local favorites should continue working.
- [Baymard: Account Drop-Down Structure](https://baymard.com/research-articles/account-drop-down-structure) recommends prioritizing the account features that matter for the particular site. For this shop's current scope, favorites and rooms are relevant; empty order, payment and address sections would add clutter.
- [IKEA: Where can I find my kitchen design?](https://www.ikea.com/us/en/customer-service/knowledge/articles/9697d151-0306-4b25-9420-442f8b61b3d7.html) shows a related product pattern: saved designs are available through the account and the planning tool. This is an example, not comparative usability evidence for our site.

## Applied layout

| Location | Controls | Reason |
| --- | --- | --- |
| Desktop header, right side | My Finds, My Rooms, Account, Bag | Familiar location for personal shopping tools; labels distinguish favorites from room projects. |
| Phone header, dedicated second row | The same four labeled controls | Keeps personal tools visible without crowding the brand or hiding them inside Menu. |
| Room workspace, above the photo | My Rooms and Save room | Saving belongs with the project being edited, where it can be found before scrolling through all the styling controls. |
| Room controls, beside Download | Save room and My Rooms | Keeps saving and exporting together at the end of the editing flow. |
| Account area | Account, My Finds, My Rooms | Shows the future structure without inventing unsupported commerce features. |

The exact arrangement is a design inference from this research and the existing storefront, not a measured conversion claim. Preserve the burgundy palette, original entrance objects, current favorites and editable room behavior. Use Coming soon on unavailable entry points and explain that no account or saved project has been created. Do not collect an email, upload a room or display a false success state.

Keep the entry buttons in the storefront HTML so their location is explicit and reviewable. JavaScript opens the existing account preview. The preview assets and HTML references must be included in the same published build, then checked on the live URL.

## Published and verified

Published as Sites version 31 on 2026-10-29 at [the public storefront](https://hollywood-and-vine-vintage.allstatecoop.chatgpt.site). The successful deployment uses source commit `3605d07288ceee9bcced041c5fe93b52a4eaeec4`; GitHub implementation commit is `c6763f1`.

All 33 existing tests and the production build pass. Desktop and phone layout checks include a 320-pixel viewport. On the live site, Account and My Rooms open their Coming soon previews, Save room opens the room-saving preview, and the phone header shows all four personal tools without horizontal overflow. Account fields stay disabled, and the room preview explains that the current room has not been saved. No browser console errors were recorded during these live checks.

The publication also preserves the concurrently landed room-category picker and the Hire Hollie occasion ordering. Live visual evidence is saved locally at `artifacts/account-layout/live-room-controls.png` and `artifacts/account-layout/live-mobile-account.png` (ignored artifacts).
