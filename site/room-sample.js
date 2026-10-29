// Reviewed placements for assets/rooms/example-room.webp (1536 × 1024).
// These bounds describe visible space in this one fixed photograph. Never use
// them for an uploaded room. Updating the photograph requires reviewing them.
// ppm is the photo width one metre spans at that slot's depth, calibrated on
// objects already in the photo (throw pillows ≈ 145 px per 45 cm, the vase,
// and the credenza, sofa and coffee-table widths). Finds with a size in cm
// are drawn at real size, capped to the slot; without ppm they just fill it.
export function sampleRoomScene() {
  return { slots: [
    // Objects stand on the coffee table, in front of the sofa in the photo.
    { id: "coffee-left", kind: "decor", x: .405, bottom: .705, w: .105, h: .15, ppm: .25 },
    { id: "coffee-right", kind: "decor", x: .585, bottom: .705, w: .105, h: .15, ppm: .25 },
    // Farther back, so small finds try the coffee table first. Empty left end of the credenza; keep the existing vase and lamp visible.
    { id: "console-left", kind: "lamp-or-decor", x: .795, bottom: .498, w: .115, h: .25, ppm: .156 },
    // Bare back cushion between the sofa's existing throw pillows, resting on the seat.
    { id: "sofa-center-left", kind: "cushion", x: .44, bottom: .615, w: .085, h: .13, ppm: .225 },
    { id: "sofa-center-right", kind: "cushion", x: .525, bottom: .615, w: .085, h: .13, ppm: .225 },
    // Blank wall to either side of the existing framed painting.
    { id: "wall-left", kind: "art", x: .31, bottom: .435, w: .14, h: .25, ppm: .21 },
    { id: "wall-right", kind: "art", x: .77, bottom: .36, w: .18, h: .23, ppm: .21 },
    // Ceiling to the right of the existing pendant.
    { id: "ceiling-right", kind: "ceiling", x: .73, bottom: .035, w: .16, h: .20, anchorTop: true, ppm: .19 },
    // Nearest corner of the room: this close to the camera a chair is large, and it
    // may stand in front of the side-table base (it is nearer than the table).
    { id: "floor-left", kind: "floor", x: .14, bottom: .97, w: .26, h: .40, ppm: .30 },
  ] };
}
