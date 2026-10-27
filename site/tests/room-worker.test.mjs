import test from "node:test";
import assert from "node:assert/strict";
import { DatabaseSync } from "node:sqlite";
import { readFileSync } from "node:fs";
import { createRoomWorker } from "../room-worker.mjs";

const webp = readFileSync(new URL("../assets/editorial/urn-lamp--400.webp", import.meta.url));
const photo = `data:image/webp;base64,${webp.toString("base64")}`;
const product = { id: "A1", title: "Brass urn lamp", sub: "Original brass lamp", surface: "table", img: "assets/photos/lamp.webp" };
const worker = createRoomWorker([product]);
function setup(t, providerStatus = 200, providerBody) {
  const db = new DatabaseSync(":memory:");
  db.exec(readFileSync(new URL("../drizzle/0000_room_preview_usage.sql", import.meta.url), "utf8"));
  const calls = [];
  const mockFetch = t.mock.method(globalThis, "fetch", async (url, init) => {
    if (init.method === "POST") {
      calls.push({ url, init, body: JSON.parse(init.body) });
      return Response.json(providerStatus === 200 ? { event_id: "a".repeat(32) } : providerBody, { status: providerStatus });
    }
    return new Response(`event: complete\ndata: ${JSON.stringify([providerBody ?? { image: photo }])}\n\n`);
  });
  const env = {
    ROOM_PREVIEW_ENABLED: "true", HF_TOKEN: "test-only-key", ROOM_RENDERER_URL: "https://room-renderer-test.hf.space",
    DB: { prepare(sql) { return { bind(...args) { return {
      async first() { return db.prepare(sql).get(...args) || null; },
      async run() { return db.prepare(sql).run(...args); },
    }; } }; } },
    ASSETS: { async fetch(request) { assert.equal(new URL(request.url).pathname, "/assets/photos/lamp.webp"); return new Response(webp); } },
  };
  const waits = [];
  const ctx = { waitUntil(promise) { waits.push(promise); } };
  t.after(async () => { await Promise.all(waits); mockFetch.mock.restore(); db.close(); });
  return { env, ctx, calls, db };
}
function request(overrides = {}, ip = "192.0.2.1", headers = {}) {
  return new Request("https://shop.test/api/room-preview", { method: "POST", headers: { origin: "https://shop.test", "content-type": "application/json", "cf-connecting-ip": ip, ...headers }, body: JSON.stringify({ image: photo, productId: "A1", mode: "place", point: { x: .4, y: .5 }, size: .25, ...overrides }) });
}
test("service discovery is honest when image editing is disabled", async () => {
  const result = await worker.fetch(new Request("https://shop.test/api/room-preview"), {});
  assert.deepEqual(await result.json(), { available: false, dailyLimit: 3 });
  assert.equal(result.headers.get("cache-control"), "no-store");
});
test("disabled AI rejects uploads without calling a provider", async (t) => {
  const { env, calls } = setup(t); env.ROOM_PREVIEW_ENABLED = "false";
  assert.equal((await worker.fetch(request(), env)).status, 503);
  assert.equal(calls.length, 0);
});
test("placement uses the original product asset, requested position and private renderer", async (t) => {
  const { env, calls, ctx } = setup(t);
  const result = await worker.fetch(request(), env, ctx);
  assert.equal(result.status, 200);
  assert.match((await result.json()).image, /^data:image\/webp;base64,/);
  assert.equal(calls[0].url, "https://room-renderer-test.hf.space/gradio_api/call/render_room");
  const payload = calls[0].body.data[0];
  assert.match(payload.prompt, /x=0.4, y=0.5/);
  assert.equal(payload.room.data, photo.split(",")[1]);
  assert.equal(payload.reference.data, webp.toString("base64"));
});
test("decorate asks the model to find a supported spot without removing furniture", async (t) => {
  const { env, calls, ctx } = setup(t);
  assert.equal((await worker.fetch(request({ mode: "decorate", point: null }), env, ctx)).status, 200);
  assert.match(calls[0].body.data[0].prompt, /Choose one visually and physically plausible spot/);
});
test("replacement accepts a selected region or a typed target and asks for background reconstruction", async (t) => {
  const { env, calls, ctx } = setup(t);
  const box = { x: .1, y: .2, width: .3, height: .4 };
  assert.equal((await worker.fetch(request({ mode: "replace", box }), env, ctx)).status, 200);
  assert.match(calls[0].body.data[0].prompt, /Reconstruct the background/);
  assert.match(calls[0].body.data[0].prompt, /left=0.1/);
  assert.equal((await worker.fetch(request({ mode: "replace", target: "lamp by the window" }), env, ctx)).status, 200);
  assert.match(calls[1].body.data[0].prompt, /lamp by the window/);
});
test("invalid images, products, coordinates, and replacement areas never consume quota", async (t) => {
  const { env, calls, db } = setup(t);
  for (const invalid of [
    { productId: "https://untrusted.test/image" }, { image: "data:image/png;base64," + "A".repeat(120) },
    { point: { x: -1, y: .5 } }, { size: 5 }, { mode: "arbitrary" },
    { mode: "replace", box: { x: .9, y: .2, width: .4, height: .3 } },
    { mode: "replace", box: null, target: "" }, { notes: "x".repeat(241) },
  ]) assert.equal((await worker.fetch(request(invalid), env)).status, 400);
  assert.equal(calls.length, 0);
  assert.equal(db.prepare("SELECT COUNT(*) AS count FROM room_preview_usage").get().count, 0);
});
test("cross-origin callers and wrong content types cannot access the paid endpoint", async (t) => {
  const { env, calls } = setup(t);
  assert.equal((await worker.fetch(request({}, undefined, { origin: "https://another.test" }), env)).status, 403);
  assert.equal((await worker.fetch(request({}, undefined, { "sec-fetch-site": "cross-site" }), env)).status, 403);
  assert.equal((await worker.fetch(request({}, undefined, { "content-type": "text/plain" }), env)).status, 415);
  assert.equal(calls.length, 0);
});
test("body limits also reject oversized bodies without Content-Length", async (t) => {
  const { env, calls } = setup(t);
  const result = await worker.fetch(request({ notes: "x".repeat(4 * 1024 * 1024) }), env);
  assert.equal(result.status, 413);
  assert.equal(calls.length, 0);
});
test("daily connection limits use atomic SQLite counters and salted hashes", async (t) => {
  const { env, calls, db, ctx } = setup(t);
  for (let i = 0; i < 3; i++) assert.equal((await worker.fetch(request(), env, ctx)).status, 200);
  const blocked = await worker.fetch(request(), env, ctx);
  assert.equal(blocked.status, 429);
  assert.ok(Number(blocked.headers.get("retry-after")) > 0);
  assert.equal(calls.length, 3);
  const row = db.prepare("SELECT * FROM room_preview_usage").get();
  assert.equal(row.uses, 3); assert.match(row.visitor, /^[a-f0-9]{64}$/);
  assert.ok(!JSON.stringify(row).includes("192.0.2.1"));
});
test("store-wide allowance caps total daily image requests", async (t) => {
  const { env, calls, ctx } = setup(t);
  for (let i = 0; i < 30; i++) assert.equal((await worker.fetch(request({}, `192.0.2.${i + 1}`), env, ctx)).status, 200);
  assert.equal((await worker.fetch(request({}, "192.0.2.99"), env, ctx)).status, 429);
  assert.equal(calls.length, 30);
});
test("provider failures refund reserved quota without exposing provider errors", async (t) => {
  const { env, db } = setup(t, 402, { error: { message: "private provider billing details" } });
  const response = await worker.fetch(request(), env);
  assert.equal(response.status, 503);
  assert.ok(!(await response.text()).includes("private provider"));
  assert.equal(db.prepare("SELECT uses FROM room_preview_usage").get().uses, 0);
});
test("a model response without an image is reported honestly and refunded", async (t) => {
  const { env, db } = setup(t, 200, { candidates: [{ content: { parts: [{ text: "I could not edit this photo." }] } }] });
  const response = await worker.fetch(request(), env);
  assert.equal(response.status, 503);
  assert.match((await response.json()).error, /couldn’t create/);
  assert.equal(db.prepare("SELECT uses FROM room_preview_usage").get().uses, 0);
});
