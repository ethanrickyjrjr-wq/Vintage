# Account and room-saving preview

Prepared on 2026-10-28 as an optional future feature, at Ricky's request. This change is a local visual preview; it does not activate accounts or publish the site.

On 2026-10-29 Ricky requested live publication with visible Coming soon controls. [The researched placement decision](account-layout.md) supersedes the original local-only delivery: My Finds, My Rooms, Account and Bag stay visible in the header, with a dedicated second row on phones. Save room also appears above the room photo. Account and room-saving entry points are now static storefront markup; the preview script supplies their dialog. Authentication and online saving remain inactive.

The header's Account button opens a burgundy dialog with Account, My Finds and My Rooms tabs. Create account and Sign in switch between visual form states. My Finds displays the catalog's existing browser favorites and follows its same-tab saved-change event, including when browser storage is unavailable. Empty favorites offer a route back to the collection. My Rooms shows an explicitly labeled example project, a room-name field and an inactive save action. Save room beside the editor's download button opens the room-saving preview. Mobile navigation also exposes My Finds and My Rooms.

The account fields and submission controls are disabled. No authentication provider, backend endpoint, email collection, verification code, room upload, additional persistence or cloud sync is implemented. No preview interaction changes an existing room. Existing favorites and PNG downloads continue to work. Room state still clears on reload or tab closure, as stated in the preview and editor.

`site/storefront.html` owns the entry buttons; `site/account-preview.js` owns the dialog and interactions; `site/account-preview.css` uses the storefront's existing type and theme tokens. Both assets are loaded by the storefront and included in the build. The dialog supports Escape, focus return, keyboard tab navigation and responsive layouts.

If accounts are approved later, choose and verify the identity and storage services before implementing authentication. Private room-photo storage, user-owned favorites and room records, account access controls, guest-favorite migration, editable layout restoration and honest saving/error states all remain future work. Replace the preview controls and copy only when that complete path is working.
