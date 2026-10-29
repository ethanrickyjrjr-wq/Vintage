import test from "node:test";
import assert from "node:assert/strict";
import { createHash } from "node:crypto";
import { readFileSync } from "node:fs";
import vm from "node:vm";
import { arrangeRoom, constrainLayer, layerBox, semanticGroup } from "../room-layout.js";
import { sampleRoomScene } from "../room-sample.js";

const width = 160, height = 100;
function mask(x, y, w, h) {
  const pixels = new Uint8Array(width * height);
  for (let py = Math.round(y * height); py < Math.round((y + h) * height); py++) {
    for (let px = Math.round(x * width); px < Math.round((x + w) * width); px++) pixels[py * width + px] = 255;
  }
  return pixels;
}
const segment = (label, box) => ({ label, score: .99, mask: mask(...box) });
const product = (id, kind) => ({ id, kind, overlay: "test.webp", ratio: 1.5 });
const grid = segments => ({ width, height, segments });

test("merged COCO labels identify surfaces and foreground stays protected", () => {
  assert.equal(semanticGroup("LABEL_199"), "wall");
  assert.equal(semanticGroup("LABEL_186"), "ceiling");
  assert.equal(semanticGroup("LABEL_190"), "floor");
  assert.equal(semanticGroup("LABEL_200"), "floor");
  assert.equal(semanticGroup("LABEL_188"), "cabinet");
  assert.equal(semanticGroup("LABEL_189"), "table");
  assert.equal(semanticGroup("floor-wood"), "floor");
  assert.equal(semanticGroup("wall-brick"), "wall");
  assert.equal(semanticGroup("couch"), "sofa");
  for (const label of ["window-other", "mirror-stuff", "tv", "door-stuff", "curtain", "light"]) assert.equal(semanticGroup(label), "obstacle");
});

test("missing surfaces never invent placements; missing cutouts are explained", () => {
  const products = [product("A1", "lamp"), product("A2", "ceiling"), product("A3", "art"), { id: "A22", kind: "floor" }];
  const result = arrangeRoom(products, grid([]), 1.6);
  assert.equal(result.layers.length, 0);
  assert.equal(result.unplaced.length, 4);
  assert.match(result.unplaced.find(item => item.id === "A22").reason, /cutout/);
});

test("coffee and unclassified tables cannot receive a lamp", () => {
  for (const segments of [
    [segment("LABEL_189", [.3, .7, .4, .15])],
    [segment("couch", [.25, .4, .5, .25]), segment("dining table", [.35, .7, .3, .15])],
  ]) {
    const result = arrangeRoom([product("A1", "lamp")], grid(segments), 1.6);
    assert.equal(result.layers.length, 0); assert.match(result.unplaced[0].reason, /side table or console/);
  }
});

test("one detected side table gets at most one lamp", () => {
  const scene = grid([segment("couch", [.3, .4, .4, .3]), segment("LABEL_189", [.12, .5, .14, .22])]);
  const result = arrangeRoom([product("A1", "lamp"), product("A13", "lamp")], scene, 1.6);
  assert.equal(result.layers.length, 1);
  assert.equal(result.unplaced.length, 1);
  assert.ok(result.layers[0].x < .3);
  assert.ok(layerBox(result.layers[0], 1.6).y < .5);
});

test("wall layouts are deterministic, bounded and limited even with many favorites", () => {
  const products = Array.from({ length: 12 }, (_, index) => product(`A${index + 1}`, "art"));
  const scene = grid([segment("LABEL_199", [.05, .05, .9, .85])]);
  const first = arrangeRoom(products, scene, 1.6), second = arrangeRoom([...products].reverse(), scene, 1.6);
  assert.deepEqual(first, second);
  assert.equal(first.layers.length, 2);
  assert.equal(first.unplaced.length, 10);
  const boxes = first.layers.map(layer => layerBox(layer, 1.6));
  assert.ok(boxes.every(box => box.x >= 0 && box.y >= 0 && box.x + box.w <= 1 && box.y + box.h <= 1));
  assert.ok(boxes[0].x + boxes[0].w <= boxes[1].x || boxes[1].x + boxes[1].w <= boxes[0].x ||
    boxes[0].y + boxes[0].h <= boxes[1].y || boxes[1].y + boxes[1].h <= boxes[0].y);
});

