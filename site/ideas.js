// Idea room: Hollie marks each idea Keep, Maybe or Cut. Picks stay in this browser; the hub copies them as text for Ricky.
(() => {
  const key = "hnv-idea-picks";
  let picks = {};
  try { picks = JSON.parse(localStorage.getItem(key)) || {}; } catch {}
  const save = () => { try { localStorage.setItem(key, JSON.stringify(picks)); } catch {} };
  for (const box of document.querySelectorAll("[data-idea]")) {
    const id = box.dataset.idea;
    const saved = picks[id] || {};
    for (const radio of box.querySelectorAll('input[type="radio"]')) {
      radio.checked = radio.value === saved.call;
      radio.addEventListener("change", () => { picks[id] = { ...picks[id], call: radio.value }; save(); });
    }
    const note = box.querySelector("textarea");
    if (note) {
      note.value = saved.note || "";
      note.addEventListener("input", () => { picks[id] = { ...picks[id], note: note.value }; save(); });
    }
  }
  const copy = document.querySelector("#copy-picks");
  copy?.addEventListener("click", async () => {
    const lines = [...document.querySelectorAll("[data-idea]")].map((box) => {
      const pick = picks[box.dataset.idea] || {};
      return `${box.dataset.title}: ${pick.call || "not decided"}${pick.note ? ` (${pick.note})` : ""}`;
    });
    try {
      await navigator.clipboard.writeText(lines.join("\n"));
      copy.textContent = "Copied. Paste it to Ricky.";
    } catch {
      copy.textContent = "Copy didn’t work here. Take a screenshot instead.";
    }
  });
})();
