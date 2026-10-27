
```
/**
 * DiscoLights - the Afterparty ball's stylized fake-light rig.
 *
 * OPEN TO PRs. This file is mirrored 1:1 in a public repo with a standalone stage
 * (same camera distance, environment and sky as the schedule) so anyone can
 * improve the effect and PR it: https://github.com/BonoboJP/threejs-paris-disco-ball
 * Merged PRs are pulled back here with `pnpm syncDiscoBall`. Keep it self-contained
 * (imports from three/tsl + three/webgpu only) so both copies stay identical.
 *
 * No real lights: a mirror ball plus three additive layers that read as one
 * club-lighting illusion.
 *
 *   1. backdrop - a soft dark bowl the lights can actually sit against (the only
 *                 normal-blended layer, because additive cannot darken)
 *   2. shafts   - ONE instanced mesh of open-ended tapered tubes rooted INSIDE the
 *                 sphere and radiating outward in 3D
 *   3. dots     - ONE instanced mesh of small camera-facing motes filling a 3D shell
 *                 around the ball, plus the same rays cast onto the backdrop
 *
 * Three ideas carry the look:
 *
 * - GRADIENT LUT. Every layer computes a scalar intensity and reads its COLOR out
 *   of a baked ramp texture instead of tinting a mask with a flat color. That is
 *   what turns a blob into light: the falloff walks violet -> magenta -> cyan ->
 *   hot white on its way to the core, the way an actual emitter blows out. Ramps
 *   are interpolated in OKLab on the CPU so magenta -> cyan never passes through
 *   mud.
 *
 * - THE BALL IS THE SOURCE, not a sprite in front of a backdrop. Shafts root at
 *   0.94 - INSIDE the unit sphere - and draw AFTER it, so the sphere's own depth
 *   write carves each tube and the beam appears to break the mirror surface
 *   exactly at the silhouette, at every spin angle, with no authored contact seam.
 *   The dot field wraps the ball in depth for the same reason. The old rig drew
 *   its flat ray quad BEFORE the sphere, so the depth buffer was empty when it
 *   rasterized and the ball could never occlude its own light - that one ordering
 *   fact was most of the "pasted on" read.
 *
 * - ONE PROJECTION FRAME. Beams, dots and the mirror's own glints all gate on the
 *   same two fake lamps and rotate on one shared phase, so the rig pulses on a
 *   single beat. That phase turns at TWICE the ball's spin: a mirror rotating by
 *   theta sweeps its reflected ray by 2*theta, and the doubled sweep is what keeps
 *   the light from looking welded to the ball as one rigid sculpture.
 */
import { atan, cameraPosition, cameraViewMatrix, color, float, fwidth, hash, instancedBufferAttribute, materialOpacity, mix, modelNormalMatrix, modelWorldMatrixInverse, positionGeometry, positionWorld, reflect, smoothstep, texture, uint, uniform, uv, varying, vec2, vec3, vec4 } from 'three/tsl'
import { AdditiveBlending, CanvasTexture, ClampToEdgeWrapping, CylinderGeometry, DoubleSide, Group, InstancedBufferAttribute, InstancedMesh, LinearFilter, Mesh, MeshBasicNodeMaterial, MeshStandardNodeMaterial, PlaneGeometry, SRGBColorSpace, Vector2, Vector3 } from 'three/webgpu'

// ---------------------------------------------------------------------------
// Shared resources (one set for every Afterparty prop that ever recycles in)
// ---------------------------------------------------------------------------

let _resources = null
let _users = 0

// Local units - the ball is a UNIT sphere in this space, so every number below
// reads directly as "n ball radii". For scale: the camera sits ~4.6 local units
// out when the item is centered, and the near plane (1 world) is ~1.6 local.
const BACKDROP_SIZE = 14
const BACKDROP_Z = -0.9

// Dots. A third of them are "wall" dots - the same rays cast onto the backdrop
// bowl - which is what makes the field read as a mirror ball throwing light onto
// a surface rather than as free-floating glitter.
const DOT_COUNT = 480
// Each dot is EMITTED from just off the mirror and drifts out to its own reach on a
// short loop, fading in and out as it goes. Deliberately not physical - a mirror
// ball does not shed motes - but it is what turns a static shell into something
// that feels alive.
//
// The reach is sized to the FRAME, not the room: with the camera ~4.6 ball radii
// out at 55deg, the visible half-height at the ball's depth is ~2.4 radii and the
// half-width ~4. A dot's visible life (envelope dies past life 0.8, travel = life
// ^0.65) ends at ~90% of its reach, so REACH_MAX * SHELL keeps the whole field on
// screen and evenly spread across it, instead of spraying most of it out of frame
// and leaving the visible part clumped around the ball.
const DOT_EMIT_R = 1.06
const DOT_REACH_MIN = 2
const DOT_REACH_MAX = 4.4
// Ellipsoidal: every dot still travels a true ray from the ball centre, the squash
// fits the volume to a 16:9 frame. Z is flattened hardest so dots shooting at the
// lens do not spend their life in the near-cut.
const DOT_SHELL = [1.55, 0.95, 0.45]

// Shafts. The last BEAM_COLLARS instances are short, fat and dim - they sum into
// the ball's halo. This project's postFX chain has no bloom pass, so the collars
// and the contact term are the only glow the ball ever gets.
const BEAM_COUNT = 24
const BEAM_COLLARS = 2
// 0.06 INSIDE the mirror. BallProp's SphereGeometry( 1, 48, 24 ) dips to
// cos( PI / 24 ) = 0.9914 at the meridian midpoints, and the root ring's own
// radius puts its corners at 0.9416 - about 0.05 of margin under the skin
// everywhere, which also absorbs the per-beam wobble. Raising this toward 1 opens
// a hairline gap wherever the tessellation undershoots.
const BEAM_ROOT = 0.94
const BEAM_ROOT_R = 0.055
// Guard-sphere radius around the eye. A 6-unit beam aimed near the lens would
// otherwise punch through the near plane and show a straight cut across the frame.
const BEAM_GUARD = 1.9

// Mirror facets. Cols x rows of tiles across the sphere's UV; grout is the half
// width of the dark seam between tiles, in tile units. Dense + thin is what reads
// as a mirror ball from across the room; 32x16 with a fat seam read as a golf ball.
const FACET_COLS = 48
const FACET_ROWS = 24
const FACET_GROUT = 0.028

// Cable the ball hangs from (local units, ball radius = 1) and its mount cap.
const CABLE_LENGTH = 7
const CABLE_RADIUS = 0.018
const CAP_RADIUS = 0.11
const CAP_HEIGHT = 0.16

// Halo billboard behind the ball, in ball radii.
const HALO_SIZE = 3.4

const GOLDEN_ANGLE = 2.399963229728653
// Low-discrepancy irrationals. Radius and hue each need their OWN sequence: reuse
// the direction's and the radius marches in lockstep with latitude, which reads as
// a staircase instead of a shell.
const R2 = 0.7548776662466927
const H2 = 0.5698402909980532

// LUT rows. Each ramp ends on white so anything hot enough blows out to the same
// core, which is what lets differently-tinted beams overlap without turning into
// soup.
const LUT_RAMPS = [
	['#150430', '#5C15AE', '#FF3EA5', '#FFC6E6', '#FFFFFF'], // magenta
	['#03182C', '#0F5FB4', '#3AE8FF', '#C8F6FF', '#FFFFFF'], // cyan
	['#0B0630', '#3A1E9E', '#8A5BFF', '#D8CBFF', '#FFFFFF'], // violet
	['#2A1203', '#A8500C', '#FF9E3A', '#FFE2BC', '#FFFFFF'], // amber
]
const LUT_W = 256
// Texel-center v for each ramp row - sampling dead-center means the linear filter
// returns that row exactly, with no bleed from its neighbours.
const RAMP_V = LUT_RAMPS.map( ( _, i ) => ( i + 0.5 ) / LUT_RAMPS.length )

// --- OKLab ramp baking ------------------------------------------------------

const srgbToLinear = c => ( c <= 0.04045 ? c / 12.92 : Math.pow( ( c + 0.055 ) / 1.055, 2.4 ) )
const linearToSrgb = c => ( c <= 0.0031308 ? c * 12.92 : 1.055 * Math.pow( c, 1 / 2.4 ) - 0.055 )

function hexToLms( hex ) {
	const n = parseInt( hex.slice( 1 ), 16 )
	const r = srgbToLinear( ( ( n >> 16 ) & 255 ) / 255 )
	const g = srgbToLinear( ( ( n >> 8 ) & 255 ) / 255 )
	const b = srgbToLinear( ( n & 255 ) / 255 )
	return [
		Math.cbrt( 0.4122214708 * r + 0.5363325363 * g + 0.0514459929 * b ),
		Math.cbrt( 0.2119034982 * r + 0.6806995451 * g + 0.1073969566 * b ),
		Math.cbrt( 0.0883024619 * r + 0.2817188376 * g + 0.6299787005 * b ),
	]
}

function lmsToBytes( l, m, s, out, at ) {
	const l3 = l * l * l, m3 = m * m * m, s3 = s * s * s
	const rgb = [
		4.0767416621 * l3 - 3.3077115913 * m3 + 0.2309699292 * s3,
		-1.2684380046 * l3 + 2.6097574011 * m3 - 0.3413193965 * s3,
		-0.0041960863 * l3 - 0.7034186147 * m3 + 1.707614701 * s3,
	]
	for ( let i = 0; i < 3; i++ ) {
		out[at + i] = Math.round( Math.min( 1, Math.max( 0, linearToSrgb( Math.min( 1, Math.max( 0, rgb[i] ) ) ) ) ) * 255 )
	}
	out[at + 3] = 255
}

// One row per ramp, interpolated through OKLab so the hue path stays saturated.
function createRampLUT() {
	const canvas = document.createElement( 'canvas' )
	canvas.width = LUT_W
	canvas.height = LUT_RAMPS.length
	const ctx = canvas.getContext( '2d' )
	const image = ctx.createImageData( LUT_W, LUT_RAMPS.length )
	for ( let row = 0; row < LUT_RAMPS.length; row++ ) {
		const stops = LUT_RAMPS[row].map( hexToLms )
		const segments = stops.length - 1
		for ( let x = 0; x < LUT_W; x++ ) {
			const t = ( x / ( LUT_W - 1 ) ) * segments
			const i = Math.min( segments - 1, Math.floor( t ) )
			const f = t - i
			const a = stops[i]
			const b = stops[i + 1]
			lmsToBytes(
				a[0] + ( b[0] - a[0] ) * f,
				a[1] + ( b[1] - a[1] ) * f,
				a[2] + ( b[2] - a[2] ) * f,
				image.data,
				( row * LUT_W + x ) * 4
			)
		}
	}
	ctx.putImageData( image, 0, 0 )

	const texture = new CanvasTexture( canvas )
	texture.colorSpace = SRGBColorSpace
	texture.minFilter = LinearFilter
	texture.magFilter = LinearFilter
	texture.generateMipmaps = false
	texture.wrapS = ClampToEdgeWrapping
	texture.wrapT = ClampToEdgeWrapping
	return texture
}

// --- CPU bakes --------------------------------------------------------------

// Fibonacci sphere. Even coverage with no clumps, and crucially ANY PREFIX of it
// is still evenly covered - which is what lets `mesh.count` be a live density knob
// with nothing moving as it changes. Keying the latitude on a live count instead
// would teleport every dot on every drag.
function fibonacci( n, total, squash, out ) {
	const y = ( 1 - ( n + 0.5 ) * 2 / total ) * squash
	const ring = Math.sqrt( Math.max( 0, 1 - y * y ) )
	const phi = n * GOLDEN_ANGLE
	out.set( ring * Math.cos( phi ), y, ring * Math.sin( phi ) ).normalize()
	return out
}

const _v = new Vector3()
const _side = new Vector3()
const _ref = new Vector3()

function bakeDots( count ) {
	const dir = new Float32Array( count * 4 )
	const look = new Float32Array( count * 4 )
	const wallTotal = Math.floor( count / 3 )
	const airTotal = count - wallTotal
	let air = 0
	let wall = 0
	for ( let i = 0; i < count; i++ ) {
		// Every third instance is a WALL dot, INTERLEAVED on purpose: the density
		// knob only moves mesh.count, and a block layout would make it delete one
		// whole population instead of thinning both evenly.
		const isWall = i % 3 === 2
		const n = isWall ? wall++ : air++
		fibonacci( n, isWall ? wallTotal : airTotal, 1, _v )
		const at = i * 4
		dir[at] = _v.x
		dir[at + 1] = _v.y
		dir[at + 2] = _v.z
		// How far THIS dot gets before its loop restarts. Per-dot rather than shared,
		// so the field never reads as one expanding ring. Unused by wall dots, which
		// ray-cast onto the backdrop instead.
		dir[at + 3] = DOT_REACH_MIN + ( DOT_REACH_MAX - DOT_REACH_MIN ) * Math.pow( ( n * R2 ) % 1, 1.35 )
		const h = ( n * H2 ) % 1
		// Quad size in ball radii. The QUAD is the glow; the hot core inside it is a
		// small fraction of it (see the fragment), so the quad sets the halo, not the
		// point. Deliberately SMALL and biased small (h squared): a mirror ball's thrown
		// light is fine glitter, and a few larger motes carry the depth read while the
		// bulk stays subtle. Wall dots are bigger because they are pools on a surface.
		look[at] = isWall ? 0.1 + h * 0.08 : 0.05 + h * h * 0.09
		// Hue is GROUPED, never random: row 1 (cyan) rides lamp A, row 0 (magenta)
		// rides lamp B, so the field's bright zones and its hue swing together and
		// the two hand over, instead of both being everywhere at once. The shader
		// recovers the family with fract( v * 2 ): 0.125 -> 0.25, 0.375 -> 0.75.
		look[at + 1] = ( i % 2 ) ? RAMP_V[1] : RAMP_V[0]
		// Emission-loop OFFSET, 0..1 (not a radian phase any more). Its own golden
		// sequence, decorrelated from both the direction and the reach, so births are
		// spread evenly through the loop and the field never pulses in unison.
		look[at + 2] = ( n * 0.6180339887498949 ) % 1
		look[at + 3] = isWall ? 1 : 0
	}
	return {
		dir: new InstancedBufferAttribute( dir, 4 ),
		look: new InstancedBufferAttribute( look, 4 ),
	}
}

function bakeBeams( count ) {
	const axis = new Float32Array( count * 4 )
	const side = new Float32Array( count * 4 )
	const look = new Float32Array( count * 4 )
	for ( let i = 0; i < count; i++ ) {
		const collar = i >= count - BEAM_COLLARS
		// Squashed off the poles: a disco ball's readable beams are the equatorial
		// band, straight-up ones just read as a fountain.
		fibonacci( i, count, 0.78, _v )
		// `side` is baked here rather than derived in the shader precisely to avoid
		// the degenerate branch when the axis is parallel to world up, where a
		// shader normalize() emits NaN and silently garbles one instance.
		_ref.set( 0, 1, 0 )
		if ( Math.abs( _v.y ) > 0.9 ) _ref.set( 1, 0, 0 )
		_side.crossVectors( _ref, _v ).normalize()

		const u = ( i * R2 ) % 1
		const h = ( i * H2 ) % 1
		const at = i * 4
		axis[at] = _v.x
		axis[at + 1] = _v.y
		axis[at + 2] = _v.z
		axis[at + 3] = collar ? 1.9 : 2.9 + 3.2 * u
		side[at] = _side.x
		side[at + 1] = _side.y
		side[at + 2] = _side.z
		// A collar is the same mesh, just short and fat. tipRadius > 0.7 is also how
		// the shader identifies one, so no extra attribute is needed.
		side[at + 3] = collar ? 1.05 : 0.2 + 0.26 * h
		look[at] = RAMP_V[i % 4]
		// Past ~0.45 the collars stop being a halo and start washing out every real
		// beam.
		look[at + 1] = collar ? 0.3 : 0.55 + 0.45 * h
		look[at + 2] = 0.6 + 1.4 * u
		look[at + 3] = ( i * 1.7 ) % 6.28318
	}
	return {
		axis: new InstancedBufferAttribute( axis, 4 ),
		side: new InstancedBufferAttribute( side, 4 ),
		look: new InstancedBufferAttribute( look, 4 ),
	}
}

function acquireResources() {
	if ( !_resources ) {
		const dot = bakeDots( DOT_COUNT )
		// InstancedMesh over a plain geometry carrying InstancedBufferAttributes -
		// the same recipe SpiralCards ships, which is the one path here already
		// proven on BOTH backends. instanceMatrix is deliberately left untouched:
		// positionNode runs AFTER instancing and replaces it wholesale.
		const dotGeometry = new PlaneGeometry( 1, 1 )
		dotGeometry.setAttribute( 'iDotDir', dot.dir )
		dotGeometry.setAttribute( 'iDotLook', dot.look )

		const beam = bakeBeams( BEAM_COUNT )
		// Open-ended so there is no cap to catch the eye where the ball's depth clip
		// ends. The 6 height segments exist so the taper can be applied per-vertex
		// and give a trumpet flare rather than the straight cone a baked
		// radiusTop/radiusBottom would produce.
		const beamGeometry = new CylinderGeometry( 1, 1, 1, 16, 6, true )
		// positionGeometry.y now runs 0 at the root to 1 at the tip.
		beamGeometry.translate( 0, 0.5, 0 )
		beamGeometry.setAttribute( 'iBeamAxis', beam.axis )
		beamGeometry.setAttribute( 'iBeamSide', beam.side )
		beamGeometry.setAttribute( 'iBeamLook', beam.look )

		// Cable: a thin open tube from the top of the ball straight up, uv.y running 0
		// at the ball to 1 at the far end so the material can fade it out. The cap is
		// a short closed cylinder sitting on the pole.
		const cableGeometry = new CylinderGeometry( CABLE_RADIUS, CABLE_RADIUS, CABLE_LENGTH, 8, 1, true )
		cableGeometry.translate( 0, 1 + CAP_HEIGHT * 0.5 + CABLE_LENGTH / 2, 0 )
		const capGeometry = new CylinderGeometry( CAP_RADIUS * 0.7, CAP_RADIUS, CAP_HEIGHT, 16, 1, false )
		capGeometry.translate( 0, 1 - CAP_HEIGHT * 0.15, 0 )

		_resources = {
			lut: createRampLUT(),
			quad: new PlaneGeometry( 1, 1 ),
			cableGeometry,
			capGeometry,
			dotGeometry,
			dotDir: dot.dir,
			dotLook: dot.look,
			beamGeometry,
			beamAxis: beam.axis,
			beamSide: beam.side,
			beamLook: beam.look,
		}
	}
	_users++
	return _resources
}

function releaseResources() {
	_users = Math.max( 0, _users - 1 )
	if ( _users || !_resources ) return
	_resources.lut.dispose()
	_resources.quad.dispose()
	_resources.cableGeometry.dispose()
	_resources.capGeometry.dispose()
	_resources.dotGeometry.dispose()
	_resources.beamGeometry.dispose()
	_resources = null
}

function additiveMaterial( name ) {
	const material = new MeshBasicNodeMaterial( {
		transparent: true,
		opacity: 0,
		depthWrite: false,
		depthTest: true,
		side: DoubleSide,
		forceSinglePass: true,
		blending: AdditiveBlending,
		toneMapped: false,
	} )
	material.name = name
	// NOTE on TRAA: the scene pass writes an MRT velocity buffer, and three derives
	// that velocity from `positionPrevious`, which stays the RAW geometry position
	// (only Skinning and Instance ever reassign it, never positionNode). Both layers
	// below displace heavily in positionNode, so their motion vectors are wrong.
	// Overriding them with a material-level `mrt( { velocity } )` does NOT work:
	// MRTNode.setup resolves each output name against the CURRENT render target's
	// textures and skips the misses, so in any pass whose target has no velocity
	// attachment the struct comes out EMPTY and WGSL rejects it outright
	// ("structures must have at least one member"). SpiralCards displaces in
	// positionNode and ships without an override for the same reason.
	return material
}

// Read a color out of one LUT row (row given as a v coordinate, so an instance can
// pick its own).
//
// The lookup is BIASED (pow < 1) while the caller still multiplies by the raw
// intensity. That split is the whole point: brightness stays linear so falloff
// reads correctly, but hue is pushed up the ramp so the large faint areas - which
// is most of any light layer - land on the ramp's vivid middle instead of pooling
// in its near-black start. Sample the ramp linearly and every layer, whatever its
// row, comes out the same washed lavender.
function rampAtV( lut, intensity, v ) {
	return texture( lut, vec2( intensity.clamp( 0, 1 ).pow( 0.5 ), v ) ).rgb
}

// Crawling grain, the cheap acura trick that stops a wide smooth ramp from
// banding into stair-steps on an 8-bit target.
function grainNode( coord, time, amount ) {
	const key = uint( coord.x.mul( 1024 ).abs() )
		.mul( uint( 1973 ) )
		.add( uint( coord.y.mul( 1024 ).abs() ) )
		.add( uint( time.mul( 24 ).abs() ) )
	return hash( key ).sub( 0.5 ).mul( amount )
}

// CPU smoothstep on 0..1.
function smooth01( x ) {
	const t = Math.max( 0, Math.min( 1, x ) )
	return t * t * ( 3 - 2 * t )
}

// Rotate about local Y with a precomputed ( cos, sin ) pair, so the shader carries
// no trig for the projection frame.
function spinY( v, cs ) {
	return vec3(
		v.x.mul( cs.x ).add( v.z.mul( cs.y ) ),
		v.y,
		v.z.mul( cs.x ).sub( v.x.mul( cs.y ) )
	)
}

// ---------------------------------------------------------------------------

export default class DiscoLights {
	/** @param {import('three').BufferGeometry} sphereGeometry shared unit sphere */
	constructor( sphereGeometry ) {
		const res = acquireResources()
		this._res = res

		this.root = new Group()
		this.root.name = 'Schedule Afterparty light rig'
		this.root.visible = false

		// ONE clock + ONE focus for the whole rig, so every layer stays in phase.
		this.time = uniform( 0 )
		this.focus = uniform( 0 )
		// The projection frame: ( cos, sin ) of the shaft/dot rotation, which runs at
		// a multiple of the ball's own spin.
		this.projCS = uniform( new Vector2( 1, 0 ) )
		// The two fake emitters. Hoisted out of the sphere shader onto the CPU so the
		// mirror's glints, the beams and the dot field all gate on the SAME lamps and
		// therefore flash on one beat.
		this.lampA = uniform( new Vector3( 0, 1, 0 ) )
		this.lampB = uniform( new Vector3( 0, 1, 0 ) )
		// Live gain knobs (pushed from the tweaks panel every frame).
		this.rayGain = uniform( 1 )
		this.speckleGain = uniform( 1 )
		this.beamReach = uniform( 1 )
		this.beamWidth = uniform( 1 )
		this.wallGain = uniform( 1 )
		// Mirror facets: how far each tile is tilted off tangent (radians-ish, it is
		// added to a unit normal), and the gain on the tile glints / white pops.
		this.facetJitter = uniform( 0.12 )
		this.glintGain = uniform( 1 )
		this.haloGain = uniform( 1 )

		this._layers = []
		this._buildBackdrop()
		this._buildSphere( sphereGeometry )
		this._buildHalo()
		this._buildCable()
		this._buildShafts()
		this._buildDots()
	}

	// A dark bowl behind everything. Additive layers cannot darken, so the contrast
	// the fake lights need has to be painted in first, in normal blending.
	_buildBackdrop() {
		const material = new MeshBasicNodeMaterial( {
			transparent: true,
			opacity: 0,
			depthWrite: false,
			depthTest: true,
			side: DoubleSide,
			forceSinglePass: true,
			toneMapped: false,
		} )
		material.name = 'Schedule Afterparty backdrop'
		const p = uv().sub( 0.5 )
		const r = p.length().mul( 2 )
		// Squared falloff plus a slow breathing edge - a plain radial reads as a
		// pasted circle, this one has no findable rim.
		const wobble = float( 1 ).add( atan( p.y, p.x ).mul( 3 ).add( this.time.mul( 0.23 ) ).sin().mul( 0.06 ) )
		const mask = smoothstep( float( 0.98 ).mul( wobble ), float( 0.06 ), r )
		material.colorNode = mix( color( '#160A33' ), color( '#2A0F4E' ), r.clamp( 0, 1 ) )
		material.opacityNode = mask.mul( mask ).mul( materialOpacity )

		const mesh = new Mesh( this._res.quad, material )
		mesh.position.z = BACKDROP_Z
		mesh.scale.setScalar( BACKDROP_SIZE )
		mesh.frustumCulled = false
		this.root.add( mesh )
		this._backdrop = mesh
		this._layers.push( { mesh, material, base: 0.9, order: -6 } )
	}

	// Long 3D tubes radiating out of the mirror. Open-ended, additive, DoubleSide,
	// so each eye ray samples both walls and the pair sums to the line integral
	// through a uniform-density cylinder.
	_buildShafts() {
		const material = additiveMaterial( 'Schedule Afterparty light shafts' )
		const res = this._res
		const t = this.time
		const axisAttr = instancedBufferAttribute( res.beamAxis ) // [ ax, ay, az, length ]
		const sideAttr = instancedBufferAttribute( res.beamSide ) // [ sx, sy, sz, tipRadius ]
		const look = instancedBufferAttribute( res.beamLook ) // [ rampV, gain, rate, phase ]

		// The eye in THIS mesh's local space. modelWorldMatrixInverse is a per-object
		// uniform three refreshes at DRAW time, so it is immune to BallProp.place()
		// running before ScheduleSpiralView's camera block, and it stays correct if a
		// parent ever rotates - neither of which a CPU-computed camera position would.
		const camLocal = modelWorldMatrixInverse.mul( vec4( cameraPosition, 1 ) ).xyz

		const axis0 = spinY( axisAttr.xyz, this.projCS )
		const side0 = spinY( sideAttr.xyz, this.projCS )
		const bino0 = axis0.cross( side0 )

		// Per-beam precession of a few degrees: air shimmer, not unglued beams.
		const wob = t.mul( look.z.mul( 0.5 ).add( 0.25 ) ).add( look.w )
		const axisRaw = axis0
			.add( side0.mul( wob.sin().mul( 0.06 ) ) )
			.add( bino0.mul( wob.mul( 0.83 ).cos().mul( 0.05 ) ) )
		const axis = axisRaw.div( axisRaw.length().max( 1e-4 ) )

		const root = axis.mul( BEAM_ROOT )
		const toCam = camLocal.sub( root )

		// GUARD SPHERE. Clip the shaft against a sphere around the eye rather than
		// trusting authored lengths, so a beam swinging at the lens fades instead of
		// showing a straight near-plane cut across the frame. Correct at any prop
		// scale, including the centerScale debug slider.
		const axial = toCam.dot( axis )
		const offAxis = toCam.sub( axis.mul( axial ) ).length()
		const hit = float( BEAM_GUARD * BEAM_GUARD ).sub( offAxis.mul( offAxis ) )
		const enter = axial.sub( hit.max( 0 ).sqrt() )
		// BOTH tests are required. `hit > 0` alone also truncates every beam pointing
		// AWAY from the eye: both roots of the quadratic are negative there (the guard
		// sits entirely behind the root), so clamping to them would stub out a whole
		// band of receding beams that were never at risk.
		const blocks = smoothstep( 0, 0.05, hit ).mul( smoothstep( 0, 0.1, enter ) )
		const limit = mix( float( 99 ), enter, blocks )
		// Beams GROW out of the ball as the item nears the centre of the coil. One
		// already at full length but 5% opacity reads as a decal; one that extends
		// reads as an emitter switching on.
		const wanted = axisAttr.w.mul( this.focus.mul( 0.62 ).add( 0.38 ) ).mul( this.beamReach )
		const reach = wanted.min( limit.max( 0.35 ) )
		// A heavily truncated beam fades rather than just stopping.
		const clipFade = smoothstep( 0.35, 0.85, reach.div( wanted.max( 1e-3 ) ) )

		const along = positionGeometry.y // 0 at the root, 1 at the tip
		// positionGeometry.xz is an exact unit circle on CylinderGeometry( 1, 1, ... ).
		const ring = side0.mul( positionGeometry.x ).add( bino0.mul( positionGeometry.z ) )
		// Trumpet, not a cone: pow < 1 opens the beam fast just off the ball and then
		// eases, which is how a real shaft's scattering envelope reads.
		const radius = mix( float( BEAM_ROOT_R ), sideAttr.w.mul( this.beamWidth ), along.pow( 0.72 ) )
		const localPos = axis.mul( along.mul( reach ).add( BEAM_ROOT ) ).add( ring.mul( radius ) )
		// positionNode, never vertexNode: positionWorld / positionView / depth all stay
		// truthful, which is exactly what buys the depth interaction with the mirror.
		material.positionNode = localPos

		const posV = varying( localPos )
		const radV = varying( radius )
		const alongV = varying( along )
		const rootV = varying( root )
		const axisV = varying( axis )
		const camV = varying( camLocal )
		const lookV = varying( look )
		const clipV = varying( clipFade )

		// --- fragment. Everything here stays in LOCAL space: mixing a local axis with
		// a world view direction is a latent bug the moment a parent rotates.
		const toEye = camV.sub( posV )
		const viewDir = toEye.div( toEye.length().max( 1e-4 ) )

		// THE volume term, and the whole reason a hollow tube reads as a solid beam.
		// What matters is how much of the cylinder's INTERIOR this eye ray crosses,
		// which is set by the lateral offset between the ray and the beam AXIS - not
		// by the fragment's own distance from the axis, which on a tube wall is always
		// exactly the radius and would make every fragment identical.
		//
		// cross( axis, viewDir ) is the common perpendicular of those two lines and
		// its length is sin( angle between them ), so one cross product yields both
		// the offset direction and the 1/sin path-length stretch.
		const perpRaw = axisV.cross( viewDir )
		// The floor is what makes a beam aimed at the lens BLOOM into a disc instead
		// of going black: as sin -> 0 the normalized offset collapses toward zero, the
		// chord saturates, and the divide below drives it to the cap.
		const sinT = perpRaw.length().max( 0.22 )
		const perpDir = perpRaw.div( sinT )
		const lateral = rootV.sub( camV ).dot( perpDir ).abs()
		const xN = lateral.div( radV.max( 1e-4 ) )
		// Exactly zero at the silhouette for ANY segment count. Reading an interpolated
		// ring normal instead only reaches sin( 180 / N ) there, so a 16-gon would
		// terminate every beam on a hard polygonal edge at ~22% brightness.
		const chord = float( 1 ).sub( xN.mul( xN ) ).max( 0 ).sqrt()
		const body = chord.div( sinT ).min( 2.6 ).pow( 0.85 )

		// No cap on the tube, plus a short rise so the few beams rooted on the NEAR
		// silhouette - which the ball never clips - still show no hard rim.
		const emerge = smoothstep( 0, 0.09, alongV )
		// Light LEAVING a source, never a wedge.
		const decay = alongV.oneMinus().pow( 1.55 )
		// The hot spot right where the beam breaks the mirror. This is the single term
		// that welds shaft to ball.
		const contact = smoothstep( 0.32, 0.02, alongV ).mul( 0.9 )
		const dust = alongV.mul( 7.5 ).sub( t.mul( 1.35 ) ).add( lookV.w )
			.sin().mul( 0.5 ).add( 0.5 ).mul( 0.3 ).add( 0.7 )
		const flicker = t.mul( 1.9 ).add( lookV.w.mul( 2.3 ) ).sin().mul( 0.5 ).add( 0.5 ).mul( 0.45 ).add( 0.55 )

		// Lamp gate, grouped by ramp family. A real ball only throws beams from the
		// facets currently facing a lamp, so the live set is a sweeping LOBE rather
		// than a hedgehog - roughly half read as bright at a time. Collars are the
		// halo and are exempt.
		const familyA = smoothstep( 0.45, 0.55, lookV.x.mul( 2 ).fract() )
		const collar = smoothstep( 0.7, 0.9, varying( sideAttr.w ) )
		const lampA = axisV.dot( this.lampA ).max( 0 ).pow( 1.6 )
		const lampB = axisV.dot( this.lampB ).max( 0 ).pow( 2 )
		const lamp = mix( mix( lampB, lampA, familyA ).mul( 0.86 ).add( 0.14 ), float( 0.85 ), collar )

		// Carve the ring-text band. BallProp hangs the white "AFTERPARTY" cylinder at
		// radius 1.18 with depthWrite:false, which is exactly where `contact` peaks -
		// without this the type stops reading the moment the beams come up.
		const bandR = posV.length().sub( 1.18 ).abs()
		const ringMask = smoothstep( 0.3, 0.12, bandR ).mul( smoothstep( 0.55, 0.3, posV.y.abs() ) )
			.mul( 0.6 ).oneMinus()

		// The backdrop is depthWrite:false and cannot absorb anything behind it, so
		// distance has to be expressed in brightness as well as in the z-buffer.
		const ref = camV.length()
		const murk = smoothstep( ref.add( 4.6 ), ref.sub( 1.2 ), toEye.length() ).mul( 0.72 ).add( 0.28 )
		const energy = this.focus.mul( 0.72 ).add( 0.28 ).mul( this.rayGain )
		const intensity = body.mul( decay.add( contact ) ).mul( emerge ).mul( dust ).mul( flicker )
			.mul( lamp ).mul( lookV.y ).mul( clipV ).mul( ringMask ).mul( murk ).mul( energy )

		material.colorNode = rampAtV( res.lut, intensity, lookV.x ).mul( intensity )
			.add( grainNode( uv(), t, 0.015 ) )

		const mesh = new InstancedMesh( res.beamGeometry, material, BEAM_COUNT )
		mesh.frustumCulled = false
		this.root.add( mesh )
		this._shafts = mesh
		// +3, i.e. AFTER the sphere (+0) and the ring text (+1, owned by BallProp).
		// The old flat ray quad sat at -4 and drew BEFORE the sphere, so the depth
		// buffer was still empty when it rasterized and the ball could never occlude
		// its own light.
		this._layers.push( { mesh, material, base: 0.85, order: 3 } )
	}

	// The mirror's projected light as a real 3D field: motes EMITTED from just off
	// the ball, drifting outward on their own short loop and fading in and out as
	// they go, plus a third of them cast onto the backdrop bowl where they stretch
	// into ellipses at grazing incidence.
	_buildDots() {
		const material = additiveMaterial( 'Schedule Afterparty mirror dots' )
		const res = this._res
		const t = this.time
		const dirA = instancedBufferAttribute( res.dotDir ) // [ dx, dy, dz, reach ]
		const look = instancedBufferAttribute( res.dotLook ) // [ size, rampV, offset, kind ]
		const kind = look.w

		const camLocal = modelWorldMatrixInverse.mul( vec4( cameraPosition, 1 ) ).xyz
		const upLocal = modelWorldMatrixInverse.mul( vec4( 0, 1, 0, 0 ) ).xyz
		const spun = spinY( dirA.xyz, this.projCS )

		// --- the emission loop. `life` runs 0..1 and wraps: born just off the mirror,
		// drifting out to this dot's own reach, gone. Rate is decorrelated from the
		// offset by a second irrational rather than a third baked float - the two need
		// to look independent, not BE independent.
		const rate = mix( 0.055, 0.15, look.z.mul( 7.13 ).fract() )
		const life = t.mul( rate ).add( look.z ).fract()
		// Ease-out: quick off the mirror then drifting. Light leaving a source, rather
		// than a particle being thrown.
		const travel = life.pow( 0.65 )
		// Fade in fast, linger, fade out long. This IS the twinkle - there is no
		// separate per-dot flicker on top, which is what keeps the field feeling like
		// one breathing volume instead of a box of fairy lights.
		const envelope = smoothstep( 0, 0.09, life ).mul( smoothstep( 1, 0.45, life ) )

		// --- airborne: a mote of light drifting out through the haze.
		const rho = mix( float( DOT_EMIT_R ), dirA.w, travel )
		const airCenter = spun.mul( rho ).mul( vec3( DOT_SHELL[0], DOT_SHELL[1], DOT_SHELL[2] ) )
		// Near-constant WORLD size is what carries the depth read - perspective shrinks
		// the far ones on its own. The reach term claws back only a little so the tail
		// of the loop does not dissolve entirely.
		// Motes swinging close to the eye would otherwise balloon into big soft blobs
		// (constant world size, shrinking distance): shrink them as they approach so
		// the field stays fine-grained from every angle.
		const airEyeDist = airCenter.sub( camLocal ).length()
		const airSize = look.x.mul( rho.mul( 0.035 ).add( 1 ) )
			.mul( smoothstep( 1.8, 5, airEyeDist ).mul( 0.6 ).add( 0.4 ) )

		// --- wall: the SAME ray, cast onto the backdrop bowl. This is what makes the
		// rig read as a mirror ball rather than as glitter - the light lands on a
		// SURFACE and slides across it with the right parallax.
		const dz = spun.z.min( -0.06 ) // guarded: the bowl is behind, so dz stays < 0
		const throwDist = float( BACKDROP_Z ).div( dz ).min( 6 )
		const wallCenter = spun.mul( throwDist )
		const wallXY = wallCenter.xy.div( wallCenter.xy.length().max( 1e-4 ) )
		const wallRadial = vec3( wallXY.x, wallXY.y, 0 )
		const wallTangent = vec3( wallXY.y.negate(), wallXY.x, 0 )
		// Physically a footprint on a plane stretches by 1/cos(incidence) toward the
		// grazing angle; deliberately NOT done here - the ellipses read as streaks and
		// scratches, round pools read as light. A far throw still lands a slightly
		// bigger, softer patch.
		const wallSize = look.x.mul( throwDist.mul( 0.18 ).add( 0.7 ) )

		const center = mix( airCenter, wallCenter, kind )
		const toDot = center.sub( camLocal )
		const camDist = toDot.length()
		// NEAR CUT. The near plane is 1 world, about 1.6 local at the coil centre, and
		// dots genuinely swing between the eye and the ball every turn. Folding this
		// into the quad's SIZE collapses an over-close dot to zero AREA; fading it in
		// the fragment stage alone would still rasterize a near-plane-sized quad.
		const alive = smoothstep( 1.9, 3.4, camDist )

		// Airborne billboard, off ONE shared roll reference so the whole field agrees.
		// A per-dot reference axis rolls each rhombus independently and swings it
		// through 90 degrees wherever the reference is swapped - and a rhombus is an
		// L1 norm, so unlike a disc it is NOT rotation invariant.
		const forward = camLocal.sub( center )
		const fwd = forward.div( forward.length().max( 1e-4 ) )
		const sideRaw = upLocal.cross( fwd )
		// Guarded divide, NOT normalize(): sideRaw is exactly zero when the eye ray is
		// parallel to up, and normalize() emits NaN there.
		const side = sideRaw.div( sideRaw.length().max( 1e-4 ) )
		const up = fwd.cross( side )
		const airOffset = side.mul( positionGeometry.x.mul( airSize ) )
			.add( up.mul( positionGeometry.y.mul( airSize ) ) )
		const wallOffset = wallRadial.mul( positionGeometry.x.mul( wallSize ) )
			.add( wallTangent.mul( positionGeometry.y.mul( wallSize ) ) )

		material.positionNode = center.add( mix( airOffset, wallOffset, kind ).mul( alive ) )

		// Analytic occlusion against the unit sphere: closest approach of the eye->dot
		// ray to the origin. The z-buffer already hard-clips dots behind the ball, so
		// this exists to fade them out just BEFORE that cut rather than have them
		// vanish on a hard edge.
		const rayDir = toDot.div( camDist.max( 1e-4 ) )
		const closest = camLocal.negate().dot( rayDir )
		const perp = camLocal.add( rayDir.mul( closest ) ).length()
		const behind = smoothstep( -0.15, 0.15, camDist.sub( closest ) )
		const visible = smoothstep( 1.3, 0.98, perp ).mul( behind ).oneMinus()

		// Distance haze. The floor is generous because the field now reaches ~14 local
		// units, well past the camera, and a stricter one simply deletes the outer two
		// thirds of the loop.
		const ref = camLocal.length()
		const murk = smoothstep( ref.add( 7 ), ref.sub( 1.2 ), camDist ).mul( 0.6 ).add( 0.4 )
		// Falloff away from the emitter, which is what makes the eye trace the gradient
		// back to the BALL instead of reading the dots as free-floating confetti. Kept
		// gentle: the field is sized to the frame now, and a steep falloff would empty
		// the corners it is meant to fill.
		const attenDist = mix( rho, throwDist, kind )
		const spread = float( 1 ).div( attenDist.mul( attenDist ).mul( mix( 0.02, 0.06, kind ) ).add( 1 ) )

		// Family recovery - see the bake. Hue and motion agree because each dot gates
		// on the lamp its ramp belongs to.
		const familyA = smoothstep( 0.45, 0.55, look.y.mul( 2 ).fract() )
		const aimA = spun.dot( this.lampA ).mul( 0.5 ).add( 0.5 ).pow( 2.6 )
		const aimB = spun.dot( this.lampB ).mul( 0.5 ).add( 0.5 ).pow( 3 )
		const aim = mix( aimB, aimA, familyA ).mul( 0.84 ).add( 0.16 )

		// Wall dots fade in as their ray swings to the back of the room, and die
		// before the bowl's own edge.
		const wallGate = mix(
			float( 1 ),
			smoothstep( 0.1, 0.34, spun.z.negate() )
				.mul( smoothstep( 4.8, 3.6, wallCenter.xy.length() ) )
				.mul( this.wallGain ),
			kind
		)

		const energy = this.focus.mul( 0.75 ).add( 0.25 ).mul( this.speckleGain )
		const brightV = varying(
			spread.mul( visible ).mul( alive ).mul( envelope ).mul( aim ).mul( wallGate ).mul( murk ).mul( energy )
		)
		const rampV = varying( look.y )
		const softV = varying( kind )

		// --- fragment: shape plus one LUT tap, nothing else.
		//
		// A POINT OF LIGHT, not a painted dot: a tiny hot core sitting inside a glow
		// several times its own width. The quad grew ~1.6x while the core shrank to
		// about an eighth of the quad (it used to fill 0.62 of it), so the visible
		// point is roughly 3x smaller than before while its halo is much larger. Those
		// two moves have to happen together - shrinking the quad instead would take the
		// glow with it and just give small hard specks.
		const q = uv().sub( 0.5 ).mul( 2 )
		// Mostly round, with a hint of the rhombus a flat mirror facet throws - kept
		// low so the field reads as points of light, not four-point confetti.
		const shape = mix( q.length(), q.x.abs().add( q.y.abs() ), 0.3 )
		const coreR = mix( 0.11, 0.18, softV )
		const core = smoothstep( coreR, coreR.mul( 0.15 ), shape )
		// The glow runs all the way to the quad edge and dies exactly there, so the
		// billboard can never show its own square. pow shapes it into a bloom falloff
		// rather than a flat disc.
		const halo = smoothstep( 1, 0, shape ).pow( 3 )
		// A faint four-point flare, only on the airborne motes and only at the top of
		// their brightness envelope - the sparkle of a bright point on a lens - thin
		// enough to be a hint, never a drawn star.
		const flare = smoothstep( 0.05, 0, q.x.abs().min( q.y.abs() ) )
			.mul( smoothstep( 1, 0.15, q.length() ).pow( 2 ) )
			.mul( softV.oneMinus() )
			.mul( smoothstep( 0.35, 0.8, brightV ) )
		// The core is overdriven relative to the halo on purpose: at this size it is
		// only a few pixels across and would otherwise be antialiased into the glow,
		// leaving soft blur with no actual point in it.
		const spot = core.mul( 1.4 ).add( halo.mul( mix( 0.34, 0.48, softV ) ) ).add( flare.mul( 0.4 ) )
		const intensity = spot.mul( brightV )

		const tint = texture( res.lut, vec2( intensity.clamp( 0, 1 ).mul( 0.55 ).add( 0.3 ), rampV ) ).rgb
		material.colorNode = mix( vec3( 1, 0.97, 1 ), tint, 0.6 ).mul( intensity.mul( 2 ) )

		const mesh = new InstancedMesh( res.dotGeometry, material, DOT_COUNT )
		// The geometry's bounding sphere is a 1x1 quad at the origin, so culling would
		// drop the entire field.
		mesh.frustumCulled = false
		this.root.add( mesh )
		this._dots = mesh
		this._layers.push( { mesh, material, base: 1, order: 4 } )
	}

	// The ball itself: one analytical normal per UV tile turns the smooth sphere
	// into hundreds of flat mirrors, which the existing RoomEnvironment then
	// reflects across - no runtime lights added to the scene.
	//
	// What sells it as a MIRROR ball rather than a tiled sphere:
	//
	// - Every facet is TILTED by its own small random amount. Real tiles are glued
	//   on by hand and never sit perfectly tangent, and it is exactly that scatter
	//   that makes neighbouring tiles reflect different parts of the room - one
	//   near-black, the next blown out - and makes the ball TWINKLE as it turns,
	//   because each tile crosses the lamps' reflection on its own schedule. A
	//   perfectly regular grid reflects the environment as a smooth gradient with a
	//   grout pattern drawn over it, which is the "grey golf ball" read.
	// - Dense grid, thin dark grout: the tile count is what says "disco ball" from
	//   across the room, and thick grout reads as a checkerboard.
	// - Slight per-tile bevel sheen (brighter toward one corner) so each tile reads
	//   as a piece of glass with a facing, not as a flat swatch of colour.
	_buildSphere( sphereGeometry ) {
		const material = new MeshStandardNodeMaterial( {
			transparent: true,
			opacity: 0,
			depthWrite: true,
			depthTest: true,
			envMapIntensity: 2.1,
		} )
		material.name = 'Schedule Afterparty disco face'
		const faceUV = uv()
		const grid = vec2( FACET_COLS, FACET_ROWS )
		const gridUV = faceUV.mul( grid )
		const tileID = gridUV.floor()
		const tileFrac = gridUV.fract()
		const tileCenter = tileID.add( 0.5 ).div( grid )
		const theta = tileCenter.y.oneMinus().mul( Math.PI )
		const phi = tileCenter.x.mul( Math.PI * 2 )
		const thetaRing = theta.sin()
		const facetBase = vec3(
			thetaRing.mul( phi.cos() ).negate(),
			theta.cos(),
			thetaRing.mul( phi.sin() )
		)
		const tileKey = uint( tileID.y ).mul( uint( FACET_COLS ) ).add( uint( tileID.x ) )
		const tileHash = hash( tileKey )
		const tileHash2 = hash( tileKey.add( uint( 17 ) ) )
		const tileHash3 = hash( tileKey.add( uint( 101 ) ) )
		const tileHash4 = hash( tileKey.add( uint( 211 ) ) )
		// Per-tile tilt in the tile's own tangent frame. `tangent` is d/dphi of the
		// sphere at the tile centre (normalised), `bitangent` completes the frame.
		const tangent = vec3( phi.sin(), 0, phi.cos() )
		const bitangent = facetBase.cross( tangent )
		const facetLocal = facetBase
			.add( tangent.mul( tileHash3.sub( 0.5 ).mul( this.facetJitter ) ) )
			.add( bitangent.mul( tileHash4.sub( 0.5 ).mul( this.facetJitter ) ) )
			.normalize()
		const facetWorld = modelNormalMatrix.mul( facetLocal ).normalize()
		const facetView = facetWorld.transformDirection( cameraViewMatrix )

		const cleanGridLine = coord => {
			const distance = float( 0.5 ).sub( coord.fract().sub( 0.5 ).abs() )
			const aa = fwidth( coord ).clamp( 1e-6, 0.5 )
			const halfWidth = float( FACET_GROUT )
			const drawWidth = aa.max( halfWidth )
			return smoothstep( drawWidth.add( aa ), drawWidth.sub( aa ), distance )
				.mul( halfWidth.div( drawWidth ).min( 1 ) )
		}
		const tileBody = cleanGridLine( gridUV.x ).max( cleanGridLine( gridUV.y ) ).oneMinus()
		// Bevel sheen: a soft diagonal ramp across each tile, direction chosen per tile
		// so the whole ball does not carry one uniform "lit from the top-left" bias.
		const bevelDir = tileHash3.mul( 6.2831853 )
		const bevel = tileFrac.sub( 0.5 ).dot( vec2( bevelDir.cos(), bevelDir.sin() ) ).mul( 0.5 ).add( 0.5 )
		const sheen = mix( 0.8, 1.2, bevel )
		// Wide per-tile albedo spread, biased dark: a mirror ball is mostly tiles
		// reflecting a dark room with a scatter of hot ones, not an even silver skin.
		// `roomLight` is a broad directional bias (facets aimed up and toward the
		// viewer's left read brighter, as if that side of the room were the lit one)
		// so the mosaic keeps a global shading on top of the per-tile scatter.
		const roomLight = facetWorld.dot( vec3( -0.35, 0.6, 0.72 ) ).mul( 0.5 ).add( 0.5 )
		const silver = mix( color( '#3A4262' ), color( '#FFFFFF' ), tileHash.pow( 1.35 ) )
			.mul( sheen )
			.mul( mix( 0.55, 1.25, roomLight ) )
		material.colorNode = mix( color( '#07091A' ), silver, tileBody )
		material.normalNode = facetView
		material.metalnessNode = mix( 0.05, 1, tileBody )
		// Mostly hard mirrors, with a scatter of slightly hazier tiles so the ball
		// keeps some body between the flashes.
		material.roughnessNode = mix( 0.72, mix( 0.03, 0.2, tileHash2.pow( 2 ) ), tileBody )

		// The SAME two lamps the beams and the dots gate on, so the facets that flash,
		// the beams that are brightest and the live zones of the dot field all pulse
		// together instead of on three unrelated clocks. Exponents are HIGH: a mirror
		// tile is either throwing the lamp straight at you or it is not.
		const viewDirection = cameraPosition.sub( positionWorld ).normalize()
		const specularA = viewDirection
			.dot( reflect( this.lampA.negate(), facetWorld ).normalize() )
			.max( 0 )
			.pow( 90 )
			.mul( facetWorld.dot( this.lampA ).max( 0 ) )
		const specularB = viewDirection
			.dot( reflect( this.lampB.negate(), facetWorld ).normalize() )
			.max( 0 )
			.pow( 70 )
			.mul( facetWorld.dot( this.lampB ).max( 0 ) )
		const cueWave = this.time.mul( tileHash2.mul( 2.4 ).add( 2.2 ) )
			.add( tileHash.mul( Math.PI * 2 ) )
			.sin()
			.mul( 0.5 )
			.add( 0.5 )
		const sparseCue = smoothstep( 0.88, 0.995, cueWave )
		const peakFocus = this.focus.pow( 3 )
		const directionalCue = specularA.add( specularB ).min( 1 )
		const glintGain = this.glintGain
		const cyanGlint = color( '#79E7FF' ).mul( specularA.mul( this.focus.mul( 1.4 ).add( 0.9 ) ) )
		const pinkGlint = color( '#FF82E3' ).mul( specularB.mul( this.focus.mul( 1.2 ).add( 0.8 ) ) )
		// The hot white pops: a tile that has just swung its lamp reflection through
		// the eye. Directional so they trace the lamps around the ball, plus a small
		// direction-free floor so the sparkle never fully stops on the far side.
		const whiteFlash = color( '#FFFBE8' ).mul(
			sparseCue.mul( directionalCue.mul( peakFocus.mul( 3.6 ).add( 0.6 ) ).add( 0.14 ) )
		)
		// A faint room reflection tinted by the rig's own colours, so the tiles that
		// are not flashing still sit in the SAME light as the beams. Facets aimed up
		// toward the lamps pick up violet, facets aimed down stay steel. Kept low:
		// past this it flattens the mosaic into one lavender skin.
		const wash = mix( color( '#0E0D24' ), color( '#2E2160' ), facetWorld.y.mul( 0.5 ).add( 0.5 ) )
			.mul( this.focus.mul( 0.35 ).add( 0.1 ) )
		// Silhouette rim. Without it the mirror dissolves into its own light exactly
		// when the rig is brightest - positionGeometry IS the unit normal on this
		// sphere, and the analytical facet normal has already taken over normalNode.
		const smoothWorld = modelNormalMatrix.mul( positionGeometry ).normalize()
		const rim = smoothWorld.dot( viewDirection ).max( 0 ).oneMinus().pow( 2.6 )
			.mul( this.focus.mul( 0.3 ).add( 0.18 ) )
		material.emissiveNode = cyanGlint.add( pinkGlint ).add( whiteFlash ).mul( glintGain ).add( wash ).mul( tileBody )
			.add( color( '#B9E4FF' ).mul( rim ) )

		const mesh = new Mesh( sphereGeometry, material )
		mesh.frustumCulled = false
		this.root.add( mesh )
		this.sphere = mesh
		this.sphereMaterial = material
	}

	// The cable the ball hangs from, plus its mount cap. Purely a read: a sphere
	// floating in space is a planet, a sphere on a wire is a disco ball. Normal
	// blending, dark, fades with the prop's fog like the ring text does. Sits OUTSIDE
	// the spinning sphere so it stays still while the mirror turns under it.
	_buildCable() {
		const material = new MeshBasicNodeMaterial( {
			transparent: true,
			opacity: 0,
			depthWrite: false,
			depthTest: true,
			forceSinglePass: true,
			toneMapped: false,
		} )
		material.name = 'Schedule Afterparty cable'
		// Fade toward the top so the wire dissolves into the sky instead of ending on
		// a hard cut, and pick up a little of the rig's light near the mount.
		const along = uv().y
		const glow = smoothstep( 0.35, 0, along ).mul( this.focus.mul( 0.5 ).add( 0.1 ) )
		material.colorNode = mix( color( '#1A1730' ), color( '#7A6FB4' ), glow )
		material.opacityNode = smoothstep( 0.9, 0.4, along ).mul( materialOpacity )

		const group = new Group()
		const cable = new Mesh( this._res.cableGeometry, material )
		cable.frustumCulled = false
		group.add( cable )
		const cap = new Mesh( this._res.capGeometry, material )
		cap.frustumCulled = false
		group.add( cap )
		this.root.add( group )
		this._cable = group
		this._layers.push( { mesh: group, material, base: 0.9, order: 2, solid: true } )
	}

	// A soft additive halo behind the ball: the bloom this postFX chain does not
	// have. Camera-facing, gated on focus, LUT-tinted, breathing with the lamps so
	// it reads as light spilling around the mirror rather than as a painted disc.
	_buildHalo() {
		const material = additiveMaterial( 'Schedule Afterparty halo' )
		const res = this._res
		const camLocal = modelWorldMatrixInverse.mul( vec4( cameraPosition, 1 ) ).xyz
		const upLocal = modelWorldMatrixInverse.mul( vec4( 0, 1, 0, 0 ) ).xyz
		// Billboard sitting a little BEHIND the ball centre along the eye ray, so the
		// sphere's depth carves the disc and the glow only shows around the rim.
		const fwd = camLocal.div( camLocal.length().max( 1e-4 ) )
		const sideRaw = upLocal.cross( fwd )
		const side = sideRaw.div( sideRaw.length().max( 1e-4 ) )
		const up = fwd.cross( side )
		const size = float( HALO_SIZE ).mul( this.focus.mul( 0.5 ).add( 0.6 ) )
		material.positionNode = fwd.mul( -0.35 )
			.add( side.mul( positionGeometry.x.mul( size ) ) )
			.add( up.mul( positionGeometry.y.mul( size ) ) )

		const q = uv().sub( 0.5 ).mul( 2 )
		const r = q.length()
		// Two lobes on the two lamps' azimuths, so the halo leans toward whichever
		// side is currently lit, on top of a faint even glow.
		const ang = atan( q.y, q.x )
		const lobeA = ang.sub( this.time.mul( 0.83 ) ).cos().mul( 0.5 ).add( 0.5 ).pow( 2 )
		const lobeB = ang.add( this.time.mul( 0.71 ) ).cos().mul( 0.5 ).add( 0.5 ).pow( 2 )
		const falloff = smoothstep( 1, 0.05, r ).pow( 1.8 )
		const intensity = falloff.mul( lobeA.mul( 0.5 ).add( lobeB.mul( 0.5 ) ).mul( 0.7 ).add( 0.3 ) )
			.mul( this.focus.mul( 0.8 ).add( 0.2 ) ).mul( this.haloGain ).mul( 1.4 )
		const tint = mix(
			rampAtV( res.lut, intensity, RAMP_V[1] ),
			rampAtV( res.lut, intensity, RAMP_V[0] ),
			lobeB.div( lobeA.add( lobeB ).max( 1e-3 ) )
		)
		material.colorNode = tint.mul( intensity ).add( grainNode( uv(), this.time, 0.01 ) )

		const mesh = new Mesh( res.quad, material )
		mesh.frustumCulled = false
		this.root.add( mesh )
		this._halo = mesh
		// Draws right after the sphere so its depth carves the disc's centre.
		this._layers.push( { mesh, material, base: 0.75, order: 1 } )
	}

	reset() {
		this.root.visible = false
		this.time.value = 0
		this.focus.value = 0
		this.projCS.value.set( 1, 0 )
		this.sphere.rotation.set( 0, 0, 0 )
		this.sphereMaterial.opacity = 0
		this._backdrop.scale.setScalar( BACKDROP_SIZE )
		for ( const layer of this._layers ) {
			layer.material.opacity = 0
			layer.mesh.visible = true
		}
	}

	hide() {
		this.root.visible = false
		for ( const layer of this._layers ) layer.material.opacity = 0
		this.sphereMaterial.opacity = 0
	}

	/**
	 * @param {number} spin  shared rotation phase (also the rig's clock)
	 * @param {number} fade  the prop's fog opacity
	 * @param {number} focus 0..1 proximity to the center of the schedule
	 * @param {number} renderOrder base render order of the prop
	 * @param {boolean} reducedMotion freeze everything that moves
	 * @param {object} gains live tweak multipliers - every key must be present:
	 *   intensity, ray, speckle, beamReach, beamWidth, dotCount, wallGain, projSpin,
	 *   facetJitter, glintGain, haloGain, lightsIn, lightsFull
	 */
	update( spin, fade, focus, renderOrder, reducedMotion, gains ) {
		this.root.visible = true
		const approach = Math.max( 0, Math.min( 1, focus ) )
		const peak = approach * approach * approach
		this.time.value = spin
		this.focus.value = approach
		this.rayGain.value = gains.ray
		this.speckleGain.value = gains.speckle
		this.beamReach.value = gains.beamReach
		this.beamWidth.value = gains.beamWidth
		this.wallGain.value = gains.wallGain
		this.facetJitter.value = gains.facetJitter
		this.glintGain.value = gains.glintGain
		this.haloGain.value = gains.haloGain

		// Reduced motion needs no branch of its own: BallProp.place() already feeds a
		// per-item CONSTANT as `spin`, and every animated quantity in the rig derives
		// from that one value, so the whole thing settles into a still, correctly
		// composed 3D pose rather than a degenerate rotation-zero one.
		const ballSpin = spin * 1.02
		this.sphere.rotation.set( 0, ballSpin, 0 )
		const proj = ballSpin * gains.projSpin
		this.projCS.value.set( Math.cos( proj ), Math.sin( proj ) )

		const pa = spin * 0.83
		this.lampA.value.set(
			Math.cos( pa ) * 0.92,
			Math.sin( pa * 0.37 ) * 0.18 + 0.42,
			Math.sin( pa ) * 0.92
		).normalize()
		const pb = spin * -0.71 + 2.1
		this.lampB.value.set(
			Math.cos( pb ) * 0.82,
			Math.cos( pb * 0.51 ) * 0.16 + 0.58,
			Math.sin( pb ) * 0.82
		).normalize()

		const breathe = reducedMotion ? 1 : 0.97 + Math.sin( spin * 0.9 ) * 0.03
		this._backdrop.scale.setScalar( BACKDROP_SIZE * breathe )
		// Density knob. The Fibonacci bake is keyed on buffer capacity, so any prefix
		// is still an evenly covered shell with both dot populations present - nothing
		// moves as this changes.
		this._dots.count = Math.max( 12, Math.round( DOT_COUNT * gains.dotCount ) )

		this.sphereMaterial.opacity = fade
		// The ball writes depth so it can carve the beams and the far half of the dot
		// cloud. At the far end of the coil `fade` is ~0.05, and an all-but-invisible
		// ball would still punch a ball-shaped hole through the light behind it. The
		// old flat speckle quad sat in FRONT of the sphere, so this failure mode is
		// new with the 3D field.
		this.sphereMaterial.depthWrite = fade > 0.05
		this.sphere.renderOrder = renderOrder
		// THE GATE. The light show belongs to the Afterparty alone: it fades in over
		// the last stretch of the ball's approach to the centre and is fully out by the
		// time a neighbouring card is centred (a neighbour sits at focus ~0.42, so the
		// window starts above that). Below the gate the mirror ball is just a mirror
		// ball - facets, cable, glints - with no rig around it. `lit` also leads with
		// the backdrop so the room has sunk into dusk before the first shaft reads.
		const lit = smooth01( ( approach - gains.lightsIn ) / Math.max( 1e-3, gains.lightsFull - gains.lightsIn ) )
		// The bowl TRAILS the gate (lit squared): the host dims its sky on `lit`, and
		// a dark disc arriving over a still-bright sky reads as a brown circle with a
		// rim. By the time the bowl is really there the room is already dusk.
		this._layers[0].material.opacity = fade * lit * lit * ( 0.62 + peak * 0.38 ) * this._layers[0].base
		const ramp = fade * lit * ( 0.7 + peak * 0.3 ) * gains.intensity
		for ( let i = 1; i < this._layers.length; i++ ) {
			const layer = this._layers[i]
			// Solid props (the cable) fade with the ball itself, like the ring text;
			// only the additive light layers ride the gate.
			layer.material.opacity = ( layer.solid ? fade : ramp ) * layer.base
		}
		for ( const layer of this._layers ) {
			layer.mesh.renderOrder = renderOrder + layer.order
			layer.mesh.visible = layer.material.opacity > 0.004
		}
	}

	dispose() {
		for ( const layer of this._layers ) layer.material.dispose()
		this.sphereMaterial.dispose()
		this.root.removeFromParent()
		releaseResources()
	}
}

```