test("windows and other foreground regions rule out wall placements", () => {
  const scene = grid([segment("LABEL_199", [.05, .05, .9, .85]), segment("window-other", [0, 0, 1, 1])]);
  const result = arrangeRoom([product("A3", "art")], scene, 1.6);
  assert.equal(result.layers.length, 0);
});

test("moving and resizing stay inside portrait and landscape photos", () => {
  for (const aspect of [.4, 1, 2.5]) {
    const layer = constrainLayer({ x: -4, y: 4, w: 2, ratio: 3 }, aspect);
    const box = layerBox(layer, aspect);
    assert.ok(box.x >= 0 && box.y >= 0 && box.x + box.w <= 1.000001 && box.y + box.h <= 1.000001);
    assert.ok(layer.w >= .025);
  }
});

test("the shipped sample places the reported Egyptian lamp on the empty cabinet", () => {
  // Pin the reviewed photograph; a replacement image needs a fresh layout review.
  const photo = readFileSync(new URL("../assets/rooms/example-room.webp", import.meta.url));
  assert.equal(createHash("sha256").update(photo).digest("hex"), "2cba2ea9e22d50e31d340d10b90b28a048ede38ca564c28b61cd367cd5cc54e2");
  // Actual visible alpha bounds from the catalog photograph: 895 × 1200 px.
  const lamp = { id: "A13", kind: "lamp", overlay: "assets/demo/gold-bust-lamp.webp", ratio: 1200 / 895 };
  const result = arrangeRoom([lamp], sampleRoomScene(), 1.5);
  assert.equal(result.layers.length, 1);
  assert.deepEqual(result.unplaced, []);
  const box = layerBox(result.layers[0], 1.5);
  assert.ok(box.x >= .73 && box.x + box.w < .88, "base sits on the cabinet, away from the existing vase");
  assert.ok(Math.abs(box.y + box.h - .498) < .00001, "lamp base meets the cabinet top");
  assert.ok(box.w >= .1, "the lamp must be visibly useful, not reduced to a tiny marker");
});

test("all sample table lamps fit individually; a collection shares the available support", () => {
  // Ratios measured from the same trimmed alpha bounds used by the editor.
  const lamps = [["A1", 1600 / 1219], ["A13", 1200 / 895], ["A17", 1200 / 368], ["S117373F4", 1600 / 926]]
    .map(([id, ratio]) => ({ ...product(id, "lamp"), ratio }));
  for (const lamp of lamps) assert.equal(arrangeRoom([lamp], sampleRoomScene(), 1.5).layers.length, 1, lamp.id);
  const result = arrangeRoom(lamps, sampleRoomScene(), 1.5);
  assert.equal(result.layers.length, 1);
  assert.equal(result.unplaced.length, 3, "never stack lamps or put them on the coffee table");
  assert.deepEqual(result, arrangeRoom([...lamps].reverse(), sampleRoomScene(), 1.5));
  assert.equal(arrangeRoom([lamps[1]], grid([]), 1.5).layers.length, 0, "uploaded rooms must not inherit sample positions");
});

test("sample arrangements keep mixed finds bounded and separated", () => {
  const products = [product("A13", "lamp"), product("A3", "art"), product("A10", "decor"), product("A16", "media"), product("A2", "ceiling"), product("A15", "floor")];
  const result = arrangeRoom(products, sampleRoomScene(), 1.5);
  assert.equal(result.layers.length, products.length);
  const boxes = result.layers.map(layer => layerBox(layer, 1.5));
  for (const [index, box] of boxes.entries()) {
    assert.ok(box.x >= .01 && box.y >= .01 && box.x + box.w <= .99 && box.y + box.h <= .99);
    for (const other of boxes.slice(index + 1)) {
      assert.ok(box.x + box.w <= other.x || other.x + other.w <= box.x || box.y + box.h <= other.y || other.y + other.h <= box.y);
    }
  }
});

// What each kind of find may rest on in the shipped sample. Cushions once landed on the floor and a credenza.
const allowedSlots = { lamp: ["lamp-or-decor"], decor: ["decor", "lamp-or-decor"], media: ["decor", "lamp-or-decor"],
  art: ["art"], ceiling: ["ceiling"], floor: ["floor"], cushion: ["cushion"] };
const read = file => readFileSync(new URL(`../${file}`, import.meta.url), "utf8");
const { roomProducts } = vm.runInNewContext(`${read("catalog-data.js")}\n${read("room-products.js")}\n${read("demo-products.js")}\n({ roomProducts: HNV_ROOM_PRODUCTS })`);

