import test from "node:test";
import assert from "node:assert/strict";
import { arrangeRoom, constrainLayer, layerBox, semanticGroup } from "../room-layout.js";

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
