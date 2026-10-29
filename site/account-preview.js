(() => {
  "use strict";

  // Visual preparation only. No authentication, email collection, uploads or room persistence.
  const header = document.querySelector(".header-actions");
  if (!header) return;
  // Entry points live in storefront.html so their placement is explicit in the published page.

  document.body.insertAdjacentHTML("beforeend", `
    <dialog class="account-dialog" id="account-dialog" aria-labelledby="account-title" aria-describedby="account-preview-note">
      <header class="account-heading">
        <div><p class="eyebrow">Your little corner of Holliewood</p><h2 id="account-title">Make yourself at home.</h2></div>
        <button class="account-close" type="button" aria-label="Close account preview" autofocus>×</button>
      </header>
      <p class="account-preview-note" id="account-preview-note"><strong>Coming soon.</strong> Accounts and saved rooms are on their way. Explore the preview below.</p>
      <div class="account-tabs" role="tablist" aria-label="Account preview">
        <button type="button" id="account-tab-welcome" role="tab" aria-selected="true" aria-controls="account-panel-welcome" data-account-tab="welcome">Account</button>
        <button type="button" id="account-tab-finds" role="tab" aria-selected="false" aria-controls="account-panel-finds" tabindex="-1" data-account-tab="finds">My Finds <span id="account-find-count">0</span></button>
        <button type="button" id="account-tab-rooms" role="tab" aria-selected="false" aria-controls="account-panel-rooms" tabindex="-1" data-account-tab="rooms">My Rooms</button>
      </div>
      <section class="account-panel" id="account-panel-welcome" role="tabpanel" aria-labelledby="account-tab-welcome" tabindex="0">
        <div class="account-welcome">
          <div class="account-story">
            <img src="assets/thumbnails/rooms-example-room--480.webp" alt="A sample living room with a cream sofa and walnut furniture" width="1536" height="1024" loading="lazy" />
            <h3>Good finds. Room to dream.</h3>
            <p>A little space for the pieces you love and the rooms you’re imagining.</p>
            <button class="account-text-link" type="button" data-account-view="rooms">Take a look at My Rooms <span aria-hidden="true">↗</span></button>
          </div>
          <div class="account-entry">
            <div class="account-entry-modes" role="group" aria-label="Preview sign-in or account creation">
              <button type="button" data-account-mode="create" aria-pressed="true">Create account</button>
              <button type="button" data-account-mode="signin" aria-pressed="false">Sign in</button>
            </div>
            <h3 id="account-entry-title">Make a little space.</h3>
            <p id="account-entry-copy">The future home for your favorite finds and unfinished rooms.</p>
            <label for="account-email-preview">Email address</label>
            <input id="account-email-preview" type="email" placeholder="you@example.com" disabled aria-describedby="account-entry-note" />
            <button class="account-primary" id="account-entry-submit" type="button" disabled>Create account · Coming soon</button>
            <p class="account-fine-print" id="account-entry-note">A preview of the sign-up screen. No email is collected and no account is created.</p>
          </div>
        </div>
      </section>
      <section class="account-panel" id="account-panel-finds" role="tabpanel" aria-labelledby="account-tab-finds" tabindex="0" hidden>
        <div class="account-section-heading"><div><h3>Your kind of character.</h3><p>Your favorites from this browser. Account syncing isn’t available yet.</p></div><button class="account-text-link" type="button" data-account-browse>Keep exploring <span aria-hidden="true">↗</span></button></div>
        <div class="account-empty" id="account-finds-empty"><span aria-hidden="true">♡</span><h4>A good collection starts with a crush.</h4><p>Tap a heart in the shop and that find will appear here. For now, favorites stay in this browser.</p><button class="account-primary" type="button" data-account-browse>Find something you love <span aria-hidden="true">↗</span></button></div>
        <ul class="account-finds" id="account-finds" aria-label="Favorites in this browser"></ul>
      </section>
      <section class="account-panel" id="account-panel-rooms" role="tabpanel" aria-labelledby="account-tab-rooms" tabindex="0" hidden>
        <div class="account-section-heading"><div><h3>A room of your own.</h3><p>Saved rooms are coming soon. Here’s a look at where your projects will live.</p></div><button class="account-text-link" type="button" data-account-room>Back to the room editor <span aria-hidden="true">↗</span></button></div>
        <div class="account-rooms">
          <article class="account-room-card"><img src="assets/thumbnails/rooms-example-room--480.webp" alt="Example project: a living room with a cream sofa, framed art and walnut tables" width="1536" height="1024" loading="lazy" /><div><p class="account-caption">Example project · AI-generated room</p><h4>The living room</h4><p>A little brass. A little character. A work in progress.</p><button class="account-text-link" type="button" disabled>Continue editing <span aria-hidden="true">↗</span></button><span class="account-fine-print">Example only. No saved project.</span></div></article>
          <div class="account-room-save"><p class="eyebrow">For your next good idea</p><h4 id="account-room-save-title">Leave room for later.</h4><p>Name a room and return to your arrangement when account saving is available.</p><label for="account-room-name">Room name</label><input id="account-room-name" type="text" placeholder="My living room" disabled /><button class="account-primary" type="button" disabled>Save to My Rooms</button><p class="account-fine-print" id="account-room-save-note">This is a preview. Your current room is not saved and clears when this page reloads or closes.</p></div>
        </div>
      </section>
      <footer class="account-footer"><span>A good eye. A space of your own.</span><button class="account-text-link" type="button" data-account-close>Back to the shop <span aria-hidden="true">↗</span></button></footer>
    </dialog>
  `);

  const dialog = document.querySelector("#account-dialog");
  const tabs = [...dialog.querySelectorAll("[data-account-tab]")];
  const items = new Map(HNV_ITEMS.filter(item => item.id !== "OWNER").map(item => [item.id, item]));
  let saved = [];
  let opener = null;
  try {
    const stored = JSON.parse(localStorage.getItem("hollywood-and-vine-saved") || "[]");
    if (Array.isArray(stored)) saved = stored;
  } catch { /* The catalog's same-tab event still supplies favorites if storage is blocked. */ }

  function renderFinds() {
    const favorites = [...new Set(saved)].filter(id => items.has(id));
    dialog.querySelector("#account-find-count").textContent = favorites.length;
    dialog.querySelector("#account-finds-empty").hidden = favorites.length > 0;
    const list = dialog.querySelector("#account-finds");
    list.replaceChildren();
    for (const id of favorites) {
      const item = items.get(id);
      const row = document.createElement("li");
      const link = document.createElement("a");
      link.href = `#item-${item.id}`;
      link.dataset.accountExit = "";
      const image = document.createElement("img");
      image.src = `assets/thumbnails/samples-${item.img.split("/").pop().replace(".webp", "")}--480.webp`;
      image.alt = "";
      image.width = 240;
      image.height = 300;
      image.loading = "lazy";
      const title = document.createElement("span");
      title.textContent = item.title;
      link.append(image, title);
      row.append(link);
      list.append(row);
    }
  }
  function showView(view) {
    const active = view === "save" ? "rooms" : view;
    dialog.dataset.view = view;
    for (const tab of tabs) {
      const selected = tab.dataset.accountTab === active;
      tab.setAttribute("aria-selected", String(selected));
      tab.tabIndex = selected ? 0 : -1;
      document.getElementById(tab.getAttribute("aria-controls")).hidden = !selected;
    }
    dialog.querySelector("#account-room-save-title").textContent = view === "save" ? "Save this little world." : "Leave room for later.";
    renderFinds();
  }
  function leaveFor(target) {
    opener = null;
    dialog.close();
    target.click();
    target.focus({ preventScroll: true });
  }
  document.addEventListener("click", event => {
    const trigger = event.target.closest("[data-account-open]");
    if (!trigger) return;
    opener = trigger;
    const mobileNav = document.querySelector("#mobile-nav");
    if (mobileNav) mobileNav.hidden = true;
    document.querySelector("#menu-toggle")?.setAttribute("aria-expanded", "false");
    showView(trigger.dataset.accountOpen);
    dialog.showModal();
    dialog.scrollTop = 0;
  });
  dialog.addEventListener("click", event => {
    const target = event.target.closest("button, a");
    if (!target) return;
    if (target.hasAttribute("data-account-exit")) opener = null;
    if (target.matches(".account-close, [data-account-close], [data-account-exit]")) dialog.close();
    if (target.dataset.accountTab) showView(target.dataset.accountTab);
    if (target.dataset.accountView) {
      showView(target.dataset.accountView);
      tabs.find(tab => tab.dataset.accountTab === target.dataset.accountView).focus();
    }
    if (target.hasAttribute("data-account-browse")) leaveFor(document.querySelector('[data-browse-category="all"]') || document.querySelector('.salon-actions a[href="#collection"]'));
    if (target.hasAttribute("data-account-room")) leaveFor(document.querySelector('.desktop-nav a[href="#your-room"]'));
    if (target.dataset.accountMode) {
      const create = target.dataset.accountMode === "create";
      dialog.querySelectorAll("[data-account-mode]").forEach(button => button.setAttribute("aria-pressed", String(button === target)));
      dialog.querySelector("#account-entry-title").textContent = create ? "Make a little space." : "Back for another look?";
      dialog.querySelector("#account-entry-copy").textContent = create ? "The future home for your favorite finds and unfinished rooms." : "Your finds and rooms, ready for your next good idea.";
      dialog.querySelector("#account-entry-submit").textContent = create ? "Create account · Coming soon" : "Sign in · Coming soon";
      dialog.querySelector("#account-entry-note").textContent = create ? "A preview of the sign-up screen. No email is collected and no account is created." : "A preview of the sign-in screen. No email is collected and no code is sent.";
    }
  });
  dialog.querySelector(".account-tabs").addEventListener("keydown", event => {
    const index = tabs.indexOf(document.activeElement);
    if (index < 0 || !["ArrowLeft", "ArrowRight", "Home", "End"].includes(event.key)) return;
    event.preventDefault();
    const next = event.key === "Home" ? 0 : event.key === "End" ? tabs.length - 1 : (index + (event.key === "ArrowRight" ? 1 : -1) + tabs.length) % tabs.length;
    showView(tabs[next].dataset.accountTab);
    tabs[next].focus();
  });
  dialog.addEventListener("close", () => {
    const inClosedMenu = opener?.closest("#mobile-nav[hidden]");
    (inClosedMenu ? document.querySelector("#menu-toggle") : opener)?.focus({ preventScroll: true });
  });
  document.addEventListener("hnv:saved-changed", event => {
    saved = Array.isArray(event.detail) ? event.detail : [];
    if (dialog.open) renderFinds();
  });
})();