const sofas = ["SCB4670A4", "S7E0E0EA5", "SAEEEA93E"];
test("every sample find lands on a surface that suits its kind", () => {
  const scene = sampleRoomScene();
  assert.equal(roomProducts.length, 40);
  for (const found of roomProducts) {
    assert.ok(allowedSlots[found.kind], `${found.id} has an unknown kind: ${found.kind}`);
    const result = arrangeRoom([{ id: found.id, kind: found.kind, overlay: found.overlay, ratio: 1, cm: found.cm }], scene, 1.5);
    if (sofas.includes(found.id)) { // Real size, in a room that already has its sofa: say so rather than shrink a sofa into a toy.
      assert.equal(result.layers.length, 0, found.id); assert.match(result.unplaced[0].reason, /too big/i); continue;
    }
    assert.equal(result.layers.length, 1, `${found.id} (${found.kind}) has nowhere to go`);
    const slot = scene.slots.find(candidate => candidate.x === result.layers[0].x);
    assert.ok(allowedSlots[found.kind].includes(slot.kind), `${found.id} (${found.kind}) landed on a ${slot.kind} slot`);
  }
});

test("sample cushions sit on the sofa between its throw pillows, never the floor or a table", () => {
  const cushions = roomProducts.filter(found => found.kind === "cushion");
  assert.deepEqual(Array.from(cushions, found => found.id).sort(), ["SB05192FF", "SB067D22F"]);
  const withOthers = [...cushions.map(found => ({ ...product(found.id, "cushion"), ratio: .95 })),
    product("A15", "floor"), product("A10", "decor"), product("A16", "media"), product("A13", "lamp")];
  const result = arrangeRoom(withOthers, sampleRoomScene(), 1.5);
  const placed = result.layers.filter(layer => layer.kind === "cushion");
  assert.equal(placed.length, 2);
  for (const layer of placed) {
    const box = layerBox(layer, 1.5);
    assert.ok(box.x >= .39 && box.x + box.w <= .58, "between the existing left and right throw pillows");
    assert.ok(Math.abs(box.y + box.h - .615) < .00001 && box.y > .45, "resting on the seat in front of the back cushion");
  }
  assert.equal(result.layers.filter(layer => layer.kind !== "cushion").length, withOthers.length - 2, "nothing else is displaced");
});

test("uploaded rooms put cushions on a detected sofa and leave them out without one", () => {
  const sofa = segment("couch", [.25, .4, .5, .25]);
  const cushion = { ...product("SB05192FF", "cushion"), ratio: .95 };
  const result = arrangeRoom([cushion], grid([sofa]), 1.6);
  assert.equal(result.layers.length, 1);
  const box = layerBox(result.layers[0], 1.6);
  assert.ok(box.x >= .25 && box.x + box.w <= .75 && box.y >= .4 && box.y + box.h <= .65, "inside the sofa's bounds");
  for (const segments of [[], [segment("LABEL_190", [0, .6, 1, .4])], [segment("LABEL_189", [.3, .5, .4, .2])]]) {
    const none = arrangeRoom([cushion], grid(segments), 1.6);
    assert.equal(none.layers.length, 0); assert.match(none.unplaced[0].reason, /sofa/);
  }
});

test("sample finds are drawn at believable sizes relative to one another", () => {
  // Ratios measured from the trimmed alpha bounds of each cutout; cm are the catalog's illustrative sizes.
  const size = (id, kind, ratio) => ({ ...product(id, kind), ratio, cm: roomProducts.find(found => found.id === id).cm });
  const placed = item => layerBox(arrangeRoom([item], sampleRoomScene(), 1.5).layers[0], 1.5);
  const lamp = placed(size("A13", "lamp", 1.34)), flute = placed(size("SA6FA3177", "decor", 2.69));
  const chair = placed(size("A15", "floor", 1.17)), cushion = placed(size("SB05192FF", "cushion", .92));
  assert.ok(lamp.h > .15 && lamp.h < .2, "the lamp is about as tall as the lamp already in the photo");
  assert.ok(flute.h < lamp.h / 1.8, "a champagne flute is far smaller than a table lamp");
  assert.ok(chair.h > .3 && chair.h < .4, "a chair nearest the camera is large");
  assert.ok(cushion.w <= .1, "a cushion is no wider than the existing throw pillows");
  assert.equal(arrangeRoom([size("A13", "lamp", 1.34)], grid([]), 1.5).layers.length, 0, "uploaded rooms have no scale and keep fit-to-slot");
});
