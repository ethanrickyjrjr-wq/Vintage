// Reviewed placements for assets/rooms/example-room.webp (1536 × 1024).
// These bounds describe visible space in this one fixed photograph. Never use
// them for an uploaded room. Updating the photograph requires reviewing them.
export function sampleRoomScene() {
  return { slots: [
    // Empty left end of the credenza; keep the existing vase and lamp visible.
    { id: "console-left", kind: "lamp-or-decor", x: .795, bottom: .498, w: .115, h: .25 },
    // Objects stand on the coffee table, in front of the sofa in the photo.
    { id: "coffee-left", kind: "decor", x: .405, bottom: .705, w: .105, h: .15 },
    { id: "coffee-right", kind: "decor", x: .585, bottom: .705, w: .105, h: .15 },
    // Blank wall to either side of the existing framed painting.
    { id: "wall-left", kind: "art", x: .31, bottom: .435, w: .14, h: .25 },
    { id: "wall-right", kind: "art", x: .77, bottom: .36, w: .18, h: .23 },
    // Ceiling to the right of the existing pendant, and open foreground rug.
    { id: "ceiling-right", kind: "ceiling", x: .73, bottom: .035, w: .16, h: .20, anchorTop: true },
    { id: "floor-left", kind: "floor", x: .19, bottom: .92, w: .18, h: .20 },
  ] };
}
